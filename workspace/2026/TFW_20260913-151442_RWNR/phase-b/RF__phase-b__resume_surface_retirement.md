# RF — TFW_20260913-151442_RWNR / Phase B: Retire the public Resume surface

> **Date**: 2026-09-14
> **Author**: robert, Executor unit `01a09b39-f0c0-70c0-9b53-6981647e72fb`
> **Status**: ❌ BLOCKED — configured gate failed; C1 restored the accepted state
> **Parent HL**: [Phase B HL](HL__phase-b__resume_surface_retirement.md)
> **TS**: [TS Phase B](TS__phase-b__resume_surface_retirement.md)

---

## 1. What Was Done

The Executor implemented the exact approved 30-VALUE plus two-ASSURANCE retirement group and froze
Candidate `6d3f3890ece2f357ab6353d4fd15a28fe4f3767c`. Candidate-targeted proof passed, but the mandatory
configured suite exposed a stale eleven-command contract in out-of-scope
`docs/scripts/command_entry_eval.py`. The Executor did not enlarge the selector or waive the failure.
Automatic C1 was selected: Candidate is rejected/unlanded and restore commit
`d09d5d49496d13b64552fe99a03821826ae435b6` returns every implementation path to the coherent
live-Resume baseline.

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | `8920124c851fdeff6e3b77cfb729d9ca7ffbe73c`; TS blob `108863dd978b9e65b713f9d2feb99a8263c16857` |
| Baseline / Candidate | `d366bb1d6d70cf457acba84d4b5aafeb5c5f5b14` / `6d3f3890ece2f357ab6353d4fd15a28fe4f3767c` (first fully tested Executor implementation commit; rejected/unlanded) |
| VALUE membership — DELETE | `VALUE` retirement payloads: `.agents/skills/tfw-resume/SKILL.md`, `.agents/workflows/tfw-resume.md`, `.claude/commands/tfw-resume.md`, `.tfw/adapters/codex/skills/tfw-resume/SKILL.md`, `.tfw/workflows/resume.md` |
| VALUE membership — MODIFY: canonical/config | `VALUE` topology and receiver ownership: `.agent/rules/agents.md`, `.agents/rules/tfw.md`, `.tfw/adapters/antigravity/tfw-rules.md.template`, `.tfw/adapters/claude-code/CLAUDE.md.template`, `.tfw/adapters/codex/AGENTS.md.template`, `.tfw/adapters/cursor/tfw.mdc.template`, `.tfw/adapters/manifest.yaml`, `.tfw/conventions.md`, `.tfw/project_config.yaml`, `.tfw/templates/project_config.yaml`, `AGENTS.md`, `CLAUDE.md` |
| VALUE membership — MODIFY: install/update | `VALUE` canonical/copy receiver convergence: `.agents/workflows/tfw-init.md`, `.agents/workflows/tfw-update.md`, `.claude/commands/tfw-init.md`, `.claude/commands/tfw-update.md`, `.tfw/workflows/init.md`, `.tfw/workflows/update.md` |
| VALUE membership — MODIFY: user docs | `VALUE` public current topology: `.tfw/adapters/README.md`, `.tfw/adapters/antigravity/README.md`, `.tfw/adapters/claude-code/README.md`, `.tfw/adapters/codex/README.md`, `README.md`, `README.ru.md`, `README.kk.md` |
| Arithmetic | 25 additions + 326 deletions = 351 touched text LOC; 30 logical VALUE files; binary/non-text N/A; actions 5 DELETE + 25 MODIFY |
| Membership deviations | None in the Candidate. The later configured-gate cause is outside the approved selector and therefore was observed, not modified. |
| Trigger disposition | 30/351 remained below approved 30/650 and configured 50/5,000; the connected group was not split. Assurance passed, but the mandatory configured gate failed, so terminal disposition is C1/BLOCKED. |
| Authority and timing | Immutable denominator 30/650 and owner-return threshold 60/1,300 were approved before work. No late authority was inferred. |
| Reproduction | Approved NUL-safe `git diff --name-status -z --no-renames` and `git diff --numstat -z --no-renames`; complete calculation in `evidence/phase-b-accounting.json` |

### New Files

| File | Description |
|---|---|
| `ONB__phase-b__resume_surface_retirement.md` | Accepted bounded handoff and resolved identity/context |
| `evidence/phase-b-surface.json` | Rejected Candidate surface and mutant evidence |
| `evidence/phase-b-receivers.json` | Rejected Candidate receiver/update and C1 evidence |
| `evidence/phase-b-history.json` | Rejected Candidate history-preservation evidence |
| `evidence/phase-b-accounting.json` | Rejected Candidate immutable accounting evidence |
| `evidence/phase-b-tests.txt` | Targeted/configured results, failure nodes, and C1 restoration |
| `evidence/EV__phase-b__resume_surface_retirement.md` | Structured evidence verdict |
| `RF__phase-b__resume_surface_retirement.md` | This blocked return |

### Modified Files

| File | Changes |
|---|---|
| `status.md` | Transitioned the phase from `ONB` to `BLOCKED` after C1 restoration |
| `journal/20260914-021737__transition__c1b0.md` | Recorded the failed gate, exact dependency, and direct return |

No product implementation path remains modified in the returned state. The rejected Candidate's exact
30 VALUE and two ASSURANCE changes remain reproducible through its immutable Git identity and evidence.

## 2. Key Decisions

1. Treated all 19 configured failures as one contract defect, not as unrelated or pre-existing failures: every failure is caused by `docs/scripts/command_entry_eval.py:89-93` requiring `resume` and eleven commands.
2. Did not modify that file because it is not one of the exact 30 VALUE or two ASSURANCE paths approved by the TS; the Executor has no amendment authority.
3. Selected C1 immediately after the mandatory gate failed, preserving the rejected Candidate as evidence while restoring the entire connected implementation group.
4. Kept G2 closed and performed no release, knowledge, landing, review, or external effect.

## 3. Acceptance Criteria

- [x] AC-1 — exact no-replacement retirement was proven at the rejected Candidate epoch.
- [x] AC-2 — canonical adapter and clean-install behavior was proven at the rejected Candidate epoch.
- [x] AC-3 — synthetic version-addressed owned-only update and atomic refusal were proven at the rejected Candidate epoch.
- [x] AC-4 — historical task and aggregate truth was proven unchanged at the rejected Candidate epoch.
- [x] AC-5 — accepted Phase A continuation and authority tests remained green at the rejected Candidate epoch.
- [x] AC-6 — exact 30-path, 351-LOC and `C = 1,523 < B = 2,737` accounting was proven.
- [ ] AC-7 — **BLOCKED**: mandatory configured execution has 19 failures caused by one out-of-scope hard-coded eleven-command expectation.
- [x] AC-8 — C1 was applied as a whole group; Candidate is unlanded and all 32 implementation paths were restored byte-for-byte.
- [x] AC-9 — N/A for release effects; the G2 stop remains intact and no effect occurred.

## 4. Verification

