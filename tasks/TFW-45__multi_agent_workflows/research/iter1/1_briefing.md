# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW-45](../../HL-TFW-45__multi_agent_workflows.md)
> Goal: Determine whether multi-agent spawn mechanics across Antigravity, Claude Code, and Codex support TFW's swarm mode design — fresh agent per investigative stage with Mindset as system prompt.

## Research Plan

### Gather — Cross-platform capabilities audit
- Antigravity: `define_subagent` / `invoke_subagent` API — system_prompt mechanics, `self` vs custom type inheritance, `.agent/rules/` propagation, Skills system current state, what changed since April 2026
- Claude Code: teamwork / `Task.spawn` / max effort — how sub-tasks get system prompts, CLAUDE.md inheritance, slash command behavior in sub-tasks, current best practices
- Codex: agent spawn mechanism (if exists), context model, constraints — or confirm no spawn capability and document fallback implications
- For ALL platforms: What becomes system prompt vs context? How is project knowledge inherited by sub-agents? Token budget for system prompts?
- Candidate dimensions expected: [platform × spawn mechanism × context inheritance × system prompt composition × stage isolation level]

### Extract — Configuration Space
- Build cross-platform comparison matrix: what each platform provides for the 5 dimensions above
- Identify which dimension combinations are platform-specific vs platform-agnostic
- Map the design space: where does one `swarm.md` cover all platforms, where does it need platform-specific branches?

### Challenge — Assumption testing
- Test: does `define_subagent` system_prompt ACTUALLY create identity-level behavior or is it just another context block?
- Test: what happens when sub-agent lacks TFW context (conventions, glossary) — degradation pattern?
- Counter-evidence: are there documented cases where sub-agent system prompts are ignored or overridden?
- Counter-argument: is the "fresh agent" advantage real, or does losing conversation history cost more than it gains?

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H2 | Antigravity `define_subagent` with custom `system_prompt` is sufficient to inject both Mindset identity AND TFW context loading instructions | needs-research |
| H3 | `self` subagent type inherits `.agent/rules/` (including tfw.md and agents.md), making TFW context available automatically | needs-research |
| H4 | Antigravity workflows (`.agent/workflows/*.md`) become system-level instructions when invoked (not just context) | needs-research |
| H5 | Antigravity has changed since April 2026 — TFW-30 findings need correction | needs-research |
| H6 | Claude Code teamwork/Task.spawn uses a similar model to Antigravity define_subagent — one swarm.md covers both | needs-research |
| H7 | Codex has an analogous spawn mechanism — or it doesn't and needs fallback | needs-research |

## Scope Intent
- **In scope:** Platform spawn mechanics, system prompt composition, context inheritance, current state of each platform's sub-agent API. What has changed since TFW-30 (April 2026). Skills and workflow invocation mechanics in Antigravity.
- **Out of scope:** Empirical quality comparison (H1 — iter2). Mode file vs execution_model abstraction (H8 — iter2). Honesty vs context loss trade-off (H9 — iter2). Actual swarm.md writing (that's TS/execution). Review workflow specifics (Phase B — reuses Phase A patterns).

## Guiding Questions
1. For Antigravity specifically: when a workflow from `.agent/workflows/` is invoked, does it become part of the system prompt or is it injected as user-turn context? This determines whether Role Lock in workflows has enforcement weight.
2. Are there platform-specific constraints on system_prompt length/complexity for sub-agents that would limit how much TFW context we can inject?
3. Should research prioritize any platform over others, or is equal depth across all three required for iter1?

## User Direction
- Q1: System prompt vs context for workflow invocation — **unknown, wants to learn the truth**
- Q2: Platform priority — **equal depth across all 3 (Antigravity, Claude Code, Codex)**
- Q3: Core concern (user emphasis): "Вызов слэш команды, скилла, воркфлоу — равносильно ли системному промпту или нет?" — this question applies to ALL platforms, not just Antigravity. This is the #1 research priority.

---
Stage complete: YES
