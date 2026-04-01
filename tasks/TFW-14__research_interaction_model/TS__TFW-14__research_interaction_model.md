# TS — TFW-14: Research Interaction Model

> **Дата**: 2026-04-01
> **Автор**: Coordinator (AI)
> **Статус**: 🟡 TS — Ожидает апрува
> **Parent HL**: [HL-TFW-14](HL-TFW-14__research_interaction_model.md)

---

## 1. Цель

Добавить в RESEARCH workflow прозрачное управление взаимодействием агент↔пользователь: явный вход (Briefing), управляемые переходы (Stage Handoff), явный выход (Closure с рекомендациями к HL), и фикс skip-bias в plan.md. Структура: 2 новых элемента + 2 расширения + 1 фикс. Turn-based ритм вместо stage-based.

## 2. Scope

### In Scope
- research.md: Briefing Protocol, Closure Protocol, расширение checkpoint, усиление Final Checkpoint
- RES.md template: секции Briefing и Closure (якоря)
- plan.md: Phase 3.5 gate (HL update after research) + skip-bias fix (pros/cons)
- Оба адаптера: синхронизация с research.md

### Out of Scope
- Стейджи (Gather/Extract/Challenge) — не меняем
- Лимиты, Entry Modes, Role Lock, статусы pipeline
- PROJECT_CONFIG.yaml
- Standalone mode research

## 3. Затрагиваемые файлы

| Файл | Действие | Описание |
|------|----------|----------|
| `.tfw/workflows/research.md` | MODIFY | Briefing, Closure, Handoff, Sufficiency, Hard Rules, Anti-patterns |
| `.tfw/templates/RES.md` | MODIFY | Секции Briefing и Closure |
| `.tfw/workflows/plan.md` | MODIFY | Phase 3.5: HL update gate + skip-bias fix |
| `.claude/commands/tfw-research.md` | MODIFY | Синхронизация (briefing, closure, turn-based) |
| `.agent/workflows/tfw-research.md` | MODIFY | Синхронизация (briefing, closure, turn-based) |

**Бюджет:** 0 новых файлов, 5 модификаций.

## 4. Детальные шаги

### Step 1: research.md — Briefing Protocol

Добавить новую секцию **перед** секцией «Process» (после «Research Mindset»):

```markdown
## Briefing Protocol

Before starting any stages, the agent MUST present a briefing and wait for user response.

### Briefing contents
1. **Research Plan** — 3-5 bullets: what you plan to investigate and why
2. **Scope intent** — what is in scope, what is not
3. **Guiding questions** (1-3) — help the user set priorities

🛑 **WAIT** — do NOT start stages until user responds. Briefing may last multiple turns.

### Turn-based rhythm
- ≤3 questions per turn (one round of Q&A)
- Briefing AND each stage may last multiple turns
- Stage transitions happen when BOTH sides are ready, not when a checklist says so
```

### Step 2: research.md — Расширение Checkpoint (Stage Handoff)

В секции «Checkpoint» (после текущего формата findings + questions) добавить:

```markdown
**Stage Handoff:** After findings and questions, announce the plan for the NEXT stage:
- "For [next stage] I plan to investigate: [plan]. Any thoughts or additions?"
- 🛑 WAIT for user response before proceeding
```

### Step 3: research.md — Closure Protocol

Добавить новую секцию **после** Final Checkpoint:

```markdown
## Closure Protocol

After Sufficiency Check = "sufficient", the agent runs the Closure Protocol:

1. **Summary** — key decisions, closed questions from RES
2. **HL Update Recommendations** — what should change in HL (phases, approach, dependencies, risks). Research agent writes recommendations; coordinator applies them
3. **Next step** — "HL updated. Proceed to TS?"
4. 🛑 **WAIT** — agent does NOT write TS without user confirmation of updated HL

> HL is updated ALWAYS after research. Even if research confirmed the original plan, HL records "confirmed by research" as a decision.

> **Recommended:** Run research in a separate session (`/tfw-research`). Research agent writes RES → coordinator reads RES → updates HL → user confirms → TS.
```

### Step 4: research.md — Sufficiency Check (усиление Final Checkpoint)

В секции «Final Checkpoint» заменить текущий вопрос:

**Было:** `"Sufficient for TS?"`
**Стало:** `"Sufficient for HL finalization? Can we confidently define phases, approach, and dependencies?"`

Добавить чеклист самопроверки:
```markdown
- Are there unclosed Open Questions in RES?
- Did all stages produce substantive findings or were any perfunctory?
- Is the solution proportionate to the problem scale?
- Are phases, boundaries and dependencies clear enough to finalize HL?
```

### Step 5: research.md — Hard Rules + Anti-patterns

