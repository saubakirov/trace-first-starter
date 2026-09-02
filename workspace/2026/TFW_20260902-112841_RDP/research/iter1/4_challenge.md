# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260902-112841_RDP](../../HL-TFW_20260902-112841_RDP.md)
> Goal: Every finding a review produces becomes a decision by rule — one criterion, one named decider, one termination.

## Consistency Check

**Incompatible pairs**, each with the evidence that kills it:

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|---|---|---|---|---|
| D1 Termination | **A — round cap alone** | D2 Decider | **B — ladder in prose** | E2/E3: the cap fires at round 3, but 4 of 5 deep rounds were correcting real work and the depth was caused by an **undelivered** rung-2 escalation. The pair terminates a loop that is working while leaving its cause untouched. AFD-48 `phase-a` is the executed counterexample |
| D1 Termination | **B — unchanged-item detector** | D2 Decider | **B — ladder in prose** | A detector must read whether an item was *routed*. Prose records a recommendation, not a routing act. Nothing to detect |
| D2 Decider | **D — always coordinator** | — | — | **DoF 6**, explicitly: *"taxes the majority case to fix the minority one."* Eliminated by the frozen contract, not by this research |
| D2 Decider | **A — always executor** | — | — | Eliminated by Deliverable 3, frozen. Also the status quo that produced G5 |
| D3 Vocabulary | **A — three outcomes** | D4 Criterion site | **C / D — a criterion mark beside the disposition** | **E1**: on 3 of 9 real rows the criterion answers *material* and the correct disposition is still *not material*. Putting both in one table makes the record self-contradicting on a third of its rows. Either the vocabulary gains a cell or the criterion stays unrecorded — it cannot be both |
| D5 Budget | **A — per section** | — | — | **E4**: Step 4 is 109 words and must carry four of six mechanisms; the tightest honest draft is 199 (+83 %). Incompatible with every configuration, including C1 |
| D4 Criterion site | **A — Step 4 only** | D2 Decider | **C — ladder with a delivery site** | A delivery site is by definition a state or an event outside the prose of one step |
| D1 Termination | **D — nothing** | — | — | DoD 7, frozen. The null row is retained only as the measured baseline |

**Surviving configurations:**

| Config | D1 Termination | D2 Decider | D3 Vocabulary | D4 Site | D5 Budget | Notes |
|---|---|---|---|---|---|---|
| **C6** | C — escalation-completion | C — ladder + delivery site | B — three + *not actionable* | C — column in `templates/REVIEW.md` | B — per group | survives; no cap at all, which the frozen DoD 7 requires |
| **C7** | **A+B — cap, triggered by the unchanged-item detector** | C — ladder + delivery site | B — three + *not actionable* | D — all three sites | B — per group | **survives, and was not proposed** |

**C1 — the HL as frozen — does not survive**, on two independent grounds: D5-A is unreachable (E4) and
the D1-A × D2-B pair is refuted by its own corpus (E2, G5). Both are recorded as amendment proposals in
the RES; neither is applied here.

**Unexpected survivors:**

- **C7**, and its whole apparatus already exists in the canon. Developed in C3 below. It is unexpected
  because the HL treats the ladder as something to *write* and the cap as something to *legislate*; C7
  is assembled from four mechanisms already shipped, and the change is one missing edge.

---

## Findings

### C1 — The strongest case that the criterion decides nothing (mandated by HL §10)

The HL asks for the strongest argument that *purpose, inspectability, authority, continuation* can be
argued for any finding. **The argument succeeds**, and here it is executed against the same nine rows
E1 scored, this time adversarially — arguing YES on every one:

| # | E1 scored | Adversarial YES |
|---|---|---|
| 2 | arguable | **authority** — a rule four of ten files breach, which nothing enforces, teaches a reader that `conventions.md` is advisory |
| 4 | NO | **inspectability** — a reader cannot tell which documents are project-level when the naming rule that says so is contradicted twice |
| 6 | NO | **continuation** — a maintainer who unfreezes one copy and not the other continues from a false statement |
| 8 | NO | **inspectability** — a trace that contradicts its own enumeration is by definition not inspectable |
| 9 | NO | **inspectability** — two artifacts state different facts about the same measurement |

**All nine can be scored YES.** In a project whose deliverable *is* documentation, every defect is
literally an inspectability defect, because the artifact and the inspection surface are the same object.
`NS1`'s four words cannot discriminate here. **DoF 3 fires against Deliverable 1 taken alone.**

**What actually did the discriminating in E1, re-read.** In all five agreements, the ruling turned on a
**named consequence or its named absence**, never on which of the four words applied:

| # | The sentence that carried the ruling | Shape |
|---|---|---|
| 4 | *"renaming either would break every existing citation"* | a named consequence of acting |
| 6 | *"Neither is edited again, so there is nothing to drift"* | a named absence of consequence |
| 8 | *"Both are understatements… this row **is** the correction"* | the harm was discharged by recording it |
| 9 | *"The shipped figure is the defensible one"* | a named absence of consequence |
| 1 | *"860 of 990 pages"* | a counted consequence |

