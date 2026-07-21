# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Mode: docs
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | verify.md: All 6 ACs verified. V1-V7 all ✅ match. No discrepancies found. |
| 2 | Philosophy aligned | ✅ | HL §7 P1 (mandatory, not optional): conventions.md §3/§4 use "MUST contain" language. P2 (template reflects values): EV template has structured Environment header + per-AC table + Verdict — trace-first, reproducible. |
| 3 | Tech debt documented | ✅ | RF §6 has 3 Observations: compilable contract Source Manifest, project_config.yaml templates, review template RF §5 references. All are real issues — naming/config gaps. |
| 4 | Style & standards | ✅ | EV naming follows D28 (2-letter abbreviation, consistent with HL/TS/RF). File naming in conventions.md §4 table follows existing patterns. New sections use same heading hierarchy as existing content. |
| 5 | Observations collected | ✅ | 3 observations, all typed "naming." Quality: Observation #1 (compilable_contract.md Source Manifest) is a real gap. #2 (project_config.yaml) correctly notes consistency with research templates. #3 (review/verify.md) correctly assessed as no-action. All are substantive, not filler. |
| 6 | RF completeness (§7-9) | ✅ | §7 Fact Candidates: "No fact candidates." — section present, empty content valid. §8 Strategic Insights: "No strategic insights." — section present, empty content valid. §9 Diagrams: BEFORE/AFTER ascii diagram present showing evidence pipeline change. |
| 7 | Evidence completeness | ✅ | All 6 TS AC items had `Evidence: N/A` — definition documents, no runtime verification applicable. EV file exists with correct all-N/A verdict. This is the correct treatment for methodology changes (templates, conventions, workflows). |

## Mode-Specific Checklist (docs)

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 7 | Content quality | ✅ | EV template is clear, well-structured, and self-documenting. Conventions updates use consistent language ("MUST contain"). TS/RF template changes are minimal and precise. Handoff substeps are actionable (create → copy → fill → walk → verdict → attachments). |
| 8 | Source verification | ✅ | D53 correctly cites "0/38 tasks created evidence/" from HL §2. EV template structure aligns with iter1 RES decisions D1-D7. Anti-pattern language at L442 correctly references `evidence/` folder. |

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D52 (Evidence Layer — TFW-46) | D53 extends, doesn't modify D52 | No — D52 preserved as original concept, D53 = enforcement extension |
| 2 | D16 (evidence/ optional) | D53 revokes D16 | No — explicit revocation with justification, not silent overwrite |

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Referenced verify.md findings in DoD assessment?
- [x] Checked RF §7-9 for presence AND quality (not just existence)?
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or "None"?
- [x] Fact Candidates from RF reviewed — any that need challenge?
  - RF §7 says "No fact candidates." — acceptable for a methodology phase that follows well-researched decisions (iter1 D1-D7).

Stage complete: YES
