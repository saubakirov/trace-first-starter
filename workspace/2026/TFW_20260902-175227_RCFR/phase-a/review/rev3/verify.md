# Verify — Review Revision 3: “Are the claims true?”
> **Mindset:** Auditor. The RF is a declaration, not a fact.
> **Test:** “If I removed the RF, would the evidence alone prove the work was done?”
> **Min verify ratio:** 0.42 default
> **RF files claimed:** 69 cumulative candidate paths
> **Minimum:** 29 paths; **actual:** 69/69 cumulative paths accounted for across this continuing Reviewer task, all 15 revision-6 return paths opened, and the evidence discrepancies escalated the pass to 100%

## Verification Log

### V1: candidate identity and lineage
- **RF claim:** Revision 6 is complete at candidate `09ba070`.
- **Actual:** Exact candidate `09ba0704f1dc7c4979221d9d53ee52e4667ac68b` and detached Reviewer parent `b82eb81929e1d8fc283895ecf29c174a01ad6aae` have the same tree `68c8c0d9688d848fd1f07d2c1adc67f21846ac8c`. The twelve requested commits form one exact parent chain from candidate review-2 point `3a47af1`; local review-2 `8dc02b8` is tree-identical to that point. The tree was clean before revision-3 stage writes.
- **Match:** ✅

### V2: R4 independent derivation — 19 cases × 2 trees × 6 fields
- **RF claim:** Every normalized field is derived from content read through the executing tree; `EXPECTED_RECORDS` is comparison-only.
- **Actual:** `Scenario` contains only baseline/candidate source probes. `execute_scenario()` reads the selected source and addressed heading, then resolves each name in `SEMANTIC_FIELDS` against `DERIVATIONS`, requires exactly one matching clause, and records `(field, path, heading, clause)` provenance. Its code object references `DERIVATIONS` but not `EXPECTED_RECORDS`. The latter appears only in the three adverse/comparison tests and final equality assertion. Independent execution produced 38 records; every record had the six ordered provenance fields, and every baseline/candidate projection matched.
- **Match:** ✅

### V3: R4 adverse separation and semantic sensitivity
- **RF claim:** Expected mutation cannot affect production; minimal anchor-only input fails; a resolvable E3 substitution changes produced output before independent comparison rejects it.
- **Actual:** Replacing `EXPECTED_RECORDS[P1]` left the produced P1 record unchanged and made the independent comparison false. A minimal P1 source containing only the resolved heading and old anchor raised `SourceContractError`. Replacing `Never write RF with failing build` by `Write RF even with failing build` preserved file/address resolution and completed execution; decision changed `report → publish`, refusal changed `build or evidence failed → build failure ignored`, and gate changed `STOP → CONTINUE`, while expected data stayed unchanged and comparison rejected the record.
- **Match:** ✅ for implementation; ⚠️ evidence wording discrepancy D2

### V4: accepted regression surfaces
- **RF claim:** Audit, digest, structural mutants, ledger, adapters/receivers, exact commands, derived copies, and repository behavior remain green; rejected rev5 compaction paths match `f5cc3f1`.
- **Actual:** Runtime suite 73/73, gen-index 155/155, combined runtime/integration 121/121, and final serial configured suite 414 passed + one skipped from 415 collected. Audit remains 45.4% and 47.4%. Project consistency and zero-pending knowledge replay pass. `.tfw/scripts/gen_index.py`, `.tfw/scripts/test_gen_index.py`, and `docs/scripts/test_integration.py` have exact `f5cc3f1` blob identities. The task diagnostic reports only the immutable RDP 123>120 item plus six informational historical groups.
- **Match:** ✅

### V5: exact scope and both budgets
- **RF claim:** Implementation/test/evidence is 41 paths and 3,795 LOC; the whole candidate is 69 paths and 5,517 LOC under the owner’s 6,000 override.
- **Actual:** Primary `git diff --numstat 2728dae…09ba070` gives 69 paths, 4,278 additions, 1,239 deletions, **5,517 LOC**. Filtering the 36 non-task implementation/test paths plus five Phase-A evidence paths gives 41 paths, 2,559 additions, 1,236 deletions, **3,795 LOC**. The return range changes only the one implementation file and authorized governing/lifecycle/evidence/state paths; no HL, Phase B/C, adapter, canonical workflow, prior REVIEW, or prior review-stage artifact changed.
- **Match:** ✅ for implementation/RF; ❌ for EV D1

