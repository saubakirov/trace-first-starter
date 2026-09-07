# RF — TFW_20260902-111644_CRATM / Phase E: Sweep correction and release preparation

> **Date**: 2026-09-07
> **Author**: robert (Codex Executor)
> **Status**: 🟢 RF — Complete; independent review challenges recorded
> **Parent HL**: [master HL](../HL-TFW_20260902-111644_CRATM.md)
> **Phase HL**: [Phase E HL](HL__phase-e__sweep_correction_and_release.md)
> **TS**: [Phase E completion TS](TS__phase-e__completion_and_release_preparation.md)

---

## 1. What Was Done

Candidate II `6c93e813e7a3ccae05b74a85170cca36c2de8856` corrects the three live
acting-principal promises and their six accepted copies, adds five single-owner glossary routers,
repairs the Phase B B9 target, and carries an exact mechanically replayed 3.0.0 release package while
leaving its six canonical release destinations unchanged. The two approved assurance modules now
cover exact current semantics, package replay and corruption, no-binding behavior, K1/current versus
immutable history, glossary/debt boundaries, and NUL-safe accounting. Evidence and the four later Main
read-only challenges are recorded without post-Candidate VALUE/ASSURANCE change.

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | Corrected dispatch `1c4b5e01082a1315659d7e4f291ff911e1a25b42`; approved planning commit `759475fe232fee39f7e25a2aa0f25df2214cde7f`; TS content blob `96585e0f8bd3d49b8d81f17bed96821b76cef1d3` |
| Baseline / Candidate | `b0bfcd22125d8a34366d7eb885a2fb54234bdc7d` / `6c93e813e7a3ccae05b74a85170cca36c2de8856` |
| VALUE membership | 3 canonical workflows MODIFY for the exact writer rule; 6 `.agent`/`.claude` workflow copies MODIFY for accepted byte parity; `.tfw/glossary.md` MODIFY for five routers; Phase B HL MODIFY for B9; release package CREATE as the accepted six-file release input |
| Arithmetic | 417 additions + 37 deletions = 454 touched text LOC; 12 logical files; 11 MODIFY + 1 CREATE; binary/non-text N/A count 0 |
| Membership deviations | None. Every literal selector member changed, and no accepted output was classified as TRACE. Exactly the two approved ASSURANCE paths changed outside the VALUE selector. |
| Trigger disposition | `KEEP_PHASE_E`: exact sweep/package subject remained inside the approved phase; cost is one formal independent review; full configured, targeted, strict build, replay and negative assurance ran; no split or new carrier/class/unit was needed. |
| Authority and timing | Immutable 12/900 plan; owner boundary 24/1,800. Actual 12/454 is below both; exact pre-work approval/dispatch preceded ONB and implementation. No retrospective authority or denominator ratchet. |
| Reproduction | Exact TS path array with `git diff --name-status --find-renames=50% -z` and `git diff --numstat --find-renames=50% -z`; NUL records, numeric adds/deletes, no line subtraction. See `evidence/phase-e-completion-accounting.txt`. |

The deduplicated final union remains exactly 46 paths. Current whole-union floor is 2,908 LOC; adding
the entire 200-LOC K2 ceiling and exact 180-LOC package release delta gives a conservative 3,288-LOC
forecast, below 4,000. Only the later landed release commit may supply the final actual measurement.

### New Files

| File | Description |
|---|---|
| `ONB__phase-e__completion_and_release_preparation.md` | Bounded continuation ONB (`TRACE`). |
| `evidence/phase-e-3.0.0-release-package.md` | Exact replayable six-destination release input (`VALUE`). |
| `evidence/EV__phase-e__sweep_correction_and_release.md` | AC-1–AC-5 evidence and unresolved challenge record (`TRACE`). |
| `evidence/phase-e-completion-tests.txt` | Test, word-count, parity, census, mutant, and repair transcript (`TRACE`). |
| `evidence/phase-e-completion-accounting.txt` | K1/Candidate-II/final-union accounting (`TRACE`). |
| `evidence/phase-e-release-replay.txt` | Package replay and exact digest ledger (`TRACE`). |
| `RF__phase-e__sweep_correction_and_release.md` | This Executor result (`TRACE`). |

### Modified Files

