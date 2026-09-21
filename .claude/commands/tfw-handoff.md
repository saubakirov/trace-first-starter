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

## Read Contract

Root instructions are already active. Read this workflow completely, then select inputs in this
order. Every shared range is addressed by its unique Markdown heading.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | selected phase/task `status.md` and `journal/` | current state, authority, and lineage before all other material | task-local |
| 2 | master HL, phase HL when present, and the highest approved TS lineage | frozen purpose, phase derivation, and one governing order | governing task artifacts |
| 3 | prior REVIEW only on a returned REVISE; then artifacts referenced by the governing TS | round basis and declared inputs | governing task artifacts |
| 4 | `.tfw/project_config.yaml` → `tfw.scope_budgets` | VALUE decomposition triggers and delegated-authority multiplier | project configuration |
| 5 | `.tfw/conventions.md` headings `Task control files`, `Session identity`, `Artifact file naming`, `Task Statuses`, `Safety and Execution Honesty`, and `Anti-patterns (prohibited)` | state/event writes, identity, revisions, lifecycle, evidence honesty, prohibitions | shared rule |
| 6 | HL §7.2 citations, then relevant implementation files named by the TS | inherited decision context and implementation facts | named source |
| 7 | `.tfw/templates/ONB.md`, `.tfw/templates/evidence/EV.md`, and `.tfw/templates/RF.md`, each only at its gate | output form | template |

Do not reload `AGENTS.md` or full `conventions.md`, `glossary.md`, or `KNOWLEDGE.md`. On a revision
return, add the highest TS, prior REVIEW, and lineage range; do not reread unchanged HL, state, or
shared authority in the same session. Missing or duplicate addressed headings are a hard stop under
`conventions.md` → `Context Selection`.

## Session identity checkpoint

After Read Contract item 1 resolves the selected task/phase, apply `Session identity` with
`WORK=EXEC` before ONB analysis, writing, waiting, or stopping. Request wording never outranks state;
transport failure reports once and does not block execution.

## Activation and routing checkpoint

Before ONB analysis or any material work, resolve the exact `/tfw-handoff` activation, selected
task/phase, lifecycle gate, actual Executor unit, and owner-direct, delegated, or continuation source.
Read the complete routing spine from `status.md`. Total absence is legacy-readable but cannot activate;
partial fields, a provisioned task, role prompt, briefing, wait result, implicit latest session,
foreign dispatch, wrong role/address/parent/scope, or authority mismatch is a pre-work refusal.

For delegated activation, verify the cited immutable mandate and direct Coordinator dispatch. Resolve
stable principal attribution only when that mandate explicitly requires it; ordinary owner-direct
activation invents no agent principal. Record actual producer unit, parent `coordinator_route`,
activation/dispatch source, exact `coordination_authority`, and originating proposer or `none` in ONB
and RF. Recheck the spine on continuation.

Under `tfw-gates-only`, send every status change, question, gate and durable return only to this
Executor's `coordinator_route`. Do not send material work to peers, owner or GATEWAY. A Coordinator
answer is accepted only as a valid task-local `gate_answer` event citing status, ONB, and governing
HL/TS. The Executor never writes or self-answers that event.

## Returning after a 🔄 REVISE

A REVISE reaches the Executor only after the Coordinator applies `conventions.md` →
`The 🔄 REVISE route`. Resolve one accepted bound in this order:

1. **Rung 1 only:** lifecycle is still `RF`; the existing approved TS remains the implementation
   order, and the live REVIEW contains the Coordinator's ruled closed return bound. No TS sibling is
   required or allowed merely for this case.
2. **Any rung 2, including mixed rung 1 + 2:** lifecycle is `TS_DRAFT`; the highest approved
   `TS__{ID}__rev{N}.md` sibling contains the complete ruled round and governs execution.
3. **Rung 3:** accept only after `HL Contract` rule 8 resolves a valid terminal verdict leaving an
   executable bound. Pending/unresolved authority is a hard stop, never an Executor decision.

Then read the live REVIEW for the cited findings and Coordinator rulings. If state, recipient, or
artifact does not match one table row, record the contradiction and stop.

**What is not re-done.** Approved prior work, answered ONB questions, or evidence for ACs not returned.

**Round artifacts:** The TS and the REVIEW take **siblings** named `…__rev{N}.md`; the RF and the ONB are **appended to** with numbered touched sections so rejected results remain openable. Only the Coordinator moves TS. → `Artifact file naming`

**What is not yours.** An item still marked `pending — coordinator`, a rung-2 round without its TS
revision, or a rung-3 round without the resolved ruler's valid terminal verdict is not executable. Record the missing authority
and **stop** — never rule the item, change the TS, or widen scope yourself.

## Knowledge at use and return

