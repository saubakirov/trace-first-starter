# EV — TFW_20260913-151442_RWNR / Phase B: Retire the public Resume surface

> **Date**: 2026-09-14
> **Author**: robert, Executor unit `01a09b39-f0c0-70c0-9b53-6981647e72fb`
> **Task**: TFW_20260913-151442_RWNR
> **TS**: [TS Phase B](../TS__phase-b__resume_surface_retirement.md)
> **Candidate epoch**: `6d3f3890ece2f357ab6353d4fd15a28fe4f3767c` — rejected and unlanded
> **C1 restore**: `d09d5d49496d13b64552fe99a03821826ae435b6`

---

## Environment

| Field | Value |
|---|---|
| OS | Windows local worktree |
| Language / Runtime | Python 3.13.5; Git 2.42.0.windows.1 |
| Database | N/A |
| Deploy target | N/A — release and external effects are G2-forbidden |
| CI / Pipeline | Local configured maintainer commands |

## Evidence

Rows E1–E6 describe observations made against the immutable rejected Candidate. They remain truthful
Candidate-epoch evidence, but do not make that Candidate acceptable after E7 failed. E8 records the
selected C1 outcome and the restored live state.

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1 | AC-1 | Candidate removed exactly the five approved artifacts, modified the other 25 VALUE paths, exposed exactly ten manifest commands, classified all 216 Resume-related matches, and introduced no replacement route. | Git objects and Python tests at Candidate `6d3f3890ece2f357ab6353d4fd15a28fe4f3767c` | VERIFIED | `phase-b-surface.json`; Candidate-targeted suite in `phase-b-tests.txt` |
| E2 | AC-2 | All four adapter receivers resolved the ten-command Candidate topology; exact-copy and managed-block ownership, empty Cursor receiver, clean install, foreign-neighbor refusal, and second-run idempotence passed. | Real temporary receiver trees driven by Candidate sources | VERIFIED | `phase-b-receivers.json` |
| E3 | AC-3 | An evidence-only pinned synthetic guide exercised `ABSENT`, `TARGET_CURRENT`, `OWNED_EXACT`, `OWNED_BLOCK`, and atomic `FOREIGN_OR_DRIFTED` refusal without creating repository release metadata. | Temporary Git source/receiver projects; no external effect | VERIFIED | `phase-b-receivers.json` |
| E4 | AC-4 | The 179-entry task manifest retained digest `ed52c4c26845e90c14a569f867ec2200b18da44374f7df2fd897bf7fb58bef96`; all protected path/mode/blob and aggregate raw-line subsequence oracles and mutants passed. | Immutable Git objects plus Candidate tree | VERIFIED | `phase-b-history.json` |
| E5 | AC-5 | Candidate kept canonical Plan at 1,199 words, kept both accepted copies byte-equal, and passed retained Phase A routing, lifecycle, identity, Role Lock, receiver, negative, and mutant checks. | Candidate-targeted Python suite | VERIFIED | `phase-b-tests.txt`; `phase-b-surface.json` |
| E6 | AC-6 | Baseline→Candidate VALUE membership was exactly 30 logical text files: 5 DELETE, 25 MODIFY, 25 additions + 326 deletions = 351 touched LOC; no extra implementation path, binary path, or unclassified instruction path occurred; `C = 1,523 < B = 2,737`. | Git NUL-safe name-status/numstat and strict UTF-8 word accounting | VERIFIED | `phase-b-accounting.json` |
| E7 | AC-7 | Targeted Candidate gate passed 357 tests and configured collection found 627 tests, but the required configured execution failed 19 cases because `docs/scripts/command_entry_eval.py:89-93` still hard-codes `resume` and the eleven-command contract. That file is outside the approved selector and cannot be changed or waived by this Executor. | `python -m pytest tools/tests/ docs/scripts/ -q` at Candidate | BLOCKED | `phase-b-tests.txt` — 19 failed, 607 passed, 1 skipped |
| E8 | AC-8 | C1 was selected. Candidate remains unlanded; restore commit `d09d5d49496d13b64552fe99a03821826ae435b6` makes all 32 implementation paths byte-identical to pre-Candidate `589409c571916158e294659d6b90a74b758318fc`, restores all five Resume files and the exact eleven-command manifest, and passes the focused 31-case command-entry suite plus 32 state tests. | Restored Executor worktree; accepted `master` remains `4539234b55386c6c1ca652f172b2c90f4aa3407c` | VERIFIED | `phase-b-tests.txt`; restore commit |
| E9 | AC-9 | No migration guide, changelog/version/tag choice, `/tfw-release` dispatch, push, publish, deploy, notification, or other external effect occurred. G2 remains unavailable because Phase B is not accepted. | Repository scope and dispatch lineage | N/A | Candidate/TRACE scope in `phase-b-surface.json`; `phase-b-tests.txt` |
| E-accounting | AC-6 | Approval `8920124c851fdeff6e3b77cfb729d9ca7ffbe73c`, TS blob `108863dd978b9e65b713f9d2feb99a8263c16857`; Baseline `d366bb1d6d70cf457acba84d4b5aafeb5c5f5b14`, Candidate `6d3f3890ece2f357ab6353d4fd15a28fe4f3767c`; exact literal 30-path VALUE selector; every path/action/class/reason is recorded; 30 logical text files, 25 + 326 = 351 LOC, binary N/A; connected phase retained; immutable 30/650 authority precedes work; NUL-delimited `git diff --name-status -z --no-renames` and `git diff --numstat -z --no-renames` reproduced the result. Terminal accounting verdict is `METRICS_PASS__CONFIGURED_GATE_BLOCKED`. | Repository Git/Python environment | VERIFIED | `phase-b-accounting.json` |

