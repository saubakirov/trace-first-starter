# Replays — TFW_20260902-112841_RDP (AC-3, AC-4, AC-7, AC-8)

> **Date**: 2026-09-02 · **Author**: Claude Code (Executor), on behalf of `saubakirov`
> **Method**: read-only throughout. `grep`, `awk`, `sed`, `wc`, `ls` only.
> **Declaration**: **no file in any project other than this one was created, modified, moved or deleted.**
> Each replay names the files it read. `git status` in the receiving project was not modified because
> nothing was written there — verified by the fact that only read commands were issued.

---

## Replay 1 — AC-3: re-ruling `TLD`'s nine real dispositions under the new grammar

**Read (this repository, read-only):**
`workspace/2026/TFW_20260830-194027_TLD/REVIEW__TFW_20260830-194027_TLD.md` §5. **Not edited** — it is a
closed review of a closed task.

**Population:** 9 rows, confirmed by count. **Not a sample.**

The new grammar asks two things of a ruling: (a) a **named consequence** or the named **absence** of one,
and (b) **which question it answers** — *not owed*, or *owed and forbidden to pay* with the barring clause
cited.

| # | Subject | Consequence named? | Which question | Ruling text changes? |
|---|---|---|---|---|
| 1 | Windows frontmatter path break | n/a — `pending — owner` is a waiting state, not an outcome | n/a | **no.** The new grammar keeps `pending — {role}`; the identifier rule forbids inventing a task directory, so the wait is correct |
| 2 | `review.md` over §11's word ceiling | yes — the absence: four of ten workflows breach a rule nothing enforces | *not owed* | **label only.** The ruling already names the absence; it must now say *not owed* in as many words |
| 3 | Blank lines inside the sealed region | yes — *"a history file's render shape costs nothing"*, and AC-1 forbids the fix | **owed and forbidden to pay** — clause cited (AC-1, P5) | ✅ **yes, substantively.** Filed as bare `not material` while the text argues the fix is barred |
| 4 | Uppercase names outside the project root | yes — *"the rule's purpose is served"* | *not owed* | **label only** |
| 5 | `paid` ambiguous for a reviewer who cannot write code | yes — DoF 10's ceremony cost of adding a canon sentence | **owed and forbidden to pay** — DoF item cited | ✅ **yes, substantively.** The row is the arguable one research flagged, and it resolves the same way |
| 6 | Retirement procedure stated twice | yes — the absence: *"neither is edited again, so there is nothing to drift"* | *not owed* | **no.** Already conforms |
| 7 | Nothing checks adapter-copy drift | yes — *"a checker is a new maintained artifact, which HL DoF 5 and TS §2 forbid outright"* | **owed and forbidden to pay** — clause quoted verbatim | ✅ **yes, substantively.** Filed as bare `not material` |
| 8 | RF/EV arithmetic understated | yes — the absence: *"no stop-and-report was owed either way"* | *not owed* | **label only** |
| 9 | `+247 %` attributed to 17 vs 19 days | yes — the absence: *"the percentage itself is right in both"* | *not owed* | **label only** |

**Result: 3 of 9 change substantively — rows 3, 5 and 7. Research scored 3 of 9 and named rows 3, 5 and 7.
It reproduces exactly, row for row.**

A refinement research did not separate: **four further rows (2, 4, 8, 9) gain the explicit label without
their argument changing.** They already named the absence of a consequence; what they lacked was the word
*not owed*. That is worth stating because it bounds the claim honestly — the grammar rewrites three
rulings and re-labels four, and it leaves rows 1 and 6 untouched.

**And the three that change share one shape**, which is A5's whole argument: on each, the reviewer argued
at length that the item mattered and then filed it under a word saying it did not. The new grammar makes
the record say what the reviewer actually concluded.

## Replay 2 — AC-4: `ai-first-devices` AFD-48 `phase-a` rev2 through the shipped route

**Read (external project, read-only):**
`/d/projects/research/ai-first-devices/tasks/AFD-48__device_bus_stall_hardening/phase-a/` —
`REVIEW__phase-a__bus_stall_hardening__rev2.md`, `…__rev3.md`, `…__rev4.md`, plus a directory listing.
**Nothing in that project was written.** TFW version there: 0.9.0.

