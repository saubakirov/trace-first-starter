# TS — TFW-23 / Phase A: Templates English Standardization

> **Date**: 2026-04-04
> **Author**: Coordinator
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-23](HL-TFW-23__templates_english_standardization.md)

---

## 1. Objective
Translate all 5 mixed-language templates from Russian/English to pure English, applying the consistency table from [RES E1](RES__TFW-23__templates_english_standardization.md). Update KNOWLEDGE.md legacy entry to match.

## 2. Scope

### In Scope
- Translate headings, field labels, table headers, instructional annotations in: HL.md, TS.md, RF.md, ONB.md, REVIEW.md
- Apply RES E1 consistency table for all term choices
- Update KNOWLEDGE.md §3 legacy entry (line 133)

### Out of Scope
- Changing template structure (no sections added/removed/renumbered)
- Adding `content_language` config to PROJECT_CONFIG.yaml (future task)
- Changing workflow files
- Changing filled artifacts in `tasks/`

## 3. Affected Files

| File | Action | Description |
|------|--------|------------|
| `.tfw/templates/HL.md` | MODIFY | Translate all RU headings, field labels, status labels, instructional annotations (§3.1, §10 filter) |
| `.tfw/templates/TS.md` | MODIFY | Translate all RU headings, field labels, status labels |
| `.tfw/templates/RF.md` | MODIFY | Translate all RU headings, field labels, status labels |
| `.tfw/templates/ONB.md` | MODIFY | Translate RU field labels, status labels, remove RU parenthetical annotations |
| `.tfw/templates/REVIEW.md` | MODIFY | Translate RU field labels |
| `KNOWLEDGE.md` | MODIFY | Update line 133 — replace `§3.1 Визуализация результата` with `§3.1 Result Visualization`, `§10 Обоснование RESEARCH` with `§10 RESEARCH Case` |

**Budget:** 0 new files, 6 modifications. Defaults: max 14 files, max 8 new, max 1200 LOC.

## 4. Detailed Steps

### Step 1: Translate HL.md
Apply RES E1 consistency table:
- Header: `Дата` → `Date`, `Автор` → `Author`, `Статус: 📝 HL_DRAFT — Ожидает ревью` → `Status: 📝 HL_DRAFT — Awaiting review`
- §1 `Видение` → `Vision`
- §2 `Текущее состояние (As-Is)` → `Current State (As-Is)`
- §3 `Целевое состояние (To-Be)` → `Target State (To-Be)`
- §3.1 `Визуализация результата` → `Result Visualization`
- §3.1 instructional block (lines 23-28): replace with domain-agnostic Variant A (RES D7):
  ```
  > Show the outcome as if it's already achieved. Choose the format that fits:
  > - **Diagrams** (architecture, flow, structure) — ASCII, mermaid, or hand-drawn
  > - **Before → After tables** — state comparison
  > - **Outlines / mockups** — document structure, UI sketches, report layout
  > - **Sample output** — example paragraph, data snippet, formula result
  >
  > Goal: executor and user must see the "finished picture" before work begins.
  ```
- §4 `Фазы` → `Phases`
- §7 `Принципы` → `Principles`
- §7.1 already English — keep
- §8 `Зависимости` → `Dependencies`, table: `Зависимость | Статус` → `Dependency | Status`
- §9 `Риски` → `Risks`, table: `Риск | Вероятность | Влияние | Mitigation` → `Risk | Probability | Impact | Mitigation`, values: `Низкая/Средняя/Высокая` → `Low/Medium/High`, `Низкое/Среднее/Высокое` → `Low/Medium/High`
- §10 `Обоснование RESEARCH` → `RESEARCH Case`
- §10.1 `Слепые зоны` → `Blind Spots`
- §10.2 `Гипотезы` → `Hypotheses`, table: `Гипотеза | Статус` → `Hypothesis | Status`
- §10 filter (line 88): replace with:
  ```
  > **Filter:** Each hypothesis: "If proven false, would our approach change?" If no — remove.
  ```
- §10.3 `Риски незнания` → `Risks of Not Researching`
- §10.4 `Предлагаемый фокус RESEARCH` → `Proposed RESEARCH Focus`
- Footer `При провале` → `On failure`

### Step 2: Translate TS.md
- Header: same as HL (Date, Author, Status)
- `Статус: 🟡 TS_DRAFT — Ожидает апрува` → `Status: 🟡 TS_DRAFT — Awaiting approval`
- §1 `Цель` → `Objective`
- §3 `Затрагиваемые файлы` → `Affected Files`, table: `Файл | Действие | Описание` → `File | Action | Description`
- §3 note `Бюджет` → `Budget`
- §6 `Риски фазы` → `Phase Risks`, table: `Риск | Mitigation` → `Risk | Mitigation`

### Step 3: Translate RF.md
- Header: same + `Статус: 🟢 RF — Выполнено` → `Status: 🟢 RF — Complete`
- §1 `Что сделано` → `What Was Done`
- §1.1 `Новые файлы` → `New Files`, table: `Файл | Описание` → `File | Description`
- §1.2 `Изменённые файлы` → `Modified Files`, table: `Файл | Изменения` → `File | Changes`
- §2 `Ключевые решения` → `Key Decisions`
- §4 `Верификация` → `Verification`

### Step 4: Translate ONB.md
- Header: same + `Статус: 🟠 ONB — Ожидает ответов` → `Status: 🟠 ONB — Awaiting answers`
- §1 `Understanding (как понял задачу)` → `Understanding` (drop RU annotation)
- §2 `Entry Points (откуда начинать)` → `Entry Points` (drop RU annotation)

### Step 5: Translate REVIEW.md
- Header: `Дата` → `Date`, `Автор` → `Author`
- All other sections already English

### Step 6: Update KNOWLEDGE.md
- Line 133: replace RU heading references with EN equivalents

### Step 7: Verify
- Run: `grep -rP '[\x{0400}-\x{04FF}]' .tfw/templates/` — must return 0 results
- Visually verify section numbering unchanged in all 5 templates

## 5. Acceptance Criteria

- [ ] Zero Cyrillic characters in `.tfw/templates/` (verified by grep)
- [ ] All 32 terms from RES E1 consistency table applied correctly
- [ ] Section structure and numbering identical to pre-change (diff shows only text changes)
- [ ] KNOWLEDGE.md §3 legacy entry updated
- [ ] No semantic drift — same meaning, English words

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| Typo or inconsistency in translation | Follow RES E1 table exactly; grep for Cyrillic as final check |
| Missed RU text in instructional annotations | Grep verification catches any remaining Cyrillic |

---

*TS — TFW-23 / Phase A: Templates English Standardization | 2026-04-04*
