# TS — TFW-11 / Phase A: Core — Артефакт, статус, воркфлоу

> **Дата**: 2026-03-30
> **Автор**: Coordinator (AI)
> **Статус**: 🟡 TS — Ожидает апрува
> **Parent HL**: [HL-TFW-11](HL-TFW-11__research_stage.md)
> **Research**: [RES__TFW-11](RES__TFW-11__research_stage.md)

---

## 1. Цель

Создать ядро RESEARCH-стадии: шаблон RES-артефакта, воркфлоу research.md, обновить conventions и glossary новым статусом 🔬 RES и артефактом, добавить настройки в PROJECT_CONFIG.yaml.

## 2. Scope

### In Scope
- Шаблон `RES.md` в `.tfw/templates/`
- Воркфлоу `research.md` в `.tfw/workflows/`
- Новый статус 🔬 RES в conventions.md (пайплайн, таблица статусов, артефакты)
- Новые термины в glossary.md
- Секция `research:` в PROJECT_CONFIG.yaml
- Naming conventions для RES-файлов

### Out of Scope
- Интеграция в plan.md (Phase B)
- Slash-команда `/tfw-research` и адаптеры (Phase B)
- Обновление README.md pipeline (Phase B)
- Proof-of-concept (Phase C)

## 3. Затрагиваемые файлы

| Файл | Действие | Описание |
|------|----------|----------|
| `.tfw/templates/RES.md` | CREATE | Шаблон RES-артефакта |
| `.tfw/workflows/research.md` | CREATE | Воркфлоу RESEARCH-процесса |
| `.tfw/conventions.md` | MODIFY | Новый статус, артефакт, пайплайн, naming |
| `.tfw/glossary.md` | MODIFY | Новые термины: RES, Stage, Pass, RESEARCH |
| `.tfw/PROJECT_CONFIG.yaml` | MODIFY | Секция `research:` с настройками |

**Бюджет:** 2 новых файла, 3 модификации. ≤7 файлов ✅, ≤4 новых ✅

## 4. Детальные шаги

### Step 1: Создать `.tfw/templates/RES.md`

Шаблон на основе решений D1-D16 из RES-артефакта:

```markdown
# RES — {PREFIX}-{N}: {Title}

> **Дата**: YYYY-MM-DD
> **Автор**: {author}
> **Статус**: 🔬 RES — В процессе
> **Parent HL**: [HL-{PREFIX}-{N}](path) _(если pipeline)_
> **Режим**: Pipeline / Standalone

---

## Контекст исследования
Одним абзацем: что исследуем и зачем.

## Решения
| # | Решение | Обоснование |
|---|---------|-------------|

## Открытые вопросы
| # | Вопрос | Статус | Ответ |
|---|--------|--------|-------|

---

## Этап: Сбор — "Что мы НЕ знаем?"
{Информационные пробелы, внешние источники, документация, версии, issues}

### Checkpoint: Сбор
| Что найдено | Что осталось |
|-------------|-------------|
→ Решение пользователя: ___

## Этап: Извлечение — "Что мы НЕ ВИДИМ?"
{Анализ проекта, скрытые знания, неявные требования}

### Checkpoint: Извлечение
| Что найдено | Что осталось |
|-------------|-------------|
→ Решение пользователя: ___

## Этап: Вызов — "Что мы НЕ ОЖИДАЕМ?"
{Альтернативы, слепые зоны, edge cases, критика}

### Checkpoint: Вызов
| Что найдено | Что осталось |
|-------------|-------------|
→ Решение пользователя: ___

---

## Итоговый checkpoint

| Этап | Статус | Ключевые находки |
|------|--------|-----------------|
| Сбор | | |
| Извлечение | | |
| Вызов | | |

### Проверка на сложность
**Вопрос:** Соразмерно ли решение задаче? Что можно убрать без потери ценности?
**Оценка агента:** [ответ]
→ Решение пользователя: ___

**Вердикт:** Достаточно для TS / Нужен ещё проход

## Заключение
[Один абзац. Что исследовано. Ключевые решения. Польза сессии. Самокритика.]
```

