# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: docs
> Min verify ratio: 0.42
> RF files/artifact rows claimed: 14
> Files to verify: ⌈14 × 0.42⌉ = 6
> Actual verification: 14/14 claimed rows plus every file inside both live-run evidence directories (100%)

## Verification Log

### V1: `editions/README.md`
- **RF claim:** guide covers Light, future Assisted and Full by work characteristics, names Light's limit, has no Team edition and is 473 words.
- **Actual:** opened in full. All three editions, work-based selection, manual Light limits, explicit Phase B availability and absence of `03-team/` are present. PowerShell whitespace count reproduces 473 words; the 600-word ceiling passes.
- **Match:** ✅

### V2: `editions/01-light/README.md`
- **RF claim:** frozen TFW-51 copy with only the copy-contents installation correction.
- **Actual:** full file opened. `git diff --no-index` against TFW-51 shows one changed sentence: copy the directory contents into the project root. The self-contained prompt, working ritual and non-code language remain intact; whitespace count is 468 ≤ 500.
- **Match:** ✅

### V3: `editions/01-light/AGENTS.md`
- **RF claim:** byte-identical TFW-51 behavioral contract.
- **Actual:** SHA-256 is `ECA387FED8DC6AAD0DFFB38067D1721E087E4EEE39E37E53373CD02433DC0358` for both source and copy. The five statuses, trace structure and ≤3-question rule are present; whitespace count is 753 ≤ 900.
- **Match:** ✅

### V4: `editions/01-light/TASKS.md`
- **RF claim:** byte-identical TFW-51 task list.
- **Actual:** SHA-256 is `C99B658F8CDE692FDFDB75334FEA39C7EE8072C1B34F61B02A72BF34E1B7B1B1` for both source and copy. Five statuses and task-folder linkage are unchanged; whitespace count is 183 ≤ 250.
- **Match:** ✅

### V5: `editions/01-light/memory/PROJECT.md`
- **RF claim:** baseline card plus filled active-edition and version fields.
- **Actual:** full file opened. Existing card contains `Активная редакция = TFW Light` and `Версия редакции = 1.0.0`; recursive diff contains only these two rows. Whitespace count is 312 ≤ 400.
- **Match:** ✅

### V6: root `README.md`
- **RF claim:** short Editions entry added without rewriting existing sections; Assisted is not presented as available.
- **Actual:** product commit `07739b5` adds only a 12-line Editions block before `Who TFW Is For`. The block links to `editions/README.md`, instructs copying contents, and says Assisted is planned and not yet available. Existing sections remain. The shared TFW-52 Task Board row is a separate pre-existing uncommitted addition, as RF states.
- **Match:** ✅

### V7: `phase-a/ONB__phase-a__product_line_and_light.md`
- **RF claim:** Coordinator approval recorded.
- **Actual:** opened in full; status is `🟠 ONB — Approved 2026-08-08`, no blocking questions remain, and the product commit changes only the approval status line.
- **Match:** ✅

### V8: EV and deterministic attachments
- **RF claim:** structured EV covers all eight AC; diff, word counts, baseline hashes and verification output support it.
- **Actual:** EV, `diff-vs-tfw51.txt`, both SHA-256 manifests and `verification.txt` opened. Independent commands reproduce the exact four-file topology, the two allowed diffs, all word ceilings, no forbidden directories, empty TFW-51 status, and identical before/after baseline hashes. The executor commit range contains no `.tfw/` or TFW-51 changes.
- **Match:** ✅

### V9: AC-6 live root and evidence copy
- **RF claim:** independent thread `019fe251-0a40-77e1-bc85-c1bbc4d9cd44` completed a clean contradiction-analysis project with 0 questions, no manual structure management, exactly two real contradictions and no invented conflict.
- **Actual:** actual root `D:\projects\research\tfw52-phase-a-runs\run-1-contradictions` exists outside any Git repository. All three inputs, live `TRACE.md`, `contradictions.md`, `TASKS.md` and `memory/PROJECT.md` were opened. The result identifies exactly the seeded HR-data and production-date conflicts, preserves committee approval as aligned and distinguishes two non-conflicting differences. Thread history is completed and proves `TRACE.md` was created before input analysis. Hashes of TASKS, PROJECT, TRACE and result exactly match evidence copies.
- **Match:** ✅

