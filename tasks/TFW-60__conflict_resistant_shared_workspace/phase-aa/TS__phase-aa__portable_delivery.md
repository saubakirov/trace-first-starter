# TS — TFW-60 / Phase AA: Portable Delivery

> **Date**: 2026-08-27
> **Author**: Claude Code (Coordinator)
> **Status**: ✅ APPROVED — owner, 2026-08-27. Execution authorized
> **Phase HL**: [HL Phase AA](HL__phase-aa__portable_delivery.md)
> **Master freeze**: `2123de1` — baseline after amendment A4
> **Origin**: [FIELD-REPORT](../FIELD-REPORT__TFW-60__first_external_update.md) F1–F10, plus three owner items
> **Predecessor RF read through the Pre-TS Gate**: [Phase A RF](../phase-a/RF__phase-a__task_state_and_coordination.md) at pinned snapshot `afd24f5`, and [REVIEW rev4 — APPROVE](../phase-a/REVIEW__phase-a__task_state_and_coordination__rev4.md)

---

## 1. Objective

Make the framework deliverable. After this phase a project that is not this one completes the update from
the payload alone: no file hand-carried out of this repository, no edit inside `.tfw/`, and every
instruction the release gives names something the receiving project actually has.

The model itself does not change. No carrier, schema, vocabulary, lifecycle value or identifier rule is
touched.

## 2. Scope

**In scope:** the payload boundary, the two scripts and their tests, `update.md`, `init.md`,
`conventions.md`, `glossary.md`, `project_config.yaml`, the `status.md` template, a per-major migration
guide, `team/` delivery, a post-update self-check, the Claude Code adapter's broken research route, the
session-naming step in `plan.md`, and the `2.0.0-dirty.2` release surface.

**Out of scope:** every historical trace artifact; the Assisted edition's folder-moving status model
(TD-182, deferred by owner decision); transport mode (TFW-61); Phases B and C; and retrofitting the
consumer project.

### Two decisions the owner has already settled

| Decision | Ruling |
|---|---|
| Where the tooling lives | **`.tfw/scripts/`** — inside the payload. Owner-approved 2026-08-27 |
| A journal `kind` for an inbound external record (F9) | **No new kind.** The canon states instead that some artifacts legitimately have no event. A closed vocabulary that opens at the first inconvenience was never closed |

## 3. Principles Check

| Principle | Where it is verified |
|---|---|
| P1 Pain before mechanism | AC-13 — the pain is a real external project, and only a real external project closes it |
| P2 Task locality | Untouched. Nothing here writes task state |
| P3 One normal writer | Untouched |
| P4 Stable paths over status moves | AC-4 — an unmatched legacy directory is reported, never reclassified or moved |
| P5 Local truth, derived views | AC-4, AC-9 — the self-check reports and repairs nothing |
| P6 Filesystem first, Git preserved | AC-8 — a committed revision is the migration's stable input |
| P7 Coordinator logs management | F9 ruling — an advisory artifact needs no event |
| P8 Consolidation is a boundary | Untouched |
| P9 No trace deletion during simplification | AC-1, AC-4 — 82 historical artifacts keep their bytes; unmatched input is surfaced, not dropped |
| P10 Every phase pays for its release surface | AC-14 — the phase that exists because a release surface was unpaid |

## 4. Affected Files

**Measured 2026-08-27 at `61f0fa8`.** Byte-identical adapter copies are excluded by owner ruling S32,
and work artifacts by S46.

### Create — 7

| Path | Why |
|---|---|
| `.tfw/scripts/gen_index.py` | moved into the payload |
| `.tfw/scripts/migrate_board.py` | moved into the payload |
| `.tfw/scripts/test_gen_index.py` | moved with its subject |
| `.tfw/scripts/test_migrate_board.py` | moved with its subject |
| `.tfw/scripts/README.md` | what these are, why they are in the payload, and how a project runs them |
| `.tfw/migrations/2.0.0.md` | the guide whose absence made a major release unfollowable |
| `.tfw/templates/team_README.md` | `team/` currently arrives, if at all, with no explanation |

### Modify — 26

| Group | Paths |
|---|---|
| Normative path references | `.tfw/conventions.md`, `.tfw/glossary.md`, `.tfw/project_config.yaml`, `.tfw/workflows/init.md` |
| Update path | `.tfw/workflows/update.md` — migration-guide routing, `task_containers` as a decision, `initial_seq` removal, the pristine-tag diff, the `team/` creation step |
| Session naming | `.tfw/workflows/plan.md` |
| Carrier ergonomics | `.tfw/templates/status.md` |
| Adapter source | `.tfw/adapters/claude-code/CLAUDE.md.template` — TD-11 |
| Tooling | `docs/scripts/gen_docs.py`, `docs/scripts/test_integration.py`, `docs/mkdocs.yml` |
| Release surface | `.tfw/VERSION`, `.tfw/CHANGELOG.md`, `README.md` |
| Adapter copies | `tfw-init`, `tfw-update`, `tfw-plan` under `.claude/commands/` and `.agent/workflows/`, and the matching `.agents/skills/` entries |

