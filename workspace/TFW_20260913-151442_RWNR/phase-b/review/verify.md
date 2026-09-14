# Verify — Phase B: “Are the claims true?”

> **Mindset:** Auditor. The RF is a declaration, not a fact.
> **RF:** [RF Phase B](../RF__phase-b__resume_surface_retirement.md), live return round §11
> **TS:** [approved revision 2](../TS__phase-b__resume_surface_retirement__rev2.md)
> **Immutable Candidate:** `6d6d094ac5325377772f26ddf314b965c1dfd135`
> **Min verify ratio:** `0.42`
> **RF implementation paths claimed:** `33`
> **Initial minimum:** `ceil(33 × 0.42) = 14`; one AC-8 discrepancy escalated verification to `33/33` paths.

## Verification Log

### V1 — Five deleted VALUE artifacts

- **RF claim:** the canonical workflow, canonical and installed Codex skill, and Antigravity/Claude full-copy commands are absent.
- **Actual:** Candidate commit records `D` for exactly `.tfw/workflows/resume.md`, `.tfw/adapters/codex/skills/tfw-resume/SKILL.md`, `.agents/skills/tfw-resume/SKILL.md`, `.agents/workflows/tfw-resume.md`, and `.claude/commands/tfw-resume.md`; none resolves in the Candidate tree.
- **Match:** ✅

### V2 — Twenty-five modified VALUE paths

- **RF claim:** all current registrations, manifests/config, adapter roots/copies, Init/Update copies, and current public documentation converge on the exact ten-command surface without changing Plan.
- **Actual:** all 25 patches were opened. The changes remove only the Resume registration or change fixed 11-command language to ten-command language; the three public READMEs route interrupted-work entry through Plan; conventions route selected close/recovery through Plan. Canonical/full-copy and managed-block parity are all true, Candidate Plan is byte-identical to Baseline and has 1,199 words.
- **Match:** ✅

The 25 opened paths were `.agent/rules/agents.md`, `.agents/rules/tfw.md`, `.tfw/adapters/antigravity/tfw-rules.md.template`, `.tfw/adapters/claude-code/CLAUDE.md.template`, `.tfw/adapters/codex/AGENTS.md.template`, `.tfw/adapters/cursor/tfw.mdc.template`, `.tfw/adapters/manifest.yaml`, `.tfw/conventions.md`, `.tfw/project_config.yaml`, `.tfw/templates/project_config.yaml`, `AGENTS.md`, `CLAUDE.md`, `README.kk.md`, `README.md`, `README.ru.md`, `.tfw/workflows/init.md`, `.agents/workflows/tfw-init.md`, `.claude/commands/tfw-init.md`, `.tfw/workflows/update.md`, `.agents/workflows/tfw-update.md`, `.claude/commands/tfw-update.md`, `.tfw/adapters/README.md`, `.tfw/adapters/claude-code/README.md`, `.tfw/adapters/antigravity/README.md`, and `.tfw/adapters/codex/README.md`.

### V3 — `docs/scripts/command_entry_eval.py`

- **RF claim:** only `resume` and the associated 11-command refusal are changed.
- **Actual:** the two one-line hunks remove `"resume"` from `REQUIRED_COMMANDS` and change `11-command` to `10-command`; Candidate blob is `fb8c3f0…`.
- **Match:** ✅

### V4 — `docs/scripts/test_repository_contracts.py`

- **RF claim:** exact surface, receiver/update, history, accounting, idempotence, and C1 models prove AC-1–AC-8.
- **Actual:** surface, real temporary receiver, history, and accounting oracles are substantive and independently reproduced. The C1 helper at lines 3858–3864 is not a path/byte model: when any input Boolean is false it assigns `implementation_matches_baseline = True` without accepting a baseline, a current tree, a path set, bytes, or a release-route result. The sole C1 test at lines 3919–3931 only compares that self-declared dictionary.
- **Match:** ❌ for AC-8; ✅ for the remaining stated responsibilities.

### V5 — `docs/scripts/test_runtime_context.py`

- **RF claim:** current runtime exposes ten commands, Resume discovery is unsupported, accepted Phase A Plan/routing/identity semantics remain, and no substitute appears.
- **Actual:** exact root/manifest/runtime command tuple is ten commands; Plan and its two copies stay fixed; Resume discovery is refused; root/manifest/role/Plan/replacement mutants fail. Historical Resume text is loaded only for frozen legacy assurance projections.
- **Match:** ✅

