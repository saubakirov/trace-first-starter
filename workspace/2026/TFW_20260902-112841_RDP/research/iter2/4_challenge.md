# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260902-112841_RDP](../../HL-TFW_20260902-112841_RDP.md)
> Goal: Every finding a review produces becomes a decision by rule — one criterion, one named decider, one termination.

## Consistency Check

**Incompatible pairs.** Each was tested by asking what the pair produces in the corpus, not by argument.

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|---|---|---|---|---|
| **D1** delivery | B `lifecycle: TS_DRAFT` | **D4** classifier | A reviewer, **per item** | The lifecycle is one value **per task**; a rung is a property **per item**. A mixed-rung REVISE — the ordinary case: AFD-48 rev2 had 4 rung-1 and 2 rung-2 items — has no representable state. E1 step 2 |
| **D1** | C artifact addressed to the coordinator | — | any | **DoF 1.** AFD's `PROPOSAL` is a new maintained artifact, and DoD 11 forbids the net count rising |
| **D2** record | D journal event | — | any | The `kind` vocabulary is **closed** by the canon's own words; adding a value is a new entity. G7 |
| **D2** | A verdict / signature line | **D5** checkability | B, C or D | A signature is byte-identical whether it was read or not, so it can carry no consequence, no citation and no bound. **DoF 3** — nothing can fail against it |
| **D1** | D new surface with its own TS | **D3** bound | B or C | A bound refers to *the previous round*. Across a TS boundary there is no previous round, so the bound has no referent. INNO-9: 9 revisions, 0 bounds |
| **D3** | A nothing bounds the round | **D5** | D names what may not reopen | Direct contradiction. `helpdesk` HD-23 is the measurement: **15 items returned against 1 ordered** |
| **D4** | D nobody classifies | **D1** | B, C or D | With no rung there is nothing to route. This is 96.7 % of 331 reviews and it is C1 |

**Surviving configurations:**

| Config | D1 delivery | D2 record | D3 bound | D4 classifier | D5 checkability | Notes |
|---|---|---|---|---|---|---|
| **C5′** | **`pending — coordinator` in the disposition cell** | round-labelled TS section for a routing ruling | coordinator's closing checklist | reviewer at verdict | consequence + clause + what may not reopen | AFD's observed-winning shape **with the new artifact removed**. Zero new entities |
| **C7** | B `lifecycle: TS_DRAFT`, whole-task | B disposition cell | C coordinator's closing checklist | A reviewer | C + D | Survives only if the mixed-rung case is resolved by *rung 2 wins* |
| **C8** | `pending — coordinator` **and** `TS_DRAFT` when the TS actually changes | **split: cell for a disposition, TS section for a routing ruling** | C | A | C + D | The two acts separated. Strongest survivor |
| C1 | A | A | B | D | A | Survives *consistency* and fails the **contract** — DoF 3 and DoF 5. Listed so the baseline is not silently dropped |

**Unexpected survivors:**

- **C5′ — AFD's winning configuration minus its only new entity.** The `PROPOSAL` was doing four jobs:
  addressing a decider, listing named alternatives with costs, recording the ruling, and bounding the next
  round. Three of them are already shipped in this repository — the `pending — {role}` disposition state
  addresses a decider, A5's clause citation records the ruling, and a REVIEW sibling file preserves the
  trace. **Only the named-alternatives-with-costs job has no home**, and deliverable 4 already assigns it:
  *"the reviewer marks and proposes."* So the artifact AFD invented was compensating for a channel this
  repository has and that project did not.
- **C8 — one act at the close of review is two acts.** Nobody proposed it because deliverable 4's wording
  (*"one act at the close of review, not one per item"*) reads as settling the question. It settles the
  *count*, not the *location*. A disposition ruling belongs where a reader meets the item; a routing
  ruling belongs in the artifact it changes.

---

## Findings

### C1: The trace-loss risk is **not real**, and the risk register should say so

HL §9, added by the coordinator ninety minutes ago:

> *"**A3's route loses the review's own trace on re-entry** — the reviewer's finding is in a REVIEW file,
> and `TS_DRAFT` re-entry has no defined door back through `handoff.md`."* Medium / Medium.

Attacked directly and it does not stand. `conventions.md` artifact naming makes every round a **sibling
file** — `REVIEW__x__rev2.md`, `__rev3.md` — and nothing in the lifecycle touches a REVIEW file. Across
11 deep rounds in four corpora, **not one prior REVIEW was overwritten**; the one artifact destruction on
record (HL §2.3) was an **RF**, which is deliverable 8's subject, not this route's.

