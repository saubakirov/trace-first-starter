# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Files were opened, commands were rerun, and claims were compared with the product commit and the read-only field source.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF product paths claimed: 30
> Files required: 13
> Files verified: 30/30 product paths, 13/13 evidence artifacts, and all cited contract/source artifacts (100% verification)

## Verification Log

### V1 — product commit, branch, and exact scope
- **RF claim:** Product commit `626d77b5c3261dff493d15c7ce5862b9e036d10e` changes exactly 30 product paths, all under `editions/`, with 1 added, 24 modified, 5 deleted and `+1,917/-853` lines.
- **Actual:** The commit parent is `e5e20f5b1070f48740d7d47bdd264ccc66ee524d`. Independent `git diff-tree`, `git diff --name-status`, and `git diff --numstat` calculations reproduce `A=1`, `M=24`, `D=5`, `TOTAL=30`, `+1,917/-853`; no product path exists outside `editions/`. The evidence commit `23509e8c4130359f2bc3ba1a3d3863ee3ab5bd7e` adds no later product change. Reviewer work began from that exact HEAD on `codex/tfw-fa15es-reviewer`.
- **Match:** ✅

### V2 — complete source manifest and immutability claim
- **RF claim:** AC-1 is verified because the owner-supplied field source is 28 files / 297,522 bytes and a private-inclusive aggregate SHA-256 `5c609354c68e8043b121b75ee4ad4a5ced70908462ed3f1ba2c82c03b3195bf2` matches before and after the final product commit.
- **Actual:** A fresh read-only reviewer census reproduces 28 files / 297,522 bytes and the same aggregate. It also reproduces all 24 non-private frozen research size/hash rows. The materializer resolves all write/delete targets under `editions/` and has no field-source write operation; Git records only repository changes. However, the first persisted private-inclusive digest is the pre-commit value, not a pre-implementation value. Frozen research says all hashes were computed read-only but deliberately withholds the four private per-record hashes and does not persist a private-inclusive aggregate. The Executor's earliest durable record contains the count/bytes census and non-private baselines only. A current rerun and the two late Executor reads cannot reconstruct the four private values as they existed before implementation.
- **Match:** ❌ — product/source non-mutation is strongly supported, but the exact historical pre/post manifest equality required by AC-1 is not proven.

### V3 — frozen disposition ledger, exact copies, and bounded adaptations
- **RF claim:** The 35 frozen dispositions produce 17 bounded adaptations with 136 hunks, 205 changed source lines and 1,900 unchanged source lines, plus six exact copies.
- **Actual:** The TS path table contains 35 dispositions and 30 writes. An independent parser of frozen research E2 ran Git no-index diffs for every one of the 17 source→target pairs with the frozen diff options; it returned `FILES=17`, `HUNKS=136`, `CHANGED_SOURCE_LINES=205`, `SOURCE_LINES=2105`, `UNCHANGED=1900`, `RANGE_MATCH=PASS`. Six exact source→target hashes match. The 24-file shipped package is 260,872 bytes. The five expected deletions are absent.
- **Match:** ✅

### V4 — privacy and neutral public derivative
- **RF claim:** Private records, company identity, source logo/palette, personalized project data, and local state do not ship or leak through evidence/renders/metadata.
- **Actual:** The four private source records are absent from the package and their exact source-relative paths have zero matches across the product and committed evidence. Independent scans found zero field-organization markers, zero absolute field-source markers, zero concrete UUIDs or task IDs in product files, zero common credential/private-key patterns, and zero prohibited control bytes. `PROJECT.md` is visibly uninitialized; `team/` contains only its neutral README; `knowledge/INDEX.md` describes an empty initial state. Both inspected committed renders use the neutral TFW mark and contain no field brand/logo.
- **Match:** ✅

### V5 — version, lifecycle, identity, and binding contracts
- **RF claim:** Assisted is a truthful standalone 1.6 with all five prompt-first skills, independent lifecycle/identity behavior, and an isolated Assisted binding namespace that never converges with Full or legacy state.
- **Actual:** `VERSION` is the exact four-byte `1.6\n` source copy. `CHANGELOG.md` retains every 1.0–1.6 heading and the version-specific migration history. All five `SKILL.md` files and five metadata files exist and agree with `AGENTS.md`, `README.md`, `PROJECT.md`, `MIGRATION.md`, and `team/README.md`. The identity contract is self-contained and prompt-only, validates profiles/bindings fail-closed, keeps Full and legacy stores inert, supports fixed/ask/missing/invalid/foreign-lock/shared-device states, and requires session-only fallback when safe local persistence cannot be established. The only shipped executable is the optional artifact builder `шаблоны/build_a4.py`; there is no identity, lifecycle, update, maintenance, or synchronization runtime.
- **Match:** ✅

