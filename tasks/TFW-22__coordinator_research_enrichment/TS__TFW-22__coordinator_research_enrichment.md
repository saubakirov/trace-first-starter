# TS — TFW-22: Coordinator & Research Enrichment

> **Дата**: 2026-04-04
> **Автор**: Coordinator (AI)
> **Статус**: 🟡 TS_DRAFT — Ожидает апрува
> **Parent HL**: [HL-TFW-22](HL-TFW-22__coordinator_research_enrichment.md)
> **RES**: [RES-TFW-22](RES__TFW-22__coordinator_research_enrichment.md)

---

## 1. Цель

Реализовать 3 фазы coordinator/research enrichment: обновить HL/RES templates (§3.1 визуализация, §10 гипотезы, Sufficiency Verdict), рефакторить plan.md в algorithm-first формат (ref-inside-step, DNA/Library split), заменить монолитный research.md на модульную архитектуру research/{base,focused,deep}.md с OODA Stage Loop, Trust Protocol и YAML-конфигурируемыми режимами.

---

## Phase A: Templates

### 2A. Scope

**In Scope:**
- HL template: §3.1 Визуализация результата, §10 Обоснование RESEARCH
- RES template: Hypotheses table, Sufficiency Verdict checkpoint format

**Out of Scope:**
- plan.md refactor (Phase B)
- research/ directory (Phase C)

### 3A. Затрагиваемые файлы

| Файл | Действие | Описание |
|------|----------|----------|
| `.tfw/templates/HL.md` | MODIFY | +§3.1 визуализация (ascii mandatory, mermaid для complex), +§10 (гипотезы, слепые зоны, риски, фокус) |
| `.tfw/templates/RES.md` | MODIFY | +Hypotheses table в Briefing, +Sufficiency Verdict формат в Checkpoint |

**Бюджет:** 0 новых файлов, 2 модификации. ≤50 LOC.

### 4A. Детальные шаги

#### Step A1: Обновить HL template

Добавить после §3 (To-Be):

```markdown
### 3.1 Визуализация результата

> Покажи результат как будто он уже достигнут. Используй:
> - **ASCII-схемы** (обязательно): architecture, flow, file structure
> - **Mermaid** (для complex flows): sequence diagrams, state machines
> - **Before→After таблицы** для сравнения state
>
> Цель: исполнитель и юзер должны увидеть «финальную картинку» до начала работы.
```

Добавить после §9 (Риски):

```markdown
## 10. Обоснование RESEARCH

### Слепые зоны
- {Что мы НЕ знаем, но что может повлиять на подход}

### Гипотезы

| # | Гипотеза | Статус |
|---|----------|--------|
| H1 | {Утверждение для проверки} | open |

> **Фильтр:** Каждая гипотеза: «Если окажется ложной — изменится ли наш подход?» Если нет — удалить.

### Риски незнания
{Что случится ЕСЛИ мы пропустим RESEARCH}

### Предлагаемый фокус RESEARCH
1. **Gather**: {конкретный вопрос}
2. **Extract**: {конкретный вопрос}
3. **Challenge**: {конкретный вопрос}
```

#### Step A2: Обновить RES template

В секцию Briefing добавить после Research Plan:

```markdown
### Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | {text} | open | 🟡 testing | |
```

В секцию каждого Stage Checkpoint добавить Sufficiency Verdict:

```markdown
### Checkpoint: {Stage}
Sufficiency Verdict:
- [ ] External source used? (not project-files only)
- [ ] Briefing gap closed? (at least 1 from Research Plan)
- [ ] {mode-specific criterion if applicable}
Stage complete: YES / NO
If NO → what specific action next
```

### 5A. Acceptance Criteria

- [ ] HL template содержит §3.1 с инструкцией по визуализации (ascii mandatory)
- [ ] HL template содержит §10 с таблицей гипотез, слепыми зонами, рисками незнания, фокусом
- [ ] RES template содержит Hypotheses table в Briefing
- [ ] RES template содержит Sufficiency Verdict формат в checkpoint

---

## Phase B: plan.md → Algorithm Refactor

### 2B. Scope

**In Scope:**
- Refactor plan.md: inline bloat → ref-inside-step (D1)
- DNA layer inline (Role Lock + Mindset, D10)
- Add Step 5 (Hypothesis Iteration), strengthen RESEARCH Gate
- Word target: ≤950 words

**Out of Scope:**
- research/ directory (Phase C)
- conventions.md changes (ref targets already exist)

### 3B. Затрагиваемые файлы

| Файл | Действие | Описание |
|------|----------|----------|
| `.tfw/workflows/plan.md` | MODIFY | Full algorithm refactor |
| `.agent/workflows/tfw-plan.md` | MODIFY | Adapter sync |
| `.claude/commands/tfw-plan.md` | MODIFY | Adapter sync |

