# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: **0.42** (`project_config.yaml` → `tfw.review.min_verify_ratio`)
> RF files claimed: **9** (2 created, 7 modified)
> Files to verify: ⌈9 × 0.42⌉ = **4** → **escalated to 9 of 9 (100%)** on discrepancy D1

## Verification Log

### V1: `.tfw/templates/review/judge.md`
- **RF claim:** row 2 clause (a) → Purpose Check carrying its rate and its consequence reason; new Purpose
  Check block below the table with reference set, two invalid references, fused field, three tests, override
  clause, three-outcome table with routing; one Checkpoint item. `+42 / −1`.
- **Actual:** all of it, at lines 16 and 32-70, Checkpoint item at line 84. `git show --numstat` → `43 1`
  (RF says `+42 / −1`; the extra insertion is the blank separator line — immaterial). The block sits below
  the table and above `## Contradictions with KNOWLEDGE.md`, so the row stays one quotable sentence per
  clause. Row 2(b) reads *"Design soundness _(4.5%)_: is the design itself sound against HL §7 principles"* —
  rate intact, separately answered, `{(b) answered separately}` in the Evidence column.
- **Match:** ✅

### V2: `.tfw/workflows/review.md`
- **RF claim:** line 28 → frozen baseline + rule-15 pointer; Reviewer Identity gains goals/values/north star
  and block authority plus `not rubber stamp`; Step 3's `HL §7 Principles check` paragraph **replaced** by
  the Purpose Check instruction; Step 4 gains a Routing block. 1,065 → 1,176 words.
- **Actual:** line 28 confirmed; identity at 35-38 reads *"Quality guardian, not rubber stamp … goals, values
  and the north star are yours to defend, and they alone can ground a block"*; line 87 is the replacement,
  and the word `mapping` does not appear in the file; line 102 is the Routing block naming both failure
  outcomes and both owner routes, closing with *"Verdict vocabulary unchanged."* `wc -w` reproduces
  **1,176**; `git show HEAD~1:… | wc -w` reproduces **1,065**.
- **Match:** ✅

### V3: `.tfw/templates/REVIEW.md`
- **RF claim:** §3 row 2 realigned to `judge.md`; the `not fit for purpose` finding surfaced inside the
  existing `### If REJECT` block, no new section.
- **Actual:** ten rows, row 2 = *"Purpose Check — is this what we set out to do? + design soundness"*. The
  finding block is a blockquote immediately after `### If REJECT`, carrying the citation-and-harm
  requirement, the "quality checks passed" sentence, the owner route and the contract-defect branch. No
  heading added. The abbreviated wording is the file's pre-existing convention — rows 6-10 are all
  abbreviations of `judge.md`'s longer rows, and the file's own note asks for *"ten rows, matching
  `review/judge.md` one-for-one and in the same order"*, which is row alignment, not wording identity.
- **Match:** ✅

### V4: `.tfw/glossary.md`
- **RF claim:** PV Index gains priority 0; priority 1 relabelled `.tfw/README.md § Values and Principles —
  methodology values` with its reason; one note that priorities 0 and 1 may name the same file.
- **Actual:** all three present. Rows 2-7 byte-identical in the diff. Row 1 keeps its original content
  (*"Core beliefs (e.g., Traces Over Code, Structural Enforcement)"*) and gains the byte-identical-across-
  projects reason. **The new label resolves:** `.tfw/README.md`:82 is `## Values and Principles`. The "Who
  scans PV" block below survives unchanged and still resolves after renumbering.
- **Match:** ✅

### V5: `.tfw/conventions.md`
- **RF claim:** §3 gains **Project North Star** with seven rules (locus, no nominated task HL, payload with
  mandatory non-goals, admission criteria, fallback chain, same-file rule, citation namespace); §14 gains
  two review-side anti-patterns; `+27 / −0`.
- **Actual:** seven numbered rules confirmed at the `### Project North Star` block after rule 21; both §14
  entries present. `git show --numstat` → **`27 0`**. Phase A's rules 1-21 and TFW-56's §14 entry untouched
  — the diff hunks are pure insertions.
- **Match:** ✅

### V6: `.tfw/templates/HL.md`
- **RF claim:** north-star header field **below** the contract block, list-valued, with fallback and explicit
  `N/A`; `+7 / −0`; contract block untouched.
- **Actual:** one additive hunk after the contract block's own *"Add further header fields below this block,
  not inside it"* line. The field renders `{one or more designated README sections — e.g. …}` or
  `N/A — no project north star designated`, followed by an explanatory blockquote naming the fallback and
  F21. Zero deletions.
- **Match:** ✅

### V7: `.tfw/compilable_contract.md`
- **RF claim:** §2 pattern table only; `P{N}` corrected from `KNOWLEDGE.md` §0 to **HL §7 Principles row
  (task-local)**; `PP{N}` and `NS{N}` added; `+3 / −1`.
