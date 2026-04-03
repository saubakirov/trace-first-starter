# TS — TFW-17: Research Depth & Coordinator Quality

> **Дата**: 2026-04-03
> **Автор**: Coordinator (AI)
> **Статус**: 🟡 TS_DRAFT — Ожидает апрува
> **Parent HL**: [HL-TFW-17](HL-TFW-17__research_depth_and_coordinator_quality.md)

---

## 1. Цель

Устранить три системных проблемы в поведении AI-агентов: skip-bias при рекомендации RESEARCH, отсутствие внешнего исследования (только файлы проекта), и rush-bias при проведении стейджей. Решение — комбинация coordinator mindset (plan.md) + research depth rules (research.md) + полная синхронизация 4 адаптеров.

## 2. Scope

### In Scope
- Coordinator Mindset секция в plan.md
- Усиление Phase 1 и RESEARCH Gate в plan.md
- Hard Rule #8 (external tools) в research.md
- Depth self-check в checkpoint template
- Stage-level mindset reminders
- Расширение Gather stage description
- Полная синхронизация 4 адаптеров + desync fixes

### Out of Scope
- Стейджи (Gather/Extract/Challenge) — не переписываем, только дополняем
- Лимиты, Entry Modes, standalone mode
- RES.md template (не меняется)
- Новые статусы или workflow

## 3. Затрагиваемые файлы

| Файл | Действие | Описание |
|------|----------|----------|
| `.tfw/workflows/plan.md` | MODIFY | +Coordinator Mindset, усиление Phase 1, RESEARCH Gate |
| `.tfw/workflows/research.md` | MODIFY | +Hard Rule #8, depth self-check, stage reminders, Gather expansion |
| `.agent/workflows/tfw-plan.md` | MODIFY | Полная синхронизация с canonical plan.md |
| `.agent/workflows/tfw-research.md` | MODIFY | Полная синхронизация с canonical research.md |
| `.claude/commands/tfw-plan.md` | MODIFY | Полная синхронизация с canonical plan.md |
| `.claude/commands/tfw-research.md` | MODIFY | Полная синхронизация с canonical research.md |

**Бюджет:** 0 новых файлов, 6 модификаций. Лимиты — см. `tfw.scope_budgets` в `.tfw/PROJECT_CONFIG.yaml`.

## 4. Детальные шаги

### Step 1: Coordinator Mindset в plan.md

Добавить новую секцию **после Role Lock block, перед Prerequisites**. ~6 строк.

```markdown
## Coordinator Mindset

Your primary goal is **quality of planning**, not speed of pipeline progression. You are the person who sees the full picture — the one who asks uncomfortable questions, catches implicit assumptions, and protects the process from rushing.

Every step of this workflow exists to ensure the executor receives a clear, well-researched, and complete specification. If you skip steps or rush through them, the executor pays the price with ambiguity, rework, and missed edge cases.

When recommending RESEARCH: your default is to recommend it. Think about what RESEARCH could reveal that you cannot see right now — blind spots, external context, alternative approaches. Present this to the user concretely: "RESEARCH could reveal X, Y, Z."
```

### Step 2: Усиление Phase 1 в plan.md

Расширить Phase 1 описание. Текущее:
```
1. **Identify context** — read relevant code, existing HL files, knowledge items
2. **Understand the problem** — what is broken, what is missing, what needs to change
```

Заменить на:
```
1. **Identify context** — read relevant code, existing HL files, knowledge items
2. **Understand the problem deeply** — what is broken, what is missing, what needs to change. Do NOT rush to solutions. Sit with the problem. What does the user actually need vs what they asked for? Are there related issues they haven't mentioned?
```

### Step 3: Усиление RESEARCH Gate в plan.md

Текущий Phase 4 (RESEARCH Gate) содержит правильную структуру, но coordinators rushают его. Добавить после "Default recommendation: **run RESEARCH**":

```markdown
   - When recommending FOR, be specific: "RESEARCH could reveal: [concrete things relevant to this task]"
   - Do NOT frame RESEARCH as overhead. Frame it as risk reduction: "Without RESEARCH, we are assuming X, Y, Z — are we confident enough?"
```