### Delete — 4

The four script files leave `docs/scripts/`. This is a move, so `git mv` preserves history.

### Never modify — 82

Historical trace artifacts under `tasks/` that name `docs/scripts/`: RF, REVIEW, ONB, TS and evidence from
TFW-26 through TFW-56. They record what was true when written.

### The eleven generated `status.md` files

Each carries `<!-- Written by docs/scripts/migrate_board.py … -->`. **Leave the bytes.** It is a
provenance statement about a past act at a path that was correct then; rewriting it would make the record
say something that did not happen. The migration guide notes that a project migrated before this phase
carries the old path in that comment. Recorded here so the choice is visible rather than silent.

### Budget

| | Count | Limit | |
|---|---:|---:|---|
| New files | 7 | 15 | ✅ |
| Modified files | 26 | 30 | ✅ |
| Total touched | 37 | — | |
| New LOC | ~600 est. | 3000 | ✅ |

**Phase AA fits the budget.** The 2,864 lines of script relocate rather than get rewritten, so they cost
a move and their path constants. The exact census is the executor's first deliverable and returns to the
coordinator if any group appears or any limit is crossed — Phase A's overrun ruling does not extend here.

## 5. Acceptance Criteria

### AC-1: The tooling ships inside the payload  [F1]

- [ ] both scripts and both test files live at `.tfw/scripts/`, moved with `git mv`
- [ ] project-root resolution no longer depends on directory depth: `parents[2]` is replaced by a search
      that finds the root by a marker, so the tools work wherever a project places them
- [ ] every normative reference names the payload path — `conventions.md`, `glossary.md`, `init.md`,
      `project_config.yaml` and their propagated copies
- [ ] `docs/scripts/` retains only documentation tooling; `gen_docs.py` and `test_integration.py` follow
      the new path where they reference it
- [ ] `.tfw/scripts/README.md` states what a receiving project runs and when
- [ ] the full suite passes from the new location, and `docs/mkdocs.yml` still builds

Gate: `git grep -n "docs/scripts/gen_index\|docs/scripts/migrate_board"` returns only historical trace
artifacts and the eleven provenance comments. Run both tools from a checkout placed at a different depth.
Evidence: command output at a pinned commit.

### AC-2: A major release ships a migration guide  [F2]

- [ ] `.tfw/migrations/2.0.0.md` exists and is written for a project that is **not** this one: no
      `task_containers: [workspace, tasks]`, no 7,505 references, no 666 files
- [ ] the ordering constraint — migrate, generate, **then** remove the board — appears where a reader is
      about to violate it, not only in a summary
- [ ] `update.md` Step 3 routes to the guide when the update crosses a major version
- [ ] the guide names the quiescence rule from AC-8 and the `task_containers` decision from AC-6
- [ ] the canon states that a major release without a migration guide is incomplete

Gate: a reader following only `update.md` and the guide reaches a validated state without opening the
CHANGELOG.
Evidence: AC-13's external run is the test; the reader's path is recorded.

### AC-3: Migration finds a board wherever the project keeps it  [F3]

- [ ] the board location and heading are inputs, not constants — `--board` and `--board-heading`, or
      configuration, or both
- [ ] defaults are unchanged, so this repository's behaviour does not move
- [ ] a zero-row result names **relocation** among the causes, not only removal; the current message sends
      the reader to diagnose a removed board when the board is merely elsewhere
- [ ] the row parser is not touched — it already read the consumer's nine-column table unmodified

Gate: run against a fixture whose board is at `tasks/README.md` under `## Board` and get the rows. Run
with no board and read the refusal.
Evidence: both outputs quoted.

### AC-4: An unmatched legacy directory is reported, never described  [F4]

- [ ] a task directory the identifier grammar does not match is routed to **`Unresolved inputs`**
- [ ] it is never classified as `Backlog`, and no generated artifact prints a reason the source did not
      carry — the run that produced this finding asserted *"backlog idea, never started"* about two
      directories holding completed HL, TS and RF traces
- [ ] the single-underscore legacy form is either matched or reported; `TASK_DIR` currently requires `__`,
      and this corpus is uniform only by accident
- [ ] the manifest and the index agree on the classification and on the count

Gate: fixture with `TFW-01_single_underscore` and `TFW-3__double__underscore` side by side; both appear,
neither is called an idea.
Evidence: generated index and manifest quoted.

### AC-5: A person can hand-author the carrier correctly  [F5]