### Step 2: Создать `.tfw/workflows/research.md`

Воркфлоу с YAML frontmatter (D6 из KNOWLEDGE.md — Antigravity требует `description`).

Содержание:
- Role Lock: Coordinator
- Два режима входа: Pipeline (есть HL, задача) и Standalone (создать мини-задачу)
- Загрузка контекста (AGENTS.md, conventions, etc.)
- 3 этапа как чеклист: Сбор, Извлечение, Вызов
- Поведение агента на каждом этапе (конкретные действия, тон)
- Лимиты — ссылка на PROJECT_CONFIG.yaml
- Формат checkpoint после каждого этапа
- Итоговый checkpoint с anti-complexity
- Правила: ≤3 вопросов за этап, RES создаётся сразу, read-only AG
- Standalone lifecycle: 🔬 RES → ✅ DONE или → новая задача

### Step 3: Обновить `.tfw/conventions.md`

Изменения:
1. **§3 Artifact Types** — добавить RES (Research Report) после HL
2. **§4 Task Numbering** — добавить naming для RES-файлов:
   - Pipeline: `RES__{PREFIX}-{N}__{title}.md`
   - Pipeline phase: `RES__Phase{X}__{title}.md`
3. **§5 Task Statuses** — добавить 🔬 RES между 🔵 HL и 🟡 TS:
   ```
   ⬜ TODO → 🔵 HL → 🔬 RES → 🟡 TS → 🟠 ONB → 🟢 RF → 🔍 REV → ✅ DONE
   ```
   Пунктирная линия HL → TS (skip path, если RESEARCH не нужен)
4. **§8 Workflows** — добавить research.md в таблицу
5. **§15 Role Lock Protocol** — добавить research.md: Coordinator, permitted: RES

### Step 4: Обновить `.tfw/glossary.md`

Добавить:
- **RES (Research Report)** — артефакт RESEARCH-стадии. Живой документ: решения и вопросы сверху, лог этапов ниже.
- **Stage (Этап)** — один тематический блок RESEARCH: Сбор, Извлечение или Вызов.
- **Pass (Проход)** — полный round-trip по всем этапам RESEARCH.
- **RESEARCH** — стадия между HL и TS. Структурированное исследование: сбор информации, извлечение скрытых знаний, критический анализ. Опционален (skip с подтверждением пользователя).

### Step 5: Обновить `.tfw/PROJECT_CONFIG.yaml`

Добавить секцию:
```yaml
research:
  web_queries_per_stage: 5
  files_read_per_stage: 15
  questions_per_stage: 3
  max_passes: 3
```

## 5. Acceptance Criteria

- [ ] `.tfw/templates/RES.md` существует, содержит все секции из Step 1
- [ ] `.tfw/workflows/research.md` существует, содержит role lock, оба режима, 3 этапа, лимиты, checkpoint формат
- [ ] `conventions.md` содержит статус 🔬 RES, артефакт RES, обновлённый пайплайн, naming для RES-файлов
- [ ] `glossary.md` содержит термины: RES, Stage, Pass, RESEARCH
- [ ] `PROJECT_CONFIG.yaml` содержит секцию `research:` с 4 параметрами
- [ ] Все пайплайн-диаграммы в conventions.md и glossary.md обновлены (8 → 9 статусов)

## 6. Риски фазы

| Риск | Mitigation |
|------|------------|
| research.md слишком длинный / сложный | Следовать стилю существующих workflows (plan.md ≈ 100 строк) |
| Пайплайн-диаграммы рассинхронизируются | Grep по `TODO.*HL.*TS` во всех .md файлах после изменений |

---

*TS — TFW-11 / Phase A: Core — Артефакт, статус, воркфлоу | 2026-03-30*
