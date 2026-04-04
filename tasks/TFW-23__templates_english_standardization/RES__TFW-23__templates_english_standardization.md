# RES — TFW-23: Templates English Standardization

> **Date**: 2026-04-04
> **Author**: Coordinator
> **Status**: 🔬 RES — In progress
> **Parent HL**: [HL-TFW-23](HL-TFW-23__templates_english_standardization.md)
> **Mode**: Pipeline / Focused

---

## Research Context
5 of 9 TFW templates have mixed Russian/English content. Goal: standardize all to English. This research validates the approach — translation consistency, community practices for multilingual template frameworks, and whether any downstream artifacts/workflows would break.

## Briefing

### Research Plan
1. **Gather** — How do other AI workflow frameworks handle template language? Is English-only the standard? Any multi-language template approaches worth considering?
2. **Extract** — Scan existing project artifacts (filled RFs, TSs, HLs) for patterns: do agents already mix section heading language when filling? Do workflows reference specific RU heading text?
3. **Challenge** — Is pure English the right call? Could we lose something by removing RU? Should we consider i18n placeholders instead of hardcoded English?

### Scope Intent
- **In scope:** Template language standardization approach, translation consistency table, downstream impact analysis
- **Out of scope:** Changing workflow files, changing conventions.md, changing filled artifacts

### Guiding Questions
1. Do you have any preference for specific English terms for ambiguous translations (e.g., "Целевое состояние" → "Target State" vs "Desired State" vs "To-Be")?
2. Should the `Статус` line use the same phrasing as PROJECT_CONFIG status descriptions, or keep the current human-friendly labels?
3. Is there any plan to support non-English users who might fork this repo and want templates in their language?

### Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | RES.md is already fully English | confirmed | ✅ confirmed | Verified by reading file |
| H2 | KNOWLEDGE.md, RELEASE.md, TOPIC_FILE.md are already English | confirmed | ✅ confirmed | Verified by reading files |
| H3 | No workflows reference template headings by RU name | open | 🟡 testing | |

→ User direction: ___

## Decisions
| # | Decision | Rationale |
|---|----------|-----------|
| D1 | English-only templates, content filled in user's language | Industry standard (G1). Templates = code → code is English |
| D2 | Use consistency table from E1 for all translations | D28: "right terminology creates right associations". 32 terms mapped |
| D3 | `content_language` config deferred to future task | Challenge C1: mixing features violates scope. TFW-20 or new task |
| D4 | Translate RU instructional annotations too, not just headings | Challenge C3: instructions are part of template structure |
| D5 | Update KNOWLEDGE.md §3 legacy entry to match new EN headings | Challenge C4: avoid confusion when agents read legacy table |
| D6 | H3 confirmed: workflows reference §numbers, not heading text | Grep verification (G4). Renaming is safe |
| D7 | §3.1 instructional block: Variant A (principle + domain examples). §10 filter: literal translation. Both rewritten to be domain-agnostic — TFW is not code-only | User feedback: HL instructions too tech-focused, TFW serves education, business, research too |

## Open Questions
| # | Question | Status | Answer |
|---|----------|--------|--------|
| 1 | Best EN terms for ambiguous RU headings? | ✅ resolved | Consistency table in E1 — D28 applied to each term |
| 2 | Status line phrasing source? | ✅ resolved | Short labels: "Awaiting review", "Awaiting approval", "Complete" |
| 3 | i18n / fork considerations? | ✅ resolved | Document principle in HL. `content_language` config = future task |

---

## Stage: Gather — "What do we NOT know?"

### G1: External i18n practices for AI prompt templates
External research confirms: **English structure + localized content** is the industry standard pattern.
Key finding: "Language-Agnostic Core — keep the core system logic consistent across all languages. Only localize the tone, style, and cultural adaptation parts."
This is exactly what TFW needs — templates = core logic (English), filled content = user language.

### G2: Template i18n architecture options

