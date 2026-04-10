# Challenge — Iteration 4: "What do we NOT expect?"
> Parent: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> Predecessors: [Gather](gather.md), [Extract](extract.md)
> Goal: Stress-test per-template naming, visual concept split, and the "Value Flow" name.

## C1: Does per-template naming confuse new agents?

**Concern:** If HL has "Value Flow" and RF has "Diagrams" — a fresh agent reading both for the first time might not realize they're the "same kind of section" with different framing.

**Counter-test scenarios:**

| Scenario | What happens with unified "Diagrams"? | What happens with per-template names? |
|----------|---------------------------------------|--------------------------------------|
| Agent writes HL | Sees "Diagrams" → thinks of UML/ERD → writes tech diagrams in a vision document | Sees "Value Flow" → thinks of user journey, value delivery → writes strategic overview ✅ |
| Agent writes RF | Sees "Diagrams" → draws tech diagrams ✅ | Sees "Diagrams" → draws tech diagrams ✅ |
| Agent writes RES | Sees "Diagrams" → draws... what? Research findings as UML? Unclear | Sees "Findings Map" → draws concept map, comparison table, decision tree ✅ |
| Agent collects from all 3 | Knows to look for "Diagrams" in each file | Needs to know: HL = "Value Flow", RF = "Diagrams", RES = "Findings Map" |

**Key finding:** For the WRITER agent, per-template names are BETTER. Each name prompts the right cognitive mode. For the COLLECTOR agent, it's slightly more complex — but the collector reads the whole file anyway.

The confusion risk is real only if agents need to cross-reference between templates by section name. In TFW, they don't — they read the template header, which tells them what to do.

**Verdict:** Per-template naming for visual section = net positive. Writer confusion DOWN (better prompts), collector cost = negligible.

## C2: "Value Flow" as HL visual section name — stress test

| Domain | What does "Value Flow" prompt? | Works? |
|--------|-------------------------------|--------|
| Software product (e2e feature) | User → input → processing → value received | ✅ |
| Business analytics (CFO report) | Data → analysis → insight → decision → business value | ✅ |
| Education (curriculum design) | Student → learning activity → skill acquisition → assessment → competence | ✅ |
| Research project (TFW-32) | Problem → investigation → finding → decision → methodology improvement | ✅ |
| Operations (logistics) | Order → fulfillment → delivery → customer satisfaction | ✅ |

Cross-domain: ✅ ALL work. "Value Flow" = universal. Every project delivers value through a flow.

**Edge case:** Pure research with no clear "value delivery" (e.g., "explore whether X is feasible"). 
→ "Value Flow" still works: question → method → evidence → answer → decision. The "value" is: clearer decision.

**Alternative considered: "Value Delivery"** — too formal, sounds like a KPI metric, not a visual prompt.

**Alternative considered: "Process Overview"** — generic, doesn't prompt VALUE thinking, agent would produce boring boxes-and-arrows.

**Verdict:** "Value Flow" is strong. Cross-domain, value-centric (TFW-native), prompts the right level of abstraction for HL.

## C3: "Findings Map" as RES visual section name — stress test

| Scenario | What does "Findings Map" prompt? |
|----------|--------------------------------|
| Research compared 5 tools | Comparison matrix / radar chart ✅ |
| Research investigated a hypothesis | Decision tree: hypothesis → evidence → verdict ✅ |
| Research gathered market data | Market landscape map / positioning chart ✅ |
| Research analyzed code architecture | Component relationship diagram ✅ |

**"Findings Map"** = "organize and visualize what we found." The "Map" part prompts spatial organization (not just a list). The "Findings" part filters to research output (not process).

**Counter-question:** Is "Findings Map" too research-specific? RES is ONLY used in research. So yes, it should be research-specific. That's the point.

**Verdict:** Works well for RES context.

## C4: HL §3.1 "Result Visualization" — does it still need to exist alongside "Value Flow"?

**The question I didn't expect:** If HL gets a "Value Flow" section, what's the difference between §3.1 "Result Visualization" and the new "Value Flow" section?

