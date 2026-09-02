---
description: TFW Handoff — executor onboarding, implementation, RF
---

# TFW Handoff — Task Execution by New Agent

> **Roles:** Coordinator (hands off) → Executor (receives, questions, implements)
> **Input:** Approved HL + TS files
> **Output:** RF file with implementation results

> **🔒 ROLE LOCK: EXECUTOR**
> Permitted artifacts: ONB, RF.
> Forbidden actions: writing HL, writing TS, writing REVIEW, modifying HL, changing scope.
> The executor MUST NOT modify HL or TS. If scope issues are found — write them in ONB and **STOP**.

## Step 0: Name This Session

**Name this session:** `Executor | {TASK-ID} | Phase {X}`
Set this as the session/conversation name before doing anything else.

## Context Loading (Executor)

When starting as executor, load in order:
1. `AGENTS.md` — agent instructions
2. `.tfw/conventions.md` — project conventions
3. `.tfw/glossary.md` — terminology
4. `KNOWLEDGE.md` — architecture, decisions, legacy (if exists)
5. **Master HL** for the task — understand vision, design philosophy, architecture decisions
6. **Phase HL** (if multi-phase) — phase-specific scope and context
7. **TS file** for the task — exact scope, DoD, constraints. On a return after a 🔄 REVISE this is the **highest-numbered revision**, `TS__{ID}__rev{N}.md`, which governs and which carries the round's order
8. **Prior REVIEW** — the reasoning behind that order: the verdict, the findings and the dispositions
9. Related HL/TS/RF files referenced in the task
10. Relevant code files listed in TS

## Who Is Acting

Resolve the acting handle **before the first durable write** — before any `status.md` change,
any journal event, any commit. Once per session, not per turn.

| Situation | What happens |
|---|---|
| One profile in `team/` | it is used, silently |
| Several profiles | read the binding on **this machine** — `~/.tfw/bindings.yaml`, or `%LOCALAPPDATA%\tfw\bindings.yaml` |
| No binding · a shared device · a copied binding · a handle whose profile is gone | **ask exactly one short question**, then proceed |

Identity is never inferred from an OS username, hostname, folder name or account display
string. Every event this session writes carries `on_behalf_of` (always a human) and `via`
(the tool). A writer is not named yet — that is TFW-54 — so do not create a profile per
session. → `conventions.md` §4

## Returning after a 🔄 REVISE

A REVISE sends the work back with a stated order. Read, in this order:

1. **The current TS revision** — `TS__{ID}__rev{N}.md`, the highest ordinal, which governs. It is the coordinator's own artifact and it **is** the order: the round, who ordered it, each item's basis, what is not re-done, and its approval. You are already obliged to read the TS, so there is nothing to detect and nothing hidden.
2. **The prior REVIEW** — the reasoning behind that order: its §4 verdict and its findings. Its §5 dispositions were ruled by the coordinator and are not yours to revisit.

**What is not re-done.** Work the prior review approved, ONB questions already answered, and evidence already collected for an acceptance criterion the round does not return.

**The round's artifacts** — grammar in `conventions.md` §4. The TS and the REVIEW take **siblings**, `…__rev{N}.md`, never an overwrite. The RF and the ONB are **appended to**: one new numbered subsection per round, in every section the round touches, because the rejected version must stay openable. The TS is the coordinator's and moves only by their act.

**What is not yours.** An item marked `pending — coordinator` is rung 2: it needs the TS changed, and changing a TS is a Role Lock violation for you. If the order names one and the TS has not moved, write that in the RF and **stop** — never widen the TS yourself.

## Phase 1: Executor Onboarding

1. **Read all context** — HL, TS, referenced files, relevant code
2. **Analyze the task** — identify:
   - Questions that need clarification (blocking and non-blocking)
   - Recommendations for improvement
   - Risks and edge cases not covered in TS
   - Read HL §7.2 Knowledge Citations — verify each item, fill ONB §7.
     For each citation: confirm read, state how applied or why N/A.
     Add any NEW PV items you find relevant that coordinator missed.
   - Inconsistencies between HL/TS/KNOWLEDGE.md and actual code
   - Missing information or incomplete specifications
   - Errors, gaps, or oversights in the spec
3. **Write ONB file** — use `.tfw/templates/ONB.md` as canonical format. Structured as:

   ```markdown
   ## Questions (blocking — cannot proceed without answers)
   | # | Question | Answer |
   |---|----------|--------|

   ## Recommendations (suggestions, not blocking)
   1. ...

   ## Risks Found (edge cases, potential issues not in TS)
   1. ...

   ## Inconsistencies with Code (spec vs reality)
   1. ...
   ```

4. **Commit ONB using Commit Attribution; push only after explicit user approval** — the onboarding report is a first-class artifact
5. **Wait for user approval** — do NOT proceed until all blocking questions resolved

   > **Coordinator ONB answer protocol:** When answering blocking questions — if the answer is not explicitly stated in HL, TS, or KNOWLEDGE.md, present 2-3 options with tradeoffs. Do not decide on behalf of the stakeholder.

6. **Set the task's own state** — `lifecycle: ONB` and `updated` in `{task}/status.md`, and append a `handoff` event to `{task}/journal/` as `{YYYYMMDD-HHMMSS}__{kind}__{token}.md` — the time read from the clock, the token drawn not chosen. No file outside this task directory changes.

