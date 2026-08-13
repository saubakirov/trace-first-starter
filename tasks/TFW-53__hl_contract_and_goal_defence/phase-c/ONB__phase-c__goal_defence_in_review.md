# ONB — TFW-53 / Phase C: Goal Defence in Review

> **Date**: 2026-08-13
> **Author**: Executor (Claude Code)
> **Status**: 🟠 ONB — **answered 2026-08-13**, cleared to execute. Q1 → (a) · Q2 → (a) + owner ruling on this project's north star · Q3 → (a). TS amended: `review.md`:85 added to §4, AC-1 and AC-11 reworded, AC-2 gains the deferral confession, AC-6/AC-7 gain the two-file case, **AC-12 added** for DoD-23
> **Parent HL**: [HL-TFW-53](../HL-TFW-53__hl_contract_and_goal_defence.md) — 🔒 FROZEN, re-frozen after A1–A14, baseline `e8ee76e`
> **TS**: [TS Phase C](TS__phase-c__goal_defence_in_review.md) — approved by the owner 2026-08-13
> **Predecessors read**: [RF Phase B](../phase-b/RF__phase-b__enforcement_in_workflows.md), [REVIEW Phase B](../phase-b/REVIEW__phase-b__enforcement_in_workflows.md) ✅ APPROVE, [RF TFW-56](../../TFW-56__review_mode_removal/RF__TFW-56__review_mode_removal.md), [RES iter2](../research/iter2/RES.md)

---

## 1. Understanding

Phases A and B stopped the goals from moving. This phase catches the case where the goals held and the
work went elsewhere anyway. The Judge's **mapping-integrity** check — structurally unable to detect a
principle violated by the mapping itself — is replaced by a **Purpose Check** whose reference set is the
committed contract baseline plus a Project North Star, never the TS and never a Phase HL. The check
cannot be satisfied by assertion: one fused field carrying a quoted clause *and* a named material harm,
an excess-and-adjacency test, an override clause that rules out *"the TS scoped it this way"* and
*"tests are green"*, and a third outcome when the reference set contradicts itself. Around it: PV Index
gains priority 0, `conventions.md` defines the north star with admission criteria, `templates/HL.md`
reaches the anchor structurally, the citation namespace stops colliding, and the whole thing is replayed
against the six TFW-48/49 phase REVIEWs and three sound ones so the check is shown to discriminate
rather than to fire on everything.

Nine of the eleven ACs are textual. The two that carry risk are AC-5 (`review.md` word budget) and
AC-11 (the replay, which can return a finding against the check itself).

## 2. Entry Points

