# TS — TFW-38 / Phase A: Review Restructure + Full Enforcement Chain

> **Date**: 2026-04-14
> **Author**: Coordinator
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)

---

## 1. Objective

Restructure the review workflow into a 4-stage cognitive flow (Map → Verify → Judge → Decide) with 3 output-type modes (code/docs/spec). Enforce §6-8 completion in handoff, Findings Map in research, and knowledge citation in plan. Close the full enforcement chain across all roles.

## 2. Scope

### In Scope
- Review workflow restructure (4 stages + mode selection)
- REVIEW template restructure to match stages
- 3 review mode files (code.md, docs.md, spec.md)
- Handoff Phase 1: KNOWLEDGE.md inconsistency check (D15)
- Handoff Phase 3: §6-8 explicit enumeration (D1/D16)
- Research Findings Map mandate (D17)
- Plan.md: knowledge citation mandate (D14)
- Anti-pattern additions to conventions.md
- PROJECT_CONFIG.yaml key for default review mode

### Out of Scope
- Diagram indexing in docs.md (Phase B)
- TS specification level guidance (parking lot — separate task)
- Adapter sync (will need tfw-update after this task)

## 3. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `.tfw/workflows/review.md` | MODIFY | Restructure: add Step 0 mode selection, restructure Steps 1-5 into 4-stage flow |
| `.tfw/templates/REVIEW.md` | MODIFY | New §1-§7: Map, Verify, Judge (mode-aware checklist), Decide, Tech Debt, Traces, Fact Candidates |
| `.tfw/workflows/review/code.md` | CREATE | Code mode: checklist items + verify actions |
| `.tfw/workflows/review/docs.md` | CREATE | Docs mode: checklist items + verify actions |
| `.tfw/workflows/review/spec.md` | CREATE | Spec mode: checklist items + verify actions |
| `.tfw/workflows/handoff.md` | MODIFY | Phase 1: add KNOWLEDGE.md to inconsistency check. Phase 3: add explicit §6-§8 enumeration |
| `.tfw/workflows/research/base.md` | MODIFY | Step 6: add Findings Map to synthesis enumeration |
| `.tfw/workflows/plan.md` | MODIFY | Step 3: add knowledge citation check + HL §4 relevant items |
| `.tfw/conventions.md` | MODIFY | §14: add 4 new anti-patterns |
| `.tfw/PROJECT_CONFIG.yaml` | MODIFY | Add `tfw.review.default_mode: code` |

**Budget:** 3 new files, 7 modifications = 10 total. Limits: max 14 files, max 8 new, max 1200 LOC. ✅

## 4. Detailed Steps

### Step 1: Restructure `review.md`

Replace current Steps 1-5 with the 4-stage flow. Keep context loading as-is. Add Step 0: Mode Selection.

**Step 0: Mode Selection** (new, insert after Context Loading):
```markdown
## Step 0: Select Review Mode

Read `PROJECT_CONFIG.yaml` → `tfw.review.default_mode` (default: `code`).
Determine mode from task context:
- `code` — implementation tasks (code changes, infrastructure)
- `docs` — writing, documentation, design, content
- `spec` — analytical, research, specifications

Present: "Review mode: [{mode}]. Reason: {why}."
Then load `.tfw/workflows/review/{mode}.md` for mode-specific checklist and verify actions.
```

**Step 1: Map** (replaces old Step 1 "Read and Understand"):
```markdown
## Step 1: Map

> **Mindset:** "Do I understand what was done?" Build a mental model before judging.

1. Read RF — what was done, decisions made, deviations from TS
2. Read TS — what was required (DoD, scope, constraints)
3. Read HL — design philosophy and architectural intent
4. Read ONB — were executor's questions/risks addressed?
5. Summarize your understanding in 2-3 sentences (write in REVIEW §1)
```

**Step 2: Verify** (new — the audit step):
```markdown
## Step 2: Verify

> **Mindset:** "Are the claims true?" Trust nothing. The RF is the executor's claim —
> your job is to check whether claims match reality.

Execute verify actions from mode file (`.tfw/workflows/review/{mode}.md`).

Record verification results in REVIEW §2 — what you checked, what you found.
If you cannot verify (no file access, no test runner) — state what you could NOT verify.
```