⚠️ **What the row half-saw is a different defect, and it is real:** the *forward* link. The TS carries no
pointer to the REVIEW that caused the change unless the ruling writes one. AFD wrote one — *«Вход: REVIEW
rev2 = 🔄 REVISE, 4 items»* — and it cost a line. **A missing reference is not a lost trace**, and calling
it one puts a Medium/Medium row against a mechanism whose actual cost is one sentence.

### C2: The scope door is real, its mitigation is prose — and the enforcement site already exists one round later

HL §9's mitigation: *"the coordinator rules only the named item, and the TS stays downstream of a frozen
HL."* Two clauses of unequal quality.

| Clause | Kind | Holds? |
|---|---|---|
| *the TS stays downstream of a frozen HL* | **structural** — §3's contract, D63, TFW-53 | ✅ goals cannot move through this route |
| *the coordinator rules only the named item* | **exhortation** | ❌ Principle 7: *"a rule with no enforcement site is decoration"* |

**But an enforcement site exists and the design has not claimed it.** The next round's reviewer reads the
TS — the Purpose Check is *against the contract baseline* — so an appended round-labelled section is read
by an independent role before the round can close. That is separation of duties, which the external
literature names as the primary anti-rubber-stamp control (G9), and it is already how TFW works.

```text
   coordinator appends  ## 11. [rev5]  to the TS
                │
                ▼
   next round's reviewer reads the TS against the frozen HL
                │
                ├── ruling stayed on the named item      →  round proceeds
                └── ruling reopened more than the item    →  a review finding, this round
```

⚠️ **The residual, and it is exact.** The check runs *one round later*. A scope change made in the
**terminating** round — where the next verdict is ✅ APPROVE or ❌ REJECT and no further review reads the
TS — **is never read by an independent role.** That is a narrow, nameable gap, and it is worth a risk row
rather than a mechanism: the terminating round is the one where the coordinator's act is unchecked.

### C3: The honest case for H3 being **false** — and it is stronger than E3 admitted

The strongest attack on E3's site is not hypothetical. It has already been measured on this very corpus.

**The attack.** `not material — {one-sentence ruling}` is a text cell. The reviewer writes a proposal; the
coordinator can copy it. G9's counter-evidence says exactly what happens next: a mandated written reason
becomes *"a ritualized legal incantation… emptied of recoverable meaning"*, and the courts' test is not
whether a reason exists but whether it *"carries sufficient information to allow the merits to be
evaluated."*

**And the incantation has already been demonstrated here.** Iteration 1's adversarial scoring is the
demonstration: **all nine** TLD disposition rows pass NS1's four words, because *"in a project whose
product is documentation, every defect is an inspectability defect."* Nine rulings, one sentence, no
discrimination. That is not a risk — it is a completed experiment on the real artifact.

| Outcome | Stampable? | Why |
|---|---|---|
| `paid — phase-x` | **No** | a phase directory exists or it does not |
| `promoted — TASK-ID` | **No** | a task directory and its `status.md`, created now |
| `not material — {ruling}` | **Yes** | text, and **8 of 9 real rulings landed here** |

**The rebuttal, and its limit.** A4 already separated the axis from the test: the ruling must name a
**consequence**, and a consequence is item-specific by construction — *"renaming would break every
existing citation"* cannot be pasted onto an unrelated row, while *"purpose is damaged"* can be pasted
onto all nine. A5 hardens it further: on the *owed and forbidden* branch the ruling must **cite the
clause**, and a citation is checkable by opening the clause. So the two amendments the owner approved this
morning are precisely the anti-boilerplate controls, and they were not argued for on that ground.

**What still does not hold.** Nothing *fails* when a consequence is generic. DoF 3 is the sanction and it
fires at review of **this task**, once — it is not a standing check on every future ruling. So:

> **H3 is confirmed, conditionally, and the condition should be stated rather than hidden.** A site exists
> in already-written text; two of its three outcomes cannot be stamped; the third is hardened by A4 and A5
> and remains the residual. The owner is **not** forced to choose between DoF 1 and the authority move —
> which is the outcome the coordinator's entry said would require a ruling.

⚠️ **And the one part the reviewer cannot pre-fill is the part worth requiring.** A ruling repeats what the
reviewer proposed; a **bound** — *what the next round may not reopen* — is a statement about the round, and
only the ruling role can make it. AFD's §11.6 is the observed form: five items, a `⛔ Не делать` list, and
*«Ревьюеру — три факта, чтобы не было третьего круга»*. The next REVIEW opened by verifying against those
five points and approved. **A bound is falsifiable at the next round by construction** — if the next
REVIEW reopens what the bound excluded, either the bound was wrong or it was ignored, and both are visible
in the artifact.

