# ONB — TFW-53 / Phase A: Contract in Artifacts

> **Date**: 2026-08-13
> **Author**: Executor (Claude Code)
> **Status**: 🟠 ONB — Answered 2026-08-10, cleared to proceed. Two amendments escalated (A10, A11); neither blocks the start of work
> **Parent HL**: [HL-TFW-53](../HL-TFW-53__hl_contract_and_goal_defence.md) — 🔒 FROZEN
> **TS**: [TS Phase A](TS__phase-a__contract_in_artifacts.md)

---

## 1. Understanding

Phase A makes the HL contract exist as artifact state, in three files and nowhere else.
`templates/HL.md` gains a contract header (state + approval date + pointer to the amendment
channel), per-section frozen/free marking, a `§12 Amendment Log` with a column grammar that makes
evidence/cost/alternative impossible to omit, and four gate clauses appended to §3.1.
`templates/RES.md` splits `HL Update Recommendations` into `Refinements` and `Amendment Proposals`
and loses line 32's `Coordinator applies these`. `conventions.md` gains the governing rules: what
freezes and at what granularity (the declarative claim, not the section text), when it freezes
(owner approval), how the baseline is recovered from git, that a verdict is a distinct recorded act,
that delegated authority is a ceiling, that a Phase HL is derivation-only, the REJECT branch (a)
redefinition, and seven §14 anti-patterns. No workflow file is touched — a rule defined here and
enforced nowhere yet is the expected intermediate state, and Phase B is what makes the workflows
obey it.

## 2. Entry Points

| File | What I will touch |
|------|-------------------|
| [`.tfw/templates/HL.md`](../../../.tfw/templates/HL.md) | header block (lines 3–5), §3.1 instruction block (24–37), section headings, new §12 before the footer |
| [`.tfw/templates/RES.md`](../../../.tfw/templates/RES.md) | `## HL Update Recommendations` (31–34), incl. deletion of line 32 |
| [`.tfw/conventions.md`](../../../.tfw/conventions.md) | §3 (Artifact Types → HL), §5 (REJECT verdict branches), §14 (anti-pattern list) |

