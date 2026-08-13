# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## HL §7 Principles Check — TS §3 mapping integrity

| # | Principle (HL §7) | TS maps to | AC result | Principle held? |
|---|------------------|-----------|-----------|-----------------|
| P2 | Classify, never edit | AC-2 | ✅ met | ✅ both "update HL" instructions replaced, not qualified; 0 grep matches repo-wide |
| P3 | Structural enforcement over guidelines | AC-1, AC-3 | ✅ met | ✅ approval is a written field + a commit; verdicts are a labelled block |
| P4 | Batch, don't interrupt | AC-2 | ✅ met | ✅ *"Escalate once per iteration — one message carrying every proposal"* |
| P5 | Evidence, cost, alternative | AC-2 | ✅ met | ✅ all three named in the escalation clause |
| P6 | Narrow D19, don't revoke it | AC-4 | ✅ met | ✅ new `MUST` rule: recommendations **every** iteration, classified, never applied |
| P7 | Token density | AC-6 | ⚠️ **partial** | ⚠️ **substance holds, target does not.** Everything added is a numbered item, no prose block; the file *shrank* (1,206 → 1,195) so DoF-3 never fires. But AC-6 bullet 1 names two figures and only the hard one is met |
| P8 | Tool-agnostic by behaviour | AC-5 | ✅ met | ✅ 0/0 on both files; rule 15 referenced instead of a command inlined |
| P11 | A remark is not a verdict | AC-3 | ✅ met | ✅ 6d makes both dispositions explicit recorded acts |
| P12 | A frozen baseline must be diffable | AC-3 | ✅ met | ✅ re-freeze commit named with the reserved scope word, not a command line |

