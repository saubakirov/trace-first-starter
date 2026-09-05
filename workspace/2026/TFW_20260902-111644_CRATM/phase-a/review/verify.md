# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed: 7 VALUE files
> Files to verify: ceil(7 x 0.42) = 3; escalated to 7/7 after the first discrepancy

## Verification Log

### V1: `.tfw/conventions.md`
- **RF claim:** One canonical body defines the worktree lifecycle, exact-path staging, cross-session landing, and three matching anti-patterns.
- **Actual:** Unique headings `Worktrees for concurrent mutation`, `Exact-path staging`, and `Landing a deliverable across sessions` contain the promised lifecycle, staging, attribution, history, and exact-Candidate rules. Section 14 contains the three matching failure rows. The worktree rule expressly disclaims locking, serialization, branch policy, and merge strategy.
- **Match:** ✅

### V2: `.tfw/workflows/handoff.md`
- **RF claim:** The Executor checkpoint carries a short enforcement edge while preserving ONB -> implementation/test -> Candidate -> EV/RF order.
- **Actual:** The read and execution order is unchanged; the added edge requires full status, cached-name inspection, explicit paths, `commit --only`, and a foreign-hunk STOP. The body remains a checkpoint edge rather than a duplicate of canon.
- **Match:** ✅

### V3: `.tfw/workflows/review.md`
- **RF claim:** The Reviewer checkpoint independently checks worktree/landing history and exact-path staging without disturbing accounting or the Purpose Check.
- **Actual:** The added Verify-stage edge requires full status, index inspection, literal review-path staging, landing/path-history inspection, and exact Candidate reachability. Independent accounting remains before review stages and the Purpose Check remains in Judge.
- **Match:** ✅

### V4: `.agent/workflows/tfw-handoff.md`
- **RF claim:** Tracked Handoff copy is byte-identical to canon.
- **Actual:** Git blob id `9f24b5c5a34d2c35be5629d0ec1c9be6337ff4ac`, identical to `.tfw/workflows/handoff.md` and the Claude copy; working-tree SHA-256 also matches.
- **Match:** ✅

### V5: `.agent/workflows/tfw-review.md`
- **RF claim:** Tracked Review copy is byte-identical to canon.
- **Actual:** Git blob id `e84d551c14248265c18e4d555f0268b73c8d6afb`, identical to `.tfw/workflows/review.md` and the Claude copy; working-tree SHA-256 also matches.
- **Match:** ✅

### V6: `.claude/commands/tfw-handoff.md`
- **RF claim:** Tracked Handoff copy is byte-identical to canon.
- **Actual:** Git blob id `9f24b5c5a34d2c35be5629d0ec1c9be6337ff4ac`, identical to the canonical and `.agent` Handoff files.
- **Match:** ✅

