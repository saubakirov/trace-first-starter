# TS — TFW-42 / Phase B: Workflow Updates

> **Date**: 2026-04-30
> **Author**: Coordinator (Antigravity)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-42](../HL-TFW-42__research_cycle_restructure.md)

---

## 1. Objective
Update the two core workflows (research/base.md and plan.md) to reference the new folder structure, numbered stage files, kebab-case phases, and enriched iterations.yaml from Phase A conventions. After this phase, any agent following the workflows will produce artifacts in the correct locations with correct naming.

## 2. Scope

### In Scope
- research/base.md: Step 0 (iteration detection), Step 3 (subfolder creation), Step 4 (briefing path), Step 6 (RES synthesis path)
- plan.md: Step 6b (iterations.yaml location + multi-agent reference), Step 7 (phase folder structure)

### Out of Scope
- conventions.md (completed in Phase A)
- Stage file template content (only paths/references change)
- Glossary, adapters → Phase C
- Other workflows (handoff.md, review.md, resume.md) — not affected by folder structure changes

## 3. Principles Check

| # | Principle (from HL §7) | Enforced by | Gate |
|---|----------------------|-------------|------|
| P1 | Locality over scattering | AC-1 | research/base.md paths all point inside `research/iterN/` |
| P2 | Sort order = execution order | AC-1 | Stage file references use `1_briefing.md`, `2_gather.md`, etc. |
| P3 | Container over proliferation | AC-1 | No `researchN/` references remain |
| P4 | Consistent casing | AC-2 | plan.md Step 7 uses `phase-a/` |
| P5 | Optional enrichment | AC-3 | plan.md Step 6b: `agent`/`sources` mentioned as optional |
| P7 | Tool-agnostic guidance | AC-3 | plan.md references conventions.md §4 for guidance, no tool names |

## 4. Affected Files

| File | Action | Description |
|------|--------|------------|
| `.tfw/workflows/research/base.md` | MODIFY | Steps 0, 3, 4, 6: folder paths, stage file names, RES output path |
| `.tfw/workflows/plan.md` | MODIFY | Step 6b: iterations.yaml location + multi-agent reference. Step 7: phase-a naming |

**Budget:** 0 new files, 2 modifications. Within limits.

## 5. Acceptance Criteria

### AC-1: research/base.md paths updated
All references in base.md reflect the new folder structure and numbered stage files.

- [ ] Step 0: iteration detection checks `research/iterations.yaml` (not task root)
- [ ] Step 0: iteration count uses `research/iterN/` folders (not `researchN/`)
- [ ] Step 0: resume checks use `research/iterN/RES.md` (not root-level `RES__*`)
- [ ] Step 3: iteration 1 creates `research/iter1/`, iteration N creates `research/iterN/`
- [ ] Step 3: no reference to `research2/`, `research3/` or `researchN/`
- [ ] Step 4: briefing path = `research/iterN/1_briefing.md` (numbered)
- [ ] Step 5: stage references use numbered names (`1_briefing`, `2_gather`, `3_extract`, `4_challenge`)
- [ ] Step 6: RES output path = `research/iterN/RES.md`
- [ ] Step 6: no reference to `RES__{ID}__title.md` or `RES__iterN__title.md` at task root
- [ ] Template copy instruction references numbered files from `templates/research/`

Gate: Grep base.md for `researchN/`, `research2/`, `RES__iter`, `briefing.md` (without number) — 0 matches each.

### AC-2: plan.md phase structure [depends: AC-1]
plan.md Step 7 multi-phase example uses kebab-case folders.

- [ ] Step 7 code block shows `phase-a/`, `phase-b/` (not `PhaseA/`, `PhaseB/`)
- [ ] Artifact filenames in example: `HL__phase-a__{title}.md`, `TS__phase-a__{title}.md`
- [ ] research/ location in example shows `research/` at task root (container, not research iteration reference)

Gate: Read Step 7 code block — verify kebab-case phase folders.

### AC-3: plan.md multi-agent reference [depends: AC-2]
plan.md Step 6b mentions multi-agent as a possibility and references conventions.md for guidance.

- [ ] Step 6b mentions `agent` and `sources` as optional fields in iterations.yaml
- [ ] Step 6b includes a 1-sentence reference: "For multi-agent research, see conventions.md §4 (Agent selection guidance)." or equivalent
- [ ] Step 6b states iterations.yaml location = `research/iterations.yaml` (not task root)
- [ ] No tool brand names in plan.md (no "Antigravity", "Claude Code", "Codex")

Gate: Read Step 6b — verify 1-sentence multi-agent reference exists, no tool names, correct path.

## 6. Technical Guidance

- research/base.md is 131 lines. Key sections to modify:
  - Step 0 (lines 12-26): iteration detection logic — `researchN/` → `research/iterN/`, `iterations.yaml` path
  - Step 3 (lines 39-49): subfolder creation — `research/` → `research/iter1/`, `researchN/` → `research/iterN/`
  - Step 4 (lines 51-58): briefing path — `research/briefing.md` → `research/iterN/1_briefing.md`
  - Step 5 (lines 60-83): stage references — add numbered prefixes
  - Step 6 (lines 85-96): RES naming — `RES__{ID}__title.md` → `research/iterN/RES.md`
- plan.md is 153 lines. Key sections:
  - Step 6b (lines 88-96): iterations.yaml creation — add `agent`/`sources`, change path, add multi-agent reference
  - Step 7 (lines 131-140): phase subfolder example — `PhaseA/` → `phase-a/`

## 7. Definition of Failure

- ❌ Any `researchN/` or `research2/` path remains in either workflow
- ❌ Any `PhaseA` reference remains in plan.md Step 7
- ❌ No multi-agent reference in plan.md Step 6b
- ❌ Stage file references without numeric prefix in base.md

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Step references in base.md shift during editing | Use section headers (Step 0, Step 3, etc.) for navigation, not line numbers |
| plan.md Step 6c also references RES paths | Verify Step 6c consistency after Step 6b changes |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `.tfw/conventions.md` | Phase A (primary) | Phase B does NOT modify conventions.md — only references it. If conventions paths change, Phase B uses the Phase A version as source of truth |

---

*TS — TFW-42 / Phase B: Workflow Updates | 2026-04-30*
