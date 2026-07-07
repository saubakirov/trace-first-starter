# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Mode: code
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | 5/5 ACs verified against actual files — verify.md V1-V5. All sub-criteria in AC-1 (10 checkboxes) confirmed. AC dependency (AC-4 depends AC-2) respected: AC-2 done before AC-4 |
| 2 | Philosophy aligned | ✅ | TS §3 Principles Check: P1 (real over synthetic) → AC-1 Step 11 text distinguishes real vs synthetic ✅; P2 (honest incompleteness) → DEFERRED/BLOCKED guidance in Step 11 ✅; P3 (coordinator designs, executor collects) → AC-3 plan.md + AC-1 handoff ✅; P4 (domain-agnostic) → no tool names in Step 11 ✅; P5 (proportional) → skip clause present ✅; P6 (tooling proactivity) → proactive tooling note present ✅; P7 (artifacts over claims) → Trust Protocol Challenge for N/A without TS evidence ✅ |
| 3 | Tech debt documented | ✅ | RF §6 has 2 observations — both substantive (numbering confusion in plan.md, stale glossary ref routed to Phase C) |
| 4 | Style & standards | ✅ | Step 11 density matches Steps 9-10 (~5 lines). Trust Protocol entries follow existing 3-column pattern. plan.md sub-step follows existing numbering |
| 5 | Observations collected | ✅ | 2 real issues: plan.md sub-step numbering pre-existing pattern, glossary.md stale ref already noted in Phase A. Quality bar: both are genuine, neither is filler |
| 6 | RF completeness (§7-9) | ✅ | §7 Fact Candidates: "No fact candidates." §8 Strategic Insights: "No strategic insights." §9 Diagrams: "No diagrams." All present with explicit N/A per F21 |
| 7 | Evidence completeness | ✅ | All 5 TS AC items have Evidence field N/A (appropriate — workflow spec). RF §5 has 7/7 VERIFIED with line references that resolve to actual content (verified in verify.md E1-E7) |

## Mode-Specific Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 7 | Code quality | ✅ | Markdown conventions followed. Step instructions use existing patterns (bold title, dash-separated guidance, proportionality clause). No formatting deviations |
| 8 | Test coverage | N/A | No executable tests for .tfw/ framework files. Build config has `echo` placeholders |
| 9 | Security | ✅ | No secrets, no external URLs, no authentication. Workflow text only |
| 10 | Breaking changes | ✅ | Step renumbering (11→12, 12→13) is additive. Trust Protocol entries added, not modified. No backward incompatibility. Existing workflows referencing "Step 11" would need updating, but no other file references handoff steps by number |

## TS §3 Principles Check Verification

| # | Principle | TS maps to | AC met? | Principle enforced? |
|---|-----------|-----------|---------|---------------------|
| P1 | Real over synthetic | AC-1 | ✅ | ✅ — Step 11 distinguishes real environment from synthetic |
| P2 | Honest incompleteness | AC-1 | ✅ | ✅ — DEFERRED/BLOCKED with reason |
| P3 | Coordinator designs, executor collects | AC-3 + AC-1 | ✅ | ✅ — plan.md reminder + handoff step |
| P4 | Domain-agnostic | AC-1 | ✅ | ✅ — environment types, not tool names |
| P5 | Proportional to risk | AC-1 | ✅ | ✅ — skip clause when no Evidence fields |
| P6 | Tooling proactivity | AC-1 | ✅ | ✅ — proactive tooling note |
| P7 | Artifacts over claims | AC-2 | ✅ | ✅ — VERIFIED without artifact = Challenge |

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D49 (TFW-41): Requirements-first TS | Step 11 follows AC-driven execution | No — extends D49 pattern |
| 2 | D46 (TFW-38): Trust Protocol | 2 new entries follow same pattern | No — extends D46 |
| 3 | D41 (TFW-38): 4-stage review | verify.md Evidence Verification referenced | No — referenced correctly |

> No contradictions found.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Referenced verify.md findings in DoD assessment?
- [x] Checked RF §7-9 for presence AND quality (not just existence)?
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or "None"?
- [x] Fact Candidates from RF reviewed — any that need challenge?

Stage complete: YES
