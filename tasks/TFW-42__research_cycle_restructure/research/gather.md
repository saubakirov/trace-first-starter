# Gather — "What do we NOT know?"
> Parent: [HL-TFW-42](../../HL-TFW-42__research_cycle_restructure.md)
> Goal: Determine how TFW should present multi-agent research orchestration to users via iterations.yaml.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1: Agent specification | Free-text name only (`agent: antigravity`) | Structured profile (`agent: {name, strengths, model}`) | Enum from registry (`agent: antigravity` validated against `.tfw/agents.yaml`) | No agent field — implicit from context |
| D2: Iteration dependency | Linear chain (`depends_on: [iter-1]`) | DAG (arbitrary `depends_on` graph) | None (pure sequential by number) | Implicit (each reads predecessor RES) |
| D3: Framework guidance | Document-only (conventions describe multi-agent as possible) | Prompt-in-template (iterations.yaml template includes `agent:` with comment guidance) | Active suggestion (plan.md Step 6b prompts coordinator to consider agent assignment) | Auto-detect (framework infers best agent from iteration focus) |

## Findings

### G1: Multi-agent framework landscape (external research)

Surveyed 4 major multi-agent frameworks (CrewAI, AutoGen, LangGraph, MetaGPT) + industry methodology patterns.

**Key patterns discovered:**

| Framework | Agent specification | Task-agent binding | Config format | Orchestration |
|-----------|--------------------|--------------------|---------------|---------------|
| CrewAI | YAML: role, goal, backstory, allow_delegation | `agent:` field on task YAML | Separate `agents.yaml` + `tasks.yaml` | Sequential or Hierarchical (code) |
| AutoGen | Python: name, description, llm_config | `speaker_selection_method` (auto/manual/custom) | Code + JSON for LLM config | GroupChat manager selects dynamically |
| LangGraph | Python: node functions | Conditional edges (routing functions) | Code (state machine) | Graph-based with state schema |
| MetaGPT | YAML: role-specific LLM config | `_watch` / `_act` cycle (message-passing) | `config2.yaml` for LLM, Python for structure | SOP (Standard Operating Procedure) |

**Critical distinction**: All frameworks separate agent DEFINITION (who the agent is) from task ASSIGNMENT (which task the agent works on). CrewAI is the closest analogue to TFW's model — YAML config, explicit agent assignment per task.

**TFW's position**: TFW doesn't need agent definition (agents are external tools — Antigravity, Claude Code, Codex CLI). TFW only needs task assignment — which iteration gets which agent. This is simpler than all surveyed frameworks.

### G2: AFD-2 empirical patterns (internal analysis)

From HL §2 and iterations.yaml focus field:

| Iteration | Agent | Focus | Why this agent |
|-----------|-------|-------|---------------|
| 1 | Antigravity | Initial investigation (web research + domain analysis) | Best at web search, multi-source synthesis, large context |
| 2 | Codex CLI | Code audit (Gradle structure analysis) | Fast file traversal, code-native, can run commands |
| 3 | Codex CLI | Deeper code audit (module dependency mapping) | Continuation of iter 2, same tool strengths |
| 4 | Antigravity | Architecture synthesis (26-module design) | Required web research (Gradle best practices) + large synthesis |
| 5 | Claude Code | Server reconnaissance (production infra audit) | MCP server access, interactive SSH, real-time queries |
| 6 | Antigravity | Domain modeling (port-interface contracts) | Large context window needed for cross-module design |
| 7 | Antigravity | Build-logic research (convention plugins) | Web research on Gradle conventions + synthesis |
| 8 | Antigravity | Final synthesis (implementation strategy) | Cross-iteration synthesis requiring full context |

**Patterns observed:**
1. Agent choice correlates with iteration TYPE, not with sequential position
2. Three agent archetypes emerge: **Web Researcher** (Antigravity), **Code Auditor** (Codex), **Infra Operator** (Claude Code)
3. Consecutive iterations with same agent (2→3, 6→7→8) suggest "continuation" is a natural pattern
4. Agent switching happened at domain boundaries, not arbitrary points
5. No iteration used more than one agent — agent is per-iteration, not per-stage

### G3: TFW coordinator workflow analysis (internal)

Current `plan.md` Step 6b creates `iterations.yaml`. The coordinator decides:
- How many iterations
- What each iteration investigates (focus + hypotheses)
- Status tracking

**Missing from current workflow:**
- No prompt to consider agent assignment
- No guidance on WHEN different agents are useful
- No mechanism to express "this iteration needs web research" vs "this needs code audit"

The `agent` field in HL-TFW-42's proposed schema is a string — free text. This matches AFD-2's actual usage where agents were named informally.

### G4: Industry methodology patterns (external research)

**Supervisor-Worker** is the dominant pattern for high-stakes multi-agent research:
- Central coordinator decomposes work
- Specialized workers execute subtasks
- Results flow back to coordinator for synthesis

This maps directly to TFW's model: Coordinator (plan.md) → Researcher (research/base.md) → back to Coordinator.

**Human-in-the-loop patterns:**
- "Pause points" / structured gates — TFW already has these (🛑 WAIT gates)
- "Progressive autonomy" — TFW supports via CL/AG modes
- "Role-based specialization" — TFW has Role Lock

**Key insight from methodology research:** The industry consensus is that agent selection should be **coordinator-driven with guidance**, not automated. Auto-detection requires capability models that don't exist yet for AI coding tools. Best practice: provide a decision framework, let the human/coordinator choose.

### G5: Counter-evidence — when agent field adds overhead (deep mode requirement)

**Counter-argument**: Most TFW projects use a single agent. Adding `agent` field creates noise for the common case.

**Evidence for counter:**
- Of all TFW-42's predecessor tasks (TFW-2 through TFW-41), ALL used a single agent (Antigravity or Claude Code)
- Multi-agent research is observed only in AFD-2 (a large, multi-domain project)
- Single-agent projects would write `agent: antigravity` on every iteration — pure noise

**Mitigation found in HL §7 P5:** "Optional enrichment — new iterations.yaml fields are optional." This principle already addresses the counter-argument. The field exists for those who need it, doesn't burden those who don't.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| 3 dimensions identified with 4 alternatives each | None — space well-mapped |
| 4 external frameworks analyzed + 1 methodology survey | None |
| AFD-2 empirical data mapped (8 iterations, 3 agent archetypes) | None |
| Counter-evidence found and addressed (single-agent overhead) | None |

**Sufficiency:**
- [x] External source used? (5 web searches: CrewAI, AutoGen, LangGraph, MetaGPT, methodology patterns)
- [x] Briefing gap closed? (H1 evidence gathered from both external and internal sources)
- [x] Dimensions identified? (3 dimensions × 4 alternatives each)

**Deep mode criteria:**
- [x] Hypothesis tested? (H1 — agent field in iterations.yaml vs separate mechanism — evidence gathered)
- [x] Counter-evidence sought? (G5: single-agent overhead)

**Metacognitive check:** I discovered something NEW — the distinction between agent definition and task assignment. TFW doesn't need agent profiles (unlike CrewAI/MetaGPT) because agents are external tools. This simplifies the design significantly. I also discovered the 3-archetype pattern from AFD-2 data, which is actionable for framework guidance.

Stage complete: YES
→ User decision: proceed (autonomous mode)
