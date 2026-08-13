# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42 (`tfw.review.min_verify_ratio`)
> RF files claimed: 7 (4 modified framework files + 2 new evidence files + `README.md` board row)
> Files to verify: ⌈7 × 0.42⌉ = **3** → **escalated to 100% on discrepancy D1**; 10 files opened in total
> (the 7 claimed + 3 undisclosed deletions found in the commit)

## Verification Log

### V1: `.tfw/workflows/plan.md`
- **RF claim:** Step 4 gains `On approval — freeze the contract` (contract field, freeze commit before the
  first research iteration, pointer to §3 rule 15). Step 6c items 3-4 replaced by classify-by-target-section
  + rule 6, `PROPOSED` transcription, one escalation per iteration. New 6d block. 13 duplication sites
  compressed. 1,206 → 1,195 words, `+35 / −47` lines.
- **Actual:** All present and worded as claimed. Step 4 lines 58-61 carry exactly three numbered items;
  item 1 sets `🔒 FROZEN — approved by {owner} YYYY-MM-DD`, matching the `Contract` field vocabulary
  `conventions.md` rule 1 defines. Item 3 points at §3 rule 15 without restating it. Step 6c items 3-4
  (lines 100-103) carry all five things AC-2 requires, including *"never by the table it arrived in"* and
  *"A coordinator may not apply a proposal it filed"*. 6d (lines 116-120) is a labelled block, not a
  renumber. `git show --stat fbdf443` reports `82 ++/--` on this file.
- **Match:** ✅

### V2: `.tfw/workflows/plan.md` — `min_iterations` gate preservation (RF §4 claim)
- **RF claim:** *"the Gate check block was left **byte-identical**"* — all three `min_iterations` outcomes
  survive, D38's only statement of the hard gate intact.
- **Actual:** `diff` of the old and new `**Gate check:**` blocks returns **exactly one changed line** — line
  10, the trailing `After all iterations complete: update HL → …` that AC-2 required to go. The nine lines
  of gate logic are byte-identical. `glossary.md`:178 still cites *"plan.md Step 6c"* and resolves.
- **Match:** ✅ — claim is precise, not approximate.

### V3: `.tfw/workflows/research/base.md`
- **RF claim:** Step 6 item 3 becomes two classes with target-section requirement + classify-never-edit;
  one new `MUST` rule. 869 → 943 words, `+5 / −1`.
- **Actual:** Diff confirms exactly +4/−1 in Step 6 and +1 `MUST` line. `wc -w` = **943**. Class names
  `Refinements` / `Amendment Proposals` are verbatim from `templates/RES.md`; the free list `(§2, §7.2,
  §8-§11)` and frozen list `(§1, §3-§7)` are the template's sets in range notation; the template's own
  `§` column is honoured by *"each row naming its target HL section"*; column grammar is referenced, not
  restated.
- **Match:** ✅

### V4: `.tfw/templates/RES.md`
- **RF claim:** line 133 only — *"proceed to `/tfw-plan` to update HL and write TS"* → *"…to classify these
  recommendations and write TS"*. `+1 / −1`.
- **Actual:** Line reads `**SUFFICIENT** — proceed to \`/tfw-plan\` to classify these recommendations and
  write TS`. `git show --stat` reports `2 +-` on this file — one line changed, nothing else.
- **Match:** ✅ — the ONB Q2 limit (*"one clause on line 133 and nothing else"*) was honoured.

### V5: `.tfw/templates/HL.md` §3.1
- **RF claim:** §3.1 only; two blocks merged into one; *"Imagine it's done"* → *"Assemble what you would put
  in front of the stakeholder"*; `Nothing Imagined Test` added; 322 → 251 words, file 1,894 → 1,823. All
  four frozen DoD-11 properties survive.
