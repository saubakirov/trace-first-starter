# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: spec
> Min verify ratio: 0.42
> RF files claimed: 7 (3 new + 4 modified)
> Files to verify: ⌈7 × 0.42⌉ = 3 (verifying all 6 in-scope files)

## Verification Log

### V1: `.tfw/templates/review/map.md`
- **RF claim:** Map stage template — Student mindset, TS↔RF alignment table, self-check gate (4 items)
- **Actual:** File exists (31 lines, 906B). Mindset field present: "Newcomer" (not "Student" as RF and TS state). Test question present. TS↔RF alignment table present. Self-check gate has 4 checkboxes. Structure: Understanding → TS↔RF Alignment → Deviations → Checkpoint.
- **Match:** ⚠️ partial — Mindset label says "Newcomer" not "Student". TS Step 1 specifies `> **Mindset:** Student.` RF §1 says "Student mindset." Actual file says `> **Mindset:** Newcomer.` Meanwhile review.md Step 1 blockquote says `> **Mindset:** Student.` — inconsistency between workflow and template.

### V2: `.tfw/templates/review/verify.md`
- **RF claim:** Verify stage template — Auditor mindset, verification log per file, commands table, discrepancy escalation, self-check gate (4 items incl. KNOWLEDGE.md)
- **Actual:** File exists (44 lines, 1341B). Mindset: "Auditor" ✅. Test question present. Verification log template per file ✅. Commands table ✅. Discrepancy escalation rule ✅. Self-check: 4 items, item 4 = KNOWLEDGE.md contradiction check ✅.
- **Match:** ✅

### V3: `.tfw/templates/review/judge.md`
- **RF claim:** Judge stage template — Judge mindset, universal 6-point checklist, mode-specific slot, KNOWLEDGE.md contradictions table, self-check gate (5 items)
- **Actual:** File exists (39 lines, 1602B). Mindset: "Judge" ✅. Universal checklist: 6 items ✅. Mode-specific slot: "{Copy items from mode file}" ✅. KNOWLEDGE.md contradictions table ✅. Self-check: 5 items including evidence, verify.md reference, §6-8 quality, KNOWLEDGE.md cross-ref, Fact Candidates ✅.
- **Match:** ✅

### V4: `.tfw/workflows/review.md`
- **RF claim:** Steps 0-4 rewritten. Role Lock updated. Reviewer Identity, Trust Protocol, 🛑 WAIT gate, file-based stages, synthesis step.
- **Actual:**
  - Role Lock (line 12): "Permitted artifacts: review stage files (map.md, verify.md, judge.md) + REVIEW file." ✅
  - Reviewer Identity (lines 30-31): "Quality guardian. Trust evidence, not declarations." ✅
  - Trust Protocol (lines 33-43): 7-row table with Verify/Challenge/Trust levels ✅
  - Step 0 (lines 53-54): 🛑 WAIT + "Switch? [code/docs/spec]" ✅
  - Steps 1-3 (lines 56-87): Create review/ folder, write stage files, self-check gates ✅
  - Step 4 (lines 89-98): Synthesize from stage files into REVIEW ✅
  - Steps 5-7 (lines 100-131): Unchanged ✅
- **Match:** ✅

### V5: `.tfw/templates/REVIEW.md`
- **RF claim:** Added stage files reference in header (lines 9-10). §2 Verify points to verify.md.
- **Actual:**
  - Lines 9-10: `> **Stage files**: \`review/map.md\`, \`review/verify.md\`, \`review/judge.md\`` + synthesis instruction ✅
  - Line 23: `> Raw verification log: see \`review/verify.md\`.` ✅
- **Match:** ✅

### V6: `.tfw/conventions.md`
- **RF claim:** §3 new "Review subfolder" section (lines 138-140)
- **Actual:** Lines 138-140: "### Review subfolder" with description paralleling research subfolder. References templates and synthesis pattern. ✅
- **Match:** ✅

### V7: `.agent/workflows/tfw-review.md` (adapter — out of TS scope)
- **RF claim:** Adapter re-synced from `.tfw/workflows/review.md`
- **Actual:** Content is byte-identical to `.tfw/workflows/review.md` (both 145 lines, 6477 bytes) except for YAML frontmatter. ✅
- **Match:** ✅

## Commands Executed

No commands to run — all artifacts are markdown files. No build/test/lint applicable. Verification was done by opening and reading each file.

## Discrepancies Found

1. **map.md mindset label inconsistency**: TS Step 1 specifies `> **Mindset:** Student.` Template uses "Newcomer." RF §1 describes it as "Student mindset" — RF claim does not match actual template content. review.md Step 1 blockquote says "Student" — workflow and template are misaligned.

2. **conventions.md §15 Role Lock table not updated**: review.md Role Lock (line 12) was updated to include stage files. But conventions.md §15 Role Lock Protocol table (line 362) still says `review.md | Reviewer | REVIEW` — doesn't mention review stage files. This is an inconsistency: the review.md workflow says "review stage files + REVIEW" but the conventions.md master table says only "REVIEW."

3. **glossary.md Reviewer entry not updated**: glossary.md line 101 says "Writes REVIEW file with 9-point checklist." Post A.2, the reviewer writes 3 stage files + REVIEW (4 artifacts). The checklist is now 6 universal + mode-specific (not "9-point"). This was likely out of scope for A.2 but creates a stale reference.

> Discrepancy #1 is within scope (AC2 specifies Mindset as mandatory header field with Student/Auditor/Judge).
> Discrepancy #2 is within scope (conventions.md was modified — the Role Lock table should match the workflow).
> Discrepancy #3 is out of scope (glossary.md was not in TS §3 Affected Files) — observation, not a blocker.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈7 × 0.42⌉ = 3 files and recorded findings? (Opened all 7)
- [x] Ran at least 1 build/test command (or documented why not)? (No commands applicable — markdown only)
- [x] Each RF §3 (AC) checkmark verified against actual file? (14/14 checked, 1 has partial mismatch)
- [x] KNOWLEDGE.md checked — do changes contradict known decisions?
  - D18 (review stages as separate files): Changes implement D18 correctly ✅
  - D21 (Coordinator Mindset / Identity): Reviewer Identity matches D21 pattern ✅
  - D27 (Trust Protocol): Trust Protocol matches D27 pattern ✅
  - D13 (Separate review from handoff): Stage files strengthen this separation ✅
  - No KNOWLEDGE.md contradictions.

Stage complete: YES
