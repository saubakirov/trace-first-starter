# ONB — TFW-53 / Phase B: Enforcement in Workflows

> **Date**: 2026-08-13
> **Author**: Executor (Claude Code)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-53](../HL-TFW-53__hl_contract_and_goal_defence.md) — 🔒 FROZEN
> **TS**: [TS Phase B](TS__phase-b__enforcement_in_workflows.md)
> **Baseline**: `git log --format="%h %s"`, filtered on `^\S+ \[[^]]*/TFW-53/freeze/` → 5 commits, latest `ffe6c6a`

---

## 1. Understanding

Phase A put the contract in the artifacts. Two workflow instructions still tell the coordinator to do
the thing the contract forbids: `plan.md`:106 (`Update HL with research findings`) and `plan.md`:117
(`update HL → present diff → user confirms`). Phase B replaces both with classification, gives the
amendment verdict its two paths, adds a re-freeze commit at the new baseline, and turns
`research/base.md` Step 6 from one undifferentiated recommendation table into the two classes Phase A
shipped in `templates/RES.md`. Two files, no new files, and one hard numeric constraint (AC-6) that I
believe is unsatisfiable as written — see Q1.

## 2. Entry Points

| File | What I touch |
|------|-------------|
| `.tfw/workflows/plan.md` | Step 4 (approval → contract state + freeze commit), Step 6c (classify, not update), verdict handling + re-freeze. 1,206 words (`wc -w`) |
| `.tfw/workflows/research/base.md` | Step 6 items 3 (two classes, target section) and the Role Lock restatement. 869 words |
| Read-only, shipped in Phase A | `conventions.md` §3 rules 1–21 (rulebook — referenced, never restated), `templates/RES.md` (class names and column grammar AC-4 must match), `templates/HL.md` header (`Contract` / `Baseline` field wording AC-1 must match) |
| Test corpus | `research/iter2/RES.md` §HL Update Recommendations — 15 refinements, 3 amendment proposals, 4 "coordinator notes" (AC-2 replay); `HL-TFW-53` §12 — 12 rows, 5 freeze commits (AC-3 replay) |

## 3. Questions (blocking — cannot proceed without answers)

### Q1 — AC-6's three bullets cannot all hold. Which one governs?

| Item | Words |
|------|------:|
| `plan.md` now | 1,206 |
| Step 6c now (of which the two "update HL" lines = 26) | 128 |
| AC-1 — Step 4 approval + freeze commit | +35 |
| AC-2 — classify / apply / log / escalate replacement | +65 |
| AC-3 — both verdict paths + re-freeze | +55 |
| Reclaimed inside Step 6c (its gate states the `min_iterations` override twice) | −30 |
| **Projected** | **≈1,305** |

Bullet 1 (`< 1,206`) is reachable only by cutting ~140 words from steps other than 6c — which bullet 2
forbids. Options:

- **(a) Honour bullet 1.** Take the reduction from measured duplication: the Mindset paragraph on
  recommending RESEARCH (33 words) restates Step 6a's first three bullets; Step 7's folder tree (~35)
  restates `conventions.md` §4; the Footer self-check (52) restates §14 and then links to it. Lands
  ≈1,150 — under F2's 1,200 as well. Breaks bullet 2's provenance clause.
- **(b) Honour bullet 2 literally.** Land ≈1,305, report bullet 1 failed.
- **(c)** Ship AC-1–AC-5, report AC-6 failed per its own bullet 3.

**Recommend (a).** Frozen DoD-17 requires F2's budget (≤1,200 hard, 700–900 working), which AC-6's
`< 1,206` does not satisfy at 1,205; TD-141 already records DoD-17 as unreachable at this phase's start.
A provenance preference is cheaper to break than a frozen DoD item, and no mechanism is lost.

**Answer:** ✅ **(a). Proceed. AC-6 was written wrong and I have rewritten it — re-read it before starting.**

You are right and the error is mine. AC-6 bullet 1 said *"below 1,206"* — the starting figure — when the frozen **DoD-17 requires F2's budget: ≤1,200 hard, 700–900 working**. At 1,205 my AC passes and the frozen DoD fails. A TS criterion weaker than the contract it serves is a defect in the TS, and you found it by arithmetic before writing a line.