### Step 4: Hard Rule #8 в research.md

В секции "Hard Rules (violation = broken research)", после rule #7, добавить:

```markdown
8. **Every stage MUST include at least one external action** (web search, URL read, documentation lookup). Internal-only analysis = incomplete research. If the topic has no external dimension, state why explicitly.
```

### Step 5: Depth self-check в checkpoint template (research.md)

В checkpoint format (after `**Recommendation:** close stage / dig deeper`), добавить:

```markdown
**Depth check:** Did I use external sources (web search, docs, URLs), or only project files?
```

Также добавить в Sufficiency Check self-check list:

```markdown
- Did every stage include external research, or was it internal-only?
```

### Step 6: Stage-level mindset reminders (research.md)

Добавить одну строку-reminder в начало каждого Stage description:

**Gather:**
```markdown
> Remember: your job is to find what we DON'T know — not confirm what we already know. Search externally. What does the rest of the world know about this problem?
```

**Extract:**
```markdown
> Remember: look for what the user hasn't told you. Patterns, inconsistencies, implicit assumptions. Read the code, not just the docs.
```

**Challenge:**
```markdown
> Remember: this is where you add the most value. Don't just list risks — propose alternatives. "What if we did X instead?" Test the chosen approach against reality.
```

### Step 7: Расширить Gather stage description (research.md)

Текущее:
```
- Analyze HL and identify information gaps
- Autonomous search: documentation, changelogs, issues, blog posts
```

Заменить на:
```
- Analyze HL and identify information gaps
- **Search externally**: how is this problem solved elsewhere? What tools, libraries, or patterns exist? What are common pitfalls? Use web search, read documentation URLs, check changelogs and issues.
- Questions to user: ...
```

### Step 8: Синхронизация адаптеров

After all changes to canonical files are complete:

1. **Copy** `.tfw/workflows/plan.md` → `.agent/workflows/tfw-plan.md` (overwrite)
2. **Copy** `.tfw/workflows/plan.md` → `.claude/commands/tfw-plan.md` (overwrite)
3. **Copy** `.tfw/workflows/research.md` → `.agent/workflows/tfw-research.md` (overwrite)
4. **Copy** `.tfw/workflows/research.md` → `.claude/commands/tfw-research.md` (overwrite)

This automatically fixes all adapter desyncs (old statuses, Phase 3.5 numbering, old pipeline).

## 5. Acceptance Criteria

- [ ] AC-1: plan.md contains Coordinator Mindset section after Role Lock
- [ ] AC-2: plan.md Phase 1 says "understand deeply", not just "identify"
- [ ] AC-3: plan.md RESEARCH Gate includes "be specific about what RESEARCH could reveal"
- [ ] AC-4: research.md has Hard Rule #8 requiring external actions per stage
- [ ] AC-5: research.md checkpoint template includes Depth check line
- [ ] AC-6: research.md Sufficiency Check includes external research bullet
- [ ] AC-7: Each stage (Gather/Extract/Challenge) has 1-line mindset reminder
- [ ] AC-8: Gather stage description mentions external search explicitly
- [ ] AC-9: All 4 adapter files are byte-identical copies of their canonical counterparts
- [ ] AC-10: No desync: all files use `📝 HL_DRAFT`/`🟡 TS_DRAFT` statuses, `Phase 4` numbering

## 6. Риски фазы

| Риск | Mitigation |
|------|------------|
| research.md grows past 330 lines (currently 299) | Budget is ~15 net new lines — additions are terse (1-line reminders, 1 hard rule, 1 checkpoint line) |
| Agent treats new rules as additional checklist items rather than mindset shift | Coordinator Mindset explicitly says "quality > speed"; reminders at stage level reinforce |
| Adapter copy misses YAML frontmatter | Step 8 uses full file copy — frontmatter included |

---

*TS — TFW-17: Research Depth & Coordinator Quality | 2026-04-03*
