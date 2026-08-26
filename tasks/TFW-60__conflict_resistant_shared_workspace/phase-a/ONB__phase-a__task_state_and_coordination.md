# ONB — TFW-60 / Phase A: Task State & Coordination

> **Date**: 2026-08-26
> **Author**: Claude Code (Executor)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-60](../HL-TFW-60__conflict_resistant_shared_workspace.md) · [HL — Phase A](HL__phase-a__task_state_and_coordination.md)
> **TS**: [TS — Phase A](TS__phase-a__task_state_and_coordination.md)
> **Master freeze**: `c1782b3` — verified present in history via `conventions.md` §3 rule 15 recovery form
> **Measurement date**: 2026-08-26, working tree at `e4d2757` plus uncommitted changes

---

## 1. Understanding

Phase A removes the root `README.md` Task Board — today the single file every lifecycle transition
writes — and replaces it with three separate things: a short bounded `status.md` inside each task
folder that is the only authority for that task's live state; a `journal/` of one immutable file per
coordination event, so two participants appending at once produce two files rather than a contended
byte range; and a deterministically generated, explicitly non-authoritative `00-INDEX.md` that
restores zero-command portfolio discovery. Tasks move to a configured container nested by immutable
creation year, with clock-derived identifiers that need no project-wide read (DoD 18 / amendment A1).
Participants are declared in `team/<handle>.md`. The existing `tasks/` corpus is accounted for exactly
and left byte-identical — nothing renamed, moved or invented — because thousands of references and
hundreds of commit subjects depend on those paths. The phase ships its whole release surface: canonical
rules, configuration, templates, adapter originals, the documentation generator, migration guidance and
a `2.0.0` version bump. Transport (Git vs file sync) is explicitly not here — amendment A3 moved it
to TFW-61.

## 2. Entry Points

| Area | Files |
|---|---|
| Canonical rules | `.tfw/conventions.md` §§2–5, `.tfw/glossary.md`, `.tfw/README.md` (NS1–NS3), `.tfw/compilable_contract.md` |
| Configuration | `.tfw/project_config.yaml`, `.tfw/templates/project_config.yaml` |
| Lifecycle workflows | `.tfw/workflows/{plan,handoff,review,resume,release,init,update}.md`, `research/base.md` |
| Templates | `.tfw/templates/*.md`, `.tfw/templates/evidence/EV.md`, `.tfw/templates/research/*.md` |
| Adapter originals | `.tfw/adapters/codex/AGENTS.md.template`, `.tfw/adapters/codex/README.md`, `.tfw/adapters/codex/skills/tfw-*/SKILL.md` |
| Generator | `docs/scripts/gen_docs.py` (board parser at line 324), `docs/scripts/test_integration.py` (line 159), `docs/scripts/test_gen_docs.py` |
| Board itself | `README.md` lines 251–315 (header + separator + 61 data rows) |
| Legacy corpus | `tasks/` — 53 task directories |
| Prior art in-repo | `editions/02-assisted/` — already ships a `work/` container and a `people/` profile model |