**Бюджет:** 0 новых, 3 модификации. ~300 LOC (plan.md = main, adapters = copy).

### 4B. Детальные шаги

#### Step B1: Restructure plan.md header

Заменить текущий header на DNA layer:

```markdown
---
description: TFW Plan — research, write HL, review, scope decision, write TS
---

> 🔒 **ROLE LOCK: COORDINATOR**
> You write HL and TS. You do NOT write ONB, RF, RES, REVIEW, or code.
> Violation = immediate stop + report.

**Mindset:** You are a strategic architect. Understand the problem deeply before proposing solutions. Show the finish line visually (§3.1). Identify what you DON'T know (§10). Challenge assumptions — be a thinking partner, not a yes-machine.
```

#### Step B2: Replace inline bloat with ref-inside-step

Remove these inline blocks and replace with algorithmic steps:

**Prerequisites (50 words) →**
```markdown
**Step 1: Load context**
Read `conventions.md` §10 (Context Loading). Verify: AGENTS.md loaded, KNOWLEDGE.md read, task board checked. If any missing → load now.
```

**Scope Budget table (160 words) →**
```markdown
**Step 7b: Budget check**
Read `PROJECT_CONFIG.yaml` → `tfw.scope_budgets`. Read `conventions.md` §6 for rules.
Calculate: count files in TS, count new files, estimate LOC.
IF exceeds any limit → split into phases OR document override with justification.
```

**Status Transitions (50 words) →**
```markdown
→ Status transitions: see `conventions.md` §5
```

**Anti-patterns (91 words) →**
```markdown
**Footer**
Before submitting: read `conventions.md` §14 (Anti-patterns). Self-check: did I violate any? Especially: TS without approved HL? Modified files outside scope? Skipped review?
→ Full anti-pattern list: `conventions.md` §14
→ Role Lock details: `conventions.md` §15
```

#### Step B3: Add new steps

Add Step 4c (within HL writing):
```markdown
**Step 4c: Fill §3.1 and §10**
- §3.1: create ASCII visualization of To-Be (mandatory). Add mermaid if flow is complex.
- §10: write 2-4 hypotheses. For each: apply filter «If false, would approach change?» Remove if no.
  Add blind spots, risks of not researching, proposed RESEARCH focus.
```

Add Step 5 (new, after HL draft):
```markdown
**Step 5: Hypothesis Iteration**
Present §10 hypotheses to user one by one:
  FOR EACH hypothesis:
    USER: "I know the answer" → mark confirmed/refuted in table, record answer
    USER: "Not sure" → mark needs-research
    USER: "This is obvious" → remove from table
  AFTER iteration:
    IF all confirmed/refuted → RESEARCH optional (offer skip)
    IF any needs-research → recommend RESEARCH
    IF coordinator sees remaining blind spots → still recommend RESEARCH despite user closure
🛑 WAIT for user response
```

Strengthen Step 6 (RESEARCH Gate):
```markdown
**Step 6: RESEARCH decision**
Review HL §10. Present: «N hypotheses need research. Blind spots: [list]. Recommend: RESEARCH / skip.»
IF user approves research → instruct: "Start `/tfw-research`". STOP.
IF user skips → confirm, proceed to Step 7.
```

#### Step B4: Word count verification

After all changes, count words. Target: ≤950. If over → compress further.

#### Step B5: Adapter sync

Copy final plan.md content to:
- `.agent/workflows/tfw-plan.md`
- `.claude/commands/tfw-plan.md`

### 5B. Acceptance Criteria

- [ ] plan.md contains Role Lock + Mindset as inline header (DNA layer)
- [ ] No inline Anti-patterns block (replaced with ref-inside-step in footer)
- [ ] No inline Status Transitions (replaced with ref)
- [ ] No inline Prerequisites list (replaced with Step 1)
- [ ] No inline Scope Budget table (replaced with Step 7b)
- [ ] Step 4c requires §3.1 and §10
- [ ] Step 5: Hypothesis Iteration exists with FOR EACH loop
- [ ] Step 6: RESEARCH Gate references §10
- [ ] Word count ≤ 950
- [ ] Both adapters synced

---

## Phase C: research/ → Modular Architecture

### 2C. Scope

**In Scope:**
- Replace `research.md` with `research/{base,focused,deep}.md`
- OODA Stage Loop in base.md
- Sufficiency Verdict with 2-level criteria
- Trust Protocol (4-tier)
- YAML config additions (default_mode, modes)
- Remove old research.md

