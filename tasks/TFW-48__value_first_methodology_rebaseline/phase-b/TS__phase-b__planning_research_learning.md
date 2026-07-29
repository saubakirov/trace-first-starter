# TS — TFW-48 / Phase B: Planning, Comparative Research, and Learning Routing

> **Date**: 2026-07-29
> **Author**: Coordinator (Codex)
> **Status**: ✅ TS — Approved for execution on 2026-07-29
> **Parent HL**: [Phase B HL](HL__phase-b__planning_research_learning.md)
> **Master HL**: [HL-TFW-48](../HL-TFW-48__value_first_methodology_rebaseline.md)
> **Predecessor RF**: [Phase A RF](../phase-a/RF__phase-a__method_kernel.md)

---

## 1. Objective

Make planning, comparative research, and selected learning signals consume the
value-first Method Kernel established in Phase A. Phase B must preserve product purpose,
applicable Project Values, uncertainty, and human insight through to decision and TS;
scope the current research sequence as one comparative procedure; remove unsupported
activity counts from completion authority; and give every selected learning signal a
disposition-typed receipt—without changing configuration values, adding a cognitive
strategy system, or modifying downstream execution/review/knowledge consumers.

## 2. Scope

### In Scope

- Refactor planning instructions around purpose, uncertainty, applicable Project Values, and decision quality.
- Add a visible planning implication and TS disposition to Strategic Insights.
- Add a Pre-TS trace gate without imposing one-insight-one-AC ceremony.
- Name and scope Briefing → Gather → Extract → Challenge as the **Comparative Decision Procedure**.
- Add a procedure-fit gate that may reject this procedure and return to the Coordinator.
- Define `focused/deep` as qualitative research intensity only.
- Replace activity-count completion with evidence-, decision-, gap-, exclusion-, and saturation-based stop conditions.
- Give every current research number or hard-looking template count a retain, retire, or transitional disposition.
- Confirm `max_passes` as unconsumed and remove `min_iterations` as a universal hard closure floor.
- Preserve one complete filesystem-traced procedure and triggered additional iterations.
- Add compact disposition-typed Learning Receipts to existing research checkpoints.
- Restrict Fact Candidates to qualifying promotion/merge/derive signals while keeping other dispositions local to stage traces.
- Preserve the H4/T0 boundary.
- Reconcile terms, owners, links, and generated documentation across all affected consumers.

### Out of Scope

- Changes to `.tfw/project_config.yaml`, its template, Config Sync Registry, or exact numeric values.
- Deleting transitional config keys or calibrating replacement thresholds.
- New inquiry methods for search, immersion, diagnosis, case study, Yin-style review, or documentation mapping.
- Cognitive strategy selector, catalog, registry, runtime selection, prompt library, or project-extension contract.
- H4 comparison execution, fresh tasks, forks, models, scorers, pilots, or owner-package authorization.
- TS/RF/evidence execution contracts owned by Phase C.
- Review, docs, knowledge workflow, topic-file, Fact Candidate promotion, or retirement consumers owned by Phase D.
- Init/resume/config/update/release and registered-extension lifecycle owned by Phase E.
- Adapter synchronization, migration, versioning, changelog, and production regression suite owned by Phase F.
- Historical edits to TFW-44 or TFW-48 research traces.
- Fixes for TD-125 or TD-126.

## 3. Principles Check

| # | Principle (from Phase HL §7) | Enforced by | Gate |
|---|------------------------------|-------------|------|
| P1 | Purpose Before Procedure | AC-2, AC-3 | Planning and procedure-fit examples begin with a decision-changing uncertainty |
| P2 | One Operational Method, Honest Scope | AC-3 | One canonical term, bounded applicability, and mismatch exit |
| P3 | Intensity Is Not Method | AC-4 | Focused/deep definitions change breadth/depth only |
| P4 | Meaning Before Number | AC-5 | Complete numeric ledger with consumer and authority disposition |
| P5 | Completion Is a Claim | AC-5 | Stage/iteration closure scenario matrix uses evidence and explicit gaps |
| P6 | Learning Is Selected and Routed | AC-6, AC-7 | Event trigger plus disposition-typed receipts and non-central dispositions |
| P7 | Existing Surfaces Before New Sections | AC-2, AC-6, AC-7 | No new top-level capture section or framework file |
| P8 | Precision Compresses Context | AC-1, AC-3, AC-9 | Single owners and point-of-use references; no duplicate definitions |
| P9 | Reality Can Overrule the Plan | AC-5, AC-6 | Counter-evidence and contradictory-signal paths can reopen or change a decision |
| P10 | Human Authority Remains Visible | AC-3, AC-5 | Procedure mismatch and iteration closure return to Coordinator/user |
| P11 | Domain-Agnostic by Design | AC-2, AC-3, AC-6 | Software and non-code scenario checks |
| P12 | Method Claims Need Evidence | AC-8 | H4/T0 scan and prohibited-architecture check |

