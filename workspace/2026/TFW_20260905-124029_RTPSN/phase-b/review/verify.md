# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42 from `.tfw/project_config.yaml` → `tfw.review.min_verify_ratio`
> RF files claimed: 25 Candidate files (23 VALUE + 2 ASSURANCE)
> Files to verify: ⌈25 × 0.42⌉ = 11; actual verification: 25/25 (100%)

## Verification Log

### V1: `.tfw/conventions.md`
- **RF claim:** Contains the sole 33-word session-identity authority.
- **Actual:** One uniquely resolving `Session identity` range defines U+00B7 spacing, the eight-token WORK vocabulary, task/phase/LEAD resolution, stable-key collision suffix, exact readback, report-once fail-soft behavior, forbidden fallbacks, and state/lineage authority. Its independently measured size is 33 words; no new file or universal preload was added.
- **Match:** ✅

### V2: `.tfw/glossary.md`
- **RF claim:** Replaces the obsolete role/pipe wording with a meaning/authority router.
- **Actual:** `Session Naming` resolves once and points to `conventions.md` → `Session identity`; it contains no copied BASE/WORK/collision/transport algorithm.
- **Match:** ✅

### V3–V9: seven canonical workflows

| # | File | Actual checkpoint and inspected compression result | Match |
|---|---|---|---|
| V3 | `.tfw/workflows/plan.md` | Existing state/lineage resolves before `PLAN`/authorized `LEAD` and before Knowledge/questions/proposals; new-task identity follows approved ID and precedes state/event/HL. Freeze, research, TS, REVISE and STOP gates remain. | ✅ |
| V4 | `.tfw/workflows/research/base.md` | Task/iteration resolves before `RESEARCH` and before write/question/wait/stage; iteration cannot become PHASE. Mode, staged OODA, synthesis and STOP gates remain. | ✅ |
| V5 | `.tfw/workflows/handoff.md` | Legacy pre-state Step 0 is removed; item 1 state resolution precedes `WORK=EXEC` and ONB. ONB, dependency, scope, build, Candidate, evidence, RF and return stops remain. | ✅ |
| V6 | `.tfw/workflows/review.md` | Legacy pre-state Step 0 is removed; Bootstrap item 1 precedes `WORK=REVIEW` and Map. Map/Verify/Judge, Purpose, citation bar, disposition, verdict, KNW routing and hard stop remain. | ✅ |
| V7 | `.tfw/workflows/resume.md` | One task resolves before `RESUME`/authorized `LEAD`; PHASE is included only for one governing phase and identity precedes matrix/question/stop. State/lineage selection and user decision remain. | ✅ |
| V8 | `.tfw/workflows/docs.md` | Auto/manual single-task selection applies `WORK=DOCS` before proposals/writes/questions/stops; batch explicitly skips. Triage, exact proposal, approval, apply and marker routing remain. | ✅ |
| V9 | `.tfw/workflows/init.md` | Full init names the created task after item 4 and before item 5 state/event writes; attach/repair skips. Route-before-discovery, setup, research, verification/RF and close boundaries remain. | ✅ |

### V10–V23: fourteen tracked receiver copies
- **RF claim:** The seven changed Claude and seven singular Antigravity compatibility receivers are byte-exact copies of their canonical workflows.
- **Actual:** Direct three-way byte comparison and the independent integration suite verified each of `plan`, `research`, `handoff`, `review`, `resume`, `docs`, and `init`: canonical = `.claude/commands/tfw-{route}.md` = `.agent/workflows/tfw-{route}.md`. All eleven tracked routes remain exact; only the approved seven per tree changed from Baseline.
- **Match:** ✅

### V24: `docs/scripts/test_runtime_context.py`
- **RF claim:** Adds source-derived semantic projections, 15 scenarios, 16 mode cases, seven independently rejected mutant families, charged graph/corpus checks, copy hashes and protected-span checks.
- **Actual:** The 451-addition/1-deletion diff adds parser/records/CLI and seven Phase-B tests. Live commands produced 15 semantic records and 16 workflow-mode records with all required fields; all seven mutant families changed the produced record and were independently rejected. Route/corpus results use the pre-existing `discover_read_graph`, `measure_graph`, and `active_runtime_corpus_words` methods. The three named D75/VBSA spans are byte-identical to Baseline.
- **Match:** ✅

