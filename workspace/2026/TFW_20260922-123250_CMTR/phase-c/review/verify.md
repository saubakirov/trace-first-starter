# Verify — "Do the material claims hold?"
> **Mindset:** Auditor. RF is a declaration, not a fact. Open files, run necessary checks, compare
> accepted claims with reality, and state the limits.
> **Test:** "Would the evidence establish this claim for this subject, revision and environment without RF?"
> Map: [map.md](map.md)

## Selection Argument

| Claim IDs | Risk / criticality | Affected behavior / dependencies | Environment | Oracle / authority | Evidence gap / limit | Selected verification and why |
|---|---|---|---|---|---|---|
| C1, C2, C4 | High: compression can preserve keywords while losing launch, authority, return or evidence semantics. | Core launch decision and complete Plan flow. | Candidate and landed equivalent in Git. | Binding TS §6, iteration-4 D15–D21, baseline workflow. | Future operator behavior cannot be proven by prose inspection. | Read the whole Candidate Plan, review every baseline-to-Candidate hunk, compare the five steps clause-by-clause and reproduce the word count. |
| C3 | Medium: a stale execution profile would create two conflicting selection systems. | Four approved active-core files and future HL/TS authoring. | Candidate tree. | TS AC-3/AC-4 and owner acceptance. | Historical/profile identity text is valid and must not be mistaken for execution-profile residue. | Inspect both template diffs and use focused legacy-term searches with semantic review of every `profile` hit. |
| C5 | High: requested/delivery evidence can be overclaimed as effective setting, sufficiency or optimum. | Executor/Reviewer launches and future dispatch records. | Durable journals, RF/EV, current addressed activation. | TS AC-5; iter3 D13–D14; iter4 D18–D21; D59/D78. | Effective backend settings and equivalent-work lower comparison are unavailable. | Audit each observed layer and both recorded live-dispatch defects; scan active and phase text for forbidden claims. |
| C6 | High for repository compatibility; low as direct semantic proof. | Documentation generator, integration build and Git blob boundary. | Windows, Python 3.13.5, current accepted tree. | TS AC-5 and existing test oracles. | Green tests do not establish purpose or wording fidelity. | Rerun the exact suite, collect its cases, inspect the guarded behavior and verify no test file changed. |
| C7, C9 | Mandatory identity/scope/safety floor. | Accepted subject, value membership, landing and reserved external effects. | Git object database and worktrees. | TS accounting contract; D76/D77; dispatch reservations. | Git cannot prove absence of an unrecorded external act; no such act is claimed. | Replay exact NUL-safe selector accounting; verify Candidate reachability, full-tree landed equivalence, later VALUE absence and clean full status. |
| C8 | Mandatory human-authority and independence floor. | Review validity and return route. | Task state, journals and native addressed activation. | A2, phase TS approval, review dispatch and root activation contract. | Title/effective-model backend state is not independently exposed to this unit; durable dispatch records bounded readback. | Validate owner root, mandate, distinct units, exact destination/source and Coordinator-only return. |

## Verification Log

### V1: C1, C2, C4 — launch-selection meaning and compressed Plan
- **Accepted claim / authority:** The five-step rule and all material Plan controls survive the concise rendering; Plan stays at or below 1,400 words.
- **Subject tuple:** four VALUE files at `e29ae633814c47cc41c82afab6d5359cd66f78ca`; landed full-tree equivalent `7205fb50bf4e0ca1ba2eba4b28a66c9eea80121b`; Windows worktree; TS/HL/iter4 oracle; approved dependencies unchanged.
- **Action or evidence:** Read the full Candidate `plan.md`; inspected every `e819908..e29ae633` hunk and the complete `Launch selection` section; compared against TS §6 and iter4 D15–D21; independently counted words.
- **Observed:** Conventions contains exactly the accepted five ordered acts. Plan Step 5 preserves capability disclosure, explicit activation/dialogue/gateway/mandate controls, the per-launch prerequisite and quality-floor decision, separate model/effort, lower option with risk or `not compared`, native versus exact two-line application, and requested/effective/delivery/outcome/rework separation. Other shortened passages retain entry/routing, PV, future-state, HL freeze, research, amendment and TS gates. The Candidate Plan is 1,390 words. Naming is compact and action-oriented; no research label was imported.
- **Limit:** Prose and workflow inspection establish the rule and enforcement site, not universal compliance by future agents.
- **Result:** HOLDS

