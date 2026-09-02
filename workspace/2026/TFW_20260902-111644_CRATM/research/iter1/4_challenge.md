# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260902-111644_CRATM](../../HL-TFW_20260902-111644_CRATM.md)
> Goal: Determine whether Codex can carry an inspectable coordinator-to-delegate chain, with git worktree isolation and task-local delegation traces, without adding a TFW runtime.

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|-------------|-------------|-------------|-------------|------------------|
| D1 | one task, no child | D4 | child-produced files plus landing commit | There is no child to produce or attribute the files. |
| D2 | read-only delegate with no checkout mutation | D4 | child-produced files plus landing commit | A read-only delegate cannot create files or a landing commit. |
| D3 | plain prompt only | D1 | nested phase coordinator with its own delegates | It omits the task, child-count, authority, and terminal bounds needed to distinguish delegation from reproduction. |
| D4 | chat/task history only | D1 | separate user-visible Codex tasks | It fails the task-local inspectability goal when task output is empty, inaccessible, or split by recovery. |
| D4 | `dispatch` only | D3 | plain prompt only | Neither side preserves the delegate's understood scope, authoritative inputs, or return contract. |

**Surviving configurations:**

| Config | D1 | D2 | D3 | D4 | Notes |
|--------|----|----|----|----|-------|
| C2 | bounded sub-agent tree | shared checkout | task reference + explicit read set | role artifacts + `dispatch` | Survives only for read-only roles or one serialized mutation owner. |
| C3 | bounded sub-agent tree | shared checkout | explicit artifact bundle | child files + landing commit | Survives only with serialized writers and exact-path landing. |
| C4 | bounded sub-agent tree | read-only delegate | task reference + explicit read set | `dispatch` | Empirically exercised; suitable for bounded probes, not implementation. |
| C6 | separate Codex tasks | separate worktree | explicit artifact bundle | child files + landing commit | Strong mutation-bearing baseline. |
| C7 | separate Codex tasks | detached worktree | task reference + explicit read set | child files + landing commit | Requires explicit branch/handoff/landing instructions. |
| C9 | nested phase coordinator | shared checkout | explicit artifact bundle | child files + landing commit | Survives only if the phase coordinator serializes all mutation. |
| C10 | nested phase coordinator | separate worktree | explicit artifact bundle | child files + landing commit | Strong full-chain candidate; descendants share the phase task's worktree unless separately isolated. |
| C11 | nested phase coordinator | detached worktree | task reference + explicit read set | child files + landing commit | Same as C10 plus detached-HEAD landing control. |
| C12 | nested phase coordinator | read-only delegate | task reference + explicit read set | role artifacts + `dispatch` | Strong low-cost research/review configuration. |

**Eliminated configurations:** C1 does not exercise delegation; C5 combines an underspecified prompt,
a shared index, and no repository trace; C8 combines implicit history with nested authority and a
shared index. They remain technically executable but do not satisfy this research goal.

**Unexpected survivor:** C12. A read-only nested chain gives inspectable specialization without a
worktree or landing operation. It should not be generalized to an executor.

## Findings

### C1. The anti-self-fork result is instruction-sensitive and under-sampled

The exact instruction `Do not spawn descendants.` held for three children, and exact child names
produced the intended canonical paths. This rejects the claim that Codex necessarily self-forks in
a coordinator chain. It does not establish that written instructions generally remove the failure:
there was one coordinator trial, no intentionally ambiguous control prompt, no interruption, and
no retry. H1 is therefore **conditionally supported for mechanics**, not proven reliable.

The minimum safe grammar is: exact number and names of children; explicit "do not fork yourself"
and "children do not spawn descendants" constraints; reuse an existing task ID when applicable;
and a terminal condition. Positive authority to create children must never be inferred from a role
name alone.

### C2. Silence is not evidence of failure

The existing user-visible task chain contained empty/silent app responses while repository traces
continued to change. Replacing the delegate immediately risks duplicate work and multiple task IDs
for one role; one reviewer recovery already exhibited that split. A coordinator should wait once,
inspect the named durable artifact and workspace, then steer or interrupt the same task before
replacement. This is a coordination protocol, not a liveness service.

### C3. Worktree isolation solves index contention, not merge correctness

The official worktree guide confirms separate file copies and indexes, a shared Git object store,
detached `HEAD` by default, and the one-branch-per-worktree constraint. It also confirms that
managed worktrees may be deleted after snapshotting and that ignored local files move only through
`.worktreeinclude`. Failure cases that remain after isolation are stale-base conflicts, detached
commits without a named landing path, missing ignored dependencies, broad landing commits, and
cleanup before the result is made durable.

H3 is **supported for index isolation** by Git mechanics and the project failures, but its economic
phrase "merge cost lower" was not benchmarked. The defensible bound is qualitative: one explicit
worktree/handoff plus one exact-path landing step replaces three already recorded contamination or
attribution incidents. Source used in this stage:
[Codex Git worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees).

### C4. `dispatch` needs referenced semantic evidence

`dispatch` by itself cannot carry the exact payload: its summary is capped at 120 code points and
the journal forbids copying artifact or chat content. H6 survives only when the event references a
role artifact that states at least destination participant/task, workflow role, bounded scope,
authoritative inputs, workspace mode, expected return, and continuity instruction. ONB records the
delegate's interpreted contract; RF/REVIEW records the returned and assessed result. Exact message
transport remains available in task history but is not required as the durable project record.

### C5. Vocabulary can remain non-colliding

Official Codex terminology distinguishes a **task/thread**, a **subagent**, and a **subagent
workflow**. The project can reserve **stage-level swarm** for TFW-45 and use **task-level role
assignment** for independently addressable Codex tasks. This supports H2's coexistence boundary
without deciding TFW-61 transport. The distinction must be explicit in HL refinements because the
generic phrase "team mode" hides both planes.

### C6. H7 and H8 lack Codex-side causal evidence

This iteration did not migrate role fields, so it cannot test whether `organization_role` plus
`project_role` is non-breaking (H7). It also did not compare a fresh reviewer with the producing
participant on the same revision (H8). Existing separate reviewer tasks prove addressability, not
freshness advantage. Both remain deferred rather than converted into positive findings.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Nine conditional survivors; C6/C10 as mutation-bearing baselines; C4/C12 as low-cost read-only baselines; explicit limits on H1, H3, and H6. | Repeated reliability trials, timed merge/landing benchmark, H7 migration evidence, and H8 controlled comparison. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Pairwise incompatibility checked? Surviving configurations listed?

Stage complete: YES
→ User decision: Standing direction applied: focused mode, no questions; synthesize RES.