### V25: `docs/scripts/test_integration.py`
- **RF claim:** Adds manifest-derived 11-route classification, checkpoint ordering/deletion/reorder mutation, clean-receiver, copy parity, protected-path and runtime-input assurance.
- **Actual:** The 137-addition/0-deletion diff derives the route set from the unchanged manifest, checks the exact 7 task/conditional + 4 project-wide partition, orders every affected checkpoint between named source anchors, mutates deletion/reorder, installs four clean receivers, verifies eleven tracked copies, protects the named paths, and forbids Phase-B TS/evidence runtime input.
- **Match:** ✅

### V-accounting: immutable VALUE boundary and Candidate timing
- **RF claim:** Baseline `83b31ff8d6cdb879fdf4f20578fa688b48863f8a` to Candidate `e16e6100b4957478a2ba351a225a1d400cee6367` is exactly 23 VALUE / 360+ / 240- / 600 touched LOC; Candidate precedes EV/RF and later work is TRACE-only.
- **Actual:** Independent NUL-safe `--name-status` parsing returned 23 records, all `M`, with membership exactly equal to the approved literal selector. Independent `--numstat` parsing returned 23 numeric records, 360 additions, 240 deletions, 600 touched text LOC, binary 0. Approval `f904af8` is descended from Baseline and precedes ONB and Candidate. Candidate is the first Executor commit containing all 23 VALUE plus both ASSURANCE files. Candidate→`b4f613d` changes only Phase-B RF, EV/attachments, status and one journal event; no VALUE or ASSURANCE path moves.
- **Match:** ✅

### V-context/protection: charged ceilings and protected selectors
- **RF claim:** All nine route profiles and the active corpus are non-growing; D75/VBSA selectors and `/tfw-plan <= 24,730` are unchanged.
- **Actual:** Independent source-tree replay returned Plan 24,665≤24,725; Research 6,052≤6,102 and 6,117≤6,167; Handoff normal/revise 6,298≤6,366; Review 24,884≤24,954; Resume 3,196≤3,264; Docs 15,242≤15,278; Init 4,508≤4,529; active corpus 33,211≤33,749. The central range is 33≤260 words and every local workflow delta is ≤45. `PHASE_C_PRIMARY_ENTRY_WORDS`, `test_phase_c_every_changed_path_and_active_corpus_clear_thirty_percent`, and `test_vbsa_plan_loads_three_unique_canonical_sections_with_d75_intact` have identical Baseline/Candidate SHA-256 values; the parsed plan constant is 24,730. The Baseline→Candidate diff is empty for AGENTS/CLAUDE managed roots, manifest, all 22 Codex source/install skills, Phase A, CRATM, and four project-wide workflows.
- **Match:** ✅

