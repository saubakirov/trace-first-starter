# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed: 31 implementation files (29 VALUE + 2 ASSURANCE)
> Files to verify: ⌈31 × 0.42⌉ = 14; discrepancies escalated verification to 31/31

## Verification Log

### V1: approved accounting contract and Git lineage
- **RF claim:** Approval `36e50e4a362d474550f26e58defe56132b5417be`, Baseline `f5a96af07dcdc4230ecf31100bd155a3dca09604`, Candidate `6dce719338fece2601c1e1ce770273a1bb87c441`, 29 modified VALUE files, 634 additions, 318 deletions, 952 touched text LOC, no binary/non-text N/A, no later VALUE changes.
- **Actual:** The approved TS resolves at the stated approval commit and is unchanged through Executor HEAD. Its literal 29-path selector produces 29 `M` name-status records and 29 numeric numstat records; the sums are 634 + 318 = 952 and binary/non-text records are zero. Git ancestry is Baseline → approval → Candidate → `824c18ec19f49e5755e698d86bd58a1a8d6e092d`; the two pre-Candidate Executor commits contain only ONB/status/journal TRACE, Candidate is the first 31-path implementation commit, and Candidate→HEAD contains only RF/EV/status/journal TRACE.
- **Match:** ✅

### V2: `.tfw/conventions.md`, `.tfw/glossary.md`, configs, changelog, and release guidance
- **RF claim:** One semantic four-class model, two VALUE measures, three project-owned keys, prospective approval-epoch migration, immutable denominator, soft triggers, bounded authority, M1–M6, and version assignment reserved to `/tfw-release`.
- **Actual:** The canonical Scope Budgets section defines exactly VALUE/ASSURANCE/TRACE/DERIVED, the two measures, fixed Baseline/Candidate behavior, three-key 50/5000/2 defaults, terminal decomposition disposition, prospective authority, M1–M6, and approval-epoch semantics. Both YAML blocks parse to the exact three-key mapping. CHANGELOG is `[Unreleased]`, RELEASE requires `/tfw-release` classification and a version-named major migration before VERSION, and `.tfw/VERSION` remains 2.1.0.
- **Match:** ✅

### V3: `.tfw/workflows/plan.md` and `Planner scope checkpoint`
- **RF claim:** D75 remains enforced; plan uses one uniquely addressed planner route to canonical authority, not a second source of truth.
- **Actual:** The heading exists exactly once, but the resolved heading body only says to apply “the classification rules above and the two canonical subsections below.” The `/tfw-plan` read graph contains only the `Planner scope checkpoint` edge, not the classification text or the `Value-bearing accounting contract` / `Decomposition, constraints, and change authority` sections. The target is positional rather than uniquely addressed, while plan Step 7 repeats a shorthand version of the normative gate. An in-memory mutant changing the checkpoint from “apply” to “ignore” leaves both the discovered `/tfw-plan` graph and `resolve_vbsa_record()` unchanged.
- **Match:** ❌ — the unique heading is present, but it does not route the selective reader to the canonical authority and current source-derived assurance cannot detect the broken route.

### V4: handoff and review workflows
- **RF claim:** Executor fixes a tested Candidate before EV/RF/final state; reviewer replays the same contract without repairing it, supplying late authority, or conflating BLOCKED/N/A/INVALID/DEFERRED.
- **Actual:** Handoff uses VALUE-only triggers and immutable-denominator authority, fixes Candidate before later TRACE, and binds the one EV row/RF. Review independently resolves the approved TS, replays the same method, separates accounting outcomes, and prohibits repair or late authority.
- **Match:** ✅

### V5: config, update, init, and migration behavior
- **RF claim:** Customized old file/LOC values survive the atomic old→new mapping; history keeps its approval-epoch meaning; receiver North Stars remain byte-identical and starter purpose is not loaded/injected.
- **Actual:** Config/update carry the exact mapping and mixed-block refusal; update explicitly preserves receiver `.tfw/README.md`. Init's read contract correctly names receiver North-Star existence/bytes with the purpose “byte-preservation without loading starter purpose,” and Mini-Setup states root/`.tfw/README.md` byte preservation and no starter quotation injection.
- **Match:** ⚠️ partial — the shipped instructions are correct, but the claimed clean-receiver assurance is not behavior-derived (V8/D2).

