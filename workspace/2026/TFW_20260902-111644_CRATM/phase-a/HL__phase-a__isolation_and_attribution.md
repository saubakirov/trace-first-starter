# HL — Phase A: Isolation and attribution for concurrent work

> **Date**: 2026-09-03
> **Author**: Coordinator (Claude Code)
> **Refreshed**: 2026-09-05 by Coordinator (Codex), after RCFR and the reviewed VBSA Phase A candidate
> **Task**: [TFW_20260902-111644_CRATM](../HL-TFW_20260902-111644_CRATM.md) — Contextual Roles and Agent Team Mode
> **Phase**: A of five · 🔴 · **Requires:** Independent
> **Status**: 📝 HL_DRAFT
> **Master contract**: 🔒 FROZEN — approved by saubakirov 2026-09-02, baseline recoverable per `conventions.md` §3 rule 15

> **This file is derivation-only** (`conventions.md` §3 rules 20–21). It restates master content and
> adds execution context: files, sequencing, phase-local risks. It carries **no §1, §5, §6 or §7** —
> vision, acceptance criteria, failure conditions and principles exist once, in the master HL. A Phase
> HL that authors them is a second, unapproved contract, and TFW-48's phase-a HL did exactly that with
> 10 DoD, 9 DoF and 10 principles of its own.
>
> **There is no §12 here either.** An amendment against a frozen claim goes to the master's §12,
> never to a phase file.

---

## What this phase discharges, from the master

| Master item | Phase A's share |
|---|---|
| §3 item 1 — concurrent work is isolated by a declared worktree protocol built on `git worktree` | **all of it** |
| §3 item 2 — attribution survives isolation: a landed deliverable names its producer | **all of it** |
| DoD 1 — the protocol answers six questions: location, a readable name, who creates, when it merges, who deletes, the disposition of a dead session's worktree | **all six** |
| DoD 2 — broad staging named and forbidden, exact-path staging required, both role surfaces carry it | **all of it** |
| DoD 3 — a crossing deliverable is recoverable from `git log -- <path>` by the task that produced it, with the TD-178 worked example | **all of it** |
| DoD 14 — no vendor name in `.tfw/` outside `adapters/` | this phase's share: the protocol declares a location and a naming grammar without naming a vendor's path as canon |
| DoD 16 — nothing executable | this phase's share: the protocol is prose over ordinary git commands. No script, no hook, no check |
| DoD 17 — debt disposed before the task closes | this phase's review captures; Phase E disposes |

Governing principles, all from the master §7 and none restated as new: P8 git owns the mechanism and
TFW owns the protocol · P9 nothing executable · P12 isolation is not a lock · P6 parallelism must not
corrupt the trace.

## 2. Current State (As-Is) 🟢 FREE

### The defect, four measured occurrences

| # | What happened | Class |
|---|---|---|
| 1 | A broad `git add` in the TFW-53/B session swept three of TFW-56's already-staged deletions into `fbdf443` | shared git index |
| 2 | TFW-53/E's board rows landed inside `8d9432b` `[claude-code/TFW-58/proposal/coordinator]`, whose body never mentions TFW-53 | wrong commit subject |
| 3 | TFW-60/A's own release: *"broad staging temporarily committed TFW-54/TFW-55 files… the release has not structurally prevented the recurring TD-144 failure"* — `judge.md` row 10, ❌ | shared git index |
| 4 | Research iteration 2 followed up a dispatch with `resume --last`; it attached to the owner's live Codex thread — 2.8 MB, 264 K tokens — answered from that thread's context and left a turn in it permanently | **shared session namespace** |

`knowledge/risk.md` F1 measured what was supposed to prevent occurrences 1 and 3: **a verbal staging
directive survived 0 of 1** against a broad `git add`, and three consecutive phases of one task
produced three different ad-hoc answers, none written down. Under D55 the commit subject is the only
record of which task a change belongs to, and the master contract's own baseline is recovered by a
subject filter — so a misattributed staging degrades the mechanism TFW-53 shipped.

**Occurrence 4 is a different class and only partly this phase's.** A worktree gives a session its own
index and its own files; it gives it nothing of its own in the vendor's session store. See §4
deliverable 6 for how this phase treats it and what it leaves to Phase D.

### What the canon says today

At `master` `8034d72`, `conventions.md` §4 → Commit Attribution still specifies only the
`[agent/task/scope/role]` subject grammar. No current or reviewed VBSA target contains a worktree,
staging, or landing rule. What changed is the context topology around the insertion: D73–D75 now
make each workflow own ordered reads by unique heading, and one manifest owns adapter copy routes.