## 4. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `.tfw/conventions.md` | MODIFY | Map planning/research consumers to the Method Kernel; define comparative procedure, research stop conditions, learning receipts, and Phase B numeric dispositions |
| `.tfw/glossary.md` | MODIFY | Define Comparative Decision Procedure and research intensity without duplicating operational contracts |
| `.tfw/workflows/plan.md` | MODIFY | Purpose/uncertainty framing, insight disposition, comparative-fit decision, triggered iteration gate, and Pre-TS trace check |
| `.tfw/workflows/research/base.md` | MODIFY | Procedure applicability, intensity semantics, evidence-based stage loop, learning receipts, triggered iteration synthesis, and nonnumeric limits contract |
| `.tfw/workflows/research/focused.md` | MODIFY | Express focused intensity through bounded uncertainty/evidence scope rather than counts |
| `.tfw/workflows/research/deep.md` | MODIFY | Express deep intensity through evidence diversity, counter-evidence, and edge cases rather than counts |
| `.tfw/templates/HL.md` | MODIFY | Add planning implication and TS disposition to Strategic Insights guidance/table |
| `.tfw/templates/RES.md` | MODIFY | Route stage receipts, constrain Fact Candidates to promotion candidates, and trace human insights to HL updates |
| `.tfw/templates/research/1_briefing.md` | MODIFY | Add comparative-procedure fit and remove arbitrary plan/question counts |
| `.tfw/templates/research/2_gather.md` | MODIFY | Use material alternatives/coverage rather than fixed dimension/alternative counts; add compact learning receipt |
| `.tfw/templates/research/3_extract.md` | MODIFY | Preserve cross-stage structure without configuration-count quotas; add compact learning receipt |
| `.tfw/templates/research/4_challenge.md` | MODIFY | Preserve pairwise/counter-evidence challenge and add compact learning receipt without count completion |

**Budget:** 0 new framework files, 12 modified framework files, estimated 500–900
changed lines. Planning and execution traces are excluded from the framework-file
budget. The phase stays within 14 files, 8 new files, 1,200 LOC, and 12 modified files.
These are planning triggers under the current transitional policy, not success targets.

## 5. Acceptance Criteria

### AC-1: Phase A contracts become observable consumers

Planning and research reference the Phase A semantic owners and show how their gates
protect the Method Kernel without redefining it.

- [ ] Purpose/Project Values, authority, evidence precedence, independent judgment, and selected learning disposition remain visible across planning and research.
- [ ] Rule Deployment determines which instructions remain complete locally and which use a canonical reference plus point-of-use gate.
- [ ] Comparative Decision Procedure and research intensity have one concise glossary definition and one operational owner in conventions/workflows.
- [ ] Research labels `K3`, `M5`, `R9`, `V1`, and Iteration dimension codes do not enter runtime/public text.
- [ ] Current consumer status is updated from “Phase A transitional” to the actual Phase B mapping without implying Phases C–F are implemented.

Gate: Ownership/consumer matrix in RF maps each Phase B concept to definition owner,
operational owner, point-of-use gate, and protected consequence; targeted `rg` scan
finds no runtime research codes or competing definitions.

Evidence: N/A — source ownership and consumer mapping are statically verifiable.

### AC-2: Purpose-led planning and insight-to-TS traceability  [depends: AC-1]

Planning begins with product purpose, applicable Project Values, decision-changing
uncertainty, and material human insight; it records what each insight changes.

- [ ] Plan context loading/understanding explicitly separates product purpose, uncertainty, evidence need, and solution proposal.
- [ ] HL Strategic Insights record the human insight, planning implication, source, and TS disposition/destination.
- [ ] Valid dispositions include AC, scope, technical guidance, Definition of Failure, decision/research direction, explicit task-local/non-use reason, or a resolvable downstream destination.
- [ ] The Pre-TS Gate verifies every material insight has a disposition without forcing every insight into a separate AC.
- [ ] The existing Project Values citation cascade remains intact and is not duplicated.
- [ ] TFW-44's insight-to-outcome gap is superseded through current planning surfaces; its historical trace remains unchanged.

