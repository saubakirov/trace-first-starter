# TS — TFW_20260902-111644_CRATM / Phase E: Integration gate

> **Date**: 2026-09-07
> **Author**: Phase E Coordinator (Codex; `robert` attribution under master A8)
> **Status**: ✅ APPROVED — Main Coordinator / LEAD `robert` under master A8, 2026-09-07; exact reviewed plan `82f34a8ae12dd3389355879c08ede402ce28a609`, TS blob `ab7d168081e65f904ee7b3e10457e54f64fcf75b`; this metadata commit is the approval epoch
> **Parent HL**: [Phase E HL](HL__phase-e__sweep_correction_and_release.md)
> **Source pins**: Baseline/knowledge `957f7be8f5f208b87be12a8cd4d67b24af00cd1e`; Main `2adf89918c64643f9edfde07182508decef1fde4`; D final `18d54060da8796ddca7d648365cbfeb18f60690b`; D approval `b755de9128f2b0442615a4ca8b787761f937bbcd`; D Candidate `fac67ef443c5cb50a766cc6c6c639ea60a259437`; RTBO/saved master `ae494e2a9f9ee82e5d0bd2a9d79e4e23d58a1822`; participants `3153c5d12528bc5bf859333f5d17097fc04b4d46`

---

## 1. Objective

Produce and independently check one tested D+RTBO+Robert/A8+knowledge integration commit, then have
Main land it in saved master before any remaining Phase E VALUE work begins.

## 2. Scope

### In Scope

- Merge exact Main into the approved `957f7be…` planning lineage; resolve the two known conflicts;
  semantically audit clean auto-merges; preserve every reviewed dependency anchor.
- Adapt only the two named ASSURANCE files so immutable D snapshots and the current integrated tree
  are checked as different epochs; run targeted, configured full, strict-build, ancestry, parity,
  accounting, and RTBO-boundary checks before committing Candidate I.
- Independent read-only checkpoint by the one E Reviewer; Main-only fast-forward saved landing with
  explicit preservation of concurrent foreign work.

### Out of Scope

- Sweep, glossary, manifest/citation debt, F11 correction, version/config/changelog/migration, RF,
  final REVIEW, KNW, DONE, tag, push, publication, and cleanup. These remain frozen Phase E outputs
  and need a subsequent exact approval and full non-duplicative VALUE plan in this same phase/team.
- Executor mutation of `D:\projects\research\steps-framework`; `.tfw/templates/project_config.yaml`,
  `docs/feedback/`, and `workspace/2026/TFW_20260907-020729_SLC/` are protected foreign work.
- New runtime, required Python/PyYAML, tracked index, config behavior, profile, role task, artifact
  class, fork/subagent, provider mixing, or historical rewrite.

## 3. Principles Check

| Master §7 principle | Enforced by | Gate |
|---|---|---|
| P1–P2 human authority / mandate ceiling | AC-2 | Main alone lands; budget escalation returns to owner |
| P3–P7 rooted units / identity is not authority | AC-1, AC-2 | Exact A8 lineage; distinct Executor and Reviewer tasks |
| P8–P9 Git protocol / nothing executable | AC-1 | Git ancestry, full verification, RTBO no-runtime boundary |
| P10–P12 separate sessions / explicit autonomy / isolation | AC-2, HC-E3 | Separate worktrees; saved checkout stays outside Executor scope |

## 4. Affected Files and Value-Bearing Accounting

The literal VALUE selector is:

```powershell
$valuePaths = @(
  '.agent/workflows/tfw-handoff.md', '.agent/workflows/tfw-plan.md',
  '.agent/workflows/tfw-research.md', '.agent/workflows/tfw-resume.md',
  '.agent/workflows/tfw-review.md', '.claude/commands/tfw-handoff.md',
  '.claude/commands/tfw-plan.md', '.claude/commands/tfw-research.md',
  '.claude/commands/tfw-resume.md', '.claude/commands/tfw-review.md',
  '.tfw/adapters/codex/AGENTS.md.template', '.tfw/conventions.md',
  '.tfw/templates/HL.md', '.tfw/templates/journal/event.md',
  '.tfw/templates/team/profile.md', '.tfw/workflows/handoff.md',
  '.tfw/workflows/plan.md', '.tfw/workflows/research/base.md',
  '.tfw/workflows/resume.md', '.tfw/workflows/review.md', 'AGENTS.md',
  'KNOWLEDGE.md', 'team/README.md', 'team/robert.md', 'team/saubakirov.md'
)
```

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| The 25 `$valuePaths` | MODIFY; `team/robert.md` CREATE | `VALUE` | Integrated D/A8/profile/knowledge product, including every approved dependency delta on this Baseline |
| `docs/scripts/test_integration.py`; `docs/scripts/test_runtime_context.py` | MODIFY | `ASSURANCE` | Combined RTBO+D current-tree checks plus immutable D snapshot guards, mutants, lineage, parity, and protected-state checks |
| Master/phase HL, status, journal, Phase-D ONB/RF/REVIEW/EV and attachments | CREATE/MODIFY/import | `TRACE` | Decision, lifecycle, evidence, and reviewed dependency history |