### V2: C3 — removal without replacement
- **Accepted claim / authority:** Legacy tier/execution-profile/self-calibration behavior is absent; the HL table ends at `Immutable epoch`; TS has no recommended profile field.
- **Subject tuple:** the four literal VALUE files at Candidate; TS AC-3/AC-4; active text only.
- **Action or evidence:** Inspected template diffs and searched for tier names, execution-profile forms, self-calibration, upshift/downshift and static-model examples; manually classified remaining `profile` occurrences.
- **Observed:** The HL execution-profile column/sample and TS field are deletion-only. No obsolete tier, model example or active-window self-calibration text remains. Remaining `profile` mentions concern participant identity/authority or the explicit sentence `profiles never substitute`; none selects model or effort.
- **Limit:** Historical task/research traces intentionally retain rejected terminology and were excluded from active-core residue classification.
- **Result:** HOLDS

### V3: C5 — evidence layers and live dispatch defects
- **Accepted claim / authority:** Requested, effective, delivery, outcome and material rework remain non-substitutable; defects are classified by cause rather than used as model-quality evidence.
- **Subject tuple:** Phase C journals/RF/EV at source `f4a970ac6f167a745e5d01efd9283e59c0bbb0dd`; current Reviewer activation; iter3/iter4 evidence rules.
- **Action or evidence:** Read every Phase C journal, RF and EV; compared Executor and Reviewer dispatches with the current addressed activation; scanned for effectiveness, optimum, sufficiency, savings and foreign-provider overclaims.
- **Observed:** Executor requested `gpt-5.6-terra` + `medium`; Reviewer requested `gpt-5.6-sol` + `high`; both name a lower option as `not compared`. Effective backend settings remain expressly unobserved. Address/worktree/title delivery and later artifact outcomes are recorded separately. The unnecessary child created by the first provisioning prompt is called a provisioning/follow-through defect; the missing later dispatch commit in the initial Executor source is called a source-delivery defect and repaired through the same unit. Neither is attributed to model capability. Reviewer delivery is observed by this exact addressed activation from the recorded Coordinator; review outcome is supplied only by the later verdict.
- **Limit:** No same-packet lower-resource comparison, backend readback, task-cost measurement or foreign-provider pilot exists; no minimum, savings or provider-wide claim is admitted.
- **Result:** HOLDS

### V4: C6 — existing guards and compatibility checks
- **Accepted claim / authority:** The configured existing suite passes, protects real repository behavior and is not used as proof of launch-selection meaning; no test was added.
- **Subject tuple:** landed Candidate-equivalent tree in the current Windows/Python environment; existing `tools/tests/` and `docs/scripts/` suites.
- **Action or evidence:** Ran `python -m pytest tools/tests/ docs/scripts/ -q`; collected all tests; inspected the blob, documentation-generator and integration cases; checked Candidate membership.
- **Observed:** `14 passed in 4.10s`. The tests protect the 5 MiB Git-blob boundary, title/frontmatter/path/link/glob/source handling, required documentation output and rendered-frontmatter leakage. Counterfactual fixtures include exact-versus-oversized blobs, hostile YAML titles, normalized paths, missing required sources and leaked rendered markup. No test path changed. These guards establish compatibility/invariants only; semantic fidelity is established by V1–V3 and independent judgment.
- **Limit:** The suite does not execute a real model selector or measure model quality, effort, cost or sufficiency.
- **Result:** HOLDS

### V5: C7 — accepted-result identity, accounting and crossing
- **Accepted claim / authority:** Baseline-to-Candidate accounting is exact, within the immutable denominator, and the crossed result preserves producer/role history and Candidate reachability.
- **Subject tuple:** baseline `e819908`; Candidate `e29ae633814c47cc41c82afab6d5359cd66f78ca`; landed equivalent `7205fb50bf4e0ca1ba2eba4b28a66c9eea80121b`; TS approval `d5a953fc985c343f93e92ab07e21123afff93f67`.
- **Action or evidence:** Replayed the TS's literal four-path NUL-safe name-status and numstat commands; inspected full status/cached names, commit authors/subjects, worktree topology, reachability and post-Candidate VALUE history; compared entire Candidate and landed trees.
- **Observed:** Four MODIFY paths only; 39 additions + 50 deletions = 89 touched text LOC; binary N/A; no rename or membership deviation. Original Candidate is an ancestor of Executor RF commit `6c88432435b07e4805c871f1349e9dbdff5d349a` in the still-existing Executor worktree. The landed commit `7205fb50…` has the same full tree `07d9ba37439b3e6424ebf329ab8995c3e0754c87` as Candidate, preserves the Executor commit subject/author, and current source has no later VALUE difference. Reviewer stage commits use exact-path staging.
- **Limit:** Executor-worktree cleanup remains correctly deferred until review/landing verification; the Reviewer does not remove it.
- **Result:** HOLDS