Gate: Trace four examples—explicit requirement, governing value, rejected suggestion,
and future research direction—from HL insight through a valid TS/non-use disposition;
no new artifact or top-level capture section is required.

Evidence: N/A — the planning contract is verified from source and filled-template examples.

### AC-3: Comparative Decision Procedure is named and bounded  [depends: AC-1]

The current four-stage sequence is one operational method for evidence-backed
comparison/configuration decisions, not a universal definition of research.

- [ ] `Comparative Decision Procedure` has one concise, domain-agnostic definition.
- [ ] Briefing states the decision, material alternatives/configuration question, and what result would change the approach.
- [ ] Procedure fit is an explicit gate before stage execution.
- [ ] A mismatch returns to Coordinator/user with the unresolved information need and does not automatically select or simulate another method.
- [ ] Gather → Extract → Challenge retains its cross-stage natural dependency when the procedure fits.
- [ ] Software, product/content, and operational decision examples all fit without code-default language.
- [ ] Lookup, corpus immersion, documentation mapping, and open exploration are explicitly non-universal cases without new substitute architecture.

Gate: Scenario matrix covers comparative product choice, cross-source content choice,
routine operational policy choice, direct lookup, documentation immersion, and open
exploration; each receives fit/mismatch plus authority outcome.

Evidence: N/A — procedure applicability is a source-level contract; alternative methods are not implemented.

### AC-4: Focused and deep remain intensity controls  [depends: AC-3]

Focused/deep change evidence breadth, challenge depth, and uncertainty tolerance without
changing the procedure, selecting a strategy, or serving as completion proof.

- [ ] `focused` describes a bounded decision and deliberately narrow evidence/countercheck scope.
- [ ] `deep` describes independent evidence families, active counter-evidence, edge/failure cases, and explicit unresolved uncertainty.
- [ ] Neither intensity requires a fixed loop, decision, turn, hypothesis, source, or file count.
- [ ] Intensity selection names why additional breadth/depth changes risk or decision quality.
- [ ] A completed count cannot make an insufficient stage pass; an exceeded former count cannot make sufficient research fail.
- [ ] Existing file names and config keys remain transitional; Phase B does not rename or delete them.

Gate: Same comparative case is written under focused and deep intensity; outputs differ
in evidence/challenge obligations but use the same stages and closure authority.

Evidence: N/A — mode behavior is verified through source scenarios.

### AC-5: Numeric authority and stop conditions are honest  [depends: AC-3]

Every active or hard-looking research number receives an explicit lifecycle disposition,
and completion follows supported decisions or explicit gaps.

- [ ] The ledger covers web queries, project files, questions per turn, `max_passes`, `min_iterations`, `loops_per_stage`, fixed decisions/turns, plan bullets/questions, dimensions, alternatives, and configuration sampling counts.
- [ ] Unvalidated counts lose universal normativity and are not silently replaced by larger or hidden numbers.
- [ ] Config keys left for Phase E are labeled transitional/unconsumed where applicable.
- [ ] One complete iteration still requires filesystem-traced Briefing, Gather, Extract, Challenge, and RES.
- [ ] Additional iterations require a named trigger: error correction, unresolved material gap/hypothesis, counter-evidence need, changed decision, or user-injected direction.
- [ ] Stage closure covers declared corpus/source families, exclusions, counter-evidence, decision effect, saturation/no-new-disposition, unresolved gaps, and authority.
- [ ] Reaching a stop condition may produce “insufficient/unresolved” rather than a false conclusion.

Gate: Numeric ledger and six stop/continue scenarios cover early sufficiency, valid cap
overrun, activity without coverage, exhausted evidence with blocker, triggered next
iteration, and untriggered iteration request.

Evidence: N/A — no exact value or runtime external outcome changes in Phase B.

### AC-6: Stage checkpoints create proportionate Learning Receipts  [depends: AC-1]

Research checkpoints select only durable or contradictory signals and give each selected
signal the receipt required by its disposition.

- [ ] Event triggers include material user correction, production/project surprise, failed assumption, contradiction, or reusable pattern likely to change a future decision.
- [ ] Routine findings, boilerplate absence, and every-artifact completion do not automatically create a Learning Transaction.
- [ ] Reject/task-local records state and reason.
- [ ] Promote/merge/derive records destination/backlink and responsible actor.
- [ ] Defer records destination or due event and responsible actor.
- [ ] Every stage checkpoint can record “no selected signal” without filler.
- [ ] Counter-evidence can reopen a decision or change a receipt disposition.

Gate: Stage-template examples cover all disposition families plus no-signal; every row
has the minimum Phase A fields and no central destination is required for reject/local.

