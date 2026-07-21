# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW-47](../../HL-TFW-47__codex_adapter_shortcut_skills.md)
> Goal: Codex becomes a first-class TFW adapter with dedicated shortcut skills.

## Configuration Space

Dimensions from Gather: (1) Skill Directory, (2) Skill Content Strategy, (3) Instruction Loading, (4) Sync Strategy, (5) Invocation Documentation.

| Config | Skill Directory | Skill Content | Instruction Loading | Sync Strategy | Invocation Docs |
|--------|----------------|---------------|---------------------|---------------|-----------------|
| C1 | `.agents/skills/` (project) | Handwritten per-workflow | On-demand via skill contract | tfw-init copies from `.tfw/adapters/codex/` | Document `$tfw-*` as primary |
| C2 | `.agents/skills/` (project) | Generated from template | On-demand via skill contract | tfw-init generates from template | Document `$tfw-*` as primary |
| C3 | `.agents/skills/` (project) | Handwritten per-workflow | AGENTS.md embeds context chain | tfw-update re-copies | Document both `$` and `/` |
| C4 | `.codex/skills/` (legacy) | Handwritten per-workflow | On-demand via skill contract | tfw-init copies | Document `$tfw-*` only |
| C5 | `.agents/skills/` (project) | Hybrid: template + per-workflow overrides | On-demand via skill contract | tfw-init copies, tfw-update diffs | Document `$tfw-*` as primary |
| C6 | No skill folders — AGENTS.md routing only | N/A | AGENTS.md embeds full routing table | tfw-update syncs AGENTS.md | Document natural language only |

## Findings

### E1: Template Insufficiency for Specialized Skills

The generic template (`tfw-command-skill.md.template`, 789 bytes) covers:
- Alias handling, `.tfw/` check, context loading, role lock, template usage

It does NOT cover:
- `tfw-research`: iterations.yaml, stage templates, researcher role lock, never-overwrite-prior-iterations rule
- `tfw-config`: config sync registry, verify/edit modes, specific permitted files
- `tfw-review`: verify-claims-against-real-files rule, review stage templates
- `tfw-handoff`: scope guard ("do not expand beyond TS"), ONB-before-implementation rule
- `tfw-update`: never-overwrite-project-state rule, preserve-customizations rule
- `tfw-init`: handle missing `.tfw/` (other skills assume it exists)

At least 6 of 11 skills require workflow-specific contract clauses that a generic template cannot express. This is structural, not a tuning issue.

### E2: On-Demand Loading Eliminates the 32 KiB Problem

The 32 KiB cap only applies to `AGENTS.md` auto-embed. The AFD skills instruct the agent to *read* conventions.md at runtime — this is a file read, not an instruction embed. TFW's AGENTS.md is ~1.8 KB (well under the cap). Even if all workflow files were loaded, they're loaded sequentially during execution, not upfront.

**Unexpected finding:** The 32 KiB problem (HL Risk R3, high probability/high impact) is a non-issue with the on-demand skill pattern. The risk was based on assuming Codex loads everything into the instruction chain upfront.

### E3: `.agents/skills/` vs `.codex/skills/` — Clear Winner

`.agents/skills/` is both the 2026 cross-platform standard AND already used in the AFD project. `.codex/skills/` is legacy. No reason to support the legacy path in TFW's canonical adapter.

The AFD project already validates this: 11 skills in `.agents/skills/`, working in production.

### E4: AGENTS.md-Only (C6) is Insufficient

C6 (no skill folders) is the current state for non-AFD TFW projects. It routes behavior correctly — the agent reads AGENTS.md, finds workflow references, follows them. But it provides zero UI affordance: no `$` menu entries, no `/skills` listing, no tab completion. H4 confirmed: routing ≠ visibility.

### E5: Generated vs Handwritten Tradeoff

| Factor | Generated (C2) | Handwritten (C1/C5) |
|--------|----------------|---------------------|
| Maintenance | Low — regenerate all from template | Medium — edit individually |
| Accuracy | Misses workflow-specific rules (E1) | Captures all contract clauses |
| Drift risk | Template drifts from workflows silently | Skills drift from workflows individually |
| Setup cost | Low — script generates 11 folders | Medium — copy 11 files |
| AFD evidence | Template exists but all 11 are handwritten | 11 working handwritten skills |

**The AFD evidence is decisive:** the team started with a template, then replaced every skill with a handwritten version. This is empirical proof that generation is insufficient.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| 6 configurations mapped | None |
| Template insufficiency proven (6/11 need custom clauses) | None |
| 32 KiB problem is a non-issue with on-demand pattern | None |
| `.agents/skills/` confirmed as canonical directory | None |

**Sufficiency:**
- [x] External source used (web research on `.agents/` vs `.codex/`)
- [x] Briefing gap closed
- [x] Configuration Space built from Gather dimensions

Stage complete: YES
