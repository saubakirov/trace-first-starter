# ONB — TFW-56: Remove the Review Mode Axis

> **Date**: 2026-08-13
> **Author**: Executor (Claude Code)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-56](HL-TFW-56__review_mode_removal.md) — 🔒 FROZEN, re-frozen 2026-08-13 after A1–A5, A7
> **TS**: [TS TFW-56](TS__TFW-56__review_mode_removal.md)
> **Research**: [iteration 1](research/iter1/RES.md)

---

## 1. Understanding

Delete the `code / docs / spec` **selection** from review — not the checks it gated. Three
byte-identical mode files, the `tfw.review.default_mode` config key, `review.md`'s mode step with its
🛑 WAIT, and four `Mode:` template fields go away. The eight mode-specific checklist rows are
re-homed by **measured residue**, not by name: four converging rows (Test coverage 23.4% · Analytical
quality 25.0% · Source attribution 22.2% · Source verification 12.5%) become one universal row **S1
Evidence sufficiency** at a combined 16.1%; Breaking changes → **S2 Backward compatibility** (8.5%);
Security → **S4 Safety** (4.0%, retained on consequence); Code quality → **S3 Design soundness**
folded into **U2 Philosophy aligned** (4.5%, six hard ❌ that are contract violations); Content
quality is dropped as the one true duplicate of U4. The universal Judge checklist goes 7 rows → 10.
Three orphaned `docs`/`spec` **verify** actions get an unconditional home in `verify.md`. Then the
six adapter copies re-sync, `config.md`'s propagation table loses a row, `conventions.md` gains an
anti-pattern so the axis cannot regrow, `glossary.md` stops making "review mode" mean two things,
TD-106 closes by deletion rather than annotation, and the acceptance test is a recorded grep.

Net: 3 files deleted, ~19 modified, 1 new evidence artifact, negative LOC. History is not rewritten
— every existing `Review Mode` header in `tasks/` and every past CHANGELOG entry stays as written.

## 2. Entry Points

| # | File | What I need from it |
|---|------|--------------------|
| 1 | `.tfw/workflows/review.md` | Step 1 (mode + 🛑 WAIT, L52-61), Step 3 mode-file load (L76), Trust Protocol (L40-50), anti-pattern step reference (L154). Steps 0-8 → 0-7 |
| 2 | `.tfw/workflows/review/{code,docs,spec}.md` | 42 lines total. Read line by line for the AC-3 / AC-4 accounting — 8 checklist rows + 10 verify actions |
| 3 | `.tfw/templates/review/judge.md` | `Mode:` (L4), Universal Checklist 7 rows (L9-17), Mode-Specific section (L19-21), Checkpoint (L30-39) |
| 4 | `.tfw/templates/review/verify.md` | `Mode:` (L4), Checkpoint (L55-67) — the destination for the three orphaned verify actions |
| 5 | `.tfw/templates/review/map.md` | `Mode:` (L6) |
| 6 | `.tfw/templates/REVIEW.md` | `Review Mode` header (L6), §3 Judge table (L27-35) — **currently 6 rows, not 7**, plus the mode placeholder comment |
| 7 | `.tfw/project_config.yaml` L59-61 · `.tfw/templates/project_config.yaml` L63-65 | The `tfw.review` block. `default_mode` out, `min_verify_ratio: 0.42` untouched |
| 8 | `.tfw/workflows/config.md` L88-93 | `review` registry section — two rows |
| 9 | `.tfw/conventions.md` | §3 Review subfolder (L262-264), §11 Design Rules (L466), §14 (L495 + new anti-pattern) |
| 10 | `.tfw/glossary.md` | L127-128 Reviewer heading + "mode-aware checklist (6 universal + mode-specific)"; L142 `review.md` Step 4 pointer |
| 11 | `.tfw/VERSION` (`1.0.0`) · `.tfw/CHANGELOG.md` (`## [Unreleased]` at L6) | Bump + entry with a `### Removed` block naming the key |
| 12 | 6 adapter copies | `.claude/commands/tfw-{review,config}.md`, `.agent/workflows/tfw-{review,config}.md`, `.tfw/adapters/codex/skills/tfw-review/SKILL.md` L19, `.agents/skills/tfw-review/SKILL.md` L19 |
| 13 | `TECH_DEBT.md` L22 | TD-106 row, status `⬜ Backlog` |