Bullet 2's provenance clause existed to stop one thing: **trimming a mechanism to hit a number.** Deleting text that restates a rulebook is not that. All three items you name — the Mindset paragraph restating Step 6a, Step 7's folder tree restating `conventions.md` §4, the Footer self-check restating §14 and then linking to it — are duplication of the exact kind **DoF-3 forbids adding**. Removing existing instances is consistent with the phase, not an exception to it.

So: target is **F2's budget, 700–900 working and ≤1,200 hard**, and the reduction may come from measured duplication anywhere in the file. Two conditions: quote the duplication you remove alongside what it duplicates, so the reviewer sees a deletion of a restatement and not a trim; and bullet 3 still governs — if a mechanism would have to go to reach the number, stop and report.

### Q2 — `templates/RES.md`:133 is a third live "update HL". DoF-1 or DoF-4?

The line reads `**SUFFICIENT** — proceed to /tfw-plan to update HL and write TS`, in the
researcher-facing template, shipped by Phase A. DoF-1 fails the phase if *"either 'update HL'
instruction survives in any form, including qualified"*. DoF-4 fails the phase if *"any file outside
the two named in §4 is modified"*, and §2 says the templates are Phase A — *"read them, do not edit
them"*. Two DoF items point opposite ways at one line. **(a)** Leave it, record it as an observation
(my default — §2 is explicit, and both AC gates grep only `plan.md`); **(b)** authorise the one-word
fix here as a corrective pass, documented in the RF; **(c)** route it to Phase D. It matters because
it is the surviving-channel argument from iter1 G10 — the same reason `templates/RES.md`:32 had to die
in Phase A.

**Answer:** ✅ **(b). Authorised. Fix it here, narrowly, and disclose it.**

DoF-1 and DoF-4 do point opposite ways, and DoF-1 is the one that means what it says. The surviving-channel argument (iter1 G10) is the whole reason `templates/RES.md`:32 had to die in Phase A — and Phase A killed 32 and missed 133. Routing it to Phase D leaves a *researcher-facing* template telling the researcher that the coordinator will "update HL", for three more phases, read once per iteration. That is the defect this task exists to remove, left running because of a scope line I wrote.

Scope, tight: **one clause on line 133 and nothing else in that file.** TS §4 now carries `templates/RES.md` as a corrective entry with that limit stated, so DoF-4 no longer contradicts it. Disclose it in RF §1 as a Phase A correction rather than Phase B scope, and record which Phase A AC should have caught it — that belongs in the RF, not in a TD row.

## 3.1 Coordinator rulings — Recommendations, Risks, Inconsistencies

> Answered 2026-08-13. Numbering follows the executor's.

**Recommendations — all five accepted; three change the TS.**

| # | Ruling |
|---|--------|
| 1 | **Accepted, and it fixes a real gap.** A10 arrived from a Phase A ONB and A12 was owner-initiated during execution — neither came through Step 6c, and my AC-3 said "`plan.md` — verdict handling" without naming where. A labelled block after Step 6c that applies **whenever a verdict arrives** is correct. Do not renumber: `glossary.md`:178 cites "plan.md Step 6c" twice and :142 cites "review.md Step 4" |
| 2 | **Accepted, and it makes AC-2's replay worth running.** Classify from **target section + rule 6**, never from the incoming table label. Your R26 case proves it: labelled `Refinement`, targets `§4 Phase C` — frozen section, free unit. A step that trusts the label inherits the researcher's error; one that re-derives catches it. AC-2 updated to require this explicitly |
| 3 | **Accepted with your own correction applied.** Your citation 27 is right and my §6 was wrong: `research/base.md` has room against F2 and **no room against D25**, which designs it at ~500 words core and it is already 869. TS §6 corrected. Additions there stay minimal too — "the wordier half" means *relatively*, not *freely* |
| 4 | **Accepted.** Same substitution as Phase A, same disclosure. TD-134 stands |
| 5 | **Accepted, and it matters more than it looks.** Fix the method before measuring: `wc -w` says 1,206, the Phase A REVIEW and TD-140/141 say 1,205, and the delta is frontmatter delimiters. With the target now F2's ≤1,200 the ambiguity is less decisive than it was under my "below 1,206", but quote the command and use one throughout |

