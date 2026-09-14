# Verify — R3 stopped native observations and late custody

> **Session identity:** `REVIEW · TKL`
> **Reviewer:** robert, same independent Reviewer task `01a09aaf-9af3-7d13-8ef8-59d3bc84d5e7`
> **Review input:** `869efcd9feb9d59b1e91235206b35fdc3214d911`
> **Executor return:** `3971b80cb6422e358c613a52dde3a2d0cca257ab`
> **Candidate:** `a99ba6cd756a7db444f217aef4e5a0eb83faee51`
> **Min verify ratio:** `0.42`
> **Returned paths:** `N=134`; minimum `ceil(134 × 0.42)=57`; opened and byte-checked `134`

## Verification Log

### V1 — return ancestry and exact custody

- **Claim:** R3's cumulative return contains an explicitly late raw-custody commit and a separate
  documentary RF return, while the native attempt remains stopped.
- **Actual:** raw commit `fc7497279ef3f70e2fcae5bb342e605a4cc7673e` has exact parent
  `22c75aae5ce1a0a6aed5a7b867277a304dd3ee6e` and adds exactly 122 R3 raw paths. Merge
  `bc03aa784f360631491fdd169fd4a45284fbe378` has parents `fc749727...` and Coordinator authority
  commit `43a55292579e4ad9ec37866926a78a8bae036ef3`. Return `3971b80...` adds exactly twelve final
  TRACE paths. Input `869efcd...` adds only the Coordinator admission and c92b dispatch.
- **Match:** ✅. The late commit is custody only; it does not change the recorded native outcome.

### V2 — every returned byte and declared final hash

- **Claim:** all 122 raw plus twelve final-return paths survived exactly.
- **Actual:** all 134 paths were opened from the integration checkout. For each path, physical bytes,
  `git hash-object --no-filters` and the expected commit blob agree: 0 mismatches across
  418,643,390 bytes. The eleven non-self SHA-256 values in `r3-return/04-validation.json` all match;
  the self row correctly names its committed Git blob rather than claiming a recursive self-hash.
  Coordinator admission SHA-256 is
  `28ab986d1c06e0592c893d1004688fc177c95e81f970797981cf4c06888aaf9c`.
- **Match:** ✅ 134/134 paths and 11/11 declared non-self hashes.

### V3 — complete receiver archive and repeat identity

- **Claim:** the sealed physical archive is a complete identity-bearing receiver observation and the
  repeat maps are identical.
- **Actual:** independent streaming inspection opened every entry of
  `r3-native/18-final-physical.zip`: 7,281 files, 419,108,392 uncompressed bytes. Recomputed size,
  SHA-256 and raw Git blob match `18-final-map.json` for all 7,281 entries; mismatch count 0.
  `17-repeat-before.json`, `17-repeat-after.json`, `18-final-map.json` and `expected-current.json`
  are byte-identical (2,397,603 bytes; SHA-256
  `e66731505d32f00acaf77ba4bdda08131276921f34a1d271b30ad64183d81e94`). Initial and final Git
  metadata ZIPs are also byte-identical (SHA-256
  `141abef3db2449fc3a25e1636c10bc9e24ae153c89630d6c83291d79ece8978c`).
- **Match:** ✅ complete archive and repeat identities hold.

### V4 — pinned Candidate source and staging

- **Claim:** R3 staged the exact Candidate source, not a substituted or normalized tree.
- **Actual:** Candidate `a99ba6cd...` has 3,036 blob paths. UTF-8 decoding of
  `07-source-routing.json` and `18-inventory.json` gives exactly 3,036 source routes and 3,036
  `.tfw/.upstream/` staging rows; every raw Git blob equals the Candidate tree. Independent TAR
  inspection opened 3,036 regular files / 214,183,526 bytes from `07-candidate.tar`; every path,
  size, SHA-256 and raw Git blob equals the source-routing row. The archive also contains one
  non-file PAX header, correctly excluded from the file count. All 31 current pin rows match their
  named Git objects.
- **Match:** ✅ 3,036/3,036 tree, route, staging and TAR identities; 31/31 pins.

### V5 — established receiver preparation and preservation

- **Claim:** the receiver began from the accepted positive state, preserved old/intended values and
  unrelated project state, then changed only the affected group.
