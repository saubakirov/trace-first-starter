# TS — TFW_20260902-111644_CRATM / Phase A: Isolation and attribution for concurrent work

> **Date**: 2026-09-05
> **Author**: Main Coordinator (Codex)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW_20260902-111644_CRATM](../HL-TFW_20260902-111644_CRATM.md) — `🔒 FROZEN`, including applied A6
> **Phase HL**: [HL__phase-a__isolation_and_attribution](HL__phase-a__isolation_and_attribution.md) — derivation-only
> **Accounting Baseline**: `11888e547b0b37dc09469aee8fe2fd897d797906`

> **Prospective immutable owner-approved denominator**: `7` logical touched VALUE files and `160`
> touched text LOC (`135` additions + `25` deletions). It becomes immutable on owner approval and
> never ratchets.

---

## 1. Objective

Make concurrent mutation safe and attributable without adding a TFW runtime: every mutation-bearing
delegated run receives an isolated Git worktree, every commit stages explicit paths, and every
deliverable landed by another session remains discoverable under the task and phase that produced it.

## 2. Scope

### In Scope

- Add one canonical worktree protocol to `conventions.md` that answers location, readable naming,
  creator, landing point, deletion owner, and dead-run disposition while stating that isolation is not
  a lock.
- Name and forbid broad staging; require full-path staging, cached-set inspection, preservation of
  unrelated dirty work, and a stop on an inseparable foreign hunk.
- Define a landing commit for a deliverable crossing a session boundary, including the TD-178 worked
  example and preservation of an exact TS-named Candidate before worktree deletion.
- Put the shortest addressed enforcement edge on Executor and Reviewer surfaces while preserving
  RCFR selective reads and VBSA Candidate-before-EV/RF/REVIEW accounting.
- Synchronize the four currently tracked whole-copy adapters for the two changed workflows and prove
  byte parity.
- Apply the worktree and exact-path rules to Phase A's own execution from its first implementation
  write, before the new prose exists in the canon.
- Record final word counts for `conventions.md`, `handoff.md`, and `review.md`. The inherited workflow
  counts are `2,013` and `2,102`; any growth must be the minimum materially necessary.

### Out of Scope

- Branch policy, merge/rebase/cherry-pick strategy, a second transport, or any TFW-61 outcome.
- Session identity, dispatch fields, principals, bindings, profiles, provider routes, Role Assignment,
  or the Phase D Claude-native acceptance gate.
- A script, hook, daemon, scheduler, lock, liveness/session registry, config key, validator, test file,
  new artifact class, or product file of any kind.
- Renaming or adopting a provider-owned worktree path as TFW canon; provider names outside
  `.tfw/adapters/`.
- Editing `.tfw/adapters/manifest.yaml`, `.agents/skills/**`, `tasks/**`, another task's workspace,
  the master/phase HL, research artifacts, or any later CRATM phase.
- Compressing RCFR/VBSA wording or redefining VALUE classes, Candidate, triggers, accounting authority,
  lifecycle, review ratio, or adapter topology.

## 3. Principles Check

| # | HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P1 | Human authority, bounded delegation | AC-6 / HC-1 | Owner approves this TS and denominator; Coordinator cannot relax protected boundaries |
| P2 | A mandate is a ceiling | AC-6 / HC-1 | Exact selector before every write; prospective stop on growth or a new path |
| P3 | Every initiation edge starts at a coordinator | N/A | Phase C owns initiation chains; Phase A may not author them |
| P4 | Every chain terminates at a human | N/A | Phase B/C outcome; no principal or chain is introduced here |
| P5 | Authority is carried by the name | N/A | Phase B outcome; no profile or grant is introduced here |
| P6 | A role is context, never permission | AC-2, AC-4 | Same staging/landing obligations follow workflow roles, not provider identity |
| P7 | Permissions are per role | AC-2, AC-4 | No participant or vendor condition may alter an Executor/Reviewer obligation |
| P8 | Git owns the mechanism, TFW the protocol | AC-1, AC-3 | Prose composes ordinary `git worktree` and commits; no implementation ships |
| P9 | Nothing executable | AC-5 | Changed selector contains only Markdown canon and tracked copies |
| P10 | A separate session is not an independent person | AC-3 | Landing records production context, never claims independent judgement |
| P11 | The autonomy boundary is declared | N/A | Phase D outcome; Phase A does not define an autonomy switch |
| P12 | Isolation is not a lock | AC-1 | Protocol states the distinction and adds no serialization claim |

