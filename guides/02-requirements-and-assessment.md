---
document_id: G02
version: 1.0.0
status: draft_for_adoption
authority_type: practitioner_guidance
review_date: '2026-11-01'
source_ids: [A02, A01, E01, E02, E04, E08, D039, ATLF11]
prerequisites: [approved_applicability, capability_inventory]
output_record_types: [requirement, mapping, test_execution, evidence]
---
# Requirements and assessment

## Purpose inputs and accountability

Use WF03 to translate approved scope into acceptance conditions and WF05 to evaluate delivery. Inputs are the applicability record, national provisions, ICT capability inventory, adopted technical profile and declared release/environment. QA is accountable for assessment coverage and classification; legal review controls the interpretation of legal duties. A mapping is a relationship to evidence, never a passing execution.

## Select and version the baseline

Consult [standards status](../control/standards-status.yaml) before selection. Publication, contractual adoption and legislation-specific citation are separate facts. As checked on 1 November 2026, EAA citation of V4.1.1 was not established; do not infer it from the WAD reference. Recheck authoritative sources before a live claim.

For V4.1.1, Annex A.2 Tables A.1–A.5 route the assessment; ZB relates requirements to the EAA, ZA to the WAD, and Annex C supplies assessment means. Retain conditions and assumptions. This package provides a routing method and examples, not a complete EN test catalogue. Specialist hardware, closed-functionality, communication, media, software and document functions need competent methods when relevant. Record a gap when those methods are unavailable.

WCAG 2.2 A/AA is this package's proposed web baseline. It becomes locally binding through adoption or an obligation; the Directive does not directly name that version. Preserve older contractual or cited baselines separately. AAA enhancements remain labelled recommendations. Perceivable, Operable, Understandable and Robust are the formal principle names. Robust concerns reliable interpretation and interoperability; clean code alone proves neither. Cognitive accessibility and usability overlap but ask different questions. Satisfaction is an additional Double-FW outcome, not an official fifth WCAG principle.

## Correct the mapping approach

Create one requirement per source clause and scoped subject, with interpretation separate from original text. For each mapping record the source version, exact clause, applicability rationale, relationship, coverage limits, method and required evidence. Many requirements need several tests; one test can support several requirements. Never infer equivalence from shared titles or numbers.

| Legal provision | Technical support example | Residual evidence |
|---|---|---|
| Annex I III(c), in-scope service interfaces | WCAG 2.2 SC 2.1.1; EN V4.1.1 9.2.1.1 and assessment C.9.2.1.1, where applicable | Other applicable criteria, states, channels and legal duties; actual complete-task operation. |
| Annex I IV(e)(ii), banking information | Comprehension review against its B2 condition | A WCAG AA result alone cannot establish the specified language complexity. SC 3.1.5 is AAA and is not a B2 equivalence rule. |
| Annex I IV(g)(iii), e-commerce authentication/signature/payment | WCAG 2.2 SC 3.3.8 at AA for applicable authentication | Transaction accuracy, payment/signature routes and all other applicable duties. |

These examples identify partial support, not full legal coverage. For information in III(b), distinguish alternatives, sensory channels, perception, text formats and typography. A resizable font does not prove understandable information or equivalent formats. Test actual language, content meaning and foreseeable display conditions. Do not invent a universally accessible typeface or relabel AAA criteria as AA.

## Plan and execute complementary methods

Specify objective, applicability, preconditions, setup, steps, expected results, method, competence and evidence before execution. Cover components, pages, routes, errors, modal states, recovery, integrations and complete journeys. Record sample rationale and what it cannot represent. Include relevant keyboard, assistive-technology, zoom/reflow, content and specialist assessment; the available axe/keyboard plan is partial.

D039 pins 4.12.1 while D036 proposes 4.13. No engine is installed or adopted by this package. A project must verify its actual package, lockfile, rule inventory, configuration and known-failure checks before use. Preserve WCAG, best-practice and experimental results separately. Counts are not accessibility coverage percentages.

Use ATLF 1.1 results: `Pass`, `Fail`, `Cannot tell`, `Not applicable`, `Not tested`, `Blocked`, `Tool error`. Preserve original QA labels and the explicit adapter in the workflow file. A false requirement precondition and invalid assessment assumptions are different: invalid assumptions require another assessment or an unresolved result. Retain observations, version, environment, raw findings, evidence and reviewer.

## Outputs and next decision

Deliver requirement/mapping records, assessment coverage, executions, evidence and owned gaps. Pause the affected conclusion for missing methods, blocked states or contradictions. A failed standard remains failed despite an accepted release risk. Route evidence to WF07 and [conformity review](05-evidence-conformity-and-claims.md); route defects to WF09. Meaning and lived experience still need [customer research](04-customer-outcomes-and-research.md).