- Candidate targeted gate (`python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_repository_contracts.py -q`): **357 passed in 371.95s**.
- State schema at Candidate (`python -m pytest tools/tests/test_tfw_state.py -q`): **32 passed**.
- Configured collection (`python -m pytest tools/tests/ docs/scripts/ -q --collect-only`): **627 collected**.
- Configured full gate (`python -m pytest tools/tests/ docs/scripts/ -q`): **BLOCKED — 19 failed, 607 passed, 1 skipped in 582.58s**.
- Focused reproduction at Candidate (`python -m pytest docs/scripts/test_command_entry_eval.py -q --tb=line`): **19 failed, 12 passed**.
- Focused C1 restoration check (`python -m pytest docs/scripts/test_command_entry_eval.py -q`): **31 passed in 42.34s**.
- Restored state schema (`python -m pytest tools/tests/test_tfw_state.py -q`): **32 passed in 0.33s**.
- Restored surface: exact accepted eleven-command manifest, all five Resume artifacts present, all 30 VALUE + two ASSURANCE paths byte-identical to `589409c571916158e294659d6b90a74b758318fc`.

## 5. Evidence

See [Phase B EV](evidence/EV__phase-b__resume_surface_retirement.md) for evidence details.

Evidence verdict: **8/10 VERIFIED, 0 DEFERRED, 1 BLOCKED, 1 N/A. Overall: BLOCKED with C1 restored.**

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|---|---|---|---|
| 1 | `docs/scripts/command_entry_eval.py` | 89–93 | missing-test / stale-assurance | `REQUIRED_COMMANDS` still includes `resume` and its assertion requires the exact eleven-command contract. A revised Phase B selector must authorize this file before the configured suite can validate retirement. `docs/scripts/test_command_entry_eval.py` need only enter the revised selector if the Coordinator's amended design requires an actual change there. |

## 7. Fact Candidates

No fact candidates.

## 8. Strategic Insights (Execution)

No strategic insights.

## 9. Diagrams

`approved selector → rejected Candidate → targeted proof passes → configured gate finds out-of-scope contract → C1 restores live Resume → Coordinator/owner scope decision`

## 10. Direct Return

Return to LEAD `01a09a32-367e-7ea1-a405-9501d17ba270`. Do not dispatch the independent Reviewer: there
is no acceptable Candidate. The minimal concrete next route is for the Coordinator/owner to revise the
immutable selector to include `docs/scripts/command_entry_eval.py` as an additional ASSURANCE path,
change its exact manifest expectation to the ten surviving commands, reapprove the revised denominator,
and redispatch this same Executor. Add `docs/scripts/test_command_entry_eval.py` only if the revised design
requires its contents to change; the current failures do not independently prove that it must.

---

*RF — TFW_20260913-151442_RWNR / Phase B: Retire the public Resume surface | 2026-09-14*

## 11. Return Round 2 — Revision 2 completion

> **Date**: 2026-09-14
> **Author**: robert, Executor unit `01a09b39-f0c0-70c0-9b53-6981647e72fb`
> **Status**: 🟢 RF — Complete; ready for independent review
> **Parent HL**: [Phase B HL](HL__phase-b__resume_surface_retirement.md)
> **Governing TS**: [TS Phase B revision 2](TS__phase-b__resume_surface_retirement__rev2.md)
> **Fresh Candidate**: `6d6d094ac5325377772f26ddf314b965c1dfd135`

### 11.1 What Was Done

Revision 2 re-executed the complete retirement from the coherent C1-restored state. Candidate
`6d6d094ac5325377772f26ddf314b965c1dfd135` deletes the five exact Resume artifacts, converges all
25 remaining VALUE paths on the ten-command topology, and changes exactly three ASSURANCE paths. The
newly authorized `docs/scripts/command_entry_eval.py` edit removes only `resume` from
`REQUIRED_COMMANDS` and changes only the matching refusal from eleven to ten commands. The excluded
`docs/scripts/test_command_entry_eval.py` retains exact blob
`7f195b31c622ac8cdbd7dad0a0f2e9ae7fa7a539`.

The first rev2 targeted run correctly found one stale two-ASSURANCE expectation in the approved
repository-contract test module. That assurance-only defect was corrected to bind the frozen rev2
TS/blob, exact 30+3 selector, evaluator semantics, and excluded-test identity. Every corrected
pre-freeze and immutable-Candidate gate then passed.

#### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | Freeze `e5efd3e608975184995d254bc5eb84176b8b4451`; exact rev2 TS blob `8c06e15e3ad8211195f2d48314d055ad1f111979`; owner ruling recorded before work in `journal/20260914-081032__transition__3333.md` |
| Baseline / Candidate | `d366bb1d6d70cf457acba84d4b5aafeb5c5f5b14` / `6d6d094ac5325377772f26ddf314b965c1dfd135`; Candidate parent `a1857064c14c72ad12996d808f0e810a432dbcf6` |
| VALUE — DELETE | `.tfw/workflows/resume.md`, `.tfw/adapters/codex/skills/tfw-resume/SKILL.md`, `.agents/skills/tfw-resume/SKILL.md`, `.agents/workflows/tfw-resume.md`, `.claude/commands/tfw-resume.md` — remove the canonical and installed public Resume payloads |
| VALUE — MODIFY: topology/config | `.agent/rules/agents.md`, `.agents/rules/tfw.md`, `.tfw/adapters/antigravity/tfw-rules.md.template`, `.tfw/adapters/claude-code/CLAUDE.md.template`, `.tfw/adapters/codex/AGENTS.md.template`, `.tfw/adapters/codex/README.md`, `.tfw/adapters/cursor/tfw.mdc.template`, `.tfw/adapters/manifest.yaml`, `.tfw/conventions.md`, `.tfw/project_config.yaml`, `.tfw/templates/project_config.yaml`, `AGENTS.md`, `CLAUDE.md` — remove live registrations/configuration while preserving managed ownership boundaries |
| VALUE — MODIFY: install/update | `.tfw/workflows/init.md`, `.agents/workflows/tfw-init.md`, `.claude/commands/tfw-init.md`, `.tfw/workflows/update.md`, `.agents/workflows/tfw-update.md`, `.claude/commands/tfw-update.md` — converge canonical and exact-copy receiver instructions without creating release identity |
| VALUE — MODIFY: public adapter/docs | `.tfw/adapters/README.md`, `.tfw/adapters/claude-code/README.md`, `.tfw/adapters/antigravity/README.md`, `README.kk.md`, `README.md`, `README.ru.md` — state the current ten-command topology without a Resume replacement |
| ASSURANCE membership | `docs/scripts/command_entry_eval.py` — exact ten-command evaluator; `docs/scripts/test_repository_contracts.py` — surface/receiver/history/accounting/C1 and rev2 scope oracles; `docs/scripts/test_runtime_context.py` — retained Phase A routing/identity and no-substitute proof |
| Arithmetic | 25 additions + 326 deletions = 351 touched text LOC; 30 logical VALUE files; binary/non-text N/A; actions exactly 5 DELETE + 25 MODIFY |
| Membership deviations | None. Candidate contains exactly 30 VALUE + three ASSURANCE paths. Excluded test, foreign OTR task, concurrent TKL, shared master, release metadata, and unrelated paths are absent. |
| Trigger disposition | Actual 30/351 stays within immutable 30/650 and below configured 50/5,000; the connected surface remained one phase. Assurance cost is three paths and does not ratchet VALUE. Terminal verdict: `METRICS_PASS__ALL_REQUIRED_GATES_PASS`. |
| Authority and timing | Owner-approved immutable 30/650 and return threshold 60/1,300 preceded work. Revision 2 prospectively added only one ASSURANCE member; no late authority or VALUE growth occurred. |
| Reproduction | Exact NUL-safe `git diff --name-status --find-renames=50% -z <Baseline> <Candidate> -- <30 literal VALUE paths>` and matching `--numstat -z`; full membership and result in `evidence/phase-b-accounting.json` |

