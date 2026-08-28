# Census — TFW-60 / Phase AA, corrective pass R4

> **Measured** 2026-08-28 at `fd85b7c`, **before the first edit**.
> **Authority**: TS §5 AC-15 at revision 4. TS §4 was not updated for R4, so this pass's
> census is the executor's first deliverable and the return-to-coordinator rule applies.
> **Method**: `git grep` / `find` over tracked files. Command per group, so the count is
> reproducible rather than asserted.

---

## One thing to raise before any edit

**The modified count depends on a method the TS already declared, and under the other method
it crosses the budget.** Both numbers, and the method behind each:

| Counting | Modified | Limit | |
|---|---:|---:|---|
| By owner ruling **S32** — byte-identical adapter copies excluded | **22** | 30 | ✅ |
| Distinct paths actually touched, copies included | **38** | 30 | ❌ **crossed** |

The difference is 16 adapter copies: eight workflows change, each has a byte copy under
`.claude/commands/` and `.agent/workflows/`, and S32 excludes them because they carry no
independent content.

Proceeding under S32, which is the declared and owner-approved method — and raising it here
rather than after, because DoF requires a limit crossing to return to the coordinator and
under path-counting this one crosses. The previous pass's review filed the same ambiguity as
**D3** and said the basis belongs in a budget-table correction. This is that correction
arriving with a real number attached: **eight workflows, not four**, is what the R4 model
change costs, and no earlier estimate anticipated it.

### A group appearing

Last pass modified four workflows. This one modifies **eight**, because every one of them
carries the sentence *"Every event this session writes carries `actor`, `on_behalf_of` and
`via`"* — a duplication of `conventions.md` §4 in seven places, which is why removing one
field touches seven files. Raised under the same rule.

## Items 1–4 — the model: `actor` is removed until TFW-54

### Where `actor` lives today

`git grep -n "\bactor\b" -- .tfw/`

| Surface | Files | What carries it |
|---|---:|---|
| Payload code | 1 | `gen_index.py`: `EVENT_NAME` regex, `EVENT_KEYS`, `EVENT_REQUIRED`, `PROVIDER_FAMILIES`, `event_filename()`, `validate_event()` — 18 lines |
| Payload templates | 3 | `journal/event.md` (7 sites incl. the front-matter key), `team/profile.md` (2), `REVIEW.md` (1, in the traces checklist) |
| Canon | 3 | `conventions.md` §4 (6 sites), `glossary.md` (1, commit-attribution wording), `migrations/2.0.0.md` (1) |
| Workflows | 8 | `handoff` (3), `init` (3), `plan` (1), `release` (1), `research/base` (1), `resume` (1), `review` (2), `update` (1) |

Seven of the eight workflows carry the identical three-field sentence. That duplication is
the reason a one-field removal reaches eight files, and it is worth naming: the canon is
restated where it should have been cited.

### Item 3 — what must not be touched, counted

`find tasks workspace -path '*/journal/*.md'`

| | Count |
|---|---:|
| Events in this repository | **28** |
| Carrying an `actor:` field | **28 — every one** |
| Filenames of the form `<time>__<kind>__<actor>.md` | 22 |
| Filenames predating that grammar | 6 |

**Zero of these 28 are edited by this pass, and zero events in either consumer project.**
The validator must read all four shapes — with and without the field, with and without the
actor in the name — and report nothing. That is the whole reason the ruling costs no project
any data.

## Items 5–9 — four instructions naming what the reader does not have

Every TS measurement re-derived here independently. All four reproduce exactly.

| # | Claim in the TS | My measurement | Agrees |
|---|---|---|---|
| 7 | `bindings.yaml`: 7 workflows instruct, 0 templates and 0 canon lines define | `git grep -l bindings.yaml -- .tfw/workflows/` → **7** (`handoff`, `init`, `plan`, `release`, `research/base`, `resume`, `review`); `ls .tfw/templates/bindings.yaml` → absent; `grep -c bindings.yaml .tfw/conventions.md` → **0** | ✅ |
| 5 | Step 6's table has no row for `.claude/commands/` | `grep -c "claude/commands" .tfw/workflows/update.md` → **0** in the whole file. The table carries 6 rows; Antigravity's copy is listed, Claude Code's is not | ✅ |
| 6 | Retired vocabulary survives in an unchecked adapter layer | **0** hits for `Task Board` in our own `.claude .agent .agents AGENTS.md CLAUDE.md`. Ours is clean — and nothing checks it, which is the finding. The consumer's was not | ✅ |
| 8 | `read_journal` globs `journal/` non-recursively | `read_journal(task_dir, …)` reads `task_dir / "journal"` once. Phase journals in this repository: **0**, so the gap is invisible here and was found only because a consumer created `phase-a/journal/` by symmetry with the per-phase `status.md` this phase shipped | ✅ |
| 9 | `installed_from` exists nowhere | **0** in `update.md`, `templates/project_config.yaml` and `project_config.yaml` | ✅ |

