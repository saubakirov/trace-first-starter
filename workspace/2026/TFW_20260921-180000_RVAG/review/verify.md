# Verify — "Do the material claims hold?"
> **Mindset:** Auditor. RF is a declaration, not a fact. Open files, run necessary checks, compare
> accepted claims with reality, and state the limits.
> **Test:** "Would the evidence establish this claim for this subject, revision and environment without RF?"
> Map: [map.md](map.md)

## Selection Argument

| Claim IDs | Risk / criticality | Affected behavior / dependencies | Environment | Oracle / authority | Evidence gap / limit | Selected verification and why |
|---|---|---|---|---|---|---|
| C1–C3, C12 | Highest: false approval, false return, or purpose loss | Review order, material finding grammar, mixed-round routes, purpose and safety floors | Code and non-code TFW consumers | Frozen HL, approved TS, North Star, accepted scenario facts | Analytic replay cannot reproduce each historical production environment | Read the actual Candidate clauses and replay MFX, TLD, CRATM, FRATS, wrong-purpose and mixed cases because these distinguish the new product semantics from ceremony. |
| C4–C5, C8 | High: arbitrary under-verification or count-based assurance | Verification selection, guard admission, existing protected tests | Local Windows, Python 3.13, pytest | TS AC-3/AC-4/AC-7; named behavior and fault fixtures | Existing tests do not prove the review methodology | Search active rules, inspect test sources, collect and rerun the suite, then keep test evidence bounded to the behavior it protects. |
| C6 | High authority risk | Durable-before-send protocol, exact recipient/ref, retry and ambiguity behavior | Codex addressed task transport | TS AC-5; current `coordinator_route`; accepted provider evidence | No external send during verification | Replay all specified delivery attacks against the actual clauses; reserve the one real send for after durable REVIEW and state. |
| C7, C9, C11 | Highest identity/scope risk | Full-copy parity, excluded surfaces, exact VALUE membership and local mirror identity | Git object database | Approved selector and immutable refs | Identity is scoped to the twelve literal VALUE paths | Compare blob identities, exact path sets and NUL-safe numstat; any mirror mismatch or extra VALUE path is material. |
| C10 | Highest authority risk | Contract/TS/Candidate/RF lineage, independent unit and return route | Git plus current Codex task metadata | Status/journal, direct delegated activation and immutable refs | Current activation is task metadata, not a Reviewer-authored trace | Verify ancestry, control files, distinct producer/reviewer units and exact route before judging. |

Safety/security, human acceptance authority and accepted-result identity were treated as mandatory
floors. No discrepancy count was used to select or expand verification.

## Verification Log

### V1: C1–C3 and C12 — value semantics and scenario discrimination
- **Accepted claim / authority:** The Candidate must judge `VALUE → ASSURANCE → TRACE`, preserve one
  aggregate verdict and per-item consequences, and never approve beside-the-point, unsafe or
  unauthorized work merely because the record is polished.
- **Subject tuple:** twelve VALUE paths at Candidate `9e86910e498ab7f74e8d3ede4dfb5e7064d84cfb`;
  code/non-code consumers; frozen HL and TS oracle; accepted RES case facts.
- **Action or evidence:** Read the canonical Review workflow, Map and Verify carriers, conventions and
  glossary; inspected the semantic Baseline→Candidate diff; replayed MFX, TLD, CRATM, FRATS,
  wrong-purpose F31, mixed, missing-safety-oracle, unauthorized-effect and sole/redundant-evidence
  cases against the actual clauses.
- **Observed:** Correct, independently established MFX product does not return to execution for
  immaterial record discrepancies; TLD wrong consumer behavior is VALUE/REVISE; CRATM authority
  contradiction stops at the ruler; FRATS missing reproducible proof is ASSURANCE/REVISE without
  automatic VALUE movement; wrong-purpose non-code work remains rejectable; mixed items retain
  distinct owners, routes and Candidate effects.
- **Limit:** Replay is analytic and uses accepted, bounded predecessor facts; it does not rewrite prior
  verdicts or claim a production reenactment.
- **Result:** HOLDS

### V2: C4 — claim/risk-selected verification
- **Accepted claim / authority:** Verification selection uses claim, risk, dependencies, environment,
  oracle/authority, evidence gap and limits while retaining mandatory floors.
