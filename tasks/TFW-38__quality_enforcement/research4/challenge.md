# Challenge — Iteration 4
> Parent: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> Goal: Stress-test citation and diagram mandates.

## C1: Knowledge Citation — What If KNOWLEDGE.md Doesn't Exist?

Many projects don't have KNOWLEDGE.md (it's optional per conventions.md §2). What happens if the coordinator tries to cite nonexistent knowledge?

**Answer:** plan.md Step 1 already says "KNOWLEDGE.md read." If the file doesn't exist, the context loading notes it's absent. The citation mandate says "If no KNOWLEDGE.md exists or nothing applies, write 'No applicable knowledge items.'"

Same pattern as RF §8 Diagrams: explicit N/A is better than silent skip. The agent documents that they checked and found nothing — that's a trace.

**Verdict:** No problem. Optional file + explicit N/A = clean behavior.

## C2: Knowledge Citation — Overhead for Simple Tasks

If every HL must include a "Relevant KNOWLEDGE.md items" check, does this add overhead for trivial tasks (e.g., "fix a typo in README")?

**Test:** Trivial tasks typically don't go through `/tfw-plan`. They're direct fixes. TFW only applies to tasks that deserve the full pipeline (HL → TS → ONB → RF → REVIEW).

For any task going through the full pipeline, reading KNOWLEDGE.md is already in Step 1. The citation mandate adds ~2 minutes of explicit verification. This is negligible compared to the HL writing time (~30-60 minutes).

**Verdict:** No significant overhead. The cost is a single paragraph in HL §4.

## C3: Diagram Mandate — Does "No Diagrams" Create Token Waste?

If the RF template requires §8 and the mandate says "write 'No diagrams' if none," then trivial phases always produce a "No diagrams" line.

**Token cost:** "No diagrams." = 3 tokens. Writing the section header + N/A line = ~10 tokens. Negligible.

**Value:** The explicit "No diagrams" tells the REVIEWER and docs.md workflow that the executor consciously decided no diagrams were needed. The reviewer can challenge this: "Phase D implemented a state machine — shouldn't there be a transition diagram?"

**Verdict:** Explicitly valuable. The reviewer's Judge stage can now check §8 as part of the "RF completeness" checklist item.

## C4: Diagram Mandate — What Counts as a Diagram?

The RF template says: "ASCII, mermaid, or structured tables." The research RES template says the same. But what's the minimum? A single-box ASCII diagram is useless.

**Proposed:** No minimum. The mandate is to THINK about whether a diagram would help. The output is either a useful diagram or a conscious "No diagrams." The reviewer judges whether the executor's choice was correct.

**This connects to the Judge stage (D11):** The reviewer in Judge stage applies the checklist. Item #10 is "RF completeness (§6-8)." If §8 says "No diagrams" for a phase that added 5 new services and a state machine — the reviewer writes ❌ with rationale.

**Verdict:** No minimum needed. The reviewer's judgment is the quality gate, not a word count.

## C5: Research Findings Map — Is It Always Useful?

Some research iterations are focused (single question, short answer). Does a Findings Map diagram make sense for a 2-page RES?

**Test:** Current RES__iter3 has a Findings Map with a nice ASCII diagram showing iteration relationships. RES__iter1 doesn't have one.

For short iterations, a Findings Map might be: "Question → Answer → Decision." That's still a trace — it shows the reasoning path.

**But:** Making Findings Map mandatory for ALL research iterations could feel forced for trivial ones.

**Compromise:** "Findings Map — visual diagram of validated findings. For single-question iterations, use a simple flow: Question → Evidence → Decision."

This gives a minimum format for simple cases and freedom for complex ones.

**Verdict:** Mandatory with a simple-case escape hatch.

## C6: Cross-Check — Are We Adding Too Many Mandates?

TFW-38 iteration 1-4 proposed changes summary:

| Change | Target Workflow | Added Words |
|--------|----------------|-------------|
| §6-8 explicit enumeration | handoff.md Phase 3 | ~30 |
| Staged review (Map → Verify → Judge → Decide) | review.md | ~150 |
| Review modes (code / docs / spec) | review.md + 3 mode files | ~300 total |
| KNOWLEDGE.md citation in HL | plan.md Step 3 | ~30 |
| KNOWLEDGE.md citation in ONB | handoff.md Phase 1 | ~10 |
| Diagram mandate in RF | handoff.md Phase 3 | ~20 |
| Findings Map mandate | research/base.md Step 6 | ~20 |
| Diagram indexing in docs.md | docs.md checklist | ~20 |

**Total added to existing workflows:** ~280 words across 4 files.
**New files:** 3 review mode files (~100 words each).

**Word budget check:**
- handoff.md: 5543 bytes → ~820 words. +60 → ~880. Under 1200.
- review.md: current ~816 words. +150 → ~966. Under 1200.
- plan.md: 7206 bytes → ~1100 words. +30 → ~1130. Under 1200 (tight).
- research/base.md: current length similar. +20 → safe.

**Verdict:** All changes fit within budget. plan.md is tightest at ~1130/1200.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Citation mandate works with optional KNOWLEDGE.md (C1) | None |
| Overhead negligible for pipeline tasks (C2) | None |
| "No diagrams" is explicitly valuable for reviewer (C3) | None |
| No minimum for diagrams — reviewer judges (C4) | None |
| Findings Map mandatory with simple-case format (C5) | None |
| All changes fit word budgets (C6) | None |

**Sufficiency:**
- [x] External source used? (iter 1 root cause, word budget from iter 2)
- [x] Briefing gap closed?

Stage complete: YES
→ Close Challenge, proceed to Synthesis.
