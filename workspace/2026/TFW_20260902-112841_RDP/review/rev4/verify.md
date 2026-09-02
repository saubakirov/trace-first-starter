# Verify — "Are the claims true?" — round 4

> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims
> against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: **0.42** (`tfw.review.min_verify_ratio` default; `project_config.yaml` sets no override)
> RF files claimed: **4** — `docs/scripts/test_integration.py`, `.tfw/glossary.md`, `KNOWLEDGE.md`,
> `.tfw/CHANGELOG.md`
> Files to verify: ⌈4 × 0.42⌉ = **2**. **Verified: 4 of 4 — 100%**, plus ten forbidden paths, three
> out-of-scope files, `plan.md`, `handoff.md`, `release.md` and the whole journal corpus.
> **Escalated to 100% by discrepancy D1** (below), and it would have been 100% regardless: a four-file
> round is cheaper to audit whole than to sample.

## Verification Log

### V1: `docs/scripts/test_integration.py`
- **RF claim** (§1.4 row 1, §3.4 item 1): `DOUBLED_SLUG`'s lookahead gains `\.md` so the mandated ordinal
  must **end** the name; a third assertion places a suffix *after* the ordinal; the comment carries the
  reason; the other three regexes and both surviving negatives untouched; +8 −3, two hunks.
- **Actual:** `git diff 859dc74 13f6d9b` on the file is exactly two hunks.
  `DOUBLED_SLUG = re.compile(r"\{ID\}__(?!rev\{N\}\.md)")` replaces `r"\{ID\}__(?!rev\{N\})"`. The
  comment above it now states *"the lookahead spells `rev{N}.md`, not `rev{N}`, because the ordinal must
  **end** the name"* and names the escaping example. One line added to
  `test_the_naming_detectors_actually_fire`:
  `assert DOUBLED_SLUG.search("TS__{ID}__rev{N}__extra.md")  # a suffix AFTER the ordinal`.
  `BARE_ID_AS_NAME`, `ACTORLESS_EVENT`, `STAMP`, `BACKTICKED` and both surviving negative assertions do
  not appear in either hunk.
- **Independently re-derived, not read:** the two expressions were imported and called directly over nine
  probe names. `TS__{ID}__rev{N}__extra.md` → old **False**, new **True**. The mandated form
  `TS__{ID}__rev{N}.md` → **False under both**, so the exception survives and this is a repair, not a
  widening. Character delta measured: `len(r"\{ID\}__(?!rev\{N\}\.md)") - len(r"\{ID\}__(?!rev\{N\})")`
  = **24 − 20 = 4**.
- **The gate that mattered most, re-proven here:** under the **old** expression the new assertion's
  subject returns `None`, so the assertion fails. The test can fail against the defect it guards — which
  is what round 3's two assertions could not do, and the whole reason this item existed.
- **Match:** ✅

### V2: `.tfw/glossary.md`
- **RF claim** (§1.4 row 2): `Execution Loop` — *Phase 2 Step 8* → *Phase 2, `Implement`*, +1 −1. Gate
  reported **NOT MET**: one `handoff.md` step number survives at line 215.
- **Actual:** the diff is one line. Line 206 now ends `→ `handoff.md` Phase 2, *Implement*`.
  `grep -n "Step [0-9]" .tfw/glossary.md` returns six lines; of those, exactly **one** cites `handoff.md`
  — line 215, `Session Naming`: *"→ `handoff.md` Step 0, `plan.md` Step 0, `review.md` Step 0"*. The
  others cite `review.md` Step 3, `plan.md` Step 7/6b/6c and `research/base.md` Step 5, which item 2's
  gate does not reach.
- **The executor's three grounds, checked one at a time rather than accepted:**
  (a) *it did not drift* — **true.** Round 3 renumbered `handoff.md` steps 8–13; Step 0 is at line 16 and
  was never in that range.
  (b) *`## Step 0: Name This Session` is a real heading rather than a count* — **true for two of the three
  workflows cited.** `handoff.md:16` and `review.md:16` both carry that exact `##` heading.
  (c) *the number is part of the glossary term itself, and de-numbering would reach `plan.md` and
  `review.md`* — **true.** The entry's first words are *"Step 0 convention present in every TFW
  workflow"*; the number is the definiendum, not a locator into a renumbered list.
- **What the executor's own argument did not check, and I did** — see **D2**: `plan.md` has **no Step 0**,
  at any revision including the HL baseline, and says so on purpose at line 84: *"This is step 3 and not
  step 0 deliberately."* So one third of that line's locator list resolves to nothing, and the entry's
  opening universal claim is false. This does **not** rescue the gate as written and does not change my
  ruling on it — it is a *separate*, pre-existing defect, and it is routed as such.
