# RES — TFW_20260902-112841_RDP: Review Decision Protocol

> **Date**: 2026-09-02
> **Author**: Claude Code (Researcher), on behalf of `saubakirov`
> **Status**: 🔬 RES — Iteration 1 complete
> **Parent HL**: [HL-TFW_20260902-112841_RDP](../../HL-TFW_20260902-112841_RDP.md)
> **Mode**: Pipeline · `deep` (configured default `focused`; escalated — see Briefing)
> **Iteration**: 1 of 2 (min) / 3 (max)
> **Gates**: written, not taken — owner instruction *"no questions to me"*, 2026-09-02

---

## Research Context

The HL sent this iteration into three corpora that behave differently on the same review templates, to
test five hypotheses of which two could fail the task outright. 331 REVIEW files across five repositories
were censused; the complete population of rounds past two (7 files) and the complete population of
dispositions ruled under the new gate (9 rows) were opened and classified; and the six mechanisms the task
must ship were drafted into `review.md` and counted. **Two of the HL's own corpus numbers were wrong, two
of its five hypotheses did not survive their own evidence, and the mechanism the design is missing turned
out to be already shipped and quoted in the HL without being recognised.**

## Briefing

[`1_briefing.md`](1_briefing.md) — mode escalation to `deep`, sampling method, hard boundaries, and the
three questions that would have been asked had the owner not directed the run to proceed without gates.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Run `deep`, not the configured `focused` | H1 and H4 can fail the task; HL §10's Challenge focus mandates counter-evidence, which `focused` does not require |
| D2 | Census all 331 REVIEW files by command; open only the two complete populations that matter | `max_files_per_stage` is 15 against 331 files. Sampling the *whole* of two small populations beats sampling a large one badly. 14 files opened |
| D3 | Re-run every HL corpus count before building on it | Trust Protocol: numbers are empirical. Two were wrong, both from greps matching task directory names rather than review filenames |
| D4 | Classify each deep round as **work / spec / record** rather than counting rounds | H2 is a claim about *what* late rounds correct. A count cannot test it |
| D5 | Test H4 by writing the text and measuring, twice — one honest draft, one maximum compression | H4 is answerable by writing, not investigating (HL §10). A single draft would confuse *did not* with *cannot* |
| D6 | Score the criterion against the complete 9-row TLD population, then re-score adversarially | The first pass tests whether it discriminates; the second tests whether the discrimination is real or an artifact of the scorer |
| D7 | Add `kaznpu-ai-lab` as a second control | One control case cannot separate *easier work* from *no loop tracing*. A corpus with a 27 % REVISE rate and zero repeat rounds does |
| D8 | Report the cap's honest defence even though H2 is refuted | The cap survives on a different rationale than the contract states. Killing the mechanism because its stated reason failed would discard a real benefit |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Does DoD 10 bind per section or across Steps 4–6? | 🔴 open — owner | The two readings give opposite verdicts on whether the task is achievable. Raised as amendment **A1** |
| Q2 | Does Step 5's 73-word debt-search snippet stay? | 🟡 coordinator | It is the difference between 499 and 426 against a 483 budget. TLD shipped it three days ago |
| Q3 | Why does `helpdesk` mark ❌ at one-fifth this repository's rate? | 🔴 open | Not determined. Easier work and a more lenient reviewer both fit the data. Carried to iteration 2 |
| Q4 | Can the coordinator's single act be made non-rubber-stamp without a new entity? | ⚪ deferred | H3, not assigned to this iteration by the briefing |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | The criterion discriminates; at least one of the eight ad-hoc rulings would change | open | ✅ **CONFIRMED — exceeded** | **3 of 9 change** (rows 3, 5, 7), 1 arguable. `3_extract.md` E1 |
| H2 | Rounds past the second correct wording or specification rather than work | open | ❌ **REFUTED** | **4 of 5** substantive deep rounds corrected **work**; 2 reviewers certified at round 3 that the spec was right. `3_extract.md` E2 |
| H4 | The mechanisms fit under budget — the excess is prose standing in for terms | open | 🟠 **CONDITIONAL** | **499 vs 483** by group (achievable); **199 vs 109** in Step 4 alone (unreachable). F40 confirmed: Step 5 shrank **24 %** while gaining two mechanisms. `3_extract.md` E4 |
| H5 | Loops invented elsewhere converge on the same ladder | open | ❌ **NOT CONFIRMED** | **3.3 %** of 331 reviews name a decider; 7 of 11 instances are in this repository. Where reached independently (AFD-48), it was never delivered. `2_gather.md` G6, G5 |
| H6 | `helpdesk` avoids the loop for a locatable reason worth more than the cap | open | ❌ **FALSIFIED (useful branch)** | `helpdesk` has **0** repeat rounds and **3 REVISE verdicts that never reached a second verdict**. There is no practice to import. `2_gather.md` G3 |
| H3 | The coordinator's act can be made non-rubber-stamp without a new entity | open | ⚪ **DEFERRED** | Not assigned to iteration 1 by the briefing |

