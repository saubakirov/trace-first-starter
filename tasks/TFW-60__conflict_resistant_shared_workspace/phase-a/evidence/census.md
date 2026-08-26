# Census — TFW-60 / Phase A

> **Purpose**: the measured baseline the owner's overrun ruling (S42, S44) stands on, and the reference
> point AC-6 and AC-7 are read against. Landed before any other write in the phase, per TS §6 required
> work order and ONB recommendation 1.
> **Measured**: 2026-08-26
> **Tree**: `80d6a16`, clean except the `README.md` status transition to `🟢 RF` that opened execution
> **Host**: Windows 11 Pro 26200, Git Bash, Python 3.13.5, pytest 9.0.2, NTFS

---

## 1. Corpus baseline

Every figure below is a **relation reference**, not a target. AC-7 is satisfied when the link-failure set
does not grow against this row, never by reproducing a number.

| Quantity | Command | Baseline |
|---|---|---:|
| Board table lines from `README.md:251` | `awk 'NR>=253 && /^\|/' README.md \| wc -l` | 63 |
| — of which header + separator | — | 2 |
| **Board data rows** | — | **61** |
| Rows matching a strict `\| \[TFW-` link | `awk 'NR>=253 && /^\| \[TFW-/' README.md \| wc -l` | 52 |
| Rows not matching it | — | 9 |
| **Task directories** | `ls -d tasks/*/ \| wc -l` | **53** |
| `TFW-N` occurrences, tracked files | `git grep -oE 'TFW-[0-9]+' \| wc -l` | **7,505** |
| Files carrying at least one | `git grep -lE 'TFW-[0-9]+' \| wc -l` | **666** |
| Commit subjects naming a task | `git log --format='%s' \| grep -cE 'TFW-[0-9]+'` | **271** |
| — of which under the `[agent/task/scope/role]` grammar | `grep -cE '^\[[^]]*/TFW-[0-9]+/'` | 186 |

### Drift since the TS was written

The TS was drafted the same day and its figures were already stale when onboarding measured them. They
moved twice more before this baseline landed — the ONB, the coordinator's answers and the TS revision each
added references to the corpus they describe.

| Figure | TS revision 1 | ONB measurement | Coordinator recheck | **This baseline** |
|---|---:|---:|---:|---:|
| Board data rows | 60 | 61 | 61 | **61** |
| Task directories | 51 | 53 | 53 | **53** |
| `TFW-N` occurrences | 7,051 | 7,462 | 7,497 | **7,505** |
| Files carrying one | 653 | 665 | 666 | **666** |
| Commit subjects | 249 | 265 | 267 | **271** |
| Directory-only entries | 0 | 1 | 1 | **1** |

This is the evidence behind ONB Q6 and the reason AC-6 and AC-7 became relations. A phase that edits the
corpus it counts cannot be held to a fixed total.

## 2. Board reconciliation

```
   61 board data rows
   53 task directories
  ────────────────────────
  114 source occurrences  →  61 logical identities

      53  matched      row and directory both exist
       8  board-only   a row with no directory
       0  directory-only, with no row of any kind
```

The 9 rows a strict regex misses are not 9 board-only tasks. One of them has a directory:

| Row | Form | Directory? | Class |
|---|---|---|---|
| TFW-16 | plain text, `⬜ TODO` | no | board-only backlog |
| TFW-20 | plain text, `⬜ TODO` | no | board-only backlog |
| TFW-28 | `~~TFW-28~~ — absorbed into TFW-27/C` | no | board-only, absorbed |
| **TFW-30** | `~~TFW-30~~ — absorbed into TFW-45/C` | **yes** | **malformed row over a real directory** |
| TFW-33 | plain text, `⬜ TODO` | no | board-only backlog |
| TFW-34 | plain text, `⬜ TODO` | no | board-only backlog |
| TFW-35 | plain text, `⬜ TODO` | no | board-only backlog |
| TFW-37 | `~~TFW-37~~ — absorbed into TFW-38` | no | board-only, absorbed |
| TFW-39 | plain text, `⬜ TODO` | no | board-only backlog |

53 matched = 52 strict-matching rows plus TFW-30, whose directory the strict regex cannot see. This is the
correction to the Phase A HL's stated `51 matched · 9 board-only · 0 directory-only`.

### Lifecycle distribution of the 52 strict rows

| Class | Count | Detail |
|---|---:|---|
| Terminal | 41 | 39 `✅ DONE` (two carry trailing prose) + 2 `❌ REJECTED` |
| Non-terminal | 11 | TFW-3, TFW-4, TFW-36, TFW-44, TFW-45, TFW-54, TFW-57, TFW-58, TFW-59, TFW-60, TFW-61 |

TFW-45 carries `❄️ FROZEN`, a value in no declared vocabulary — `FROZEN` appears 0 times in
`project_config.yaml` and the snowflake 0 times in `conventions.md`. Carried verbatim as a diagnostic per
ONB Q12.

## 3. File census against TS §4

Measured per file rather than by group. `board` counts case-insensitive "task board"; `tasks/` counts
literal path occurrences; `ident` counts identifier-grammar tokens (`{PREFIX}-{N}`, `{prefix}-{seq}`,
`PROJ-N`, `TFW-N`).

