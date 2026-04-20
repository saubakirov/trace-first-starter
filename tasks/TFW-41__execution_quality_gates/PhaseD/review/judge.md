# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Mode: code
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | verify.md V1-V6: all AC-1 (15 terms) and AC-2 (4 adapters) items confirmed. One 1-byte encoding diff in tfw-plan.md is non-semantic. |
| 2 | Philosophy aligned | ✅ | HL §7 P2 (Requirements, not implementation): glossary entries define WHAT terms mean, verified domain-neutral. HL §7 P6 (Domain-agnostic): no domain-specific examples in any definition. Both mapped principles confirmed met per TS §3 Principles Check. |
| 3 | Tech debt documented | ✅ | RF §5 Observations present: 1 item (`briefing.md` forward reference). Quality-filtered: the observation is real and actionable. |
| 4 | Style & standards | ✅ | All 15 definitions follow single-paragraph format with `→ file §N` reference pattern. Section placements (`## Execution Gates` after `## Roles`, `## Research — Dimensional Analysis` after `## Read-only AG`) match TS §6 Technical Guidance suggestion. Glossary naming convention consistent with existing entries. |
| 5 | Observations collected | ✅ | RF §5 has 1 observation (briefing.md). Not generated for the sake of section existence — specific actionable issue with rationale. Quality bar met. |
| 6 | RF completeness (§6-8) | ✅ | §6 Fact Candidates: 2 items (process + convention). §7 Strategic Insights: explicitly marked "No strategic insights" with rationale (documentation-only phase). §8 Diagrams: explicitly marked "No diagrams" with rationale. All 3 sections present. |

## Mode-Specific Checklist (code)

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 7 | Code quality (conventions, naming) | ✅ | Pure markdown — naming follows TFW conventions. Glossary term ordering (logical grouping), section headings (H2), term headings (H3) all consistent with existing glossary structure. |
| 8 | Test coverage | N/A | No tests for markdown tasks. RF §4 Verification explicitly states "No build/lint commands defined — pure markdown modifications" with a manual checklist completed. |
| 9 | Security | N/A | No code, no secrets, no authentication. Not applicable. |
| 10 | Breaking changes | ✅ | Glossary: additive-only. Adapters: verbatim overwrite — no regression possible since source workflows already approved in Phases B/C. README: additive links only. Zero breaking changes. |

## HL §7 Principles Check

TS §3 maps two principles:
- **P2 (Requirements, not implementation)** → AC-1: glossary entries describe WHAT terms mean. Verified in verify.md V1: definitions are conceptual, not implementation-instructional.
- **P6 (Domain-agnostic by default)** → AC-1: domain-neutral language. Verified in verify.md V1: no code/CSS/API examples in any of the 15 definitions.

Both principles pass. No principle violation.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | TFW v3 canonical framework (KI) | Glossary extended with 15 new terms | No contradiction — this is an extension, not a change to existing terms |

No contradictions found. KNOWLEDGE.md TFW framework KI reflects glossary at time of last sync; Phase D extends it. This is expected behavior.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Referenced verify.md findings in DoD assessment?
- [x] Checked RF §6-8 for presence AND quality (not just existence)?
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or "None"?
- [x] Fact Candidates from RF reviewed — any that need challenge?

**FC challenge assessment:**
- FC1 (process: HL is authoritative over TS when they diverge) — this is a genuine process insight from a real ONB resolution. High confidence. Worth capturing.
- FC2 (convention: "Alternative" as missing link in term cluster completeness) — medium confidence, reviewer-discovered rather than human-sourced, borderline. Acceptable.

Stage complete: YES
