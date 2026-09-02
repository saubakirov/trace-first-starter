# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260902-112841_RDP](../../HL-TFW_20260902-112841_RDP.md)
> Goal: Every finding a review produces becomes a decision by rule — one criterion, one named decider, one termination.

## Configuration Space

Five dimensions × four alternatives is 1 024 cells, so the space is built the way the template's rule
requires — from the configurations that are **real or contractually forced**, with the forbidden columns
marked. Every row below is either observed in a corpus, specified by the frozen HL, or the difference
between two such rows.

| Config | D1 delivery | D2 record of the act | D3 bound on the return round | D4 who classifies the rung | D5 what makes it checkable | Status |
|---|---|---|---|---|---|---|
| **C1** today | A items-to-fix list | A verdict line | B reviewer's item list | D nobody | A that it exists | the status quo, 96.7 % of 331 reviews |
| **C2** AFD-48 `phase-a` | A items-to-fix list | — none | B reviewer's item list | A reviewer at verdict | A | **observed failing**: rev2·rev3·rev4, item unchanged |
| **C3** `helpdesk` HD-23 | A | — none | **A nothing** | D nobody | A | **observed failing**: 15 items returned against 1 ordered |
| **C4** INNO-9 `phase-a` | **D new surface + own TS** | C the new TS itself | D TS diff | C coordinator at close | A | **observed**: 9 revisions, 0 terminations, canon-endorsed |
| **C5** AFD-48 `phase-b`/S3 | **C artifact to the coordinator** | **C round-labelled TS section** | **C coordinator's closing checklist** | **B executor on receipt** | B + D consequence + what may not reopen | **observed succeeding**: rev3 ✅ |
| **C6** the HL as frozen | **B `lifecycle: TS_DRAFT`** | B disposition cell citing the clause | B reviewer's item list | A reviewer at verdict | C cites the clause | **specified**, untested — thread 2's subject |
| **C7** C6 + C5's bound | B `TS_DRAFT` | B cell | **C coordinator's closing checklist** | A reviewer | C + D | ⭐ **the combination nobody proposed** |
| **C8** C7, D2 split by rung | B `TS_DRAFT` | **B for a disposition · C for a routing ruling** | C | A | C + D | ⭐ **second combination nobody proposed** |
| **C9** | C artifact to the coordinator | any | any | any | any | ⛔ **DoF 1** — AFD's `PROPOSAL` is a new maintained artifact |
| **C10** | any | **D journal event** | any | any | any | ⛔ **DoF 1** — the `kind` vocabulary is closed (G7) |
| **C11** | A | any | any | **A reviewer at verdict** | any | ⛔ **DoF 5 / §2.7** — reviewer rules; this is the defect under repair |

**What the space makes visible that the Briefing did not.**

1. **C7 — the bound is per-round content, not workflow prose.** Deliverable 7 puts *"what the round is
   bounded by"* into `handoff.md`. But `handoff.md` is one file for every round of every task; it can name
   **where the bound lives**, never **what it says**. The only observed bound that worked was written per
   round, by the ruling role, naming five items and a `⛔ Не делать` list — and addressed to the reviewer
   as well as the executor. A bound stated in `handoff.md` as guidance is Principle 7's decoration; a
   bound stated in the round's own ruling is structural.
2. **C8 — D2 is not one act, it is two.** A *disposition* ruling (this item is not owed, or is owed and
   forbidden) belongs in the REVIEW cell beside the item, where a reader meets it. A *routing* ruling
   (this item needs the TS changed, and here is the change) belongs in the TS, because that is the
   artifact it changes. The HL treats deliverable 4's *"one act at the close of review"* as covering both.
   C5 shows a corpus that separated them without being told to.
3. **C4 is legal.** The configuration with nine revisions and no termination is not a violation of
   anything in the frozen contract. It is what deliverable 5 instructs when read literally.

---

## Findings

### E1: The paper replay — AFD-48 `phase-a` rev2 through the applied A3 route

