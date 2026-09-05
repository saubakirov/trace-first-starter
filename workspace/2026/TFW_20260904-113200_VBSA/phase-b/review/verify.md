# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed: 10 Baseline→Candidate paths
> Files to verify: ⌈10 × 0.42⌉ = 5; escalated voluntarily to all 10, plus Candidate→RF TRACE

## Verification Log

### V1: `KNOWLEDGE.md`
- **RF claim:** Candidate changes only the six owner-authorized rows: Config, D70, D75, D76, Phase A result, and the legacy Phase A row.
- **Actual:** The fixed Baseline→Candidate diff has one VALUE path, 5 hunks, 4 additions and 1 deletion in `--numstat` (7 touched text LOC). Each target row occurs exactly once. D75 and all of §4 are byte-for-byte unchanged. D70 retains its ten operative rules and seven stated failure causes; its five links are unchanged. D76, Config, and both Phase A rows match their cited sources and measurements.
- **Match:** ✅

### V2: master and phase HL
- **RF claim:** Governing TRACE records Phase B scope, immutable refs, knowledge-only VALUE, accounting method, acceptance criteria, and Coordinator authority.
- **Actual:** Both HL artifacts do so. The master Amendment Log contains the prospective R1 and R2 rulings; Phase B HL keeps the accepted result limited to four row outcomes plus the legacy row and forbids implementation/config/index work.
- **Match:** ✅

### V3: Phase B TS and prospective rulings
- **RF claim:** TS fixes Baseline `9221dbb...`, Candidate rule, literal `KNOWLEDGE.md` selector, 1-file/5-LOC denominator, two universal measures, protected boundaries, and the R1/R2 ceilings before replacement Candidate work.
- **Actual:** The approved TS at `d0a2bfd...` contains the original contract. R1 `bf4a5d5...` and R2 `c0d3af3...` are append-only prospective rulings; `27f9d7e...` is a direct child of R2. Approval→first Candidate→R1→R2→replacement Candidate→RF ancestry is linear and verified. The R1/R2 journal references were corrected after Candidate from stale `ruling` names to the actual `dispatch` event names without changing authority or VALUE.
- **Match:** ✅

### V4: ONB, status, and pre-Candidate journals
- **RF claim:** Execution context, role/authority boundaries, plan, citations, lifecycle, and dispatch history are complete and consistent.
- **Actual:** ONB covers all five ACs, the ten-row work plan, fixed refs, exclusions, and all knowledge citations. `status.md` is at `RF` with Executor handoff recorded. The created, initial-dispatch, handoff, R1, and R2 journal entries form a consistent chronological trace.
- **Match:** ✅

### V5: EV, RF, transition journal, and post-Candidate TRACE
- **RF claim:** Evidence reproduces selection/counts, semantic content, lineage, tests, and Candidate timing; no post-Candidate VALUE or index edit exists.
- **Actual:** EV/RF references resolve and agree with independent replay. Candidate→RF contains only current-task TRACE. `KNOWLEDGE.md` and `workspace/00-INDEX.md` have zero Candidate→RF changes. The transition event records TS→RF handoff at the declared RF HEAD.
- **Match:** ✅

