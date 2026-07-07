# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW-45](../../HL-TFW-45__multi_agent_workflows.md)
> Goal: Map viable swarm configurations across platforms and identify where one protocol covers all vs where platform-specific branches are needed.

## Configuration Space

Cross-referencing the 3 most decision-relevant Gather dimensions: **D1 (Platform)**, **D2 (Instruction injection model)**, and **D3 (Sub-agent context inheritance)**.

D4 (Invocation semantics) and D5 (Communication) are used as filters — they constrain which combinations are viable but don't create independent choices.

| Config | D1: Platform | D2: How sub-agent gets instructions | D3: How sub-agent inherits TFW context | Viable? | Notes |
|--------|-------------|-------------------------------------|----------------------------------------|---------|-------|
| C1 | Antigravity | `define_subagent.system_prompt` (TRUE system prompt) | `self` type — inherits full parent config (rules, tools, model) | ✅ | **Richest option.** Sub-agent gets Mindset as system prompt AND inherits all TFW rules. BUT: `self` type = inherits PARENT's system prompt, not custom one |
| C2 | Antigravity | `define_subagent.system_prompt` (TRUE system prompt) | Custom type — ONLY what's in system_prompt param | ✅ | **Cleanest isolation.** Sub-agent gets ONLY Mindset + explicitly injected TFW context. No parent baggage. But must include TFW loading rules in system_prompt |
| C3 | Antigravity | `self` type (inherits parent prompt + custom task prompt) | Full parent clone + task-specific prompt via invoke | ✅ | Sub-agent = clone of parent with same rules. Task prompt adds stage-specific instructions. Mindset = task prompt, not system prompt. **Less pure** than C2 |
| C4 | Claude Code | Agent definition `.md` file (own prompt) | Explicit — must include all needed rules in agent file | ✅ | Sub-agent gets its own `.claude/agents/stage_name.md`. TFW rules must be explicitly included or referenced. CLAUDE.md inheritance unreliable |
| C5 | Claude Code | Agent Teams (peer-to-peer) | Shared task list + mailbox, isolated context per agent | ✅ | **NEW capability (Feb 2026).** Agents coordinate via shared files. Each has own 1M context. 3-7x cost. Best for parallel stages (review?) |
| C6 | Claude Code | `<system-reminder>` via CLAUDE.md | Automatic CLAUDE.md loading (unreliable for sub-agents) | ⚠️ | Main agent only — not suitable for sub-agent Mindset injection |
| C7 | Codex | TOML agent definition + `model_instructions_file` | Global AGENTS.md inherited + specialized instructions override | ✅ | Sub-agent defined in `.codex/agents/`. Gets Mindset as `model_instructions_file`. AGENTS.md (TFW) inherited automatically |
| C8 | Codex | Direct task prompt to sub-agent | Only global AGENTS.md inherited | ⚠️ | No custom system prompt — sub-agent just gets a task. Mindset = task instruction, not identity |
| C9 | ANY platform | No sub-agents (single agent) | Full context (single conversation) | ✅ | **Fallback.** `focused.md`/`deep.md` mode. Current behavior. Must remain working |

## Findings

### E1: The `self` vs custom sub-agent dilemma (Antigravity)

The HL proposes: "define_subagent with Mindset as system_prompt." But there's a tension I notice:

- **`self` type (C3):** inherits parent's full system prompt (including `.agent/rules/`). The sub-agent automatically has all TFW rules. BUT the `system_prompt` parameter for `self` is the PARENT's system prompt — you can't inject a custom Mindset as system_prompt AND inherit parent config. The Mindset goes into the `Prompt` field of `invoke_subagent`, which is a task prompt, not a system prompt.

- **Custom type (C2):** you write a custom `system_prompt` with Mindset identity + TFW context loading instructions. The sub-agent starts fresh with ONLY what you put in `system_prompt`. This is the "clean slate" model. BUT you must inject TFW rules into the system_prompt manually (or instruct the agent to read them from filesystem).

- **Key insight:** For genuine Mindset-as-identity, C2 (custom type) is correct — Mindset IS the system prompt. For TFW compliance, C3 (self type) is easier — rules are inherited. **These pull in opposite directions.**

**Resolution options:**
- (a) Custom type + explicit TFW context loading in system_prompt: `"You are The Explorer. Read AGENTS.md, then .tfw/conventions.md..."` — agent loads TFW context as its first action
- (b) Custom type + Mindset AND TFW rules pasted into system_prompt — but this may exceed token budget
- (c) `self` type + Mindset in task prompt — weaker (task ≠ identity), but TFW rules guaranteed

### E2: Claude Code's two sub-agent models

