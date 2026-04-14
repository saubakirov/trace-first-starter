# TS — TFW-38 / Phase B: Knowledge Citation Table

> **Date**: 2026-04-14
> **Author**: Coordinator
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> **Supersedes**: Old Phase B (Diagram Indexing → moved to TFW-39)

---

## 1. Objective

Make Project Values (PV) citations traceable and verifiable. Currently: agent says "per D28 naming convention" — but no link, no proof of reading, could be hallucinated.

After: Coordinator does full PV scan (see glossary.md → PV Index) and produces a Knowledge Citations table in HL §7.2 with explicit links. Executor reads those citations and reports in ONB §7. Reviewer verifies links resolve to real items. Cascade model: coord scans → executor references → reviewer verifies.

This is the structural enforcement of P6 (Knowledge Gate) and S9 (cross-task knowledge as hard gate).

## 2. Scope

### In Scope
- Knowledge Citations table format (shared across templates)
- HL template §7.2: Coordinator fills during planning (full PV scan)
- ONB template §7: Executor references HL §7.2 citations, confirms read + adds new items
- review/verify.md template: Reviewer verifies citation link resolution
- plan.md Step 3: instruct coordinator to scan PV Index → fill HL §7.2
- handoff.md Phase 1: instruct executor to read HL §7.2 → fill ONB §7
- glossary.md: already done (PV term + PV Index table)

### Out of Scope
- Diagram indexing (→ TFW-39)
- RES/RF template changes (researcher/executor have Fact Candidates; citations = input, not output)
- Automated link validation (future — could be gen_docs.py extension)
- KNOWLEDGE.md rename to DOCS (→ TECH_DEBT.md)

## 3. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `.tfw/templates/HL.md` | MODIFY | Add §7.2 Knowledge Citations table |
| `.tfw/templates/ONB.md` | MODIFY | Add §7 Knowledge Citations table |
| `.tfw/templates/review/verify.md` | MODIFY | Add Knowledge Citations Verified section |
| `.tfw/workflows/plan.md` | MODIFY | Step 3: scan PV Index → fill HL §7.2 |
| `.tfw/workflows/handoff.md` | MODIFY | Phase 1: read HL §7.2 → fill ONB §7 |

**Budget:** 0 new files, 5 modifications = 5 total. ✅

## 4. Detailed Steps

### Step 1: Define citation table format

Shared format for HL and ONB:

```markdown
### Knowledge Citations

> Scan PV Index (glossary.md → Project Values). List items relevant to this task.
> Link MUST resolve to an actual file and item — reviewer verifies.
> If no applicable items after scanning: "No applicable knowledge items."

| # | Source | Item | How it applies |
|---|--------|------|----------------|
| 1 | [KNOWLEDGE.md D28](../../KNOWLEDGE.md) | Naming > Explanation | Stage names use active verbs |
| 2 | [knowledge/philosophy.md F4](../../knowledge/philosophy.md) | Structural enforcement | File existence as gate |
```

### Step 2: Add §7.2 to `templates/HL.md`

Insert after §7.1 Quality Contract (line 101), before §8 Dependencies:

```markdown
### 7.2 Knowledge Citations

> Coordinator: scan PV Index (glossary.md → Project Values).
> Full scan of priorities 1-4 (README Values, philosophy.md, KNOWLEDGE.md §1, conventions.md).
> Skim priorities 5-7 for relevant items.
> Reviewer will verify these links resolve to real items.

| # | Source | Item | How it applies |
|---|--------|------|----------------|

> For new projects with empty KNOWLEDGE.md: "No applicable knowledge items — project in bootstrap phase."
```

### Step 3: Add §7 to `templates/ONB.md`

Insert after §6 (Inconsistencies with Code), before the cross-references footer:

```markdown
## 7. Knowledge Citations

> Executor: read coordinator's citations in HL §7.2. For each item:
> - Confirm you read it (link + item name)
> - State how you applied it OR why it doesn't apply to your work
> - Add any NEW items you found relevant that coordinator missed

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | D28 Naming | ✅ | Applied: template names follow verb pattern | |
| 2 | F4 Structural | ✅ | Applied: review/ subfolder as state gate | |
| 3 | (NEW) D31 FS-SM | ✅ | Applied: parallels research/ subfolder | Not in HL §7.2 |
```

### Step 4: Update `templates/review/verify.md`

Add "Knowledge Citations Verified" section after Discrepancies, before Checkpoint:

```markdown
## Knowledge Citations Verified

> Verify that HL §7.2 and ONB §7 citation links resolve to real items.
> If ANY link doesn't resolve → flag as hallucination in Discrepancies.

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | HL §7.2 #1 | KNOWLEDGE.md D28 | ✅ / ❌ | ✅ / ❌ |
| 2 | ONB §7 #3 | KNOWLEDGE.md D31 | ✅ / ❌ | ✅ / ❌ |
```

Update Checkpoint self-check — replace current KNOWLEDGE.md bullet:

```markdown
- [ ] KNOWLEDGE.md checked — contradictions with changes documented?
- [ ] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist)?
  - Total citations: {N}, verified: {M}, hallucinations: {H}
```

### Step 5: Update `plan.md` Step 3

Amend existing knowledge citation instruction:

```markdown
4. **Scan Project Values (PV)** — see glossary.md PV Index.
   Full scan: README Values, knowledge/philosophy.md, KNOWLEDGE.md §1, conventions.md §3/§11/§14.
   Skim: knowledge/convention.md, knowledge/process.md, other topic files.
   Fill HL §7.2 Knowledge Citations table — each item linked.
   If no applicable items: "No applicable knowledge items."
   For new projects: "No applicable knowledge items — project in bootstrap phase."
```

### Step 6: Update `handoff.md` Phase 1

Amend existing KNOWLEDGE.md instruction:

```markdown
- Read HL §7.2 Knowledge Citations — verify each item, fill ONB §7.
  For each citation: confirm read, state how applied or why N/A.
  Add any NEW PV items you find relevant that coordinator missed.
- Inconsistencies between HL/TS/KNOWLEDGE.md and actual code
```

## 5. Acceptance Criteria

- [ ] HL template has §7.2 Knowledge Citations (after §7.1 Quality Contract)
- [ ] ONB template has §7 Knowledge Citations (after §6 Inconsistencies)
- [ ] review/verify.md has Knowledge Citations Verified section (links resolve check)
- [ ] verify.md self-check counts total/verified/hallucination citations
- [ ] plan.md Step 3 references PV Index from glossary.md
- [ ] handoff.md Phase 1 instructs executor to read HL §7.2 → fill ONB §7
- [ ] Cascade model enforced: coordinator scans (full), executor references (HL §7.2), reviewer verifies (links)
- [ ] "No applicable knowledge items." documented as valid N/A (including bootstrap note for new projects)
- [ ] Table name unified: "Knowledge Citations" in HL, ONB, and verify.md

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| Citation tables become boilerplate (same items every task) | Reviewer checks relevance in Judge stage. Irrelevant citation = challenged |
| New projects have empty PV → empty tables for first tasks | Bootstrap note in template: "project in bootstrap phase" — valid, expected |
| Link format varies across tools | Relative markdown links are tool-agnostic. `[text](path)` universal |
| Executor finds coordinator missed a critical PV item | ONB §7 has "NEW" row type — executor adds missing items, coordinator sees in review |

---

*TS — TFW-38 / Phase B: Knowledge Citation Table | 2026-04-14*
