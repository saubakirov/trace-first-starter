# TS — TFW-48 / Phase A: Method Kernel and Canonical Language

> **Date**: 2026-07-29
> **Author**: Coordinator (Codex)
> **Status**: ✅ TS — Approved for execution on 2026-07-29
> **Parent HL**: [Phase A HL](HL__phase-a__method_kernel.md)
> **Master HL**: [HL-TFW-48](../HL-TFW-48__value_first_methodology_rebaseline.md)

---

## 1. Objective

Establish the approved value-first semantic foundation in TFW's four existing canonical documentation surfaces. Phase A must reconcile the product promise, define the Method Kernel and its minimal object grammar, assign precise terms and owners, and record the rule/proof/learning/extension/numeric contracts that later phases will implement—without changing workflow behavior, adapters, config values, or historical traces.

## 2. Scope

### In Scope

- Reconcile the public product promise in `README.md` with philosophy, values, and success criteria in `.tfw/README.md`.
- Define the five-obligation Method Kernel in `.tfw/conventions.md`.
- Define the minimal object grammar: Rule Record, Proof Record, Learning Transaction, Project Extension, and Numeric Control.
- Replace the universal inline/reference binary with consequence- and observability-typed Rule Deployment.
- Define local, seam, live, and value-debt proof obligations independently from review packaging.
- Separate Learning Transaction receipts from Project Extension lifecycle requirements.
- Define Numeric Control types, semantic lifecycle, and the eight-object provisional restore-owner-or-retire ledger.
- Add concise canonical term definitions to `.tfw/glossary.md` and remove or cross-reference competing foundational wording in the four affected files.

### Out of Scope

- Changes to `.tfw/workflows/`, `.tfw/templates/`, adapters, skills, root agent files, docs generator code, or production repositories.
- Changes to `.tfw/project_config.yaml`, any exact numeric value, enforcement consumer, or Config Sync Registry.
- Implementation of learning receipts, extension loading, proof fields, or new runtime gates in downstream workflows/templates.
- Cognitive-strategy selection, a method catalog, H4 comparison execution, or a strategy-extension contract.
- Changes to KNOWLEDGE.md, TECH_DEBT.md, Task Board history beyond the current TFW-48 status/link update, or historical task/research artifacts.
- Release/version/changelog work and production-project migration.

## 3. Principles Check

| # | Principle (from Phase HL §7) | Enforced by | Gate |
|---|------------------------------|-------------|------|
| P1 | Purpose Before Process | AC-1, AC-2 | Every kernel obligation traces to the reconciled promise, values, and success criteria |
| P2 | Meaning Is the Product | AC-2, AC-3 | Public/philosophical text and the formal kernel preserve intent and trace value beyond output type |
| P3 | Preserve Proven Outcomes, Not Accidental Ceremony | AC-3, AC-6 | Five semantic obligations survive while proof packaging remains independently proportionate |
| P4 | Precision Compresses Context | AC-1, AC-4, AC-9 | One owner per definition; synonym and duplicate-owner scan passes |
| P5 | Structural Gates for Invariants, Judgment for Context | AC-5, AC-6 | Full local pre-action gates remain; claim-triggered proof can vary in packaging |
| P6 | Reality Can Overrule the Plan | AC-3, AC-6 | Evidence precedence and seam/live proof are explicit kernel obligations |
| P7 | Learning Must Become Portable | AC-7 | Selected signals have disposition-typed receipts |
| P8 | Domain-Agnostic by Design | AC-2–AC-8 | Every contract passes a non-code wording/example review |
| P9 | Human Chooses, Framework Clarifies | AC-7, AC-8 | Owner/override decisions remain visible; no inferred replacement values |
| P10 | Method Claims Need Evidence | AC-2, AC-9 | H4 remains unresolved and no strategy architecture enters runtime canon |

## 4. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `README.md` | MODIFY | Align the public promise and “How It Works” summary with the value-first kernel without turning the landing page into formal reference |
| `.tfw/README.md` | MODIFY | Align philosophy, values, “How TFW Works,” and success criteria with product-purpose continuity and the five protected obligations |
| `.tfw/conventions.md` | MODIFY | Become the operational owner of the Method Kernel, object grammar, Rule Deployment, proof obligations, learning/extension boundaries, and Numeric Control lifecycle/ledger |
| `.tfw/glossary.md` | MODIFY | Define the minimal foundational vocabulary once and link operational details to conventions |

