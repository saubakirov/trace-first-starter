# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed: 18 implementation files (16 VALUE + 2 ASSURANCE)
> Files to verify: ⌈18 × 0.42⌉ = 8; verified: 18/18 (100%) because this is a high-risk contract/authority change and the initial implementation run exposed nine predecessor regressions.

## Verification Log

| # | Candidate path | RF claim | Actual at Candidate `9edbebcf68872a72a9274765ad053e8d25fa66ac` | Match |
|---|---|---|---|---|
| V1 | `.tfw/conventions.md` | AT declaration, activation, duties, seven returns, degradation and eight admission gates | Source-derived parser returns all three declaration facts, separate activation, both duties, 7 exact trigger/channel rows, safe degradation, 8 gates, non-ordinal same-unit resolution and metadata non-authority; zero parser errors | ✅ |
| V2 | `.tfw/templates/HL.md` | Six-column frozen Role Assignment before phase dependencies | Exact heading and six required columns are present; table absence, committed freeze, approvals, `—`, human-rooted handles and Role Lock-only permission are explicit | ✅ |
| V3 | `.tfw/workflows/plan.md` | Validate declaration before freeze and dispatch after exact TS approval | Source-derived Plan record resolves the pre-freeze check and post-approval direct dispatch without executing another workflow | ✅ |
| V4 | `.tfw/workflows/handoff.md` | Receive Executor row before ONB/work and return directly | Record resolves row/source before work, preserves Role Lock, and sends questions/RF directly to Coordinator | ✅ |
| V5 | `.tfw/workflows/review.md` | Receive independent Reviewer row before Map and return directly | Record resolves Reviewer-row checkpoint before Map and direct verdict/proposal return while preserving Role Lock | ✅ |
| V6 | `.tfw/workflows/research/base.md` | Receive Researcher row before Briefing and return every gate/final RES directly | Record resolves both ordering and direct-return requirements without weakening stage gates | ✅ |
| V7 | `.tfw/adapters/codex/AGENTS.md.template` | Adapter-local visible-task/worktree/direct-operation profile with explicit exclusions and evidence limit | Managed block names `create_thread`, `send_message_to_thread`, `wait_threads`, separate worktrees, same-role reuse, rejected holders, human-rooted rows and G1–G7/G8 limit; no canonical provider leak | ✅ |
| V8 | `AGENTS.md` | Exact managed receiver with project-local bytes preserved | Managed CODEX block equals V7; prefix and suffix equal Baseline exactly | ✅ |
| V9 | `.agent/workflows/tfw-plan.md` | Exact Plan copy | SHA-256 and bytes equal V3; LF-terminated | ✅ |
| V10 | `.agent/workflows/tfw-handoff.md` | Exact Handoff copy | SHA-256 and bytes equal V4; LF-terminated | ✅ |
| V11 | `.agent/workflows/tfw-review.md` | Exact Review copy | SHA-256 and bytes equal V5; LF-terminated | ✅ |
| V12 | `.agent/workflows/tfw-research.md` | Exact Research copy | SHA-256 and bytes equal V6; LF-terminated | ✅ |
| V13 | `.claude/commands/tfw-plan.md` | Exact Plan copy, not a Claude profile | Bytes equal V3; no Claude-native admission claim | ✅ |
| V14 | `.claude/commands/tfw-handoff.md` | Exact Handoff copy, not a Claude profile | Bytes equal V4; no Claude-native admission claim | ✅ |
| V15 | `.claude/commands/tfw-review.md` | Exact Review copy, not a Claude profile | Bytes equal V5; no Claude-native admission claim | ✅ |
| V16 | `.claude/commands/tfw-research.md` | Exact Research copy, not a Claude profile | Bytes equal V6; no Claude-native admission claim | ✅ |
| V17 | `docs/scripts/test_runtime_context.py` | Actual source-derived consumers, negative cases and output-changing mutants without oracle/parser coupling | 17 scenarios resolve from product sources to separately declared expected tuples; 45 mutants in 11 families first change the parsed projection and are then rejected; the expected tables are independent literals and the nine predecessor semantic anchors remain | ✅ |
| V18 | `docs/scripts/test_integration.py` | Literal selector, copy/receiver/provider/protected-boundary assurance without weakening predecessor tests | Adds 94 lines and removes one superseded root-byte assertion only: the root check is narrowed to the authorized managed block and paired with exact outside-block and parity checks; no inherited test is deleted | ✅ |

