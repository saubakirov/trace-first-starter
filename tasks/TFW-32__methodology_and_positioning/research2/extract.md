# Extract — Iteration 2: "What do we NOT see?"
> Parent: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> Predecessor: [RES1](../RES__TFW-32__methodology_and_positioning.md), [Gather2](gather.md)
> Goal: Design decisions for naming, visualization, business processes, multi-iteration.

## Findings

### E1: Naming — honest alternatives analysis (no status-quo bias)

**The question:** Is "Strategic Insights" genuinely the best name, or am I validating user preference?

**Test: Apply D28 strictly.** The name must tell the agent:
1. WHAT to look for (target)
2. WHERE it comes from (source)
3. WHY it matters (value)

**6 candidates tested:**

| # | Name | What agent looks for | Source signal | Risk | D28 score |
|---|------|---------------------|-------------|------|-----------|
| A | **Strategic Insights** (current) | Business context, motives, priorities, domain knowledge | Human-only. Synthesis-mode | "Strategic" might over-narrow: agent skips non-strategic human knowledge (e.g., "we tried X and it failed" — is that strategic?) | 7/10 |
| B | **Knowledge Candidates** (RES1 D2) | Anything that could be knowledge | Human-sourced | Too broad — triggers retrieval mode. Agent writes everything | 3/10 |
| C | **Domain Signals** | Domain-specific facts, market rules, business logic | Human + external research | Misses stakeholder emotions, priorities, corrections | 5/10 |
| D | **Stakeholder Intelligence** | Priorities, constraints, decisions, politics, emotions | Human-only | Too corporate. Misses pure domain knowledge (e.g., "revenue is seasonal") | 6/10 |
| E | **Strategic Signals** | Strategic decisions, priorities, corrections, domain patterns | Human-only, synthesis | "Signal" implies filtering — agent looks for high-value items only. Tighter than "Insight" | 8/10 |
| F | **Context Signals** | Background, constraints, domain, motives, emotions — anything that shapes decisions | Human + environment | "Context" is broad but "Signal" narrows it: only what changes decisions. Inclusive but filtered | 7/10 |

**Honest assessment of "Strategic Insights" (option A):**
- PRO: "Strategic" frames synthesis mode (confirmed by external research). Agent doesn't list facts, it identifies implications
- PRO: Current name, already works, no migration cost
- CON: "Strategic" might make agent skip NON-strategic human input: emotional signals, personal experience ("I tried this, it broke"), cultural context. These are valuable but an agent might not classify them as "strategic"
- CON: "Insight" implies the agent must generate the insight, not just record it. Sometimes the human IS the insight

**Alternative "Strategic Signals" (option E):**
- PRO: "Signal" implies detection + filtering (Agent: "Is this a signal I should capture?"). Better alignment with Human-Only Test
- PRO: "Strategic" keeps the D28 behavioral frame
- CON: "Signal" is less common in methodology language — might confuse human users who aren't signal-processing-minded

**Counter-test: When does "Strategic Insights" fail?**
User says: "Мне понравилась возможно запускать несколько ресерчей отдельно, друг за другом." 
Is this a "Strategic Insight"? It's a PROCESS preference, not strategy. Agent might hesitate to capture it under "Strategic." But it IS exactly the kind of human-only knowledge that matters.

Under "Strategic Signals" — agent sees "signal" and asks: "Does this change how we work? Yes → capture."
Under "Context Signals" — same behavior, broader net.

**Decision recommendation:** Keep "Strategic" framing (D28 confirmed — synthesis mode). But acknowledge the gap: rename from "Strategic Session Insights" to one of:
- **Option A (conservative):** "Strategic Insights" (drop "Session" — already proposed in RES1 E2)
- **Option E (sharper):** "Strategic Signals" — adds filtering behavior

Both are improvements over RES1's "Knowledge Candidates." The real choice is between A and E. This is a coordinator decision, not a researcher one.

### E2: Fixing "Fact Candidates" (§6) — the actually vague name

**Current problem:** "Fact Candidates" in RF §6 and RES §FC is a catch-all. Agent doesn't know what KIND of thing to capture.

**But wait — is this actually a problem?** Let me check what RF §6 actually captures in practice.

Looking at RES1 FC1-FC9:
- FC1: "Documentation = facts about the project..." — user-sourced definition → should be Strategic Insight
- FC2: "Product-oriented people learn TFW faster..." — user-sourced stakeholder insight → should be Strategic Insight
- FC3: "TFW = team tool..." — user-sourced philosophy → should be Strategic Insight
- FC6: "SECI model maps to TFW..." — research finding → documentation/methodology knowledge
- FC7: "Competitive positioning..." — research finding → documentation
- FC9: "Orchestration of docs+knowledge..." — research design → documentation

