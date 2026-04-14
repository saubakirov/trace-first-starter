# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Mode: spec
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ⚠️ | 13/14 AC items verified ✅. AC2 ("Each template has Mindset as mandatory header field: Student / Auditor / Judge") — map.md uses "Newcomer" instead of "Student." The cognitive intent is identical but the label deviates from the TS specification. Minor: doesn't break functionality but breaks spec-to-implementation traceability. |
| 2 | Philosophy aligned | ✅ | HL §7 P1 (Workflow > Template): enforcement in review.md workflow confirmed — Steps 1-3 reference templates, stage mindsets inline. P2 (Map/Verify/Judge/Decide): 4 stages present. P5 (Naming Creates Behavior): "Map", "Verify", "Judge" are 1-syllable active verbs. P6 (Knowledge Gate): verify.md and judge.md both have KNOWLEDGE.md self-check items. |
| 3 | Tech debt documented | ✅ | RF §5 Observations: 2 items documented in table format with file, line, type, description. Both are real issues (stale Visual Sections table, Role Lock artifact count). |
| 4 | Style & standards | ⚠️ | Template structure follows TS-specified format. conventions.md §3 parallels research subfolder structure ✅. However, conventions.md §15 Role Lock table is stale (says "REVIEW" only, should include stage files per review.md line 12). |
| 5 | Observations collected | ✅ | 2 observations, both substantive. Obs #1 (Visual Sections table stale) is a real consistency gap. Obs #2 (Role Lock artifact count) is informational but valid. No filler. |
| 6 | RF completeness (§6-8) | ✅ | §6 Fact Candidates: "No fact candidates." — present ✅. §7 Strategic Insights: "No strategic insights." — present ✅. §8 Diagrams: "No diagrams." — present ✅. Challenge on §8: this task adds a 4-stage review flow (Map→Verify→Judge→Decide) — but the flow diagram is already in HL §3.1 and this phase adds templates/modifications, not new architecture. "No diagrams" is acceptable. |

## Mode-Specific Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 7 | Analytical quality | ✅ | Stage templates are well-structured: clear cognitive modes per stage, progressive information flow (map builds understanding → verify tests claims → judge evaluates quality), self-check gates prevent mechanical check-offs. The D21/D27 pattern integration (Reviewer Identity + Trust Protocol) provides reviewer calibration before stage work begins. |
| 8 | Source attribution | ✅ | RF §2 Key Decisions cite ONB §4.1-§4.3 coordinator approvals. TS references D18 (supersedes D8), D21, D27 patterns. Templates reference KNOWLEDGE.md decisions correctly. All claims traceable. |

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D18: review stages as separate files | RF implements 3 stage templates | No — exact implementation of D18 |
| 2 | D21: Coordinator Mindset / Identity | RF adds Reviewer Identity blockquote | No — applies same pattern to reviewer role |
| 3 | D27: Trust Protocol levels | RF adds 7-row Trust Protocol table | No — adapts same pattern for review context |
| 4 | conventions.md §15 Role Lock: review.md → REVIEW only | review.md now permits stage files + REVIEW | ⚠️ Inconsistency — §15 table not updated. Not a contradiction with KNOWLEDGE.md decisions, but a within-file consistency issue |

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Referenced verify.md findings in DoD assessment? (V1 map.md mindset discrepancy, V6 conventions.md Role Lock table)
- [x] Checked RF §6-8 for presence AND quality (not just existence)? (All present, §8 "No diagrams" challenged and accepted)
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or "None"? (4 items checked, 1 within-file inconsistency noted)
- [x] Fact Candidates from RF reviewed — any that need challenge? (RF §6 says "No fact candidates" — no human insights visible in this spec task to challenge)

Stage complete: YES