This is thread 2, the coordinator's first priority. The input is real: REVIEW rev2, 🔄 REVISE, six items,
of which **two are rung 2** (item 3 *"Obtain coordinator amendments"*, item 5 *"no executor-authored
contract decisions"*) and four are rung 1. Each question the coordinator's entry asked, answered by
reading the canon as it now stands.

#### Step 1 — the reviewer marks and the verdict is written. ✅ works

Step 4 writes one verdict; A5 gives each debt row a disposition; deliverable 3 gives each ordered item a
rung. All three fit in text that exists.

#### Step 2 — the rung-2 item is routed. ❌ **the first real defect: one lifecycle field, two rungs**

```text
   REVIEW rev2  ──  6 items
                    ├── items 1, 2, 4, 6   rung 1  →  execution
                    └── items 3, 5         rung 2  →  lifecycle: TS_DRAFT
                                    │
                                    ▼
              status.md carries ONE `lifecycle` value.
              Set it to TS_DRAFT → the four rung-1 items have no state to be worked in.
              Set it to execution → the two rung-2 items are stranded exactly as in C2.
```

`conventions.md` §5 is a single-valued state machine and `status.md`'s `lifecycle` is one closed field.
**A mixed-rung REVISE — which is the ordinary case, not a corner case — has no representable state.**
A3's route is stated per *item*; the mechanism it lands on is per *task*. The one arm of the corpus where
rung 2 was discharged (C5) did not move any lifecycle: AFD has no `status.md` at all.

Two escapes exist and both are honest:
- **rung 2 wins**: the task goes to `TS_DRAFT`, and the rung-1 items travel with the coordinator's ruling
  into the return round — which is what AFD's §11.6 checklist actually did (five items, mixed rungs, one
  document).
- **the ladder describes the item's decider, not the task's state**: `TS_DRAFT` names *who must act
  before the round can proceed*, and the lifecycle moves once, back to execution, when they have.

The first is C5, observed. The second is a re-reading of deliverable 3, not a new entity. Neither is in
the HL, and the choice belongs to the coordinator.

#### Step 3 — the coordinator receives it. ❌ **a state is not a delivery**

`lifecycle: TS_DRAFT` is a value in a file in the task directory. Nothing dispatches it, and `plan.md` has
no entry point for *"re-entering `TS_DRAFT` from a REVIEW"*. The journal's `dispatch` kind — *"work was
handed to a named participant"* — exists and would carry it, and this task may not add a step to
`plan.md` (**DoF 8**: `plan.md` is not among the files §4 names).

⚠️ **So the applied A3 delivers the item to a state, and §2.9's finding was that the previous mechanism
delivered it to a list. Both are places rather than people.** What made C5 work was that the artifact
carried an addressee — *«Адресовано: Coordinator»* — and the external evidence says the same thing from
outside: a board with no impact assessment addressed to it *has no basis for refusal* (G9).

#### Step 4 — what may the coordinator change? ⚠️ **prose, with one structural answer available**

HL §9's mitigation is *"the coordinator rules only the named item, and the TS stays downstream of a frozen
HL."* The second clause is structural — a frozen HL genuinely bounds the TS. The first is an exhortation,
and Principle 7 says an exhortation is decoration.

C5 supplies the structural form for free: **the ruling is an appended, round-labelled section, and no
earlier TS text is edited.** Then *"changed more than the named item"* is not a matter of trust — it is
visible as the section's own content, next to the section the previous round wrote. `## 9. [rev3]`,
`## 10. [rev4]`, `## 11. [rev5]` is an audit trail that costs one heading convention.

#### Step 5 — what does the executor read on return? ❌ **confirmed gap, and it is worse than the HL states**

`handoff.md` Context Loading, all nine items, verbatim: `AGENTS.md` · `conventions.md` · `glossary.md` ·
`KNOWLEDGE.md` · Master HL · Phase HL · **TS** · related HL/TS/RF files · relevant code.

```bash
grep -niE 'revise|re-entry|returning|previous review' .tfw/workflows/handoff.md
# → only role-lock prohibitions: "writing REVIEW", "Executor writes REVIEW file"
```

**The REVIEW file is not in the list a returning executor loads, and the word `REVISE` appears in
`handoff.md` only inside prohibitions.** An executor re-entering after a REVISE reads the TS and the code
and reaches the items only by knowing to look. `helpdesk` HD-23 is what that produces: **15 items
delivered against 1 ordered**, nobody reviewed the other 14. Deliverable 7 is therefore not a convenience
— it is the only thing that makes a return round bounded, and C3 is the measurement of its absence.

#### Step 6 — does the review's own trace survive? ✅ **yes, and the risk row overstates it**

