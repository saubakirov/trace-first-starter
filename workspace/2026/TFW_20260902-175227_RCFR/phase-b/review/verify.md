# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed: 23
> Files to verify: ⌈23 × 0.42⌉ = 10; escalated to 23 after discrepancies V5-D1 and V5-D2; routing authorities then checked for V7-D3

## Verification Log

### V1: canonical primary-role workflows (4 files)
- **Paths:** `.tfw/workflows/plan.md`, `.tfw/workflows/research/base.md`, `.tfw/workflows/handoff.md`, `.tfw/workflows/review.md`.
- **RF claim:** each primary path has a selective read contract, preserved role semantics, explicit gates, and a hard stop.
- **Actual:** all four algorithms were read completely. The Coordinator retains inception/amendment branches and approval gates; Research retains resume/mode/OODA/stage-template behavior; Executor retains acceptance/refusal, TS execution, evidence and RF handoff; Reviewer retains independent Bootstrap/Map/Verify/Purpose/Decide stages. Supplemental routing verification found the Reviewer Step 6 contradiction detailed in V7.
- **Match:** ❌ — three paths hold; Reviewer verdict routing does not have one executable meaning

### V2: canonical and installed skills (8 files)
- **Paths:** `.tfw/adapters/codex/skills/tfw-{plan,research,handoff,review}/SKILL.md` and `.agents/skills/tfw-{plan,research,handoff,review}/SKILL.md`.
- **RF claim:** thin skills route to canonical workflows without independent common-library preload and enforce role/template/stop contracts.
- **Actual:** all eight files were opened. Each installed copy is byte-identical to its canonical source by SHA-256; the claimed thin routing, role lock, staged template gate, and hard stop are present.
- **Match:** ✅

### V3: generated command/workflow copies (8 files)
- **Paths:** `.claude/commands/tfw-{plan,research,handoff,review}.md` and `.agent/workflows/tfw-{plan,research,handoff,review}.md`.
- **RF claim:** all derived copies match the canonical workflows.
- **Actual:** all eight files were opened or hash-compared; every `.claude/commands` and `.agent/workflows` copy is byte-identical to its canonical workflow.
- **Match:** ✅

### V4: `.tfw/adapters/manifest.yaml`
- **RF claim:** the four primary skills and workflows remain declared as strict adapters with the required sources and destinations.
- **Actual:** the manifest contains the claimed four skill routes and four workflow routes, including the two generated workflow destinations.
- **Match:** ✅

### V5: `docs/scripts/test_runtime_context.py`
- **RF claim:** the audit measures a complete, symmetric baseline/candidate read graph, rejects omitted routes and non-source-derived semantics, demonstrates one output-changing mutant in every P/R/E/V/C/A family, and proves all reductions.
- **Actual:** baseline counts, implementation surface, copy checks, receiver checks, and threshold arithmetic are reproducible. Two material gaps remain:
  1. `_add_primary_supplements()` line 682 adds only `RESEARCH_STAGE_TEMPLATES[:1]` to a candidate Researcher graph that already has a workflow contract, omitting `2_gather.md`, `3_extract.md`, and `4_challenge.md` even though the candidate workflow requires those staged reads. The published candidate totals 5,362/5,427 therefore undercount 741 words; full staged totals are 6,103/6,168. Corrected reductions remain 79.7%/79.5%, so the threshold holds but graph completeness and the stated exact candidate totals do not.
  2. `source_mutant()` lines 319–340 changes each scenario probe needle. The family-parametrized test at lines 365–369 then fails on an absent anchor before producing a `SemanticRecord`; only the separate E3 substitution test at line 343 demonstrates changed produced output. A direct reproduction for P1, R1, E1, V1, C1, and A1 yielded `no record produced` followed by `SourceContractError` in every family.
- **Match:** ❌

