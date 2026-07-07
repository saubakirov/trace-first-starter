# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW-45](../../HL-TFW-45__multi_agent_workflows.md)
> Goal: Determine cross-platform spawn mechanics and whether workflow/skill/slash-command invocation = system prompt.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1: Platform | Antigravity | Claude Code | Codex CLI | |
| D2: Instruction injection model | True system prompt | `<system-reminder>` tag (high-priority context) | User-turn context injection | TOML/YAML config → system prompt |
| D3: Sub-agent context inheritance | Full parent clone (`self`) | Isolated with explicit injection | Partial (global rules inherited, conversation not) | No sub-agents |
| D4: Workflow/Skill invocation semantics | System prompt (identity-level) | Conversation context (high-authority) | On-demand lazy load (progressive disclosure) | N/A for platform |
| D5: Cross-agent communication | send_message (direct) | Peer-to-peer mailbox + shared files | Orchestrator-only (hierarchical) | File-based coordination |

## Findings

### G1: Antigravity — Primary source (self-observation + web research)

**Sub-agent mechanics (first-hand — verified from own system prompt):**
- `define_subagent`: takes `name`, `description`, `system_prompt`, optional `enable_write_tools`, `enable_mcp_tools`, `enable_subagent_tools`
- `system_prompt` parameter: described as "A detailed system prompt for this subagent" — this IS the sub-agent's system-level instruction
- `self` type: documented as "Subagent that inherits the parent agent's full configuration including tools, system prompt, and model"
- `research` type: documented as "Research subagent with read-only tools for exploring the codebase, searching the web, and reading files"
- Communication: `send_message` tool for inter-agent messaging. System auto-notifies when sub-agent responds (no polling needed)
- Workspace modes: `inherit` (same workspace), `branch` (isolated clone), `share` (shared directory)

**Rules and Workflows (first-hand — verified from own system prompt):**
- `.agent/rules/` files appear in `<user_rules>` section of system prompt — they ARE system prompt content
- `.agent/workflows/` files are listed under `<workflows>` section: "If a workflow looks relevant, or the user explicitly uses a slash command like /slash-command to invoke a workflow, then view the workflow file"
- Critical distinction: **Rules = system prompt. Workflows = NOT system prompt.** Workflows are listed by description, agent reads the file on invocation via `view_file` tool
- Skills: appear under `<skills>` section: "If a skill seems relevant... you MUST use the `view_file` tool on the SKILL.md file to read its full instructions"

**Implication for H2 (system_prompt injection):** ✅ CONFIRMED — `define_subagent.system_prompt` is a genuine system-level prompt for the sub-agent. It defines the sub-agent's identity.

**Implication for H3 (self type inherits rules):** ✅ CONFIRMED with caveat — `self` inherits "parent agent's full configuration including tools, system prompt, and model." This means `.agent/rules/` (which are part of system prompt) ARE inherited. But `.agent/workflows/` (which are NOT system prompt, just a listing) would also be inherited as a list.

**Implication for H4 (workflows = system prompt?):** ❌ REFUTED — Workflows are NOT system prompt. They are file references loaded on demand. The agent reads them via `view_file`. Rules ARE system prompt. This is a critical distinction.

### G2: Claude Code — External research (web sources)

**CLAUDE.md injection mechanics:**
- CLAUDE.md is NOT injected into the actual system prompt. The system prompt is static/shared across all users (for prompt caching optimization)
- Instead, CLAUDE.md content is injected as `<system-reminder>` XML tags within the conversation history
- This is "high-priority context" — the model treats it as highly authoritative, effectively overriding defaults
- BUT it's not technically system prompt — it's a specially-tagged user-turn message

**Skill loading (progressive disclosure):**
- Level 1: YAML frontmatter (name, description) → always loaded into agent awareness
- Level 2: Full SKILL.md body → loaded into conversation context ONLY when triggered/invoked
- Level 3: Supporting files → loaded only when agent explicitly reads them
- Skills extend the CURRENT agent's context. NOT system prompt.

**Sub-agents:**
- Subagents run in isolated context windows with their own prompts
- `.claude/agents/` directory contains agent definitions (YAML frontmatter + markdown body)
- Subagents do NOT automatically inherit project CLAUDE.md — this is unreliable
- AGENTS.md may be more reliably inherited than CLAUDE.md for subagents
- Skills must be explicitly assigned to subagents; they don't auto-inherit

