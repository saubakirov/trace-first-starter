# RF — TFW-60 / Phase AA: Portable Delivery

> **Date**: 2026-08-27
> **Author**: Claude Code (Executor), `on_behalf_of: saubakirov`, `via: claude`
> **Status**: 🟢 RF — **revision 3**, adding §11 for the R4 corrective pass. Written after the
> phase was closed `DONE`, because the owner's own closing outcome names its absence:
> *"the pass has no RF of its own."* Closes **TD-199**
> **Parent HL**: [HL-TFW-60](../HL-TFW-60__conflict_resistant_shared_workspace.md)
> **Phase HL**: [HL Phase AA](HL__phase-aa__portable_delivery.md)
> **TS**: [TS Phase AA](TS__phase-aa__portable_delivery.md) at **revision 4** — §11 answers AC-15
> **ONB**: [ONB Phase AA](ONB__phase-aa__portable_delivery.md) — eight blocking questions answered
> **REVIEW**: [first](REVIEW__phase-aa__portable_delivery.md) 🔄 REVISE · [rev2](REVIEW__phase-aa__portable_delivery__rev2.md) ✅ APPROVE · [rev3](REVIEW__phase-aa__portable_delivery__rev3.md) ✅ APPROVE by owner ruling over the reviewer's REVISE
> **Field report**: [second external update](../FIELD-REPORT__TFW-60__second_external_update.md) — filed verbatim, not authored here
> **Pinned at**: `1079020` for the phase's measurements; revision 2's own work is measured at
> its own commit and says so per item. Two files unrelated to this phase (TFW-55, TFW-54) stay
> dirty in the working tree and are excluded from every commit — ONB Risk 6 ruling.

---

## 1. What Was Done

Three commits. Every rename is recorded as a rename.

| Commit | What |
|---|---|
| `f14f744` | the seven moves, and everything that names their result |
| `80c2ed5` | the profile template cut to its own job |
| `1079020` | two findings the external fixture produced |
| `0215aca` · `440d6fd` | RF, EV and evidence; then the parser claim replaced by a measurement |
| revision 2 | the review's three items, plus four the review's own generalization surfaced |

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

`git log --follow` at the declared pin `1079020` returns **9** commits for `gen_index.py`,
**6** for `migrate_board.py`, 3 for `team/profile.md`, 3 for `journal/event.md`, 5 for
`knowledge/topic.md`. Revision 2 corrects the first two: they were 8 and 5, the values at
`80c2ed5`, taken before the third commit and then reported against a later pin. TS §6 makes
the pin a rule and a measurement has to be taken at the commit it names.

### Modified — 25 by the census's method · 31 distinct paths in the table below

**Both numbers, because they count different things and the earlier heading gave one while
the table showed the other.** The census classifies the four scripts and three templates as
*moves* and excludes them from the modified count — 25 is that figure, it is the one measured
against the budget of 30, and it is the basis the coordinator approved. The table below then
lists those same files as rows, because they were modified as well as moved: 31 distinct
paths were touched in total.

Neither number is wrong; reporting only the first over a table showing the second is. The
review recorded this as D3, and the census's basis for the classification is where it
genuinely needs a coordinator ruling: the TS predicted the scripts would *"relocate rather
than get rewritten … cost a move and their path constants"*, and `gen_index.py` changed 507
lines, `migrate_board.py` 246. That prediction did not survive execution. It belongs in the
next phase's budget table, and this row is the pointer to it.

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
| D7 | Runtime messages are ASCII; content is not | Both reach a console whose codepage nobody chose. A message can be rewritten; a verbatim board block cannot, so streams are made tolerant instead. Enforced by a test over `print(`/`SystemExit(` spans rather than by fixing the occurrences one at a time — a heuristic with a stated reach, not a proof over every possible message |
| D8 | The index names its own generator by resolved path | A project that placed the tools elsewhere gets an index naming a command it can actually run. Still deterministic: the same tree produces the same bytes |
| D9 | `update.md` stayed under the 1200-word ceiling by deleting duplication, not required content | Step 3a *measures* which files are customized, so the "typically safe" and "requires merge" lists were guesses standing where a measurement now exists. 835 → 1165 words with five ACs added |
| D10 | `team_readme.md` was not created at all, and the profile template shrank | The ONB's naming catch (`team_README.md` breaks §10.4) was the small answer. R3 asked the larger question, and the same duplication of `conventions.md` sat in the profile template's comment. 50 lines → 33 |
| D11 | AC-13's fixture was pointed at a commit SHA, not a tag | Q3 ruling (b). `git archive <sha>` exercises the same mechanics as a tag; a tag adds a name, and asserting releasability is the reviewer's finding |

