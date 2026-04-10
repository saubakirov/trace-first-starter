# Extract — "What do we NOT see?"
> Parent: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> Goal: Fix TFW's pipeline gaps and clarify positioning for non-engineer audience.

## Findings

### E1: docs-vs-knowledge architecture — orchestrated pair, not merge

**Decision: H1 REFUTED.** SECI model + user input confirm: docs and knowledge are different processes. But they must be orchestrated, not independent.

**Proposed architecture: KNW status = orchestration point**

```
... → 🔍 REV → 📚 KNW → ✅ DONE
                  │
                  ├── Step 1: /tfw-docs (always) — Combination (explicit→explicit)
                  │   Updates: §1 Architecture Map, §2 Decisions, §3 Legacy, TECH_DEBT.md
                  │   Output: "docs complete. Run /tfw-knowledge if Fact Candidates exist."
                  │
                  └── Step 2: /tfw-knowledge (conditional) — Externalization (tacit→explicit)
                      Trigger: FC exist in RF/REVIEW/RES for this task
                      Updates: knowledge/ topic files, §4 Project Facts index
                      Output: "knowledge complete. Task → ✅ DONE."
```

**Fix for tfw-knowledge Phase 4:** Strip §1/§2 updates from tfw-knowledge entirely. Phase 4 becomes:
- Update §4 Project Facts index (counts + links) — KEEP (this IS knowledge territory)
- Update knowledge_state.yaml — KEEP
- ~~Update §1 Architecture Decisions~~ — REMOVE (tfw-docs territory)
- ~~Update §2 Key Artifacts~~ — REMOVE (tfw-docs territory)

**Orchestration options (from user input: "one should recommend launching the other"):**

| Option | Mechanism | User burden | Agent autonomy |
|--------|-----------|-------------|----------------|
| A: Sequential in one session | tfw-docs runs, then says "now run /tfw-knowledge" | User must obey recommendation | Low — user intermediates |
| B: tfw-docs calls tfw-knowledge | tfw-docs finishes, automatically launches knowledge phase | Zero — one command | High — requires agent to switch context mid-session |
| C: KNW status with substatus | Task Board shows `📚 KNW (docs)` → `📚 KNW (knw)` → `✅ DONE` | User sees progress, acts on prompts | Medium |
| D: YAML tracking in REVIEW | REVIEW file gets `tfw-docs: done`, `tfw-knowledge: done/N/A` markers | Markers guide next agent session | Low — filesystem state |

**Recommendation: Option D (YAML markers in REVIEW) + tfw-docs recommends next step.**
- Already partially exists: tfw-docs writes `tfw-docs: Applied — updated Sections 1, 3` or `tfw-docs: N/A`
- Add: `tfw-knowledge: pending` / `tfw-knowledge: applied` / `tfw-knowledge: N/A (no FC)`
- tfw-docs ending: "Docs update complete. Fact Candidates detected in RF §6 / REVIEW §5 — run `/tfw-knowledge` to consolidate. Or mark `tfw-knowledge: N/A` if no actionable facts."
- tfw-review ending: after writing REVIEW + verdict, prompt "Run `/tfw-docs` to update project documentation."
- Status 📚 KNW = both markers are set (Applied or N/A)

### E2: Fact Candidates vs Strategic Insights — TWO concepts, ONE pipeline

**Decision: H5 CONFIRMED.** User (Q2) + SECI model confirm these capture different knowledge types:

| Concept | What it captures | SECI phase | Source | Discoverable from code? |
|---------|-----------------|------------|--------|------------------------|
| **Fact Candidates** | Operational observations during work — patterns, bugs, debt, constraints, architecture | Externalization (agent extracts tacit patterns from work) | RF §6, REVIEW §5, RES §FC | Partially — agent observes during execution |
| **Strategic Insights** | Domain/stakeholder knowledge — priorities, emotions, vision, market context, business rules | Socialization (human shares tacit knowledge) | HL §11, RF §7 | **Never** — only human can provide |

**Terminology decision:**
- Keep BOTH terms. They are different concepts per D28 (Naming Creates Behavior)
- **Fact Candidates** = agent-generated observations (bottom-up)
- **Strategic Insights** = human-sourced knowledge signals (top-down)
- Both feed into `/tfw-knowledge` consolidation, but with different trust levels:
  - FC: needs Human-Only Test filter (some are just implementation details)
  - SI: pre-filtered by coordinator — higher trust, higher value

