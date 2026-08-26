# RF — TFW-60 / Phase A: Task State & Coordination

> **Date**: 2026-08-26
> **Author**: Claude Code (Executor)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-60](../HL-TFW-60__conflict_resistant_shared_workspace.md) · [HL — Phase A](HL__phase-a__task_state_and_coordination.md)
> **TS**: [TS — Phase A](TS__phase-a__task_state_and_coordination.md) — revision 2, approved by owner 2026-08-26
> **ONB**: [ONB — Phase A](ONB__phase-a__task_state_and_coordination.md) — 12 questions, all answered
> **Master freeze**: `c1782b3`
> **Baseline for every measurement**: `80d6a16`

---

## 1. What Was Done

The root `README.md` Task Board is gone. Live state lives in each task's own `status.md`,
coordination history in each task's own `journal/`, and the portfolio view is regenerated from
those. Two tasks advancing at the same time now write to two different directories.

### New Files — 28

| File | Description |
|------|------------|
| `.tfw/templates/status.md` | Task state carrier. YAML front matter, closed key set of 11, bounded fields, no free-text body. Every key has a named reader, and the template says which |
| `.tfw/templates/journal_event.md` | One event. Closed `kind` vocabulary, at most one summary, ceiling 120 code points with the measurement recorded in the template itself |
| `.tfw/templates/team_profile.md` | Participant profile, human or agent. Carries the four resolution cases and the binding location |
| `docs/scripts/gen_index.py` | Deterministic index generation, and the **shared task resolver** — `parse_identifier`, `sort_key`, `read_config`, `task_containers`, `iter_task_dirs`, `read_status`, `read_snapshot` — imported by the other two scripts |
| `docs/scripts/test_gen_index.py` | 28 tests: resolver, discovery, bounds, determinism, degraded states |
| `docs/scripts/migrate_board.py` | Accounting migration. Dry run by default; `--apply` writes only files that do not exist |
| `docs/scripts/test_migrate_board.py` | 30 tests, weighted toward the negative guarantees — nothing renamed, nothing byte-changed, nothing invented, nothing dropped |
| `tasks/README.md` | Why a second container exists, with the measured reason for not renaming |
| `tasks/BOARD-SNAPSHOT.md` | All 61 board rows, verbatim, captured before removal |
| `team/README.md`, `team/saubakirov.md` | The participant model and the first profile |
| `workspace/00-INDEX.md` | The generated portfolio view |
| 11 × `{task}/status.md` | Live state for the 11 non-terminal legacy tasks, written in place |
| `team/claude-code.md` | The agent principal that executed this phase — required by AC-4 once its handle appears as a journal actor |
| 5 × `tasks/TFW-60…/journal/*.md` | This phase's own coordination events, from real commit timestamps: the budget escalation, the TS approval, the handoff, execution opening on the census, and the handoff to review |

### Modified Files — 44

| Group | Files | Changes |
|------|---|---------|
| Canonical rules | `.tfw/conventions.md`, `glossary.md`, `README.md`, `compilable_contract.md` | §4 rewritten as **Task Identity and Location**: container list, clock identifier, collision rule, task control files, discovery. §2 drops the board and adds three templates. §5 replaces the board row format. §13 and §14 restated. Glossary gains `status.md`, `journal/`, Portfolio index, `team/`, `UNDECLARED`, and the status legend moved from the README |
| Configuration | `.tfw/project_config.yaml`, `.tfw/templates/project_config.yaml` | `task_containers`, `id_format`, `id_max_retries`, `legacy_id_format`, `journal.max_summary_length`; real `build.*` commands; version `2.0.0` |
| Lifecycle workflows | `handoff.md`, `init.md`, `plan.md`, `release.md`, `research/base.md`, `resume.md`, `review.md` | Read and write task state instead of the board; create tasks in the configured container from the clock |
| Templates | 13 files | `{PREFIX}-{N}` → `{ID}`, so both grammars read everywhere. `REVIEW.md` and `RELEASE.md` checklists point at task state |
| Adapter originals | `AGENTS.md.template`, `adapters/codex/README.md`, 7 × `SKILL.md` | Same rules at the adapter source |
| Documentation generator | `gen_docs.py`, `test_integration.py` | Board parser removed; containers read from configuration; three new tests guard the removal |
| Release surface | `.tfw/VERSION`, `.tfw/CHANGELOG.md`, `.tfw/quickstart.md`, `README.md` | `2.0.0` with migration guidance; board replaced by a permanent route plus four prose corrections |
| Root entry points | `AGENTS.md`, `CLAUDE.md`, `RELEASE.md` | Context-loading step 5 and the release checklist |