## 3. Acceptance Criteria

| AC | Verdict | Where |
|---|---|---|
| AC-1 — tooling ships inside the payload | ✅ | E1–E5. Every gate hit classified; the depth test run at three placements |
| AC-2 — a major release ships a migration guide | ✅ | E6–E10 |
| AC-3 — migration finds a board wherever the project keeps it | ✅ | E11–E13. The parser's untouchedness is measured: one changed line, the locator |
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
| `test_every_runtime_message_is_ascii` | **five** real occurrences, including two of my own (`✗`, `·`) | passes. **What it enforces**, stated so its silence is not over-read: it scans payload script lines, toggles on a `print(` or `SystemExit(` and resets at a line ending in `)`, then rejects non-ASCII inside that span. That covers a literal handed to a print or a raise — every case in these two files — and not a message assembled into a variable and printed later |
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
| 8 | `docs/scripts/test_integration.py` | 428–470 | missing-test | **`test_no_normative_file_states_a_retired_rule` does not scan the payload scripts' own comments and docstrings**, and the stale `--validate` docstring at `.tfw/scripts/test_gen_index.py:741` was found by hand rather than by it. The gap is deliberate: a comment explaining that a flag was retired legitimately names it, and no mechanical rule separates that from a docstring that still instructs — a line-proximity heuristic or a line-number allowlist would both rot. The shipped harm is bounded, because a receiving project reads templates and workflows and never reads these test files. Candidate fix if it recurs: require every retired name in payload code to sit inside a span the file marks as historical, which means adding such a marker convention first |

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
| 8 | process | **A rule corrected in the canon is not corrected until every shipped copy of its old wording is found**, and the mechanical form of the check is to grep the *old sentence* rather than the concept. The two files a reviewer reads were right; the missed one was the carrier template a receiving project hand-authors from. Running that grep in revision 2 found three more instances of the same class, one of them in code the same phase had just edited | Reviewer, REVIEW TFW-60/AA §7 | High |
| 9 | process | **A review item and the class it belongs to are not the same size.** The review filed one file and one line; generalizing the finding it named turned up four more sites and one deliberate exemption worth recording. Closing the item without running its own stated mechanic would have left the class open and looked complete | Reviewer's own fact candidate, applied in revision 2 | High |

## 8. Strategic Insights (Execution)

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | The owner's instruction for this phase was *"подход изменился в целом в сторону качества архитектуры, а не фиксов ради фиксов"* — and it changed what the work is. Under a fix-oriented reading, AC-9 gets a third flag and AC-7 gets a README template, both closing their AC. Under the owner's reading, the third flag **is** the finding: three names for three questions about three subjects collapse into one flag, and the config comment that existed to tell two of them apart gets deleted rather than extended. **Implication:** an AC that names a symptom should be read as an invitation to find what the symptom is a symptom of. Phase AA ended up removing more surface than it added — 1 created against 2 withdrawn and 3 pulled out of a flat namespace — and that was the owner's correction, not the plan's | philosophy | User, 2026-08-27, on handing back the amended TS |
| S2 | Testing a delivery mechanism inside the repository that produces it is structurally blind, not merely incomplete. Every finding this phase closed came from one external run; four review rounds here produced none of them — and the reason is mechanical. `parents[2]` resolves correctly from `.tfw/scripts/` **by coincidence**, so the depth defect would have passed every test written here. **Implication:** for any capability whose subject is *another project*, the fixture must be another project, and the phase's own gate should say so in a form an executor cannot satisfy locally. AC-13's split into a development half and an acceptance half is the shape that survives | process | Coordinator, ONB Q1 answer, extended by this run |
| S3 | A check that reports and exits is cheap to trust and cheap to add; the moment it repairs anything it becomes a second authority over state that a task's own file already owns. `--check project` was deliberately built as a reporter — and the constraint paid off in an unexpected place: because it writes nothing, `test_no_check_subject_writes_anything` could byte-compare the entire tree before and after all three subjects, which is a much stronger assertion than any per-check test. **Implication:** the non-authority constraint is not only a safety rule, it is what makes the check testable as a class | philosophy | PV 1 (one authoritative owner per truth type), applied |
| S4 | **A phase that legislates against a failure mode is the most likely place to commit it.** This phase's own DoF names *"a check reported as passing that never ran"* in four forms, and its review found four claims stated wider than their evidence — mine. It rewrote the absolute `UNDECLARED` rule and left the sentence standing in the one copy a receiving project reads. It removed depth arithmetic from the tools and left it in the tools' own tests. None of these is carelessness in a different area; each is the phase's declared subject, reappearing in the place the author was not looking. **Implication:** the finding of a phase should be turned back on the phase before the RF is written — grep the retired string, re-measure the claim at the pin it declares, run the gate against the pre-fix file. Two of the four items above are things a five-minute sweep would have caught before review, and the sweep is now a test rather than an intention | philosophy | Reviewer + this revision |

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

