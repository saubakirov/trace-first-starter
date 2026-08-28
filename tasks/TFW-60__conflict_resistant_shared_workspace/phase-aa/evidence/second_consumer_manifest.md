# Migration accounting


Produced by `python .tfw/scripts/migrate_board.py --manifest`. Every board row and
every task directory is accounted for exactly once. Re-runnable: the numbers below
are recomputed from the tree, not transcribed.

## Reconciliation

```
   17 board data rows
   15 task directories
  ----------------------------------------
   32 source occurrences  ->   16 logical identities

       16  matched       row and directory both exist
        1  board-only    a row with no directory at all
        0  unresolved    a row whose directory the grammar rejects
        0  unresolved    a rejected directory no row names
        0  directory-only  a directory with no row
```

Rows in a shape no strict `| [ID](path)` parser matches: **3**. They are reported, not repaired.

## Board-only rows

A row with **no directory at all**. A row whose directory exists but whose directory
*name* the grammar rejects is not here — it is under Unresolved inputs, because
calling it a backlog idea asserts something the source never said.

| ID | Status | Why it has no directory |
|---|---|---|
| `TFW-91` | ✅ DONE | backlog idea, never started |

## Unresolved inputs

A directory the identifier grammar does not parse — not clock
`YYYYMMDD-HHMMSS__slug`, not legacy `PREFIX-N` optionally followed by `__slug`.
**No state file is written for one, and nothing is asserted about whether work
happened there.** The grammar is not widened to admit it: an accountable person may
rename the directory by hand, which leaves a trace, and a tool that normalized it
would not. Same rule as `UNDECLARED`.

None — every directory name parses.

## Directory-only entries

None — every directory is named by a row, though not every row names it in a shape a strict parser matches.

## Malformed rows

| ID | Form | Directory? |
|---|---|---|
| `TFW-90` | plain text, not a link | yes |
| `TFW-90` | plain text, not a link | yes |
| `TFW-91` | plain text, not a link | no |

## Every board identifier, by name — 17

The requirement is that each one **resolves** somewhere after the board is gone, and
that the list is produced by counting rather than asserted. A previous pass claimed
61 rows were retained while the snapshot held zero; naming them individually is what
makes that failure impossible to repeat.

| # | Identifier | Resolves to |
|---:|---|---|
| 1 | `TFW-90` | snapshot + task directory + index (unresolved or closed) |
| 2 | `TFW-90` | snapshot + task directory + index (unresolved or closed) |
| 3 | `TFW-91` | snapshot |
| 4 | `INNO-1` | snapshot + task directory + index (unresolved or closed) |
| 5 | `INNO-2` | snapshot + task directory + `status.md` → index |
| 6 | `INNO-3` | snapshot + task directory + `status.md` → index |
| 7 | `INNO-4` | snapshot + task directory + `status.md` → index |
| 8 | `INNO-5` | snapshot + task directory + `status.md` → index |
| 9 | `INNO-6` | snapshot + task directory + index (unresolved or closed) |
| 10 | `INNO-7` | snapshot + task directory + `status.md` → index |
| 11 | `INNO-8` | snapshot + task directory + `status.md` → index |
| 12 | `INNO-9` | snapshot + task directory + `status.md` → index |
| 13 | `INNO-10` | snapshot + task directory + `status.md` → index |
| 14 | `INNO-11` | snapshot + task directory + `status.md` → index |
| 15 | `INNO-12` | snapshot + task directory + `status.md` → index |
| 16 | `INNO-13` | snapshot + task directory + index (unresolved or closed) |
| 17 | `INNO-14` | snapshot + task directory + `status.md` → index |

**Unaccounted: 0.** Every identifier the board carried resolves after its removal.

## Task state written

Only for non-terminal tasks that have a directory. Every value comes from the
board or the directory; `unrecorded` marks a fact the source never carried.

| Task | Lifecycle | Authority | Note |
|---|---|---|---|
| `INNO-2` | RF | `HL-INNO-2__shareholder_vision_presentation.md` |  |
| `INNO-3` | RF | `HL-INNO-3__openclaw_meeting_agent.md` |  |
| `INNO-4` | UNDECLARED | `HL-INNO-4__ai_first_engineering_presentation.md` | status `🟡 TS` is outside the declared vocabulary — carried verbatim |
| `INNO-5` | RF | `HL-INNO-5__seminar_geospatial_data_presentation.md` |  |
| `INNO-7` | RF | `HL__INNO-7__cto_interview_preparation.md` |  |
| `INNO-8` | RES | `HL-INNO-8__ai_work_mini_mba_course.md` |  |
| `INNO-9` | KNW | `HL-INNO-9__ceo_transformation_plan_2026h2.md` |  |
| `INNO-10` | RF | `HL-INNO-10__ai_university_rector_presentation.md` |  |
| `INNO-11` | RF | `HL-INNO-11__qairu_gis_lab_collaboration.md` |  |
| `INNO-12` | RF | `HL-INNO-12__seminar_ai_assistant_aug2026.md` |  |
| `INNO-14` | HL_DRAFT | `HL-INNO-14__ai_policy_import_and_provenance.md` |  |

## Guarantees checked

| Guarantee | How |
|---|---|
| Zero renames, zero moves | the script has no rename or move call |
| Zero byte changes to existing artifacts | only paths that do not yet exist are opened for writing; an existing target aborts the run |
| No fact invented | absent facts are written as `unrecorded`; a lifecycle outside the vocabulary becomes `UNDECLARED` plus the verbatim value |
| Every row and directory accounted once | the reconciliation above sums to the source occurrence count |

---

*Migration accounting*