**Mapping integrity: 8 of 9 rows resolve to a fully-met AC.** One row (P7) resolves to a partially-met AC.
Per `review.md` Step 3 this is flagged as a principle shortfall, not only an AC miss — with the qualifier
that P7's own text (*"everything added is a numbered gate, never a prose block"*) is satisfied, and the
missed half is F2's working range, which frozen DoD-17 also requires.

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | **AC-1 – AC-5: fully met and independently reproduced** (verify.md V1-V4, commands 2-6). **AC-6: partial and declared** — 1,195 words meets F2's ≤1,200 hard threshold, misses the 700-900 working range; AC-6 bullet 1 requires both. Reporting rather than trimming is the behaviour AC-6 bullet 3 and DoF-2 mandate, so the *conduct* is correct while the *criterion* is unmet. **DoF-4 is triggered:** `fbdf443` modified six files, not the three TS §4 names (verify.md D1, D2) |
| 2 | Philosophy aligned — (a) mapping integrity, (b) design soundness | ❌ | **(a)** 8 of 9 TS §3 rows resolve to a met AC; P7 → AC-6 does not (table above). **(b) The design is sound and unusually well demonstrated:** 6d sits outside the research loop because 4 of this task's 13 §12 rows entered from an ONB or from the owner during execution — a measurement, not a preference; classification derives from target section + rule 6 rather than the incoming label, and the replay proves the difference on real history (verify.md C4). Separately: the phase's own thesis — *a change to a shipped artifact must be visible as a change* — is what D1 breaches in execution, not in design |
| 3 | Tech debt documented | ✅ | RF §6 carries 7 observations, each with file, line range, type and a stated consequence. Existing debt correctly cited and bounded: TD-134 (build placeholders, substitution disclosed), TD-135 (trigger does not fire — verified, C7), TD-140 (remaining half routed to Phase D), TD-141/TD-142 |
| 4 | Style & standards | ❌ | Template structure followed; naming, commit grammar `[claude-code/TFW-53/phase-b/executor]` and file naming all conform. Two defects in the artifact itself: **RF §3 contradicts RF §1** — the table lists four modified files, the DoF clearance line says *"outside TS §4's three"* (D2); and **RF §2 skips Decision 12**, running 1–11, 13, 14 (D4) |
| 5 | Observations collected | ✅ | All 7 survive the quality filter — none is filler. Obs. 2 (`🚫 WITHDRAWN` has no 6d path, with the 14-words-against-5-headroom arithmetic), obs. 4 (DoD-18's relabel entered a frozen section on ruling Q5 with no §12 row — independently confirmed at HL:724) and obs. 5 (two adapter surfaces still say *"Update HL"*) each name a consequence that would bite if left. The set's gap is D1, counted in row 1 |
| 6 | RF completeness (§7-9) | ✅ | §7: 3 fact candidates, each sourced to a dated user directive. §8: 2 strategic insights with implications drawn, not just captured. §9: two diagrams — an ASCII before/after of all four instruction sites, and a mermaid graph of verdict entry points annotated with measured counts (12 approved / 1 withdrawn / 0 rejected) |
| 7 | Evidence completeness — does the evidence **exist**? | ✅ | EV file present with environment header, 8 rows, verdict, 2 exhibits, attachments index. Every TS Evidence field is covered; the three `N/A` rows quote the TS's own justification verbatim; the one `DEFERRED` names a checkable blocker (0 rejected amendments in 13 rows) rather than a vague one. All statuses come from the fixed 4-value vocabulary |
| 8 | Evidence sufficiency — does the evidence **establish the claim**? | ❌ | For AC-1 – AC-5 it does, and better than required: the AC-2 replay declares its own circularity first and still finds a live unlogged frozen-section edit, and AC-3's history replay reports three divergences against itself rather than a clean pass. **What the evidence never tested is the file set.** No row, exhibit or command in the EV compares the commit's actual contents against TS §4 — the one check that would have caught D1 — while RF §3 certifies exactly that claim. Second gap: E8's ledger omits the authorised `plan.md`:97 removal and admits an unexplained 2-word reconciliation gap (D3) |
| 9 | Backward compatibility | ✅ | Step numbers deliberately stable — `glossary.md`:178 cites `plan.md Step 6c` twice and still resolves (verified C5); 6d added as a new label, nothing renumbered; the `min_iterations` gate block is byte-identical, so D38's only statement of the hard floor survives (V2). `pytest` 68/68 and `mkdocs build` both consume these files and both pass. Known consumer lag: the two adapter copies of `plan.md` still carry the old Step 6c — TS §9 assigns this to Phase D, and RF obs. 5 flags that until D runs, 2 of 3 surfaces instruct what the core now forbids |
| 10 | Safety | ❌ | No secrets, credentials or destructive shell operations. But the row's subject is *irreversible* operations judged on consequence: `fbdf443` committed three file deletions belonging to another task under this task's subject line, and a merged commit's subject cannot be rewritten. The misattribution is permanent — asking git when TFW-56 removed the mode files now returns a TFW-53 commit (D1) |

> Rows 7 and 8 answered separately and land differently — ✅ on existence, ❌ on sufficiency — which is the
> shape the template names as the normal form of a real finding. The distinguishing fact: the evidence is
> thorough about every claim it chose to test and silent about the claim that turned out to be false.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D19 — HL update = mandatory RESEARCH output | Research still produces HL recommendations every iteration; only the frozen channel turns from write to propose | No — narrowed as the HL designed, and the new `MUST` rule makes the narrowing visible rather than implicit |
| 2 | D20 — implicit approval = transition to next status | Step 4 replaces the transition with a written `Contract` field plus a freeze commit | No — this is D20's root cause being closed at the workflow site, as HL §7.2 #5 intends |
| 3 | D23 / D24 — workflow compression; Pattern A inline defaults | 13 duplication sites removed; `min_iterations: 2` and `max_iterations: 5` kept **inline** | No — the distinction was applied correctly: rules referenced, enforcement-critical defaults inline |
| 4 | D25 — `research/base.md` ≈500-word core algorithm | `base.md` 869 → 943 words | No contradiction with a shipped rule, but the gap to design intent widened. Already recorded: ONB citation 27 and the coordinator's ONB Recommendation-3 ruling both bound the addition; the +74 is 4 lines of class definitions and 1 `MUST` rule |
| 5 | D38 — `min_iterations` hard gate lives in `plan.md` Step 6c | Gate block left byte-identical | No — verified by diff (V2), the risk ONB flagged was actually neutralised |
| 6 | D50 — agent selection guidance removed from `conventions.md` §4 | *(no claim)* | No contradiction; D50 is what made `plan.md`:97 a dead reference, and its removal is correct but undisclosed (D3) |

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Every `⚪ N/A` carries a stated reason — no row skipped as a bare ✅? *(no row was N/A this review — all
      ten applied)*
- [x] Rows 7 and 8 answered separately, with different reasoning? *(existence vs. what the evidence tests)*
- [x] Referenced verify.md findings in DoD assessment? *(V1-V4, D1-D4, commands 2-6)*
- [x] Checked RF §7-9 for presence AND quality (not just existence)?
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or "None"? *(6 items checked, none contradicted)*
- [x] Fact Candidates from RF reviewed — any that need challenge? *(FC1 is the one to challenge and it
      survives on substance: parallel execution in one tree is real and no workflow states the staging rule.
      Its framing needs correcting, not its content — the RF presents it as a hazard avoided; D1 shows it as
      a hazard realised)*

Stage complete: YES

---

## Addendum — re-ruling after the owner's D1 waiver

> Appended 2026-08-13. The first-pass table above is left unedited. Four rows move; six stand.
> Basis: owner ruling of 2026-08-13 waiving D1, plus verify.md findings F1-F5.

| # | Check | First pass | Now | Why it moved |
|---|-------|-----------|-----|--------------|
| 1 | DoD met? | ❌ | **✅** | DoF-4's trigger was D1, waived by the owner. AC-1 – AC-5 were already fully met and independently reproduced. AC-6 remains partial **and reported**, which its own bullet 3 and DoF-2 make the correct outcome — a reported shortfall is compliance with the criterion's own instruction, not a breach of it |
| 2 | Philosophy aligned | ❌ | **✅** | (a) The only unmet mapping was P7 → AC-6, and AC-6's shortfall is a reported one, so no principle was defeated: P7's own text (*numbered gates, never a prose block*) holds and the file shrank. (b) Design soundness was never in doubt and F1 sharpens the compliment — the mechanism's one discriminating case was found by the mechanism itself, on real history |
| 4 | Style & standards | ❌ | **❌ stands** | D2 (RF §1 says four files, RF §3 says three) and D4 (Decision 12 missing) are internal to the RF and unaffected by the waiver |
| 8 | Evidence sufficiency | ❌ | **❌ stands** | The waiver removes what the evidence failed to catch, not the gap in the evidence itself: D3's undisclosed authorised removal still sits inside AC-6's number, and F5 shows *"no further duplication exists"* is an assertion with a live counterexample |
| 10 | Safety | ❌ | **⚪ N/A** | The only entry was D1's irreversible misattribution. Waived by the owner and carried by TD-144. Nothing else in this phase touches secrets, credentials or destructive operations — reason stated, not a bare ✅ |
| 3, 5, 6, 7, 9 | — | ✅ | **✅ unchanged** | — |

**Net: 7 ✅ · 2 ❌ · 1 ⚪.** Both ❌ rows are documentary defects in the RF, not defects in the shipped
mechanism, and neither blocks the phase.

### Principles Check — re-ruling

P7 → AC-6 was the one row that did not resolve to a fully-met AC. Re-ruled as **held**: the principle
commits to *"everything added is a numbered gate, never a prose block"* and to respecting the budget;
everything added is a numbered item, and `plan.md` left the phase **shorter** than it entered, so DoF-3
(*"`plan.md` grows past the attention budget"*) never came near firing. What remains unmet is F2's working
range — an obligation frozen DoD-17 carries, reported honestly, and now blocked by the F1 trade rather than
by unwillingness. **9 of 9 principles held.**

### F1-F5 do not change the verdict, and here is why

None of the five is a failure to deliver what the TS required:

- **F1** is a vice with no compliant exit — 5 words of headroom against a ~10-word clause, with DoF-2
  forbidding the trim that would pay for it. Escalating rather than choosing silently is exactly P5 and F25
  behaviour. → owner decision, TD-159.
- **F2** and **F3** are gaps in the frozen contract that only became visible once the mechanism ran. AC-2 and
  DoD-13 require applying refinements and require no record; `handoff.md` and `review.md` are outside TS §2.
  → TD-160, TD-161.
- **F4** and **F5** are text-quality findings worth ~10 and ~50 words. → TD-162, TD-163.

Judging an executor against obligations its TS does not carry is the mirror of the drift this task exists to
stop, and Principle 16 (*judge against the baseline, never the spec*) cuts both ways: the baseline is also
the ceiling of what may be demanded.

Addendum complete: YES
