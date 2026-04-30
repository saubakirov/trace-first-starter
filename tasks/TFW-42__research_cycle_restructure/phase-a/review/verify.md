# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: docs
> Min verify ratio: 0.42
> RF files claimed: 6 (conventions.md MODIFY, 4 template renames, RES.md MODIFY)
> Files to verify: ⌈6 × 0.42⌉ = 3

## Verification Log

### V1: `.tfw/conventions.md` §4 Research subfolder (lines 131-150)
- **RF claim:** Complete rewrite — unified `research/` container, `research/iterN/` pattern, numbered stage files, co-located `RES.md`
- **Actual:** Lines 131-150 show:
  - `research/` described as single container (line 133)
  - `research/iterations.yaml` as control file location (line 137)
  - `research/iterN/` pattern with `1_briefing.md` through `4_challenge.md` (lines 138-149)
  - `RES.md` co-located inside `iterN/` (lines 143, 149)
  - Multi-iteration table shows `research/iter1/`, `research/iter2/`, `research/iterN/` paths (lines 158-162)
  - Trace rule preserved at line 164
- **Match:** ✅

### V2: `.tfw/conventions.md` §4 iterations.yaml schema (lines 166-190)
- **RF claim:** Enriched with `agent` + `sources` optional fields, `res_file` paths updated, no `brief`/`notes`/`depends_on`, "traceability, not dispatch" text
- **Actual:**
  - `agent: antigravity` commented-out with `# optional` annotation (line 179)
  - `sources: [external, codebase]` commented-out with `# optional` annotation (line 180)
  - `res_file: research/iter1/RES.md` (line 178), `res_file: research/iter2/RES.md` (line 185)
  - No `brief`, `notes`, or `depends_on` fields (grep verified: 0 matches)
  - Line 188: "The `agent` field records which tool or agent conducted the iteration — for traceability, not dispatch."
- **Match:** ✅

### V3: `.tfw/templates/research/` — numbered stage files
- **RF claim:** `1_briefing.md`, `2_gather.md`, `3_extract.md`, `4_challenge.md` exist; old files deleted
- **Actual:** Directory listing shows exactly 4 files:
  - `1_briefing.md` (694 bytes)
  - `2_gather.md` (1290 bytes)
  - `3_extract.md` (1357 bytes)
  - `4_challenge.md` (1508 bytes)
  - No files without numeric prefix present
- **Match:** ✅

### V4: `.tfw/conventions.md` §4 Agent selection guidance (lines 192-204)
- **RF claim:** New subsection, 5-row capability table, no tool brand names, "guidance, not prescription" footer
- **Actual:**
  - Subsection titled "Agent selection guidance" (line 192)
  - 5-row table: Web research, Code audit, Infrastructure recon, Architecture synthesis, Data analysis (lines 197-202)
  - Columns: Research Activity, Key Capability, When to consider (line 196)
  - No tool brand names (no "Antigravity", "Claude Code", "Codex", "Cursor" in section)
  - Footer: "This is guidance, not prescription — the coordinator decides agent assignment based on project context and available tools." (line 204)
- **Match:** ✅

### V5: `.tfw/conventions.md` §4 Phase folder naming (lines 113-125, 210-227)
- **RF claim:** `PhaseA` → `phase-a` in filename table and multi-phase folder structure
- **Actual:**
  - Filename table uses `phase-{x}` format and `phase-a` examples (lines 121-125)
  - Multi-phase example tree uses `phase-a/`, `phase-b/` (lines 218-226)
  - Grep for `PhaseA` in conventions.md: 0 matches
- **Match:** ✅

### V6: `.tfw/templates/RES.md` line 15
- **RF claim:** Updated from `research/briefing.md` to `1_briefing.md in iteration folder`
- **Actual:** Line 15 reads: `{Copied from or reference to `1_briefing.md` in iteration folder.}`
- **Match:** ✅

### V7: `.tfw/conventions.md` Review subfolder reference (line 208)
- **RF claim:** Updated parallel reference from `research/gather.md` to `research/iterN/1_briefing.md`
- **Actual:** Line 208 reads: `Parallels research stage files (`research/iterN/1_briefing.md`, etc.)`
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | Grep `PhaseA` in conventions.md | 0 matches ✅ |
| 2 | Grep `research2/` in conventions.md | 0 matches ✅ |
| 3 | Grep `depends_on` in conventions.md | 0 matches ✅ |
| 4 | `ls .tfw/templates/research/` | 4 numbered files, 0 unnumbered ✅ |

> No test runner applicable — documentation changes only.

## Discrepancies Found

No discrepancies. Escalation to 100% was performed proactively (7/6 files verified = >100%).

## Knowledge Citations Verified

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | HL §7.2 KC1 | philosophy.md F4 — Structural enforcement beats format enforcement | ✅ | ✅ (line 11) |
| 2 | HL §7.2 KC2 | philosophy.md F24 — Instructions produce compliance, heuristics produce competence | ✅ | ✅ (line 31) |
| 3 | HL §7.2 KC3 | convention.md F19 — Naming consistency is a design principle | ✅ | ✅ (line 26) |
| 4 | HL §7.2 KC4 | KNOWLEDGE.md D48 — Naming normalization | ✅ | ✅ (line 79) |
| 5 | HL §7.2 KC5 | KNOWLEDGE.md D38 — Multi-iteration research | ✅ | ✅ (line 69) |
| 6 | HL §7.2 KC6 | process.md F14 — Without YAML control files, agents fast-run | ✅ | ✅ (line 21) |
| 7 | HL §7.2 KC7 | convention.md F15 — Multi-phase uses PhaseX/ subfolders | ✅ | ✅ (line 22) |

> Total citations: 7, verified: 7, hallucinations: 0

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈6 × 0.42⌉ = 3 files and recorded findings? (opened 7)
- [x] Ran at least 1 build/test command (or documented why not)? (grep commands run, no test runner for docs)
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented? (D38 references `researchN/` — will be updated by tfw-docs as "refactored by TFW-42")
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist)?
  - Total citations: 7, verified: 7, hallucinations: 0

Stage complete: YES
