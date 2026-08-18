# RF — TFW-53 / Phase D: Glossary, Adapters and Version

> **Date**: 2026-08-14 · **second pass 2026-08-18**
> **Author**: Executor (Claude Code)
> **Status**: 🟢 RF — Complete, corrected after review
> **Parent HL**: [HL-TFW-53](../HL-TFW-53__hl_contract_and_goal_defence.md) — 🔒 FROZEN
> **TS**: [TS Phase D](TS__phase-d__glossary_adapters_version.md) — approved 2026-08-13, amended 2026-08-14 after ONB
> **ONB**: [ONB Phase D](ONB__phase-d__glossary_adapters_version.md) — Q1 → (a), Q2 → (a), Q3 → (a); R1-R5 approved, R6 overruled
> **REVIEW**: [REVIEW Phase D](REVIEW__phase-d__glossary_adapters_version.md) — 🔄 REVISE, four items
> **Covers**: frozen DoD 30–33 · corrective pass AC-8 to AC-12
> **Ships**: TFW **v1.2.0**

> **Second pass, 2026-08-18.** The reviewer was right on all four items and I reproduced each before
> touching anything: the total-file count, the `-U0` hunk count, the substitution count, and the
> Human-Only Test failures. **No framework file was re-edited except AC-11's two links** — no glossary
> article changed, no adapter was re-copied, the release stands. AC-1 to AC-7 keep their functional
> outcomes, which the reviewer confirmed. This pass repairs the **trace**, not the work. Every
> correction is marked ⟳ so the first-pass claim and its replacement are both readable.

---

## 1. What Was Done

### New Files — six, all **trace**, none product ⟳

> ⟳ **Corrected 2026-08-18 (AC-8).** The first pass listed five files here and omitted the RF itself.
> Under the owner's ruling of 2026-08-18 — *the scope budget counts product files, not task artifacts* —
> all six are trace and none spends the budget. `conventions.md` §6's own rationale is *"agent maintains
> full context of changed files"*, and a saved `grep` capture carries no context to hold.

| File | Description |
|------|------------|
| `phase-d/RF__phase-d__glossary_adapters_version.md` | This file. Omitted from the first pass's own list |
| `phase-d/evidence/EV__phase-d__glossary_adapters_version.md` | Structured evidence — 19 rows, verdict recomputed in §5 |
| `phase-d/evidence/drift-check-before.txt` | The `config.md` drift check run verbatim before the sync: 14 `DRIFT:` lines |
| `phase-d/evidence/direction-check.txt` | Per-pair source-only / copy-only counts, run **before** any copy |
| `phase-d/evidence/drift-check-after.txt` | The same check after the sync: no output |
| `phase-d/evidence/ac-gates.txt` | Every AC gate command with its output |

### Modified Files — the six framework files (AC-7 requires a justification per file)

`git diff --stat`, framework files only:

```
 .tfw/compilable_contract.md    |  4 ++--
 .tfw/conventions.md            |  4 ++--
 .tfw/glossary.md               | 36 ++++++++++++++++++++++++++++++++++--
 .tfw/templates/HL.md           |  8 ++++----
 .tfw/templates/review/judge.md |  6 +++---
 .tfw/workflows/review.md       |  4 ++--
 6 files changed, 47 insertions(+), 15 deletions(-)
```

| File | ± | Justification — every hunk is a substitution, a named debt fix, or an addition |
|------|---|------|
| `.tfw/glossary.md` | +34 / 2 changed | **Addition:** ten articles — nine under a new `## Contract and Purpose Defence` grouping, `Result Visualization` between `Value Flow` and `Findings Map`. **Two substitutions:** PV Index priority 0 `frozen baseline` → `contract baseline`; Knowledge Gate `Phase 0` → `Step 2` (TD-163) |
| `.tfw/templates/HL.md` | 4 changed | **One debt fix:** line 10, the inline recovery command → a pointer to `conventions.md` §3 rule 15 (TD-164). **Three substitutions:** the north-star field label and its explainer (:18, :20) gain `Project`; :22 `frozen baseline` → `contract baseline` |
| `.tfw/templates/review/judge.md` | 3 changed | **Three substitutions**, all in the Purpose Check block: the hybrid *"committed frozen baseline"* → `contract baseline` (:34), the fallback chain (:35), the Checkpoint row (:84) |
| `.tfw/compilable_contract.md` | 2 changed | **Two debt fixes:** `PP{N}` and `NS{N}` added to the Resolution rules (TD-165); `KNOWLEDGE.md` §0 removed from *"Where references appear"* (TD-167) |
| `.tfw/conventions.md` | 2 changed | **Two substitutions:** :94 *"frozen contract baseline"* → *"contract baseline"*; :108 the north-star fallback rule |
| `.tfw/workflows/review.md` | 2 changed | **Two substitutions:** :28 the context-loading line, :87 the Purpose Check paragraph. Word-neutral — 1,176 before, 1,176 after |
| `.tfw/workflows/plan.md` | **0** | **Untouched.** The TS listed it as MODIFY, but it carries no occurrence of either retired form. Deviation recorded in §3 |

