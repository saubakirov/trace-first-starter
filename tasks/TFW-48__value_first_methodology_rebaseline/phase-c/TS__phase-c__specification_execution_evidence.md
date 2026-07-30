# TS — TFW-48 / Phase C: Specification, Execution, and Claim-Typed Evidence

> **Date**: 2026-07-30
> **Author**: Coordinator (Codex)
> **Status**: ✅ TS — Approved for execution on 2026-07-30
> **Parent HL**: [Phase C HL](HL__phase-c__specification_execution_evidence.md)
> **Master HL**: [HL-TFW-48](../HL-TFW-48__value_first_methodology_rebaseline.md)
> **Research decision**: SKIP approved — Iterations 1–2 are sufficient
> **Execution approval**: 2026-07-30

---

## 1. Objective

Make TFW's existing specification, onboarding, execution, RF, and EV consumers operate
the approved D55 Method Kernel as one honest claim chain. Phase C must preserve product
intent without turning TS into implementation, require claim-triggered Local/Seam/Live
Proof or explicit Value Debt, distinguish executor attestation from independent review,
and remove automatic phase-splitting authority from transitional scope counts—without
adding a framework artifact, changing exact config values, or modifying Phase D/E/F
consumers.

## 2. Scope

### In Scope

- Define the canonical Requirement Claim → observation → Proof Record → RF attestation
  hierarchy in conventions and concise linked glossary terms.
- Make planning and TS expose source intent, observable outcome, claim boundary, and
  applicable precision/proof decisions without prescribing implementation.
- Make ONB challenge wrong identifiers, unavailable cited systems, missing tests or
  proof routes, value fragmentation, and requirement/guidance ambiguity before action.
- Simplify handoff around the approved role lock, ONB approval, applicable execution
  gates, claim-triggered proof collection, material deviations, complete output, and
  STOP after RF.
- Use the existing mandatory EV file as the index for Proof Records, Evidence
  observations, provenance, and Value Debt; do not create a parallel proof artifact.
- Make RF an explicit executor attestation that resolves each claimed deliverable to
  Proof Records and limitations.
- Preserve the four Evidence statuses while giving each a non-overlapping claim
  consequence.
- Reclassify the four configured scope values as transitional attention/escalation
  signals in current Phase C consumers; preserve their exact values and Phase E owner.
- Reconcile all eight approved framework consumers and generated documentation.

### Out of Scope

- Changes to `.tfw/project_config.yaml`, `.tfw/templates/project_config.yaml`, exact
  scope-budget values, Config Sync Registry, or any other numeric value.
- Changes to `.tfw/workflows/review.md`, `.tfw/templates/REVIEW.md`,
  `.tfw/templates/review/*`, docs/knowledge workflows, or independent Reviewer
  authority; these belong to Phase D.
- Changes to init, resume, config, update, release, lifecycle, registered-extension,
  adapter, migration, version, or changelog consumers; these belong to Phases E–F.
- Changes to planning/research/learning behavior approved in Phase B except the
  specification handoff and scope-budget consumer statements explicitly listed here.
- A new `PROOF`, attestation, evidence-plan, scope, or value-debt file; a new top-level
  artifact type; a uniform staged proof package.
- Strategy selector, catalog, prompt/method registry, runtime cognitive-strategy choice,
  strategy extension, H4 execution, or strategy-effect claim.
- Production-repository changes or retrospective edits to historical task, research,
  RF, or REVIEW traces.
- KNOWLEDGE.md, TECH_DEBT.md, or knowledge-topic writes before post-review workflows.

## 3. Principles Check

