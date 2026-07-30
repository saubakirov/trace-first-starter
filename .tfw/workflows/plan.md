---
description: TFW Plan — research, write HL, review, scope decision, write TS
---

# TFW Plan — Task Inception Workflow

> 🔒 **ROLE LOCK: COORDINATOR**
> You write HL and TS. You do NOT write ONB, RF, RES, REVIEW, or code.
> Violation = immediate stop + report.

**Mindset:** You are a strategic architect. Start from product purpose, applicable
Project Values, and the decision-changing uncertainty—not from a preferred solution.
Show the finish line visually (§3.1). Identify what you DON'T know (§10). Challenge
assumptions; quality of decision > speed of pipeline progression.

When recommending RESEARCH: your default is to recommend it. Think about what RESEARCH could reveal — blind spots, external context, alternatives. Present concretely: "RESEARCH could reveal X, Y, Z."

## Step 0: Name This Session

**Name this session:** `Coordinator | {TASK-ID}`
Set this as the session/conversation name before doing anything else.

## Step 1: Load context

Read `conventions.md` §10 (Context Loading). Verify: AGENTS.md loaded, KNOWLEDGE.md read, task board checked, conventions.md and glossary.md loaded. If any missing → load now.

## Step 2: Knowledge Gate

1. Read `.tfw/knowledge_state.yaml`
2. Read `tfw.knowledge.gate_mode` from project_config.yaml
3. Compute: `current_seq - last_consolidation_seq`
4. IF `>= interval` AND gate_mode = `hard`:
   → **HARD STOP**: "Knowledge consolidation overdue ({N} tasks). Run `/tfw-knowledge` before proceeding."
   Skip allowed with justification. Record: `knowledge-gate: skipped (reason: ...)`
5. IF `>= interval` AND gate_mode = `soft`:
   → Reminder: "Knowledge consolidation recommended ({N} tasks since last)."
6. IF gate_mode = `off`: skip silently

## Step 3: Research & Understand

1. **Identify purpose and authority** — name the product purpose, stakeholder/owner
   decision, and applicable Project Values before evaluating a solution.
2. **Separate the planning inputs** — record the decision-changing uncertainty, the
   evidence needed to reduce it, and any proposed solution as distinct items. A proposed
   solution is not evidence that the uncertainty is closed.
3. **Study references and reality** — compare relevant code/output, existing HL/RF
   files, knowledge items, Architecture Decisions, and observed evidence.
4. **Scan Project Values (PV)** — see glossary.md PV Index.
      Full scan: README Values, knowledge/philosophy.md, KNOWLEDGE.md §1, conventions.md §3/§11/§14.
      Skim: knowledge/convention.md, knowledge/process.md, other topic files.
      Fill HL §7.2 Knowledge Citations table — each item linked.
      If no applicable items: "No applicable knowledge items."
      For new projects: "No applicable knowledge items — project in bootstrap phase."
5. **Ask clarifying questions** — ask only questions whose answers can change the
   decision. Prioritize and split them when the user cannot answer safely or coherently
   in one turn; do not use question volume as progress.
6. **Prepare Requirement Claim inputs** — for every material intended deliverable,
   identify its intent/authority, observable outcome, local or crossed boundary,
   acceptance-critical precision, adaptable guidance, and likely proof route. This is
   planning input, not implementation. Leave a non-triggered cognitive field `N/A` with
   reason rather than inventing a value.
🛑 WAIT for user answers

## Step 4: Write HL

1. **Create task folder** — `tasks/{PREFIX}-{N}__{description}/`
   → Read `tfw.task_prefix` and `tfw.initial_seq` from `project_config.yaml`
2. **Create HL file** — use `templates/HL.md` as canonical format
3. **Fill §3.1 (visualization)** — create ASCII visualization of To-Be (mandatory). Add mermaid if flow is complex.
4. **Fill §10 (RESEARCH justification)** — write only decision-changing hypotheses.
   For each, apply the filter: «If false, would the approach change?» Remove if no.
   Add blind spots, risks of not researching, and proposed RESEARCH focus.
