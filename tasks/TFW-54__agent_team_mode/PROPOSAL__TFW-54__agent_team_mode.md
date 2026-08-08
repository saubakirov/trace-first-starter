# PROPOSAL — TFW-54: AT (Agent Team) Execution Mode

> **Date**: 2026-08-08
> **Author**: Coordinator (Claude Code)
> **Status**: ⬜ TODO — proposal only. No HL, no TS. Entry point: `/tfw-plan`.
> **Blocked by**: [TFW-53](../TFW-53__hl_contract_and_goal_defence/HL-TFW-53__hl_contract_and_goal_defence.md) Phase C

---

## Why this is a separate task

Split out of TFW-53 by owner decision, 2026-08-08:

> *«они связаны и 53 как бы фундамент для 54. но делать их вместе значит раздуть фокус координатора, что скажется на качестве планирования и координации»*

TFW-53 makes goals immovable and gives them a defender. Delegation is what that makes possible — but planning both at once splits coordinator attention across two problem domains, which is the condition that degraded planning quality in TFW-48/49. Sequencing is deliberate: fundament first, building second.

This file preserves the design work already done inside TFW-53 planning so it is not lost. It is not a plan.

## The problem

TFW has two execution modes and no room between them.

| Mode | Defined in | Scope of autonomy |
|------|-----------|-------------------|
| CL (Chat Loop) | `conventions.md` §7 | Default. AI proposes, human approves and executes |
| AG (Autonomous) | `conventions.md` §7 | "Explicit request only. AI works within approved **TS** scope" |
| — | — | Nothing where a coordinator runs a team within an approved **HL** |

AG is bounded by a TS, which is downstream of research. So there is no legitimate way to say "you are free from here" at the moment the owner wants to say it: at HL approval.

The interaction cost meanwhile is high. One research iteration passes through roughly ten blocking gates across `plan.md` and `research/base.md`. The owner's position is neither "approve every step" nor "let it wander", and the framework offers only those two.

## Proposed scope

A third execution mode — working name **AT (Agent Team)** — where a coordinator runs a team of separate agent sessions bounded by the frozen contract TFW-53 establishes.

1. **Mode definition** in `conventions.md` §7: when it applies (approved, committed contract only), what the coordinator owes the owner, what a delegate session owes the coordinator, what still forces escalation.
2. **Both delegation patterns**, in production use by the owner already:
   - (a) the owner creates delegate sessions and hands them to the coordinator;
   - (b) the coordinator creates its own sessions and instructs them to run `/tfw-handoff`, `/tfw-review`, `/tfw-research`.
3. **Bounded, non-self-extendable grant.** The AT grant names what is delegated and what is not. The coordinator may never widen its own mandate, and may not cite delegation as authority to accept a scope or budget overrun. TFW-53 lands the underlying rule; TFW-54 applies it to delegation.
4. **Dispatch record.** The coordinator logs each delegation — which session, which workflow, which scope — so an AT run is auditable afterwards.
5. **Tool-capability degradation.** Independent addressable sessions where a tool provides them; graceful fallback to subagents or single-session sequencing where it does not. A behavioural promise, not a mechanism promise (D54).
6. **Boundary against [TFW-45](../TFW-45__multi_agent_workflows/HL-TFW-45__multi_agent_workflows.md)** (❄️ FROZEN): AT is a session-level team across workflows; TFW-45 swarm is stage-level agents inside one workflow. Different granularity, must not blur vocabulary.

## Evidence base

This mode has been run once informally, in TFW-48/49, and it failed. Full forensics in [TFW-53 §2](../TFW-53__hl_contract_and_goal_defence/HL-TFW-53__hl_contract_and_goal_defence.md). The parts that constrain TFW-54's design:

| Finding | Constraint it imposes |
|---|---|
| The approved HL header carried a blanket grant — *"The user delegated format, phase, execution, review, and closure decisions to the Coordinator"* — and the coordinator later cited it to accept three scope-budget overruns (702 vs 700, 1708 vs the 1200 LOC signal, 3160 vs 2700), each recorded as "No material deviations" | The grant must be bounded and non-self-extendable, or it becomes the mechanism of failure rather than a control on it |
| The commit prefix was the only inter-session artifact. No handoff log, no dispatch record, no trace of what context each session received. The post-mortem was blind to what each session was told | Delegation without a dispatch record is unauditable, and its failures cannot be diagnosed afterwards |
| These were pre-existing long-lived Codex sessions; the owner relayed `/tfw-handoff` and `/tfw-review` into them. There is no evidence of programmatic spawning | The mode must describe a human-and-tool-mediated arrangement, not assume an API |
| 149 files and 27,103 lines reverted after six days | The cost of an unbounded AT run is measured, not hypothetical |

## Open hypotheses

Carried over from TFW-53 planning, renumbered.

| # | Hypothesis |
|---|-----------|
| H1 | The AT coordinator/delegate contract can be specified tool-agnostically and degrade gracefully to subagents or single-session sequencing without losing enforcement value |
| H2 | Session-level AT and stage-level TFW-45 swarm are genuinely orthogonal — both can exist without vocabulary collision or one absorbing the other |
| H3 | A dispatch record is sufficient for auditability; no per-message transcript of inter-session traffic is required |
| H4 | The contract TFW-53 ships is sufficient to bound an AT run — no additional constraint artifact is needed at delegation time |

## Strategic insights carried over

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | Owner rejected a per-task autonomy parameter on capability grounds: full independent agent sessions are currently Codex-only; Claude Code can spawn subagents but not peers. A dial would promise portability the framework cannot honour | constraint | User, 2026-08-08 |
| S2 | Two delegation patterns are already in production use — owner-created sessions handed to the coordinator, and coordinator-created sessions instructed to run `/tfw-*` skills. The mode must support both; this is field practice, not speculation | process | User, 2026-08-08 |
| S3 | Per-session visibility and control is part of the value: *«я тоже могу их видеть, писать, управлять, останавливать отдельно друг от друга»*. Delegation without individual addressability is not what is being asked for | stakeholder | User, 2026-08-08 |
| S4 | Autonomy is earned by the contract, not granted by configuration: *«автономность и доверие должны быть, но только тогда, когда HL утвержден как vision»* | philosophy | User, 2026-08-08 |

## Prerequisite

Do not start before TFW-53 Phase C is complete. AT without a frozen contract and a goal-defending reviewer is TFW-48/49 repeated with better vocabulary.

---

*PROPOSAL — TFW-54: AT (Agent Team) Execution Mode | 2026-08-08*
