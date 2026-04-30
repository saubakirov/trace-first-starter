# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: docs
> Min verify ratio: 0.42
> RF files claimed: 8
> Files to verify: ⌈8 × 0.42⌉ = 4

## Verification Log

### V1: `.tfw/glossary.md` (L144-148)
- **RF claim:** "Iteration (Research)": `researchN/` → `research/iterN/`, `RES__iterN__*.md` → `research/iterN/RES.md`. "iterations.yaml": "at task root" → "inside `research/` subfolder", `agent`/`sources` optional fields added.
- **Actual:** L144: `research/iterN/` and `research/iterN/RES.md` confirmed. L147-148: "Control file inside the `research/` subfolder" confirmed. `agent` described as "(free-text — which tool/agent ran the iteration, for traceability)" and `sources` as "(list — what source categories were consulted)". Both marked as "Optional fields". L150-151: "min_iterations" unchanged (config-only, no path references).
- **Match:** ✅

### V2: `.agent/workflows/tfw-research.md` vs `.tfw/workflows/research/base.md`
- **RF claim:** "Overwritten with `.tfw/workflows/research/base.md` (Phase B output)"
- **Actual:** `Compare-Object` returned empty output — 0 differences. Files are byte-identical.
- **Match:** ✅

### V3: `.claude/commands/tfw-plan.md` vs `.tfw/workflows/plan.md`
- **RF claim:** "Overwritten with `.tfw/workflows/plan.md` (Phase B output)"
- **Actual:** `Compare-Object` returned empty output — 0 differences.
- **Match:** ✅

### V4: `.tfw/VERSION`
- **RF claim:** "0.8.5 → 0.8.6"
- **Actual:** File contains `0.8.6` (single line).
- **Match:** ✅

### V5: `.tfw/CHANGELOG.md` (L8-18)
- **RF claim:** "Added `[0.8.6] — 2026-04-30` section with 10 changelog items covering all 3 phases"
- **Actual:** L8: `## [0.8.6] — 2026-04-30` confirmed. L9: `### Changed` section. L10-18: 9 bullet items (not 10 as RF claims) covering Phase A (5 items), Phase B (2 items), Phase C (2 items). All have phase attribution tags (TFW-42/A, /B, /C).
- **Match:** ⚠️ Minor: RF says "10 changelog items", actual count is 9. Semantically immaterial — all changes are documented.

### V6: `.tfw/project_config.yaml` (L7)
- **RF claim:** "`tfw.version: \"0.8.5\"` → `\"0.8.6\"`"
- **Actual:** L7: `version: "0.8.6"` confirmed.
- **Match:** ✅

### V7: `.claude/commands/tfw-research.md` vs `.tfw/workflows/research/base.md`
- **RF claim:** Byte-identical after sync.
- **Actual:** `Compare-Object` returned empty output — 0 differences.
- **Match:** ✅

### V8: `.agent/workflows/tfw-plan.md` vs `.tfw/workflows/plan.md`
- **RF claim:** Byte-identical after sync.
- **Actual:** `Compare-Object` returned empty output — 0 differences.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `grep researchN/ glossary.md` | 0 matches ✅ |
| 2 | `grep RES__iter glossary.md` | 0 matches ✅ |
| 3 | `grep "at task root" glossary.md` | 0 matches ✅ |
| 4 | `grep PhaseA glossary.md` | 0 matches ✅ |
| 5 | `Compare-Object base.md tfw-research.md` (×2 adapters) | 0 differences each ✅ |
| 6 | `Compare-Object plan.md tfw-plan.md` (×2 adapters) | 0 differences each ✅ |

> No build/test/lint commands applicable — markdown documentation changes only.

## Discrepancies Found

1. **Minor:** RF §1 says "10 changelog items", actual CHANGELOG has 9 bullet points under `[0.8.6]`. Not a DoD violation — all changes are documented. Likely a counting error in the RF narrative.

> Discrepancy is cosmetic (narrative text, not AC-related). No escalation to 100%.

## Knowledge Citations Verified

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | HL §7.2 KC1 | knowledge/philosophy.md F4 | ✅ | ✅ |
| 2 | HL §7.2 KC2 | knowledge/philosophy.md F24 | ✅ | ✅ |
| 3 | HL §7.2 KC3 | knowledge/convention.md F19 | ✅ | ✅ |
| 4 | HL §7.2 KC4 | KNOWLEDGE.md D48 | ✅ | ✅ |
| 5 | HL §7.2 KC5 | KNOWLEDGE.md D38 | ✅ | ✅ |
| 6 | HL §7.2 KC6 | knowledge/process.md F14 | ✅ | ✅ |
| 7 | HL §7.2 KC7 | knowledge/convention.md F15 | ✅ | ✅ |

> Total citations: 7, verified: 7, hallucinations: 0

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈8 × 0.42⌉ = 4 files and recorded findings? (opened 8 — all files verified)
- [x] Ran at least 1 build/test command (or documented why not)? (N/A — markdown only, documented)
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented? (no contradictions)
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist)?
  - Total citations: 7, verified: 7, hallucinations: 0

Stage complete: YES
