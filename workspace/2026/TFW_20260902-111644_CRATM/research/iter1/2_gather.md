# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260902-111644_CRATM](../../HL-TFW_20260902-111644_CRATM.md)
> Goal: Determine whether Codex can carry an inspectable coordinator-to-delegate chain, with git worktree isolation and task-local delegation traces, without adding a TFW runtime.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1: coordination topology | one task, no child | bounded sub-agent tree inside one task | separate user-visible Codex tasks | nested phase coordinator with its own delegates |
| D2: workspace isolation | shared checkout and index | separate git worktree | detached worktree | read-only delegate with no checkout mutation |
| D3: delegation payload | plain prompt only | inherited conversation | explicit artifact bundle | task reference plus explicit read set |
| D4: durable trace | chat/task history only | TFW `dispatch` journal event | role artifacts plus `dispatch` | child-produced files plus landing commit |

## Findings

### G1. Codex exposes two coordination planes, not one undifferentiated "team mode"

Official Codex documentation describes subagents as a parent-orchestrated tree: the main agent
spawns delegates, routes follow-ups, waits, and closes them; the app exposes the subagent threads
for inspection. The same documentation warns that write-heavy parallel work can conflict and says
subagents inherit the parent permission and sandbox policy. Separately, the Codex app exposes
independently addressable user-visible tasks with task IDs, status, follow-up, wait, interrupt, and
handoff operations. These are distinct mechanisms:

| Plane | Addressability | Context transport | Default filesystem boundary | Durable visibility |
|-------|----------------|-------------------|-----------------------------|-------------------|
| in-task subagent tree | canonical parent/child path | selected conversation fork plus explicit prompt | the parent task's current checkout | subagent thread and returned result |
| user-visible Codex tasks | stable task ID | explicit task prompt and later messages | local checkout or an app-managed worktree chosen for that task | sidebar task, task history, and task status |

Sources: [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents),
[Codex app server](https://learn.chatgpt.com/docs/app-server).

### G2. The capability is present in the measured local build

- `codex --version` returned `codex-cli 0.151.0-alpha.7.2`.
- `codex features list` reported `multi_agent` as stable and enabled; `multi_agent_v2` was stable
  but disabled. No explicit `[agents]` override was found in the local Codex configuration.
- The current collaboration surface supported spawn, message, follow-up, wait, interrupt, and
  tree inspection. The app surface separately supported task creation, read, follow-up, wait,
  interrupt, fork, and worktree handoff. Task creation was not exercised because it creates a
  user-owned sidebar task and was outside this iteration's authorization.
- Existing app task history supplied a field case with an actual coordinator -> phase coordinator
  -> executor/reviewer chain. Exact task IDs remained independently addressable, but empty/silent
  app responses required the coordinator to inspect durable repository traces before deciding that
  a delegate had failed. Recovery also split one logical reviewer role across more than one task ID.

This separates **documented**, **exposed**, and **observed** claims. A documented operation is not
reported as observed unless this iteration or an existing task trace actually exercised it.

### G3. Controlled nested delegation worked once, with an explicit bound

A read-only phase-coordinator probe created exactly three direct children sequentially:
`researcher_probe`, `executor_probe`, and `reviewer_probe`. Each returned a canonical path of the
form `/root/phase_coord_probe/<role>`, identified its parent and intended role, and reported the
same working directory as the root task. No child created a descendant, no self-fork appeared, and
no child hung. The minimum repeated anti-fork sentence was `Do not spawn descendants.`

The context experiment also exposed a limitation. `fork_turns="all"`, `"none"`, and `"3"` changed
the requested history boundary, but every delegate still received repository/system constraints
and enough surrounding task metadata to characterize them as inherited context. Therefore
`fork_turns="none"` does not mean "blank process context"; exact task identity, role, permitted
artifact set, tested hypothesis, and terminal condition still belong in the explicit delegation
prompt. All three delegates independently named the missing tested question or fork setting as an
ambiguity when it was omitted.

This is positive mechanics evidence for one bounded chain, not a reliability measurement across
retries, concurrent writers, interruption, or failure recovery.

### G4. A Codex worktree isolates files and index, but not landing responsibility

Official documentation states that app worktree tasks use Git worktrees: files are separate while
Git metadata is shared. App-managed worktrees normally start at detached `HEAD`; a task can be
handed between Local and Worktree, and one branch cannot be checked out in two worktrees at once.
Codex prunes older managed worktrees subject to retention protections and snapshots changes before
deletion. The local environment showed one app-managed detached worktree under
`$CODEX_HOME/worktrees` alongside the primary branch checkout, matching the documented model.

Project evidence records three attribution/index failures that isolation addresses:

1. TFW-54 recorded sibling-task file contamination in a shared index.
2. TD-144 records a broad add/commit that captured sibling deletions into the wrong task commit.
3. TD-178 records Phase E README rows landing in an unrelated TFW-58 commit.

The first two are prevented by a separate worktree/index. The third demonstrates the residual
cost: isolation does not itself produce an attributable landing commit. Exact-path review and a
deliberate landing/handoff remain necessary. Sources: [Codex Git worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees),
[`knowledge/risk.md`](../../../../../knowledge/risk.md), and
[`tasks/DEBT-SNAPSHOT.md`](../../../../../tasks/DEBT-SNAPSHOT.md).

### G5. Current `dispatch` is an index, not a transport transcript

The journal grammar records a `dispatch` when work is handed to a named participant, but its common
schema contains only time, kind, accountable human, producer, references, and an optional one-line
summary. The event body must not copy chat or artifact content. Consequently `dispatch` plus ONB,
RF, and REVIEW can reconstruct who was assigned, what durable artifacts resulted, and what was
accepted; it cannot reconstruct the exact delegation payload unless the referenced role artifact
contains the required scope and decisions. The RDP ONB field case does preserve the executor's
understanding, blocking questions, coordinator answers, and corrections, but this is semantic
reconstruction rather than a byte-for-byte message transcript.

Sources: [`event.md`](../../../../../.tfw/templates/journal/event.md) and the existing RDP ONB field
case referenced by the master HL.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Two distinct coordination planes; one successful bounded nested probe; documented and observed worktree mechanics; three repository contamination/attribution cases; the actual `dispatch` evidence boundary. | Reliability across repeated/concurrent trials, controlled user-visible task creation, interrupt recovery, and a timed landing-cost benchmark. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?

Stage complete: YES
→ User decision: Standing direction applied: focused mode, no questions; proceed to Extract.