#### New Files

| File | Description |
|---|---|
| `journal/20260914-095800__transition__a07a.md` | Revision-2 `ONB → RF` return with exact Candidate, gates, and direct next recipient |

No implementation file was created; the approved result is deletion-led.

#### Modified Files

| File/group | Changes |
|---|---|
| 30 literal VALUE paths above | Five deleted and 25 modified to remove only the live Resume surface and fixed eleven-command topology |
| Three literal ASSURANCE paths above | Added exact rev2 evaluator, selector, regression, receiver, history, accounting, mutant, and C1 proof |
| `evidence/EV__phase-b__resume_surface_retirement.md` and five attachments | Preserved revision-1/C1 evidence and appended Candidate-bound revision-2 results |
| `RF__phase-b__resume_surface_retirement.md` | Preserved the blocked first round and appended this complete returned round |
| `status.md` | Transitioned phase lifecycle from `ONB` to `RF` after all required gates passed |

### 11.2 Key Decisions

1. Corrected the stale two-ASSURANCE scope oracle inside the already approved assurance module after its deliberate first-run failure; no VALUE path or TS bound changed.
2. Kept the evaluator production change to its two exact approved lines and proved the excluded evaluator test byte-identical.
3. Reused detailed receiver/history/accounting receipts only where all 30 claim-relevant VALUE inputs are byte-identical to the earlier challenged Candidate, and paired that reuse with fresh Candidate-bound targeted/full oracle passes.
4. Kept the rewritten shared master, TKL history, foreign OTR task, review, landing, knowledge/digest work, G2, release metadata, and external effects outside this isolated producer.

### 11.3 Acceptance Criteria

- [x] AC-1 — exact five-path retirement, 25 VALUE modifications, ten-command manifest, 206 classified Candidate matches, zero live/unclassified match, and no replacement.
- [x] AC-2 — all four canonical/install receivers, managed boundaries, empty Cursor case, refusal, and repeat idempotence pass.
- [x] AC-3 — synthetic version-addressed owned-only update covers all five classes, atomic refusal, and no real release guide/version.
- [x] AC-4 — 179 task entries, required digest, protected blobs/modes, three aggregate subsequences, and mutants pass.
- [x] AC-5 — Plan and accepted copies remain byte-fixed; every retained Phase A continuation/authority scenario passes.
- [x] AC-6 — exact 30/351 VALUE result, Plan 1,199, `C=1,523 < B=2,737`, and no unclassified instruction addition.
- [x] AC-7 — exact 30+3 Candidate, exact evaluator contract, excluded test unchanged, and all targeted/configured/focused/state gates pass.
- [x] AC-8 — preflight and all C1 failure models pass; Candidate remains unlanded and isolated from current shared history.
- [x] AC-9 — N/A for external release effects; G2 remains the hard stop and no prohibited effect occurred.

### 11.4 Verification

- Configured lint/collection (`python -m pytest tools/tests/ docs/scripts/ -q --collect-only`): **627 collected in 0.24s** at Candidate.
- Configured tests (`python -m pytest tools/tests/ docs/scripts/ -q`): **626 passed, 1 skipped in 823.51s** at Candidate.
- Targeted rev2 (`python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_repository_contracts.py docs/scripts/test_command_entry_eval.py -q`): **388 passed in 468.15s** at Candidate.
- Focused evaluator (`python -m pytest docs/scripts/test_command_entry_eval.py -q`): **31 passed in 65.17s** at Candidate.
- State schema (`python -m pytest tools/tests/test_tfw_state.py -q`): **32 passed in 0.42s** at Candidate.
- Pre-freeze corrected target/full: **388 passed**; **626 passed, 1 skipped**.
- `git diff --check`: **clean**. Exact Candidate diff: **33 paths**, 5 DELETE + 28 MODIFY overall; VALUE subset is 5 DELETE + 25 MODIFY.
- Independent LEAD read-only corroboration: targeted **388 passed**; full **626 passed, 1 skipped**; collection **627**; focused **31**; state **32**; diff check clean.

### 11.5 Evidence

See [Phase B EV](evidence/EV__phase-b__resume_surface_retirement.md) for evidence details.

Evidence verdict: **9/10 VERIFIED, 0 DEFERRED, 0 BLOCKED, 1 N/A. Overall: READY FOR INDEPENDENT REVIEW; Candidate remains unlanded.**

### 11.6 Observations (out-of-scope, not modified)

No observations.

### 11.7 Fact Candidates

No fact candidates.

### 11.8 Strategic Insights (Execution)

No strategic insights.

### 11.9 Diagrams

`C1-restored state → rev2 30+3 implementation → fresh Candidate 6d6d094 → targeted/full proof → RF → independent review → later LEAD landing checks → G2 hard stop`

### 11.10 Direct Return

Return this exact producer directly to LEAD `01a09a32-367e-7ea1-a405-9501d17ba270`. The next act is
independent `/tfw-review` by the reserved Reviewer unit; this Executor performs no review, landing,
shared-history integration, TKL work, knowledge work, G2 decision, release, or external effect.

---

*RF return round 2 — TFW_20260913-151442_RWNR / Phase B | 2026-09-14*

## 12. Return Round 3 — real AC-8 recovery models

> **Date**: 2026-09-14
> **Author**: robert, Executor unit `01a09b39-f0c0-70c0-9b53-6981647e72fb`
> **Status**: 🟢 RF — Complete; ready for the reserved independent Reviewer
> **Parent HL**: [Phase B HL](HL__phase-b__resume_surface_retirement.md)
> **Governing TS**: [TS Phase B revision 2](TS__phase-b__resume_surface_retirement__rev2.md)
> **Governing TS blob**: `8c06e15e3ad8211195f2d48314d055ad1f111979`
> **Independent REVIEW producer**: `efa7cdd2ad66856d2be5e5799a82ba67e4c1b7cc`
> **Fresh Candidate**: `a81e0c12ec982ee4f73639ebf15394ef53877294`
> **Candidate parent / C1 implementation baseline**: `5cfca7abfa51fe3f565295ca4fc8be81c74c474f`

### 12.1 What Was Done

This return implements only the accepted rung-1 correction in REVIEW §4.1. The earlier
declarative `implementation_matches_baseline=True` proof was removed. Its replacement materializes
actual temporary trees and derives complete path/SHA-256 maps for all 30 VALUE plus three ASSURANCE
paths. It executes four distinct C1 cases:

1. preflight failure before any connected-group write;
2. injected mid-application failure after one real deletion in the connected group;
3. independent Reviewer rejection of a Candidate tree;
4. landing/integrated mismatch after a Candidate tree exists.

Every case restores the whole 33-path group to exact C1 before-image
`d09d5d49496d13b64552fe99a03821826ae435b6`, produces the same canonical full-map digest
`1a2d5d271b7ae2cf5c246f0b1344b71a0cbb1143a00c8204c8d853fcb292c666`, and observes empty
release routes/effects. The oracle independently rejects an altered path, one retained deletion,
and an emitted release route/effect.

