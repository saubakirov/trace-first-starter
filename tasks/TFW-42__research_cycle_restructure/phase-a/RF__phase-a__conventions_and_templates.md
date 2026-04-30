# RF — TFW-42 / Phase A: Conventions & Templates

> **Date**: 2026-04-30
> **Author**: Executor (Antigravity)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-42](../HL-TFW-42__research_cycle_restructure.md)
> **TS**: [TS Phase A](TS__phase-a__conventions_and_templates.md)

---

## 1. What Was Done

### New Files
| File | Description |
|------|------------|
| `.tfw/templates/research/1_briefing.md` | Renamed stage template (was `briefing.md`) |
| `.tfw/templates/research/2_gather.md` | Renamed stage template (was `gather.md`) |
| `.tfw/templates/research/3_extract.md` | Renamed stage template (was `extract.md`) |
| `.tfw/templates/research/4_challenge.md` | Renamed stage template (was `challenge.md`) |

### Modified Files
| File | Changes |
|------|---------| 
| `.tfw/conventions.md` | §4 filename table: `Phase{X}` → `phase-{x}` in all 5 Phase rows. §4 Research subfolder: complete rewrite — unified `research/` container, `research/iterN/` pattern, numbered stage files, co-located `RES.md`. §4 iterations.yaml: moved from task root to `research/`, enriched schema with `agent` + `sources` optional fields, updated `res_file` paths. §4 new Agent selection guidance subsection (5-row capability table). §4 Review subfolder: updated parallel reference from `research/gather.md` to `research/iterN/1_briefing.md`. §4 Multi-phase folder structure: `PhaseA/` → `phase-a/`, updated all artifact filenames in tree. Fixed section ordering (Research → iterations.yaml → Agent guidance → Review → Multi-phase). |
| `.tfw/templates/RES.md` | Line 15: `research/briefing.md` → `1_briefing.md in iteration folder` |

### Deleted Files
| File | Reason |
|------|--------|
| `.tfw/templates/research/briefing.md` | Renamed to `1_briefing.md` |
| `.tfw/templates/research/gather.md` | Renamed to `2_gather.md` |
| `.tfw/templates/research/extract.md` | Renamed to `3_extract.md` |
| `.tfw/templates/research/challenge.md` | Renamed to `4_challenge.md` |

## 2. Key Decisions

1. **Section reordering in §4.** The TS assumed iterations.yaml block was after Review subfolder, but actually Review subfolder (line 148) was between Research subfolder (131) and iterations.yaml (152). Restructured to logical grouping: Research subfolder → Multi-iteration → iterations.yaml → Agent guidance → Review subfolder → Multi-phase. Coordinator approved this in ONB §6.

2. **RES template briefing path made relative.** Since RES.md now lives inside `research/iterN/` alongside its stage files, changed the reference from absolute `research/briefing.md` to relative `1_briefing.md in iteration folder`.

3. **Multi-phase tree updated.** Replaced `RES__PROJ-5__query_redesign.md ← Master RES (if any)` with `research/ ← Master research (if any)` to align with the new container convention.

## 3. Acceptance Criteria

- [x] **AC-1: Research folder structure** — `research/` is single container, `research/iterations.yaml` documented, `research/iterN/` pattern used, `research/iterN/RES.md` co-located, trace rule preserved, table shows iter1/iter2/iterN paths
- [x] **AC-2: iterations.yaml schema** — `agent:` field present (commented-out, marked optional), `sources:` field present (commented-out, marked optional), `res_file` paths use `research/iterN/RES.md`, no `brief`/`notes`/`depends_on` fields, text explains "traceability, not dispatch"
- [x] **AC-3: Numbered stage files** — `1_briefing.md`, `2_gather.md`, `3_extract.md`, `4_challenge.md` exist in templates/research/; old files deleted; conventions.md §4 lists numbered filenames
- [x] **AC-4: Phase folder naming** — folder example shows `phase-a/`, `phase-b/`; filename table uses `phase-{x}` format and `phase-a` example; 0 matches for `PhaseA` in §4
- [x] **AC-5: Schema backward compatibility** — all 9 original fields preserved (`task_id`, `title`, `min_iterations`, `max_iterations`, `iterations[]` with `number`, `focus`, `hypotheses`, `status`, `res_file`); `agent` and `sources` are additive
- [x] **AC-6: Agent selection guidance** — subsection titled "Agent selection guidance", 5-row capability table (web research, code audit, infra recon, architecture synthesis, data analysis), columns: Research Activity / Key Capability / When to consider, no tool brand names, footer: "guidance, not prescription"

## 4. Verification

- Lint: N/A (markdown documentation changes only)
- Tests: N/A (no test infrastructure for conventions)
- Verify:
  - `ls .tfw/templates/research/` → 4 files with numeric prefixes, 0 without ✅
  - Grep `PhaseA` in conventions.md → 0 matches ✅
  - Grep `researchN/`, `research2/`, `research3/` in conventions.md → 0 matches ✅
  - Grep `depends_on`, `brief:`, `notes:` in conventions.md → 0 matches ✅
  - Visual verification of all updated sections — confirmed correct ✅

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/compilable_contract.md` | 56, 78 | naming | References `PhaseA/` in resolution rules — needs update when conventions adopt kebab-case. Not in Phase A scope |
| 2 | `.tfw/workflows/handoff.md` | 140-141 | naming | Multi-Phase Task Flow example uses `HL__PhaseA`, `TS__PhaseA`, `RF__PhaseA` — needs Phase B/C update |
| 3 | `.tfw/workflows/plan.md` | 134-136 | naming | Multi-phase structure example uses `PhaseA/`, `HL__PhaseA__`, `TS__PhaseA__` — needs Phase B update |
| 4 | `.tfw/workflows/research/base.md` | 53 | naming | References `research/briefing.md` and `researchN/briefing.md` — needs Phase B update to use `research/iterN/1_briefing.md` |
| 5 | `.tfw/CHANGELOG.md` | 284 | naming | Historical reference to `PhaseA/`, `PhaseB/` in v0.6.0 — historical, no action needed |

## 6. Fact Candidates

No fact candidates.

## 7. Strategic Insights (Execution)

No strategic insights.

## 8. Diagrams

No diagrams.

---

*RF — TFW-42 / Phase A: Conventions & Templates | 2026-04-30*
