# Verify — "Are the claims true?" · round 3

> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: **0.42** (`tfw.review.min_verify_ratio`)
> RF files claimed: **8** modified outside the task directory (`3c998ea`)
> Files to verify: ⌈8 × 0.42⌉ = **4**
> **Verified: 8 of 8 — 100%.** Escalated on D1, and every file was opened regardless.

## Verification Log

### V1: `docs/scripts/test_integration.py` — item 1
- **RF claim:** `DOUBLED_SLUG` becomes `\{ID\}__(?!rev\{N\})`, a lookahead admitting the one form §4
  mandates and **nothing else**; two assertions in `test_the_naming_detectors_actually_fire`; a comment
  citing §4 in the file's own style.
- **Actual:** the diff is +6/−2 lines: the constant becomes `re.compile(r"\{ID\}__(?!rev\{N\})")`, its
  comment cites §4 and states why an ordinal is admitted where a title suffix is not, and two assertions
  land in the self-test — `assert DOUBLED_SLUG.search("TS__{ID}__draft.md")` in the positives and
  `assert not DOUBLED_SLUG.search("TS__{ID}__rev{N}.md")` in the negatives. Offenders on the canonical
  surface re-measured with the file's own regexes: **12 → 0**. `test_no_canonical_example_doubles_the_slug`
  **passes**.
- **Match:** ⚠️ partial — the mechanism is right, the assertions are real, and the offenders are gone.
  **The claim *"and nothing else"* does not hold.** See **D2**.

### V2: `.tfw/workflows/handoff.md` — item 2
- **RF claim:** step 7 deleted not rewritten; steps 8–13 renumber to 7–12; the `RF` transition becomes
  step 13, the last act of Phase 3, after *Create RF*; the words dropped are the event-filename pattern
  step 6 already states; 1 730 → 1 727 words.
- **Actual:** the diff removes old step 7 entirely. Numbering re-derived from the file itself, before and
  after: *Implement* 8→7, *Run tests* 9→8, *Build gate* 10→9, *Collect evidence* 11→10, *Pre-RF Gate*
  12→11, *Create RF file* 13→12, and a new step **13** *Set the task's own state — `lifecycle: RF`* at the
  end of Phase 3. The new step carries no filename pattern. `wc -w`: **1 730 → 1 727.**
- **Match:** ✅ on the file itself. **The renumbering's consumers are D3.**

### V3: `.tfw/templates/REVIEW.md` — item 3
- **RF claim:** `### If REVISE — items to fix:` → `### If REVISE — items proposed to the coordinator:`,
  the placeholder asks for the condition each item breaches, nothing added, heading count unchanged.
- **Actual:** the diff is exactly two lines changed for two lines — the heading, and
  `1. {the item} — **basis:** {the TS acceptance criterion or frozen HL claim it breaches}`. Heading count
  counted independently: **10 before, 10 after.** No block, no section, no optional field.
- **Match:** ✅ — and read against `conventions.md` §15's Reviewer entry, the two now say the same thing.

### V4: `.tfw/conventions.md` §4 — item 4
- **RF claim:** one row; the EV file classified **appended** by the generating line rather than by
  analogy, with the reason in the row; the generating line not restated.
- **Actual:** the whole diff to `conventions.md` is **one added line**. The generated table now carries
  five rows — TS, REVIEW, RF, ONB, **EV** — and the EV row reads *"appended — a round's rows beside the
  earlier round's"* with the reason: *"nothing about an EV governs either, and an earlier round's
  verification does not stop being true, so a later round has nothing to supersede."* The generating line
  above it is untouched. §5 measures **1 673**, unchanged, which item 6's DoF required.
- **Match:** ✅ — and it is derived from the line rather than asserted, which is what the item asked for.

### V5: `.tfw/CHANGELOG.md` — item 5
- **RF claim:** both `§14:9NN` locators removed not corrected; the verbatim/non-verbatim claim untouched;
  no other locator swept; four `⚠️ Changed` bullets, one each for items 2, 3, 4 and 6.
