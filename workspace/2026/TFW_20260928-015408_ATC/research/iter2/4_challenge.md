# Challenge — What fails after a correct-looking return?

> **Mindset:** Critic. A plausible route survives only with its missing witness named.
> **Parent:** [HL-TFW_20260928-015408_ATC.md](../../HL-TFW_20260928-015408_ATC.md)
> **Goal:** Advance authorized task roles and phases without routine owner command transfer while preserving strategic control.
> **Producer unit:** `codex:thread:local:01a0e687-ddc2-7081-b9a0-f9b5afd1d82e`
> **Parent Coordinator:** `codex:thread:local:01a0e442-ef8f-7e83-99fd-5efb81c52927`
> **Authority / dispatch:** frozen HL `0ba239b2f98ae66765f43a07e8122998c77f037d`; same-unit iteration 2 dispatch `5a994448b8987f0b12afad438e714eb812103aa4`; `native-gates`, `baseline`
> **Source window:** [Extract](3_extract.md) at `12b1f4958ced9b4508870e055781e94b0ab5b563`; official OpenAI pages checked 2026-09-28

## Consistency Check

I checked all 21 pairs of the seven [Gather](2_gather.md) dimensions. Most pairs are compatible as *states* even when they cannot yield a lawful next action: a stale checkout can receive a message, a fork can carry older history while current files exist, and a disputed criterion can coexist with any topology. The incompatible pairs below use the same parent/instant and the alternatives' literal definitions. They do not eliminate a later scheduled or owner-initiated action.

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|---|---|---|---|---|
| D1 Parent execution state at return | Loaded chat with no active turn | D5 Continuation trigger | Active event wait in that same parent turn | There is no active turn in which to wait at this instant. |
| D1 Parent execution state at return | Unloaded/closed chat | D5 Continuation trigger | Active event wait in that same parent turn | The parent is not executing the wait. |
| D1 Parent execution state at return | Active turn waiting for a named role | D5 Continuation trigger | Addressed follow-up that starts a **new** turn at that same instant | The parent already has an active turn; an incoming message may steer or queue, but this pair cannot prove a new-turn start. |
| D1 Parent execution state at return | Replacement unit selected, old unit stopped | D5 Continuation trigger | Active event wait in the stopped old unit | The old unit cannot be the current next-action actor. A wait in the replacement is a different state. |

**Surviving configurations:** No Extract row contains the incompatible pair at the same instant. Logical survival does not mean the route passes the three success witnesses.

| Config | D1 Parent execution state at return | D2 Receiving context availability | D3 Intent fidelity | Notes |
|---|---|---|---|---|
| E2-A | Active turn waiting | Current primary files | Frozen HL | Native gate analogue; next-role act still required. |
| E2-B | Loaded idle | Current primary files | Frozen HL | Conditional on actual desktop turn start. |
| E2-C | Unloaded/closed | Current primary files | Frozen HL | Time-based re-entry may occur under host/app conditions; not event wake. |
| E2-D | Active turn waiting | Current primary files | Selected owner record omitted from HL | False-success risk despite prompt return. |
| E2-E | Loaded idle | Secondary-folder files | Owner conversation only | Source and instruction activation unresolved. |
| E2-F | Active turn waiting | Current primary files | Frozen HL | Strategy boundary has a distinct cross-phase edge. |
| E2-G | Replacement selected | Current primary files | Frozen HL | New unit needs exact mandate and current lineage. |
| E2-H | Replacement selected | Older fork plus current files | Selected owner record omitted from HL | History and file epoch must be reconciled. |
| E2-I | Active turn waiting | Checkout behind needed commit | Frozen HL | Receipt does not repair missing dispatch. |
| E2-J | Loaded idle | Current primary files | Absent/disputed criterion | Owner judgment is a separate dependency. |

