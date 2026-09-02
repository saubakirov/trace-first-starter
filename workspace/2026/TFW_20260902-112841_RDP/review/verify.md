# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: **0.42** (`.tfw/project_config.yaml` → `tfw.review.min_verify_ratio`)
> RF files claimed: **16** modified outside the task directory (+ 4 created inside it, + 9 declared no-ops)
> Files to verify: ⌈16 × 0.42⌉ = **7** → **escalated to 16/16 (100 %)** on the V8 discrepancy, plus all 9 no-ops

## Verification Log

### V1: `.tfw/workflows/review.md`
- **RF claim:** Steps 4–6 rewritten at **480** against a 483 baseline; Anti-patterns **160** against 163; frontmatter `description` corrected; whole file 1 702 against 1 706; six new mechanisms; two Anti-patterns removed.
- **Actual:** Every figure reproduces to the word against `1f5f578^`. Per-step split reproduces too — baseline 116/299/68 and shipped 148/212/120, exactly `word_budget.md`'s table. Step 5 is the five-act table (Filter · Axis · Test · Route · Propose); Step 6 opens *"The coordinator rules every proposed disposition — one act at the close"*; Step 4 carries the `Max revision cycles | 2 | Hard | tfw.review.max_revision_cycles` row and the pre-REVISE count instruction. `description` reads *"proposes a disposition per finding"*.
- **Match:** ✅

### V2: `.tfw/conventions.md`
- **RF claim:** §5 gains *The 🔄 REVISE route* (rung table, `revision` defined, budget, return); diagram label → *(routed by rung)*; verdict list routes per item; §14 gains two anti-patterns; §15's `review.md` row names acceptance authority and forbids `disposition rulings`, with a paragraph above the table.
- **Actual:** All present and as described. §5 measured **952 → 1 433**. The rung table gives all three rungs a destination and states *"a rung is a property of the item; `lifecycle` is a property of the task."* §14's two new lines are the rung-2-into-the-executor-list failure and the exhausted-budget-still-looping failure — neither is covered by any role list. §15's row and the paragraph above it are as claimed.
- **Match:** ✅

### V3: `.tfw/workflows/handoff.md`
- **RF claim:** *Returning after a 🔄 REVISE* added; Context Loading gains the prior REVIEW as item 8 and runs to ten.
- **Actual:** Both present. The new section names the read order, what is not re-done, the round's artifacts as **appended / sibling / never-overwritten** (HL DoD 9), what is not the executor's, and where the bound lives without saying what it says. Context Loading runs 1–10 with the prior REVIEW at 8.
- **Match:** ✅

### V4: `.tfw/templates/REVIEW.md`
- **RF claim:** §5 carries the ruling's grammar, `pending — coordinator` beside `pending — owner`, the example row rewritten, and the relocated project-wide search; §3 row 3 mirrors `judge.md`.
- **Actual:** All present. The grammar paragraph states the consequence rule and both questions with the barring-clause requirement. The example row now reads `not material — not owed: {the consequence that will not follow}`. The search block is verbatim the block removed from `review.md`, with **253** substituted for 252.
- **Match:** ✅

### V5: `.tfw/templates/review/judge.md`
- **RF claim:** Row 3 checks the grammar and names the coordinator; Checkpoint line follows; **no row added** — 10 before, 10 after.
- **Actual:** Row 3 rewritten as claimed; checkpoint bullet updated. Row count 10 before and 10 after, confirmed by reading both versions.
- **Match:** ✅

### V6: `.tfw/project_config.yaml` · `.tfw/templates/project_config.yaml`
- **RF claim:** One key each, same key, three-line comment defining the unit; both files re-parse.
- **Actual:** Four added lines per file — a three-line comment plus `max_revision_cycles: 2`. Both parse: `{'min_verify_ratio': 0.42, 'max_revision_cycles': 2}`, identical in both. One key, no second.
- **Match:** ✅