### V7: `.claude/commands/tfw-review.md`
- **RF claim:** Tracked Review copy is byte-identical to canon.
- **Actual:** Git blob id `e84d551c14248265c18e4d555f0268b73c8d6afb`, identical to the canonical and `.agent` Review files.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `git status --short --branch`; ancestry/object checks for Baseline, approval, Candidate, TRACE and `87c26bb…` | Review-ready HEAD is `71e2589…`; Baseline -> approval -> Candidate -> TRACE holds; `87c26bb…` is not an ancestor. |
| 2 | NUL-safe `git diff --name-status --find-renames=50% -z Baseline Candidate -- <7 literals>` | Seven records, all `M`, and exactly the seven immutable VALUE paths. |
| 3 | Identical NUL-safe `git diff --numstat ...` replay | `7/1, 6/0, 7/1, 6/0, 58/14, 7/1, 6/0`; totals 97 additions, 17 deletions, 114 touched LOC; no binary record. |
| 4 | `git rev-parse`/`git ls-tree` for the governing TS at approval, Candidate, and HEAD | Governing TS blob stays `0d90b1ddf029d0506c40445577bce8233fad9c7a`; approval and denominator are immutable. |
| 5 | `git diff --check Baseline Candidate -- <7 literals>` | Exit 0. |
| 6 | `python .tfw/scripts/gen_index.py --check project` | Exit 0: project is consistent with the declared release. |
| 7 | `python -m pytest docs/scripts/test_runtime_context.py::test_phase_c_every_changed_path_and_active_corpus_clear_thirty_percent docs/scripts/test_runtime_context.py::test_vbsa_plan_loads_three_unique_canonical_sections_with_d75_intact` | Independent Reviewer run: 2 passed in 26.31 s. |
| 8 | `python -m pytest docs/scripts` | Independent Reviewer run: 306 passed in 284.11 s. |
| 9 | Blob-id and SHA-256 comparison of canonical Handoff/Review files and four literal tracked copies | Both three-file groups are byte-identical. |
| 10 | Immutable-ref `\S+` word counts for Baseline and Candidate | `conventions.md` 9,791 -> 10,179 (+388); `handoff.md` 2,013 -> 2,088 (+75); `review.md` 2,102 -> 2,187 (+85). |
| 11 | `git log`, `git diff Candidate HEAD -- <7 literals>`, and Candidate subject/path inspection | Candidate is the first post-approval VALUE commit; no later VALUE write exists; subject and all seven paths match the TS. |
| 12 | Temporary two-file Git fixture with unrelated `sibling.md` staged and `git commit --only -- selected.md` | Independent Reviewer fixture committed only `selected.md` and left `sibling.md` staged. |
| 13 | Initial fixture setup using `New-Item -LiteralPath` | Verification harness error only: this PowerShell exposes no such `New-Item` parameter; no fixture directory was created. Repeated with `-Path` in command 12 and passed. |
| 14 | Resolution of every explicit Markdown target in both HL §7.2 tables | 25/25 explicit file targets and anchors resolve. Inherited `same` rows and all 49 exact item identities were then inspected at source. |
| 15 | `git show`/`git ls-tree`/path history for `87c26bb…` | Mechanical tree and Candidate ancestry are real, but the commit has no `REVIEW__*` or `review/**`, was made at lifecycle RF, and is absent from current lineage. It is not a qualifying post-review landing. |
| 16 | Executor task transcript: full-status/cached-name/Candidate command, fixture, targeted tests, full suite | Exact seven-path staging and `commit --only` are recorded; targeted tests passed 2/2, final pre-Candidate suite passed 306/306, and the Candidate was committed afterwards. |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | `7` logical files and `97 + 17 = 114` touched LOC against immutable `7/160` | RF §§1, 4; EV E-accounting | Raw NUL-delimited Git output between exact Baseline `11888e…` and Candidate `e3f3b3c…`, plus the approval-tree TS blob | ✅ |
| C2 | D75 gates and the final full suite pass after the compacting repair | RF §4; EV E5 | Independent targeted 2/2 and full 306/306 runs; Executor transcript places its own final 306/306 before Candidate | ✅ |
| C3 | Actual coordinator landing is still deferred and must occur after review | RF §§2, 5; EV E3b | Current ancestry, phase lifecycle, canonical protocol, and historical `87c26bb…` tree/history | ✅ as a deferred fact; ❌ as support for RF §3's completed AC-3 checkmark |

All 49 HL source items and their 49 ONB applications were traced to live artifacts. The detailed results are recorded below; the only source defects are the two stale Master-HL NS2 ordinals.

## Discrepancies Found

1. **Material AC-3 gap:** RF §3 checks AC-3 complete, but EV E3b accurately says the required actual post-review landing and cleanup-precondition verification are `DEFERRED`. No qualifying landing is reachable from review-ready HEAD. Historical commit `87c26bb…` cannot satisfy the gate: it predates REVIEW, contains no review artifact, and is not on the current lineage. This is a closed, same-TS return item rather than a new implementation bound.
2. **Master HL citation #2:** it labels the quoted “Human authority, bounded delegation” clause as NS2 principle 4; the live clause is principle 5. ONB #2 already identifies the drift.
3. **Master HL citation #4:** it labels “Assurance proportional to risk” as NS2 principle 6; the live clause is principle 7. ONB #4 already identifies the drift.