### C4: A2's trigger — attacked on four failure modes, and it survives on the corpus (thread 5, delivered)

Thread 5 was dropped as low value and folded into thread 4. It is answerable now at no cost, because the
population is open on the desk.

Four ways *"a round that returns an item the previous round already ordered"* could misfire:

| Mode | The claim | Tested against |
|---|---|---|
| **(a)** the intended signal | the channel cannot discharge the item — §2.9 | AFD-48 `phase-a` |
| **(b)** false positive | the item returns because the **executor was given an impossible instruction**, and the terminating verdict then punishes the wrong party | AFD-48 `phase-b`/S3 |
| **(c)** false negative | the fixes **created new defects**, which are not returning items, so nothing fires while the loop still runs | INNO-13 `phase-b-rev5` |
| **(d)** false positive | a **standing condition** ( *"keep source-level `@OptIn` coverage"* ) is restated each round and reads as a returning item | AFD-48 `phase-a` rev2 item 1 |

| Case | Trigger | Correct? |
|---|---|---|
| AFD-48 `phase-a` — *"Obtain coordinator amendments"* in rev2, rev3, rev4 | **fires at rev3** | ✅ and **one round earlier than the round cap**, which fires at rev3 only after rev3 exists |
| TFW-60 `phase-a` rev3 — every rev2 item closed, new findings only | **abstains** | ✅ this is the case iteration 1 said a round cap would have destroyed |
| INNO-13 `phase-b-rev5` — 6 of 8 closed, *«правки породили четыре новых дефекта»* | **abstains** | ✅ mode (c) confirmed as a real gap, and the honest answer is that four new defects are **not** a drift signal — they are a new round of work |
| AFD-48 `phase-b`/S3 rev2 — item 1 is rev1's own **added AC** returning | **fires at rev2** | ✅ **and the response the corpus actually chose was the right one**: the coordinator descoped the AC he had added. Mode (b) inverted — the impossible instruction was the coordinator's, and firing exposed it |

**2 of 2 correct firings, 2 of 2 correct abstentions, on every case in the population where the trigger is
testable.** Mode (d) is a wording question, not a defect: a standing condition is a constraint, not an
ordered item, and the distinction belongs in the TS's own wording rather than in an amendment against a
ruling made this morning.

⚠️ **Mode (c) is the honest residual and it is A2's real limit.** A loop whose every round produces *new*
defects never trips the trigger. INNO-13 is that loop. Nothing in this task's scope closes it, and the
correct response is to say so in §9 rather than to legislate a second trigger — DoF 1, and NS2 principle 6.

### C5: The escape hatch — **the strongest objection in this iteration, and it lands on a frozen deliverable**

The attack, in one line: **any termination rule anchored to *"the previous round"* is defeated by renaming
the surface, and DoF 1 forbids the only instrument that would count across a rename.**

```text
  HL §10, "Why not count rounds in a control file?"
      "It is a new maintained artifact, which DoF 1 forbids. The round is already visible in the
       artifact names — rev2, rev3 — and that is the structural home."
                                       │
                                       ▼
   INNO-9 phase-a:   REVIEW__phase-a__…   →   REVIEW__phase-a-rev1-7__…   →   REVIEW__phase-a-rev8__…
                     9 revisions · 8 TS files · 3 reviews · 0 terminations
                                       │
                                       ▼
   The "structural home" is a FILENAME, and a filename is chosen by whoever writes the file.
```

And it is not a defiant act. **Deliverable 5 instructs it**: *"Work that cannot be accepted under the
existing TS is new work and takes a new TS."* A rung-2 item is by definition work the existing TS cannot
accept. So deliverable 5 says *new TS* and deliverable 3's rung 2 says *the coordinator changes this TS and
the round continues*. **Two frozen clauses, the same situation, opposite instructions** — and A3 created
the collision by giving rung 2 a destination, four minutes before this iteration opened.