### Final census against the ruling

| | Configured | Ruled (S42 / S44) | **Delivered** | Δ vs ruling |
|---|---:|---:|---:|---:|
| Modified files | 30 | 45 | **44** | −1 |
| New files | 15 | 23 | **28** | **+5** |
| Files total | 30 | 68 | **72** | **+4** |
| LOC | 3000 | — | **2,641 added · 272 removed** | under |

Measured `git diff 80d6a16 HEAD`, excluding byte-identical adapter copies (S32) and work
artifacts (S46).

**The +5 is TFW-60's own `journal/`, and it needs stating rather than burying.** The TS's
create list did not include it. The phase ships a journal as a named deliverable and its own
task did not use one — a model unused on the task that introduces it is a gap a reviewer should
not have to find. Under S44 the response to needing more is to deliver properly and say so, not
to trim to hit a number.

**The DoF tripwire did not fire.** It reads: *"the census exceeding roughly 75 files total, or a
new group appearing, without returning to the coordinator."* The total is **72**, and `journal/`
is a Phase A deliverable named in the TS scope, the HL and AC-3 — not a new group. Had either
condition held, this would have gone back to the coordinator instead of into the RF.

The 28 also includes `team/claude-code.md`, which AC-4 forces: this session wrote `actor:
claude-code` into real journal events, and AC-4 requires an automated principal to carry its own
profile rather than borrow a person's. Shipping the events without the profile would have left
the tree violating a rule it ships.

**Three corrections to TS §4, as it asked for:**

| §4 said | Reality | Effect |
|---|---|---|
| `.tfw/workflows/update.md` modified | It carries no board reference, no container path and no identifier token. **Untouched** | −1 |
| 8 × `skills/tfw-*/SKILL.md` | Only **7** of the 11 skills mention the board | −1 |
| `.tfw/quickstart.md` not listed | Modified — AC-10 requires Quick Start to describe the shipped model | +1 |

None is a new group, so the TS §7 return-to-coordinator condition did not fire.

## 2. Key Decisions

1. **The state carrier is YAML front matter with a closed key set and no free-text body.** A
   `.md` file so it renders and so a person can open it, front matter so a parser has no
   ambiguity. The template lists every key's reader; a field nothing reads is rejected at review
   rather than argued about. There is deliberately no place to write a paragraph — TS §8 names
   "the state carrier drifts back toward prose" as a risk, and the cheapest control is to leave
   no field that invites it.

2. **The journal entry ceiling is 120 code points, chosen from a measurement, not from taste.**
   Two populations measured separately because they are different genres: 272 commit summaries
   (median 38) and 63 review verdicts (median 9). Combined p99 is 110. 120 clears p99 for both
   with headroom and refuses 3 of 335 real entries — and all three are shown in the evidence, so
   the number is judged against its consequence. All three are multi-fact summaries that belong
   in an artifact.

3. **`UNDECLARED` was added rather than normalizing two real values.** `🟡 TS` and `❄️ FROZEN`
   are outside the vocabulary. Mapping `TS` to `TS_DRAFT` would have looked tidier and would have
   rewritten a recorded fact. Both are carried verbatim in `lifecycle_verbatim` and flagged.
   `UNDECLARED` is documented as never selectable by a person.

4. **A struck-through board row gets no `status.md`.** TFW-30's row says "absorbed into
   TFW-45/C" and its directory exists. Writing state for it would have made retired work look
   actionable and produced 12 files where the TS says 11. It stays an unresolved input, visible
   in both the index and the snapshot with a stable diagnostic. This is the AC-6 requirement
   "unresolved entries stay discoverable and **non-actionable**" taken literally.

5. **The collision check is on the identifier, not the directory name.** The identifier is the
   timestamp alone; the directory is `identifier__slug`. Testing `{identifier}__{slug}` passes on
   a real collision and issues a duplicate. **My first fixture made exactly this mistake and
   failed**, which is why the rule in `conventions.md` §4 now states the operational form —
   glob `{identifier}__*` — instead of only the principle.

