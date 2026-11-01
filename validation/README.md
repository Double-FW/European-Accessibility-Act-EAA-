# Validation

Use Python 3.10 or later. Install the tested direct dependencies in a virtual environment:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install PyYAML==6.0.3 jsonschema==4.26.0
.venv/bin/python validation/check_repository.py
```

The checker resolves paths from its own location, checks local Markdown links/anchors and guide metadata, parses structured files, validates record/workflow schemas, checks IDs/references and selected semantic constraints, and executes positive and negative [fixtures](cases.yaml). It exits nonzero for detected errors or missing dependencies. It does not fetch URLs or write changes.

A test fixture includes expected errors or routing and prohibited outcomes. The checker compares these with actual results. The fixtures and [example cycle](../examples/synthetic-service-cycle.yaml) are synthetic developer material, not independent accuracy results or participant evidence. Routing is a deterministic decision helper, not an implemented orchestration service.

A competent human must review legal interpretation, source currency, evidence authenticity/sufficiency, sampling, participant ethics, genuine authority and operational outcomes. Build an independent reference set with experts who did not write the fixtures. Separate it from training/retrieval examples, record disagreement and adjudication, select risk-based thresholds before use, then evaluate actual agent outputs against it. No such independent study has been performed here.

See [validation-report.md](../control/validation-report.md) for the executed run, mutation checks and adoption dependencies.