Because discrepancy 1 was found during Map, verification was expanded to all seven claimed VALUE files. No additional implementation or accounting discrepancy was found.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | EV E1 / canonical worktree protocol and real worktree facts | ✅ | ✅ — all six lifecycle answers and the no-lock/no-merge boundary are present. |
| E2 | EV E2 / exact-path rules, Candidate staging trace, temporary fixture | ✅ | ✅ — source text, Executor transcript, and an independent Reviewer fixture agree. |
| E3a | EV E3a / canonical landing rule and Candidate history | ✅ | ✅ — subject, path history, exact Candidate object, and reachability rules are real. |
| E3b | EV E3b / actual crossing landing | ✅ | ✅ — the `DEFERRED` status is honest and current; it does **not** satisfy AC-3's completion gate. |
| E4 | EV E4 / ordering, parity, structure | ✅ | ✅ — ordering is preserved, both copy groups are byte-identical, and structural checks pass. |
| E5 | EV E5 / frozen surface, word counts, D75 and full tests | ✅ | ✅ — immutable-ref counts and independent tests reproduce the evidence. The added checkpoint edges are materially necessary because selective role paths do not otherwise load the canonical body. |
| E-accounting | EV E-accounting / approval, Baseline, Candidate and NUL-safe replay | ✅ | ✅ — all SHAs, immutable blob, literal membership, arithmetic, trigger disposition, timing, and authority result reproduce exactly. |

Evidence artifact verdict: all 7 rows exist and accurately report their status; 6 are `VERIFIED`, 1 is accurately `DEFERRED`, and none is missing or blocked.

## Knowledge Citations Verified