6. **Freshness is derived from the newest task `updated`, never from the wall clock.** A
   generation timestamp would make two runs a minute apart differ and quietly break AC-5's
   byte-identity requirement. The input-derived value is also the more honest measure of how
   current the view is.

7. **The container list is one key taking an ordered list**, per ONB Q9. Created in the first,
   resolved across all. Migration guidance presents it as one setting with one or two values,
   never as two supported layouts (S39).

8. **The shared resolver lives in `gen_index.py` and is imported**, rather than in a fourth
   module. It keeps the new-file count at the ruled 23 and, more to the point, gives every
   consumer one implementation. Per-call-site pattern matching is how the old board parser drifted
   into TD-81.

9. **`test_integration.py` line 159 was rewritten into three tests, not deleted.** After the board
   is gone the original assertion passes vacuously. The replacements fail if a board-shaped regex
   returns, if the tasks index reads the README again, or if a live task table reappears.

10. **The migration writes new files only and aborts on any existing target.** No legacy artifact
    is opened in write mode at all — not even to rewrite it unchanged, because a checkout with
    `autocrlf` set would rewrite line endings on the way out (ONB risk 5).

## 3. Acceptance Criteria

**AC-1 — Tasks live in a configured container, nested by creation year, on stable paths**
- [x] `project_config.yaml` carries `task_containers` with a documented default; every workflow reads it
- [x] No workflow writes a hardcoded `tasks/` path — `gen_docs.py` expands one glob per configured container
- [x] No lifecycle transition and no terminal state moves a directory — path set identical across `TODO → ONB → BLOCKED → RF → DONE → REJECTED`
- [x] The year is never recomputed — a December task updated the following March stays in 2026
- [x] Two container values over one tree resolve differently

**AC-2 — Task identifiers need no project-wide read**
- [x] Identifier is `YYYYMMDD-HHMMSS`; the directory is `<identifier>__<slug>`, and the collision rule is stated at identifier level
- [x] Creation reads no other task directory and no counter
- [x] Two participants with no shared state cannot produce the same identifier
- [x] A same-second collision is detected and resolved by a new actual timestamp, never reuse or overwrite
- [x] The retry is bounded by `id_max_retries` and fails visibly — verified against a clock that never advances
- [x] Both grammars readable by every consumer, through one resolver

**AC-3 — The journal is one immutable file per event, with a measured ceiling**
- [x] One file per event, named from the clock; the filename is the identifier
- [x] A written event is never rewritten; a correction is a new event — original bytes verified unchanged
- [x] Closed vocabulary, with `consolidation` reserved
- [x] Every event carries time, kind, actor, state change, ≥1 reference, ≤1 bounded summary
- [x] **Finite ceiling of 120 code points, justified by a recorded measurement** — the 240 fixture value was given no standing
- [x] Over-ceiling content is refused with the artifact route named
- [x] No event body copies artifact or chat text — the template states it and the field set gives no room
- [x] Two concurrent appends produce two files and no contended write

**AC-4 — Participants are declared in `team/`, and a session knows who is acting**
- [x] One file per participant: stable handle, display name, explicit `human`/`agent` type
- [x] An automated principal has its own profile and borrows no person's identity
- [x] A single profile is used without asking
- [x] Several profiles resolve through a binding on the participant's own machine only
- [x] No binding, shared device, copied binding or stale profile → exactly one short question before the first durable write
- [x] Identity never inferred from OS username, hostname, folder name or account string
- [x] The shared tree contains no current-user file and no private preferences
- [x] Documented as declared attribution, never authentication
- [ ] **Readability by a non-specialist — DESIGN INTENT ONLY, NOT OBSERVED.** No such participant appears in a transport-independent fixture. The observation is TFW-61's under S43, and NS3 forbids the untested claim