- **Subject tuple:** Candidate Review/Verify/config surfaces; current repository; TS AC-3.
- **Action or evidence:** Searched both active configs and all Review carriers for
  `min_verify_ratio`, percentage escalation and blanket discrepancy rules; inspected Config migration
  wording and selection fields.
- **Observed:** The active key is absent from both configs; Config mentions it only as retired inert
  state. The canonical workflow and Verify template require the complete selection basis and floors;
  no active any-discrepancy-to-full-audit rule remains.
- **Limit:** Natural-language equivalence was checked semantically in addition to exact search.
- **Result:** HOLDS

### V3: C5 and C8 — guards and protected regression checks
- **Accepted claim / authority:** Permanent guards need a named invariant, failure consequence and
  relevant demonstrated counterfactual; existing protected checks remain meaningful and green; RVAG
  adds no permanent test.
- **Subject tuple:** Candidate-equivalent local mirror; Python 3.13; test sources under `tools/tests/`
  and `docs/scripts/`; TS AC-4/AC-7.
- **Action or evidence:** Inspected the test sources, collected the suite, and ran it independently.
- **Observed:** Fourteen exact tests collected and fourteen passed in 4.07 s. The Git blob-size test
  uses an exact-limit success plus limit+1 fault; documentation unit cases exercise malformed and
  boundary inputs; integration checks build the public docs and detect page/frontmatter leakage. No
  test path appears in the Candidate commit.
- **Limit:** These guards protect their named repository behaviors, not the Review methodology as a
  whole; semantic replay supplies the latter evidence.
- **Result:** HOLDS

### V4: C6 — terminal protocol
- **Accepted claim / authority:** One compact signal follows durable REVIEW/state, uses the exact route
  and immutable matching ref, and never turns uncertain delivery into blind retry or an exactly-once
  claim.
- **Subject tuple:** Candidate workflow/conventions; task route
  `codex:thread:local:01a0c400-3e48-7422-bb86-3b34fe177aa5`; Codex addressed-send mechanism; TS AC-5.
- **Action or evidence:** Replayed success, wrong route, stale/unresolved ref, verdict/ref mismatch,
  duplicate tuple, provider-confirmed non-application, ambiguous delivery and genuine later verdict.
- **Observed:** Actual clauses refuse wrong route/ref, make duplicate tuples semantic no-ops, permit at
  most one identical retry only after confirmed non-application, and stop rather than claim success or
  retry under ambiguity. Detail remains in REVIEW; the envelope carries identity only.
- **Limit:** No external message was sent during replay; the authorized terminal send remains a
  post-Decision effect.
- **Result:** HOLDS

### V5: C7 and C11 — propagation and accepted-result identity
- **Accepted claim / authority:** Canonical/full-copy pairs and the local twelve-path mirror must match
  the immutable Candidate; excluded AGSK, adapter, Handoff, release and test surfaces must remain
  untouched.
- **Subject tuple:** Candidate `9e86910e498ab7f74e8d3ede4dfb5e7064d84cfb`, mirror
  `2c990430b73ffb7a1e0a43e67c083e01929d289e`, Baseline
  `504e4a34d182f4181f65134a5a3f42b4f2553be9`; Git blob oracle.
- **Action or evidence:** Compared Git blob OIDs for every literal VALUE path; compared both declared
  full-copy pairs; diffed all excluded surfaces.
- **Observed:** All twelve Candidate/mirror blob OIDs are identical; canonical Review equals Claude
  Review and canonical Config equals Claude Config byte-for-byte. Excluded-surface diff is empty.
- **Limit:** Mirror identity is asserted only for the twelve authorized VALUE paths, not rebased trace
  commits.
- **Result:** HOLDS

### V6: C9 — immutable accounting and release boundary
- **Accepted claim / authority:** Candidate changes all and only twelve literal VALUE paths within
  2,000 touched text LOC and performs no release or external effect.
- **Subject tuple:** approved TS `6705d7c524bdb025c9887e19f3e1e30023b44928`; Baseline
  `504e4a34d182f4181f65134a5a3f42b4f2553be9`; Candidate `9e86910e498ab7f74e8d3ede4dfb5e7064d84cfb`.
- **Action or evidence:** Replayed the approved NUL-safe membership and numstat commands with full SHAs;
  inspected Candidate commit paths, versions and release-owned exclusions; ran `git diff --check`.
