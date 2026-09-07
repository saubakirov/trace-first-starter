# Verify rev4 — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF Candidate files claimed: 3
> Files to verify: ⌈3 × 0.42⌉ = 2; verified: 3/3 (100%)

## Verification Log

### V1: `.tfw/conventions.md`
- **RF claim:** The collision/readback/fail-soft contract applies after rendering, to ordinary `BASE`
  and qualified `LEAD_BASE` alike.
- **Actual:** The source defines `RENDERED:=BASE|LEAD_BASE`, evaluates duplicate titles against that
  value, appends the shortest unique stable-key prefix only when needed, claims success only after
  exact readback, and otherwise reports once and continues unclaimed.
- **Match:** ✅

### V2: `docs/scripts/test_runtime_context.py`
- **RF claim:** Source-derived coverage proves duplicate qualified roots `ab7`/`ac9` render `· @ab`,
  exact readback claims, no-key and altered-readback fail soft, and ordinary root/child Plan/Resume
  behavior remains.
- **Actual:** The independent oracle produced exact `LEAD · cratm-main · CRATM · D · @ab` for the
  qualified collision; exact readback claimed it; no-key and altered-readback each emitted one report
  and remained unclaimed. Ordinary `BASE` collision, no-key, readback-unavailable and altered-readback
  probes behaved identically. Root Plan/Resume, same-principal child, child Coordinator, stale and
  forwarded routes retained their expected projections. All 23 navigation mutants changed output and
  were rejected; the wider 75-mutant Phase-D set also changed output and was rejected.
- **Match:** ✅

### V3: `docs/scripts/test_integration.py`
- **RF claim:** The continuation guard admits only the finite rev3/rev4 review surface, cumulative
  ONB/EV/RF, seven exact attachments per round, status and valid phase journals, while rejecting
  arbitrary review/evidence/product/assurance/malformed TRACE paths.
- **Actual:** The guard contains exact path constants plus a closed journal filename grammar. A direct
  47-positive matrix admitted exact rev3/rev4 REVIEW and all three stage files, cumulative ONB/EV/RF,
  status, 14 attachments and 21 valid journals with zero misses. A 14-negative matrix rejected future
  review revisions and stages, arbitrary evidence, unsuffixed attachments, product/assurance paths,
  malformed or nested journals, unrelated trace and notes with zero false accepts.
- **Match:** ✅

### V4: immutable Candidate, membership and arithmetic
- **RF claim:** Replacement Candidate `fac67ef443c5cb50a766cc6c6c639ea60a259437` is the first tested
  implementation after the accepted return, changes exactly the ruled three paths, and preserves the
  approved 21-path VALUE selector at 463 + 464 = 927 touched text LOC.
- **Actual:** Approval → ruling → ONB acceptance → Candidate → EV/RF → RF transition → review dispatch
  is a single ancestor chain. Candidate parent is `4c10fc04c266ae896c2b25d11dc1d63b05b8df2f`;
  Candidate-own paths are exactly the one VALUE and two ASSURANCE files in V1–V3. The approved literal
  selector independently decoded 21 MODIFY/VALUE paths, no missing/extra/binary rows, and 463 additions
  + 464 deletions = 927. Approval→Candidate contains only 21 VALUE, two ASSURANCE and 21 legal TRACE
  paths; Candidate→dispatch contains 12 TRACE paths; all 23 selected VALUE/ASSURANCE blobs at dispatch
  equal Candidate.
- **Match:** ✅

### V5: protected history, cumulative trace and attachments
- **RF claim:** Frozen inputs, earlier phases, protected release/config/knowledge paths and cumulative
  Round-1–4 trace remain intact; the exact Round-4 evidence set exists.
- **Actual:** Seven frozen inputs match approval byte-for-byte; cumulative ONB/EV/RF retain the approval
  byte prefix; 13 pre-approval journals, 61 Phase A–C paths, and 22 protected release/config/knowledge
  paths match approval; Phase E is absent. All seven `phase-d-round4-*` attachments exist and were read.
- **Match:** ✅

### V6: A5 context and warning boundary
- **RF claim:** Active corpus is 33,682/33,749 words, central range 166/260, all local workflow deltas
  stay below 45%, and only exact occurrence counts for 24 pre-existing MkDocs warning tokens are claimed.
- **Actual:** Direct measurement reproduced 33,682/33,749 and 166/260. Workflow-local deltas are plan
  −152, research −137, handoff −37, review −65, resume −77, docs −36 and init −54, each below 45%.
  Independent Git-object counts reproduced all 24 token counts with zero mismatches; no full-log
  equivalence is inferred.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `python -m pytest docs/scripts/test_runtime_context.py -q -k 'phase_d_root_lead or rtpsn_phase_b' --disable-warnings --maxfail=1` | PASS — 8 passed, 181 deselected in 49.51s |
| 2 | `python -m pytest docs/scripts/test_integration.py -q -k 'phase_d_continuation or phase_d_literal_value_assurance or phase_d_approval_epoch or phase_d_release_config' --disable-warnings --maxfail=1` | PASS — 4 passed, 114 deselected in 164.92s |
| 3 | `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_integration.py -q -k 'phase_d' --disable-warnings --maxfail=1` | PASS — 22 passed, 285 deselected in 225.02s |
| 4 | `python -m pytest .tfw/scripts/ docs/scripts/ -q --disable-warnings --maxfail=1` | PASS — 668 passed, 1 skipped in 555.14s |
| 5 | `python -m mkdocs build --strict -f docs/mkdocs.yml --quiet` | PASS — exit 0; known warnings retained |
| 6 | approved literal NUL-safe Baseline→Candidate selector | PASS — 21 paths; 463 + 464 = 927; no missing, extra or binary rows |
| 7 | direct collision, navigation-mutant and finite-continuation matrices | PASS — all required positives accepted; every output-changing negative rejected |
| 8 | approval/history/blob/cumulative-prefix comparisons | PASS — zero protected-path or prefix mismatches |
| 9 | exact 24-token Git-object occurrence comparison | PASS — 24/24 tokens, zero count mismatches |
| 10 | `git diff --check` | PASS — no whitespace errors |