**AC-5 — The index is generated, declared derived, and never authoritative**
- [x] Deterministic — same input, same bytes, verified twice on the real corpus and in fixtures
- [x] Carries identity, goal, value, lifecycle, owner, terminal outcome, link to authority
- [x] Declares that it is derived, its source count and its freshness
- [x] Reports every legacy, malformed and unresolved input instead of dropping it
- [x] Explicit sort by a declared key; newest year last, newest task last within it
- [x] The `00-` prefix is documented as a hint, not a promise (ONB risk 4)
- [x] Absent, stale or malformed → discovery degrades, task state byte-identical in all four conditions
- [x] Every workflow acting on a task re-reads that task's state first — stated in `conventions.md` §4, `resume.md`, and as a §14 anti-pattern

**AC-6 — The legacy corpus is accounted for exactly and left byte-identical**
- [x] Dry run against a committed manifest before any project write
- [x] **61 rows + 53 directories = 114 occurrences → 61 identities: 53 matched, 8 board-only, 0 directory-only.** Zero unexplained
- [x] **Zero renames, zero moves, zero byte changes** — `git diff 80d6a16 HEAD -- tasks/` is 14 additions and nothing else
- [x] State created only for the 11 non-terminal tasks, from verified facts only
- [x] Nothing invented — `value: unrecorded`, `owner: unassigned` where the source was silent
- [x] Unresolved and malformed entries stay discoverable and non-actionable with a stable diagnostic
- [x] **All 61 rows captured verbatim** in `tasks/BOARD-SNAPSHOT.md`, including the 6 backlog rows and 3 struck-through absorptions
- [x] Out-of-vocabulary values carried verbatim, never normalized
- [x] The migration opens no legacy artifact in write mode; the diff gate ran against a clean baseline worktree

> **The TS's stated "52 of 60 rows match a strict regex" is corrected.** Measured: **52 of 61**
> match strictly, and **53** are matched in fact — the strict regex cannot see TFW-30, whose row
> is struck through over a real directory. Final counts: 53 matched · 8 board-only · 0
> directory-only · 9 rows a strict parser misses.

**AC-7 — Existing references and history keep resolving**
- [x] Every reference recorded in the census baseline still resolves — **the link-failure set shrank from 82 to 64**
- [x] 278 commit subjects checked against 53 directories; the only unresolvable identifier is **TFW-37**, which never had a directory and was already unresolvable at baseline
- [x] Counts read as relations against the baseline, not fixed totals (ONB Q6)
- [x] No relative link broke; new and legacy tasks are at the same depth below the root
- [x] `tasks/README.md` explains why a second container exists

**AC-8 — The board is gone and nothing still reads it**
- [x] Root `README.md` carries a permanent route and no live task table
- [x] No workflow, template, adapter original or script parses a task table
- [x] The generator no longer regex-reads board columns, **and a test fails on reintroduction** — it fired during this phase and caught a real leftover
- [x] `test_integration.py` line 159 rewritten, not deleted
- [x] `resume` and `release` read task state
- [x] The sweep over `.tfw/`, `docs/`, `README.md`, `AGENTS.md`, `CLAUDE.md`, `RELEASE.md` returns only historical mentions; the docs generator builds with the board absent

**AC-9 — No component is required to read or advance a task**
- [x] Creating a task, writing state and appending an event are ordinary file writes — a full lifecycle driven with no engine and no mutation interface
- [x] Executable code is exactly `gen_docs.py`, `gen_index.py`, `migrate_board.py`
- [x] With no index present, the task stayed readable and reached `DONE`; discovery reported itself stale rather than blocking
- [x] Nothing requires a daemon, database, lock server, vendor API or MCP host

**AC-10 — The release describes what shipped**
- [x] `.tfw/VERSION` is `2.0.0`; `tfw.version` matches
- [x] CHANGELOG states the breaking change and the migration path
- [x] Migration guidance presents the container as one configuration value (S39)
- [x] Quick Start, canonical rules, glossary, templates and adapter originals carry no residue of the board, a state engine or an identity subsystem
- [x] TD-81 and TD-177 retired by the code change and the reintroduction test. **The `TECH_DEBT.md` registry edit is not the executor's** under D37 — handed to `/tfw-docs` in §6

**Result: 62 of 63 criteria met. The one open item is AC-4's non-specialist readability, which the
TS itself requires be stated as intent and not claimed as observed.**

## 4. Verification

- **Tests** (`python -m pytest docs/scripts/`): **129 passed, 1 skipped** — baseline was 68 passed.
  61 tests added. The skip is `test_repository_accounting_balances`, which skips by design once
  the board is gone.
