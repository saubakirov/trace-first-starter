# Verify — “Are the claims true?”

> **Reviewer:** robert, Reviewer task `01a09aaf-9af3-7d13-8ef8-59d3bc84d5e7`
> **R1 review input:** `c02cd3ca1af5d33eea37479ad514d0541e5daafe`
> **Exact R1 return:** `92a78deee082521b1056ef38aa14d51d36a3b649`
> **Candidate:** `65c3c94b2347c69f6d21ac2e2664a39ef46b3ae2`
> **Baseline:** `ec91c56007c20cda79f740fec15c85e4af74d17c`
> **Min verify ratio:** `0.42`
> **RF VALUE files claimed:** `58`
> **Minimum:** `ceil(58 × 0.42) = 25`
> **Actual:** `58/58`; the current-contract discrepancy below triggered 100% verification.

## Verification Log

### V1 — all 58 literal VALUE paths

- **RF claim:** Candidate changes all and only the approved 58 VALUE paths, with 53 MODIFY, four CREATE and one DELETE.
- **Actual:** the approved TS table yields 58 unique literal paths. All 57 current UTF-8 files were opened (764,046 bytes); the one declared deletion, `.tfw/templates/knowledge_state.yaml`, is absent. Per-path planned action equals the NUL-safe Baseline→Candidate status for every row.
- **Match:** ✅ structure, identity and action; semantic discrepancy V8 remains.

Coverage groups opened in full:

| Group | Files | Result |
|---|---:|---|
| Canonical `.tfw/` contracts, templates, workflows, routers and migration | 30 | Opened; current routes and preserved legacy sections distinguished |
| Installed `.agents/` workflow/skill copies | 12 | Opened; affected parity evidence and current affected tests hold |
| Installed `.claude/commands/` copies | 10 | Opened; affected parity evidence and current affected tests hold |
| Root entry and qualified record | 2 | Opened; one current-routing contradiction found in the entry |
| Optional upstream tools | 3 | Opened; removed pending implementation confirmed; one stale current docstring found |
| Documentation generator | 1 | Opened; AC-8 alias implementation and current rendering checked |

### V2 — seven-file AC-8 correction commit

- **RF claim:** commit `65c3c94b...` fixes only the five reviewed historical fragment destinations in existing VALUE/ASSURANCE surfaces.
- **Actual:** the commit has parent `add496c0...`, changes exactly seven files and adds 166/deletes 18 lines. Three canonical/installed knowledge workflows add a retired-destination section; the compilable contract states the bounded alias rule; `gen_docs.py` adds three SLC heading aliases; generator and integration tests check exact IDs, source preservation, ambiguity/collision refusal and all five occurrences. No VALUE/ASSURANCE path changes between Candidate and review input.
- **Match:** ✅

### V3 — AC-8 tests, build and navigation

- **RF claim:** 89 generator tests, 47 selected contract/adapter tests, 18 integration tests, 641-test collection, one production build and five browser observations pass.
- **Actual:** the raw stdout and receipts report exactly `89 passed`, `47 passed, 351 deselected`, `18 passed`, and `641 tests collected`, all exit 0 and bound to the sealed pre-Candidate input. The build receipt exits 0. The five recorded source hrefs reach four unique target IDs; the SLC alias IDs coexist with the current MkDocs IDs.
- **Match:** ✅

### V4 — AC-7 source, prerequisite and preservation

- **RF claim:** one actual replay uses pinned Baseline/Candidate sources, confirms completed SLC, preserves the physical receiver and old/intended bytes, and installs readers before authority retirement.
- **Actual:** source revalidation names exact commits and matching tree maps before the replay clock. SLC receipt identifies accepted REVIEW `99198f1...`, terminal close `c51ee0...`, current `DONE`, active `[workspace]`, historical `[tasks]`, 53 removed pairs absent and 11 unaffected pairs exact. Preservation contains 57 distinct affected physical paths and a whole-receiver archive; source/authority identities and exclusions are explicit.
- **Match:** ✅

### V5 — AC-7 immediate writes and prepared cut

