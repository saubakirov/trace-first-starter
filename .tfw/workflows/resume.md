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

Read this workflow completely, then select inputs in order; shared ranges use unique headings.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | named task/phase state; else `.tfw/project_config.yaml` → `tfw.task_containers` only to resolve it, then `status.md`/`journal/` | state first | task/config |
| 2 | each current phase's own `status.md` and `journal/` when the task is `PHASES` | phase truth without task-level rollup | phase-local |
| 3 | referenced authority/lineage; master HL/TS only if named | governing purpose/scope/artifact | governing artifacts |
| 4 | highest completed/returned REVIEW; RF only for claim detail | verdict/disposition/return | governing artifacts |
| 5 | `.tfw/conventions.md` headings `Task control files`, `Session identity`, `Artifact file naming`, `Task Statuses`, and `The 🔄 REVISE route` | identity/state/route | shared rule |

Indexes/globs/chat/unrelated RF/full libraries are not state; heading/lineage defects stop under `Context Selection`.

## Who Is Acting

Before writing resolve handle: one profile, valid binding, or one question. Never infer; events use human `on_behalf_of` and tool `via`.

## 1. Resolve Current State

1. Resolve the selected task only through the Read Contract.
2. Verify `status.md`; list the referenced governing artifacts and highest valid lineage.
3. If lifecycle is `PHASES`, read every current phase's local state and journal. A missing or
   malformed live phase state is reported and blocks a confident next-stage recommendation.
4. For the latest completed/returned phase, read its live REVIEW. Preserve every recorded
   disposition; never reopen REVIEW §5 as a backlog.
5. After one task resolves, resolve selected/acting principals and mandate root/current actual units;
   apply `LEAD · {handle} · …` only when the central root predicate qualifies this exact `RESUME`
   unit. Same-principal children keep `RESUME` with no handle. Include `PHASE` only when exactly one resolves.
   Act before Matrix/question/stop.

## 2. Build the Matrix

Present one row per declared phase:

| Phase | Description | Authority | Lifecycle | REVIEW verdict | Exact next route |
|---|---|---|---|---|---|

Derive artifacts from state/lineage, not filenames. Report vision, phases, lessons, blockers,
and exact route; REVISE uses the shared rung table.

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