---

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | **Neither artifact is approved.** The Phase A HL header reads `📝 HL_DRAFT — awaiting owner review`, the TS header reads `🟡 TS_DRAFT — Awaiting approval`, and the board row reads `🟡 TS_DRAFT (A) — owner approval required`. `handoff.md` takes an **approved** HL + TS as input. Is the owner's approval given, and should both headers and the board row be updated to record it before execution starts? | _{coordinator/owner fills in}_ |
| 2 | **The TS's own return-to-coordinator tripwire has fired.** TS §7 DoF item 10: *"The census exceeding roughly 75 files total, **or a new group appearing**, without returning to the coordinator."* Measurement finds 8 modified originals that carry board or container semantics and are absent from §4, in groups §4 does not have: project-root governance (`AGENTS.md`, `CLAUDE.md`, `RELEASE.md`), shipped editions (`editions/02-assisted/AGENTS.md`, `editions/02-assisted/MIGRATION.md`), and knowledge/debt registries (`KNOWLEDGE.md`, `knowledge/convention.md`, `TECH_DEBT.md`). Corrected upper bound: **50 modified · 23 new · 73 total** against the ruled 42 / 23 / 65. Does the owner extend the S42 overrun ruling to these counts, or does the phase split? Full evidence in §6 item 1. | _{coordinator/owner fills in}_ |
| 3 | **Which of those 8 files are the executor's, and which belong to `/tfw-docs` and `/tfw-knowledge`?** `KNOWLEDGE.md` D66 states README is *"the only Task Board"*; `knowledge/convention.md` F22 is a ✅ verified fact about board updates; `TECH_DEBT.md` holds TD-81 and TD-177. All three are downstream-workflow territory, but AC-8's gate — *"`git grep -i "task board"` over originals returns only historical mentions in CHANGELOG and closed task traces"* — cannot pass while they carry live board statements. Options: **(a)** executor edits all three and AC-8 passes as written; **(b)** executor leaves them, AC-8's gate is narrowed to `.tfw/`, `docs/` and `README.md`, and the three are handed to `/tfw-docs` + `/tfw-knowledge` after REVIEW; **(c)** executor edits `TECH_DEBT.md` only, since TD closure is named in AC-10, and defers the two knowledge files. | _{coordinator fills in}_ |
| 4 | **`work/` already means something else in this repository.** `editions/02-assisted/AGENTS.md` line 71 defines `work/new`, `work/doing`, `work/review`, `work/done`, `work/blocked` and states that status changes **by moving the whole folder** between them. TS §6 selects `work/` as this repository's container, and master HL P4 / DoF 3 prohibit exactly that move. Shipping both means TFW distributes two contradictory meanings for one directory name. Options: **(a)** choose a different container name here (`workspace/`, `w/`); **(b)** bring the Assisted edition into Phase A scope and align it (+2 files, already counted in Q2); **(c)** keep both and record the divergence in `tasks/README.md` and the CHANGELOG as a known edition difference. | _{coordinator fills in}_ |
| 5 | **Six backlog tasks have no home after the board is removed.** `LEGACY-INDEX.md` is specified as *"a frozen snapshot of the 41 terminal legacy tasks"*, and `status.md` is written for the *11 non-terminal* tasks — both counts derived from linked rows only. TFW-16, TFW-20, TFW-33, TFW-34, TFW-35 and TFW-39 are `⬜ TODO` rows with **no task directory**: they are neither terminal nor holders of a `status.md`, so they land nowhere and the project's backlog is deleted. That is a DoF hit (*"Any board row or directory unaccounted for"*). Options: **(a)** `LEGACY-INDEX.md` captures all 61 rows, terminal and not; **(b)** create the 6 directories with a `status.md` each, taking the new-file count to 29; **(c)** a separate `BACKLOG.md`. | _{coordinator fills in}_ |
| 6 | **Every census number in AC-6 and AC-7 is stale, and two are wrong in kind, not just in size.** Measured today vs stated: 61 board data rows (stated 60) · 53 task directories (51) · 7,462 `TFW-N` occurrences across 665 files (7,051 / 653) · 265 commit subjects naming a task (249) · **1 directory-only entry, TFW-30** (stated 0). Worse, these keep moving while the phase runs — writing this ONB raised the reference count again. A fixed-count acceptance criterion is unsatisfiable by construction. Proposal: re-measure at execution start, record the baseline in `evidence/census.md`, and read AC-7 as its own gate already words it — *"the failure set must not grow"* — rather than as fixed totals. Confirm? | _{coordinator fills in}_ |
| 7 | **What is the measurement population behind the journal entry ceiling (AC-3)?** The AC requires *"the configured value is justified by a recorded measurement"* and explicitly denies the 240-code-point fixture any privileged status, but names nothing to measure. Without a defined population the requirement cannot fail, which defeats it. Proposal: measure the 265 real commit subjects in this repository plus the state-change summaries in existing REVIEW verdicts, report the distribution, and set the ceiling at a stated percentile. Confirm, or name a different population. | _{coordinator fills in}_ |
| 8 | **Where does the private profile binding live (AC-4)?** The AC requires *"a binding stored **only** on the participant's own machine"* and forbids a shared current-user file, but the machine-local TFW home from S28 was removed with the identity subsystem in research iteration 3, so no location survives in the frozen contract. The executor must not invent an architectural location. Options: **(a)** `~/.tfw/bindings.yaml` keyed by absolute project path; **(b)** an existing gitignored project-local file — `.user_preferences.md` already carries per-user state and is gitignored, though constraint F1 forbids copying its content into shared files; **(c)** an environment variable, no file at all. | _{coordinator fills in}_ |
| 9 | **Do legacy tasks stay reachable by workflows, and through what key?** AC-1 requires *"no workflow writes a hardcoded `tasks/` path"*, but the 11 non-terminal legacy tasks stay under `tasks/` and receive a `status.md` — so `resume`, `review` and `handoff` must still resolve `tasks/` to act on TFW-55, TFW-60 and the rest. Options: **(a)** a second configured key, e.g. `legacy_container`, read alongside the primary; **(b)** the container key accepts an ordered list and workflows search each in turn; **(c)** legacy paths resolve only through `LEGACY-INDEX.md`, and workflows never construct a legacy path themselves. | _{coordinator fills in}_ |
| 10 | **What is the build gate?** `handoff.md` step 10 requires running the build command from the TS verification section; the TS has no verification section, and `project_config.yaml` sets `build.lint`, `build.test` and `build.verify` to placeholder `echo` strings. Python 3.13.5 and pytest 9.0.2 are present. Proposal: the gate is `python -m pytest docs/scripts/` — the only executable tests in the repository — plus a corpus-wide relative-link check, and Phase A also replaces the three placeholder `build.*` values with those real commands. Confirm — and confirm that editing `build.*` is in scope, since it is not named in §4. | _{coordinator fills in}_ |
| 11 | **Does the README status legend stay?** `KNOWLEDGE.md` D65 records `❌ REJECTED` as living in exactly **five** carriers, one of which is *"the README legend"* — the legend that sits with the Task Board. Removing the board without a decision either silently drops a carrier D65 counts, or leaves a status legend in a README that no longer shows statuses. Options: **(a)** the legend stays in README beside the route; **(b)** it moves into the generated index header; **(c)** it moves to `glossary.md` `## Status Flow`, which already holds one, and D65's count becomes four. | _{coordinator fills in}_ |
| 12 | **Is `❄️ FROZEN` a real status?** TFW-45's board row carries `❄️ FROZEN`, which appears in neither `conventions.md` §5 nor the `tfw.statuses` list in `project_config.yaml`. AC-6 forbids inventing a fact and forbids silently normalizing a malformed input. Options: **(a)** admit `FROZEN` to the status vocabulary, costing one status in two config files and the conventions table; **(b)** migrate it as `❌ BLOCKED`, which changes a recorded fact and needs an owner ruling; **(c)** carry it into `status.md` verbatim and flag it as a stable diagnostic for a non-vocabulary value. | _{coordinator fills in}_ |

