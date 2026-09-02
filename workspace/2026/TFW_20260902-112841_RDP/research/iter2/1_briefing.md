# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW_20260902-112841_RDP](../../HL-TFW_20260902-112841_RDP.md)
> Goal: Every finding a review produces becomes a decision by rule — one criterion from NS1, one named
> decider, one termination.

## Which HL version was read

The coordinator's `iterations.yaml` entry for this iteration asks this question explicitly, because the
entry was written *after* the owner launched the iteration. The answer:

| Read | Version | Bytes | Consequence |
|---|---|---:|---|
| Context load, before the mode gate | pre-amendment HL, 11:52 | 47 684 | Used only to recommend a mode and derive a focus, which the coordinator's entry then independently confirmed. **No stage file was written against it** |
| Before this file, and every read after it | post-amendment HL, 12:31 | 64 159 | A1, A2, A4, A5 approved; A3 applied as a refinement to deliverable 3; §2.9 added; §3.1 redrawn; §9 carries two new rows naming this iteration's thread 2 |

The mode recommendation and the three-thread focus were produced from `iter1/RES.md`'s Open Threads before
the coordinator's entry existed, and both matched it. That agreement is not evidence of anything except
that the threads were stated clearly in iteration 1; it is recorded because the coordinator asked which
text was in front of the researcher.

**What the corrected contract changes for this iteration, concretely:**

| | Iteration 1 read | This iteration reads |
|---|---|---|
| Deliverable 3 | *"the routing ladder … in `review.md` and mirrored in `conventions.md` §5"* — prose | **A3 applied**: rung 2 → `lifecycle: TS_DRAFT`, rung 3 → `amendment_escalated` + §12 |
| Deliverable 6 · DoD 7 | round-count trigger, two rounds | **unchanged-item trigger**, two rounds as ceiling |
| DoD 10 | per section, 461 / 161 | **Steps 4–6 as one unit ≤483**; `Anti-patterns` ≤163 |
| §9 Risks | 8 rows | **10 rows** — two of them name this iteration's thread 2 as the mitigation |

So thread 2 is no longer *"test the researcher's own proposal"*. It is **testing an applied part of the
contract**, and the risk register already lists it as the mitigation for two Medium/Medium risks. If it
fails, the failure lands on a deliverable, not on a proposal.

## Mode

`deep`, on the owner's decision of 2026-09-02, against the configured `focused`.

| | `focused` | `deep` — selected |
|---|---|---|
| OODA loops per stage | 1 | up to 3 |
| Counter-evidence | not required | **required** |
| Hypothesis per stage | — | ≥1 |

**Why it matters here and not merely as rigour.** Both live questions fail in the same direction — by
finding something that looks like an answer and is not. H3 fails by locating a "site" that on close
reading is a signature line the coordinator signs without checking anything; thread 2 fails by declaring a
route sound because it can be drawn. Neither failure is visible without an obligation to look for it. And
thread 2 is an adversarial test of text that reached the contract **through this researcher's own
proposal**: a single-pass mode lets the author confirm the author.

## Predecessor context (mandatory for iteration ≥2)

Predecessor: [`../iter1/RES.md`](../iter1/RES.md). Stage files: `1_briefing.md`, `2_gather.md`,
`3_extract.md`, `4_challenge.md`.

**Decisions carried forward:**

| # | Iteration 1 decision | How it binds this iteration |
|---|---|---|
| D2 | Census by command; open only complete populations | Thread 4 opens the last **2** of the 7-file deep population. After this iteration the population is closed |
| D3 | Re-run every corpus count before building on it | Two HL numbers were wrong last time. Any number this iteration reuses is re-run, including its own predecessor's |
| D4 | Classify a deep round as **work / spec / record**, not count it | Thread 4 uses the same three labels, so the 7 cases stay comparable |
| D8 | Report the honest defence of a mechanism whose stated reason failed | Applies now to A3: if the route breaks, say what it still buys before proposing its removal |

**Open threads assigned by the coordinator, in the coordinator's priority order:**

| Order | Thread (iter1 numbering) | Question | Can it change a deliverable? |
|---|---|---|---|
| 1 | **2** | Does A3's route survive a real rung-2 finding? | Yes — deliverables 3 and 7 |
| 2 | **1** (H3) | Is there an existing site that makes the coordinator's act checkable? | Yes — deliverable 4; and if the answer is no, DoF 1 collides with the authority move and the owner must rule |
| 3 | **4** | Classify the last two deep rounds | Yes, indirectly — it can move H2's ratio under an **already-approved** amendment (A2) |

**Dropped by the coordinator, on iteration 1's own recommendation:** thread 3 (`helpdesk`'s ❌ rate —
bounds what a corpus comparison may claim, changes no deliverable) and thread 5 (A2's trigger across the
corpus — folded into thread 4, which opens the same files).

**New direction since iteration 1:** the four approved amendments and the applied refinement. Nothing
else; the owner injected no new hypothesis.

## Research Plan

### Gather — "what do we not know?"

- **Replay material for thread 2.** AFD-48 `phase-a` rev2 is the real rung-2 finding: the item *"Obtain
  coordinator amendments. Reviewer cannot self-amend TS"* that then survived rev3 and rev4. Read the rev2
  REVIEW, that phase's TS, and its `status.md` — the route's inputs are exactly these three.
- **What that project did instead.** `AFD-48/phase-b/PROPOSAL__phase-b-s3-block1__revise_closure.md` was
  found while listing the corpus: a project with the same gap invented an **artifact** to close a revise.
  That is the strongest available counter-example to *"every site already exists"*, and it is direct
  evidence on DoF 1.
- **H3's candidate sites, enumerated before any is judged.** `review.md` Step 5 and Step 6,
  `templates/REVIEW.md` §5, the journal event-kind list and whether it is closed, the `status.md` schema,
  `conventions.md` §15's role table and §13 trace discipline.