Read-only references used: HL-TFW-53 §3 (frozen/free table — source of truth), §4 Phase A, §5 DoD
1–11, §6 DoF, §7 Principles + §7.1 Quality Contract, §12 (nine live rows = the AC-2 test corpus);
`research/iter1/RES.md` (D2/D4/D5/D6/D8/D9/D13 + the recommendation rows that AC-8 classifies);
`.tfw/templates/evidence/EV.md`; `docs/scripts/gen_docs.py` (build-side impact of heading markers).

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | **Does §12 get a `Proposer` column?** HL §5 DoD-6 (as amended by A4) requires an owner-initiated change to be *"logged in §12 with the owner as proposer and the verdict on the same row"*. TS AC-2's column grammar has no proposer field, so the requirement has no structural home — and HL §12's own row A9 proves it: the proposer is smeared across two cells as prose (`Proposed change` opens *"Owner-proposed; revised before ruling"*, `Verdict` closes *"proposer and ruler are the same party; recorded per A4"*). **(a)** Ship AC-2's nine columns exactly and record `proposer` in the EV file as a field the grammar cannot hold — TS-literal, and AC-2's Evidence clause explicitly anticipates such a record, but it ships DoD-6 as prose-dependent. **(b)** Add a tenth `Proposer` column — a superset of AC-2's list, so its gate still passes; makes DoD-6 and Principle 11 structurally enforceable; costs one column against F22 template minimalism. **(c)** Fix the grammar of the existing cells instead: `Verdict` becomes `{verdict} — {ruler}, {date}` and `Proposed change` must open with the proposer. **Recommend (b)** — P3 says a rule with no enforcement site is decoration, and this rule currently has none. | **✅ Answer: (b) — add the `Proposer` column. Proceed; this is a refinement, not an amendment, and needs no owner verdict.** Reasoning, so the reviewer can check it: (i) DoD-2's enumeration is **already** non-exhaustive — it omits the `#` column that the live §12 has carried through nine rows and that nobody has treated as a violation. An indicative list is not a closed set. (ii) Under the granularity rule (iter1 D2) the frozen unit is the *declarative claim*. DoD-2's claim is "§12 has a fixed grammar that makes evidence, cost and alternative impossible to omit, plus an explicit-N/A default". A tenth column does not touch that claim. (iii) The D4 tripwire asks whether the change can be accepted under the existing §5/§6 — here it is the only way to *satisfy* existing §5: DoD-6 requires a logged proposer and today has no field to log it in. A change required to meet a frozen criterion is not an amendment against it. (iv) Your N1 is the decisive argument and I am adopting it: D53 measured 0 of 38 tasks creating `evidence/` while it was optional. A proposer recorded in prose is optional by construction. **Also do:** retro-fit the column to HL §12's nine live rows — I have done this, so your AC-2 diff runs against a conforming corpus. Record the reasoning in the RF; I have logged it in §12's applied-without-amendment note. |
| 2 | **What does `APPLIED — restrictive` mean in the shipped grammar, and where is that stated?** TS AC-2 and HL DoD-2 enumerate it as a **Type** value beside `EXTEND` / `SUPERSEDE`. RES iter1 **D8** treats it as a **verdict**: a restrictive change (adds a DoF, narrows scope, drops a deliverable) *"applies immediately and lands in §12 with verdict `APPLIED — restrictive`"*. Both cannot be literally true — as a Type it sits in a column about the change's relation to the baseline, and it leaves the `Verdict` cell of such a row undefined; as a verdict it is absent from the column the TS enumerates it in. D8's restrictive-application rule is stated in no DoD item and no AC, so shipping the enum without it delivers a value whose meaning exists nowhere in the contract. **(a)** Keep it as a Type per the TS, and state the D8 rule in one line — restrictive changes apply on filing, verdict cell reads `✅ APPLIED — no owner verdict required` — with the classification rule in `conventions.md` §3 beside the granularity rule (AC-8 territory). **(b)** Ship the Type value with no semantics in Phase A, strictly TS-literal, and let a later phase define it. **(c)** Drop it from the Type enum and re-introduce it as a verdict value, deviating from AC-2's explicit list. **Recommend (a)** — it is the only option under which the enum means something on the day it ships; but it adds ~2 lines to `conventions.md` §3 that no DoD item mandates, which is a scope call, not mine. | **✅ Answer: (a) for the semantics — ship them now. The token *name* is escalated to the owner as amendment A10; do not block on it.** You are right that both readings cannot hold, and the history explains why: iter1 **D8** coined the token when there was no Type column, then **A2** created the Type column and swept the token into it without re-deciding. Two axes were conflated. The correct decomposition is **Type = relation to the baseline** (`EXTEND` adds, `SUPERSEDE` replaces, a restrictive change *narrows*) and **Verdict = disposition** (applied on filing, no owner verdict required). So `APPLIED — restrictive` is a past participle sitting in a column of relation nouns — incoherent on its face, and P9/D28 is a principle this very TS claims AC-2 enforces. **Do now (unblocked):** state D8's rule in `conventions.md` §3 beside the granularity rule — a restrictive change (adds a DoF, narrows scope, drops a deliverable) applies on filing and is logged with the verdict `✅ APPLIED — no owner verdict required`; restrictive-free is prohibited because the classifier benefits from the label. **Do last:** the Type enum itself. If A10 is approved the third value is `RESTRICT`; if rejected, ship `APPLIED — restrictive` verbatim per DoD-2. Escalated today, so this should not stall you. |

## 3.1 Coordinator rulings on §4 Recommendations, §5 Risks and §6 Inconsistencies

> Answered 2026-08-10 by the coordinator. Numbering follows the executor's.

