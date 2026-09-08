# TS — TFW_20260907-133942_PTTC / Phase A: Proportionate repository verification

> **Date**: 2026-09-08
> **Author**: robert, phase Coordinator `01a08196-9e95-7ef3-8a4f-a5d6b4a424a9`
> **Status**: Approved by saubakirov on 2026-09-08; phase state remains TS_DRAFT until Executor onboarding
> **Parent HL**: [master](../HL-TFW_20260907-133942_PTTC.md), Phase A, A2 freeze `5c151d57f66df3ea321fe145170fe3db07c3eb6a`
> **Phase context**: [Phase HL](HL__phase-a__proportionate_repository_verification.md)
> **Authority**: [addressed continuation e18d](../journal/20260908-215755__dispatch__e18d.md), committed at `49ddad02f97dfb46919bdd19292902b9082d696f`
> **Approved requirement source**: `af52ef3ab6891031db8c411932879d76cfc1e6e6`, TS blob `b7ef498c4d911cf6fb4f8c810aef24913480f68d`; this update records approval metadata only

## 1. Objective

Deliver four results: a source/Git test family without a website-build dependency; removal of obsolete bodies and duplicate wrappers; knowledge protection that allows harmless explanations and approved successors; and usable check-selection/evidence-reuse guidance in the existing maintainer README. The maintainer spends less effort on irrelevant verification while real source, provenance and generated-output defects remain detectable.

## 2. Scope

### In Scope

- Split the existing integration module by actual direct/helper/global inputs, decorators and import-time effects. Keep one module-scoped build for generated-output and unresolved consumers. Move proved pure predicates and their needed helpers/constants as one coherent family.
- Remove seven statically shadowed definitions and two thin historical aliases identified below; preserve the latest effective protection. Rework the current knowledge predicate, retaining distinct immutable historical regression evidence.
- Repair the two live source-target references affected by the move, and update upstream maintainer guidance with risk-based selection, broad-risk triggers and claim-specific evidence applicability.
- Establish a same-environment local cost comparison, zero MkDocs starts for the knowledge selection, absent/stale-output protection, meaningful negative cases, one genuine integration defect and a bounded native example of check-selection permission/reuse. Independently review the result and evidence; return the reviewed result for checked local landing and Phase B planning.

### Out of Scope

Phase B closure/capture/terminal-repair changes and synthetic receiver; new research or tasks beyond the approved Executor/Reviewer pair; code changes to `gen_docs.py`, `tfw_state.py`, `tools/tests/` or container behavior; product knowledge edits; release/version/publication; changes to any project configuration, particularly `.tfw/templates/project_config.yaml`; canonical workflow/adapter permission changes; a global runner, cache, evidence passport, registry or status aggregate. Controlled adverse evidence uses isolated disposable inputs, never shared product files.

## 3. Principles Check

| # | Master HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P1 | Saint-Exupery | AC-1/2/3/4 | Explain what disappears and its surviving protective consequence; reject needless machinery |
| P2 | Consequence and risk first | AC-1/3/4/5 | Distinguish structural, semantic and generated-output claims; no diff-size shortcut |
| P3 | Existing evidence is an input | AC-4/5 | Independent applicability judgment; changed oracle invalidates its prior result |
| P4 | Final state follows final effects | AC-5 | Bind observations to actual Candidate; later VALUE requires replacement; closure-rule change belongs to B |
| P5 | One owner per rule | AC-4; §9 | Maintainer commands stay in this repository; no portable workflow or SLC ownership change |
| P6 | Cost includes attention | AC-5 | Separate process/setup/body/review observations; unknown tokens/money remain unknown |
| P7 | Prospective bounds | §4; AC-5 | Pre-act cost check; preserve partial failures and stop instead of declaring success |
| P8 | No unapproved publication | §4; AC-5 | Local commits and parent return only; separate final owner approval for publication |

## 4. Affected Files and Value-Bearing Accounting

