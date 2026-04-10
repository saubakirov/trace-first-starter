# HL — TFW-32 / Phase D: Positioning & Messaging

> **Date**: 2026-04-10
> **Author**: AI (Coordinator)
> **Status**: 📝 HL_DRAFT
> **Parent HL**: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)

---

## 1. Vision

TFW's public face (README.md, .tfw/README.md) speaks to engineers. Its actual audience is broader — product leaders, analysts, and product-minded engineers who can't afford to lose context between sessions and team members. This phase produces a **positioning spec** — a structured document defining audience, messaging, and section-by-section improvement direction. The spec is the deliverable. The actual README rewrite is a separate future task.

## 2. Current State (As-Is)

From master HL §2.6 and RES1 D5/D9:

- README "Who This Is For" lists 6 domains without hierarchy. Business and operations are listed alongside education — no primary audience signal
- Pain point never stated explicitly. Closest: "If your work involves AI-assisted iteration and you need continuity across sessions"
- Differentiator "The thinking is the product" never contrasts with Confluence/Notion: "TFW generates knowledge, Confluence/Notion store it"
- Language is tech-heavy: ETL, SQL, codebase
- Team framing missing: TFW = team methodology where AI agents are team members, currently read as individual tool
- .tfw/README.md "The Problem: Knowledge Evaporates" is strong but framed for individual developer, not team
- VLM-3 RES3 identified 8 unique TFW features absent from all coding agents. Knowledge Pipeline survived sycophancy demolition. These are unused in README positioning

## 3. Target State (To-Be)

### 3.1 Result Visualization

```
DELIVERABLES (this phase):

  PhaseD/
    positioning_spec.md          ← Section-by-section README improvement spec
    audience_personas.md         ← 3-tier persona matrix with pain points
    translation_table.md         ← TFW technical → business-friendly terms
    philosophy_improvement.md    ← .tfw/README.md improvement spec
```

### 3.2 Value Flow

```
INPUTS                         PROCESSING                        OUTPUT
──────                         ──────────                        ──────
RES1 D5, D9                →   Audience hierarchy               → Persona matrix with pain points
HL §11 S1-S17              →   Insight distillation             → Value proposition (1 paragraph)
VLM-3 RES3 D19-D20        →   Competitive differentiation      → "Generates vs stores" frame
Shape Up / DORA patterns   →   Translation methodology          → TFW → business terms table
Current README sections    →   Gap analysis per section         → Before/after improvement spec
Current .tfw/README.md     →   Philosophy gap analysis          → Philosophy improvement spec
```

## 4. Context (from master HL §4 Phase D)

**Key decisions driving this phase:**
- D5: TFW = team knowledge methodology, not individual AI coding assistant. "Generates, not stores" vs Confluence/Notion
- D9: 3-tier audience: product leaders (primary) > analysts/researchers (core) > product-minded engineers (secondary)

**Key strategic insights:**
- S1: TFW = value operating system for ANY domain
- S2: "Not only programmers, but higher level"
- S9: Team tool, AI agents are team members
- S10: "Product people learn TFW faster than engineers learn business thinking"
- S11: "Any growing business suffers from communication gaps"

**External references:**
- Shape Up: pain-point framing, "betting" not "sprint planning"
- DORA: translation table pattern (technical metric → business value)
- Scrum Guide 2020: Product Owner as "Value Maximizer"
- VLM-3 RES3: 8 unique features, Knowledge Pipeline confirmed

## 5. Principles

1. **Spec before rewrite** — this phase produces direction, not final copy
2. **Audience-first** — README speaks to product leaders, not to the agent
3. **Pain-point framing** — problems first, solution elements second (Shape Up pattern)
4. **Translation, not simplification** — technical terms need business equivalents, not dumbing down

## 6. Definition of Done

- ✅ 1. Audience persona matrix exists with 3 tiers, pain points, and adoption patterns
- ✅ 2. Value proposition (1 paragraph) articulates "generates vs stores" differentiator
- ✅ 3. Translation table maps TFW terms to business-friendly equivalents
- ✅ 4. README improvement spec has before/after direction per section
- ✅ 5. .tfw/README.md improvement spec exists

---

*HL — TFW-32 / Phase D: Positioning & Messaging | 2026-04-10*