**Step 3: Judge** (replaces old Step 2 "Review Checklist"):
```markdown
## Step 3: Judge

> **Mindset:** "Is the quality sufficient?" Apply the checklist with evidence from Step 2.

Apply checklist from mode file. For each item: pass/fail with evidence.
Universal items (all modes):
1. DoD met? (all TS acceptance criteria)
2. Philosophy aligned (matches HL design philosophy)
3. Tech debt (shortcuts documented?)
4. Style & standards (code style, conventions)
5. Observations collected (executor reported findings)
6. RF completeness (§6-8 present — Fact Candidates, Strategic Insights, Diagrams)

Mode-specific items: from loaded mode file.
```

**Step 4: Decide** (replaces old Step 5 "Verdict"):
```markdown
## Step 4: Decide

> **Mindset:** "What's the verdict?" Synthesize Map + Verify + Judge into a decision.

Choose verdict: ✅ APPROVE / 🔄 REVISE / ❌ REJECT
Write rationale referencing specific evidence from Verify and Judge stages.
```

Keep Steps 5-7 (Tech Debt Collection, Update Traces, Knowledge Capture) largely unchanged — they are post-verdict procedural steps.

Update anti-patterns section: add reviewer-specific anti-patterns (see Step 7).

### Step 2: Restructure `REVIEW.md` template

New section structure:

```markdown
## 1. Map
{2-3 sentence summary of understanding: what was done, key decisions, scope}

## 2. Verify
| # | What was checked | Result | Evidence |
|---|-----------------|--------|----------|

> If verification was limited (no file access, etc.): state what could NOT be verified.

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅/❌ | {specific} |
| 2 | Philosophy aligned | ✅/❌ | |
| 3 | Tech debt documented | ✅/❌ | |
| 4 | Style & standards | ✅/❌ | |
| 5 | Observations collected | ✅/❌ | |
| 6 | RF completeness (§6-8) | ✅/❌ | |
| {mode-specific items from mode file} |

## 4. Verdict

**{✅ APPROVE / 🔄 REVISE / ❌ REJECT}**

{Rationale referencing §2 Verify and §3 Judge evidence}

### If REVISE — items to fix:
### If REJECT — fundamental issues:

## 5. Tech Debt Collected
{Same as current §3}

## 6. Traces Updated
{Same as current §4}

## 7. Fact Candidates
{Same as current §5}
```

### Step 3: Create review mode files

Create `.tfw/workflows/review/` directory with 3 files.

**code.md:**
```markdown
# Review Mode: code

## Verify Actions
1. Open 2-3 files from RF §1 (What Was Done) → verify changes exist and match description
2. Check RF §4 (Verification) → re-run at least 1 build/test command if possible
3. Cross-reference RF §3 (Acceptance Criteria) checkmarks against TS DoD
4. If "Tests pass" claimed → check test file exists and covers stated scenarios

## Mode-Specific Checklist Items
| # | Check | Description |
|---|-------|-------------|
| 7 | Code quality | Conventions, naming, type hints |
| 8 | Test coverage | Tests written and passing per TS |
| 9 | Security | No secrets exposed, guards in place |
| 10 | Breaking changes | API compat, backward compat, migrations |
```

**docs.md:**
```markdown
# Review Mode: docs

## Verify Actions
1. Verify deliverable files exist at stated paths
2. Check document structure matches spec (headings, required sections)
3. Spot-check 2-3 key claims/sources for accuracy

## Mode-Specific Checklist Items
| # | Check | Description |
|---|-------|-------------|
| 7 | Content quality | Clarity, accuracy, completeness, tone |
| 8 | Source verification | Key claims traceable to sources |
```

**spec.md:**
```markdown
# Review Mode: spec

## Verify Actions
1. Verify deliverable files exist at stated paths
2. Check source citations are traceable to real artifacts
3. Verify data claims against primary sources where possible

## Mode-Specific Checklist Items
| # | Check | Description |
|---|-------|-------------|
| 7 | Analytical quality | Logic, completeness, methodology |
| 8 | Source attribution | Claims traceable to evidence |
```

### Step 4: Update `handoff.md` Phase 3

In Phase 3 "Write RF" (line 73), replace the current bullet list with explicit §1-§8 enumeration:

```markdown
12. **Create RF file** — use `.tfw/templates/RF.md` as canonical format. MANDATORY sections:
    - **§1 What Was Done** — changes list with file paths
    - **§2 Key Decisions** — decisions and rationale
    - **§3 Acceptance Criteria** — checkmark each TS DoD item
    - **§4 Verification** — lint/test/verify results
    - **§5 Observations** — out-of-scope items noticed (table format). Quality bar: only issues that would bite the next developer.
    - **§6 Fact Candidates** — review conversation history, extract human-sourced knowledge. If none: "No fact candidates."
    - **§7 Strategic Insights** — capture domain knowledge with implications. If none: "No strategic insights."
    - **§8 Diagrams** — architecture, data flow, component interaction. If none: "No diagrams."
    Never omit §6-8. Empty content is acceptable ("No X."); absent section is not.
```

In Phase 1 "Executor Onboarding" (line 36), add KNOWLEDGE.md to the inconsistency check bullet:

Current:
```markdown
   - Inconsistencies between HL/TS and actual code
```

Replace with:
```markdown
   - Inconsistencies between HL/TS/KNOWLEDGE.md and actual code
```

### Step 5: Update `research/base.md` Step 6

In Step 6 "Synthesis" (line 86-93), add Findings Map to the enumerated list. Current line 91 reads:
```
4. Fact Candidates — review conversation history first
```

After line 91, add:
```
5. **Findings Map** — visualize research findings (root cause, hypothesis trees, priority matrices). If no visualization relevant: "No findings map."
```

Renumber subsequent items (old 5→6 Iteration Status, old 6→7 Conclusion).

### Step 6: Update `conventions.md` §14

Add 4 new anti-patterns:

```markdown
- Reviewer approves without opening any files — Step 2 (Verify) requires spot-checking RF claims against actual artifacts
- Executor omits RF §6-8 (Fact Candidates, Strategic Insights, Diagrams) — sections are mandatory; empty content ("No X.") is valid, absent section is not
- Researcher omits Findings Map in RES — section is mandatory; "No findings map." is valid if genuinely no visualization relevant
- Coordinator reads KNOWLEDGE.md in context loading but never cites relevant items in HL §4 — "read but don't use" pattern breaks cross-task knowledge flow
```

### Step 7: Update `plan.md` Step 3

In Step 3 "Research & Understand" (line ~20), add a knowledge citation sub-step after "Study references":

```markdown
4. **Check KNOWLEDGE.md** — scan Architecture Decisions, known conventions, and prior task findings.
   If any are relevant to this task, cite them in HL §4 (Phase Context). If none apply: write "No applicable knowledge items."
```

### Step 8: Update `PROJECT_CONFIG.yaml`

Add under `tfw:` section:

```yaml
  review:
    default_mode: code        # code / docs / spec — determines review checklist
```

## 5. Acceptance Criteria

- [ ] `review.md` has Step 0 (mode selection) + Steps 1-4 (Map, Verify, Judge, Decide)
- [ ] `REVIEW.md` template has §1-§7 structure (Map, Verify, Judge, Verdict, Tech Debt, Traces, Fact Candidates)
- [ ] 3 mode files exist in `.tfw/workflows/review/` with mode-specific checklists and verify actions
- [ ] `handoff.md` Phase 1 includes KNOWLEDGE.md in inconsistency check; Phase 3 explicitly enumerates §1-§8 with "never omit §6-8"
- [ ] `research/base.md` Step 6 includes Findings Map in synthesis enumeration
- [ ] `plan.md` Step 3 includes knowledge citation check with explicit N/A option
- [ ] `conventions.md` §14 has 4 new anti-patterns (reviewer no-verify, executor §6-8 skip, researcher no-map, coordinator no-cite)
- [ ] `PROJECT_CONFIG.yaml` has `tfw.review.default_mode: code`
- [ ] All workflows stay under 1200 words
- [ ] Mode files don't duplicate universal checklist items

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| review.md exceeds 1200 words after restructure | Mode files carry differential items; main workflow references them. Stage descriptions are concise (3-5 lines each). |
| Template-workflow section mismatch | §-numbers in REVIEW.md template MUST match stage names in review.md workflow (Map=§1, Verify=§2, Judge=§3, Decide=§4). |

---

*TS — TFW-38 / Phase A: Review Restructure + Full Enforcement Chain | 2026-04-14*
