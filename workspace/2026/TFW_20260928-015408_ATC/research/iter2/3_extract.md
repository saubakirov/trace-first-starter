# Extract — Which return paths remain distinct?

> **Mindset:** Analyst. Cross the gathered factors before assessing any route.
> **Parent:** [HL-TFW_20260928-015408_ATC.md](../../HL-TFW_20260928-015408_ATC.md)
> **Goal:** Advance authorized task roles and phases without routine owner command transfer while preserving strategic control.
> **Producer unit:** `codex:thread:local:01a0e687-ddc2-7081-b9a0-f9b5afd1d82e`
> **Parent Coordinator:** `codex:thread:local:01a0e442-ef8f-7e83-99fd-5efb81c52927`
> **Authority / dispatch:** frozen HL `0ba239b2f98ae66765f43a07e8122998c77f037d`; iteration 2 same-unit dispatch `5a994448b8987f0b12afad438e714eb812103aa4`; `native-gates`, `baseline`
> **Source window:** [Gather](2_gather.md) at `b104326fdc89c7e4322a33f31ba46b4b559e9a52`; official OpenAI pages checked 2026-09-28

## Configuration Space

The seven [Gather](2_gather.md) dimensions generate more than 30 combinations. The rows below span distinct return, intent, receiving-context, and topology states; they are scenario configurations, not evaluations or selections. D3's omitted criterion is hypothetical unless a lawful owner source identifies it. D5's addressed-follow-up alternative denotes a trigger to be verified, not a claim that the desktop tool wakes an idle task.

| Config | D1 Parent execution state at return | D2 Receiving context availability | D3 Intent fidelity | D4 Return evidence | D5 Continuation trigger | D6 Strategy boundary | D7 Branch/replacement complexity |
|---|---|---|---|---|---|---|---|
| E2-A | Active turn waiting for a named role | Current task files in primary project checkout | Consequential criterion in frozen HL | Artifact and task-local lineage verified | Active event wait | One continuing direct Coordinator | One bounded phase |
| E2-B | Loaded chat with no active turn | Current task files in primary project checkout | Consequential criterion in frozen HL | Artifact and task-local lineage verified | Addressed follow-up that starts a turn | One continuing direct Coordinator | One bounded phase |
| E2-C | Unloaded/closed chat | Current task files in primary project checkout | Consequential criterion in frozen HL | Ambiguous send with durable artifact but no confirmed receipt | Scheduled same-chat recheck | One continuing direct Coordinator | Long sequential phases |
| E2-D | Active turn waiting for a named role | Current task files in primary project checkout | Criterion in selected owner record but omitted from HL | Artifact and task-local lineage verified | Active event wait | One continuing direct Coordinator | One bounded phase |
| E2-E | Loaded chat with no active turn | Task files present but in secondary folder | Criterion only in owner conversation | Addressed-send receipt only | Owner starts named continuation | Task strategy Coordinator plus phase Coordinator | Long sequential phases |
| E2-F | Active turn waiting for a named role | Current task files in primary project checkout | Consequential criterion in frozen HL | Artifact and task-local lineage verified | Active event wait | Task strategy Coordinator plus phase Coordinator | Concurrent branches with dependencies |
| E2-G | Replacement unit selected, old unit stopped | Current task files in primary project checkout | Consequential criterion in frozen HL | Artifact and task-local lineage verified | Owner starts named continuation | Current successor Coordinator from files | Coordinator replacement mid-task |
| E2-H | Replacement unit selected, old unit stopped | Fork carries older chat history plus current files | Criterion in selected owner record but omitted from HL | Provider status signal only | Owner starts named continuation | Current successor Coordinator from files | Coordinator replacement mid-task |
| E2-I | Active turn waiting for a named role | Isolated checkout behind the needed commit | Consequential criterion in frozen HL | Addressed-send receipt only | Active event wait | Owner-facing Gateway plus phase Coordinator | One bounded phase |
| E2-J | Loaded chat with no active turn | Current task files in primary project checkout | Criterion absent or disputed even with owner source | Artifact and task-local lineage verified | Scheduled same-chat recheck | One continuing direct Coordinator | Long sequential phases |

An arrival with D1 active can coexist with a future scheduled check; D5 records the proposed *next-action* trigger. A replacement's owner-started continuation is one possible explicit trigger, not an authority transfer by itself. The table exposes E2-J, a gap outside the Briefing's simple complete/omitted split: even a reachable source may leave a consequential criterion disputed.

## Findings