### V6: C8, C9 — authority, independence, safety and reserved effects
- **Accepted claim / authority:** A human-rooted A2 delegates Phase C coordination to the recorded Coordinator; distinct Executor and Reviewer units act only inside scope and return vertically; reserved effects remain untouched.
- **Subject tuple:** owner `saubakirov`; A2 `2c72ec8…`; coordination `addb2e7…`; Phase C TS approval; destination Reviewer `codex:thread:local:01a0c92b-bbfd-7431-9bc5-8a6e3cd68fef`; source `f4a970a…`.
- **Action or evidence:** Validated task/phase status, all journals, mandate/reservations, current source, direct activation, separate Executor/Reviewer addresses and exact `coordinator_route`; inspected all implementation paths and Git status.
- **Observed:** The spine is complete and child-only. Reviewer is independent from the Executor and has made no implementation/HL/TS/ONB/RF change. Scope contains no executable, credential, adapter, provider binding, release, push, history rewrite, permanent test or other external effect. Ordinary security behavior is unchanged.
- **Limit:** Provider backend settings and exactly-once transport behavior are not observable and are not used as authority or evidence.
- **Result:** HOLDS

## Commands Executed

| # | Command | Claim IDs | Result |
|---|---|---|---|
| 1 | `git diff --find-renames=50% --unified=12 e819908 e29ae633 -- <four literal paths>` | C1–C4, C7 | Full semantic diff inspected; four files only. |
| 2 | `git show e29ae633:.tfw/workflows/plan.md` | C1, C2, C4 | Complete Candidate workflow inspected. |
| 3 | `(Get-Content -Raw .tfw/workflows/plan.md \| Measure-Object -Word).Words` | C4 | `1390`. |
| 4 | Focused `rg` searches for tiers, execution profile, self-calibration, static names and overclaims | C3, C5 | No active legacy mechanism or forbidden claim; remaining profile terms are identity/negation. |
| 5 | `git diff --check e819908 e29ae633 -- <four literal paths>` | C4, C7 | Exit 0. |
| 6 | TS exact `git diff --name-status --find-renames=50% -z …` | C7 | Four `M` entries. |
| 7 | TS exact `git diff --numstat --find-renames=50% -z …` | C7 | `10/13`, `3/3`, `0/2`, `26/32`; total `39/50/89`. |
| 8 | `python -m pytest tools/tests/ docs/scripts/ -q` | C6 | Exit 0; `14 passed in 4.10s`. |
| 9 | `python -m pytest tools/tests/ docs/scripts/ -q --collect-only` and source inspection | C6 | 14 existing guards classified; no added test. |
| 10 | `git worktree list --porcelain`; reachability checks; Candidate/landing full-tree diff | C7, C8 | Candidate reachable through Executor RF; landed tree byte-identical at Git-tree level. |
| 11 | `git status --short`; `git diff --cached --name-status` before exact stage commits | C7–C9 | No foreign/staged path mixed into review commits. |
| 12 | Read-only Codex task listing plus durable dispatch/activation comparison | C5, C8 | Coordinator address resolves; current task omission from the listing is not used as title/effective-setting proof. |

## Claim and Source Checks

| # | Claim / citation | Where | Primary artifact / source | Holds? |
|---|---|---|---|---|
| 1 | Hard prerequisites, quality floor, adjacent lower discriminator and five evidence layers | TS §6; conventions; Plan | iter4 RES D15–D21 and accepted TS rendering | ✅ |
| 2 | Provider-specific rosters stay outside core and cross-surface claims remain bounded | conventions; HL/ONB | iter3 Gather G2–G5; iter3 RES D13; iter4 RES D21 | ✅ |
| 3 | Executor requested settings and delivery are observed, effective settings are not | Phase C dispatch/RF/EV | `20260922-173311__dispatch__41c6.md`, later transition/RF | ✅ |
| 4 | Live provisioning and source-delivery defects are not model-quality evidence | Phase C journals | dispatch `41c6`, gate answer `0e7c`, handoff `7ac4` | ✅ |
| 5 | Reviewer requested settings/delivery are separate from verdict/outcome | Reviewer dispatch and current activation | `20260922-175156__dispatch__8f31.md`; exact addressed activation | ✅ |
| 6 | Landed result is the exact Candidate content and remains reproducible | RF/EV accounting | Git trees `e29ae633^{tree}` = `7205fb50^{tree}`; Executor worktree RF descendant | ✅ |

## Guard and Check Admission

