# Migration accounting — TFW-60 / Phase A


Produced by `python docs/scripts/migrate_board.py --manifest`. Every board row and
every task directory is accounted for exactly once. Re-runnable: the numbers below
are recomputed from the tree, not transcribed.

## Reconciliation

```
   61 board data rows
   53 task directories
  ----------------------------------------
  114 source occurrences  ->   61 logical identities

       53  matched       row and directory both exist
        8  board-only    a row with no directory
        0  directory-only  a directory with no row
```

Rows in a shape no strict `| [ID](path)` parser matches: **9**. They are reported, not repaired.

## Board-only rows

| ID | Status | Why it has no directory |
|---|---|---|
| `TFW-16` | ⬜ TODO | backlog idea, never started |
| `TFW-20` | ⬜ TODO | backlog idea, never started |
| `TFW-28` | — | absorbed into another task |
| `TFW-33` | ⬜ TODO | backlog idea, never started |
| `TFW-34` | ⬜ TODO | backlog idea, never started |
| `TFW-35` | ⬜ TODO | backlog idea, never started |
| `TFW-37` | — | absorbed into another task |
| `TFW-39` | ⬜ TODO | backlog idea, never started |

## Directory-only entries

None — every directory is named by a row, though not every row names it in a shape a strict parser matches.

## Malformed rows

| ID | Form | Directory? |
|---|---|---|
| `TFW-16` | plain text, not a link | no |
| `TFW-20` | plain text, not a link | no |
| `TFW-28` | struck through | no |
| `TFW-30` | struck through | yes |
| `TFW-33` | plain text, not a link | no |
| `TFW-34` | plain text, not a link | no |
| `TFW-35` | plain text, not a link | no |
| `TFW-37` | struck through | no |
| `TFW-39` | plain text, not a link | no |

## Every board identifier, by name — 61

The requirement is that each one **resolves** somewhere after the board is gone, and
that the list is produced by counting rather than asserted. A previous pass claimed
61 rows were retained while the snapshot held zero; naming them individually is what
makes that failure impossible to repeat.

| # | Identifier | Resolves to |
|---:|---|---|
| 1 | `TFW-1` | snapshot + task directory + index (unresolved or closed) |
| 2 | `TFW-2` | snapshot + task directory + index (unresolved or closed) |
| 3 | `TFW-3` | snapshot + task directory + `status.md` → index |
| 4 | `TFW-4` | snapshot + task directory + `status.md` → index |
| 5 | `TFW-5` | snapshot + task directory + index (unresolved or closed) |
| 6 | `TFW-6` | snapshot + task directory + index (unresolved or closed) |
| 7 | `TFW-7` | snapshot + task directory + index (unresolved or closed) |
| 8 | `TFW-8` | snapshot + task directory + index (unresolved or closed) |
| 9 | `TFW-9` | snapshot + task directory + index (unresolved or closed) |
| 10 | `TFW-10` | snapshot + task directory + index (unresolved or closed) |
| 11 | `TFW-11` | snapshot + task directory + index (unresolved or closed) |
| 12 | `TFW-12` | snapshot + task directory + index (unresolved or closed) |
| 13 | `TFW-13` | snapshot + task directory + index (unresolved or closed) |
| 14 | `TFW-14` | snapshot + task directory + index (unresolved or closed) |
| 15 | `TFW-15` | snapshot + task directory + index (unresolved or closed) |
| 16 | `TFW-16` | snapshot |
| 17 | `TFW-17` | snapshot + task directory + index (unresolved or closed) |
| 18 | `TFW-18` | snapshot + task directory + index (unresolved or closed) |
| 19 | `TFW-19` | snapshot + task directory + index (unresolved or closed) |
| 20 | `TFW-20` | snapshot |
| 21 | `TFW-21` | snapshot + task directory + index (unresolved or closed) |
| 22 | `TFW-22` | snapshot + task directory + index (unresolved or closed) |
| 23 | `TFW-23` | snapshot + task directory + index (unresolved or closed) |
| 24 | `TFW-24` | snapshot + task directory + index (unresolved or closed) |
| 25 | `TFW-25` | snapshot + task directory + index (unresolved or closed) |
| 26 | `TFW-26` | snapshot + task directory + index (unresolved or closed) |
| 27 | `TFW-27` | snapshot + task directory + index (unresolved or closed) |
| 28 | `TFW-28` | snapshot |
| 29 | `TFW-29` | snapshot + task directory + index (unresolved or closed) |
| 30 | `TFW-30` | snapshot + task directory + index (unresolved or closed) |
| 31 | `TFW-31` | snapshot + task directory + index (unresolved or closed) |
| 32 | `TFW-32` | snapshot + task directory + index (unresolved or closed) |
| 33 | `TFW-33` | snapshot |
| 34 | `TFW-34` | snapshot |
| 35 | `TFW-35` | snapshot |
| 36 | `TFW-36` | snapshot + task directory + `status.md` → index |
| 37 | `TFW-37` | snapshot |
| 38 | `TFW-38` | snapshot + task directory + index (unresolved or closed) |
| 39 | `TFW-39` | snapshot |
| 40 | `TFW-40` | snapshot + task directory + index (unresolved or closed) |
| 41 | `TFW-41` | snapshot + task directory + index (unresolved or closed) |
| 42 | `TFW-42` | snapshot + task directory + index (unresolved or closed) |
| 43 | `TFW-43` | snapshot + task directory + index (unresolved or closed) |
| 44 | `TFW-44` | snapshot + task directory + `status.md` → index |
| 45 | `TFW-45` | snapshot + task directory + `status.md` → index |
| 46 | `TFW-46` | snapshot + task directory + index (unresolved or closed) |
| 47 | `TFW-47` | snapshot + task directory + index (unresolved or closed) |
| 48 | `TFW-48` | snapshot + task directory + index (unresolved or closed) |
| 49 | `TFW-49` | snapshot + task directory + index (unresolved or closed) |
| 50 | `TFW-50` | snapshot + task directory + index (unresolved or closed) |
| 51 | `TFW-51` | snapshot + task directory + index (unresolved or closed) |
| 52 | `TFW-52` | snapshot + task directory + index (unresolved or closed) |
| 53 | `TFW-53` | snapshot + task directory + index (unresolved or closed) |
| 54 | `TFW-54` | snapshot + task directory + `status.md` → index |
| 55 | `TFW-55` | snapshot + task directory + index (unresolved or closed) |
| 56 | `TFW-56` | snapshot + task directory + index (unresolved or closed) |
| 57 | `TFW-57` | snapshot + task directory + `status.md` → index |
| 58 | `TFW-58` | snapshot + task directory + `status.md` → index |
| 59 | `TFW-59` | snapshot + task directory + `status.md` → index |
| 60 | `TFW-60` | snapshot + task directory + `status.md` → index |
| 61 | `TFW-61` | snapshot + task directory + `status.md` → index |

