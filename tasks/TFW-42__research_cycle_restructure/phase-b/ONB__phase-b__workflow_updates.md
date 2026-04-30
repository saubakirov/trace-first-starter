# ONB — TFW-42 / Phase B: Workflow Updates

> **Date**: 2026-04-30
> **Author**: Executor (Antigravity)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-42](../HL-TFW-42__research_cycle_restructure.md)
> **TS**: [TS Phase B](TS__phase-b__workflow_updates.md)

---

## 1. Understanding

Phase B updates two workflow files (`research/base.md` and `plan.md`) to reference the new folder structure established in Phase A — unified `research/` container with `research/iterN/` subfolders, numbered stage files (`1_briefing.md`…`4_challenge.md`), co-located `RES.md`, `research/iterations.yaml` location, and kebab-case phase folders (`phase-a/`). After this phase, any agent following these workflows will create research artifacts in the correct locations.

## 2. Entry Points

| File | Current state | What changes |
|------|--------------|-------------|
| `.tfw/workflows/research/base.md` (131 lines) | References `researchN/`, `research/briefing.md`, `RES__{ID}__title.md` | Steps 0, 3, 4, 5, 6: all paths to new convention |
| `.tfw/workflows/plan.md` (153 lines) | References `PhaseA/`, `HL__PhaseA__`, iterations.yaml at task root | Step 6b: path + multi-agent ref. Step 7: kebab-case phases |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions | — |

## 4. Recommendations (suggestions, not blocking)

1. **TS §6 line number references are approximate.** TS gives line numbers (e.g., "Step 0 lines 12-26") that match the pre-Phase-B state of base.md. I will navigate by section headers (Step 0, Step 3, etc.) as the TS §8 Risk section itself recommends.

2. **Step 6c in plan.md also references RES paths.** TS §8 Risk row 2 correctly identifies this. Step 6c (line 100) says `Read all RES__* files` — this needs updating to `Read all research/iterN/RES.md files` for consistency. I will include this as part of AC-1's spirit (all old-style RES paths should be gone from both files), though it technically lives in plan.md.

3. **plan.md Step 6b currently says "Create `iterations.yaml` in task folder"** (line 90). The new convention places it at `research/iterations.yaml`. This change is explicitly covered by AC-3.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **plan.md Step 6c RES path reference.** Line 100 has `Read all RES__* files and iterations.yaml` — uses old naming. Not explicitly in AC-1/AC-2/AC-3 but the Definition of Failure §7 says "Any `researchN/` or `research2/` path remains in **either** workflow". The `RES__*` glob also needs updating. Will fix as part of ensuring no old paths remain.

2. **handoff.md TD-112 (PhaseA references).** TS §2 Out of Scope explicitly excludes handoff.md. Will report as observation if still present, but will NOT modify.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS §6 says base.md Step 4 is at lines 51-58.** Actual Step 4 (Briefing Protocol) is at lines 51-58. Correct — no inconsistency.

2. **TS §6 says plan.md Step 7 is at lines 131-140.** Actual Step 7 block showing `PhaseA/` is at lines 131-140. Correct.

3. **TS says plan.md Step 6b is at lines 88-96.** Actual Step 6b (Create iterations.yaml) is at lines 88-96. Correct.

No inconsistencies found between spec and reality.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| KC1 | knowledge/philosophy.md F4 — Structural enforcement | ✅ | Applied: numbered files in template references enforce execution order | |
| KC2 | knowledge/philosophy.md F24 — Instructions vs heuristics | ✅ | Applied: numbered stage file names are self-explanatory in workflow references | |
| KC3 | knowledge/convention.md F19 — Naming consistency | ✅ | Applied: kebab-case `phase-a/` in plan.md Step 7 replaces PascalCase | |
| KC4 | KNOWLEDGE.md D48 — Naming normalization | ✅ | Applied: extending lowercase convention to phase folder examples in workflows | |
| KC5 | KNOWLEDGE.md D38 — Multi-iteration research | ✅ | Applied: refactoring iteration folder references from `researchN/` to `research/iterN/` | |
| KC6 | knowledge/process.md F14 — YAML control files | ✅ | Applied: iterations.yaml path update + multi-agent reference in plan.md | |
| KC7 | knowledge/convention.md F15 — Multi-phase subfolders | ✅ | Applied: PhaseX → phase-x in plan.md Step 7 example | |

No additional PV items needed — coordinator's coverage is complete for this scope.

---

*ONB — TFW-42 / Phase B: Workflow Updates | 2026-04-30*