**Verified before starting:** all four full-file adapter copies (`.claude/commands/tfw-review.md`,
`.agent/workflows/tfw-review.md`, `.claude/commands/tfw-config.md`, `.agent/workflows/tfw-config.md`)
are **byte-identical** to their `.tfw/` sources today (`diff` → empty). Re-sync is a byte copy, and
AC-9's "nothing project-specific was clobbered" check has a clean baseline.

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | **What version does `VERSION` become?** TS AC-10 and HL DoD-12 say only "bumped". Current is `1.0.0`, and this is the first bump inside 1.x, so there is no in-repo precedent. `RELEASE.md` §3 is not silent but it points somewhere uncomfortable — its MAJOR row reads *"Template field renamed, status flow changed, **required file removed**"*, and this task removes three framework files and four template fields. Against that: nothing downstream actually breaks. An upgrading project keeps its existing REVIEW files verbatim, and the orphaned `default_mode: code` line is inert, not corrupting. **(a) `2.0.0`** — the letter of RELEASE.md §3; the removal is visible at a glance and `/tfw-update` treats a major as a read-the-CHANGELOG event. Cost: 2.0.0 for one deletion task sets a low bar for future majors. **(b) `1.1.0`** — matches observed behaviour: a backward-compatible removal of an internal mechanism, `### Removed` block carrying the detail. Cost: contradicts RELEASE.md §3 as written, so either the bump or the rule is wrong and one of them should be corrected. **(c) `1.0.1`** — rejected on my side; three deleted framework files are not a clarification. **My recommendation: (b) `1.1.0`**, and note in Observations that RELEASE.md §3's "required file removed" clause needs the owner's eye, because a framework that must go major every time it deletes an unused file will stop deleting unused files. | **`1.1.0`** — owner, 2026-08-13. Option (b). RELEASE.md §3's "required file removed" clause is left as-is and goes to Observations for the owner's own call. |

> Everything else below is non-blocking: I have a defensible path for each and will state the choice
> in the RF rather than stall on it.

## 4. Recommendations (suggestions, not blocking)

1. **Migrate all three orphaned verify actions rather than declining any.** AC-4 permits either, and
   A2's own alternative (b) allows a written decline. But *spot-check 2-3 key claims/sources*,
   *check citations traceable to real artifacts* and *verify data claims against primary sources* are
   the Verify-stage half of the same convergence S1 is the Judge-stage half of — the check whose
   combined firing rate is 16.1%. Declining any of the three would hand S1 a Judge row with no
   Verify-stage action to feed it. Destination: `verify.md`'s **Checkpoint**, alongside the existing
   *"Ran at least 1 build/test command (or documented why not)?"* — that is the file's established
   structural-enforcement site, and it is where `code`'s build/test action already lives
   unconditionally. I will also add a short claim-spot-check block to the Verification Log so the
   Checkpoint item has somewhere to record its result, and will name the exact lines in the RF.

2. **Word U2 so its design-soundness clause is a separately quotable sentence.** TFW-53 Phase C
   DoD-20 (frozen) *replaces* the Judge "mapping-integrity check" — and Phase C's context block names
   `judge.md` **Universal Checklist row 2** as its target. S3's approved home is that same row. If U2
   is rewritten as one fused sentence, Phase C's replacement takes S3's 4.5% / six hard ❌ out with
   it, silently. If the design-soundness clause is its own sentence with its own rate cited, Phase C
   can replace the mapping-integrity clause and leave S3 standing. This costs nothing here and is
   the only in-scope thing I can do about it. See Risk 1.

3. **Leave `conventions.md` §11 L466 (*"Mode files loaded at Step 2, not at start"*) unedited.**
   Its phrasing is inherited from D42, which is about review mode files — but it is also, and after
   this task exclusively, **true of research**: `.tfw/workflows/research/{focused,deep}.md` exist and
   are selected at `research/base.md` Step 2. The sentence therefore survives as a true statement
   about the only mode files left. Editing it would be a third change to `conventions.md` that AC-8
   does not ask for. I will report it in Observations so a later reader knows the ambiguity was seen
   and priced, not missed.

