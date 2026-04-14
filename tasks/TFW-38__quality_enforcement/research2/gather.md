# Gather — "What do we NOT know?"
> Parent: [HL-TFW-38](../HL-TFW-38__quality_enforcement.md)
> Goal: Evidence for domain-agnostic review stages and review modes.

## Findings

### G1: External — Universal Quality Gate Stages (Domain-Independent)

ISO 9001 and industry QA frameworks identify three universal quality activities:

| Activity | Question | Domain-Independent? |
|----------|----------|---------------------|
| **Verification** | "Are we building the product right?" = process check | ✅ Yes — applies to code, docs, research, design |
| **Validation** | "Are we building the right product?" = outcome check | ✅ Yes — applies everywhere |
| **Conformance** | Does it match standards/requirements? | ✅ Yes — universal |

Industry standard quality gate progression:
1. **Requirements Gate** → does output match spec?
2. **Quality Gate** → does output meet internal standards?
3. **Acceptance Gate** → does output fulfill end-user needs?

These are NOT code-centric. "Requirements" could be TS acceptance criteria, design requirements, or content specs. "Quality" could be code conventions, writing style, or pedagogical standards.

### G2: Natural Stages in Real TFW REVIEW Files

Analyzing the best REVIEW files, natural stages emerge:

**HD-3 PhaseF REVIEW (code task, 103 lines):**
1. Read — checklist with evidence (§1)
2. Acceptance Criteria Audit — line-by-line AC verification (§2)
3. Tech Debt Collection — triage observations (§3)
4. Process Verdict — scope budget, artifacts, discipline (§4)
5. Fact Candidates (§5)
6. Final Verdict

**HD-2 Phase0 REVIEW (document task, 76 lines):**
1. Read — checklist with N/A for code-centric items (§1)
2. AC verification detail (inline)
3. Tech Debt (§3)
4. Traces (§4)
5. Fact Candidates — "none" (§5)

**Pattern:** Both follow the same structure but the CODE review has deeper verification (line numbers, formula checks). The DOC review marks code-centric items as N/A.

### G3: Current 9-Point Checklist — Domain Analysis

| # | Check | Code | Docs | Research | Design |
|---|-------|------|------|----------|--------|
| 1 | DoD met? | ✅ always | ✅ always | ✅ always | ✅ always |
| 2 | Code quality | ✅ core | N/A | N/A | N/A |
| 3 | Test coverage | ✅ core | N/A | N/A | N/A |
| 4 | Philosophy aligned | ✅ always | ✅ always | ✅ always | ✅ always |
| 5 | Tech debt | ✅ always | ✅ always | ✅ always | ✅ always |
| 6 | Security | ✅ conditional | N/A | N/A | N/A |
| 7 | Breaking changes | ✅ conditional | N/A | N/A | N/A |
| 8 | Style & standards | ✅ always | ✅ partial | ✅ partial | ✅ partial |
| 9 | Observations collected | ✅ always | ✅ always | ✅ always | ✅ always |

**Universal items (all domains):** #1 DoD, #4 Philosophy, #5 Tech debt, #8 Style, #9 Observations = 5 items
**Code-specific items:** #2 Code quality, #3 Tests, #6 Security, #7 Breaking changes = 4 items

The checklist is ~44% code-specific. For non-code tasks, reviewers write "N/A" for 4 items = friction.

### G4: Review Stage Candidates (Domain-Agnostic Naming)

Mapping ISO verification/validation/conformance to TFW review context:

| Stage | Cognitive Mode | What Reviewer Does | Parallel to Research |
|-------|---------------|--------------------|-----------------------|
| **Comprehend** | Passive understanding | Read RF, TS, HL. Understand what was done and why. Answer: "Do I understand the claims?" | Briefing |
| **Verify** | Active audit | Open deliverables. Spot-check RF claims against reality. Run one test/build if code. Check deliverable existence if docs. Answer: "Are the claims true?" | Gather |
| **Assess** | Analytical judgment | Apply domain-relevant checklist. Judge quality, standards, philosophy alignment. Answer: "Is the quality sufficient?" | Extract |
| **Synthesize** | Decision-making | Write verdict, collect tech debt, capture facts. Answer: "What's the verdict and what did we learn?" | Challenge + RES |

This is a 4-stage model:
- **Comprehend** = read and understand (current Step 1)
- **Verify** = audit (the missing step from iteration 1)
- **Assess** = checklist + judgment (current Step 2, but with domain-aware items)
- **Synthesize** = verdict + traces (current Steps 3-7 compressed)

## Checkpoint

| Found | Remaining |
|-------|-----------|
| ISO verification/validation/conformance model is universal | None |
| Current checklist is 44% code-specific — needs domain config | None |
| 4-stage model: Comprehend → Verify → Assess → Synthesize | Needs classification of what "Verify" means per domain |
| Natural stages already emerge in best REVIEW files | None |

**Sufficiency:**
- [x] External source used? (ISO 9001, QA gate frameworks)
- [x] Briefing gap closed? (Domain-agnostic stages designed)

Stage complete: YES
→ User decision: ___
