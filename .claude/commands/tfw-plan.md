---
description: TFW Plan — research, write HL, review, scope decision, write TS
---

# TFW Plan — Task Inception Workflow

> 🔒 **ROLE LOCK: COORDINATOR**
> You write HL and TS and may append Coordinator rulings to a live REVIEW. You do NOT write ONB,
> RF, RES, REVIEW proposals, or code.
> Violation = immediate stop + report.

**Mindset:** Architect before proposing: visualize the finish (§3.1), expose unknowns (§10), challenge assumptions, and apply Saint-Exupéry as judgment, never mechanical subtraction. Planning quality outranks pipeline speed.

## Read Contract

Root instructions are already active. Read this workflow completely; then use this ordered
contract. Every shared range is addressed by its unique Markdown heading.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | selected task/phase `status.md` and `journal/`, when one exists | current state and lineage before global material | task-local |
| 2 | `.tfw/project_config.yaml` → `tfw.task_prefix`, `tfw.task_containers`, `tfw.knowledge`, `tfw.research`, `tfw.scope_budgets`, and `tfw.templates` | exact task, gate, research, VALUE, authority, and template values | project config |
| 3 | `.tfw/conventions.md` headings `Task control files`, `Session identity`, `Artifact file naming`, `Research subfolder`, `Review subfolder`, `Evidence subfolder`, `Multi-phase folder structure`, `Task Statuses`, `A phase carries its own state`, `Semantic value-bearing classification`, `Value-bearing accounting contract`, `Decomposition, constraints, and change authority`, and `Role Lock Protocol` | attribution, session identity, topology, lifecycle, VALUE contract, writer authority | shared rule |
| 4 | `.tfw/glossary.md` heading `Project Values (PV)` | independent P0–P4 scan and relevant P5–P7 routing | routing index |
| 5 | `.tfw/templates/HL.md` and `.tfw/templates/TS.md`, only at their write gates | output form | template |
| 6 | relevant task artifacts and cited PV/knowledge items selected by Steps 3–8 | task-specific decisions, not permanent preload | named source |

Full `conventions.md`, full `glossary.md`, full `KNOWLEDGE.md`, unrelated tasks, derived
indexes, and historical traces are not inputs unless a named conflict or compatibility check
triggers their exact range. Missing or duplicate addressed headings are a hard stop under
`conventions.md` → `Context Selection`.

## Step 1: Load context

Apply the Read Contract above. Root and skill instructions are already active; do not reload
them or any full common library. Load each template only when its write gate is reached.

### Session identity checkpoint

For an existing task, after task/phase state and lineage resolve, resolve selected LEAD principal,
acting principal, mandate root Coordinator unit and current actual unit. Apply `Session identity` as
`LEAD · {handle} · …` only when the central root predicate qualifies this exact `PLAN` unit;
same-principal children keep `PLAN` with no handle. Do this before the Knowledge Gate, questions or
proposals. If no task exists, defer identity until Step 4 creates its approved ID.

## Step 2: Knowledge Gate

1. Read `tfw.knowledge.gate_mode` and `interval` from `.tfw/project_config.yaml`.
2. Open `.tfw/workflows/knowledge.md` at the unique heading `Canonical Knowledge Gate algorithm`
   and execute it exactly. It is the complete semantic, tool-independent Full route;
   do not substitute a generated index or optional upstream diagnostic.
3. If it reports any problem or removed task, **HARD STOP** and name every trace problem. Do
   not compute a threshold over unresolved input.
4. Let `delta` be the number of distinct pending task IDs. Zero is an explicit no-op.
5. In `off` mode, skip; in `soft` mode, report `delta/interval` and continue.
6. In `hard` mode, when `delta >= interval`, **STOP** and route to `/tfw-knowledge`:
   "Knowledge consolidation overdue ({delta} pending tasks; interval {interval})."
   Below the threshold, continue.

## Step 3: Research & Understand

1. **Identify context** — read relevant code, existing HL files, knowledge items
2. **Define the need** — separate breakage, gaps, requests, and actual value
3. **Study references** — how similar problems were solved before (existing Architecture Decisions)
4. **Scan Project Values (PV)** — the `glossary.md` PV Index: priorities 0-4 in full, 5-7 by relevance.
      Fill HL §7.2 Knowledge Citations with the exact clause/item read, a link, and its concrete
      application. Record priority 0 and priority 1 as distinct semantic items even when they share
      a file; a file-only citation is insufficient. Explicit N/A is allowed only after the required
      scan and must state why. New projects add: "No applicable knowledge items — project in bootstrap phase."