**Budget:** 0 new framework files, 4 modified files, approximately 400–700 changed lines. Current config ceilings are treated here as planning escalation triggers, not completion targets: 4/14 files, 0/8 new, estimated below 1200 LOC, 4/12 modifications.

## 5. Acceptance Criteria

### AC-1: Canonical ownership map

The four affected files have distinct, non-competing semantic responsibilities.

- [ ] `README.md` owns the concise public promise and entry path.
- [ ] `.tfw/README.md` owns the philosophy, values, and success criteria.
- [ ] `.tfw/conventions.md` owns operational obligations and contracts.
- [ ] `.tfw/glossary.md` owns concise term definitions and points to operational owners.
- [ ] Foundational definitions are not restated with competing semantics across these files.

Gate: Inspect the four files and produce an RF ownership table showing one owner and all references for every Phase A term.
Evidence: N/A — semantic ownership is verified from the canonical source set; behavioral use is deferred to consuming phases.

### AC-2: Reconciled product promise  [depends: AC-1]

The root and philosophy READMEs express one domain-agnostic product outcome: TFW preserves product purpose, applicable values, decisions, evidence, independent judgment, and durable learning across people, agents, sessions, tools, and output domains.

- [ ] Root positioning remains concise and audience-oriented.
- [ ] Philosophy remains rationale-oriented and does not become an artifact reference manual.
- [ ] Both documents preserve Traces Over Code, honesty, structural enforcement, precise naming, single source of truth, portability, resume, traceability, compounding knowledge, and complete usable output.
- [ ] “Same ritual” does not imply one uniform artifact volume or one universal inquiry method.
- [ ] H4 uncertainty is not converted into a cognitive-strategy capability claim.

Gate: Side-by-side content review against Phase HL §5 items 1–2 and master HL §1/§5; no contradictory promise or code-default language.
Evidence: Open the rendered root landing page and philosophy page; verify the promise hierarchy, value links, and success-criteria links remain readable and navigable.

### AC-3: Method Kernel and object grammar  [depends: AC-1]

`conventions.md` defines a compact Method Kernel and the approved composition model using semantic runtime terms rather than research codes.

- [ ] The Method Kernel contains exactly these five protected obligations: product purpose/applicable Project Values; lifecycle/role authority; evidence precedence; independent judgment; visible learning disposition.
- [ ] The composition model supports one-or-more Rule Records, one-or-more Proof Records per claim, event-triggered Learning Transactions, zero-or-more independent Project Extensions, and applicable Numeric Controls.
- [ ] Protected obligation—not global task weight—is the unit of proportionality.
- [ ] Project-owned values/domain gates remain outside universal kernel content while the kernel requires their discovery and protection.
- [ ] K3, M5, R9, V1, and other research configuration labels do not appear as public/runtime terms.

Gate: Inspect the Method Kernel section and run `rg -n "K3|M5|R9|V1" README.md .tfw/README.md .tfw/conventions.md .tfw/glossary.md`; no research-code match is allowed.
Evidence: N/A — this phase establishes the contract; later phases collect behavioral evidence from its consumers.

### AC-4: Minimal canonical terminology  [depends: AC-3]

`glossary.md` defines only terms that distinguish authority or behavior and does not duplicate operational prose.

- [ ] Canonical definitions exist for Method Kernel, Protected Obligation, Rule Record, Rule Deployment, Proof Record, Local Proof, Seam Proof, Live Proof, Value Debt, Learning Transaction, Learning Receipt, Project Extension, Registered Extension, Numeric Control, and Numeric Control Type.
- [ ] Each definition is concise, domain-agnostic, and linked to the operational section in `conventions.md`.
- [ ] Existing terms are reused when their meaning already matches; superseded synonyms are removed or redirected.
- [ ] Research-only terms remain in research traces and are not added to the glossary.
- [ ] Terminology origin does not claim external authority that the research did not establish.

Gate: Glossary/conventions cross-check: every listed term has one definition, one operational owner, and no conflicting definition in either README.
Evidence: N/A — terminology is source-verifiable.

### AC-5: Rule Deployment contract  [depends: AC-3]

The operational rules select locality by protected consequence and observability rather than by universal repetition, reference-only minimalism, or global task weight.

- [ ] Rule Deployment records semantic owner, point-of-use cue or gate, observable enforcement, authority/exception, and provenance/freshness.
- [ ] Reversible explanatory rules may use canonical reference plus a discovery cue.
- [ ] Lifecycle/navigation failures require a canonical owner plus observable point-of-use gate.
- [ ] Role, safety, destructive, and irreversible pre-action boundaries retain complete local imperatives and hard gates even in routine tasks.
- [ ] Task exposure may strengthen but cannot weaken a pre-action boundary.
- [ ] Current Design Rules no longer present Pattern A or pure reference as universally correct.

