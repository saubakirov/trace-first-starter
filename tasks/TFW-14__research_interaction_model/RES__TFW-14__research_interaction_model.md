# RES — TFW-14: Research Interaction Model

> **Date**: 2026-04-01
> **Author**: Coordinator (AI)
> **Status**: 🔬 RES — In progress
> **Parent HL**: [HL-TFW-14](HL-TFW-14__research_interaction_model.md)
> **Mode**: Pipeline

---

## Research Context
Исследуем модель взаимодействия агента с пользователем в RESEARCH stage. HL-TFW-14 предлагает 5 протоколов (Briefing, Stage Handoff, Sufficiency Check, Closure, skip-bias fix). Нужно найти слепые зоны, проверить совместимость с существующим workflow, и убедиться что протоколы не избыточны.

## Briefing

### Research Plan
1. **Gather** — изучить как текущий research.md реально работает (TFW-12 RES как единственный живой кейс). Найти конкретные точки где протоколы бы изменили поведение
2. **Extract** — проанализировать plan.md (Phase 3.5), шаблон RES.md, и адаптеры — найти скрытые зависимости и неконсистентности
3. **Challenge** — проверить: не переусложняем ли мы? 5 протоколов для одного workflow — это пропорционально? Какие можно объединить?

### Scope Intent
- **В скоупе:** взаимодействие агент↔пользователь в research, структура протоколов, RES template, plan.md gate
- **Не в скоупе:** стейджи (Gather/Extract/Challenge), лимиты, Entry Modes, standalone mode

### Наводящие вопросы к пользователю
1. Вы уже видели одну живую сессию research (TFW-12). Что конкретно в ней было «слишком быстрым»? Был ли момент, когда вы хотели сказать «подожди, я хочу обсудить X», но агент уже ушёл дальше?
2. 5 протоколов (Briefing, Handoff, Sufficiency, Closure, skip-bias) — вам не кажется, что это может стать слишком тяжёлым? Или каждый из них отвечает на отдельную потребность?
3. Есть ли другие процессные workflow (не TFW), которые вам нравятся как образец интерактивности? Что-то, что вы хотели бы воспроизвести?

→ User decision: (1) Описал проблему: стейджи прогоняются автономно без превью. (2) Протоколы не тяжёлые, но нужна оптимизация — простота. (3) Нет внешних образцов — TFW = codification собственного мышления. Дополнительно: pros/cons формат для gate, RES template и промпт важны, рассмотреть отдельного агента для research.

## Decisions
| # | Decision | Rationale |
|---|----------|-----------|
| R1 | RESEARCH gate: pros/cons формат, пользователь всегда решает сам | Skip-bias fix — агент склонен рекомендовать skip |
| R2 | HL update = обязательный выход research | Research существует для уточнения HL |

## Open Questions
| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Отдельный агент для research vs тот же координатор? | 🔬 | — |
| Q2 | 5 протоколов или можно объединить? | 🔬 | — |
| Q3 | Нужен ли блок «чего ты возможно не видишь» в каждом checkpoint? | 🔬 | — |

---

## Stage: Gather — "What do we NOT know?"

### G1: TFW-12 RES — единственный живой кейс

Изучил [RES__TFW-12](../TFW-12__scope_budget_centralization/RES__TFW-12__config_centralization.md). Структура:
- Research Context → Decisions → Open Questions → Stages → Final Checkpoint → Conclusion
- **Нет секции Briefing** — research начинается сразу с Gather
- **Нет следов пользовательского направления** — стейджи идут один за другим, вопросы только в конце каждого
- **Нет Closure** — после Final Checkpoint сразу Conclusion, без явного «обновляем HL? к TS?»
- **Self-critique в Conclusion** — «I initially focused too narrowly... the Gather stage needed a second pass» — агент сам признаёт проблему поверхностности

### G2: plan.md Phase 3.5 — skip-bias в коде

Текущая логика (L72-74):
```
1. Assess — give a recommendation: is RESEARCH needed? (with rationale)
   - Complex/ambiguous tasks → recommend RESEARCH
   - Simple/clear tasks → recommend skip
```
Проблема: «simple/clear» — субъективная оценка агента. Агенты системно переоценивают ясность задачи (потому что для них любая задача «понятна» — они просто генерируют ответ). Нет структуры для обоснования skip.

### G3: plan.md Phase 3.5 → Phase 4 — пропущен шаг HL update

L81: «After RESEARCH completes → proceed to Phase 4». Phase 4 = Decide Scope (write TS). Нет промежуточного шага «обновить HL по результатам research → утвердить обновлённый HL → затем TS».

### G4: RES template — нет Briefing и Closure секций

