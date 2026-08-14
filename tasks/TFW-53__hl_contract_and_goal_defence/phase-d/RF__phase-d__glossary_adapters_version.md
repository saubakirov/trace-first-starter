# RF — TFW-53 / Phase D: Glossary, Adapters and Version

> **Date**: 2026-08-14
> **Author**: Executor (Claude Code)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-53](../HL-TFW-53__hl_contract_and_goal_defence.md) — 🔒 FROZEN
> **TS**: [TS Phase D](TS__phase-d__glossary_adapters_version.md) — approved 2026-08-13, amended 2026-08-14 after ONB
> **ONB**: [ONB Phase D](ONB__phase-d__glossary_adapters_version.md) — Q1 → (a), Q2 → (a), Q3 → (a); R1-R5 approved, R6 overruled
> **Covers**: frozen DoD 30–33
> **Ships**: TFW **v1.2.0**

---

## 1. What Was Done

### New Files

| File | Description |
|------|------------|
| `phase-d/evidence/EV__phase-d__glossary_adapters_version.md` | Structured evidence — 19 rows, all VERIFIED |
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

## 3. Acceptance Criteria

| AC | Gate | Result |
|----|------|--------|
| **AC-1** — vocabulary defined | `grep -ci` each term ≥ 1; `wc -w` per article | ✅ 10/10 terms ≥ 1 (lowest is 1, highest 5). All ten articles 41–50 words against the p75 = 50 ceiling. Each ends with a `→` pointer; every pointer target opened and confirmed |
| **AC-2** — one name per concept | `grep -rn` each retired form → 0; `wc -w` both workflows | ✅ `frozen baseline` **8 → 0**. `committed baseline` excluding the negation **0 → 0**. Bare `North Star` **2 → 0** (one line-wrap artefact remains and is recorded). `plan.md` 1,195 → **1,195**, `review.md` 1,176 → **1,176** |
| **AC-3** — adapter parity | drift check → no output; `diff` per copy → empty | ✅ 14 `DRIFT:` lines → **silent**, exit 0. All 22 pairs diff to 0 lines. Direction verified per pair before copying. The six/eight split is stated in §2 D5. Codex routers checked; one false statement found and fixed |
| **AC-4** — entry points | read both tables against the shipped workflows | ✅ Both `CLAUDE.md` cells rewritten and read back against `plan.md` Steps 4/6c/6d and `review.md` Step 3. Two rows added under the recorded extension. `AGENTS.md` unchanged — nothing false. No new section in either file |
| **AC-5** — release shippable | `cat VERSION`; `grep -c` config; `grep -c TFW-54` | ✅ `1.2.0` · `1` · `1`. One `[1.2.0]` entry, five blocks, Phases A–D. `[Unreleased]` folded and corrected |
| **AC-6** — five debts, TD-164 first | open each line; `pytest docs/scripts/` | ✅ TD-164 closed first, by replacement not rewording. TD-163 (glossary half), TD-165, TD-167 closed; TD-157 closed by AC-3. Each records the reason. **68 passed**, unchanged from the pre-phase baseline |
| **AC-7** — no unasked content change | `git diff` reviewed hunk by hunk | ✅ Twelve hunks across six files: eight substitutions, four debt fixes, plus pure additions in `glossary.md`. **No hunk is a rewritten sentence.** No section added anywhere; no template gained a field. Diffstat with per-file justification in §1 |

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
| Scope budget | `git status --short` | **28 modified**, 5 new files in one new folder, against 30 / 15. Fourteen of the 28 are `cp` with zero authored content |

No lint or build command is configured for markdown in this project; `docs/scripts/` is the only executable gate and it is the one AC-6 names.

## 5. Evidence

> **Cognitive mode:** Observational verification — evidence lives in the EV file, not inline.

See [EV file](evidence/EV__phase-d__glossary_adapters_version.md) for evidence details.

