# RES — TFW-32 Iteration 4: Per-Template Naming & HL Vision Visual

> **Date**: 2026-04-10
> **Author**: AI (Researcher)
> **Status**: 🔬 RES — Complete (Iteration 4)
> **Parent HL**: [HL-TFW-32](HL-TFW-32__methodology_and_positioning.md)
> **Mode**: Pipeline (deep)
> **Predecessors**: [RES1](RES__TFW-32__methodology_and_positioning.md) (D1-D9), [RES2](research2/RES__iter2__naming_visualization_multiiter.md) (D10-D14), [RES3](RES__iter3__naming_visualization_multiiter.md) (D15-D20)

---

## Research Context

Iteration 4 re-examines two constraints from RES1-RES3: (1) the requirement to use ONE section name across all templates, and (2) treating HL §3.1 "Result Visualization" as the same kind of thing as process/flow diagrams. User input triggered both: "different artifacts = different framings, different mindsets" and "HL must have a visual — Working Backwards style — but that's NOT a diagram."

## Briefing

See [research4/briefing.md](research4/briefing.md). Key user direction:
- Relax the "one term" requirement. Different templates = different cognitive modes. Per-template naming is fine if the collection algorithm can handle it
- HL's "Result Visualization" is Amazon Working Backwards — "see the result as if it's done." This is NOT a process diagram
- The process/value visualization section is something different. "Value Maps"?
- Collection algorithm: one common section number, agent reads each section

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D21 | **Two distinct visual concepts in HL. §3.1 "Result Visualization" = outcome preview (Working Backwards). NEW visual section = process/flow visualization. Both stay, both needed** | §3.1 = WHAT done looks like (tables, before/after, sample output, mockups). Visual section = HOW the machine works (flows, architecture, journeys). Amazon PR/FAQ confirms: outcome narrative ≠ process diagram. **Empirically confirmed:** Exp1 shows zero overlap between "Result Visualization" (narrative timeline, testimonials, "6 months after launch") and "Value Flow" (value streams, INPUT→OUTCOME) |
| D22 | **Per-template naming for visual section. HL = "Value Flow", RF = "Diagrams", RES = "Findings Map"** | Decision criterion: "Does the cognitive mode CHANGE between templates?" **Empirically confirmed:** Exp1 found 6 different names trigger 6 distinct cognitive modes. Exp2 found "Diagrams" in HL context = confused mix; "Value Flow" in HL = focused strategic output. "Diagrams" in RF = pure technical. Per C1 + Exp2: per-template naming = net positive |
| D23 | **Reject "Value Maps" as section name. Use "Value Flow" instead** | "Value Map" has 3 conflicting industry meanings. "Value Flow" = cleaner. **Empirically confirmed:** "Value Flow" consistently triggers value-oriented output with INPUT→PROCESSING→OUTCOME structure and "Value Created" columns |
| D24 | **§6 Fact Candidates: keep ONE name across all templates. No per-template rename** | Cognitive mode is IDENTICAL across RF, RES, REVIEW: "report facts without interpretation." RES3 empirical test confirmed |
| D25 | **§7/§11 Strategic Insights: keep ONE name + qualifier (Planning / Execution / Research)** | RES3 empirically proved: "Strategic Insights" triggers deepest analytical mode. Qualifiers serve humans (context clarity), not agents. Cost = zero, benefit = human readability |
| D26 | **§3.1 "Result Visualization" stays. Enhance instructions with Working Backwards framing** | **Empirically confirmed:** Exp1 shows "Result Visualization" triggers Amazon Working Backwards style — narrative timeline ("8:00 AM..."), user testimonials, "imagine it's done" framing. This is fundamentally different from "Value Flow" output |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q11 | Should conventions.md have a cross-cutting "Visual Section" reference documenting all per-template names? | Open | Recommended (Option A from challenge C5). Useful for human understanding and new template creation |
| Q12 | Exact position of "Value Flow" in HL template — after §3.1? New §3.2? Separate section? | Open | Logical position: §3.2 (within "Target State" container). Or separate §X after Phases. Coordinator decides |
| Q13 | Should REVIEW template also have a visual section? | Open | Challenge found: REVIEW is a checklist/verdict, not a result. Visual section = not needed unless reviewer wants to annotate diagrams |