### V6 — provider-neutral maintenance and current release truth
- **RF claim:** Forward updates require an exact versioned source, dynamic observed manifest, immediate recheck, one human Gate, protected preservation, and explicit origin limitations; reverse flow is candidate-only and does not mutate public core. No GitHub Release is claimed to exist.
- **Actual:** `editions/ASSISTED_MAINTENANCE.md`, `editions/README.md`, `README.md`, `MIGRATION.md`, and `tfw-update/SKILL.md` encode those boundaries consistently. Fresh local/Drive-like/GitHub-like/archive fixtures pass; drift, unsafe path, collision, and incomplete input stop; reverse flow creates only a generic candidate. The repository's official GitHub Releases page currently states that there are no releases, matching the product's explicit non-claim.
- **Match:** ✅

### V7 — standalone copied starter and protected-state fixtures
- **RF claim:** Copying the 24-file package to a clean root yields an independently usable starter whose protected state and sibling binding namespaces are preserved.
- **Actual:** A fresh reviewer fixture in `E:\TEMP\tfw-fa15es-review-1676638aa7f64f4dad23a59945bda396` reproduced `24 files / 260,872 bytes`, an uninitialized project, zero human profiles, no `workspace/`, four A4 pages, four slides, byte-identical protected sentinels, and the expected binding/acquisition stop states. The fixture runner models prompt-defined state transitions; therefore its result was accepted only together with direct inspection of the five skill contracts and their cross-document surfaces, not as a substitute for those contracts.
- **Match:** ✅

### V8 — templates and committed render evidence
- **RF claim:** The package contains the complete neutral note, plan, A4, and presentation templates plus the artifact-only builder; rendered evidence shows 4/4 pages, 4/4 slides, 5/5 passive marks, no clipping, and passing contrast.
- **Actual:** The builder and all four practical templates are among the 17 bounded source adaptations; V3's independent hunk/range check confirms that only their allowlisted neutralization/path surfaces changed and their remaining source lines stayed intact. Both committed full-page PNGs were opened at original resolution. All four A4 pages and all four slides are visibly present, readable, neutral, and unclipped; five passive marks are referenced by the HTML/A4 outputs. Re-running the contrast helper reproduces PASS at 4.5:1 ordinary and 3:1 large-text thresholds. The lower slide-index/pause-index ratios are ancillary/incidental labels and do not carry the slide's semantic content.
- **Match:** ✅

### V9 — links, encoding, and the recovered control-byte defect
- **RF claim:** Product links resolve, UTF-8/control-byte checks pass, and the malformed Python escape sequence was corrected before the final product commit.
- **Actual:** An independent Markdown/HTML relative-link scan found `9 checked / 0 broken`. Strict UTF-8 decoding of product/evidence text succeeds and the prohibited control-byte census is zero. Executor reflog shows the initial unpublished product commit `683a9608b12b229ae0e08fe6a11885413621d893` followed by amended product commit `626d77b…`; their diff contains only the binding-path line in `CHANGELOG.md`, replacing the tab/bell/backspace-corrupted literal with `%LOCALAPPDATA%\tfw\assisted\bindings.yml`. No control byte remains.
- **Match:** ✅

### V10 — the sole `git diff --check` finding
- **RF claim:** Presentation source line 168 is a blank line with four inherited trailing spaces outside the frozen allowlist; preserving it is required and it is the sole whitespace finding.
- **Actual:** The source and target line are byte-equal and contain four spaces. `git diff --check e5e20f5b… 626d77b… -- editions` returns only `editions/02-assisted/шаблоны/презентация.html:168: trailing whitespace`. Removing it would add an unapproved 137th hunk and reduce source-preserved unchanged lines. The byte has no rendered or behavioral effect.
- **Match:** ✅ — disclosed, source-preserved, and not material.

### V11 — repository tests, schema, and frozen contract integrity
- **RF claim:** Repository tests/schema pass and the implementation stays inside the frozen HL/TS contract.
- **Actual:** `python -m pytest .tfw/scripts/ docs/scripts/ -q` returns `322 passed, 1 skipped`; `python .tfw/scripts/gen_index.py --check tasks` validates 58 tasks with only the documented informational phase-state notices. Frozen HL §§1, 3, 4, 5, 6 and 7.1 are byte-equal to refreeze commit `2b5f2e8e7ab84b7035ec1eb397ea91b14b48d62d`; §12 is unchanged and remains a valid append-only prefix. Product budgets are below all frozen ceilings. The independent Reviewer task, exact branch/base, and exact-path staging satisfy AC-11's role and staging boundary.
- **Match:** ✅