4. **Fix `glossary.md` L142** — Principles Check ends *"→ `templates/TS.md` §3, `review.md` Step 4"*.
   After renumbering, Judge is Step 3. This is inside `.tfw/`, so DoF-3 covers it, and `glossary.md`
   is already a MODIFY file. Not a scope expansion — a stale pointer created by this task's own
   renumbering. `glossary.md` L157 (Session Naming → `review.md` Step 0) needs nothing; it becomes
   true for the first time.

5. **Write the §14 anti-pattern to satisfy both formulations.** HL DoD-9 (frozen) says *"a review
   checklist row that cannot produce a finding"*; TS AC-8 says *"a review checklist row whose firing
   rate is not evidenced"* — A6 sharpened DoF-2 but did not touch DoD-9, so the two acceptance
   surfaces now differ. One row covering both readings satisfies each without needing an amendment.
   See Inconsistency 1.

6. **Run a stronger sweep alongside the mandated grep, and record both.** See Risk 3 — the
   mandated pattern has a dead alternative. AC-12's command runs verbatim with its output recorded as
   required; the supplementary sweep is additional evidence, not a substitute.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **TFW-53 Phase C will evict S3 unless its TS is told not to.** *(highest-value item in this ONB.)*
   TFW-53 DoD-20 is frozen and reads: *"The Judge mapping-integrity check is replaced by a
   substantive Purpose Check."* Phase C's context block points at `judge.md` Universal Checklist
   **row 2** — the row A1 gives S3 to. Neither task's DoD notices: TFW-56 DoF-1 fires on coverage
   lost *by this task*, and TFW-53's DoD says nothing about mode rows because none existed when it
   was frozen (HL §8 verified exactly that and concluded "no amendment required" — correctly, for the
   files, but the *row* was not in view). Consequence if unhandled: S3 lands, then disappears at
   Phase C with no §12 row anywhere, which is the silent-contract-edit failure mode TFW-53 exists to
   prevent. This does **not** make Phase C unlandable, so TS §6's stop condition is not triggered and
   I am proceeding. Mitigation within my scope: Recommendation 2. Outside my scope: Phase C's TS
   needs one line, and this belongs in TECH_DEBT or a cross-task note at review time. It is not
   mine to file.

2. **S1 sits at position 8 of 10 — the position the research warns about.** HL §7.2 #25 records
   that LLM judges are order-sensitive and that appending promoted rows at positions 8-11 is *"the
   shape the research warns about"*; DoF-2 as sharpened by A6 names a set that pushes rows past being
   read. HL §3.1's frozen after-diagram puts S1 at 8, S2 at 9, S4 at 10, and I will implement that
   order — it is not mine to change, and it is better than it looks: S1 at 8 lands **adjacent to U7
   at 7**, which is the pairing AC-2 needs, since the contrast is legible only when the two rows are
   read together. The residual risk is real for S2 and S4 in the tail, and the mitigation the HL
   chose is the structural explicit-N/A grammar, not reordering. I am recording it so the reviewer
   sees a priced decision rather than an oversight.

3. **The mandated grep gate has a dead alternative and a case-sensitivity hole.** `review/{code`
   matches nothing in the tree **today, before any change** — the real string is
   `.tfw/workflows/review/{mode}.md`. So one quarter of the gate has never been able to fail, which
   is, with some irony, the anti-pattern this task is adding to §14. Two further blind spots: the
   pattern is case-sensitive, so `glossary.md`'s lowercase *"coordinator in review mode"* is invisible
   to it, and `config.md`'s `review.default_mode` registry row does not match `default_mode: code`.
   AC-8 and AC-9 cover those three places by other means, so the ACs together are sound — the single
   command is not. Handling: run AC-12's command verbatim and record its output as required, then
   record a supplementary sweep (`-i`, plus `review/{mode}`, `Mode:`, `mode-specific`, `mode file`)
   as separate evidence. I am not modifying the AC.

