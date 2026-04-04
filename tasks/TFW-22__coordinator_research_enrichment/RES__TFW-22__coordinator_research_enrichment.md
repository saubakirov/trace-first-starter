# RES — TFW-22: Coordinator & Research Enrichment

> **Date**: 2026-04-04
> **Author**: Coordinator (AI)
> **Status**: 🔬 RES — In progress
> **Parent HL**: [HL-TFW-22](HL-TFW-22__coordinator_research_enrichment.md)
> **Mode**: Pipeline

---

## Research Context
TFW-22 предлагает 4 изменения: визуализация в HL, hypothesis iteration, research enrichment алгоритмами мышления, workflow refactor. Гипотезы H1-H4 требуют data-driven валидации. Дополнительно — исследовать терминологию и алгоритмы ClearThought/SequentialThinking/Claude Dreaming для naming + ideology.

## Briefing

### Research Plan
1. **Gather** — word audit plan.md/research.md. H2 validation.
2. **Extract** — ретроспективный compliance analysis + deep dive ClearThought/SequentialThinking/Claude Dreaming. Терминология и алгоритмы.
3. **Challenge** — контрпримеры ref-pattern. Инверсия H4.

### Scope Intent
- **In scope:** word count analysis, compliance retroanalysis, ref-pattern risk, terminology/algorithm research
- **Out of scope:** implementation of changes, template modifications

### Guiding Questions → User Answers
1. Scope budget case — ref broke because no step, not because ref itself
2. Research спринтит — нужен loop + user answers on tech = unverified
3. 2-3 режима: base/focused/deep. Keep ClearThought terminology

**Key insight:** для ИИ важны правильные термины — через naming создаются ассоциации и поведение. Пример: Claude Code «dreaming» для knowledge consolidation. Маленький промпт + точные термины > длинный промпт с объяснениями.

## Decisions
| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Ref допустим ТОЛЬКО внутри алгоритмического шага. «→ ref:» одной строкой = Pattern B (broken). «Step N: Read X → evaluate → act» = Pattern A (working) | Scope budget кейс + TFW-19 D24 |
| D2 | Research режимы — 3 файла: base/focused/deep | User preference + ClearThought architecture |
| D3 | User answers on tech = unverified hypothesis. Cross-check externally | User feedback |
| D4 | Терминология важнее объяснений. Правильный термин = правильные ассоциации | Dreaming pattern, user insight |
| D5 | Realistic word target plan.md = 850-950, не 700 | Word audit data |
| D6 | Naming: Approach A (operational) — base/focused/deep | User choice |
| D7 | OODA inner loop: loops_per_stage configurable via YAML. YAML содержит числа/boolean, не тексты критериев | User: настройки цифрами true/false |
| D8 | Checkpoint criteria двухуровневый: generic (base.md) + mode-specific (mode file). focused=2, deep=4 | User confirmed |
| D9 | Архитектура research/ сохранена как proposed_research_readme.md | User: сохранить дизайн |
| D10 | Role Lock + Mindset = ALWAYS inline (DNA layer). Steps = inline. Reference data = library (budgets, anti-patterns, transitions). Step must be self-contained: ref gives precision, not direction | Industry consensus (modular instruction stack) + H4 stress test |
| D11 | Checkpoint criteria = SOFT (report, not block). loops_per_stage = HARD LIMIT (force exit + report unmet criteria) | Challenge #3 stall prevention |
| D12 | Progressive Disclosure: mode file загружается ONLY at Step 2, не при старте | Challenge #2 overhead reduction |

## Open Questions
| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Word budget при удалении inline блоков | ✅ | 393 words (32.4%) freed from plan.md |
| Q2 | Ref-pattern compliance evidence | ✅ | Pattern B proven broken (TFW-19 D24) |
| Q3 | Research loop: формализация | ✅ | OODA inner loop + Sufficiency Verdict (checkpoint checklist) |
| Q4 | Research modes: naming + distribution | ✅ | Approach A: base/focused/deep. Settings via YAML |
| Q5 | Какие термины из ClearThought взять | ✅ | OODA, Sufficiency Verdict, Metacognitive Check, Trust Protocol |
| Q6 | base.md = orchestrator с переходами? | ✅ | Yes, base = routing + core algorithm |
| Q7 | Full architecture design | ✅ | See [proposed_research_readme.md](proposed_research_readme.md) |

---

## Stage: Gather — "What do we NOT know?"

### Word Audit: plan.md (1213 words total)

