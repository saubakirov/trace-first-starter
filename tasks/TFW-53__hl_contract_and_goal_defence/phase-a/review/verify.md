# Verify — "Are the claims true?"

> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: spec
> Min verify ratio: 0.42 (`tfw.review.min_verify_ratio`)
> RF files claimed: 6 (3 modified + 3 created)
> Files to verify: ⌈6 × 0.42⌉ = 3 → **6 of 6 verified (100%)**, escalated on the discrepancies in §Discrepancies

## Verification Log

### V1: `.tfw/templates/HL.md`

- **RF claim:** contract header block (5 fields + a field-usage note, left open for Phase C); three-state marker on every section heading plus a subsection-inheritance rule; new `## 12. Amendment Log` with 10-column grammar, `Type` and `Verdict` vocabularies, append-only/no-edit-before-verdict/remark-is-not-a-verdict instruction, `No amendments.` default; §3.1 gate clause block appended (4 properties + checkpoint). +92 / −6.
- **Actual:** `git diff ffe6c6a -- .tfw/templates/HL.md` → **+92 / −6**, exact. Header carries `Contract` / `Frozen` / `Free` / `Append-only` / `Baseline`, followed by a usage note ending *"Add further header fields below this block, not inside it"* — TS §9's extensibility requirement for Phase C. **14** headings carry markers (§1 §3 §4 §5 §6 §7 §7.1 = `🔒 FROZEN`; §2 §7.2 §8 §9 §10 §11 = `🟢 FREE`; §12 = `🟢 APPEND-ONLY`), which is HL §3's 13-row table plus the explicitly-marked §7.1. §12 present with all 10 columns, three `Type` values, five `Verdict` values including `🚫 WITHDRAWN`, the `PROPOSED`-as-state-of-the-request line, and *"If nothing was ever proposed, write: **No amendments.**"*. §3.1's four properties + *"the owner's checkpoint **before** the spend of tokens and time"*; the pre-existing Working Backwards paragraph, the four format options and the §3.2 contrast survive **verbatim** in the diff (append-only, zero deletions in that block).
- **Match:** ✅

### V2: `.tfw/templates/RES.md`

- **RF claim:** `HL Update Recommendations` rewritten as two classed tables; classify-never-apply instruction; explicit-N/A for both classes; line 32 `<!-- … Coordinator applies these. -->` deleted. +34 / −4.
- **Actual:** `git diff` → **+34 / −4**, exact. The four deleted lines are precisely the old comment, the old 3-column header and its separator. Two `###` tables present: `Refinements — free sections, coordinator applies` (`# · § · What to update · Source`) and `Amendment Proposals — frozen sections, owner verdict required` (`# · § · Type · Proposed change · Evidence · Cost · Alternatives considered`). Instruction opens *"The researcher classifies. The researcher never applies."* and routes proposals to HL §12 as `PROPOSED`. Explicit N/A: *"**No refinements.** / **No amendment proposals.**"*
- **Match:** ⚠️ partial — content correct, one enumeration defect. See D1.

### V3: `.tfw/conventions.md`