**Recommendations — all seven accepted.** Three change the TS; I have updated it, re-read §4 and §5 before starting.

| # | Ruling |
|---|--------|
| 1 | **Accepted, and it is a defect in what I wrote.** Ship `git log --grep="{TASK-ID}/freeze"`. A recovery command that returns silently empty on Windows-with-Git-Bash fails AC-6's purpose while passing its wording — that is the distinction AC-6 exists to make. The HL header carried the broken form; I have corrected it. Put the measured transcript in `evidence/baseline_recovery.txt` as you propose |
| 2 | **Accepted.** The reserved scope word applies to the first freeze too. Note the consequence honestly in the RF: TFW-53's own initial freeze `8136306` used scope `task` and is therefore non-conforming. History is not rewritten; the HL header now names it explicitly as the pre-rule baseline. A rule whose first live instance violates it is exactly what a reviewer should catch, and you caught it before it shipped |
| 3 | **Accepted — this is a TS defect, not a deviation.** AC-1 enumerated two states where HL §3 defines three. §12 is `🟢 APPEND-ONLY` and must be marked as such. AC-1 updated; ship three markers |
| 4 | **Accepted.** Marker inside the heading line. Your `gen_docs.py` verification is the kind of check the TS should have specified and did not — carry it into the EV file so the reviewer inherits the proof rather than re-deriving it |
| 5 | **Accepted.** `PROPOSED`, with the one line of D28 reasoning. It describes the state of the request, which is what the log tracks |
| 6 | **Accepted.** `pytest docs/scripts/` + `mkdocs build` is the real gate; `build.*` in `project_config.yaml` are starter placeholders. Record that fact in the RF — it is a live defect of this repository, not of this phase |
| 7 | **Accepted**, already TS §9. Keep the header block one-field-per-line and unclosed |

**Risks — acknowledged; two change the work.**

| # | Ruling |
|---|--------|
| 1 | **Resolved by removing the requirement, not by satisfying it.** You were right that HL §3.1 declares no cut order. The reason it declares none is that the requirement should never have been there: the owner asked for Working Backwards and mandatory visualization; the budget-and-cut-order property came from reference material the owner supplied as an example and was folded into A9 by me as if it had been requested. Owner ruling 2026-08-10: **amendment A12 removes it from the contract entirely** — from §3.1, from `plan.md`, and from the DoD. My A11 is withdrawn. **Action for you: do not implement any budget, slot, size, count or cut-order language anywhere.** AC-11 has been rewritten; re-read it. If any draft you have already started mentions it, delete that part |
| 2 | **Accepted, and your mitigation is better than my AC.** Five discriminating rows including at least two D4-tripwire cases, with the circularity limit stated in the EV file. A 5/5 score that reads as validation is worse than a 3/5 that reads honestly. AC-8 updated to require the discriminating selection rather than any five rows |
| 3 | **Accepted.** Count §14's block specifically; record both counts and the exact command so the reviewer can reproduce. AC-12's gate wording relaxed from `grep -c` to "a reproducible count of the §14 block" |
| 4 | Correct. Append-only in §14; do not touch the §5 status table that Phase E needs |
| 5 | Correct. Report the delta; do not compress the rules below usability to hit an estimate. ~180 lines was a coordinator's estimate, not a budget |

**Inconsistencies — rulings.**

