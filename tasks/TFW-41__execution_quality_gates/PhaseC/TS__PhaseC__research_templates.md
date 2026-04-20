# TS — TFW-41 / Phase C: Research Templates — Embedded Dimensional Analysis

> **Date**: 2026-04-20
> **Author**: Coordinator (AI)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-41](../HL-TFW-41__execution_quality_gates.md)

---

## 1. Objective

Embed dimensional analysis into the research stage templates (Gather, Extract, Challenge) so that morphological analysis emerges naturally from the stage sequence — not as a named methodology to comply with. Add a 4-line thread to the research workflow connecting the three stages. Add terminology origin note to conventions. This prevents the "first viable option" problem (Problem #10) while avoiding the "simulation" trap (HD-19).

## 2. Scope

### In Scope
- Modify `gather.md` template — add `## Dimensions` section
- Modify `extract.md` template — add `## Configuration Space` section
- Modify `challenge.md` template — add `## Consistency Check` section
- Modify `research/base.md` workflow — add dimensional analysis thread in Step 5
- Modify `conventions.md` — add terminology origin note

### Out of Scope
- TS/HL template changes (Phase A — done)
- Workflow gate changes (Phase B — done)
- Glossary terms (Phase D)
- GMA/Zwicky terminology in any researcher-facing template

## 3. Principles Check

| # | Principle (from HL §7) | Enforced by | Gate |
|---|----------------------|-------------|------|
| P1 | Gates over guidelines | AC-1, AC-2, AC-3 | Cross-stage dependency = structural gate (Extract needs Gather dimensions) |
| P2 | Requirements, not implementation | All ACs | ACs specify WHAT sections contain, not exact wording |
| P5 | Executor as engineer, not copier | AC-4 | Workflow thread gives connecting logic, not copy-paste instructions |
| P6 | Domain-agnostic by default | AC-1, AC-2, AC-3 | Templates use native terminology (Dimension, Configuration Space, Consistency Check), not methodology names |

## 4. Affected Files

| File | Action | Description |
|------|--------|------------|
| `.tfw/templates/research/gather.md` | MODIFY | Add `## Dimensions` section before `## Findings` |
| `.tfw/templates/research/extract.md` | MODIFY | Add `## Configuration Space` section before `## Findings` |
| `.tfw/templates/research/challenge.md` | MODIFY | Add `## Consistency Check` section before `## Findings` |
| `.tfw/workflows/research/base.md` | MODIFY | Add dimensional analysis thread in Step 5 |
| `.tfw/conventions.md` | MODIFY | Add terminology origin note (Zwicky reference, non-researcher-facing) |

**Budget:** 0 new files, 5 modifications. Defaults: max 14 files, max 8 new, max 1200 LOC.

## 5. Acceptance Criteria

### AC-1: Gather template — `## Dimensions` section

Research problems often have multiple independent decision factors. Gather decomposes the problem into these dimensions before collecting findings.

- [ ] `gather.md` has `## Dimensions` section placed BEFORE `## Findings`
- [ ] Section instruction: identify independent decision factors; each dimension gets a table with ≥3 alternatives
- [ ] Instruction explicitly says: do NOT mark any alternative as "recommended"
- [ ] Checkpoint sufficiency adds: `- [ ] Dimensions identified? (if ≥3 independent decision factors exist)`
Gate: Read `gather.md` → Dimensions section exists before Findings, no "recommended" marking

### AC-2: Extract template — `## Configuration Space` section  [depends: AC-1]

Extract constructs the full solution space by cross-referencing Gather's dimensions. This makes visible what the researcher doesn't see until enumeration.

- [ ] `extract.md` has `## Configuration Space` section placed BEFORE `## Findings`
- [ ] Section instruction: build cross-reference table using Gather's dimensions (one column per dimension, one row per viable combination)
- [ ] Instruction explicitly says: "Do NOT evaluate yet — list all combinations that are not obviously contradictory"
- [ ] Overflow protection: "If >30 combinations, list only configs where ≥1 dimension differs from the first-listed alternative"
Gate: Read `extract.md` → Configuration Space section exists, references Gather dimensions, no evaluation instruction

### AC-3: Challenge template — `## Consistency Check` section  [depends: AC-2]

Challenge eliminates inconsistent combinations through pairwise comparison. The output is surviving configurations and unexpected survivors.

- [ ] `challenge.md` has `## Consistency Check` section placed BEFORE `## Findings`
- [ ] Section instruction: take each pair of dimensions, ask "Can Alternative X coexist with Alternative Y?"
- [ ] Instruction: mark incompatible pairs, remove configurations containing them
- [ ] Instruction: note unexpected survivors (configurations that survived but weren't initially favored)
Gate: Read `challenge.md` → Consistency Check section exists, pairwise instruction present

### AC-4: Research workflow — dimensional analysis thread  [depends: AC-1]

The workflow needs a connecting thread explaining how the three sections work together across stages.

- [ ] `research/base.md` Step 5 has a dimensional analysis paragraph (≤6 lines)
- [ ] Thread explains: Gather decomposes into dimensions, Extract builds configuration space, Challenge eliminates inconsistencies
- [ ] Includes graceful degradation: "If <3 independent dimensions, use comparison matrix instead"
- [ ] Does NOT use GMA/Zwicky terminology
Gate: Read `research/base.md` → dimensional analysis thread exists in Step 5, no methodology names

### AC-5: Conventions — terminology origin note

The conventions should document that the dimensional analysis terminology originates from Zwicky's General Morphological Analysis, but this reference is for framework maintainers — not researchers.

- [ ] `conventions.md` has a note (in §-numbering or as addendum) stating terminology origin
- [ ] Note says: Dimension, Alternative, Configuration Space, Consistency Check, Surviving Configuration are TFW-native terms derived from Zwicky's GMA
- [ ] Note explicitly says this reference is for maintainers, not for inclusion in researcher-facing templates
Gate: Read `conventions.md` → origin note present, explicitly maintainer-facing

## 6. Technical Guidance

> Reference material, not instructions. Executor MAY deviate with justification in RF.

- **Template sizes:** gather.md (25 lines), extract.md (25 lines), challenge.md (25 lines). Target: ~35-40 lines each after additions.
- **Workflow size:** research/base.md (129 lines). Dimensional analysis thread adds ~5-6 lines. Target: ~135 lines.
- **Stage character alignment:** Dimensions → "What do we NOT know?" (decomposing unknowns). Configuration Space → "What do we NOT see?" (making invisible combinations visible). Consistency Check → "What do we NOT expect?" (finding unexpected constraints/survivors).
- **Cross-stage dependency mechanism:** Extract's Configuration Space table references Gather's Dimension table by column headers. This makes it structurally impossible to fill Configuration Space without having done dimension decomposition — natural enforcement without a checkpoint gate.
- **RES iter2 DR12:** Graceful degradation for <3 dimensions → comparison matrix (pros/cons format). This is a single instruction in the workflow, not template complexity.
- **conventions.md insertion point:** After §14 anti-patterns, before §15 Role Lock (or as a subsection of §14 / new §14.1). Keep concise — 3-4 lines.

## 7. Definition of Failure

- ❌ Any template uses "Zwicky", "GMA", "morphological box", or "morphological analysis" in researcher-facing text → reject RF
- ❌ Configuration Space section does NOT reference Gather dimensions → no cross-stage dependency → reject RF
- ❌ Dimensions section allows marking alternatives as "recommended" → defeats systematic exploration → reject RF
- ❌ Workflow thread exceeds 8 lines → violates conciseness budget → reject RF

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Template additions look like "another box to fill" → simulation risk | Sections are embedded in existing stage flow, not standalone. Cross-stage dependency forces genuine decomposition |
| Researchers skip Dimensions for simple problems | Graceful degradation: <3 dimensions → comparison matrix. Checkpoint item is conditional |
| conventions.md origin note leaks into templates | DoF explicitly rejects GMA terminology in researcher-facing text |

## 9. Cross-Phase Modifications (multi-phase only)

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `.tfw/conventions.md` | Phase A (anti-patterns, §14), Phase B (no changes) | Phase C adds terminology origin note — different section than Phase A's anti-patterns. No conflict. |

> **Cross-references**: HL-TFW-41 §4 Phase C, DR7-DR13 (embedded dimensional analysis), RES iter2 FC4 (instructions vs heuristics), FC5 (cross-stage dependencies), S6 (instructions produce compliance), S7 (natural enforcement).

---

*TS — TFW-41 / Phase C: Research Templates — Embedded Dimensional Analysis | 2026-04-20*