### V6: cumulative RF, EV, semantic evidence, and lifecycle traces
- **RF claim:** Revision-6 evidence is 4/4 VERIFIED and the phase is correctly returned to `RF` under TS rev6.
- **Actual:** Status authority is TS rev6; journal records the rev4/rev5/rev6 handoffs and `ONB → RF`; ONB/RF/EV/semantic evidence append rather than erase prior rounds. RF’s corrected final counters match primary Git. Two “final” raw/structured evidence observations do not match the candidate: EV line 60 still says 68 paths/5,505 LOC, and semantic evidence says the minimal P1 source fails on `refusal_reason`, while the current test input actually resolves that field and first fails on `artifacts_created`.
- **Match:** ❌ — D1/D2

### V7: knowledge citations and project documentation
- **RF claim:** No new Fact Candidate or Strategic Insight; prior knowledge applications remain in force.
- **Actual:** The 13 master-HL §7.2 / ONB §7 applications are unchanged from the two previous full semantic checks and their source blobs did not change. No new human-only fact appears. `KNOWLEDGE.md` still has the previously documented stale Architecture Map `Adapters` row; it remains post-approval `/tfw-docs` work and is not a revision-6 implementation regression.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | candidate/base tree and exact parent-chain checks | `8dc02b8^{tree}=3a47af1^{tree}`; `b82eb81^{tree}=09ba070^{tree}=68c8c0d…`; clean before review writes |
| 2 | independent two-counter `git diff --numstat 2728dae…09ba070` | implementation/test/evidence: **41 paths, 2,559 + 1,236 = 3,795 LOC**; whole tree: **69 paths, 4,278 + 1,239 = 5,517 LOC** |
| 3 | custom 38-record production/provenance probe | 19 baseline + 19 candidate records; all six provenance fields present and sourced |
| 4 | custom expected/minimal/E3 adverse probe | expected mutation isolated; minimal source rejected on `artifacts_created`; E3 completed, changed three fields, independent comparison rejected |
| 5 | `python -m pytest docs/scripts/test_runtime_context.py -q -k "round2 or baseline_and_candidate or deliberate_mutant"` | 28 passed, 45 deselected |
| 6 | `python -m pytest docs/scripts/test_runtime_context.py -q` | 73 passed in 6.99s |
| 7 | `python -m pytest .tfw/scripts/test_gen_index.py -q` | 155 passed in 2.58s |
| 8 | `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_integration.py -q` | 121 passed in 287.43s |
| 9 | `python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only` | 415 collected |
| 10 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | Final serial run: 414 passed, 1 skipped in 272.45s |
| 11 | initial full run launched concurrently with command 8 | Discarded as reviewer-induced interference: both processes used the same fixed `_probe.md`; one deleted the other’s probe. A clean serial rerun is command 10 and passes. |
| 12 | `python docs/scripts/test_runtime_context.py --audit` | plan 64,229 → 35,068 (**45.4%**); knowledge 78,587 → 41,347 (**47.4%**) |
| 13 | `python .tfw/scripts/gen_index.py --check project` | PASS |
| 14 | `python .tfw/scripts/gen_index.py --check tasks` | Exit 1 only for immutable RDP summary 123 vs 120; six historical groups informational |
| 15 | `python .tfw/scripts/gen_index.py --knowledge-pending --format json` | 61 current; pending/removed/problems empty; migration false |
| 16 | three `f5cc3f1` blob comparisons | All exact: gen-index implementation/tests and integration tests |
| 17 | `git diff --check 2728dae…09ba070` | PASS |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | “All 19 … records derive all six fields independently” and expected data is comparison-only | RF §11.1–§11.3; EV R6-E1/R6-E2 | `docs/scripts/test_runtime_context.py:64-345`, source clauses, custom adverse probe | ✅ |
| C2 | “Minimal P1 anchor-only input fails with `refusal_reason … 0 times`” | `semantic-fixtures.txt` revision-6 section | exact current test input through `execute_scenario()` | ❌ — it fails on `artifacts_created`; the broader rejection claim holds, but the quoted evidence is false |
| C3 | “Final counters … whole candidate 68 paths … 5,505 LOC” | EV line 60 | primary `git diff --numstat 2728dae…09ba070` | ❌ — exact result is 69 paths and 5,517 LOC |
| C4 | Corrected “69 paths … 5,517 LOC” and 41/3,795 scoped result | RF §11.4 | same primary Git diff and explicit scope filter | ✅ |
| C5 | “45.4% plan; 47.4% knowledge” and 415/414+1 gates | RF §11.4 | runtime audit and independently rerun suites | ✅ |