### E1 — The eight intent × parent-state × duration cells have different failure witnesses

The compact comparison uses two D3 cases (criterion in frozen HL; criterion omitted from HL but asserted in a selected owner record), two D1 cases (active parent turn; loaded idle parent), and two D7 cases (bounded phase; long or branching work). It assumes current primary files and a checked return artifact so those factors cannot hide the distinction. “Omitted” remains a controlled vignette, not a finding about this owner's actual HL.

| Intent | Parent | Duration | Actor for the next action | Observable trigger / required witness |
|---|---|---|---|---|
| Complete HL | Active | Bounded | Direct task Coordinator | Checked return in the active wait, then exact next role activation. This is the closest match to current native gates. |
| Complete HL | Idle | Bounded | Same Coordinator if addressed follow-up starts a turn; otherwise owner/scheduler | Idle-state signal **before** addressed send, then recipient turn-start and next authorized action. Still unobserved. |
| Complete HL | Active | Long/branching | Direct task Coordinator or bounded task-strategy carrier | Recheck invariants and branch dependencies at each phase result; trace one actual cross-phase decision. |
| Complete HL | Idle | Long/branching | Same Coordinator on verified wake, or a lawfully selected successor | Recipient turn-start plus current-file reconstruction and an observed cross-phase decision. |
| Omitted HL | Active | Bounded | Owner for criterion resolution; Coordinator may hold the gate | Compare a lawful owner source with HL before declaring the step correct. Activity alone cannot supply the omitted criterion. |
| Omitted HL | Idle | Bounded | Owner for criterion resolution, after a proven turn trigger | Both wake and criterion resolution are independent witnesses; either can fail. |
| Omitted HL | Active | Long/branching | Owner resolves criterion; task strategy owner preserves it across phases | Source comparison and a later phase receiving check; a phase layer cannot infer missing intent. |
| Omitted HL | Idle | Long/branching | Owner resolves criterion; current Coordinator or lawful successor handles return | Need source resolution, a proven turn trigger, and later phase receiving evidence. |