- **Actual:** lines 59-61 exactly as claimed; `git show --numstat` → `4 2`, of which the §2 table accounts
  for `3 1` and the remaining `1 1` is the CRLF/line-ending normalisation the repo warns about — no other
  content line changed. Line 65's second stale `KNOWLEDGE.md §0` reference survives, as RF §6 obs. 2 says.
- **Match:** ✅

### V8: `phase-c/evidence/EV__phase-c__goal_defence_in_review.md`
- **RF claim:** environment header, 13 evidence rows, verdict, the `review.md` word ledger as Exhibit A.
- **Actual:** all present. Every gate command in E1-E12 was re-run by this reviewer and every output
  reproduces (see Commands Executed). The two disclosed divergences (E1 clause (b), E3 recovery form) are
  stated in the rows *and* repeated in the verdict block rather than buried. Exhibit A's removal column is
  genuinely empty and the arithmetic closes: 18 + 34 + 11 + 48 = 111, and 1,065 + 111 = 1,176.
- **Match:** ✅

### V9: `phase-c/evidence/purpose_check_replay.md`
- **RF claim:** the Purpose Check as shipped, replayed against nine reviews with every citation-and-harm
  field filled; 5 of 6 non-approve on the rejected corpus, 0 of 3 on the sound one.
- **Actual:** nine rows present, each with the fused field filled, the three tests answered and an outcome.
  Fourteen quoted clauses and quantitative claims were traced to git history (see Claim & Source Checks) —
  twelve are verbatim-correct. **One row's classification does not survive its own source: 49/A** (D1).
  One quotation is a paraphrase presented inside quotation marks (D2).
- **Match:** ⚠️ partial — the corpus, the citations and the arithmetic hold; row 49/A's conclusion does not

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `grep -rc "mapping integrity" .tfw/templates/review/judge.md .tfw/workflows/review.md` | `judge.md:0`, `review.md:0` — reproduces AC-1 |
| 2 | `grep -c "^| [0-9]" .tfw/templates/review/judge.md` | `10` — reproduces the ten-row count |
| 3 | `grep -n "frozen baseline\|not fit for purpose" .tfw/workflows/review.md` | lines 28, 87, 102 — reproduces AC-4 |
| 4 | `wc -w .tfw/workflows/review.md` / `git show HEAD~1:… \| wc -w` | **1,176** / **1,065** — reproduces AC-5 exactly |
| 5 | `grep -n "P{N}\|NS{N}\|PP{N}" .tfw/compilable_contract.md` | lines 59, 60, 61 (+ line 81, the resolution list — RF §6 obs. 3) |
| 6 | `git show --numstat HEAD -- .tfw/conventions.md` | `27 0` — reproduces AC-10 |
| 7 | `grep -rn "git log --format" .tfw/ --include="*.md"` | **two** hits: `conventions.md`:77 and `templates/HL.md`:10 — reproduces AC-3's disclosed counterexample |
| 8 | `python -m pytest docs/scripts/ -q` | **68 passed** in 32.81s — reproduces the RF's 68 |
| 9 | `git diff e8ee76e HEAD -- …/HL-TFW-53*.md` | HL changes since the baseline are the status field, the Step 3/Step 4 stale-pointer correction, the deliverable renumber 4→5-8, one §8 dependency row, S38 and the A14 row — all in free sections or non-substantive under `conventions.md` §3 rules 6/7. **No unlogged frozen-section edit.** |
| 10 | `git status --short` | `README.md` modified and uncommitted, carrying both this phase's RF link and the TFW-55 row — matches RF §2 decision 8 |

## Claim & Source Checks

