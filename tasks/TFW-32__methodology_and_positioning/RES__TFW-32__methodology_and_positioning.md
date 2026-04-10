# RES — TFW-32: Methodology Refinement & Product Positioning

> **Date**: 2026-04-10
> **Author**: AI (Researcher)
> **Status**: 🔬 RES — Complete
> **Parent HL**: [HL-TFW-32](HL-TFW-32__methodology_and_positioning.md)
> **Mode**: Pipeline (deep)

---

## Research Context

TFW-32 addresses 5 structural gaps exposed by 31 tasks of real usage: the docs-vs-knowledge workflow conflict, missing pipeline status for knowledge collection, manual handoff state, terminology fragmentation, and README positioning that speaks to engineers while TFW's actual audience is broader. This research investigated 8 hypotheses (7 open, 1 pre-confirmed), using the SECI knowledge management model, competitive analysis of Shape Up/DORA/Scrum/Confluence/Notion, and the user's direct domain expertise to arrive at architectural decisions.

## Briefing

See [research/briefing.md](research/briefing.md). Key user steering during briefing:
- **Documentation** = facts about the project discoverable from the project itself
- **Knowledge** = facts from OUTSIDE the project, things you can't learn from code
- Product-oriented people adopt TFW more easily than engineers learning business thinking
- Multi-iteration research: coordinator-driven grouping and iteration count

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | **Keep tfw-docs and tfw-knowledge as separate workflows.** Fix overlap by stripping §1/§2 updates from tfw-knowledge Phase 4 | SECI model: docs = Combination (explicit→explicit), knowledge = Externalization (tacit→explicit). Different cognitive processes. Merging conflates them. Current collision: both write to KNOWLEDGE.md §1/§2. Fix: each owns non-overlapping sections |
| D2 | **Rename Fact Candidates → Doc Candidates + Knowledge Candidates.** Two sections in RF/RES/REVIEW templates, matching the two workflows | User input: "if we have two workflows, logical to have two sections." D28 (Naming Creates Behavior): name tells agent WHERE the observation goes. Classification heuristic = Human-Only Test applied at capture time. Misclassification self-corrects at consolidation |
| D3 | **Add 📚 KNW status with REVIEW markers.** Visible only for significant tasks. Trivial tasks: reviewer pre-closes with N/A markers → status goes directly DONE | Pipeline gap proven: 21 RF files with zero facts (TFW-18). KNW makes knowledge step visible. Markers in REVIEW: `tfw-docs: applied/N/A`, `tfw-knowledge: applied/N/A`. Both set = DONE |
| D4 | **Multi-iteration research via iterations.yaml.** Each researcher writes per-iteration RES. Coordinator consolidates by reading all RES files and updating HL | User: "each researcher writes their own RES, coordinator consolidates." Control file at `research/iterations.yaml` tracks iteration count, focus, hypothesis assignments. Researcher CANNOT write final RES — coordinator owns synthesis |
| D5 | **TFW positioning: team knowledge tool, not individual productivity tool.** Pain point: "growing teams lose knowledge." Differentiator: "Confluence stores knowledge, TFW generates it" | User: "most tools are individual, we want team play where AI agents are part of the team." Shape Up/DORA/Scrum pattern: pain-point framing + translation table. TFW = AI-augmented team methodology, not solo coding assistant |
| D6 | **Defer KNOWLEDGE.md rename (H2).** Fix content (remove §0, fix Phase 4 overlap) in this task. Rename to DOCS.md = separate future task | Rename is correct in principle but costly — every TFW file references KNOWLEDGE.md. Compilable contract can handle resolution later. Content fix is higher impact, lower risk |
| D7 | **§0 Philosophy moves to knowledge/philosophy.md.** No workflow updates §0 today — it's orphaned. knowledge/philosophy.md already exists with 14 facts | §0 content = values, principles, north star decisions. This IS knowledge (tacit→explicit), not documentation. Correct home = knowledge/ folder |
| D8 | **KNW orchestration: tfw-docs first, recommends tfw-knowledge.** Both tracked via REVIEW markers | tfw-docs always runs (Combination is faster, lower risk). tfw-knowledge runs conditionally. tfw-docs ending: "Fact candidates detected — run /tfw-knowledge." Self-sequencing, no extra YAML needed |
| D9 | **Audience hierarchy: Product leaders (primary) > Analysts/Researchers (core) > Engineers (secondary).** "Can't afford to lose context" as universal qualifier | User: "product people learn TFW faster than engineers learn business thinking." Excludes hobbyists (acceptable). Includes educators via "can't afford to lose" framing |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Should HL §11 be renamed "Strategic Insights" → "Knowledge Candidates (Planning)"? | Open | User steered toward "Knowledge Candidates" naming. Coordinator to decide exact section header |
| Q2 | Should RF §7 be renamed "Execution Session Insights" → "Knowledge Candidates (Execution)"? | Open | Same as Q1 — unified naming needed |
| Q3 | How should the reviewer pre-close KNW for trivial tasks — inline in REVIEW or separate field? | Open | Current tfw-docs already has marker format. Extend with tfw-knowledge marker. Coordinator decides exact format |
| Q4 | Multi-iteration: should iterations.yaml be created by coordinator in plan.md Step 6, or in a new Step 6b? | Open | Design proposed but insertion point in plan.md TBD |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | tfw-docs is unnecessary as standalone workflow — tfw-knowledge can absorb it | open | ❌ REFUTED | SECI model: docs = Combination (explicit→explicit), knowledge = Externalization (tacit→explicit). Different processes. Fix = strip overlap, not merge |
| H2 | KNOWLEDGE.md should become DOCS.md or INDEX.md | open | ⏸️ DEFERRED | Correct in principle. Cost: every TFW file references KNOWLEDGE.md. Separate task after content fix |
| H3 | Adding 📚 KNW status will make knowledge visible and reduce loss | open | ✅ CONFIRMED | 21 RF files with zero facts. KNW + REVIEW markers make step visible. Trivial tasks skip via N/A |
| H4 | Unique value = Knowledge Pipeline bundle | confirmed | ✅ CONFIRMED | Pre-confirmed. Extended: "generates, not stores" differentiator vs Confluence/Notion |
| H5 | FC and SI are TWO different concepts, not one | open | ✅ CONFIRMED | Renamed: Doc Candidates (agent-observed, internal) + Knowledge Candidates (human-sourced, external). D28 applied: name → workflow routing |
| H6 | TFW needs Visualization/Diagrams section | open | ⏸️ DEFERRED | Lower priority. Not investigated — can be added to TS without research |
| H7 | Multi-iteration research should be formalized | open | ✅ CONFIRMED | iterations.yaml + per-iteration RES + coordinator consolidation. Each researcher writes own RES, coordinator reads all |
| H8 | TFW audience = "AI-augmented knowledge workers" | open | ✅ REFINED | "Teams and individuals who can't afford to lose context." Primary = product leaders. Core = analysts/researchers. Secondary = product-minded engineers. Team tool, not individual |

