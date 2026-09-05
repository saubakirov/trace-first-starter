# Extract — "Which role topology closes which gate?"
> **Mindset:** Analyst. Build the space without promoting documentation into field proof.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260902-111644_CRATM](../../HL-TFW_20260902-111644_CRATM.md)
> Goal: Re-charter full TFW agent-team delegation with project-scoped roles and task-local coordination while preserving the frozen no-runtime, no-live-roster boundary.

## Configuration Space

The dimensions are conditional rather than freely Cartesian: provider surface determines which provisioning and addressing alternatives can coexist. These are all non-obviously-contradictory profile families after removing impossible cross-products; evaluation is deferred to Challenge.

| Config | D1. Long-lived role identity | D2. Provisioning | D3. Discovery and addressability | D4. Role separation | D5. Workspace isolation | D6. Durable coordination trace | D7. Artifact legality | D8. Owner intervention after autonomy |
|--------|-------------------------------|------------------|--------------------------------------|---------------------|-------------------------|-------------------------------|-----------------------|---------------------------------------|
| C1. Codex managed tasks | User-visible task | Coordinator creates task | Direct task/thread id | Dedicated task per role | Managed worktree per task | Existing TFW status/journal/artifacts | Existing TFW artifacts only | Contract-declared exceptions only |
| C2. Codex tasks in a permanent worktree | User-visible task | Coordinator creates task | Direct task/thread id | Dedicated task per role | Permanent worktree, multiple chats | Existing TFW trace | Existing TFW artifacts only | Contract-declared exceptions only |
| C3. Codex bounded helper | Nested subagent | Coordinator creates helper | Parent return or named child | Helper only; parent keeps workflow role | Temporary worktree or read-only shared checkout | Parent's TFW trace | No new project artifact | Contract-declared exceptions only |
| C4. One Claude native agent team | Agent-team teammate | Interactive lead spawns named teammates | Team name/mailbox | Dedicated teammate per role | Shared checkout with file partitioning by default | TFW trace plus provider-generated task state | Existing TFW artifacts plus ephemeral provider state | Contract-declared exceptions only |
| C5. One Claude team with explicit worktrees | Agent-team teammate | Interactive lead spawns named teammates | Team name/mailbox | Dedicated teammate per role | Each teammate explicitly enters an assigned worktree | TFW trace plus provider-generated task state | Existing TFW artifacts plus ephemeral provider state | Contract-declared exceptions only |
| C6. Owner-opened Claude peers | User-visible independent session | Owner opens every peer before boundary | `ListAgents` / `SendMessage` by session name | Dedicated session per role | Separate `--worktree` session | Existing TFW trace | Existing TFW artifacts only | Owner provisioning before boundary only |
| C7. Coordinator-dispatched Claude background peers | User-visible/background session | Coordinator launches named background session | `ListAgents` / `SendMessage` plus session id | Dedicated session per role | Background/desktop worktree per session | Existing TFW trace | Existing TFW artifacts only | Contract-declared exceptions only |
| C8. Claude headless resumable delegates | Resumable `-p` session | Coordinator launches process | Explicit returned session id and `--resume` | Dedicated session id per role | `-p --worktree`, resumed into same worktree | Existing TFW trace plus captured session id in dispatch evidence | Existing TFW artifacts only | Contract-declared exceptions only |
| C9. Two-level Claude homogeneous hybrid | Independent Phase Coordinator session leading its own per-phase agent team | Main Coordinator launches Phase Coordinator; Phase Coordinator spawns role teammates | Cross-session name at upper edge; team names below | Dedicated session/team member per role | Phase Coordinator worktree plus explicit teammate worktrees | TFW trace plus provider runtime state | Existing TFW artifacts plus ephemeral provider state | Contract-declared exceptions only |
| C10. Same-provider sequential fallback | One independent session at a time | Coordinator launches/resumes next session | Explicit id | Roles remain distinct sessions but never concurrent | One worktree transferred or one fresh worktree per session | Existing TFW trace | Existing TFW artifacts only | Contract-declared exceptions only |
| C11. Mixed bounded subprocess helper | Fresh foreign-provider run | Coordinator launches process | Returned result/session id | Helper only; coordinator keeps workflow role | Read-only or dedicated worktree | Parent's TFW trace plus dispatch evidence | Existing TFW artifacts only | Contract-declared exceptions only |

C7 and C9 were not proposed in the Briefing. Current Claude documentation exposes a coordinator-created background-session plus cross-session-messaging composition, and C9 uses that upper edge to place the Phase Coordinator in its own session, where it can be the fixed lead of a per-phase team. This combination matters because a teammate cannot create a nested team.

