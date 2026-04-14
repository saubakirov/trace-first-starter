# TS — TFW-38 / Phase A.2: Review Stage Files + Self-Check Gates

> **Date**: 2026-04-14
> **Author**: Coordinator
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> **Supersedes**: D8 from RES iter 2 ("stages as sections, not files")

---

## 1. Objective

Convert review stages from sections-in-one-file into file-based traces (like research stages), and add self-check gates at the end of each stage file. D8 was wrong: without file-based fixation, the reviewer runs through stages as a single stream of consciousness — same root cause as P1-P3 (no physical artifact = agent skips the cognitive work).

## 2. Scope

### In Scope
- 3 review stage templates: `map.md`, `verify.md`, `judge.md`
- Updated `review.md` workflow: stages write files, then synthesize into REVIEW
- Self-check gates per stage (paralleling research Sufficiency Verdict)
- REVIEW.md template: now a synthesis artifact (like RES), not the raw stage work
- Step 0 mode selection hardened: 🛑 WAIT gate (paralleling research Step 2)
- Mindset as mandatory header field in each stage template (not just workflow blockquote)
- Overall Reviewer Identity statement before Step 0 (D21 pattern — research has "Critical thinking partner")
- Trust Protocol for Review (D27 pattern — what trust level for each RF claim type)

### Out of Scope
- WAIT gates between stages (variant 2 — continuous flow)
- Mode files — already done in A.1, no changes needed
- Handoff/research/plan changes — already done in A.1

## 3. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `.tfw/templates/review/map.md` | CREATE | Map stage template with self-check gate |
| `.tfw/templates/review/verify.md` | CREATE | Verify stage template with self-check gate |
| `.tfw/templates/review/judge.md` | CREATE | Judge stage template with self-check gate |
| `.tfw/workflows/review.md` | MODIFY | Steps 1-3 write stage files; Step 4 synthesizes from files into REVIEW |
| `.tfw/templates/REVIEW.md` | MODIFY | Add "Stage files read" instruction; §2 Verify references verify.md findings |
| `.tfw/conventions.md` | MODIFY | §3: add review stage files to artifact taxonomy |

**Budget:** 3 new files, 3 modifications = 6 total. ✅

## 4. Detailed Steps

### Step 1: Create `templates/review/map.md`

```markdown
# Map — "What was done?"
> **Mindset:** Student. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF path](...)
> TS: [TS path](...)
> Mode: {code / docs / spec}

## Understanding

{2-3 sentences: what the executor did, key decisions, scope of changes}

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| {DoD item 1} | {RF §3 check} | ✅/❌ |

## Deviations from TS

{List any RF work not in TS scope, or TS items not addressed in RF}

## Checkpoint

**Self-check:**
- [ ] Read RF §1-§5 completely?
- [ ] Read TS DoD and matched each item to RF §3?
- [ ] Read HL §7 Principles — can I state the design philosophy?
- [ ] Read ONB — were blocking questions resolved?

Stage complete: YES / NO
```

### Step 2: Create `templates/review/verify.md`

```markdown
# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: {code / docs / spec}
> Min verify ratio: {from PROJECT_CONFIG.yaml, default 0.42}
> RF files claimed: {N}
> Files to verify: ⌈N × ratio⌉ = {M}

## Verification Log

### {V1: file path}
- **RF claim:** {what RF says about this file}
- **Actual:** {what the file actually contains}
- **Match:** ✅ / ❌ / ⚠️ partial

### {V2: file path}
...

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | {build/test/lint command} | {output summary} |

> If no commands could be run: state why. "No test runner" is valid.

## Discrepancies Found

{List. If none: "No discrepancies."}

> On ANY discrepancy: escalate to 100% verification (check all files).

## Checkpoint

**Self-check:**
- [ ] Opened ≥ ⌈N × ratio⌉ files and recorded findings?
- [ ] Ran at least 1 build/test command (or documented why not)?
- [ ] Each RF §3 (AC) checkmark verified against actual file?
- [ ] KNOWLEDGE.md checked — do changes contradict known decisions?
  - If yes: list contradictions
  - If no applicable items: "No KNOWLEDGE.md contradictions."

Stage complete: YES / NO
```

### Step 3: Create `templates/review/judge.md`

```markdown
# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Mode: {code / docs / spec}
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅/❌ | {reference verify.md §TS↔RF and specific items} |
| 2 | Philosophy aligned | ✅/❌ | {reference HL §7 Principles} |
| 3 | Tech debt documented | ✅/❌ | {RF §5 Observations present/absent} |
| 4 | Style & standards | ✅/❌ | {conventions followed? naming?} |
| 5 | Observations collected | ✅/❌ | {quality filter: are they real issues?} |
| 6 | RF completeness (§6-8) | ✅/❌ | {§6 Fact Candidates, §7 Strategic Insights, §8 Diagrams — present?} |

## Mode-Specific Checklist

{Copy items from mode file, fill with evidence}

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|

> If no KNOWLEDGE.md exists or nothing applies: "No applicable knowledge items."

## Checkpoint

**Self-check:**
- [ ] Every checklist item has evidence (not just ✅/❌)?
- [ ] Referenced verify.md findings in DoD assessment?
- [ ] Checked RF §6-8 for presence AND quality (not just existence)?
- [ ] KNOWLEDGE.md cross-referenced — contradictions documented or "None"?
- [ ] Fact Candidates from RF reviewed — any that need challenge?

Stage complete: YES / NO
```

