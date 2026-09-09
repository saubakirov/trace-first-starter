# tasks/ — the legacy task container

Current work goes to [`workspace/`](../workspace/). This historical container retains the
pre-2.0.0 corpus at its original paths. It stays available to exact citations and documentation,
and is excluded from ordinary current-work discovery and the Knowledge Gate.

## Why a second container exists

Legacy tasks use the `TFW-N` identifier grammar and live directly under `tasks/`. Current tasks
use `workspace/{YYYY}/{PREFIX}_{YYYYMMDD}-{HHMMSS}_{ABBR}/`; the earlier dirty-clock grammar
illustrated by `workspace/2026/20260826-143000__slug/` remains readable history.

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

All three identifier grammars remain readable. Existing `status.md` and snapshot records retain
their original meaning; historical disposition does not assert that every task finished. Exact
historical resume reads the cited trace without changing state or silently starting continuation.

Six rows in the snapshot are backlog ideas that never had a directory — TFW-16, TFW-20,
TFW-33, TFW-34, TFW-35 and TFW-39. They are ideas, not tasks. Picking one up means creating
a real task in `workspace/`, not resurrecting a row.

## Configuration

Active and historical reachability come from
[`.tfw/project_config.yaml`](../.tfw/project_config.yaml):

```yaml
task_containers: [workspace]
historical_containers: [tasks]
```

A task is created in the **first active** entry. Exact reading and documentation use the
deduplicated active-plus-historical union; current discovery uses only active paths. The 3.3.0
transition follows the owner's recorded historical disposition and exact digest reconciliation,
without moving or rewriting any task artifact. Existing single/custom project choices remain valid.

## When this folder empties

It does not. Terminal tasks keep their paths forever, and reverting a result never reverts
its trace. This container shrinks only in the sense that nothing new arrives in it.