### Modified Files — adapters, entry points, release, registry

| File | Changes |
|------|---------|
| `.claude/commands/tfw-{plan,review,research,init,handoff,update,knowledge}.md` × 7 | Byte copies from `.tfw/workflows/`. Diffstat lines: plan 82 · init 41 · handoff 14 · review 12 · update 12 · research 6 · knowledge 2 |
| `.agent/workflows/tfw-{plan,review,research,init,handoff,update,knowledge}.md` × 7 | Identical set, identical figures |
| `.tfw/adapters/codex/skills/tfw-plan/SKILL.md` · `.agents/skills/tfw-plan/SKILL.md` | One word: `description` said *"creates or revises **approved** HL/TS artifacts"* — a permission `conventions.md` §3 rule 3 now forbids. Both copies stay byte-identical |
| `CLAUDE.md` | Two purpose cells rewritten (`/tfw-plan`, `/tfw-review`); two rows added (`/tfw-knowledge`, `/tfw-config`) per the coordinator's recorded R6 extension. No new section |
| `AGENTS.md` | **Unchanged** — checked row by row, nothing false. AC-4 directs change only on falsity |
| `.tfw/VERSION` · `.tfw/project_config.yaml` | `1.1.0` → `1.2.0`, in lockstep |
| `.tfw/CHANGELOG.md` | One `## [1.2.0]` entry covering Phases A–D, five blocks, with the TFW-54 pointer. Both `[Unreleased]` bullets folded into `### Changed`, the drift-check sentence corrected from 12 to 14 and from *"not yet repaired"* to repaired |
| `TECH_DEBT.md` | Five closures with reasons (TD-157, TD-163, TD-164, TD-165, TD-167); two re-routes out (TD-158, TD-131); one new debt (TD-170) |
| `README.md` | Board row only — **left unstaged**, see §2 D8 |

### File accounting under the stated rule ⟳ (AC-8)

> **Counting rule, quoted:** *"the budget counts product files, not task artifacts. The RF, the EV file
> and its attachments are the trace of a change, not the change."* — owner ruling 2026-08-18, TS AC-8.

| Class | Count | Limit | Detail |
|---|---|---|---|
| **Modified product files** | **28** | 30 · `max_modified_files` 30 | 27 in commit `ce30f3b` + `README.md`, modified in the working tree and deliberately unstaged |
| ├─ of which byte `cp` | 14 | — | zero authored content: 7 workflows × 2 adapter folders |
| └─ of which authored | 14 | — | 6 framework files · 2 Codex router copies · `CHANGELOG` · `VERSION` · `project_config` · `CLAUDE.md` · `TECH_DEBT.md` · `README.md` |
| **New product files** | **0** | `max_new_files` 15 | none |
| **Trace files** (not budgeted) | 6 | — | this RF · the EV file · four command-output attachments |

**Total product files touched: 28 of 30.** Under the limit, with the rule named beside the number.

**Two figures in circulation were wrong, and I am not adopting either:**

- The first pass reported *"28 modified, 5 new, against 30 / 15"* and compared only the sub-limits. It
  never computed a total, which is what let a 33-file phase read as green. The reviewer was right to
  call that masking.
- **TS AC-8 says "27 modified product files"; the correct figure is 28.** 27 is the commit's modified
  count, which omits `README.md` — a product file this phase changed twice (board row to `🟠 ONB`, then
  to `🟢 RF`) and will change a third time now. Being unstaged does not make it untouched. The
  conclusion is unaffected — 28 < 30 — and the ambiguity is filed as **TD-173**.

## 2. Key Decisions

