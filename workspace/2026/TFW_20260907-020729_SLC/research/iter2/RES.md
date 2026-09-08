# RES — TFW_20260907-020729_SLC: Workspace default and safe historical access
> **Date:** 2026-09-08
> **Author:** robert (Researcher, Codex)
> **Status:** RES — Complete, research sufficient
> **Parent HL:** [HL SLC](../../HL-TFW_20260907-020729_SLC.md)
> **Mode:** Pipeline / focused, iteration 2
> **Boundary:** Research only. No HL amendment, TS, implementation, receiver migration or release was performed.

## Research Context
SLC can deliver one workspace default without moving legacy files or rewriting historical links. The smallest complete design separates current work from historical reading and migrates only the digest state affected by that separation. Two iterations examined 27 initial combinations, independently reproduced helpdesk's failure, and challenged the preferred recovery model. Source baseline is `49ddad02f97dfb46919bdd19292902b9082d696f`; approved HL freeze is `dedf339`. The acting principal is owner-selected `robert`, accountable to `saubakirov`, in the same bounded non-AT research task `01a08164-fb6d-78a3-b41a-e0fabdc680c9`; no child units or amendment mandate are claimed.

## Briefing
[Iteration 2 Briefing](1_briefing.md), [Gather](2_gather.md), [Extract](3_extract.md), [Challenge](4_challenge.md); predecessor [iteration 1 RES](../iter1/RES.md). The owner authorized completing research autonomously and expressly withheld implementation. The prior Knowledge Gate waiver was respected without changing gate configuration.

## Decisions
| # | Decision | Rationale |
|---|---|---|
| D5 | Recommend `tfw.historical_containers` as the sole optional history setting; retain `task_containers` for working paths | Plain path lists preserve the existing project-owned schema; new projects receive no archive field |
| D6 | Creation and ordinary discovery use active paths; exact reference reading, existing-project detection and compilation use the reference union | Historical access remains possible without routinely reopening history |
| D7 | Preserve every single/custom choice; automatically migrate only the frozen HL's unambiguous mixed cases | A new default does not establish an old user's intent |
| D8 | Remove only remembered keys whose whole IDs are verified in the retiring container | Preserve unaffected digests, knowledge, stats and dates; no prefix pruning or invented processing |
| D9 | Use an immutable before-image in the existing update attachment area, state before final config, and present-state re-entry | Seven semantic cut/repeat cases converge; later active changes survive; no new controller or runtime required |
| D10 | Stop research as sufficient for Coordinator review | Remaining checks require implementation/native execution, not another speculative research iteration |

D5-D9 refine iteration 1 D1-D4; none reverses them.

### Proposed configuration
A new Full project has only:

```yaml
tfw:
  task_containers: [workspace]
```

An established historical receiver, including this repository after the later approved migration, has:

```yaml
tfw:
  task_containers: [workspace]
  historical_containers: [tasks]
```

An existing `task_containers: [tasks]` remains valid, including future creation there. This is a recommendation, not an applied config change.

### Receiver consequences
| Before | After | Container questions |
|---|---|---|
| New supported Full installation | Workspace only; no history field/folder | 0 |
| Existing single workspace/tasks or custom paths/order | Preserve choice | 0 |
| Exact mixed workspace/tasks, absent or empty tasks with determinate state | Workspace only | 0 |
| Mixed with established historical-only tasks | Workspace active, tasks historical; exact digest reconciliation | 0 |
| Mixed with live/unclear continuation | Preserve reachability until resolved | One grouped decision only if existing authority cannot settle it |
| Mixed with an existing decision to keep both active | Preserve that decision | 0 repeated |
| Already migrated | Preserve; re-observe incomplete update if applicable | 0 repeated |

An absent directory plus unmatched remembered IDs is an evidence defect, not permission to delete keys by prefix. Existing explicit historical disposition can settle missing modern task statuses without fabricating completion. Our baseline has 53 historical tasks, 42 without `status.md`, 53 affected digest keys and 11 unaffected keys.

### Minimal recovery contract
Before migration/provenance publication, preserve pinned source and previous provenance, governing disposition, affected old/new fields, exact historical membership and removed digest pairs as one immutable update attachment. Then make compatible readers available, revalidate inputs, reconcile those keys and publish the final config. Verify the actual receiver before completing the ordinary receipt. On interruption, finish the evidenced group or refuse divergent affected input while preserving subsequent project work. Do not restore a whole old map or repository.