- **Actual:** `03-positive-map.json` contains 2,317 paths and `06-checkout-map.json` 2,312 baseline
  paths; all available physical identities agree semantically with their maps. The four target
  old/intended/final identities agree with the positive map, Candidate and final receiver map.
  `08-old-intended.zip` has exactly twenty files: old and intended copies for the four targets plus
  the README, state and nine topic sources required for preservation. The final effects are:
  `.tfw/conventions.md` blob `47d64213...`, `tools/tfw_state.py` `9705cef6...`, `KNOWLEDGE.md`
  `8046b555...`, and the customized 4,420-byte `.tfw/project_config.yaml` blob `3305bc86...`.
  The first three equal their Candidate intent; the fourth changes only the selected
  `installed_from` scalar while retaining the receiver's other YAML choices.
- **Match:** ✅ four intended affected effects, no unrelated positive-repository drift.

### V6 — phase chronology and strict terminal outcome

- **Claim:** receiver work completed thirteen named phases with exit 0 before two bookkeeping/custody
  failures; the whole attempt ended `STOPPED 24/24`.
- **Actual:** the thirteen immutable step records are `prepare`, `stage`, `preserve`, `effect26`,
  `effect55`, `effect57`, `check`, `build`, `output`, `provenance`, `receipt`, `repeat`, `seal`; each
  has exit 0 and ordered start/completion times. Invocation 21 then failed before archive validation,
  metadata write, staging or commit because it asserted 14 phase records against the actual 13.
  Invocation 23 staged the existing 122 paths but its targeted cached diff-check exited 2 before
  commit. Invocation 24 returned STOP within the original 22:13:37Z–22:43:37Z clock; there was no
  receiver access after the first failure and no retry. The raw commit completed later at
  22:51:11.876309Z under d3c8/f00f authority.
- **Match:** ✅ chronology and observations; ❌ no bounded-success claim. The correct attempt outcome
  remains `STOPPED 24/24`.

### V7 — source checks, one build and actual opened output

- **Claim:** the affected current descriptions were checked, built once and observed in generated
  output without replaying unchanged source suites.
- **Actual:** `12-source-check.json` contains the exact current Task Storage and Where tasks live
  text, reports the non-docstring AST unchanged and lists the selected adapter paths as preserved;
  it explicitly records `source_test_executed: false`. The build step exited 0, produced 1,924
  files and ended with `Documentation built in 162.59 seconds`; its existing unresolved-reference
  warnings remain in the raw streams. `14-opened-pages.zip` contains exactly
  `knowledge-index/index.html` and `reference/conventions/index.html`; both byte identities match
  the final archive. Parsed page text contains the new Full `workspace` default, optional
  `historical_containers`, read-only history and no-move/no-relabel semantics claimed by the RF.
- **Match:** ✅ for the two affected current output pages only. This build does not render the later
  provenance scalar, receipt or cumulative RF/EV/ONB append.

### V8 — immutable receipt and completed repeat

- **Claim:** one immutable receipt records the observed application at its seal epoch; a subsequent
  repeat completed unchanged.
- **Actual:** the receipt at `.tfw/update_receipts/UPDATE__20260913-223205__fb31.md` is 4,969 bytes,
  SHA-256 `e5bb94d9120f8299b9015b755c076fa3268d468b709c66cfc2a45a761d1700db`, raw blob
  `b7a707e8...`, and is present identically in the final archive. It covers all five canonical
  template sections, pinned source/receiver, authority, applied/preserved/skipped/refused effects,
  verification, cleanup and next action. Its `planned/not-yet-observed` delivery and not-yet-observed
  repeat wording is accurate at its 22:32:05 seal and was not rewritten. The later repeat ran
  22:32:19–22:32:45, covered all 7,281 files, reported zero physical writes, no new receipt/build and
  one completed unchanged repeat.
- **Match:** ✅, with the two epochs kept distinct.

### V9 — cumulative reports and pre-verdict RF state

- **Claim:** R3 was appended to the cumulative ONB/RF/EV without rewriting prior epochs; the current
  carrier is a real ONB→RF return, not acceptance.
