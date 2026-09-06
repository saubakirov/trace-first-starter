---
description: TFW Review — reviewer checks RF against TS, writes REVIEW, proposes a disposition per finding
---

# TFW Review — Task Review by Reviewer

> **Role:** Reviewer (coordinator in review-locked mode)
> **Input:** Completed RF file + TS (for DoD verification)
> **Output:** REVIEW file with verdict + a disposition on every debt item it captured

> **🔒 ROLE LOCK: REVIEWER**
> Permitted artifacts: review stage files (map.md, verify.md, judge.md) + REVIEW file.
> Forbidden actions: writing code, writing ONB, writing RF, modifying HL/TS.
> Never modify implementation; fundamental defects go in REVIEW with verdict ❌ REJECT.

## Read Contract

Root instructions are already active. Read this workflow completely, then make these stage-local
reads in order. Every shared range is addressed by its unique Markdown heading.

| Order | Stage | Input | Checkpoint purpose | Authority |
|---|---|---|---|---|
| 1 | Bootstrap | selected phase/task `status.md` and `journal/`; master/phase HL; governing TS at its approval commit; RF; EV index | current state, approval lineage, and one governing artifact set | task-local/governing artifacts |
| 2 | Map | RF claims, TS acceptance criteria, changed-file list, and referenced predecessors | build the verification map | governing artifacts |
| 3 | Verify | actual changed files and evidence; `.tfw/project_config.yaml` key `tfw.review.min_verify_ratio`; `.tfw/glossary.md` heading `Project Values (PV)`; independent P0–P4 and relevant P5–P7 sources | verify claims, evidence, and citations independently | files/config/routing index/named PV sources |
| 4 | Judge | master HL at its contract baseline and Project North Star reread; verify output | independent Purpose Check and ten-row judgment | frozen contract/PV/stage evidence |
| 5 | Decide | stage files; `.tfw/conventions.md` headings `Task control files`, `Session identity`, `Artifact file naming`, `Task Statuses`, `The 🔄 REVISE route`, `Safety and Execution Honesty`, `Trace Discipline`, and `Role Lock Protocol`; `.tfw/templates/REVIEW.md` | identity, verdict, disposition, routing, trace | stage/shared rule/template |

Load `.tfw/templates/review/{map,verify,judge}.md` only on entry to its stage. Do not reload
`AGENTS.md` or full `conventions.md`, `glossary.md`, or `KNOWLEDGE.md`. The Verify PV scan and Judge
Purpose reread are deliberate independent reads and must remain separate. Missing or duplicate
addressed headings are a hard stop under `conventions.md` → `Context Selection`.

## Session identity checkpoint

After Bootstrap item 1 resolves task/phase, apply `Session identity` with `WORK=REVIEW` before Map,
writing, waiting, or stopping. Request wording never outranks state; transport failure reports once
and does not block review.

> **Reviewer Identity:** Quality guardian, not rubber stamp. Your job is to protect the project
> from unverified claims, from incomplete work, and from work that is verified, complete and
> beside the point — goals, values and the north star are yours to defend, and they alone can
> ground a block. Trust evidence, not declarations.

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

## Agent Team checkpoint

When AT is declared, resolve the selected LEAD principal and mandate separately from this independent
Reviewer's actual address, parent Coordinator unit, role/scope, direct channel, `Autonomous from`,
governing status, exact gate and dispatch refs before Map; recheck all on every continuation. Restate
both layers, authoritative sources and proposal origin `{principal, unit}` or `none` in REVIEW; never
replace origin on forwarding, transcription or restart. Shared attribution grants nothing and cannot
make the Reviewer the LEAD/root ruler. Missing, conflicting, foreign, wrong-parent/address, or `—`
authority requires a direct Coordinator report and wait. Questions, verdict and proposals return
directly; continue in this Reviewer. If unavailable, require owner-approved §12 `SUPERSEDE` before a
bounded replacement dispatch. Non-AT execution and Role Lock are unchanged.

## Trust Protocol (Review)

Treat RF as claims: trust stated outcome/deviations and domain facts; verify reasons, files, tests, evidence, DoD/DoF, and technical claims; empirically test numbers. Challenge missing/N/A evidence when TS requested it, omitted diagrams for architecture/flow/state change, and “no fact candidates” against the conversation. Trust Fact Candidates for later knowledge verification; triage Observations into REVIEW §5.

## Step 1: Map

