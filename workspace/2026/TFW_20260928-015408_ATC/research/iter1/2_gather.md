# Gather — What do we NOT know?

> **Mindset:** Explorer. Map independent choices and evidence boundaries before comparing configurations.
> **Parent:** [HL-TFW_20260928-015408_ATC.md](../../HL-TFW_20260928-015408_ATC.md)
> **Goal:** Advance authorized task roles and phases without routine owner command transfer while preserving strategic control.
> **Producer unit:** `codex:thread:local:01a0e687-ddc2-7081-b9a0-f9b5afd1d82e`
> **Parent Coordinator:** `codex:thread:local:01a0e442-ef8f-7e83-99fd-5efb81c52927`
> **Activation / dispatch:** `journal/20260928-104423__dispatch__c3d2.md @ 114732c45b079a1422cff7cd264fe5bad6f8d7ba`
> **Authority:** `HL-TFW_20260928-015408_ATC.md @ 0ba239b2f98ae66765f43a07e8122998c77f037d`; `status.md` reporting `native-gates`, selection `baseline`
> **Originating proposer:** `none`

## Dimensions

Each row is a decision factor. Alternatives are possible values, not recommendations; compatibility and adequacy remain for Extract and Challenge.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| D1 Strategy carrier | One persistent task Coordinator | Task Coordinator with phase-local Coordinators | Durable strategy contract plus replaceable successor Coordinator | Distinct owner-facing Gateway plus task/phase Coordinators |
| D2 Next-action actor | Current Coordinator after each return | Phase-local Coordinator after its workers return | Explicit event-triggered scheduler resumes named unit | Owner performs each transfer |
| D3 Context lifetime | One continuing chat | Compact same chat at checkpoints | New task from file handover | Fork from fixed planning seed or accumulated chat |
| D4 Intent input | Approved HL and current trace | Approved HL plus selected owner insight record | Inherited planning conversation | Fresh owner clarification at a named gap |
| D5 Return/delivery proof | Task artifact and immutable Git ref | Addressed send receipt plus artifact | Event wait/status plus artifact | Manual owner-carried artifact ref |
| D6 Owner interface | Direct task Coordinator | Separate Gateway | Owner views selected task status only | Owner receives scheduled summary from current unit |
| D7 Resumption trigger | Coordinator turn still active and awaiting event | Addressed follow-up to same unit | Scheduled chat wake | Owner starts named continuation |
| D8 Identity/authority binding | Task-local unit address and mandate | Stable principal plus task-local unit address | Provider chat title | Durable task/phase route plus immutable selection event |

## Findings

### G1 — Current TFW control chain names roles and recipients, but its execution has distinct boundaries

Selected repository sources at `d1296bdc198344bcdc664e48e19eab10fb862cc5`: `.tfw/conventions.md` → `Workflow activation and routing`, `status.md` fields, `.tfw/workflows/plan.md` → Steps 1, 5, 7, 9, `.tfw/workflows/research/base.md`, `.tfw/workflows/handoff.md` → ONB/RF, and `.tfw/workflows/review.md` → Step 6. The path currently reads:

| Boundary | Current rule | Evidence that the boundary completed |
|---|---|---|
| Authority | Owner-approved frozen HL, exact status spine and immutable dispatch precede delegated role work. | Frozen commit, matching current status and task-local dispatch; a title or tool alone does not grant scope. |
| Activation | Coordinator sends only `/tfw-* <task[/phase]>` to a distinct role unit. | Native create receipt and the new unit's validated task/dispatch; provisioning alone does not prove activation. |
| Working gate | Worker sends named status/question to its own `coordinator_route`; Coordinator may answer only inside mandate. | Exact addressed send and lawful task-local `gate_answer` when authority is needed. |
| Durable result | Researcher writes stage/RES; Executor writes ONB/RF/EV; Reviewer writes REVIEW and its status/journal effect. | Immutable artifact ref, actual producer and route; prose or a send receipt alone is insufficient. |
| Next role/phase | Coordinator verifies returned artifact, updates its owned controls and launches the ready authorized next role/phase. | A subsequent valid dispatch/transition, not merely a completed worker turn. |

This is a contract map, not measured runtime success. Our own activation supplies one bounded observation: the exact role command arrived, but this Researcher stopped until the Coordinator committed its dispatch; the addressed return and readback then allowed the same unit to continue. That demonstrates a recoverable gate on this surface, not unattended advancement or delivery reliability across sessions/providers. The Coordinator's later free-section citation correction at `93726473db4b1074793e4a1cc8955c7342aef3cc` is a separate verified repository event, not a Researcher edit.

### G2 — Intent fidelity, context lifetime and wakeup are independent failure candidates

The owner reports small one-phase work can succeed and long work often needs intervention; prior planning chats may hold omitted intent (HL §2, §10–§11, owner testimony). The selected `TKL-20260923-PCUX-INTENT` record says automation should remove manual mechanics while preserving judgment and attention, but its one human origin and later confirmation do not measure a cause or provider behavior. The selected PCUX technical record establishes current core/profile/status scope and explicitly leaves cross-platform cycles and native reliability unproved. Philosophy F34/F35/F38 and process F6/F7/F30/F31/F33/F35 explain why follow-through, frozen purpose, finite attention, enforcement sites, correct review reference and receiving-project exposure matter; historical examples remain scoped evidence.

