# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW-52](../../HL-TFW-52__tfw_light_v1.md)
> Goal: Determine whether Team has a stable, independently useful working mechanism between Assisted and Full, while preserving the simpler Assisted-plus-subagents answer if H9 fails.

## Evidence Boundary for This Stage

The coordinator authorized this Iteration 3 task itself as bounded executed evidence for a subset of Gather mechanism M3. No additional task, thread, subagent, worktree, permission change, or external write was created in Extract.

| Evidence ID | Actually exercised in Iteration 3 | What it supports | What it does **not** support |
|---|---|---|---|
| **M3-E1** | The coordinator created this separate user-owned Researcher task from a different coordinator task. | A separate role task can be created and addressed from another app task. | Independent person/account, permissions, worktree or cross-user assignment. |
| **M3-E2** | This task persisted through Briefing, Gather and Extract turns; the coordinator repeatedly located it and continued it. | Separate transcript continuity and app-visible task persistence across multiple checkpoint turns. | Persistence across app restart, archival/restoration or host migration. |
| **M3-E3** | Coordinator follow-ups were delivered after both prior checkpoints, with precise authorization and scope changes. | Cross-task follow-up delivery can steer the role task. | Transactional message acknowledgement, ordering under concurrency or peer-to-peer bus semantics. |
| **M3-E4** | The coordinator states it exercised read/wait completion routing to review the checkpoint and return the next instruction. | A coordinator task can inspect/wait on a separate task and resume after completion. | Needs-attention routing, approval routing, failure recovery or more than one concurrent target. |
| **M3-E5** | Files written here were visible to the coordinator for full review before each follow-up; both tasks operated against the same local checkout. | Shared-checkout file visibility and artifact-mediated checkpoint review. | Write isolation, race prevention, worktree behavior or immutable snapshots. |

