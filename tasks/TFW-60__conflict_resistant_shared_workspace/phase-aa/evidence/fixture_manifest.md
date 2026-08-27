# Migration accounting


Produced by `python .tfw/scripts/migrate_board.py --manifest`. Every board row and
every task directory is accounted for exactly once. Re-runnable: the numbers below
are recomputed from the tree, not transcribed.

## Reconciliation

```
    4 board data rows
    2 task directories
  ----------------------------------------
    6 source occurrences  ->    4 logical identities

        2  matched       row and directory both exist
        0  board-only    a row with no directory at all
        2  unresolved    a row whose directory the grammar rejects
        0  unresolved    a rejected directory no row names
        0  directory-only  a directory with no row
```

Rows in a shape no strict `| [ID](path)` parser matches: **0**. They are reported, not repaired.

## Board-only rows

A row with **no directory at all**. A row whose directory exists but whose directory
*name* the grammar rejects is not here — it is under Unresolved inputs, because
calling it a backlog idea asserts something the source never said.

None.

## Unresolved inputs

A directory the identifier grammar does not parse — not clock
`YYYYMMDD-HHMMSS__slug`, not legacy `PREFIX-N` optionally followed by `__slug`.
**No state file is written for one, and nothing is asserted about whether work
happened there.** The grammar is not widened to admit it: an accountable person may
rename the directory by hand, which leaves a trace, and a tool that normalized it
would not. Same rule as `UNDECLARED`.

| Directory | Named by a board row? | Status the board carried |
|---|---|---|
| `tasks/TFW-01_awesome_list_restructure` | `TFW-01` | ✅ DONE |
| `tasks/TFW-02_enhanced_validation` | `TFW-02` | ✅ DONE |

## Directory-only entries

None — every directory is named by a row, though not every row names it in a shape a strict parser matches.

## Malformed rows

None.

## Every board identifier, by name — 4

The requirement is that each one **resolves** somewhere after the board is gone, and
that the list is produced by counting rather than asserted. A previous pass claimed
61 rows were retained while the snapshot held zero; naming them individually is what
makes that failure impossible to repeat.

| # | Identifier | Resolves to |
|---:|---|---|
| 1 | `TFW-01` | snapshot + directory whose name the grammar rejects + index (unresolved) |
| 2 | `TFW-02` | snapshot + directory whose name the grammar rejects + index (unresolved) |
| 3 | `TFW-3` | snapshot + task directory + index (unresolved or closed) |
| 4 | `TFW-4` | snapshot + task directory + `status.md` → index |

**Unaccounted: 0.** Every identifier the board carried resolves after its removal.

## Task state written

Only for non-terminal tasks that have a directory. Every value comes from the
board or the directory; `unrecorded` marks a fact the source never carried.

| Task | Lifecycle | Authority | Note |
|---|---|---|---|
| `TFW-4` | ONB | `HL-TFW-4__showcase_reorg.md` |  |

## Guarantees checked

| Guarantee | How |
|---|---|
| Zero renames, zero moves | the script has no rename or move call |
| Zero byte changes to existing artifacts | only paths that do not yet exist are opened for writing; an existing target aborts the run |
| No fact invented | absent facts are written as `unrecorded`; a lifecycle outside the vocabulary becomes `UNDECLARED` plus the verbatim value |
| Every row and directory accounted once | the reconciliation above sums to the source occurrence count |

---

*Migration accounting*