**Agent Teams (v2.1.32+, Feb 2026):**
- Peer-to-peer communication (not just hierarchical)
- Shared task lists (tasks.md/TODO.md) as coordination layer
- Each agent maintains own 1M token context window
- Git-based locking for file conflict prevention
- 3-7x token cost vs single session

**Implication for H6 (Claude Code similar model):** PARTIALLY — both have sub-agent spawn, both support custom prompts. But injection mechanics differ fundamentally: Antigravity uses true `system_prompt` parameter, Claude Code uses `<system-reminder>` tags and agent definition files. NOT the same model — one swarm.md protocol will need platform-aware branches.

### G3: Codex CLI — External research (web sources)

**Agent configuration:**
- Custom agents defined via TOML files in `~/.codex/agents/` or `.codex/agents/`
- Each agent gets: model config, instructions, sandbox permissions
- `AGENTS.md` file (note: same name as TFW!) read from home dir and project root
- `config.toml` supports `model_instructions_file` key to point to custom system prompt file
- `AGENTS.override.md` can replace (not append) instructions at any level

**Sub-agent spawn:**
- Orchestrator-worker pattern: main agent delegates bounded tasks to sub-agents
- Sub-agents operate in isolated context windows
- Global guidance (AGENTS.md, sandbox policies) inherited by default
- Specialized system prompt overrides general inheritance at spawn time
- Directory tree walking: Codex reads AGENTS.md from root down to working dir

**Instruction hierarchy:**
- Global → Project → Working Dir (layered, not replaced)
- User chat prompts > config files > inherited rules
- Sub-agent definition file = primary override for role-specific behavior

**Implication for H7 (Codex spawn mechanism):** ✅ EXISTS — Codex has sub-agent spawn. Custom TOML agent definitions with system prompt + tool permissions. Similar enough that one swarm protocol could cover it with platform-specific spawn syntax.

### G4: Critical comparison — System prompt question (user's #1 concern)

| Platform | "Rules" files | "Workflow" files | "Skill" files | Sub-agent system prompt |
|----------|--------------|------------------|---------------|------------------------|
| **Antigravity** | `.agent/rules/` → **TRUE system prompt** (in `<user_rules>` block) | `.agent/workflows/` → **NOT system prompt** (file reference, read on demand via `view_file`) | `.agent/skills/` → **NOT system prompt** (description always available, body read on demand) | `define_subagent.system_prompt` → **TRUE system prompt** for the sub-agent |
| **Claude Code** | `.claude/rules/` → **`<system-reminder>` tag** (high-priority context, NOT true system prompt) | N/A (not the same concept) | `.claude/skills/` → **conversation context** when triggered (NOT system prompt) | Agent definition file body → **injected as agent instructions** (mechanism varies) |
| **Codex** | `AGENTS.md` → **layered context** (global + project + dir) | N/A (not the same concept) | `SKILL.md` → **loaded on demand** | TOML definition + `model_instructions_file` → **system prompt** |

**Key insight:** NONE of the three platforms make workflow/skill invocation equal to system prompt in the strict sense. Only rules-type files get system-prompt-level treatment. Skills and workflows are HIGH-PRIORITY CONTEXT but not system prompt.

EXCEPT: Antigravity's `define_subagent.system_prompt` IS true system prompt. And `self` type inherits the parent's full system prompt (including rules).

### G5: What changed since TFW-30 (April 2026) — H5

| Area | April 2026 (TFW-30) | June 2026 (current) |
|------|---------------------|---------------------|
| Sub-agents | `define_subagent` existed | Same API, still works |
| `self` type | Existed | Still exists, documented identically |
| Skills | Not used in project | Still not used — but system supports them via `<skills>` section |
| Workflows | Full-copy pattern (12 files) | Still full-copy — this needs fixing |
| Claude Code | Subagents existed | Agent Teams added (v2.1.32, Feb 2026) — peer-to-peer, not just hierarchical |
| Codex | Limited agent support | Formalized custom agent definitions via TOML, AGENTS.md layering |

**Implication for H5:** ✅ CONFIRMED — landscape has changed. Biggest change: Claude Code now has Agent Teams (peer-to-peer). Codex has formalized agent definitions. Antigravity API appears stable but the ecosystem (best practices, Skills guidance) has matured.

### G6: DEEP DIVE — System prompt hierarchy per platform (OODA loop 2)

#### Antigravity — What exactly IS the system prompt?

**Empirical evidence (first-hand, from own system prompt structure):**

The system prompt for an Antigravity agent is assembled from these layers, in this order:

| Layer | Source | XML tag in system prompt | Evidence |
|-------|--------|------------------------|----------|
| 1. Core identity | Antigravity platform | `<identity>` | I see: "You are Antigravity, a powerful agentic AI coding assistant..." |
| 2. User information | Platform metadata | `<user_information>` | OS, workspace URIs, corpus names |
| 3. MCP servers | Platform config | `<mcp_servers>` | Server names, tools, schema paths |
| 4. **User rules** | **`.agent/rules/`** files | **`<user_rules>`** → `<RULE[filename]>` | Each rules file wrapped in `<RULE[agents.md]>` and `<RULE[tfw.md]>` tags. **This IS system prompt — highest user-controllable priority** |
| 5. Workflows | `.agent/workflows/` | `<workflows>` | Listed by description ONLY. "If a workflow looks relevant... view the workflow file." **NOT system prompt content — just a directory listing** |
| 6. Skills | `.agent/skills/` or plugins | `<skills>` | Listed by name + description. "you MUST use the view_file tool on the SKILL.md file to read its full instructions." **NOT system prompt content** |
| 7. Plugins | Plugin config | `<plugins>` | Plugin metadata + skill references |
| 8. Subagents | Defined in session | `<subagents>` | Available subagent types + descriptions |
| 9. Planning mode | Platform config | `<planning_mode>` | Planning mode instructions |
| 10. Guidelines | Platform config | `<guidelines>` | Behavioral guidelines |

**Key conclusion for Antigravity:**
- `.agent/rules/*.md` → **TRUE system prompt** (in `<user_rules>`, takes precedence over all other instructions)
- `.agent/workflows/*.md` → **NOT system prompt** (listed by filename + description, read on demand)
- `.agent/skills/` → **NOT system prompt** (listed by name + description, read on demand)
- `define_subagent.system_prompt` → creates **TRUE system prompt** for the sub-agent

**What `.agent/rules/` preamble says:**
> "The following are user-defined rules that you MUST ALWAYS FOLLOW WITHOUT ANY EXCEPTION. These rules take precedence over any following instructions."

This is the strongest enforcement language possible. Rules files are the **only** user-controllable content that gets this treatment.

#### Claude Code — What exactly IS the system prompt?

**Architecture (from external research):**

| Layer | Source | Injection mechanism | Priority |
|-------|--------|-------------------|----------|
| 1. Anthropic system prompt | Fixed/hidden | True `system` role message | Highest (immutable) |
| 2. Managed settings | Enterprise admin | `managed-settings.json` | High (overrides user) |
| 3. User global | `~/.claude/CLAUDE.md` | `<system-reminder>` tag in conversation | User-level |
| 4. **Project rules** | **`CLAUDE.md` (project root)** | **`<system-reminder>` tag in conversation** | **Project-level — primary user interface** |
| 5. **Rules directory** | **`.claude/rules/*.md`** | **Same as CLAUDE.md** (path-scoped possible) | **Same priority as CLAUDE.md** |
| 6. Subdirectory CLAUDE.md | `src/CLAUDE.md` etc. | `<system-reminder>`, loaded when accessing files in that subdir | Scoped |
| 7. AGENTS.md | Fallback if no CLAUDE.md | Same as CLAUDE.md | **Fallback only** — recognized automatically, but CLAUDE.md takes priority |

**Critical nuance:** Claude Code's "system prompt" (layer 1) is Anthropic's fixed code. User instructions (CLAUDE.md, .claude/rules/) are injected as `<system-reminder>` tags inside the conversation. This is NOT the API-level `system` message — it's a high-priority context injection pattern. The model treats it as authoritative, but it's technically conversation context, not system prompt.

**AGENTS.md in Claude Code:**
- Claude Code recognizes `AGENTS.md` as a **fallback** if no `CLAUDE.md` exists
- If CLAUDE.md exists, it takes priority
- Best practice: `CLAUDE.md` can reference AGENTS.md via `@AGENTS.md` import syntax
- AGENTS.md is **not a Claude-native concept** — it's a cross-tool standard that Claude adopted as fallback

**For sub-agents:**
- Sub-agents configured via `.claude/agents/*.md` files (YAML frontmatter + markdown body)
- Sub-agent's own `.md` file IS its instruction set
- Sub-agents do **NOT reliably inherit** parent's CLAUDE.md or .claude/rules/
- If sub-agent needs rules → must be explicit in the agent definition file

#### Codex CLI — What exactly IS the system prompt?