В «Agent Behavior Protocol» добавить Hard Rules:

```markdown
- Agent MUST run Briefing before any stages — skipping briefing is a protocol violation
- Agent MUST run Closure after final checkpoint — silently proceeding to TS is a protocol violation
- Agent MUST present Sufficiency Check with concrete assessment, not just "sufficient"
```

В «Anti-patterns» добавить:

```markdown
- ❌ Agent skips Briefing and jumps directly into Gather
- ❌ Agent rushes from Briefing to Gather without follow-up (rush-bias)
- ❌ Agent proceeds to TS without Closure or HL update
- ❌ Agent recommends skipping RESEARCH without structured justification (skip-bias)
```

### Step 6: RES.md template — секции Briefing и Closure

Добавить секцию **Briefing** после Research Context:

```markdown
## Briefing

### Research Plan
1. **Gather** — {what to investigate}
2. **Extract** — {what to analyze}
3. **Challenge** — {what to test/challenge}

### Scope Intent
- **В скоупе:** {scope}
- **Не в скоупе:** {out of scope}

### Guiding Questions
1. {question}
2. {question}
3. {question}

→ User direction: ___
```

Добавить секцию **Closure** перед Conclusion:

```markdown
## Closure

### HL Update Recommendations
| # | What to update | Source |
|---|---------------|--------|

### Next Step
→ User decision: ___
```

### Step 7: plan.md — Phase 3.5 HL update gate + skip-bias fix

Переписать Phase 3.5:

```markdown
## Phase 3.5: RESEARCH Gate

After HL is approved, the coordinator:

1. **Present pros/cons** — list 2-3 reasons FOR and AGAINST running RESEARCH
   - Default recommendation: **run RESEARCH**
   - Skipping requires concrete justification (not just "task is simple")
2. **User decides** — coordinator does NOT decide to skip unilaterally
3. **Never skip silently** — even if recommending skip, wait for user response

If RESEARCH is done:
- Run the research workflow (`.tfw/workflows/research.md`), recommended in a separate session
- RES file is created in the task folder
- **After RESEARCH: coordinator reads RES Closure → updates HL → presents diff to user → user confirms → proceed to Phase 4**

If RESEARCH is skipped:
- User confirms skip → proceed directly to Phase 4
```

Добавить anti-pattern:

```markdown
- Do not write TS without updating HL after RESEARCH — process gate violation
- Do not recommend skipping RESEARCH without presenting pros/cons to user
```

### Step 8: Адаптеры — синхронизация

Обновить оба файла (`.claude/commands/tfw-research.md` и `.agent/workflows/tfw-research.md`):

Заменить текущий Step 4:
```markdown
4. Run research with Briefing → Stages → Closure:
   - BRIEFING first: present research plan, ask guiding questions. 🛑 WAIT.
   - ≤3 questions per turn (not per stage). Stages may last multiple turns.
   - 🛑 Checkpoint + Stage Handoff after each stage — WAIT for user response.
   - SUFFICIENCY CHECK: "Sufficient for HL finalization?" (not "for TS")
   - CLOSURE: summary + HL update recommendations. 🛑 WAIT.
```

## 5. Acceptance Criteria

- [ ] 1. research.md: Briefing Protocol section with 🛑 WAIT, turn-based rhythm documented
- [ ] 2. research.md: Checkpoint includes Stage Handoff (+2 lines)
- [ ] 3. research.md: Closure Protocol section with HL recommendations, separate agent recommendation
- [ ] 4. research.md: Final Checkpoint asks "sufficient for HL finalization?" with self-check list
- [ ] 5. research.md: Hard Rules include briefing/closure/sufficiency mandates
- [ ] 6. research.md: Anti-patterns include skip-bias, rush-bias, silent closure, skipping HL update
- [ ] 7. RES.md: Briefing section (plan, scope intent, questions) as anchor
- [ ] 8. RES.md: Closure section (HL recommendations table, next step)
- [ ] 9. plan.md: Phase 3.5 with pros/cons format, default=recommend, HL update gate
- [ ] 10. plan.md: Anti-patterns for skip-without-justification and TS-without-HL-update
- [ ] 11. Both adapters: synced with new research.md structure
- [ ] 12. Executor Observations section: any gaps, inconsistencies, or edge cases found during execution

## 6. Риски фазы

| Риск | Mitigation |
|------|------------|
| Briefing text too verbose → agent produces walls of text | Keep Briefing instructions to 10 lines max in research.md |
| Turn-based rhythm ambiguous → agent still rushes | Hard Rule + Anti-pattern + concrete example in workflow |
| Adapter sync incomplete | DoD item 11 explicitly checks both adapters |

---

*TS — TFW-14: Research Interaction Model | 2026-04-01*
