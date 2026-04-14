---
description: TFW Plan — research, write HL, review, scope decision, write TS
---

# TFW Plan — Task Inception Workflow

> 🔒 **ROLE LOCK: COORDINATOR**
> You write HL and TS. You do NOT write ONB, RF, RES, REVIEW, or code.
> Violation = immediate stop + report.

**Mindset:** You are a strategic architect. Understand the problem deeply before proposing solutions. Show the finish line visually (§3.1). Identify what you DON'T know (§10). Challenge assumptions — be a thinking partner, not a yes-machine. Quality of planning > speed of pipeline progression.

When recommending RESEARCH: your default is to recommend it. Think about what RESEARCH could reveal — blind spots, external context, alternatives. Present concretely: "RESEARCH could reveal X, Y, Z."

## Step 1: Load context

Read `conventions.md` §10 (Context Loading). Verify: AGENTS.md loaded, KNOWLEDGE.md read, task board checked, conventions.md and glossary.md loaded. If any missing → load now.

## Step 2: Knowledge Gate

1. Read `.tfw/knowledge_state.yaml`
2. Read `tfw.knowledge.gate_mode` from PROJECT_CONFIG.yaml
3. Compute: `current_seq - last_consolidation_seq`
4. IF `>= interval` AND gate_mode = `hard`:
   → **HARD STOP**: "Knowledge consolidation overdue ({N} tasks). Run `/tfw-knowledge` before proceeding."
   Skip allowed with justification. Record: `knowledge-gate: skipped (reason: ...)`
5. IF `>= interval` AND gate_mode = `soft`:
   → Reminder: "Knowledge consolidation recommended ({N} tasks since last)."
6. IF gate_mode = `off`: skip silently

## Step 3: Research & Understand

1. **Identify context** — read relevant code, existing HL files, knowledge items
2. **Understand the problem deeply** — what is broken, what is missing, what needs to change. Do NOT rush to solutions. What does the user actually need vs what they asked for?
3. **Study references** — how similar problems were solved before (existing Architecture Decisions)
4. **Check KNOWLEDGE.md** — scan Architecture Decisions, known conventions, and prior task findings. If any are relevant to this task, cite them in HL §4 (Phase Context). If none apply: write "No applicable knowledge items."
5. **Ask clarifying questions** — batch all questions, max 3-5
🛑 WAIT for user answers

## Step 4: Write HL

1. **Create task folder** — `tasks/{PREFIX}-{N}__{description}/`
   → Read `tfw.task_prefix` and `tfw.initial_seq` from `PROJECT_CONFIG.yaml`
2. **Create HL file** — use `templates/HL.md` as canonical format
3. **Fill §3.1 (visualization)** — create ASCII visualization of To-Be (mandatory). Add mermaid if flow is complex.
4. **Fill §10 (RESEARCH justification)** — write 2-4 hypotheses. For each: apply filter «If false, would approach change?» Remove if no. Add blind spots, risks of not researching, proposed RESEARCH focus.
5. **Update project task board** — add task with status `📝 HL_DRAFT`. ID must be a link: `[PROJ-N](tasks/PROJ-N__title/)`
6. **Capture Strategic Insights** — review conversation history, fill HL §11 (Strategic Session Insights). Each insight: Category (§10.1), Source. Human-Only Test: would this be unknown without the user saying it?

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

## Step 6: RESEARCH decision & iteration management

### 6a. Initial RESEARCH decision

Review HL §10. Present: «N hypotheses need research. Blind spots: [list]. Recommend: RESEARCH / skip.»
- Default recommendation: **run RESEARCH**
- Frame as risk reduction: "Without RESEARCH, we are assuming X, Y, Z — are we confident enough?"
- Skipping requires concrete justification (not just "task is simple")

IF user skips → confirm, proceed to Step 7.
IF user approves research:

### 6b. Create iterations.yaml

Create `iterations.yaml` in task folder. Fields:
- `task_id`, `title`
- `min_iterations`: from `PROJECT_CONFIG.yaml` → `tfw.research.min_iterations` (default: 2). Coordinator can override per task.
- `max_iterations`: soft ceiling (default: 5)
- `iterations`: array with first entry: `number: 1`, `focus`, `hypotheses`, `status: pending`

**Then:** "Start `/tfw-research`. Researcher role takes over." **STOP.**

### 6c. Iteration gate (after each research iteration returns)

Read all `RES__*` files and `iterations.yaml`. For each completed iteration:
1. Update `iterations.yaml`: mark iteration `status: complete`, record `res_file`
2. Read Iteration Status block from RES: gaps, open threads, recommendation
3. Update HL with research findings (present diff to user)

**Gate check:**
- IF completed iterations < `min_iterations` → **MUST** launch next iteration.
  Add next entry to `iterations.yaml` (focus = gaps/threads from previous RES).
  "Starting iteration {N}. `/tfw-research`." **STOP.**
- IF completed iterations ≥ `min_iterations`:
  - IF researcher recommends MORE NEEDED and coordinator agrees → launch next iteration
  - IF researcher recommends SUFFICIENT or coordinator overrides → proceed to Step 7
  - Coordinator may override `min_iterations` with documented justification

After all iterations complete: update HL → present diff to user → user confirms → proceed to Step 7.

## Step 7: Write TS

1. **Determine complexity** — single-phase or multi-phase?
2. **Budget check** — read `PROJECT_CONFIG.yaml` → `tfw.scope_budgets`. Read `conventions.md` §6 for rules.
   Calculate: count files in TS, count new files, estimate LOC.
   IF exceeds any limit → split into phases OR document override with justification.

### Small task (single phase):
3a. Write TS using `templates/TS.md`
4a. Get user approval on TS
5a. **STOP.** "TS is approved. Suggest execute `/tfw-handoff`. After RF, run `/tfw-review`."

### Large task (multi-phase):
3b. Create phase subfolder + write Phase HL + TS using `templates/TS.md`:
```
tasks/{PREFIX}-{N}__{title}/          ← master HL, RES, research/ here
  PhaseA/
    HL__PhaseA__{title}.md            ← uses §4 Context block from master HL
    TS__PhaseA__{title}.md
  PhaseB/
    HL__PhaseB__{title}.md
    TS__PhaseB__{title}.md
```
Each phase: HL → TS → `/tfw-handoff` → ONB → RF → `/tfw-review` → REVIEW
4b. Suggest execute via `/tfw-handoff`
5b. After RF, run `/tfw-review`. Repeat for next phase.

> ⚠️ The coordinator MUST NOT proceed to ONB/execution/RF. Even for small tasks, the role boundary is absolute.
> → Role Lock details: `conventions.md` §15

**Footer — Self-check before submitting:**
Read `conventions.md` §14 (Anti-patterns). Did I violate any? Especially: TS without approved HL? Modified files outside scope? Skipped RESEARCH without presenting pros/cons? HL without §3.1, §10, or §11? Did I hand off to Researcher properly? Did I STOP after recommending research?
→ Full anti-pattern list: `conventions.md` §14
→ Status transitions: `conventions.md` §5

