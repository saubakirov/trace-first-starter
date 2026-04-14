# Extract — "What do we NOT see?"
> Parent: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> Goal: Concrete review stage design, mode system, checklist decomposition, diagram index format.

## Findings

### E1: Review Stage Specification

**Proposed 4-stage review flow:**

```
COMPREHEND → VERIFY → ASSESS → SYNTHESIZE
   (read)     (audit)  (judge)   (decide)
```

#### Stage 1: Comprehend
**Mindset:** "Understand before judging."
- Read RF, TS, HL (current Step 1 — no change needed)
- Output: mental model of what was done, why, and how

#### Stage 2: Verify
**Mindset:** "Trust nothing. Check evidence."
- Open 2-3 files from RF §1 → do the changes exist?
- If RF §4 claims "tests pass" → verify test file exists, re-run if possible
- Cross-reference RF §3 (AC) checkmarks against TS DoD
- For docs tasks: verify deliverable files exist, check structure matches spec
- Output: verification evidence (line numbers, command output, file existence)

#### Stage 3: Assess
**Mindset:** "Apply domain standards."
- Run domain-relevant checklist items (universal + mode-specific)
- Check RF §6-8 completeness
- Judge philosophy alignment, style, standards
- Output: checklist with evidence, not just ✅/❌

#### Stage 4: Synthesize
**Mindset:** "Decide and capture."
- Write verdict (APPROVE / REVISE / REJECT) with rationale
- Triage executor observations → tech debt
- Capture fact candidates from review process
- Update traces (Task Board, TECH_DEBT.md)
- Output: complete REVIEW artifact

### E2: Review Modes (paralleling research modes)

Like research has `focused` / `deep`, review needs domain modes that configure the Assess stage checklist.

**Proposed mode structure:**

```yaml
# In PROJECT_CONFIG.yaml
tfw:
  review:
    default_mode: standard  # standard | content | analytical
    modes:
      standard:
        description: "Code/implementation tasks"
        checklist_items:
          - dod_met
          - code_quality
          - test_coverage
          - philosophy_aligned
          - tech_debt
          - security
          - breaking_changes
          - style_and_standards
          - observations_collected
          - rf_completeness
        verify_depth: "spot-check 2-3 files, re-run 1 test"
      content:
        description: "Writing, documentation, design spec tasks"
        checklist_items:
          - dod_met
          - content_quality  # replaces code_quality
          - source_verification  # replaces test_coverage
          - philosophy_aligned
          - tech_debt
          - style_and_standards
          - observations_collected
          - rf_completeness
        verify_depth: "verify deliverable existence, check structure"
      analytical:
        description: "Research output, analytical specs, positioning"
        checklist_items:
          - dod_met
          - analytical_quality  # replaces code_quality
          - source_attribution  # replaces test_coverage
          - philosophy_aligned
          - tech_debt
          - style_and_standards
          - observations_collected
          - rf_completeness
        verify_depth: "verify deliverable existence, check source citations"
```

**Mode selection:** Reviewer picks mode at Step 0 based on task type. Same pattern as research mode selection.

### E3: Checklist Decomposition Into Universal + Mode-Specific

| # | Check | Universal | Standard (code) | Content (writing) | Analytical |
|---|-------|-----------|-----------------|--------------------| -----------|
| 1 | DoD met? | ✅ | ✅ | ✅ | ✅ |
| 2 | {quality} | — | Code quality | Content quality | Analytical quality |
| 3 | {coverage} | — | Test coverage | Source verification | Source attribution |
| 4 | Philosophy aligned | ✅ | ✅ | ✅ | ✅ |
| 5 | Tech debt | ✅ | ✅ | ✅ | ✅ |
| 6 | {domain gate} | — | Security | NDA compliance | — |
| 7 | {domain gate} | — | Breaking changes | — | — |
| 8 | Style & standards | ✅ | ✅ | ✅ | ✅ |
| 9 | Observations collected | ✅ | ✅ | ✅ | ✅ |
| 10 | RF completeness (§6-8) | ✅ | ✅ | ✅ | ✅ |

**Universal (all modes):** #1, #4, #5, #8, #9, #10 = 6 items
**Mode-specific:** #2, #3, #6, #7 = 2-4 items depending on mode

Total per review: 8-10 items. Within the <10 constraint budget.

### E4: Stage Files vs Single REVIEW Artifact

**Option A: Separate stage files** (like research/)
```
review/
  comprehend.md  ← notes from reading
  verify.md      ← evidence collected
  assess.md      ← checklist results
REVIEW__*.md     ← final synthesis
```

**Option B: Stages as sections within REVIEW** (no separate files)
```
REVIEW__*.md
  §1. Comprehend (summary of what was reviewed)
  §2. Verify (evidence table)
  §3. Assess (checklist)
  §4. Verdict
  §5. Tech Debt
  ...
```

**Analysis:**
- Research stage files serve a purpose: they accumulate over OODA loops and get synthesized. Review doesn't loop — it's a single pass through each stage.
- Creating 3 extra files per review adds overhead for a single-pass process.
- The REVIEW template already has sections that map to stages naturally.
- BUT: the staged mindset is what matters, not the file structure. The workflow can enforce stages by ordering Steps differently and adding mindset blocks.

**Verdict: Option B (sections in REVIEW) is better.** The workflow enforces the cognitive mode transitions through step ordering and mindset blocks. The REVIEW artifact captures everything in one place. No extra files.

### E5: Diagram Index Format for KNOWLEDGE.md

**Proposed format for KNOWLEDGE.md §2 (Key Artifacts):**

```markdown
### Diagrams Index

| # | Description | Location | Type | Created |
|---|-------------|----------|------|---------|
| 1 | Auth flow sequence diagram | RF Phase H §8 | mermaid sequence | 2026-04-14 |
| 2 | RLS policy evaluation tree | RES iter1 Findings Map | ASCII | 2026-04-14 |
| 3 | ETL pipeline data flow | RF Phase F §8 | mermaid flowchart | 2026-04-13 |
```

**Collection rule in docs.md:** After each REVIEW with ✅ APPROVE, check RF §8 and RES Findings Map. If non-trivial diagrams exist, add reference to KNOWLEDGE.md §2 Diagrams Index.

### E6: Word Budget Impact of Staged Review

Current review.md: 816 words.

Estimated staged review.md:
- Step 0: Mode selection (like research Step 2): ~30 words
- Step 1: Comprehend (current Step 1, minor additions): ~10 words added
- Step 2: Verify (new — mindset block + verification actions): ~80 words
- Step 3: Assess (current Step 2, reformulated with mode reference): ~20 words added
- Step 4: Synthesize (current Steps 3-7 compressed): ~0 (restructure, no net addition)
- Step 5: checklist item #10 addition: ~10 words

**Total estimated: 816 + ~150 = ~966 words.** Well within 1200 budget.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| 4-stage model: Comprehend → Verify → Assess → Synthesize | None |
| 3 review modes: standard, content, analytical | Naming needs validation |
| Stages as REVIEW sections, not separate files | None |
| 6 universal + 2-4 mode-specific checklist items | None |
| Diagram index format for KNOWLEDGE.md | None |
| Word budget: ~966/1200 after changes | None |

**Sufficiency:**
- [x] External source used? (ISO verification/validation model applied in Gather)
- [x] Briefing gap closed? (Concrete stage design, mode system, checklist decomposition complete)

Stage complete: YES
→ User decision: ___
