# TS — TFW-18: Knowledge Consolidation

> **Дата**: 2026-04-03
> **Автор**: Coordinator (AI)
> **Статус**: 🟡 TS_DRAFT — Ожидает апрува
> **Parent HL**: [HL-TFW-18](HL-TFW-18__knowledge_consolidation.md)
> **RES**: [RES-TFW-18](RES__TFW-18__knowledge_consolidation.md)

---

## 1. Цель

Deliver the complete knowledge consolidation system: Fact Candidates collection in all artifacts (Phase A), `/tfw-knowledge` workflow with topic files infrastructure (Phase B), and Knowledge Gate enforcement in plan.md (Phase C). After this task, project facts will be systematically captured, consolidated, and protected from drift.

## 2. Scope

### In Scope
- §6 Fact Candidates in RF.md, §5 in REVIEW.md, §Closure in RES.md (all mandatory)
- Quality filter + anti-patterns in Fact Candidates template section
- Mindset reminders in handoff.md, research.md, review.md
- `.user_preferences.md` template + `.gitignore` in init.md
- New `.tfw/workflows/knowledge.md` (4-phase consolidation)
- `knowledge/` folder with topic file template
- §5 Project Facts compact index in KNOWLEDGE.md template
- `.tfw/knowledge_state.yaml`
- `tfw.knowledge` section in PROJECT_CONFIG.yaml
- tfw-docs checklist update (п.6)
- Phase 0 Knowledge Gate Check in plan.md
- conventions.md + glossary.md updates
- All adapters synced (Antigravity + Claude Code)

### Out of Scope
- `tfw-config` workflow (future task)
- `tfw-user-tune` workflow (future task)
- Main pipeline diagram changes (none)
- Backfilling existing RF/REVIEW files with Fact Candidates

## 3. Затрагиваемые файлы

### Phase A: Fact Candidates — templates + collection

| Файл | Действие | Описание |
|------|----------|----------|
| `.tfw/templates/RF.md` | MODIFY | Add §6 Fact Candidates section with quality filter |
| `.tfw/templates/REVIEW.md` | MODIFY | Add §5 Fact Candidates section with quality filter |
| `.tfw/templates/RES.md` | MODIFY | Add Fact Candidates to Closure section |
| `.tfw/workflows/handoff.md` | MODIFY | Add 1-line mindset reminder about Fact Candidates in RF writing step |
| `.tfw/workflows/research.md` | MODIFY | Add 1-line mindset reminder about Fact Candidates in Closure |
| `.tfw/workflows/review.md` | MODIFY | Add 1-line mindset reminder about Fact Candidates in REVIEW writing |
| `.tfw/templates/KNOWLEDGE.md` | MODIFY | Add §5 Project Facts compact index |

### Phase B: `/tfw-knowledge` workflow + knowledge infrastructure

| Файл | Действие | Описание |
|------|----------|----------|
| `.tfw/workflows/knowledge.md` | CREATE | 4-phase consolidation workflow (Orient → Gather → Consolidate → Prune) |
| `.tfw/templates/TOPIC_FILE.md` | CREATE | Template for topic files in knowledge/ folder |
| `.tfw/knowledge_state.yaml` | CREATE | Knowledge tracking state + stats |
| `.tfw/PROJECT_CONFIG.yaml` | MODIFY | Add `tfw.knowledge` section (limits, gate_mode, interval) |
| `.tfw/workflows/docs.md` | MODIFY | Add п.6 to checklist: Fact Candidates marker |
| `.tfw/conventions.md` | MODIFY | Add Fact Candidates definition, categories table, knowledge/ folder, knowledge.md workflow |
| `.tfw/glossary.md` | MODIFY | Add terms: Fact Candidate, Topic File, Knowledge Gate, Consolidation |

### Phase C: Knowledge Gate — plan.md integration

| Файл | Действие | Описание |
|------|----------|----------|
| `.tfw/workflows/plan.md` | MODIFY | Add Phase 0: Knowledge Gate Check |

### Adapters (Phase A+B+C sync)

| Файл | Действие | Описание |
|------|----------|----------|
| `.agent/workflows/tfw-handoff.md` | MODIFY | Sync mindset reminder from canonical |
| `.agent/workflows/tfw-docs.md` | MODIFY | Sync п.6 from canonical |
| `.agent/workflows/tfw-plan.md` | MODIFY | Sync Phase 0 from canonical |
| `.agent/workflows/tfw-research.md` | MODIFY | Sync mindset reminder from canonical |
| `.agent/workflows/tfw-review.md` | MODIFY | Sync mindset reminder from canonical |
| `.agent/workflows/tfw-knowledge.md` | CREATE | New adapter for knowledge.md workflow |

**Бюджет:** 5 новых файлов, 14 модификаций. Лимиты: ≤8 new (✅), ≤14 total (✅), ≤1200 LOC.

## 4. Детальные шаги