| # | Ruling |
|---|--------|
| 1 | **Proceed per the TS; no amendment needed.** §7.1's *"E owns §5 + §13"* was written before amendment **A5** was approved, and A5 put the REJECT branch (a) rewrite in Phase A. An approved amendment supersedes earlier frozen text — that is what the amendment channel is for. §7.1 reads as amended by A5; TS §9 is the operative allocation. Record as an RF observation so the reviewer does not flag it as drift |
| 2 | **Confirmed and fixed** — see Recommendations 1–2. Both facts are correct as measured |
| 3 | **Confirmed** — see Recommendation 3. AC-1 updated |
| 4 | **Answered in Q2.** Semantics ship now; the token name is amendment A10 |
| 5 | **Answered in Q1.** Column ships as a refinement |
| 6 | Agreed — pre-existing heading-level inconsistency in `templates/HL.md`. Do not fix here; RF observation |
| 7 | **Good find, and it is a live bug.** `gen_docs.py` `_replace_phase` still globs `Phase{X}/` after D50 renamed folders to `phase-a/`, so every phase reference in this task mis-resolves. Out of scope; RF observation → I will triage it to `TECH_DEBT.md` at review |
| 8 | Agreed. `P{N}` resolving to a section D37 removed is real; Phase C owns the namespace work (`NS{n}` / `PP{n}`). RF observation |
| 9 | Agreed. Starter defaults are a consequence of this repository's dual identity (`constraint.md` F6) — it is simultaneously the upstream template and a live project. Pre-existing; drives Recommendation 6 |

**New citations N1–N3: all three accepted.** N1 (D53, `0 of 38`) is now the load-bearing argument in the Q1 answer above — it converted a design preference into a measured one. N2 correctly identifies the docs build as this phase's only real gate. N3 explains inconsistency 8.

**Assessment.** Both blocking questions found genuine contradictions inside the frozen contract — DoD-2 against DoD-6, and a Type value against its own definition in research. Neither was reachable by reading the TS alone; both required cross-reading the HL, the TS and RES iter1 against each other. That is what this gate is for, and it worked on its first use.

## 4. Recommendations (suggestions, not blocking)

1. **Ship the slash-free recovery form** `git log --grep="{TASK-ID}/freeze"`, not the HL prototype's
   `git log --grep='/freeze/'`. Measured in this repository today: the slash form returns **0 rows**
   under Git Bash (MSYS converts the leading `/` into a filesystem path before git sees it) and
   **3 rows** under PowerShell; the slash-free form returns 3 under both. A recovery command that is
   silently empty on Windows-with-Git-Bash fails AC-6's purpose — the baseline is findable — while
   passing its wording. Full transcript goes into `evidence/baseline_recovery.txt`.
2. **State that the reserved `freeze` scope word applies to the *first* freeze too.** TFW-53's own
   initial freeze `8136306` carries scope `task`, so even the working recovery command returns only
   the three re-freezes (`d9a4c57`, `99d4e20`, `dcb9bf1`) and not the baseline the HL header names.
   The rule should not ship in a form whose first live instance is non-conforming.
3. **Mark §12 as a third state, `🟢 APPEND-ONLY`.** AC-1 names two lists (six frozen, six free);
   HL §3's table has thirteen rows in three states. AC-1's own gate requires exact agreement with
   HL §3, and TS §6 says the HL wins on disagreement — so three markers, not two. Flagged here
   rather than silently, because it means the template will carry a state AC-1 does not enumerate.
4. **Put the section marker inside the heading line** (`## 1. Vision 🔒 FROZEN`). Verified safe for
   the docs build: `gen_docs.py` derives no anchors from headings — `add_table_anchors()` only
   injects ids on table rows carrying `D`/`TD`/`P`/`F`/`S` entity ids, and the `§{section}`
   reference form is not resolved to a heading slug anywhere in the resolver.
5. **Use `PROPOSED`, not `UNAPPROVED`, as the empty-verdict value**, and spend one line saying why:
   `PROPOSED` describes the state of the *request*, which is what the log tracks, while TFW-52's
   field-tested `UNAPPROVED` describes the state of the world. RES iter1 coordinator note 3 asks for
   exactly this line of D28 reasoning rather than an unexamined default; HL §3's worked example
   already uses `PROPOSED`.
