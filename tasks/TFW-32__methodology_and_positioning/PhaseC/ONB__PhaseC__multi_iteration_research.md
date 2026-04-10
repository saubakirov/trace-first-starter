# ONB — TFW-32 / Phase C: Multi-Iteration Research Formalization

> **Date**: 2026-04-10
> **Author**: AI (Executor)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> **TS**: [TS Phase C](TS__PhaseC__multi_iteration_research.md)

---

## 1. Understanding

Formalize the multi-iteration research pattern — proven across 8 real iterations (TFW-32×4, VLM-3×4) — into structural enforcement. The changes span 6 files: add `min_iterations` config, update conventions.md with `researchN/` folder naming and `iterations.yaml` format, update the research workflow (`base.md`) with iteration detection/resume/naming, add the coordinator iteration gate to `plan.md` Step 6, insert an Iteration Status block into the RES template, and add glossary terms.

## 2. Entry Points

| File | Current lines | Relevant section |
|------|--------------|-----------------|
| `.tfw/PROJECT_CONFIG.yaml` | L43-56 | `tfw.research` section — insert after `max_passes: 3` (L47) |
| `.tfw/conventions.md` | L121-123 | §4 "Research subfolder" — replace with expanded version |
| `.tfw/workflows/research/base.md` | L12-16 (Step 0), L30-32 (Step 3), L66-73 (Step 6), L97-107 (Limits) | 4 separate modification points |
| `.tfw/workflows/plan.md` | L65-75 | Step 6: RESEARCH decision — replace with 3 sub-steps |
| `.tfw/templates/RES.md` | L83-85 | Before `## Conclusion` — insert Iteration Status block |
| `.tfw/glossary.md` | L109-111 | After "Pass (Research)" — insert 3 new terms |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | TS Step 2 says to replace lines 121-123 of conventions.md, but the "After" block ends with a stray triple-backtick (line 109 in TS: ` ``` `). Should I omit this trailing backtick (i.e., the `iterations.yaml` YAML block is part of the markdown content, not fenced code)? The YAML example is already inside a fenced code block on lines 90-106. The trailing backtick on line 109 appears to be a TS formatting artifact. | **A (Coordinator):** Correct — the trailing triple-backtick on TS line 109 is a TS formatting artifact. It closes the outer "After:" fenced block in the TS document. The actual content to insert into conventions.md ends with the paragraph `Coordinator updates iterations.yaml after each iteration...`. The YAML example inside that content is its own fenced code block within the markdown being inserted. Omit the trailing backtick. |

## 4. Recommendations (suggestions, not blocking)

1. **TS Step 3c references line 66-73 for Step 6 Synthesis but actual current content is at lines 66-73.** Verified — line numbers match. No issue.

2. **TS Step 3d says "after line 106" for adding `min_iterations` to the Limits table.** Current file has exactly 107 lines. The last content line is L107: `| Max passes | 3 | Soft | `max_passes` |`. The new row goes after this. Verified — correct.

3. **Backwards compatibility is well-handled.** All changes are additive. If no `iterations.yaml` exists, Step 0 falls back to standard single-iteration flow. Good design.

4. **Consider adding `iterations.yaml` to the conventions.md §4 naming table** (the one at lines 103-115 with artifact naming). Currently only the multi-iteration subsection documents it, but the main naming table doesn't list it. Non-blocking — can be noted in RF observations.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **plan.md Step 6 replacement is substantial (11 lines → 40 lines).** The resulting plan.md will grow from 108 to ~137 lines. Within attention budget but worth noting — plan.md is already the longest workflow.

2. **TS Step 5 says "insert before line 84, before `## Conclusion`"**, but the current RES template has `## Conclusion` at line 84. The Iteration Status block is 24 lines. This pushes Conclusion to line ~108. No issue — RES is a template, not a workflow.

3. **Step 6c iteration gate references "update HL after each iteration"** — this assumes the coordinator re-enters `plan.md` Step 6c after each `/tfw-research` completes. The flow is: researcher finishes → returns to coordinator → coordinator reads Step 6c → decides. This is implicit in the workflow but not explicitly stated in plan.md. The TS content handles this via "after each research iteration returns." Acceptable.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS says plan.md Step 6 is at lines 65-75.** Actual: lines 65-75 contain Step 6 and the post-RESEARCH line. Verified — matches.

2. **TS says research/base.md Step 0 is at lines 12-16.** Actual lines 12-16:
   ```
   12: ## Step 0: Resume
   13: (blank)
   14: IF resuming (not fresh start): re-read this workflow + mode file.
   15: Check task folder: `research/` exists? → which stage files exist? → `RES__*` exists?
   16: Resume from first missing stage. If RES exists → research complete.
   ```
   Matches TS "Before" block.

3. **TS says research/base.md Step 3 is at lines 30-32.** Actual:
   ```
   30: ## Step 3: Create Research Subfolder
   31: (blank)
   32: Create `research/` subfolder in task directory. Copy templates from `templates/research/`. Fill Goal from HL §1 Vision.
   ```
   Matches.

4. **TS says research/base.md Step 6 Synthesis is at lines 66-73.** Actual:
   ```
   66: ## Step 6: Synthesis
   67: (blank)
   68: 1. Read all stage files (briefing, gather, extract, challenge)
   69: 2. Write final `RES__*.md` using `templates/RES.md` — synthesize, don't copy-paste
   70: 3. HL Update Recommendations (table)
   71: 4. Fact Candidates — review conversation history first
   72: 5. Conclusion (1 paragraph)
   73: 6. **STOP.** "Research complete. Continue with `/tfw-plan` to update HL and write TS."
   ```
   Matches.

5. **TS says Limits table `Max passes` row is the last line.** Actual line 106: `| Max passes | 3 | Soft | `max_passes` |`. Line 107 is empty. Matches.

All line references verified. No inconsistencies found.

> **Cross-references**: HL-TFW-32 §4 Phase C, D4, D14, D18, D19. HL Phase C §5 Key Research Decisions. Phase A REVIEW. Phase B REVIEW.

---

*ONB — TFW-32 / Phase C: Multi-Iteration Research Formalization | 2026-04-10*
