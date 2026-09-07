# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF changed-file universe: 64 physical Baseline/final paths (37 VALUE path identities, 10 ASSURANCE, 1 DERIVED, 16 TRACE)
> Files to verify: ⌈64 × 0.42⌉ = 27
> Files actually verified: 64/64 physical paths plus all 10 RF evidence items (100%; the action-form deviation was checked at full scope)

## Verification Log

### V1: Candidate and final Git boundaries
- **RF claim:** Candidate `fd1d29949f948d141b745dcc99d771b953fd75c9` is the first tested implementation commit, and later writes are excluded TRACE/evidence only.
- **Actual:** Candidate is the direct child of `aa8f2acd6981e1444f89802ca6ea5e562184a1c6`. Candidate→final changes exactly 13 task-local paths: RF, EV, nine attachments, one transition event, and `status.md`. No implementation path changes after Candidate.
- **Match:** ✅

### V2: approved VALUE selector and accounting
- **RF claim:** The approved 37 literal paths represent 35 logical VALUE files and replay to 1,159 additions plus 1,067 deletions.
- **Actual:** Independent Baseline→Candidate replay with `--find-renames=50%` returned 35 logical records, including `R085` and `R057`, and exactly `+1159/-1067 = 2226` touched text LOC. There are no binary rows, no additional VALUE member, and no omitted approved constituent. The actual count equals the immutable 35-file denominator and is 1,374 LOC below the immutable 3,600-LOC denominator.
- **Match:** ✅

### V3: `.tfw/scripts/`, `workspace/00-INDEX.md`, and retained upstream tools
- **RF claim:** The tracked cache and Full payload executables are removed; retained executable behavior is upstream-only under `tools/`.
- **Actual:** Candidate has no `.tfw/scripts/**` entry and no `workspace/00-INDEX.md`. `tools/tfw_state.py` has no CLI, render, or shared-write surface. `tools/tfw_doctor.py` is read-only and bounded. The versioned migration lives under `tools/migrations/2.0.0/` with its own requirements and acquisition guidance.
- **Match:** ✅

### V4: canonical Knowledge Gate and no-helper receiver
- **RF claim:** Full contains one exact semantic no-helper Knowledge Gate, with independent agreement and no Python/PyYAML receiver prerequisite.
- **Actual:** The addressed algorithm exists once in `.tfw/workflows/knowledge.md`; Plan routes to it once. An independent PowerShell/.NET implementation selected the Candidate's sole knowledge-bearing artifact/section and produced `49b09711477dc71725c6271b7719980375dcd17728c3e27bcfee869b0d902c4e`, exactly matching the recorded oracle. The Candidate payload has zero `.tfw/scripts/**` files. Live mentions of Python/PyYAML in receiver workflows are prohibitions or absence checks; local upstream build commands remain project-owned configuration, not receiver prerequisites.
- **Match:** ✅

### V5: `tools/tfw_doctor.py` and schema/exit behavior
- **RF claim:** The doctor has exactly four operations, deterministic output, exits 0/1/2, and writes nothing.
- **Actual:** Source inspection confirms four explicit operations and the indeterminate-before-material exit ordering. Live `check tasks --format json` exited 0 with empty material and indeterminate arrays, 64 recognized tasks, and 31 phases. The complete focused doctor suite passed 7/7, including controlled exit 1/2, ordering, stable schema, and before/after no-write snapshots. Worktree status was unchanged by the live run.
- **Match:** ✅

### V6: prose guidance and structural validation
- **RF claim:** Numeric prose ceilings and truncation are gone while structural failures remain findings and the known 123-code-point event is unchanged.
- **Actual:** Retired-key scan over live config/templates/workflows returned no hits. Tests accept a 1,230-character current-event summary, preserve long migration source prose, and reject malformed identity, refs, writer, filename token, transition, collision, and unmatched inputs. The known event blob is `d156e68b55c47818820e364e2816630cbb03cef8` at both Baseline and Candidate and its summary length remains 123.
- **Match:** ✅

### V7: versioned migration
- **RF claim:** The pre-2.0 migration is self-contained, exact, non-overwriting, and dependency-honest before receiver reads/writes.
- **Actual:** The moved implementation no longer imports the removed payload module. `python -S ... --help` exits 0. With site packages absent, a normal invocation exits 2 before inspecting the deliberately nonexistent root and states that no receiver file was inspected or changed. The full migration suite, including accounting, no-overwrite, source-revision, malformed-row, and long-prose cases, passed in the whole-system run.
- **Match:** ✅

