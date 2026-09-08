# RF — TFW_20260907-133942_PTTC / Phase A: Proportionate repository verification

> **Date**: 2026-09-08
> **Author**: robert, Executor `01a081fd-96cb-7862-9c15-33d803c1aade`
> **Status**: 🟢 RF — Complete; independent review pending
> **Parent HL**: [Phase A HL](HL__phase-a__proportionate_repository_verification.md), [master HL](../HL-TFW_20260907-133942_PTTC.md)
> **TS**: [approved Phase A TS](TS__phase-a__proportionate_repository_verification.md)

## 1. What Was Done

Source/Git/temp-tree checks now live in `test_repository_contracts.py`, without a website-build dependency. `test_integration.py` retains all 15 output predicates and its original shared module-scoped MkDocs fixture. The split preserves effective predicates and their dependencies, removes overwritten bodies and redundant aliases, repairs only the two live runtime-context ledger paths, and adds concrete selection/reuse guidance to the existing maintainer README.

Knowledge protection separates immutable historical identity from current structural facts. Current selected decisions and artifacts retain cardinality, phase lineage and required immutable sources while allowing explanations and additional decisions. A labeled successor fixture illustrates the already approved Phase D transition. Independent reading against actual authority remains necessary for material meaning, principal attribution and successor legitimacy; this RF does not grant that acceptance.

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | `49ddad02f97dfb46919bdd19292902b9082d696f`, exact approved requirement source `af52ef3ab6891031db8c411932879d76cfc1e6e6`, TS blob `b7ef498c4d911cf6fb4f8c810aef24913480f68d` |
| Baseline / Candidate | `099d37d21ddfada2ca72c576055f0a26029c7205` / `8c72c4c25aa7dde461cfee23b11f90db5f09e220` |
| VALUE membership | MODIFY `docs/scripts/test_integration.py`: output boundary and source transfer; CREATE `docs/scripts/test_repository_contracts.py`: accepted source/Git assurance product; MODIFY `docs/scripts/test_runtime_context.py`: R10/R14 live target repairs only; MODIFY `tools/README.md`: accepted maintainer verification/reuse route. All four are VALUE, whole paths, attributable to this Phase A Executor |
| Arithmetic | 2,922 additions + 2,937 deletions = **5,859 touched text LOC; 4 logical files**. No detected rename. Binary/non-text N/A |
| Membership deviations | None; no extra VALUE or ASSURANCE product file. Own status/journal/ONB/RF/evidence are authorized TRACE; disposable output is DERIVED |
| Trigger disposition | Above 5,000-LOC soft prompt, within the original owner-approved coherent split disposition. The move counts both sides; separating it would leave an incomplete dependency boundary or duplicate setup/handoff. Retained predicates, one broad run and independent review are the assurance. No quality exemption or line subtraction |
| Authority and timing | Owner receipt predates execution and approves fixed denominator 4 files/6,400 LOC. Multiplier 2 means 8 files/12,800 LOC; actual reaches neither. No denominator change or late authority |
| Reproduction | Approved four-path NUL-safe `git diff --name-status --find-renames=50% -z` and `git diff --numstat --find-renames=50% -z` with the full Baseline/Candidate above; exact argv and original bytes in EV's single E-accounting row |

### New Files

| File | Description |
|---|---|
| `docs/scripts/test_repository_contracts.py` | Ordinary pure test module: 90 effective test functions, with retained parameterized cases, helpers and source/history contracts |
| `phase-a/ONB__phase-a__proportionate_repository_verification.md` | Previously committed onboarding with no blockers |
| `phase-a/evidence/EV__phase-a__proportionate_repository_verification.md` | Per-claim evidence, one approved-scope accounting row and explicit remaining independent judgments |
| `phase-a/evidence/phase-a-verification.txt`, `phase-a/evidence/phase-a-input-variants.md`, `phase-a/evidence/phase-a-raw.zip` | Commands, variants, native choices and original inspectable receipts |
| This RF and phase-local handoff/transition events | Executor-owned reporting and local state trace; no root state aggregate |

### Modified Files

| File | Changes |
|---|---|
| `docs/scripts/test_integration.py` | Pure definitions transferred; original output bodies/build retained; imports narrowed |
| `docs/scripts/test_runtime_context.py` | Only `LEDGER_SPECS` R10/R14 source targets point to the new module |
| `tools/README.md` | Six change→risk selections, output/broad triggers, claim-specific reuse, semantic/native evidence and existing configured gates |
| `phase-a/status.md` | Own lifecycle ONB → RF at the recorded clock second |

The complete 156-body baseline disposition, 150 current function/helper dependency map and exact body hashes are attached in EV. Seven earlier overwritten bodies disappear. Two aliases resolve to the already-collected `test_phase_d_approval_epoch_protects_history_inputs_and_cumulative_prefixes` and `test_phase_d_added_product_provider_terms_are_confined_to_adapter_and_named_exception`; those substantive targets remain. `_cratm_authority_consumer_errors` and `_phase_d_git_paths` were orphaned by already superseded bodies and are removed. The board guard retains its consequence with self-exclusion based on the containing filename.

## 2. Key Decisions

