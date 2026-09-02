---
description: TFW Resume — locate task, build status matrix, decide next phase
---

# TFW Resume — Phase Status Bootstrap

> **Role:** Coordinator (new or returning)
> **Output:** Phase status matrix + recommendation for next phase
> **When to use:** Starting a new session for a multi-phase task, or returning after a break

> **🔒 ROLE LOCK: COORDINATOR**
> This workflow runs in Coordinator mode ONLY.
> Permitted actions: read artifacts, build status matrix, write Phase HL + TS.
> Forbidden actions: execution, writing ONB, writing RF, writing code.

> Context loading: verify conventions.md §10 core context is loaded before proceeding.

## Who Is Acting

Resolve the acting handle **before the first durable write** — before any `status.md` change,
any journal event, any commit. Once per session, not per turn.

| Situation | What happens |
|---|---|
| One profile in `team/` | it is used, silently |
| Several profiles | read the binding on **this machine** — `~/.tfw/bindings.yaml`, or `%LOCALAPPDATA%\tfw\bindings.yaml` |
| No binding · a shared device · a copied binding · a handle whose profile is gone | **ask exactly one short question**, then proceed |

Identity is never inferred from an OS username, hostname, folder name or account display
string. Every event this session writes carries `on_behalf_of` (always a human) and `via`
(the tool). A writer is not named yet — that is TFW-54 — so do not create a profile per
session. → `conventions.md` §4

## Phase 1: Locate Task

1. User specifies task folder path (e.g. `workspace/2026/20260826-143000__admin_ui/`), or names a task from the portfolio index. **Re-read that task's `status.md` before acting** — the index may be stale, and acting on a projection is what makes it authoritative.
2. List the task folder contents — identify Master HL, Master TS, and all phase artifacts
3. Read **Master HL** — extract:
   - Vision (section 1) — one-liner
   - Phase list (section 4) — all planned phases with priorities
   - Design principles (section 7) — non-negotiable rules
   - Strategic Insights (section 11) — check for gaps from previous session

4. Read **Master TS** (if exists) — extract:
   - Phase definitions and scope budgets
   - Quality contract (anti-patterns, style rules)
   - Verification plan

## Phase 2: Build Status Matrix

5. Scan folder for `HL__Phase*`, `TS__Phase*`, `ONB__Phase*`, `RF__Phase*`, `REVIEW__Phase*` files
6. Build matrix and present:

```markdown
## Phase Status Matrix

| Phase | Description | HL | TS | ONB | RF | REVIEW | Status |
|-------|-------------|----|----|-----|----|----|--------|
| A | Backend: API endpoints | ✅ | ✅ | ✅ | ✅ | ✅ APPROVED | ✅ Done |
| B | Frontend: components | ❌ | ❌ | ❌ | ❌ | ❌ | ⬜ Next |
| C | Integration tests | ❌ | ❌ | ❌ | ❌ | ❌ | ⬜ TODO |
```

7. If the last completed phase has a REVIEW file — read it, extract:
   - Verdict (APPROVED / REVISE / REJECT)
   - Key lessons or issues found
   - Debt captured in REVIEW §5, and the disposition each item carries
8. If a REVISE verdict exists for any phase — flag it as needing re-execution

## Phase 3: Report & Decide

9. Present structured status report to user:

```markdown
## Resume Report — {ID}

**Task**: [title from Master HL]
**Progress**: X of Y phases complete

### Completed
- Phase A: [one-line summary] ✅ [REVIEW verdict]
- Phase B: [one-line summary] ✅ [REVIEW verdict]

### Lessons from Last Phase
- [extracted from REVIEW]

### Next Phase
**Phase C**: [description from Master HL]
- Scope: [N files, brief]
- Dependencies: [any blockers from previous phases]
```

10. Ask user: **"Start planning Phase C?"** or **"Which phase to work on?"**

## After User Confirms

11. Use [plan workflow](plan.md) Phase 4 flow (large task path) to write HL+TS for the chosen phase
12. Present HL+TS for user approval
13. After approval → use [handoff workflow](handoff.md) to delegate to executor agent
14. After RF → use [review workflow](review.md) (`/tfw-review`) for review

## Anti-patterns

- Skip reading Master HL/TS and jump straight to writing phase TS
- Read all RF files in full (only read REVIEW summaries — RF is for executors)
- Start planning without showing the status matrix first
- Assume phase order is fixed — user may want to skip or reorder
- Treat a previous phase's REVIEW §5 as a queue to inherit — every item there was disposed of before that phase closed, and re-opening it is how a project rebuilds the registry retired at 2.1.0