> Escalated well past the mandated 2-3: the replay is AC-11's entire evidence base and every row of it is a
> quotation from a reverted task's contract, so each was traced to the commit the replay names.

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | *"smaller where precision and references can replace prose"* | replay 48/A | `721ca15:…HL-TFW-48…`:15 — verbatim | ✅ |
| C2 | DoF-12 *"adds another conceptual layer or document that duplicates an existing owner"* | replay 48/A, 48/C | `721ca15:…HL-TFW-48…`:369 — verbatim | ✅ |
| C3 | DoD-6 *"Planning preserves user insights, product requirements, applicable Project Values, and uncertainty…"* | replay 48/B | `721ca15:…HL-TFW-48…`:341 — verbatim | ✅ |
| C4 | DoD-12 *"Every claimed deliverable has local proof…"* | replay 48/C | `721ca15:…HL-TFW-48…`:347 — verbatim | ✅ |
| C5 | *"transitional attention signals"* (the Phase E adjacency finding) | replay 48/C | `721ca15:…phase-c/REVIEW…`:20 and `TS…`:42/97/168 | ✅ |
| C6 | §1 *"The identity remains readable without special tooling"* | replay 49/A | `9e19a4f:…HL-TFW-49…`:15-16 — verbatim, **but the sentence continues** | ⚠️ see D1 |
| C7 | *"This is provenance, not decoration"* | replay 49/A | `9e19a4f:…HL-TFW-49…`:19 — verbatim | ✅ |
| C8 | DoD-3 *"A versioned structural validator rejects malformed or missing identity…"* | replay 49/A | `9e19a4f:…HL-TFW-49…`:200 — verbatim | ✅ |
| C9 | DoF-8 *"Enforcement depends only on agent compliance prose or only on unversioned `.git/` state"* | replay 49/A, 49/C | `9e19a4f:…HL-TFW-49…`:235 — verbatim | ✅ |
| C10 | DoD-4 *"observable point-of-action consumer of the canonical contract"* | replay 49/B | `9e19a4f:…HL-TFW-49…`:203 — verbatim | ✅ |
| C11 | P11 *"agents see the local imperative and one valid example at commit time"* | replay 49/B | `9e19a4f:…HL-TFW-49…`:270 — verbatim | ✅ |
| C12 | *"3,160 lines"* router | replay 49/B | `721ca15:…phase-b/REVIEW…`:38 — `719 + 1,066 + 1,296 + 79 = 3,160` | ✅ |
| C13 | *"1,708 lines"* validator | replay 49/A | `721ca15:…phase-a/RF…`:47 / `REVIEW…`:74 | ✅ |
| C14 | Phase C deliverable 1 *"Replace or safely bypass the current local branch-prefix hook…"* | replay 49/C | `9e19a4f:…HL-TFW-49…`:182 — verbatim | ✅ |
| C15 | *"the independent reviewer commit `1ebb680` recorded 7 of 10 Judge checks FAIL and was overwritten three commits later"* | replay 49/C | `1ebb680` exists — `[codex/TFW-49/phase-c/reviewer] request runtime lifecycle corrections`, writes `phase-c/review/judge.md` | ✅ |
| C16 | *"preserves all ten mapped principles"* — offered as the shipped review's wording | replay 48/A note | `721ca15:…phase-a/review/judge.md`:12 reads *"preserves Phase HL P1–P10"* | ⚠️ see D2 |
| C17 | The 48/A analysis: the shipped row mapped against a Phase HL that dropped master principles | replay 48/A note | Confirmed — `721ca15:…phase-a/HL__phase-a…`:145-154 authors **its own ten** principles; the master HL carries **thirteen**, and master P7/P10/P12 are absent from the phase list | ✅ substance correct |
| C18 | §1 *"One precise Markdown rule achieves this without enforcement software"* | replay TFW-50 | `tasks/TFW-50…/HL-TFW-50…`:9 — verbatim | ✅ |
| C19 | §1 *"Codex becomes a first-class TFW adapter with dedicated shortcut skills … matching the adapter parity already achieved"* | replay 47/B | `tasks/TFW-47…/HL-TFW-47…`:14 — verbatim | ✅ |
| C20 | The 42/A vision clauses and *"know exactly what to investigate"* | replay 42/A | `tasks/TFW-42…/HL-TFW-42…`:10 — every clause present | ✅ |
| C21 | The 42/A near-miss: the guidance table the owner later removed as tautological | replay 42/A | `knowledge/process.md` F22 — *"Generic capability guidance tables … tautological overhead — removed by user as valueless"*, TFW-42 session, 2026-04-30 | ✅ |
| C22 | *"~4 blocks in 149 reviews"* inside the shipped row | `judge.md`:16 | HL §4 Phase C design note at baseline: *"base rate ~4 blocks in 149 reviews"*. No project named in the template (F13); the row flags it as *"a different corpus"* against the file header's 637-row figure | ✅ |

## Discrepancies Found

### D1 — Replay row 49/A: the third-outcome classification does not survive its own source ❌

The row rules TFW-49 Phase A a **contract defect** (the third outcome) on this reasoning:

> §1 Vision promises *"readable without special tooling"* and *"This is provenance, not decoration"*, while
> DoD-3 mandates a versioned structural validator and DoF-8 makes *"enforcement depends only on agent
> compliance prose"* a failure condition. **The minimal Markdown solution the Vision implies is the solution
> DoF-8 forbids.** Both clauses are owner-approved and cannot be jointly satisfied.

The quoted §1 sentence, read to its end at `9e19a4f:…HL-TFW-49…`:15-17:

> "The identity remains readable without special tooling, **while structural validation prevents quiet
> drift** between Coordinator, Researcher, Executor, Reviewer, adapters, and repositories."

§1 asks for **both** properties in one sentence — human-readable identity *and* structural validation. It
does not imply a Markdown-only solution; it names validation as the companion of readability. DoD-3's
validator is therefore the §1 clause discharged, not a contradiction of it, and DoF-8 (which forbids
enforcement resting *only* on prose or *only* on unversioned `.git/` state) is satisfied by any versioned
check. There is no pair of clauses here that cannot be jointly satisfied. **The reference set is not
internally inconsistent, so the third outcome is not the correct outcome for this row.**