**Template changes needed:**
- HL §11: rename "Strategic Session Insights" → "Strategic Insights" (drop "Session" — redundant)
- RF §7: rename "Execution Session Insights" → "Strategic Insights (Execution)" — same concept, different phase
- Glossary: add "Strategic Insight" entry (already exists but weak — strengthen)
- tfw-knowledge Phase 2: explicitly scan both FC and SI sections, note different trust levels

This **resolves TD-76** differently than HL proposed. HL wanted to merge into one term. Research shows they ARE two concepts. The fix is: sharpen definitions + unify pipeline, not unify names.

### E3: Multi-iteration research — control file design

**Design for `research/iterations.yaml`:**

```yaml
# Written by coordinator, read/updated by researcher
task: TFW-32
goal: "Fix pipeline gaps and clarify positioning"
min_iterations: 3
current_iteration: 1

iterations:
  - id: 1
    focus: "docs-vs-knowledge architecture, positioning patterns"
    hypotheses: [H1, H2, H3, H8]
    status: complete  # set by researcher
    res_file: "RES__iter1__architecture.md"
    key_decisions: [D1, D2]  # set by researcher
    gaps: ["multi-iteration formalization", "audience persona matrix"]

  - id: 2
    focus: "multi-iteration research, terminology"
    hypotheses: [H5, H7]
    status: pending
    res_file: null
    key_decisions: []
    gaps: []

accumulated:
  decisions: [D1, D2]  # growing list
  tested_hypotheses: [H1, H2]
  remaining_gaps: ["audience persona matrix"]
```

**Workflow changes for multi-iteration:**

1. **plan.md Step 6 extension:** When coordinator recommends research, can specify `min_iterations: N` and write `research/iterations.yaml` with hypothesis groupings
2. **research/base.md Step 0 extension:** Check for `iterations.yaml`. If exists → read current iteration context. If `current_iteration > 1` → also read previous RES files
3. **research/base.md Step 6 (Synthesis) extension:** Update `iterations.yaml` with completed iteration data. End with: "Iteration {N} complete. {M} iterations remaining. Launch next `/tfw-research` in a new agent."
4. **Naming:** RES files get iteration suffix: `RES__iter{N}__{focus}.md`. Final synthesis (by coordinator after all iterations): `RES__TFW-32__methodology_and_positioning.md`

**Key constraint (from user):** Researcher always rushes to close. The `min_iterations` in YAML is a hard floor — researcher CANNOT write the final RES. Only coordinator consolidates after all iterations.

### E4: Positioning architecture — pain point + translation layer

**User's pain-point statement (from Q2 answers):**
> "Any business growing suffers from communication gaps, lack of information exchange, decentralized decision-making, information not flowing up and down. Here we try to solve this through routine and methodology — so that all team members contribute to knowledge. Most tools are individual — they boost one person. We want team play where AI assistants/agents are part of the team and part of knowledge and communications."

**TFW pain-point formulation:**

**Problem:** Growing teams lose knowledge. Decisions don't propagate. Information doesn't flow between people, departments, and AI agents. Every new team member (human or AI) starts from zero.

**TFW solution:** A methodology that makes knowledge accumulation automatic — built into the work process, not bolted on after. AI agents are team members who read, write, and preserve institutional memory.

**Differentiator (from H4, confirmed):** No other framework combines:
1. Structured lifecycle (HL → RES → TS → RF → REVIEW)
2. Role-locked specialization (Coordinator, Researcher, Executor, Reviewer)
3. Knowledge pipeline (FC + SI → consolidation → verified facts → cross-session persistence)
4. Domain-agnostic (code, analytics, writing, education, business)

**Translation table for README:**

| TFW Technical | Business-Friendly |
|--------------|-------------------|
| HL (High Level) | Decision map — captures what, why, and what we're betting on |
| TS (Task Spec) | Clear brief — exactly what to do, when it's done |
| RF (Result File) | Execution record — what happened, what we learned |
| REVIEW | Quality gate — independent check before closing |
| Fact Candidates | Team observations — patterns spotted during work |
| Strategic Insights | Institutional knowledge — what only people know |
| Knowledge Pipeline | Organizational memory — gets smarter with every task |
| Role Lock | Clear ownership — no one person does everything |
| Task Board | Single source of truth — everyone sees the same picture |

**Audience persona (refined from user Q3 input):**

