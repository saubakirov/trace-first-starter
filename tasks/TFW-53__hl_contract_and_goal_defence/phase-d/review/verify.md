# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: **0.42** (`project_config.yaml` → `tfw.review.min_verify_ratio`)
> RF files claimed: **33** (28 modified, 5 new; RF trace excluded, following prior TFW-53 review counting)
> Files to verify: ⌈33 × 0.42⌉ = **14** → escalated to **33 of 33 (100%)** on discrepancy D1

## Verification Log

### V1: `.tfw/glossary.md`
- **RF claim:** ten articles exist in the required locations, each body is 41–50 words, each has a governing-rule pointer, and the retired terminology is gone.
- **Actual:** all ten headings and bodies are present. Independent section parsing reproduces body counts `48, 49, 50, 50, 45, 48, 48, 43, 41, 49`; every section contains `→`. `frozen baseline` is absent outside CHANGELOG, non-negated `committed baseline` is absent, and the two former template-field occurrences now read `Project North Star`.
- **Match:** ✅

### V2: `.tfw/conventions.md`, `.tfw/templates/HL.md`, `.tfw/templates/review/judge.md`, `.tfw/workflows/review.md`
- **RF claim:** canonical-term substitutions only, plus TD-164's command-copy removal; no workflow growth.
- **Actual:** every changed line is either a `Contract Baseline` / `Project North Star` substitution or the named TD-164 pointer fix. `plan.md` is unchanged at 1,195 words; `review.md` remains 1,176 words. The HL template no longer contains the recovery command and points to `conventions.md` §3 rule 15.
- **Match:** ✅

### V3: `.tfw/compilable_contract.md`
- **RF claim:** remove the stale `KNOWLEDGE.md` §0 source location and add `PP{N}` / `NS{N}` to the declared resolution rules, while filing the implementation gap separately.
- **Actual:** both two-line changes are present. `docs/scripts/gen_docs.py` still resolves only `D{N}` and `TD-{N}` links; the wider mismatch is accurately registered as TD-170 rather than hidden.
- **Match:** ✅

### V4: fourteen changed full-copy adapters and all adapter pairs
- **RF claim:** the parent tree had fourteen drifted copies; after the sync all twenty-two full-copy pairs are byte-identical, and source direction was checked before copying.
- **Actual:** blob-ID comparison at `ce30f3b^` reproduces exactly fourteen mismatches, naming the same seven workflows in both copy folders. Blob IDs at `ce30f3b` and current SHA-256 checks reproduce **0 mismatches across 22 pairs**. The seven unique parent diffs were opened: every adapter-only line is an older form of a source-side line in the same hunk; no adapter-only mechanism was merged into the canonical source.
- **Match:** ✅

### V5: Codex routers
- **RF claim:** all source/installed skill pairs are identical; only the false word `approved` was removed from the plan router, while the review router stayed unchanged.
- **Actual:** all eleven source/installed Codex skill pairs have matching SHA-256 hashes. Commit `ce30f3b` changes only the two plan-router copies and removes exactly that word. The review router remains a thin, truthful pointer to the canonical workflow.
- **Match:** ✅

### V6: `CLAUDE.md` and `AGENTS.md`
- **RF claim:** two purpose cells corrected and two explicitly authorized rows added to `CLAUDE.md`; `AGENTS.md` unchanged because its routing table contains no false description.
- **Actual:** the commit contains exactly the four claimed `CLAUDE.md` edits and no new section. `AGENTS.md` has no Phase D diff and its table routes all eleven commands to the canonical workflows.
- **Match:** ✅

### V7: `.tfw/VERSION`, `.tfw/project_config.yaml`, `.tfw/CHANGELOG.md`
- **RF claim:** release 1.2.0, lockstep version markers, one A–D changelog entry, corrected fourteen-copy statement, and a TFW-54 pointer.
- **Actual:** both version carriers read `1.2.0`; `TFW-54` occurs in the 1.2.0 entry; the stale `12 drifted copies` text is absent and the entry says fourteen copies were repaired. Git history verifies **8 of 8 releases from 0.8.5 through 1.2.0** kept VERSION and `tfw.version` equal.
- **Match:** ✅

