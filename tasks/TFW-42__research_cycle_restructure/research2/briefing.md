# Briefing — Iteration 2
> Parent: [HL-TFW-42](../../HL-TFW-42__research_cycle_restructure.md)
> Goal: Map agent capabilities for research subtasks and formalize how TFW guides coordinators in agent selection.

## Predecessor Context (from iter 1)

**Decisions to build on:**
- D1: `agent` field = free-text string, optional → we now need to answer WHAT the coordinator writes in this field and WHY
- D6: Framework guidance = prompt-in-template → we now need to design the actual prompt/guidance content
- D7: Agent purpose = traceability, not dispatch → guidance should inform, not automate

**Open threads from iter 1:**
- FC3 identified 3 agent archetypes (Web Researcher, Code Auditor, Infra Operator) but didn't validate externally
- No external research on actual tool capabilities (Claude Code, Codex CLI, Antigravity-class tools)
- "Prompt-in-template" (D6) was decided but the template content wasn't designed

## Research Plan

**Gather:**
- External research: documented capabilities of Claude Code, Codex CLI (Gemini), Cursor, Windsurf, Aider — what makes each unique for research
- Map research subtask types to tool strengths (web search, code analysis, file traversal, MCP integration, context window, synthesis)
- Analyze: where should guidance live in TFW? (conventions vs template vs workflow)

**Extract:**
- Build capability matrix: tool × research subtask type
- Cross-reference with formalization options: where does this matrix live in TFW?
- Design concrete template/guidance text

**Challenge:**
- Stress-test: will capability guidance become stale as tools evolve?
- Counter-evidence: does prescriptive guidance conflict with TFW's tool-agnostic philosophy?
- Edge case: what if a user has only 1 tool available?

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | Multi-agent orchestration needs `agent` field in iterations.yaml, not a separate mechanism | confirmed (iter 1) — iter 2 extends: what guidance accompanies the field? |

## Scope Intent
- **In scope:** Tool capability mapping for research. Formalization location (where guidance lives). Concrete template/comment text. Human-choice vs recommendation model.
- **Out of scope:** Tool installation/setup. Runtime integration. Non-research tool usage (execution, review).

## Guiding Questions
1. Should TFW name specific tools (Claude Code, Codex) or use generic archetypes (Web Researcher, Code Auditor)?
2. Where does capability guidance live without becoming a maintenance burden?
3. How prescriptive should the guidance be — "consider using X for Y" vs "X is best for Y"?

## User Direction
User feedback (triggering iter 2): «мы не ответили на вопрос для чего и каких случаев каких агентов лучше использовать claude gemini codex, и как это лучше формализовать, рекомендовать что-то или человек сам выбирает или что?»

Key signal: user wants ACTIONABLE guidance, not just a schema field. The coordinator should know WHEN to consider switching agents and WHY.

---
Stage complete: YES