- **Verify** (`python docs/scripts/gen_index.py --check`): `index up to date`.
- **Lint** (`python -m pytest docs/scripts/ -q --collect-only`): 130 tests collect; no import or
  syntax error.
- **Docs build**: the MkDocs build runs inside `test_integration.py` and passes with the board absent.
- **Link check**: baseline 82 broken relative links → 64. The failure set shrank by 18.
- **Corpus integrity**: `git diff --name-status 80d6a16 HEAD -- tasks/` → 14 × `A`, zero `M`/`R`/`D`.

The three placeholder `build.*` values in `project_config.yaml` were replaced with these real
commands (ONB Q10), so the next executor's build gate verifies something.

**Build gate ran before this RF was written, and passed.**

## 5. Evidence

See [EV file](evidence/EV__phase-a__task_state_and_coordination.md) for evidence details.

Evidence verdict: **43/44 VERIFIED, 1 DEFERRED, 0 BLOCKED, 0 N/A.**

**Every AC in the TS carries `Evidence: N/A`, and that is not coverage.** Amendment A3 moved every
real-environment transport claim to TFW-61 and S43 moved the non-technical-participant observation
there. Two things are therefore **not claimed anywhere in this phase**:

1. **No transport behaviour was verified.** No provider, no client, no second machine. The
   concurrency evidence is two processes on one machine.
2. **No non-specialist read these carriers.** Readability is design intent, asserted as intent and
   nothing more.

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `KNOWLEDGE.md` | D66 | `todo` | States the README is *"the only Task Board"*. False as of `2.0.0`. **`/tfw-docs` handoff** — D37 gives this file another owner (ONB Q3) |
| 2 | `KNOWLEDGE.md` | D65 | `todo` | Records `❌ REJECTED` as living in **five** carriers, one being "the README legend". The legend moved to `glossary.md` § Status Flow, so the count is now four. **`/tfw-docs` handoff** (ONB Q11) |
| 3 | `knowledge/convention.md` | F22 | `todo` | A ✅ verified fact about root Task Board updates being a process artifact. The subject no longer exists. **`/tfw-knowledge` handoff** |
| 4 | `TECH_DEBT.md` | TD-81, TD-177 | `todo` | Both retired by this phase's code change and its reintroduction test. The registry rows still read open. **`/tfw-docs` handoff** — AC-10 assigns the closure there, not here (ONB Q3) |
| 5 | `editions/02-assisted/AGENTS.md` | 71 | `security` | Defines `work/new`, `work/doing`, `work/review`, `work/done`, `work/blocked` and states that **status changes by moving the whole folder** — precisely what master HL P4 and DoF 3 prohibit. A shipped TFW edition instructs the anti-pattern. Not edited: that copy is v1.0 against a shipped v1.4, so editing a stale copy buys nothing (ONB Q4). **Debt candidate against the edition** |
| 6 | `tasks/TFW-36__content_marketing_blog_series/` | `.gitignore` | `todo` | The folder carries a `.gitignore` containing `*`, and the `.gitignore` is itself untracked. **The entire task is invisible to Git** — no HL, no artifacts, no `status.md`. Pre-existing, not created here. Consequences: the index is reproducible from a working tree but not from a fresh clone, and under Git-mode collaboration that task's state reaches nobody. Someone should decide whether that was intended |
| 7 | `README.md` | 251+ | `todo` | The board section is replaced by a route. Four prose statements elsewhere in the file also described the board as live (lines 140, 157, 203, 242) and were corrected. Line 140 sits inside § How It Works, a **North Star locus** — the wording changed from "reads the Task Board" to "reads the task's own state file", which tracks the mechanism without altering what the clause commits to. Flagged so a reviewer rules on it rather than discovering it |
| 8 | `tasks/TFW-45__multi_agent_workflows/status.md` | `lifecycle` | `todo` | `❄️ FROZEN` is carried as `UNDECLARED` + verbatim, per ONB Q12. Whether `FROZEN` should join the declared vocabulary is a real open question and a separate owner ruling — filed here for triage, as the owner directed |
| 9 | `tasks/TFW-4__framework_cleanup/status.md` | `lifecycle` | `todo` | `🟡 TS` is the pre-rename label of `TS_DRAFT` (renamed in TFW-15) and is outside today's vocabulary, so it is `UNDECLARED` + verbatim. Someone with the history can set it to `TS_DRAFT` deliberately; a migration script may not |
| 10 | `docs/scripts/gen_docs.py` | 105, 681 | `duplication` | `_glob_sources(root)` is called twice and re-reads `project_config.yaml` each time. Harmless at this scale; would matter if the config read grew expensive |
| 11 | — | — | `missing-test` | The 11 migrated `status.md` files carry `value: unrecorded` and `owner: unassigned` because the board never held those facts. They are honest placeholders, not data. Someone who knows those tasks should fill them; nothing in the framework will prompt for it |