| File | Changes |
|---|---|
| `.tfw/workflows/{handoff,research/base,review}.md` | Replaced each stale four-line TFW-54 promise with the exact optional resolved-principal sentence. |
| `.agent/workflows/tfw-{handoff,research,review}.md` | Copied complete corrected canonical bytes. |
| `.claude/commands/tfw-{handoff,research,review}.md` | Copied complete corrected canonical bytes. |
| `.tfw/glossary.md` | Added AT, Principal, Initiation Chain, Worktree Protocol, and Landing Commit routers. |
| `phase-b/HL__phase-b__named_principals.md` | Corrected B9 to the existing `#11-strategic-insights-planning-free` anchor. |
| `docs/scripts/test_integration.py` | Added Candidate-II selector/package/glossary/protection tests and repaired Phase-D-final versus K1-current separation. |
| `docs/scripts/test_runtime_context.py` | Added exact writer-rule positive/no-binding semantics, copy checks, historical/current separation, and mutants. |
| `phase-e/status.md` and Phase E journal | Recorded ONB binding and this RF transition only (`TRACE`). |

## 2. Key Decisions

1. Replaced the complete stale identity paragraph with the TS's one exact sentence. This removed 27
   words per canonical workflow and avoided a second source of principal/unit/origin semantics.
2. Routed each glossary term to one existing canonical section and copied no procedure.
3. Stored the release as a full-index embedded patch plus exact SHA-256 pre/post ledger. Space-only
   diff context uses a visible decoded marker so Candidate `git diff --check` remains clean.
4. Separated immutable Phase-D objects from the exact K1 current tree after the first full suite
   exposed two stale pre-K1 equality assertions. Historical bytes remain immutable; current markers
   are pinned to K1.
5. Froze Candidate II before EV/RF. When Main later raised four read-only challenges, recorded them as
   independent-review inputs and made no VALUE/ASSURANCE correction or acceptance ruling.

## 3. Acceptance Criteria

- [x] AC-1 — Exact K1 ancestry, 10/97 selector, F11, markers, state, digest, zero-diff
  `KNOWLEDGE.md`, clean knowledge-pending, and failed-intermediate disclosure are evidenced.
- [x] AC-2 — Current stale census is 3→0, exact writer rule and no-binding semantics hold, all copies
  match, and PowerShell word counts decrease 27 words in every canonical workflow.
- [x] AC-3 — Five glossary routers, B9 anchor, master NS2, Antigravity spelling, manifest/config
  protection, and the three terminal debt dispositions are evidenced without historical rewrite.
- [x] AC-4 — Exact package mechanically replays to the six expected postimages and rejects corruption;
  Candidate changes no canonical release destination. Main's later command/wording/scope challenges
  remain explicitly unresolved for independent review, not silently treated as acceptance.
- [x] AC-5 — Candidate position, exact 12/454 VALUE and two-path ASSURANCE selectors, configured
  collection/full test, targeted Phase E, strict docs, diff/parity/census/replay/mutants, snapshot/current
  separation, no new shipped runtime/config behavior, and 46/3,288 forecast are evidenced. Main's
  successor-test concern remains an independent-review question.

## 4. Verification

- Lint (`python -m pytest tools/tests/ docs/scripts/ -q --collect-only`): **529 collected**, exit 0.
- Tests (`python -m pytest tools/tests/ docs/scripts/ -q`): **528 passed, 1 skipped**, exit 0.
- Targeted (`python -m pytest docs/scripts/test_integration.py docs/scripts/test_runtime_context.py -q -k "phase_e"`): **15 passed, 310 deselected**, exit 0.
- Strict docs (`python -m mkdocs build --strict -f docs/mkdocs.yml --quiet`): exit 0; known plugin/corpus warning stream disclosed in EV.
- Package replay: exact six paths, 177 additions + 3 deletions = 180 LOC, all six SHA-256 postimages exact; two package mutants rejected.
- Git/census/parity: `git diff --check` clean; stale current canon 0; workflow words 2024/1140/2095; three canonical/copy hashes exact; six release destinations, manifest and config unchanged from `b0bfcd2…`.

## 5. Evidence

See [Phase E completion EV](evidence/EV__phase-e__sweep_correction_and_release.md) for evidence details.