1. **`uncommitted baseline` left untouched (ONB Q1 → (a)).** The phrase names the *absence* of a baseline, not a synonym for it. Substituting `contract` into it produces a sentence meaning its opposite, and repairing that is a rewrite — DoF-1. The gate is read as `grep -roE "[^n]committed baseline"`, which returns 0 both before and after. Two occurrences survive by design: `conventions.md`:75 and `plan.md`:60.
2. **The north-star field label was renamed, not exempted (ONB Q2 → (a)).** `templates/HL.md`:18 and :20 were the only two genuine bare-capital occurrences in the framework. A form field reading `North Star` while the glossary defines `Project North Star` teaches the wrong name at the moment the reader learns it. Cost: 2 lines, +2 words, in a template off F2's budget.
3. **The nine contract terms got one grouping, not two (ONB R1).** `## Contract and Purpose Defence` after `## Artifact Types`. The five contract terms and the four review-side terms are one mechanism read from two ends; 35 → 36 groupings is the minimal structural change to a file with 78 existing entries.
4. **The AC-1 gate is case-insensitive, and this was not cosmetic.** A case-sensitive `grep -c "deferral confession"` returns **0** across the whole framework — the term ships as `**Deferral confession**` at `judge.md`:50. The original gate would have failed a term that exists and driven a false conclusion that Phase C never shipped it. The glossary heading matches the shipped casing rather than the DoD's, so one name carries one form.
5. **All fourteen adapter copies were re-synced, after a direction check, not on faith.** Six were this task's doing (`tfw-plan` ×2, `tfw-review` ×2, `tfw-research` ×2); eight belong to earlier tasks (`tfw-init` ×2, `tfw-handoff` ×2, `tfw-update` ×2, `tfw-knowledge` ×2). Before copying, every pair was diffed and every copy-only line read: each is an older form of a source-only line in the same hunk. **No copy held content its source lacks**, so the stop condition did not fire and the copy propagated already-reviewed content only.
6. **One word changed in the Codex `tfw-plan` router; `tfw-review` was left alone.** AC-3 permits editing only statements that are now false. `tfw-review`'s contract survives the contract mechanism intact. `tfw-plan`'s `description` granted revision of an *approved* HL — precisely what Phase A removed. Removing `approved` is the minimal true edit; adding a freeze/amendment statement would have been an addition, not a correction, and is reported in §6 instead.
7. **The `[Unreleased]` block was edited, not folded verbatim (ONB R4).** Its closing sentence read *"First run of the check found 12 drifted copies (6 workflows × 2 folders) — recorded, not yet repaired."* Carried as written into `1.2.0`, the release note would have been false about the release it announces, on the day it ships, in the exact number that release corrects. `grep -c "12 drifted copies"` now returns 0.
8. **`README.md` was edited but not staged (ONB R3).** The working tree carries a concurrent uncommitted TFW-55 row change. Staging `README.md` by path would sweep another session's work into a TFW-53 commit. The board row is written; the coordinator lands the file. TS §9 provides this fallback explicitly.
9. **The registry re-scan the coordinator ordered found a second omission.** Beyond TD-158, **TD-131** points at Phase D and appears in neither TS list. Treated the same way — re-routed out with the reasoning recorded — because its own text says fixing it *"changes heading depth in every HL"*, a structural change to a shipped template inside Phase A's section, not a naming fix.
10. **The resolver gap was filed once, for four patterns, not four times (coordinator ruling on ONB §5.4).** TD-165's stated defect is closed. TD-170 records the wider finding: `gen_docs.py` resolves only `TD-{N}` and `D{N}`, so `P{N}` and `F{N}` were already aspirational in the same line before NS/PP joined them.
11. **The Codex `tfw-plan` router carried a false permission, and byte-parity could never have caught it.** ⟳ *Re-homed here from §8 S3 by AC-10 — it describes a change that was made, not an insight.* The `description` field read *"creates or revises **approved** HL/TS artifacts"*: written before the contract existed, true then, and granting exactly what `conventions.md` §3 rule 3 now forbids. The routers are deliberately **not** copies, so a `diff`-based parity check passes over them by design. Only a human reading a router against the mechanism catches it, which is why AC-3 states that as a separate bullet from the `cp`. One word removed, in both the source and the installed copy.
12. **Review item 1 was refused, and the refusal is the coordinator's, recorded.** ⟳ The reviewer asked to *"consolidate or remove at least three supporting evidence files"* to bring 33 under 30. Deleting proof to satisfy a counter is not available in this framework — the four attachments are the raw output of the gates AC-3 and AC-5 turn on. The coordinator refused it as written and ruled the counting subject instead (§1, AC-8). I record the refusal here rather than quietly complying, because a reviewer reading the next RF must be able to see that an instruction was declined, and by whom.
13. **The first pass's `12 hunks` came from a command run over a different file set than the claim describes.** ⟳ The ledger names six files — the five substitution and debt-fix targets **plus `glossary.md`**. The command I actually ran listed `plan.md` (0 hunks) and **omitted `glossary.md`** (4 hunks): 16 − 4 + 0 = 12. The number and the sentence were written in the same session and neither checked the other. Corrected in §3, §4 and §9; the classification underneath is unchanged, and the reviewer confirmed it independently.
14. **The evidence verdict was recomputed, not restored** (AC-12). Two rows moved because their underlying artifacts changed; seventeen were left alone. §5 carries the row-level accounting.

## 3. Acceptance Criteria