Gate: Scenario table in RF covers reversible explanation, lifecycle transition, false evidence/seam claim, and irreversible pre-action authority; each maps to a distinct valid locality.
Evidence: N/A — scenario behavior will be implemented and observed in later workflow/template phases.

### AC-6: Claim-typed proof obligations  [depends: AC-3]

The canon separates proof obligation from review artifact count.

- [ ] Every claimed deliverable requires Local Proof.
- [ ] A claim crossing a component, source, role, package, phase, or other interface adds Seam Proof of both sides and their relation.
- [ ] A claim depending on stakeholder, environment, user, or irreversible external result adds Live Proof at the earliest honest event.
- [ ] Deferred triggered proof creates Value Debt with owner, due event, evidence route, and explicit non-claim.
- [ ] Proof may be packaged compactly, staged, risk-expanded, or grouped without erasing an obligation.
- [ ] Existing Evidence and Verification concepts remain compatible and are not collapsed.

Gate: Four claim examples—local document, cross-source content, cross-component result, and deferred live outcome—each yield the required proof records without prescribing file count.
Evidence: N/A — canonical contract only; real proof use belongs to Phases C–D and F.

### AC-7: Independent learning and extension lifecycles  [depends: AC-3]

Learning Transactions and Project Extensions are distinct objects with proportionate minimum records.

- [ ] Learning entry is event-triggered for selected durable or contradictory signals, not every artifact.
- [ ] Reject/task-local disposition records state and reason.
- [ ] Promote/merge/derive records destination/backlink and responsible actor.
- [ ] Defer records destination or due event and responsible actor.
- [ ] Registered Extension records semantic owner, source/version, precedence/conflict behavior, consumers, freshness evidence, and unsupported/migration behavior.
- [ ] Registration requires an observable load/sync/conflict result; passive metadata is not presented as sufficient.
- [ ] Direct upstream-core fork and every-artifact central registry are not framework defaults.

Gate: Contract matrix demonstrates that a learning transaction can exist without an extension and an extension can exist without a learning transaction.
Evidence: N/A — lifecycle consumers are implemented in Phases B, D, and E.

### AC-8: Numeric Control lifecycle and transitional ledger  [depends: AC-3]

The canon distinguishes numeric semantics before value and records research dispositions without changing current values.

- [ ] Numeric Control Type distinguishes structural existence gate, tunable boundary/threshold, escalation trigger, attention warning, sampling default, normative target, and descriptive measurement.
- [ ] Every normative control lifecycle includes semantic owner, protected failure or intended outcome, observed consumer/enforcement, counting rule, breach response, override authority, provenance/freshness, and monitoring/recalibration.
- [ ] Descriptive measurements require provenance and counting consistency but no breach or override.
- [ ] The ledger records provisional class and next decision for `max_passes`, `min_iterations`, `max_index_lines`, `max_index_facts_lines`, `max_facts_per_topic`, `max_topic_files`, the workflow word-count rule, and the adapter line-count rule.
- [ ] The ledger says current behavior remains transitional until an approved consuming phase restores or retires it.
- [ ] No exact value is changed, endorsed, increased, or inferred from observed breach/non-breach.

Gate: Compare the resulting table with Iteration 2 RES “Numeric Lifecycle”; all eight objects and claim limitations are present, with no project_config diff.
Evidence: N/A — no runtime numeric behavior changes in Phase A.

### AC-9: Cross-document consistency and navigability  [depends: AC-2, AC-4, AC-5, AC-6, AC-7, AC-8]

The four-file result is internally consistent, referenceable, and safe for later phases to consume.

- [ ] No broken relative link is introduced in the affected files.
- [ ] No duplicate foundational definition or conflicting owner remains in the affected files.
- [ ] No strategy selector/catalog claim, research-code runtime term, global light/heavy method, or universal inline/reference rule remains.
- [ ] Downstream workflow/template/config behavior is explicitly transitional rather than falsely claimed implemented.
- [ ] Documentation generator unit and integration tests pass.
- [ ] RF reports before/after word and line measurements as descriptive observations, not success quotas.

Gate: `python -m pytest docs/scripts/test_gen_docs.py docs/scripts/test_integration.py` passes; targeted `rg` scans for research codes, obsolete universal claims, and affected links are reviewed in RF.
Evidence: View the generated landing, philosophy, conventions, and glossary pages and record the rendered-page/link result in `evidence/EV__phase-a__method_kernel.md`.

