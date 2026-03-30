# ONB — TFW-11 / Phase B: Integration — Plan Gate + Pipeline Desyncs

> **Date**: 2026-03-30
> **Author**: Executor (AI)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-11](HL-TFW-11__research_stage.md)
> **TS**: [TS Phase B](TS__PhaseB__integration_desyncs.md)

---

## 1. Understanding

Fix all pipeline desyncs left from Phase A and integrate the RESEARCH gate into plan.md. Six file modifications, zero new files. This resolves Tech Debt #1-8 from Phase A REVIEW plus adds the plan.md RESEARCH gate (recommend/ask/never-skip logic). Adapters and slash commands are Phase C.

## 2. Entry Points

| File | Action | TS Step |
|------|--------|---------|
| `.tfw/workflows/plan.md` | MODIFY | Step 1 — RESEARCH gate (Phase 3.5) + pipeline diagram |
| `.tfw/README.md` | MODIFY | Step 2 — pipeline diagram, artifact table, status count |
| `.tfw/init.md` | MODIFY | Step 3 — pipeline status line |
| `README.md` (root) | MODIFY | Step 4 — Key Concepts pipeline string |
| `.tfw/conventions.md` | MODIFY | Step 5 — §2 required artifacts, §8 workflow count |
| `.tfw/glossary.md` | MODIFY | Step 6 — workflow def, coordinator role, task naming, read-only AG |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions | — |

## 4. Recommendations (suggestions, not blocking)

1. **`.tfw/README.md` Evolution section** (line 272-273) says "7-status lifecycle" and "3 canonical workflows". TS doesn't mention this section, but it will be stale after our changes. Recommend updating these two numbers inline — same file, minimal extra work.

2. **`.tfw/README.md` Canonical Workflows table** (line 158-164) lists three workflows. Recommend adding research workflow row for consistency — same file, already in scope.

3. **init.md Step 2 config block** (lines 30-37) shows PROJECT_CONFIG.yaml example without `res` template. Recommend adding it for consistency with the actual config file.

## 5. Risks Found

1. **plan.md step numbering** — inserting "Phase 3.5" avoids renumbering existing step numbers (5-15b). If the user later wants clean numbering, a separate cleanup pass would be needed.

## 6. Inconsistencies with Code (spec vs reality)

1. **init.md Antigravity workflow copies** (lines 87-93) — only lists plan, handoff, resume, docs. Missing `research.md`. TS doesn't include this. Will note as observation.

---

*ONB — TFW-11 / Phase B: Integration — Plan Gate + Pipeline Desyncs | 2026-03-30*
