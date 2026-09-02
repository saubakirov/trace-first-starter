# Verify rev2 — "Does the remediation close D1?"
> **Mindset:** Auditor. The revised RF is a declaration, not a fact.
> **Test:** "Can an independent replay establish AC-1 without inventing the missing original history?"
> Prior finding: [REVIEW__TFW_20260830-202031_FA15ES.md](../../REVIEW__TFW_20260830-202031_FA15ES.md) §4 D1
> Reviewed Executor head: `c623b79a632d11a3d396c2e74ac75f2ecaaffd23`
> Revised RF object: `c623b79a632d11a3d396c2e74ac75f2ecaaffd23:workspace/2026/TFW_20260830-202031_FA15ES/RF__TFW_20260830-202031_FA15ES.md`
> Product paths claimed: 30
> Revised paths claimed: 8
> Files verified: 30/30 product paths, 8/8 revised RF/evidence paths, and all retained contract/evidence surfaces needed for regression checks

## Verification Log

### V1 — reviewed revision identity, exact scope, and role boundary
- **RF claim:** Executor remediation is evidence-only and leaves product commit `626d77b5c3261dff493d15c7ce5862b9e036d10e` unchanged.
- **Actual:** Reviewed Executor branch `codex/tfw-fa15es-executor` at clean HEAD `c623b79a632d11a3d396c2e74ac75f2ecaaffd23`, whose parent is exactly `23509e8c4130359f2bc3ba1a3d3863ee3ab5bd7e`. Its diff contains 8 task-local paths: RF, EV, source-integrity, the clean-replay report, the replay harness, two aggregate JSON files, and result JSON. `git diff 626d77b5… c623b79a… -- editions` is empty. The Reviewer stayed on `codex/tfw-fa15es-reviewer`; no Executor commit was merged, rebased, or cherry-picked.
- **Match:** ✅

### V2 — clean replay from the exact product parent
- **RF claim:** A clean replay based on `e5e20f5b1070f48740d7d47bdd264ccc66ee524d` persists the complete source aggregate immediately before and after the same materializer and passes.
- **Actual:** The committed result records the exact base, expected branch, materializer exit 0, and `PASS`. I independently created a different disposable checkout at `E:\TEMP\tfw-fa15es-reviewer-replay-b2cf2f285c19400e92aa951984b30c6e`, checked out the exact parent on the required branch name, copied the exact committed harness/materializer blobs, supplied the owner source out-of-band, and ran the harness. It returned exit 0 and `CLEAN_REPLAY_VERDICT=PASS`.
- **Match:** ✅

### V3 — complete source state and temporal ordering
- **RF claim:** The replay covers all 28 source rows, including the four private rows without publishing per-row private hashes, and measures immediately around materialization.
- **Actual:** Both committed aggregates contain `28 files / 297,522 bytes` and aggregate SHA-256 `5c609354c68e8043b121b75ee4ad4a5ced70908462ed3f1ba2c82c03b3195bf2`; `private_rows_covered` is true, private per-row data and source locators are absent. The harness constructs ordinal `relative|size|sha256` rows with normalized POSIX paths and a final LF, persists the pre record once using exclusive creation, flush, and `fsync`, launches the same materializer subprocess, computes/persists post immediately after it, and checks equality before routing-evidence writes. The initial `runpy` call only loads guarded constants/target logic; the materializer's `main` is not invoked there. Fresh replay reproduces the same count, bytes, aggregate, and pre/post equality.
- **Match:** ✅

### V4 — no source writes and exact delivered-product equivalence
- **RF claim:** The replay has zero source write targets and its complete product is identical to `626d77b5…`.
- **Actual:** The materializer resolves all 28 materialization writes/deletes through product-confined paths under `editions/`; it has no source write operation. The committed and fresh replay results both record `source_write_targets: []`. Each replay yields 30 product paths / 293,321 bytes / aggregate `5944aa9b1fcf4f2816cc562d6e0b5cd16b6e09a52c8d0b542efb26f01515b532`, with no missing, extra, or mismatched path and expected Git tree OID `8c12e1c66f5d961de44dbc9c9a0d3cd54bd06cdc`. Thus the source-bracketed materialization plus the two post-measurement routing files reproduces the entire delivered `editions/` tree exactly.
- **Match:** ✅

### V5 — honest classification and evidence sanitization
- **RF claim:** The original historical limitation remains disclosed; the new proof is classified as a clean replay rather than an original observation.
- **Actual:** Revised RF, EV, source-integrity, and clean-replay report all state that the original private-inclusive prewrite aggregate was not preserved. They identify the new run as clean replay evidence and do not backdate it. Strict UTF-8/privacy scans across all eight revised paths found zero control bytes, source-locator markers, organization markers, or exact private record paths. JSON parses; the harness compiles. The public aggregates prove coverage without disclosing the four private row hashes.
- **Match:** ✅

### V6 — retained product and regression holdings
- **RF claim:** Evidence remediation does not weaken any prior product holding.
- **Actual:** Re-running the branch-locked verifier at Executor HEAD returns `VERDICT=PASS`: 30 product paths; 24 files / 260,872 bytes; 17 adapted files / 136 hunks / 205 changed / 1,900 unchanged lines; six exact copies; source 28 / 297,522 / `5c609354…`; 9 links / 0 broken. A fresh fixture run returns PASS with protected equality and all binding/acquisition states. The repository suite returns `322 passed, 1 skipped`; 323 tests collect. Task schema validates 58 tasks. The Executor worktree remains clean.
- **Match:** ✅