**Architecture (from external research):**

| Layer | Source | Injection mechanism | Priority |
|-------|--------|-------------------|----------|
| 1. OpenAI base prompt | Fixed/hidden | `system` role message | Highest (immutable) |
| 2. Global AGENTS.md | `~/.codex/AGENTS.md` | Appended to system context | Global user-level |
| 3. **Project AGENTS.md** | **Root `AGENTS.md`** | **Layered (concatenated) into system context** | **Project-level** |
| 4. Subdirectory AGENTS.md | Walking down directory tree | Layered (deeper = later = higher effective priority) | Scoped |
| 5. AGENTS.override.md | Any level | **Replaces** (not appends) parent AGENTS.md at that level | Override |
| 6. config.toml | `.codex/config.toml` | `model_instructions_file` key → custom system prompt file | Can replace default instructions entirely |

**AGENTS.md IS the primary instruction mechanism in Codex.** Unlike Claude (where it's a fallback), in Codex AGENTS.md is the native, expected file.

**For sub-agents:**
- Custom agents defined via TOML files in `.codex/agents/`
- Each gets its own `model_instructions_file` → true system prompt
- Global AGENTS.md still inherited by sub-agents
- Specialized instructions in agent definition override general inheritance

#### G6 Summary — The definitive comparison

| What | Antigravity | Claude Code | Codex CLI |
|------|------------|-------------|-----------|
| **True system prompt (platform)** | `<identity>` block (fixed) | Anthropic hidden prompt (fixed) | OpenAI base prompt (fixed) |
| **Primary user instruction file** | `.agent/rules/*.md` → `<user_rules>` | `CLAUDE.md` → `<system-reminder>` | `AGENTS.md` → system context |
| **Rules directory** | `.agent/rules/` (**true system prompt**) | `.claude/rules/` (same as CLAUDE.md) | N/A (AGENTS.md IS the rules) |
| **AGENTS.md role** | `.agent/rules/agents.md` (**part of system prompt** — our adapter puts it there) | **Fallback** if no CLAUDE.md | **Primary** instruction file |
| **Injection mechanism** | XML `<user_rules><RULE[file]>` | XML `<system-reminder>` in conversation | Concatenated system context |
| **Enforcement language** | "MUST ALWAYS FOLLOW WITHOUT ANY EXCEPTION. Take precedence over any following instructions" | "High-priority context" | "System/developer level (highest privilege)" |
| **Workflow invocation** | `view_file` on demand (**NOT** system prompt) | N/A (different concept) | N/A |
| **Skill invocation** | `view_file` on demand (**NOT** system prompt) | Injected into conversation when triggered | Loaded on demand |
| **Sub-agent instruction** | `define_subagent.system_prompt` (**true** system prompt) | Agent definition `.md` file (own prompt) | TOML definition + `model_instructions_file` |
| **Sub-agent inherits rules?** | `self` type: YES. Custom: only what's in `system_prompt` param | **Unreliable** — must be explicit | Global AGENTS.md: yes. Project: configurable |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Complete system prompt hierarchy for all 3 platforms | Empirical test of sub-agent behavior (iter2) |
| `.agent/rules/` = TRUE system prompt in Antigravity | Whether Mindset in `define_subagent.system_prompt` shifts behavior |
| `CLAUDE.md` = `<system-reminder>` tag, NOT true system prompt | Token budget limits for system_prompt per platform |
| `AGENTS.md` = fallback in Claude, primary in Codex | |
| Workflows/Skills = NOT system prompt on ANY platform | |
| Claude Code sub-agents don't reliably inherit CLAUDE.md | |
| 5 dimensions with ≥3 alternatives each | |

**Sufficiency (OODA loop 2 — deep mode):**
- [x] External source used? (12 web searches across 3 platforms, 2 OODA loops)
- [x] Briefing gap closed? (System prompt hierarchy mapped per platform with evidence)
- [x] Dimensions identified? (5 dimensions: Platform, Injection model, Inheritance, Invocation semantics, Communication)
- [x] Hypothesis tested? (H2 ✅, H3 ✅ with caveat, H4 ❌ refuted, H5 ✅, H6 partial, H7 ✅)
- [x] Counter-evidence sought? (CLAUDE.md ≠ true system prompt; Claude sub-agent inheritance unreliable; AGENTS.md has different roles per platform)
- [x] Metacognitive check: Discovered NEW facts — not just confirming assumptions

Stage complete: YES
→ User decision: ___

