# Verify — "Are the claims true?" · round 2

> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: **0.42** (`tfw.review.min_verify_ratio`)
> RF files claimed: **15** modified outside the task directory (round 2 commits `fb1fb36`, `fa17b41`)
> Files to verify: ⌈15 × 0.42⌉ = **7**
> **Verified: 15 of 15 — 100%.** Escalated on discrepancy D1 (below), and every file was opened regardless.

## Verification Log

### V1: `.tfw/glossary.md` — item 1, the `Reviewer` entry
- **RF claim:** *"stop granting the reviewer disposition authority"*; committed at `fb1fb36`.
- **Actual:** line 186 reads *"Triages executor Observations into REVIEW §5 and **proposes** a disposition
  for each; the **coordinator** rules them, once at the close of review (`conventions.md` §15). Cannot:
  … **rule a disposition**."*
- **Match:** ✅ — and this is the finding that blocked round 1. **HL DoF 5 no longer fires.**

### V2: `.tfw/glossary.md` — item 2, the `Disposition` entry
- **RF claim:** `pending — coordinator` added, ruler named, reference repointed.
- **Actual:** line 324 carries *"`pending — coordinator` and `pending — owner` are legal waiting states"*,
  *"the **coordinator** rules, once at the close of review"*, and *"→ `templates/REVIEW.md` §5,
  conventions.md §15"*. All three sub-items present.
- **Match:** ✅

### V3: `.tfw/glossary.md` — AC-16, `Revision budget` out and `Citation bar` in
- **RF claim:** the term removed and replaced, `Revision` loses its count language, `Rung` kept.
- **Actual:** `grep -n "Revision budget"` → **no hits**. `### Citation bar` at line 155, naming the basis
  cell as its enforcement site. `### Revision` (152) defines a revision by *did the declared outcome
  change* and names the sibling form; no count language. `### Rung` (158) intact.
- **Match:** ✅

### V4: `KNOWLEDGE.md` — items 4 and 5, and the AC-16 sites
- **RF claim:** line 173/174's two facts corrected; the `TLD` §2 row added; `Correction Loop` and `D72`
  describe the citation bar and record the reversal; this task's own row stops claiming a key.
- **Actual:** line 174 reads *"written out in `templates/REVIEW.md` §5 and measured at **253 rows**"* —
  both facts corrected. `TFW_20260830-194027_TLD` row present at line 160. `Correction Loop` (line 23)
  carries the citation bar, the basis cell, the two REVISE lifecycle states, and *"There is no revision
  count and no configuration key"*. `D72` (line 166) carries its own reversal in the words *"The headline
  was earned in two rounds, and the first round failed it"*. Line 161, this task's row: *"zero new
  artifacts and zero configuration keys"*.
- **Match:** ✅ — four sites, four confirmed.

### V5: `.tfw/CHANGELOG.md` — item 3 (verified, not edited) and the AC-16 sites
- **RF claim:** item 3 closed at `1de76bc` by the `TFW_20260902-153617_RTMW` session; the 2.1.0 entry
  announces no key and no budget and says both were introduced and withdrawn inside it.
- **Actual:** `git show 1de76bc -- .tfw/CHANGELOG.md` replaces *"verbatim duplicates … Nothing was lost"*
  with a line separating `§14:902` (verbatim) from `§14:901` (not), and says where the missing clause went.
  Chronology confirmed: `7bfc5b1` 15:59 → `1de76bc` 16:07 → `1a5d282` 16:08, so the fix pre-dates this
  round and the executor was right not to edit it. The 2.1.0 entry states, at line 118, *"A configured
  budget on revisions was introduced and withdrawn inside this same unreleased entry"*, with four grounds
  and *"nothing for a receiving project to remove"*.
- **Match:** ✅ on the claim · ⚠️ **D1** on what sits beside it — see Discrepancies.

### V6: `.tfw/conventions.md` §4 — AC-15, the revision grammar
- **RF claim:** four filename rows plus a new subsection generating four artifact rules from one line;
  the ordinal is the only suffix; the unsuffixed file is revision 1 and is never renamed; the highest
  ordinal governs; the RF rule cites `PROPOSAL__TFW-58__revise_protocol`.