The mandated continuation test against a committed review tip is deliberately not discharged by these
pre-commit runs. It is the Decide-stage post-commit gate and will be recorded in REVIEW rev4 after the
first exact-path review commit.

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | Replacement Candidate is the first tested implementation after accepted Round-4 ONB and before trace-only commits | RF Round 4 §1 accounting | Immutable Git parent/ancestor chain from `61c7364…` through `35e75d3…` | ✅ |
| C2 | VALUE result is exactly 21 paths and 927 touched text LOC | RF Round 4 §1 accounting; EV R4-E-accounting | Approved selector replay against Baseline `8e68ab3…` and Candidate `fac67ef…` | ✅ |
| C3 | A5 and warning claims are bounded to the stated measures | RF Round 4 §4; attachments | Direct source-word measurement and exact Git-object counts for the 24 named tokens | ✅ |

Every citation in the reviewed HL/ONB surface traces to an existing local artifact. Numeric claims above
were checked against immutable Git objects or current primary source files, not accepted from RF prose.

## Discrepancies Found

No discrepancies.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | EV R4-E1; `phase-d-round4-scenarios.json`, `phase-d-round4-mutants.json` | ✅ | ✅ — collision/readback/fail-soft and retained navigation cases reproduced |
| E2 | EV R4-E2; scenarios, mutants and `phase-d-round4-test-output.txt` | ✅ | ✅ — finite continuation positives/negatives and Phase-D suite reproduced |
| E3 | EV R4-E3; test output and `phase-d-round4-mkdocs-baseline.json` | ✅ | ✅ — targeted/full suites, strict build and exact warning-count boundary reproduced |
| E4 | EV R4-E-accounting; accounting, WIP and A5 attachments | ✅ | ✅ — lineage, 21/927 selector, history and A5 values reproduced |

Round-4 evidence verdict independently remains 4/4 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A. All seven
Round-4 attachments exist; cumulative EV/RF paths resolve and retain their prior byte prefixes.

## Knowledge Citations Verified

PV priorities 0–4 were scanned in full and priorities 5–7 by cited relevance. The 38 master-HL rows,
11 Phase-D-HL rows and 31 ONB §7 rows are 80 real, semantically matching, relevant citation items.
The 28 explicit Markdown links across those sections resolve to files; README anchors `ns1`, `ns2`,
`ns3`, `methodology-values` and `success-criteria` exist. The Round-2 and Round-4 ONB deltas preserve
and apply those citations rather than introducing unresolved items.

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | Master HL §7.2 #1–4, #37 | PV0 NS1–NS3; PV1 Success Criteria | ✅ | ✅ | ✅ — purpose, bounded authority, portability and proportional assurance are separate clauses | ✅ — governs visible continuation and human return |
| 2 | Master HL §7.2 #5–7 | PV1 Methodology values | ✅ | ✅ | ✅ — Structural Enforcement, Naming Creates Behavior and Portability are quoted accurately | ✅ — gates live in files while names remain non-authoritative |
| 3 | Master HL §7.2 #8–19, #33–35, #38 | PV2 F37/F38; PV3 D31/D54/D55/D59/D63/D64/D68/D73–D75/D80–D82; PV4 HL Contract/§14 | ✅ | ✅ | ✅ — authority, identity, trace, context and review meanings match | ✅ — these are the contracts Round 4 preserves |
| 4 | Master HL §7.2 #20–32, #36 | PV5–PV7 cited topic facts and Assisted role source | ✅ | ✅ | ✅ — named items and three absence values exist | ✅ — naming, enforcement, source-derived coverage, provider honesty and exact staging apply |
| 5 | Phase-D HL §7.2, 11 rows | PV0–PV7 and master A7 | ✅ | ✅ | ✅ — cited ranges F4/F5/F19, F6/F7/F30/F39–F41, F2/F12, F6/F7/F14 and D63/D72–D82 exist | ✅ — directly constrains the Phase-D implementation and return |
| 6 | ONB §7, 31 rows plus Round-2/Round-4 deltas | Exact Phase-HL cascade | N/A — references inherit the resolving Phase-HL links | ✅ | ✅ — every named clause/fact was independently located and read | ✅ — each row states the concrete Executor action or preserved bound |

No citation is irrelevant or hallucinated, and current KNOWLEDGE.md introduces no contradiction with
the replacement Candidate. In particular, D72 governs the Rung-1 return, D79 keeps titles navigation-
only, D80–D82 keep principal/unit/authority/admission separate, and D77 plus risk F1 require exact-path
review staging.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈3 × 0.42⌉ files and recorded findings (3/3 Candidate files)?
- [x] Ran at least 1 build/test command?
- [x] Claim & Source Checks filled — key claims checked, every citation traced, data checked against primary sources?
- [x] Each RF §3 checkmark verified against actual files?
- [x] KNOWLEDGE.md checked — no contradiction with changes?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total: 80, resolved: 80, semantically verified: 80, irrelevant: 0, hallucinated: 0
- [x] Evidence artifacts from RF §5 verified?
  - Total Round-4 evidence items: 4, verified: 4, missing: 0; attachments: 7/7

Stage complete: YES
