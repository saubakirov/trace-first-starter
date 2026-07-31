---
description: TFW Docs — update KNOWLEDGE.md and TECH_DEBT.md after task completion
---

# TFW Docs — Knowledge Update Workflow

> **Role:** Coordinator. A Reviewer may trigger this workflow after APPROVE, but any
> routed docs commit uses the registered `coordinator` Role Lock.
> **Trigger:** After REVIEW → ✅ APPROVE, or manually via `/tfw-docs`

## Prerequisites

1. Read `KNOWLEDGE.md` — current state before updating
2. Read `TECH_DEBT.md` — current entries

## Scope

**Writes to:** KNOWLEDGE.md §1 (Architecture Map), §2 (Key Artifacts), §3 (Legacy & Deprecation), TECH_DEBT.md
**Does NOT write to:** `knowledge/` topic files, KNOWLEDGE.md §4 (Project Facts index) — those belong to `/tfw-knowledge`

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
| 5 | New principle or convention? | `conventions.md` | Design Rules / relevant section |
| 6 | Fact Candidates present in RF/REVIEW/RES? | _(no action)_ | They will be processed during next `/tfw-knowledge`. Do NOT consolidate facts here — that is `/tfw-knowledge`'s job. |

## After Update

- Mark in REVIEW: `tfw-docs: Applied — updated Sections 1, 3` or `tfw-docs: N/A (minor)`
- Before a local docs commit, use the adapter-declared surface and the one documented
  task to run:

  ```text
  python .tfw/scripts/commit_identity_router.py route --workflow docs --surface {adapter-surface} --task {TASK-ID} --work docs --role coordinator --operation ordinary --summary "{concise documentation result}" --repo .
  ```

  Use the returned validated subject. Split task-spanning or mixed-task batches into
  truthful task commits, or stop for explicit authority; never collapse them into
  `task:none`.
- Local commit completion and documentation closure are separate from publication
  authority. Do not push unless the user separately and explicitly authorizes it; for
  TFW-49, process F26 keeps publication unavailable until all phases close and the
  user later says `APPROVE PUSH`.

## Orchestration

After tfw-docs completes:
- IF Fact Candidates exist in RF, REVIEW, or RES → recommend: "Run `/tfw-knowledge` to consolidate fact candidates"
- IF no Fact Candidates → mark `tfw-knowledge: N/A` in REVIEW

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