**Pattern:** RES1's Fact Candidates are a MIX of:
1. Human-sourced strategic knowledge (FC1-FC5, FC8) — should be in Strategic Insights
2. Research-derived findings (FC6-FC7, FC9) — operational/methodology observations

The problem: researcher put human-only insights into "Fact Candidates" because the RES template has no "Strategic Insights" section (only HL has §11).

**Fix options:**

| Option | Change | Impact |
|--------|--------|--------|
| X1: Add "Strategic Insights" section to RES and RF templates | Each artifact captures BOTH types explicitly | More sections, but each is precise |
| X2: Keep "Fact Candidates" but add subsection headers | §6a Operational, §6b Strategic | Minimal template change, agent still writes to one section |
| X3: Rename "Fact Candidates" → "Project Observations" and add "Strategic Insights" | Two sections with precise names | Clean separation, but "Observations" already exists in RF §5 |

**Recommendation: X1 — add "Strategic Insights" section to RES and RF templates.**
- HL §11 already has it → extend to RES and RF
- RF §5 Observations = agent technical findings (stays)
- RF §6 Fact Candidates = becomes operationally scoped: agent-observable patterns about the project itself
- RF §7 (new) or integrated: Strategic Insights = human-sourced domain knowledge captured during execution
- RES: add Strategic Insights section after Fact Candidates

This resolves TD-76 DIFFERENTLY from RES1: instead of renaming everything, EXTEND the precise naming to all artifacts.

### E3: Visualization section — naming options with framing analysis

**The problem:** One name across all artifacts, but different content per context. The name must FRAME what the agent draws.

**Testing 5 name candidates against arc42 and D28:**

| # | Section Name | What agent draws in HL | What agent draws in RF | What agent draws in RES | Framing quality |
|---|-------------|----------------------|----------------------|------------------------|-----------------|
| V1 | **Diagrams** | Architecture vision | Implementation detail | Research discoveries | Neutral — doesn't specify PURPOSE. Agent might skip if "no diagram needed" | 4/10 |
| V2 | **Visual Map** | Value flow map | System/data flow maps | Concept maps, findings | "Map" implies spatial relationships. Misses sequences, timelines | 5/10 |
| V3 | **Process & Flow** | Value delivery flow | API/DB/sequence flow | Research flow/findings | "Process" is specific to flows — excludes architecture diagrams, mockups | 6/10 |
| V4 | **Blueprints** | Vision blueprint | Technical blueprint | Research blueprint | "Blueprint" = planning orientation. Doesn't fit RF (result, not plan) | 4/10 |
| V5 | **Visual Evidence** | "Here's what it should look like" | "Here's what was built" | "Here's what we found" | "Evidence" implies PROOF. Agent creates visuals that DEMONSTRATE something. Works across contexts | 7/10 |
| V6 | **Schemas** (RU: Схемы) | Value delivery schema | Technical schemas | Analytical schemas | "Schema" = structured representation. Works in both RU and EN. But might be confused with DB schemas | 6/10 |

**Additional consideration from user input:**
> "Везде должно быть одна общая глава с одним четким названием, которая на стадии знаний будет куда-то собираться"

The name must also work as a COLLECTION target during 📚 KNW. During knowledge consolidation, all "Visual Evidence" sections from all artifacts → collected into knowledge as reference diagrams.

**I notice:** HL §3.1 "Result Visualization" already exists — it's close to V5 but narrower. Could be evolved.

**My concern with all options:** The section name alone won't ensure agent draws the RIGHT thing. The INSTRUCTIONS inside the section (like HL §3.1 currently has) are what guide behavior. The name is a trigger, the instructions are the behavior.

**Design:** One name + per-artifact instruction block.

```
## {Section Name}
> {Per-artifact instruction — changes by template}
```

With this pattern, V1 "Diagrams" or V5 "Visual Evidence" both work — the instruction block does the real framing. V1 is simpler, V5 is more behaviorally loaded.

**This needs more testing.** Recommend parking for iteration 3 with user input on preferred direction.

### E4: Multi-iteration research — control file and enforcement design

**From lived experience (this session = iteration 2):**

What I needed at session start:
1. Which hypotheses were tested (and results)
2. Which hypotheses were NOT tested (and why)
3. What NEW questions emerged during RES1
4. User's satisfaction with RES1 findings

What I had to manually reconstruct:
- Re-read entire HL (291 lines)
- Re-read entire RES1 (101 lines)
- Re-read all 4 stage files (~500 lines total)
- Parse checkpoint results from each stage

**What iterations.yaml SHOULD contain (minimal viable state):**

