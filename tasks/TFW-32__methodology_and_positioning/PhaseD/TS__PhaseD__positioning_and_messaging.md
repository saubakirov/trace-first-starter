# TS — TFW-32 / Phase D: Positioning & Messaging

> **Date**: 2026-04-10
> **Author**: AI (Coordinator)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> **Phase HL**: [HL Phase D](HL__PhaseD__positioning_and_messaging.md)

---

## 1. Objective

Produce positioning spec documents that define TFW's audience hierarchy, value proposition, business-language translation, and section-by-section improvement direction for README.md and .tfw/README.md. This phase is **analytical** — it produces specs, not final copy. The actual rewrite is a separate future task.

## 2. Scope

### In Scope
- Audience persona matrix (3-tier hierarchy with pain points and adoption patterns)
- Unique value proposition articulation (1 paragraph, "generates vs stores")
- Translation table: TFW technical terms → business-friendly equivalents
- README.md improvement spec (section-by-section, before/after)
- .tfw/README.md philosophy paper improvement spec

### Out of Scope
- Actual README rewriting (separate task TFW-33+)
- Marketing copy, landing page, or external comms
- Changes to any .tfw/ core files (conventions, glossary, templates, workflows)
- Fact candidate consolidation (Phase E)

## 3. Affected Files

| File | Action | Description |
|------|--------|------------|
| `PhaseD/audience_personas.md` | CREATE | 3-tier persona matrix |
| `PhaseD/positioning_spec.md` | CREATE | README section-by-section improvement spec + value proposition |
| `PhaseD/translation_table.md` | CREATE | TFW terms → business equivalents |
| `PhaseD/philosophy_improvement.md` | CREATE | .tfw/README.md improvement spec |

**Budget:** 4 new files, 0 modifications. Well within max 8 new, max 14 files, max 1200 LOC.

## 4. Detailed Steps

### Step 1: Write audience persona matrix (`audience_personas.md`)

Create a structured document with 3 tiers. For each tier:

**Tier 1 — Product Leaders (Primary)**
- Who: Product managers, team leads, CTOs of growing teams, founders scaling from 5→50
- Pain: "Decisions made in one session don't propagate. New team members re-learn everything. Knowledge lives in people's heads."
- TFW value: Decisions become traceable. Knowledge compounds across tasks. Any agent (human or AI) resumes from the last checkpoint.
- Adoption pattern: Learn TFW faster than engineers learn business thinking (S10). Need structured autonomy (Shape Up parallel).
- Qualifying question: "How much of your team's knowledge would survive if your top 3 people left tomorrow?"

**Tier 2 — Analysts & Researchers (Core)**
- Who: Data analysts, business analysts, academic researchers, educators
- Pain: "Research iterations lose context. Previous analysis not discoverable. Reports don't reference decisions that drove them."
- TFW value: Multi-iteration research preserves all findings. Knowledge compounds. Methodology works for analytics, writing, education — not just code.
- Adoption pattern: Already structured thinkers. TFW fits their mental model of rigorous documentation.
- Qualifying question: "Can you find your analysis from 3 months ago — and the reasoning behind it?"

**Tier 3 — Product-minded Engineers (Secondary)**
- Who: Software engineers who care about architecture decisions, tech debt tracking, codebase evolution
- Pain: "Why was this built this way? Who decided? What was rejected? Context dies with the chat session."
- TFW value: Architecture decisions preserved. Tech debt tracked structurally. New agent reads traces, not raw code.
- Adoption pattern: Already closest to TFW's current language. Need the "why" behind TFW, not just the "how."
- Qualifying question: "Can a new developer understand your architecture decisions without asking the original team?"

**Universal qualifier:** "Teams and individuals who can't afford to lose context."

### Step 2: Write positioning spec with value proposition (`positioning_spec.md`)

**Section A — Value Proposition (1 paragraph)**

Write a single paragraph articulating TFW's unique position. Must include:
1. The pain: growing teams/projects lose knowledge when decisions don't propagate
2. The mechanism: TFW generates knowledge as a byproduct of working methodology (not stored manually)
3. The differentiator vs Confluence/Notion: "generates vs stores"
4. The team frame: AI agents are team members, not individual assistants
5. The domain breadth: works for code, analytics, writing, education, business processes