**Against the HL's own filter.** H1 true → the criterion survives DoF 3, *in modified form* (see A4).
H2 false → *"the cap is arbitrary and must be re-derived or dropped"* — it is re-derived, on a different
rationale, in A2. H4 false under one reading → *"DoD 10 and the deliverables cannot both hold, and the
owner must rule which gives"* — A1. H5 false → *"the receiving prose must be written far more carefully"* —
and C3 shows prose is not enough at any level of care. H6's confirmation would have replaced part of the
design; its falsification instead supplied direct evidence for Deliverable 7.

## HL Update Recommendations

> The researcher classifies. The researcher never applies.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2.2 | `helpdesk` repeat rounds **1 → 0**. Surfaces here that ran a repeat round **8 → 5** by REVIEW basename (`phase-a`, `phase-aa`, `phase-ab`, `ASSISTED15`, `TLD`). The two originals came from a grep matching task directory names — `HD-16__user_feedback_v12`, `AFD-18__…_android_v1` — not review filenames. *Past two rounds* = **3** ✅ stands | G1 |
| R2 | §2.2, §10 | `ai-first-devices` REVIEW files **150 → 149** outside `.tfw/`. The cap's evidence base is **7 files, not 4** — AFD-48 `phase-a` rev3/rev4 and two more rev3 surfaces | G1, G4 |
| R3 | §10 corpus table | Replace *"`helpdesk` … 1 … almost never loops"* with the measured row, and add `kaznpu-ai-lab` as the second control: 10 reviews, **27.3 % REVISE**, **0 repeat rounds**. Two corpora with opposite finding rates and identical loop behaviour | G1, E5 |
| R4 | §2 (new §2.9) | **The §5 routing asymmetry**, which is the task's real gap: `conventions.md` §5 gives ❌ REJECT a three-way route (`HL_DRAFT` / `RES` / `TS_DRAFT`) and gives 🔄 REVISE exactly one destination — *"back to execution."* A reviewer holding a rung-2 finding has no door that is not REJECT | C3 |
| R5 | §2.4 or §2.6 | The disposition column collapses two questions — *is it owed* and *may we pay it*. On 3 of 9 TLD rows the reviewer had to answer the second in a cell labelled for the first | E1, C4 |
| R6 | §9 Risks | Add: *"A rung-2 route to `TS_DRAFT` re-opens the TS and becomes a scope door"* — Medium / Medium; the coordinator rules only the named item, and the TS stays downstream of a frozen HL | C5.1 |
| R7 | §9 Risks | Amend the two-round-cap row: the corpus evidence supports the cap as **cheaper failure**, not as *"the spec was wrong."* The mitigation as written cites §2.2's three cases as evidence for a claim E2 refutes | E2, C2 |
| R8 | §10 Hypotheses | Set statuses: H1 confirmed, H2 refuted, H4 conditional, H5 not confirmed, H6 falsified, H3 deferred | this RES |
| R9 | §7.2 | Add a citation row: `conventions.md` §5 lines 80–81 — the existing REJECT three-way route and the single-destination REVISE. It is the enforcement site Principle 7 demands and Deliverable 3 does not name | C3 |
| R10 | §11 | Add SS1 below | this RES |