> **Read this before running `git status` in that project.** It carries **four** pre-existing uncommitted
> entries that are not mine and predate this session: `M TECH_DEBT.md`,
> `M tasks/AFD-51__.../phase-d/HL__phase-d__prod_metrics_plane.md`, and two untracked paths under
> `tasks/AFD-46__operator_identity_and_rbac/`. The proof that none of them is this replay's is narrower and
> checkable: `git status --short -- tasks/AFD-48__device_bus_stall_hardening/` returns **empty**, and
> AFD-48 is the only directory this replay opened.

**rev2's verdict is 🔄 REVISE with six items.** Classified by *what the fix must change*:

| Item | Ordered | Rung | Why |
|---|---|---|---|
| 1 | Close all production opt-in paths; add a committed red-drill | **1** | implementation inside the approved TS |
| 2 | Scope the test compiler opt-in | **1** | implementation |
| 3 | *"Obtain coordinator amendments."* Ratify `RegistryApiTest` 49→50 and record the semantic AC-5 change **or** revert the implementation. *"An executor statement that the change is unavoidable is not an amendment."* | **2** | an acceptance criterion must change — the executor may not amend a TS |
| 4 | Restore trace truth in the RF | **1** | the executor's own artifact |
| 5 | Version the binding artifacts — Phase HL/TS and reviewer traces must exist in history, *"no executor-authored contract decisions"* | **2** | the coordinator must author and commit them |
| 6 | Correct Fact Candidate 6 | **1** | the executor's own artifact |

**Four rung-1 and two rung-2 in one verdict. Research measured four and two. Reproduces exactly.**