The complete revision-2 product was then recreated from the coherent C1 baseline commit and frozen
as new Candidate `a81e0c12ec982ee4f73639ebf15394ef53877294`. Rejected Candidate
`6d6d094ac5325377772f26ddf314b965c1dfd135` remains unaccepted and unlanded evidence; it is not
used as the acceptance Candidate for this round.

#### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| Baseline / Candidate | VALUE baseline `d366bb1d6d70cf457acba84d4b5aafeb5c5f5b14`; Candidate `a81e0c12ec982ee4f73639ebf15394ef53877294`; Candidate parent `5cfca7abfa51fe3f565295ca4fc8be81c74c474f` |
| VALUE actions | Exact 30 paths: 5 DELETE + 25 MODIFY |
| ASSURANCE actions | Exact three MODIFY paths: `docs/scripts/command_entry_eval.py`, `docs/scripts/test_repository_contracts.py`, `docs/scripts/test_runtime_context.py` |
| Arithmetic | 25 additions + 326 deletions = 351 touched text LOC; binary/non-text N/A |
| Retained instruction accounting | Plan 1,199 words; `C=1,523 < B=2,737`; no unclassified instruction change |
| Immutable authority | Actual `30/351` remains within owner-approved `30/650`; no denominator ratchet, extra VALUE path, architecture change, or owner-return threshold |
| Candidate boundary | Full status named only 33 approved paths; initially empty index; literal staged set 33, missing 0, extra 0; post-Candidate status empty |
| Excluded test | `docs/scripts/test_command_entry_eval.py` is absent from Candidate diff and retains exact C1 blob `7f195b31c622ac8cdbd7dad0a0f2e9ae7fa7a539` |
| Terminal accounting verdict | `METRICS_PASS__ALL_REQUIRED_GATES_PASS` |

#### Modified Files

| File/group | Return-round change |
|---|---|
| `docs/scripts/test_repository_contracts.py` | Replaced declarative C1 decision with real temporary-tree image, restore, observation, oracle, four scenarios, and three hostile mutants; corrected worktree-vs-Candidate scope anchoring |
| Exact 30 VALUE + other two ASSURANCE paths | Recreated the already approved coherent revision-2 result byte-for-byte; no extra product scope |
| `evidence/phase-b-receivers.json` | Preserved earlier objects and appended `return_round_3` with full required and per-scenario 33-path SHA-256 maps plus mutant observations |
| `evidence/phase-b-tests.txt` | Preserved earlier epochs and appended the full round-3 chronology, initial failed check, correction, Candidate boundary, and Candidate-bound gates |
| `evidence/EV__phase-b__resume_surface_retirement.md` | Preserved earlier verdict epochs and appended E19–E-accounting-R3 |
| `RF__phase-b__resume_surface_retirement.md` | Appended this cumulative returned round |

### 12.2 Key Decisions

1. Used the C1 restore as the byte authority for all 33 approved paths and made actual filesystem
   observations determine the verdict; no boolean is assigned as proof of restoration.
2. Required the mid-application scenario to perform at least one connected-group write before the
   injected failure, so a no-op model cannot satisfy the test.
3. Included path inventory and release-route/effect observations in the oracle so byte-preserving
   but scope- or route-hostile mutants cannot pass.
4. Corrected the pre-Candidate scope anchor after a truthful first targeted failure. The correction
   remained in the approved assurance module and all complete pre-freeze gates were rerun.
5. Kept shared master/TKL, knowledge/digest, G2/release, landing, and all external effects outside
   this Executor mandate.

### 12.3 Acceptance Criteria

- [x] AC-1 — exact five-path retirement, 25 VALUE modifications, ten-command manifest, no live substitute.
- [x] AC-2 — four receivers, ownership boundaries, atomic refusal, and idempotence pass in real temporary trees.
- [x] AC-3 — all five update ownership classes remain covered through evidence-only pinned fixtures; no release identity is created.
- [x] AC-4 — task/aggregate history oracles and mutants pass; protected history is untouched.
- [x] AC-5 — Plan/accepted-copy bytes and all Phase A authority/continuation behaviors remain intact.
- [x] AC-6 — exact 30/351 VALUE accounting, Plan 1,199, `C=1,523 < B=2,737`, no unclassified change.
- [x] AC-7 — exact 30+3 Candidate, excluded test unchanged, and all targeted/configured/focused/state gates pass.
- [x] AC-8 — four real recovery models restore 33/33 path-byte identities with no release route/effect; all three hostile mutants fail.
- [x] AC-9 — N/A for external release effects; G2 remains closed and no prohibited effect occurred.

### 12.4 Verification

- Isolated AC-8 model: **5 passed, 133 deselected in 9.20s**.
- Truthful first pre-freeze targeted attempt: **1 failed, 391 passed in 417.37s**; scope-anchor cause corrected inside ASSURANCE.
- Corrected isolated selector/C1 checks: **6 passed, 132 deselected in 22.77s**.
- Corrected pre-freeze targeted: **392 passed in 395.39s**.
- Corrected pre-freeze configured collection: **631 collected in 0.23s**.
- Corrected pre-freeze configured full: **630 passed, 1 skipped in 639.02s**.
- Corrected pre-freeze focused/state: **31 passed in 44.49s**; **32 passed in 0.23s**.
- Candidate-bound targeted: **392 passed in 426.20s**.
- Candidate-bound configured collection: **631 collected in 0.21s**.
- Candidate-bound configured full: **630 passed, 1 skipped in 701.40s**.
- Candidate-bound focused/state: **31 passed in 45.13s**; **32 passed in 0.28s**.
- Candidate `git diff --check`: **clean**; exact implementation scope: **33 paths**; post-Candidate tree: **clean**.

### 12.5 Evidence

See [Phase B EV](evidence/EV__phase-b__resume_surface_retirement.md),
[`phase-b-receivers.json`](evidence/phase-b-receivers.json), and
[`phase-b-tests.txt`](evidence/phase-b-tests.txt).

Evidence verdict: **9/10 VERIFIED, 0 DEFERRED, 0 BLOCKED, 1 N/A. Overall: READY FOR
INDEPENDENT REVIEW; Candidate remains unaccepted and unlanded.**

### 12.6 Observations

The first full targeted check exposed one return-lineage-specific ambiguity in the existing scope
helper. The corrected helper now measures `HEAD → worktree` while an implementation delta exists and
`Candidate^ → Candidate` after freeze. Complete gates were rerun after correction; no failure is
hidden or treated as acceptance evidence.

### 12.7 Fact Candidates

No fact candidates.

### 12.8 Strategic Insights

No strategic insights.

### 12.9 Direct Return

Return this exact producer directly to LEAD `01a09a32-367e-7ea1-a405-9501d17ba270`. The same reserved
independent Reviewer must execute `/tfw-review` against Candidate
`a81e0c12ec982ee4f73639ebf15394ef53877294` and this appended evidence. This Executor performs no
review, landing, shared-history integration, TKL, knowledge/digest, G2/release, or external effect.

---

*RF return round 3 — TFW_20260913-151442_RWNR / Phase B | 2026-09-14*

## 13. Return Round 4 — exact-path Candidate evidence

