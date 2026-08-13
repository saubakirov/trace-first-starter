# EV — TFW-56: Remove the Review Mode Axis

> **Date**: 2026-08-13
> **Author**: Executor (Claude Code)
> **Task**: TFW-56
> **TS**: [TS TFW-56](../TS__TFW-56__review_mode_removal.md)

---

## Environment

| Field | Value |
|-------|-------|
| OS | Windows 11 Pro 10.0.26200 |
| Language / Runtime | Python 3.13.5 |
| Shells | Git Bash (MSYS2), git 2.42.0.windows.1 |
| Build | `python -m pytest docs/scripts/` (68 tests) — the docs pipeline is the only build that consumes the changed files |
| CI / Pipeline | `.github/workflows/docs.yml` — run locally here |

> `project_config.yaml` `build.lint/test/verify` are unconfigured starter placeholders
> (`echo "configure your … command"`). `conventions.md`, `glossary.md`, `.tfw/workflows/**` and
> `.tfw/templates/**` are Source Manifest rows 4, 5, 12 and 13, so the docs build is the substitution
> — the same substitution used and approved in EV TFW-53/A.

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | The mode-file folder is gone and `review.md`'s steps are contiguous with Step 0 = Session Naming | Git Bash | **VERIFIED** | §E1 — `ls` fails; 8 headings, 0-7, no gaps |
| E2 | AC-2 | Judge checklist is exactly ten universal rows, no `Mode:` field, no Mode-Specific section | Git Bash | **VERIFIED** | §E2 — row count 10, `grep -c "Mode"` → 0 |
| E3 | AC-2 | **S1-vs-U7 dry-run** against an archived RF/EV/REVIEW triple — do rows 7 and 8 produce different answers? | Reading, against TFW-53 Phase A | **VERIFIED** | §E3 — row 7 ✅, row 8 ❌ with three findings. Different answers, different reasoning |
| E4 | AC-3 | Eight mode checklist rows each accounted for | Reading | N/A | TS Evidence field: `N/A — this is a documentation-completeness check, verifiable by reading.` Table in RF §3 / §2 |
| E5 | AC-4 | Eight distinct verify actions each accounted for; `map.md` and `verify.md` carry no `Mode:` | Reading + grep | N/A | TS Evidence field: `N/A — file content, verifiable by reading.` Table in RF §2; grep result in §E6 below |
| E6 | AC-5 | `REVIEW.md` §3 matches `judge.md` row-for-row, same order; no header field, no placeholder | Reading | N/A | TS Evidence field: `N/A — template content.` §E4 carries the row-list diff |
| E7 | AC-6 | `default_mode` absent from both config files; `min_verify_ratio: 0.42` and its comment intact | Git Bash | **VERIFIED** | §E5 — both file excerpts, before and after |
| E8 | AC-7 | `config.md` no longer routes `review.default_mode`; the `min_verify_ratio` row names the correct step | Git Bash | N/A | TS Evidence field: `N/A — cross-reference check.` Resolution recorded in §E6 |
| E9 | AC-8 | No mode vocabulary in `conventions.md` / `glossary.md`; anti-pattern present | Git Bash | N/A | TS Evidence field: `N/A — text content.` `grep -rn "review mode" .tfw/` → 0, recorded in §E6 |
| E10 | AC-9 | Six adapter and entry-point copies carry no mode reference and match their sources | Git Bash | **VERIFIED** | §E6 — grep → 0 matches across all six; five `diff` runs, all empty |
| E11 | AC-10 | `VERSION` bumped; CHANGELOG `### Removed` names the key | Git Bash | N/A | TS Evidence field: `N/A — changelog content.` `1.1.0`; key named at CHANGELOG L21 |
| E12 | AC-11 | TD-106 closed with the reason | Reading | N/A | TS Evidence field: `N/A` |
| E13 | AC-12 | The grep gate, run verbatim, with its output | Git Bash | **VERIFIED** | §E7 — zero matches, exit 1. Plus a supplementary sweep, because one quarter of the mandated pattern is dead |
| E14 | AC-12 | History intact: no existing task REVIEW file modified, no past CHANGELOG entry edited | Git Bash | **VERIFIED** | §E8 — 41 files under `tasks/` still carry `Review Mode`; nothing under `tasks/` in the diff except this task's own artifacts |
| E15 | AC-12 | Diffstat: 3 deletions, no framework file created | Git Bash | **VERIFIED — with an anomaly that must be read** | §E9 — the substance holds; the three deletions were **swept into a concurrent session's commit**, so they do not appear in this task's own diffstat |
| E16 | Build gate | Docs pipeline tests, since the changed files are Source Manifest rows | Python 3.13.5 | **VERIFIED** | §E10 — 68 passed |