| File | Where | What is there today |
|------|-------|--------------------|
| `.tfw/templates/review/judge.md` | line 16 | Row 2, two clauses: **(a) Mapping integrity** · **(b) Design soundness** _(4.5%)_. 10 rows total, rows 8–10 carry measured rates inside the row (TFW-56 grammar). 639 words |
| `.tfw/workflows/review.md` | line 28 | *"**Master HL** for the task — understand vision, design philosophy, architecture decisions"* — no revision named |
| `.tfw/workflows/review.md` | line 35 | Reviewer Identity: *"Quality guardian. Your job is to protect the project from unverified claims and incomplete work."* Two quality failure modes, no purpose |
| `.tfw/workflows/review.md` | line 85 | **Step 3's `HL §7 Principles check` paragraph — the mapping-integrity check, stated as a workflow instruction.** Not listed in TS §4 → **Q1** |
| `.tfw/workflows/review.md` | lines 89–98 | Step 4 Decide — verdict set `APPROVE / REVISE / REJECT`, no routing rule for a goal failure |
| `.tfw/workflows/review.md` | whole file | **1,065 words** (`wc -w`). F2: ≤1,200 hard, 700–900 working |
| `.tfw/templates/REVIEW.md` | line 32, §4 | §3 row 2 label *"Philosophy aligned — mapping integrity + design soundness"*; §4 Verdict has no purpose finding |
| `.tfw/glossary.md` | lines 221–237 | PV Index priorities 1–7, priority 1 = *"README Values"*; **"Who scans PV"** block directly below |
| `.tfw/conventions.md` | §3, §14 | §3 = artifact types + HL Contract rules 1–21 (Phase A's); §14 = anti-pattern list, last entry is TFW-56's checklist-row rule |
| `.tfw/templates/HL.md` | lines 3–16 | Header block; the contract block ends with *"Add further header fields below this block, not inside it"* |
| `.tfw/compilable_contract.md` | line 59 | `P{N}` → *"KNOWLEDGE.md §0 Philosophy row"* — §0 was removed by D37. Line 65 carries a **second** stale §0 reference → §6.5 |
| Replay corpus | `git show 721ca15:<path>` | 6 phase REVIEWs (TFW-48 a/b/c, TFW-49 a/b/c) + `review/judge.md` per phase, all present. Approved TFW-49 HL at `9e19a4f` present |
| Sound corpus | working tree | `REVIEW TFW-50`, `REVIEW TFW-42/A`, `REVIEW TFW-47/B` — all three present |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | **`review.md`:85 still instructs the mapping-integrity check, and it is not in TS §4.** The paragraph reads *"For each mapped principle: verify the linked AC was met in RF §3. If a principle was mapped to an AC but that AC failed — flag as a principle violation."* AC-1 deletes that check from `judge.md`; nothing in the TS touches this paragraph, so as specified the phase ships a workflow that instructs the check its own template no longer contains. This is the third appearance in this task of the surviving-channel defect (`templates/RES.md`:32 → :133 were the first two). **(a) Replace it with the Purpose Check instruction + reference set** — ~45 words out, ~45 in, so AC-5 pays nothing; **(b) delete it** — −45 words of AC-5 headroom, but the *"mapped to a failed AC = principle violation"* rule loses its only statement; **(c) leave it, report in RF §6** — costs nothing now, ships a live contradiction and exposes HL DoF-11 (*"the goal check … reverts to mapping integrity"*). **My recommendation: (a).** | **(a) — replace.** Your reading is right and the cost analysis is right. Two additions: (i) the mapping-integrity rule is not "losing its only statement", it is being **retired on purpose** — DoD-20 says the check *is replaced*, and DoF-11 names *"reverts to mapping integrity"* as a failure condition of this phase. Option (c) does not merely ship a contradiction, it ships DoF-11. (ii) `review.md`:85 is now **in TS §4 with its limit** — *"the `HL §7 Principles check` paragraph in Step 3, and nothing else in that step"*. Recorded before you touch it, same discipline as `templates/RES.md`:133 in Phase B. An unrecorded scope extension is still a scope extension, and I am the one who has to write it down |
| 2 | **Q9 — is the nominated-HL north-star locus supported, excluded, or left silent?** HL §8 records Q9 as *"decide at Phase C TS"*; the TS restates both branches (*"supported **only as nominated-and-frozen**, or excluded explicitly"*) without choosing, so the decision is still open and AC-6 cannot be closed without it. **(a) Exclude explicitly** — one sentence in `conventions.md`: the locus is a designated section of the root `README.md`, and a task HL may not be nominated. Cost: AFD's live practice (`HL-AFD-2`) becomes non-conformant and would have to move its 45 load-bearing lines into its README. **(b) Support as nominated-and-frozen** — requires a project-level freeze mechanism this task has not scoped (HL §9 says so in as many words); shipping the permission without the mechanism is a rule with no enforcement site (F4, HL DoF-1). **(c) Say nothing** — silence reads as permission and reproduces the measured drift (AFD's anchor grew 10 → 14 principles after approval, six unlogged markers). **My recommendation: (a)** — it is the only branch whose mechanism exists on the day it ships. | **(a) — exclude explicitly.** Owner ruling 2026-08-13, and the practice now agrees with the rule: **this project's north star is its philosophy, and it lives in the root `README.md` and the founder essay `.tfw/README.md`.** A README locus, never a task HL. Three consequences you must build for, all recorded as HL §11 S38. **(i) The anchor is a list, not a path** — AC-7's header field takes more than one location, with explicit N/A when a project has none. **(ii) Priority 0 and priority 1 may point at the same file, and the rule must permit it.** DoD-18 relabels priority 1 because `.tfw/README.md § Values and Principles` is byte-identical across projects and cannot carry project information — true everywhere except here, where the methodology *is* the product. One clause in `conventions.md`: the two priorities are distinguished by *what the section says*, not by which file holds it; a project whose product is its method may designate sections of the same file to both. Without that clause this repository can never conform to a rule it wrote. **(iii) Do not write the designation into either README.** A TFW-55 session is restructuring both files right now (§5 risk 5) — a section-level pointer landed today is the stale-pointer defect this task keeps finding (S32, TD-163). Phase C ships the slot and the grammar; the owner's designation is recorded in HL §11 S38 and lands as a header field when the next HL here is written |
| 3 | **Does the `deferral confession` test ship in this phase?** Frozen §4 Phase C lists it in the Phase C vocabulary and frozen DoD-30 makes Phase D write its glossary article — but **no DoD item and no AC puts it anywhere in `judge.md`**, and TS §2 lists only three tests. Research defined it (D16/E7): *the spec or the result says the right home for this is elsewhere, and ships it here anyway.* **(a) Ship it** as a third test below the table — ~20 words in a template, no `review.md` cost, and Phase D's article then has a referent; **(b) do not ship it** — Phase D defines a term that appears nowhere in the framework, which is the S32 defect (a label with nothing behind it) one layer up. **My recommendation: (a)**, and if it is (b) I will say so in the RF rather than let Phase D discover it. | **(a) — ship it.** Not a scope extension: frozen DoD-30 obliges Phase D to define the term, and a glossary article whose referent exists nowhere in the framework is S32's defect one layer up — a label that resolves and means nothing. Rule 6's tripwire clears, because shipping it is what makes DoD-30 non-vacuous under §5 as it stands. **AC-2 now carries it as a fourth test**, worded as research defined it: *the spec or the result names a different home for this work and it ships here anyway.* Keep it to one sentence below the table — TS §8's *"row 2 grows into a paragraph"* risk applies to the block too |

