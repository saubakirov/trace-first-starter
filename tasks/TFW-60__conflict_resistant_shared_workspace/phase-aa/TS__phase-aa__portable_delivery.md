# TS — TFW-60 / Phase AA: Portable Delivery

> **Date**: 2026-08-27
> **Author**: Claude Code (Coordinator)
> **Status**: ✅ APPROVED — owner, at **revision 4**. Corrective pass authorized
> **Revision 4**: 2026-08-28. AC-13 half two ran and came back negative on four counts; AC-15 carries
> them. Review revision 2 approved the work and held the phase open for exactly this evidence, so this
> is the awaited result rather than a reopening. TD-192 and TD-193 are promoted out of the register.
> **Revision 2**: 2026-08-27, after onboarding. Eight blocking questions answered; changes carry `R2`.
> **Revision 3**: 2026-08-27, after the owner challenged `team_readme.md`. Changes carry `R3` and the
> phase now **removes more than it adds**: two files the coordinator invented are withdrawn, three
> templates move into the shape this repository already uses, and three synonymous flags collapse into
> one. Create drops 7 → 5; the flat template namespace shrinks by 3; a five-line disambiguating comment
> is deleted.
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

### Create — 1

**R3 — a moved file is not a new file, and revision 1 counted seven.** The four scripts relocate by
`git mv`; they add no surface, and Git records them as renames. Revision 1 listed them under Create,
which inflated the count and hid what this phase actually introduces. It introduces one document.

| Path | Why |
|---|---|
| `.tfw/migrations/2.0.0.md` | the guide whose absence made a major release unfollowable |

Both numbers are stated so a reviewer sees the move rather than a smaller total: **1 created, 7 moved.**

### Withdrawn at R3 — two files the coordinator invented

Both were removals disguised as additions, and neither survives the question *what existing
responsibility does this absorb.*

| Withdrawn | Why it does not exist |
|---|---|
| a `team/` README template | It solved a problem that does not occur. AC-7 creates `team/` **together with its first profile**, so an unexplained empty directory never appears. Its content duplicated `conventions.md` — declared-attribution-not-authentication at :268, the three identity fields at :290–292, provider-is-not-an-actor at :296 — and shipping that duplication into every project makes the canon's third copy. D24 does not rescue it: that decision governs **enforcement-critical values an agent must apply**, and this file is read by a human browsing a directory. The orientation a person needs lives in the profile template's own guidance comment, where they already are |
| `.tfw/scripts/README.md` | Third copy. `--help` says how to run the tools, the migration guide says when, `conventions.md` says where they live. The one genuinely new fact — the tools find the root by walking upward, so a project may place them anywhere — goes into `--help` output and one line in `conventions.md`, not a new file |

### Move — 3 templates into the shape this repository already uses

`.tfw/templates/` already mirrors its output directories for `research/`, `evidence/` and `review/`. Three
templates break that rule by spelling the directory as an underscore inside the filename:

```text
templates/team_profile.md    → team/<handle>.md      →  templates/team/profile.md
templates/journal_event.md   → journal/<name>.md     →  templates/journal/event.md
templates/topic_file.md      → knowledge/<topic>.md  →  templates/knowledge/topic.md
```

`git mv`, references updated. **No new files** — the flat namespace shrinks by three. Two of the three
shipped in Phase A and the third is older; they are corrected here because this phase is already sweeping
template references, and noticing dirt without removing it is leaving it.

### Modify — 26

| Group | Paths |
|---|---|
| Normative path references | `.tfw/conventions.md`, `.tfw/glossary.md`, `.tfw/project_config.yaml`, `.tfw/workflows/init.md` |
| Update path | `.tfw/workflows/update.md` — migration-guide routing, `task_containers` as a decision, `initial_seq` removal, the pristine-tag diff, the `team/` creation step |
| Session naming | `.tfw/workflows/plan.md` |
| Carrier ergonomics | `.tfw/templates/status.md` |
| Adapter source | **R2** — `.tfw/adapters/claude-code/CLAUDE.md.template`, **`.tfw/adapters/claude-code/README.md`** and **`.tfw/adapters/antigravity/README.md`**. All three route `/tfw-research` at the non-existent `.tfw/workflows/research.md`; bounding AC-11 to the template would leave its own gate unwritable |
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
| **Created** | **1** | 15 | ✅ |
| **Moved** | **7** — 4 scripts, 3 templates | — | adds no surface; Git records renames |
| Modified files | ~25 | 30 | ✅ |
| New LOC | ~500 est. | 3000 | ✅ |
| **Files removed from the flat template namespace** | **3** | — | net cleanup |
| **Files withdrawn before creation** | **2** | — | net cleanup |

