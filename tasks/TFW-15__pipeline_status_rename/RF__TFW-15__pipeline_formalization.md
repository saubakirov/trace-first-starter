# RF — TFW-15: Pipeline Formalization

> **Дата**: 2026-04-01
> **Автор**: Executor (AI)
> **Статус**: 🟢 RF — Выполнено
> **Parent HL**: [HL-TFW-15](HL-TFW-15__pipeline_status_rename.md)
> **TS**: [TS TFW-15](TS__TFW-15__pipeline_formalization.md)

---

## 1. Что сделано

### Новые файлы

None.

### Изменённые файлы

| Файл | Изменения |
|------|-----------|
| `.tfw/PROJECT_CONFIG.yaml` | Added `tfw.statuses` registry (9 entries with `role` field) |
| `.tfw/conventions.md` | §5: pipeline diagram → `HL_DRAFT`/`TS_DRAFT`, status table updated, REJECT = branching user decision |
| `.tfw/glossary.md` | Status Flow diagram updated, Concept Taxonomy section added (5 concepts) |
| `.tfw/README.md` | Task Lifecycle pipeline diagram updated, REJECT verdict wording updated |
| `.tfw/workflows/plan.md` | Phase 3.5→Phase 4 (RESEARCH Gate), Phase 4→Phase 5 (Decide Scope & Write TS), steps 8/9/10 renumbered, `🔵 HL`→`📝 HL_DRAFT`, body Phase refs updated, pipeline diagram updated |
| `.tfw/workflows/research.md` | Status Transitions section: `HL_DRAFT`/`TS_DRAFT` |
| `README.md` (root) | Key Concepts pipeline, Task Board legend, TFW-15 row status |
| `.tfw/templates/HL.md` | `🔵 HL — Ожидает ревью` → `📝 HL_DRAFT — Ожидает ревью` |
| `.tfw/templates/TS.md` | `🟡 TS — Ожидает апрува` → `🟡 TS_DRAFT — Ожидает апрува` |

## 2. Ключевые решения

1. **Phase title from HL §2.5**: Phase 5 renamed to `Decide Scope & Write TS` (per coordinator answer in ONB Q1)
2. **Step numbering continues from 11**: Phase 4/5 step numbers start from 11 (per coordinator answer in ONB Q2)
3. **conventions.md "Task Board legend"**: Skipped (TS line ref error — confirmed by coordinator as root README.md reference)

## 3. Acceptance Criteria

- [x] 1. Pipeline string `⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → 🟢 RF → 🔍 REV → ✅ DONE` present in all 7 pipeline locations
- [x] 2. `tfw.statuses` block in PROJECT_CONFIG.yaml with 9 entries and `role` field
- [x] 3. conventions.md status table has `📝 HL_DRAFT` and `🟡 TS_DRAFT`
- [x] 4. conventions.md REJECT = branching user decision point
- [x] 5. glossary.md has Concept Taxonomy section
- [x] 6. plan.md: no `Phase 3.5` (header renamed to `Phase 4`), no step gap
- [x] 7. research.md: Status Transitions use `HL_DRAFT` / `TS_DRAFT`
- [x] 8. HL.md template: `📝 HL_DRAFT — Ожидает ревью`
- [x] 9. TS.md template: `🟡 TS_DRAFT — Ожидает апрува`
- [x] 10. Grep `🔵 HL` in `.tfw/` (excluding CHANGELOG.md) → 0 results
- [x] 11. Grep `Phase 3.5` in `.tfw/` (excluding CHANGELOG.md) → 0 results
- [x] 12. No archived files (`tasks/TFW-{1..14}/`) modified

## 4. Верификация

- Grep `🔵 HL` in `.tfw/`: **0 results** ✅
- Grep `🔵 HL` in root `README.md`: **0 results** ✅
- Grep `Phase 3.5` in `.tfw/`: **only CHANGELOG.md** (historical, out of scope) ✅
- Archived files diff (`tasks/TFW-{1..14}`): **0 files changed** ✅

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/glossary.md` | 60 | naming | RESEARCH glossary entry still says "between HL and TS" — should say "between HL_DRAFT and TS_DRAFT" for consistency, but this is prose description of document types, not statuses |
| 2 | `.tfw/README.md` | 133-134 | naming | Step list uses "Write an HL" / "Write a TS" — refers to document types (correct), but step 1 status reference is implicit. Low priority |
| 3 | `.tfw/conventions.md` | 222 | style | Role Lock table still says "Forbidden Artifacts" — column name is fine but `handoff.md` row says "code" in Forbidden, while executor role forbids writing code AND HL/TS/RES/REVIEW. Minor table-vs-workflow mismatch |
| 4 | `.tfw/workflows/plan.md` | 155 | naming | Anti-pattern "Do not write TS without updating HL after RESEARCH" — uses document type names, not status names. Correct as-is (anti-patterns describe actions on documents, not status transitions) |

> **Types:** `dead-code`, `naming`, `todo`, `duplication`, `perf`, `security`, `style`, `missing-test`, `ux`

---

*RF — TFW-15: Pipeline Formalization | 2026-04-01*
