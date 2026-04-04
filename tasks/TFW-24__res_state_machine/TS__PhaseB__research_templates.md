# TS — TFW-24 / Phase B: Research Stage Templates

> **Date**: 2026-04-04
> **Author**: Coordinator
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-24](HL-TFW-24__res_state_machine.md)

---

## 1. Objective

Create canonical templates for the 4 research stage files (`briefing`, `gather`, `extract`, `challenge`) in `.tfw/templates/research/`. These templates give the Researcher role a concrete starting point for each stage, enforce Goal anchoring from HL §1, and guarantee consistent Checkpoint format for the filesystem state machine.

## 2. Scope

### In Scope
- 4 template files in `.tfw/templates/research/`
- `base.md` Step 3 → reference templates instead of conventions
- `conventions.md` §4 → replace inline format with templates reference
- Adapter sync (`.agent/workflows/tfw-research.md`)

### Out of Scope
- Changes to RES synthesis template (done in Phase A)
- OODA loop or mode file changes
- Briefing content changes (Step 4 already defines what goes in briefing)

## 3. Affected Files

| File | Action | Description |
|------|--------|------------|
| `.tfw/templates/research/briefing.md` | CREATE | Briefing template: Research Plan, Hypotheses, Scope, Guiding Questions, User Direction |
| `.tfw/templates/research/gather.md` | CREATE | Gather stage: "What do we NOT know?" — external + internal findings |
| `.tfw/templates/research/extract.md` | CREATE | Extract stage: "What do we NOT see?" — analysis, patterns, gaps |
| `.tfw/templates/research/challenge.md` | CREATE | Challenge stage: "What do we NOT expect?" — edge cases, stress tests |
| `.tfw/workflows/research/base.md` | MODIFY | Step 3: reference templates. Step 4: template ref for briefing. Step 5: template ref for stages |
| `.tfw/conventions.md` | MODIFY | §4: replace inline stage format with templates reference |
| `.agent/workflows/tfw-research.md` | MODIFY | Sync from base.md |

**Budget:** 4 new files, 3 modifications = 7 total. Limits: max 14 files, max 8 new. ✅ Within budget.

## 4. Detailed Steps

### Step 1: Create `.tfw/templates/research/briefing.md`

```markdown
# Briefing
> Parent: [HL-{PREFIX}-{N}](../../HL-{PREFIX}-{N}__{title}.md)
> Goal: {from HL §1 Vision — one sentence}

## Research Plan
{3-5 bullets per stage: what to investigate}

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | {text} | open |

## Scope Intent
- **In scope:** {what research covers}
- **Out of scope:** {what research does NOT cover}

## Guiding Questions
1. {≤3 questions for the user}

## User Direction
{Record user answers and steering decisions here during briefing discussion}

---
Stage complete: YES / NO
```

### Step 2: Create `.tfw/templates/research/gather.md`

```markdown
# Gather — "What do we NOT know?"
> Parent: [HL-{PREFIX}-{N}](../../HL-{PREFIX}-{N}__{title}.md)
> Goal: {from HL §1 Vision — one sentence}

## Findings

### {G1: source/topic title}
{content}

### {G2: source/topic title}
{content}

## Checkpoint

| Found | Remaining |
|-------|-----------|
| {key finding} | {gap, if any} |

**Sufficiency:**
- [ ] External source used?
- [ ] Briefing gap closed?

Stage complete: YES / NO
→ User decision: ___
```

### Step 3: Create `.tfw/templates/research/extract.md`

```markdown
# Extract — "What do we NOT see?"
> Parent: [HL-{PREFIX}-{N}](../../HL-{PREFIX}-{N}__{title}.md)
> Goal: {from HL §1 Vision — one sentence}

## Findings

### {E1: analysis title}
{content — patterns, comparisons, internal file analysis}

### {E2: analysis title}
{content}

## Checkpoint

| Found | Remaining |
|-------|-----------|
| {key finding} | {gap, if any} |

**Sufficiency:**
- [ ] External source used?
- [ ] Briefing gap closed?

Stage complete: YES / NO
→ User decision: ___
```

### Step 4: Create `.tfw/templates/research/challenge.md`

```markdown
# Challenge — "What do we NOT expect?"
> Parent: [HL-{PREFIX}-{N}](../../HL-{PREFIX}-{N}__{title}.md)
> Goal: {from HL §1 Vision — one sentence}

## Findings

### {C1: edge case / stress test title}
{content — what could go wrong, alternatives, counter-evidence}

### {C2: edge case / stress test title}
{content}

## Checkpoint

| Found | Remaining |
|-------|-----------|
| {key finding} | {gap, if any} |

**Sufficiency:**
- [ ] External source used?
- [ ] Briefing gap closed?

Stage complete: YES / NO
→ User decision: ___
```

### Step 5: Update `base.md` Steps 3, 4, and 5

**Step 3** — change:
```
Create `research/` subfolder in task directory. → See `conventions.md §4 (Research subfolder)` for file list and format.
```
To:
```
Create `research/` subfolder in task directory. Copy templates from `templates/research/`. Fill Goal from HL §1 Vision.
```

**Step 4** — change:
```
Write Briefing to `research/briefing.md`:
```
To:
```
Write Briefing to `research/briefing.md` (use `templates/research/briefing.md`):
```

**Step 5** — change:
```
Cover all three. Order flexible. Each stage writes to its file in `research/`. Each uses the OODA loop below.
```
To:
```
Cover all three. Order flexible. Each stage uses its template from `templates/research/` and writes to `research/`. Each uses the OODA loop below.
```

### Step 6: Update `conventions.md` §4

Replace inline stage file format block with:
```
Stage file format: see `.tfw/templates/research/` (briefing.md, gather.md, extract.md, challenge.md).
```

### Step 7: Adapter sync

```bash
cp .tfw/workflows/research/base.md .agent/workflows/tfw-research.md
```

## 5. Acceptance Criteria

- [ ] 4 template files exist in `.tfw/templates/research/`
- [ ] Each stage template has: Parent HL link, Goal from §1 Vision, Findings section, Checkpoint with `Stage complete: YES / NO`
- [ ] Each stage template has its guiding question as subtitle (D28): Gather = "What do we NOT know?", Extract = "What do we NOT see?", Challenge = "What do we NOT expect?"
- [ ] Briefing template includes: Research Plan, Hypotheses table, Scope Intent, Guiding Questions, User Direction
- [ ] Gather/Extract/Challenge templates include Sufficiency checklist (external source + briefing gap)
- [ ] `base.md` Step 3 references `templates/research/`
- [ ] `base.md` Step 4 references `templates/research/briefing.md`
- [ ] `base.md` Step 5 references `templates/research/` for stage files
- [ ] `conventions.md` §4 references templates instead of inline format
- [ ] Adapter synced

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| Templates too rigid → agent can't adapt to specific research | Templates are starting points, not contracts. Findings section is free-form |
| base.md word count exceeds 600 after Step 3 change | Change is same word count (~12 words → ~12 words). No budget impact |

---

*TS — TFW-24 / Phase B: Research Stage Templates | 2026-04-04*
