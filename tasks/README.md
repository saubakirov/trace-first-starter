# tasks/ — the legacy task container

This project has two task containers. New work goes to
[`workspace/`](../workspace/00-INDEX.md). This folder holds every task created before TFW
`2.0.0` and is not the place to create a new one.

## Why a second container exists

Legacy tasks use the `TFW-N` identifier grammar and live directly under `tasks/`. New tasks
use a clock-derived identifier and nest under a creation year:
`workspace/2026/20260826-143000__slug/`.

The obvious tidy-up — renaming the old corpus into the new grammar — was measured and
refused. At the `2.0.0` migration the old identifiers were carried by **7,505 references
across 666 files** and **271 commit subjects** in immutable Git history. Renaming would have
orphaned every one of them, and a trace that needs a translation table to be read has
already lost the property this framework exists to provide.

So nothing here was renamed, moved or byte-changed. The cost of a clean single sequence is
paid in trace integrity, and that is the one thing not for sale.

## What changed here at 2.0.0

Only additions:

- each task still in flight received a `status.md` — its live state, written in place;
- [`BOARD-SNAPSHOT.md`](BOARD-SNAPSHOT.md) captured all 61 rows of the root Task Board
  verbatim, on the day the board was removed.

No existing artifact in this folder was touched.

## Reading a legacy task

Both identifier grammars resolve everywhere. A task in flight has a `status.md` that is
authoritative for its state, exactly as a new task does. A task that finished before the
migration has no `status.md`; its row in the snapshot is the record.

Six rows in the snapshot are backlog ideas that never had a directory — TFW-16, TFW-20,
TFW-33, TFW-34, TFW-35 and TFW-39. They are ideas, not tasks. Picking one up means creating
a real task in `workspace/`, not resurrecting a row.

## Configuration

Resolution order comes from `tfw.task_containers` in
[`.tfw/project_config.yaml`](../.tfw/project_config.yaml):

```yaml
task_containers: [workspace, tasks]
```

A task is created in the **first** entry. A task is resolved by searching **every** entry in
order. That is one setting, not two supported layouts — a project migrating to `2.0.0`
either keeps one container or lists two, and nothing else in the method changes.

## When this folder empties

It does not. Terminal tasks keep their paths forever, and reverting a result never reverts
its trace. This container shrinks only in the sense that nothing new arrives in it.
