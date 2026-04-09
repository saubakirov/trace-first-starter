# Research Briefing — TFW-31: Quick Start Agent-First

**Mode:** focused
**Date:** 2026-04-09

## Research Goal

Design a Quick Start that works for a complete newcomer who:
- Has never seen TFW before
- May barely know how to use AI agents
- At best has Claude Code installed

The curl approach sends init.md to an agent without context — the agent doesn't know the repo URL, what TFW is, or why it exists.

## Hypotheses

| # | Hypothesis | Status |
|---|-----------|--------|
| H1 | Sending just init.md via curl is sufficient for agent onboarding | ❌ Refuted |
| H2 | The oh-my-openagent pattern translates directly to TFW | ❌ Refuted — OMO is installable software (npm/bun), TFW is a methodology |
| H3 | We need a dedicated "agent-readable" landing document | 🔬 Investigating |

## Guiding Questions

1. What's the actual first-contact journey for a newcomer?
2. What must the agent know BEFORE running init.md?
3. How do we bridge "human discovers TFW" → "agent sets it up"?

## Scope

- IN: Quick Start section design, agent onboarding document
- OUT: init.md rewrite (only small patches), docs site changes
