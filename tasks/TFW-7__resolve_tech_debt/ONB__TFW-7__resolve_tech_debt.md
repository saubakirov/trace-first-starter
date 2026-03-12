# ONB — TFW-7: Resolve All Open Tech Debt

> **Date**: 2026-03-12
> **Author**: Executor (AI)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-7](HL-TFW-7__resolve_tech_debt.md)
> **TS**: [TS-TFW-7](TS__TFW-7__resolve_tech_debt.md)

---

## 1. Understanding

Resolve all 6 open tech debt items (TD-2, TD-3, TD-4, TD-7, TD-8, TD-9) via targeted text edits to `.tfw/` files and status updates in `TECH_DEBT.md`. Three items get actual file edits (TD-4, TD-8, TD-9 + TD-2 cross-refs), three are reclassified as Accepted (TD-2, TD-3, TD-7). Goal: zero `⬜ Backlog` items remaining.

## 2. Entry Points

| File | Relevance |
|------|-----------|
| `TECH_DEBT.md` | Registry — update all 6 item statuses |
| `.tfw/conventions.md` L134–142 | §8 Workflows table — add `docs.md` row (TD-8) |
| `.tfw/README.md` L159–169 | §Canonical Workflows — add `docs` row (TD-4), fix count (TD-9) |
| `.tfw/glossary.md` L60–61 | Workflow definition — add cross-ref (TD-2) |
| `.tfw/conventions.md` L31–53 | §3 Artifact Types — add cross-ref (TD-2) |
| `.tfw/README.md` L103–116 | §Artifact Types — add cross-ref (TD-2) |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions. | — |

## 4. Recommendations (suggestions, not blocking)

1. **TD-9 resolution**: TS says to change "five" → remove count entirely ("the following"). I'll also verify line numbers match current file state (TS references L161, currently confirmed at L161).
2. **TD-2 cross-reference placement**: TS specifies exact locations. For `glossary.md`, the TS says "after §Artifact Types header" with path `../conventions.md` and `../README.md` — but these files are siblings in `.tfw/`, so correct relative paths are just `conventions.md` and `README.md` (no `../`). I'll use the correct relative paths.

## 5. Risks Found

1. **Relative path correctness (TD-2)**: TS specifies `../conventions.md` for glossary.md cross-refs, but since glossary.md is in `.tfw/` alongside conventions.md and README.md, the correct path is just `conventions.md` / `README.md`. Minor spec error — will use correct paths.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS §3: "0 new files, 3 modifications"** — Actually 4 files are modified (conventions.md, README.md, glossary.md, TECH_DEBT.md). The count in TS says 3 but lists 4 in the table. Not blocking — all 4 are within budget.
2. **`.tfw/README.md` L278**: Says "3 canonical workflows (plan, handoff, resume)" in the Evolution section. After TD-4/TD-9 fix, this becomes inconsistent. However, this is in the historical v3 description (what v3 *added*), so it's technically accurate — v3 *initially* had 3, the others were added later. No change needed, but flagging for awareness.
3. **`conventions.md` §8**: Currently has 5 rows (plan, handoff, resume, release, update). After TD-8 fix it'll have 6. TS acceptance criteria says "6 rows" — confirmed correct.

---

*ONB — TFW-7: Resolve All Open Tech Debt | 2026-03-12*