| §3.1 Result Visualization | NEW Value Flow section |
|---|---|
| Shows the OUTCOME — "what does done look like" | Shows the PROCESS — "how does value get from A to B" |
| Amazon Working Backwards. Tables, examples, sample output | Lean/BPMN tradition. Flowcharts, journey maps, architecture overview |
| Part of §3 "Target State (To-Be)" — embedded | Separate section — standalone |
| ALWAYS present (required in HL) | OPTIONAL (not every HL needs a process diagram) |
| TEXT-heavy: before/after tables, mockups, code snippets | VISUAL-heavy: diagrams, flows, maps |

**These are genuinely different:**
- §3.1 = "Imagine the result exists. Show me."
- Value Flow = "Show me how the machine works that produces that result."

**Example from TFW-32 HL:**
- §3.1 shows: pipeline comparison (before → after), docs-vs-knowledge separation diagram, terminology unification table. These are OUTCOMES.
- Value Flow would show: the workflow sequence (HL → RES → TS → RF → REVIEW → KNW → DONE), or the knowledge collection flow (Fact Candidates → /tfw-knowledge → verified facts). These are PROCESSES.

Both are valuable. Both are different. Both should exist.

**Verdict:** §3.1 "Result Visualization" and "Value Flow" are complementary, not overlapping. Keep both.

## C5: The "generic section label" question for conventions.md

User asked: «в теории мы можем просто иметь один общий номер раздела и как-то его условно назвать»

What should conventions.md say about the visual section?

**Option A: Named reference**
```markdown
### Visual Section (per-template)
Each result artifact has a visual section with template-specific naming:
- HL: "Value Flow" — value delivery overview
- RF: "Diagrams" — technical process detail
- RES: "Findings Map" — research findings visualization
```

**Option B: Numbered reference**
```markdown
### §VIS (Visual Section)
Section number §VIS appears in HL, RF, and RES templates with template-specific names.
```

**Option C: No special marking — just template instructions**
Each template defines its own section. No cross-cutting reference needed. Agents read their own template.

**My assessment:** Option A is cleanest. Conventions.md documents the pattern. Each template implements its own name. Collection algorithm reads by position, not by name.

But — do we even NEED a cross-cutting reference? The collector agent reads the full artifact. It doesn't search by section name. It reads everything.

The cross-cutting reference is useful for:
1. Human understanding: "where do diagrams go?" → "each template has a visual section"
2. Glossary entry: one place to see all visual section names
3. Template consistency: new templates know they should include a visual section

**Verdict:** Option A. Document the pattern in conventions.md. Brief, not heavy.

## C6: Strategic Insights qualifier — final stress test

RES3 left Q8 open: should Strategic Insights have qualifiers?

With per-template naming established for visual section, let me re-check:

| Template | Without qualifier | With qualifier |
|----------|------------------|----------------|
| HL §11 | "Strategic Insights" | "Strategic Insights (Planning)" |
| RF §7 | "Strategic Insights" | "Strategic Insights (Execution)" |
| RES §7 | "Strategic Insights" | "Strategic Insights (Research)" |

**Does the qualifier change agent behavior?** RES3 empirical test showed "Strategic Insights" triggers deep analytical mode. Adding "(Planning)" or "(Execution)" = context, not behavior change. The core prompt word is "Strategic Insights" — qualifier is parenthetical annotation.

**Does the qualifier help the human?** Yes. When reviewing: "is this from planning or execution?" matters. The qualifier answers without reading the whole artifact.

**Does the qualifier help collection?** No. Collection gathers ALL Strategic Insights. Source context is in the table (Source column).

**Verdict:** Qualifiers are useful for humans, neutral for agents. Add them. Cost = zero. Benefit = human clarity.

## Checkpoint

| # | Finding | Status |
|---|---------|--------|
| C1 | Per-template naming for visual = net positive. Writer confusion ↓, collector cost ≈ 0 | ✅ CONFIRMED |
| C2 | "Value Flow" is cross-domain, value-centric, prompts right level | ✅ CONFIRMED |
| C3 | "Findings Map" works for RES context | ✅ CONFIRMED |
| C4 | §3.1 "Result Visualization" and "Value Flow" are DIFFERENT concepts. Both needed | ✅ CONFIRMED: two sections, not one |
| C5 | Conventions.md should document the visual section pattern (Option A) | Recommend |
| C6 | Strategic Insights qualifiers: useful for humans, neutral for agents. Add | ✅ CONFIRMED |

