# HL — Phase A: Isolation and attribution for concurrent work

> **Date**: 2026-09-03
> **Author**: Coordinator (Claude Code)
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

`conventions.md` §4 → Commit Attribution is **84 words**, one paragraph, unchanged since TFW-50. It
specifies the `[agent/task/scope/role]` subject grammar and nothing about staging, landing, or
isolation. There is no worktree protocol anywhere in `.tfw/`.

### The three files this phase edits, with the space available

| File | Now | Constraint |
|---|---|---|
| `.tfw/conventions.md` | 11,269 words, 1,073 lines | A reference document, not an instruction read start to finish, so `constraint.md` F2's 700–900 range does not apply to the whole. The discipline that does: a rule lands **once**, and §4 does not restate what §14 will carry as an anti-pattern |
| `.tfw/workflows/handoff.md` | **1,727 words** | Already past F2's ~1200 ceiling before this phase touches it. Master §7.1 therefore binds: growth is paid for by cuts in the same document |
| `.tfw/workflows/review.md` | **1,699 words** | The same. Both files carry an identical seven-workflow identity preamble that must not be orphaned |

This is the sharpest execution constraint in the phase, and it is not a style preference: two of the
three files have no room. The staging rule reaches them as the shortest form that still names the
prohibition, and whatever it displaces is named in the RF.

### Worktree mechanics, as measured

| Fact | Source |
|---|---|
| An app-managed worktree is normally **detached** and tied to one chat, shares the repository's git metadata, and git permits a branch in only one worktree at a time | research iter1, G4 |
| **Nested subagents share the parent task's checkout** unless another boundary is created explicitly. A child relationship is not worktree evidence | research iter1, D2, E1 |
| Separate worktrees have separate indexes, which is what occurrences 1 and 3 needed and what no rule delivered in three attempts | research iter1, H3 🟢 |
| Cost bound: one handoff or branch step, plus one exact-path landing. Never benchmarked | research iter1, Q3 |
| The vendor's own worktrees live under `~/.codex/worktrees/{token}/{project}`. **14 entries at the time of writing** (15 when iteration 2 counted, hours earlier — the set churns), **3 of them already readably named** (`kz-intake-phase-a`, `-review`, `-smoke`), and 6 token-named directories holding an **empty** project shell with no `.git` while `.git/worktrees/` holds one admin entry | research iter2, G5; re-counted here |
| So a finished run's measured residue is **litter, not a dangling tree** — cleanup is the cheaper half of disposition | research iter2, R2 |
| `~/.tfw/` **does not exist on this machine.** The binding mechanism the canon describes has never been used here | verified 2026-09-02 |

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
   it lands in its own commit whose subject names that task and phase.

### 3.1 Result Visualization

**The protocol as it will read** — this is the artifact, not a description of it:

```markdown
### Worktrees for concurrent work            (conventions.md §4, new subsection)

A run that MUTATES the repository under a delegated mandate takes its own working
tree. A read-only run does not: it contends for nothing and pays no landing cost.

  location   ~/.tfw/worktrees/{TASK-ID}__{phase}/
             Per machine, outside the project tree — the same reason bindings.yaml
             lives there: a project-local file can be gitignored but not
             sync-ignored. A worktree a VENDOR created is the vendor's; this
             grammar names ours, and a foreign worktree is read, never renamed.

  name       {TASK-ID}__{phase}, extended to {TASK-ID}__{phase}__{principal}
             once principals exist (Phase B). NEVER renamed afterwards — a
             rename breaks every reference that already resolves, which is the
             rule task directories already live under.

  create     the coordinator, before dispatching a mutation-bearing run.
  merge      when the run's role artifact exists and the phase's review has run.
  delete     the coordinator, AFTER the work is landed and verified — never
             before, because the measured residue is litter and the measured
             loss is a detached commit with no landing path.
  dead run   the worktree is READ, its commits are landed by the rule below,
             and only then is it removed. A dead session's tree is evidence.
```

