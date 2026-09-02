# Judge — "Is the quality sufficient?" · round 2

> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md) · Map: [map.md](map.md)
> Contract baseline: **`1c7b55e`** — HL verified byte-identical to it (verify.md command 17)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | **The round's own four criteria hold under 100% verification.** AC-13 (V6, V10, E12) · AC-14 (V9, V11, V12, and the sixth step closed by this file) · AC-15 (V6) · AC-16 (commands 1–4, 12, 13) · item 7 (V7, V13–V14) · items 1–5 (V1, V2, V4, V5, C4). **What fails is revision 1's AC-11, bullet 1** — *"The build passes: `python -m pytest .tfw/scripts/ docs/scripts/ -q`"* — which TS rev2 §3 keeps in force as verified. Independently re-run: **1 failed, 321 passed, 1 skipped** (command 8), the failure reproduced offender-for-offender (command 9). One criterion of the approved TS, breached |
| 2 | **(a) Purpose Check** · **(b) design soundness** | ✅ | **(a)** See the filled field below — ✅ Aligned. **(b) Sound against all seven HL §7 principles**, and two carry weight here. **Principle 6** (*subtraction is the proof*): the mechanism that ends the loop arrived while `review.md` Steps 4–6 went **483 → 480 → 477** and the whole file **1 706 → 1 699**, with the withdrawal (88 words) funding the addition (82) — measured, not asserted. **Principle 7** (*a rule with no enforcement site is decoration*): the citation bar's site is the basis cell in the round's order, and TS rev2 §5a has **nine items and nine filled cells**; `plan.md` Step 8 states *"An empty basis cell means the item does not belong there"*. Round 1's design defect — the coordinator writing into the reviewer's artifact — is removed rather than patched, and the four patches it needed (a detector, a status field, a chat explanation, an invisible round) are all withdrawn. **Zero new entities**, and the one key round 1 spent is given back |
| 3 | **Debt disposed** | ✅ | Eleven rows in §5, **all `pending — coordinator`** — legal, and each keeps the task open (`glossary.md` `Disposition`, shipped by this task). The reviewer may not rule them (`conventions.md` §15), so each carries a proposal in the shipped grammar: **four `paid — this task's phase`** naming this task's own phase, which exists; **three `not material — not owed`** each naming the absence rather than a priority; **four `not material — owed and forbidden to pay`** each citing the barring clause (HL DoF 8 ×2, HL §7.1 + TS rev2 §2, HL DoD 10). **No bare priority anywhere**, and no `→ backlog` |
| 4 | Style & standards | ✅ | Every file LF (command 15); no `$0`–`$9` or `$ARGUMENTS` in `review.md` or `templates/REVIEW.md` (command 14); adapter parity 33/33 by `cmp` (command 12); the revision filename grammar the round *defines* is obeyed by the round's own artifacts (`TS__…__rev2.md` a sibling, revision 1 untouched since 15:59, RF and ONB appended); four journal events on the closed `kind` vocabulary, each carrying `on_behalf_of` and `via`, each timestamp bracketing the work it records. **One ambiguity met and resolved rather than guessed:** `conventions.md` §5's rung table sets `TS_DRAFT` *"only when the TS is actually changed"* while §15's Reviewer entry tells this role to set it at the verdict. §15 is the entry addressed to the reviewer and it is unambiguous, so it governs; recorded here rather than escalated, because no role is left guessing |
| 5 | Observations collected | ✅ | Six in RF §6.2, **all six independently verified real** — O1 at `handoff.md:103` (read), O2 reproduced by re-implementing the detector, O3 at `templates/REVIEW.md:48` (read), O4 by counting the §4 table's four rows against five round artifacts, O5 at `update.md:122–131` (read), O6 by `git log -- ` on the orphaned paths and the commit graph. **Zero filler.** Each carries a rung and a blast-radius statement; two are reported against the executor's own convenience |
| 6 | RF completeness (§7–§9) | ✅ | §7.2 five Fact Candidates (F5–F9), §8.2 five Strategic Insights, §9.2 four diagrams. **Quality, not just presence:** F9 records a measured operating rule for a shared working tree (`git commit --only` with explicit paths, never `git add -A`) that this review independently confirmed matters; S1 names the generalisable finding — *the defect was a missing artifact, not a missing rule*; and §9.2's before/after and scorecard blocks are readable without holding anything in the head, which is this owner's stated requirement |
| 7 | Evidence completeness — does it **exist**? | ✅ | Seven rows E12–E18 in the EV file's *Evidence — round 2*, every one covering an item of the order, with raw output in `evidence/round2.md` and an environment delta naming the shared working tree and its commit discipline. **0 DEFERRED, 0 BLOCKED, 0 N/A** — nothing declared inapplicable and nothing silently dropped |
| 8 | Evidence sufficiency — does it **establish the claim**? | ✅ | **Every figure re-measured from a primary source and every one reproduced**: the count 14/12 → 0/0 at both revisions; 477/160/1 699/1 730/1 847/1 673/668 all to the word; the twelve offenders enumerated rather than counted, so nothing hides behind the number; 33/33 `cmp`. Two rows report against the executor (command 5, check C5). **One presentational note, not a green-on-red:** E18's status reads *"VERIFIED as a measured failure"* and its first sentence states the failure — the status describes the evidence, not the criterion — but the row's summary line *"7/7 VERIFIED"* would not, alone, tell a reader that one of the seven documents a broken gate |
| 9 | Backward compatibility | ❌ | **Two consumers of the changed grammar are left inconsistent with it.** (1) `docs/scripts/test_integration.py:938` — `DOUBLED_SLUG = re.compile(r"\{ID\}__")` encodes *nothing may follow `{ID}`*, an absolute A14 relaxed for exactly one suffix; the repository's own build gate is red and the canon is the side that is right. (2) `.tfw/templates/REVIEW.md:48` still heads the reviewer's own section `### If REVISE — items to fix:` — an **order** in the file that must now carry **proposals**, which is the precise site that produced round 1's measured defect. Blast radius correctly bounded by the RF: neither reaches a receiving project, because `update.md` Step 5's payload is `.tfw/` — but (2) *is* in `.tfw/` and does ship. **Not left inconsistent, and checked:** `conventions.md` §14, `glossary.md` `Revision`, both `project_config.yaml` files, all six adapter copies and `KNOWLEDGE.md`'s four sites |
| 10 | Safety | ✅ | No secrets, no credentials, no destructive or irreversible operation. No external tree was touched this round. `git status` shows only a neighbouring session's `.gitignore` edit and one untracked link directory, **neither this task's** (command 16) — which is the direct repair of round 1's observation 6: this round's verdict rests on commits, not on a working tree |

