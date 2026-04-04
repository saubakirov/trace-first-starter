# HL — TFW-23: Templates English Standardization

> **Date**: 2026-04-04
> **Author**: Coordinator
> **Status**: 📝 HL_DRAFT — Awaiting review

---

## 1. Vision
Templates are the DNA of TFW — every artifact starts from a template. Currently 5 of 9 templates have mixed Russian/English content (RU headings, EN body, RU annotations). This creates inconsistency, wastes tokens, and confuses AI agents that work better with English prompts.

**Goal:** All templates → pure English. AI agents fill them in the user's language at runtime.

> "Templates are code. Code is English. Content is user's language."

## 2. Current State (As-Is)

| Template | Language | RU Elements |
|----------|----------|-------------|
| HL.md | Mixed | `Дата`, `Автор`, `Статус`, `Видение`, `Текущее состояние`, `Целевое состояние`, `Визуализация результата`, `Фазы`, `Принципы`, `Зависимости`, `Риски`, `Обоснование RESEARCH`, `Слепые зоны`, `Гипотезы`, `Фильтр`, `Риски незнания`, `Предлагаемый фокус`, `При провале` |
| TS.md | Mixed | `Дата`, `Автор`, `Статус`, `Цель`, `Затрагиваемые файлы`, `Файл`, `Действие`, `Описание`, `Бюджет`, `Риски фазы` |
| RF.md | Mixed | `Дата`, `Автор`, `Статус`, `Что сделано`, `Новые файлы`, `Файл`, `Описание`, `Изменённые файлы`, `Изменения`, `Ключевые решения`, `Верификация` |
| ONB.md | Mixed | `Дата`, `Автор`, `Статус`, RU annotations in parentheses |
| REVIEW.md | Mixed | `Дата`, `Автор` |
| RES.md | ✅ English | — |
| KNOWLEDGE.md | ✅ English | — |
| RELEASE.md | ✅ English | — |
| TOPIC_FILE.md | ✅ English | — |

**Token waste estimate:** ~150-200 tokens of Cyrillic per template × 5 templates = ~800-1000 wasted tokens per full task cycle (HL+TS+ONB+RF+REVIEW).

## 3. Target State (To-Be)

All 9 templates in `.tfw/templates/` use English for:
- Section headings
- Field labels (Date, Author, Status)
- Table headers
- Instructional text / annotations
- Placeholders

### 3.1 Result Visualization

```
BEFORE (HL.md):                          AFTER (HL.md):
┌────────────────────────┐               ┌────────────────────────┐
│ > **Дата**: YYYY-MM-DD │               │ > **Date**: YYYY-MM-DD │
│ > **Автор**: {author}  │               │ > **Author**: {author} │
│ > **Статус**: 📝 ...   │               │ > **Status**: 📝 ...   │
│                        │               │                        │
│ ## 1. Видение          │               │ ## 1. Vision           │
│ ## 2. Текущее состояние│     ───►      │ ## 2. Current State    │
│ ## 3. Целевое состояние│               │ ## 3. Target State     │
│ ## 7. Принципы         │               │ ## 7. Principles       │
│ ## 8. Зависимости      │               │ ## 8. Dependencies     │
│ ## 9. Риски            │               │ ## 9. Risks            │
│ ## 10. Обоснование ... │               │ ## 10. RESEARCH Case   │
└────────────────────────┘               └────────────────────────┘

Status labels:
  "📝 HL_DRAFT — Ожидает ревью"  →  "📝 HL_DRAFT — Awaiting review"
  "🟡 TS_DRAFT — Ожидает апрува" →  "🟡 TS_DRAFT — Awaiting approval"
  "🟠 ONB — Ожидает ответов"     →  "🟠 ONB — Awaiting answers"
  "🟢 RF — Выполнено"            →  "🟢 RF — Complete"
```

## 4. Phases

### Phase A: Template Standardization ✅
- Translate all 5 mixed-language templates to English (headings, field labels, table headers, instructional annotations)
- Use consistency table from [RES E1](RES__TFW-23__templates_english_standardization.md) for all translations
- Update KNOWLEDGE.md §3 legacy entry (line 133) to match new EN headings
- Preserve exact structure, section numbers, placeholders
- No content changes — only language

### Phase B: Content Language Config 🔴
- Add `tfw.content_language: en` to `PROJECT_CONFIG.yaml`
- Add a convention rule to `conventions.md`: agents fill content in the language from config
- Update `tfw-init` workflow: ask user for preferred content language during init
- Register in Config Sync Registry (`conventions.md` §12)

## 5. Definition of Done (DoD)

- ✅ 1. All 9 templates in `.tfw/templates/` are 100% English
- ✅ 2. Zero Cyrillic characters in any template file (headings, labels, tables, instructional annotations)
- ✅ 3. Section structure and numbering unchanged
- ✅ 4. Placeholder syntax (`{author}`, `{PREFIX}`, etc.) unchanged
- ✅ 5. No semantic drift — every EN heading maps 1:1 to the original RU heading (per RES consistency table)
- ✅ 6. KNOWLEDGE.md §3 legacy entry updated to match new heading names
- ✅ 7. `tfw.content_language` config key exists in PROJECT_CONFIG.yaml with default `en`
- ✅ 8. Convention rule documents how agents use `content_language`
- ✅ 9. `tfw-init` asks user for preferred content language

## 6. Definition of Failure (DoF)

- ❌ 1. Template structure changes (sections added/removed/renumbered)
- ❌ 2. Placeholder format changes
- ❌ 3. Inconsistent translation — same RU term translated differently across templates

**On failure:** revert, re-translate with consistency table.

## 7. Principles

1. **Templates = code** — code is English, always
2. **Content follows user** — AI fills templates in user's language, template structure stays English
3. **Zero semantic drift** — EN headings must carry the same meaning as RU originals
4. **Consistency across templates** — same field name everywhere (`Date`, `Author`, `Status`, `File`, `Description`, `Action`)
5. **Naming > Explanation (D28)** — heading names chosen to trigger correct agent behavior, not just describe content

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| None | ✅ |

## 9. Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Inconsistent translation across templates | Low | Medium | Use consistency table (§7 P4) |
| Existing filled artifacts reference old headings | N/A | N/A | Filled artifacts are not affected — templates change, not past outputs |

## 10. RESEARCH Case

> RESEARCH completed. See [RES](RES__TFW-23__templates_english_standardization.md) for full analysis.

### Hypotheses

| # | Hypothesis | Status | Evidence |
|---|----------|--------|----------|
| H1 | RES.md is already fully English | ✅ confirmed | File inspection |
| H2 | KNOWLEDGE.md, RELEASE.md, TOPIC_FILE.md are already English | ✅ confirmed | File inspection |
| H3 | No workflows reference template headings by RU name | ✅ confirmed | Grep: workflows use §numbers, not heading text (RES G4) |

### Key RES Decisions
- D1: English-only templates, content in user's language (industry standard)
- D2: 32-term consistency table built with D28 (Naming > Explanation)
- D3: `content_language` config deferred to future task
- D4: RU instructional annotations also need translation
- D5: KNOWLEDGE.md §3 legacy entry needs update

---

*HL — TFW-23: Templates English Standardization | 2026-04-04*
