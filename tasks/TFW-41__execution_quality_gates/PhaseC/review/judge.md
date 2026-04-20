# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Mode: docs
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | All 5 ACs verified against actual files (verify.md V1-V5). All TS §7 DoF conditions avoided. See verify.md — zero content discrepancies. |
| 2 | Philosophy aligned | ✅ | P1 (Gates over guidelines): cross-stage dependency in extract.md column headers is a structural gate, not a checkbox. P6 (Domain-agnostic): no methodology names in researcher-facing text — grep confirms 0 Zwicky hits. P5 (Executor as engineer): workflow thread gives connecting logic, not copy-paste instructions. All HL §7 principles with mapped ACs enforced. |
| 3 | Tech debt documented | ✅ | RF §5 Observations table present: 1 item — briefing.md has no reference to Dimensions section. Real issue, specific file, concrete mitigation path. Quality-filtered: not filler. |
| 4 | Style & standards | ✅ | Heading hierarchy consistent (## Dimensions, ## Configuration Space, ## Consistency Check match section naming convention). Terminology: TFW-native throughout researcher-facing files. Conventions §14.1 heading uses consistent numbering style (`### 14.1`, matching existing `### Hard Stop Rule` pattern in §15). §15 Role Lock section number preserved. |
| 5 | Observations collected | ✅ | 1 genuine observation (briefing.md gap). Executor correctly flagged as Phase D candidate. Not over-reported. |
| 6 | RF completeness (§6-8) | ✅ | §6 Fact Candidates: present — "No fact candidates" with clear rationale (pure executor phase, no human domain knowledge). §7 Strategic Insights: present — "No strategic insights" with rationale. §8 Diagrams: present — cross-stage dependency flow diagram included, adds real explanatory value. All three sections exist. |

## Mode-Specific Checklist Items (docs)

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 7 | Content quality | ✅ | Template instructions are clear and actionable: Gather uses "Do NOT mark any alternative as 'recommended'" (explicit prohibition), Extract uses "Do NOT evaluate yet" (explicit prohibition), Challenge uses guiding question format ("Can X coexist with Y?"). Inline example in extract.md overflow note anchors the pruning rule concretely. Graceful degradation notes appear consistently across all 3 templates. |
| 8 | Source verification | ✅ | Key claim: "grep Zwicky → 0 results" — verified by reviewer independently (verify.md V1, V4). Key claim: "§15 numbering preserved" — verified in conventions.md (lines 405+). Key claim: "cross-stage dependency mechanism" — verified: Extract column headers use `{D1 from Gather}` placeholder format, enforcing dependency structurally (verify.md V2). |

## Contradictions with KNOWLEDGE.md

> KNOWLEDGE.md exists at project root. The TFW v3 knowledge item (trace_first_workflow_v3_standard) covers artifacts (HL, TS, ONB, RF, REVIEW), Role Lock, and Scope Budgets. It does not cover research templates or dimensional analysis.

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | TFW v3 KI: research/base.md uses OODA loop per stage | Phase C adds introductory paragraph BEFORE the OODA heading, not inside it | No contradiction — additive, preserves OODA structure |
| 2 | TFW v3 KI: Scope Budget ≤7 files per phase (KI says v3 default) | 5 modifications, 0 new files | No contradiction — within budget. Note: project_config.yaml overrides to 14 files; either way compliant. |

No contradictions found.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Referenced verify.md findings in DoD assessment?
- [x] Checked RF §6-8 for presence AND quality (not just existence)?
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or "None"?
- [x] Fact Candidates from RF reviewed — any that need challenge? (None to challenge — "No fact candidates" rationale is sound: pure executor phase)

Stage complete: YES