- **Match:** ✅ for the ordered edit · ⚠️ the gate is unmet as literally written, disclosed by the
  executor, ruled in `judge.md` row 2

### V3: `KNOWLEDGE.md`
- **RF claim** (§1.4 row 3, §3.4 item 3): **D52** — *handoff Step 11* → *handoff `Collect evidence`*;
  nothing else touched; 1 insertion, 1 deletion.
- **Actual:** the diff is exactly one line — D52's cell, `(RF §5 Evidence table, handoff *Collect
  evidence*)` replacing `(RF §5 Evidence table, handoff Step 11)`. §2's `TFW-46` row at line 147 still
  reads *"handoff Step 11"* and is **correctly** untouched: TS revision 4 §5 item 3 bullet 3 and §7 both
  name it as history that is not to be repaired.
- **The stated consequence checked against the primary source, not the RF:** the claim is that D52 is
  **PV priority 3**. `glossary.md` § *PV Index (scan order)* row 3 is `KNOWLEDGE.md` **§1 — Architecture
  Decisions (D-records)**; D52 is a D-record in §1. The same table's *Who scans PV* block requires the
  **coordinator** to scan priorities 0–4 **in full** before planning. So the consequence the order and the
  prior review both asserted — a wrong locator here is an input to every future plan — is real and
  verified at its source. It also means the repair was correctly ranked above item 2's.
- **Match:** ✅

### V4: `.tfw/CHANGELOG.md`
- **RF claim** (§1.4 rows 3–4, §3.4 items 3–4): the round-3 bullet reports **four** live citations and
  names all four; `### Removed` gains the un-gating with the receiver instruction, its mechanism and the
  one-sentence reason; `### Known open at this tag` records that the malformed event was **not** repaired.