### V6: `.tfw/templates/{TS,RF,REVIEW}.md` and `.tfw/templates/evidence/EV.md`
- **RF claim:** Templates carry the prospective contract, actual binding, independent review, and exactly one EV accounting row using the evidence status vocabulary.
- **Actual:** TS/RF/REVIEW contain the required role-specific forms and EV contains exactly one `E-accounting` row. However EV first mandates only `VERIFIED / DEFERRED / BLOCKED / N/A`, then its Result placeholder is `{VERIFIED/BLOCKED/N/A/INVALID}`. `INVALID` is the phase-attribution outcome required inside the accounting account, but D52 and TS AC-5 keep the EV Result vocabulary at four statuses.
- **Match:** ❌ — internally contradictory EV form; a future valid unresolved-attribution account can be recorded as a fifth evidence status.

### V7: `docs/scripts/test_runtime_context.py` and `docs/scripts/test_integration.py`
- **RF claim:** Source-derived behavioral tests and output-changing mutants prove classification, accounting, authority, migration, D75 preservation, clean receivers, and adapter parity.
- **Actual:** Classification/accounting/authority/migration records and mutants are source-derived and the NUL rename/binary fixture is real. Adapter and manifest checks are byte-based. But the North-Star test creates receiver bytes, performs no init/update operation from the workflow contract, then asserts the untouched bytes. Its only init source guard is `"never" in text and "North Star" in text`; changing “Preserve every existing … byte-for-byte” to “Overwrite every existing … byte-for-byte” still passes that guard, leaves the `/tfw-init` graph unchanged, and leaves the VBSA semantic record unchanged. The planner-route mutant in V3 is likewise invisible.
- **Match:** ❌ — AC-7's clean-receiver and D75 behavior/mutation-sensitivity claim is not established.

### V8: twelve adapter copies
- **RF claim:** Six `.agent` and six `.claude` copies are exact copies of their canonical workflows.
- **Actual:** SHA-256 comparison is equal for plan, handoff, review, config, update, and init across both destinations. Candidate's adapter manifest blob `752e22ae03c9d1d85949a09111b019f3ec192d0e` equals Baseline.
- **Match:** ✅

### V9: HC-1, local Saint-Exupéry placement, and historical RDP observation
- **RF claim:** No HC-1 path changed; the quotation is local at NS2 position 2 and does not reach root/localized or foreign receiver North Stars; the RDP 123/120 defect remains untouched.
- **Actual:** Baseline→Candidate changes are exactly 31 implementation paths plus nine authorized current-task TRACE paths. `tasks/**`, other workspace/history, master HL/RES, adapter manifest, `.agents/**`, root/localized README, VERSION, and existing migrations have zero changes. The quotation occurs once at local `.tfw/README.md` NS2 item 2; root/localized READMEs are Baseline-identical. The named RDP journal file is unchanged and its YAML summary is 123 code points; `--check tasks` reports that one known problem and exits 1.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---|---|
| 1 | approved NUL-safe `git diff --name-status --find-renames=50% -z … -- $valuePaths` | 29 records; all `M`; membership exactly equals the 29 approved rows |
| 2 | approved NUL-safe `git diff --numstat --find-renames=50% -z … -- $valuePaths` | 634 additions; 318 deletions; 952 touched text LOC; 0 binary/non-text N/A |
| 3 | Git ancestry, per-commit path sets, approval-TS equality, Candidate→HEAD selector diff, HC-1 census | all three refs ordered; Candidate first implementation commit; post-Candidate VALUE count 0; protected count 0 |
| 4 | `python -m pytest docs/scripts/test_runtime_context.py -q -k vbsa` | 20 passed, 129 deselected |
| 5 | `… -k "vbsa and (accounting or candidate or attribution)"` | 6 passed, 143 deselected |
| 6 | `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_integration.py -q -k "vbsa and (config or migration or release or update or init)"` | 9 passed, 214 deselected |
| 7 | `… -k "vbsa and (authority or saint or north_star)"` | 4 passed, 219 deselected |
| 8 | `… -k "vbsa and (handoff or rf or ev)"` | 2 passed, 147 deselected |
| 9 | `… -k "vbsa and review"` | 1 passed, 148 deselected |
| 10 | `python -m pytest docs/scripts/test_runtime_context.py -q` | 149 passed |
| 11 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | 553 passed, 1 skipped |
| 12 | `python .tfw/scripts/gen_index.py --check project` | exit 0; project consistent with declared release |
| 13 | `python .tfw/scripts/gen_index.py --check tasks` | expected baseline exit 1; exact RDP summary 123 > 120; informational legacy phase notes do not add failures |
| 14 | `git diff --check Baseline Candidate`; YAML parse; Python source compile | all exit 0 |
| 15 | SHA-256 adapter comparisons and Baseline/Candidate manifest blobs | 12/12 copies equal; manifest unchanged |
| 16 | in-memory planner and init adverse mutants | both preserve discovered graphs/VBSA record; bad init overwrite wording passes the current text guard |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|---|---|---|---|
| C1 | 29 VALUE / 634 + 318 = 952 / no binary N/A | RF §1; EV E-accounting | approved TS at `36e50e4`; raw NUL-safe Git outputs from Baseline→Candidate | ✅ |
| C2 | D75 selective reads remain enforced, with `Planner scope checkpoint` as route | RF §2 decision 2; EV E4/E7 | actual `/tfw-plan` graph + resolved checkpoint body + adverse mutant | ❌ — target ranges are neither loaded nor uniquely named; mutant is invisible |
| C3 | init/update clean receiver and EV status behavior are structurally proved | RF §4; EV E4/E5/E7 | actual tests, `/tfw-init` graph, EV template, D52 | ❌ — receiver test is self-fulfilling; EV form admits a fifth Result status |

