# TS — TFW-42 / Phase A: Conventions & Templates

> **Date**: 2026-04-30
> **Author**: Coordinator (Antigravity)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-42](../HL-TFW-42__research_cycle_restructure.md)

---

## 1. Objective
Rewrite conventions.md §4 to establish the new folder structure (unified `research/iterN/`, numbered stages, kebab-case phases), update the iterations.yaml schema (add `agent` + `sources`), rename stage file templates, and add agent selection guidance. This is the foundation phase — all workflow and glossary changes in Phase B/C depend on the conventions written here.

## 2. Scope

### In Scope
- conventions.md §4: Research subfolder, Multi-iteration research, Multi-phase folder structure
- conventions.md §4: artifact filename table (PhaseA → phase-a)
- conventions.md §4: iterations.yaml schema + example
- conventions.md §4: agent selection guidance subsection (5-row capability table)
- Stage file template renames (4 files)
- RES template header update (file path convention)

### Out of Scope
- Workflow files (plan.md, research/base.md) → Phase B
- Glossary updates → Phase C
- Adapter syncing → Phase C
- review/ subfolder structure (unchanged)

## 3. Principles Check

| # | Principle (from HL §7) | Enforced by | Gate |
|---|----------------------|-------------|------|
| P1 | Locality over scattering | AC-1, AC-2 | RES.md co-located with stages; iterations.yaml inside research/ |
| P2 | Sort order = execution order | AC-3 | Numbered files: `1_briefing` < `2_gather` < `3_extract` < `4_challenge` |
| P3 | Container over proliferation | AC-1 | Single `research/` with `iterN/` subfolders |
| P4 | Consistent casing | AC-4 | phase-a/phase-b in filename table |
| P5 | Optional enrichment | AC-5 | `agent` and `sources` fields marked optional |
| P6 | Domain-agnostic | N/A | Conventions §4 contains no domain-specific examples |
| P7 | Tool-agnostic guidance | AC-6 | Capability categories, no tool names in table |

## 4. Affected Files

| File | Action | Description |
|------|--------|------------|
| `.tfw/conventions.md` | MODIFY | §4 Research subfolder, Multi-iteration, Multi-phase, filename table, new Agent Guidance subsection |
| `.tfw/templates/research/briefing.md` | RENAME → `1_briefing.md` | Numbered stage template |
| `.tfw/templates/research/gather.md` | RENAME → `2_gather.md` | Numbered stage template |
| `.tfw/templates/research/extract.md` | RENAME → `3_extract.md` | Numbered stage template |
| `.tfw/templates/research/challenge.md` | RENAME → `4_challenge.md` | Numbered stage template |
| `.tfw/templates/RES.md` | MODIFY | Update header path example (iterN/RES.md) |

**Budget:** 0 new files, 6 modifications (4 renames + 2 content edits). Within limits (max 14 files, max 12 modified).

## 5. Acceptance Criteria

### AC-1: Research folder structure
The conventions.md §4 "Research subfolder" and "Multi-iteration research" sections describe the new structure where all research artifacts live inside a single `research/` container.

- [ ] `research/` described as single container for all research content
- [ ] `research/iterations.yaml` is the documented location (not task root)
- [ ] `research/iterN/` is the documented pattern for iteration subfolders (not `researchN/`)
- [ ] `research/iterN/RES.md` is the documented RES location (not task root)
- [ ] Trace rule preserved: "never delete previous iteration's files"
- [ ] Table shows updated paths for iterations 1, 2, N

Gate: Read §4 — verify all paths use `research/iterN/` pattern, no references to `researchN/` or root-level RES.

### AC-2: iterations.yaml schema [depends: AC-1]
The conventions.md §4 iterations.yaml code block reflects the enriched schema with `agent` and `sources` fields.

- [ ] Schema example includes `agent:` field (commented-out or explicit, marked optional)
- [ ] Schema example includes `sources:` field (commented-out or explicit, marked optional)
- [ ] `res_file` paths in schema example use `research/iterN/RES.md` convention
- [ ] No `brief`, `notes`, or `depends_on` fields in schema
- [ ] Text explains: `agent` = traceability, not dispatch (per RES D7)

