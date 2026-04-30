# TS — TFW-42 / Phase C: Glossary & Adapter Sync

> **Date**: 2026-04-30
> **Author**: Coordinator (Antigravity)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-42](../HL-TFW-42__research_cycle_restructure.md)

---

## 1. Objective
Update glossary terms to reflect the new folder structure and iterations.yaml schema. Sync adapter workflow copies to match the modified workflows from Phase B. After this phase, all TFW documentation is internally consistent — glossary, conventions, workflows, and adapters all reference the same paths and naming.

## 2. Scope

### In Scope
- glossary.md: "Iteration (Research)", "iterations.yaml", "min_iterations" entries
- Adapter workflow sync: copy modified `research/base.md` and `plan.md` to adapter directories
- CHANGELOG.md entry for TFW-42
- VERSION bump

### Out of Scope
- conventions.md (Phase A)
- Workflow content changes (Phase B)
- project_config.yaml (no structural changes needed — `min_iterations`, research config unchanged)

## 3. Principles Check

| # | Principle (from HL §7) | Enforced by | Gate |
|---|----------------------|-------------|------|
| P1 | Locality over scattering | AC-1 | Glossary references `research/iterN/` paths |
| P3 | Container over proliferation | AC-1 | No `researchN/` in glossary |
| P5 | Optional enrichment | AC-1 | Glossary mentions `agent`/`sources` as optional |
| P7 | Tool-agnostic guidance | AC-1 | No tool brand names in glossary |

## 4. Affected Files

| File | Action | Description |
|------|--------|------------|
| `.tfw/glossary.md` | MODIFY | Update 3 entries: Iteration, iterations.yaml, min_iterations |
| `.agent/workflows/tfw-research.md` | MODIFY | Copy of `.tfw/workflows/research/base.md` (adapter sync) |
| `.agent/workflows/tfw-plan.md` | MODIFY | Copy of `.tfw/workflows/plan.md` (adapter sync) |
| `.tfw/CHANGELOG.md` | MODIFY | Add TFW-42 entry |
| `.tfw/VERSION` | MODIFY | Version bump |

**Budget:** 0 new files, 5 modifications. Within limits.

## 5. Acceptance Criteria

### AC-1: Glossary entries updated
All iteration-related glossary entries reflect the new folder structure, RES location, and iterations.yaml schema.

- [ ] "Iteration (Research)": `researchN/` → `research/iterN/`, `RES__iterN__*.md` → `research/iterN/RES.md`
- [ ] "iterations.yaml": "at task root" → "inside `research/` subfolder". Mentions `agent` (optional, free-text) and `sources` (optional, list) as fields
- [ ] "min_iterations": no path references to update (config-only entry), verify unchanged
- [ ] No `PhaseA` references in glossary (verify: was none before, confirm still none)

Gate: Grep glossary.md for `researchN/`, `RES__iter`, "at task root" — 0 matches each.

### AC-2: Adapter workflow sync [depends: AC-1]
Adapter workflow copies match the source files from Phase B.

- [ ] `.agent/workflows/tfw-research.md` is byte-identical to `.tfw/workflows/research/base.md`
- [ ] `.agent/workflows/tfw-plan.md` is byte-identical to `.tfw/workflows/plan.md`
- [ ] Other adapter directories (claude-code, cursor) checked — if workflow copies exist, sync them too

Gate: `diff .tfw/workflows/research/base.md .agent/workflows/tfw-research.md` — no differences.

### AC-3: Version & changelog
TFW-42 is recorded in CHANGELOG and VERSION is bumped.

- [ ] CHANGELOG.md has an entry for the new version referencing TFW-42
- [ ] VERSION file updated to new version (patch bump: 0.8.5 → 0.8.6)
- [ ] project_config.yaml `tfw.version` updated to match VERSION

Gate: `cat .tfw/VERSION` matches CHANGELOG latest entry.

## 6. Technical Guidance

- Glossary entries at lines 144-151. Three entries to update — all are single-paragraph definitions.
- Adapter sync: convention.md F1/F5 — adapters are exact byte-copies. Use `cp` command.
- Check `.agent/workflows/` directory for existing workflow copies before syncing.
- CHANGELOG format: Keep a Changelog (keepachangelog.com). Section: `### Changed`.
- Version: current 0.8.5. This is a structural convention change (not breaking) — patch bump appropriate.

## 7. Definition of Failure

- ❌ Glossary references `researchN/` or `RES__iterN__` (old naming)
- ❌ Adapter workflow copies differ from source files
- ❌ No CHANGELOG entry for TFW-42

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Additional adapter directories with workflow copies not identified | Check all 3 adapter dirs + project `.agent/` dir |
| Version conflict if another task lands between Phase A and C | Unlikely — single active task. Resolve at merge if needed |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `.tfw/CHANGELOG.md` | Any future task | Standard append — no conflict risk |
| `.tfw/VERSION` | Any future task | Last writer wins — verify at merge |

---

*TS — TFW-42 / Phase C: Glossary & Adapter Sync | 2026-04-30*
