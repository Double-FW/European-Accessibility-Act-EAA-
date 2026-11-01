# Validation and adoption report

Version 1.0.0 • 1 November 2026

This report records the package checks and their limits. The guides remain draft for adoption. No real service, jurisdiction adapter, participant study, engine integration or legal approval is represented by the examples.

## Executed checks

Executed with Python 3.12, PyYAML 6.0.3 and jsonschema 4.26.0. The exact invocation was `python validation/check_repository.py`, using an isolated dependency directory on this build host; portable installation instructions are in the validation README.

| Check | Observed result |
|---|---|
| Markdown navigation and metadata | Passed for 13 Markdown files and six indexed guides. |
| Structured syntax and schemas | Passed for 10 JSON/YAML files, both JSON Schemas, all workflows and example record instances. |
| IDs and relationships | Passed for 34 registered sources, 10 workflows, 36 remediation findings and 20 synthetic records. |
| Developer cases | 40 of 40 passed: 13 routing cases, 20 invalid-record mutations and seven transition cases. |
| Whole-package corruption checks | Five of five deliberately broken copies failed with nonzero exit status and the expected error. |

The five package corruptions were a broken local link, inconsistent guide version, unknown source, cyclic step dependency and deliberately false fixture expectation. They produced LOCAL_LINK, METADATA, SOURCE_REFERENCE, STEP_DEPENDENCY and FIXTURE errors respectively. Temporary copies were discarded; the deliverable retained the valid files.

The checker is an implemented read-only structural and selected semantic validator. It does not execute workflow orchestration, inspect a live service, contact participants, authenticate approvers or determine legal sufficiency. The fixtures were authored with the checker and are not an independent accuracy benchmark. No operational or legal approval is inferred from the passing run.

## Editorial and remediation results

All six guides fall within the requested 600–1,000-word range. Root README and AGENTS.md meet their respective targets; each secondary README is below 300 words. The core narrative is below approximately 8,000 words. There is one canonical six-guide set and shared structured support.

All R01–R36 findings have a correction, exclusion or explicitly constrained disposition. No finding was marked resolved solely from a passing schema. Remediation concerns the new package; originals and remote files remain unchanged. Constrained items include complete standards coverage, real national-law scope, exact inaccessible test-library assets, provider/engine integration, remote link repair, maturity crosswalks and a real operational pilot. No constrained module is labelled ready for operational legal use.

## Remaining adoption dependencies

| Dependency | Effect and resolution |
|---|---|
| National law and service facts | Populate a real jurisdiction adapter and scope, with competent legal review, before live conclusions. |
| Test-library access | ATLF 1.1 recovered; live QA repository returned 404 again. Obtain exact current test assets before adopting their procedures. |
| Standards/legal status | Official EN/TR and Commission sources rechecked on the report date; EAA citation not established. Recheck at decision time. |
| Specialist methods | Select/verify methods for applicable hardware, communication, media, documents and software; no complete test catalogue asserted. |
| Engine/provider contracts | Adopt actual package/profile, manual complement and survey instrument/export/API only after implementation evidence. |
| Evidence and approvals | Synthetic records cannot authorise live action or authenticate a human. Verify real evidence and identity in controlled systems. |
| Operational pilot | Run and observe a representative real cycle including interruption, failed dependency, correction, retest and handover. |
| Independent evaluation | Commission a competent human-reviewed reference set distinct from developer fixtures; set risk-based thresholds before testing. |
| Publication rights | Owner selects repository distribution terms; source rights and private data restrictions remain separate. |

## Source review updates

The recovered ATLF 1.1 copy verifies the seven-result vocabulary and the delivery/evidence framework; it does not restore the remote library. The missing EAA 2025 guide was recovered as practitioner commentary and is not the legal authority. The new guides replace erroneous attachment subject matter through original synthesis; no original file or remote repository was edited. Thirty-six review findings retain explicit dispositions and remaining dependencies in the remediation register.