| # | Principle (from Phase HL §7) | Enforced by | Gate |
|---|------------------------------|-------------|------|
| P1 | Intent Before Specification | AC-2, AC-3 | Requirement/source/value trace and ONB reality scenarios resolve |
| P2 | Requirements Are WHAT | AC-2, AC-3 | Required precision and adaptable Technical Guidance remain distinct |
| P3 | Claim Boundary Determines Proof | AC-2, AC-6, AC-9 | Local/Seam/Live/Value Debt scenario matrix passes |
| P4 | Presence Is Not Sufficiency | AC-6–AC-8 | File/checkmark/test/evidence implication scans and claim consequences pass |
| P5 | Reality Can Overrule the Spec | AC-3, AC-6, AC-7 | Source, seam, live, and blocker paths can limit or reject an attestation |
| P6 | Attestation Is Accountable, Not Final | AC-7, AC-8 | RF identifies executor authority and Phase D remains independent |
| P7 | Honest Non-Claim Beats Proxy Completion | AC-6–AC-8 | Deferred proof requires complete Value Debt; BLOCKED cannot close |
| P8 | Product Cohesion Before Scope Metric | AC-4, AC-9 | Scope-warning responses preserve one coherent outcome and seams |
| P9 | Protected Obligation Is the Proportionality Unit | AC-5, AC-6, AC-9 | Proof packaging varies while every triggered obligation remains |
| P10 | Natural Gates Before Repeated Prose | AC-1, AC-5, AC-10 | Owners, point-of-use actions, references, and local role locks are mapped |
| P11 | Domain-Agnostic by Design | AC-5, AC-9 | Code, document, research, design, operations, and decision scenarios pass |
| P12 | Existing Owners Before New Artifacts | AC-1, AC-6, AC-10 | Exact eight-consumer scope and zero-new-framework-file gate pass |

## 4. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `.tfw/conventions.md` | MODIFY | Own the Requirement Claim/Proof/attestation hierarchy, Evidence-status consequences, and transitional scope-budget authority |
| `.tfw/glossary.md` | MODIFY | Define only the concise new or narrowed Phase C meanings and link to conventions/templates |
| `.tfw/workflows/plan.md` | MODIFY | Plan claim boundaries, required precision/proof, and scope-warning responses before TS approval |
| `.tfw/templates/TS.md` | MODIFY | Carry compact intent/claim/boundary/precision/proof intent in existing AC structure |
| `.tfw/templates/ONB.md` | MODIFY | Expose specification-to-reality, proof-feasibility, and value-fragmentation conflicts before execution |
| `.tfw/workflows/handoff.md` | MODIFY | Execute applicable gates, collect claim-triggered proof, report deviations, attest, and STOP |
| `.tfw/templates/RF.md` | MODIFY | Relate each claimed deliverable to Proof Record references and explicit limitations |
| `.tfw/templates/evidence/EV.md` | MODIFY | Index Proof Records, real Evidence observations, provenance, and complete Value Debt |

**Budget:** 0 new framework files and exactly 8 modified framework consumers. Current
configuration shows 14 files, 8 new files, 1,200 LOC, and 12 modified files; Phase C
treats these as transitional attention/escalation signals rather than success or
automatic-split authority. Estimated framework change is 350–700 changed lines. Task
trace artifacts and the README Task Board update are lifecycle traces, not new
methodology owners.

## 5. Acceptance Criteria

### AC-1: Canonical owners and consumer chain

The eight affected files have one coherent responsibility chain and no competing
definition or proof artifact.

- [ ] `conventions.md` owns the operational claim/proof/attestation and scope-warning contracts.
- [ ] `glossary.md` owns concise definitions and points to operational/template owners rather than restating their procedures.
- [ ] `plan.md`, TS, ONB, handoff, RF, and EV each consume only the decision/action/output appropriate to their role.
- [ ] Phase A D55 and Phase B D56 remain the semantic authorities; neither is redefined or falsely superseded.
- [ ] No ninth framework consumer, new framework file, or top-level artifact type is introduced.
- [ ] RF includes an ownership/consumer matrix with semantic owner, point-of-use action, protected consequence, and transition boundary.

Gate: Inspect all eight files and produce the RF ownership matrix; targeted scans find
one operational owner and no competing `PROOF`/attestation artifact or Phase A/B
redefinition.

Evidence: N/A — canonical ownership is verified from the source graph.

### AC-2: Compact Requirement Claim contract  [depends: AC-1]

Planning and TS preserve intent while defining an observable claim and the boundary
that determines proof.