**External confirmation that this is a known, solved class.** Service-desk platforms hit exactly this: a
ticket closed and reopened restarts the clock, and *"re-opens can destroy 'solve in X days' metrics"*
([Atlassian community](https://community.atlassian.com/forums/App-Central-articles/The-Hidden-Cost-of-Reopened-Tickets-and-How-to-Prevent-Them/ba-p/3152740)).
The fix the tools converged on is **not** a counter and **not** a prohibition on reopening — it is to make
the reset conditional on **who reopened it and why**: fully restart if the requester reopened it, merely
**resume** if it was reopened internally
([Zendesk](https://support.zendesk.com/hc/en-us/articles/4408825745690-Can-I-pause-the-SLA-timer-or-reset-it-under-certain-conditions),
[Atlassian](https://community.atlassian.com/forums/App-Central-articles/Take-control-of-your-SLAs-Reset-breaches-and-track-time-directly/ba-p/3072804)).

Mapped onto this contract, with no new entity:

| A new TS is opened because… | The round count should |
|---|---|
| a rung-2 item needed the specification changed — the coordinator's own act | **resume.** It is the same work, still under review |
| the task's declared outcome genuinely grew | **restart.** It is new work, and deliverable 5 is right about it |

The discriminator is **who opened it and for what**, and both are already recorded: rung 2 names the
coordinator, and `amendment_escalated` / §12 names the owner. Nothing needs counting.

**Two repairs, and they are not equivalent.**

| Repair | Where | Cost | Closes the hatch? |
|---|---|---|---|
| Anchor the trigger to **any previous round on this task**, not *the previous round* | §5 DoD 7 · §4 deliverable 6 — **frozen**, and set by A2 this morning | the reviewer reads prior REVIEWs of the task, not only the last. Max in the population: 4 | Partly — survives a phase rename, still defeated by a **new task** |
| State that a **rung-2 TS change does not restart the count** — the round continues under the amended TS | §4 deliverable 5 — **frozen** | one clause; removes the collision with deliverable 3 | **Yes**, and it also removes the contradiction rather than guarding it |

The second is Principle 6 — *name the term and delete the paragraph* — and it is cheaper. Both are
frozen-section changes and neither is the researcher's to apply.

⚠️ **The honest counter to my own repair.** *"Any previous round on this task"* over-fires by design: an
item ordered twice because the first fix was wrong **and** the second attempt was also wrong now
terminates the loop. That is not a bug — it is S3 verbatim: *«не более 1-2 циклов, иначе признак дрифта»*.
Over-firing in that direction is the owner's stated intent.

---

## Checkpoint

| Found | Remaining |
|-------|-----------|
| **The trace-loss risk row does not stand.** 11 deep rounds, 4 corpora, no prior REVIEW overwritten. What is missing is a forward reference, worth one line | — |
| **The scope door's enforcement site already exists** — the next round's reviewer reads the TS against the frozen HL. Residual: a scope change made in the **terminating** round is read by nobody | Worth a risk row, not a mechanism |
| **H3 confirmed conditionally.** Two of three dispositions are unstampable because TLD made them name an artifact; the third is hardened by A4 and A5; the residual is that nothing fails when a consequence is generic. **The owner is not forced to choose between DoF 1 and the authority move** | The residual is named, not closed |
| **A2's trigger validated on the whole population**: 2 of 2 correct firings, 2 of 2 correct abstentions — and on AFD-48 `phase-b` it fires **one round earlier** than a round cap would. Residual: a loop producing only *new* defects never trips it | Mode (c) is out of this task's scope and belongs in §9 |
| ⚠️ **Deliverables 3 and 5 give opposite instructions for the same situation**, and the corpus already takes the exit — INNO-9 nine times, on the canon's own wording. The termination rule's *"structural home"* is a filename | Two repairs proposed; both target frozen text; the owner rules |

**Sufficiency:**
- [x] External source used? — the SLA-reset literature supplies the *resume vs restart* discriminator for C5; the boilerplate literature supplies C3's attack
- [x] Briefing gap closed? — all four planned attacks executed; one (the trace loss) **refuted the premise it was given**
- [x] Pairwise incompatibility checked? Surviving configurations listed? — 7 incompatible pairs, 4 survivors, 2 of them combinations nobody proposed
- [x] Hypothesis tested? — H3 confirmed with its residual named; A2 and A3 both attacked with real cases
- [x] Counter-evidence sought? — C3 was built to break E3 and it partly did; C5 was built to break a deliverable the owner froze and it did; C1 was built to support a coordinator's risk row and refuted it

**Metacognitive check.** New, and the discomfort is the useful part. Three of the five findings here argue
against text that was written today: C1 refutes a risk row the coordinator added, C5 finds a contradiction
A3 created, and C3 shows that the two amendments the owner approved this morning are the anti-boilerplate
controls — which is a defence of them on a ground nobody claimed. The iteration did not confirm what it
set out to confirm; it found that the applied fix is right about the decider and wrong about the
mechanism, and that the termination rule has a free exit the canon recommends.

Stage complete: YES
→ Gate written, not taken — owner instruction *«без вопросов ко мне»*, 2026-09-02
