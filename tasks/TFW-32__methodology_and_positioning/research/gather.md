# Gather — "What do we NOT know?"
> Parent: [HL-TFW-32](../HL-TFW-32__methodology_and_positioning.md)
> Goal: Fix TFW's pipeline gaps and clarify positioning for non-engineer audience.

## Findings

### G1: docs-vs-knowledge workflow overlap analysis

**tfw-docs** produces updates to:
- `KNOWLEDGE.md` §1 Architecture Map (new components)
- `KNOWLEDGE.md` §2 Architecture Decisions (new D-records)
- `KNOWLEDGE.md` §3 Legacy & Deprecation (removed items)
- `TECH_DEBT.md` (new entries)
- Also item #5: "New principle or convention?" → KNOWLEDGE.md or conventions
- Item #6: explicitly says "Do NOT consolidate facts here — that is /tfw-knowledge's job"

**tfw-knowledge** produces updates to:
- `KNOWLEDGE.md` §4 Project Facts (index counts/links)
- `knowledge/{category}.md` topic files (verified facts)
- `.tfw/knowledge_state.yaml` (consolidation tracking)
- Also Phase 4 Update: §1 Architecture Decisions, §2 Key Artifacts — **OVERLAP with tfw-docs**

**Collision point identified:** tfw-knowledge Phase 4 explicitly writes to §1 and §2 of KNOWLEDGE.md — the same sections tfw-docs writes to. This is where the agent says "already captured."