---

## 4. Recommendations (suggestions, not blocking)

1. **Write the corrected census before touching any file, and commit it as its own artifact.** DoF 12 makes the owner's overrun ruling valid only against exact counts, and the counts in §4 are already stale. Producing `evidence/census.md` first turns the ruling in Q2 into a decision on real numbers rather than a second estimate.

2. **Do the migration accounting as a dry run against a manifest, and land the manifest before the writes.** AC-6 requires the isolated-copy run anyway; making the manifest a committed artifact means the reviewer can reconcile 61 rows and 53 directories independently instead of trusting the RF's totals.

3. **Sequence the work so the framework the session runs inside changes last.** This phase rewrites `handoff.md`, `CLAUDE.md` and `conventions.md` — the files governing the session performing the rewrite. Suggested order: templates and new carriers → generator and migration scripts → migration run → canonical rules → workflows → adapter originals → root entry points → release surface. That keeps the executing session on stable rules until the final block.

4. **Write one resolver, wire it everywhere, and give it its own test.** TS §6 already says this. Concretely: a single function accepting both `YYYYMMDD-HHMMSS__slug` and `{prefix}-{seq}`, used by `gen_index.py`, `migrate_board.py` and `gen_docs.py`, with the 61 real rows as fixtures. Per-call-site pattern matching is how the current board parser became TD-81.

