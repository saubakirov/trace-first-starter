# Briefing
> Parent: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> Goal: Fix TFW's pipeline gaps (docs-vs-knowledge conflict, missing knowledge status, manual handoff, terminology fragmentation) and clarify positioning for non-engineer audience.

## Research Plan

### Gather — "What do we NOT know?"
1. Analyze overlap between `tfw-docs` and `tfw-knowledge` workflows — map every output of each, find exact collision points
2. Study how other methodology frameworks (Shape Up, DORA, Scrum Guide, SAFe) present themselves to non-engineer audiences — what language, structure, and framing they use
3. Investigate multi-iteration research patterns — how do existing tools (Cursor, Devin, Aider) handle iterative agent sessions with state handoff?
4. Examine KNOWLEDGE.md structure vs `knowledge/` folder — who reads what, for what purpose

### Extract — "What do we NOT see?"
1. Design the merged vs separated workflow architecture (H1) — model both options with concrete artifact flow
2. Define the boundary between Fact Candidates and Strategic Insights (H5) — what information is lost if merged, what confusion if separated
3. Map multi-iteration research state requirements (H7) — what minimum state must persist between RES1 → RES2 → RES3

### Challenge — "What do we NOT expect?"
1. Stress-test the merge hypothesis (H1): if tfw-knowledge absorbs tfw-docs, what technical documentation currently captured by tfw-docs would be orphaned?
2. Challenge H2 (rename KNOWLEDGE.md → DOCS.md): what breaks? Who references KNOWLEDGE.md today?
3. Challenge H8 (audience = "AI-augmented knowledge workers"): is this too narrow? Too broad? Does it exclude someone who should be included?

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | tfw-docs is unnecessary as standalone workflow — tfw-knowledge can do everything in phases: (1) strategic facts/insights → (2) technical documentation updates. Merging eliminates the conflict entirely | open |
| H2 | KNOWLEDGE.md should become a technical documentation index (rename to DOCS.md or INDEX.md). Knowledge = knowledge/ folder. Documentation = KNOWLEDGE.md. Currently confused | open |
| H3 | Adding `📚 KNW` status to pipeline will make knowledge collection visible and reduce knowledge loss | open |
| H4 | The unique value proposition is the Knowledge Pipeline BUNDLE — no single component is unique, the combination is | confirmed (VLM-3 RES3 D19) |
| H5 | Fact Candidates and Strategic Insights are TWO different concepts, not one. FC = operational observations. Insights = domain/stakeholder knowledge that can't be learned from code. Both should be kept | open |
| H6 | TFW needs a standard "Visualization" or "Diagrams" section in artifacts for business process flows | open |
| H7 | Multi-iteration research (RES1 → RES2 → RES3 in series, each in separate agent) is a valuable pattern that should be formalized | open |
| H8 | TFW's real audience is "AI-augmented knowledge workers" — broader than engineers, narrower than "everyone" | open |

## Scope Intent
- **In scope:** H1-H3 (docs-vs-knowledge architecture), H5 (terminology boundary), H7 (multi-iteration research), H8 (audience positioning), external competitive analysis for positioning
- **Out of scope:** H4 (already confirmed), H6 (lower priority — can be deferred to TS without research), actual README rewrite, actual implementation of handoff manifests, VLM-3 fact triage (Phase C execution, not research)

## Guiding Questions
1. The user context mentions "each hypothesis could be checked separately" and "coordinator decides how many times" — does this mean you envision multi-iteration research as hypothesis-driven (one RES per hypothesis cluster), or volume-driven (always N iterations regardless)?
2. User said «docs should fix technical things that will help the agent later — verify, remove outdated, etc. Knowledge discards what you can learn from code. docs should do the opposite.» — is the core distinction: docs = agent-facing reference, knowledge = human-facing institutional memory?
3. For positioning: when you say "entrepreneurs, PMs, analysts, educators" — are these people who would adopt TFW independently, or people whose AI agents would be configured with TFW by an engineer?

## User Direction

**Q1 (multi-iteration model):** Coordinator-driven. Coordinator groups hypotheses, decides minimum iteration count, writes it somewhere. Not one-RES-per-hypothesis, not fixed N — coordinator guides the grouping and sets minimum.

**Q2 (docs vs knowledge):** Sharp distinction provided:
- **Documentation** = facts about the project and how it's built. Discoverable from the project itself and its tools.
- **Knowledge** = facts about the project from OUTSIDE the project. Things you can't learn from the codebase. Normally in people's heads or other departments (sales, support, commercial). Purpose: everything that can influence decision-making.
- Implication: tfw-docs = internal reference (what IS in the project). tfw-knowledge = external institutional memory (what ISN'T in the project but affects decisions).

**Q3 (audience adoption):** Critical signal:
- All current non-engineer users were personally trained by the author. Self-service adoption doesn't work — too many barriers.
- Pure engineers also struggle — TFW is "a step up" for them (requires business/product thinking).
- **Key insight:** «product people find it easier to learn TFW than engineers find it to learn business product value and think at a higher level»
- Implication: primary audience = product-oriented people. Engineers = secondary. But neither can self-serve today.

---
Stage complete: YES
