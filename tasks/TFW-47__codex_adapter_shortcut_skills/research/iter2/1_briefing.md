# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW-47](../../HL-TFW-47__codex_adapter_shortcut_skills.md)
> Goal: Codex becomes a first-class TFW adapter with dedicated shortcut skills, matching adapter parity with Claude Code and Antigravity.
> **Parallel note:** Iter1 (evidence template design) runs in parallel. No predecessor RES dependency.

## Research Plan

**Gather (Explorer):**
- Research Codex CLI skill discovery mechanism: directory hierarchy (`~/.codex/skills/`, `.codex/skills/`, project-level), `SKILL.md` structure (YAML frontmatter fields), reload/refresh behavior
- Research Codex instruction loading chain: `AGENTS.md` cascade, instruction size limits (32 KiB cap), what gets auto-loaded vs on-demand
- Research Codex invocation syntax: `/tfw-plan` vs `$tfw-plan` vs natural language trigger — what actually creates a visible entry in Codex UI
- Examine existing Claude Code `.claude/commands/` patterns and Antigravity `.agent/workflows/` patterns as reference architectures
- Candidate dimensions: discovery mechanism, invocation syntax, instruction budget, generated vs handwritten, sync strategy

**Extract (Analyst):**
- Build configuration space: adapter structure options × invocation mechanism × instruction loading strategy × sync approach
- Cross-reference against TFW adapter principles (thin routers, no logic duplication, portable installation)

**Challenge (Critic):**
- Can a new Codex user actually see and use `tfw-plan` after setup? Test the full path.
- Does the 32 KiB cap block TFW conventions loading? If so, what's the workaround?
- Generated skill set vs handwritten: which is safer for maintenance?

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H3 | Dedicated Codex skill folders are required for separate visible entries in Codex UI | open |
| H4 | `AGENTS.md` routing is sufficient for behavior but insufficient for UI affordance | open |
| H5 | Generated shortcut-skill set is safer than maintaining 11 handwritten folders | open |
| H6 | `$tfw-plan` is the reliable invocation; `/tfw-plan` may only be user convention | open |
| H7 | Codex can load conventions.md on-demand via skill references instead of instruction chain | open |

## Scope Intent
- **In scope:** Codex skill discovery directories, `SKILL.md` format requirements, invocation syntax, 32 KiB instruction cap and workarounds, generated vs handwritten skill folders, adapter structure for `.tfw/adapters/codex/`, sync strategy for tfw-update.
- **Out of scope:** Evidence template design (iter1). Codex agent spawning/TOML agents (TFW-45 scope). Actual implementation of the adapter (HL Phase C). Cursor adapter changes.

## Guiding Questions
1. Have you tested any Codex skill invocation yourself (e.g., placed a SKILL.md and tried to trigger it)? Any observations?
2. Is there a preference for where Codex skills should live — project-level only, or also support `~/.codex/skills/` for global TFW skills?
3. Should the Codex adapter support `tfw-config`, `tfw-knowledge`, and `tfw-init` as separate skills, or only the core workflow set (plan, research, handoff, review, resume, docs)?

## User Direction

1. **Testing:** User has tested Codex skills in the AFD project (`D:\projects\research\ai-first-devices`). Full 11-skill setup exists in `.agents/skills/tfw-*/SKILL.md` with handwritten contracts. `.tfw/adapters/codex/` also exists with README + generic template.
2. **Location:** Project-level (`.agents/skills/`) — user doesn't know exact global mechanics but wants skills in the project repo.
3. **Scope:** Full workflow skill set — all 11 skills (plan, research, handoff, review, resume, docs, knowledge, config, init, release, update).

---
Stage complete: YES