This is recoverable sequential application. It does not promise an instantaneous switch for arbitrary concurrent readers. The existing updater must complete/recover its group before ordinary gate arithmetic; equal-version re-entry must retain the applicable migration route. A before-image is preservation evidence read during migration/recovery, not a current-state registry or a new archive feature.

## Open Questions
| # | Question | Status | Answer |
|---|---|---|---|
| Q1 | Is a mass link rewrite necessary? | Resolved | No. Keep source paths, IDs, relative references and public `tasks/` URLs; change the readers that need the union |
| Q2 | Does helpdesk demonstrate the risk? | Resolved for a pinned snapshot | Commit `31baa3444cfe98b35bda03688b5b4eafdc2d43a4` retains 30 historical task directories and remembered IDs with an unchanged state blob; the unchanged oracle reproduces exactly 30 removed IDs |
| Q3 | Did the workspace template cause that receiver change? | Not established; attribution rejected | The receipt pins a source whose template was still tasks and explicitly excludes the owner's dirty edit; receipt preservation claims disagree with the later committed config |
| Q4 | Must old tasks be declared DONE? | Resolved | No. A container disposition limits operations and does not rewrite lifecycle truth |
| Q5 | Does the design require a new migration engine? | Resolved at research level | No. Existing version-addressed update, preserved evidence and re-entry suffice with an explicit SLC field/state exception |
| Q6 | Is another owner decision needed now? | Resolved | No research decision is missing; implementation remains outside the current authorization |

## Hypotheses (from HL §10)
| # | Hypothesis | HL Status | RES Status | Evidence and limit |
|---|---|---|---|---|
| H1 | One optional historical-path setting and affected readers suffice without registry/lifecycle machinery | Open | Supported | Existing walker accepts explicit union; operation boundaries mapped; no historical file relocation needed |
| H2 | Clean template and existing entry guidance suffice for every new-project route | Open | Supported for supported Full installation | Existing copy/templates route verified in source; full framework clone preserves its actual history; native init acceptance remains for delivery |
| H3 | Existing version-addressed update/receipt/re-entry can migrate and preserve resolved choices without another control file | Open | Supported with specified recovery conditions | Real receiver fixture plus seven semantic cut/repeat cases and six refusal cases; preservation attachment is evidence, not runtime state; no native updater/crash proof claimed |

## HL Update Recommendations
The Researcher classifies only. Frozen HL and free sections remain byte-identical to the research baseline.

### Refinements — free sections, coordinator applies
| # | § | What to update | Source |
|---|---|---|---|
| R1 | §2, §7.2 | Replace helpdesk's reported-only status with the exact verified commit, omitted HD-29, unchanged state blob and receipt/config discrepancy; retain attribution limits | iter1 G3/G4/C1 |
| R2 | §8, §10 | Select active plus optional historical lists and mark H1-H3 research-supported with native verification limits | D5-D9; both RES |
| R3 | §9 | Specify exact-ID state exception, before-image preparation, state-first publication and equal-version recovery; reject multi-file atomicity claims | iter2 E2/E3/C1/C2/C5 |
| R4 | §8, §11 | Include history-only init, read-only historical resume and full-reference compiler tests; re-read PTTC and the parallel Knowledge Gate task before fixing implementation baseline | iter2 G2/G4/C4 |
| R5 | §11 | Record research sufficient and awaiting Coordinator consideration; do not infer permission to implement | D10, owner instruction |

### Amendment Proposals — frozen sections, resolved-ruler verdict required
No amendment proposals. The contract already permits safe completion or refusal of partial migration and preserves old task truth.

## Delivery Surfaces and Acceptance Evidence
This is a reader map for later planning, not a TS or executable assignment.

