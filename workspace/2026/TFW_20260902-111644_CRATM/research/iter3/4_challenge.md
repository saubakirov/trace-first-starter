# Challenge — "Which profile survives the frozen contract, not just the provider demo?"
> **Mindset:** Critic. Every survivor needs evidence; every elimination needs an observable contradiction.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260902-111644_CRATM](../../HL-TFW_20260902-111644_CRATM.md)
> Goal: Re-charter full TFW agent-team delegation with project-scoped roles and task-local coordination while preserving the frozen no-runtime, no-live-roster boundary.

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D1. Long-lived role identity | Nested subagent | D3. Discovery and addressability | Direct task/session id for the child | Helpdesk and current provider semantics route the reply to the parent; a child name does not create an independent cross-session role identity |
| D1. Long-lived role identity | Agent-team teammate | D2. Provisioning | Non-interactive `-p` process spawns the teammate | Current Claude docs explicitly say non-interactive `-p` cannot spawn teammates |
| D1. Long-lived role identity | One session changes roles | D4. Role separation | Dedicated task/session per role | One writer cannot simultaneously be the distinct Executor and independent Reviewer required by the Role Locks |
| D2. Provisioning | Coordinator creates teammate in one native team | D4. Role separation | Nested team led by a Phase Coordinator teammate | Claude agent teams prohibit nested teams and fix the original main session as lead |
| D2. Provisioning | Owner opens peers during execution | D8. Owner intervention after autonomy | Contract-declared exceptions only | Peer creation after the boundary is owner routing/provisioning, not a predeclared infrastructure failure |
| D3. Discovery and addressability | Parent relay plus free-text handle | D8. Owner intervention after autonomy | No relay/owner routing | The role cannot receive or reply directly; the relay is the actual provider-visible sender |
| D3. Discovery and addressability | Explicit foreign fresh-run id | D1. Long-lived role identity | Address an already-running task in the other provider | The id names the process just launched, not an existing foreign provider task/session |
| D4. Role separation | Concurrent mutation-bearing role holders | D5. Workspace isolation | Shared checkout with file partitioning | Frozen isolation is structural; file ownership guidance does not give separate indexes or prevent same-file/status collisions |
| D5. Workspace isolation | Permanent worktree with multiple chats | D4. Role separation | Concurrent independent writers in those chats | Multiple chats share one working tree and index, so the worktree ceases to isolate the writers from one another |
| D6. Durable coordination trace | New live project roster | D7. Artifact legality | Existing TFW artifacts only | The roster is a new artifact and a second task-state authority; Helpdesk measured its drift |
| D6. Durable coordination trace | Transcript/provider task list only | D7. Artifact legality | Existing status/journal as task authority | Runtime/transcript state cannot replace the frozen task-local authority and is not an immutable TFW trace |
| D7. Artifact legality | Agent-definition file used as role holder | D1. Long-lived role identity | Provider-visible session/task | A definition is instructions, not a running identity; Helpdesk observed this exact category error |

**Surviving configurations** (after applying the incompatibilities and narrowing each to the scope it can actually carry):

| Config | D1. Long-lived role identity | D2. Provisioning | D3. Discovery and addressability | Notes |
|--------|-------------------------------|------------------|--------------------------------------|-------|
| C1. Codex managed tasks | User-visible task per role | Coordinator creates task | Direct thread id | First-release candidate; G1–G7 field-supported, G8 not controlled |
| C3. Codex bounded helper | Nested subagent | Coordinator spawns helper | Parent return | Survives only as a stage helper, never a long-lived TFW role |
| C5. Claude team + explicit worktrees | Teammate per role | Interactive lead spawns | Team mailbox/name | Research survivor only; teammate worktree retention and fixed-lead mapping need field proof |
| C6. Owner-opened Claude peers | Independent session per role | Owner provisions before boundary | Native session discovery/message | Later-test candidate; installed surface and no-roster whole workflow unproved |
| C7. Claude background peers | Background session per role | Coordinator launches | Cross-session name/id | Later-test candidate on a newer compatible build; not field-supported here |
| C8. Claude headless resumable | Explicit persistent session id per role | Coordinator launches `-p` | `--resume <id>` | Later-test candidate; continuity measured, whole TFW role not measured |
| C9. Two-level Claude hybrid | Independent Phase Coordinator + teammates | Main launches Phase; Phase lead spawns team | Cross-session upper edge, team mailbox below | Unexpected survivor; most contract-shaped, most composed and least tested |
| C10. Sequential same-provider fallback | Distinct sessions, one active at a time | Coordinator launches/resumes | Explicit id | Honest fallback, not evidence for concurrent team operation |
| C11. Mixed bounded helper | Fresh foreign process | Coordinator launches | Returned result/id | Survives only as a bounded helper; eliminated as a long-lived role profile |