Evidence: N/A — receipt structure is verified in templates; project promotion behavior belongs to Phase D.

### AC-7: RES synthesis routes learning without multiplying capture  [depends: AC-2, AC-6]

RES synthesizes stage receipts and human insights while preserving the distinction among
Fact Candidates, Strategic Insights, decisions, and Learning Transactions.

- [ ] Fact Candidates contain only qualifying promote/merge/derive signals that need durable project verification.
- [ ] Fact Candidate rows preserve source plus destination/backlink and responsible actor.
- [ ] Reject/local/defer receipts stay resolvable in stage traces or the appropriate existing decision/open-thread field and are not copied centrally by default.
- [ ] Strategic Insights record the human-sourced insight, analytical implication, and HL/decision disposition.
- [ ] HL Update Recommendations consume applicable strategic-insight and research-decision destinations.
- [ ] No new top-level capture section or framework file is created.
- [ ] Current `/tfw-knowledge` compatibility is explicitly transitional for Phase D rather than falsely claimed complete.

Gate: Synthesis example traces four stage signals and one human insight into reject,
task-local, Fact Candidate, defer/open-thread, and HL-update outcomes with resolvable
backlinks.

Evidence: N/A — downstream knowledge consolidation is out of Phase B scope.

### AC-8: H4 remains an enforced non-claim  [depends: AC-3, AC-4]

Phase B must not turn procedure fit or research intensity into a cognitive-strategy
architecture or benefit claim.

- [ ] H4 is stated as unresolved/inconclusive where relevant.
- [ ] T0 remains the only authorized desk protocol/owner package.
- [ ] No strategy selector, catalog, registry, runtime strategy choice, prestigious method list, prompt library, or strategy-extension mechanism is added.
- [ ] No name-only, operational, token-matched, matched/mismatched, pilot, or inferential comparison is executed or implied.
- [ ] `focused/deep` is not used as evidence that task-matched strategies improve outcomes.
- [ ] Future search/immersion/Yin work is referenced only as separately owner-gated research.

Gate: Targeted scans plus semantic review find no prohibited architecture/benefit claim;
RF states that no H4 execution occurred.

Evidence: N/A — H4 execution is prohibited.

### AC-9: Cross-consumer consistency, compression, and navigability  [depends: AC-1, AC-2, AC-3, AC-4, AC-5, AC-6, AC-7, AC-8]

The 12-file result is internally consistent, referenceable, and ready for later phases
without claiming that downstream consumers are already migrated.

- [ ] No broken relative link or missing owned anchor is introduced.
- [ ] Workflows contain algorithms, point-of-use gates, and references rather than duplicated template formats.
- [ ] Templates carry output shape and dual-use mindset/test guidance without duplicating workflow policy.
- [ ] No obsolete activity-count completion statement remains in the affected files.
- [ ] No exact config value changes.
- [ ] Phase C/D/E/F transition boundaries are explicit.
- [ ] Documentation generator unit and integration tests pass.
- [ ] RF reports before/after line/word/count measurements as descriptive observations, not acceptance quotas.
- [ ] Generated planning, research workflow, glossary, conventions, and template pages are readable and navigable.

Gate: `python -m pytest docs/scripts/test_gen_docs.py docs/scripts/test_integration.py`
passes; `git diff --check` passes; targeted `rg` scans review former counts, procedure
names, H4 terms, research codes, config diffs, and affected links.

Evidence: Render the generated planning/research/conventions/glossary/template
documentation and record page readability, owned-link navigation, and transition
wording in `evidence/EV__phase-b__planning_research_learning.md`.

### Evidence Artifacts

| File | Description |
|------|-------------|
| `evidence/EV__phase-b__planning_research_learning.md` | Structured evidence: generated documentation environment, affected-page navigation, owned-link results, and per-AC dispositions |

## 6. Technical Guidance

> Reference material, not instructions. Executor MAY deviate with justification in RF.