### Phase A: Fact Candidates

#### Step 1: RF.md — add §6 Fact Candidates

After existing §5 Observations, add:

```markdown
## 6. Fact Candidates

> Record what you learned about this project that would change how the NEXT agent
> approaches a similar task. If it wouldn't change their decision — don't record it.
>
> Anti-patterns: "project uses git", "code is in Python", "tests exist"
> These are NOT verified facts. They become facts after `/tfw-knowledge` consolidation.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | {category} | {what you learned} | {where from} | High/Medium/Low |
```

Categories reference: `environment`, `process`, `stakeholder`, `constraint`, `convention`, `domain`, `context`, `risk` (open list).

#### Step 2: REVIEW.md — add §5 Fact Candidates

After existing §4 Verdict, add same section (renumbered to §5).

#### Step 3: RES.md — add Fact Candidates to Closure

In the Closure section (before Conclusion), add:

```markdown
### Fact Candidates

> Research uncovered domain knowledge. Record project-relevant facts here —
> not findings about alternatives, but facts about THIS project, its environment,
> and its constraints.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
```

#### Step 4: Mindset reminders in workflows

**handoff.md** — in the RF writing step, add:
```
> 💡 As you work, capture what you learn about the project — environment, constraints,
> stakeholders, conventions — in §6 Fact Candidates. These save the next agent
> from re-learning the same lessons.
```

**research.md** — before Closure instructions, add:
```
> 💡 Your research uncovered domain knowledge. Capture project-relevant facts
> in the Fact Candidates section — not findings about alternatives, but facts
> about THIS project.
```

**review.md** — in the REVIEW writing step, add:
```
> 💡 If you discovered something about the project during review that isn't
> in KNOWLEDGE.md, record it in §5 Fact Candidates.
```

#### Step 5: KNOWLEDGE.md — add §5 Project Facts

After existing §4 Tech Stack, add:

```markdown
## 5. Project Facts

> Index of verified project knowledge. Details in `knowledge/` topic files.
> Updated by `/tfw-knowledge` consolidation.

| Category | Count | Topic File |
|----------|-------|------------|
```

#### Step 6: .user_preferences.md template + init.md update

Create template at project root suggestion in init.md. Template header:

```markdown
# User Preferences

> ⚠️ PERSONAL FILE — DO NOT COMMIT TO GIT
> This file stores individual user preferences for AI agents.
> It is listed in .gitignore by default.
> To disable: set `tfw.user_preferences: false` in `.tfw/PROJECT_CONFIG.yaml`

## Communication
- Language: {your language}
- Tone: {direct / friendly / formal}

## Work Style
- {preferences}
```

Add to init.md's `.gitignore` setup: `.user_preferences.md`.

### Phase B: `/tfw-knowledge` + infrastructure

#### Step 7: Create `.tfw/workflows/knowledge.md`

Role Lock: Coordinator. ~120 lines. Structure:

```markdown
# Knowledge Consolidation Workflow

> Role lock: **Coordinator only**.
> Trigger: manual (`/tfw-knowledge`) or gate in plan.md Phase 0.
> Duration: 5-20 minutes.

## Prerequisites
1. Read `.tfw/knowledge_state.yaml`
2. Read `KNOWLEDGE.md`
3. Read all topic files in `knowledge/`

## Phase 1: Orient
- Understand current knowledge state
- Note last_consolidation_seq and task range to scan

## Phase 2: Gather
- Scan all RF/REVIEW/RES files for tasks since last_consolidation_seq
- Collect Fact Candidates from each artifact
- If no candidates found in any artifact — note in stats and skip to Phase 4

## Phase 3: Consolidate
For each candidate:
  - Check if fact already exists in topic files → skip (deduplicate)
  - Check if fact contradicts existing → flag contradiction, ask user
  - If ≥2 independent sources → mark as ✅ verified, add to topic file
  - If 1 source → show to user, ask to confirm or skip
  - Mark processed artifacts: `> fact-candidates: processed YYYY-MM-DD`

## Phase 4: Prune
- Review existing facts for staleness (source > 20 tasks ago)
- Check limit compliance (max_facts_per_topic, max_topic_files)
- Update KNOWLEDGE.md §5 compact index (category counts + links)
- Update `.tfw/knowledge_state.yaml` (seq, date, stats)
- Present summary to user

## Behavior Rules
- DO NOT invent facts — only consolidate from artifacts
- DO NOT auto-resolve contradictions — ask user
- DO NOT exceed topic file limits without user approval
```

#### Step 8: Create topic file template

Create `.tfw/templates/TOPIC_FILE.md`:

```markdown
# Knowledge: {Category}

> Topic file for `{category}` facts. Updated by `/tfw-knowledge`.
> See KNOWLEDGE.md §5 for the index.

| # | Fact | Verified | Source(s) | Added |
|---|------|----------|-----------|-------|
```

#### Step 9: Create `.tfw/knowledge_state.yaml`