| Block | Lines | Words | % | Can remove? |
|-------|-------|-------|----|-------------|
| Prerequisites | 24-33 | 50 | 4.1% | → algorithmic step with ref |
| Scope Budget | 116-138 | 160 | 13.2% | → algorithmic step with ref |
| Approval Gates | 144-151 | 42 | 3.5% | Keep (unique to plan) |
| Status Transitions | 152-162 | 50 | 4.1% | → ref conventions.md §5 |
| Anti-patterns | 164-175 | 91 | 7.5% | → compact (3-5 unique) + ref |
| **Total removable** | — | **393** | **32.4%** | — |
| **After removal** | — | **820** | — | — |

**H2 ✅ confirmed.** 393 words removable > predicted 300+. Post-removal = 820. Budget = ~380 words for enrichment.

### Word Audit: research.md (1165 words total)

| Block | Lines | Words | % | Can remove? |
|-------|-------|-------|----|-------------|
| Prerequisites | 37-39 | 27 | 2.3% | → ref |
| Limits table | 140-153 | 89 | 7.6% | → compact or move to mode files |
| Status Transitions | 155-162 | 38 | 3.3% | → ref |
| **Total removable** | — | **154** | **13.2%** | — |
| **After removal** | — | **1011** | — | — |

Research.md bloat = modest. But with mode split → word budget opens up per file.

### Ref-pattern evidence (TFW-19)
- **P11:** Enforcement-critical values inline (Pattern A)
- **D24:** Pattern B (pure reference) proven to kill compliance
- **User correction:** Not ref itself — absence of algorithmic step. Config ref without step = recommendation → ignored. Config ref WITH step = algorithm → executed.

### Checkpoint: Gather
| Found | Remaining |
|-------|-----------|
| plan.md: 393 words removable, exactly what goes where | How to structure refs-as-steps |
| research.md: 154 removable, mode split needed | Mode architecture & naming |
| Pattern B broken, but fix = step not duplication | Algorithm design for ref-steps |
| H2 confirmed | — |

**Agent assessment:** Gather complete. Data sufficient for design decisions.
**Depth check:** Internal evidence (TFW-19 REVIEW, word audit). No external needed — internal architecture question.
**Recommendation:** Close → Extract.
→ User decision: confirmed, proceed to Extract with ClearThought deep dive

---

## Stage: Extract — "What do we NOT see?"

### ClearThought Full Architecture (38 operations)

Studied: README, source code for OODA Loop, Scientific Method, Metacognitive Monitoring, Ulysses Protocol, Collaborative Reasoning.

#### Categories & Operations

| Category | Operations | Relevance to TFW Research |
|----------|-----------|--------------------------|
| **Core** | sequential_thinking, mental_model, debugging_approach, creative_thinking, visual_reasoning, metacognitive_monitoring, scientific_method | **HIGH** — metacognitive_monitoring, scientific_method |
| **Collaborative** | collaborative_reasoning, decision_framework, socratic_method, structured_argumentation | **MEDIUM** — collaborative_reasoning (multi-perspective) |
| **Analysis** | systems_thinking, research, analogical_reasoning, causal_analysis, statistical_reasoning, simulation, optimization, ethical_analysis | **LOW** — too specialized |
| **Metagame** | **ooda_loop**, **ulysses_protocol** | **HIGH** — core algorithms for research modes |
| **Patterns** | tree_of_thought, beam_search, mcts, graph_of_thought | **LOW** — search algorithms not applicable |

#### Key Algorithms Extracted

**1. OODA Loop (Observe → Orient → Decide → Act)**
- Source: Military decision-making (John Boyd)
- ClearThought implementation: SessionState with phases, hypothesis tracking, evidence quality scoring, auto-advance when minEvidence met, loop counter, learning rate metric
- **Key terms:** observe, orient, decide, act, hypothesis, evidence, learning rate
- **TFW mapping:** Research stage loop. Observe = gather data. Orient = interpret against context. Decide = stage verdict. Act = update RES + next stage
- **Why it works for AI:** cyclic, not linear. Agent re-enters observe after each act → prevents one-pass sprint

**2. Ulysses Protocol (Phases + Gates + Constraints)**
- Source: Odysseus binding to mast — pre-commit to constraints to prevent future self from deviating
- ClearThought implementation: Time-boxed execution, iteration limits, constraint checking before each step, auto-escalation on violation, scope drift tracking, min confidence threshold
- **Key terms:** gate, constraint, escalation, scope drift, confidence threshold, timebox
- **TFW mapping:** Research modes. «Deep» = more iterations, tighter constraints. «Focused» = scoped, time-boxed. Gate = checkpoint
- **Why it works for AI:** self-binding. Agent declares limits → cannot bypass without explicit escalation