- **Observed:** Exactly 12 modifications, +538/−365 = 903 touched text LOC, zero binary rows and no
  extra path. Both config versions remain 3.5.0; release/history/migration surfaces are unchanged;
  whitespace check is clean.
- **Limit:** Scope arithmetic proves authority compliance, not product quality.
- **Result:** HOLDS

### V7: C10 — lineage and Reviewer independence
- **Accepted claim / authority:** Review is activated by the authorized Coordinator, applies to the
  fixed Candidate/RF lineage, is performed by a distinct unit and returns only to the recorded route.
- **Subject tuple:** Contract `db61ecac1a7f0743036f84a5d5075ca727b5364c`; TS `6705d7c…`;
  Candidate `9e86910…`; RF/EV `4ae3173…`; RF transition `cea0bcd…`; current Reviewer unit
  `codex:thread:local:01a0c822-51be-72b3-875f-4274d539c924`.
- **Action or evidence:** Verified ancestry for the immutable production line; read status and journal;
  compared Executor and Reviewer task identities; confirmed exact delegated source and route; set and
  read back the title `REVIEW · RVAG`.
- **Observed:** The production refs form the declared ancestry, lifecycle was RF at entry, Executor and
  Reviewer are distinct, and both activation and `coordinator_route` identify the same exact Parent
  Coordinator.
- **Limit:** The local mirror is a rebased integration line, so identity is established by scoped blob
  equality rather than false ancestry.
- **Result:** HOLDS

### V8: C1–C12 — RF/EV applicability
- **Accepted claim / authority:** RF and EV evidence must independently resolve to the accepted subject,
  Candidate, environment and oracle.
- **Subject tuple:** immutable Candidate plus byte-identical local mirror; actual repository; approved
  TS/HL and primary sources.
- **Action or evidence:** Reproduced path, byte, semantic, test and accounting evidence; inspected every
  cited artifact and corroborative external source.
- **Observed:** Reproduced observations agree with RF/EV. The only bounded differences are a faster/slower
  local test duration and rebased trace SHAs, neither of which changes the accepted product subject.
- **Limit:** External standards corroborate narrow design principles only; no external certification or
  provider guarantee is claimed.
- **Result:** HOLDS

## Commands Executed

| # | Command | Claim IDs | Result |
|---|---|---|---|
| 1 | `python -m pytest tools/tests/ docs/scripts/ -q --collect-only` | C5, C8 | exit 0; 14 exact tests collected in 0.09 s |
| 2 | `python -m pytest tools/tests/ docs/scripts/ -q` | C5, C8 | exit 0; 14 passed in 4.07 s |
| 3 | `git diff --name-status --find-renames=50% -z 504e4a34d182f4181f65134a5a3f42b4f2553be9 9e86910e498ab7f74e8d3ede4dfb5e7064d84cfb -- <12 literal paths>` | C9 | twelve `M` records, exact authorized membership |
| 4 | `git diff --numstat --find-renames=50% -z 504e4a34d182f4181f65134a5a3f42b4f2553be9 9e86910e498ab7f74e8d3ede4dfb5e7064d84cfb -- <12 literal paths>` | C9 | +538/−365, 903 touched, zero binary |
| 5 | `git show --format= --name-status 9e86910e498ab7f74e8d3ede4dfb5e7064d84cfb` | C5, C9 | exactly the twelve VALUE paths; no test path |
| 6 | `git diff --check 504e4a34d182f4181f65134a5a3f42b4f2553be9 9e86910e498ab7f74e8d3ede4dfb5e7064d84cfb` | C7, C9 | exit 0 |
| 7 | Git blob-OID comparison for each literal path at `9e86910…` and `2c99043…` | C7, C11 | `ALL_12_IDENTICAL=True` |
| 8 | Git blob-OID comparison of Review and Config canonical/Claude pairs | C7 | both pairs identical |
| 9 | Baseline→Candidate diff over `.agents`, adapters, Handoff, VERSION, CHANGELOG, migrations and test directories | C7, C9 | empty |
| 10 | Exact search for `min_verify_ratio`, percentage escalation, versions and terminal protocol terms | C4, C6, C9 | retired key only in Config migration prose; no active blanket escalation; versions remain 3.5.0 |
| 11 | `git rev-list --ancestry-path` / `git merge-base --is-ancestor` over Contract, TS, Candidate, RF/EV and transition refs | C10 | declared production lineage verified |