- **Actual:** `git show 4f799c5` touches §3.1 and nothing else in the file. `wc -w` = **1,823**. DoD-11's
  four properties checked clause by clause: (1) *"Working Backwards — from the finished state, as if the
  result already exists"* ✅; (2) rendering list + *"Prose alone is not a rendering"* ✅; (3) *"The value is
  visible in the same picture as the thing that changes"* ✅; (4) *"A multi-phase task labels every change
  with its phase and gives each phase one line saying what it is for"* ✅. The 14-word negation
  (*"A description of the plan that will produce it does not satisfy §3.1"*) is gone by construction, not
  compressed — as claimed.
- **Match:** ✅ on substance. One residue: bullet 2 now lists *"a narrative timeline"* as a rendering in the
  same bullet as *"Prose alone is not a rendering"*. The tension is pre-existing (the old block listed
  `Narrative — timeline of a user's day` as a format option and then said prose was insufficient), but
  merging the lists puts both halves in one sentence. → tech debt, not a finding.

### V6: `phase-b/evidence/EV__phase-b__enforcement_in_workflows.md`
- **RF claim:** environment, 8 evidence rows, verdict, two exhibits.
- **Actual:** Present. 8 rows (E1-E8), verdict `4 VERIFIED / 1 DEFERRED / 3 N/A / 0 BLOCKED`, Exhibit A
  (7-commit history table + 3 named divergences + a practice note) and Exhibit B (word ledger, 13 rows,
  mechanism table, reconciliation, honest-failure note). The three `N/A` rows quote the TS's own
  `Evidence: N/A` text verbatim.
- **Match:** ✅

### V7: `phase-b/evidence/routing_replay.md`
- **RF claim:** all 22 iter2 recommendation rows routed through the shipped step; 19 route, 1 against its
  label, 3 cannot route.
- **Actual:** Present, 22 rows tabulated, arithmetic checks out (1 + 5 + 4 + 2 + 1 + 1 + 3 rows of R-items
  = 17, plus A6/A7/A8 = 20, plus 4 notes counted as 2 routable + … — the table's own row groups sum to 22
  named items). Three findings, each with its reasoning. **The method's circularity is declared first, not
  buried**: *"I wrote the step and I am judging it, so the instrument is circular. The corpus is not."*
- **Match:** ✅

### V8: `.tfw/workflows/review/code.md`, `docs.md`, `spec.md` — **not claimed by the RF**
- **RF claim:** none. RF §3 states *"no file modified outside TS §4's three"*.
- **Actual:** `git show --stat fbdf443` lists six files, not three: the three above are **deleted**
  (`code.md` −15, `docs.md` −12, `spec.md` −12 lines) inside the Phase B commit.
- **Match:** ❌ — see D1.

### V9: `README.md` board row
- **RF claim:** Task Board row — status and the ONB / RF column links (executor-writable).
- **Actual:** `git show --stat 5d264ac` → `README.md | 2 +-`, a single line. Row 301 carries
  `🟢 RF (B) · 📚 KNW (A)` with `B🟠` / `B🟢` links present and resolving.