## Commands Executed

| # | Command | Result |
|---|---|---|
| 1 | `git diff-tree --no-commit-id --name-status -r --no-renames -z 6d6d094…` compared with the literal TS selector | `33/33`; `5 D + 28 M`; missing `0`, extra `0`, wrong action `0` |
| 2 | Candidate-bound `rwnr_phase_b_accounting_record(6d6d094…)` | `30 VALUE`; `5 DELETE + 25 MODIFY`; `25 + 326 = 351`; Plan `1,199`; `C=1,523 < B=2,737`; no unclassified instruction change; all copy/block parity true |
| 3 | Candidate-bound `rwnr_phase_b_history_record(6d6d094…)` | 179 entries; digest `ed52c4c…`; 2,243 protected paths with zero mismatch; three aggregate identities/subsequences true; all three mutants caught |
| 4 | Fresh `rwnr_receiver_migration_receipt()` in a temporary tree | clean `APPLIED`; repeat `APPLIED` with empty diff; cross-adapter foreign case `REFUSED`; whole connected group unchanged; evidence-only pinned guide confirmed |
| 5 | In a clean detached worktree at Candidate: `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_repository_contracts.py docs/scripts/test_command_entry_eval.py -q` | `388 passed in 414.63s` |
| 6 | Adversarial C1 probe: write `c1-restored`, hash; overwrite with `partially-retired`, hash; call `rwnr_phase_b_c1_decision({'mid_application': False})` | Actual hashes differ (`f0a598…` vs `ede909…`), yet oracle returns `implementation_matches_baseline: true` and `decision: C1` — false green reproduced |
| 7 | `git rev-parse` for excluded test at C1 restore and Candidate | both `7f195b31c622ac8cdbd7dad0a0f2e9ae7fa7a539` |
| 8 | Candidate-parent `git diff --check`; C1→Candidate and Candidate→RF ancestry checks | clean; both ancestry checks exit `0` |
| 9 | Byte comparison of all 30 VALUE paths between rejected Candidate `6d3f389…` and rev2 Candidate `6d6d094…` | zero mismatches; detailed receiver/history evidence reuse is applicable to unchanged claim inputs, with fresh Candidate execution added |

The Executor directly confirmed that cached staging was empty before staging, the explicit `$paths` set contained exactly 33 paths, the cached audit had `missing=0/extra=0`, and the commit used `git commit --only … -- $paths`. A complete `git status --short --untracked-files=all` was not recorded before that commit; only the tracked inventory used `--untracked-files=no`. The immutable commit nevertheless proves that the known foreign OTR tree and every other unlisted path are absent from Candidate. This is an execution-evidence limitation, not a competing Candidate-scope result; any replacement Candidate should record the full status required by TS §6.

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|---|---|---|---|
| C1 | “exactly 30 VALUE + three ASSURANCE paths” | RF §11.2/§11.4, EV E16 | Candidate parent→commit tree diff and approved rev2 selector/blob `8c06e15…` | ✅ exact 33-path identity and actions |
| C2 | “30 files; 25 + 326 = 351; `C=1,523`” | RF §11.2, EV E15/E-accounting-R2 | independent NUL-safe accounting oracle over Baseline `d366bb1…` and Candidate `6d6d094…` | ✅ reproduced |
| C3 | “mid-application … and landing-mismatch C1 models remain green” | RF §11.3/§11.4, EV E17 | only `rwnr_phase_b_c1_decision()` and its Boolean-dictionary test; adversarial changed-byte probe | ❌ green result does not establish whole-group byte identity or absence of a release route |

Every RF/EV citation resolves. The numerical and lineage claims above were checked against Git objects and executable primary oracles rather than copied from RF prose.

## Discrepancies Found

1. **AC-8 evidence is false green.** The approved gate requires four failure models — preflight, mid-application, Reviewer rejection, and landing mismatch — to assert whole-group path/byte identity and no release route. Only the preflight foreign-refusal model manipulates and compares a real connected tree. The remaining C1 helper declares baseline identity from Boolean inputs. A partial-byte mutation is therefore accepted by the test as “matches baseline.” This breaches TS AC-8 and also leaves frozen HL §7 principle 4 (“scenario evidence decides it”) unproved for the destructive fallback.
2. **Pre-commit observation limit.** Exact-path staged and committed membership is proven, but the Executor did not preserve the complete `--untracked-files=all` status observation requested by TS §6. This does not change the independently verified 33-path Candidate membership, but it should be closed in the replacement round rather than represented as evidence already collected.

