# ONB — TFW-11 / Phase A: Core — Артефакт, статус, воркфлоу

> **Дата**: 2026-03-30
> **Автор**: Executor (AI)
> **Статус**: 🟠 ONB — Ожидает ответов
> **Parent HL**: [HL-TFW-11](HL-TFW-11__research_stage.md)
> **TS**: [TS Phase A](TS__PhaseA__core_artifact_workflow.md)

---

## 1. Understanding (как понял задачу)

Создать ядро RESEARCH-стадии TFW: шаблон RES-артефакта (`.tfw/templates/RES.md`), воркфлоу research.md (`.tfw/workflows/research.md`), обновить conventions.md (новый статус 🔬 RES, артефакт, пайплайн, naming, workflows, role lock), glossary.md (4 новых термина), и PROJECT_CONFIG.yaml (секция `research:`). Всего 2 новых файла + 3 модификации. Фаза не затрагивает интеграцию (plan.md, адаптеры, README pipeline) — это Phase B.

## 2. Entry Points (откуда начинать)

| Файл | Роль |
|------|------|
| `.tfw/templates/RES.md` | CREATE — шаблон по Step 1 из TS |
| `.tfw/workflows/research.md` | CREATE — воркфлоу по Step 2 из TS |
| `.tfw/conventions.md` | MODIFY — §3, §4, §5, §8, §15 |
| `.tfw/glossary.md` | MODIFY — новые термины в секцию Artifact Types |
| `.tfw/PROJECT_CONFIG.yaml` | MODIFY — секция `research:` + `tfw.templates.res` |
| `RES__TFW-11__research_stage.md` | READ — живой пример RES-артефакта для сверки |
| `.tfw/workflows/plan.md` | READ — стиль для нового воркфлоу |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | Нет блокирующих вопросов | — |

## 4. Recommendations (suggestions, not blocking)

1. **`tfw.templates.res` в PROJECT_CONFIG.yaml** — TS Step 5 упоминает только секцию `research:`, но все остальные шаблоны (hl, ts, rf, onb, review) зарегистрированы в `tfw.templates`. Предлагаю добавить `res: .tfw/templates/RES.md` для консистентности. Файл уже в scope (MODIFY).

2. **Язык шаблона RES.md** — Существующие шаблоны (HL, RF, ONB) используют русские заголовки секций + английские инструкции внутри. TS Step 1 показывает RES с русскими заголовками и русскими placeholder-инструкциями. Предлагаю следовать TS-шаблону максимально близко, сохраняя русские заголовки (как в HL.md), с минимальными английскими пояснениями в фигурных скобках — как это уже сделано в TS Step 1.

3. **Skip-path в ASCII-диаграмме** — TS Step 3 требует "пунктирную линию HL → TS". Предлагаю реализовать как дополнительную строку под основным пайплайном: `(skip: 🔵 HL ··· 🟡 TS)` — компактно, видно.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Временная рассинхронизация пайплайнов** — conventions.md и glossary.md покажут 🔬 RES в пайплайне, но plan.md, handoff.md и README.md останутся с 7-статусным пайплайном до Phase B. Это ожидаемо по design (TS Out of Scope), но стоит помнить при Phase B.

2. **research.md может превысить ~100 строк** — TS Risk #1 ссылается на plan.md ≈ 100 строк как ориентир. Однако research.md содержит два режима (pipeline + standalone), 3 этапа с описаниями поведения, checkpoint-формат и лимиты. Буду стремиться к компактности, но ~120-140 строк реалистичнее.

## 6. Inconsistencies with Code (spec vs reality)

1. **Счёт статусов** — TS acceptance criteria говорит "8 → 9 статусов", но conventions.md §5 перечисляет 7 основных + BLOCKED = 8 всего. С добавлением RES станет 8 основных + BLOCKED = 9. Формулировка TS корректна если считать BLOCKED.

---

*ONB — TFW-11 / Phase A: Core — Артефакт, статус, воркфлоу | 2026-03-30*
