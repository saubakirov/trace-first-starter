# HL — Phase B: Codex Adapter + Framework Integration

> **Date**: 2026-07-17
> **Author**: Coordinator (Antigravity)
> **Status**: 📝 Phase HL
> **Parent HL**: [HL-TFW-47](../HL-TFW-47__codex_adapter_shortcut_skills.md)

---

## Context

> **Requires:** Phase A ✅ (evidence enforcement)
>
> **Key decisions from research (iter2):**
> - D1: `.agents/skills/` canonical path (2026 cross-platform standard)
> - D2: 11 handwritten skills, not generated from template
> - D3: On-demand loading bypasses 32 KiB cap
> - D4: `$tfw-*` native invocation; `/tfw-*` soft alias
> - D5: Two-location: `.tfw/adapters/codex/` (source) → `.agents/skills/` (installed)
> - D6: YAML frontmatter + Contract heading convention
> - D7: tfw-init copies, tfw-update re-copies
>
> **Budget override:** 13 new files exceeds max_new=8. Justified: 11 skill files are ~1.2 KB thin routers, single conceptual unit.
>
> **Executor: Codex (CL mode)** — the adapter's first user is its own creator. Evidence = Codex successfully runs a TFW workflow using the installed adapter.
>
> **Files to read before writing TS:**
> 1. iter2/RES.md — all Codex adapter decisions
> 2. .tfw/adapters/ — existing adapter patterns (claude-code, antigravity, cursor)
> 3. Phase A RF — what was delivered in evidence enforcement
> 4. README.md — current adapter table
> 5. .tfw/workflows/init.md, update.md — current adapter install/sync steps
> 6. .tfw/glossary.md — Adapter Command definition

## Deliverables

1. `.tfw/adapters/codex/README.md` — install + fallback instructions
2. `.tfw/adapters/codex/AGENTS.md.template` — root routing
3. 11 handwritten skills: `.tfw/adapters/codex/skills/tfw-*/SKILL.md`
4. Install to `.agents/skills/tfw-*/SKILL.md`
5. README adapter table + Quick Start updated
6. `.tfw/adapters/README.md` updated
7. `init.md` — Codex install option
8. `update.md` — Codex adapter sync
9. `glossary.md` — Adapter Command includes Codex
10. Evidence: Codex runs TFW workflow in CL mode

---

*HL — Phase B: Codex Adapter + Framework Integration | 2026-07-17*