## Verdict

Evidence verdict: **9/16 VERIFIED, 0 DEFERRED, 0 BLOCKED, 7 N/A**

The 7 N/A are the TS's own `Evidence:` fields, quoted verbatim above — not executor judgement.
E15 is VERIFIED on substance with a trace anomaly recorded in full; it is not marked N/A or
DEFERRED, because the fact being evidenced is true and checkable — it is the *attribution* of the
change that is wrong, and hiding that behind a softer status would be the failure this layer exists
to prevent.

---

## E1 — The selection is absent (AC-1)

```
$ ls .tfw/workflows/review/
ls: cannot access '.tfw/workflows/review/': No such file or directory

$ grep -n "^## Step" .tfw/workflows/review.md
16:## Step 0: Name This Session
52:## Step 1: Map
60:## Step 2: Verify
78:## Step 3: Judge
89:## Step 4: Decide (Synthesize → REVIEW)
100:## Step 5: Tech Debt Collection
109:## Step 6: Update Traces
116:## Step 7: Knowledge Capture (KNW)
```

Contiguous 0-7, and **Step 0 is Session Naming** — the TFW-standard opening this file has never had
(`knowledge/process.md` F19, TD-106).

The only surviving occurrence of "mode" or "WAIT" in the whole file:

```
$ grep -ni "mode\|WAIT" .tfw/workflows/review.md
7:> **Role:** Reviewer (coordinator in review-locked mode)
```

"review-locked mode" is the Role Lock, not a genre. It is invisible to the AC-8 gate
(`grep -rn "review mode"`) because the words are not adjacent, and it means one thing.

**Internal step references, read end to end.** Three references pointed at step numbers. All three
were **wrong before this task** and are correct after it, with no edit:

| Reference | Says | Verify was | Verify is | Before | After |
|---|---|---|---|---|---|
| `review.md` L143 anti-pattern | "Step 2 (Verify)" | Step 3 | **Step 2** | ❌ stale | ✅ |
| `conventions.md` L495 anti-pattern | "Step 2 (Verify)" | Step 3 | **Step 2** | ❌ stale | ✅ |
| `config.md` L92 propagation row | "Step 2: Verify" | Step 3 | **Step 2** | ❌ stale | ✅ |

One reference needed an actual edit, and it pointed at Judge rather than Verify:

| Reference | Was | Now | Why |
|---|---|---|---|
| `glossary.md` Principles Check | "`review.md` Step 4" | "`review.md` Step 3" | Judge moved 4 → 3 |

`glossary.md` L157 (Session Naming → `review.md` Step 0) needed nothing and becomes true for the
first time.

## E2 — Ten universal rows (AC-2)

```
$ grep -c "^| [0-9]* |" .tfw/templates/review/judge.md
10

$ grep -c "Mode" .tfw/templates/review/judge.md
0
```

| # | Row | Rate carried in the row |
|---|-----|------------------------|
| 1 | DoD met? | — |
| 2 | Philosophy aligned — (a) mapping integrity · **(b) design soundness** | **4.5%** on (b) |
| 3 | Tech debt documented | — |
| 4 | Style & standards | — |
| 5 | Observations collected | — |
| 6 | RF completeness (§7-9) | — |
| 7 | Evidence completeness — does the evidence **exist**? | — |
| 8 | **Evidence sufficiency** — does the evidence **establish the claim**? | **16.1%** |
| 9 | **Backward compatibility** | **8.5%** |
| 10 | **Safety** — kept on consequence, not on rate | **4.0%** |