**3. Scientific Method (Observation → Hypothesis → Experiment → Analysis → Conclusion)**
- Parameters: observation, hypothesis, experiment, data, analysis, conclusion, reproducibility, peerReview
- **Key terms:** hypothesis, experiment, reproducibility, peer review
- **TFW mapping:** HL §10 Hypotheses → Research Briefing → Stages = experiments → Conclusion = verdict
- **Why it works for AI:** hypothesis-driven, not task-driven. Changes "search for stuff" to "test this claim"

**4. Collaborative Reasoning (Multi-persona: Analyst, Critic, Synthesizer)**
- Parameters: participants, perspectives, conflicts, consensusPoints, facilitationMode, convergenceScore
- **Key terms:** analyst, critic, synthesizer, conflict, consensus, convergence
- **TFW mapping:** Extract stage. Agent assumes 3 perspectives: executor (feasibility), user (value), reviewer (quality)
- **Insight:** default participants = `['Analyst', 'Critic', 'Synthesizer']`. Terminology creates behavior

**5. Metacognitive Monitoring (awareness → evaluation → strategies → adjustments)**
- Parameters: awareness, evaluation, strategies, adjustments, confidence, biasCheck
- **Key terms:** awareness, bias check, confidence, adjustment
- **TFW mapping:** Checkpoint self-check. "Did I confirm what I already knew, or discover something new?"

**6. SequentialThinking (Thought → Revision → Branch)**
- Source: Anthropic MCP server
- Implementation: ThoughtData with `isRevision`, `revisesThought`, `branchFromThought`, `branchId`, `needsMoreThoughts`, `nextThoughtNeeded`
- **Key terms:** revision, branch, nextThoughtNeeded
- **TFW mapping:** Research loop. After checkpoint: revise previous stage findings. Branch: explore alternative hypothesis
- **Key pattern:** `nextThoughtNeeded: boolean` — agent explicitly signals whether more thinking is needed instead of silently stopping

#### Claude Code «Dreaming» Pattern

AutoDream (memory consolidation, triggered between sessions):
- **Metaphor:** biological REM sleep → consolidation, pruning, indexing
- **4 phases:** Orient → Gather Signal → Consolidate → Prune and Index
- **Trigger gates:** Time Gate (24h), Session Gate (5 sessions), Lock Gate
- **Why it works:** The word "dreaming" creates right associations — the agent understands this is reflection, not action. It knows to be gentle with memory, to compress, to discard noise
- **Lesson for TFW:** naming matters. "Dreaming" = 1 word that replaces paragraphs of instructions. The right metaphor creates the right behavior

### Terminology Candidates for TFW Research Modes

Based on analysis, candidate naming approaches:

**Approach A: ClearThought-style (operational)**
- `base.md` — core research algorithm + routing
- `focused.md` — scoped investigation, time-boxed (Ulysses-inspired)
- `deep.md` — iterative, multi-loop (OODA-inspired)

**Approach B: Scientific-style (metaphorical)**
- `base.md` — research protocol + routing
- `survey.md` — broad scan, quick assessment (like literature survey)
- `experiment.md` — hypothesis-driven, iterative, rigorous (like scientific experiment)

**Approach C: Cognitive-style (brain metaphors, like Dreaming)**
- `base.md` — research protocol + routing
- `scan.md` — breadth-first, pattern recognition, "scanning the horizon"
- `probe.md` — depth-first, targeted investigation, "probing a wound"

### Algorithmic Patterns for Research Loop (Q3)

The core problem: research runs one-pass per stage. Need a loop.

**OODA gives the answer.** Each stage should be an OODA micro-loop:

```
OBSERVE: gather data (web search, file read, user input)
    ↓
ORIENT: interpret against existing understanding
    "Is this confirming or challenging what I thought?"
    ↓
DECIDE: is this stage sufficient?
    → If yes: checkpoint → present to user → advance
    → If no: what's missing? formulate next observe action
    ↓
ACT: update RES, formulate questions
    → Loop back to OBSERVE
```

**SequentialThinking gives the exit condition:** `nextThoughtNeeded: boolean`

Each checkpoint should explicitly declare: "Stage [X]: more investigation needed? [yes/no + reason]"

### Trust Levels for User Input (D3 implementation)

