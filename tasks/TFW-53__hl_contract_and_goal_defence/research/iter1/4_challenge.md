# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW-53](../../HL-TFW-53__hl_contract_and_goal_defence.md)
> Goal: An approved HL becomes a frozen strategic contract that research may only amend through a logged, evidenced, owner-ruled channel.

**OODA loops run:** 3 of 3. L1 — pairwise consistency. L2 — attack the survivors, including the corpus itself. L3 — edge cases and the protocol's own blind spots.

---

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D1 Scope | B/C/D — anything less than all six | D2 Granularity | any | Every reduced set releases a section TFW-49 actually moved: §4 released → "Phase C flipped from bypass-the-hook to install-a-runtime" is a refinement; §5/§6 released → all 10 DoD and all 10 DoF replaced silently; §1/§3 released → Vision widened from agent-authored commits to every commit. The corpus supplies a counterexample for each reduction |
| D1 Scope | B/C/D | *(process)* | first research iteration | Any reduction requires amending frozen HL §3 on iteration 1. Not illegal — but it spends the owner's central decision to buy something D2 gives free (E2) |
| D5 Batching | C — one batch at the pre-TS gate | *(config)* | `min_iterations: 2` | Iteration N+1's briefing must build on iteration N's decisions (`iterations.yaml` requires it, and iteration 2's focus is written against iteration 1's outcome). Deferring all verdicts to pre-TS means iteration 2 is designed on top of unruled proposals |
| D5 Batching | D — passive log, no push | D8 REJECT | any | DoF-7 by construction: proposals accumulate with no resolution and the log becomes noise. Also leaves the contract in an undefined state while work proceeds |
| D6 Asymmetry | B — restrictive applies freely, unlogged | D4 Classify | A or C — an agent classifies | The classifier benefits from calling a change restrictive. S13: a grant that can justify its own extension is the root cause; self-served "this is only a tightening" is the same move in the opposite direction. Corpus proof that the label is unreliable: TFW-27 #1 "Remove artifact graph from all phases" reads as tightening and is a target-state redesign |
| D6 Asymmetry | D — impact-classed | D4 Classify | A or C | Same defect, worse: "impact" is self-assessed by the party that wants a low number. TFW-49's coordinator accepted 702-vs-700, 1708-vs-1200 and 3160-vs-2700 as "no material deviations" |
| D3 State | D — filesystem marker holding a snapshot | *(values)* | F22 template minimalism / single source of truth | Two copies of the contract can disagree, and nothing says which wins. D31's principle is *file existence = state*, not *file content = duplicate* — the HL file plus git history already provide the state |
| D3 State | A — header field only | *(acceptance)* | DoD-5 "baseline is diffable" | A header field asserts frozenness without naming the baseline. TFW-52 already invented `✅ HL_APPROVED` unaided and it changed nothing measurable |
| D7 Phase HL | A — inherit the master freeze | D2 Granularity | any | Inheritance without a template means the phase HL inherits *a rule* but not *a shape*; TFW-48's phase HL would still have authored 10 DoD and 9 DoF, now nominally frozen. Freezing an unapproved contract makes it harder to fix, not safer |
| D7 Phase HL | D — its own approval gate | *(principle 4)* | batch, don't interrupt | Doubles owner approval events per multi-phase task. The interruption budget is the resource the task exists to protect |
| D4 Classify | D — mechanical rule table as the classifier | *(knowledge)* | `process.md` F22 — generic guidance matrices can be tautological overhead | A table cannot enumerate the declarative/specification boundary exhaustively. It survives only as a short test *inside* judgement (E3's DoD tripwire), not as a replacement for it |

**Surviving configurations:**

| Config | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | Notes |
|--------|----|----|----|----|----|----|----|----|-------|
| **C4** | A all six | B declarative claims | C +baseline ref | C two-key | B per iteration | C restrictive-logged | C derivation-only | B redefine (a) | Lowest escalation among configurations that keep the full frozen set; needs no amendment to ship (E2) |
| **C3** | A all six | B declarative claims | C +baseline ref | A researcher | B per iteration | A symmetric | C derivation-only | B redefine (a) | C4 minus the asymmetry and the second key. Simpler; ~2.5 vs ~2.3 proposals per escalating iteration |
| **C13** | A all six | B declarative claims | C +baseline ref | A researcher | B per iteration | C restrictive-logged | **B abolished** | B redefine (a) | C4 with the Phase HL removed rather than constrained |
| **C5** | A all six | C numbered items | C +baseline ref | A researcher | B per iteration | C restrictive-logged | C derivation-only | B redefine (a) | Survives consistency but at ~3.1 proposals/iteration; the least defensible survivor |

**Unexpected survivors:**

- **C13 (abolish the Phase HL entirely).** Non-obvious because `conventions.md` §15 explicitly grants
  `resume.md` the right to write one, so the artifact reads as established. It survives on three independent
  facts: TFW-42 and TFW-46 completed multi-phase work without one; TFW-47's constrained form carries zero
  information beyond master §4; TFW-48's unconstrained form is where three approved principles were lost.
  An artifact class that is either empty or dangerous is a candidate for deletion, not for governance.
  It is not recommended over C4 only because removing a permitted output is a larger blast radius than
  constraining it, and because `resume.md` would need its own change — outside TFW-53's declared file set.

- **C4's D6=C (restrictive-logged).** The Briefing framed asymmetry as free-vs-gated. The survivor is
  neither: tightening applies immediately *and* is logged with verdict `APPLIED — restrictive`. It keeps the
  volume reduction of Alt B while removing the incentive to mislabel, because the label is visible in §12
  and costs nothing to check.

---

## Findings

### C1 — The strongest attack on this iteration is on its own corpus, and it survives partially

**The attack.** The 213 rows were produced under D19 ("HL update = mandatory output of RESEARCH") and
`plan.md` Step 6c ("update HL with research findings"). The table exists because the template demands it.
Under a freeze, researchers would produce different findings — the 76% is an artefact of the regime being
measured, and using it to design the regime is circular.

**What holds.** The attack explains why *rows exist*; it does not explain *where they point*. D19 incentivises
producing recommendations, not producing frozen-targeting ones. A researcher filling a mandatory table with
low-cost content would gravitate to the cheapest rows — hypothesis statuses and risk probabilities, which are
free sections — yet those are 24% of the corpus, not 76%. Also, one iteration (TFW-46 iter2) shipped with no
table at all and no consequence, and TFW-52 iter1 opened its table with an unprompted non-authority
disclaimer — both show the table is not compulsively filled.

**What does not hold.** `plan.md` Step 6c points research at *scope*, and §3/§4 is where scope lives. Some of
the §3/§4 concentration is endogenous to the instruction. So the *direction* of H1's refutation is robust —
the frozen set is not a minority target under any reading — while the **76% figure should be treated as an
upper bound**, and the modelled C3/C4 figures inherit that caveat.

**What would settle it.** Nothing available in artifacts. The unknowable quantity is how many of the 162 rows
the owner would have *rejected* had they been asked. Recorded as a limit, not papered over.

### C2 — "Declarative claim" is the weakest joint in the surviving design

C3/C4 rest on a boundary an agent must apply: phase *set and declared outcome* are frozen, deliverable
*lists* are free. Three failure modes, with what actually contains each:

| Failure | Mechanism | Containment | Residual |
|---|---|---|---|
| Under-classification — an agent calls a goal change a deliverable refinement to avoid escalation | The classifier's incentive runs one way | E3's DoD tripwire: if the change needs a §5/§6 edit, it is an amendment. Mechanical, checkable against two tables, validated 5/5 on the corpus | An agent can avoid the tripwire by *not proposing* the DoD change and letting the deliverable ship unaccepted |
| Boundary genuinely unclear — "replace Phase C's architecture" is both | Real ambiguity, not bad faith | D4 Alt C two-key: researcher classifies, coordinator verifies. Disagreement defaults to escalation | Costs one classification review per iteration |
| Salami — twelve free deliverable refinements that sum to a new phase | Each row is individually defensible; this is HL §11 S3 exactly | §12 is append-only, so the refinements are *not* logged — only amendments are. **Nothing counts the free changes** | Real and unaddressed |

The salami residual is the honest weak point of the recommended design and it is not solvable by more
classification rules. Two candidate containments, both cheap, neither validated here:
(a) the pre-TS gate compares the phase's current deliverable list against the frozen baseline commit and
reports the delta — one `git diff` against the freeze tag, no new artifact; (b) `conventions.md` §14 gains
"deliverable list grew past its DoD coverage" as an anti-pattern. Carried to RES as an open thread rather
than asserted as solved.

### C3 — The first residual is a real hole: a deliverable with no acceptance criterion

The DoD tripwire assumes the researcher proposes the DoD change. An agent optimising for "no escalation"
simply does not. The deliverable then enters the TS with no DoD to anchor its acceptance criterion.

This is partially self-detecting: TS §5 acceptance criteria derive from the DoD, so an unaccepted deliverable
produces an AC with nothing above it — visible to the reviewer as a coverage gap. But nothing currently
*checks* for it, and D49's Principles Check is a mapping check, not a coverage check.

Honest verdict: the tripwire is a good default and an incomplete gate. It should ship with the §14
anti-pattern that names the evasion explicitly — per F4, structural enforcement beats exhortation, but where
no structural site exists, naming the anti-pattern is the cheapest available thing and TFW's §14 is the
established home for it.

### C4 — The protocol has no path for an owner-initiated change, and that is where S6 comes back

Every artifact in this task describes one direction: research proposes → owner rules. Neither HL §3, §5, §7
nor the §12 grammar covers the owner deciding, mid-task, to change a frozen section themselves.

Left unspecified, the coordinator will do the natural thing: apply the owner's remark directly, because the
owner is the approving authority. That is **TFW-49's S6 failure with the polarity reversed** — there, a
mid-research *user remark* was promoted into master-HL authority with no verdict, no log and no evidence.
DoD-6 closes the case where the remark is treated as approval of a *research* proposal. It does not close the
case where the remark *is* the proposal.

The fix is one clause and costs nothing: an owner-initiated change is an amendment too. It lands in §12 with
the owner as proposer and verdict `✅ APPROVED` on the same row. The log's value is not the gate — it is the
record. A §12 that omits the owner's own changes cannot answer the question §12 exists to answer:
*"which goals were approved and when did each of them change?"*

This also protects the owner from themselves in the exact way HL §1 promises: six months later the table
shows every pressure the task came under, including their own.

### C5 — Volume converts a gate into a rubber stamp: the external prior applies to C1, not to C4

G8's field evidence is causal, not decorative: *"If the board owns execution, it will either drown or start
rubber-stamping changes to clear the queue"*, and *"the board approves everything because declining a change
request requires a rationale that nobody wrote down."*

Applied here:
- **C1 at 4.6 proposals per iteration, ~9 per two-iteration task**, is squarely in the drown-or-stamp band.
  The design would not fail loudly — it would produce a §12 full of ✅ APPROVED rows, which is
  indistinguishable in the artifact from a healthy contract and is *worse than today*, because the drift
  would now carry a paper trail asserting it was authorised. This is the sharpest argument against C1 and
  it is not in HL §9's risk register.
- **C4 at ~2.3 per escalating iteration, on ~two thirds of iterations**, is inside the band where the second
  quote's remedy applies: the proposer carries the rationale burden (evidence + cost + alternative), so
  declining is cheap. HL Principle 5 already states this; the external evidence upgrades it from a stylistic
  preference to the mechanism that keeps the gate alive.

Counter-consideration for honesty: no source gives a numeric threshold, and none exists. The claim is
directional — fewer, better-evidenced proposals keep a gate live; many thin ones kill it — not calibrated.

### C6 — DoF-1 is reachable through a single unedited comment

`templates/RES.md:32` reads `<!-- List what should change in HL based on research. Coordinator applies
these. -->`. Phase A deliverable 2 changes the section's *table structure*. A conscientious executor can
deliver Refinements/Amendment Proposals columns and leave the comment in place — at which point one file
simultaneously instructs the researcher to classify and instructs the coordinator to apply everything.

That is DoF-1 ("a rule with no enforcement site") reproduced inside the enforcement site itself. It costs one
line to prevent and it will not be caught by any DoD item as currently written, because no DoD item mentions
the comment. Flagged for the Phase A TS, where it is an acceptance criterion, not an amendment.

### C7 — Edge cases

| Case | Behaviour under C4 | Status |
|---|---|---|
| Task with no research (`HL_DRAFT → TS_DRAFT` skip) | Freeze applies at approval; no research means no proposals. The freeze still binds the coordinator writing the TS | Fine |
| Single-phase task | Identical; §4 has one phase, its outcome is frozen, its deliverables are free-with-tripwire | Fine |
| Typo or broken link in a frozen section | Formally an amendment. ADR practice explicitly carves this out ("no content changes beyond typos or broken links") | **Gap** — needs a one-line non-substantive carve-out, or agents will either file absurd proposals or learn to edit frozen text quietly. The second is worse |
| Amendment approved → text applied | Requires a re-freeze commit (E7 step 5), otherwise the second baseline is unverifiable | **Gap** — unspecified in HL §4/§5 |
| Amendment rejected | Row stays in §12 with ❌ REJECTED; work continues under the original contract. Covered by DoD-11 | Fine |
| Task rejected (`❌ REJECT`) then re-entered at `HL_DRAFT` | Under D20's implicit approval, re-entering the status silently thaws the frozen sections. REJECT becomes the universal bypass | **Gap** — G6; needs branch (a) redefined as *file an amendment*, and an explicit statement that re-entry does not thaw |
| Phase HL under C4's derivation-only rule | May restate master content and add execution context; may not carry its own §1/§5/§6/§7 | Fine — and it composes with the free-granularity rule without a special case |
| Project adopting TFW mid-task, HL already written and never committed | No baseline exists. Freeze can only take effect at the next commit | Acceptable; worth one sentence so agents do not fabricate a retroactive baseline |

### C8 — What would falsify the recommended design

Stated in advance so the next iteration and the phases can check it rather than argue it:

1. **Escalation count.** If TFW-53's own Phase A→E research and planning produces more than ~3 amendment
   proposals per iteration under C4's rules, the granularity definition is too tight and E1's projection was
   wrong. This iteration is itself the first data point — and it produces **5** (see RES), which is above the
   modelled 2.3. The design-heavy first iteration of the task that invents the mechanism is the expected
   worst case, but a second iteration above 3 would be a genuine signal.
2. **Classification disagreement.** If the coordinator's two-key verification overturns the researcher's
   classification more than occasionally, the boundary is not expressible and D2 Alt C (item-level) becomes
   the better trade despite its higher volume.
3. **Salami.** If a phase's deliverable list at TS time differs materially from its frozen baseline with no
   §12 row, C2's residual is real in production and needs the `git diff` gate.
4. **Rubber stamp.** If §12 across the next several tasks shows ✅ APPROVED on essentially every row, the
   gate is decorative regardless of volume.

---

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Every reduction of the frozen set is refuted by a specific TFW-49 event; D1 Alt A survives on evidence, not on deference to the owner's approval | — |
| C4 recommended; C3 simpler fallback; C13 (abolish Phase HL) an unexpected survivor; C5 survives but is dominated | Owner's preference between constraining and abolishing the Phase HL |
| G1's 76% is an upper bound — `plan.md` Step 6c points research at scope, so §3/§4 concentration is partly endogenous | Unknowable from artifacts; recorded as the limit of the estimate |
| Salami accumulation of free deliverable refinements is unlogged and unaddressed by any classification rule | Two candidate containments proposed, neither validated — open thread |
| **No owner-initiated amendment path exists** — S6's failure with the polarity reversed | Fix is one clause; carried as an amendment proposal |
| Volume converts a gate into a rubber stamp — C1 at 4.6/iteration lands in that band and would produce authorised drift | — |
| Non-substantive edits (typos, broken links) have no carve-out; ADR practice has one | Carried to RES |
| Re-freeze after an approved amendment, and REJECT-re-entry thawing, are both unspecified | Carried as amendment proposals |
| `templates/RES.md:32` can survive Phase A intact and reproduce DoF-1 inside the enforcement site | Phase A TS acceptance criterion, not an amendment |

**Sufficiency:**
- [x] External source used? — the CCB volume→rubber-stamp mechanism applied quantitatively to C1 vs C4; ADR's typo carve-out imported as a gap finding
- [x] Briefing gap closed? — freeze asymmetry resolved (restrictive-logged), REJECT composition resolved (redefine branch (a) + no-thaw clause)
- [x] Pairwise incompatibility checked? Surviving configurations listed? — 11 incompatible pairs, 4 survivors, 2 unexpected
- [x] *(deep)* Hypothesis tested? — H1's corpus attacked on its own selection effect and partially conceded; H3's mechanism attacked on duplication and self-reference; H6's remedy attacked on inheritance
- [x] *(deep)* Counter-evidence sought? — C1 is a deliberate attack on this iteration's central number; C2/C3 attack the recommended design's weakest joint; C8 states falsification conditions in advance

**Metacognitive check.** Genuinely new here, not carried from Extract: C4 (the missing owner-initiated path —
the protocol is asymmetric in a way nobody noticed because every artifact was written from the researcher's
seat), C5's causal reading of the external evidence (volume kills gates, so C1 fails *quietly* by producing
authorised drift), and C2's salami residual, which no classification rule can close and which is the same
mechanism as HL §11 S3. Conceded rather than defended: the 76% is an upper bound. Sources not consulted and
deliberately deferred: TFW-48/49 phase REVIEW files and AFD — both belong to iteration 2.

Stage complete: YES
→ User decision: autonomous run — advancing to Synthesis per owner instruction.