Evidence verdict: 6/6 mechanical evidence rows VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A.
This is an Executor attestation, not disposition of Main's challenges or a Reviewer verdict.

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|---:|---:|---|---|
| 1 | `docs/scripts/test_integration.py` | 2829 | missing-test | Main asks whether the current-project six-release-destination equality assertion would necessarily fail after legitimate G-3 instead of separating immutable pre-release snapshot from post-release current state/full suite. **UNRESOLVED — Reviewer checks; no post-Candidate assurance edit.** |
| 2 | `evidence/phase-e-3.0.0-release-package.md` | 91, 364, 372–374, 381 | missing-test | Main asks whether Python/MkDocs commands lack explicit `$releaseTree` CWD/exit propagation and whether rollback refers to the patch after application removes it. **UNRESOLVED — Reviewer checks; no package edit.** |
| 3 | `evidence/phase-e-3.0.0-release-package.md` | 251 | naming | “no shared knowledge index” may be ambiguous because semantic `KNOWLEDGE.md` remains; RTBO retired the task portfolio cache and line ceilings. **UNRESOLVED — Reviewer checks; no package edit.** |
| 4 | `evidence/phase-e-3.0.0-release-package.md`; `knowledge/constraint.md` F11 | 190; 18 | naming | Provider-neutral AT wording must not imply an admitted Claude-only complete role chain; F11 bounds the first release to provider-homogeneous long-lived chains and fresh cross-provider helpers. **UNRESOLVED — Reviewer checks; no package edit.** |

## 7. Fact Candidates

No fact candidates. Main's post-Candidate agent read-only challenges are implementation/review
observations in §6, not human-sourced project facts.

## 8. Strategic Insights (Execution)

No strategic insights.

## 9. Diagrams

No diagrams.

---

*RF — TFW_20260902-111644_CRATM / Phase E: Sweep correction and release preparation | 2026-09-07*

## 10. Return round 1 — replacement Candidate II

### 10.1 What Was Done

The ruled Rung-1 round repaired only the existing release-package VALUE carrier and the two existing
ASSURANCE modules. Package execution now captures the invocation's exact commit independently from
the six fixed content preimages, runs every configured gate through an explicit native fail-fast
helper in the named release tree, retains its patch through a verified forward → reverse → reapply
cycle, and restores the exact initial index/staging between applications. Assurance preserves
immutable pre-release Git objects while accepting only coherent exact pre-release or six-postimage
successor states; this covers legitimate K2/DONE and G3 without a late assurance write and rejects
mixed/corrupt states. Migration and changelog prose now preserve semantic `KNOWLEDGE.md` §4 and the
provider-homogeneous/Codex-first/Claude-native-proof/fresh-helper admission boundary.

Replacement Candidate II is `b5a45c622c035c574d0fd5f5f7795add769be529` (tree
`bb42a3eb351abf7af778b89e0a40d65099c24a7e`). Failed attempt
`6c93e813e7a3ccae05b74a85170cca36c2de8856` remains its ancestor. Contemporaneous exact-path staging
is committed at `c565cdb465639dd91e700c76e5c562b2451f5529`; revised evidence follows Candidate at
`9c57778e067ce0c09ddb05b6f257e2f0c5554371` and contains no VALUE/ASSURANCE change.

#### 10.1.1 Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | Planning `759475fe232fee39f7e25a2aa0f25df2214cde7f`; TS blob `96585e0f8bd3d49b8d81f17bed96821b76cef1d3`; Rung-1 ruling `6ceaa7d9e1ea05162fae6404dad2130c8e1f5b30`; dispatch `ed69a3ca919c0cfd0fcd7520d5f89e63ecd07c1b` |
| Baseline / Candidate | `b0bfcd22125d8a34366d7eb885a2fb54234bdc7d` / `b5a45c622c035c574d0fd5f5f7795add769be529` |
| VALUE membership | MODIFY three canonical workflows for the exact writer rule; MODIFY their six accepted byte copies; MODIFY glossary for five routers; MODIFY Phase-B HL for B9; CREATE the package as accepted release input. All 12 are VALUE by the unchanged TS. Only the package changed this repair; the other 11 equal `6c93e813…`. |
| Arithmetic | 480 additions + 37 deletions = 517 touched text LOC; 12 logical files; 11 MODIFY + 1 CREATE; binary/non-text N/A 0 |
| Membership deviations | None. Every literal VALUE member changes over the fixed Baseline; exactly the two approved ASSURANCE paths change outside it. Candidate's own ruled repair commit contains only package + those two assurance paths. |
| Trigger disposition | `KEEP_PHASE_E / COMPLETE_THEN_RELEASE`: cause—four in-TS AC-4/AC-5 defects; cost—one same-Executor repair and same-Reviewer return; assurance—current/release full suites, strict builds, native fail-fast, reversal, corrupt mutants; split—none; authority—Main A8 Rung-1 ruling; terminal result—inside unchanged selector/budgets. |
| Authority and timing | Immutable 12/900; owner 24/1800. Actual 12/517 is below both; ruling and dispatch preceded `RF→ONB`, staging and all product writes. No late authority or denominator ratchet. |
| Reproduction | Raw-NUL argument-array parsing of `git diff --name-status --find-renames=50% -z` and `--numstat` from fixed Baseline to Candidate over the literal TS array; no line subtraction or repair-only measurement. See `evidence/phase-e-completion-accounting.txt`. |

