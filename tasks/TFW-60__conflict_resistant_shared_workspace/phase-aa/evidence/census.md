# Census — TFW-60 / Phase AA: Portable Delivery

> **Measured**: 2026-08-27, working tree at `5c8fcea`, before the first edit.
> **Method**: `git grep` / `git ls-files` over tracked files only. Commands are quoted per row so the
> count is reproducible rather than asserted.
> **Authority**: TS §4 as amended at revision 3. TS §4's `Modify — 26` was the coordinator's estimate;
> R2 states the counted census governs. This is the count.

---

## Verdict

| | Count | Limit | |
|---|---:|---:|---|
| Created | **1** | 15 | ✅ |
| Moved | **7** — 4 scripts, 3 templates | — | `git mv`; adds no surface |
| Modified | **26** | 30 | ✅ |
| Deleted outright | **0** | — | the 4 script deletions from `docs/scripts/` are the move |
| Never modified | **82 + 11 + 2** | — | historical traces · provenance comments · `KNOWLEDGE.md` historical rows |

No budget limit is crossed. One group appeared that TS §4 does not enumerate — see
**Group appearing** below.

## Moved — 7

### Scripts — 4 (`docs/scripts/` → `.tfw/scripts/`)

| From | To | Bytes |
|---|---|---:|
| `docs/scripts/gen_index.py` | `.tfw/scripts/gen_index.py` | 41,732 |
| `docs/scripts/migrate_board.py` | `.tfw/scripts/migrate_board.py` | 29,714 |
| `docs/scripts/test_gen_index.py` | `.tfw/scripts/test_gen_index.py` | 39,337 |
| `docs/scripts/test_migrate_board.py` | `.tfw/scripts/test_migrate_board.py` | 14,814 |

`docs/scripts/` retains `gen_docs.py`, `test_gen_docs.py`, `test_integration.py` — documentation
tooling, which is what that directory is for.

### Templates — 3 (flat name → directory mirroring its output)

| From | To | Produces into |
|---|---|---|
| `.tfw/templates/team_profile.md` | `.tfw/templates/team/profile.md` | `team/<handle>.md` |
| `.tfw/templates/journal_event.md` | `.tfw/templates/journal/event.md` | `{task}/journal/<name>.md` |
| `.tfw/templates/topic_file.md` | `.tfw/templates/knowledge/topic.md` | `knowledge/<topic>.md` |

Existing precedent this joins: `templates/research/`, `templates/evidence/`, `templates/review/`.
The flat template namespace shrinks by 3.

## Created — 1

| Path | Why |
|---|---|
| `.tfw/migrations/2.0.0.md` | the guide whose absence made a major release unfollowable |

### Withdrawn before creation — 2

Per TS R3. Recorded here so the reviewer sees the withdrawal as a decision.

| Withdrawn | Absorbed by |
|---|---|
| a `team/` README template | AC-7 creates `team/` together with its first profile; the orientation lives in the profile template's own guidance comment |
| `.tfw/scripts/README.md` | `--help` says how, the migration guide says when, `conventions.md` says where |

## Modified — 26

`git grep` commands that produced each group are given so the list can be re-derived.

### Normative path references — 5

`git grep -ln "docs/scripts/gen_index\|docs/scripts/migrate_board\|team_profile\.md\|journal_event\.md\|topic_file\.md" -- .tfw/`

| # | Path | Hits |
|---:|---|---|
| 1 | `.tfw/conventions.md` | `:332` script · `:27,28,267,268,603,629` templates · plus AC-14 canon additions |
| 2 | `.tfw/glossary.md` | `:309` script · `:262` template |
| 3 | `.tfw/project_config.yaml` | `:27` template · `:132,133,139` build commands · `:135–138` comment deleted (AC-9) |
| 4 | `.tfw/workflows/init.md` | `:69,233` script · `:132` template · AC-7 `team/` step |
| 5 | `.tfw/workflows/knowledge.md` | `:71` template |

### Update path — 1

| # | Path | Why |
|---:|---|---|
| 6 | `.tfw/workflows/update.md` | AC-2 routing · AC-6 container decision and `initial_seq` · AC-7 `team/` step · AC-10 pristine-tag diff and local source |

### Session naming — 1

| # | Path | Why |
|---:|---|---|
| 7 | `.tfw/workflows/plan.md` | AC-12 — the naming step moves after the identifier exists |

### Carrier ergonomics — 1

| # | Path | Why |
|---:|---|---|
| 8 | `.tfw/templates/status.md` | AC-5 — quoted example, the quoting rule, a worked valid example |

### Adapter source — 3

`for f in $(git ls-files '.tfw/adapters/**'); do` … extract `.tfw/…` paths, test each resolves.
Three files name the non-existent `.tfw/workflows/research.md`; nothing else fails to resolve.

| # | Path | Hits |
|---:|---|---|
| 9 | `.tfw/adapters/claude-code/CLAUDE.md.template` | `:31` |
| 10 | `.tfw/adapters/claude-code/README.md` | `:43` |
| 11 | `.tfw/adapters/antigravity/README.md` | `:22,64` |