```yaml
task: TFW-32
min_iterations: 2  # set by coordinator
current: 2

log:
  - iteration: 1
    folder: research/
    res_file: RES__TFW-32__methodology_and_positioning.md
    hypotheses_tested: [H1, H2, H3, H5, H7, H8]
    hypotheses_deferred: [H6]
    decisions: [D1, D2, D3, D4, D5, D6, D7, D8, D9]
    gaps:
      - "H6 (visualization) — not investigated"
      - "D2 naming — 'Knowledge Candidates' may be too vague"
      - "D4 (iterations.yaml) — designed but untested"
      - "Business process representation — not covered"
    new_hypotheses: []
    researcher_note: "H6 deferred without investigation. H2 deferred pragmatically. D4 is least validated."
    
  - iteration: 2
    folder: research2/
    res_file: null  # pending
    hypotheses_tested: [H5b, H6, H6b, H7b]
    hypotheses_deferred: []
    decisions: []
    gaps: []
    new_hypotheses: [H5b, H6b, H7b]
    researcher_note: null
```

**Researcher exit protocol (end of each iteration):**

```markdown
## Iteration Status
- **Iteration:** {N} of {min_iterations}
- **Tested:** {list}
- **Deferred/Remaining:** {list}  
- **Gaps discovered:** {list}
- **New hypotheses:** {list or "none"}

### Recommendation
{CONTINUE / SUFFICIENT}
- If CONTINUE: "Gaps remain. Launch `/tfw-research` iteration {N+1} in a new agent. Focus: {gaps + new hypotheses}"
- If SUFFICIENT: "All hypotheses tested. Recommend proceeding to `/tfw-plan` for TS."

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.
```

**Coordinator gate (plan.md extension):**
- After receiving RES from researcher, coordinator checks iterations.yaml
- If `current < min_iterations` → MUST launch next iteration (no bypass)
- If `current >= min_iterations` AND researcher says SUFFICIENT → may proceed to TS
- If `current >= min_iterations` AND researcher says CONTINUE → coordinator decides
- Coordinator can INCREASE min_iterations at any point

**Key enforcement: min_iterations is a HARD FLOOR.**
User's point: "без ямла все закончится на фаст ран" — the YAML IS the structural enforcement. Without it, the researcher writes "done" and the coordinator has no gate to check.

### E5: Two-level business process representation

**Design based on user input + BPMN + VSM patterns:**

**Level 1 — HL (Vision):** Value Delivery Flow
```
User/Trigger → [Step 1] → [Step 2] → ... → Value/Result
```
- ASCII or mermaid
- Shows: who triggers, what flows, where value is delivered
- Purpose: "Does the executor understand WHERE the value ends?"
- Abstraction: business-level (no technical details)

**Level 2 — RF (Result):** Technical Process Detail
```
API Call → DB Query → Transform → Response → UI Update
```
- Sequence diagrams, data flow, API contracts
- Shows: exact implementation of the value flow
- Purpose: "Can the next agent reproduce this?"
- Abstraction: implementation-level

**Both levels live in the visualization section** (whatever it's named). The section instructions differ per template:
- HL template: "Show the value delivery flow — from trigger to outcome"
- RF template: "Show the technical process — databases, APIs, sequences"
- RES template: "Show research findings visually — concept maps, relationship diagrams, comparison matrices"

## Checkpoint

| # | Finding | Status | Open question |
|---|---------|--------|---------------|
| E1 | "Strategic Insights" is good but not perfect. "Strategic Signals" might be sharper. Both beat "Knowledge Candidates" | Options A vs E for coordinator | Need user input on "Insight" vs "Signal" |
| E2 | Fix §6 "Fact Candidates" by adding Strategic Insights section to RES/RF templates (X1) | Design ready | Does this create too many sections? |
| E3 | Visualization section name: V1 "Diagrams" vs V5 "Visual Evidence" — instructions matter more than name | Needs more testing | Park for iteration 3 |
| E4 | iterations.yaml format + researcher exit protocol + coordinator hard gate | Design ready | Insertion point in plan.md |
| E5 | Two-level business process: HL=value flow, RF=technical detail | Design ready | Where does RES fit? |

**Sufficiency:**
- [x] External source used? (arc42, C4, BPMN, VSM, naming research — all from Gather)
- [x] Briefing gap closed? (all 4 hypotheses have design proposals)

**Deep mode criteria:**
- [x] Hypothesis tested? H5b: BOTH "Strategic Insights" and "Knowledge Candidates" tested honestly. Neither is perfect — "Strategic Signals" is a third option
- [x] Counter-evidence sought? Against "Strategic Insights": tested edge case where process preference ≠ strategy. Against keeping names: tested if Fact Candidates is actually problematic (it is — FC1-FC5 from RES1 prove misclassification)

**Metacognitive check:** Found something uncomfortable — "Strategic Insights" has a real gap (non-strategic human knowledge gets missed). I could have just confirmed user preference but the edge case test revealed a genuine weakness. Also found that the REAL fix for TD-76 is extending Strategic Insights to RES/RF, not renaming it.

Stage complete: YES
→ User decision: ___