## Claim and Source Checks

| # | Claim / citation | Where | Primary artifact / source | Holds? |
|---|---|---|---|---|
| C1 | Ordered value-first judgment and mandatory subjects | RF §§1–3; EV E1 | Candidate Review/Map/Verify/conventions plus frozen HL | ✅ |
| C2 | Complete item contract and material-consequence predicate | RF §§1–3; EV E1/E2 | Candidate workflow/conventions/glossary; TS AC-1/AC-2 | ✅ |
| C3 | Per-item mixed routes and Candidate effects | EV scenario replay | Candidate clauses plus accepted RES iter2 cases | ✅ |
| C4 | Claim/risk selection replaces ratio and blanket escalation | EV E3 | Candidate configs, Config and Review/Verify text | ✅ |
| C5 | Detection-power admission and honest labels | EV E4 | Candidate Review/Verify plus inspected test sources | ✅ |
| C6 | Compact durable addressed terminal protocol | EV E5 | Candidate Review/conventions; status route; accepted provider facts | ✅ |
| C7 | Propagation parity and excluded-surface preservation | EV E6 | Git blob and diff results | ✅ |
| C8 | Protected checks remain meaningful and green | EV E7 | Actual tests, fixtures and independent pytest output | ✅ |
| C9 | Exact Candidate and accounting | EV E-accounting | Approved TS selector and independent NUL-safe Git replay | ✅ |
| C10 | Authorized independent routing spine | RF header/§5; status/journal | Immutable lineage and current task metadata | ✅ |
| C11 | Local mirror identity | Coordinator dispatch | Per-path Candidate/mirror Git blobs | ✅ |
| C12 | Frozen purpose and North Star remain controlling | HL §§1,3,5–7; Map C12 | Frozen HL, `.tfw/README.md` NS1–NS3 and Candidate semantics | ✅ |

## Guard and Check Admission

| # | Kind | Protected behavior / invariant | Failure consequence | Counterfactual detection | Admission |
|---|---|---|---|---|---|
| G1 | permanent guard | Git blob-size boundary accepts exactly 5 MiB and rejects larger blobs | Oversized repository blobs could pass policy or valid boundary blobs could fail | Explicit exact-limit fixture plus limit+1 fault | admitted |
| G2 | permanent guards | Documentation extraction/rendering preserves valid pages and rejects malformed/frontmatter leakage cases | Published docs can omit content or expose internal metadata | Concrete malformed, missing and boundary inputs in eleven unit tests | admitted |
| G3 | permanent guards | Public-core documentation builds and exposes expected pages without frontmatter-body leakage | Deployment can succeed structurally while shipped navigation/content is wrong | Two integration cases build the site and assert positive pages plus negative leakage | admitted |
| G4 | positive/governance controls | Test count, commit existence, path count and LOC arithmetic | Misreporting scope or reproducibility | N/A for product behavior; exact commands only establish inventory and authority | governance only |
| G5 | temporary diagnostic | Scenario replay over historical cases | A methodology clause can misclassify a bounded known case | Contrasting VALUE, ASSURANCE, TRACE and wrong-purpose cases | temporary analytic evidence; no new permanent test |

## Candidate Findings

No findings.

## Evidence Verification

Evidence applies to Candidate `9e86910e498ab7f74e8d3ede4dfb5e7064d84cfb`, the byte-identical
twelve-path mirror `2c990430b73ffb7a1e0a43e67c083e01929d289e`, the local Windows/Python
environment, the frozen HL/approved TS oracle and the accepted predecessor facts.