### V6: `docs/scripts/test_integration.py`
- **RF claim:** adapter parity, clean receiver cardinality, reinstall repair, idempotence, preservation, and legacy route retirement are enforced.
- **Actual:** relevant tests and helpers were inspected; the targeted and full suites pass. Direct hashes confirm installed/canonical and generated/canonical parity, and the clean-receiver evidence reports 11/11 artifacts for all four receivers.
- **Match:** ✅

### V7: Reviewer three-rung routing authorities
- **Paths:** `.tfw/workflows/review.md:143,153,159`; `.tfw/conventions.md:580–600,897–900,932–939`; TS AC-4 and §4; current Phase B REVIEW/status/journal.
- **RF claim:** AC-4's three-rung route, acceptance-authority boundary, REVISE transitions, and Reviewer hard stop retain meaning and are source-backed.
- **Actual:** the mandatory Decide sources issue mutually exclusive actions for a rung-1 finding. The convention table says rung 1 goes “back to execution” and “nothing” moves, while rung 2 alone moves to `TS_DRAFT` only when the TS is actually changed. Role Lock confirms rung 1 “needs no coordinator.” In contrast, review Step 6 and the convention Hard Stop send every REVISE to the Coordinator for a TS revision and set `TS_DRAFT`. This review reproduced the consequence: REVIEW §4 items 1–2 are explicitly rung 1, yet status and journal moved `RF → TS_DRAFT` and routed `/tfw-plan` under the universal instruction.
- **Match:** ❌

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `git rev-parse HEAD` before Reviewer traces / `git show -s --format=%H 272a7cf` | Governing implementation candidate resolves to `272a7cf737c84958d81c41257cc9c2568c74ee0f`. |
| 2 | `git cat-file -e 80382fbffd52b1f13cb3b38e8e450ecc0fef2fd5^{commit}` and baseline audit reproduction | Immutable baseline exists; exact fixed counts reproduce as 50,851 / 29,992 / 30,057 / 55,885 / 74,537. |
| 3 | `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_integration.py -q` | 143 passed in 183.54s. |
| 4 | `python -m pytest .tfw/scripts/ docs/scripts/ -q --collect-only` | 437 tests collected in 0.40s. |
| 5 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | 436 passed, 1 skipped in 219.43s. |
| 6 | `python .tfw/scripts/gen_index.py --check project` | Exit 0; project index consistent. |
| 7 | `python .tfw/scripts/gen_index.py --check tasks` | Exit 1 only for the pre-existing immutable RDP event summary at 123 words over a 120-word limit; no Phase B diagnostic. |
| 8 | `git diff --numstat 80382fbf..HEAD -- <23 implementation/test paths>` | 23 files, +733/−272 = 1,005 changed LOC, within both budgets. |
| 9 | `git diff --name-only 80382fbf..HEAD -- <frozen exclusions>` | Empty for `tasks/**`, `TFW-36`, RDP, templates, secondary workflows, `project_config.yaml`, and `state.yaml`. |
| 10 | SHA-256 comparisons for canonical/installed skills and canonical/generated workflows | All twelve destination comparisons equal their canonical source. |
| 11 | Direct Researcher graph diagnostic using the audit module | Focused: reported 5,362 vs full 6,103; deep: reported 5,427 vs full 6,168; three required stage templates missing from each reported graph. |
| 12 | Direct family-mutant diagnostic using the audit module | P1/R1/E1/V1/C1/A1 all rejected at probe resolution; none produced a mutated semantic record. |
| 13 | Line-addressed comparison of Reviewer Step 6 with convention `The 🔄 REVISE route` and `Role Lock Protocol` | Rung 1 requires direct return to execution with no state move/coordinator; the universal Step 6/Hard Stop requires Coordinator, TS revision, and `TS_DRAFT` for the same case. |
| 14 | `git diff --quiet 80382fbf..272a7cf -- .tfw/conventions.md` plus review-workflow diff | Conventions are unchanged from the immutable baseline; Step 6's universal route is also unchanged. Phase B did not create the contradiction, but its AC-4 acceptance claim and mandatory Decide read path expose and claim to preserve one meaning that the sources do not have. |
| 15 | Inspection of V1–V4/C1 scenarios and Reviewer assertions in `docs/scripts/test_runtime_context.py` | No case distinguishes rung 1, rung 2, or rung 3 recipients/state effects; V4 checks generic proposal authority only, so the green semantic suite cannot detect this conflict. |
| 16 | Self-host trace: Phase B REVIEW §4 items 1–2, status, and `20260904-121258__transition__f28c.md` | Two rung-1 findings were nevertheless returned to the Coordinator and moved `RF → TS_DRAFT`, demonstrating observable routing ambiguity. |

