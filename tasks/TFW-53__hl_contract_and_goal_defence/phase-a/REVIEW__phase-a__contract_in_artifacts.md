# REVIEW — TFW-53 / Phase A: Contract in Artifacts

> **Date**: 2026-08-13
> **Author**: Reviewer (Claude Code)
> **Verdict**: ✅ **APPROVE**
> **Review Mode**: spec _(owner override of the configured `code` default — the deliverable is a rule system judged on logical completeness, not compilation)_
> **RF**: [RF Phase A](RF__phase-a__contract_in_artifacts.md)
> **TS**: [TS Phase A](TS__phase-a__contract_in_artifacts.md)
> **Parent HL**: [HL-TFW-53](../HL-TFW-53__hl_contract_and_goal_defence.md) — 🔒 FROZEN, baseline `git log --grep="TFW-53/freeze"`
> **Stage files**: [`review/map.md`](review/map.md), [`review/verify.md`](review/verify.md), [`review/judge.md`](review/judge.md)
> This file is a synthesis of stage findings. Reference stage files for raw evidence.

---

## 1. Map

Phase A makes the HL contract exist as artifact state in exactly three framework files and creates
none. `templates/HL.md` gains a five-field contract header (left open for Phase C), a three-state
marker on every section heading with a subsection-inheritance rule, a `§12 Amendment Log` with a
10-column grammar and explicit `Type`/`Verdict` vocabularies, and a four-property gate clause
appended to §3.1. `templates/RES.md` splits its recommendations into `Refinements` and `Amendment
Proposals` and loses line 32's `Coordinator applies these` — the template-side twin of the
instruction that produced the TFW-49 drift. `conventions.md` gains the governing definition: 21
numbered rules under `#### HL Contract`, a §5 REJECT-branch-(a) redefinition, and seven §14
anti-patterns. 165 insertions, 16 deletions, three files.

Two decisions exceed the TS letter, both declared in RF §2: `🚫 WITHDRAWN` added to the §12 verdict
vocabulary, and rule 6's tripwire time-scoped to "§5 and §6 *as they stand at the moment of
classification*". Both are refinements under the granularity rule the phase itself ships — no frozen
claim moves — and both were **caused by evidence collection**, not by drafting preference.