REVIEW files are siblings (`__rev2`, `__rev3`) and are never overwritten; `conventions.md`'s artifact
naming already guarantees it. HL §9's row *"A3's route loses the review's own trace on re-entry"* is
**not confirmed**: the trace survives. What does not survive is the **forward link** — the TS carries no
pointer to the REVIEW that caused the change unless the ruling writes one. C5 wrote one:
*«Вход: REVIEW rev2 = 🔄 REVISE, 4 items»*. So the link is content, and content is cheap; it is one line
of the section heading convention, not a mechanism.

#### Replay verdict

| Question from the coordinator's entry | Answer |
|---|---|
| What does the coordinator receive, and from where? | **A state, from a file nobody is directed to read.** Defect — E1 step 3 |
| What may they change — only the named item, or has the TS reopened? | **Nothing structural bounds it**, but an append-only round-labelled section makes an overreach visible at no cost. E1 step 4 |
| What does the executor read on return, and does `handoff.md` cover arriving from `TS_DRAFT`? | **No, and it does not cover arriving from a REVISE either.** The REVIEW is absent from the load list. E1 step 5 |
| Does the review's own trace survive the round trip? | **Yes.** The §9 risk row is not confirmed; the missing piece is a forward reference, not the trace. E1 step 6 |
| *(unasked, and it outranks the four)* Can a mixed-rung REVISE be represented at all? | **No.** One `lifecycle`, two rungs. E1 step 2 |

**A3's route survives contact — but not as written.** It is sound where it says *the coordinator is the
decider for a rung-2 item*, and it is unimplementable where it says *the delivery mechanism is a lifecycle
value*, because the state is per task and the rung is per item.

### E2: Thread 4 — the population is closed, and H2 is refuted **more strongly**, not less

All 11 deep rounds, classified on iteration 1's three labels. The five new rows are marked ⭐.

| # | Corpus | Surface | Round | Verdict | What that round ordered |
|---|---|---|---|---|---|
| 1 | this repo | TFW-60 `phase-a` | rev3 | 🔄 | **work** — fail-closed participant validation, a hang |
| 2 | this repo | TFW-60 `phase-a` | rev4 | ✅ | — terminating |
| 3 | this repo | TFW-60 `phase-aa` | rev3 | 🔄→✅ | **record** — *"all record-keeping and none in the engineering"*; owner overrode |
| 4 | this repo | `ASSISTED15` | rev3 | 🔄 | **work** — a non-terminating Windows lock path |
| 5 | AFD-48 | `phase-a` | rev3 | 🔄 | **work** + an undelivered rung-2 escalation |
| 6 | AFD-48 | `phase-a` | rev4 | 🔄 | **work** + the same rung-2 escalation, still open |
| 7 ⭐ | AFD-48 | `phase-b-s3-block1` | rev3 | ✅ | — terminating. **What ended it was a spec change made between rounds** (below) |
| 8 ⭐ | AFD-27 | `phase-c1-block1` | rev3 | ✅ | — terminating; it accepted **work** — a naming gate built from an invariant, 4 red-drills |
| 9 ⭐ | INNO-13 | `phase-b-rev5` | rev3 | 🔄 | **work** — 6 of 8 blockers closed, *«правки породили четыре новых дефекта»* |
| 10 ⭐ | INNO-13 | `phase-b-rev5-rev1` | rev3+ | ✅ | — terminating |
| 11 ⭐ | INNO-9 | `phase-a-rev8` | rev3 | ✅ | — terminating; it accepted a **bounded language sweep** ordered by `rev1-7` |

| | iteration 1 | now |
|---|---|---|
| Population | 7 | **11** |
| Substantive (ordering) rounds past two | 5 | **6** |
| …of which corrected **work** | 4 | **5** |
| …**wording** | 0 | **0** |
| …**record** | 1 | 1 |
| …**specification** | 0 | **0** |
| Terminating verdicts | 2 | 5 |

**H2 is refuted at 5 of 6, and A2 needs no re-proposal.** A2 was approved on 4 of 5; the completed
population moves the ratio the same direction. Guiding question 3 is answered **no** — there is nothing to
file against a ruled amendment.

⚠️ **And row 7 is the finding inside the finding.** No deep round in 11 corrected a specification. But
`phase-b-s3-block1` still needed a specification corrected, and it got one — **between rounds, in the TS,
by the coordinator**, not by a review round:

> *«Item 1 rev2 (lane-based totality) **СНЯТ с Блока 1 решением координатора** и перенесён в S4a…
> Это **объявленное сужение AC**, а не невыполненное требование — ⛔ не считать его открытым.»*

