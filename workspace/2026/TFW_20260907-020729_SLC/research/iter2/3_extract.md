# Extract — Adoption and recovery outcomes
> **Mindset:** Analyst. Make every boundary observable.
> **Test:** A retry must distinguish unfinished migration from later project edits.
> Parent: [HL SLC](../../HL-TFW_20260907-020729_SLC.md)
> Goal: Define the minimum complete behavior to challenge.

## Configuration Space
Continue Gather's comparison matrix.

| Variant | Before first write | Interrupted observation | Scope of recovery |
|---|---|---|---|
| V1 | Pin authority, source and exact membership; preserve affected before-image | Old config/old state, old config/pruned state, or target config/pruned state | Revalidate and finish; refuse divergent affected fields |
| V2 | Same preparation | Target config/old state can expose removed IDs | Requires repairing before any ordinary gate |
| V3 | Git checkpoint | Index/tree/ref combinations, possibly later uncommitted work | Depends on external transaction/restore policy |

[Python's replacement API](https://docs.python.org/3/library/os.html#os.replace) covers a single path operation. The matrix models semantic cuts between individually complete writes; torn-file and process/power-loss behavior still require delivery-level validation.

## Findings
### E1: No-question adoption is a bounded decision table
| Observed receiver | Proposed migration consequence |
|---|---|
| New Full project | Template `[workspace]`, absent historical key, no task/history folder question |
| Existing single `[workspace]` or `[tasks]` | Preserve, including future creation |
| Custom path/order, including `[tasks, workspace]` | Preserve |
| Exact mixed `[workspace, tasks]`, tasks absent/empty | Narrow to workspace without creating history scaffolding, after accounting for any remembered missing IDs |
| Mixed with established historical-only disposition | Workspace active, tasks historical; exact digest reconciliation |
| Mixed with live work or unclear continuation | Keep reachability; use existing authority, otherwise one grouped material choice |
| Mixed with an already recorded decision to retain both active | Preserve unchanged; no repeated question |
| Already split active/history | Preserve; repair only an evidenced incomplete migration, not re-decide disposition |

Unresolved remembered IDs in an absent/empty secondary container do not authorize deleting them by prefix. The path default can normalize only if its connected state is safe; otherwise the affected group needs evidence/recovery. A new owner request to continue historical work is outside the automatic migration: read the source, then explicitly decide a new current task or another authorized scope change.

### E2: Minimal preparation is evidence, not another operational registry
For a migration that changes digests, preserve one immutable attachment under the existing update-receipt area before the first group/provenance write. Content: source identity and previous provenance; authority reference; affected old/new config fields; exact historical task paths/IDs; removed digest pairs; hashes needed to distinguish expected prior/target states. Copy no unrelated configuration or secrets. The final attempt receipt links it and records actual verification. No ordinary task command reads it; migration/re-entry alone uses it. A project without affected digests needs no digest backup.

This preparation must precede publication of version/provenance that could erase the intervening migration route. On equal-version re-entry, target workflow plus preserved prior provenance/applicable guide still select the incomplete group. Completed final state is verified from actual fields, never inferred from the version or a success receipt alone.

### E3: Proposed V1 sequence
1. Validate authority, relative distinct scopes, whole-ID membership and collisions across the reference union; verify historical-only disposition. If an affected problem is unresolved, preserve reachability and refuse the group.
2. Preserve immutable preparation evidence. Stage/validate compatible readers and intended field changes. Keep normal gates and task work outside this unfinished update group.
3. Re-read membership and affected fields. Reconcile exactly the allowed historical digest keys; retain every other current value, including intervening unrelated additions.
4. Publish active/history config only after coherent reader payload is present and state validation succeeds. Use one complete-file replacement per affected file; do not claim a two-file transaction.
5. Re-observe active state and historical reference behavior. Complete provenance, cleanup and the existing final receipt order only after checks succeed.
6. Re-entry with old config/pruned state finishes the config after revalidation. Divergence in authority, membership or affected values causes bounded refusal, not whole-tree rollback. Any safe restoration merges only the recorded affected fields and preserves later work.

### E4: Delivery proof and research proof differ
A set/fixture model can validate identities, deltas, retries and preservation invariants. It cannot prove a future agent follows the canonical guide, that a new supported installation actually asks no container question, or that a rebuilt site's historical links all resolve. Those are future phase acceptance checks, not excuses for another speculative research phase.

## Checkpoint
| Found | Remaining |
|---|---|
| Concrete adoption table, preparation boundary, state-first sequence and equal-version route | Execute identity/recovery probes, reject alternatives and settle H1-H3 |

**Sufficiency:** external source used: YES; Briefing gap closed for Extract: YES; Gather comparison extended: YES.
Stage complete: YES
Decision: proceed to final Challenge. Recommendations remain research output only.
