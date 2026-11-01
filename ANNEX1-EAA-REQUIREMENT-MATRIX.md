# EAA Annex I requirement support matrix

This matrix is a repository-level planning aid for the `Double-FW/EAA-Compliance` operating model. It links each EAA Annex I requirement family to a relevant repository in the Double-FW ecosystem that can support delivery, governance, evidence collection, and evaluation. It is not a legal conclusion or a national adapter; it is a working evidence map to be reviewed against the actual service, product scope, jurisdiction, implemented baseline, and approved organisation policy.

## Legend

- Ref: stable internal requirement reference
- Annex I area: requirement family derived from the EAA Annex I / WCAG mapping structure used by the EAA practice guides
- Primary repo: repository most directly enabling delivery or evaluation for that area
- Supporting repos: additional repositories that help with management, evidence, or delivery controls
- Prompt: concise operating prompt to use with the relevant Double-FW repositories

| Ref | Annex I area | Primary repo | Supporting repos | Prompt |
| --- | --- | --- | --- | --- |
| EAA-A1-REF-01 | 1.1 Text alternatives | `Double-FW/Inclusive_and_Effective_Design` | `Double-FW/Phased-Approach-to-integrating-Accessibility-into-QA` | "Using the Inclusive and Effective Design and QA accessibility repositories, identify the user need, the relevant content alternatives, the delivery owners, and the evidence required to verify text alternatives for EAA Annex I 1.1. Produce a requirement record, a test plan, and any evidence gaps or remediation priorities for the product/service." |
| EAA-A1-REF-02 | 1.2 Time-based media | `Double-FW/Phased-Approach-to-integrating-Accessibility-into-QA` | `Double-FW/Inclusive_and_Effective_Design`, `Double-FW/Task-Analysis-for-Comparative-Accessibility-Evaluation-of-Internal-Systems` | "Review the time-based media experience using the QA and task-analysis repositories. Identify the media flows, captions, audio descriptions, and alternative access paths. Produce a delivery checklist, testing method, and evidence pack showing how the service meets the EAA Annex I 1.2 requirement." |
| EAA-A1-REF-03 | 1.3 Adaptable content | `Double-FW/POUR-for-Branding-Systems-and-CX` | `Double-FW/Cognitive-UX-Design`, `Double-FW/Inclusive_and_Effective_Design` | "Using the POUR-for-Branding-Systems and design repositories, map the information structure, presentation, and content adaptation needs for the product. Record how content remains understandable across devices, layouts, and assistive technologies, then list the delivery and evidence actions needed for EAA Annex I 1.3." |
| EAA-A1-REF-04 | 1.4 Distinguishable information | `Double-FW/POUR-for-Branding-Systems-and-CX` | `Double-FW/Cognitive-UX-Design`, `Double-FW/Inclusive_and_Effective_Design` | "Using the branding and cognitive design repositories, assess contrast, focus visibility, text legibility, and state communication. Produce a design decision log, evidence list, and evaluation notes showing whether users can distinguish content and interactions under EAA Annex I 1.4." |
| EAA-A1-REF-05 | 2.1 Keyboard accessibility | `Double-FW/Phased-Approach-to-integrating-Accessibility-into-QA` | `Double-FW/Managing-Embedded-Accessibility-and-Inclusive-Design`, `Double-FW/Inclusive_and_Effective_Design` | "Using the QA and embedded design repositories, map all critical user flows to keyboard and focus management requirements. Produce a task-based test plan, a delivery checklist, and evidence for keyboard operability under EAA Annex I 2.1." |
| EAA-A1-REF-06 | 2.2 Enough time and pauses | `Double-FW/Task-Analysis-for-Comparative-Accessibility-Evaluation-of-Internal-Systems` | `Double-FW/Inclusive_and_Effective_Design`, `Double-FW/Phased-Approach-to-integrating-Accessibility-into-QA` | "Using task-analysis and QA repositories, evaluate whether the service provides sufficient time, pauses, and user control for time-sensitive tasks. Capture user journeys, fairness risk, and evidence needed to show conformance with EAA Annex I 2.2." |
| EAA-A1-REF-07 | 2.3 Seizures and physical reactions | `Double-FW/AI-Accessibility-Maturity-Model` | `Double-FW/Managing-Embedded-Accessibility-and-Inclusive-Design`, `Double-FW/Inclusive_and_Effective_Design` | "Assess the service for flashing, motion, and sensory triggers using the AI accessibility maturity and design guidance repositories. Identify risk, required controls, and evidence for managing harmful visual and interaction patterns required by EAA Annex I 2.3." |
| EAA-A1-REF-08 | 2.4 Navigable and findable | `Double-FW/Managing-Embedded-Accessibility-and-Inclusive-Design` | `Double-FW/Inclusive_and_Effective_Design`, `Double-FW/Organisation_Governance_and_Strategy` | "Using the embedded design and organisational governance repositories, review navigation, landmarks, headings, and findability. Produce a management and delivery plan that demonstrates navigability, ownership, and evidence for EAA Annex I 2.4." |
| EAA-A1-REF-09 | 2.5 Input modalities | `Double-FW/Inclusive_and_Effective_Design` | `Double-FW/Cognitive-UX-Design`, `Double-FW/Phased-Approach-to-integrating-Accessibility-into-QA` | "Assess how users can complete tasks across input modes, including pointer, keyboard, touch, voice, and alternative interaction patterns. Use the inclusive design and QA repositories to record evidence, acceptance criteria, and any accessibility gaps for EAA Annex I 2.5." |
| EAA-A1-REF-10 | 3.1 Readable and understandable language | `Double-FW/Cognitive-UX-Design` | `Double-FW/Inclusive_and_Effective_Design`, `Double-FW/POUR-for-Branding-Systems-and-CX` | "Using the cognitive design and inclusive design repositories, assess readability, language clarity, and user comprehension. Produce a content review, evaluation plan, and evidence record showing how the product supports EAA Annex I 3.1 readability and understandability." |
| EAA-A1-REF-11 | 3.2 Predictable behaviour and operation | `Double-FW/Managing-Embedded-Accessibility-and-Inclusive-Design` | `Double-FW/Cognitive-UX-Design`, `Double-FW/Inclusion-and-Accessibility-Policy` | "Review the product for consistency, predictable changes, and clear interaction patterns. Use the embedded design and policy repositories to document decision ownership, user risk, and evidence for preventing confusion under EAA Annex I 3.2." |
| EAA-A1-REF-12 | 3.3 Input assistance | `Double-FW/Data_Ethics_and_Disability` | `Double-FW/Cognitive-UX-Design`, `Double-FW/Inclusive_and_Effective_Design` | "Using the disability data ethics and cognitive design repositories, assess error prevention, feedback quality, labels, and support mechanisms. Produce evidence and operational guidance for input assistance and recovery under EAA Annex I 3.3." |
| EAA-A1-REF-13 | 4.1 Compatible with assistive technologies and systems | `Double-FW/Phased-Approach-to-integrating-Accessibility-into-QA` | `Double-FW/Managing-Embedded-Accessibility-and-Inclusive-Design`, `Double-FW/Executive-and-Organisational-Commitments` | "Using the QA and governance repositories, evaluate compatibility with assistive technologies, APIs, browsers, and support tooling. Produce a conformance review, release evidence, and risk register for EAA Annex I 4.1 compatibility claims." |

