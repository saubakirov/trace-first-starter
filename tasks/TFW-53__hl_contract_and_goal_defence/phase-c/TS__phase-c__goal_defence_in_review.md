# TS — TFW-53 / Phase C: Goal Defence in Review

> **Date**: 2026-08-13
> **Author**: Coordinator (Claude Code)
> **Status**: 🟡 TS_DRAFT — **approved by the owner 2026-08-13**, cleared for execution · **amended after ONB** (Q1 → `review.md`:85 in scope · Q2 → north-star locus ruled · Q3 → deferral confession ships · **AC-12 added** for the uncovered DoD-23) · **amended after REVIEW 🔄 REVISE — AC-13, AC-14, AC-15 added for the second execution pass, same executor**
> _(§5 has no `TS_APPROVED` token and this task does not invent one — the approval is recorded, the status vocabulary is unchanged.)_
> **Parent HL**: [HL-TFW-53](../HL-TFW-53__hl_contract_and_goal_defence.md) — 🔒 FROZEN, re-frozen after A1–A14
> **Covers**: frozen DoD 18–29
> **Predecessor read** (Pre-TS gate): [RF Phase B](../phase-b/RF__phase-b__enforcement_in_workflows.md), [REVIEW Phase B](../phase-b/REVIEW__phase-b__enforcement_in_workflows.md) — ✅ APPROVE
> **Sibling read**: [RF TFW-56](../../TFW-56__review_mode_removal/RF__TFW-56__review_mode_removal.md) — landed first; it rewrote every file this phase touches

---

## 1. Objective

Phases A and B stopped the goals from moving. This phase catches the other case: the goals held, and the work went somewhere else anyway. The Judge's mapping-integrity check — which cannot detect a principle violated by the mapping itself — is replaced by a **Purpose Check** whose reference set is the committed contract baseline plus a Project North Star, never the TS. A reviewer gains the authority to reject work that is verified, complete, tested and beside the point, and loses the ability to assert alignment without citing the clause it serves.

## 2. Scope

### In Scope

- `templates/review/judge.md` — Purpose Check replacing row 2 clause (a); reference set, fused citation-and-harm, excess-and-adjacency test, third outcome, override clause
- `workflows/review.md` — context-loading line 28, Reviewer Identity, `not fit for purpose` verdict routing
- `templates/REVIEW.md` — row 2 realignment + Purpose Check finding in the synthesis
- `glossary.md` — PV Index priority 0 and the priority 1 relabel
- `conventions.md` — Project North Star definition, two §14 anti-patterns
- `templates/HL.md` — north-star header field with its fallback chain
- `compilable_contract.md` — the `NS{n}` / `PP{n}` / `P{n}` namespace rows
- Replay validation against TFW-48/49 and three sound reviews

### Out of Scope

- **Adapter and entry-point sync** — Phase D deliverable 3 owns it. Do not touch `.claude/`, `.agent/`, `.agents/` or `.tfw/adapters/`
- **Glossary articles** for `Project North Star`, `Purpose Check`, `not fit for purpose`, `deferral confession` — Phase D deliverable 1. This phase adds the **PV Index rows**, not the term articles
- **Writing this repository's north-star designation into either README.** The owner has ruled *what* it is — the philosophy in the root `README.md` and the founder essay `.tfw/README.md` (HL §11 S38) — and AC-6/AC-7 build for it. But a [TFW-55](../../TFW-55__canonization_program/HL-TFW-55__canonization_program.md) session is restructuring both files right now, so a section-level pointer landed today is stale on arrival. Phase C ships the slot and the grammar; the pointer lands with TFW-55 or with the next HL written here. The fallback (master HL §1 at the frozen baseline) must therefore still work on day one
- Version bump, CHANGELOG — Phase D
- Any part of the AT execution mode (HL DoF-4)

## 3. Principles Check