C2 is removed for concurrent writers because multiple chats in one permanent worktree share an index. C4 is removed in its documented default form because a shared checkout does not satisfy the frozen worktree requirement and one fixed lead cannot reproduce the two-level creation chain. Neither elimination says the provider feature is defective; each says the feature's default shape is not the TFW profile being specified.

**Unexpected survivors** (configurations that survived but were not initially favored — worth highlighting):

- **C9 two-level Claude hybrid:** it maps fixed-lead/no-nested-team semantics to the frozen initiation chain by making the independent Phase Coordinator session the per-phase team lead. It survives logically, not empirically.
- **C7 background peers:** current provider docs give a coordinator-created independent-session family that neither the predecessor nor Helpdesk measured. It removes universal owner pre-provisioning only on a compatible, freshly proven surface.
- **C8 headless resumable:** it has less peer visibility than agent teams but more field evidence for creation and continuity. Sequential explicit-id dispatch may meet the walk-away outcome even if it is not the richest team UI.

## Findings

### C1. Codex C1 survives structurally, not as a completed walk-away experiment

The strongest attack is selection bias: RCFR and VBSA are the runs the owner already cited as successful, task metadata was inspected after the fact, and neither run declared a measurement protocol for owner turns before autonomy. The sample proves capability, not reliability rate.

Counter-evidence inside the same traces:

- The master records the owner's report that Codex can self-fork unexpectedly. Neither RCFR nor VBSA yields a denominator for silent tasks, duplicate forks, or failed starts.
- VBSA needed an owner verdict after Phase A when `/tfw-docs` found a required `KNOWLEDGE.md` value path but the lifecycle had no legal KNW return. That was a contract defect rather than a routing defect, yet it still breaks the strong “owner returns to a finished result” observation.
- RCFR's finish-except-push instruction is compatible with an autonomy boundary, but the inspected trace does not label the exact boundary and count every subsequent owner turn.
- Git commit subjects prove role attribution, not task independence. The stronger identity evidence came from app task ids and separate CWDs; future evidence must preserve both.
- Managed worktrees isolate files but share git metadata. Landing and branch-state conflicts remain protocol obligations, not properties of the chat identity.

**Challenge result:** retain C1 as the first-release candidate and H10 as **field-supported for G1–G7**. Do not promote it to a controlled G8 pass or a reliability guarantee. Disconfirm H10 if one sampled long-lived role is actually a nested subagent, cannot be addressed directly by its coordinator, shares a mutation index with a concurrent role, or writes outside its Role Lock.

### C2. Claude agent teams do not directly mirror the frozen hierarchy

The native-team alternative looks strongest until the contract is overlaid:

- [Agent-team documentation](https://code.claude.com/docs/en/agent-teams) fixes one lead, forbids nested teams, and says teammates inherit project context plus the spawn prompt rather than the lead's conversation. The Phase Coordinator therefore needs an explicit authoritative payload; conversational inheritance cannot be assumed.
- A single Main-Coordinator-led team can spawn every role, but the Phase Coordinator no longer creates its Executor/Reviewer descendants. A Phase-Coordinator-led team preserves that lower edge but needs a separate upper Main→Phase session route.
- Agent-team teammates share a checkout by default, and the official guidance is to partition files. That conflicts with the frozen “isolated working trees” result for concurrent mutation owners. C5 survives only if an actual teammate can enter, remain in, and report from a distinct worktree without losing team addressability.
- Permission prompts surface at the lead. A walk-away trial must pre-authorize only the approved scope or treat an unexpected permission request as a declared infrastructure stop; having the owner click prompts throughout is not autonomy.
- Team config/task state is useful runtime state, but the config is removed on exit and the task list follows provider retention. Neither may become TFW task authority or a copied project registry.

**Challenge result:** default C4 is eliminated. C5 and C9 remain exact later-test candidates, not shippable evidence. A successful field run must show the role identity, worktree and hierarchy simultaneously; three separate demos do not compose by assertion.

### C3. Version/OS/surface belongs to preflight evidence, not participant identity

Extract E3 overreached when it said a profile must “bind” OS and version. The frozen master separates stable participant identity from provider/model/session mechanics: the Role Assignment names a principal and semantic channel, not an executable build. Putting `Claude Code 2.1.234 on Windows` into `team/{handle}.md` or Role Assignment would create a fast-stale registry and revive the two-files-must-agree failure.

The hostile case is an automatic update after freeze. A stored minimum version remains textually true while an organization flag disables the feature, a permission setting holds every inbound message, or a later build changes behavior. Conversely, the installed `2.1.109` Helpdesk surface reported `ListAgents` behavior not explainable from today's documented minimum alone. Version comparison is diagnostic, not a capability proof.

The corrected boundary is:

| Stable contract | Dispatch-time preflight evidence | Never stored as authority |
|-----------------|----------------------------------|---------------------------|
| Participant/principal, workflow role, scope, reports-to edge, autonomy boundary, semantic channel such as `provider-visible task` | Current executable/version/OS, actual tool/flag presence, target listing, nonce delivery, inbound decision, worktree path/common-dir, permission result | Live session roster, “current version” in profile, process pid/lock, copied provider team config/task list |

Preflight belongs in the existing dispatch/journal evidence for that run. It tests behavior first and records version/OS only to diagnose/reproduce it. No new profile field, config key, per-task file or liveness update is warranted. If the semantic route is unavailable, the frozen participant is unavailable and the existing owner-return rule applies; the task does not silently substitute another topology.

### C4. Channels and app-server defeat absolute H12, not the first-release boundary

The external falsification search found two current integration surfaces:

- [Claude channels](https://code.claude.com/docs/en/channels) can push external events into an already-open Claude Code session and can be two-way. But a channel is an MCP server/plugin running as a subprocess, opted in at session start, gated by auth/organization policy/sender allowlists, and in research preview. A custom bridge is exactly a runtime/integration CRATM froze out.
- [Codex app-server](https://developers.openai.com/codex/app-server) exposes `thread/list`, `thread/resume`, and `turn/start`; the [Codex SDK](https://developers.openai.com/codex/sdk) can resume a local thread by id. But this is an API for a client application. The docs do not prove that an arbitrary Claude session can identify and append to the already-running user-visible Codex desktop task used by TFW, nor that doing so avoids an integration client and approval/session-store boundary.

A custom program could plausibly connect the two surfaces. That possibility is sufficient to reject “mixed providers are impossible forever.” It does not supply an in-scope first-release peer route:

1. neither provider's native peer list names the other's task/session;
2. the bridge itself becomes a runtime, transport, credential and liveness subject;
3. current field evidence covers fresh subprocesses only;
4. no run shows bidirectional direct role identity, worktree isolation, Role Lock and owner-free correction through the bridge.

**Challenge result:** H12 survives only as **exclude mixed long-lived roles from the first release under the current no-runtime contract and measured routes**. It is reopened by a later separately scoped task that either proves a direct provider-native existing-session route or explicitly re-charters a bridge/runtime with its own security and trace design. Mixed fresh runs remain legal bounded helpers when only the returned result matters.

### C5. Owner interaction is an outcome metric, not a topology label

No profile gets G8 merely by avoiding a relay. The later acceptance run counts owner turns after the declared boundary and classifies each against the frozen exhaustive return list:

| Owner turn cause | G8 treatment |
|------------------|--------------|
| Reserved frozen claim, proposer is nearest ruler, Purpose Check contradiction, REJECT, unavailable participant, budget excess, nonterminating initiation chain | Allowed contract return; autonomy stopped honestly |
| Permission approval that should have been preflighted | Profile failure for that run |
| Opening/replacing a peer after autonomy | Profile failure unless the participant became unavailable and the contract stopped first |
| Relaying a message to an unreachable role | Direct-address failure |
| Correcting a stale roster or identifying the active session | Artifact/address failure |
| “Keep going,” task-status query needed to wake a role, or manual gate forwarding | Walk-away failure even if artifacts later pass |

This prevents C6 from hiding owner provisioning inside “setup” after the boundary, and prevents C1 from treating VBSA's legitimate lifecycle stop as proof that Codex routing failed. G8 is controlled only when the boundary and count are declared before the run.

### C6. Pairwise profile verdicts and reversal evidence

| Comparison | Survives for first release? | Why | Evidence that reverses it |
|------------|-----------------------------|-----|---------------------------|
| C1 Codex tasks vs C2 shared permanent worktree | **C1** | Same identity/addressing, but C1 supplies one index per role | Field proof that permanent-worktree chats cannot overlap mutation and still meet every phase latency/landing requirement |
| C1 Codex tasks vs C4 default Claude team | **C1** | C1 has field task/worktree/role evidence; C4 conflicts with worktree and hierarchy defaults | One native Claude trial passing the full acceptance envelope |
| C5 Claude isolated team vs C6 owner peers | Neither yet | C5 removes owner provisioning but has no field worktree proof; C6 has peer evidence but not a roster-free full chain | Whichever first completes the same frozen acceptance unit with G1–G8 evidence |
| C6 owner peers vs C8 headless resumable | Neither yet | C6 has better live visibility; C8 has better on-demand creation/continuity | Same unit, same owner-turn count, compare only after both use exact ids and isolated worktrees |
| C7 background peers vs C9 hybrid | Neither yet | C7 is simpler; C9 better matches the two-level initiation chain but composes more untested surfaces | Compatible-build trial proving hierarchy and worktree behavior end to end |
| Any homogeneous long-lived profile vs mixed long-lived profile | **Homogeneous only** | No current in-scope direct peer route crosses provider namespaces | Direct provider-native bidirectional existing-session route, or a separately approved bridge/runtime design and field trial |

Hypothesis disposition entering Synthesize:

- **H10:** survives as **field-supported G1–G7, G8 not controlled**. It supports a Codex-only first-release profile, not a claim of completed walk-away reliability.
- **H11 as written:** the universal owner-preprovision premise is refuted by current documented agent teams/background-session possibilities. The broader claim “a Claude-only profile can satisfy the contract” remains open; C5/C6/C7/C8/C9 are separately testable, and none has a native whole-TFW pass.
- **H12:** survives as a first-release exclusion under current measured/in-scope routes. Channels/app-server make permanent impossibility untenable and define a later bridge research task, not a current mixed profile.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C1 survives only at the field-supported G1–G7 level | Synthesize a recommendation that does not imply controlled G8 reliability |
| Default Claude team C4 fails frozen hierarchy/worktree defaults; C5/C9 remain testable | No native Claude end-to-end test exists |
| Version/OS/surface moved from stable profile identity to dispatch-time behavioral preflight | Final acceptance text must avoid introducing a version registry |
| Channels/app-server are credible bridge ingredients but require an out-of-scope runtime/client | Phrase H12 as current first-release exclusion, never permanent impossibility |
| Pairwise comparisons and reversal evidence exist for H10–H12 | Convert them into RES decisions, refinements and open threads after STOP approval |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Pairwise incompatibility checked? Surviving configurations listed?

Stage complete: YES
→ Main Coordinator decision: pending at STOP