Paths below are repository-relative. Whole-path classification follows accepted-output precedence: these tests are themselves the accepted assurance product, so calling their folder ASSURANCE would incorrectly exclude the main delivery. No line subtraction is authorized.

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `docs/scripts/test_integration.py` | MODIFY | VALUE | Output family, shared build and removal/transfer of pure definitions |
| `docs/scripts/test_repository_contracts.py` | CREATE | VALUE | Accepted source/Git/temp-tree family, retained negative protection and reworked knowledge contract |
| `docs/scripts/test_runtime_context.py` | MODIFY | VALUE | Necessary current-source target updates in `LEDGER_SPECS` R10/R14 only |
| `tools/README.md` | MODIFY | VALUE | Existing upstream maintainer guidance becomes a usable verification selection/reuse route |
| This phase's named HL, TS, status, journal, ONB, RF, REVIEW, review stage files and `evidence/EV__phase-a__proportionate_repository_verification.md` | Role-owned CREATE/MODIFY | TRACE | Planning, authority, reported observations and acceptance records; no delivery budget exclusion for product hidden here |
| Disposable command logs, input variants and `site/` used by the evidence program | CREATE temporarily | TRACE / DERIVED | Inspectable experiment receipts or reproducible website output; not separately accepted products |

### Prospective accounting contract

| Fact | Owner-approved value |
|---|---|
| Subject / exact VALUE selector | The four literal VALUE paths in the table; whole Baseline→Candidate differences, including test additions/removals |
| Baseline / selector source | `099d37d21ddfada2ca72c576055f0a26029c7205`; selector is the exact TS approved from `af52ef3ab6891031db8c411932879d76cfc1e6e6`, blob `b7ef498c4d911cf6fb4f8c810aef24913480f68d`. Immutable owner approval receipt: `49ddad02f97dfb46919bdd19292902b9082d696f`; receipt/control intake does not move the source Baseline |
| Candidate rule | First tested immutable Executor commit containing required VALUE+ASSURANCE, before EV/RF/REVIEW/final transition. A later TRACE/DERIVED-only commit does not move it. Later VALUE requires a replacement Candidate and recomputation; keep original and replacement evidence provenance |
| Logical VALUE files | Planned **4**; count a detected rename once |
| Touched text LOC | Forecast **3,300 additions + 3,100 deletions = 6,400**; this is an unmeasured planning denominator, mainly the module split. Actual measure is numeric numstat additions + deletions; binary/non-text per-file N/A |
| Triggers | Project config: 50 files / 5,000 LOC. The forecast crosses the soft LOC prompt, not the file prompt. The owner approved the disposition below at the initial TS approval epoch |
| Multiplier / authority | Configured 2 against the immutable owner plan: owner rules before work forecast at/above **8 files or 12,800 LOC**, or growth from a planned-zero measure. Below those boundaries, Coordinator additions require the canonical necessary-constituent conditions and a prospective ruling; no denominator ratchet |
| Approval epoch / failures | Initial owner approval of this exact TS and its four-path/6,400-LOC denominator is recorded at `49ddad02f97dfb46919bdd19292902b9082d696f`, before Executor work. Missing, mutable, mismatched or late authority is BLOCKED; metric-only inapplicability is N/A; unresolved phase attribution is INVALID; DEFERRED is not terminal |

Reproduce the two measures with the four literal VALUE paths, the Baseline above and the actual Candidate SHA using `git diff --name-status --find-renames=50% -z` and `git diff --numstat --find-renames=50% -z`. Record the resolved commands/results in one EV accounting row; RF binds the result/deviations and Reviewer reproduces it without supplying authority.

### Prospective scope ruling proposed to the owner

**APPROVED — saubakirov, 2026-09-08, receipt `49ddad02f97dfb46919bdd19292902b9082d696f`:** keep the split and its two reference repairs in one phase despite the 5,000-LOC soft prompt. The cause is moving roughly 2,800 lines between two ordinary files, counted on both sides of the diff. Splitting this dependency change into separate delivery phases would leave an incomplete boundary or duplicate setup and require another handoff/review. The four-file scope, retained predicates, one final broad run and independent source/evidence review provide assurance. This is not a hard LOC limit or a quality exemption. The phase Coordinator originated this proposal; root recommended it; the human owner ruled before work.

For planning only, approximately 5,600 touched LOC represent the unchanged transfer; approximately 800 cover removals, the deliberate knowledge-oracle change, necessary import/guard/reference adjustments and maintainer guidance. These are rough explanatory components estimated before implementation, not separately enforceable budgets or measured line subtraction. The actual whole-path numstat total is authoritative. The 91 non-output functions are classification candidates, not a relocation quota. A plain move preserves each effective predicate; AC-2 removals and AC-3 oracle rework are distinct intentional semantic changes and must be identified as such in RF.

### Task-local hard constraints

