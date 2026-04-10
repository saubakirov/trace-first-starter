# HL — TFW-32: Methodology Refinement & Product Positioning

> **Date**: 2026-04-10
> **Author**: AI (Coordinator)
> **Status**: 📝 HL_DRAFT — Post-RESEARCH update, awaiting approval
> **Research**: 4 iterations complete (RES1-RES4). 26 decisions. 18 fact candidates. 10 strategic insights.

---

## 1. Vision

TFW's methodology pipeline has structural gaps exposed by 31 tasks and 8 research iterations (4 VLM-3 + 4 TFW-32). The docs-vs-knowledge workflow collides because tfw-knowledge Phase 4 encroaches on tfw-docs territory. The pipeline has no visible knowledge status. Terminology for knowledge capture splits into three inconsistent names. Multi-iteration research — proven valuable in practice — has no formal mechanism. And TFW's public face speaks to engineers, while its real audience is teams that can't afford to lose context: product leaders, analysts, and product-minded engineers.

This task fixes the pipeline, formalizes multi-iteration research, establishes naming conventions with empirical backing, and documents product positioning.

**Impact:** After this task, (1) docs and knowledge workflows have non-overlapping scope, (2) the pipeline has a visible `📚 KNW` step, (3) naming for §5/§6/§7 + visual sections is empirically validated, (4) multi-iteration research has structural enforcement, (5) TFW positioning shifts from "individual AI tool" to "team knowledge methodology."

> "Each section name is a micro-prompt. If named right, AI needs fewer instructions. The thinking is the product — now the pipeline reflects that."

## 2. Current State (As-Is)

### 2.1 docs vs knowledge conflict

| Aspect | Current state | Problem |
|--------|-------------|---------|
| `/tfw-knowledge` | Consolidates Fact Candidates → verified facts in `knowledge/` topic files | Phase 4 also writes to KNOWLEDGE.md §1/§2 — **overlaps with tfw-docs** |
| `/tfw-docs` | Updates KNOWLEDGE.md (§0-§4) and TECH_DEBT.md after REVIEW | After `/tfw-knowledge` runs, docs agent says "already captured" and refuses to work |
| Root cause | tfw-knowledge Phase 4 encroaches on tfw-docs territory (§1 Architecture Map, §2 Key Artifacts) | Both workflows write to the same sections — collision |
| §0 Philosophy | Set by user once, never updated by any workflow | Orphaned — should be in `knowledge/philosophy.md` (already exists, 14 facts) |
| SECI mapping | tfw-docs = Combination (explicit→explicit). tfw-knowledge = Externalization (tacit→explicit) | Different cognitive processes — validated by Nonaka-Takeuchi theory (RES1 D1) |

**User distinction (RES1 briefing):**
- **Documentation** = facts about the project discoverable FROM the project (code, architecture, configs)
- **Knowledge** = facts from OUTSIDE the project that only humans know (domain, stakeholders, strategy, decisions rationale)

### 2.2 Pipeline lacks knowledge status

Current pipeline:
```
⬜ TODO → 📝 HL_DRAFT → 🔬 RES → 🟡 TS_DRAFT → 🟠 ONB → 🟢 RF → 🔍 REV → ✅ DONE
```

Knowledge collection happens via Knowledge Gate in `plan.md` Phase 0 — gates the NEXT task, not current. Result: 21 RF files analyzed during TFW-18 showed zero project facts recorded.

### 2.3 Terminology — three names for two concepts

| Name | Where | What it captures | Empirical LLM behavior |
|------|-------|-----------------|----------------------|
| Fact Candidates | RF §6, REVIEW §5, RES | Agent-observed project patterns | Pure reporting: "record factual without interpretation" (RES3 D16) |
| Strategic Session Insights | HL §11 | User/domain knowledge during planning | Deep analytical synthesis: model ADDS implications (RES3 D15) |
| Execution Session Insights | RF §7 | User/domain knowledge during execution | Never tested — name existed but section was inconsistent |

