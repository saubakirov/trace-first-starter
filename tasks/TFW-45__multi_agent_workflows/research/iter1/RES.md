# RES — TFW-45 iter1: Cross-Platform Capabilities Audit

> **Date**: 2026-06-15
> **Author**: Researcher (Antigravity)
> **Status**: 🔬 RES — Complete
> **Parent HL**: [HL-TFW-45](../../HL-TFW-45__multi_agent_workflows.md)
> **Mode**: Deep (2 OODA loops in Gather)

---

## Research Context

TFW-45 iteration 1 investigated cross-platform sub-agent spawn mechanics, system prompt hierarchies, and context inheritance across Antigravity, Claude Code, and Codex CLI. The user's #1 question: "Is invoking a slash command, skill, or workflow equivalent to a system prompt or not?" This research answered definitively: **no, on any platform.** Only rules-type files receive system-prompt-level enforcement. The research also mapped the complete instruction hierarchy per platform, identified 4 surviving configurations for swarm mode, and eliminated 5 configurations with structural reasons.

## Briefing

Reference: [1_briefing.md](1_briefing.md). Focus: H2–H7 (cross-platform capabilities). User direction: equal depth across all 3 platforms, system prompt question is #1 priority. Mode: deep.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | **Antigravity: custom sub-agent type for swarm mode (not `self`)** | `self` type inherits parent's system prompt — cannot inject custom Mindset as system_prompt. Custom type allows Mindset = TRUE system prompt. Sub-agent must explicitly load TFW context via `system_prompt` instruction to read files. User confirmed this preference |
| D2 | **Workflows and Skills ≠ system prompt on ANY platform** | Empirical (Antigravity: first-hand from own system prompt) + external (Claude Code, Codex docs). Workflows/Skills are file references loaded on demand. Only `.agent/rules/` (Antigravity), `CLAUDE.md` + `.claude/rules/` (Claude Code), and `AGENTS.md` (Codex) receive enforcement-level injection |
| D3 | **`swarm.md` is platform-agnostic protocol, not executable code** | swarm.md describes WHEN to spawn, WHAT Mindset each stage agent gets, WHAT context to load, HOW results flow. Platform-specific spawn syntax lives in adapter layer (`.agent/workflows/`, `.claude/agents/`, `.codex/agents/`). Stress-tested in Challenge C5 |
| D4 | **`.agent/rules/` is the ONLY user-controllable true system prompt in Antigravity** | Wrapped in `<user_rules><RULE[filename]>` with preamble: "MUST ALWAYS FOLLOW WITHOUT ANY EXCEPTION. Take precedence over any following instructions." This is the strongest enforcement language. All critical TFW identity content must go here |
| D5 | **AGENTS.md has different roles per platform** | Antigravity: placed in `.agent/rules/agents.md` = part of system prompt. Claude Code: fallback if no CLAUDE.md exists. Codex: primary/native instruction file. One file, three completely different injection mechanisms |
| D6 | **Claude Code sub-agents don't reliably inherit CLAUDE.md** | External research + community reports confirm unreliable inheritance. Sub-agent rules must be explicit in agent definition file (`.claude/agents/*.md`). This is a design constraint, not a bug |
| D7 | **4 surviving configurations for swarm mode** | C2 (Antigravity custom), C4 (Claude agent def), C7 (Codex TOML), C9 (single-agent fallback). 5 others eliminated with structural incompatibility evidence |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Does Mindset-as-system-prompt produce measurably better behavior than Mindset-as-conversation-context? | Deferred to iter2 (H1) | Structurally plausible (system prompt = identity level, can't be "forgotten") but no empirical test yet |
| Q2 | What are the token budget limits for `define_subagent.system_prompt`? | Deferred to iter2 | Estimated ~300-400 words needed (Mindset + TFW loading + stage instructions). Likely within budget but untested |
| Q3 | Can Claude Code `<system-reminder>` reliably replicate Mindset identity shift? | Deferred to iter2 (H8) | Functionally equivalent for TFW purposes (Challenge C3 verdict) but subtle priority conflicts possible with Anthropic's hidden system prompt |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H2 | `define_subagent` with custom `system_prompt` sufficient for Mindset + TFW context | needs-research | ✅ Confirmed | First-hand: `system_prompt` param is TRUE system prompt. Default read tools available. Agent can read TFW files as first action. Challenge C1 + C4 stress-tested |
| H3 | `self` type inherits `.agent/rules/` (TFW context auto-available) | needs-research | ✅ Confirmed but NOT recommended | `self` inherits full parent config including rules. BUT: incompatible with custom Mindset injection — `self` clones parent's system prompt, can't replace it. C1 eliminated |
| H4 | Workflows become system-level instructions when invoked | needs-research | ❌ Refuted | First-hand: workflows listed by description in `<workflows>` block. Agent reads them via `view_file` on demand. NOT system prompt content. Same for Skills |
| H5 | Antigravity changed since April 2026 — TFW-30 findings need correction | needs-research | ✅ Confirmed | Claude Code added Agent Teams (Feb 2026). Codex formalized agent definitions via TOML. Antigravity API stable but Skills/workflow ecosystem matured |
| H6 | Claude Code teamwork similar to Antigravity `define_subagent` — one swarm.md covers both | needs-research | 🔄 Refined | Similar concept (isolated sub-agents with custom prompts) but different injection mechanism (`<system-reminder>` vs true system prompt). swarm.md IS platform-agnostic as protocol, but adapters differ per platform |
| H7 | Codex has analogous spawn mechanism | needs-research | ✅ Confirmed | TOML agent definitions in `.codex/agents/` with `model_instructions_file`. AGENTS.md auto-inherited. Cleanest model of the three |

## HL Update Recommendations

| # | What to update | Source |
|---|---------------|--------|
| 1 | §10 H3: Mark as "Confirmed but NOT recommended for swarm" — `self` type conflicts with custom Mindset injection | D1, Challenge C1 elimination |
| 2 | §10 H4: Change to "Refuted — workflows are NOT system prompt, they're on-demand file reads" | D2, G1 first-hand evidence |
| 3 | §10 H6: Change to "Refined — similar concept, different injection. swarm.md is platform-agnostic protocol, adapters differ" | D3, Extract E2 |
| 4 | §3.2: Add constraint — TFW critical identity content MUST go in `.agent/rules/` (Antigravity), not workflows or skills | D4 |
| 5 | §3.2: Add platform comparison table showing instruction hierarchy per platform | Gather G6 |

## Fact Candidates

> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | architecture | Antigravity system prompt is assembled from 10 XML-tagged layers: `<identity>`, `<user_information>`, `<mcp_servers>`, `<user_rules>`, `<workflows>`, `<skills>`, `<plugins>`, `<subagents>`, `<planning_mode>`, `<guidelines>`. Only `<user_rules>` (from `.agent/rules/`) has enforcement language ("MUST ALWAYS FOLLOW WITHOUT ANY EXCEPTION") | Gather G6, first-hand | ★★★ |
| FC2 | architecture | Claude Code injects CLAUDE.md and .claude/rules/ as `<system-reminder>` XML tags within conversation history, NOT as API-level `system` role message. This is "high-priority context" but technically not system prompt. Anthropic's actual system prompt is fixed and hidden (for prompt caching optimization) | Gather G6, external research | ★★☆ |
| FC3 | architecture | AGENTS.md serves fundamentally different roles: Antigravity = placed in `.agent/rules/` = part of system prompt; Claude Code = fallback if no CLAUDE.md; Codex = primary native instruction file. Same filename, three injection mechanisms | Gather G6, D5 | ★★★ |
| FC4 | architecture | Antigravity `define_subagent` custom type sub-agents have default read tools (view_file, grep_search, list_dir, search_web) without explicit configuration. Write tools, MCP, and sub-sub-agents require explicit opt-in | Challenge C4, first-hand (tool documentation) | ★★☆ |
| FC5 | process | Claude Code sub-agents (`.claude/agents/*.md`) do NOT reliably inherit project CLAUDE.md or `.claude/rules/`. Multiple community reports + GitHub issues document this. Sub-agent rules must be explicit in agent definition file | Gather G2, G6, D6 | ★★☆ |

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS1 | architecture | The system prompt hierarchy across platforms reveals a consistent pattern: platform vendors keep their TRUE system prompt hidden/fixed, and provide a "user instruction layer" that is authoritative but technically sits below. Only Antigravity's `define_subagent.system_prompt` gives users TRUE system-prompt-level control for sub-agents. Claude and Codex both use high-priority-context workarounds. This makes Antigravity the strongest platform for Mindset-as-identity injection | G6 cross-platform comparison | ★★☆ |
| SS2 | strategy | The adapter layer architecture (swarm.md = protocol, adapters = platform-specific) naturally maps to TFW's existing 3-tier structure: `.tfw/` (core) → `.agent/` or `.claude/` or `.codex/` (adapter) → project files. swarm.md belongs in `.tfw/workflows/research/`, not in the adapter layer | Extract E5, Challenge C5 | ★★★ |

## Findings Map

```
    ┌─────────────────────────────────────────────────┐
    │         SYSTEM PROMPT HIERARCHY                  │
    │         (per platform)                           │
    └───────┬──────────┬──────────┬───────────────────┘
            │          │          │
    ┌───────▼──┐ ┌─────▼────┐ ┌──▼──────────┐
    │ANTIGRAV  │ │CLAUDE    │ │CODEX        │
    │          │ │CODE      │ │             │
    │rules/=SP │ │CLAUDE.md │ │AGENTS.md    │
    │wflow≠SP  │ │=reminder │ │=system ctx  │
    │skill≠SP  │ │rules/    │ │TOML agents  │
    │          │ │=reminder │ │             │
    │sub-agent:│ │          │ │sub-agent:   │
    │TRUE SP   │ │sub-agent:│ │instructions │
    │(custom)  │ │agent .md │ │file = SP    │
    └────┬─────┘ └────┬─────┘ └──────┬──────┘
         │            │              │
         └────────────┼──────────────┘
                      │
    ┌─────────────────▼──────────────────┐
    │         swarm.md (protocol)         │
    │  • WHEN to spawn                   │
    │  • WHAT Mindset per stage          │
    │  • WHAT context to load            │
    │  • HOW results flow                │
    │  (platform-agnostic)               │
    └─────────────────┬──────────────────┘
                      │
    ┌────────┬────────┼────────┬─────────┐
    │        │        │        │         │
    ▼        ▼        ▼        ▼         ▼
   C2       C4       C7       C9
  Antigrav  Claude   Codex    Fallback
  custom    agent/   TOML     single
  type+SP   .md      +instr   agent
```

## Iteration Status

- **Iteration:** 1 of 2 (min) / 4 (max)
- **Hypotheses tested:** H2 (✅), H3 (✅ not recommended), H4 (❌ refuted), H5 (✅), H6 (🔄 refined), H7 (✅)
- **Hypotheses deferred:** H1, H8, H9 (iter2 scope per iterations.yaml)
- **Gaps discovered:** Token budget for system_prompt untested; H1 empirical validation needed
- **Superseded decisions:** None

### Open Threads (for iter2)

1. **H1 empirical test:** Does fresh agent with Mindset-as-system-prompt produce measurably better output than single-agent mindset switch? This is the foundational hypothesis — everything else is implementation detail.
2. **H8 mode file vs execution_model:** Should swarm be a mode file (`swarm.md`) or an abstraction layer (`execution_model` in project_config.yaml)?
3. **H9 honesty vs context loss:** Fresh agent = honest identity but loses conversation history. What's the trade-off boundary?
4. **Token budget measurement:** How many tokens can `define_subagent.system_prompt` accept before degradation?

### Recommendation
- [x] **SUFFICIENT for iter1** — cross-platform capabilities mapped, surviving configurations identified
- [ ] **MORE NEEDED** — iter2 required per iterations.yaml (H1, H8, H9 unresolved)
- [ ] **BLOCKED** — N/A

> Iter1 delivered what it promised: capabilities audit across 3 platforms. The 4 surviving configurations (C2/C4/C7/C9) provide a solid foundation for iter2's design validation. The H4 refutation (workflows ≠ system prompt) and the AGENTS.md role asymmetry (D5) are material discoveries that should update HL before iter2 begins.

## Conclusion

This research determined the exact system prompt hierarchy across Antigravity, Claude Code, and Codex CLI through a combination of first-hand observation (Antigravity — reading own system prompt structure) and external research (Claude Code, Codex). The key finding: **on no platform does workflow, skill, or slash-command invocation equal system prompt.** Only rules-type files (`.agent/rules/` in Antigravity, `CLAUDE.md` + `.claude/rules/` in Claude Code, `AGENTS.md` in Codex) receive enforcement-level priority. For sub-agents, Antigravity's `define_subagent.system_prompt` provides TRUE system prompt — the strongest available mechanism. Claude Code uses `<system-reminder>` tags (functionally equivalent but technically not system prompt), while Codex uses TOML definitions with instruction files. The `self` sub-agent type was eliminated for swarm mode because it clones parent's system prompt and cannot accept custom Mindset injection. The research produced 4 surviving configurations and confirmed that `swarm.md` can be platform-agnostic (protocol-level), with platform-specific adapters handling spawn syntax. Without this research, the implementation would have likely assumed workflows = system prompt (wrong), used `self` type for sub-agents (incompatible with Mindset injection), and designed platform-specific swarm files instead of a single protocol + adapters.

---

*RES — TFW-45 iter1: Cross-Platform Capabilities Audit | 2026-06-15*