Текущий `RES.md` template начинается с Research Context → Decisions → Open Questions → Stages. Нет:
- Секции Briefing (план, scope intent, вопросы ДО стейджей)
- Секции Closure (итог, HL changes, next step)

### G5: Промпт vs шаблон — что важнее для поведения агента

Пользователь сказал: «нам вероятно надо изменить шаблон документа. а также сам промпт на ресерч, от этих вещей многое зависит.» Здесь два рычага:
- **Шаблон (RES.md)** — определяет структуру артефакта, агент заполняет секции
- **Промпт (research.md workflow)** — определяет поведение агента, алгоритм действий

Оба меняются в скоупе TFW-14. Но важно: шаблон работает как «якорь» — если в шаблоне есть секция Briefing, агент вынужден её заполнить. Промпт может быть проигнорирован, но пустая секция в шаблоне — труднее.

### Checkpoint: Gather
| Found | Remaining |
|-------|-----------|
| TFW-12 RES: zero user direction, no briefing, no closure (G1) | Q1: отдельный агент? |
| plan.md skip-bias: «simple/clear → skip» is subjective (G2) | Q2: оптимизация 5 протоколов |
| plan.md: no HL update step after research (G3) | Q3: «чего ты не видишь» блок |
| RES template: missing Briefing + Closure sections (G4) | |
| Template = anchor, prompt = behavior — both matter (G5) | |

**Agent assessment:** Gather подтвердил все проблемы из HL. Конкретные gaps найдены. Ничего неожиданного пока.
**Recommendation:** Close Gather, переходить к Extract.

**Stage Handoff → Extract:** Планирую изучить: (1) Role Lock в plan.md — может ли coordinator писать HL после research? (2) Адаптеры — нужно ли обновлять копии research workflow? (3) «Чего я возможно не вижу» — попробую выявить скрытые проблемы с 5 протоколами.

Есть мысли, что-то хотите добавить перед Extract?

→ User decision: ___

## Stage: Extract — "What do we NOT see?"

### E1: Live proof-of-concept — проблема воспроизвелась в этой сессии

Агент (я) после получения ответов на Briefing сразу ушёл в Gather без паузы, follow-up вопросов, и без предложения обсудить. Пользователь ожидал продолжения разговора, получил стену findings. Это БУКВАЛЬНО As-Is из HL: «агент прогоняет стейджи автономно».

**Корневая причина:** `research.md` L59: «Run three stages (checklist, not strict sequence)» — агент трактует как «прогони по чек-листу как можно быстрее». Нет инструкции задержаться, убедиться что пользователь готов к следующему шагу.

**Вывод:** Ритм разговора определяется не стейджами, а готовностью обеих сторон. 3 вопроса — это бюджет на один turn, не на весь стейдж. Briefing может длиться несколько turns.

### E2: Адаптеры — структурно копируют проблему

`.claude/commands/tfw-research.md` (L30-33) и `.agent/workflows/tfw-research.md` (L36-39):
```
4. Run three stages: Gather → Extract → Challenge (order flexible).
   - Max 3 questions per stage (hard limit).
   - 🛑 Checkpoint after each stage.
   - Final checkpoint: "Sufficient for TS?"
```
Проблемы:
- Zero mention of Briefing
- Zero mention of Closure
- «Sufficient for TS?» — а должно быть «for HL finalization?»
- «Max 3 questions per stage» — фреймит вопросы как бюджет на стейдж, а не как ритм разговора

### E3: Role Lock — coordinator МОЖЕТ писать HL после research

`plan.md` Role Lock (L12): «Permitted artifacts: HL, TS.» Coordinator write-access к HL сохранён. `research.md` Role Lock (L12): «Permitted artifacts: RES only.» Значит: research-агент пишет RES, а coordinator (тот же или другой) обновляет HL по результатам. **Конфликта нет**, но flow не задокументирован.

### E4: Отдельный агент для research — архитектурное решение

Пользователь предложил: research = отдельная сессия (новый чат). Это значит:
- Research-агент пишет RES → завершает сессию
- Coordinator читает RES → обновляет HL → пишет TS (новая сессия или та же)
- **Важно:** research.md Closure Protocol должен работать ВНУТРИ research-сессии. А HL update — ПОСЛЕ неё, в coordinator-сессии.

Это меняет Closure: вместо «обновить HL» в Closure пишем «рекомендации к обновлению HL». Сам update делает coordinator.

### E5: Скоуп расширяется — 5 файлов

Нужно обновить не 3, а 5 файлов:
1. `research.md` — workflow (основной)
2. `RES.md` — template
3. `plan.md` — Phase 3.5
4. `.claude/commands/tfw-research.md` — Claude Code adapter
5. `.agent/workflows/tfw-research.md` — Antigravity adapter