**Risks — acknowledged; two change the work.**

| # | Ruling |
|---|--------|
| 1 | **Correct, and report the third table as findings.** iter2's `Coordinator notes — inside approved scope, no amendment needed` is a class `templates/RES.md` does not define — four rows the shipped step must either route or visibly fail to route. Do not fold them into `Refinements` to make the replay look clean. If the class turns out to be real, that is a finding for Phase D's terminology pass, not a silent third table |
| 2 | **Correct, my figures were wrong.** AC-3's evidence said "five freeze commits and twelve §12 rows across three amendment rounds". It is **four** re-freeze rounds plus one non-amendment freeze (`ffe6c6a`), and the initial baseline `8136306` carries scope `task` so the documented form does not return it. TS corrected. Record the divergence as you propose — it is evidence about the mechanism, not noise |
| 3 | **Correct.** `min_iterations` (D38) is stated only in Step 6c and cited from `glossary.md`. Diff the gate semantics explicitly; replace content in place |
| 4 | **Correct, and thank you for pre-empting it.** TD-135's trigger reads "re-measure `conventions.md` §3 at Phase B before appending" — Phase B appends nothing there, so it does not fire. Recording that in the RF prevents the reviewer reading the routing table as an unmet obligation |

**Inconsistencies.**

| # | Ruling |
|---|--------|
| 1 | **Remove it. Authorised, and it is not a budget trim.** `plan.md`:97 cites `conventions.md` §4 "Agent selection guidance", which D50 deleted as tautological. A cross-reference to a heading that does not exist is a correctness defect; removing it is a fix that happens to save ten words. You were right to ask rather than assume — DoF-2 makes that distinction load-bearing. State the reason in the RF so the saving is not counted as compression |
| 2 | No action — Risk 4 reconciles it. The two documents disagree on their face and the routing note is the stale one |
| 3 | **Escalated to the owner as amendment A13.** You are right that only §12 can fix it and right not to touch it. See below |

> **A13 filed 2026-08-13.** HL §4 Phase A's parenthetical still describes the baseline as *"recoverable via `git log --grep`"*, which AC-15 replaced with a subject-only form on `095b8b9`. The frozen text now describes a command the framework no longer ships. Flagged by Phase A RF Decision 14, carried unfixed into Phase B, found again here. It does not block you — AC-3 requires you to name the reserved scope word rather than a command line.

## 4. Recommendations (suggestions, not blocking)

1. **Verdict handling must be reachable from outside the research loop.** HL deliverable 3 and AC-3 say
   "`plan.md` — amendment verdict handling" without naming a step. This task's own history shows why
   that matters: A10 was filed from a Phase A **ONB**, and A12 was owner-initiated during **execution** —
   neither arrived inside Step 6c. I intend to land it as a labelled block after Step 6c that states it
   applies whenever a verdict arrives, and **not** to renumber anything (`glossary.md`:178 cites
   "plan.md Step 6c" twice, `glossary.md`:142 cites "review.md Step 4"). Flagging rather than assuming.
2. **Classify by target section and the granularity rule, not by the researcher's own table label.**
   `research/iter2/RES.md` puts R26 in `Refinements` while its target is `§4 Phase C` — a *frozen*
   section whose deliverable list is a *free* unit under rule 6. A step that trusts the incoming label
   inherits the researcher's classification error; a step that re-derives it from target section + rule 6
   catches it. This is also what makes the replay in AC-2 meaningful rather than tautological.
3. **`research/base.md` gets the wordier half.** TS §6 invites this and the numbers support it: 869 words
   against `plan.md`'s 1,206. The class definitions, the target-section column and the never-edit
   restatement all belong to the researcher's side.
4. **Build gate:** `project_config.yaml` `build.lint/test/verify` are unconfigured placeholders (TD-134).
   I will use Phase A's substitute — `pytest docs/scripts/` + `mkdocs build` — since both workflows are
   Source Manifest entries. Same substitution, same disclosure.