| Surface | Necessary responsibility |
|---|---|
| `.tfw/templates/project_config.yaml`, helper fallback in `tools/tfw_state.py`, current init guidance | Workspace default, no inherited upstream config/history, no container-specific interview |
| `.tfw/conventions.md`, `.tfw/compilable_contract.md` | Active versus reference operations, original paths/URLs, no inferred lifecycle |
| `.tfw/workflows/init.md`, `.tfw/workflows/resume.md` | Recognize initialized history-only projects; show historical citations without automatically continuing them |
| `tools/tfw_state.py`, `docs/scripts/gen_docs.py` | One minimal union reader, existing whole-ID/collision rules, four compiler uses: globs, output mapping, landings, resolver |
| `.tfw/workflows/update.md`, relevant `knowledge.md` scope/state wording, version-addressed guide and changelog route | Prescribed compatible migration, bounded state exception, recovery and same-major/equal-version routing |
| This repository's `.tfw/project_config.yaml`, `.tfw/knowledge_state.yaml`, optional `tasks/README.md` clarification | Apply owner disposition later; change zero historical task directories |
| Existing state/compiler/integration/runtime-context tests and affected manifest copies | Verify actual consumers; follow PTTC's accepted file placement; avoid unrelated test refactoring |

Actual later acceptance must cover supported fresh init, all preserved/mixed cases, exact historical lookup and a real docs build, unchanged historical bytes, unaffected knowledge/digests, repeated/interrupted updater runs, and release guide routing. Test the real compiler rather than only a copied prefix-glob helper. Source tests, a reference model and a native receiver run must remain separately labeled.

Research observed: helpdesk snapshot restored mixed = 35 discovered/0 removed/3 pending; narrowed plus exact reconciliation = 5/0/3. The forwarded 4/5 may describe later work and was not established by this snapshot. Seven model cuts repeat cleanly, six conflicting input cases refuse without mutation, later active data survive, HD-1 never prunes HD-10, and a cross-scope duplicate raises the existing collision error.

Artifact validation (not an independent REVIEW): both iteration records complete; eight stage checkpoints complete; both RES structures and local links valid; task status and new journal event pass the existing semantic validators; HL byte-identical; zero product-file changes and no TS. Research is retained in the isolated `codex/slc-research-robert` worktree for Coordinator review; the root checkout's separate owner template edit is untouched.

## Fact Candidates
No new fact candidates. Conversation history was checked; workspace-only intent, the temporary mixed layout and preservation of deliberate tasks choices already exist in the governing HL. Research observations are independently discoverable and are recorded as evidence, not duplicated as human-only facts.

## Strategic Insights (Research)
No new strategic insights. The owner's Saint-Exupery direction is already a frozen design test. Its application here removes the archive interview, per-task closure exercise, extra lifecycle/map/controller and mass rename while retaining the readers and recovery needed for continuity.

## Findings Map
| Cause / fact | Result | Necessary response |
|---|---|---|
| One old list serves current work and history | Dropping tasks hides historical inputs | Optional history list and selective union readers |
| Persisted digest keys outlive a scope change | Helpdesk reports 30 removed despite intact files | Exact one-time reconciliation |
| 42 old source tasks lack modern state | Per-task completion gate invents work | Use established container disposition, preserve task bytes |
| Two live files change sequentially | A partial update is observable | Prepared evidence, explicit re-entry, honest completion check |
| Existing projects own their layout | Default replacement can override intent | Preserve singles/custom/retained-active decisions |

## Iteration Status
- **Iteration:** 2 of 2 (min) / 5 (max)
- **Hypotheses tested:** H1 supported; H2 supported for supported install route; H3 supported with explicit bounded recovery
- **Hypotheses deferred:** None
- **Gaps discovered:** No research blocker. Future native init/update/site behavior and filesystem failure handling require phase acceptance.
- **Superseded decisions:** None; D5-D9 make D1-D4 concrete.

### Open Threads (for next iteration)
No further research iteration is recommended. Before later TS, the Coordinator re-reads accepted PTTC/Knowledge Gate changes and classifies these free-section recommendations. Release numbering and exact candidate/file scope belong to later authorized planning/release gates.

### Recommendation
- [x] **SUFFICIENT** — return to the owner/Coordinator for consideration through `/tfw-plan`.
- [ ] **MORE NEEDED**
- [ ] **BLOCKED**

Research sufficiency does not authorize TS or implementation. The current task lifecycle remains RES, with both iterations complete.

## Conclusion
The minimal complete change is a workspace default, one optional historical-path setting for old projects, preserved historical readers and a narrowly scoped recoverable state migration. Research disproved the need for mass historical edits, verified the receiver failure without assigning unsupported blame, and found init/resume and interrupted-update boundaries that a template-only edit would miss. Its limitation is explicit: source inspection and disposable models support the design, while actual receiver and site acceptance await an authorized implementation. Stop here and return the requested Russian summary.
