# Map — Review Revision 4: “What was done?”
> **Mindset:** Experienced newcomer. Understand the evidence-only return before judging it.
> **Test:** “Can I explain what was done to someone who has not read the RF?”
> **RF:** [RF Phase A revision 8 return](../../RF__phase-a__common_authority_and_context_topology.md#12-revision-8-return--exact-evidence-correction)
> **TS:** [TS Phase A revision 8](../../TS__phase-a__common_authority_and_context_topology__rev8.md)

## Understanding

Revision 8 closes only REVIEW revision 3 findings D1 and D2. It appends an exact correction to the
existing EV for reviewed implementation snapshot `09ba070`, retaining the historical false line but
superseding it with whole-tree `69 / 4,278 / 1,239 / 5,517` and scoped
`41 / 2,559 / 1,236 / 3,795`. It likewise appends the actual minimal-P1 failure
`P1: artifacts_created semantic source resolved 0 times` to `semantic-fixtures.txt`, while leaving the
prior `refusal_reason` observation visible as superseded history.

The return also appends concise revision-8 ONB and RF sections, adds the two governing TS revisions,
records the canonical `TS_DRAFT → ONB → RF` lifecycle, and reconciles knowledge state last. No code,
test, HL, prior TS, prior REVIEW, workflow, adapter, derived-copy, unrelated trace, or other evidence
blob is part of the repair. Candidate `2535102a1af25f38af226d1f88e42ba4a647c57f` is tree-identical
to local Reviewer parent `61e1fd807515f2b077e4a3dedb46dbdc3476608e`.

## TS ↔ RF Alignment

| TS revision 8 requirement | RF §12 claim | Aligned? |
|---------------------------|--------------|----------|
| Append exact whole and scoped corrections for fixed snapshot `09ba070` | EV supersedes 68/5,505 with 69/5,517 and retains 41/3,795 | Claimed ✅; Verify must reproduce both counters |
| Append the exact minimal-P1 first failure | Semantic evidence supersedes `refusal_reason` with `artifacts_created` | Claimed ✅; Verify must run the targeted test and direct probe |
| Preserve accepted implementation and all excluded blobs | Only EV, semantic evidence, concise ONB/RF, governing/lifecycle/state traces changed | Claimed ✅; Verify must inspect the complete return diff and blob identities |
| State-last replay and project consistency | Project check and knowledge replay pass with no pending, removed, or problem IDs | Claimed ✅; Verify must replay at the returned candidate |
| Keep separate fixed-snapshot and post-trace budgets | Fixed implementation/evidence 3,795; fixed whole 5,517; post-trace whole 6,065 under 7,000 | Claimed ✅; Verify must measure each named range |
| Do not rerun the accepted full suite | RF explicitly records that no full suite was rerun | Aligned ✅ |

## Deviations from TS

No deviation is declared or visible. The return changes exactly ten authorized paths: two new
governing TS files, two append-only evidence files, cumulative ONB/RF, knowledge state, phase status,
and two phase journal events. The full suite and accepted R4 implementation were not reopened.

## Checkpoint

**Self-check:**
- [x] Read the governing TS revision 8 and its revision-7 basis?
- [x] Read RF §12, the revision-8 ONB append, both corrected evidence appends, status, state, and journal events?
- [x] Kept REVIEW revision 3’s accepted implementation findings as immutable review input?
- [x] Identified the fixed reviewed snapshot separately from the post-trace return candidate?

Stage complete: YES