## 4. Recommendations (suggestions, not blocking)

1. **Do not name AFD inside the shipped template.** AC-1 asks the row to carry *"roughly 4 goal-based
   blocks in 149 AFD reviews"*. `judge.md` ships to every TFW project, and its established grammar for
   provenance is a bare corpus reference (*"measured non-✅ rates from a 637-row corpus"*, rows 8–10 carry
   only the number). **Default I will apply unless told otherwise:** the rate and the
   consequence-not-frequency reason ship in full; the project's name does not. Recorded as a deviation
   in the RF either way.
2. **Put the three tests and the override clause below the table, not in the row.** TS §4 already says
   this; naming it here because TS §8 lists *"row 2 grows into a paragraph"* as a risk and the row has
   to stay two quotable sentences to keep AC-1's clause-(b) property true.
3. **Reconcile, do not compute, the base rate in AC-11.** Nine reviews cannot produce a rate. What the
   replay can establish is *discrimination* — fires on the rejected corpus, silent on the sound one —
   plus consistency with the ~4-in-149 figure. I will state that boundary in the replay file rather than
   present 9 reviews as a measurement.
4. **TD-155 stays open and this is the phase that was told to close it.** Its action reads *"→ next
   phase that may edit `conventions.md` §3 (not B — out of scope)"* — Phase C does edit §3. But the fix
   is a rewording of Phase A's rules 13–15, and both HL §7.1 and TS §9 forbid rewriting another phase's
   entries. Reporting it so the reviewer does not read the omission as an oversight.
5. **`review.md` will be reported at ~1,155 words, not resolved into 700–900.** Same posture Phase B
   took at 1,195 and the reviewer accepted, and AC-5 bullet 3 instructs it explicitly.