- **RF claim:** every affected write has an immediate actual old/intended comparison; 55 compatible readers precede config/entry retirement; one reader-only cut continues as the same attempt.
- **Actual:** all 116 write records were parsed. All 58 sequence/path pairs agree, each after-hash equals its before-record intended hash, every authority batch matches, and there is no chronology error. The maximum before→after interval is 0.326106 s. Sequences 1–55 exclude config/entry; 56–58 are config retirement, `KNOWLEDGE.md`, and final provenance. There are 57 distinct paths because config is intentionally written twice. The prepared cut and continuation preserve the expected intermediate map.
- **Match:** ✅

### V6 — AC-7 output, repeat, refusal and clock

- **RF claim:** current receiver output opens, an unchanged repeat writes nothing, and changed affected-field Z=17 plus an unrelated note causes a zero-write refusal within one 45-minute attempt.
- **Actual:** the positive receiver build opens six exact pages and preserves the relevant baseline routes. Repeat hashes are equal across 7,035 files with zero writes. Refusal hashes are equal across 7,037 files with zero writes and explicitly preserve Z plus the note. Start is `18:13:50Z`; raw commit is `18:41:23.276348Z` (`1653.276348 s`), final return is `18:53:46.709286Z`; both precede `18:58:50Z`, with zero deductions and no second attempt.
- **Match:** ✅

### V7 — raw/final seals and cumulative reports

- **RF claim:** 174 listed raw hashes equal committed bytes; the final return has exactly 17 report/control paths and preserves prior report epochs as byte prefixes.
- **Actual:** all 174 listed AC-7 hashes match current files, and no AC-7 file changed after raw commit `6b0d5c7...`; that commit contains exactly 175 task-local trace paths including its self-seal. Final commit `92a78dee...` changes exactly 17 declared paths. Fifteen non-recursive declared hashes below 50 MB match; the 57,216,329-byte raw diff was intentionally not re-diffed or normalized. ONB, RF and EV prior prefixes reproduce byte-for-byte.
- **Match:** ✅

### V8 — current knowledge entry and current contract

- **RF claim:** AC-5/9 remain valid: the stable entry and all current consumer routes agree that the global pending/digest Knowledge Gate is retired.
- **Actual:** the new `Current knowledge use`, `Knowledge` architecture row, glossary, plan workflow and scoped successor `TKL-20260913-01` all retire the global gate. D87 and the accepted SLC source retain active/history container semantics only. However:
  - `KNOWLEDGE.md:34` says present-tense `task_containers` governs current work **and the Knowledge Gate**;
  - `.tfw/conventions.md:238` says ordinary discovery **and the Knowledge Gate** search active paths;
  - `tools/tfw_state.py:3-5` says the module computes canonical Knowledge Gate inputs although the Candidate deletes that implementation.
- **Match:** ❌ Material current-policy contradiction. These are current entry/contract/tool descriptions in three approved VALUE paths, not preserved D22/D73/D82 history or the explicitly retired compatibility heading.

### V9 — changed final report rendering

- **RF claim:** cumulative ONB/RF/EV are usable final accepted-output candidates and their new local evidence citations resolve.
- **Actual:** all 57 R1 local link occurrences resolve to 31 existing repository targets. A fresh isolated current-tree build exits 0 in 239.29 s and produces 1,976 HTML files. ONB, RF and EV pages contain their R1 headings and no frontmatter leak. The five corrected href occurrences and all four distinct compatibility IDs are present exactly once at their targets.
- **Match:** ✅ for rendering and the AC-8 destinations. The build still warns that raw JSON evidence is not a documentation input; those local source citations exist and AC-8 does not claim publication of raw evidence. This is a bounded output-family limitation, not an additional verdict condition.

## Commands Executed