The second and sixth cells keep H1/H5 open: an addressed-send receipt does not establish a turn start. [Codex App Server documentation](https://learn.chatgpt.com/docs/app-server) explicitly distinguishes `turn/start`, which begins generation, from `thread/inject_items`, which appends history without beginning a turn. That is API counterevidence to treating stored input as execution; it does **not** specify how this desktop `send_message_to_thread` maps to those methods. The observed Briefing checkpoint reached a parent with an `inProgress` turn, so it belongs in an active cell only.

### E2 — Topology changes the number of authority and context boundaries, not the liveness or fidelity requirements

Iteration 1 C1/C2 direct variants, if the parent is active or has a verified timed continuation, require one role-to-meaningful-Coordinator return, a checked artifact/authority decision, and a separate activation of the next role. C3 task-strategy plus phase-Coordinator adds a phase-to-task return at each cross-phase transition and distinct phase dispatch/receiving checks. C5 successor route adds an explicit selection/dispatch and current-file reconstruction when a Coordinator changes. These are counts of obligations, not token, latency, attention or error measurements. A Gateway adds an owner-interface boundary only where an owner-reserved decision must be routed; it supplies neither worker wake nor missing intent by itself.

For a single bounded phase with complete HL, no distinct failure shown here requires a strategy layer (E2-A/B). For long or branching work, C3 may have a distinct strategy address (E2-F), while a direct Coordinator may also preserve that strategy if current files and decision record remain sufficient. Neither is demonstrated superior. For replacement, C5 is distinct because the current receiver must establish its mandate and reconstruct the latest task state (E2-G/H). [Official worktree documentation](https://learn.chatgpt.com/docs/environments/git-worktrees) says a managed worktree starts at the selected branch's HEAD and ignored local files need an explicit `.worktreeinclude` exception; a fresh checkout is thus not proof that the newest task commit or every local context file is present. [Official App Server documentation](https://learn.chatgpt.com/docs/app-server) says a fork copies stored history through a chosen turn, may mark an in-progress turn interrupted, and reports loaded instruction sources separately. A fork is therefore a history carrier whose file epoch and instruction selection still need verification, not an authority carrier. These are counterexamples to a broad reading of H3/H4.

The minimal replacement input is: exact task/phase and current role address; frozen HL and selected owner record versions; effective status route/selection and scope; latest approved stage/return artifact and its Git lineage; unresolved gates and owner reservations; primary project/instruction source check; then one explicit continuation trigger. The recipient must report which items it actually read and any absent or stale input before material work. A title, fork ancestry, receipt or copied files cannot replace these checks. Reserved architecture, frozen amendments, TS, implementation and release decisions route to the owner as the HL specifies; a phase Coordinator cannot silently adopt them.

### E3 — A receiving entry needs two checks; a return needs a third

The [Projects and chats documentation](https://learn.chatgpt.com/docs/projects) distinguishes primary-folder automatic discovery of `AGENTS.md`, skills and configuration from readable secondary folders. Thus D2 “files present in a secondary folder” does not imply that governing entry instructions were selected. The [App Server](https://learn.chatgpt.com/docs/app-server) exposes `instructionSources` for thread start/resume/fork; it demonstrates that loaded instruction sources are a separately inspectable property at the API surface, without proving this desktop receiver exposes the same readback. D4 and D5 add the third check: a return must be checked and cause an observed next turn/action. The three checks are (1) task files reachable at the required epoch, (2) governing instructions actually activated on the receiving surface, and (3) return trigger producing the next authorized action. A success claim that reports only one or two is narrower.

The smallest decision-changing native observation for H1/H5 is one normal gate sent to an *already idle* exact Coordinator, with an idle signal before send and a later turn-start plus task-local next action. A negative result or ambiguous delivery would not prove all send paths fail; it would constrain this desktop path under those conditions. For H3, a receiving-project demonstration would record the selected primary folder, exact file commit, actual instruction source and a bounded task decision. For omitted intent, only an owner-authored consequential criterion outside the HL, or the owner's judgment on a controlled vignette, can convert the hypothetical cell into an actual fidelity result. No such criterion is available in this role.

## Checkpoint

| Found | Remaining |
|---|---|
| Eight-cell comparison separates intent fidelity, parent state and task duration; activity does not repair omitted intent. | Actual owner omission, if any, requires owner evidence. |
| Direct, phase-strategy, successor and Gateway paths have distinct authority/context boundaries. | Relative token/time/attention cost and long-task performance are unmeasured. |
| New E2-J shows that even a reachable owner source may leave a criterion disputed. | Owner judgment would resolve whether the criterion is consequential. |
| Worktree/fork source counterexamples require commit and instruction-source checks at receiving entry. | Cross-project receiving demonstration and idle-parent wake remain unobserved. |

**Sufficiency:**
- [x] External source used: official Codex App Server, Worktrees and Projects documentation.
- [x] Briefing gap closed for Extract: complete/omitted × active/idle × bounded/long cells, topology boundaries, evidence levels and smallest change-making observations are explicit.
- [x] Configuration Space built from all seven Gather dimensions; >30 theoretical combinations are represented by distinct noncontradictory configurations without evaluating them in the table.
- [x] Hypotheses tested: H1/H5 against explicit turn-start semantics; H3/H4 against worktree epoch, ignored-file and fork-history counterexamples.
- [x] Counter-evidence sought for both direct and added-boundary routes; neither receives an unsupported success claim.
- [x] Metacognitive check: new distinctions are a disputed-but-present owner source (E2-J), the three-part receiving/return witness, and the worktree/fork epoch checks; actual idle wake remains unknown.

**Decision D-E2.1:** Keep topology, intent fidelity and liveness as independent variables; an extra role boundary cannot be credited with resolving missing intent or starting an idle turn without a witness.

**Decision D-E2.2:** Compare candidate routes by exact checked obligations and receiving evidence until measured context/attention cost or a native idle-parent result exists; do not rank them by assumed performance.

**Decision D-E2.3:** Carry both source reachability and actual instruction activation into Challenge for every new or replacement receiver, then require an observed next-action trigger for any autonomous-continuation claim.

## Material handover at this checkpoint

**Producer/source:** this Researcher; Gather `b104326fdc89c7e4322a33f31ba46b4b559e9a52`, predecessor RES `946af78804aeaff48e21d1be34a48c6749916313`, frozen HL and linked official documentation checked 2026-09-28. **Inspected scope:** eight intent/state/duration cells, C1/C2 versus C3/C5 structural boundaries, replacement input and receiving-source counterexamples. **Material:** three independent success witnesses and explicit owner-reserved path; E2-J disputed-source combination. **Uncertainty:** native idle wake, actual omitted owner criterion, cross-project instruction activation and performance cost. **Continuation:** Coordinator decides whether Extract is sufficient; this same Researcher will then stress the surviving paths in Challenge.

---
Stage complete: YES
→ User decision: Await Coordinator Extract checkpoint under `native-gates`.
