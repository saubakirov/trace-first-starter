# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase B](../RF__phase-b__planning_research_learning.md)
> TS: [TS Phase B](../TS__phase-b__planning_research_learning.md)
> Mode: spec

## Understanding

Phase B changed the twelve approved planning, comparative-research, intensity, and
research-template consumers so they consume the value-first Method Kernel established
in Phase A. The result names and bounds the existing Briefing → Gather → Extract →
Challenge → RES sequence as the Comparative Decision Procedure, replaces activity
counts as completion authority with claim-based closure, adds disposition-typed
Learning Receipts, preserves the H4/T0 non-claim, and leaves configuration values and
later-phase consumers unchanged.

The implementation is split between commit `4466109` (the twelve framework consumers
plus the Task Board trace) and commit `d2f1466` (EV, RF, and the final Task Board trace).
The ONB and initial execution gate are recorded in commit `8758529`.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1: Phase A contracts become observable consumers | RF §3 ownership/consumer matrix claims distinct definition and operational owners, point-of-use gates, five protected consequences, no runtime research codes, and an accurate Phase B transition | ✅ Claimed |
| AC-2: Purpose-led planning and insight-to-TS traceability | RF §3 traces four planning cases through implication and AC/scope/guidance/DoF/research/non-use destinations without a new artifact | ✅ Claimed |
| AC-3: Comparative Decision Procedure is named and bounded | RF §3 gives six fit/mismatch scenarios; mismatch returns only the unresolved need to Coordinator/user | ✅ Claimed |
| AC-4: Focused and deep remain intensity controls | RF §3 compares the same case under focused/deep while retaining the same stages and closure authority | ✅ Claimed |
| AC-5: Numeric authority and stop conditions are honest | RF §3 lists twelve numeric/former-count objects, preserves the five-file procedure floor, and gives six closure scenarios | ✅ Claimed |
| AC-6: Stage checkpoints create proportionate Learning Receipts | RF §3 lists reject, task-local, promote/merge/derive, defer, and no-selected-signal cases and claims all four stage templates implement them | ✅ Claimed |
| AC-7: RES routes learning without multiplying capture | RF §3 traces stage signals and one human insight into existing stage, Fact Candidate, open-thread, and HL-update surfaces; Phase D remains transitional | ✅ Claimed |
| AC-8: H4 remains an enforced non-claim | RF §3 states H4 is unresolved/T0-only and denies any comparison or strategy architecture | ✅ Claimed |
| AC-9: Cross-consumer consistency, compression, and navigability | RF §4 claims exactly 12 consumers, unchanged config/template/exact values, 68 passing tests, valid links/anchors, rendered QA, and no new framework file | ✅ Claimed |

## Deviations from TS

The RF declares no TS deviation. `iterations.yaml max_iterations: 5` is explicitly
included in the twelve-row numeric ledger even though the TS checklist names it only
through the broader requirement to cover every active or hard-looking research number;
the Coordinator accepted that clarification at the implementation checkpoint. README,
ONB, EV, and RF changes are lifecycle traces rather than additional framework
consumers. No implementation work outside the twelve approved framework files is
declared.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

The ONB reported no blocking specification questions. The Coordinator explicitly
approved implementation with the twelve-consumer, unchanged-config, complete-stage,
mismatch-return-only, Fact Candidate compatibility, explicit-no-signal, and H4
boundaries.

Stage complete: YES