- **Actual:** old byte prefixes of ONB (79,703 bytes), RF (47,230) and EV (33,111) match their stored
  SHA-256 values. The three suffixes contain 45 new local Markdown links (5/4/36); all 45 resolve.
  Transition event `79ad` has eleven refs and all eleven resolve. Current `status.md` SHA-256 is the
  declared `f4773325...` and the review-input state is `RF`. EV truthfully leaves R3-E7/AC-7 and R3-E11/AC-11 BLOCKED
  for this independent decision and preserves R3's stopped outcome. The final complete inventory has
  1,018 paths: 58 VALUE, 9 ASSURANCE and 951 TRACE.
- **Match:** ✅. The final report claims no render of its own post-build append.

### V10 — immutable VALUE accounting and affected reuse

- **Claim:** Candidate, approved TS and original product/test surface are unchanged, so accepted
  earlier claims remain usable under D86 while exact accounting still reproduces.
- **Actual:** approval `2794cbdb...` resolves to TS blob `f69fd409...`; Baseline is `ec91c560...` and
  Candidate remains `a99ba6cd...`. The 58 VALUE plus seven original ASSURANCE paths show no changes
  from Candidate to review input. Re-running the two exact NUL-safe Git commands stored in
  `r2-checkpoint/08-accounting/accounting.json` reproduced byte-identical stdout hashes
  `b0f9d3f7...` and `20af28b9...`, exit 0 and empty stderr. Result remains 58 logical VALUE files,
  53 MODIFY / 4 ADD / 1 DELETE, `+1,235/-1,005 = 2,240` touched text LOC against the owner-approved
  planned `+1,375/-1,199 = 2,574`; no threshold or membership deviation.
- **Match:** ✅. Two new R3 ASSURANCE scripts and later TRACE do not move Candidate.

## Commands Executed

| # | Read-only command / audit | Result |
|---|---|---|
| 1 | Git graph, parents and exact path diffs for `22c75..fc749`, `bc03..3971`, `3971..869` | exact 122 / 12 / 2 path layers |
| 2 | Open/hash/blob-check all 134 returned paths | 134/134, 0 mismatches |
| 3 | Stream `18-final-physical.zip` and recompute size/SHA-256/raw blob against final map | 7,281/7,281, 0 mismatches |
| 4 | Compare repeat/final maps and initial/final Git metadata archives | byte-identical pairs hold |
| 5 | Compare Candidate tree, UTF-8 source routing/staging and stream Candidate TAR | 3,036/3,036, 0 mismatches |
| 6 | Check 31 pins, 2,317 positive paths, four old/intended/final targets and 20 preservation members | all named identities hold |
| 7 | Parse thirteen step records, operator ledger, failure, stop and late-tail records | 13 exit 0; attempt STOPPED 24/24; no post-stop receiver access |
| 8 | Open and parse two captured HTML pages | exact final-archive bytes and claimed current semantics present |
| 9 | Open receipt from final archive and compare identity/template coverage | exact earlier-seal receipt; pending wording preserved |
| 10 | Recompute 45 suffix links, eleven transition refs and eleven final hashes | 45/45, 11/11, 11/11 |
| 11 | Re-run exact stored name-status and numstat commands | stdout hashes exact; 58 VALUE and 2,240 touched LOC |
| 12 | Compare original 65 VALUE/ASSURANCE paths Candidate→input | zero changed paths |

No receiver was accessed. No build, source suite, init, AC-9/AC-10 consumer, native run, repeat,
cleanup or original failed validator was re-executed.

Several Reviewer helper attempts failed read-only before making comparisons: two archive scripts used
.NET APIs unavailable in this PowerShell runtime before a compatible streaming audit succeeded; one
source script decoded UTF-8 JSON as ANSI and one TAR listing displayed Unicode as octal escapes before
the UTF-8 and byte-level TAR audits above resolved all six apparent path mismatches; one final-hash
script prefixed already repository-relative paths before the corrected 11/11 check. These are Reviewer
tooling corrections, not changes to or discrepancies in the returned evidence.

## Claim & Source Checks

