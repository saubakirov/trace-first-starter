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

For an existing task, after task/phase state and lineage resolve, apply `Session identity` with
`WORK=PLAN`, or `LEAD` only from governing authority. Do this before the Knowledge Gate, questions,
or proposals. If no task exists, defer identity until Step 4 creates its approved ID.

## Step 2: Knowledge Gate

1. Read `tfw.knowledge.gate_mode` and `interval` from `.tfw/project_config.yaml`.
2. If mode is `off`, skip. Otherwise run:
   `python .tfw/scripts/gen_index.py --knowledge-pending --format json`.
3. If the command exits nonzero or reports `problems` or `removed_task_ids`, **HARD STOP**;
   name every trace problem. Do not compute a threshold over unresolved input.
4. Let `delta` be the number of distinct `pending_task_ids` in the JSON. Zero is an explicit
   no-op.
5. In `soft` mode, report `delta/interval` and continue.
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

1. **Know who is acting.** Before the first durable write of the session, resolve the acting
   handle: one profile in `team/` → use it silently; several → read the binding on this
   machine (`~/.tfw/bindings.yaml`, or `%LOCALAPPDATA%\tfw\bindings.yaml`); no binding, a
   copied binding, or a handle whose profile is gone → **ask exactly one short question**,
   once, then proceed. Never infer identity from an OS username, hostname or folder name.

2. **Create the task folder.**

   ```
   container = tfw.task_containers[0]             # from project_config.yaml
   prefix    = tfw.task_prefix                    # uppercase alphanumeric, no `_`
   abbr      = initials of the approved title     # approved with it; uppercase alphanumeric, no `_`
   stamp     = system clock, read now, as YYYYMMDD-HHMMSS
   id        = {prefix}_{stamp}_{abbr}
   dir       = {container}/{stamp[0:4]}/{id}
   if dir exists: STOP; ask the owner to approve a different abbreviation
   otherwise: create dir exactly once
   ```

   **The whole directory name is the identifier.** Single underscores are unambiguous
   separators because no field may contain `_`. The full title remains in `status.md`; the HL
   header carries **Title** and **Abbreviation** as adjacent fields, in that order.

   On collision, do not recompute the timestamp, add a suffix or retry silently. Those actions
   would invent an identifier different from the one the planning exchange approved. Ask for
   a different abbreviation and repeat the approval exchange before a later creation attempt.

   **Read no counter, no project-wide maximum and no other task's contents.** The one
   existence check above is what lets two offline participants stay safe with nothing shared
   between them.

3. **Apply session identity.** With the approved ID, apply `Session identity` as `PLAN`, or
   `LEAD` only from governing authority, before the status/event/HL writes below.

   This is step 3 and not step 0 deliberately. Understanding the task and asking before
   creating a folder is the right order, and it is kept — which means the identifier does not
   exist until now, so an instruction to use it earlier is unsatisfiable and what happens
   instead is a name carrying a role and a guess.

   **Repeat this step if an approved collision resolution creates a different ID.** A rename
   that leaves the session named after the old ID is worse than no name.

4. **Write the task's own state and its first event** — `status.md` from
   `.tfw/templates/status.md`, and a `created` event in `journal/` named
   `{stamp}__created__{token}.md`, carrying `on_behalf_of` and `via`. The `token` is a short
   opaque value whose only job is that two writes in one second differ — it is not an
   identity and needs no profile. The event's `time` is read from the clock, never typed.

5. **Create HL file** — use `templates/HL.md` as canonical format
6. **Fill §3.1** — satisfy the template's mandatory visualization gate.
7. **Fill §10 (RESEARCH Case)** — 2-4 hypotheses. The filter and the remaining subsections are in the template.
8. **Set the task's own state** — `lifecycle: HL_DRAFT` in `{task}/status.md`; fields and bounds in `conventions.md` §4
9. **Capture Strategic Insights** — review conversation; fill template-governed §11.

**GATE: User approves HL**
🛑 WAIT — present HL for review. Incorporate feedback. Repeat until approved.

**On approval — freeze the contract:**
1. Set the HL header `Contract` field to `🔒 FROZEN — approved by {owner} YYYY-MM-DD`
2. Commit with `freeze` **before** research; an uncommitted baseline is not diffable
3. What freezes, what stays free, and the recovery form: `conventions.md` §3 (HL Contract), rule 15

## Step 5: Hypothesis Iteration

Present §10 hypotheses to user one by one:
  FOR EACH hypothesis:
    USER: "I know the answer" → mark confirmed/refuted in table, record answer
    USER: "Not sure" → mark needs-research
    USER: "This is obvious" → remove from table
  AFTER iteration:
    IF all confirmed/refuted → RESEARCH optional (offer skip)
    IF any needs-research → recommend RESEARCH
    IF coordinator sees remaining blind spots → still recommend RESEARCH despite user closure
🛑 WAIT for user response

## Step 6: RESEARCH decision & iteration management

### 6a. Initial RESEARCH decision

Review HL §10. Present: «N hypotheses need research. Blind spots: [list]. Recommend: RESEARCH / skip.»
- Default recommendation: **run RESEARCH**
- Frame as risk reduction: "Without RESEARCH, we are assuming X, Y, Z — are we confident enough?"
- Skipping requires concrete justification (not just "task is simple")

IF user skips → confirm, proceed to Step 7.
IF user approves research:

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
