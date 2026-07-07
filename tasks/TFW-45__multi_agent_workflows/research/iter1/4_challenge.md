# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW-45](../../HL-TFW-45__multi_agent_workflows.md)
> Goal: Stress-test surviving configurations for swarm mode and expose failure modes before TS.

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D1: Antigravity | `self` type | D2: Custom system_prompt | Mindset as identity | `self` inherits PARENT's system prompt. You can't inject custom Mindset as system_prompt AND use `self` type. `system_prompt` param in `define_subagent` is for custom types only — `self` ignores it and clones parent's prompt |
| D1: Claude Code | Subagent | D3: Automatic CLAUDE.md inheritance | Reliable | Claude sub-agents DON'T reliably inherit project CLAUDE.md. Counting on automatic inheritance = fragile |
| D1: ANY | No sub-agents (C9) | D2: Sub-agent system_prompt | Any injection model | C9 is single-agent fallback — no sub-agents means no injection mechanism needed. Not incompatible, just different mode |
| D1: Claude Code | Agent Teams (C5) | Sequential stages | Strict order | Agent Teams are designed for parallel work. Using them for strictly sequential research stages wastes 3-7x tokens for no benefit |

**Surviving configurations** (after removing incompatible rows):

| Config | Platform | Sub-agent instruction | Context inheritance | Notes |
|--------|---------|----------------------|---------------------|-------|
| C2 ✅ | Antigravity | `define_subagent` custom type, Mindset as `system_prompt` | Explicit — must inject TFW context loading in system_prompt | **User-preferred for Antigravity.** Cleanest Mindset isolation. Must include "read AGENTS.md + conventions.md" in system_prompt |
| C4 ✅ | Claude Code | `.claude/agents/stage_name.md` definition | Explicit — all rules in agent definition file | Equivalent to C2 for Claude. Agent file = stage Mindset + TFW rules |
| C7 ✅ | Codex | TOML + `model_instructions_file` | AGENTS.md auto-inherited + custom instructions | Cleanest: TFW rules come free via AGENTS.md, Mindset via instruction file |
| C9 ✅ | ANY | None (single agent, `focused`/`deep` mode) | Full context (same conversation) | **Fallback.** Must remain working. Backward-compatible |

**Eliminated configurations:**

| Config | Reason |
|--------|--------|
| C1 | `self` type with custom Mindset — incompatible. `self` clones parent, no custom system_prompt |
| C3 | `self` type + Mindset as task prompt — weaker than C2. Mindset is task instruction, not identity. User chose custom type |
| C5 | Agent Teams for sequential stages — overkill, 3-7x cost, designed for parallel work |
| C6 | `<system-reminder>` via CLAUDE.md for sub-agents — unreliable inheritance |
| C8 | Codex direct task prompt without custom instructions — no Mindset isolation |

**Unexpected survivors:**
- None. All survivors were among the initially favored options. The filtering was clean — incompatibilities were structural, not edge-case.

## Findings

### C1: Can custom type sub-agent actually load TFW context on its own?

**Attack:** C2 (Antigravity custom type) requires the sub-agent to read TFW context files as its first action. But what if the agent doesn't follow that instruction?

**Defense:** The `system_prompt` parameter is TRUE system prompt with "MUST ALWAYS FOLLOW" enforcement. If the system_prompt says "Your first action: read `.tfw/conventions.md`" — this has the same weight as `.agent/rules/`. The agent has `view_file` tool available.

**Counter-attack:** But the sub-agent starts with a CLEAN context. It has no `.agent/rules/` content (those are parent-only for custom types). The only instructions it has are what's in `system_prompt`. If the `system_prompt` is too short or vague, TFW compliance degrades.

**Resolution:** The `system_prompt` for custom sub-agents must be carefully composed:
1. Mindset block (identity, behavioral directive) — ~100-150 words
2. TFW context loading instructions (explicit file list to read first) — ~50-100 words
3. Stage-specific instructions (what to produce, format, stop conditions) — ~100-150 words

Total: ~300-400 words. Within token budget. **Risk is manageable if the system_prompt template is well-designed.**

### C2: Does Mindset-as-system-prompt actually change behavior vs Mindset-as-conversation-context?

**Attack:** User hypothesis H1: "A new agent with clean chat and system prompt will work better and more honestly than one agent serially trying to switch mindsets." But we have NO empirical evidence for this. Maybe system_prompt Mindset and conversation-context Mindset produce identical behavior.

**Defense:** There IS a structural difference:
- System prompt = processed before any conversation, shapes ALL subsequent responses. Cannot be "forgotten" via context rotation
- Conversation context = competes with other messages, can be pushed out by long conversations, model may "drift" away from it

**Counter-counter:** For SHORT tasks (1-2 OODA loops per stage in deep mode), context drift is unlikely. The benefit of system_prompt identity may only manifest in longer conversations.