Order is HL §3.1's frozen after-diagram. *Content quality* is absent — the one true duplicate of
row 4.

**Explicit-N/A is structural, not advisory.** Status vocabulary on every row is `✅/❌/⚪`; the
section header states that `⚪ N/A` requires a stated reason and that a row skipped as a bare `✅`
leaves the stage incomplete; and the Checkpoint carries `- [ ] Every ⚪ N/A carries a stated reason —
no row skipped as a bare ✅?`. Three sites, so deleting any one leaves the rule visible.

## E3 — The S1-vs-U7 dry-run (AC-2)

> **Subject:** TFW-53 Phase A — [RF](../../TFW-53__hl_contract_and_goal_defence/phase-a/RF__phase-a__contract_in_artifacts.md) ·
> [EV](../../TFW-53__hl_contract_and_goal_defence/phase-a/evidence/EV__phase-a__contract_in_artifacts.md) ·
> [REVIEW](../../TFW-53__hl_contract_and_goal_defence/phase-a/REVIEW__phase-a__contract_in_artifacts.md) (✅ APPROVE, three passes, `Review Mode: spec`).
>
> Chosen because it is this repository's most recent completed review, it has a real 15-row EV file
> with resolving attachments, and it was scored under an owner mode override — so it is the hardest
> available test of whether the new row adds anything the old checklist missed.
>
> **This is a dry-run of a checklist, not a re-review.** I am TFW-56's executor, not TFW-53's
> reviewer. Nothing here revises TFW-53/A's APPROVE verdict, and a row-8 ❌ in a dry-run is not a
> claim that the verdict should have been REVISE — that verdict rested on the whole picture, and
> row 8 did not exist when it was made.

**Row 7 — Evidence completeness. Does the evidence exist? → ✅**

All 15 TS ACs appear in the EV table. Only the 4-status vocabulary is used (7 VERIFIED, 0 DEFERRED,
0 BLOCKED, 8 N/A). Both attachments resolve — `baseline_recovery.txt` and
`classification_exercise.md` are present in `phase-a/evidence/`. The 8 N/A quote the TS's own
`Evidence:` fields verbatim rather than asserting executor judgement. Same answer the archived
review reached on its row 7.

**Row 8 — Evidence sufficiency. Does the evidence establish the claim? → ❌, three findings**

| # | The green signal | What it does not establish |
|---|------------------|---------------------------|
| 1 | **E2 marked VERIFIED**, concluding *"the amended template can carry HL-TFW-53's own §12 unchanged"* | E2's own table records `Type` = `RESTRICT` as *"not exercised by this corpus… recorded as a coverage gap"*. One of the shipped enum's values has **zero live coverage**. The exhibit establishes the narrow claim; the verdict line `7/15 VERIFIED` reads as the broad one |
| 2 | **E13 marked VERIFIED**, shipping an anchored `--grep` recovery form | Its conclusion was **superseded inside the same pass** by E15: *"no `--grep` form can be subject-only"*. The measurements stand; the conclusion does not. A VERIFIED exhibit whose conclusion has been retracted is the exact shape row 8 exists to catch |
| 3 | **E11 scored 4/4 — pass** | The exhibit states the earlier *budget and cut-order* property is *"absent from both the rule and this check"* — removed by amendment A12 and deliberately not implemented. 4/4 is against a rule with a property removed, and the score does not carry that |

**Result: rows 7 and 8 produced different answers, from different reasoning. AC-2 is met.**

Two properties of this outcome matter more than the ❌ itself:

1. **Row 8's findings are not absences, so row 7 structurally cannot see them.** Every one is a
   *present, VERIFIED* artifact whose stated scope is narrower than the claim it is offered for. Row 7
   asks whether the row is filled; all three rows were filled, correctly, in the 4-status vocabulary.
