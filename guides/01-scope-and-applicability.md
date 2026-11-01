---
document_id: G01
version: 1.0.0
status: draft_for_adoption
authority_type: practitioner_guidance
review_date: '2026-11-01'
source_ids: [A05, E01, ATLF11]
prerequisites: [service_facts, jurisdiction_facts]
output_record_types: [jurisdiction, applicability, legal_limitation]
---
# Scope and applicability

## Purpose and trigger

Use WF02 when a service is introduced, procured or materially changed, a territory is added, or a legal assumption changes. The purpose is a bounded decision about which duties apply. A website's existence, commercial purpose or availability in Europe is insufficient. This guide interprets the Directive; applicable national law and competent human judgement control the actual decision. The legal reviewer is accountable for legal interpretation and scope approval; the service owner supplies facts and funds the response.

## Inputs and boundaries

Describe the legal entity, operator role, consumers, product or service, functions, channels, suppliers, release, territories and relevant dates. Separate manufacturer, authorised representative, importer, distributor and service-provider duties. One organisation may hold several roles. Include support, authentication, payment, content and third-party dependencies. Distinguish consumer services from employee systems; other duties may still apply to an internal system outside this EAA route.

Create one jurisdiction record per relevant Member State. Record the national law and version, official source, authority, applicability dates, procedures, documentation, language, notification and retention duties, reviewer and next review. No country has been selected for this package: its templates are unpopulated, not approved national adapters. If a material fact or legal source is missing, record `legal review required` and continue independent design work.

## Article 2 routing

The following is a routing summary, not a replacement for definitions and qualifications in E01.

| Route | Categories to check |
|---|---|
| Products, Article 2(1) | Consumer general-purpose computer hardware and operating systems; payment terminals; specified service terminals including ATMs, ticketing, check-in and interactive information terminals; consumer terminal equipment for electronic communications or access to audiovisual services; e-readers. |
| Consumer services, Article 2(2) | Electronic communications, excluding machine-to-machine transmission; access to audiovisual services; specified air, bus, rail and waterborne passenger-transport elements; consumer banking; e-books and dedicated software; e-commerce. |
| Emergency answering, Article 2(3) | Answering communications to 112 by the appropriate PSAP. |

For transport, check the exact category: urban, suburban and regional services have a narrower route concerning interactive self-service terminals. Do not broaden transport website obligations automatically. Distinguish audiovisual programmes from services providing access to them; programme length is not an exclusion test.

## Exclusions dates and limitations

Check Article 2(4) for pre-28 June 2025 recorded media and office formats, conditional map exclusions, third-party content outside the operator's funding/development/control, and qualifying archives. Document conditions and evidence; an outsourced component is not automatically excluded.

Check Articles 3(23), 4(5), 14, 31 and 32 through national implementation. The microenterprise service exemption is distinct from product duties. The Directive definition concerns fewer than ten persons and annual turnover or annual balance-sheet total not exceeding EUR 2 million. Fundamental alteration and disproportionate burden require the applicable assessment, not a schedule-based waiver. Check Annex VI, third-party accessibility funding, notification and record duties. For service disproportionate-burden assessments, review on relevant alteration, authority request and at least every five years.

Record transitions precisely. Existing contracts and products used in services have different rules; a blanket grace period for every service is wrong. Verify the conditions for the 2030 transition and any nationally permitted terminal-life provision. Emergency-answering implementation may have a different date. Keep scope and each affected limitation separate, including continuing duties and review/expiry.

## Annex routing and decision

Sections I–II concern products; III general services; IV specified services; V emergency answering; VI the Article 24(2) route. Section VII applies to functions not addressed in I–VI. Its alternative-technical-requirement route is conditional: the accessibility requirement must still be met and foreseeable use must result in equivalent or increased accessibility. Record the exact route and evidence; customer preference alone cannot establish it.

Prepare `in scope`, `partly in scope`, `out of scope` or `legal review required`. The authorised human approves the exact version. Retain included/excluded boundaries, national sources, Annex clauses, limitation status and evidence. An out-of-scope EAA finding removes no other obligation. Next, pass approved scope to [requirements and assessment](02-requirements-and-assessment.md) through WF03; unresolved legal questions remain explicit.