### V7 — revised trace completeness and prior debt
- **RF claim:** RF/EV now cite the clean replay and retain the sole observation about inherited trailing whitespace.
- **Actual:** All eight revised paths exist in the reviewed Git object; the revised task-relative link scan finds 85 checked / 0 broken. The one product `git diff --check` result remains the same source-preserved blank line in `презентация.html:168`; it is outside the hunk allowlist, has no rendered effect, and was already disposed `not material` in the first REVIEW. No new debt or discrepancy was found.
- **Match:** ✅

## Independent commands and operations

| # | Command / operation | Result |
|---|---------------------|--------|
| 1 | Git identity/scope checks at Executor `c623b79a…` | clean head; exact parent `23509e8c…`; 8 task-local evidence/RF paths; zero `editions/` delta |
| 2 | Fresh disposable clean replay from `e5e20f5…` using exact committed harness/materializer | exit 0; pre/post 28 / 297,522 / `5c609354…`; zero source writes; exact product tree; PASS |
| 3 | Structured diff of fresh and committed replay results | verdict, source totals/aggregate, zero-write set, product totals/aggregate, path census, and Git-tree equality all match |
| 4 | Strict UTF-8, control-byte, organization/source-locator/private-path scan over 8 revised paths | zero prohibited findings |
| 5 | Branch-locked `verify_assisted.py` | PASS; all product/source/diff/link totals retained |
| 6 | Fresh standalone/binding/acquisition fixture run | PASS; 24 / 260,872; protected equality; all states pass |
| 7 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | 322 passed, 1 skipped in 255.63 s; exit 0 |
| 8 | pytest collection | 323 tests collected |
| 9 | `python .tfw/scripts/gen_index.py --check tasks` | 58 tasks validate; exit 0 |
| 10 | Compile replay harness and parse all three replay JSON files | PASS |
| 11 | Revised task-relative link scan | 85 checked, 0 broken |

Two initial fixture invocations stopped during Reviewer setup—first before the required source environment was supplied, then because the requested fresh root had not yet been created. Neither reached fixture work or changed product state. The corrected invocation used a pre-created empty unique root and produced the PASS recorded above.

## Claim & source checks

| # | Claim | Holds? | Basis |
|---|-------|--------|-------|
| C1 | A complete 28-file pre/post source manifest exists for an implementation run | ✅ | Committed and independently reproduced clean replay: identical normalized path/size/SHA-256 aggregate immediately around materialization |
| C2 | The clean replay is not being passed off as the original historical run | ✅ | Explicit limitation and classification in revised RF, EV, source-integrity, and replay report |
| C3 | The replay corresponds to the delivered product | ✅ | Complete 30-path/293,321-byte product aggregate and Git tree OID equal `626d77b5…:editions` |
| C4 | The source was not written by the replay | ✅ | Empty source-write target set, product-confined materializer paths, equal source aggregates |

## Evidence verification

| # | Revised object path at `c623b79a…` | Exists? | Matches claim? |
|---|-------------------------------------|---------|----------------|
| E1 | `RF__TFW_20260830-202031_FA15ES.md` | ✅ | ✅ — candid historical limitation plus bounded remediation claim |
| E2 | `evidence/EV__TFW_20260830-202031_FA15ES.md` | ✅ | ✅ — AC-1 index now points to replay and source-integrity evidence |
| E3 | `evidence/source-integrity-and-preservation.md` | ✅ | ✅ — retains limitation and reports replay separately |
| E4 | `evidence/clean-replay-source-immutability.md` | ✅ | ✅ — commands, ordering, outcomes, scope, and classification are complete |
| E5 | `evidence/attachments/replay_source_immutability.py` | ✅ | ✅ — rerun succeeds; ordering and confinement inspected |
| E6 | `evidence/attachments/replay-pre-source-aggregate.json` | ✅ | ✅ — complete redacted aggregate before materialization |
| E7 | `evidence/attachments/replay-post-source-aggregate.json` | ✅ | ✅ — same complete aggregate after materialization |
| E8 | `evidence/attachments/replay-result.json` | ✅ | ✅ — zero writes and exact product/tree comparison; fresh result agrees |

## Discrepancies Found

None. Prior D1 is closed by a new, independently reproducible implementation run from the exact product parent. The absent digest from the original run remains a truthful historical limitation, but AC-1 does not require the first attempted run to be the only qualifying run; it requires a pre/post manifest comparison around implementation. The clean replay supplies that comparison and proves its output is the delivered product byte-for-byte.

## Checkpoint

**Self-check:**
- [x] Read all revised RF/evidence blobs from the exact reviewed Executor commit?
- [x] Reproduced the clean replay in a new disposable checkout rather than trusting committed JSON?
- [x] Verified temporal ordering, full private-inclusive coverage, sanitization, zero source writes, and exact delivered-product equivalence?
- [x] Re-ran product verifier, fixtures, repository tests, schema, link, encoding, and privacy checks in proportion to regression risk?
- [x] Distinguished the original historical limitation from the new qualifying implementation run?
- [x] Checked the prior REVIEW debt disposition and found no new debt?

Stage complete: YES