5. **Close TD-81 and TD-177 with a test that fails on reintroduction, not only with a registry edit.** AC-10 names both as retired in this release. A test asserting that no board-shaped regex remains in `docs/scripts/` is what keeps them retired.

6. **Keep the `📚 KNW` handoff explicit in the RF.** Whatever Q3 decides, RF §6 Observations should name the exact `KNOWLEDGE.md` and `knowledge/` items left contradicting the shipped model, so the coordinator's `/tfw-docs` pass gets a list rather than a search.

---

## 5. Risks Found (edge cases, potential issues not in TS)

1. **The phase edits the rules the executing session obeys.** `CLAUDE.md` step 5 of context loading and `AGENTS.md` step 5 both name the board; `handoff.md` is itself rewritten. A session that reloads context mid-phase gets a different contract than the one it started under. Recommendation 3 mitigates the ordering; it does not remove the hazard, and a session resumed after a context boundary must re-read this ONB rather than the workflow it is rewriting.

2. **The index generator is deterministic only if its inputs are ordered deterministically.** AC-5 requires byte-identical output from identical input, but directory iteration order is filesystem-dependent, and this repository lives on Windows (NTFS) while the docs generator may run in CI on Linux. Sorting must be explicit and by a declared key, never inherited from `os.listdir` or glob order.

3. **A clock-derived identifier is collision-free only if the clock is trustworthy.** AC-2 requires a same-second collision be resolved *"by taking a new actual timestamp, never by reuse or overwrite"*. If the wall clock steps backwards — an NTP correction, a machine returning from sleep, a restored VM — the new timestamp can collide with an already-used one and the retry loop does not terminate. A bounded retry with a visible failure is needed, and the TS does not say so.

4. **`00-INDEX.md` pins to the top of a listing only under some sort orders.** AC-5 requires the index *"pinned to the top of the container listing"* via the `00-` prefix. That holds under ASCII sort; it does not hold in file managers that group directories before files, which is the default in Windows Explorer and most graphical browsers — the year folders will sit above the index for exactly the non-technical reader the pin exists to serve.

5. **Byte-identical preservation is not the same as leaving the corpus untouched.** AC-6 forbids byte changes to *existing task artifacts*, and the 11 new `status.md` files are additions rather than modifications, so that part is clean. But a Windows checkout with `core.autocrlf` set can rewrite line endings on any file the migration script opens for writing, even when the content is unchanged. The script must never open a legacy artifact in write mode, and AC-6's diff gate should run on a fresh checkout to catch it if it does.

6. **Two participants creating tasks in the same second is not the only collision case.** Two creating tasks in the same second *with the same slug* produce the same directory name; different slugs produce different directories that both claim the same identifier prefix. AC-2's collision text addresses the directory, not the identifier. Whether an identifier is `YYYYMMDD-HHMMSS` or `YYYYMMDD-HHMMSS__slug` decides which of the two is unique, and the TS uses both forms — the bare grammar in AC-2 bullet 1, the directory form in AC-1.

7. **Removing the board removes the cold-start discovery path S15 credits with proven value, for at least one commit.** The board and the index cannot both be authoritative, so there is a window where the board is gone and the index is not yet generated. If the phase is interrupted there, the project has no portfolio view at all. The migration should generate the index before the board is deleted, and the RF should state which commit closed the window.

8. **`docs/scripts/test_integration.py` line 159 asserts the index page does *not* contain the board.** That test passes today because the board exists and is excluded. After removal it may pass vacuously — a green test that no longer tests anything. It needs rewriting rather than deleting, and §4 counts it as modified without saying which way.

---

## 6. Inconsistencies with Code (spec vs reality)

**1. TS §4 census omits 8 modified originals, in groups §4 does not contain.**