**Unexpected survivors:**
- **E2-C:** An unloaded chat plus a scheduled same-chat recheck is not logically contradictory. [Scheduled tasks documentation](https://learn.chatgpt.com/docs/automations) describes same-chat context and desktop local-project runs, but local runs require the computer on and app running. It is a conditional time trigger, not the role-return event.
- **E2-I:** A message receipt can coexist with a stale checkout; the receiver still lacks the needed task-local dispatch and must stop.
- **E2-J:** Complete file reachability can coexist with an unresolved consequential criterion. More transport or more role layers cannot decide it.

## Findings

### C1 — One phase can pass the routing check while failing the next-action check

**Trace:** A role finishes one bounded phase, commits its artifact, and sends an exact vertical return. The active direct Coordinator reads the checked artifact, verifies status and scope, then activates the next authorized role or reports an owner gate. This is compatible with observed Briefing/Gather gate behavior in this iteration, although the observed parent had an `inProgress` turn. If the same return reaches a loaded idle Coordinator, a send receipt and status update establish delivery/readback at most; the missing step is a *new recipient turn* followed by a task-local next action. [App Server documentation](https://learn.chatgpt.com/docs/app-server) distinguishes thread state, `turn/start`, and history injection without a new turn. This is a counterexample to H1/H5 interpreted as “durable return automatically wakes the parent.” The desktop `send_message_to_thread` mapping remains unverified, so this challenges a strong claim without falsifying the possible native path.

**False-success injection:** The return artifact exists and the Coordinator's sidebar status changes, but no next-role dispatch appears. The correct report is “return delivered or visible; advancement unproved.” A timer can recheck that state, if the local scheduler and app are available, but its recheck cadence and host dependence differ from event continuation. [Official scheduled-task documentation](https://learn.chatgpt.com/docs/automations) says desktop local-file runs need the computer on and app running and that event-triggered scheduled tasks are not available in the desktop app. A schedule cannot be credited as the missing immediate worker-return trigger.

A compact native status snapshot immediately before this Challenge gate again reported the parent turn `inProgress`. This is a second active-parent observation, not an idle-parent test; no parent transcript or unfinished work was inspected.

### C2 — Long, branching and replacement paths make different files and authority fail

**Long sequential trace:** Direct C1/C2 can preserve task strategy in the same Coordinator if each phase result, unresolved decision and next mandate are in current files and the context remains usable. C3 task-strategy/phase Coordinator can bound phase traffic, but every phase result crosses an additional vertical boundary into a lawful task-strategy actor, then requires a new phase dispatch. If that task-strategy actor is idle and cannot be started, the extra layer simply moves the liveness gap upward. Neither route has comparative token/time or owner-attention evidence here. H2/H4 remain conditional, not a reason to impose the hierarchy.

**Branching trace:** Two independent branch results can arrive in either order. A task-level actor must verify branch identities, dependency state and the next shared gate before integrating either. A phase-local unit cannot issue a cross-branch decision merely because it received its own branch result. Duplicate Reviewer envelopes with the same artifact lineage cannot be counted as two independent completions; the receiving actor must correlate actual unit, phase, artifact and return identity before one next-action decision. This is an analytical stress case, not an observed duplicate delivery.

**Replacement trace:** E2-G/H require the new unit to read current task/phase control, its own exact dispatch and current artifact lineage before a decision. An old title or fork transcript is insufficient. [Worktree documentation](https://learn.chatgpt.com/docs/environments/git-worktrees) states managed worktrees begin at a selected branch HEAD and ignored files are copied only by configured inclusion (with a documented override exception). [App Server documentation](https://learn.chatgpt.com/docs/app-server) states a fork copies stored history and can mark a mid-turn source interrupted; it separately reports instruction sources for start/resume/fork. These facts supply counterevidence to H3's strongest “fork/file handover always suffices” reading. A replacement with current files but a criterion omitted from HL still needs the owner source and a lawful decision on its consequence. A successor selection does not turn inherited text into owner authority.

### C3 — Intent and evidence injections expose correct stops, not topology winners

**Omitted criterion vignette:** Suppose the owner-selected record includes a consequential criterion absent from the frozen HL and a new Executor follows that HL exactly. Its prompt artifact and Coordinator return can be mechanically correct yet miss the target. If the receiving project never sees the selected record, it cannot detect the omission from the HL alone. If it sees a discrepant record, the discrepancy is a question for the owner or the HL's reserved amendment path; the Researcher cannot declare the criterion binding or rewrite frozen scope. This case has *not* been observed for the real owner. E2-J is stricter: even an available owner source may be disputed or unclear, so retrieval alone is not resolution. The [Projects documentation](https://learn.chatgpt.com/docs/projects) adds a separate hazard: files in a secondary folder can be readable without automatic governing-instruction discovery.

**Ambiguous send:** If a send times out after a durable artifact is committed, neither blind resend nor assumption of failure is warranted. The Coordinator (or scheduled/owner continuation if it is idle) must inspect task-local return identity and recipient state, then accept at most one checked return. A provider status signal without artifact/lineage verification is weaker. This is a proposed idempotent decision rule, not a tested guarantee of this provider's send behavior.

**Owner-reserved change:** If Challenge uncovers a frozen HL amendment, architecture choice, TS approval, implementation or release decision, the role can classify and route it to the owner but cannot continue as if the gate were routine. A Gateway label, title, fork or phase strategy unit cannot absorb the reserved choice. Current research proposes no amendment; it tests this boundary to prevent a false “fully autonomous” claim.

### C4 — Evidence tiers for the survivors

| Claim | Current native observation | Official provider documentation | Missing proof / smallest next witness |
|---|---|---|---|
| Exact same-unit mandate and active parent gate | Iteration 2 was stopped on missing new dispatch, then resumed after committed dispatch; Briefing/Gather gates reached a parent whose sampled turn was active. | App Server defines separate thread and turn actions. | One normal return with an idle signal *before* send, recipient turn start, and a current-file next-role act. |
| Current-file receiver can begin a bounded role | This Researcher read exact route, dispatch and current stage files in its isolated checkout after fast-forward. | Projects documents primary-folder instruction discovery; Worktrees documents starting commit behavior. | New receiving project confirms primary folder, loaded governing instructions, exact current commit and one correct bounded decision. |
| Direct route carries long strategy | No long-task outcome measured. | Long-running work guidance recommends preserving related work in the same chat and source project; it is guidance, not a capacity guarantee. | One long/branch trace with checked phase decisions and measured context/attention cost. |
| Phase or successor boundary resolves long/replacement risk | No phase Coordinator or successor run was created in this role. | Worktree/fork docs describe isolated files/history, not TFW authority. | Lawful dispatch and receiving-entry demonstration through a real cross-phase or replacement gate. |
| Timed same-chat fallback | No task schedule was created or run here. | Scheduled tasks documents time-based local runs subject to computer/app availability; desktop app events are unavailable. | A configured same-chat run with source/route reconstruction, duplicate suppression and observed lawful next action; compare its delay/conditions with the owner requirement. |
| Omitted owner criterion is detected | No actual omitted criterion was supplied to this Researcher. | Provider docs cannot determine the owner's intended target. | Owner-authored criterion or owner verdict on a controlled vignette, then source-to-HL-to-receiver comparison. |

## Checkpoint

| Found | Remaining |
|---|---|
| All ten Extract rows are logically consistent; four same-instant parent/trigger pairs are incompatible. | Logical survival does not establish success or performance. |
| A direct route has the shortest structural chain in a bounded active-parent case; a phase boundary has a distinct cross-phase strategy address and additional edges. | No measured comparative cost or long-task outcome. |
| Stale checkout, fork history, secondary-folder instructions, ambiguous return and disputed intent each admit a false-success report. | Real receiving-project, idle-parent and owner-intent witnesses remain absent. |
| Local scheduled re-entry is conditionally documented, with host/app requirements and no desktop app-event trigger. | No scheduled fallback was configured or observed. |

**Sufficiency:**
- [x] External source used: official Codex App Server, Worktrees, Projects, Scheduled tasks and Long-running work documentation.
- [x] Briefing gap closed for Challenge: one-phase, long sequential, branch, replacement, omitted/disputed criterion, stale route, ambiguous send, duplicate Reviewer and owner-reserved decision were stressed.
- [x] Pairwise incompatibility checked across all seven dimensions; surviving Extract configurations and unexpected survivors listed.
- [x] Hypotheses tested: H1/H5 against missing turn-start witness, H2/H4 against added authority edges, H3 against stale checkout/fork/secondary-folder cases.
- [x] Counter-evidence sought for direct, phase, successor and timed routes; no route promoted beyond its evidence.
- [x] Metacognitive check: the new finding is that a scenario may survive all logical-pair checks yet fail the source/instruction/next-action witness; E2-J remains unresolved even with reachable source. No real owner omission or idle wake was inferred.

**Decision D-C2.1:** Treat “survives scenario consistency” and “passes continuation acceptance” as separate findings. A route passes only with current reachable files, activated governing instructions, checked return and an observed authorized next action, plus resolved owner intent for consequential criteria.

**Decision D-C2.2:** Retain direct, phase-strategy and lawful successor routes as conditional options; keep Gateway and fork as narrow interface/history variants only when they address an identified failure. Count the extra edges, but leave their performance value open.

**Decision D-C2.3:** Present the idle-parent turn-start, receiving-project instruction activation, real omitted-intent criterion and measured long-task cost as open owner-facing limits. A desktop schedule is a conditional audit/fallback with different trigger semantics.

## Material handover at this checkpoint

**Producer/source:** this Researcher, Extract `12b1f4958ced9b4508870e055781e94b0ab5b563`, current task files and linked official OpenAI documentation checked 2026-09-28. **Inspected scope:** pairwise dimension consistency, ten configurations, adversarial traces and evidence tiers. **Material:** no topology is selected; three distinct receiving/return witnesses and owner-intent resolution are required for an acceptance claim; documented schedule behavior is time-based with local host/app conditions. **Uncertainty:** exact idle desktop turn start, cross-project instruction activation, real omitted criterion, comparative context cost and ambiguous-send runtime behavior. **Continuation:** Coordinator closes or returns this Challenge gate; on clearance this same Researcher synthesizes iteration 2 RES and stops.

---
Stage complete: YES
→ User decision: Await Coordinator Challenge checkpoint under `native-gates`.