The first discrepancy triggered 100% inspection of all 33 implementation paths.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|---|---|---|
| E10 / AC-1 | `phase-b-surface.json` rev2 validation | ✅ | ✅ exact five deletions, 25 VALUE modifications, ten commands, no live-classified match |
| E11 / AC-2 | `phase-b-receivers.json` + fresh receiver run | ✅ | ✅ four-adapter owned migration, foreign refusal, whole-group unchanged on preflight failure, idempotence |
| E12 / AC-3 | receiver receipt synthetic pinned target | ✅ | ✅ five ownership classes and evidence-only guide; no real migration identity in Candidate |
| E13 / AC-4 | `phase-b-history.json` + independent replay | ✅ | ✅ 179/digest/protected paths/three aggregate subsequences and mutants |
| E14 / AC-5 | surface/runtime oracles and targeted execution | ✅ | ✅ accepted Plan bytes/copies and retained Phase A route/identity behavior |
| E15 / AC-6 | `phase-b-accounting.json` + independent replay | ✅ | ✅ exact selector, actions, arithmetic, word limits, authority and trigger disposition |
| E16 / AC-7 | `phase-b-tests.txt`, Candidate Git objects, fresh target run | ✅ | ✅ 388 independently rerun; recorded 627 collect, 626+1 full, 31 focused, 32 state are applicable to the same Candidate; excluded test identity exact |
| E17 / AC-8 | receiver receipt, tests log, C1 helper | ✅ | ❌ artifact exists but does not model mid-application, Reviewer-rejection, or landing-mismatch byte/release outcomes |
| E18 / AC-9 | Candidate/TRACE scope and journal lineage | ✅ | ✅ justified N/A for release effect; no release metadata/effect, TKL import, or G2 route |
| E-accounting-R2 / AC-6 | `phase-b-accounting.json` rev2 validation | ✅ | ✅ independently reproduced, not inferred from rejected-Candidate summary |

The six evidence files referenced by RF §11.5 exist and have been opened: four structured JSON receipts, `phase-b-tests.txt`, and `EV__phase-b__resume_surface_retirement.md`. Evidence completeness is high; sufficiency fails only for E17/AC-8.

## Knowledge Citations Verified

The current HL §7.2 contains 33 citations and ONB §7 applies the same 33, for 66 citation applications. P0–P4 were scanned in full; P5–P7 were scanned by relevance. Each relative target resolves from the artifact that cites it.

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|---|---|---|---|---|---|
| 1 | HL/ONB #1 | P0 `README.md` → `How It Works` (inspectable context/checkpoint continuation) | ✅ | ✅ | ✅ | ✅ task-local continuation, not chat reconstruction |
| 2 | HL/ONB #2–#14 | P0 `.tfw/README.md` → NS1, NS2.1–NS2.7, NS3 clauses, `Where truth belongs` | ✅ | ✅ all 13 | ✅ all 13 | ✅ purpose, subtraction boundary, authority, history and non-goals map directly |
| 3 | HL/ONB #15–#21 | P1 `.tfw/README.md` → four Methodology values and Success Criteria 1, 2, 4 | ✅ | ✅ all 7 | ✅ all 7 | ✅ especially Structural Enforcement; this citation is also the value implicated by the AC-8 false green |
| 4 | HL/ONB #22–#23 | P2 `knowledge/philosophy.md` → F3 and F45 | ✅ | ✅ both | ✅ | ✅ adversarial proof and subtraction/artifact budget |
| 5 | HL/ONB #24–#26 | P3 `KNOWLEDGE.md` §1 → D15, D31, D68 | ✅ | ✅ all 3 | ✅ | ✅ canonical adapters, research-local continuation and task-local state |
| 6 | HL/ONB #27–#29, #33 | P4 `.tfw/conventions.md` → HL Contract, Design Rules, Anti-patterns, Session identity/AT | ✅ | ✅ all 4 | ✅ | ✅ amendment, 1,200-word cap, Role Lock/history and exact unit identity |
| 7 | HL/ONB #30–#31 | P6 `knowledge/process.md` → F37 and F39 | ✅ | ✅ both | ✅ | ✅ revision-bound measurement and search-derived delivery set |
| 8 | HL/ONB #32 | P7 `knowledge/stakeholder.md` → F13 | ✅ | ✅ | ✅ | ✅ supplies deletion direction without waiving proof |

