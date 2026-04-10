# Extract — Iteration 4: "What do we NOT see?"
> Parent: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> Predecessors: RES1-RES3, [Gather](gather.md)
> Goal: Design per-template naming, separate two visual concepts, define collection algorithm.

## E1: The two visual concepts — naming each

From Gather G2: HL §3.1 and process diagrams are FUNDAMENTALLY different. They need different treatment.

### Concept 1: "Outcome Preview" (HL §3.1)

What it is: Amazon Working Backwards. "Write as if it's already done." Stakeholder perspective. Not a diagram — it's a visualization of the RESULT.

Current name: **"Result Visualization"** (HL template §3.1)

| # | Name candidate | Framing | Pro | Con |
|---|---------------|---------|-----|-----|
| 1 | **Result Visualization** (current) | "Show the result" | Works. Already in use. Clear | "Visualization" sounds technical. Could mean diagram |
| 2 | **Outcome Preview** | "Preview the finished product" | Industry term. Amazon-adjacent. Non-technical | Learning curve vs current name. "Preview" = incomplete? |
| 3 | **Future State** | "Show to-be state" | Standard PM term. Crystal clear | Generic. Doesn't carry the "imagine it's done" prompt |
| 4 | **Finished Picture** | "Show what done looks like" | Colloquial, vivid, strong prompt | Too informal for methodology. Not used in industry |
| 5 | **Press Release** | "Write the announcement" | Exact Amazon term. Strong framing | Too specific. Not every task has a "press release" |

**Analysis:** Current name "Result Visualization" works. It's in the §3.1 position within "Target State (To-Be)" — which is already the right container. The INSTRUCTIONS matter more — they should say: "Write as if the work is done. Show tables, comparisons, output samples. This is NOT a process diagram."

The name doesn't need to change. The instructions need to carry the Amazon Working Backwards framing. RES3 D17 confirmed: instructions carry the framing load.

**Recommendation E1:** Keep **"Result Visualization"** as §3.1 name. Enhance instructions: add "Working Backwards" framing — show the result as if achieved. Explicitly state: "This is NOT a process diagram or system architecture."

### Concept 2: Process/Value visualization (NEW section)

What it is: diagrams showing HOW value flows, HOW the process works, WHERE bottlenecks are. This is the Lean/BPMN tradition.

This section does NOT YET EXIST as a standard section. RES3 D17 proposed adding "Diagrams" to RF and RES. User now questions: maybe it should also be in HL? And maybe "Value Maps" is better?

#### "Value Maps" — viability check

From Gather G3, "Value Map" has 3 conflicting industry meanings:
1. Value Proposition Map (Strategyzer) — customer jobs/pains/gains
2. Value Stream Map (Lean) — material/information flow
3. Business Value Map (Management) — strategy-to-execution

**Problem:** Using "Value Maps" generically would be understood as Lean VSM by anyone who knows Lean, and as Strategyzer canvas by anyone who knows that. Neither is what TFW means.

**Counter-argument:** TFW could DEFINE its own meaning. "In TFW, Value Maps = visual representation of where value is created and delivered." But this creates a learning curve AND conflicts with established terms.

#### Alternative names for process visualization section

| # | Name | Framing | HL fit | RF fit | RES fit | Cross-domain? |
|---|------|---------|--------|--------|---------|:---:|
| 1 | **Diagrams** (RES3 D17) | "Draw diagrams" | ⚠️ tech | ✅ | ✅ | ✅ |
| 2 | **Value Maps** (user) | "Map value flow" | ✅ | ❌ tech detail ≠ value map | ❌ | ❌ loaded |
| 3 | **Process Maps** | "Map the process" | ✅ for value flow | ⚠️ not all = process | ❌ | Partial |
| 4 | **Flow Diagrams** | "Show the flow" | ✅ | ✅ | ⚠️ | ✅ |
| 5 | **System View** | "Show the system" | ✅ | ✅ | ⚠️ | ✅ |

I notice: this is the SAME question as RES3. And RES3 chose "Diagrams." User is now pushing back on "Diagrams" specifically for HL — because HL is about VALUE, not about technical diagrams.

**But wait.** The user's insight is deeper: MAYBE this section should have DIFFERENT NAMES per template. This is H_pertemplate.

## E2: Per-template naming — the core design decision

User's insight: «разные артефакты это разные фрейминги, разный майндсет. возможно стоит подобрать каждое под каждое»

This challenges RES3 D17 ("use 'Diagrams' everywhere"). Let me evaluate:

### What changes between templates

| Template | Mindset | What goes in § Visual | Name should prompt... |
|----------|---------|----------------------|----------------------|
| **HL** | Coordinator. Vision. "Where value flows" | Value delivery flow, business process overview, user journey | Strategic thinking. Show the big picture of value/process |
| **RF** | Executor. Results. "What was built/done" | Technical architecture, process detail, data flows, API sequences | Precise, technical documentation of what was implemented |
| **RES** | Researcher. Findings. "What we discovered" | Concept maps, comparison diagrams, decision trees, research findings | Analytical visualization of knowledge gained |

These ARE different cognitive modes. "Diagrams" works for RF (engineering output). But for HL, you want the agent thinking about VALUE and FLOW, not about UML.

### Design option: Hybrid naming

Common section marker: **§ Visual** (a generic label in conventions.md for the collection algorithm)

Per-template names:

| Template | Section name | Cognitive prompt |
|----------|-------------|-----------------|
| HL | **Value Flow** | "Show how value moves from user to outcome" |
| RF | **Diagrams** | "Draw technical diagrams of what was built" |
| RES | **Findings Map** | "Visualize what we discovered" |
| REVIEW | (not needed) | — |

