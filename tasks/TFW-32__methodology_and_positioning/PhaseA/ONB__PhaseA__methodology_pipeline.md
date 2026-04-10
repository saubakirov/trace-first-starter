# ONB — TFW-32 / Phase A: Methodology Pipeline Fixes

> **Date**: 2026-04-10
> **Author**: AI (Executor)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> **TS**: [TS Phase A](TS__PhaseA__methodology_pipeline.md)

---

## 1. Understanding

Fix the docs-vs-knowledge workflow collision by establishing exclusive write territories: tfw-docs owns KNOWLEDGE.md §1-§3 + TECH_DEBT.md (Combination), tfw-knowledge owns `knowledge/*.md` + KNOWLEDGE.md §4 (Externalization). Add `📚 KNW` status between REV and DONE in the pipeline. Remove orphaned §0 from KNOWLEDGE.md. Add `tfw-docs` and `tfw-knowledge` markers in the REVIEW template. Update review.md with a KNW transition step. 9 files modified, 0 new.

## 2. Entry Points

| File | Relevance |
|------|-----------|
| `.tfw/workflows/knowledge.md` | Phase 4 §1/§2 writes to strip (lines 85-88) + header Output (line 8) |
| `.tfw/workflows/docs.md` | Add Scope section + Orchestration note |
| `.tfw/workflows/review.md` | Add Step 7 KNW transition. Also: Step 5 verdict (line 89) says `✅ APPROVE → ✅ DONE` — needs intermediate KNW |
| `.tfw/templates/REVIEW.md` | §4 Traces Updated (line 51 has tfw-docs, need to add tfw-knowledge) |
| `.tfw/conventions.md` | §5 pipeline diagram (line 127) + status table (lines 136-146) |
| `.tfw/glossary.md` | Pipeline diagram (line 59) + status count (line 62) + new KNW definition |
| `.tfw/PROJECT_CONFIG.yaml` | `tfw.statuses` — insert KNW between REV and DONE (lines 93-94) |
| `KNOWLEDGE.md` | §0 (lines 8-20) to remove |
| `README.md` | Status legend (line 201) + Key Concepts pipeline (line 147) |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions | — |

## 4. Recommendations (suggestions, not blocking)

1. **review.md Step 5 verdict update**: The current Step 5 says `✅ APPROVE → update Task Board to ✅ DONE`. With KNW, after APPROVE the status should go to `📚 KNW`, then to `✅ DONE` after both markers are set. TS Step 7 adds the new Step 7 but doesn't explicitly mention updating Step 5's text. I will update both Step 5 and add Step 7 for consistency.

2. **KNOWLEDGE.md §0 removal — keep header comment**: After §0 removal, KNOWLEDGE.md will start with `## 1. Architecture Map`. The file header and intro paragraph above §0 should be preserved. I will remove only the §0 section (table + heading), keeping the file intro intact.

3. **conventions.md REVISE/REJECT flow**: Lines 130-133 show a REVISE/REJECT branch from REV. KNW sits between REV and DONE on the success path. The ASCII diagram needs careful editing to not break the branching visual.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **review.md inconsistency if Step 5 not updated**: If Step 5 still says `✅ APPROVE → ✅ DONE` but Step 7 says `KNW → DONE`, agents may skip Step 7 and go directly to DONE on APPROVE. Low risk — addressed by Recommendation #1.

2. **KNOWLEDGE.md horizontal rule**: There's a `---` between §0 and §1 (line 84 in KNOWLEDGE.md). After §0 removal, a stray `---` at the top may look odd. Will clean up accordingly.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS lists "9 modifications" (§3 Budget)** — count matches: knowledge.md, docs.md, review.md, REVIEW.md, conventions.md, glossary.md, PROJECT_CONFIG.yaml, KNOWLEDGE.md, README.md. Confirmed.

2. **TS Step 5d mentions "Key Concepts" line**: Line 147 in README.md currently reads `(RES optional)`. After update: `(RES, KNW optional)`. Confirmed target exists.

> **Cross-references**: HL-TFW-32 §4 Phase A, RES1 D1/D3/D6/D7/D8, Phase A HL §4

---

*ONB — TFW-32 / Phase A: Methodology Pipeline Fixes | 2026-04-10*