The first ad-hoc module import omitted registration in `sys.modules` and failed before exercising repository code; it was corrected and rerun for commands 11–12 with no repository effect.

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | exact Phase B baseline is `80382fbf…` with five fixed counts | TS AC-1; RF §3/§4; EV E1 | immutable Git commit plus direct audit reproduction | ✅ |
| C2 | all five candidate paths clear 30% and combined reduction is 72.4% | RF §3 AC-6; EV E1/E6 | primary workflow/skill/template word graph and direct arithmetic | ❌ exact percentage; ✅ threshold — corrected Researcher reductions are 79.7%/79.5% and the corrected combined reduction is 71.8%, still above 30% |
| C3 | each P/R/E/V/C/A family has an output-changing deliberate mutant before rejection | TS AC-6; RF AC-6; semantic evidence | `source_mutant()`, `execute_scenario()`, family test, and direct reproduction | ❌ five families have no such proof and the shared family test produces no record in any family |
| C4 | evidence candidate and reviewed implementation are identical | EV §2/§5 (`7b871bf`) | `git diff 7b871bf..272a7cf -- <23 paths>` | ✅ empty diff |
| C5 | all canonical and installed/generated routes are equal and clean receivers contain 11 artifacts | RF AC-5; EV E4/E5 | primary files, hashes, integration tests, clean-receiver transcript | ✅ |
| C6 | Reviewer three-rung routing, REVISE transitions, acceptance authority, and hard stop “retain meaning” | TS/RF AC-4; EV E4 | mandatory workflow/convention clauses, semantic scenarios, and this review's own trace | ❌ — rung 1 has incompatible recipient and state instructions, and no semantic case tests that branch |

All RF, EV, HL §7.2, ONB §7, predecessor RF/REVIEW, and source-code references resolve to real repository artifacts. Numeric claims above were checked against Git objects, executable tests, or direct file-derived arithmetic rather than accepted from summaries.

## Discrepancies Found

1. **Incomplete candidate Researcher read graph (AC-1; AC-6).** `docs/scripts/test_runtime_context.py:682` excludes Gather, Extract, and Challenge templates whenever a workflow contract is present, while `.tfw/workflows/research/base.md` Step 5 requires those stage templates. This contradicts TS AC-1's complete edge-classification requirement and AC-6's prohibition on omitted mandatory inputs/symmetric exclusions. The 30% gate still passes after correction, but EV E1 and E6 and `runtime-context-primary-roles.txt` overstate graph completeness and publish undercounted candidate totals.
2. **Family mutants reject before changing produced output (AC-6).** `source_mutant()` mutates the probe used to locate a source clause, and `execute_scenario()` raises before record construction. The parametrized P/R/E/V/C/A test proves only anchor sensitivity, not the TS requirement that at least one deliberate mutant per family change produced output before independent comparison rejects it. EV E3 and `semantic-primary-roles.txt` therefore do not support the checked AC-6 claim.
3. **Reviewer rung routing has mutually exclusive active instructions (AC-4; frozen DoD 6/10 and DoF 3).** `.tfw/conventions.md:595–596` assigns rung 1 directly to execution with no state move and reserves `TS_DRAFT` for a rung-2 TS change; lines 897–900 explicitly say rung 1 needs no Coordinator. `.tfw/workflows/review.md:153,159` and `.tfw/conventions.md:936–939` instead require every REVISE to go through the Coordinator, a TS revision, and `TS_DRAFT`. Because the candidate read contract loads all of these sources at Decide, a Reviewer cannot derive one route. The existing V1–V4/C1 oracle has no rung-specific scenario and did not detect the conflict. The defect predates Phase B, but AC-4 expressly claims that this touched path's three-rung route, transitions, acceptance boundary, and hard stop retain meaning. A complete repair is **rung 2**: `.tfw/conventions.md` is absent from TS §4's 23-file surface and adding it would exceed the 23-file ceiling, so the Coordinator must revise the TS before aligning the shared authority, workflow/copies, and tests.

