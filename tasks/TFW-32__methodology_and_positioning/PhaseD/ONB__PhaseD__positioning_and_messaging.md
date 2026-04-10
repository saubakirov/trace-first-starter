# ONB — TFW-32 / Phase D: Positioning & Messaging

> **Date**: 2026-04-10
> **Author**: AI (Executor)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> **TS**: [TS Phase D](TS__PhaseD__positioning_and_messaging.md)

---

## 1. Understanding

Phase D is an analytical phase that produces 4 positioning spec documents — no code changes, no modifications to TFW core files. The deliverables are: (1) audience persona matrix with 3-tier hierarchy and pain points, (2) positioning spec with value proposition paragraph + README section-by-section improvement direction + competitive frame, (3) translation table mapping ≥15 TFW terms to business equivalents, (4) .tfw/README.md philosophy paper improvement spec. All reference research decisions D5, D9, strategic insights S1-S17, and VLM-3 RES3 competitive analysis. The specs will be used by a future task (TFW-33+) to actually rewrite the READMEs.

## 2. Entry Points

| File | Purpose |
|------|---------|
| `TS__PhaseD__positioning_and_messaging.md` | Detailed steps with pre-written content for all 4 deliverables |
| `../HL-TFW-32__methodology_and_positioning.md` §2.6, §3.2, §11 | Current README gaps analysis, value flow diagrams, strategic insights S1-S17 |
| `../RES__TFW-32__methodology_and_positioning.md` D5, D9 | Team knowledge methodology positioning + audience hierarchy |
| `../research/gather.md` G2 | Shape Up / DORA / Scrum Guide positioning patterns |
| `../research/briefing.md` User Direction Q3 | "Product people learn TFW faster" |
| `README.md` (project root) | Current README — what to improve |
| `.tfw/README.md` | Current philosophy paper — what to improve |
| VLM-3 RES3 D19-D20 | Knowledge Pipeline confirmed unique + thinking traces novel |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions. | — |

The TS is self-contained: it pre-specifies content for all 4 deliverables with inline citations and concrete before/after direction. All source decisions (D5, D9) and strategic insights (S1-S17) are already embedded in the TS text. I can proceed with execution immediately.

## 4. Recommendations (suggestions, not blocking)

1. **VLM-3 RES3 is in Russian.** The TS references D19-D20 from VLM-3 RES3 for the 8 unique features list. The RES3 content is written in Russian. Per `tfw.content_language: en`, I'll translate relevant content into English for the positioning spec. The actual unique features are clear from the decision rationale regardless of language.

2. **TS Step 2 has extensive pre-written content.** The TS essentially pre-writes much of the positioning spec (Section A value proposition structure, Section B table, Section C competitive frame with 8 features). I recommend following this closely rather than re-inventing — the coordinator invested significant research into these formulations.

3. **Qualifying questions are a strong differentiator.** The TS includes specific qualifying questions per tier ("How much of your team's knowledge would survive if your top 3 people left tomorrow?"). These are unusually sharp for methodology positioning and should be preserved exactly.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Current README already reflects some Phase A changes.** README.md line 147 shows the updated pipeline with `📚 KNW` status and line 201 shows the status legend. The positioning spec should reference the current (post-Phase A) README, not the pre-Phase A version described in HL §2.6. This affects the "before/after" analysis for the "Key Concepts" section.

2. **FAQ section partially stale.** The TS Step 2 Section B proposes adding FAQ questions, but the current README FAQ section (lines 76-86) already has 3 questions. The spec should be precise about whether to ADD to them or REPLACE.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS §4 Step 2 Section B "Key Concepts" row says "Update if pipeline changed (already done by Phase A)."** Confirmed: README line 147 already shows `📚 KNW` in the pipeline. The positioning spec should note this as "already current" rather than proposing a change.

> **Cross-references**: D5 (RES1), D9 (RES1), S1-S17 (HL §11), D19-D20 (VLM-3 RES3), G2 (gather.md)

---

*ONB — TFW-32 / Phase D: Positioning & Messaging | 2026-04-10*