5. **Update project task board** — add task with status `📝 HL_DRAFT`. ID must be a link: `[PROJ-N](tasks/PROJ-N__title/)`
6. **Capture Strategic Insights** — review conversation history and fill HL §11.
   Every material insight records its planning implication and TS
   disposition/destination. Valid dispositions include AC, scope, Technical Guidance,
   Definition of Failure, decision/research direction, explicit task-local/non-use
   reason, or a resolvable downstream destination. Do not force one insight into one AC.
   Apply the Human-Only Test: would this be unknown without the user saying it?

**GATE: User approves HL**
🛑 WAIT — present HL for review. Incorporate feedback. Repeat until approved.

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

## Step 6: Comparative RESEARCH Decision & Iteration Management

### 6a. Initial RESEARCH decision

Review HL §10. Present: «N hypotheses need research. Blind spots: [list]. Recommend: RESEARCH / skip.»
- Default recommendation: **run RESEARCH**
- Frame as risk reduction: "Without RESEARCH, we are assuming X, Y, Z — are we confident enough?"
- Skipping requires concrete justification (not just "task is simple")

**Procedure-fit gate:** The current
[Comparative Decision Procedure](../glossary.md#comparative-decision-procedure) fits
only when the uncertainty requires comparing material alternatives, relationships, or
configurations. Record what decision the comparison supports and what result would
change the approach.

- IF fit → offer the procedure and a qualitative focused/deep intensity.
- IF mismatch → report the unresolved information need and return the decision to the
  user. Do not choose, name, simulate, or load another strategy in this workflow.
- IF user skips a fitting procedure → confirm the decision and proceed to Step 7.
- IF user approves a fitting procedure → continue below.

### 6b. Create iterations.yaml

Create `research/iterations.yaml` in task's `research/` folder. Fields:
- `task_id`, `title`
- `min_iterations`: copy the current config value for compatibility/migration
  visibility only; it no longer has universal closure authority
- `max_iterations`: preserve the existing field when used by the project, but treat it
  as transitional planning metadata rather than completion evidence
- `iterations`: array with first entry: `number: 1`, `focus`, `hypotheses`, `status: pending`
- Optional fields per iteration: `agent` (free-text, for traceability), `sources` (list of source categories consulted)

The first entry starts one complete filesystem-traced procedure. Every later entry's
`focus` MUST name its trigger: error correction, unresolved material gap/hypothesis,
counter-evidence need, changed decision, or user-injected direction.

**Then:** "Start `/tfw-research`. Researcher role takes over." **STOP.**

### 6c. Iteration closure gate (after each research iteration returns)

Read all `research/iterN/RES.md` files and `research/iterations.yaml`. For each completed iteration:
1. Update `research/iterations.yaml`: mark iteration `status: complete`, record `res_file`
2. Read Iteration Status block from RES: gaps, open threads, recommendation
3. Update HL with research findings (present diff to user)

**Closure claim:**

1. Verify the completed iteration contains `1_briefing.md`, `2_gather.md`,
   `3_extract.md`, `4_challenge.md`, and `RES.md`. Missing trace = incomplete.
2. Review declared corpus/evidence families, exclusions, counter-evidence, decision
   effect, saturation, and explicit unresolved gaps.
3. IF a named next-iteration trigger exists and Coordinator/user agrees → add the next
   entry with that trigger in `focus`, start `/tfw-research`, and **STOP**.
4. IF no trigger exists and the decision is supported or honestly unresolved →
   Coordinator/user may proceed, deepen, defer, or accept the gap. A legacy
   `min_iterations`/`max_iterations` value does not decide closure.
5. Exhausted evidence may yield an insufficient/unresolved result; never convert
   activity volume into a conclusion.

After all iterations complete: update HL → present diff to user → user confirms → proceed to Step 7.

## Step 7: Write TS

1. **Pre-TS insight trace gate** — for every material HL §11 Strategic Insight,
   human requirement/correction, owner decision, cited authority, and applicable
   Project Value, verify a planning implication and resolvable claim, scope,
   Technical Guidance, Degree-of-Freedom, Definition-of-Failure, decision/research
   direction, or explicit task-local/non-use destination. Challenge missing
   dispositions, but do not require a separate AC when another destination protects
   the consequence.
2. **Determine complexity** — single-phase or multi-phase?
3. **Scope-attention check** — read `project_config.yaml` →
   `tfw.scope_budgets` and `conventions.md` §6. Record the counting method, proposed
   files, new files, modified files, and estimated LOC. The numbers are transitional
   attention/escalation signals, not quality or completion gates.
   - When a signal is crossed, explicitly choose: simplify; remove unrelated work;
     split at a coherent value boundary; record a bounded override with cohesion/proof
     rationale; or return to the Coordinator/user.
   - Do not split when it would orphan the product outcome, hide a seam, or defer
     triggered value without complete Value Debt.
   - Do not reclassify physical or functional files/LOC solely to satisfy a number.
4. **Requirement Claim gate** — for every material AC, use the compact contract in
   `templates/TS.md` and verify:
   - intent/authority and observable outcome are resolvable;
   - the boundary names every crossed source, interface, role, package, phase,
     stakeholder, live environment, or irreversible event;
   - exact identifiers, cited-source relations, and named checks are
     acceptance-critical only when changing them changes compatibility, fidelity, or
     acceptance; other implementation choices remain adaptable Technical Guidance;
   - every claimed deliverable triggers Local Proof; crossed/live boundaries add
     Seam/Live Proof; grouping remains resolvable;
   - non-triggered fields use justified `N/A`, never blank boilerplate or invented
     values.
5. **Gate and Evidence intent** — make each `Gate:` name the claim or failure protected
   by its synthetic/structural/source check. Code tests and builds are conditional, not
   universal. Write `Evidence:` for intended-environment observation only: a full or
   minimal specification, `N/A — {claim-based reason}`, `DEFERRED — {named due event
   and planned Value Debt}`, or an explicit Executor decision boundary. The Executor
   MAY adjust adaptable tools with RF rationale, but not acceptance-critical proof.

### Small task (single phase):
6a. Write TS using `templates/TS.md`
7a. Get user approval on TS
8a. **STOP.** "TS is approved. Suggest execute `/tfw-handoff`. After RF, run `/tfw-review`."

### Large task (multi-phase):
6b. **Pre-TS Gate (multi-phase):** Before writing the TS for Phase N (any phase after the first), read the RF of the latest completed phase in the dependency chain. Verify: what was actually delivered? What deviated from plan? Read RF (actual output), not TS (planned output) — these differ. Skip if this is the first phase (no predecessor RF exists).

7b. Create phase subfolder + write Phase HL + TS using `templates/TS.md`:
```
tasks/{PREFIX}-{N}__{title}/          ← master HL, research/ here
  phase-a/
    HL__phase-a__{title}.md           ← uses §4 Context block from master HL
    TS__phase-a__{title}.md
  phase-b/
    HL__phase-b__{title}.md
    TS__phase-b__{title}.md
```
Each phase: HL → TS → `/tfw-handoff` → ONB → RF → `/tfw-review` → REVIEW
8b. Suggest execute via `/tfw-handoff`
9b. After RF, run `/tfw-review`. Repeat for next phase.

> ⚠️ The coordinator MUST NOT proceed to ONB/execution/RF. Even for small tasks, the role boundary is absolute.
> → Role Lock details: `conventions.md` §15

**Footer — Self-check before submitting:**
Read `conventions.md` §14 (Anti-patterns). Did I violate any? Especially: TS without approved HL? Modified files outside scope? Skipped RESEARCH without presenting pros/cons? HL without §3.1, §10, or §11? Did I hand off to Researcher properly? Did I STOP after recommending research?
→ Full anti-pattern list: `conventions.md` §14
→ Status transitions: `conventions.md` §5