## Hypotheses

| # | Hypothesis | RES3 Status | RES4 Status | Evidence |
|---|-----------|-------------|-------------|----------|
| H_pertemplate | Different templates should have DIFFERENT section names for visual section | NEW | ✅ **CONFIRMED** (for visual), ❌ REFUTED (for §6, §7) | Analytical: C1 writer confusion ↓. **Empirical:** Exp1 — 6 names trigger 6 distinct modes. Exp2 — "Diagrams" in HL = confused, "Value Flow" in HL = focused. Context × Name interaction validated |
| H_visionvs | HL §3.1 "Result Visualization" is fundamentally different from process diagrams | NEW | ✅ **CONFIRMED** | Analytical: C4 — complementary, not overlapping. **Empirical:** Exp1 — "Result Visualization" → narrative timeline + testimonials. "Value Flow" → value streams + transformation tables. Zero content overlap |
| H_valuemaps | "Value Maps" could be the process visualization section name | NEW | ❌ **REFUTED** | Analytical: 3 conflicting meanings. **Empirical:** "Value Flow" triggers clean value-oriented mode. No industry term confusion |

## HL Update Recommendations

| # | What to update | Source |
|---|---------------|--------|
| 1 | §3 Target State / Phase A: Add "NEW visual section to HL, RF, RES templates — per-template naming: HL = Value Flow, RF = Diagrams, RES = Findings Map" | D22 |
| 2 | §3.1 instructions: Enhance with Working Backwards framing. Add: "This is NOT a process diagram. Show outcomes as if achieved" | D26 |
| 3 | §3 Target State: Add "§3.1 Result Visualization and § Value Flow are TWO separate concepts. §3.1 = outcome. Visual section = process" | D21 |
| 4 | §3 Unified terminology: Update to reflect: §6 = one name, §7/§11 = one name + qualifiers, § Visual = per-template | D24, D25, D22 |
| 5 | Phase A scope: Add "conventions.md cross-cutting Visual Section reference documenting per-template names" | Q11 |
| 6 | §10 Hypotheses: Add H_pertemplate, H_visionvs, H_valuemaps results | All |

## Fact Candidates

> Reviewing conversation history. Project-level facts discoverable by reading code/data. NOT tech debt (→ Observations). NOT human-only (→ Strategic Insights).

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC16 | convention | Decision criterion for per-template vs unified section naming: "Does the cognitive mode CHANGE between templates?" If yes → per-template. If no → unified. Applied: visual section = per-template, §6 = unified, §7 = unified | Extract E2 analysis, 2026-04-10 | ★★★ |
| FC17 | convention | TFW has TWO types of visual content in HL: (1) "Result Visualization" = outcome preview (Working Backwards, WHAT done looks like), (2) "Value Flow" = process visualization (HOW value gets created). These are complementary, not overlapping | Challenge C4 analysis, 2026-04-10 | ★★★ |
| FC18 | domain | "Value Map" has 3 conflicting industry meanings: Strategyzer (customer jobs/pains/gains), Lean (material/information flow), Management (strategy-to-execution KPIs). Using it as a generic term creates confusion for anyone familiar with these frameworks | External research (Gather G3), 2026-04-10 | ★★☆ |

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS8 | philosophy | «разные артефакты это разные фрейминги, разный майндсет» — the insight that different templates serve different cognitive modes is a DESIGN PRINCIPLE, not just a naming preference. It means: template names are micro-prompts tuned per context. This extends D28 from "one name = one behavior" to "right name PER CONTEXT = right behavior PER CONTEXT" | User (2026-04-10) | ★★★ |
| SS9 | philosophy | HL vision visual is inspired by Amazon Working Backwards / PR/FAQ. «я хочу визуально видеть результат, представить что он уже есть» — this is an explicit design philosophy: the HL must make the reader SEE the outcome before work begins. Not a process diagram — an outcome narrative | User (2026-04-10) | ★★★ |
| SS10 | process | «не проблема заставить агента заглянуть в каждый раздел» — pragmatic insight that simplifies the design. Collection algorithm doesn't need standardized names — it reads full artifacts. Section names are PROMPTS for writers, not TAGS for collectors | User (2026-04-10) | ★★★ |

