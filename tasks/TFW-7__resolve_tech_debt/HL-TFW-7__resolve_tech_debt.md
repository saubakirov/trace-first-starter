# HL — TFW-7: Resolve All Open Tech Debt

> **Date**: 2026-03-12
> **Author**: Coordinator (AI)
> **Status**: 🔵 HL — Awaiting review

---

## 1. Vision

Clean up all open tech debt items accumulated from TFW-4 through TFW-6 reviews. After this task, `TECH_DEBT.md` should have zero `⬜ Backlog` items — everything is either `✅ Resolved` or `Accepted`.

## 2. Current State (As-Is)

| # | Severity | Description | Status |
|---|----------|-------------|--------|
| TD-2 | Med | Content duplication across `.tfw/conventions.md`, `.tfw/README.md`, `.tfw/glossary.md` | ⬜ TFW-4 Phase B |
| TD-3 | Low | ONB overhead for small single-phase tasks | ⬜ TFW-4 Phase C |
| TD-4 | Low | `.tfw/README.md` workflows section omits `docs` workflow | ⬜ Backlog |
| TD-7 | Low | No Claude Code/Cursor adapter copies for `release`/`update` workflows | ⬜ Backlog |
| TD-8 | Med | `docs.md` workflow not listed in `conventions.md` §8 Workflows table | ⬜ Backlog |
| TD-9 | Low | `.tfw/README.md` L161 says "five" workflows but lists only 5 rows — `docs` is missing; project structure (L77) lists 6 | ⬜ Backlog |

## 3. Target State (To-Be)

All items resolved via targeted text edits:

| # | Resolution |
|---|-----------|
| TD-2 | Add cross-reference notes in each overlapping file, deduplicate where possible. Mark `Accepted — cross-refs added`. |
| TD-3 | ONB is always required — lightweight mode could undermine the protocol. Mark `Accepted — ONB always required`. |
| TD-4 | Add `docs` row to `.tfw/README.md` §Canonical Workflows table. Mark `✅ Resolved`. |
| TD-7 | Adapter copies for `release`/`update` are NOT needed — adapters reference `.tfw/workflows/` directly. Reclassify as `Accepted — by design`. |
| TD-8 | Add `docs.md` row to `conventions.md` §8 Workflows table. Mark `✅ Resolved`. |
| TD-9 | Remove the hardcoded count from `.tfw/README.md` L161 (future-proof). Mark `✅ Resolved`. |

## 4. Phases

### Single Phase 🟢

All items are small text edits across ≤6 files. Fits within scope budget as a single phase.

## 5. Definition of Done (DoD)

- ✅ 1. All TD items in `TECH_DEBT.md` have status `✅ Resolved` or `Accepted`
- ✅ 2. `conventions.md` §8 lists all 6 workflows
- ✅ 3. `.tfw/README.md` §Canonical Workflows lists all workflows without hardcoded count
- ✅ 4. No factual inconsistencies between `.tfw/README.md`, `conventions.md`, and `glossary.md`
- ✅ 5. `TECH_DEBT.md` registry updated with final statuses

## 6. Definition of Failure (DoF)

- ❌ 1. Edits introduce new inconsistencies between files
- ❌ 2. Scope creep beyond text fixes (e.g., restructuring entire files)

**On failure:** revert edits, re-scope as multi-phase.

## 7. Principles

1. **Minimal edits** — fix only what each TD describes, no rewrites
2. **Accept where appropriate** — not all debt needs fixing; some is acceptable

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| TFW-6 complete | ✅ |

## 9. Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Cross-reference edits create circular references | Low | Low | Keep references one-directional |

---

*HL — TFW-7: Resolve All Open Tech Debt | 2026-03-12*