### V6: all fixed Baseline→Candidate paths
- **RF claim:** The phase stays within VALUE scope and protected boundaries.
- **Actual:** All 10 paths were inspected. Exactly one is VALUE (`KNOWLEDGE.md`); the other nine are current-task TRACE. No protected implementation, workflow, template, config, test, adapter, unrelated-task, or index path is changed. Actual 1 logical VALUE file and 7 touched text LOC are below R2 ceilings 2 and 9 and below the configured 50/5000 decomposition triggers.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | NUL-safe `git diff --name-status -z` and `git diff --numstat -z` for Baseline→Candidate with the literal selector | ✅ 1 logical VALUE file; `4 + 1 = 5` line events, 7 touched LOC; no binary VALUE |
| 2 | Full Baseline→Candidate path inventory and protected/index checks | ✅ 10 paths: 1 VALUE + 9 current-task TRACE; protected 0; index 0 |
| 3 | Candidate→RF VALUE/index checks | ✅ `KNOWLEDGE.md` 0; `workspace/00-INDEX.md` 0 |
| 4 | `git merge-base --is-ancestor` across approval, first Candidate, R1, R2, replacement Candidate, and RF | ✅ every required ancestry edge holds |
| 5 | `git diff --check 9221dbb... 27f9d7e...` | ✅ exit 0 |
| 6 | Exact D70 rule/rationale script plus word/link comparison | ✅ R1–R10 and Q1–Q7 true; 429→214 whitespace words; links 5→5 unchanged |
| 7 | Candidate row uniqueness, D75 equality, §4 equality, and 19 local-link resolution checks | ✅ all unique/equal; 19/19 paths resolve; the §12 anchor exists as `## 12. Amendment Log` |
| 8 | Phase A owner-approved selector replay (`f5a96af...`→`59c73bf...`) | ✅ 29 literal VALUE paths, all `M`; 663 additions + 321 deletions = 984 touched LOC; binary 0 |
| 9 | `.tfw/project_config.yaml` exact-key parse | ✅ `decomposition_trigger_files: 50`, `decomposition_trigger_loc: 5000`, `owner_escalation_multiplier: 2`, and no fourth scope-budget key |
| 10 | Two named former-ceiling tests | ✅ 2 passed in 27.34 s |
| 11 | Direct `/tfw-plan` graph measurement | ✅ output 24,720 bytes ≤ 24,730 ceiling |
| 12 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | ✅ 562 passed, 1 skipped in 226.93 s |
| 13 | `python -m pytest .tfw/scripts/ docs/scripts/ --collect-only -q` | ✅ 563 tests collected |
| 14 | `python .tfw/scripts/gen_index.py --check project` | ✅ framework 2.1.0, one participant, consistent |
| 15 | `python .tfw/scripts/gen_index.py --knowledge-pending --format json` | ✅ VBSA is the sole pending task; `migration_required: false`; no problems |
| 16 | `python .tfw/scripts/gen_index.py --check tasks` | ⚠️ exit 1 only for an inherited unrelated RDP journal summary of 123 code points over its 120 ceiling; VBSA has no task-index finding |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | Phase B actual is 1 logical VALUE file / 7 touched LOC against a 1 / 5 owner-approved denominator, within R2 ceilings 2 / 9 | RF §§1/3/5; EV accounting | Raw NUL-safe Git diff at immutable Baseline/Candidate; approved TS; R1/R2 commits and journals | ✅ Independently reproduced |
| C2 | D70 preserves all operative update-without-guesswork rules and the stated 114-row rationale | `KNOWLEDGE.md` D70; RF AC-1 | TFW-60 Phase AC RF, REVIEW, ONB Q1, amendment rulings, and fourth/fifth field reports | ✅ Ten rule groups and seven causes retained; 114-row S-vs-So finding matches primary task evidence |
| C3 | Historical Phase A result is 29 modified VALUE paths and 984 touched LOC | `KNOWLEDGE.md` Phase A and legacy rows; RF AC-4 | Owner-approved Phase A TS literal selector; raw `f5a96af...`→`59c73bf...` replay; Phase A RF/EV/final REVIEW | ✅ 29 `M`, 663 additions, 321 deletions, no binary entries |
| C4 | Current project settings are 50 files, 5000 LOC, multiplier 2, with exactly three scope keys | `KNOWLEDGE.md` Config; RF AC-3 | Parsed `.tfw/project_config.yaml`; template/config workflow/conventions carriers | ✅ Exact key set and values confirmed |

## Discrepancies Found

No discrepancies in the reviewed Phase B scope. The unrelated pre-existing RDP journal-summary failure is recorded as a repository observation, not a Phase B discrepancy; Phase B changes neither that task nor the index.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | EV E1 — immutable references and linear lineage | ✅ | ✅ Replayed independently |
| E2 | EV E2 — accounting and boundary enforcement | ✅ | ✅ Raw diff reproduces 1 file / 7 touched LOC and zero protected/index paths |
| E3 | EV E3 — semantic row checks | ✅ | ✅ D70, D75, D76, Config, Phase A, legacy row, §4, and links verified |
| E4 | EV E4 — validation suite and plan ceiling | ✅ | ✅ Named tests, direct graph, full suite, collection, and project check reproduced |
| E5 | EV E5 — Candidate timing and final Reviewer slice | ✅ | ✅ Candidate precedes RF and is unchanged; the RF correctly marked the then-future independent Reviewer slice deferred, and this review now supplies it |

## Knowledge Citations Verified

