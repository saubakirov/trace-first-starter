# Briefing
> Parent: [HL-TFW-42](../../HL-TFW-42__research_cycle_restructure.md)
> Goal: Determine how TFW should present multi-agent research orchestration to users via iterations.yaml.

## Research Plan

**Gather:**
- External research: how existing multi-agent frameworks handle agent assignment (CrewAI, AutoGen, LangGraph, MetaGPT)
- Analyze AFD-2 production data: what drove agent selection for each iteration
- Map AI tool strengths/weaknesses for research subtasks (web research, code audit, server recon, synthesis)
- Identify dimensions: agent selection mechanism, iteration dependency model, briefing granularity

**Extract:**
- Build configuration space from agent selection × dependency model × briefing approach
- Cross-reference with AFD-2 empirical patterns to identify which combinations actually occurred
- Compare TFW's coordinator-driven model vs automated orchestration approaches

**Challenge:**
- Stress-test surviving configurations against edge cases: single-agent projects, 3+ agent projects, agent unavailability
- Counter-evidence: when does explicit agent assignment add overhead without value?
- Test H1: can `agent` field in iterations.yaml handle all observed patterns, or do we need a separate mechanism?

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | Multi-agent orchestration needs `agent` field in iterations.yaml, not a separate mechanism | open |

## Scope Intent
- **In scope:** How TFW presents multi-agent research to coordinators. Schema design for iterations.yaml `agent` field. UX patterns for agent selection (auto-detect vs ask vs document-only). Empirical validation from AFD-2.
- **Out of scope:** Actual tool integration code. Runtime agent dispatch. Tool-specific capabilities beyond research context.

## Guiding Questions
1. What granularity of agent guidance is useful without being prescriptive? (field-level: just name vs structured profile with strengths)
2. Should iterations.yaml encode WHY an agent was chosen (rationale), or just WHO (name)?
3. Is the `depends_on` field between iterations sufficient for expressing agent handoff patterns?

## User Direction
User directive: proceed autonomously in deep mode. No questions to user — self-answer from AFD-2 evidence and external research.

Self-answers to guiding questions (based on HL context):
1. AFD-2 used agent names only (`antigravity`, `codex`). Rationale was implicit in the `focus` field. Suggest: agent name + optional `agent_rationale` or encode rationale in existing `brief` field.
2. The `focus` field already captures WHY. Agent field captures WHO. Separation of concerns aligns with TFW principles.
3. `depends_on` expresses iteration sequencing. Agent handoff = side-effect of different agents being assigned to dependent iterations. No separate handoff mechanism needed.

---
Stage complete: YES