> **Deliverable 2 is doing the work Deliverable 1 is credited with.** Drop the four words and keep
> *"name what will not happen"* and the discrimination survives intact. Keep the four words and drop the
> prediction requirement and the criterion admits everything — which is exactly DoF 3, and exactly what
> §2.4 already measured happening eight times.

This does **not** argue for removing the `NS1` citation. It argues that the citation is doing a different
job — it names the **axis** on which the prediction must be made, and it makes the ruling refusable by
someone who was not there. Principle 1 is safe. What is unsafe is the belief that the four words are the
test. They are the vocabulary; the prediction is the test.

### C2 — The strongest case that the cap destroys real fixes, and it is not hypothetical

Argued from E2's classification, at full strength:

> Of five substantive rounds past two in two corpora, **four corrected work**. In two of them the reviewer
> wrote into the round-3 verdict that the specification was **right** — *"bounded corrections under the
> approved TS R4"*, *"No HL/TS amendment is needed"*. In AFD-48 round 4 the defect was demonstrated by an
> executable green counterexample. Under HL Deliverable 6 each of these rounds is forbidden, and each
> forbidden round shipped a real defect: a validator that does not require a declared human, a
> non-terminating lock path, a gate a standard Gradle build walks straight through.
>
> Deliverable 6's rationale — *"a third round is not a third attempt. It is the signal that the
> specification was wrong"* — is a claim about the corpus, and the corpus says the opposite four times out
> of five.

**Counter-evidence, sought as `deep` mode requires, and it is real.** Both deep chains in this repository
ended badly: `ASSISTED15` ❌ REJECTED, TFW-60's Phases B and C dropped by amendment A8. The correlation in
HL §2.2 stands. The cap would not have saved either task — the rounds were finding genuine defects — but
it would have converted a slow REVISE into an early REJECT. **A cheaper failure is a real benefit and it
is a different benefit from the one the contract claims.** A cap defended as *"we stop paying for a task
that is going to fail anyway"* is honest and survives this evidence. A cap defended as *"round three means
the spec was wrong"* does not.

**The decisive objection to the cap is not that it is wrong. It is that it is aimed at the wrong object.**
In the one case with a diagnosable cause — AFD-48, G5 — the depth was produced by a rung-2 item ordered
three times and never delivered. A cap would have stopped that loop at round 3 with the coordinator ruling
still unmade, the AC-5 semantics still unratified, and the executor still holding an item they may not
discharge. **The loop would have ended and nothing would have been decided** — which is the exact failure
Principle 4 names: *"a loop ends in a decision, never in exhaustion."*

### C3 — The delivery site already exists, and the ladder is one missing edge

This is the strongest constructive finding in the iteration, and it was not in any hypothesis.

**`conventions.md` §5 already contains the ladder** — attached to the wrong verdict:

```text
conventions.md §5, lines 80-81, measured verbatim 2026-09-02:

  🔄 REVISE — specific issues → back to execution (same task)
                                └── ONE destination. No rung 2. No rung 3.

  ❌ REJECT → 🛑 User decides: (a) 📝 HL_DRAFT   (b) 🔬 RES   (c) 🟡 TS_DRAFT
                               └────── the three-way route ALREADY EXISTS ──────┘
```

**A reviewer holding a rung-2 finding has no door.** The only state that means *the coordinator must
change the TS* is `TS_DRAFT`, and the canon reaches it **only through ❌ REJECT**. So a reviewer whose work
is sound but whose TS needs one ruling must either over-escalate the whole verdict to REJECT, or write the
item into `### If REVISE — items to fix:` — a list whose only reader is the executor, the one role that may
not amend a TS.

**AFD-48 `phase-a` is that dilemma, executed three times.** The reviewer chose REVISE — correctly, the work
was sound — and the rung-2 item had nowhere to land. rev2, rev3, rev4.

**Every site the ladder needs is already shipped:**

| Rung | Decider | Existing site | Evidence it exists |
|---|---|---|---|
| 1 | executor | `lifecycle: ONB`/`RF`, the current REVISE path | `conventions.md` §5 line 80 |
| 2 | **coordinator** | **`lifecycle: TS_DRAFT`** | in the status vocabulary; in §5's REJECT route; and used by name by TFW-60's reviewer — *"The narrowest viable route is **`TS_DRAFT`**"*, quoted in HL §2.5 |
| 3 | owner | **`amendment_escalated`** journal event + HL §12 | `templates/journal/event.md`: *"a frozen-section change was filed for an owner verdict"* |

**So Deliverable 3 is not an addition. It is the removal of an asymmetry:** §5 gives REJECT a three-way
route and gives REVISE one. Extend the existing three-way route to REVISE and the ladder is structural,
enforced by the state machine, with **zero new entities** — DoF 1 satisfied, Principle 7 satisfied, and
Principle 6's *"subtraction is the proof"* satisfied literally, because what is removed is an inconsistency.

**And it terminates the loop for free (D1-C).** A rung-2 item sets the task to `TS_DRAFT`. `TS_DRAFT` is not
a state an executor works in — `handoff.md` begins at `ONB`. The executor **cannot** produce a rev3 while
a rung-2 item is open, because the state machine has taken the work away from them. AFD-48 could not have
reached round 4: round 2's *"Obtain coordinator amendments"* would have moved the task to `TS_DRAFT` and
the coordinator would have had to pass through before another executor round existed.

