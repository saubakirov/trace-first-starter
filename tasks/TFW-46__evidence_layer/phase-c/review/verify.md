# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: docs
> Min verify ratio: 0.42
> RF files claimed: 10
> Files to verify: ⌈10 × 0.42⌉ = 5

## Verification Log

### V1: `.tfw/glossary.md`
- **RF claim:** New `## Evidence Terms` section with 5 entries (Evidence, Evidence Plan, Evidence Collection, Evidence Audit, Evidence Status Vocabulary). Fixed TD-2: `RF §7` → `RF §8` in Strategic Insight entry.
- **Actual:** Lines 59-80 contain `## Evidence Terms` heading with 5 entries, all domain-agnostic (no screenshots, browser, curl). Line 48 reads `RF §8 "Strategic Insights (Execution)"` — TD-2 confirmed fixed. Cross-references to conventions.md §3 present.
- **Match:** ✅

### V2: `.tfw/VERSION`
- **RF claim:** Contains `0.8.8`
- **Actual:** Line 1 = `0.8.8`. Single-line file.
- **Match:** ✅

### V3: `.tfw/CHANGELOG.md`
- **RF claim:** New `[0.8.8] — 2026-07-07` entry with Added (9 items) and Changed (3 items). [Unreleased] section remains above.
- **Actual:** Lines 6-22. `## [Unreleased]` at L6 (empty). `## [0.8.8] — 2026-07-07` at L8. `### Added` with 9 items (L9-18). `### Changed` with 3 items (L19-22). All reference TFW-46 and phase identifiers.
- **Match:** ✅

### V4: Adapter sync (handoff — canonical vs .agent vs .claude)
- **RF claim:** All 6 pairs byte-identical via SHA256
- **Actual:** SHA256 hash comparison executed:
  - `handoff.md`: canonical = `.agent` = `.claude` = `8BA929E90DEEF7E92BFB6BF5114CC8A455889B327F93E03F33D1CF1A8A9F2EB8` ✅
  - `review.md`: canonical = `.agent` = `.claude` = `DE410ADBB012A2E48AEAD204CBBEEF79E4014522893C9C1FE58986833E5BB633` ✅
  - `plan.md`: canonical = `.agent` = `.claude` = `2C44DF5E1C32F4B03FB1624B6454D75F4C802F8EAAF3830AB51C365C84ABB250` ✅
- **Match:** ✅

### V5: Document structure check (glossary.md)
- **RF claim:** Terms follow established glossary pattern, no domain-specific examples, cross-references present
- **Actual:** Each entry follows h3 heading + 2-3 line definition pattern. Evidence Plan references `templates/TS.md` §5. Evidence Collection references `handoff.md` Step 11. Evidence Audit references `templates/review/verify.md`, `templates/review/judge.md`. Evidence Status Vocabulary lists 4 statuses with one-line descriptions + cross-ref to conventions.md §3, §12.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `Get-FileHash` for handoff canonical/agent/claude | All 3 hashes identical ✅ |
| 2 | `Get-FileHash` for review canonical/agent/claude | All 3 hashes identical ✅ |
| 3 | `Get-FileHash` for plan canonical/agent/claude | All 3 hashes identical ✅ |

## Discrepancies Found

No discrepancies.

## Evidence Verification

> RF §5 Evidence items: 7 items, all VERIFIED with local file references.

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | glossary.md lines 58-80 (5 Evidence terms) | ✅ | ✅ — 5 terms present under ## Evidence Terms |
| E2 | glossary.md line 48 (TD-2 fix) | ✅ | ✅ — reads `RF §8` |
| E3 | glossary.md lines 58-80 (no domain-specific examples) | ✅ | ✅ — no mentions of screenshots, browser, curl |
| E4 | Hash comparison (adapter sync) | ✅ | ✅ — independently verified via Get-FileHash |
| E5 | .tfw/VERSION line 1 | ✅ | ✅ — `0.8.8` |
| E6 | .tfw/CHANGELOG.md lines 8-22 | ✅ | ✅ — [0.8.8] entry present with correct structure |
| E7 | .tfw/CHANGELOG.md line 6 | ✅ | ✅ — [Unreleased] present |

## Knowledge Citations Verified

> HL §7.2 has 11 citations (K1-K11). Spot-checking key items:

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|-------------|
| 1 | HL §7.2 K4 | philosophy.md F21 | ✅ | ✅ — "Explicit N/A pattern transforms silent skip → conscious trace" |
| 2 | HL §7.2 K7 | conventions.md §12 | ✅ | ✅ — Safety and Execution Honesty section exists |
| 3 | HL §7.2 K11 | philosophy.md F13 | ✅ | ✅ — domain-agnostic principle |

> ONB §7 confirms all 11 citations read. Executor marked most as N/A (Phase C = documentation, not behavioral), K4 and K11 applied.

## Checkpoint

**Self-check:**
- [x] Opened ≥ 5 files and recorded findings?
- [x] Ran at least 1 build/test command (or documented why not)? (Hash comparisons for adapter sync)
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented? (No contradictions — Phase C is documentation/sync)
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist)?
  - Total citations: 11, verified (spot-check): 3, hallucinations: 0
- [x] Evidence artifacts from RF §5 verified (files exist, claims match)?
  - Total evidence items: 7, verified: 7, missing: 0

Stage complete: YES