## 10. Revision 2 — what the review returned, and what generalizing it found

REVIEW `440d6fd` returned 🔄 **REVISE** with three items. Two were in one file and one was a
set of four claims stated wider than their evidence. All are closed below.

The review's §7 fact candidate also named the **mechanical form** of the finding: *"grep the
old sentence, not the concept, before declaring the rewrite complete."* Running that grep
found three more instances of the same class that neither the RF nor the review had caught.
They are closed here too, because a review item and the class it belongs to are not the same
size.

### The review's three items

| # | Item | What was done |
|---|---|---|
| 1 | `.tfw/templates/status.md` stated the retired absolute `UNDECLARED` prohibition — verbatim the sentence `f14f744` rewrote in `conventions.md` §5 and `glossary.md` | Replaced with the two-act rule, citing §5 rather than restating its table. The release note's Canon entry now says the rule lives in **three** files and records that the third was missed on the first pass |
| 2 | Same file: *"the four keys that are never prose"* listed six | *"The six keys that are never prose."* Counted |
| 3 | Four claims looser than their evidence | **(a)** E47 carries the `__pycache__` caveat **at the row**, with the transcript's own `1` quoted and explained. **(b)** RF §1's `git log --follow` counts re-measured at the declared pin: **9** and **6**, not 8 and 5 — those were the values at `80c2ed5`, reported against a later pin. **(c)** E60 and RF §4 now state what `test_every_runtime_message_is_ascii` enforces — a `print(`/`SystemExit(` span scan that reaches a literal and not a message assembled into a variable. **(d)** `ac3_parser_untouched.txt` records **both** measurements, each re-derived here rather than copied: **40 → 45** whole-function with four differing code lines forming two replacements (signature, locator) and five added docstring lines, and **34 → 34** body-only with one replacement. Stating the second alone was the defect. The review reported 42 → 47 for the first; the gap is trailing blank lines under a different extraction method, and the artifact states its method and says so — a number taken from someone else's run is not one this artifact can vouch for |

### What generalizing item 1 found