## Commands Executed

| # | Command / operation | Result |
|---|---------------------|--------|
| 1 | `git diff-tree --no-commit-id --name-status -r 626d77b…` plus independent `--numstat` aggregation | 1 A / 24 M / 5 D; +1,917/-853; 30 paths; only `editions/` |
| 2 | Branch-locked `verify_assisted.py` from the saved Executor worktree with the owner-supplied read-only source | `VERDICT=PASS`; 30 paths; 24 files/260,872 bytes; 136/205/1,900; six exact copies; 9/0 links; aggregate `5c609354…` |
| 3 | Independent no-index diff of all 17 E2 source→target mappings | 17 files; 136 hunks; 205 changed; 1,900 unchanged; `RANGE_MATCH=PASS` |
| 4 | Independent ordinal manifest of all 28 source files | 28 / 297,522; aggregate `5c609354…`; 24 disclosed frozen rows match |
| 5 | Fresh reviewer standalone/binding/acquisition fixture run | PASS; 24/260,872; protected equality; expected stop states |
| 6 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | 322 passed, 1 skipped; exit 0 |
| 7 | `python .tfw/scripts/gen_index.py --check tasks` | 58 tasks validate; exit 0 |
| 8 | Independent relative-link scanner over `editions/` | 9 checked, 0 broken |
| 9 | Strict UTF-8, control-byte, privacy, private-path, UUID, and secret-pattern scans | zero prohibited findings in product/evidence; zero control bytes |
| 10 | `git diff --check e5e20f5b… 626d77b… -- editions` | one result: source-preserved blank line 168; exit 2 |
| 11 | `contrast_audit.py` | `CONTENT_CONTRAST=PASS` |
| 12 | Original-resolution inspection of `a4-full.png` and `presentation-full.png` | 4 pages and 4 slides visible; readable, neutral, unclipped |
| 13 | Frozen-section comparison against `2b5f2e8…` | all frozen sections equal; amendment log equal |
| 14 | GitHub Releases page inspection | official page: “There aren’t any releases here” |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | “Pre-implementation and post-implementation manifests … have identical normalized paths, sizes, and SHA-256 values” | TS AC-1; RF AC-1; EV E1 | frozen research E1, source-integrity evidence, current primary field source | ❌ — full pre-implementation private-inclusive value is not durably present |
| C2 | “17 adapted files, 136 hunks, 205 changed and 1,900 unchanged source lines” | TS AC-2; RF AC-2 | frozen research E2 plus independent Git no-index diffs against the primary field source | ✅ |
| C3 | “This repository does not claim that a GitHub Release … already exists” | `editions/README.md`, `ASSISTED_MAINTENANCE.md` | official repository Releases page and current product text | ✅ |

Every remaining numerical RF claim was also reproduced through V1–V11; C1 is the only discrepancy.

## Discrepancies Found

### D1 — required pre-implementation private-inclusive manifest value is absent

TS AC-1 requires the 28-path pre/post manifests to be compared on normalized paths, sizes, and SHA-256 values; its Evidence field requires both source manifest hashes to be recorded. The durable record before implementation contains count/bytes and disclosed non-private baselines, but no aggregate covering the four private rows. Research asserts that hashes were computed but intentionally omits those values and the aggregate. Later matching digests, source-target confinement, and absence of source-write code make mutation unlikely and support the product's integrity, but do not prove the exact historical equality the criterion asks for. This is an evidence-sufficiency defect, not evidence of a product mutation.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|-----------------|-----------------|----------------|
| E1 | `evidence/EV__TFW_20260830-202031_FA15ES.md` | ✅ | ❌ — accurately indexes files but overstates AC-1 as VERIFIED despite the disclosed limitation |
| E2 | `evidence/source-integrity-and-preservation.md` | ✅ | ⚠️ — accurate and candid; establishes late equality and confinement, not the missing pre-implementation aggregate |
| E3 | `evidence/privacy-and-release-audit.md` | ✅ | ✅ — independent scans and changelog inspection agree |
| E4 | `evidence/bindings-and-update-fixtures.md` | ✅ | ✅ — fixture results and direct prompt-contract inspection agree |
| E5 | `evidence/standalone-smoke.md` | ✅ | ✅ — fresh external-copy fixture agrees |
| E6 | `evidence/template-render-audit.md` | ✅ | ✅ — render inspection and contrast rerun agree |
| E7 | `evidence/attachments/materialize_assisted.py` | ✅ | ✅ — branch/path gates and source-read/product-write separation verified |
| E8 | `evidence/attachments/verify_assisted.py` | ✅ | ✅ — rerun unchanged on the exact Executor branch; its historical-manifest limitation is not treated as proof |
| E9 | `evidence/attachments/run_fixtures.py` | ✅ | ✅ — rerun passed; modeled states were corroborated by direct contract reading |
| E10 | `evidence/attachments/contrast_audit.py` | ✅ | ✅ — rerun passed |
| E11 | `evidence/attachments/fixture-results.json` | ✅ | ✅ — structured values match the fresh run except run-specific archive digest/temp path |
| E12 | `evidence/renders/a4-full.png` | ✅ | ✅ — opened at original resolution |
| E13 | `evidence/renders/presentation-full.png` | ✅ | ✅ — opened at original resolution |