1. Keep output consumers with one build fixture and move source checks as an ordinary module. No conftest coupling, permanent runner, cache, registry or receiver requirement is introduced. MOVE/KEEP identities and actual absent/stale observations jointly establish the boundary.
2. Rework both current knowledge row locks explicitly. The Phase D closure check now reads its actual immutable knowledge Candidate snapshot. The Phase E check preserves historical full-row identity at the real K2 epochs, while current checks cover structure/provenance. Exact wording, synthetic successor and authority-distortion inputs are supplied for independent semantic judgment.
3. Preserve the initial failed pure run. Two incorrect selectors caused three failures; the Coordinator prospectively allocated one correction process. All three dependency-affected tests passed with no site; 121 unaffected observations were reused with their unchanged dependencies. The complete stale family and later broad run passed on the final same source bytes.
4. Follow canonical Candidate chronology: test final working bytes at `62cb3f58a56c2dc8e69fd5f67366264f10725c6d`, commit Candidate, audit all 1,984 source files and Git-dependent semantics, then write EV/RF. The SHA did not exist before execution. Later reporting traces do not move Candidate and have no blanket full-suite PASS claim.
5. Use one comparable unchanged-scanner pair and one ordinary adverse output path. Pair 01/07 uses identical global pytest 9 with the disclosed dependency-range limitation; ordinary acceptance runs use isolated pytest 8.4.2. No baseline/full repeat was made to improve statistics. The real generator variation was confined to a disposable root and restored after capture.
6. Keep the AC4 native exercise independent before unblinding. Both existing holders rejected changed-oracle reuse and preserved unrelated evidence. Different selection breadth and the Reviewer's missing-output-dependency challenge remain visible. These choices establish only this bounded maintainer example.

## 3. Acceptance Criteria

- [x] AC-1 Executor evidence: preserved output family and live ledger targets; complete dependency/disposition map; source family observed without builds under absent and stale output.
- [x] AC-2 Executor evidence: obsolete bodies/aliases removed with surviving protective targets and meaningful existing negative cases observed.
- [x] AC-3 executable portion: historical identity, current structure/provenance, harmless-input acceptance and structural adverse consequences observed with zero-build source checks.
- [ ] AC-3 independent semantic portion: assigned Reviewer must judge the exact harmless wording, existing approved successor sources and principal/unit authority distortion. Structural green is insufficient.
- [x] AC-4 bounded native evidence: identical guide and raw cases, independently formed choices, affected-oracle reuse rejected and configured gates retained.
- [x] AC-5 Executor observations: comparable local cost pair, configured collection/full run, genuine fresh-build defect detection, unchanged tested-source→Candidate crossing and approved accounting.
- [ ] AC-5 independent acceptance and later landing: Reviewer/root responsibilities remain pending. Reviewed, landed and published are separate states.

## 4. Verification

- Lint (`python -m pytest tools/tests/ docs/scripts/ -q --collect-only`): **549 collected**, 0.98 s pytest summary, exit 0.
- Tests (`python -m pytest tools/tests/ docs/scripts/ -q`): **548 passed, 1 skipped**, 557.84 s pytest summary; 558.657059 s process wall, exit 0. Existing skip is `tools/tests/test_migrate_board_2_0.py::test_repository_accounting_balances`: “board already removed — accounting is frozen in BOARD-SNAPSHOT.md”. It was recovered from the existing event/source without a rerun.
- Build: full-suite ordinary MkDocs build succeeds. The adverse ordinary build also succeeds, then the unchanged frontmatter-leak test reports the intended single-page defect. Expected adverse pytest exit 1 is detection evidence, not a failing Candidate build.
- Local unchanged-scanner pair: **148.519337 s → 0.989397 s** process wall, **147.529940 s lower**, MkDocs **1 → 0**. One local pair; exact subject bodies, 1,968 shared non-VALUE source files, runtime/env and absent-output preconditions are recorded. No universal speedup or changed-knowledge timing claim.
- Total actual use: **8 pytest / 3 MkDocs**, zero nested pytest. Measured commands plus separately labeled 120 s and 180 s preparation/closeout bounds yield **1,539.239969 s** Executor accounting. Adding the Coordinator's separate 0.154197 s read gives **1,539.394166 s** against the common 3,600 s ceiling. Common balance at return: **2 pytest / 1 MkDocs / 2,060.605834 s**; use requires Coordinator routing. Executor's process/build allocation is exhausted. Native labor, tokens and money remain unknown.

## 5. Evidence

See [EV file](evidence/EV__phase-a__proportionate_repository_verification.md) for evidence details.

Evidence verdict: **8/10 VERIFIED, 2 DEFERRED, 0 BLOCKED, 0 N/A**. Deferred semantic acceptance and independent Candidate/landing judgment are named above; the RF is ready for the assigned independent Reviewer, not a phase PASS declaration.

## 6. Observations (out-of-scope, not modified)

No observations. The local pytest 9 comparison limitation, failed/corrected attempt and existing conditional skip are verification qualifications recorded above, not newly discovered product defects.

## 7. Fact Candidates

No fact candidates. Execution-time resource routing and owner scope authority are already recorded in their governing traces; no new human-sourced domain fact was supplied for promotion.

## 8. Strategic Insights (Execution)

No strategic insights.

## 9. Diagrams

No diagrams.

*RF — TFW_20260907-133942_PTTC / Phase A | 2026-09-08*