Discrepancies 1–2 are correctable within the approved TS. Discrepancy 3 requires a Coordinator-issued TS revision to expand the affected-file surface and budget; it does not require a frozen-HL amendment.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | `evidence/EV__phase-b__primary_role_paths.md` | ✅ | ❌ — references resolve, but E1/E3/E4/E6 repeat incomplete graph, mutant, or Reviewer-routing claims |
| E2 | `evidence/runtime-context-primary-roles.txt` | ✅ | ❌ — tests pass and baseline counts hold, but the candidate Researcher graph omits three required stage-template edges |
| E3 | `evidence/semantic-primary-roles.txt` | ✅ | ❌ — records match for ordinary cases, but the transcript establishes neither output-changing mutants for every family nor any rung-specific Reviewer route |
| E4 | `evidence/clean-receiver-primary-routes.txt` | ✅ | ✅ — four independent receivers each report 11 artifacts and correct routing |
| E5 | `evidence/verification-primary-roles.txt` | ✅ | ❌ — test/scope/hash portions hold, but its final acceptance depends on all three unsupported claims above |

## Knowledge Citations Verified

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | master HL §7.2 K1 | P0 · `.tfw/README.md` NS1 | ✅ | ✅ | ✅ — purposeful, inspectable continuation | ✅ — reductions must preserve decisions and routes |
| 2 | master HL §7.2 K2 | P0 · `.tfw/README.md` NS3 | ✅ | ✅ | ✅ — no maximum-documentation bureaucracy | ✅ — duplicate preload is a subtraction target |
| 3 | master HL §7.2 K3 | P1 · `.tfw/README.md` Methodology values | ✅ | ✅ | ✅ — structural enforcement, naming, portability | ✅ — gates, role terms, and local runtime remain observable |
| 4 | master HL §7.2 K4 | P2 · `knowledge/philosophy.md` F22/F40/F43/F45 | ✅ | ✅ | ✅ — minimal templates, naming, architecture, subtraction | ✅ — supports deletion and single ownership |
| 5 | master HL §7.2 K5 | P3 · `KNOWLEDGE.md` D23/D25/D61 | ✅ | ✅ | ✅ — template ownership, progressive disclosure, deleted ceremony | ✅ — directly precedes this context reduction |
| 6 | master HL §7.2 K6 | P3 · `KNOWLEDGE.md` D63/D68/D72 | ✅ | ✅ | ✅ — freeze, task-local state, citation bar | ✅ — protected semantics in all four paths |
| 7 | master HL §7.2 K7 | P4 · `.tfw/conventions.md` Design Rules/Anti-patterns | ✅ | ✅ | ✅ — dense algorithms, addressed reads, role locks | ✅ — constrains route design and tests |
| 8 | master HL §7.2 K8 | P5 · `knowledge/convention.md` F4/F8/F14 | ✅ | ✅ | ✅ — executable refs, one list owner, no template duplication | ✅ — matches the claimed consolidation |
| 9 | master HL §7.2 K9 | P6 · `knowledge/process.md` F3/F4/F22/F30 | ✅ | ✅ | ✅ — named checkpoints, algorithms, enforcement sites | ✅ — matches the primary-path rewrite |
| 10 | master HL §7.2 K10 | P7 · no additional applicable fact | N/A | ✅ | ✅ — relevance scan found only duplicative constraints | ✅ — no uncited task-specific constraint was found |
| 11 | ONB §7 #1 / K1 | P0 · NS1 | ✅ | ✅ | ✅ | ✅ — observable decisions/gates/routes retained |
| 12 | ONB §7 #2 / K2 | P0 · NS3 | ✅ | ✅ | ✅ | ✅ — duplicate prose/preload targeted |
| 13 | ONB §7 #3 / K3 | P1 · Methodology values | ✅ | ✅ | ✅ | ✅ — tests enforce routes and semantics |
| 14 | ONB §7 #4 / K4 | P2 · F22/F40/F43/F45 | ✅ | ✅ | ✅ | ✅ — minimal architecture-led subtraction |
| 15 | ONB §7 #5 / K5 | P3 · D23/D25/D61 | ✅ | ✅ | ✅ | ✅ — follows prior compression decisions |
| 16 | ONB §7 #6 / K6 | P3 · D63/D68/D72 | ✅ | ✅ | ✅ | ✅ — protected freeze/state/citation semantics |
| 17 | ONB §7 #7 / K7 | P4 · Design Rules/Anti-patterns | ✅ | ✅ | ✅ | ✅ — algorithmic workflows and structural locks |
| 18 | ONB §7 #8 / K8 | P5 · F4/F8/F14 | ✅ | ✅ | ✅ | ✅ — references and owned lists remain executable |
| 19 | ONB §7 #9 / K9 | P6 · F3/F4/F22/F30 | ✅ | ✅ | ✅ | ✅ — named checkpoints and enforcement sites |
| 20 | ONB §7 #10 / K10 | P7 · no additional domain/environment/risk constraint | N/A | ✅ | ✅ — scan found no additional non-duplicative constraint | ✅ — current phase requires no extra application |

