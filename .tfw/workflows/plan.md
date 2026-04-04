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
4. **Ask clarifying questions** — batch all questions, max 3-5
🛑 WAIT for user answers

## Step 4: Write HL

1. **Create task folder** — `tasks/{PREFIX}-{N}__{description}/`
   → Read `tfw.task_prefix` and `tfw.initial_seq` from `PROJECT_CONFIG.yaml`
2. **Create HL file** — use `templates/HL.md` as canonical format
3. **Fill §3.1 (visualization)** — create ASCII visualization of To-Be (mandatory). Add mermaid if flow is complex.
4. **Fill §10 (RESEARCH justification)** — write 2-4 hypotheses. For each: apply filter «If false, would approach change?» Remove if no. Add blind spots, risks of not researching, proposed RESEARCH focus.
5. **Update project task board** — add task with status `📝 HL_DRAFT`. ID must be a link: `[PROJ-N](tasks/PROJ-N__title/)`

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

## Step 6: RESEARCH decision

Review HL §10. Present: «N hypotheses need research. Blind spots: [list]. Recommend: RESEARCH / skip.»
- Default recommendation: **run RESEARCH**
- Frame as risk reduction: "Without RESEARCH, we are assuming X, Y, Z — are we confident enough?"
- Skipping requires concrete justification (not just "task is simple")

IF user approves research → "Start `/tfw-research`. Researcher role takes over." **STOP.**
IF user skips → confirm, proceed to Step 7.

After RESEARCH: read RES Closure → update HL → present diff to user → user confirms → proceed to Step 7.

## Step 7: Write TS

1. **Determine complexity** — single-phase or multi-phase?
2. **Budget check** — read `PROJECT_CONFIG.yaml` → `tfw.scope_budgets`. Read `conventions.md` §6 for rules.
   Calculate: count files in TS, count new files, estimate LOC.
   IF exceeds any limit → split into phases OR document override with justification.

### Small task (single phase):
3a. Write TS using `templates/TS.md` with DoD in same folder
4a. Get user approval on TS
5a. **STOP.** "TS is approved. Start execution with `/tfw-handoff`. After RF, run `/tfw-review`."

### Large task (multi-phase):
3b. Write Phase A HL + TS. Each Phase gets its own cycle:
```
Master HL (coordinator)
  ├── Phase A: HL__PhaseA → TS__PhaseA → ONB → RF__PhaseA → /tfw-review → REVIEW
  ├── Phase B: HL__PhaseB → TS__PhaseB → ONB → RF__PhaseB → /tfw-review → REVIEW
  └── Phase C: ...
```
4b. Hand off via `/tfw-handoff`
5b. After RF, run `/tfw-review`. Repeat for next phase.

> ⚠️ The coordinator MUST NOT proceed to ONB/execution/RF. Even for small tasks, the role boundary is absolute.
> → Role Lock details: `conventions.md` §15

**Footer — Self-check before submitting:**
Read `conventions.md` §14 (Anti-patterns). Did I violate any? Especially: TS without approved HL? Modified files outside scope? Skipped RESEARCH without presenting pros/cons? HL without §3.1 or §10? Did I hand off to Researcher properly? Did I STOP after recommending research?
→ Full anti-pattern list: `conventions.md` §14
→ Status transitions: `conventions.md` §5