| # | Principle (HL §7) | Enforced by | Gate |
|---|-------------------|-------------|------|
| P3 | Structural enforcement over guidelines | AC-1, AC-2 | The check lives in the template that is filled every review, not in `review.md` prose |
| P8 | Tool-agnostic by behavior | AC-1, AC-6 | No vendor mechanism named; the anchor is a file and a PV row, not a memory layer |
| P13 | Purpose is a distinct question, judged where verdicts are formed | AC-1 | One row inside Judge, no fifth stage, no new document |
| P14 | Every gate needs a materiality bar | AC-2 | The harm clause is mandatory; a phrasing objection cannot satisfy it |
| P15 | Alignment must be cited, not asserted | AC-2 | A `✅` with no quoted clause fails the row |
| P16 | Judge against the baseline, never the spec | AC-3, AC-4 | TS and Phase HL named as invalid references in both files |
| P9 | Naming creates behavior | AC-4, AC-9 | `not fit for purpose` is the finding name; `NS{n}` cannot collide with `P{n}` |
| P7 | Token density | AC-5 | `review.md` word ledger |
| P2, P4, P5, P6, P10, P11, P12 | contract/amendment mechanics | N/A | Discharged in Phases A and B; no review-side surface |
| P1, P17 | contract earns autonomy; failed trace | N/A | P1 is the task-level thesis, not a phase deliverable; P17 is Phase E |

## 4. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `.tfw/templates/review/judge.md` | MODIFY | Row 2 clause (a) replaced by the Purpose Check; the three tests and the override clause added below the table; one Checkpoint item |
| `.tfw/workflows/review.md` | MODIFY | Line 28 context row, Reviewer Identity block, verdict routing for `not fit for purpose`, and **the `HL §7 Principles check` paragraph in Step 3 — that paragraph and nothing else in that step** _(added 2026-08-13 on ONB Q1: it is the second live statement of the mapping-integrity check, and leaving it ships DoF-11)_ |
| `.tfw/templates/REVIEW.md` | MODIFY | §3 row 2 wording realigned to `judge.md`; Purpose Check finding surfaced in §4 Verdict |
| `.tfw/glossary.md` | MODIFY | PV Index gains priority 0; priority 1 relabelled |
| `.tfw/conventions.md` | MODIFY | Project North Star defined (§3); two §14 anti-patterns |
| `.tfw/templates/HL.md` | MODIFY | Header block gains the north-star field and its fallback chain |
| `.tfw/compilable_contract.md` | MODIFY | **One table, reference patterns only.** `P{N}` row corrected — it still points at `KNOWLEDGE.md §0`, removed by D37; `NS{N}` and `PP{N}` rows added |
| `phase-c/evidence/EV__phase-c__goal_defence_in_review.md` | CREATE | Structured evidence, per-AC table, verdict |
| `phase-c/evidence/purpose_check_replay.md` | CREATE | AC-11 — the replay corpus, per-review outcome, and the derived base rate |

**Budget:** 2 new, 7 modified. Limits: 30 files, 15 new, 3000 LOC, 30 modified. Net LOC small and additive.

## 5. Acceptance Criteria

### AC-1: The Purpose Check replaces clause (a) of row 2, and clause (b) survives intact

`judge.md` row 2 currently carries two separately answered clauses: **(a) mapping integrity** and **(b) design soundness _(4.5%)_**. DoD-20 replaces the mapping-integrity check. Clause (b) arrived four hours earlier from TFW-56 carrying six hard `❌` and its own measured rate; replacing the whole row deletes it silently.

- [ ] Row 2 clause (a) is the Purpose Check: *is this what we set out to do?* — no mapping-integrity check remains anywhere in `judge.md`
- [ ] Clause (b) *Design soundness _(4.5%)_* is present, still separately answered, its meaning unchanged
- [ ] The checklist is still **10 rows**. The Purpose Check does not become row 11
- [ ] The row carries its base rate **and the reason it is kept on consequence rather than frequency**, in the grammar `conventions.md` §14 now requires: roughly 4 goal-based blocks in 149 reviews, against a miss that cost six days of work rejected wholesale. **No project is named inside the template** — `judge.md` ships to every TFW install and its grammar for provenance is a bare corpus figure (F13) _(corrected 2026-08-13, ONB R1)_
- [ ] The mapping-integrity check is also gone from `review.md` Step 3 — see AC-4. Removing it from the template and leaving it in the workflow ships DoF-11