Measured with `git grep -il "task board"` over the tree excluding `tasks/`, `.claude/`, `.agent/` and `.agents/` — 34 files hit, of which 26 fall inside §4's groups and 8 do not:

| File | Live board statement found | §4 group |
|---|---|---|
| `AGENTS.md` | line 11 `5. Project task board (README.md)`; line 60 *"the `README.md` Task Board"* | none — root entry point |
| `CLAUDE.md` | line 14 `5. Project Task Board (README.md) — status of all tasks` | none — root entry point |
| `RELEASE.md` | line 37 *"task board updates"*; line 42 checklist *"Task Board is current"*; line 52 *"Review Task Board"* | none — root release strategy |
| `editions/02-assisted/AGENTS.md` | line 71 forbids a shared task board **and** defines `work/` status-by-move | none — shipped edition |
| `editions/02-assisted/MIGRATION.md` | line 20 *"не новым общим task board"* | none — shipped edition |
| `KNOWLEDGE.md` | Public Entry row *"sole Task Board"*; D3, D4, D5; D66 *"the only Task Board"* | none — knowledge registry |
| `knowledge/convention.md` | F22, ✅ verified: the board update is a process artifact | none — knowledge registry |
| `TECH_DEBT.md` | TD-81, TD-177 | none — debt registry |

Corrected upper bound: **50 modified · 23 new · 73 total files**, against the 42 / 23 / 65 the S42 ruling was given on. Under the ~75 ceiling, but three new groups. → Q2, Q3.

**2. TS §4 overcounts the workflow group.** `.tfw/workflows/update.md` contains neither a board reference nor a `tasks/` path; its only match is a pointer to the codex adapter README. It is listed among the 8 lifecycle workflows and appears to need no edit beyond the version string. `resume.md` likewise carries no board reference but does read `tasks/`, so it stays in scope for the container key. Per §4's own instruction, the RF reports both as corrections.

**3. TS §4 overcounts the template group.** 13 templates are listed for *"path and identifier examples; board references removed"*. Measured: **zero** templates contain `tasks/`, and only two contain "task board" — `RELEASE.md` and `REVIEW.md`. The other 11 carry `{PREFIX}-{N}` or `PROJ-N` identifier examples only, so their edit is the identifier grammar, not the board. The group is real, but its stated reason is wrong for 11 of the 13 files.

**4. The migration accounting in the Phase A HL is arithmetically superseded.** The HL states `60 board rows + 51 task directories = 111 → 60 identities · 51 matched · 9 board-only · 0 directory-only`. Measured today:

```
   61 board data rows          (header and separator excluded)
   53 task directories
  ───────────────────────────
  114 source occurrences  →  61 logical identities
                             53 matched
                              8 board-only, no directory
                              0 directory-only with no row of any kind
                              1 MALFORMED: TFW-30 has a directory and a
                                strike-through row `~~TFW-30~~ — absorbed
                                into TFW-45/C`, which no strict row regex matches
```

The stated *"0 directory-only"* is what the strict regex sees; the directory is real. TFW-30 is precisely the case AC-6 requires to stay visible and non-actionable, and the specification currently says it does not exist. → Q6.

**5. AC-6's "8 malformed rows" is 9.** The rows a strict `| [TFW-` regex misses: TFW-16, TFW-20, `~~TFW-28~~`, `~~TFW-30~~`, TFW-33, TFW-34, TFW-35, `~~TFW-37~~`, TFW-39. Nine, not eight. Six are live `⬜ TODO` backlog with no directory, three are struck-through absorptions, and one of those three (TFW-30) has a directory. → Q5, Q6.

**6. AC-7's fixed reference counts are already false and keep moving.** Stated: *"all 7,051 `TFW-N` references across 653 files"* and *"all 249 commit subjects"*. Measured: **7,462 occurrences across 665 files**, and **265 commit subjects** mentioning a task ID — 180 of them under the strict `[agent/task/scope/role]` attribution grammar, so even the stated 249 does not correspond to either measurable definition. → Q6.