```yaml
# Knowledge consolidation state — updated by /tfw-knowledge
# Configuration (interval, gate_mode, limits) → see tfw.knowledge in PROJECT_CONFIG.yaml
knowledge:
  last_consolidation_seq: 0
  last_consolidation_date: null
  stats:
    total_facts: 0
    verified: 0
    unverified: 0
    rejected: 0
    candidates_processed: 0
    sources_scanned: 0
```

#### Step 10: PROJECT_CONFIG.yaml — add `tfw.knowledge` section

After `tfw.research:` section, add:

```yaml
  knowledge:
    interval: 5
    gate_mode: hard          # hard / soft / off
    max_index_lines: 200
    max_index_facts_lines: 30
    max_facts_per_topic: 50
    max_topic_files: 8
```

Add `knowledge: .tfw/workflows/knowledge.md` to `tfw.workflows` section.

#### Step 11: tfw-docs checklist update

Add item 6 to the docs.md checklist:

```
6. **Fact Candidates** — Are there Fact Candidates in RF/REVIEW/RES?
   If yes → they will be processed during next `/tfw-knowledge`.
   Note: do NOT consolidate facts here — that is `/tfw-knowledge`'s job.
```

#### Step 12: conventions.md + glossary.md

**conventions.md** additions:
- §3 artifact types: add "Fact Candidates (§ in RF, REVIEW, RES)" description
- §8 workflows: add `knowledge.md` row
- New subsection: Fact categories table (8 universal categories, open list)
- New subsection: `knowledge/` folder and `knowledge_state.yaml` registration

**glossary.md** additions:
- Fact Candidate — raw observation recorded during work, unverified
- Topic File — per-category knowledge file in `knowledge/` folder
- Knowledge Gate — periodic consolidation checkpoint (Phase 0 in plan.md)
- Consolidation — 4-phase process (Orient → Gather → Consolidate → Prune)

### Phase C: Knowledge Gate

#### Step 13: plan.md — Phase 0

Before Phase 1 (Registration), add:

```markdown
### Phase 0: Knowledge Gate Check

1. Read `.tfw/knowledge_state.yaml`
2. Read `tfw.knowledge.gate_mode` from PROJECT_CONFIG.yaml
3. Compute: `current_seq - last_consolidation_seq`
4. If `>= interval` AND gate_mode = `hard`:
   → **HARD STOP**: "Knowledge consolidation overdue ({N} tasks since last).
   Run `/tfw-knowledge` before proceeding."
   Skip allowed with justification. Record: `knowledge-gate: skipped (reason: ...)`
5. If `>= interval` AND gate_mode = `soft`:
   → Reminder: "Knowledge consolidation recommended ({N} tasks since last)."
6. If gate_mode = `off`: skip silently
```

### Adapter Sync

#### Step 14: Sync all adapters

For each canonical workflow modified (handoff, research, review, docs, plan):
- Copy relevant change to `.agent/workflows/tfw-{name}.md`
- Create new `.agent/workflows/tfw-knowledge.md` adapter

## 5. Acceptance Criteria

- [ ] RF.md template has §6 Fact Candidates with quality filter and anti-patterns
- [ ] REVIEW.md template has §5 Fact Candidates with quality filter
- [ ] RES.md template has Fact Candidates in Closure section
- [ ] handoff.md, research.md, review.md each have 1 mindset reminder about Fact Candidates
- [ ] KNOWLEDGE.md template has §5 Project Facts compact index
- [ ] `.tfw/workflows/knowledge.md` exists with 4-phase process, role lock, behavior rules
- [ ] `.tfw/templates/TOPIC_FILE.md` exists
- [ ] `.tfw/knowledge_state.yaml` exists with initial state
- [ ] PROJECT_CONFIG.yaml has `tfw.knowledge` section with 6 configurable parameters
- [ ] tfw-docs checklist has item 6 (Fact Candidates marker)
- [ ] plan.md has Phase 0 Knowledge Gate Check
- [ ] conventions.md has Fact Candidates definition + categories + new files
- [ ] glossary.md has 4 new terms
- [ ] All 6 adapters synced (5 modified + 1 new)
- [ ] No changes to main pipeline diagrams
- [ ] Grep verification: "Fact Candidates" appears in RF.md, REVIEW.md, RES.md templates

## 6. Риски фазы

| Риск | Mitigation |
|------|------------|
| Many files touched (19 total) | Changes per file are small (2-20 lines each). LOC budget ~400, well within 1200 |
| knowledge.md workflow too long | Cap at ~120 lines. Comparable to research.md (~145 lines) |
| Adapter sync misses a file | Step 14 is explicit checklist. Final grep verification |
| Fact Candidates section ignored by future agents | Quality filter + anti-patterns + mindset reminders = 3 reinforcement mechanisms |

---

*TS — TFW-18: Knowledge Consolidation | 2026-04-03*