Read `conventions.md` headings `Current knowledge use` and `Knowledge handover` at the relevant
use/transfer checkpoint. Required PV/HL citations include relevant new records and incoming relations
to exact legacy/record identities; source content is evidence, never authority. Keep scope, source,
grounds, disposition, producer and unresolved conflicts explicit before applying a claim.
Before each actual Executor interim/final or stage/iteration return, preserve available material insight
in the existing role/stage section. A necessary stopped/interim fallback uses the handover template
under the owning task; no file per person or copied source corpus. Return actual source/version,
producer/unit, inspected context and continuation to the authorized Coordinator. Justified-none cites
inspected scope; unavailable context and its missing decision are not none. Retain rejected work with
its real state. A required unresolved effect stays open; no private context or successful return is
invented. Qualification and independent acceptance remain their existing owners' work.

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

4. **Commit ONB using Commit Attribution; push only after explicit user approval** — the onboarding report is a first-class artifact.
   Before every commit, enforce `conventions.md` → `Exact-path staging`: read full
   status and cached names, stage explicit full paths, and use `git commit --only -- <paths>`.
   `git add -A`, `git add .`, and `git commit -a` are forbidden for shared-tree work. Preserve unrelated
   dirt; STOP on an inseparable foreign hunk.
5. **Resolve blocking questions** — do NOT proceed while any blocker lacks a valid `gate_answer`.
   If no blockers exist, the valid activation and approved TS are sufficient; no second execution
   permission is invented. Report the status change to `coordinator_route`.

   > **ONB answers:** if HL/TS/KNOWLEDGE does not answer, the Coordinator obtains the ruling through
   > `owner_gateway` and writes the immutable event; the Executor only cites its operational effect.

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
   - Perform every authorized local action needed by the approved TS
   - Stop and report to `coordinator_route` when a required action exceeds the activation or authority

   **Execution Loops:** for `[depends: AC-X]`, verify the prerequisite AC gate passes before starting the dependent AC. Independent ACs may run in any order.

8. **Run tests** — satisfy the TS verification section for the actual result. Reuse a recorded check
   only when its relevant inputs/output, oracle/authority and environment assumptions still apply;
   name that basis in existing evidence. Changed or uncertain dependencies require affected checks.
9. **Build gate** — satisfy the build/compile command from the TS verification section with applicable
    evidence; run it when the required output or its evidence is changed, missing or uncertain.
    If build fails → fix BEFORE writing RF. Never write RF with failing build.

10. **Fix the Candidate** — after every required `VALUE` and `ASSURANCE` change is complete and the
    required targeted/full tests pass, create the first immutable Executor implementation commit. Its
    full SHA is Candidate. Do this before creating or updating EV or RF and before the RF transition.
    Recheck that its complete changed-path set is contained by the approved VALUE+ASSURANCE selector plus
    already-authorized task-local TRACE. A later excluded-only TRACE/ASSURANCE/non-value DERIVED write
    does not move Candidate; any later VALUE write requires a new Candidate and full recomputation.
    For cross-session landing, record producer task/phase and keep the exact Candidate reachable;
    never remove the worktree before reviewed landing (`conventions.md` → `Landing a deliverable across sessions`).

    A selected stable uncommitted sibling trace is admissible only when the approved TS/RF names its
    exact path, producer task and phase, relationship to this unit, and semantic effect. Record that
    selection in EV/RF and stage only the current unit's deliverable. Do not wait for sibling `DONE`
    and do not copy the sibling into a second result.

11. **Collect evidence** — create the phase/task `evidence/` folder, open
    `.tfw/templates/evidence/EV.md`, and record the actual environment and one result per TS AC.
    Use only VERIFIED / DEFERRED / BLOCKED / N/A, give every VERIFIED row a resolving artifact,
    explain every non-VERIFIED row, summarize the verdict counts, and index any attachments.
    Resolve the approved TS from its approval commit and add exactly one dedicated accounting row. Run
    its exact NUL-safe method with the same full Baseline and Candidate SHAs; record actual VALUE
    membership, additions, deletions, touched LOC, trigger disposition, immutable-denominator authority
    result, decision timing, and the command. Missing, mutable, mismatched, or late facts are `BLOCKED`;
    `N/A` is only for an inapplicable metric.
    - Uncollectable evidence is DEFERRED/BLOCKED with its exact missing environment/device/deployment; never omit it.
    - Record claim-relevant source/output identity, oracle/authority and environment assumptions only
      as needed to assess applicability. Later carrier changes do not give blanket PASS or invalidate
      unrelated checks. Changed final accepted output remains owed to the Coordinator and independent
      Reviewer under `conventions.md` → `Closing and record recovery`; the Executor never accepts it.
    - Proactively configure available evidence tools.
    - RF §5 says `See [EV file](...) for evidence details.` plus verdict summary.

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

Per phase: Coordinator derives Phase HL/TS and gets exact approval; Executor produces ONB, implementation, evidence, and RF; a separate `/tfw-review` Reviewer issues REVIEW before the next dependent phase.

## Anti-patterns

> Full generic list → conventions.md §14. Role-specific items below:

- Executor continues past Phase 3 — must STOP after RF
- Executor writes REVIEW file — **🔒 Role Lock violation**
- **🔒 Executor MUST NOT write HL, TS, REVIEW, or change scope** — Role Lock violation