**Out of Scope:**
- Glossary updates (separate commit or tech debt)
- conventions.md §15 Role Lock update for research/ (path change only)

### 3C. Затрагиваемые файлы

| Файл | Действие | Описание |
|------|----------|----------|
| `.tfw/workflows/research/base.md` | CREATE | Core algorithm (~500-600 words) |
| `.tfw/workflows/research/focused.md` | CREATE | Focused mode settings (~150-200 words) |
| `.tfw/workflows/research/deep.md` | CREATE | Deep mode settings (~200-250 words) |
| `.tfw/workflows/research.md` | DELETE | Replaced by directory |
| `.tfw/PROJECT_CONFIG.yaml` | MODIFY | +default_mode, +modes.{focused,deep} |
| `.agent/workflows/tfw-research.md` | MODIFY | Adapter sync (copy of base.md) |
| `.claude/commands/tfw-research.md` | MODIFY | Adapter sync (copy of base.md) |
| `.tfw/workflows/config.md` | MODIFY | Update sync registry (research.md → research/base.md) |

**Бюджет:** 3 новых файлов, 4 модификации, 1 удаление = 8 total. ~600 LOC.

### 4C. Детальные шаги

#### Step C1: Create base.md

Core algorithm file (~500-600 words). Structure:

```markdown
---
description: TFW Research — structured investigation between HL and TS
---

> 🔒 **ROLE LOCK: COORDINATOR (Research Mode)**
> You write RES only. You do NOT write HL, TS, ONB, RF, REVIEW, or code.

**Mindset:** Critical thinking partner. Find what's missing. Healthy critique. Show blind spots. You are an opponent who demands proof — not a yes-machine.

## Step 1: Load Context
Read `conventions.md` §10. Verify loaded.

## Step 2: Select Mode
Read `PROJECT_CONFIG.yaml` → `tfw.research.default_mode`.
Present to user: "Recommend [{mode}]. Reason: {specific}. Switch? [focused/deep]"
🛑 WAIT
Load `research/{mode}.md`.

## Step 3: Create RES File
→ ref: `templates/RES.md`
Create in task directory. Fill header.

## Step 4: Briefing Protocol
1. Research Plan (3-5 bullets: what to investigate per stage)
2. Hypotheses table from HL §10 (if pipeline mode)
3. Scope intent (in/out)
4. Guiding questions (≤3)
🛑 WAIT for user response

## Step 5: Run Stages (Gather → Extract → Challenge)

FOR EACH stage:

### OODA Stage Loop
Repeat up to `loops_per_stage` times (from YAML):

**OBSERVE:** Gather data — web search, file read, codebase analysis, user input.
**ORIENT:** Interpret against existing understanding. "Does this confirm or challenge what I thought?"
**DECIDE:** Sufficiency Verdict — run checkpoint criteria:
  Generic (always):
  - [ ] External source used? (not project-files only)
  - [ ] Briefing gap closed? (at least 1)
  Mode-specific (from mode file):
  - [ ] {criteria from mode file}
  ALL met → exit loop → STAGE CHECKPOINT
  NOT met + loops remaining → back to OBSERVE
  NOT met + no loops → report unmet criteria, exit loop
**ACT:** Update RES with findings. Formulate next observe action.

### Stage Checkpoint
Present findings + open questions (≤3) to user.
🛑 WAIT for user response

## Step 6: Final Checkpoint
Sufficiency Check:
- Are unclosed questions remaining?
- Did all stages use external sources?
- Is solution proportionate to problem?
Present verdict to user.
🛑 WAIT

## Step 7: Closure Protocol
1. HL Update Recommendations (table: what to update, source decision)
2. Fact Candidates (table: category, candidate, source, confidence)
→ User decides next step (HL update → TS, or TS directly)
🛑 WAIT

## Trust Protocol
| Input Type | Trust Level | Agent Behavior |
|-----------|-------------|----------------|
| Business/domain | Trust as-is | Clarifying questions only |
| Technical approach | Verify externally | Cross-check with docs/web |
| Performance numbers | Verify empirically | Test or find evidence |
| "I tried this before" | Trust outcome | Verify reason (why fail?) |

## Rules
- MUST: external research in every stage (Hard Rule)
- MUST: present checkpoint findings before advancing
- MUST: update RES after every stage
- NEVER: skip straight to conclusions without data
- NEVER: treat user technical claims as proven (D3)
→ Full anti-pattern list: `conventions.md` §14
```

#### Step C2: Create focused.md

Mode file (~150-200 words):