**Phase AA fits the budget.** The 2,864 lines of script relocate rather than get rewritten, so they cost
a move and their path constants. The exact census is the executor's first deliverable and returns to the
coordinator if any group appears or any limit is crossed — Phase A's overrun ruling does not extend here.

> **R2 — the counted census governs, not the number above.** Onboarding enumerated the paths this table
> actually lists and reached **23**, not 26; the figure was the coordinator's estimate and the table
> under-listed. With the two adapter READMEs added and `KNOWLEDGE.md` excluded, expect roughly **25**
> against a limit of 30. The RF carries what was counted.

## 5. Acceptance Criteria

### AC-1: The tooling ships inside the payload  [F1]

- [ ] both scripts and both test files live at `.tfw/scripts/`, moved with `git mv`
- [ ] project-root resolution no longer depends on directory depth: `parents[2]` is replaced by a search
      that finds the root by a marker, so the tools work wherever a project places them
- [ ] every normative reference names the payload path — `conventions.md`, `glossary.md`, `init.md`,
      `project_config.yaml` and their propagated copies
- [ ] `docs/scripts/` retains only documentation tooling; `gen_docs.py` and `test_integration.py` follow
      the new path where they reference it
- [ ] **R3** — no `.tfw/scripts/README.md`. The root-resolution rule is stated in `--help` output and in
      one line of `conventions.md`; a fourth copy of how to run the tools is not created
- [ ] the full suite passes from the new location, and `docs/mkdocs.yml` still builds

Gate **R2**: `git grep -n "docs/scripts/gen_index\|docs/scripts/migrate_board"` returns only historical
trace artifacts, the eleven provenance comments, **and `KNOWLEDGE.md:22`** — a known exception, owned by
`/tfw-docs` under the D37 split and closed after approval, not by the executor. It is named here so the RF
does not report a green gate over a red one.

**The depth test is not what it first appears.** `parents[2]` resolves correctly *by coincidence* from
`.tfw/scripts/`, so a source-only move passes every test in this repository while leaving the defect
intact — and a checkout at a different depth does not catch it either, because the default is relative to
the script file rather than the cwd. The observable test is a **copy of the tools at a different depth
inside a project**, for example `tools/tfw/gen_index.py`. That is the required fixture.
Evidence: command output at a pinned commit.

### AC-2: A major release ships a migration guide  [F2]

- [ ] `.tfw/migrations/2.0.0.md` exists and is written for a project that is **not** this one: no
      `task_containers: [workspace, tasks]`, no 7,505 references, no 666 files
- [ ] the ordering constraint — migrate, generate, **then** remove the board — appears where a reader is
      about to violate it, not only in a summary
- [ ] `update.md` Step 3 routes to the guide when the update crosses a major version
- [ ] the guide names the quiescence rule from AC-8 and the `task_containers` decision from AC-6
- [ ] the canon states that a major release without a migration guide is incomplete
- [ ] **R2** — the guide names `build.*` as something the operator edits by hand. `update.md` lists it
      under *"Project sections (preserve)"*, so a receiving project keeps a `build.verify` pointing at a
      path that no longer exists. This is F1's own class arriving a second time, through the update path
      this phase is repairing

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
- [ ] **R2 — reported, never matched.** Widening `LEGACY_ID` would edit an identifier rule, which §7 DoF
      forbids. `TASK_DIR` requires `__` and this corpus is uniform only by accident, so the single-
      underscore form is surfaced as unresolved
- [ ] **R2** — the migration guide tells the operator that an unresolved directory may be **renamed by
      hand** to the recognized grammar. The tool never normalizes; an accountable person may resolve. Same
      shape as the `UNDECLARED` ruling, and it keeps the report from being a dead end
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

- [ ] **R3 — no README template ships.** `update.md` and `init.md` carry a step that creates `team/`
      **together with its first profile**, so the directory never exists unexplained and needs no file to
      explain it
- [ ] the step runs **before the first durable write**
- [ ] `.tfw/templates/team/profile.md` carries the short orientation in its guidance comment — what a
      profile is, that it is attribution and not authentication, and that the handle matches the filename.
      It does not restate the identity-field canon; `conventions.md` §§268, 290–296 owns that