| # | RF evidence ref | Subject tuple | Artifact exists? | Establishes the claim? | Limit |
|---|---|---|---|---|---|
| E1 | EV E1 and Scenario replay | Candidate semantics; accepted case facts; HL/TS oracle | ✅ | ✅ | Analytic replay, not production reenactment |
| E2 | EV E2 and Scenario replay | Candidate per-item routes; mixed cases | ✅ | ✅ | Accepted bounded case facts |
| E3 | EV E3 and static checks | Candidate configs/workflows | ✅ | ✅ | Semantic synonyms also inspected manually |
| E4 | EV E4 and guard replay | Candidate guard rules and path audit | ✅ | ✅ | Methodology itself is not claimed to be pytest-proven |
| E5 | EV E5 and terminal replay | Candidate protocol; recorded route; provider bounds | ✅ | ✅ | No external send during verification |
| E6 | EV E6 and propagation checks | Candidate pairs and excluded Baseline diff | ✅ | ✅ | Full byte parity required only for declared copies |
| E7 | EV E7 and protected checks | Candidate-equivalent mirror; actual test sources/runtime | ✅ | ✅ | Green tests remain bounded regression evidence |
| E-accounting | EV accounting proof | approved Baseline/Candidate selector and Git oracle | ✅ | ✅ | Governance/scope proof, not quality by volume |

## Knowledge Citations Verified

PV priorities 0–4 were read in full; priorities 5–7 were selected by direct relevance. Each row
below verifies both the frozen HL citation and the corresponding ONB application. External standards
are primary-source corroboration only and do not become acceptance authorities.

| # | Artifact | Priority + exact citation | Resolves? | Item exists? | Meaning matches? | Relevant? |
|---|---|---|---|---|---|---|
| 1 | HL §7.2 #1; ONB §7 #1 | P0 `.tfw/README.md` NS1 Purpose | ✅ | ✅ | ✅ — value is purpose/authority/inspectability/continuation, not process volume | ✅ — governs MFX false-return risk |
| 2 | HL #2; ONB #2 | P1 `.tfw/README.md` NS2.1, NS2.7 | ✅ | ✅ | ✅ — purpose first; assurance proportional to risk; subtract useless ceremony | ✅ — governs selection and subtraction |
| 3 | HL #3; ONB #3 | P0/P1 `.tfw/README.md` NS3 | ✅ | ✅ | ✅ — TFW must not become an artifact-count factory | ✅ — excludes new score/carrier objectives |
| 4 | HL #4; ONB #4 | P1 `.tfw/README.md` Methodology values; Success Criteria 4 | ✅ | ✅ | ✅ — candor/structural enforcement and a usable acceptance-ready result | ✅ — requires observable clauses, not exhortation |
| 5 | HL #5; ONB #5 | P2 `knowledge/philosophy.md` F20/F36/F42/F43/F45 | ✅ | ✅ | ✅ — staged judgment, purpose/quality distinction, material gates, architecture and subtraction | ✅ — directly shapes the correction |
| 6 | HL #6; ONB #6 | P3 `KNOWLEDGE.md` D13/D52/D61/D64/D72/D76/D86 | ✅ | ✅ | ✅ — independent review, evidence, purpose, finite decisions, accounting and record-only recovery | ✅ — retained boundaries and superseded proxy semantics are distinguished |
| 7 | HL #7; ONB #7 | P4 `.tfw/conventions.md` HL Contract/Coordination/Design Rules/Anti-patterns | ✅ | ✅ | ✅ — frozen purpose, exact routing, observable structure and role independence | ✅ — authority and purpose floors |
| 8 | HL #8; ONB #8 | P5 `knowledge/convention.md` F3/F22 | ✅ | ✅ | ✅ — actual files outrank specification prose; process artifacts do not spend VALUE budget | ✅ — actual-file and accounting checks |
| 9 | HL #9; ONB #9 | P6 `knowledge/process.md` F23/F29/F31/F32 | ✅ | ✅ | ✅ — evidence complements tests; acceptance differs from completeness; correct reference points matter; evidence-only failure exists | ✅ — core value/assurance distinction |
| 10 | HL #10; ONB #10 | P6 `knowledge/process.md` F37/F38/F40/F42 | ✅ | ✅ | ✅ — reproducible metrics, pre-act bounds, controllable ACs and candid weaknesses | ✅ — accounting and verification honesty |
| 11 | HL #11; ONB #11 | P6 `knowledge/process.md` F35 | ✅ | ✅ | ✅ — producer-local tests can be blind to a receiver | ✅ — environment/oracle binding |
| 12 | HL #12; ONB #12 | P7 ISO/IEC/IEEE 29119-1:2022; NISTIR 7608; NIST SP 800-171A Rev. 3 | ✅ | ✅ | ✅ — risk-based testing, structured claim/evidence reasoning and context-tailored sufficiency without a fixed artifact count | ✅ — narrow corroboration of selection |
| 13 | HL #13; ONB #13 | P7 NASA-STD-8739.8B; SLSA Build Provenance 1.2 | ✅ | ✅ | ✅ — intended/unintended assurance and provenance bound to identified artifacts/revisions | ✅ — safety and result-identity floors |
| 14 | HL #14; ONB #14 | P7 Papadakis et al., ICSE 2018 | ✅ | ✅ | ✅ — mutation score is not an independent universal real-fault proxy when suite size is controlled | ✅ — supports local counterfactual, rejects global score |
| 15 | HL #15; ONB #15 | P7 NIST SP 800-53A Rev. 5 | ✅ | ✅ | ✅ — assessment procedures are tailorable to risk and assurance needs | ✅ — narrow corroboration of depth selection |
| 16 | HL #16; ONB #16 | P7 GitHub Checks; OASIS SARIF 2.1.0 | ✅ | ✅ | ✅ — aggregate conclusions coexist with detailed item annotations/results and locations | ✅ — existence example only |
| 17 | HL #17; ONB #17 | P7 RFC 9110 §9.2.2; Google Pub/Sub exactly-once delivery | ✅ | ✅ | ✅ — retry safety depends on idempotent semantics/known application state; acknowledgment and provider region bound delivery guarantees | ✅ — limits retry and exactly-once claims |

