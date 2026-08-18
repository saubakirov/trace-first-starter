# EV — TFW-53 / Phase D: Glossary, Adapters and Version

> **Date**: 2026-08-14
> **Author**: Executor (Claude Code)
> **Task**: TFW-53
> **Passes**: first 2026-08-14 · **corrective 2026-08-18** after REVIEW 🔄 REVISE
> **TS**: [TS Phase D](../TS__phase-d__glossary_adapters_version.md)

---

## Environment

| Field | Value |
|-------|-------|
| OS | Windows 11 Pro 10.0.26200 |
| Shell | Git Bash (POSIX sh) — the `config.md` drift check is a `bash` snippet and was run verbatim |
| Language / Runtime | Python (project venv), `python -m pytest` |
| Repository state | branch `master`, working tree; concurrent uncommitted TFW-55 edits present in `README.md` and two TFW-55 files |
| CI / Pipeline | local — `docs/scripts/` suite only; the GitHub Pages build was not triggered |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | All ten terms resolve in `glossary.md` under a case-insensitive `grep -ci`. Counts: HL Contract 2 · Contract Baseline 3 · Frozen Section 2 · Amendment 5 · Amendment Log 1 · Project North Star 4 · Purpose Check 3 · not fit for purpose 1 · deferral confession 1 · Result Visualization 2. All ≥ 1 | local shell | VERIFIED | [`ac-gates.txt`](ac-gates.txt) § AC-1 |
| E2 | AC-1 | Every article is at or under the p75 = 50-word ceiling: 48 · 49 · 50 · 50 · 45 · 48 · 48 · 43 · 41 · 49. Median of the ten is 48 | local shell | VERIFIED | [`ac-gates.txt`](ac-gates.txt) § AC-1 `wc -w` |
| E3 | AC-1 | Each of the ten articles ends with a `→` pointer, and each pointer target was opened: `conventions.md` §3 HL Contract · rules 13-16 · rules 3, 5 · rules 10-12 · rule 4 · §3 Project North Star · `templates/review/judge.md` (×3) · `conventions.md` §3 Visual Sections | local shell + file read | VERIFIED | inline — `git diff .tfw/glossary.md` |
| E4 | AC-1 | `Deferral confession` exists in the framework and its pointer resolves: `templates/review/judge.md`:50, the second of the Purpose Check's three tests. A case-**sensitive** search for the lower-case form returns 0, which is why the gate was changed to `grep -ci` | local shell | VERIFIED | `judge.md`:50, quoted in RF §2 D4 |
| E5 | AC-2 | `frozen baseline` across `.tfw/**.md` excluding `CHANGELOG.md`: **8 → 0** | local shell | VERIFIED | [`ac-gates.txt`](ac-gates.txt) § AC-2 |
| E6 | AC-2 | `committed baseline` excluding the negation (`grep -roE "[^n]committed baseline"`): **0**, before and after. The two literal substring hits are `uncommitted baseline` at `conventions.md`:75 and `plan.md`:60, ruled out of mandate (ONB Q1 → (a)) and left untouched | local shell | VERIFIED | [`ac-gates.txt`](ac-gates.txt) § AC-2 |
| E7 | AC-2 | Bare capitalised `North Star`: **2 genuine → 0**. `templates/HL.md`:18 and :20 renamed to `Project North Star`. The one remaining literal match, `glossary.md`:268 `> North Star.`, is the tail of `Project North Star` wrapped across a line break — recorded rather than "fixed" | local shell | VERIFIED | [`ac-gates.txt`](ac-gates.txt) § AC-2, remaining-occurrence block |
| E8 | AC-2 | Neither workflow grew: `plan.md` **1,195 → 1,195** (zero occurrences, so zero substitutions), `review.md` **1,176 → 1,176** (two substitutions, 3 words → 3 words each) | local shell | VERIFIED | [`ac-gates.txt`](ac-gates.txt) § AC-2 budgets |
| E9 | AC-3 | Direction check run **before** any copy, all 14 pairs. Source-only vs copy-only line counts recorded per pair; every copy-only line read and confirmed to be an older form of a source-only line in the same hunk. **No copy holds content its source lacks** — AC-3's stop condition does not fire | local shell + diff read | VERIFIED | [`direction-check.txt`](direction-check.txt) |
| E10 | AC-3, TD-157 | `config.md` drift check **before**: 14 `DRIFT:` lines, exit 0. Captured verbatim | local shell | VERIFIED | [`drift-check-before.txt`](drift-check-before.txt) |
| E11 | AC-3, TD-157 | `config.md` drift check **after** the sync: **no output**, exit 0. Independently, `diff` per pair across all 22 copies returns 0 lines | local shell | VERIFIED | [`drift-check-after.txt`](drift-check-after.txt) |
| E12 | AC-3 | Codex routers read in full. `tfw-review/SKILL.md` — no statement is false, unchanged. `tfw-plan/SKILL.md` — the `description` field read *"creates or revises **approved** HL/TS artifacts"*, which grants what `conventions.md` §3 rule 3 now forbids; one word removed in both the source and the installed copy, which remain byte-identical | local shell + file read | VERIFIED | `git diff .tfw/adapters/codex/ .agents/skills/` |
| E13 | AC-4 | `CLAUDE.md` both purpose cells rewritten and read back against the shipped workflows: `plan.md` Step 4 (freeze), Step 6c (classify/route), Step 6d (verdicts); `review.md` Step 3 + the Purpose Check paragraph. Two missing rows added (`/tfw-knowledge`, `/tfw-config`) per the coordinator's recorded R6 extension. `AGENTS.md` checked row by row — nothing false, so unchanged, exactly as AC-4 directs | local shell + file read | VERIFIED | `git diff CLAUDE.md`; `git diff --stat AGENTS.md` empty |
| E14 | AC-5 | `cat .tfw/VERSION` → `1.2.0`; `grep -c 'version: "1.2.0"' .tfw/project_config.yaml` → 1; `grep -c "TFW-54" .tfw/CHANGELOG.md` → 1. One `## [1.2.0]` entry; `grep -c "12 drifted copies"` → 0, so the stale count did not survive the fold | local shell | VERIFIED | [`ac-gates.txt`](ac-gates.txt) § AC-5 |
| E15 | AC-6 | Each of the four named lines opened before and after: `templates/HL.md`:10 (recovery command → pointer), `glossary.md` Knowledge Gate (Phase 0 → Step 2, checked against `plan.md`'s actual Steps 0-7), `compilable_contract.md`:81 (`PP{N}`, `NS{N}` added to the Resolution rules), `compilable_contract.md`:65 (`KNOWLEDGE.md` §0 removed from the list) | local shell + file read | VERIFIED | `git diff` hunks, quoted in RF §1 |
| E16 | AC-6 | `python -m pytest docs/scripts/` — **68 passed** in 55.82s, against a pre-phase baseline of 68 passed in 55.99s. Same count, no new failures | local venv | VERIFIED | [`ac-gates.txt`](ac-gates.txt) § AC-6 |
| E17 | AC-7, AC-9 | ⟳ **Row replaced 2026-08-18.** Command named exactly: `git diff -U0 ce30f3b^ ce30f3b -- .tfw/conventions.md .tfw/glossary.md .tfw/templates/HL.md .tfw/templates/review/judge.md .tfw/workflows/review.md .tfw/compilable_contract.md \| grep -c '^@@'` → **16** (14 at default context). Per file: 2 · 4 · 4 · 2 · 2 · 2. Classification: **10 substitution hunks carrying 11 substituted lines** (`judge.md` @@ -34,2 holds two), **4 named debt fixes**, **2 addition sites**. `git diff --stat` → 6 files, 47 insertions, 15 deletions. **No hunk is a rewritten sentence** | local shell | VERIFIED | full reconciliation in RF §9; `git diff -U0` output |
| E17b | AC-9 | **The first pass's figure of 12 does not reproduce, and why is recorded rather than glossed.** The ledger names six files including `glossary.md`; the command actually run listed `plan.md` (0 hunks) and omitted `glossary.md` (4 hunks) — 16 − 4 + 0 = 12. A number produced by one file set and reported against another | local shell | VERIFIED | RF §9, *Where 12 came from* |
| E18 | AC-7 | `git diff --stat` on the six framework files: `compilable_contract.md` 4 · `conventions.md` 4 · `glossary.md` 36 · `templates/HL.md` 8 · `judge.md` 6 · `review.md` 4 — 47 insertions, 15 deletions. Per-file justification in RF §1 | local shell | VERIFIED | RF §1 diffstat table |
| E19 | AC-8 | ⟳ **Row replaced 2026-08-18.** Counted under the rule the owner stated on 2026-08-18 — *the budget counts product files, not task artifacts* — and the rule is quoted beside the number, which the first pass did not do. `git diff --name-status ce30f3b^ ce30f3b` → 27 modified, 6 added; plus `README.md` modified and unstaged in the working tree. **Product: 28 modified of 30, 0 new of 15.** Of the 28, 14 are byte `cp` and 14 authored. **Trace, unbudgeted: 6** — the RF, the EV file, four command-output attachments | local shell | VERIFIED | RF §1 accounting table |
| E19b | AC-8 | **The first pass compared only the sub-limits and computed no total** — which is exactly what let a 33-file phase read as green. The reviewer's 33-vs-30 count was arithmetically correct against its own reading of the rule. Recorded as a defect of the first trace, not argued away | reading RF/EV first pass | VERIFIED | REVIEW §2 row 5, verify.md V11 |
| E20 | AC-8 | **The TS's own corrected figure is also wrong, and I did not adopt it.** TS AC-8 states *"27 modified product files"*; 27 is the commit's modified count and omits `README.md`, a product file this phase changed twice and changes again in this pass. Correct figure **28**; conclusion unaffected (28 < 30). Ambiguity filed as **TD-173** | local shell | VERIFIED | RF §1, closing note |
| E21 | AC-10 | §8 reads `No strategic insights.` with its reason. §7 carries one row. Each re-homed item was opened at its stated destination and found there: **S3** in §2 decision 11, **S4** in §6 observation 8, **S2's operative half** in §6 observation 9, **FC5** in §6 observation 10. S1, FC1, FC2, FC4 dropped, with the ground stated | file read | VERIFIED | RF §2, §6, §7, §8 |
| E22 | AC-10 | **The §7 contradiction is measured, not asserted.** `templates/RF.md` §7 Scope admits *"agent-observed project patterns"* four lines above a Human-Only Test that bars anything *"an agent can discover by reading code or running commands"*. Both cannot hold. RF TFW-56 (3 entries), RF TFW-53/B (2) and RF TFW-53/C (4) carried agent-derived entries and were approved — four consecutive reviews. Filed as **TD-174** | file read across four RFs | VERIFIED | `TECH_DEBT.md` TD-174 |
| E23 | AC-11 | `grep -rn "PROJECT_CONFIG" CLAUDE.md AGENTS.md` → **before: 2 matches** (`CLAUDE.md`:51, :53); **after: no matches**, exit 1. Both now read `.tfw/project_config.yaml`; `ls .tfw/project_config.yaml` confirms the target exists. TD-172 closed with its reason | local shell | VERIFIED | RF §6 obs. 5 |
| E24 | AC-11 | Repo-wide sweep for the retired filename outside `CLAUDE.md`: **no live occurrence**. Every hit is history that must not be rewritten (`CHANGELOG.md`, `KNOWLEDGE.md` D16/D20/D22/D48 + Legacy, `knowledge/philosophy.md` F23, two README task titles, 136 files under `tasks/`) or the rule itself (`conventions.md`:468). `AGENTS.md` and `.tfw/workflows/init.md` are clean. **Reported, not fixed**, as AC-11 directs | local shell | VERIFIED | RF §6 obs. 11 |

## Verdict

Evidence verdict: **26/26 VERIFIED**, 0 DEFERRED, 0 BLOCKED, 0 N/A

> ⟳ **Recomputed 2026-08-18 (AC-12), not restored.** At REVISE time the supported count was the
> reviewer's **17 of 19**: E17 and E19 did not establish their claims. Both rows were **replaced**, not
> re-asserted — E17 now names the command and carries its 16-header output, E19 carries the counting rule
> and the 28-of-30 product total. Seven rows were added for the corrective pass — E17b, E19b and E20–E24; row
> count 19 → 26. **E1–E16 and E18 were not touched and not re-run** — the reviewer independently
> established all seventeen at 100% file coverage, and re-running them to pad a count is the behaviour
> this section exists to prevent. No row was upgraded without its underlying artifact changing.

## Attachments

| File | Description |
|------|-------------|
| `drift-check-before.txt` | The `config.md` drift check run verbatim before the sync — 14 `DRIFT:` lines, exit 0 |
| `direction-check.txt` | Per-pair source-only / copy-only line counts, run before any copy, with the read verdict |
| `drift-check-after.txt` | The same check after the sync — no output, exit 0 |
| `ac-gates.txt` | Every AC gate command and its output: AC-1 term counts and word counts, AC-2 occurrence counts and word budgets, AC-5 release gates, AC-6 test result |

---

*EV — TFW-53 / Phase D: Glossary, Adapters and Version | 2026-08-14*
