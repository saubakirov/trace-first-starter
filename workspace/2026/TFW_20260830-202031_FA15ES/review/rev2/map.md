# Map rev2 — "What changed after the first review?"
> **Mindset:** Experienced newcomer. Understand the remediation before judging it.
> **Test:** "Can I explain what was changed, what was deliberately not changed, and why?"
> Prior REVIEW: [REVIEW__TFW_20260830-202031_FA15ES.md](../../REVIEW__TFW_20260830-202031_FA15ES.md)
> Revised RF object: `c623b79a632d11a3d396c2e74ac75f2ecaaffd23:workspace/2026/TFW_20260830-202031_FA15ES/RF__TFW_20260830-202031_FA15ES.md`
> TS: [TS__TFW_20260830-202031_FA15ES.md](../../TS__TFW_20260830-202031_FA15ES.md)
> Reviewed Executor head: `c623b79a632d11a3d396c2e74ac75f2ecaaffd23`
> Product commit: `626d77b5c3261dff493d15c7ce5862b9e036d10e`
> Reviewer branch / starting HEAD: `codex/tfw-fa15es-reviewer` / `f1ed604754ad3a98111d19e607b797e4c9855356`

## Understanding

The first review found no product defect but returned **REVISE** on D1: the durable trace did not contain a private-inclusive aggregate of the 28-file field source from before the original implementation. A later source read could not be relabelled as that missing historical observation.

The Executor did not rewrite history and did not edit the product. Instead, it performed a new clean implementation replay in a disposable checkout created from the exact product parent `e5e20f5b1070f48740d7d47bdd264ccc66ee524d`. The replay harness persisted an ordinal aggregate over all 28 source rows immediately before invoking the same bounded materializer, persisted it again immediately afterward, compared the two source states, recorded the materializer's source-write target set, and compared the entire replayed `editions/` tree with product commit `626d77b5…`.

The revised Executor commit changes exactly eight task-local RF/evidence paths. It adds the clean-replay narrative, harness, two source aggregate records, and a structured result; it revises RF, EV, and the source-integrity report to classify this correctly as **clean replay evidence, not an original historical observation**. It has zero `editions/` delta from the product commit.

## Prior finding → remediation map

| Prior order | Remediation | Intended proof |
|-------------|-------------|----------------|
| Persist a private-inclusive aggregate immediately before materialization | `replay-pre-source-aggregate.json`, written with exclusive creation and `fsync` before the materializer subprocess | Exact 28-row pre-implementation state for the clean replay |
| Persist the same aggregate immediately after | `replay-post-source-aggregate.json`, written after the subprocess and before evidence routing writes | Exact post-implementation state and pre/post equality |
| Prove no field-source write targets | The harness records `source_write_targets: []`; the materializer's resolved writes/deletes are confined to `editions/` | Source-write boundary |
| Bridge replay output to the delivered product | Full path/size/SHA-256 aggregate plus Git tree comparison against `626d77b5…:editions` | The replay implements the same delivered bytes, not a merely similar package |
| Revise RF/EV honestly | RF, EV, and source-integrity explicitly retain the original historical limitation and distinguish the new replay | No invented or relabelled evidence |

## Scope and unchanged holdings

- Remediation scope is evidence-only: 7 modified/new files under `evidence/` plus the task RF, all in the task workspace.
- The product remains commit `626d77b5c3261dff493d15c7ce5862b9e036d10e`: 30 product paths, only under `editions/`, yielding the same 24-file Assisted package.
- AC-2 through AC-11, all frozen budgets, privacy/neutrality findings, provider/binding behavior, template renders, and role separation are unchanged from the first review and are rechecked where regression risk exists.
- The first REVIEW and its three stage files remain the immutable record of the failed evidence-sufficiency pass.

## Declared limitation

The revised RF does **not** claim that the new files reconstruct the absent prewrite digest from the original run. That historical absence remains true. The remediation instead supplies a new complete implementation observation from the exact parent and proves that its output is byte/tree-equal to the delivered product. Whether this satisfies AC-1 is reserved for Verify and Judge.

## Checkpoint

**Self-check:**
- [x] Read the prior REVIEW and its exact two remediation orders?
- [x] Read the revised RF and all seven revised/new evidence files from the reviewed Git object?
- [x] Matched each remediation artifact to D1 without treating a narrative assertion as evidence?
- [x] Confirmed the product commit and frozen contract were not changed?

Stage complete: YES
