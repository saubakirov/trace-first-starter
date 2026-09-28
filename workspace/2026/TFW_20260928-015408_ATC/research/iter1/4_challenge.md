# Challenge — What do we NOT expect?

> **Mindset:** Critic. Attack every combination at its authority, intent and liveness edge.
> **Parent:** [HL-TFW_20260928-015408_ATC.md](../../HL-TFW_20260928-015408_ATC.md)
> **Goal:** Advance authorized task roles and phases without routine owner command transfer while preserving strategic control.
> **Producer unit:** `codex:thread:local:01a0e687-ddc2-7081-b9a0-f9b5afd1d82e`
> **Parent Coordinator:** `codex:thread:local:01a0e442-ef8f-7e83-99fd-5efb81c52927`
> **Activation / dispatch:** `journal/20260928-104423__dispatch__c3d2.md @ 114732c45b079a1422cff7cd264fe5bad6f8d7ba`
> **Authority:** `HL-TFW_20260928-015408_ATC.md @ 0ba239b2f98ae66765f43a07e8122998c77f037d`; originating proposer `none`

## Consistency Check

The eight Gather dimensions yield 28 unordered pairs. Each pair was checked for a simultaneous value in one current task epoch. D1/D2, D1/D6, D1/D8, D2/D7, D3/D4, D3/D7, D4/D8, D5/D7, D5/D8 and D6/D8 contain hard incompatibilities or a mandatory condition shown below. The remaining pairs can coexist but require the ordinary authority and evidence gates; coexistence is not evidence of benefit.

**Incompatible pairs or missing mandatory conditions:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible or conditional |
|---|---|---|---|---|
| D1 Strategy carrier | Sole persistent task Coordinator | D2 Next-action actor: independent phase Coordinator | A phase Coordinator cannot be the next actor if no such unit and mandate exist; adding one changes D1. |
| D1 Strategy carrier | Owner-facing Gateway | D6 Owner interface: direct task Coordinator | The owner interface cannot simultaneously be a separate Gateway and direct task Coordinator for the same selection. |
| D1 Strategy carrier | Replaceable successor | D8 Identity/authority binding: old unit's title or principal | Replacement requires a new actual address and valid mandate/selection; inherited navigation or attribution cannot bind it. |
| D2 Next-action actor | Owner performs each routine transfer | D7 Resumption trigger: owner starts named continuation | This pair is internally coherent but violates frozen HL §3.1/DoF 1, so it is excluded from viable autonomous configurations. |
| D3 Context lifetime | New file-only chat | D4 Intent input: inherited planning conversation | Mutually exclusive as an input description; a fork changes D3, and current files remain necessary. |
| D3 Context lifetime | Ended prior chat, new unit | D7 Resumption trigger: active wait in prior chat | An ended unit cannot still own a live wait; the new unit needs an actual trigger and activation. |
| D4 Intent input | Inherited planning conversation alone | D8 Identity/authority binding: current route + immutable selection | History alone cannot validate current route/selection; current status and journal must be read. |
| D5 Return/delivery proof | Send receipt only | D7 Resumption trigger: event-driven next step | Receipt says a send was accepted, not that an idle recipient ran and launched the next role. |
| D5 Return/delivery proof | Artifact ref only | D8 Identity/authority binding: current route | An artifact without actual producer, status/dispatch and route cannot establish who may act next. |
| D6 Owner interface | Separate Gateway | D8 Identity/authority binding: title alone | Gateway title does not identify or authorize the distinct unit; frozen mandate and exact routing are still required. |

**Surviving configurations from Extract:**

| Config | D1 Strategy carrier | D2 Next-action actor after durable return | D3 Context lifetime | D7 Resumption trigger | Challenge status |
|---|---|---|---|---|---|
| C1 | Persistent direct task Coordinator | Same Coordinator | Compact same chat | Active wait/same active turn | Coherent for a bounded task; idle-turn liveness and long context unresolved. |
| C2 | Persistent direct task Coordinator | Same Coordinator | Compact same chat | Scheduled same-chat wake | Conditional on schedule availability, host/app uptime and a bounded recheck; not an event trigger. |
| C3 | Task strategy + phase workers | Phase Coordinator, then task Coordinator at phase boundary | Fresh phase chats from files | Addressed parent follow-up | Coherent if both exact units and their returns are active; extra boundary adds delivery/mandate cost. |
| C4 | Gateway + phase Coordinators | Phase Coordinator, then authorized parent | Fresh phase chats from files | Addressed parent follow-up | Conditional on a new owner-selected Gateway topology; Gateway cannot replace operational parent. |
| C5 | Durable strategy baton | Current named successor Coordinator | Fresh chat from files | Addressed current unit or scheduled wake | Conditional on new immutable selection/mandate and a trigger; old unit cannot self-appoint replacement. |
| C6 | Fixed-seed planning fork | Current phase Coordinator | Fork plus current-file refresh | Addressed parent follow-up | Conditional on current state refresh and proof that inherited owner context adds useful intent. |
| C7 | Durable strategy + Gateway | Current named successor Coordinator | Fresh chat from files | Scheduled audit | Conditional on both new selection and timer reliability; high number of boundaries to justify. |

**Unexpected survivors:** C2 shows a single direct Coordinator could address idle-turn risk through a same-chat timed recheck without adding a hierarchy, subject to real schedule limits. C5 shows replacement can preserve strategy in ordinary files without a mandatory Gateway, if a lawful successor and trigger exist. Neither observation selects those designs.

## Findings

### C1 — One-phase and long sequential cases distinguish proportion from context lifetime

