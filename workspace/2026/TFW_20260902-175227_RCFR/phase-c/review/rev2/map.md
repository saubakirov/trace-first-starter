# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase C, Return Round 1](../../RF__phase-c__closure_secondary_paths_and_whole_system_proof.md#10-return-round-1--review-b33d534--coordinator-ruling-7bded93)
> TS: [governing Phase C TS](../../TS__phase-c__closure_secondary_paths_and_whole_system_proof.md)
> Live ruling: [REVIEW return-round ruling](../../REVIEW__phase-c__closure_secondary_paths_and_whole_system_proof.md#coordinator-ruling--return-round-1)

## Understanding

Return Round 1 addresses the three Rung-1 findings accepted by the Coordinator at
`7bded933d4c72a6c728722e4c2b3694e8baee7c6` under the unchanged approved TS. Candidate
`587bc417c4a00b8f592d88f7000509bcbbc76b55` changes 11 existing implementation/test files and
append-supplements six evidence files: it replaces the circular Phase C semantic producer, closes
the declared current-event write bounds while keeping legacy reads tolerant, and reconciles Docs
and Release to one source-derived Coordinator role census. The trace commit then appends the RF
return report and records the phase's `ONB → RF` return without changing the master task state.

## TS ↔ RF Alignment

| TS requirement / ruled return item | RF return claim | Aligned? |
|-------------------------------------|-----------------|----------|
| AC-6 / ruling 1 — six source-derived fields, independent expectation, anti-feed before production, minimal-input refusal, output-changing mutants | All 66 fields across 11 cases are independently resolved; expected data is poisoned before production; 11 mutants change a named field and are rejected. | ✅ |
| AC-3 / ruling 2 — complete current-event pre-write bounds with tolerant legacy reads | Actual gate rejects 4 impossible time/offsets, 4 absolute refs, 2 escaping refs, and 4 invalid summaries; accepts 3 relative refs; reads 2 adverse legacy events. | ✅ |
| AC-2/AC-4/AC-5 / ruling 3 — one baseline-equivalent Docs/Release role, source-derived exhaustive census, adapter parity, 8 adverse mutants | Docs and Release declare Coordinator across workflow, lock, manifest, skills, installed copies, and tracked copies; census is baseline-derived and 8/8 mutants fail. | ✅ |
| AC-1/AC-7 preserved — exact graph/count method and thresholds | Primary totals remain at/below entry ceilings; trajectory is 63.9% lower and active corpus 51.7% lower after the four-word role cleanup. | ✅ |
| AC-5 preserved — four clean receivers and exact topology | Original four-receiver evidence remains in force; affected copy hashes are refreshed and the full integration module is reported green. | ✅ |
| AC-8 preserved — configured tests, scope, exclusions, and trace honesty | 509 collected, 508 passed/1 skipped; project check green; only ruled RDP diagnostic; cumulative scope 41 files/4,480 LOC with no excluded change. | ✅ |

## Deviations from TS

The RF declares no deviation and no new authority, role, lifecycle state, field, key, runtime file,
or external effect. The return candidate's 11 implementation/test files are within the original
44-file surface and the cumulative 4,480 changed LOC remain below 5,000. ONB, RF, EV, and raw
evidence are extended in the existing artifacts rather than creating new runtime or governing
artifacts. These are mapped claims only; Verify will test them independently.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 and Return Round 1 completely?
- [x] Read TS DoD and matched each item to the original and return RF claims?
- [x] Read frozen master HL §7 Principles — can I state the design philosophy?
- [x] Read ONB including Return Round 1 — were blocking questions resolved?

Stage complete: YES
