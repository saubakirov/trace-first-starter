# RES — TFW_20260902-111644_CRATM: Codex coordination and worktree mechanics (Iteration 1)

> **Date**: 2026-09-03
> **Author**: Codex (Researcher) · on behalf of `saubakirov`
> **Status**: 🔬 RES — Iteration 1 complete
> **Parent HL**: [HL-TFW_20260902-111644_CRATM](../../HL-TFW_20260902-111644_CRATM.md)
> **Mode**: Pipeline · `focused` · run without questions at the owner's instruction

---

## Research Context

Iteration 1 measured the Codex side of the frozen HL's coordination design: whether a coordinator
can route work through a phase coordinator to researcher, executor, and reviewer roles; which
context a delegate actually receives; whether written bounds prevent accidental self-forking; what
worktree isolation does and does not solve; and whether the existing `dispatch` plus role artifacts
is a sufficient durable trace. The evidence combines official Codex documentation, the enabled
local build, existing app task history, a controlled read-only nested delegation probe, and three
recorded repository contamination/attribution failures. It introduces no runtime, liveness service,
lock, or new artifact class.

## Briefing

[`1_briefing.md`](1_briefing.md) defined four independent dimensions: coordination topology,
workspace isolation, delegation payload, and durable trace. The completed evidence and analysis are
in [`2_gather.md`](2_gather.md), [`3_extract.md`](3_extract.md), and
[`4_challenge.md`](4_challenge.md).

Primary external sources:

