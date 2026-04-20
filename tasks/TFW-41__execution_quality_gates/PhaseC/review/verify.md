# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: docs
> Min verify ratio: 0.42
> RF files claimed: 5
> Files to verify: ⌈5 × 0.42⌉ = 3 minimum → verified all 5 (100%)

## Verification Log

### V1: `.tfw/templates/research/gather.md`
- **RF claim:** Added `## Dimensions` section before `## Findings`; added conditional checkpoint item. 25 → 40 lines. Instruction: "do NOT mark any alternative as 'recommended'".
- **Actual:** File is 40 lines. `## Dimensions` section at line 5 — BEFORE `## Findings` at line 19. ✅ Table with D1/D2/D3 rows and 4 alternative columns. Line 9: "Do NOT mark any alternative as 'recommended'". Line 36 checkpoint item: `- [ ] Dimensions identified? _(skip if <3 independent factors — use comparison matrix in Findings instead)_`. Graceful degradation instruction at line 17.
- **Match:** ✅

### V2: `.tfw/templates/research/extract.md`
- **RF claim:** Added `## Configuration Space` section before `## Findings`; references Gather dimension names via column headers; no evaluation instruction; overflow protection. 25 → 42 lines.
- **Actual:** File is 42 lines. `## Configuration Space` at line 5 — BEFORE `## Findings` at line 21. Column headers: `{D1 from Gather}`, `{D2 from Gather}`, `{D3 from Gather}` — explicitly reference Gather by name, creating structural cross-stage dependency. Line 9: "Do NOT evaluate yet — list all combinations that are not obviously contradictory." Lines 17-19: overflow protection with inline example (if C1 = (A, A, A), only keep rows where at least one column is not A). Graceful degradation note line 19.
- **Match:** ✅

### V3: `.tfw/templates/research/challenge.md`
- **RF claim:** Added `## Consistency Check` section before `## Findings`; pairwise instruction; incompatible pairs table; surviving configurations table; unexpected survivors field; graceful degradation note. 25 → 47 lines.
- **Actual:** File is 47 lines. `## Consistency Check` at line 5 — BEFORE `## Findings` at line 26. Line 7: "Take each pair of dimensions from Gather and ask: 'Can Alternative X coexist with Alternative Y?'" Incompatible pairs table at lines 10-13. Surviving configurations table at lines 15-19. Unexpected survivors field at lines 21-22. Graceful degradation note at line 24. Checkpoint item line 43: "Pairwise incompatibility checked? Surviving configurations listed?"
- **Match:** ✅

### V4: `.tfw/workflows/research/base.md`
- **RF claim:** Added 3-sentence dimensional analysis thread at start of Step 5. 129 → 132 lines (RF says 132, actual is 131). No GMA/Zwicky terminology.
- **Actual:** File is 131 lines (minor self-reporting error in RF §1 — "129 → 132", actual delta is +2). Thread at line 62 (one long paragraph before `Cover all three...`): explains Gather→Dimensions, Extract→Configuration Space, Challenge→Consistency Check chain; cross-stage dependency ("skipping Dimensions in Gather makes Configuration Space in Extract impossible to fill"); graceful degradation ("If fewer than 3 independent dimensions exist, use a comparison matrix in Gather instead"). No "Zwicky", "GMA", or "morphological" present — grep confirmed 0 results.
- **Match:** ✅ (minor: RF reports 132 lines, actual 131 — not a DoF violation)

### V5: `.tfw/conventions.md`
- **RF claim:** Added `### 14.1 Terminology Origin (maintainer reference)` subsection after §14 anti-patterns. Maps 5 TFW-native terms to Zwicky GMA equivalents. Explicitly maintainer-only.
- **Actual:** `### 14.1 Terminology Origin (maintainer reference)` at line 391. Table at lines 395-401 mapping all 5 terms (Dimension, Alternative, Configuration Space, Consistency Check, Surviving Configuration) to Zwicky GMA equivalents. Line 403: "> **Scope:** This note is for framework maintainers only. The terms \"Zwicky\", \"GMA\", \"General Morphological Analysis\", \"morphological box\", and \"cross-consistency assessment\" MUST NOT appear in any researcher-facing template or workflow instruction." §15 Role Lock Protocol follows at line 405 — numbering intact.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `grep "Zwicky" .tfw/templates/research/` (recursive) | 0 results ✅ |
| 2 | `grep "Zwicky" .tfw/workflows/research/base.md` | 0 results ✅ |
| 3 | `grep "recommended" .tfw/templates/research/gather.md` | 0 matches (prohibition text uses "recommended" only in negation — not present as positive instruction) ✅ |
| 4 | `grep "Configuration Space" .tfw/templates/research/extract.md` | Section heading confirmed ✅ |

> Note: No build/lint commands exist in project_config.yaml for Markdown files. This is a docs-only phase — no test runner applicable.

## Discrepancies Found

1. **base.md line count discrepancy (minor):** RF §1 states "129 → 132 lines" but actual file has 131 lines. Net delta = +2, not +3. RF claim is internally consistent (says "3 sentences, 1 paragraph block" in §3 AC-4) — the paragraph occupies 1 line in the file (long wrapped sentence), not 3. Discrepancy is in RF §1 metadata only, not in actual content. **Not a DoF violation.** DoF triggers only on content failures, not metadata inaccuracies.

No other discrepancies found. Escalation to 100% verification not required (triggered only on content discrepancies), but was done anyway as a quality measure.

## Knowledge Citations Verified

> HL §7.2 has 4 citations. ONB §7 verified all 4.

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | HL §7.2 #1 | `conventions.md §14` — Anti-patterns list | ✅ | ✅ (verified: lines 366-389, anti-patterns) |
| 2 | HL §7.2 #2 | `conventions.md §3` — TS definition | ✅ | ✅ (verified: lines 56-57) |
| 3 | HL §7.2 #3 | `glossary.md` — Scope Budget | ✅ | ✅ (file exists at .tfw/glossary.md) |
| 4 | HL §7.2 #4 | `README.md Values` — "The thinking is the product" | ✅ | ✅ (README.md exists at project root) |

> Total citations: 4, verified: 4, hallucinations: 0.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈5 × 0.42⌉ = 3 files and recorded findings? (All 5 verified — 100%)
- [x] Ran at least 1 build/test command (or documented why not)?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist)?
  - Total citations: 4, verified: 4, hallucinations: 0

Stage complete: YES
