# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42 (`tfw.review.min_verify_ratio`)
> RF files claimed: 24 (20 modified + 3 deleted + 1 new evidence artifact)
> Files to verify: ⌈24 × 0.42⌉ = **10**. Opened: **24 of 24 (100%)** — escalated on discrepancy V-D1.

## Verification Log

### V1: `.tfw/workflows/review/{code,docs,spec}.md` — deleted
- **RF claim:** folder gone, not emptied; 15 / 12 / 12 lines.
- **Actual:** `ls .tfw/workflows/review/` → *No such file or directory*. `git cat-file -e HEAD:.tfw/workflows/review/code.md` → *does not exist in HEAD*. Content recovered from `6c3c506` for the coverage audit below.
- **Match:** ✅

### V2: `.tfw/workflows/review.md`
- **RF claim:** mode step + WAIT removed, mode-file load removed from Verify, Steps 2-8 → 1-7, Step 0 = Session Naming.
- **Actual:** headings at L16/52/60/78/89/100/109/116 read Step 0 Name This Session · 1 Map · 2 Verify · 3 Judge · 4 Decide · 5 Tech Debt · 6 Update Traces · 7 Knowledge Capture. Contiguous, no gaps. L65 reads *"Every action in it is unconditional — verification depth is set by the ratio below, never by the kind of work under review."* Only surviving "mode" is L7 *"coordinator in review-locked mode"* — the Role Lock, one meaning.
- **Match:** ✅

### V3: `.tfw/templates/review/judge.md`
- **RF claim:** no `Mode:`, no Mode-Specific section, 10 universal rows, U2 split, S1/S2/S4 added with rates, `✅/❌/⚪` vocabulary, contrast note, two new Checkpoint items.
- **Actual:** `grep -c "Mode"` → 0. Ten table rows. Row 2 carries clauses (a) mapping integrity and (b) design soundness *(4.5%)*. Row 8 *Evidence sufficiency* *(16.1%)*, row 9 *Backward compatibility* *(8.5%)*, row 10 *Safety* *(4.0%)* with "kept on consequence, not on rate" written into the row. Contrast note at L26-30. Checkpoint gains *"Every ⚪ N/A carries a stated reason — no row skipped as a bare ✅?"* and *"Rows 7 and 8 answered separately, with different reasoning?"*.
- **Baseline (`6c3c506`):** 7 universal rows, `Mode: {code / docs / spec}` header, `## Mode-Specific Checklist` section. Confirms the 7 → 10 move and the removals.
- **Match:** ✅

### V4: `.tfw/templates/review/verify.md`
- **RF claim:** `Mode:` removed; new **Claim & Source Checks** section with the three orphaned actions, a table and a Checkpoint item.
- **Actual:** section present at L26-38, marked *"Unconditional — every review, whatever the deliverable is. Three actions, all mandatory"*, wording each action and stating it feeds judge.md row 8. Table `C1`. Checkpoint L73 added. `grep -n "Mode"` → no matches.
- **Match:** ✅

### V5: `.tfw/templates/review/map.md`
- **RF claim:** `Mode:` field removed.
- **Actual:** header carries Mindset, Test, RF, TS. No `Mode:`.
- **Match:** ✅

### V6: `.tfw/templates/REVIEW.md`
- **RF claim:** `Review Mode` header field and mode placeholder removed; §3 realigned to ten rows matching `judge.md` in order; `⚪` added.
- **Actual:** ten rows, identical labels and order to `judge.md`. `<!-- Add mode-specific checklist items… -->` absent. §3 note states `⚪ N/A` requires a stated reason.
- **Baseline:** 6 rows + the placeholder comment, no Evidence completeness row. Confirms RF §2 decision 5.
- **Match:** ✅

### V7-V8: `.tfw/project_config.yaml`, `.tfw/templates/project_config.yaml`
- **RF claim:** `default_mode` removed from both; `min_verify_ratio: 0.42` intact with comment; `tfw.version` → `1.1.0`.
- **Actual:** `project_config.yaml:59-60` → `review:` / `min_verify_ratio: 0.42    # minimum fraction of changed files to verify (escalate to 1.0 on discrepancy)`. `templates/project_config.yaml:63-64` → `review:  # ← FRAMEWORK: updated by tfw-update` / `min_verify_ratio: 0.42`. No `default_mode` in either `tfw.review` block. `tfw.version: "1.1.0"` at L7. The surviving `default_mode: focused` at L49 / L53 is the **research** axis, out of scope.
- **Match:** ✅

### V9: `.tfw/workflows/config.md`
- **RF claim:** `review.default_mode` row removed; one `review` row remains, pointer resolves.
- **Actual:** `grep -n "review\."` → single row L92 `| review.min_verify_ratio | .tfw/workflows/review.md | Step 2: Verify | Min verify ratio |`. Opened `review.md` at Step 2 — it is Verify. Pointer resolves.
- **Match:** ✅