| # | Kind | Protected behavior / invariant | Failure consequence | Counterfactual detection | Admission |
|---|---|---|---|---|---|
| G1 | permanent guard | Git blobs at exactly 5 MiB pass; larger blobs fail. | Oversized history damages repository operation/distribution. | Fixture supplies exact-limit and limit+1 blobs; only larger is reported. | admitted |
| G2 | permanent guards | Documentation metadata, POSIX path mapping, link/glob routing and required sources. | Broken or unsafe generated reference pages and cross-platform paths. | Special YAML titles, path traversal normalization, mapping examples and missing-source exception. | admitted |
| G3 | permanent integration guards | Public core renders and generated frontmatter does not leak into page bodies. | Published documentation becomes missing or visibly corrupted. | Real MkDocs build plus required-output and negative offender scans. | admitted |
| G4 | temporary diagnostics / governance assertions | Word ceiling, exact path membership, LOC arithmetic, legacy-term absence and commit existence. | Detects scope/format/trace drift but cannot establish product purpose or model quality. | N/A; direct measurements on named revisions, not permanent behavioral guards. | temporary / governance only |

## Candidate Findings

No findings. The two live-dispatch defects are already accurately classified and repaired in their
own trace; they do not change Candidate content, authority, outcome attribution or the next authorized
act. No material VALUE, ASSURANCE or TRACE consequence remains open at Verify.

## Evidence Verification

| # | RF evidence ref | Subject tuple | Artifact exists? | Establishes the claim? | Limit |
|---|---|---|---|---|---|
| E1 | EV E1 | Candidate rule at exact four-file tree; TS/iter4 oracle | ✅ | ✅ | Establishes text/structure, not future compliance. |
| E2 | EV E2 | Executor and current Reviewer native dispatches on Codex | ✅ | ✅ | Requested/delivery/outcome trace is now complete enough for Phase C; effective setting/minimum remains unavailable and unclaimed. |
| E3 | EV E3 | Candidate templates and active-core legacy search | ✅ | ✅ | Historical traces legitimately retain rejected terms. |
| E4 | EV E4 | `e819908..e29ae633`; literal selector; Candidate environment | ✅ | ✅ | Counts are scope evidence only. |
| E5 | EV E5 | Current equivalent tree; existing test environment; independent review | ✅ | ✅ | Tests establish repository invariants; purpose is judged separately in Judge. |
| E-accounting | EV accounting | TS approval, baseline, Candidate, four actions/classes | ✅ | ✅ | Binary N/A; Candidate/landing crossing separately verified. |

## Knowledge Citations Verified

| # | Artifact | Priority + exact citation | Resolves? | Item exists? | Meaning matches? | Relevant? |
|---|---|---|---|---|---|---|
| 1 | HL/ONB #1 | P0 `.tfw/README.md` NS1 Purpose | ✅ | ✅ | ✅ — purpose, authority, inspectability and continuation outrank output/process volume. | ✅ — selection must preserve the quality/purpose floor. |
| 2 | HL/ONB #2 | P1 Methodology values + Success Criteria | ✅ | ✅ | ✅ — candor, structural enforcement, naming, portability and acceptance-ready output. | ✅ — rule must act at dispatch and stay provider-neutral. |
| 3 | HL/ONB #3 | P2 `knowledge/philosophy.md` F3/F36/F40/F43 | ✅ | ✅ | ✅ — critical challenge, purpose separate from quality, precise terminology, architecture over symptom fixes. | ✅ — supports independent purpose review and `Launch selection` naming. |
| 4 | HL/ONB #4 | P3 `KNOWLEDGE.md` D59/D64/D78 | ✅ | ✅ | ✅ — non-substitutable claim layers and purpose against baseline + North Star. | ✅ — directly governs evidence ceilings and Judge. |
| 5 | HL/ONB #5 | P3 `KNOWLEDGE.md` D79/D80/D81/D83 | ✅ | ✅ | ✅ — navigation is not authority; rooted delegation and distinct addressable units. | ✅ — directly governs launch prerequisites/topology. |
| 6 | HL/ONB #6 | P4 conventions HL Contract, Coordination, Design Rules, Anti-patterns | ✅ | ✅ | ✅ — frozen contract, enforcement site, ≤1,400-word ceiling and proxy/count prohibitions. | ✅ — direct implementation and review boundary. |
| 7 | HL/ONB #7 | P6 `knowledge/process.md` F22/F30/F31/F37/F40/F49 | ✅ | ✅ | ✅ — avoid generic tables, enforce at behavior site, review purpose, named-revision measurements and evidence-led decisions. | ✅ — direct support for four-file/no-extra-entity design and accounting method. |
| 8 | HL/ONB #8 | P7 `knowledge/environment.md` F5/F6 | ✅ | ✅ | ✅ — role/tool topology varies and one surface cannot prove another. | ✅ — bounds foreign-provider claims; F5's role-quality history is not used as a current model claim. |
| 9 | HL/ONB #9 | P7 `knowledge/constraint.md` F11/F12/F14 | ✅ | ✅ | ✅ — installed-surface proof, repository-owned obligations and separate decision act. | ✅ — supports native inspection, durable core rule and Coordinator close. |
| 10 | HL/ONB #10 | material source `research/iter3/RES.md` D9–D14/H1–H4/R6–R10 | ✅ | ✅ | ✅ — separate capability/effort, actual launch binding and bounded unknowns. | ✅ — predecessor design and claim ceilings. |
| 11 | HL/ONB #11 | material source provider-native evidence dated 2026-09-22 | ✅ — durable at iter3 Gather G2–G5 | ✅ | ✅ — exact tool/help/roster observations are explicitly surface-bounded. | ✅ — confirms why the core contains no static roster. |
| 12 | HL/ONB #12 | material source `research/iter4/RES.md` D15–D22/H1–H4 | ✅ | ✅ | ✅ — hard gate, oracle/consequence fork, lower option and five fields. | ✅ — binding TS rendering derives from it. |

