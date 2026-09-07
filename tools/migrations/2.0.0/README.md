# TFW 2.0.0 board migration bundle

Use this self-contained bundle only to convert a pre-2.0 root Task Board into task-local
state and an immutable board snapshot. Acquire `tools/migrations/2.0.0/` from the same
immutable upstream release ref as the Full payload being installed; do not copy the current
moving branch into an older receiver.

## Prerequisites and stop conditions

1. Confirm `python --version` succeeds. If Python is unavailable, stop before copying or
   changing receiver files and obtain Python through your platform's trusted package route.
2. Create a temporary virtual environment outside the receiver if possible and install
   `requirements.txt` into it. Do not add Python or PyYAML to the receiver's runtime.
3. `python migrate_board.py --help` remains available without PyYAML. Any other invocation
   without PyYAML exits `2` before project discovery, planning, or receiver writes and names
   the missing dependency.
4. Work from a clean, backed-up repository. The default is a dry run over the committed
   `HEAD:README.md`; it neither silently reads a changing working tree nor overwrites files.

## Procedure

From the receiver root, with `BUNDLE` naming the acquired immutable directory:

```bash
python "$BUNDLE/migrate_board.py" --root .
python "$BUNDLE/migrate_board.py" --root . --manifest migration-accounting.md
python "$BUNDLE/migrate_board.py" --root . --apply
```

Use `--board`, `--board-heading`, or `--board-rev` when the historical source differs.
`--working-tree` is an explicit opt-in to an uncommitted source. The apply step refuses any
existing target; `--skip-existing` leaves those targets untouched and writes only missing
ones. Review the dry-run reconciliation, accounting, target set, and snapshot before apply.

Rollback is repository-native: remove only newly created migration targets after verifying
their exact list in the accounting output, or restore the clean backup. Never rewrite an
existing journal or task carrier to make a newer rule appear satisfied.