> **Date**: 2026-09-14
> **Author**: robert, Executor unit `01a09b39-f0c0-70c0-9b53-6981647e72fb`
> **Status**: 🟢 RF — Complete; ready for the same independent Reviewer
> **Parent HL**: [Phase B HL](HL__phase-b__resume_surface_retirement.md)
> **Governing TS**: [TS Phase B revision 2](TS__phase-b__resume_surface_retirement__rev2.md)
> **Governing TS blob**: `8c06e15e3ad8211195f2d48314d055ad1f111979`
> **Binding REVIEW producer**: `9eaf775cc0ff3a28e3c989e4018d34b3b707eb57`
> **Fresh Candidate**: `51ea3015290393da001810629f305f5969f4c8b8`
> **Candidate parent / C1 implementation baseline**: `41a70febc6d33d369af125d7ad2ecf98a2de0761`

### 13.1 What Was Done

This return implements only the accepted rung-1 process/evidence correction in live REVIEW §8.7.
From a coherent C1 implementation baseline, the exact corrected 30 VALUE + three ASSURANCE bytes
were replayed without semantic change. Before Candidate creation, the complete status, empty cached
inventory, literal ordered selector/staging command, staged names/actions, and zero missing/extra
audit were captured outside the repository. Candidate `51ea3015290393da001810629f305f5969f4c8b8`
was created with the actual command form
`git commit -m <message> --only -- <all 33 literal approved pathspecs>`.

Immediately after freeze, post-status, post-index, exact Candidate names/actions, clean diff, exact
commit result, and 33-path byte identity were appended to that outside receipt. Only then was it
copied into phase-local evidence. The repository copy is byte-identical to the outside receipt and
has SHA-256 `4c3350df1a496af6de502c10f2dd9ca773a4872167ca53d573008831bc476530`.
All 33 Candidate implementation bytes match corrected Candidate
`a81e0c12ec982ee4f73639ebf15394ef53877294`; that earlier Candidate remains unaccepted and
unlanded evidence only.

#### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval / blob | `e5efd3e608975184995d254bc5eb84176b8b4451` / `8c06e15e3ad8211195f2d48314d055ad1f111979` |
| Baseline / Candidate | VALUE baseline `d366bb1d6d70cf457acba84d4b5aafeb5c5f5b14`; C1 parent `41a70febc6d33d369af125d7ad2ecf98a2de0761`; Candidate `51ea3015290393da001810629f305f5969f4c8b8` |
| VALUE actions | Exact 30 paths: 5 DELETE + 25 MODIFY |
| ASSURANCE actions | Exact three MODIFY paths: `docs/scripts/command_entry_eval.py`, `docs/scripts/test_repository_contracts.py`, `docs/scripts/test_runtime_context.py` |
| Arithmetic | 25 additions + 326 deletions = 351 touched text LOC; binary/non-text N/A |
| Retained instruction accounting | Plan 1,199 words; `C=1,523 < B=2,737`; no unclassified instruction change |
| Immutable authority | Actual `30/351` remains within owner-approved `30/650`; no denominator ratchet, added VALUE, architecture change, or owner-return threshold |
| Candidate boundary | Full status and empty index captured; literal selector 33, staged 33, missing 0, extra 0; actual `commit --only -- <33 paths>`; post-Candidate status/index empty; receipt copied only after freeze |
| Byte identity | All 33 approved paths match `a81e0c12…`; mismatch count 0 |
| Excluded test | `docs/scripts/test_command_entry_eval.py` is absent from Candidate diff and has blob `7f195b31c622ac8cdbd7dad0a0f2e9ae7fa7a539` at Candidate and parent |
| Reproduction | Frozen TS NUL-safe name-status/numstat method plus literal-path boundary receipt |
| Terminal accounting verdict | `METRICS_PASS__ALL_REQUIRED_GATES_PASS__EXACT_PATH_PROCESS_PASS` |

#### New Evidence Files

| File | Description |
|---|---|
| `evidence/phase-b-candidate-boundary-round4.txt` | Complete pre/post-Candidate exact-path boundary receipt copied byte-identically after freeze |
| `evidence/phase-b-targeted-round4.txt` | Raw observed Candidate-bound targeted command/result |
| `evidence/phase-b-full-round4.txt` | Raw observed Candidate-bound configured-full command/result |

#### Modified Trace Files

| File | Changes |
|---|---|
| `evidence/phase-b-tests.txt` | Appended complete round-4 identities, boundary result, completed test outcomes, accounting, and prohibited-effect confirmation |
| `evidence/phase-b-accounting.json` | Appended `return_round_4_validation` without rewriting earlier epochs |
| `evidence/EV__phase-b__resume_surface_retirement.md` | Appended E28–E-accounting-R4 and retained every earlier verdict epoch |
| `RF__phase-b__resume_surface_retirement.md` | Appended this cumulative return |

### 13.2 Key Decisions

1. Rebuilt the same implementation from C1 and compared every approved path byte to the corrected
   return, making the fresh Candidate functionally and byte-identical rather than editing semantics.
2. Kept the complete raw boundary outside the repository until Candidate freeze so no evidence path
   could enter the exact 33-path Candidate.
3. Used the actual required `git commit --only --` form with all 33 literal pathspecs and preserved
   its exact command/result plus pre/post observations in durable phase-local evidence.
4. Preserved completed Candidate-bound test outputs as separate raw receipts; no test was rerun
   while preparing RF round 4.
5. Kept shared master/OTR/TKL, knowledge/digest, G2/release, landing, and all external effects outside
   this Executor mandate.

### 13.3 Acceptance Criteria

- [x] AC-1 — exact five-path retirement, 25 VALUE modifications, ten-command manifest, no live substitute.
- [x] AC-2 — four receivers, ownership boundaries, atomic refusal, and idempotence pass.
- [x] AC-3 — all five update ownership classes remain covered; no release identity is created.
- [x] AC-4 — task/aggregate history oracles and mutants pass; protected history is untouched.
- [x] AC-5 — Plan/accepted-copy bytes and Phase A authority/continuation behavior remain intact.
- [x] AC-6 — exact 30/351 VALUE accounting, Plan 1,199, `C=1,523 < B=2,737`, no unclassified change.
- [x] AC-7 — exact 30+3 Candidate, durable raw boundary, actual literal-path `commit --only`, excluded test unchanged, and all required gates pass.
- [x] AC-8 — corrected real recovery models remain byte-fixed and pass; no evidence path entered Candidate.
- [x] AC-9 — N/A for release effects; G2 remains closed and no prohibited effect occurred.

### 13.4 Verification

- Candidate-bound targeted: **392 passed in 428.13s (0:07:08)**; raw receipt SHA-256
  `bfd9410246c865506f31017e318214b34a961142d4e281f3001f8bf769a7cd22`.
- Candidate-bound configured collection: **631 collected in 0.23s**.
- Candidate-bound configured full: **630 passed, 1 skipped in 743.11s (0:12:23)**; raw receipt
  SHA-256 `ef612a1d155d9d37ce88809567faece9a1c17561a4512d7516751b5f9efff60a`.
- Candidate-bound focused/state: **31 passed in 53.41s**; **32 passed in 0.32s**.
- Candidate `git diff --check`: **clean**; exact implementation scope: **33 paths**.
- Exact boundary: selector **33**, staged **33**, missing **0**, extra **0**; pre/post cached inventories empty.
- Reference byte identity: **33 paths checked, 0 mismatches**.
- Boundary receipt SHA-256: `4c3350df1a496af6de502c10f2dd9ca773a4872167ca53d573008831bc476530`.

### 13.5 Evidence

