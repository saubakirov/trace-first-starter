# Six-Edge Semantic Replay — FRATS Phase B

> **Comparison**: Phase A Candidate `1a9209530d7a939db1270e2f91dcef40a9f449e6` → Phase B Candidate `fd0655ce17f2c650d238622c1d6a57ec5dd9a204`
> **Oracle**: activation, authority, evidence, recovery, continuation and exception must remain equivalent or become less ambiguous

## Consolidation map

The `F*` identifiers resolve to the disposition ledger. Each cell names source → destination,
authority, carrier/recovery and the consequence of loss. `N/A` means the family neither carried nor
removed that edge; it is not used to hide a changed outcome.

| Family | Activation | Authority | Evidence | Recovery | Continuation | Exception |
|---|---|---|---|---|---|---|
| C1 — F4 activation/routing consolidation | Repeated workflow prose → `conventions.md` `Workflow activation and routing`; root request + exact spine remain carrier; root/owner authority; loss would allow provision/navigation to activate work. | Canonical spine + status route remain authoritative; local workflow checks task/phase/owner/dispatch; loss would permit wrong unit/scope. | Activation provenance remains in ONB/RF/REVIEW headers and events; loss would make execution unattributed. | Missing/mismatched spine refuses; Update/Init load the section conditionally for adapter repair; loss would make fresh/repaired entries unsafe. | Already-active role workflow proceeds from validated status; exact `coordinator_route` carries durable return; loss would strand work or invite peer routing. | Owner-only/gateway constraints and `tfw-gates-only` remain canonical; loss would turn dialogue or provisioning into authority. |
| C2 — F5 knowledge-handover consolidation | N/A — no workflow activation text removed in this family. | Repeated blocks → `conventions.md` `Knowledge handover`; producer owns its artifact, Coordinator owns downstream route. | Role-local handover retains producer/unit, source/epoch, inspected scope, material/none, uncertainty, continuation and unresolved decision. | Shared heading is uniquely resolved; missing/duplicate heading refuses at read contract; local required fields preserve offline recovery. | Exact recipient and continuation stay in each workflow's return step; loss would force chat reconstruction. | Human-only facts and unresolved owner decisions remain explicit; no implementation fact is promoted to human knowledge. |
| C3 — F6 template handover compression | N/A — templates do not activate roles. | Form authority remains the artifact template; content authority remains the named shared handover rule. | Long prose → mandatory `Material handover at this return` heading plus exact compact field set. | Template remains usable with the shared range; if the range cannot resolve, workflow read-contract refusal applies. | The artifact carries continuation and unresolved decision; append behavior remains artifact-specific. | “Justified none” and uncertainty fields prevent a blank handover from masquerading as evidence. |
| C4 — F7–F9 filename/RES repair | Producer activation still selects exact task/phase status before deriving a path. | Naming canon owns grammar; Plan/Handoff/Review own production; template is form, not naming authority. | Exact emitted path makes the write and later citation inspectable; historical forms remain evidence inputs. | Deterministic slug and topology resolve one path; missing/duplicate lineage refuses; fixed research stage paths remain discoverable. | Unsuffixed ONB/RF/EV append; TS/REVIEW revisions use `__revN`; highest approved TS continues execution. | Historical variants are readable but cannot authorize new issuance; ambiguous or mismatched current path stops before write. |
| C5 — F1–F3 targeted corrections | Config now has an explicit activation checkpoint; other corrections are N/A to activation. | REVIEW is explicitly independent Reviewer output; config no longer claims engine authority. | Deferral now points to the actual Review Purpose Check; the record must cite its resolving evidence. | Correct cross-reference and role owner remove dead-end recovery; existing status/journal paths remain unchanged. | Review returns vertically to Coordinator; Config propagates registered values before return. | Reviewer proposal versus Coordinator/owner ruling remains distinct; missing decision is not converted into silent approval. |

Generated Claude/Antigravity copies are C1–C5 delivery projections, not additional semantic owners.
The eight persistent zero-diff paths retain local bootstrap/recovery behavior and therefore were not
subtracted.

