# Audience Persona Matrix — TFW Positioning

> **Source decisions**: D5 (RES1), D9 (RES1)
> **Source insights**: S1, S2, S9, S10, S11 (HL §11)
> **Source research**: G2 (gather.md — Shape Up / DORA / Scrum Guide patterns)
> **Briefing**: Q3 — "Product people learn TFW faster than engineers learn business thinking"

---

## Universal Qualifier

**"Teams and individuals who can't afford to lose context."**

This qualifier:
- Includes solo practitioners working across sessions (analysts, researchers, writers)
- Includes teams of any size where decisions must propagate (product orgs, cross-functional teams)
- Includes AI-augmented workflows where agents change between sessions
- Excludes hobbyists and one-off project users (acceptable loss per D9)
- Maps to the root pain: knowledge evaporates when context doesn't persist

---

## Tier 1 — Product Leaders (Primary)

| Dimension | Detail |
|-----------|--------|
| **Who** | Product managers, team leads, CTOs of growing teams (5→50 people), founders scaling operations, heads of departments managing cross-functional work |
| **Pain** | "Decisions made in one session don't propagate to the next person. New team members re-learn everything from scratch. Knowledge lives in people's heads — and walks out the door when they leave. We can't explain why we built it this way." |
| **TFW Value** | Every decision becomes traceable — the "why" is preserved alongside the "what." Knowledge compounds across tasks instead of evaporating between sessions. Any team member — human or AI — resumes from the last checkpoint without re-explanation. The product knows its own history, limitations, and purpose. |
| **Adoption Pattern** | Product leaders learn TFW faster than engineers learn business thinking (S10). They already think in structured decisions, constraints, and trade-offs. TFW formalizes what they already do informally — but adds persistence and traceability. Similar to Shape Up's model of structured autonomy: leaders shape the work, teams execute with full context. |
| **Qualifying Question** | *"How much of your team's knowledge would survive if your top 3 people left tomorrow?"* |
| **Anti-signal** | Teams with no turnover, no AI usage, and no cross-session work have low TFW need. |

### Why Primary?

Product leaders feel the pain most acutely because they're responsible for continuity across people, sessions, and time. Engineers can re-read code. Analysts can re-run queries. But the strategic context — why this approach, which alternatives were rejected, what constraints drove the decision — that lives in the product leader's head. TFW captures it structurally.

> *"Any growing business suffers from communication gaps, decentralized decision-making, information not flowing up and down."* — S11

---

## Tier 2 — Analysts & Researchers (Core)

| Dimension | Detail |
|-----------|--------|
| **Who** | Data analysts, business analysts, academic researchers, educators developing curriculum, anyone who builds knowledge iteratively across sessions |
| **Pain** | "My research iterations lose context. I can't find my analysis from 3 months ago — and if I find it, I can't find the reasoning behind it. Reports don't reference the decisions that drove them. Every new analysis starts from scratch because previous knowledge isn't structured." |
| **TFW Value** | Multi-iteration research preserves all findings — hypotheses tested, alternatives rejected, evidence gathered. Knowledge compounds: each task adds verified facts to a growing knowledge base. The methodology works for analytics, writing, education, and research — not just code. Traces make results reproducible: another analyst can follow the reasoning chain and validate or extend the work. |
| **Adoption Pattern** | Already structured thinkers — they document methodology, cite sources, track decisions. TFW fits their mental model of rigorous documentation. The lifecycle (plan → research → specify → execute → review) mirrors academic research and analytical workflows. They often self-select after seeing the research stage (RES artifact). |
| **Qualifying Question** | *"Can you find your analysis from 3 months ago — and the reasoning behind it?"* |
| **Anti-signal** | Ad-hoc analysts who don't iterate or build on previous work. One-off report generators. |

### Why Core?

Analysts and researchers represent the natural "middle ground" — they already value structured knowledge but currently lack the infrastructure to preserve it across sessions. They produce the raw material (analyses, findings, decisions) that TFW is designed to capture. They're the heaviest users of the knowledge pipeline and research workflow.

> *"TFW is a value operating system for ANY domain."* — S1

---

## Tier 3 — Product-minded Engineers (Secondary)

| Dimension | Detail |
|-----------|--------|
| **Who** | Software engineers who care about architecture decisions, tech debt tracking, codebase evolution history. Engineers who ask "why was this built this way?" and want the answer to be discoverable. |
| **Pain** | "Why was this built this way? Who decided? What was rejected? Context dies with the chat session. The codebase tells me what exists — but not why it exists, what was tried before, or what constraints drove the design. New developers can't understand architecture decisions without asking the original team." |
| **TFW Value** | Architecture decisions preserved in structured traces (HL, RES, RF). Tech debt tracked and triaged — not forgotten in Slack threads. Every change has a traceable decision chain: what prompted it, what alternatives were considered, what was rejected and why. New agents (human or AI) read traces, not raw code. |
| **Adoption Pattern** | Closest to TFW's current language — they understand artifacts, pipelines, and workflows. They need the "why" behind TFW (business value, knowledge compounding) more than the "how" (they'll figure out the mechanics). Risk: they may try to over-engineer TFW itself rather than using it as a methodology. |
| **Qualifying Question** | *"Can a new developer understand your architecture decisions without asking the original team?"* |
| **Anti-signal** | Engineers who view documentation as overhead, prefer "the code is the documentation," or work solo without knowledge transfer needs. |

### Why Secondary?

Engineers are secondary not because they're less important, but because they're already closest to TFW's current positioning. The biggest unlock for TFW is reaching product leaders and analysts *first* — once they adopt the methodology, the engineering team inherits the structured context automatically. Engineers benefit from TFW, but product leaders *need* it.

> *"Focus on value and how to scale it. Not only to programmers, but to higher level."* — S2

---

## Cross-tier Patterns

| Pattern | Expression Across Tiers |
|---------|------------------------|
| **Root pain** | Knowledge evaporates between sessions, people, and tools |
| **Mechanism** | TFW generates knowledge as byproduct of working methodology — no manual documentation required |
| **Team frame** | AI agents are team members, not individual assistants. Everyone (human and AI) reads the same traces. |
| **Domain breadth** | Works for code, analytics, writing, education, business processes — same lifecycle, same artifacts |
| **Adoption barrier** | No self-service path today (S10 context: "All current non-engineer users were personally trained by the author") |

---

## Persona ↔ TFW Feature Mapping

| TFW Feature | Product Leaders | Analysts & Researchers | Engineers |
|-------------|:-:|:-:|:-:|
| Task Board (project dashboard) | ★★★ primary view | ★★ secondary | ★★ secondary |
| Knowledge Pipeline (fact capture → consolidation) | ★★★ institutional memory | ★★★ research knowledge | ★★ architecture decisions |
| Multi-iteration research (RES1→RES2→...) | ★★ understanding depth | ★★★ core workflow | ★★ investigation |
| Trace Discipline (HL→TS→RF chain) | ★★★ decision traceability | ★★★ reproducibility | ★★★ architecture history |
| Role Lock (coordinator ≠ executor) | ★★★ separation of concerns | ★★ quality gate | ★★ review discipline |
| Scope Budgets (guardrails) | ★★ risk management | ★ less relevant | ★★★ prevents scope creep |
| Tech Debt Registry | ★★ backlog management | ★ less relevant | ★★★ core concern |

---

*Audience Persona Matrix — TFW Positioning | 2026-04-10*
*Sources: D5, D9 (RES1), S1-S11 (HL §11), G2 (gather.md), VLM-3 RES3 D19*