### V8: documentation generator, CI, and navigation
- **RF claim:** Every task remains directly reachable through an unlisted landing; Tasks/current status are absent from primary publication; the optional CI snapshot is finite and non-gating.
- **Actual:** A clean MkDocs build exits 0 and leaves tracked/cached state unchanged. The RTBO landing exists at `site/tasks/2026/TFW_20260902-222456_RTBO/index.html`; `site/tasks/index.html` does not exist; neither built home nor `docs/mkdocs.yml` contains a top-level Tasks route. The workflow defines an explicit boolean snapshot input, captures the doctor exit without failing the docs build, retains the artifact for seven days, and does not place it under `site/`.
- **Match:** ✅

### V9: canon and active adapter receivers
- **RF claim:** Four changed canonical workflows and eight active copies are byte-exact and express one boundary.
- **Actual:** Direct byte comparison returned 8/8 exact for `.claude/commands/tfw-{plan,knowledge,init,update}.md` and `.agent/workflows/tfw-{plan,knowledge,init,update}.md` against their canonical workflows. Current-instruction scans found no unexplained old index/script/prose-ceiling route. The complete adapter and clean-receiver integration suite passed.
- **Match:** ✅

### V10: Assisted and protected history
- **RF claim:** Assisted is unchanged, 243 protected paths are unchanged, and the known event is unchanged.
- **Actual:** Baseline and Candidate both resolve `editions/02-assisted` to tree `871ce20594402353a51818681f6f14c8cc9a3feb`; path diff exits 0. The independent selector found 243 Baseline task/workspace journal or snapshot paths; every Candidate path/blob tuple is identical and the protected-path diff exits 0. The known event blob matches exactly. The recorded pre-act manifest SHA-256 is consistent with the same immutable selector; tuple equality was independently recomputed from Git objects.
- **Match:** ✅

### V11: ASSURANCE move action form
- **RF claim:** The sole deviation is the planned `.tfw/scripts/test_gen_index.py` → `tools/tests/test_tfw_state.py` move appearing as delete plus add below Git's 50% threshold.
- **Actual:** At 50%, Git reports exactly `D .tfw/scripts/test_gen_index.py` plus `A tools/tests/test_tfw_state.py`; no-renames accounting is `-1783/+311`. Both paths are the approved ASSURANCE source/destination, the destination contains 15 focused state/gate tests, all 491 tests collect, and 490 pass with the one declared skip. This changes neither the 35-member VALUE selector nor any AC.
- **Match:** ✅ — action form differs, approved semantic scope and acceptance behavior do not.

