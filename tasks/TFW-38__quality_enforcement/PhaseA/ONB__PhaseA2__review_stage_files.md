# ONB — TFW-38 / Phase A.2: Review Stage Files + Self-Check Gates

> **Date**: 2026-04-14
> **Author**: Executor
> **Status**: 🟠 ONB — Answered
> **Parent HL**: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> **TS**: [TS Phase A.2](TS__PhaseA2__review_stage_files.md)

---

## 1. Understanding

Convert review stages (Map/Verify/Judge) from inline sections in review.md into file-based traces with self-check gates, paralleling the research stage file model. The reviewer now creates a `review/` subfolder in the task phase directory and writes 3 stage files before synthesizing into the REVIEW artifact. REVIEW becomes a synthesis document (like RES for research). Additionally: Step 0 mode selection hardened with 🛑 WAIT gate (parallels research Step 2), and each stage template has identity-based mindsets as mandatory header fields (Identity + Rule + Test Question). 3 new template files, 3 modifications.

## 2. Entry Points

| File | Role |
|------|------|
| `.tfw/templates/review/` (new) | 3 stage templates: map.md, verify.md, judge.md |
| `.tfw/workflows/review.md` (136 lines) | Steps 0-4 rewrite: Step 0 mode gate + WAIT, Steps 1-3 file-based stages, Step 4 synthesis |
| `.tfw/templates/REVIEW.md` (90 lines) | Add stage files reference in header |
| `.tfw/conventions.md` (387 lines) | §3 — add review stage files to artifact taxonomy |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions. TS provides exact template content for all 3 stage files. | — |

## 4. Recommendations (suggestions, not blocking)

1. **Role Lock update.** Current review.md line 12 says "Permitted artifacts: REVIEW file only." With stage files, this should become "Permitted artifacts: review stage files (map.md, verify.md, judge.md) + REVIEW file." Otherwise an agent interpreting role lock strictly will refuse to write stage files.
   **→ Coordinator: Approved. Do it.**

2. **REVIEW.md §2 Verify table.** TS Step 5 says "§2 Verify references verify.md findings." Current REVIEW template §2 is a standalone table. I'll add a note pointing to verify.md for raw evidence, but keep the summary table for the synthesis artifact.
   **→ Coordinator: Agreed. Summary table + link to raw evidence.**

3. **Conventions §3 placement.** The review stage files entry should go right after the Research subfolder section (line 136) since it parallels that structure. Will insert after the multi-iteration research block.
   **→ Coordinator: Correct placement.**

## 5. Risks Found (edge cases, potential issues not in TS)

1. **review.md word count.** Current: 136 lines. Steps 1-4 rewrite adds stage file creation instructions (richer than current inline summaries). Review.md might exceed the original 1200 word limit from A.1. Will monitor and report in RF.

2. **Anti-pattern update.** Current anti-pattern "Reviewer approves without opening any files" (line 134) should be updated to reference stage files — the new enforcement is that verify.md must exist with verification log entries. Current anti-pattern still works but is weaker than it could be.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS Step 4 says "Replace Steps 0-4."** TS was updated post-ONB to include Step 0 mode gate rewrite with 🛑 WAIT. Current review.md Step 0 (lines 30-39) will be replaced with hardened version. Steps 5-7 untouched. Confirmed.

2. **TS Step 4 preserves Steps 5-7.** Current Steps 5-7 (Tech Debt Collection, Update Traces, Knowledge Capture) remain untouched — TS only modifies Steps 0-4. Confirmed.

3. **TS Step 2 verify.md self-check includes "KNOWLEDGE.md checked."** This is a new check not in Phase A.1 — it extends the KNOWLEDGE.md enforcement chain established in plan.md and handoff.md. Consistent.

4. **TS updated post-ONB with 3 items:** (a) 🛑 WAIT gate in Step 0 with "Switch? [code/docs/spec]" — parallels research Step 2; (b) Identity-based mindsets in each stage template header (Student / Auditor / Judge / Decision-maker) with Test Questions; (c) Mindset as mandatory header field, not just workflow blockquote. These are ADDITIONS to scope, not contradictions with existing ONB analysis.

5. **TS updated post-ONB with 2 more items (knowledge/values cross-check):** (d) Overall Reviewer Identity statement before Step 0 — "Quality guardian. Trust evidence, not declarations." Parallels research base.md "Critical thinking partner" (D21 pattern). (e) Trust Protocol for Review — 7-row table mapping RF claim types to trust levels (Verify/Challenge/Trust) and reviewer actions. Parallels research Trust Protocol (D27 pattern). Both items from systematic cross-check against `knowledge/philosophy.md` (F3: critical opponent), `knowledge/convention.md` (F14: template instruction blocks), and `KNOWLEDGE.md` Architecture Decisions (D21, D27).

---

*ONB — TFW-38 / Phase A.2: Review Stage Files + Self-Check Gates | 2026-04-14*