### V8: `TECH_DEBT.md`
- **RF claim:** TD-157, TD-163, TD-164, TD-165 and TD-167 closed with reasons; TD-131 and TD-158 re-routed; TD-170 filed.
- **Actual:** every row exists with the claimed disposition and reasoning. TD-163's pointer defect is closed, but its separate ~50-word duplication remains open only in prose inside the closed row and RF observation 1; it needs its own open registry row during review triage. TD-133 is now orphaned and its residual is subsumed by TD-170, as RF observation 4 states.
- **Match:** ⚠️ implementation claims hold; registry follow-up required

### V9: `README.md`
- **RF claim:** the complete Phase D board row was written but left unstaged to preserve concurrent TFW-55 work.
- **Actual:** the working-tree diff contains exactly the Phase D additions to the TFW-53 row plus the unrelated TFW-55 row change. Nothing is staged. The file must remain a path-specific edit.
- **Match:** ✅

### V10: five new evidence files
- **RF claim:** EV plus four supporting captures exist and contain the stated term, adapter, release and test outputs.
- **Actual:** all five files exist and were opened. The before capture lists fourteen drift lines; the after capture is silent with exit 0; the direction file lists the same fourteen pairs; the gate file carries the term counts, body counts, word budgets, release gates and historical 68-test result.
- **Match:** ✅ for existence and most claims; see D1–D2 for two overclaims inside EV

### V11: scope-budget claim
- **RF claim:** `28 modified`, `5 new`, “against 30 / 15”; EV E19 says one new artifact folder matches the TS estimate exactly.
- **Actual:** excluding the RF trace, the phase changed **33 files: 28 modified + 5 new**. Config carries three independent limits: total files **30**, modified files **30**, new files **15**. Modified and new limits hold; total-file limit is exceeded by **3**. The approved TS estimated `28 modified + 1 new = 29`; the four additional evidence captures were not included and no explicit owner override was recorded.
- **Match:** ❌ — D1

### V12: AC-7 hunk ledger
- **RF claim:** `git diff -U0` yielded twelve hunks: eight substitutions, four named debt fixes, plus glossary additions.
- **Actual:** the stated command yields **16 hunk headers**; the default-context diff yields 14. The semantic line ledger contains eleven canonical-term substitutions, four named debt fixes and two glossary addition sites, with some adjacent changes sharing one hunk. All actual changes remain inside the permitted categories, but RF §3, RF §9 and EV E17 report false counts.
- **Match:** ❌ — D2