### V12: task-local TRACE and evidence
- **RF claim:** Evidence and final lifecycle writes do not alter the product snapshot.
- **Actual:** All 16 Baseline→final TRACE paths were opened. The approved TS differs from the approval commit only by the pre-ONB Baseline-literal correction; ONB binds execution to that correction; RF/EV and nine attachments are internally consistent; status/journal record the linear ONB→RF transition. Candidate→final contains no VALUE or ASSURANCE path.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python -m pytest --collect-only -q` | Exit 0; 491 tests collected. |
| 2 | `python -m pytest -q` | Exit 0; 490 passed, 1 skipped in 323.52 s. |
| 3 | `python -m mkdocs build --config-file docs/mkdocs.yml --clean --quiet` | Exit 0; only known non-fatal historical unresolved-reference warnings; tracked diff and status stable. |
| 4 | `python tools/tfw_doctor.py --root . check tasks --format json` | Exit 0; 0 material, 0 indeterminate; 64 tasks, 31 phases; no write. |
| 5 | `python -m pytest tools/tests/test_tfw_doctor.py -q` | Exit 0; 7 passed, including controlled exits and no-write. |
| 6 | independent PowerShell/.NET Knowledge Gate digest | Exact digest `49b097…d902c4e`; no Python, PyYAML, or repository helper used. |
| 7 | `python -S tools/migrations/2.0.0/migrate_board.py --help` | Exit 0 without site packages. |
| 8 | `python -S tools/migrations/2.0.0/migrate_board.py --root Z:\\definitely-missing` | Exit 2 for missing PyYAML before receiver inspection/write. |
| 9 | exact approved VALUE `git diff --name-status/--numstat --find-renames=50%` replay | 35 logical records; +1159/-1067; 2,226 touched text LOC. |
| 10 | Candidate→final name-status replay | Exactly 13 task-local TRACE/evidence paths. |
| 11 | Baseline/Candidate Assisted tree and protected-selector replay | Same Assisted tree; 243/243 tuples identical; known blob identical. |
| 12 | direct canonical/adapter byte comparison | 8/8 exact. |
| 13 | `git diff --check Baseline final` | Exit 0. |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | “35 logical VALUE files; 1,159 additions + 1,067 deletions” | RF §§2, 4–5; EV E-accounting | Primary Git Baseline→Candidate selector replay from approved TS literals | ✅ exact |
| C2 | “491 collected; 490 passed, 1 skipped” | RF §§3–5; EV E9 | Independent local pytest collect and execution output | ✅ exact |
| C3 | Semantic YAML plus exact SHA-256; hidden MkDocs pages; finite workflow artifacts; schema assertions versus annotations; dependency-group separation | HL §7.2 K20–K23 and ONB §7 | YAML 1.2.2, NIST FIPS 180-4, GitHub Releases/Immutable Releases/Attestations/Workflow Artifacts, MkDocs nav, JSON Schema validation vocabulary, and PyPA Dependency Groups primary documentation | ✅ sources resolve and support the applied claims |

All other internal HL/ONB citations were traced to repository artifacts in the table below. No citation resolves only by plausible name.

## Discrepancies Found

No implementation, acceptance, accounting, evidence-status, or citation discrepancy was found after 100% changed-path verification.

Two lifecycle/process notes do not alter that result:

1. `KNOWLEDGE.md` §1 still contains the pre-cutover architecture wording about the tracked task index and old script. TS §4 explicitly defers project-knowledge capture until after approved review, so this is the expected `/tfw-docs` follow-up, not a Candidate contradiction or an allowed Reviewer edit.
2. RF/EV do not retain a literal transcript of the Executor's pre-commit `git status`, cached-name check, or `git commit --only` invocation. Git independently proves the observable boundary: the Candidate commit contains only its 48 expected physical implementation paths, Candidate→final contains exactly 13 task-local TRACE/evidence paths, and the supplied final ref was clean before review work. The invocation itself is not reconstructible from Git, but no unrelated or unapproved content entered either commit.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|-----------------|------------------|----------------|
| E1 | `evidence/rtbo-boundaries.txt` | ✅ | ✅ Candidate tree and no-write boundary independently replayed. |
| E2 | `evidence/knowledge-gate-conformance.json` | ✅ | ✅ PowerShell/.NET digest, canonical route, thresholds, and mutant-focused tests match. |
| E3 | `evidence/doctor-conformance.json` | ✅ | ✅ Source, live run, schema, exits, and no-write tests match. |
| E4 | `evidence/prose-and-structure.json` | ✅ | ✅ Retired keys absent; long prose and structural cases pass; known blob matches. |
| E5 | `evidence/migration-runtime-matrix.txt` | ✅ | ✅ `-S` help and dependency stop independently reproduced; full migration tests pass. |
| E6 | `evidence/docs-reachability.txt` | ✅ | ✅ Clean build, RTBO landing, absent aggregate/nav route, and CI mode match. |
| E7 | `evidence/canon-and-adapters.txt` | ✅ | ✅ Canon scan and 8/8 byte parity match. |
| E8 | `evidence/assisted-history-boundary.txt` | ✅ | ✅ Assisted tree, 243 tuple identities, and known blob match. |
| E9 | `evidence/test-and-accounting.txt` | ✅ | ✅ Whole-system tests, receiver proof, and accounting match. |
| E-accounting | `evidence/test-and-accounting.txt` | ✅ | ✅ Approval/Baseline/Candidate rule, selector, metrics, thresholds, and sole action-form deviation match. |

## Knowledge Citations Verified

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | HL K1 / ONB K1 | P0 — Project North Star NS1 | ✅ | ✅ | ✅ attention-cost reduction with durable continuation | ✅ cache subtraction preserves trace continuation |
| 2 | HL K2 / ONB K2 | P0 — NS2.2, NS2.4, NS2.7 | ✅ | ✅ | ✅ simplification, traceability, proportional assurance | ✅ directly governs removal and retained tests |
| 3 | HL K3 / ONB K3 | P0 — NS3 | ✅ | ✅ | ✅ method is not a mandatory runtime/generator | ✅ excludes shipped helper authority |
| 4 | HL K4 / ONB K4 | P1 — Methodology values: Structural Enforcement, Portability | ✅ | ✅ | ✅ structural contracts remain; runtime independence matters | ✅ exact gate plus optional upstream tooling |
| 5 | HL K5 / ONB K5 | P1 — Success Criteria 1, 2, 4 | ✅ | ✅ | ✅ direct state, durable decisions, tested completion | ✅ task-local state and whole-system tests retain them |
| 6 | HL K6 / ONB K6 | P2 — `knowledge/philosophy.md` F6, F8, F11 | ✅ | ✅ | ✅ Markdown traces are source; views are downstream | ✅ removes authoritative generated cache |
| 7 | HL K7 / ONB K7 | P2 — F42 | ✅ | ✅ | ✅ enforce length only for material harm | ✅ prose ceilings become guidance |
| 8 | HL K8 / ONB K8 | P2 — F43, F45 | ✅ | ✅ | ✅ architecture over suppression; artifact count is a budget | ✅ removes mechanism without replacement cache |
| 9 | HL K9 / ONB K9 | P3 — KNOWLEDGE D34, D68 | ✅ | ✅ | ✅ cited traces stay compiled; task-local state is authority | ✅ hidden landings replace catalogue authority |
| 10 | HL K10 / ONB K10 | P3 — D61, D69 | ✅ | ✅ | ✅ proportional QA; whole identifiers or refusal | ✅ bounded doctor and exact discovery |
| 11 | HL K11 / ONB K11 | P3 — D73, D75, D76 | ✅ | ✅ | ✅ selective reads, tolerant history/strict writes, immutable accounting | ✅ gate/history/VALUE behavior follows them |
| 12 | HL K12 / ONB K12 | P4 — conventions Task control, Discovery, Design Rules, Anti-patterns | ✅ | ✅ | ✅ local authority, exact discovery, no broad rewrite | ✅ cutover preserves ownership boundaries |
| 13 | HL K13 / ONB K13 | P5 — `knowledge/convention.md` F22 | ✅ | ✅ | ✅ old board-budget classification is historical | ✅ not misused to retain the cache |
| 14 | HL K14 / ONB K14 | P6 — `knowledge/process.md` F37, F38 | ✅ | ✅ | ✅ figures require method/ref; post-act bounds do not govern | ✅ accounting is replayable and prose bounds are removed |
| 15 | HL K15 / ONB K15 | P7 — `knowledge/stakeholder.md` F7, F11 | ✅ | ✅ | ✅ owner-approved boundary and owning-artifact rule | ✅ scope and trace ownership are preserved |
| 16 | HL K16 / ONB K16 | task-local predecessor — Iteration 1 Gather | ✅ | ✅ | ✅ six responsibilities behind one import boundary | ✅ supports responsibility split |
| 17 | HL K17 / ONB K17 | task-local predecessor — Iteration 1 Extract | ✅ | ✅ | ✅ shipping, dependency, invocation, publication differ | ✅ supports payload/upstream split |
| 18 | HL K18 / ONB K18 | task-local predecessor — Iteration 1 Challenge | ✅ | ✅ | ✅ structural validation survives prose-ceiling removal | ✅ implemented and tested |
| 19 | HL K19 / ONB K19 | task-local predecessor — Iteration 2 Gather | ✅ | ✅ | ✅ gate, migration, doctor, and hidden-landing evidence needs | ✅ each appears in TS and evidence |
| 20 | HL K20 / ONB K20 | external primary — YAML 1.2.2; NIST FIPS 180-4 | ✅ | ✅ | ✅ semantic structures and standard digest behavior | ✅ canonical gate requires semantic YAML and SHA-256 |
| 21 | HL K21 / ONB K21 | external primary — GitHub releases, immutable releases, attestations | ✅ | ✅ | ✅ versioned immutable delivery and provenance | ✅ migration guidance is version-addressed |
| 22 | HL K22 / ONB K22 | external primary — MkDocs navigation; GitHub Actions artifacts | ✅ | ✅ | ✅ unlisted pages still build; artifacts retain outputs finitely | ✅ hidden landings and seven-day snapshot match |
| 23 | HL K23 / ONB K23 | external primary — JSON Schema validation; PyPA dependency groups | ✅ | ✅ | ✅ assertions differ from annotations; internal tool deps can be separated | ✅ doctor advice and upstream dependencies are separated |

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈64 × 0.42⌉ files and recorded findings? 64/64 physical changed paths plus 10/10 evidence items.
- [x] Ran at least 1 build/test command? Full pytest, collect-only, clean docs, live/controlled doctor, migration, receiver, and Git replays ran.
- [x] Claim & Source Checks filled — 3 high-dependency claims checked against Git, test output, and primary standards/platform docs.
- [x] Each RF §3 (AC) checkmark verified against actual files and independent commands?
- [x] KNOWLEDGE.md checked — expected post-review architecture-doc capture is documented above.
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total unique citation rows: 23, resolved: 23, semantically verified: 23, irrelevant: 0, hallucinated: 0.
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 10, verified: 10, missing: 0.

Stage complete: YES