| AC | Gate | Result |
|----|------|--------|
| **AC-1** — vocabulary defined | `grep -ci` each term ≥ 1; `wc -w` per article | ✅ 10/10 terms ≥ 1 (lowest is 1, highest 5). All ten articles 41–50 words against the p75 = 50 ceiling. Each ends with a `→` pointer; every pointer target opened and confirmed |
| **AC-2** — one name per concept | `grep -rn` each retired form → 0; `wc -w` both workflows | ✅ `frozen baseline` **8 → 0**. `committed baseline` excluding the negation **0 → 0**. Bare `North Star` **2 → 0** (one line-wrap artefact remains and is recorded). `plan.md` 1,195 → **1,195**, `review.md` 1,176 → **1,176** |
| **AC-3** — adapter parity | drift check → no output; `diff` per copy → empty | ✅ 14 `DRIFT:` lines → **silent**, exit 0. All 22 pairs diff to 0 lines. Direction verified per pair before copying. The six/eight split is stated in §2 D5. Codex routers checked; one false statement found and fixed |
| **AC-4** — entry points | read both tables against the shipped workflows | ✅ Both `CLAUDE.md` cells rewritten and read back against `plan.md` Steps 4/6c/6d and `review.md` Step 3. Two rows added under the recorded extension. `AGENTS.md` unchanged — nothing false. No new section in either file |
| **AC-5** — release shippable | `cat VERSION`; `grep -c` config; `grep -c TFW-54` | ✅ `1.2.0` · `1` · `1`. One `[1.2.0]` entry, five blocks, Phases A–D. `[Unreleased]` folded and corrected |
| **AC-6** — five debts, TD-164 first | open each line; `pytest docs/scripts/` | ✅ TD-164 closed first, by replacement not rewording. TD-163 (glossary half), TD-165, TD-167 closed; TD-157 closed by AC-3. Each records the reason. **68 passed**, unchanged from the pre-phase baseline |
| **AC-7** — no unasked content change | `git diff` reviewed hunk by hunk | ✅ ⟳ **Ledger corrected 2026-08-18, see AC-9.** `git diff -U0 ce30f3b^ ce30f3b` over the six ledger files returns **16** hunk headers (14 at default context), classifying as **10 substitution hunks carrying 11 substituted lines**, 4 named debt fixes and 2 addition sites. The first pass said *"twelve hunks … eight substitutions"*; both figures were wrong. **The classification is unaffected, and the reviewer confirmed it:** no hunk is a rewritten sentence, no section was added, no template gained a field |
| **AC-8** — budget counted under a stated rule | the recount, with the rule quoted beside it | ✅ **28 modified product files of 30**, 0 new product, 6 trace files listed separately. The rule is quoted in §1 from the owner's 2026-08-18 ruling. **I do not adopt the TS's own figure of 27** — it omits `README.md`, a product file this phase changed. Ambiguity filed as **TD-173** |
| **AC-9** — the ledger reproduces | run the named command, compare | ✅ `git diff -U0 ce30f3b^ ce30f3b -- <six files>` → 16 hunk headers: `conventions.md` 2 · `glossary.md` 4 · `templates/HL.md` 4 · `judge.md` 2 · `review.md` 2 · `compilable_contract.md` 2. Full reconciliation in §9. AC-7 asked for `--stat`; **both are now reported**, each labelled with the command that produced it |
| **AC-10** — §7/§8 carry knowledge, not computation | read §7 and §8; confirm each re-homed item is at its destination | ✅ §8 is `No strategic insights.` with its reason. §7 keeps **FC3 only**. S3 → §2 D11, S4 → §6 obs. 8, S2's operative half → §6 obs. 9, FC5 → §6 obs. 10. S1, FC1, FC2 and FC4 dropped as duplication of rulings the ONB and TS already carry. Template contradiction filed as **TD-174** |
| **AC-11** — broken entry-point links | `grep -rn "PROJECT_CONFIG" CLAUDE.md AGENTS.md` → no matches | ✅ Both `CLAUDE.md` links now read `.tfw/project_config.yaml`, and the target exists at that path. Gate returns nothing. The repo-wide sweep the AC required was run — every other occurrence is history that must not be rewritten, or the rule itself; enumerated in §6 obs. 11. TD-172 closed |
| **AC-12** — verdict recomputed | read the verdict against its rows | ✅ **17/19 → 19/19**, stated as a recomputation: E17 and E19 moved because their artifacts changed, and five rows were added for this pass. No row upgraded without an underlying change. Row-level accounting in §5 |

**Definition of Failure — all nine clear:**

| DoF item | Status |
|---|---|
| A sentence rewritten under the consistency banner | ✅ clear — hunk-by-hunk review, §1 table |
| `plan.md` or `review.md` crosses 1,200 words | ✅ clear — 1,195 and 1,176, neither moved |
| Drift check still prints, or the sync reported without running it | ✅ clear — run before and after, both captured verbatim |
| An adapter copy found ahead of its source and merged | ✅ clear — direction check on all 14 pairs before copying |
| A glossary article restates a rule instead of defining a term | ✅ clear — max 50 words, each pointing at the rule rather than reproducing it |
| TD-164 closed by editing the command rather than replacing it | ✅ clear — the command is gone, replaced by the pointer |
| A re-routed debt fixed here anyway | ✅ clear — TD-120/140/142/153/154/155/158/131 all untouched |
| `VERSION` and `tfw.version` disagree | ✅ clear — both `1.2.0` |
| Ships without the TFW-54 pointer | ✅ clear — named in the `[1.2.0]` preamble |