## Verdict

Evidence verdict: **8/10 VERIFIED, 0 DEFERRED, 1 BLOCKED, 1 N/A. Overall: BLOCKED; C1 restored the accepted live-Resume state.**

## Attachments

| File | Description |
|---|---|
| `phase-b-surface.json` | Candidate surface inventory, 216 match classifications, exact actions, and mutants |
| `phase-b-receivers.json` | Clean install, owned-only update, atomic refusal, idempotence, and C1 models |
| `phase-b-history.json` | Immutable history manifest, aggregate subsequences, and mutants |
| `phase-b-accounting.json` | Exact selector, numstat, instruction accounting, denominator, and gated verdict |
| `phase-b-tests.txt` | Raw command/result summary, 19 failed node IDs, cause, and completed C1 restoration |

---

*EV — TFW_20260913-151442_RWNR / Phase B: Retire the public Resume surface | 2026-09-14*

## Revision 2 — fresh Candidate evidence

> **Governing TS**: [TS Phase B revision 2](../TS__phase-b__resume_surface_retirement__rev2.md)
> **TS freeze / blob**: `e5efd3e608975184995d254bc5eb84176b8b4451` / `8c06e15e3ad8211195f2d48314d055ad1f111979`
> **Fresh Candidate**: `6d6d094ac5325377772f26ddf314b965c1dfd135`
> **Candidate parent**: `a1857064c14c72ad12996d808f0e810a432dbcf6`
> **Disposition**: tested, ready for independent review, unlanded

The earlier E1–E-accounting rows remain the immutable revision-1/C1 epoch. The following rows are
fresh revision-2 observations. Detailed receiver, history, and VALUE accounting receipts are reused
only where all 30 claim-relevant VALUE inputs are byte-identical to the rejected Candidate; their
changed selector/evaluator dependencies and final output were independently exercised against the new
Candidate in both the 388-case targeted and 626-case configured suites.

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E10 | AC-1 | Candidate has exactly five approved deletions and 25 approved VALUE modifications, the exact ten-command manifest, no substitute, and 206 Git-tree Resume-related matches classified with zero `LIVE` results. | Immutable Candidate Git tree | VERIFIED | `phase-b-surface.json` → `revision_2_validation` |
| E11 | AC-2 | All four adapters still produce exact ten-command clean receivers, preserve foreign outer bytes, accept empty Cursor command state, refuse invalid roots, and converge with an empty second run. All claim-relevant VALUE inputs are byte-identical to the detailed earlier receipt, and the Candidate-bound receiver oracle passed twice. | Real temporary receiver trees in targeted/configured pytest | VERIFIED | `phase-b-receivers.json` → `revision_2_validation`; `phase-b-tests.txt` |
| E12 | AC-3 | The evidence-only pinned synthetic guide still exercises all five ownership classes; successful update is owned-only/idempotent and any foreign connected subject refuses the whole group without a write. No real migration/version identity was created. | Temporary Git source/receiver projects | VERIFIED | `phase-b-receivers.json` → `revision_2_validation`; Candidate-bound oracle |
| E13 | AC-4 | The 179-entry manifest retains digest `ed52c4c26845e90c14a569f867ec2200b18da44374f7df2fd897bf7fb58bef96`, no protected mismatch exists, all three aggregate subsequences hold, and history mutants fail. Claim-relevant VALUE/history inputs are unchanged from the detailed earlier receipt. | Immutable Git objects and Candidate-bound history oracle | VERIFIED | `phase-b-history.json` → `revision_2_validation` |
| E14 | AC-5 | Canonical Plan remains 1,199 words and byte-fixed with its two accepted copies; all retained Phase A route, lifecycle, identity, Role Lock, negative, receiver, and semantic mutant cases pass. | Candidate-bound targeted and configured suites | VERIFIED | `phase-b-tests.txt`; `phase-b-surface.json` |
| E15 | AC-6 | Exact VALUE selector remains 30 text files, 5 DELETE + 25 MODIFY, 25 additions + 326 deletions = 351 touched LOC; `C=1,523 < B=2,737`, with no unclassified instructional addition. | Candidate-bound NUL-safe Git accounting and strict UTF-8 words | VERIFIED | `phase-b-accounting.json` → `revision_2_validation` |
| E16 | AC-7 | Candidate contains exactly the 30 VALUE + three ASSURANCE paths. Evaluator contains the ten surviving commands and exact ten-command refusal; excluded `test_command_entry_eval.py` retains blob `7f195b31c622ac8cdbd7dad0a0f2e9ae7fa7a539`. Targeted 388/388, collection 627, full 626 passed + one skip, focused 31/31, and state 32/32 all pass. | Windows, Python 3.13.5, Git 2.42; immutable Candidate | VERIFIED | `phase-b-tests.txt`; `phase-b-surface.json` |
| E17 | AC-8 | Restored-state preflight, mid-application scope oracle, rejected-Candidate, and landing-mismatch C1 models remain green. Candidate is unlanded; current rewritten shared master and foreign OTR content never entered implementation, accounting, staging, or proof. | Isolated detached worktree and Candidate-bound mutants | VERIFIED | `phase-b-receivers.json`; `phase-b-tests.txt`; exact Candidate diff |
| E18 | AC-9 | Candidate and TRACE contain no migration guide, changelog/version/tag change, release route, TKL import, or external effect. G2 remains closed pending independent acceptance and later LEAD landing checks. | Candidate/TRACE scope and direct dispatch lineage | N/A | `phase-b-surface.json`; `phase-b-tests.txt` |
| E-accounting-R2 | AC-6 | Approval/freeze `e5efd3e608975184995d254bc5eb84176b8b4451`, TS blob `8c06e15e3ad8211195f2d48314d055ad1f111979`; Baseline `d366bb1d6d70cf457acba84d4b5aafeb5c5f5b14`, Candidate `6d6d094ac5325377772f26ddf314b965c1dfd135`; the 30 literal VALUE paths retain their approved path/action/class/reason membership and the three exact ASSURANCE paths are separately recorded; phase attribution is resolved, not `INVALID`; 30 logical text files, 25 + 326 = 351 LOC, binary N/A; connected phase retained; immutable 30/650 authority preceded work and did not ratchet; the exact NUL-safe name-status/numstat method was reproduced. | Repository Git/Python environment | VERIFIED | `phase-b-accounting.json` → `revision_2_validation`; `phase-b-tests.txt` |