See [Phase B EV](evidence/EV__phase-b__resume_surface_retirement.md),
[`phase-b-candidate-boundary-round4.txt`](evidence/phase-b-candidate-boundary-round4.txt),
[`phase-b-targeted-round4.txt`](evidence/phase-b-targeted-round4.txt),
[`phase-b-full-round4.txt`](evidence/phase-b-full-round4.txt),
[`phase-b-accounting.json`](evidence/phase-b-accounting.json), and
[`phase-b-tests.txt`](evidence/phase-b-tests.txt).

Evidence verdict: **9/10 VERIFIED, 0 DEFERRED, 0 BLOCKED, 1 N/A. Overall: READY FOR
INDEPENDENT REVIEW; Candidate remains unaccepted and unlanded.**

### 13.6 Observations

No observations.

### 13.7 Fact Candidates

No fact candidates.

### 13.8 Strategic Insights

No strategic insights.

### 13.9 Diagrams

`C1 implementation baseline → byte-identical 33-path replay → outside raw boundary → exact-path Candidate 51ea301 → Candidate-bound gates → TRACE/RF → same independent Reviewer`

### 13.10 Direct Return

Return the final TRACE producer directly to LEAD `01a09a32-367e-7ea1-a405-9501d17ba270`.
The same independent Reviewer unit `01a09b82-d0ed-78b1-9b72-42291fd8359e` must execute affected
`/tfw-review` against Candidate `51ea3015290393da001810629f305f5969f4c8b8` and this cumulative
evidence. This Executor performs no review, landing, shared-history integration, TKL,
knowledge/digest, G2/release, or external effect.

---

*RF return round 4 — TFW_20260913-151442_RWNR / Phase B | 2026-09-14*

## 14. Landing Composite Return — fresh-master TKL-safe Candidate

> **Date**: 2026-09-14
> **Author**: robert, Executor unit `01a09b39-f0c0-70c0-9b53-6981647e72fb`
> **Status**: RF complete; ready for affected review by the same independent Reviewer
> **Parent HL**: [Phase B HL](HL__phase-b__resume_surface_retirement.md)
> **Governing TS**: [TS Phase B revision 2](TS__phase-b__resume_surface_retirement__rev2.md)
> **Governing TS blob**: `8c06e15e3ad8211195f2d48314d055ad1f111979`
> **Accepted Candidate / REVIEW producer**: `51ea3015290393da001810629f305f5969f4c8b8` / `14da05a4f1b4a341f30b75fce4f572db2c367b2d`
> **Landing contract producer**: `f979eac49bc3acd0d0220591047ec8abccf49072`
> **Fresh master / landing Candidate**: `3fd16fd1549a3f92006e8f37102df4a511b8aa55` / `3c354ba29d525ccb4e7683c5c477290682b90a5a`

### 14.1 What Was Done

The Executor created a new clean landing worktree from the re-read TKL release-line master and
performed a product-only semantic composition. No merge, rebase, cherry-pick, old-RWNR ancestry
transport, wholesale Candidate checkout, directory staging, or shared-master mutation was used.

For nineteen clean-preimage paths, the accepted Candidate after-image was applied exactly. Fourteen
paths had already diverged through TKL; eleven were composed to preserve both TKL 3.4 and accepted
Resume-retirement meaning, while the three retired Resume copies remained deletions. Before freeze,
the complete status, empty index, ordered 33-path selector, per-path provenance, exact staging command,
and missing/extra-zero audit were preserved outside the repository. The product commit used
`git commit --only --` with all 33 literal paths. Candidate
`3c354ba29d525ccb4e7683c5c477290682b90a5a` has parent
`3fd16fd1549a3f92006e8f37102df4a511b8aa55`, tree
`7b61356eb8990ccec78cb9f4275dbae305948eb1`, and exactly 28 MODIFY plus five DELETE paths.
No product byte changed after Candidate freeze.

After freeze, the exact 36 Phase-B paths from accepted REVIEW producer
`14da05a4f1b4a341f30b75fce4f572db2c367b2d` plus contract event `f764` from
`f979eac49bc3acd0d0220591047ec8abccf49072` were transferred as 37 literal paths. Every transferred
worktree blob matches its source blob, with zero missing, extra, or mismatched paths. Root-task and
Phase-A trace were not transferred.

#### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| Approved Phase-B authority | TS blob `8c06e15e3ad8211195f2d48314d055ad1f111979`; accepted Candidate `51ea3015290393da001810629f305f5969f4c8b8`; accepted independent REVIEW producer `14da05a4f1b4a341f30b75fce4f572db2c367b2d` |
| Fresh master / landing Candidate | `3fd16fd1549a3f92006e8f37102df4a511b8aa55` / `3c354ba29d525ccb4e7683c5c477290682b90a5a` |
| Product membership | Exact approved 30 VALUE + three ASSURANCE paths; overall actions 28 MODIFY + five DELETE |
| Composition classes | 19 clean-preimage paths with exact accepted after-images; 14 TKL-diverged semantic-composite paths, including three deletions |
| Accepted VALUE arithmetic | Unchanged: 30 logical text paths, 25 additions + 326 deletions = 351 touched LOC; Plan 1,199; `C=1,523 < B=2,737` |
| Landing transport arithmetic | Candidate versus fresh master: 1,123 additions + 460 deletions over 33 product paths. This is integration provenance and does not redefine or ratchet accepted VALUE accounting. |
| Candidate boundary | Pre-index empty; literal selector/staging 33; missing 0; extra 0; actual `commit --only -- <33 literal paths>`; post-index/status empty |
| Large blobs | Master and Candidate each contain exactly the same five grandfathered blobs at or above 10 MiB; new qualifying blobs 0 |
| Terminal disposition | Product Candidate and RF complete; affected independent review required; shared-master landing, DONE, G2, and release remain forbidden |

#### New Landing Evidence Files

| File | Description |
|---|---|
| `evidence/phase-b-landing-candidate-boundary.txt` | External pre/post-Candidate boundary copied byte-identically after freeze; all 33 provenance rows and large-blob audit |
| `evidence/phase-b-landing-provenance-check.txt` | Focused per-path composition oracle |
| `evidence/phase-b-landing-trace-transfer.txt` | Exact 36+1 transfer selector, source/observed blobs, and initial staging audit |
| `evidence/phase-b-landing-targeted-attempt1.txt` | Truthful 419-pass/one-fail landing-worktree attempt caused by adjacent unstaged TRACE state |
| `evidence/phase-b-landing-targeted.txt` | Clean detached Candidate targeted raw output |
| `evidence/phase-b-landing-collect.txt` | Clean detached Candidate collection raw output |
| `evidence/phase-b-landing-full.txt` | Clean detached Candidate configured-full raw output |
| `evidence/phase-b-landing-focused-command-entry.txt` | Clean detached Candidate focused command-entry raw output |
| `evidence/phase-b-landing-state.txt` | Clean detached Candidate state-suite raw output |

### 14.2 Key Decisions

1. Treated current master as the only landing baseline and stopped short of changing it; the landing
   Candidate is review input, not a completed landing.
2. Preserved exact accepted after-images only where fresh-master preimages matched the accepted
   parent; TKL-diverged paths were composed semantically and verified individually.
3. Kept the first TRACE-bearing worktree test failure as non-acceptance evidence. LEAD directed final
   Candidate-bound verification in a separate clean detached checkout, and no product repair followed
   Candidate freeze.
