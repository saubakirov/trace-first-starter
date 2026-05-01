# ONB — TFW-43: Research Stage Protocol

> **Date**: 2026-05-01
> **Author**: Executor (Antigravity)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-43](HL-TFW-43__research_stage_protocol.md)
> **TS**: [TS-TFW-43](TS-TFW-43__research_stage_protocol.md)

---

## 1. Understanding

Add per-stage Mindset blocks (Strategist/Explorer/Analyst/Critic) + Test questions to 4 research templates, add h1 guiding question to Briefing, restructure `base.md` to copy-on-enter (one template at a time as each stage begins) with 🛑 STOP after each stage checkpoint. This restores D31 (file existence = stage completion) broken by TFW-42's batch-copy, and mirrors the proven review stage protocol (D41).

## 2. Entry Points

| # | File | Role |
|---|------|------|
| 1 | `.tfw/templates/research/1_briefing.md` | Template — add h1 question + Mindset block |
| 2 | `.tfw/templates/research/2_gather.md` | Template — add Mindset block |
| 3 | `.tfw/templates/research/3_extract.md` | Template — add Mindset block |
| 4 | `.tfw/templates/research/4_challenge.md` | Template — add Mindset block |
| 5 | `.tfw/workflows/research/base.md` | Workflow — restructure Steps 3/4/5 |
| 6 | `.agent/workflows/tfw-research.md` | Adapter — byte-copy of base.md |
| 7 | `.claude/commands/tfw-research.md` | Adapter — byte-copy of base.md |
| 8 | `.tfw/VERSION` | Version bump 0.8.6 → 0.8.7 |
| 9 | `.tfw/project_config.yaml` | Version bump |
| 10 | `.tfw/CHANGELOG.md` | New entry |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions | — |

## 4. Recommendations (suggestions, not blocking)

1. **TS §2 file count discrepancy**: TS lists 10 files in §2 Scope but HL §6 planned 8. The delta is correct — TS added `project_config.yaml` and `CHANGELOG.md` which HL counted under "version files = needs budget override". No action needed, just noting the trace.

2. **TS filename format**: TS filename is `TS-TFW-43__...` (single separator) while conventions §4 shows `TS__{PREFIX}-{N}__{title}.md` (double underscore between artifact type and prefix). This is a pre-existing naming choice by the coordinator — not modifying per Role Lock.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Step 5 OODA Stage Loop subsection** — currently the OODA Stage Loop (L66-76) and Stage Checkpoint (L78-83) sit as subsections of Step 5. After restructuring Step 5 with a FOR EACH loop, these subsections need to remain referenceable from inside the loop. TS AC-4 says "OODA Stage Loop section stays as subsection referenced from inside" — this is clear. Risk is minimal.

2. **Step 3 iteration 2+ text** — AC-2 says "Iteration 2+ predecessor reference instructions stay in Step 3." Currently Step 3 lines 46-49 have the iteration 2+ briefing predecessor reference. This content mentions Briefing but is about predecessor context loading, not about template copying. It will stay in Step 3 as specified.

3. **Step 4 already references `1_briefing.md`** — Current Step 4 (L51-58) already says "Write Briefing to current iteration's subfolder (`research/iterN/1_briefing.md`) using `templates/research/1_briefing.md`". AC-3 requires adding an explicit **copy** instruction before writing. The existing "using" phrasing is implicit — needs to become an explicit "copy template, then fill."

## 6. Inconsistencies with Code (spec vs reality)

1. **No inconsistencies found.** All files match what TS describes. Templates currently lack Mindset blocks (confirmed). `base.md` Step 3 currently batch-copies all 4 templates (confirmed at L44). Review template `map.md` confirms the Mindset format pattern (L2-3).

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | KC1: philosophy F4 (structural enforcement) | ✅ | Applied — copy-on-enter is the structural mechanism | |
| 2 | KC2: philosophy F18 (different templates = different modes) | ✅ | Applied — each stage template gets a distinct Mindset | |
| 3 | KC3: philosophy F20 (investigative workflows need forced transitions) | ✅ | Applied — STOP gates + mindset blocks = forced transitions | |
| 4 | KC4: philosophy F24 (instructions→compliance, heuristics→competence) | ✅ | Applied — Mindset = heuristic, copy-on-enter = structural dependency | |
| 5 | KC5: process F4 (agents follow steps+gates, lose focus in prose) | ✅ | Applied — Step 5 restructure to explicit per-stage protocol | |
| 6 | KC6: D31 (filesystem state machine) | ✅ | Applied — core motivation for copy-on-enter | |
| 7 | KC7: D41 (4-stage review flow) | ✅ | Applied — source pattern for Mindset blocks | Verified review template map.md format |
| 8 | KC8: stakeholder F2 (file naming = execution order) | ✅ | Applied — file existence = completion status extension | |

> No NEW items found beyond coordinator's citations.

> **Cross-references**: use Reference Format (e.g. `RF TFW-18`, `D24`, `TD-72`). See compilable_contract.md §2. Build script resolves to hyperlinks.

---

*ONB — TFW-43: Research Stage Protocol | 2026-05-01*