### Revision 2 verdict

Evidence verdict: **9/10 VERIFIED, 0 DEFERRED, 0 BLOCKED, 1 N/A. Overall: READY FOR INDEPENDENT REVIEW; Candidate remains unlanded.**

### Revision 2 attachments

| File | Revision-2 resolving content |
|---|---|
| `phase-b-surface.json` | Exact Candidate selector/actions, evaluator and excluded-test identities, 206 Git match classifications, zero live matches, and green gates |
| `phase-b-receivers.json` | Detailed prior receipt plus explicit relevant-input parity and fresh Candidate-bound receiver/update verdict |
| `phase-b-history.json` | Detailed prior receipt plus exact 179-entry/digest/aggregate parity and fresh Candidate-bound history verdict |
| `phase-b-accounting.json` | Exact rev2 approval, 30+3 membership, VALUE numstat, Plan/C calculation, denominator, method, and terminal PASS |
| `phase-b-tests.txt` | Full round chronology, pre-freeze and Candidate-bound commands, exact results, correction, and independent corroboration |

---

*EV return round 2 — TFW_20260913-151442_RWNR / Phase B | 2026-09-14*

## Return Round 3 — real AC-8 recovery evidence

> **Governing TS**: [TS Phase B revision 2](../TS__phase-b__resume_surface_retirement__rev2.md)
> **TS blob**: `8c06e15e3ad8211195f2d48314d055ad1f111979`
> **Independent REVIEW producer / verdict**: `efa7cdd2ad66856d2be5e5799a82ba67e4c1b7cc` / `REVISE`
> **C1 implementation baseline**: `5cfca7abfa51fe3f565295ca4fc8be81c74c474f`
> **Fresh Candidate**: `a81e0c12ec982ee4f73639ebf15394ef53877294`
> **Candidate parent**: `5cfca7abfa51fe3f565295ca4fc8be81c74c474f`
> **Disposition**: tested, ready for the reserved independent Reviewer, unaccepted and unlanded