## Phase 2: Execution

7. **Implement** — follow TS step by step:
   - For code changes: write production-ready code, no placeholders
   - For CL tasks: present commands/SQL to user, wait for execution
   - For AG tasks: create artifacts directly

   **Execution Loops** — if TS acceptance criteria have `[depends: AC-X]` annotations (meaning one AC must be verified before another can start): verify the prerequisite AC gate passes before starting the dependent AC. Example: if AC-2 has `[depends: AC-1]`, verify AC-1 is complete before implementing AC-2. Independent ACs (no `[depends]`) may be implemented in any order.

8. **Run tests** — as specified in TS verification section
9. **Build gate** — run build/compile command from TS verification section.
    If build fails → fix BEFORE writing RF. Never write RF with failing build.

10. **Collect evidence** — create the evidence folder and populate the EV file:
    1. Create `evidence/` folder in task directory (or phase directory for multi-phase tasks).
    2. Copy `.tfw/templates/evidence/EV.md` to `evidence/EV__{ID}.md` (or `EV__phase-{x}__{title}.md` for multi-phase).
    3. Fill the Environment header with actual verification environment details.
    4. Walk through each TS AC item — for each, add a row to the evidence table with what was verified, the environment, the result (VERIFIED / DEFERRED / BLOCKED / N/A), and an artifact reference.
    5. Write the Verdict summary line with counts per status.
    6. If binary artifacts exist (screenshots, logs, API responses), place them in `evidence/` and index them in the Attachments section.
    - If evidence can't be collected (no environment, no device, no deployment): mark DEFERRED or BLOCKED with the specific reason. Silent omission is a violation.
    - Proactively seek and configure tools (MCP servers, browser automation, CLI utilities) needed for evidence collection. Don't wait for tools to be handed to you.
    - RF §5 is a pointer to the EV file — write it as: `See [EV file](...) for evidence details.` + verdict summary.

## Phase 3: Write RF

11. **Pre-RF Gate** — open `.tfw/templates/RF.md`. Read all section headings before writing anything. Then write RF following this structure.

12. **Create RF file** — use `.tfw/templates/RF.md` as canonical format. MANDATORY sections:
    - **§1 What Was Done** — changes list with file paths
    - **§2 Key Decisions** — decisions and rationale
    - **§3 Acceptance Criteria** — checkmark each TS DoD item
    - **§4 Verification** — lint/test/verify results
    - **§5 Evidence** — pointer to EV file + verdict summary. Full evidence in `evidence/EV__{...}.md`.
    - **§6 Observations** — out-of-scope items noticed (table format). Quality bar: only issues that would bite the next developer.
    - **§7 Fact Candidates** — review conversation history, extract human-sourced knowledge. If none: "No fact candidates."
    - **§8 Strategic Insights** — capture domain knowledge with implications. If none: "No strategic insights."
    - **§9 Diagrams** — architecture, data flow, component interaction. If none: "No diagrams."
    Never omit §5. Never omit §7-9. Empty content is acceptable ("No X."); absent section is not.

13. **Set the task's own state** — `lifecycle: RF` in `{task}/status.md`, with a `transition` event in `{task}/journal/`, the time read from the clock

> 💡 As you work, capture strategic knowledge about the project — stakeholder priorities,
> domain patterns, business context, external constraints — in §7 Fact Candidates.
> These save the next agent from missing critical context.
>
> **Before writing Fact Candidates, review the conversation history.** The human's
> messages are the primary source — their decisions, priorities, concerns, and domain
> insights. Extract what informs decisions, not implementation details.

### Observations Section (mandatory in RF)

Executors MUST report anything they noticed but did NOT modify:

```markdown
## Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `example.tsx` | 42 | dead-code | Unused import `OldComponent` |
| 2 | `utils.ts` | 15-20 | duplication | Same helper exists in 3 files |
```

**Types:** `dead-code`, `naming`, `todo`, `duplication`, `perf`, `security`, `style`, `missing-test`, `ux`

**Quality bar**: report only issues that would bite the next developer. Don't generate observations just because the section exists.

If nothing found, write: `No observations.`

## 🛑 Executor STOP

> **Your work is done.** Do NOT proceed to review.
> Inform the user: "RF is complete. Start `/tfw-review` to review the results."
> Writing a REVIEW file as executor is a **🔒 Role Lock violation**.

## Multi-Phase Task Flow

For large tasks broken into phases:

```
Coordinator: Master HL (approved)
    │
    ├── Phase A: Coordinator writes TS__phase-a
    │   └── Executor Agent: reads → ONB → executes → RF__phase-a
    │   └── After RF, run /tfw-review for review
    │
    ├── Phase B: Coordinator writes TS__phase-b
    │   └── Executor Agent: reads → ONB → executes → RF__phase-b
    │   └── After RF, run /tfw-review for review
    │
    └── ... repeat per Phase
```

Each Phase Agent starts with full context loading.
Coordinator maintains the Master HL for continuity.

## Anti-patterns

> Full generic list → conventions.md §14. Role-specific items below:

- Executor continues past Phase 3 — must STOP after RF
- Executor writes REVIEW file — **🔒 Role Lock violation**
- **🔒 Executor MUST NOT write HL, TS, REVIEW, or change scope** — Role Lock violation