Nothing here executes. Phase B makes the workflows obey; TS §2 declares that intermediate state
expected, and DoF confirms no workflow file was touched.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|-----------------|--------|----------|
| 1 | Diffstat against the freeze baseline `ffe6c6a` | ✅ | `3 files changed, 165 insertions(+), 16 deletions(-)` — RF §1's total, exact. 0 new framework files, so HL §3.1's *"0 new artifacts in a project's root"* holds |
| 2 | AC-3 gate — `grep "Coordinator applies these" templates/RES.md` | ✅ | **0 matches**. The four deleted lines are precisely the old comment and the old 3-column header. DoF-3 could not have fired |
| 3 | AC-11 gate — no budget / slot / cut-order language in `templates/HL.md` | ✅ | 0 matches, including the hyphenated `cut-order` form the RF's grep omitted. Amendment A12's removal is complete |
| 4 | AC-2 — the pre-A10 token `APPLIED — restrictive` | ✅ | **0 occurrences**. Phase D has no synonym to reconcile |
| 5 | AC-6 gate — recovery command **re-run by the reviewer under both shells** | ✅ | Git Bash: shipped form → 5 commits, rejected `/freeze/` form → **0**. PowerShell 5.1: 5 and 5. Every count and SHA in `baseline_recovery.txt` reproduces. The MSYS asymmetry rule 15 exists for is measured, not asserted |
| 6 | AC-12 gate — reproducible §14 block count | ✅ | `awk … \| grep -c '^- '` → **35**; same command at `ffe6c6a` → **28**. Exactly **+7, −0** |
| 7 | AC-8 — `conventions.md` word/line delta | ✅ | 3,952 → 5,068 words (**+1,116, +28.2%**), 513 → 568 lines. RF §4's figures reproduce exactly |
| 8 | AC-9 gate — `git show 721ca15:…TFW-48/phase-a/HL__phase-a__method_kernel.md` | ✅ | `## 1. Vision` L11 · `## 5. DoD` L116 (**10** items) · `## 6. DoF` L129 (**9** items) · `## 7. Principles` L143 · `## 7.1` L156 · `**Status**: ✅ HL — Approved` L5. Every line number and count in EV §E9 reproduces |
| 9 | AC-4 — three-way agreement of the frozen/free split | ✅ | `conventions.md` §3 table, `templates/HL.md` header, HL-TFW-53 §3 — identical section lists. D24 Pattern A honoured (restated inline, not cross-referenced) |
| 10 | AC-10 — §5 verdict vocabulary and status table unchanged | ✅ | The `APPROVE / REVISE / REJECT` line is byte-identical in the diff; the new blockquote is appended after it; Phase E's status table untouched |
| 11 | `conventions.md` append-only discipline | ✅ | `+55 / −0` — a pure append in §3, §5 and §14. DoF-7 ("§14 restructured or renumbered") is structurally impossible on this diff |
| 12 | Build gate — `pytest docs/scripts/` | ✅ | **68 passed** in 33.87s, matching the RF |
| 13 | Build gate — `mkdocs build` | ⚠️ | Exit **0**, built in 42.05s. One warning is new and attributable to this phase — see V1 in §5 |
| 14 | Evidence artifacts (RF §5 / EV) | ✅ | 12/12 items verified, 0 missing. The seven `N/A`s quote the TS's own `Evidence:` fields **verbatim** — checked word for word against TS AC-1/3/4/5/7/10/12, so they are coordinator design, not executor convenience. Each of the five `VERIFIED` points at a file or exhibit I re-executed |
| 15 | Knowledge citations (HL §7.2 ×26, ONB §7 N1–N3) | ✅ | 29/29 resolve to real items. **0 hallucinations** |
| 16 | Role Lock | ✅ | No HL, TS, RES or workflow file modified. `git diff ffe6c6a` shows the executor wrote only its own ONB/RF/EV, the three in-scope files, and the README board row |

> Raw verification log: [`review/verify.md`](review/verify.md). Verification was **escalated to 100%**
> (6 of 6 files vs. the 3 required by `min_verify_ratio: 0.42`) on the first discrepancy.
> Nothing material could not be verified: every AC gate, every measurement and every evidence claim
> in this RF was independently re-executed.

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ✅ | 12/12 ACs verified against the artifacts rather than against the RF. HL DoD-1…DoD-11 all land. No AC rests on a claim I could not re-execute |
| 2 | Philosophy aligned (matches HL design philosophy) | ✅ | 9 mapped principles (P2, P3, P5, P6, P7, P9, P10, P11, P12), **9 satisfied, 0 violations**. No principle was mapped to a failed AC. Full table: [`review/judge.md`](review/judge.md) §HL §7 Principles Check |
| 3 | Tech debt documented | ✅ | RF §6 carries 6 typed observations with file and line. Five are substantive; obs. 2 is a live resolver bug the executor found by reading build code nobody asked them to read |
| 4 | Style & standards | ✅ | Additions are numbered rules and table rows per TS §6 and `process.md` F4. TS §6's fixed vocabulary shipped exactly; no synonyms invented |
| 5 | Observations collected | ✅ | Quality filter applied in §5 — 6 of 6 survive, severities assigned |
| 6 | RF completeness (§7-9 present) | ✅ | §7 three sourced fact candidates; §8 three insights each carrying an explicit **Implication** — the cognitive mode conventions.md §3 requires and most RFs omit; §9 two diagrams, the second rendering the shipped classification rule as a decision tree with rule numbers on every branch |
| 7 | Evidence completeness (spec mode) | ✅ | All 12 TS Evidence fields covered; statuses valid; the `N/A`-challenge in the Trust Protocol was applied and survived |
| 8 | Analytical quality — logic, completeness, methodology (spec) | ✅ | The three ACs that could have been satisfied by assertion were run against live artifacts and **all three changed the deliverable** — see §4 |
| 9 | Source attribution — claims traceable to evidence (spec) | ✅ | 29/29 citations resolve, 0 hallucinations. Every RF §4 measurement ships with the command that produced it, and all reproduce. RF §8 S2's quotation of the ONB Assessment is verbatim and correct |

