# Judge — "Is the quality sufficient?"

> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Mode: spec
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | All 12 TS ACs verified against the artifacts, not against the RF — verify.md V1–V3 for the three files, V4–V6 for the evidence set, Commands 2–10 for every gate. HL DoD-1…DoD-11 (Phase A's block) map onto AC-1…AC-12 and all land. Not one AC rests on a claim I could not re-execute |
| 2 | Philosophy aligned | ✅ | See §HL §7 Principles Check below — 9 mapped principles, 9 satisfied, 0 violations |
| 3 | Tech debt documented | ✅ | RF §6 carries 6 typed observations with file and line. Five survive the quality filter (obs. 2 is a live bug, obs. 3 a dead reference namespace, obs. 4 a repo-wide config defect, obs. 5 a forward-looking structural warning, obs. 6 a stale-TS notice). Obs. 1 is a genuine but cosmetic heading-level issue already ruled out of scope in ONB §6.6 |
| 4 | Style & standards | ✅ | `conventions.md` additions are numbered rules and table rows per TS §6 and `knowledge/process.md` F4 — 21 rules, one 3-row table, one 6-line blockquote in §5 (the AC-10 deliverable, which has no numbered form). §14 appended, never renumbered — verified as `+55 / −0`, so DoF-7 could not have fired. Naming matches TS §6's fixed vocabulary exactly: `Contract`, `FROZEN`, `Amendment`, `Amendment Log`, `EXTEND`, `SUPERSEDE`, `RESTRICT`, `Contract Baseline`; the pre-A10 token `APPLIED — restrictive` appears **0** times (Command 4), so Phase D has nothing to reconcile |
| 5 | Observations collected | ✅ | Quality filter applied — see §5 of the REVIEW. Obs. 2 (`gen_docs.py` `_replace_phase` still globbing `Phase{X}/` after D50 renamed folders) is a live resolver bug affecting **every** phase reference in this repository, found by an executor reading build code they were not asked to read |
| 6 | RF completeness (§7-9) | ✅ | §7 three fact candidates, each sourced and dated; §8 three strategic insights, each carrying an explicit **Implication**, which is the cognitive mode conventions.md §3 requires and which most RFs omit; §9 two diagrams — a file-to-AC map and a decision tree that renders the shipped classification rule as executable branching, with the rule number cited on every branch |
| 7 | Evidence completeness | ✅ | All 12 TS `Evidence:` fields are covered in the EV file. The 7 `N/A`s quote the TS verbatim — checked word for word against TS AC-1/3/4/5/7/10/12, so they are the coordinator's design, not executor convenience (this is exactly the `N/A`-challenge the Trust Protocol demands, and it survives). The 5 `VERIFIED` each point at a file or an inline exhibit that I re-executed: both shells for AC-6, `git show 721ca15` for AC-9, the live §12 corpus for AC-2 |

## Mode-Specific Checklist (spec)

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 7 | Analytical quality — logic, completeness, methodology | ✅ | The three ACs that could have been satisfied by assertion were instead run against live artifacts, and **all three changed the deliverable**: AC-6 against live history proved the documented recovery command returns nothing under Git Bash (rules 15's slash-free form exists because of it); AC-2 against 12 live rows exposed a disposition the verdict vocabulary could not name (`🚫 WITHDRAWN`); AC-8's exercise exposed a rule that reaches opposite classifications from the same evidence depending on when it is applied (rule 6's time-scoping). That is methodology producing findings, not methodology decorating conclusions. **Circularity is handled correctly:** `classification_exercise.md` puts the disqualifying limit *before* the 5/5 score and states plainly that agreement measures readability, not correctness — AC-8 asked for the limit to be stated; the executor also declined to let the number carry weight |
| 8 | Source attribution — claims traceable to evidence | ✅ | 29 of 29 knowledge citations resolve; 0 hallucinations (verify.md §Knowledge Citations). Every RF §7 fact candidate is traceable: FC1 to the measured shell transcript, FC2 to the coordinator's ONB rulings (I read the rulings — *"it is a defect in what I wrote"*, *"your mitigation is better than my AC"* — both verbatim), FC3 to HL §12 row A10 whose `Proposer` cell does read `Executor (Phase A ONB Q2)`. RF §8 S2 quotes the ONB §3.1 Assessment verbatim and correctly. Every measurement in RF §4 ships with the command that produced it, and all of them reproduce |

## HL §7 Principles Check

Read from TS §3. For each principle mapped to an AC, the linked AC was verified met in RF §3.

| # | Principle | Mapped AC | AC met? | Verdict |
|---|-----------|-----------|---------|---------|
| P2 | Classify, never edit | AC-3 | ✅ | ✅ — `templates/RES.md` offers two classes, states the researcher never applies, and the `Coordinator applies these` line is gone (Command 2 → 0 matches). The instruction that *caused* TFW-49's drift no longer exists on the template side |
| P3 | Structural enforcement over guidelines | AC-1, AC-2, AC-6 | ✅ ✅ ✅ | ✅ — the contract is a header field, a marker on every heading and a 10-column table, plus a git-recoverable baseline. Nothing here is advisory prose, which is DoF-1's exact failure mode |
| P5 | Evidence, cost, alternative | AC-2 | ✅ | ✅ — all three are mandatory columns; the template restates *"A proposal without evidence, cost and a considered alternative is not a proposal"* |
| P6 | Narrow D19, don't revoke it | AC-3 | ✅ | ✅ — RES still produces HL feedback; only the frozen channel turns from write to propose. DoF-8 not hit |
| P7 | Token density | AC-8 | ✅ | ✅ with a flag — additions are numbered rules and table rows, no prose blocks in §3. But `conventions.md` grew **+28.2%** in one phase and B, C, E each append more. Not a violation (ONB Risk 5 ruling: report the delta, do not compress below usability) and correctly measured and surfaced in RF §4 — it is the number the next three phases inherit. Raised as TECH_DEBT, not as a finding against this phase |
| P9 | Naming creates behavior | AC-1, AC-2 | ✅ ✅ | ✅ — and strengthened during execution: the ONB Q2 escalation that became amendment A10 exists precisely because `APPLIED — restrictive` was a disposition sitting in a column of relation nouns. The executor refused to ship a token that would have made this principle's own enforcement claim false on day one |
| P10 | Authority cannot self-extend | AC-7 | ✅ | ✅ — rules 17–19 plus the matching §14 anti-pattern. TFW-49 cited its own delegation three times to accept overruns; rule 19 names that move and forbids it |
| P11 | A remark is not a verdict | AC-5 | ✅ | ✅ — rule 8 covers research thread, review **and** chat; rule 9 closes the reverse polarity (owner-initiated change is still an amendment). Both restated in the §12 instruction block, so the rule sits where the author is working |
| P12 | A frozen baseline must be diffable | AC-6 | ✅ | ✅ — and this is the phase's strongest work. Rule 14 extends the reserved word to the **first** freeze because the executor checked and found TFW-53's own baseline commit non-conforming; rule 15 is slash-free because the documented form was measured returning zero rows |
| P1, P4, P8, P13–P17 | — | N/A per TS §3 | — | Correctly scoped out: P1 is task-level, P4 lives in `plan.md` (Phase B), P8 is Phase D, P13–P16 are review-side (Phase C), P17 is Phase E |

**No principle was mapped to a failed AC. No principle violation found.**

> Noted for Phase C, which replaces this check: the mapping-integrity structure the HL itself
> criticises (§3 *"a principle mapped to a passing AC scores ✅ regardless of the AC's content"*) is
> the structure I just used. It happens to hold here because I verified AC content independently in
> verify.md rather than trusting the checkmarks — but that is reviewer discretion, not the check
> working. The HL's diagnosis of its own review template is correct and Phase A does not fix it,
> nor was it asked to.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D19 — HL update = mandatory RESEARCH output | RES now classifies into two tables; frozen sections get proposals, not edits | **No** — narrowed, not revoked. Research still produces HL feedback; DoF-8 is the guard and it is not hit |
| 2 | D20 — implicit approval = transition to next status | The `Contract` field makes approval explicit and separate from task status | **No** — this is the correction D20's failure mode called for. `conventions.md` rule 1 states the two are not interchangeable |
| 3 | D24 — Pattern A: inline defaults, not indirection | The frozen/free split is restated inline in `templates/HL.md`, `conventions.md` §3 **and** HL-TFW-53 §3 | **No** — Pattern A honoured. All three lists verified identical (verify.md V1, V3); TS §6 names HL §3 as the single decision point if they ever diverge |
| 4 | D31 — filesystem-as-state-machine | No new state file; contract state lives in the HL header plus git history | **No** — RES iter1 D5 settled this: a snapshot file creates two contracts that can disagree. H3 recorded the partial confirmation and the commit-scope-word remedy |
| 5 | D53 — evidence folder mandatory; 0 of 38 tasks created it while optional | `evidence/` present with three artifacts | **No** — compliant, and D53 is the argument that made `Proposer` a column rather than prose |
| 6 | D55 — `[agent/task/scope/role]` commit attribution | Rule 14 occupies the `scope` slot with a reserved `freeze` word | **No** — extends D55 within its own grammar; the phase's own commit `e37a8dc` conforms |
| 7 | D50 — phase folders renamed to `phase-a/` | RF obs. 2 reports `gen_docs.py` still globbing `Phase{X}/` | **No contradiction — a confirmation.** The RF documents that the resolver never caught up with D50. This is TECH_DEBT, not a conflict |

No applicable contradictions.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)? — each cites a verify.md V-item, a numbered command, or a quoted artifact passage
- [x] Referenced verify.md findings in DoD assessment? — check 1 cites V1–V6 and Commands 2–10; D1–D5 carried into REVIEW §5 rather than re-investigated
- [x] Checked RF §7-9 for presence AND quality (not just existence)? — check 6. §8's insights each carry an Implication; §9's second diagram is the shipped rule rendered as a decision tree with rule numbers on the branches, which is a genuine test of whether the rule is executable and not merely readable
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or "None"? — 7 items checked, none contradicts
- [x] Fact Candidates from RF reviewed — any that need challenge? — none challenged. FC1 re-measured by me in both shells and confirmed. FC2 and FC3 both trace to artifacts I opened. All three pass the "would the next agent decide differently?" filter — FC1 in particular is a standing constraint on every shell command this framework ever ships

Stage complete: YES
