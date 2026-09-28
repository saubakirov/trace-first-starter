# Extract — What do we NOT see?

> **Mindset:** Analyst. Make compatible combinations visible; do not choose an architecture yet.
> **Parent:** [HL-TFW_20260928-015408_ATC.md](../../HL-TFW_20260928-015408_ATC.md)
> **Goal:** Advance authorized task roles and phases without routine owner command transfer while preserving strategic control.
> **Producer unit:** `codex:thread:local:01a0e687-ddc2-7081-b9a0-f9b5afd1d82e`
> **Parent Coordinator:** `codex:thread:local:01a0e442-ef8f-7e83-99fd-5efb81c52927`
> **Activation / dispatch:** `journal/20260928-104423__dispatch__c3d2.md @ 114732c45b079a1422cff7cd264fe5bad6f8d7ba`
> **Authority:** `HL-TFW_20260928-015408_ATC.md @ 0ba239b2f98ae66765f43a07e8122998c77f037d`; originating proposer `none`

## Configuration Space

The columns preserve Gather D1–D8. These are analytical arrangements, not role launches or owner selections. “Active wait,” “addressed follow-up” and “scheduled wake” are distinct proposed trigger mechanisms. A successor or Gateway would require its own lawful selection and dispatch before operation.

| Config | D1 Strategy carrier | D2 Next-action actor | D3 Context lifetime | D4 Intent input | D5 Return/delivery proof | D6 Owner interface | D7 Resumption trigger | D8 Identity/authority binding |
|---|---|---|---|---|---|---|---|---|
| C1 Direct continuing task | Persistent task Coordinator | Same Coordinator | Compact same chat | Approved HL + selected insight | Artifact ref + addressed receipt + checked return | Direct Coordinator | Active wait, then next step in same turn | Task route + immutable mandate |
| C2 Direct timed continuation | Persistent task Coordinator | Same Coordinator | Compact same chat | Approved HL + selected insight | Artifact ref + checked return | Direct Coordinator | Scheduled wake of same chat | Task route + immutable mandate |
| C3 Task strategy, phase worker | Task Coordinator above phase-local Coordinators | Phase Coordinator for own phase; task Coordinator for phase handoff | New phase chats from file handover | HL + selected insight + phase state | Phase artifact ref + vertical receipt + checked return | Direct task Coordinator | Addressed follow-up at each boundary | Task/phase routes + distinct dispatches |
| C4 Gateway and phase Coordinators | Owner-facing Gateway + task/phase Coordinators | Phase Coordinator for in-phase work; authorized parent for phase transition | New phase chats from file handover | HL + selected insight + phase state | Phase artifact ref + checked return | Separate Gateway | Addressed gate to active parent, with explicit next-role launch | Exact task/phase routes + mandate |
| C5 Replaceable strategy baton | Durable strategy contract plus successor Coordinator | Named current successor Coordinator | New chat from current file handover | HL + selected insight + current status/journal | Artifact ref + addressed receipt + checked return | Direct current Coordinator | Addressed follow-up to current unit or scheduled same-chat wake | New immutable mandate/selection for successor |
| C6 Fixed-seed planning fork | Task Coordinator whose new phase units fork one fixed planning seed | Current phase Coordinator | Fork from fixed seed, then file refresh | Frozen HL + inherited planning seed + current state | Artifact ref + checked return | Direct task Coordinator | Parent addressed follow-up | Fresh unit dispatch + current route, not inherited title |
| C7 File-only replacement with timed audit | Durable strategy contract plus replaceable current Coordinator | Current named Coordinator | New chat from file handover | HL + current task trace, no inherited chat | Artifact ref + checked return | Separate Gateway | Scheduled same-chat audit of blocked/ready status | New immutable mandate/selection + observed address |

An owner-carried command at every return is excluded because it contradicts the frozen target state and DoF 1. A provider SDK handoff inside one application run is excluded from current Codex-native configurations because it is not this task's active runtime. Every listed arrangement still pauses at owner-reserved architecture, amendment, TS and implementation gates.

## Findings

### E1 — Topology, lifetime and liveness vary independently

C1 versus C2 holds strategy and interface constant and changes only the resumption trigger. If C1 stalls after its Coordinator turn ends, adding another named layer alone does not explain how it wakes. C3 versus C4 changes the owner interface but retains the need for a phase-to-parent return and next phase launch. C5 and C7 expose a new combination from the morphology: the strategy can be durable and the working Coordinator replaceable while the owner interface remains either direct or separate. This combination did not appear as a whole in the Briefing. C6 tests inherited planning context without letting the fork's inherited title or stale messages become authority.

