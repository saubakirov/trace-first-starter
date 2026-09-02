# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260902-112841_RDP](../../HL-TFW_20260902-112841_RDP.md)
> Goal: Every finding a review produces becomes a decision by rule — one criterion, one named decider, one termination.

## Configuration Space

Cross-product of Gather's five dimensions, reduced per the template's rule: **C1 is the HL's design as
frozen**, and every other row differs from it in at least one column.

| Config | D1 Termination | D2 Decider | D3 Vocabulary | D4 Criterion site | D5 Budget |
|---|---|---|---|---|---|
| **C1 — the HL as frozen** | A: round cap (2) | B: ladder in prose | A: three outcomes | B: Step 4 + `conventions.md` §5 | A: per section |
| C2 | A: cap | **C: ladder + delivery site** | A: three | B | A |
| C3 | **C: escalation-completion** | C: ladder + delivery site | A: three | B | A |
| C4 | **B: unchanged-item detector** | C: ladder + delivery site | A: three | B | A |
| C5 | A: cap | C: ladder + delivery site | **B: three + not-actionable** | B | A |
| C6 | C: escalation-completion | C: ladder + delivery site | B: three + not-actionable | **C: a column in `templates/REVIEW.md`** | **B: per group** |
| C7 | **A+B: cap, with the detector as its trigger** | C: ladder + delivery site | B: three + not-actionable | **D: all three sites** | B: per group |
| C8 | D: nothing | A: always executor | A: three | A: Step 4 only | D: none — *status quo, the null row* |
| C9 | A: cap | **D: always coordinator** | A: three | B | A | *— retained only to be eliminated; DoF 6* |

**C7 is the combination nobody proposed**, and it is assembled entirely from parts the HL already owns.
It is developed in E4.

---

## Findings

### E1 — H1: the criterion scored against all nine TLD rows, blind, then compared

The complete population of dispositions ruled under TLD's gate. Each row was scored against `NS1`'s four
words *before* re-reading its actual ruling; the ruling column is transcribed, not summarised.

| # | The finding | Criterion score | Ruled | Agree? |
|---|---|---|---|---|
| 1 | Frontmatter leaked as body text on 860 of 990 built pages | **YES — inspectability.** A reader cannot inspect material grounds rendered as YAML garbage | `paid` | ✅ |
| 2 | `review.md` 1 708 words vs a ≤1 200 rule four of ten files breach | **ARGUABLE.** Nothing named happens to a reader; but *"a rule nothing enforces"* is a real claim on **authority** | `not material` — *"the rule is stale, not the file"* | ⚠️ |
| 3 | Five blank lines inside a sealed region; the table renders as six blocks | **YES — inspectability.** The table is literally unreadable as a table | `not material` — *"AC-1 forbids reformatting the sealed region, and that prohibition is the point"* | ❌ **disagree** |
| 4 | Uppercase filenames outside the project root | **NO.** Nothing named happens; renaming breaks every citation | `not material` | ✅ |
| 5 | `paid` is ambiguous; a first-time reviewer may hit the role lock | **YES — continuation.** *"the next reviewer stalls"* is exactly a checkable prediction | `not material` — *"I met this gate as its first user and resolved it in under a minute"* | ❌ **disagree** |
| 6 | Retirement procedure stated twice in two frozen release artifacts | **NO.** Neither is edited again, so nothing can drift | `not material` | ✅ |
| 7 | Nothing checks that an adapter copy matches its source; drift recurs in the field (`TD-110`) | **YES — inspectability.** A reader cannot know whether the copy they hold matches its source, and the recurrence is evidenced | `not material` — *"a checker is a new maintained artifact, which HL DoF 5 and TS §2 forbid outright"* | ❌ **disagree** |
| 8 | *"24 adapter copies"* contradicts its own enumeration of 33; *"41 modified"* vs 42 | **NO — the row is the correction.** Recording it repaired the inspectability it damaged | `not material` | ✅ |
| 9 | `+247 %` attributed to 17 days in one file and 19 in another | **NO.** The shipped figure is right; the correction is on the record | `not material` | ✅ |

**H1 — CONFIRMED, and by a wider margin than the hypothesis claimed.** H1 asked for *"at least one of
those eight would change."* **Three change** (rows 3, 5, 7) and a fourth is arguable (row 2). The criterion
discriminates: 5 agreements, 3 disagreements, 1 arguable, on a population of 9.

**And the three disagreements share one shape, which is the finding.** In every one, the criterion says
*material* and the reviewer's ruling is still *correct* — because the fix is **out of bounds**:

| Row | Criterion says | Why the reviewer was right anyway |
|---|---|---|
| 3 | material — inspectability | AC-1, a **frozen acceptance criterion**, forbids touching it |
| 5 | material — continuation | *"adding one to fix a gap nobody has yet fallen into is ceremony"* — a cost judgement, not a materiality judgement |
| 7 | material — inspectability | **DoF 5** forbids the only fix that exists |

