# Gather — What do we NOT know after iteration 1?

> **Mindset:** Explorer. Seek evidence that makes an attractive first-pass explanation fail.
> **Parent:** [HL-TFW_20260928-015408_ATC.md](../../HL-TFW_20260928-015408_ATC.md)
> **Goal:** Advance authorized task roles and phases without routine owner command transfer while preserving strategic control.
> **Producer unit:** `codex:thread:local:01a0e687-ddc2-7081-b9a0-f9b5afd1d82e`
> **Parent Coordinator:** `codex:thread:local:01a0e442-ef8f-7e83-99fd-5efb81c52927`
> **Activation / dispatch:** same-unit iteration 2 continuation, `journal/20260928-112223__dispatch__d4e3.md @ 5a994448b8987f0b12afad438e714eb812103aa4`
> **Authority / selection:** frozen HL `0ba239b2f98ae66765f43a07e8122998c77f037d`; `status.md` `native-gates`, `baseline`; originating proposer `none`
> **Source window:** repository at `c7b773da0ccf380d48063104eab0679b385c3f25`; official OpenAI documentation fetched 2026-09-28

## Dimensions

These refine iteration 1 D1–D8 around the four open threads. Alternatives are states to compare, not preferences.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| D1 Parent execution state at return | Active turn waiting for a named role | Loaded chat with no active turn | Unloaded/closed chat | Replacement unit selected, old unit stopped |
| D2 Receiving context availability | Current task files in primary project checkout | Task files present but in secondary folder | Isolated checkout behind the needed commit | Fork carries older chat history plus current files |
| D3 Intent fidelity | Consequential criterion in frozen HL | Criterion in selected owner record but omitted from HL | Criterion only in owner conversation | Criterion absent or disputed even with owner source |
| D4 Return evidence | Artifact and task-local lineage verified | Addressed-send receipt only | Provider status signal only | Ambiguous send with durable artifact but no confirmed receipt |
| D5 Continuation trigger | Active event wait | Addressed follow-up that starts a turn | Scheduled same-chat recheck | Owner starts named continuation |
| D6 Strategy boundary | One continuing direct Coordinator | Task strategy Coordinator plus phase Coordinator | Current successor Coordinator from files | Owner-facing Gateway plus phase Coordinator |
| D7 Branch/replacement complexity | One bounded phase | Long sequential phases | Concurrent branches with dependencies | Coordinator replacement mid-task |

## Findings

### G1 — Native continuation scope was a separate authority edge, and the parent was not idle at observation

This Researcher's iteration 1 dispatch explicitly covered only iteration 1. The Coordinator's prepared iteration 2 control and exact continuation message did not by themselves widen that task-local role scope; this unit stopped and sent a vertical gate. The Coordinator then committed a second dispatch to this same address at `5a994448b8987f0b12afad438e714eb812103aa4`, after which the Briefing was written and its gate answered. This is a second bounded, observable stop/recovery at a mandate boundary. It supports the need for explicit scope per new slice; it does not show that an idle parent wakes or that a role starts the next phase unattended.

One `wait_threads` snapshot after the Briefing gate reported the parent task `active` with latest turn `inProgress`. That signal is sufficient to classify the parent as *not observed idle* at that point. No parent transcript, reasoning, unfinished tree or unreturned work was inspected. An addressed gate during an active parent turn tests a different D1 value from the idle-parent case in predecessor T1.

### G2 — File existence and instruction discovery can diverge at a receiving project