## 4. Verdict

**✅ APPROVE**

Twelve of twelve acceptance criteria are met against the artifacts, not against the report. I
re-executed every gate command in the RF — the four greps, both shells of the AC-6 recovery, the
`git show` of the TFW-48 artifact, the §14 block count, the word delta, `pytest` and `mkdocs build` —
and each one reproduces to the number (§2, V1–V16). Twelve of twelve evidence items resolve; 29 of
29 knowledge citations resolve; zero hallucinations. Role Lock held: no HL, TS or workflow file was
touched, and the append-only discipline on `conventions.md` is provable from the diff itself
(`+55 / −0`), which makes DoF-5 and DoF-7 structurally unreachable rather than merely unviolated.

**What earns the approval beyond compliance** is that the evidence requirement functioned as a design
mechanism rather than as reporting overhead. Three of this phase's shipped clauses exist *only*
because a rule was run against reality instead of reasoned about:

- **Rule 15's slash-free recovery form.** The documented command returned zero rows under Git Bash.
  A rule that passes its own wording while failing its purpose is precisely the failure class AC-6
  was written to catch, and it was caught on the artifact's first live use.
- **Rule 14 extending the reserved word to the *first* freeze.** TFW-53's own baseline commit
  `8136306` is non-conforming. The executor reported the rule's first live instance violating it
  rather than quietly scoping the rule around the problem.
- **`🚫 WITHDRAWN`.** Diffing the shipped grammar against 12 live §12 rows surfaced a disposition the
  four-value vocabulary could not name. Recording the gap was all AC-2 asked for; closing it was the
  right call, because a template that cannot carry the artifact AC-2 names as its test corpus is a
  template that fails on the day it ships.

Each would have shipped broken under a reading-only gate. RF §8 S3 makes this claim about itself and
I am confirming it independently: this is the evidence discipline paying for its own cost.