Gate: read row 2; `grep -rc "mapping integrity" .tfw/templates/review/judge.md .tfw/workflows/review.md` → 0 in both; row count = 10; clause (b) diffs clean against `git show HEAD~:.tfw/templates/review/judge.md`
Evidence: the before/after of row 2, both clauses quoted in full

### AC-2: The check cannot be passed by assertion [depends: AC-1]

Four properties, all in `judge.md`, all failing conditions rather than advice:

- [ ] **Fused citation-and-harm** — one field, one sentence: quote the clause served **and** name the concrete harm at stake. A citation that resolves but is irrelevant fails. A harm asserted with no citation fails. `✅` with an empty field fails
- [ ] **Excess-and-adjacency** — does the result deliver something the cited clause does not ask for, or that a baseline non-goal, a DoF item or a phase boundary excludes?
- [ ] **Deferral confession** — does the spec or the result itself name a different home for this work and ship it here anyway? One sentence. _(added 2026-08-13, ONB Q3: frozen DoD-30 makes Phase D define the term, and a glossary article with no referent in the framework is a label that resolves and means nothing — S32 one layer up.)_
- [ ] **Override clause** — *"the TS scoped it this way"* and *"tests are green"* are stated as insufficient grounds to `✅`
- [ ] **Materiality bar** — the harm must be material impact on the value, never phrasing. A wording objection does not satisfy the harm clause (P14; AFD's first firing was a false positive on prose-only rationale)

Gate: fill the row against RF Phase B once, in the evidence file, and show a bare citation with no harm being rejected by the row's own wording
Evidence: the dry-run, with the failing variant shown beside the passing one

### AC-3: The reference set is stated, and the invalid references are named [depends: AC-1]

- [ ] `judge.md` states the reference set: the **master HL at its committed frozen baseline** plus the **Project North Star**
- [ ] The **TS** and any **Phase HL** are named as invalid references, with the one-line reason: the TS is downstream of any drift (P16), and a Phase HL holds nothing approved (`conventions.md` §3, Phase HL is derivation-only)
- [ ] The **fallback chain** is stated where the reviewer reads it: project north star → master HL §1 at the frozen baseline. The absence of a north star never blocks a review
- [ ] Recovering the baseline points at `conventions.md` §3 rule 15 — the recovery form is not restated (rule 15 exists so it can be corrected in one place; A13 is what happens when it is copied)

Gate: read the block; confirm no second copy of the recovery command exists in `.tfw/`
Evidence: N/A — textual, verified by reading

### AC-4: `review.md` carries the identity, the reference and the routing

- [ ] Line 28 reads **master HL at its frozen baseline**, not "Master HL for the task"
- [ ] The `HL §7 Principles check` paragraph in Step 3 is **replaced** by the Purpose Check instruction naming the reference set. Not deleted and not left: deleting costs the step its only content, leaving it makes the workflow instruct a check its own template no longer contains — which is DoF-11 verbatim. Budget-neutral, roughly 45 words out and 45 in _(added 2026-08-13, ONB Q1)_
- [ ] Reviewer Identity names the third defended object — goals, values and north star — alongside unverified claims and incomplete work, with authority to block work that is verified, complete and beside the point
- [ ] A goal failure is stated as sufficient grounds for **❌ REJECT with every quality check passing**; the finding is named **`not fit for purpose`**; the verdict **routes to the owner**, not back to the executor
- [ ] **No new verdict token.** The vocabulary stays `✅ APPROVE / 🔄 REVISE / ❌ REJECT`
- [ ] Identity text is not load-bearing: every property above is also enforced by AC-1–AC-3 in `judge.md`. D46 recorded *"Quality guardian, not rubber stamp"* and only the first half ever shipped — identity text in this repository has a measured survival rate of ½

Gate: `grep -n "frozen baseline\|not fit for purpose" .tfw/workflows/review.md`; confirm the verdict set is unchanged
Evidence: N/A — textual

### AC-5: `review.md` stays inside the attention budget [depends: AC-4]

F2: working range 700–900 words, hard degradation above 1,200. `review.md` is **1,065 words** today — TFW-56 shortened it by deleting the mode step.

- [ ] Final count is **below 1,200**, measured with `wc -w` and recorded with the before figure
- [ ] Every word removed to pay for an addition is a **genuine restatement**, paired in a ledger with the text it restated. Phase B's precedent: a removal that deletes the sole statement of a mechanism is forbidden, and manufacturing "duplication" to buy headroom is the trim this rule exists to prevent
- [ ] If the working range 700–900 is not reachable without such a trim, **report it, do not resolve it** — that is what Phase B did at 1,195 and the reviewer accepted it

Gate: `wc -w .tfw/workflows/review.md` before and after
Evidence: the word ledger, one row per removal

### AC-6: PV Index gains a source that answers "what are we building"

- [ ] `glossary.md` PV Index gains **priority 0 — Project North Star**: what we are building, why, **and what we are deliberately not building**. It is stated as distinct in kind from the seven existing sources, which are all *how we build*
- [ ] **Priority 1 is relabelled** `.tfw/README.md § Values and Principles — methodology values`. Reason to record: that section is byte-identical across projects and cannot carry project information; the current label "README Values" points at a section a real project does not have
- [ ] `conventions.md` defines the Project North Star with its **admission criteria** — a clause states what the product *is for* or *must never become*; if a single task's implementation choice could satisfy or violate it, it is a principle (HL §7), not a north star. This is a criterion, not a size cap
- [ ] The locus is a **designated section of a README**, and a **task HL may never be nominated** — excluded explicitly, one sentence _(owner ruling 2026-08-13, ONB Q2; the nominated-HL branch needs a project-level freeze mechanism this task has not scoped, and AFD's anchor grew 10 → 14 principles after approval with no log)_
- [ ] The anchor may be **more than one location**. This project's own north star is its philosophy across the root `README.md` and the founder essay `.tfw/README.md` (HL §11 S38)
- [ ] **Priority 0 and priority 1 may point at the same file, and the rule says so.** They are distinguished by what the section says — *what we are building* versus *how we build* — not by which file holds it. A project whose product is its own method may designate sections of one file to both. Without this clause the framework's own repository can never conform to the rule it ships
- [ ] The **"Who scans PV"** block below the index still resolves after the renumbering

Gate: read the index; confirm priorities 1–7 kept their content and only their labels moved
Evidence: N/A — textual

### AC-7: The HL template reaches the anchor structurally

- [ ] `templates/HL.md` header block gains a north-star field, placed **below** the contract block per that block's own instruction (*"Add further header fields below this block, not inside it"*)
- [ ] The field takes **one or more locations**, not a single path — this project's designation is two files
- [ ] The field states the fallback: project north star → master HL §1 at the frozen baseline
- [ ] A task with no project north star renders a valid header — explicit N/A grammar (F21), not an absent field

Gate: read the header; confirm the contract block is not modified
Evidence: N/A

### AC-8: The REVIEW template matches the checklist and surfaces the finding [depends: AC-1]

- [ ] `REVIEW.md` §3 row 2 wording matches `judge.md` row 2 one-for-one — TFW-56 DoD-6 made row-for-row alignment an invariant of this file
- [ ] The **Purpose Check finding is surfaced in the synthesis**, not only in the table: a `not fit for purpose` finding appears in §4 Verdict with its citation and its harm
- [ ] The template is still ten rows and no new section is added (F22)

Gate: diff `REVIEW.md` §3 against `judge.md`'s table row by row
Evidence: the ten-row alignment check

### AC-9: The citation namespace cannot collide

- [ ] `NS{n}` is declared for north-star clauses, `PP{n}` for a project principle registry (`KNOWLEDGE.md` §0 where a project has one), `P{n}` unchanged for HL §7
- [ ] `compilable_contract.md`'s `P{N}` row is corrected: it currently resolves `P{N}` to `KNOWLEDGE.md §0 Philosophy row`, a section **D37 removed**. `knowledge/constraint.md` F4 records the double semantics this created. Correct the row to HL §7 and add the two new rows. **One table, nothing else in that file**
- [ ] `PP{n}` is declared even though this repository has no §0 — it is a reserved namespace for projects that keep one, and reserving it is what stops the collision AFD has (three live `P8`s). If it is declared and unused here, say so in the RF rather than inventing a §0

Gate: `grep -n "P{N}\|NS{N}\|PP{N}" .tfw/compilable_contract.md`
Evidence: the corrected table

### AC-10: The two review-side anti-patterns are registered

- [ ] `conventions.md` §14: *a reviewer approves work that satisfies the TS but not the approved contract or the north star*
- [ ] `conventions.md` §14: *a reviewer asserts alignment without citing the clause it serves*
- [ ] Section-level coordination held (HL §7.1): Phase C appends to §14 and owns the review-flow description. Phase A's HL-contract entries and TFW-56's checklist-row entry are not edited

Gate: `git diff .tfw/conventions.md` shows additions only, in §14 and the north-star definition

### AC-11: Replay — the check fires on the failures and stays quiet on the sound work

DoD-29. A check that fires on everything is as useless as one that fires on nothing. This is also what `conventions.md` §14 now demands of any checklist row: an evidenced rate, or a written reason for keeping it on consequence.

- [ ] Run the Purpose Check as shipped against the **TFW-48/49 phase REVIEWs**, recovered with `git show 721ca15:<path>` — the reference set is the *approved* HL at `9e19a4f`, not the drifted one
- [ ] Run it against **three TFW reviews that were genuinely sound**. Recommended: `TFW-50`, `TFW-42/A`, `TFW-47/B`. Substituting one is allowed with the reason written; **do not use TFW-53's own phase reviews** — a check cannot be validated on the task that authored it
- [ ] **At least one non-approve on the former set, none on the latter.** If the check fires on a sound review, that is a finding about the check, not about the review — report it and stop, do not tune the corpus
- [ ] Every outcome carries the filled citation-and-harm field, so a reader can see *why* it fired or did not
- [ ] What the replay establishes is **discrimination, not a rate** — nine reviews cannot produce one. State that boundary in the replay file and check the result for consistency with the ~4-in-149 figure the row cites, rather than presenting nine samples as a measurement _(corrected 2026-08-13, ONB R3)_
- [ ] **Three of the six rejected-corpus replays run post-drift**, because TFW-48's pre-amendment HL was never committed — that is the documented TFW-48 failure and the reason DoD-5 exists. Record it per review as a divergence from *"the approved HL"*, never averaged away. It is the harder test, not the easier one _(ONB §5 risk 2)_
- [ ] A row that returns **the third outcome** (reference set inconsistent → owner) is recorded as such, not collapsed into "fired". TFW-49's approved contract is genuinely self-contradictory, so this is a likely and legitimate result _(ONB §5 risk 3)_

Gate: `purpose_check_replay.md` — one row per review, outcome, citation, harm
Evidence: the replay file, mandatory. This AC cannot be marked N/A

### AC-12: The third outcome exists and routes to the owner [depends: AC-1]

Frozen **DoD-23**, added by approved amendment A6. It had no acceptance criterion until the executor found the gap at ONB; this AC closes it.

- [ ] `judge.md` carries a third outcome distinct from pass and fail: **the reference set is internally inconsistent** — the baseline and the north star, or two clauses of the baseline, cannot both be satisfied
- [ ] It is recorded as a finding and **routed to the owner as a contract defect**, not to the executor as a work defect. The executor has no channel to a frozen section, so routing it down is routing it nowhere
- [ ] `review.md`'s routing block gains one clause for it — the mechanism lives in `judge.md`, which is off the F2 budget
- [ ] The precedent is stated in one line so the outcome is not read as theoretical: TFW-49's approved §1 promised *"readable without special tooling"* while its approved DoD-3 required a versioned structural validator. Part of the scope the owner later rejected was a faithful reading of the DoD the owner approved

Gate: read the block; confirm the routing target is the owner and that a reviewer can reach the outcome without leaving `judge.md`
Evidence: covered by AC-11 — at least one 48/49 replay row is expected to land here

---

> ## Second execution pass — corrective, added 2026-08-13
>
> **Origin:** [REVIEW Phase C](REVIEW__phase-c__goal_defence_in_review.md) 🔄 REVISE, discrepancy D1, verified independently by the coordinator against `9e19a4f` before being accepted.
>
> **What is *not* reopened**, stated first so the scope of this pass is unambiguous: no re-run of the replay corpus, no change to the Purpose Check mechanism, no change to the reference-set rule, the three tests, the override clause or the outcome table, no new evidence artifact, and no change to any of the seven framework files beyond AC-14's one blockquote. AC-1 through AC-12 keep their passing status. AC-11's pass condition holds at **4 of 6** and the 0-of-3 sound-corpus result is untouched. This is the correction of one reading, not a re-validation.
>
> **What the coordinator has already done, so you do not look for it and do not touch it:** HL §2's evidence row and §9's risk row are corrected, and a *correction of record* is appended below the §12 table. A6's row itself is **not** rewritten — the log is append-only. The HL is closed to you under the Role Lock; if you find another site, report it in RF §6 and I will land it.

### AC-13: Replay row 49/A is re-scored against the full sentence

The row ruled TFW-49 Phase A a **contract defect** on the reading that §1's *"readable without special tooling"* cannot be jointly satisfied with DoD-3's versioned structural validator. At `9e19a4f` the sentence continues — *"…without special tooling, **while structural validation prevents quiet drift** between Coordinator, Researcher, Executor, Reviewer, adapters, and repositories"* — and approved DoF-8 makes prose-only or unversioned-only enforcement a failure condition. §1 asks for both properties; DoD-3 discharges the second.

- [ ] The row quotes §1 **to the end of the sentence** and states that §1 pairs readability with structural validation
- [ ] The recorded outcome is what the shipped check actually returns — `✅ aligned`, or a fire on **excess** grounds if the 1,708-line delivery is argued that way, but **not** the third outcome
- [ ] The row's outside confirmation is corrected or dropped: TFW-50's approved *"one precise Markdown rule … without enforcement software"* ran under a **different** HL with no DoF-8, so it evidences a change in the owner's preference between two contracts, not an inconsistency inside one
- [ ] Every dependent site is propagated, none missed: `purpose_check_replay.md` §1, §3, the §0 research-divergence note and the §3 AC-11 condition table · **EV E11 and E12** · RF §3 AC-11 and AC-12 (drop *"Exercised for real: replay row 49/A"*) · RF §2 decision 6 · RF §5's `13/13`
- [ ] The re-score is recorded as a **correction with its cause named** — a quotation ended early — not silently rewritten. This phase's own thesis is that a change to a shipped artifact must be visible as a change

Gate: `git show 9e19a4f:tasks/TFW-49__agent_commit_identity_and_attribution/HL-TFW-49__agent_commit_identity_and_attribution.md` — read §1 whole and DoF-8, then diff every site named above
Evidence: the corrected replay row, with the full sentence quoted

### AC-14: The shipped precedent line no longer teaches the error [depends: AC-13]

`judge.md`'s Purpose Check block closes with a blockquote offering this same reading as **the canonical illustration of a contract defect**. It ships to every install, three paragraphs below the rule that *a citation which resolves but is irrelevant fails the row*. This is the item that outlives the task.

- [ ] The blockquote no longer presents surface tension between two clauses as joint unsatisfiability
- [ ] Either a pair of clauses that **genuinely cannot both be satisfied** replaces it, or — since the corpus now yields **zero** verified instances — the outcome's **shape** is described abstractly and the absence of an observed case is stated plainly. Saying "not observed" is better than shipping a weak example; HL §9's risk row now reads `Unmeasured` for exactly this reason
- [ ] The surviving true half of the old line — *part of the scope the owner later rejected was a faithful reading of the DoD the owner approved* — is **not** silently repurposed as a contract-defect example. It is a purpose or excess illustration, or it goes
- [ ] **No net word growth in `judge.md`.** A corrective pass may not grow the artifact it corrects; if the replacement is longer, pay for it inside the same block
- [ ] `review.md` is untouched by this AC and stays at its measured count

Gate: read the block; `wc -w .tfw/templates/review/judge.md` before and after
Evidence: the before/after blockquote, quoted in full

### AC-15: The two documentary defects are repaired [depends: AC-13]

- [ ] **RF §8 S2 is corrected or withdrawn.** Its premise — *"the check found its own predecessor's defect while being validated on it"* — rests on the ruling AC-13 removes. It is High confidence and bound for `KNOWLEDGE.md` at KNW, so approving it as written writes a false fact into project memory that later work will cite. What survives is smaller and still real: a replay is worth re-running whenever the check changes, and here the re-run **confirmed** research's original verdict rather than overturning it
- [ ] **The 48/A quotation marks are fixed.** The note reads *"preserves all ten mapped principles"* inside quotation marks; the source reads *"preserves Phase HL P1–P10"*. A paraphrase inside quotation marks is the same defect class as the truncation — in this phase of all phases, the form is part of the deliverable
- [ ] No other RF §7 or §8 item is touched — the reviewer checked all three RF §7 candidates and they hold

Gate: re-read both sources; confirm every remaining quotation in the replay and the RF is verbatim to its full sentence
Evidence: N/A — textual, verified against the sources named

### Evidence Artifacts

| File | Description |
|------|-------------|
| `evidence/EV__phase-c__goal_defence_in_review.md` | Environment header, per-AC table, verdict _(required)_ |
| `evidence/purpose_check_replay.md` | AC-11 corpus and outcomes _(required)_ |

## 6. Technical Guidance

> Reference material, not instructions. Deviate with justification in the RF.

**What TFW-56 changed under this phase, four hours before it started.** Read [RF TFW-56](../../TFW-56__review_mode_removal/RF__TFW-56__review_mode_removal.md) before touching anything:

- `review.md` steps renumbered — **Judge is Step 3**, not Step 4. The frozen HL Phase C context block still says "Step 4 Judge"; that pointer is stale, not a contract change
- The Judge checklist is **10 rows**, not 7. Rows 8/9/10 (evidence sufficiency, backward compatibility, safety) are new and carry measured rates inside the row — match that grammar
- Row 2 was **deliberately split into two quotable clauses** so this phase could replace one and leave the other. RF TFW-56 §6 observation 2: *"nothing in either task's frozen DoD requires it to. One line in Phase C's TS closes this."* AC-1 is that line
- `conventions.md` §14 gained: *a review checklist row is added without an evidenced firing rate*. AC-11 is how this phase satisfies it
- `verify.md` gained a **Claim & Source Checks** section — unrelated, do not disturb
- `VERSION` is `1.1.0`. Phase D bumps again; do not touch it here

**No amendment to TFW-53 is required by TFW-56.** Every frozen DoD 18–29 was checked against the shipped state: none names a mode file, the mapping-integrity check still exists as clause 2(a) so DoD-20 has its target, and `review.md` got *shorter*, which makes DoD-28 easier. TFW-56's own DoF-8 — *"the change collides with TFW-53 Phase C and forces an amendment against its frozen DoD"* — did not trigger.

**If forced to choose, the order is frozen** (HL §4 Phase C, deliverable weighting): reference-set rule > forcing function > `judge.md` row > identity text. The anchor degrades gracefully; the reference-set rule does not.

**Word ledger for `review.md`.** Line 28 revision ≈ +8, invalid-reference statement ≈ +22, Reviewer Identity third clause ≈ +32, verdict routing ≈ +28, third-outcome clause ≈ +14. The Step 3 paragraph replacement is **budget-neutral** — roughly 45 words out, 45 in. Total ≈ +104, landing near **1,170 of 1,200**. Stated up front so it is not discovered at ONB the way AC-6 was in Phase B; revised 2026-08-13 after the ONB priced the two items the first ledger missed.

**Negative controls worth reading before writing the row:** `AFD-38/phase-b/review/judge.md` — a Judge that scored `✅` on the very AC containing the violation, then had its APPROVE retracted by its own author. And `AFD-48/phase-b/` — the false-positive precedent that produced the materiality bar.

## 7. Definition of Failure

- ❌ Clause (b) *Design soundness* is lost, weakened, or fused back into a single unquotable sentence — a 4.5% check with six hard failures deleted as collateral
- ❌ The Purpose Check ships as row 11. The tail positions are the weakest ones for an LLM judge (HL TFW-56 §7.2 #25), and the strongest new check must not sit there
- ❌ The check can be satisfied by a citation alone, or by a harm alone — the two halves must be one field
- ❌ A wording objection satisfies the harm clause. That is P14's failure and AFD's first firing
- ❌ The TS or a Phase HL is left usable as a reference point
- ❌ The mapping-integrity check survives anywhere — in `judge.md` or in `review.md` Step 3. HL DoF-11 names *"reverts to mapping integrity"* as a failure of this phase, and the check currently has two live statements
- ❌ The third outcome ships without a route to the owner, or routes to the executor
- ❌ A project name appears inside a shipped template (F13)
- ❌ The corrective pass reopens the mechanism, the corpus or an already-passing AC — the scope of the second pass is three documents and one blockquote
- ❌ A weak contract-defect example is substituted for the withdrawn one rather than admitting the corpus has none
- ❌ `judge.md` grows on a corrective pass, or a corrected quotation is fixed without naming why it was wrong
- ❌ A new verdict token is introduced, or a fifth review stage appears in any form
- ❌ `review.md` crosses 1,200 words, or headroom is bought by deleting the sole statement of a mechanism
- ❌ The replay is skipped, marked N/A, or run against TFW-53's own reviews
- ❌ Adapter copies, glossary term articles, or a north star for this repository are written here — all three are later phases
- ❌ A vendor mechanism is named in `conventions.md` or `glossary.md` (HL §7.1)

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| The Purpose Check becomes a rubber stamp — `✅ aligned` 145 times in 149 | The fused citation-and-harm field makes `✅` cost work; AC-11 measures whether it discriminates at all |
| It becomes the opposite — reviews blocked on phrasing | The materiality bar ships in the same pass, not after. AFD retro-fitted it and paid for a false positive first |
| Row 2 grows into a paragraph | Two clauses, each one quotable sentence. TFW-56 set the length precedent for rows 8–10 |
| The north star does not exist yet in this repository, so the mechanism is untested where it matters most | The fallback chain is a first-class AC, not a footnote. TFW-55 fills the anchor; this phase must work before it does |
| `review.md` budget squeezed between AC-4's additions and F2 | Ledger up front (§6); report rather than trim, per Phase B |
| Phase D finds three terms shipped without glossary articles | Deliberate — Phase D deliverable 1 owns them. Named in §2 so it does not read as an omission |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `.tfw/conventions.md` | A (§3 + HL-contract §14 entries), B (§14), E (§5, §13, §14) | C appends only. Never rewrite another phase's entries |
| `.tfw/glossary.md` | D (term articles) | C adds PV Index rows; D adds the articles. Do not pre-empt |
| `.tfw/templates/HL.md` | A (contract header, §12), B (§3.1 corrective) | C appends one field **below** the contract block |
| `.tfw/templates/review/judge.md`, `review.md`, `REVIEW.md` | TFW-56 (landed) | Read RF TFW-56 first. Row 2 clause (b) is the trap |
| adapter copies | D | Out of scope here by design |

---

*TS — TFW-53 / Phase C: Goal Defence in Review | 2026-08-13*