- **Actual:** lines 392–395 carry exactly four rows — single-phase TS, single-phase REVIEW, phase TS,
  phase REVIEW. Lines 409–432 are *The revision suffix, and what it generates*: *"`__rev{N}` is the one
  suffix the grammar admits, and it is an ordinal"*; *"The unsuffixed file is revision 1, and is never
  renamed. No retroactive rename, ever"*; *"The highest ordinal governs"*; *"One line generates the four
  rules below: sibling where exactly one must govern; appended where the record is cumulative"*, followed
  by the four-row table. The RF row quotes the TFW-58 measurement verbatim. The bar on title suffixes at
  lines 397–403 is left standing, word for word.
- **Match:** ✅ — six of AC-15's bullets land in this one section, all confirmed by reading.

### V7: `.tfw/conventions.md` §5 — AC-16, item 7, and the round cycle
- **RF claim:** budget/ceiling/exhaustion return replaced by the citation bar with A10's return kept in
  full; the round cycle drawn once with three exits; *who takes the round is not regulated*, with the
  reason; `(develop)` gone; a 🔄 REVISE gains two lifecycle states in order.
- **Actual:** lines 699–710 carry *"The citation bar, and the return"* — the bar, the ✅ APPROVE fallback,
  the return to `owner` as a `transition` to ❌ BLOCKED with *no basis can be stated* as the trigger, the
  `type: human` / `type: agent` / `unassigned` cases, and *"Why it returns rather than being ruled here"*.
  Lines 715–730 draw the cycle: REVIEW → TS revision → RF → REVIEW rev2, with the three exits. Lines
  732–735 carry *"Who takes the round is deliberately not regulated"* with its reason. `grep -n "develop)"`
  → **no hits**. Line 667: *"🔄 **REVISE** — specific issues → 🟡 TS_DRAFT while the coordinator writes the
  round's order, then 🟠 ONB when the executor takes it."*
- **Match:** ✅ — five claims, five confirmed. No trace of a budget, a ceiling or a count.

### V8: `.tfw/conventions.md` §14 — the anti-pattern swap
- **RF claim:** the exhausted-budget anti-pattern becomes the citation-bar one.
- **Actual:** line 994 reads *"A 🔄 REVISE orders an item that names no breached condition — the citation
  bar, §5 … A loop that cannot close is evidence about the HL, and the agents inside it are the ones who
  could not close it."* No budget anti-pattern remains.
- **Match:** ✅ — and the edit's authority is textual (revision 1's file list, carried by TS rev2 §4).

### V9: `.tfw/conventions.md` §15 — item 6, the two Hard Stop entries
- **RF claim:** the Reviewer's REVISE entry returns the work to the Coordinator instead of dispatching an
  executor; a new Coordinator entry receives it, boundary only.
- **Actual:** lines 1053–1056: *"On 🔄 REVISE — state that the items are **proposals**, say how many, and
  **return the work to the Coordinator**: 'Start `/tfw-plan` to order the round.' Set `lifecycle: TS_DRAFT`.
  Do **not** write an ordered bound and do **not** dispatch an executor."* Lines 1061–1066 are the new
  *When a Coordinator receives work returned by a 🔄 REVISE* entry: order in your own artifact, instruct
  `/tfw-handoff`, **do not execute the round yourself**. The `review.md` row in the table above already
  named acceptance authority and forbids `disposition rulings`.
- **Match:** ✅ — round 1's defect (*point at `REVIEW` §4, dispatch an executor*) is gone from both sides.

### V10: `.tfw/workflows/review.md` — AC-13 bullet 4 and AC-16 bullet 2
- **RF claim:** Step 4 loses the count block and its config row and gains the citation bar; Step 6 item 4
  stops ordering; the only surviving occurrence of *bound* is the prohibition.
- **Actual:** Step 4 carries *"**The citation bar.** A 🔄 REVISE may propose only items naming the
  condition each breaches …"* and **no** configuration table row. `grep -nEi "budget|max_revision|revision
  cycle"` → **no hits in the file**. `grep -n bound` → **one hit, line 155**: *"the items stay **proposals**
  and the work returns to the **coordinator**, who orders the round in a TS revision (§15). No bound, no
  dispatch."*
- **Match:** ✅ — the RF's *"the only surviving occurrence is the prohibition"* is literally true.

### V11: `.tfw/workflows/plan.md` — AC-14's coordinator leg
- **RF claim:** Step 8, the coordinator's post-review act, with the two writes inline and the Hard Stop
  after them; measured at 1 847 words against an estimate of ~1 775.