## Empirical Validation

Two experiments run against Qwen3.5-27B (local vLLM, 192.168.1.109:8000). Full analysis: [research4/experiment_analysis.md](research4/experiment_analysis.md).

**Experiment 1** (6 section names, same context): Each name triggers a DISTINCT cognitive mode. "Value Flow" → strategic/value-oriented. "Diagrams" → technical/engineering. "Findings Map" → analytical/research. "Result Visualization" → narrative/outcome. "Visual Overview" → generic/unfocused (weakest). "Process Maps" → operational/BPM.

**Experiment 2** (same name across HL/RF contexts): "Diagrams" in HL = confused output (mixed vision/tech). "Value Flow" in HL = clean strategic output. "Diagrams" in RF = focused technical diagrams. Confirms per-template naming is not just cosmetic — it activates the RIGHT cognitive mode per context.

## Conclusion

Iteration 4 resolved two constraints inherited from previous iterations, now with **both analytical and empirical validation**.

First: the "one name for all templates" requirement was partially relaxed — per-template naming is applied WHERE cognitive modes differ (visual section: HL = Value Flow, RF = Diagrams, RES = Findings Map) and kept unified WHERE modes are identical (§6 Fact Candidates, §7 Strategic Insights). The decision criterion is clean: does the cognitive mode change between templates? LLM experiments confirmed: 6 different names → 6 distinct output patterns.

Second: HL §3.1 "Result Visualization" (Amazon Working Backwards style) and process/flow visualization are confirmed as TWO SEPARATE CONCEPTS — empirically zero overlap. "Result Visualization" produces narrative timelines and testimonials; "Value Flow" produces value stream diagrams and transformation tables.

"Value Maps" was rejected due to 3 conflicting industry meanings. "Value Flow" is cleaner, cross-domain validated, and TFW-native.

## Iteration Status

- **Iteration:** 4 of 2 (min) / 5 (max)
- **Hypotheses tested:** H_pertemplate (partially confirmed: yes for visual, no for §6/§7), H_visionvs (confirmed: two separate concepts), H_valuemaps (refuted: loaded term, use "Value Flow")
- **Hypotheses deferred:** None
- **Gaps discovered:**
  - Q11: conventions.md visual section reference (design exists, placement TBD)
  - Q12: exact position of "Value Flow" in HL template
  - Q13: REVIEW visual section (probably not needed)
- **Superseded decisions:** D22 extends D17 (RES3 "Diagrams everywhere" → per-template naming for visual). D23 rejects user's "Value Maps" proposal → "Value Flow" instead

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | ~~Empirical LLM test for "Value Flow"~~ | ~~Only analytically validated~~ | ✅ DONE — Exp1 + Exp2 validated |
| 2 | Exact template positions for new sections | Templates need concrete line-by-line edits | TS-level work |
| 3 | REVIEW visual section decision | Low priority, probably "no" | TS-level decision |

### Recommendation
- [x] **SUFFICIENT** — proceed to `/tfw-plan` to update HL and write TS
- [ ] MORE NEEDED
- [ ] BLOCKED

All naming decisions now have BOTH analytical AND empirical validation. The only remaining work (template positions, REVIEW visual) is TS-level implementation detail, not research.

> ⚠️ Coordinator decides. Researcher recommends but does NOT decide.

---

*RES — TFW-32 Iteration 4: Per-Template Naming & HL Vision Visual | 2026-04-10*