## Purpose Check — row 2 clause (a)

**Outcome: ✅ Aligned.**

**The clause served, and the harm at stake, in one field.** HL §1 at baseline `1c7b55e` commits that
*"the loop ends in a decision rather than in exhaustion: a round is available exactly when the reviewer
can name the condition the work breaches"*, and NS1 requires that *"another authorized person or agent
can … see where authority remains, and continue without rebuilding the original conversation."* Round 1
shipped the opposite of the first — a counter whose exhaustion ended the loop, contradicting this
contract's own principle 4 in those words — and it left the second unserved, because the coordinator's
round order lived in the reviewer's file, so the concrete harm was measured on this very task: the owner
could not see from the directory that a round was open (*«раньше я видел эти rev1 rev2 и т.д., теперь не
вижу»*), the executor was to be given a detector to find an order that was misfiled, `status.md` asserted
`RF` while items were owed, and the rest stayed in chat, which does not persist. Round 2 removes both
harms at their source: the count is gone from all twelve tracked files that carried it, and the round is a
`rev{N}` sibling TS in the coordinator's own artifact — the file Role Lock already obliges the executor to
read — so continuation now needs neither the conversation nor a detector.

**The three tests, each answered *no*:**

1. **Excess and adjacency — no.** Nothing is delivered that the clause does not ask for: **zero** files,
   templates, scripts, checks or configuration keys created, the one key round 1 spent returned, and the
   task's net entity count back at zero, so NS3's *"maximum-documentation bureaucracy … that measures
   success by artifact count"* is not approached. No DoF item fires: `.tfw/scripts/` untouched, no new
   status value, no rename, one live revision, and both word ceilings met by subtraction. The two edits
   outside the order's own tables (`conventions.md` §14, `KNOWLEDGE.md` §2's own row) are authorised by
   TS rev2 §4's *"Revision 1's file list stands"* and by HL §7.1's bar on false corpus claims respectively,
   and both were declared before this review opened.