The current workflow puts the next-role decision in the responsible Coordinator after each worker return (`plan.md` Step 7/9; `conventions.md` → `Workflow activation and routing`). A new unit needs a distinct dispatch even if it shares a principal or a chat ancestor. Thus every configuration has two control edges: **return recognition** (artifact plus route) and **new activation** (authorized exact command). D7 asks how the actor runs between them. D4 asks whether that actor understands the intended result; neither edge answers the other.

### E2 — A state handoff can preserve current facts without preserving an omitted goal

If the HL is complete, current status, journal, selected knowledge and role artifact can let a fresh unit reconstruct the next action without another role's transcript, as this Researcher did after its dispatch was recorded. If the HL omits a consequential owner criterion, more exact routing merely carries an incomplete target. C6 may expose earlier owner discussion, but it can also import stale state or bias. A fixed seed plus current files is analytically different from a fork of the accumulated operating chat; neither is an authority source. C1/C2 may retain more informal context, with an unresolved context-lifetime cost. The owner report and `TKL-20260923-PCUX-INTENT` are grounds for testing both cases, not measured comparative performance.

### E3 — External runtime comparison identifies a design distinction, not a desktop feature grant

[OpenAI's Agents SDK orchestration guide](https://developers.openai.com/api/docs/guides/agents/orchestration) distinguishes a handoff that transfers the next reply to a specialist from a manager calling a specialist as a tool; it advises adding specialists when instructions, tools or policy materially differ. [The SDK running-agents guide](https://developers.openai.com/api/docs/guides/agents/running-agents) separates one run's loop from the next turn's state strategy and warns that mixing replay with server-managed state can duplicate context. [Results and state](https://developers.openai.com/api/docs/guides/agents/results) identifies final output, last agent, history and interrupted state as different return surfaces. These are primary technical examples of distinct ownership, state and continuation responsibilities. They run in an application-managed SDK; they do not establish that Codex desktop chat dispatches or wakes another TFW unit automatically. [Codex scheduled-task documentation](https://learn.chatgpt.com/docs/automations) separately offers same-chat timed continuation with host availability conditions; a cadence is not a proof of event delivery or exact next-step execution.

### E4 — Conditional validity differs from current authorization

Under current `status.md` and frozen HL §4.1, only the recorded Coordinator may provision Researcher units and answer ordinary research gates. C1/C2 describe that current direct route at the research slice if the required trigger works. C3–C7 are research candidates only: any added Gateway, successor or phase Coordinator must be owner-selected or otherwise fall inside a valid immutable mandate and task/phase state. No configuration here changes the frozen owner reservations. A topology can be logically coherent and still be unavailable on the present surface or unauthorized for this task.

## Checkpoint

| Found | Remaining |
|---|---|
| C1–C7 combine all eight Gather dimensions; C5/C7 reveal replaceable strategy and timed-audit combinations absent from the Briefing. | Challenge each against long, branching, replacement, ambiguous-delivery, reserved-decision and imperfect-HL scenarios. |
| Same strategy carrier can have active, addressed or scheduled resumption. | Verify actual reliability and cost of each trigger on a receiving project; current evidence is conceptual or scoped observation. |
| External SDK docs distinguish ownership, state and return surfaces in an application runtime. | No transfer of SDK capability to Codex desktop; seek provider-specific evidence for candidate mechanisms. |

**Sufficiency:**
- [x] External source used: official OpenAI Agents SDK and Codex scheduled-task documentation.
- [x] Briefing gap closed for Extract: combinations and conditional validity are explicit.
- [x] Configuration Space built from Gather D1–D8, including an unproposed combination.

**Decision D-E1:** Challenge must test *both* a strategy/intent failure and a continuation/liveness failure for each surviving family. If an actor or trigger is missing, the arrangement fails even when its artifact and hierarchy are complete.

## Material handover at this checkpoint

**Producer/source:** this Researcher, Gather `2_gather.md @ 810b9be4bef9add05d00b0fd982e087a7208e41b`, frozen HL/current routing, and the linked official pages fetched 2026-09-28. **Inspected scope:** combinations of the eight dimensions, conditional mandate validity and a separate SDK runtime analogy. **Material:** C1–C7 expose different next-action ownership and trigger choices; C5/C7 expose a replacement path absent from the initial Briefing. **Uncertainty:** trigger reliability, provider parity, context cost and comparative success remain unmeasured. **Continuation:** Coordinator rules the Extract checkpoint; this same Researcher then challenges the candidate families.

---
Stage complete: YES
→ User decision: Await Coordinator Extract checkpoint under `native-gates`.