| # | Command / independent check | Result |
|---|---|---|
| 1 | `git -c core.longpaths=true rev-parse`, ancestry and ordered commit log | Exact Baseline/Candidate/raw/final/review lineage holds |
| 2 | NUL-safe `git diff --name-status --find-renames=50% -z` over the 58 TS paths | exit 0; 1,793 bytes; SHA-256 `b0f9d3...a8f3a`; 53 M / 4 A / 1 D |
| 3 | NUL-safe `git diff --numstat --find-renames=50% -z` over the 58 TS paths | exit 0; 1,960 bytes; SHA-256 `36fc67...65d5`; +1230/−999 = 2229 |
| 4 | NUL-safe complete Baseline→Candidate name-status | exit 0; 46,342 bytes; SHA-256 `a518f3...785`; 546 logical changes = 58 VALUE + 7 ASSURANCE + 481 TRACE |
| 5 | Parse all 58 TS VALUE rows, open every current file and compare per-path actions | 58 unique; 57 read; one declared deletion absent; no action mismatch |
| 6 | Parse preservation plus all 58 before/after pairs | 57 preserved paths; 58 writes; 55 reader-first; zero hash/authority/chronology mismatches |
| 7 | Re-hash all 174 listed AC-7 raw files and check post-commit drift | zero mismatch; zero later drift |
| 8 | Re-hash final-return files except the intentionally excluded 57 MB raw diff | 15 declared hashes checked; zero mismatch; exact 17 commit paths |
| 9 | Prefix-hash current ONB/RF/EV at the `6b0d5c7...` byte cut | all three exact |
| 10 | `mkdocs build --config-file docs/mkdocs.yml --site-dir C:/Users/c0rpa/AppData/Local/Temp/TFW_TKL_REVIEW_01a09aaf/r1-final-site` | exit 0; 239.29 s; 1,976 HTML files |
| 11 | Parse current final HTML for R1 headings, frontmatter leakage, five hrefs and compatibility IDs | three final pages present; no leak; 5/5 hrefs; each target ID count = 1 |
| 12 | Scan all VALUE text for current/global gate language and compare with scoped successor/current-use/SLC | one connected three-surface contradiction, V8 |

The earlier configured `636 passed, 1 skipped` run remains applicable to unchanged Candidate behavior. Candidate `65c3c94b...` changes only the seven AC-8 files; the current 89/47/18 affected slices cover their generator, contract/adapter and integration dependencies, and current collection succeeds. Under the approved TS's “repeat only when later changes or unresolved concerns warrant it” clause plus D86, a second full suite is not independently warranted; the fresh final build covers the later report-only inputs.

## Claim & Source Checks

| # | Claim / citation checked | Where | Primary artifact | Holds? |
|---|---|---|---|
| C1 | “57 before-image paths, 58 immediate write pairs, 55 reader-first” | RF R1 AC-7 | preservation plus all `07-writes/*` records | ✅ Exact |
| C2 | “58 VALUE, +1230/−999 = 2229, 53M/4A/1D” | RF/EV R1 accounting | approved TS literal selector plus independently rerun Git byte streams | ✅ Exact |
| C3 | “five historical destinations now open” | RF R1 AC-8 | Candidate diff, affected tests, build archive/browser observations and fresh final HTML | ✅ Exact |
| C4 | “all current routes agree and the global gate stops” | RF inherited AC-9 | current `KNOWLEDGE.md`, conventions, glossary, plan, tool source and scoped successor | ❌ V8 |

All R1 report citations resolve to actual local artifacts. No evidence status was accepted solely from a summary receipt.

## Discrepancies Found

### D1 — active Knowledge Gate wording survives in three current VALUE surfaces

The current entry and scoped record correctly say the global planning count/digest gate is retired, while `KNOWLEDGE.md:34`, `.tfw/conventions.md:238` and `tools/tfw_state.py:3-5` still describe active gate behavior. The historical D22/D73/D82 rows are intentionally retained and are not the defect; D87 preserves container routing, not the retired gate. The contradiction is material under AC-5 and AC-9 because a fresh planner or maintainer can follow a current authority surface and perform the exact task-container gate/search that the approved TS forbids, fragmenting ordinary continuation and current policy.

Per the template, D1 escalated verification to all 58 VALUE paths. No second independent discrepancy was found.

## Evidence Verification

