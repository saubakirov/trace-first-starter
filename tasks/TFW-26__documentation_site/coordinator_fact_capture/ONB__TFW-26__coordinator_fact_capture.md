# ONB — TFW-26: Coordinator Fact Capture & Session Discipline

> **Date**: 2026-04-05
> **Author**: Executor
> **Status**: 🟠 ONB — TS revised, re-read required
> **Parent HL**: [HL-TFW-26](../HL-TFW-26__documentation_site.md) §11 S9, S10, S12
> **TS**: [TS__TFW-26__coordinator_fact_capture](TS__TFW-26__coordinator_fact_capture.md)

---

## 1. Understanding

Add a Fact Candidates mechanism to the Coordinator role by: (1) adding §11 Strategic Session Insights to the HL template, (2) adding a mandatory Step 4b to plan.md for capturing insights during planning, (3) adding a reminder to resume.md for coordinators picking up work, (4) adding "Strategic Insight" to the glossary. This closes the gap where Coordinator is the only role without an explicit fact capture path.

## 2. Entry Points

| File | Current State |
|------|---------------|
| `.tfw/templates/HL.md` | Ends at §10 RESEARCH Case (line 105), footer at line 108 |
| `.tfw/workflows/plan.md` | Step 4 (Write HL) ends at line 47, GATE at line 48-49. Step 5 starts at line 51 |
| `.tfw/workflows/resume.md` | Phase 1 (Locate Task) starts at line 16, no fact capture mentions |
| `.tfw/glossary.md` | 179 lines, ends with empty "Project-Specific Terms" section |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions. TS is precise and self-contained. | — |

## 4. Recommendations (suggestions, not blocking)

1. **TS Step 2 references `knowledge/process.md F2` directly in the plan.md text.** This hardcodes a fact ID that may change during the next `/tfw-knowledge` consolidation. Recommend: keep the reference but note it's illustrative, not a stable link. The principle behind F2 ("user emotions are the primary signal") is what matters, not the fact ID. I'll include it as written in TS since the reference is valuable for context even if the ID drifts.

2. **TS Step 3 placement in resume.md is loosely specified** — "in the context loading or orient phase." I'll place it in Phase 1 (Locate Task) between step 3 (Read Master HL) and step 4 (Read Master TS), since that's where the coordinator first gains context about the task and would be primed to look for missed insights.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **plan.md word count** — Adding Step 4b (~100 words) to plan.md increases it from ~795 words. The workflow was compressed to ~795 in TFW-22. Adding ~100 words is modest (~13% increase) and justified given this is DNA-level behavior (fact capture = core workflow), not reference data.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS §4 Step 1 says "after §10 RESEARCH Case"** — confirmed, the template currently ends at §10. No inconsistency.
2. **TS says "Step 4 or new step" in §2 but specifies "Step 4b" in §4** — minor spec ambiguity, but §4 is authoritative. Will use Step 4b as specified.

## 7. TS Revision Notice (2026-04-05)

> **Lead Coordinator revised TS after ONB was written.** Changes:
>
> 1. **New Step 1 added:** Add `philosophy` category to conventions.md §10.1 Fact Categories table.
>    - Row to add after `risk`: `| philosophy | Values, principles, vision | design rationale, methodology beliefs, north star decisions |`
>    - Rationale: `philosophy` was the most-used category in TFW-26 (5/13 insights) but was missing from canonical list.
> 2. **Steps renumbered:** Old Step 1→2, Step 2→3, Step 3→4, Step 4→5.
> 3. **Category references changed:** HL template §11 and plan.md Step 4b now reference `conventions.md §10.1` instead of hardcoding `{philosophy/process/constraint/convention}`.
> 4. **New affected file:** `.tfw/conventions.md` added (MODIFY). Budget: 5 files (was 4).
> 5. **New acceptance criterion:** "No hardcoded category lists — all templates reference §10.1."
>
> **Action required:** Re-read TS Steps 1-5 before execution. No blocking questions expected — changes are additive.

---

*ONB — TFW-26: Coordinator Fact Capture & Session Discipline | 2026-04-05*