## Discrepancies Found

1. **D1 — AC-7 / D75 planner route failure (rung 1).** `Planner scope checkpoint` resolves once but names its canonical inputs positionally and does not add them to `/tfw-plan`'s read graph. A route-body mutant is not rejected. Consequence: a fresh planner can author the VALUE contract from Step 7 shorthand without loading the canonical class, accounting, and authority rules, creating drift in an approval-critical TS.
2. **D2 — AC-4 and AC-7 clean-receiver evidence false positive (rung 1).** `test_vbsa_update_and_init_preserve_receiver_north_star_and_history` does not execute or derive preservation from init/update semantics. An explicit overwrite mutant passes the current init guard and leaves all discovered semantic records unchanged. Consequence: a regression that overwrites a receiver North Star can ship while E4/E7 and the full suite stay green.
3. **D3 — AC-5 EV status-vocabulary contradiction (rung 1).** `.tfw/templates/evidence/EV.md` mandates four statuses but permits `INVALID` in the Result cell. Consequence: future evidence can emit a fifth status that verdict summaries and evidence consumers do not recognize instead of recording attribution `INVALID` inside a four-status accounting result.

Accounting itself has no discrepancy; D1–D3 triggered and received 100% verification of the 31 implementation files.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|---|---|---|
| E1 | EV E1 / targeted semantic output | ✅ | ✅ — 20-pass family rerun; canonical class/measure content inspected |
| E2 | EV E2 / accounting-Candidate-attribution output | ✅ | ✅ — 6-pass family plus independent raw Git replay |
| E3 | EV E3 / config-migration-release-update-init output | ✅ | ✅ — 9-pass family; exact mapping/config/release facts independently inspected |
| E4 | EV E4 / authority-Saint-North-Star output | ✅ | ❌ — 4 tests pass, but clean-receiver preservation is not derived and accepts an overwrite mutant (D2) |
| E5 | EV E5 / handoff-RF-EV output | ✅ | ❌ — row-count binding passes, but the EV form contradicts the four-status vocabulary (D3) |
| E6 | EV E6 / review output | ✅ | ✅ — independent-replay/no-repair clauses and 1-pass gate verified |
| E7 | EV E7 / full suite, project check, parity | ✅ | ❌ — 553/1, project check, syntax, and parity reproduce, but source-derived D75/receiver mutation coverage claimed by AC-7 is absent (D1/D2) |
| E-accounting | EV accounting row and inline reproduction | ✅ | ✅ — refs, membership, arithmetic, triggers, authority/timing, HC-1, and invariance agree exactly |

## Knowledge Citations Verified

