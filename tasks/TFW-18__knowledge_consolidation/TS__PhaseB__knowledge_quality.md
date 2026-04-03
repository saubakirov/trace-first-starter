# TS — TFW-18 / Phase B: Knowledge Quality

> **Дата**: 2026-04-03
> **Автор**: Coordinator (AI)
> **Статус**: 🟡 TS_DRAFT — Ожидает апрува
> **Parent HL**: [HL-TFW-18 Phase B](HL__PhaseB__knowledge_quality.md)

---

## 1. Цель

Reframe Fact Candidates guidance from technical to strategic across all templates and workflows. Ensure .tfw/README.md reflects the knowledge consolidation system added in Phase A.

## 2. Scope

### In Scope
- Reframe FC prompt in 3 templates (RF, REVIEW, RES) + 2 workflows (research, handoff)
- Expand §10.1 category examples in conventions.md
- Sharpen knowledge.md gather guidance
- Add knowledge system to .tfw/README.md

### Out of Scope
- Changing the consolidation process itself (Phase A — already works)
- Changing category names (already right in glossary)
- Adding new categories

## 3. Затрагиваемые файлы

| Файл | Действие | Описание |
|------|----------|----------|
| `.tfw/templates/RF.md` | MODIFY | §6 FC: reframe prompt + examples |
| `.tfw/templates/REVIEW.md` | MODIFY | §5 FC: same reframe |
| `.tfw/templates/RES.md` | MODIFY | §FC: same reframe |
| `.tfw/workflows/research.md` | MODIFY | §Closure L110: one-line reframe |
| `.tfw/workflows/handoff.md` | MODIFY | L81-87: reorder + reframe |
| `.tfw/conventions.md` | MODIFY | §10.1: expand category examples |
| `.tfw/workflows/knowledge.md` | MODIFY | Phase 2: sharpen gather guidance |
| `.tfw/README.md` | MODIFY | §v3 + workflows table: add knowledge + config |

**Бюджет:** 0 новых файлов, 8 модификаций. Defaults: max 14 files, max 8 new, max 1200 LOC.

## 4. Детальные шаги

### Step 1: Reframe FC in RF.md §6

Replace L51-56:

```markdown
> **Before writing Fact Candidates, review the conversation history.** The human's
> messages are the primary source of strategic knowledge — domain insights, stakeholder
> priorities, business context, and constraints that shape decisions.
>
> Good: "18% clients = 80% revenue (Pareto)", "stakeholder: find problem clients first"
> NOT fact candidates: "project uses git", "code is in Python", implementation details (→ §5 Observations → tfw-docs)
> These are NOT verified facts. They become facts after `/tfw-knowledge` consolidation.
```

### Step 2: Reframe FC in REVIEW.md §5

Same text as Step 1. Replace L53-58.

### Step 3: Reframe FC in RES.md §Fact Candidates

Replace L116-121:

```markdown
> **Before writing Fact Candidates, review the conversation history.** The human's
> messages are the primary source of strategic knowledge — domain insights, stakeholder
> priorities, business context, and constraints that shape decisions.
>
> Record strategic facts about THIS project — not findings about alternatives,
> not implementation details (those belong in tfw-docs).
```

### Step 4: Reframe in research.md §Closure L110

Replace the FC bullet:

```markdown
3. **Fact Candidates** — **review the full conversation history first.** Extract strategic knowledge — domain patterns, stakeholder priorities, business context. Technical observations belong in tfw-docs, not here
```

### Step 5: Reframe in handoff.md L81-87

Replace:

```markdown
> 💡 As you work, capture strategic knowledge about the project — stakeholder priorities,
> domain patterns, business context, external constraints — in §6 Fact Candidates.
> These save the next agent from missing critical context.
>
> **Before writing Fact Candidates, review the conversation history.** The human's
> messages are the primary source — their decisions, priorities, concerns, and domain
> insights. Extract what informs decisions, not implementation details.
```

### Step 6: Expand conventions.md §10.1 examples

Replace the category table:

