# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW-45](../../HL-TFW-45__multi_agent_workflows.md)
> Goal: Collect evidence for H1 (fresh agent quality), H8 (mode abstraction), H9 (context trade-off).

## Dimensions

| Dimension | Alt A | Alt B | Alt C |
|-----------|-------|-------|-------|
| D1: Persona injection level | System prompt (identity) | High-priority context (`<system-reminder>`) | User-turn instruction |
| D2: Mode model for swarm | Third mode alongside focused/deep | Orthogonal axis (swarm × focused/deep) | Default for all (no fallback) |
| D3: Inter-stage information passing | Full predecessor stage files | Structured summary/handoff | Predecessor RES only |
| D4: Backward compatibility | Hard requirement (C9 preserved) | Soft (graceful degradation) | Break allowed (multi-agent by default) |

## Findings

### G1: H1 — System prompt persona vs conversation-context persona

**External research evidence:**

1. **System prompt gets higher weight:** Models are trained to give system instructions higher attention weight than user messages. System prompt = persistent constraint that shapes ALL responses; user message = variable input processed within system prompt's framework.

2. **Persona inconsistency in research (Peh et al., 2024/2025):** Systematic evaluations show persona injection does NOT consistently improve performance on objective/factual tasks vs neutral control. "Double-edged sword" — can enhance domain reasoning but also degrade or produce random effects depending on specificity.

3. **Key nuance for TFW:** TFW Mindset personas are NOT "be a helpful expert" generic roles. They are FUNCTIONAL role-nouns (Strategist/Explorer/Analyst/Critic) on two non-overlapping axes (convergent↔divergent, build↔break). TFW-43 D1 established this. Research shows highly specific, domain-tailored personas > generic roles. TFW's personas fit this criterion.

4. **Anchoring bias evidence (strong for H1):** LLMs are highly susceptible to anchoring — relying too heavily on information encountered early in the interaction. In single-agent mode, the Explorer's Gather findings ANCHOR the Analyst's Extract and Critic's Challenge. Standard mitigations (CoT, "ignore the hint") are insufficient for deep-seated anchoring. This is the strongest theoretical argument for fresh agents.

**Structural argument for H1 (not just persona):**

The fresh-agent advantage is NOT primarily about persona. It's about **eliminating anchoring bias from conversation history**:
- Single agent: Explorer finds X → Extract sees X in conversation → Analyst builds on X (anchored)
- Multi-agent: Explorer's output becomes Extract's INPUT (file), but without the exploration journey, dead ends, user corrections, implicit agreements. The Analyst sees ONLY the structured output, not the cognitive path.

**Conclusion for H1:** Theoretically plausible with structural evidence (anchoring bias, attention dilution, "Lost in the Middle" effect). BUT no direct empirical proof that TFW stages specifically benefit. User's plan (helpdesk A/B test) is the right path. For iter2: treat as **structurally justified hypothesis** — implement with expectation of empirical validation later.

### G2: H9 — Fresh context vs lost nuance

**"Context rot" evidence (favors fresh):**
- "Lost in the Middle" effect: models prioritize beginning and end of context, losing middle information
- Attention dilution: longer conversation = less focused responses
- Cascade of errors: early mistakes compound, model becomes cautious
- Task interference: switching tasks in single thread → old context bleeds into new

**What does the fresh agent LOSE?**

| Lost | Example in TFW research | Impact |
|------|------------------------|--------|
| User corrections | "No, I meant X not Y" during Gather | Medium — correction is in stage file output but not the reasoning that led there |
| Implicit agreements | User said "ok" to a direction during Gather | Low — if important, it's in Briefing's User Direction |
| Dead ends explored | "I searched for Z but found nothing useful" | **Positive loss** — dead ends shouldn't anchor next stage |
| Emotional/tonal context | User's enthusiasm or skepticism about a direction | Low — stage files capture decisions, not feelings |
| Cross-stage conversation nuance | The WHY behind a Gather finding that isn't in the stage file | Medium — depends on stage file quality |

**What does predecessor output AS INPUT provide?**

| Provided | Mechanism |
|----------|-----------|
| Structured findings | Stage file (e.g., `2_gather.md`) — dimensions table, findings, checkpoint |
| Decisions made | Explicit in stage file |
| Hypotheses status | Updated in stage file |
| User direction | Briefing file captures this |
| Scope | Briefing file captures this |

**Key insight:** The quality of inter-stage transfer depends on STAGE FILE QUALITY, not conversation history. If the Gather file is comprehensive (as TFW templates enforce with structured sections), the Extract agent has everything it needs. If the Gather file is sloppy, even a single-agent would struggle because the conversation is too long to hold.