### The incoming surface this phase edits

| File | Original draft | RCFR in `master` | reviewed VBSA candidate | Constraint |
|---|---:|---:|---:|---|
| `.tfw/conventions.md` | 11,269 words | 9,269 | 9,791 | Reference document: one rule body, separate §14 failure row |
| `.tfw/workflows/handoff.md` | **1,727** | **1,751** | **2,013** | Preserve its Read Contract and VBSA Candidate/accounting order; add only a short enforcement edge |
| `.tfw/workflows/review.md` | **1,699** | **1,894** | **2,102** | Preserve independent accounting replay; add only the reviewer-side edge |

The VBSA candidate changes the same three canonical paths plus four tracked adapter copies. Its
accepted value-bearing accounting makes the expected Phase A delivery surface **7 VALUE files**, far
below the 50-file and 5,000-touched-LOC soft triggers, while task traces and ordinary verification do
not spend that delivery budget. Those semantics apply only after VBSA lands.

The sharpest constraint remains attention, not configured scope. The workflows are already far past
F2 before this phase. Approved A4 and its owner-initiated successor A5 replace the impossible absolute
bound with minimum materially necessary growth: the TS states why a shorter reference, substitution
or cut would lose meaning, and EV records exact before/after counts.

### Worktree mechanics, as measured

| Fact | Source |
|---|---|
| An app-managed worktree is normally **detached** and tied to one chat, shares the repository's git metadata, and git permits a branch in only one worktree at a time | research iter1, G4 |
| **Nested subagents share the parent task's checkout** unless another boundary is created explicitly. A child relationship is not worktree evidence | research iter1, D2, E1 |
| Separate worktrees have separate indexes, which is what occurrences 1 and 3 needed and what no rule delivered in three attempts | research iter1, H3 🟢 |
| Cost bound: one handoff or branch step, plus one exact-path landing. Never benchmarked | research iter1, Q3 |
| The vendor's own worktrees live under `~/.codex/worktrees/{token}/{project}`. On 2026-09-05 there are **15 entries**, 3 readably named (`kz-intake-phase-a`, `-review`, `-smoke`), and two registered detached worktrees for this repository | direct recount after RCFR/VBSA |
| The two registered detached worktrees carry one VBSA lineage: the executor head is 23 commits ahead of `master`, while the reviewed Phase A point is 19 commits ahead. Main stays clean, but the result is not available there until landing | direct `git worktree`, `rev-list`, and status inspection, 2026-09-05 |
| So a finished run's measured residue is **litter, not a dangling tree** — cleanup is the cheaper half of disposition | research iter2, R2 |
| Neither `~/.tfw/` nor `%LOCALAPPDATA%\tfw\` exists on this machine. The protocol must state both POSIX and Windows locations rather than canonize one syntax | verified 2026-09-05 |

The readable-name finding matters for scope: three of the vendor's own directories already carry
task-shaped names, so a name a person can read back is not something this protocol has to win from a
vendor. It has to *specify* one.

## 3. Target State (To-Be) — derived from master §3 items 1 and 2

After this phase, three things are true that are not true today.

1. **A mutation-bearing autonomous run has its own working tree**, in a declared location, under a
   name a person reads back to its task and phase. Read-only delegates keep sharing the parent
   checkout, because they contend for nothing and pay no landing cost.
2. **Broad staging is named and forbidden**, on both role surfaces, in the form the executor and the
   reviewer each actually meet.
3. **A deliverable that crosses a session boundary is findable by the task that produced it**, because
   it lands in its own commit whose subject names that task and phase. When VBSA accounting applies,
   the exact Candidate commit remains reachable after landing and before worktree deletion.

### 3.1 Result Visualization

**The protocol as it will read** — this is the artifact, not a description of it:

```markdown
### Worktrees for concurrent work            (conventions.md §4, new subsection)

A run that MUTATES the repository under a delegated mandate takes its own working
tree. A read-only run does not: it contends for nothing and pays no landing cost.

  location   POSIX:   ~/.tfw/worktrees/{TASK-ID}__{phase}/
             Windows: %LOCALAPPDATA%\tfw\worktrees\{TASK-ID}__{phase}\
             Per machine, outside the project tree — the same split already used
             by bindings.yaml. A worktree a VENDOR created is the vendor's; this
             grammar names ours, and a foreign worktree is read, never renamed.

  name       {TASK-ID}__{phase}, extended to {TASK-ID}__{phase}__{principal}
             once principals exist (Phase B). NEVER renamed afterwards — a
             rename breaks every reference that already resolves, which is the
             rule task directories already live under.

  create     the coordinator, before dispatching a mutation-bearing run.
  land       when the run's role artifact exists and the phase's review has run;
             if a TS fixes an immutable Candidate SHA, that exact commit remains
             reachable. The transport and merge strategy remain outside Phase A.
  delete     the coordinator, AFTER the work is landed and verified — never
             before landing, verification, and Candidate reachability are checked,
             because the measured residue is litter and the measured loss is a
             detached commit with no durable landing path.
  dead run   the worktree is READ, its commits are landed by the rule below,
             and only then is it removed. A dead session's tree is evidence.