- [ ] a project that skips it learns so from AC-9's self-check, not from a framework test it was never
      told to run

Gate: update a fixture with no `team/` and confirm the step fires and the self-check reports it.
Evidence: self-check output.

### AC-8: Migration reads a stable input  [F8]

- [ ] `read_board()` defaults to a committed revision; the working tree becomes the explicit opt-in
- [ ] **R2** — with no committed board — not a Git repository, or the path absent at `HEAD` — the run
      **refuses**, names the working-tree opt-in and prints the revision it tried. It never falls back
      silently: a printed notice is the thing nobody reads, and the silent live read is what AC-8 exists
      to remove
- [ ] **R2** — AC-3 and this criterion are one code path. Reading `--board` from the working tree while
      logging a revision would produce a false provenance statement, which is worse than either defect
- [ ] the guide states plainly: do not migrate while a participant is mid-gate
- [ ] the run records which revision it read

Gate: change the working-tree board during a run and show the result is unaffected.
Evidence: run log naming the revision.

### AC-9: One command answers whether the project is consistent with the release  [rec 9]

**R3 — the three checks collapse into one flag with a subject.** `gen_index.py` carries `--check` and
`--validate`, and `project_config.yaml` needs **five lines of comment** to keep them apart. Adding
`--doctor` as a third synonym is the failure, not the fix: when prose is required to distinguish your own
names, the names are wrong. The three answer three questions about three subjects, so the subject belongs
in the command.

```text
--check index      is the derived index current?
--check tasks      is each task's own state legal?        (was --validate)
--check project    is this project consistent with the release?
```

- [ ] one flag, three subjects; the disambiguating comment in `project_config.yaml` is **deleted**, not
      rewritten — it exists only because the names failed
- [ ] `build.verify` becomes `--check tasks`. This breaks the shipped `--validate` in every project that
      has it: today that is this repository and one consumer, both already being touched, and `2.0.0` is
      unreleased. The cost is near zero now and grows permanently after
- [ ] `--check project` reports on the payload, `team/`, the container configuration, retired keys and
      carrier validity
- [ ] it **reports and exits**: it repairs nothing, writes nothing, and is not authority
- [ ] each subject's output names what it did not check. `--check tasks` states that it does not answer
      index freshness — the fact the deleted comment used to carry, now said where it is read
- [ ] `--check project` is named in the migration guide as the last step

Gate: run on this repository and on a deliberately broken fixture; both outputs quoted.
Evidence: both runs.

### AC-10: The update path carries the technique that made it safe  [field report §3]

- [ ] `update.md` instructs diffing every local `.tfw/` file against the **pristine previous tag** before
      merging anything
- [ ] the reason is stated: this single check collapsed three declared manual merges to zero, including
      `conventions.md` with 212 changed lines
- [ ] **R2 — the text says *whose* tag.** The diff is against the **source** tree's previous tag. The
      first consumer had no TFW tags at all, so an operator told to diff against "the previous tag" looks
      for one their project never had and concludes the technique does not apply to them
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

> **R2 — this criterion has two halves and revision 1 conflated them.** A development fixture is what the
> executor builds against; acceptance evidence is what the owner produces. Neither substitutes for the
> other, and the executor can close only the first.

**Half one — the development fixture. The executor closes this.**

- [ ] a pre-2.0.0 external corpus is cloned **into the scratch directory** and the full
      `1.3.0 → 2.0.0-dirty.2` update is run against it. `KZ-IT-telegram-list` at `c919640` is authorized:
      its board sits at `tasks/README.md` under `## Board`, its four task directories carry mixed
      grammar, and it declares one container — F3, F4 and F6 in one fixture
- [ ] **the live consumer project is never written to.** It is the owner's, and a second agent writing
      into it is the F14 / TD-144 defect this task exists to end
- [ ] AC-2's routing is exercised here and nowhere else: `2.0.0-dirty → 2.0.0-dirty.2` does not cross a
      major, so a run against an already-migrated project skips the guide entirely
- [ ] the fixture is pointed at a **commit SHA**, not a tag — the tag is cut by the coordinator after
      review

**Half two — acceptance evidence. The owner closes this; the executor reports it unmet.**

- [ ] at least one real external project, updated by its own operator, completes with zero files
      hand-carried and zero edits inside `.tfw/`
- [ ] every local delta the first consumer had to invent — the board flags, the copied `team/README.md`,
      the tooling placement — is unnecessary