The replay's own supporting argument points the same way once tested. It offers TFW-50 as *"confirmation
from outside this replay"* — TFW-50 shipped *"one precise Markdown rule … without enforcement software"* and
was approved. But TFW-50 ran under **its own** HL; a prose-only rule would have failed TFW-49's DoF-8
outright. What TFW-50 confirms is that the owner's preference changed between two contracts, not that one
contract contradicted itself. And the row itself concedes the excess reading is *"arguable at most … the
clause asked for one"* — which is the honest reading, and it lands on `✅ aligned`, exactly where research
iteration 2 put it before amendment A6 existed.

**Four consequences, sized:**

| # | What it touches | Effect |
|---|-----------------|--------|
| 1 | AC-11's count | 5 of 6 → **4 of 6** non-approve (48/A, 48/C, 49/B, 49/C). Pass condition is *"≥1 non-approve"* → **AC-11 still passes**, and the 0-of-3 sound-corpus result is untouched |
| 2 | RF §3 AC-12 *"Exercised for real: replay row 49/A"* | Unsupported. AC-12's gate is textual (*"read the block; routing target is the owner; reachable without leaving `judge.md`"*) and passes independently, and its Evidence field says a replay row is *"expected"*, not required → **AC-12 still passes on its gate**, but the RF sentence overclaims |
| 3 | The shipped `judge.md` precedent line | **This is the material one.** Every install now reads *"one rejected task's approved §1 promised 'readable without special tooling' while its approved DoD required a versioned structural validator"* as the canonical illustration of a contract defect. The illustration is built on a half-sentence, so it teaches reviewers to read surface tension as unsatisfiability — the opposite of the discipline the same block demands three paragraphs above (*"a citation that resolves but is irrelevant fails the row"*) |
| 4 | RF §8 S2 and the KNW pipeline | S2 (*"the check found its own predecessor's defect while being validated on it"*) has no basis left, and the derived implication (*the replay is the check's regression suite*) rests on it. S2 is High-confidence material headed for `KNOWLEDGE.md` at KNW — approving it writes a false fact into project memory |

Escalation triggered: verification raised from 4 files to 9 of 9.

### D2 — A paraphrase inside quotation marks ⚠️

The 48/A note attributes to the shipped review the words *"preserves all ten mapped principles"*. The source
reads *"preserves Phase HL P1–P10"* (`721ca15:…phase-a/review/judge.md`:12). The substance is right — and
C17 confirms the deeper claim independently — but the marks say verbatim and the words are not. Low
severity on its own; it shares a shape with D1, and in the phase whose thesis is *alignment must be cited,
not asserted* the form is part of the deliverable.

### D3 — HL §4 Phase C deliverable 2 no longer describes what shipped ⚠️ (coordinator-side)

The frozen deliverable reads *"Locus: a designated section of the root `README.md`"*. The shipped
`conventions.md` rule 1 reads *"designated section(s) of a README"* and permits more than one location, on
the owner's ONB Q2 ruling, recorded at HL §11 S38.

The widening is **legitimate**: `conventions.md` §3 rule 6 makes deliverable lists inside an approved phase
free, and the tripwire clears — no §5 or §6 item as it stands is breached (DoD-18 and DoD-19 name no locus,
DoF-14 is satisfied). But the deliverable text itself was never refined to match, so the HL now describes a
narrower rule than the framework ships. **Not the executor's to fix** — the role lock forbids it, and this
reviewer's too. → coordinator.

### D4 — The adapter copy of `review.md` is stale, and this review is the proof ⚠️ (known, in flight)

This review session was invoked through `.claude/commands/tfw-review.md`, which still carries
*"Reviewer Identity: Quality guardian."* and the deleted *"HL §7 Principles check"* paragraph. The canonical
`.tfw/workflows/review.md` was followed instead, per AGENTS.md. Out of scope by design (Phase D owns the
sync, TS §2), already recorded as TD-157 and predicted in ONB §5 risk 4 — logged because the window is now
demonstrably live, not theoretical, and because a reviewer who trusted the adapter copy would have run the
retired check.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | AC-1 gates in EV | ✅ | ✅ — both greps and the row count reproduce; the clause-(b) divergence is disclosed in the row itself |
| E2 | `purpose_check_replay.md` §5 | ✅ | ✅ — passing and failing forms both present; the failing form is rejected by the row's own quoted wording |
| E3 | recovery-command gate | ✅ | ✅ — two hits reproduce, and the row states the gate does not literally clear rather than reporting a pass |
| E4 | `review.md` line greps | ✅ | ✅ — lines 28, 87, 102; verdict set unchanged at line 100 |
| E5 | word ledger, Exhibit A | ✅ | ✅ — 1,065/1,176 reproduce; ledger arithmetic closes; removal column empty by construction |
| E6 | PV Index + `conventions.md` §3 | ✅ | ✅ — rows 2-7 byte-identical; seven rules present; new label resolves to a real heading |
| E7 | `templates/HL.md` diff | ✅ | ✅ — one additive hunk, zero deletions, below the contract block |
| E8 | `REVIEW.md` row alignment | ✅ | ✅ — ten rows, row 2 realigned, no new section |
| E9 | `compilable_contract.md` numstat | ✅ | ✅ — table-only change confirmed line by line |
| E10 | `conventions.md` numstat `27 0` | ✅ | ✅ — reproduces exactly |
| E11 | the replay | ✅ | ⚠️ — 8 of 9 rows hold; row 49/A's classification fails on its own source (D1). AC-11's pass condition survives at 4 of 6 |
| E12 | third outcome + routing | ✅ | ⚠️ — the block, the routing and the reachability all hold; *"exercised for real: replay row 49/A"* does not |
| E13 | build gate | ✅ | ✅ — 68 tests re-run and pass; the changed files are docs-pipeline sources and no warning names them |

Total evidence items: 13, verified: **11**, partial: **2** (E11, E12), missing: 0.

**On the RF's `13/13 VERIFIED` verdict:** eleven rows are clean, and the two divergences the RF *does*
disclose (E1, E3) are disclosed well — named in the row, repeated in the verdict, not downgraded to look
tidy. The defect is not concealment; it is that E11 and E12 rest on a reading of one source that the source
does not support, and nothing in the evidence file re-tested it.

## Knowledge Citations Verified

> ONB §7 carries 26 items from HL §7.2 plus six new ones (N1-N6). Every referenced record was checked for
> existence in its named file.

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | HL §7.2 / ONB §7 | `KNOWLEDGE.md` D19, D20, D23, D24, D31, D43, D46, D49, D54, D55 | ✅ | ✅ all ten |
| 2 | ONB §7 N1, N3 | `KNOWLEDGE.md` D61, D53 | ✅ | ✅ both |
| 3 | HL §7.2 / ONB §7 | `knowledge/philosophy.md` F4, F13, F21, F22, F25 | ✅ | ✅ all five |
| 4 | ONB §7 N4 | `knowledge/philosophy.md` F24 | ✅ | ✅ |
| 5 | HL §7.2 / ONB §7 | `knowledge/process.md` F4, F6, F11, F14, F19, F20, F25 | ✅ | ✅ all seven |
| 6 | replay 42/A | `knowledge/process.md` F22 | ✅ | ✅ |
| 7 | HL §7.2 / ONB §7 | `knowledge/constraint.md` F2 | ✅ | ✅ |
| 8 | ONB §7 N2 | `knowledge/constraint.md` F4 | ✅ | ✅ |
| 9 | ONB §7 | `.tfw/README.md` § Structural Enforcement, § Naming Creates Behavior, § Candor Over Flattery | ✅ | ✅ headings at 100, 104, 88 as claimed |
| 10 | ONB §7 | `conventions.md` §7, §15 | ✅ | ✅ |

Total citations: **32**, verified: **32**, hallucinations: **0**.

**KNOWLEDGE.md contradiction check.** D61 (TFW-56's universal ten-row checklist, measured rates carried
inside each promoted row) is respected, not contradicted: ten rows kept, and row 2(a) carries its figure
inside the row in the rows 8-10 grammar. D46 (Reviewer Identity) is *completed* rather than contradicted —
its recorded text was *"Quality guardian, not rubber stamp"* and only half had shipped. D43 (citation-with-
link as the anti-hallucination device) is extended by the harm half, which is the SS2 gap. No contradiction
found.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files and recorded findings? — 9 of 9, escalated to 100% on D1
- [x] Ran at least 1 build/test command (or documented why not)? — pytest re-run, 68 passed; ten commands logged
- [x] Claim & Source Checks filled — 22 claims traced, 20 verbatim-correct, 2 flagged (D1, D2)
- [x] Each RF §3 (AC) checkmark verified against actual file? — all twelve, gate commands re-run
- [x] KNOWLEDGE.md checked — contradictions with changes documented? — none found; D61/D46/D43 examined explicitly
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist)?
  - Total citations: **32**, verified: **32**, hallucinations: **0**
