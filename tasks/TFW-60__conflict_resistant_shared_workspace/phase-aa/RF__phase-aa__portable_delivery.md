# RF — TFW-60 / Phase AA: Portable Delivery

> **Date**: 2026-08-27
> **Author**: Claude Code (Executor), `actor: saubakirov`, `via: claude`
> **Status**: 🟢 RF — Complete, with AC-13 half two reported **unmet**
> **Parent HL**: [HL-TFW-60](../HL-TFW-60__conflict_resistant_shared_workspace.md)
> **Phase HL**: [HL Phase AA](HL__phase-aa__portable_delivery.md)
> **TS**: [TS Phase AA](TS__phase-aa__portable_delivery.md) at **revision 3**
> **ONB**: [ONB Phase AA](ONB__phase-aa__portable_delivery.md) — eight blocking questions answered
> **Pinned at**: `1079020`. Two files unrelated to this phase (TFW-55, TFW-54) stay dirty in
> the working tree and are excluded from every commit — ONB Risk 6 ruling.

---

## 1. What Was Done

Three commits. Every rename is recorded as a rename.

| Commit | What |
|---|---|
| `f14f744` | the seven moves, and everything that names their result |
| `80c2ed5` | the profile template cut to its own job |
| `1079020` | two findings the external fixture produced |

### Created — 1

| Path | What it is |
|---|---|
| `.tfw/migrations/2.0.0.md` | the migration procedure, written for a project that is not this one |

**Two files the TS withdrew at R3 were not created**, and their responsibilities went
somewhere that already existed: the `team/` README template (the profile template's guidance
comment carries the orientation, and `team/` is now created together with its first profile,
so an unexplained directory never appears) and `.tfw/scripts/README.md` (`--help` says how,
the guide says when, `conventions.md` says where).

### Moved — 7, all `git mv`, history verified to follow

| From | To |
|---|---|
| `docs/scripts/gen_index.py` | `.tfw/scripts/gen_index.py` |
| `docs/scripts/migrate_board.py` | `.tfw/scripts/migrate_board.py` |
| `docs/scripts/test_gen_index.py` | `.tfw/scripts/test_gen_index.py` |
| `docs/scripts/test_migrate_board.py` | `.tfw/scripts/test_migrate_board.py` |
| `.tfw/templates/team_profile.md` | `.tfw/templates/team/profile.md` |
| `.tfw/templates/journal_event.md` | `.tfw/templates/journal/event.md` |
| `.tfw/templates/topic_file.md` | `.tfw/templates/knowledge/topic.md` |

`git log --follow` returns 8 commits for `gen_index.py`, 5 for `migrate_board.py`, 3 for
`team/profile.md`, 3 for `journal/event.md`, 5 for `knowledge/topic.md`.

### Modified — 25

| Group | Paths | What changed |
|---|---|---|
| Payload tooling | `.tfw/scripts/gen_index.py`, `.tfw/scripts/migrate_board.py` | marker-based root resolution; `--check {index,tasks,project}`; board locator and committed-revision default on one code path; unmatched directories reported; key-naming validator; ASCII messages; tolerant streams |
| Payload tests | `.tfw/scripts/test_gen_index.py`, `.tfw/scripts/test_migrate_board.py` | +33 tests; the migration fixture is now a Git repository so every existing test runs through the new default |
| Normative | `.tfw/conventions.md`, `.tfw/glossary.md`, `.tfw/project_config.yaml`, `.tfw/workflows/init.md`, `.tfw/workflows/knowledge.md` | payload paths; four new canon sections; the `build` block's five-line comment deleted |
| Update path | `.tfw/workflows/update.md` | Step 3 guide routing, Step 3a pristine-tag diff, the two decisions, the `team/` step, local-source form, Step 8 self-check |
| Session naming | `.tfw/workflows/plan.md` | `Step 0` removed; naming is step 3 of Step 4, after the identifier exists |
| Templates | `.tfw/templates/status.md`, `.tfw/templates/project_config.yaml`, `.tfw/templates/team/profile.md` | quoted example + worked example; a real `verify` command; the profile comment cut to its own job |
| Adapter sources | `.tfw/adapters/claude-code/CLAUDE.md.template`, `.tfw/adapters/claude-code/README.md`, `.tfw/adapters/antigravity/README.md` | TD-11 in all three, not one |
| Docs tooling | `docs/scripts/gen_docs.py`, `docs/scripts/test_integration.py` | cross-directory import bootstrap; +7 tests |
| Release surface | `.tfw/VERSION`, `.tfw/CHANGELOG.md`, `README.md` | `2.0.0-dirty.2`, the entry, the payload path |
| Project docs | `team/README.md` | the template link the move would have broken |
| Adapter copies | `.claude/commands/tfw-{init,update,plan,knowledge}.md`, `.agent/workflows/tfw-{init,update,plan,knowledge}.md` | re-synced, verified byte-identical |