```markdown
| Category | Scope | Examples |
|----------|-------|----------|
| `environment` | Where the work lives | servers, tools, platforms, classrooms, labs, hosting |
| `process` | How work gets done | schedules, approvals, reporting cadence, grading cycles |
| `stakeholder` | Who needs what | priorities, pain points, expectations, quotes, key decisions |
| `constraint` | What limits exist | contractual obligations, regulatory deadlines, resource caps, technical limits |
| `convention` | Agreed standards | naming, style, format, language, tone |
| `domain` | Subject matter knowledge | revenue patterns, client segments, market metrics, business rules, curriculum |
| `context` | Background that shapes decisions | market conditions, competitive landscape, regulatory changes, prior decisions |
| `risk` | Known dangers | client concentration, market dependency, knowledge silos, fragile dependencies |
```

### Step 7: Sharpen knowledge.md Phase 2 gather

Replace L32-34:

```markdown
> **⚠️ Conversation history is the primary source of strategic knowledge.**
> The human's messages contain domain insights, stakeholder priorities, business context,
> and concerns that artifacts miss. Look for decisions, emotions, and data shared during work.
> Technical implementation details belong in tfw-docs — here we capture what informs decisions.
```

### Step 8: Update .tfw/README.md

**8a.** Add to §v3 additions (after L283 `TECH_DEBT.md pipeline` bullet):

```markdown
- **Knowledge consolidation** — Fact Candidates in every artifact capture strategic knowledge (domain, stakeholder, context). `/tfw-knowledge` workflow consolidates them into verified project facts in `knowledge/` topic files, with configurable Knowledge Gate enforcing regular consolidation.
```

**8b.** Add `knowledge` and `config` to workflows table (L161-170):

```markdown
| **knowledge** | Coordinator | Consolidate fact candidates → verified project knowledge in `knowledge/` |
| **config** | Coordinator | Interactive config change → propagate to all inline values |
```

### Step 9: Sync adapters

Copy modified workflows to `.agent/workflows/`:
- `tfw-research.md` ← research.md
- `tfw-handoff.md` ← handoff.md
- `tfw-knowledge.md` ← knowledge.md

## 5. Acceptance Criteria

- [ ] RF.md FC prompt says «strategic knowledge» not «next agent's behavior»
- [ ] REVIEW.md FC prompt matches RF.md
- [ ] RES.md FC prompt same reframe + keeps «THIS project» filter
- [ ] research.md §Closure FC bullet reframed
- [ ] handoff.md FC guidance leads with «stakeholder priorities, domain patterns»
- [ ] conventions.md §10.1 `domain` examples include: revenue patterns, client segments, market metrics
- [ ] conventions.md §10.1 `stakeholder` examples include: priorities, pain points, quotes
- [ ] knowledge.md Phase 2 says «strategic knowledge» and mentions «decisions, emotions, data»
- [ ] .tfw/README.md §v3 lists Knowledge consolidation
- [ ] .tfw/README.md workflows table includes knowledge and config
- [ ] All 3 adapters synced (diff = 0)
- [ ] No file exceeds P10 word limit after changes
- [ ] Anti-pattern examples include «implementation details» as NOT-FC

## 6. Verification

```bash
# Strategic reframe present
grep -l "strategic knowledge" .tfw/templates/RF.md .tfw/templates/REVIEW.md .tfw/templates/RES.md
grep "strategic knowledge" .tfw/workflows/knowledge.md
grep "strategic knowledge" .tfw/workflows/research.md

# Old framing removed
grep -c "next agent's behavior" .tfw/templates/RF.md  # should be 0
grep -c "next agent's behavior" .tfw/templates/REVIEW.md  # should be 0

# Category examples updated
grep "revenue patterns" .tfw/conventions.md
grep "priorities, pain points" .tfw/conventions.md

# README updated
grep "Knowledge consolidation" .tfw/README.md
grep "knowledge" .tfw/README.md | grep -i "workflow"

# Adapters synced
diff .tfw/workflows/research.md .agent/workflows/tfw-research.md
diff .tfw/workflows/handoff.md .agent/workflows/tfw-handoff.md
diff .tfw/workflows/knowledge.md .agent/workflows/tfw-knowledge.md

# Word count check
wc -w .tfw/workflows/research.md  # should be ≤1200
wc -w .tfw/workflows/knowledge.md  # should be ≤1200
```

## 7. Риски фазы

| Риск | Mitigation |
|------|------------|
| Word count exceeds P10 after edits | Pre-calculated +120 words total, all files stay within limits |
| «Strategic» guidance too vague for engineering projects | Examples include both business AND engineering in §10.1 |
| Executor replaces entire FC section instead of targeted edit | TS specifies exact replacement text |

---

*TS — TFW-18 / Phase B: Knowledge Quality | 2026-04-03*