## Repository prompt pack

The following prompt pack can be used as a reusable operating pattern across the Double-FW repositories for management, delivery, and evaluation:

1. Management prompt
   - "Using the relevant Double-FW repositories for governance, design, and policy, identify the accountable owner, the delivery scope, the acceptance conditions, and the evidence needed for the EAA Annex I requirement being assessed. Record assumptions, limitations, and unresolved gaps before any public claim is prepared."

2. Delivery prompt
   - "Using the relevant Double-FW repositories for implementation, QA, and design, map the requirement to the product features, user flows, and evidence checkpoints. Identify required design decisions, engineering controls, and acceptance evidence for release readiness."

3. Evaluation prompt
   - "Using the relevant Double-FW repositories for QA, task analysis, and customer outcomes, evaluate whether the implemented experience meets the requirement. Capture tested scenarios, negative evidence, remaining gaps, and the exact evidence required to support an operational conclusion."

## Working notes

- This matrix is intentionally scoped as a planning and evidence-routing tool for the repository and should be checked against the local jurisdiction, national implementation status, baseline documentation, and approved organisational policy before use in a formal legal or public-facing claim.
- Where a requirement is not directly covered by a single repository, the supporting repo list provides the operational bridge between design, delivery, governance, and evidence review.
- Evidence, outcome, and claim records should remain separate, as required by the EAA-Compliance repository contract and the record model.

## Reference list

- `EAA-A1-REF-01` to `EAA-A1-REF-13` are internal matrix references for the requirement families above.
- Source grounding for repository mapping comes from the source register and document index in this repository, with suitable caution around legal status, evidence limits, and draft guidance status.