Evidence verdict: 19/19 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/workflows/plan.md` | Step 2 | duplication | **TD-163's second half, left open on the coordinator's R5 ruling.** Step 2 restates the three Knowledge Gate modes (`hard` stop + justification / `soft` reminder / `off` skip) that `glossary.md` also states — **~50 words**. Removing it is content deletion in Phase B's file, which HL §7.1 forbids this phase. It is the single cheapest cut available to a file at 1,195 of 1,200, and TFW-57 needs exactly this kind of concrete candidate |
| 2 | `docs/scripts/gen_docs.py` | `resolve_references()`, `add_table_anchors()` | missing-test | **Four of the six anchor-link patterns the contract declares are not implemented.** The resolver links `TD-{N}` and `D{N}` only; `P{N}` and `F{N}` get table anchors but no link resolution; `NS{N}` and `PP{N}` get neither. An `NS3` or `P7` reference renders as plain text and the build emits no warning. **Filed as TD-170**, one debt for all four, per the coordinator's ruling on ONB §5.4. Extending the script was explicitly out of scope |
| 3 | `TECH_DEBT.md` | TD-131 | todo | **Second row found by the ordered re-scan.** It points at *"Phase D terminology/consistency pass"* and appears in neither TS list — the same omission as TD-158. Re-routed out and the reasoning recorded in the row: its own text says fixing it *"changes heading depth in every HL"*, so it is a structural change to a shipped template inside Phase A's section, not a naming fix |
| 4 | `TECH_DEBT.md` | TD-133 | todo | **An orphaned row.** It routes to *"Phase C, owns the `NS{n}` / `PP{n}` namespace work"* — a phase that closed on 2026-08-13. Its stated defect (`P{N}` resolving to the removed `KNOWLEDGE.md` §0) **no longer reproduces**: the §2 pattern table now reads *"HL §7 Principles row (task-local)"*. The residual — that `P{N}` has no resolution target — is subsumed by TD-170. Left for reviewer triage rather than closed here, since it is in neither TS list |
| 5 | `CLAUDE.md` | 49, 51 | naming | **Two references to `.tfw/PROJECT_CONFIG.yaml`**, a filename D48 retired in April 2026 in favour of `project_config.yaml`. Both are broken pointers in the entry point a Claude session actually reads. AC-4 scopes this phase to two purpose cells plus the two-row extension, so it was not fixed — but it is the same class of defect the R6 extension was granted for |
| 6 | `.tfw/adapters/codex/skills/tfw-{plan,review}/SKILL.md` | Contract bullets | todo | **Neither router mentions the freeze, the amendment channel or the Purpose Check.** No statement is false — both point at the canonical workflow, which carries the rules — so AC-3's *"edit only what is false"* correctly leaves them alone. Recording it because the two routers are the Codex surface's only always-loaded contract, and a reader who never opens `plan.md` learns nothing about the mechanism this release exists to ship |
| 7 | `.tfw/glossary.md` | 268 | style | The PV Index closing note wraps *"Project North Star"* across a line break, so `> North Star.` stands alone on line 268 and any naive `grep "North Star"` reports it as drift forever. Not fixed: rewrapping the line is a formatting change to Phase C's section and buys nothing but a cleaner grep |

**On AC-2's third-synonym-pair clause:** none found. Checked while sweeping — `goal check` 0, `goal defence` 0, `purpose check` 12 (one form), `amendment log` 6 (one form), `freeze commit` 2 (one form). The three hyphenated `north-star` uses (`conventions.md`:106, :113, `REVIEW.md`:54) are adjectival — *"a north-star clause"* — which is ordinary English, not a second defined term.

## 7. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | process | The coordinator ruled that a re-route list built from one review's rows is not a re-route list, and ordered a full registry re-scan as part of the ONB answer. The re-scan found a second omission (TD-131) that the review-derived list had missed | Coordinator, ONB Q3 answer, 2026-08-14 | High |
| 2 | process | Two consecutive phases have had their TS arithmetic corrected at ONB time — Phase B caught AC-6's budget, Phase D corrected six measurements. The coordinator recorded this as a pattern rather than fixing the numbers quietly, on the ground that a TS whose figures need re-deriving is spending an execution stage on planning work | Coordinator, ONB response preamble, 2026-08-14 | High |
| 3 | stakeholder | The owner ruled on 2026-08-13 that all fourteen drifted adapter copies be re-synced, not only the six this task caused, because a binary check that keeps printing eight failures after the phase whose deliverable is adapter parity stops being read | TS AC-3, owner decision 2026-08-13; D53 | High |
| 4 | convention | A coordinator scope extension is recorded in the TS with its limit stated (*"two rows, no other change to `CLAUDE.md`"*), not inferred or absorbed into an existing AC. The coordinator overruled the executor's report-not-fix recommendation and named the extension explicitly as its own | Coordinator, ONB R6 answer, 2026-08-14 | High |
| 5 | environment | The `config.md` drift check is written as a `bash` snippet and must be run in a POSIX shell. On this Windows workstation that means Git Bash — the project's primary shell is PowerShell, where the snippet is a parse error | Executor, running the check verbatim | Medium |

## 8. Strategic Insights (Execution)

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | **A gate is only as honest as its measurement, and a measured gate can be unsatisfiable.** Three of AC-2's figures survived planning, an owner approval and a coordinator's own re-read before the ONB showed the `committed baseline` gate could only reach zero by rewriting a sentence the same TS forbids. **Implication:** the ONB's re-measurement step is not verification theatre — it is the only place in the pipeline where a gate's *arithmetic* is checked against the repository, and this is the second consecutive phase it has caught something. The framework's own `Evidence sufficiency` row (D61, 16.1% firing rate) asks whether evidence *proves what it is offered to prove*; the same question asked of a TS gate before execution is what this ONB did | philosophy | Coordinator ONB answers Q1–Q3, 2026-08-14 |
| S2 | **The negation is not the term.** `uncommitted baseline` matched a synonym sweep as a substring and would have been "normalised" into nonsense by any mechanical pass. **Implication:** a terminology gate expressed as a raw substring `grep` is structurally unable to distinguish a concept from its denial, and the fix is not a smarter regex but a human-ruled exclusion recorded in the spec — which is what the coordinator did by amending AC-2's table to two names rather than three | convention | ONB Q1 ruling, 2026-08-14 |
| S3 | **The false permission was one word, in a field nobody reads as prose.** The Codex `tfw-plan` router's `description` said the command *"creates or revises approved HL/TS artifacts"* — written before the contract existed, true then, and granting exactly what `conventions.md` §3 rule 3 now forbids. **Implication:** adapter parity checked as *byte equality* would never have caught this, because the routers are deliberately not copies. The only thing that catches a thin router going stale is a human reading it against the mechanism, which is why AC-3 spells that out as a separate bullet from the `cp` | philosophy | Executor, AC-3 router check |
| S4 | **This session was invoked from the stale copy it was sent to repair.** `/tfw-handoff` loaded `.claude/commands/tfw-handoff.md`, which still instructed an inline RF §5 table and permitted skipping evidence collection; the canonical `handoff.md` requires a structured EV file and no skip. **Implication:** the owner's all-fourteen decision was argued from D53 (*optional never happens*) and was already right; what arrived by accident is a live demonstration on a **second** workflow and by a **second** role, which is stronger evidence than the argument it was made on. Adapter drift is not a tidiness problem — it silently changes what an agent is instructed to produce | risk | Executor, observed at Step 0 of this session; coordinator ONB §5.2 ruling |

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

---

*RF — TFW-53 / Phase D: Glossary, Adapters and Version | 2026-08-14*