| M1 consequence | M2 protected object/risk | M3 direct measure / selector | M4 pre-act enforcement | M5 softer-control insufficiency | M6 change authority |
|---|---|---|---|---|---|
| Another unbounded verification campaign consumes time without establishing the result | Phase A verification from first baseline probe through review and local landing, including failed and repeated attempts | Cumulative **60 minutes** command wall time; **10 pytest processes**; **4 actual MkDocs starts**; all counts include nested/repeated invocations. Three builds are planned and one is contingency, not a target | Before each invocation, record spent/remaining amount and next command's upper bound; stop if it cannot fit. Individual full-suite invocation at most 20 min, individual other build invocation at most 15 min, always within remaining aggregate time | Reporting after an expensive run cannot recover the spend; a failed/partial run must not be silently repeated | saubakirov prospectively through root for a larger/different experiment; Coordinator may select/reuse adequate observations inside the unchanged bound |
| Concurrent mutation damages an independently owned change or bypasses owner approval | Four VALUE paths, SLC behavior, user configuration, native role/authority and publication boundary | Exact staged paths and diff; owner TS approval reference; root overlap clearance; one assigned Executor and independent Reviewer | Re-resolve addressed dispatch/approval and shared paths before product writes; inspect exact commit/landing set | Review after conflicting writes or publication cannot restore the absent authority | Owner for reserved changes; root for coordination inside the mandate; phase Coordinator for ordinary in-bound routing |

**Actions, not budget dimensions:** VALUE = one CREATE and three MODIFY; no additional ASSURANCE product file is planned. **Immutable owner-approved denominator:** four VALUE files and 6,400 touched text LOC, fixed by receipt `49ddad02f97dfb46919bdd19292902b9082d696f`.

## 5. Acceptance Criteria

### AC-1: Pure checks have no website dependency

- [ ] `test_integration.py` retains its output checks and one shared module-scoped build. The new pure module imports no build-backed test module and neither reads generated output nor starts MkDocs, including through helpers.
- [ ] Every effective baseline test and reachable helper/global input, decorator and import-time effect has an inspectable MOVE/KEEP/REWORK/REMOVE disposition in the existing RF/EV. Static classification alone is not called proof. Unresolved/output consumers retain build setup; there is no target number to move.
- [ ] The baseline 15 direct output consumers remain: `test_static_pages_generated`, `test_knowledge_index_generated`, `test_task_pages_generated`, `test_knowledge_topic_pages_generated`, `test_workflow_pages_generated`, `test_template_pages_generated`, `test_frontmatter_in_generated_pages`, `test_decision_refs_resolved_in_knowledge_index`, `test_artifact_refs_resolved_in_knowledge_topics`, `test_td_refs_resolved_in_output`, `test_no_page_renders_its_own_frontmatter_as_body_text`, `test_index_override_used`, `test_section_index_pages_generated`, `test_every_recognized_task_has_an_unlisted_landing_and_nav_has_no_tasks_entry`, `test_resolved_links_use_directory_urls`.
- [ ] The pure family passes in isolated absent-output and stale-output conditions. The selected knowledge check starts zero MkDocs processes. The output family rebuilds before accepting output, including when valid old output exists.
- [ ] R10/R14 in the current-source deletion ledger resolve the same two retained predicates at their new path. Historical Git selectors and named package paths retain their historical meaning.

Gate: static direct/helper dependency and active-definition mapping; candidate pure selection with absent/stale `site/`; retained ledger test `test_round1_r03_r14_ledger_resolves_real_targets`; ordinary output selection. Parametrized case counts are observations, never quotas.

Evidence: minimal real-environment command logs at the exact candidate, with actual process/build-start observations and `site/` preconditions, plus independent Reviewer inspection. The final full-suite and adverse-output observations in AC-5 may satisfy the output portions here; no duplicate build per criterion.

### AC-2: Obsolete duplicates leave without losing protection [depends: AC-1]

- [ ] Remove the seven earlier shadowed bodies at baseline ranges 1026–1033, 1036–1048, 2113–2142, 2191–2199, 2202–2214, 2217–2230 and 2233–2244; preserve each latest substantive definition. These ranges identify source at the Baseline, not future line numbers.
- [ ] Remove the two thin aliases `test_phase_d_claude_release_config_history_and_prior_phases_are_byte_exact` and `test_phase_d_added_product_lines_do_not_leak_provider_names_or_apis`. Preserve their already-collected unique targets `test_phase_d_approval_epoch_protects_history_inputs_and_cumulative_prefixes` and `test_phase_d_added_product_provider_terms_are_confined_to_adapter_and_named_exception`. No current caller was found in the bounded source search; a newly evidenced consumer returns for a decision rather than silently acquiring a compatibility wrapper.
- [ ] Preserve the narrow board-parser regression guard, including its meaningful source population and self-exclusion after movement. Preserve controlled doctor behavior, adapter parity, package replay and adverse checks; do not restore the already removed global doctor-clean gate.