### V13: RF §7–§9 quality
- **RF claim:** five Fact Candidates and four Strategic Insights are suitable knowledge inputs; diagrams explain the implementation.
- **Actual:** the diagrams are relevant and accurate. In §7, only FC3 is human-sourced; FC1, FC2, FC4 and FC5 are discoverable from artifacts or commands and fail the RF template's Human-Only Test. All four §8 items derive from coordinator/executor analysis rather than user-provided domain knowledge and fail §8's Human-Only Test; they belong in observations/analysis or the section should state `No strategic insights.`
- **Match:** ❌ — D3

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python -m pytest docs/scripts/` | ✅ **68 passed in 41.47s**, exit 0 |
| 2 | SHA-256 comparison of 22 canonical workflow/copy pairs | ✅ 22 pairs, 0 mismatches |
| 3 | SHA-256 comparison of 11 Codex source/installed skill pairs | ✅ 11 pairs, 0 mismatches |
| 4 | Parent/commit blob-ID comparison for all 22 full-copy pairs | ✅ parent: 14 mismatches; `ce30f3b`: 0 |
| 5 | Independent glossary term, body-word and pointer checks | ✅ 10/10 present, 41–50 body words, 10/10 pointers |
| 6 | Retired-form sweep across `.tfw/**/*.md`, excluding CHANGELOG | ✅ `frozen baseline` 0; non-negated `committed baseline` 0; two genuine bare-capital forms removed |
| 7 | VERSION/config/changelog gates plus release-history comparison | ✅ 1.2.0 in both carriers; TFW-54 present; 8/8 historical releases lockstep |
| 8 | `git diff --check ce30f3b^ ce30f3b` and secret-pattern scan | ✅ no whitespace errors; no credential-like assignments |
| 9 | Phase file-count reconstruction from `ce30f3b` plus unstaged README | ❌ 33 total against 30, although 28 modified and 5 new separately remain within their limits |
| 10 | `git diff -U0` hunk count on the six framework files | ❌ 16, not the RF/EV claim of 12 |
| 11 | Canonical Bash drift snippet through the available WSL `bash` | Not used — Windows stdin/line mediation produced a parse error; byte-hash and blob-ID comparisons above independently establish parity |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | “Ten articles, all at or below 50 words, each pointing to its rule” | RF §1/§3; EV E1–E4 | `.tfw/glossary.md`, governing sections in conventions/judge | ✅ |
| C2 | “14 drifted pairs before, 0 of 22 after; no copy was ahead” | RF §2 D5/§3/§4; EV E9–E11 | parent and commit blob IDs; seven unique parent diffs; current SHA-256 hashes | ✅ |
| C3 | “VERSION and `tfw.version` have moved in lockstep since 0.8.5” | TS AC-5; RF §2/§3; source `RF TFW-56 FC2` | Git history for eight release commits, plus the cited RF row | ✅ |
| C4 | “28 modified + 5 new is within 30 / 15” | RF §4; EV E19 | commit diff, README working-tree diff, `project_config.yaml` scope budgets | ❌ — ignores the independent 30-file total limit |
| C5 | “Twelve `-U0` hunks, eight substitutions” | RF §3/§9; EV E17 | `git diff -U0 ce30f3b^ ce30f3b` | ❌ — 16 hunk headers; eleven canonical substitutions |
| C6 | RF citations and task references | RF throughout | `KNOWLEDGE.md` D28/D48/D53/D61/D62; `RF TFW-56` FC2; TFW-42/C and TFW-46/C RFs; TFW-57 proposal; TD-131/133/157/158/163/164/165/167/170 | ✅ all resolve and support the nearby statements |

## Discrepancies Found

1. **D1 — unapproved total-file budget overrun.** Actual scope is 33 files against `max_files_per_phase: 30`; RF and EV compare only the modified/new sub-limits and call the result green.
2. **D2 — false diff-ledger evidence.** `git diff -U0` returns 16 hunk headers, not 12, and the semantic substitution count is eleven, not eight. The underlying changes are compliant; the recorded gate is not.
3. **D3 — knowledge sections fail their own admission test.** Four of five Fact Candidates and all four Strategic Insights are agent-discoverable or agent-generated rather than human-sourced.

The first discrepancy triggered 100% verification of all 33 claimed files. No additional implementation discrepancy was found.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1–E16 | EV rows E1–E16 and four attachments | ✅ | ✅ — independently reproduced or traced |
| E17 | AC-7 hunk review | ✅ | ❌ — actual `-U0` count is 16, not 12; classification result still holds |
| E18 | Six-file diffstat | ✅ | ✅ — `47 insertions, 15 deletions` reproduced |
| E19 | Scope budget | ✅ | ❌ — 33 total files exceed the 30-file limit by 3; new/modified sub-limits alone are not the whole budget |

Total evidence items: **19**; verified: **17**; overclaimed: **2**; missing: **0**. The EV verdict `19/19 VERIFIED` is not supported.

## Knowledge Citations Verified

> ONB §7 carries the 26 HL §7.2 items plus four new items N1–N4. Every referenced record was checked for existence and relevance in its named file.

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | HL §7.2 / ONB §7 | `.tfw/README.md` § Structural Enforcement, § Naming Creates Behavior, § Candor Over Flattery | ✅ | ✅ all three |
| 2 | HL §7.2 / ONB §7 | `KNOWLEDGE.md` D19, D20, D23, D24, D31, D43, D46, D49, D54, D55 | ✅ | ✅ all ten |
| 3 | ONB §7 N1–N3 | `KNOWLEDGE.md` D53, D62, D61 | ✅ | ✅ all three |
| 4 | HL §7.2 / ONB §7 | `knowledge/philosophy.md` F4, F13, F21, F22, F25 | ✅ | ✅ all five |
| 5 | HL §7.2 / ONB §7 | `knowledge/process.md` F4, F6, F11, F14, F20 | ✅ | ✅ all five |
| 6 | HL §7.2 / ONB §7 | `knowledge/constraint.md` F2 | ✅ | ✅ |
| 7 | HL §7.2 / ONB §7 | `conventions.md` §7, §15 | ✅ | ✅ both |
| 8 | ONB §7 N4 | `conventions.md` §14 review-vs-contract anti-pattern | ✅ | ✅ |

Total unique citations: **30**, verified: **30**, hallucinations: **0**.

**KNOWLEDGE.md contradiction check.** D28/D54 support the naming and behavioral-parity changes; D61 requires the separate evidence-sufficiency judgment that exposes E17/E19. No implementation decision contradicts KNOWLEDGE.md. The unresolved total-file overrun conflicts with `conventions.md` §6 and cannot be converted into compliance by the executor's own count.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files and recorded findings? — **33 of 33**, escalated to 100% on D1
- [x] Ran at least 1 build/test command (or documented why not)? — pytest re-run, 68 passed; ten verification command groups logged
- [x] Claim & Source Checks filled — three key claims independently tested, all cited references traced, two numeric overclaims flagged
- [x] Each RF §3 (AC) checkmark verified against actual file? — all seven functional AC outcomes hold; scope-budget and RF-quality defects are separately recorded
- [x] KNOWLEDGE.md checked — contradictions with changes documented? — none in implementation; budget conflict documented against conventions
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist)?
  - Total unique citations: **30**, verified: **30**, hallucinations: **0**
- [x] Evidence artifacts from RF §5 verified (files exist, claims match)?
  - Total evidence items: **19**, verified: **17**, overclaimed: **2**, missing: **0**

Stage complete: YES

---

# Verify — second pass (corrective, 2026-08-18)

> Corrective files: **5** across coordinator and executor commits (`TS`, `CLAUDE.md`, `TECH_DEBT.md`,
> `RF`, `EV`). Minimum at 0.42: 3. Opened: **5 of 5 (100%)**.

## Corrective Verification Log

### V14: corrective scope and role boundaries
- **Claim:** only the trace and two entry-point links changed; the framework implementation was not reopened.
- **Actual:** coordinator commit `3d89b59` changes only the TS. Executor commit `2e60934` changes only
  `CLAUDE.md`, `TECH_DEBT.md`, RF and EV. `CLAUDE.md` has exactly two case corrections; no workflow,
  adapter, glossary, template, version or changelog file changed after `ce30f3b`.
- **Match:** ✅

### V15: AC-8 budget under the owner's governing subject
- **Claim:** the phase is within the 30-file product budget.
- **Actual:** `git diff --name-status ce30f3b^ ce30f3b` gives **27 modified** and **6 added** files. The
  six additions are RF, EV and four captures. The owner clarified on 2026-08-18 that `README.md` is a TFW
  process artifact, not an executor-derived product file, and is not counted. Governing result:
  **27 product files of 30; 0 new product files; 6 trace files**.
- **Match:** ✅. RF/EV's 28 is a conservative overcount made before the clarification; it cannot hide an
  overrun because even that count is below 30. TD-173 correctly keeps the general rule-encoding work open.

### V16: AC-9 reproducible ledger
- **Claim:** 16 `-U0` hunk headers, 11 substituted lines, 4 debt fixes and 2 addition sites.
- **Actual:** independent per-file recount is `2 + 4 + 4 + 2 + 2 + 2 = 16`. The two-line Judge hunk makes
  10 substitution hunks carry 11 substituted lines. Default context gives 14, and `--stat` gives
  47 insertions / 15 deletions.
- **Match:** ✅; D2 discharged.

### V17: AC-10 knowledge admission and re-homing
- **Claim:** only the human-sourced FC remains; no agent analysis remains in Strategic Insights.
- **Actual:** §7 has one owner-sourced row. §8 says `No strategic insights.` S3 is in §2 decision 11;
  S4, S2's operative half and FC5 are observations 8–10. S1/FC1/FC2/FC4 are removed with reasons.
  TD-174 reproduces the RF/REVIEW/RES template contradiction.
- **Match:** ✅; D3 discharged.

### V18: AC-11 entry-point compatibility
- **Claim:** both retired uppercase links are fixed and no live counterpart remains.
- **Actual:** `PROJECT_CONFIG` has 0 matches in `CLAUDE.md` and `AGENTS.md`; both links resolve to the
  existing `.tfw/project_config.yaml`. Commit `2e60934` changes no other `CLAUDE.md` line. TD-172 records
  the closure and owner-authorized scope extension.
- **Match:** ✅

### V19: AC-12 evidence recomputation
- **Claim:** evidence was recomputed rather than restored.
- **Actual:** EV has **26 uniquely identified rows**. E17 and E19 are replacements; E17b, E19b and
  E20–E24 are seven additions; 19 + 7 = 26. RF §5 and EV both state 26/26. E20's 28-file classification
  is superseded by the owner's later README ruling, but the row remains a conservative proof that the
  limit is not exceeded. RF §1's “19 rows” label and RF §3 AC-12's `19/19` / “five” are stale summaries,
  not the verdict source.
- **Match:** ✅ for the acceptance claim and implementation evidence; two non-material summary labels
  retained under the owner's explicit materiality ruling.

### V20: carried implementation gates
- **Tests:** `python -m pytest docs/scripts/` → **68 passed in 34.47s**.
- **Full-copy parity:** SHA-256 comparison → **22/22 match**.
- **Codex source/installed parity:** SHA-256 comparison → **11/11 match**.
- **Whitespace:** `git diff --check ce30f3b..2e60934` and current `git diff --check` → clean.
- **Match:** ✅

## Second-pass Evidence Verification

| Evidence set | Exists? | Establishes the material claim? |
|---|---:|---:|
| E1–E16, E18 | ✅ | ✅ — carried from the first pass and independently verified there |
| E17, E17b | ✅ | ✅ — 16 headers / 11 substituted lines reproduce |
| E19, E19b | ✅ | ✅ — even the conservative 28-file count is under 30; owner-governing count is 27 |
| E20 | ✅ | ⚠️ superseded — its README classification predates the owner's clarification; not needed for the pass conclusion |
| E21–E24 | ✅ | ✅ — re-homing, template debt and link repair were opened and reproduced |

Evidence rows present: **26**. Material acceptance claims established: **all**. No missing artifact and no
unverified implementation claim remains.

## Residuals — explicitly non-blocking

1. TS §4's budget paragraph retains a duplicated `14 of the 28` tail after the corrected 27 count.
2. RF §1 calls the EV “19 rows”; RF §3 AC-12 says `19/19` and five additions, while RF §5/EV correctly
   state 26/26 and seven additions.
3. EV E20 predates the owner's clarification that the Task Board update is a TFW process artifact.

The owner directed this review to judge execution quality and not block on these accounting labels. None
changes a file, behavior, test, adapter, release marker or evidence conclusion.

## Checkpoint — second pass

- [x] Opened 5/5 corrective files?
- [x] Re-ran an executable test gate?
- [x] Reproduced every first-pass failed claim independently?
- [x] Re-checked evidence existence separately from sufficiency?
- [x] Recorded the owner's current classification and materiality ruling?
- [x] Confirmed no framework mechanism was reopened?

Stage complete: YES