Gate: Read the YAML code block in §4 — verify 2 new optional fields present, 3 dropped fields absent.

### AC-3: Numbered stage files
Stage file templates are renamed with numeric prefixes that match execution order.

- [ ] `.tfw/templates/research/1_briefing.md` exists (old `briefing.md` deleted)
- [ ] `.tfw/templates/research/2_gather.md` exists (old `gather.md` deleted)
- [ ] `.tfw/templates/research/3_extract.md` exists (old `extract.md` deleted)
- [ ] `.tfw/templates/research/4_challenge.md` exists (old `challenge.md` deleted)
- [ ] conventions.md §4 lists numbered filenames

Gate: `ls .tfw/templates/research/` — 4 files with numeric prefixes, 0 files without.

### AC-4: Phase folder naming [depends: AC-1]
Conventions.md §4 "Multi-phase folder structure" and artifact filename table use kebab-case.

- [ ] Folder example shows `phase-a/`, `phase-b/` (not `PhaseA/`, `PhaseB/`)
- [ ] Artifact filename table uses `phase-a` in format and example columns
- [ ] Phase artifact filenames: `TS__phase-a__{title}.md`, `RF__phase-a__{title}.md`, etc.

Gate: Grep conventions.md for `PhaseA` — 0 matches. Grep for `phase-a` — multiple matches.

### AC-5: Schema backward compatibility
Existing iterations.yaml fields are preserved unchanged.

- [ ] Fields preserved: `task_id`, `title`, `min_iterations`, `max_iterations`, `iterations[]` with: `number`, `focus`, `hypotheses`, `status`, `res_file`
- [ ] New fields `agent` and `sources` are additive (do not replace any existing field)

Gate: Compare old and new schema — all 9 original fields present.

### AC-6: Agent selection guidance
A new subsection in conventions.md §4 provides tool-agnostic guidance for multi-agent research.

- [ ] Subsection titled "Agent selection guidance" (or similar)
- [ ] Contains a 5-row capability table: web research, code audit, infra recon, architecture synthesis, data analysis
- [ ] Table columns: Research Activity, Key Capability, When to consider
- [ ] Table does NOT name specific tools (no "Antigravity", "Claude Code", "Codex")
- [ ] Footer or note: "guidance, not prescription — coordinator decides"

Gate: Read the subsection — verify 5 rows, no tool brand names, capability-based framing.

## 6. Technical Guidance

- conventions.md §4 currently spans lines 107-191. The rewrite affects 3 sub-sections: "Research subfolder" (lines 131-146), "Multi-iteration research" (within same), "Multi-phase folder structure" (lines 174-191). The iterations.yaml code block is at lines 152-170.
- The artifact filename table (lines 113-125) needs `PhaseA` → `phase-a` replacement in all Phase rows.
- Stage file renames: use `git mv` or equivalent for traceability. Content of templates stays the same — only filenames change.
- Agent guidance subsection: place after the iterations.yaml block, before "Review subfolder" (line 148).
- RES.md template: line 15 references `research/briefing.md` — update to `research/iterN/1_briefing.md` pattern.

## 7. Definition of Failure

- ❌ Any reference to `researchN/` (old multi-iteration pattern) survives in §4
- ❌ Any reference to `PhaseA` (PascalCase) survives in §4 filename table or folder structure
- ❌ Stage file templates in `.tfw/templates/research/` lack numeric prefix
- ❌ `depends_on`, `brief`, or `notes` appear in iterations.yaml schema example

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Missed references to old naming in conventions.md sections outside §4 | Grep entire file for `PhaseA`, `research2`, `research3` after edits |
| RES template briefing path becomes confusing with iterN/ prefix | Keep reference generic: "See `1_briefing.md` in iteration folder" |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `.tfw/conventions.md` | Phase B (workflows reference §4) | Phase A sets §4 structure; Phase B will update workflow references to §4 paths |

---

*TS — TFW-42 / Phase A: Conventions & Templates | 2026-04-30*