## Knowledge Citations Verified

Each row below occurs once in HL §7.2 and once in ONB §7: 30 citation applications, 15 unique citations.

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------|
| 1 | HL K1 + ONB 1 | PV0 — `README.md` opening and How It Works | ✅ | ✅ | ✅ — proportional, independently copyable editions | ✅ |
| 2 | HL K2 + ONB 2 | PV0 — `.tfw/README.md` NS1–NS3 | ✅ | ✅ | ✅ — continuity, human authority, no vendor-bound runtime/bureaucracy | ✅ |
| 3 | HL K3 + ONB 3 | PV1 — Methodology Values: Structural Enforcement, Portability | ✅ | ✅ | ✅ — bounded ledgers and ordinary files | ✅ |
| 4 | HL K4 + ONB 4 | `knowledge/philosophy.md` F14/F32/F36/F43/F45 | ✅ | ✅ | ✅ — methodology over software, preservation, purpose, subtraction | ✅ |
| 5 | HL K5 + ONB 5 | `KNOWLEDGE.md` D57/D58/D59/D68/D70 | ✅ | ✅ | ✅ — Editions topology and independent mechanics | ✅ |
| 6 | HL K6 + ONB 6 | `.tfw/conventions.md` §§3/11/14 | ✅ | ✅ | ✅ — Full contract, scope, usability, anti-drift | ✅ |
| 7 | HL K7 + ONB 7 | `knowledge/convention.md` F10/F20 | ✅ | ✅ | ✅ — self-contained prompts and visibly unknown starter | ✅ |
| 8 | HL K8 + ONB 8 | `knowledge/constraint.md` F10/F11 | ✅ | ✅ | ✅ — standalone editions and Codex-specific visible sessions | ✅ |
| 9 | HL K9 + ONB 9 | `knowledge/process.md` F6/F13/F36 | ✅ | ✅ | ✅ — bounded phase and research trigger | ✅ |
| 10 | HL K10 + ONB 10 | `knowledge/environment.md` F5 | ✅ | ✅ | ✅ — visible separate role topology | ✅ |
| 11 | HL K11 + ONB 11 | `knowledge/risk.md` F1 | ✅ | ✅ | ✅ — shared index and exact staging risk | ✅ |
| 12 | HL K12 + ONB 12 | official Git `diff` documentation | ✅ | ✅ | ✅ — `--unified=0` and zero inter-hunk context behavior | ✅ |
| 13 | HL K13 + ONB 13 | NIST Privacy Framework Core + SP 800-188 | ✅ | ✅ | ✅ — minimization and governed de-identification | ✅ |
| 14 | HL K14 + ONB 14 | Keep a Changelog 1.1.0 | ✅ | ✅ | ✅ — human-relevant version history | ✅ |
| 15 | HL K15 + ONB 15 | WCAG 2.2 SC 1.4.3 | ✅ | ✅ | ✅ — 4.5:1 ordinary, 3:1 large, incidental exception | ✅ |

## Checkpoint

**Self-check:**
- [x] Opened ≥ 13 claimed product files and recorded findings? All 30 product paths were checked.
- [x] Ran at least 1 build/test command? Full repository suite, schema check, product verifier, fixtures, links, contrast, and independent diff/manifests were run.
- [x] Claim & Source Checks filled with key claims, every citation traced, and primary data checked?
- [x] Each RF §3 acceptance checkmark verified against actual files? AC-1 failed proof; AC-2–AC-11 hold.
- [x] `KNOWLEDGE.md` checked? No contradiction found.
- [x] Knowledge Citations verified?
  - Total applications: 30; unique citations: 15; resolved: 30; semantically verified: 30; irrelevant: 0; hallucinated: 0.
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence artifacts: 13; verified without reservation: 11; partial: 1; claim mismatch: 1; missing: 0.

Stage complete: YES
