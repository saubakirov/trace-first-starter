# Challenge — Recovery and scope stress test
> **Mindset:** Critic. A successful model is not native delivery evidence.
> **Test:** Preserve unrelated new work and refuse ambiguous affected changes.
> Parent: [HL SLC](../../HL-TFW_20260907-020729_SLC.md)
> Goal: Settle the research recommendation and expose delivery limits.

## Consistency Check
| Variant | Result | Reason |
|---|---|---|
| V1: prepared evidence, state before final config | Survives with explicit update-group re-entry | Seven semantic cut cases converge; no introduced removed-ID cut; intermediate pending work is not a completed migration |
| V2: config before state | Reject | Real helpdesk fixture exposes 30 removed IDs before reconciliation |
| V3: Git-only checkpoint/restore | Reject | Adds a receiver prerequisite and risks later unrelated work; no need demonstrated |

No unexpected new survivor displaces iteration 1 C1. Its richer-schema reserve still has no benefit for the approved need.

## Findings
### C1: Seven semantic cut states converge in a disposable reference model
Ran a reference state model in Python 3.13 with existing `tfw_state` readers, bytecode disabled, at `E:/TEMP/tfw-slc-boundaries-ug2u5myp`. Inputs: old config `[workspace,tasks]`; target active `[workspace]` plus historical `[tasks]`; historical ID `HD-1` with digest `a*64`; active `HD-10` with `b*64`. Recovery validates authority, retained preparation, identical historical membership, old-or-target affected config and absent-or-original affected digest values, then computes current map minus exact historical IDs and target config.

| Observed cut | Expected recovery | Result |
|---|---|---|
| After preparation | Revalidate and apply state/config | PASS |
| After compatible reader payload | Revalidate and apply state/config | PASS |
| After state reconciliation | Preserve pruned state, finish config | PASS |
| After config | Verify actual final pair | PASS |
| After verification | Verify final pair; finish remaining update steps | PASS |
| After provenance | Re-observe final pair; do not infer completion from version | PASS |
| After receipt | Re-observe; second migration effect is empty | PASS |

Each row was immediately run a second time with identical results. The model deliberately does not simulate a filesystem crash or an agent's execution of the guide.

### C2: Six divergent inputs refuse without mutation
Missing recovery evidence, withdrawn authority, changed historical membership, divergent affected config, changed historical digest and an unrelated absent remembered ID each raise refusal and leave both input structures unchanged. These are evidence/model checks, not a new permission questionnaire. An interrupted attempt without its before-image cannot claim verified recovery; current evidence can still authorize a separately observed fresh migration, but it cannot reconstruct or restore unknown prior values.

A later changed active digest (`HD-10: c*64`) and a new current task digest (`HD_20260908-120000_NEW: d*64`) survive recovery together. No complete old map is restored.

### C3: Existing walker supports the intended scope separation
The fixture contains `tasks/HD-1__old`, `workspace/2026/HD-10__current`, and `workspace/2026/HD_20260908-120000_NEW`. Existing default discovery returns active tasks only; passing the union explicitly returns both scopes. Whole-ID subtraction removes HD-1 without touching HD-10. Adding `workspace/HD-1__collision` makes the existing union walker raise `IdentifierCollisionError`; migration must validate the union before separating scopes. This is executed reader behavior, not a new implementation.

For future configuration acceptance, reject an ambiguous active/history overlap, aliases resolving to the same path, repository escape, or duplicate whole ID before applying the group. Preserve unrelated existing choices; do not use SLC to redesign all path validation.

### C4: Necessary scope is small but greater than a template line
Core delivery surfaces are the template/default, shared operation rules, four compiler reader uses, init/resume boundaries, version-addressed update/state exception, and this repository's config/digest pair. The 53 old task directories require zero edits. `tasks/README.md` may need one container-level explanation. The Config Sync Registry needs no project-specific path propagation. Adapter copies follow only changed canonical sources.

A source inspection also found `docs/scripts/test_gen_docs.py:_task_glob` duplicates a resolver with prefix globs. Do not use that imitation as sole evidence of exact historical resolution; SLC assurance must exercise actual compiler behavior and keep the integration landing assertion over the full reference corpus. This does not authorize a general test refactor.

### C5: The bounded recovery claim survives, not universal atomicity
[Python os.replace](https://docs.python.org/3/library/os.html#os.replace) still supplies no cross-file transaction. The recommended protocol isolates an unfinished semantic update from its own ordinary gate and resumes it explicitly. It does not guarantee arbitrary concurrent third-party readers see an instantaneous switch, or that a torn file is recoverable without intact evidence. Frozen HL §3/DoF already permit safe completion or refusal of a partial migration; no stronger promise or new controller is necessary.

## Checkpoint
| Found | Remaining |
|---|---|
| C1/V1 survives seven cut/repeat cases and six refusal cases; later active work preserved; exact IDs and collision behavior verified | Future implementation/native receiver/site acceptance only; no research blocker |

**Sufficiency:** external source used: YES; Briefing gap closed for Challenge: YES; all matrix variants challenged: YES.
Stage complete: YES
Decision: research is sufficient for Coordinator review. Synthesize iteration 2, return a summary and stop before HL/TS/implementation.