### V10: `.tfw/conventions.md`
- **RF claim:** §14 anti-pattern added; Review subfolder entry needed no change.
- **Actual:** L496 carries the anti-pattern, worded to cover both formulations and permitting retention on consequence *provided the reason is written into the row*. L262-264 Review subfolder entry describes stage files with no mode vocabulary. L466 *"Mode files loaded at Step 2"* remains — reported, see V-D2.
- **Match:** ✅

### V11: `.tfw/glossary.md`
- **RF claim:** Reviewer heading disambiguated; entry describes one universal 10-row checklist; Principles Check pointer Step 4 → Step 3.
- **Actual:** L127 `### Reviewer (AI — coordinator under the reviewer Role Lock)`; L128 describes *"one universal 10-row Judge checklist — every row asked in every review, with explicit `⚪ N/A`"*. L142 points at `review.md` Step 3, which is Judge. L157 Session Naming → `review.md` Step 0, now true.
- **Match:** ✅

### V12-V13: `.tfw/VERSION`, `.tfw/CHANGELOG.md`
- **RF claim:** `1.1.0`; new entry; `### Removed` names the key.
- **Actual:** `VERSION` = `1.1.0`. `## [1.1.0] — 2026-08-13` inserted below `## [Unreleased]` and above `## [1.0.0]`. `### Removed` L21 names **`tfw.review.default_mode`** with upgrade instructions ("this key is now inert… delete it from your `tfw.review` block") and states `min_verify_ratio` is unchanged. D42's revocation recorded at L22. No prior entry altered.
- **Match:** ✅

### V14-V19: the six adapter and entry-point copies
- **RF claim:** all six clean of mode vocabulary; five `diff` runs empty; Codex skill no longer names a WAIT gate.
- **Actual:** re-ran the five diffs independently — `.claude/commands/tfw-review.md`, `.agent/workflows/tfw-review.md`, `.claude/commands/tfw-config.md`, `.agent/workflows/tfw-config.md`, `.agents/skills/tfw-review/SKILL.md` all **identical** to their sources. Read `.tfw/adapters/codex/skills/tfw-review/SKILL.md` in full: the line now reads *"Follow every gate in the workflow exactly as it requires, including each stage self-check gate before advancing"* — the four gates that actually remain. No WAIT-gate reference.
- **Match:** ✅

### V20-V21: `TECH_DEBT.md`, `README.md`
- **RF claim:** TD-106 closed with the reason; Task Board → 🟢 RF with ONB link.
- **Actual:** TD-106 status ✅ Closed, reason recorded ("deleted, not annotated"), naming the renumbering carried out in the same task. README L304 shows 🟢 RF with HL / research / TS / ONB / RF links present.
- **Match:** ✅

### V22: `evidence/EV__TFW-56__review_mode_removal.md`
- **RF claim:** 16 rows, 9 VERIFIED / 0 DEFERRED / 0 BLOCKED / 7 N/A.
- **Actual:** 16 rows, counts confirmed. Environment header complete. Every VERIFIED row carries a command with output or a named-file reading. The 7 N/A each quote the TS's own `Evidence:` field verbatim — checked against TS §5, all seven quotes are accurate.
- **Match:** ✅

### V23: coverage audit against the deleted files (AC-3, AC-4)
- **RF claim:** eight mode checklist rows and eight distinct verify actions, each with a stated home.
- **Actual:** recovered all three mode files from `6c3c506` and counted independently.
  **Checklist rows — 8:** `code` Code quality · Test coverage · Security · Breaking changes; `docs` Content quality · Source verification; `spec` Analytical quality · Source attribution. Matches the RF table exactly.
  **Verify actions — 10 entries, 8 distinct:** the ratio action appears in all three files (3 → 1); `code` adds re-run build/test, AC×DoD cross-check, test-file check; `docs` adds structure-matches-spec and spot-check claims; `spec` adds citations-traceable and data-vs-primary-source. Matches the RF table exactly, including action 5 (*structure matches spec*), a fourth `docs` action neither HL nor TS enumerated and which the executor accounted for anyway under DoF-1.
  Each stated destination opened and confirmed present in the shipped file.
- **Match:** ✅