---

### Checkpoint: Extract
| Found | Remaining |
|-------|-----------|
| Live proof-of-concept: agent rushed from briefing (E1) | — |
| Adapters copy the same problems verbatim (E2) | — |
| Role Lock: coordinator can write HL after research (E3) | — |
| Separate agent: Closure = recommendations, not direct HL update (E4) | — |
| Scope: 5 files, not 3 (E5) | — |

→ User decision: Closed. Proceed to Challenge.

## Stage: Challenge — "What do we NOT expect?"

### C1: 5 протоколов → 2+2+1

Разбили 5 «протоколов» на реальные категории:
- **2 новых элемента:** Briefing (вход) + Closure (выход)
- **2 расширения существующего:** Stage Handoff (+2 строки к checkpoint) + Sufficiency (усиление Final Checkpoint)
- **1 фикс текста:** skip-bias в plan.md (pros/cons формат)

Это проще, чем «5 новых протоколов». Суть не меняется, фрейминг проще.

### C2: Turn-based ритм vs stage-based

Текущее правило: «Max 3 questions per stage (hard limit)». Это создаёт давление «задай 3 вопроса и беги дальше».

Предложение: «до 3 вопросов per turn. Стейдж может длиться несколько turns, пока обе стороны готовы перейти дальше.» Turn = один раунд вопрос-ответ, не рестарт.

### C3: HL update gate — process gate, не новый статус

Варианты:
- A: Новый статус в pipeline → лишняя сложность
- B: Явный шаг в plan.md Phase 3.5 + anti-pattern → достаточно

Решение: **B.** Plan.md Phase 3.5: «After RESEARCH → coordinator reads RES → updates HL → user confirms → TS.» Anti-pattern: «Writing TS without updating HL after research.»

### Checkpoint: Challenge

| Found | Remaining |
|-------|-----------|
| 2+2+1 structure (C1) | — |
| Turn-based rhythm (C2) | — |
| Process gate in plan.md, not new status (C3) | — |

→ User decision: Closed.

---

## Final Checkpoint

| Stage | Status | Key Findings |
|-------|--------|-------------|
| Gather | ✅ | TFW-12 RES: no briefing/closure (G1); plan.md skip-bias (G2); no HL update step (G3); RES template gaps (G4); template = anchor (G5) |
| Extract | ✅ | Live proof-of-concept (E1); adapters copy problems (E2); Role Lock ok (E3); separate agent = closure writes recommendations (E4); scope = 5 files (E5) |
| Challenge | ✅ | 5→2+2+1 simplification (C1); turn-based rhythm (C2); process gate not status (C3) |

### Sufficiency Check
**Вопрос:** Достаточно ли информации для финализации HL?
**Ответ:** Да. Фазы, подход и зависимости ясны. 6 конкретных рекомендаций к обновлению HL. Открытых вопросов нет.

**Verdict:** ✅ Sufficient for HL finalization.

## Closure

### Рекомендации к обновлению HL

| # | Что обновить | Источник |
|---|-------------|---------|
| 1 | Скоуп: 5 файлов (+2 адаптера) | E2, E5 |
| 2 | Turn-based ритм: ≤3 вопросов per turn, не per stage | E1, C2 |
| 3 | Closure = рекомендации к HL (не прямой update) | E4 |
| 4 | plan.md: явный шаг «update HL → confirm → TS» + anti-pattern | G3, C3 |
| 5 | Отдельный агент = рекомендация (не обязательное) | E4 |
| 6 | Структура: 2 новых + 2 расширения + 1 фикс | C1 |

→ User decision: Закрыто. Обновляем HL.

## Conclusion

RESEARCH на TFW-14 оказался meta-экспериментом: мы нашли проблемы, буквально воспроизведя их в live session. Ключевое открытие — ритм разговора определяется готовностью обеих сторон, а не стейджами. Агент системно торопится, потому что workflow говорит «run three stages» как чек-лист. Шаблон (RES.md) работает как якорь: пустая секция заставляет агента её заполнить, что надёжнее промпта.

Конкретные выводы: 5 протоколов → 2+2+1 (проще), скоуп 5 файлов (не 3), Closure пишет рекомендации (не делает update), plan.md получает process gate для HL update.

Self-critique: Я сам продемонстрировал skip-bias (предложил пропустить RESEARCH) и rush-bias (перескочил с briefing на gather). Пользователь поймал обе проблемы — это подтверждает ценность interactive research.

---

*RES — TFW-14: Research Interaction Model | 2026-04-01*