| Option | Description | Complexity | Fit |
|--------|-------------|-----------|-----|
| A. English-only templates | Templates in EN, agents fill in user's language | Low | ✅ Best — simple, no infra |
| B. Locale directories | `templates/en/HL.md`, `templates/ru/HL.md` | High | ❌ File explosion, sync nightmare |
| C. YAML key-value i18n | `{t.vision}` placeholders, resolved from locale file | Medium | ❌ Over-engineered for markdown |
| D. Config-driven content language | `tfw.content_language: en` in config, agent uses it for filling | Low | ✅ Good — configurable without file duplication |

**Conclusion:** Option A + D hybrid is best. Templates stay English (Option A). Config has `tfw.content_language` (Option D) that tells the agent which language to use when **filling** the template. Default = `en`. During `tfw-init`, ask user preferred language.

### G3: Naming — D28 principle application
Per D28 ("Naming > Explanation") and P5 ("right terminology creates right associations"):
- Section headings should use **evocative, standard AI/engineering terms** that trigger correct behavior
- External research confirms: "Use Title Case for headings", "Keep labels concise, intuitive, and consistent"
- The same external sources use: "ROLE", "CONTEXT", "TASK", "CONSTRAINTS", "OUTPUT FORMAT" — short, imperative

### G4: H3 verification (workflow heading references)
Grep confirmed: workflows reference sections by **§ number** (§3.1, §10), never by heading text. Zero RU heading references in any workflow file. Renaming headings is safe.

### Checkpoint: Gather
| Found | Remaining |
|-------|-----------|
| i18n best practice = EN structure, localized content | — |
| 4 architecture options evaluated, A+D hybrid selected | — |
| D28 naming principle applicable to heading translation | translation table (→ Extract) |
| H3 confirmed: no workflow refs to RU headings | — |