**The three-outcome vocabulary has no cell for *material, and deliberately not fixed*.** Today those are
filed as `not material`, and the record then says something false: the reviewer *did* think it mattered and
argued so at length in the same cell. HL §3.1's diagram sends `NO` to *"NOT MATERIAL, and the ruling states
WHAT WILL NOT HAPPEN."* For rows 3, 5 and 7 something **will** happen, the reviewer knows it, and the
ruling is an accepted cost rather than a prediction of nothing.

This is the first thing the criterion **did** — it separated *is it owed* from *may we pay it*, which the
current design conflates. It is developed as an amendment proposal.

### E2 — H2: what the deep rounds actually corrected

Every round past two in every corpus, classified against G4's raw quotes. **work** = a functional or
contractual defect in the deliverable; **spec** = the specification itself must change; **record** = the
artifact describing the work, not the work.

| # | Surface | Round | work | spec | record | Would the cap have destroyed a fix? |
|---|---|---|:---:|:---:|:---:|---|
| 1 | TFW-60 `phase-a` | rev3 | **●** | ● | ● | **YES** — a validator that does not require a declared *human* would have shipped |
| 2 | TFW-60 `phase-a` | rev4 | — | — | — | no — this is the terminating ✅ |
| 3 | TFW-60 `phase-aa` | rev3 | — | — | **●** | **NO** — and the owner applied the cap by hand: *«эти мелочи править не будем»* |
| 4 | `ASSISTED15` | rev3 | **●** | — | ● | **YES** — a non-terminating Windows lock/ACL path would have shipped |
| 5 | AFD-48 `phase-a` | rev3 | **●** | **●** | ● | **YES** — a green build could re-open the production class the gate promises to close |
| 6 | AFD-48 `phase-a` | rev4 | **●** | **●** | ● | **YES** — AC-6 still falsified by an executable counterexample |
| | **totals (5 substantive rounds)** | | **4** | 3 | 5 | **4 of 5** |

**H2 — REFUTED.** The hypothesis states that *"rounds beyond the second correct wording or specification
rather than work."* **Four of five substantive rounds past two corrected work**, and in four of five the
cap would have destroyed a real fix. The one round that matched H2's description is the one the owner had
already capped by hand without a rule.

**The refutation is sharper than a count, because two reviewers wrote the opposite of the cap's premise
into the round-3 verdict itself:**

> TFW-60 `phase-a` rev3: *"All three are **bounded corrections under the approved TS R4**; no HL amendment
> or new budget ruling is needed."*
>
> `ASSISTED15` rev3: *"**No HL/TS amendment is needed.** The same Executor must make only the bounded
> corrections below."*

HL Deliverable 6 asserts that *"a third round is not a third attempt. It is the signal that the
specification was wrong."* Two independent reviewers, at round 3, certified in writing that the
specification was **right** and the round was rung-1 executor work. The cap's stated rationale is
contradicted by the only evidence there is for it.

**What survives, and it is not nothing.** Both deep chains ended badly — `ASSISTED15` ❌ REJECTED,
TFW-60's Phases B and C dropped by amendment A8. The HL's §2.2 correlation holds. But the causal reading
inverts: the rounds were correcting real defects and the tasks failed anyway, so a cap would not have saved
either. It would have converted a REVISE into a REJECT sooner — which is a **cheaper failure**, not a
prevented one. That is a defensible reason to want a limit, and it is a different reason from the one in
the contract.

### E3 — H5: convergence is weak; delivery is the actual failure

G6's rate is 3.3 % across 331 reviews, 7 of 11 instances inside this repository. **H5 — NOT CONFIRMED.**
The ladder is this repository's habit, and the HL's own filter prescribes the consequence: *"the receiving
prose must be written far more carefully."*

G5 says why care is not enough. In AFD-48 `phase-a` the ladder **was** reached independently — the reviewer
named rung 2 correctly in rev2, rev3 and rev4 — and it produced **nothing**, three times. The reason is
structural and it is visible in the template: the only place a REVISE finding can be written is
`### If REVISE — items to fix:`, a list whose sole reader is the **executor**. A rung-2 finding written
there is addressed to the one role that may not discharge it.

> **A ladder that names a decider but has no site where that decider must act is the F30 pattern exactly** —
> *"capture without an enforcement site does not change behaviour."* Deliverable 3 as frozen states the
> ladder. It does not state where a routed item lands.

This is the strongest argument in the research, and it argues **for** the HL's design and **against** its
sufficiency.

### E4 — H4: drafted and counted, and the answer depends on a word DoD 10 leaves ambiguous

Two drafts of Steps 4–6 were written with all six mechanisms in — the criterion, the prediction rule, the
ladder, the authority move, the revision definition, the termination rule. Drafts are in the session
scratchpad; the counts are reproducible by the command in G7.

| Draft | Step 4 | Step 5 | Step 6 | **Total** | vs 483 |
|---|---:|---:|---:|---:|---:|
| baseline (today) | 109 | 289 | 63 | **483** | — |
| first honest draft | 285 | 260 | 59 | **626** | **+30 %** |
| maximum compression | 199 | 219 | 59 | **499** | **+3.3 %** |
| …and cutting Step 5's 73-word debt-search snippet | 199 | 146 | 59 | **426** | **−12 %** |