- [ ] the run records what was confusing, not only what worked
- [ ] **this repository is not admissible as a fixture for either half.** Every Phase A round ran here,
      which is why none of the ten findings was found

Gate: half one closes on the clone run, filed in `phase-aa/evidence/`. Half two closes on the owner's run,
filed at task root as `FIELD-REPORT__TFW-60__second_external_update.md`, matching its predecessor and
visible to Phases B and C.
Evidence: the executor authors the first and **not** the second. An RF claiming the external check passed
on the executor's own clone is the DoF pattern in a fifth form, and review must reject it.

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

### AC-15: AC-13 half two came back — four instructions name what the reader does not have  [DoD 19]  🆕 R4

**This is not a reopening.** Review revision 2 approved the work and held the phase open in the same
breath: *"AC-13 half two remains unmet and remains the owner's… the phase closes when a real external
project is updated by its own operator and the result is filed."* That run has now happened and its
report is filed. **The evidence the phase was waiting for arrived, and on four counts it is negative.**

[Field report 2](../FIELD-REPORT__TFW-60__second_external_update.md) — `innoforce-ai-first`,
`1.3.0 → 2.0.0-dirty.2`, 2026-08-28 — first confirms the phase achieved its purpose. The first consumer
spent a session reconstructing the order of operations; this one spent nothing. The manifest accounted
for every row, no directory went unrecognized, and the identity gate **refused** a bad actor rather than
accepting it: the operator wrote `actor: claude-code` and was told a provider family is not a writer.
That is a working gate, and none of what follows takes it back.

**Already tracked — not duplicated here.** The report's third finding is **TD-192**, filed by review
revision 2 with reasoning this criterion does not override. Its mechanism gap is **TD-193**, which the
same review called the highest-value item of its set. Both are addressed below by their own rows, not by
being restated.

**Verified by the coordinator at the source before this list was written:**

| Finding | Measurement |
|---|---|
| No agent-handle minting rule | `PROVIDER_FAMILIES` appears in `gen_index.py` and **zero times** in `.tfw/` prose |
| `bindings.yaml` undefined | **7** workflows instruct the reader to read it; **0** templates and **0** lines of `conventions.md` define it |
| Step 6 has no row for Claude Code commands | The table carries `.agent/workflows/tfw-*.md` and **not** `.claude/commands/tfw-*.md`. Both are byte copies of `.tfw/workflows/*.md` — identical md5 confirmed — and only the listed one is maintained |
| Reproduced live | `KZ-IT-telegram-list` at `2.0.0-dirty`, **work in flight**: six files still instruct agents to update a Task Board removed the day before. It has no `.agent/` directory, so the covered adapter was never exercised there and the uncovered one rotted. **Two external projects out of two** |

**The corrections:**

- [ ] **1 — an agent handle has a stated minting rule.** `templates/team/profile.md` gains an **agent**
      example beside the human one and one line of the rule; `conventions.md` §4 names the refused set and
      says whether `team/` grows per session. The report's operator reached a working handle by writing
      the obvious one, being refused, **reading the validator's source**, and inventing a suffix. A gate
      that refuses without naming what it accepts is the defect this release declared as its subject
- [ ] **2 — `.tfw/templates/bindings.yaml` ships with its schema**, and the step that creates `team/`
      writes it **when the second profile appears**. Today Step 3b creates one profile and stops; the
      first journal event naming an agent makes two, and every later session falls into *"no binding →
      ask one question"* permanently. A resolution mechanism that never executes is not a mechanism
- [ ] **3 — Step 6 gains the missing row and re-syncs rather than reports.**

      | Adapter | Source | Target | Status |
      |---|---|---|---|
      | Antigravity workflows | `.tfw/workflows/*.md` | `.agent/workflows/tfw-*.md` | present |
      | **Claude Code commands** | `.tfw/workflows/*.md` | **`.claude/commands/tfw-*.md`** | **missing — add** |

      Re-copy only the `tfw-*` entries the payload provides and touch nothing else: a project's own
      commands sit beside them — `kz-release.md`, `kz-stats.md` in the telegram project — and are not
      ours. That bound already exists in this step for Codex skills; it is applied to the others rather
      than invented
- [ ] **4 — after Step 6 no file in the adapter layer carries retired vocabulary.** The check is the one
      the report used and takes seconds: `grep -rl 'Task Board' .claude .agent .agents AGENTS.md CLAUDE.md`,
      run against the same retired-term register the payload files already face