Earlier epochs remain immutable. In particular, Candidate
`6d6d094ac5325377772f26ddf314b965c1dfd135` retains its `REVISE`, unaccepted, unlanded
disposition and is not reused as acceptance evidence. This epoch resolves only REVIEW §4.1: the
former declarative C1 boolean was replaced by observable temporary-tree recovery, complete 33-path
byte maps, and hostile mutants. All other product bytes retain the coherent revision-2 result.

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E19 | AC-1 | Candidate has exactly five approved deletions and 25 approved VALUE modifications, an exact ten-command manifest, no Resume substitute, and no unclassified live match. | Immutable Candidate Git tree and Candidate-bound selector oracle | VERIFIED | `phase-b-tests.txt`; unchanged detailed surface receipt |
| E20 | AC-2 | Four-adapter clean receiver, ownership boundary, whole-group refusal, and repeat-idempotence contracts pass against the new Candidate. | Real pytest temporary receiver trees | VERIFIED | `phase-b-tests.txt`; retained detailed receiver epoch |
| E21 | AC-3 | The evidence-only pinned update fixture still covers all five ownership classes and creates no real migration/version identity. | Candidate-bound configured suite; temporary Git fixtures | VERIFIED | `phase-b-tests.txt`; retained detailed receiver epoch |
| E22 | AC-4 | The 179-entry history and aggregate-preservation oracles and mutants pass; no history, aggregate, knowledge, digest, or TKL path entered the Candidate. | Immutable Git objects and Candidate-bound history oracle | VERIFIED | `phase-b-tests.txt`; retained detailed history epoch |
| E23 | AC-5 | Canonical Plan and accepted copies remain byte-fixed; all Phase A route, lifecycle, identity, Role Lock, negative, and semantic-mutant cases pass. | Candidate-bound targeted and configured suites | VERIFIED | `phase-b-tests.txt` |
| E24 | AC-6 | VALUE remains exactly 30 text paths, 5 DELETE + 25 MODIFY, 25 additions + 326 deletions = 351 touched LOC; Plan is 1,199 words and `C=1,523 < B=2,737`, with no unclassified instruction change. | NUL-safe Git diff and strict UTF-8 accounting against immutable Candidate | VERIFIED | `phase-b-tests.txt`; unchanged detailed accounting result |
| E25 | AC-7 | Candidate is exactly 30 VALUE + 3 ASSURANCE paths; excluded evaluator test retains blob `7f195b31c622ac8cdbd7dad0a0f2e9ae7fa7a539`. Candidate-bound targeted is 392/392, collection is 631, full is 630 passed + one skip, focused is 31/31, state is 32/32, and `diff --check` is clean. | Windows, Python, Git; immutable Candidate | VERIFIED | `phase-b-tests.txt` |
| E26 | AC-8 | Four real temporary-tree cases — preflight failure, injected mid-application failure after one connected-group delete, Reviewer rejection, and landing/integrated mismatch — each derive a complete 33-path SHA-256 map, restore it to C1 before-image digest `1a2d5d271b7ae2cf5c246f0b1344b71a0cbb1143a00c8204c8d853fcb292c666`, and observe no release route/effect. Altered-path, retained-deletion, and emitted-release-route mutants each fail the oracle. | Real filesystem operations under pytest `tmp_path`; Candidate-bound source bytes | VERIFIED | `phase-b-receivers.json` → `return_round_3`; `phase-b-tests.txt` |
| E27 | AC-9 | Candidate and TRACE contain no release metadata mutation or external effect. No release route, landing, shared-history import, G2 action, push, publish, deploy, or notification occurred. | Exact Candidate/TRACE scope and current execution lineage | N/A | `phase-b-receivers.json` → `return_round_3`; `phase-b-tests.txt` |
| E-accounting-R3 | AC-6 | TS blob and 30/650 authority remain unchanged. Candidate `a81e0c12ec982ee4f73639ebf15394ef53877294` has parent `5cfca7abfa51fe3f565295ca4fc8be81c74c474f`, exactly 33 implementation paths, 30/351 actual VALUE accounting, no added VALUE, and a clean literal staged-set audit of 33 staged, zero missing, zero extra from an initially empty index. | Repository Git/Python environment | VERIFIED | `phase-b-tests.txt` |

### Return Round 3 verdict

Evidence verdict: **9/10 VERIFIED, 0 DEFERRED, 0 BLOCKED, 1 N/A. Overall: READY FOR
INDEPENDENT REVIEW; Candidate remains unaccepted and unlanded.**

The verdict does not supersede the independent Reviewer and does not authorize landing or G2. The
same reserved Reviewer must review this return.

---

*EV return round 3 — TFW_20260913-151442_RWNR / Phase B | 2026-09-14*

## Return Round 4 — exact-path Candidate process evidence

> **Governing TS**: [TS Phase B revision 2](../TS__phase-b__resume_surface_retirement__rev2.md)
> **TS blob**: `8c06e15e3ad8211195f2d48314d055ad1f111979`
> **Binding REVIEW producer / verdict**: `9eaf775cc0ff3a28e3c989e4018d34b3b707eb57` / `REVISE`
> **Closed ruling**: live REVIEW §8.7, accepted rung 1
> **C1 implementation baseline**: `41a70febc6d33d369af125d7ad2ecf98a2de0761`
> **Fresh Candidate**: `51ea3015290393da001810629f305f5969f4c8b8`
> **Candidate parent**: `41a70febc6d33d369af125d7ad2ecf98a2de0761`
> **Disposition**: tested, ready for the same independent Reviewer, unaccepted and unlanded

