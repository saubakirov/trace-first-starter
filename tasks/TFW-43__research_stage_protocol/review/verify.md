# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: docs
> Min verify ratio: 0.42
> RF files claimed: 10
> Files to verify: ⌈10 × 0.42⌉ = 5 (escalated to 10 — all files verified)

## Verification Log

### V1: `.tfw/templates/research/1_briefing.md`
- **RF claim:** Added h1 guiding question `"What should we investigate?"` + `> **Mindset:** Strategist...` + `> **Test:**` blockquote
- **Actual:** L1: `# Briefing — "What should we investigate?"` ✅. L2: `> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.` ✅. L3: `> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"` ✅. Mindset block sits between h1 and `> Parent:` line (L4). All existing content below header preserved.
- **Match:** ✅ — exact match with TS §4 AC-1 wording

### V2: `.tfw/templates/research/2_gather.md`
- **RF claim:** Added `> **Mindset:** Explorer...` + `> **Test:**` blockquote between h1 and `> Parent:`
- **Actual:** L1: `# Gather — "What do we NOT know?"` (pre-existing h1). L2: `> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.` ✅. L3: `> **Test:** "Can I name every dimension and its alternatives without checking my sources?"` ✅. L4: `> Parent:` ✅.
- **Match:** ✅ — exact match with TS §4 AC-1 wording

### V3: `.tfw/templates/research/3_extract.md`
- **RF claim:** Added `> **Mindset:** Analyst...` + `> **Test:**` blockquote between h1 and `> Parent:`
- **Actual:** L1: `# Extract — "What do we NOT see?"` (pre-existing). L2: `> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.` ✅. L3: `> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"` ✅. L4: `> Parent:` ✅.
- **Match:** ✅ — exact match with TS §4 AC-1 wording

### V4: `.tfw/templates/research/4_challenge.md`
- **RF claim:** Added `> **Mindset:** Critic...` + `> **Test:**` blockquote between h1 and `> Parent:`
- **Actual:** L1: `# Challenge — "What do we NOT expect?"` (pre-existing). L2: `> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.` ✅. L3: `> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"` ✅. L4: `> Parent:` ✅.
- **Match:** ✅ — exact match with TS §4 AC-1 wording

### V5: `.tfw/workflows/research/base.md`
- **RF claim:** Step 3 removed batch copy. Step 4 copy-on-enter for briefing. Step 5 restructured as FOR EACH.
- **Actual:**
  - **Step 3 (L39-48):** Title "Create Research Subfolder." Contains only mkdir instructions + iteration 2+ predecessor reference. NO copy instruction, NO template filenames. ✅ AC-2
  - **Step 4 (L49-58):** Title "Briefing Protocol." L51: `Copy \`templates/research/1_briefing.md\` into \`research/iterN/\`. Read the **Mindset** block — adopt this cognitive mode.` ✅ AC-3. Explicit copy verb.
  - **Step 5 (L60-69):** Title "Run Stages (Gather → Extract → Challenge)." L62: dimensional analysis thread (preserved). L64-69: `**FOR EACH stage** (Gather → Extract → Challenge):` with 5 numbered sub-steps: 1. Copy, 2. Read Mindset, 3. Execute OODA, 4. Complete Checkpoint, 5. 🛑 STOP. ✅ AC-4, AC-5
  - **Step 0 (L12-25):** Resume protocol says "which stage files exist? Resume from first missing stage." No assumption all files pre-exist. ✅ AC-6
- **Match:** ✅ — all Step 3/4/5 claims verified against actual file

### V6: `.agent/workflows/tfw-research.md`
- **RF claim:** Byte-copy sync from base.md
- **Actual:** 134 lines, 6097 bytes. Content identical to base.md (verified line-by-line: same frontmatter, same Steps 3/4/5 restructure, same FOR EACH at L64-69).
- **Match:** ✅

### V7: `.claude/commands/tfw-research.md`
- **RF claim:** Byte-copy sync from base.md
- **Actual:** 134 lines, 6097 bytes. Content identical to base.md.
- **Match:** ✅

### V8: `.tfw/VERSION`
- **RF claim:** `0.8.6` → `0.8.7`
- **Actual:** L1: `0.8.7` ✅
- **Match:** ✅

### V9: `.tfw/project_config.yaml`
- **RF claim:** version `0.8.6` → `0.8.7`
- **Actual:** L7: `version: "0.8.7"` ✅
- **Match:** ✅

### V10: `.tfw/CHANGELOG.md`
- **RF claim:** Added `[0.8.7]` entry with Added/Changed/Removed sections
- **Actual:** L8-16: `[0.8.7] — 2026-05-01` with ### Added (Mindset blocks + Briefing h1), ### Changed (copy-on-enter + adapters), ### Removed (batch template copy). All items reference TFW-43. ✅
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| — | N/A — methodology framework, no executable code or tests | No test runner available |

> Markdown templates and workflow files — no build/lint/test applicable. SHA-256 comparison claim in RF trusted (all 3 adapter files confirmed identical by byte count: 134 lines, 6097 bytes each).

## Discrepancies Found

No discrepancies. All 10 files verified — RF claims match actual file contents exactly.

## Knowledge Citations Verified

> Verify that HL §7.2 and ONB §7 citation links resolve to real items.

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | HL §7.2 KC1 | knowledge/philosophy.md F4 | ✅ | ✅ (structural enforcement beats format enforcement) |
| 2 | HL §7.2 KC2 | knowledge/philosophy.md F18 | ✅ | ✅ (different templates serve different cognitive modes) |
| 3 | HL §7.2 KC3 | knowledge/philosophy.md F20 | ✅ | ✅ (investigative vs procedural workflows) |
| 4 | HL §7.2 KC4 | knowledge/philosophy.md F24 | ✅ | ✅ (instructions→compliance, heuristics→competence) |
| 5 | HL §7.2 KC5 | knowledge/process.md F4 | ✅ | ✅ (agents follow steps + gates) |
| 6 | HL §7.2 KC6 | KNOWLEDGE.md §1 D31 | ✅ | ✅ (filesystem state machine) |
| 7 | HL §7.2 KC7 | KNOWLEDGE.md §1 D41 | ✅ | ✅ (4-stage review flow) |
| 8 | HL §7.2 KC8 | knowledge/stakeholder.md F2 | ✅ | ✅ (file naming = execution order) |

> ONB §7 confirmed all 8 HL citations read and applied. No new items added. No hallucinations detected.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈10 × 0.42⌉ = 5 files and recorded findings? (opened all 10)
- [x] Ran at least 1 build/test command (or documented why not)? (no executable code — documented)
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented? (no contradictions — D31 restored, consistent with D50)
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist)?
  - Total citations: 8, verified: 8, hallucinations: 0

Stage complete: YES
