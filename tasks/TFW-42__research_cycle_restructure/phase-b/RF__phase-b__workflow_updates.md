# RF — TFW-42 / Phase B: Workflow Updates

> **Date**: 2026-04-30
> **Author**: Executor (Antigravity)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-42](../HL-TFW-42__research_cycle_restructure.md)
> **TS**: [TS Phase B](TS__phase-b__workflow_updates.md)

---

## 1. What Was Done

### New Files
| File | Description |
|------|-------------|
| (none) | — |

### Modified Files
| File | Changes |
|------|---------|
| `.tfw/workflows/research/base.md` | Step 0: `iterations.yaml` → `research/iterations.yaml`, `researchN/` → `research/iterN/`, `RES__*` → `research/iterN/RES.md`. Step 3: `research/` → `research/iter1/`, `researchN/` → `research/iterN/`, template list now explicit with numbered names. Step 4: briefing path → `research/iterN/1_briefing.md`, template ref → `1_briefing.md`. Step 5: template ref now lists `2_gather.md`, `3_extract.md`, `4_challenge.md`. Step 6: stage file list numbered, RES output → `research/iterN/RES.md`, removed iteration-specific naming variants. |
| `.tfw/workflows/plan.md` | Step 6b: `iterations.yaml` path → `research/iterations.yaml`, added `agent` + `sources` optional fields, added 1-sentence multi-agent reference to conventions.md §4. Step 6c: `RES__*` → `research/iterN/RES.md`, `iterations.yaml` → `research/iterations.yaml` (3 occurrences). Step 7: `PhaseA/` → `phase-a/`, `PhaseB/` → `phase-b/`, artifact filenames updated, removed `RES,` from tree comment (RES no longer at task root). |

## 2. Key Decisions

1. **plan.md Step 6c also updated (beyond explicit TS scope).** Step 6c had 3 references to old-convention paths (`RES__*`, `iterations.yaml` at task root). TS §7 Definition of Failure explicitly forbids old paths in "either workflow", so updating Step 6c was mandatory to pass the DoF gate. This was flagged in ONB §5 Risk #1.

2. **Removed `RES,` from plan.md Step 7 tree comment.** The old comment said `← master HL, RES, research/ here`. Since RES files now live inside `research/iterN/RES.md` (not at task root), the `RES,` reference was stale. Updated to `← master HL, research/ here` to match conventions.md §4 Multi-phase folder structure.

3. **Explicit numbered file lists in base.md.** Where the old workflow said "Copy templates from `templates/research/`", the new version lists all 4 numbered files explicitly: `1_briefing.md`, `2_gather.md`, `3_extract.md`, `4_challenge.md`. This reinforces P2 (sort order = execution order) by making the numbering visible at every reference point.

## 3. Acceptance Criteria

- [x] **AC-1: research/base.md paths updated**
  - [x] Step 0: iteration detection checks `research/iterations.yaml` (line 17)
  - [x] Step 0: iteration count uses `research/iterN/` folders (line 19)
  - [x] Step 0: resume checks use `research/iterN/RES.md` (lines 24-25)
  - [x] Step 3: iteration 1 creates `research/iter1/`, iteration N creates `research/iterN/` (lines 41-42)
  - [x] Step 3: no reference to `research2/`, `research3/` or `researchN/` (lines 41-42)
  - [x] Step 4: briefing path = `research/iterN/1_briefing.md` (line 53)
  - [x] Step 5: stage references use numbered names (line 64)
  - [x] Step 6: RES output path = `research/iterN/RES.md` (line 88)
  - [x] Step 6: no reference to `RES__{ID}__title.md` or `RES__iterN__title.md` (lines 87-88)
  - [x] Template copy instruction references numbered files (line 44)
  - Gate: grep `researchN/`, `research2/`, `RES__iter`, `briefing.md` (without number) — 0 matches each ✅

- [x] **AC-2: plan.md phase structure**
  - [x] Step 7 code block shows `phase-a/`, `phase-b/` (lines 137, 140)
  - [x] Artifact filenames: `HL__phase-a__{title}.md`, `TS__phase-a__{title}.md` (lines 138-139)
  - [x] research/ location shows `research/` at task root (line 136)
  - Gate: 0 matches for `PhaseA` in plan.md ✅

- [x] **AC-3: plan.md multi-agent reference**
  - [x] Step 6b mentions `agent` and `sources` as optional fields (line 95)
  - [x] Step 6b includes multi-agent reference: "For multi-agent research, see conventions.md §4 (Agent selection guidance)." (line 97)
  - [x] Step 6b states iterations.yaml location = `research/iterations.yaml` (line 90)
  - [x] No tool brand names in plan.md — 0 matches for Antigravity/Claude Code/Codex ✅

## 4. Verification

- Lint: N/A (markdown documentation changes only)
- Tests: N/A (no test infrastructure for conventions)
- Verify:
  - Grep `researchN/` in base.md → 0 matches ✅
  - Grep `research2/` in base.md → 0 matches ✅
  - Grep `RES__iter` in base.md → 0 matches ✅
  - Grep `briefing.md` (without number) in base.md → 0 matches ✅
  - Grep `PhaseA` in plan.md → 0 matches ✅
  - Grep `researchN/` in plan.md → 0 matches ✅
  - Grep `Antigravity|Claude Code|Codex` in plan.md → 0 matches ✅
  - Visual verification of all updated sections — confirmed correct ✅

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/workflows/handoff.md` | 140-144 | naming | Multi-Phase Task Flow example still uses `HL__PhaseA`, `TS__PhaseA`, `RF__PhaseA`, `HL__PhaseB`, `TS__PhaseB`, `RF__PhaseB`. Needs kebab-case update. Carried from TD-112 |
| 2 | `.tfw/compilable_contract.md` | 56, 78 | naming | Still references `PhaseA/` in resolution rules. Carried from TD-111 |

## 6. Fact Candidates

No fact candidates.

## 7. Strategic Insights (Execution)

No strategic insights.

## 8. Diagrams

No diagrams.

---

*RF — TFW-42 / Phase B: Workflow Updates | 2026-04-30*