**Section B — README.md Improvement Spec**

For each current README section, write before/after direction:

| Section | Current state | Direction | Source |
|---------|--------------|-----------|--------|
| Opening quote | *"The thinking is the product"* | Keep. Strong. Add subtitle: team methodology framing | S9 |
| Description block | Technical, individual-focused | Rewrite: team-focused, pain-point opening. "Growing teams lose knowledge..." | D5, S11 |
| "Who This Is For" | 6 undifferentiated bullets | Rewrite with 3-tier hierarchy. Lead with product leaders. Use qualifying questions. | D9, S10 |
| Quick Start | Good. Agent-first. | Minor: add "For teams: ..." starter prompt for team onboarding | S9 |
| "How It Works" | 4 bullets, strong | Sharpen #3 "Knowledge compounds vs evaporates" with "generates vs stores" contrast | D5 |
| "What's Inside" | Reference table | Keep as-is. Technical users need this. | — |
| "Tool Adapters" | Reference table | Keep as-is. | — |
| "Key Concepts" | Pipeline + links | Update if pipeline changed (already done by Phase A) | — |
| FAQ | 3 questions | Add: "How is TFW different from Confluence/Notion?" → generates vs stores. Add: "Is TFW only for software?" → No, methodology for any domain | D5 |
| Links | Minimal | Add: "Getting Started" → quickstart. Add link to docs site if deployed | — |

**Section C — Competitive Frame**

Document the positioning frame (from HL §3.2):

```
Confluence/Notion ─── "STORES knowledge" ─── requires manual documentation
                                              → decay, stale, nobody reads
                                              
TFW ─────────────── "GENERATES knowledge" ── byproduct of working methodology
                                              → compounds, self-updates, agents READ it
```

Add VLM-3 validated unique features (from RES3 D19):
1. Knowledge Pipeline bundle (lifecycle + research + facts + consolidation)
2. Multi-iteration research with structural enforcement
3. Role Lock (coordinator ≠ executor ≠ researcher ≠ reviewer)
4. Thinking traces as project artifacts (future — TFW-32 S6, VLM-3 D20)
5. Domain-agnostic methodology (not code-specific)
6. Scope budgets calibrated for AI agents
7. Knowledge Gate with configurable consolidation
8. Trace Discipline (filesystem = state machine)

### Step 3: Write translation table (`translation_table.md`)

Create a two-column mapping following the DORA pattern (technical → business-language).

| TFW Term | Business Equivalent | Context |
|----------|-------------------|---------|
| HL (High Level) | Strategic brief | "Map of meaning" — defines why, constraints, rejected alternatives |
| TS (Task Spec) | Work order / Implementation brief | Self-contained: what to do, acceptance criteria, scope limits |
| RF (Result File) | Delivery report | Results, decisions made, observations, deviations logged |
| RES (Research Report) | Investigation report | Structured research: findings, decisions, hypotheses tested |
| ONB (Onboarding Report) | Pre-flight checklist | Executor's understanding check before starting work |
| REVIEW | Quality gate report | Formal checklist: did the delivery meet the spec? |
| Task Board | Project dashboard | Single view of all tasks and their statuses |
| Knowledge Pipeline | Institutional memory engine | Captures, verifies, and compounds knowledge from every task |
| Fact Candidates | Observed findings (unverified) | Raw observations recorded during work. Verified later. |
| Strategic Insights | Domain intelligence | Human-sourced knowledge that can't be learned from project files |
| Scope Budget | Guardrails | Limits per work unit to prevent quality degradation |
| Role Lock | Separation of duties | Different roles have different permissions. No role crossover. |
| Trace | Decision record | The reasoning, constraints, and alternatives behind every change |
| Knowledge Gate | Periodic checkpoint | "Have we captured what we learned?" — prevents knowledge loss |
| KNOWLEDGE.md | Architecture index | Map of project structure, decisions, and legacy systems |
| TECH_DEBT.md | Issue backlog | Known shortcuts and improvements — triaged, not forgotten |
| Pipeline status | Workflow stage | Where a task is in its lifecycle (planning → execution → review → done) |
| Coordinator | Strategic planner | Plans tasks, writes specs, reviews results. Does NOT execute. |
| Executor | Implementer | Reads the spec, does the work, delivers results |
| Researcher | Investigator | Structured investigation between planning and execution |