- [ ] Each material AC relates to its product purpose, applicable Project Value, human requirement/correction, cited authority, or explicit task-local source.
- [ ] Each material AC states the observable outcome the task is authorized to claim.
- [ ] Each AC exposes whether the claim stays local or crosses a source, interface, role, package, phase, stakeholder, live environment, or irreversible boundary.
- [ ] Every claimed deliverable triggers Local Proof; crossed and live boundaries add the applicable Seam/Live Proof intent.
- [ ] A non-triggered cognitive field may be explicit N/A with reason; blank boilerplate and invented values are prohibited.
- [ ] The contract fits inside the existing AC surface and does not create a new artifact or duplicate the HL narrative.
- [ ] The plan Pre-TS gate checks that material Strategic Insights and user requirements have a claim/scope/guidance/DoF/non-use destination.

Gate: Fill the resulting TS contract for a local document, cited-source adaptation,
cross-component feature, stakeholder design outcome, and operational decision. Each
case preserves intent and yields the correct boundary without implementation steps.

Evidence: Render the generated planning and TS-template pages; verify the claim
contract, owner links, and output hierarchy are legible and navigable.

### AC-3: Required precision, adaptable guidance, and ONB reality check  [depends: AC-2]

Exact identifiers, cited systems, tests, and outcomes are binding only when they define
the requirement or proof boundary; implementation choices remain adaptable.

- [ ] TS distinguishes acceptance-critical precision from reference-only Technical Guidance.
- [ ] Code/file/API identifiers are exact when compatibility or public contract depends on them and explicitly N/A when the work has no such identifier decision.
- [ ] A cited system identifies the source and required relation when acceptance depends on faithful adaptation; citing it without comparison is insufficient.
- [ ] Required tests/checks name the failure or claim they protect; code tests are not universal for non-code work.
- [ ] Product/stakeholder outcomes are observable or become Live Proof/Value Debt rather than vague success prose.
- [ ] ONB checks the actual project/source for required identifiers, cited authorities, proof feasibility, tests/checks, and outcome boundaries before implementation.
- [ ] A mismatch in an acceptance-critical element becomes a blocking question and STOP; an adaptable-guidance deviation may proceed only with RF rationale and claim-impact disclosure.
- [ ] ONB uses existing understanding/question/risk/inconsistency surfaces rather than adding a parallel specification artifact.

Gate: Scenario audit covers wrong path/identifier, unavailable cited source, omitted
required test, adaptable implementation substitution, non-code task, and impossible
live proof. Each produces the correct block/deviation/N/A/debt response.

Evidence: N/A — specification/source reality behavior is verified through filled
scenarios; live project execution is outside this methodology-doc phase.

### AC-4: Scope budgets become owned attention signals  [depends: AC-1]

Current exact scope values remain visible but no longer command automatic splitting or
prove quality.

- [ ] Files-per-phase, new-files, LOC, and modified-files are classified as transitional attention/escalation signals in every affected current consumer.
- [ ] Crossing a signal requires an explicit choice among simplification, removal of unrelated work, a coherent value-boundary split, a bounded override with rationale, or return to Coordinator/user.
- [ ] A split is invalid when it orphans the product outcome, hides a seam, or defers triggered value without complete Value Debt.
- [ ] Reclassifying physical/functional LOC or files solely to satisfy a number is prohibited.
- [ ] Exact values remain unchanged in config and config template.
- [ ] Phase E remains the owner of restore/retire and any future calibration decision.
- [ ] Scope measurements may be reported descriptively with provenance but cannot serve as completion evidence.

Gate: Scope scenario matrix covers below-signal work, cohesive over-signal work,
unrelated scope growth, separable value slices, inseparable enabling work with due live
validation, and metric reclassification. Each returns an authority decision rather
than an automatic split/pass.

Evidence: N/A — this AC changes normative semantics, not a live environment.

### AC-5: Simplified role-locked execution flow  [depends: AC-1, AC-2, AC-3]

Handoff remains a procedural workflow whose gates follow applicable claims rather than
code-default branches or repeated template prose.