| # | RF evidence | Exists? | Matches claim? |
|---|---|---|---|
| E1 | `evidence/r1-ac8/04...07` receipts and streams | ✅ | ✅ exact commands, counts, exits and stream hashes |
| E2 | `evidence/r1-ac8/08-navigation/{manifest,browser-observations}.json` | ✅ | ✅ bounded five-click claim; transcription limitation retained |
| E3 | `evidence/r1-ac8/09-accounting/` NUL streams and JSON | ✅ | ✅ independently reproduced byte hashes and arithmetic |
| E4 | `evidence/r1-ac7/06-preservation.json` and all `07-writes/` pairs | ✅ | ✅ full 57/58/55 chronology and hashes |
| E5 | `08-reader-only-cut`, `09-continuation-checks`, `13-positive-result`, `14-repeat`, `15-refusal` | ✅ | ✅ positive/cut/repeat/refusal identities and zero-write claims hold |
| E6 | `10-mkdocs`, `11-output`, `16-native-result`, `17-raw-seal`, `18-git-seal` | ✅ | ✅ output, limits, paths, clock and raw custody hold |
| E7 | `evidence/r1-return/{native-commit,prior-prefixes,validation,control}.json` | ✅ | ✅ current commits, report epochs and bounded hashes hold |
| E8 | `evidence/coordinator-r1-return/{admission,recovery}.json` | ✅ | ✅ admission/representation claim only; not used as product acceptance |

Total material R1 evidence groups: 8; verified: 8; missing: 0.

## Knowledge Citations Verified

| # | Priority / exact citation | Resolves and exists? | Meaning and relevance |
|---|---|---|---|
| 1 | P0 NS1 | ✅ | ✅ Continuity requires inspectable purpose/grounds; D1 is material on this axis |
| 2 | P0 NS2 2/4/7 and NS3 | ✅ | ✅ simplicity, selected trace, proportionate assurance and non-bureaucracy match |
| 3 | P1 Structural Enforcement, Portability; success 1/3 | ✅ | ✅ ordinary-file routes and qualified continuation match |
| 4 | P2 F21/F32/F42/F43/F45 | ✅ | ✅ explicit outcome, preserved meaning and materiality bar match |
| 5 | P3 D37/D68/D82 | ✅ | ✅ legacy meanings exist; TKL record is their scoped successor for carrier/gate scope |
| 6 | P3 D85/D86 | ✅ | ✅ source-pinned preservation and affected final checks match |
| 7 | P4 HL Contract, Design Rules, Anti-patterns | ✅ | ✅ frozen contract, progressive disclosure, independent review and no bonus fix apply |
| 8 | P5 Convention F23 | ✅ | ✅ English artifact semantics retained |
| 9 | P6 Process F30/F37/F38/F49 | ✅ | ✅ enforcement site, referenced measurements, pre-act bounds and prior research match |
| 10 | P7 Constraint F16 / Stakeholder F6 | ✅ | ✅ no receiver runtime and bounded autonomy match |
| 11 | ADR/Event Sourcing/Git design context | inherited exact R0 check | ✅ unchanged, design context only |
| 12 | Memory overview / Lost in the Middle | inherited exact R0 check | ✅ unchanged, no vendor or performance claim |
| 13 | accepted SLC RF/REVIEW/3.3.0 | ✅ | ✅ exact local sources; corrected compiled fragments now resolve |
| 14 | iteration-2 RES / custody | ✅ | ✅ bounded first-consumer meaning retained |
| 15 | RES D11–D12 / PROV / retry design | ✅ local + inherited external check | ✅ provenance/intent distinction retained |

HL §7.2 and ONB §7 contain 51 link occurrences: 37 local and 14 external; no local target is missing. Total cited rows: 15; resolved: 15; semantically verified: 15; irrelevant: 0; hallucinated: 0. The P3 scan itself exposed D1; a resolving citation did not mask the current contradiction.

## Checkpoint

**Self-check:**

- [x] Opened 58/58 VALUE paths after the discrepancy escalated verification to 100%.
- [x] Independently established evidence applicability and ran the affected final rendering check.
- [x] Spot-checked the four highest-leverage claims against primary local artifacts and traced all citations.
- [x] Re-evaluated all RF AC rows: AC-7 and AC-8 corrections hold; AC-11 remains blocked by D1 through AC-5/9.
- [x] Checked `KNOWLEDGE.md`; the current-entry contradiction is documented rather than silently normalized.
- [x] Verified all 15 knowledge-citation rows and all local link targets.
- [x] Verified all eight material R1 evidence groups; no referenced artifact is missing.

Stage complete: YES

## R2 continuation verification — 2026-09-14

