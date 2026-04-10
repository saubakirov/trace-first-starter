# Gather — Iteration 4: "What do we NOT know?"
> Parent: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> Predecessors: RES1-RES3, [Briefing](briefing.md)
> Goal: Data on per-template naming, HL vision visual concept, "Value Maps" as term.

## Findings

### G1: Amazon Working Backwards — the "outcome preview" concept

Amazon PR/FAQ document structure:
- **Press Release** — written as if the product is ALREADY LAUNCHED. Customer-centric. Date = projected launch
- Key sections: Headline, Problem, Solution, Leader Quote, **Customer Quote** (hypothetical testimonial), Call to Action
- **FAQ** — internal/external questions to vet feasibility

Key principle: **"If it is difficult to write the press release, the product concept itself needs more refinement."**

This maps directly to HL §3.1 "Result Visualization":
- Both = "see the finished picture before work begins"
- Both = written from user/stakeholder perspective
- Both = NOT a process diagram — it's an outcome narrative + visual proof

**Current HL §3.1 name: "Result Visualization"**
Amazon calls it: the Press Release (outcome narrative)
Industry terms: "Outcome Preview", "Future State Vision", "Target State Visualization"

### G2: Two distinct visual concepts identified

From research (VSM/Process Map/Flow Diagram comparison):

| Concept | Purpose | Level | Where in TFW |
|---------|---------|-------|-------------|
| **Outcome preview** | "What does done look like?" — show the result as if achieved | Vision | HL §3.1 |
| **Process/value visualization** | "How does value flow?" — map steps, bottlenecks, structure | Operational/detail | NEW section needed in HL, RF, RES |

These are fundamentally different:
- Outcome preview = WHAT we'll see when done (Amazon Working Backwards)
- Process visualization = HOW value gets created/delivered (Lean/BPMN tradition)

**User confirmed this split:** "вот эта верхняя часть визуал результата — оно должно там и остаться, это не диаграмма и не бизнес процесс"

### G3: "Value Maps" — term analysis

"Value Map" has THREE established meanings in industry:

1. **Value Proposition Map** (Strategyzer/Osterwalder): products → pain relievers → gain creators. Strategic/marketing tool
2. **Value Stream Map** (Lean/Toyota): material + information flow, lead times, waste identification. Operational tool
3. **Business Value Map** (Management): connects strategy to execution via KPIs

None of these = exactly what user wants (a generic section for visual process representation across any domain).

**Problem:** "Value Map" is HEAVILY loaded with Lean/Strategyzer meaning. Using it generically would confuse people who know these frameworks.

### G4: Hybrid naming pattern — common section number, different names

External research confirms the hybrid approach is a recognized best practice:

| Approach | How | Pros | Cons |
|----------|-----|------|------|
| **Unified naming** | Same section title everywhere | Consistency, easy automation | Forces content into generic headings |
| **Per-template naming** | Different title per template | Accurate framing, better cognitive mode per context | Harder to automate collection, more names to learn |
| **Hybrid** | Common section NUMBER + template-specific NAME | Both: automation via number, precision via name | Slightly more complex templates |

Key insight: **Metadata as the real standardizer.** If the collection algorithm reads by section number (§6, §7), the section NAME becomes a free variable — optimized per-template for the best cognitive mode.

This directly validates user's insight: «не проблема заставить агента заглянуть в каждый раздел. в теории мы можем просто иметь один общий номер раздела и как-то его условно назвать»

### G5: Current TFW section map — what exists and what needs naming

| §# | HL | RF | RES | REVIEW | Current name |
|----|----|----|-----|--------|-------------|
| §3.1 | Result Visualization | — | — | — | "Result Visualization" |
| §5 | — | Observations | — | — | "Observations" |
| §6 | — | Fact Candidates | Fact Candidates | Fact Candidates | "Fact Candidates" |
| §7 | — | — | — | — | (does not exist yet) |
| §11 | Strategic Session Insights | — | — | — | "Strategic Session Insights" |
| NEW | (in Target State?) | (process detail?) | (findings viz?) | — | (needs decision) |

Observations:
1. §6 Fact Candidates = same name across RF, RES, REVIEW. Works because the cognitive mode is same: "report facts without interpretation"
2. §11 Strategic Session Insights = HL only. User wants equivalent in RF and RES but possibly with different name
3. §3.1 Result Visualization = HL only. This is the "outcome preview" — Amazon Working Backwards style
4. NEW process/value visualization section = does NOT exist. Needs creation

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Two distinct visual concepts confirmed: outcome preview (HL §3.1) vs process visualization (new section) | Design: per-template naming table |
| "Value Maps" is heavily loaded — not ideally generic | Alternative names for process visualization |
| Hybrid naming (common number + specific name) is validated pattern | Apply to TFW sections |
| Amazon Working Backwards maps directly to HL §3.1 | Name for HL §3.1 — keep or rename? |
| §6 same name works (same cognitive mode everywhere) | §7/§11 — same name or per-template? |

**Sufficiency:**
- [x] External source used? (Amazon PR/FAQ, VSM literature, Value Map definitions, hybrid naming practices)
- [x] Briefing gap closed? (All 3 directions have data)

**Deep mode criteria:**
- [x] Hypothesis tested? H_pertemplate (hybrid pattern found), H_visionvs (two concepts confirmed), H_valuemaps ("Value Maps" = loaded term)
- [x] Counter-evidence sought? "Value Maps" has 3 incompatible meanings. Hybrid naming adds complexity

Stage complete: YES
→ User decision: ___