- **RF claim:** §3 → new `#### HL Contract` subsection (state table + 21 numbered rules in four groups); §5 → REJECT branch (a) redefined, verdict vocabulary untouched; §14 → 7 anti-patterns appended. +55 / −0.
- **Actual:** `git diff` → **+55 / −0**, exact — a pure append in all three sections, so DoF-7 ("§14 restructured or renumbered") cannot have fired. §3 subsection carries the 3-row state table and rules 1–21 numbered continuously across the four group headers (contract 1–12, Contract Baseline 13–16, Delegated authority 17–19, Phase HL 20–21). §5: the `APPROVE / REVISE / REJECT` list line is byte-identical in the diff; the new blockquote is added *after* it; the §5 status table (Phase E's territory) is untouched. §14: exactly 7 `+` bullets, 0 `-` lines.
- **Match:** ✅

### V4: `phase-a/evidence/EV__phase-a__contract_in_artifacts.md`

- **RF claim:** structured evidence — environment, per-AC table, verdict, three detailed exhibits (E2, E9, E11). Verdict 5 VERIFIED / 0 DEFERRED / 0 BLOCKED / 7 N/A.
- **Actual:** file present, follows `templates/evidence/EV.md` shape. Environment header names OS, runtime, both shells, the substituted build and the CI file. 12 rows, one per AC. The seven `N/A` rows quote the TS's own `Evidence:` field **verbatim** — checked against TS AC-1/3/4/5/7/10/12: all seven match word for word, so the `N/A`s are the coordinator's design decision, not executor judgement. The five VERIFIED are exactly the set TS §6 named (AC-2, AC-6, AC-8, AC-9, AC-11).
- **Match:** ✅

### V5: `phase-a/evidence/baseline_recovery.txt`

- **RF claim:** the documented recovery command run on live history under both shells, plus the rejected form and the pre-rule baseline.
- **Actual:** five labelled blocks. **Independently re-run by the reviewer:** Git Bash `git log --oneline --grep="TFW-53/freeze"` → 5; Git Bash `--grep="/TFW-53/freeze/"` → **0**; PowerShell 5.1 shipped form → 5; PowerShell rejected form → 5; `--grep="TFW-53/task"` → `8136306`. Every number and every SHA in the file reproduces. The MSYS asymmetry the whole rule rests on is real and measured, not asserted.
- **Match:** ✅

### V6: `phase-a/evidence/classification_exercise.md`

- **RF claim:** five discriminating RES iter1 rows classified from the shipped rule text alone, circularity limit stated first.
- **Actual:** the circularity limit is the **first section of the document**, before the score, and states the disqualifying condition plainly — same researcher wrote the rule and the assignments; the executor knew each row's assignment in advance; *"agreement demonstrates that the shipped text is readable … and demonstrates nothing about whether the classification is correct."* The rule text quoted in §Shipped rule text is byte-identical to rules 2, 5, 6, 7 as shipped. Row selection is genuinely discriminating: rows 1–2 are tripwire cases where the naive reading says *refinement* and the answer is *amendment*; row 3 is the inverse; rows 4–5 are controls. §What was not tested names two real gaps (RES assignments unvalidated; rule 7 unexercised by the corpus).
- **Match:** ✅ — and the honesty here exceeds what AC-8 required.

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `git diff --stat ffe6c6a -- .tfw/templates/HL.md .tfw/templates/RES.md .tfw/conventions.md` | `3 files changed, 165 insertions(+), 16 deletions(-)` — matches RF §1 exactly |
| 2 | `grep -c "Coordinator applies these" .tfw/templates/RES.md` | `0` — AC-3 gate reproduces |
| 3 | `grep -niE "cut order\|budget\|slot\|cut-order" .tfw/templates/HL.md` | no matches — AC-11 gate reproduces (RF's grep omitted `cut-order`; the hyphenated form is also absent) |
| 4 | `grep -c "APPLIED — restrictive" .tfw/templates/HL.md` | `0` — the pre-A10 token ships nowhere |
| 5 | `git log --oneline --grep="TFW-53/freeze" \| wc -l` (Git Bash) | `5` |
| 6 | `git log --oneline --grep="/TFW-53/freeze/" \| wc -l` (Git Bash) | `0` — the MSYS failure the rule exists to avoid |
| 7 | same two, PowerShell 5.1 | `5` and `5` — the shell disagreement is confirmed |
| 8 | `awk '/^## 14\) Anti-patterns/,/^### 14\.1/' .tfw/conventions.md \| grep -c '^- '` | `35`; same command on `git show ffe6c6a:` → `28`. **+7, −0** — AC-12 gate reproduces |
| 9 | word count before/after `.tfw/conventions.md` | `3952` → `5068` = **+1116 (+28.2%)**; lines `513` → `568` — RF §4's numbers reproduce exactly |
| 10 | `git show 721ca15:tasks/TFW-48__*/phase-a/HL__phase-a__method_kernel.md` | `## 1. Vision` L11, `## 5. DoD` L116 (**10** items), `## 6. DoF` L129 (**9** items), `## 7. Principles` L143, `## 7.1` L156, `**Status**: ✅ HL — Approved` L5 — every line number and count in EV §E9 reproduces |
| 11 | `python -m pytest docs/scripts/ -q` | **68 passed** in 33.87s — matches RF's 68 |
| 12 | `python -m mkdocs build --config-file docs/mkdocs.yml` | Built in 42.05s, **exit 0** — but see D2 |
| 13 | `git diff --stat ffe6c6a` (unscoped) | 9 files: the 3 in scope, `README.md`, the ONB, and the 4 created artifacts — see D3 |

## Discrepancies Found

**D1 — `templates/RES.md` says "two fields" and then enumerates four.** Shipped text under
`### Amendment Proposals`:

> Same column grammar as HL §12, **minus the two fields** a researcher cannot fill: the coordinator
> adds `#`, `Date` and `Proposer` on transcription, and `Verdict` opens as `PROPOSED`.

HL §12 has 10 columns; the RES table has 7 and **includes `#`**. The difference is three fields
(`Date`, `Proposer`, `Verdict`), not two, and `#` is listed as coordinator-added while sitting in the
researcher's own table. RF §2 Decision 7 carries the same defect from the other side — *"carries 7 of
§12's 10 columns … a researcher cannot fill any of the four"* (7 + 4 = 11). AC-3's five bullets do
not cover this sentence, so no acceptance criterion fails; the operative artifact is the table, which
is correct. But it is a numeric claim contradicted by its own enumeration, in the template that
defines a column grammar, inside the task whose subject is grammatical precision. **Low, fix cheap.**

**D2 — the build-gate claim is scoped so that the phase's own new warning falls outside it.**
RF §4: *"Warnings are pre-existing cross-tree links in other tasks' artifacts (TFW-54, TFW-55); the
three files this phase changed produced none."* True as written. But re-running the build surfaces:

```
WARNING - Doc file 'tasks/TFW-53__hl_contract_and_goal_defence/phase-a/evidence/
          EV__phase-a__contract_in_artifacts.md' contains a link 'baseline_recovery.txt',
          but the target … is not found among documentation files.
```

That file is **new in this phase**, so the warning is new in this phase. The build is not `strict`
and exits 0, and the `.txt` artifact is mandated by TS §5 Evidence Artifacts — mkdocs cannot resolve
a non-`.md` target, so this is a framework-level gap rather than executor sloppiness. The finding is
against the *claim*, not the work: a verification statement scoped to three files while the phase
shipped six. **Low → TECH_DEBT.**

**D3 — "exactly three modified files" is scoped-true, and one modification is undisclosed.**
RF §4 DoF check: *"`git diff --stat` confirms exactly three modified files."* Scoped to the three
target paths, correct. Unscoped, commit `e37a8dc` modifies **five** files and creates four. The two
extra are both executor-writable, so there is no Role Lock issue and no framework file outside scope
was touched — but one is undeclared anywhere: the same commit strips the markdown links from three
rows of the executor's own ONB §2 table (`[\`.tfw/templates/HL.md\`](../../../.tfw/templates/HL.md)`
→ `` `.tfw/templates/HL.md` ``). Given D2, the likely motive is silencing mkdocs link warnings; it is
not stated. **Low.**

**D4 — RF §2 Decision 3's rationale contradicts the shipped template.** The RF says *"only §7.2
carries its own marker because it is the one subsection whose state differs from its parent."* The
shipped template marks **§7.1 explicitly too** (`## 7.1 Quality Contract (optional, for multi-phase
tasks) 🔒 FROZEN`), and §7.1's state does not differ from §7's. The template's own inheritance note
even describes §7.1 as inheriting (*"§7.1 is frozen with §7"*) while the heading carries a marker
anyway. The shipped state is unambiguous either way — §7.1 is frozen on both readings — and there is
a good unstated reason for the marker (§7.1 is an `##` heading, a markup sibling of §7, so inheritance
is not visually obvious; that is RF observation 1). The defect is in the RF's description of its own
deliverable. **Low.**

**D5 — the `🚫 WITHDRAWN` addition has no traceability row, where its sibling decision has one.**
The `Proposer` column, also ruled a refinement, was recorded in HL §12's *"Applied without amendment"*
note by the coordinator. `🚫 WITHDRAWN` is recorded only in RF §2 Decision 1 and EV §E2. The executor
could not have done otherwise — HL is outside the executor's Role Lock — so this is a coordinator
action item at `/tfw-docs`, not an executor defect. Flagged because the phase's own thesis is that a
change to a frozen artifact is visible *as a change*. **Low → coordinator follow-up.**

> Verification was escalated to 100% (6 of 6 files) on D1. No discrepancy touches an acceptance
> criterion: all 12 ACs verify against the actual artifacts.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | AC-1, `N/A` | — | ✅ — quotes TS AC-1's `Evidence:` field verbatim; TS confirms |
| E2 | AC-2, EV §E2 (inline exhibit) | ✅ | ✅ — 12 live rows, not the TS's nine (A9–A12 postdate the TS); column set 10/10; the `RESTRICT`-untested coverage gap is disclosed rather than glossed |
| E3 | AC-3, `N/A` | — | ✅ — verbatim TS field; gate result independently reproduced (0 matches) |
| E4 | AC-4, `N/A` | — | ✅ — verbatim TS field |
| E5 | AC-5, `N/A` | — | ✅ — verbatim TS field |
| E6 | AC-6, [`baseline_recovery.txt`](../evidence/baseline_recovery.txt) | ✅ | ✅ — **re-run by the reviewer in both shells; every count and SHA reproduces** |
| E7 | AC-7, `N/A` | — | ✅ — verbatim TS field |
| E8 | AC-8, [`classification_exercise.md`](../evidence/classification_exercise.md) | ✅ | ✅ — circularity limit stated first, as AC-8 demanded; rule text quoted matches shipped text byte for byte |
| E9 | AC-9, EV §E9 (inline exhibit) | ✅ | ✅ — **`git show 721ca15:…` re-run; all six line numbers and both item counts (10 DoD, 9 DoF) reproduce** |
| E10 | AC-10, `N/A` | — | ✅ — verbatim TS field |
| E11 | AC-11, EV §E11 (inline exhibit) | ✅ | ✅ — 4/4 against HL-TFW-53 §3.1 at `ffe6c6a`; each property cites the specific passage that satisfies it. The exhibit volunteers that the same HL would have **failed** property 4 before 2026-08-10 |
| E12 | AC-12, `N/A` | — | ✅ — verbatim TS field; the reproducible count is in RF §4 and reproduces (28 → 35) |

Total evidence items: 12 · verified: 12 · missing: 0. No `VERIFIED` status rests on an assertion —
each of the five points at a file or an inline exhibit that the reviewer re-executed.

## Knowledge Citations Verified

HL §7.2 carries 26 citations; ONB §7 confirms all 26 read and adds N1–N3. Every referenced item was
resolved against its target file.

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | HL §7.2 #1–#3 | `.tfw/README.md` § Structural Enforcement / Naming Creates Behavior / Candor Over Flattery | ✅ | ✅ |
| 2 | HL §7.2 #4–#10 | `KNOWLEDGE.md` §1 D19, D20, D23, D24, D31, D49, D54 | ✅ | ✅ — all 7 resolve |
| 3 | HL §7.2 #11–#15 | `knowledge/philosophy.md` F4, F13, F21, F22, F25 | ✅ | ✅ — all 5 resolve |
| 4 | HL §7.2 #16–#19 | `knowledge/process.md` F4, F6, F14, F20 | ✅ | ✅ — all 4 resolve |
| 5 | HL §7.2 #20 | `knowledge/constraint.md` F2 | ✅ | ✅ |
| 6 | HL §7.2 #21–#22 | `.tfw/conventions.md` §7, §15 | ✅ | ✅ |
| 7 | HL §7.2 #23–#26 | `KNOWLEDGE.md` §1 D55, `knowledge/process.md` F11, `KNOWLEDGE.md` D43, D46 | ✅ | ✅ |
| 8 | ONB §7 N1–N3 | `KNOWLEDGE.md` §1 D53, D34, D37 | ✅ | ✅ |
| 9 | RF §6 obs. 4 | `knowledge/constraint.md` F6 (repository dual identity) | ✅ | ✅ |

**Hallucinations: 0.** N1 (D53 — `0 of 38 tasks created evidence/` while optional) is load-bearing:
it is the argument the coordinator adopted to make `Proposer` a column rather than prose.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files and recorded findings? — 6 of 6 (100%), escalated per the ratio rule
- [x] Ran at least 1 build/test command? — 13 commands; `pytest` (68 passed) and `mkdocs build` (exit 0) both re-run
- [x] Each RF §3 (AC) checkmark verified against actual file? — all 12 ACs; every gate command re-executed independently
- [x] KNOWLEDGE.md checked — contradictions with changes documented? — none. D19 is narrowed not revoked (RES still produces HL feedback); D20's implicit approval is closed by the `Contract` field; D24 Pattern A is honoured (the frozen/free split is restated inline in both files rather than cross-referenced); D31 is satisfied without a new state file
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total citations: 29 (26 + N1–N3), verified: 29, hallucinations: **0**
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 12, verified: 12, missing: **0**

Stage complete: YES
