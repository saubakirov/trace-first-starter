# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: docs
> Min verify ratio: 0.42
> RF files claimed: 2 (base.md, plan.md)
> Files to verify: ⌈2 × 0.42⌉ = 1 (escalated to 2 — both files verified since only 2 total)

## Verification Log

### V1: `.tfw/workflows/research/base.md`
- **RF claim:** Steps 0, 3, 4, 5, 6 updated. `iterations.yaml` → `research/iterations.yaml`. `researchN/` → `research/iterN/`. `RES__*` → `research/iterN/RES.md`. Stage files numbered. No old-convention paths remain.
- **Actual:**
  - Line 17: `Check \`research/iterations.yaml\`` ✅
  - Line 19: `Count \`research/iterN/\` folders` ✅
  - Line 21: `read predecessor \`research/iterN/RES.md\`` ✅
  - Line 24: `research/iterN/` for subfolder checks ✅
  - Line 41: `research/iter1/` for iteration 1 ✅
  - Line 42: `research/iterN/` for iteration N ✅
  - Line 44: explicit template list `1_briefing.md`, `2_gather.md`, `3_extract.md`, `4_challenge.md` ✅
  - Line 46: `research/iterN-1/RES.md` for predecessor ✅
  - Line 53: `research/iterN/1_briefing.md` ✅
  - Line 64: `2_gather.md`, `3_extract.md`, `4_challenge.md` (numbered) ✅
  - Line 87: stage files listed numbered ✅
  - Line 88: `research/iterN/RES.md` ✅
  - PowerShell grep: `researchN/` → 0 matches ✅
  - PowerShell grep: `research2/` → 0 matches ✅
  - PowerShell grep: `RES__iter` → 0 matches ✅
  - PowerShell grep: `briefing.md` without number → all 3 matches have `1_` prefix ✅
- **Match:** ✅

### V2: `.tfw/workflows/plan.md`
- **RF claim:** Step 6b: `research/iterations.yaml` path, `agent`/`sources` optional fields, multi-agent reference. Step 6c: `research/iterN/RES.md`. Step 7: `phase-a/`, `phase-b/` kebab-case.
- **Actual:**
  - Line 90: `Create \`research/iterations.yaml\` in task's \`research/\` folder` ✅
  - Line 95: `agent` (free-text), `sources` (list) as optional fields ✅
  - Line 97: `For multi-agent research, see conventions.md §4 (Agent selection guidance).` ✅
  - Line 103: `Read all \`research/iterN/RES.md\` files and \`research/iterations.yaml\`` ✅
  - Line 104: `Update \`research/iterations.yaml\`` ✅
  - Line 110: `Add next entry to \`research/iterations.yaml\`` ✅
  - Line 137: `phase-a/` ✅
  - Line 138-139: `HL__phase-a__{title}.md`, `TS__phase-a__{title}.md` ✅
  - Line 140-142: `phase-b/`, `HL__phase-b__{title}.md`, `TS__phase-b__{title}.md` ✅
  - Line 136: `← master HL, research/ here` (no stale `RES,`) ✅
  - PowerShell grep: `PhaseA` → 0 matches ✅
  - PowerShell grep: `researchN/` → 0 matches ✅
  - PowerShell grep: `RES__` → 0 matches ✅
  - PowerShell grep: `Antigravity|Claude Code|Codex` → 0 matches ✅
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `Select-String "researchN/"` in base.md | 0 matches ✅ |
| 2 | `Select-String "research2/"` in base.md | 0 matches ✅ |
| 3 | `Select-String "RES__iter"` in base.md | 0 matches ✅ |
| 4 | `Select-String "briefing.md"` in base.md | 3 matches, all with `1_` prefix ✅ |
| 5 | `Select-String "PhaseA"` in plan.md | 0 matches ✅ |
| 6 | `Select-String "researchN/"` in plan.md | 0 matches ✅ |
| 7 | `Select-String "Antigravity\|Claude Code\|Codex"` in plan.md | 0 matches ✅ |
| 8 | `Select-String "RES__"` in plan.md | 0 matches ✅ |
| 9 | `Select-String "research/iterations.yaml"` in plan.md | 4 matches (lines 90, 103, 104, 110) ✅ |
| 10 | `Select-String "research/iterN/RES.md"` in plan.md | 1 match (line 103) ✅ |
| 11 | `Select-String "phase-a"` in plan.md | 3 matches (lines 137, 138, 139) ✅ |
| 12 | `Select-String "Agent selection guidance"` in plan.md | 1 match (line 97) ✅ |
| 13 | `Select-String "iterN"` in base.md | 7 matches (lines 19, 21, 24, 42, 46, 53, 88) ✅ |
| 14 | `Select-String "1_briefing"` in base.md | 3 matches (lines 44, 53, 87) ✅ |
| 15 | `Select-String "2_gather"` in base.md | 3 matches (lines 44, 64, 87) ✅ |

> No lint/test commands applicable — documentation-only changes.

## Discrepancies Found

No discrepancies.

## Knowledge Citations Verified

> HL §7.2 has 7 citations. ONB §7 confirms all 7 as read+applied.

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | HL §7.2 KC1 | knowledge/philosophy.md F4 | ✅ | ✅ |
| 2 | HL §7.2 KC2 | knowledge/philosophy.md F24 | ✅ | ✅ |
| 3 | HL §7.2 KC3 | knowledge/convention.md F19 | ✅ | ✅ |
| 4 | HL §7.2 KC4 | KNOWLEDGE.md D48 | ✅ | ✅ |
| 5 | HL §7.2 KC5 | KNOWLEDGE.md D38 | ✅ | ✅ |
| 6 | HL §7.2 KC6 | knowledge/process.md F14 | ✅ | ✅ |
| 7 | HL §7.2 KC7 | knowledge/convention.md F15 | ✅ | ✅ |

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files and recorded findings?
- [x] Ran at least 1 build/test command (or documented why not)?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist)?
  - Total citations: 7, verified: 7, hallucinations: 0

Stage complete: YES
