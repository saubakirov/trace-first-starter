# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260902-111644_CRATM](../../HL-TFW_20260902-111644_CRATM.md)
> Goal: Determine whether Codex can carry an inspectable coordinator-to-delegate chain, with git worktree isolation and task-local delegation traces, without adding a TFW runtime.

## Configuration Space

The raw cross-product is 4^4 = 256 rows. The table retains the architecturally distinct,
non-contradictory combinations needed to expose every alternative at least once; variants that
only substitute a weaker durable trace are represented by C1, C5, and C8.

| Config | D1: coordination topology | D2: workspace isolation | D3: delegation payload | D4: durable trace |
|--------|---------------------------|-------------------------|------------------------|-------------------|
| C1 | one task, no child | shared checkout and index | inherited conversation | chat/task history only |
| C2 | bounded sub-agent tree inside one task | shared checkout and index | task reference plus explicit read set | role artifacts plus `dispatch` |
| C3 | bounded sub-agent tree inside one task | shared checkout and index | explicit artifact bundle | child-produced files plus landing commit |
| C4 | bounded sub-agent tree inside one task | read-only delegate with no checkout mutation | task reference plus explicit read set | TFW `dispatch` journal event |
| C5 | separate user-visible Codex tasks | shared checkout and index | plain prompt only | chat/task history only |
| C6 | separate user-visible Codex tasks | separate git worktree | explicit artifact bundle | child-produced files plus landing commit |
| C7 | separate user-visible Codex tasks | detached worktree | task reference plus explicit read set | child-produced files plus landing commit |
| C8 | nested phase coordinator with its own delegates | shared checkout and index | inherited conversation | role artifacts plus `dispatch` |
| C9 | nested phase coordinator with its own delegates | shared checkout and index | explicit artifact bundle | child-produced files plus landing commit |
| C10 | nested phase coordinator with its own delegates | separate git worktree | explicit artifact bundle | child-produced files plus landing commit |
| C11 | nested phase coordinator with its own delegates | detached worktree | task reference plus explicit read set | child-produced files plus landing commit |
| C12 | nested phase coordinator with its own delegates | read-only delegate with no checkout mutation | task reference plus explicit read set | role artifacts plus `dispatch` |

## Findings

### E1. Topology and filesystem isolation are independent

The controlled probe established a nested parent/child topology but every participant reported the
same working directory. The official worktree model associates an isolated checkout with a Codex
task selected to run in a worktree; it does not establish one worktree per nested subagent. Thus C8
and C9 are technically possible but share an index, while C10 and C11 require the coordinator to
establish and communicate an explicit workspace boundary. A chain diagram alone cannot prove
isolation.

### E2. Context inheritance is not a complete delegation payload

All three probe variants received repository/system constraints even when conversation inheritance
was set to none. Conversely, each delegate noticed a task-specific omission when the tested
hypothesis or fork setting was absent. The viable minimum payload is therefore semantic, not a
history-size setting:

1. exact parent and destination role;
2. task ID and current workflow stage;
3. bounded objective and tested hypothesis;
4. authoritative artifact references or explicit read set;
5. workspace and mutation boundary;
6. expected return artifact or message;
7. terminal condition and descendant policy;
8. existing task ID to reuse when continuity matters.

`Do not spawn descendants.` prevented unintended grandchildren in one controlled trial. It should
be paired with exact child count and names because the trial did not test ambiguous positive
instructions such as "form a team" or "continue the chain."

### E3. The durable trace alternatives form an audit ladder

| Trace choice | Reconstructs assignment | Reconstructs understood scope | Attributes repository result | Survives empty task output |
|--------------|-------------------------|-------------------------------|------------------------------|----------------------------|
| chat/task history only | yes, inside Codex | usually | no | no |
| `dispatch` only | yes, if refs identify both ends | only a short summary | no | partly |
| role artifact + `dispatch` | yes | yes, if ONB/RF/REVIEW states it | result artifact, not necessarily commit | yes |
| child files + landing commit | yes when paired with `dispatch` | yes when paired with role artifact | yes | yes |

The non-obvious viable configuration is C4/C12: read-only research or review can use bounded nested
delegation without paying worktree or landing cost. Mutation-bearing execution cannot inherit this
economy.

### E4. Worktree cost is bounded but has two components

The documented app control plane supports thread start/resume/fork/read/list, status, steering, and
interruption; parent and ancestor filters make hierarchy inspectable. The documented worktree plane
adds checkout creation and Local/Worktree handoff. Repository evidence adds a separate landing cost:
exact-path review and an attributable commit or merge. These are operational steps, not a daemon or
new TFW runtime. C6/C7/C10/C11 pay both costs in exchange for removing shared-index contention.

Source used in this stage: [Codex app-server API overview](https://learn.chatgpt.com/docs/app-server#api-overview).

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Twelve distinct viable configurations, a semantic minimum delegation payload, an audit ladder, and the separation between topology and isolation. | Adversarial elimination under wrong-target, silent-child, detached-HEAD, and incomplete-trace failures. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?

Stage complete: YES
→ User decision: Standing direction applied: focused mode, no questions; proceed to Challenge.