**7. The 41 / 11 terminal split holds, and is the only census figure that does.** Counting the 52 strictly-matching rows: 39 `✅ DONE`, two of which carry trailing prose, plus 2 `❌ REJECTED` = 41 terminal; and 4 `⬜ TODO` + 2 `📝 HL_DRAFT` + 1 `🟢 RF` + 1 `🟡 TS` + 1 `🟡 TS_DRAFT (A)` + 1 `📚 KNW (A)` + 1 `❄️ FROZEN` = 11 non-terminal. The `❄️ FROZEN` value belongs to no declared vocabulary. → Q12.

**8. `.tfw/README.md` carries an uncommitted modification.** `git diff` shows 4 added lines — a brand image block inserted after the H1. The file is a Project North Star locus (PV 0, NS1–NS3) and is listed in §4 as modified by this phase. The change is unrelated to TFW-60 and predates this session. It should be committed or reverted by its author before Phase A edits the same file, so the phase's diff is not mixed with it.

**9. No `team/` container exists, but `editions/02-assisted/people/README.md` does.** S31 records the `people/` → `team/` rename and S28 cites the Assisted profile model as its source. The Assisted edition is not in §4, so after Phase A the repository ships `team/` in the Full core and `people/` in the Assisted edition with no statement of their relationship. Q4 covers the container name; this is the same divergence for the profile model.

---

## 7. Knowledge Citations

Coordinator's citations in master HL §7.2 — all 29 items read. Grouped where the application is identical.

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|---|---|---|---|
| 1 | PV 0 — `README.md` opening and § How It Works | ✅ | Applied | Bounded resumability is what Q5 protects: deleting six backlog rows with no carrier makes the project less resumable, not more |
| 2 | PV 0 — `.tfw/README.md` NS1, NS2 principles 3 and 5 | ✅ | Applied | NS2.3 *Selected Trace* is the argument behind Q5 and §6 item 4 — a malformed row is trace, not noise |
| 3 | PV 1 — Methodology values, Structural Enforcement | ✅ | Applied | Recommendation 5: TD-81 and TD-177 close with a test that fails on reintroduction, not with a registry line |
| 4 | PV 1 — one authoritative owner per truth type | ✅ | Applied | Q3 is exactly this: `KNOWLEDGE.md` and `knowledge/` have owners who are not the executor, and AC-8's gate crosses that line |
| 5 | PV 1 — Portability, Success Criteria | ✅ | Applied | Risk 2 — deterministic index output must not inherit filesystem iteration order, or it is portable in name only |
| 6 | PV 2 — `knowledge/philosophy.md` F4, structural gates over procedural tables | ✅ | Applied | Supports the file-per-event journal design; no executor action beyond honouring it |
| 7 | PV 2 — F11, TFW Markdown is already the knowledge graph | ✅ | Applied | Q5 option (c), a separate `BACKLOG.md`, is the weakest of the three under F11 — it adds an entity where `LEGACY-INDEX.md` could absorb the rows |
| 8 | PV 2 — F27, observable file-by-file progress | ✅ | Applied | Recommendation 2: commit the migration manifest so the reviewer can reconcile independently |
| 9 | PV 2 — F34, a vague request leads through discovery to a usable result | ✅ | N/A | Planning-stage guidance; the request reaching the executor is not vague |
| 10 | PV 2 — F38, coordinator attention is finite | ✅ | Applied | Twelve blocking questions is a lot; each states its options so the answer is a selection rather than an investigation |
| 11 | PV 3 — D31, D50, filesystem state and locality | ✅ | Applied | The foundation of the whole phase; drives Recommendation 3's ordering |
| 12 | PV 3 — D37, exclusive knowledge write territories | ✅ | Applied | Q3 — this is the decision rule that makes `KNOWLEDGE.md` not the executor's file |
| 13 | PV 3 — D43, knowledge citation cascade | ✅ | Applied | This section; and Q3 option (b) keeps the cascade intact by routing to `/tfw-docs` |
| 14 | PV 3 — D55, D59, attribution and capability boundaries | ✅ | Applied | D59's *declared attribution ≠ authentication* is why Q8 asks for the binding location instead of inventing one |
| 15 | PV 3 — D65, reverting a result never reverts its trace | ✅ | Applied | Q11 — D65 counts the README legend as one of five carriers, and this phase deletes what surrounds it |
| 16 | PV 4 — `.tfw/conventions.md` §§3–5 | ✅ | Applied | Q12 — `❄️ FROZEN` belongs to no §5 vocabulary; §4 file naming governs this ONB's own filename |
| 17 | PV 4 — same §13 trace discipline, §14 whole-tree restore | ✅ | Applied | Risks 5 and 7 — the window where neither board nor index exists is a restore-shaped hazard |
| 18 | PV 5 — `knowledge/convention.md` F22 | ✅ | Applied | Q3 — F22 is itself one of the eight files carrying a live board statement |
| 19 | PV 6 — `knowledge/process.md` F7, F30 | ✅ | Applied | Risk 1 — cross-session context loss matters more than usual when the phase rewrites the context-loading instructions |
| 20 | PV 7 — `knowledge/risk.md` F1, shared Git index | ✅ | N/A | Transport and index isolation moved to TFW-61 by amendment A3 |
| 21 | PV 7 — `knowledge/constraint.md` F1, F3 | ✅ | Applied | F1 shapes Q8 option (b): `.user_preferences.md` is gitignored per-user state whose content may never reach a shared file |
| 22 | RES 1 — YAML 1.2.2 | ✅ | Applied | Bears on the `status.md` carrier format if it is YAML-fronted: closed key set, unique keys, fail-closed parsing |
| 23 | RES 1 — RFC 8259, duplicate object names | ✅ | N/A | The JSONL journal was removed; the journal is one Markdown file per event |
| 24 | RES 1 — Git, git-rev-parse, git-add | ✅ | N/A | Git topology moved to TFW-61 by A3 |
| 25–27 | RES 1 — Google Drive, OneDrive, Dropbox conflict behaviour | ✅ | N/A | Provider behaviour moved to TFW-61 by A3 |
| 28 | RES 1 — GSD, BMAD, Hermes, Spec Kit, OpenSpec | ✅ | N/A | Comparative research input, consumed at planning |
| 29 | RES 2 — git-interpret-trailers, git-log, git-merge-base | ✅ | N/A | The L3 landing protocol was superseded into TFW-61 by A3 |