- [ ] the `status.md` template's example quotes its values; the current example models the unquoted form
      and a value containing `": "` ends a YAML plain scalar
- [ ] the template states that values need quoting, alongside the bounds it already gives
- [ ] `--validate` names the offending key rather than reporting `unparseable front matter: ScannerError`
- [ ] a worked, valid example is reachable from the template

Gate: feed five files whose titles contain `": "`; each error names its key.
Evidence: validator output before and after.

### AC-6: `task_containers` is presented as a decision  [F6]

- [ ] `update.md` presents it as a choice with its two real options — one container, or the old container
      second so existing paths keep resolving — and not as a value to preserve
- [ ] the text states that it does not exist before 2.0.0, so there is nothing to preserve
- [ ] `initial_seq` is named as a key to **remove**, not left to be inferred from `init.md`

Gate: an operator following `update.md` makes the choice deliberately and can say why.
Evidence: recorded in AC-13's run.

### AC-7: `team/` is delivered, not assumed  [F7]

- [ ] `.tfw/templates/team_README.md` ships and explains the directory
- [ ] `update.md` and `init.md` carry an explicit step creating `team/` and the acting profile **before the
      first durable write**
- [ ] a project that skips it learns so from AC-9's self-check, not from a framework test it was never
      told to run

Gate: update a fixture with no `team/` and confirm the step fires and the self-check reports it.
Evidence: self-check output.

### AC-8: Migration reads a stable input  [F8]

- [ ] `read_board()` defaults to a committed revision; the working tree becomes the explicit opt-in
- [ ] the guide states plainly: do not migrate while a participant is mid-gate
- [ ] the run records which revision it read

Gate: change the working-tree board during a run and show the result is unaffected.
Evidence: run log naming the revision.

### AC-9: One command answers whether the project is consistent with the release  [rec 9]

- [ ] a self-check reports on the payload, `team/`, the container configuration, retired keys and carrier
      validity
- [ ] it **reports and exits**: it repairs nothing, writes nothing, and is not authority
- [ ] its output names what it did not check
- [ ] it is named in the migration guide as the last step

Gate: run on this repository and on a deliberately broken fixture; both outputs quoted.
Evidence: both runs.

### AC-10: The update path carries the technique that made it safe  [field report §3]

- [ ] `update.md` instructs diffing every local `.tfw/` file against the **pristine previous tag** before
      merging anything
- [ ] the reason is stated: this single check collapsed three declared manual merges to zero, including
      `conventions.md` with 212 changed lines
- [ ] `tfw.upstream` accepts a local working tree as a source, and the operator is told to verify that the
      source's own `.tfw/` is clean at the tag before trusting the payload

Gate: the sequence is followable against `v2.0.0-dirty` with no local modifications found.
Evidence: recorded in AC-13's run.

### AC-11: Shipped instructions name files that exist  [TD-11]

- [ ] `.tfw/adapters/claude-code/CLAUDE.md.template` routes `/tfw-research` to
      `.tfw/workflows/research/base.md`; it has named the non-existent `.tfw/workflows/research.md` for two
      releases
- [ ] every path in every adapter source resolves; a test fails if one does not
- [ ] propagated copies match their sources

Gate: a link/path check over adapter sources and copies, failing on a deliberately broken entry first.
Evidence: the check failing, then passing.

### AC-12: The session name carries the task once the task exists  [owner, out of theme]

- [ ] `plan.md`'s naming step moves to **after** the identifier exists. The question-first order stays —
      understanding the task and asking before creating a folder is the order the owner wants kept
- [ ] the step repeats when the slug changes
- [ ] a phase appears in the name when the agent is given one, as `handoff.md` already does
- [ ] the instruction is a numbered step, not a note; the current `Step 0` form is unsatisfiable for a new
      task because it demands an identifier that does not yet exist

Gate: walk `plan.md` for a new task and confirm the name is set once the folder exists, and again after a
slug change.
Evidence: the walked sequence recorded.

### AC-13: An external project completes the update from the payload alone  [DoD 19]

- [ ] **at least one project other than this one** completes the update with zero files hand-carried and
      zero edits inside `.tfw/`
- [ ] the operator follows `update.md` and the migration guide only
- [ ] every local delta the first consumer had to invent — the board flags, the copied `team/README.md`,
      the tooling placement — is unnecessary
- [ ] the run records what was confusing, not only what worked
- [ ] **this repository is not admissible as the only fixture.** Every Phase A round ran here, which is
      why none of this was found

Gate: the external run itself, reported as the first one was.
Evidence: a field report from the receiving project, filed like its predecessor.

### AC-14: The release describes what shipped  [P10]