## 4. Affected Files and Value-Bearing Accounting

The seven rows below are the complete planned implementation selector. Each tracked adapter copy is
`VALUE` because it is accepted shipped behavior even when byte-identical to its canonical source.

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `.tfw/conventions.md` | MODIFY | `VALUE` | Canonical worktree, staging, landing, and §14 anti-pattern rules |
| `.tfw/workflows/handoff.md` | MODIFY | `VALUE` | Executor-side exact-path and landing enforcement at the commit/Candidate boundary |
| `.tfw/workflows/review.md` | MODIFY | `VALUE` | Reviewer-side independent staging and landing verification |
| `.agent/workflows/tfw-handoff.md` | MODIFY | `VALUE` | Exact tracked copy of canonical handoff workflow |
| `.agent/workflows/tfw-review.md` | MODIFY | `VALUE` | Exact tracked copy of canonical review workflow |
| `.claude/commands/tfw-handoff.md` | MODIFY | `VALUE` | Exact tracked copy of canonical handoff workflow |
| `.claude/commands/tfw-review.md` | MODIFY | `VALUE` | Exact tracked copy of canonical review workflow |

### Declared excluded selectors

| Selector | Class | Treatment |
|---|---|---|
| Exact Phase HL, this governing `TS__phase-a__isolation_and_attribution*.md`, `status.md`, `journal/*.md`, `ONB__phase-a__isolation_and_attribution.md`, `RF__phase-a__isolation_and_attribution.md`, `REVIEW__phase-a__isolation_and_attribution*.md`, `evidence/EV__phase-a__isolation_and_attribution.md`, and `review/**`, all below this `phase-a/` directory | `TRACE` | Required lifecycle, evidence, and review surface; never part of delivery measures |
| Test caches, diff extracts, temporary worktree inspection output, and transient parity results | non-value `DERIVED` | Reproducible and untracked; never persisted as delivery or a parallel ledger |

No planned file mixes a narrower excluded implementation role. If implementation makes VALUE and an
excluded role inseparable in one listed file, the whole fixed Baseline→Candidate file diff is VALUE.
Freehand hunk subtraction is prohibited.

### Prospective accounting contract

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | Only changed paths in the seven exact `VALUE` rows above |
| Baseline / selector source | `11888e547b0b37dc09469aee8fe2fd897d797906`; this TS at its owner-approval commit, resolved through phase status/journal and Git |
| Candidate rule | First tested Executor commit with all required VALUE changes, before EV/RF/REVIEW/final transition; excluded-only later writes do not move it; later VALUE requires a new Candidate and recomputation |
| Logical VALUE files | Planned `7`; rename = one, though no rename is planned |
| Touched text LOC | Planned `135` additions + `25` deletions = `160`; numeric numstat fields; binary/non-text = per-file `N/A` |
| Triggers / disposition | Configured prompts are `50` files and `5,000` LOC. **Keep one phase:** 7/160 is below both, and splitting canonical rules from their role consumers/copies would ship inconsistent behavior |
| Multiplier / authority | Immutable planned denominator 7/160; Owner required at `≥14` VALUE files, `≥320` touched LOC, growth from an applicable zero, or any HC-1 boundary change. Coordinator may rule only prospectively below that ceiling inside unchanged boundaries |
| Approval epoch / failure | Prospective from owner approval of this TS; missing/mutable/mismatched/late contract facts = `BLOCKED`; metric-only `N/A`; unresolved phase attribution = `INVALID`; `DEFERRED` is non-terminal |