**New items the executor found relevant, not in §7.2:**

| # | Source | Item | Why it belongs |
|---|---|---|---|
| N1 | `KNOWLEDGE.md` D66 | *"`README.md` is the complete practical English project guide and the **only** Task Board"* — approved, and its predecessor contract was superseded after owner rejection | The most direct verified contradiction of the phase's central deliverable. Any board removal has to state its relationship to D66, whose own history shows a README contract being rejected once already |
| N2 | `KNOWLEDGE.md` D3, D4, D5 | *"Replaced by RF files + Task Board"*, *"backlog in Task Board"*, *"RF + Task Board = project memory"* | Three decisions name the board as the replacement mechanism for artifacts that were removed. D4 is the origin of the six orphaned backlog rows in Q5 — the backlog was deliberately put there |
| N3 | `README.md` lines 140, 157, 203, 242 | Four prose statements outside the table describing the board as a live artifact and a resume mechanism | §4 counts `README.md` once, for *"board removed from root, permanent route left in its place"*. The edit is larger than deleting a table |
| N4 | `RELEASE.md` line 42 | Release checklist item *"Task Board is current"* | Phase A ships a `2.0.0` release under this very checklist, so the checklist stops being satisfiable during the phase that must use it |
| N5 | `editions/02-assisted/AGENTS.md` line 71 | Status changes by moving the whole folder between `work/*` subfolders | A shipped TFW edition instructs exactly what master HL P4 and DoF 3 prohibit, in the directory name TS §6 selects |

> **Cross-references**: use Reference Format (e.g. `RF TFW-18`, `D24`, `TD-72`). See compilable_contract.md §2.

---

*ONB — TFW-60 / Phase A: Task State & Coordination | 2026-08-26*