**Verdict:** H1 is plausible but **unproven**. This is explicitly deferred to iter2. For TFW-45 design, we proceed with system_prompt because:
- It's structurally cleaner (system prompt IS identity)
- It aligns with platform intent (that's what `define_subagent.system_prompt` is FOR)
- Even if benefit is marginal, it has no downside — we're not losing anything

### C3: Claude Code — can `.claude/agents/` reliably replicate the Antigravity model?

**Attack:** C4 assumes `.claude/agents/stage_name.md` works like `define_subagent.system_prompt`. But the injection mechanism is different — Claude uses `<system-reminder>`, not true `system` role.

**Defense:** The functional equivalence is sufficient. What matters for TFW:
- Does the agent follow Mindset behavioral directive? → Yes, `<system-reminder>` is "highly authoritative"
- Does the agent have TFW context? → Yes, if included in agent definition file
- Is the context isolated (fresh agent)? → Yes, sub-agents get own context window

**Counter:** The subtle difference: if the model hits a conflict between its hidden system prompt (Anthropic's) and the `<system-reminder>` Mindset, the hidden prompt wins. Example: Mindset says "Be a Critic, challenge everything" but Anthropic's hidden prompt may have "Be helpful and constructive." In practice, this is unlikely to cause issues for research stage Mindsets, but could matter for adversarial stages.

**Verdict:** C4 works. The `<system-reminder>` mechanism is "good enough" for Mindset injection. Not identical to Antigravity's true system prompt, but functionally equivalent for TFW's purposes.

### C4: What if the sub-agent can't read project files?

**Attack:** C2 depends on the sub-agent reading `.tfw/conventions.md`, `AGENTS.md`, etc. But what tools does a custom sub-agent have?

**Defense (Antigravity):** `define_subagent` has explicit tool toggle parameters:
- `enable_write_tools` — file creation, editing, commands
- `enable_mcp_tools` — MCP server access
- `enable_subagent_tools` — sub-sub-agents

By default (from docs): "all subagents have read tools to research the codebase, searching the web, and reading files, and tools to communicate with other agents."

**Verdict:** ✅ Sub-agents CAN read files by default. No tool access issue. The `system_prompt` instruction to "read conventions.md" will work.

### C5: Cross-platform protocol — can one `swarm.md` file work?

**Attack:** Each platform has different spawn syntax. One `swarm.md` can't contain `define_subagent` calls AND `.claude/agents/` instructions AND `.codex/agents/` TOML configs.

**Defense:** `swarm.md` is a MODE FILE (per HL) — it doesn't contain spawn commands. It contains:
1. WHEN to switch from single-agent to swarm
2. What Mindset each stage agent gets
3. What context each stage agent must load
4. How results flow between stages

The actual spawn SYNTAX is platform-specific and lives in the adapter layer (`.agent/workflows/`, `.claude/agents/`, `.codex/agents/`).

**Verdict:** ✅ `swarm.md` IS platform-agnostic. It's a protocol description, not executable code. Platform adapters translate it into platform-specific spawn commands. This architecture was correctly anticipated in the HL.

### C6: Single-agent backward compatibility (C9)

**Attack:** If `swarm.md` changes how `base.md` works, existing single-agent mode might break.

**Defense:** The HL explicitly states: "swarm.md must be a thin mode file." `base.md` remains unchanged. The mode file only adds spawn capability. When mode = `focused` or `deep` (no swarm), the old behavior persists.

**Verification:** Current `.tfw/project_config.yaml` has `default_mode: focused`. Nothing changes until a user explicitly selects `swarm` mode or the research workflow selects it via criteria in `swarm.md`.

**Verdict:** ✅ C9 (single-agent fallback) is safe. No breaking change.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| 4 surviving configurations (C2, C4, C7, C9) | System_prompt template design (TS scope) |
| 5 eliminated with structural reasons | H1 empirical test (iter2) |
| Custom type sub-agent CAN read files (default read tools) | Token budget measurement (iter2) |
| `swarm.md` IS platform-agnostic (protocol, not code) | Platform adapter specifics (TS scope) |
| Single-agent backward compatibility confirmed | |
| `<system-reminder>` sufficient for Claude Mindset injection | |

**Sufficiency (deep mode):**
- [x] External source used? (Building on 12 web searches + first-hand system prompt observation)
- [x] Briefing gap closed? (All 6 hypotheses tested, configurations stress-tested)
- [x] Pairwise incompatibility checked? Surviving configurations listed? (4 incompatible pairs → 5 eliminated → 4 survivors)
- [x] Hypothesis tested? (H2 ✅ confirmed, H3 ✅ with C2>C1, H4 ❌ refuted, H5 ✅, H6 ✅ functional equiv, H7 ✅)
- [x] Counter-evidence sought? (6 stress tests with attacks + defenses + verdicts)
- [x] Metacognitive check: Challenge produced refinements (C1/C3 eliminated based on structural incompatibility, not preference) ✅

Stage complete: YES
→ User decision: ___