### V10: AC-7 live root and evidence copy
- **RF claim:** independent thread `019fe251-16eb-7461-b4a1-a6d6af38446f` completed a clean handout project with 0 questions, no manual structure management and a ready 20-minute material containing one example, six exercises and six answers.
- **Actual:** actual root `D:\projects\research\tfw52-phase-a-runs\run-2-handout` exists outside any Git repository. Source, live `TRACE.md`, `handout.md`, `TASKS.md` and `memory/PROJECT.md` were opened. The handout has a 4+5+7+4 minute route, one self-contained example, six classification rows and six reasoned answers; it preserves source constraints and adds no external facts. Thread history is completed and proves trace/task initialization before creation of the handout. Hashes of TASKS, PROJECT, TRACE and result exactly match evidence copies.
- **Match:** ✅

### V11: live-run provenance
- **RF claim:** two separate Codex tasks produced actual evidence.
- **Actual:** app thread records resolve to two different completed local threads titled `Evidence | TFW-52/A | AC-6 documents` and `Evidence | TFW-52/A | AC-7 handout`, with distinct roots, prompts, file-change histories and final answers. `tree.txt` in each evidence folder matches the current actual root. Both roots preserve starter README/AGENTS byte-for-byte and contain no `.git`, hooks, `.codex`, Assisted or knowledge artifacts.
- **Match:** ✅

### V12: implementation commits and scope
- **RF claim:** `07739b5`, `f4b9ae9`, `bf47823` contain product, dispatch and live evidence respectively; no push.
- **Actual:** all three commits resolve with correctly attributed subjects and file scopes matching RF. Their combined diff has no `.tfw/` or TFW-51 paths. Remote push state was not needed for acceptance and no push action was taken by this Reviewer.
- **Match:** ✅

## Acceptance Criteria Verification

| AC | Independent result | Proof |
|---|---|---|
| AC-1 | ✅ PASS | V1; all checklist content present; 473 words; current editions tree has no Team folder |
| AC-2 | ✅ PASS | V2–V5, V8; exactly four files; only two permitted content diffs; limits and forbidden-path checks pass |
| AC-3 | ✅ PASS | V2, V9, V10; copy-contents instruction is literal; both real roots use the starter at root; `tfw-light-ru` has 0 matches under `editions/` |
| AC-4 | ✅ PASS | V5; active edition and version are filled in the existing project card |
| AC-5 | ✅ PASS | V6; isolated commit diff adds only the Editions entry and preserves existing README sections |
| AC-6 | ✅ PASS | V9, V11; actual files, source-to-result audit, thread chronology and hashes verified |
| AC-7 | ✅ PASS | V10, V11; actual files, source-to-result audit, thread chronology and hashes verified |
| AC-8 | ✅ PASS | V8, V12; four current hashes match both manifests; `git diff`/`status` for TFW-51 are empty across executor range and current worktree |

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `Get-ChildItem editions -Recurse -Force` | Exact current tree: only `README.md` and `01-light/` with four files |
| 2 | `Get-Content -Raw` for every product, RF/EV and live-run file | All required structure and content opened and inspected |
| 3 | PowerShell whitespace word counts | 473 / 468 / 753 / 183 / 312; every TS ceiling passes |
| 4 | `git diff --no-index TFW-51 editions/01-light` | Only installation sentence and two project-card rows differ |
| 5 | `Get-FileHash -Algorithm SHA256` for baseline, copy, live roots and evidence copies | Baseline manifests match; immutable copies and all eight runtime evidence mappings match |
| 6 | `git status` and executor-range diffs for TFW-51 and `.tfw/` | No changes in either protected scope from Phase A execution |
| 7 | `git show` for `07739b5`, `f4b9ae9`, `bf47823` | Commits and claimed scopes resolve |
| 8 | App thread reads for AC-6 and AC-7 | Separate completed threads, correct roots, chronology and final results verified |
| 9 | `python -m pytest docs/scripts/test_gen_docs.py docs/scripts/test_integration.py -q` | `68 passed in 34.87s` |
| 10 | Local Markdown link and citation target checks | 15/15 HL links resolve; all 17 distinct HL/ONB citation items exist |

