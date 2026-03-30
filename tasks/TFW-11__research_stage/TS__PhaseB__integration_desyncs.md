# TS — TFW-11 / Phase B: Integration — Plan Gate + Pipeline Desyncs

> **Дата**: 2026-03-30
> **Автор**: Coordinator (AI)
> **Статус**: 🟡 TS — Ожидает апрува
> **Parent HL**: [HL-TFW-11](HL-TFW-11__research_stage.md)
> **Research**: [RES__TFW-11](RES__TFW-11__research_stage.md)

---

## 1. Цель

Интегрировать RESEARCH в plan.md (гейт после HL) и устранить все pipeline desyncs из Phase A REVIEW (Tech Debt #1-8) + review findings.

## 2. Scope

### In Scope
- RESEARCH gate в plan.md (после HL approval, перед TS)
- Pipeline diagram update: plan.md, `.tfw/README.md`, init.md, root README.md
- Text fixes: conventions.md §2 + §8, glossary.md (workflow count, Coordinator role, Task Naming, read-only AG)

### Out of Scope
- Adapter files (CLAUDE.md.template, CLAUDE.md) — Phase C
- Slash command file `.claude/commands/tfw-research.md` — Phase C
- Proof-of-concept — Phase C

## 3. Затрагиваемые файлы

| Файл | Действие | Описание |
|------|----------|----------|
| `.tfw/workflows/plan.md` | MODIFY | RESEARCH gate after Phase 3, pipeline diagram update |
| `.tfw/README.md` | MODIFY | Pipeline diagram (§Task Lifecycle), artifact types table (add RES) |
| `.tfw/init.md` | MODIFY | Pipeline status line in Step 4 code block |
| `README.md` (root) | MODIFY | Key Concepts pipeline string |
| `.tfw/conventions.md` | MODIFY | §2: add RES.md + research.md to Required Artifacts. §8: "three" → "four" |
| `.tfw/glossary.md` | MODIFY | Workflow def: "Three" → "Four". Coordinator role: add RES. Task Naming: add RES__ example. Add "Read-only AG" term |

**Бюджет:** 0 новых файлов, 6 модификаций. ≤7 файлов ✅, ≤4 новых ✅, ≤6 modified ✅

## 4. Детальные шаги

### Step 1: plan.md — RESEARCH gate

Insert new Phase 3.5 between current Phase 3 (Review & Refine) and Phase 4 (Decide Scope):

```markdown
## Phase 3.5: RESEARCH Gate

After HL is approved, the coordinator:

1. **Assess** — give a recommendation: is RESEARCH needed? (with rationale)
   - Complex/ambiguous tasks → recommend RESEARCH
   - Simple/clear tasks → recommend skip
2. **Ask** — present recommendation to user, ask for confirmation
3. **Never skip silently** — even if recommending skip, wait for user response

If RESEARCH is needed:
- Run the research workflow (`.tfw/workflows/research.md`) inline
- RES file is created in the task folder
- After RESEARCH completes → proceed to Phase 4

If RESEARCH is skipped:
- User confirms skip → proceed directly to Phase 4
```

Also update the pipeline diagram in plan.md Status Transitions section to include 🔬 RES.

### Step 2: `.tfw/README.md` — pipeline + artifact table

1. Update the pipeline diagram in §Task Lifecycle:
   ```
   ⬜ TODO → 🔵 HL → 🔬 RES → 🟡 TS → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → ✅ DONE
   ```
   Add note: "RES is optional — user can skip from HL directly to TS"

2. Update artifact types table — add RES row:
   ```
   | **RES** | Research Report | Structured investigation: decisions, questions, stage logs |
   ```

3. Update "seven statuses" text to "eight statuses (plus optional RES)"

### Step 3: `.tfw/init.md` — pipeline status line

Update the status line in Step 4 code block:
```
> Statuses: ⬜ TODO → 🔵 HL → 🔬 RES → 🟡 TS → 🟠 ONB → 🟢 RF → 🔍 REV → ✅ DONE | ❌ BLOCKED
```

### Step 4: `README.md` (root) — Key Concepts

Update the pipeline string in Key Concepts section:
```
- **Task lifecycle**: `⬜ TODO → 🔵 HL → 🔬 RES → 🟡 TS → 🟠 ONB → 🟢 RF → 🔍 REV → ✅ DONE` (RES optional)
```

### Step 5: `.tfw/conventions.md` — text fixes

1. §2 Required Artifacts — add two lines:
   ```
   - `.tfw/templates/RES.md` — canonical Research Report template.
   - `.tfw/workflows/research.md` — canonical research workflow.
   ```

2. §8 Workflows — change "three canonical workflows" to "four canonical workflows"

### Step 6: `.tfw/glossary.md` — text fixes

1. Workflow definition (line ~73): "Three canonical workflows" → "Four canonical workflows: plan (HL→RES→TS), research (structured investigation), handoff (ONB→execute→RF→REVIEW), resume (status matrix→next phase)"

2. Coordinator role (line ~89-94): add "- Writes RES (research mode)" or "- Conducts RESEARCH and writes RES files"

3. Task Naming section (line ~41): add `RES__{PREFIX}-{N}__*.md` to the file examples

4. Add new term — **Read-only AG**: "A mode within RESEARCH where the agent autonomously reads project files and web sources but writes only to the RES artifact. No code changes, no other file modifications. Formally CL with expanded read permissions."

## 5. Acceptance Criteria

- [ ] plan.md contains RESEARCH gate between Phase 3 and Phase 4 with recommend/ask/never-skip logic
- [ ] Pipeline diagrams updated in: plan.md, `.tfw/README.md`, init.md, root README.md (all show 🔬 RES)
- [ ] `.tfw/README.md` artifact types table includes RES
- [ ] conventions.md §2 lists RES.md template and research.md workflow
- [ ] conventions.md §8 says "four" not "three"
- [ ] glossary.md: Workflow def updated, Coordinator mentions RES, Task Naming includes RES, Read-only AG defined
- [ ] Grep for "three canonical" across `.tfw/` returns 0 matches

## 6. Риски фазы

| Риск | Mitigation |
|------|------------|
| plan.md restructuring breaks existing flow | Preserve all existing phases, only insert 3.5 between 3 and 4 |
| Missing pipeline instances | Final grep: `TODO.*HL.*TS` across all .md to catch stragglers |

---

*TS — TFW-11 / Phase B: Integration — Plan Gate + Pipeline Desyncs | 2026-03-30*
