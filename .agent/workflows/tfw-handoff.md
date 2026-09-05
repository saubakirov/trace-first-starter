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

## Read Contract

Root instructions are already active. Read this workflow completely, then select inputs in this
order. Every shared range is addressed by its unique Markdown heading.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | selected phase/task `status.md` and `journal/` | current state, authority, and lineage before all other material | task-local |
| 2 | master HL, phase HL when present, and the highest approved TS lineage | frozen purpose, phase derivation, and one governing order | governing task artifacts |
| 3 | prior REVIEW only on a returned REVISE; then artifacts referenced by the governing TS | round basis and declared inputs | governing task artifacts |
| 4 | `.tfw/project_config.yaml` → `tfw.scope_budgets` | VALUE decomposition triggers and delegated-authority multiplier | project configuration |
| 5 | `.tfw/conventions.md` headings `Task control files`, `Artifact file naming`, `Task Statuses`, `Safety and Execution Honesty`, and `Anti-patterns (prohibited)` | state/event writes, revisions, lifecycle, evidence honesty, prohibitions | shared rule |
| 6 | HL §7.2 citations, then relevant implementation files named by the TS | inherited decision context and implementation facts | named source |
| 7 | `.tfw/templates/ONB.md`, `.tfw/templates/evidence/EV.md`, and `.tfw/templates/RF.md`, each only at its gate | output form | template |

Do not reload `AGENTS.md` or full `conventions.md`, `glossary.md`, or `KNOWLEDGE.md`. On a revision
return, add the highest TS, prior REVIEW, and lineage range; do not reread unchanged HL, state, or
shared authority in the same session. Missing or duplicate addressed headings are a hard stop under
`conventions.md` → `Context Selection`.

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

A REVISE reaches the Executor only after the Coordinator applies `conventions.md` →
`The 🔄 REVISE route`. Resolve one accepted bound in this order:

1. **Rung 1 only:** lifecycle is still `RF`; the existing approved TS remains the implementation
   order, and the live REVIEW contains the Coordinator's ruled closed return bound. No TS sibling is
   required or allowed merely for this case.
2. **Any rung 2, including mixed rung 1 + 2:** lifecycle is `TS_DRAFT`; the highest approved
   `TS__{ID}__rev{N}.md` sibling contains the complete ruled round and governs execution.
3. **Rung 3:** do not accept a handoff until the owner verdict leaves an executable bound. A pending
   amendment is an exact hard stop, not an Executor decision.

Then read the live REVIEW for the cited findings and Coordinator rulings. If state, recipient, or
artifact does not match one table row, record the contradiction and stop.

**What is not re-done.** Work the prior review approved, ONB questions already answered, and evidence already collected for an acceptance criterion the round does not return.

**The round's artifacts** — grammar in `conventions.md` §4. The TS and the REVIEW take **siblings**, `…__rev{N}.md`, never an overwrite. The RF and the ONB are **appended to**: one new numbered subsection per round, in every section the round touches, because the rejected version must stay openable. The TS is the coordinator's and moves only by their act.

**What is not yours.** An item still marked `pending — coordinator`, a rung-2 round without its TS
revision, or a rung-3 round without an owner verdict is not executable. Record the missing authority
and **stop** — never rule the item, change the TS, or widen scope yourself.

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
3. **Write ONB file** — open `.tfw/templates/ONB.md` at this gate and fill every required section.

4. **Commit ONB using Commit Attribution; push only after explicit user approval** — the onboarding report is a first-class artifact
5. **Wait for user approval** — do NOT proceed until all blocking questions resolved. An already
   approved AG execution grant satisfies the authorization gate when the ONB records no blockers.

   > **Coordinator ONB answer protocol:** When answering blocking questions — if the answer is not explicitly stated in HL, TS, or KNOWLEDGE.md, present 2-3 options with tradeoffs. Do not decide on behalf of the stakeholder.

6. **Set the task's own state** — after the bound resolves, set `lifecycle: ONB` from the table's
   required prior state (`RF` for rung 1 only; `TS_DRAFT` for rung 2/mixed), update `status.md`, and
   append a `handoff` event to `{task}/journal/` as
   `{YYYYMMDD-HHMMSS}__{kind}__{token}.md` — the time read from the clock, the token drawn not chosen.
   No file outside this task directory changes.