`knowledge/convention.md` (P5) contains relevant canonical-first/adapter patterns but no additional item that changes this Phase B decision. `KNOWLEDGE.md` §1 still describes the pre-retirement current topology as 11 routes including Resume. That is a real post-Candidate knowledge-capture delta, but the approved Phase B selector and master DoF 10 explicitly prohibit knowledge consolidation in this phase; it is not a Candidate implementation contradiction to be silently fixed by the Reviewer. The three cited P3 decisions themselves remain valid.

## Checkpoint

**Self-check:**

- [x] Opened and recorded all `33/33` implementation paths after discrepancy escalation.
- [x] Independently established evidence applicability and ran the affected Candidate and receiver/accounting/history checks.
- [x] Spot-checked the three highest-load claims, resolved every RF/EV reference, and checked data against Git/executable sources.
- [x] Checked every RF §11.3 AC checkmark; AC-8 is not established.
- [x] Checked `KNOWLEDGE.md`; the expected post-retirement capture delta is documented without mutating it.
- [x] Verified all 66 HL §7.2/ONB §7 applications: resolved `66`, semantically verified `66`, irrelevant `0`, hallucinated `0`.
- [x] Verified all six RF evidence artifacts: present `6`; materially adequate for eight AC rows plus accounting, inadequate for E17/AC-8.

Stage complete: **YES**

## Affected Return Round 3 — Verify

> **Immutable Candidate:** `a81e0c12ec982ee4f73639ebf15394ef53877294`
> **Candidate parent:** `5cfca7abfa51fe3f565295ca4fc8be81c74c474f`
> **Affected bound:** AC-7/AC-8, 33/33 Candidate paths after discrepancy escalation

### Verification log

#### V-A1 — fresh Candidate lineage, scope, accounting and applicability

- **RF claim:** fresh Candidate is built from the coherent C1 implementation baseline, contains exactly
  30 VALUE + 3 ASSURANCE paths, retains the excluded test blob, and preserves the unaffected rev2
  product/evidence inputs.
- **Actual:** Git identifies parent `5cfca7a…`, tree `b043a11…`, and exactly 33 paths with `5 D + 28 M`.
  The parent is byte-identical to original C1 restore `d09d5d4…` across all 33 paths. The 30 VALUE
  paths and both other ASSURANCE paths are byte-identical to rejected rev2 Candidate `6d6d094…`;
  only `docs/scripts/test_repository_contracts.py` changes in the affected implementation. Excluded
  `docs/scripts/test_command_entry_eval.py` has blob
  `7f195b31c622ac8cdbd7dad0a0f2e9ae7fa7a539` at both parent and Candidate. Independent accounting
  returns 30 VALUE, `5 DELETE + 25 MODIFY`, `25 + 326 = 351`, Plan 1,199,
  `C=1,523 < B=2,737`, and zero unclassified instruction changes. `git diff --check` is clean.
- **Match:** ✅ for immutable result identity, membership, accounting and prior-finding applicability.

#### V-A2 — real complete-group C1 oracle

- **RF claim:** preflight failure, one-write mid-application failure, Reviewer rejection and
  landing/integrated mismatch each restore the complete 33-path before-image and emit no release
  route/effect; altered-path, one-deletion-left and emitted-release mutants reject.
- **Actual:** the affected implementation materializes actual temporary files, performs a real
  deletion in the mid-application branch, restores all 33 paths, observes presence/size/SHA-256 for
  every approved path plus unexpected files, and compares the full map to the immutable C1 image.
  Independent execution returned no changed or unexpected path, identical digest
  `1a2d5d271b7ae2cf5c246f0b1344b71a0cbb1143a00c8204c8d853fcb292c666`, empty release
  route/effect, and `oracle_pass=true` for all four scenarios. Each of the three hostile mutants
  returned `oracle_pass=false`. The committed return-round-3 receiver receipt matches the independent
  maps, digest, scenario observations and mutant outcomes.
