---
description: TFW Docs — update KNOWLEDGE.md and TECH_DEBT.md after task completion
---

# TFW Docs — Knowledge Update Workflow

> **Role:** Coordinator / Reviewer
> **Trigger:** After REVIEW → ✅ APPROVE, or manually via `/tfw-docs`

## Trigger Modes

| Mode | Command | When |
|------|---------|------|
| Auto | _(part of REVIEW)_ | After every approved task |
| Manual | `/tfw-docs {TASK-ID}` | Update knowledge from a specific RF |
| Batch | `/tfw-docs --scan` | Scan all RFs without a `tfw-docs:` marker in REVIEW |

## Triage Gate (1-second decision)

Before running the checklist, decide:

> Was this a **significant** task?
> - Architecture change (new component, pattern, integration)
> - Strategic decision (D-record worthy)
> - Deprecation (something dropped or replaced)
> - New convention or principle
>
> **YES** → run checklist below
> **NO** (bugfix, small refactor, config) → write `tfw-docs: N/A (minor)` in REVIEW

## Knowledge Update Checklist

| # | Question | If YES → update | Section |
|---|----------|-----------------|---------|
| 1 | Architecture changed? | `KNOWLEDGE.md` | Architecture Map |
| 2 | New decision (D-record)? | `KNOWLEDGE.md` | Architecture Decisions |
| 3 | Something deprecated/dropped? | `KNOWLEDGE.md` | Legacy & Deprecation |
| 4 | New tech debt discovered? | `TECH_DEBT.md` | _(append)_ |
| 5 | New principle or convention? | `KNOWLEDGE.md` or `conventions` | Philosophy / Rules |

## After Update

- Mark in REVIEW: `tfw-docs: Applied — updated Sections 1, 3` or `tfw-docs: N/A (minor)`
- Commit knowledge changes with the task commit (not separately)

## Manual Mode

```
/tfw-docs TFW-9
```

Agent reads the RF for the specified task, extracts:
- Observations → tech debt candidates
- Dropped concepts → legacy candidates
- Architecture changes → KNOWLEDGE.md candidates

Presents a diff preview. Human approves before applying.

## Batch Mode

```
/tfw-docs --scan
```

Agent scans all REVIEW files. Any REVIEW without a `tfw-docs:` marker is unprocessed.
Produces a consolidated update proposal for KNOWLEDGE.md and TECH_DEBT.md.
