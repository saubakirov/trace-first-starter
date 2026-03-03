# HL — TFW-5: KNOWLEDGE.md + tfw-docs Workflow

> **Дата**: 2026-03-03
> **Автор**: Coordinator (AI) + User
> **Статус**: 🔵 HL — Ожидает ревью
> **Источник**: Atamat TFW-11 Phase B (testing ground → canonical)

---

## 1. Видение

TFW v3 создаёт знания (RF файлы: решения, архитектура, observations), но **не возвращает** их в центральные документы. После 10+ задач новый агент сталкивается с десятками HL/RF без единого индекса. Решения рассеяны по RF. Устаревшие концепты не задокументированы → агенты заново изобретают отброшенные идеи.

Проблема обостряется для **brownfield-проектов**: кодовая база существовала до TFW, знания живут в головах разработчиков, а не в файлах.

**Решение**: два новых элемента TFW v3:

1. **`KNOWLEDGE.md`** — центральный индекс проекта: архитектурная карта, decision log, legacy/deprecation, AI reference. Не дубликация README — а его knowledge layer.

2. **`tfw-docs` workflow** — механизм обратной связи. После каждого REVIEW координатор прогоняет 5-item checklist: что обновить в KNOWLEDGE.md и TECH_DEBT.md.

## 2. Текущее состояние (As-Is)

- `.tfw/templates/` содержит шаблоны HL, TS, RF, ONB, REVIEW — нет KNOWLEDGE.md
- `.tfw/workflows/` содержит plan, handoff, resume — нет tfw-docs
- REVIEW template не содержит Knowledge Update маркера
- `init.md` Step 6 не упоминает KNOWLEDGE.md
- Знания теряются между задачами

## 3. Целевое состояние (To-Be)

### 3.1 KNOWLEDGE.md Template
Канонический шаблон в `.tfw/templates/KNOWLEDGE.md` со структурой:

| Section | Содержание |
|---------|-----------|
| Philosophy & Principles | Ключевые принципы проекта (ссылки на HL где были сформулированы) |
| Architecture Map | Компоненты, их связи, текущий стек (ссылки на HL/RF) |
| Decision Log | Таблица D1..Dn — решения, обоснование, ссылка на RF |
| Legacy & Deprecation | Что устарело, что заморожено, когда и почему |
| Key Artifacts | Индекс самых важных RF/HL для контекста |

**Принцип**: Index, don't duplicate. Ссылки на RF/HL, не копии содержимого.

### 3.2 tfw-docs Workflow
Канонический workflow в `.tfw/workflows/tfw-docs.md`:

**3 режима запуска:**
| Mode | Trigger | Когда |
|------|---------|-------|
| Auto | REVIEW → ✅ APPROVE | После каждой апрувнутой задачи |
| Manual | `/tfw-docs {TASK-ID}` | Вручную для конкретного RF |
| Batch | `/tfw-docs --scan` | Периодический скан всех необработанных RF |

**Triage gate** (1-секундное решение координатора):
- Архитектурное изменение? Стратегическое решение? Deprecation? Новая конвенция?
- YES → run 5-item checklist
- NO (bugfix, мелкий рефактор) → «tfw-docs: N/A (minor)» в REVIEW

**5-item checklist:**
1. Architecture changed? → KNOWLEDGE.md Architecture Map
2. New decision (D-record)? → KNOWLEDGE.md Decision Log
3. Something deprecated? → KNOWLEDGE.md Legacy & Deprecation
4. New tech debt? → TECH_DEBT.md
5. New principle/convention? → KNOWLEDGE.md или conventions

### 3.3 REVIEW template update
Добавить в «Traces Updated» секцию маркер: `tfw-docs: {Applied — updated Sections X,Y / N/A (minor)}`

### 3.4 init.md update
В Step 6 добавить: «Создать `KNOWLEDGE.md` по шаблону, если проект — brownfield».

## 4. Scope

Single-phase задача.

| Файл | Действие |
|------|----------|
| `.tfw/templates/KNOWLEDGE.md` | NEW — шаблон |
| `.tfw/workflows/tfw-docs.md` | NEW — workflow с frontmatter |
| `.tfw/templates/REVIEW.md` | MODIFY — добавить tfw-docs маркер |
| `.tfw/init.md` | MODIFY — Step 6 update |
| `.tfw/conventions.md` | MODIFY — добавить KNOWLEDGE.md в §2 |
| `.agent/workflows/tfw-docs.md` | NEW (sync copy) |

**Бюджет**: 3 NEW, 3 MODIFY = 6 файлов. Укладывается в ≤7.

## 5. Definition of Done (DoD)

- ✅ `.tfw/templates/KNOWLEDGE.md` создан с 5 секциями
- ✅ `.tfw/workflows/tfw-docs.md` создан ≤60 строк, 3 trigger modes, 5-item checklist
- ✅ REVIEW.md template содержит tfw-docs маркер
- ✅ init.md Step 6 упоминает KNOWLEDGE.md для brownfield-проектов
- ✅ conventions.md §2 содержит KNOWLEDGE.md как опциональный артефакт
- ✅ `.agent/workflows/tfw-docs.md` синхронизирован

## 6. Definition of Failure (DoF)

- ❌ KNOWLEDGE.md template > 80 строк — слишком тяжёлый для старта
- ❌ tfw-docs workflow > 60 строк — слишком сложный
- ❌ Checklist items содержат project-specific ссылки (должен быть generic)

## 7. Принципы

1. **Index, don't duplicate** — KNOWLEDGE.md ссылается на RF/HL, не копирует содержимое
2. **Lightweight docs workflow** — tfw-docs = 5 checkbox items, не бюрократия
3. **Generic first** — всё должно работать в любом проекте, не только Atamat
4. **Brownfield-aware** — KNOWLEDGE.md особенно ценен для проектов с existing codebase

## 8. Риски

| Риск | Mitigation |
|------|------------|
| KNOWLEDGE.md никто не заполняет при init | Step 6 в init.md напоминает. tfw-docs workflow поддерживает актуальность |
| tfw-docs добавляет overhead | Triage gate: minor tasks = «N/A», 1 секунда |

---

*HL — TFW-5: KNOWLEDGE.md + tfw-docs Workflow | 2026-03-03*