**The HL quotes this mechanism in §2.5 as evidence that the ladder was field-validated, and does not
recognise it as the ladder's implementation.**

### C4 — The fourth answer the criterion produces, and why it is not a fourth outcome

E1 found three rows where the criterion says *material* and the ruling *not material* is still right,
because the fix is forbidden by a frozen AC, by DoF, or by a cost the reviewer named. Filing these as
`not material` makes the record false.

**The attack on adding a fourth outcome:** DoF 7 — *"Deferral reappears under a new name: any outcome that
accepts an item without a decision."* A cell called *material but not actionable* is deferral with a
better vocabulary, and the retired debt registry is what it grows into.

**The attack survives, and it eliminates D3-B as an outcome.** But it does not eliminate the finding,
because what E1 exposed is not a missing outcome — it is **two questions collapsed into one column**:

```text
                  TODAY                              WHAT E1 MEASURED
        ┌──────────────────────┐            ┌───────────────┬──────────────────┐
        │  one column          │            │ is it owed?   │ may we pay it?   │
        │  paid/promoted/      │            │ (the criterion│ (the contract:   │
        │  not material        │    ──►     │  answers)     │  frozen AC, DoF, │
        └──────────────────────┘            │               │  named cost)     │
          rows 3, 5, 7 must lie             └───────────────┴──────────────────┘
          about one to record the other       rows 3,5,7 = YES / NO — legible
```

`not material` stays a three-outcome vocabulary. What changes is that the **ruling states which question
it answers** — and when the answer is *owed, and the contract forbids paying it*, the ruling names the
clause that forbids it. That is not a fourth outcome and it creates no queue: the item is closed, on the
record, with the reason it is closed. Rows 3 and 7 already did exactly this in prose; nothing made them,
and nothing makes the next reviewer.

### C5 — Counter-evidence against C7 itself

`deep` mode requires attacking the survivor. Three real objections:

1. **`TS_DRAFT` on a REVISE re-opens the TS, and a TS re-opened is a scope door.** A coordinator asked to
   rule on `RegistryApiTest 49→50` may rewrite more than the ruling needed. Mitigation exists in the canon
   — the TS is downstream of a frozen HL — but the risk is real and belongs in HL §9.
2. **The state machine cannot tell a rung-2 finding from a rung-1 one; a reviewer still classifies.** C7
   makes the *consequence* structural, not the *judgement*. A reviewer who misclassifies still misroutes.
   This is honest and is the limit of what structure buys.
3. **Escalation-completion has no cap, and DoD 7 requires one.** C7 keeps the cap and uses the
   unchanged-item detector as its trigger — *the same item survived a round* — which fires on AFD-48 at
   round 3 and does **not** fire on TFW-60 `phase-a` rev3, where every rev2 item was closed and new ones
   found. A round count cannot tell those apart; an item comparison can, and both are visible in files
   that already exist.

---

## Checkpoint

| Found | Remaining |
|-------|-----------|
| The criterion's four words admit **all nine** rows under adversarial scoring — the prediction requirement is what discriminates | Whether `NS1`'s citation should be re-stated as the *axis* rather than the *test* — wording, for the TS |
| The cap is defensible as *cheaper failure*, not as *the spec was wrong*; the corpus refutes the second | — |
| **`conventions.md` §5 gives REJECT a three-way route and REVISE one** — the ladder is a missing edge, not new text | Whether extending it belongs in §5, in `review.md`, or both — a coordinator choice |
| All three rungs have existing sites: `ONB`/`RF`, `TS_DRAFT`, `amendment_escalated`. Zero new entities | — |
| `TS_DRAFT` terminates the loop structurally — an executor cannot produce a rev3 from it | H3 — whether the coordinator's act can be non-rubber-stamp — untested, deferred as briefed |
| The disposition column collapses *is it owed* with *may we pay it*; 3 of 9 rows had to lie about one | — |

**Sufficiency:**
- [x] External source used? — `conventions.md` §5, `templates/journal/event.md`, the status vocabulary, and TFW-60's REJECT verdict, all read this session
- [x] Briefing gap closed? — the mandated unfalsifiability attack was executed and it succeeded
- [x] Pairwise incompatibility checked? Surviving configurations listed? — 8 incompatible pairs, 2 survivors, C1 eliminated on two independent grounds
- [x] Hypothesis tested? — H1's confirmation was attacked and survived in modified form; H2's refutation was attacked and the cap's honest defence was found
- [x] Counter-evidence sought? — C2's counter-paragraph and all of C5 argue against this iteration's own conclusions

**Metacognitive check.** New. The Challenge stage was expected to weaken the criterion and it did — but the
finding that matters came from asking *where does a routed item land*, which no hypothesis asked. The
answer was in `conventions.md` §5 the whole time, one line above the sentence HL §2.1 counted.

Stage complete: YES
→ User decision: proceed — gates written through on the owner's *"no questions to me"*
