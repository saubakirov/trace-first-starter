# Task — Chat Instance of trace-first-starter

## Objective
Demonstrate and harden the TFW entry point so any human/AI can: read the repo → generate CSA + project README + TASK + initial STEPS → proceed in strict Summary loop.

## In Scope
- Chat-Specific AGENTS.md (CSA) for THIS chat
- Project-specific README.md and TASK.md
- Initial STEPS.md entries (2–3 lines)
- Enforcement: strict Summary format; **Don’t be sycophantic**; **No placeholders**
- Fallback when browsing is unavailable (ordered file ingestion)

## Out of Scope
- Domain-heavy examples beyond what’s needed to validate the ritual
- Real secrets or proprietary data

## Definition of Done (DoD)
- CSA, README.md, TASK.md are present and self-consistent
- At least two valid `STEPS.md` entries exist (strict Summary spec)
- Next mode selected and ready to proceed

## Risks & Mitigations
- Non-compliant Summary → self-correct immediately to the strict format
- Token waste → flat root; avoid unrelated text
- Drift between docs and practice → maintain `TASK.md` and propose PR/diff for ritual changes

## Next Milestones
- v1.0 — CSA + project docs accepted; README cross-links validated
- v1.1 — Add short validation checklist (lint) for Summary lines and CSA presence