| # | Claim / citation | Traces to | Holds? |
|---|---|---|---|
| C1 | late custody is authorized but cannot cure native STOP | d3c8, f00f, `00-terminal-tail.json`, `01-late-custody.json` | ✅ |
| C2 | four actual effects preserve the established receiver | positive/final maps, preservation ZIP, steps 08–15 | ✅ |
| C3 | one complete unchanged repeat occurred after receipt sealing | steps/results 16–18 and four identical maps | ✅ |
| C4 | only two affected current pages were opened | `13-build.step.json`, `14-output.json`, opened-pages ZIP | ✅ |
| C5 | unchanged claims may reuse accepted evidence | KNOWLEDGE D86 and zero-change Candidate→input check | ✅ |
| C6 | original failures and output limits remain visible | cumulative RF/EV, `21-original-failure.json`, terminal tail | ✅ |
| C7 | cumulative final carrier is reviewable | exact prefixes, 45 links, 11 refs/hashes, complete inventory | ✅ |

## Discrepancy and resolution

The evidence has two outcome levels that must not be collapsed. The receiver-side affected application
reached four exact effects, one build, one immutable receipt and one complete zero-write repeat before
the bookkeeping failures. The encompassing native attempt nevertheless failed its later custody path
and is permanently `STOPPED 24/24`; the explicitly authorized late raw commit supplies durable exact
custody, not an in-bound-success observation. The missing original invocation-23 stdout remains
unknown. Later byte inspection shows no trailing-space normalization target, but it is not substituted
for the missing original diagnostic.

The receipt's pending wording and the R3 build's earlier epoch are likewise not errors: each is true at
its own seal. They constrain which facts those artifacts prove. No source byte, raw record or historical
claim was rewritten to make the sequence appear cleaner.

## Evidence Verification

| Evidence group | Status | Independent result and limit |
|---|---|---|
| R3 source/pin/preparation | VERIFIED | exact Candidate, 3,036 source files, 31 pins and accepted positive receiver identities |
| Preservation and four affected effects | VERIFIED | old/intended/final identities and unrelated receiver preservation hold |
| Native build and output | VERIFIED | one build and two affected current pages only; known warnings retained |
| Receipt | VERIFIED | exact immutable receipt at its earlier seal; no future delivery/repeat claim |
| Repeat | VERIFIED | one complete 7,281-file unchanged repeat, zero receiver writes |
| Native attempt outcome | BLOCKED as success / VERIFIED as STOPPED | two failures, 24-call return, no in-bound raw commit |
| Late custody | VERIFIED as documentary custody | exact 122-path later commit under explicit authority; no retroactive cure |
| Cumulative report/control | VERIFIED | 12 final paths, prefixes, links, refs, hashes, state and inventory hold |

The evidence is sufficient to judge the actual affected effects and their limits. It is not evidence
of an overall successful native attempt, universal update reliability, owner comprehension, deployment,
release, publication or G8 reliability.

## Knowledge Citations Verified

P0–P4 were read in full for this review; relevant P5–P7 rows were read directly. The substantive
HL §7.2 and ONB §7 citation sections are unchanged from the prior independent review epoch: ONB §7
hash remains `5b6380c4...`; all other P0–P7 source files are byte-identical between `2cc0143` and
input `869efcd`. The two citation sections contain 51 links (37 local, 14 external); all local targets
exist. The prior independent external-source verification is reused only because the citations and
their claims are unchanged under D86.

| # | Priority / exact citation | Resolves and exists? | Meaning and relevance |
|---|---|---|---|
| 1 | P0 NS1 | ✅ | inspectable purpose and grounds survive the stopped/custody distinction |
| 2 | P0 NS2 2/4/7 and NS3 | ✅ | selected trace, simple operation, proportionate assurance and no bureaucracy |
| 3 | P1 Structural Enforcement, Portability; success 1/3 | ✅ | ordinary files and durable qualified continuation, without receiver runtime |
| 4 | P2 F21/F32/F42/F43/F45 | ✅ | explicit outcome, preserved meaning, materiality and bounded cost |
| 5 | P3 D37/D68/D82 | ✅ | legacy meanings and no-runtime/no-index boundary remain intact |
| 6 | P3 D85/D86/D87 | ✅ | source pin, immutable receipt, finite close/recovery and active/history preservation apply directly |
| 7 | P4 HL Contract, Design Rules, Anti-patterns | ✅ | frozen contract, progressive disclosure, real evidence and independent review |
| 8 | P5 Convention F23 | ✅ | canonical English semantics and retained localized files are preserved |
| 9 | P6 Process F30/F37/F38/F49 | ✅ | enforcement site, reference revision and pre-act bound remain explicit |
| 10 | P7 Constraint F16 / Stakeholder F6 | ✅ | no receiver runtime; bounded autonomy without silent drift |
| 11 | accepted SLC/PTTC/R1/R2 sources | ✅ local | exact accepted unchanged claims only; no new trial claim |
| 12 | `TKL-20260913-01` | ✅ | scoped architecture successor; implementation/review/release remain separate acts |