**Three results, and they do not agree with each other.**

1. **F40 is confirmed empirically.** Step 5 **shrank** — 289 → 219, **−24 %** — while *gaining* two
   mechanisms. Naming the criterion and the prediction rule deleted the two paragraphs that were standing
   in for them: *"reject filler — only items that would cause real problems if left unfixed"* and
   *"`not material` is a first-class answer."* The owner's *"which term is missing, since a paragraph is
   standing in for it"* is not a metaphor here; it is a measured 70-word saving.

2. **Under the group reading, H4 is nearly true and is a judgement call.** 499 against 483 is **16 words**.
   Cutting the debt-search snippet clears it by 57. Whether that snippet stays is a coordinator decision
   about a mechanism TLD shipped three days ago, not a compression problem.

3. **Under the per-section reading, H4 is FALSE and unreachable.** Step 4 is **109 words** and must carry
   **four of the six mechanisms**. The tightest draft is 199. Step 5's 70-word surplus cannot be credited
   to Step 4 — that is what *per section* means. No compression closes an 83 % overrun on a step whose
   entire current content is *"read three files and write the review."*

**And DoD 10 does not say which reading binds.** Its sentence is per-section — *"Every section this task
edits ends no larger than it started"* — and the numbers it then names are for a three-step **group**:
*"`review.md` Steps 4–6 stand at 461 words and Anti-patterns at 161; those are the numbers to beat."*
Under the sentence the task is already failed at planning time; under the numbers it is achievable.

**This is `S8` recurring one granularity in, inside the criterion that `S8` was written about.** §2.8
records the owner catching a whole-file target that DoF 8 made unreachable. The correction moved the unit
from *file* to *section* — and stated the section budget in group numbers. The plausibility question was
asked once and answered once, and the same class of defect survived the answer.

### E5 — the two corpora that never loop, and what separates them

| | `helpdesk` | `kaznpu-ai-lab` | this repository |
|---|---|---|---|
| REVIEW files | 70 | 10 | 85 |
| REVISE rate | 4.4 % | 27.3 % | 15.0 % |
| ❌ per review | 0.20 | — | 1.06 |
| repeat rounds | **0** | **0** | 9 |
| REVISE verdicts that reached a second verdict | **0 of 3** | **0 of 3** | 9 of 12 |

`kaznpu-ai-lab` is the second control and it breaks the easier-work explanation: its REVISE rate is
**27.3 %**, six times `helpdesk`'s and nearly double this repository's — and it still has **zero** repeat
rounds. Two corpora, opposite finding rates, identical loop behaviour: **the REVISE is issued and the round
is never traced.**

So the honest answer to *"why does `helpdesk` not loop"* is not about `helpdesk`. **Of the six REVISE
verdicts issued outside this repository's line, zero produced a second REVIEW file.** Looping is not the
default that `helpdesk` escaped; **not looping is the default, and this repository is the outlier that
loops.** That inverts the HL's framing of the whole research case.

The `helpdesk`/`kaznpu` difference in ❌ rate remains real and is a separate axis from loop closure. It is
not resolved here and is carried as an open thread.

---

## Checkpoint

| Found | Remaining |
|-------|-----------|
| **H1 confirmed** — 3 of 9 rulings change, and all 3 share the shape *material but out of bounds* | Whether the coordinator's act should carry a fourth cell or a second column — a design choice for the TS |
| **H2 refuted** — 4 of 5 substantive deep rounds corrected **work**; 2 reviewers certified at round 3 that the spec was right | AFD `phase-b-s3-block1` / `phase-c1-block1` rev3 not classified |
| **H5 not confirmed** — 3.3 % across 331 reviews, and where reached it was never delivered | — |
| **H4 depends on a word** — 499 vs 483 by group (achievable), unreachable per section | Whether Step 5's debt-search snippet stays — coordinator's call, worth 73 words |
| **F40 measured** — Step 5 shrank 24 % while gaining two mechanisms | — |
| Not looping is the default across four corpora; this repository is the outlier | Why `helpdesk` marks ❌ at one-fifth this repository's rate |

**Sufficiency:**
- [x] External source used? — the criterion scored against a complete 9-row population; 7 deep rounds classified across two corpora
- [x] Briefing gap closed? — all four Extract bullets answered
- [x] Configuration Space built from Gather dimensions? — 9 configurations, C7 unproposed
- [x] Hypothesis tested? — four tested, one confirmed, two refuted or unconfirmed, one conditional
- [x] Counter-evidence sought? — H2 and H5 were the HL's own; both were attacked with its own corpus and did not survive

**Metacognitive check.** New, not confirmatory. Two hypotheses the HL expected to hold did not, and the
reason in both cases was the same missing piece — **delivery**, not rule. The criterion works and needs a
fourth answer; the ladder is right and needs a landing site; the cap is aimed at a symptom whose cause is
an escalation that never arrives.

Stage complete: YES
→ User decision: proceed — gates written through on the owner's *"no questions to me"*