**Sufficiency:**
- [x] External source used? (Gather G1-G5 informing all challenges)
- [x] Briefing gap closed? (All 3 hypotheses challenged and resolved)

**Deep mode criteria:**
- [x] Hypothesis tested? H_pertemplate (confirmed FOR visual, rejected for §6/§7), H_visionvs (confirmed: two separate concepts), H_valuemaps (rejected: "Value Maps" too loaded, "Value Flow" is better)
- [x] Counter-evidence sought? Tested confusion risk (C1), cross-domain coverage (C2-C3), overlap risk (C4)
- [x] Metacognitive check: The unexpected finding was C4 — I came in thinking "Value Flow" replaces §3.1, but actually they're complementary. §3.1 = WHAT done looks like. Value Flow = HOW the machine works. Both needed in HL.

Stage complete: YES

---

## C7: Empirical LLM Validation (Post-Challenge)

Two experiments run against Qwen3.5-27B locally (vLLM, 192.168.1.109:8000).

**Experiment 1:** Same context (school management system), 6 different section names. temp=0.3, max_tokens=2000.
**Experiment 2:** Same section name in different template contexts (HL vision vs RF result report). temp=0.3, max_tokens=1500.

Full analysis: [experiment_analysis.md](experiment_analysis.md)
Raw data: captured in chat session (Qwen3.5-27B vLLM, 2026-04-10)

### Experiment 1 Results: Each name triggers a DISTINCT cognitive mode

| Section Name | Cognitive Mode | Content Type |
|-------------|---------------|-------------|
| **Value Flow** | Strategic / Value-oriented | Value streams, INPUT→PROCESSING→OUTCOME, "Value Created" column |
| **Diagrams** | Technical / Engineering | Mermaid (ERD, graph TD, swimlane), system architecture, schema |
| **Process Maps** | Operational / BPM | As-Is vs To-Be, pain point annotations, per-step timing |
| **Findings Map** | Analytical / Research | Root cause analysis, hypothesis tree, priority matrix |
| **Visual Overview** | Generic / Unfocused | Mixed architecture — no specific mode activated |
| **Result Visualization** | Narrative / Outcome | "6 Months After Launch", timeline (8:00 AM →...), testimonials |

**Key finding:** Zero overlap between "Value Flow" and "Result Visualization". They are empirically distinct concepts.

### Experiment 2 Results: Context × Name interaction

| | HL Context | RF Context |
|---|-----------|-----------|
| **"Value Flow"** | ✅ Clean strategic output, value principles | ⚠️ OK but adds tech details |
| **"Diagrams"** | ⚠️ CONFUSED — mixed vision/tech | ✅ Pure technical diagrams |

**Key finding:** "Diagrams" in HL = model confusion. "Value Flow" in HL = focused strategic output. Confirms per-template naming decision.

### Hypothesis Updates

| Hypothesis | Analytical status | Empirical status |
|-----------|------------------|-----------------|
| H_pertemplate (visual section) | CONFIRMED (C1) | ✅ **CONFIRMED** — 6 modes + context test |
| H_visionvs (§3.1 ≠ Value Flow) | CONFIRMED (C4) | ✅ **CONFIRMED** — zero content overlap |
| H_valuemaps → Value Flow | REFUTED (C2) | ✅ **CONFIRMED** — "Value Flow" triggers right mode |
| Findings Map for RES | CONFIRMED (C3) | ✅ **CONFIRMED** — research-native output |
| Visual Overview = weak | — | ✅ **CONFIRMED** — generic, unfocused |
| Diagrams wrong for HL | — | ✅ **CONFIRMED** — model produces confused mix |

→ ALL naming decisions now have BOTH analytical AND empirical validation.
→ Proceed to Synthesis (RES)