> **Coordinator response to §4 and §6, 2026-08-13.**
>
> **R1 — no project name in a shipped template: agreed, and AC-1 is corrected to say so.** It asked for *"4 goal-based blocks in 149 AFD reviews"*; `judge.md` ships to every TFW project and its own grammar is a bare corpus figure. F13. The rate and the consequence-not-frequency reason ship; the provenance stays in this task's trace, where a reader who wants it can find it.
>
> **R2 — tests and override clause below the table: confirmed**, it is what TS §4 specifies and what keeps AC-1's clause-(b) property true.
>
> **R3 — reconcile, do not compute: agreed, and this is the better science.** Nine reviews cannot produce a rate. AC-11's word *"reconciled"* means exactly what you propose — state the boundary, show discrimination, do not dress nine samples as a measurement. AC-11 is reworded to say `discrimination, not rate`.
>
> **R4 — TD-155 stays open: correct.** Both §7.1 and TS §9 forbid rewriting Phase A's rules 13–15, and that prohibition outranks a debt row's routing note. The note was written before the section-ownership rule existed. Report it; I will re-route it to Phase D.
>
> **R5 — report ~1,155, do not resolve: confirmed.** AC-5 bullet 3 instructs it and the Phase B precedent stands.
>
> **§6.1 — DoD-23 had no acceptance criterion. That is my gap, not yours, and it is now AC-12.** You were right to flag it rather than implement it silently: an executor implementing a frozen DoD item with no AC is indistinguishable, from the outside, from an executor exceeding scope. AC-12 gives it a gate so the RF has something to close against.
>
> **§6.3 — `compilable_contract.md`:65 stays out of scope, deliberately.** AC-9's *"one table, nothing else"* exists because that file is the reference registry for the whole framework and a namespace pass is not licence to edit prose in it. Report the second stale §0 reference in RF §6; it goes to Phase D with TD-155.
>
> **§6.4 — the duplicate deliverable number is fixed.** Phase C had two items numbered 4; renumbered to 5–8 in the HL, marked as a rule 7 non-substantive correction. Your deliverable accounting can now read against a clean list.
>
> **§5 risks — all seven accepted as written.** Two get instructions. **Risk 2:** record post-drift replays per review, never averaged; the divergence from AC-11's *"the approved HL"* is real and is the harder test, so state it as a divergence rather than a footnote. **Risk 5:** if `README.md` is still held by the other session, leave the board row uncommitted and say so in the RF — I will land it. Do not stage a hunk you did not write.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **The replay can return a finding against the check itself.** AC-11 forbids tuning the corpus if the
   check fires on a sound review — it must be reported and execution stopped. Concretely likely on
   `REVIEW TFW-42/A`: it is the one sound-corpus review the research iteration did **not** use (research
   ran TFW-46/A, TFW-47/B, TFW-50), so it is genuinely untested. That independence is worth having, and
   it is also where a false positive would appear first.
2. **TFW-48's reference set is not recoverable at its frozen baseline.** Its pre-amendment HL was never
   committed — that is the documented TFW-48 failure and the reason DoD-5 exists. So three of the six
   rejected-corpus replays must run against the HL as it stood at `721ca15`, i.e. *post-drift*. That is
   a strictly harder test for the check (it has to fire using master DoF-12 and P7 while reading the
   drifted contract), not an easier one, but it is a divergence from AC-11's *"the approved HL"* wording
   and will be recorded per review rather than averaged away.
