# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Mode: docs
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | All 6 ACs verified in verify.md V1-V7. Each AC sub-item confirmed against actual file content. No missing items |
| 2 | Philosophy aligned | ✅ | P1 (Locality): RES.md co-located with stages ✅ (V1). P2 (Sort order): numbered files ✅ (V3). P3 (Container): single `research/` ✅ (V1). P4 (Consistent casing): phase-a ✅ (V5). P5 (Optional enrichment): agent/sources commented-out ✅ (V2). P7 (Tool-agnostic): no brand names ✅ (V4). All 6 applicable principles enforced |
| 3 | Tech debt documented | ✅ | RF §5 has 5 observations covering compilable_contract.md, handoff.md, plan.md, research/base.md, CHANGELOG.md — all relevant out-of-scope issues for Phase B/C |
| 4 | Style & standards | ✅ | Conventions.md follows existing formatting. Numbered files use consistent `N_name.md` pattern. iterations.yaml example is valid YAML with consistent indentation. Agent guidance table follows conventions.md table style |
| 5 | Observations collected | ✅ | 5 observations, all typed (naming), all with file/line references, all actionable (4 need Phase B/C update, 1 historical no-action). Quality filter passed: each would cause real broken references if left unfixed |
| 6 | RF completeness (§6-8) | ✅ | §6 Fact Candidates present ("No fact candidates."). §7 Strategic Insights present ("No strategic insights."). §8 Diagrams present ("No diagrams."). All mandatory sections present with explicit N/A content |

## Mode-Specific Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 7 | Content quality | ✅ | Clarity: section structure is logical (Research → Multi-iteration → Schema → Agent guidance → Review → Multi-phase). Accuracy: all examples use correct paths. Completeness: covers all 7 HL §5 DoD items. Tone: consistent with rest of conventions.md |
| 8 | Source verification | ✅ | Key claims traced: HL §7.2 has 7 citations, all verified to resolve in verify.md. RES iter1 D1-D7 and iter2 D8-D12 referenced in HL — consistent with schema decisions (2 fields, not 5) |

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D38: `researchN/` subfolder accumulation | Phase A establishes `research/iterN/` instead | No — D38 is being refactored by TFW-42. KNOWLEDGE.md §1 will be updated via tfw-docs after approval |
| 2 | convention.md F15: `PhaseX/` subfolders | Phase A establishes `phase-x/` instead | No — F15 records the OLD convention. Will be updated via tfw-knowledge after approval |

> Both are expected contradictions — the whole point of TFW-42 is to refactor these conventions. They will be resolved in the KNW step.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Referenced verify.md findings in DoD assessment?
- [x] Checked RF §6-8 for presence AND quality (not just existence)?
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or "None"?
- [x] Fact Candidates from RF reviewed — any that need challenge? (RF has "No fact candidates" — acceptable for a pure documentation restructuring task)

Stage complete: YES
