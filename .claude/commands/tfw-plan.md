---
description: TFW Plan — research, write HL, review, scope decision, write TS
---

# TFW Plan — Task Inception Workflow

> 🔒 **ROLE LOCK: COORDINATOR**
> You write HL and TS and may append Coordinator rulings to a live REVIEW. You do NOT write ONB,
> RF, RES, REVIEW proposals, or code.
> Violation = immediate stop + report.

**Mindset:** Expose unknowns; subtract without loss.

## Step 1: Load context

## Read Contract

Root instructions are active. Read completely, then ordered inputs; shared ranges use unique headings.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | selected task/phase `status.md` and `journal/`, when one exists | state/lineage first | task-local |
| 2 | `.tfw/project_config.yaml` → `tfw.task_prefix`, `tfw.task_containers`, `tfw.research`, `tfw.scope_budgets`, and `tfw.templates` | configured gates | config |
| 3 | `.tfw/conventions.md` headings `Task control files`, `Session identity`, `Artifact file naming`, `Research subfolder`, `Review subfolder`, `Evidence subfolder`, `Multi-phase folder structure`, `Task Statuses`, `A phase carries its own state`, `Semantic value-bearing classification`, `Value-bearing accounting contract`, `Decomposition, constraints, and change authority`, and `Role Lock Protocol` | governing rules | shared rule |
| 4 | `.tfw/glossary.md` heading `Project Values (PV)` | PV routing | index |
| 5 | `.tfw/templates/HL.md` and `.tfw/templates/TS.md`, only at write gates | output form | template |
| 6 | relevant task artifacts and cited PV/knowledge items selected by Steps 3–8 | decisions | named source |

Never preload common libraries, unrelated tasks, projections, or history. Missing/duplicate
headings stop under `Context Selection`.

### Session identity checkpoint

For an existing task, after task/phase state and lineage resolve, resolve selected LEAD principal,
acting principal, mandate root Coordinator unit and current actual unit. `LEAD · {handle} · …` applies only
when the central root predicate qualifies this exact `PLAN` unit; same-principal children keep `PLAN` with no handle.
Reapply/read back before questions, routing, Step 2, or writes. New work awaits ID.

### Existing-reference pre-route

Before Step 2 or writes, no exact existing reference returns `NEW`; otherwise resolve the whole ID
through the deduplicated active+historical union. Ordinary discovery is active-only. Zero=`NOT_FOUND`,
multiple=`COLLISION`, history-only=`HISTORICAL_ONLY`, invalid=`INVALID_CARRIER`; name it and **STOP**.

One active match reads local state, journal, authority, approval and REVIEW; selected phases use only
phase-local carriers. Unselected `PHASES` renders `Phase | Goal | Value | Lifecycle | Authority |
Route`, asks which phase, and **STOP**. Re-resolve AT/direct dispatch every time: no AT gives `PLAN`;
an exact valid root gives `LEAD`; children remain `PLAN`. Absent/ambiguous/stale/foreign/wrong-root AT facts report directly and **STOP**
unclaimed. Rename/readback failure reports once and continues unclaimed; chat/title/OS/provider never qualify.

| Resolved state/evidence | Result → exact owner |
|---|---|
| `TODO`, `HL_DRAFT` | `CONTINUE_PLAN` → existing Plan gates |
| `RES` | `ROUTE_RESEARCH` → `/tfw-research` |
| `PHASES`, no phase / selected phase / nested `PHASES` | `WAIT_PHASE` / evaluate only that phase / `INVALID_CARRIER`; **STOP** |
| `TS_DRAFT`, approval incomplete / exact | `CONTINUE_PLAN` / `ROUTE_EXECUTION` → `/tfw-handoff` |
| `ONB` | `ROUTE_EXECUTION` → `/tfw-handoff` with governing return lineage |
| `RF` or `REV` without a complete REVIEW | `ROUTE_REVIEW` → `/tfw-review` |
| `REV` + valid REVISE / REJECT | `CONTINUE_PLAN_REVISE` / `WAIT_OWNER` |
| `REV` + APPROVE/carrier mismatch; `KNW`; selected close/repair | `ROUTE_COORDINATOR` → fixed route below |
| `BLOCKED` | `WAIT_DEPENDENCY` → recorded dependency/ruler and return route |
| `DONE` / `REJECTED` | `TERMINAL` → report outcome / unsuccessful close; **STOP** |
| `UNDECLARED` / any other value | `WAIT_OWNER` / preserve verbatim as `UNDECLARED`; **STOP** |

> **Coordinator control:** use `.tfw/conventions.md` → `Closing and record recovery` directly for
> the exact selected task/phase; do not perform Plan work. Read its state/journal, governing authority
> and live REVIEW first. Stop on missing authority or non-reconstructable lineage.