**Resolution for H9:** ✅ Fresh context wins for investigative workflows. Predecessor stage files + Briefing provide sufficient context. The "lost nuance" is either: (a) captured in structured output, (b) irrelevant (dead ends), or (c) low-impact (emotional context). The risk of anchoring bias from conversation history outweighs the risk of losing nuance.

### G3: H8 — Mode file vs execution_model vs default

**Current TFW mode model:**
- `focused.md` — 1 OODA loop, quick scan
- `deep.md` — up to N OODA loops, hypothesis-driven
- Mode selected at Step 2 of `research/base.md`
- Mode changes PARAMETERS (loops, verification depth) not STRUCTURE

**What would swarm change?**
Swarm doesn't change parameters — it changes WHO RUNS the stages. This is fundamentally different from focused vs deep. It's not "how many loops" but "same agent or different agents."

**Three design options:**

**(A) Third mode:** `swarm.md` alongside `focused.md`/`deep.md`
- Pro: simple, fits existing pattern
- Con: false equivalence — swarm is orthogonal to focused/deep. A swarm agent still needs to know if each stage runs focused or deep

**(B) Orthogonal axis:** `swarm × focused`, `swarm × deep`
- Pro: correct modeling — swarm is about execution model, not investigation depth
- Con: combinatorial — 2 axes = 4 combinations. Config complexity increases

**(C) Multi-agent by default:** New version = always multi-agent if platform supports it
- Pro: simplest user experience — no mode selection for swarm
- Con: backward compatibility broken for single-agent platforms. Token cost increase (every stage = new agent)
- User signal: "willing to break backward compatibility if genuinely better"

**Industry pattern (external):** "Start with single-agent, introduce execution model abstraction when complexity requires it." Multi-agent should be opt-IN, not default — until empirically proven better (H1 unvalidated).

**Key realization:** Swarm is NOT a mode. It's an **execution model**. Modes (focused/deep) describe HOW DEEP to investigate. Execution model describes WHO investigates. These are independent axes:

```
                  focused    deep
single-agent:     current    current
multi-agent:      swarm+     swarm+
                  focused    deep
```

### G4: Token budget for system_prompt

**Findings:**
- System instructions are part of the total context window (200K–1M+ tokens for current models)
- 300-400 words ≈ 400-500 tokens — trivially small vs context window
- Antigravity's current system prompt is already ~5000+ tokens (identity, rules, workflows, skills, etc.)
- Sub-agent system_prompt of 400-500 tokens = <1% of even a 200K context window

**Verdict:** Token budget is NOT a constraint. 300-400 words of Mindset + TFW loading instructions fits easily.

### G5: Inter-stage information passing — what to pass

**Best practice (external):** "Information hygiene" — pass only essential data between agents, not full conversation. Use structured artifacts (JSON, markdown tables, spec files).

**TFW already does this.** Stage files ARE structured artifacts:
- `2_gather.md` = Dimensions table + Findings + Checkpoint
- `3_extract.md` = Configuration Space + Findings + Checkpoint
- `4_challenge.md` = Consistency Check + Surviving Configs + Findings

**What each stage agent should receive:**

| Stage | Receives as input | Why |
|-------|------------------|-----|
| Gather | Briefing file (1_briefing.md) | Scope, hypotheses, research plan |
| Extract | Briefing + Gather file | Needs Gather's Dimensions to build Configuration Space |
| Challenge | Briefing + Gather + Extract files | Needs both to do pairwise consistency checks |

**Full stage files, not summaries.** TFW stage files are already structured — they ARE the summary. Adding a summary-of-summary step loses information unnecessarily.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Anchoring bias = strongest theoretical argument for H1 | Empirical validation (helpdesk test — out of scope) |
| "Context rot" evidence supports fresh agents (H9 ✅) | |
| Swarm ≠ mode — it's an execution model, orthogonal to focused/deep | Whether "execution_model" is the right config name |
| Token budget NOT a constraint | |
| Stage files = sufficient inter-stage transfer | |
| User willing to break backward compatibility | Whether to break or not (design decision) |

**Sufficiency (deep mode):**
- [x] External source used? (5 web searches — persona research, anchoring bias, context rot, orchestration patterns, token limits)
- [x] Briefing gap closed? (H1, H8, H9 all have evidence)
- [x] Dimensions identified? (4: injection level, mode model, info passing, backward compat)
- [x] Hypothesis tested? (H1 structurally justified, H8 orthogonal axis, H9 fresh wins)
- [x] Counter-evidence sought? (persona inconsistency research — double-edged sword)
- [x] Metacognitive check: NEW insight — swarm is not a mode but an execution model. This reframes H8 entirely ✅

Stage complete: YES
→ User decision: ___
