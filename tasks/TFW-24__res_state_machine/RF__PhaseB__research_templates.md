# RF — TFW-24 / Phase B: Research Stage Templates

> **Date**: 2026-04-04
> **Author**: Executor
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-24](HL-TFW-24__res_state_machine.md)
> **TS**: [TS Phase B](TS__PhaseB__research_templates.md)

---

## 1. What Was Done

### New Files
| File | Description |
|------|------------|
| `.tfw/templates/research/briefing.md` | Briefing template: Research Plan, Hypotheses, Scope Intent, Guiding Questions, User Direction |
| `.tfw/templates/research/gather.md` | Gather stage: "What do we NOT know?" — Findings, Checkpoint, Sufficiency |
| `.tfw/templates/research/extract.md` | Extract stage: "What do we NOT see?" — Findings, Checkpoint, Sufficiency |
| `.tfw/templates/research/challenge.md` | Challenge stage: "What do we NOT expect?" — Findings, Checkpoint, Sufficiency |

### Modified Files
| File | Changes |
|------|---------| 
| `.tfw/workflows/research/base.md` | Step 3: `templates/research/` ref. Step 4: `templates/research/briefing.md` ref. Step 5: template ref |
| `.tfw/conventions.md` | §4: replaced 18-line inline format block with 1-line template reference |
| `.agent/workflows/tfw-research.md` | Synced from base.md |

## 2. Key Decisions

1. **Step 5 wording compressed.** TS specified "Each stage uses its template from `templates/research/` and writes to `research/`" — this pushed base.md to 604 words. Trimmed to "Each stage uses its template (`templates/research/`)" — 599 words. "writes to `research/`" is implied by the template ref and Step 3's subfolder creation.

## 3. Acceptance Criteria

- [x] 4 template files exist in `.tfw/templates/research/`
- [x] Each stage template has: Parent HL link, Goal from §1 Vision, Findings section, Checkpoint with `Stage complete: YES / NO`
- [x] Each stage template has its guiding question as subtitle (D28): Gather = "What do we NOT know?", Extract = "What do we NOT see?", Challenge = "What do we NOT expect?"
- [x] Briefing template includes: Research Plan, Hypotheses table, Scope Intent, Guiding Questions, User Direction
- [x] Gather/Extract/Challenge templates include Sufficiency checklist (external source + briefing gap)
- [x] `base.md` Step 3 references `templates/research/`
- [x] `base.md` Step 4 references `templates/research/briefing.md`
- [x] `base.md` Step 5 references `templates/research/` for stage files
- [x] `conventions.md` §4 references templates instead of inline format
- [x] Adapter synced (diff = 0)

## 4. Verification

- Lint: N/A (markdown-only project)
- Tests: N/A
- Verify: Passed
- `wc -w base.md`: **599 words** ✅ (under 600 budget)
- `diff base.md adapter`: **0 differences** ✅
- Template count: **4 files** in `.tfw/templates/research/` ✅

### Deviation from TS

| # | TS spec | Actual | Reason |
|---|---------|--------|--------|
| 1 | Step 5: "...and writes to `research/`" | "Each stage uses its template (`templates/research/`)" | Word count: TS wording = 604 words (over budget). Trimmed redundant clause — writing target implied by Step 3 subfolder creation |

## 5. Observations (out-of-scope, not modified)

No observations.

## 6. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | convention | Research stage templates live in `.tfw/templates/research/` (briefing, gather, extract, challenge). These are starting points, not contracts — Findings section is free-form. Canonical format for Goal anchoring and Checkpoint consistency | TS Phase B, this RF | High |

---

*RF — TFW-24 / Phase B: Research Stage Templates | 2026-04-04*
