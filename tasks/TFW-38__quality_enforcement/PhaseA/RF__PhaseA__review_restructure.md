# RF — TFW-38 / Phase A: Review Restructure + Full Enforcement Chain

> **Date**: 2026-04-14
> **Author**: Executor
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> **TS**: [TS Phase A](TS__PhaseA__review_restructure.md)

---

## 1. What Was Done

### New Files
| File | Description |
|------|------------|
| `.tfw/workflows/review/code.md` | Code review mode — 4 verify actions + 4 mode-specific checklist items (#7-10) |
| `.tfw/workflows/review/docs.md` | Docs review mode — 3 verify actions + 2 mode-specific checklist items (#7-8) |
| `.tfw/workflows/review/spec.md` | Spec review mode — 3 verify actions + 2 mode-specific checklist items (#7-8) |

### Modified Files
| File | Changes |
|------|---------| 
| `.tfw/workflows/review.md` | Full restructure: Steps 0-4 (Mode/Map/Verify/Judge/Decide) + Steps 5-7 (Tech Debt/Traces/Knowledge). Step 2: Pattern A Limits table with `min_verify_ratio` (0.42) + escalation rule. |
| `.tfw/templates/REVIEW.md` | Restructured from §1-§5 to §1-§7: Map/Verify/Judge/Verdict/Tech Debt/Traces/Fact Candidates. Added Review Mode to header. Mode-specific placeholder as HTML comment. |
| `.tfw/workflows/handoff.md` | Phase 1: KNOWLEDGE.md added to inconsistency check (line 36). Phase 3: §1-§8 explicit enumeration with "Never omit §6-8" mandate (lines 73-82). |
| `.tfw/workflows/research/base.md` | Step 6: Findings Map added as item 5 with explicit N/A option. Renumbered items 6-8. |
| `.tfw/workflows/plan.md` | Step 3: knowledge citation check added as item 4 with explicit N/A option. "Ask questions" renumbered to 5. |
| `.tfw/conventions.md` | §14: 4 new anti-patterns (reviewer no-verify, executor §6-8 skip, researcher no-map, coordinator no-cite). Lines 343-346. |
| `.tfw/PROJECT_CONFIG.yaml` | Added `tfw.review.default_mode: code` + `tfw.review.min_verify_ratio: 0.42`. |
| `.tfw/workflows/config.md` | Config Sync Registry: new `review` section with `default_mode` and `min_verify_ratio` entries. |
| `.agent/workflows/tfw-review.md` | Adapter re-synced from `.tfw/workflows/review.md`. |
| `.agent/workflows/tfw-handoff.md` | Adapter re-synced from `.tfw/workflows/handoff.md`. |
| `.agent/workflows/tfw-research.md` | Adapter re-synced from `.tfw/workflows/research/base.md`. |
| `.agent/workflows/tfw-plan.md` | Adapter re-synced from `.tfw/workflows/plan.md`. |
| `.agent/workflows/tfw-config.md` | Adapter re-synced from `.tfw/workflows/config.md`. |

## 2. Key Decisions

1. **REVIEW template mode-specific placeholder as HTML comment** (`<!-- Add mode-specific checklist items from mode file below -->`) instead of pseudo-table-row. Cleaner for agent consumption — approved in ONB §4.2.
2. **review.md Step 7 §-reference updated** from §4 to §6 (Traces Updated) to match the new REVIEW template structure. §4 is now the Verdict section.
3. **Preserved handoff.md step 12 numbering** for Phase 3 RF creation — per ONB §4.4 approval.
4. **`min_verify_ratio: 0.42` added** (post-approval user request). Replaces hardcoded "2-3 files" with configurable ratio + escalation-on-discrepancy. Pattern A enforcement (inline default + config key). Config Sync Registry updated.

## 3. Acceptance Criteria

- [x] `review.md` has Step 0 (mode selection) + Steps 1-4 (Map, Verify, Judge, Decide)
- [x] `REVIEW.md` template has §1-§7 structure (Map, Verify, Judge, Verdict, Tech Debt, Traces, Fact Candidates)
- [x] 3 mode files exist in `.tfw/workflows/review/` with mode-specific checklists and verify actions
- [x] `handoff.md` Phase 1 includes KNOWLEDGE.md in inconsistency check; Phase 3 explicitly enumerates §1-§8 with "never omit §6-8"
- [x] `research/base.md` Step 6 includes Findings Map in synthesis enumeration
- [x] `plan.md` Step 3 includes knowledge citation check with explicit N/A option
- [x] `conventions.md` §14 has 4 new anti-patterns (reviewer no-verify, executor §6-8 skip, researcher no-map, coordinator no-cite)
- [x] `PROJECT_CONFIG.yaml` has `tfw.review.default_mode: code`
- [x] All workflows stay under 1200 words (review.md = 849 words)
- [x] Mode files don't duplicate universal checklist items (universal #1-6 in review.md, mode-specific #7+ in mode files)

## 4. Verification

- Lint: N/A (markdown files, no linter configured)
- Tests: N/A (no automated tests for workflow files)
- Verify: Manual — all 10 acceptance criteria verified via file inspection:
  - review.md: ✅ (under 1200 words)
  - Mode files: 3 files exist with `min_verify_ratio` references ✅
  - handoff.md line 36: `KNOWLEDGE.md` present in inconsistency check ✅
  - handoff.md line 82: `Never omit §6-8` mandate present ✅
  - research/base.md line 91: Findings Map with N/A option ✅
  - plan.md line 36: Knowledge citation check with N/A option ✅
  - conventions.md lines 343-346: 4 new anti-patterns ✅
  - PROJECT_CONFIG.yaml: `default_mode: code` + `min_verify_ratio: 0.42` ✅
  - config.md: review section in Config Sync Registry ✅
  - Adapter sync: 5 adapter copies match canonical workflows ✅

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/workflows/review.md` | 103 | style | Step 7 references "REVIEW §6" for traces markers — if future template restructure changes §6 numbering, this will break. Consider using section name instead of number. |
| 2 | `.tfw/templates/REVIEW.md` | 6 | style | Header shows `Review Mode` field — this is new metadata not present in other templates. Consistent but potentially a convention drift point. |
| 3 | `.tfw/workflows/handoff.md` | 73 | naming | Step number jumps from 10 (build gate) to 12 (create RF file) — step 11 is missing. Pre-existing issue, not introduced by this change. |

## 6. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | philosophy | User values strict verification ratios over soft guidelines — "42% minimum" preferred over "2-3 files" because it scales with task size and is enforceable | User directive, TFW-38/A execution | High |

## 7. Strategic Insights (Execution)

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | Post-approval refinements (like min_verify_ratio) should follow the same Pattern A discipline as original TS items. User expects config-level changes even for "small fixes" — this prevents ad-hoc drift. | convention | User, TFW-38/A execution |

## 8. Diagrams

No diagrams.

---

*RF — TFW-38 / Phase A: Review Restructure + Full Enforcement Chain | 2026-04-14*
