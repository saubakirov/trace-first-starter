# Briefing — Iteration 3: Naming Finals, Visualization Finals, Multi-Iteration Formalization
> Parent: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> Predecessors: [RES1](../RES__TFW-32__methodology_and_positioning.md) (D1-D9), [RES2](../research2/RES__iter2__naming_visualization_multiiter.md) (D10-D14)
> Mode: deep (3 OODA loops, counter-evidence обязателен)
> Goal: Финализировать нейминг секций (факты/знания + визуализация), формализовать многоэтапный ресерч из реальной практики (VLM-3 × 4, TFW-32 × 2).

## Мотивация RES3

RES2 оставил 3 открытых вопроса: Q5 (название секции визуализации), Q6 (шарпинг Fact Candidates), Q7 (точка вставки coordinator gate). RES2 D10 предложил «Strategic Signals» и D12 предложил «Diagrams» — оба без рассмотрения альтернатив. Это итерация для финального выбора с таблицей вариантов и decision matrix.

Мета-принцип (user): «если правильно назвать секцию — ИИ проще, слов надо меньше.» Названия = фундамент коммуникации между людьми и агентами. Индустриальные термины понятны но code-centric, свои термины = value-centric но требуют обучения. Нужен баланс.

## Research Plan

### Gather — варианты и критерии
1. **Нейминг секций фактов/знаний:** Собрать 5-7 вариантов для обеих секций (§6 агентские наблюдения + §7/§11 человеческие сигналы). Для каждого: название, фрейминг (что оно говорит агенту), за, против. Применить D28 + «Claude Code Dreaming» критерий (название = промпт)
2. **Нейминг секции визуализации:** Собрать 4-6 вариантов для universal section name. Для каждого: название, фрейминг, за, против. Проверить: как индустрия vs value-centric термины работают в контексте «не только код»
3. **Многоэтапный ресерч — анализ реальной практики:** Анализ VLM-3 (4 итерации) и TFW-32 (2 итерации). Что работало, что нет. Structure/flow/prompts для формализации

### Extract — дизайн
1. Финальный decision matrix для нейминга (обе секции)
2. Финальный decision matrix для визуализации
3. Формализованный flow многоэтапного ресерча: файлы, кто что контролирует, exit protocol, min_iterations, briefing template для iteration 2+

### Challenge — stress-test
1. Каждое финальное название: как его поймёт (a) новый агент без контекста, (b) бизнес-пользователь, (c) инженер?
2. Многоэтапный ресерч: что сломается если coordinator не запустит следующую итерацию? Что если researcher пишет «sufficient» после первой?
3. Общая философия: держится ли единая идея за всеми названиями? Есть ли coherent naming system или набор ad-hoc решений?

## Hypotheses

| # | Hypothesis | Source |
|---|-----------|--------|
| H5c | «Strategic Signals» (D10) — не финальный ответ. Есть лучший вариант, или нужно уточнение. Требуется comparison table | User (iteration 3 input) |
| H6c | «Diagrams» (D12) — не финальный ответ. Есть лучший вариант для cross-domain use (не только код/архитектура) | User (iteration 3 input) |
| H7c | Многоэтапный ресерч должен быть самоведущим: каждая итерация явно оставляет gap list + directions для следующей. min_iterations = 2 (hard floor). Структура, flow, prompts = полная спецификация | User (iteration 3 input) |
| H_meta | Все названия (секции фактов, секции визуализации, research stages) должны следовать ОДНОЙ философии нейминга. Если философии нет — названия будут ad-hoc и agent behavior будет непредсказуемым | User meta-principle: «название = промпт» |

## Scope Intent
- **In scope:** Decision matrices для нейминга (обе секции + визуализация), формализация multi-iteration research, единая философия нейминга
- **Out of scope:** Реализация (template changes, workflow edits). H1-H4, H8 (closed в RES1). Positioning/README (Phase B topic)

## Guiding Questions
_(answered in User Direction below)_

## User Direction

**Q1 (нейминг фактов/знаний):** Хочет таблицу вариантов: название, фрейминг, за, против. Не согласие с D10 «Strategic Signals» по умолчанию — хочет увидеть альтернативы.

**Q2 (нейминг визуализации):** Точно также — таблица вариантов.

**Q3 (многоэтапный ресерч):** Ресерч должен сам вести к следующему запуску. Явно оставлять: что не закрыто, что стоит проработать, новые инсайты от юзера, новые направления. Минимум 2 итерации всегда. Нужна полная спецификация: структура, flow, prompts.

**Meta-принцип (Claude Code Dreaming):** Если правильно назовём — ИИ проще, слов надо меньше. Индустриальные термины = code-centric, понятны. Свои термины = value-centric, нужно обучение. Но термины станут основой коммуникации между людьми. Нужен баланс.

---
Stage complete: YES