Each row below covers both the named HL citation and its corresponding ONB §7 application. “Resolves” includes explicit links, inherited `same` references, and literal repository paths.

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | Master #1 + ONB #1 | PV0 NS1 purpose | ✅ | ✅ | ✅ | ✅ |
| 2 | Master #2 + ONB #2 | PV0 NS2 “Human authority, bounded delegation”, claimed principle 4 | ✅ | ✅ | ❌ — quoted clause is live principle 5; ONB corrects it | ✅ |
| 3 | Master #3 + ONB #3 | PV0 NS3 vendor-bound non-goal | ✅ | ✅ | ✅ | ✅ |
| 4 | Master #4 + ONB #4 | PV0 NS2 “Assurance proportional to risk”, claimed principle 6 | ✅ | ✅ | ❌ — quoted clause is live principle 7; ONB corrects it | ✅ |
| 5 | Master #5 + ONB #5 | PV1 Structural Enforcement | ✅ | ✅ | ✅ | ✅ |
| 6 | Master #6 + ONB #6 | PV1 Naming Creates Behavior | ✅ | ✅ | ✅ | ✅ |
| 7 | Master #7 + ONB #7 | PV1 Portability | ✅ | ✅ | ✅ | ✅ |
| 8 | Master #8 + ONB #8 | PV2 philosophy F37 | ✅ | ✅ | ✅ | ✅ |
| 9 | Master #9 + ONB #9 | PV2 philosophy F38 | ✅ | ✅ | ✅ | ✅ |
| 10 | Master #10 + ONB #10 | PV3 D59 | ✅ | ✅ | ✅ | ✅ |
| 11 | Master #11 + ONB #11 | PV3 D68 | ✅ | ✅ | ✅ | ✅ |
| 12 | Master #12 + ONB #12 | PV3 D63 | ✅ | ✅ | ✅ | ✅ |
| 13 | Master #13 + ONB #13 | PV3 D64 | ✅ | ✅ | ✅ | ✅ — implementation N/A is justified; review applies it directly |
| 14 | Master #14 + ONB #14 | PV3 D55 | ✅ | ✅ | ✅ | ✅ |
| 15 | Master #15 + ONB #15 | PV3 D54 | ✅ | ✅ | ✅ | ✅ |
| 16 | Master #16 + ONB #16 | PV3 D31 | ✅ | ✅ | ✅ | ✅ |
| 17 | Master #17 + ONB #17 | PV4 conventions §3 rules 17–19 | ✅ | ✅ | ✅ | ✅ |
| 18 | Master #18 + ONB #18 | PV4 conventions §3 rules 20–21 | ✅ | ✅ | ✅ | ✅ |
| 19 | Master #19 + ONB #19 | PV4 conventions §14 | ✅ | ✅ | ✅ | ✅ |
| 20 | Master #20 + ONB #20 | PV5 convention F19 | ✅ | ✅ | ✅ | ✅ |
| 21 | Master #21 + ONB #21 | PV6 process F6 | ✅ | ✅ | ✅ | ✅ |
| 22 | Master #22 + ONB #22 | PV6 process F30 | ✅ | ✅ | ✅ | ✅ |
| 23 | Master #23 + ONB #23 | PV6 process F7 | ✅ | ✅ | ✅ | ✅ |
| 24 | Master #24 + ONB #24 | PV7 constraint F11 | ✅ | ✅ | ✅ | ✅ — Phase A N/A is correctly bounded |
| 25 | Master #25 + ONB #25 | PV7 constraint F12 | ✅ | ✅ | ✅ | ✅ |
| 26 | Master #26 + ONB #26 | PV7 constraint F2 | ✅ | ✅ | ✅ | ✅ |
| 27 | Master #27 + ONB #27 | PV7 risk F1 | ✅ | ✅ | ✅ | ✅ |
| 28 | Master #28 + ONB #28 | PV7 stakeholder F6 | ✅ | ✅ | ✅ | ✅ |
| 29 | Master #29 + ONB #29 | PV7 stakeholder F7 | ✅ | ✅ | ✅ | ✅ |
| 30 | Master #30 + ONB #30 | PV7 stakeholder F8 | ✅ | ✅ | ✅ | ✅ |
| 31 | Master #31 + ONB #31 | PV7 environment F3/F4 | ✅ | ✅ | ✅ | ✅ |
| 32 | Master #32 + ONB #32 | PV7 Assisted `team/README.md` | ✅ | ✅ | ✅ | ✅ — Phase A N/A is correctly bounded |
| 33 | Master #33 + ONB #33 | PV3 D68 opaque event token | ✅ | ✅ | ✅ | ✅ |
| 34 | Master #34 + ONB #34 | PV3 D73 | ✅ | ✅ | ✅ | ✅ |
| 35 | Master #35 + ONB #35 | PV3 D74/D75 | ✅ | ✅ | ✅ | ✅ |
| 36 | Master #36 + ONB #36 | PV6 process F39 | ✅ | ✅ | ✅ | ✅ |
| 37 | Phase A1 + ONB #37 | PV0 NS3 vendor-bound non-goal | ✅ | ✅ | ✅ | ✅ |
| 38 | Phase A2 + ONB #38 | PV1 Structural Enforcement | ✅ | ✅ | ✅ | ✅ |
| 39 | Phase A3 + ONB #39 | PV3 D55 | ✅ | ✅ | ✅ | ✅ |
| 40 | Phase A4 + ONB #40 | PV3 D59 | ✅ | ✅ | ✅ | ✅ |
| 41 | Phase A5 + ONB #41 | PV3 D68 | ✅ | ✅ | ✅ | ✅ |
| 42 | Phase A6 + ONB #42 | PV7 risk F1 | ✅ | ✅ | ✅ | ✅ |
| 43 | Phase A7 + ONB #43 | PV7 environment F3/F4 | ✅ | ✅ | ✅ | ✅ |
| 44 | Phase A8 + ONB #44 | PV6 process F30 | ✅ | ✅ | ✅ | ✅ |
| 45 | Phase A9 + ONB #45 | PV7 constraint F2 | ✅ | ✅ | ✅ | ✅ |
| 46 | Phase A10 + ONB #46 | PV3 D73 | ✅ | ✅ | ✅ | ✅ |
| 47 | Phase A11 + ONB #47 | PV3 D74/D75 | ✅ | ✅ | ✅ | ✅ |
| 48 | Phase A12 + ONB #48 | PV4 conventions `Design Rules` | ✅ | ✅ | ✅ | ✅ |
| 49 | Phase A13 + ONB #49 | PV6 process F39 | ✅ | ✅ | ✅ | ✅ |

The two failures above belong only to Master HL citations #2 and #4. Their matching ONB rows are semantically correct because they explicitly record the live ordinals.

## Checkpoint

**Self-check:**
- [x] Opened >= ceil(7 x 0.42) files and recorded findings? 7/7 opened after escalation.
- [x] Ran at least 1 build/test command (or documented why not)? Targeted 2/2 and full 306/306 passed independently.
- [x] Claim & Source Checks filled — 3 key claims spot-checked, every citation traced, and numeric claims checked against primary Git/test output?
- [x] Each RF §3 (AC) checkmark verified against actual file? AC-3 completion discrepancy recorded.
- [x] KNOWLEDGE.md checked — contradictions with changes documented? No implementation contradiction; D75 gates pass.
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total artifact-citation occurrences: 98; resolved: 98; semantically/exactly verified: 96; irrelevant: 0; hallucinated: 0.
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 7; artifact/status claims verified: 7; missing: 0. Outcome counts remain 6 VERIFIED / 1 DEFERRED.

Stage complete: YES
