# RF — TFW-32 / Phase B: Naming & Templates

> **Date**: 2026-04-10
> **Author**: AI (Executor)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> **TS**: [TS Phase B](TS__PhaseB__naming_and_templates.md)

---

## 1. What Was Done

### New Files
| File | Description |
|------|------------|
| `tasks/TFW-32__methodology_and_positioning/PhaseB/ONB__PhaseB__naming_and_templates.md` | Executor onboarding report |

### Modified Files
| File | Changes |
|------|---------| 
| `.tfw/templates/HL.md` | §3.1 enhanced with Working Backwards framing. §3.2 Value Flow added. §11 renamed to "Strategic Insights (Planning)" with cognitive mode instructions |
| `.tfw/templates/RF.md` | §6 sharpened with cognitive mode + scope. §7 "Strategic Insights (Execution)" added. §8 "Diagrams" added |
| `.tfw/templates/RES.md` | Fact Candidates sharpened with cognitive mode. "Strategic Insights (Research)" section added. "Findings Map" section added |
| `.tfw/templates/REVIEW.md` | §5 Fact Candidates sharpened with cognitive mode, reviewer-specific scope, exclusion of analysis/opinions |
| `.tfw/conventions.md` | "Visual Sections (per-template)" cross-reference table added. "Knowledge Capture Sections (unified naming)" table added. Fact Candidates definition updated with cognitive mode |
| `.tfw/glossary.md` | "Strategic Insight" definition updated with qualifiers/contrast. "Value Flow", "Findings Map", "Per-template Naming" terms added |

## 2. Key Decisions

1. Followed TS exactly — no deviations from specified before/after content blocks.
2. Section numbering in RF: §7 Strategic Insights (Execution) + §8 Diagrams placed before footer `---`, maintaining clean sequential numbering.
3. RES sections (Strategic Insights, Findings Map) use heading-only naming without section numbers — consistent with RES being a synthesis document, not a phase report.

## 3. Acceptance Criteria

- [x] HL §11 heading reads "Strategic Insights (Planning)" — not "Strategic Session Insights"
- [x] HL §11 instructions include "Cognitive mode: Deep analytical synthesis" and cross-reference to §6
- [x] HL §3.1 instructions include "Working Backwards" framing and "This is NOT a process diagram" note
- [x] HL has §3.2 "Value Flow" with strategic visualization instructions
- [x] RF has §7 "Strategic Insights (Execution)" with Human-Only Test and "No strategic insights" fallback
- [x] RF has §8 "Diagrams" with technical visualization instructions
- [x] RF §6 instructions include "Cognitive mode: Pure reporting" and explicit out-of-scope list
- [x] RES has "Strategic Insights (Research)" section with Human-Only Test
- [x] RES has "Findings Map" section with analytical visualization instructions
- [x] RES Fact Candidates instructions sharpened to match RF level (cognitive mode + scope + before-writing note)
- [x] REVIEW §5 instructions include "Cognitive mode: Pure reporting" and reviewer-specific scope
- [x] conventions.md has "Visual Sections (per-template)" table with all 5 template rows
- [x] conventions.md has "Knowledge Capture Sections (unified naming)" table
- [x] conventions.md "Fact Candidates" definition includes "Cognitive mode: pure reporting"
- [x] glossary.md "Strategic Insight" definition updated with qualifiers and contrast to Fact Candidate
- [x] glossary.md has "Value Flow", "Findings Map", "Per-template Naming" entries

## 4. Verification

- Tests (`pytest docs/scripts/test_gen_docs.py`): 55/55 passed
- Manual verification: all 6 files inspected after changes — content matches TS spec

## 5. Observations (out-of-scope, not modified)

No observations.

## 6. Fact Candidates

> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.
>
> **Scope:** Agent-observed project patterns discovered during execution.
>
> **Before writing:** review the conversation history. The human's messages are the primary source.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | convention | All 4 template modifications (HL, RF, RES, REVIEW) required exactly the same pattern: add "Cognitive mode" as first instruction line, then scope, then Human-Only Test. This pattern could become a template-writing convention | TS Phase B Steps 1-6 | Medium |

## 7. Strategic Insights (Execution)

No strategic insights. No human interaction during execution — TS was fully specified.

## 8. Diagrams

No diagrams.

---

*RF — TFW-32 / Phase B: Naming & Templates | 2026-04-10*