4. **`min_verify_ratio`'s propagation pointer self-corrects, and that is worth stating.** AC-7
   requires `config.md`'s `review.min_verify_ratio` row to name the correct step. It currently reads
   `Step 2: Verify`; Verify is Step **3** today, so the row is stale — and becomes correct with no
   edit once Step 1 is deleted. Same for `review.md` L154 and `conventions.md` L495, both of which
   say *"Step 2 (Verify)"* and are wrong today. Three stale references heal passively. I will verify
   each rather than assume it, and record the before/after, because "we changed nothing and it became
   correct" is exactly the claim a reviewer should distrust.

5. **`.tfw/` sources are LF, `TECH_DEBT.md` is CRLF.** TS §6 warns about CRLF generally; the split is
   per-file. Editing `TECH_DEBT.md` with LF endings would produce a whole-file diff and obscure the
   one-row TD-106 change. I will keep each file's existing endings and confine diffs to changed lines.

6. **A `git rm` of the folder is required, not a file-by-file delete.** DoF-7 rejects "an empty
   `review/` folder left in place". On Windows, deleting three tracked files leaves the directory
   present in the working tree. I will remove the directory itself and confirm with `ls` that it
   errors — which is also AC-1's gate.

7. **`site/` holds generated pages for the files being deleted** — `site/404.html` and siblings
   reference `/reference/workflows/review/{code,docs,spec}/`. It is **untracked** (`git ls-files site`
   → 0 entries), so it is build output, not a consumer, and it is outside every path the grep gate
   walks. No action; recorded so nobody re-discovers it as a leak. `docs/scripts/gen_docs.py` is
   clean (no `review` match), confirming RES D9.

## 6. Inconsistencies with Code (spec vs reality)

1. **HL DoD-9 and TS AC-8 state the §14 anti-pattern differently.** HL: *"a review checklist row
   that cannot produce a finding"*. TS: *"a review checklist row whose firing rate is not evidenced"*.
   A6 sharpened DoF-2 only, leaving DoD-9 on the older wording. Both are satisfiable by one row that
   states the rule and its test; that is what I will write. No amendment needed — but the reviewer
   should know the two documents were reconciled deliberately rather than one of them being ignored.

2. **`templates/REVIEW.md` §3 has 6 rows; `judge.md` has 7.** The Evidence completeness row added to
   `judge.md` by TFW-46 never reached `REVIEW.md` §3. AC-5 requires the two to match row-for-row,
   so bringing §3 to ten rows silently repairs a pre-existing TFW-46 defect. Stating it so the extra
   row is not read as scope creep. HL DoD-3's arithmetic ("the seven existing ones ... plus three")
   is correct against `judge.md`, which is the right reference.

3. **`glossary.md` L128 says the checklist is "6 universal + mode-specific".** Already wrong by one
   before this task (7 universal since TFW-46). It becomes 10 and non-mode-aware. In scope under
   AC-8's "`glossary.md` defines no review-mode term".

4. **HL §7.2 #8 cites D25 for review mode files.** D25 is *research* modular architecture
   (`research/{base,focused,deep}.md`); the review mode files are **D42**, which HL §7.2 #1 already
   cites correctly. The Progressive Disclosure argument the citation is reaching for is genuinely
   shared by both records, so the citation is imprecise rather than hallucinated — it resolves to a
   real D-record whose *principle* applies. Flagging it because the reviewer's Knowledge Citations
   check tests link resolution, and this one resolves to a row about a different mechanism.

5. **HL §7.2 #11 cites `.tfw/README.md` § "Naming Creates Behavi**o**ur"; the heading is "Naming
   Creates Behavi**or**"** (US spelling). Resolves; noted only so the citation check does not read a
   spelling variant as a miss.

## 7. Knowledge Citations

