# RF — TFW-23 / Phase A: Templates English Standardization

> **Date**: 2026-04-04
> **Author**: Executor
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-23](HL-TFW-23__templates_english_standardization.md)
> **TS**: [TS Phase A](TS__TFW-23__templates_english_standardization.md)

---

## 1. What Was Done

### Modified Files
| File | Changes |
|------|---------|
| `.tfw/templates/HL.md` | Translated 18+ RU terms to EN per RES E1 table. Replaced §3.1 instructional block with domain-agnostic Variant A. Replaced §10 filter with EN translation |
| `.tfw/templates/TS.md` | Translated 6 RU terms (Дата, Автор, Статус, Цель→Objective, Затрагиваемые файлы→Affected Files, Бюджет→Budget, Риски фазы→Phase Risks) |
| `.tfw/templates/RF.md` | Translated 8 RU terms (header fields, Что сделано→What Was Done, Новые файлы→New Files, Изменённые файлы→Modified Files, Ключевые решения→Key Decisions, Верификация→Verification) |
| `.tfw/templates/ONB.md` | Translated header fields, removed RU parenthetical annotations from Understanding and Entry Points sections |
| `.tfw/templates/REVIEW.md` | Translated 2 RU fields (Дата→Date, Автор→Author) |
| `KNOWLEDGE.md` | Updated line 133: `§3.1 Визуализация результата` → `§3.1 Result Visualization`, `§10 Обоснование RESEARCH` → `§10 RESEARCH Case` |

## 2. Key Decisions

1. **§3.1 instructional block rewritten, not just translated** — Original was too engineering-focused (ASCII diagrams, Mermaid, file structure). Replaced with domain-agnostic Variant A per user direction (RES D7). Now covers diagrams, tables, outlines/mockups, and sample output
2. **Templates overwritten via `write_to_file` (not patched)** — HL, TS, RF, ONB templates had pervasive changes. Full rewrite was cleaner than multi-chunk patches. REVIEW.md was patched (only 2 fields)

## 3. Acceptance Criteria

- [x] Zero Cyrillic characters in `.tfw/templates/` (verified by Python script)
- [x] All 32 terms from RES E1 consistency table applied correctly
- [x] Section structure and numbering identical to pre-change
- [x] KNOWLEDGE.md §3 legacy entry updated
- [x] No semantic drift — same meaning, English words

## 4. Verification

- Cyrillic check (`python -c "...cyrillic regex..."`): **PASS** — zero Cyrillic characters found
- Section structure: manually verified all § numbers preserved in HL (1-10), TS (1-6), RF (1-6), ONB (1-6), REVIEW (1-5)

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/CHANGELOG.md` | 17 | naming | Has `Визуализация результата` in historical entry — not updated (historical record, not active template) |
| 2 | `tasks/` | various | naming | Existing filled artifacts (past HLs, TSs, RFs) still use RU headings — as expected per TS Out of Scope |

## 6. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | convention | Templates = English always; filled content = user's language. Template structure is code, code is English | User direction + RES G1 | High |
| 2 | process | D28 (Naming > Explanation) applies to template heading names — not just workflow terms. Heading names should trigger correct agent behavior | RES E1 + C2 analysis | High |
| 3 | process | When AI crashes mid-workflow and user presses "continue", all 🛑 WAIT gates are lost. 6/6 gates were violated in this session's research phase. Crash recovery is not built into TFW — need mechanism to re-read workflow + determine current gate | Session observation | High |
| 4 | convention | §3.1 Result Visualization instruction must be domain-agnostic — TFW is not code-only. User: "на уровне HL мыслить надо иначе, через ценности, процессы" | User feedback during gate review | High |

---

*RF — TFW-23 / Phase A: Templates English Standardization | 2026-04-04*