`TKL-20260913-01` is current but concerns knowledge-lifecycle allocation; it preserves D86 and neither
supersedes nor conflicts with Reviewer verdict semantics.

## Accounting Replay

| Approval / authority | Baseline | Candidate | Literal VALUE membership / actions / classes / reasons | Adds | Deletes | Touched LOC | Binary | Trigger disposition | Exact NUL-safe command | Verdict |
|---|---|---|---|---:|---:|---:|---|---|---|---|
| TS approved prospectively at `6705d7c524bdb025c9887e19f3e1e30023b44928`; owner-only expansion; no expansion | `504e4a34d182f4181f65134a5a3f42b4f2553be9` | `9e86910e498ab7f74e8d3ede4dfb5e7064d84cfb` | Exact 12/12 literal paths, all `M`, all VALUE, reasons match TS §4; no extra action/path | 538 | 365 | 903 | N/A — zero binary rows | 12 paths and 903 LOC remain below 50/5,000; no release effect | `git diff --name-status --find-renames=50% -z <Baseline> <Candidate> -- <12 literals>` and identical `--numstat` replay | VERIFIED |

Candidate is the first tested implementation commit. EV/RF and lifecycle changes follow it and do not
move VALUE. The local integration Candidate is a scoped byte-identical mirror, not a substituted
accepted-result identity.

## Selected Knowledge Evidence

- **Accepted research returns:** `research/iter1/RES.md` and `research/iter2/RES.md`; Researcher scope
  supplies bounded scenario facts and challenged design conclusions, while HL/TS remain the authority.
- **Executor return:** ONB `fe4bb36136f28756685bbd73803dfa88679de07b`, Candidate `9e86910…`,
  EV/RF `4ae3173…`, Executor unit `codex:thread:local:01a0c7fa-57ae-7171-af08-d6fbe0b734fa`;
  applicable to the exact selector and independently reproduced rather than accepted by presence.
- **Current Reviewer:** unit `codex:thread:local:01a0c822-51be-72b3-875f-4274d539c924`, directly
  delegated by the exact Parent Coordinator; independent of the Executor and authorized only to
  verify/judge/decide, not repair.
- **Currentness:** No selected qualified knowledge record supersedes the frozen purpose or approved
  Reviewer semantics. External sources corroborate bounded principles and carry no imported control
  regime.

## Checkpoint

**Self-check:**
- [x] Replayed the Map selection and verified all mandatory safety/security, authority and identity floors?
- [x] Established evidence applicability and ran every TS-required or dependency-affected check?
- [x] Recorded explicit limits instead of substituting file, discrepancy, test, commit or artifact counts?
- [x] Classified guards and controls by protected behavior, consequence and counterfactual detection?
- [x] Recorded every candidate finding with the complete item contract and material consequence test?
- [x] Verified RF AC claims, evidence references, citations and immutable accounting against actual artifacts?

Stage complete: YES