[Official Projects and chats documentation](https://learn.chatgpt.com/docs/projects) says local projects use a primary folder for default Git operations and automatic discovery of `AGENTS.md`, skills and `config.toml`; secondary folders remain available for reading/editing but do not get the same automatic discovery. It also says related chats can share project files while keeping separate transcripts. This is a concrete counterexample to the broad claim “ordinary files automatically transfer all governing instructions”: the same files can be available in a secondary folder yet not automatically loaded as instructions. An isolated checkout behind the frozen task commit is another local case: the role cannot use a dispatch absent from its checkout, as iteration 1 showed. The minimal receiving entry therefore has two distinct checks: the correct task files are reachable, and the governing entry instructions are actually selected on that surface. H3's file-handover sufficiency remains conditional on both.

### G3 — App-server exposes explicit turn control, but mapping from this task's addressed-send tool is unknown

[Official Codex App Server documentation](https://learn.chatgpt.com/docs/app-server) distinguishes `thread/start`/`thread/resume` from `turn/start`, which begins generation, and `turn/steer`, which modifies an active turn. It also distinguishes `thread/inject_items`, which appends model-visible items without starting a user turn, from a new turn. The documented event stream reports thread/turn status and completion. This is primary counterevidence to equating “message stored” or “chat exists” with “agent ran.” It describes an integration API, not the semantics of the desktop `send_message_to_thread` tool exposed here. That mapping, and whether an addressed message to an idle Coordinator starts one turn, remains unverified.

[Official prompting documentation](https://learn.chatgpt.com/docs/prompting) says a message sent while Codex is already working can steer the current run or queue for the next run. It does not say a stage artifact itself is a continuation trigger. [Official notifications documentation](https://learn.chatgpt.com/docs/notifications) describes status and alerts for people; these are an observation surface, not a documented task-to-task handoff protocol. These sources challenge H1/H5's possible inference that a routed artifact and visible notification suffice for autonomous advancement.

### G4 — Owner-reported intent loss cannot be manufactured as a test result

HL §11 S1–S7 and the selected `TKL-20260923-PCUX-INTENT` record preserve the owner's stated need for less manual command transfer and retained strategic judgment. This Researcher can test whether those *recorded* criteria appear in an architecture and receiving-unit input. It cannot prove an actual omitted owner criterion without a lawful owner-authored source and human determination of consequence. A controlled vignette in later stages can show how an omission propagates; it must remain hypothetical. A fork may expose more source conversation, yet current state and authority still come from task files. This is counterevidence to treating either file-only or forked context as universally sufficient.

### G5 — Extra boundaries are countable even before their performance cost is known

Under the current Plan/Research/Review contracts, a direct route needs worker → task Coordinator return, the Coordinator's checked artifact/state decision, and a separate next-role activation. A phase-local strategy route adds phase Coordinator → task Coordinator at each cross-phase boundary, and each phase Coordinator requires its own valid dispatch/state. A Gateway route adds a further owner-interface boundary for owner decisions and phase results, but does not absorb worker traffic under `tfw-gates-only`. A successor baton adds an immutable selection/dispatch and a current-file reconstruction. These are structural steps, not token/time measurements. Counting them tests H2/H4's claim of acceptable context cost without falsely assigning a speedup or failure rate.

## Checkpoint

| Found | Remaining |
|---|---|
| A second real dispatch repair shows scope continuation is distinct from control-file preparation. | Idle-parent return-to-turn still unobserved; use a normal gate only if the provider reports an idle parent at that moment. |
| Primary-folder instruction discovery is a concrete receiving-entry condition. | Verify how this project and a new receiver select the primary folder and exact instruction source; no cross-project result yet. |
| App-server separates message items, thread state and turn start; notifications are human-facing. | Mapping of `send_message_to_thread` to idle desktop task execution is undocumented here. |
| Owner intent in HL/record is inspectable; a real omitted criterion has no lawful source in this role. | Treat omission as a hypothetical until the owner identifies one; compare mechanisms without fabricating an outcome. |
| Added role boundaries can be counted. | Their context/attention costs remain unmeasured; later stages must compare exact obligations and evidence. |

**Sufficiency:**
- [x] External source used: official OpenAI Projects and chats, App Server, prompting and notifications documentation.
- [x] Briefing gap closed for Gather: refined dimensions and new receiving-entry/runtime counterevidence are explicit.
- [x] Dimensions identified: seven factors with at least three alternatives each.
- [x] Hypothesis tested: H3 against secondary-folder instruction discovery; H1/H5 against explicit turn-start semantics, with desktop mapping left open.
- [x] Counter-evidence sought: found a file-availability/instruction-discovery split and a message/turn split.
- [x] Metacognitive check: new findings are the primary-folder and turn-start distinctions; no idle-parent success was inferred from the active-turn snapshot.

**Decision D-G2.1:** A receiving-project claim needs evidence of both source reachability and governing instruction activation, not simply files in the repository.

**Decision D-G2.2:** Preserve the idle-parent case as unverified until an actual idle-state signal precedes a normal addressed gate and a next action is observed; active-turn returns are a different result.

## Material handover at this checkpoint

**Producer/source:** this Researcher, predecessor RES `946af78804aeaff48e21d1be34a48c6749916313`, current dispatch `5a994448b8987f0b12afad438e714eb812103aa4`, one native parent-status snapshot, current repository contract and linked official pages fetched 2026-09-28. **Inspected scope:** H1/H3/H5 counterexamples, seven refined dimensions, receiving entry and structural handover boundaries. **Material:** source reachability differs from instruction discovery; stored message/visible status differs from generation; iteration scope needed its own dispatch. **Uncertainty:** parent idle wake, actual owner omission, provider mapping and performance cost. **Continuation:** Coordinator decides whether Gather is sufficient; this same Researcher then compares complete/omitted intent and active/idle parent configurations in Extract.

---
Stage complete: YES
→ User decision: Await Coordinator Gather checkpoint under `native-gates`.
