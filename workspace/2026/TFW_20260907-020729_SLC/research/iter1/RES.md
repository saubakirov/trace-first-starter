# RES — TFW_20260907-020729_SLC: Minimal container model
> **Date:** 2026-09-08
> **Author:** robert (Researcher, Codex)
> **Status:** RES — Complete, iteration 1
> **Parent HL:** [HL SLC](../../HL-TFW_20260907-020729_SLC.md)
> **Mode:** Pipeline / focused

## Research Context
The frozen SLC contract requires a workspace default, preservation of existing choices and historical access. This iteration compared 27 configuration/digest/recovery combinations and verified the reported helpdesk failure against its immutable commit. Acting principal and bounded non-AT authorization are recorded in Briefing: same Researcher, no child units or amendment authority, no implementation.

## Briefing
[Iteration 1 Briefing](1_briefing.md); evidence chain [Gather](2_gather.md), [Extract](3_extract.md), [Challenge](4_challenge.md). Source baseline: `49ddad02f97dfb46919bdd19292902b9082d696f`; HL freeze: `dedf339`.

## Decisions
| # | Decision | Rationale |
|---|---|---|
| D1 | Prefer active `task_containers` plus optional `historical_containers`; no history field in a new template | C1 preserves existing list semantics and the one-working-folder result with minimum schema change |
| D2 | Preserve historical paths and compiler `tasks/` URLs; widen historical readers only | Discovery and references currently share a reader, not a necessary storage identity |
| D3 | Reconcile only exact historical digest keys once, as a migration exception | Recurring historical filtering defeats active-only gates; wholesale reset destroys unrelated state |
| D4 | Test existing update preparation/attachment/re-entry before declaring H3 settled | Two file writes have observable intermediate states; config-first reproduces helpdesk |

## Open Questions
| # | Question | Status | Answer |
|---|---|---|---|
| Q1 | Does a new installer need to be introduced? | Answered at source level | No; existing clean copy/template route suffices, subject to later actual init acceptance |
| Q2 | Is helpdesk's report technically supported? | Answered for pinned snapshot | Exactly 30 removed IDs reproduced; retained task files and unchanged state proven; 4/5 not corroborated at this snapshot |
| Q3 | Can the migration recover without a new control system? | Carry to iteration 2 | Candidate uses an immutable preservation attachment and affected-field re-entry; cut/disagreement cases still require challenge |

## Hypotheses (from HL §10)
| # | Hypothesis | HL Status | RES Status | Evidence |
|---|---|---|---|---|
| H1 | One optional history setting suffices | Open | Supported by source analysis | Four compiler uses and existing explicit-container walker hook; iter1 G1/E1/C1 |
| H2 | Templates and existing clean entry guidance suffice | Open | Supported, native delivery untested | iter1 G2; current template/fallback mismatch identified |
| H3 | Existing update machinery suffices without another control file | Open | Conditional | iter1 C2/C3; preservation attachment is evidence, but recovery remains to be tested |

## HL Update Recommendations
The Researcher classifies only. No HL section was edited.

### Refinements — free sections, coordinator applies
| # | § | What to update | Source |
|---|---|---|---|
| R1 | §2, §7.2 | Upgrade helpdesk from reported to independently observed, retaining pinned commit and the receipt/config discrepancy | G3/G4, C1 |
| R2 | §8, §10 | Carry C1 and its exact reader/digest split as the leading design; do not imply multi-file atomicity | E1/E3, C2 |
| R3 | §9, §11 | Require interrupted-state and present-receiver verification before migration success | C2/C3 |

### Amendment Proposals — frozen sections, resolved-ruler verdict required
No amendment proposals.

## Fact Candidates
No new fact candidates. Conversation history was checked: the owner's workspace-only preference, temporary dual-list history, preservation of deliberate tasks choices and Knowledge Gate exception are already captured in the governing HL. Receiver/code observations are independently discoverable technical evidence, not new human-only facts.

## Strategic Insights (Research)
No new strategic insights. The owner's simplicity direction already governs HL §7 and was used to compare alternatives.

## Findings Map
| Observation | Causal consequence | Design implication |
|---|---|---|
| One list controls current and historical reads | Narrowing hides both history and remembered IDs | Separate operation scopes |
| Helpdesk files remain but 30 keys are absent from discovery | Removed does not mean deleted on disk | Exact migration reconciliation, no knowledge reset |
| State-first leaves 33 pending; config-first leaves 30 removed | Write order alone is insufficient | Recover connected update before gate/completion |

## Iteration Status
- **Iteration:** 1 of 2 (min) / 5 (max)
- **Hypotheses tested:** H1 supported; H2 source-supported; H3 conditional
- **Hypotheses deferred:** None omitted; H3's recovery proof continues.
- **Gaps discovered:** interrupted-state handling, authority conflicts, history-only init and explicit resume behavior
- **Superseded decisions:** None

### Open Threads (for next iteration)
| # | Thread | Why it matters | Suggested focus |
|---|---|---|---|
| 1 | Recovery at every cut and with later project edits | Avoid both false success and destructive rollback | Observe/complete/refuse table and disposable assertions |
| 2 | Preservation without repeated questions | A mixed list is not proof of history | Exact adoption cases and persisted owner decisions |
| 3 | Scope boundaries | A historical task must stay readable without becoming resumable work | Init/resume/docs/tooling/parallel-test review |

### Recommendation
- [x] **MORE NEEDED** — complete the already owner-authorized second iteration on these bounded gaps.
- [ ] **SUFFICIENT**
- [ ] **BLOCKED**

Coordinator review remains required before planning or implementation. The owner's current instruction authorizes continuing research to completion, so no additional stage approval is requested.

## Conclusion
The task does not need mass reference rewrites or a generalized archive subsystem. A single optional historical list appears sufficient, but the main migration risk is config/digest coherence, as independently reproduced from helpdesk's commit. This iteration provides a defensible preferred design and rejects a false atomicity claim; it does not establish a future updater's native behavior. Iteration 2 will test the remaining recovery and integration conditions before returning a final research recommendation.