2. **Deferral confession — no.** The RF names four things it did not do and routes each rather than
   shipping past it: the red test as rung 2 with the one-line fix named, `handoff.md` step 7 as rung 2
   rather than an unauthorised edit, the template heading as out of scope by TS rev2 §2, and `update.md`'s
   rule as out of scope by DoF 8. None of them says *this belongs somewhere else* and ships here anyway;
   each says *this belongs to the coordinator* and stops, which is the route the protocol defines.
3. **Materiality — the harms named are impact on the value, not wording.** A withdrawn counter that had
   fired on the legitimate case within hours; an order nobody could find in a directory listing. Both were
   observed on this task, by its owner, before the amendments were filed.

**Why the two `❌` rows do not make this a purpose failure.** Rows 1 and 9 rest on the same fact — one
stale check and one stale template heading — and both are *repairs to what was shipped*, inside the
approved contract, with a named basis and a one-line fix each. That is a work defect routed by rung, which
is what 🔄 REVISE exists for. *"The TS scoped it this way"* and *"tests are green"* are named in this row
as insufficient grounds to approve; the inverse is equally true — a red check is not evidence that the work
serves the wrong purpose. **The reference set is internally consistent:** HL §1, §4, §5, §6 and §7 at
`1c7b55e` and NS1–NS3 can all be satisfied at once, and A13's own record is the proof — the one place two
clauses did conflict (a counter versus principle 4) was resolved by amendment before this round began.
**No contract defect.**

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | `Correction Loop` (§1, line 23) — *"There is no revision count and no configuration key"* | AC-16: the count withdrawn from all twelve files; both configs re-parse without the key | **No** — the knowledge row and the canon were rewritten in the same act and agree |
| 2 | **D72** (§1, line 166) — *"the loop ends in a decision rather than in exhaustion"*, and it now carries its own reversal | RF §2.2 decision 1 and §8.2 insight 4 | **No.** Round 1 shipped a mechanism that contradicted this record's own headline; D72 now states that, names the four grounds, and says the mechanism was withdrawn before release. **A fact that carries its reversal, which is what makes it worth keeping** |
| 3 | **D71** (§1) — a defect only one platform can produce is invisible to CI on the other | RF §2 decision 10 (round 1): eight files silently converted to CRLF by `pathlib.write_text` on Windows | **No** — and this round's CRLF sweep is clean (command 15), so the lesson held |
| 4 | §2 Key Artifacts, this task's row (line 161) | *"zero new artifacts and zero configuration keys"*, *"Round 1's configured budget was built, measured and **withdrawn** in round 2"* | **No** — the row was corrected in this round precisely because it asserted one key. Verified against the diff |
| 5 | §3 Legacy & Deprecation (line 175) — *"🔄 REVISE carrying one destination … Replaced"* | `conventions.md` §5 now routes per rung and gives REVISE two lifecycle states | **No** — the retirement row and the replacement text agree |
| 6 | `Debt` / `Disposition` knowledge — three outcomes, no fourth, a disposition names something existing | §5's eleven rows: four `paid` naming this task's phase, seven `not material` with the question named | **No** |

## Checkpoint

**Self-check:**
- [x] Every checklist item carries evidence, not a bare symbol — each row names the verify.md finding or the command number behind it
- [x] No `⚪ N/A` used; no row skipped as a bare ✅
- [x] Row 2(a) answered against the **contract baseline `1c7b55e` and the north star** — never the TS, never a Phase HL — with a quoted clause **and** a named harm in one field, plus all three tests answered
- [x] Rows 7 and 8 answered separately and with different reasoning: 7 counts what exists, 8 re-measured every load-bearing figure from a primary source
- [x] DoD assessment references verify.md findings rather than re-deriving them
- [x] Row 3: every §5 row disposed *as a proposal only* — the coordinator rules (`conventions.md` §15) — each disposition naming something that exists today, each ruling naming a consequence or its named absence
- [x] RF §7–§9 checked for presence **and** quality
- [x] KNOWLEDGE.md cross-referenced — six items, no contradiction
- [x] RF Fact Candidates reviewed — F5–F9 all sourced to the owner or to a measurement made this session; **F9 challenged and confirmed** by reading the commit graph, which shows a neighbouring session's `git add` moving a third session's files and `1de76bc`'s own message recording two deletions swept into `7bfc5b1`

Stage complete: **YES**