- [ ] The complete local Executor role lock, forbidden actions, scope-change STOP, and session naming remain before action.
- [ ] Context loading still includes master/phase HL, TS, predecessor facts, cited knowledge, and affected artifacts.
- [ ] ONB is committed/pushed and explicitly approved before implementation.
- [ ] Execution runs every applicable TS Gate and proof obligation; test/build/source/render/live checks may be N/A only with a claim-based reason.
- [ ] A failing applicable verification/build gate is resolved or represented as a blocked/non-claim outcome before RF.
- [ ] Material deviations identify source requirement, rationale, affected claim/proof, and authority; silent scope or requirement changes are prohibited.
- [ ] Complete usable output remains mandatory across code and non-code work.
- [ ] Pre-RF opens the current RF/EV templates; RF contains every required section; Executor STOP before review remains complete and local.
- [ ] Workflow algorithms reference template-owned output shapes instead of duplicating full section/form instructions where a point-of-use gate is sufficient.

Gate: Walk six domain scenarios—code change, document, research output, design artifact,
operational action, and business decision—through ONB → execution → proof → RF. Each
uses the same role/authority flow with only claim-applicable checks.

Evidence: Render the generated handoff and ONB-template pages; verify role lock,
approval/STOP gates, template links, and non-code applicability are visible.

### AC-6: Proof Records are claim-triggered and resolvable  [depends: AC-2]

The existing EV/RF chain makes every required proof relation explicit without forcing
one row/file package per mechanism.

- [ ] Every claimed deliverable has one-or-more Proof Records with a stable reference.
- [ ] A Proof Record relates claim, boundary/proof class, method or observation, result, artifact/provenance, actor/time when material, and unresolved debt.
- [ ] Local Proof verifies the result inside its owned requirement boundary.
- [ ] Seam Proof verifies both sides and their relation for every crossed source/interface/role/package/phase boundary.
- [ ] Live Proof observes the stakeholder/environment/irreversible outcome at the earliest honest event.
- [ ] Unavailable triggered Seam or Live Proof becomes Value Debt with owner, due event, evidence route, and explicit non-claim.
- [ ] Shared observations may support grouped records when every claim and boundary remains resolvable.
- [ ] A passing test, one-sided interface check, RF checkmark, EV row, or folder/file presence never implies an unobserved boundary.
- [ ] The existing mandatory EV file indexes Proof Records; no new proof file is added.

Gate: Proof matrix covers local document, cross-source content, cross-component
software, cross-phase handoff, live stakeholder outcome, and deferred live outcome.
Every triggered obligation is present; no untriggered artifact volume is required.

Evidence: Render the generated EV-template page and inspect one filled sample; verify
Proof Record relations, artifact/provenance references, grouping, and debt remain
readable.

### AC-7: Evidence status and Value Debt have honest claim consequences  [depends: AC-6]

Verification, Evidence, source/interface observation, Proof Record, and attestation
remain distinct; the four existing Evidence statuses are backward-compatible but no
longer ambiguous.

- [ ] Verification means synthetic/local tool or structural output; Evidence means real-world observation in the intended environment.
- [ ] Source/interface observations may support Seam Proof without being mislabeled as live Evidence.
- [ ] `VERIFIED` requires the intended real-world observation plus a resolvable artifact/provenance reference.
- [ ] `DEFERRED` requires a named future event and complete Value Debt; the deferred outcome remains a non-claim.
- [ ] `BLOCKED` means the required observation cannot currently be obtained and no authorized safe due-event path supports closure; the affected claim cannot close.
- [ ] `N/A` requires a reason that the Evidence class is not triggered and never waives Local or triggered Seam Proof.
- [ ] Evidence status scopes only the observation row and does not automatically become the claim or deliverable status.
- [ ] EV preserves actual environment, method, result, artifact/provenance, and actor/time when material.

Gate: Status matrix covers verified live observation, future due event, external
impasse, genuinely local-only claim, missing artifact, and unjustified N/A. Only the
first four valid cases receive the declared status; missing/unjustified cases fail.

Evidence: Inspect the generated Evidence/Proof contract and a filled EV sample; verify
status consequence and Value Debt fields render without horizontal overflow.