5. **Ask clarifying questions** — batch all questions, max 3-5. When this exchange will
   establish a new task, propose the **full title and its initials together**: `ABBR` is the
   acronym of the title's significant words, uppercase alphanumeric — *Conflict Resistant
   Shared Workspace* → `CRSW`, *Assisted 1.5 core and synchronization* → `ASSISTED15`. The
   owner approves both in this exchange, before any task directory is created. Never invent a
   code apart from a title; never create one without approval
🛑 WAIT for user answers

## Step 4: Write HL

1. **Know who is acting.** Before durable writes, resolve once: one `team/` profile → silently; several → this machine's binding (`~/.tfw/bindings.yaml` or `%LOCALAPPDATA%\tfw\bindings.yaml`); missing/copied binding or profile → ask one short question. Never infer from OS, host, folders, or display names.

2. **Create the task folder.**

   ```
   container = tfw.task_containers[0]
   prefix    = tfw.task_prefix
   abbr      = approved title initials
   stamp     = clock now as YYYYMMDD-HHMMSS
   id        = {prefix}_{stamp}_{abbr}
   dir       = {container}/{stamp[0:4]}/{id}
   if dir exists: STOP; ask owner to approve another abbreviation
   otherwise: create dir once
   ```

   Prefix/abbreviation are uppercase alphanumeric without `_`. **The whole directory name is the identifier.** `_` separates fields; HL keeps full Title then Abbreviation. On collision, never retry, restamp, or suffix: reapprove the abbreviation, then create later. Read no counter, global maximum, or other task; perform only this existence check.

3. **Apply session identity.** With the approved ID, apply `PLAN` (`LEAD` only by governing authority) before state/event/HL writes; no ID exists earlier. Reapply if an approved collision changes it.

4. **Write the task's own state and first event** from templates: `status.md` and `journal/{stamp}__created__{token}.md`, with clock time, human `on_behalf_of`, and tool `via`. The opaque token gives same-second uniqueness, not identity.

5. **Create HL file** — use `templates/HL.md` as canonical format
6. **Fill §3.1** — satisfy the template's mandatory visualization gate.
7. **Fill §10 (RESEARCH Case)** — 2-4 hypotheses. The filter and the remaining subsections are in the template.
8. **Set the task's own state** — `lifecycle: HL_DRAFT` in `{task}/status.md`; fields and structural rules in `conventions.md` §4
9. **Capture Strategic Insights** — review conversation; fill template-governed §11.
10. **Prepare Role Assignment only when AT is contemplated.** Keep the selected-LEAD mandate and
    append-only working-unit assignment visibly separate. Before approval the mandate is draft; a
    complete roster is not required and no unit row starts work. Its absence leaves CL and separately
    explicit AG unchanged.

**GATE: User approves HL**
🛑 WAIT — present HL for review. Incorporate feedback. Repeat until approved.

**On approval — freeze the contract:**
1. Set the HL header `Contract` field to `🔒 FROZEN — approved by {owner} YYYY-MM-DD`
2. Commit with `freeze` **before** research; an uncommitted baseline is not diffable
3. What freezes, what stays free, and the recovery form: `conventions.md` §3 (HL Contract), rule 15
4. Ask the human owner to choose manual work or AT. No choice preserves CL. For AT, require one
   existing stable agent principal selected as LEAD and an explicit bounded mandate covering scope,
   role coverage/reach, reservations/controls, direct reporting and `Autonomous from`. Record the
   owner act; neither a profile, roster, binding nor lifecycle token substitutes for it.

## Step 5: Hypothesis Iteration

Present §10 individually: answer → confirmed/refuted; unsure → needs-research; obvious → remove. Offer skip only with none; recommend RESEARCH for needs-research or a Coordinator-visible blind spot. 🛑 WAIT.

## Step 6: RESEARCH decision & iteration management

### 6a. Initial RESEARCH decision

Present §10 count, blind spots, and risk assumptions; default RESEARCH. Skip needs concrete justification. Skip→Step 7; approval→6b.

### 6b. Create iterations.yaml

Create `research/iterations.yaml` in the task's `research/` folder. Format and field list: `conventions.md` §4 (Research subfolder).
`min_iterations`: from `project_config.yaml` → `tfw.research.min_iterations` (default: 2). `max_iterations`: soft ceiling (default: 5).

**Then:** "Start `/tfw-research`. Researcher role takes over." **STOP.**

### 6c. Iteration gate (after each research iteration returns)

Read all `research/iterN/RES.md` files and `research/iterations.yaml`. For each completed iteration:
1. Update `research/iterations.yaml`: mark iteration `status: complete`, record `res_file`
2. Read Iteration Status block from RES: gaps, open threads, recommendation
3. **Classify each recommendation by target section and rule 6**, never source table:
   - free section, or a free unit inside a frozen one → apply it
   - frozen claim → transcribe into HL §12 with verdict `PROPOSED`; the section itself stays untouched