```

```markdown
### Staging                                   (conventions.md §4, new subsection)

In a shared tree, commit only an explicit full path list. `git add -A`,
`git add .` and `git commit -a` are forbidden — the verbal rule survived 0 of 1.

Before every commit, read all status and the staged set. Use exact pathspecs;
`git commit --only -- <paths>` prevents an already-staged sibling path from
riding along. A foreign hunk in one selected path is not separable by path:
STOP and report it. Never normalize or repair dirty work into your change.
```

```markdown
### Landing a deliverable across a session boundary        (conventions.md §4)

A deliverable committed by a session other than its producer goes in ITS OWN
commit, and the subject names the PRODUCER's task and phase. `role` stays the
acting role.

  wrong   [claude-code/TFW-58/proposal/coordinator] propose the revise protocol
          ← carries TFW-53/E's board rows; `git log -- README.md` shows no
            TFW-53/E commit for the deliverable of that phase          (TD-178)

  right   [claude-code/TFW-53/phase-e/coordinator] land the board rows

If the producer's TS names a VBSA Candidate SHA, landing keeps that commit
reachable. Recreating equivalent content under only a new SHA is not equivalent
evidence and cannot justify deleting the producer's worktree.
```

**Before and after, on the case that produced the rule:**

```
today                                                     after Phase A
────────────────────────────────────────────────────────  ────────────────────────────────────────────────
$ git log --format="%h %s" -- README.md                   $ git log --format="%h %s" -- README.md
5d0f86c [claude-code/TFW-53/phase-e/executor] correct…    5d0f86c [claude-code/TFW-53/phase-e/executor] …
8d9432b [claude-code/TFW-58/proposal/coordinator] pro…    a1b2c3d [claude-code/TFW-53/phase-e/coordinator]
                    ▲                                                        ▲
      the phase's own deliverable, filed under                its own commit, naming the phase
      another task, body silent about it                      that produced it