```powershell
$valuePaths = @(
  '.tfw/conventions.md',
  '.tfw/workflows/handoff.md',
  '.tfw/workflows/review.md',
  '.agent/workflows/tfw-handoff.md',
  '.agent/workflows/tfw-review.md',
  '.claude/commands/tfw-handoff.md',
  '.claude/commands/tfw-review.md'
)
git diff --name-status --find-renames=50% -z 11888e547b0b37dc09469aee8fe2fd897d797906 <CANDIDATE_SHA> -- $valuePaths
git diff --numstat --find-renames=50% -z 11888e547b0b37dc09469aee8fe2fd897d797906 <CANDIDATE_SHA> -- $valuePaths
```

`<CANDIDATE_SHA>` is the full immutable SHA produced by the Candidate rule; it is unknown by design
until implementation has passed its pre-evidence gates and is never guessed or backfilled.

### Prospective scope rulings

None at approval. Before touching another VALUE path or forecasting more work, the Executor stops.
The Coordinator may accept a necessary constituent only prospectively, below 2× both immutable
denominators, with unchanged objective, accepted outcomes, phase ownership, public behavior,
architecture, persisted data, and security/trust/authority boundaries. The ruling must record cause,
cost, assurance impact, split alternative, Saint-Exupéry judgment, authority, verdict, time, and ref.
Performed work is a deviation, never retroactive approval.

### Task-local hard constraint — HC-1

| M1 consequence | M2 object/risk | M3 measure/selector | M4 pre-act check | M5 softer-control gap | M6 change authority |
|---|---|---|---|---|---|
| A foreign write can corrupt another task's evidence, add a runtime, or silently expand transport/identity architecture | Every repository path outside the seven VALUE rows and declared Phase A TRACE; especially master/phase HL, research, other workspaces, `tasks/**`, `.tfw/adapters/manifest.yaml`, `.agents/skills/**`, code/config, and provider runtime state | Zero Baseline→Candidate changes outside the seven VALUE paths; Candidate changed set contained by VALUE plus authorised Phase A TRACE only | Compare intended and actual full path sets before every write and before Candidate creation; stop on first mismatch | File/LOC prompts cannot distinguish one tiny unauthorized architecture/history mutation from legitimate prose | Owner `saubakirov` prospectively; Coordinator multiplier authority cannot relax HC-1 |

**Actions (not budget dimensions):** 7 modified VALUE files; 0 planned ASSURANCE files; required TRACE
files created/appended by lifecycle. **Immutable owner-approved denominator:** 7 VALUE files and 160
touched text LOC; never ratchets after approval.

## 5. Acceptance Criteria

### AC-1: Complete worktree protocol

`conventions.md` defines one portable protocol over ordinary Git and answers all six master questions.

- [ ] Location names both POSIX and Windows per-machine forms outside the project tree without
  canonizing a provider-owned path.
- [ ] Naming reads back to task and phase, admits the later principal extension, and forbids renaming
  an established worktree.
- [ ] The coordinator creates before mutation-bearing dispatch; a read-only run may share because it
  contends for no writes.
- [ ] Landing occurs only after role output and review; deletion occurs only after landing,
  verification, and exact Candidate reachability.
- [ ] A dead run's tree is read and landed before removal; session death does not authorize deletion.
- [ ] The protocol says a worktree isolates index/files and is not a lock or merge strategy.

Gate: Read the new uniquely headed protocol and map each sentence to the six items; verify no branch
or merge strategy and no executable implementation was added.
Evidence: Real repository worktree listing plus recorded path, git common directory, separate index,
landing reachability, and cleanup-precondition checks in phase EV.

### AC-2: Exact-path staging is enforced on both role surfaces [depends: AC-1]

