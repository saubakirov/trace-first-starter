---
description: TFW Docs — update KNOWLEDGE.md sections 1-3 after review
---

# TFW Docs — Knowledge Update Workflow

> **Role:** Coordinator
> **Trigger:** after REVIEW → ✅ APPROVE, or manually via `/tfw-docs`

> **🔒 ROLE LOCK: COORDINATOR**
> Permitted: `KNOWLEDGE.md` §§1–3, the selected REVIEW marker, and a convention range only when
> checklist item 4 fires. Forbidden: code, implementation, debt, `KNOWLEDGE.md` §4, and topic files.

## Read Contract

Root instructions are already active. Read this workflow completely, then read in order. Shared
ranges are addressed by unique Markdown heading.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | selected task/phase `status.md` and `journal/` | current state and live lineage | task-local |
| 2 | highest REVIEW and the RF it references | verdict, markers, changes, decisions, and candidates | governing artifacts |
| 3 | `KNOWLEDGE.md` headings `Architecture Map`, `Key Artifacts`, and `Legacy & Deprecation`, each once | current documentation and exact write destinations | project documentation |
| 4 | only the named conventions heading when checklist item 4 fires | existing rule before a convention update | shared rule |

`KNOWLEDGE.md` §4, `knowledge/*.md`, debt, full conventions/glossary, unrelated task bodies, and
already processed REVIEWs are not inputs. Missing/duplicate addressed headings are a hard stop.

## 1. Select and Triage

Modes:

- Auto: the approved REVIEW already selected the task.
- Manual: `/tfw-docs {TASK-ID}` resolves that task's live REVIEW/RF.
- Batch: `/tfw-docs --scan` selects only REVIEWs without a `tfw-docs:` marker.

For each selection decide whether it is significant: architecture change, D-record-worthy decision,
deprecation, or new convention/principle. If no, write `tfw-docs: N/A (minor)` in REVIEW. If yes,
continue.

## 2. Propose Exact Writes

| Question | If yes | Destination |
|---|---|---|
| Architecture changed? | update the map | `KNOWLEDGE.md` §1 |
| New decision? | add a D-record | `KNOWLEDGE.md` §1, Architecture Decisions |
| Dropped or replaced? | add a legacy row | `KNOWLEDGE.md` §3 |
| New principle/convention? | update only its named range after reading it | `.tfw/conventions.md` |
| Fact Candidates present? | no write here; route later | `/tfw-knowledge` |

Show the exact diff and sources. Manual and batch modes wait for human approval before applying;
Auto may use the approval already recorded by its enclosing review flow. Never consolidate facts or
create debt here.

## 3. Apply and Route

Apply only the approved rows. Mark the live REVIEW `tfw-docs: Applied — updated Sections …` or the
N/A form. Commit with the task changes, not as an unrelated documentation commit.

If Fact Candidates remain, recommend `/tfw-knowledge`; otherwise mark
`tfw-knowledge: N/A`. Stop after reporting changed ranges and the marker.