### AC-8: RF is an accountable executor attestation  [depends: AC-6, AC-7]

RF states what the executor can support, where proof lives, and what remains explicitly
unclaimed; it does not impersonate independent review.

- [ ] RF §3 relates each claimed deliverable/AC to its Proof Record references and any limitation, debt, or blocked condition.
- [ ] RF §4 reports applicable verification with reproducible commands/methods, actual results, and proof references rather than generic placeholders.
- [ ] RF §5 remains a concise pointer to EV, includes the Evidence verdict, and does not duplicate the full proof/evidence tables.
- [ ] A checkmark cannot coexist with unresolved blocking proof; supported local work may coexist with an explicit live non-claim/Value Debt.
- [ ] Material deviations identify their requirement authority and effect on the attested claim.
- [ ] RF identifies its statements as executor attestation; Phase D REVIEW retains independent acceptance/rejection authority.
- [ ] Mandatory RF §§6–9 and explicit no-content dispositions remain compatible with Phase B learning receipts.
- [ ] EV/RF or evidence-folder existence is described only as trace presence, never completion proof.

Gate: Filled RF scenarios cover full support, local support plus live Value Debt,
requirement-guidance deviation, and BLOCKED proof. Each resolves its Proof Records and
never overclaims REVIEW authority.

Evidence: Render the generated RF-template page; verify attestation, EV pointer,
limitation, mandatory sections, and owner links are legible.

### AC-9: Cross-domain and production-countercase behavior  [depends: AC-2, AC-3, AC-4, AC-5, AC-6, AC-7, AC-8]

The Phase C contract protects the same product meaning across routine and high-risk
boundaries without uniform proof volume.

- [ ] Helpdesk HD-25 wrong identifier/missing-test pattern is caught before or at ONB/claim verification.
- [ ] Helpdesk HD-30 local-phase success cannot close an unverified adjacent seam.
- [ ] Helpdesk HD-23 phase splitting cannot defer the product outcome without owner, due event, evidence route, and non-claim.
- [ ] AFD-10 a cited source is not proof until the required relation is compared.
- [ ] AFD-36 stale output, failed command, and clean reproduced result remain distinct.
- [ ] AFD-14 synthetic setup cannot claim an honest-live outcome.
- [ ] Routine local code/document work can close with compact Local Proof when no seam/live boundary is triggered.
- [ ] Document/content, research, design, operations, business-decision, and software examples use the same universal terms without code-default gates.

Gate: RF contains a scenario matrix with the six production counter-cases plus at least
six cross-domain/routine cases. Each identifies claim, triggered proof, valid
attestation/non-claim, and authority outcome.

Evidence: N/A — these are historical-corpus and contract scenarios, not fresh production
runs; Phase F owns production migration/regression execution.

### AC-10: Exact scope, consistency, and navigability  [depends: AC-1, AC-2, AC-3, AC-4, AC-5, AC-6, AC-7, AC-8, AC-9]

The eight-consumer result is internally consistent, rendered, and safe for Phase D to
consume without claiming downstream migration.

- [ ] Framework diff modifies all and only the eight approved consumers; no new framework file exists.
- [ ] README changes are limited to the TFW-48 Task Board trace.
- [ ] Config, config template, exact values, review/knowledge/lifecycle/adapter/migration/release consumers, historical traces, and H4 surfaces are unchanged.
- [ ] All changed operational terms have one glossary definition/operational owner and resolvable links/anchors.
- [ ] No automatic scope split/fail/quality language, claim-from-presence implication, Evidence/Proof synonym, code-universal gate, or competing attestation authority remains in the eight consumers.
- [ ] All removals are classified in RF as obsolete, moved to owner/reference, replaced by a precise term, or covered by a stronger structural relation.
- [ ] Documentation generator unit and integration tests pass.
- [ ] Generated conventions, glossary, plan, handoff, TS, ONB, RF, and EV pages are readable, navigable, and free of changed-content overflow.
- [ ] RF reports before/after lines/words/branch/consumer measurements descriptively, with one reproducible counting method and no quota claim.
- [ ] `git diff --check`, protected-file diff, reference, status-scenario, proof-scenario, and exact-write-set checks pass.