```

**What a reader gains, and it is the whole point:** `git log -- <path>` answers *which task delivered
this*, and the master contract's baseline recovery — a filter over commit subjects — keeps working
when several sessions write at once.

## 4. Deliverables, in order

Master §4 lists five. Order below is the one the executor should follow; items 6–7 are current
compatibility refinements, not new phase outcomes.

1. **`conventions.md` §4 — the worktree protocol.** All six questions answered: location, naming
   grammar, who creates, when it merges, who deletes, the disposition of a dead run's tree. Built on
   `git worktree`; no implementation of our own, and no script.
2. **`conventions.md` §4 — staging.** `git add -A`, `git add .` and `git commit -a` named and
   forbidden in a shared tree; `git diff --cached --name-only` before every commit; a sibling's hunk
   is reported and never committed; unrelated dirty work is preserved rather than normalized.
3. **`conventions.md` §4 — the landing rule**, with the TD-178 worked example above. It must stay
   **subject-based**: `knowledge/environment.md` F4 measured that `--grep` matches the whole message
   and cannot be made subject-only, and F3 that this shell rewrites a leading `/` in an argument. The
   rule must reintroduce neither.
4. **`workflows/handoff.md` — the executor's side.** Add the shortest addressed enforcement edge at
   each commit boundary; preserve the VBSA Candidate-before-EV/RF order. If the TS forbids a path,
   report it and name what must be landed. Any growth is the minimum materially necessary and carries
   the A5 necessity and exact-count evidence.
5. **`workflows/review.md` — the reviewer's side.** Require the same staging and landing check where
   the reviewer records its result; preserve independent VBSA accounting replay. Any growth is the
   minimum materially necessary and carries the A5 necessity and exact-count evidence.
6. **`conventions.md` §14 — anti-patterns**, one per measured occurrence, each naming its evidence:
   - broad staging with a sibling session live (occurrences 1 and 3);
   - landing another session's deliverable inside an unrelated commit (occurrence 2);
   - **a foreign caller resuming "the last session" instead of a session id** — it writes into a
     session nobody delegated (occurrence 4).
7. **Adapter parity under D73.** Synchronize the manifest-declared copies of the two changed
   workflows and prove byte parity. Do not change the manifest or create another copy list.

**Coordinator's decision on occurrence 4, so no ONB question is needed.** The anti-pattern lands here,
because Phase A is already opening §14 and the cost is one row. The **positive** rule — a dispatch
captures the returned session id and follow-up goes by id — belongs to Phase D, where dispatch is
specified. Phase A does not invent a dispatch field, and the worktree protocol says nothing about
session identity: a worktree isolates an index and files, and claiming it isolates a vendor's session
store would be exactly the over-promise master §7 P12 forbids.

## What this phase must NOT do

| Not here | Why | Where |
|---|---|---|
| Branch policy, merge strategy, or a second transport | Master DoF 11 | TFW-61 |
| A dispatch field, a session-id field, or any delegation grammar | Not this phase's subject | Phase D |
| A principal in the worktree name | Principals do not exist yet; the grammar must *admit* one without a rename | Phase B |
| A script, a hook, a check, or a test | Master DoF 2 and DoD 16, and NS3's runtime non-goal | — |
| Naming a vendor's path as canon | Master DoD 14 | — |
| Redefining VBSA classes, Candidate, triggers, or authority | Reviewed before this phase and outside its outcome | VBSA |
| Editing anything under `tasks/` | Owner ruling 2026-09-03: frozen, unmaintained, ignored | — |

## 7.2 Knowledge Citations 🟢 FREE

Phase-scoped additions to the master's §7.2. Principles are the master's; these are the items this
phase's own deliverables rest on.

| # | Source | Item | How it applies here |
|---|--------|------|---------------------|
| A1 | PV 0 — [`.tfw/README.md` #ns3](../../../../.tfw/README.md#ns3) | non-goal: *"a vendor-bound tool, runtime, model, interface, or memory feature"* | Why the protocol is prose over `git worktree` and not an implementation, and why a vendor's path is read rather than adopted |
| A2 | PV 1 — [#methodology-values](../../../../.tfw/README.md#methodology-values) | Structural Enforcement | Isolation replaces a directive measured at 0 of 1. The staging rule still ships, because isolation does not cover a shared tree that two sessions legitimately use |
| A3 | PV 3 — [`KNOWLEDGE.md`](../../../../KNOWLEDGE.md) D55 | The commit subject is the searchable record of declared context | The landing rule's entire justification |
| A4 | PV 3 — same D59 | recoverability ≠ locking | A worktree removes contention; it serialises nothing. Master §7 P12 |
| A5 | PV 3 — same D68 | Task-local state; a path is created once and outlives every state | The naming rule's "never renamed": the same reasoning that forbids moving a task directory |
| A6 | PV 7 — [`knowledge/risk.md`](../../../../knowledge/risk.md) F1 | A verbal staging directive survived 0 of 1; *"its grant must bound what may be **staged**, not only what may be **decided**"* | Deliverables 2, 4 and 5 |
| A7 | PV 7 — [`knowledge/environment.md`](../../../../knowledge/environment.md) F3, F4 | The shell rewrites a leading `/`; `--grep` matches the whole message | Deliverable 3 must not reintroduce either |
| A8 | PV 6 — [`knowledge/process.md`](../../../../knowledge/process.md) F30 | Capture without an enforcement site does not change behaviour | Why each rule lands in §4 *and* as a §14 row, and why neither is a substitute for the other |
| A9 | PV 7 — [`knowledge/constraint.md`](../../../../knowledge/constraint.md) F2 | Instructions degrade past ~1200 words | Deliverables 4 and 5 are already over it. Under approved A5, the TS justifies the minimum necessary delta and EV records exact before/after counts |
| A10 | PV 3 — [`KNOWLEDGE.md`](../../../../KNOWLEDGE.md) D73 | Workflow-owned ordered reads plus one adapter manifest | New convention headings must have an addressed consumer; adapter copies derive from the manifest, not a hand-maintained list |
| A11 | PV 3 — same D74, D75 | Selective primary and secondary role paths preserve semantics with less fixed context | Phase A must not restore a universal preamble or duplicate a full rule into every role |
| A12 | PV 4 — [`conventions.md`](../../../../.tfw/conventions.md) `Design Rules` | Token density, inline enforcement, progressive disclosure, adapter-safe commands | One canonical rule body plus short checkpoint edges; every command is exercised through its adapters |
| A13 | PV 6 — [`knowledge/process.md`](../../../../knowledge/process.md) F39 | A rule's delivery set is derived by search, including definition, tests, glossary, and copies | The TS derives the complete consumer/copy surface before implementation rather than trusting the 2026-09-03 file list |

## 8. Dependencies 🟢 FREE

| Dependency | Status |
|------------|--------|
| Master contract frozen and committed | ✅ 2026-09-02, one baseline commit |
| Research iterations 1 and 2 | ✅ complete; worktree mechanics and the census are theirs |
| RCFR | ✅ `DONE` and landed in `master`; D73–D75 are the current context contract |
| VBSA | 🟠 reviewed Phase A is `KNW`; closure Phase B is `ONB`; 23 commits at the executor head are not in `master`. **Dispatch blocker until `DONE` and landed** |
| Explicit-path staging, claimed by TFW-61's proposal as its own Git-mode deliverable | ✅ **taken by this phase**, recorded in the master §8 on 2026-09-03. TFW-61 has neither an HL nor a freeze; the second task to arrive must not re-author it |
| Per-machine TFW directory | ⬜ both POSIX `~/.tfw/` and Windows `%LOCALAPPDATA%\tfw\` are absent. The protocol declares platform locations; this phase creates only the worktree actually needed for execution |
| Principals | ⬜ Phase B. The naming grammar must admit one without a rename |
| Phase B, C, D, E | ⬜ all downstream of this phase |

## 9. Risks — phase-local 🟢 FREE

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| PA1. The reviewed incoming workflows are 2,013 and 2,102 words, so another inline rule body deepens the attention failure | High | High | Approved A5: one canonical body plus the shortest addressed edges; TS justifies any positive delta against a shorter reference/substitution/cut, and EV records exact before/after counts |
| PA2. The protocol drifts into branch and merge policy, taking TFW-61's subject | Medium | High | "When it merges" answers *at which lifecycle point*, never *by which strategy*. A merge command in the deliverable is the tripwire |
| PA3. The worktree is treated as a lock, and a later rule leans on it for serialisation | Medium | High | Master §7 P12 is quoted in the deliverable itself; nested children share the parent checkout, which is the measured counter-example |
| PA4. The naming grammar has to be reopened in Phase B when principals arrive | Medium | Medium | The grammar is specified as extensible now — `{TASK-ID}__{phase}` widening to `{TASK-ID}__{phase}__{principal}` — and existing names are never rewritten |
| PA5. The landing rule reintroduces the shell or `--grep` defects TFW-53 already paid for | Low | Medium | F3 and F4 are cited in the deliverable; the rule is subject-based by construction, and the recovery form in `conventions.md` §3 rule 15 is the shape to copy |
| PA6. This phase's own work reproduces occurrence 1 while writing the rule against it | Medium | High | The executor works in its own worktree from the first commit and stages by exact path from the first commit — the rule applies to the phase that writes it, before it is written down |
| PA7. `conventions.md` grows by restating in §4 what §14 also carries | Medium | Low | §4 states the rule; §14 states the failure and its evidence. One sentence each, no overlap |
| PA8. Selective loading makes the new convention true but unavailable at the checkpoint that needs it | High | High | Each consuming workflow names the exact heading or states the short rule inline; route coverage is derived from D73's manifest and D75's command census |
| PA9. Worktree landing recreates equivalent content under a new SHA, then deletes the only reachable VBSA Candidate | Medium | High | Landing preserves reachability of the exact Candidate commit; deletion waits for an explicit reachability check, without prescribing merge strategy |
| PA10. CRATM is dispatched while VBSA's 23-commit worktree lineage is still unlanded | Medium | High | Planning may continue; execution is blocked until VBSA is `DONE`, landed in the selected base, and the main tree is clean |

## 10. RESEARCH Case

**Phase-local N/A.** The isolation and attribution outcome has enough evidence, but the owner's
Helpdesk field run has reopened a master-level topology decision before any CRATM TS is dispatched:
peer session/task versus nested subagent, Claude-only provisioning, and exclusion or admission of
mixed-provider execution. Iteration 3 is approved and assigned to a dedicated Codex Researcher task
that reports to `Main Coordinator` through threads. Independently, VBSA must close and land before
this phase executes.

## 11. Strategic Insights

No phase-local addition. The owner's 2026-09-05 sequencing decision is recorded once as master S21:
known shared-file overlap is sequenced even when worktrees exist, because isolation does not land a
reviewed result.

---

*HL — Phase A: Isolation and attribution for concurrent work | TFW_20260902-111644_CRATM | refreshed 2026-09-05*