### A process failure in this session, reported rather than buried

While staging the migration I ran `git add -A tasks/`, which swept **~90 uncommitted files
belonging to TFW-55's in-progress research** and one modification to `iterations.yaml` into a
Phase A commit. I detected it during the AC-6 corpus diff and backed it out in
`[claude-code/TFW-60/phase-a/executor] return TFW-55 work to its own author`: `git rm --cached`
for the untracked tree, and a restore of the baseline blob for the modified file, both leaving the
working tree untouched. TFW-54's uncommitted HL was swept the same way and removed the same way.

This is worth recording because it is the exact failure mode master HL DoF 6 names — broad staging
as the documented path — committed by the phase built to prevent it. Explicit task-owned staging
is a rule this session had to learn by breaking.

## 7. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | `stakeholder` | The owner approved a 2.3× scope-budget overrun with one condition — *quality must not suffer* — and it was recorded as a **direction, not a caveat**: the overrun exists so the scope ships whole, and hitting the number by delivering less inverts the ruling. Returning to the coordinator is the response to needing more, not trimming | ONB Q2, owner 2026-08-26 (S44) | High |
| 2 | `philosophy` | Trace integrity outranks tidiness, and the owner accepted a permanently split container rather than a rename that would have orphaned 7,505 references and 271 commit subjects. Stated as: a trace needing a translation table has already lost the property the framework exists to provide | ONB Q5/Q9 rulings; `tasks/README.md` | High |
| 3 | `process` | Artifacts recording the work sit outside the file budget entirely (S46), *specifically* so no budget argument can ever justify producing less evidence. The exclusion exists to remove an incentive, not to save counting | TS §4, S46 | High |
| 4 | `constraint` | An executor may not edit `KNOWLEDGE.md`, `knowledge/*` or `TECH_DEBT.md` even when an acceptance gate cannot pass without it. The gate narrows and the work is handed to the owning workflow; territory beats convenience | ONB Q3 ruling | High |
| 5 | `convention` | A numeric default with no recorded measurement is not acceptable in this project. The journal ceiling required a named population, a distribution, a stated percentile **and a demonstration of what the value refuses** | TS AC-3, ONB Q7 ruling | High |
| 6 | `risk` | `.user_preferences.md` is gitignored but **not sync-ignored**. Under file synchronization a per-user file reaches every participant — which is why the participant binding was placed outside the project tree entirely | ONB Q8 ruling | High |
| 7 | `process` | A fixed-count acceptance criterion over a corpus the phase itself edits is unsatisfiable by construction. The coordinator called this its own error and converted AC-6 and AC-7 into relations against a committed baseline | ONB Q6 ruling | High |