**Research finding (RES3):** These are NOT three names for one concept. They are TWO distinct cognitive modes:
1. **Fact Candidates (§6)** = operational observations agent can detect from code/data. Agent mode: report without interpretation
2. **Strategic Insights (§7/§11)** = human-sourced domain knowledge. Agent mode: synthesize, identify implications

Both names are **empirically optimal** — renaming was tested (7 variants for §7, 5 for §6) and originals outperformed all alternatives (RES3 D15, D16).

### 2.4 No visual section in result artifacts

HL has §3.1 "Result Visualization" but neither RF nor RES has a standard visualization section. Business process flows, architecture diagrams, and user journeys have no canonical home.

### 2.5 Multi-iteration research not formalized

VLM-3 ran 4 iterations, TFW-32 ran 4 iterations. Both discovered significant insights in later iterations that early iterations missed or got wrong (e.g., D2 proposed wrong naming, D15 corrected it in iteration 3). Current TFW research: one `/tfw-research` → one RES → done. No iteration tracking, no coordinator control, no structural enforcement of depth.

### 2.6 README positioning

| Aspect | Current | Gap |
|--------|---------|-----|
| Audience framing | "Who This Is For" with 6 domain bullets | Doesn't distinguish primary vs secondary. Software engineering listed alongside business |
| Pain point | Not explicitly stated | "Growing teams lose knowledge" — the universal qualifier (RES1 D9) |
| Differentiator | "The thinking is the product" | Never states: "TFW generates knowledge, Confluence/Notion store it" (RES1 D5) |
| Language | Tech-heavy: ETL, SQL, codebase | Needs translation layer: technical terms → business language (Shape Up/DORA pattern) |
| Team framing | Individual tool assumption | TFW = team methodology where AI agents are team members (RES1 FC3) |

## 3. Target State (To-Be)

### 3.1 Result Visualization

```
BEFORE:
  docs-vs-knowledge:
    tfw-knowledge Phase 4 ──writes──→ KNOWLEDGE.md §1/§2 ←──writes── tfw-docs
                                      (COLLISION)

AFTER:
  tfw-docs ──writes──→ KNOWLEDGE.md §1 Architecture + §2 Decisions + §3 Legacy
                       (exclusive territory: Combination, explicit→explicit)

  tfw-knowledge ──writes──→ knowledge/*.md (verified facts) + KNOWLEDGE.md §4 (index only)
                            (exclusive territory: Externalization, tacit→explicit)

  KNOWLEDGE.md §0 Philosophy → DELETED (content already in knowledge/philosophy.md)
```

```
PIPELINE (before → after):

  BEFORE: ... → 🔍 REV → ✅ DONE
                          ↑ Knowledge Gate in NEXT task (reactive, often skipped)

  AFTER:  ... → 🔍 REV → 📚 KNW → ✅ DONE
                            ↑
                            tfw-docs (always) → recommends tfw-knowledge (conditional)
                            REVIEW markers: tfw-docs: applied/N/A | tfw-knowledge: applied/N/A
```

```
NAMING (before → after):

  BEFORE:                              AFTER:
    §5: Observations                     §5: Observations (unchanged)
    §6: Fact Candidates                  §6: Fact Candidates (unchanged, empirically optimal)
    §7: Execution Session Insights       §7: Strategic Insights (Execution) — unified with HL §11
    §11: Strategic Session Insights      §11: Strategic Insights (Planning) — unified with RF §7
    Visual: only HL §3.1                 Visual: HL = "Value Flow", RF = "Diagrams", RES = "Findings Map"
```

```
MULTI-ITERATION RESEARCH (before → after):

  BEFORE: /tfw-research → 1 RES → done
  AFTER:
    Coordinator writes iterations.yaml (focus, hypotheses, min_iterations=2)
    └→ Researcher iter 1: research/  + RES on task root
    └→ Researcher iter 2: research2/ + RES__iter2 on task root
    └→ ...
    └→ Coordinator reads ALL RES files, updates HL, decides: more or proceed to TS
```

