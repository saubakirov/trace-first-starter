# HL — TFW-8: Reviewer Role and Workflow

> **Date**: 2026-03-12
> **Author**: Coordinator (AI)
> **Status**: 🔵 HL — Awaiting review

---

## 1. Vision

Executor agents (especially low-cost models) self-review their own work — writing REVIEW files without being asked. This defeats the entire purpose of review as a quality gate. The root cause is structural: TFW v3 doesn't treat review as a first-class role-locked activity.

> "Review must be a separate act by a separate agent. Self-review is not review."

## 2. As-Is — Root Cause Analysis

### 2.1 What's broken

| # | Problem | Location | Impact |
|---|---------|----------|--------|
| P1 | `handoff.md` combines executor (Phases 1-3) and reviewer (Phase 4) in **one file** | `.tfw/workflows/handoff.md` | Executor reads the whole file, sees review instructions, and continues into Phase 4 |
| P2 | Role Lock table says "REVIEW files can be written by **any role**" | `.tfw/conventions.md` §15 | Explicitly permits executor self-review |
| P3 | No **Reviewer** role exists | `.tfw/glossary.md` §Roles | Review is a "phase" of Coordinator, not a distinct identity |
| P4 | No dedicated `/tfw-review` workflow | `.agent/workflows/` | No clear entry point for "I want to review an RF" |
| P5 | Phase 4 of `handoff.md` says "coordinator (original architect **or user**)" | `.tfw/workflows/handoff.md` L101 | Ambiguous — who exactly reviews? |

### 2.2 What works well

| # | Good aspect | Why keep it |
|---|-------------|-------------|
| G1 | REVIEW template is solid | 9-point checklist, verdict system, tech debt collection all work |
| G2 | Tech debt pipeline works | Observations → REVIEW triage → TECH_DEBT.md is proven |
| G3 | Status flow has `🔍 REV` | The status exists, just needs enforcement |
| G4 | Role Lock concept is sound | Just needs correct application to review |

### 2.3 Why executors self-review

1. **They read `handoff.md`** → see Phase 4 → no barrier says "stop here, you're the executor"
2. **conventions.md explicitly allows it** → "REVIEW files can be written by any role"
3. **No role switch signal** → no `/tfw-review` command, no "start a new session for review"
4. **Low-cost models** follow instructions literally — if Phase 4 is in the same file they were told to read, they execute it

## 3. To-Be

### 3.1 Changes overview

| # | Change | From → To |
|---|--------|-----------|
| C1 | Add **Reviewer** role | 3 roles → 4 roles (User, Coordinator, Executor, **Reviewer**) |
| C2 | Extract Phase 4 into `/tfw-review` workflow | Embedded in handoff → standalone workflow |
| C3 | Remove Phase 4 from `handoff.md` | 4 phases → 3 phases (executor STOPS after RF) |
| C4 | Fix Role Lock table | "REVIEW by any role" → "REVIEW by Reviewer only" |
| C5 | Add explicit STOP instruction at end of `handoff.md` | Implicit → explicit "DO NOT REVIEW" |
| C6 | New `.agent/workflows/tfw-review.md` | Doesn't exist → adapter workflow |

### 3.2 The Reviewer role

The Reviewer is a **coordinator acting in review mode**. Not a fundamentally new identity — it's the coordinator with a locked scope:

- **Can do**: read RF, read TS (for DoD), write REVIEW, triage observations, update TECH_DEBT.md, update Task Board
- **Cannot do**: write code, write ONB, write HL/TS, modify RF
- **Who fills this role**: coordinator AI in a new session, or the user

This distinction matters because:
- A **new session** = fresh context, no bias from implementation
- A **role lock** = even if same model, it's constrained to review-only actions
- An **explicit workflow** = the model knows exactly what it can/cannot do

### 3.3 Handoff workflow change

Current `handoff.md`:
```
Phase 1: ONB (executor)
Phase 2: Execute (executor)
Phase 3: RF (executor)
Phase 4: Review (coordinator)  ← REMOVE FROM HERE
```

After:
```
Phase 1: ONB (executor)
Phase 2: Execute (executor)
Phase 3: RF (executor)
🛑 STOP — executor's job is done. Start /tfw-review.
```

## 4. Phases

### Phase A: Core extraction 🔴

Extract review into its own workflow and update all role/convention files:

1. Create `.tfw/workflows/review.md` — canonical review workflow
2. Create `.agent/workflows/tfw-review.md` — adapter copy
3. Modify `.tfw/workflows/handoff.md` — remove Phase 4, add STOP
4. Modify `.agent/workflows/tfw-handoff.md` — adapter sync (same edits as #3)
5. Modify `.tfw/conventions.md` — fix Role Lock table, §8 Workflows table, §14 anti-patterns
6. Modify `.tfw/glossary.md` — add Reviewer role, update Workflow definition, update Coordinator
7. Modify `AGENTS.md` — add review workflow to the list
8. Modify `.tfw/CHANGELOG.md` — add to `[Unreleased]`

Scope check: 2 NEW + 6 MODIFY = 8 files. Exceeds budget by 1 — acceptable because 2 of the modifications are adapter copies (byte-identical).

### Phase B: Documentation sync 🟡

Update all secondary references across docs:

1. Modify `.tfw/README.md` — L77 directory tree, L168 workflows table, L281 evolution
2. Modify `.tfw/workflows/plan.md` — L76 mention `/tfw-review` after `/tfw-handoff`
3. Modify `.tfw/workflows/resume.md` — L83 note review step after handoff
4. Modify `.tfw/init.md` — L97, L184, L192 workflow lists
5. Modify `.tfw/adapters/antigravity/README.md` — L21, L39, L51 adapter setup instructions

Scope check: 0 NEW + 5 MODIFY = 5 files. Within budget.

## 5. Definition of Done (DoD)

- ✅ 1. `.tfw/workflows/review.md` exists with Role Lock: Reviewer, 9-point checklist, tech debt pipeline, trace updates
- ✅ 2. `.agent/workflows/tfw-review.md` is byte-identical copy of `.tfw/workflows/review.md` (with YAML frontmatter)
- ✅ 3. `handoff.md` Phase 4 removed; executor STOP instruction present at end
- ✅ 4. `.agent/workflows/tfw-handoff.md` updated to match canonical `handoff.md`
- ✅ 5. `conventions.md` §15 Role Lock table updated: Reviewer role added, "any role" removed
- ✅ 6. `glossary.md` has Reviewer role definition, Coordinator duties updated
- ✅ 7. `AGENTS.md` lists `review.md` workflow
- ✅ 8. `CHANGELOG.md` has review workflow entry in `[Unreleased]`
- ✅ 9. `.tfw/README.md` directory tree, workflows table, and evolution section updated
- ✅ 10. `plan.md`, `resume.md`, `init.md` reference `/tfw-review`
- ✅ 11. Antigravity adapter README includes review workflow in setup instructions
- ✅ 12. Status flow unchanged (`🔍 REV` remains as-is)
- ✅ 13. REVIEW template unchanged (it's already good)

## 6. Definition of Failure (DoF)

- ❌ 1. Executor can still read review instructions in `handoff.md`
- ❌ 2. Role Lock table still permits "any role" for REVIEW
- ❌ 3. No `/tfw-review` slash command available
- ❌ 4. Any file in `.tfw/` still says "Executor + Coordinator" for handoff role
- ❌ 5. `CHANGELOG.md` doesn't mention the new workflow

**On failure:** re-examine the extraction boundary. Check if executor models still see review content.

## 7. Principles

1. **Separation of execution and review** — the person who writes the code does not review it. Even if it's the same AI model, it must be a different session with a different role lock.
2. **Explicit over implicit** — a STOP instruction is better than hoping the executor knows to stop. A dedicated workflow is better than a phase buried in another workflow.
3. **Low-cost model compatibility** — the design must work with models that follow instructions literally. No nuance requirement. Clear boundaries are cheaper than clever heuristics.

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| All prior tasks complete | ✅ (TFW-1 through TFW-7 DONE) |
| REVIEW template stable | ✅ (no changes needed) |

## 9. Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Existing adapters (Claude Code, Cursor) don't get the new workflow | Low | Medium | Add to scope — but only Antigravity adapter is maintained here; others are templates |
| User forgets to run `/tfw-review` after `/tfw-handoff` | Medium | Low | Add reminder in the STOP instruction of handoff.md |
| Over-engineering the Reviewer role | Low | Medium | Keep it simple: Reviewer = Coordinator with locked scope, not a new persona |

---

*HL — TFW-8: Reviewer Role and Workflow | 2026-03-12*
