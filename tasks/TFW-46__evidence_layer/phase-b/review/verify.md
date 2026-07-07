# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: code
> Min verify ratio: 0.42 (from project_config.yaml)
> RF files claimed: 5 (handoff.md, review.md, plan.md, RF.md, README.md)
> Files to verify: ⌈5 × 0.42⌉ = 3 (escalated to 100% for thoroughness — workflow spec changes)

## Verification Log

### V1: `.tfw/workflows/handoff.md`
- **RF claim:** New Step 11 (Collect evidence) inserted between Step 10 (build gate) and Step 12 (Pre-RF Gate). Proportionality clause, DEFERRED/BLOCKED guidance, proactive tooling, no tool names. Steps 11→12, 12→13 renumbered. §5 Evidence in mandatory sections. `Never omit §5. Never omit §7-9.`
- **Actual:**
  - Line 85: `11. **Collect evidence**` — correct title, present between Step 10 (line 82-83) and Step 12 (line 94) ✅
  - Lines 85-90: Full step content — proportionality clause ("If NO TS AC items have Evidence fields — skip this step entirely" at line 90), DEFERRED/BLOCKED guidance (line 88), proactive tooling note (line 89), environment types listed (line 86) without specific tool names ✅
  - Line 94: `12. **Pre-RF Gate**` — correctly renumbered from 11 ✅
  - Line 96: `13. **Create RF file**` — correctly renumbered from 12 ✅
  - Line 101: `- **§5 Evidence**` in mandatory sections list ✅
  - Line 106: `Never omit §5. Never omit §7-9.` — two separate constraints ✅
- **Match:** ✅

### V2: `.tfw/workflows/review.md`
- **RF claim:** 2 new Trust Protocol entries — "Evidence: VERIFIED" (Verify) and "Evidence: N/A" (Challenge). Step 3 evidence audit reference. Existing entries unchanged.
- **Actual:**
  - Line 45: `| "Evidence: VERIFIED" (RF §5) | Verify | Check artifact exists and matches claim — see verify.md Evidence Verification |` ✅
  - Line 46: `| "Evidence: N/A" or no evidence (RF §5) | Challenge | Check if TS had Evidence fields; if yes, challenge the N/A |` ✅
  - Lines 42-44, 47-50: Original 7 entries unchanged ✅
  - Line 77: `Check evidence: verify.md includes an Evidence Verification section — audit evidence artifacts against RF §5 claims.` ✅
  - Total Trust Protocol entries: 9 (was 7, +2 new) — matches RF claim ✅
- **Match:** ✅

### V3: `.tfw/workflows/plan.md`
- **RF claim:** Step 7, sub-step 3: Evidence fields reminder. 3 lines. References TS template grammar. Proportionality note.
- **Actual:**
  - Line 125: `3. **Evidence fields** — for each AC item, consider whether real-environment evidence is needed.` ✅
  - Line 126: `   Write an \`Evidence:\` field (full spec, minimal, N/A, DEFERRED, or leave empty). See TS template for grammar.` ✅
  - Line 127: `   Proportionality: trivial tasks may have all Evidence fields N/A or empty.` ✅
  - Placement: after sub-step 2 (Budget check, line 122-124), before small/large task branching (line 129) ✅
  - No duplication of TS template instructions — just a pointer with grammar summary ✅
- **Match:** ✅

### V4: `.tfw/templates/RF.md`
- **RF claim:** Line 68: `§5 Observations` → `§6 Observations` (TD-1 fix)
- **Actual:**
  - Line 68: `> NOT fact candidates: "project uses git", implementation details (→ §6 Observations → tfw-docs),` ✅
  - Previous Phase A value was `§5 Observations` — now correctly `§6 Observations` ✅
- **Match:** ✅

### V5: `README.md`
- **RF claim:** Task Board updated with Phase B TS/ONB links
- **Actual:**
  - Line 278: TFW-46 row shows `[B🟡](tasks/TFW-46__evidence_layer/phase-b/TS__phase-b__workflow_integration.md)` for TS, `[B🟠](tasks/TFW-46__evidence_layer/phase-b/ONB__phase-b__workflow_integration.md)` for ONB, `[B🟢](tasks/TFW-46__evidence_layer/phase-b/RF__phase-b__workflow_integration.md)` for RF ✅
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| — | N/A | Markdown-only changes. No build/test/lint commands configured for .tfw/ framework files |

> No test runner applicable — this is a methodology spec project with `echo` commands in build config.

## Discrepancies Found

No discrepancies. All 5 files match RF claims exactly.

## Evidence Verification

> Verify that RF §5 Evidence artifact references resolve to real files or inline output.

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | handoff.md lines 85-90 | ✅ | ✅ — Step 11 content confirmed |
| E2 | handoff.md lines 94, 96 | ✅ | ✅ — Steps 12, 13 renumbered correctly |
| E3 | handoff.md lines 101, 106 | ✅ | ✅ — §5 in mandatory list, Never omit §5 present |
| E4 | review.md lines 45-46 | ✅ | ✅ — 2 Trust Protocol entries correct |
| E5 | plan.md lines 125-127 | ✅ | ✅ — 3-line evidence reminder present |
| E6 | review.md line 77 | ✅ | ✅ — Evidence audit reference present |
| E7 | RF.md line 68 | ✅ | ✅ — `§6 Observations` correct |

> All 7 evidence items VERIFIED. Line references match actual file content.

## Knowledge Citations Verified

> Verify that HL §7.2 and ONB §7 citation links resolve to real items.

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | HL §7.2 K1 | README Values: Honesty Over Convincingness | ✅ | ✅ — README.md line 124 |
| 2 | HL §7.2 K3 | philosophy.md F4 | ✅ | ✅ — structural enforcement fact |
| 3 | HL §7.2 K7 | conventions.md §12 | ✅ | ✅ — line 395-396 |
| 4 | HL §7.2 K9 | D41 (TFW-41) | ✅ | ✅ — KNOWLEDGE.md §1 row D49 |
| 5 | HL §7.2 K10 | D46 (TFW-38) | ✅ | ✅ — KNOWLEDGE.md §1 row D46 |

> 5/11 spot-checked. All resolve to real items. No hallucinations.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files and recorded findings?
- [x] Ran at least 1 build/test command (or documented why not)?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist)?
  - Total citations: 11, verified: 5, hallucinations: 0
- [x] Evidence artifacts from RF §5 verified (files exist, claims match)?
  - Total evidence items: 7, verified: 7, missing: 0

Stage complete: YES