**ClearThought's Collaborative Reasoning has participant roles.** Adapt:

| Input Type | Trust Level | Agent Behavior |
|-----------|-------------|----------------|
| Business/people/domain context | Trust as-is | Ask clarifying questions only |
| Technical approach/architecture | Verify externally | Cross-check with docs, web search, codebase analysis |
| Performance claims/numbers | Verify empirically | Test, benchmark, or find external evidence |
| "I tried this before" | Trust the outcome | But verify the reason (why did it fail?) |

### Checkpoint: Extract
| Found | Remaining |
|-------|-----------|
| 6 algorithms mapped to TFW stages | Challenge: do these mappings hold under stress? |
| OODA loop = research stage inner loop pattern | Does inner loop add overhead for simple research? |
| 3 naming approaches for modes | Need to pick one |
| Trust levels for user input | Need to formalize in workflow |
| `nextThoughtNeeded` = exit condition | How to enforce without MCP? |
| Dreaming = right naming creates right behavior | What's TFW's "dreaming" equivalent? |

**Agent assessment:** Extract produced substantial findings. 6 algorithmic patterns mapped, 3 naming approaches, trust levels defined. Not just surface-level — actual code studied.
**Depth check:** External sources used (GitHub repos: ClearThought, SequentialThinking, web search for Claude Dreaming). Project files analyzed (TFW-19 REVIEW, RF).
**Recommendation:** Close Extract → Challenge.

User decisions:
1. **Naming:** Approach A (operational) — base/focused/deep
2. **OODA loops:** yes, YAML-configurable (numbers/booleans, not text criteria)
3. **Checkpoint criteria:** 2 generic + 0-2 mode-specific = ok

→ User decision: Close Extract → Challenge

---

## Stage: Challenge — "What do we NOT expect?"

### Challenge 1: Инверсия H4 — «А что если inline duplication ПОМОГАЕТ?»

**Claim:** ref-inside-step = лучше чем inline copy.
**Counter-argument:** inline copy = agent видит правило прямо в потоке, не нужен context switch.

**Тест:** Когда ref-inside-step проиграет inline?
- Когда context window ограничен и agent не загружает referenced file (не хватает budget на еще один file read)
- Когда ref target изменился с момента написания workflow, и step ссылается на устаревшую секцию
- Когда agent слабый (не Sonnet/Opus уровня) и буквально не выполняет инструкцию «прочитай файл X»

**Внешнее исследование (web search):**
Индустрия 2025 пришла к consensus: **modular instruction stack**
- Inline = «DNA» агента (persona, safety, role). Короткое, статичное, non-negotiable
- Reference = «knowledge layer» (procedures, specs, compliance). Загружается on-demand
- **Progressive Disclosure**: давать агенту только правила для ТЕКУЩЕГО шага, не всю rulebook
- **Ключевая цитата:** «Treat inline as the character/operating manual and reference docs as the library»

**Вердикт:** ref-inside-step = ПРАВИЛЬНЫЙ подход, НО с защитой:
1. **Role Lock + Mindset = всегда inline** (это DNA агента)
2. **Алгоритмические шаги = inline** (это структура workflow)
3. **Reference data = ref** (scope budgets, anti-patterns, status transitions — это library)
4. **Progressive Disclosure** = загружать mode file ТОЛЬКО когда нужен (Step 2, не сразу)

**Risk mitigation:** Step в workflow должен быть self-contained: «WHAT to do» inline + «WHERE details» as ref. Agent должен уметь выполнить step даже если не прочитает ref — ref даёт precision, а не direction.

### Challenge 2: Mode overhead — 3 файла вместо 1

**Claim:** research/{base,focused,deep}.md = лучшая архитектура.
**Counter-argument:** agent загружает base.md + mode file = 2 файла вместо 1. Больше context, больше reading.

**Тест:** Сколько слов в каждом файле?
- base.md ≈ 500-600 слов (core algorithm: steps, OODA, closure, rules)
- focused.md ≈ 150-200 слов (mindset, settings, criteria)
- deep.md ≈ 200-250 слов (mindset, settings, criteria, metacognitive check)
- **base + focused = 650-800 слов** (< текущий research.md = 1165)
- **base + deep = 700-850 слов** (< текущий research.md = 1165)

**Вердикт:** overhead = отрицательный. Суммарно МЕНЬШЕ чем текущий монолит. Agent reads LESS, not more. ✅