All eighteen Candidate blobs end in LF and contain no CRLF. Candidate contains only these eighteen paths; ordinary Phase D traces are in its ancestry or later TRACE commits.

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | Target the nine initially failing predecessor names (including all parameterized neighbors) with `pytest -k ...` | `29 passed, 265 deselected in 151.38s`; the exact formerly failing A1/R1/R2 and R/A instances are green |
| 2 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | `655 passed, 1 skipped in 355.95s`; exit 0 |
| 3 | `python -m mkdocs build --config-file docs/mkdocs.yml` | Exit 0; documentation built in `416.41 seconds`; only existing generated-doc/reference warnings |
| 4 | Independent NUL-safe `git diff --name-status -z` / `--numstat -z` replay, Baseline→Candidate, literal 16 VALUE paths | 16/16 modified text members; `180 + 423 = 603`; no binary row; exact membership |
| 5 | Direct source projection of Phase D scenarios, mutants and census | 17 exact scenarios; 45/45 output-changing/rejected mutants across 11 families; 182 current classified occurrences, zero unclassified, zero positive provider leak (RF snapshot was 178 before Reviewer trace) |
| 6 | Git-object byte replay for four canonical workflows/eight copies, CODEX managed block, and 18 line endings | All byte-equal; root outside block unchanged; all LF, no CRLF |
| 7 | Git-object replay of `phase-d-protected.json` rows | 109/109 protected rows match Baseline; no Phase E tree entry |
| 8 | `python docs/scripts/test_runtime_context.py --session-identity-context` | Active corpus `32946/33749`; central range `33/260`; all nine route ceilings and seven workflow-local `45` caps pass |
| 9 | `python .tfw/scripts/gen_index.py --check tasks` | Expected exit 1: 15 historical `writer` diagnostics plus unchanged RDP `123/120`; both implicated source blobs are identical at Baseline and Candidate |
| 10 | Executor-task command/output audit plus `git worktree list`, Candidate ancestry and path history | Explicit 18-path cached set and `commit --only`; Candidate parent is ONB; Candidate precedes EV/RF; Executor worktree remains registered; Candidate is reachable here |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | Declaration is not activation; bare/draft/uncommitted/metadata/foreign/ambiguous/`—` states cannot self-authorize | RF §§1/3; EV E1–E2 | Candidate product clauses in `.tfw/conventions.md` and `.tfw/templates/HL.md`; 17 independently expected decisions and the matching output-changing mutant families | ✅ |
| C2 | Nine inherited anchors were restored before Candidate with their semantics and mutant sensitivity intact | RF §§2/4 | Executor's first full implementation run: exactly 9 failed and 646 passed; later pre-Candidate run: 655 passed. Current source assertions derive records from both Git/source trees and reject deleted, reordered and semantic mutants; independent targeted rerun is green | ✅ |
| C3 | Actual VALUE is exactly 16 files and 603 touched lines against immutable plan 16/640 | RF §§1/3; EV E-accounting | Raw Git objects `8e68ab37d300122ff110500ad58f354f76b6210f` and `9edbebcf68872a72a9274765ad053e8d25fa66ac`; independent NUL parser reproduces 16 names, 16 numeric rows, 180 additions and 423 deletions | ✅ |

Every non-knowledge citation in RF §§1–5 resolves to the phase HL, approved TS, ONB, EV, attachments, Git objects, predecessor artifacts, or recorded direct task output. Numeric claims were re-derived from Git objects and executable source rather than copied from the RF/EV summaries.

## Discrepancies Found

No Candidate/TS discrepancy.

The current live census is 182 rather than the RF attachment's 178 because the later Reviewer dispatch and review trace are permitted TRACE and Candidate is immutable; both counts are fully classified with no provider leak. The direct MkDocs run emits repository-wide historical reference warnings but exits 0. The two RF observations remain deliberately unfixed and byte-identical to Baseline: `gen_index.py` still does not accept template-valid `writer`, and the historical RDP event still has a 123-code-point summary.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | `evidence/EV__phase-d__team_mode_and_role_assignment.md` | ✅ | ✅ — all seven rows name executable/object evidence and match independent replay |
| E2 | `phase-d-scenarios.json` | ✅ | ✅ — 17 source-derived actual records equal separately declared expected records |
| E3 | `phase-d-mutants.json` | ✅ | ✅ — 45 rows, 11 families, every projection changes and every independent oracle rejects |
| E4 | `phase-d-census.json` | ✅ | ✅ — RF-time 178 occurrences classified, no unclassified row or positive product leak |
| E5 | `phase-d-byte-parity.json` | ✅ | ✅ — four canonicals/eight copies and managed receiver replay exactly |
| E6 | `phase-d-protected.json` | ✅ | ✅ — 109 protected blobs replay with zero mismatches; Phase E absent |
| E7 | `phase-d-accounting.json` | ✅ | ✅ — immutable refs, selector, 180/423/603 arithmetic, thresholds and lineage reproduce |
| E8 | `phase-d-context.json` | ✅ | ✅ — all route/corpus/local counts reproduce from protected cap literals |
| E9 | `phase-d-native-profile.json` | ✅ | ✅ — task IDs, distinct worktrees, shared common-dir, direct operations and G1–G7/G8 limit match task/worktree records; it is correctly labelled mechanics, not authority |
| E10 | `phase-d-test-output.txt` | ✅ | ✅ — Executor's final runs are confirmed by direct task output; independent Reviewer runs are also green |