- [ ] `2.0.0-dirty.2` in `.tfw/VERSION`, `tfw.version` and the tag. **Not `2.0.1-dirty`**: `2.0.0` was
      never pushed, so there is nothing to patch, and by semver `2.0.0-dirty.2 < 2.0.0` keeps the claim
      unmade
- [ ] the CHANGELOG entry states what the first external update found, including that the framework could
      not deliver its own tooling
- [ ] the migration prose no longer instructs a reader to run a file they do not have
- [ ] the canon states that migration must never normalize `UNDECLARED` while an accountable owner may
      resolve it through a recorded transition (F10) — currently the prohibition reads as absolute and
      projects will either strand tasks or resolve them without a trace
- [ ] the canon states that some artifacts legitimately have no journal event (F9 ruling), so the closed
      vocabulary stays closed

Gate: read the entry as a receiving project and follow every instruction it gives.
Evidence: AC-13's run is the read.

## 6. Technical Guidance

- **Order of work.** Census first, before a single edit. Then the move with `git mv` and its path
  constants, then the suite, then the normative references, then `update.md` and the migration guide,
  then the self-check, then adapters and copies, then the release surface. The move goes first because
  everything else names its result.
- **The move is a move.** `git mv` so history follows. Do not copy-and-delete; a script whose history
  stops at Phase AA loses the four rounds of reasoning behind its current shape.
- **Root resolution.** Replace depth arithmetic with a marker search — walk upward for `.tfw/`. This is
  what makes AC-1's "wherever a project places them" true rather than aspirational.
- **Do not touch the row parser** (AC-3). The field report is explicit: it already read a nine-column
  table unmodified. Only the locator was wrong, and a parser change would put a working component at
  risk for no gain.
- **Preserve what Phase A got right.** The empty-board refusal, the per-identifier accounting, the
  index's declaration of its own non-authority. All three earned their place in the field report; none may
  be weakened. If a change would soften one, stop and return.
- **The self-check is not a repair tool.** It reports and exits. The moment it writes, it becomes a second
  authority over task state, which P5 forbids.
- **Evidence is measured at a pinned commit** and never against `HEAD` — the rule Phase A learned over
  three rounds and recorded in its own RF. A measurement cannot include the act of recording it.
- **Session naming is bounded** (AC-12) to the rename step and its repeat. Anything larger returns to the
  coordinator: it is an out-of-theme rider, admitted only because the file is already open.
- **The stray `phases/` directory** is not produced by anything this release ships — zero occurrences in
  `.tfw/` or either script. Record the check; do not chase it. Its author is findable only in the
  consumer's own history.

## 7. Definition of Failure

- ❌ The payload still cannot deliver a file the release instructs a project to run
- ❌ A historical trace artifact is edited to follow the new path
- ❌ A generated artifact describes real work as something the source never said
- ❌ The row parser, the empty-board refusal or the index's non-authority declaration is weakened
- ❌ The self-check writes anything, or is treated as authority
- ❌ Root resolution still depends on directory depth
- ❌ `2.0.0` is claimed, or the version is numbered as a patch to a release that never shipped
- ❌ **This repository is used as the only evidence fixture.** The phase exists because that was
  sufficient once
- ❌ A check reported as passing that never ran — Phase A's recurring failure in four forms: a review
  passing `E27` against a file containing zero; an event stamped from a composed time; a scan whose
  `grep -P` had aborted; a validator test taking the one path where its defect cannot appear
- ❌ Any census group appearing, or any budget limit crossed, without returning to the coordinator.
  Phase A's overrun ruling does not extend to this phase
- ❌ The model changed: any edit to a carrier schema, the event grammar, the lifecycle vocabulary or the
  identifier rules

## 8. Phase Risks

| Risk | Control |
|---|---|
| The move breaks this repository while fixing others | Suite runs before and after; `mkdocs` build is a gate; every reference follows in one pass |
| A second external project reveals a third class of assumption | Expected. DoD 19 says *an external project*, and one fixture is the floor |
| The migration guide becomes another unread wall | Per-major, routed from the step that needs it, ordering stated where it would be violated |
| The session-naming rider grows | Bounded in AC-12; anything larger returns |
| `UNDECLARED` guidance invites normalization | The canon separates the two acts explicitly: migration never normalizes, an accountable owner resolves through a recorded transition |
| Phase AA is read as licence to revisit Phase A | The declared outcome is delivery. A finding about the model is filed, not fixed here |

## 9. Cross-Phase Modifications

None. Phase AA touches no file Phases B or C own, and changes no carrier they will extend. `TECH_DEBT.md`
and `KNOWLEDGE.md` are untouched — TD-11's repair is in the adapter source, and its row is closed by
`/tfw-docs` after approval, not by the executor.

---

*TS — TFW-60 / Phase AA: Portable Delivery | 2026-08-27*
