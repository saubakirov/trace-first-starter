# Challenge — What do we NOT expect?
> **Mindset:** Critic. Attack both simplification and recovery claims.
> **Test:** Distinguish a recoverable update from an imaginary atomic multi-file transaction.
> Parent: [HL SLC](../../HL-TFW_20260907-020729_SLC.md)
> Goal: One workspace default with compatible historical access.

## Consistency Check

Pairs were checked for Representation × Digest, Representation × Recovery, and Digest × Recovery. None is technically impossible as data structures; the following choices fail the frozen contract or add avoidable machinery.

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible with the selected contract |
|---|---|---|---|---|
| Any representation | A/B/C | Digest treatment | B | Every ordinary gate must resolve history to exempt remembered IDs, violating exclusion of history from that operation |
| Any representation | A/B/C | Digest treatment | C | A second permanent digest map adds ongoing archive state without a required current-work function |
| Any representation | A/B/C | Recovery | B | New migration controller/lock is outside the no-new-registry/runtime direction |
| Any representation | A/B/C | Recovery | C | Receiver compatibility cannot require a clean Git transaction or whole-tree restore |

Representation C also fails the final active-only meaning of `task_containers` by retaining historical paths in that list. Representation B is technically viable but changes the schema of every existing path entry; it loses the minimum-change comparison.

| Config | Representation | Digest treatment | Recovery | Result |
|---|---|---|---|---|
| C1 | A | A | A | Preferred, conditional on explicit interrupted-state recovery |
| C10 | B | A | A | Technically viable reserve; rejected for unnecessary schema migration |

Unexpected survivor: C10 can meet behavior and recovery requirements; “more complex” is a cost judgment, not proof it cannot work.

## Findings

### C1: Real-receiver snapshot reproduces the scope error
Using Python 3.13/PyYAML 6.0.3 as optional upstream research tools, materialized only tracked `tasks/`, `workspace/` and config/state from helpdesk commit `31baa3444cfe98b35bda03688b5b4eafdc2d43a4` into `E:/TEMP/tfw-slc-research-dmfp8sfk`. Imported the unchanged source-baseline `tools/tfw_state.py` with bytecode writing disabled and ran `knowledge_pending` on four fixture variants. No receiver file was written.

| Fixture variant | Discovered | Removed | Pending | Other problems |
|---|---:|---:|---:|---:|
| Committed narrowed config + unchanged state | 5 | 30 | not computed | 0 |
| Restored mixed config + unchanged state | 35 | 0 | 3 | 0 |
| Historical keys pruned, config still mixed | 35 | 0 | 33 | 0 |
| Narrowed config + exactly pruned state | 5 | 0 | 3 | 0 |

The 30 IDs are exactly HD-1...HD-28, HD-30, HD-31. Three unaffected remembered entries are preserved. The three pending current IDs are `HD_20260903-160919_BIAI`, `HD_20260907-030535_RFU`, and `HD_20260907-122117_AAT`. This immutable snapshot does not corroborate the later reported 4/5 count, nor contradict a later working-tree delta. This is execution of the existing oracle against real receiver files in a fixture, not native execution of a future updater.

### C2: Neither write order is an atomic migration
The official [Python os.replace documentation](https://docs.python.org/3/library/os.html#os.replace) describes one replacement operation; it does not supply a transaction spanning config and knowledge state. The fixture demonstrates both intermediate outcomes. Prefer state reconciliation before final config publication to avoid introducing removed IDs, but that alone leaves history pending after a crash. The update must recover its connected group before running an ordinary gate or announcing completion. Do not claim concurrent readers can never observe an intermediate state.

### C3: Existing recovery can carry a narrowly scoped preservation attachment
A candidate migration can prepare immutable evidence in the existing update-receipt attachment area before changing live fields: pinned source, governing disposition, exact historical path/ID membership, affected old/new config values, and the digest pairs to remove. It is a fixed before-image for this update, not a runtime registry, per-task marker, or another configuration setting. Preserve the attachment across interruption; seal the ordinary attempt receipt only at the workflow's existing final checkpoint. Re-entry recomputes current membership/authority and reconciles affected fields only. No blanket restore may erase later work. Iteration 2 must test every cut and disagreement case.

### C4: Local updater rules need an explicit exception
The present update rule says never overwrite project knowledge state. The SLC guide must distinguish payload exclusion from the compatible semantic removal of verified historical keys, with active entries/stats/dates/facts preserved. Otherwise a conscientious updater either repeats helpdesk's config-only failure or refuses all state reconciliation. This is an implementation refinement within HL §3, not authority to change the unrelated gate mode.

## Checkpoint

| Found | Remaining |
|---|---|
| C1 preferred; receiver failure and two intermediate states measured; no bulk link rewrite required | Adversarial recovery matrix, exact no-question adoption rules, init/historical access boundaries and delivery surfaces |

**Sufficiency:** external source used: YES; Briefing gap closed for Challenge: YES; all dimension pairs checked: YES; survivors listed: YES.

Stage complete: YES
Decision: synthesize iteration 1, then use the already authorized second iteration to test C1's remaining conditions. Implementation remains excluded.
