# Gather — What do we not know?

> **Mindset:** Explorer. Separate authority, identity, timing, scope and compatibility before selecting a carrier.
> **Parent:** [HL-TFW_20260922-192606_PCUX](../../HL-TFW_20260922-192606_PCUX.md)
> **Goal:** Preserve strategic Coordinator planning while enabling command-only launches, live mandates, provider routes and complete documented closure.
> **Producer / route:** `codex:thread:local:01a0cb19-cbf2-7603-8775-c776f52660d4` → `codex:thread:local:01a0c980-4552-7ed3-b2aa-3c5cc46bc7bc`.
> **Source epoch:** governing status, HL and iteration control at `ff66d7ed5df678061d5689713fcf64c0e84ac744`; iteration-2 Briefing `73ca536b536d09f2f8e0454e76c42aee5168ea21`; current repository readers inspected 2026-09-23. External documentation is a mechanism comparison, not PCUX runtime evidence.

## Dimensions

Each row is a choice to test, not a recommendation. Approved HL constraints will exclude some combinations in Extract/Challenge.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| D1 — source of an effective launch grant | Frozen HL mandate only | Later immutable direct-owner decision only | Current status selection referencing the applicable immutable mandate/decision | Mutable status or provider setting alone |
| D2 — first trustworthy child identity | Native creation receipt | First ordinary addressed gate/status from the actual child | One transport-only readiness exchange if an ordinary gate lacks address data | Address preallocation or dormant role task before its gate |
| D3 — future or revoked operating selection | Change current status as soon as a conditional instruction is given | Record pending owner decision, change status only at its named checkpoint | Make every reader compute current mode by replaying journal decisions | Keep selection only in chat or provider session state |
| D4 — root-to-phase scope | Phase reads root status live for operating choice | Phase-local current status cites the applicable root decision and exact phase authority | Separate owner decision created for each phase | Root status mirrors every phase state and route |
| D5 — same-unit continuation | Reuse initial activation/dispatch and ignore later current selection | Keep unit/round identity, revalidate current local spine and effective decision at the next gate | Provision a new unit for each operating switch | Treat revoked delegation as retroactive deletion of already produced work |
| D6 — legacy/default interpretation | Missing complete spine remains read-only, with owner-only/gates-only defaults only for new choices | Synthesize delegation/reporting from missing fields | Require a truthful one-time complete migration before current activation | Treat any unknown or partial state as permissive manual mode |

## Findings

### G1 — State and immutable decision are different authorities

The current [status template](../../../../../.tfw/templates/status.md) and `.tfw/conventions.md` → `Task control files`, `Task Statuses` make task/phase `status.md` the sole current state and routing authority. The key set is closed. Its five coordination fields are all-or-none: `coordinator_route`, `owner_gateway`, `dialogue`, `activation`, `coordination_authority`. Total absence is legacy-readable but cannot activate current work. `tools/tfw_state.py` enforces those structural facts, admits `owner_gateway: gateway:{address}` with `tfw-gates-only`, and rejects `dialogue: iterative` when the gateway is `owner:{human}`. It has no current `reporting` or owner-selection reference, and its closed event vocabulary has no ordinary owner-mode-decision kind. The [event template](../../../../../.tfw/templates/journal/event.md) gives `gate_answer` a blocked-artifact purpose, while `transition` changes lifecycle and `ownership_changed` changes ownership; none presently names an ordinary future operating selection. Sources: `tools/tfw_state.py` `COORDINATION_KEYS`, `STATUS_KEYS`, `validate_status`, `EVENT_KINDS`; `.tfw/templates/status.md`; `.tfw/templates/journal/event.md`; `.tfw/conventions.md` → `Workflow activation and routing`.

The owner-approved HL §3.6 instead requires status to hold the **current** launch/reporting/dialogue choice and reference its immutable direct-owner decision; a future conditional instruction becomes active only at the named checkpoint. This is an authority relation, not a request to replay journal history for every read. Microsoft's [Event Sourcing pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing) describes a different architecture in which the append-only event stream is the system of record and projections derive current state. That external contrast supports keeping TFW's stated status authority explicit; it does not prove which new field grammar to choose. Git's [revision verification](https://git-scm.com/docs/git-rev-parse) can check that an immutable object exists, but an existing SHA or event path does not by itself establish human origin, scope or current effect. The TFW event template separately requires actual authority and contained, opened references before a write.

### G2 — Address discovery and dispatch provenance have distinct times

The frozen HL §§3.4 and 4.1 and A4 authorize a role to begin from an exact command plus task files even if the parent only later learns its address. Current `.tfw/conventions.md` → `Workflow activation and routing` says pre-work validation includes actual unit/address/parent and delegated dispatch, while its dispatch paragraph preserves actual destination and native address. `plan.md`'s post-approval dispatch also lists the address as a recorded fact. Neither status nor the event frontmatter has a child-address slot; the `dispatch` body/refs carry the actual source, destination, parent, channel and role/scope. Thus a receipt, first normal gate and contingent transport-only readiness are different evidence points; the earlier command cannot justify a fabricated prior addressed event. Once observed, later exact addressed sends and same-unit returns still require a real native identity. Sources: `.tfw/conventions.md` → `HL Contract` rule 8 and `Workflow activation and routing`; `.tfw/templates/journal/event.md` dispatch paragraph; `.tfw/workflows/plan.md` Step 7/dispatch paragraph; iteration-1 RES D2.