**What the old canon did with it, measured:** `🔄 REVISE` had one destination — *"back to execution (same
task)"* — so both rung-2 items went into *"Items to fix"*, a list only the executor reads. Item 3 returns
in **rev2, rev3 and rev4**, verbatim in intent each time (rev3: *"The coordinator must explicitly rule on
(a) the `RegistryApiTest` pin/exception policy and (b) AC-5's literal subscriber…"*; rev4: *"Obtain
coordinator amendments A and B"*, with the review stating outright that *"Reviewer cannot ratify the AC-5
semantic change or registry-pin policy"*). **No amendment was ever logged** — the phase directory holds
HL, ONB, TS, RF, four REVIEWs, `evidence/` and `review/`, and no journal at all.

**The same verdict through the shipped text:**

| | What the role receives |
|---|---|
| **Executor** | items 1, 2, 4 and 6, rung 1, back to execution with the round's **bound** naming exactly those four and nothing beyond them. `handoff.md`'s *Returning after a 🔄 REVISE* tells them the prior REVIEW is item 8 of Context Loading, that items marked `pending — coordinator` are **not theirs**, and that if the bound orders one and the TS has not moved they write that in the RF and **stop** |
| **Coordinator** | items 3 and 5 arrive as `pending — coordinator` **written beside the item** in REVIEW §5, not in a list addressed to someone else. They may change the TS to discharge them; that single change sets `lifecycle: TS_DRAFT`, **once for the round**, not once per item |
| **The task's state** | representable, which it was not before: `status.md` holds one `lifecycle` field and `conventions.md` §5 is single-valued, so a mixed-rung round had no state. The rung now travels with the item and `lifecycle` with the task |
| **The count** | the TS change discharges a finding, so it **continues** the same revision count — it does not restart it. Under the old *"can the existing TS accept it"* test a rung-2 finding restarted the count by construction |
| **The budget** | rev2 is revision 1. Had the TS been amended at rev3 and again at rev4, the ceiling of 2 would have been reached at rev4 and the work would have **stopped** and returned to `owner` instead of returning a fourth REVISE |

**What the route does not claim.** It does not make the coordinator act. It gives the item a channel to
someone who can discharge it and a state that keeps the task open until they do — which is the measured
difference between this arm and the same reviewer's `phase-b` S3 Block 1, where a rung-2 item addressed to
the coordinator closed at rev3.

## Replay 3 — AC-7: the exhaustion, walked for all three owner cases

**Read (this repository, read-only):** every `status.md` under `workspace` and `tasks` (`owner:` values
only), `team/saubakirov.md`, `.tfw/templates/journal/event.md`.

```
$ grep -rh '^owner:' --include='status.md' workspace tasks | sort | uniq -c | sort -rn
     10 owner: unassigned
     10 owner: saubakirov
$ grep -h '^type:' team/*.md | sort | uniq -c
      1 type: human
```

| `owner` | Where the work stops | Event kind | Live instance in this corpus? |
|---|---|---|---|
| `type: human` | the work stops; the task returns to that person, who reads the HL and the research behind it | `transition`, `from:` the live value, `to: BLOCKED`, summary naming the exhausted budget as the blocker | ✅ **10 tasks** carry `owner: saubakirov`, the one declared profile, `type: human` |
| `type: agent` | the work stops; that agent applies the same rule upward to reach its own human or a higher agent | the same `transition`; the upward application writes its own event in its own task | ❌ **none.** `team/` declares one profile and it is `type: human`. The schema admits `type: agent` and the slot is deliberately empty until named-agent principals land — so this is the case with **no live instance**, and the canon states the rule rather than demonstrating it |
| `unassigned` | a **hard stop naming that as the blocker** — a budget cannot be exhausted toward nobody | the same `transition`, with `unassigned` named as the blocker instead of the budget | ✅ **10 tasks**, all in the frozen legacy corpus. `tasks/TFW-58__revise_protocol` — the proposal this task carries forward — is one of them |

**No kind was invented.** `event.md`'s vocabulary is closed — `created`, `dispatch`, `handoff`,
`transition`, `ownership_changed`, `amendment_escalated`, `consolidation` (reserved) — and the return uses
`transition`, which `conventions.md` §5 already defines as recording *"lifecycle changed, **blockage and
resumption included**"*. `BLOCKED` is *"waiting on a dependency, resumes when it clears"*; the dependency
is the owner's ruling. `dispatch` was considered and refused by the coordinator: it records a handover, and
the load-bearing fact is that the work **halted**.

**No owner is named in the canon.** Gate re-run by diffing the whole grep against `HEAD`:

```
$ grep -rn 'saubakirov' .tfw/ --include='*.md' --include='*.yaml'   # before vs after
1c1
< .tfw/CHANGELOG.md:1320:- **GitHub Pages Deploy** — live site at `tfw.saubakirov.kz` …
> .tfw/CHANGELOG.md:1398:- **GitHub Pages Deploy** — live site at `tfw.saubakirov.kz` …
```

One line, shifted by 78 lines of new CHANGELOG text. It is the pre-existing deploy URL. **No handle was
introduced.**

## Replay 4 — AC-8: `TLD`'s revision 1 through the new `handoff.md` entry point

**Read (this repository, read-only):**
`workspace/2026/TFW_20260830-194027_TLD/` — `REVIEW__TFW_20260830-194027_TLD.md`,
`REVIEW__…__rev2.md` (existence only), `journal/` listing, `TS__…` listing.

**What happened.** The first REVIEW returned **🔄 REVISE** on one finding, D1 against judge row 9: the
`grep`/`awk` search block in `review.md` used the awk field reference `$0` twice, which is also the Claude
Code slash-command argument placeholder, so the harness substituted it before the workflow text reached
the agent and the review session received a command that could not run. Nine of ten judge rows held. The
REVIEW got a sibling `__rev2.md`; the RF was appended to, not overwritten.

**What the executor would load under the new entry point, in order:**

| Order | What | Present in TLD? |
|---|---|---|
| 1 | Context Loading items 1–7 as before | ✅ |
| 2 | **item 8 — the prior REVIEW** | ✅ it exists, and **nothing in the old `handoff.md` told the executor to read it**: its list ran to nine items and named no REVIEW, while the word `REVISE` appeared in the file only inside prohibitions |
| 3 | **this round's bound**, in that REVIEW's §4 | ⚠️ **not written as such.** The finding is stated at length and the fix is unambiguous, but nothing says *these items and nothing beyond them*. That is what the new Step 6 item 4 now requires |
| 4 | the TS **as it now stands** | ✅ unchanged — and that is the point below |

**What the bound would have said:** *"Rewrite the search block without any `$N` field reference and run it
once from the project root. Nothing else is ordered; nine of ten judge rows hold."* One item, rung 1.

**And the revision count for TLD's phase is zero, not one.** The phase holds exactly **one** TS file and
it was never corrected: the finding was discharged inside the approved TS. Under the old round-counting
reading this was round 1 of a budget of 2; under A12's unit it consumed **no revision at all**. That is
the unit working as designed — a substantive round that corrects work inside the contract does not spend
the budget that exists to detect a bad contract.

**What was not re-done, per the new text:** nine judge rows already verified, twenty-two knowledge
citations already resolved, the seal diff, the 33-copy `cmp` sweep, and the suite run. The review returned
one item and one item was owed. Compare `helpdesk` HD-23, which the HL measures at **15 items returned
against 1 ordered** — the absence of a written bound is what that number is.

---

*Replays — TFW_20260902-112841_RDP | 2026-09-02*