**Unaccounted: 0.** Every identifier the board carried resolves after its removal.

## Task state written

Only for non-terminal tasks that have a directory. Every value comes from the
board or the directory; `unrecorded` marks a fact the source never carried.

| Task | Lifecycle | Authority | Note |
|---|---|---|---|
| `TFW-3` | RF | `HL-TFW-3__readme_public_readiness.md` |  |
| `TFW-4` | UNDECLARED | `HL-TFW-4__framework_cleanup.md` | status `🟡 TS` is outside the declared vocabulary — carried verbatim |
| `TFW-36` | KNW | `HL-TFW-36__content_marketing_blog_series.md` |  |
| `TFW-44` | HL_DRAFT | `HL-TFW-44__coordinator_quality_gates.md` |  |
| `TFW-45` | UNDECLARED | `HL-TFW-45__multi_agent_workflows.md` | status `❄️ FROZEN` is outside the declared vocabulary — carried verbatim |
| `TFW-54` | HL_DRAFT | `PROPOSAL__TFW-54__agent_team_mode.md` |  |
| `TFW-57` | TODO | `PROPOSAL__TFW-57__artifact_growth_control.md` |  |
| `TFW-58` | TODO | `PROPOSAL__TFW-58__revise_protocol.md` |  |
| `TFW-59` | TODO | `PROPOSAL__TFW-59__north_star_lifecycle.md` |  |
| `TFW-60` | RF | `HL-TFW-60__conflict_resistant_shared_workspace.md` |  |
| `TFW-61` | TODO | `PROPOSAL__TFW-61__collaboration_transport_modes.md` |  |

## Guarantees checked

| Guarantee | How |
|---|---|
| Zero renames, zero moves | the script has no rename or move call |
| Zero byte changes to existing artifacts | only paths that do not yet exist are opened for writing; an existing target aborts the run |
| No fact invented | absent facts are written as `unrecorded`; a lifecycle outside the vocabulary becomes `UNDECLARED` plus the verbatim value |
| Every row and directory accounted once | the reconciliation above sums to the source occurrence count |

---

*Migration accounting — TFW-60 / Phase A*
