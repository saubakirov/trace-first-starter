# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW_20260902-111644_CRATM](../../HL-TFW_20260902-111644_CRATM.md)
> Goal: Determine whether Codex can carry an inspectable coordinator-to-delegate chain, with git worktree isolation and task-local delegation traces, without adding a TFW runtime.

## Research Plan

### Gather
- Measure the Codex surfaces available in this session for task creation, sub-agent delegation, follow-up, waiting, interruption, and worktree placement.
- Inspect official OpenAI documentation for the documented relationship between Codex tasks, subagents, worktrees, and parent-child coordination.
- Inspect project traces that record prior Codex delegation and worktree behaviour, especially ONB and review evidence rather than design claims.
- Decompose the choices into independent dimensions: coordination topology, workspace isolation, delegation payload, and durable trace boundary.

### Extract
- Cross-reference the dimensions into viable coordination configurations rather than treating “Codex team mode” as one indivisible capability.
- Compare documented capability, capability exposed to this session, and behaviour directly observed during the iteration.
- Identify the smallest instruction set that prevents accidental self-forking while preserving intentional child delegation.
- Price worktree isolation against merge and landing overhead using the three recorded trace-corruption cases.

### Challenge
- Attack H1, H3, and H6 with failure cases: wrong delegation target, parent/child ambiguity, dead child, detached HEAD, dirty sibling work, and incomplete handoff context.
- Test the vocabulary boundary against TFW-45, TFW-58, and TFW-61 without deciding their subjects.
- Evaluate H7 and H8 only where Codex-side evidence exists; leave cross-vendor claims to independent iteration 2.
- Eliminate configurations that require a TFW runtime, shared liveness state, implicit authority, or unrecorded transport assumptions.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | Codex can carry the full chain — coordinator → phase coordinator → researcher, executor, reviewer — reliably enough that written instructions remove self-forking, without any TFW-side runtime. | open |
| H3 | A worktree per autonomous run removes index contention at a merge cost lower than the three measured corruptions it prevents. | open |
| H6 | `dispatch` plus the role artifacts make a delegation inspectable, so narrower-than-workflow handoffs need not be prohibited to stay auditable. | open |
| H2 | Session-level team mode and stage-level TFW-45 swarm can coexist without vocabulary collision, while Phase A avoids deciding TFW-61 transport. | open — Challenge |
| H7 | `organization_role` and `project_role` are the right two context dimensions and do not require a breaking migration. | open — Challenge |
| H8 | A fresh participant outperforms the producing participant on a revision round. | open — bounded Codex-side evidence only |

## Scope Intent
- **In scope:** Codex task and sub-agent mechanics; parent/child routing; what context a delegate receives; worktree creation and detached-HEAD behaviour; merge/landing cost; `dispatch` and existing role artifacts as the durable delegation trace; explicit failures and instruction-sensitive behaviour.
- **Out of scope:** Claude capability and cross-vendor communication (iteration 2); branch policy or merge strategy (TFW-61); revise-loop ownership and re-entry semantics (TFW-58); stage-level swarm design (TFW-45); any runtime, scheduler, daemon, liveness registry, lock service, or new artifact class; edits outside `research/iter1/`.

## Guiding Questions
1. Which Codex coordination operations are documented, exposed, and empirically usable here, and which of those three sets differ?
2. What exact payload and instruction boundary lets a coordinator create the intended child instead of accidentally reproducing itself or losing task context?
3. Does worktree isolation remove the measured index-contamination risk at an acceptable, explicitly bounded landing cost?

## User Direction
The owner selected iteration 1 and instructed the researcher to ask no questions. Use `focused` mode and concrete defaults, report mechanics including failures, and reserve all owner-facing choices for the coordinator after RES synthesis.

---
Stage complete: YES