## 8. Strategic Insights (Execution)

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | The owner ruled that a shipped edition contradicting the master contract is **not fixed opportunistically by a passing phase**. `editions/02-assisted/` instructs status-by-folder-move, which P4 and DoF 3 forbid — and the ruling was to rename this phase's container away from the collision and record the contradiction as debt, because the copy is v1.0 against a shipped v1.4 and editing a stale artifact buys nothing. Implication: version skew between a shipped edition and the core is a first-class problem needing its own task, and Phase A must not be read as having addressed it | `philosophy` | User, ONB Q4 ruling 2026-08-26 |
| S2 | The coordinator answered a blocking question by **withdrawing an acceptance criterion** rather than defending it: the index's "pinned to the top of the container listing" was unachievable across file managers, and Windows Explorer — grouping directories before files — is the default case for the very reader the pin was meant to serve. Implication: an AC that cannot hold in the reader's real environment is removed, not weakened into a hope. The guaranteed entry point became the README route, and the `00-` prefix survives only as a hint | `process` | User, ONB risk 4 ruling 2026-08-26 |
| S3 | The order of work was made a **requirement**, not a suggestion, because this phase rewrites the rules the executing session obeys — `handoff.md`, `CLAUDE.md`, `conventions.md`. A session crossing a context boundary mid-phase re-reads the ONB, not the workflow it is rewriting. Implication: any future task that edits its own governing workflow inherits this hazard, and the mitigation is ordering plus an explicit instruction about which document is authoritative during the rewrite | `process` | User, ONB risk 1 ruling 2026-08-26 |
| S4 | The distinction the owner enforced between *verbatim* and *tidy* turned out to have teeth in three separate places — the snapshot, the status vocabulary, and the migrated state files. Each time, the tidier output was rejected. Implication: this project treats "the listing looks cleaner" as evidence that a fact is being rewritten, and a reviewer should read every normalization as a claim requiring justification | `philosophy` | User, ONB Q12 ruling 2026-08-26 |

## 9. Diagrams

**Where authority lives, before and after**

```text
BEFORE — one file, every writer

  Task A ─┐
  Task B ─┼──►  README.md § Task Board     live authority AND portfolio view
  Task C ─┘            ▲                   61 rows · schema drift (TD-177)
                       │                   regex-read by gen_docs.py (TD-81)
              permanent contention:
              three unrelated tasks, one byte range


AFTER — authority is local, the view is rebuilt

  README.md  ──── permanent route, low churn, never a lifecycle write
       │
       ▼
  workspace/00-INDEX.md      derived · non-authoritative · rebuildable · may be stale
       │                     declares source count + freshness + unresolved inputs
       │  select a task, then re-read ITS authority
       ▼
  workspace/<year>/<id>__<slug>/
    ├── status.md      ◄── the only authority. 11 keys, bounded, no prose body
    ├── journal/           one immutable file per event
    │     20260819-140312__created.md
    │     20260826-091500__handoff.md
    └── HL · RES · TS · ONB · RF · REVIEW · evidence/

  team/<handle>.md     who acted — humans and agents. Attribution, not authentication
  ~/.tfw/bindings.yaml which handle THIS machine is — outside the project, never synced

  tasks/               the pre-2.0.0 corpus. Frozen. Not one byte changed
    ├── README.md          why a second container exists
    └── BOARD-SNAPSHOT.md  all 61 rows, verbatim, the day the board died
```

**Why concurrent writes stop colliding**

```text
  two tasks advancing            two roles inside one task        two events at once
  ─────────────────────          ────────────────────────         ──────────────────
  A → workspace/…/A/status.md    coordinator → TS__…md            actor1 → …140000__handoff.md
  B → workspace/…/B/status.md    executor    → RF__…md            actor2 → …140000__dispatch.md

  different directories          different files, role-owned      different files, clock-named

  The identifier is the filename. Nobody allocates it, nothing counts, so there is no
  shared counter to contend for — and an append is a create, never an edit.
```

**Which reads are authoritative, and which are not**

| Reader | Reads | Authoritative? | If it is missing or stale |
|---|---|---|---|
| `resume`, `review`, `handoff`, `release` | the selected task's `status.md` | **yes** | the task cannot be advanced — this is the real state |
| a person browsing | `workspace/00-INDEX.md` | no | regenerate it; nothing was lost |
| `gen_docs.py` tasks index | every `status.md` via the shared resolver | no | the docs page shows a task without a lifecycle line |
| anyone, about pre-2.0.0 tasks | `tasks/BOARD-SNAPSHOT.md` | historical | it never changes, so it is never stale |

**The dependency direction among the three scripts**

```text
        gen_index.py ──────────────► the shared task resolver
         ▲          ▲                parse_identifier · sort_key · task_containers
         │          │                iter_task_dirs · read_status · read_snapshot
         │          │
  gen_docs.py   migrate_board.py

  One implementation, three consumers. Per-call-site pattern matching is how the
  previous board parser drifted out of sync with the board it parsed.
```

---

*RF — TFW-60 / Phase A: Task State & Coordination | 2026-08-26*
