# RF — TFW-53 / Phase C: Goal Defence in Review

> **Date**: 2026-08-13
> **Author**: Executor (Claude Code)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-53](../HL-TFW-53__hl_contract_and_goal_defence.md) — 🔒 FROZEN, baseline `e8ee76e`
> **TS**: [TS Phase C](TS__phase-c__goal_defence_in_review.md) — amended after ONB
> **ONB**: [ONB Phase C](ONB__phase-c__goal_defence_in_review.md) — 3 blocking questions, all answered `(a)`; the answers added `review.md`:85 to scope, the deferral-confession test to AC-2, the north-star ruling to AC-6/AC-7, and **AC-12** for the uncovered frozen DoD-23
> **Evidence**: [EV Phase C](evidence/EV__phase-c__goal_defence_in_review.md) — 13/14 VERIFIED, 1 DEFERRED, 0 BLOCKED, 0 N/A
> **Second pass**: 2026-08-13, after [REVIEW Phase C](REVIEW__phase-c__goal_defence_in_review.md) 🔄 REVISE
> on discrepancy D1 — replay row 49/A rested on a quotation of TFW-49 §1 that ended one clause early. Verified
> against `9e19a4f` before accepting, then corrected across all eight dependent sites (AC-13), the shipped
> precedent blockquote in `judge.md` replaced with the outcome's **bar** and a plain statement that no
> instance has been observed (AC-14), and RF §8 S2 rewritten (AC-15). The mechanism is unchanged and the
> corpus was not re-run. Every correction is marked **as a correction**, with its cause named.

---

## 1. What Was Done

### New Files

| File | Description |
|------|------------|
| `phase-c/evidence/EV__phase-c__goal_defence_in_review.md` | Environment, 13 evidence rows, verdict, the `review.md` word ledger as Exhibit A |
| `phase-c/evidence/purpose_check_replay.md` | AC-11 — the Purpose Check as shipped, replayed against nine reviews with every citation-and-harm field filled |

**Zero new framework files.** A project upgrading to this version gains no artifact it must create.

### Modified Files

| File | Changes |
|------|---------|
| `.tfw/templates/review/judge.md` | Row 2 clause (a) — mapping integrity → **Purpose Check**, carrying its rate and its consequence-not-frequency reason. New **Purpose Check** block below the table: reference set, the two invalid references with their reasons, the fused citation-and-harm field, three tests (excess-and-adjacency, deferral confession, materiality), the override clause, and a three-outcome table with routing. One Checkpoint item. **Second pass:** the closing blockquote no longer offers TFW-49 as an example of contradicting clauses — it states the **bar** for the outcome (read each clause to the end of its sentence; surface tension is not inconsistency; coherent-but-wrong is the purpose question) and that **no instance has been observed**. Paid for inside the same block: **1,167 → 1,165 words, no net growth** |
| `.tfw/workflows/review.md` | Line 28 → *"Master HL at its frozen baseline"* with the rule-15 pointer; Reviewer Identity gains goals/values/north star and block authority (and `not rubber stamp`, recorded in D46 and never shipped); Step 3's `HL §7 Principles check` paragraph **replaced** by the Purpose Check instruction; Step 4 gains a **Routing** block. **1,065 → 1,176 words.** `+8 / −4` |
| `.tfw/templates/REVIEW.md` | §3 row 2 realigned to `judge.md`; the `not fit for purpose` finding surfaced inside the existing `### If REJECT` block — no new section. `+6 / −1` |
| `.tfw/glossary.md` | PV Index gains **priority 0 — Project North Star**; priority 1 relabelled `.tfw/README.md § Values and Principles — methodology values` with the byte-identical reason recorded; one note that priorities 0 and 1 may name the same file. `+6 / −1` |
| `.tfw/conventions.md` | §3 gains **Project North Star** — seven rules: locus, no nominated task HL, payload with mandatory non-goals, admission criteria, fallback chain, the same-file rule, citation namespace. §14 gains the two review-side anti-patterns. `+27 / −0`, **additions only** |
| `.tfw/templates/HL.md` | A north-star header field **below** the contract block, taking a list of locations, with the fallback and explicit `N/A`. `+7 / −0`, contract block untouched |
| `.tfw/compilable_contract.md` | §2 pattern table only: `P{N}` corrected from the `KNOWLEDGE.md` §0 that D37 removed to **HL §7 Principles row (task-local)**; `PP{N}` and `NS{N}` added. `+3 / −1` |

