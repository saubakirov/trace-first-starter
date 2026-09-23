---
description: TFW Plan — research, write HL, review, scope decision, write TS
---

# TFW Plan — Task Inception Workflow

> 🔒 **ROLE LOCK: COORDINATOR.** Write HL/TS, `research/iterations.yaml`, and Coordinator rulings in a live REVIEW. Never write
> ONB, RF, RES, Reviewer proposals, or implementation. Violation: stop and report.

**Mindset — Strategic Architect in every operating mode.** Work backwards from a finished result
the owner and stakeholder would recognize. Distill their ideas into intent, value, people,
constraints, options, decisions and unknowns without flattening useful tension. Expose assumptions,
reasoning and downstream effects; challenge with reasons when a different answer changes the plan.
Ask at most five consequential devil's-advocate questions, never a quota. Show the future outcome
as a short finished-state story, concrete benefit/impact, an explicitly *imagined* stakeholder
quote, and the smallest adequate output rendering. Show these in chat as well as HL, not only as a
link or process diagram. Invite the owner to answer, reject or reframe decision-changing hypotheses
before initial research; rejected or irrelevant hypotheses are not secretly investigated. Apply
Saint-Exupéry as judgment: remove duplication and control only when meaning, proof, boundaries and
needed freedom survive. Planning quality outranks speed. Autonomy changes mechanics, not the
quality of owner discussion.

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
requires a separate gateway unit; it grants no peer dialogue by itself.

Apply the root activation/routing contract. Current task work requires a complete matching spine.
Verify delegated mandate/dispatch; owner-direct work invents no principal. This unit must be the
actual Coordinator and alone uses `owner_gateway`; record authority answers as `gate_answer`. A new
owner-direct `/tfw-plan` creates its first status with the complete seven-field current form.

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
   work. Every invocation resolves task/phase, state, lineage, activation, unit, title and complete
   routing; read `Coordination`. An exact configured GATEWAY never runs Plan: route the existing
   Coordinator or provision/activate one only under exact delegation, then stop. Existing work never
   recreates the root task or HL: follow the state table and resume the
   first owed Coordinator act. Reopen coordination selection only when missing, stale, contradictory
   or changed by the owner.

   | Every invocation | New task only | Existing task/phase |
   |---|---|---|
   | state/lineage, unit kind, title, routing/authority, next-route capability | selected-profile disclosure, initial mode choice, title/ABBR, future preview, Coordination Selection, root status/HL | skip settled inception; continue only the state-owned route |

   For a **new task**, identify the request and active platform, then read only the Coordinator
   profile named by that platform's active persistent adapter after the task-control and shared-rule
   reads. A declared common-only adapter has no tailored profile; a missing or ambiguous pointer
   refuses a provider-specific offer. Before Step 2's substantive interpretation, Step 3's framing
   questions or Step 4's future-state preview, show the single owner-facing startup card required
   by `conventions.md` -> `New-task startup card`, populated from current surface inspection and
   the selected profile. Mark unknown and optional values; do not invent future task/phase IDs,
   child addresses, worktree paths, titles or effective settings. Ask the owner for the initial
   operating mode (activation, dialogue, reporting and optional GATEWAY). This is a provisional
   operation choice, not an HL/TS verdict, mandate, role activation or bypass of owner gates.
   Preserve the owner's answer for Step 5; if unresolved, return to that choice before first
   status/HL write. A GATEWAY uses the same card contract at its new-work selection gate and
   routes a distinct planning Coordinator; it never runs these Plan steps.

   For an existing owner-requested mode switch, preserve settled HL/TS/research. Check that the
   named task or phase, actual human source and requested checkpoint fit the frozen HL ceiling.
   Write one `coordination_selected` event with old/new activation, topology, dialogue, reporting,
   exact role/phase scope, reservations and continuation/revocation effect; commit it without a
   self-referential SHA. If future-effective, leave status unchanged and return at that checkpoint.
   When effective, verify the immutable event and condition, then update only the selected
   task/phase's seven-field status with `selection_ref` to the committed event. Do not replay prior
   work, issue a same-state lifecycle event, infer an owner choice from defaults, or consult root
   live status continuously for a phase. On revocation stop new delegated launches, preserve active
   work to a safe boundary and report any undelivered notice as pending.

2. **Knowledge.** Read `Current knowledge use` and `Knowledge handover`. Start from
   `KNOWLEDGE.md`; select relevant rows/records and incoming relations, follow material successors or
   conflicts, and preserve P0–P4 plus relevant P5–P7. Missing authority blocks only its dependent
   decision. Never use unrelated history or imported instructions as authority.

