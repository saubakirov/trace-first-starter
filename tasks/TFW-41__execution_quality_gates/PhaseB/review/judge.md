# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Mode: docs
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | verify.md: all 6 AC items confirmed in actual files. All gates are mandatory steps, not suggestions (verified in-file language). |
| 2 | Philosophy aligned | ✅ | HL §7 P1 (Gates over guidelines): all insertions are imperative steps, not "consider" language. P3 (Verify against fact): Pre-TS Gate explicitly says "Read RF (actual output), not TS (planned output)." P5 (Executor as engineer): Execution Loops force self-checking, not copying. |
| 3 | Tech debt documented | ✅ | RF §5 has 2 observations in table format with file, line, type, and description. Both are genuine structural fragility findings (step-label collision, alpha-numeric branch labeling). |
| 4 | Style & standards | ✅ | All insertions follow existing workflow prose style (imperative, second-person, blockquote for role notes). File naming follows conventions §4. No §4 "Detailed Steps" or §5 "Acceptance Criteria" old-template references found (per RF §4 scan). |
| 5 | Observations collected | ✅ | 2 observations, both qualify: review.md Step 0 collision and plan.md alpha-numeric label fragility are real structural issues that will bite future executors. Quality bar met. |
| 6 | RF completeness (§6-8) | ✅ | §6 Fact Candidates: 2 entries (both real). §7 Strategic Insights: present, correctly "No strategic insights" (execution-only task, no human domain input). §8 Diagrams: present, correctly "No diagrams." All sections present. |

## Mode-Specific Checklist (docs)

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 7 | Content quality | ✅ | Gate language is unambiguous and imperative. Pre-RF Gate: "Open `.tfw/templates/RF.md`. Read all section headings before writing anything." — no wiggle room. Execution Loops: defines the annotation, gives example, states the independent-AC rule. ONB answer protocol: "Do not decide on behalf of the stakeholder." All gates meet TS §7 DoF requirement: no "suggestion" or "recommendation" language. |
| 8 | Source verification | ✅ | All TS cross-references (DR2, DR3, D6, D9, D10, D11 from HL §4) are traceable to research decisions in the master HL §10 research decisions table. The `[depends: AC-X]` annotation mechanism was specified in Phase A's TS template — verified: conventions.md §14 anti-pattern "TS contains ready-made implementation" is present (Phase A deliverable). |

## Deviation Assessment: HL §7 Principles check as paragraph, not checklist item

TS AC-5 states: "checklist item." Executor placed it as a body paragraph in Step 4 Judge. This is a minor form deviation. Substantive test: does the paragraph enforce the same behavior as a checklist item would?

- The text is mandatory (no conditional language).
- It names the exact artifact to read (TS §3 Principles Check table).
- It names the exact location to verify against (RF §3).
- It specifies the escalation condition (principle violation ≠ AC miss).

**Verdict on deviation:** The paragraph form is functionally equivalent to a checklist item and is arguably more readable in a flowing step. The TS AC-5 gate condition ("Read review.md → Principles check exists in Judge step") is fully satisfied. Deviation accepted — no impact on gate effectiveness.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| — | No KNOWLEDGE.md exists in this project | N/A | No applicable knowledge items |

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Referenced verify.md findings in DoD assessment?
- [x] Checked RF §6-8 for presence AND quality?
- [x] KNOWLEDGE.md: N/A — project has no KNOWLEDGE.md yet?
- [x] Fact Candidates from RF reviewed — both are real, no challenge needed?

Stage complete: YES