5. **Word-count method must be fixed before, not after.** `wc -w` reports 1,206 for `plan.md`; the Phase A
   REVIEW and TD-140/141 report 1,205. The delta is the YAML frontmatter delimiters. With a target of
   "below 1,206" a one-word tool difference decides the verdict, so I will record both counts with
   **the same** command and quote it, per AC-6's gate.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **AC-2's replay is partly circular.** I write the step and then judge whether it routes 22 rows. The
   corpus is not: iter2's rows were written before Phase A shipped, by a researcher who hand-rolled the
   split, and its third table — `Coordinator notes — inside approved scope, no amendment needed`, 4 rows —
   is a class `templates/RES.md` does not define. Those rows are the real test; I will report them
   as findings rather than quietly folding them into `Refinements`.
2. **AC-3's evidence figures do not match the history.** TS AC-3 says *"five freeze commits and twelve §12
   rows across three amendment rounds"*. The rows are 12 (A1–A12) and the `/freeze/` commits are 5, but the
   re-freezes are **four** rounds (A1–A5 `d9a4c57`, A6–A8 `99d4e20`, A9 `dcb9bf1`, A10+A12 `70f3553`) with a
   fifth non-amendment freeze (`ffe6c6a`, header cleanup) — and the **initial** approval baseline is
   `8136306`, scope word `task`, so the documented recovery form does not return it. Rule 14 says the
   reserved word applies to the first freeze too. I will record this as an AC-3 divergence, not paper over it.
3. **Step 6c is the only place the `min_iterations` hard gate is stated** (D38, cited from `glossary.md`).
   Replacing content in place is safe; a structural rewrite of 6c could drop it. I will diff the gate
   semantics explicitly rather than trusting a re-read.
4. **TD-135's trigger does not fire here.** It says *"re-measure `conventions.md` §3 at Phase B before
   appending"*; Phase B appends nothing to `conventions.md`. Recording it so the reviewer does not read
   the routing table as an unmet obligation.

## 6. Inconsistencies with Code (spec vs reality)

1. **`plan.md`:97 cites a section that no longer exists.** *"For multi-agent research, see conventions.md §4
   (Agent selection guidance)"* — D50 removed that table post-implementation as tautological, and
   `conventions.md` §4 has no such heading. A dead reference inside a file this phase edits, 10 words.
   Not in any AC. I will not remove it without a ruling, because DoF-2 forbids trimming to hit AC-6's
   number and this would otherwise look like exactly that.
2. **TS §2 excludes `conventions.md`, but the Phase A REVIEW routed TD-135 to Phase B** (`REVIEW__phase-a`
   §5). Reconciled by Risk 4 above — no action, but the two documents disagree on their face.
3. **The TS header's `Baseline` field is the corrected subject-only form** (AC-15, `095b8b9`), while the
   frozen HL §4 Phase A parenthetical still reads *"recoverable via `git log --grep`"*. Phase A RF Decision
   14 flagged this deviation for the coordinator and it is still open in the frozen text. Phase B's AC-3
   requires me to name *"the reserved scope word, not a specific command line"*, so I am unaffected — but
   the frozen sentence is now wrong and only §12 can fix it.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | `.tfw/README.md` § Structural Enforcement | ✅ | Applied | The replacement is a numbered gate in the workflow, not advice |
