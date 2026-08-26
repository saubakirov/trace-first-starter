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
| `TFW-54` | HL_DRAFT | `HL-TFW-54__agent_team_mode.md` |  |
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
