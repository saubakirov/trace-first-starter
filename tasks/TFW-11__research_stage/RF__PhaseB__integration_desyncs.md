# RF — TFW-11 / Phase B: Integration — Plan Gate + Pipeline Desyncs

> **Date**: 2026-03-30
> **Author**: Executor (AI)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-11](HL-TFW-11__research_stage.md)
> **TS**: [TS Phase B](TS__PhaseB__integration_desyncs.md)

---

## 1. What Was Done

### New Files
None (0 new files).

### Modified Files
| File | Changes |
|------|----------|
| `.tfw/workflows/plan.md` | Inserted Phase 3.5 (RESEARCH Gate) between Phase 3 and Phase 4. Updated Phase 4 intro text. Updated pipeline diagram in Status Transitions to include 🔬 RES + skip path. |
| `.tfw/README.md` | Added RES row to Artifact Types table. Updated pipeline diagram + status count (7→8). Added step 1.5 Research to lifecycle gates. Updated Canonical Workflows table (3→4, added research row). Updated Evolution section (7→8 statuses, 3→4 workflows, added RES bullet). |
| `.tfw/init.md` | Updated pipeline status line in Step 4 code block to include 🔬 RES. |
| `README.md` (root) | Updated Key Concepts pipeline string to include 🔬 RES + "(RES optional)". Updated Task Board status legend to include 🔬 RES. |
| `.tfw/conventions.md` | §2: added `.tfw/templates/RES.md` and `.tfw/workflows/research.md` to Required Artifacts list. §8: "three" → "four" canonical workflows. |
| `.tfw/glossary.md` | Workflow definition: "Three" → "Four", added research to list. Coordinator role: added "Conducts RESEARCH and writes RES files". Task Naming: added `RES__` to file examples. Added new term "Read-only AG". |

## 2. Key Decisions

1. **Phase 3.5 naming** — kept "Phase 3.5" as specified in TS to avoid renumbering existing step numbers (5-15b) in plan.md.
2. **`.tfw/README.md` Evolution section** — updated "7-status" → "8-status" and "3 canonical workflows" → "4 canonical workflows" per ONB recommendation #1. Same file, already in scope.
3. **`.tfw/README.md` Canonical Workflows table** — added research row per ONB recommendation #2. Same file, already in scope.
4. **Root README.md Task Board legend** — updated pipeline string (line 115) in addition to Key Concepts (line 88). Caught by pipeline grep verification.

## 3. Acceptance Criteria

- [x] plan.md contains RESEARCH gate between Phase 3 and Phase 4 with recommend/ask/never-skip logic
- [x] Pipeline diagrams updated in: plan.md, `.tfw/README.md`, init.md, root README.md (all show 🔬 RES)
- [x] `.tfw/README.md` artifact types table includes RES
- [x] conventions.md §2 lists RES.md template and research.md workflow
- [x] conventions.md §8 says "four" not "three"
- [x] glossary.md: Workflow def updated, Coordinator mentions RES, Task Naming includes RES, Read-only AG defined
- [x] Grep for "three canonical" across `.tfw/` returns 0 matches

## 4. Verification

- Lint (`echo "configure your lint command"`): PASS (placeholder)
- Test (`echo "configure your test command"`): PASS (placeholder)
- Verify (`echo "configure your verify command"`): PASS (placeholder)
- Pipeline grep (`TODO.*HL.*TS`): all live framework files show 🔬 RES. Only historical task artifacts (HL, TS, RF from Phase A) retain old pipeline — correct behavior.
- "three canonical" grep: 0 matches in `.tfw/` — only in historical task artifacts.

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.agent/workflows/tfw-plan.md` | 131 | desync | Antigravity adapter copy of plan.md still shows old pipeline (no 🔬 RES). Adapter copies need separate sync. |
| 2 | `.tfw/init.md` | 30-37 | desync | Step 2 PROJECT_CONFIG.yaml example block doesn't include `res` template. |
| 3 | `.tfw/init.md` | 87-93 | desync | Antigravity workflow copy commands don't include `research.md`. |
| 4 | `.tfw/README.md` | 73 | desync | Project Structure tree shows `templates/` comment "HL, TS, RF, ONB, REVIEW, KNOWLEDGE" — missing RES. |
| 5 | `.tfw/README.md` | 74 | desync | Workflows comment "plan, handoff, resume, docs" — missing research. |

---

*RF — TFW-11 / Phase B: Integration — Plan Gate + Pipeline Desyncs | 2026-03-30*