- [ ] `git add -A`, `git add .`, and `git commit -a` are named and forbidden for shared-tree work.
- [ ] Full pathspec staging, full status, and cached-name inspection precede every commit; the selected
  commit cannot inherit an already-staged sibling path.
- [ ] An inseparable foreign hunk causes STOP; unrelated dirty work is preserved, never normalized.
- [ ] `handoff.md` requires the Executor behavior at its commit/Candidate checkpoint and `review.md`
  independently verifies the resulting path set and staging/landing evidence.

Gate: Search the three canonical files for all forbidden forms, exact-path requirement, cached-set
inspection, foreign-hunk stop, and preservation rule; inspect the two role checkpoints in context.
Evidence: In Phase A's own worktree, record pre-commit status/cached path sets showing only authorised
paths; exercise a harmless temporary shared-index fixture if the real tree contains no sibling change.

### AC-3: Cross-session landing preserves producer attribution [depends: AC-1] [depends: AC-2]

- [ ] A deliverable committed by a session other than its producer lands in its own commit; the
  subject names the producer task and phase while `role` names the acting role.
- [ ] The TD-178 wrong/right example is present and `git log -- <path>` can recover the producing task.
- [ ] If a TS fixes a Candidate, that exact commit remains reachable after landing and before cleanup;
  recreating equivalent bytes under only a new SHA is explicitly insufficient.
- [ ] The rule never reintroduces the shell-leading-slash or message-wide `--grep` defects.

Gate: Inspect the canonical worked example and replay `git log --format="%H %s" -- <changed-path>` on
the Phase A landing; verify the full Candidate with `git cat-file -e <CANDIDATE_SHA>^{commit}`.
Evidence: Phase EV records Candidate, landing commit, producer-shaped subject, path history, and
reachability before any worktree cleanup.

### AC-4: Selective loading and tracked copies remain coherent [depends: AC-2] [depends: AC-3]

- [ ] Each new rule has one canonical body and the shortest addressed workflow edge; no full body is
  duplicated into a role workflow.
- [ ] Handoff retains ONB→implementation/test→Candidate→EV/RF ordering; review retains independent
  accounting replay and Purpose Check.
- [ ] Existing unique headings and ordered Read Contracts remain valid; no universal preamble returns.
- [ ] Each changed canonical workflow is byte-identical to its `.agent` and `.claude` tracked copies.

Gate: Compare each workflow pair by file hash; run `git diff --check` and
`python .tfw/scripts/gen_index.py --check project`.
Evidence: Phase EV records the four pair hashes and the structural-check output.

### AC-5: Frozen boundaries and attention contract hold

- [ ] Candidate contains only the seven VALUE paths; no code, config, test, hook, runtime, registry,
  provider profile, manifest, task-history, branch policy, or later-phase change appears.
- [ ] No provider name is added to `.tfw/` outside `adapters/`.
- [ ] `conventions.md`, `handoff.md`, and `review.md` exact before/after word counts are recorded.
- [ ] Any positive workflow delta is the minimum needed at its addressed enforcement site. A shorter
  pointer alone is rejected because selective loading does not guarantee the canonical §4 body at the
  commit/review checkpoint; substitution or a same-document cut is rejected when it would remove
  RCFR/VBSA semantics already required there.

Gate: Inspect Candidate changed paths and diff; compare word counts to `9,791`, `2,013`, and `2,102`;
search changed `.tfw/` lines for provider names and prohibited runtime/config vocabulary.
Evidence: Phase EV records exact counts, deltas, necessity assessment, considered shorter form, and
the no-prohibited-surface result.

### AC-6: Value-bearing accounting is reproducible [depends: AC-4] [depends: AC-5]

- [ ] Baseline, approval commit, Candidate, literal seven-path selector, membership, additions,
  deletions, touched LOC, trigger disposition, authority and timing are all immutable and consistent.