Gate: baseline/effective-definition comparison and retained targeted tests in the candidate pure/full runs. Deleting a function is justified by lost duplication or supersession, not by a lower test count.

Evidence: minimal RF/EV mapping from each removed body/alias to surviving predicate and immutable history. Reviewer independently checks the mapping and a meaningful retained negative case; the same observation may support AC-1/3/5.

### AC-3: Knowledge protection permits legitimate evolution [depends: AC-1]

- [ ] Historical pre/post-K2 claims remain checked against their actual immutable inputs: `b5a45c622c035c574d0fd5f5f7795add769be529`, `29df734a4ab12a4f4a796a0577389cef2e73bcac`, `7b4d4190c06a6ca02d55e23f90ed24214df8d2b5`, and existing Phase D/E anchors. Whole-row equality may establish that finite historical identity; it cannot be the current knowledge oracle.
- [ ] Current structural checks retain decision identity/cardinality, relevant task/phase lineage, required real immutable references, current/superseded relations and material attribution. D82 is the ordinary-Full/tooling boundary; D83 is the final owner AT choice; D84 is optional acting-principal `writer` attribution. Old Phase D capture is historical, not a competing current D82 decision.
- [ ] A wording-only D82/D83/D84 explanation preserving protected facts is accepted. A bounded successor fixture re-expresses the already owner-approved initial-to-final CRATM Phase D authority transition, with explicit predecessor/successor relation and its actual frozen/ruling references; adding later decisions does not itself fail. Label the fixture as synthetic: it illustrates an existing owner act and grants no new approval or live knowledge change.
- [ ] Missing/duplicate decision or selected artifact rows, incompatible phase lineage, fabricated/wrong immutable sources and principal-versus-unit/authority distortion remain rejected by the relevant structural check or independent semantic review. Keep the existing meaningful negative consequences; remove redundant full-row mutants only when their consequence has an adequate remaining check.
- [ ] State explicitly which claims the executable check establishes and which require semantic judgment. Unrecognized semantic change is not automatic approval. No universal meaning validator, mandatory phrase roster, new approval registry or editable product knowledge is introduced.

Gate: one bounded knowledge case group covering current and pinned historical inputs, harmless wording, a clearly labeled synthetic approved successor, and the named adverse consequences. Assertions must observe the relevant consequence rather than mirror the implementation's chosen spelling.

Evidence: zero-build run on actual repository knowledge; exact input variants in EV attachments; independent Reviewer judgment of harmless wording, successor evidence and material distortion, with the governing claim and reason. Synthetic examples are not native owner acts or proof of universal semantic equivalence.

### AC-4: The maintainer can select and reuse adequate verification [depends: AC-1, AC-3]

- [ ] `tools/README.md` gives one concise change→risk→selection→evidence route for text, parser, instruction/adapter, docs/knowledge, lifecycle and release-input changes. It names existing commands and explains when output/build or broad integration evidence is required. A small diff is not an exemption.
- [ ] Reuse records the claim, relevant inputs, oracle/authority, environment and exact evidence identity in existing EV/RF. An unrelated TODO/trace change alone does not invalidate other claims; changing relevant input, fixture, expected result or authority invalidates the affected result. No enclosing-commit-only expiration or automatic universal reuse.
- [ ] Configured build/lint/test gates and workflow authority remain in force. Selection guidance cannot silently waive them. Receiver projects retain their own check commands; no upstream environment is exported.
- [ ] One bounded native exercise in the same future Executor/Reviewer tasks observes how the changed maintainer selection guidance is applied: classify an unrelated TODO, a wording-only knowledge change and an altered oracle/permission input; identify applicable old evidence and the exact affected check or return. The Reviewer forms an independent judgment before reading the Executor's proposed decisions. The observed choices, not merely matching prose, establish this limited behavioral result.

Gate: independent reading of the guide and its concrete commands against actual module/dependency boundaries. The oracle-change example must reject reuse for the affected claim while retaining unrelated applicable evidence.

Evidence: existing native message addresses plus a short EV account of actual choices and independent challenge. Use one case batch per holder inside ordinary handoff/review, with no extra agent, session, role or behavior interpreter. No reliability or cross-provider claim follows. This exercise tests maintainer check-selection permission; canonical closure permission and the synthetic receiver remain Phase B.