**Deviations from the TS's Affected Files, both raised in the census before acting:**

- `docs/mkdocs.yml` was listed and **needed no change** — `gen-files` runs
  `scripts/gen_docs.py` relative to `docs/`, which the move does not touch. Modify is 25, not
  26. Verified by `mkdocs build` exit 0.
- The three `.agents/skills/` entries were listed and **needed no change** — Codex skills
  route by path and do not copy workflow content. Verified: all 11 byte-identical to
  `.tfw/adapters/codex/skills/`, and none of the five that name a template names a moving one.
- Four files the TS's table does not enumerate were modified: `.tfw/workflows/knowledge.md`
  and its two copies, plus `team/README.md`. All four are reached only through R3's own
  template moves. Raised in [census.md](evidence/census.md) § "Group appearing"; no limit
  crossed at 25 of 30.
- `.tfw/templates/project_config.yaml` was modified beyond a path reference: `build.verify`
  became a real command instead of a placeholder, because a receiving project can run it from
  the moment the payload lands.

## 2. Key Decisions

| # | Decision | Why |
|---|---|---|
| D1 | Root resolution walks upward for `.tfw/`, skipping any path containing `.upstream` | `update.md` Step 0 clones a full `.tfw/` into `.tfw/.upstream/`, which satisfies the marker. Without the skip, a tool run from inside staging would generate a project's index from the upstream clone — silently, with a plausible-looking result |
| D2 | `iter_unmatched_task_dirs()` as an additive sibling, not a changed return type | `iter_task_dirs` is called by `gen_docs.py`, `migrate_board.py` and the tests. A tuple return breaks all three for no gain |
| D3 | `--board` / `--board-heading` are flags, not configuration keys | Relocating a board is a fact about one run of a once-per-project act. A key read forever to answer a question asked once is surface with no reader |
| D4 | A new reconciliation class, `board-only, directory unresolved` | A row whose directory exists but whose *name* the grammar rejects is neither matched nor board-only. Reusing either would have made the manifest assert something false, which is the defect being fixed |
| D5 | The unresolved reason talks about the name and nothing else | The only fact available is the directory name. A reason about whether work happened is a claim the source never carried |
| D6 | The migration fixture became a Git repository, rather than passing `--working-tree` everywhere | Since the committed revision is now the default, a non-repository fixture would leave the path every real project takes exercised by nothing — a check reported as passing that never ran |
| D7 | Runtime messages are ASCII; content is not | Both reach a console whose codepage nobody chose. A message can be rewritten; a verbatim board block cannot, so streams are made tolerant instead. Enforced as a class by a test, not fixed occurrence by occurrence |
| D8 | The index names its own generator by resolved path | A project that placed the tools elsewhere gets an index naming a command it can actually run. Still deterministic: the same tree produces the same bytes |
| D9 | `update.md` stayed under the 1200-word ceiling by deleting duplication, not required content | Step 3a *measures* which files are customized, so the "typically safe" and "requires merge" lists were guesses standing where a measurement now exists. 835 → 1165 words with five ACs added |
| D10 | `team_readme.md` was not created at all, and the profile template shrank | The ONB's naming catch (`team_README.md` breaks §10.4) was the small answer. R3 asked the larger question, and the same duplication of `conventions.md` sat in the profile template's comment. 50 lines → 33 |
| D11 | AC-13's fixture was pointed at a commit SHA, not a tag | Q3 ruling (b). `git archive <sha>` exercises the same mechanics as a tag; a tag adds a name, and asserting releasability is the reviewer's finding |

## 3. Acceptance Criteria