- **Match:** ✅ AC-8's previously false-green implementation/evidence defect is corrected.

#### V-A3 — affected and retained regression evidence

- **RF claim:** the fresh Candidate passes 392 targeted tests, 631 collection, 630+1 configured,
  31 focused command-entry and 32 state tests; the four C1 cases contribute five affected tests.
- **Actual:** in a clean detached worktree at exact Candidate, the Reviewer independently ran the
  C1 selection (`5 passed, 133 deselected`) and the complete targeted command (`392 passed in
  443.02s`). In the continuing review tree, collection reproduced 631, state reproduced 32, and the
  excluded focused module reproduced 31. The Executor's post-freeze full-suite receipt records
  `630 passed, 1 skipped` at the same immutable Candidate; its command, environment, Candidate and
  relevant inputs remain unchanged, so it is applicable without another full-suite run.
- **Match:** ✅ test outcomes and applicability.

#### V-A4 — exact-path Candidate creation and durable pre-commit evidence

- **RF claim:** full status named only the approved 33 paths, pre-stage cached inventory was empty,
  literal selector/staged counts were 33/33 with no missing/extra path, and the fresh Candidate is a
  reproducible exact-path boundary.
- **Actual:** Candidate Git objects prove the final parent-to-commit set is exactly the approved 33
  paths. On direct read-only clarification, Executor unit
  `01a09b39-f0c0-70c0-9b53-6981647e72fb` confirmed that the contemporaneous full status, empty
  index, literal 33-path selector, `git add -- $rwnrCandidatePaths`, and complete staged-name output
  exist only in that task's tool transcript; committed `phase-b-tests.txt` preserves summaries, not
  the verbatim inventories. More importantly, the exact Candidate command was
  `git commit -m '[codex/01a09b39-f0c0-70c0-9b53-6981647e72fb/executor] create corrected Phase B Candidate'`:
  it supplied no `--only` and no pathspec. This fails the review workflow's unconditional
  exact-path-staging requirement to verify complete durable pre-commit evidence and
  `git commit --only -- <paths>`, and conflicts with TS technical guidance requiring exact-path
  staging over only the 33 paths after full status inspection.
- **Match:** ❌ AC-7 reproducible Candidate evidence/process is not established, although the final
  Candidate content and scope themselves are exact.

### Commands executed / evidence reused

| # | Check | Result |
|---|---|---|
| A1 | `git show`, `diff-tree`, exact selector/action comparison for `a81e0c…` | Parent/tree resolved; 33/33; `5 D + 28 M`; no missing/extra/wrong action. |
| A2 | C1 original restore → coherent parent comparison over all 33 paths | Empty diff. |
| A3 | Rejected rev2 Candidate → fresh Candidate implementation comparison | Only `docs/scripts/test_repository_contracts.py`; all 30 VALUE and two other ASSURANCE paths unchanged. |
| A4 | `rwnr_phase_b_accounting_record(a81e0c…)` | 30 VALUE; `25 + 326 = 351`; Plan 1,199; `C=1,523`; no unclassified path. |
| A5 | `python -m pytest docs/scripts/test_repository_contracts.py -q -k "rwnr_phase_b_c1"` in clean Candidate worktree | `5 passed, 133 deselected`. |
| A6 | `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_repository_contracts.py docs/scripts/test_command_entry_eval.py -q` in clean Candidate worktree | `392 passed in 443.02s`. |
| A7 | configured collection / state / focused module | `631 collected`; `32 passed`; `31 passed in 44.67s`. |
| A8 | recorded post-freeze configured full suite | `630 passed, 1 skipped in 701.40s`; applicable to exact Candidate and unchanged inputs. |
| A9 | direct Executor clarification of actual pre-commit observations and command | Full inventories only in task transcript; committed evidence summarizes; Candidate command omitted `--only` and all pathspecs. |

### Claim and source checks

| # | Claim checked | Primary source | Holds? |
|---|---|---|---|
| A-C1 | All four C1 scenarios restore the real 33-path map and prohibit release | affected implementation, independent temporary-tree execution, `phase-b-receivers.json` return round 3 | ✅ |
| A-C2 | Fresh Candidate has exact 30+3 membership and unchanged excluded test | Candidate Git tree/diff and blob identities | ✅ |
| A-C3 | Complete exact-path pre-commit evidence and Candidate creation satisfy the accepted return | committed `phase-b-tests.txt`, Candidate commit, direct Executor clarification | ❌ summary-only repository evidence; actual commit lacked required `--only -- <paths>`. |

