# HL — TFW-21: Research Workflow Compression

> **Дата**: 2026-04-03
> **Автор**: Coordinator
> **Статус**: 📝 HL_DRAFT — Ожидает ревью

---

## 1. Видение

research.md — самый длинный воркфлоу TFW (2397 слов, 319 строк). Он в 2.7× больше среднего рабочего воркфлоу (handoff=895, review=731). На новых проектах (без привычки и KI-контекста) агенты не усваивают инструкции полностью — пролетают мимо stages, задают 1-2 дежурных вопроса и объявляют "ready for TS".

> Сжать research.md до ~150 строк / ~1200 слов без потери поведенческих требований.

## 2. Текущее состояние (As-Is)

| Метрика | Значение |
|---------|----------|
| Файл | `.tfw/workflows/research.md` + `.agent/workflows/tfw-research.md` (копии) |
| Строк | 319 |
| Слов | 2397 |
| Средний рабочий воркфлоу | ~800 слов |
| Отклонение от среднего | +200% |

### Структурный аудит (где раздуто)

| Секция | Строки | Слов | Проблема |
|--------|--------|------|----------|
| Research Mindset | 16-26 | ~120 | Многословное — можно 2 предложения |
| Entry Modes | 28-39 | ~80 | OK, компактно |
| Prerequisites | 41-49 | ~60 | OK |
| Briefing Protocol | 51-65 | ~90 | OK |
| Process (stages) | 67-116 | ~350 | Ядро — оставить |
| Checkpoint format | 117-144 | ~150 | Дублирует templates/RES.md |
| Final checkpoint | 146-170 | ~150 | Дублирует templates/RES.md |
| Closure Protocol | 172-197 | ~160 | Можно сжать |
| **Example Flow** | **199-243** | **~280** | **Самый жирный кусок. 45 строк примера** |
| **Agent Behavior Protocol** | **245-278** | **~320** | **Дублирует Hard Rules + переформулирует Anti-patterns** |
| Limits | 280-293 | ~80 | OK |
| Status Transitions | 295-301 | ~40 | OK |
| **Anti-patterns (дубль)** | **303-318** | **~150** | **Третья формулировка того же — после Hard Rules и Good/Bad** |

**Итого дубликатов: ~750 слов (31% документа).**

Три блока говорят одно и то же разными словами:
1. Hard Rules (строки 248-257) — "agent MUST..."
2. What good/bad research looks like (строки 259-272) — "probing, not reporting..."
3. Anti-patterns (строки 303-318) — "agent runs through stages silently..."

## 3. Целевое состояние (To-Be)

| Метрика | As-Is | To-Be |
|---------|-------|-------|
| Строк | 319 | ~150 |
| Слов | 2397 | ~1200 |
| Дублирование | 3 блока (750 слов) | 1 блок (Rules & Anti-patterns) |
| Inline шаблоны | 2 (Checkpoint + Sufficiency) | 0 (ссылка на templates/RES.md) |
| Example Flow | 45 строк | 0 (убрать полностью) |

### Что убираем

1. **Example Flow** (строки 199-243, ~280 слов) — агент видит паттерн из Hard Rules + Briefing Protocol. Пример не помогает новым проектам — он слишком длинный чтобы служить quick-reference и слишком короткий чтобы быть training data.

2. **Inline markdown шаблоны** (Checkpoint format строки 131-144, Sufficiency Check строки 150-170, ~220 слов) — эти форматы уже в `templates/RES.md`. Ставим ссылку "format: see `templates/RES.md` Checkpoint section".

3. **"Good/Bad research" + Anti-patterns дубль** (~300 слов) — сливаем в один блок "Rules & Anti-patterns" таблицей: 8 Hard Rules + 5 ключевых anti-patterns.

### Что сжимаем

4. **Research Mindset** (120→~80 слов) — сжимаем, но сохраняем настрой и mindset полностью. Best practice: "Principles, not procedures" — mindset объясняет WHY.

5. **Closure Protocol** (160→80 слов) — убираем пояснения, оставляем шаги.

### Что оставляем без изменений

- Entry Modes, Prerequisites, Briefing Protocol — компактные, работающие
- Process (3 stages) с stage mindset reminders — ядро воркфлоу (confirmed by research: "motivation per rule")
- Limits, Status Transitions — справочные, компактные

## 4. Фазы

### Single Phase 🔴

Deliverables:
- Дополненный `templates/RES.md` — добавить checkpoint поля (Agent assessment, Depth check, Recommendation) — **prerequisite** (RES R1)
- Сжатый `research.md` (~150 строк, ~1200 слов)
- Синхронизированный `.agent/workflows/tfw-research.md`
- Верификация: `wc -w` < 1300

## 5. Definition of Done (DoD)

- ✅ 1. research.md ≤ 160 строк
- ✅ 2. research.md ≤ 1300 слов
- ✅ 3. Все 8 Hard Rules сохранены (можно в иной форме)
- ✅ 4. 3 stages (Gather, Extract, Challenge) сохранены со своими mindset-reminders
- ✅ 5. Briefing Protocol и Closure Protocol сохранены
- ✅ 6. Нет inline шаблонов — только ссылки на templates/RES.md
- ✅ 7. `.agent/workflows/tfw-research.md` = точная копия `.tfw/workflows/research.md`
- ✅ 8. `wc -w` и `wc -l` верификация пройдена
- ✅ 9. templates/RES.md checkpoint дополнен полями Agent assessment, Depth check, Recommendation (RES R1)

## 6. Definition of Failure (DoF)

- ❌ 1. Документ > 1300 слов — сжатие недостаточное
- ❌ 2. Потеряно хотя бы одно Hard Rule — поведение деградирует
- ❌ 3. Убраны stage mindset-reminders — агент вернётся к поверхностному ресерчу

**При провале:** вернуть из git, пересмотреть что было убрано лишнего.

## 7. Принципы

1. **Density over verbosity** — каждое предложение должно менять поведение агента. Если убрать предложение и ничего не изменится — оно лишнее.
2. **Deduplicate ruthlessly** — одно правило, одно место. Не три формулировки одного и того же.
3. **Templates belong in templates** — inline markdown форматы = дрейф от канонических шаблонов.
4. **Preserve behavioral anchors** — mindset reminders в stages и Hard Rules — это то, что реально меняет поведение. Их нельзя терять.

## 8. Зависимости

| Зависимость | Статус |
|-------------|--------|
| templates/RES.md содержит Checkpoint и Sufficiency форматы | 🔴 Gap найден — Checkpoint без Agent assessment/Depth check/Recommendation (RES R1) |

## 9. Риски

| Риск | Вероятность | Влияние | Mitigation |
|------|-------------|---------|------------|
| Потеря nuance из Example Flow | Средняя | Среднее | Hard Rules покрывают все паттерны из примера |
| templates/RES.md не содержит нужных форматов | Низкая | Высокое | Проверить перед execution, добавить если нет |

---

*HL — TFW-21: Research Workflow Compression | 2026-04-03*