**Deviations from the TS §4 file list, all in the restrictive direction:**

1. **`.tfw/workflows/plan.md` — listed MODIFY, not touched.** It carries no occurrence of either retired form. Touching it would have been an unasked change.
2. **`.tfw/adapters/codex/skills/tfw-review/SKILL.md` and `.agents/skills/tfw-review/SKILL.md` — listed MODIFY, not touched.** AC-3 conditions the edit on a statement being false; none is.
3. **`README.md` — modified, deliberately not staged** (§2 D8).

## 4. Verification

| Check | Command | Result |
|---|---|---|
| Tests | `python -m pytest docs/scripts/` | **68 passed** in 55.82s. Pre-phase baseline captured at ONB time: 68 passed in 55.99s — same count, no new failures |
| Adapter parity | `config.md` § Drift check, verbatim | **No output**, exit 0 (was 14 lines) |
| Byte parity | `diff` per adapter pair, 22 pairs | 0 diff-lines on every pair |
| Codex router parity | `diff` source vs installed, `tfw-plan` and `tfw-review` | Byte-identical after the edit |
| Word budgets | `wc -w` | `plan.md` 1,195 · `review.md` 1,176 — both unchanged, both under 1,200 |
| Scope budget ⟳ | `git diff --name-status ce30f3b^ ce30f3b` + working tree | **28 modified product files of 30**; 0 new product; 6 trace files, unbudgeted. Rule quoted in §1. The first pass reported *"28 modified, 5 new, against 30 / 15"* and computed no total — the defect the reviewer caught |
| AC-7 ledger ⟳ | `git diff -U0 ce30f3b^ ce30f3b -- <six ledger files>` | **16** hunk headers; 14 at default context. 10 substitution hunks / 11 substituted lines · 4 debt fixes · 2 additions. The first pass reported 12 and 8 |
| Entry-point links | `grep -rn "PROJECT_CONFIG" CLAUDE.md AGENTS.md` | **No matches** (was 2 in `CLAUDE.md`). Target `.tfw/project_config.yaml` exists |

No lint or build command is configured for markdown in this project; `docs/scripts/` is the only executable gate and it is the one AC-6 names.

## 5. Evidence

> **Cognitive mode:** Observational verification — evidence lives in the EV file, not inline.

See [EV file](evidence/EV__phase-d__glossary_adapters_version.md) for evidence details.

Evidence verdict: **26/26 VERIFIED**, 0 DEFERRED, 0 BLOCKED, 0 N/A — ⟳ **recomputed 2026-08-18, not restored** (AC-12)

| Rows | First pass | Now | Why they moved |
|---|---|---|---|
| E17 (AC-7 ledger) | VERIFIED on a count that does not reproduce | **VERIFIED** on the reproduced count | The artifact changed. The row now names the exact command, its 16-header output and the per-file breakdown. Not the old claim upgraded — the old claim replaced |
| E19 (scope budget) | VERIFIED against sub-limits only | **VERIFIED** against the total, under a quoted rule | The artifact changed. The row now carries the counting rule, the 28-of-30 product total and the trace list |
| E17b, E19b, E20–E24 | — | **VERIFIED** (seven new) | Added for the corrective pass: E17b and E19b record *why* the two replaced rows were wrong; E20–E24 cover AC-8 through AC-12. Row count 19 → 26 |
| E1–E16, E18 | VERIFIED | **VERIFIED**, untouched | The reviewer independently established all seventeen. Nothing was re-run to inflate a count |

