---
description: TFW Resume — locate task, build status matrix, decide next phase
---

# TFW Resume — Phase Status Bootstrap

> **Role:** Coordinator (new or returning)
> **Output:** Phase status matrix and recommendation

> **🔒 ROLE LOCK: COORDINATOR**
> Permitted: read-only status analysis, then Phase HL/TS only after the user selects planning.
> Forbidden: execution, ONB, RF, RES, REVIEW, and code changes.

## Read Contract

Root instructions are already active. Read this workflow completely, then select inputs in order.
Every shared range is addressed by its unique Markdown heading.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | user-named task/phase `status.md` and `journal/`; otherwise `.tfw/project_config.yaml` → `tfw.task_containers` solely to resolve the task, then its `status.md` and `journal/` | current state before derived or global material | task-local/project config |
| 2 | each current phase's own `status.md` and `journal/` when the task is `PHASES` | phase truth without task-level rollup | phase-local |
| 3 | the authority and artifact lineage referenced by those state/event files; master HL/TS only when the lineage names them | governing purpose, scope, and highest valid artifact | governing artifacts |
| 4 | highest REVIEW for the last completed or returned phase; its referenced RF only when a claim must be expanded | verdict, lessons, dispositions, and return basis | governing artifacts |
| 5 | `.tfw/conventions.md` headings `Task control files`, `Artifact file naming`, `Task Statuses`, and `The 🔄 REVISE route` | authority, lineage, state meaning, and return routing | shared rule |

Derived indexes, obsolete `HL__Phase*`-style globs, chat memory, unrelated RF files, and full
common libraries are not state inputs. Missing/duplicate addressed headings or contradictory
state/lineage are a hard stop under `conventions.md` → `Context Selection`.

## Who Is Acting

Resolve the acting handle before the first durable write: one `team/` profile is used silently;
several use the valid per-machine binding; otherwise ask exactly one short question. Never infer
identity. Every event uses a human `on_behalf_of` and optional tool `via`. → `conventions.md`,
`Which handle a machine acts as`.

## 1. Resolve Current State

1. Resolve the selected task only through the Read Contract.
2. Verify `status.md`; list the referenced governing artifacts and highest valid lineage.
3. If lifecycle is `PHASES`, read every current phase's local state and journal. A missing or
   malformed live phase state is reported and blocks a confident next-stage recommendation.
4. For the latest completed/returned phase, read its live REVIEW. Preserve every recorded
   disposition; never reopen REVIEW §5 as a backlog.

## 2. Build the Matrix

Present one row per declared phase:

| Phase | Description | Authority | Lifecycle | REVIEW verdict | Exact next route |
|---|---|---|---|---|---|

Derive artifact presence from state references and valid lineage, not filename guesses. Report the
master vision, completed phases, latest lessons, blockers, and the recommended next phase or return
route. A REVISE uses the shared rung table exactly.

## 3. User Decision Gate

Ask: **“Start planning Phase X?”** or **“Which phase should we work on?”** Then stop. Phase order is
not assumed.

After the user chooses, enter `/tfw-plan` for the selected phase. After its approved TS use
`/tfw-handoff`; after RF use `/tfw-review`.

## Anti-patterns

- planning before the matrix and user decision;
- treating a derived index or filename glob as state;
- reading every RF or inheriting disposed debt;
- writing Executor/Reviewer artifacts or implementation.
