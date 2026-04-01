# ONB — TFW-14: Research Interaction Model

> **Дата**: 2026-04-01
> **Автор**: Executor (AI)
> **Статус**: 🟠 ONB — Ожидает ответов
> **Parent HL**: [HL-TFW-14](HL-TFW-14__research_interaction_model.md)
> **TS**: [TS TFW-14](TS__TFW-14__research_interaction_model.md)

---

## 1. Understanding (как понял задачу)

Добавить в RESEARCH workflow 4 механизма взаимодействия и 1 фикс. **2 новых элемента:** Briefing Protocol (вход в research с планом и наводящими вопросами, turn-based) и Closure Protocol (выход с рекомендациями к HL update). **2 расширения:** Stage Handoff (расширение checkpoint — план следующего стейджа + вопрос) и Sufficiency Check (усиление Final Checkpoint: «хватит для финализации HL?»). **1 фикс:** skip-bias в plan.md (pros/cons формат, default = recommend research). 5 файлов: `research.md`, `RES.md`, `plan.md`, оба адаптера.

## 2. Entry Points (откуда начинать)

| # | File | Lines | What to change |
|---|------|-------|----------------|
| 1 | `.tfw/workflows/research.md` | L16-27 (after Research Mindset, before Process) | Insert Briefing Protocol |
| 2 | `.tfw/workflows/research.md` | L92-116 (Checkpoint section) | Extend with Stage Handoff |
| 3 | `.tfw/workflows/research.md` | L118-136 (after Final Checkpoint) | Insert Closure Protocol |
| 4 | `.tfw/workflows/research.md` | L118-136 (Final Checkpoint) | Update Sufficiency Check |
| 5 | `.tfw/workflows/research.md` | L144-168 (Agent Behavior Protocol) | Add Hard Rules + Anti-patterns |
| 6 | `.tfw/templates/RES.md` | L11-12 (after Research Context) | Insert Briefing section |
| 7 | `.tfw/templates/RES.md` | L63-66 (before Conclusion) | Insert Closure section |
| 8 | `.tfw/workflows/plan.md` | L68-85 (Phase 3.5) | Rewrite with pros/cons + HL gate |
| 9 | `.claude/commands/tfw-research.md` | L30-33 (Step 4) | Sync with new structure |
| 10 | `.agent/workflows/tfw-research.md` | L36-39 (Step 4) | Sync with new structure |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | Нет блокирующих вопросов | — |

## 4. Recommendations (suggestions, not blocking)

1. **Limits table update.** TS Step 4 меняет «per stage» на «per turn» (turn-based ритм). Таблица Limits в `research.md` (L183) говорит `Questions to user per stage | 3 | Hard`. Предлагаю обновить на `Questions to user per turn | 3 | Hard` для консистентности. TS не упоминает эту таблицу явно, но это прямое следствие turn-based смены.
2. **Verdict wording.** TS Step 4 меняет Final Checkpoint вопрос с «Sufficient for TS?» на «Sufficient for HL finalization?». Verdict line (L135) `Sufficient for TS / Need another pass` тоже нужно обновить на `Sufficient for HL finalization / Need another pass`. TS не упоминает эту строку, но это часть того же блока.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **research.md L151 consistency.** Hard Rule #4: «Max 3 questions per stage (hard limit)» — конфликтует с turn-based ритмом. Нужно заменить «per stage» → «per turn» здесь тоже, иначе агент получает противоречивые инструкции.

## 6. Inconsistencies with Code (spec vs reality)

1. Нет инконсистентностей — TS точно описывает текущее состояние файлов.

---

*ONB — TFW-14: Research Interaction Model | 2026-04-01*