3. **AC-11 may land on the third outcome rather than on a fire.** TFW-49's approved contract is
   internally contradictory (§1 *"readable without special tooling"* vs DoD-3's *"versioned structural
   validator"*). A reviewer running the shipped check on 49/A can legitimately return *reference set
   inconsistent → owner*. That satisfies "non-approve" but not "fires"; the replay will report which of
   the two it is per row instead of collapsing them.
4. **Two of three adapter surfaces will instruct the old review flow from the moment this phase lands.**
   `.claude/commands/tfw-review.md` and `.agent/workflows/tfw-review.md` are out of scope (Phase D owns
   the sync, TS §2). TD-157 already records this window for `tfw-plan`; after this phase it is open for
   `tfw-review` too, and the D54 parity promise is live-broken until Phase D runs.
5. **A concurrent session holds `README.md`.** A TFW-55 session has an uncommitted Task Board row change
   at line 302 right now. Phase B's `fbdf443` swept a sibling task's work into this task's commit for
   exactly this reason (TD-144). I will stage by explicit path, and for `README.md` stage only my own
   hunk after checking the diff — or leave the board row uncommitted and say so in the RF.
6. **The third outcome costs `review.md` words that the TS ledger did not price.** TS §6 budgets +90 for
   line 28, the invalid-reference statement, the identity clause and the verdict routing. DoD-23's
   contract-defect routing is a fourth routing branch. Mitigation: the mechanism lands in `judge.md`
   (a template, off the budget) and `review.md` gets one clause inside the routing block it already
   gains.
7. **The check's own first firing could be a wording objection.** AFD's was, and it was demoted after
   owner challenge. The materiality bar ships in the same pass (AC-2, P14) — the risk is not that it is
   missing but that it is stated as advice instead of as a failing condition. It will be worded as the
   latter.

## 6. Inconsistencies with Code (spec vs reality)

1. **Frozen DoD-23 has no acceptance criterion.** The third outcome (*reference set internally
   inconsistent → owner as a contract defect*) is a frozen DoD item added by approved amendment A6. It
   appears in TS §2 In Scope and TS §4's description of `judge.md`, but no AC and no gate names it, and
   TS §7 does not list its absence as a failure. I will implement it — it is inside the declared scope,
   so this is an AC-coverage gap, not a scope extension — and record it in the RF. Flagging it because a
   reviewer checking DoD 18–29 against the AC set will find the same hole.
2. **`review.md`:85** — see Q1. Spec says the mapping-integrity check is replaced; the workflow still
   instructs it.
3. **`compilable_contract.md` line 59 is the defect AC-9 names; line 65 is a second one it forbids me to
   touch.** `Where references appear` opens with *"`KNOWLEDGE.md` §0 Source column"* — the same section
   D37 removed. AC-9 says *"One table, nothing else in that file"*, so the stale prose reference survives
   the pass that corrects the table. Reported, not fixed.
4. **HL §4 Phase C has two deliverables numbered 4** (the Reviewer Identity amendment and the verdict
   semantics, HL lines 518–519). Non-substantive under rule 7 and inside a frozen section I have no
   channel to; recorded so the RF's deliverable accounting reads against a known defect rather than
   looking like a miscount.
5. **`glossary.md`:213 places the Knowledge Gate in *"Phase 0 of `plan.md`"*** and `plan.md` has Steps
   0–7 with no Phase 0. Already TD-163, already assigned to Phase D. Not touched here; noted because
   Phase C does edit `glossary.md` and the reviewer will see the file in the diff.
6. **`process.md` F19's first half is already historical** — it describes `review.md`'s non-standard
   Step 0, deleted by TFW-56. The fact carries its own correction dated 2026-08-13, so nothing is
   required; confirming I read it against the shipped file rather than trusting it.

## 7. Knowledge Citations

> HL §7.2 carries 26 items. Every one was opened and checked against the shipped file, not accepted from
> the table. Six new items are added below.

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | `.tfw/README.md` § Structural Enforcement | ✅ | Applied | The check lives in `judge.md`, the template filled every review — not in `review.md` prose. Heading confirmed at line 100 |
| 2 | `.tfw/README.md` § Naming Creates Behavior | ✅ | Applied | `Purpose Check`, `not fit for purpose`, `Project North Star`, `NS{n}` ship as the named vocabulary. Heading at line 104 |
| 3 | `.tfw/README.md` § Candor Over Flattery | ✅ | Applied | Q1–Q3 are the uncomfortable questions; each carries a cost and a refusal consequence. Heading at line 88 |
| 4 | `KNOWLEDGE.md` §1 D19 | ✅ | N/A here | Research→HL channel; discharged in Phases A/B. No review-side surface |
| 5 | `KNOWLEDGE.md` §1 D20 | ✅ | Applied indirectly | Implicit approval is why the reference set must name the *frozen baseline* rather than "the HL" |
| 6 | `KNOWLEDGE.md` §1 D23 | ✅ | Applied | Workflow compression — AC-5's ledger; `review.md` additions are clauses inside existing blocks, not new prose sections |
| 7 | `KNOWLEDGE.md` §1 D24 | ✅ | Applied | Pattern A: the reference set, the tests and the override clause are inline in `judge.md`; only `conventions.md` rule 15 is referenced, and AC-3 requires exactly that |
| 8 | `KNOWLEDGE.md` §1 D31 | ✅ | N/A here | Filesystem state; the north star is a README section, not a marker file |
| 9 | `KNOWLEDGE.md` §1 D49 | ✅ | Applied | Gates > guidelines — the fused field is a failing condition, not advice |
| 10 | `KNOWLEDGE.md` §1 D54 | ✅ | Partially N/A | Adapter parity is Phase D; §5 risk 4 records the window this phase opens |
| 11 | `knowledge/philosophy.md` F4 | ✅ | Applied | Structural over exhortation — the reason AC-4 says the identity text must not be load-bearing |
| 12 | `knowledge/philosophy.md` F13 | ✅ | Applied | Domain-agnostic — drives Recommendation 1 (no project name in a shipped template) and the wording of the harm clause |
| 13 | `knowledge/philosophy.md` F21 | ✅ | Applied | Explicit N/A — AC-7's header field must render for a project with no north star |
| 14 | `knowledge/philosophy.md` F22 | ✅ | Applied | Template minimalism — no new REVIEW section (AC-8), no row 11 (AC-1) |
| 15 | `knowledge/philosophy.md` F25 | ✅ | Applied | Framework proposes, human decides — Q1–Q3 present options with costs, not decisions |
| 16 | `knowledge/process.md` F4 | ✅ | Applied | Numbered steps + gates; the `review.md` routing addition is a labelled branch, not a paragraph |
| 17 | `knowledge/process.md` F6 | ✅ | Applied | The recorded, unfixed instance — the reason the Purpose Check exists at all |
| 18 | `knowledge/process.md` F14 | ✅ | Applied | Agents route around non-structural rules; hence the check in the template, not in identity text |
| 19 | `knowledge/process.md` F20 | ✅ | Applied | HL authoritative on WHAT; the executor reports the DoD-23 gap (§6.1) rather than resolving it silently |
| 20 | `knowledge/constraint.md` F2 | ✅ | Applied | ≤1,200 / 700–900 — AC-5, measured before and after |
| 21 | `.tfw/conventions.md` §7 | ✅ | N/A here | Execution modes; AT is TFW-54 |
| 22 | `.tfw/conventions.md` §15 | ✅ | Applied | Role Lock — I write ONB, RF, evidence and the framework files in TS §4. No HL, no TS, no REVIEW |
| 23 | `KNOWLEDGE.md` §1 D55 | ✅ | Applied | Commit subjects `[claude-code/TFW-53/phase-c/executor]`; local commits only, push on explicit approval |
| 24 | `knowledge/process.md` F11 | ✅ | Applied | Organic emergence → formalisation: AFD's memory-only reviewer rule becomes repo text |
| 25 | `KNOWLEDGE.md` §1 D43 | ✅ | Applied | Knowledge Citations as the anti-hallucination device — the fused field is the same mechanism, with the harm half added because a resolving citation is not a relevant one (SS2) |
| 26 | `KNOWLEDGE.md` §1 D46 | ✅ | Applied | Reviewer Identity, and its measured ½ survival rate — AC-4's non-load-bearing requirement |

**New items the coordinator's table does not carry:**

| # | Source | Item | Why it belongs here |
|---|--------|------|--------------------|
| N1 | `KNOWLEDGE.md` §1 **D61** | TFW-56: universal 10-row Judge checklist, measured rates carried inside each promoted row, structural explicit-N/A at three sites, D42 revoked | The grammar AC-1 must match. The HL predates TFW-56, so §7.2 cannot cite it — and it is the single most binding constraint on how row 2 may be written |
| N2 | `knowledge/constraint.md` **F4** | *"`P{N}` has irreconcilable double semantics: KNOWLEDGE.md §0 vs HL §7"* — ✅ verified | AC-9's subject, cited in TS §5 but absent from §7.2. It is also the evidence that reserving `PP{n}` is a fix rather than a precaution |
| N3 | `KNOWLEDGE.md` §1 **D53** | `evidence/` mandatory in every task directory; RF §5 is a pointer, not a table | Governs `phase-c/evidence/` and the EV file's shape |
| N4 | `knowledge/philosophy.md` **F24** | Instructions produce compliance, heuristics produce competence; cross-stage structural dependency enforces better than a mandate | Why the citation and the harm are **one field**: a reviewer who cannot fill it has failed the row by construction, with no separate rule to obey |
| N5 | `knowledge/process.md` **F19** | Corrected 2026-08-13: `review.md` Step 0 is Session Naming; Judge is Step 3 | Confirms the frozen HL Phase C pointer to *"Step 4 Judge"* is stale, non-substantive (rule 6) |
| N6 | `knowledge/process.md` **F25** | A fabricated citation traversed an entire pipeline undetected and was caught only by the owner | The concrete precedent for why an unverifiable citation must fail the row rather than pass it |

> **Cross-references**: use Reference Format (e.g. `RF TFW-18`, `D24`, `TD-72`). See compilable_contract.md §2. Build script resolves to hyperlinks.

---

*ONB — TFW-53 / Phase C: Goal Defence in Review | 2026-08-13*