Claude Code offers TWO fundamentally different sub-agent architectures:

1. **Subagents** (hierarchical): Parent spawns child, child reports back. Agent definition in `.claude/agents/*.md`. Child gets its own context window. CLAUDE.md inheritance unreliable.

2. **Agent Teams** (peer-to-peer, Feb 2026+): Agents coordinate via shared files and mailbox. Each has independent 1M context. Direct inter-agent communication. 3-7x cost.

For TFW swarm mode:
- **Subagents** (C4) = closer to Antigravity's `define_subagent` model. Sequential stages work naturally (parent invokes Gather agent → collects result → invokes Extract agent).
- **Agent Teams** (C5) = overkill for sequential research stages but interesting for review (where Map/Verify could potentially run in partial parallel with later stages benefiting from earlier ones).

**Hidden combination nobody proposed:** Use Agent Teams for review (Map + Verify can partially overlap) while using hierarchical subagents for research (strict sequential). Different swarm protocols for different workflows.

### E3: Codex as the simplest model

Codex (C7) has the cleanest architecture for swarm mode:
- `AGENTS.md` in project root = automatically inherited by all sub-agents (TFW rules covered)
- TOML agent definition with `model_instructions_file` = custom system prompt per stage (Mindset covered)
- No inheritance ambiguity

This means: if we design swarm.md for Codex's model first, we get the simplest protocol. Antigravity and Claude Code need additional steps (explicit context loading, unreliable inheritance workarounds).

### E4: The "what goes in rules" implication

From G6, the adapter strategy becomes clear:

| Platform | "TFW identity" file | "TFW stage Mindset" injection |
|----------|---------------------|-------------------------------|
| **Antigravity** | `.agent/rules/tfw.md` + `.agent/rules/agents.md` (TRUE system prompt) | `define_subagent.system_prompt` param (custom type) |
| **Claude Code** | `CLAUDE.md` (high-priority context) + `.claude/rules/` | `.claude/agents/stage_name.md` body |
| **Codex** | `AGENTS.md` (auto-inherited) | `.codex/agents/stage.toml` → `model_instructions_file` |

**What should be in `.agent/rules/` (Antigravity)?**
Everything that MUST be enforced — it's the only place with "MUST ALWAYS FOLLOW WITHOUT ANY EXCEPTION" language. Currently we have 2 rules files totaling ~2.6KB. This is the right content:
- `agents.md` — role, conduct, context loading order (= AGENTS.md content)
- `tfw.md` — TFW is active, follow conventions, no sycophancy, no placeholders

**What should NOT be in rules?** Workflow-specific instructions (those are workflows). Stage templates (those are read on demand). Anything that changes per-task.

### E5: Hidden combination — The "coordinator stays, stages spawn" model

The HL assumes the coordinator agent manages everything: writes briefing, spawns sub-agents, collects results, writes RES. But there's a simpler variant:

**The coordinator IS the parent agent.** It doesn't need `define_subagent` for itself — it already has TFW rules via `.agent/rules/`. It writes the briefing normally. Then it spawns sub-agents ONLY for the stages where fresh Mindset matters (Gather, Extract, Challenge). It reads their outputs and writes RES itself.

This means swarm.md doesn't need to describe how the coordinator works — it already works via `base.md`. Swarm.md only describes how to spawn and coordinate stage agents. **This is simpler than the HL's full-rewrite model.**

## Checkpoint

| Found | Remaining |
|-------|-----------|
| 9 configurations across 3 platforms | Consistency check: which combinations are incompatible? |
| `self` vs custom type tension (E1) | Resolution: which option for Antigravity? |
| Claude's two sub-agent models (E2) | Whether Agent Teams cost is justified for review |
| Codex = cleanest model (E3) | Whether Codex model can be the canonical reference |
| "Coordinator stays" simplification (E5) | Impact on swarm.md word budget |
| What belongs in `.agent/rules/` (E4) | Exact content for adapter restructure |
| Hidden combo: different swarm for research vs review | |

**Sufficiency:**
- [x] External source used? (Building on Gather's 12 web searches + first-hand observation)
- [x] Briefing gap closed? (Design space mapped, hidden combinations surfaced)
- [x] Configuration Space built from Gather dimensions? (9 configs across 3 platforms)
- [x] Hypothesis tested? (Design implications for H2, H3, H6, H7 materialized)
- [x] Counter-evidence sought? (`self` type tension undermines naive "just use system_prompt" — E1 reveals the trade-off)
- [x] Metacognitive check: E5 ("coordinator stays") and E2 (different swarm per workflow type) are combinations nobody proposed in the Briefing or HL ✅

Stage complete: YES
→ User decision: ___