### Step 4: Write philosophy improvement spec (`philosophy_improvement.md`)

Analyze `.tfw/README.md` and write section-by-section improvement direction:

| Section | Current state | Direction | Source |
|---------|--------------|-----------|--------|
| "The Problem: Knowledge Evaporates" | Strong. Individual-focused ("You open a new session") | Add team dimension: "Your team member opens a new session — and the context you built yesterday is invisible." | S9, S11 |
| "The Thesis: Traces Over Code" | Good philosophy. "Code can be regenerated." | Add explicit team value: "Traces are the team's shared memory." Add "generates vs stores" positioning against knowledge tools | D5 |
| Traditional vs Trace-First table | 4 rows, developer-centric | Add row: "Team knowledge lives in Slack threads and meetings" → "Team knowledge lives in structured traces that any member can read" | S9 |
| "How TFW Works" | Describes ritual. "A task moves through a deterministic lifecycle" | Add: "The same ritual works whether you're a product manager, data analyst, or engineer." Add qualifier: "Teams that can't afford to lose context." | D9 |
| "Values and Principles" | 8 values, well-articulated | No changes needed. Values are strong and domain-agnostic. | — |
| "Anti-patterns" | Ref to conventions.md | Keep. | — |
| "Success Criteria" | 4 criteria, mostly engineering | Reframe: "A TFW project is successful when any team member — human or AI — can resume work from any checkpoint without re-learning the context" | D9, S9 |
| Missing section | — | ADD: "How TFW Compares" — 3-way comparison: TFW vs Confluence/Notion vs no methodology. Pain points each addresses. What each generates vs requires. | D5, G2 |

## 5. Acceptance Criteria

- [ ] 1. `audience_personas.md` has 3 tiers with: Who, Pain, TFW value, Adoption pattern, Qualifying question
- [ ] 2. `audience_personas.md` includes the universal qualifier: "Teams and individuals who can't afford to lose context"
- [ ] 3. `positioning_spec.md` Section A has a single-paragraph value proposition containing: pain, mechanism, differentiator, team frame, domain breadth
- [ ] 4. `positioning_spec.md` Section B covers every current README.md section with before/after direction
- [ ] 5. `positioning_spec.md` Section C documents the competitive frame with "generates vs stores" and lists 8 unique features
- [ ] 6. `translation_table.md` maps ≥15 TFW terms to business equivalents with context column
- [ ] 7. `philosophy_improvement.md` covers every .tfw/README.md section with before/after direction
- [ ] 8. `philosophy_improvement.md` includes proposed "How TFW Compares" section content
- [ ] 9. All files reference their source decisions (D5, D9, S1-S17, VLM-3 RES3) with inline citations
- [ ] 10. No changes to any file outside `PhaseD/` folder

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| Positioning overfit to user's perspective (1 person) | Cross-reference with external patterns (Shape Up, DORA, Scrum Guide). Use qualifying questions as external validation proxy |
| Specs too abstract — future executor can't rewrite README from them | Every section spec includes concrete before/after direction and source citations |
| Translation table oversimplifies — loses precision | Keep both: "HL (High Level) → Strategic brief." TFW term stays primary, business equivalent is alias |
| VLM-3 competitive analysis was from different project context | Filter: only reference VLM-3 findings that survived sycophancy demolition (RES3). Knowledge Pipeline = confirmed. 8 features = confirmed |

> **Cross-references**: D5 (RES1), D9 (RES1), S1-S17 (HL §11), VLM-3 RES3 D19-D20, G2 (gather.md)

---

*TS — TFW-32 / Phase D: Positioning & Messaging | 2026-04-10*
