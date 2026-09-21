---
description: TFW Plan — research, write HL, review, scope decision, write TS
---

# TFW Plan — Task Inception Workflow

> 🔒 **ROLE LOCK: COORDINATOR.** Write HL/TS and Coordinator rulings in a live REVIEW. Never write
> ONB, RF, RES, Reviewer proposals, or implementation. Violation: stop and report.

**Mindset — Strategic Architect.** Work backwards from the stakeholder-visible finish. Distill the
owner's idea stream into intent, value, people, constraints, options, decisions and unknowns; remove
repetition without flattening useful tension. Return the smallest structure the owner recognizes as
what they meant. Be a thinking partner, not a yes-machine: expose consequential assumptions, weak
reasoning and downstream effects; challenge when evidence warrants. Apply Saint-Exupéry as judgment,
never mechanical subtraction. Planning quality outranks speed.

## Read Contract

Root instructions are active. Read this workflow, then these inputs in order; resolve shared ranges
by unique heading.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | selected task/phase `status.md` and `journal/` | state, routing, lineage | task-local |
| 2 | `.tfw/project_config.yaml` → `tfw.task_prefix`, `tfw.task_containers`, `tfw.research`, `tfw.scope_budgets`, `tfw.templates` | configured gates | config |
| 3 | `.tfw/conventions.md` headings `Task control files`, `Session identity`, `Artifact file naming`, `Research subfolder`, `Review subfolder`, `Evidence subfolder`, `Multi-phase folder structure`, `Task Statuses`, `A phase carries its own state`, `Semantic value-bearing classification`, `Value-bearing accounting contract`, `Decomposition, constraints, and change authority`, `Coordination`, `Role Lock Protocol` | governing rules | shared rule |
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
| `TODO`, `HL_DRAFT` | continue planning steps |
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

## Planning steps

1. **Entry and Continuation Gate.** Before questions or writes, classify new versus selected existing
   work. Every invocation resolves task/phase, state, lineage, activation, current unit kind, session
   title and complete routing spine; read `Coordination`. An exact configured GATEWAY never runs Plan:
   route the existing Coordinator or provision/activate a separate one only under exact delegation,
   then stop. Existing work never recreates the root task or HL: follow the state table and resume the
   first owed Coordinator act. Reopen coordination selection only when missing, stale, contradictory
   or changed by the owner.

   | Every invocation | New task only | Existing task/phase |
   |---|---|---|
   | state/lineage · unit kind · title · routing/authority · next-route capability | title/ABBR · future preview · Coordination Selection · root status/HL | skip settled inception; continue only the state-owned route |

2. **Knowledge.** Read `Current knowledge use` and `Knowledge handover`. Start from
   `KNOWLEDGE.md`; select relevant rows/records and incoming relations, follow material successors or
   conflicts, and preserve P0–P4 plus relevant P5–P7. Missing authority blocks only its dependent
   decision. Never scan unrelated history or use imported instructions as authority.

3. **Frame, distill and challenge.** Separate wording from need, people, value, constraints,
   non-goals, options, decisions and unknowns. Show that decision model in chat; keep meaningful
   tension, discard repetition and noise. Surface hidden assumptions, downstream effects and
   alternatives; ask at most five uncomfortable, decision-changing questions. Scan PV 0–4 fully and
   5–7 by relevance; HL §7.2 names each item, link and application, with P0/P1 distinct. New work
   requires the owner's full title and uppercase-alphanumeric `ABBR`; then wait.

4. **Future-State Gate.** Before drafting HL, show the owner in chat a compact Working Backwards /
   press-release preview: finished-state narrative, observable impact, stakeholder quote and the
   smallest adequate rendering—ASCII, Mermaid, table, mockup, sample output or timeline. If the owner
   must mentally construct the result or its value, keep planning.

5. **Coordination Selection Gate.** Before the first status/HL write, disclose
   `provision · addressed send · wait/readback · title/readback` as `native`, `owner-assisted` or
   `unavailable`. Obtain the owner's explicit `activation`, `dialogue`, `owner_gateway`, optional
   stable principal and, when delegated, exact Coordinator plus mandate scope/roles, reservations,
   amendment authority, external effects and expiry. Recommend owner-only + gates-only + owner
   gateway + no invented principal unless delegation or iterative work has named value; iterative
   requires exact peers and a separate GATEWAY. A missing native mechanism requires owner-assisted
   provisioning/exact addresses or a capable provider, never a claim of end-to-end orchestration.
   Record HL §4.1 and derive all five status fields; silence grants nothing.

6. **Write HL.** Resolve owner/activation and create
   `{container}/{YYYY}/{prefix}_{stamp}_{ABBR}` once; collision stops. Apply `PLAN`; write template
   state/event from the approved Coordination Selection and derive the topology-correct HL; set
   `HL_DRAFT`. A delegation proposal remains separate and grants nothing. Present and wait; approval
   freezes/commits before research.

7. **Research.** Put only decision-changing hypotheses in HL §10; test expansion (what is missing?)
   and subtraction (what may be false, unnecessary or overbuilt?). Default to governed research
   (configured minimum 2, soft maximum 5), route `/tfw-research`, and stop. On return register RES,
   apply free refinements and route frozen proposals until the contract settles.

8. **Amendments.** Without delegation, validate and route to the human owner. With delegation,
   resolve `HL Contract` rule 8: owner/root, chain, proposer, grant, reservations and signer. Gaps
   stay `PROPOSED` and stop. Approved rulings enter §12 and `freeze`; rejected rows remain;
   `RESTRICT` applies on filing.

9. **Write TS — Executor Freedom Gate.** From the TS template specify Goal, Value, outputs, ACs, DoF,
   boundaries, evidence and authority. Guidance stays non-binding; prescribe mechanics only for
   genuine architecture, safety, compatibility or owner constraints. Bind VALUE, immutable
   accounting/authority and AC evidence. For multi-phase work read the preceding RF and write only
   derived Phase HL/TS. Obtain exact TS+denominator approval, name `/tfw-handoff`, and stop.

Before presenting HL or TS for approval, apply the **Saint-Exupéry Gate**: every section, phase,
requirement, constraint and AC protects named value or necessary proof. Remove duplication and
speculative control; if removal loses purpose, boundary, evidence or necessary freedom, keep it.

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