### AC-5: Local benefit and retained integration protection are observed [depends: AC-1, AC-2, AC-3, AC-4]

- [ ] Compare the unchanged `test_the_control_character_scanner_actually_detects_one` and its helper/constants at Baseline and Candidate, in separate single-selection pytest invocations with the same interpreter, installed versions, OS, environment variables, parameters and fixture inputs. Confirm the oracle/helper bodies are unchanged before claiming a paired result. Both isolated comparison roots use the same non-VALUE source corpus from the Baseline; the candidate-side composition changes only the four VALUE paths to their exact Candidate blobs. Record composition and blob identities, keep unrelated phase/SLC/trace changes out of the comparison, and disclose that this controlled composition is separate from the full-suite observation on the actual Candidate. Use absent `site/` on both sides. Separately establish the knowledge selection's zero-build property under AC-3; do not mislabel a changed knowledge oracle as a controlled timing comparison.
- [ ] Record process wall time, pytest setup/call/teardown where observable, MkDocs process count and elapsed time, selected input/oracle identities, repeated processes and actual review effort. Distinguish summed durations from incident elapsed time. The candidate removes the representative test's MkDocs start and has lower comparable total time; report the observed absolute difference and its one-pair/local limitations, without a promised universal speedup. If noise or environment differences prevent that conclusion, report insufficient evidence.
- [ ] Run configured collection and the full `python -m pytest tools/tests/ docs/scripts/ -q` once on the final Candidate because the shared module split and live target movement span multiple test surfaces. Preserve outcomes, warnings and actual nonempty collection. Full-suite inclusion supplies meaningful existing controlled negative checks; do not add a duplicate guard for every research comment.
- [ ] One isolated real rendering defect is detected through the ordinary output test/build path: start with valid stale output from the candidate suite, apply a minimal input/generator variation causing frontmatter to render as body text, and require a fresh build plus failure of the existing frontmatter-leak check. A missing executable or deliberately failing pytest assertion is not this observation. Preserve normal and adverse artifacts and undo only disposable input changes.
- [ ] Independently inspect the Candidate, four-path accounting, applicability and adverse result. Use a targeted rerun for an unresolved claim, not a second full suite by default. If local landing preserves every claim-relevant byte/environment and exact Candidate reachability, inspect that crossing and reuse applicable evidence; changed relevant inputs need affected revalidation within the remaining budget. Report reviewed, landed and published as separate states.

Gate: immutable Candidate, configured collection/full suite and accounting; compare unchanged benchmark subjects; require actual expected adverse failure. Required missing evidence is BLOCKED/DEFERRED with its reason, never PASS because a count or deadline was reached.

Evidence: one existing EV file with per-AC rows, dependency/disposition and accounting summaries, and raw command/variant attachments. RF points to EV. Earlier CRATM/CRUE durations remain attributed context and are not substituted for the paired run. No tests/builds/probes have been executed during this TS preparation.

### Evidence program and cost

| Observation group | Minimal planned execution | Shared use |
|---|---|---|
| Controlled cost pair | Baseline unchanged text test, then Candidate same test: two pytest processes, one baseline build | AC-1/5; same oracle and environment isolate setup dependence |
| Candidate pure family | Absent output, then stale output: two processes, zero builds; include knowledge variants and ledger target check in the same selections where possible | AC-1/2/3; no separate process for every assertion |
| Final candidate coherence | Configured collection and one full suite: two processes, one shared output build | AC-1/2/3/5 plus existing parser, adapter, release and controlled doctor protection |
| Stale-output rendering defect | One ordinary selected output run, one fresh build, expected failure | AC-1/5; stale-data and genuine integration consequence in one observation |
| Independent targeted uncertainty | At most one planned targeted pure selection; no automatic full repeat | Reviewer AC-2/3/4/5 challenge |

Eight pytest processes and three builds are planned at most; adequate observations may be shared further. The total ceiling is ten processes, four build starts and 60 minutes cumulative command wall time, including corrections and landing checks. The two extra processes/one build are contingency inside the same allowance. Forecast **20–35 minutes** is rough, informed by historical 320.86-second single-selection and 715.86-second full-run reports with different scopes/environments; it is neither a benchmark nor a guaranteed finish time. Native case-batch and review effort are recorded separately when observable; token/monetary totals and agent labor duration are not known. The command cap does not pretend to cap total agent work or total task elapsed time.