### Discrepancy and 100% escalation

1. **AC-7 / exact-path staging remains unproved and was not followed.** TS AC-7 requires reproducible
   immutable Candidate evidence whose claims resolve to raw evidence; TS technical guidance requires
   exact-path staging over only the approved 33 paths after full status inspection. The canonical
   review contract additionally requires `git commit --only -- <paths>`. The actual commit used no
   `--only` or pathspec, and the complete contemporaneous inventories were not preserved in committed
   task-local evidence. Frozen master HL DoD 17 requires independent verification of evidence
   integrity before landing; final tree membership cannot retroactively prove the omitted commit
   method or durable pre-commit observation.

The discrepancy escalated verification to 100%. All 33 Candidate paths/actions were checked; all 32
unaffected implementation paths were matched byte-for-byte to already reviewed inputs, and the sole
affected path was opened, exercised and matched to the round-3 receipt. No additional product defect
was found.

### Evidence verification

| Evidence | Exists? | Affected judgment |
|---|---|---|
| `phase-b-receivers.json` return round 3 | ✅ | ✅ Complete 33-path scenario maps/digest and three rejecting mutants match independent execution. |
| `phase-b-tests.txt` return round 3 | ✅ | ⚠️ Test, scope and accounting summaries match, but exact pre-commit inventories/command are not preserved verbatim. |
| `phase-b-accounting.json`, `phase-b-surface.json`, `phase-b-history.json` | ✅ | ✅ Candidate identity and unaffected findings remain applicable; accounting independently reproduced. |
| cumulative EV/RF return round 3 | ✅ | ⚠️ AC-8 evidence is now sufficient; AC-7 overclaims a complete reproducible Candidate boundary. |

### Knowledge citation applicability

The affected implementation changes only `docs/scripts/test_repository_contracts.py`; the 30 VALUE
paths, other two ASSURANCE paths, master HL citation table, ONB §7 citation table, and every cited
P0–P7 source retain the inputs and meanings independently verified in the preceding 66/66 scan.
The Verify PV scan was repeated at the routing/source level: P0 purpose/NS1–NS3, P1 methodology
values/success criteria, P2 philosophy, P3 architecture decisions, P4 contract/design/prohibitions,
and relevant P6/P7 items still resolve and remain applicable. No citation changed or became
irrelevant. The AC-7 finding specifically reinforces P0 Selected Trace, P1 Structural Enforcement,
and frozen DoD 17 rather than introducing a new product-purpose objection.

### Affected checkpoint

- [x] Verified 33/33 Candidate paths after discrepancy escalation.
- [x] Independently executed the changed AC-8 oracle and complete targeted suite.
- [x] Reproduced collection/state/focused results and established full-suite applicability.
- [x] Checked exact Candidate parent/tree/scope/actions/accounting/excluded blob.
- [x] Checked committed evidence against the actual Executor command without reconstructing missing proof.
- [x] Retained prior citation verification only where citation tables, sources, meanings and application inputs are unchanged.

Affected Verify stage complete: **YES**

## Final Affected Return Round 4 — Verify

> **Immutable Candidate:** `51ea3015290393da001810629f305f5969f4c8b8`
> **Candidate parent / coherent C1 baseline:** `41a70febc6d33d369af125d7ad2ecf98a2de0761`
> **Reference corrected implementation:** `a81e0c12ec982ee4f73639ebf15394ef53877294`
> **Affected bound:** AC-7 exact-path process/evidence plus applicability of the already verified AC-8 result

### Verification log

#### V-R4.1 — exact Candidate boundary and command provenance

- **RF claim:** the Executor captured the complete boundary outside the repository, staged exactly
  the 33 approved paths, used literal-path `git commit --only -- <33 paths>`, and preserved a
  byte-identical phase-local receipt only after Candidate freeze.