Incoming relation search found no later successor/correction/equivalence/conflict targeting exact
record `TKL-20260913-01`. Its scoped relation to D37/D82 and continuing D86/D87 remains applicable.

## Checkpoint

- [x] Opened 134/134 returned paths, exceeding the 57-path minimum.
- [x] Independently audited all 7,281 final receiver archive entries and all 3,036 Candidate TAR files.
- [x] Verified four affected effects, preservation, build/output, receipt and one unchanged repeat.
- [x] Preserved `STOPPED 24/24`, both failures, late-custody timing and missing original stdout as limits.
- [x] Reproduced exact VALUE accounting and confirmed all 65 original product/test paths unchanged.
- [x] Verified cumulative report prefixes, 45 links, eleven refs/hashes and pre-verdict RF state.
- [x] Verified P0–P7 relevance and unchanged citation applicability without claiming a new external trial.

Stage complete: **YES**

## Bounded final-effect follow-up — 2026-09-14

This appendix verifies only the changed closing/capture claims at input
`eed634f7d3f446bba440cc163ab6aab3f69886f3`, cumulative return
`18903c32e863a0fe5e8ab2376cc69666dc829611` and replacement Candidate
`daa520874c1f1236c95bc2dfbd268be911098d49`. It does not reopen the completed rev4 stages.

| Check | Independent result |
|---|---|
| Candidate composition and product effect | The Candidate has the recorded two merge parents. Relative to approved Candidate `a99ba6cd...`, only `KNOWLEDGE.md` changes in product scope, exactly +2/-0; the corrected Candidate changes the stopped row locator by +1/-1. |
| Source custody | `01-source-bytes.zip` contains exactly 17/17 declared members. Every archived physical size/SHA-256 and every Candidate Git blob/size/content SHA-256 holds. Only `knowledge/records/TKL-20260913-01.md` has the declared inherited CRLF physical/LF Git distinction. |
| Returned custody and reports | Candidate→return contains exactly the listed 20 TRACE paths; all 20 physical bytes equal raw Git, 19/19 non-self size/SHA-256 claims hold, and 13/13 new RF/EV references resolve at the return. Old RF/EV prefixes are exact. |
| Accounting | Re-executing the exact three stored read-only commands yields byte-identical raw stdout/stderr. Parsed result is 58 VALUE = 53M/4A/1D and +1,237/-1,005 = 2,242; the full Baseline→return inventory is 1,070/1,070 paths = 58 VALUE / 9 ASSURANCE / 1,003 TRACE. |
| Build and test applicability | The corrected one-build start/result pair agrees, exits 0 and binds both exact raw streams. Prior pytest custody contains `107 passed`; `gen_docs.py`, `test_gen_docs.py` and `test_integration.py` are byte-identical between that epoch and the replacement Candidate, so D86 reuse holds without claiming a new run. |
| Actual compiled output | The six-member witness ZIP matches 6/6 declared hashes. Independent HTML parsing finds the two rows, exactly seven href occurrences to five archived destinations, the exact literal `.tfw/migrations/knowledge-lifecycle.md` code and no false guide href. |
| Dispositions and controls | HL S1–S11 each has the source-bound reuse/retain/resolution described in formal rev4 §6; Researcher, Executor and Reviewer handovers are present. Status remains byte-identical at KNW; no release path or `4.0.0.md` effect exists. |

The prior capture remains a real stopped epoch: its eight links included the missing guide destination,
and its `07-stopped-return.json` still says STOPPED. The corrected evidence does not rewrite that event.
The native attempt likewise remains permanently `STOPPED 24/24`, with late custody and missing original
invocation-23 stdout unchanged.

Result: **sufficient for bounded final-effect acceptance**. No defect requiring a REVISE route was
found. Landing, DONE controls and any later untagged release candidate remain outside this appendix.