## Discrepancies Found

No discrepancies. Verification was nevertheless expanded to 100% because the review delegation explicitly requires all eight AC, both live runs, full evidence provenance, current edition topology and TFW-51 integrity.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|-----------------|-----------------|----------------|
| E1 | `editions/README.md`, `verification.txt` | ✅ | ✅ — direct document gate; N/A matches TS Evidence field |
| E2 | `diff-vs-tfw51.txt` | ✅ | ✅ — independent diff/count/hash checks reproduce it |
| E3 | two live trees, `verification.txt` | ✅ | ✅ — root layout, thread provenance and installation behavior verified |
| E4 | Light `memory/PROJECT.md`, `verification.txt` | ✅ | ✅ — fields exist; N/A matches Phase B runtime gate |
| E5 | root `README.md`, `verification.txt` | ✅ | ✅ — isolated commit diff verifies docs-only gate; N/A valid |
| E6 | run-1 inputs/state/trace/result/tree | ✅ | ✅ — actual root opened; result correct; four runtime hashes match copies |
| E7 | run-2 source/state/trace/result/tree | ✅ | ✅ — actual root opened; result correct; four runtime hashes match copies |
| E8 | before/after baseline manifests | ✅ | ✅ — four hashes match; protected path has no diff/status entries |

## Knowledge Citations Verified

| # | Artifact | Citation | Link resolves? | Item exists? |
|---|----------|----------|----------------|--------------|
| 1 | HL K1 / ONB 1 | `.tfw/README.md` — The Problem / The Thesis | ✅ | ✅ |
| 2 | HL K2 / ONB 2 | `.tfw/README.md` — Structural Enforcement / Naming Creates Behavior | ✅ | ✅ |
| 3 | HL K3 / ONB 3 | `.tfw/README.md` — Candor / Honesty | ✅ | ✅ |
| 4 | HL K4 / ONB 4 | `KNOWLEDGE.md` D22 | ✅ | ✅ |
| 5 | HL K5 / ONB 5 | `KNOWLEDGE.md` D28, D33 | ✅ | ✅ |
| 6 | HL K6 / ONB 6 | `KNOWLEDGE.md` D40, D47 | ✅ | ✅ |
| 7 | HL K7 / ONB 7 | `KNOWLEDGE.md` D56 | ✅ | ✅ |
| 8 | HL K8 / ONB 8 | `knowledge/philosophy.md` F3, F4, F7, F13 | ✅ | ✅ |
| 9 | HL K9 / ONB 9 | `knowledge/process.md` F4, F5, F6 | ✅ | ✅ |
| 10 | HL K10 / ONB 10 | `knowledge/constraint.md` F1, F2, F7 | ✅ | ✅ |
| 11 | HL K11 / ONB 11 | `knowledge/stakeholder.md` F1, F3 | ✅ | ✅ |
| 12 | HL K12 / ONB 12 | HL TFW-51 — four-file baseline and seminar purpose | ✅ | ✅ |
| 13 | HL K13 / ONB 13 | RES iter1 — topology/history/work-based choice/pedagogy | ✅ | ✅ |
| 14 | HL K14 / ONB 14 | RES iter2 — hooks/attribution/shared-folder/risk boundary | ✅ | ✅ |
| 15 | HL K15 / ONB 15 | RES iter3 — stable Team not justified; tasks as carrier | ✅ | ✅ |
| 16 | ONB 16 | `knowledge/process.md` F26 | N/A — plain item ref | ✅ |
| 17 | ONB 17 | `knowledge/constraint.md` F8 | N/A — plain item ref | ✅ |

HL citation links: 15/15 resolved. Citation rows across HL and ONB: 32/32 verified; unique reference groups: 17/17; hallucinations: 0.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files and recorded findings?
- [x] Ran at least 1 build/test command (or documented why not)?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist)?
  - Total citation rows: 32, verified: 32, hallucinations: 0
- [x] Evidence artifacts from RF §5 verified (files exist, claims match)?
  - Total evidence items: 8, verified: 8, missing: 0

Stage complete: YES