```markdown
### Staging                                   (conventions.md §4, new subsection)

Stage by exact path. `git add -A`, `git add .` and `git commit -a` are forbidden
in a shared tree — a verbal version of this rule survived 0 of 1.

Before every commit, read the staged set: `git diff --cached --name-only`.
A path you did not produce is not yours to commit. Report the overlap; never
normalize it, and never repair someone's dirty work into your own change.
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

Master §4 lists five. Order below is the one the executor should follow; item 6 is a coordinator
decision recorded here so onboarding does not have to ask for it.

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
4. **`workflows/handoff.md` — the executor's side.** Stage by path; if the TS forbids you a file, say
   so in the RF and name what must be landed. **Paid for by a cut in the same file** — it is 1,727
   words and F2's ceiling is ~1200.
5. **`workflows/review.md` — the reviewer's side.** The same staging rule, in the form a reviewer
   meets it. Same payment rule; 1,699 words.
6. **`conventions.md` §14 — anti-patterns**, one per measured occurrence, each naming its evidence:
   - broad staging with a sibling session live (occurrences 1 and 3);
   - landing another session's deliverable inside an unrelated commit (occurrence 2);
   - **a foreign caller resuming "the last session" instead of a session id** — it writes into a
     session nobody delegated (occurrence 4).

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
| A9 | PV 7 — [`knowledge/constraint.md`](../../../../knowledge/constraint.md) F2 | Instructions degrade past ~1200 words | Deliverables 4 and 5 are already over it. Growth is paid for by cuts named in the RF |

## 8. Dependencies 🟢 FREE

| Dependency | Status |
|------------|--------|
| Master contract frozen and committed | ✅ 2026-09-02, one baseline commit |
| Research iterations 1 and 2 | ✅ complete; worktree mechanics and the census are theirs |
| Explicit-path staging, claimed by TFW-61's proposal as its own Git-mode deliverable | ✅ **taken by this phase**, recorded in the master §8 on 2026-09-03. TFW-61 has neither an HL nor a freeze; the second task to arrive must not re-author it |
| `~/.tfw/` on the owner's machine | ⬜ absent. The protocol declares the location; nothing in this phase creates it |
| Principals | ⬜ Phase B. The naming grammar must admit one without a rename |
| Phase B, C, D, E | ⬜ all downstream of this phase |

## 9. Risks — phase-local 🟢 FREE

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| PA1. Two of the three files have no word budget left, so the rule arrives as prose nobody finishes reading | High | Medium | The prohibition ships as the shortest form that still names the forbidden commands; every cut is named in the RF, and the reviewer checks the net word count of both workflow files |
| PA2. The protocol drifts into branch and merge policy, taking TFW-61's subject | Medium | High | "When it merges" answers *at which lifecycle point*, never *by which strategy*. A merge command in the deliverable is the tripwire |
| PA3. The worktree is treated as a lock, and a later rule leans on it for serialisation | Medium | High | Master §7 P12 is quoted in the deliverable itself; nested children share the parent checkout, which is the measured counter-example |
| PA4. The naming grammar has to be reopened in Phase B when principals arrive | Medium | Medium | The grammar is specified as extensible now — `{TASK-ID}__{phase}` widening to `{TASK-ID}__{phase}__{principal}` — and existing names are never rewritten |
| PA5. The landing rule reintroduces the shell or `--grep` defects TFW-53 already paid for | Low | Medium | F3 and F4 are cited in the deliverable; the rule is subject-based by construction, and the recovery form in `conventions.md` §3 rule 15 is the shape to copy |
| PA6. This phase's own work reproduces occurrence 1 while writing the rule against it | Medium | High | The executor works in its own worktree from the first commit and stages by exact path from the first commit — the rule applies to the phase that writes it, before it is written down |
| PA7. `conventions.md` grows by restating in §4 what §14 also carries | Medium | Low | §4 states the rule; §14 states the failure and its evidence. One sentence each, no overlap |

## 10. RESEARCH Case

**N/A — research is complete at the master level.** Two iterations, both `SUFFICIENT`, and no
hypothesis assigned to this phase remains open: H3 returned 🟢 for isolation with the cost bounded
qualitatively, which is what a protocol needs. The unresolved items that touch this phase are risks
above, not questions: no timed landing benchmark exists (PA1's sibling), and the fourth corruption's
positive rule is Phase D's by the decision in §4.

## 11. Strategic Insights

**None yet.** Nothing human-sourced has arrived that is specific to this phase and absent from the
master's §11.

---

*HL — Phase A: Isolation and attribution for concurrent work | TFW_20260902-111644_CRATM | 2026-09-03*