> **R2 review input:** `1409cbdcb8046bcc0a7c0efa727536e5ad6d3e62`
> **Exact Executor return:** `b91ec17f16a1a5ef13171b53a404670c5b9745b2`
> **Tested Candidate:** `a99ba6cd756a7db444f217aef4e5a0eb83faee51`
> **Candidate checkpoint / native pin:** `793cd97f71f484fcbe7c2e01dcfe7503148b402d` / `98a250d28679f43741e97c48556eb1804d812411`
> **Stopped native raw commit:** `1a0a37c443fe0d762a1396f1354d93ac08391637`

The R1 verification above remains the same Reviewer's complete `58/58` VALUE-path audit. R2 changes
only three of those VALUE paths and one approved ASSURANCE path. Those four paths were inspected in
full; all other accepted R1 claims are reused only where their product bytes, oracle, authority and
environment assumptions are unchanged, as D86 permits. No configured suite, full replay or native
case was repeated merely to populate this continuation.

### R2-V1 — identity, authority and Candidate position

- **RF claim:** R2 uses the unchanged approved TS and the first immutable post-fix product Candidate.
- **Actual:** current TS blob is still `f69fd4099a21a07ae2d17e6b5108b04ac94f107e`, approved at
  `2794cbdb40f6c4f3a7d4bce1f8d4eb949d9e6913`. Candidate `a99ba6cd...` immediately follows the
  R2 ONB/control commit `090fa3f7...` and changes exactly `.tfw/conventions.md`, `KNOWLEDGE.md`,
  `tools/tfw_state.py` and `docs/scripts/test_repository_contracts.py`. It precedes checkpoint,
  native custody, RF/EV and final review dispatch. None of the 58 VALUE or seven ASSURANCE paths
  changes between Candidate and exact Executor return.
- **Match:** ✅

### R2-V2 — corrected current descriptions and affected guard

- **RF claim:** AC-5/9's three current descriptions no longer activate the retired global gate,
  while historical D/topic/changelog/compatibility meaning remains readable.
- **Actual:** the Task Storage row now ends current authority at `task_containers` governing current
  work; the unique `Where tasks live` section limits active containers to ordinary discovery; the
  maintained state-reader docstring describes only declared-carrier reads and whole-identifier
  resolution. Direct selection of those three current carriers finds no active gate sentence.
  Historical D22/D73/D82 and old task-index rows still contain their dated gate wording. The new
  AST-based guard selects only the unique current carriers, accepts explicit retirement, rejects a
  separate active sentence, and restores each Baseline claim as a rejecting mutant without importing
  historical code.
- **Affected evidence:** the exact Candidate-bound receipt records `25 passed in 1.19s`, exit 0, with
  empty stderr. The guard itself and all three product edits were independently read; rerunning the
  same passing tests was not needed for this review.
- **Match:** ✅ AC-5 and the affected AC-9 current-surface claim.

### R2-V3 — immutable VALUE accounting

- **RF claim:** Baseline→Candidate changes all 58 literal VALUE paths as 53 MODIFY, four CREATE and
  one DELETE, with `+1235/-1005 = 2240` touched text LOC.
- **Actual:** the approved TS table independently parses as 58 unique VALUE and seven ASSURANCE
  selectors. NUL-safe Git output over the literal VALUE selector is 1,793 bytes for name-status,
  SHA-256 `b0f9d3f781caa5717a017a2b92838fd78b8108bf88f1883ba4a89daa3b1a8f3a`, and 1,960 bytes for
  numstat, SHA-256 `20af28b988360518a848cc1268eb9385cf6e038f484d38a35f85eee3803201fe`.
  Every selector is present, there are no renames/binary rows, and the independent action/arithmetic
  totals are exactly 53M/4A/1D and `1235+1005=2240`. They remain below 116 paths and 5,148 LOC.
- **Match:** ✅ AC-11 accounting; the two byte-stream hashes equal the sealed R2 receipt.

### R2-V4 — changed AC-7 applicability and the sole native attempt

- **RF claim:** R1 evidence remains applicable to unchanged mechanics, but new Candidate pin,
  intended/actual receiver bytes, provenance and unchanged repeat are BLOCKED because the sole R2
  attempt stopped during preparation.