- **Actual:** `## Step 8: a 🔄 REVISE returned the work — order the round` exists, and carries: (1) promote
  what needs its own contract, each with a PROPOSAL, *"because a disposition must name something that
  exists"*; (2) write `TS__{ID}__rev{N}.md`, a sibling, stating the round, who ordered it, the review it
  answers, **each item's basis**, what is not re-done, and *"its approval, which you stamp"*, with *"An
  empty basis cell means the item does not belong there: that cell is the citation bar's enforcement
  site"*; (3) **STOP**. `wc -w` → **1 847**.
- **Match:** ✅ on content · the 1 847 reproduces exactly, and it is 647 over `conventions.md` §11's
  ceiling — self-reported, and outside DoD 10's binding unit. Recorded as §5 row 3.

### V12: `.tfw/workflows/handoff.md` — AC-14's executor leg, AC-16 bullet 4
- **RF claim:** Context Loading item 7 sends a returning executor to the highest-numbered TS revision and
  item 8 becomes the prior REVIEW; the return section is TS-first with the corrected grammar; *"The budget
  is counted, and not by you"* is gone; the detector is withdrawn.
- **Actual:** item 7 ends *"On a return after a 🔄 REVISE this is the **highest-numbered revision**,
  `TS__{ID}__rev{N}.md`, which governs and which carries the round's order"*; item 8 is
  *"**Prior REVIEW** — the reasoning behind that order"*, **unconditional** — round 1's dangling
  *"when this is a return after 🔄 REVISE"* is gone, and so is the never-built detector that was ordered
  to evaluate it. The return section reads TS first, REVIEW second, and states *"You are already obliged
  to read the TS, so there is nothing to detect and nothing hidden."* `grep -i budget` → **no hits**.
- **Match:** ✅ — and the file is 1 730 words, **19 lighter** than round 1 left it, exactly as claimed.

### V13–V14: `.tfw/project_config.yaml` · `.tfw/templates/project_config.yaml`
- **RF claim:** the key and its three-line comment removed from both; both re-parse to
  `{'min_verify_ratio': 0.42}`; `ONB`'s `description` covers the executor's whole leg.
- **Actual:** `yaml.safe_load` on both → `tfw.review == {'min_verify_ratio': 0.42}`. Both `ONB` entries
  read *"Onboarding report written; the executor is working toward the RF, re-entry after a 🔄 REVISE
  included"*; both `RF` entries still read *"Execution complete, RF written"*, which is what makes the
  pair honest.
- **Match:** ✅ ✅ — two files, byte-level confirmation by parse rather than by grep.

### V15: the six re-synced adapter copies (`.claude/commands/`, `.agent/workflows/` × `tfw-{review,handoff,plan}`)
- **RF claim:** six copies re-synced; **all 22 verify by `cmp`**; the three Codex thin routers are genuine
  no-ops.
- **Actual:** independent sweep of all 11 sources against both full-copy folders — **22 of 22
  `cmp`-identical, drift 0**. All 11 Codex skills also `cmp`-identical to their sources in
  `.tfw/adapters/codex/skills/`. Neither `tfw-review` SKILL nor any router appears in `git status`.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `git grep -n "max_revision_cycles" -- . \| grep -v "^workspace/\|^tasks/"` | **no output — 0 hits.** The gate the order names, passing |