### V-staging: exact-path commit discipline
- **RF claim:** Candidate and final trace commits preserve unrelated work and use the exact approved path set.
- **Actual:** Executor task trace shows full `git status`, cached-name inspection, explicit `git add -- <paths>`, cached diff checks, and `git commit --only -- <paths>` for ONB, state transition, the 25-file Candidate, and final trace set. Candidate commit tree and final trace commit match those explicit pathspecs; no unrelated path entered either commit.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `py -m py_compile docs/scripts/test_runtime_context.py docs/scripts/test_integration.py` | PASS, exit 0 |
| 2 | `git diff --check 83b31ff… e16e610…` | PASS, exit 0 |
| 3 | `py docs/scripts/test_runtime_context.py --session-identity-scenarios` | PASS; 15 semantic + 16 workflow-mode records |
| 4 | `py docs/scripts/test_runtime_context.py --session-identity-mutants` | PASS; 7/7 changed and independently rejected |
| 5 | `py docs/scripts/test_runtime_context.py --session-identity-context` | PASS; nine profiles, corpus and local caps within immutable ceilings |
| 6 | Exact NUL-safe `git diff --name-status/--numstat --find-renames=50% -z Baseline Candidate -- <23 literal paths>` parsed independently | PASS; exact 23 `M`; 360+ / 240- / 600; binary 0 |
| 7 | Direct Baseline/Candidate protected-path diff and AST named-span hash comparison | PASS; path diff empty; all three spans byte-exact; plan constant 24,730 |
| 8 | Direct Codex task metadata readback for `01a07296…` and `01a07281…` | PASS; exact `EXEC · RTPSN · B` and `PLAN · RTPSN · B` |
| 9 | `py -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_integration.py -q` | PASS; 268 passed in 299.14s |
| 10 | `py -m pytest .tfw/scripts docs/scripts -q` | PASS; 629 passed, 1 suite-defined skip in 351.54s |
| 11 | `py .tfw/scripts/gen_index.py --check project` | PASS, exit 0 |
| 12 | `py .tfw/scripts/gen_index.py --check tasks` | Expected exit 1 solely for the unchanged RDP event summary at 123/120 code points; no RTPSN defect; 17 historical stateless-phase notes are informational |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | Exact 23 VALUE / 360+ / 240- / 600 touched accounting and no decomposition trigger | RF §§1/4; EV E-accounting | Approved TS at `f904af8`, literal selector, independent NUL-safe Git replay, config triggers 50/5,000 and multiplier 2 | ✅ |
| C2 | All charged profiles and active corpus are at or below immutable Baseline ceilings without weakening D75/VBSA | RF §4; EV E3/E6 | Baseline Git tree, current Candidate tree, pre-existing graph oracle, direct AST span hashes, independent two-file/full test runs | ✅ |
| C3 | Current Codex host has exact new/resumed titles, while search/visible/non-Codex claims remain bounded | RF §§3–5; EV E5 | Current direct metadata reads by both exact task IDs plus recorded list/API limitations; no screen or literal-query capability inferred | ✅ |
| C4 | A1 suffix is approved and A2 ASCII fallback rejected; implementation follows both | RF §§1–2; contract/scenario evidence | Frozen master amendment rows A1/A2 at `7bc0f30`, approved Phase-B TS, conventions range, base-collision and middle-dot-corrupt records | ✅ |
| C5 | Phase-A entry architecture and R0–R5 claim boundary remain intact | RF §§1–4 | Phase-A RF/REVIEW, D78, empty protected diff, unchanged 22 Codex skills and manifest, unchanged named tests/constants | ✅ |

Every Markdown citation in the Phase HL, TS, ONB, RF, EV and attachments was resolved relative to its actual file. No cited artifact is missing.

## Discrepancies Found

No discrepancies.

The RF observation about the immutable RDP event is real: the independent task check reproduces the 123-code-point summary against the 120-point ceiling. It is not a Phase-B implementation discrepancy; it is routed for disposition in REVIEW §5.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|-----------------|------------------|----------------|
| E1 | `EV__phase-b__session_identity_ergonomics.md` → contract/scenarios/mutants | ✅ | ✅ — one authority; 15 scenarios; 16 modes; 7/7 changing/rejected families |
| E2 | EV coverage row → `session-identity-coverage.txt` | ✅ | ✅ — 11 routes exactly once, 7/4 classification, required mode/checkpoint boundaries and four clean receivers |
| E3 | EV context row → `session-identity-context.txt` | ✅ | ✅ — nine exact ceiling comparisons, corpus 33,211, 33-word range, local deltas, copy/protection hashes |
| E4 | EV scenario/mutant row → both JSON files | ✅ | ✅ — JSON parses; counts, required fields, source manifests, suffix/failure behavior and independent rejection all hold |
| E5 | EV host row → `session-title-readback.json` and `session-title-visibility.txt` | ✅ | ✅ — direct live metadata readback matches; literal search/sidebar pixels/non-Codex hosts are explicitly N/A/unobserved |
| E6 | EV integrated row → `test-output.txt` | ✅ | ✅ — syntax/diff/project claims reproduced; 268 and 629/1 independent reruns match; task defect attribution exact |
| E-accounting | EV accounting row → `session-identity-accounting.txt` | ✅ | ✅ — approval, full SHAs, exact membership/arithmetic/action/binary/trigger/timing and trace-only tail independently reproduced |