Three separable diagnostic paths follow: (a) a complete HL reaches a worker but no actor resumes after its return; (b) work resumes but an omitted owner criterion distorts the target; (c) current intent and dispatch are sound, but a long-lived Coordinator accumulates enough irrelevant context to weaken choices. Any one can occur without the others. No path has a measured frequency in this task.

### G3 — Official OpenAI documentation describes several continuation mechanisms, with distinct limits

At this 2026-09-28 Gather checkpoint, [OpenAI's long-running-work documentation](https://learn.chatgpt.com/docs/long-running-work) says a desktop `/goal` can pursue a multi-step outcome in the same chat and pauses for decisions; it does not enlarge access. It recommends separate chats/worktrees for independent parallel work. [Scheduled-task documentation](https://learn.chatgpt.com/docs/automations) says a scheduled task inside an existing chat can return to that chat's context on a cadence, including ongoing research; project-scoped local runs need the machine on and desktop app running. The docs distinguish standalone scheduled runs, which start a new chat, from same-chat follow-ups. [OpenAI's Codex Remote guide](https://developers.openai.com/blog/mastering-codex-remote-for-engineering) says a fork inherits history and a side chat is a separate branch of thought; it also describes compaction, queue and steer. [OpenAI's long-horizon experiment](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex) attributes one long run's coherence partly to externalized spec, plan and status, but explicitly calls it an experiment.

These official sources establish available product concepts, not an automatic event-triggered transition from a Researcher artifact to an idle Coordinator. In this exact task, native `create_thread`, `send_message_to_thread`, `wait_threads`, title write/readback and isolated worktree were exposed and used; a receipt/readback establishes only its own observed action. Whether a same-chat scheduler, goal or future provider can reliably wake a specific idle Coordinator from a durable TFW event is still unverified. The Responses/Agents API background and sessions are different runtimes; their existence cannot be silently substituted for the desktop task mechanism.

### G4 — The receiving unit needs a compact lawful reconstruction path

`status.md` carries current state and route, the frozen HL carries goal/authority, `research/iterations.yaml` carries the pending research slice, and the dispatch identifies the actual Researcher parent and scope. This unit could reconstruct enough to write a Briefing without reading the Coordinator's transcript. The initial missing dispatch forced a stop and a vertical gate; it was repaired by an immutable event and read from the role checkout. The role's exact title was readable, yet the title itself supplied no authority. This observed case supports file handover as a viable input channel for a bounded research slice. It does not prove that every future replacement gets all strategic intent or that a long task restarts without an external wake.

## Checkpoint

| Found | Remaining |
|---|---|
| D1–D8 expose distinct strategy, actor, context, intent, proof, interface, trigger and authority choices. | Test compatible combinations; some alternatives may violate the frozen HL or current authority unless redesigned and owner-selected. |
| Current workflow assigns next-action responsibility to the Coordinator after durable worker return. | Establish whether an idle Coordinator is actually awakened by an addressed gate or only while an active wait/turn exists. |
| Official OpenAI docs distinguish goal continuation, scheduled same-chat runs, forks and externalized project memory. | No source yet proves an exact desktop TFW event-to-phase handoff, exactly-once send, or performance gain. |
| This role's missing-dispatch gate was resolved via immutable task trace and addressed message. | Test replacement, ambiguous delivery, complete versus imperfect HL and receiving-project entry. |

**Sufficiency:**
- [x] External source used: official OpenAI documentation and published experiment, with limits noted.
- [x] Briefing gap closed for Gather: mapped current boundaries, provider concepts and candidate dimensions.
- [x] Dimensions identified: eight independent factors with at least three alternatives each.

**Decision D-G1:** Extract should compare compatible combinations around an explicit next-action actor and trigger. It must not treat a durable artifact, a title, an addressed send or a scheduled cadence alone as proof that the next authorized phase starts.

## Material handover at this checkpoint

**Producer/source:** this Researcher; repository texts at `d1296bdc198344bcdc664e48e19eab10fb862cc5`, task dispatch `114732c45b079a1422cff7cd264fe5bad6f8d7ba`, selected knowledge records at current checkout, and the linked official OpenAI pages fetched 2026-09-28. **Inspected scope:** H1–H5 stop/start/return sites, owner intent versus technical reliability, eight design dimensions and this one observed role activation. **Material:** the chain has separate authorization, activation, return, advancement and wake boundaries; the latter two are the unresolved liveness edge. **Uncertainty:** no measured failure rate, cost or scheduler reliability; no cross-provider inference. **Continuation:** Coordinator decides whether to close Gather or deepen the specific evidence gap; the same Researcher then proceeds to Extract.

---
Stage complete: YES
→ User decision: Await Coordinator Gather checkpoint under `native-gates`.