```markdown
# Research Mode: Focused

> **Mindset Override:** "Scan → Assess → Report"
> Quick, scoped investigation. One question, one answer, move on.

## When to Use
- Topic is understood, specific question needs answering
- Time-constrained, need fast turnaround
- Low uncertainty — looking for confirmation, not discovery

## Stage Behavior
- **OODA loops per stage:** 1 (single pass)
- **Verify user tech claims:** yes (1x cross-check)
- **Require counter-evidence:** no

## Checkpoint Criteria
Generic only (from base.md):
- [ ] External source used?
- [ ] Briefing gap closed?

## Exit Criteria
- Min 1 decision per stage
- Max 2 user-facing turns per stage
```

#### Step C3: Create deep.md

Mode file (~200-250 words):

```markdown
# Research Mode: Deep

> **Mindset Override:** "Hypothesize → Test → Revise → Test"
> Rigorous, hypothesis-driven investigation. Challenge everything.

## When to Use
- Many unknowns, high architectural impact
- HL §10 contains unresolved hypotheses
- Decision is irreversible or costly to change

## Stage Behavior
- **OODA loops per stage:** up to N (from YAML `loops_per_stage`, default: 3)
- **Verify user tech claims:** yes (2x cross-check)
- **Require counter-evidence:** yes

## Checkpoint Criteria
Generic (from base.md):
- [ ] External source used?
- [ ] Briefing gap closed?

Mode-specific:
- [ ] Hypothesis tested? (at least 1 from HL §10)
- [ ] Counter-evidence sought? (actively looked for reasons approach might fail)

## Metacognitive Check (at each checkpoint)
Ask yourself: "Did I discover something NEW, or just confirm what I already knew?"
IF only confirmed → flag this in checkpoint. Consider: what sources haven't I checked?

## Exit Criteria
- Min 2 decisions per stage
- Min 1 hypothesis tested per stage
- Metacognitive check completed at each checkpoint
```

#### Step C4: Update PROJECT_CONFIG.yaml

Add mode configuration:

```yaml
  research:
    max_web_queries_per_stage: 5
    max_files_per_stage: 15
    max_questions_per_turn: 3
    max_passes: 3
    default_mode: focused
    modes:
      focused:
        loops_per_stage: 1
        verify_user_tech_claims: true
      deep:
        loops_per_stage: 3
        verify_user_tech_claims: true
        require_counter_evidence: true
```

#### Step C5: Delete old research.md

Remove `.tfw/workflows/research.md` — replaced by `research/` directory.

#### Step C6: Update config.md sync registry

Update the Config Sync Registry:
- Change `research.md` → `research/base.md` in workflow path
- Add new sync entries for `tfw.research.default_mode` and `tfw.research.modes.*`

#### Step C7: Update PROJECT_CONFIG.yaml workflows section

```yaml
  workflows:
    research: .tfw/workflows/research/base.md    # Changed from research.md
```

#### Step C8: Adapter sync

Copy `base.md` content to:
- `.agent/workflows/tfw-research.md`
- `.claude/commands/tfw-research.md`

Mode files do NOT need adapter copies — loaded via ref from base.md.

#### Step C9: Word count verification

Verify:
- base.md ≤ 600 words
- focused.md ≤ 200 words
- deep.md ≤ 250 words
- base + focused ≤ 800 words (< current 1165)
- base + deep ≤ 850 words (< current 1165)

### 5C. Acceptance Criteria

- [ ] `research/base.md` exists, ≤600 words, contains OODA Stage Loop
- [ ] `research/focused.md` exists, ≤200 words, contains focused mode settings
- [ ] `research/deep.md` exists, ≤250 words, contains deep mode + metacognitive check
- [ ] Old `research.md` deleted
- [ ] `PROJECT_CONFIG.yaml` has `default_mode` and `modes.{focused,deep}` with numeric/boolean settings
- [ ] Sufficiency Verdict format in base.md (2-level: generic + mode-specific)
- [ ] Checkpoint criteria = SOFT (report, not block). loops_per_stage = HARD LIMIT
- [ ] Trust Protocol table in base.md
- [ ] Config sync registry updated
- [ ] Both adapters synced with base.md content

---

## 6. Риски (all phases)

| Риск | Mitigation |
|------|------------|
| ref-inside-step: agent still skips ref | Step is self-contained (WHAT inline, WHERE as ref). Agent can execute without ref — ref gives precision, not direction |
| OODA loop stall | YAML hard limit (loops_per_stage). Criteria = SOFT. Force exit + report after max loops |
| Word count creep during implementation | Verify word count as explicit step in each phase. Budget clearly defined |
| research/ directory path breaks existing refs | Update CONFIG workflows section. Update config.md sync registry |
| Adapter desync after major refactor | Adapter sync = explicit final step in phases B and C |

---

*TS — TFW-22: Coordinator & Research Enrichment | 2026-04-04*