In a one-phase task C1 has one next-action owner after Researcher, Executor and Reviewer returns; it does not require a distinct owner interface to preserve the current explicitly selected direct route. C3/C4/C7 add units or transfers whose benefit must be shown against their additional dispatch, gate and handover surfaces. For long sequential work, C1 may accumulate context even if it compacts; current evidence does not measure when this causes error. C3–C5 bound individual worker/phase contexts but add a task strategy or successor handover. Their durable input must include the frozen target, current status, exact phase authority and next action. A handover that merely says “continue” is insufficient.

### C2 — Branching and replacement reveal the actor after each return

For branches, a task-level actor must know dependencies and decide which ready authorized branch to advance. A phase Coordinator may complete its own phase but cannot silently launch a sibling from an unrecorded ancestor route. C1/C2 keep one actor; C3/C4/C6 must name the parent task Coordinator at cross-phase boundaries; C5/C7 must identify the currently selected successor. If the parent is idle when a phase return lands, all still need a wake mechanism. Replacement is strongest test of C5/C7: old task status or old title cannot transfer the frozen mandate to a new unit. The required selection and actual dispatch are an owner/authority action; absent either, replacement remains blocked. This Researcher's own missing-dispatch gate is a small observed example of that boundary.

### C3 — Ambiguous delivery and reserved amendment defeat optimistic progression

If a role's addressed send has ambiguous delivery, no configuration may count it as returned and start dependent work merely because the artifact exists. The current rule requires a durable artifact and provider status/readback; the Reviewer envelope has exact tuple semantics and permits an identical retry only after confirmed non-application. There is no universal exactly-once claim. A recipient's valid response can then advance one authorized step. If a finding changes the frozen HL or owner-reserved architecture, every configuration stops the affected path for the human owner; a Gateway, scheduler, fork, successor or delegated Coordinator cannot self-answer. Unrelated authorized work can continue only if dependencies permit it.

### C4 — A perfect HL and an imperfect HL produce different error modes

With a complete HL, file handover may preserve goal, authority and next action while limiting inherited chat; the active task demonstrates one bounded instance. With an imperfect HL, C1/C2 can repeat the omission from one chat, C3–C5/C7 can propagate it via files, and C6 can inherit an earlier owner statement yet also inherit obsolete preferences or unauthorized assumptions. The diagnostic is to compare a consequential owner criterion in the source planning discussion with the approved HL and returned output; if missing, the owner must resolve whether to amend/refine, rather than letting a fork become silent authority. The owner's report that authoring-chat behavior differs from receiving projects supports this test but does not prove fork superiority.

### C5 — Primary provider evidence limits the wake claim

[OpenAI's scheduled-task documentation](https://learn.chatgpt.com/docs/automations) says same-chat tasks can re-enter on minute-based or longer schedules, while event-triggered tasks on supported Gmail/Slack/GitHub events are unavailable in the desktop app and do not describe TFW role-artifact events. Local project runs require the computer and app to remain running. Thus C2/C7 can investigate a time-based audit, but cannot claim immediate or durable event wake. [Long-running-work documentation](https://learn.chatgpt.com/docs/long-running-work) says a goal uses the same permission boundary and pauses for decisions; it does not erase owner reservations. [OpenAI Agents API webhooks](https://developers.openai.com/api/docs/guides/agents-api/sessions/webhooks) show an application-managed event mechanism in another runtime, and explicitly distinguish `idle` from successful completion and note that its connection wait is not a durable input queue. This is counterevidence to treating an event/idle signal as a completed TFW step on the present desktop surface.

## Checkpoint

| Found | Remaining |
|---|---|
| All seven analytical rows survive only with named actor, current authority, checked return and a real trigger; invalid pairs and the owner-transfer variant are excluded. | Second iteration should independently stress the shortest coherent route against a long/replacement case, and test a receiving-project wake/return path if the owner wants a native claim. |
| Direct continuation, phase strategy and successor baton have distinct costs and failure modes. | Relative attention/context cost is unmeasured; no architecture choice is justified from this pass alone. |
| Scheduled same-chat wake is time-based with host/app conditions; desktop event-triggered tasks do not cover task-local TFW returns. | Exact addressed-send wake behavior for an idle Coordinator and delivery ambiguity remain unverified on a receiving project. |
| Imperfect HL is an intent-fidelity failure that none of the liveness mechanisms fixes automatically. | Identify a minimal owner-context capture/check that detects omitted consequential intent without requiring raw transcript inheritance. |

**Sufficiency:**
- [x] External source used: official OpenAI scheduled-task, goal and Agents API webhook documentation.
- [x] Briefing gap closed for Challenge: one-phase, long sequential, branch, replacement, ambiguous delivery, amendment and imperfect-HL cases tested.
- [x] Pairwise incompatibility checked across 28 pairs; survivors listed with conditions.

**Decision D-C1:** Iteration 1 can synthesize a bounded architecture comparison and material uncertainty. It cannot certify autonomous cross-turn/cross-phase continuation, a replacement protocol or a selected topology; iteration 2 should test those decision-changing gaps before the Coordinator presents an owner architecture choice.

## Material handover at this checkpoint

**Producer/source:** this Researcher, Gather `810b9be4bef9add05d00b0fd982e087a7208e41b`, Extract `849b30ca7b9319bea96d68194381ea02ed156756`, frozen task authority, and the linked official pages fetched 2026-09-28. **Inspected scope:** 28 dimension pairs and seven configurations under seven stress scenarios. **Material:** actor and trigger remain independent; no topology alone solves an idle parent or an omitted owner criterion. **Uncertainty:** native idle-unit wake reliability, delivery semantics, cost and receiving-project behavior are unmeasured. **Continuation:** Coordinator rules the Challenge checkpoint; this same Researcher may then synthesize RES for iteration 1.

---
Stage complete: YES
→ User decision: Await Coordinator Challenge checkpoint under `native-gates`.
