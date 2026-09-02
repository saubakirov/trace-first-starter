# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | Ten of eleven acceptance criteria verified against actual files, most of them reproducing **to the word** (verify.md V1–V6, V10–V17, commands 1–13). **AC-10 fails on one bullet — *"`glossary.md` … carry the change"* — and through it HL DoD 5 and DoF 5, both frozen.** `glossary.md:186` still reads *"Triages executor Observations into REVIEW §5 and **disposes of every one** before the task closes"*, and `glossary.md:324` still names `pending — owner` as the only waiting state with no ruler and a pointer to a step that no longer holds the grammar. verify.md D1, D2. Nothing else in DoD 1–14 is unmet: DoD 9's appended/sibling/never-overwritten classification is in `handoff.md`, DoD 10's budget cleared at 480 and 160, DoD 14 is answered with a measured *yes* |
| 2 | Two clauses, both answered. **(a) Purpose Check** · **(b) Design soundness** | ✅ | **(a)** Serves HL §1 Vision at baseline `29be329` — *"One role rules on each kind of output, named before the autonomy is granted"* — and NS1's *"see where authority remains"*; **the concrete harm at stake was a reviewer inventing a private standard per finding and a rung-2 item with no door but REJECT, measured at AFD-48 rev2/rev3/rev4 with no amendment ever logged (verify.md C2), and the shipped mechanism closes it.** Excess/adjacency: none — six mechanisms, six deliverables, zero new artifacts. Deferral confession: none — nothing here names another home for itself. Materiality: the delivered mechanism is the mechanism the baseline asked for; D1 is an incomplete delivery site, not a mis-aimed deliverable, so it belongs to row 1 and row 9 and does not ground a purpose block. **(b)** Sound against HL §7: the axis is quoted and cited (P1), authority is named in the role table rather than only in the workflow (P2), rung 1 costs the majority case nothing (P3), the loop ends on a configured budget (P4), a bare priority is inadmissible (P5), the file is four words shorter (P6), and every mechanism lands on a site that already shipped (P7) |
| 3 | **Debt disposed** — every §5 row, ruled by the coordinator, naming something that exists, with a consequence rather than a priority | ✅ | Six rows — five from the RF's surviving observations, one found by applying Step 6 during this review. **All six carry `pending — coordinator`, which this release's own template declares legal and which keeps the task open.** The reviewer may not rule them (`conventions.md` §15, shipped by this task), so each carries a **proposal** written in the new grammar instead: three `not material — owed and forbidden to pay` with the barring clause cited (HL DoF 8 + the owner's 2026-09-01 ruling; HL §7.1 + TS §2; HL DoF 8 + DoD 10's three words of headroom), one `not material — not owed`, one `promoted` blocked on the identifier grammar, one `paid`. **No bare priority anywhere; every row names a consequence or its named absence.** This is the protocol's first live application and it ran without improvisation, with one exception recorded as row 6 |
| 4 | Style & standards | ✅ | Reference Format held throughout; no `$0`–`$9` or `$ARGUMENTS` in either shipped command surface (verify.md command 9); every file LF after the mid-run CRLF incident (command 11); the identifier and journal grammars respected. `handoff.md` at 1 749 words breaches `conventions.md` §11's ≤1 200 — **instructed growth** under AC-8, out of DoD 10's scope, and recorded by the executor as its own observation rather than left for a reviewer to find |
| 5 | Observations collected | ✅ | Five, and **all five verified real** — the `tfw-task.md` pair genuinely differs and genuinely has no source (`cmp` differs at line 1; `.tfw/workflows/tfw-task.md` and `.agents/skills/tfw-task` do not exist); `resume.md:68` reads as quoted; `handoff.md` measures 1 749 against 1 452; `KNOWLEDGE.md` §2 carries no TLD task row; `init.md`/`plan.md` measure 2 032 and 1 702. Zero filler |
| 6 | RF completeness (§7-9) | ✅ | §7: four Fact Candidates, all sourced to a dated conversation or artifact and all non-obvious — FC2, *"a coordinator's own acceptance criterion can be unpassable as written, and the executor is the first role that can find out"*, is the sharpest and is evidenced by three amendments in this task alone. §8: four Strategic Insights, each with an implication that changes a later work choice. §9: three diagrams, and the third — the before/after table — is the one an owner with aphantasia can read without holding anything in their head |
| 7 | Evidence completeness — does the evidence **exist**? | ✅ | All eleven AC rows present in the EV file with an environment header, per-AC statuses and inline output. Every one of the four `N/A`s is an `N/A` the **TS itself declared**, quoted back at the point of use — not a reviewer's word taken on trust. Three evidence artifacts required by TS §5, three delivered |
| 8 | Evidence sufficiency — does the evidence **establish the claim**? | ❌ | Almost all of it does, and unusually well: the AC-1 gates reproduce **to the word** including the per-step split nobody was required to make checkable; Replay 1 re-rules the **complete** nine-row population rather than a sample; Replay 2's rung split and its rev2/rev3/rev4 recurrence reproduce exactly in a second repository; Replay 4 reports a result **against the executor's own convenience** (TLD's revision count is zero, not one). **One justification does not establish what it is offered to prove.** `word_budget.md` subtraction 8 justifies a 29-word saving on the ground that both removed Anti-patterns are *"word-for-word §14 lines"*, and the same claim ships in `.tfw/CHANGELOG.md` as *"verbatim duplicates … Nothing was lost."* One of the two is verbatim; the other lost `(start /tfw-review instead)`, which is now in neither list. verify.md D3, C4. Separately, the honest-draft figure of 753 leaves no artifact and is accepted as a self-report with that limit stated (C8), and `word_budget.md`'s *"no `$N` in the file"* line runs a grep that is not that check — the real one is in RF §4 and I re-ran it clean |
| 9 | Backward compatibility — does the change break an existing consumer? | ❌ | **Three consumers were left stating the retired rule.** (i) `glossary.md` `Reviewer` — the role definition every workflow loads as context item 3, **before** the workflow — tells a reviewer it disposes of every observation, which `review.md`'s two new Anti-patterns then forbid. (ii) `glossary.md` `Disposition` — names `pending — owner` alone and points at `review.md` Step 5 for a grammar that moved to `templates/REVIEW.md` §5. (iii) `KNOWLEDGE.md:173` — *"written out in `review.md` Step 5 and measured at 243 rows"*, the two facts TS §4 authorisations 1 and 3 ordered corrected, corrected in the CHANGELOG and left here in a row the executor edited in the same act. verify.md D1, D2, D4. Every other consumer was handled correctly, including nine no-ops verified by reading rather than grepping and three localized READMEs read in their own language |
| 10 | Safety | ✅ | No secrets, credentials or destructive operations anywhere in the diff. One external repository was opened and it was opened read-only: `git status --short -- tasks/AFD-48…` returns empty, and the four pre-existing dirty entries in that tree are exactly the four the RF declares in advance. Nothing was run outside this session that is claimed to have been run |

## Purpose Check — row 2 clause (a)

**Reference set:** master HL at contract baseline `29be329` (§1 Vision, §5 DoD and §6 DoF verified byte-identical to the current file), plus `.tfw/README.md` `NS1`.

**Outcome: Aligned (✅).** The clause served is HL §1's *"both become decisions by a stated rule… One role
rules on each kind of output, named before the autonomy is granted"*, under NS1's *"see where authority
remains"*; the concrete harm it exists to prevent is a finding only a coordinator can discharge being
written into a list only the executor reads — measured at AFD-48 rev2, rev3 and rev4, returned three times
with no amendment ever logged (verify.md C2) — and the shipped rung-2 route closes exactly that harm.

- **Excess and adjacency:** no. Six mechanisms against six deliverables; zero new files, templates,
  scripts or checks; one configuration key, which A11 authorised on the record. Nothing here is adjacent
  work smuggled in — and `KNOWLEDGE.md` §3's one extra row is declared in RF Decision 11 for a ruling
  rather than left to be found.
- **Deferral confession:** no. Nothing in the TS or the RF names a different home for this work.
- **Materiality:** the mechanism is what the baseline asked for. D1 is a delivery site missed, not a
  deliverable aimed elsewhere, so it fails row 1 and row 9 and does not ground a purpose block.

**Not the third outcome.** The baseline and the north star are consistent here, and no two baseline
clauses conflict: DoF 1's *"nothing new that must be maintained"* is discharged in its own second half by
A11's single permitted key, and DoD 10's word ceiling is satisfiable with all six mechanisms in — measured
at 480 against 483, not argued.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | §1 *TFW Core* files `.tfw/glossary.md` as part of the tool-agnostic framework spec; `conventions.md:100` calls it **PV priority 0** | RF §1: *"`glossary.md` — Three terms: `Revision`, `Revision budget`, `Rung`"*, offered as AC-10's *carry the change* | **Yes.** A canon file at PV 0 was extended but not reconciled: its `Reviewer` entry still grants the authority DoF 5 forbids anywhere in the canon |
| 2 | §3 Legacy row 173, TLD's registry retirement: *"…written out in `review.md` Step 5 and measured at 243 rows"* | RF Decision 6 (the search moved) and Decision 7 (the count is 253) | **Yes.** The knowledge base states a location and a figure this release retired, in a row edited during this same act |
| 3 | §1 new *Correction Loop* row; §1 D72; §2 task row; §3 retirement row | The four `KNOWLEDGE.md` edits | **No.** All four are accurate against the shipped text, and D72's *"one corpus ran nine revisions across eight TS files with zero terminations"* is consistent with Replay 4's finding |

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Every `⚪ N/A` carries a stated reason — no row skipped as a bare ✅? *(No row is `⚪` — all ten applied)*
- [x] Row 2(a): answered against the contract baseline and the north star — never the TS or a Phase HL — with a quoted clause **and** a named harm in one field?
- [x] Rows 7 and 8 answered separately, with different reasoning? *(7 = the artifacts exist and their N/As are the TS's own; 8 = one justification does not establish its claim → ❌)*
- [x] Referenced verify.md findings in DoD assessment?
- [x] Row 3: every §5 row disposed by the coordinator, each disposition naming something that exists today, and each ruling naming a consequence or its absence rather than a priority? *(All five are `pending — coordinator` — legal, keeps the task open — each carrying a proposal in the new grammar)*
- [x] Checked RF §7-9 for presence AND quality (not just existence)?
- [x] KNOWLEDGE.md cross-referenced — contradictions documented?
- [x] Fact Candidates from RF reviewed — any that need challenge? *(FC1–FC4 all hold; FC2 is corroborated by three amendments in this task's own §12. None challenged)*

Stage complete: YES