**Collection algorithm:** `/tfw-knowledge` and `/tfw-docs` look for the section by convention reference: "look for the visual section in each artifact." Template instructions specify the exact heading. Glossary entry: "Visual Section — each template has a named visual section. HL = Value Flow, RF = Diagrams, RES = Findings Map."

### Does per-template naming work for §6 and §7/§11?

| §# | HL | RF | RES | Same name everywhere? | Per-template better? |
|----|----|----|-----|:----:|:----:|
| §6 Fact Candidates | — | Fact Candidates | Fact Candidates | ✅ Same cognitive mode everywhere (pure reporting) | ❌ No benefit |
| §7/§11 Strategic Insights | Strategic Session Insights | (does not exist yet) | Strategic Insights (RES3) | ⚠️ Different | ✅ Maybe |

**For §6:** Same name works because the cognitive mode IS the same — "report facts without interpretation." Whether you're writing an RF or a RES, §6 behavior is identical. No benefit from per-template naming.

**For §7/§11 Strategic Insights:**
- In HL (§11): captured during PLANNING. The agent captures human direction for the task ahead. Framing = "what the stakeholder told us that shapes this work"
- In RF (§7, if added): captured during EXECUTION. The agent captures human corrections and domain knowledge mid-flight. Framing = "what the human revealed while we worked"
- In RES (§7, if added): captured during RESEARCH. The agent captures human steering and domain signals. Framing = "what the human saw that research didn't"

These ARE different framings. But RES3 tested "Strategic Insights" empirically — it triggers the deepest analytical mode regardless of context. The name works because "Strategic" elevates everything. Per-template naming would sacrifice the proven prompt for marginal framing gain.

**Recommendation E2:** 
- **§ Visual section: YES — per-template naming.** Different cognitive modes (vision vs engineering vs analysis). Benefit > cost
- **§6 Fact Candidates: NO — keep one name.** Same cognitive mode everywhere
- **§7/§11 Strategic Insights: BORDERLINE.** One name with qualifier (Planning / Execution / Research) is sufficient. Per-template naming is marginal here because the empirically proven "Strategic Insights" prompt is too valuable to sacrifice

## E3: Revised complete section architecture

Putting it together:

```
                   HL                    RF                    RES
                   ────                  ────                  ────
§1-§4              Vision, State,       What Was Done,        Context, Briefing,
                   Phases...             Decisions...          Decisions...

§3.1               Result               —                     —
                   Visualization
                   (Working Backwards)

§ Visual           Value Flow            Diagrams              Findings Map
(NEW — per-name)   (value delivery,      (architecture,       (concept maps,
                    process overview,     sequence, ERD,       comparison,
                    user journey)         API flows)           decision trees)

§5                 —                     Observations          —
                                         (tech debt)

§6                 —                     Fact Candidates       Fact Candidates
                                         (project facts)       (project facts)

§7/§11             Strategic Insights    Strategic Insights    Strategic Insights
                   (Planning)            (Execution)           (Research)
```

### What this design gives us:

1. **HL §3.1 "Result Visualization"** stays as is — with enhanced Working Backwards instructions. This is NOT a diagram. It's "see the result."
2. **NEW § Visual section** — per-template named. HL = "Value Flow", RF = "Diagrams", RES = "Findings Map". Each gets its own instructions in the template
3. **§6 Fact Candidates** — unchanged, one name everywhere
4. **§7/§11 Strategic Insights** — one name everywhere, with qualifier in parentheses (Planning / Execution / Research)

### Collection algorithm

For `/tfw-knowledge`:
```
FOR EACH artifact in task folder:
  READ §6 (Fact Candidates) → collect into fact candidates pool
  READ §7 or §11 (Strategic Insights *) → collect into strategic insights pool
```

For `/tfw-docs`:
```
FOR EACH artifact in task folder:
  READ § Visual section (any name: Value Flow, Diagrams, Findings Map) → 
    assess which diagrams should update KNOWLEDGE.md §1 or knowledge/ topic files
```

The agent doesn't need to know the exact section name — it reads the template and finds the visual section by position/convention. Or simpler: the convention says "look for the section between §X and §Y."

But actually — the agents already read the whole artifact. The section name is a PROMPT (tells the agent what to write), not a SEARCH TAG (tells the collector what to find). The collector reads everything anyway.

**This means:** Per-template naming has ZERO collection cost. The agent reads the full file. Different names are purely a prompting benefit.

## Checkpoint

| # | Finding | Decision needed |
|---|---------|----------------|
| E1 | HL §3.1 "Result Visualization" = stays. Enhance instructions with Working Backwards framing. NOT a diagram | Coordinator confirms |
| E2a | Visual section: per-template naming. HL = "Value Flow", RF = "Diagrams", RES = "Findings Map" | Coordinator picks names |
| E2b | §6 Fact Candidates: keep one name (same cognitive mode) | Coordinator confirms |
| E2c | §7/§11 Strategic Insights: keep one name + qualifier (Planning/Execution/Research) | Coordinator confirms |
| E3 | Complete section architecture designed | Coordinator reviews |

**Sufficiency:**
- [x] External source used? (Gather G1-G5)
- [x] Briefing gap closed? (All 3 hypotheses addressed with design)

**Deep mode criteria:**
- [x] Hypothesis tested? H_pertemplate (YES: per-template for visual, NO for §6/§7)
- [x] Counter-evidence sought? "Value Maps" rejected (loaded term). Per-template for §6 rejected (no benefit). Per-template for §7 rejected (empirical prompt too valuable)
- [x] Metacognitive check: I notice the answer is nuanced — not "all per-template" or "all unified." The decision criterion is: "Does the cognitive mode CHANGE between templates?" If yes → per-template. If no → unified.

Stage complete: YES
→ User decision: ___
