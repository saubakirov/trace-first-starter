# ONB — TFW-25: Values & Principles Consolidation

> **Date**: 2026-04-04
> **Author**: Executor (AI)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-25](HL-TFW-25__values_consolidation.md)
> **TS**: [TS-TFW-25](TS__TFW-25__values_consolidation.md)

---

## 1. Understanding

Consolidate TFW's dispersed values/principles/facts into a clean 3-tier hierarchy: (1) README Values = 8 philosophical beliefs, (2) KNOWLEDGE §0 = 7 battle-tested design principles, (3) knowledge/ = 18 verified facts (pruned from 29). Remove redundant KNOWLEDGE sections (§3 legacy resolved items, §4 tech stack). Absorb P10-P13 engineering patterns into conventions.md. Net result: fewer duplicate concepts, clearer separation of "beliefs" vs "design rules" vs "implementation facts."

## 2. Entry Points

| File | What changes |
|------|-------------|
| `.tfw/README.md` L217-242 | §Values rewrite (5 → 8 items) |
| `KNOWLEDGE.md` L8-26 | §0 prune (14 → 7 P# items) |
| `KNOWLEDGE.md` L115-137 | §3 prune (18 resolved Legacy items) |
| `KNOWLEDGE.md` L152-160 | §4 remove entirely |
| `KNOWLEDGE.md` §5 | Update fact counts |
| `knowledge/convention.md` | Remove F4, F6, F8-F10, F12 → keep 6, renumber |
| `knowledge/process.md` | Remove F2, F3, F8-F10 → keep 5, renumber |
| `.tfw/conventions.md` | New §11 "Design Rules" subsection for P10-P13 |
| `README.md` task board L135 | Status update |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions. TS is fully specified with exact content for all changes. | — |

## 4. Recommendations (suggestions, not blocking)

1. **TS Step 3 line references are off by 1-2 lines from actual KNOWLEDGE.md.** The TS says "Remove lines 115-137" but actual content starts at L113 (first Legacy table row). I'll match by content, not line numbers. No impact on outcome.

2. **TS Step 8 placement.** TS says "insert into §11 or create new subsection nearby. Executor decides." Conventions.md has §11 = "Quality Standard", not "Scope Budgets" (that's §6). I'll insert "Design Rules" as a new subsection under §11 "Quality Standard (no compromises)" since these are quality-adjacent design constraints. Alternative: create a standalone §11.1. I'll use the cleaner approach: add it as a subsection within §11.

3. **philosophy.md F4 — TS says "compress" but doesn't specify how.** F4 content (structural enforcement > format enforcement) is being promoted to README Values as "Structural Enforcement." I'll leave F4 as-is since the README will reference it, and the fact has unique user quote content not in the README. TS §philosophy says "compress F4 (will be in README values)" — the simplest compression is to shorten the fact text and add "→ see also README §Values" cross-ref.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **P# gap numbering may confuse future agents.** After removing P4, P6, P10-P14, the surviving set is P1, P2, P3, P5, P7, P8, P9. Agents reading "P5" might wonder about the missing P4/P6. TS explicitly acknowledges this ("P# numbering preserved, gaps acceptable, historical refs stay valid"). Low risk — accepted.

2. **Cross-references to removed P# items in other task HLs.** The Source column in old task HLs references P10, P11, etc. These are historical artifacts in closed tasks. TS acknowledges ("Historical task HL refs to removed P# remain valid as source links"). No action needed.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS Step 8 says "insert into §11 or create §11.1"** but conventions.md uses `##` headings numbered 1-15 (`## 6) Scope Budgets`, `## 11) Quality Standard`). There is no §X notation — the TS should reference `## 11)`. Minor labeling difference, no functional impact. I'll add a `### Design Rules` under `## 11) Quality Standard`.

---

*ONB — TFW-25: Values & Principles Consolidation | 2026-04-04*