| # | Where | What | Class |
|---|---|---|---|
| 4 | `.tfw/scripts/test_gen_index.py:741` | A docstring reading *"Driven through `gen_index.main(--validate)`, the command the build gate runs"* — naming a flag this phase retired, in a test whose call site the same phase updated. `sed` moved the arguments and left the prose | **Exactly item 1's class**, in my own code, and neither the RF nor the review caught it |
| 5 | `.tfw/scripts/test_gen_index.py:20`, `test_migrate_board.py:22` | `PROJECT_ROOT = Path(__file__).resolve().parents[2]` — depth arithmetic in the test files of the module that stopped depending on depth in this phase. Correct today by the same coincidence AC-1 exists to remove, and it breaks confusingly the moment a project relocates the tools. Now `find_project_root(Path(__file__))` | The review saw it — *"`parents[2]` survives only in a docstring and two test constants"* — and did not file it |
| 6 | `.tfw/CHANGELOG.md` | My own release note cited **`TD-11`**, an identifier `TECH_DEBT.md` does not carry; the historical TD-11 was an unrelated purged defect. The reviewer filed this as TD-191 with two options, one of which was *"drop the ID from the entry"* | Took the executor half: the label is dropped and why is stated. Registering the defect under a fresh ID is `TECH_DEBT.md`, which is not mine to write, so **TD-191 stays open** for that decision |
| 7 | `.tfw/CHANGELOG.md:168` — the `[2.0.0-dirty]` entry's *"normalizing it away is prohibited"* | **Deliberately not changed**, and classified rather than passed over silently. A changelog entry records what a release shipped, and `2.0.0-dirty` shipped the absolute rule. Rewriting it would make the record describe something that did not happen — the same P9 logic as the eleven provenance comments. Note it is a *paraphrase*, so the exact-string grep does not reach it; the broader `prohibited` grep does, which is why both were run | Recorded so the next person running this grep does not re-derive the exemption |

### The class is now detectable rather than remembered

`test_no_normative_file_states_a_retired_rule` checks a named registry of retired wordings —
currently the absolute `UNDECLARED` sentence, `--validate` and `--doctor` — against every
payload file that **instructs**: `templates/`, `workflows/`, `migrations/`, `conventions.md`,
`glossary.md`, `README.md`, `quickstart.md`, `compilable_contract.md`.

`CHANGELOG.md` is excluded, and the exclusion is a rule rather than a convenience: a
changelog records, and item 7 above is why that distinction has to live in the test rather
than in whoever reads its output.

**What it does not reach**, said here rather than left to be discovered: the payload scripts'
own comments and docstrings. A comment explaining that a flag was retired legitimately names
it, and no mechanical rule separates that from a docstring that still instructs — item 4 was
found by hand and would be found by hand again. The shipped harm is bounded, because a
receiving project reads templates and workflows and never reads these test files. Filed as
RF §6 observation 8 with the candidate fix and why it was not taken.

**Proven against the real defect, not against a fixture alone.** Run over
`440d6fd:.tfw/templates/status.md` it reports the retired sentence at line 92; run over the
corrected file it is clean. `test_the_retired_rule_check_actually_fires` covers the empty and
the negative case.

This is what the phase's own PV 1 citation asks for — *a rule that cannot reveal its own
violation is only advice*. The review's fact candidate is the rule; this is its enforcement
site.

### Not closed in this revision

**RF §1's `Modified — 25` versus 31 distinct paths.** The heading now states both numbers and
what each counts, so the RF no longer contradicts its own table. The underlying question is
the coordinator's and stays open: the TS predicted the scripts would *"cost a move and their
path constants"*, and they changed 507 and 246 lines. That is a budget-basis correction for
the next phase's table, exactly as the review placed it.

**AC-13 half two.** Unchanged and unchangeable here. The payload the owner will run against no
longer contradicts itself, which is what made taking this round cheap now rather than after a
tag.

---

## 11. The R4 corrective pass — `actor` removed until TFW-54

**Why this section exists, and why it is late.** Review revision 3 returned 🔄 REVISE with three
items, all record-keeping; the owner ruled them not worth a round and carried them as debt, then
closed the phase `DONE` with an outcome naming this gap in words: *"the pass has no RF of its
own."* Its first item is exact and I do not soften it:

> *"The Trust Protocol makes the RF the thing a review is conducted against; for the largest
> architectural change of the phase there is no declaration to test. In six months the reasoning
> that makes this defensible lives only in commit messages."*

That is right. A review that has to reconstruct the claim from a diff is not reviewing a claim.
This section is the declaration that should have existed at `b75bef1`, written now rather than
not at all, and it changes no verdict: rev3's APPROVE stands, and the reviewer's analysis stands
beside it unrewritten.

### 11.1 What was done

**Measured before the first edit** — [`census_r4.md`](evidence/census_r4.md), at `fd85b7c`.