- [ ] **5 — `installed_from: <source>@<tag>` is written beside `tfw.version`** at Step 7. A local unpushed
      tag is unreachable from `tfw.upstream`, so the next update clones the remote, finds the older
      payload and reports that all is well. One key answers *where did this actually come from*

**Two tracked items promoted into this pass rather than left in the register:**

- [ ] **6 — TD-193, the path-check reach.** Two independent sources now name the same mechanism: the
      reviewer called it *"the mechanism gap that let TD-192 and TD-194 survive"*, and the report's third
      finding survived for exactly that reason — *"тест покрывает адаптеры и не покрывает прозу самой
      нагрузки"*. Extend the check to **every path any payload file names, in both reference forms** —
      `.tfw/templates/X` and bare `templates/X`. Follow the shape the reviewer named and the executor
      already proved on retired wordings: a registry, a stated reach, a demonstrated failing branch.
      TD-194's five stale glossary paths close as a side effect
- [ ] **7 — TD-192, and the owner asked for it now.** The reviewer's objection is sound and is not
      overridden: swapping the filename leaves a rule that **nine of its own twenty subjects contradict**,
      and after the move no Markdown template demonstrates `lower_snake_case` at all. **So fix the rule,
      not the example.** §10.4 states the convention that actually holds — an artifact template carries
      its artifact's name, everything else is `lower_snake_case` — and then a true example exists to give.
      That satisfies the owner's *"fix it now"* and the reviewer's *"do not buy a patch and leave the rule
      wrong"* with one edit instead of two decisions

**The owner's ruling on adapters, 2026-08-28 — recorded because it settles a standing contradiction.**

Copies are the model and they stay. Skills and commands are **byte-identical copies placed where each
tool expects them, in the form that tool knows** — never thin references. The executor for this phase is
Claude Code and therefore knows where Claude Code looks; place them so that after an update every project
finds them in the right place. This confirms S32 and S33 and closes the question the second report reopened.

- [ ] **8 — `.tfw/adapters/claude-code/README.md`:36 is corrected.** It reads *"Commands never duplicate
      workflow content — they reference it"*, and this repository's own `.claude/commands/tfw-plan.md` is
      a byte-identical 187-line copy. **We ship a rule we deliberately do not follow.** The README states
      the real model: full copies, placed per tool convention, re-synced by Step 6, kept in the same commit
      as the source. A rule nobody follows is worse than no rule — it teaches the reader to distrust the
      ones that are true

Gate: each line closes on command output. For 3 and 4 the proof is a fixture whose adapter copies are
stale before the step and clean after, with the `grep` returning zero. For 7, the rule is read back
against all twenty templates and contradicts none.
Evidence: regenerated at a pinned snapshot.

> **Why no amendment.** Findings 1, 2, 3 and 4 each fail DoD 19's last clause — *every instruction the
> release gives names something the receiving project actually has* — as it already stands. Nothing new
> is claimed. What the second report shows is that Phase AA drew its boundary one layer too small:
> `.tfw/` is the payload, but the adapter layer is also delivered, also instructs agents, and was
> measured by nothing.


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
- **Before adding any file, look for the rule already in the repository.** `templates/research/`,
  `templates/evidence/` and `templates/review/` had settled the template-directory question long before
  this phase; the coordinator proposed `team_readme.md` without looking, and an underscore standing in for
  a directory separator is what that oversight looks like on disk.
- **`tasks/BOARD-SNAPSHOT.md` is recorded as debt, not fixed.** Its SCREAMING-KEBAB name matches nothing
  else in the tree, and renaming it would break the links Phase A established days ago. Name it in RF §6
  so it is a decision rather than an oversight.
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
- ❌ **R2 — AC-13's acceptance half reported as met by the executor.** The clone is a development
  fixture. Only the owner's real run closes half two
- ❌ **R2 — the live consumer project written to by this phase.** It belongs to its owner
- ❌ **R3 — a new file created where an existing document should have gained a line.** Every artifact this
  phase adds must name the responsibility it absorbs. Two proposed files failed that test and were
  withdrawn; a third arriving the same way is the same defect
- ❌ **R3 — a name that needs prose to distinguish it from its neighbour.** The `--check` / `--validate` /
  `--doctor` collision is the worked example: the five-line comment in `project_config.yaml` was the
  symptom, and deleting the comment without fixing the names would have hidden it
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
