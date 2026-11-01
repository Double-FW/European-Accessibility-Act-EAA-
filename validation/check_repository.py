#!/usr/bin/env python3
"""Read-only repository checks and synthetic fixtures. No external requests or approvals."""
import argparse
import copy
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit
try:
    import yaml
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:
    print(f'DEPENDENCY_ERROR: {exc}. Install PyYAML==6.0.3 jsonschema==4.26.0 in your environment.', file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
KINDS = {'source','jurisdiction','applicability','requirement','mapping','test_execution','evidence',
         'outcome_finding','issue','legal_limitation','delegation','approval','conformity_conclusion',
         'public_claim','monitoring_event'}
ATLF = {'Pass','Fail','Cannot tell','Not applicable','Not tested','Blocked','Tool error'}
QA_MAP = {'Pass':'Pass','Fail':'Fail','Not applicable':'Not applicable','Not run':'Not tested','Needs review':'Cannot tell'}
CODES = set()

def load(path):
    text = (ROOT/path).read_text(encoding='utf-8')
    return json.loads(text) if str(path).endswith('.json') else yaml.safe_load(text)

def same_scope(a, b):
    return a == b

def record_errors(records, schema, sources, workflow_ids, as_of):
    """Structural and selected relational/business checks; not legal or authenticity validation."""
    errors = []
    def err(code, rid, reason):
        errors.append({'code': code, 'record': rid, 'reason': reason})
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    index = {}
    for record in records:
        rid = record.get('id', '<missing>') if isinstance(record, dict) else '<non-object>'
        found = list(validator.iter_errors(record))
        if found:
            for e in found[:4]:
                err('SCHEMA', rid, str(list(e.absolute_path))+': '+e.message)
            continue
        if rid in index:
            err('DUPLICATE_ID', rid, 'Record IDs must be unique.')
        index[rid] = record
    def ref(r, target, expected=None):
        if target not in index:
            err('DANGLING_REFERENCE', r['id'], f'Unknown record {target}')
            return None
        value = index[target]
        if expected and value['kind'] not in expected:
            err('REFERENCE_KIND', r['id'], f'{target} has kind {value["kind"]}, expected {sorted(expected)}')
        if not r['synthetic'] and value['synthetic']:
            err('SYNTHETIC_LEAK', r['id'], f'Real record cannot rely on synthetic {target}')
        return value
    for r in index.values():
        rid, kind, d = r['id'], r['kind'], r['data']
        for sid in r['source_ids']:
            if sid not in sources: err('SOURCE_REFERENCE', rid, f'Unknown source {sid}')
        for evid in r['evidence_refs']: ref(r, evid, {'evidence'})
        for rel in r['relationships']: ref(r, rel['target'])
        if kind == 'jurisdiction' and r['status'] == 'approved' and not d['national_law_refs']:
            err('LEGAL_CONTEXT', rid, 'Approved jurisdiction needs national law.')
        if kind == 'applicability':
            for key, expected in [('jurisdiction_refs', {'jurisdiction'}), ('legal_limitation_refs', {'legal_limitation'})]:
                for target in d[key]: ref(r, target, expected)
            if r['status'] == 'approved' and d['scope_decision'] == 'legal review required':
                err('LEGAL_CONTEXT', rid, 'Unresolved legal route cannot be approved scope.')
            if d['legal_limitation_status'] == 'one or more limitations recorded' and not d['legal_limitation_refs']:
                err('LIMITATION_LINK', rid, 'Claimed limitation needs a separate record.')
        if kind == 'requirement': ref(r, d['applicability_ref'], {'applicability'})
        if kind == 'mapping':
            ref(r, d['requirement_ref'], {'requirement'})
            if d['source_id'] not in sources: err('SOURCE_REFERENCE', rid, 'Mapping source not registered.')
        if kind == 'test_execution':
            ref(r, d['requirement_ref'], {'requirement'})
            ref(r, d['procedure_ref'], {'mapping'})
            if d['source_vocabulary'] == 'ATLF-1.1': expected = d['source_result'] if d['source_result'] in ATLF else None
            else:
                expected = QA_MAP.get(d['source_result'])
                if d['source_result'] == 'Blocked':
                    expected = 'Tool error' if d['cause'] == 'tool_failure' else 'Blocked'
                    if not d['cause']: err('MISSING_CAUSE', rid, 'Blocked adapter needs its recorded cause.')
            if not expected or d['normalised_result'] != expected:
                err('RESULT_ADAPTER', rid, 'Source and normalised results do not match the explicit adapter.')
            if not d['assumptions_met'] and d['normalised_result'] in {'Pass','Not applicable'}:
                err('INVALID_ASSESSMENT', rid, 'Invalid test assumptions cannot establish pass or non-applicability.')
            if not d['precondition_met'] and d['normalised_result'] == 'Pass':
                err('INVALID_ASSESSMENT', rid, 'False requirement precondition cannot produce a pass.')
            if d['normalised_result'] in {'Pass','Fail'} and not r['evidence_refs']:
                err('EXECUTION_EVIDENCE', rid, 'A conclusive execution requires evidence.')
            if d['normalised_result'] == 'Pass' and not d['coverage_complete']:
                err('INCOMPLETE_COVERAGE', rid, 'Incomplete declared execution coverage cannot be a complete pass.')
        if kind == 'evidence':
            for target in d['supports_refs']+d['contradicts_refs']: ref(r, target)
            if r['synthetic'] != (d['authenticity'] == 'synthetic'):
                err('SYNTHETIC_LABEL', rid, 'Evidence authenticity and synthetic marker disagree.')
        if kind == 'issue':
            for target in d['requirement_refs']: ref(r, target, {'requirement'})
            for target in d['retest_refs']: ref(r, target, {'test_execution'})
            if d['resolution'] == 'verified_corrected':
                retests = [index.get(x) for x in d['retest_refs']]
                if not retests or any(not x or x['data'].get('normalised_result') != 'Pass' for x in retests):
                    err('RETEST_REQUIRED', rid, 'Verified correction requires passing linked retest evidence.')
            if d['category'] == 'exception' and not d['expires_on']:
                err('EXCEPTION_EXPIRY', rid, 'Temporary exception must expire.')
            if d['resolution'] == 'accepted_unresolved' and not r.get('approval_ref'):
                err('APPROVAL_REQUIRED', rid, 'Accepted unresolved issue needs authorised decision.')
            if d['resolution'] == 'accepted_unresolved' and d['expires_on'] and d['expires_on'] < as_of:
                err('EXPIRED_EXCEPTION', rid, 'Accepted exception has expired.')
        if kind == 'legal_limitation':
            for target in d['affected_requirements']: ref(r, target, {'requirement'})
        if kind == 'delegation':
            if d['valid_from'] > d['valid_until']: err('DATE_ORDER', rid, 'Delegation validity is reversed.')
        if kind == 'approval':
            target = ref(r, d['target_ref'])
            if target:
                if target['version'] != d['target_version'] or not same_scope(target['scope'], d['approved_scope']):
                    err('APPROVAL_BINDING', rid, 'Approval version/scope differs from its target.')
                if target['synthetic'] != r['synthetic']:
                    err('SYNTHETIC_LEAK', rid, 'Approval and target synthetic status must agree.')
                if target['kind'] == 'public_claim' and target['data']['artifact_hash'] != d['artifact_hash']:
                    err('APPROVAL_BINDING', rid, 'Approved claim hash differs.')
            if d['approved_on'] > d['valid_until']: err('DATE_ORDER', rid, 'Approval validity is reversed.')
            if d['delegation_ref']: ref(r, d['delegation_ref'], {'delegation'})
        if kind == 'conformity_conclusion':
            app = ref(r, d['applicability_ref'], {'applicability'})
            reqs = d['requirement_ids']
            for target in reqs: ref(r, target, {'requirement'})
            supplied = [c['requirement_ref'] for c in d['requirement_conclusions']]
            if set(supplied) != set(reqs) or len(supplied) != len(set(supplied)):
                err('REQUIREMENT_COVERAGE', rid, 'Exactly one conclusion per declared requirement is required.')
            positive = d['overall_decision'] == 'supported within stated scope'
            for c in d['requirement_conclusions']:
                ref(r, c['requirement_ref'], {'requirement'})
                executions = [ref(r, x, {'test_execution'}) for x in c['execution_refs']]
                for target in c['outcome_refs']: ref(r, target, {'outcome_finding'})
                if positive:
                    if c['result'] != 'supported as met':
                        err('UNSUPPORTED_POSITIVE', rid, 'Positive aggregate contains an unmet or unresolved requirement.')
                    if not executions or any(not x or x['data'].get('normalised_result') != 'Pass' or x['scope'] != r['scope'] for x in executions):
                        err('UNSUPPORTED_POSITIVE', rid, 'Positive requirement needs passing assessment in its scope; outcomes alone do not suffice.')
            if positive:
                if not app or app['status'] != 'approved' or app['scope'] != r['scope']:
                    err('LEGAL_CONTEXT', rid, 'Positive conclusion requires approved applicability for this exact scope.')
                if not d['contradictions_resolved'] or not d['evidence_complete'] or d['legal_review_required']:
                    err('UNSUPPORTED_POSITIVE', rid, 'Contradictory, incomplete or legally unresolved evidence blocks positive conclusion.')
                if not r['evidence_refs']: err('UNSUPPORTED_POSITIVE', rid, 'Positive conclusion needs evidence.')
                for evid in r['evidence_refs']:
                    e=index.get(evid)
                    if e and (not e['data'].get('current') or e['data'].get('contradicts_refs')):
                        err('UNSUPPORTED_POSITIVE', rid, 'Stale or unresolved contradictory evidence cannot support this positive conclusion.')
        if kind == 'public_claim':
            conf = ref(r, d['conformity_ref'], {'conformity_conclusion'})
            actual_hash=hashlib.sha256(d['exact_wording'].encode('utf-8')).hexdigest()
            if actual_hash != d['artifact_hash']: err('CLAIM_HASH', rid, 'Exact wording has changed or hash is wrong.')
            if r['status'] in {'approved','published'} or d['publication_state'] in {'handoff_ready','published'}:
                if r['status'] not in {'approved','published'}: err('APPROVAL_REQUIRED', rid, 'Handoff/publication needs an approved claim record.')
                if not conf or conf['status'] != 'approved' or conf['data'].get('overall_decision') != 'supported within stated scope' or conf['scope'] != r['scope']:
                    err('UNSUPPORTED_CLAIM', rid, 'Claim must match an approved supported conclusion and exact scope.')
                delegation = ref(r,d['publication_authority_ref'],{'delegation'}) if d['publication_authority_ref'] else None
                if not delegation:
                    err('PUBLICATION_AUTHORITY', rid, 'No publication/handoff authority.')
                else:
                    dd=delegation['data']
                    op='publish_claim' if d['publication_state']=='published' else 'handoff_claim'
                    if delegation['status']!='approved' or dd['revoked'] or not dd['valid_from']<=as_of<=dd['valid_until'] or op not in dd['operations'] or delegation['scope']!=r['scope']:
                        err('PUBLICATION_AUTHORITY', rid, 'Operation outside active delegation, validity or scope.')
        if kind == 'monitoring_event':
            for target in d['affected_refs']: ref(r, target)
            if d['next_workflow'] not in workflow_ids: err('WORKFLOW_REFERENCE', rid, 'Unknown next workflow.')
        if r['status'] in {'approved','published'} or r.get('approval_ref'):
            approval = ref(r, r.get('approval_ref',''), {'approval'})
            if not approval: err('APPROVAL_REQUIRED', rid, 'Missing approval record.')
            else:
                ad=approval['data']
                if approval['status']!='recorded' or ad['target_ref']!=rid or ad['target_version']!=r['version'] or ad['approved_scope']!=r['scope'] or not ad['approved_on']<=as_of<=ad['valid_until']:
                    err('APPROVAL_BINDING', rid, 'Approval missing, inactive, expired or for a different target/version/scope.')
    return errors

# Decision helper is intentionally limited: a recommendation, not an orchestration or legal engine.
def route(signals):
    if signals.get('missing_national_law') or signals.get('scope_unresolved'):
        return {'workflow':'WF02','state':'blocked','conclusion':'legal review required'}
    if signals.get('unapproved_claim') or signals.get('expired_delegation') or signals.get('claim_changed'):
        return {'workflow':'WF08','state':'blocked','conclusion':'cannot publish'}
    if signals.get('superseded_source'):
        return {'workflow':'WF01','state':'blocked','conclusion':'cannot conclude'}
    if signals.get('invalid_assumptions'):
        return {'workflow':'WF05','state':'blocked','conclusion':'cannot conclude'}
    if signals.get('technical_failure') or signals.get('journey_failure') or signals.get('severe_minority_barrier'):
        return {'workflow':'WF09','state':'running','conclusion':'not supported'}
    if signals.get('inaccessible_complaints') or signals.get('contradiction'):
        return {'workflow':'WF09','state':'running','conclusion':'cannot conclude'}
    if signals.get('supplier_declaration_only'):
        return {'workflow':'WF04','state':'blocked','conclusion':'cannot conclude'}
    if signals.get('approved_complete_case'):
        return {'workflow':'WF08','state':'awaiting_approval','conclusion':'prepare controlled handoff'}
    return {'workflow':'WF07','state':'blocked','conclusion':'cannot conclude'}

def transition_errors(event, workflows):
    errors=[]
    def bad(code):errors.append({'code':code,'record':event.get('workflow','unknown'),'reason':'Invalid workflow transition instance.'})
    wf=next((w for w in workflows['workflows'] if w['id']==event.get('workflow')),None)
    step=next((s for s in wf['steps'] if s['id']==event.get('step')),None) if wf else None
    if not step:bad('WORKFLOW_REFERENCE');return errors
    tr=next((t for t in workflows['transitions'] if t['from']==event.get('from') and t['to']==event.get('to')),None)
    if not tr:bad('INVALID_TRANSITION');return errors
    if tr['requires_evidence'] and not event.get('evidence_refs'):bad('TRANSITION_EVIDENCE')
    if event.get('to')=='completed':
        if not set(step['depends_on']).issubset(event.get('completed_step_ids',[])):bad('STEP_DEPENDENCY')
        if step['approval_required'] or tr['requires_human_approval']:
            if not event.get('approval_verified'):bad('TRANSITION_APPROVAL')
            if event.get('from')!='awaiting_approval':bad('INVALID_TRANSITION')
    if event.get('from')=='blocked' and event.get('to')=='running' and not event.get('dependency_resolved'):bad('UNRESOLVED_DEPENDENCY')
    if event.get('to')=='running' and not event.get('authority_valid'):bad('ACTION_AUTHORITY')
    return errors

def anchors(text):
    used={}; result=set()
    text=re.sub(r'```.*?```','',text,flags=re.S)
    for title in re.findall(r'^#{1,6}\s+(.+)$',text,re.M):
        slug=re.sub(r'[^\w -]','',title.lower()).replace(' ','-')
        n=used.get(slug,0);used[slug]=n+1
        result.add(slug if not n else slug+'-'+str(n))
    return result

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--records',help='Validate a supplied YAML bundle of records in addition to repository fixtures.')
    parser.add_argument('--as-of',default=None,help='YYYY-MM-DD for supplied records; defaults to current date.')
    args=parser.parse_args()
    failures=[]; stats={}
    def fail(code,message):failures.append(f'{code}: {message}')
    try:
        docs=load('control/document-index.yaml'); sr=load('control/source-register.yaml'); wf=load('workflows/workflows.yaml')
        schema=load('records/record.schema.json'); wfschema=load('workflows/workflow.schema.json')
        example=load('examples/synthetic-service-cycle.yaml'); cases=load('validation/cases.yaml')
        remediation=load('control/remediation-register.yaml'); standards=load('control/standards-status.yaml')
        # Parse every structured source, not only the known registries.
        parsed=[p for p in ROOT.rglob('*') if p.suffix in {'.json','.yaml','.yml'}]
        for p in parsed:load(p.relative_to(ROOT))
        stats['structured_files']=len(parsed)
        Draft202012Validator.check_schema(schema);Draft202012Validator.check_schema(wfschema)
        for e in Draft202012Validator(wfschema,format_checker=FormatChecker()).iter_errors(wf):fail('WORKFLOW_SCHEMA',e.message)
        source_ids=[s['id'] for s in sr['sources']]; source_set=set(source_ids)
        if len(source_set)!=len(source_ids):fail('DUPLICATE_ID','Duplicate source IDs')
        workflow_ids=[w['id'] for w in wf['workflows']];workflow_set=set(workflow_ids)
        if len(workflow_set)!=len(workflow_ids):fail('DUPLICATE_ID','Duplicate workflow IDs')
        guide_ids={d['document_id'] for d in docs['documents']}
        for w in wf['workflows']:
            if w['guide_id'] not in guide_ids:fail('GUIDE_REFERENCE',w['id'])
            ids=[s['id'] for s in w['steps']]
            if len(set(ids))!=len(ids):fail('DUPLICATE_ID',w['id']+' steps')
            seen=set()
            for step in w['steps']:
                if not set(step['depends_on']).issubset(seen):fail('STEP_DEPENDENCY',step['id']+' has missing/cyclic/forward dependencies')
                seen.add(step['id'])
        markdown=list(ROOT.rglob('*.md'));stats['markdown_files']=len(markdown)
        for p in markdown:
            text=p.read_text(); rel=p.relative_to(ROOT)
            if text.count('```')%2:fail('MARKDOWN_FENCE',str(rel))
            for raw in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',text):
                target=raw.strip('<>');u=urlsplit(target)
                if u.scheme or u.netloc:continue
                dest=(p.parent/unquote(u.path)).resolve() if u.path else p
                if not dest.is_relative_to(ROOT):fail('LINK_ESCAPE',str(rel)+' -> '+raw);continue
                if not dest.is_file():fail('LOCAL_LINK',str(rel)+' -> '+raw);continue
                if u.fragment and dest.suffix=='.md' and unquote(u.fragment) not in anchors(dest.read_text()):fail('ANCHOR',str(rel)+' -> '+raw)
        for d in docs['documents']:
            p=ROOT/d['path'];text=p.read_text()
            if not text.startswith('---\n'):fail('METADATA',d['path']);continue
            fm=yaml.safe_load(text.split('---',2)[1])
            for key in ['document_id','version','status','authority_type','review_date','source_ids','prerequisites','output_record_types']:
                if key not in fm or fm[key]!=d.get(key):fail('METADATA',d['path']+' field '+key)
            if not set(fm['source_ids']).issubset(source_set):fail('SOURCE_REFERENCE',d['path'])
            if not set(d['anchors']).issubset(anchors(text)):fail('ANCHOR',d['path']+' index anchors')
            if not set(fm['output_record_types']).issubset(KINDS):fail('RECORD_KIND',d['path'])
        findings=remediation['findings'];fids=[f['id'] for f in findings]
        if len(fids)!=36 or set(fids)!={f'R{i:02d}' for i in range(1,37)}:fail('REMEDIATION_COVERAGE','Expected exactly R01–R36')
        for f in findings:
            if not f['rationale'] or not f['validation'] or not f['source_ids']:fail('REMEDIATION_EVIDENCE',f['id'])
            if not set(f['source_ids']).issubset(source_set):fail('SOURCE_REFERENCE',f['id'])
            for loc in f['output_locations']:
                p,_,anchor=loc.partition('#');dest=ROOT/p
                if not dest.is_file() or (anchor and anchor not in anchors(dest.read_text())):fail('REMEDIATION_LOCATION',f['id']+' '+loc)
            if f['priority']=='P0' and f['disposition']=='blocked' and remediation['ready_for_operational_use']:fail('P0_READINESS',f['id'])
        for e in record_errors(example['records'],schema,source_set,workflow_set,example['as_of']):fail(e['code'],e['record']+': '+e['reason'])
        fixture_ids=[c['id'] for c in cases['cases']]
        if len(set(fixture_ids))!=len(fixture_ids):fail('DUPLICATE_ID','Duplicate fixture IDs')
        if len(guide_ids)!=len(docs['documents']):fail('DUPLICATE_ID','Duplicate guide IDs')
        if len(guide_ids)!=6:fail('GUIDE_COUNT','Expected six canonical guides')
        passed=0
        for case in cases['cases']:
            if case['mode']=='routing':
                actual=route(case['signals'])
                if actual!=case['expected']:fail('FIXTURE',case['id']+' expected routing mismatch');continue
                if actual['conclusion'] in case['prohibited_conclusions']:fail('FIXTURE',case['id']+' prohibited conclusion');continue
            elif case['mode']=='record_mutation':
                records=copy.deepcopy(example['records'])
                for mutation in case['mutations']:
                    r=next(x for x in records if x['id']==mutation['record_id']);parts=mutation['path'].split('.')
                    for key in parts[:-1]:r=r[int(key)] if isinstance(r,list) else r[key]
                    last=parts[-1]
                    if mutation.get('delete'):
                        if isinstance(r,list):del r[int(last)]
                        else:del r[last]
                    else:
                        if isinstance(r,list):r[int(last)]=mutation['value']
                        else:r[last]=mutation['value']
                errors=record_errors(records,schema,source_set,workflow_set,example['as_of']);codes={x['code'] for x in errors}
                if not set(case['expected_error_codes']).issubset(codes):fail('FIXTURE',case['id']+f' missing errors {case["expected_error_codes"]}; got {sorted(codes)}');continue
            elif case['mode']=='transition':
                codes={e['code'] for e in transition_errors(case['event'],wf)}
                if codes!=set(case['expected_error_codes']):fail('FIXTURE',case['id']+f' transition errors {sorted(codes)}');continue
            else:fail('FIXTURE',case['id']+' unknown mode');continue
            passed+=1
        stats.update({'sources':len(source_set),'workflows':len(workflow_set),'guides':len(guide_ids),'remediation_findings':len(fids),'example_records':len(example['records']),'fixtures_passed':passed,'fixtures_total':len(cases['cases'])})
        if args.records:
            p=Path(args.records);bundle=yaml.safe_load(p.read_text())
            for e in record_errors(bundle['records'],schema,source_set,workflow_set,args.as_of or date.today().isoformat()):fail(e['code'],e['record']+': '+e['reason'])
            stats['additional_records']=len(bundle['records'])
    except Exception as exc:
        fail('CHECKER_ERROR',f'{type(exc).__name__}: {exc}')
    print(json.dumps({'status':'fail' if failures else 'pass','checks':stats,'errors':failures,'human_review_required':['legal interpretation and national applicability','source currency and legal citation at point of use','evidence authenticity/sufficiency and real authority','research ethics, real pilot and independent benchmark'],'scope':'Local structural and synthetic semantic checks only; no network, real users or legal approval.'},indent=2))
    return 1 if failures else 0

if __name__=='__main__':
    sys.exit(main())