### Step 4: Update `review.md` workflow

Replace Steps 0-4 with hardened mode gate + file-based stages:

```markdown
> **Reviewer Identity:** Quality guardian. Your job is to protect the project
> from unverified claims and incomplete work. Trust evidence, not declarations.

## Trust Protocol (Review)

| RF Claim Type | Trust Level | Reviewer Action |
|---------------|-------------|----------------|
| "Tests pass" | Verify | Re-run test command or check test file exists |
| "File modified" | Verify | Open file, confirm changes match description |
| "DoD met" (RF §3) | Verify | Cross-check each TS AC item against actual files |
| "No diagrams needed" | Challenge | Check if task had architecture/flow/state changes |
| "No fact candidates" | Challenge | Scan conversation — were there human insights? |
| Fact Candidates | Trust | Record, verify during /tfw-knowledge |
| Observations (RF §5) | Trust | Triage to TECH_DEBT.md without re-investigation |

## Step 0: Select Review Mode

Read `PROJECT_CONFIG.yaml` → `tfw.review.default_mode` (default: `code`).
Determine mode from task context:
- `code` — implementation tasks (code changes, infrastructure)
- `docs` — writing, documentation, design, content
- `spec` — analytical, research, specifications

Present: "Review mode: [{mode}]. Reason: {specific}. Switch? [code/docs/spec]"
🛑 WAIT — then load `.tfw/workflows/review/{mode}.md`.

## Step 1: Map

> **Mindset:** Student. Understand before you judge.

Create `review/` subfolder in task phase directory.
Copy `templates/review/map.md` → fill all fields.
Complete self-check gate. If any unchecked → go back and do it.

## Step 2: Verify

> **Mindset:** Auditor. The RF is a declaration, not a fact.

Copy `templates/review/verify.md` → fill verification log.
Execute verify actions from mode file.
Complete self-check gate. If any unchecked → go back and do it.

## Step 3: Judge

> **Mindset:** Judge. Evidence from Verify → rule on quality.

Copy `templates/review/judge.md` → fill checklists with evidence.
Must reference verify.md findings (not re-invent).
Complete self-check gate. If any unchecked → go back and do it.

## Step 4: Decide (Synthesize → REVIEW)

> **Mindset:** Decision-maker. Synthesize stages into a binding verdict with cited proof.

Read all 3 stage files (map.md, verify.md, judge.md).
Write `REVIEW__*.md` using `templates/REVIEW.md` — synthesize, don't copy-paste.
- §1 Map: summarize from map.md
- §2 Verify: reference verify.md findings table
- §3 Judge: summarize from judge.md checklist
- §4 Verdict: APPROVE / REVISE / REJECT with rationale citing stage evidence
```

The continuous flow (no WAIT gates) means the reviewer proceeds through all 3 stages without stopping for user approval — but MUST write each file before moving to the next.

### Step 5: Update `REVIEW.md` template header

Add stage files instruction to REVIEW.md header:

```markdown
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`
> This file is a synthesis of stage findings. Reference stage files for raw evidence.
```

### Step 6: Update `conventions.md` §3

Add review stage files to artifact types:

```markdown
Review stage files (`review/map.md`, `review/verify.md`, `review/judge.md`) — intermediate
review traces written during the review process. Created in task phase directory. Parallels
research stage files (`research/gather.md`, etc.). The REVIEW artifact synthesizes these files.
```

## 5. Acceptance Criteria

- [ ] 3 stage templates exist in `.tfw/templates/review/` (map.md, verify.md, judge.md)
- [ ] Each template has **Mindset** as a mandatory header field (not just a workflow blockquote)
- [ ] Each template has a Checkpoint section with self-check gates (checkboxes)
- [ ] verify.md self-check includes KNOWLEDGE.md contradiction check
- [ ] judge.md self-check includes evidence requirement + KNOWLEDGE.md cross-reference
- [ ] `review.md` Step 0 has 🛑 WAIT gate after mode presentation (parallels research Step 2)
- [ ] `review.md` Step 0 presents mode with "Switch? [code/docs/spec]" option
- [ ] `review.md` Steps 1-3 instruct reviewer to create `review/` folder and write stage files
- [ ] `review.md` Step 4 instructs reviewer to synthesize stage files into REVIEW artifact
- [ ] `REVIEW.md` template references stage files in header
- [ ] `conventions.md` §3 documents review stage files
- [ ] Stage file structure parallels research stage file structure (Findings → Checkpoint → Self-check)
- [ ] `review.md` has Overall Reviewer Identity statement before Step 0 (D21 pattern)
- [ ] `review.md` has Trust Protocol table for RF claim types (D27 pattern, 7 rows)

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| Review becomes too heavy for trivial tasks | Mode files already differentiate — `docs` and `spec` verify actions are lighter. Stage templates are short (~20 lines each). Total review overhead ~10 min for a serious task. |
| Reviewer fills self-check mechanically (all checked without doing the work) | Self-check items require specific evidence (file names, commands, contradiction lists). A mechanical check is visible: no evidence = not done. |

---

*TS — TFW-38 / Phase A.2: Review Stage Files + Self-Check Gates | 2026-04-14*