Priority 5–7 relevance scan also considered constraint F2/F12, domain F2, environment F5, risk facts, and stakeholder F8. The applicable items duplicate already-cited attention, repository-authority, provider-independence, and known-diagnostic constraints; none changes the Phase B contract. `KNOWLEDGE.md` D72 supports the universal “round is now a TS revision” route and therefore exposes the same unresolved conflict with the convention rung-1 table/Role Lock recorded in V7; D73 remains consistent with the Phase A foundation. Knowledge reconciliation is not authorized while Phase B remains under REVISE.

## AC Verification Summary

| AC | Result | Independent basis |
|----|--------|-------------------|
| AC-1 | ❌ | exact baseline holds, but the candidate Researcher graph omits three mandatory reads |
| AC-2 | ✅ | Coordinator/Researcher algorithms, modes, gates, routing, and stops inspected; targeted semantics pass |
| AC-3 | ✅ | Executor acceptance, refusal, execution, evidence, RF, and stop semantics inspected and tested |
| AC-4 | ❌ | staged independence and Purpose/citation behavior hold, but rung-1 recipient/state semantics conflict across mandatory authorities and have no oracle case |
| AC-5 | ✅ | canonical/generated/installed parity, four clean receivers, idempotence, repair, and preservation verified |
| AC-6 | ❌ | thresholds/full gates/scope hold, but family output-changing mutants and no-omission proof do not |

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈N × ratio⌉ files and recorded findings? 23/23 implementation/test files verified after escalation.
- [x] Ran at least 1 build/test command (or documented why not)? Targeted and full suites plus both index checks run.
- [x] Claim & Source Checks filled — key claims spot-checked, every citation traced, and data checked against primary sources?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented? D72 routing conflict is recorded in V7 and Judge; D73 has none.
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Total: 20, resolved: 20 (two N/A link rows are explicit scan claims), semantically verified: 20, irrelevant: 0, hallucinated: 0
- [x] Evidence artifacts from RF §5 verified?
  - Total evidence items: 5, verified without qualification: 1, missing: 0; 4 exist but contain or inherit discrepant claims

Stage complete: YES