**Sufficiency Verdict:**
- [x] External source used? (3 web searches)
- [x] Briefing gap closed? (Research Plan #1: how frameworks handle template language)

**Agent assessment:** Gather is sufficient. Architecture decision made (A+D hybrid). H3 confirmed.
**Depth check:** 3 external web searches used (i18n practices, naming conventions, locale config patterns).
**Recommendation:** close stage, move to Extract for naming table
Stage complete: YES
→ User decision: ___

## Stage: Extract — "What do we NOT see?"

### E1: Translation Consistency Table (applying D28: Naming > Explanation)

**Method:** For each RU heading, identify the behavior it should trigger in the agent. Then find the shortest English term that the AI already associates with that behavior (D28: "right terminology creates right associations").

#### Common fields (all templates)

| RU Original | EN Translation | D28 Rationale |
|-------------|---------------|---------------|
| `Дата` | `Date` | Universal |
| `Автор` | `Author` | Universal |
| `Статус` | `Status` | Universal |
| `Ожидает ревью` | `Awaiting review` | Short, clear intent |
| `Ожидает апрува` | `Awaiting approval` | Standard process term |
| `Ожидает ответов` | `Awaiting answers` | Direct, no ambiguity |
| `Выполнено` | `Complete` | Shortest possible |

#### HL template

| § | RU Original | Candidate A | Candidate B | **Winner** | D28 Rationale |
|---|-------------|-------------|-------------|------------|---------------|
| 1 | `Видение` | `Vision` | `Goal` | **Vision** | Standard strategic planning term; agents associate it with "why + business value" |
| 2 | `Текущее состояние (As-Is)` | `Current State (As-Is)` | `As-Is` | **Current State (As-Is)** | Already has EN annotation; keep both for scan-ability |
| 3 | `Целевое состояние (To-Be)` | `Target State (To-Be)` | `To-Be` | **Target State (To-Be)** | Mirror of §2 |
| 3.1 | `Визуализация результата` | `Result Visualization` | `Outcome Preview` | **Result Visualization** | Agents associate "visualization" with diagrams/ascii — exactly what we want |
| 4 | `Фазы` | `Phases` | `Roadmap` | **Phases** | Direct translation; TFW uses "Phase" heavily |
| 5 | `Definition of Done (DoD)` | — | — | **Keep** | Already EN |
| 6 | `Definition of Failure (DoF)` | — | — | **Keep** | Already EN |
| 7 | `Принципы` | `Principles` | `Design Philosophy` | **Principles** | Short, standard. Section body already says "Design philosophy" |
| 8 | `Зависимости` | `Dependencies` | `Prerequisites` | **Dependencies** | Standard engineering term |
| 8 tbl | `Зависимость \| Статус` | `Dependency \| Status` | — | **Dependency \| Status** | Direct |
| 9 | `Риски` | `Risks` | — | **Risks** | Universal |
| 9 tbl | `Риск \| Вероятность \| Влияние` | `Risk \| Probability \| Impact` | `Risk \| Likelihood \| Severity` | **Risk \| Probability \| Impact** | Standard risk matrix terms |
| 9 tbl | `Низкая/Средняя/Высокая` | `Low/Medium/High` | — | **Low/Medium/High** | Universal |
| 10 | `Обоснование RESEARCH` | `RESEARCH Case` | `RESEARCH Justification` | **RESEARCH Case** | Shorter. "Case" = argument. Agents associate "case" with "make this argument" |
| 10.1 | `Слепые зоны` | `Blind Spots` | `Unknown Unknowns` | **Blind Spots** | Already used in workflows in EN. AI associations: strong |
| 10.2 | `Гипотезы` | `Hypotheses` | — | **Hypotheses** | Standard scientific term |
| 10.2 tbl | `Гипотеза \| Статус` | `Hypothesis \| Status` | — | **Hypothesis \| Status** | Direct |
| 10.3 | `Фильтр` | `Filter` | — | **Filter** | Direct. But the content is more important — translate the instruction |
| 10.4 | `Риски незнания` | `Risks of Not Researching` | `Ignorance Risks` | **Risks of Not Researching** | Explicit, no ambiguity |
| 10.5 | `Предлагаемый фокус RESEARCH` | `Proposed RESEARCH Focus` | — | **Proposed RESEARCH Focus** | Direct, clear |
| footer | `При провале` | `On failure` | — | **On failure** | Short |

#### TS template

| § | RU Original | **Winner** | D28 Rationale |
|---|-------------|------------|---------------|
| 1 | `Цель` | **Objective** | Stronger action signal than "Goal"; agents associate "objective" with deliverable |
| 3 | `Затрагиваемые файлы` | **Affected Files** | Standard term in PR/diff tooling |
| 3 tbl | `Файл \| Действие \| Описание` | **File \| Action \| Description** | Direct |
| 3 note | `Бюджет` | **Budget** | Direct; already used in EN context |
| 6 | `Риски фазы` | **Phase Risks** | Mirror HL §9 |

#### RF template

| § | RU Original | **Winner** | D28 Rationale |
|---|-------------|------------|---------------|
| 1 | `Что сделано` | **What Was Done** | Direct, action-past |
| 1.1 | `Новые файлы` | **New Files** | Direct |
| 1.2 | `Изменённые файлы` | **Modified Files** | Standard term (git) |
| 1 tbl | `Файл \| Описание`, `Файл \| Изменения` | **File \| Description**, **File \| Changes** | Direct |
| 2 | `Ключевые решения` | **Key Decisions** | Direct |
| 4 | `Верификация` | **Verification** | Direct |

#### ONB template

| § | RU Original | **Winner** | D28 Rationale |
|---|-------------|------------|---------------|
| 1 | `Understanding (как понял задачу)` | **Understanding** | Drop RU annotation |
| 2 | `Entry Points (откуда начинать)` | **Entry Points** | Drop RU annotation |

#### REVIEW template
Only `Дата`, `Автор` — covered in common fields.

### E2: `content_language` config pattern

Proposed addition to `PROJECT_CONFIG.yaml`:
```yaml
tfw:
  content_language: en    # Language for filled artifacts (en, ru, etc.)
```

Agent instruction (goes in conventions.md or AGENTS.md):
> "When filling templates, use the language specified in `tfw.content_language`. Template structure (headings, labels, field names) stays English always."

During `tfw-init`, agent asks: "What language should I use when filling artifacts? Default: English."

### E3: Impact on existing KNOWLEDGE.md entry (D25 in KNOWLEDGE.md §3)

KNOWLEDGE.md line 133 has:
> `§3.1 Визуализация результата (ascii mandatory), §10 Обоснование RESEARCH (hypotheses + blind spots)`

This is a historical record (Source column = TFW-22). Will need updating to match new EN headings.

### Checkpoint: Extract
| Found | Remaining |
|-------|-----------|
| Full translation table for 5 templates (32 term pairs) | — |
| content_language config pattern designed | — |
| KNOWLEDGE.md §3 needs historical record update | HL scope update |

**Sufficiency Verdict:**
- [x] External source used? (D28/P5 applied from verified project knowledge)
- [x] Briefing gap closed? (Research Plan #2: scan existing patterns, naming analysis)

**Agent assessment:** Extract is sufficient. Complete consistency table built. No gaps remaining.
**Depth check:** Project knowledge (D28, P5) + convention analysis + grep verification of downstream refs.
**Recommendation:** close stage, move to Challenge
Stage complete: YES
→ User decision: ___

## Stage: Challenge — "What do we NOT expect?"

### C1: Is `content_language` overengineering?

**Argument FOR:** User explicitly asked for it. Minimal implementation — one YAML key + one sentence in conventions.md. Enables non-English users without template duplication.

**Argument AGAINST:** If we add it now, we need to:
1. Add key to `PROJECT_CONFIG.yaml`
2. Document it in conventions.md
3. Add to `tfw-init` workflow (ask user)
4. Add to Config Sync Registry (via `/tfw-config`)
5. Update AGENTS.md or conventions.md with the instruction

This is **not** template standardization — it's a new feature. Mixing it into TFW-23 violates scope.

**Verdict:** Split `content_language` into a separate concern. TFW-23 = English templates only. The `content_language` feature can be part of TFW-20 (user preferences) or a new task. Today we document the principle: "templates = English, content = user's language" in the HL, but don't implement the config mechanism.

### C2: Do the chosen heading names actually trigger better behavior?

Testing a few critical names against alternatives:

| Term | Why it works (D28) | Risk |
|------|-------------------|------|
| **Vision** (§1) | AI models are trained on business docs — "Vision" triggers strategic framing, not just description | Low — universally understood |
| **Objective** (TS §1) vs "Goal" | "Objective" is more specific: "measurable deliverable". "Goal" is vaguer. In military/project contexts, "objective" = concrete target | Low |
| **RESEARCH Case** (§10) vs "RESEARCH Justification" | "Case" = shorter, implies "make the argument". "Justification" = reactive, implies "defend a decision already made". "Case" is proactive | Low |
| **Result Visualization** (§3.1) vs "Outcome Preview" | "Visualization" literally tells the agent to produce a visual (diagram, ascii). "Preview" is passive — could mean just text description | Winner: Result Visualization confirmed |

No alternative names are clearly better. The consistency table from Extract holds.

### C3: What about the RU instructions inside HL template (not headings)?

Lines 23-28 in HL.md are RU instructional text:
```
> Покажи результат как будто он уже достигнут. Используй:
> - **ASCII-схемы** (обязательно): ...
> - **Mermaid** (для complex flows): ...
> - **Before→After таблицы** для сравнения state
> Цель: исполнитель и юзер должны увидеть «финальную картинку» до начала работы.
```

And line 88:
```
> **Фильтр:** Каждая гипотеза: «Если окажется ложной — изменится ли наш подход?» Если нет — удалить.
```

These are **instructional annotations**, not headings. They also need translation. I missed these in the initial HL scope. Must be included.

### C4: Should KNOWLEDGE.md historical entries be updated?

Line 133 in KNOWLEDGE.md has `§3.1 Визуализация результата`. This is a **Legacy & Deprecation** record. The convention (P2: "Index, don't duplicate") says link to sources. The §3.1 heading name is descriptive context in the legacy table. It should be updated to reflect the new name to avoid confusion when agents read it.

### Checkpoint: Challenge
| Found | Remaining |
|-------|-----------|
| `content_language` = separate concern, not TFW-23 scope | Document principle in HL only |
| Naming table confirmed — no alternatives are clearly better | — |
| RU instructional text inside templates needs translation too | Add to HL scope |
| KNOWLEDGE.md historical entry needs update | Add to HL scope |

**Sufficiency Verdict:**
- [x] External source used? (D28 application cross-checked against external naming research)
- [x] Briefing gap closed? (Research Plan #3: is pure English correct? Answered: yes, with content_language as future)

**Agent assessment:** Challenge revealed 2 scope additions (instructional text, KNOWLEDGE.md) and 1 scope reduction (content_language → future task). Net change is minor.
**Depth check:** Internal analysis of assumptions, external D28 cross-reference.
**Recommendation:** close stage, proceed to Final Checkpoint
Stage complete: YES
→ User decision: ___

---

## Final Checkpoint

| Stage | Status | Key Findings |
|-------|--------|-------------|
| Gather | ✅ Done | EN structure + localized content = industry standard. A+D hybrid architecture. H3 confirmed (no RU heading refs in workflows) |
| Extract | ✅ Done | 32-term consistency table built (D28 applied). `content_language` config pattern designed. KNOWLEDGE.md legacy entry found |
| Challenge | ✅ Done | `content_language` = separate task (scope reduction). RU instructional text also needs translation (scope addition). KNOWLEDGE.md entry update needed |

### Sufficiency Check
**Question:** Sufficient for HL finalization? Can we confidently define phases, approach, and dependencies?
**Self-check:**
- Are there unclosed Open Questions in RES? → No, all 3 resolved (see Decisions)
- Did all stages produce substantive findings or were any perfunctory? → All substantive: Gather (architecture), Extract (naming table), Challenge (scope corrections)
- Did every stage include external research, or was it internal-only? → Gather: 3 web searches. Extract: project knowledge (D28/P5). Challenge: cross-reference with external naming research
- Is the solution proportionate to the problem scale? → Yes — simple text replacement guided by a consistency table
- Are phases, boundaries and dependencies clear enough to finalize HL? → Yes
**Agent assessment:** Sufficient. Clear scope, no unknowns remaining.
→ User decision: ___

**Verdict:** Sufficient for HL finalization

## Closure

### HL Update Recommendations
| # | What to update | Source |
|---|---------------|--------|
| 1 | Add RU instructional text (HL.md lines 23-28, 88) to scope — not just headings | C3 |
| 2 | Add KNOWLEDGE.md §3 legacy entry update to scope | C4 |
| 3 | Remove `content_language` config from TFW-23 scope → note as future (TFW-20 or new task) | C1 |
| 4 | Add consistency table reference to HL (or keep in RES as source of truth) | E1 |
| 5 | Document principle: "templates = English, content = user's language" in HL §7 | C1 |

### Next Step
Update HL → confirm → TS
→ User decision: ___

### Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | convention | Templates = English always; filled content = user's language. Template structure is code, code is English | User direction + external i18n best practice | High |
| 2 | convention | `content_language` as a config key is the right pattern for i18n in TFW — avoids template duplication, avoids locale directories, minimal infra. Implementation deferred | RES G2 analysis | Medium |
| 3 | process | D28 (Naming > Explanation) applies not just to workflow terms but also to template section headings — heading names should trigger correct agent behavior, not just describe content | RES E1 + C2 analysis | High |

## Conclusion
Research confirmed that English-only templates with user-language content is the industry standard for AI prompt frameworks. A 32-term consistency table was built applying D28 (Naming > Explanation), choosing terms that trigger correct agent behavior. Challenge stage refined scope: `content_language` config is a separate feature (deferred), while RU instructional annotations and KNOWLEDGE.md legacy entries were added to scope. All hypotheses confirmed. No unknowns remain.

---

*RES — TFW-23: Templates English Standardization | 2026-04-04*