- [x] Evidence artifacts from RF §5 verified (files exist, claims match)?
  - Total evidence items: **13**, verified: **11**, partial: **2**, missing: **0**

Stage complete: YES

---

# Verify — second pass (corrective, 2026-08-13)

> **Scope:** the corrective pass only. Commits `2642e81` (coordinator: HL §2, §9, §12 note, TD-168),
> `7e5311d` (coordinator: TS AC-13 to AC-15 + four DoF items), `bd032a5` (executor: `judge.md`, RF, EV,
> replay). Files changed: **4** — one framework file and three task artifacts. Ratio 0.42 → 2 required;
> **all 4 opened**, plus the HL and TS the coordinator changed, for **6 of 6**.
> First-pass findings under re-test: D1 (49/A truncation), D2 (48/A quotation), D3 (HL deliverable 2).

## Verification Log — second pass

### V10: `.tfw/templates/review/judge.md` — AC-14
- **RF claim:** the blockquote no longer offers the withdrawn reading as the canonical contract defect; it
  states the bar instead; no substitute example was hunted for; `1,167 → 1,165` words, paid inside the same
  block; `review.md` untouched.
- **Actual:** the old precedent blockquote is gone. In its place, lines 66-70: *"Two clauses conflict only if
  satisfying one **necessarily** violates the other. Read each to the end of its sentence: a clause that
  qualifies itself in its second half is not in tension with the clause that discharges it. Surface tension
  is not inconsistency — and a contract that is coherent but wrong for the product is the purpose question
  above, not this one. **No instance has been observed** in the corpus this check was validated against."*
  `wc -w` reproduces **1,165**; `git show HEAD~1:… | wc -w` reproduces **1,167**. `review.md` reproduces
  **1,176**, byte-identical to the first pass.