- **Actual:** the raw receipt records the complete 33-line pre-status, empty pre-index, ordered
  33-path selector, literal `git add --` arguments, staged names/actions, `missing=0`, `extra=0`,
  clean cached diff, the actual `git commit -m … --only -- <33 literal paths>` command and its
  result, then empty post-status/index and the immutable Candidate inventory. An independent parser
  matched every selector, status, staging, commit and Candidate set in exact order. The outside and
  repository copies are both 12,400 bytes, byte-identical, and hash to
  `4c3350df1a496af6de502c10f2dd9ca773a4872167ca53d573008831bc476530`.
  The Executor's read-only task transcript independently confirms the same actual command and
  result.
- **Match:** ✅ the prior AC-7 process/evidence discrepancy is closed.

#### V-R4.2 — immutable Git identity, membership and accounting

- **RF claim:** Candidate is a byte-identical replay of the corrected 30 VALUE + three ASSURANCE
  implementation from coherent C1 and retains the exact approved accounting.
- **Actual:** Git resolves parent `41a70f…`, tree `315173ab9971cfa4d31bb0a7000768bf3ae11b54`,
  and exactly 33 changed paths with `5 DELETE + 28 MODIFY`. Candidate names/actions exactly match
  the receipt and approved selector. A 33-path comparison to `a81e0c…` is empty; the C1 parent is
  likewise byte-identical to original C1 restore `d09d5d…` over the group. Independent accounting
  returns 30 VALUE, `5 DELETE + 25 MODIFY`, `25 + 326 = 351`, Plan 1,199,
  `C=1,523 < B=2,737`, and no unclassified instruction change. The excluded test retains blob
  `7f195b31c622ac8cdbd7dad0a0f2e9ae7fa7a539` at parent and Candidate.
- **Match:** ✅ identity, membership, action, denominator and accounting claims hold.

#### V-R4.3 — Candidate-bound tests and AC-8 applicability

- **RF claim:** the exact fresh Candidate passes the required suites, while the already corrected
  real C1 models and hostile mutants remain unchanged and applicable.
- **Actual:** the raw targeted receipt hashes to
  `bfd9410246c865506f31017e318214b34a961142d4e281f3001f8bf769a7cd22` and records
  `392 passed` with exit 0. The raw configured-full receipt hashes to
  `ef612a1d155d9d37ce88809567faece9a1c17561a4512d7516751b5f9efff60a` and records
  `630 passed, 1 skipped` with exit 0. The cumulative log also records 631 collected, 31 focused,
  32 state and a clean Candidate diff. The Executor transcript confirms both raw command/results.
  In a clean temporary worktree at exact Candidate, the Reviewer independently reran the affected
  C1 selection: `5 passed, 133 deselected`. All 33 implementation bytes, affected oracles and
  excluded-test identity match the already independently verified corrected implementation.
- **Match:** ✅ new gates hold and the prior AC-8 finding remains applicable without reconstruction.

#### V-R4.4 — lineage, authority and prohibited effects

- **RF claim:** this is only the Coordinator-accepted rung-1 exact-path return; it neither lands the
  Candidate nor changes product authority, knowledge, shared history, G2 or release state.
- **Actual:** Candidate is an ancestor of RF producer
  `fd795babc5d22608c95e8afb0b0cb3540f2c9e9b`, which is an ancestor of dispatch
  `bc023eaf4ced737c437f02cbb10dce3ae09d08ac`. Prior REVIEW producer `9eaf775…` is an ancestor of
  the C1 baseline. Candidate contains only the approved 33 implementation paths; no evidence,
  knowledge, digest, TKL, release or shared-master path is present. The governing TS blob remains
  `8c06e15e3ad8211195f2d48314d055ad1f111979` under approval
  `e5efd3e608975184995d254bc5eb84176b8b4451`.
- **Match:** ✅ authority and effect boundaries hold.

### Commands executed and evidence reused