**Budget:** 2 new, 7 modified, **99 insertions / 8 deletions**. Limits 30 files · 15 new · 3,000 LOC · 30 modified — inside every axis.

`README.md` Task Board row: status and the ONB link were committed with the ONB (`2370082`); the RF column is updated in the working tree — see §2 decision 8.

**Row 2, before and after** (AC-1's evidence, both clauses quoted in full):

```
BEFORE
| 2 | Philosophy aligned — two clauses, both answered. **(a) Mapping integrity:** does every TS §3
      Principles Check row resolve to an AC that was actually met? **(b) Design soundness** _(4.5%)_:
      is the design itself sound against those principles — not "is it named well", which is row 4 |

AFTER
| 2 | Two clauses, both answered. **(a) Purpose Check** — *is this what we set out to do?* Answered
      against the reference set below, never against the TS _(~4 blocks in 149 reviews, a different
      corpus; kept on consequence rather than frequency — the miss it exists to catch cost six days of
      work rejected wholesale)_. **(b) Design soundness** _(4.5%)_: is the design itself sound against
      HL §7 principles — not "is it named well", which is row 4 |
```

## 2. Key Decisions

1. **The check is a row plus a block, and the block is where the enforcement lives.** Row 2(a) is one
   quotable sentence; the reference set, the fused field, the three tests, the override clause and the
   three outcomes sit below the table. Two reasons, both from the TS: the row must stay quotable for
   clause (b) to remain separately answerable (AC-1), and `judge.md` is a template — the whole mechanism
   costs `review.md`'s attention budget nothing. TS §8 named *"row 2 grows into a paragraph"* as a risk;
   the block is how it was avoided rather than accepted.

2. **Clause (b) is not byte-identical, and the three words are load-bearing.** It read *"sound against
   **those** principles"* — where *those* referred to the TS §3 Principles Check rows named in clause (a).
   Deleting clause (a) leaves the pronoun pointing at nothing, so the referent was made explicit:
   *"against **HL §7** principles"*. Meaning unchanged, separateness unchanged, rate unchanged. **A
   reviewer running AC-1's `diff` gate will see a diff**, which is why it is stated here, in EV E1 and in
   §3 rather than left to be discovered. The alternative — shipping a dangling *those* — is the
   stale-pointer defect this task has now found four times.

3. **The third outcome is a finding, not a fourth symbol.** AC-12 asks for an outcome *distinct from pass
   and fail*; the temptation is a new status glyph in the Status column. That would collide twice — with
   TFW-56's fixed `✅/❌/⚪` vocabulary, and with Phase E's forthcoming `❌ REJECTED` **status**, which is
   the two-new-`❌`-tokens-in-one-release confusion that research D18 rejected for the verdict set. So the
   status stays `❌` and the *finding* carries the distinction: `not fit for purpose` (work defect → owner)
   versus **contract defect** (reference set inconsistent → owner). Same move A2 made for §12's `Type`
   column: the classification is visible at ruling time instead of reconstructed from prose.

4. **`P16` is not cited inside the shipped template, deliberately.** The natural wording for the
   invalid-reference rule is *"the TS is downstream of any drift (P16)"* — and `P{n}` is **task-local**
   (`knowledge/constraint.md` F4, and it is the very defect AC-9 corrects three files away). A shipped
   template citing `P16` would resolve, in every project, to that project's sixteenth HL principle. The
   reason is written out in words instead. The task fixing a namespace collision must not commit one.

5. **`not rubber stamp` was restored to the Reviewer Identity.** D46 recorded the identity as *"Quality
   guardian, **not rubber stamp**"* and only the first half ever shipped — the word `rubber` appeared zero
   times in `.tfw/`, and HL §2 records this as the second, older instance of the retention pattern. AC-4
   authorises the identity block; two words close a four-month-old documented loss. It is not load-bearing
   and is not claimed to be: every property it names is separately enforced in `judge.md`.

6. **Replay row 49/A was wrong on the first pass, and the cause was a quotation ended early.** _(Corrected
   on the second pass, AC-13. The first version of this decision argued the opposite.)_ I ruled TFW-49
   Phase A a **contract defect** — the third outcome — because approved §1 promised *"readable without
   special tooling"* while approved DoD-3 required a versioned structural validator. The sentence does not
   end where I ended it: *"…readable without special tooling, **while structural validation prevents quiet
   drift** between Coordinator, Researcher, Executor, Reviewer, adapters, and repositories."* §1 asks for
   both properties in one breath, DoD-3 discharges the second, and DoF-8 — which forbids enforcement
   resting *only* on prose or *only* on unversioned `.git/` state — is satisfied by any versioned check.
   Re-scored to **`✅ aligned`**, which is where research iteration 2 put it. So the two runs now agree on
   all nine rows, and the claim that they diverged was an artifact of the same truncation.

   **What the corrected row is worth is more than what the wrong one claimed.** 49/A is aligned with its
   approved contract and the owner rejected the product anyway — part of the rejected scope was a faithful
   reading of the DoD the owner approved. The check judges against the baseline, so a contract that is
   internally *coherent* but wrong for the product returns `aligned` and this row cannot help. That is not
   a defect in the check; it is exactly the case HL §4 says the **north star** exists for — *"the only
   defence against a task whose own approved HL is wrong for the product"*. The replay now supplies the
   evidence for the HL's own deliverable weighting: the reference-set rule catches four of the six, and
   only an anchor above the task HL could have caught the fifth. Priority 0 stopped being insurance.

   **How the error got in, since that is the reusable part.** The truncation originated in research
   iteration 2 and propagated into the HL and into my replay unexamined, because the quotation *resolved* —
   it was verbatim as far as it went, and it pointed at a real clause in a real commit. The phase whose
   thesis is *alignment must be cited, not asserted* shipped an illustration built on a citation that
   resolved and misled. TD-166 is the structural half of this: `verify.md` checks that citations resolve,
   and nothing checks that they are relevant.

7. **The near-miss on TFW-42/A is written up, not smoothed.** ONB §5 risk 1 predicted a false positive
   would surface there first, and something did: the five-row agent-selection guidance table the owner
   later removed as tautological. It fails the materiality bar and produces no block — which is the
   design working, so the row records what the check noticed and what stopped it. AC-11 forbids tuning the
   corpus; it does not forbid reporting a near-miss, and a replay that showed nothing at all on the sound
   half would be weaker evidence that the bar does anything.

8. **`README.md` was left uncommitted, on the coordinator's instruction.** The concurrent TFW-55 session
   still holds an uncommitted Task Board row. The ONB row was committed earlier by staging only my own
   hunk after inspecting the diff; for this RF the coordinator's ONB ruling is explicit — *"leave the
   board row uncommitted and say so in the RF — I will land it. Do not stage a hunk you did not write."*
   The working tree carries the phase-c RF link; the commit does not.

9. **Two files this phase touched are the same files TFW-56 shipped four hours before it.** Every edit
   was made against the shipped state, not the pre-TFW-56 state: ten rows not seven, Judge at Step 3 not
   Step 4, rows 8-10's rate-inside-the-row grammar copied for the Purpose Check, and `verify.md`'s new
   Claim & Source Checks section left untouched.

## 3. Acceptance Criteria

> Per TD-142 V2: `AC │ gate │ result`, not a restatement of the TS.

| AC | Gate (from TS) | Result |
|----|----------------|--------|
| AC-1 | `grep -rc "mapping integrity"` → 0 in both files; row count = 10; clause (b) diffs clean | ✅ **Met, with one disclosed divergence.** 0 and 0; ten rows; the Purpose Check is clause (a), not row 11. Clause (b) keeps its 4.5%, its separate answer and its meaning — **three words changed** to repair the antecedent the deletion orphaned (decision 2). The row carries the rate *and* the consequence reason, and names no project (F13) |
| AC-2 | Fill the row against RF Phase B once; show a bare citation being rejected | ✅ All five properties present as failing conditions. Dry-run and failing variant: `purpose_check_replay.md` §5 |
| AC-3 | Read the block; confirm no second copy of the recovery command in `.tfw/` | ⚠️ **Substantively met; the gate has a pre-existing counterexample.** All four bullets hold — reference set, both invalid references with reasons, fallback chain, and a *pointer* to rule 15 with no command restated. But `templates/HL.md`:10 already carries the recovery form inside the contract header block, and **AC-7's gate forbids this phase to modify that block**. Nothing new was created here. §6 obs. 1 |
| AC-4 | `grep -n "frozen baseline\|not fit for purpose"`; verdict set unchanged | ✅ Lines 28, 87, 102. Step 3's paragraph replaced, not deleted; identity names the third defended object with block authority; `not fit for purpose` routes to the owner; `APPROVE / REVISE / REJECT` unchanged, no fourth token in the file |
| AC-5 | `wc -w` before and after | ✅ **Met at the hard threshold, reported not resolved.** 1,065 → **1,176**, 24 words under 1,200; not in 700-900. **Zero removals to buy headroom** — the ledger's removal column is empty by construction (EV Exhibit A) |
| AC-6 | Read the index; priorities 1-7 keep their content, only labels move | ✅ Priority 0 added; priority 1 relabelled with its reason; rows 2-7 byte-identical; "Who scans PV" resolves. `conventions.md` §3 carries all four ruled properties — single locus, no nominated task HL, multiple locations, and the priority-0/1 same-file rule without which this repository could never conform to its own rule |
| AC-7 | Read the header; contract block not modified | ✅ One additive hunk entirely below the contract block, zero deletions. The field takes a list, states the fallback, and renders `N/A` rather than being absent |
| AC-8 | Diff `REVIEW.md` §3 against `judge.md` row by row | ✅ Ten rows, same order, row 2 realigned. The finding is surfaced in §4 inside the existing `### If REJECT` subsection — no new section (F22) |
| AC-9 | `grep -n "P{N}\|NS{N}\|PP{N}"` | ✅ Three rows at 59-61; `+3 / −1`, nothing else in the file touched. **`PP{N}` is declared and unused here** — this repository has no `KNOWLEDGE.md` §0 and none was invented |
| AC-10 | `git diff` shows additions only | ✅ **`27 0`** — twenty-seven insertions, zero deletions. Phase A's §3 rules and TFW-56's §14 entry untouched |
| AC-11 | `purpose_check_replay.md` — one row per review, outcome, citation, harm | ✅ **4 of 6 non-approve on the rejected corpus, 0 of 3 on the sound corpus** — `≥1` holds. Was 5 of 6 before the second pass re-scored 49/A (decision 6). Discrimination in both directions: 48/B is a sound phase inside a rejected task, and TFW-42/A's near-miss shows the materiality bar doing work. Three divergences recorded per review, never averaged |
| AC-12 | Read the block; routing target is the owner; reachable without leaving `judge.md` | ✅ **The gate passes; the branch is unexercised, and that is now stated everywhere it matters.** Third outcome in the outcome table with both routing targets, the bar for reaching it, and the plain statement that no instance has been observed. The TS's Evidence field expected AC-11 to supply one — after the 49/A correction the corpus supplies none, recorded as **EV E14 `DEFERRED`** with the blocker named rather than left in prose |

**Second pass — AC-13 to AC-15:**

| AC | Gate (from TS) | Result |
|----|----------------|--------|
| AC-13 | Read §1 whole and DoF-8 at `9e19a4f`, then diff every dependent site | ✅ The row quotes §1 to the end of its sentence, states that §1 pairs readability with structural validation, and returns **`✅ aligned`** — not the third outcome, not a fire, since the excess argument was tested against DoD-3 and DoD-7 and rejected. Outside confirmation **dropped**: TFW-50 ran under a different HL with no DoF-8, so it evidences a change of owner preference between two contracts, not an inconsistency inside one. **All eight sites propagated:** replay §0 (correction of record with the cause named), §1 row 49/A, §3 diagram, §3 AC-11 table, §4 reconciliation · EV E11, E12, new E14 · RF §2 decision 6, §3 AC-11 and AC-12, §5, §8 S2, §9 both affected diagrams |
| AC-14 | Read the block; `wc -w` before and after | ✅ The blockquote states the **bar** — satisfying one clause must *necessarily* violate the other; read each to the end of its sentence; surface tension is not inconsistency; coherent-but-wrong is the purpose question — and then that **no instance has been observed**. No substitute example was hunted for (DoF: *"a weak contract-defect example is substituted … rather than admitting the corpus has none"*). The surviving true half of the old line was **not** repurposed: *"part of the scope the owner rejected was a faithful reading of the approved DoD"* now lives in the replay's 49/A row as a **purpose** finding, not a contract-defect one. **1,167 → 1,165 words**, paid inside the same block; `review.md` untouched at 1,176 |
| AC-15 | Re-read both sources; confirm every remaining quotation is verbatim to its full sentence | ✅ S2 rewritten to what survives — the replay is the check's regression suite, its second run **confirmed** research's original verdict, and the reusable half is that a truncated citation passed three artifacts because it *resolved*. **New S4** records why stating "not observed" beats shipping a weak example. On the 48/A quotation: **the quotation was verbatim** — *"preserves all ten mapped principles"* is `REVIEW__phase-a__method_kernel.md`:51, and the sentence REVIEW Phase C cited instead, *"Phase HL P1–P10 all pass through their mapped ACs"*, is line 38 of the same file. Both now appear with their line numbers, which is the improvement that was actually available; §6 obs. 7 records the finding |

**Definition of Failure — all sixteen clear**, including the three added for this pass: the mechanism, the
corpus and the twelve passing ACs were not reopened · no substitute example was shipped for the withdrawn
one · `judge.md` did not grow, and every corrected quotation names why it was wrong.

**Original thirteen — all clear.** Clause (b) present, separately answered, rate intact · the
Purpose Check is clause 2(a), not row 11 · citation and harm are one field, and a bare citation is shown
being rejected · the materiality bar is a failing condition and demonstrably stopped a wording objection
(TFW-42/A) · TS and Phase HL are named invalid in both files · the mapping-integrity check survives in
neither `judge.md` nor `review.md` Step 3 · the third outcome routes to the owner · no project name in any
shipped template · no new verdict token, no fifth stage · 1,176 < 1,200 with no mechanism trimmed · the
replay ran, on the required corpus, and not on TFW-53's own reviews · no adapter copy, glossary article or
repository north star written · no vendor mechanism named.

## 4. Verification

- **Lint** (`build.lint`): unconfigured starter placeholder (TD-134) — substituted by the docs pipeline
  below, per the precedent set in Phase A and reused in Phase B and TFW-56.
- **Tests** (`python -m pytest docs/scripts/ -q`): **68 passed** in 42.31s. Run before the RF was written,
  per the Step 10 build gate.
- **Verify** (`python -m mkdocs build -f docs/mkdocs.yml`): **built in 30.74s**. All seven changed files
  are Source Manifest rows 4, 5, 12, 13 and 14, so this build is their only consumer.
- **Warning attribution**: **0** warnings name any of the seven changed files as source; **0** name this
  phase's artifacts. Repo-wide 455 is the pre-existing baseline — up from Phase B's 401 because concurrent
  sessions added artifacts, 16 of the new ones sourced to `tasks/TFW-55*`. I claim only that none is
  attributable here.
- **AC gates** reproduced with their commands and outputs in EV E1-E14.

## 5. Evidence

See [EV file](evidence/EV__phase-c__goal_defence_in_review.md) for evidence details.

Evidence verdict: **13/14 VERIFIED, 1 DEFERRED, 0 BLOCKED, 0 N/A**

Three rows carry a disclosed divergence rather than a clean pass — E1 (clause (b) is not byte-identical),
E3 (the recovery-form gate has a pre-existing counterexample this phase may not clear) and **E14**, the
row added on the second pass: the third outcome ships specified and **unexercised**, because after the
49/A correction the corpus contains no genuinely self-contradictory contract. E14 is `DEFERRED` with its
blocker named, on the Phase B precedent for an unexercised branch — a status a reviewer can audit rather
than a sentence they have to notice.

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/templates/HL.md` | 10 | duplication | **The recovery command has a fourth copy, in the template every future HL is written from.** Amendment A13 removed the command form from `HL-TFW-53` at all three occurrences and pointed at `conventions.md` §3 rule 15 — but it was applied to the *artifact*, not to the *template*. So every new HL is still born carrying a command form that rule 15 exists to own in one place. AC-7's gate (*"confirm the contract block is not modified"*) forbids this phase to touch it, and AC-3's gate cannot pass while it stands → whoever owns `templates/HL.md` next |
| 2 | `.tfw/compilable_contract.md` | 65 | todo | **A second stale `KNOWLEDGE.md` §0 reference, six lines below the one AC-9 corrects.** *"Where references appear"* still opens with *"`KNOWLEDGE.md` §0 Source column"* — the section D37 removed in April. AC-9's *"one table, nothing else in that file"* is a deliberate boundary (coordinator, ONB §6.3), so it stays. → Phase D with TD-155 |
| 3 | `.tfw/compilable_contract.md` | 81 | todo | The **Resolution rules** list reads `D{N}, P{N}, F{N}, TD-{N} → anchor links` and does not mention the two patterns this phase declared. `NS{N}` and `PP{N}` are therefore declared in the pattern table with no stated resolution behaviour. Same one-table boundary; same destination |
| 4 | `.tfw/workflows/review.md` | 85-88 | naming | Step 3 is now titled **Judge** and contains a *Purpose Check* instruction whose mechanism lives in `judge.md`. Correct and deliberate, but the step now has two named things a reader must hold apart, and the next person to compress this workflow will be tempted to merge them |
| 5 | `.tfw/templates/review/verify.md` | Knowledge Citations Verified | missing-test | The reviewer verifies that citation **links resolve** — the anti-hallucination gate (D43). The Purpose Check now demands a citation that is *relevant*, and nothing verifies relevance. SS2 named this exact shape: *a citation that resolves is not a citation that is relevant*. The fused harm field is the guard inside Judge; Verify has no counterpart |
| 6 | `knowledge/process.md` · `KNOWLEDGE.md` §1 D46 | F19 · D46 | todo | D46's row still records the Reviewer Identity as *"Quality guardian, not rubber stamp"* with no note that only half shipped for four months. Now that the other half is shipped, the row is accidentally correct again — but the retention finding (HL §2, iter2 G7) is not recorded anywhere durable. → `/tfw-knowledge` at KNW |
| 7 | `phase-c/REVIEW__phase-c__goal_defence_in_review.md` · `phase-c/TS__…md` | REVIEW item 3 · AC-15 bullet 2 | todo | **The paraphrase-in-quotation-marks finding is itself a mis-citation, and it travelled from the REVIEW into an acceptance criterion.** *"Preserves all ten mapped principles"* is verbatim at `REVIEW__phase-a__method_kernel.md`:**51** (§4 Verdict). The sentence the REVIEW offers as the true source — *"Phase HL P1–P10 all pass through their mapped ACs"* — is line **38** (Judge row 2) of the same file. Two different sentences, both real, both supporting the point. Nothing was repaired because nothing was broken; the quotation now carries both line numbers. Recorded because AC-15 asks for a fix that would have introduced the defect it was written to remove, and because it is the third instance in this phase of a citation checked for resolution rather than for what it actually says (D1, TD-166, this) → coordinator |

## 7. Fact Candidates
> fact-candidates: processed 2026-08-18 (`/tfw-knowledge`, TFW-53 A–E)


| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | philosophy | **This project's north star is its own philosophy, and it lives in two files** — the root `README.md` and the founder essay `.tfw/README.md`. Owner ruling at Phase C ONB. The consequence the framework had to absorb: when the product *is* the methodology, PV priority 0 and priority 1 legitimately point at the same file, and the anchor is a **list** of locations rather than a path. Both properties are now rules; neither was anticipated by the frozen DoD | User, 2026-08-13 (ONB Q2); HL §11 S38 | High |
| 2 | process | **The owner defers a designation whose target is being rewritten, rather than landing a pointer that will be stale by morning.** Ruling on the same question: ship the slot and the grammar now, record the designation in the HL, and let the pointer land with the session that is restructuring the files. Preference revealed: a correct-but-stale pointer is worse than a recorded intention, when a concurrent session owns the target | User, 2026-08-13 (ONB Q2, consequence iii) | High |
| 3 | stakeholder | **A gap in the coordinator's own spec is answered by fixing the spec, not by authorising the executor to proceed around it.** Frozen DoD-23 had no acceptance criterion; the coordinator's answer was *"That is my gap, not yours, and it is now AC-12"*, with the reason stated — an executor implementing an uncovered DoD item is indistinguishable from an executor exceeding scope. The same session also added `review.md`:85 to TS §4 *before* it was touched, and corrected AC-1, AC-6, AC-7 and AC-11 from the ONB's findings | Coordinator, 2026-08-13 (ONB answers) | High |

## 8. Strategic Insights (Execution)

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | **A rule cannot be written for every project unless the project writing it can obey it.** The frozen DoD relabelled PV priority 1 because `.tfw/README.md § Values and Principles` is byte-identical across projects and therefore carries no project information — true in every project except the one that authored the rule, where the methodology *is* the product and that file is a north star. The owner caught it at ONB and the fix is one clause: priorities 0 and 1 are distinguished by *what the section says*, never by which file holds it. **Implication, and it generalises past this row:** a framework that is also a project has a systematic blind spot at exactly the clauses where "framework" and "project" are assumed distinct. The self-test is cheap and was not being run — *can this repository satisfy the rule it is shipping?* It would have caught this before the freeze, and it is the same shape as S32's *labels that resolve*: the rule was true, checkable, and false about its author | philosophy | User, 2026-08-13 (ONB Q2); HL §11 S38 |
| S2 | **A replay is the check's regression suite, and its second run disagreed with its first — in favour of the original research.** _(Rewritten on the second pass. The withdrawn version claimed the replay had "found its own predecessor's defect", which rested on the 49/A ruling REVIEW Phase C removed. The premise is gone; what survives is smaller, verified, and points the other way.)_ Row 49/A was re-scored from *contract defect* to `✅ aligned`, which is where research iteration 2 put it before amendment A6 existed — so two independent runs, the second adversarial to the first's design, now agree on all nine rows. **Implication, and it is the reusable half:** the replay is cheap enough to re-run whenever the check changes, and running it twice is what surfaced a truncated citation that had already passed through research, an HL and a first-pass evidence file — three artifacts, each of which had *resolved* the quotation without reading it to the end of its sentence. Worth proposing as a standing obligation for any checklist row that carries a claimed rate, which `conventions.md` §14 now requires of every row. The structural half is TD-166: `verify.md` checks that a citation resolves and nothing checks that it is relevant — and this task's own error is the instance | philosophy | Executor, 2026-08-13; REVIEW TFW-53/C D1; RES iter2 D19; HL §12 A6 |
| S4 | **The corpus contains no self-contradictory contract, and saying so is worth more than an example.** The third outcome (A6) was approved on a structural argument — against a genuinely contradictory reference set the same evidence supports a defensible fire and a defensible pass — and its one supposed instance evaporated on a full reading. The alternatives were to hunt for another candidate or to ship the weak one; both would have taught reviewers that surface tension is unsatisfiability, in the template filled every review, three paragraphs below the rule that a resolving-but-irrelevant citation fails the row. **Implication:** a mechanism whose triggering case has never been observed should ship with that stated in the artifact, not in the task trace. `judge.md` now carries *"no instance has been observed"*, HL §9's risk reads `Unmeasured`, and EV E14 is `DEFERRED` with the blocker named — three places a later reader can find it without reading this RF. The pattern generalises to any gate justified on consequence rather than frequency, which `conventions.md` §14 explicitly permits | philosophy | Coordinator ruling 2026-08-13 (AC-14); REVIEW TFW-53/C item 2 |
| S3 | **Two independent sessions in one working tree have now cost this task twice, and the second time it was avoided by hand, not by a rule.** Phase B swept a sibling's deletions into its own commit (TD-144). This phase committed the ONB by generating the full `README.md` diff, keeping only its own hunk and applying that to the index — a manoeuvre no workflow describes, decided by an executor mid-run. The coordinator then ruled that for the RF the board row should stay uncommitted entirely. **Implication:** the discipline currently lives in two places, neither durable — an executor's judgement and a per-run verbal instruction. This is TFW-54's problem arriving early, as RF Phase B S1 already argued, and the concrete missing artifact is small: a staging rule in `handoff.md` and `review.md` saying stage by explicit path, and what to do when a shared file carries someone else's hunk | risk | Executor + Coordinator, 2026-08-13; RF TFW-53/B S1; TD-144 |

## 9. Diagrams

**What a reviewer reads, before and after.** The reference point is the whole change:

```
                    BEFORE                                      AFTER
                    ──────                                      ─────
  review.md:28    "Master HL for the task"           "Master HL at its FROZEN BASELINE"
                   └─ resolves to the current file    └─ recovered via conventions.md §3 rule 15
                      = whatever it drifted into
                                                      invalid, and named as such:
                                                        ✗ TS        — downstream of any drift
                                                        ✗ Phase HL  — holds nothing approved

  judge.md row 2  (a) MAPPING INTEGRITY               (a) PURPOSE CHECK
                  "did every TS §3 principle          "is this what we set out to do?"
                   resolve to an AC that passed?"      one field: QUOTE the clause
                   └─ scores ✅ on a principle              + NAME the concrete harm
                      violated by the mapping         three tests, each answerable NO:
                      itself                            excess/adjacency · deferral
                  (b) design soundness  4.5%             confession · materiality
                                                       not grounds to ✅: "TS scoped it"
                                                                         "tests are green"
                                                      (b) design soundness  4.5%  ← intact

  outcomes        ✅ / ❌                             ✅ aligned
                                                      ❌ not fit for purpose → OWNER
                                                      ❌ contract defect     → OWNER
                                                         (reference set self-contradictory;
                                                          the executor cannot repair an HL)

  PV Index        1  README Values ─────────────┐    0  PROJECT NORTH STAR  ← what we build,
                  2  philosophy.md              │       why, and what we never build
                  …  all seven: HOW we build    │    1  .tfw/README.md § Values and Principles
                                                │       — methodology values
                  nothing above the task HL ────┘    2-7 unchanged
```

**Three outcomes, and the bar the third one has to clear.** _(Corrected on the second pass: the first
version of this diagram used TFW-49 §1 vs DoD-3 as its example of contradicting clauses. It is not one —
§1 asks for readability **and** structural validation in the same sentence.)_

```
                     reference set = frozen baseline + north star
                                        │
                    ┌───────────────────┴────────────────────┐
                    │                                        │
          clauses can all be satisfied            clauses CANNOT both be satisfied
                    │                             i.e. honouring one NECESSARILY
        quote one + name the harm                 violates the other
                    │                                        │
        ┌───────────┴──────────┐                  the bar, learned the hard way:
        │                      │                  ▸ read each clause to the END
   no harm nameable      harm is material            of its sentence
        │                      │                  ▸ a clause that qualifies itself
        ▼                      ▼                    in its 2nd half is NOT in tension
       ✅                     ❌                     with the clause discharging it
     aligned         not fit for purpose           ▸ surface tension ≠ inconsistency
                          → OWNER                  ▸ coherent but wrong for the product
                                                     = the PURPOSE question, not this one
                                                              │
                                                              ▼
                                                    ❌ contract defect → OWNER
                                                    (not the executor: no channel
                                                     to a frozen section)

  Observed instances in the nine-review corpus: ZERO. The outcome ships on its structural
  argument — against a truly contradictory reference set the same evidence supports both a
  defensible fire and a defensible pass — and judge.md says "no instance has been observed"
  rather than shipping a weak example. EV E14 carries it as DEFERRED with the blocker named.
```

**The replay, and what each half proves.**

```
  REJECTED CORPUS (6)  ─ all shipped ✅ APPROVE, whole result later reverted
    48/A  ██ fires      DoF-12: a new conceptual layer over an existing owner
    48/B  ·· aligned    ← a sound phase inside a rejected task: not a corpus detector
    48/C  ██ fires      DoF-12 again + a partial deferral confession
    49/A  ·· aligned    ← re-scored on the 2nd pass; §1 asks for readability AND
                          structural validation in one sentence. Aligned with a contract
                          the owner still rejected → only a NORTH STAR reaches this case
    49/B  ▓  fires (mod)  DoD-4's "observable consumer" → a 3,160-line router
    49/C  ██ fires      "safely bypass" → a two-hook runtime; DoF-8 hit outright
                        ────────────────────────────────────────────────
                        4 non-approve · 2 aligned

  SOUND CORPUS (3)  ─ work the owner kept and built on
    TFW-50    ✅  "one precise Markdown rule … without enforcement software" — served exactly
    TFW-42/A  ✅  check NOTICED the guidance table → materiality bar stopped it  ← the bar earns its place
    TFW-47/B  ✅  the one deviation moved toward the cited clause, and was disclosed
                        ────────────────────────────────────────────────
                        0 of 3 blocked

  Sharpest result: 49/C and TFW-50 answer the SAME product question — agent commit provenance.
  Both were verified, tested and internally consistent. The check fires on the two-hook runtime
  and stays silent on the one-Markdown-rule solution.

  And the limit, in the same corpus: 49/A is ALIGNED with its approved contract, and the owner
  rejected the product. Nothing in this row could have caught it. That case belongs to the
  north star (PV priority 0), which is why the anchor is a deliverable and not a footnote.
```

---

*RF — TFW-53 / Phase C: Goal Defence in Review | 2026-08-13*
