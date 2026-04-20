# ONB — TFW-41 / Phase A: Templates and Conventions

> **Date**: 2026-04-20
> **Author**: Executor (AI)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-41](../HL-TFW-41__execution_quality_gates.md)
> **TS**: [TS__PhaseA__templates_and_conventions](TS__PhaseA__templates_and_conventions.md)

---

## 1. Understanding

Phase A rewrites the TS template from a procedural (Detailed Steps) model to a requirements-first model, adds a Principles Check table and `[depends: AC-X]` dependency annotation, adds a Phase Dependencies subsection to the HL template, and appends 4 new anti-patterns to `conventions.md §14`. This phase is the structural foundation for all subsequent phases — Phase B references the new TS template for Execution Loops, Phase C references it for Research integration. No external dependencies.

## 2. Entry Points

| File | Current state | Change |
|------|--------------|--------|
| `.tfw/templates/TS.md` | 54 lines. Has §4 Detailed Steps, §5 Acceptance Criteria (flat checklist), §6 Phase Risks. No Principles Check, no Technical Guidance, no Definition of Failure. | Full rewrite: §3 Principles Check (new), §4 AC (replaces §4+§5), §5 Technical Guidance (new), §6 DoF (new), §7 Phase Risks (renumbered) |
| `.tfw/templates/HL.md` | 176 lines. §4 Phases has Phase A/B templates, no Phase Dependencies subsection. | Add Phase Dependencies subsection before the first Phase block |
| `.tfw/conventions.md` | §14 Anti-patterns has 19 items (lines 366–386). | Append 4 new anti-patterns |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions. All AC items are unambiguous and directly implementable. | — |

## 4. Recommendations (suggestions, not blocking)

1. **Section ordering in new TS.md**: The TS spec places "Principles Check" between Scope and Affected Files (as §3), shifting Affected Files to §4, and then §4 AC, §5 Technical Guidance, §6 DoF, §7 Phase Risks. I'll follow the TS AC-5 spec literally: `## 3. Principles Check` comes after Scope, before Affected Files. This means the Affected Files section becomes §4 — but that conflicts with AC-1 requiring §4 to be "Acceptance Criteria". **Resolution**: reading TS more carefully — AC-5 says "New section between Scope and Affected Files", so Principles Check = §3, Affected Files = §4, AC = §5, TG = §6, DoF = §7, Phase Risks = §8. This matches the AC-5 table columns and is consistent with the TS structure as demonstrated in the TS itself (which uses §4 AC, §5 TG, §6 DoF, §7 Phase Risks with Affected Files at §3). Confirming: the TS itself follows the pattern: §1 Objective, §2 Scope, §3 Affected Files, §4 AC, §5 TG, §6 DoF, §7 Phase Risks — and AC-5 says Principles Check goes "between Scope and Affected Files" → §3 Principles Check, §4 Affected Files... but that pushes AC to §5. I will use the ordering demonstrated in the TS itself as ground truth: §3 = Affected Files, then a new "Principles Check" section inserted after §3 but before §4 AC. Final numbering: §1 Obj, §2 Scope, §3 Affected Files, §3.1 (or standalone) Principles Check, §4 AC, §5 TG, §6 DoF, §7 Phase Risks. Cleanest: make Principles Check a standalone §3.5 or place it as §4, shift everything down. I will use the numbering from the TS spec examples directly: **§3 Principles Check, §4 Affected Files, §5 AC, §6 TG, §7 DoF, §8 Phase Risks** — aligning with AC-5 instruction ("between Scope and Affected Files").

   > This is a non-blocking structural interpretation. If the coordinator prefers a different numbering, note in RF.

2. **`[depends: AC-X]` annotation placement**: The TS shows the annotation inline in the heading: `### AC-3: Report reflects transformed data  [depends: AC-1]`. The template should show this pattern in at least one AC item per AC-2. The template instruction text should explain that executors verify dependent ACs in order.

3. **Domain-agnostic examples**: The TS specifies using the analytics ETL example from HL §3.1 as the template's domain-neutral example. Using that exact example in the template is appropriate.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Section renumber cascade into Phase B**: Phase B modifies `handoff.md` and `plan.md` which may reference TS sections by number (e.g., "read §4 Detailed Steps"). TS spec §7 Phase Risks explicitly calls this out and assigns resolution to Phase B. I will note current §-references I observe during editing to aid Phase B coordinator.

2. **`{curly braces}` convention consistency**: The current TS template uses `{curly braces}` for placeholder instruction text. The new template must maintain this convention throughout — all instruction text in `{curly braces}`, all structural text as literal headings/labels. One risk: the Principles Check table columns are structural (literal column headers), not placeholders — these should not be wrapped in braces.

3. **HL template Phase Dependencies placement**: The TS says "Add to HL template §4 Phases, before the first Phase". The current HL §4 starts with instruction text `Break into Phases (A, B, C...) with priorities 🔴🟡🟢.` followed immediately by `### Phase A`. The new Phase Dependencies subsection should go between the §4 instruction text and the first `### Phase A` block. This is unambiguous.

## 6. Inconsistencies with Code (spec vs reality)

1. **Principles Check position ambiguity**: AC-5 says "New section between Scope and Affected Files" but the TS itself (as a live example) places Principles Check absent and has §3 = Affected Files, §4 = AC. The template will implement AC-5 literally: Principles Check as §3, Affected Files as §4. This makes the TS file a self-demonstrating example that does not perfectly match its own new template (it was written before the template change). This is expected — TS spec §5 explicitly notes "forward-only change — old TS files remain valid."

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | conventions.md §14 — Anti-patterns list | ✅ | Applied: read all 19 existing anti-patterns; will append 4 new ones in correct one-line format, after line 386 | Verified: §14 currently ends at line 386 with the `Coordinator reads KNOWLEDGE.md...` item |
| 2 | conventions.md §3 — TS definition: "self-contained: inputs/outputs/constraints/DoD" | ✅ | Applied: the new template reinforces this by making AC the DoD mechanism; Technical Guidance = constraints/context section | The definition aligns with requirements-first model |
| 3 | glossary.md — Scope Budget | ✅ | N/A for this phase: Phase A modifies templates only, no scope budget enforcement needed in the template itself (budget is in project_config.yaml, not template) | Phase D will add new terms to glossary |
| 4 | README.md Values — "The thinking is the product" | ✅ | Applied: directly motivates the requirements-first restructure. Template instruction text will emphasize WHAT not HOW to enforce executor thinking | Core value that the new §5 Technical Guidance explicitly states |

---

*ONB — TFW-41 / Phase A: Templates and Conventions | 2026-04-20*
