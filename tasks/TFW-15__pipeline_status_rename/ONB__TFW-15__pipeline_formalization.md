# ONB — TFW-15: Pipeline Formalization

> **Дата**: 2026-04-01
> **Автор**: Executor (AI)
> **Статус**: 🟠 ONB — Ожидает ответов
> **Parent HL**: [HL-TFW-15](HL-TFW-15__pipeline_status_rename.md)
> **TS**: [TS TFW-15](TS__TFW-15__pipeline_formalization.md)

---

## 1. Understanding (как понял задачу)

Rename pipeline statuses from document-centric names (`🔵 HL`, `🟡 TS`) to process-centric names (`📝 HL_DRAFT`, `🟡 TS_DRAFT`) across 9 live files. Add a centralized status registry (`tfw.statuses`) to PROJECT_CONFIG.yaml with `role` field. Add Concept Taxonomy to glossary.md. Renumber `Phase 3.5` → `Phase 4` in plan.md and fix step numbering gap. Update REJECT verdict to a branching user decision point. No archive files touched.

## 2. Entry Points (откуда начинать)

| # | File | Key sections |
|---|------|-------------|
| 1 | `.tfw/PROJECT_CONFIG.yaml` | After `tfw.research` block (L40-44) |
| 2 | `.tfw/conventions.md` | §5 (L95-128) — pipeline, status table, verdicts |
| 3 | `.tfw/glossary.md` | Status Flow (L47-57), add Concept Taxonomy after |
| 4 | `.tfw/README.md` | Task Lifecycle (L122-143) — pipeline diagram + steps |
| 5 | `.tfw/workflows/plan.md` | L60, L68, L86, L64, L142-149 |
| 6 | `.tfw/workflows/research.md` | L278-281 — Status Transitions |
| 7 | `README.md` (root) | L90 Key Concepts, L125 TFW-15 row, L128 legend |
| 8 | `.tfw/templates/HL.md` | L5 — status label |
| 9 | `.tfw/templates/TS.md` | L5 — status label |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | **plan.md Phase renumber scope**: TS says Phase 3.5 → Phase 4 and Phase 4 → Phase 5. Current plan.md has `Phase 3.5: RESEARCH Gate` (L68) and `Phase 4: Decide Scope` (L86). Should the header text stay identical (just number changes), or should we also update `Phase 4: Decide Scope` → `Phase 5: Decide Scope & Write TS` (matching HL §2.5 title)? | **Да, обновить заголовок:** `Phase 4: RESEARCH Gate`, `Phase 5: Decide Scope & Write TS`. Title из HL §2.5 — правильный. |
| 2 | **plan.md step numbering**: Current steps jump 7 → 9 (L60, L64). TS Step 5.4 says "Renumber: 8→Notify, 9→Incorporate, 10→Repeat". Current L64-66 has steps labeled as `9. Notify`, `10. Incorporate`, `11. Repeat` — the actual gap is 7→9 (step 8 missing). Should I renumber to `8. Notify`, `9. Incorporate`, `10. Repeat`? | **Да, ренумеровать.** 8→Notify, 9→Incorporate, 10→Repeat. Далее step numbers в Phase 4/5 продолжают с 11. |

## 4. Recommendations (suggestions, not blocking)

1. **README.md TFW-15 row status**: TS Step 7 says update `🔵 HL` → `📝 HL_DRAFT` on L125. However the current row already shows `🟡 TS`. Since we're executing now, it should be `🟠 ONB` during ONB phase and `🟢 RF` after completion. I'll set it to `🟠 ONB` during execution and leave final status for the review workflow.
   > **✅ Coordinator:** Верно. Во время execution ставь `🟠 ONB`, при финализации RF — `🟢 RF`. Финальный статус ставит reviewer.
2. **conventions.md REJECT section**: TS specifies the branching pattern but the exact insertion point and format for replacing L124-128 should preserve the existing structure. I'll replace the `❌ REJECT` bullet with the new branching format inline.
   > **✅ Coordinator:** Согласен. Сохрани структуру bullet list, замени только текст `❌ REJECT` пункта.
3. **`.tfw/README.md` step list** (L133-143): TS Step 4 mentions updating "step 1 references and REJECT verdict wording". The current REJECT text at L142 says `❌ REJECT — fundamental issues, rethink from HL/TS.` — I'll update to match the new branching pattern from conventions.
   > **✅ Coordinator:** Да, обновить REJECT wording чтобы соответствовал conventions.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **plan.md L81 reference to "Phase 4"**: Line says `proceed to Phase 4`. After renumber this becomes `proceed to Phase 5`. TS doesn't mention this cross-reference explicitly — need to update it.
   > **✅ Coordinator:** Правильно пойман. Обнови все `Phase 4` refs в body → `Phase 5`. Это in-scope (touching same file).
2. **plan.md L84 "Phase 4"**: Line says `proceed directly to Phase 4`. Same renumber issue.
   > **✅ Coordinator:** Аналогично, обнови.
3. **plan.md L88 "After HL is approved"**: This is Phase 4 (old) → Phase 5 (new) header context. Need to verify all `Phase 4` references in plan.md text body, not just headers.
   > **✅ Coordinator:** Grep `Phase 4` in plan.md, замени все на `Phase 5`. Заголовок `Phase 4` = RESEARCH Gate (новый).

## 6. Inconsistencies with Code (spec vs reality)

1. **TS line references vs actual**: TS Step 5.4 says `Step 8 (L60)` for `🔵 HL` ref — actual `🔵 HL` is at L60 (`status 🔵 HL`), confirmed.
2. **TS says step gap is 7→9 at L64**: Actual plan.md L64 is `9. **Notify user**` — confirmed, step 8 is indeed missing.
3. **conventions.md L119-122 "Task Board format"**: TS mentions updating status example here. Actual content at L119-122 is the Task Board format code block with `[PROJ-1]` example — no pipeline status in this block, just the link format. The status example referenced may be the legend at the bottom of the file or in the example. Will check during execution.
   > **✅ Coordinator:** Верный catch. В conventions.md нет отдельной legend. Пропусти этот sub-item для conventions.
4. **TS Step 2 mentions "Task Board legend (L128)"** in conventions.md — but L128 is `- ❌ **REJECT** — fundamental problems → new task with HL/TS`. There is no separate "Task Board legend" in conventions.md. This may be a reference confusion with root README.md L128. I'll skip this sub-item for conventions.md and handle the legend only in root README.md where it actually exists.
   > **✅ Coordinator:** Да, это ошибка в TS — перепутал с root README.md. Legend обновляем только в root README.md L128.

---

*ONB — TFW-15: Pipeline Formalization | 2026-04-01*