- **Match:** ✅ — and the single-hunk discipline RF Decision 14 claims **does** hold for this commit.

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python -m pytest docs/scripts/ -q` | **68 passed** in 32.86s — reproduces the RF §4 claim exactly |
| 2 | `grep -n "[Uu]pdate HL" .tfw/workflows/plan.md` | 0 matches — AC-2 gate holds |
| 3 | `grep -rn "[Uu]pdate HL" .tfw/ --include="*.md"` | 0 matches repo-wide, including `CHANGELOG.md` |
| 4 | `grep -niEc "windows\|macos\|linux\|bash\|msys\|powershell\|zsh"` on both workflows | `plan.md:0`, `base.md:0` — AC-5 gate holds |
| 5 | `wc -w .tfw/workflows/plan.md .tfw/workflows/research/base.md` | `1195`, `943` |
| 6 | `git show fbdf443~1:.tfw/workflows/plan.md \| wc -w` | `1206` — the before-figure is real, same command |
| 7 | `git log --format="%h %s" \| grep -E "^\S+ \[[^]]*/TFW-53/freeze/"` | **6** commits — matches RF Decision 8 |
| 8 | `git show --stat fbdf443 / 5d264ac / 4f799c5` | file sets — source of D1 and D2 |
| 9 | `diff` of old vs new `**Gate check:**` block | 1 line differs (the intended one) |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | *"no file modified outside TS §4's three"* | RF §3, DoF clearance line | `git show --stat fbdf443` → 6 files; RF §1's own table → 4 files | ❌ **false on both counts** |
| C2 | *"Only my own paths were staged, and the README hunk was checked before staging"* | RF §2 Decision 14 | True for `5d264ac` (README = 1 line). **False for `fbdf443`**, which carries three foreign deletions | ❌ |
| C3 | *"The recovery form now returns **6** freeze commits"* | RF §2 Decision 8 | Command 7 above → exactly 6 | ✅ |
| C4 | *"Q5 is not [a §12 row]. Q5 is an owner ruling at HL line 724"* | `routing_replay.md` Finding 1 | HL:724 → *"Q5 — is the PV priority-1 relabel in scope… ✅ **travels with TFW-53** — owner, 2026-08-10"*. Not in §12's 13 rows | ✅ — the unlogged frozen-section edit is real |
| C5 | *"`glossary.md`:178 cites 'plan.md Step 6c' twice and still resolves"* | RF §2 Decision 3 | `glossary.md`:178 → two citations of `plan.md Step 6c`; the step number was not moved | ✅ |
| C6 | *"`wc -w` reports 1,206 where the Phase A REVIEW and TD-140/141 report 1,205"* | EV Exhibit B | `TECH_DEBT.md` TD-140 reads *"plan.md 1,205"*; command 6 returns 1,206. Delta declared as frontmatter delimiters | ✅ — and one command used throughout |
| C7 | *"TD-135 does not fire… Phase B appends nothing to `conventions.md`"* | RF §4 | TD-135 trigger is *"re-measure §3 at Phase B before appending"*; `conventions.md` is untouched in all three commits | ✅ |
| C8 | Frozen DoD-11's four properties survive the §3.1 rewrite | RF §2 Decision 13 | Clause-by-clause against HL:581 (DoD-11) — see V5 | ✅ |
| C9 | HL §7.2 / ONB §7 citations resolve | 26 + 4 items | 14 of 14 `D`-numbers spot-checked exist in `KNOWLEDGE.md`; `knowledge/constraint.md` F2 confirms *"degrade at >~1200 words… Working range: 700-900"* | ✅ |

## Discrepancies Found

### D1 — `fbdf443` deleted three files outside TS §4, and no artifact of this phase says so *(High)*

`git show --stat fbdf443` lists six files. Three of them — `.tfw/workflows/review/code.md`, `docs.md`,
`spec.md` — are **deletions belonging to concurrent task TFW-56** ("remove the review mode axis"). They
appear in no RF table, no EV row and no observation. TFW-56's commit `68a8be8` lands **after** `fbdf443`
and does **not** contain them, because they were already gone.

- **TS DoF-4 reads:** *"❌ Any file outside the two named in §4 is modified."* Triggered in letter.
- **Substance is unharmed:** the deletions are TFW-56's own approved work and the end state is correct.
  This executor authored no content change to those files; a directory-level stage (`git add
  .tfw/workflows/`, which reaches `.tfw/workflows/review/*`) is the only mechanism that fits.
- **The trace is harmed:** asking git *"when did TFW-56 remove the mode files"* now returns a commit
  subject reading `[claude-code/TFW-53/phase-b/executor]`.
- **It is already recorded — in the other task.** TFW-56's RF §6 observation 1 and §2 decision 7 describe
  the capture precisely, and its §1 carries a `⚠️` note. So the fact is known to the project; what is
  missing is any acknowledgement in the artifact under review.
- **Sharpest form:** RF §8 S1 argues that under concurrency the commit subject becomes *"the only record of
  which task a change belongs to"* and that no workflow protects the staging step. That insight is correct,
  and the document asserting it also asserts, in Decision 14, that the discipline was kept. It was not.

### D2 — `templates/HL.md` is a fourth modified file, and RF §3 still says "three" *(Medium)*

RF §1's table lists four modified files; RF §3's DoF clearance line says *"no file modified outside TS §4's
three"*. The RF contradicts itself in two sections. The `templates/HL.md` pass itself is properly handled —
owner-authorised, classified against rule 6 before being touched, disclosed as Decision 13, with the RF
stating that adding the TS §4 entry is the coordinator's act. But the clearance line was not updated to
match, so the one line a reviewer reads as a DoF self-check is the one line that is wrong.

### D3 — an authorised removal was not disclosed, against an explicit ONB instruction *(Medium)*

ONB Inconsistency 1: `plan.md`:97 read *"For multi-agent research, see conventions.md §4 (Agent selection
guidance)"* — a reference to a heading D50 deleted. The coordinator ruled: **"Remove it. Authorised, and it
is not a budget trim… State the reason in the RF so the saving is not counted as compression."**

- The line is gone from `plan.md` (verified against `fbdf443~1`, old line 97).
- `grep -niE "agent selection|D50|:97|line 97"` over the RF **and** the EV returns **0 matches**.
- EV Exhibit B's 13-row ledger does not itemise it. Its `Step 6b −38` row describes only *"the six-bullet
  field list"*, which the dead reference is not — so a 9-word correctness fix is either silently folded into
  a duplication row or unaccounted. Exhibit B's own reconciliation carries an unexplained 2-word gap.
- Consequence: the condition attached to the authorisation is unmet, and 9 of the 11 words AC-6 claims came
  from duplication came from a correctness fix instead.

### D4 — RF §2 skips Decision 12 *(Low)*

The decision list runs 1–11, then **13**, 14. `conventions.md` §3 gives the RF priority as source of truth;
a numbering gap in it invites the next reader to hunt for a decision that was never written.

> Escalation applied: on D1 the ratio moved from ⌈7 × 0.42⌉ = 3 to 100% of claimed files, plus the three
> undisclosed ones. All 10 opened.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | AC-1 `N/A — workflow text` | ✅ | ✅ — TS Evidence field is quoted verbatim; the gate result sits in RF §4 |
| E2 | AC-2 grep, inline output | ✅ | ✅ — reproduced independently, 0 matches in `plan.md` and repo-wide |
| E3 | `routing_replay.md` | ✅ | ✅ — 22 rows, 3 findings; circularity declared up front. Finding 1's HL:724 anchor verified (C4) |
| E4 | AC-3 Exhibit A, 7 commits | ✅ | ✅ — 6 `/freeze/` commits reproduced by the documented form; `8136306` confirmed absent from it (divergence 1 real) |
| E5 | AC-3 rejected path — DEFERRED | ✅ | ✅ — blocker named and checkable: 13 §12 rows = 12 `✅ APPROVED` + 1 `🚫 WITHDRAWN`, 0 rejected. Valid DEFERRED per the status vocabulary |
| E6 | AC-4 `N/A — workflow text` | ✅ | ✅ — the character-by-character claim holds (V3) |
| E7 | AC-5 `N/A — a grep is the whole check` | ✅ | ✅ — reproduced, 0/0 |
| E8 | AC-6 Exhibit B word ledger | ✅ | ⚠️ **partial** — both endpoints reproduce exactly (1,206 → 1,195, one command). The ledger is missing the authorised dead-reference removal (D3), and its own reconciliation admits a 2-word gap |

**Totals:** 8 evidence items, 7 verified clean, 1 partial (E8), 0 missing.

## Knowledge Citations Verified

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | HL §7.2 #4-#10, #23, #25, #26 | `KNOWLEDGE.md` D19, D20, D23, D24, D31, D49, D54, D55, D43, D46 | ✅ | ✅ — 14 of 14 spot-checked `D`-numbers present |
| 2 | HL §7.2 #11-#15 | `knowledge/philosophy.md` F4, F13, F21, F22, F25 | ✅ | ✅ |
| 3 | HL §7.2 #16-#19, #24 | `knowledge/process.md` F4, F6, F14, F20, F11 | ✅ | ✅ |
| 4 | HL §7.2 #20 | `knowledge/constraint.md` F2 | ✅ | ✅ — text confirms 700-900 working / >1200 degradation, the figure AC-6 rests on |
| 5 | HL §7.2 #1-#3 | `.tfw/README.md` § Structural Enforcement, § Naming Creates Behavior, § Candor Over Flattery | ✅ | ✅ |
| 6 | ONB §7 new #27-#30 | `KNOWLEDGE.md` D25, D38, D50; `conventions.md` §4 | ✅ | ✅ — D50 is what makes the `plan.md`:97 reference dead (D3) |

**Totals:** 30 citations (26 HL + 4 ONB additions), 30 verified, **0 hallucinations.**

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files and recorded findings? *(10 of 10 — escalated to 100% on D1)*
- [x] Ran at least 1 build/test command? *(pytest 68 passed; 8 further commands logged)*
- [x] Claim & Source Checks filled — 9 claims spot-checked, every citation traced, data claims checked
      against primary sources (`git show`, `wc -w`, `TECH_DEBT.md`, `KNOWLEDGE.md`)?
- [x] Each RF §3 (AC) checkmark verified against actual file? *(AC-1 through AC-6, all six)*
- [x] KNOWLEDGE.md checked — contradictions with changes documented? *(D19 narrowed as designed; D20's
      implicit-approval root cause closed at the workflow site; D23/D24 respected — enforcement-critical
      defaults stayed inline; D38's hard gate byte-identical. No contradiction.)*
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total citations: 30, verified: 30, hallucinations: 0
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 8, verified: 7, partial: 1 (E8), missing: 0

Stage complete: YES

---

## Addendum — owner ruling on D1, and second-pass findings

> Appended 2026-08-13 after the owner reviewed the first pass. The stage log above is left unedited —
> a verification record that is rewritten after the fact is not a record.

### Owner ruling: D1 is waived

Owner, 2026-08-13: *«задача делалась параллельно с 56-й и они там напутали коммиты. можно не обращать
внимание»*. D1's substance is unchanged and TD-144 continues to carry it at High severity from the TFW-56
side. Per the ruling it no longer counts against this phase, and TS DoF-4 is treated as not triggered for
the three `.tfw/workflows/review/*` deletions. D2's remaining half (`templates/HL.md` as an
undeclared-in-TS fourth file, disclosed in RF Decision 13), D3 and D4 stand — they are not commit artifacts.

### F1 — the tripwire, the only part of rule 6 that changes an outcome, is not inline *(the strongest finding)*

Step 6c item 3 says *"Classify… by its target section and `conventions.md` §3 rule 6"* and then states the
two destinations. Rule 6 has two halves, and only the second discriminates:

| Rule 6, half 1 | Rule 6, half 2 — the tripwire |
|---|---|
| *"Deliverable lists inside an already-approved phase are free"* | *"if the change cannot be accepted under §5 and §6 **as they stand at the moment of classification**, it is an amendment"* |
| Inline in the step, as *"a free unit inside a frozen one → apply it"* | **Not inline. Reference only.** |

`routing_replay.md` measures the split: of 22 real recommendation rows, **21 route identically with or
without the tripwire; exactly 1 routes differently** — R26 item (2) — and that one is a live unlogged edit
to a frozen section (verified independently at HL:724, check C4). So the single row on which the step earns
its existence is decided by text the step does not contain.

`conventions.md` §11 Design Rules is explicit: *"enforcement-critical values MUST be inline (Pattern A:
defaults + config key). Pure refs (Pattern B) = broken."* By the replay's own measurement the tripwire is
the enforcement-critical half.

**The trade is real, not an oversight.** AC-6 leaves 5 words of headroom against F2's 1,200; the missing
clause costs ~10. DoF-2 forbids trimming a mechanism to buy them. The executor was inside a vice with no
compliant exit, and did not paper over it. **Owner decision, not an executor defect.**

The mirror image of the same trade: `research/base.md` spent **+74 words** restating class definitions that
`templates/RES.md` already carries in full and that the researcher opens anyway — 0 of 22 rows depend on
that restatement. Word budget was allocated inversely to measured value across the two files.

### F2 — applying a refinement to a frozen section produces no record, so the salami pattern stays invisible

Step 6c item 3's free-unit branch reads *"→ apply it"* and requires nothing else. No log line, no marker.

HL §12's own note block states the risk in the first person: *"§3.1 rendered three times without amendment…
three edits to a frozen section under a refinement label is the salami pattern this task tracks, **and the
reviewer should check the classification rather than accept it**."*

The reviewer has nothing to check. N successive refinements to §4's deliverable lists leave zero trace, by
design of the shipped step. Not an executor defect either — AC-2 and frozen DoD-13 require applying
refinements and require no record of it. **Contract-level gap, surfaced by the mechanism working.**

### F3 — the interruption budget is protected on one channel out of four

AC-2's batching clause (*"Escalate once per iteration"*) governs research output. 6d correctly handles a
verdict *arriving* from any channel. Nothing governs **filing** outside the research loop:

| Channel | §12 rows | Filing discipline shipped |
|---|---|---|
| research iteration (A1–A8) | 8 | ✅ one message per iteration |
| executor ONB (A10, A13) | 2 | ✗ none |
| owner during execution (A9, A12) | 2 | ✗ none |
| review finding | 0 | ✗ none |

**4 of 13 rows arrived through channels with no batching rule.** HL §11 S29 records that the owner's
interruption budget is spent on *frequency, not authority*, and that the design's success metric is
proposals-per-iteration — so the unprotected channels are load-bearing for the task's own stated metric.
`handoff.md` and `review.md` are outside TS §2, so this is input for a later phase, not a Phase B debt.

### F4 — the step's paraphrase of rule 6 is broader than rule 6

The step generalises to *"a free unit inside a frozen one"*. Rule 6 names exactly one free unit: a
deliverable list inside an already-approved phase. The paraphrase saves no reading (the coordinator must
open rule 6 regardless, since the step does not enumerate free units) and widens the boundary on a first
read — in the direction of treating frozen text as free, which is the failure mode the task exists to stop.

### F5 — "no further measured duplication exists" is not established

EV Exhibit B asserts that the remaining large blocks are each *"the sole statement of their mechanism"*.
Counterexample found in one pass:

| `plan.md` Step 2 (77 words total) | `glossary.md`:213 |
|---|---|
| `hard` → HARD STOP + justification | *"`hard` (stop + justification)"* |
| `soft` → reminder | *"`soft` (reminder only)"* |
| `off` → skip silently | *"`off` (skip)"* |

~50 words of the three mode behaviours exist in both places. It does not reach the 700-900 range, but it
turns *"nothing left to remove"* from a measured fact into an unverified assertion — which is the claim
AC-6's shortfall report rests on.

Adjacent defect found in the same check: `glossary.md`:213 places the Knowledge Gate in *"Phase 0 of
`plan.md`"*. `plan.md` has Steps 0–7 and no Phase 0; the gate is Step 2. A stale cross-reference in a file
Phase D owns.

Addendum complete: YES
