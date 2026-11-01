# EAA delivery and evidence guides

This repository helps people and authorised agents manage European Accessibility Act requirements through delivery, assessment, customer evidence and continuing correction. It is prepared for Double FW Ltd, using its methods alongside official legal and technical sources. Six concise guides share structured workflows and record definitions. The objective is traceable decisions and comparable service outcomes, including satisfaction, rather than a numerical compliance score.

## Bootstrap and adoption state

1. Read [AGENTS.md](AGENTS.md) for execution and authority rules.
2. Inspect the [document index](control/document-index.yaml) and [source register](control/source-register.yaml).
3. Check [standards status](control/standards-status.yaml), including the verification date and legislation-specific citation.
4. Select a workflow from [workflows.yaml](workflows/workflows.yaml); load only the relevant guide sections and prerequisite records.
5. Follow the [record contract](records/README.md). Run the [repository checker](validation/README.md) before proposing a controlled change.

Version 1.0.0 is a **draft for organisational adoption** with executed structural and synthetic validation. It is not a product conformity assessment, approved national adapter, complete EN test library, working survey service or proven operational process. All example people, approvals and transactions are synthetic. Schema acceptance cannot authenticate a signature or establish that evidence is true.

## Task routing

| Task | Guide and workflow | Prerequisites | Outputs |
|---|---|---|---|
| Verify sources or correct guidance | G02; WF01 | Source record, change | Source disposition, remediation |
| Decide legal scope | [G01](guides/01-scope-and-applicability.md); WF02 | Service facts, jurisdiction | Applicability, limitations |
| Plan requirements and assessment | [G02](guides/02-requirements-and-assessment.md); WF03 | Approved scope, capabilities | Requirements, mappings, plan |
| Procure or deliver | [G03](guides/03-delivery-and-procurement.md); WF04–WF05 | Requirements, funded owners | Supplier/implementation evidence |
| Understand customer outcomes | [G04](guides/04-customer-outcomes-and-research.md); WF06 | Protocol, data permissions | IDSO findings, issues |
| Review conformity or a claim | [G05](guides/05-evidence-conformity-and-claims.md); WF07–WF08 | Scope, requirement evidence | Recommendation, approved decision/claim |
| Correct or monitor | [G06](guides/06-monitoring-and-corrective-action.md); WF09–WF10 | Event, current decisions | Retest, review, correction |

Workflow identifiers are stable; ranges in this table refer to individual entries in the workflow registry. [Guide navigation](guides/README.md) provides section routes. [Validation](validation/README.md) describes checks, fixtures and limits.

## Authority and source use

Applicable law governs legal decisions. Technical standards provide scoped assessment requirements; contracts and adopted policy may add obligations. Double-FW guidance supplies delivery and research methods. Source status distinguishes current material, commentary, historical redirects and unavailable dependencies. A retrieved recommendation does not become a statutory rule or an authorised executive commitment.

Preserve standard versions, raw results, evidence limits and negative findings. High satisfaction cannot erase a failed requirement; a clean scan cannot establish independent task completion. Examples and developer fixtures are excluded from real evidence and independent benchmark results.

The recovered ATLF 1.1 file supports the result vocabulary and delivery controls; its linked test repository remains inaccessible. The report's missing EAA guide was also recovered. Neither recovery verifies every linked test. Missing national facts, specialist methods and provider contracts block affected conclusions while independent authorised drafting and assessment continue. Record the owner, impact and next evidence needed rather than inventing a pass.

## Maintenance and rights

Use the [remediation register](control/remediation-register.yaml), [validation report](control/validation-report.md) and [changelog](CHANGELOG.md). Store personal operational evidence in controlled systems, not this public-ready package. Sources retain their own rights and attribution. No repository-wide licence is selected; the owner must decide distribution terms before publication. No remote repository or external publication is created by this package.