P5 `knowledge/convention.md` has no launch/model/evidence item relevant to this result. P0 and P1
were read and applied as separate semantic inputs; neither was inferred from the other.

## Accounting Replay

| Approval / authority | Baseline | Candidate | Literal VALUE membership / actions / classes / reasons | Adds | Deletes | Touched LOC | Binary | Trigger disposition | Exact NUL-safe command | Verdict |
|---|---|---|---|---:|---:|---:|---|---|---|---|
| Owner acceptance `20260922-171921__gate_answer__3d91.md`; TS approved at `d5a953fc985c343f93e92ab07e21123afff93f67` before implementation | `e819908` | `e29ae633814c47cc41c82afab6d5359cd66f78ca` | MODIFY/VALUE `.tfw/conventions.md` (core rule); `.tfw/workflows/plan.md` (dispatch enforcement); `.tfw/templates/HL.md` (delete execution-profile column); `.tfw/templates/TS.md` (delete profile field). | 39 | 50 | 89 | N/A | 4/89 is below project prompts 50/5,000 and immutable maximum 4/300; no exception or split. | `git diff --{name-status,numstat} --find-renames=50% -z e819908 e29ae633… -- $valuePaths` with the TS's four literal paths | VERIFIED |

Candidate is the final tested VALUE commit in the Executor line after the in-boundary brevity pass.
Its Executor RF descendant remains reachable in the retained worktree; later landed trace commits do
not move VALUE, and landed commit `7205fb50…` is full-tree identical to Candidate.

## Selected Knowledge Evidence

| Source / epoch | Producer / unit | Scope and authority | Applicability |
|---|---|---|---|
| iter3 RES and accepted stages; A2/re-frozen HL | Researcher `01a0c89b…` | Per-launch rule, native surface observations and initial claim ceilings under Phase B dispatch/gates. | Applicable as design predecessor; its open empirical claims remain open. |
| iter4 RES and accepted stages; synthesis gate `59f1222…` | independent Researcher `01a0c8bf…` | Adversarial hard gate, oracle fork, lower-option and evidence-field refinement. | Applicable to TS rendering and evidence ceiling; no optimum claim imported. |
| Phase C ONB/RF/EV; TS approval `d5a953f…` | Executor `01a0c913…` | Four-file implementation and tests inside immutable denominator. | Candidate content, accounting and compatibility evidence independently replayed. |
| Phase C journals through review dispatch; source `f4a970a…` | Coordinator `01a0c400…` | Human-rooted dispatch/repair/return topology under A2. | Applicable to authority, live-pilot layers and defect classification; no model capability inference. |

## Checkpoint

**Self-check:**
- [x] Replayed the Map selection and verified all mandatory safety/security, authority and identity floors?
- [x] Established evidence applicability and ran every TS-required or dependency-affected check?
- [x] Recorded explicit limits instead of substituting file, discrepancy, test, commit or artifact counts?
- [x] Classified guards and controls by protected behavior, consequence and counterfactual detection?
- [x] Recorded every candidate finding with the complete item contract and material consequence test?
- [x] Verified RF AC claims, evidence references, citations and immutable accounting against actual artifacts?

Stage complete: YES
