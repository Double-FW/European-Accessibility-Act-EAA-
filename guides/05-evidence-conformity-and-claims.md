---
document_id: G05
version: 1.0.0
status: draft_for_adoption
authority_type: practitioner_guidance
review_date: '2026-11-01'
source_ids: [A06, A05, ATLF11, E01, D017]
prerequisites: [approved_applicability, current_evidence_set]
output_record_types: [evidence, conformity_conclusion, approval, public_claim]
---
# Evidence conformity and claims

## Purpose trigger and authority

Use WF07 for a requirement or conformity decision and WF08 for a proposed claim. Inputs are approved applicability, current national and technical sources, complete requirement inventory, mappings, executions, outcomes, legal limitations and issue history. QA prepares the evidence assessment; the authorised legal/compliance owner controls the legal conclusion and claim. The service owner owns implementation and correction. Automation prepares and checks records but cannot create human approval.

This guide extends the supplied evidence model into a concise operating procedure. Its record rules are proposed repository controls, not a universal regulator reporting template. A reviewer must still determine whether the evidence and statement satisfy applicable national and sector duties.

## Build a reconstructable chain

Preserve relationships from scope to legal requirement, interpretation, technical/policy mapping, test execution, evidence, outcome finding, requirement conclusion, conformity decision, claim and monitoring. A relationship has a named meaning: supports, partially supports, contradicts, assesses, supersedes or triggers review. Neither a related criterion nor a supplier certificate is itself an executed test.

Each evidence item needs its source/collector, date, release, task/state, environment, method, sample where relevant, actual observation, limitations and what it cannot establish. Maintain accessible text accounts of material visual/audio evidence. Reference controlled locations rather than exporting private research or credentials to this repository. Record access, retention, supersession and confidentiality controls.

Preserve original findings and result vocabulary. The framework's available 1.1 copy confirms seven test results; the QA six-label adapter is explicit in the workflows file. An invalid test approach is unresolved until an appropriate method is used. Do not rewrite prior results when a repair produces a new passing execution.

## Reach a bounded requirement conclusion

For each legal requirement, the authorised reviewer records `supported as met`, `not met`, `cannot conclude`, `not applicable by approved scope decision` or `not assessed`. Use `legal review required` as routing when the legal basis or interpretation is unresolved, not as a disguised pass. Scope non-applicability requires the approved applicability record; an outcome marked not relevant supplies no such authority.

A positive conclusion needs relevant current sources, an explicit interpretation, sufficient methods across material scope, traceability to release/configuration, considered contradictions and approval. Split scope where evidence differs across territory, feature or period. Confidence is high, moderate, low or insufficient with rationale; it is not a mathematical compliance probability.

Investigate disagreements by comparing release, environment, task, method and population. Preserve real differences and severe minority cases. Prefer targeted additional evidence that can change the decision. Do not remove an adverse finding because it conflicts with a favourable average, technical result or business preference.

## Distinguish decision routes

| Route | Effect |
|---|---|
| Repair and retest | New implementation evidence may support a new result; historical failure remains. |
| Temporary defect acceptance | Records unresolved failure, responsible owner, compensating action, monitoring, review and expiry; it does not create legal conformity. |
| Policy departure | Permitted alternative to an organisational baseline needs equal-or-better-outcome evidence and authorised review. |
| Alternative technical solution | Requires the exact permitted legal route and evidence, including equivalent/increased accessibility where required. |
| Statutory limitation | Requires legal basis, affected scope, assessment, correct authority, continuing duties and applicable notification/review. |

The available test libraries behind ATLF remain inaccessible remotely. The recovered framework supports governance and vocabulary, not validation of every referenced test. Specialist methods and national adapters remain product-specific prerequisites.

## Product service and claim records

For products, check the operator's technical documentation, conformity assessment, EU declaration and marking duties under Articles 7–11 and Annex IV. For services, check Article 13 and Annex V information explaining fulfilment. Article 13(2) requires public written and oral information, accessible to disabled people, retained while the service operates; verify its national implementation and continuing controls. Do not impose product CE documentation on a service by analogy. Retention, languages and notifications must follow the verified legal route, not a universal period invented here.

A claim record needs exact wording, audience/channel/language, product/service and release, territory, requirement scope, evidence and decision links, material limitations and authorised approval of the exact version or content hash. A publication operator may transmit only that approved artifact under permission; editing wording requires reconsideration. Draft examples are never real approvals.

## Stop conditions outputs and handoff

Stop the affected decision if scope is unapproved, a material requirement fails or is unassessed, evidence is stale/contradictory, a limitation is unsupported, authority is missing, or a claim implies more than the record supports. Narrow the statement or return `cannot conclude`. Deliver the decision bundle, claim draft and pending actions. Use WF09 for correction and WF10 for review triggers, expiry and withdrawal under [monitoring](06-monitoring-and-corrective-action.md).
