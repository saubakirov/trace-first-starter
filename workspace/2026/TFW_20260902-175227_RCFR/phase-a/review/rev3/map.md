# Map — Review Revision 3: “What was done?”
> **Mindset:** Experienced newcomer. Understand the returned repair before judging it.
> **Test:** “Can I explain what was done to someone who has not read the RF?”
> **RF:** [RF Phase A revision 6 return](../../RF__phase-a__common_authority_and_context_topology.md#11-revision-6-return--final-r4-repair)
> **TS:** [TS Phase A revision 6](../../TS__phase-a__common_authority_and_context_topology__rev6.md)

## Understanding

Revision 6 retains R4 as the sole semantic change and records the owner’s phase-local whole-tree budget override. The Executor changed only `docs/scripts/test_runtime_context.py`: `EXPECTED_RECORDS` is comparison-only, while `DERIVATIONS` resolves each of the six produced fields from clauses read through the executing baseline or candidate `SourceTree`, recording field/path/heading/clause provenance. Three guards cover expected-oracle separation, failure of a minimal anchor-only source, and a resolvable E3 source substitution that changes produced behavior before the independent comparison rejects it.

The cumulative ONB, RF, EV, and `semantic-fixtures.txt` append the revision-6 account; `.tfw/knowledge_state.yaml`, phase status, and phase journal record state-last reconciliation and the return to `RF`. The exact candidate is `09ba0704f1dc7c4979221d9d53ee52e4667ac68b`; the detached Reviewer parent `b82eb81929e1d8fc283895ecf29c174a01ad6aae` has the same tree `68c8c0d9688d848fd1f07d2c1adc67f21846ac8c`.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| Independent derivation for all 19 cases and all six fields | Source clauses produce every field independently in both trees; provenance accompanies each record | Claimed ✅; Verify must inspect the production path and field provenance |
| Expected data cannot feed production | Mutating `EXPECTED_RECORDS[P1]` leaves production unchanged and makes only comparison fail | Claimed ✅; Verify must execute the adverse guard independently |
| Minimal anchor-only input cannot manufacture a record | P1 minimal source fails resolving `refusal_reason` | Claimed ✅; Verify must reproduce the named failure |
| Resolvable semantic substitution changes production before rejection | E3 substitution changes decision/refusal/gate and then fails comparison | Claimed ✅; Verify must confirm execution completes and expected data is untouched |
| No unrelated behavior change | Accepted audit, digest, adapter, receiver, structural, ledger, and full-suite gates remain green | Claimed ✅; Verify must rerun the required gates and compare rejected compaction paths |
| Separate budgets | 41 implementation/test/evidence paths and 3,795 LOC; 69 whole-tree paths and 5,517 LOC under the 6,000 override | Claimed ✅ in RF; EV still states 68 paths/5,505 LOC, so Verify must resolve the primary diff |

## Deviations from TS

The RF reports no implementation deviation. Revision 4 stopped before implementation on the then-governing budget, revision 5’s compaction experiment was discarded, and revision 6 explicitly restored the three unrelated paths to `f5cc3f1`. The only declared discrepancy among returned traces is the cumulative counter conflict between RF revision 6 (`69 / 5,517`) and EV revision 6 (`68 / 5,505`), which requires independent verification and sufficiency judgment.

## Checkpoint

**Self-check:**
- [x] Read cumulative RF §§1–11 completely, including the revision-6 return?
- [x] Read governing TS revision 6 and its revision-4/5 lineage?
- [x] Reconfirmed the unchanged master HL contract baseline and Phase HL from the preceding review?
- [x] Read cumulative ONB through revision 6 and confirmed no blocking question remains?

Stage complete: YES