User distinction (from briefing Q2):
- **Documentation** = facts about the project discoverable from the project itself (how it's built)
- **Knowledge** = facts from OUTSIDE the project, things you can't learn from code (sales, support, commercial, human decisions)

Mapping this to current KNOWLEDGE.md sections:
- §0 Philosophy & Principles → **Knowledge** (human decisions, values — not discoverable from code)
- §1 Architecture Map → **Documentation** (discoverable from the project)
- §2 Architecture Decisions table → **Mixed**: the decision = documentation, the rationale = sometimes knowledge
- §3 Legacy & Deprecation → **Documentation** (discoverable from git history + files)
- §4 Project Facts → **Knowledge** (index to knowledge/ folder)

### G2: How methodology frameworks position for non-engineers

**Shape Up (Basecamp):**
- Primary audience: "product teams facing challenges with traditional agile"
- Pain-point framing: "stalled progress, high admin burden, desire for strategic focus"
- Language: "betting" not "sprint planning", "shaping" not "requirements", "appetite" not "estimate"
- Key: describes PROBLEMS first, then names the solution elements
- Adoption barrier: "requires culture of autonomy and trust, works best with experienced teams"

**DORA:**
- Positioning to business: "business intelligence framework that measures how efficiently an organization converts investments into customer value"
- Translation table: each technical metric → business-language equivalent
- "Deployment Frequency" → "Business Agility: How quickly can we respond to market changes?"
- Emphasis: "measures the system/process, not individual developers"

**Scrum Guide 2020:**
- Product Owner framed as "Value Maximizer" not "backlog manager"
- Translation: "manages the Product Backlog" → "maintains categorized master list of what matters most"
- Core: "The Product Owner owns the 'Why' and the 'What.' The team owns the 'How.'"

**Pattern observed:** All three frameworks use a **translation layer** — technical concepts reframed in business language. None of them say "for everyone." Each names a specific pain point. Shape Up is closest to TFW in philosophy (structured autonomy, fixed time/variable scope).

### G3: Multi-iteration research patterns

**External research on "control file" pattern:**
- Common architecture: control file (`.md` or `.yaml`) read at session start, updated during work, persisted between sessions
- Three memory tiers: short-term (chat context), working state (active task/step tracking), long-term (accumulated facts/decisions)
- Best practice: "Aggressive Summarization" — store summaries, not raw history
- Separate concerns: control file stores paths/links to full artifacts, not artifacts themselves
- Frameworks: Letta (MemGPT), Mem0, LangChain memory — all provide cross-session persistence

**VLM-3 actual experience (from HL §11 S17):**
- RES1 → RES2 → RES3 → RES4 in separate agents
- User insight: "researcher rushes to close. Coordinator decides how many iterations"
- State needed between iterations: hypotheses tested, decisions made, gaps remaining
- Current TFW research has NO mechanism for this — each `/tfw-research` produces one RES and says "done"

**Gap:** TFW already has the filesystem state machine (D31) — `research/` subfolder with stage files. Multi-iteration could extend this: `research/iteration_1/`, `research/iteration_2/`, plus a control file at `research/control.md` or `research/state.yaml`. The coordinator writes the control file with iteration count, hypothesis assignments, and accumulation state. Each researcher reads it, writes their RES, and updates it.

### G4: KNOWLEDGE.md structure analysis — who reads what

| Section | Updated by | Read by | Purpose |
|---------|-----------|---------|---------|
| §0 Philosophy | Nobody recently (frozen) | Agents at context load | Set values frame |
| §1 Architecture Map | tfw-docs + tfw-knowledge(!) | Agents at context load | Understand project structure |
| §2 Architecture Decisions | tfw-docs + tfw-knowledge(!) | Agents at context load | Understand past decisions |
| §3 Legacy | tfw-docs | Agents (less frequent) | Know what's deprecated |
| §4 Project Facts | tfw-knowledge | Agents at context load | Navigate to knowledge/ |

Two problems visible:
1. §0 is orphaned — no workflow updates it. User already said it should be in `knowledge/philosophy.md` (which exists with 14 facts)
2. §1/§2 dual-written by both workflows — root cause of conflict

### G5: External theory — SECI model mapping to TFW

The Nonaka-Takeuchi SECI model maps cleanly onto TFW's docs-vs-knowledge distinction:

| SECI Stage | TFW Equivalent | Flow |
|-----------|---------------|------|
| **Socialization** (tacit→tacit) | HL §11 Strategic Insights, user conversations | Human shares tacit knowledge with AI |
| **Externalization** (tacit→explicit) | Fact Candidates in RF/REVIEW/RES | AI captures observations into structured form |
| **Combination** (explicit→explicit) | tfw-docs: updating Architecture Map, D-records | Merging project-internal explicit facts |
| **Internalization** (explicit→tacit) | Context Loading (§10): next agent reads KNOWLEDGE.md | Agent absorbs explicit docs to build operational understanding |

This confirms the user's distinction:
- **tfw-docs = Combination phase** (explicit→explicit, internal project facts — discoverable)
- **tfw-knowledge = Externalization + Socialization** (tacit→explicit, human knowledge — NOT discoverable)

This is a clean theoretical boundary. The current overlap exists because tfw-knowledge's Phase 4 tries to also do Combination work (updating §1/§2).

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Exact collision: tfw-knowledge Phase 4 writes to §1/§2 — tfw-docs territory | Design: should Phase 4 be stripped from tfw-knowledge, or should tfw-docs absorb it? |
| Methodology positioning pattern: pain-point framing + translation layer | TFW's specific translation table (what technical terms become business terms) |
| Multi-iteration state: control file pattern confirmed externally, TFW already has filesystem state machine as foundation | Design: exact format and location of iteration control file |
| SECI model validates docs=Combination, knowledge=Externalization | Apply to H1 (merge or keep separate) — SECI says they ARE different processes |
| §0 Philosophy orphaned — should move to knowledge/ | Already proposed in HL, now validated — no workflow touches §0 |

**Sufficiency:**
- [x] External source used? (Shape Up, DORA, Scrum Guide, SECI model, control file pattern research)
- [x] Briefing gap closed? (docs-vs-knowledge overlap mapped precisely, positioning patterns gathered, multi-iteration mechanism researched)

**Deep mode criteria:**
- [x] Hypothesis tested? H1 tested — SECI says docs and knowledge are DIFFERENT processes. Merging conflates Combination (explicit→explicit) with Externalization (tacit→explicit)
- [x] Counter-evidence sought? Sought reasons to merge: simpler (1 workflow instead of 2), fewer context loads. Found: SECI model says they serve different cognitive functions. Merging = forcing one agent to do two different types of knowledge work

**Metacognitive check:** I discovered something NEW — the SECI model mapping. I didn't just confirm what I already knew. The Combination vs Externalization distinction is a theoretical anchor for why the workflows should stay separate.

Stage complete: YES
→ User decision: ___