- **Match:** ✅ — and the replacement is **stronger than the thing it replaces.** The old line gave a reader
  one example to pattern-match; the new one gives the discriminating test, and the test is exactly the one
  whose absence produced D1. A gate that teaches the error it was built from is the better artifact.

### V11: `.tfw/templates/review/judge.md` — what the trim removed
- **RF claim:** *"paid inside the same block"* — no ledger given.
- **Actual:** diffed line by line. Four sites, all inside the Purpose Check block, all rhetorical emphasis:
  *"— naming them is the point of this row"* · *"— the fallback chain makes that hard to write honestly"* ·
  *"Three outcomes, **not two**. The Status column keeps…"* → *"Three outcomes. Status stays…"* · three
  outcome-table cells compressed (*"the filled citation-and-harm field"* → *"the filled field"*, the fused
  field being defined in bold two paragraphs above). **No mechanism lost:** the reference set, both invalid
  references with their reasons, the fallback chain, all five failing conditions, the three tests, the
  override clause and all three outcomes with their routing are intact and verified present.
- **Match:** ✅ substantively — see second-pass discrepancy D6 on the missing ledger.

### V12: `purpose_check_replay.md` — AC-13
- **RF claim:** row 49/A re-scored with the full sentence quoted, outcome `✅ aligned`, excess argued and
  rejected, the TFW-50 confirmation dropped, the correction recorded with its cause named.
- **Actual:** §0 carries a **Correction of record** quoting §1 to the end of the sentence and naming the
  cause (*"a quotation ended early"*), and states that the shipped check and research iteration 2 now agree
  on all nine rows. Row 49/A returns `✅ aligned`. The excess rebuttal cites **DoD-7** — *"repository
  fixtures … across all four TFW roles and at least two agent surfaces"* including *"search/filter
  behavior"* — which I traced to `9e19a4f:…HL-TFW-49…`:206-208 and is **verbatim**. The TFW-50 paragraph is
  gone. The §3 diagram, the §3 AC-11 condition table and the §4 reconciliation all carry `4 of 6`.
- **Match:** ✅ — and the row is now the most informative in the file. It records that 49/A is *aligned with
  its approved contract* while the owner rejected the product, and routes that case to the north star (PV
  priority 0). That is empirical support for the HL's own deliverable weighting, which the first pass did
  not have.

### V13: `EV__phase-c…md` — AC-13 propagation
- **RF claim:** E11 re-scored to 4 of 6 with the cause named, E12 narrowed to the textual gate, new **E14**
  `DEFERRED` with the blocker named; verdict `13/14 VERIFIED, 1 DEFERRED`.
- **Actual:** all three present and worded as claimed. E14's blocker: *"no such case exists in the
  nine-review corpus"*, with the Phase B precedent for an unexercised branch cited. The verdict block gained
  E14 as a third disclosed divergence.
- **Match:** ✅ — see D5 on row ordering.

### V14: `RF__phase-c…md` — AC-13, AC-15
- **RF claim:** eight sites propagated; S2 rewritten; S4 added; §6 obs. 7 records the 48/A finding.
- **Actual:** §2 decision 6 rewritten with the cause and a *"how the error got in"* paragraph naming TD-166
  as its structural half · §3 AC-11 → `4 of 6`, AC-12 → gate passes / branch unexercised · §5 → `13/14` with
  E14 explained · §8 S2 rewritten with the withdrawal marked inline, S4 added · §9 both affected diagrams
  corrected, each carrying a *"corrected on the second pass"* note · a second AC table for AC-13 to AC-15 ·
  DoF count `16`, which matches TS §7 (`grep -c "^- ❌"` → **16**).
- **Match:** ✅ 8 of 8 sites

