# RF — TFW-21: Research Workflow Compression

> **Date**: 2026-04-03
> **Status**: 🟢 RF

---

## Changes

| # | File | Action | Description |
|---|------|--------|-------------|
| 1 | `.tfw/templates/RES.md` | Modified | Added 3 checkpoint fields (Agent assessment, Depth check, Recommendation) to all 3 stage checkpoints. Added external research line to Sufficiency Check self-check |
| 2 | `.tfw/workflows/research.md` | Rewritten | Compressed from 2397→1145 words, 319→160 lines |
| 3 | `.agent/workflows/tfw-research.md` | Synced | Exact copy of `.tfw/workflows/research.md` |
| 4 | `README.md` | Updated | Task Board: TFW-21 status → 🟢 RF |

## What Was Removed

| Section | Words removed | Reason |
|---------|--------------|--------|
| Example Flow (lines 199-243) | ~280 | Template RES.md + Hard Rules sufficient |
| "What good research looks like" (lines 259-264) | ~60 | Duplicates Hard Rules #1-#3 |
| "What bad research looks like" (lines 266-272) | ~60 | Duplicates Anti-patterns |
| "Operational" (lines 274-278) | ~40 | Repeats Role Lock |
| Anti-patterns duplicate block (lines 303-318) | ~150 | Merged into Rules § NEVER |
| Inline Checkpoint format (lines 131-144) | ~70 | Moved to templates/RES.md |
| Inline Sufficiency Check (lines 150-170) | ~100 | Already in templates/RES.md |

## What Was Preserved

- ✅ Research Mindset — full tone, compressed from 9→5 lines
- ✅ All 8 Hard Rules (MUST section)
- ✅ 3 stage mindset reminders ("> Remember: ...")
- ✅ Briefing Protocol with WAIT
- ✅ Closure Protocol (5 steps)
- ✅ Entry Modes, Prerequisites, Limits, Status Transitions

## Verification

```
Before: 2397 words, 319 lines
After:  1145 words, 160 lines (-52% words, -50% lines)

Hard Rules (MUST): 8 ✅
Stage reminders (Remember:): 3 ✅
Briefing mentions: 4 ✅
Closure mentions: 3 ✅
Stage definitions: 3 ✅
WAIT stops: 3 ✅
Adapter diff: identical ✅
```

## Observations (out-of-scope, not modified)

| # | File | Type | Description |
|---|------|------|-------------|
| 1 | `.tfw/workflows/plan.md` | duplication | Naming Rules table (lines 64-75) duplicates conventions.md §4 — ~100 words recoverable |
| 2 | `.tfw/workflows/handoff.md` | duplication | Anti-patterns section partially overlaps conventions.md §14 |

## Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | constraint | AI workflow instructions degrade at >~1200 words per document — agents lose mid-document attention. Working range: 700-900 words | TFW-21 analysis + external research | Medium |
| 2 | convention | Checkpoint behavioral fields (Agent assessment, Depth check, Recommendation) must live in templates/RES.md, not inline in workflow docs | TFW-21 RES R1 | High |

---

*RF — TFW-21: Research Workflow Compression | 2026-04-03*
