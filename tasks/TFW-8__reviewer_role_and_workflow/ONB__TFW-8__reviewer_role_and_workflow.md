# ONB — TFW-8: Reviewer Role and Workflow

> **Date**: 2026-03-12
> **Author**: Executor (AI)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-8](HL-TFW-8__reviewer_role_and_workflow.md)
> **TS**: [TS TFW-8](TS__TFW-8__reviewer_role_and_workflow.md)

---

## 1. Understanding

TFW v3 has a structural flaw: `handoff.md` bundles executor work (Phases 1-3) and coordinator review (Phase 4) in one file. Low-cost executor models read the whole file and self-review, violating the quality gate principle. The fix: extract Phase 4 into a standalone `/tfw-review` workflow with `🔒 ROLE LOCK: REVIEWER`, add Reviewer as a named role in glossary/conventions, and make executors explicitly STOP after RF.

## 2. Entry Points

| File | Lines of Interest |
|------|-------------------|
| `.tfw/workflows/handoff.md` | L99-140 (Phase 4 to remove), L142-161 (multi-phase diagram), L163-178 (anti-patterns) |
| `.tfw/conventions.md` | L136-146 (§8 Workflows table), L181-196 (§14 Anti-patterns), L198-217 (§15 Role Lock) |
| `.tfw/glossary.md` | L62-63 (Workflow definition), L72-93 (Roles section) |
| `AGENTS.md` | L28-32 (workflow list) |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions. | — |

HL and TS are clear, self-consistent, and match actual file content. Proceeding.

## 4. Recommendations (suggestions, not blocking)

1. **REVIEW template Author field**: The current template has `{coordinator}` as author placeholder. Consider updating it to `{reviewer}` for consistency with the new role. TS marks template changes as out of scope, so I will NOT touch the template — noting for future.
   > **Coordinator**: Agreed. Out of scope. Noted for future task.

2. **`handoff.md` Antigravity adapter**: The adapter `.agent/workflows/tfw-handoff.md` is a byte-identical copy of `.tfw/workflows/handoff.md`. After modifying the canonical `handoff.md`, the adapter must also be updated. TS doesn't explicitly list this file, but it's the same adapter pattern as Step 2 (creating `tfw-review.md`). I will update the adapter copy to stay consistent.
   > **Coordinator**: Correct. Added to TS as Step 4 in Phase A.

3. **`conventions.md` §8 Workflows table, `handoff.md` description**: TS says to change the `description` YAML frontmatter. The Antigravity adapter copy also has the same frontmatter — both need the same update.
   > **Coordinator**: Addressed in Step 3a (canonical) and Step 4 (adapter sync).

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Adapter sync for `handoff.md`**: `.agent/workflows/tfw-handoff.md` is a copy of `.tfw/workflows/handoff.md`. If only the canonical file is modified without updating the adapter, Antigravity will use the stale adapter with Phase 4 still present. The TS doesn't list this file explicitly, but consistency requires updating it.
   > **Coordinator**: Added to TS as Step 4. Also added Phase B for all remaining doc references (`.tfw/README.md`, `plan.md`, `resume.md`, `init.md`, adapter README).

2. **YAML frontmatter of `handoff.md`**: The `description` field says "coordinator review". TS Step 3a mentions updating the header but doesn't explicitly mention the YAML `description` frontmatter. It should also be updated to remove "coordinator review".
   > **Coordinator**: Addressed in updated TS Step 3a — explicitly covers the YAML `description` field.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS Step 3a references "lines 1-15"**: Actual role lock block spans lines 1-15 in `handoff.md`. Confirmed accurate.

2. **TS Step 3b references "lines 99-140"**: Phase 4 actually spans lines 99-140. Confirmed accurate.

3. **TS Step 3c references "lines 142-161"**: Multi-phase diagram spans lines 142-161. Confirmed accurate.

4. **TS Step 3d references "lines 163-178"**: Anti-patterns span lines 163-178. Confirmed accurate.

5. **TS Step 4b references "around line 195"**: Anti-patterns in conventions.md are at lines 181-196. Confirmed accurate.

6. **TS Step 4c references "lines 202-209"**: Role Lock table is at lines 198-209. Confirmed accurate. Line 209 = `**REVIEW** files can be written by any role.` — confirmed present.

7. **TS Step 5a references "line 63"**: Workflow definition is at line 63 in glossary.md. Confirmed accurate.

8. **TS Step 5c references "lines 79-84"**: Coordinator role is at lines 79-84. Confirmed accurate.

9. **TS Step 6a references "line 32"**: AGENTS.md workflow list last item is at line 32. Confirmed accurate.

No inconsistencies found. All TS line references match the actual file content.

---

*ONB — TFW-8: Reviewer Role and Workflow | 2026-03-12*