- **Actual:** writes 26, 55 and 57 are exactly the three changed VALUE sources; config write refs
  56/58 would also need the new `tfw.installed_from` Candidate. The accepted R1 result therefore
  cannot prove those new effects. The only authorized attempt started `2026-09-13T20:28:59Z`, with
  deadline `20:58:59Z`, 24-operation ceiling, zero deductions and no retry. Operation 3 raised an
  `AssertionError` at `20:29:53.549973Z`; the failure was observed on operation 4. It stopped before
  new upstream staging, preservation, target writes, native build, provenance publication or repeat.
  Raw stopped custody committed at `20:34:12.701849Z` (313.701849 s); direct return completed at
  `20:35:33.937Z` (394.937 s), operation 10/24.
- **Match:** ✅ the RF's honest BLOCKED report; ❌ the completion conditions in AC-7 fifth/sixth
  bullets and AC-7 Evidence are not established for Candidate `a99ba6cd...`.

### R2-V5 — stopped custody is complete but is not a successful effect

- **RF claim:** the partial repository was diagnosed and sealed without converting STOP into PASS.
- **Actual:** the raw commit changes exactly the seal's 20 paths. All 19 non-self declared sizes,
  SHA-256 hashes and physical/Git blobs match; the twentieth path is the self-identifying seal.
  Independent comparison of the 2,317-row partial physical map with the 7,035-row accepted positive
  map finds zero byte/size/SHA/raw-Git, CR or CRLF mismatch. Forty binary/archive rows differ only
  because the failed observer counted every LF byte while the prior record counted bare LF; in every
  row the difference equals CRLF count. The earlier CR explanation in `06-stop-diagnosis.json` is
  false and remains preserved; `08-stopped-result.json` records `explanation=false`, and the later
  clarification states the verified LF-only interpretation. Operation 7's Windows `os error 206`
  occurred before process creation; subsequent calls only sealed, verified and returned custody.
- **Match:** ✅ evidence identity and honest limitation; no native success inference is available.

### R2-V6 — affected AC-8 output and final report rendering

- **RF claim:** one Candidate-epoch production build and eight inspected pages show the corrected
  current prose and preserve the five reviewed compatibility fragments; later cumulative reports are
  usable at the final return epoch.
- **Actual:** the checkpoint build exits 0, and its observation records all eight pages, all five
  original fragment occurrences and no native/browser-click claim. A separate current-tree Reviewer
  build over the unchanged reviewed product/reports plus the Reviewer-owned map continuation exits 0
  in 137.83 s and produces 1,988 HTML files (2,058 total files).
  Its ONB, RF, EV and existing REVIEW pages contain the R2/final headings. Rendered Task Storage and
  `Where tasks live` carry the corrected current wording and not the three former active-gate clauses.
  Each of the five compatibility source occurrences has a matching href and exactly one target ID.
  The 56 local links in the R2 ONB/RF/EV and current REVIEW sections resolve to existing repository
  targets; the Coordinator-ruling fragment exists both in source and rendered HTML.
- **Match:** ✅ affected AC-8 and final report rendering. Existing corpus-wide historical warnings
  remain outside this task's fixed scope and are not relabelled as TKL link failures.

### R2-V7 — cumulative report and prefix custody

- **RF claim:** prior report epochs remain byte prefixes, while the cumulative return states ten
  VERIFIED and two BLOCKED criteria without synthetic PASS.
- **Actual:** current ONB, RF and EV reproduce their exact pre-R2-return prefixes at 67,893, 37,467
  and 25,012 bytes with SHA-256 `9bf30ada...`, `9d5a2d59...` and `66a3ea2f...`. The cumulative RF/EV
  state AC-7 and dependent AC-11 as BLOCKED, preserve the original failure and corrected counter
  explanation, and claim no new receiver effect. Exact report/control return precedes the sole R2
  review dispatch and changes no VALUE/ASSURANCE path.
- **Match:** ✅ report truthfulness, custody and inspectability; AC-11 completion remains dependent on
  the unresolved native effect.

### R2-V8 — Project Values and knowledge citations

- **RF/ONB claim:** the unchanged fifteen citation rows remain applicable to the R2 correction and
  its bounded return.