| Group | Paths | AC-15 items |
|---|---|---|
| Payload code | `.tfw/scripts/gen_index.py` | 1, 2, 3, 8 |
| Payload tests | `.tfw/scripts/test_gen_index.py` | 1, 3, 8 |
| Templates | `journal/event.md`, `team/profile.md`, `REVIEW.md`, `project_config.yaml` | 1, 2, 4, 9 |
| **Created — 1** | `.tfw/templates/bindings.yaml` | 7 |
| Canon | `conventions.md`, `glossary.md`, `migrations/2.0.0.md` | 2, 4, 7, 8, 11 |
| Workflows — **8** | `handoff`, `init`, `plan`, `release`, `research/base`, `resume`, `review`, `update` | 1, 4, 5, 6, 7, 9 |
| Adapter source | `.tfw/adapters/claude-code/README.md` | 12 |
| Docs tooling | `docs/scripts/test_integration.py` | 6, 10 |
| Release surface | `.tfw/VERSION`, `.tfw/CHANGELOG.md`, `.tfw/project_config.yaml` | AC-14 |
| Adapter copies | 8 workflows × `.claude/commands/` + `.agent/workflows/` = 16 | 5 |

**Counts, both methods, because they differ and the difference is the point.** By owner ruling
S32 — byte-identical adapter copies excluded — **22 modified, 1 created**. By distinct paths
touched — **38**. S32 is the declared method and 22 is under the limit of 30; path-counting
crosses it. Raised in the census *before* any edit, under the return-to-coordinator rule, and
recorded here rather than resolved in my favour.

**A group appeared and was raised there too:** the previous pass modified four workflows, this
one eight, because seven of them restate `conventions.md`'s identity sentence verbatim. A
one-field removal reaching eight files is what that duplication costs.

### 11.2 Key decisions

| # | Decision | Why |
|---|---|---|
| **D10** | **`actor` is removed, not renamed and not given a naming convention** | The field held two unrelated jobs — *say who wrote this* and *make the filename unique* — and they contradict each other: a distinct writer needs a distinct value, a declared handle needs a profile. The report handed over a symptom with two branches, and both were the small answer. Blessing per-session handles would have shipped a naming convention over an unresolved contradiction. Naming a writer honestly needs a principal that delegates and answers to someone; TFW does not have one until TFW-54, so the field waits for the task that will |
| **D11** | **An `actor` already written is tolerated, never required, never rewritten** | Events are immutable and profiles are not — which is exactly how one consumer's gate went red permanently. Any rule about the field would either demand an edit to an immutable file or go red when someone tidies `team/`. So there is no rule: not a `team/` comparison, not a provider list, not a shape check. This is what makes the correction cost every project nothing |
| **D12** | **The two name shapes are deliberately indistinguishable** | `__saubakirov.md` and `__9f2c.md` match the same pattern. Nothing has to tell a historical handle from a new token, so nothing does, so no corpus needs classifying or migrating |
| **D13** | **Naming the token's one job removed machinery rather than adding any** | Uniqueness came from the second, so a collision could only be resolved by waiting for time to pass — a retry loop with sleeps. Uniqueness now comes from the token, so a collision is re-drawn and the clock is read once. `PROVIDER_FAMILIES` was deleted for the same reason: its only reader was the gate that is gone |
| **D14** | **Two registries for retired text, not one with exemptions** | A retired *wording* is wrong wherever it appears. A retired *term* is legitimate in prose narrating its retirement — `glossary.md` says the status legend moved when the board was removed — and never legitimate in a live instruction. One registry plus an exemption list would have buried that distinction |
| **D15** | **§10.4 was rewritten as a rule, not patched at its example** | Swapping the dead filename would have left a rule nine of its own twenty subjects contradict. The reviewer's revision-2 objection is quoted in the canon rather than overridden |

### 11.3 Acceptance criteria — TS §5 AC-15