**The reviewer's figure of 17 of 19 was correct at REVISE time.** It is superseded by artifacts that changed, not by argument.

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/workflows/plan.md` | Step 2 | duplication | **TD-163's second half, left open on the coordinator's R5 ruling.** Step 2 restates the three Knowledge Gate modes (`hard` stop + justification / `soft` reminder / `off` skip) that `glossary.md` also states — **~50 words**. Removing it is content deletion in Phase B's file, which HL §7.1 forbids this phase. It is the single cheapest cut available to a file at 1,195 of 1,200, and TFW-57 needs exactly this kind of concrete candidate |
| 2 | `docs/scripts/gen_docs.py` | `resolve_references()`, `add_table_anchors()` | missing-test | **Four of the six anchor-link patterns the contract declares are not implemented.** The resolver links `TD-{N}` and `D{N}` only; `P{N}` and `F{N}` get table anchors but no link resolution; `NS{N}` and `PP{N}` get neither. An `NS3` or `P7` reference renders as plain text and the build emits no warning. **Filed as TD-170**, one debt for all four, per the coordinator's ruling on ONB §5.4. Extending the script was explicitly out of scope |
| 3 | `TECH_DEBT.md` | TD-131 | todo | **Second row found by the ordered re-scan.** It points at *"Phase D terminology/consistency pass"* and appears in neither TS list — the same omission as TD-158. Re-routed out and the reasoning recorded in the row: its own text says fixing it *"changes heading depth in every HL"*, so it is a structural change to a shipped template inside Phase A's section, not a naming fix |
| 4 | `TECH_DEBT.md` | TD-133 | todo | **An orphaned row.** It routes to *"Phase C, owns the `NS{n}` / `PP{n}` namespace work"* — a phase that closed on 2026-08-13. Its stated defect (`P{N}` resolving to the removed `KNOWLEDGE.md` §0) **no longer reproduces**: the §2 pattern table now reads *"HL §7 Principles row (task-local)"*. The residual — that `P{N}` has no resolution target — is subsumed by TD-170. Left for reviewer triage rather than closed here, since it is in neither TS list |
| 5 | `CLAUDE.md` | 51, 53 | naming | **⟳ Reported in the first pass, fixed in the second.** Two references to `.tfw/PROJECT_CONFIG.yaml`, a filename D48 retired in April 2026. Broken on any case-sensitive filesystem; Windows masks it. The review routed it to TD-172; the **owner ruled it fixed here** on 2026-08-18, widening AC-4's limit to *"two rows and two link corrections, nothing else"*. Both links now read `.tfw/project_config.yaml`. TD-172 closed |
| 6 | `.tfw/adapters/codex/skills/tfw-{plan,review}/SKILL.md` | Contract bullets | todo | **Neither router mentions the freeze, the amendment channel or the Purpose Check.** No statement is false — both point at the canonical workflow, which carries the rules — so AC-3's *"edit only what is false"* correctly leaves them alone. Recording it because the two routers are the Codex surface's only always-loaded contract, and a reader who never opens `plan.md` learns nothing about the mechanism this release exists to ship |
| 7 | `.tfw/glossary.md` | 268 | style | The PV Index closing note wraps *"Project North Star"* across a line break, so `> North Star.` stands alone on line 268 and any naive `grep "North Star"` reports it as drift forever. Not fixed: rewrapping the line is a formatting change to Phase C's section and buys nothing but a cleaner grep |

| 8 | `.claude/commands/tfw-handoff.md` | Step 11, §5 guidance | environment | **⟳ Re-homed from §8 S4 by AC-10.** This session was invoked from the stale copy it was sent to repair: `/tfw-handoff` loaded the adapter file, which still instructed an inline RF §5 evidence table and permitted skipping evidence collection when no AC carries an `Evidence:` field. The canonical `.tfw/workflows/handoff.md` requires a structured EV file and allows no skip. I followed the canonical file. It is TD-157's failure mode observed live on a **second** workflow and by a **second** role — and it is why adapter drift is not a tidiness problem: it silently changes what an agent is instructed to produce. Closed by this phase's sync |
| 9 | `.tfw/workflows/config.md` | § Drift check | naming | **⟳ Re-homed from §8 S2 by AC-10, operative half only.** A terminology gate written as a raw substring `grep` cannot distinguish a concept from its denial: the sweep for `committed baseline` matched inside `uncommitted baseline`, which names the *absence* of the thing. A mechanical pass would have substituted it into nonsense. The fix is not a smarter regex but a ruled exclusion recorded in the spec, which is what AC-2's amended table now carries. Worth keeping because it is why the AC-2 gate had to be re-read at ONB before it could be run |
| 10 | `.tfw/workflows/config.md` | § Drift check | environment | **⟳ Re-homed from §7 FC5 by AC-10.** The drift check is a `bash` snippet and must be run in a POSIX shell. This project's primary shell on Windows is PowerShell, where the snippet is a parse error; it was run in Git Bash. Any executor on a Windows workstation hits this before the check produces its first line |
| 11 | repository-wide | — | naming | **AC-11's sweep for the retired `PROJECT_CONFIG.yaml` filename, outside `CLAUDE.md`: nothing live.** Every remaining occurrence is either history that must not be rewritten — `.tfw/CHANGELOG.md` recording the rename itself, `KNOWLEDGE.md` D16/D20/D22/D48 and its Legacy row, `knowledge/philosophy.md` F23, two `README.md` task titles — or the rule stating the retirement (`conventions.md`:468, *"not `PROJECT_CONFIG.yaml`"*). 136 files under `tasks/` carry it as sealed trace. `.tfw/workflows/init.md` is clean, although TD-102's row still quotes it as if it were not. **Reported, not fixed**, exactly as AC-11 directs |

**On AC-2's third-synonym-pair clause:** none found. Checked while sweeping — `goal check` 0, `goal defence` 0, `purpose check` 12 (one form), `amendment log` 6 (one form), `freeze commit` 2 (one form). The three hyphenated `north-star` uses (`conventions.md`:106, :113, `REVIEW.md`:54) are adjectival — *"a north-star clause"* — which is ordinary English, not a second defined term.

## 7. Fact Candidates
> fact-candidates: processed 2026-08-18 (`/tfw-knowledge`, TFW-53 A–E)


> ⟳ **Corrected 2026-08-18 (AC-10).** The first pass carried five. Four failed the template's Human-Only
> Test — *"would this fact be unknown without the human saying it?"* — and the reviewer was right to fail
> them. **FC1, FC2 and FC4 are dropped:** each restates a coordinator ruling that the ONB and the TS
> already carry, and re-recording a decision away from where it was made is duplication, not knowledge.
> **FC5 is not dropped but re-homed** to §6 observation 10 — it is an environment fact an agent discovers
> by running the command, which is a §6 item, not a fact candidate.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | stakeholder | The owner ruled on 2026-08-13 that **all fourteen** drifted adapter copies be re-synced, not only the six this task caused — because a binary check that keeps printing eight failures after the phase whose deliverable is adapter parity **stops being read**. The reasoning generalises past adapters: it is a rule about when a passing-with-known-failures signal loses its value | Owner decision 2026-08-13, recorded in TS AC-3; reasoning extends D53 | High |

*(Numbered FC3 in the first pass; retained on the reviewer's own recommendation. It is the one entry no
agent could have derived from the repository — the owner's reasoning existed only in the instruction.)*

## 8. Strategic Insights (Execution)

No strategic insights.

> ⟳ **Corrected 2026-08-18 (AC-10).** The first pass carried four entries; all four were agent analysis,
> and the template is unambiguous here — *"Only when the human provides domain knowledge… If no human
> interaction occurred — write `No strategic insights.`"* **No human domain knowledge entered during
> execution:** the owner's input reached this phase at TS approval, before it began, and every answer
> received mid-flight came from the coordinator, which is an agent.
>
> Nothing was deleted — three of the four were re-homed and the RF says where: **S3** → §2 D11 (it
> describes a change that was made), **S4** → §6 observation 8, **S2's operative half** → §6
> observation 9. **S1 is dropped**: it was commentary on this TS's measurement quality, already recorded
> in the ONB and in the coordinator's own commit.
>
> The section's admission rule and §7's are not equally clear, and the difference matters: §8's test is
> unambiguous and I misapplied it, while §7's Scope line and its Human-Only Test contradict each other
> outright. That contradiction is filed as **TD-174**, with the measurement that shows it has been live
> for four consecutive approved reviews.

## 9. Diagrams

**What Phase D changed, by kind of change.**

```
                            .tfw/  (canonical)
                              │
  ┌───────────────────────────┼───────────────────────────────┐
  │ ADD                       │ SUBSTITUTE                    │ FIX (named debt)
  │                           │                               │
  glossary.md                 conventions.md      :94 :108    templates/HL.md      :10  TD-164
   ├─ ## Contract and         glossary.md         PV Index     compilable_contract  :81  TD-165
   │  Purpose Defence  [new]  templates/HL.md     :18 :20 :22  compilable_contract  :65  TD-167
   │   ├─ HL Contract         review/judge.md     :34 :35 :84  glossary.md    Knowledge
   │   ├─ Contract Baseline   workflows/review.md :28 :87        Gate step pointer   TD-163
   │   ├─ Frozen Section
   │   ├─ Amendment          frozen baseline    8 → 0
   │   ├─ Amendment Log      committed frozen   1 → 0
   │   ├─ Project North Star bare North Star    2 → 0
   │   ├─ Purpose Check
   │   ├─ not fit for purpose         plan.md   1195 → 1195  ── no hunk at all
   │   └─ Deferral confession         review.md 1176 → 1176  ── word-neutral
   └─ ## Knowledge Terms
       └─ Result Visualization  [new, between Value Flow and Findings Map]
