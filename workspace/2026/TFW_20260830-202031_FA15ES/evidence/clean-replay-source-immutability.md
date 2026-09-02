# Clean replay source-immutability proof — TFW_20260830-202031_FA15ES

> Date: 2026-09-02
> Reviewer finding: D1 in `REVIEW__TFW_20260830-202031_FA15ES.md` at `f1ed604754ad3a98111d19e607b797e4c9855356`
> Proof classification: **clean replay evidence, not an original historical observation**
> Disposable checkout: `E:\TEMP\tfw-fa15es-replay-d1-final2-23509e8`

## Purpose and confidentiality boundary

The original Executor trace did not durably persist the four private per-row hashes before implementation. This replay does not claim to recover that historical observation. It follows the Reviewer's requested remediation instead: start from the exact product parent, persist a private-inclusive aggregate immediately before the same bounded materializer, persist the same aggregate immediately after, prove zero source write targets, and prove the resulting complete `editions/` tree is byte-equal to the frozen product commit.

The canonical 28 source rows are ordered ordinally by POSIX-normalized relative path and encoded as `relative-path|size|sha256`, joined by LF with a final LF. All 28 rows, including the four private rows, contribute to the aggregate. Private filenames, contents, and per-row hashes are never printed or persisted; the internal source locator is supplied only through `TFW_FA15ES_SOURCE` and is not persisted.

## Exact checkout and command ledger

All commands completed with exit code 0. The source environment variable was set out of band before the proof command; its value is intentionally absent from public evidence.

| # | Working directory | Exact command | Exit |
|---:|---|---|---:|
| 1 | PowerShell | `New-Item -ItemType Directory -Path E:\TEMP\tfw-fa15es-replay-d1-final2-23509e8` | 0 |
| 2 | PowerShell | `git -C E:\TEMP\tfw-fa15es-replay-d1-final2-23509e8 init` | 0 |
| 3 | PowerShell | `git -C E:\TEMP\tfw-fa15es-replay-d1-final2-23509e8 remote add origin C:\Users\c0rpa\.codex\worktrees\4eac\steps-framework` | 0 |
| 4 | PowerShell | `git -C E:\TEMP\tfw-fa15es-replay-d1-final2-23509e8 fetch --no-tags origin e5e20f5b1070f48740d7d47bdd264ccc66ee524d 626d77b5c3261dff493d15c7ce5862b9e036d10e` | 0 |
| 5 | PowerShell | `git -C E:\TEMP\tfw-fa15es-replay-d1-final2-23509e8 switch -c codex/tfw-fa15es-executor e5e20f5b1070f48740d7d47bdd264ccc66ee524d` | 0 |
| 6 | PowerShell | `New-Item -ItemType Directory -Force -Path E:\TEMP\tfw-fa15es-replay-d1-final2-23509e8\workspace\2026\TFW_20260830-202031_FA15ES\evidence\attachments` | 0 |
| 7 | PowerShell | `Copy-Item -LiteralPath C:\Users\c0rpa\.codex\worktrees\4eac\steps-framework\workspace\2026\TFW_20260830-202031_FA15ES\evidence\attachments\materialize_assisted.py -Destination E:\TEMP\tfw-fa15es-replay-d1-final2-23509e8\workspace\2026\TFW_20260830-202031_FA15ES\evidence\attachments\materialize_assisted.py` | 0 |
| 8 | PowerShell | `Copy-Item -LiteralPath C:\Users\c0rpa\.codex\worktrees\4eac\steps-framework\workspace\2026\TFW_20260830-202031_FA15ES\evidence\attachments\replay_source_immutability.py -Destination E:\TEMP\tfw-fa15es-replay-d1-final2-23509e8\workspace\2026\TFW_20260830-202031_FA15ES\evidence\attachments\replay_source_immutability.py` | 0 |
| 9 | PowerShell | `git -C E:\TEMP\tfw-fa15es-replay-d1-final2-23509e8 rev-parse HEAD` | 0 |
| 10 | PowerShell | `git -C E:\TEMP\tfw-fa15es-replay-d1-final2-23509e8 branch --show-current` | 0 |
| 11 | PowerShell | `git -C E:\TEMP\tfw-fa15es-replay-d1-final2-23509e8 diff --exit-code` | 0 |
| 12 | PowerShell | `git -C E:\TEMP\tfw-fa15es-replay-d1-final2-23509e8 status --short` | 0 |
| 13 | `E:\TEMP\tfw-fa15es-replay-d1-final2-23509e8` | `D:\python\Python313\python.exe workspace/2026/TFW_20260830-202031_FA15ES/evidence/attachments/replay_source_immutability.py` | 0 |

