# ONB — TFW-13 / Phase B: Adapter Docs + References Cleanup

> **Дата**: 2026-03-30
> **Автор**: Executor (AI)
> **Статус**: 🟠 ONB — Ожидает ответов
> **Parent HL**: [HL-TFW-13](HL-TFW-13__tfw_init_workflow.md)
> **TS**: [TS Phase B](TS__PhaseB__docs_and_cleanup.md)

---

## 1. Understanding (как понял задачу)

Phase B — документация и интеграция: (1) перенести "How to Write a New Adapter" в `.tfw/adapters/README.md`; (2) обновить conventions.md (§2, §8, §15), glossary.md, Antigravity README, PROJECT_CONFIG.yaml, KNOWLEDGE.md. 1 новый файл, 5 модификаций.

## 2. Entry Points (откуда начинать)

| Файл | Роль |
|------|------|
| `.tfw/adapters/README.md` | CREATE — adapter docs (Step 1) |
| `.tfw/conventions.md` | MODIFY — §2, §8, §15 (Step 2) |
| `.tfw/glossary.md` | MODIFY — add tfw-init term (Step 3) |
| `.tfw/adapters/antigravity/README.md` | MODIFY — add tfw-init to instructions (Step 4) |
| `.tfw/PROJECT_CONFIG.yaml` | MODIFY — add init to workflows (Step 5) |
| `KNOWLEDGE.md` | MODIFY — D18 + TFW-13 artifact (Step 6) |

## 3. Questions (blocking — cannot proceed without answers)

Нет блокирующих вопросов. TS достаточно подробный для всех шагов.

## 4. Recommendations (suggestions, not blocking)

1. TS Step 1 содержит `{markdown}` / `{/markdown}` как pseudo-tags для вложенного code block. Отрендерю как обычный fenced code block с backticks.

## 5. Risks Found (edge cases, potential issues not in TS)

1. Conventions §2 не перечисляет review.md, docs.md, release.md, update.md — pre-existing gap, только plan/research/handoff/resume. Добавлю init.md per TS, но остальные пропуски зафиксирую в Observations.
2. Conventions §8 table не содержит research.md — pre-existing gap. Зафиксирую в Observations.
3. Conventions §15 Role Lock table не содержит docs.md, release.md, update.md — pre-existing gap. Зафиксирую в Observations.
4. Antigravity README lists only 4 workflows (plan, handoff, review, resume) — research, docs, release, update отсутствуют. Добавлю только init per TS scope.

## 6. Inconsistencies with Code (spec vs reality)

Нет расхождений spec vs reality для файлов в scope.

---

*ONB — TFW-13 / Phase B: Adapter Docs + References Cleanup | 2026-03-30*