| # | Item | Status | Evidence |
|---|---|---|---|
| 1 | Two identity fields; the filename's third component is an opaque token | ✅ | `EVENT_REQUIRED` drops `actor`; `EVENT_NAME` group renamed to `token`; `event_token()` is 4 hex chars deriving from nothing — asserted by `test_the_token_is_opaque_and_carries_no_identity` over the function's code with its docstring stripped |
| 2 | No agent profile, and the payload says so | ✅ | `team/profile.md`, `conventions.md` §4, `glossary.md`, `migrations/2.0.0.md` each state that `team/` holds people and why a writer is not named until TFW-54. `PROVIDER_FAMILIES` **deleted** — `test_the_provider_family_list_is_gone` |
| **3** | **An already-written `actor` is tolerated, never required, never rewritten** | ✅ | **0 events touched.** At the pass's pin `b75bef1`: **29 events, 28 carrying the field**, none edited. Re-checked 2026-08-29 after four later commits by other sessions — **all 29 still byte-identical**, and the five events written since carry no `actor`, so the new shape is in use and the old one is undisturbed. Both consumers validated read-only. [`ac15_actor_tolerated.txt`](evidence/ac15_actor_tolerated.txt) |
| 4 | The canon, templates and guide state the two-field model and when the third returns | ✅ | `conventions.md` §4, `templates/journal/event.md`, `glossary.md`, `migrations/2.0.0.md` |
| 5 | Step 6 gains the Claude Code row and re-syncs rather than reports | ✅ | Row is **first** in the table, because it was the one forgotten. The `tfw-*`-only bound applied to every row |
| 6 | After Step 6 the adapter layer carries no retired vocabulary | ✅ | 0 files. Now a test — `test_no_adapter_file_states_a_retired_rule` — over both registries, proved to fire |
| 7 | `.tfw/templates/bindings.yaml` ships with its schema | ✅ | Created; defined in `conventions.md` §4, where `glossary.md` already pointed and where nothing was |
| 8 | Per-phase journals are part of the model and are read | ✅ | `journal_dirs()`; three tests including two phases holding the same event name |
| 9 | `installed_from: <source>@<tag>` beside `tfw.version` | ✅ | `update.md` Step 7, `templates/project_config.yaml`, this repository's own config |
| 10 | TD-193 — every path any payload file names, in both forms | ✅ **and wider** | **Three** forms, not two: the bare filename with no directory was named by neither the TS nor the review, and is how §10.4's dead example survived four releases. 212 references scanned, 0 unresolved. TD-194 closed as a side effect |
| 11 | TD-192 — fix the rule, not the example | ✅ | §10.4 rewritten. Read back against all **20** templates: **0 contradicting** |
| 12 | The adapter README states the model that ships | ✅ | Copies **are** the model, with the two mechanisms that make it true rather than hopeful |

### 11.4 Verification

| Gate | Result |
|---|---|
| `pytest .tfw/scripts/ docs/scripts/ -q` | **260 passed, 1 skipped** |
| `mkdocs build` | exit 0 |
| `--check tasks` · `--check project` · `--check index` | exit 0 · exit 0 · exit 0 |
| Adapter copies vs sources | 0 drifted |
| Adapter layer, retired terms | 0 |
| Payload paths, three reference forms | 212 references, 0 unresolved |
| Naming rule vs its own subjects | 20 templates, 0 contradicting |
| **Journal events changed** | **0**. 29 at the pin, 28 of them carrying `actor`; all 29 still byte-identical four commits later |
| `update.md` | **1380 words against a ceiling of 1200** — see observation 9 |

**The measurement that carries the phase's value**, run read-only against both consumers and
recorded in [`ac15_actor_tolerated.txt`](evidence/ac15_actor_tolerated.txt):

```text
BEFORE (code shipped at 2.0.0-dirty.2)
  KZ-IT-telegram-list    4 tasks validate
  innoforce-ai-first     actor 'claude-20260828a' is not a declared team/ participant
                         actor 'claude-20260828b' is not a declared team/ participant
                         2 problem(s) across 15 tasks          <- red, and unfixable from inside

AFTER (2.0.0-dirty.3, same corpora, same bytes)
  KZ-IT-telegram-list    4 tasks validate
  innoforce-ai-first    15 tasks validate

CHANGED IN EITHER PROJECT: nothing. 0 files edited, 0 events rewritten.
```

Its gate was red *permanently*: the events name profiles that were deleted, events are immutable
and profiles are not, so no action available inside that project could ever have cleared it.

### 11.5 Evidence

See [EV file](evidence/EV__phase-aa__portable_delivery.md), rows **E64–E66** — the three
artifacts this pass produced, indexed there rather than left loose, which was the second half of
the review's first item.

### 11.6 Observations