### V24: `git` — history and attribution
- **RF claim:** 3 deletions, no framework file created, no task REVIEW file or past CHANGELOG entry edited; deletions swept into `fbdf443`.
- **Actual:** `git show --stat fbdf443` contains the three `review/` deletions alongside TFW-53/B's own three files — the sweep is real and exactly as described. `68a8be8` touches 23 files; the only `tasks/` paths are TFW-56's own ONB, RF and EV. `grep -rl "Review Mode" tasks/` now returns **43**, not the RF's 41 — the two extra are this task's own RF and EV, written after the count. No pre-existing REVIEW file appears in either commit.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python -m pytest docs/scripts/ -q` | **68 passed in 36.97s** — re-run independently, matches RF §4 |
| 2 | `grep -rn "code / docs / spec\|default_mode: code\|Review Mode\|review/{code" .tfw/ .claude/ .agent/ .agents/ --exclude=CHANGELOG.md` | zero matches, **exit 1** — the AC-12 gate re-run independently |
| 3 | `ls .tfw/workflows/review/` | *No such file or directory* |
| 4 | `grep -rniE "review mode\|review-mode\|default_mode\|mode-specific\|mode file" .tfw/ .claude/ .agent/ .agents/` | hits only in the **research** axis, the new CHANGELOG entry, and `conventions.md:466` — no review-mode residue |
| 5 | `diff` × 5 across the adapter copies | all empty |
| 6 | `grep -rn "review\.md.*Step [0-9]\|review\.md:[0-9]"` repo-wide | every pointer resolves; no stale step reference anywhere (DoF-3 clear) |
| 7 | `git show --stat fbdf443` / `68a8be8` | attribution anomaly confirmed exactly as the RF describes it |

## Claim & Source Checks

> Applying the section this task ships, on its own delivery. Three claims chosen by how much the
> result rests on them.

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | *"E2 marked VERIFIED… `RESTRICT` is not exercised by this corpus"* — finding 1 of the S1-vs-U7 dry-run, the exhibit AC-2 passes or fails on | EV §E3 | `TFW-53/phase-a/evidence/EV__phase-a…md:71` — verbatim: *"`RESTRICT` is not exercised by this corpus… recorded as a coverage gap"* | ✅ |
| C2 | *"E13's conclusion was superseded inside the same pass by E15: no `--grep` form can be subject-only"* | EV §E3 | Same file L185 — *"The finding that decided it: no `--grep` form can be subject-only."* E13 does ship a `--grep` form and E15 does supersede it | ✅ |
| C3 | *"E11 scored 4/4 while the budget and cut-order property is absent from both the rule and this check"* | EV §E3 | Same file L129 — *"Not tested: the earlier budget and cut-order property is absent from both the rule and this check"* | ✅ |
| C4 | *"Both attachments resolve — `baseline_recovery.txt` and `classification_exercise.md`"* | EV §E3 | `ls TFW-53/phase-a/evidence/` — both present | ✅ |
| C5 | *"41 files under `tasks/` still carry `Review Mode`"*, including TFW-53/A's REVIEW header | EV §E8 | Count is now 43 (this task's own RF and EV added the string after the measurement); the named header `> **Review Mode**: spec` is present at L6 of that REVIEW file | ✅ *(count drift explained, claim intact)* |
| C6 | *"`git log -p` shows `tfw.version` moving in lockstep with `.tfw/VERSION` on every release since 0.8.5"* | RF §2 decision 1 | Both fields read `1.1.0` today; the historical lockstep is the executor's stated method and is plausible, but I did not re-run the full `log -p`. **Partially verified** | ⚠️ |
| C7 | Measured firing rates (16.1% / 8.5% / 4.5% / 4.0%) carried inside the promoted rows | `judge.md` rows 2, 8, 9, 10 | RES iter1 E1/E2 (637 rows / 203 reviews / 3 installs) and HL §3 coverage table — the numbers in the shipped rows match the amended §3 table exactly | ✅ |

## Discrepancies Found

**V-D1 — RF §3 AC-8 states a command it did not run.** The RF writes
*"`grep -rn "review mode" .tfw/` → 0 matches"*. Run exactly as written, that command returns **two
hits**, both in `.tfw/CHANGELOG.md` (L17 and L23 of the new 1.1.0 entry). The EV file records the
correct command — `grep -rn "review mode" .tfw/ --exclude=CHANGELOG.md` — so the work was done
properly and the RF dropped the flag when summarising.

*Substance is unaffected.* TS AC-8's gate is not "zero matches"; it is *"every remaining hit means
the same thing"*. Both hits are the new changelog entry describing the axis that was removed —
exactly one meaning, and the changelog is the one file DoD-15 forbids rewriting. AC-8 passes on its
own criterion. Severity: **Low**, a reporting inaccuracy in a summary line, not a coverage failure.
Escalated verification to 100% on finding it; nothing further surfaced.

**V-D2 — `conventions.md:466` remains, by decision, not by oversight.** *"Mode files loaded at Step
2, not at start"* is inherited from D42 and now describes only the research axis. It is true as
written (`research/base.md` Step 2 loads `focused`/`deep`), out of AC-8's scope, and correctly
reported in RF §2 decision 6 and Observation 6 instead of being silently edited. Not a discrepancy
against the TS — recorded so the review does not read as having missed it. → tech debt.

**V-D3 — the count in EV §E8 has drifted from 41 to 43.** Cause identified: this task's own RF and
EV files contain the string `Review Mode` and were written after the measurement. The claim the count
supports — *no pre-existing REVIEW file was modified* — is verified independently by
`git show --name-only 68a8be8`, which touches only TFW-56's own artifacts under `tasks/`. Not a
defect.

**No other discrepancies.** All 24 files opened; every AC checkmark cross-checked against the actual
file; the mandated grep gate, the build gate and the five parity diffs re-run independently.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | EV §E1 — folder absence, step contiguity | ✅ | ✅ — `ls` re-run, headings re-counted 0-7 |
| E2 | EV §E2 — 10 rows, `Mode` count 0 | ✅ | ✅ — re-counted against the shipped file |
| E3 | EV §E3 — S1-vs-U7 dry-run vs TFW-53/A | ✅ | ✅ — all three findings traced to the source EV file, C1-C4 above. Rows 7 and 8 did produce different answers from different reasoning |
| E4-E6 | N/A rows quoting TS Evidence fields | ✅ | ✅ — all seven N/A quotes checked against TS §5, verbatim |
| E7 | EV §E5 — both config excerpts, before and after | ✅ | ✅ — re-run; `min_verify_ratio` comment byte-identical |
| E10 | EV §E6 — six-adapter grep + five diffs | ✅ | ✅ — re-run independently, all empty |
| E13 | EV §E7 — the grep gate verbatim, with exit status | ✅ | ✅ — re-run, zero matches, exit 1. The executor's finding that `review/{code` was a dead alternative is correct: the real string was always `review/{mode}.md` |
| E14 | EV §E8 — history intact | ✅ | ⚠️ count 41 → 43, explained (V-D3); the claim it supports verifies independently |
| E15 | EV §E9 — diffstat + attribution anomaly | ✅ | ✅ — `git show --stat fbdf443` confirms the three TFW-56 deletions sitting in TFW-53/B's commit, exactly as described. Keeping this VERIFIED rather than softening it to DEFERRED was the right call: the fact is true and the disclosure is the point |
| E16 | EV §E10 — 68 tests passed | ✅ | ✅ — re-run: 68 passed |

Total evidence items: 16 · verified: 16 · missing: 0.

## Knowledge Citations Verified

HL §7.2 carries 26 citations. Sampled 8, weighted toward the ones the design rests on.

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | HL §7.2 #1 | `KNOWLEDGE.md` D42 — review mode files | ✅ | ✅ — L74, wording matches the citation |
| 2 | HL §7.2 #6 | `KNOWLEDGE.md` D54 — adapter parity is behavioural | ✅ | ✅ |
| 3 | HL §7.2 #7 | `KNOWLEDGE.md` D28 — one name, one behaviour | ✅ | ✅ |
| 4 | HL §7.2 #14 | `knowledge/philosophy.md` F21 — explicit N/A | ✅ | ✅ |
| 5 | HL §7.2 #18 | `knowledge/process.md` F19 — the Step 0 anomaly | ✅ | ✅ — L26, and now historical (RF obs. 3) |
| 6 | HL §7.2 #19 | `TECH_DEBT.md` TD-106 | ✅ | ✅ — L22, closed by this task |
| 7 | HL §7.2 #21 | `conventions.md` §14 anti-patterns registry | ✅ | ✅ |
| 8 | HL §7.2 #23-25 | External — Gawande Do-Confirm; 5-9 checklist band; LLM-judge dilution/order sensitivity | ✅ | ✅ — sourced to RES iter1 `2_gather` G7, present in that file |

Total citations: 26 · sampled: 8 · verified: 8 · hallucinations: **0**.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files and recorded findings? *24 of 24 — 100%, escalated on V-D1.*
- [x] Ran at least 1 build/test command (or documented why not)? *`pytest docs/scripts/` → 68 passed, plus the grep gate and five parity diffs.*
- [x] Claim & Source Checks filled — 2-3 key claims spot-checked, every citation traced to a real artifact, data claims checked against a primary source (or explicit N/A with a reason)? *Seven checks, C1-C7; C6 partially verified and marked as such.*
- [x] Each RF §3 (AC) checkmark verified against actual file? *All twelve.*
- [x] KNOWLEDGE.md checked — contradictions with changes documented? *D42 and the Legacy row are now stale — the RF reports both (obs. 4) and routes them to `/tfw-docs`. No undocumented contradiction.*
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist)?
  - Total citations: 26, verified: 8 sampled, hallucinations: 0
- [x] Evidence artifacts from RF §5 verified (files exist, claims match)?
  - Total evidence items: 16, verified: 16, missing: 0

Stage complete: YES