```

**The sync, and the check that made it safe.**

```
  step 1  DIRECTION CHECK — before any copy, all 14 pairs
          ┌──────────────────────────────────────────────────┐
          │  for each pair: source-only lines vs copy-only    │
          │  read every copy-only line                        │
          │                                                   │
          │  result: every copy-only line is an OLDER form    │
          │          of a source-only line in the same hunk   │
          │  → no copy holds content its source lacks         │
          │  → AC-3 stop condition does NOT fire              │
          └──────────────────────────────────────────────────┘
                                │
  step 2  DRIFT CHECK — before                14 DRIFT lines, exit 0
                                │             ├─ ours (6): plan ×2, review ×2, research ×2
                                │             └─ earlier tasks (8): init ×2, handoff ×2,
                                │                                   update ×2, knowledge ×2
                                ▼
  step 3  cp  .tfw/workflows/{7}.md ──┬──► .claude/commands/tfw-{7}.md
                                      └──► .agent/workflows/tfw-{7}.md
                                │
  step 4  DRIFT CHECK — after         (silent), exit 0
                                │     diff per pair, 22 pairs → 0 lines each
                                ▼
          Codex routers: NOT copies — read, not cp
            tfw-review  → no false statement          → unchanged
            tfw-plan    → "revises APPROVED HL/TS"     → one word removed
                          (granted what §3 rule 3 forbids)