So the thing a round cap was reaching for — *a deep loop means the spec is wrong* — **is true of this
case and invisible to every round-counting instrument**, because the correction did not happen in a round.
It happened in the channel §2.9 says does not exist. A2's unchanged-item trigger would have fired here at
rev2 (item 1 was rev1's added AC, returning); the round count would have fired at rev3, after the fix.
**A2 is better than the count for the reason the corpus now shows, not the reason it was proposed on.**

### E3: H3 — three candidate sites survive G7, and one of them is already shipped

Candidates, scored on the test G9's counter-evidence forces: **not "was a reason written" but "does the
record carry enough information to be evaluated, and is there something that fails if it does not".**

| Site | Exists today? | New entity? | Can a reader who was not there tell a real act from a formality? | Verdict |
|---|---|---|---|---|
| A journal event kind | no | **yes** — closed vocabulary (G7) | — | ⛔ eliminated by DoF 1 |
| A verdict / signature line | yes | no | **No.** A signature is identical whether it was read or not | ⛔ eliminated by DoF 3 |
| `status.md` `lifecycle` | yes | no | Partly — one value per task, not per item; and E1 step 2 shows it cannot even hold a mixed-rung round | ⚠️ insufficient alone |
| **The disposition cell + its `pending — {role}` state** | **yes, shipped by TLD** | **no** | **Yes** — see below | ✅ **H3's site** |
| **A round-labelled append-only section in the TS** | yes as a convention, unnamed in the canon | no — it is a heading | **Yes** — the previous round's text sits beside it | ✅ for a *routing* ruling |

**The disposition cell already does three-quarters of the work, and nobody noticed.**
`templates/REVIEW.md` §5, shipped 2026-08-30:

> *"Every row carries a disposition, and **a disposition names something that already exists**:
> `paid — phase-{x}` · `promoted — {TASK-ID}` · `not material — {one-sentence ruling}`. **A row awaiting
> an owner ruling is `pending — owner`** and keeps the task open until it becomes one of the three."*

| Outcome | What the coordinator must produce | Can it be stamped? |
|---|---|---|
| `paid — phase-x` | **a phase that exists** | **No** — a directory either exists or does not |
| `promoted — TASK-ID` | **a task directory and its `status.md`, created now** | **No** — same |
| `not material — {ruling}` | text | **Yes, today.** This is where 8 of 9 real rulings landed |

**Two of the three outcomes are already unfakeable, because TLD made them name an artifact.** The stamp
risk lives entirely in the third — and A5 is already the amendment that hardens it: the ruling must say
*not owed* or *owed and forbidden, citing the clause*. A clause citation is checkable by opening the
clause. That is the same discipline `KNOWLEDGE.md` D64 records for the Purpose Check — *"alignment must be
cited"* — extended one level down.

**And the `pending — {role}` state is the delivery mechanism the ladder needs, at zero cost.** It already
exists for `owner`. `pending — coordinator` uses the same slot; the row stays visible beside the item, the
task cannot reach `DONE` while it stands, and the transformation from `pending — coordinator` to
`not material — owed, forbidden by DoD 10` is **visible in one cell, in the artifact a reader opens
anyway**. No lifecycle move, no dispatch, no new file, no new column.

⚠️ **What the cell cannot do, and C5 supplies.** A disposition cell records a ruling about an item. It
cannot record *what the next round may not reopen* — and that is the one thing the reviewer cannot
pre-fill, so it is the one thing that proves the coordinator read the round rather than initialled it.
AFD's §11.6 wrote it as three facts addressed to the reviewer, and the next REVIEW opened with *«Rev3
проверена по пяти конкретным пунктам координатора»* and approved.

**H3's answer, stated as the hypothesis asked it:** the mechanism exists in text already written — the
disposition column, its `pending — {role}` state, and A5's clause citation — and it needs **one addition
that is also not a new entity**: the ruling names what the return round may not reopen. That sentence is
deliverable 7's *"what the round is bounded by"*, relocated from `handoff.md`, where it can only be
generic, to the ruling, where it is specific. H3 is **confirmed**, and the owner is not forced to choose
between DoF 1 and the authority move.

### E4: The escape hatch — deliverables 5 and 6 cancel each other, and the corpus already walks through the gap

The interaction, in the contract's own words:

```text
  Deliverable 5   "A revision is repair of what was already specified.
                   Work that cannot be accepted under the existing TS is NEW WORK and takes a NEW TS."

  Deliverable 6   "A round that returns an item the previous round already ordered
                   is the terminating round."
                                     │
                                     ▼
        For any item the executor cannot fix under the current TS — which is the definition of
        a rung-2 item — deliverable 5 says: new TS.  A new TS starts round 1.
                                     │
                                     ▼
        INNO-9 phase-a:  rev1 … rev9, eight TS files, three REVIEW files, zero terminations.
        AFD-48:          phase-b-s3-block1 … block2, S3 … S4a — the same shape with better names.
```

| Instrument | Fires across a TS boundary? |
|---|---|
| Round count in the artifact name (HL §10's *"structural home"*) | **No** — `phase-a-rev8` renames the surface and the counter restarts |
| A2's unchanged-item trigger | **No** — there is no *previous round* on this specification |
| A control file counting rounds | rejected by DoF 1, and would not help: it counts what it is told |

**This is DoF 4 as written**: *"a third round remains reachable by anyone willing to write one"* — and it
turns out the price is not even a defiant act. It is a filename. Two of four corpora already pay it, and
one of them (INNO-9) is doing exactly what deliverable 5 instructs.

⚠️ **The distinction the contract is missing is not a rule, it is a term.** Deliverable 5 defines a
revision by **what the TS can accept**. But whether the TS can accept the fix is the *rung*, which
deliverable 3 already answers, and rung 2's whole point is that **the TS gets changed and the work
continues** — not that the work becomes a new task. So deliverable 5's second sentence and deliverable 3's
second rung describe the same situation and prescribe opposite things: *take a new TS* versus *the
coordinator changes this TS and the round continues*. C5 chose the second and terminated in three rounds;
C4 chose the first and ran nine.

This is a contradiction inside the **frozen** §4, discovered by measurement, and it is not one iteration 1
could have found — A3 created it, four minutes before this iteration started, by giving rung 2 a
destination that deliverable 5 sends elsewhere.

---

## Checkpoint

| Found | Remaining |
|-------|-----------|
| **A3's route breaks on a mixed-rung REVISE**: one `lifecycle` field, two rungs, and the ordinary case is mixed. Two honest repairs exist, both without new entities | Which repair the coordinator prefers — a design choice, not a research one |
| **`handoff.md` does not load the REVIEW file at all**, and the word REVISE appears in it only inside prohibitions. Deliverable 7's gap is confirmed by reading the nine-item load list | — |
| The review's own trace **does** survive `TS_DRAFT` re-entry; HL §9's row overstates the risk. What is missing is a forward reference from the TS, which is content | — |
| **H3 confirmed.** The site is the disposition cell plus its `pending — {role}` state: two of three outcomes already name an artifact and cannot be stamped; A5 hardens the third; and the round's bound is the part the reviewer cannot pre-fill | Whether requiring the bound turns into boilerplate — Challenge |
| **H2 refuted at 5 of 6** on the closed 11-file population. No specification was corrected by any deep round — the one specification correction that mattered happened **in the TS, between rounds** | — |
| ⚠️ **Deliverables 5 and 6 cancel**: *new work takes a new TS* restarts the round count, and two corpora already do it — INNO-9 nine times, on the canon's own instruction | The strongest form of the objection, and whether any wording closes it — Challenge |

**Sufficiency:**
- [x] External source used? — the AFD and INNO corpora for E1, E2 and E4; G9's external diagnosis supplies E3's scoring test
- [x] Briefing gap closed? — all three assigned threads answered; thread 2's answer is *"sound in principle, unimplementable as written"*
- [x] Configuration Space built from Gather dimensions? — yes, and it produced two combinations nobody proposed (C7, C8)
- [x] Hypothesis tested? — H3 confirmed with its site named; H2's population closed
- [x] Counter-evidence sought? — E1 was run to break A3 and it broke it in one place; E3's scoring test was taken from the search that argued *against* mandated rationale

**Metacognitive check.** New, and one item is uncomfortable: **E4 is a finding against a change this
researcher proposed and the coordinator applied ninety minutes ago.** A3 gave rung 2 a destination;
deliverable 5 already sent the same case somewhere else. Iteration 1 could not have caught it because A3
did not exist yet, and I would not have looked for it if `innoforce-ai-first` had not turned up three
files iteration 1's own grep could not see.

Stage complete: YES
→ Gate written, not taken — owner instruction *«без вопросов ко мне»*, 2026-09-02
