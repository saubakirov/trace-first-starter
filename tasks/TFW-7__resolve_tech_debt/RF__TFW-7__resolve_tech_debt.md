# RF — TFW-7: Resolve All Open Tech Debt

> **Date**: 2026-03-12
> **Author**: Executor (AI)
> **Status**: 🟢 RF — Awaiting review
> **Parent HL**: [HL-TFW-7](HL-TFW-7__resolve_tech_debt.md)
> **TS**: [TS-TFW-7](TS__TFW-7__resolve_tech_debt.md)

---

## 1. What Was Done

### Step 1: Workflow listing consistency (TD-4, TD-8, TD-9)

| Item | File | Change |
|------|------|--------|
| TD-8 | `.tfw/conventions.md` §8 | Added `docs.md` row to Workflows table (now 6 rows) |
| TD-4 | `.tfw/README.md` §Canonical Workflows | Added `docs` row to table |
| TD-9 | `.tfw/README.md` L161 | Changed "five canonical workflows" → "the following canonical workflows" |

### Step 2: Accept TD-3 (no file changes)

TD-3 reclassified as `Accepted — ONB always required`. ONB is always required by protocol; lightweight mode would undermine quality gates.

### Step 3: Cross-references (TD-2)

| File | Location | Cross-ref added |
|------|----------|-----------------|
| `.tfw/conventions.md` | §3 Artifact Types | → glossary.md (terminology), README.md (philosophy) |
| `.tfw/README.md` | After §Artifact Types | → conventions.md (naming rules), glossary.md (definitions) |
| `.tfw/glossary.md` | §Artifact Types | → conventions.md (canonical rules), README.md (philosophy) |

### Step 4: Accept TD-7 (no file changes)

TD-7 reclassified as `Accepted — by design`. Adapters reference `.tfw/workflows/` directly; no per-adapter copies needed.

### Step 5: TECH_DEBT.md updated

All 6 items resolved:

| Item | Final Status |
|------|-------------|
| TD-2 | Accepted — cross-refs added (TFW-7) |
| TD-3 | Accepted — ONB always required (TFW-7) |
| TD-4 | ✅ Resolved (TFW-7) |
| TD-7 | Accepted — by design (TFW-7) |
| TD-8 | ✅ Resolved (TFW-7) |
| TD-9 | ✅ Resolved (TFW-7) |

## 2. Files Changed

| File | Action | Lines changed |
|------|--------|---------------|
| `.tfw/conventions.md` | MODIFY | +3 lines (cross-ref + docs row + count fix) |
| `.tfw/README.md` | MODIFY | +4 lines (cross-ref + docs row + count fix) |
| `.tfw/glossary.md` | MODIFY | +2 lines (cross-ref) |
| `TECH_DEBT.md` | MODIFY | 6 status updates |
| `README.md` | MODIFY | Task board status → 🟠 ONB |

## 3. Deviations from TS

| # | TS spec | Actual | Justification |
|---|---------|--------|---------------|
| 1 | glossary.md cross-ref uses `../conventions.md` | Used `conventions.md` | Files are siblings in `.tfw/`; `../` is incorrect |
| 2 | "0 new files, 3 modifications" | 4 files modified | conventions.md, README.md, glossary.md, TECH_DEBT.md — TS table listed 4 but summary said 3 |

## 4. Acceptance Criteria Check

- [x] `conventions.md` §8 Workflows table has 6 rows (plan, handoff, resume, docs, release, update)
- [x] `.tfw/README.md` §Canonical Workflows has all rows and no hardcoded count
- [x] TD-3 marked as Accepted in TECH_DEBT.md
- [x] Cross-reference notes added to conventions, README, glossary
- [x] All TECH_DEBT.md items resolved or accepted — no `⬜ Backlog` remaining
- [x] No new inconsistencies introduced

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/README.md` | 280 | naming | Evolution §v3 says "3 canonical workflows" — historically accurate (v3 initially had 3), but could confuse readers. Not modified per TS scope. |
| 2 | `.tfw/glossary.md` | 61 | naming | Workflow definition says "Three canonical workflows: plan, handoff, resume" — outdated count, should list all 6. Not modified per TS scope. |

---

*RF — TFW-7: Resolve All Open Tech Debt | 2026-03-12*