- **Authority order:** approved Phase B HL → Phase A RF/APPROVE REVIEW → master HL → Iteration 2 RES → Iteration 1 RES → current consumers.
- **Phase A owners:** definitions remain in glossary; operational contracts remain in conventions; workflows/templates consume them through point-of-use gates.
- **Procedure name:** `Comparative Decision Procedure` should replace vague claims that the dimensional-analysis sequence is “research itself.” Avoid an acronym unless implementation proves it saves more context than it adds.
- **Procedure fit:** the gate asks whether the uncertainty requires comparing alternatives, relationships, or configurations. It can only accept/reject the current procedure.
- **Natural dependency:** Gather supplies material decision factors/evidence; Extract constructs relationships/configurations; Challenge attacks them. Preserve this dependency without fixed alternative/configuration counts.
- **Planning trace:** adapt the existing HL Strategic Insights table and Pre-TS gate; do not add a separate insight artifact or ONB section.
- **Learning receipt:** use existing Checkpoint and Fact Candidate surfaces. A compact row is sufficient when its required relations are visible.
- **Fact Candidate compatibility:** keep the canonical `## Fact Candidates` heading for Phase D and `/tfw-knowledge`; narrow entry semantics rather than renaming it in Phase B.
- **Numeric transition:** research workflow consumers may stop enforcing unsupported values while config keys remain unchanged and marked for Phase E restore/remove.
- **Structural floor:** one procedure means all stage traces plus RES, regardless of removed `min_iterations`; additional iterations require a named trigger.
- **Citation safety:** source verification follows claim risk. Do not require a newly fetched external source in a stage that is legitimately structuring or challenging an already declared corpus.
- **H4:** no task/model dispatch or experiment is permitted.
- **Documentation checks:** existing generator/integration suite is the synthetic gate; TD-125/126 remain out of scope and should be observed without bonus fixes.

## 7. Definition of Failure

- ❌ Any Phase A protected obligation disappears from planning/research.
- ❌ Comparative Decision Procedure is universalized or silently applied after a fit mismatch.
- ❌ `focused/deep` selects a method or proves completion.
- ❌ Any retired count is replaced by another unsupported number, hidden quota, or equivalent count language.
- ❌ Config or config-template values change.
- ❌ `min_iterations` removal allows incomplete stage traces or bypasses Coordinator closure authority.
- ❌ Learning Transactions are created for every artifact/finding or selected signals lack disposition receipts.
- ❌ Fact Candidates become a synonym for all learning or lose source/destination/actor traceability.
- ❌ TFW-44 is edited rather than superseded through current contracts.
- ❌ H4 strategy architecture or benefit claim appears.
- ❌ A new framework file or top-level capture section is created.
- ❌ Phase C/D/E/F consumers are modified or falsely declared implemented.
- ❌ Documentation tests, rendered navigation, or affected links fail.

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Count removal weakens depth | Preserve mandatory stage artifacts, claim-based sufficiency, explicit unresolved outcomes, and Coordinator authority |
| Workflow becomes longer while claiming compression | Move output shapes to templates, link Phase A owners, and measure descriptive deltas |
| Procedure-fit branch becomes strategy selection | Permit only current-procedure fit/mismatch and return to Coordinator |
| Qualitative intensity is not observable | Require evidence breadth, counter-evidence, edge cases, and uncertainty statements in outputs |
| Learning tables cause boilerplate | Event-trigger test plus valid no-signal disposition |
| Fact Candidate consumers drift before Phase D | Keep heading and compatibility note; defer promotion/closure changes |
| Config and workflow temporarily disagree | Record exact transitional/unconsumed status in conventions and RF |
| Cross-file terminology diverges | Ownership matrix, targeted scans, generated-link verification |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `.tfw/conventions.md` | Phases C–E | Phase B owns planning/research/learning-entry consumers; later phases must preserve D55 and read Phase B RF |
| `.tfw/glossary.md` | Phases C–E | Phase B owns Comparative Decision Procedure and intensity definitions; later phases reference rather than redefine |
| `.tfw/templates/HL.md` | Phase F validation | Phase B owns insight implication/disposition; migration must preserve filled historical HL artifacts |
| `.tfw/templates/RES.md` | Phase D | Phase B owns research receipt and Fact Candidate entry semantics; Phase D owns knowledge closure/promotion integration |
| `.tfw/workflows/plan.md` | Phase E | Phase B owns purpose/uncertainty/research-fit/iteration gates; Phase E may reconcile config lifecycle without weakening them |
| `.tfw/workflows/research/*` | Phase F validation | Phase B owns comparative procedure and intensity; Phase F validates adapters and production scenarios |
| `.tfw/templates/research/*` | Phase F validation | Phase B owns stage dependency and receipts; Phase F validates generated references and adapters |

> **Cross-references:** master HL Phase B and DoD 6, 8–10; Phase A RF/REVIEW;
> Iteration 2 D15, D18–D20; D22, D23, D37, D43, D49, D51, D55; TFW-44 HL;
> TD-90, TD-107, TD-115, TD-119, TD-123, TD-125, TD-126.

---

*TS — TFW-48 / Phase B: Planning, Comparative Research, and Learning Routing | 2026-07-29*