The current official OpenAI/Codex manual was refreshed again at Extract entry and remained current. The analysis continues to use the Gather official-source set: [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Projects and chats](https://learn.chatgpt.com/docs/projects), [Long-running work](https://learn.chatgpt.com/docs/long-running-work), [Worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees), [Codex App Server](https://learn.chatgpt.com/docs/app-server), [Code review](https://learn.chatgpt.com/docs/code-review), and [Remote connections](https://learn.chatgpt.com/docs/remote-connections).

## Configuration Space

The full D1–D14 cross-product is too large to enumerate. The table lists coherent configurations in which at least one dimension differs from the R0/M1 control. Dimension names match Gather exactly.

| Config | D1 Coordination unit | D2 Human authority | D3 Session ownership | D4 Context transfer | D5 Execution location | D6 Communication | D8 Permission boundary | D9 Artifact ownership | D10 Review separation | D11 Persistence/resume | D12 Integration authority | D13 Role cardinality | D14 Upward artifact mapping |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **C0 — Assisted control** | Main chat + ordinary subagents | Owner directs main agent | Parent-owned inspectable agent threads | Parent prompt + selected inherited context | Same local checkout | Parent aggregates child results | Children inherit parent mode | Assisted task trace; optional child notes | Self-review or review subagent | Parent chat/tree + Assisted trace | Main agent/owner | Owner/main agent; temporary specialists | One trace expands manually |
| **C1 — Explicit child tree** | Coordinator-controlled collaboration-agent tree | Owner delegates orchestration to coordinator | Parent-owned child tree | Explicit all/none/N turn fork + files | Same checkout with disjoint paths | Direct tree message/follow-up/wait | Same runtime lineage; optional narrowed child | Coordinator brief + child-local outputs | Reviewer child with fresh bounded context | Live tree + files; user-owned persistence unproven | Parent coordinator | Owner/coordinator + executor/reviewer children | Two or three role records assembled by parent |
| **C2 — Two-party persistent handoff** | Separate user-owned executor task; owner/coordinator also reviews | Owner and coordinator collapse | User-owned executor thread; coordinator task remains separate | Frozen `BRIEF.md` + explicit starting-state manifest | Shared checkout, disjoint role-owned files/paths | App read/send/wait fast lane + artifact authority lane | Separate runtime exists; independence unproven | `BRIEF.md`, `EXECUTION.md`, `REVIEW.md` owned by coordinator/executor/coordinator | Reviewer is separate from executor but not from planning | Saved coordinator + executor tasks; files are state | Owner/coordinator | Two actor lanes: owner/coordinator/reviewer + executor | A2 split maps to HL/TS, ONB/RF, REVIEW |
| **C3 — Three-lane persistent shared-root** | Separate coordinator, executor and reviewer app tasks | Owner collapses with coordinator | Three user-owned persistent threads | Frozen artifact packets only; no transcript inheritance required | Same shared checkout; one writer per role artifact and result path | Cross-thread read/send/wait + file questions/decisions | Separate-task settings unproven; reviewer instructed read-only | A2 three role-owned artifacts | Separate reviewer task receives frozen brief/result | Saved tasks + artifact state | Coordinator integrates; owner accepts | Three lanes: owner/coordinator, executor, reviewer | A2 additive mapping to Full |
| **C4 — Three-lane persistent worktrees** | Separate coordinator, executor and reviewer app tasks | Owner collapses with coordinator | Three user-owned persistent threads | Frozen artifacts + explicit Git starting state | Executor/reviewer worktrees; coordinator integrates in Local | Cross-thread fast lane + artifact authority lane | Separate-task settings unproven | A2 plus result branches/worktrees | Detached reviewer task/worktree reads a selected result revision | Saved tasks + associated worktrees/snapshots | Coordinator merges selected revisions | Three lanes | A2 mapping plus later Full evidence/branch refs |
| **C5 — Artifact-bus Team** | Separate persistent tasks or sessions; app coordination optional | Owner delegates coordination or coordinates directly | User-owned or independently owned sessions | Filesystem packet only; thread IDs are locators | Shared non-Git root with disjoint role paths, or Git worktrees | Durable file questions/decisions; human/app notification optional | Role restriction procedural unless external policy exists | A2 role-owned artifacts; immutable handoff revisions | Separate reviewer lane reads frozen packet | Any session may restart; artifacts reconstruct state | Named coordinator/integrator | Two or three actor lanes | A2 maps upward; original artifacts retained |
| **C6 — Independent human/session team** | Truly independent human/agent sessions | External manager/owner assigns | Separately owned accounts/hosts/sessions | Frozen artifact packet + repository/source revision | Separate repo/worktree/host or controlled shared system | Human/process queue plus repository review | Independent credentials/policies possible | Immutable inputs, role-owned outputs, integration receipts | Independent reviewer identity and policy | External system of record + files | Named integrator/change owner | Three or four distinct actors | A2 can expand; high-risk path may enter Full directly |
| **C7 — Full-shadow Team** | Separate user-owned or independent sessions | Owner + coordinator + executor + reviewer all distinct | Persistent independent lanes | Full artifact chain | Worktree/repo per phase | App/process routing + all TFW gates | Per-role policy | HL/TS/ONB/RF/REVIEW/evidence | Full reviewer workflow | Full Task Board/filesystem state | Coordinator + owner | Four roles | Already Full; no intermediate mapping needed |
| **C8 — Assurance overlay** | One Assisted execution chat + separate reviewer task | Owner directs executor and reviewer | Executor is owner chat; reviewer user-owned task | Frozen result/criteria only | Same checkout, reviewer read-only by procedure | Owner routes one review request/result | Reviewer restriction unproven | Assisted trace/result + `REVIEW.md` | Separate reviewer task | Two saved tasks + artifacts | Owner | Owner/executor + reviewer | Trace/result map to RF; review maps to REVIEW; no coordinator lane |

### Unexpected configurations revealed

1. **C5 Artifact-bus Team** was not proposed in the Briefing. It keeps separate persistent roles but makes app cross-thread messaging optional rather than foundational. Semantic coordination is reconstructed from three role-owned artifacts, so the configuration remains viable for non-Git work and for products whose cross-thread APIs change.
2. **C2 Two-party persistent handoff** shows that four roles do not require four people or even three task lanes. An owner can be coordinator and reviewer while a separate executor provides the independently inspectable value.
3. **C8 Assurance overlay** isolates review without adding a coordinator lane. It may prove that some work needs a review extension to Assisted rather than a stable Team edition.

## Findings

### E1 — Platform coordination and semantic handoff are orthogonal layers

| Layer | Unit | Evidence | Failure if omitted |
|---|---|---|---|
| **Platform coordination** | Create/fork task, send follow-up, read/wait status, optional worktree/Handoff | M3-E1–E5 plus official thread/worktree docs | Slow/manual routing, but artifacts may remain correct |
| **Semantic handoff** | Frozen outcome/criteria, input revision, owner, path ownership, blockers, result revision, review verdict | Proposed A2 artifact contract; predecessor K1–K6 authority/receipt boundary | Fast messages can route the wrong/stale work and leave no independently verifiable transfer |
| **Execution isolation** | Disjoint role paths, single writer, optional worktree | Shared-checkout visibility executed; worktree isolation documented only | Concurrent edits can race or silently invalidate reviewer input |
| **Authority independence** | Separate reject/accept authority and, when required, identity/policy | Not executed inside M3; possible only conditionally in C6 | Separate chats can simulate roles while one actor retains all control |

M3-E1–E5 prove that a coordinator can run a separate, persistent Researcher lane with visible artifacts and checkpoint routing. They do not prove that the Researcher cannot be overridden, that its permissions differ, or that its identity is independent. Therefore platform coordination is a real mechanism beyond an ordinary subagent, but it becomes Team-relevant only when paired with semantic artifact handoff and role-owned authority.

**E-D1:** Define the Team candidate as a two-layer mechanism: persistent role lanes are the coordination carrier; role-owned artifact handoffs are the semantic authority. Either layer alone is insufficient.

### E2 — Pairwise mechanism tests

#### C0 control × C1 child tree

| Test | C0 Assisted + ordinary subagents | C1 explicit child tree | Distinctness result |
|---|---|---|---|
| Parent ownership | Yes | Yes | Same class |
| Shared checkout | Yes | Yes | Same collision boundary |
| Context control | Product-managed child prompt | Explicit all/none/N fork | C1 improves determinism, not independence |
| Messaging/waiting | Main agent orchestrates | Explicit tree API | C1 improves control/observability |
| User-owned persistence | Not required; unproven for child | Unproven | No Team distinction |
| Review independence | Parent selects reviewer child/input/output | Parent selects reviewer child/input/output | Cognitive separation only |

**Pair result:** C1 is a stronger execution engine for the C0 control, not a distinct Team working mechanism. It belongs under Assisted orchestration unless later evidence establishes user-owned persistence or independent authority.

#### C1 child tree × C2/C3 persistent tasks

| Test | C1 child tree | C2/C3 separate tasks | Evidence status |
|---|---|---|---|
| Separate user-owned lane | No evidence | **Executed for this Researcher task** | M3-E1 |
| Multi-checkpoint continuity | Parent runtime tree | **Executed across Briefing/Gather/Extract** | M3-E2 |
| Coordinator follow-up | Child message/follow-up | **Executed from coordinator task** | M3-E3 |
| Read/wait completion routing | Live child wait | **Coordinator exercised read/wait** | M3-E4 |
| Artifact visibility | Shared directory | **Executed shared checkout** | M3-E5 |
| Independent permissions/identity | No | Unproven | No advantage established |
| Semantic handoff | Parent prompt/file optional | Proposed frozen A2 packet | Not yet executed as Team executor/reviewer |

**Pair result:** C2/C3 add a demonstrated durable, separately visible task lane beyond C1. The distinction is persistence and user ownership, not stronger permissions or identity. H9 gains partial support only on this axis.

#### C2 two-party × C3 three-lane

| Test | C2 owner/coordinator/reviewer + executor | C3 owner/coordinator + executor + reviewer | Pressure exposed |
|---|---|---|---|
| Independent execution | Yes, if executor artifact/path is separate | Yes | Equivalent for execution separation |
| Independent review from executor | Yes | Yes | Both satisfy minimum anti-self-review |
| Independent review from planning | No | Better: reviewer did not author brief | C3 offers stronger bias separation |
| Coordination overhead | Two tasks/lanes | Three tasks/lanes | C3 must justify extra lane |
| Small-team fit | Strong for two people | Strong for three people | Role collapse should follow team/risk, not edition dogma |

**Pair result:** C2 can produce independently inspectable value with two actors, but its reviewer is not independent of planning. C3 strengthens review independence without requiring a separate owner lane. Extract keeps both coherent; Challenge must decide what Team may honestly claim.

#### C3 shared root × C4 worktrees

| Test | C3 shared root | C4 worktrees | Pressure exposed |
|---|---|---|---|
| Domain coverage | Git and non-Git | Git only | Worktree cannot be core Team invariant |
| File race control | Disjoint paths + single writer | Separate checkout plus integration | C4 stronger for implementation isolation |
| Starting-state clarity | Explicit root/artifact version | Explicit branch/commit/working-tree snapshot | Both need version authority |
| Integration | File/path-level coordinator | Git merge/cherry-pick/Handoff | C4 adds adapter-specific ceremony |
| Executed evidence here | Shared visibility only | None | C4 remains documented, not observed |

**Pair result:** C4 is a Git adapter of C3/C5, not the semantic definition of Team.

#### C3 app-coordinated × C5 artifact-bus

| Test | C3 app fast lane required operationally | C5 artifact bus remains authoritative | Pressure exposed |
|---|---|---|---|
| API dependency | Read/send/wait available | Optional notification only | C5 survives API/rollout drift |
| Blocking questions | App message + file record | File record + optional notification | Same semantic authority if files are complete |
| Resume after lost task | Task transcript helpful | Artifact state sufficient | C5 stronger recovery property |
| User friction | Faster live routing | More explicit file interaction | C5 risks bureaucracy |
| Non-Codex/cross-user | Weak/unproven | Possible with shared artifacts | C5 forms the path toward Full/agent-agnostic behavior |

**Pair result:** platform messaging is useful but not defining. C5 is the first configuration whose Team semantics do not disappear when the coordinator cannot address another task directly.

#### C5 artifact-bus × C6 independent human/session

| Test | C5 separate lanes, identity may be procedural | C6 separate identities/policies | Pressure exposed |
|---|---|---|---|
| Reviewer authority | Bounded by procedure | Can be organizationally independent | C6 supports stronger claim |
| Permissions | Prompt/process restriction | Separate credentials/policy possible | C6 stronger enforcement |
| Traceability | Artifact ownership and revision | Artifact + external system identity | C6 stronger non-repudiation |
| Product complexity | Three files + routing | Repository/ACL/queue/change control | C6 can cross into Full/organizational process |

**Pair result:** Team inside one user's Codex can claim role-separated and independently inspectable work, not authenticated organizational independence. C6 is the ceiling case, not the default promise.

#### C3/C5 A2 spine × C7 Full-shadow

| Test | A2 Team spine | C7 Full artifacts | Pressure exposed |
|---|---|---|---|
| Planning | One coordinator-owned `BRIEF.md` | HL + TS (+ optional RES) | A2 intentionally combines context/spec at lower assurance |
| Execution | One executor-owned `EXECUTION.md` | ONB + RF + evidence | A2 combines acceptance and result; no Full evidence claim |
| Review | One reviewer-owned `REVIEW.md` | Staged REVIEW + evidence audit | Same semantic destination, different assurance depth |
| Knowledge | Inherits Assisted candidates/memory | Full Fact Candidate + knowledge loop | Team must not duplicate this loop |
| Migration | Split/map with retained originals | Native | A2 provides a real upward path; C7 has no intermediate value |

**Pair result:** A2 can remain Team only if it states its lower assurance honestly. If it adopts Full stage gates, evidence artifacts, research loop and Task Board semantics, C7 absorbs it.

### E3 — Distinct-mechanism tests by configuration

Legend: **E** = executed in Iteration 3; **D** = officially documented; **P** = proposed semantic contract; **U** = unavailable/unproven; **N** = property absent by design.

| Test | C0 Assisted control | C1 child tree | C2 two-party persistent | C3 three-lane persistent | C4 worktrees | C5 artifact-bus | C6 independent team |
|---|---|---|---|---|---|---|---|
| **T1 User-owned separately resumable role lane** | N | U | **E** | **E** for mechanism class; only Researcher lane executed | D | D/P | External/P |
| **T2 Coordinator can inspect/route follow-up/completion** | Parent-native | D/local contract | **E** | **E** for one lane | D/local contract | Optional | External process |
| **T3 Frozen semantic handoff with version authority** | Optional trace | Parent prompt/file | P | P | P | P | P/external |
| **T4 Single writer per role artifact/result** | N/optional | P | P | P | P | P | Policy/P |
| **T5 Reviewer separate from executor and unable to mutate reviewed result** | Cognitive only | Cognitive only | P; unable-to-mutate unproven | P; unable-to-mutate unproven | P; checkout separate, permissions unproven | P/procedural | Policy possible |
| **T6 Resume without hidden transcript** | Assisted trace partial | Files partial | P | P | P | Core P | Core P |
| **T7 Non-Git applicability** | Yes | Yes | Yes | Yes | No | Yes | Depends |
| **T8 Authenticated independent authority** | N | N | U | U | U | U | Possible/external |
| **T9 Additive mapping into Full** | Manual | Parent synthesis | A2 P | A2 P | A2 P | A2 P | A2/full entry |

The configuration space exposes a candidate distinct mechanism at T1+T3+T4+T5+T6. T1 alone is now executed; T3–T6 remain artifact/protocol claims for Challenge. T8 must not become part of the default Team promise.

**E-D2:** “Separate task” is necessary but not sufficient for the Team candidate. The minimum distinction is a persistent role lane plus frozen semantic handoff, separate artifact ownership, reviewer non-mutation and transcript-independent resume.

### E4 — Role-collapse consistency matrix

| Collapse | Compatible conditions | Incompatible claim | Resulting shape |
|---|---|---|---|
| **Owner + coordinator** | Small team; owner can decompose work, route blockers and integrate | None; this is normal delegated authority | C2/C3 minimum |
| **Owner + reviewer** | Owner has competence/authority and did not execute the reviewed result | “Reviewer independent of planning/acceptance preferences” | C2 bounded review |
| **Coordinator + reviewer** | Coordinator planned but did not execute; review input frozen; verdict trace preserved | Full organizational independence; freedom from planning bias | C2 bounded or C3 if reviewer separate |
| **Coordinator + executor** | One bounded lane, no parallel assignments/integration conflict | A distinct delegation mechanism between coordinator and executor | Usually collapses toward Assisted/C8 |
| **Owner + executor** | Personal work or direct execution; no separate acceptance gate claimed | Independent owner acceptance | C0/C8, not core Team |
| **Executor + reviewer of same result** | Only self-check, clearly named verification rather than review | Independent verification/reviewer separation | Incompatible with Team review claim |
| **Owner + coordinator + reviewer** | Two-party work: one owner directs/accepts, another executes | Reviewer independent of planning | C2: minimal two-actor Team candidate |
| **All four distinct** | High-risk, multi-assignment or organizational policy demands it | “Minimum Team for 2–3 people” | C6/C7 ceiling, not default floor |

The role floor is functional:

1. **Owner authority** must exist, but may be outside the active workflow or collapse with coordinator/reviewer.
2. **Coordinator function** becomes distinct only when assignment, dependencies, blocker routing or integration need management.
3. **Executor lane** is required for delegated Team work.
4. **Reviewer lane** is required only when Team promises independent verification; it must not collapse with the executor.

**E-D3:** A stable Team design must support both C2 (two actors) and C3/C5 (three lanes). It must not require four distinct people. The honest guarantee gradient is: separate from execution (C2) → separate from execution and planning (C3) → independent identity/policy (C6).

### E5 — Minimal semantic artifact contract

#### A2.1 `BRIEF.md` — coordinator-owned

| Section | Purpose | Full migration target |
|---|---|---|
| Outcome/impact/owner quote | Working Backwards target and human value | HL Vision |
| Constraints, risks, rejected simple alternative | Boundary and “why not just” | HL Current/Target, Principles, Risks, Why Not Just |
| Acceptance checks | Observable result conditions | TS Acceptance Criteria and Definition of Failure |
| Assignments/dependencies | Executor/reviewer task IDs, role owners, disjoint paths, ordering | HL Phase Dependencies + TS scope |
| Starting-state authority | Root/branch/commit/working-tree snapshot, required artifact versions/digests | TS Inputs/Technical Guidance + K5 authority |
| Decision log | Coordinator answers to executor/reviewer question IDs | HL/TS decisions or later RES/open questions |
| Aggregate status links | Derived links to role-owned statuses; coordinator is sole writer | Full Task Board/phase status |

#### A2.2 `EXECUTION.md` — executor-owned

| Section | Purpose | Full migration target |
|---|---|---|
| Acceptance/understanding | Restate assignment, input revision and intended output | ONB understanding |
| Blocking questions/risks | Question ID, impact, safe stop; references coordinator answer in BRIEF | ONB questions/risks |
| Working trace | Actions, sources, decisions, deviations and checkpoints | RF result/decisions/deviations |
| Result manifest | Output paths/versions/digests and status | RF artifact list/results |
| Verification/limitations | Checks run, observable evidence links, unresolved conditions | RF verification; Full later adds EV/evidence plan |
| Observations/candidates | Useful facts/debt without promotion | RF observations/fact candidates |

#### A2.3 `REVIEW.md` — reviewer-owned

| Section | Purpose | Full migration target |
|---|---|---|
| Frozen review packet | Exact BRIEF/EXECUTION/result versions | REVIEW inputs/map |
| Checks/findings | Requirement-by-requirement verification and actionable defects | REVIEW verify/judge |
| Independence declaration | Relationship to planning/execution; permissions/identity limitations | REVIEW context/limitations |
| Verdict | APPROVE / REVISE / REJECT with reason | REVIEW verdict |
| Follow-up scope | Exact changes required; reviewer does not repair result | REVIEW next action |

#### Cross-file communication without shared writes

- Executor creates `Q-EX-N` in `EXECUTION.md`; coordinator answers `D-N` in `BRIEF.md`; executor records the received decision reference without modifying BRIEF.
- Reviewer creates `F-RV-N` in `REVIEW.md`; coordinator creates a new assignment/revision in BRIEF; executor creates a new result revision in EXECUTION; the old verdict remains.
- Each file carries its own status and current input/output revision. Coordinator derives aggregate state in BRIEF; other roles never edit it.
- Thread/task IDs are locators. Missing thread access does not invalidate the artifact chain.

#### Upward migration rules

1. Retain original Team artifacts as K3 provenance; do not rename them into Full artifacts and destroy history.
2. Split `BRIEF.md` semantically into HL context and TS acceptance/scope. Any unresolved research question creates a new RES; Team does not pretend it already conducted Full RESEARCH.
3. Split `EXECUTION.md` at the acceptance/work boundary into ONB and RF. Full Evidence planning/EV collection is added prospectively; old Team verification is cited with its actual assurance level.
4. Map `REVIEW.md` to the Full REVIEW starting point, but re-run Full review/evidence gates when risk requires; do not promote a Team verdict automatically.
5. Apply predecessor K5/K6: declare source/target edition/version and active authority, retain unknown material, fail closed on semantic conflicts, emit a migration receipt.
6. Assisted task traces/knowledge candidates remain referenced inputs; Team adds no duplicate knowledge index or consolidation loop.

**E-D4:** A2 is a mapping spine, not a compressed Full template set. Its three files align with cognitive ownership boundaries while explicitly deferring RES, EV/evidence and full knowledge gates.

### E6 — Lifecycle state composition

The lifecycle is the composition of three single-writer states, not a common file everyone updates.

| Coordinator `brief_status` | Executor `execution_status` | Reviewer `review_status` | Derived Team state | Allowed next actor |
|---|---|---|---|---|
| DRAFT | — | — | INTAKE/PLAN | Owner/coordinator |
| ASSIGNED | PENDING | — | AWAITING_ACCEPTANCE | Executor |
| ACTIVE | ACCEPTED | — | EXECUTING | Executor |
| ACTIVE | BLOCKED | — | BLOCKED_QUESTION | Coordinator/owner; answer in BRIEF |
| REVIEW | READY | PENDING | AWAITING_REVIEW | Reviewer |
| REVIEW | READY | IN_REVIEW | REVIEWING | Reviewer |
| REVISION | REVISE | COMPLETE_REVISE | REVISING | Coordinator then executor |
| DONE | COMPLETE | COMPLETE_APPROVE | COMPLETE | Owner/coordinator closure |
| STOPPED | any nonterminal | any nonterminal | INTERRUPTED/STALE | Current role reloads artifact/version manifest |

Properties:

- App waiting/status can notify the coordinator, but the derived state is recoverable from files.
- Stale input is detected when a role's declared input revision differs from the current BRIEF/result revision; the role stops before mutation.
- Concurrent writes are safe only when paths and role files are disjoint. Shared result files require a named single writer or worktree integration.
- Completion does not mean Full evidence or knowledge gates have run; those are migration/edition decisions.

### E7 — Review-independence gradient and measurable value

| Level | Mechanism | Independently verifiable value | Honest label |
|---|---|---|---|
| **V0 Self-check** | Executor verifies own work in same transcript | Catches mistakes but no separation from implementation choices | Verification, not review |
| **V1 Child reviewer** | Fresh review subagent, parent-owned | Different context/model/prompt; findings inspectable by parent | Cognitive review assistance |
| **V2 Separate task reviewer** | User-owned reviewer task; frozen input; separate REVIEW artifact; no result edits by contract | Separate transcript and trace; coordinator can compare verdict against exact versions | Role-separated review; permissions/identity bounded |
| **V3 Separate planner-independent reviewer** | Reviewer did not author BRIEF or EXECUTION | Reduces both implementation and planning anchoring | Independently inspectable review within one app/user |
| **V4 Independent authority** | Different person/account/policy/credentials | Can reject without executor/coordinator control; identity trace | Organizationally independent review |

Reviewer value is measurable only if the review produces at least one of:

- a defect, unmet criterion, risk or evidence gap that changes the result or verdict;
- a signed/attributed acceptance decision required by the owner;
- confirmation that the frozen result satisfies the brief without mutating it;
- a revision history showing findings were resolved by the executor rather than silently repaired by the reviewer.

A role/file that produces none of these is ceremony. A separate chat alone establishes V2's transcript boundary only when the artifact and non-mutation rules also hold.

### E8 — What Team adds beyond Assisted, if anything

| Assisted + subagents already provides | Candidate Team addition | Distinct only when |
|---|---|---|
| One owner, task trace, status, identity, memory | Separate user-owned executor/reviewer lanes | They are independently resumable and not merely parent child threads |
| Parallel specialists and summarized results | Durable assignment/acceptance/blocker routing | Semantic state is artifactized and recoverable without parent transcript |
| Optional fresh review child | Role-owned frozen review/verdict | Reviewer is separate from executor, does not edit result and declares independence level |
| Same checkout/file visibility | Explicit path ownership and optional worktree adapter | Concurrent mutation cannot silently cross ownership boundaries |
| One task's completion | Integration authority across role outputs | Coordinator function resolves dependencies/versions rather than merely forwarding summaries |

The new working mechanism is therefore **durable delegation across separately resumable role lanes with single-writer semantic handoffs**. Agent count is not new; subagents already provide it. Separate chats alone are not enough; Projects already provide parallel chats without a Team method.

**E-D5:** Keep C0/C1 as the no-Team control. Advance C2, C3 and C5 as the minimal Team candidate family; treat C4 as a Git adapter, C6 as the independent-authority ceiling, C7 as Full-shadow, and C8 as an assurance-overlay counter-configuration. This is an Extract classification, not a final elimination.

### E9 — H9 extraction verdict

**H9:** Team can be a separate stable edition between Assisted and Full only if Codex tasks/threads provide verifiable separation of coordinator, executor and reviewer beyond ordinary subagents.

| Clause | Extract evidence | Status before Challenge |
|---|---|---|
| Tasks/threads add something beyond ordinary subagents | M3-E1–E5 show user-owned separate task creation, multi-checkpoint persistence, coordinator follow-up, read/wait routing and shared artifact visibility; C0/C1 lack the same demonstrated user-owned lane. | **Supported for persistence/coordination only** |
| Coordinator/executor/reviewer can be separated | C2/C3/C5 + A2 define separate role lanes and single-writer artifacts; only Researcher/coordinator separation was executed. | **Structurally coherent; executor/reviewer unexecuted** |
| Separation is verifiable | Frozen artifact versions, non-overlapping ownership and separate verdict provide a testable trace. Permissions/identity remain bounded. | **Proposed and inspectable; not enforced independently** |
| Team is distinct from Assisted | Durable delegation/semantic handoff is not present in C0/C1 by default. C8 may cover review-only cases without Team. | **Conditional** |
| Team remains below Full | A2 omits RES, EV/evidence and full knowledge gates while mapping upward with K5/K6. | **Structurally coherent** |

**Extract H9 status: 🟡 conditional support.** The executed M3 evidence falsifies the strongest no-difference claim: a separate user-owned task can persist, be followed, read/waited, and exchange visible artifacts across checkpoints, unlike a merely parent-owned child tree. It does not yet prove executor/reviewer independence, permission separation, identity, restart persistence or worktree isolation. Challenge must decide whether the proposed semantic contract closes that gap honestly enough for a stable Team edition, or whether C2/C3/C5 remain an optional pattern inside Assisted.

### E10 — Extract decisions

| # | Decision | Rationale |
|---|---|---|
| **E-D1** | Define Team as persistent role lanes + role-owned semantic handoffs; do not define it by agent count, app messaging or worktrees alone. | Pairwise tests isolate the only combination with a distinct durable mechanism. |
| **E-D2** | Require T1+T3+T4+T5+T6 for the Team candidate; keep authenticated authority T8 outside the default promise. | Separates verifiable process value from unproven identity/permission claims. |
| **E-D3** | Support two-actor C2 and three-lane C3/C5; owner+coordinator collapse is normal, executor+reviewer collapse is incompatible with independent review. | Minimum roles are functions, not job titles or four separate people. |
| **E-D4** | Advance A2 (`BRIEF.md`, `EXECUTION.md`, `REVIEW.md`) as the minimal upward-mapping spine; A3/Full-shaped artifacts remain a failure control. | Three single-writer cognitive modes map cleanly into HL/TS, ONB/RF and REVIEW without pretending Full gates ran. |
| **E-D5** | Treat worktrees and cross-thread APIs as adapter accelerators; the semantic protocol must work through artifacts in a shared non-Git root. | Preserves domain independence and robustness to product-surface changes. |
| **E-D6** | Bound M3-E1–E5 exactly as authorized; preserve all stronger capabilities as unproven. | Prevents availability/one executed Researcher flow from becoming a universal Team guarantee. |

## OODA Stage Log

| Loop | Observe | Orient | Decide | Act |
|---|---|---|---|---|
| **1 — executed M3 evidence** | Re-read current official manual status and coordinator-authorized M3-E1–E5 from this task's actual Briefing/Gather lifecycle. | Separate task persistence/routing is real in this environment, but all isolation/identity claims remain absent. | Split coordination carrier from authority contract. | Added evidence boundary, C0–C8 configuration space and T1–T9 tests. |
| **2 — pairwise mechanism/role analysis** | Cross-referenced Gather D1–D14 across C0 child control, persistent tasks, worktrees and independent sessions. | Most named mechanisms differ on only one axis; C2/C3/C5 combine the axes that can create verifiable value. | Keep role collapse and assurance gradient explicit rather than forcing four actors. | Added pairwise matrices, role-collapse matrix and V0–V4 review gradient. |
| **3 — artifact/migration analysis** | Applied predecessor K1–K6 and the Full artifact semantics to A0–A3. | A2 can map upward without pretending Team is Full; C7 has no intermediate identity. | Make three single-writer artifacts the maximum-minimum candidate and keep app tools optional. | Added exact A2 contract, lifecycle composition, migration rules and conditional H9 status. |

### Deep sufficiency verdict

- [x] External source used: refreshed current official Codex manual; O1–O7 applied to configuration constraints.
- [x] Briefing gap closed: coherent coordination/session/role/artifact configurations and the no-Team control are cross-referenced.
- [x] Configuration Space built from Gather dimensions: C0–C8 vary D1–D14 coherently.
- [x] H9 tested: conditional support, with executed M3 claims separated from proposed Team semantics.
- [x] Counter-evidence sought: C0/C1, C8 and C7 remain active alternatives/collapse cases.
- [x] Metacognitive check: Extract found three unplanned configurations (C2, C5, C8) and a new mechanism definition—persistent role lanes plus single-writer semantic handoff—rather than simply restating the HL's role list.

## Checkpoint

| Found | Remaining |
|---|---|
| This task executes a bounded persistent coordinator↔Researcher lane beyond a parent-owned subagent: creation, multi-turn persistence, follow-up, read/wait completion routing and shared artifact visibility. | No executor/reviewer task experiment; permission, identity, worktree, Handoff, needs-attention, restart and cross-user properties remain unproven by owner lock. |
| C1 child-tree orchestration is a stronger Assisted engine, not Team. | Challenge whether C2/C3/C5 add enough measurable value to deserve an edition or should remain Assisted patterns. |
| C2 two-party and C3/C5 three-lane configurations support owner/coordinator collapse while separating executor/reviewer. | Challenge planning bias in C2 and ceremony cost in C3/C5. |
| Platform coordination and semantic handoff are orthogonal; app APIs are the fast lane, A2 artifacts the authority lane. | Attack lost/stale messages, stale artifact versions, abandoned tasks and coordinator failure. |
| A2 (`BRIEF.md`, `EXECUTION.md`, `REVIEW.md`) maps additively into Full without importing RES/evidence/knowledge gates. | Pairwise consistency check against K1–K6, Full-shadow drift and duplicate Assisted trace/memory. |
| Review independence has an honest V0–V4 gradient; one-user Team can promise role separation, not authenticated organizational independence. | Decide the minimum guarantee that a “stable Team edition” name may carry. |

**Blocking questions:** none.

**Authorization request:** proceed to Challenge only. No further live experiment is requested; attack C2/C3/C5 against the C0/C1 no-Team control, C8 assurance overlay, C6 independence ceiling and C7 Full-shadow, then decide whether conditional H9 supports a stable Team edition.

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?
- [x] Minimum two Extract decisions recorded?
- [x] Hypothesis and counter-configurations tested?

Stage complete: YES
Coordinator record: Extract accepted on 2026-08-08; Challenge authorized.
