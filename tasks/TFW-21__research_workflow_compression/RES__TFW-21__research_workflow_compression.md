# RES — TFW-21: Research Workflow Compression

> **Date**: 2026-04-03
> **Author**: Coordinator
> **Status**: 🔬 RES — Complete
> **Parent HL**: [HL-TFW-21](HL-TFW-21__research_workflow_compression.md)
> **Mode**: Pipeline (short)

---

## Research Context

Проверяем две вещи: (1) templates/RES.md содержит все форматы, которые мы планируем вынести из research.md, (2) best practices по компактным AI workflow instructions.

## Gather: Template alignment check

### RES.md template — что содержит

| Секция в research.md (inline) | Присутствует в templates/RES.md? | Расхождения |
|-------------------------------|----------------------------------|-------------|
| Checkpoint format (строки 131-144) | ✅ Да — строки 47-50, 55-58, 63-66 | Template проще: нет `Agent assessment`, `Depth check`, `Recommendation` полей |
| Sufficiency Check (строки 150-170) | ✅ Да — строки 78-88 | Template содержит все self-check пункты. НО: в template нет `Depth check: Did I use external sources?` |
| Closure format (строки 172-197) | ✅ Да — строки 90-99 | Template содержит HL Update Recommendations + Next Step |

### Template gaps (нужно закрыть перед сжатием)

1. **Checkpoint `Depth check` отсутствует в template** — строка "Did I use external sources (web search, docs, URLs), or only project files?" есть в research.md inline, но НЕ в templates/RES.md checkpoint. Это важное поле (Hard Rule #8).
2. **Checkpoint `Agent assessment` и `Recommendation` отсутствуют в template** — в research.md каждый checkpoint имеет 3 поля, template имеет только табличку Found/Remaining + `→ User decision`.

**Вывод**: перед сжатием research.md, нужно дополнить templates/RES.md checkpoint формат тремя полями. Иначе вынос inline шаблонов потеряет информацию.

## Gather: External best practices

### Ключевые паттерны из external research

| # | Паттерн | Источник | Применимость |
|---|---------|----------|-------------|
| 1 | **Principles, not procedures** — объяснять WHO/WHY/WALLS вместо 20-step checklist | Anthropic CLAUDE.md practices | ✅ Подтверждает: оставляем Mindset, убираем пошаговые шаблоны |
| 2 | **Constraint-based rules** — "MUST/NEVER/PREFER" вместо прозы | Token optimization guides | ✅ Hard Rules уже в этом формате. Anti-patterns можно сократить до NEVER-списка |
| 3 | **Don't repeat standard LLM behavior** — focus only on what's unique | CLAUDE.md best practices | ✅ "What good research looks like" описывает стандартное хорошее поведение — можно убрать |
| 4 | **Recency bias** — критичные правила ставить в конец | Anthropic | ✅ Hard Rules + Anti-patterns в конец — check |
| 5 | **Motivation per rule** — объяснять WHY за правилом | Anthropic | ✅ Mindset reminders в stages — уже делают это. Оставляем |
| 6 | **Template > Examples** — структурированные шаблоны лучше длинных examples | Token optimization | ✅ Подтверждает: шаблон RES.md > Example Flow |

### Что это значит для нашего HL

- **Example Flow убирать правильно** — template + Hard Rules достаточно. Паттерн "Template > Examples" подтверждён.
- **"Good/Bad research" убирать правильно** — "don't repeat standard behavior". Hard Rules + Anti-patterns покрывают всё нестандартное.
- **Mindset оставлять правильно** — "Principles, not procedures" + "Motivation per rule" — mindset объясняет WHY.
- **Новая находка**: нужно дополнить templates/RES.md перед сжатием.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| R1 | Дополнить templates/RES.md checkpoint: добавить Agent assessment, Depth check, Recommendation | Без этого вынос inline шаблонов потеряет Hard Rule #8 enforcement |
| R2 | Example Flow убрать полностью | Template + Hard Rules = достаточная калибровка. Подтверждено best practice "Template > Examples" |
| R3 | "Good/Bad research" убрать полностью | Повторяет standard behavior + дублирует Hard Rules. Best practice: "don't repeat standard LLM behavior" |
| R4 | Mindset и stage reminders оставить | Best practice: "Principles, not procedures" + "Motivation per rule" |
| R5 | Anti-patterns сжать в NEVER-список (убрать как отдельную секцию, добавить к Hard Rules) | Deduplicate. Best practice: "Constraint-based rules" |

## HL Update Recommendations

| # | What to update | Source |
|---|---------------|--------|
| 1 | Добавить в scope: дополнение templates/RES.md (checkpoint fields) | RES R1 |
| 2 | Clarify: mindset и stage reminders остаются (user request + best practice confirmation) | User + RES R4 |
| 3 | DoD: добавить "templates/RES.md обновлён с checkpoint полями" | RES R1 |

## Conclusion

Короткий ресерч подтвердил план с одной находкой: templates/RES.md checkpoint format неполный — нет `Agent assessment`, `Depth check`, `Recommendation`. Без дополнения template потеряем Hard Rule #8 при выносе. Best practices подтверждают: mindset оставлять (principles > procedures), example flow убирать (templates > examples), дубликаты убирать (don't repeat standard behavior).

---

*RES — TFW-21: Research Workflow Compression | 2026-04-03*