Later sweep/knowledge/release paths are not classified away: they are absent from this execution
subject and must enter the subsequent Phase E VALUE selector when exact approval is requested.

### Prospective accounting contract

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | Candidate-I integrated product; the 25 literal `$valuePaths`; whole Baseline→Candidate diff, no line subtraction |
| Baseline / selector source | `957f7be8f5f208b87be12a8cd4d67b24af00cd1e`; this TS at its exact approval commit |
| Candidate rule | First fully tested merge commit after approval, with the approved planning line as first parent and exact Main as second parent, before EV/checkpoint landing; TRACE-only writes do not move it; later VALUE needs a new approved subject/Candidate and full recomputation |
| Logical VALUE files | Immutable plan: 25; rename = one |
| Touched text LOC | Immutable plan: 1,200 total. Actual additions + deletions come only from numeric Candidate numstat; binary/non-text is per-file N/A |
| Triggers / disposition | Configured prompts 50 files / 5,000 LOC. `KEEP_PHASE_E / INTEGRATION_GATE_FIRST`: the 25/982 virtual forecast includes conflict markers; 25/1,200 bounds semantic resolution; assurance is full; later work is not summed into this result |
| Multiplier / authority | Immutable `25/1200`; owner boundary `50/2400`. Main may rule a necessary constituent below both while outcome and constraints stay fixed; at/above either or from planned zero returns to owner before work |
| Approval epoch / failure | Exact Main approval after verifying source pins; missing/mutable/mismatched/late = BLOCKED; unresolved phase attribution = INVALID; metric-only N/A; DEFERRED non-terminal |

```powershell
git diff --name-status --find-renames=50% -z 957f7be8f5f208b87be12a8cd4d67b24af00cd1e <CANDIDATE_I_SHA> -- $valuePaths
git diff --numstat --find-renames=50% -z 957f7be8f5f208b87be12a8cd4d67b24af00cd1e <CANDIDATE_I_SHA> -- $valuePaths
```

### Prospective scope ruling

`KEEP_PHASE_E / INTEGRATION_GATE_FIRST`: cause — owner needs approved D in saved master now; cost —
one interim independent replay and landing preflight; assurance — targeted conflict, full configured,
build, ancestry, parity, and saved-preservation checks; split — later outcomes wait for another exact
approval but remain Phase E and use the same roles; Saint-Exupéry — no new carrier or unit; authority —
Main Coordinator under A8; verdict — `APPROVED / KEEP_PHASE_E / INTEGRATION_GATE_FIRST`, Main
technical ruling on exact plan `82f34a8…`, 2026-09-07.

### Task-local hard constraints

| M1 consequence | M2 object/risk | M3 measure/selector | M4 pre-act check | M5 softer-control gap | M6 change authority |
|---|---|---|---|---|---|
| D remains invisible while polish proceeds | Candidate ancestry/tree and saved HEAD | before commit: first-parent HEAD plus exact `MERGE_HEAD`; after commit: two parents, five ancestor checks, exact 25-path diff, saved HEAD | Reviewer checkpoint green and Main landing before later VALUE | Final review is too late for the immediate usable result | Main within A8; changed outcome returns owner |
| RTBO or D semantics are silently lost | no-runtime/no-index boundary; `fac67ef…` and final REVIEW; D82/D83 | absence/hash/census checks plus configured suite | resolve/audit before Candidate commit | textual merge success misses contradictory rules/tests | Main for in-TS resolution; frozen change uses rule 8 |
| Concurrent saved work is overwritten | foreign tracked hunk and two untracked roots | pre/post status, hash, Candidate diff exclusion | Executor never opens saved checkout; Main preflights | remote review cannot observe a later saved overwrite | owner for foreign work; Main may abort, never normalize |

**Actions (not budget dimensions):** 24 MODIFY + 1 CREATE VALUE; 2 MODIFY ASSURANCE; required TRACE only.
**Immutable owner-approved denominator:** 25 VALUE files; 1,200 touched text LOC; never ratchets.

## 5. Acceptance Criteria

### AC-1: Candidate I integrates every approved source without semantic regression

- [ ] Before commit, the approved planning HEAD is the first-parent source and `MERGE_HEAD` is exact
  `2adf899…`; after commit, Candidate has those two parents and descends from `957f7be…`, `2adf899…`,
  `ae494e2…`, `fac67ef…`, and `3153c5d…`.
- [ ] D approval `b755de…`, Candidate `fac67ef…`, final artifacts, and REVIEW anchors remain openable
  and byte-identical at their immutable Git snapshots. Current merged-tree checks are separate; no
  guard requires the legitimate E/A8/RTBO tree to equal the D approval epoch.
- [ ] `KNOWLEDGE.md` retains RTBO as D82 and final corrected CRATM as D83; it does not reinstate the
  superseded early-CRATM D82. `docs/scripts/test_integration.py` composes RTBO declared-path protection
  with the D managed-block exception. No conflict marker remains.
