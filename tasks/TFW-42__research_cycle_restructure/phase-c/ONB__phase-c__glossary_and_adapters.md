# ONB — TFW-42 / Phase C: Glossary & Adapter Sync

> **Date**: 2026-04-30
> **Author**: Executor (Antigravity)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-42](../HL-TFW-42__research_cycle_restructure.md)
> **TS**: [TS Phase C](TS__phase-c__glossary_and_adapters.md)

---

## 1. Understanding

Phase C finalizes TFW-42 by updating three glossary entries (Iteration, iterations.yaml, min_iterations) to reflect the `research/iterN/` folder structure and co-located RES.md convention established in Phase A. Then sync the two modified workflows (`research/base.md` and `plan.md`) to all adapter directories (`.agent/workflows/` and `.claude/commands/`), bump VERSION to 0.8.6, and record the TFW-42 change in CHANGELOG.md.

## 2. Entry Points

| File | Current state | What changes |
|------|---------------|--------------|
| `.tfw/glossary.md` L144-151 | 3 entries with old paths (`researchN/`, `RES__iterN__*.md`, "at task root") | Update to `research/iterN/`, `research/iterN/RES.md`, `research/iterations.yaml` |
| `.agent/workflows/tfw-research.md` | Stale copy (pre-Phase B) | Overwrite with `.tfw/workflows/research/base.md` |
| `.agent/workflows/tfw-plan.md` | Stale copy (pre-Phase B) | Overwrite with `.tfw/workflows/plan.md` |
| `.claude/commands/tfw-research.md` | Stale copy (pre-Phase B) | Overwrite with `.tfw/workflows/research/base.md` |
| `.claude/commands/tfw-plan.md` | Stale copy (pre-Phase B) | Overwrite with `.tfw/workflows/plan.md` |
| `.tfw/VERSION` | `0.8.5` | `0.8.6` |
| `.tfw/CHANGELOG.md` | No TFW-42 entry | Add `[0.8.6]` section |
| `.tfw/project_config.yaml` L7 | `version: "0.8.5"` | `version: "0.8.6"` |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions. | — |

## 4. Recommendations (suggestions, not blocking)

1. **Sync all 4 adapter copies (not just 2).** TS §5 AC-2 says "Other adapter directories (claude-code, cursor) checked — if workflow copies exist, sync them too." Both `.agent/workflows/` (Antigravity) and `.claude/commands/` (Claude Code) have stale copies of tfw-research.md and tfw-plan.md. The cursor adapter (`.tfw/adapters/cursor/`) only has a template file, no workflow copies — no action needed there. **Total: 4 files to sync** (2 Antigravity + 2 Claude Code).

## 5. Risks Found (edge cases, potential issues not in TS)

1. **TS says 5 modifications, actual is 8.** TS §4 lists `.agent/workflows/tfw-research.md` and `.agent/workflows/tfw-plan.md` but `.claude/commands/` also has stale copies (tfw-research.md, tfw-plan.md). AC-2 explicitly covers this ("Other adapter directories... if workflow copies exist, sync them too"). Plus project_config.yaml version bump (AC-3 bullet 3) adds a 6th modification not in the TS §4 table. **Total: 8 files modified** (glossary + 4 adapter copies + CHANGELOG + VERSION + project_config.yaml). All within scope budgets.

2. **glossary.md "Iteration" entry L144-145 also references `researchN/` (not just `research/iterN/`).** Verified: the current text says `researchN/` which is the old convention. TS correctly identifies this.

## 6. Inconsistencies with Code (spec vs reality)

1. TS §4 Affected Files table lists 5 files, but AC-2 and AC-3 together imply 8 files total. Not a contradiction — TS §4 was conservative, ACs are authoritative.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| KC1 | philosophy.md F4 (Structural enforcement) | ✅ | Applied — numbered files and container structure are being propagated to glossary definitions | |
| KC2 | philosophy.md F24 (Heuristics > instructions) | ✅ | N/A — glossary is definitional, not instructional | |
| KC3 | convention.md F19 (Naming consistency) | ✅ | Applied — glossary entries will use consistent `phase-a` kebab-case | |
| KC4 | KNOWLEDGE.md D48 (Naming normalization) | ✅ | Applied — glossary paths updated to match D48 convention | |
| KC5 | KNOWLEDGE.md D38 (Multi-iteration research) | ✅ | Applied — glossary entries describe the refactored D38 implementation | |
| KC6 | process.md F14 (YAML control files) | ✅ | Applied — iterations.yaml glossary entry describes its role as coordinator control | |
| KC7 | convention.md F15 (Multi-phase subfolders) | ✅ | N/A — Phase glossary entry already uses generic naming; no `PhaseX` reference to fix | |

---

*ONB — TFW-42 / Phase C: Glossary & Adapter Sync | 2026-04-30*