### Evidence Artifacts

| File | Description |
|------|-------------|
| `evidence/EV__phase-a__method_kernel.md` | Structured evidence: rendered documentation environment, AC-2 and AC-9 observations, link/navigation results, and verdict |

## 6. Technical Guidance

> Reference material, not instructions. Executor MAY deviate with justification in RF.

- **Authority order:** approved Phase A HL → master HL → Iteration 2 RES → Iteration 1 RES → current implementation. Current files are evidence, not authority when they conflict with the approved contract.
- **Semantic owners:** root README = public promise; `.tfw/README.md` = philosophy/values/success criteria; conventions = operational contract; glossary = concise definitions.
- **Research translation:** D11–D20 and M5/K3 explain why the architecture was selected, but their codes should be translated into meaning-based runtime terms.
- **Rule record source:** Iteration 1 X-D1 plus Iteration 2 D13 and challenged M5. Preserve the complete-local exception for pre-action authority/safety/destructive/irreversible boundaries.
- **Proof source:** Iteration 2 D14 and Challenge C3. Local, seam, live, and value-debt records are additive claim obligations, not global modes.
- **Learning/extension source:** Iteration 2 D15–D16. A relation may fit in one line; central registry is conditional, not the default.
- **Numeric source:** Iteration 2 D18–D19 and “Provisional restore-owner-or-retire objects.” The ledger is a decision queue, not value calibration.
- **Transitional compatibility:** no current consumer changes in Phase A. Later phases must read Phase A RF before writing their TS and may not infer that new definitions are already enforced.
- **No extra owner:** do not add `method_kernel.md`, a strategy registry, or another canonical file. If clarity requires a new file, stop and return to `/tfw-plan`.
- **Current documentation verification:** the repository provides MkDocs generation and integration tests under `docs/scripts/`.

## 7. Definition of Failure

- ❌ Any of the five Method Kernel obligations is omitted or reduced to optional ceremony.
- ❌ A new framework file is created to own concepts already assigned to README, philosophy, conventions, or glossary.
- ❌ Research labels appear as runtime/public vocabulary.
- ❌ Rule locality is reduced to “always inline,” “always reference,” or one task-wide light/heavy choice.
- ❌ A deliverable can be claimed without Local Proof, or a crossed/live claim can pass with Local Proof alone.
- ❌ Learning and extensions are coupled, every artifact is centrally routed by default, or passive extension registration is declared sufficient.
- ❌ An exact numeric value or config consumer changes in Phase A.
- ❌ H4 uncertainty is presented as evidence for a strategy selector, catalog, or extension architecture.
- ❌ Workflow/template/adapter/code/project-state/historical-trace files outside the four affected canonical files are modified.
- ❌ Documentation tests, rendered navigation, or affected links fail.

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Four documents repeat the same kernel wording | Enforce the ownership map: public summary, philosophy rationale, operational contract, concise definitions |
| Conventions grow while claiming compression | Replace or link displaced rules; report descriptive before/after measurements and semantic removals |
| Later phases assume definitions equal implementation | Mark transitional consumers and require the Phase A RF at every Pre-TS Gate |
| Broad terminology rewrite creates broken references | Keep the Phase A term set minimal; run targeted reference scans and docs integration tests |
| Numeric ledger is mistaken for approval to delete gates | Preserve current behavior and state the restore/retire owner decision explicitly |
| Domain-neutral terms become vague | Validate each contract with both software and non-code claim examples without making examples normative |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `README.md` | Phase F | Phase A owns product promise; Phase F may add migration/release results without changing the kernel |
| `.tfw/README.md` | Phase F | Phase A owns philosophy alignment; release edits must preserve approved values and success criteria |
| `.tfw/conventions.md` | Phases B–E | Phase A owns kernel/contracts; later phases add or refactor consumers and must read Phase A RF before editing |
| `.tfw/glossary.md` | Phases B–E | Phase A owns foundational definitions; later terms must reference rather than redefine them |

> **Cross-references:** master HL §4 Phase A and §5–§7; Iteration 1 RES D1–D10; Iteration 2 RES D11–D20; KNOWLEDGE D23–D29, D37, D43–D54; TD-45, TD-90, TD-99, TD-107, TD-115, TD-119, TD-123.

---

*TS — TFW-48 / Phase A: Method Kernel and Canonical Language | 2026-07-29*