No automatic repeat is allowed merely to improve a time statistic. Before any next invocation, estimate its fit against the remaining allowance. Failure to collect all required observations inside the approved program ends further spend and returns partial evidence plus a concrete proposal to root; it does not remove an AC, create another research round, or authorize an expanded campaign.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-a__proportionate_repository_verification.md` | Executor-created environment, per-AC results, applicability, one accounting row and attachments index |
| `evidence/phase-a-verification.txt` | Commands, immutable identities, raw outcomes and timing/process observations in execution order |
| `evidence/phase-a-input-variants.md` | Exact disposable knowledge/rendering changes and normal/adverse artifact references; includes direct native case-batch references |

Additional raw attachments are justified only by an observation above; their names and identities go in EV. Evidence exists when observed, not prefilled by the Coordinator.

## 6. Technical Guidance

- Preserve existing module-level helper structure where it serves the input family. One new ordinary test file is sufficient for the planned split; an autouse fixture shared from `conftest.py` would recreate the coupling.
- Board-guard exclusion must follow the file that contains the guard; do not blanket-exclude generators or remove its protective consequence.
- Preserve known historical constants/path selectors as historical objects; only the two live ledger targets migrate. The real named functions, not folder labels, determine disposition.
- Retain historical literal regression tests as bounded history checks; separate current structural facts from semantic acceptance. The Executor may choose a simpler adequate implementation and explain it in RF within this TS.
- Existing pytest duration output plus observed child processes is sufficient measurement context. A disposable observation aid may record raw events, but cannot become a shipped runner or self-authored agent-compliance evaluator.

## 7. Definition of Failure

Master DoF remains governing. Reject loss of a necessary predicate for green results; a pure family that imports/reads output through helpers; stale-output false green; current whole-row/prose locking; inferred or fabricated approval/source identity; changed-oracle evidence reuse; omission of required observations for cost; synthetic or phrase checks represented as native reliability; unapproved VALUE paths, SLC behavior/config edits, publication or extra role tasks. A failed required observation returns through the existing responsible role and authority; preserve its evidence.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Indirect output input or accidental collection loss | Direct/helper inventory, absent/stale cases, nonempty final collection and independent comparison |
| Platform/environment drift contaminates timing | Same machine/interpreter/env/inputs; one-pair limitation; no claimed saving if comparability fails |
| A synthetic successor masks real authority drift | Explicit fixture label, real immutable source attachment, independent semantic disposition; never promote a fixture to owner authority |
| The whole-file move crosses the soft LOC prompt | Four-path VALUE accounting and prospective owner decision, without line subtraction or artificial renames |
| Shared-file or late landing change invalidates evidence | Root overlap clearance, exact Candidate/landed diff and claim-specific revalidation |

## 9. Cross-Phase and Parallel Modifications

| Surface | Other owner / phase | Coordination note |
|---|---|---|
| `docs/scripts/test_integration.py`, all-recognized-task landing test | SLC | PTTC retains this output predicate's behavior; root agrees file sequencing before edits |
| `docs/scripts/test_runtime_context.py`, R10/R14 source targets | SLC candidate shared file | PTTC changes only the two live target paths; preserve parser/container behavior and historical source observations |
| `tools/tests/`, `tools/tfw_state.py`, `docs/scripts/gen_docs.py` | SLC candidate surfaces | No product edits in this TS. Temporary isolated adverse rendering inputs supply evidence only |
| `tools/README.md` | B may consume A's result | A owns maintainer verification guidance. B plans from reviewed RF/deviations, not this proposed outcome |
| Full closing/review/knowledge instructions and synthetic receiver | Phase B | Remain B's deliverables; A provides reviewed evidence applicability and selection results |

Root relayed SLC's direct confirmation during planning: no new functional overlap in these four VALUE paths, no SLC implementation yet, and R10/R14 do not touch its container/config extraction. The landing test remains output-backed; `task_containers` and `iter_task_dirs` stay unchanged. If PTTC lands first, root supplies the resulting SHA and new function/helper addresses to SLC. Root retains coordination of any later overlap; at continuation e18d, no second active PTTC implementation team is evidenced. Publication and Phase B execution remain separately owner-reserved. Next act under owner-approved TS and continuation e18d: create and verify the one Executor and independent Reviewer, record actual addresses/parents and phase-local dispatches, then route `/tfw-handoff` and subsequent `/tfw-review` to those holders.