### Amendment Proposals — frozen sections, owner verdict required

| # | § | Type | Proposed change | Evidence | Cost | Alternatives considered |
|---|---|------|-----------------|----------|------|------------------------|
| **A1** | §5 DoD 10 · §6 DoF 2 | `SUPERSEDE` | Two corrections. (a) The named baselines are wrong: Steps 4–6 measure **483** words, not 461; Anti-patterns **163**, not 161. (b) State the binding unit explicitly. DoD 10's sentence says *per section*; its numbers are for a three-step group. **Per section the task is unsatisfiable at planning time** — Step 4 is 109 words and must carry four of six mechanisms, tightest honest draft 199 (+83 %). Proposed: the budget binds across **Steps 4–6 as a unit at ≤483**, with per-step figures reported in the RF | E4, G7. Reproducible: `awk '/^## Step 4/{f=1} f&&/^## Step 7/{exit} f' .tfw/workflows/review.md \| wc -w` | The owner rules on a criterion he approved five hours earlier. Accepting also concedes that a step may grow, which was the point of the per-section wording | **Leave as written** — rejected: the task fails at execution on a criterion nobody can meet, which is exactly `S8`. **Cut Step 4 elsewhere** — nothing is left; Step 4's whole content is *"read three files and write the review."* **Move mechanisms to `conventions.md` §5** — relocates the overrun into another edited section with its own budget |
| **A2** | §4 Deliverable 6 · §5 DoD 7 | `SUPERSEDE` | Replace the round-count trigger with an **unchanged-item trigger**, keeping two rounds as the ceiling. *A round that returns an item the previous round already ordered is the terminating round* — the verdict must be ✅ APPROVE naming what remains, or ❌ REJECT to planning. Also restate the rationale: the cap buys **an earlier, cheaper failure**, not a diagnosis that the specification was wrong | E2: 4 of 5 substantive deep rounds corrected **work**. TFW-60 `phase-a` rev3 — *"bounded corrections under the approved TS R4; no HL amendment … needed"*; `ASSISTED15` rev3 — *"No HL/TS amendment is needed."* G5: AFD-48 returned *"Obtain coordinator amendments"* in rev2, rev3 **and** rev4 | The trigger requires comparing two REVIEW files' item lists — a reviewer act, not a script. Slightly more work than counting to three | **Keep the round cap as frozen** — rejected: it forbids four rounds that each shipped a real defect, and does not fire on the one case with a diagnosable cause until after the diagnosis was needed. **Drop termination entirely** — rejected, DoD 7. **Cap at three** — rejected: arbitrary in the same way, and the corpus offers no support for any number |
| **A3** | §4 Deliverable 3 | `EXTEND` | The ladder needs a **landing site**, not better prose. Extend `conventions.md` §5's existing three-way route from ❌ REJECT to 🔄 REVISE: rung 1 → execution (unchanged); **rung 2 → `lifecycle: TS_DRAFT`**; rung 3 → an **`amendment_escalated`** journal event + HL §12. All three states and the event kind already exist — **zero new entities** | C3. TFW-60's reviewer used the site by name — *"The narrowest viable route is `TS_DRAFT`"* — quoted in HL §2.5 without being recognised as the implementation. G5: the ladder stated in prose produced nothing three times in AFD-48 | One edge on `conventions.md` §5's diagram, plus the `review.md` sentence that uses it. Cheaper than the prose Deliverable 3 currently implies | **Ladder in prose as frozen** — rejected: F30, and G5 is the measured failure. **A new routing artifact** — rejected, DoF 1. **Route rung 2 through REJECT** — rejected: over-escalates sound work, which is why AFD-48's reviewer refused it |
| **A4** | §4 Deliverable 1–2 · §7 Principle 1 | `EXTEND` | State that `NS1`'s four words name the **axis** and the prediction is the **test**. Adversarially, all nine TLD rows score YES on the four words — in a project whose deliverable is documentation, every defect is an inspectability defect. In all five agreements the ruling turned on a named consequence or its named absence, never on which word applied | C1, scored against the complete 9-row population | Deliverable 1 currently reads as if the four words decide. Correcting it makes Deliverable 2 the operative rule and demotes Deliverable 1 to vocabulary | **Leave as frozen** — rejected: DoF 3 fires, since a test that admits all nine cannot fail. **Drop the `NS1` citation** — rejected: Principle 1, and the citation is what makes a ruling refusable by someone who was not there |
| **A5** | §4 Deliverable 2 · §3.1 | `EXTEND` | The ruling must state **which question it answers**. On 3 of 9 rows the criterion says *owed* and *not material* is still correct, because the fix is forbidden by a frozen AC (row 3), by DoF (row 7), or by a named cost (row 5). Filing those as `not material` makes the record say the reviewer thought it did not matter, when they argued at length that it did. **No fourth outcome** — three stay; the ruling names the clause that forbids paying | E1, C4 | One clause in Step 5 and one column note in `templates/REVIEW.md` §5 | **A fourth outcome** *material but not actionable* — rejected on DoF 7: it is deferral with a better vocabulary. **Leave it** — rejected: §3.1 promises the ruling *"states WHAT WILL NOT HAPPEN"*, and on these rows something will |