- [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Codex app-server API overview](https://learn.chatgpt.com/docs/app-server#api-overview)
- [Codex Git worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Model Codex coordination as two planes: an in-task subagent tree and independently addressable user-visible tasks | The first has canonical parent/child paths and shares the parent task's checkout by default; the second has stable task IDs and can be placed in an app-managed worktree. Official docs and the local surfaces expose both (G1–G3) |
| D2 | Treat coordination topology and Git isolation as independent | The controlled nested chain succeeded while every participant reported the same working directory. A child relationship is not worktree evidence (G3, E1) |
| D3 | Use an explicit semantic delegation envelope regardless of history inheritance | `fork_turns` bounds conversation history, not repository/system instructions. Delegates still needed exact role, task, hypothesis, artifact set, mutation boundary, return, descendant policy, and terminal condition (G3, E2) |
| D4 | Bound anti-self-fork instructions by exact child count and names, plus `Do not spawn descendants.` | Three sequential child roles obeyed that sentence and no unintended child appeared. One trial establishes workable mechanics, not general reliability (G3, C1) |
| D5 | Use a worktree for a mutation-bearing autonomous task; allow read-only subagents to share the task checkout | Separate worktrees remove shared-index contention. Read-only C4/C12 avoid both contention and landing cost. Nested children are not automatically isolated from one another (E1, E4, C3) |
| D6 | Make landing an explicit exact-path operation after isolated work | Two recorded failures are shared-index contamination; a third is wrong-commit attribution. A worktree prevents the first class, not the third (G4, C3) |
| D7 | Treat `dispatch` as an index into semantic evidence, not as a transport transcript | The journal summary is deliberately short and cannot copy artifacts or chat. ONB/RF/REVIEW must carry understood scope, returned result, and assessment (G5, E3, C4) |
| D8 | On silence, inspect the named durable artifact and workspace, then steer or interrupt the same task before replacement | Existing field history contained empty responses alongside continuing filesystem evidence; premature replacement split one reviewer role across multiple task IDs (G2, C2) |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Which Codex coordination operations are documented, exposed, and observed? | ✅ closed | Subagent spawn/route/wait and task start/read/list/steer/interrupt are documented and exposed. This iteration observed nested spawn/wait and read existing task chains; it did not create or interrupt a user-visible task (G1–G3) |
| Q2 | What explicit payload prevents role and parent ambiguity? | ✅ closed for a conservative baseline | Use D3's eight-field semantic envelope and D4's exact descendant bound. Reliability under ambiguous prompts remains unmeasured (E2, C1) |
| Q3 | Does worktree isolation address the three recorded corruptions at acceptable cost? | 🟡 qualitative answer | It structurally prevents the two shared-index cases and makes parallel file changes independent. It does not prevent wrong landing attribution. One handoff/branch step plus one exact-path landing step is the bounded cost; elapsed effort was not benchmarked (G4, C3) |
| Q4 | Is `dispatch` plus role artifacts sufficient for auditability? | ✅ closed with conditions | Yes for semantic reconstruction when the event references artifacts containing destination, role, scope, inputs, workspace, return, and continuity. No for exact message replay, which remains task-history evidence (G5, C4) |
| Q5 | How reliable is the full chain under interruption, retry, concurrent writers, and a dead child? | 🟡 open | One read-only controlled trial and one historical field chain do not provide a rate. The design must retain conservative recovery and single-mutation-owner constraints (C1–C3) |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | Codex can carry the full coordinator → phase coordinator → researcher, executor, reviewer chain reliably enough that written instructions remove self-forking without a TFW runtime | open | 🟡 **mechanics supported; reliability unproven** | One nested read-only trial created the intended three direct children with correct canonical paths, role recognition, no descendant, and no hang. Existing task history demonstrates a visible coordinator/phase/delegate chain but also silence and recovery splits. No ambiguous-control or failure trial was run (G2–G3, C1–C2) |
| H3 | A worktree per autonomous run removes index contention at a merge cost lower than the three measured corruptions it prevents | open | 🟢 **isolation supported; cost only bounded qualitatively** | Official Git-worktree mechanics and a local detached worktree establish independent files/index. TD-144 and the TFW-54 case are prevented; TD-178 still requires exact landing attribution. No timed cost comparison was run (G4, E4, C3) |
| H6 | `dispatch` plus role artifacts make delegation inspectable, so narrower-than-workflow handoffs need not be prohibited | open | 🟢 **supported with a minimum evidence envelope** | `dispatch` identifies the event and references; ONB/RF/REVIEW can preserve interpreted scope, result, and assessment. The transport payload itself is not reproduced and need not be if the semantic fields in D3/D7 are durable (G5, E3, C4) |
| H2 | Session-level team mode and stage-level TFW-45 swarm can coexist without vocabulary collision while Phase A avoids deciding TFW-61 transport | open | 🟢 **supported as a terminology boundary** | Official terminology distinguishes task/thread, subagent, and subagent workflow. Reserve task-level role assignment and stage-level swarm as separate project terms; do not use undifferentiated “team mode” (G1, C5) |
| H7 | `organization_role` and `project_role` are the right two context dimensions and do not require a breaking migration | open | ⚪ **not tested** | No profile migration or consumer compatibility test was in the Codex mechanics scope (C6) |
| H8 | A fresh participant outperforms the producing participant on a revision round | open | ⚪ **not tested** | Separate reviewer addressability is observed, but no controlled same-work comparison measured freshness advantage (C6) |

## HL Update Recommendations

> The researcher classifies. The researcher never applies.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 | Replace inference about current Codex capability with the measured environment: `codex-cli 0.151.0-alpha.7.2`; `multi_agent` stable/enabled; `multi_agent_v2` disabled; documented subagent and task controls listed separately | G1–G2 |
| R2 | §2 | Record the controlled nested trial: three sequential named children, correct parent paths and roles, common working directory, no descendants or hangs. State sample size one and read-only scope | G3, C1 |
| R3 | §7.2 | Define two provider-neutral coordination planes: in-task subagent tree versus independently addressable task. Do not let “team mode” imply workspace isolation or user-visible task creation | G1, E1, C5 |
| R4 | §7.2 | Add the minimum delegation envelope from D3 and anti-self-fork grammar from D4. Require an explicit destination/role even when conversation context is inherited | E2, C1 |
| R5 | §8 | State the measured worktree dependency: an app-managed worktree is normally detached, tied to one chat, shares Git metadata, and permits a branch in only one worktree. Nested subagents share the task checkout unless another boundary is explicitly created | G4, E1, C3 |
| R6 | §9 | Add silent/degraded task output and recovery duplication as a risk. Mitigation: wait once; inspect the referenced durable artifact and workspace; steer or interrupt the same task; replace only after evidence of termination; record the new task ID if replacement occurs | G2, C2 |
| R7 | §9 | Add residual worktree risks: stale base, detached commit without a landing path, ignored dependency absent from the worktree, cleanup before durable landing, and broad landing that reintroduces attribution error | G4, C3 |
| R8 | §9 | Add parallel-write conflict inside one task/worktree. Mitigation: one mutation owner per worktree, serial role changes where children share a checkout, and read-only parallelism for research/review | G1, E1, C3 |
| R9 | §10 H1 | Mark mechanics conditionally supported, not reliable. Preserve the required follow-up: repeated trials covering ambiguous prompts, interruption, retry, dead child, and concurrent writers | C1–C2 |
| R10 | §10 H3 | Split the claim: index isolation supported; lower merge cost not quantitatively tested. Record the qualitative bound of one workspace handoff/branch step plus one exact-path landing step against three historical incidents | G4, C3 |
| R11 | §10 H6 | Mark supported only when `dispatch` references semantic evidence containing destination participant/task, workflow role, bounded scope, authoritative inputs, workspace mode, expected return, and continuity instruction | G5, C4 |
| R12 | §10 H2/H7/H8 | Mark H2 supported at the vocabulary boundary; leave H7 and H8 untested by this iteration. Do not convert separate reviewer addressability into evidence for reviewer freshness | C5–C6 |
| R13 | §11 | Add the agent-measured insight: delegation, isolation, context transport, and durable trace are four independent controls. A provider capability label cannot stand in for any one of them | D1–D7, E1–E4 |

### Amendment Proposals — frozen sections, owner verdict required

**No amendment proposals.** The evidence refines capability, dependency, risk, and hypothesis
status. It does not invalidate a frozen declarative claim at the HL's granularity.

## Fact Candidates

**No fact candidates.** The owner's no-question instruction is already recorded in the Briefing;
all substantive findings are agent-discoverable from documentation, environment, and project
traces.

> fact-candidates: processed 2026-09-05

## Strategic Insights (Research)

**No strategic insights.** No human domain briefing occurred in this iteration.

## Findings Map

```text
                              delegated role
                                    |
                         Does it mutate the repo?
                           /                  \
                         no                    yes
                         |                      |
             bounded subagent tree      one mutation owner
             same task checkout                |
             explicit read set          isolated task worktree
                         |              /                   \
                  dispatch + role   attached/branch       detached HEAD
                     artifact             |                    |
                         |           exact-path landing   branch/handoff +
                   no merge cost          commit          exact-path landing
                         \                  |                    /
                          \_________________|___________________/
                                            |
                                  durable result reference

       Orthogonal controls: topology × workspace × payload × durable trace
       A child path proves topology; only Git state proves isolation.
```

## Iteration Status

- **Iteration:** 1 of 2 (min) / 5 (max), per `research/iterations.yaml`
- **Hypotheses tested:** H1 (mechanics conditionally supported, reliability unproven), H2 (terminology boundary supported), H3 (isolation supported, cost qualitative), H6 (supported with evidence envelope)
- **Hypotheses deferred:** H7 (requires profile migration/consumer test); H8 (requires controlled same-work reviewer comparison)
- **Gaps discovered:** user-visible task creation and interruption were not exercised; no ambiguous prompt control; no concurrent writer or dead-child trial; no timed merge/landing benchmark; current `dispatch` grammar alone cannot preserve the semantic envelope
- **Superseded decisions:** None

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|----------------|-----------------|
| 1 | Repeat the full nested chain under ambiguous positive instructions and injected child failure | Distinguishes one successful bounded script from reliable coordination | Measure wrong-child, self-fork, timeout, steer, interrupt, and replacement behavior over multiple runs |
| 2 | Mutation-bearing task in an isolated worktree through landing | H3's remaining claim is the operational cost and attribution boundary | Time creation/handoff/verification/landing; verify exact commit attribution and stale-base handling |
| 3 | Semantic envelope fit within existing artifacts | H6 depends on durable fields, while `dispatch` must remain short | During TS, map each required field to `dispatch` refs, ONB, RF, and REVIEW without adding an artifact class |
| 4 | H7 and H8 | Neither is evidenced by Codex mechanics | Leave to the iteration or phase explicitly assigned to migration compatibility and fresh-participant comparison |

### Recommendation

- [x] **SUFFICIENT** — the assigned Codex mechanics focus is sufficient for the coordinator to compare with the independent iteration and proceed to `/tfw-plan`
- [ ] MORE NEEDED
- [ ] BLOCKED

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Codex can execute the intended nested shape without a TFW runtime: one controlled phase
coordinator created the three named role children, preserved the parent hierarchy, and produced no
self-fork or hang. The result is deliberately narrower than H1's reliability wording. It was one
read-only trial, while the existing user-visible field chain showed silent outputs and recovery
splits. Worktrees structurally remove shared-index contention, but descendants do not receive one
automatically and landing attribution remains a separate obligation. `dispatch` plus role artifacts
is sufficient when it indexes an explicit semantic envelope; `dispatch` alone is not a transcript.
The planning value of this iteration is the four-control model and its conservative configurations:
C4/C12 for read-only delegation, C6/C10 for mutation-bearing tasks, and a single mutation owner per
worktree. **Self-critique:** no user-visible task was created or interrupted, no child failure was
injected, the worktree path was inspected rather than run through a timed landing, and one trial
cannot supply a reliability rate. The RES therefore recommends implementable bounds and explicit
remaining tests, not a universal capability guarantee.

---

*RES — TFW_20260902-111644_CRATM: Codex coordination and worktree mechanics (Iteration 1) | 2026-09-03*