- **Actual:** `grep -n '§14:9'` → **0 hits**, and a sweep for any `§NN:NNN` pattern in the whole 2.1.0
  entry returns **nothing at all** — so none was left and none was added. The clause now reads *"a
  **verbatim** duplicate of its §14 counterpart"* and *"§14 reads ``…``"*, with the quoted anti-pattern
  text intact, so both still resolve by text. `git diff … | grep -c '^+- \*\*'` → **4** new bullets, and
  reading them: `handoff.md`'s step deletion, the template heading, the EV row, the `paid` clause — items
  2, 3, 4, 6 exactly, each naming its file and what a receiver does, three of them *"nothing"*.
- **Match:** ✅ on all five bullets.

### V6: `.tfw/glossary.md` — items 6 and 2
- **RF claim:** `Disposition` gains one sentence on what a `paid` ruling requires; the two `handoff.md`
  step-number citations name the step by title instead.
- **Actual:** the diff touches exactly three entries. `Disposition` gains *"A **`paid`** ruling names the
  phase that pays it, and where the payment has not happened yet the **same act must order it** — in a
  round, citing the item's condition; unordered, `paid` accepts an item without a decision, which is
  deferral under a new name."* `Evidence Collection` and `Pre-RF Gate` lose their step numbers for titles.
  No new term. Word count **5 127 → 5 175**.
- **Match:** ✅ on item 6. ⚠️ on item 2's half — **two further citations survive, D3.** One minor figure
  note: the RF reports 5 126 → 5 174 where the same boundary measures 5 127 → 5 175; the **delta is
  identical at +48** and no gate reads this file's length, so it is a one-word measurement offset, not a
  false claim.

### V7–V8: `.claude/commands/tfw-handoff.md` · `.agent/workflows/tfw-handoff.md`
- **RF claim:** re-synced after item 2; all 22 copies verify by `cmp`.
- **Actual:** independent sweep of all 11 sources against both full-copy folders — **22 of 22
  `cmp`-identical, drift 0** — plus **11 of 11** Codex skills against their sources. 33 pairs, no drift.