- **Actual:** P0–P4 were scanned in full again; relevant P5 Convention F23, P6 Process
  F30/F37/F38/F49, P7 Constraint F16 and Stakeholder F6 were read directly. All fifteen HL §7.2 and
  ONB §7 rows resolve, exist and retain the asserted semantics. `TKL-20260913-01` remains an
  architecture-selection record rather than implementation acceptance. D86 expressly preserves
  prior evidence only for unchanged claims and requires affected verification for changed/unknown
  inputs; D87 preserves active/history reachability without restoring the retired gate.
- **Match:** ✅. External design-context checks and unchanged R1 citation semantics are reused under
  D86; no new external performance, authority or provider claim is made.

## R2 Claim & Source Checks

| # | Claim | Primary evidence | Result |
|---|---|---|---|
| R2-C1 | Three active current-gate descriptions are retired and historical occurrences remain | exact four-file Candidate diff, current carriers and guard source | ✅ Exact |
| R2-C2 | Affected checks/build are Candidate-bound | checkpoint input/receipts, stream hashes and output observation | ✅ Exact |
| R2-C3 | Accounting is 58, 53M/4A/1D, `+1235/-1005` | approved selector plus independently generated NUL streams | ✅ Exact |
| R2-C4 | New Candidate receiver effects and unchanged repeat occurred | stopped native raw/return | ❌ They did not occur; RF correctly says BLOCKED |
| R2-C5 | Final reports preserve earlier epochs and render current R2 truthfully | independent prefix hashes, local-link scan and current-tree build | ✅ Exact |

## R2 Discrepancy Found

### R2-D1 — affected Candidate-native evidence is absent after the strict stop

The source correction closes R1's AC-5/9 defect, but AC-7's approved evidence contract is
Candidate-specific. The sole bound was consumed by an observer failure before any changed effect.
Consequently there is no actual `a99ba6cd...` receiver pin/provenance publication, no observed
intended/actual result for writes 26/55/57, no applicable native output and no zero-write completed
repeat. Preparation-byte equality cannot substitute for those effects. This breaches AC-7 fifth and
sixth bullets plus its Evidence clause, and therefore AC-11's requirement that every meaningful
behavior have applicable evidence and that the independent Reviewer validate actual effects.

No source, accounting, compatibility, report-custody or second current-policy discrepancy was found.

## R2 Evidence Verification

| # | Evidence group | Exists? | Matches its bounded claim? |
|---|---|---|---|
| R2-E1 | `r2-checkpoint/04-source-checks`, `05-docs-build`, `07-output-observation` | ✅ | ✅ commands, exit/counts, current prose and five compatibility destinations |
| R2-E2 | `r2-checkpoint/08-accounting`, source/native proposals and Coordinator admission | ✅ | ✅ exact selector/arithmetic and prospective identities; no acceptance inference |
| R2-E3 | `r2-native/` clocks, failure, partial map/archive, ledger and Git seal | ✅ | ✅ complete stopped custody; explicitly no target effect |
| R2-E4 | `r2-return/` native return, prefix/counter clarification and validation | ✅ | ✅ honest 10/12 result, prefix and no-later-product-change claims |
| R2-E5 | current R2 ONB/RF/EV plus Reviewer final-epoch build | ✅ | ✅ final report links/headings/rendering within stated corpus-warning limits |

Evidence exists for the failure and stop; it is insufficient evidence of the missing AC-7 success.

## R2 Checkpoint

- [x] Inspected every R2-changed VALUE/ASSURANCE path and preserved the prior `58/58` audit only for unchanged claims.
- [x] Reproduced exact immutable accounting, including NUL-stream byte hashes.
- [x] Distinguished partial preparation equality from actual Candidate effects and unchanged repeat.
- [x] Verified all stopped raw hashes, exact 20-path commit and corrected LF-counter interpretation.
- [x] Built and inspected the actual final-report epoch without rerunning tests or native cases for row completion.
- [x] Rechecked all fifteen knowledge-citation rows and current D86/D87 applicability.
- [x] Re-evaluated every AC: AC-5/9 and affected AC-8 now hold; AC-7 and dependent AC-11 remain BLOCKED.

R2 stage complete: **YES**