Gate: `python -m pytest docs/scripts/test_gen_docs.py docs/scripts/test_integration.py`
passes; targeted semantic scans, generated-link/anchor checks, rendered QA,
`git diff --check`, protected-content comparison, and exact write-set audit are
recorded in RF/EV.

Evidence: View all eight affected generated pages and record the environment,
claim/proof hierarchy, owner-link navigation, role gates, status semantics, and layout
results in `evidence/EV__phase-c__specification_execution_evidence.md`.

### Evidence Artifacts

| File | Description |
|------|-------------|
| `evidence/EV__phase-c__specification_execution_evidence.md` | Resulting Phase C Evidence/Proof index: environment, per-claim Proof Records, applicable real Evidence observations, Value Debt, artifacts/provenance, and verdict |

No additional binary artifact is required. Screenshots or generated-page captures may
be added only if they materially establish a rendered-layout claim that cannot be
represented by a reproducible inspection result.

## 6. Technical Guidance

> Reference material, not instructions. Executor MAY deviate with justification in RF
> unless the item names an acceptance boundary from §5.

- **Authority order:** approved Phase C HL → Phase A RF/APPROVE REVIEW → Phase B
  RF/APPROVE REVIEW → master HL → Iteration 2 RES → current implementation.
- **Existing semantic owner:** `conventions.md` §1.1 already owns Proof Records and
  claim boundaries. Extend the consumer contract there; do not establish a second
  operational proof owner elsewhere.
- **Requirement trace:** the smallest useful TS shape relates intent/authority, claim,
  boundary, precision classification, Gate/proof intent, and Evidence intent. Exact
  headings or compact table layout may vary if AC-2 behavior remains observable.
- **Precision test:** an exact identifier/source/test is a requirement when changing it
  changes compatibility, fidelity, or acceptance. Otherwise place it in Technical
  Guidance and preserve MAY-deviation with claim-impact rationale.
- **ONB placement:** prefer the existing Understanding, Questions, Risks, and
  Inconsistencies surfaces. A compact reality-check cue is sufficient; no new task
  artifact is permitted.
- **Proof packaging:** EV is the index, not the semantic meaning of Evidence. A Proof
  Record may cite RF §4 verification, an EV Evidence row, source/seam comparison, or
  Value Debt. Shared proof may be grouped when references remain resolvable.
- **Attestation:** RF should state support/limitation/non-claim in plain language and
  cite Proof Record IDs. Do not add a second competing global status vocabulary merely
  to label attestation.
- **Status compatibility:** preserve `VERIFIED / DEFERRED / BLOCKED / N/A`; narrow their
  semantics and consequences rather than rename them before Phase D.
- **Scope transition:** change only current consumer authority. Keep all four exact
  config/template values byte-for-value unchanged; Phase E owns restore/retire.
- **Handoff compression:** workflow owns actions and hard role gates; templates own
  output shape. A template reference is valid only when the workflow step says what to
  do and how completion is observed.
- **Role locality:** Executor authority, forbidden artifacts, approval, destructive or
  irreversible boundaries, and STOP before review remain complete local imperatives.
- **Phase D compatibility:** retain current Evidence rows and RF pointer so the existing
  reviewer can audit them; do not edit review consumers or claim Phase D support is
  complete.
- **Domain language:** use output, source, interface, stakeholder, environment, and
  deliverable as universal terms. Code/build/test are conditional examples.
- **Documentation verification:** the repository's canonical synthetic gate is
  `python -m pytest docs/scripts/test_gen_docs.py docs/scripts/test_integration.py`.
  TD-125/TD-126 remain out of scope unless changed content introduces a new failure.

## 7. Definition of Failure

