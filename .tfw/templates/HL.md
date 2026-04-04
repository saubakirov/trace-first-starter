# HL — {PREFIX}-{N}: {Title}

> **Дата**: YYYY-MM-DD
> **Автор**: {author}
> **Статус**: 📝 HL_DRAFT — Ожидает ревью

---

## 1. Видение
What we want and WHY. Business value. Brand context.
> One key quote that captures the essence.

## 2. Текущее состояние (As-Is)
Current code, bugs, metrics, architecture.
Tables with REAL data — files, sizes, statuses, test results.

## 3. Целевое состояние (To-Be)
What it should look like after. Clear deliverables.
Tables comparing As-Is → To-Be where applicable.

### 3.1 Визуализация результата

> Покажи результат как будто он уже достигнут. Используй:
> - **ASCII-схемы** (обязательно): architecture, flow, file structure
> - **Mermaid** (для complex flows): sequence diagrams, state machines
> - **Before→After таблицы** для сравнения state
>
> Цель: исполнитель и юзер должны увидеть «финальную картинку» до начала работы.

## 4. Фазы
Break into Phases (A, B, C...) with priorities 🔴🟡🟢.
Each Phase = separate TS→RF cycle.

### Phase A: {title} 🔴
- {bullet list of deliverables}

### Phase B: {title} 🟡
- {bullet list of deliverables}

## 5. Definition of Done (DoD)
Numbered list. Each item starts with ✅.
Must cover: tests, code, data, deploy, monitoring (as applicable).

- ✅ 1. {Criterion 1}
- ✅ 2. {Criterion 2}

## 6. Definition of Failure (DoF)
Numbered list. Each item starts with ❌.
What to do on failure: rollback, rethink, escalate.

- ❌ 1. {Failure condition 1}
- ❌ 2. {Failure condition 2}

**При провале:** {action plan}

## 7. Принципы
Design philosophy. Non-negotiable rules.

1. **{Principle name}** — {description}
2. **{Principle name}** — {description}

## 7.1 Quality Contract (optional, for multi-phase tasks)
Anti-patterns, style rules, and constraints that MUST be copied into each Phase TS.
Purpose: prevent executor agents from drifting.
Only needed for tasks where consistency across phases matters.

## 8. Зависимости
| Зависимость | Статус |
|-------------|--------|
| {dependency} | ⬜ / ✅ |

## 9. Риски
| Риск | Вероятность | Влияние | Mitigation |
|------|-------------|---------|------------|
| {risk} | Низкая/Средняя/Высокая | Низкое/Среднее/Высокое | {mitigation} |

## 10. Обоснование RESEARCH

### Слепые зоны
- {Что мы НЕ знаем, но что может повлиять на подход}

### Гипотезы

| # | Гипотеза | Статус |
|---|----------|--------|
| H1 | {Утверждение для проверки} | open |

> **Фильтр:** Каждая гипотеза: «Если окажется ложной — изменится ли наш подход?» Если нет — удалить.

### Риски незнания
{Что случится ЕСЛИ мы пропустим RESEARCH}

### Предлагаемый фокус RESEARCH
1. **Gather**: {конкретный вопрос}
2. **Extract**: {конкретный вопрос}
3. **Challenge**: {конкретный вопрос}

---

*HL — {PREFIX}-{N}: {Title} | YYYY-MM-DD*
