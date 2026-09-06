# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase C](../RF__phase-c__authority_routing.md)
> TS: [TS Phase C](../TS__phase-c__authority_routing.md), approved at `1f1173d968e9b74a5e06e3e2070ae604c2844ca5`

## Understanding

The Executor replaced the universal owner-only frozen-amendment path with one canonical Markdown
contract: a separately authorized, human-rooted Coordinator prefix admits child-only dispatch edges,
preserves the originating principal as proposer, and selects the nearest immutable-`true`
non-proposer ruler or the governing human owner. Plan, Review, Handoff, HL, RES, six accepted tracked
copies, and two existing repository-only assurance modules were updated as one bounded consumer
cascade; human-only exceptions, Role Locks, Phase A/B semantics, and Phase D/E exclusions are claimed
unchanged.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|---|---|---|
| AC-1 — human-rooted child-only initiation, refusal matrix, ordinary CL compatibility, no new runtime/schema | RF §3 marks AC-1 complete; §1 claims status owner + separate root authorization, Coordinator-only child construction, malformed-chain refusal, and direct owner-only CL fallback | ✅ claimed |
| AC-2 — stable proposer, nearest eligible non-proposer, immutable grant, signed terminal verdict | RF §3 marks AC-2 complete; §§1–2 claim stable-handle proposer preservation, nearest-`true` traversal, owner fallback, signer validation, and no grant mutation | ✅ claimed |
| AC-3 — human exceptions and role boundaries remain distinct | RF §3 marks AC-3 complete; §§1–2 claim reserved/self-grant/Purpose/REJECT/budget/unavailable/direct-owner/`RESTRICT` behavior and Reviewer/Coordinator/Executor separation | ✅ claimed |
| AC-4 — full owner-only census, one authority across consumers, six exact copies, source-derived assurance and mutants | RF §3 marks AC-4 complete; §§1, 4–5 claim all consumers classified, six copy pairs equal, 38 payloads, and 10 output-changing rejected mutants | ✅ claimed |
| AC-5 — exact boundary, Phase A/B and D73–D80 compatibility, attention ceilings, checks/build | RF §3 marks AC-5 complete; §§1, 4 claim exactly 12 VALUE + 2 ASSURANCE, fixed route/corpus limits, 635 passed + 1 skipped, structure and MkDocs success | ✅ claimed |
| AC-6 — approved immutable accounting/lineage and independent replay | RF §3 marks AC-6 complete; §§1, 4 claim approval/Baseline/Candidate lineage, exact 12-file and 89+/90− replay, Candidate-first timing, and zero later VALUE | ✅ claimed |

## Deviations from TS

No implementation deviation is declared. RF §6 discloses one live §14 sentence using “logged owner
verdict” and asks the independent Reviewer to decide whether canonical rule 8 narrows it adequately
or whether it is an unclosed AC-4 consumer/cascade defect. The TS's 320 touched-LOC figure is an
immutable comparison denominator; RF reports 179 actual touched LOC as an underspend, not a
rebaseline. Phase A's final REVIEW and Phase B's RF/final REVIEW revision 2 are the referenced
compatibility predecessors; their worktree/Candidate and stable-principal/grant boundaries are the
ones this review must preserve.

## Checkpoint

**Self-check:**
- [x] Read RF §1–§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

Stage complete: YES
