# EV — TFW-53 / Phase D: Glossary, Adapters and Version

> **Date**: 2026-08-14
> **Author**: Executor (Claude Code)
> **Task**: TFW-53
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
| E17 | AC-7 | Every diff hunk in the six framework files reviewed one by one with `git diff -U0`. Twelve hunks total: eight canonical-term substitutions, four named debt fixes, plus the glossary's pure additions. **No hunk is a rewritten sentence.** `plan.md` has no hunk at all | local shell | VERIFIED | inline diffstat in RF §1; `git diff -U0` output |
| E18 | AC-7 | `git diff --stat` on the six framework files: `compilable_contract.md` 4 · `conventions.md` 4 · `glossary.md` 36 · `templates/HL.md` 8 · `judge.md` 6 · `review.md` 4 — 47 insertions, 15 deletions. Per-file justification in RF §1 | local shell | VERIFIED | RF §1 diffstat table |
| E19 | AC-3 (scope) | Scope budget: **28 modified files**, 1 new artifact folder, against a 30-file limit. Fourteen of the 28 are `cp` with zero authored content, matching the TS's estimate exactly | local shell | VERIFIED | `git status --short` in RF §4 |

## Verdict

Evidence verdict: 19/19 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

## Attachments

| File | Description |
|------|-------------|
| `drift-check-before.txt` | The `config.md` drift check run verbatim before the sync — 14 `DRIFT:` lines, exit 0 |
| `direction-check.txt` | Per-pair source-only / copy-only line counts, run before any copy, with the read verdict |
| `drift-check-after.txt` | The same check after the sync — no output, exit 0 |
| `ac-gates.txt` | Every AC gate command and its output: AC-1 term counts and word counts, AC-2 occurrence counts and word budgets, AC-5 release gates, AC-6 test result |

---

*EV — TFW-53 / Phase D: Glossary, Adapters and Version | 2026-08-14*