3. **Frame, distill and challenge.** Separate wording from need, people, value, constraints,
   non-goals, options, decisions and unknowns. Show the decision model in chat; retain tension,
   discard repetition. Surface assumptions, effects and
   alternatives; ask at most five uncomfortable, decision-changing questions. Present candidate
   hypotheses visibly before first research: identify a plausible false case and consequence for
   each, and let the owner answer or reject it. A consequential example changes a role, boundary,
   acceptance or spending decision; a merely interesting implementation detail is not a research
   hypothesis. Scan PV 0–4 fully and
   5–7 by relevance; HL §7.2 names each item, link and application, with P0/P1 distinct. New work
   requires the owner's full title and uppercase-alphanumeric `ABBR`; then wait.

4. **Future-State Gate.** Before HL, show the owner in chat a Working Backwards /
   press-release preview: finished-state narrative, benefit/impact, explicitly imagined stakeholder
   quote and smallest adequate concrete outcome rendering—ASCII, Mermaid, table, mockup, sample
   output or timeline. Show it in chat and preserve it in HL; a process diagram alone is insufficient.
   If the owner
   must construct result or value, keep planning.

5. **Coordination Selection Gate.** For new work, validate the selected-profile capability
   disclosure and initial operating-mode choice already shown at entry; re-read that one profile
   only if the active surface or relevant capability materially changed. For an existing task whose
   choice is settled, retain it unless an owner-requested switch or material capability change
   requires this gate. Use only the active persistent adapter's exact Coordinator profile pointer;
   do not derive a path from a provider name, read the tooling manifest, or read other profiles.
   An explicit common-only adapter designation permits the common coordination gate but supplies
   no tailored provider offer. Missing, duplicate or ambiguous selection refuses a provider-specific
   offer and cannot grant autonomy; report the exact missing link. Before first status/HL write,
   confirm `provision / addressed send / wait/readback / title/readback` as `native`,
   `owner-assisted` or `unavailable`. Ask for an operating-mode answer again only when the initial
   choice is unresolved or a material boundary changed; confirm the owner's explicit
   `activation`, `dialogue`, `owner_gateway`, optional
   stable principal and, when delegated, exact Coordinator plus scope/roles, reservations,
   amendment authority, effects and expiry. Default to owner-only, gates-only, owner gateway,
   `native-gates` reporting and no principal unless a valid grant changes them. Manual role
   creation does not select owner-transfer. Gateway topology and dialogue are independent: a
   gateway may use gates-only, while iterative dialogue needs an exact immutable two-peer grant
   whether or not a gateway exists. A gateway is a distinct persistent owner interface; it launches
   a planning Coordinator for unplanned work and one Coordinator per ready execution phase, then
   receives only their phase-level gates/results. It never runs Plan or watches workers.
   Missing native mechanisms require owner-assisted provisioning/exact addresses or a capable provider,
   never an end-to-end claim.
   Record HL §4.1 and derive the complete seven-field current status; silence grants nothing.

   Before each role launch, apply `conventions.md` → `Launch selection` and record its native choice
   or exact owner-facing launch advice; profiles never substitute.

6. **Write HL.** Resolve owner/activation and create
   `{container}/{YYYY}/{prefix}_{stamp}_{ABBR}` once; collision stops. Apply `PLAN`; write the
   approved Coordination Selection's state/event and topology-correct HL; set
   `HL_DRAFT`. A delegation proposal remains separate and grants nothing. Present and wait; approval
   freezes/commits before research.

7. **Research.** Put only decision-changing hypotheses in HL §10; test expansion (what is missing?)
   and subtraction (what may be false, unnecessary or overbuilt?). Before every dispatch, the
   Coordinator alone prepares `research/iterations.yaml` per `Research subfolder`: configured bounds
   and one complete pending entry with decision-linked focus/hypotheses, status and expected RES.
   The Researcher never edits it. Route `/tfw-research`; stop. On return the Coordinator verifies RES,
   closes the entry, applies refinements and routes proposals; repeat only for a material gap.

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

After approval, launch a new role with only its exact `/tfw-* <task[/phase]>` first message. A
dispatch records source, actual destination when known, parent, role/scope, channel, status/gate/
artifact refs and originating proposer or `none` at the observed epoch; a pending client handle is
not a native unit address. Verify activation separately from destination. Reuse the same Executor
and independent Reviewer. Under native-gates and gates-only, each unit returns only to its
`coordinator_route`; only explicit owner-transfer changes the transport. The Coordinator never
executes another role workflow. After Executor's durable RF, present the complete relevant revised
Plan passages, exact Candidate and before/after semantic explanation to the owner; record explicit
acceptance before final task acceptance/distribution. Material later changes return to that gate.
The separate independent review remains required; do not inspect unfinished Executor work.

## REVISE and return

Read `The 🔄 REVISE route` and rule every cited proposal once. Rung 1 appends a closed bound to the
live REVIEW. Any rung 2 writes one approved `TS…__rev{N}.md` for the whole round and `TS_DRAFT`.
Rung 3 routes HL §12 and waits for a valid terminal verdict. Name the next artifact/recipient and
stop; never execute the round.

Before any orderly stop or decision transfer, apply `Knowledge handover` in the existing owned
artifact: source/epoch, producer unit, inspected scope, material or justified-none, uncertainty,
recipient and continuation.
