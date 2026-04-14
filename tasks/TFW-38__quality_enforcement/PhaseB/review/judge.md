# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Mode: docs
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | All 9 TS acceptance criteria verified against actual files (verify.md V1-V7). One minor deviation in V3 (preserve+extend vs replace) — documented, defensible, net improvement. |
| 2 | Philosophy aligned | ✅ | HL §7 P6 Knowledge Gate enforced: cascade model (coord→executor→reviewer) implements the "hard gate" principle. Naming unified per D28/D39: "Knowledge Citations" everywhere (one cognitive mode = one name). Bootstrap N/A documented per S8 "explicit N/A" pattern. |
| 3 | Tech debt documented | ✅ | RF §5 Observations: 2 items (#1 heading hierarchy, #2 multi-line bullet format). Both style-type, low severity. Quality bar met — real maintainability concerns, not filler. |
| 4 | Style & standards | ✅ | Template instructions use blockquote format consistent with existing §7.1 Quality Contract. Table column counts match TS spec (4-col HL, 5-col ONB, 5-col verify). Section numbering clean (HL: 7.2, ONB: 7, verify: subsection). |
| 5 | Observations collected | ✅ | 2 observations in RF §5 — both genuine style items. No filler. |
| 6 | RF completeness (§6-8) | ✅ | §6 Fact Candidates: 2 entries with source+confidence. §7 Strategic Insights: "No strategic insights." §8 Diagrams: "No diagrams." All three sections present with content or explicit N/A. |

## Mode-Specific Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 7 | Content quality | ✅ | Instructions in all 3 templates are clear, actionable, role-specific. PV scan instruction in plan.md specifies priority tiers (full 1-4, skim 5-7) — not a vague "check knowledge." ONB template distinguishes "confirm read" from "how applied" — granular executor accountability. verify.md explicitly handles the N/A case ("No applicable knowledge items → write N/A"). |
| 8 | Source verification | ✅ | RF traces all decisions to ONB Q&A (coordinator answers Q1, Q2). Cascade model maps to HL §4 Phase B design rationale. Fact Candidates (#1, #2) cite user answers with direct quotes. |

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D28: Naming > Explanation | Table name unified: "Knowledge Citations" | No — consistent application of D28 |
| 2 | D39: Per-template naming for different cognitive modes, unified for same | "Knowledge Citations" same name across HL/ONB/verify.md | No — cognitive mode is same ("report what you read"), so unified name is correct per D39 |
| 3 | D24: Pattern A (inline defaults + config key) | No config key needed — citation is a template section, not a configurable parameter | No contradiction — D24 applies to numeric budgets, not template sections |

> No contradictions found.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Referenced verify.md findings in DoD assessment?
- [x] Checked RF §6-8 for presence AND quality (not just existence)?
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or "None"?
- [x] Fact Candidates from RF reviewed — any that need challenge?

> RF Fact Candidates review: FC#1 (user prefers clean replacement over amendment) — genuine strategic insight about cross-phase instruction management. FC#2 (user prefers semantic grouping over numbering granularity) — genuine process pattern. Both high-confidence, specific to user decision-making style. No challenge needed.

Stage complete: YES