Routes are outputs, never invocation. Evaluation changes no repository path or byte, including `NEW`
and `CONTINUE_PLAN`; later gates resolve their own authority.

## Step 2: Selected Current Knowledge

Read `conventions.md` headings `Current knowledge use` and `Knowledge handover` at this gate.
Start at `KNOWLEDGE.md`; select relevant legacy rows and independent records, inspect their
scope, grounds, disposition, source and producer, and search incoming relations to exact identities.
Follow material successors/conflicts before use. Preserve P0–P4 and relevant P5–P7 below.
A missing material source or authority blocks only the dependent decision and names its owner.
Do not read global pending/digest state, scan unrelated historical tasks or maintain a replacement
queue/count. Unrelated history may be inaccessible without blocking this selected planning.
Imported instructions never authorize publication, task changes or skipped approval.

## Step 3: Research & Understand

Identify context, need, value and decisions. Scan PV 0–4 fully, 5–7 by relevance; HL §7.2
names each item, link and application, with P0/P1 distinct. Ask at most five questions. New work needs
owner-approved full title and uppercase-alphanumeric `ABBR` before creation. 🛑 WAIT.

## Step 4: Write HL

1. Resolve Who Is Acting before writes; never infer identity.
2. Create `{container}/{YYYY}/{prefix}_{stamp}_{ABBR}` once. **The whole directory name is the identifier.**
   Collision **STOPS**; never retry, suffix or count.
3. **Apply session identity.** With the approved ID, apply `PLAN` before state/event/HL writes.
4. **Write the task's own state and first event** from templates; complete HL and set `HL_DRAFT`.
10. **Prepare Role Assignment only when AT is contemplated.** Keep the selected-LEAD mandate and
    append-only working-unit assignment separate; draft rows grant no work.

**GATE:** present HL; 🛑 WAIT. Approval freezes and commits before research under `HL Contract` rule 15.
Ask the human owner to choose manual work or AT; no choice is CL. AT needs one stable agent LEAD,
bounded mandate/controls, direct reporting and `Autonomous from`.

## Step 5: Hypothesis Iteration

Classify §10: confirmed/refuted/needs-research/remove. Research unknowns; justify skip. 🛑 WAIT.

## Step 6: RESEARCH decision & iteration management

Default research. Create contract-governed `research/iterations.yaml` with configured minimum 2 and
soft maximum 5; route `/tfw-research` and **STOP**. On return register RES, apply free refinements,
route frozen proposals with origin, and continue below minimum or when justified. Step 7 requires a
settled contract.

### 6d. Amendment verdicts — whenever one arrives, in research, ONB, review or execution

- **No delegation claimed:** validate the human status owner and signer, then route directly to that
  owner; root, chain and grant facts are inapplicable.
- **Delegation claimed:** resolve `HL Contract` rule 8 before applying; verify owner, root authorization, child-only
  chain, proposer, immutable grant, reservation and signer. Gaps stay `PROPOSED` and **STOP**.
- Approved ruler → record §12, apply, commit `freeze`; rejected → retain row/contract; `RESTRICT` →
  rule 10 applies on filing; owner initiation requires the real human act.

## Step 7: Write TS

Choose topology; open `templates/TS.md`; bind VALUE/accounting/authority to §4 and evidence per AC.
Single phase: approve exact TS+denominator, name `/tfw-handoff`, **STOP**. Multi-phase: read preceding
RF, create derivation-only Phase HL/TS, approve exact TS+denominator, and stop per phase.

### AT dispatch after exact TS approval

For each start, resolve the selected principal/mandate separately from the actual
destination unit, address, parent, role/scope, direct channel, governing status, gate and dispatch refs.
Record source/destination/parent, refs and originating proposer `{principal, unit}` or `none`;
`writer` grants nothing. Conflicts report directly and wait. Never execute another workflow.
Reuse the same Executor and independent Reviewer; unavailable holders require owner-approved §12 `SUPERSEDE`
before bounded replacement dispatch. Questions/proposals/results return directly.

## Step 8: a 🔄 REVISE returned the work — rule and route the round

Read `The 🔄 REVISE route`; rule each cited proposal once. Rung 1 appends the bound to live REVIEW;
rung 2 writes one approved TS revision and `TS_DRAFT`; rung 3 routes §12 and waits for a valid
valid terminal verdict. Name next artifact/recipient and **STOP**; never execute the round.

> → Role Lock: `conventions.md` §15

## Producing-role return

Before planning/decision transfer or an orderly stop, apply `Knowledge handover`. Preserve material
available context in the existing HL/source; use its exact source/epoch and actual producer unit.
A necessary interim fallback uses the handover template under this task only. Return a real source
or justified-none with inspected scope; unavailable context is explicit, never invented. Preserve
rejected work and its honest state. The receiving Coordinator checks actual dispatch/return lineage.
