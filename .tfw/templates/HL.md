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

> **Working Backwards:** Show the outcome as if it's already achieved. Imagine it's done —
> what does the user see? What changed? Write from the perspective of "6 months after launch."
>
> Choose the format that fits:
> - **Before → After tables** — state comparison with real data
> - **Outlines / mockups** — document structure, UI sketches, report layout
> - **Sample output** — example paragraph, data snippet, formula result
> - **Narrative** — timeline of a user's day after the change ships
>
> This is NOT a process diagram or architecture flow — those belong in §3.2 Value Flow.
> Goal: executor and user must see the "finished picture" before work begins.

### 3.2 Value Flow

> Visualize HOW value gets created — the machine, not the outcome.
> Show the flow from user pain → pipeline steps → value delivered.
>
> Formats:
> - **ASCII flow** — `INPUT → PROCESSING → OUTCOME` with value labels
> - **Mermaid diagram** — for complex multi-path flows
> - **Value stream table** — columns: Step, Input, Transformation, Value Created
>
> This is NOT the outcome preview (§3.1) — this is the process that creates the outcome.

## 4. Phases
Break into Phases (A, B, C...) with priorities 🔴🟡🟢.
Each Phase = separate TS→RF cycle.

### Phase A: {title} 🔴

> **For multi-phase tasks (3+ phases):** include Context block per phase.
> Phase coordinator reads ONLY this block + referenced files — not all research.
>
> **Requires:** {Independent | Requires: Phase X ✅}
>
> **⚠️ Shared files with Phase X:** {files modified by multiple phases — omit if none}
>
> **Context for coordinator:** numbered list of files + specific §/D-references to read before writing Phase TS
>
> **Key decisions:** D-numbers with inline one-line summaries
>
> **⚠️ Cascade dependency:** {if modifying workflow steps — warn about adjacent steps. Omit if none}
>
> **Deliverables:** numbered list

- {bullet list of deliverables — for simple tasks without Context block}

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

### 7.2 Knowledge Citations

> Coordinator: scan PV Index (glossary.md → Project Values).
> Full scan of priorities 1-4 (README Values, philosophy.md, KNOWLEDGE.md §1, conventions.md).
> Skim priorities 5-7 for relevant items.
> Reviewer will verify these links resolve to real items.

| # | Source | Item | How it applies |
|---|--------|------|----------------|

> For new projects with empty KNOWLEDGE.md: "No applicable knowledge items — project in bootstrap phase."

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

## 11. Strategic Insights (Planning)

> **Cognitive mode:** Deep analytical synthesis. Capture human-sourced domain knowledge,
> then ADD implications — what does this insight mean for the project's direction?
>
> **Human-Only Test:** Would this insight be unknown without the user saying it?
> If an agent can discover it by reading code — it's NOT a strategic insight, it's a Fact Candidate (§6).
>
> **High-value signals to watch for:**
> - User corrects direction or reframes the problem
> - User expresses emotion (frustration, excitement, urgency)
> - User shares domain knowledge not in any artifact
> - User makes strategic decisions between alternatives
> - User reveals business context, stakeholder priorities, or constraints
>
> **Categories:** conventions.md §10.1.

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | {insight} | {category — see §10.1} | User, {context} |

> **Cross-references**: use Reference Format (e.g. `RF TFW-18`, `D24`, `TD-72`). See compilable_contract.md §2. Build script resolves to hyperlinks.

---

*HL — {PREFIX}-{N}: {Title} | YYYY-MM-DD*
