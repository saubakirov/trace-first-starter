# Corrective plan — TFW-60 / Phase A, against TS §6

> **Written**: 2026-08-26, after `evidence/census.md` and before any AC-12 edit.
> **Against**: TS revision 3, approved. Work order as revised at R3.
> **Not a re-run.** The RF is not the starting point; the REVIEW's 15 findings and the R3
> clause changes are.

---

## Status of each step in the revised order

| # | Step | State | Evidence |
|---:|---|---|---|
| 1 | `evidence/census.md` | ✅ **done** — landed at `1917615` before any further edit | `census.md` |
| 2 | new lifecycle id in `tfw.statuses` | ⬜ **next** — must precede the templates, or the sweep runs twice | — |
| 3 | templates and new carriers | 🟡 partly — grammar and identity fields done; second precision and phase state remain | `journal_event.md`, `status.md` |
| 4 | generator and migration scripts | 🟡 partly — resolver, schema, journal, board source done; second precision, phase rows, remaining hardcodes remain | `gen_index.py`, `migrate_board.py` |
| 5 | migration run + index generation | 🟡 re-run needed after steps 2–4 | — |
| 6 | **snapshot verified BY COUNT** | ✅ **gate passes** — 61 = 61, side by side | `census.md` §2 |
| 7 | board removal | ✅ done in the rejected pass; the trace it destroyed is restored | `BOARD-SNAPSHOT.md` |
| 8 | canonical rules → workflows → adapters → root | 🟡 done for the grammar; re-sweep needed for the new lifecycle id | — |
| 9 | release surface | 🟡 CHANGELOG updated for the grammar; needs the lifecycle id and second precision | `.tfw/CHANGELOG.md` |

Step 6 is behind step 7 in the tree only because the board was removed in the rejected pass.
The gate is satisfied on the restored artifact, verified by count against
`git show b094943:README.md`, not by assertion.

## What each review finding required, and where it stands

| # | Finding | Disposition |
|---|---|---|
| F1 | seconds-only identifier cannot promise offline uniqueness | ✅ identifier is the whole directory name; bare stamp refused by the resolver; tested |
| F2 | creation protocol absent from shipped workflows | ✅ full create-or-retry algorithm now inline in `plan.md`, with the bound and the failure |
| F3 | event filename collides on same second + same kind | ✅ filename gains the actor; next-second on conflict; both cases tested |
| F4 | participant resolution only in a harness | ✅ a **Who Is Acting** block in all six workflows that write durably |
| F5 | `.user_preferences.md` visible to sync peers | ⬜ **transferred to TFW-61** by R3 — a file-sync concern, settled by `.gitignore` in Git mode |
| F6 | status reader does not enforce the closed schema | ✅ `validate_status` enforces required keys, vocabulary, conditional keys both ways, dates, directory↔id agreement; 11 tests |
| F7 | `gen_docs.py` not migrated | ✅ container- and year-aware `_task_glob`; year no longer read as a task |
| F8 | 10 states ship, not 11; TFW-54 authority absent from Git | ✅ 11 tracked; authority now prefers what a clone will have |
| F9 | accounting overwritten; script hardcodes | ✅ board source explicit, zero rows refused, `--today` defaults to today, snapshot path from config. **Remaining: index link and title hardcodes** |
| F10 | release residue | ✅ template `2.0.0`; `initial_seq` and `{PREFIX}-1` gone from six files and every copy |
| F11 | AC-7 contradicts AC-1 | ✅ clause deleted by R3; nothing to execute |
| F12 | evidence numbers stale | 🟡 census regenerated; EV and RF still to rebuild from current commands |
| F13 | coverage gaps | 🟡 same-second creation, same-kind append, full schema, snapshot count, empty-board refusal all covered. **Remaining: docs resolution under clock IDs and year nesting** |
| F14 | broad staging | ✅ every commit this pass staged by explicit path, staged set diffed against intent before commit |
| F15 | index is a shared transition hot spot | ✅ the forcing test deleted and replaced by two that assert the opposite; `build.verify` now `--validate`, which reads task-local truth |

## Remaining work, in order

1. **Step 2 — the lifecycle id.** Add one value to `tfw.statuses` for *phases running*, in
   both config files, `conventions.md` §5, `glossary.md`, and every workflow, template and
   adapter copy that enumerates the vocabulary. Then set TFW-60's own `lifecycle` to it —
   today it reads `RF`, which is a fragment of phase A's state standing in for a three-phase
   task.
2. **Step 3 — second precision.** `created` and `updated` become `YYYYMMDD-HHMMSS`. The
   status template, its reader, its validator and the migration all change together. The
   migration must write a **declared zero time** where the legacy source carried only a
   date, and the RF must say so rather than imply second-accurate history.
3. **Step 3 — phase state.** One `status.md` per phase directory, same closed schema. The
   task-level `lifecycle` never rolls phase state up.
4. **Step 4 — index phase rows**, rendered beneath their task row. Remaining `migrate_board`
   hardcodes removed.
5. **Step 5 — re-run** migration from the pre-removal board and regenerate the index.
6. **Step 8/9 — re-sweep** for the new vocabulary value; CHANGELOG.
7. **F13 remainder** — docs-resolution tests for clock IDs and year nesting.
8. **F12 — rebuild EV and RF** with every number regenerated from current commands, and the
   AC-12 gate: a three-phase fixture driven concurrently under two owners.

## Two rules held throughout

**No typed timestamp.** Every time value written this pass is read from the system clock and
the read is shown in evidence. The rejected pass shipped one event stamped `23:20:00` — round
seconds, dated after the review that consumed it. The `ownership_changed` event written this
pass shows its read: `datetime.now().astimezone() -> 2026-08-26T22:46:47+05:00`.

**No broad staging.** No `git add -A`, no `git add .`, no directory-wide add. Paths are
named, and the staged set is diffed against the intended set before every commit.

## Standing question for the owner

The census puts the total at **75 now, 76 on completion, against a ruling of 68.** Raised in
`census.md` §1 and §7 with every excess file named. Work continues on everything that does
not depend on the answer; the count is not trimmed to reach 68, because S44 forbids meeting
the number by delivering less.

---

*Corrective plan — TFW-60 / Phase A | 2026-08-26*
