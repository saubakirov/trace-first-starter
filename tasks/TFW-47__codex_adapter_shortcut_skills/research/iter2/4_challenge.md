# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW-47](../../HL-TFW-47__codex_adapter_shortcut_skills.md)
> Goal: Codex becomes a first-class TFW adapter with dedicated shortcut skills.

## Consistency Check

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| Skill Directory | `.codex/skills/` (C4) | Sync Strategy | any | Legacy path — community moved to `.agents/skills/`, breaks cross-tool portability |
| Skill Content | Generated (C2) | Instruction Loading | On-demand | Generated template misses 6/11 workflow-specific contract clauses (E1) — agent won't enforce iterations.yaml, scope guard, verify-claims rules |
| Skill Content | None / AGENTS.md only (C6) | Invocation Docs | `$tfw-*` | No skill folders = no `$` menu entries. Contradicts invocation documentation claim |
| Instruction Loading | AGENTS.md embed (C3) | Instruction Budget | 32 KiB | conventions.md alone is 27 KB. AGENTS.md + conventions + glossary exceeds cap. Silent truncation |

**Eliminated:**
- **C2** (generated from template): Template structurally insufficient for 6/11 skills. AFD empirically proved this by abandoning the approach.
- **C3** (AGENTS.md embeds context): Hits 32 KiB cap. On-demand loading is strictly better.
- **C4** (`.codex/skills/`): Legacy directory. No cross-tool benefit.
- **C6** (AGENTS.md routing only): No UI affordance. Confirmed by H4.

**Surviving configurations:**

| Config | Skill Directory | Skill Content | Instruction Loading | Sync Strategy | Invocation Docs |
|--------|----------------|---------------|---------------------|---------------|-----------------|
| C1 | `.agents/skills/` | Handwritten per-workflow | On-demand via contract | tfw-init copies from adapters/ | `$tfw-*` primary, `/` as alias |
| C5 | `.agents/skills/` | Hybrid: template + overrides | On-demand via contract | tfw-init copies, tfw-update diffs | `$tfw-*` primary |

**Unexpected survivors:** None — C1 and C5 were the expected front-runners.

## Findings

### C1: C1 vs C5 — Is the Hybrid Worth the Complexity?

C5 proposes a base template with per-skill overrides. In practice, the AFD skills share a common structure:

```
---
name: tfw-{command}
description: Codex adapter for TFW {command} workflow. Use when...
---
# TFW {Command}
Use this skill as the Codex-native equivalent of `/tfw-{command}`.
## Contract
- Alias handling
- .tfw/ check
- Context loading order
- Open canonical workflow
- Role lock + permitted/forbidden artifacts
- Stop conditions
- Next skill recommendation
```

But the *content* of each bullet differs per workflow. The "template" is really a structural convention (same headings), not a generatable file. C5 collapses to C1 in practice: you write 11 files following the same heading convention, not a template + override mechanism.

**Verdict:** C5 adds complexity (override mechanism, diff logic in tfw-update) without reducing effort. C1 is simpler and proven.

### C2: Drift Risk for Handwritten Skills

If a workflow changes (e.g., research.md adds a new gate), the corresponding skill's contract may not be updated. This is the same drift risk that affects Claude Code commands and Antigravity workflow copies.

**Mitigation already exists:** `tfw-update` workflow re-copies adapter files. For Codex, `tfw-update` would re-copy `.tfw/adapters/codex/skills/tfw-*/SKILL.md` → `.agents/skills/tfw-*/SKILL.md`. Same pattern as Antigravity's `cp .tfw/workflows/*.md .agent/workflows/tfw-*.md`.

### C3: Can a New User Actually See and Use `$tfw-plan`?

**Path test:**
1. Clone repo with `.agents/skills/tfw-plan/SKILL.md` committed → ✅ Codex scans at session start
2. Type `$` → skill menu shows `tfw-plan` → ✅ frontmatter `name` field controls this
3. Type `$tfw-plan TFW-50` → skill body loads, agent reads plan.md → ✅ on-demand loading
4. Type `/tfw-plan` in message → agent matches via description field → ✅ soft alias works

**Failure mode:** If `.agents/skills/` is in `.gitignore` → skills not committed → new clone has nothing. Must document: commit skill folders to repo.

### C4: Adapter Location — `.tfw/adapters/codex/` vs `.agents/skills/` Directly

The AFD project has BOTH:
- Templates/README in `.tfw/adapters/codex/` (framework-owned, version-controlled with TFW)
- Installed skills in `.agents/skills/tfw-*/` (project-level, where Codex discovers them)

This is the same pattern as:
- Claude Code: templates in `.tfw/adapters/claude-code/` → installed in `.claude/commands/`
- Antigravity: templates in `.tfw/adapters/antigravity/` → installed in `.agent/workflows/`

The two-location pattern is consistent and correct. `.tfw/adapters/codex/` = source. `.agents/skills/` = installed copy.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C1 is the clear winner — handwritten, `.agents/skills/`, on-demand loading | None |
| C5 collapses to C1 in practice | None |
| Drift mitigated by tfw-update re-copy | None |
| New user path validated end-to-end | None |

**Sufficiency:**
- [x] External source used (Codex skill discovery mechanics, `.agents/` standard)
- [x] Briefing gap closed
- [x] Pairwise incompatibility checked, surviving configurations listed

Stage complete: YES
