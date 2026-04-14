# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: docs
> Min verify ratio: 0.42
> RF files claimed: 7
> Files to verify: ⌈7 × 0.42⌉ = 3 (verified all 7)

## Verification Log

### V1: `.tfw/templates/HL.md`
- **RF claim:** "Added §7.2 Knowledge Citations after §7.1 Quality Contract (lines 103-113). Table with PV Index scan instruction, 4-column format, bootstrap note."
- **Actual:** Lines 103-113 contain `### 7.2 Knowledge Citations` with blockquote instructions (PV Index scan, priority tiers 1-4 full scan / 5-7 skim, reviewer verification note), 4-column table (`#`, `Source`, `Item`, `How it applies`), and bootstrap note "No applicable knowledge items — project in bootstrap phase." Section positioned after §7.1 Quality Contract (L98-101), before §8 Dependencies (L115).
- **Match:** ✅

### V2: `.tfw/templates/ONB.md`
- **RF claim:** "Added §7 Knowledge Citations after §6 Inconsistencies (lines 32-43). Executor-facing table: 5-column format, NEW row support, bootstrap confirmation note."
- **Actual:** Lines 32-43 contain `## 7. Knowledge Citations` with blockquote instructions (read coordinator's citations, confirm read, state applied/N/A, add NEW items), 5-column table (`#`, `HL §7.2 ref`, `Read?`, `Applied / N/A`, `Notes`), example row with `{D-number or F-number from HL §7.2}` placeholder, and bootstrap note "No applicable knowledge items — confirmed." Cross-references footer at L45. Section positioned after §6 (L29-30), before footer.
- **Match:** ✅

### V3: `.tfw/templates/review/verify.md`
- **RF claim:** "Added Knowledge Citations Verified section (lines 33-42) between Discrepancies and Checkpoint. Updated Checkpoint: replaced old KNOWLEDGE.md bullet with expanded citation verification."
- **Actual:** Lines 33-42 contain `## Knowledge Citations Verified` with blockquote instructions (verify HL §7.2 / ONB §7, flag hallucinations), 5-column table, N/A note for empty HL §7.2. Positioned after `## Discrepancies Found` (L27-31), before `## Checkpoint` (L44). Checkpoint self-check at L50-52: old KNOWLEDGE.md bullet **preserved** at L50 (`KNOWLEDGE.md checked — contradictions with changes documented?`), new citation bullet **added** at L51-52 (`Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist)?` with `Total citations: {N}, verified: {M}, hallucinations: {H}`).
- **Match:** ⚠️ partial — RF decision #3 says "old KNOWLEDGE.md self-check was kept as a separate line" but TS Step 4 says "replace current KNOWLEDGE.md bullet." Executor chose preserve+extend over replace. **This is actually the better choice** — contradiction check and citation verification are independent concerns. The TS instruction was slightly ambiguous ("replace" could mean "update the area" vs "delete and substitute").

### V4: `.tfw/workflows/plan.md`
- **RF claim:** "Step 3 item 4: replaced 'Check KNOWLEDGE.md' with 'Scan Project Values (PV)' (lines 36-41). Full PV scan with priority tiers, targets HL §7.2, includes bootstrap note."
- **Actual:** Lines 36-41 contain item 4 of Step 3: `**Scan Project Values (PV)** — see glossary.md PV Index.` with sub-lines specifying full scan (README Values, philosophy.md, KNOWLEDGE.md §1, conventions.md §3/§11/§14), skim (convention.md, process.md, other topic files), output target (HL §7.2 Knowledge Citations table), and two N/A variants (general + bootstrap). Previous Phase A text fully replaced per coordinator answer Q1.
- **Match:** ✅

### V5: `.tfw/workflows/handoff.md`
- **RF claim:** "Phase 1 step 2: added citation-reading sub-bullet (lines 36-38) before KNOWLEDGE.md inconsistency check."
- **Actual:** Lines 36-38 under step 2 "Analyze the task" contain: `- Read HL §7.2 Knowledge Citations — verify each item, fill ONB §7.\n  For each citation: confirm read, state how applied or why N/A.\n  Add any NEW PV items you find relevant that coordinator missed.` Positioned before line 39 (`- Inconsistencies between HL/TS/KNOWLEDGE.md and actual code`). Multi-line continuation format with leading spaces — as noted in RF observation #2.
- **Match:** ✅

### V6: `.agent/workflows/tfw-plan.md`
- **RF claim:** "Adapter re-synced from `.tfw/workflows/plan.md`."
- **Actual:** Content is byte-identical to `.tfw/workflows/plan.md`. Lines 36-41 match exactly.
- **Match:** ✅

### V7: `.agent/workflows/tfw-handoff.md`
- **RF claim:** "Adapter re-synced from `.tfw/workflows/handoff.md`."
- **Actual:** Content is byte-identical to `.tfw/workflows/handoff.md`. Lines 36-38 match exactly.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | N/A — markdown files, no linter or test runner configured | No test runner |

> No commands could be run: pure markdown templates/workflows, no linter configured for .md files.

## Discrepancies Found

1. **V3 (verify.md checkpoint): TS says "replace" but executor preserved old bullet + added new one.** TS Step 4 exact text: "Update Checkpoint self-check — replace current KNOWLEDGE.md bullet." Executor kept the old KNOWLEDGE.md contradiction bullet (L50) and added the new citation verification bullet (L51-52) below it. The executor's RF decision #3 explicitly documents this choice with rationale: "contradictions and citations are different checks." The old check ("contradictions with changes documented?") is indeed a separate concern from citation link verification — this is a defensible improvement over the TS, not an omission. **Severity: Low (enhancement, not defect).**

> No escalation to 100% — the single discrepancy is a documented, minor enhancement that improves the template. All other files match exactly.

## Knowledge Citations Verified

> This is Phase B of TFW-38 — the task that *creates* Knowledge Citations. The ONB file (Phase B) has no §7 Knowledge Citations because the ONB template didn't have this section yet (it's being added by this phase). The HL for TFW-38 was written before Phase B added §7.2 to the HL template — so HL-TFW-38 doesn't have §7.2 either.

N/A — Knowledge Citation infrastructure is the deliverable of this phase. No prior citations to verify.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈7 × 0.42⌉ = 3 files and recorded findings? (opened all 7)
- [x] Ran at least 1 build/test command (or documented why not)? (documented: no test runner)
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented? (no contradictions)
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist)?
  - Total citations: 0 (N/A — this phase creates the citation infrastructure), verified: 0, hallucinations: 0

Stage complete: YES