### V7: `.tfw/glossary.md`  ⚠️
- **RF claim:** *"Three terms: `Revision`, `Revision budget`, `Rung`."* AC-10 requires `glossary.md` to **carry the change**; TS §2 puts the file in scope.
- **Actual:** The three new terms are present, accurate and cross-referenced to `conventions.md` §5. **But the two existing entries the change contradicts were not touched:**
  - `glossary.md:186` — `## Reviewer`: *"Triages executor Observations into REVIEW §5 and **disposes of every one** before the task closes."*
  - `glossary.md:324` — `## Disposition`: *"`pending — owner` is a legal waiting state, not a fourth outcome. → `.tfw/workflows/review.md` Step 5"* — no coordinator, no `pending — coordinator`, and the pointer aims at a step that no longer holds the outcome definitions.
- **Match:** ⚠️ **partial.** The additions are correct; the file does not carry the change. See D1 and D2.

### V8: `.tfw/CHANGELOG.md`  ⚠️
- **RF claim:** Second headline block, nine changed items, **ten verbatim retired-wording entries**; two existing lines corrected (the search's location and its row count).
- **Actual:** Nine added bullets carrying ten quoted strings — the count is honest. Both corrections are in: line 55 relocates the search to `templates/REVIEW.md` §5 and states **253** with its date. Spot-checked three quoted strings against `1f5f578^`; all three are byte-verbatim, so `update.md` Step 6's allowlist can fire on them. **One claim in the entry does not hold:** the retired-wording bullet says the two Anti-patterns were *"removed from `review.md`'s Anti-patterns as **verbatim duplicates** of `conventions.md` §14 … Nothing was lost."* One is verbatim (`conventions.md:902`); the other is not — §14:901 reads *"Executor writes REVIEW file → **Role Lock violation**"* against `review.md`'s *"Executor writes REVIEW file — **🔒 Role Lock violation** (start `/tfw-review` instead)"*. The remedial clause is now in neither list.
- **Match:** ⚠️ **partial.** See D3.

### V9: `KNOWLEDGE.md`  ⚠️
- **RF claim:** §1 Debt row rewritten + new Correction Loop row; §1 D72; §2 task row; §3 one row for what this retires.
- **Actual:** All four present and substantively accurate. **But §3's pre-existing row 173** — TLD's registry retirement — still reads *"Discovery is one search over REVIEW files, written out in `review.md` Step 5 and measured at 243 rows."* Both facts are the two the TS ordered corrected in the CHANGELOG (§4 authorisations 1 and 3), and the executor edited §3 in the same act.
- **Match:** ⚠️ **partial.** See D4.

### V10–V15: the six adapter copies
- **RF claim:** Six whole copies re-synced, each `cmp`-verified; `.agents/skills/tfw-review/SKILL.md` a genuine no-op absent from `git status`.
- **Actual:** `cmp` run independently on all six pairs — all identical. `.agents/skills/tfw-review/SKILL.md` matches its source and is absent from the commit. Its `## Contract` block names no rule this task changed; the `tfw-handoff` pair's does, and gained the prior REVIEW in both source and copy.
- **Match:** ✅

### V16: `workspace/…/status.md` + `journal/20260902-143632__transition__845e.md`
- **RF claim:** `ONB` → `RF` transition recorded.
- **Actual:** `lifecycle: RF`, `updated: 20260902-143632`; the event carries `kind: transition`, `on_behalf_of: saubakirov`, `via: claude-code`, `from: ONB`, `to: RF`, refs and summary. Schema-valid.
- **Match:** ✅

### V17: the nine declared no-ops
- **RF claim:** Two `tfw-review` SKILL copies, four marker files, three READMEs — all genuine no-ops, none manufactured into an edit.
- **Actual:** `grep -icE 'revise|revision|disposi|debt|rung|acceptance authority|max_revision'` returns **0** on all four marker files. The three READMEs were read, not grepped: `README.md:265` and the parallel `README.ru.md:154` / `README.kk.md:154` blocks state the three outcomes and disposal-before-closing — both still true — and none names who rules, the routing, or the budget. Neither `tfw-review` SKILL appears in the commit. **Nine no-ops, nine confirmed, zero manufactured edits.**
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | ✅ **322 passed, 1 skipped in 267.11s**, exit 0 — reproduces the RF's 322/1 |
| 2 | `python .tfw/scripts/gen_index.py --check tasks` | ✅ *58 tasks validate against the closed schema*; the same 17 informational legacy notes |
| 3 | `python .tfw/scripts/gen_index.py --check project` | ✅ *project is consistent with the release it declares* |
| 4 | The three AC-1 `awk … \| wc -w` gates, before and after | ✅ 483→**480**, 163→**160**, 952→**1 433**, 1 706→**1 702** |
| 5 | Per-step `awk` split, before and after | ✅ 116/299/68 → 148/212/120 — `word_budget.md`'s table to the word |
| 6 | The relocated debt search, from the project root | ✅ **253 rows** — the shipped figure, not 243 and not 252 |
| 7 | `grep -rn 'max_revision_cycles' .tfw/ \| grep -v adapters` | ✅ Byte-identical to the RF's pasted output; every prose site pairs the key with *default 2* |
| 8 | `grep -c revision` on the three canon files | ✅ 1 / 2 / 5 after, **0 / 0 / 0** before |
| 9 | `grep -n '\$[0-9]\|\$ARGUMENTS'` on `review.md` and `templates/REVIEW.md` | ✅ empty — the `$N` hazard is clean in both |
| 10 | `cmp` on all six source/copy pairs | ✅ six OK |
| 11 | CRLF sweep over all 22 committed files | ✅ none — every file is LF, as Decision 10 claims |
| 12 | `yaml.safe_load` on both config files | ✅ `{'min_verify_ratio': 0.42, 'max_revision_cycles': 2}` in both |
| 13 | `git status --short -- tasks/AFD-48…` in `ai-first-devices` | ✅ **empty** — the external tree was not written; its four pre-existing dirty entries are exactly the four the RF declares |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | The axis *"purpose, inspectability, authority or continuation"*, cited to `NS1` | `review.md` Step 5, Axis row, link `../README.md#ns1` | `.tfw/README.md:72` carries `<a id="ns1"></a>`; the paragraph reads *"understand what the work is for, **inspect** its material grounds…, see where **authority** remains, and **continue**"*. The anchor resolves and the four words are the clause's own | ✅ |
| C2 | *"Item 3 returns in rev2, rev3 and rev4 with no amendment ever logged"* — the load-bearing empirical claim for rung 2 | RF §1 commit body; `replays.md` Replay 2 | Opened all three files in `ai-first-devices`. rev2 item 3 *"Obtain coordinator amendments"*; rev3 item 2 *"The coordinator must explicitly rule on (a)… and (b)…"*; rev4 item 3 plus *"Reviewer cannot self-amend TS"*. The phase directory holds no `journal/`. **Reproduces exactly** | ✅ |
| C3 | *"3 of 9 TLD dispositions change substantively — rows 3, 5 and 7"* (DoD 14's answer) | RF §3 DoD 14; `replays.md` Replay 1 | Read TLD's REVIEW §5 whole. Nine rows. Rows 3, 5 and 7 each argue the fix is barred — by AC-1, by DoF 10, by *"HL DoF 5 and TS §2 forbid outright"* — and each is filed as bare `not material`. All three are *owed and forbidden to pay* misfiled as *not owed*. **The population is complete, not sampled, and the classification holds row for row** | ✅ |
| C4 | *"Two Anti-patterns removed as **verbatim** duplicates of `conventions.md` §14"* | RF Decision 9 · `word_budget.md` subtraction 8 · shipped `.tfw/CHANGELOG.md` | §14:902 is verbatim. §14:901 is **not** — it lacks *"(start `/tfw-review` instead)"* and uses `→` where `review.md` used `— **🔒 …**` | ❌ — see D3 |
| C5 | *"`revision` appeared **zero** times before"* | RF §3 AC-8, `glossary.md`, CHANGELOG | `grep -c revision` on the three files at `1f5f578^`: 0, 0, 0 | ✅ |
| C6 | *"10 tasks `owner: saubakirov`, 10 `owner: unassigned`, one `team/` profile and it is `type: human`"* | `replays.md` Replay 3 | Re-ran both greps: 10 / 10, and one `type: human`. `type: agent` therefore has no live instance, as stated | ✅ |
| C7 | *"No owner is named anywhere in the canon"* (DoF 4) | RF §4, AC-7's gate | The only `saubakirov` hit under `.tfw/` is the pre-existing deploy URL at `CHANGELOG.md:1398`, shifted from 1320 by the new entry. No handle introduced | ✅ |
| C8 | The honest draft measured **753** words (+56 %) | RF Decision 1, `word_budget.md` | **Not independently reproducible** — an intermediate draft leaves no artifact. The two figures that bind (baseline and shipped) both reproduce exactly, and the eight named subtractions sum plausibly to the gap. Accepted as a self-report with its limits stated | ⚠️ |

## Discrepancies Found

**D1 — `glossary.md` still grants the reviewer disposition authority.** `.tfw/glossary.md:186`, the
`Reviewer` entry, reads *"Triages executor Observations into REVIEW §5 and **disposes of every one**
before the task closes."* HL DoF 5 (frozen) names *"the reviewer retains disposition authority anywhere
in the canon"* as a failure, and DoD 5 (frozen) requires the reviewer to rule dispositions **nowhere** in
it. `glossary.md` is canon — `conventions.md` §2 lists it in the core spec, `KNOWLEDGE.md` §1 files it
under *TFW Core*, `conventions.md:100` calls it PV priority 0, and every workflow loads it as context
item 3, **before** the workflow itself. The same false sentence class was corrected two files away:
`review.md`'s frontmatter *"disposes of debt"* was fixed under TS §4 authorisation 2 precisely because it
*"becomes false under AC-5."*

**D2 — `glossary.md`'s `Disposition` entry is stale in three ways.** `.tfw/glossary.md:324` names
`pending — owner` as the only waiting state, when this release makes `pending — coordinator` the ordinary
one; names no ruler, when naming the ruler is the task's AC-5; and points to *"`.tfw/workflows/review.md`
Step 5"* for a grammar and an outcome list that now live in `templates/REVIEW.md` §5.

**D3 — a shipped claim is wider than its evidence.** *"Verbatim duplicates of `conventions.md` §14 …
Nothing was lost"* is true of one removed Anti-pattern and not of the other; `(start /tfw-review
instead)` now appears in neither list. The claim is in the released `.tfw/CHANGELOG.md`, in RF Decision 9
and in `evidence/word_budget.md`.

**D4 — two facts the TS ordered corrected were corrected in one file and left in another.**
`KNOWLEDGE.md:173` still reads *"…written out in `review.md` Step 5 and measured at 243 rows."* TS §4
authorisations 1 and 3 ordered both corrected; the CHANGELOG carries both fixes and `KNOWLEDGE.md` §3 —
edited in the same act — carries neither.

> Escalated to 100 % verification on D3. All 16 modified files and all 9 declared no-ops opened.
> No further discrepancy found: the mechanism itself is sound and the measurements are honest.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | `evidence/EV__TFW_20260902-112841_RDP.md` | ✅ | ✅ — environment header, 11-row per-AC table, inline output, verdict. Every N/A is one the TS itself declared |
| E2 | `evidence/word_budget.md` | ✅ | ✅ — all four gate figures and the per-step split reproduce **to the word**; eight subtractions each carry a justification. One nit: the *"no `$N` in the file"* line greps for the literal phrase *"positional parameter placeholders"*, which is not that check — the real check is pasted in RF §4 and I re-ran it clean |
| E3 | `evidence/replays.md` Replay 1 (AC-3) | ✅ | ✅ — complete nine-row population, not a sample; the three substantive changes reproduce row for row against TLD's closed REVIEW |
| E4 | `evidence/replays.md` Replay 2 (AC-4) | ✅ | ✅ — AFD-48 rev2's six items are as quoted; the 4/2 rung split is defensible on the text; the rev2/rev3/rev4 recurrence and the absent journal both confirmed; the external tree is unwritten |
| E5 | `evidence/replays.md` Replay 3 (AC-7) | ✅ | ✅ — owner census 10/10 and the single `type: human` profile both re-run; the closed `kind` vocabulary confirmed verbatim in `templates/journal/event.md` |
| E6 | `evidence/replays.md` Replay 4 (AC-8) | ✅ | ✅ — and it is the most useful of the four: it reports that TLD's revision count is **zero**, which is a result against the executor's own convenience |
| E7 | RF §4 inline gates (AC-1, AC-6, AC-7, AC-8, AC-9, `$N`, `cmp`) | ✅ inline | ✅ — every one re-run independently; all reproduce |

## Knowledge Citations Verified

> HL §7.2 carries **27** rows. PV 0–4 verified in full; PV 6–7 verified by relevance (all of them — there
> are only six such rows and each is load-bearing for an AC).

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1–2 | HL §7.2 #1, #2 | PV 0 — `NS1`, ¶1 four words and ¶2 *"polished and technically correct"* | ✅ `#ns1` at `.tfw/README.md:72` | ✅ | ✅ both quoted verbatim | ✅ the axis and the reason a fourth round is drift |
| 3–6 | HL §7.2 #3–#6 | PV 0 — `NS2` principles 4, 5, 6 and the closing test | ✅ `#ns2` at :79 | ✅ | ✅ all four verbatim; principle 4 is literally *"acceptance authority"* | ✅ AC-5, AC-7, proportional routing, DoF 3 |
| 7 | HL §7.2 #7 | PV 0 — `NS3` *"maximum-documentation bureaucracy… measures success by artifact count"* | ✅ `#ns3` at :103 | ✅ :111 | ✅ | ✅ AC-9 |
| 8–10 | HL §7.2 #8–#10 | PV 1 — Structural Enforcement · Naming Creates Behavior · Candor Over Flattery | ✅ `#methodology-values` at :91 | ✅ | ✅ all three verbatim | ✅ checked **separately** from priority 0 though both live in `.tfw/README.md` |
| 11–15 | HL §7.2 #11–#15 | PV 2 — `philosophy.md` F42, F40, F25, F43, F36 | ✅ | ✅ rows 49, 47, 32, 50, 43 | ✅ every quotation matches its row | ✅ the materiality bar, the compression method, decision-infrastructure, architecture-over-fixes, the orthogonal axes |
| 16–19 | HL §7.2 #16–#19 | PV 3 — `KNOWLEDGE.md` D64, D63, D13, D65 | ✅ | ✅ | ✅ | ✅ cite-don't-assert, the frozen contract, review-split-from-handoff, the rejected trace survives |
| 20–21 | HL §7.2 #20–#21 | PV 4 — `conventions.md` §11 *"≤1200 words"* and §14 firing-rate rule | ✅ | ✅ :858, :903 | ✅ | ✅ DoD 10 and AC-3's *no row added* |
| 22, 25 | HL §7.2 #22, #25 | PV 7 — `conventions.md` §15 Role Lock and §5 verdict routes | ✅ | ✅ | ✅ | ✅ the row edited under AC-5 and the site extended under AC-4 |
| 23–24 | HL §7.2 #23–#24 | PV 6 — `process.md` F30, F14 | ✅ | ✅ rows 37, 21 | ✅ | ✅ Principle 7; the round count needs a structural home |
| 26–27 | HL §7.2 #26, #27 | PV 7 — `templates/REVIEW.md` §5 `pending — owner`; `templates/journal/event.md` closed vocabulary | ✅ | ✅ | ✅ — #26's quoted sentence has since been **superseded by this very task**, which is expected, not a defect | ✅ the delivery channel and the closed `kind` list |

**On the priority labels.** HL §7.2's closing note records that four rows carried a PV-4 label the PV
Index does not support and were moved to PV 7 after the executor's ONB. I re-derived the Index from
`glossary.md` and the correction is right: §5, §15 and `templates/` are not PV-4 sources. **This is the
opposite of a citation defect — the executor found and fixed a coordinator labelling error before a
reviewer could escalate on it.** ONB §7 records all 27 rows read individually, with line numbers; my
sample corroborates every one I checked.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files and recorded findings? — **16/16 plus all 9 no-ops (100 %, escalated)**
- [x] Ran at least 1 build/test command? — 13 commands, including the full suite at 267 s
- [x] Claim & Source Checks filled — 8 claims spot-checked, every citation traced, the two load-bearing data claims (C2, C3) checked against their primary sources in two repositories
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented? — **yes: D4**
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total: **27**, resolved: **27**, semantically verified: **27**, irrelevant: **0**, hallucinated: **0**
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: **11** (7 VERIFIED, 4 N/A), verified: **11**, missing: **0**

Stage complete: YES