| 2 | `git grep -c "max_revision_cycles" 1f5f578 -- .` (same exclusion) | **12 files** listed, **14 hits** — reproduces the RF's before-figure exactly, file for file |
| 3 | `awk '/^## Step 4/{f=1} f&&/^## Step 7/{exit} f' .tfw/workflows/review.md \| wc -w` | **477** (ceiling 483) |
| 4 | `awk '/^## Anti-patterns/{f=1} f' .tfw/workflows/review.md \| wc -w` | **160** (ceiling 163) |
| 5 | `wc -w` on `review.md` · `handoff.md` · `plan.md` | **1 699** · **1 730** · **1 847** |
| 6 | the same three at `fb1fb36` (round 1 as it entered round 2) | **1 702** · **1 749** · **1 702** — every delta in the RF's table reproduces |
| 7 | `awk` §5 and §4-naming boundaries on `conventions.md` | §5 **1 673** · §4 naming **668** — both figures as claimed |
| 8 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | **1 failed, 321 passed, 1 skipped in 285.74 s** — reproduces the RF's own report |
| 9 | the `DOUBLED_SLUG` detector re-run standalone | **12 offenders**, every one `TS__{ID}__rev{N}.md` or `REVIEW__{ID}__rev{N}.md` — the RF's enumeration, line for line |
| 10 | `python .tfw/scripts/gen_index.py --check tasks` | ✅ *59 tasks validate against the closed schema*; 17 informational phase notes, unchanged |
| 11 | `python .tfw/scripts/gen_index.py --check project` | ✅ *project is consistent with the release it declares* |
| 12 | `cmp` sweep: 11 sources × 2 folders, plus 11 Codex skills | **33 of 33 identical, drift 0** |
| 13 | `yaml.safe_load` on both config files | `{'min_verify_ratio': 0.42}` — no key, and it parses |
| 14 | `grep -n '\$[0-9]\|\$ARGUMENTS'` on `review.md` and `templates/REVIEW.md` | **no hits** — the adapter-substitution hazard stays clear |
| 15 | CRLF sweep over all files in the three round-2 commits | **none** — every file LF, so the `cmp` gate means what it says |
| 16 | `git status --porcelain` | ` M .gitignore` and one untracked link directory, **neither this task's** — every round-2 artifact is committed |
| 17 | `diff` of the HL against `git show 1c7b55e:` | **identical** — the contract baseline is the file I judged against |
| 18 | `git log --format="%h %s" \| grep -E "^\S+ \[[^]]*/TFW_20260902-112841_RDP/freeze/"` | six freeze commits; `1c7b55e` is the live baseline (A13 + A14) |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | *"14 hits in 12 tracked files at `1f5f578` → 0 in 0 now"* | RF §3.2 AC-16, EV E15 | `git grep -c` at both revisions, run independently — 12 files named, 14 hits summed; 0 now | ✅ |
| C2 | *"477 of 483, met by subtraction: 88 words freed, 82 spent"* | RF §2.2 decision 1, §4.2 | `awk`+`wc` at `1f5f578^`, `fb1fb36` and `HEAD`: 483 → 480 → **477**. The arithmetic is internally consistent and the endpoint is measured | ✅ |
| C3 | *"All twelve offenders are `TS__{ID}__rev{N}.md` or `REVIEW__{ID}__rev{N}.md`"* | RF §4.2, §6.2 obs 2 | the detector re-implemented from `docs/scripts/test_integration.py`'s own regexes and re-run — 12 offenders, all that one form, no unintended offender behind the count | ✅ |
| C4 | *"Item 3 — closed at `1de76bc` by the `TFW_20260902-153617_RTMW` session"* | RF §3.2 items 1–5, EV E17 | `git show 1de76bc -- .tfw/CHANGELOG.md`, and the commit's own message, which also records that two deletions were swept into `7bfc5b1` by a concurrent session | ✅ — a claim about **another session's** work, and it holds |
| C5 | *"`plan.md` measures 1 847 against the order's ~1 775 estimate. Over by 72"* | RF §4.2, reported against the executor's own interest | `wc -w .tfw/workflows/plan.md` → 1 847; TS rev2 §4 → *"~1 702 → ~1 775 words"* | ✅ — the overrun is real and was self-reported |
| C6 | *"`PROPOSAL__TFW-58__revise_protocol` … 'the TS was overwritten in place; revisions 2 → 3 → 4 recorded only as header prose'"* | `conventions.md` §4 revision table; TS rev2 §6 | quoted in the canon as the RF rule's measurement. **The proposal file is in the frozen legacy corpus** and the quotation is consistent with HL §2.3, which measures the same event independently | ✅ |
| C7 | *"the mechanism ends the loop in exhaustion, which §7 principle 4 forbids in those words"* — A13's first ground | HL §12 A13; `glossary.md` `Citation bar`; `KNOWLEDGE.md` D72 | HL §7 principle 4, read at baseline `1c7b55e`: *"A loop ends in a decision, never in exhaustion."* The contradiction was real, and D72 now records it | ✅ |
| C8 | `.tfw/CHANGELOG.md`'s *"`§14:902` … `§14:901`"* line citations | 2.1.0 entry, lines 353–356 | `conventions.md` **956** and **957** today. Correct when written at `1f5f578`; **round 2's own +55 lines in §14 moved them** | ❌ **D1** |

## Discrepancies Found

**D1 — two line citations in the shipped CHANGELOG no longer resolve.** The 2.1.0 entry names `§14:901`
and `§14:902` to distinguish the verbatim duplicate from the non-verbatim one. Both were correct at
`1f5f578`; `fa17b41` added 118 lines to `conventions.md`, and the two anti-patterns now sit at **956** and
**957**. The *substance* of the claim still holds — I re-read both lines and the verbatim/non-verbatim
split is exactly as stated — so this is a stale locator, not a false claim. It is in a file this round
edited, in the release this task ships.