## Items 10–12 — promoted out of the register

### Item 10 — TD-193, the real reach

A scan over every payload `.md`/`.yaml`/`.template` for both reference forms:

| | Count |
|---|---:|
| References found — prefixed `.tfw/templates/X` | **154** |
| References found — bare `templates/X` | **58** |
| Total | **212** |
| Broken targets | **8** |

All 8 are deliberate: five in `CHANGELOG.md` (historical entries recording past releases) and
three in `migrations/2.0.0.md` (the list of files the operator is told to **delete**). So the
registry needs the exemptions stated, exactly as the retired-wording check states its own.

**A third reference form exists and neither the TS nor the reviewer named it:** a bare
*filename* with no directory at all — `conventions.md` §10.4's `` `topic_file.md` ``, which is
item 11's subject. It is invisible to both patterns above. Recorded because a check that
claims "every path" and silently omits a form is this task's own recurring defect.

### Item 11 — TD-192, the rule versus its subjects

`.tfw/conventions.md` §10.4 says *"Markdown templates in `.tfw/templates/` also follow
`lower_snake_case`"*. Measured against all **20** Markdown templates:

| Class | Count | Files |
|---|---:|---|
| Contradict the rule | **9** | `HL.md`, `TS.md`, `RF.md`, `RES.md`, `ONB.md`, `REVIEW.md`, `KNOWLEDGE.md`, `RELEASE.md`, `evidence/EV.md` |
| Single lowercase word — no underscore to demonstrate | 8 | `status.md`, `journal/event.md`, `knowledge/topic.md`, `team/profile.md`, `review/{judge,map,verify}.md` |
| Numeric-prefixed | 3 | `research/{1_briefing,2_gather,3_extract,4_challenge}.md` |

The reviewer's objection reproduces exactly: **9 of 20**, and after the template moves no
Markdown template demonstrates `lower_snake_case` proper. Swapping the example filename would
leave the rule wrong about nine of its own subjects, which is why the TS rules the other way.

### Item 12 — the adapter README contradicts what ships

`.tfw/adapters/claude-code/README.md`:36 — *"Commands never duplicate workflow content — they
reference it"* — beside 12 byte-identical copies in `.claude/commands/`, verified identical by
`cmp`. Per the owner's 2026-08-28 ruling, copies **are** the model.

## Affected files — 22 modified by S32, 1 created, 38 paths touched

| Group | Paths | Items |
|---|---|---|
| Payload code | `.tfw/scripts/gen_index.py` | 1, 2, 3, 8 |
| Payload tests | `.tfw/scripts/test_gen_index.py` | 1, 3, 8 |
| Templates | `.tfw/templates/journal/event.md`, `team/profile.md`, `REVIEW.md`, `project_config.yaml` | 1, 2, 4, 9 |
| **Created** | `.tfw/templates/bindings.yaml` | 7 |
| Canon | `.tfw/conventions.md`, `.tfw/glossary.md`, `.tfw/migrations/2.0.0.md` | 2, 4, 8, 11 |
| Workflows | `handoff`, `init`, `plan`, `release`, `research/base`, `resume`, `review`, `update` | 1, 4, 5, 6, 7, 9 |
| Adapter source | `.tfw/adapters/claude-code/README.md` | 12 |
| Docs tooling | `docs/scripts/test_integration.py` | 6, 10 |
| Release surface | `.tfw/VERSION`, `.tfw/CHANGELOG.md`, `.tfw/project_config.yaml` | — |
| Adapter copies (S32) | 8 workflows × `.claude/commands/` + `.agent/workflows/` = 16 | 5 |

### Never modified

| Class | Count | Why |
|---|---:|---|
| Journal events, this repository | **28** | Immutable. Item 3 makes tolerating them the fix |
| Journal events, both consumers | all | Item 3's whole point: the ruling costs no project any work |
| Historical trace artifacts under `tasks/` | 82 + 26 | They record what was true when written |
| Provenance comments in generated `status.md` | 11 | A true statement about a past act at a path correct then |
| `.tfw/CHANGELOG.md` entries below `[2.0.0-dirty.3]` | — | A changelog records; 5 of the 8 broken paths above live there by design |

## Order of work, from TS §6 and the owner's instruction

Model first, because items 4 and 8 name its result: **1–4**, then **5–9**, then **10–12**.

---

*Census — TFW-60 Phase AA corrective pass R4 | 2026-08-28, at `fd85b7c`*