## Fact Candidates

> Human-Only Test applied strictly. Almost everything this iteration produced is agent-discoverable by
> running the commands recorded in the stage files, and is therefore **not** a fact candidate.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | process | For a run the owner marks *"no questions to me"*, the researcher writes every gate checkpoint but does not stop at it, and records in the Briefing the questions that would have been asked. The gates remain in the trace as decisions taken without him rather than gates that did not exist | User, 2026-09-02 command arguments | ★★☆ |

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS1 | process | **The owner delegated judgement for a run whose two decisive questions were his to rule on.** *"No questions to me"* arrived on an iteration that then produced five amendment proposals against sections he froze the same day — including one (A1) saying an acceptance criterion he approved cannot be met. Implication: an ungated run does not remove owner decisions, it **batches** them, and the batch is larger and later than the questions would have been. The compensating discipline is that every withheld question is written into the Briefing rather than resolved silently — which is what makes A1 a proposal rather than a quiet reinterpretation at execution time | User, 2026-09-02; Briefing § Guiding Questions | ★★☆ |

## Findings Map

**The causal chain, corrected. What the HL believed → what the corpus says:**

```text
  HL's causal model                        MEASURED 2026-09-02
  ─────────────────                        ───────────────────

  no cap on rounds                         conventions.md §5:
        │                                    🔄 REVISE  → ONE destination  (execution)
        ▼                                    ❌ REJECT  → THREE            (HL_DRAFT/RES/TS_DRAFT)
  loops run deep                                   │
        │                                          ▼
        ▼                                  a reviewer holding a rung-2 finding
  round 3 = the spec was wrong             has no door that is not REJECT
        │                                          │
        ▼                                          ▼
  ∴ cap the rounds                         writes it into "items to fix"
                                           — a list only the EXECUTOR reads
     ✗ refuted: 4 of 5 deep rounds                 │
       corrected WORK, not spec                    ▼
                                           the executor MAY NOT amend a TS
                                                   │
                                                   ▼
                                           the item survives every round
                                           AFD-48 phase-a: rev2 · rev3 · rev4
                                           "Obtain coordinator amendments" ×3
                                                   │
                                                   ▼
                                           ∴ THE LOOP IS AN ESCALATION-DELIVERY
                                             FAILURE, NOT A COUNTING FAILURE
```

**The three corpora, and which control case answers what:**

```text
                REVISE rate      repeat rounds     REVISE→2nd verdict
  helpdesk         4.4 %              0                0 of 3     ┐ opposite finding rates,
  kaznpu-ai-lab   27.3 %              0                0 of 3     ┘ identical loop behaviour
  this repo       15.0 %              9                9 of 12    ← the OUTLIER
  ai-first-dev    15.0 %             11                    —

  ⇒ "not looping" is the DEFAULT across four corpora.
    helpdesk did not escape a loop. It never traced one.
    H6's premise — that looping is normal and helpdesk avoids it — is backwards.
```