- ❌ Any Phase A protected obligation or Phase B purpose/learning boundary disappears.
- ❌ TS becomes ready-made implementation or fails to distinguish binding precision from adaptable guidance.
- ❌ A material intent/value/source has no resolvable requirement disposition.
- ❌ A claimed deliverable has no Local Proof, or a crossed source/interface/live claim closes on local-only proof.
- ❌ An AC checkmark, passing test, named command, RF statement, EV row, or file/folder presence implies proof beyond its observed boundary.
- ❌ `DEFERRED` lacks complete Value Debt, `BLOCKED` is represented as closed, or `N/A` hides applicable proof.
- ❌ Evidence status is treated as the entire claim status or as independent REVIEW approval.
- ❌ Scope values remain automatic split/fail/quality authority, are raised, or are gamed through reclassification.
- ❌ Phase splitting fragments a coherent product outcome or leaves an unowned seam/live obligation.
- ❌ Handoff weakens role lock, ONB approval, applicable verification, deviation reporting, complete output, or Executor STOP.
- ❌ Code/build/test/deploy becomes the universal meaning of work or proof.
- ❌ A new proof/attestation/scope artifact, global execution mode, or uniform proof-volume requirement is added.
- ❌ A ninth framework consumer changes, any protected exact value changes, or Phase D/E/F/H4 work is performed or claimed.
- ❌ Historical traces are rewritten instead of current contracts being narrowed/superseded.
- ❌ Documentation tests, rendered changed pages, owner links, status/proof scenarios, protected-file checks, or exact-scope audit fail.

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Claim fields bloat every small AC | Permit compact/grouped layout and explicit N/A; verify boundary semantics, not row count |
| Proof Record duplicates Evidence | Keep Evidence as live observation and Proof Record as the claim relation; scenario-test both directions |
| EV becomes a universal evidence dump | Index only claim-triggered proof; allow RF §4/source references and grouped shared observations |
| Scope warning loses practical force | Require explicit response and authority decision when crossed; preserve role/safety hard gates |
| Scope values continue to anchor agents | Remove automatic language from conventions, glossary, and plan; keep Phase E transition explicit |
| Handoff compression removes enforcement | Retain complete local role/approval/STOP imperatives and observable template-use gates |
| Non-code work receives fake test/build N/A boilerplate | Use claim-applicable gates and cross-domain scenarios; require a reason only for applicable decisions |
| Deferred validation becomes routine closure | Require full Value Debt and explicit non-claim; otherwise BLOCKED |
| Existing review consumers misread the richer EV | Preserve current evidence table/status/pointer contract and mark Phase D boundary |
| Eight-file terminology drifts | Ownership matrix, complete consumer scan, generated owner-link checks, and independent review |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `.tfw/conventions.md` | Phases D–E | Phase C owns claim/proof production and scope-warning consumer semantics; Phase D owns independent judgment, Phase E exact numeric lifecycle |
| `.tfw/glossary.md` | Phases D–E | Phase C owns concise requirement/attestation/status narrowing; later phases reference rather than redefine |
| `.tfw/workflows/plan.md` | Phase E | Phase C owns TS claim/proof planning and non-automatic scope response; Phase E may change config lifecycle only |
| `.tfw/templates/RF.md` | Phase D | Phase C owns executor attestation; Phase D owns review use and knowledge closure |
| `.tfw/templates/evidence/EV.md` | Phase D/F | Phase C owns proof/evidence production shape; Phase D audits it and Phase F validates migration |
| `.tfw/workflows/handoff.md` | Phase F | Phase C owns universal execution behavior; Phase F validates adapter parity and migrated projects |
| `.tfw/templates/TS.md` | Phase F | Phase C owns requirement/proof contract; Phase F validates historical and adapter consumption |
| `.tfw/templates/ONB.md` | Phase F | Phase C owns pre-action reality check; Phase F validates generated/copied artifacts |

> **Cross-references:** Phase C HL §3–§7; master HL Phase C and DoD 6, 12–14;
> Phase A RF/REVIEW; Phase B RF/REVIEW; Iteration 2 D14, D17–D19; D24, D49,
> D52–D56; philosophy F20/F21/F24/F26/F28/F30/F31; process F4/F6/F16/F18/F23/F25.

---

*TS — TFW-48 / Phase C: Specification, Execution, and Claim-Typed Evidence | 2026-07-30*