- **The two unclassified deep rounds.** AFD-48 `phase-b-s3-block1` rev3 and — corrected here — AFD-**27**
  `phase-c1-block1` rev3. Iteration 1's RES filed the second under AFD-48; it is a different task.
- **External, on the rubber stamp.** How review and approval bodies outside this project keep a
  single-approver act from becoming a formality. This is the one question in the iteration where the
  project has no corpus of its own: 3.3 % of 331 reviews name a decider at all.
- **Candidate dimensions to decompose:** where a rung-2 item is *delivered*; what the coordinator's act is
  *recorded as*; what *bounds* a return round; where the executor *re-enters*; whether the review's own
  trace *survives* the round trip.

### Extract — "what does it mean?"

- Build the Configuration Space across those dimensions and mark which combinations the frozen contract
  already forbids (DoF 1 kills every column containing a new artifact — including AFD's own solution).
- The paper replay, step by step, with the question stated at each step: what does the coordinator
  receive, from where, what may they change, what does the executor read on return, what survives.
- Score each H3 candidate site on one test: **can a reader who was not there tell a real act from a
  formality by reading the artifact?** A signature cannot. A cited clause can.
- Classify the two rev3 rounds work / spec / record and restate H2's ratio.

### Challenge — "what would break this?"

- Argue that `TS_DRAFT` re-entry **loses the review trace**: the finding lives in a REVIEW file, and the
  lifecycle move points at the TS.
- Argue the **scope door**: a coordinator inside a reopened TS may change more than the named item, and
  nothing structural stops them.
- Argue that **no site makes the coordinator's act checkable without a new entity** — the honest case for
  H3 being false, which the coordinator's entry explicitly permits as an answer.
- Argue that A2's approved trigger **misfires**: an unchanged item can also mean the executor was given an
  impossible instruction, in which case the terminating verdict punishes the wrong party.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|---|---|
| H3 | The coordinator's single act can be made non-rubber-stamp **without a new artifact** — the mechanism exists in text already written (a verdict line, a column, an existing event kind) rather than needing a new one | ⚪ deferred to iteration 2 — *"A5's 'name the clause that forbids paying' may already be the site"* |
| H2 | Rounds beyond the second correct wording or specification rather than work | ❌ refuted at 4 of 5. **Reopened only to close the population** — 2 files remain |

H1, H4, H5, H6 are settled by iteration 1 and are not re-tested. Where this iteration's evidence touches
them it is reported as a correction, not as a re-test.

> **Filter, restated from HL §10 for the one live hypothesis.** H3 false → the authority move needs a new
> entity, which DoF 1 forbids, so the design changes shape. The coordinator's entry adds the honest
> corollary: *"The answer may be 'no mechanism exists without a new entity', and then the owner must rule
> between DoF 1 and the authority move. Do not invent one to avoid that."*

## Scope Intent

**In scope**

- Threads 2, 1 and 4, in that order, and nothing else.
- Reading `.tfw/` text this task will edit — `review.md`, `handoff.md`, `conventions.md`,
  `templates/REVIEW.md`, the journal event template — **as evidence about where a mechanism could land.**
- Reading, read-only, the AFD corpus for the replay and for the two unclassified rounds.
- Drafting text **only** where a draft is the measurement, as iteration 1 did for H4. A draft in a stage
  file is evidence, not a deliverable.

**Out of scope**

- Thread 3 and thread 5 — dropped by the coordinator.
- Re-testing H1, H4, H5, H6.
- Any edit to the HL. Iteration 1's classification discipline holds: **the researcher classifies,
  the coordinator applies.** This iteration may file a proposal against an *already-approved* amendment
  (thread 4 could) and must file it rather than absorb it.
- Any write outside this task directory. Sibling trees are read with `find`, `grep -n`, `sed -n`, `wc`
  and nothing else.
- `tasks/` in this repository: cited, never edited. It is the frozen legacy corpus.

## Guiding Questions

Gates are written and not taken: the owner directed this run with *«без вопросов ко мне»* on 2026-09-02,
the same instruction iteration 1 ran under and the practice recorded as FC1 there. The questions that
would have been asked are written here instead, so the batching effect S9 names stays visible.

1. **If H3 has no answer without a new entity, which gives — DoF 1 or the authority move?** The
   coordinator's entry says the owner must rule this and forbids inventing a mechanism to avoid asking.
   The iteration will produce the evidence and file the question; it cannot answer it.
2. **If AFD's `PROPOSAL` artifact turns out to be the thing that actually closed a revise loop, does DoF 1
   still hold?** It is the only case in 331 reviews where a rung-2 item was discharged by a named
   artifact. A contract that forbids the one mechanism observed to work deserves the question asked out
   loud.
3. **If thread 4 moves H2's ratio materially, is A2 reopened?** A2 is approved. Iteration 1's own rule
   says a finding against a ruled amendment is filed as a proposal, not absorbed — but whether the owner
   wants his own approval re-litigated on two files is his call, not the researcher's.

## User Direction

- **2026-09-02, mode gate.** Owner selected `deep` over the configured `focused`, and selected threads
  1+2+3 of the presented five — which the coordinator's `iterations.yaml` entry, written independently,
  ordered as threads 2 → 1 → 4.
- **2026-09-02, gates.** *«без вопросов ко мне. но прошу обратить внимание что координатор обновил HL и
  про ресерч и про итерацию. направил тебя четче куда видит. делай работу на основе того что он
  написал»* — the run proceeds without stopping, and the coordinator's updated HL and `iterations.yaml`
  entry are the authority for what this iteration investigates. Both were re-read in full before this
  file was written; the version table above is the record.

---
Stage complete: YES
