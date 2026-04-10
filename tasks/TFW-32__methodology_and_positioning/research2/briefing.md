# Briefing — Iteration 2
> Parent: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> Goal: Address gaps left by Research1 — naming precision ("Strategic" vs "Knowledge"), visualization/diagrams section design, business process representation, and multi-iteration research formalization from lived experience.
> Predecessor: [RES1](../RES__TFW-32__methodology_and_positioning.md) — 9 decisions, H6 deferred, H7 designed but untested

## Research Plan

### Gather — "What do we NOT know?"
1. **Naming analysis: "Strategic Insights" vs "Knowledge Candidates"** — RES1 proposed renaming to "Doc Candidates + Knowledge Candidates" (D2). User now questions: "knowledge" is vague. "Strategic" had focus — it told you WHAT to look for. Investigate naming theory: does specificity in a name improve agent capture quality? What happens when a category name is too broad?
2. **Visualization/Diagrams in methodology artifacts** — no investigation in RES1 (H6 deferred). Research: what do other frameworks (C4, arc42, ADR, Shape Up) recommend for diagram placement? Where do diagrams live in artifact lifecycle — HL? TS? RF? Knowledge? What is the consolidation path?
3. **Business process representation** — user insight: every project has business processes but TFW doesn't capture them explicitly. How do BPM frameworks (BPMN, user journey maps, sequence diagrams) handle process documentation? Where should process flows live in TFW artifacts?
4. **Multi-iteration research: lived experience analysis** — this IS iteration 2 right now. What actually happened: user ran RES1, got insights, wants more. The researcher "rushes to close" — confirmed. What state handoff is needed? What does the coordinator control file actually need?

### Extract — "What do we NOT see?"
1. Design the naming decision: concrete options for the two-section naming (FC/SI vs DocC/KnwC vs something else). Apply D28 to each option. Test: which name triggers the most precise agent behavior?
2. Design the "Diagrams" or "Visualization" section — exact location in each artifact template, naming, consolidation path during knowledge collection
3. Design multi-iteration research from the INSIDE — what would have helped THIS iteration start faster? What was missing from RES1 that I had to re-discover?

### Challenge — "What do we NOT expect?"
1. Challenge the visualization section: does adding a diagrams section to every artifact create bloat? When is it valuable vs ceremony?
2. Challenge naming: what if BOTH "Strategic" and "Knowledge" are wrong and the concept needs a third name entirely?
3. Challenge multi-iteration: what if the coordinator control file becomes stale or contradicts RES findings? Who has authority?

## Hypotheses (from HL §10 + RES1 gaps)

| # | Hypothesis | Source | RES1 Status |
|---|-----------|--------|-----------|
| H5b | "Knowledge Candidates" is too vague as a name — loses the behaviorally-targeted focus of "Strategic" (D28). A better name would preserve the FILTRATION function: telling the agent what KIND of thing to capture | User (iteration 2 input) | Supersedes RES1 D2 |
| H6 | TFW needs a standard section in artifacts for diagrams/visualizations/flow representations. This section should have ONE clear name across all artifacts and consolidate into knowledge during 📚 KNW | HL §10, deferred by RES1 | ⏸️ DEFERRED |
| H6b | Business processes (user journeys, value delivery flows, sequence diagrams) need explicit representation in TFW — not just as "diagrams" but as a specific artifact type or section that captures the PROCESS from user to value | User (iteration 2 input, S15) | NEW |
| H7b | Multi-iteration research needs LESS structure than RES1 proposed (iterations.yaml is overengineered) — the actual experience shows the coordinator just needs to say "gaps remain, run again" and pass the RES + gap list. The researcher reads RES1 and picks up from there | Lived experience (this session) | Challenges RES1 D4 |

## Scope Intent
- **In scope:** H5b (naming precision), H6 (visualization section), H6b (business processes), H7b (multi-iteration from lived experience)
- **Out of scope:** H1-H4, H8 (addressed in RES1 — no new evidence to revisit). Actual implementation of any design. README rewrite.

## Guiding Questions

1. Про нейминг: ты сказал «если переименуем strategic в knowledge не теряем тот самый принцип про нейминг». Конкретнее: что именно тебе нравилось в слове "strategic"? Что оно подсказывало агенту искать — бизнес-контекст? мотивы стейкхолдеров? вещи недоступные из кода? Или тебя беспокоит что "knowledge" настолько широкое что агент будет туда всё подряд писать?
2. Про визуализацию: ты хочешь отдельную главу в каждом артифакте (HL, TS, RF), или одну центральную главу только в HL (как сейчас §3.1 Result Visualization)?
3. Про бизнес-процессы: когда ты говоришь «диаграмма последовательностей чтобы видно процесс и где достигается ценность» — ты имеешь в виду что в HL (на стадии планирования) уже должна быть scheme of value delivery? Или это часть RF (после выполнения — вот как работает)?

## User Direction

**H7b correction:** User DISAGREES that multi-iteration needs less structure. Opposite: without YAML/statuses, agents will fast-run every time. Multi-iteration REQUIRES structural enforcement. Researcher must remind human to run again. Coordinator must block TS until coverage is complete. "Agents always want to finish faster" — trust as business/domain input.

**Q1 (naming):** "Strategic Insight" is a good vector — it tells the agent WHAT to look for. "Knowledge" is too broad — agent will write everything there. Keep "Strategic" direction.

**Q2 (visualization):** Separate chapter in each RESULT artifact (RES, RF) — wherever applicable (processes, flows). Not just HL.

**Q3 (business processes):** BOTH locations:
- **HL** = vision-level value stream, flow of value delivery (upper level)
- **RF** = factual result in detail — DB schemas, API calls, sequence diagrams

Two levels: planning vision → execution detail.

---
Stage complete: YES