**Two further quality signals.** The AC-8 exercise handles its own circularity better than the AC
required — the disqualifying limit is the *first section of the document*, before the 5/5 score, and
states plainly that agreement measures readability and not correctness. And the executor escalated
two genuine contradictions inside the **frozen** contract at ONB time (DoD-2's column enumeration
against DoD-6's proposer requirement; a `Type` value that its own research defined as a `Verdict`),
neither reachable by reading the TS alone. Both produced owner amendments. That is the amendment
channel working before the artifact that defines it had shipped.

**Five findings, none blocking.** All are Low severity, none touches an acceptance criterion, and
none is a DoF hit. Applying the materiality bar this project has adopted (HL §7 P14 — *a block must
rest on material impact on the value, never on phrasing*), they do not justify a revision cycle. Two
become tech debt (V1, V2 in §5); three are accuracy notes recorded here so the next phase reads the
artifact correctly rather than the report:

1. **`templates/RES.md` says "minus the two fields" and then enumerates four.** HL §12 has 10 columns,
   the RES table has 7 and includes `#`; the difference is three (`Date`, `Proposer`, `Verdict`), and
   `#` is listed as coordinator-added while sitting in the researcher's own table. RF §2 Decision 7
   carries the same error from the other side (7 + 4 = 11). The operative artifact — the table — is
   correct, and AC-3's bullets do not cover this sentence. Still a numeric claim contradicted by its
   own enumeration, in the template defining a column grammar. → **TD-137**.
2. **The build-gate claim is scoped so the phase's own new warning falls outside it.** RF §4 states
   the three changed files produced no warnings — true — but the phase also *created* an EV file
   whose link to `baseline_recovery.txt` mkdocs cannot resolve, emitting a new WARNING. Non-`strict`,
   exit 0, and the `.txt` artifact is TS-mandated, so this is a framework gap rather than executor
   error; the finding is against the scoping of the claim. → **TD-138**.
3. **"Exactly three modified files" is scoped-true and one modification is undisclosed.** Commit
   `e37a8dc` modifies five files and creates four. The two extra are executor-writable (the README
   board row, and the ONB), so there is no Role Lock issue — but the same commit silently strips the
   markdown links from three rows of the ONB §2 table, and that appears in neither RF §1 nor RF §4.
   Given finding 2, the likely motive is silencing mkdocs warnings. It should have been one line in
   RF §1.
4. **RF §2 Decision 3's rationale contradicts its own deliverable.** The RF claims *"only §7.2 carries
   its own marker because it is the one subsection whose state differs from its parent"*; the shipped
   template also marks §7.1 explicitly, and §7.1's state does *not* differ from §7's. The shipped
   state is unambiguous either way, and there is a good unstated reason for the marker — §7.1 is an
   `##` heading, a markup sibling of §7, so inheritance is not visually obvious (RF obs. 1). The
   defect is in the description, not the artifact.
5. **`🚫 WITHDRAWN` has no traceability row where its sibling decision has one.** The `Proposer`
   column, also ruled a refinement, was recorded in HL §12's *"Applied without amendment"* note. This
   one lives only in RF §2 and EV §E2. The executor could not have done otherwise — HL is outside
   their Role Lock — so this is a **coordinator action at `/tfw-docs`**, recorded in §6.

### If REVISE — items to fix:

N/A — no revision required.

### If REJECT — fundamental issues:

N/A.

## 5. Tech Debt Collected

> Quality filter applied to RF §6: all six observations survive — each names a specific file, a
> specific defect and a consequence, and none is filler. Two reviewer findings added (V1, V2).

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| TD-131 | RF TFW-53/A obs. #1 | Low | `.tfw/templates/HL.md` (L150, L155) | `## 7.1` is an `##` heading while `### 7.2` is `###`, so §7.1 escapes the §7 nesting §7.2 observes — and the new inheritance rule asserts a parent-child relation the markup does not express. Pre-existing; ruled out of scope in ONB §6.6. Fixing it changes heading depth in every HL | → Phase D (terminology and consistency pass) |
| TD-132 | RF TFW-53/A obs. #2 | **High** | `docs/scripts/gen_docs.py` (L442–465) | `_replace_phase` globs `tasks/{id}*/Phase{X}/{TYPE}__Phase{X}*.md`, but D50 renamed phase folders to `phase-a/`. Every phase reference (`RF TFW-53/A`) silently falls back to the task root and mis-resolves. **Silent** is what makes it High — the build reports success while every phase cross-reference in the repository points at the wrong file | → next task (own TS); coordinator flagged for triage in ONB ruling 7 |
| TD-133 | RF TFW-53/A obs. #3 | Med | `.tfw/compilable_contract.md` (§2 Reference Format) | `P{N}` resolves to `KNOWLEDGE.md §0`, which D37 removed. HL §7 principle references (`P1`–`P17` in this very HL) therefore have no resolution target | → Phase C (owns the `NS{n}` / `PP{n}` namespace work) |
| TD-134 | RF TFW-53/A obs. #4 | Med | `.tfw/project_config.yaml` (L1–4, L110–113) | `project.name: my-project` and three `echo` placeholders for `build.lint/test/verify`. Consequence of this repository's dual identity (`constraint.md` F6 — simultaneously the upstream template and a live project), but it means **no TFW task in this repo has ever had a working `build` gate from config** — every phase substitutes by hand, as this one did | → backlog; decide whether the live project keeps a separate config from the shipped starter |
| TD-135 | RF TFW-53/A obs. #5 | Low | `.tfw/conventions.md` (§3 HL Contract) | 21 numbered rules in one unbroken block. Readable now; if Phases B/C/E each append their own §3 subsections it needs sub-headings. Compounded by the measured **+28.2% word growth** in this phase alone (3,952 → 5,068), with three phases still to append | → Phase B (measure again before appending); watch, do not pre-emptively restructure |
| TD-136 | RF TFW-53/A obs. #6 | Low | `tasks/TFW-53__…/phase-a/TS__phase-a__contract_in_artifacts.md` (L6, L83) | TS header still carries the broken `git log --grep='/TFW-53/freeze/'` form that AC-6 exists to replace, and AC-2's Evidence says "nine live rows" where §12 now has twelve. Stale-at-write, not defects in the shipped work — but a Phase B executor copying the header form would reproduce the bug this phase fixed | → coordinator, at `/tfw-docs` |
| TD-137 | REVIEW TFW-53/A finding 1 | Low | `.tfw/templates/RES.md` (§ Amendment Proposals) | *"minus the two fields a researcher cannot fill"* then enumerates four (`#`, `Date`, `Proposer`, `Verdict`); the real difference is three, and `#` is listed as coordinator-added while present in the researcher's table. RF §2 Decision 7 repeats it as 7 + 4 = 11. One-sentence fix in a canonical template Phase D will propagate | → Phase B or D (whichever reopens the file first) |
| TD-138 | REVIEW TFW-53/A finding 2 | Low | `docs/mkdocs.yml`, `.tfw/templates/evidence/EV.md` | mkdocs cannot resolve links to non-`.md` evidence artifacts, so every TS that mandates a `.txt`, log or binary attachment adds a build WARNING by construction (first instance: `baseline_recovery.txt`). Either exclude `evidence/` from the docs tree, register non-`.md` artifacts as `extra_files`, or have the EV template reference attachments as plain text rather than links | → backlog; decide before `strict` is ever enabled |

## 6. Traces Updated

- [x] README Task Board — status updated: `🟢 RF (A)` → `📚 KNW (A)`, REVIEW column linked
- [x] TECH_DEBT.md — TD-131…TD-138 appended
- [ ] HL status — **not** updated: Phase A is one of five; HL-TFW-53 stays `🟠 Phase A in execution` until Phase B opens. No frozen section touched by this review
- [x] project_config.yaml — `initial_seq` unaffected (no new task ID)
- [x] Other project files — checked for stale info: TD-136 covers the stale TS header
- [ ] **tfw-docs: Pending** — run `/tfw-docs`. Phase A produced decision-grade material for `KNOWLEDGE.md` §1 (the HL Contract as artifact state; the `freeze` scope word extending D55; the granularity rule) plus the eight TECH_DEBT items above
- [ ] **tfw-knowledge: Pending** — RF §7 carries three fact candidates and this REVIEW adds one. FC1 (the two-shell disagreement) is a standing constraint on every shell command the framework ships and should not wait for a batch

> **Coordinator action, from §4 finding 5:** transcribe the `🚫 WITHDRAWN` verdict-vocabulary
> addition into HL-TFW-53 §12's *"Applied without amendment"* note, alongside the `Proposer` column
> entry it parallels. The executor could not write it (Role Lock); the phase's own thesis is that a
> change to a frozen artifact is visible *as a change*.

> Status reaches ✅ DONE only when both markers above are set.

## 7. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | convention | For TFW phases whose deliverable is framework text — templates, `conventions.md`, workflow rules — the owner reviews in **`spec` mode**, not the `code` default configured in `project_config.yaml`. Offered `code` (the configured default, which would have driven diff-and-build verification) against `spec` (logical completeness and non-contradiction of the rule system), the owner chose `spec`. The configured default is calibrated for a project that ships code; this repository's tasks mostly ship rules, so the default is wrong more often than it is right here | Owner, `/tfw-review` mode selection 2026-08-13 | High |

> **Source format**: Use reference patterns (e.g., `RF TFW-18`, `D24`). See compilable_contract.md §2.

---

*REVIEW — TFW-53 / Phase A: Contract in Artifacts | 2026-08-13*