Every RF/EV link resolves. All 13 knowledge applications remain resolved, semantically matched, and relevant; no new revision-6 citation was introduced.

## Discrepancies Found

1. **D1 — EV budget evidence is stale and false.** EV revision-6 E4 is marked VERIFIED but its “Final counters” state 68 paths/5,505 LOC. The exact final candidate and corrected RF are 69 paths/5,517 LOC. Both outcomes are under the 6,000 override, so implementation containment passes, but the structured evidence does not establish the exact claim required by TS rev6 §3.4.
2. **D2 — semantic raw evidence names the wrong minimal-source failure.** The implementation correctly rejects the minimal anchor-only source, but the evidence records `refusal_reason … 0 times`; current execution deterministically reaches and resolves that field, then fails on `artifacts_created … 0 times`. This breaches the exact adverse evidence required by TS rev6 §3.2 even though the R4 mechanism itself passes.

Both discrepancies are confined to append-only evidence correction. They require no code, RF, HL, prior evidence, or prior review rewrite. On the first discrepancy, verification expanded to all 69 cumulative paths; the 54 unchanged candidate paths retain their prior Reviewer results and all 15 return-round paths were opened here.

## Evidence Verification

| # | RF/EV revision-6 evidence ref | Artifact exists? | Matches claim? |
|---|-------------------------------|-----------------|----------------|
| R6-E1 | Independent derivation; `semantic-fixtures.txt`; implementation `13853b0` | ✅ | ✅ — production/provenance path and 38 records verified |
| R6-E2 | Expected isolation, minimal source, E3 substitution | ✅ | ⚠️ — all three behaviors pass, but D2 makes the recorded exact minimal failure false |
| R6-E3 | Regression suite and rejected compaction equality | ✅ | ✅ — all final serial gates and blob checks pass |
| R6-E4 | Two budgets and final counters | ✅ | ❌ — D1; scoped count is correct, whole-tree count is stale |

## Knowledge Citations Verified

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1–13 | Master HL §7.2 K1–K10 and cumulative ONB §7 #1–#13 | P0 NS1/NS3; P1 Structural Enforcement/Naming/Portability; P2 F22/F40/F43/F45; P3 D23/D25/D54/D61/D63/D68/D69/D72; P4 conventions §§11/14; P5 F4/F8/F14; P6 F3/F4/F22/F30; P7 relevance scan; router entries | ✅ 13/13 | ✅ 13/13 | ✅ 13/13 — unchanged source and assertion | ✅ 13/13 — R4 implements the cited structural/evidence principles |

`KNOWLEDGE.md` Architecture Map `Adapters` row remains stale exactly as documented in REVIEW revisions 1–2. It requires `/tfw-docs` only after a future APPROVE and is not writable by this Reviewer.

## Checkpoint

**Self-check:**
- [x] Accounted for 69/69 cumulative paths and opened every revision-6 return path?
- [x] Ran targeted, combined, final serial full-suite, audit, scope, state, and independent adverse probes?
- [x] Claim & Source Checks cover the semantic mechanism, exact evidence text, primary counters, reductions, and suites?
- [x] Each governing TS revision-6 acceptance item checked against implementation and evidence?
- [x] `KNOWLEDGE.md` contradiction retained without crossing the Reviewer role lock?
- [x] All 13 knowledge applications remain resolved, semantically verified, relevant, and non-hallucinated?
  - Total: 13, resolved: 13, semantically verified: 13, irrelevant: 0, hallucinated: 0
- [x] All four revision-6 evidence items checked separately for existence and sufficiency?
  - Total: 4, verified: 2, partial: 1, insufficient: 1, missing: 0

Stage complete: YES