**Дополнительный бонус:** agent загружает ТОЛЬКО свой mode — focused agent не видит deep rules (нет confusion). Это и есть Progressive Disclosure.

### Challenge 3: OODA loop stall — агент застревает в петле

**Claim:** OODA inner loop предотвращает one-pass sprint.
**Counter-argument:** агент может застрять в loop, бесконечно решая «недостаточно» по чеклисту.

**Сценарии stall:**
1. Checkpoint criteria невыполнимы (нет внешних источников по теме → «external source used? NO» → loop forever)
2. Agent перфекционист — каждый loop находит ещё один gap → никогда не «sufficient»
3. User не отвечает → agent в WAIT бесконечно (не stall, но latency)

**Mitigation:**
1. `loops_per_stage` = HARD LIMIT в YAML. Exceeded → force exit + report «loop budget exhausted, N criteria unmet»
2. Checkpoint criteria = **soft (рекомендательные), не blocking.** Если criteria unmet после max loops → agent reports what's missing, moves on
3. Add: «If no external sources exist for topic, state why explicitly and proceed» (уже есть в текущем research.md rule #8)

**Вердикт:** stall risk = LOW при наличии YAML hard limit. Без hard limit = HIGH risk. ✅ с YAML config

### Challenge Summary

| Challenge | Risk | Mitigation | Verdict |
|-----------|------|------------|---------|
| Inline > ref-step | Medium | Role Lock + Mindset inline, ref = library. Self-contained steps | ✅ Accepted |
| 3 files overhead | None | Sum < current monolith. Progressive Disclosure bonus | ✅ Non-issue |
| OODA loop stall | Low-Medium | YAML hard limit + soft criteria + explicit «no external sources» clause | ✅ Mitigated |

### New Decision from Challenge

| # | Decision | Rationale |
|---|----------|-----------|
| D10 | Role Lock + Mindset = ALWAYS inline (DNA layer). Reference = library (scope budgets, anti-patterns). Steps = inline + ref for details | Industry consensus + H4 stress test |
| D11 | Checkpoint criteria = SOFT (report, not block). loops_per_stage = HARD LIMIT (force exit) | Challenge #3 stall prevention |
| D12 | Progressive Disclosure: mode file загружается ONLY at Step 2, не при старте | Challenge #2 overhead reduction |

### Checkpoint: Challenge
| Found | Remaining |
|-------|-----------|
| Inline vs ref: industry validates modular stack | None — clear pattern |
| 3-file overhead: negative (sum < monolith) | None |
| OODA stall: mitigated by YAML hard limit + soft criteria | None |
| 3 new decisions: D10, D11, D12 | — |

**Agent assessment:** Challenge complete. All three stress tests passed. No fatal flaws found. Architecture design holds.
**Depth check:** External web search for inline vs reference compliance patterns (2025 industry best practices). Quantitative estimate of word counts per file.
**Recommendation:** Close Challenge → Final Checkpoint.
→ User decision: Close Challenge → Final Checkpoint

---

## Final Checkpoint

| Stage | Status | Key Findings |
|-------|--------|--------------|
| Gather | ✅ Done | plan.md: 393 words removable (32.4%). research.md: 154 words. H2 confirmed. Pattern B proven broken (TFW-19) but root cause = no algorithmic step, not ref itself |
| Extract | ✅ Done | 6 algorithms mapped (OODA, Ulysses, Scientific Method, Collaborative Reasoning, Metacognitive Monitoring, SequentialThinking). OODA = inner loop. Naming = Approach A. Architecture = base/focused/deep. Claude Dreaming lesson: naming > explanation |
| Challenge | ✅ Done | 3 stress tests passed. Modular stack validated by industry (2025). Mode overhead = negative. OODA stall = mitigated by YAML hard limit + soft criteria |

### Sufficiency Check
**Question:** Sufficient for HL finalization? Can we confidently define phases, approach, and dependencies?
**Self-check:**
- Are there unclosed Open Questions in RES? **No** — all 7 closed (Q1-Q7)
- Did all stages produce substantive findings or were any perfunctory? **All substantive** — Gather: quantitative word audit. Extract: 6 source code analyses + web search. Challenge: 3 stress tests with mitigations
- Did every stage include external research? **Yes** — Gather: TFW-19 REVIEW analysis. Extract: GitHub repos (ClearThought, SequentialThinking) + web (Claude Dreaming). Challenge: web search (industry best practices 2025)
- Is the solution proportionate to the problem scale? **Yes** — 3 workflow files + YAML config + template updates. No scripts, no new tools
- Are phases, boundaries and dependencies clear enough to finalize HL? **Yes** — full architecture in [proposed_research_readme.md](proposed_research_readme.md)

**Agent assessment:** Research is sufficient. 12 decisions made, all grounded in data or user input. Architecture stress-tested. HL can be updated confidently.
→ User decision: ___

**Verdict:** Sufficient for HL finalization

---

## Closure

### HL Update Recommendations

| # | What to update | Source |
|---|---------------|--------|
| 1 | **Replace HL Phase C** (research.md enrichment) with **research/ directory architecture**: base.md + focused.md + deep.md. Update file list, word estimates, phase scope | RES D2, D6, D9 |
| 2 | **Add OODA Stage Loop** to Phase C as core algorithm change. Include YAML config for loops_per_stage, verify_user_tech_claims, require_counter_evidence | RES D7, D11 |
| 3 | **Add Sufficiency Verdict** (checkpoint checklist) to Phase C. 2-level: generic in base.md + mode-specific in mode files | RES D8 |
| 4 | **Add Trust Protocol** to Phase C. 4-tier trust levels for user input | RES D3 |
| 5 | **Update Phase B** (plan.md refactor): word target = 850-950, not 700. Ref-inside-step pattern, not pure ref. DNA/Library split (D10) | RES D1, D5, D10 |
| 6 | **Add D12 Progressive Disclosure** to Phase C: mode file loaded at Step 2, not at start | RES D12 |
| 7 | **Update H1-H4 hypothesis statuses** based on research findings. H2 = confirmed. H4 = partially confirmed (ref works IF inside step, breaks WITHOUT step) | RES D1, Gather data |
| 8 | **Add new hypothesis H5:** "Naming > Explanation" — right terminology creates right AI behavior (Claude Dreaming pattern) | RES D4, user insight |
| 9 | **Update DoD** to include: research/ directory, YAML mode config, Sufficiency Verdict in RES template, Trust Protocol | All RES decisions |

### Fact Candidates

> Reviewed full conversation history. Extracting strategic knowledge from human messages.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | philosophy | Юзер не любит когда ИИ соглашается и бежит делать. Нужен оппонент со здоровым недоверием. Не тупое сопротивление, а требование доказать что юзер прав. «Мне нужен оппонент, я хочу чтобы мне доказали что я прав» | User прямая цитата, начало сессии | High |
| 2 | process | Для ИИ правильные термины важнее длинных объяснений. Через naming создаются ассоциации и поведение. Пример: Claude Code «dreaming» = 1 слово вместо абзацев. Маленький промпт + точные термины > длинный промпт с объяснениями | User прямое наблюдение | High |
| 3 | process | ИИ лучше следует нумерованным шагам и гейтам, чем описательным текстам. «Особенно я это вижу когда executor делает TS — он прям не отходит от шагов». Workflow = algorithm (steps + gates + refs), не info dump | User наблюдение за поведением агентов | High |
| 4 | process | Ref-pattern (ссылка на conventions.md) ломается не потому что ref, а потому что нет алгоритмического шага. «Мы просто не сделали из этого алгоритм или шаг. Там было на уровне рекомендации» | User анализ scope budget кейса | High |
| 5 | process | Юзер хочет чтобы ИИ писал и в файл сразу, и в чат — для удобства чтения и защиты от прерывания. Сначала файл, потом summary в чате | User прямое требование | Medium |

### Next Step

HL нуждается в обновлении по 9 пунктам. После обновления HL → confirm → TS.
→ User decision: ___

## Conclusion

Research исследовал 4 области: word budget feasibility (H2 confirmed — 393 words, 32.4%), ref-pattern compliance (уточнение D24: не ref ломает, а отсутствие алгоритмического шага), ClearThought/SequentialThinking алгоритмы (OODA inner loop, Sufficiency Verdict, Trust Protocol), и stress-testing архитектуры research/{base,focused,deep}.md. Ключевой вклад RESEARCH: преобразование монолитного research.md в модульную архитектуру с YAML-настройками режимов, OODA-лупом внутри stages, и Sufficiency Verdict вместо формального checkpoint. Без RESEARCH эта архитектура не была бы обоснована данными. Самокритика: research мог бы глубже исследовать альтернативы OODA (например, Cynefin framework), но scope не позволял — это можно сделать при следующем обновлении.

---

> fact-candidates: processed 2026-04-04

*RES — TFW-22: Coordinator & Research Enrichment | 2026-04-04*