The same 21 citations appear in master HL §7.2 and ONB §7, so each row below represents two citation applications (42 total). Priority 0–4 sources were read in full as required; priorities 5–7 were read by relevance. External claims were checked against the linked primary or authoritative source.

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | HL #1 / ONB #1 | P0 · NS1 Purpose | ✅ | ✅ | ✅ Selected traces serve inspectability/continuation, not text volume | ✅ Separates VALUE from TRACE |
| 2 | HL #2 / ONB #2 | P0 · NS2.1, NS2.3, NS2.6 | ✅ | ✅ | ✅ Purpose, selected trace, and risk-proportional assurance | ✅ Grounds membership and independent assurance |
| 3 | HL #3 / ONB #3 | P0 · NS3 Non-goals | ✅ | ✅ | ✅ No documentation-factory or artifact-count success | ✅ Rejects trace taxation |
| 4 | HL #4 / ONB #4 | P1 · Structural Enforcement | ✅ | ✅ | ✅ Rules must be observable in structure | ✅ Fixed refs/selector/evidence implement it |
| 5 | HL #5 / ONB #5 | P1 · Success Criteria #4 | ✅ | ✅ | ✅ Complete, usable, inspectable result | ✅ Candidate contains the acceptance-ready VALUE |
| 6 | HL #6 / ONB #6 | P2 · F13/F42/F43/F45 | ✅ | ✅ | ✅ Domain neutrality, materiality, architecture, subtraction | ✅ Supports one concise cross-domain carrier |
| 7 | HL #7 / ONB #7 | P3 · D16/D24/D49/D52/D72 | ✅ | ✅ | ✅ Enforceable settings, requirements-first execution, assurance separation, decision closure | ✅ Matches the TS→EV→REVIEW chain |
| 8 | HL #8 / ONB #8 | P4 · Scope Budgets | ✅ | ✅ | ✅ Classification, accounting, and authority semantics | ✅ D76 records the established contract |
| 9 | HL #9 / ONB #9 | P4 · Design Rules | ✅ | ✅ | ✅ Inline enforcement and progressive disclosure | ✅ Reuses existing carriers without indirection |
| 10 | HL #10 / ONB #10 | P5 · F22 | ✅ | ✅ | ✅ Historical process-artifact budget exclusion | ✅ Supports TRACE exclusion without rewriting history |
| 11 | HL #11 / ONB #11 | P6 · F32/F37/F38/F40 | ✅ | ✅ | ✅ Fixed references, method, pre-act bounds, reachable units | ✅ Matches immutable Candidate accounting |
| 12 | HL #12 / ONB #12 | P7 · F7 | ✅ | ✅ | ✅ Evidence must work across non-code domains | ✅ Prevents code-only VALUE semantics |
| 13 | HL #13 / ONB #13 | Git `git-diff` documentation | ✅ | ✅ | ✅ `--numstat`, rename/path handling, NUL termination | ✅ Grounds replayable file/LOC arithmetic |
| 14 | HL #14 / ONB #14 | NASA SWE-093 + software-size guide | ✅ | ✅ | ✅ LOC requires an explicit method and context | ✅ Limits LOC to applicable text VALUE |
| 15 | HL #15 / ONB #15 | Scrum Guide + Kanban Guide | ✅ | ✅ | ✅ Goals and explicit policies coexist with adaptation | ✅ Supports bounded learning without outcome drift |
| 16 | HL #16 / ONB #16 | DORA small batches + Google Small CLs | ✅ | ✅ | ✅ Small coherent batches aid feedback; no universal line rule | ✅ Supports soft decomposition prompts |
| 17 | HL #17 / ONB #17 | PeerJ experiment + Empirical Software Engineering study | ✅ | ✅ | ✅ Patch decomposition/size affect review contextually | ✅ Supports visible judgment, not TFW thresholds |
| 18 | HL #18 / ONB #18 | Library of Congress sustainability factors | ✅ | ✅ | ✅ Significant characteristics vary by genre | ✅ Supports per-medium applicability |
| 19 | HL #19 / ONB #19 | NASA Systems Engineering Handbook | ✅ | ✅ | ✅ Baseline, proposal, authority, implementation, verification are distinct | ✅ Supports prospective bounded authority |
| 20 | HL #20 / ONB #20 | NIST SP 800-53 CM-3 | ✅ | ✅ | ✅ Controlled changes are reviewed/approved before implementation | ✅ Rejects retrospective authorization |
| 21 | HL #21 / ONB #21 | Semantic Versioning 2.0.0 | ✅ | ✅ | ✅ Released contents are immutable | ✅ Supports prospective migration and untouched history |
| 22 | ONB additional phase-HL dependencies | P3 D37/D43/D44/D63/D68/D73–D75; P7 F14; risk F1 | ✅ | ✅ | ✅ Ownership, semantic citation review, frozen/state boundaries, selective authority, independent review, full-status reads | ✅ Directly governs Phase B execution and this review |

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files and recorded findings?
- [x] Ran at least 1 build/test command (or documented why not)?
- [x] Claim & Source Checks filled — key claims spot-checked, every citation traced to a real artifact, data claims checked against primary sources?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] `KNOWLEDGE.md` checked — contradictions with changes documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total applications: 43 (21 HL + 21 ONB table rows + 1 ONB dependency group), resolved: 43, semantically verified: 43, irrelevant: 0, hallucinated: 0
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 5, verified: 5, missing: 0

Stage complete: YES
