# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. The surviving configurations are attacked against the simpler control, the independence ceiling and the Full-shadow failure case.
> **Test:** "Would the Team claim survive if persistence, role labels and artifact count were denied as evidence by themselves?"
> Parent: [HL-TFW-52](../../HL-TFW-52__tfw_light_v1.md)
> Goal: Determine whether Team has a stable, independently useful working mechanism between Assisted and Full, while preserving the simpler Assisted-plus-subagents answer if H9 fails.

## Evidence Boundary and Claim Labels

Challenge adds no live experiment. No task, thread, subagent, worktree, permission boundary, identity boundary, Handoff, restart, cross-user session or external write was created. It attacks Extract using only the Gather source set, the bounded behavior of this Iteration 3 Researcher task and repository precedents.

| Label | Evidence lane | Permitted claim in Challenge |
|---|---|---|
| **D — documented** | Current official Codex manual: [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Projects and chats](https://learn.chatgpt.com/docs/projects), [Long-running work](https://learn.chatgpt.com/docs/long-running-work), [Worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees), [Codex App Server](https://learn.chatgpt.com/docs/app-server), [Code review](https://learn.chatgpt.com/docs/code-review), [Remote connections](https://learn.chatgpt.com/docs/remote-connections) and [Approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security). | A supported product capability or limitation, not an executed Team guarantee. |
| **O — observed** | M3-E1–E5 from this Researcher task plus read-only repository/app observations recorded in Gather and Extract. | Separate user-owned task creation, multi-checkpoint visibility/persistence, follow-up delivery, coordinator read/wait completion routing and shared-checkout artifact visibility only. |
| **U — unavailable/unproven** | Capabilities not exercised or not established by official support. | Must remain a limitation: executor/reviewer exercise, worktree isolation, permissions, identity, needs-attention, Handoff, restart, cross-user behavior, transactional messaging and enforced single-writer ownership. |
| **P — proposed TFW behavior** | C2/C3/C5/A2 protocols derived in Extract. | A design candidate or falsifiable rule, never a current Codex or Team guarantee. |

The four lanes are not additive by implication. In particular, **D + O does not promote P into an executed guarantee**, and one observed Researcher lane does not establish executor/reviewer separation.

## Consistency Check

### Incompatible pairs

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|---|---|---|---|---|
| D3 Session ownership | Parent-owned child tree | D11 Persistence/resume | Independently resumable user-owned role lane | C0/C1 child control is owned and resumed through the parent orchestration context; no user-owned persistence was established for it. |
| D8 Permission boundary | Same user/runtime or procedural restriction | D10 Review separation | Organizationally independent reviewer | A separate prompt/task cannot prove inability to mutate, independent credentials or reject authority. |
| D9 Artifact ownership | Everyone may edit shared mutable files | D5 Execution location | Concurrent shared non-Git root | Visibility does not serialize writes; without disjoint paths or an external lock/merge system, collision safety is false. |
| D9 Artifact ownership | Single writer by convention only | D10 Review separation | Reviewer cannot repair executor output | The rule is inspectable after the fact but not enforced; “cannot mutate” is an unsupported claim. |
| D13 Role cardinality | Owner/coordinator/reviewer are one actor | D10 Review separation | Reviewer independent of planning and acceptance preference | C2 separates review from execution only. It cannot claim planner-independent or organizational review. |
| D14 Upward mapping | Full HL/TS/ONB/RF/REVIEW/evidence already required | Edition boundary | Team is an intermediate edition | This is C7: Full under a different name. |
| D14 Upward mapping | Three mandatory new Team files on every task | Assisted preservation | Reuse existing task TRACE/memory with no duplicate bureaucracy | A fixed A2 spine repeats outcome, criteria, plan, questions, trace and verification that Assisted already records. |
| D12 Integration authority | Coordinator is sole resolver/integrator with no owner succession rule | D11 Persistence/resume | Team survives coordinator abandonment | Files preserve state, but authority to answer blockers, reassign and accept is still absent. |
| D4 Context transfer | Mutable latest files with no version manifest | D11 Persistence/resume | Fail-closed stale-context recovery | A resumed role cannot distinguish current authority from a changed brief/result. |

### Configuration verdicts after attack

| Config | Challenge result | Evidence basis | Edition consequence |
|---|---|---|---|
| **C0 — Assisted control** | **Survives** for one accountable owner, one active lane and reversible work. | **D:** subagents already provide bounded specialists and review assistance. **P:** Assisted TRACE/memory remains the project state. | Default simpler answer. |
| **C1 — explicit child tree** | **Survives inside Assisted**, not as Team. | **D/O:** stronger orchestration and context control, but parent authority/shared checkout remain. | Assisted execution engine. |
| **C2 — two-party persistent handoff** | **Eliminated as a Team definition; retained as an optional delegated-work pattern.** | **O:** persistence is real. **U:** planning-independent review and independent authority are absent. Coordinator function adds little for one assignment. | Assisted delegation pattern, not stable Team. |
| **C3 — three-lane persistent shared root** | **Survives only as a Team pilot configuration.** | **P:** distinct coordinator/executor/reviewer records are coherent. **U:** executor/reviewer flow, enforcement, stale recovery and concurrent editing are unexecuted. | Candidate to validate; insufficient for stable edition now. |
| **C4 — persistent worktrees** | **Retained only as a Git adapter for a future C3/C5 pilot.** | **D:** checkout isolation exists. **U:** not executed here and not permission/authority isolation. | Never an edition invariant. |
| **C5 — artifact-bus Team** | **Survives only as the semantic protocol candidate.** | **P:** transcript-independent handoff and non-Git applicability are coherent. **U:** no executed recovery, ownership enforcement or multi-role concurrency. | Candidate protocol, not proven edition. |
| **C6 — independent human/session team** | **Survives as the independence ceiling, not the minimum.** | **U/external:** different identities/policies could enforce authority, but cross-user behavior is outside current evidence. | Defines claims that one-user Team must not make. |
| **C7 — Full-shadow Team** | **Eliminated.** | Requiring the Full artifact/gate chain erases the intermediate boundary. | Use Full directly. |
| **C8 — assurance overlay** | **Survives and defeats Team for review-only need.** | **D:** detached review/separate review chat is supported; **P:** a frozen input and separate verdict add bounded assurance. | Optional Assisted review pattern. |

### Unexpected survivors

- **C8 survives more strongly than C2.** When the only missing control is fresh, non-self review, a separate reviewer task plus a frozen result supplies the relevant separation without a coordinator lane or three-file spine.
- **C5 survives without proving an edition.** It identifies the semantic packet needed for a future Team mechanism, but a coherent protocol can remain an optional pattern until its operational guarantees are executed.
- **C0/C1 remain valid even after M3-E1–E5.** The observed persistent task does not make persistence necessary for bounded work; it only proves availability of another carrier.

## Findings

### C1 — Persistence alone does not justify an edition

**Attack.** M3-E1–E5 demonstrate a durable, separately visible Researcher task beyond a parent-owned subagent. The same evidence does not show that the task had distinct authority, could reject the coordinator, survived restart, recovered after abandonment, or coordinated concurrent writers. A saved transcript is a product capability, not yet a workflow invariant.

| Observable outcome | C0/C1 | C2/C3/C5 candidate | Challenge result |
|---|---|---|---|
| Work can continue over multiple turns | Main task and files already do this | Separate task also does this (**O**) | No edition distinction by itself. |
| Worker can be addressed separately | Parent addresses child; owner addresses main task (**D**) | Coordinator followed a user-owned task (**O**) | A carrier distinction, not semantic assurance. |
| Work survives hidden transcript loss | Assisted TRACE may preserve task state (**P/boundary**) | Artifact packet proposes reconstruction (**P**) | Neither path was restart-tested here. |
| Worker has independent authority | No | **U** | No demonstrated Team distinction. |
| Parallel work is collision-safe | Shared checkout warning applies (**D**) | Single-writer/disjoint paths proposed (**P**) | Not executed or enforced. |

**Conclusion:** persistence is **necessary for a persistent-lane Team candidate but insufficient for an edition**. An edition must add repeatable semantic delegation, recovery and review outcomes that the simpler control cannot produce with lower overhead.

### C2 — One-user separate tasks are role separation, not a human team or independent authority

The observed coordinator↔Researcher boundary is real at the transcript/task level (**O**). It is not a separate identity, permission domain or owner (**U**). The same user/coordinator can steer the task and controls which output is integrated. Therefore one user's separate tasks may honestly be called **separate role sessions** or a **multi-session agent pattern**. They are not enough to claim:

- independent human participation;
- authenticated authorship or non-repudiation;
- independent approval authority;
- inability of the reviewer to alter implementation;
- cross-user assignment or visibility.

This does not erase the usefulness of separate tasks. It bounds the name and promise. A stable edition named Team would need to say whether “Team” means role-separated agent sessions or independently governed participants. Current evidence supports only the first, and only for the Researcher lane.

**C-D1:** Do not use one-user task count as the edition discriminator. The discriminator, if later validated, must be durable delegation across at least two separately resumable role owners plus an observable handoff/recovery contract.

### C3 — C2 review independence is materially misleading unless qualified

C2 collapses owner, coordinator and reviewer into one actor. That actor writes the brief, chooses acceptance criteria, steers the executor, reads the result and issues the verdict. This can still catch implementation errors because the reviewer did not produce the executor result. It cannot test whether the plan itself is biased, incomplete or fitted to the desired verdict.

| Claim | C2 can support? | Honest evidence level/label |
|---|---|---|
| Reviewer is separate from executor | Yes, if the executor is a separate actor/session and the verdict is frozen | **P**, not executed here; “execution-separated review.” |
| Reviewer is separate from planning | No | Incompatible; do not claim. |
| Reviewer has independent identity/policy | No evidence | **U**; C6 only. |
| Review result is independently inspectable | Yes, if exact input versions and a non-mutating verdict are retained | **P**; inspectable trace, not independent authority. |
| Two people obtain useful acceptance separation | Possibly | Conditional on a finding/verdict affecting the outcome; otherwise ceremony. |

For two actors, “owner/coordinator accepts executor output” is more accurate than “independent reviewer.” If an edition requires a reviewer, C2 fails its minimum claim. If it does not, C2 collapses to Assisted delegated execution.

**C-D2:** Eliminate C2 as the minimum Team edition. Retain it as an Assisted handoff pattern with **owner acceptance**, not an independent-review promise.

### C4 — C8 defeats C2 and often C3 when the problem is review only

C8 adds a fresh, separately visible reviewer task to Assisted execution. It does not need a coordinator lane because the owner routes one frozen review packet and receives one verdict. Against C2, it avoids pretending that ordinary delegation is team coordination. Against C3, it avoids a permanent three-lane lifecycle when the work has no parallel assignments, dependencies or integration problem.

C8 is sufficient when all of the following hold:

1. one owner/executor remains accountable for the work;
2. the result and criteria can be frozen for review;
3. the reviewer does not repair the result;
4. planner-independent or organizational authority is not claimed;
5. one verdict/revision round is enough.

C8 is insufficient when multiple role owners must accept assignments, route blockers independently, resume after coordinator absence, or integrate concurrent outputs. Those are the only remaining reasons to test C3/C5.

### C5 — Three mandatory files duplicate Assisted and are not the true minimum

Assisted already gives each meaningful task a `TRACE.md` containing the owner, desired result, criteria, Working Backwards plan, questions/decisions, work trace, verification, result/status links and knowledge candidates. Its memory layer already preserves task traces and derives shared knowledge. A mandatory A2 `BRIEF.md` and `EXECUTION.md` would repeat much of that state; a `REVIEW.md` is useful only when a distinct reviewer exists.

| A2 content | Existing Assisted home | Duplicate risk | Surviving semantic need |
|---|---|---|---|
| Outcome, constraints, criteria, plan | Task `TRACE.md` | High | Freeze the coordinator-owned assignment revision when another writer receives it. |
| Questions, decisions, working trace, verification | Task `TRACE.md` | High | Preserve executor ownership and input/output version references. |
| Status | Task folder/status + TRACE | High | One derived coordination status may link role records; do not create a second task board. |
| Knowledge observations | TRACE → candidates/records/index | High | Link to existing memory pipeline; create no Team memory layer. |
| Independent findings and verdict | No equivalent when review is separate | Low | Separate reviewer-owned record only when review is required. |

The real minimum is therefore a **logical handoff spine**, not three mandatory filenames:

- reuse the existing Assisted executor `TRACE.md` as the execution record;
- add one coordinator-owned frozen assignment/decision record only when work crosses a role-owner boundary;
- add one reviewer-owned verdict record only when a distinct review lane is justified;
- keep output manifests in the owning record and shared project memory unchanged.

For C2, the coordinator's assignment and owner acceptance may share one coordinator-owned record, yielding two role-owned records total. For C3/C5, three logical records remain appropriate because there are three writers. For C8, the Assisted trace plus a reviewer record is enough. Filenames and templates belong to later design; Challenge does not modify Assisted or the master HL.

**C-D3:** Reject A2 as a mandatory three-new-file floor. Preserve its semantic mapping as a **maximum-minimum for three distinct writers**, with physical artifact count equal to distinct mutable owners not already represented by Assisted TRACE.

### C6 — Single-writer discipline is not an enforced safety boundary

Official Codex guidance warns that parallel write-heavy work on the same files can conflict (**D**). The current collaboration tree shares a directory, and this Researcher task shared artifact visibility with the coordinator (**O**). No current evidence proves file ACLs, per-role write restrictions, transactionality or conflict-free saves (**U**).

Single-writer ownership therefore has three assurance levels:

| Level | Mechanism | What it can claim |
|---|---|---|
| **W1 procedural** | Prompt/template says who owns a file/path | Attribution and post-hoc violation detection if traces are honest; no prevention. |
| **W2 structural** | Disjoint role directories, immutable revision filenames, coordinator-only aggregate | Reduces accidental collisions; still same-user writable and manual. |
| **W3 enforced** | External ACL, separate credentials, protected review/change-control or equivalent | Can prevent unauthorized mutation; outside current evidence/default Team. |

C3/C5 can target W2, not W3. Worktrees improve checkout isolation for Git but do not prove role authority. In a shared non-Git root, Team must **forbid concurrent mutation of the same output**, allocate disjoint output paths and serialize integration through one named owner. If the task inherently requires several writers to the same mutable artifact, C3/C5 has no safe domain-agnostic mechanism; use a domain collaboration system or Full/external change control.

This restriction narrows the candidate considerably. “Collision-safe Team” is unsupported; “collision-avoiding ownership protocol with detectable revisions” is the strongest honest claim.

### C7 — Abandoned and stale tasks expose missing recovery semantics

M3-E2 proves this task remained available across several checkpoint turns (**O**), not that it survives app restart or that an abandoned task resumes safely (**U**). Artifact state helps only if the last write is complete and the role declared its exact input revision.

| Failure | What remains | Unsafe default | Minimal recovery rule (**P**) |
|---|---|---|---|
| Executor task disappears before accepting | Frozen assignment | Coordinator assumes work began | Reassign from the same assignment revision; mark old locator abandoned. |
| Executor disappears mid-output | Possibly partial TRACE/result | New executor edits partial state in place | Freeze partial revision, assign a new executor-owned revision/path, record provenance. |
| Reviewer disappears | Frozen result packet | Coordinator self-approves while claiming independent review | Replace reviewer explicitly or downgrade assurance; never silently relabel owner acceptance as review. |
| Resumed task has stale brief | Old transcript/files | Continues mutation | Compare declared input revision/digest and stop on mismatch. |
| Coordinator disappears | Role-owned outputs may exist | No one can answer blockers or integrate | Owner appoints successor in a new authority record; old coordinator record remains provenance. |
| Owner and coordinator are the same and disappear | Work may continue technically | No acceptance/reassignment authority | Stop; external human authority is required. Persistence cannot solve missing authority. |

A lease/heartbeat would add expiry, clock and split-brain problems already exposed by predecessor Assisted research. It is not justified for the minimum Team pattern. Recovery should be explicit reassignment from immutable versions, not automatic takeover. This is coherent but unexecuted.

### C8 — The coordinator is a single point of decision and integration failure

C3/C5 centralize brief revisions, blocker answers, dependency state and integration in the coordinator. The artifact bus prevents the coordinator's hidden transcript from being the only source, but it does not distribute authority. If the coordinator is unavailable:

- executor and reviewer can finish only work already bounded by frozen packets;
- new scope decisions, conflict resolution and final integration stop;
- app read/send/wait does not elect a replacement;
- a replacement needs owner authority and an explicit succession record;
- if owner and coordinator collapse, there is no internal Team failover.

This is acceptable for a small delegated workflow only if described as **recoverable state with human reassignment**, not high availability. Adding replicated coordination, quorum, automated leases or distributed task governance would approach C7/Full or an external project-management system.

### C9 — Non-Git concurrent editing remains a hard boundary

C5 was attractive because its semantic protocol does not depend on Git. That does not make arbitrary non-Git products safely mergeable. Separate role records can avoid collisions, but the product output may still be a spreadsheet, document, image, database, cloud object or single local file with no useful merge operation.

The candidate survives only with a scope rule:

1. parallel assignments own disjoint outputs or immutable revisions;
2. one named integrator owns any shared mutable output;
3. workers return proposals/patches/copies rather than concurrently editing the integration target;
4. the handoff record identifies the exact source and result version;
5. if the domain system offers its own locking/versioning, Team records it as an adapter guarantee rather than a TFW guarantee.

Without this rule, C5 fails. With it, C5 coordinates independent deliverables but cannot promise generic concurrent co-editing.

### C10 — C6 exposes the ceiling; C7 exposes edition collapse

C6 distinguishes process separation from independent authority. Different people, accounts, credentials or organizational policies may make reviewer rejection and mutation restrictions enforceable. Codex documentation and this experiment do not establish cross-user assignment, ACLs or identity proof (**U**). A stable one-user Team edition must not borrow C6 language.

C7 shows the opposite failure. If Team adds Full HL/TS/ONB/RF/REVIEW, evidence planning, knowledge gates, migration receipts and formal approvals to repair every gap above, it ceases to be intermediate. The stable boundary, if later proven, must be narrower:

- Team coordinates delegated work through role-owned handoffs;
- Full governs consequential lifecycle decisions, research, specification, evidence and knowledge promotion.

Current C3/C5 do not yet demonstrate the first line strongly enough to ship as an edition, while C7 over-solves it.

### C11 — What would falsify or support a future stable Team edition

No further experiment is authorized in this stage. Challenge converts the uncertainty into exact future acceptance tests rather than assuming success.

| Test | Required observable result | Failure interpretation |
|---|---|---|
| **F1 Delegated execution** | A separate executor accepts a versioned assignment, asks/receives a blocking decision through owned records and returns a versioned result without coordinator transcript dependence. | If Assisted main task/subagent produces the same recoverable trace with less overhead, keep it Assisted. |
| **F2 Planner-independent review** | A reviewer that did not write the assignment receives a frozen packet, does not edit the result and issues a verdict that can force executor revision. | If the owner/coordinator silently repairs or overrides findings, review separation is cosmetic. |
| **F3 Abandon/resume** | Executor or reviewer is interrupted/abandoned; a replacement resumes from artifacts, detects stale inputs and preserves old provenance. | If hidden chat context or manual reconstruction is required, persistence has not become workflow state. |
| **F4 Shared non-Git safety** | Two roles work in parallel on disjoint outputs; overlapping mutation is blocked procedurally before write and serialized by the integrator; version mismatch fails closed. | If last-writer-wins or an overwritten role record occurs, C5 fails. |
| **F5 Control comparison** | C3/C5 produces a measurable result unavailable from C0/C1/C8: fewer lost blockers, recoverable reassignment, or a review-caused correction, at acceptable artifact/coordination cost. | If value is only more transcripts/files, Team remains an Assisted pattern. |
| **F6 Full-boundary migration** | Existing Assisted TRACE plus role records map into Full without duplicate truth, lost content or automatic promotion of Team review/evidence. | If Full files/gates must exist from task start, use Full instead. |

### C12 — H9 and stable-edition verdict

**H9:** Team can be a separate stable edition between Assisted and Full only if Codex tasks/threads provide verifiable separation of coordinator, executor and reviewer beyond ordinary subagents.

| H9 component | Challenge result | Evidence level |
|---|---|---|
| Codex tasks add a mechanism beyond ordinary subagents | **Yes, narrowly:** separately visible/user-owned persistence plus cross-task follow-up/read/wait was exercised. | **O: M3-E1–E5.** |
| That mechanism verifiably separates executor and reviewer | **Not established.** Only coordinator↔Researcher was exercised; permissions, identity and non-mutation are unproven. | **U.** |
| Semantic handoff can make separation inspectable | **Coherent but unexecuted.** Versioned role-owned records would expose assignments, questions, results and verdicts. | **P.** |
| Team adds enough beyond Assisted controls | **Not yet.** C0/C1 cover bounded multi-agent work; C8 covers review-only work; C2 collapses into delegated Assisted work. | **D + Challenge comparison.** |
| Team remains lighter than Full | **Possible only with reused Assisted TRACE and conditional role records.** Fixed A2 duplicates Assisted; C7 is already Full. | **P + repository boundary.** |

**H9 verdict: 🟡 CONDITIONAL.** The necessary platform distinction is partially supported, but the required coordinator/executor/reviewer separation is not demonstrated. H9 is neither supported as a stable-edition claim nor refuted as an architectural possibility.

**Stable-edition verdict: NOT CURRENTLY JUSTIFIED.** On the present evidence, Team should remain an **optional Assisted delegated-work/review pattern or explicitly experimental pilot**, not a stable edition. This preserves the owner-required no-Team control and avoids marketing persistence, one-user role play or three files as independent teamwork.

This verdict does not modify the immutable HL or approved plan. Any topology/wording change belongs to an exact, transparent, **UNAPPROVED** recommendation in RES and requires owner approval.

## Challenge Decisions

| # | Decision | Rationale |
|---|---|---|
| **C-D1** | Persistence and separate task visibility are necessary carrier evidence but do not justify an edition. | M3-E1–E5 do not establish authority, recovery, reviewer behavior or collision safety. |
| **C-D2** | Eliminate C2 as the minimum Team edition; call its verdict owner acceptance or execution-separated review. | Owner/coordinator/reviewer collapse makes planner-independent review misleading, and one assignment does not require a coordination edition. |
| **C-D3** | Replace mandatory A2 physical files with a logical role-owner spine that reuses Assisted TRACE; create a distinct record only for a distinct writer/authority boundary. | Prevents duplicate plans, traces, status and memory while preserving Full mapping. |
| **C-D4** | Keep C3/C5 only as a pilot candidate; keep C4 as Git adapter, C6 as independence ceiling, C7 eliminated and C8 as Assisted review overlay. | This is the smallest configuration classification consistent with current evidence. |
| **C-D5** | Bound single-writer safety to W2 collision avoidance, not enforced isolation; forbid concurrent shared-output mutation in the domain-agnostic core. | No ACL/permission/transaction enforcement was observed; worktrees are Git-only. |
| **C-D6** | Require explicit owner-led succession and immutable-version reassignment for abandoned/stale roles; do not add leases or automatic coordinator election. | Files preserve state, not authority; heavier failover would duplicate predecessor failure modes or approach Full. |
| **C-D7** | Mark H9 conditional and do not recommend a stable Team edition on current evidence. | The platform carrier exists, but semantic executor/reviewer separation and measurable advantage over C0/C1/C8 remain unexecuted. |

## OODA Stage Log

| Loop | Observe | Orient | Decide | Act |
|---|---|---|---|---|
| **1 — simpler-control attack** | Compared M3-E1–E5 with documented C0/C1 and the C8 assurance overlay. | Persistence is a real carrier difference, but C0/C1 still solve bounded delegation and C8 solves review-only needs with less machinery. | Eliminate persistence and agent/task count as sufficient edition criteria; demote C2. | Added configuration verdicts and C1–C4 stress tests. |
| **2 — ownership/recovery attack** | Cross-checked A2 with Assisted TRACE/memory, shared-checkout limits and predecessor lease/recovery findings. | Three mandatory files duplicate existing state; single-writer is procedural; stale/abandoned roles and coordinator loss need explicit authority transfer. | Reuse Assisted TRACE, scale logical records by distinct writers, bound safety to W2 and reject automatic leases/election. | Added C5–C9, recovery matrix and non-Git boundary. |
| **3 — ceiling/boundary attack** | Compared surviving C3/C5 with C6 independent authority and C7 Full-shadow; formulated falsifiable future tests. | Adding enforcement/gates would become Full, while current one-user evidence remains below independent Team assurance. | Keep C3/C5 experimental, mark H9 conditional and withhold stable-edition status. | Added C10–C12, F1–F6 and exact Challenge decisions. |

### Deep sufficiency verdict

- [x] External source used: Challenge preserved and applied the current official Codex primary-source set gathered for this iteration.
- [x] Briefing gap closed: every requested Team mechanism, role, lifecycle, artifact and no-Team comparison now has an adversarial disposition.
- [x] Pairwise incompatibility checked: C2/C3/C5 were attacked against C0/C1, C8, C6 and C7; surviving configurations are listed.
- [x] H9 tested: conditional, with stable-edition status not currently justified.
- [x] Counter-evidence sought: persistence insufficiency, TRACE duplication, misleading review, one-user naming, unenforced ownership, stale/abandoned roles, coordinator failure, non-Git collision and artifact ceremony were all tested.
- [x] Minimum two decisions recorded: C-D1–C-D7.
- [x] Metacognitive check: Challenge changed the Extract result rather than confirming it—C2 is demoted, fixed A2 is rejected, C8 strengthens, and C3/C5 are retained only as an experimental protocol rather than a stable edition.

## Checkpoint

| Found | Remaining for Synthesis |
|---|---|
| M3-E1–E5 prove a distinct persistent task carrier, not a Team edition. | Preserve the exact bounded evidence and non-claims in RES. |
| C0/C1 remain the default Assisted control; C8 covers review-only assurance; C2 is an Assisted handoff pattern. | State the stable-edition rejection without reopening the immutable owner decision or applying changes. |
| C3/C5 define a coherent pilot protocol but lack executed executor/reviewer, recovery, enforcement and measurable-control evidence. | Record F1–F6 as unresolved validation, not promised implementation. |
| Fixed A2 duplicates Assisted; the minimum is logical role-owner records that reuse TRACE and add records only at writer/authority boundaries. | Map the logical spine upward into HL/TS, ONB/RF and REVIEW without claiming Full gates ran. |
| Single-writer safety is W2 collision avoidance at best; same-output concurrency is outside the domain-agnostic core. | Separate confirmed HL, challenged HL, unresolved and exact UNAPPROVED owner-change recommendations. |
| H9 is conditional; Team does not currently deserve a stable edition. | Synthesize the owner-readable verdict and exact transparent HL diff proposal, unapplied. |

**Blocking questions:** none.

**Authorization request:** proceed to Synthesis only. No further experiment is requested. Create only `RES.md`, preserve the immutable HL/plan and add the required iteration-completion marker there only.

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Pairwise incompatibility checked and surviving configurations listed?
- [x] Hypothesis and counter-evidence tested?
- [x] Minimum two Challenge decisions recorded?

Stage complete: YES
Coordinator record: Challenge accepted on 2026-08-08; RES synthesis authorized.