4. **Route once per iteration** — preserve each proposer; submit the evidenced/costed batch under `HL Contract` rule 8

**Gate check:**
- IF completed iterations < `min_iterations` → **MUST** launch next iteration.
  Add next entry to `research/iterations.yaml` (focus = gaps/threads from previous RES).
  "Starting iteration {N}. `/tfw-research`." **STOP.**
- IF completed iterations ≥ `min_iterations`:
  - IF researcher recommends MORE NEEDED and coordinator agrees → launch next iteration
  - IF researcher recommends SUFFICIENT or coordinator overrides → proceed to Step 7
  - Coordinator may override `min_iterations` with documented justification

Before Step 7 every proposal is ruled/escalated; never derive TS from a moving contract.

### 6d. Amendment verdicts — whenever one arrives, in research, ONB, review or execution

- **No delegation claimed:** validate the human status owner and signer, then route directly to that
  owner; root, chain and grant facts are inapplicable.
- **Delegation claimed:** resolve rule 8 before applying; verify owner, root authorization, child-only
  chain, proposer, immutable grant, reservation and signer. Gaps stay `PROPOSED` and **STOP**.
- **✅ Approved by the resolved ruler** → record the signed §12 verdict, apply, then commit the new `freeze` baseline
- **❌ Rejected** → the row keeps its verdict and stays; the original contract holds; resume work
- **`RESTRICT`** → rule 10 applies on filing; **owner-initiated** → rule 9 requires the real human owner's explicit act

## Step 7: Write TS

1. **Choose phase topology.**
2. **Open `templates/TS.md`; apply all three loaded canonical sections to §4.** Missing authority stops
   approval.
3. **Write proportional Evidence per AC.**

### Small task (single phase):
4a. Write TS; get user approval of it and its immutable VALUE denominator.
5a. **STOP.** "TS is approved. Suggest execute `/tfw-handoff`. After RF, run `/tfw-review`."

### Large task (multi-phase):
4b. **Pre-TS Gate:** after Phase 1 read dependency RF result/deviations, never planned TS.

5b. Create the phase subfolder + write Phase HL + TS using `templates/TS.md`.
Folder layout: `conventions.md` §4 (Multi-phase folder structure). The Phase HL is derivation-only — §3 rules 20-21.
Each phase: HL → TS → `/tfw-handoff` → ONB → RF → `/tfw-review` → REVIEW
6b. Get owner approval of the TS and immutable VALUE denominator. Suggest `/tfw-handoff`; repeat per phase.

### AT dispatch after exact TS approval

For each start or continuation, resolve the selected principal/mandate separately from the actual
destination unit, address, parent, role/scope, direct channel, governing status, exact gate and
dispatch refs. A Coordinator unit may instantiate only a directly addressable child inside mandate;
record actual source/destination/parent, role/scope/channel, governing refs and originating proposer
`{principal, unit}` or `none`. `writer` is attribution, not an edge or inherited grant. Apply rule 8
without replacing origin after forwarding/restart. Missing, conflicting, foreign or `—` facts report
directly and wait. Never execute another workflow. Reuse the same Executor and independent Reviewer;
if either assigned holder is unavailable, require owner-approved §12 `SUPERSEDE` before bounded
replacement dispatch. Questions, proposals and results return directly.

## Step 8: a 🔄 REVISE returned the work — rule and route the round

Read `conventions.md` → `The 🔄 REVISE route`; it alone decides recipient, ruling site, governing
artifact, lifecycle effect, and hard stop. Then:

1. **Rule each proposal once.** A `promoted` disposition first gets its task, `status.md`, and
   PROPOSAL. Retain the cited criterion/claim, owner, and observable completion; no basis fails.
2. **Apply one table case.** Rung 1 appends its bound to live REVIEW and keeps TS/RF. Any rung 2 writes
   one approved TS revision and sets `TS_DRAFT`. Rung 3 files the §12 proposal/event, resolves rule 8,
   and waits for a valid terminal verdict before Executor dispatch.
3. **STOP at the table recipient.** Rung 1/2: name the governing artifact and `/tfw-handoff`. Rung 3:
   name amendment/ruler and "STOP until terminal verdict." Never execute the round.

> → Role Lock: `conventions.md` §15

**Footer — Self-check before submitting:**
Read the addressed `conventions.md` headings `Anti-patterns (prohibited)` and `Task Statuses`:
did I violate either contract?