```

**Release surface after v1.2.0.**

```
  VERSION            1.1.0 ──► 1.2.0   ┐
  project_config     1.1.0 ──► 1.2.0   ┘ lockstep, unbroken since 0.8.5

  CHANGELOG  ## [Unreleased]  ── "Nothing pending."
             ## [1.2.0] — 2026-08-14   one entry, Phases A–D
                ├─ why it exists ──► TFW-54  (the pointer DoD-33 requires;
                │                             was 0 occurrences in .tfw/)
                ├─ Added    HL Contract · §12 Amendment Log · Purpose Check
                │           · PV priority 0 · ten glossary articles · §14 anti-patterns
                ├─ Changed  plan.md 6c inverted · research/base.md · Reviewer Identity
                │           · review.md:28 · REJECT branch (a) · Phase HL derivation-only
                │           · §3.1 mandatory · one name per concept
                │           · scope budgets  ⟵ folded from [Unreleased]
                │           · adapter sync    ⟵ folded, "12 … not yet repaired" → 14, repaired
                ├─ Removed  Judge mapping-integrity check · RES.md:32
                │           · inline recovery command · KNOWLEDGE.md §0 pointer
                └─ Fixed    TD-165 · TD-163 · TD-157 (+ six further workflows)
```

**⟳ The AC-7 ledger, reconciled (AC-9).** The first pass reported *twelve hunks, eight substitutions*.
Both numbers were wrong. Command, output and classification, so a reader can reproduce it:

```
  $ git diff -U0 ce30f3b^ ce30f3b -- <the six ledger files> | grep -c '^@@'
    16                          ← default context (-U3) merges adjacent hunks and gives 14

  file                        hunks   what each hunk is
  ─────────────────────────── ─────   ────────────────────────────────────────────────
  conventions.md                  2   @@ -94   substitution
                                      @@ -108  substitution
  glossary.md                     4   @@ -41,0 +42,29   ADDITION  ## Contract and Purpose Defence
                                      @@ -52,0 +82,3    ADDITION  ### Result Visualization
                                      @@ -213/+245      DEBT FIX  TD-163
                                      @@ -225/+257      substitution
  templates/HL.md                 4   @@ -10   DEBT FIX  TD-164
                                      @@ -18   substitution   ┐ field label
                                      @@ -20   substitution   ┘ + explainer
                                      @@ -22   substitution
  templates/review/judge.md       2   @@ -34,2 +34,2      substitution ×2 LINES in ONE hunk
                                      @@ -84             substitution
  workflows/review.md             2   @@ -28   substitution
                                      @@ -87   substitution
  compilable_contract.md          2   @@ -67   DEBT FIX  TD-167
                                      @@ -81   DEBT FIX  TD-165
  ─────────────────────────── ─────
  TOTAL                          16

  classification            hunks   lines
  ───────────────────────── ─────   ─────
  canonical substitution       10      11   ← judge.md @@ -34,2 carries two
  named debt fix                4       4
  addition site                 2       —
  ───────────────────────── ─────   ─────
                               16

  git diff --stat  (what AC-7 literally asked for)
    6 files changed, 47 insertions(+), 15 deletions(-)
```

**Where 12 came from.** The ledger table names six files — the five substitution and debt-fix targets
**plus `glossary.md`**. The command actually run listed `plan.md` (0 hunks) and **omitted `glossary.md`**
(4 hunks): `16 − 4 + 0 = 12`. A number produced by one file set, reported against another.

```
  claimed set   conventions · judge · review · plan · HL · compilable_contract   → 12  ✗ reported
  ledger set    conventions · judge · review · glossary · HL · compilable_c.     → 16  ✓ correct
                                               ▲▲▲▲▲▲▲▲
                                               the four missing hunks
```

**What did not change:** every hunk still classifies as a substitution, a named debt fix or an addition,
and the reviewer confirmed that independently at 100% file coverage. AC-7's *claim* holds; only its
*count* was false — which in a phase about making rules findable is not a small thing. It is the same
defect class as Phase C's truncated citation: a figure in an evidence file that a reader cannot reproduce.

---

*RF — TFW-53 / Phase D: Glossary, Adapters and Version | 2026-08-14*