| AC | Verdict | Where |
|---|---|---|
| AC-1 — tooling ships inside the payload | ✅ | E1–E5. Every gate hit classified; the depth test run at three placements |
| AC-2 — a major release ships a migration guide | ✅ | E6–E10 |
| AC-3 — migration finds a board wherever the project keeps it | ✅ | E11–E13 |
| AC-4 — an unmatched directory is reported, never described | ✅ | E14–E18, on the exact corpus that produced the finding |
| AC-5 — a person can hand-author the carrier correctly | ✅ | E19–E22 |
| AC-6 — `task_containers` is presented as a decision | ✅ | E23–E24 |
| AC-7 — `team/` is delivered, not assumed | ✅ | E25–E27 |
| AC-8 — migration reads a stable input | ✅ | E28–E32 |
| AC-9 — one command answers project consistency | ✅ | E33–E38 |
| AC-10 — the update path carries the technique that made it safe | ✅ | E39–E41 |
| AC-11 — shipped instructions name files that exist | ✅ | E42–E44 |
| AC-12 — the session name carries the task once it exists | ✅ | E45–E46 |
| **AC-13 half one — development fixture** | ✅ | E47–E50 |
| **AC-13 half two — acceptance evidence** | ❌ **UNMET** | E51. **The executor cannot close this.** See below |
| AC-14 — the release describes what shipped | ✅ | E52–E57. The tag is the coordinator's act (E53) |

### AC-13 half two is unmet, and this is the phase's declared outcome

The declared outcome of Phase AA is *a project other than this one completes the update from
the payload alone*. What was produced is a **development fixture**: a clone in a scratch
directory, driven by the same agent that wrote the code. It built AC-2, AC-3, AC-4, AC-6 and
AC-8 against a real corpus, and it found three defects nothing here could have found. It is
not acceptance evidence, because the point of DoD 19 is an operator who is not the author.

Reported unmet and handed back, per the ONB Q1 ruling. What closes it: the owner updating at
least one real external project, filed at task root as
`FIELD-REPORT__TFW-60__second_external_update.md`.

## 4. Verification

- **Lint** (`python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only`): **254 tests
  collected**, no collection errors
- **Tests** (`python -m pytest .tfw/scripts/ docs/scripts/ -q`): **253 passed, 1 skipped** in
  303 s. Baseline before the phase: **220 passed, 1 skipped**. Net +33
- **Verify** (`python .tfw/scripts/gen_index.py --check tasks`): **53 tasks validate against
  the closed schema**, exit 0
- **`--check project`**: exit 0 — version `2.0.0-dirty.2`, 1 participant, creates in
  `workspace`, resolves across `[workspace, tasks]`
- **`mkdocs build --config-file docs/mkdocs.yml`**: exit 0, built in 264 s. This is the gate
  for `gen_docs.py`'s cross-directory import, which mkdocs runs with `docs/` as its config
  root
- **Adapter sync**: `cmp` over all 22 workflow copies and 11 Codex skills → all identical
- **`update.md` word count**: 1165, under the §11 ceiling of 1200

**Checks that failed first, then passed** — recorded because a check whose failing branch was
never taken is not a check:

| Check | Failed on | Then |
|---|---|---|
| `test_every_path_an_adapter_source_names_resolves` | the three real adapter sources naming `.tfw/workflows/research.md` | passes after the fix |
| `test_every_path_an_installed_adapter_copy_names_resolves` | four copies naming the pre-move template paths | passes after the sweep |
| `test_every_runtime_message_is_ascii` | **five** real occurrences, including two of my own (`✗`, `·`) | passes |
| `test_the_status_template_examples_parse_and_validate` | written against the template before it was fixed | passes |
| `test_a_manifest_containing_the_project_own_characters_prints` | reproduced the fixture's `UnicodeEncodeError` | passes |
| `test_the_adapter_path_check_actually_fires` | its own broken-entry fixture, by construction | passes |

## 5. Evidence

See [EV file](evidence/EV__phase-aa__portable_delivery.md) for evidence details.

Evidence verdict: **58/60 VERIFIED, 1 DEFERRED, 0 BLOCKED, 1 N/A**