## Source-derived positive and material-negative replays

The replay read exact source clauses from the Phase A and Phase B Git trees. Where a real validator
exists it was used (`tools/tfw_state.py`); otherwise the check resolved the canonical heading,
producer step and required fields, then applied a single output-changing omission/mismatch mutant.

| Edge | Positive replay | Material negative replay | Result |
|---|---|---|---|
| Activation | Exact owner request plus task/phase/role/owner/dispatch spine activates the named workflow. | Provision-only text, incomplete spine and mismatched task/phase each fail activation. | Equivalent and more explicit after C1. |
| Authority | Complete task-local `gate_answer` with answerer/source, epoch and governing HL/TS refs is accepted by `tfw_state.validate_new_event`. | Removing the role artifact or governing HL/TS reference is rejected. | Equivalent; no chat/title/principal shortcut. |
| Evidence | `VERIFIED` resolves to a concrete artifact containing the observed input/output and oracle. | An unsupported `VERIFIED` source mutant is rejected rather than inherited from an enclosing commit. | Equivalent and less ambiguous after C2/C3. |
| Recovery | Legal `ONB → RF` transition with required refs is accepted by the real state validator. | Same-state `ONB → ONB` event is rejected. | Equivalent; consolidation did not loosen lifecycle recovery. |
| Continuation | Same Researcher/Reviewer unit lineage and highest approved TS continue the next stage/return. | Implicit unit substitution, foreign lineage or a lower/superseded TS is refused. | Equivalent; exact recipient survives C1/C2/C4. |
| Exception | Cited REVISE condition routes through the rung-specific Coordinator/owner rule and back to the same Executor/Reviewer where permitted. | An unruled rung-3 change hard-stops before execution. | Equivalent; C5 preserves independent proposal and reserved ruling. |

All six positive cases passed on both trees. All six negative cases changed the outcome in the
required direction and were refused on the Candidate. No subtraction was retained after a
non-equivalent result.

## Filename behavior fixtures

Positive current fixtures produced the master HL, single TS, current phase TS/EV, phase TS rev2 and
same-file RF append names listed in the disposition ledger. Negative fixtures supplied historical
`TS-*`, root `RES__*`, generic `TYPE__*.md`, malformed slug and duplicate-current-lineage forms.
History remained readable only when explicitly referenced; none could become the new output path.

## Historical oracle compatibility and limit

The retired RCFR source-derived harness was loaded from immutable Git history and applied only where
its source anchors still resolved. Exact semantic projections were unchanged for:

```text
P1 P3 R1 R2 R3 E2 E3 V1 V3 V4 A1
```

No resolved projection changed. The old negative mutants for R2, E3, V3 and V4 were still rejected;
the Executor evidence contract passed and the resolved REVISE routes remained equal. Other retired
cases were skipped because their Phase-A-era anchor strings no longer resolve after the accepted
Phase A refactor. They are not claimed as coverage. The six explicit current edge replays above are
the controlling Phase B evidence; the historical harness is corroboration only.

Verdict: every removal/consolidation family has a closed six-edge map, and every applicable edge has
one positive and one material-negative outcome. PASS.

## Return Round 1 — R1/R2 replay

Replacement Candidate `50ed7fb8c09cfc32e67623848b0551f9ada881da` reduces the four returned
canonical workflows while retaining the mapped carriers. The exact source-derived command and output
are in [`rung1-semantic-replay.txt`](rung1-semantic-replay.txt). It reads Plan, Handoff, Review,
Update and `tools/tfw_state.py` directly from the Candidate Git tree; no working-tree fallback exists.

All six positive cases pass. One in-memory removal per structural edge is rejected. The real
validator accepts the complete gate-answer and legal `ONB → RF` cases, rejects the missing governing
HL/TS reference and rejects `ONB → ONB`. This section supersedes the original validator-path sentence;
the actual path exists and resolves at the named Candidate.
