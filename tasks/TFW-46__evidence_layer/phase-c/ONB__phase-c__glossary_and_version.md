# ONB — TFW-46 / Phase C: Glossary + Adapters + Version

> **Date**: 2026-07-07
> **Author**: Executor (Antigravity, Claude Opus 4.6)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-46](../HL-TFW-46__evidence_layer.md)
> **TS**: [TS Phase C](TS__phase-c__glossary_and_version.md)

---

## 1. Understanding

Phase C is the final phase of TFW-46 (Evidence Layer). It completes the Evidence Layer by: (1) adding Evidence-related terms to glossary.md, (2) syncing 6 adapter workflow copies that now contain Phase A and B modifications to handoff/review/plan workflows, (3) bumping VERSION from 0.8.7 to 0.8.8, and (4) writing the CHANGELOG entry summarizing all three phases. This is a documentation and sync phase — no behavioral or template changes.

## 2. Entry Points

| File | Purpose |
|------|---------|
| `.tfw/glossary.md` | Add Evidence terms, fix TD-2 stale ref |
| `.agent/workflows/tfw-handoff.md` | Sync from canonical handoff.md |
| `.agent/workflows/tfw-review.md` | Sync from canonical review.md |
| `.agent/workflows/tfw-plan.md` | Sync from canonical plan.md |
| `.claude/commands/tfw-handoff.md` | Sync from canonical handoff.md |
| `.claude/commands/tfw-review.md` | Sync from canonical review.md |
| `.claude/commands/tfw-plan.md` | Sync from canonical plan.md |
| `.tfw/VERSION` | 0.8.7 → 0.8.8 |
| `.tfw/CHANGELOG.md` | New [0.8.8] entry |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions | — |

No blocking questions. The TS is clear and all inputs are available. The glossary entry pattern is well-established (existing entries provide templates), adapter sync is a mechanical copy, and CHANGELOG format is defined by [0.8.7] as a reference.

## 4. Recommendations (suggestions, not blocking)

1. **Claude adapter file sizes differ from Antigravity adapters** — `.claude/commands/tfw-handoff.md` (6283 bytes) vs `.agent/workflows/tfw-handoff.md` (7195 bytes) vs canonical (8120 bytes). Both are stale but the Claude adapter appears more stale. Will sync both to canonical. No action needed from coordinator.
2. **Evidence heading in glossary** — TS §6 suggests a `## Evidence Terms` heading after `## Knowledge Terms` (line 42). I'll follow this recommendation — it matches the existing grouping pattern (Artifact Types → Knowledge Terms → Evidence Terms).

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Claude adapter may have structural differences** — `.claude/commands/` files sometimes have a different header/frontmatter format compared to `.agent/workflows/` files. Will check both before overwriting and document any differences in RF.
2. **CHANGELOG entry scope** — Phase A had significant structural changes (§5 Evidence, renumbering §5-8 → §6-9, 5 anti-patterns, 12 files modified). Phase B had 5 files modified. Phase C is documentation/sync. The CHANGELOG entry needs to cover all three coherently without being excessively long.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS says `.agent/workflows/tfw-{handoff,review,plan}.md`** — confirmed these files exist in `.agent/workflows/`. Sizes show they're stale (all smaller than canonical sources).
2. **TD-2 location** — TS §6 says "glossary.md line 48, Strategic Insight entry — `RF §7` should be `RF §8`." Confirmed: glossary.md line 48 contains `RF §7 "Strategic Insights (Execution)"` which should be `RF §8` after Phase A renumbering.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| K1 | README Values: Honesty Over Convincingness | ✅ | N/A — Phase C is documentation/sync, no honesty-in-evidence concerns | |
| K2 | README Values: Structural Enforcement | ✅ | N/A — Phase C doesn't create structural enforcement | |
| K3 | philosophy.md F4 | ✅ | N/A — structural enforcement principle, not applicable to glossary/adapter sync | |
| K4 | philosophy.md F21 | ✅ | Applied — glossary definitions for DEFERRED/BLOCKED/N/A follow the explicit N/A pattern | |
| K5 | philosophy.md F27 | ✅ | N/A — observable progress principle, not applicable to documentation phase | |
| K6 | process.md F14 | ✅ | N/A — YAML control files, not applicable to glossary | |
| K7 | conventions.md §12 | ✅ | N/A — honesty rules already extended in Phase A | |
| K8 | conventions.md §14 | ✅ | N/A — anti-patterns already added in Phase A | |
| K9 | D41 (TFW-41) | ✅ | N/A — requirements-first TS, Phase C doesn't modify AC structure | |
| K10 | D46 (TFW-38) | ✅ | N/A — Trust Protocol extended in Phase B, no further changes | |
| K11 | philosophy.md F13 | ✅ | Applied — glossary terms must use no domain-specific examples (domain-agnostic by default) | |

> **Cross-references**: use Reference Format (e.g. `RF TFW-18`, `D24`, `TD-72`). See compilable_contract.md §2. Build script resolves to hyperlinks.

---

*ONB — TFW-46 / Phase C: Glossary + Adapters + Version | 2026-07-07*
