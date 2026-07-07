# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW-45](../../HL-TFW-45__multi_agent_workflows.md)
> Goal: Validate whether swarm mode has genuine quality advantage (H1), determine the right abstraction (H8), and resolve the fresh context vs lost nuance trade-off (H9).

## Predecessor (iter1)

Reference: [iter1/RES.md](../iter1/RES.md)

**Decisions to build on:**
- D1: Custom sub-agent type for Antigravity (not `self`) — Mindset = TRUE system prompt
- D2: Workflows/Skills ≠ system prompt on any platform
- D3: `swarm.md` is platform-agnostic protocol, not executable code
- D4: `.agent/rules/` is the ONLY user-controllable true system prompt in Antigravity
- D7: 4 surviving configurations (C2 Antigravity custom, C4 Claude agent, C7 Codex TOML, C9 single-agent fallback)

**Open threads from iter1:**
1. H1 empirical test: fresh agent with Mindset-as-system-prompt vs single-agent mindset switch
2. H8: mode file (`swarm.md`) vs `execution_model` abstraction
3. H9: honesty of fresh context vs loss of conversation nuance
4. Token budget for `define_subagent.system_prompt`

## Research Plan

### Gather — Evidence for H1, H8, H9
- H1: Search for evidence on persona prompting in system prompt vs user message. LLM research on role-playing persistence, anchoring bias from conversation history, cognitive mode switching. Does system-prompt-level identity produce measurably different outputs than conversation-level instruction?
- H8: Compare mode file pattern (focused.md, deep.md — changes parameters) vs execution_model pattern (changes pipeline structure). How do other frameworks handle this? Is `mode` the right abstraction or does swarm need its own concept?
- H9: What does a fresh agent LOSE from conversation history? What does predecessor stage output AS INPUT provide? Is the delta (lost nuance) significant for investigative workflows specifically? Sequential stage dependencies (Gather→Extract→Challenge)
- Token budget: What are known limits for system prompts in Gemini/Claude/GPT? Can 300-400 words of Mindset + TFW loading fit?

### Extract — Design space for swarm.md
- Build configuration space: mode file vs execution_model vs hybrid
- Map the information flow: what each stage agent receives as input (predecessor output, TFW context, Mindset) vs what it loses (conversation history, user corrections, implicit knowledge)
- Evaluate: does the "clean slate" model work for all 4 research stages, or does Briefing need special treatment (coordinator writes it, not a spawned agent)?

### Challenge — Stress test the swarm model
- Attack H1: what if system-prompt persona is just as "simulated" as conversation-context persona? What evidence would falsify H1?
- Attack H9: construct a scenario where lost conversation context causes the Challenge stage to miss something the Gather stage's agent discussed with the user
- Attack H8: does adding a third mode (`swarm`) to `focused`/`deep` create combinatorial complexity? Should swarm be orthogonal to focused/deep?

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | A fresh sub-agent with Mindset as system prompt produces qualitatively different (more genuine) output than the same agent switching mindsets mid-conversation — the "clean slate" eliminates anchoring bias from previous stages | needs-research |
| H8 | Mode file (like focused/deep — changes parameters) is the right abstraction for swarm, rather than a separate execution_model concept (changes how the whole pipeline runs) | needs-research |
| H9 | The trade-off "honesty of fresh context" vs "loss of nuance from conversation history" resolves in favor of fresh context for investigative workflows — predecessor output as input is sufficient | needs-research |

## Scope Intent
- **In scope:** H1 evidence (theoretical + structural), H8 abstraction design, H9 trade-off analysis, swarm.md content sketch, mode interaction model (swarm × focused/deep)
- **Out of scope:** Adapter implementation details (TFW-45 TS scope). Actual empirical A/B test of H1 (would need a separate experiment task). Review workflow swarm specifics (Phase B — builds on Phase A patterns)

## Guiding Questions
1. Is there LLM research evidence that system-prompt-level persona produces meaningfully different outputs than user-message-level persona? Or is this an assumption we can't validate without running our own experiment?
2. Should `swarm` be a third mode alongside `focused`/`deep`, or should it be orthogonal (any mode can be swarm or single-agent)?
3. What's the minimal information a Challenge agent needs from Gather+Extract to do its job — full stage files or a summary?

## User Direction
- Q1: H1 = hypothesis without proof. Plan: empirical A/B test on helpdesk project (old review vs new multi-agent review, across Claude Code + Antigravity). For iter2: theoretical/structural evidence only.
- Q2: Mode model is OPEN. Options user sees: (a) separate commands, (b) multi-agent by default in new version (break backward compat). User: "не знаю, проверять надо." This IS the research question.
- Q3: Deferred to researcher.
- Key user signal: willing to break backward compatibility if multi-agent is genuinely better. This changes the design space — C9 (single-agent fallback) might not be a hard requirement if user accepts breakage.

---
Stage complete: YES