## Phase 2: Execution

**Scope gate — value-bearing.** Before every implementation write, compare the intended path with the
approved TS selector and any M1–M6 protected selector. Compare only planned/forecast `VALUE` logical
files and touched text LOC with `.tfw/project_config.yaml` → `tfw.scope_budgets`; `ASSURANCE`, `TRACE`,
and non-value `DERIVED` volume never creates a delivery overrun. The two decomposition triggers are soft
prompts and require their recorded terminal disposition, not a quality veto. The owner-approved VALUE
plan is the immutable denominator. Stop before any added VALUE path, any protected-boundary change, any
forecast at or above `owner_escalation_multiplier`, or growth from an applicable planned zero. The
Coordinator may rule only prospectively below that ceiling inside every unchanged boundary; the Executor
never widens or approves scope.

7. **Implement** — follow TS step by step:
   - For code changes: write production-ready code, no placeholders
   - For CL tasks: present commands/SQL to user, wait for execution
   - For AG tasks: create artifacts directly

   **Execution Loops** — if TS acceptance criteria have `[depends: AC-X]` annotations (meaning one AC must be verified before another can start): verify the prerequisite AC gate passes before starting the dependent AC. Example: if AC-2 has `[depends: AC-1]`, verify AC-1 is complete before implementing AC-2. Independent ACs (no `[depends]`) may be implemented in any order.

8. **Run tests** — as specified in TS verification section
9. **Build gate** — run build/compile command from TS verification section.
    If build fails → fix BEFORE writing RF. Never write RF with failing build.

10. **Fix the Candidate** — after every required `VALUE` and `ASSURANCE` change is complete and the
    required targeted/full tests pass, create the first immutable Executor implementation commit. Its
    full SHA is Candidate. Do this before creating or updating EV or RF and before the RF transition.
    Recheck that its complete changed-path set is contained by the approved VALUE+ASSURANCE selector plus
    already-authorized task-local TRACE. A later excluded-only TRACE/ASSURANCE/non-value DERIVED write
    does not move Candidate; any later VALUE write requires a new Candidate and full recomputation.

11. **Collect evidence** — create the phase/task `evidence/` folder, open
    `.tfw/templates/evidence/EV.md`, and record the actual environment and one result per TS AC.
    Use only VERIFIED / DEFERRED / BLOCKED / N/A, give every VERIFIED row a resolving artifact,
    explain every non-VERIFIED row, summarize the verdict counts, and index any attachments.
    Resolve the approved TS from its approval commit and add exactly one dedicated accounting row. Run
    its exact NUL-safe method with the same full Baseline and Candidate SHAs; record actual VALUE
    membership, additions, deletions, touched LOC, trigger disposition, immutable-denominator authority
    result, decision timing, and the command. Missing, mutable, mismatched, or late facts are `BLOCKED`;
    `N/A` is only for an inapplicable metric.
    - If evidence can't be collected (no environment, no device, no deployment): mark DEFERRED or BLOCKED with the specific reason. Silent omission is a violation.
    - Proactively seek and configure tools (MCP servers, browser automation, CLI utilities) needed for evidence collection. Don't wait for tools to be handed to you.
    - RF §5 is a pointer to the EV file — write it as: `See [EV file](...) for evidence details.` + verdict summary.

## Phase 3: Write RF

12. **Pre-RF Gate** — open `.tfw/templates/RF.md`. Read all section headings before writing anything.

13. **Create RF file** — follow `.tfw/templates/RF.md` exactly. Fill every mandatory section,
    including §5 as an EV pointer plus verdict summary and §7–§9 with explicit `No …` when empty.
    Bind the full Candidate SHA, approval ref, actual VALUE membership with class/reason, additions,
    deletions, touched LOC, trigger disposition, deviations, and pre-work authority reference. RF reports
    the approved contract; it never creates a selector or supplies late authority.

14. **Set the task's own state** — `lifecycle: RF` in `{task}/status.md`, with a `transition` event in `{task}/journal/`, the time read from the clock

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