### 3.2 Value Flow

```
USER PAIN                 TFW PIPELINE                           VALUE DELIVERED
──────────                ──────────                             ───────────────
"Growing team loses    →  HL (planning traces)              →   Every decision traceable
 context between          RES (multi-iteration research)         No re-explanation needed
 sessions and             TS/ONB/RF (execution traces)           New agent resumes from
 team members"            tfw-docs (documentation capture)       last checkpoint
                          tfw-knowledge (knowledge capture)      Knowledge compounds
                          📚 KNW (visible pipeline step)        across 10, 50, 100 tasks
```

```
POSITIONING FRAME:

  Confluence/Notion ──── "STORES knowledge" ──── someone must WRITE docs manually
                                                 ↓
                                                 decay, stale, nobody reads

  TFW ──────────────── "GENERATES knowledge" ── byproduct of working methodology
                                                 ↓
                                                 compounds, self-updates, agents READ it
```

### docs vs knowledge separation (research-validated)
- `/tfw-docs`: KNOWLEDGE.md §1-§3 + TECH_DEBT.md. Scope = Combination (explicit→explicit). Facts discoverable from code.
- `/tfw-knowledge`: `knowledge/` topic files + KNOWLEDGE.md §4 (index). Scope = Externalization (tacit→explicit). Facts from outside the project.
- §0 Philosophy → removed from KNOWLEDGE.md (content lives in `knowledge/philosophy.md`)
- tfw-knowledge Phase 4: strip §1/§2 writes (was the collision source)
- KNOWLEDGE.md rename (→ DOCS.md/INDEX.md) — **deferred** (correct but costly; every TFW file references it)

### Pipeline with knowledge status (research-validated)
- New status `📚 KNW` between REV and DONE
- REVIEW template adds markers: `tfw-docs: applied/N/A` | `tfw-knowledge: applied/N/A`
- Both markers set → status transitions to DONE
- Trivial tasks: reviewer pre-closes with N/A markers
- KNW orchestration: tfw-docs runs first (always), recommends tfw-knowledge (conditional)

### Naming conventions (empirically validated, RES3-RES4)
- **§6 Fact Candidates** — keep. Triggers correct LLM mode: "report factual without interpretation"
- **§7/§11 Strategic Insights** — keep. Triggers deep analytical synthesis. Add qualifier: (Planning) in HL, (Execution) in RF, (Research) in RES
- **Visual section** — per-template naming (cognitive modes differ between templates):
  - HL: **Value Flow** (strategic value delivery)
  - RF: **Diagrams** (technical process detail)
  - RES: **Findings Map** (research findings visualization)
- **§3.1 Result Visualization** — keep, enhance with Working Backwards framing (Amazon PR/FAQ). This is SEPARATE from Value Flow: §3.1 = WHAT done looks like, Value Flow = HOW value gets created
- **Decision criterion**: "Does the cognitive mode CHANGE between templates?" → per-template. "Same mode?" → unified name

### Multi-iteration research (formalized from 8 real iterations)
- `iterations.yaml` in task root: min_iterations, focus per iter, hypothesis assignments
- `researchN/` folders accumulate (trace preservation — never delete stage files)
- Each researcher: writes per-iteration RES on task root + stage files in researchN/
- Researcher exit protocol: mandatory "Iteration Status" block (tested/deferred/gaps/open threads)
- Coordinator gate in plan.md: cannot proceed to TS while iterations < min_iterations
- `min_iterations = 2` as configurable hard floor in PROJECT_CONFIG.yaml
- Iteration triggers: error correction, gap filling, depth on finding, user-injected new direction