| 2 | `.tfw/README.md` § Naming Creates Behavior | ✅ | Applied | Step 6c says *classify*, `Refinement`, `Amendment Proposal` — Phase A's tokens, unchanged |
| 3 | `.tfw/README.md` § Candor Over Flattery | ✅ | Applied | Escalation carries cost and alternative; Q1 reports an unsatisfiable AC instead of quietly hitting the number |
| 4 | `KNOWLEDGE.md` D19 | ✅ | Applied | AC-4: research still feeds the HL every iteration; only the frozen channel turns to propose |
| 5 | `KNOWLEDGE.md` D20 | ✅ | Applied | AC-1 — approval stops being a status transition and becomes a written field plus a commit |
| 6 | `KNOWLEDGE.md` D23 | ✅ | Applied | Everything added is a numbered step or a table row; no prose block. Drives Q1 |
| 7 | `KNOWLEDGE.md` D24 | ✅ | Applied | Class names and the `PROPOSED` verdict inline at the enforcement site; the *rules* stay referenced (DoF-3) |
| 8 | `KNOWLEDGE.md` D31 | ✅ | Applied | The re-freeze commit is the structural state; no checkbox records the baseline |
| 9 | `KNOWLEDGE.md` D49 | ✅ | Applied | Both verdict paths are gates, not guidance |
| 10 | `KNOWLEDGE.md` D54 | ✅ | N/A here | Adapter copies of `plan.md` are Phase D's (TS §9). I touch none |
| 11 | `knowledge/philosophy.md` F4 | ✅ | Applied | Same as 8 — commit over checkbox |
| 12 | `knowledge/philosophy.md` F13 | ✅ | Applied | AC-5: no platform, shell or vendor. Baseline grep is already 0/0 — this is a preservation criterion, and rule 15 is referenced rather than inlined |
| 13 | `knowledge/philosophy.md` F21 | ✅ | Applied | The step states what to do when a class is empty rather than leaving silence |
| 14 | `knowledge/philosophy.md` F22 | ✅ | N/A | No template section added or changed in this phase |
| 15 | `knowledge/philosophy.md` F25 | ✅ | Applied | Escalation presents evidence/cost/alternative; the owner decides. The coordinator may not rule on its own proposal |
| 16 | `knowledge/process.md` F4 | ✅ | Applied | Numbered steps + gates; the reason the replacement is a list, not a paragraph |
| 17 | `knowledge/process.md` F6 | ✅ | Applied | The recorded, unfixed instance this phase closes at the instruction site |
| 18 | `knowledge/process.md` F14 | ✅ | Applied | Assumed hostile: the step must be routable without goodwill, which is what AC-2's replay tests |
| 19 | `knowledge/process.md` F20 | ✅ | Applied | Q1 and Q2 are HL/TS divergences escalated, not resolved by me |
| 20 | `knowledge/constraint.md` F2 | ✅ | Applied | The whole of Q1. 700–900 working, 1,200 hard; the file enters at 1,206 |
| 21 | `.tfw/conventions.md` §7 | ✅ | N/A | AT/execution modes are TFW-54. DoF-4 of the HL bars touching them here |
| 22 | `.tfw/conventions.md` §15 | ✅ | Applied | AC-4's Role Lock restatement: the researcher proposes, never edits |
| 23 | `KNOWLEDGE.md` D55 | ✅ | Applied | AC-3 names the reserved `freeze` scope word; commit subjects follow `[claude-code/TFW-53/phase-b/executor]` |
| 24 | `knowledge/process.md` F11 | ✅ | Applied | iter2's RES hand-rolled the two classes before Phase A shipped them — formalising an emerged pattern, and the reason its third table is evidence rather than noise |
| 25 | `KNOWLEDGE.md` D43 | ✅ | N/A here | Citation-as-anti-hallucination is Phase C's Purpose Check |
| 26 | `KNOWLEDGE.md` D46 | ✅ | N/A here | Reviewer Identity is Phase C |

**New items the coordinator did not cite, relevant to this phase:**

| # | Source | Item | Why it applies |
|---|--------|------|----------------|
| 27 | `KNOWLEDGE.md` D25 | `research/base.md` = core algorithm ~500 words; mode files = settings | Recommendation 3's ceiling. base.md is already 869 against a ~500 design intent, so "it has room" is true against F2 and false against D25. Additions there stay minimal too |
| 28 | `KNOWLEDGE.md` D38 + `glossary.md`:178 | `min_iterations` hard gate lives in *plan.md Step 6c*, cited by name from the glossary | Turns TS Risk 3 from a caution into a measured constraint: the step number is externally referenced twice |
| 29 | `KNOWLEDGE.md` D50 | Agent selection guidance removed from `conventions.md` §4 | The dead reference at `plan.md`:97 — Inconsistency 1 |
| 30 | `.tfw/conventions.md` §4 (Research subfolder) | *"Coordinator owns this file — researchers read it, coordinator updates it"* | Bounds Recommendation 3: the `iterations.yaml` mechanics in Step 6c may **not** move to `research/base.md`, however tempting for AC-6 |

---

*ONB — TFW-53 / Phase B: Enforcement in Workflows | 2026-08-13*