- [ ] Every automatic merge is semantically audited. Eight Plan/Research/Handoff/Review/Resume/Init/
  Knowledge/Update canonical workflows equal both installed accepted copies byte-for-byte.
- [ ] RTBO's no shipped runtime, no required Python/PyYAML, no tracked index, direct task-local
  discovery, upstream-only tools, and hidden non-primary documentation landings remain true.
- [ ] A8, `team/robert.md`, participant updates, approved knowledge `957f7be…`, and all Phase-D traces
  are present. Full configured collect/test, strict MkDocs build, targeted integration checks, and
  `git diff --check` pass before the tested merge is committed as Candidate.

Gate: pre-commit HEAD/`MERGE_HEAD`, post-commit parent/ancestry/blob checks; conflict/stale-runtime
census; canonical/copy digests; configured `python -m pytest tools/tests/ docs/scripts/ -q --collect-only`
and `python -m pytest tools/tests/ docs/scripts/ -q`; strict MkDocs; exact 25-path accounting.

Evidence: local Executor worktree, real Git objects and commands, raw outputs, exit codes, Candidate SHA.

### AC-2: Independent checkpoint and saved landing precede all later E work [depends: AC-1]

- [ ] The distinct E Reviewer independently checks Candidate from its own worktree without supplied
  totals as authority and reports exact green evidence or cited defects. This is an interim checkpoint,
  not final REVIEW and not a lifecycle verdict.
- [ ] Main alone verifies saved HEAD `ae494e2…` (or stops on an unexpected successor), proves Candidate
  is fast-forward reachable, records the foreign tracked hunk/untracked roots, and performs the landing.
- [ ] Saved HEAD equals Candidate afterward; the foreign `.tfw/templates/project_config.yaml` hunk and
  both untracked roots are unchanged. Candidate changes that template by zero bytes against `ae494e2…`.
- [ ] Phase E remains live; no RF, final REVIEW, KNW, DONE, release or cleanup claim is emitted. The
  same Executor/Reviewer addresses and exact landed SHA return for the next exact E order.

Gate: independent replay transcript plus Main pre/post HEAD, status, path diff/hash, ancestry, and
saved-tree checks; absence of later VALUE work.

Evidence: actual Reviewer task report and Main landing report with immutable SHAs.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-e__integration_gate.md` | AC-1/AC-2 evidence, accounting, and checkpoint verdicts |
| `evidence/phase-e-integration-lineage.txt` | Candidate parents, ancestry, blobs, conflicts, and saved landing |
| `evidence/phase-e-integration-tests.txt` | Targeted/full/build/parity raw results |

## 6. Technical Guidance

- Keep the merge uncommitted until conflict resolution and every Candidate test pass; validate
  `MERGE_HEAD` before commit, then Candidate parents/ancestry after it.
- Resolve knowledge by decision meaning/epoch, not side choice. In assurance, preserve immutable D
  snapshot guards while deriving current-tree expectations from the integrated sources.
- The 700–900 word range cannot retain 25 literal paths, the landing guard, and M1–M6; a glob or
  reference-only order was rejected because it loses replayability and protected saved-state checks.

## 7. Definition of Failure

- ❌ Candidate lacks a pinned parent/ancestor, changes a protected reviewed snapshot, loses RTBO
  boundaries, carries conflict markers, or passes by deleting/weakening historical assurance.
- ❌ Later E VALUE begins before independent check, confirmed saved landing, and subsequent exact approval;
  or the checkpoint is represented as RF/REVIEW/DONE.
- ❌ Saved foreign work changes, broad staging occurs, Executor touches saved checkout, or another task,
  profile, fork, subagent, runtime, index, tag, push, or publication enters scope.
- ❌ Dependency work is omitted, hand-subtracted, or added twice; accounting or authority is late.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Automatic merge is syntactically clean but semantically false | Named auto-merge audit, source-derived tests, independent checkpoint |
| A D snapshot guard rejects valid E evolution | Immutable-snapshot and current-tree expectations are distinct and mutation-tested |
| Saved work blocks fast-forward | Main aborts and coordinates; no Executor workaround or normalization |
| Checkpoint is mistaken for phase closure | Explicit no-RF/no-final-REVIEW boundary and subsequent exact approval |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|---|---|---|
| Canon/workflows/templates/adapters/assurance | A–D, RTBO, RCFR/VBSA/RTPSN | Preserve all reviewed semantics; exact Main+RTBO merge and full-suite gate |
| `KNOWLEDGE.md` | D docs, RTBO docs, approved knowledge pass | Keep RTBO D82 and final CRATM D83; no decision-number collision |
| Master HL, Phase-D folder, task journals | Master A7/A8; D | TRACE landing only; preserve exact Candidate/REVIEW anchors |

---

*TS — TFW_20260902-111644_CRATM / Phase E: Integration gate | 2026-09-07*