> Read HL §7.2 in full. All 26 citations were opened and resolved to real items. Two are imprecise
> and are flagged in §6 (#4, #5); none is a hallucination.

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | `D42` — Review mode files, Progressive Disclosure | ✅ | Applied — the decision being revoked. Its premise ("44% of the old checklist was code-only") is not what I am touching; its mechanism is. AC-10's CHANGELOG entry records the revocation | KNOWLEDGE.md L74. Also carries the "loaded at Step 2" phrasing that L466 inherits (Rec 3) |
| 2 | `D41` — 4-stage review + mode selection with 🛑 WAIT | ✅ | Applied — Map/Verify/Judge/Decide and the per-stage mindsets survive untouched; only the mode-selection clause is removed | Confirms the stage flow is not in scope |
| 3 | `D46` — Reviewer Identity, Trust Protocol, WAIT gate | ✅ | Applied — the WAIT gate loses its subject; the Reviewer Identity block (`review.md` L35-36) and the 9-row Trust Protocol (L40-50) are preserved verbatim. The Trust Protocol row *"Tests pass → re-run or check test file exists"* is where one deleted `code` verify action already lives, per AC-4 | Verified the row exists before relying on it |
| 4 | `D49` — Requirements-first TS, AC as the binding declaration | ✅ | Applied — Principle 4's basis: the TS already declares what to check, so nothing needs to declare it again behind a gate | |
| 5 | `D52` / `D53` — Evidence Layer, mandatory `evidence/`, 4-status vocabulary | ✅ | Applied — the EV file is created under `tasks/TFW-56__review_mode_removal/evidence/` per D53, and only VERIFIED / DEFERRED / BLOCKED / N/A are used | D53's precedent (revoking TFW-46 D16) is also cited at #9 |
| 6 | `D54` — Adapter parity is behavioural, not byte-level | ✅ | Applied — AC-9. Convenient here: all four full-copy adapters are byte-identical today, so parity is provable both ways | |
| 7 | `D28` — Naming creates behaviour; one name = one behaviour | ✅ | Applied twice — AC-2 (S1 must not read as U7) and AC-8 (`glossary.md` L127-128, so "review mode" stops meaning two things) | The strongest constraint on the S1 wording |
| 8 | `D25` — Progressive Disclosure | ✅ | Applied as a principle, N/A as a record — D25 documents *research* mode files, not review ones. The principle holds: disclosure earns its cost only if the loaded content earns its load | Imprecise citation → §6 #4 |
| 9 | `D53` revoking TFW-46 D16 | ✅ | Applied — the precedent that a recorded decision is revoked in the open by a later task. D42 follows the same route | |
| 10 | `.tfw/README.md` § **Structural Enforcement** | ✅ | Applied — AC-12's recorded grep, and the choice to put the three verify actions in `verify.md`'s Checkpoint rather than in prose | README L100 |
| 11 | `.tfw/README.md` § **Naming Creates Behavior** | ✅ | Applied — *"if you have to explain what a step does, the step is named wrong"* is the cleanest statement of why the mode step goes: it needed a config key, a three-line table and a WAIT to explain itself | README L108-110. Spelling variant → §6 #5 |
| 12 | `.tfw/README.md` § **Single Source of Truth** | ✅ | Applied — six copies of the mode step is the cost being removed; the re-sync is a byte copy from one source | README L112 |
| 13 | `philosophy.md` F13 — domain-agnostic, no code-specific terminology | ✅ | Applied — bars the extension option outright, and constrains the S2/S4 wording: "Backward compatibility" and "Safety" must read for a report or a curriculum, not only for an API | F13 L20 |
| 14 | `philosophy.md` F21 — explicit N/A over silent skip | ✅ | Applied — the load-bearing one. AC-2's last bullet makes a skipped promoted row *visibly* marked; a silent ✅ fails the AC. This is what keeps S4 at 4.0% honest instead of decorative | F21 L28 |
| 15 | `philosophy.md` F22 — template minimalism, «не захламляй шаблон» | ✅ | Applied — four `Mode:` fields and a placeholder comment leave; three rows arrive. Net template surface shrinks | F22 L29 |
| 16 | `philosophy.md` F20 — investigative vs procedural workflow classes | ✅ | Applied — review stays investigative and staged. This task removes a *parameter*, not a stage, which is why steps renumber rather than restructure | F20 L27 |
| 17 | `philosophy.md` F24 — instructions produce compliance, heuristics produce competence | ✅ | Applied — 33 ✅ of 38 locally is compliance. It shapes how the promoted rows are worded: each asks a question with a failure mode, not "confirm X" | F24 L31 |
| 18 | `process.md` F19 — `review.md` is the only workflow with a non-standard Step 0 | ✅ | Applied — the anomaly is deleted. F19 becomes historical; its file is **not** in TS §4, so I am not editing it, and it goes to Observations for `/tfw-knowledge` | process.md L26 |
| 19 | `TECH_DEBT.md` TD-106 — the Step 0 renumbering trap | ✅ | Applied — AC-11 closes it; its warning is the source of Risk 4's "verify, don't assume" stance | TECH_DEBT L22, status `⬜ Backlog` |
| 20 | `conventions.md` §6 — scope budgets, project override to 30 | ✅ | Applied — 22 files against 30/15/3000/30. Within budget on every axis, net LOC negative | |
| 21 | `conventions.md` §14 — anti-patterns registry | ✅ | Applied — AC-8's new row, plus the executor-side rows that govern me: no out-of-scope fixes, no RF before the build gate, Observations mandatory | Wording conflict → §6 #1 |
| 22 | HL TFW-53 §4 Phase C — the base-rate argument | ✅ | Applied — and it is the reason S1's rate is quoted *in the row*: a promoted row that cannot show a rate is the fifth review stage all over again | Also the source of Risk 1 |
| 23 | External — Gawande, Do-Confirm selection by consequence | ✅ | Applied — S4 Safety at 4.0% is retained on consequence, and its row says so, so the next person to audit rates does not delete it as ceremony | 2_gather G7 (L258+) |
| 24 | External — 5-9 item working-memory band | ✅ | Applied as a constraint I must not exceed: exactly 10 rows, no eleventh, and the explicit-N/A grammar carries the load instead | Basis of Risk 2 |
| 25 | External — LLM-as-judge composite dilution, order sensitivity, redundant criteria | ✅ | Applied — three ways: Content quality is dropped rather than kept "just in case" (redundancy degrades judges); S1 is placed adjacent to U7 so the contrast is read, not inferred; and the tail-position risk is recorded rather than waved off | Basis of Risk 2 |
| 26 | External — role/persona priming, two-sided effect | ✅ | N/A to my implementation, applied to my reporting — H6 is unresolved and the test is unavailable, so I cannot verify the label's absence is harmless. I will not claim in the RF that removing the label had no behavioural effect. C5 (a non-gated descriptor) stays available to the owner | Standing limitation, HL §10 |

**New items the coordinator did not cite, which I found relevant:**

| # | Source | Item | Why it matters here |
|---|--------|------|--------------------|
| N1 | `RELEASE.md` §3 Version Scheme | MAJOR = *"Breaking changes to conventions, templates, or workflow structure — template field renamed, status flow changed, required file removed"* | The only rule in the repository that speaks to blocking Q1, and it points at 2.0.0 while the observable impact points at 1.1.0 |
| N2 | `RES` iter1 FC5 / HL §8 last row | `min_verify_ratio` sits inside a `tfw.review` block that `update.md` marks *framework → update*, so a project that tuned 0.42 loses it on any upgrade | Pre-existing and explicitly **not** caused by this task. AC-6 proves I did not make it worse; it is a TECH_DEBT candidate at review time, per HL §8 |
| N3 | `conventions.md` §3 rules 17-19 (delegated authority) | A mandate is a ceiling; no agent widens its own grant; delegation never authorises an overrun | Governs Risk 1 and Recommendation 3: I fix what this task's renumbering broke, and report the rest instead of absorbing it |
| N4 | `philosophy.md` F4 (via HL TFW-53 §4 Phase C context) | Structural enforcement over exhortation — cited by Phase C after AFD's memory-only rule proved non-portable | Reinforces putting the three verify actions in the Checkpoint, which is machine-checkable, rather than in Verify prose, which is not |

---

*ONB — TFW-56: Remove the Review Mode Axis | 2026-08-13*