Checkout verification before any replay write:

| Field | Observed |
|---|---|
| branch | `codex/tfw-fa15es-executor` |
| HEAD | `e5e20f5b1070f48740d7d47bdd264ccc66ee524d` |
| tracked worktree state | clean |
| permitted untracked state before proof | task-local `evidence/` containing only the copied harness/materializer |

## Persisted pre/post aggregate

| Snapshot | Persisted at | Files | Bytes | Private-inclusive aggregate SHA-256 |
|---|---|---:|---:|---|
| immediately before materialization | `2026-09-02T17:05:54.391370+05:00` | 28 | 297,522 | `5c609354c68e8043b121b75ee4ad4a5ced70908462ed3f1ba2c82c03b3195bf2` |
| immediately after the materializer subprocess | `2026-09-02T17:05:54.795709+05:00` | 28 | 297,522 | `5c609354c68e8043b121b75ee4ad4a5ced70908462ed3f1ba2c82c03b3195bf2` |

Pre/post equality: **PASS**. The pre snapshot was opened with exclusive create, flushed, and `fsync`-persisted before the materializer subprocess started. The post snapshot used the same persistence rule immediately after that subprocess completed and before either routing target was written.

## Materialization and write-target proof

The copied materializer SHA-256 was `56c2039517f0a7fc257b73356330507f55e1b97bfb73b1cd65f24b3be6a8c631`. It returned:

```text
MATERIALIZED=23 field-derived writes + 5 deletions
SOURCE_LINE_REPLACEMENTS=205
ROUTING_DOCS_PENDING=2
```

The remaining routing targets were written deterministically from the exact frozen product objects:

| Target | Bytes | SHA-256 | Object authority |
|---|---:|---|---|
| `editions/README.md` | 3,130 | `1a4229a02f02c0e013edab4d1fa02f2e25be77993801bdc08cb7407cbcec0814` | `626d77b5…:editions/README.md` |
| `editions/ASSISTED_MAINTENANCE.md` | 8,053 | `072c4acea8590d3605a525e34d760ca5b67abe381bfce9e99e08f5ed1c3c7ab2` | `626d77b5…:editions/ASSISTED_MAINTENANCE.md` |

The persisted result contains the exact 28 materializer targets plus the two routing targets. Product write-target count is exactly 30. Every target resolves under the disposable checkout's `editions/` tree; source write targets are `[]` and source write-target count is **0**.

## Whole-product tree equality

The comparison covered the complete `editions/` tree, not only changed paths.

| Side | Files | Bytes | Canonical aggregate SHA-256 |
|---|---:|---:|---|
| frozen product commit `626d77b5c3261dff493d15c7ce5862b9e036d10e` | 30 | 293,321 | `5944aa9b1fcf4f2816cc562d6e0b5cd16b6e09a52c8d0b542efb26f01515b532` |
| replayed working `editions/` tree | 30 | 293,321 | `5944aa9b1fcf4f2816cc562d6e0b5cd16b6e09a52c8d0b542efb26f01515b532` |

- expected Git tree OID: `8c12e1c66f5d961de44dbc9c9a0d3cd54bd06cdc`;
- missing paths: 0;
- extra paths: 0;
- byte/content mismatches: 0;
- byte and tree equality: **PASS**.

## Sanitized proof artifacts

- [replay-pre-source-aggregate.json](attachments/replay-pre-source-aggregate.json)
- [replay-post-source-aggregate.json](attachments/replay-post-source-aggregate.json)
- [replay-result.json](attachments/replay-result.json)
- [replay_source_immutability.py](attachments/replay_source_immutability.py)

Clean replay verdict: **PASS**. This closes Reviewer D1 by reproducible clean replay, while preserving the truthful statement that no original private-inclusive pre-implementation aggregate was historically recorded.