HL §7.2 rows and the corresponding ONB §7 rows were checked independently; ONB's added D73–D75 references were also checked.

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|---|---|---|---|---|---|
| 1 | HL/ONB #1 | P0 · NS1 Purpose | ✅ | ✅ | ✅ — value is purpose, authority, inspectability, continuation, not output volume | ✅ |
| 2 | HL/ONB #2 | P0 · NS2.1/2.4/2.7 (renumbered after Saint insertion) | ✅ | ✅ | ✅ — purpose, selected trace, proportional assurance | ✅ |
| 3 | HL/ONB #3 | P0 · NS3 Non-goals | ✅ | ✅ | ✅ — forbids documentation-factory/artifact-count success | ✅ |
| 4 | HL/ONB #4 | P1 · Structural Enforcement | ✅ | ✅ | ✅ — observable gates, not exhortation | ✅ |
| 5 | HL/ONB #5 | P1 · Success Criteria #4 | ✅ | ✅ | ✅ — complete, usable, inspectable accepted result | ✅ |
| 6 | HL/ONB #6 | P2 · philosophy F13/F42/F43/F45 | ✅ | ✅ | ✅ — domain breadth, materiality, architecture, subtraction | ✅ |
| 7 | HL/ONB #7 | P3 · D16/D24/D43/D49/D52/D63/D72–D75 | ✅ | ✅ | ✅ — config, inline enforcement, citations, requirements, evidence, contract, routing, selective reads | ✅ |
| 8 | HL/ONB #8 | P4 · Scope Budgets | ✅ | ✅ | ✅ — canonical governed surface and measures | ✅ |
| 9 | HL/ONB #9 | P4 · Design Rules | ✅ | ✅ | ✅ — inline enforcement and progressive disclosure | ✅ |
| 10 | HL/ONB #10 | P5 · convention F22 | ✅ | ✅ | ✅ — historical process-artifact budget precedent | ✅ |
| 11 | HL/ONB #11 | P6 · process F32/F37/F38/F40 | ✅ | ✅ | ✅ — contemporary evidence, refs/method, pre-act reader, reachable AC | ✅ |
| 12 | HL/ONB #12 | P7 · constraint F7 | ✅ | ✅ | ✅ — domain-agnostic evidence | ✅ |
| 13 | HL/ONB #13 | Git diff documentation | ✅ | ✅ | ✅ — numstat binary `-`, `-z` NUL terminators, rename-aware method | ✅ |
| 14 | HL/ONB #14 | NASA SWE-093 and NASA-GB-8719.13 | ✅ | ✅ | ✅ — documented analysis method; LOC varies by language and is available only after code | ✅ |
| 15 | HL/ONB #15 | Scrum Guide and Kanban Guide | ✅ | ✅ | ✅ — goal-preserving adaptation and explicit flow policies | ✅ |
| 16 | HL/ONB #16 | DORA small batches and Google Small CLs | ✅ | ✅ | ✅ — coherent small batches and reviewer judgment; no hard universal line rule | ✅ |
| 17 | HL/ONB #17 | PeerJ/Empirical Software Engineering studies | ✅ | ✅ | ✅ — decomposition/review effects without a sufficient universal cutoff | ✅ |
| 18 | HL/ONB #18 | Library of Congress format sustainability | ✅ | ✅ | ✅ — significant characteristics vary by content category/genre | ✅ |
| 19 | HL/ONB #19 | NASA Systems Engineering Handbook | ✅ | ✅ | ✅ — proposal/justification/approval/implementation/verification order | ✅ |
| 20 | HL/ONB #20 | NIST SP 800-53 CM-3 | ✅ | ✅ | ✅ — configuration changes reviewed/approved and controlled before implementation | ✅ |
| 21 | HL/ONB #21 | Semantic Versioning 2.0.0 | ✅ | ✅ | ✅ — released contents immutable; public-contract changes versioned | ✅ |
| 22 | ONB additional | P3 · D73 | ✅ | ✅ | ✅ — workflow-owned uniquely addressed reads and one manifest | ✅; D1 is a failure to preserve it, not a bad citation |
| 23 | ONB additional | P3 · D74 | ✅ | ✅ | ✅ — minimal role paths with dynamic edges and source-derived proof | ✅; D1/D2 show implementation drift |
| 24 | ONB additional | P3 · D75 | ✅ | ✅ | ✅ — selective workflow reads, source-derived proof, strict/tolerant behavior | ✅; directly material to D1/D2 |

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈31 × 0.42⌉ files and recorded findings? (31/31 after escalation)
- [x] Ran at least 1 build/test command (or documented why not)?
- [x] Claim & Source Checks filled — 2-3 key claims spot-checked, every citation traced to a real artifact, data claims checked against a primary source?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total cited items: 45 (21 HL + 21 ONB + D73–D75); resolved: 45; semantically verified: 45; irrelevant: 0; hallucinated: 0
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 8; sufficient: 5; present but insufficient/contradicted: 3; missing: 0

Stage complete: YES
