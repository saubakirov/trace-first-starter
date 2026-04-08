# HL — {PREFIX}-{N}: {Title}

> **Date**: YYYY-MM-DD
> **Author**: {author}
> **Status**: 📝 HL_DRAFT — Awaiting review

---

## 1. Vision
{Strategic narrative: what we want and why — 2-3 sentences. Write as if it's already done.}

**Impact:** {What changes when this is done — for users, team, product}

> Key quote from the stakeholder perspective — what they would say when this ships.

## 2. Current State (As-Is)
Current state: problems, structure, metrics, constraints.
Tables with REAL data where applicable.

## 3. Target State (To-Be)
What it should look like after. Clear deliverables.
Tables comparing As-Is → To-Be where applicable.

### 3.1 Result Visualization

> Show the outcome as if it's already achieved. Choose the format that fits:
> - **Diagrams** (architecture, flow, structure) — ASCII, mermaid, or hand-drawn
> - **Before → After tables** — state comparison
> - **Outlines / mockups** — document structure, UI sketches, report layout
> - **Sample output** — example paragraph, data snippet, formula result
>
> Goal: executor and user must see the "finished picture" before work begins.

## 4. Phases
Break into Phases (A, B, C...) with priorities 🔴🟡🟢.
Each Phase = separate TS→RF cycle.

### Phase A: {title} 🔴
- {bullet list of deliverables}

### Phase B: {title} 🟡
- {bullet list of deliverables}

## 5. Definition of Done (DoD)
Numbered list. Each item starts with ✅.
Must cover all deliverables from §4 Phases.

- ✅ 1. {Criterion 1}
- ✅ 2. {Criterion 2}

## 6. Definition of Failure (DoF)
Numbered list. Each item starts with ❌.
What to do on failure: rollback, rethink, escalate.

- ❌ 1. {Failure condition 1}
- ❌ 2. {Failure condition 2}

**On failure:** {action plan}

## 7. Principles
Design philosophy. Non-negotiable rules.

1. **{Principle name}** — {description}
2. **{Principle name}** — {description}

## 7.1 Quality Contract (optional, for multi-phase tasks)
Anti-patterns, style rules, and constraints that MUST be copied into each Phase TS.
Purpose: prevent executor agents from drifting.
Only needed for tasks where consistency across phases matters.

## 8. Dependencies
| Dependency | Status |
|------------|--------|
| {dependency} | ⬜ / ✅ |

## 9. Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| {risk} | Low/Medium/High | Low/Medium/High | {mitigation} |

## 10. RESEARCH Case

### Blind Spots
- {What we do NOT know that could affect our approach}

### Hypotheses

| # | Hypothesis | Status |
|---|----------|--------|
| H1 | {Statement to verify} | open |

> **Filter:** Each hypothesis: "If proven false, would our approach change?" If no — remove.

### Risks of Not Researching
{What happens IF we skip RESEARCH}

### Proposed RESEARCH Focus
1. **Gather**: {specific question}
2. **Extract**: {specific question}
3. **Challenge**: {specific question}

### Why Not Just...?
- Why not {obvious alternative A}? — {reason}
- Why not {obvious alternative B}? — {reason}

## 11. Strategic Session Insights

> **Human-Only Test:** Would this insight be unknown without the user saying it?
> Watch for: corrections, emotions, domain knowledge, strategic decisions, business context.
> Categories: conventions.md §10.1.
>
> **High-value signals to watch for:**
> - User corrects direction or reframes the problem
> - User expresses emotion (frustration, excitement, urgency)
> - User shares domain knowledge not in any artifact
> - User makes strategic decisions between alternatives
> - User reveals business context, stakeholder priorities, or constraints

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | {insight} | {category — see §10.1} | User, {context} |

> **Cross-references**: use §16 Reference Format (e.g. `RF TFW-18`, `D24`, `TD-72`). Build script resolves to hyperlinks.

---

*HL — {PREFIX}-{N}: {Title} | YYYY-MM-DD*