- **Match:** ✅ ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | **1 failed, 321 passed, 1 skipped in 176.78 s** — reproduces the RF's own figure; `test_no_canonical_example_doubles_the_slug` now **passes** |
| 2 | `python .tfw/scripts/gen_index.py --check tasks`, exit code captured directly | **exit 1** · *"…20260902-181437__amendment_escalated__531a.md: summary is 123 code points, ceiling is 120"* · *"1 problem(s) across 60 tasks"* |
| 3 | a scan of every `journal/*.md` under `workspace/` and `tasks/` for `summary` length | **exactly one** event over the ceiling, at **123** code points — the coordinator's `20260902-181437` |
| 4 | the shipped regex probed against 9 names, including 3 the RF does not test | **2 mismatches** — `TS__{ID}__rev{N}__extra.md` and `TS__{ID}__rev{N}_draft.md` do **not** fire. **D2** |
| 5 | the candidate `\{ID\}__(?!rev\{N\}\.md)` probed against the same 9 | **0 mismatches**, and the canonical surface still returns **0 offenders** — so the tightening costs nothing |
| 6 | `handoff.md` numbered steps re-derived, before and after | 8–13 → 7–12 with a new 13; every one of the six titles moved by one |
| 7 | `grep -rniE "handoff…Step [0-9]+"` across `.tfw/`, `.claude/`, `.agent/`, `.agents/`, root docs | **four live citations existed**; two were de-numbered, **two survive and both are now wrong.** **D3** |
| 8 | `wc -w` on `handoff.md`, `review.md`, `glossary.md`, `templates/REVIEW.md`, `conventions.md` §4/§5 | 1 730→**1 727** · 1 699→**1 699** · 5 127→**5 175** · 1 128→**1 140** · 668→**743** · 1 673→**1 673** |
| 9 | `git diff a314751 HEAD -- .tfw/workflows/review.md` | **zero lines** — *left closed* is literally true, and its gates stay at 477/483 and 160/163 |
| 10 | `grep -n '§14:9' .tfw/CHANGELOG.md`, then a sweep for any `§NN:NNN` in the 2.1.0 entry | 0 hits, and none anywhere in the entry |
| 11 | `cmp` sweep: 11 sources × 2 folders + 11 Codex skills | **33 of 33 identical, drift 0** |
| 12 | template heading count, before and after | **10 → 10** |
| 13 | `conventions.md` §4 generated table, printed whole | **5 rows for the 5 artifacts a round produces** |
| 14 | `git grep -n "max_revision_cycles"` outside the trace | **0 hits** — round 2's withdrawal holds |
| 15 | `diff` of the HL against `git show 1c7b55e:` | **identical** — the file judged is the file frozen; no amendment was proposed this round |
| 16 | `git status --porcelain` | ` M .gitignore` only — a neighbouring session's, **not this task's.** Every round-3 artifact is committed |
| 17 | ONB §9.2 answer cells | Q10, Q11, Q12 all answered `(a)` with a pointer to §9.2a; none left `_{coordinator fills in}_` |
| 18 | `git show --stat` on the round's two commits | 8 files outside the task directory, exactly the 8 the order's §4 names; **no ninth** |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | *"12 offenders → 0"* | RF §3.3, §4.3, EV E19 | the detector's own regexes re-implemented and re-run over the same canonical surface | ✅ |
| C2 | *"The regex admits **exactly** the mandated ordinal suffix and nothing else"* | RF §3.3 item 1 bullet 1; EV E19; TS revision 3 item 1 | probed: two names of the form `{ID}__rev{N}<more>` are admitted | ❌ **D2** |
| C3 | *"1 730 → 1 727"*, and *"`review.md` left closed"* | RF §1.3, §4.3 | `wc -w` at `a314751` and `HEAD`; `git diff` empty for `review.md` | ✅ |
| C4 | *"the order's before figure had already changed: 2 failed, not 1"* | RF §2.3 decision 1 | the failing event was written in `bbdfde8`, the order's own commit — confirmed by `git show --stat` and by the event's clock time 18:14 against the order's 18:18 | ✅ — a claim **against the coordinator** and it holds |
| C5 | *"a journal event is immutable once written (`conventions.md` §4)"* | RF §2.3 decision 9, §6.3 obs 1 | `conventions.md` §4: *"A written event is never edited and never deleted; a correction is a new event that references the one it corrects"* | ✅ — quoted correctly, and it is what makes the repair a decision rather than a task |
| C6 | *"`glossary.md`'s two citations of those numbers … now name the step by its title"* | `.tfw/CHANGELOG.md`, round-3 bullet 1; RF §1.3 | **four** live citations existed | ❌ **D3** |
| C7 | *"heading count 10 before, 10 after"* | RF §1.3, §3.3 item 3 | counted independently at both revisions | ✅ |
| C8 | *"exactly four `⚠️ Changed` bullets, one per shipping item"* | RF §3.3 item 5; TS DoF | `git diff \| grep -c` → 4, and each read against its item | ✅ |

## Discrepancies Found

**D1 — the project's declared build gate is red, and it is not the executor's work.**
`python .tfw/scripts/gen_index.py --check tasks` (`build.verify` in `project_config.yaml`) **exits 1**:
`workspace/…/journal/20260902-181437__amendment_escalated__531a.md` carries a `summary` of **123 code
points** against `tfw.journal.max_summary_length` = **120**. `build.test` fails on the same fact, through
`test_gen_index.py::test_the_repository_stateless_phases_are_all_informational`, which asserts that gate
returns 0. **TS AC-11's two bullets — *"The build passes"* and *"`--check tasks` stays green"* — are both
breached.** The event was written at 18:14 in `bbdfde8`, the commit that ordered this round, as the act
paying REVIEW revision 2 §5 row 10. Scanned the whole corpus: it is the **only** event over the ceiling.
The RF declares all of this and routes it; the finding is the state, not the reporting.

**D2 — the lookahead admits more than the one documented form.** `\{ID\}__(?!rev\{N\})` checks only that
`rev{N}` *follows*, never that it *ends* the name. Measured:

```
  fires=False   TS__{ID}__rev{N}__extra.md     ← an ordinal followed by a title suffix
  fires=False   TS__{ID}__rev{N}_draft.md      ← an ordinal glued to more
  fires=True    TS__{ID}__draft.md             ← the case the two new assertions test
```

The order's bullet says *"admits **exactly** the mandated ordinal suffix and nothing else"* and *"`{ID}__`
followed by anything other than the revision form still fires"*; revision 3 §7's first DoF names *"made
green by widening `DOUBLED_SLUG` beyond the one documented form"*. The admitted set is
`{ID}__rev{N}<anything>`, which is broader than `{ID}__rev{N}.md`. **The repair is verified, not
proposed:** `\{ID\}__(?!rev\{N\}\.md)` returns 0 mismatches across all nine probes **and** 0 offenders on
the canonical surface, so it costs nothing. The two new assertions do not cover this because both place
their suffix *before* the ordinal, never after it.

**D3 — the renumbering left two live citations pointing at real but different steps.** Four existed; two
were de-numbered; two survive, and **both were correct before this round and are wrong now** — the worst
shape, because they resolve:

| Citation | Before | Now points at | State |
|---|---|---|---|
| `glossary.md` `Evidence Collection` | Step 11 = *Collect evidence* ✅ | the step's **title** | ✅ fixed by item 2 |
| `glossary.md` `Pre-RF Gate` | Step 11, already wrong (it was 12) | the step's **title** | ✅ fixed, and the pre-existing error dissolved |
| `glossary.md` `Execution Loop` | *"Phase 2 Step 8"* = *Implement* ✅ | Step 8 = **Run tests** | ❌ **broken by this round** |
| `KNOWLEDGE.md` **D52** | *"handoff Step 11"* = *Collect evidence* ✅ | Step 11 = **Pre-RF Gate** | ❌ **broken by this round** |

Item 2's own justification says *"a renumbering that leaves them pointing at old numbers is half of
one"*, and the ONB's Q10 recorded that this class *"has already failed here unobserved"*. It failed again,
twice, in the act of fixing it. **D52 is PV priority 3** — an architecture decision every coordinator's
PV scan reads — so the wrong locator is in the highest-traffic of the four.

**History, correctly untouched, recorded so no one "fixes" it later:** `.tfw/CHANGELOG.md` lines 1396,
1448 and 1516 cite `handoff.md` step numbers inside **released** 2.0.x entries, and `KNOWLEDGE.md` §2's
`TFW-46` row cites them inside a historical task row. A changelog entry describing what a step was then is
a record. Neither is a live reference and neither is a finding.

**Escalation:** verification went to **8 of 8 files, 100%**, on D1, and every claim in the Claim & Source
table was re-derived from a primary source rather than from the RF.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E19 | `evidence/round3.md` §1 — item 1, the detector | ✅ | ⚠️ — the offender count and the four admitted/caught cases reproduce exactly; the row's own headline *"admits exactly the mandated suffix"* is refuted by D2's two probes, which the evidence does not attempt |
| E20 | `evidence/round3.md` §2 — item 2, the deletion and renumbering | ✅ | ✅ — the step sequence and both word figures reproduce; the consumers outside the file are not in scope of this row and are D3 |
| E21 | `evidence/round3.md` §3 — item 3, the template | ✅ | ✅ — heading count and both changed lines reproduce |
| E22 | `evidence/round3.md` §4 — item 4, the EV row | ✅ | ✅ — five rows counted independently |
| E23 | `evidence/round3.md` §5 — item 5, the locators and the four bullets | ✅ | ✅ — 0 hits, no sweep, 4 bullets |
| E24 | `evidence/round3.md` §6 — item 6, the `paid` clause | ✅ | ✅ — the sentence is generic, and the four rulings it legitimises are quoted in the evidence rather than in the shipped text, which HL §7.1 requires |
| — | the EV file's *Evidence — round 3* header and verdict | ✅ | ✅ — **and the verdict declares item 1's gate BLOCKED rather than reporting it green**, with the three suite runs and the reason for the third |