The DEFERRED item is E51, AC-13 half two, with the specific blocker named. The N/A is E53,
the `v2.0.0-dirty.2` tag, by the coordinator's Q3 ruling.

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `KNOWLEDGE.md` | 22 | naming | Names `docs/scripts/gen_index.py` in the architecture table. The known exception from the ONB Q5 ruling (b): owned by `/tfw-docs` under the D37 split, so the executor does not write it. **AC-1's gate names it explicitly** so this RF does not report a green gate over a red one. Closes by `/tfw-docs` after approval |
| 2 | `tasks/BOARD-SNAPSHOT.md` | — | naming | SCREAMING-KEBAB, matching nothing else in the tree. **Deliberately not renamed** — Phase A's links resolve to it and a rename would break them days after they were established. Recorded per TS §6 so it is a decision rather than an oversight |
| 3 | `.tfw/workflows/init.md`, `.tfw/workflows/plan.md` | whole file | style | **1,897 and 1,598 words** against the §11 design ceiling of 1,200. Both were already over before this phase (1,821 and 1,501); this phase added 76 and 97. `update.md` was brought *under* the ceiling by deleting duplication rather than by cutting required content, and the same is available here — `init.md`'s tutorial asides and `plan.md`'s worked pseudocode are the candidates. Not attempted: neither file's overrun is in this phase's scope, and cutting a workflow is a change reviewers should see on its own |
| 4 | `.tfw/scripts/gen_index.py` | 1150–1230 | duplication | `check_project` re-implements the `build.*` path check that `--check tasks` does not have, and `gen_docs.py:_find_root` restates `find_project_root` in ten lines. The second is a genuine bootstrap — `gen_docs` needs the root to locate the module it would import the function from — and the first is small. Both are the honest kind of duplication; recorded so a later reader does not read them as oversights |
| 5 | `.tfw/scripts/gen_index.py` | — | missing-test | `--check project` does not report a **retired framework file** still sitting in a project's `.tfw/` (the fixture found `templates/topic_file.md`). The migration guide now finds them by command. Not added to the check: payload *completeness* and payload *minimality* are two different claims, and the second needs a manifest of what the release ships, which does not exist |
| 6 | `docs/scripts/test_integration.py` | 248 | perf | The full `docs/scripts/` suite takes ~290 s of the 303 s total, almost all of it `mkdocs` builds inside tests. The payload suite alone is 15 s. A receiving project runs only the payload suite, so this does not reach them — but it makes this repository's own gate slow enough to be skipped |
| 7 | `.tfw/CHANGELOG.md` | 200–265 | style | The `2.0.0-dirty` entry's migration code fence still names `docs/scripts/`, correctly — it is a record of that tag. The new entry says so and points at the guide. A reader who scrolls to the fence without reading the note above it can still copy a dead command. The structural fix would be a per-release "superseded by" marker, which is a CHANGELOG-format change and not this phase's |

## 7. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | philosophy | When prose is required to distinguish two of your own names, the names are wrong — and deleting the prose without fixing the names hides the symptom. The owner applied this to `--check`/`--validate`/`--doctor`, where a five-line config comment had been accepted as the fix | Owner, via TS R3 | High |
| 2 | philosophy | Every artifact a phase adds must name the responsibility it absorbs; a new file where an existing document should have gained a line is the defect. Two proposed files were withdrawn on this test after the owner asked the larger question | Owner, via TS R3 | High |
| 3 | process | A development fixture and acceptance evidence are different things, and an AC that conflates them cannot be closed honestly. The executor builds against the first; only an operator who is not the author produces the second | Coordinator, ONB Q1 answer | High |
| 4 | process | The live consumer project must never be written to by an agent working in this repository — it belongs to its owner, and a second agent writing into it is the defect TFW-60 exists to end | Coordinator, ONB Q1 answer | High |
| 5 | constraint | `KZ-IT-telegram-list` is the owner's real project and the only external TFW consumer. Its pre-update commit `c919640` is a reusable fixture: TFW 1.3.0, board at `tasks/README.md` under `## Board`, four task directories with mixed identifier grammar, one container | Owner's field report + this run | High |
| 6 | environment | The owner's machine runs a console codepage that is not UTF-8, so any shipped tool printing project content must not assume UTF-8 stdout. This is why the migration guide's first command died and why no test here could have caught it | This run, on the owner's machine | High |
| 7 | philosophy | A rename that looks like a correct catch may still be the small answer. `team_README.md` → `team_readme.md` was right about the naming rule and wrong about the file existing at all | Owner, via TS R3 | Medium |

## 8. Strategic Insights (Execution)

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | The owner's instruction for this phase was *"подход изменился в целом в сторону качества архитектуры, а не фиксов ради фиксов"* — and it changed what the work is. Under a fix-oriented reading, AC-9 gets a third flag and AC-7 gets a README template, both closing their AC. Under the owner's reading, the third flag **is** the finding: three names for three questions about three subjects collapse into one flag, and the config comment that existed to tell two of them apart gets deleted rather than extended. **Implication:** an AC that names a symptom should be read as an invitation to find what the symptom is a symptom of. Phase AA ended up removing more surface than it added — 1 created against 2 withdrawn and 3 pulled out of a flat namespace — and that was the owner's correction, not the plan's | philosophy | User, 2026-08-27, on handing back the amended TS |
| S2 | Testing a delivery mechanism inside the repository that produces it is structurally blind, not merely incomplete. Every finding this phase closed came from one external run; four review rounds here produced none of them — and the reason is mechanical. `parents[2]` resolves correctly from `.tfw/scripts/` **by coincidence**, so the depth defect would have passed every test written here. **Implication:** for any capability whose subject is *another project*, the fixture must be another project, and the phase's own gate should say so in a form an executor cannot satisfy locally. AC-13's split into a development half and an acceptance half is the shape that survives | process | Coordinator, ONB Q1 answer, extended by this run |
| S3 | A check that reports and exits is cheap to trust and cheap to add; the moment it repairs anything it becomes a second authority over state that a task's own file already owns. `--check project` was deliberately built as a reporter — and the constraint paid off in an unexpected place: because it writes nothing, `test_no_check_subject_writes_anything` could byte-compare the entire tree before and after all three subjects, which is a much stronger assertion than any per-check test. **Implication:** the non-authority constraint is not only a safety rule, it is what makes the check testable as a class | philosophy | PV 1 (one authoritative owner per truth type), applied |