Evidence inventory: RF refs 1/1 resolved; EV records 7/7 verified; EV attachments 9/9 present and matched.

## Knowledge Citations Verified

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | HL §7.2 K1 / ONB §7 K1 | P0 — root `README.md` `How It Works`; `.tfw/README.md` NS1 purpose/continuity and NS3 vendor/runtime non-goals | ✅ | ✅ | ✅ — durable state/authorized humans remain authority; host title is navigation only | ✅ |
| 2 | HL K2 / ONB K2 | P1 — `.tfw/README.md` `Methodology values`: Structural Enforcement, Naming Creates Behavior, Portability; Success Criteria 1,2,4 | ✅ | ✅ | ✅ — executable checkpoints, precise cues, provider-neutral files, inspectable acceptance | ✅ |
| 3 | HL K3 / ONB K3 | P2 — `knowledge/philosophy.md` F18 | ✅ | ✅ | ✅ — contextual names cue distinct cognitive/work modes | ✅ |
| 4 | HL K4 / ONB K4 | P2 — `knowledge/philosophy.md` F38/F45 | ✅ | ✅ | ✅ — coordinator attention/context and artifact count are finite budgets; subtraction is preferred when complete | ✅ |
| 5 | HL K5 / ONB K5 | P3 — `KNOWLEDGE.md` D15/D54 | ✅ | ✅ | ✅ — Codex skills remain thin workflow routers; parity is behavioral rather than layout identity | ✅ |
| 6 | HL K6 / ONB K6 | P3 — `KNOWLEDGE.md` D73–D75 (Phase HL/ONB also applies D68–D70 and D76–D78) | ✅ | ✅ | ✅ — workflow-owned selective reads, manifest topology, immutable accounting and R0–R5 boundaries are preserved | ✅ |
| 7 | HL K7 / ONB K7 | P4 — `conventions.md` Tool Adapter Pattern and Role Lock Protocol | ✅ | ✅ | ✅ — canonical workflow owns the algorithm/role; copies and title metadata grant no authority | ✅ |
| 8 | HL K8 / ONB K8 | P5 — `knowledge/convention.md` F4/F19 | ✅ | ✅ | ✅ — identity is an algorithmic checkpoint and uses one exact case/delimiter vocabulary | ✅ |
| 9 | HL K9 / ONB K9 | P6 — `knowledge/process.md` F3/F4/F7/F27/F30/F43 | ✅ | ✅ | ✅ — naming/gates/state-backed continuation and reason-at-confusion-point directly support the seven placements | ✅ |
| 10 | HL K10 / ONB K10 | task-local predecessor — Iteration 1 RES D1–D8 | ✅ | ✅ | ✅ — preserves thin proxy, distinct failure classes and non-substitutable evidence ladder | ✅ |
| 11 | HL K11 / ONB K11 | task-local predecessor — Iteration 2 RES D1–D10 | ✅ | ✅ | ✅ — exact grammar, vocabulary, placement, collision/failure rules and bounded claim level implemented | ✅ |

Independent P7 relevance scan found `knowledge/stakeholder.md` F16 as direct corroboration that titles are operational navigation and failure is non-blocking; F13 preserves `resume.md` until a separate task, and F14 bounds the current Codex long-lived-session context. These add no Phase-B rule beyond the frozen master/approved TS, so the Phase HL's P7 “no additional rule” conclusion is valid. No contradiction was found with `KNOWLEDGE.md` §1 or the other P0–P7 sources.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files and recorded findings? 25/25 Candidate files, 100%.
- [x] Ran at least 1 build/test command (or documented why not)? Two independent pytest gates plus syntax, source-derived and structural commands.
- [x] Claim & Source Checks filled — key claims checked, every citation traced, numeric claims checked against primary Git/app/test sources?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — no contradictions found; post-approval knowledge capture remains pending.
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total: 11, resolved: 11, semantically verified: 11, irrelevant: 0, hallucinated: 0
- [x] Evidence artifacts from RF §5 verified?
  - RF refs: 1/1; EV rows: 7/7; attachments: 9/9; missing: 0

Stage complete: YES