Earlier epochs remain immutable. Candidate `a81e0c12ec982ee4f73639ebf15394ef53877294`
retains its `REVISE`, unaccepted and unlanded disposition. This return changes no implementation
semantics: all 33 approved path bytes in the fresh Candidate are identical to that corrected
implementation. It resolves only the exact-path process and durable raw-evidence defect in REVIEW
§8.4–§8.7.

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E28 | AC-1 | Fresh Candidate contains the same exact five approved deletions, 25 VALUE modifications, ten-command manifest, no substitute, and no unclassified live match as the corrected return. | Immutable Candidate Git tree; 33-path byte comparison | VERIFIED | `phase-b-candidate-boundary-round4.txt`; `phase-b-tests.txt` |
| E29 | AC-2 | Four-adapter receiver, ownership boundary, whole-group refusal, and repeat-idempotence contracts pass in the fresh Candidate-bound targeted and configured suites; all 33 approved implementation inputs are byte-identical to the corrected return. | Real pytest temporary receiver trees and Git byte oracle | VERIFIED | `phase-b-targeted-round4.txt`; `phase-b-full-round4.txt`; retained detailed receiver epoch |
| E30 | AC-3 | The evidence-only pinned update fixture and all five ownership classes remain covered by the Candidate-bound suites; no release identity was created. | Candidate-bound configured suite; temporary Git fixtures | VERIFIED | `phase-b-full-round4.txt`; retained detailed receiver epoch |
| E31 | AC-4 | Protected task/aggregate history oracles and mutants pass; no history, aggregate, knowledge, digest, or TKL path entered Candidate or TRACE. | Immutable Git objects and Candidate-bound history oracle | VERIFIED | `phase-b-targeted-round4.txt`; `phase-b-full-round4.txt`; retained detailed history epoch |
| E32 | AC-5 | Canonical Plan and accepted-copy bytes remain fixed; retained Phase A routing, lifecycle, identity, Role Lock, negative, receiver, and mutant tests pass. | Candidate-bound targeted and configured suites | VERIFIED | `phase-b-targeted-round4.txt`; `phase-b-full-round4.txt` |
| E33 | AC-6 | VALUE is exactly 30 text paths, 5 DELETE + 25 MODIFY, 25 additions + 326 deletions = 351 touched LOC; Plan is 1,199 words and `C=1,523 < B=2,737`, with no unclassified instruction change. | Candidate-bound NUL-safe Git accounting and strict UTF-8 words | VERIFIED | `phase-b-accounting.json` → `return_round_4_validation`; `phase-b-tests.txt` |
| E34 | AC-7 | Before Candidate freeze, the complete full-status, empty-index, literal ordered selector/staging command, staged names/actions, and 33/33/missing-0/extra-0 audit were captured outside the repository. The actual commit used `git commit -m <message> --only -- <all 33 literal paths>`. Post-status/scope and exact result were appended before the receipt was copied into TRACE. Candidate-bound targeted is 392/392, collection is 631, full is 630 passed + one skip, focused is 31/31, state is 32/32, and diff check is clean. | Outside-repository pre/post receipt copied byte-identically after freeze; immutable Candidate | VERIFIED | `phase-b-candidate-boundary-round4.txt` (SHA-256 `4c3350df1a496af6de502c10f2dd9ca773a4872167ca53d573008831bc476530`); `phase-b-targeted-round4.txt`; `phase-b-full-round4.txt`; `phase-b-tests.txt` |
| E35 | AC-8 | Fresh Candidate is byte-identical over all 33 approved paths to corrected Candidate `a81e0c12…`; the real recovery models and hostile mutants are unchanged and passed within both complete Candidate-bound suites. No raw evidence path entered Candidate. | Exact Git path-byte comparison; Candidate-bound pytest | VERIFIED | `phase-b-candidate-boundary-round4.txt`; `phase-b-targeted-round4.txt`; `phase-b-full-round4.txt`; retained `phase-b-receivers.json` → `return_round_3` |
| E36 | AC-9 | Candidate and TRACE contain no release metadata mutation or external effect. No landing, shared-history import, G2 action, push, publish, deploy, or notification occurred. | Exact Candidate/TRACE scope and execution lineage | N/A | `phase-b-candidate-boundary-round4.txt`; `phase-b-tests.txt` |
| E-accounting-R4 | AC-6 | Approval `e5efd3e608975184995d254bc5eb84176b8b4451`, TS blob `8c06e15e3ad8211195f2d48314d055ad1f111979`; VALUE baseline `d366bb1d6d70cf457acba84d4b5aafeb5c5f5b14`; C1 parent `41a70febc6d33d369af125d7ad2ecf98a2de0761`; Candidate `51ea3015290393da001810629f305f5969f4c8b8`; exact 30 VALUE + three ASSURANCE membership; 30 logical text files, 25 + 326 = 351 LOC, binary N/A; immutable 30/650 denominator; no unclassified path; copy and managed-block parity all true; exact boundary evidence records an initially empty index and literal 33-path `commit --only` process. | Repository Git/Python environment | VERIFIED | `phase-b-accounting.json` → `return_round_4_validation`; `phase-b-candidate-boundary-round4.txt` |