## 9. Diagrams

### The payload boundary, before and after

```text
BEFORE — the release named files the payload did not carry

  /tfw-update copies  ──►  .tfw/  ── rules · templates · workflows · adapters
                                       │
                                       │  these were REQUIRED but OUTSIDE:
  docs/scripts/gen_index.py     ✖ ─────┤    conventions.md names the path
  docs/scripts/migrate_board.py ✖ ─────┤    CHANGELOG says "run this"
  team/README.md                ✖ ─────┤    no step creates team/
  a migration guide             ✖ ─────┘    does not exist

  and the tools resolved the root as parents[2], so the DEPTH was load-bearing:
  a project placing them elsewhere had to edit .tfw/ and forfeit clean updates


AFTER — everything the release asks for is inside the payload,
        or already in the receiving project

  .tfw/
   ├── scripts/          gen_index.py · migrate_board.py + their tests
   │                     root found by walking upward for .tfw/  ── ANY depth
   ├── migrations/2.0.0.md   the procedure, for a project that is not this one
   ├── templates/
   │    ├── team/profile.md      ──► team/<handle>.md
   │    ├── journal/event.md     ──► {task}/journal/<name>.md
   │    └── knowledge/topic.md   ──► knowledge/<topic>.md
   └── workflows/update.md   Step 3  ──► the guide, when a major is crossed
                             Step 3a ──► diff against the source's pristine tag
                             Step 8  ──► --check project

  withdrawn rather than created:  team/ README template · scripts/README.md
                                  (each duplicated a document that already existed)
```

### `--check`: three subjects, one flag

```text
                       ┌─────────────────────────────────────────────┐
                       │  BEFORE: two flags + a 5-line comment       │
                       │  telling them apart, and a third proposed   │
                       └─────────────────────────────────────────────┘
                                          │
                                          ▼
   gen_index.py --check ─┬─ index    is the derived view current?
                         │             never a gate on a task transition
                         │
                         ├─ tasks    is each task's own state legal?
                         │             THE BUILD GATE. task-local only, so it
                         │             cannot be blocked by a stale index
                         │
                         └─ project  is this project consistent with the release?
                                       payload · team/ · containers · retired
                                       keys · version marker · carrier validity

   every subject:  reports and exits · writes nothing · is authority over nothing
                   and states what it did NOT check
```

### How a board reaches task-local state

```text
  --board PATH ────────┐
  --board-heading H ───┼──►  read_board()  ──►  git show REV:PATH   ◄── ONE code path.
  --board-rev REV ─────┤        │                                       Reading the path
  (default: HEAD)      │        │                                       from the working
  --working-tree ──────┘        │                                       tree while logging
                                │                                       a revision would be
                                ▼                                       false provenance.
                          parse_board(text, H)
                          (parser untouched: it already
                           read a 9-column table)
                                │
                                ▼
                          reconcile()  ──► ONE classification, read by both consumers
                                │
        ┌───────────────────────┼───────────────────────┬──────────────────────┐
        ▼                       ▼                       ▼                      ▼
     matched              board-only            board-only,            directory-only
   row + directory      no directory         directory unresolved      no row
        │                  at all           name rejects the grammar        │
        ▼                     ▼                       ▼                     ▼
   status.md written    snapshot: Backlog     NO state file.          reported
   (unless terminal      / Absorbed           Reported as unresolved,
    or absorbed)                              in BOTH the manifest and
                                              the index, for the same
                                              stated reason.
                                              A person may rename it;
                                              no tool ever will.
```

---

*RF — TFW-60 / Phase AA: Portable Delivery | 2026-08-27, pinned at `1079020`*
