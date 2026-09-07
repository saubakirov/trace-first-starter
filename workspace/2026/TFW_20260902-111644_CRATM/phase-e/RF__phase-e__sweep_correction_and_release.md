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
