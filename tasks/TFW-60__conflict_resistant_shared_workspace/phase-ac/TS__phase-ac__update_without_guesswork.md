# TS — TFW-60 / Phase AC: Update Without Guesswork

> **Date**: 2026-08-30
> **Author**: Claude Code (Coordinator), `on_behalf_of: saubakirov`
> **Status**: ✅ APPROVED — owner, 2026-08-30, at revision 1. Execution authorized via `/tfw-handoff`
> **Revision 2**: after onboarding, 2026-08-30. Two blocking questions answered, nine rulings on the
> executor's recommendations, risks and inconsistencies; changes carry `R2`. Census 23 → 26 counted.
> One question touched frozen text (the briefing's inputs); filed as amendment A7 and **approved by the
> owner the same day** — the briefing reads `Changed` as a fourth block.
> **Phase HL**: [HL Phase AC](HL__phase-ac__update_without_guesswork.md) — approved by owner 2026-08-30
> **Master freeze**: `56c3d70` — baseline after amendment A6
> **Origin**: [fourth](../FIELD-REPORT__TFW-60__fourth_external_update.md) and [fifth](../FIELD-REPORT__TFW-60__fifth_external_update.md) field reports, both on `v2.0.0-dirty.4`
> **Predecessor read through the Pre-TS Gate**: Phase AB RF revision 2 and REVIEW revision 2 (APPROVE, `4846f27`). AB delivered the whole-or-refuse dispatcher for **identifiers**, computed manifest guarantees, the current grammar, the test split and the source pin in `update.md`. It did not touch the status cell — `classify_status()` still takes the first `[A-Z_]+` token — and its pin is written from `HEAD`. Both are this phase's work, not AB's failure.

---

## 1. Objective

Remove every place where the update path guesses or decides for the owner. After this phase: the pin
is derived from the tag the operator names; the update asks who is acting, where tasks go and how the
project verifies before it writes anything, and ends by telling the owner what changed in their own
language; the migration refuses a status cell it cannot read whole and names every phase directory it
left without state; the payload copy cannot overwrite the receiver's own configuration; every
instruction in the path can be executed as written by a receiver on any earlier tag. A task's
abbreviation is the initials of a title a person can read.

## 2. Scope

**In scope:** `update.md` Steps −1, 0, 3, 5, 6, 7 and a new briefing step; the abbreviation rule in
`plan.md`, `init.md`, `conventions.md`, `glossary.md` and the HL template; the status-cell classifier
and phase reporting in `migrate_board.py`; the missing-phase-state report in `gen_index.py --check
tasks`; the CHANGELOG's reach across skipped tags, its retracted-wording quote and its dead references;
the `RELEASE.md` rules that make those permanent; the Claude rules markers; the Antigravity template;
the event, profile, status and project-config templates; the migration guide; tests for every behaviour
change.

**Out of scope:** the identifier grammar; `status.md` keys, the event schema, the lifecycle vocabulary,
the index format; renaming or rewriting any task directory, event or already-migrated `status.md`;
hand-authoring phase state for other tasks in this repository;
the four consumer projects; the `actor` field (TFW-54); transport mode (TFW-61); Phases B and C;
claiming `2.0.0`; the fifth report's §6 minor items — `since` semantics, `created` seconds provenance, a
README route template, a stale index in a non-first container, `--check project` before migration — to
be recorded in RF §6 Observations for the reviewer to file.

### Decisions the owner has already settled

| Decision | Ruling |
|---|---|
| Phase AC exists, after AB and before B; fourth-report defects 3–6, 8 and the filed debt are its scope | 2026-08-30, in chat; amendment A6 |
| Fifth-report items 6–8 and 10 stay in the phase | 2026-08-30, HL gate: approved as written |
| `2.0.0` is not ready; this phase ships as the next `2.0.0-dirty` tag | 2026-08-30, superseding 2026-08-29 |
| The abbreviation is the initials of the approved title, proposed with the title | 2026-08-30 |

## 3. Principles Check

| Principle (master HL §7) | Enforced by |
|---|---|
| P1 Pain before mechanism | AC-6, AC-7, AC-8 — each fixes a shape measured on a real project, reproduced as a fixture |
| P4 Stable paths over status moves | AC-8 — nothing is renamed; `UNDECLARED` is a value a person resolves with an event |
| P5 Local truth, derived views | AC-8 — the manifest and the gate name what they did not write instead of implying it |
| P9 No trace deletion during simplification | AC-2 — the CHANGELOG quotes retired wording; it never deletes the entry it retracts |
| P10 Every phase pays for its release surface | AC-11 — the next dirty tag with a consumer run, `2.0.0` unclaimed |

## 4. Affected Files

Byte-identical adapter copies are excluded from the count by S32; work artifacts by S46. The executor
measures this table at onboarding and reports the measured census in the RF.

| Group | Paths | Counted |
|---|---|---:|
| Update workflow | `.tfw/workflows/update.md` — Step −1 (new), Step 0 pin at :17–20 and :86–87, Step 3 gate at :64–72, Step 5 exclusions, Step 6 table at :99–107 and allowlist at :111–115, Step 7 at :119, Step 8a briefing (new) | 1 |
| Abbreviation rule | `.tfw/workflows/plan.md`:38–42, :55–68 · `.tfw/workflows/init.md`:113–114, :136–143 · `.tfw/conventions.md`:229–262 (Identifier), :369–398 (Artifact file naming) · `.tfw/glossary.md`:120 · `.tfw/templates/HL.md`:3–5 | 5 |
| Migration honesty | `.tfw/scripts/migrate_board.py` — `classify_status()`:162–181, `plan()`:865 terminal skip, `render_manifest()`:750–752 · `.tfw/scripts/gen_index.py` — `check_tasks()`:1186–1221, `read_phase_status()`:474 | 2 |
| Tests | `.tfw/scripts/test_migrate_board.py` · `.tfw/scripts/test_gen_index.py` · `docs/scripts/test_integration.py` (markers and exclusion list, if the executor places them there) | 3 |
| Release surface | `.tfw/CHANGELOG.md` — `.3` entry (TD-198), :297 (TD-191), :200–265 fence (TD-190), updating sections · `RELEASE.md` §5–6 | 2 |
| Adapters | `.tfw/adapters/claude-code/CLAUDE.md.template` (markers; block brought current) · `.tfw/adapters/claude-code/README.md` · `.tfw/adapters/antigravity/tfw-rules.md.template`:5–7 · `.agent/rules/tfw.md`:5–8 (TD-204) · **R2** `.tfw/adapters/cursor/tfw.mdc.template`:2, :6, :8 (same `{version}` defect) · **R2** `.tfw/adapters/codex/README.md`:104 (first-run sentence → pointer) | 6 |
| **R2** Marker rule, canon | `.tfw/conventions.md` §9 Tool Adapter Pattern — the one place the marker-bounded block rule is stated (already in the census for §4; no new path) | 0 |
| **R2** The framework as its own consumer | `CLAUDE.md` (this repository's root) — carries the template's managed block between markers, byte-identical, checked by the installed-copies test | 1 |
| Templates | `.tfw/templates/journal/event.md`:49, :70 (TD-200) · `.tfw/templates/team/profile.md`:12–14, :27–33 (TD-203, role location) · `.tfw/templates/status.md` (phase paragraph) · `.tfw/templates/project_config.yaml`:17 (`installed_from` form) | 4 |
| Briefing | `.tfw/templates/briefing.md` — **new** | 1 |
| Migration guide | `.tfw/migrations/2.0.0.md` — manifest location at :94, `cd .tfw` at :61, `--working-tree`, phase state hand-authored, three grammars unchanged | 1 |
| Copies, excluded | `.claude/commands/tfw-{update,plan,init}.md` · `.agent/workflows/tfw-{update,plan,init}.md` — re-synced byte-identical in the same commit as their source | 0 |

**Census at TS:** 29 physical paths, 23 counted, 1 new. **R2, measured at onboarding and extended by the
rulings below: 32 physical paths, 26 counted, 1 new.** Configured budget since `f3eb986` (owner,
2026-08-30): `50 / 50 / 5000 / 50`. The phase is also inside the `30 / 15 / 3000 / 30` that governed
A–AB; no ruling is needed under either. Any group appearing that this table does not name returns to the
coordinator before the work proceeds.

## 5. Acceptance Criteria

### AC-1: The pin is derived from the tag, not from `HEAD`

Fourth report §6. `update.md`:17–20 reads `source_head=$(git rev-parse HEAD)` and tests
`tag_commit = source_head`; on a source whose development has moved past its release the test can
never pass, and the fifth report passed it only because the source happened to stand on the tag.

- [ ] the operator names the target — a tag, or a commit when the owner deliberately takes an
      untagged payload and says so in the checklist; `source_head` is derived from it
      (`git rev-parse "$target_ref^{commit}"`), never from `HEAD`
- [ ] `VERSION` is read from that commit and compared with the tag's name; a mismatch stops
- [ ] the Step 5 recheck compares against the same derived commit, so a source that moved
      *elsewhere* during the update is still detected and a source that was ahead all along is not
      reported as movement
- [ ] the local-source cleanliness rule (`status --porcelain -- .tfw/`) stays as written

Gate: on this repository with `HEAD` ahead of `v2.0.0-dirty.4`, Step 0 as written passes for that tag;
with a fabricated tag whose `VERSION` disagrees with its name, it stops.
Evidence: both runs in the gates file, commands verbatim.

### AC-2: A receiver on any earlier tag finds its path

Fourth report §2–3; TD-190, TD-191, TD-198.

- [ ] the new entry's updating section names or points to every intervening entry's updating
      section (*"if you are on `.2`, also perform the `.3` section"* is sufficient); `RELEASE.md`
      §6 makes this a step of every release
- [ ] `RELEASE.md` §5 adds: when a release reverses a normative statement, the CHANGELOG quotes the
      retired wording verbatim as a search string. The `.3` entry gains the quote it lacks — *"Commands
      never duplicate workflow content — they reference it"* — and what a project that already went thin
      does about it (TD-198)
- [ ] the `2.0.0-dirty.2` entry's `TD-11` reference (`:297`) is corrected or removed (TD-191)
- [ ] the `2.0.0-dirty` migration fence (`:200–265`) carries a *superseded by* line pointing at the
      guide, and `RELEASE.md` names that marker as the form for any instruction a later release
      replaces (TD-190)
- [ ] `update.md` opens with Step −1: read the **target's** `.tfw/workflows/update.md` from the pinned
      payload and follow it, not the installed one; the migration guide's *"Updating from 1.x"*
      position repeats it as the first instruction, since an installed 1.x workflow cannot carry it.
      **R2:** the new entry's updating section opens with the same line — a `.2`–`.4` receiver's
      installed workflow lacks Step −1 too, and the entry is the first file the release tells it to open
- [ ] no CHANGELOG entry is rewritten in substance; additions are appended to the entries they
      concern, dated

Gate: a reader on `.2` follows the new entry to every instruction the `.3` and `.4` sections give,
without being told which of them to open by anyone but the CHANGELOG.
Evidence: the read-through recorded step by step in the gates file.

### AC-3: The retired-vocabulary gate can be literally green

Third and fourth reports; six hits in `update.md`:68, `init.md`:123 and their copies.

- [ ] the allowlist at `update.md`:111–115 admits *text whose purpose is to retire the term* — a
      retirement instruction anywhere in the payload — and says so in one sentence
- [ ] the six known hits fall inside the allowlist under that wording; the wording does not admit a
      live use of a retired term

Gate: the check on this repository and on one consumer returns zero outside the allowlist, with the
allowlist printed.
Evidence: both runs.

### AC-4: Every Step 6 row is executable the same way

Fourth report §4; TD-204.

- [ ] `.tfw/adapters/claude-code/CLAUDE.md.template` gains `<!-- TFW:CLAUDE:START -->` /
      `<!-- TFW:CLAUDE:END -->` markers bounding the managed content, on the Codex pattern
- [ ] the Step 6 table states per row whether the target is a **whole copy** verified by `cmp` or a
      **marker-bounded block** in a project-owned file verified on the region between the markers;
      the Claude rules and Codex routing rows are blocks, the rest are copies
- [ ] **R2 — one marker rule, stated once.** `conventions.md` §9 Tool Adapter Pattern carries the rule
      for every marker-bounded row, three cases: markers present → replace the text between them;
      file absent → create it from the template; file present **without** markers → **report and
      leave it**, the operator inserts the block once and it is mechanical from then on. Step 6 and
      both adapter READMEs point to §9. The Codex README's *"If it has no markers, append the
      complete block"* (`:104`) becomes that pointer: appending to a file that already has an
      unmarked hand-written TFW section produces two sections — the fourth report's `CLAUDE.md`
- [ ] **R2 — the block is brought current with the canon it describes.** The template's Context
      Loading names `status.md` as the task's only authority (conventions §10 order) and the command
      table carries every canonical workflow, `/tfw-knowledge` and `/tfw-config` included; `{version}`
      inside the block reads *see `.tfw/VERSION`*. Bounds: the `## TFW` section — context loading,
      commands, templates, key references. Project identity, mandatory rules, execution mode and code
      standards stay outside as project-owned text
- [ ] **R2 — the framework is its own first consumer.** This repository's root `CLAUDE.md` carries
      the block between markers, byte-identical to the template's block, and the installed-copies
      test checks it as it checks every other installed copy. Conduct and Execution Modes stay
      outside the block as this project's text
- [ ] **R2 — Cursor.** `.tfw/adapters/cursor/tfw.mdc.template` carries `{version}` three times, the
      TD-204 defect one adapter over; same fix, and the Cursor row is a whole copy
- [ ] `.tfw/adapters/antigravity/tfw-rules.md.template` stops requiring `{version}`: it reads
      `.tfw/VERSION` the way the rendered `.agent/rules/tfw.md` already does, and the two agree
      (TD-204)
- [ ] `.tfw/adapters/claude-code/README.md` describes the block and the first-run rule

Gate: `cmp` of the marker-bounded region on a fixture `CLAUDE.md` carrying project text above and
below the block, before and after sync; project text unchanged.
Evidence: the fixture and both regions.

### AC-5: `installed_from` has one form

Fourth report §8.

- [ ] `update.md` Step 7 and `templates/project_config.yaml`:17 state the form:
      `{upstream}@{verified-tag}`, where `{upstream}` is the value of `tfw.upstream` as configured —
      a URL or a symbolic name — and never a machine-local path; when the source is a local checkout,
      `tfw.upstream` names it symbolically and the checklist records the path
- [ ] `--check project` reports an `installed_from` that carries a drive letter, a leading `/` or a
      backslash as *machine-local; record the upstream reference*; it does not rewrite it
- [ ] `self` remains valid for this repository

Gate: `--check project` on a fixture config with `D:/…@v2.0.0-dirty.4`; then with `steps-framework@v2.0.0-dirty.4`.
Evidence: both outputs.

### AC-6: The owner is asked, not guessed

Fifth report §2 and the owner's account quoted there.

- [ ] `update.md` Step 3 gains a 🛑 gate **before the first durable project write**, with exactly three
      questions: *who is acting* (the handle — asked, never inferred from `git config user.name`, an
      OS username or the upstream's profiles), *where new tasks are created* (`tfw.task_containers`),
      *how the project verifies* (`build.*`). In AG mode the same three go out as one message and the
      run proceeds through read-only steps and stops at the write
- [ ] the answers are recorded in the update checklist
- [ ] after Step 8 a new Step 8a writes the **briefing** to the owner in `content_language`, from
      `.tfw/templates/briefing.md`: three blocks — *what is now possible* (from `Added`), *what stopped
      breaking* (from `Fixed`), *what no longer has to be done* (from `Removed`) — derived from the
      intervening CHANGELOG entries, no free text of its own.
      **R2:** an absent section yields *nothing in this release* for its block, never invented content.
      **A7 approved by the owner 2026-08-30: `Changed` is read too**, as a fourth block — *what you now
      do differently* — bound to the entry's own bullets, no free text. The sequencing constraint is
      lifted; AC-6 is built like any other criterion
- [ ] the briefing is the update's last message, and the checklist records that it was delivered
- [ ] `update.md` stays **under 1200 words** with Steps −1, 3, 5, 8a added; duplication is removed
      before content is

Gate: an AG-mode dry run against a fixture project stops with the three questions before any write;
the word count.
Evidence: the transcript of that stop and the rendered briefing for this repository's `.3 → .5` delta.

### AC-7: The payload copy cannot overwrite project-owned files

Fifth report §4.

- [ ] Step 5 names the exclusions: `.tfw/project_config.yaml` and `.tfw/knowledge_state.yaml` are
      never overwritten by the copy; the config is merged key by key as Step 3 already describes; the
      state file is never touched
- [ ] the step that copies **prints what it skipped**; a copy that reports nothing skipped on a project
      that has both files is a failed step
- [ ] **executor decision, recorded in the RF:** whether the payload stops carrying
      `knowledge_state.yaml` altogether (it is ⚫ project state by Step 3's own classification) or the
      exclusion list carries it. Either satisfies the criterion; the reason is what the RF records
- [ ] the payload path test (`test_integration.py`:510) covers the exclusion list, so a new
      project-owned file added to the payload without an exclusion fails a test
- [ ] **R2 — decided at onboarding: the exclusion list carries both files; the payload keeps carrying
      them.** A root `.gitattributes export-ignore` would govern `git archive` alone and add a root
      file outside the census. The RF records the root cause as an observation for the payload
      boundary (Phase AA's surface): the payload carries this repository's own `project_config.yaml`
      and `knowledge_state.yaml`, files conventions §10.3 says are never sourced from upstream

Gate: a fixture with a customized `project_config.yaml` and a non-framework `knowledge_state.yaml`;
after the copy both are byte-identical and both are printed as skipped.
Evidence: the fixture, the copy output, `cmp` on both files.

### AC-8: The status cell is parsed whole or refused, and no phase is left without a named state

Fifth report §1. `classify_status()`:162–181 takes the first `[A-Z_]+` token; `✅ DONE (A/V/B/C) ·
🔄 Phase D … R8 🟢 RF …` classified `DONE`, and `plan()`:865 wrote nothing for a live task.

- [ ] a status cell is **one** declared lifecycle token followed by free text that contains **no further
      declared token and no further status symbol**. Anything else is `UNDECLARED` with
      `lifecycle_verbatim` carrying the cell, bounded as today.
      **R2 — a status symbol is a character of Unicode category `So`** (other symbols: ✅ ❌ 🔄 🟢 🟡
      ⬜ …), measured on four corpora at onboarding: 8 rows change, every one carrying a second
      emoji or a second declared token. `Sm`, `Sc`, `Sk` (`+ → = <`) are prose punctuation on every
      board measured and are not signals — under category S entire, three single-signal rows
      (`TFW-52`, `HD-30`, live `HD-31`) would be refused on a plus sign or an arrow. `U+FE0F` and
      `U+200D` are skipped explicitly. The fixture tests a second emoji alone, a second token alone,
      `→` and `+` as non-signals, and a bare variation selector after the token
- [ ] an `UNDECLARED` row is never classified terminal and never skipped by `plan()`; it receives a
      `status.md` at `UNDECLARED`, exactly as a single unknown token does today
- [ ] the manifest lists such rows under their own heading — *Rows carrying more than one lifecycle
      signal* — and the *Task state written* note stops implying the skipped rows are all terminal
- [ ] the manifest names every `phase-*` directory of every matched task and states in one sentence
      that **phase state is not written by migration; author `{phase}/status.md` by hand**
- [ ] `--check tasks` reports a phase directory that carries no `status.md`: a **failure** when the
      task's own `status.md` is non-terminal; an **informational line** when the task is terminal or
      carries no `status.md` at all — a terminal legacy task migrated without state, by design, and a
      phase closed before phase state existed is history, not a defect. On this repository the
      measured set is 17 directories under TFW-42, 46, 47, 52, 53 and 55; all six tasks are terminal
      by the board snapshot and carry no task-level state, so all 17 are informational. It writes
      nothing. **R2:** informational lines are grouped **one line per task**, naming that task's
      stateless phase directories — six lines on this repository, not seventeen; exit code unchanged.
      When the task's own `status.md` is malformed, its stateless phases are informational — the
      malformed state is already the failure — and the line says so
- [ ] `templates/status.md` carries the phase paragraph a phase file already uses in this repository
      (*"…this phase's live state. The task-level `status.md` never summarizes it."*) and says when to
      use which
- [ ] the migration guide says all of the above in the order a receiver meets it
- [ ] the `AILAB-2` row shape is a committed fixture, failing before the change and passing after

Gate: the fixture; `--check tasks` on a fixture task with a phase directory lacking state; and on this
repository — green, with 17 informational lines and no failure.
Evidence: the three runs, plus the four pinned corpora compared identifier by identifier before and
after — no classification other than the multi-signal rows changes.

### AC-9: The abbreviation is the initials of the approved title

Owner ruling 2026-08-30; TD-201.

- [ ] `conventions.md` §4 Identifier: `ABBR` is the acronym of the approved full title — the initials of
      its significant words, uppercase alphanumeric — proposed **together with the title** in one
      exchange and approved by the owner with it. *Never derived silently* is rewritten to say both
      things it means: never invented apart from the title, never created without approval
- [ ] `plan.md` Step 3.5 and Step 4.2, `init.md` Batch 1 and Mini-Setup 6, `glossary.md` *Task Naming*
      say the same in their own words; the worked examples read as title → initials
      (*Conflict Resistant Shared Workspace* → `CRSW`; *Assisted 1.5 core and synchronization* →
      `ASSISTED15` is admissible, since digits are alphanumeric)
- [ ] the HL template header carries **Title** and **Abbreviation** as adjacent fields, in that order
- [ ] `conventions.md` §4 Artifact file naming gains the current-grammar rows with an example:
      `HL-TFW_20260829-172110_ABT.md`, `RES__TFW_20260829-172110_ABT.md` — no title appended, for the
      reason the clock-task rule already gives (TD-201)

Gate: read `plan.md`, `init.md`, `conventions.md`, `glossary.md`, `templates/HL.md`: one rule, four
carriers, no contradiction; `gen_docs.py` resolves the example filename.
Evidence: the five excerpts side by side in the EV.

### AC-10: Payload carriers agree with the canon and with each other

TD-200, TD-203; fifth report §5–6.

- [ ] `templates/journal/event.md`:49 and :70 describe `via` as `conventions.md` §4 does — free-form
      non-empty provider or tool text (TD-200)
- [ ] `templates/team/profile.md` stops saying *humans and agents alike* while saying agents are
      unusable; it says: one file per person, and where a participant's **role and context** are
      recorded — `team/README.md`, which the parser skips — so no one invents a fifth key (TD-203)
- [ ] `.tfw/migrations/2.0.0.md`: one manifest location (`tasks/MIGRATION-2.0.0.md`, beside the
      snapshot, or the root — one, stated); the sentence *when the board in the working tree is newer
      than `HEAD` and committing is not within your authority, `--working-tree` is the flag for exactly
      this case; record the choice*; every command written from the project root — `cd .tfw && …`
      at :61 rewritten
- [ ] a `grep` for the four retired wordings over the templates and the guide returns nothing

Gate: the grep; the guide's commands executed from the root as written.
Evidence: the grep output and one command run.

### AC-11: The release describes what shipped

- [ ] **executor:** the RF states what a project on `2.0.0-dirty.2`, `.3` or `.4` must know, so the
      entry's updating section and the briefing can be written from it
- [ ] **executor:** every fifth-report §6 item and fourth-report defect 7 is either fixed here with a
      one-line reason or recorded in RF §6 Observations for the reviewer to file
- [ ] **`/tfw-release`, after review:** version bump, CHANGELOG entry and tag as one act, the tag
      verified to exist; the entry's updating section satisfies AC-2 for a receiver on `.2`, `.3`
      or `.4`
- [ ] **field:** one consumer already on the line updates to the new tag following the target's
      `update.md` from Step −1, with the derived pin, the three questions and the briefing on record —
      a field report is welcome but the checklist alone is the evidence
- [ ] `2.0.0` is not claimed

Gate: read the entry as a receiver on `.2` and follow every instruction it gives.
Evidence: the tag exists; the consumer's checklist.

### Evidence Artifacts

| File | Description |
|------|-------------|
| `evidence/EV__phase-ac__update_without_guesswork.md` | Environment header, per-AC table, verdict _(required)_ |
| `evidence/pin_on_live_source.txt` | AC-1 — both Step 0 runs, commands verbatim |
| `evidence/skipped_tag_read_through.txt` | AC-2 — the `.2` reader's path through the entries |
| `evidence/gates_and_word_count.txt` | AC-3, AC-6 — allowlist runs, word count, AG-mode stop transcript |
| `evidence/markers_and_exclusions.txt` | AC-4, AC-7 — `cmp` regions, copy output, both skipped files |
| `evidence/status_cell_before_after.txt` | AC-8 — the `AILAB-2` fixture, `--check tasks` runs, four-corpus comparison |
| `evidence/carriers.txt` | AC-9, AC-10 — the five excerpts, the grep, the root-run command |
| `evidence/briefing_dirty3_to_dirty5.md` | AC-6 — the rendered briefing for this repository's own delta |

## 6. Technical Guidance

- **Whole-or-refuse is one rule, now applied to the second cell.** `parse_identifier()` is the model:
  named forms, one dispatcher, `malformed`/`UNDECLARED` as the only fallback. Do not add a second
  heuristic for "closed phases then a live one" — that is the guess, restated.
- **The `AILAB-2` shape has two signals:** a second declared token (`RF`) and a second status symbol
  (`🔄`). Either alone must be enough; the fixture should test them separately.
- **`iter_phase_dirs()` already exists** in `gen_index.py`:464; `migrate_board.py` imports from
  `gen_index` today. Reuse it for the manifest's phase listing.
- **Terminal tasks with stateless phase directories are history.** Seventeen of them in this repository,
  under six tasks that closed before phase state existed and carry no task-level state either —
  migration writes state only for non-terminal tasks, by design. An informational line, not a failure.
- **The word ceiling is the pressure that keeps `update.md` a procedure.** Steps −1, 3, 5 and 8a add
  roughly 250–300 words to 840. Remove duplication first; the briefing's structure lives in the
  template, not in the workflow.
- **Markers, first run — R2.** Revision 1 called *report and leave* the Codex rule; the Codex README
  actually appends. The TS rules *report and leave* for every block row and puts the rule once in
  conventions §9. Do not invent detection of "where the TFW content probably is".
- **Do not touch other tasks' files.** `check_tasks` naming a stateless phase directory is the
  deliverable; writing its `status.md` is not. The same for consumer projects.
- **Evidence at a pinned commit, never `HEAD`** — the rule this task has met from both sides.
- **The RF is not optional** (TD-199). The reviewer reads it against this TS and the master HL at
  `56c3d70`.

## 7. Definition of Failure

- ❌ A pin, anywhere in `update.md`, that is computed from the source's `HEAD`
- ❌ A status cell carrying two lifecycle signals classified by either of them
- ❌ A row skipped by `plan()` for a reason the manifest does not print
- ❌ A phase directory without state that `--check tasks` does not name
- ❌ A `status.md` written by this phase into any task other than its own fixtures
- ❌ A copy step that can overwrite `project_config.yaml` or `knowledge_state.yaml`
- ❌ A handle inferred from a Git identity, OS username or upstream profile — in the workflow text or in
  the fixture run
- ❌ An abbreviation rule that can be read as "invent a code" or as "derive without approval"
- ❌ `update.md` at or above 1200 words
- ❌ A CHANGELOG entry rewritten in substance rather than appended to
- ❌ A form that parsed before this change no longer parses, or any identifier classified differently
  except the multi-signal rows
- ❌ Any budget limit crossed without returning to the coordinator
- ❌ A check reported as passing that never ran

## 8. Phase Risks

| Risk | Control |
|---|---|
| `UNDECLARED` for multi-signal cells strands real tasks | The rule conventions §5 already gives: a person resolves with a `transition` event `from: UNDECLARED`; the manifest names each row |
| The three questions make unattended updates impossible | One message, before the first durable write; read-only steps proceed; AG already stops at approvals |
| `update.md` crosses the ceiling | Duplication removed first; briefing structure in a template; word count is an AC gate |
| Markers break a consumer whose `CLAUDE.md` has none | Reported and left untouched on first sync — the marker rule in conventions §9, one rule for both adapters |
| The exclusion list rots | Covered by the payload path test that already enumerates every payload file |
| The phase reopens the parser wider than one cell | AC-8's before/after comparison on four corpora: only multi-signal rows change |
| A stateless phase directory in a live consumer task turns its gate red | That is the report the fifth report asked for; the owner authors the file and records the event, the shape conventions §5 already gives for `UNDECLARED` |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|---|---|---|
| `.tfw/templates/status.md` | Phase B may add debt-related guidance | AC adds only the phase paragraph; no key changes |
| `.tfw/workflows/update.md` | Phase B (debt view in the update path, if any) | AC leaves it under 1200 words; B inherits the ceiling |
| `.tfw/scripts/gen_index.py` | Phase B (debt discovery) | AC touches `check_tasks()` only |

---

*TS — TFW-60 / Phase AC: Update Without Guesswork | 2026-08-30*