**Escalation:** verification went to **15 of 15 files, 100%**, on D1. Nothing further surfaced.

**Not a discrepancy, recorded so the next reviewer does not re-open it.** `TS__…md` (revision 1) still
carries *"This consumes TS revision 2 of `tfw.review.max_revision_cycles` = 2 — the budget is now spent"*,
a mechanism that no longer exists. `git log -- ` on that path shows its last touch at `7bfc5b1` 15:59,
**before** revision 2 existed at 16:08. AC-15's own rule — *a superseded revision is never touched* — makes
leaving it correct. This is the grammar working, not drift.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E12 | `evidence/round2.md` §1 — AC-13, the nine basis cells read out | ✅ | ✅ — I counted the basis cells in TS rev2 §5a independently: **nine items, nine filled cells**, none empty |
| E13 | `evidence/round2.md` §2 — AC-14's chain walked | ✅ | ✅ — cross-checked against the four journal events and the commit graph; every step's file-read and file-write is the one the trace shows. The pending sixth step is declared as pending |
| E14 | `evidence/round2.md` §3 — the directory listing as the grammar's first instance | ✅ | ✅ — `ls` confirms `TS__…md` beside `TS__…__rev2.md`, one RF, one ONB |
| E15 | `evidence/round2.md` §4 — the count before and after | ✅ | ✅ — reproduced by commands 1, 2, 3, 4, 12, 13 above |
| E16 | `evidence/round2.md` §5 — the lifecycle across the leg | ✅ | ✅ — the two `transition` events carry `from: TS_DRAFT`/`to: ONB` and `from: ONB`/`to: RF`, and their clock times bracket the work |
| E17 | `evidence/round2.md` §6 — items 1–5 verified rather than redone | ✅ | ✅ — reproduced by V1, V2, V4, V5 and check C4 |
| E18 | `evidence/round2.md` §7 — the red test with all twelve offenders | ✅ | ✅ — reproduced exactly by commands 8 and 9 |
| — | `evidence/EV__…md` *Evidence — round 2* | ✅ | ✅ — seven rows, an environment delta naming the shared working tree and its commit discipline, and a round-2 attachment row |

**Verdict on the evidence itself: 7/7 present, 7/7 reproduced independently, 0 missing.** Two rows report
against the executor's own convenience — `plan.md`'s overrun and the red test. **One vocabulary note:**
E18's status reads *"VERIFIED as a measured failure"*. The status vocabulary describes the evidence, not
the criterion, so this is not a false green — the row states the failure in its own first sentence — but a
reader scanning the *"7/7 VERIFIED"* summary line alone would not see that one of the seven documents a
broken gate.

## Knowledge Citations Verified