### Tooling — 3

| # | Path | Why |
|---:|---|---|
| 12 | `docs/scripts/gen_docs.py` | `:18` bare `import gen_index` · `:190` root derivation |
| 13 | `docs/scripts/test_integration.py` | `:174` glob loses coverage on the move · `:309` shipped-text roots · AC-11 path check lands here |
| 14 | `docs/mkdocs.yml` | verified: `gen-files` runs `scripts/gen_docs.py` and is unaffected. Listed by the TS; **modified only if the build requires it.** If no change is needed the RF records 25, not 26 |

### Release surface — 3

| # | Path | Why |
|---:|---|---|
| 15 | `.tfw/VERSION` | `2.0.0-dirty.2` |
| 16 | `.tfw/CHANGELOG.md` | `:52,58` template paths · `:75,79,91,120,131,132` script paths · new entry |
| 17 | `README.md` | `:257` script path |

### Project participant document — 1

| # | Path | Why |
|---:|---|---|
| 18 | `team/README.md` | `:18` links `.tfw/templates/team_profile.md`; the link breaks on the move |

### Adapter copies — 8

Byte-identical copies of four workflows this phase edits. Verified byte-identical before the change:
all 22 copies matched their sources.

| # | Path |
|---:|---|
| 19–22 | `.claude/commands/tfw-{init,update,plan,knowledge}.md` |
| 23–26 | `.agent/workflows/tfw-{init,update,plan,knowledge}.md` |

### Not modified — three TS entries that turn out not to need it

| TS entry | Finding |
|---|---|
| `.agents/skills/tfw-init/SKILL.md` · `tfw-update` · `tfw-plan` | **No change needed.** Codex skills route by path — they load `.tfw/workflows/<name>.md` and do not copy its content. All 11 are byte-identical to `.tfw/adapters/codex/skills/`, and none of the five that name a template names one of the three moving. A workflow's content change does not reach them. This is why the count is 26 and not 29 |

## Never modified

| Class | Count | Verification |
|---|---:|---|
| Historical trace artifacts under `tasks/` naming `docs/scripts/` | 82 | TFW-26 … TFW-56. They record what was true when written |
| Generated `status.md` files carrying the provenance comment | 11 | `git grep -l "Written by docs/scripts/migrate_board.py"` returns 13: the script itself, the Phase AA TS, and exactly 11 `status.md`. Rewriting one would make the record describe an act that did not happen |
| `tasks/` artifacts naming a moving template | 17 | same class |
| `KNOWLEDGE.md:82` (D48) · `:204` (legacy table) | 2 | **Historical decision records about a past rename.** They name `TOPIC_FILE.md → topic_file.md` deliberately. Same P9 logic as the provenance comments |

### `KNOWLEDGE.md` — the two live references, both excluded

| Line | Content | Ruling |
|---|---|---|
| `:22` | names `docs/scripts/gen_index.py` in the architecture table | Excluded by ONB Q5 answer **(b)**: owned by `/tfw-docs` under the D37 split. AC-1's gate names it as a known exception; it goes to RF §6 |
| `:82`, `:204` | historical rows about the 2026-04-15 rename | Never modified — see above |

`KNOWLEDGE.md:26` names `docs/scripts/gen_docs.py`, which does not move. No action.

## Group appearing — raised, not absorbed

TS §4's Modify table does not enumerate the reference surface that TS **R3's own** template moves
create. Four files are reached only through that decision:

| Path | Reached by |
|---|---|
| `.tfw/workflows/knowledge.md` | `topic_file.md` → `knowledge/topic.md` |
| `.claude/commands/tfw-knowledge.md` · `.agent/workflows/tfw-knowledge.md` | copies of the above |
| `team/README.md` | `team_profile.md` → `team/profile.md` |

Recorded under the return-to-coordinator rule. **Proceeding**, because the group is a direct
consequence of a decision revision 3 took two hours before this census — it is enumerated here rather
than newly discovered — and because no limit is crossed at 26 of 30. If the coordinator reads the
group as requiring a fifth revision, this row is where to start.

## Also checked, no action

| Check | Result |
|---|---|
| `.github/workflows/docs.yml` | runs `mkdocs build` only. **No CI runs pytest**, so the move needs no CI change |
| `.gitignore` | already carries `__pycache__/`, `*.pyc`, `.pytest_cache/`. `.tfw/scripts/__pycache__` is covered |
| A stray `phases/` directory | `git grep -c "phases/" -- .tfw/ docs/scripts/` → **0 occurrences**. Nothing this release ships produces it. Per TS §6, the check is recorded and the cause is not chased |
| `tasks/BOARD-SNAPSHOT.md` | SCREAMING-KEBAB name matches nothing else in the tree. **Not renamed** — Phase A's links resolve to it. Recorded as debt in RF §6 per TS §6 |
| Baseline suite | `pytest docs/scripts/ -q` → **220 passed, 1 skipped**, 305 s. The two moving test files alone: **131 passed, 1 skipped** |

---

*Census — TFW-60 / Phase AA | 2026-08-27, at `5c8fcea`*