| Persona | Pain point | How TFW helps | Adoption path |
|---------|------------|---------------|---------------|
| **Product leader / Entrepreneur** | "My AI helps me but doesn't remember. I repeat context every session" | Knowledge persists. Every task builds on the last. AI reads history, not you | Primary audience — learns faster than engineers learn business thinking |
| **Team lead / PM** | "Knowledge lives in people's heads. When someone leaves, knowledge leaves" | Structured capture of decisions, alternatives, and reasoning. Fact Candidates + Strategic Insights create institutional memory | High value — directly addresses #1 scaling pain |
| **Analyst / Researcher** | "I do deep work but can't trace my reasoning chain afterwards" | Research stages (Gather → Extract → Challenge) preserve the investigation, not just the conclusion | Natural fit — research workflow maps directly |
| **Engineer (product-minded)** | "I make architecture decisions but nobody knows why 6 months later" | Architecture Decision records (D-table), Observations, Tech Debt registry | Secondary — needs to think beyond code. TFW is a "step up" |

**Key positioning insight:** TFW is NOT "for everyone." It's for teams where **knowledge loss costs money** — growing businesses, distributed teams, AI-augmented workflows where session continuity is critical.

### E5: H2 analysis — KNOWLEDGE.md rename

**Current state:**
- `KNOWLEDGE.md` = mix of documentation (§1-§3) and knowledge index (§4)
- `knowledge/` folder = verified facts (pure knowledge)
- User suggestion: rename KNOWLEDGE.md → DOCS.md or INDEX.md

**Analysis:**

| Option | Pros | Cons |
|--------|------|------|
| Keep KNOWLEDGE.md | No breaking changes, familiar | Name lies — it's mostly documentation, not knowledge |
| Rename → DOCS.md | Honest name, matches tfw-docs | Breaks every reference in conventions, workflows, templates, CHANGELOG, task board. Massive sed-job |
| Rename → INDEX.md | Neutral name | Vague — index of what? |
| Keep name, fix content | Zero migration cost | Name still misleading |

**Decision: H2 PARTIALLY CONFIRMED but DEFERRED.** The naming IS confusing, but the cost of renaming is high (every TFW file references KNOWLEDGE.md). Better fix for THIS task: remove §0 (move to knowledge/philosophy.md), fix tfw-knowledge Phase 4 overlap. Rename = separate future task when all references are in a single compilable contract (which already exists for resolution).

### E6: H3 — KNW status viability

**H3 CONFIRMED.** The pipeline gap is real:
- 21 RF files had zero facts (from TFW-18 analysis)
- Knowledge Gate in plan.md Phase 0 gates the NEXT task, not the CURRENT one
- Adding 📚 KNW makes knowledge collection visible on Task Board
- Skippable with N/A preserves flow for trivial tasks

KNW status mechanics:
- Trigger: REVIEW verdict = ✅ APPROVE
- Entry: coordinator runs `/tfw-docs` + optionally `/tfw-knowledge`
- Exit: both markers set in REVIEW (Applied or N/A)
- Task Board: status changes `🔍 REV → 📚 KNW → ✅ DONE`
- If reviewer approved but docs not needed: `📚 KNW (N/A)` → `✅ DONE`

## Checkpoint

| Found | Remaining |
|-------|-----------|
| H1 REFUTED: workflows stay separate, fix overlap in Phase 4 | Validate: could Phase 4 strip cause data loss? |
| H5 CONFIRMED with twist: FC ≠ SI, keep both, sharpen definitions | Check: does glossary "Strategic Insight" entry need rewrite? |
| H7 design: iterations.yaml + iteration folders + coordinator consolidation | Stress test: what if researcher writes final RES anyway? |
| H8 refined: "teams where knowledge loss costs money" | Challenge: is this too narrow? |
| H2 DEFERRED: rename is correct but costly, fix content first | — |
| H3 CONFIRMED: KNW status with REVIEW markers | Challenge: does adding another status slow down simple tasks? |
| Pain point: "Growing teams lose knowledge. AI agents are team members." | Challenge: does any competitor claim this? |

**Sufficiency:**
- [x] External source used? (SECI model applied to architecture, Shape Up/DORA/Scrum for positioning)
- [x] Briefing gap closed? (all 6 in-scope hypotheses addressed)

**Deep mode criteria:**
- [x] Hypothesis tested? H1 (refuted), H2 (deferred), H3 (confirmed), H5 (confirmed), H7 (designed), H8 (refined)
- [x] Counter-evidence sought? For H1: sought reasons to merge (simplicity). For H5: sought reasons to unify terms (D28). For H2: sought reasons to rename now (honesty). Found counter-arguments for each.

**Metacognitive check:** New discovery = positioning as TEAM tool, not individual. User's "most tools are individual, we want team play" is a genuine differentiator I hadn't considered. This changes the README positioning fundamentally — TFW isn't competing with Cursor/Claude features (individual boost), it's competing with knowledge management systems (Confluence, Notion) and methodology frameworks (Scrum, Shape Up).

Stage complete: YES
→ User decision: ___