## HL Update Recommendations

| # | What to update | Source |
|---|---------------|--------|
| 1 | §3 Target State: Replace "merge" language with "separate + orchestrate" for docs-vs-knowledge | D1 |
| 2 | §3 Unified terminology: Replace "Fact Candidates everywhere" with "Doc Candidates + Knowledge Candidates" split | D2 |
| 3 | §4 Phase A: Add "strip §1/§2 from tfw-knowledge Phase 4, add REVIEW markers" | D1, D8 |
| 4 | §4 Phase A: Add iterations.yaml design to handoff conventions or as separate sub-item | D4 |
| 5 | §4 Phase B: Replace persona matrix with the 3-tier audience hierarchy | D9 |
| 6 | §4 Phase B: Add competitive positioning spec vs Confluence/Notion ("generates vs stores") | D5 |
| 7 | §4 Phase B: Add translation table (TFW technical → business-friendly) to README spec | D5 |
| 8 | §10 Hypotheses: Update all statuses per table above | All |
| 9 | §2 Current State: Note that §0 Philosophy is orphaned — no workflow updates it | D7 |
| 10 | §1 Vision: Strengthen "team tool, not individual tool" framing | D5, D9 |

## Fact Candidates

> Reviewing conversation history for human-sourced knowledge signals.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | philosophy | Documentation = facts about the project discoverable from the project. Knowledge = facts from OUTSIDE the project that only humans know. This is the foundational distinction for tfw-docs vs tfw-knowledge scope | User (2026-04-10), briefing Q2 | ★★★ |
| FC2 | stakeholder | Product-oriented people learn TFW faster than engineers learn business/product thinking. Primary audience = product leaders, not engineers | User (2026-04-10), briefing Q3 | ★★★ |
| FC3 | philosophy | TFW = team tool, not individual productivity tool. "Most tools are individual — they boost one person. We want team play where AI assistants are part of the team and part of knowledge and communications" | User (2026-04-10), gather Q1 | ★★★ |
| FC4 | philosophy | TFW's problem space = communication breakdown at scale: "any business growing suffers from communication gaps, lack of information exchange, decentralized decision-making, information not flowing up and down" | User (2026-04-10), gather Q2 | ★★★ |
| FC5 | process | Multi-iteration research: each researcher writes their own per-iteration RES. Coordinator reads all iterations and consolidates. Researcher does NOT write final consolidated RES | User (2026-04-10), extract Q3 | ★★★ |
| FC6 | domain | SECI model maps to TFW: docs = Combination (explicit→explicit), knowledge = Externalization (tacit→explicit). Different cognitive processes validated by Nonaka-Takeuchi theory | Research (2026-04-10), gather G5 | ★★☆ |
| FC7 | domain | Competitive positioning: Confluence protects memory through enforcement, Notion through usability. Neither generates knowledge from work process. TFW generates it as byproduct of methodology | Research (2026-04-10), challenge C4 | ★★☆ |
| FC8 | philosophy | TFW's vision = "one repo for all roles (product, developer, analyst, QA), one methodology, shared knowledge." All team members including AI agents contribute | User (2026-04-10), challenge response | ★★★ |
| FC9 | process | Orchestration of docs+knowledge: tfw-docs runs first (always), recommends tfw-knowledge (conditional). No need for separate orchestration YAML — REVIEW markers are sufficient | Research (2026-04-10), extract E1 | ★★☆ |

## Conclusion

This research investigated 8 hypotheses across 3 stages using external theory (SECI model, competitive methodology analysis) and direct user domain expertise. The central finding is that the docs-vs-knowledge conflict is NOT a merge problem but an overlap problem — both workflows correctly exist as separate SECI phases, but Phase 4 of tfw-knowledge encroaches on tfw-docs territory. The fix is surgical: strip §1/§2 from Phase 4, add REVIEW markers for orchestration, and rename the capture sections to match workflows (Doc Candidates + Knowledge Candidates).

The positioning discovery was unexpected: TFW's real competitive frame is "team knowledge methodology" (vs Confluence/Notion), not "individual AI coding assistant" (vs Cursor/Claude features). The pain point — growing teams losing knowledge when decisions don't propagate — resonates with the primary audience (product leaders, PMs) more than with engineers. The "generates, not stores" differentiator against existing knowledge tools is sharp and defensible.

Self-critique: H6 (Visualization section) was deferred without investigation. H2 (KNOWLEDGE.md rename) deferred pragmatically but leaves a naming inconsistency. Multi-iteration design (D4) is the least validated decision — it has no external precedent and relies on coordinator discipline.

---

*RES — TFW-32: Methodology Refinement & Product Positioning | 2026-04-10*