| # | File | Type | Description |
|---|---|---|---|
| 9 | `.tfw/workflows/update.md` | style | **1380 words against the §11 ceiling of 1200.** History: 835 → 1165 (brought *under* by deleting duplication, D9) → 1380 after AC-15's four instruction items. Twice reduced by the D9 move; the duplication is now gone and what remains is instruction. Not a matter of shaving further: the honest options are to accept the overrun, or to split the file the way `research/base.md` was split when research grew — a change to the workflow's shape that no TS authorized. **Coordinator ruling needed.** This is rev3's F4 |
| 10 | `.tfw/scripts/gen_index.py`, `conventions.md` | missing-test | **`via` is validated by nothing** while the canon still presents it as an enumeration — `claude`, `codex`, `gemini`. Under Structural Enforcement a rule that cannot reveal its own violation is advice. It was checked indirectly through `PROVIDER_FAMILIES`, which this pass deleted with its only reader. Either declare `via` free-form provider text or check it — one deliberate sentence. This is rev3's F5, and I did not close it because choosing between those two is a model decision |
| 11 | `TECH_DEBT.md`:113–114 | duplication | **TD-199 is registered twice**, as two rows with different sources for the same finding. Not mine to edit — `TECH_DEBT.md` is the reviewer's and `/tfw-docs`' territory — recorded so the duplicate is a decision rather than a surprise |
| 12 | `.tfw/workflows/handoff.md`, `init.md`, `plan.md`, `review.md` | style | Over the §11 ceiling and were **before** this pass. Named here only to keep observation 9 honest about what this pass did and did not cause: `update.md` is the one it pushed across |

### 11.7 What this pass did not close

**AC-13 half two** was reported unmet by this pass and **ruled met by review revision 3** on the
already-filed second external report — a real project, updated by an operator who is not the
author, 0 files hand-carried, independently re-measured. I record the ruling rather than the
claim: an RF asserting the external check passed on its author's own work is the DoF pattern the
ONB was told to expect, and it is not this RF's to assert either way.

**Review revision 3's item 2** — the TS mandates in AC-15 what its own §1, §7, §8 and §9 forbid —
routed to the **coordinator** and was **closed at `ab7093e`**, *"bring the spec into line with its
own ruling"*: §1 now carries the removal as a declared exception, §7's model-change refusal is
bounded to *"beyond the one removal AC-15 declares"*, and §9 states what Phases B and C inherit.
The reviewer was right that an executor reading §7 before AC-15 is told the pass is a declared
failure; I read them in the order the owner gave and proceeded on the ruling, which is why this
was the coordinator's to fix and not mine.

**Review revision 3's item 3** — a version marker naming a release the CHANGELOG did not carry —
was **closed at `edab067`**, after the review was written. The `[2.0.0-dirty.3]` entry exists,
leads with *what an updating project must do about the change: nothing*, and carries F6: copies
are the declared adapter model and the "commands never duplicate workflow content" rule is
withdrawn, because a consumer had already acted on it.

### 11.8 Fact candidates from this pass

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 10 | philosophy | **Before a field, a file or a flag exists, say the one job it does and what leaves because it arrives.** Four entities in this task were caught only after they collided: the task identifier carried four jobs, `team_readme` carried a directory relationship inside a filename, three flags carried no subject, and `actor` carried an identity and a filename's uniqueness. The last reached two external projects and left one with a permanently red gate. The question is never *what do we call it* | Owner, TS §7 DoF R4 | High |
| 11 | process | **A symptom reported from the field usually arrives with two branches, and both are the small answer.** The report offered: bless per-session agent handles, or forbid them. Both would have shipped a naming convention over a contradiction. The third move — ask what job the thing actually does — is not in the report because a reporter sees the collision, not the cause | This pass, on the second field report | High |
| 12 | process | **Duplication in instructions is measured in files touched per rule changed.** Seven workflows restate one canon sentence, so removing one field reached eight files. The cost is invisible until something changes, which is when it is most expensive | `census_r4.md`, measured | Medium |

---

*RF — TFW-60 / Phase AA: Portable Delivery | revision 3, 2026-08-29 | §11 closes TD-199 | phase measurements pinned at `1079020`, the R4 pass at `b75bef1`*