### README positioning (research-validated)
- **Audience hierarchy**: Product leaders (primary) > Analysts/Researchers (core) > Product-minded engineers (secondary)
- **Universal qualifier**: "Teams and individuals who can't afford to lose context"
- **Pain point**: "Growing teams lose knowledge when decisions don't propagate"
- **Differentiator vs Confluence/Notion**: "TFW generates knowledge as byproduct of methodology. Others require someone to manually write and maintain docs"
- **Team framing**: "AI agents are team members, not individual assistants"
- **Translation table** needed: TFW technical terms → business-friendly equivalents (Shape Up/DORA pattern)

## 4. Phases

### Phase A: Methodology pipeline fixes 🟡 TS_DRAFT

**Context for coordinator:**
Read these files before writing TS:
1. This HL — §2.1 (current collision), §3 "docs vs knowledge separation", §3 "Pipeline with knowledge status"
2. [RES1](RES__TFW-32__methodology_and_positioning.md) — D1 (keep separate, SECI model), D3 (KNW status + markers), D7 (§0 → philosophy.md), D8 (orchestration: docs first)
3. [RES1 gather](research/gather.md) — G1 (exact collision: tfw-knowledge Phase 4 writes §1/§2), G4 (who reads what in KNOWLEDGE.md), G5 (SECI mapping)
4. `.tfw/workflows/docs.md` — current tfw-docs workflow (what to change)
5. `.tfw/workflows/knowledge.md` — current tfw-knowledge workflow (Phase 4 to strip)
6. `.tfw/workflows/review.md` — needs REVIEW markers addition
7. `.tfw/conventions.md` §5 (status flow — where to add KNW)
8. `.tfw/PROJECT_CONFIG.yaml` — `tfw.statuses` to update
9. `KNOWLEDGE.md` — current §0 content to verify against `knowledge/philosophy.md`

**Key decisions driving this phase:** D1, D3, D6, D7, D8