**H1, scored twice against the same nine rows:**

```text
              honest scoring          adversarial scoring
  row 1   YES ──── paid        ✅       YES
  row 2   ?   ──── not mat.    ⚠️       YES  ← authority: an unenforced rule
  row 3   YES ──── not mat.    ❌       YES     teaches the canon is advisory
  row 4   NO  ──── not mat.    ✅       YES  ← inspectability
  row 5   YES ──── not mat.    ❌       YES
  row 6   NO  ──── not mat.    ✅       YES  ← continuation
  row 7   YES ──── not mat.    ❌       YES  ← inspectability
  row 8   NO  ──── not mat.    ✅       YES  ← inspectability
  row 9   NO  ──── not mat.    ✅       YES  ← inspectability
          ───────────────              ─────
          3 of 9 CHANGE                9 of 9 admitted
          H1 confirmed                 DoF 3 fires on the four words ALONE

  What discriminated was never the four words.  It was:
     "renaming would break every existing citation"      ← named consequence
     "neither is edited again, so nothing can drift"     ← named ABSENCE of one
     "this row IS the correction"                        ← harm discharged by recording
  ⇒ Deliverable 2 is doing the work Deliverable 1 is credited with.
```

**H4, drafted and measured — the budget question in one picture:**

```text
                   Step 4      Step 5      Step 6     TOTAL   vs 483
  today              109         289          63       483      —
  honest draft       285         260          59       626    +30 %
  max compression    199         219          59       499    +3.3 %   ← group: 16 words short
                     ↑           ↑
              +83 % FAILS   −24 % PASSES ← F40 measured: naming two terms
              4 of 6 mechs   while GAINING   deleted 70 words of prose
              land here      two mechanisms  that stood in for them

  per section  → unreachable, at any level of care
  per group    → a judgement call worth 73 words (the debt-search snippet)
  DoD 10 does not say which.  ⇒ A1
```

## Iteration Status

- **Iteration:** 1 of 2 (min) / 3 (max)
- **Hypotheses tested:** H1 ✅ confirmed · H2 ❌ refuted · H4 🟠 conditional · H5 ❌ not confirmed · H6 ❌ falsified
- **Hypotheses deferred:** H3 — not assigned to iteration 1 by the briefing; a design question answered by reading existing text
- **Gaps discovered:**
  1. `conventions.md` §5 routes REVISE to one destination and REJECT to three — the task's real gap, in no hypothesis
  2. The disposition column collapses *is it owed* with *may we pay it*
  3. DoD 10's binding unit is ambiguous and one reading makes the task unsatisfiable
  4. Why `helpdesk` marks ❌ at one-fifth this repository's rate — undetermined
  5. AFD `phase-b-s3-block1` and `phase-c1-block1` rev3 counted but not classified
- **Superseded decisions:** None

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | **H3 — can the coordinator's single act be non-rubber-stamp without a new entity?** | HL §9 lists it as *"unaddressed by design at this stage."* If no mechanism exists, DoF 1 forbids the one that would fix it and the authority move ships as a signature line | Read `review.md` Step 6, `templates/REVIEW.md` §5, the journal event kinds and the `status.md` schema for a site where the coordinator's ruling is a *recorded act* rather than a silent acceptance. A5's *"name the clause that forbids paying"* may already be that site |
| 2 | **Does the `TS_DRAFT` route survive contact with a real rung-2 finding?** | A3 is the iteration's strongest proposal and it is untested. If re-entering `TS_DRAFT` from REVIEW loses the review's own trace, or re-opens more of the TS than the finding needed, the mechanism is worse than the prose | Replay AFD-48 `phase-a` rev2 against the proposed route on paper: what does the coordinator receive, what may they change, what does the executor read on return, and what does `handoff.md` say to someone re-entering at `ONB` from `TS_DRAFT` |
| 3 | **The `helpdesk` ❌ rate — leniency or easier work?** | It decides whether *"not looping is the default"* is a finding about TFW or about this repository's subject matter. It also bounds what any corpus comparison in the HL may claim | Sample matched pairs: the same check row (`Purpose Check`, `DoD met?`) across ten `helpdesk` and ten local reviews, and compare what evidence each cites. A reviewer citing no evidence and marking ✅ is leniency; one citing evidence is easier work |
| 4 | **Classify AFD `phase-b-s3-block1` rev3 and `phase-c1-block1` rev3** | Two of seven deep rounds are counted but unclassified. H2's refutation stands at 4 of 5; these could make it 6 of 7 or 4 of 7 | Same work/spec/record classification as E2. Two files, bounded |
| 5 | **Does A2's unchanged-item trigger fire correctly on the whole corpus?** | It is proposed on two cases. A trigger that also fires on TFW-60 `phase-a` rev3 — where every rev2 item was closed — would be worse than the round count | Diff the item lists of every consecutive REVIEW pair in the 7-file deep population and check the trigger against each |