| # | File | board | `tasks/` | ident | lines | Verdict |
|---:|---|---:|---:|---:|---:|---|
| 1 | `.tfw/conventions.md` | 4 | 4 | 24 | 607 | edit |
| 2 | `.tfw/glossary.md` | 2 | 0 | 3 | 310 | edit |
| 3 | `.tfw/README.md` | 1 | 0 | 0 | 133 | edit |
| 4 | `.tfw/compilable_contract.md` | 1 | 10 | 16 | 118 | edit |
| 5 | `.tfw/project_config.yaml` | 0 | 0 | 1 | 116 | edit — container key, journal ceiling, `build.*` |
| 6 | `.tfw/templates/project_config.yaml` | 0 | 0 | 1 | 120 | edit — same keys |
| 7 | `.tfw/workflows/handoff.md` | 2 | 0 | 1 | 173 | edit |
| 8 | `.tfw/workflows/init.md` | 11 | 5 | 0 | 222 | edit |
| 9 | `.tfw/workflows/plan.md` | 1 | 1 | 1 | 148 | edit |
| 10 | `.tfw/workflows/release.md` | 1 | 0 | 0 | 79 | edit |
| 11 | `.tfw/workflows/research/base.md` | 1 | 0 | 0 | 138 | edit |
| 12 | `.tfw/workflows/resume.md` | 0 | 1 | 2 | 98 | edit — container resolution |
| 13 | `.tfw/workflows/review.md` | 3 | 0 | 0 | 154 | edit |
| 14 | **`.tfw/workflows/update.md`** | **0** | **0** | **0** | 167 | **no board or container reference — correction to §4** |
| 15–27 | 13 × `.tfw/templates/*` | 2 total | **0 total** | 42 total | 1,138 | edit — 11 for identifier grammar only, 2 for board text |
| 28 | `.tfw/adapters/codex/AGENTS.md.template` | 1 | 0 | 0 | 36 | edit |
| 29 | `.tfw/adapters/codex/README.md` | 2 | 1 | 0 | 162 | edit |
| 30–37 | 8 × `skills/tfw-*/SKILL.md` | 10 total | 0 | 0 | 171 | edit |
| 38 | `docs/scripts/gen_docs.py` | 1 | 19 | 18 | 693 | edit — board parser at line 324 |
| 39 | `docs/scripts/test_integration.py` | 1 | 5 | 0 | 187 | rewrite line 159, do not delete |
| 40 | `.tfw/VERSION` | 0 | 0 | 0 | 2 | edit — `2.0.0` |
| 41 | `.tfw/CHANGELOG.md` | 4 | 0 | 427 | 694 | edit — new entry; existing 4 mentions are history and stay |
| 42 | `README.md` | 5 | 397 | 605 | 318 | edit — table plus 4 prose statements |
| 43 | `AGENTS.md` | 2 | 0 | 0 | 63 | edit |
| 44 | `CLAUDE.md` | 1 | 0 | 0 | 54 | edit |
| 45 | `RELEASE.md` | 3 | 0 | 0 | 63 | edit |
| | **Total** | | | | **6,164** | |

**Two corrections to §4, as the TS instructs:**

1. `.tfw/workflows/update.md` carries zero board references, zero `tasks/` paths and zero identifier
   tokens. Its only grep match was a pointer to the codex adapter README. It changes only if the version
   string requires it. The RF reports the final disposition.
2. **Zero** of the 13 templates contain `tasks/`, and only `REVIEW.md` and `RELEASE.md` contain a board
   reference. The other 11 change for identifier grammar, which is a real edit with a different reason
   than §4 recorded.

## 4. Files excluded from the count, and why

| Class | Ruling | Members |
|---|---|---|
| Byte-identical adapter copies | S32 | `.claude/`, `.agent/`, `.agents/` — regenerated by adapter sync |
| Artifacts of the work itself | S46 | this file, `migration_accounting.md`, `EV__phase-a__*.md`, the ONB, the RF, the REVIEW |
| Other-owner registries under D37 | ONB Q3 | `KNOWLEDGE.md`, `knowledge/convention.md`, `TECH_DEBT.md` → `/tfw-docs`, `/tfw-knowledge` after REVIEW |
| Stale edition copy | ONB Q4 | `editions/02-assisted/AGENTS.md`, `editions/02-assisted/MIGRATION.md` — v1.0 here against a shipped v1.4; recorded as a debt candidate in RF §6 |

S46 is the ruling that matters most for this file: because evidence sits outside the count, there is no
budget argument for producing less of it.

## 5. Budget position at baseline

| | Configured | Ruled (S42 / S44) | At baseline |
|---|---:|---:|---:|
| Modified files | 30 | 45 | 45 planned, 1 expected to fall out (`update.md`) |
| New files | 15 | 23 | 23 |
| Files total | 30 | 68 | 68 |
| LOC | 3,000 | — | reported in the RF |

Return-to-coordinator condition (TS §7): a new group appears, or the total passes roughly 75. Neither
holds at baseline.

---

*Census — TFW-60 / Phase A | 2026-08-26*