### Return Round 4 verdict

Evidence verdict: **9/10 VERIFIED, 0 DEFERRED, 0 BLOCKED, 1 N/A. Overall: READY FOR
INDEPENDENT REVIEW; Candidate remains unaccepted and unlanded.**

This evidence resolves the sole exact-path process/durability return bound. It does not supersede
the same independent Reviewer, authorize landing, or open G2.

### Return Round 4 attachments

| File | Resolving content |
|---|---|
| `phase-b-candidate-boundary-round4.txt` | Byte-identical outside-repository pre/post boundary receipt, exact commands and complete inventories |
| `phase-b-targeted-round4.txt` | Raw observed Candidate-bound targeted command/result |
| `phase-b-full-round4.txt` | Raw observed Candidate-bound configured-full command/result |
| `phase-b-accounting.json` | Candidate-bound `return_round_4_validation` accounting and identities |
| `phase-b-tests.txt` | Cumulative round chronology and all completed Candidate-bound outcomes |

---

*EV return round 4 — TFW_20260913-151442_RWNR / Phase B | 2026-09-14*

## Landing Composite — fresh-master Candidate evidence

> **Governing TS**: [TS Phase B revision 2](../TS__phase-b__resume_surface_retirement__rev2.md)
> **TS blob**: `8c06e15e3ad8211195f2d48314d055ad1f111979`
> **Accepted Phase-B Candidate / REVIEW**: `51ea3015290393da001810629f305f5969f4c8b8` / `14da05a4f1b4a341f30b75fce4f572db2c367b2d` (`APPROVE`)
> **Landing contract producer**: `f979eac49bc3acd0d0220591047ec8abccf49072`
> **Fresh master / landing Candidate**: `3fd16fd1549a3f92006e8f37102df4a511b8aa55` / `3c354ba29d525ccb4e7683c5c477290682b90a5a`
> **Landing Candidate tree**: `7b61356eb8990ccec78cb9f4275dbae305948eb1`
> **Disposition**: product frozen and tested; ready for affected review; not landed