### V15: `HL-TFW-53…md` — coordinator, and the harder question
- **RF claim (coordinator's):** §2's evidence row and §9's risk row corrected; a correction of record
  appended below §12; **A6's row not rewritten**; TD-168 closed by refining deliverable 2.
- **Actual:** §2's row now carries the strikethrough and the withdrawal inline, with the surviving claim
  stated. §9's probability reads **`Unmeasured` (was Medium)** with zero instances recorded. The §12 note is
  appended below the table and A6's row is byte-identical to the baseline. Deliverable 2 now reads
  *"designated section or sections of a README"* with the rule-6 reasoning inline.
- **Contract discipline re-checked, because a frozen section was touched.** §2 is **free** (header: *"Free:
  §2 · §7.2 · §8 · §9 · §10 · §11"*), §9 is free, §12 is append-only and was appended to. Deliverable 2 sits
  in **frozen §4**, and `conventions.md` §3 rule 6 makes deliverable lists inside an already-approved phase
  free; the tripwire clears, since no §5 or §6 item as it stands is breached by permitting more than one
  location. `git diff e8ee76e HEAD` on the HL shows **no edit to §1, §3, §5, §6 or §7**.
- **Match:** ✅ — **D3 closed.** The refusal to rewrite A6's row is the correct call and the harder one: it
  keeps the log honest about what was believed when the amendment was ruled.

### V16: `TS__phase-c…md` — coordinator
- **RF claim (coordinator's):** AC-13 to AC-15 added with gates; the scope of the pass stated as a negative
  first; four DoF items added.
- **Actual:** all present. The *"What is not reopened"* paragraph names the mechanism, the corpus, the seven
  framework files and AC-1 to AC-12 explicitly. Four new DoF items, including *"`judge.md` grows on a
  corrective pass, or a corrected quotation is fixed without naming why it was wrong"*.
- **Match:** ✅ — and AC-13's bullet list names all eight propagation sites, which is why none was missed.

## Commands Executed — second pass

| # | Command | Result |
|---|---------|--------|
| 11 | `wc -w .tfw/templates/review/judge.md` / `git show HEAD~1:… \| wc -w` | **1,165** / **1,167** — AC-14's no-growth gate reproduces |
| 12 | `wc -w .tfw/workflows/review.md` | **1,176** — untouched, as AC-14 requires |
| 13 | `grep -rc "mapping integrity" …judge.md …review.md` | `0` / `0` — still clear after the trim |
| 14 | `grep -c "^| [0-9]" .tfw/templates/review/judge.md` | `10` — still ten rows |
| 15 | `grep -c "^- ❌" TS §7` | **16** — matches RF's *"all sixteen clear"* |
| 16 | `git diff e8ee76e HEAD -- …HL-TFW-53*.md` | frozen §1/§3/§5/§6/§7 untouched; §4 deliverable 2 refined under rule 6 with reasoning inline; A6's row byte-identical |
| 17 | `python -m pytest docs/scripts/ -q` | **68 passed** in 58.66s |
| 18 | `python -m mkdocs build -f docs/mkdocs.yml` | built in 51.92s, no new warning attributable to the four changed files |
| 19 | `for f in templates/review/*.md templates/*.md workflows/review.md; do wc -w; done` | map 159 · verify 618 · **judge 1,165** · REVIEW 679 · TS 533 · RF 593 · review.md 1,176 — see D4 |

## Claim & Source Checks — second pass

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C23 | §1 quoted to the end: *"readable without special tooling, **while structural validation prevents quiet drift** between Coordinator, Researcher, Executor, Reviewer, adapters, and repositories"* | replay §0, row 49/A; HL §2, §12 note | `9e19a4f:…HL-TFW-49…`:15-17 — **verbatim, full sentence** | ✅ |
| C24 | DoF-8 *"Enforcement depends only on agent compliance prose or only on unversioned `.git/` state"* | replay §0 | `9e19a4f:…HL-TFW-49…`:235-236 — verbatim | ✅ |
| C25 | DoD-7 *"repository fixtures … across all four TFW roles and at least two agent surfaces"*, incl. *"search/filter behavior"* — the new excess rebuttal | replay row 49/A | `9e19a4f:…HL-TFW-49…`:206-208 — verbatim | ✅ |
| C26 | *"preserves all ten mapped principles"* — the executor's counter-claim that it is verbatim | replay 48/A note; RF §6 obs. 7 | `721ca15:…phase-a/REVIEW__phase-a__method_kernel.md`:**51** (§4 Verdict) — **verbatim** | ✅ **executor is right** |
| C27 | *"Phase HL P1–P10 all pass through their mapped ACs"* — the sentence the first pass offered as the true source | replay 48/A note; RF §6 obs. 7 | `721ca15:…phase-a/REVIEW__phase-a__method_kernel.md`:**38** (Judge row 2) — verbatim, **different sentence, same file** | ✅ both exist |
| C28 | *"the same verdict research iteration 2 recorded"* for 49/A | replay row 49/A, §0 | `research/iter2/` replay recorded 49/A as *passes* — consistent with the first pass's own §0 statement of the divergence, which is now withdrawn as an artifact of the truncation | ✅ |

## Discrepancies Found — second pass

### D1 — **CLOSED.** Corrected, propagated, and the cause named
Every one of the four consequences the first pass sized is discharged: AC-11 recounts to 4 of 6 (condition
`≥1` holds), AC-12 is restated as *gate passes, branch unexercised*, the shipped illustration is replaced by
the bar, and S2 is rewritten to what survives. The correction is recorded as a correction in five artifacts
— replay §0 and §1, HL §2 and §9, the §12 note, EV E11/E14, RF §2 decision 6 — with the cause stated each
time. Nothing was silently repaired.

### D2 — **WITHDRAWN. This was my error, not the executor's** ❌→✅
The first pass claimed *"preserves all ten mapped principles"* was a paraphrase inside quotation marks. It
is not. It is verbatim at `REVIEW__phase-a__method_kernel.md`:**51**. I compared it against
`phase-a/review/judge.md`:12 — the **stage file**, a different document — found different wording there, and
called the quotation inaccurate without checking the file the quotation came from. Both sentences the
executor now cites are real, at the lines given (C26, C27).

The executor refused the fix, verified both sources, added line numbers to each half, and filed RF §6 obs. 7
saying so — including that TS AC-15's second bullet *"asks for a fix that would have introduced the defect it
was written to remove"*. That is the correct handling of a wrong instruction from a reviewer, and it is the
same discipline the phase ships: the claim was checked against the source rather than obeyed.

### D3 — **CLOSED.** HL deliverable 2 refined under rule 6, reasoning inline, TD-168 closed (V15)

### D4 — `judge.md` is now the largest artifact of its class in the repository ⚠️ (new, Low)

| Artifact | Words | Note |
|---|---:|---|
| `templates/review/map.md` | 159 | |
| `templates/TS.md` | 533 | |
| `templates/RF.md` | 593 | |
| `templates/review/verify.md` | 618 | |
| `templates/REVIEW.md` | 679 | |
| **`templates/review/judge.md`** | **1,165** | **639 before this phase — +82% in one phase** |
| `workflows/review.md` | 1,176 | F2 hard threshold 1,200 |

The Judge template is now 1.7× the next-largest template and **effectively the same weight as the workflow
it serves**, while being the artifact a reviewer fills in every review. **This is not a violation:** frozen
DoD-28 *directs* the mechanism into `judge.md` precisely because *"a template is not a workflow"* and is off
F2's budget, and HL §4 states that choice explicitly. The coordinator also installed the right rule the
moment it mattered — AC-14 forbids growth on a corrective pass, and the executor met it at −2 words.

What is new is the **measurement**. TD-141 records that the attention budget is numeric for workflows only,
and that the classes with no number are where growth lands; TD-140 measured `templates/HL.md` at +76% in one
phase as the first instance. This is the second, larger instance, in the template with the highest fill
frequency in the framework. → appended to TD-141 as evidence, not filed as a new defect.

### D5 — EV row order runs E1…E12, **E14, E13** ⚠️ (new, Low)
`E14` was inserted above `E13` rather than appended. Evidence rows are addressed by identifier — RF §4 still
reads *"AC gates reproduced with their commands and outputs in EV **E1-E13**"* while E14 exists outside that
range. Cosmetic, no claim affected. → `/tfw-docs`, on the TD-146 precedent.

### D6 — the `judge.md` trim has no ledger ⚠️ (new, Low)
AC-14 required no-net-growth and did not require a ledger, so this is not a gate miss. But AC-5 required one
for `review.md` for exactly this risk — a trim that quietly removes the sole statement of a mechanism — and
the asymmetry means a reviewer must diff the file to learn what was cut. I diffed it (V11): four rhetorical
removals, nothing load-bearing. Recorded so the next corrective pass on a template carries the two lines.

## Evidence Verification — second pass

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E11 | replay, re-scored | ✅ | ✅ — `4 of 6` reproduces in all five places it appears; cause named |
| E12 | third outcome, textual gate | ✅ | ✅ — narrowed honestly from the first pass's overclaim |
| E14 | third outcome unexercised | ✅ | ✅ — `DEFERRED` with the blocker named; the status is auditable, which is the point of using one |
| E13 | build gate | ✅ | ✅ — re-run: 68 passed, site builds |

Total evidence items: **14**, verified: **13**, deferred: **1** (E14, blocker named), missing: 0.
**The `13/14 VERIFIED, 1 DEFERRED` verdict is now accurate.**

## Checkpoint — second pass

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files? — 6 of 6 (4 changed + HL + TS), ratio required 2
- [x] Ran at least 1 build/test command? — pytest 68 passed, mkdocs built; nine commands logged
- [x] Claim & Source Checks filled? — 6 new claims traced, **all 6 hold**, including the one that overturns my own first-pass finding
- [x] Each RF §3 (AC) checkmark verified? — AC-13, AC-14, AC-15 against their gates; AC-1 to AC-12 re-confirmed unchanged
- [x] KNOWLEDGE.md checked? — no new contradiction; S2's rewrite removes the false fact before KNW
- [x] Knowledge Citations verified? — 32 of 32 from the first pass unchanged; 6 new source checks added
- [x] Evidence artifacts verified? — 14 items, 13 verified, 1 deferred with its blocker named

Stage complete: YES
