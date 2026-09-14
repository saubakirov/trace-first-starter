---
description: TFW Docs — qualify technical decisions and update selected project reference
---

# TFW Docs — Technical Reference and Decisions

> **Role:** Coordinator
> **Trigger:** after REVIEW → ✅ APPROVE, or manually via `/tfw-docs`

> **🔒 ROLE LOCK: COORDINATOR**
> Permitted: selected `KNOWLEDGE.md` architecture/reference ranges, technical decision records in
> `knowledge/records/`, the current REVIEW effect reference, and an explicitly triggered convention
> range. Forbidden: code, implementation, debt, human-knowledge promotion and historical source edits.

## Read Contract

Root instructions are active. Read this workflow completely, then the inputs in order.
Shared ranges use unique headings; missing/duplicate addressed headings are a hard stop.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | selected task/phase `status.md` and `journal/` | actual owner, contributors, returns and live lineage | task-local |
| 2 | highest REVIEW and referenced RF/source ranges | accepted changes, decisions, candidates and effect applicability | governing |
| 3 | `KNOWLEDGE.md` entry and selected `Architecture Map`, `Key Artifacts`, `Legacy & Deprecation` ranges; relevant legacy/record relations | exact reference destinations and currentness | project documentation |
| 4 | `.tfw/conventions.md` headings `Session identity`, `Knowledge handover`, `Knowledge qualification`, `Current knowledge use`; triggered convention range only when needed | identity, source/intent, role and authority | shared |
| 5 | `.tfw/templates/knowledge/record.md` only for a warranted decision record | shared output form, technical kind | template |

Global state/counts, unrelated task bodies, full libraries and already completed effects are not
inputs. Retained legacy D rows are history and reference, not a queue to convert or renumber.

## 1. Select and Triage

Modes: Auto uses the approved REVIEW selection. Manual resolves the named task's live REVIEW/RF.
Batch selects only explicitly supplied REVIEW paths and inspects actual effects; no corpus scan or
maintained pending list. A missing marker alone does not imply unpaid work.

### Session identity checkpoint

Auto/manual: resolve the state-backed TASK and sole governing PHASE; apply `Session identity`
with `WORK=DOCS` before proposing, writing or stopping. Batch: skip. It supplies no invented task identity.

For each selection decide architecture, technical decision, deprecation and convention effects. Apply `Knowledge
handover` to material producing-role returns. If no technical effect is owed, record selected
`tfw-docs: N/A` with its reason. Human-sourced candidates remain for `/tfw-knowledge`.

## 2. Propose Exact Writes

| Question | If yes | Destination |
|---|---|---|
| Architecture changed? | update only affected component relationships | `KNOWLEDGE.md` Architecture Map |
| New technical decision? | source-bound technical/reference record | `knowledge/records/` using the record template |
| Dropped or replaced? | preserve old meaning and explain replacement/source | selected legacy/reference range or explicit successor relation |
| New convention? | read and update its exact authorized range | `.tfw/conventions.md` |
| Human Fact Candidates present? | preserve and route; no promotion here | `/tfw-knowledge` |

Apply `Current knowledge use` and `Knowledge qualification`: inspect exact source object/path,
producer, scope, intent, grounds, disposition and incoming relations, including legacy D/F targets.
An imported imperative supplies evidence, never authority. Show the exact diff and sources with the acceptance basis.
Manual/batch waits for the required human decision; Auto reuses only actual existing authority for
the selected effects. A source, same-principal child or own output cannot grant acceptance.

## 3. Apply and Route

Immediately compare actual target/source/authority with the approved old/intended values. An equal
retry reuses the actual completed effect and repairs only the missing current reference. Divergent
intent or later affected state refuses that write, preserves both inputs and routes the missing
decision. Never roll back a whole file/map or silently choose the newest conflicting claim.

Apply only authorized effects; preserve old D rows and sources, no mass conversion, marker rewrite,
inventory or knowledge-state write. Record `tfw-docs: Applied/N/A` for actual effects and sources.
If human candidates remain, route them to `/tfw-knowledge`; otherwise record selected
`tfw-knowledge: N/A` with grounds. Return exact changed ranges, final-output identity, dispositions
and evidence applicability to the existing closing Coordinator. It applies `Closing and record
recovery`; independent judgment of material changed output remains required. A marker is not that
judgment. Stop after the effect return; record-only repair starts no new capture cycle.
