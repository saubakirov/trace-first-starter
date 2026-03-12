---
description: TFW Review — reviewer checks RF against TS, writes REVIEW, triages tech debt
---

# TFW Review — Task Review by Reviewer

> **Role:** Reviewer (coordinator in review-locked mode)
> **Input:** Completed RF file + TS (for DoD verification)
> **Output:** REVIEW file with verdict + TECH_DEBT.md updates

> **🔒 ROLE LOCK: REVIEWER**
> Permitted artifacts: REVIEW file only.
> Forbidden actions: writing code, writing ONB, writing RF, modifying HL/TS.
> The reviewer MUST NOT modify any implementation artifacts. If fundamental issues are found — write them in REVIEW and set verdict to ❌ REJECT.

## Context Loading (Reviewer)

When starting as reviewer, load in order:
1. `AGENTS.md` — agent instructions
2. `.tfw/conventions.md` — project conventions
3. `.tfw/glossary.md` — terminology
4. `KNOWLEDGE.md` — architecture, decisions, legacy (if exists)
5. **Master HL** for the task — understand vision, design philosophy, architecture decisions
6. **Phase HL** (if multi-phase) — phase-specific scope and context
7. **TS file** for the task — exact scope, DoD, constraints
8. **RF file** to review — the executor's results (mandatory)
9. Related HL/TS/RF files referenced in the task
10. Relevant code files modified by the executor

## Step 1: Read and Understand

1. **Read RF thoroughly** — understand what was done, how, and why
2. **Read TS** — understand what was required (DoD, scope, constraints)
3. **Read HL** — understand design philosophy and architectural intent
4. **Examine changed files** — verify changes match RF claims
5. **Read executor's ONB** — check if ONB recommendations were addressed

## Step 2: Review Checklist

Apply the 9-point checklist. For each item, note pass/fail with evidence:

| Check | Description |
|-------|-------------|
| **DoD met?** | All items from TS Definition of Done achieved |
| **Code quality** | Follows project conventions, naming, type hints |
| **Test coverage** | Tests written and passing per TS |
| **Philosophy aligned** | Matches design philosophy from HL |
| **Tech debt** | Any shortcuts taken? Documented? |
| **Security** | No secrets exposed, guards in place |
| **Observability** | Logging, trace_id, records preserved |
| **Breaking changes** | API compat, backward compat, migration needed? |
| **Style & standards** | Code style, naming conventions |

## Step 3: Tech Debt Collection

After reviewing, the reviewer MUST:
1. Read executor's `## Observations` section from RF
2. Triage each item (severity: Low/Medium/High)
3. Add to REVIEW file as `## Tech Debt Collected` section
4. Append to project-level `TECH_DEBT.md`

```markdown
## Tech Debt Collected

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| 1 | Phase A RF | Low | 3 files | Duplicate helpers | → backlog |
```

## Step 4: Write REVIEW File

Create REVIEW file using `.tfw/templates/REVIEW.md` as canonical format. Must contain:
- Checklist results (9-point, with evidence)
- Tech debt collected from observations
- Verdict with justification

## Step 5: Verdict

Choose one verdict:

- **✅ APPROVE** — all checks pass → update Task Board to ✅ DONE, update all traces
- **🔄 REVISE** — specific items to fix → list items clearly, user starts new `/tfw-handoff` session for fixes
- **❌ REJECT** — fundamental issues → back to HL/TS revision with new `/tfw-plan`

## Step 6: Update Traces

After verdict:
1. **Update Task Board** in `README.md` — set final status
2. **Update TECH_DEBT.md** — append any new items from Tech Debt Collected
3. If ✅ APPROVE: mark task as ✅ DONE in Task Board

## Anti-patterns

- Reviewer writes REVIEW without reading RF — must read the actual results
- Reviewer skips observations triage — every observation must be triaged to TECH_DEBT.md
- Reviewer modifies RF or code — **🔒 Role Lock violation**
- Executor writes REVIEW file — **🔒 Role Lock violation** (start `/tfw-review` instead)
- Reviewer approves without checking DoD — each TS acceptance criterion must be verified
- Reviewer and executor are the same session — review must be a separate session/agent
- **🔒 Reviewer MUST NOT write code, ONB, RF, HL, or TS** — Role Lock violation
