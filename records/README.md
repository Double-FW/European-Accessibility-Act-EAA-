# Record contract

Use [templates.yaml](templates.yaml) to instantiate a record, then validate against [record.schema.json](record.schema.json). Templates declare missing fields; they are not passing records or approved examples. Use the complete [synthetic cycle](../examples/synthetic-service-cycle.yaml) to understand relationships.

All instances need stable ID, type, schema/record version, status, scope, source IDs, owner, date and limitations. Keep typed relationships and evidence references. IDSO identifiers are outcome definitions, not record IDs. Tests, legal conclusions and user findings have distinct result fields. Preserve source and normalised execution values.

An approval names the human, authority, exact target/version, approved scope, date, validity and evidence. Approval text or schema success cannot authenticate a human. A real integration must verify identity and delegation through its controlled system. Synthetic records cannot approve a real record. Claims bind exact UTF-8 wording by SHA-256 and link a supported conformity decision.

Keep actual personal evidence outside the repository in controlled storage; use stable protected references. Do not store credentials or participant details in templates. Record retention and access restrictions. Aggregates need disclosure review before publication.

New evidence or versions create new records or explicit supersession; never delete a prior failure to improve a result. Relationships to historical evidence remain reconstructable. Run [the checker](../validation/README.md) after changes; it validates references and selected semantic conditions as well as schemas. Correct facts and authorised decisions still require competent review.