**Deliverables:**
1. Fix docs-vs-knowledge collision: strip §1/§2 writes from tfw-knowledge Phase 4
2. Move KNOWLEDGE.md §0 → knowledge/philosophy.md (content already exists — verify no loss)
3. Update tfw-docs workflow: clear scope = KNOWLEDGE.md §1-§3 + TECH_DEBT.md
4. Update tfw-knowledge workflow: clear scope = knowledge/*.md + KNOWLEDGE.md §4
5. Add `📚 KNW` status: conventions.md, PROJECT_CONFIG.yaml, glossary.md, pipeline diagram
6. Add REVIEW markers: `tfw-docs: applied/N/A` | `tfw-knowledge: applied/N/A`
7. Update tfw-review workflow to reference KNW status and markers

---

### Phase B: Naming & templates 🔴

**Context for coordinator:**
Read these files before writing TS:
1. This HL — §2.3 (current naming), §3 "Naming conventions"
2. [RES3](RES__iter3__naming_visualization_multiiter.md) — D15 (keep Strategic Insights, empirical), D16 (keep Fact Candidates, empirical), D17→D22 (visual per-template), D20 (naming philosophy coherent)
3. [RES4](RES__iter4__per_template_naming.md) — D21 (two visual concepts in HL), D22 (per-template: HL=Value Flow, RF=Diagrams, RES=Findings Map), D24 (§6 unified), D25 (§7 unified + qualifier), D26 (§3.1 Working Backwards)
4. [RES4 experiment_analysis](research4/experiment_analysis.md) — empirical LLM test results backing naming decisions
5. `.tfw/templates/HL.md` — current §11 "Strategic Session Insights" (rename to "Strategic Insights (Planning)")
6. `.tfw/templates/RF.md` — current §6, §7 (sharpen + add visual section)
7. `.tfw/templates/RES.md` — needs Strategic Insights + Findings Map sections added
8. `.tfw/templates/REVIEW.md` — needs Fact Candidates instructions sharpened
9. `.tfw/glossary.md` — needs new terms
10. `.tfw/conventions.md` — needs Visual Sections cross-reference table

**Key decisions driving this phase:** D15, D16, D20, D21, D22, D24, D25, D26

**Critical nuance:** RES1 D2 and RES2 D10 proposed RENAMING §6/§7 — both were **superseded** by RES3 D15/D16 which proved originals are empirically optimal. Do NOT rename. Sharpen instructions only.

**Decision criterion for per-template vs unified naming:** "Does the cognitive mode CHANGE between templates?" Visual section = YES → per-template. §6/§7 = NO → unified.

**Deliverables:**
1. Sharpen §6 "Fact Candidates" instructions in all templates (RF, RES, REVIEW) — scope = agent-observed project patterns
2. Sharpen §7/§11 "Strategic Insights" instructions + add qualifier (Planning/Execution/Research)
3. Extend "Strategic Insights" section to RES and RF templates (currently only HL §11 has it)
4. Add visual section to templates: HL = "Value Flow", RF = "Diagrams", RES = "Findings Map"
5. Enhance HL §3.1 instructions with Working Backwards framing
6. Add conventions.md cross-cutting "Visual Sections" reference documenting per-template names
7. Update glossary with new terms: Value Flow, Findings Map, strategic vs operational capture distinction

---

### Phase C: Multi-iteration research formalization 🟡

**Context for coordinator:**
Read these files before writing TS:
1. This HL — §2.5 (current gap), §3 "Multi-iteration research"
2. [RES1](RES__TFW-32__methodology_and_positioning.md) — D4 (iterations.yaml + exit protocol)
3. [RES2](research2/RES__iter2__naming_visualization_multiiter.md) — D14 (enforcement: YAML + coordinator hard gate + min_iterations)
4. [RES3](RES__iter3__naming_visualization_multiiter.md) — D18 (researchN/ folders, accumulate don't overwrite), D19 (full design: iterations.yaml + exit protocol + briefing template + coordinator gate + min_iterations=2)
5. `.tfw/workflows/plan.md` — current Step 6 (RESEARCH decision — needs iteration gate)
6. `.tfw/workflows/research.md` — current research workflow (needs multi-iteration flow)
7. `.tfw/PROJECT_CONFIG.yaml` — where to add `tfw.research.min_iterations`
8. `.tfw/glossary.md` — needs Iteration, iterations.yaml definitions
9. This task's own `research/`, `research2/`, `research3/`, `research4/` — living example of pattern

**Key decisions driving this phase:** D4, D14, D18, D19

**Living example:** This very task (TFW-32) ran 4 iterations. The pattern: each researcher wrote stage files in researchN/ + per-iteration RES on task root. Coordinator read all RES files and consolidated into HL update. The superseded decisions chain (D2→D10→D15) demonstrates WHY multi-iteration matters.

**Deliverables:**
1. Design `iterations.yaml` format (fields: iteration, focus, hypotheses, status)
2. Add `tfw.research.min_iterations` config key to PROJECT_CONFIG.yaml (default: 2)
3. Write researcher exit protocol (Iteration Status block template)
4. Write briefing template for iteration 2+ (references predecessor RES)
5. Add coordinator iteration gate to plan.md (Step 6 extension — cannot proceed to TS while iterations < min)
6. Update tfw-research workflow with multi-iteration flow
7. Update glossary: Iteration, iterations.yaml, min_iterations

---

### Phase D: Positioning & messaging 🟡

**Context for coordinator:**
Read these files before writing TS:
1. This HL — §2.6 (current README gaps), §3 "README positioning", §3.2 Value Flow diagrams
2. [RES1](RES__TFW-32__methodology_and_positioning.md) — D5 (team knowledge tool positioning), D9 (audience hierarchy)
3. [RES1 gather](research/gather.md) — G2 (Shape Up / DORA / Scrum Guide positioning patterns — translation tables, pain-point framing)
4. [RES1 briefing](research/briefing.md) — User Direction Q3: "product people learn TFW faster than engineers learn business thinking"
5. `README.md` — current root README (what to improve)
6. `.tfw/README.md` — current philosophy paper (what to improve)
7. VLM-3 research: `d:\projects\research\vllm-local-coding\tasks\VLM-3__multi_agent_orchestrator\RES3__VLM-3__multi_agent_orchestrator.md` — competitive analysis, 8 unique features
8. This HL §11 — S1, S2, S9, S10, S11 (user positioning insights)

**Key decisions driving this phase:** D5, D9

**Important:** This phase produces a SPEC, not a finished README. The spec says what to change per section. Actual rewrite = separate future task.

**Deliverables:**
1. Write audience persona matrix (3-tier hierarchy: product leaders > analysts > product-minded engineers, with pain points per tier)
2. Articulate unique value proposition (1 paragraph, "generates vs stores" differentiator)
3. Write translation table: TFW technical terms → business-friendly equivalents (following DORA pattern)
4. Write README improvement spec (section-by-section, with before/after direction)
5. Write .tfw/README.md philosophy paper improvement spec

---

### Phase E: Knowledge capture & backlog 🟡

**Context for coordinator:**
Read these files before writing TS:
1. This HL — all §11 Strategic Insights (S1-S17)
2. All RES files at task root:
   - [RES1](RES__TFW-32__methodology_and_positioning.md) — FC1-FC9, SS (not yet named)
   - [RES2](research2/RES__iter2__naming_visualization_multiiter.md) — FC10-FC12, SS1-SS4
   - [RES3](RES__iter3__naming_visualization_multiiter.md) — FC13-FC15, SS5-SS7
   - [RES4](RES__iter4__per_template_naming.md) — FC16-FC18, SS8-SS10
3. VLM-3 research (external project): `d:\projects\research\vllm-local-coding\tasks\VLM-3__multi_agent_orchestrator\` — RES1, RES2, RES3, RES4 (fact candidates to triage into steps-framework knowledge/)
4. `KNOWLEDGE.md` — current state, §1/§2 to update with new decisions
5. `knowledge/` — existing topic files to extend
6. `.tfw/knowledge_state.yaml` — current consolidation state
7. `.tfw/workflows/knowledge.md` — consolidation process to follow
8. `README.md` Task Board — where to add future tasks

**Key decisions driving this phase:** All D1-D26 (decisions become knowledge). FC1-FC18 + SS1-SS10 are raw material.

**Deliverables:**
1. Triage TFW-32 RES1-RES4 fact candidates (FC1-FC18) into steps-framework knowledge/
2. Triage TFW-32 strategic insights (SS1-SS10) into knowledge/
3. Triage VLM-3 fact candidates into steps-framework knowledge/
4. Record future tasks in Task Board:
   - Thinking traces as first-class TFW artifacts
   - Knowledge pipeline automation (plugin-based capture)
   - Handoff manifest implementation (task_state.yaml)
   - KNOWLEDGE.md rename to DOCS.md (deferred from this task)
   - README rewrite execution (based on Phase D spec)
5. Update KNOWLEDGE.md with new decisions from this task (D1-D26 → D-table)

## 5. Definition of Done (DoD)

- ✅ 1. tfw-docs and tfw-knowledge have non-overlapping scope (no dual writes to any KNOWLEDGE.md section)
- ✅ 2. `📚 KNW` status exists in conventions.md, PROJECT_CONFIG.yaml, glossary.md with REVIEW markers
- ✅ 3. §6 "Fact Candidates" and §7/§11 "Strategic Insights" have sharpened instructions in all templates
- ✅ 4. Visual section exists in HL (Value Flow), RF (Diagrams), RES (Findings Map) templates
- ✅ 5. Multi-iteration research formalized: iterations.yaml, exit protocol, plan.md gate, min_iterations config
- ✅ 6. Audience persona matrix with 3-tier hierarchy and pain points exists
- ✅ 7. README improvement spec exists (section-by-section, before/after)
- ✅ 8. All FC1-FC18 and SS1-SS10 from TFW-32 research triaged into knowledge/
- ✅ 9. Future tasks added to Task Board

## 6. Definition of Failure (DoF)

- ❌ 1. tfw-docs and tfw-knowledge still collide after Phase A
- ❌ 2. KNW status added but no workflow references it — orphan status
- ❌ 3. Naming changes without updated glossary — agents use old terms
- ❌ 4. Positioning produces generic "for everyone" instead of specific personas
- ❌ 5. Multi-iteration formalization adds overhead without structural enforcement (min_iterations ignored)

**On failure:** Rollback Phase A/B files. For Phase D, conduct user interviews to sharpen personas.

## 7. Principles

1. **SECI separation** — docs = Combination (explicit→explicit, discoverable from code). Knowledge = Externalization (tacit→explicit, from humans). Different cognitive processes, different workflows.
2. **Pipeline visibility** — if a step matters, it must have a status on the Task Board. Invisible steps get skipped.
3. **Naming = Prompting (D28 extended)** — section headers are micro-prompts. Empirically validated: correct name triggers correct LLM cognitive mode. Per-template naming WHERE modes differ; unified naming WHERE they don't.
4. **Trace preservation** — multi-iteration research accumulates, never overwrites. `researchN/` folders are traces. Deleting them = deleting reasoning.
5. **Audience-first messaging** — README speaks to product leaders and analysts, not to the agent.
6. **Spec before rewrite** — Phase D produces a spec, not a finished README. Rewrite = separate task.

## 7.1 Quality Contract (multi-phase consistency)

- All template changes MUST update glossary.md and conventions.md in the same phase
- No section can be renamed without updating all templates that contain it
- Per-template visual section names MUST be documented in conventions.md cross-reference table
- Workflow changes MUST reference the exact section numbers they read/write

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| VLM-3 research (4 iterations, RES1-RES4) | ✅ Complete (external project) |
| TFW-32 research (4 iterations, RES1-RES4) | ✅ Complete |
| TFW-31 Quick Start rewrite | ✅ DONE |
| TFW-30 Antigravity adapter audit | 📝 HL_DRAFT (independent) |

## 9. Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Adding KNW status breaks existing task flow | Low | Medium | KNW is skippable (N/A). Existing DONE tasks not affected |
| §0 removal causes information loss | Medium | High | verify: every principle in §0 has a corresponding fact in knowledge/philosophy.md before removing |
| Per-template visual names confuse agents | Low | Medium | Conventions.md cross-reference table + per-template instructions |
| Multi-iteration adds overhead for simple tasks | Low | Low | min_iterations = 2 is configurable. Simple tasks: coordinator sets min=1 |
| Positioning overfit to single user | Medium | Medium | Cross-reference with VLM-3 + DORA/Shape Up patterns |
| 5 phases exceed scope budget | Medium | Medium | Phases D and E are analytical (no code changes). Phases A-C are core. Can split if needed |

## 10. RESEARCH Case

### Research Complete — 4 iterations

| # | Hypothesis | Status | Evidence |
|---|----------|--------|----------|
| H1 | tfw-docs merge into tfw-knowledge | ❌ REFUTED | SECI: different cognitive processes. Fix overlap, not merge (D1) |
| H2 | KNOWLEDGE.md rename → DOCS.md | ⏸️ DEFERRED | Correct but costly — every file references it. Content fix first (D6) |
| H3 | 📚 KNW status reduces knowledge loss | ✅ CONFIRMED | 21 RF files with zero facts. KNW + REVIEW markers (D3) |
| H4 | Knowledge Pipeline bundle = unique | ✅ CONFIRMED | Pre-confirmed. Extended: "generates, not stores" (D5) |
| H5 | FC and SI are two concepts | ✅ CONFIRMED | Two cognitive modes empirically validated. Keep both names (D15, D16) |
| H6 | Visualization section needed | ✅ CONFIRMED | Per-template: HL=Value Flow, RF=Diagrams, RES=Findings Map (D22) |
| H7 | Multi-iteration research formalization | ✅ CONFIRMED | iterations.yaml + exit protocol + coordinator gate. min_iterations=2 (D19) |
| H8 | Audience = "AI-augmented knowledge workers" | ✅ REFINED | "Teams that can't afford to lose context." 3-tier: product > analysts > engineers (D9) |
| H5c | "Strategic Signals" better than "Strategic Insights" | ❌ REFUTED | Empirical: original outperformed all alternatives (D15) |
| H6c | Better name than "Diagrams" for visual | ⚠️ PARTIAL | Per-template naming: Diagrams for RF, Value Flow for HL (D22) |
| H7c | Multi-iteration self-leading with min_iterations=2 | ✅ CONFIRMED | Full design validated (D19) |
| H_pertemplate | Different templates = different section names for visual | ✅ PARTIAL | Yes for visual (modes differ). No for §6/§7 (modes same) (D24, D25) |
| H_visionvs | §3.1 ≠ process diagrams | ✅ CONFIRMED | Zero content overlap empirically. Two separate concepts (D21) |
| H_valuemaps | "Value Maps" for visual section | ❌ REFUTED | 3 conflicting industry meanings. "Value Flow" cleaner (D23) |

### Superseded decisions chain
```
RES1 D2 (Doc/Knowledge Candidates) → superseded by RES2 D10 (Strategic Signals) → superseded by RES3 D15 (keep Strategic Insights)
RES1 D2 (rename §6) → superseded by RES3 D16 (keep Fact Candidates)
RES2 D12 (Diagrams everywhere) → superseded by RES4 D22 (per-template naming)
```

This chain demonstrates why multi-iteration research matters: iteration 1 proposed wrong naming, iteration 3 corrected it with empirical evidence.

## 11. Strategic Insights (Planning)

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | TFW = value operating system for ANY domain. Target audience = product leaders, PMs, analysts, educators — not pure coders | philosophy | User, VLM-3 RES1 |
| S2 | «Focus on value and how to scale it. Not only to programmers, but to higher level» — positioning north star | stakeholder | User |
| S3 | docs vs knowledge conflict is a REAL pain. Agent refuses to work after knowledge consolidation | process | User, direct report |
| S4 | «Last status should be knowledge collection, explicitly» — pipeline gap confirmed | process | User |
| S5 | «docs = technical things from project. Knowledge = things from outside you can't learn from code» — foundational distinction | philosophy | User |
| S6 | Thinking traces = future TODO. «I don't understand what this is yet» — honest uncertainty | stakeholder | User |
| S7 | Knowledge Pipeline = killer feature (survived sycophancy demolition in VLM-3) | philosophy | VLM-3 RES3 |
| S8 | 8 TFW-unique features absent from ALL coding agents | domain | VLM-3 RES1 |
| S9 | TFW = team tool, not individual. «AI assistants are part of the team and part of knowledge» | philosophy | User |
| S10 | «Product people learn TFW faster than engineers learn business thinking» — primary audience signal | stakeholder | User |
| S11 | «Any growing business suffers from communication gaps, decentralized decision-making, information not flowing» — universal pain | domain | User |
| S12 | Multi-iteration research: «researcher rushes to close. Coordinator decides how many iterations» | process | User |
| S13 | «Section name = strongest single-word prompt. If named right, AI needs fewer instructions» (Claude Code Dreaming) | philosophy | User |
| S14 | Terms become communication foundation for humans too. Balance: industry (understood) vs custom (value-centric) | philosophy | User |
| S15 | §3.1 = Amazon Working Backwards. «See the result, imagine it's done.» NOT a process diagram | philosophy | User |
| S16 | «Different artifacts = different framings, different mindsets» — template names are context-tuned micro-prompts | philosophy | User |
| S17 | «Collection algorithm reads each section — agent doesn't need standardized names to collect» | process | User |

---

*HL — TFW-32: Methodology Refinement & Product Positioning | 2026-04-10*
