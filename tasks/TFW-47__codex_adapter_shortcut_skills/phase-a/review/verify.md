# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: docs
> Min verify ratio: 0.42
> RF files claimed: 6 (1 new + 5 modified)
> Files to verify: ⌈6 × 0.42⌉ = 3 minimum → verified 6 (all)

## Verification Log

### V1: `.tfw/templates/evidence/EV.md` (NEW)
- **RF claim:** "Structured evidence template: Environment header (5 fields), per-AC evidence table (6 columns), Verdict summary, optional Attachments index"
- **Actual:** File exists. Contains Environment header with 5 fields (OS, Language/Runtime, Database, Deploy target, CI/Pipeline) — all with "(if applicable)" where appropriate. Per-AC table has 6 columns (`# | AC | What was verified | Environment | Result | Artifact`). Verdict line uses `{N}/{M} VERIFIED...` format. Attachments section present with guidance "Omit this section if no binary artifacts exist." Naming convention documented at bottom.
- **Match:** ✅

### V2: `.tfw/conventions.md` §3 (MODIFIED)
- **RF claim:** "§3: mandatory folder language + EV file in pipeline table + template reference"
- **Actual:** §3 blockquote (L113-117) says "Every task directory MUST contain an `evidence/` subfolder" — mandatory language confirmed. Pipeline table (L119-125) has EV file row and RF row updated (Summary/Reference cognitive mode). Template reference at L117. No "optional" or "only when binary" language found (grep confirmed zero hits).
- **Match:** ✅

### V3: `.tfw/conventions.md` §4 (MODIFIED)
- **RF claim:** "§4: 2 EV naming rows in artifact table + evidence subfolder section + evidence/ in multi-phase structure"
- **Actual:** Artifact naming table (L146-147) has 2 new rows: `Single-phase EV` and `Phase EV` with correct format/examples. Evidence subfolder section (L219-221) uses "MUST contain" language. Multi-phase structure (L237-238) shows `evidence/` as "Mandatory evidence folder" with `EV__phase-a__data_model.md` example.
- **Match:** ✅

### V4: `.tfw/templates/TS.md` (MODIFIED)
- **RF claim:** "Added `### Evidence Artifacts` subsection after AC items with guidance and example table"
- **Actual:** `### Evidence Artifacts` at L63. Guidance text: "List expected evidence files. Minimum: one EV file (always required)." Example table shows required EV file + optional binary row. Section is after AC items block but within §5 scope (subsection).
- **Match:** ✅

### V5: `.tfw/templates/RF.md` §5 (MODIFIED)
- **RF claim:** "§5 replaced: inline evidence table → pointer to EV file + verdict summary"
- **Actual:** §5 at L39. Cognitive mode comment updated. Pointer: `See [EV file](evidence/EV__{PREFIX}-{N}__{title}.md) for evidence details.` Verdict line: `Evidence verdict: {N}/{M} VERIFIED...` No inline table present.
- **Match:** ✅

### V6: `.tfw/workflows/handoff.md` Step 11 (MODIFIED)
- **RF claim:** "Step 11 rewritten: 6 numbered substeps for evidence folder creation and population. Skip condition removed"
- **Actual:** Step 11 (L85-94) has 6 numbered substeps: (1) Create evidence/ folder, (2) Copy EV template, (3) Fill Environment header, (4) Walk AC items → add rows, (5) Write Verdict, (6) Binary artifacts → Attachments. No skip condition found (grep "skip this step" = zero hits). RF §5 pointer instruction present at L94.
- **Match:** ✅

### V7: `KNOWLEDGE.md` D53 (MODIFIED)
- **RF claim:** "D53 added: evidence enforcement decision with D16 revocation"
- **Actual:** D53 at L84. Contains "**Revokes** TFW-46 research D16 (optional folder policy)." Full justification present with 0/38 metric. Source column: "TFW-47 HL, RES iter1, Phase A RF".
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `grep -c "evidence/" conventions.md` | 6 hits (gate ≥3 ✅) |
| 2 | `grep "only when binary" conventions.md` | 0 hits ✅ — old language removed |
| 3 | `grep "skip this step" handoff.md` | 0 hits ✅ — skip condition removed |
| 4 | `grep "Evidence Artifacts" templates/TS.md` | L63 ✅ — section exists |
| 5 | `grep "EV file" templates/RF.md` | L41, L44 ✅ — pointer format present |
| 6 | `grep "D53" KNOWLEDGE.md` | L84 ✅ — decision exists |

## Discrepancies Found

No discrepancies.

## Evidence Verification

> RF §5 points to `evidence/EV__phase-a__evidence_enforcement.md`. All ACs had `Evidence: N/A` in TS.

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | evidence/EV__phase-a__evidence_enforcement.md | ✅ | ✅ — EV file exists with 6 rows (E1-E6), all N/A status. Verdict "0/6 VERIFIED, 0 DEFERRED, 0 BLOCKED, 6 N/A" matches RF §5 verdict |

> All TS AC items had `Evidence: N/A` — definition documents, not runtime output. The all-N/A verdict is correct for this task type.

## Knowledge Citations Verified

> HL §7.2 has 9 citations (KC1-KC9). ONB §7 confirms read of all 9. Verifying resolution:

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | HL §7.2 KC1 | KNOWLEDGE.md D52 | ✅ | ✅ — L83 |
| 2 | HL §7.2 KC2 | TFW-46 research D16 | ✅ | ✅ — referenced in research/iter2/RES.md |
| 3 | HL §7.2 KC3 | knowledge/convention.md F5 | ✅ | ✅ — workflows = source of truth |
| 4 | HL §7.2 KC4 | KNOWLEDGE.md D15 | ✅ | ✅ — L46, Claude Code thin adapters |
| 5 | HL §7.2 KC5 | KNOWLEDGE.md D50 | ✅ | ✅ — L81, adapter sync |
| 6 | HL §7.2 KC6 | knowledge/process.md F3 | ✅ | ✅ — naming creates behavior |
| 7 | HL §7.2 KC7 | knowledge/domain.md F4 | ✅ | ✅ — agents = IDE systems |
| 8 | HL §7.2 KC8 | conventions.md §12 | ✅ | ✅ — L411, evidence requires artifact ref |
| 9 | HL §7.2 KC9 | conventions.md §14 | ✅ | ✅ — L442, VERIFIED without artifact = anti-pattern |

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files and recorded findings?
  - Opened 7/6 files (100%)
- [x] Ran at least 1 build/test command (or documented why not)?
  - Ran 6 grep commands (no test suite for markdown)
- [x] Each RF §3 (AC) checkmark verified against actual file?
  - AC-1 through AC-6 all verified against actual file contents
- [x] KNOWLEDGE.md checked — contradictions with changes documented?
  - D53 correctly extends D52 without contradiction. D16 revocation explicit.
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist)?
  - Total citations: 9, verified: 9, hallucinations: 0
- [x] Evidence artifacts from RF §5 verified (files exist, claims match)?
  - Total evidence items: 1 (EV file), verified: 1, missing: 0

Stage complete: YES