4. Preserved the accepted Phase-B denominator and arithmetic instead of misclassifying TKL integration
   changes as new Phase-B VALUE.
5. Kept the owner N/A for docs/knowledge/consolidation and performed no release, G2, tag, push, publish,
   deploy, notification, OTR mutation, or external effect.

### 14.3 Acceptance Criteria

- [x] AC-1 — exact five-path retirement, 25 VALUE modifications, ten-command topology, no live substitute.
- [x] AC-2 — all four receivers, managed boundaries, atomic refusal, and idempotence pass.
- [x] AC-3 — evidence-only pinned update and all ownership classes pass without a release identity.
- [x] AC-4 — all 33 fresh-master/accepted/composite paths are accounted for; TKL 3.4 and historical truth remain intact.
- [x] AC-5 — Plan/copy parity, Phase-A continuation, and TKL handover semantics pass.
- [x] AC-6 — accepted 30/351 VALUE accounting and `C < B` remain immutable; integration provenance is separate.
- [x] AC-7 — exact 33-path `commit --only`, durable raw receipts, and all Candidate-bound gates pass.
- [x] AC-8 — clean fresh-master parent, no old ancestry transport, exact 36+1 TRACE transfer, and no post-freeze product edit.
- [x] AC-9 — N/A for external effects; shared-master landing, DONE, G2, and release remain closed.

### 14.4 Verification

- Targeted:
  `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_repository_contracts.py docs/scripts/test_command_entry_eval.py -q`
  — **420 passed in 587.26s**.
- Configured collection:
  `python -m pytest tools/tests/ docs/scripts/ -q --collect-only`
  — **719 collected in 0.60s**.
- Configured full:
  `python -m pytest tools/tests/ docs/scripts/ -q`
  — **718 passed, 1 skipped in 953.64s**.
- Focused command entry:
  `python -m pytest docs/scripts/test_command_entry_eval.py -q`
  — **31 passed in 47.91s**.
- State:
  `python -m pytest tools/tests/test_tfw_state.py -q`
  — **32 passed in 0.43s**.
- Focused landing provenance:
  `python -m pytest docs/scripts/test_repository_contracts.py -q -k rwnr_phase_b_landing_composes_clean_and_tkl_diverged_paths_exactly`
  — **1 passed, 145 deselected in 6.76s**.
- Product diff check: clean. Product selector: 33, missing 0, extra 0. TRACE transfer:
  37, missing 0, extra 0, blob mismatch 0.
- Boundary receipt internal/external identity after whitespace-only receipt normalization:
  SHA-256 `dcaab1c0bf3657e8e2483f6fe053ed7efa34c7377d51026e8011927c64a101c3`, 19,843 bytes.

### 14.5 Evidence

See [Phase B EV](evidence/EV__phase-b__resume_surface_retirement.md) and the nine landing evidence
files listed in §14.1.

Evidence verdict: **9/10 VERIFIED, 0 DEFERRED, 0 BLOCKED, 1 N/A. Overall: READY FOR AFFECTED
INDEPENDENT REVIEW; Candidate remains unlanded and Phase B remains KNW.**

### 14.6 Observations

No out-of-scope product issue remains. The first worktree attempt documents a verification-isolation
condition, not a Candidate defect; the final clean detached verification resolves it.

### 14.7 Fact Candidates

No fact candidates.

### 14.8 Strategic Insights

No strategic insights.

### 14.9 Material Handover at This Return

Use this RF, its EV, the nine landing receipts, accepted REVIEW producer
`14da05a4f1b4a341f30b75fce4f572db2c367b2d`, and landing contract producer
`f979eac49bc3acd0d0220591047ec8abccf49072` as the bounded current-use source. The producing unit is
Executor `01a09b39-f0c0-70c0-9b53-6981647e72fb`; the source epoch is fresh master
`3fd16fd1549a3f92006e8f37102df4a511b8aa55` through immutable landing Candidate
`3c354ba29d525ccb4e7683c5c477290682b90a5a`. Material technical knowledge is the exact 19-clean /
14-composite provenance and green Candidate-bound verification. There is no new human-sourced fact
or strategic insight. The continuation is affected review by the same Reviewer; uncertainty remains
only in that independent judgment and later exact landing, which this Executor cannot perform.

### 14.10 Direct Return

Return the final TRACE producer directly to LEAD `01a09a32-367e-7ea1-a405-9501d17ba270` and
Coordinator `01a09a92-18fb-7da1-a639-6a86844bf147`. The same independent Reviewer unit
`01a09b82-d0ed-78b1-9b72-42291fd8359e` must execute affected `/tfw-review` against landing
Candidate `3c354ba29d525ccb4e7683c5c477290682b90a5a`. This Executor performs no REVIEW, shared-master
landing, DONE transition, docs/knowledge/consolidation work, release, G2, or external effect.

---

*RF landing composite — TFW_20260913-151442_RWNR / Phase B | 2026-09-14*

## 15. Landing Provenance Return — Closed Rung-1 Evidence Correction

> **Date**: 2026-09-14
> **Author**: robert, Executor unit `01a09b39-f0c0-70c0-9b53-6981647e72fb`
> **Status**: RF complete; ready for affected review by the same independent Reviewer
> **Coordinator producer**: `a3f54f4053d5b06502856914712c25c99d0e3fb4`
> **Proposal origin**: Reviewer `{robert, 01a09b82-d0ed-78b1-9b72-42291fd8359e}`
> **Governing TS blob**: `8c06e15e3ad8211195f2d48314d055ad1f111979`
> **Closing contract producer**: `f979eac49bc3acd0d0220591047ec8abccf49072`
> **Immutable landing Candidate**: `3c354ba29d525ccb4e7683c5c477290682b90a5a`

### 15.1 What Was Done

This return implements only the Coordinator-accepted evidence-only bound in live REVIEW §10.6.
The existing landing branch was fast-forwarded without a merge commit from TRACE producer
`69decdbbc305e6fb3a0d91ccdf8e6af7ea6bc1fd` to Coordinator producer
`a3f54f4053d5b06502856914712c25c99d0e3fb4`. No product or ASSURANCE path changed.

A new provenance receipt resolves all 33 literal product paths through four immutable Git epochs:

1. fresh master `3fd16fd1549a3f92006e8f37102df4a511b8aa55`;
2. actual accepted parent `41a70febc6d33d369af125d7ad2ecf98a2de0761`;
3. accepted Candidate `51ea3015290393da001810629f305f5969f4c8b8`;
4. immutable landing Candidate `3c354ba29d525ccb4e7683c5c477290682b90a5a`.

Every required commit and present path is resolved with checked Git plumbing; a missing or mistyped
required object aborts the operation. Only the five literal expected Candidate deletions may be absent.
The table contains all 33 accepted-parent Git blob OIDs, exact accepted/landing actions
`28 MODIFY + 5 DELETE`, selector missing/extra zero, and the independently reproduced
`19 CLEAN_PREIMAGE + 14 COMPOSITE` split, including three composite deletions.

The defective historical receipt
`evidence/phase-b-landing-candidate-boundary.txt` remains byte-identical to its Coordinator-producer
blob `e9be20aeba899c3bba569086dfe502b0ddec2506`. It is not overwritten or silently repaired. RF §14
and EV E40 remain openable as the affected historical claims; this §15 and the new EV rows replace
only their evidentiary basis for accepted-parent provenance.

#### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| Authority | Coordinator producer `a3f54f4053d5b06502856914712c25c99d0e3fb4`; live REVIEW §10.6; unchanged TS blob `8c06e15e3ad8211195f2d48314d055ad1f111979`; closing producer `f979eac49bc3acd0d0220591047ec8abccf49072` |
| Baseline / Candidate | Fresh master `3fd16fd1549a3f92006e8f37102df4a511b8aa55`; immutable landing Candidate `3c354ba29d525ccb4e7683c5c477290682b90a5a`; actual accepted parent `41a70febc6d33d369af125d7ad2ecf98a2de0761`; accepted Candidate `51ea3015290393da001810629f305f5969f4c8b8` |
| VALUE membership | No VALUE path changed in this return. The accepted 30-path VALUE selector, classes, reasons, and product bytes remain unchanged. |
| ASSURANCE membership | No ASSURANCE path changed in this return. |
| TRACE membership | Two new evidence files, cumulative EV and RF supplements, and one new handoff event only |
| Arithmetic | VALUE `0 + 0 = 0` touched LOC across 0 logical VALUE files; binary/non-text N/A |
| Membership deviations | None. Historical defective receipt, status, product, ASSURANCE, HL, TS, REVIEW, master, TKL, OTR, and knowledge/digest state are unchanged by this Executor. |
| Trigger disposition | Evidence-only rung 1; no decomposition trigger, denominator growth, or owner escalation applies |
| Authority and timing | Closed bound existed at Coordinator producer before writes; immutable `30 VALUE / 650 LOC` denominator is not ratcheted |
| Reproduction | New receipt records literal selector and four Git blobs per row; focused validator independently recomputes all rows and invalid-parent rejection |

#### New Files

| File | Description |
|---|---|
| `evidence/phase-b-landing-provenance-correction.json` | Correct fail-closed 33-row four-epoch Git blob table; SHA-256 `50029a652b5985f88984a18cd5ca37d28f5c908aa54e1582d76aee6a68be2977`, Git blob `da565f31bb41922011a407dd2fb327411e5b568d` |
| `evidence/phase-b-landing-provenance-validation.txt` | Exact independent validator source and raw output; SHA-256 `314f645c2448580ed4d67df9f57b5f0fae542854a9e61c0d9f22a780329ef738`, Git blob `5ef5d61dc8a3edc49d53a0f61038cfa1fb4224b9` |

#### Modified Files

| File | Changes |
|---|---|
| `evidence/EV__phase-b__resume_surface_retirement.md` | Appended E46–E-accounting-provenance; preserved all earlier epochs and disclosed the exact historical defect |
| `RF__phase-b__resume_surface_retirement.md` | Appended this §15 cumulative return only |

### 15.2 Key Decisions

1. Used the actual accepted parent commit as a required exact full SHA and made every required object
   or present-path lookup fail closed instead of converting failure to an absence marker.
2. Kept expected deletion handling explicit and path-bounded, so a missing surviving path is an error
   while the five accepted deletions remain representable.
3. Bound a second implementation-independent validator to the durable table hash and Git blob, then
   proved the known invalid-parent mutant is rejected with Git exit 128.
4. Preserved the defective receipt as immutable history and identified exactly which RF/EV claim it
   cannot support; no inference or alternate SHA-256 map is substituted for the corrected Git table.
5. Reused existing green regression receipts because the validator observed zero tested-dependency
   changes. No test restart was performed.

### 15.3 Acceptance Criteria

- [x] AC-7 / DoD 17 — new receipt contains correct accepted-parent Git blobs and four-epoch identities for 33/33 literal paths.
- [x] AC-7 / closing provenance — accepted actions are `28 M + 5 D`; missing/extra is zero.
- [x] AC-7 / landing composition — classification is `19 CLEAN_PREIMAGE + 14 COMPOSITE`, including three composite deletions.
- [x] AC-7 / evidence integrity — independent validation matches Git for 33/33 rows and rejects the invalid parent.
- [x] AC-8 — Candidate and all product/ASSURANCE bytes remain immutable and unlanded; historical defective receipt is preserved.
- [x] AC-9 — N/A for external effects; no prohibited effect occurred.

### 15.4 Verification

- Focused receipt-to-Git validator: **PASS — 33/33 rows matched; 33 accepted-parent blobs present;
  actions 28 M + 5 D; classifications 19/14; three composite deletions; selector missing/extra 0**.
- Invalid-parent mutant `41a70b94019b86b99d87bb48f3da653a51112050`:
  **REJECTED**, `git rev-parse --verify <ref>^{commit}` exit **128**.
- Historical receipt preservation: HEAD/worktree Git blob
  `e9be20aeba899c3bba569086dfe502b0ddec2506` / same — **PASS**.
- Tested-dependency changes: **0**. Existing recorded regressions are reused without rerun:
  targeted 420; collection 719; full 718 + one skip; focused command-entry 31; state 32.
- Current mutation scope before RF: only the two new Phase-B evidence files and cumulative EV/RF
  append; product/ASSURANCE/status/HL/TS/REVIEW changes **0**.
- `git diff --check`: **clean** before RF append.

### 15.5 Evidence

See [Phase B EV](evidence/EV__phase-b__resume_surface_retirement.md), especially E46–E49 and
E-accounting-provenance.

Evidence verdict: **4/5 VERIFIED, 0 DEFERRED, 0 BLOCKED, 1 N/A. Overall: READY FOR AFFECTED
INDEPENDENT REVIEW; Candidate remains unaccepted and unlanded.**

### 15.6 Observations

No observations.

### 15.7 Fact Candidates

No fact candidates.

### 15.8 Strategic Insights

No strategic insights.

### 15.9 Diagrams

`defective historical receipt (preserved) → correct fail-closed 33-row table → independent 33/33 validation + invalid-parent rejection → RF → same Reviewer`

### 15.10 Material Handover at This Return

Use live REVIEW §10.6, Coordinator producer
`a3f54f4053d5b06502856914712c25c99d0e3fb4`, the new correction JSON, this RF §15, and the new EV
rows as the bounded source. The producing unit is Executor
`01a09b39-f0c0-70c0-9b53-6981647e72fb`; the proposal originated from independent Reviewer
`{robert, 01a09b82-d0ed-78b1-9b72-42291fd8359e}`. Material technical knowledge is the corrected
33-row accepted-parent Git blob chain and fail-closed validator result. There is no new human-sourced
fact or strategic insight. The only remaining uncertainty is the same Reviewer's independent
judgment of this return; Candidate landing remains a separate later LEAD-controlled effect.

### 15.11 Direct Return

Return the exact TRACE producer directly to LEAD/root
`01a09a32-367e-7ea1-a405-9501d17ba270` through Coordinator
`01a09a92-18fb-7da1-a639-6a86844bf147`. The same independent Reviewer unit
`01a09b82-d0ed-78b1-9b72-42291fd8359e` must run affected `/tfw-review` against immutable landing
Candidate `3c354ba29d525ccb4e7683c5c477290682b90a5a` and this correction. Phase remains `KNW`.
This Executor performs no REVIEW, status transition, master landing, DONE, TKL/OTR work,
knowledge/digest work, release, G2, or external effect.

---

*RF landing provenance rung-1 return — TFW_20260913-151442_RWNR / Phase B | 2026-09-14*
