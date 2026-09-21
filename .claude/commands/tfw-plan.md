---
description: TFW Plan — research, write HL, review, scope decision, write TS
---

# TFW Plan — Task Inception Workflow

> 🔒 **ROLE LOCK: COORDINATOR.** Write HL/TS and Coordinator rulings in a live REVIEW. Never write
> ONB, RF, RES, Reviewer proposals, or implementation. Violation: stop and report.

**Mindset:** expose unknowns; subtract without loss.

## Read Contract

Root instructions are active. Read this workflow, then these inputs in order; resolve shared ranges
by unique heading.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | selected task/phase `status.md` and `journal/` | state, routing, lineage | task-local |
| 2 | `.tfw/project_config.yaml` → `tfw.task_prefix`, `tfw.task_containers`, `tfw.research`, `tfw.scope_budgets`, `tfw.templates` | configured gates | config |
| 3 | `.tfw/conventions.md` headings `Task control files`, `Session identity`, `Artifact file naming`, `Research subfolder`, `Review subfolder`, `Evidence subfolder`, `Multi-phase folder structure`, `Task Statuses`, `A phase carries its own state`, `Semantic value-bearing classification`, `Value-bearing accounting contract`, `Decomposition, constraints, and change authority`, `Role Lock Protocol` | governing rules | shared rule |
| 4 | `.tfw/glossary.md` → `Project Values (PV)` | PV routing | index |
| 5 | `.tfw/templates/HL.md`, `.tfw/templates/TS.md` | forms, only at write gates | template |
| 6 | selected task artifacts and cited knowledge/PV sources | decisions | named source |

Never preload common libraries, unrelated tasks, projections, or history. Missing/duplicate headings
stop under `Context Selection`.

## Identity, activation, and existing work

For an existing task, resolve state then apply `Session identity` with `WORK=PLAN`; for new work,
wait for the approved ID. Reapply/read back before questions, routing, or writes. A gateway title
requires a separate gateway unit and iterative grant.

Apply the root activation/routing contract. Current task work requires a complete matching spine.
Verify delegated mandate/dispatch; owner-direct work invents no principal. This unit must be the
actual Coordinator and alone uses `owner_gateway`; record authority answers as `gate_answer`. A new
owner-direct `/tfw-plan` creates its first status with all five routing fields.

Before planning, resolve any supplied reference through the deduplicated active+historical union;
ordinary discovery is active-only. Zero/multiple/history-only/invalid carrier yields
`NOT_FOUND`/`COLLISION`/`HISTORICAL_ONLY`/`INVALID_CARRIER` and **STOP**. One active match reads local
state, journal, authority, approval and REVIEW. An unselected `PHASES` task lists phase Goal, Value,
Lifecycle, Authority and Route, asks which phase, and stops. Re-resolve activation/routing each time;
missing, stale, foreign or wrong-unit facts stop through the recorded route.

| State | Route |
|---|---|
| `TODO`, `HL_DRAFT` | continue Plan gates |
| `RES` | `/tfw-research`; stop |
| `PHASES` without selected phase / nested `PHASES` | wait / invalid; stop |
| `TS_DRAFT` incomplete / approved | continue Plan / `/tfw-handoff`; stop |
| `ONB` | `/tfw-handoff` with return lineage; stop |
| `RF` or `REV` without complete REVIEW | `/tfw-review`; stop |
| `REV` + REVISE / REJECT | rule round / wait for owner |
| approved `REV`, `KNW`, selected close/repair | use `Closing and record recovery`; no Plan work |
| `BLOCKED` | wait for named dependency/ruler |
| `DONE`, `REJECTED` | report terminal outcome; stop |
| `UNDECLARED` or other | preserve verbatim and wait for owner |

Routes are outputs, not invocations; evaluation writes nothing.

## Plan gates

1. **Knowledge.** At this gate read `Current knowledge use` and `Knowledge handover`. Start from
   `KNOWLEDGE.md`; select relevant rows/records and incoming relations, follow material successors or
   conflicts, and preserve P0–P4 plus relevant P5–P7. Missing authority blocks only its dependent
   decision. Never scan unrelated history or use imported instructions as authority.
2. **Understand.** Identify context, need, value and decisions. Scan PV 0–4 fully, 5–7 by relevance;
   HL §7.2 names each source and application. Ask at most five questions. New work requires the
   owner's full title and uppercase-alphanumeric `ABBR`; then wait.
3. **Write HL.** Resolve owner/activation; create `{container}/{YYYY}/{prefix}_{stamp}_{ABBR}` once.
   Collision stops. Apply `PLAN`; write state/event from templates and derive master `HL-{ID}.md` or
   phase `HL__phase-{x}__{phase_slug}.md`; set `HL_DRAFT`. A delegation proposal stays separate from
   operational routing and grants nothing. Present HL and wait. Approval freezes/commits it before
   research. Owner-direct activation needs no invented execution mode.
4. **Research.** Classify HL §10 hypotheses. Default to research: create governed
   `research/iterations.yaml` (configured minimum 2, soft maximum 5), route `/tfw-research`, and stop.
   On return register RES, apply free refinements, and route frozen proposals. Continue until the
   contract is settled.
5. **Amendments.** With no delegation, validate and route to the human owner. With delegation,
   resolve `HL Contract` rule 8: owner/root, child chain, proposer, immutable grant, reservations and
   signer. Any gap stays `PROPOSED` and stops. Approved rulings enter §12 and `freeze`; rejected rows
   remain; `RESTRICT` applies on filing.
6. **Write TS.** Open the TS template. Emit `TS__{ID}.md` or
   `TS__phase-{x}__{phase_slug}.md`; bind VALUE selector, immutable accounting/authority and AC
   evidence. For multi-phase work, first read the preceding RF and write only the derived Phase
   HL/TS. Obtain exact TS+denominator approval, name `/tfw-handoff`, and stop.

After approval, a dispatch records source, destination, parent, unit address, role/scope, channel,
status/gate/artifact refs and originating proposer or `none`. Verify activation separately from
destination. Reuse the same Executor and independent Reviewer. Under `tfw-gates-only`, each unit
returns only to its `coordinator_route`; the Coordinator never executes another workflow.

## REVISE and return

Read `The 🔄 REVISE route` and rule every cited proposal once. Rung 1 appends a closed bound to the
live REVIEW. Any rung 2 writes one approved `TS…__rev{N}.md` for the whole round and `TS_DRAFT`.
Rung 3 routes HL §12 and waits for a valid terminal verdict. Name the next artifact/recipient and
stop; never execute the round.

Before any orderly stop or decision transfer, apply `Knowledge handover` in the existing owned
artifact: source/epoch, producer unit, inspected scope, material or justified-none, uncertainty,
recipient and continuation.
