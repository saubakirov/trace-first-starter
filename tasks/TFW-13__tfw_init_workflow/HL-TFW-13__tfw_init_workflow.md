# HL — TFW-13: tfw-init Workflow

> **Дата**: 2026-03-30
> **Автор**: Coordinator (AI)
> **Статус**: 🔵 HL — Ожидает ревью

---

## 1. Видение

Текущий `init.md` — инструкция для человека: "скопируй файлы, отредактируй конфиг, выбери адаптер". AI-агент не может её "запустить" — он может только интерпретировать как набор команд. Это анти-паттерн для фреймворка, который работает через AI-агентов.

`/tfw-init` — полноценный workflow, который AI-агент находит естественно, читает, и выполняет. Агент впервые видит TFW, ничего не знает — и через tfw-init понимает, что делать: настроить конфиг, адаптировать под проект, спросить пользователя о стеке, провести первый RESEARCH проекта, создать KNOWLEDGE.md.

> Ключевая идея: init.md написан для человека. tfw-init написан для AI-агента. Агент — первичный потребитель.

## 2. Текущее состояние (As-Is)

| Аспект | Состояние |
|--------|-----------|
| `init.md` | 232 строки, ручная инструкция (cp, edit, cat) |
| Механическая часть | Steps 1-4: copy .tfw/, edit config, choose adapter, create root files |
| Онбординг | Step 6: study codebase, adapt artifacts — тезисный, не формализован |
| Как workflow | Не существует. Нет `/tfw-init` |
| Adapter docs | "How to Write a New Adapter" (строки 204-231) — живёт в init.md, не по адресу |
| Первый запуск AI | Агент читает CLAUDE.md → видит workflows → но init.md — не workflow, а документ |

### Что не работает

- AI-агент не может "запустить" init.md — это документ, не workflow
- Step 6 (онбординг) — самая ценная часть, но описана в 10 строках
- Механические шаги (copy, edit) перемешаны с интеллектуальными (study codebase, adapt)
- Нет RESEARCH при инициализации — агент не задаёт вопросы о проекте
- Нет интерактивного опроса пользователя о стеке, конвенциях, целях

## 3. Целевое состояние (To-Be)

| Аспект | Целевое состояние |
|--------|-------------------|
| `init.md` | Удалён или сведён к минимальному указателю на workflow |
| `tfw-init` workflow | `.tfw/workflows/init.md` — полноценный workflow |
| `/tfw-init` | Слэш-команда во всех адаптерах |
| Механика | Агент делает сам: создаёт файлы, заполняет config |
| Онбординг | Встроенный RESEARCH: агент изучает проект, задаёт вопросы, адаптирует |
| Adapter docs | Переносятся в `.tfw/README.md` или отдельный файл |

### Процесс tfw-init

```
/tfw-init
  │
  ├── Phase 1: Discover — агент читает проект, определяет стек, структуру
  │   "Я вижу package.json → Node.js, src/ → TypeScript..."
  │
  ├── Phase 2: Interview — интерактивный опрос пользователя
  │   "Какой task_prefix? Какие build/test/lint команды? Какие конвенции?"
  │
  ├── Phase 3: Setup — механическая настройка
  │   Создать/обновить: PROJECT_CONFIG.yaml, AGENTS.md, README.md (Task Board),
  │   TECH_DEBT.md, adapter файлы
  │
  ├── Phase 4: Knowledge — первый RESEARCH проекта
  │   Изучить кодовую базу, создать KNOWLEDGE.md, зафиксировать архитектуру,
  │   решения, зависимости
  │
  └── Phase 5: Verify — чеклист, всё на месте
```

### Ключевое отличие от init.md

| | init.md (сейчас) | tfw-init (целевое) |
|--|---|---|
| Для кого | Человек | AI-агент |
| Формат | Документ с bash-командами | Workflow с ролью и этапами |
| Интерактивность | Нет | Опрос, RESEARCH, адаптация |
| Онбординг | 10 строк в конце | Полноценная Phase 4 |
| Результат | Скопированные файлы | Настроенный и адаптированный TFW |

## 4. Фазы

### Phase A: Workflow + slash command 🔴
- `.tfw/workflows/init.md` — workflow с 5 фазами (Discover → Interview → Setup → Knowledge → Verify)
- Слэш-команда `/tfw-init` во всех адаптерах
- Удаление/замена текущего `.tfw/init.md`

### Phase B: Adapter docs + cleanup 🟡
- Перенос "How to Write a New Adapter" из init.md
- Обновление ссылок в conventions.md, README.md
- Обновление KNOWLEDGE.md

## 5. Definition of Done (DoD)

- ✅ 1. `.tfw/workflows/init.md` существует как полноценный workflow с role lock
- ✅ 2. `/tfw-init` работает как слэш-команда (Claude Code, Antigravity)
- ✅ 3. Workflow содержит 5 фаз: Discover, Interview, Setup, Knowledge, Verify
- ✅ 4. Phase 4 (Knowledge) включает RESEARCH-подобный процесс
- ✅ 5. Старый `init.md` удалён или заменён указателем
- ✅ 6. "How to Write a New Adapter" перенесён в адекватное место
- ✅ 7. Все ссылки на init.md обновлены

## 6. Definition of Failure (DoF)

- ❌ 1. Workflow слишком длинный (>200 строк) — агент теряет фокус
- ❌ 2. Init превращается в RESEARCH + PLAN + HANDOFF одновременно — должен быть простым
- ❌ 3. Агент не может выполнить init автономно для очевидных случаев (Node.js проект с package.json)

**При провале:** упростить, вынести Knowledge phase в отдельный `/tfw-research` вызов.

## 7. Принципы

1. **Agent-first** — workflow написан для AI, не для человека. Человек может читать, но первичный потребитель — агент.
2. **Interactive by default** — агент не делает предположений. Он спрашивает и подтверждает.
3. **One-time** — запускается ровно один раз при подключении TFW к проекту.
4. **Progressive** — агент может остановиться после Phase 3 (Setup) если Knowledge phase избыточна для нового проекта.

## 8. Зависимости

| Зависимость | Статус |
|-------------|--------|
| research.md workflow (для Phase 4 Knowledge) | ✅ TFW-11 |
| PROJECT_CONFIG.yaml structure | ✅ TFW-12 |
| Adapter structure (Claude Code, Antigravity) | ✅ |

## 9. Риски

| Риск | Вероятность | Влияние | Mitigation |
|------|-------------|---------|------------|
| Конфликт naming: init.md (workflow) vs init.md (старый) | Средняя | Среднее | Workflow = `.tfw/workflows/init.md`, старый удаляется |
| Phase 4 (Knowledge) делает init слишком тяжёлым | Средняя | Среднее | Knowledge = опциональная фаза, агент рекомендует но не навязывает |
| Разные AI-инструменты по-разному обрабатывают init | Низкая | Высокое | Workflow tool-agnostic, адаптеры — thin wrappers |

---

*HL — TFW-13: tfw-init Workflow | 2026-03-30*