2. **All three findings were written by TFW-53/A's own executor**, inside the EV file, and none is
   surfaced by its verdict line. That is the case for the row: the honesty was already in the trace,
   and no checklist row was asking the question that would promote it into the verdict. Under the old
   checklist this was reachable only through `spec` mode — and TFW-53/A *was* reviewed as `spec`,
   scored both mode rows ✅, and did not surface them.

## E4 — REVIEW.md §3 against judge.md (AC-5)

Row lists compared in order. `REVIEW.md` §3 carries condensed labels by design — it is a synthesis
document, not a second copy of the stage file — so the check is one-for-one on identity and order:

| # | `judge.md` | `REVIEW.md` §3 | Match |
|---|-----------|---------------|-------|
| 1 | DoD met? | DoD met? (all TS acceptance criteria) | ✅ |
| 2 | Philosophy aligned — mapping integrity + design soundness | Philosophy aligned — mapping integrity + design soundness | ✅ |
| 3 | Tech debt documented | Tech debt documented | ✅ |
| 4 | Style & standards | Style & standards | ✅ |
| 5 | Observations collected | Observations collected | ✅ |
| 6 | RF completeness (§7-9) | RF completeness (§7-9 present) | ✅ |
| 7 | Evidence completeness — does it exist? | Evidence completeness — does it exist? | ✅ |
| 8 | Evidence sufficiency — does it establish the claim? | Evidence sufficiency — does it establish the claim? | ✅ |
| 9 | Backward compatibility | Backward compatibility | ✅ |
| 10 | Safety | Safety | ✅ |

10/10, same order. The `<!-- Add mode-specific checklist items from mode file below -->` comment and
the `> **Review Mode**:` header field are both gone.

**Repaired in passing:** `REVIEW.md` §3 had **6** rows against `judge.md`'s **7** — the Evidence
completeness row added in 0.8.8 never reached it. Closing that gap is required by AC-5 and is not
scope creep; it is recorded in RF §2 as a decision.

## E5 — The config key, and its sibling (AC-6)

**Before** — `.tfw/project_config.yaml`:

```yaml
  review:
    default_mode: code        # code / docs / spec — determines review checklist
    min_verify_ratio: 0.42    # minimum fraction of changed files to verify (escalate to 1.0 on discrepancy)
```

**After** — `grep -n "review:" -A4 .tfw/project_config.yaml`:

```
59:  review:
60-    min_verify_ratio: 0.42    # minimum fraction of changed files to verify (escalate to 1.0 on discrepancy)
```

**After** — `grep -n "review:" -A4 .tfw/templates/project_config.yaml`:

```
63:  review:                             # ← FRAMEWORK: updated by tfw-update
64-    min_verify_ratio: 0.42
```

`min_verify_ratio` keeps its value, its inline comment byte-for-byte, and its `# ← FRAMEWORK`
annotation in the template. Its behavioural home — `review.md` Step 2's parameter table with
`Default 0.42 | Hard | min_verify_ratio` and the `⌈5 × 0.42⌉ = 3` worked example — is unchanged. This
is the one place where collateral damage would have been silent, which is why AC-6 asked for both
excerpts rather than an assertion.

## E6 — Propagation, vocabulary and adapter parity (AC-7, AC-8, AC-9)

```
$ grep -n "review\." .tfw/workflows/config.md
92:| `review.min_verify_ratio` | `.tfw/workflows/review.md` | Step 2: Verify | Min verify ratio |
```

One row, and its pointer resolves: `review.md:60` is `## Step 2: Verify`. The `review.default_mode`
row is gone with its key.

```
$ grep -rn "review mode" .tfw/ --exclude=CHANGELOG.md
(no matches — exit 1)

$ grep -rniE "review mode|review-mode|default_mode: code|code / docs / spec|mode-aware|mode file" \
       .claude/commands/tfw-review.md .claude/commands/tfw-config.md \
       .agent/workflows/tfw-review.md .agent/workflows/tfw-config.md \
       .tfw/adapters/codex/skills/tfw-review/SKILL.md .agents/skills/tfw-review/SKILL.md
(no matches — exit 1)
```

Behavioural parity, five `diff` runs, all empty:

| Copy | Source | Result |
|---|---|---|
| `.claude/commands/tfw-review.md` | `.tfw/workflows/review.md` | identical |
| `.agent/workflows/tfw-review.md` | `.tfw/workflows/review.md` | identical |
| `.claude/commands/tfw-config.md` | `.tfw/workflows/config.md` | identical |
| `.agent/workflows/tfw-config.md` | `.tfw/workflows/config.md` | identical |
| `.agents/skills/tfw-review/SKILL.md` | `.tfw/adapters/codex/skills/tfw-review/SKILL.md` | identical |

The four full copies were byte-identical to their sources *before* this task as well (checked at
onboarding), so "nothing project-specific was clobbered" is established against a clean baseline
rather than assumed. The Codex skill line *"Follow the review-mode WAIT gate…"* now reads *"Follow
every gate in the workflow exactly as it requires, including each stage self-check gate before
advancing"* — the four self-check gates are what actually remains to be followed.

`map.md` and `verify.md` carry no `Mode:` field:

```
$ grep -n "Mode" .tfw/templates/review/map.md .tfw/templates/review/verify.md
(no matches)
```

## E7 — The grep gate, verbatim (AC-12)

```
$ grep -rn "code / docs / spec\|default_mode: code\|Review Mode\|review/{code" \
       .tfw/ .claude/ .agent/ .agents/ --exclude=CHANGELOG.md
$ echo $?
1
```

**Zero matches.** Recorded with its exit status because a silent pass and an empty output look the
same on the page.

**A finding about the gate itself, not about the sweep.** One of the four alternatives,
`review/{code`, **matched nothing in this repository before any change was made** — the real string
was always `.tfw/workflows/review/{mode}.md`. A quarter of the acceptance test could never fail,
which is precisely the anti-pattern this task adds to `conventions.md` §14. Two narrower holes: the
pattern is case-sensitive, so `glossary.md`'s lowercase *"coordinator in review mode"* was invisible
to it, and `config.md`'s `review.default_mode` registry row does not match `default_mode: code`.
AC-8 and AC-9 cover all three places by other means, so the ACs *together* are sound — the single
command is not. Supplementary sweep, wider and case-insensitive:

```
$ grep -rniE "review mode|review-mode|mode-aware|mode-specific|default_mode: code|review/\{(code|mode)|Mode: \{code" \
       .tfw/ .claude/ .agent/ .agents/ --exclude=CHANGELOG.md
.tfw/workflows/research/base.md:79:  Mode-specific: ☐ {from mode file}
.tfw/workflows/research/deep.md:21:Mode-specific:
.claude/commands/tfw-research.md:79:  Mode-specific: ☐ {from mode file}
.agent/workflows/tfw-research.md:79:  Mode-specific: ☐ {from mode file}
```

All four hits are the **research** mode axis (`focused` / `deep`), which is out of scope and
untouched. No review-mode residue at any case or spelling.

## E8 — History is intact (AC-12)

```
$ grep -rl "Review Mode" tasks/ | wc -l
41
```

41 files under `tasks/` still carry the string, including
`tasks/TFW-53__hl_contract_and_goal_defence/phase-a/REVIEW__phase-a__contract_in_artifacts.md`,
whose header still reads `> **Review Mode**: spec` with its owner-override note — the file used as
this task's own dry-run subject. Nothing under `tasks/` appears in this task's diff except its own
artifacts (ONB, this EV file, RF). No past CHANGELOG entry was edited; `## [1.1.0]` is inserted
above `## [1.0.0]`, and the `## [Unreleased]` heading is left in place.

## E9 — Diffstat, and a trace anomaly that has to be reported (AC-12)

**The substance holds.** Three files deleted, zero framework files created, net LOC negative. The
only new file is this task's own evidence artifact, which is not a framework file.

**The anomaly.** The three deletions are **not in this task's commit**. A concurrent session working
on TFW-53 Phase B committed `fbdf443 [claude-code/TFW-53/phase-b/executor] enforce the contract in the
workflows` at 17:44, and that commit swept up my already-staged `git rm` of the mode files:

```
$ git show --stat fbdf443
 .tfw/templates/RES.md           |  2 +-      ← TFW-53/B's own work
 .tfw/workflows/plan.md          | 82 +++---   ← TFW-53/B's own work
 .tfw/workflows/research/base.md |  6 ++-      ← TFW-53/B's own work
 .tfw/workflows/review/code.md   | 15 ------   ← TFW-56's deliverable
 .tfw/workflows/review/docs.md   | 12 ------   ← TFW-56's deliverable
 .tfw/workflows/review/spec.md   | 12 ------   ← TFW-56's deliverable
```

Scope of the leak, bounded by timing: at 17:44 the only TFW-56 change staged in the index was that
`git rm`. Every other file in this task was still an unstaged working-tree edit and was not captured.
So the leak is exactly three deletions, and they are the three that were meant to be deleted.

**Consequence, stated plainly.** The outcome AC-1 and AC-12 require is real and verifiable — the
folder is gone from the working tree and from `HEAD`. What is wrong is the **attribution**: recovering
"when did TFW-56 delete the mode files" by reading TFW-56's commits will find nothing, and the
deletion is filed under a task whose own TS says `review.md` and its neighbourhood are "Phase C only".
No attempt was made to repair this by rewriting history — `fbdf443` is another session's commit and
rewriting it is not an executor's call. It is recorded here, in RF §2 and in RF §6.

**This task's own diffstat**, staged by explicit path only — never `git add -A`, which is how the
leak became possible in the first place:

```
 .agent/workflows/tfw-config.md                  |  1 -
 .agent/workflows/tfw-review.md                  | 27 +++-------
 .agents/skills/tfw-review/SKILL.md              |  2 +-
 .claude/commands/tfw-config.md                  |  1 -
 .claude/commands/tfw-review.md                  | 27 +++-------
 .tfw/CHANGELOG.md                               | 19 +++++++
 .tfw/VERSION                                    |  2 +-
 .tfw/adapters/codex/skills/tfw-review/SKILL.md  |  2 +-
 .tfw/conventions.md                             |  1 +
 .tfw/glossary.md                                |  6 ++--
 .tfw/project_config.yaml                        |  3 +-
 .tfw/templates/REVIEW.md                        | 21 +++++---
 .tfw/templates/project_config.yaml              |  1 -
 .tfw/templates/review/judge.md                  | 35 ++++++++-----
 .tfw/templates/review/map.md                    |  1 -
 .tfw/templates/review/verify.md                 | 16 +++++-
 .tfw/workflows/config.md                         |  1 -
 .tfw/workflows/review.md                        | 27 +++-------
 README.md                                       |  2 +-
 TECH_DEBT.md                                    |  2 +-
 20 files changed, 105 insertions(+), 94 deletions(-)
```

20 modified + 3 deleted (in `fbdf443`) = **23 framework and root files touched**, one more than the
TS's 22 because `.tfw/project_config.yaml` carries two changes rather than one — the key removal and
the version field, which tracks `VERSION` on every release (RF §2). Against the project budget of 30
files / 15 new / 3000 LOC / 30 modified: within budget on every axis, net LOC **−94 + 105 = +11** in
the modified set and **−39** once the three deleted files are counted.

## E10 — Build gate (Step 10)

```
$ python -m pytest docs/scripts/ -q
....................................................................    [100%]
68 passed in 33.47s
```

The docs pipeline is the consumer of every changed `.tfw/` file — `conventions.md`, `glossary.md`,
`workflows/**` and `templates/**` are Source Manifest rows 4, 5, 12 and 13. Deleting three
`workflows/**` files removes three generated pages; the suite passes, and `gen_docs.py` carries no
reference to review modes (`grep -rn "review" docs/scripts/*.py` → no matches), confirming RES D9's
consumer audit against the shipped state rather than against the pre-change state.

## Attachments

> No binary artifacts. Every exhibit above is a command with its output, or a reading against a named
> file and line.

---

*EV — TFW-56: Remove the Review Mode Axis | 2026-08-13*