**Verdict on the evidence: 6/6 rows present, 6/6 reproduced, 0 missing.** Three suite runs are reported
where one would have been enough, including a third taken only because a comment was restyled after the
second — *"the figure that ships should come from the bytes that ship"*. The honesty is unusual and it is
what let this review find D2 by extending a probe the RF had already half-built rather than by distrusting
it.

## Knowledge Citations Verified

> PV priorities 0–4 scanned in full; 5–7 by relevance. HL §7.2 carries **27** rows, unchanged since
> round 2's audit and re-checked here for resolution; ONB §9.6 adds a **round-3 delta** of three
> re-applications and, deliberately, **no new item** — which is itself the check that this round
> introduces no new mechanism.

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1–27 | HL §7.2 | all rows, PV 0 → PV 7 | ✅ 27/27 — `#ns1`, `#ns2`, `#ns3`, `#methodology-values` all resolve in `.tfw/README.md`; `philosophy.md` F13/F21/F25/F36/F40/F42/F43, `process.md` F14/F30, `KNOWLEDGE.md` D13/D63/D64/D65 all present | ✅ 27/27 | ✅ — quotations exact, re-spot-checked on the four rows round 3 uses | ✅ — unchanged since round 2's audit; the labelling defect on 4 rows stands as REVIEW revision 2 §5 row 9's ruled `not material` |
| N1 | ONB §9.6 #8 | PV 1 — Structural Enforcement, *"a rule that cannot reveal its own violation is only advice"* | ✅ | ✅ | ✅ | ✅ — **the load-bearing citation of this round, and it is why D2 matters**: the two assertions are the site, and they do not cover the one widening they exist to prevent |
| N2 | ONB §9.6 #21 | PV 4 — `conventions.md` §14 firing-rate rule | ✅ | ✅ | ✅ | ✅ — items 1 and 3 sharpen existing gates; `templates/review/judge.md` was verified untouched, 10 rows before and after |
| N3 | ONB §9.6 #12 | PV 2 — `philosophy.md` F40, *"which term is missing"* | ✅ | ✅ (line 47) | ✅ | ✅ — applied to item 6: a clause on an existing term rather than a paragraph in §5, which is why §5 measures 1 673 unchanged |
| N4 | ONB §9.6 #14 | PV 2 — F43, *"answering a correct catch with the smallest possible fix is itself a defect pattern"* | ✅ | ✅ (line 50) | ✅ | ✅ — cited **against the executor's own convenience**: Q10 and Q11 exist because the smallest fix leaves stale references and undocumented shipped changes behind. **D3 is the measure of how right that instinct was and how incompletely it was carried out** |

**Totals: 27 HL citations + 4 ONB rows. Resolved 31/31. Semantically verified 31/31. Irrelevant 0.
Hallucinated 0.**

## Checkpoint

**Self-check:**
- [x] Opened **8 of 8** files (≥ the required 4) and recorded findings per file
- [x] Ran **18** commands, including the full suite, the release gate's exit code read directly rather than through a pipe, a corpus-wide scan of journal summary lengths, a 33-pair `cmp` sweep, and an independent probe of the shipped regex against cases the RF does not test
- [x] Claim & Source Checks filled — eight claims chosen by weight; **two failed**, and both failures were found by extending a measurement rather than by re-reading prose
- [x] Each RF §3.3 checkmark verified against the actual file, including the one honestly left `[ ]`
- [x] `KNOWLEDGE.md` checked — and it is where **D3**'s second half lives: `D52` cites a step number this round moved
- [x] Knowledge Citations from HL §7.2 and ONB §9.6 verified; priorities 0 and 1 checked separately though both live in `.tfw/README.md`
  - Total: **31**, resolved: **31**, semantically verified: **31**, irrelevant: **0**, hallucinated: **0**
- [x] Evidence artifacts from RF §5.3 verified
  - Total evidence items: **6**, verified: **6**, missing: **0**

Stage complete: **YES**