Three observed shapes are excluded from the candidate space, but retained as negative controls:

| Excluded shape | Contradiction |
|----------------|---------------|
| X1. Helpdesk hidden role subagent behind a parent relay | The durable role holder is neither independently listable nor directly addressable; the relay sees/replies as the sender |
| X2. Helpdesk-style `SESSIONS.md` as the role map | New task artifact and live second state authority; field-observed drift violates frozen DoF 3/7 |
| X3. Mixed-provider fresh-run crossing used as a long-lived role peer | Explicit id can resume the fresh foreign run, but the coordinator still lacks a route to the other provider's already-live task/session namespace |

## Findings

### E1. Source-labelled profile evidence

| Profile | Field-observed | Provider-documented | Inference only | TFW gate not closed |
|---------|----------------|---------------------|----------------|---------------------|
| **C1 Codex managed tasks** | RCFR and VBSA expose distinct coordinator/executor/reviewer task ids, direct sends/waits, same-role reuse on correction, separate worktrees and role-attributed artifacts | Codex worktree docs describe one isolated checkout per managed chat; subagent docs distinguish parent-collected helpers | The same structure will work for every phase without a self-fork or silent task | Controlled run with an explicit autonomy timestamp and zero non-exception owner turns after it |
| **C4/C5 Claude native team** | None. Helpdesk did not use a native agent team | [Agent teams](https://code.claude.com/docs/en/agent-teams): interactive lead spawns named independent teammates; mailbox and shared tasks; no nested teams; lead fixed; `-p` cannot spawn teammates; team config is generated runtime state | A teammate can enter and retain an isolated worktree while remaining addressable, and one team can carry the whole TFW hierarchy | Native TFW unit; exact Role Lock delivery; per-teammate worktree proof; permission prompts pre-resolved; hierarchy compatible with fixed lead/no nested teams |
| **C6 owner-opened Claude peers** | Iteration 2 listed eight durable peers and got a cross-project response; Helpdesk used directly addressable sessions for `helpdesk-7f`, `helpdesk-d2`, `helpdesk-82`, and `helpdesk-89`, but the overall run also used relays and a roster | [Cross-session messaging](https://code.claude.com/docs/en/cross-session-messaging): sufficiently new sessions discover/send by `ListAgents`/`SendMessage`; [worktrees](https://code.claude.com/docs/en/worktrees): separately launched sessions can be isolated and resumed | A frozen role assignment plus session names is enough to remove the roster and every message will be delivered unattended | Re-measure on the exact installed build; eliminate duplicate-name ambiguity and held inbound approvals; complete a TFW unit with no roster or owner relay |
| **C7 coordinator-dispatched background peers** | None in Helpdesk/RCFR/VBSA on Claude | Current CLI docs expose `--bg`; background sessions appear in cross-session discovery; agent view sessions receive worktrees automatically | A Claude Main/Phase Coordinator can create every required peer and preserve the downward initiation chain without owner pre-provisioning | Installed binary route unavailable/unverified; role naming, worktree base, inbound policy, whole TFW chain and cleanup all untested |
| **C8 headless resumable delegates** | Iteration 2: `claude -p` returned a session id and answered a follow-up from its own history through explicit `--resume`; one-word route only | Current CLI/worktree docs preserve `-p`, `--resume`, `--session-id`, and `-p --worktree`; non-interactive sessions do not spawn agent-team teammates | Repeated explicit-id invocations can carry a long-lived TFW role as reliably as a live peer mailbox | Whole `/tfw-handoff` or `/tfw-review`; independently visible role identity; bidirectional coordinator routing; bounded resume cost; artifact/commit conformance |
| **C9 two-level Claude hybrid** | None | Each component is separately documented: independent-session messaging/worktrees above, native team below | The composition preserves “Phase Coordinator creates the others” despite fixed lead/no nested teams | Cross-feature compatibility, two worktree layers, Role Lock propagation, routing trace and full unit are wholly untested |
| **C11 mixed bounded helper** | Iteration 2 launched both directions and got text; no existing foreign live session was addressed | Each provider documents only its own task/session namespace | Safe as a bounded helper where only the return matters | It cannot hold a long-lived Role Assignment row until a direct existing-session cross-provider route exists |

The three required Claude alternatives therefore remain distinct:

1. **Native agent team:** strongest documented internal messaging and coordinator-created teammates; weakest field evidence and no automatic worktree isolation.
2. **Owner-opened peer sessions:** strongest Claude field evidence for independent identity and direct session work; provisioning costs an owner action and current documented cross-session semantics require a newer Windows build than the one measured here.
3. **Headless resumable sessions:** strongest measured on-demand creation and explicit continuity; weakest evidence for live peer visibility, peer-to-peer routing, and whole-workflow conformance.

C7/C9 add a fourth family rather than collapsing those three: coordinator-created background peers may eventually replace owner provisioning while retaining independent-session worktrees and the TFW initiation chain.

### E2. Observable TFW gate matrix

Provider terms do not satisfy a gate by name. Each gate has an observable pass condition:

| Gate | Observable pass condition | C1 Codex | C4/C5 Claude team | C6 Claude peers | C8 headless | X1 relay | Long-lived mixed |
|------|---------------------------|----------|--------------------|-----------------|-------------|----------|-----------------|
| G1 Identity | Every long-lived role has its own provider-visible identity | Field pass | Docs only | Field partial + docs | Session id only | **Fail** | Foreign fresh id only |
| G2 Provisioning | Its coordinator can establish the role before use, or owner provisioning is explicitly before autonomy | Field pass | Docs only | Field owner-provisioned | Field launch pass | Parent creates wrong topology | Fresh launch only |
| G3 Direct address | Coordinator sends and receives without a human or parent relay | Field pass | Docs only | Field partial; current route version-bound | Explicit CLI follow-up only | **Fail** | **Fail for existing role** |
| G4 Role Lock | Dedicated writer stays within one TFW role and legal artifact set | Field pass in sampled chains | Untested | Partial artifact evidence | Untested | Sender/role obscured | Untested |
| G5 Isolation | Every concurrent mutation owner has a separate git worktree | Field pass | **Docs default fails; C5 untested** | Docs only | Docs only | Parent-dependent | Worktree cannot fix routing |
| G6 Durable trace | Status/journal/role artifacts reconstruct dispatch and return without transcript authority | Field pass | Untested; provider task list is non-authoritative | Helpdesk needed illegal roster | One-word probe only | **Fail without relay trace** | Fresh-run dispatch only |
| G7 Artifact boundary | No new registry, lock, runtime or project liveness file | Field pass | Docs permit runtime state outside project | Helpdesk overall failed through roster | Candidate pass; untested in workflow | **Fail when repaired by roster** | Candidate pass as helper only |
| G8 Walk-away | After declared boundary, owner turns occur only for the frozen exhaustive exception list | Not controlled | Untested | Helpdesk **fail** | Untested | **Fail** | **Fail for long-lived role** |

Only C1 has field passes across the seven structural gates G1–G7. It still lacks a controlled measurement for G8. No Claude profile has more than partial field closure, and provider documentation must not fill the missing cells.

### E3. Version and surface are part of the profile

The Extract-stage official-source refresh corrected the initial Gather snapshot:

- Current agent-team documentation describes behaviour as of v2.1.178 and records later changes through at least v2.1.251. It does not provide evidence for this workstation by itself.
- Current cross-session messaging requires v2.1.234+ on native Windows, with later floors for some provider combinations. It supports live local/background sessions, but delivery may be held for owner approval unless inbound settings and permission classes align.
- This workstation returned `Claude Code 2.1.109`. Its `--help` exposes `-p`, `--resume`, `--session-id`, and `--worktree`, but the filtered help did not expose current `--bg`/background-session flags. The installed build is below the documented Windows cross-session floor.
- Helpdesk's `SESSIONS.md` nevertheless reports a `ListAgents`/`SendMessage` surface. That trace does not record the executable/version/feature flags, so it proves the field behaviour it states but cannot be equated to the current documented route.

Therefore “Claude-only” is not a single capability fact. A profile must bind at least provider, surface, OS, version, provisioning mechanism, address mechanism, inbound-message policy, and worktree mechanism. This is environment evidence, not a proposal to store liveness in TFW.

### E4. The fixed-lead constraint splits the Claude-native design

The frozen design says every initiation edge starts at a coordinator, and field practice is Main Coordinator → Phase Coordinator → Executor/Reviewer. Current agent teams have one fixed lead and prohibit nested teams. Three structurally different mappings follow:

1. **Single task-level team (C4/C5):** Main Coordinator is lead and spawns all roles. Phase Coordinator can message Executor/Reviewer, but did not establish those role holders. The provider hierarchy and TFW reports-to/initiation hierarchy diverge.
2. **Phase-only team:** owner or Main Coordinator separately establishes the Phase Coordinator session; that session is team lead and spawns Executor/Reviewer. The phase hierarchy fits, but the upper Main→Phase edge still needs owner provisioning, cross-session messaging, or a background-session launch.
3. **Two-level homogeneous hybrid (C9):** Main Coordinator launches a distinct Phase Coordinator background/session peer and addresses it cross-session; Phase Coordinator leads its own agent team. This preserves both initiation levels without nested teams, but it is a composition of documented features with zero field evidence.

The second and third mappings did not appear in the Briefing. They keep H11 open in a narrower and more testable form instead of forcing either “owner opens every peer” or “one team mirrors the entire Codex tree.”

### E5. Owner turns must be classified by cause

| Trace | Post-boundary owner involvement observed | Classification for H10/H11 |
|-------|------------------------------------------|-----------------------------|
| Helpdesk | Opened/replaced sessions, corrected agent-definition/session confusion, stopped a phase planned before research closure, and participated when routing/roster identity was unclear | Both topology failures and legitimate contract corrections; overall G8 fails |
| RCFR | The inspected chain contains direct task routing and a broad finish-except-push grant; no relay was found | Structural H10 support. The trace does not carry a predeclared timestamped G8 experiment, so absence of a found relay is not proof of zero owner turns |
| VBSA | Direct role routing ran through approve; the Main Coordinator then asked the owner whether required `KNOWLEDGE.md` value belonged in a new phase because current lifecycle forbade a direct KNW return | A contract/lifecycle ambiguity, not a task-addressing failure. It still means the observed run did not satisfy the strong zero-intervention outcome |

This classification prevents two opposite errors: calling every owner verdict a provider routing failure, or erasing owner time merely because the platform's sends worked.

### E6. Exact evidence envelope for the later Claude-native trial

The later trial should choose exactly one Claude profile and record the following without adding a TFW artifact class:

1. **Preflight:** capture OS, `claude --version`, enabled surface, `--help` support, worktree base, permission mode and inbound-message policy in existing dispatch/journal evidence. Do not copy provider runtime registries into the project.
2. **Frozen unit:** use one small already-approved phase with Phase Coordinator, Executor and Reviewer roles, an explicit `Autonomous from` value, existing ONB/RF/REVIEW outputs, and no known amendment.
3. **Provisioning proof:** show who created each long-lived role and how. For native team, prove teammate rather than subagent. For peers, prove independent session rather than parent relay. For headless, capture each explicit session id and forbid `--last`.
4. **Address proof:** coordinator lists the exact target, sends a nonce-bearing bounded assignment, target replies directly, and the durable dispatch/return records the named participant without using a live roster. Duplicate or ambiguous names fail.
5. **Isolation proof:** before mutation, record each role's absolute worktree and git common directory; prove worktree paths differ and only the allowed mutation owner dirties each. Agent-team shared-checkout partitioning fails this gate.
6. **Role proof:** Phase Coordinator authors neither ONB/RF nor REVIEW; Executor authors ONB/RF; Reviewer independently reads the fixed result and authors REVIEW. A forced rejection/correction round reuses the same role identities without role switching.
7. **Autonomy proof:** after the declared boundary, count every owner message. Only a trigger already in the frozen exhaustive return list may be nonzero; permission prompts, address ambiguity, peer creation, relay forwarding, roster repair, or “keep going” are failures.
8. **Terminal proof:** the bounded unit reaches its declared approved terminal state; status and immutable journal reconstruct initiation, dispatch, correction, approval and owner-turn count without consulting provider transcripts or runtime task state.

Profile-specific disconfirmation is now explicit: C4/C5 fail if a role is a subagent, if a teammate cannot stay in its worktree, or if fixed-lead hierarchy forces an illegal initiation edge; C6 fails if owner-opened peers require any later owner relay/approval or live roster; C8 fails if explicit resume cannot carry the whole workflow or expose a directly addressable role; C9 fails if the independent-session and team planes cannot compose without the lead becoming the owner-facing router.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Eleven non-contradictory configurations plus three excluded controls derived from all eight Gather dimensions | Challenge pairwise trade-offs and remove configurations that fail frozen gates |
| Three required Claude families remain separate, with field/docs/inference/unclosed-gate columns | No Claude family has a native whole-TFW field pass |
| Current docs expose new C7/C9 background-peer and two-level homogeneous combinations | Installed `2.1.109` cannot be treated as having the current Windows cross-session route |
| Codex C1 closes structural G1–G7 in repeated field traces | Controlled G8 walk-away measurement remains absent |
| Exact eight-step Claude acceptance envelope extracted | Challenge whether every step is minimal, observable and compatible with fixed lead/no nested teams |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?

Stage complete: YES
→ Main Coordinator decision: pending at STOP