All earlier evidence epochs remain immutable. This epoch verifies the owner-approved semantic
composition of the accepted Phase-B result with the current TKL release line. It does not reinterpret
the accepted Phase-B accounting, supersede the independent Reviewer, or authorize landing.

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E37 | AC-1 | The fresh-master Candidate has the exact five approved deletions and 25 approved VALUE modifications, the ten-command manifest, no public Resume substitute, and no unclassified live Resume surface. | Clean detached checkout at `3c354ba29d525ccb4e7683c5c477290682b90a5a` | VERIFIED | `phase-b-landing-targeted.txt`; `phase-b-landing-candidate-boundary.txt` |
| E38 | AC-2 | Canonical and installed receiver topology, managed ownership boundaries, foreign-neighbor refusal, empty Cursor receiver, and second-run convergence pass within both complete Candidate-bound suites. | Real temporary receiver trees in clean detached Candidate checkout | VERIFIED | `phase-b-landing-targeted.txt`; `phase-b-landing-full.txt` |
| E39 | AC-3 | The evidence-only pinned update fixture still covers all five ownership classes, preserves owned-only atomic refusal, and creates no release/version identity. | Candidate-bound configured suite and temporary Git fixtures | VERIFIED | `phase-b-landing-full.txt` |
| E40 | AC-4 | Nineteen clean-preimage paths reproduce the accepted Candidate after-images exactly; fourteen TKL-diverged paths preserve both accepted retirement semantics and the fresh-master TKL 3.4 meaning. Per-path master, accepted-parent, accepted-Candidate, and composite blob identities cover 33/33 paths with zero missing or extra. | Git blob oracle against fresh master, accepted Candidate, and landing Candidate | VERIFIED | `phase-b-landing-candidate-boundary.txt`; `phase-b-landing-provenance-check.txt` |
| E41 | AC-5 | Canonical Plan, generated copies, retained Phase-A continuation/authority behavior, and TKL handover semantics pass in the 420-case targeted and 718-pass configured runs. | Clean detached Candidate checkout | VERIFIED | `phase-b-landing-targeted.txt`; `phase-b-landing-full.txt` |
| E42 | AC-6 | Accepted Phase-B VALUE accounting remains the immutable 30 paths, 5 DELETE + 25 MODIFY, 351 touched LOC, Plan 1,199 words, and `C=1,523 < B=2,737`. The fresh-master composite transport is separately recorded as exactly 30 VALUE + three ASSURANCE paths and does not ratchet that accepted denominator. | Accepted evidence plus fresh-master per-path provenance | VERIFIED | `phase-b-accounting.json`; `phase-b-landing-candidate-boundary.txt` |
| E43 | AC-7 | Pre-Candidate status named exactly 33 product paths, the index was empty, exact literal staging had 33 paths with missing 0 and extra 0, and the actual product commit used `git commit --only --` with all 33 literal paths. In a clean detached checkout: targeted 420/420, collection 719, full 718 passed + one skip, focused 31/31, state 32/32, and focused provenance 1/1 all passed. | Windows local Git/Python; immutable landing Candidate | VERIFIED | `phase-b-landing-candidate-boundary.txt`; `phase-b-landing-targeted.txt`; `phase-b-landing-collect.txt`; `phase-b-landing-full.txt`; `phase-b-landing-focused-command-entry.txt`; `phase-b-landing-state.txt`; `phase-b-landing-provenance-check.txt` |
| E44 | AC-8 | Product Candidate parent is exactly fresh master; no merge, rebase, cherry-pick, old-RWNR ancestry transport, wholesale Candidate checkout, broad staging, or post-Candidate product edit occurred. The 36 accepted REVIEW trace paths plus contract event `f764` were transferred byte-exactly with 37/37 selector coverage and zero mismatch. | Separate clean landing and detached verification worktrees | VERIFIED | `phase-b-landing-trace-transfer.txt`; `phase-b-landing-targeted-attempt1.txt` |
| E45 | AC-9 | Candidate, verification, and TRACE preparation performed no shared-master landing, release, G2, tag, push, publish, deploy, notification, OTR mutation, knowledge/digest repair, or other external effect. The 10 MiB audit retains exactly the five grandfathered TKL blobs and introduces no sixth. | Git object inventory and execution lineage | N/A | `phase-b-landing-candidate-boundary.txt` |
| E-accounting-landing | AC-6 | Accepted selector and metric authority remain bound to TS blob `8c06e15e3ad8211195f2d48314d055ad1f111979` and accepted Candidate `51ea3015290393da001810629f305f5969f4c8b8`. Landing Candidate `3c354ba29d525ccb4e7683c5c477290682b90a5a` has parent `3fd16fd1549a3f92006e8f37102df4a511b8aa55`, exactly 33 product paths, 28 MODIFY + 5 DELETE, 19 clean-preimage and 14 semantic-composite paths, and no large-blob addition. This is integration provenance, not a new VALUE denominator. | NUL-safe Git diff, literal selector, per-path blob audit | VERIFIED | `phase-b-landing-candidate-boundary.txt` |

### Landing-composite verdict

Evidence verdict: **9/10 VERIFIED, 0 DEFERRED, 0 BLOCKED, 1 N/A. Overall: READY FOR AFFECTED
INDEPENDENT REVIEW; landing Candidate remains unlanded and Phase B remains KNW.**

The first landing-worktree targeted attempt is retained truthfully in
`phase-b-landing-targeted-attempt1.txt`: it reported 419 passes and one scope-oracle failure because
the transferred tracked TRACE carrier was still an unstaged worktree change. No product byte was
changed in response. LEAD directed final verification in a clean detached checkout at the immutable
Candidate, where every required suite passed.

### Landing-composite attachments

| File | Resolving content |
|---|---|
| `phase-b-landing-candidate-boundary.txt` | Byte-identical external receipt; 33-path pre/post boundary, provenance, commit, diff, and five-large-blob audit |
| `phase-b-landing-provenance-check.txt` | Focused 33-path landing provenance oracle |
| `phase-b-landing-trace-transfer.txt` | Exact 36 REVIEW + one contract-event transfer selector, staging, and blob parity |
| `phase-b-landing-targeted-attempt1.txt` | Truthful non-acceptance attempt in the TRACE-bearing landing worktree |
| `phase-b-landing-targeted.txt` | Raw clean-Candidate targeted output: 420 passed |
| `phase-b-landing-collect.txt` | Full collection output: 719 collected |
| `phase-b-landing-full.txt` | Raw clean-Candidate full output: 718 passed, one skipped |
| `phase-b-landing-focused-command-entry.txt` | Raw focused command-entry output: 31 passed |
| `phase-b-landing-state.txt` | Raw state output: 32 passed |

---

*EV landing composite — TFW_20260913-151442_RWNR / Phase B | 2026-09-14*

## Landing Provenance Return — Rung-1 Evidence Correction