- **Actual, bullet by bullet:** the round-3 bullet now reads *"the **four** live citations of those
  numbers — `glossary.md`'s `Evidence Collection`, `Pre-RF Gate` and `Execution Loop`, and this
  repository's `KNOWLEDGE.md` **D52**"*, and adds *"Search rather than recall: the first pass here named
  the two it remembered."* The `### Removed` bullet names the key gone from **both** config files, the
  `Verify` line, the `test_gen_index.py` assertion and what that test still owns; gives the reason in one
  sentence (*"a never-authoritative view must not stand in a blocking check, because one malformed line in
  one task then stops every unrelated run"*); states `gen_index.py` is untouched and still reports; and
  carries the receiver instruction *"if your own `project_config.yaml` carries a `build.verify` that names
  this check, **remove it**"* with the mechanism (`build.*` is a PROJECT section an update preserves). The
  `Known open` bullet states 123 code points against 120, *"and it was not repaired"*, the owner's ruling
  that the event is not edited and the ceiling not moved, and that the check *"still exits 1 … alongside
  whatever else the corpus holds at the time you run it."* **No claim that the event was repaired.**
- **Match:** ⚠️ **partial — see D1.** Every ordered element is present and accurate. One figure inside the
  `Known open` bullet is wrong: *"the only event over the ceiling among the **116** in this corpus that
  carry a summary."*

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | **322 passed, 1 skipped in 152.52s, exit 0.** Matches the RF's figure exactly. AC-11 bullet 1 **verified**, not taken on report |
| 2 | old vs new `DOUBLED_SLUG` imported and called over nine probe names | mandated form refused-free under both; `…rev{N}__extra.md` and `…rev{N}extra.md` differ. The new assertion **fails** under the old expression |
| 3 | `python .tfw/scripts/gen_index.py --check tasks; echo $?` | **exit 1**, *"1 problem(s) across 61 tasks"*, naming the 123-code-point summary. Expected per the owner's ruling; **61 tasks confirms the RF's correction from 56** |
| 4 | `git diff --quiet 859dc74 HEAD -- <path>` over ten forbidden paths | **all ten IDENTICAL**: `gen_index.py`, `review.md`, `handoff.md`, `templates/REVIEW.md`, `conventions.md`, the journal event, both `project_config.yaml`, `templates/RF.md`, `test_gen_index.py` |
| 5 | `git diff 1c7b55e HEAD -- <the HL>` | **empty** — the contract is frozen and unmoved at its baseline |
| 6 | `git diff --name-only 859dc74 HEAD` | 18 paths: 4 payload + 7 this task's own artifacts + **7 belonging to two other sessions** (RCFR, RTBO). The RF's "seven more paths" is exact |
| 7 | `git status --porcelain` | only ` M .gitignore` — a neighbouring session's, in no commit of this round. Confirms the RF's shared-tree discipline claim |
| 8 | journal corpus scan at `859dc74`, `1a9059b`, `13f6d9b`, `HEAD` — events carrying a `summary`, and events over 120 | **114 / 117 / 118 / 118** carrying a summary; **1** over the ceiling at every revision. Re-run by a second method at `1a9059b`: **117 events, 117 with a summary, 0 without.** The shipped figure is **116** → **D1** |
| 9 | `git grep -nE` for `handoff` step numbers, project-wide | every hit outside `.tfw/glossary.md:215` and `KNOWLEDGE.md:147` is a released CHANGELOG entry or the frozen `tasks/` corpus — i.e. history, as claimed |
| 10 | `grep -n "Step 0" .tfw/workflows/*.md` | `handoff.md:16`, `review.md:16`, `update.md` ×2. **`plan.md` absent** → **D2** |
| 11 | `git show 1c7b55e:.tfw/workflows/plan.md \| grep -n "Step 0"` | line 84, *"This is step 3 and not step 0 deliberately"* — **the defect predates this task entirely** |
| 12 | `git show 859dc74^:.tfw/templates/project_config.yaml` `build:` block | the removed `verify` was annotated *"A real command, not a placeholder … works from the moment the payload lands"* — **confirms RF §6.4 row 5 exactly** |
| 13 | `grep -n` over `.tfw/workflows/release.md` for a re-measurement step | **none exists.** Step 7 asks for *"accurate content"* as prose; nothing re-measures a corpus count. Bears on D1's consequence and on §5 row 3 |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|---|---|---|---|
| C1 | *"the addition is four characters, `\.md`, not the three both the review and the TS call it"* | RF §2.4 dec. 5, EV E25 | Measured: 24 − 20 = **4**. TS rev4 §5 item 1 and REVIEW rev3 §5 row 5 both say *three* | ✅ — **the executor is right and its own order was wrong** |
| C2 | *"the corpus is **61** tasks, not 56"* | RF §2.4 dec. 4, EV E28 | `gen_index.py --check tasks` run here: *"1 problem(s) across **61** tasks"* | ✅ |
| C3 | *"byte-identity … measured against `859dc74`, not the HL baseline `1c7b55e`"* | RF §4.4, EV round-4 header | Verified both ways: all ten paths identical vs `859dc74`; and `review.md`/`handoff.md`/`templates/REVIEW.md`/`conventions.md` **do** differ from `1c7b55e` by rounds 1–3's approved deliveries. The reference revision is the correct one and naming it was necessary | ✅ |
| C4 | *"the only event over the ceiling among the **116** in this corpus that carry a summary"* | `.tfw/CHANGELOG.md`, `Known open at this tag` — **shipped** | Two independent counts: **117** at `1a9059b`, the commit that ships the bullet; **118** at HEAD; 114 at dispatch. **116 matches no revision.** The over-ceiling count, **1**, is correct and stable | ❌ → **D1** |
| C5 | *"`## Step 0: Name This Session` is a real heading"*, cited for three workflows | RF §2.4 dec. 3, ONB §10.5 item 2, EV E26 | `handoff.md:16` ✅, `review.md:16` ✅, **`plan.md` — no such heading at any revision** | ⚠️ — true for two of three → **D2** |
| C6 | *"D52 is **PV priority 3** — scanned in full by every coordinator before planning"* | TS rev4 §5 item 3, RF §3.4 | `glossary.md` § PV Index row 3 = `KNOWLEDGE.md` §1 D-records; *Who scans PV* = coordinator, priorities 0–4 **in full** | ✅ |
| C7 | *"`build.*` is a PROJECT section that an update preserves"* — the mechanism the receiver instruction rests on | `.tfw/CHANGELOG.md` `### Removed` | `templates/project_config.yaml:142` marks `build:` *"← PROJECT: set during init"*, and lines 152–154 state an update **preserves** it | ✅ |
| C8 | *"item 4's work was applied by the **coordinator** in `859dc74` … before this round began"* | RF §1.4, ONB §10.1 | `git show --stat 859dc74` names exactly those four files; all four byte-identical at HEAD. Attribution to the coordinator, outside Role Lock, is recorded in TS rev4 §5 item 4 by the coordinator itself | ✅ |
| C9 | *"1 failed, 321 passed"* was round 3's close and *"that failure went with the gate"* | RF §4.4 | The removed assertion in `test_gen_index.py` at `859dc74` read the live corpus's exit code; the suite is now 322/1 with the event unchanged. Consistent and independently green | ✅ |

## Discrepancies Found

**D1 — the shipped `Known open` bullet asserts a corpus count that is wrong at its own commit.**
`.tfw/CHANGELOG.md` states *"the only event over the ceiling among the **116** in this corpus that carry a
summary."* Measured twice, by two methods: **117** journal events at `1a9059b` — the commit that adds the
bullet — **all 117 carrying a summary, none without**; **118** at HEAD; 114 at `859dc74`. **116 is not the
count at any revision in this round.** The load-bearing half of the sentence — *the only event over the
ceiling*, i.e. **1** — is correct and stable across all four revisions I measured.

Two things make this more than an off-by-one. First, `EV__…` round 4 and `evidence/round4.md` record the
measurement as `$ python  # over every journal event in workspace/ and tasks/` — a comment, not a command,
so the figure **cannot be re-derived** by the next reader. Second, this is the same failure class the round
diagnosed and set out to remove from this very bullet: RF §2.4 decision 4 says *"a number measured over a
live shared corpus is a claim with an expiry date, and a CHANGELOG has none"*, and fact candidate **F18**
offers *"1 of 116"* as its example of **"a figure the neighbours cannot move"** — while that denominator
moved three times inside this round. The correct number was removed and an incorrect one of the same class
left in its place, in a **shipped, untagged** release entry, and command 13 confirms nothing in
`release.md` re-measures it before the tag.
→ **Escalated to 100% verification.** Done: all four payload files, ten forbidden paths, the HL baseline,
three out-of-scope files, `plan.md`, `handoff.md`, `release.md`, and the whole journal corpus at four
revisions. **No second discrepancy of this class was found** — the other figures (322/1, 61 tasks, 4
characters, 1 event over the ceiling, 8 project-wide hits, 1 insertion/1 deletion) all reproduce.

**D2 — `glossary.md:215`'s locator list contains one member that resolves to nothing, and its opening
claim is false.** *"Step 0 convention present in **every** TFW workflow … → `handoff.md` Step 0, `plan.md`
Step 0, `review.md` Step 0."* `plan.md` has no Step 0 — not at HEAD and not at the HL baseline `1c7b55e` —
and states the omission is deliberate at line 84: *"This is step 3 and not step 0 deliberately.
Understanding the task and asking before naming is worth more than an early label."* So the glossary
asserts a universal that one of its three cited files deliberately breaks, and points a reader at a step
that does not exist. **Pre-existing, caused by nothing in this task**, and already propagated into the
frozen corpus (`tasks/TFW-60__conflict_resistant_shared_workspace/research/iter3/3_extract.md:243` repeats *"session naming in `plan.md`,
`handoff.md` and `review.md` Step 0"*). Routed to §5, not ordered — see `judge.md` row 2.

> Neither discrepancy touches the four ordered items' delivery, which verified at 100%.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|---|---|---|
| E25 | `evidence/EV__…` round 4 row E25 → `round4.md` §0, §1 | ✅ | ✅ — nine probes, 3 mismatches → 0, and the assertion shown failing under the reverted expression. Independently reproduced here; the *"four characters, not three"* correction is in the row itself |
| E26 | row E26 → `round4.md` §2 · ONB §10.5 item 2 | ✅ | ✅ — **VERIFIED, with one classified survivor**, declared as a judgement and marked overturnable rather than reported clean. The status is honest. The reasoning is incomplete on one of its three cited files → D2 |
| E27 | row E27 → `round4.md` §2 | ✅ | ✅ — 8 hits, each attributed to its release by walking back to the nearest `## [` header rather than inferred. Reproduced |
| E28 | row E28 → `round4.md` §3 | ✅ | ⚠️ — the bullet-by-bullet check against item 4's three requirements holds and is well made. But the row carries *"1 event over the ceiling of the 116 carrying a summary, measured here"*, and `round4.md` records the command as a bare `$ python  # …` → **D1** |

Verdict on the RF's own evidence claim (**4/4 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A**): sustained for
E25–E27; **E28 is VERIFIED for the record it audits and carries one unverifiable figure inside it.**
Nothing is missing, nothing is padded, and the evidence discloses more against the executor's interest
than any round so far — three figures corrected, one gate reported unmet.

## Knowledge Citations Verified

> Round 4 adds **no** citation. ONB §10.6 states *"rounds 1–3 cover thirty-two rows; all stand. Round 4
> turns on three and adds none."* Those three are re-verified in full below; the priority-label correction
> recorded under HL §7.2 (four rows moved from priority 4 to 7, 2026-09-02) is checked against the PV
> Index and is correct. PV priorities 0–4 scanned in full, 5–7 by relevance.

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|---|---|---|---|---|---|
| 1 | HL §7.2 #8 / ONB §10.6 #8 | PV 1 — `.tfw/README.md` § Methodology values → **Structural Enforcement**: *"a rule that cannot reveal its own violation is only advice"* | ✅ `#methodology-values` → `.tfw/README.md:92` | ✅ line 97, verbatim | ✅ | ✅ — **the sharpest application in the task.** Round 3's two assertions could not reveal the violation they were added to prevent; the third can, and was shown doing it. PV 1 is a *methodology* value and is cited as one, kept separate from PV 0 |
| 2 | HL §7.2 #14 / ONB §10.6 #14 | PV 2 — `knowledge/philosophy.md` **F43**: *"answering a correct catch with the smallest possible fix is itself a defect pattern"* | ✅ | ✅ line 50, verbatim, `✅ verified` | ✅ | ✅ — applied *against the executor's own convenience*: the smallest fix was the regex alone; it added the failing-first proof and the reason in the comment. **ONB §10.6 row 14 still says "three characters"**, the order's figure; RF §2.4 dec. 5 corrects it to four. The citation's application is unaffected |
| 3 | HL §7.2 #21 / ONB §10.6 #21 | PV 4 — `conventions.md` §14: *"A review checklist row is added without an evidenced firing rate — a row that cannot produce a finding is ceremony"* | ✅ | ✅ `conventions.md:959`, verbatim | ✅ | ✅ — the round adds no row, no check, no key. Verified structurally: zero new entities in the diff |
| 4 | HL §7.2 #1–#7 | PV 0 — `NS1`, `NS2` principles 4/5/6 + closing test, `NS3` | ✅ all — `#ns1` → `.tfw/README.md:72`, `#ns2` → 80, `#ns3` → 104 | ✅ | ✅ — NS1's four words checked verbatim at line 75: *"understand what the work is for, inspect its material grounds and current result, see where authority remains, and continue"* | ✅ — priority 0 checked against the **purpose/non-goal** clause claimed, separately from priority 1's methodology clause, per `conventions.md` §3 rule 6 |
| 5 | HL §7.2 #16–#19 | PV 3 — `KNOWLEDGE.md` D64, D63, D13, D65 | ✅ | ✅ | ✅ | ✅ — and #16/#17 are the two this verdict itself rests on: *the reviewer defends purpose and alignment must be cited*, and *an approved HL is a contract* |
| 6 | HL §7.2 #22, #25, #26, #27 | PV 7 (relabelled from 4 on 2026-09-02) | ✅ | ✅ | ✅ | ✅ — the relabelling is **correct**: the PV Index defines priority 4 as `conventions.md` §3/§11/§14 only, and these cite §15, §5 and `templates/`. Verified against the Index rather than accepted from the note |

**No citation discrepancy.** Every item resolves, exists, matches its quoted meaning and is relevant to
the application asserted. The one imprecision found is a stale character count inside ONB §10.6 row 14's
*application* text, corrected in the RF and immaterial to the citation.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files and recorded findings? — required 2, **verified 4 of 4 (100%)** plus ten
      forbidden paths, the HL at baseline, `plan.md`, `handoff.md`, `release.md`, three out-of-scope files
      and the journal corpus at four revisions
- [x] Ran at least 1 build/test command? — **13 commands**, including the full suite (322 passed, 1
      skipped, exit 0), the board check, and the regex probes re-derived rather than read
- [x] Claim & Source Checks filled — nine claims spot-checked by how much the result rests on them; every
      citation traced; every data claim checked against a primary source, not against the RF's summary of it
- [x] Each RF §3 (AC) checkmark verified against actual file? — all four items' checkboxes, AC-11 bullet 1
      re-run, AC-11 bullet 2 confirmed **withdrawn** in TS revision 4 §1 and correctly not claimed
- [x] KNOWLEDGE.md checked — contradictions with changes documented? — D52 repaired and verified; §2's
      `TFW-46` row correctly left as history; **no** contradiction introduced. `KNOWLEDGE.md` §2 still has
      no task row for `TFW_20260830-194027_TLD` (RF §6 round-1 row 4), unchanged and already disposed
- [x] Knowledge Citations from HL §7.2 and ONB §7/§10.6 verified?
  - Total: **32 standing, 3 exercised by round 4, 0 added.** Resolved: 32/32. Semantically verified:
    32/32. Irrelevant: **0**. Hallucinated: **0**
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: **4** (E25–E28). Verified: **4**. Missing: **0**. One figure inside E28 does not
    hold and one command in `round4.md` is not recoverable → D1

Stage complete: **YES**
