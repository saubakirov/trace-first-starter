# RES — TFW-38: Quality Enforcement (Iteration 2)

> **Date**: 2026-04-14
> **Author**: Researcher
> **Status**: 🔬 RES — Complete
> **Parent HL**: [HL-TFW-38](HL-TFW-38__quality_enforcement.md)
> **Predecessor**: [RES iteration 1](RES__TFW-38__quality_enforcement.md)
> **Mode**: Pipeline

---

## Research Context

Iteration 2 explores the user's direction that review should be structured with domain-specific stages (like research has gather/extract/challenge), not a single-pass checklist. Resolves all open threads from iteration 1: staged review design, mode system, workflow classification, and diagram indexing format.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D6 | **4-stage review flow: Comprehend → Verify → Assess → Synthesize** | ISO verification/validation model mapped to TFW. Natural stages already appear in the best REVIEW files (HD PhaseF, TFW-19, TFW-36). Each stage has a distinct cognitive mindset: passive understanding → active audit → analytical judgment → decision-making. |
| D7 | **3 review modes: `code`, `prose`, `spec`** | Current 9-point checklist is 44% code-specific. Steps-framework is 60% non-code tasks. Mode describes output type, not domain. Configures Assess-stage checklist items. Same selection pattern as research modes (focused/deep). |
| D8 | **Stages are sections in REVIEW artifact, not separate files** | Review is single-pass (no OODA loops). Creating stage files would add overhead for no value. ONB proves sections-in-one-file CAN enforce cognitive transitions if workflow describes mindset per section. Key difference from research: stages flow sequentially without WAIT gates. |
| D9 | **REVIEW template must restructure to match 4-stage flow** | Iteration 1 root cause: template-workflow disconnect causes skipping. Template and workflow MUST change together. New template: §1 Comprehend → §2 Verify → §3 Assess → §4 Verdict → §5 Tech Debt → §6 Traces → §7 Fact Candidates. |
| D10 | **Diagram collection = indexing in KNOWLEDGE.md §2, not copying** | Confirmed from iteration 1 D3. Format: table with Description, Location (RF/RES path + section), Type (mermaid/ASCII), Date. Collection triggered in docs.md after APPROVE. |

## Hypothesis Status

| # | Hypothesis | Iter 1 | Iter 2 | Evidence |
|---|-----------|--------|--------|----------|
| H1 | Explicit §6-8 enumeration stops skipping | 🟢 | 🟢 (no change) | 96-100% skip rate confirmed empirically |
| H2 | Audit step changes reviewer behavior | 🟢 | 🟢 superseded by H3 | Audit step is now stage 2 (Verify) in the 4-stage model |
| H3 | Domain-specific review stages produce more reliable reviews | — | 🟢 supported | 4-stage model maps to ISO V&V. 3 modes handle task type diversity. 44% code-specific checklist items → mode eliminates N/A friction. Stages-as-sections pragmatism (D8) prevents overhead. |

## Staged Review Design Summary

### Flow

```
┌─────────────┐    ┌──────────┐    ┌──────────┐    ┌─────────────┐
│ COMPREHEND  │ →  │  VERIFY  │ →  │  ASSESS  │ →  │ SYNTHESIZE  │
│ "Understand │    │ "Check   │    │ "Judge   │    │ "Decide and │
│  claims"    │    │  evidence"│    │  quality" │    │  capture"   │
└─────────────┘    └──────────┘    └──────────┘    └─────────────┘
   Read RF/TS/HL     Open files      Checklist       Verdict + 
   Build mental      Spot-check      (mode-aware)    Tech Debt +
   model             Re-run tests    Philosophy      Fact Candidates
                     Check evidence  Standards       Traces
```

### Mode Checklist Configuration

| # | Check | `code` | `prose` | `spec` |
|---|-------|--------|---------|--------|
| 1 | DoD met? | ✅ | ✅ | ✅ |
| 2 | Quality | Code quality | Content quality | Analytical quality |
| 3 | Coverage | Test coverage | Source verification | Source attribution |
| 4 | Philosophy aligned | ✅ | ✅ | ✅ |
| 5 | Tech debt | ✅ | ✅ | ✅ |
| 6 | Domain gate A | Security | NDA compliance | — |
| 7 | Domain gate B | Breaking changes | — | — |
| 8 | Style & standards | ✅ | ✅ | ✅ |
| 9 | Observations collected | ✅ | ✅ | ✅ |
| 10 | RF completeness (§6-8) | ✅ | ✅ | ✅ |