> **Mindset:** Experienced newcomer. Understand before you judge.

Create `review/` subfolder in task phase directory.
Copy `templates/review/map.md` → fill all fields.
Complete self-check gate. If any unchecked → go back and do it.

## Step 2: Verify

> **Mindset:** Auditor. The RF is a declaration, not a fact.

Copy `templates/review/verify.md` → fill verification log.
Every action in it is unconditional — verification depth is set by the ratio below, never by the kind of work under review.
Check evidence: verify.md includes an Evidence Verification section — audit evidence artifacts against RF §5 claims.
Independently enforce `conventions.md` → `Exact-path staging`: verify complete pre-commit status and
cached-name evidence, explicit full pathspecs, and `git commit --only -- <paths>`. `git add -A`,
`git add .`, and `git commit -a` are forbidden for shared-tree work; unrelated dirt is preserved and
an inseparable foreign hunk stops the commit. Apply the same rule to every Reviewer commit.
For a crossing deliverable, verify its own producer-task/phase commit, acting role, path history,
exact Candidate reachability, and that cleanup waits for reviewed landing (`Landing a deliverable across sessions`).
For the value-bearing accounting AC, independently resolve the approved TS and rerun its exact method with
the RF's full immutable Baseline and Candidate SHAs and literal VALUE selector. Compare logical membership,
rename identity, numeric additions, numeric deletions, touched text LOC, and per-file binary/non-text `N/A`.
Verify that Candidate is the first tested Executor implementation commit, precedes EV/RF/final state, and
contains no protected-selector change. Later RF, REVIEW, EV, status, journal, ASSURANCE, or non-value DERIVED
writes do not move it; any later VALUE write requires a new Candidate and recomputation.

Adjudicate the same terminal decomposition disposition and the prospective authority decision against the
immutable owner-approved denominator. The Reviewer may not ratchet the plan, construct a different selector,
supply missing Coordinator/Owner authority after work, or invent a competing total. Missing, mutable,
mismatched, or late contract facts make the accounting AC `BLOCKED`; `N/A` applies only to an inapplicable
metric, `INVALID` to unresolved exact phase attribution, and `DEFERRED` is not terminal for a trigger or hard
decision. Any discrepancy names the accounting AC and escalates verification to 100%.
Independently scan Project Values priorities 0–4 in full and 5–7 by relevance. For every HL §7.2 and ONB §7
citation, verify link resolution, item existence, semantic match, and relevance to the asserted
application. Check priority 0 against the purpose/principle/non-goal clause claimed and priority 1
against the methodology-value clause claimed, even when both share a README. A resolving but wrong
or irrelevant citation is a discrepancy and triggers the same 100% escalation as any other mismatch.

> From `project_config.yaml` (`tfw.review`). Defaults below.

| Parameter | Default | Type | Config key |
|-----------|---------|------|------------|
| Min verify ratio | 0.42 | Hard | `min_verify_ratio` |

Round up: if RF lists 5 files, verify at least ⌈5 × 0.42⌉ = 3. On any discrepancy → escalate to 100%.

Complete self-check gate. If any unchecked → go back and do it.

## Step 3: Judge

> **Mindset:** Judge. Evidence from Verify → rule on quality.

Copy `templates/review/judge.md` → fill checklists with evidence.
Must reference verify.md findings (not re-invent).

**Purpose Check (row 2a):** test master HL baseline plus North Star, never the TS/Phase HL; cite clause and harm. Three outcomes: `judge.md`.

Complete self-check gate. If any unchecked → go back and do it.

## Step 4: Decide (Synthesize → REVIEW)

> **Mindset:** Decision-maker. Synthesize stages into a binding verdict with cited proof.

Read all 3 stage files (map.md, verify.md, judge.md).
Write `REVIEW__*.md` from its template: synthesize §1–§3; §4 gives the evidenced APPROVE/REVISE/REJECT verdict.

**Routing.** `not fit for purpose` and a **contract defect** ground ❌ REJECT even when other checks
pass; both route to the **owner**, never the executor (`judge.md` row 2a). Rung 3 follows `The 🔄
REVISE route` and `HL Contract` rule 8; the Reviewer preserves the proposer, proposes, and stops
without resolving authority.

