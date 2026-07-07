# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Mode: code
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | All 6 ACs verified against actual files (verify.md V1-V12). AC-1 through AC-6 all match TS requirements. One minor stale ref found (RF.md line 68: `§5 Observations` should be `§6`) — cosmetic, doesn't affect AC fulfillment |
| 2 | Philosophy aligned | ✅ | P1 (real over synthetic): Evidence concept cleanly separates §4 synthetic from §5 real — verified in conventions.md §3 (V1). P2 (honest incompleteness): DEFERRED/BLOCKED/N/A in vocabulary — verified in RF template (V3). P3 (coordinator designs, executor collects): role pipeline in conventions.md + TS Evidence field + RF §5 — verified (V1, V2, V3). P4 (domain-agnostic): no code-specific examples in any template — verified (V1-V5). P5 (proportional): Evidence field supports N/A/empty — verified (V2). P7 (artifacts over claims): §14 anti-patterns enforce artifact references — verified (V1) |
| 3 | Tech debt documented | ✅ | RF §6 Observations has 3 items: (1) compilable_contract.md pre-existing REVIEW §5/§7 error, (2) glossary.md stale RF §7 ref (Phase C scope), (3) HL.md §9 Diagrams hint style note. All are real issues, properly scoped |
| 4 | Style & standards | ⚠️ | Overall good: naming follows conventions, Evidence Sections table follows D39 per-template pattern, anti-patterns follow existing format. One style issue: RF.md line 68 stale ref `§5 Observations` — inconsistent with §8 SI ref on line 69 which was correctly updated to §8. This indicates incomplete find-and-replace within the same instruction block |
| 5 | Observations collected | ✅ | 3 observations, all substantive: (1) pre-existing compilable_contract bug, (2) glossary stale ref correctly deferred to Phase C, (3) HL.md style note. Quality filter passes — these are real issues that would affect the next developer |
| 6 | RF completeness (§7-9) | ✅ | §7 Fact Candidates: "No fact candidates." — present, explicit N/A. §8 Strategic Insights: "No strategic insights." — present, explicit N/A. §9 Diagrams: "No diagrams." — present, explicit N/A. All sections present with explicit N/A per F21 pattern |
| 7 | Evidence completeness | ✅ | All 6 TS Evidence fields are `N/A` (conventions/template spec — validation is when users write real TS/RF with the new fields). RF §5 correctly mirrors this with 6/6 VERIFIED using local file references. Appropriate for a template-only task |

## Mode-Specific Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 7 | Code quality | ✅ | Markdown templates follow existing conventions. Evidence Sections table in conventions.md §3 follows the same pattern as Visual Sections and Knowledge Capture tables (4 columns: Template, Section, Cognitive Mode, What it produces). Anti-patterns follow existing format. TS Evidence field instruction block is clear and concise |
| 8 | Test coverage | N/A | No executable tests for `.tfw/` markdown. Executor ran 2 grep commands for reference validation |
| 9 | Security | ✅ | No secrets, no external access. Framework template changes only |
| 10 | Breaking changes | ⚠️ | RF section renumbering (§5-8 → §6-9) is a breaking change for any existing project RF files that reference old numbers. TS §8 Phase Risks acknowledges this: "Renumbering applies only to `.tfw/` templates and workflows. Existing project RFs keep their numbering until next task." Mitigated by scope — only template/workflow files updated, not user project files |

## HL §7 Principles Check

| # | Principle | Mapped AC | AC met? | Evidence |
|---|-----------|-----------|---------|----------|
| P1 | Real over synthetic | AC-1 | ✅ | conventions.md §3 clearly separates §4 (synthetic) from §5 (real) — V1 |
| P2 | Honest incompleteness | AC-1, AC-3 | ✅ | Status vocabulary in conventions.md §3 and RF template §5 — V1, V3 |
| P3 | Coordinator designs, executor collects | AC-2, AC-3 | ✅ | TS Evidence field + RF §5 Evidence section — V2, V3 |
| P4 | Domain-agnostic by default | AC-1, AC-2 | ✅ | No domain-specific examples in any template — V1-V5 |
| P5 | Proportional to risk | AC-2 | ✅ | Evidence field supports N/A, empty, DEFERRED — V2 |
| P6 | Tooling proactivity | N/A (Phase B) | — | TS §3 marks as Phase B scope |
| P7 | Artifacts over claims | AC-5 | ✅ | §14 anti-patterns require artifact references — V1 |

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D39: Per-template visual sections | Evidence Sections as new per-template table | No — follows same pattern |
| 2 | F21: Explicit N/A pattern | RF §7-9 all use "No X." pattern | No — correctly applied |
| 3 | F13: Domain-agnostic | Templates avoid code-specific examples | No — correctly enforced |

No contradictions found.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Referenced verify.md findings in DoD assessment?
- [x] Checked RF §7-9 for presence AND quality (not just existence)?
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or "None"?
- [x] Fact Candidates from RF reviewed — any that need challenge?

> **"No fact candidates" challenge (Trust Protocol):** This is a template-modification task with no human interaction during execution beyond the initial TS approval. No domain knowledge, stakeholder insights, or strategic decisions were surfaced. "No fact candidates" is legitimate.

Stage complete: YES