### G3 — Local phase state and continuation expose the scope question

The current task-level `PHASES` status never summarizes phase state; each phase has its own `status.md` and `journal/` and its consumers read those local files. `tools/tfw_state.py` uses the same phase status schema (aside from the directory-ID check). A journal event's `refs` must remain within the owning task/phase directory, while an actual local authority artifact can establish ancestor lineage. Consequently a root owner choice does not automatically become the phase's current selection merely because a reader can see the root file; Extract must test an explicit, scope-bounded local reference and the point it becomes effective. Sources: `.tfw/conventions.md` → `Task control files`, `A phase carries its own state`; `.tfw/templates/journal/event.md` reference rule; `tools/tfw_state.py` `read_phase_status`; HL §§3.4, 3.6.

For continuation, current rules require the **same** unit to cite prior activation and the still-current routing spine and to recheck all fields. They do not yet explain whether a pending future selection, a newly effective selection or immediate revocation changes the active unit's next safe action without changing its identity. `plan.md` Step 1 already says existing work resumes its state-owned route rather than repeating inception. Its Step 5 defaults to owner-only, gates-only, owner gateway and no principal absent a positive owner choice; current `activation` validates only `owner-only` or `delegated:{ref}` and has no reporting mode. Those defaults do not themselves confer delegation or fully manual transfer. `Session identity` currently ties the GATEWAY title to iterative dialogue, even though the validator accepts a gates-only gateway. `Launch selection` independently preserves per-launch model and reasoning-effort choice, quality floor and effective-setting evidence. Sources: `.tfw/conventions.md` → `Workflow activation and routing`, `Session identity`, `Launch selection`; `.tfw/workflows/plan.md` Identity and Steps 1/5; `tools/tfw_state.py` `validate_status`; HL A12.

### G4 — A rule change would have multiple readers and copied entry points

Plan, Research, Handoff and Review each resolve activation/routing before material work; Handoff and Review require the complete spine and cited mandate/dispatch, and Reviewer continuation preserves the same Reviewer unit. The installed root and `.tfw/adapters/` Codex, Claude, Antigravity and Cursor entry text repeats the spine/vertical-return instruction in varying detail. A contract change written only into `plan.md` or `tools/tfw_state.py` could therefore validate one path while a role reader still refuses it. This is a reader/copy inventory for Extract, not permission to edit any of those files in Research. Sources: `.tfw/workflows/plan.md`, `research/base.md`, `handoff.md`, `review.md`; `.tfw/adapters/` and installed root entry text found by exact `rg` patterns on 2026-09-23.

## Checkpoint

| Found | Remaining for Extract/Challenge |
|---|---|
| Six independent dimensions distinguish grant origin, child identity, future decision timing, phase scope, same-unit continuation and legacy/default behavior. | Compare connected configurations against the frozen HL and identify the minimum coherent status/event/reference form. |
| Current status authority, closed schema/event kinds and reader/copy seams are concrete; an event-history-as-live-state approach would be a different architecture. | Map each affected reader precisely and test false-authority, stale-scope and address-race cases. |
| The existing phase-local state and exact-ref rules constrain how root decisions reach workers. | Test pending switch/revocation with an active unit and a phase that has its own current route. |

**Sufficiency:**

- [x] External source used: official Microsoft event-sourcing and Git revision documentation opened 2026-09-23 for bounded comparison; neither is treated as a PCUX field trial.
- [x] Briefing gap closed for Gather: current authority/reference readers and the six choice axes are identified for H5/H6/H7.
- [x] Dimensions identified: six independent factors with at least three alternatives each; no survivor is selected in this stage.

**Stage decision:** pass D1–D6 to Extract for connected configuration and minimum-reader analysis, without changing the approved mandate or treating an unselected provider addendum as evidence.

## Material handover at this checkpoint

Producer is the Researcher unit above. Inspected source/epoch: task control and HL at `ff66d7ed5df678061d5689713fcf64c0e84ac744`, iteration-1 RES and iteration-2 Briefing, current status/event/validator/Plan/role/adapter-reader files, and the opened official Microsoft/Git pages on 2026-09-23. Material: D1–D6 and G1–G4 separate state authority from immutable grant provenance, late child identity from dispatch timing, and phase-local state from ancestor scope. Uncertainty: exact effective-decision reference, phase projection, revocation timing, legacy behavior and reader set need connected testing. Continuation: return this Gather to the recorded Coordinator; proceed to Extract only after its stage gate. No HL, TS, control or code file was edited.

---
Stage complete: YES
→ User decision: no new owner decision requested; frozen choices stand and configuration comparison moves to Extract after the Coordinator gate.
