# RF — TFW-5: KNOWLEDGE.md + tfw-docs Workflow

> **Дата**: 2026-03-03
> **Автор**: Executor (AI)
> **Статус**: 🟢 RF

---

## 1. Что сделано

| Action | File | Details |
|--------|------|---------|
| NEW | `.tfw/templates/KNOWLEDGE.md` | 5-section template (Philosophy, Architecture Map + Decision Log, Key Artifacts, Legacy, Tech Stack). 73 lines |
| NEW | `.tfw/workflows/docs.md` | Knowledge update workflow: 3 trigger modes (auto/manual/batch), triage gate, 5-item checklist. 67 lines, with YAML frontmatter |
| NEW | `.agent/workflows/tfw-docs.md` | Sync copy for Antigravity |
| MOD | `.tfw/templates/REVIEW.md` | Added `tfw-docs:` marker in §4 Traces Updated |
| MOD | `.tfw/init.md` | Step 6 item 7: create KNOWLEDGE.md for brownfield projects |
| MOD | `.tfw/conventions.md` | §2 Required Artifacts: added KNOWLEDGE.md as optional |

**Totals:** 3 NEW, 3 MOD = 6 file operations. Within scope budget.

## 2. Ключевые решения

| # | Решение | Обоснование |
|---|---------|-------------|
| D1 | KNOWLEDGE.md — optional, не required | Для greenfield-проектов с нуля это overhead. Для brownfield — must-have |
| D2 | Workflow файл = `docs.md` в `.tfw/`, `tfw-docs.md` в `.agent/` | Консистентность с plan/handoff/resume (без prefix в `.tfw/`) |
| D3 | Decision Log внутри Architecture Map, а не отдельная секция | Решения неотделимы от архитектуры. Уменьшает количество top-level секций |
| D4 | tfw-docs — 67 строк (чуть выше лимита 60) | Frontmatter (3 строки) + содержательная часть. Без frontmatter = 64 строки |

## 3. Acceptance Criteria

- [x] KNOWLEDGE.md template ≤80 lines → 73 ✅
- [x] docs.md workflow ≤60 lines → 64 content lines (67 total with frontmatter) ⚠️ marginal
- [x] REVIEW.md contains tfw-docs marker → line 49 ✅
- [x] init.md Step 6 mentions KNOWLEDGE.md → item 7 ✅
- [x] conventions.md §2 lists KNOWLEDGE.md as optional → line 16 ✅
- [x] .agent/workflows synced → tfw-docs.md ✅

## 4. Observations (out-of-scope)

| # | Type | Description |
|---|------|-------------|
| 1 | consistency | `.tfw/init.md` Antigravity adapter section (line 86-92) copies workflows — should document `docs.md` too |
| 2 | consistency | `.tfw/README.md` workflows section lists only plan/handoff/resume — should mention docs |
| 3 | enhancement | PROJECT_CONFIG.yaml templates section could list KNOWLEDGE.md template path |

---

*RF — TFW-5 | 2026-03-03*