**Universal (all modes):** 6 items (#1, #4, #5, #8, #9, #10)
**Mode-specific:** 2-4 items → total per review: 8-10

### Verify Stage Actions by Mode

| Mode | Verify actions |
|------|---------------|
| `code` | Open 2-3 files from RF §1, verify changes exist. Check test file presence. Re-run 1 test/build if possible. Cross-reference AC checkmarks against TS DoD. |
| `prose` | Verify deliverable files exist. Check structure matches spec. Check key sources/citations. |
| `spec` | Verify deliverable files exist. Check source citations are traceable. Verify data claims against primary sources. |

### Key Design Distinction from Research

| | Research | Review |
|-|---------|--------|
| Stage files | Separate files (gather.md, extract.md, ...) | Sections in REVIEW artifact |
| OODA loops | Multiple per stage | None — single pass |
| WAIT gates | Between each stage | None — continuous flow |
| Purpose | Accumulate knowledge iteratively | Apply judgment once |
| Output | RES artifact | REVIEW artifact |
| Mode timing | Per-iteration | Per-review |

## HL Update Recommendations

| # | What to update | Source |
|---|---------------|--------|
| 1 | Phase A scope: add REVIEW template restructure (§1-§7 renumbering) alongside review.md workflow changes | D9 |
| 2 | Phase A scope: add `review/` mode files (code.md, prose.md, spec.md) to `.tfw/workflows/review/` | D7 |
| 3 | Phase A scope: add Step 0 (mode selection) to review.md | D7 |
| 4 | Phase B D6: diagram indexing format decided — table in KNOWLEDGE.md §2 | D10 |
| 5 | Rename Phase A from "Workflow & Template Enforcement" to "Review Restructure + Handoff Enforcement" | D6-D9 broaden Phase A scope |
| 6 | Add H3 to HL §10 | H3 |

## Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| F6 | philosophy | Review stages should be sections in a single artifact (not separate files) because review is single-pass, unlike research which iterates. The cognitive transition comes from the workflow's mindset descriptions, not from file boundaries. ONB is proof: sections-in-one-file enforce cognitive transitions when the workflow explicitly describes the mindset per section. | D8, Challenge C1 | High |
| F7 | philosophy | User's "like research but not research" direction means: review should have structured cognitive phases with different goals per phase, but without the OODA loops, WAIT gates, and iteration mechanism that research uses. The structural parallel is in forced mindset transitions, not in process mechanics. | User, 2026-04-14 | High |
| F8 | convention | Review mode names should describe the output type being reviewed (code/prose/spec), not the domain (business/education/transit). Output-type naming is finite and domain-agnostic; domain naming creates infinite modes. | Challenge C4 | High |
| F9 | process | Current REVIEW checklist is 44% code-specific (4 of 9 items). Non-code tasks generate 4 N/A entries per review. Mode-specific checklists eliminate this friction while keeping 6 universal items. | Gather G3 | High |

## Iteration Status

- **Iteration:** 2 of 2 (min) / 3 (max)
- **Hypotheses tested:** H1 (🟢), H2 (🟢 → superseded by H3), H3 (🟢)
- **Hypotheses deferred:** None
- **Gaps discovered:** None
- **Superseded decisions:** D2 (audit step) → superseded by D6 (staged review with Verify as stage 2)

### Open Threads

| # | Thread | Status |
|---|--------|--------|
| 1 | Staged review workflow | ✅ Resolved — D6, D7, D8, D9 |
| 2 | Two classes of TFW workflows | ✅ Resolved — review gets staged structure, handoff/docs stay procedural |
| 3 | Diagram indexing format | ✅ Resolved — D10 |

### Recommendation
- [x] **SUFFICIENT** — proceed to `/tfw-plan` to update HL and write TS
- [ ] **MORE NEEDED**

All open threads from iteration 1 are resolved. The staged review design (D6-D9) is concrete enough for TS. Handoff enforcement (D1, D4) was ready since iteration 1. Diagram indexing (D10) format is defined.

## Conclusion

Iteration 2 designed a 4-stage domain-agnostic review flow (Comprehend → Verify → Assess → Synthesize) with 3 output-type modes (`code`, `prose`, `spec`). The design maintains TFW's domain independence by naming modes after output types, not domains. Stages live as sections within the existing REVIEW artifact (no separate files) — the cognitive transition is enforced by the workflow's explicit mindset descriptions, not file boundaries. Combined with iteration 1's confirmed enforcement fixes (§6-8 enumeration in handoff.md, Findings Map mandate in research/base.md), TFW-38 has a complete research foundation for TS specification.

---

*RES — TFW-38: Quality Enforcement (Iteration 2) | 2026-04-14*