6. **Build gate will be `pytest docs/scripts/` plus `mkdocs build`.** `project_config.yaml`
   `build.lint/test/verify` are unconfigured placeholders (`echo "configure your …"`), so they
   verify nothing. `conventions.md` and `.tfw/templates/**` are Source Manifest rows 4 and 13 —
   the docs pipeline is the only build that actually consumes what this phase changes.
7. **Keep the header block open-ended** — one field per line, no closing enumeration — because
   Phase C adds the north-star pointer to the same block (TS §9).

## 5. Risks Found (edge cases, potential issues not in TS)

1. **AC-11's evidence will probably return a negative on the task's own HL.** HL-TFW-53 §3.1 states
   who judges (implicitly), the medium, and a scale figure (*"12 files modified, 2 post-mortem files
   created, 0 new artifacts in a project's root"*), but it declares **no cut order** — what goes
   first if the outcome overflows its constraint. That is one of the four properties AC-11 ships.
   The TS anticipates this (*"that is a finding, not a formality"*), but the consequence is an RF
   carrying an unresolved finding against a frozen section that the executor may not touch and has
   no channel to amend. Confirm the finding is the intended terminus.
2. **AC-8's classification exercise is partially circular by construction.** RES iter1's own
   self-critique says it: the row classifications were produced by the same researcher who wrote the
   granularity rule. Agreement therefore demonstrates the shipped text is *readable*, not that the
   rule is *correct*. Mitigation: I will pick five rows that discriminate — including at least two
   where the naive reading and the RES classification differ (the D4 tripwire cases) — and state the
   limit explicitly in the EV file rather than letting a 5/5 score read as validation.
3. **AC-12's `grep -c` gate is ambiguous on the current file.** `conventions.md` §14 is an
   unnumbered bullet list and the file contains bullet lists in nine other sections, so a loose
   pattern counts the wrong thing. I will count §14's block specifically and record both the
   before/after counts and the command used, so the reviewer can reproduce it.
4. **Four phases append to §14 and two edit §5.** A renumber or restructure in this phase creates
   conflicts in three others (DoF-7). I will append only, and will not touch the §5 lines Phase E
   needs (the status table); AC-10 changes only the REJECT branch (a) sentence.
5. **`conventions.md` attention budget.** TS §6 warns the file is near it. AC-8 requires the
   before/after word-count delta in the RF. If the delta lands materially above the TS's ~180-line
   estimate I will report it in the RF rather than compress the rules below usability — but the
   estimate is a signal I am tracking from the start, not at the end.

## 6. Inconsistencies with Code (spec vs reality)

1. **HL §7.1 vs HL §5 DoD-10 / TS AC-10 on `conventions.md` §5 ownership.** §7.1's Quality Contract
   says *"E owns §5 + §13"*; DoD-10 (approved amendment A5) and TS AC-10 put the REJECT branch (a)
   rewrite in Phase A. TS §9 resolves it — different lines, sequence A before E. Proceeding per the
   TS; recorded because §7.1's text still reads as an unconditional assignment.
2. **The HL header's own baseline reference does not work as written.** `git log --grep='/freeze/'`
   returns nothing under Git Bash on Windows, and the initial freeze it names (`8136306`) uses the
   scope word `task`, so it is unreachable by the documented command under any shell. Both facts
   measured today; see Recommendations 1–2.
3. **AC-1 enumerates two section states; HL §3 defines three.** §12 is `🟢 APPEND-ONLY` in HL §3 and
   absent from both of AC-1's lists.
4. **`APPLIED — restrictive` is a Type in the TS/HL and a verdict in RES iter1 D8.** Blocking Q2.
5. **DoD-6 requires a logged proposer; AC-2's column grammar has no field for one.** Blocking Q1.
6. **`templates/HL.md` §7.1 is an `##` heading while §7.2 is `###`** (lines 121 and 126), so §7.1
   escapes the §7 nesting that §7.2 observes. Pre-existing, unrelated to this phase's ACs; will not
   be fixed here, will be recorded as an RF observation.
7. **`gen_docs.py` phase-reference resolver is stale since D50.** `_replace_phase` globs
   `tasks/{id}*/Phase{X}/…`, but phase folders were renamed to `phase-a/` by TFW-42. Phase refs such
   as `RF TFW-53/A` silently fall back to the task root and mis-resolve. Out of scope; RF observation.
8. **`P{N}` in the Reference Format resolves to `KNOWLEDGE.md §0`,** which D37 removed. HL §7's
   `P1`–`P17` therefore have no resolution target. Out of scope — HL §4 Phase C assigns the
   namespace work (`NS{n}` / `PP{n}`) to that phase; RF observation.
9. **`project_config.yaml` carries starter defaults** — `project.name: my-project`, all three
   `build.*` commands are `echo` placeholders. Pre-existing; drives Recommendation 6.

## 7. Knowledge Citations

> Coordinator's citations are HL §7.2, items 1–26. Each confirmed read below, with how it applies to
> Phase A specifically. Items whose force lands in Phases B/C/D are marked N/A **for this phase**,
> not dismissed.

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | `.tfw/README.md` § Structural Enforcement | ✅ | Applied | Drives Q1 and Q2: a value or a requirement with no field to live in is decoration. The contract ships as header state + §12 rows + marked headings, not as advisory text |
| 2 | `.tfw/README.md` § Naming Creates Behavior | ✅ | Applied | The shipped words are fixed by TS §6: `Contract`, `FROZEN`, `Amendment`, `Amendment Log`, `EXTEND`, `SUPERSEDE`, `APPLIED — restrictive`, `Contract Baseline`. No synonyms invented for Phase D to reconcile |
| 3 | `.tfw/README.md` § Candor Over Flattery | ✅ | Applied | Directly shapes this ONB: the recovery command is reported broken and the task's own §3.1 is reported as a probable AC-11 failure, rather than smoothed over |
| 4 | `KNOWLEDGE.md` §1 D19 | ✅ | Applied | AC-3 narrows it, never revokes it — RES keeps producing HL feedback; only the frozen channel turns from write to propose. DoF-8 is the guard |
| 5 | `KNOWLEDGE.md` §1 D20 | ✅ | Applied | Implicit approval is the root cause AC-1 closes: the contract state field is what makes an approved HL structurally distinguishable from a draft |
| 6 | `KNOWLEDGE.md` §1 D23 | ✅ | N/A this phase | `plan.md` is untouched here (DoF-5). The equivalent discipline for `conventions.md` is TS §6's "numbered rule or table row, never a prose block" |
| 7 | `KNOWLEDGE.md` §1 D24 | ✅ | Applied | Pattern A: the frozen/free lists are restated inline in both `templates/HL.md` and `conventions.md` rather than one referencing the other. AC-1 and AC-4 require exactly this, with HL §3 as the single decision point |
| 8 | `KNOWLEDGE.md` §1 D31 | ✅ | Applied | Settled by RES iter1 D5 — no snapshot file; two contracts that can disagree is worse than one. State lives in the HL file plus git history |
| 9 | `KNOWLEDGE.md` §1 D49 | ✅ | Applied | Explains why AC-2's column grammar is the deliverable rather than an instruction to "record evidence": the columns are the gate |
| 10 | `KNOWLEDGE.md` §1 D54 | ✅ | N/A this phase | Adapter sync is Phase D. Relevant only as a constraint on wording — Recommendation 4's heading marker must not depend on any tool's rendering |
| 11 | `knowledge/philosophy.md` F4 | ✅ | Applied | The same lever as citation 1, stated as the project fact it came from; underwrites Q1's recommendation |
| 12 | `knowledge/philosophy.md` F13 | ✅ | Applied | All shipped examples stay domain-neutral; §3.1's "medium the stakeholder can judge" must not narrow to code or UI |
| 13 | `knowledge/philosophy.md` F21 | ✅ | Applied | AC-2's `"No amendments."` default, and the same treatment for the RES split when a class is empty |
| 14 | `knowledge/philosophy.md` F22 | ✅ | Applied | Only §12 is added to the HL template — no optional blocks. It is also the cost side of Q1's option (b) |
| 15 | `knowledge/philosophy.md` F25 | ✅ | Applied | Why Q1 and Q2 are questions and not executor decisions: both change what the contract grammar can express |
| 16 | `knowledge/process.md` F4 | ✅ | Applied | Every `conventions.md` addition lands as a numbered rule or a table row |
| 17 | `knowledge/process.md` F6 | ✅ | Applied | The recorded, unfixed instance this phase closes. Held as the reason to keep AC-7's ceiling clause blunt rather than diplomatic |
| 18 | `knowledge/process.md` F14 | ✅ | Applied | Agents route around non-structural gates — the argument for marking every section heading (AC-1 bullet 5) instead of relying on the header alone |
| 19 | `knowledge/process.md` F20 | ✅ | Applied | Precedent for §6 item 1: an HL/TS divergence is escalated, not silently resolved by the executor |
| 20 | `knowledge/constraint.md` F2 | ✅ | N/A this phase | The 700–900/1200-word budget governs workflow documents; no workflow is touched here. `conventions.md` is measured instead, per AC-8 |
| 21 | `.tfw/conventions.md` §7 | ✅ | N/A this phase | CL/AG is the section AT extends in TFW-54. Untouched here — DoF-4 |
| 22 | `.tfw/conventions.md` §15 | ✅ | Applied | Role Lock holds: I write ONB, RF, EV and the three in-scope files. I do not amend HL §3.1 even where AC-11's evidence shows it failing |
| 23 | `KNOWLEDGE.md` §1 D55 | ✅ | Applied | Supplies the `[agent/task/scope/role]` slot that AC-6's reserved `freeze` word occupies — and, measured against live history, the source of Recommendations 1–2 |
| 24 | `knowledge/process.md` F11 | ✅ | Applied | TFW-52 iteration 2 hand-rolled this protocol; formalising it is the documented pattern. Concretely: it is why `PROPOSED` vs TFW-52's field-tested `UNAPPROVED` deserves a stated reason (Recommendation 5) |
| 25 | `KNOWLEDGE.md` §1 D43 | ✅ | N/A this phase | The citation-as-anti-hallucination device lands in Phase C's Purpose Check. Read to keep Phase A's vocabulary compatible with it |
| 26 | `KNOWLEDGE.md` §1 D46 | ✅ | N/A this phase | Reviewer Identity is Phase C. Its lesson is carried here as a warning, not a deliverable: D46's *"not rubber stamp"* half was recorded and never shipped, so Phase A puts its rules in fields and columns rather than in exhortation |

**New items the coordinator did not cite, found relevant:**

| # | Source | Item | Why it matters here |
|---|--------|------|---------------------|
| N1 | `KNOWLEDGE.md` §1 D53 | Evidence folder mandatory; `0 of 38 tasks created evidence/` while optional | The empirical case that an optional field is an absent field — applies directly to Q1 (a proposer recorded in prose is optional by construction) |
| N2 | `KNOWLEDGE.md` §1 D34 | Compilable Contract, Source Manifest, Reference Format | `conventions.md` and `.tfw/templates/**` are Manifest rows 4 and 13, which makes the docs build the real build gate for this phase (Recommendation 6) and makes heading-marker choice a build-side question (Recommendation 4) |
| N3 | `KNOWLEDGE.md` §1 D37 | KNOWLEDGE.md §0 removed | Explains inconsistency 8: the `P{N}` resolver still points at a section that no longer exists |

> **Cross-references**: use Reference Format (e.g. `RF TFW-18`, `D24`, `TD-72`). See compilable_contract.md §2. Build script resolves to hyperlinks.

---

*ONB — TFW-53 / Phase A: Contract in Artifacts | 2026-08-13*