| # | Check | Result |
|---|---|---|
| R4-1 | Independent parser over `phase-b-candidate-boundary-round4.txt` | Selector, pre-status, staged names/actions, stage arguments, commit arguments and Candidate names/actions all exact 33/33; empty pre/post indexes; `--only` present. |
| R4-2 | SHA-256 and byte comparison: outside receipt ↔ repository receipt | Both 12,400 bytes; byte-identical; SHA-256 `4c3350…`. |
| R4-3 | Git `show` / `diff-tree` / selector-action comparison for `51ea301…` | Parent/tree resolved; exactly 33 paths; `5 D + 28 M`; receipt and Git agree. |
| R4-4 | Git comparisons `a81e0c… ↔ 51ea301…` and `d09d5d… ↔ 41a70f…` over the 33 paths | Both diffs empty. |
| R4-5 | Candidate ancestry through RF and dispatch producers | Candidate → `fd795ba…` → `bc023ea…`; prior REVIEW producer precedes C1 baseline. |
| R4-6 | Independent accounting at exact Candidate | 30 VALUE; `25 + 326 = 351`; Plan 1,199; `C=1,523`; zero unclassified paths. |
| R4-7 | `python -m pytest docs/scripts/test_repository_contracts.py -q -k "rwnr_phase_b_c1"` in clean Candidate worktree | `5 passed, 133 deselected in 9.91s`. |
| R4-8 | Raw Candidate-bound targeted/configured-full receipts plus direct transcript confirmation | Exit 0; `392 passed`; `630 passed, 1 skipped`; receipt hashes match RF. |
| R4-9 | Temporary Candidate worktree post-check | Exact HEAD, clean worktree after verification; safely removed. |

### Claim and source checks

| # | Claim checked | Primary source | Holds? |
|---|---|---|---|
| R4-C1 | Actual Candidate command used exact literal-path `--only` form and no unapproved path | complete raw boundary receipt, external byte twin, Executor tool transcript, immutable Git inventory | ✅ |
| R4-C2 | All 33 bytes equal the corrected AC-8 implementation and preserve exact accounting | Git objects/diffs plus independent Candidate accounting | ✅ |
| R4-C3 | Candidate-bound tests and no-release recovery behavior hold | raw pytest receipts, independent affected C1 run, Candidate tree | ✅ |

### Discrepancies found

No discrepancies. The earlier AC-7 discrepancy already required a 100% path check; this return
again checks all 33/33 Candidate paths and the complete boundary receipt.

### Evidence verification

| Evidence | Exists? | Final affected judgment |
|---|---|---|
| `phase-b-candidate-boundary-round4.txt` | ✅ | ✅ Complete, authentic exact-path boundary; external copy matches byte-for-byte and command transcript agrees. |
| `phase-b-targeted-round4.txt` | ✅ | ✅ Exact Candidate, exit 0, 392 passed; hash matches RF. |
| `phase-b-full-round4.txt` | ✅ | ✅ Exact Candidate, exit 0, 630 passed + one skip; hash matches RF. |
| `phase-b-tests.txt` round 4 | ✅ | ✅ Collection/focused/state/diff/scope/accounting chronology agrees with primary receipts and Git. |
| `phase-b-accounting.json` → `return_round_4_validation` | ✅ | ✅ Identities, actions, arithmetic, denominator and terminal exact-path verdict independently reproduced. |
| cumulative EV/RF return round 4 | ✅ | ✅ E28–E-accounting-R4 and RF §13 resolve to the primary artifacts without overstatement. |

### Knowledge citation applicability

The full prior 66/66 HL §7.2 and ONB §7 citation verification remains applicable because the
governing tables and P0–P7 sources are unchanged, while all 33 implementation inputs and affected
oracles are byte-identical to the independently verified corrected result. The Review PV scan again
confirms the deciding applications: P0 NS1–NS3 require explicit continuation and bounded human
authority; P1 Structural Enforcement and Candor require an observable exact-path boundary; P2 F3
requires hostile critical-opponent tests; P3 D15/D31/D68 retain thin adapters and task-local state;
P4 Exact-path, Role Lock, design and anti-pattern rules apply directly; relevant P6 F37/F39 require
revision-bound measurement and search-derived scope; P7 stakeholder F13 supplies the deletion value
without waiving proof. Resolved `66`, semantically verified `66`, irrelevant `0`, hallucinated `0`.

### Final affected checkpoint

- [x] Verified 33/33 Candidate paths, actions, bytes and exact-path command boundary.
- [x] Independently established raw receipt authenticity, external-copy identity and transcript provenance.
- [x] Independently reproduced accounting and the affected C1 tests at the immutable Candidate.
- [x] Verified all RF §13.3 checks against Git, raw evidence or unchanged independently reviewed inputs.
- [x] Verified six return-round-4 evidence groups; present `6`, adequate `6`, missing `0`.
- [x] Reconfirmed all 66 citation applications remain resolved and relevant on unchanged inputs.

Final affected Verify stage complete: **YES**