### Recommendation

- [ ] **SUFFICIENT**
- [x] **MORE NEEDED** — iteration 2, and not because `min_iterations: 2` requires it. Three specific
  reasons: **(a)** A3 is the iteration's strongest proposal and is untested against a real finding
  (thread 2); **(b)** H3 is untested and HL §9 already flags the rubber-stamp risk as *"unaddressed by
  design"*, so the authority move currently has no mechanism (thread 1); **(c)** H2's refutation rests on
  5 of 7 available cases, and completing the population is two files' work (thread 4). Threads 3 and 5
  are lower value and can be dropped without weakening the design.
- [ ] **BLOCKED**

> ⚠️ Coordinator decides. Five amendment proposals wait on an owner verdict before any frozen section
> moves; **A1 in particular reports that a frozen acceptance criterion cannot be met as written**, and
> execution should not start until it is ruled.

## Conclusion

This iteration measured 331 REVIEW files across five repositories and opened the two populations that
decide the task: every round past two (7 files, not the 4 the HL knew about) and every disposition ruled
under the new gate (9 rows). The criterion **discriminates** — three of nine rulings change, more than H1
claimed — but not for the reason the contract gives: adversarially, all nine rows score YES on `NS1`'s four
words, and what actually decided every ruling was a named consequence or its named absence. The two-round
cap's stated rationale is **refuted by its own corpus**: four of five substantive deep rounds corrected
real work, and two reviewers wrote into a round-3 verdict that the specification was right. And `helpdesk`,
named by the owner as the control case, turned out not to avoid the loop at all — it has zero repeat rounds
because none of its three REVISE verdicts ever reached a second one, a pattern `kaznpu-ai-lab` repeats at
six times the finding rate. Not looping is the default; this repository is the outlier.

**What research provided that would have been missed:** the cause. The HL's model is *no cap → deep loops*.
The corpus says `conventions.md` §5 gives ❌ REJECT a three-way route and 🔄 REVISE exactly one, so a
reviewer holding a finding only the coordinator can discharge must write it into a list the executor reads
— and AFD-48 did that three times across rev2, rev3 and rev4 while the amendment was never logged. The
loop is an escalation-delivery failure. Every site the fix needs is already shipped, including the one the
HL quotes in §2.5 without recognising it. Without this iteration the task would have legislated a round cap
that forbids four rounds which each caught a real defect, against a DoD whose own numbers are 22 words
wrong and whose binding unit makes it unsatisfiable.

**Self-critique.** Three weaknesses. **(1)** H2 rests on 5 of 7 available cases; two AFD rev3 files were
counted and not opened, and completing them could move the ratio either way. **(2)** The work/spec/record
classification is my judgement on other people's verdicts, made from the §4 text alone without reading the
diffs those rounds produced — a reviewer's own words about what they were ordering, which is good evidence
but not the same as the change. **(3)** The `helpdesk` leniency question is left open, and it bounds how
much any cross-corpus claim in this RES may be leaned on; I state the loop-closure finding confidently
because zero-of-six is not a rate question, and I state the ❌-rate finding as undetermined for the same
reason.

---

*RES — TFW_20260902-112841_RDP: Review Decision Protocol | 2026-09-02*