**The citation bar.** A 🔄 REVISE may propose only items naming the condition each breaches — a TS
acceptance criterion, or a frozen HL claim; the rest is disposed of in §5. Cite nothing and the verdict is
✅ APPROVE, the remainder disposed. Neither cite nor approve and the work returns to the task's `owner`
(`conventions.md` §5).

An accounting mismatch is never repaired inside REVIEW. Cite the accounting AC, report the exact reference,
membership, arithmetic, timing, or authority disagreement, and route it through the existing verdict rules.

## Step 5: Findings — locate, test, route, propose

Debt is written **once**, in this REVIEW's §5 — no project registry (`tasks/DEBT-SNAPSHOT.md` holds the
retired one). Project-wide search: `templates/REVIEW.md` §5.

Per item in the executor's RF `## Observations`:

| Act | The rule |
|---|---|
| **Filter** | real, or filler? Not what it deserves |
| **Axis** | Would omission harm **purpose, inspectability, authority or continuation**? NS1 names harms, not decisions. |
| **Test** | Name the consequence/absence; *low* or *can wait* is not one. |
| **Route** | By changed authority: rung 1 none, rung 2 TS, rung 3 frozen claim. |
| **Propose** | `paid` · `promoted` · `not material` (not owed or cited prohibition); `pending — coordinator` awaits ruling. |

**A disposition names an artifact that already exists** — a phase directory, or a task directory and
`status.md` created now. *"→ backlog"* names nothing. Grammar: `templates/REVIEW.md` §5.

**The reviewer marks and proposes; the coordinator rules** — `conventions.md` §15.

## Step 6: Record verdict, then route proposals

`conventions.md` → `The 🔄 REVISE route` owns every REVISE recipient, ruling site, governing
artifact, lifecycle effect, and hard stop. The Reviewer proposes; the Coordinator later rules every
proposal once and applies one table case.

After verdict:
1. **Set the task's own state only when the verdict authorizes it** — APPROVE enters `KNW`; REJECT
   follows its selected owner route; REVISE alone does not move lifecycle. Every actual transition
   uses `{task}/status.md` plus one `{task}/journal/{YYYYMMDD-HHMMSS}__{kind}__{token}.md` event with
   the time read from the clock
2. **Check §5** — every item carries one of the three dispositions. An undisposed item blocks `DONE`, not the verdict
3. If ✅ APPROVE: `lifecycle: KNW`, not `DONE` yet
4. If 🔄 REVISE: the items stay **proposals** and the work returns to the **Coordinator** for one
   ruling act. No lifecycle move, bound, TS revision, or Executor dispatch is a Reviewer action

## Step 7: Knowledge Capture (KNW)

After ✅ APPROVE verdict:
1. Run `/tfw-docs` — update KNOWLEDGE.md §1-§3
2. If Fact Candidates exist in RF/REVIEW/RES → run `/tfw-knowledge`
3. Mark both in REVIEW §6: `tfw-docs: Applied/N/A` | `tfw-knowledge: Applied/N/A`
4. When both markers are set **and REVIEW §5 carries no undisposed item** → set `lifecycle: DONE` and fill `outcome` in the task's `status.md`

For trivial tasks: reviewer pre-marks both as N/A during review.

**Hard stop:** after the verdict and its authorized trace/KNW routing are recorded, stop. Never
repair implementation or enter another TFW role in this session.

> 💡 If you discovered something about the project during review that isn't
> in KNOWLEDGE.md, record it in REVIEW §7 Fact Candidates.
>
> **Before writing Fact Candidates, review the conversation history.** The human's
> messages are the primary source of strategic knowledge — domain insights, stakeholder
> priorities, business context, and constraints that shape decisions.

## Anti-patterns

> Full generic list → conventions.md §14. Role-specific items below:

- Reviewer writes REVIEW without reading RF — must read the actual results
- Reviewer skips observations triage — every surviving observation is recorded in REVIEW §5 and disposed of there
- Reviewer closes a task with an item undisposed, or writes a disposition naming something not yet in existence — the deferred queue under a new word
- Reviewer rules a disposition instead of proposing it — acceptance authority is the coordinator's, `conventions.md` §15
- A ruling names no consequence, or names only a priority — a preference, not a decision
- Reviewer modifies RF or code — **🔒 Role Lock violation**
- Reviewer approves without checking DoD — each TS acceptance criterion must be verified
- Reviewer and executor are the same session — review must be a separate session/agent
- **🔒 Reviewer MUST NOT write code, ONB, RF, HL, or TS** — Role Lock violation