The whole 46-path `957f7be8f5f208b87be12a8cd4d67b24af00cd1e` → Candidate measurement has
40 currently changed paths and 2612+661=3273 LOC. Adding the complete 200-LOC K2 ceiling and exact
187+3=190 LOC release patch gives 3663≤4000. Package SHA-256 is
`c080af1e4905a77e009e85206fac5d5f805f58150133b7e877d675e7368f4214`.

#### 10.1.2 New and Modified Files in This Round

No new file or product path was created in this return round.

| File | Round change |
|---|---|
| `evidence/phase-e-3.0.0-release-package.md` | VALUE: corrected executable/reversible package, postimages and RTBO/provider prose |
| `docs/scripts/test_integration.py` | ASSURANCE: coherent pre/post release state, reverse/reapply/index proof and successor-compatible payload checks |
| `docs/scripts/test_runtime_context.py` | ASSURANCE: package execution/semantic contract and negative mutants |
| Cumulative ONB/EV/RF, three existing evidence attachments, status and journal | TRACE: ruled return, contemporaneous staging, failures, results, accounting and lifecycle only |

### 10.2 Key Decisions

1. Current release destinations are validated as one complete state: all immutable preimages or all
   package postimages. Any mixture or byte corruption fails; unrelated K2/DONE successors do not.
2. `$contentBaseline` is fixed only for six preimages; `$executionBaseline` is runtime-captured exact
   `HEAD`, so Candidate and later post-DONE execution are exact without a self-referential future SHA.
3. Native commands share one location-preserving helper that checks `$LASTEXITCODE` immediately and
   throws. The package retains/reconstructs the patch and checks both index tree and staged names.
4. The narrow 3.0.0 migration path exemption applies only to two files it explicitly tells an
   operator to delete; it does not weaken general payload-path resolution.

### 10.3 Acceptance Criteria

- [x] AC-4 — The package executes in its named Candidate-based release tree, distinguishes execution
  baseline from immutable content preimages, propagates native failures, proves exact six-file
  forward/reverse/reapply and staging restoration, and retains a usable rollback patch.
- [x] AC-4 — RTBO prose retains semantic `KNOWLEDGE.md` and §4 while retiring only the portfolio cache
  and numeric ceiling; provider prose retains the exact admission boundary. Negative mutants fire.
- [x] AC-5 — Immutable pre-release snapshot checks, legitimate pre-release/K2-DONE state and exact G3
  postimages coexist without late assurance edits; corrupt/mixed successors fail.
- [x] AC-5 — Replacement Candidate positioning, fixed 12/517 VALUE, exactly two ASSURANCE, 46/3663
  whole forecast, exact staging evidence and all required current/release gates are verified.
- [x] AC-1–AC-3 — Not returned and not redone; the prior VERIFIED evidence remains unchanged and the
  other eleven Candidate-II VALUE outputs are byte-identical to failed attempt `6c93e813…`.

### 10.4 Verification

- Collection: **530 collected**, exit 0 in current and exact post-package release trees.
- Targeted Phase E: **16 passed, 310 deselected**, exit 0.
- Current full suite: **529 passed, 1 skipped**, exit 0.
- Package-created exact-Candidate release-tree full suite: **529 passed, 1 skipped**, exit 0.
- Current and release-tree configured strict MkDocs: exit 0; unchanged historical warning stream is
  disclosed in EV. Current and staged-release diff checks: exit 0.
- Extracted native helper: success command passed; Python exit 7 was propagated as an exception.
- Package cycle: all six preimages → all six postimages → exact preimages/index/empty staging → all
  six postimages/exact staged set; final release index `721a89043adbf53558f1abdae905777ff7be24bd`.
- Initial failures remain in evidence: ineffective one-occurrence mutant; two extraction/probe harness
  errors; and first release full suite 526 passed/1 skipped/3 failed before successor guards were fixed.

### 10.5 Evidence

See [Phase E completion EV](evidence/EV__phase-e__sweep_correction_and_release.md) §8 for details.

Return-round evidence verdict: 6/6 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A.

### 10.6 Observations (out-of-scope, not modified)

No observations. The four prior §6 items were the ruled in-scope Rung-1 bound and are resolved by this
round; no consequential out-of-scope issue was found.

### 10.7 Fact Candidates

No fact candidates.

### 10.8 Strategic Insights (Execution)

No strategic insights.

### 10.9 Diagrams

No diagrams.

---

*RF return round 1 — TFW_20260902-111644_CRATM / Phase E | 2026-09-07*