RF §5 has one direct EV reference, verified 1/1. Its nine attached evidence files are also verified 9/9.

## Knowledge Citations Verified

All PV priorities 0–4 were read in full; priorities 5–7 were read for the cited and Phase-D-relevant items. `KNOWLEDGE.md` Architecture Map contains no contradiction with the Candidate: D73–D75 selective/copy semantics, D76 immutable VALUE, D77 crossing/isolation, D79 navigation-only title, D80 principal identity and D81 human-rooted authority are preserved.

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | Master HL §7.2 #1–4 | PV0 NS1, NS2 principles 4/6, NS3 | ✅ | ✅ | ✅ — purpose, bounded delegation, proportional assurance and non-vendor/runtime boundary match | ✅ — direct authority, stopping and provider-neutrality |
| 2 | Master HL §7.2 #5–7 | PV1 Structural Enforcement, Naming Creates Behavior, Portability | ✅ | ✅ | ✅ | ✅ — artifact gates, self-describing grants and neutral handles |
| 3 | Master HL §7.2 #8–9 | PV2 `philosophy.md` F37/F38 | ✅ | ✅ | ✅ | ✅ — no self-widening mandate; finite Coordinator attention |
| 4 | Master HL §7.2 #10–16, #33–35 | PV3 D59, D68, D63, D64, D55, D54, D31, D73–D75 | ✅ | ✅ | ✅ — each exact architecture item says what the HL attributes to it | ✅ — authority/identity separation, immutable traces, frozen claims, selective reads and exact copies |
| 5 | Master HL §7.2 #17–19 | PV4 HL Contract rules 17–21 and §14 | ✅ | ✅ | ✅ | ✅ — budget/phase derivation and prohibited-pattern enforcement bound the task |
| 6 | Master HL §7.2 #20 | PV5 `convention.md` naming consistency | ✅ | ✅ | ✅ | ✅ — vocabulary remains stable and Phase E owns the later sweep |
| 7 | Master HL §7.2 #21–23, #36 | PV6 `process.md` F6, F7, F30, F39 | ✅ | ✅ | ✅ | ✅ — direct durable assignment and consumer census prevent coordination drift |
| 8 | Master HL §7.2 #24–32 | PV7 `constraint.md` F11/F12/F2; `risk.md` F1; `stakeholder.md` F6/F7/F8; `environment.md` F3/F4; Assisted team README | ✅ | ✅ | ✅ — including F11 as an explicitly outdated measured claim reserved for Phase E correction | ✅ — compactness, persistence, native-profile boundary and edition distinction |
| 9 | Phase HL §7.2 #1–18 | PV0 NS1/NS3; PV1 values/success; PV2 F37/F38; PV3 D63/D73/D74/D75/D76/D77/D79/D80/D81; PV4 HL Contract/§6/§15 | ✅ | ✅ | ✅ | ✅ — these are the exact authority, activation, budget, copying and Role Lock constraints implemented and tested |
| 10 | Phase HL §7.2 #19–31 | PV5 F4/F5/F19; PV6 F6/F7/F30/F39/F40/F41; PV7 constraint F2/F12, stakeholder F6/F7/F14, environment F6 | ✅ | ✅ | ✅ | ✅ — every application maps to a real receive/report/copy/census/cap/profile boundary |
| 11 | ONB §7 #1–31 | Exact back-references to the 31 Phase-HL citations above | ✅ | ✅ | ✅ — every ONB note preserves the cited item's meaning | ✅ — each note is tied to a concrete implementation or assurance action |

Citation records checked: 98; resolved: 98; semantically verified: 98; irrelevant: 0; hallucinated: 0.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈18 × 0.42⌉ files and recorded findings? — 18/18.
- [x] Ran at least 1 build/test command (or documented why not)? — targeted pytest, full pytest, and direct MkDocs.
- [x] Claim & Source Checks filled — 3 load-bearing claims checked, every citation traced, numeric claims re-derived from primary Git/source objects.
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — no contradiction with changes.
- [x] Knowledge Citations from master/phase HL §7.2 and ONB §7 verified?
  - Total: 98, resolved: 98, semantically verified: 98, irrelevant: 0, hallucinated: 0.
- [x] Evidence artifacts from RF §5 verified?
  - Total: 10 (1 direct EV + 9 attachments), verified: 10, missing: 0.

Stage complete: YES