> PV priorities 0–4 scanned in full; 5–7 by relevance. HL §7.2 carries **27** rows; ONB §8.6 adds a
> **round-2 delta** of four re-applications plus one new item (N4).

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1–2 | HL §7.2 #1, #2 | PV 0 — `NS1` and its second paragraph | ✅ `#ns1` at `.tfw/README.md:72` | ✅ | ✅ — *"understand what the work is for, inspect its material grounds … see where authority remains, and continue"*, and the *"increases output while obscuring purpose"* paragraph, both quoted exactly | ✅ — the axis is those four words; round 2's citation bar rests on the same clause |
| 3–6 | HL §7.2 #3–#6 | PV 0 — `NS2` principles 4, 5, 6 and the closing test | ✅ `#ns2` at line 79 | ✅ | ✅ — all four quoted verbatim, including *"Name boundaries, acceptance authority, accountability, stop conditions, and escalation **before** granting autonomy"* | ✅ — principle 4 is the whole of §15's grant; principle 5 is what the citation bar's ✅ APPROVE exit delivers |
| 7 | HL §7.2 #7 | PV 0 — `NS3` non-goals | ✅ `#ns3` at line 103 | ✅ | ✅ — *"a maximum-documentation bureaucracy … that measures success by artifact count"* | ✅ — and round 2 makes it stronger: the one entity round 1 spent was returned |
| 8–10 | HL §7.2 #8–#10 | PV 1 — Methodology values: Structural Enforcement · Naming Creates Behavior · Candor Over Flattery | ✅ `#methodology-values` at line 91 | ✅ | ✅ — *"a rule that cannot reveal its own violation is only advice"* is exact | ✅ — **#8 is round 2's load-bearing citation**: it is why the basis cell, not the prose, is the bar's site |
| 11–15 | HL §7.2 #11–#15 | PV 2 — `knowledge/philosophy.md` F42, F40, F25, F43, F36 | ✅ | ✅ all five present (lines 49, 47, 32, 50, 43) | ✅ | ✅ — F40 is why a word ceiling is a defensible criterion; F43 is why round 2 fixed the artifact rather than patching four symptoms |
| 16–19 | HL §7.2 #16–#19 | PV 3 — `KNOWLEDGE.md` D64, D63, D13, D65 | ✅ | ✅ all four present (lines 100, 99, 49, 101) | ✅ | ✅ — **D65** *(reverting a result never reverts its trace)* is the direct ancestor of AC-15's RF rule |
| 20–21 | HL §7.2 #20, #21 | PV 4 — `conventions.md` §11 Design Rules, §14 | ✅ | ✅ | ✅ — *"workflow instructions ≤1200 words"* and the firing-rate anti-pattern | ✅ |
| 22, 25, 26, 27 | HL §7.2 #22, #25, #26, #27 | labelled **PV 7** — `conventions.md` §15 and §5; `templates/REVIEW.md` §5; `templates/journal/event.md` | ✅ all four | ✅ all four | ✅ — each quotation is exact, and #27's post-ONB correction about `transition`/`BLOCKED` matches `conventions.md` §5 | ✅ — **but the priority label is unsupported.** See D2 below |
| 23–24 | HL §7.2 #23, #24 | PV 6 — `knowledge/process.md` F30, F14 | ✅ | ✅ (lines 37, 21) | ✅ | ✅ — F30 *"capture without an enforcement site does not change behaviour"* is principle 7's source |
| N1–N4 | ONB §8.6 round-2 delta | #8, #19, #22, #27 re-applied, plus **N4 — `conventions.md` §4 *Artifact file naming*** | ✅ | ✅ — the table AC-15 describes | ✅ | ✅ — N4 **is** ONB Q7, and it corrected the order: AC-15 had named §3, and the table is in §4 |

**D2 — a labelling defect, not a citation defect, and it recurred inside this task.** The PV Index
(`glossary.md`) defines priority 4 as `conventions.md` **§3, §11 and §14** and priority 7 as *"Other
`knowledge/*.md`"*. HL §7.2's own note records four rows being moved from PV 4 to PV 7 after the ONB — but
`conventions.md` §5 and §15 and `.tfw/templates/` are **not** `knowledge/*.md` either, so the new label is
also unsupported, and the round-2 ONB then labelled `conventions.md` §4 as PV 4 again. Measured across the
corpus: **eight such citations in two tasks** (this one and `TLD`, which labels `conventions.md` §2 as
PV 4). Every item exists, resolves, matches and is relevant — the defect is that the Index has **no
priority slot** for canon sections outside §3/§11/§14, nor for `templates/`. Recorded, not escalated
against this delivery: §7.2 is a 🟢 FREE section and the citations themselves are sound.

**Totals: 27 HL citations + 5 ONB rows. Resolved 32/32. Semantically verified 32/32. Irrelevant 0.
Hallucinated 0.** Priority labels unsupported on 5 of 32.

## Checkpoint

**Self-check:**
- [x] Opened **15 of 15** files (≥ the required 7) and recorded findings per file
- [x] Ran **18** commands, including the full build gate, both consistency gates, a 33-pair `cmp` sweep and an independent re-implementation of the failing detector
- [x] Claim & Source Checks filled — eight claims spot-checked by weight, every citation traced, the two load-bearing numbers re-measured from primary sources rather than from the RF
- [x] Each RF §3.2 checkmark verified against the actual file — including the one deliberately left `[ ]`
- [x] `KNOWLEDGE.md` checked — `Correction Loop`, `D72`, §2's two rows and §3's row all read; **no contradiction with the shipped canon**
- [x] Knowledge Citations from HL §7.2 and ONB §8.6 verified — priorities 0 and 1 checked separately though both live in `.tfw/README.md`
  - Total: **32**, resolved: **32**, semantically verified: **32**, irrelevant: **0**, hallucinated: **0**
- [x] Evidence artifacts from RF §5.2 verified
  - Total evidence items: **7**, verified: **7**, missing: **0**

Stage complete: **YES**