- [ ] Candidate is the first tested Executor VALUE commit and precedes EV, RF, REVIEW, and RF state.
- [ ] The NUL-safe commands reproduce the same logical membership and numeric arithmetic.
- [ ] Any missing/mutable/mismatched/late fact is `BLOCKED`; a later VALUE write creates a new
  Candidate and recomputation rather than moving the result informally.

Gate: Run the two §4 commands with full SHAs and the literal array; compare the result to one dedicated
EV accounting row and later to independent REVIEW replay.
Evidence: Full Baseline/Candidate/approval refs, raw membership/arithmetic, terminal trigger
disposition, and authority result in `evidence/EV__phase-a__isolation_and_attribution.md`.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-a__isolation_and_attribution.md` | Per-AC evidence, word-count necessity, Candidate/landing reachability, parity, and one accounting row |

## 6. Technical Guidance

- Use the rendered protocol and wrong/right landing example in Phase HL §3.1 as non-binding drafting
  guidance; preserve the outcomes and sharpen wording where the current canon offers a shorter fit.
- Prefer one new `conventions.md` §4 subsection per governed concept and compact §14 rows for measured
  failures. Workflows should reference the unique heading or state only the checkpoint-specific edge.
- Create the Phase A execution worktree from the approved TS baseline. Record its absolute path and
  common Git directory before mutation; keep one mutation owner.
- Synchronize only the four tracked copies listed in §4. Do not infer a new adapter target from a
  missing directory or alter the manifest.

## 7. Definition of Failure

- ❌ Any of the six worktree questions is unanswered, or isolation is described as locking or merge policy.
- ❌ A broad staging form remains allowed, exact-path/cached-set inspection is absent from either role
  surface, or Phase A commits a foreign path/hunk.
- ❌ A crossing deliverable can land under the landing session's task, shares an unrelated commit, or
  loses exact Candidate reachability before cleanup.
- ❌ Selective-read or VBSA order regresses, a tracked copy differs, or a canonical rule body is duplicated.
- ❌ Candidate touches a path outside the seven VALUE rows or introduces executable/runtime/config,
  session registry, provider-dependent canon, branch strategy, or later-phase semantics.
- ❌ An inherited over-limit workflow grows without the exact count, minimum-necessity argument, and
  rejected shorter reference/substitution/cut required by A5.
- ❌ Accounting cannot be reproduced from immutable approval, Baseline, Candidate, and selector facts.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Rule body deepens attention debt | One canonical body, shortest role edges, A5 exact-count/necessity evidence |
| Worktree protocol drifts into transport policy | State lifecycle point and owner, never merge method; AC-1 tripwire |
| Phase B would require renaming Phase A worktrees | Name grammar admits a principal suffix but established paths are immutable |
| Landing repeats TD-178 or loses Candidate | Own landing commit, producer-shaped subject, reachability gate before cleanup |
| Selective reads hide the rule at action time | Address exact headings or state the minimum checkpoint edge; AC-4 context inspection |
| Phase A reproduces shared-index corruption while writing the fix | Separate worktree and exact paths from first implementation commit |
| Forecast is exceeded | Stop prospectively; Coordinator below 2× and unchanged bounds, otherwise Owner |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|---|---|---|
| `.tfw/conventions.md` | Phases B, C, D | Phase A owns §4 worktree/staging/landing clauses; later phases preserve them and use separate subsections |
| `.tfw/workflows/review.md` | Phases C, D | Phase A owns staging/landing verification; later routing/team edits must not replace this edge |
| `.tfw/workflows/handoff.md` | Phase D | Phase A owns commit/landing enforcement; Phase D adds delegation semantics at a distinct checkpoint |
| Four tracked workflow copies | Phases C, D, E when sources change | Re-sync from canonical source after each owning phase; never edit copies independently |

---

*TS — TFW_20260902-111644_CRATM / Phase A: Isolation and attribution for concurrent work | 2026-09-05*