> **Coordinator producer**: `a3f54f4053d5b06502856914712c25c99d0e3fb4`
> **Proposal origin**: Reviewer `{robert, 01a09b82-d0ed-78b1-9b72-42291fd8359e}`
> **Closed bound**: live REVIEW §10.6, accepted rung 1
> **Governing TS blob**: `8c06e15e3ad8211195f2d48314d055ad1f111979`
> **Closing contract producer**: `f979eac49bc3acd0d0220591047ec8abccf49072`
> **Immutable landing Candidate**: `3c354ba29d525ccb4e7683c5c477290682b90a5a`
> **Disposition**: evidence correction complete; Candidate remains unaccepted and unlanded

Earlier evidence remains openable and unchanged. In particular,
`phase-b-landing-candidate-boundary.txt` remains the defective historical receipt whose mistyped
nonexistent parent produced 33 fail-soft `accepted_parent=-` cells and false `A` actions on the 28
surviving paths. Landing-composite E40 and the corresponding RF §14 provenance claim are not reused
as sufficient evidence. The following rows correct that claim without relabeling the earlier epoch.

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E46 | AC-7 / frozen DoD 17 | A new four-epoch table resolves every literal product path against fresh master `3fd16fd1549a3f92006e8f37102df4a511b8aa55`, actual accepted parent `41a70febc6d33d369af125d7ad2ecf98a2de0761`, accepted Candidate `51ea3015290393da001810629f305f5969f4c8b8`, and immutable landing Candidate `3c354ba29d525ccb4e7683c5c477290682b90a5a`. All 33 accepted-parent Git blob OIDs are present; accepted and landing actions are each exactly `28 M + 5 D`; selector missing/extra is zero. | Checked Git object plumbing in the existing clean landing worktree | VERIFIED | `phase-b-landing-provenance-correction.json` — SHA-256 `50029a652b5985f88984a18cd5ca37d28f5c908aa54e1582d76aee6a68be2977`, Git blob `da565f31bb41922011a407dd2fb327411e5b568d` |
| E47 | AC-7 / closing provenance bound | An independent receipt-to-Git validator matched 33/33 rows, reproduced `19 CLEAN_PREIMAGE + 14 COMPOSITE`, including three composite deletions, and rejected invalid-parent mutant `41a70b94019b86b99d87bb48f3da653a51112050` with Git exit 128. Required commit and present-path lookup is fail-closed; only the five expected Candidate deletions may be absent. | Python 3.13 and Git object database; narrow evidence validator only | VERIFIED | `phase-b-landing-provenance-validation.txt` — SHA-256 `314f645c2448580ed4d67df9f57b5f0fae542854a9e61c0d9f22a780329ef738`, Git blob `5ef5d61dc8a3edc49d53a0f61038cfa1fb4224b9` |
| E48 | AC-8 | Historical defective receipt blob `e9be20aeba899c3bba569086dfe502b0ddec2506` is unchanged; no product or ASSURANCE path changed, landing Candidate identity did not move, and phase status remains `KNW`. The focused validator observed zero tested-dependency changes. | Git status, object identity, and exact Phase-B TRACE scope | VERIFIED | Both new receipts; immutable Candidate and historical receipt objects |
| E49 | AC-9 | No master landing, TKL/OTR mutation, knowledge/digest work, DONE, G2, release, tag, push, publish, deploy, notification, or external effect occurred. | Local append-only TRACE execution | N/A | Exact final status/index and commit selector audit in the Executor return |
| E-accounting-provenance | AC-6 / rung-1 scope | The accepted `30 VALUE / 650 LOC` denominator and all product accounting remain unchanged. This return adds zero VALUE and zero ASSURANCE paths; its only mutations are the two new evidence files, this cumulative EV supplement, the cumulative RF supplement, and one handoff event. Existing green regression receipts are reused because tested dependency changes are exactly zero. | Coordinator producer `a3f54f4053d5b06502856914712c25c99d0e3fb4`; NUL-safe final TRACE selector audit | VERIFIED | `phase-b-landing-provenance-validation.txt`; final exact-path commit audit |

### Rung-1 provenance verdict

Evidence verdict: **4/5 VERIFIED, 0 DEFERRED, 0 BLOCKED, 1 N/A. Overall: READY FOR AFFECTED
INDEPENDENT REVIEW; landing Candidate remains unaccepted and unlanded, and Phase B remains KNW.**

The prior green regression receipts remain applicable: targeted 420 passed, collection 719, configured
full 718 passed plus one skipped, focused command-entry 31 passed, and state 32 passed. They were not
rerun because neither product, ASSURANCE, Candidate, command, oracle, runtime dependency, nor
environment assumption changed. The only executed check was the new receipt-bound focused validator.

### Rung-1 provenance attachments

| File | Resolving content |
|---|---|
| `phase-b-landing-provenance-correction.json` | Correct 33-row four-epoch Git blob table, actions, classifications, selector checks, and fail-closed lookup policy |
| `phase-b-landing-provenance-validation.txt` | Exact independent validator source and output; 33/33 match and invalid-parent rejection |

---

*EV landing provenance rung-1 return — TFW_20260913-151442_RWNR / Phase B | 2026-09-14*
