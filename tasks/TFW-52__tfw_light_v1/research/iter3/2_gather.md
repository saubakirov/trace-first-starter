# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW-52](../../HL-TFW-52__tfw_light_v1.md)
> Goal: Determine whether Team has a stable, independently useful working mechanism between Assisted and Full, while preserving the simpler Assisted-plus-subagents answer if H9 fails.

## Source and Evidence Discipline

The official Codex manual was refreshed through the OpenAI `openai-docs` helper on 2026-08-08. The helper reported that the cached manual was current and provided the source-page map used below. Official pages are treated as documented product support; current-session tool contracts and read-only commands are treated as local/app observations; neither is silently promoted into an executed end-to-end guarantee.

### Official OpenAI/Codex primary sources

| ID | Source | Material used |
|---|---|---|
| O1 | [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) | Subagent terminology, visibility, orchestration, permission inheritance, custom agents, parallel-write warning |
| O2 | [Projects and chats](https://learn.chatgpt.com/docs/projects) | Separate chat transcripts, shared project files/instructions, local-project root behavior, saved-chat resume |
| O3 | [Long-running work](https://learn.chatgpt.com/docs/long-running-work) | Per-chat context/goals, parallel-chat guidance, avoid concurrent writes, use worktrees for separate checkouts |
| O4 | [Worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees) | Git-only checkout isolation, per-chat managed worktrees, Local↔Worktree handoff, persistence/snapshot and branch limits |
| O5 | [Codex App Server](https://learn.chatgpt.com/docs/app-server) | Thread/turn primitives; start, resume, fork, read, list, archive, steer, interrupt, runtime status, approvals |
| O6 | [Code review](https://learn.chatgpt.com/docs/code-review) | Dedicated reviewer, no-change review, optional detached review chat, Git-only built-in review surface |
| O7 | [Remote connections](https://learn.chatgpt.com/docs/remote-connections) | Continue and steer chats across devices; host supplies files, credentials and permissions; host/worktree handoff |
| O8 | [Agent approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security) | Sandbox/approval separation and per-surface runtime boundaries |

### Read-only local/app observations

| ID | Observation | Boundary |
|---|---|---|
| L1 | The current collaboration surface exposes coordinator-controlled `spawn_agent`, `send_message`, `followup_task`, `wait_agent`, `interrupt_agent`, and `list_agents`. Spawn can fork all, none, or a bounded number of recent turns. All agents in the current tree share the same directory and immediately see each other's file edits; the current concurrency cap is four including the root. | Contract visible in this session; no child was created because the owner prohibited it. Product docs call the adjacent feature “subagents,” not “collaboration agents.” |
| L2 | The current app exposes user-owned task/thread operations: create, fork, list, read, send a follow-up, wait for up to eight, move/handoff another thread, pin, archive, and rename. Project task creation defaults to a worktree for a Git project unless Local is explicitly selected; creation is asynchronous. | Callable interface observed, but no task/thread was created, messaged, waited on, or handed off in Gather. This interface is stronger than the public Projects page and must not be presented as executed behavior. |
| L3 | `list_agents` returned only `/root` in `running` state. | Confirms no hidden Gather experiment or child-agent evidence; it does not test spawn behavior. |
| L4 | The repository is the primary local checkout at `D:/projects/research/steps-framework`, on `master`, with no additional Git worktree listed. | Current checkout only. It does not prove how a newly created app worktree would materialize this dirty state. |
| L5 | The current task directory is untracked as a whole and `README.md` is modified. A default-branch worktree would therefore not necessarily contain the live TFW-52 research unless creation explicitly starts from `working-tree` state or the state is otherwise transferred. | Direct current-checkout evidence of a stale/missing-context risk. The app contract offers `startingState: working-tree`, but this path was not executed. |
| L6 | The installed Codex app executable resolves under Windows package version `26.727.6591.0`, but direct `codex --version`/`codex features list` execution returned Access denied. | App package location is observable; CLI feature output is unavailable in this environment and is not inferred. |

## Dimensions

The following factors are independently selectable. Alternatives are deliberately left open for Extract and Challenge.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|---|---|---|---|---|
| **D1 Coordination unit** | One chat, one agent | Main chat + ordinary subagents | Coordinator-controlled collaboration-agent tree | Separate user-owned tasks/threads or independent sessions |
| **D2 Human authority** | Owner directs every worker | Owner delegates coordination to one coordinator | Shared/peer coordination | External manager/process controls assignment |
| **D3 Session ownership** | Parent-owned ephemeral child | Parent-owned inspectable agent thread | User-owned persistent app task/thread | Separately owned human/account/host session |
| **D4 Context transfer** | Full/shared conversation | Forked completed history | Explicit prompt + project files/instructions | Frozen artifact packet only |
| **D5 Execution location** | Same local checkout | Disjoint paths in same checkout | Per-task Git worktree | Separate repository/host/non-Git workspace |
| **D6 Communication** | Parent aggregates results | Direct agent-tree message/follow-up | Cross-thread read/send/wait | Artifact queue or human relay |
| **D7 Blocking-question route** | Worker asks owner directly | Worker → coordinator → owner if necessary | App needs-attention signal + coordinator relay | Durable file inbox/decision record |
| **D8 Permission boundary** | One shared permission mode | Child inherits parent, optional read-only custom agent | Separate thread runtime/defaults | Independent identity/credentials and repository policy |
| **D9 Artifact ownership** | Everyone edits one trace | Shared file with role sections | One role-owned artifact per stage | Immutable inputs/receipts plus integrator-owned aggregate |
| **D10 Review separation** | Same-turn self-review | Review subagent in parent tree | Detached/separate reviewer task | Independent human/agent identity with immutable review input |
| **D11 Persistence/resume** | Chat transcript only | Parent + child thread tree | Saved user-owned task/thread + project files | Filesystem state plus independent system of record |
| **D12 Integration authority** | Last writer wins | Parent coordinator applies child results | One named integrator merges worktrees/outputs | Pull request/change-control owner |
| **D13 Role cardinality** | Owner only | Owner/coordinator + executor | Owner/coordinator + executor + reviewer | Owner + coordinator + executor + reviewer |
| **D14 Upward artifact mapping** | One trace expands manually | Two combined role records | Three role-owned Team artifacts | Full HL/TS/ONB/RF/REVIEW already present |

## Findings

### G1 — Product terms do not identify four independent platform primitives

The current official manual documents **subagent workflows**, **subagents**, and **agent threads**. It does not document “collaboration agents” as a distinct end-user Codex product concept. The current session does expose a collaboration-oriented agent-control API, but its operations map to orchestration of spawned descendant agents: spawn, steer/message, wait, interrupt, inspect, and close. Therefore the evidence set must distinguish four *working mechanisms*, not assume four product brands:

1. **Ordinary subagents** — documented child agents whose results return to the main thread.
2. **Coordinator-controlled collaboration agents** — the current session's explicit child-tree control contract; likely an orchestration surface over the same child-agent class, with observable context-fork and shared-filesystem semantics.
3. **Separate user-owned app tasks/threads** — first-class saved chats/tasks in the sidebar, each with its own transcript and optional worktree.
4. **Truly independent human/agent sessions** — separate people, credentials, hosts, or organizational authority; not established merely by creating another Codex thread.

**G-D1:** Treat “collaboration agents” as the current orchestration contract around child agents, not as official evidence of a new independent-agent class. Any Team claim must name the observable property it needs—ownership, persistence, permissions, checkout isolation, or review independence.

### G2 — Four evidence lanes by capability

| Capability | Documented support | Observed local/app behavior | Unavailable or unproven | Candidate TFW behavior to test later |
|---|---|---|---|---|
| **Ordinary subagents** | O1: main agent spawns specialized children, routes follow-ups, waits, closes threads, and consolidates results; child threads are inspectable. | L1 exposes equivalent coordinator controls; current tree has only root. | No Gather spawn; no evidence that child ownership survives the parent session as a user-owned task; no independent human authority. | Use for bounded parallel exploration/execution inside one owner's task; never claim cross-session Team separation from spawn alone. |
| **Collaboration-agent tree** | No exact public term found; closest documented concept is O1 subagent orchestration. | L1 exposes named child tasks, bounded history fork, messages/follow-ups, waiting, interruption, nested spawning, and shared filesystem. | Persistence across app restart, sidebar ownership, independent permissions/approvals, and durable needs-attention routing were not executed. | Treat as coordinator-private execution machinery; artifacts remain authoritative if the tree disappears. |
| **Separate app tasks/threads** | O2/O3/O5: separate transcripts, saved threads, start/resume/fork/read/list/archive/status; related chats can share project files/instructions. | L2 exposes create/read/send/wait/handoff and management of user-owned tasks across local/remote/signed-in history. | No live create/read/send/wait experiment; no proof that every current tool is a stable public contract; per-thread permission defaults not exposed by create schema. | Candidate Team lane only if task ownership, status and handoff are durable outside coordinator memory and survive stale/missing chat context. |
| **Independent sessions/people** | O7 supports the same signed-in user controlling hosts/chats remotely; it does not establish multi-person role authority. | No separate human/account/host session observed. | Cross-user task assignment, ACLs, identity proof, non-repudiation, and organizational reviewer independence are unavailable in current evidence. | Require external identity/repository policy and artifact ownership; do not market a separate thread as an independent person. |
| **Shared checkout** | O1/O3 warn against parallel write-heavy work and two chats changing the same files. | L1 children share this exact directory; edits are immediately visible. | No race was induced. File visibility is not serialization. | Only disjoint paths or a single writer per mutable artifact; coordinator integrates. |
| **Worktree checkout** | O4: Git-only separate checkout per chat, same Git metadata, detached HEAD by default, same branch cannot be active in two worktrees. | L2 creation contract defaults Git project tasks to worktrees and can start from default branch, an existing branch, or working-tree state. | No app worktree created; non-Git domains cannot use the mechanism; dirty/untracked-state fidelity untested. | Optional implementation isolation for Git-backed work; never a Team edition invariant. |
| **Thread messaging/waiting** | O5 provides turn start/steer, status and event streams for app-server clients; O3 says follow-ups steer the same chat. | L2 can send follow-up prompts to another thread and wait for completion/needs-attention with cursors; `wait_threads` ignores commentary as a wake event. | No delivery, acknowledgement, ordering, retry, or lost-message test; public docs do not describe a general peer-to-peer message bus. | Notifications accelerate coordination; durable questions, decisions and status remain in role-owned files. |
| **Handoff** | O4/O7: Handoff moves the same chat and Git state between Local/Worktree or matching hosts, interrupting a running response when needed. | L2 `handoff_thread` moves another thread and associated Git state; caller cannot move itself; cloud handoff unsupported. | No handoff executed; ignored files and dirty-state behavior remain untested here. | Reserve “Codex Handoff” for execution-location movement. TFW role handoff is an artifact packet + ownership transfer, optionally followed by a Codex move. |
| **Context inheritance** | O1: child is configured from parent/custom-agent settings; O2: chats share project files/instructions but keep separate transcripts; O5: fork copies stored history. | L1 spawn can fork all/none/N recent turns; L2 fork copies completed history only; create starts from a prompt plus project/environment. | Exact hidden context and stale-instruction refresh are not inspectable; active unfinished fork history is explicitly absent. | Every role receives a bounded manifest identifying authoritative artifact versions; transcript inheritance is convenience, not state. |
| **Permissions/approvals** | O1: subagents inherit parent sandbox/permission mode and live overrides; unavailable interactive approval causes child action to fail. O8: sandbox and approvals remain separate controls. | Current root is `danger-full-access`/`never`; L2 create schema has no permission argument. | Separate-task effective defaults and whether needs-attention reliably routes every approval were not tested. | Executor write scope and reviewer read-only scope must be explicit and externally checkable; inherited permission is not role independence. |
| **Visibility/persistence** | O1: child activity/status/results visible; O2: saved chats resume; O4: managed worktree chat returns to the same worktree and deleted worktrees can restore from snapshot. | L2 can list/read/pin/archive tasks; L1 only lists the live descendant tree. | Long-term child-agent persistence and cross-account visibility are not proven. | Team state cannot depend on an Active/Done panel; files index task/thread IDs and current role-owned status. |
| **Review** | O6: `/review` uses a dedicated reviewer, does not change the working tree, and can run in a detached separate review chat; built-in scope is Git/code. | App-server exposes `review/start`; no review was launched. | Same model/account can still share bias; non-code Team work lacks a built-in diff reviewer; detached does not authenticate independence. | Separate review task with frozen brief/result, no execution write authority, explicit verdict; independent human only when risk demands it. |

### G3 — Minimum comparison of working mechanisms

| Mechanism | Coordinator control | Transcript/context | Filesystem isolation | Permission independence | User visibility/persistence | What it adds beyond Assisted | Primary counter-evidence |
|---|---|---|---|---|---|---|---|
| **M0 — Assisted + one agent** | Owner steers one chat | One full transcript | One checkout | N/A | Saved chat + Assisted traces | No Team mechanism; lowest overhead | Cannot parallelize or obtain even cognitive reviewer separation |
| **M1 — One-session ordinary subagents** | Main agent spawns, steers, waits and summarizes | Child agent thread; parent-controlled; project context/config inherited | Usually the same checkout unless product creates another environment | Inherits parent mode; custom agent may narrow sandbox | Child activity inspectable, but parent remains owner of workflow | Parallelism, context de-noising, specialist prompts, fresh child context | O1 explicitly warns about parallel writes; parent still selects input, receives summary and controls review; no independent ownership |
| **M2 — Coordinator-controlled collaboration agents** | Explicit tree API: bounded history fork, message/follow-up, wait, interrupt, nested spawn | Parent selects fork depth; child state lives in one runtime tree | L1 says all agents share the same directory | Same session/runtime lineage; independence unproven | Live tree inspection; durable user ownership unproven | More deterministic orchestration than natural-language delegation | This may be an implementation surface of M1, not a distinct working mechanism; shared checkout and parent authority remain |
| **M3 — Separate app tasks/threads** | Owner creates; current coordinator tools can read/send/wait after creation | Separate transcript; project files/instructions shared; new, forked, or explicitly briefed start | Local shared checkout or optional Git worktree | Separate runtime is plausible, but create contract does not select permissions | First-class sidebar task, resume/pin/archive, independent goal/status | Durable separately inspectable work lanes, optional checkout isolation, background/needs-attention coordination | Same user/account is not independent reviewer; file races remain in Local; app messaging is not artifact authority; creation adds user-visible ceremony |
| **M4 — Truly independent human/agent sessions** | Explicit human/process assignment | Separate history and potentially separate project understanding | Separate worktree/repo/host or shared folder | Separate credentials/policies possible | Independent system/account records | Real organizational separation, independent approvals and reviewer authority | Codex alone does not provide a verified shared task bus or identity proof; artifact/repository governance becomes mandatory and can approach Full |

The **no-Team control** is M0/M1: Assisted supplies task-local trace, status, identity and memory; one owner uses subagents for bounded parallel work and optionally a review-specialist child. This control already covers many “multiple agents” use cases. Team must therefore prove value in M3/M4 properties, not in agent count.

### G4 — Context inheritance is a selectable risk, not a binary feature

| Start mechanism | What is carried | What is not guaranteed | Stale-context failure |
|---|---|---|---|
| **Ordinary subagent** | Parent/custom-agent configuration; selected task prompt; product-managed agent thread | Independent authority; non-inherited secrets/tools; persistence beyond parent workflow | Parent may provide biased or incomplete task framing; child may edit same files from stale assumptions |
| **Current collaboration spawn** | Explicitly all, none, or N recent turns plus shared files and developer/system context | User-owned persistence; fresh project reload after later file change | `fork_turns: all` carries bias; `none` loses decisions unless artifactized |
| **App thread fork** | Completed stored history; same directory or worktree | Running turn and unfinished response are not copied | Fork during active work begins before the latest reasoning/result |
| **New app task** | Initial prompt, chosen project, discovered project instructions/files, selected starting Git state | Source chat transcript; current dirty state unless `working-tree` is selected; identical effective permissions | Default branch can omit the current untracked TFW-52 task entirely (L5) |
| **Independent session** | Only what shared project sources and handoff packet expose | Any hidden chat decision or implicit owner preference | Maximum stale-context risk unless the artifact packet names versions/digests and unresolved decisions |

**G-D2:** Context freshness and cognitive independence trade off. Team cannot define “fresh thread” as sufficient; it needs a versioned handoff packet that makes missing context observable while avoiding wholesale transcript inheritance.

### G5 — Messaging, waiting, and Handoff have narrower semantics than Team communication

The app's current cross-thread tools are valuable coordination accelerators:

- `send_message_to_thread` starts a follow-up turn in a named thread;
- `read_thread` reads recent status and turn summaries;
- `wait_threads` wakes on completion or needs-attention for up to eight targets, but commentary does not wake it;
- `fork_thread` creates a new transcript from completed history;
- `handoff_thread` moves an existing thread and Git state between execution locations/hosts.

They do **not** by themselves provide:

- a transactional assignment acceptance;
- a durable blocking-question inbox with ownership and acknowledgement;
- a decision record that survives thread deletion or tooling changes;
- peer-to-peer authority (the coordinator can inspect and steer every target it can address);
- semantic ownership transfer of requirements/results;
- proof that a reviewer did not receive implementation-side persuasion.

A candidate Team communication model must therefore use two layers:

1. **Fast lane:** app send/read/wait/needs-attention for notification and steering.
2. **Authority lane:** role-owned artifacts for assignment, questions, decisions, result handoff, verdict and status.

Codex Handoff may move the execution environment after an authority-lane decision, but it is not the decision itself.

### G6 — Worktrees solve checkout collision, not collaboration or domain independence

O4 gives each worktree its own checkout and one chat an associated background environment. This materially reduces concurrent file interference in Git repositories. It also creates constraints:

- worktrees are unavailable for non-Git projects;
- a branch is owned by one worktree at a time;
- merging/integration remains a separate act;
- ignored files move only through `.worktreeinclude` rules, with local-app-specific behavior;
- permanent worktrees can host multiple chats and therefore reintroduce same-checkout races;
- a new worktree's start point may exclude dirty/untracked live context unless explicitly transferred;
- a worktree does not create different permissions, identity, review authority, or communication reliability.

The TFW-52 edition promise is domain-agnostic. Team therefore needs an ownership protocol that works in a shared non-Git folder; worktrees can be an adapter-level enhancement for Git-backed work.

### G7 — Permissions and approvals expose a false-independence trap

O1 says child agents inherit the parent's current permission mode and live overrides. A read-only custom agent can narrow a child, but the parent controls its creation and framing. This is useful least privilege, not independent authority.

Separate app tasks are stronger process boundaries, but the current `create_thread` call contract does not accept explicit sandbox or approval settings. The new task uses the environment and effective settings available on its host/project; exact defaults and needs-attention behavior require execution evidence. A task started by the same user can also be re-steered by that user or coordinator.

For Team, three concepts must remain separate:

| Concept | Minimum observable property |
|---|---|
| **Execution isolation** | Worker cannot accidentally mutate another role's owned artifact/location. |
| **Review restriction** | Reviewer does not write the execution result and receives a frozen review input. |
| **Authority independence** | Reviewer/owner can reject despite coordinator preference, supported by a distinct human/account/policy when required. |

Only the first two are plausibly obtainable inside one user's Codex app without external identity controls. A stable Team edition must not claim the third universally.

### G8 — Visibility and persistence form the strongest candidate distinction

Ordinary subagent threads are visible and inspectable, but they remain descendants of a main orchestration flow whose job is to consolidate their outputs. Current collaboration agents are even more clearly parent-owned: their state is a live root/child tree.

Separate project chats/tasks have first-class persistence: each keeps its own transcript and goal, can be resumed, pinned or archived, and can have an associated worktree that is restored from a snapshot if the managed directory was removed. This is the first mechanism in the evidence set that can plausibly support a separately resumable executor or reviewer lane.

However, durable transcript ownership is still weaker than durable project state. O2 explicitly recommends checked-in/project documentation for future chats; O3 warns that parallel chats must not share mutable sources. The Team mechanism, if any, is therefore not “another chat.” It is **separately resumable role work plus explicit artifact ownership and routing**.

### G9 — Role value and collapse for two to three people

| Role | Irreducible responsibility | May collapse with | Must not collapse with when the claim is made |
|---|---|---|---|
| **Owner** | Defines desired outcome, risk/acceptance authority, resolves decisions outside delegated scope | Coordinator for a small team; reviewer for final acceptance | Executor if an independent acceptance/review claim is required |
| **Coordinator** | Converts outcome into a Working Backwards brief, assignments, owned paths/artifacts and dependencies; routes blockers; integrates status/results | Owner; executor for one bounded work item; reviewer if coordinator did not execute and review scope is frozen | All roles simultaneously if Team is claimed as role-separated |
| **Executor** | Accepts/clarifies assignment, produces result and trace, reports blockers/deviations/verification | Coordinator for low-risk single-lane work (which may collapse back to Assisted) | Reviewer of the same result when independent verification is claimed |
| **Reviewer** | Reads frozen intent and result, verifies rather than repairs, returns verdict/findings without editing executor output | Owner; coordinator when neither executed the reviewed result | Executor of the reviewed result |

Candidate small-team shapes remain open:

| Shape | People/agent lanes | Potential value | Ceremony risk |
|---|---|---|---|
| **R0 no-Team** | Owner/coordinator/executor in one chat; optional review subagent | Lowest overhead; adequate for reversible work | Review is cognitive assistance, not independent gate |
| **R1 two-party** | Owner+coordinator+reviewer; separate executor task | Executor result is independently accepted by another actor | Coordinator's planning bias remains in review; role titles may overstate independence |
| **R2 three-lane** | Owner+coordinator; executor task; reviewer task | Separate execution and review transcripts/artifacts | Owner/coordinator distinction may add no value; app coordination ceremony grows |
| **R3 four-role** | Owner, coordinator, executor, reviewer all distinct | Maximum authority separation | Likely Full-scale ceremony for 2–3-person work; unnecessary unless risk/organization demands it |

Preliminary role floor: **owner authority is always present but need not be a separate working lane; coordinator is a function, not necessarily a person; executor is required only when work is delegated; reviewer is required only when the edition promises independent verification.** Extract must test whether a Team edition can remain stable with R1/R2 rather than requiring R3.

### G10 — Lifecycle and communication model to carry into Extract

| Lifecycle moment | Owner | Coordinator | Executor | Reviewer | Durable authority |
|---|---|---|---|---|---|
| **Intake** | States outcome, risk and decision authority | Confirms desired result and boundaries | — | — | Coordinator-owned brief draft |
| **Working Backwards plan** | Approves only material choices | Defines criteria, assignments, dependencies and owned artifacts | Can challenge feasibility before acceptance | Can challenge reviewability before execution when assigned early | Approved/frozen brief revision |
| **Assignment** | Authorizes new user-owned task if required | Creates or requests lane; sends manifest with artifact/version IDs | Explicitly accepts or raises blocker | Receives future review scope, not implementation transcript | Assignment/acceptance entry |
| **Execution** | Not continuously involved | Monitors status/needs-attention; does not rewrite executor trace | Writes only executor-owned artifact/result/path | No execution participation | Executor-owned trace/result |
| **Blocking question** | Answers only scope/risk/acceptance choices | Triages, answers within authority, escalates bounded question | Records question, impact and safe stopping point | — | Question + decision record; app message is notification |
| **Status** | Reads concise outcome state | Owns aggregate status | Owns lane status | Owns review status | Derived aggregate from role-owned states, not one shared free-edit table |
| **Handoff to review** | — | Freezes review input/version and routes it | Marks result ready; no more silent mutation | Acknowledges exact brief/result versions | Immutable/frozen handoff receipt |
| **Review** | May decide exception | Receives verdict; does not pressure repair inside review | Responds only after verdict | Verifies and issues verdict without editing result | Reviewer-owned verdict/findings |
| **Revision** | Resolves scope change | Issues new brief revision or returns bounded findings | Produces new result revision | Reviews new revision, preserving previous verdict | Version-linked cycle, no overwrite |
| **Completion** | Accepts outcome when required | Integrates status/artifact links and closes coordination lane | Executor lane closes | Reviewer lane closes after verdict | Completion record points to all role artifacts |
| **Interruption/resume** | — | Reassigns only from durable state | Resumes from own artifact + brief version | Resumes from frozen review packet | Thread ID is a locator; files are state |
| **Stale context** | Clarifies only if decision changed | Detects brief/version mismatch before steering | Stops before mutation on mismatch | Rejects review packet with mismatched versions | Fail-closed version/manifest check |
| **Concurrent edits** | — | Allocates disjoint paths/worktrees and one integrator | Does not edit coordinator/reviewer artifacts | Read-only on frozen input | Single writer per mutable artifact; optional Git worktree |

### G11 — Minimal Team artifact-spine candidates

The artifact question must stay open until Extract, but Gather identifies four realistic configurations:

| Spine | Contents | Full mapping | Risk |
|---|---|---|---|
| **A0 Assisted trace only** | One task `TRACE.md` with owner, plan, work, review notes | Manual split later | Multi-writer ambiguity; no independently inspectable handoff or verdict |
| **A1 Two artifacts** | Coordinator `BRIEF.md`; combined executor/reviewer `OUTCOME.md` | BRIEF → HL/TS; OUTCOME → ONB/RF/REVIEW | Executor/reviewer ownership collision; reviewer independence mostly cosmetic |
| **A2 Three role-owned artifacts** | `BRIEF.md`, `EXECUTION.md`, `REVIEW.md` | BRIEF → HL+TS; EXECUTION acceptance/questions → ONB and result/verification → RF; REVIEW → REVIEW | Combined mappings need explicit section roles; could be the minimum without Full filenames/gates |
| **A3 Full-shaped artifacts** | HL, TS, ONB, RF, REVIEW (+ evidence) | Already Full | Team collapses into Full ceremony and violates the edition boundary |

Assisted memory/candidate behavior remains a boundary condition, not a new Team file. A candidate Team artifact should link to Assisted task trace/knowledge machinery rather than duplicate the knowledge loop.

### G12 — Active falsification and the no-Team control

| Counter-case | What it attacks | Current evidence |
|---|---|---|
| **Subagents are enough** | “Multiple agents” justifies Team | O1 already supplies parallel specialists, fresh child contexts, inspection, steering and consolidated results. For one accountable owner and bounded work, Team adds no mechanism. |
| **Collaboration-agent API is only subagent orchestration** | A new API noun justifies a new edition | L1 retains parent authority, shared checkout and one runtime tree. It improves control, not independence. |
| **Separate threads cannot coordinate reliably** | Persistence automatically implies workflow | L2 messaging/waiting is unexecuted and not a transactional bus; O2 relies on project files/instructions; artifact routing remains necessary. |
| **Reviewer independence is fake** | Separate reviewer task guarantees verification | O6's detached review is a separate chat but normally the same user/product/model; role framing and hidden shared context can remain. Independence needs frozen input, no result writes, and sometimes a different person/policy. |
| **Shared-checkout races** | Parallel lanes are safe by default | O1/O3 explicitly warn against write-heavy parallelism on the same files; L1 shares the current directory. Worktrees are Git-only. |
| **Team becomes Full** | More roles/artifacts are always better | A3 duplicates the full lifecycle. If Team requires all Full artifacts/gates, it is not a stable intermediate edition. |
| **Coordinator adds no value** | Every delegated task needs a named coordinator | One owner with one executor and one outcome can brief directly. Coordinator becomes distinct only when assignments/dependencies/blockers/integration exceed owner-direct handling. |
| **Reviewer adds no measurable value** | Every Team task needs review | Low-risk reversible work may need owner acceptance only. Reviewer value must appear as defects/decision evidence or a required assurance boundary, not a file count. |
| **Worktree equals independence** | Checkout isolation creates role separation | O4 isolates files, but the same user can steer both chats and permissions may remain equivalent; integration bias/authority remain. |
| **Persistent task equals independent person** | User-owned thread proves human-team collaboration | O2/O7 document same-account/project/host continuation, not multi-person identity or non-repudiation. |

The falsification threshold for H9 is now sharper: if M3 cannot produce a durable, separately resumable, role-owned handoff/review lane with observable version/ownership boundaries beyond M1/M2, preserve Assisted plus subagents and reject Team as an edition.

### G13 — Repository precedents are useful but not proof

TFW-45's frozen multi-agent research already models a coordinator that owns Briefing/synthesis and subagents that own bounded stage work. That is evidence for the **no-Team control**, because the proposed swarm remains one coordinator-owned workflow; it does not establish user-owned sessions or independent review. TFW-45 itself records that its quality advantage remained empirically unvalidated and is frozen in project knowledge (`knowledge/process.md` F24).

TFW-8 establishes why execution and review should not be one uninterrupted workflow: executor agents continued into self-review when review instructions were visible. Its remedy—new session + reviewer role lock—creates cognitive and structural separation. It does not prove independent human authority, and the current official O6 detached-review option shows the same distinction: separate chat is useful, but same-account detached review is not automatically organizational independence.

Iteration 1 and iteration 2 remain boundary conditions:

- K1–K6 require portable meaning, explicit authority/version, conflict behavior and receipts for upward migration.
- Assisted S1/S0/C3 findings distinguish availability from executed behavior, next-start from calendar freshness, recovery from locking, and attribution from authentication.
- Team must inherit these honesty boundaries; another thread cannot upgrade declared attribution into authentication or a worktree into strict role authority.

### G14 — Current checkout exposes a concrete stale-context hazard

The current TFW-52 folder is untracked, and the master checkout contains other owner changes. The app task-creation contract defaults Git projects to a worktree and uses the project's default branch unless `startingState: working-tree` or an existing branch is chosen. A new default worktree in this exact repository could therefore start without the approved HL and all three research iterations.

This is not a theoretical edge case: it is the current project state. It implies that any Team assignment manifest must include both:

1. **conversation/artifact version authority** — exact required paths and digests/revisions; and
2. **execution starting-state authority** — Local, working-tree snapshot, branch/commit, or non-Git shared root.

A thread ID alone does not prove that the executor or reviewer can see the intended artifacts.

### G15 — Gather decisions and H9 status

| # | Gather decision | Rationale |
|---|---|---|
| **G-D1** | “Collaboration agents” are not treated as a documented independent product class; they remain a current-session orchestration surface over parent-owned child agents until contrary evidence exists. | Prevents naming from creating a false Team distinction. |
| **G-D2** | Fresh context must be paired with explicit artifact/starting-state version authority. | New/forked/worktree sessions can omit active turns, dirty files, untracked artifacts or later instruction changes. |
| **G-D3** | Checkout isolation, session persistence, permission restriction and authority independence are four separate properties. | Worktrees, separate chats and read-only agents each solve only part of the problem. |
| **G-D4** | Codex send/read/wait and Handoff are fast-lane controls; role-owned files remain the authority lane. | Current app tools are useful but not transactional task governance, and Codex Handoff is an environment move. |
| **G-D5** | Preserve M0/M1 Assisted-plus-subagents as the active falsification control through Extract and Challenge. | Documented subagents already cover most single-owner multi-agent work. Team must demonstrate a durable role/session mechanism beyond them. |
| **G-D6** | A2 (three role-owned artifacts) is the highest-complexity Team spine allowed to advance provisionally; A3 is retained only as the “collapses into Full” counter-configuration. | Prevents Gather from silently making Team a renamed Full lifecycle. |

**Preliminary H9 observation:** not supported yet. Official Codex and the current app expose ingredients for a distinct mechanism—persistent separate tasks, independent transcripts, optional worktrees, cross-thread follow-up/wait, detached review—but no executed evidence yet shows that they jointly deliver verifiable role separation beyond Assisted plus subagents. H9 remains live only as a conditional configuration to test in Extract/Challenge.

## OODA Stage Log

| Loop | Observe | Orient | Decide | Act |
|---|---|---|---|---|
| **1 — official product model** | Refreshed the current Codex manual; read O1–O8. | Subagents, chats, worktrees, reviews and handoff are separate capabilities. Public docs do not name “collaboration agents” as a separate class or promise multi-human Team coordination. | A capability bundle, not an agent count, must define Team. | Created D1–D14 and the documented-support lane. |
| **2 — current local/app contract** | Inspected current agent and app task/thread tool contracts; ran only `list_agents` and read-only Git/app checks. | Current app orchestration is richer than public Projects guidance, but no end-to-end task was authorized. The live dirty/untracked checkout makes starting-state drift concrete. | Treat schemas as available interface, not executed behavior; record the exact missing live test. | Added L1–L6, context/communication tables and experiment candidate. |
| **3 — repository precedent and counter-evidence** | Read TFW-45 iter1/iter2 RES and TFW-8 HL; cross-checked predecessor iteration 1/2 boundaries. | Existing TFW subagent work supports the no-Team control, while Reviewer role separation shows value of a fresh role but not authenticated independence. | Keep A2/M3 conditional; eliminate no option until pairwise Extract, but do not let A3 define Team. | Added role-collapse, lifecycle, artifact-spine and falsification matrices. |

### Deep sufficiency verdict

- [x] External source used: current official OpenAI/Codex manual pages O1–O8.
- [x] Briefing gap closed: mechanisms, context, permissions, visibility, persistence, communication, lifecycle, roles and artifact candidates are mapped.
- [x] H9 tested: preliminary verdict is conditional/unproven; M0/M1 remains live.
- [x] Counter-evidence sought: ten explicit no-Team/failure cases recorded.
- [x] Metacognitive check: Gather discovered new distinctions rather than merely confirming the HL—especially Handoff ≠ role handoff, collaboration-agent API ≈ parent-owned subagent orchestration, worktree ≠ authority, and current untracked state can make a new default worktree miss the task entirely.

## Checkpoint

| Found | Remaining |
|---|---|
| Public Codex supports inspectable subagents, separate saved chats, thread lifecycle APIs, detached review, worktrees and execution-location Handoff. | Determine which combinations survive pairwise consistency checks without relying on undocumented or unexecuted behavior. |
| Current app contracts add user-owned task creation plus cross-thread read/send/wait and handoff. | Execute or explicitly defer an end-to-end user-owned-thread test for working-tree context, follow-up, needs-attention/wait and resume. |
| Ordinary/collaboration subagents remain parent-owned and share the local checkout in this session. | Determine whether separate app tasks provide enough durable role ownership to justify Team or merely add ceremony. |
| Worktrees isolate Git checkouts but cannot be a domain-agnostic invariant. | Define the shared-folder/non-Git ownership configuration and compare it with Git worktrees. |
| Owner/coordinator can collapse; executor/reviewer cannot collapse when independent verification is claimed. | Pairwise-test R0–R3 and specify when reviewer independence is genuine, bounded, or fake. |
| A2 (`BRIEF.md`, `EXECUTION.md`, `REVIEW.md`) is a plausible maximum-minimum spine; A3 is already Full-shaped. | Test A0–A3 mappings and whether A2 preserves K1–K6 without duplicate bureaucracy. |

**Bounded live experiment proposed for explicit coordinator authorization (not executed):** create exactly one user-owned Codex project task in a worktree with `startingState: working-tree`, give it a read-only prompt to (a) report whether the approved TFW-52 HL and iter3 Gather are present, (b) return one deliberately specified blocking question without writing files, and (c) stop. From this coordinator session, use `read_thread`, `send_message_to_thread`, and `wait_threads` once each to test visibility, follow-up delivery and needs-attention/completion routing. Do not test Git mutation, Handoff, archive, permissions changes, subagents, external writes or additional threads. The experiment would establish actual M3 context/routing behavior; without it, Extract must keep those properties **unproven**.

**Checkpoint questions:**

1. Authorize the single bounded M3 live experiment above for Extract, or direct Extract to keep all end-to-end task/thread properties unproven?
2. No other blocking question.

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?
- [x] Hypothesis tested and counter-evidence sought?
- [x] Minimum two Gather decisions recorded?

Stage complete: YES
Coordinator record: Gather accepted on 2026-08-08; Extract authorized; optional extra M3 task experiment declined in favor of bounded evidence from this Researcher task.
