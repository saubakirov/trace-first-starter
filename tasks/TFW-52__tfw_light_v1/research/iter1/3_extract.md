# Extract — "What do we NOT see?"

> **Mindset:** Analyst. Use the Gather dimensions to expose coherent combinations without selecting a winner.
> **Test:** Does the configuration space reveal at least one coherent combination not proposed in the Briefing?
> **Parent:** [HL-TFW-52](../../HL-TFW-52__tfw_light_v1.md)
> **Goal:** Extract a small set of coherent TFW product-spine configurations with explicit migration authority, conflict behavior, and teachable progression.

## 1. Extraction method

Gather produced seven four-way dimensions, a theoretical Cartesian product of 16,384 rows. Listing that product would hide rather than expose structure. This stage therefore uses G-D1 through G-D5 as constraints and extracts five topology-anchored configurations:

- one visible-editions configuration with an explicit compatibility contract;
- one independently released package configuration;
- one hybrid common-source/independent-delivery configuration;
- one hidden-siblings counter-configuration;
- one newly visible combination: visible generated sources with new-workspace migration instead of in-place upgrade.

Each row selects one primary alternative per Gather dimension. Secondary safeguards are described in the configuration anatomy, not smuggled into the table as extra alternatives. No configuration is eliminated in Extract; risk statements are inputs to Challenge.

## 2. Configuration Space

| Config | Product-spine granularity | Source topology | Variant governance and evolution | Migration contract | Edition selection signal | Learning sequence | Reinforcement and consolidation |
|---|---|---|---|---|---|---|---|
| **X1 — Visible Contract** | A2. Name-neutral semantic contract | B1. Same repository, visible `editions/<edition>/` | C4. Independent artifacts with compatibility checks | D2. Explicit one-time converter/map | E2. Work-characteristic score | F3. Mental model/terms → demo → hands-on → review/retrieval | G2. Immediate retrieval plus trace review |
| **X2 — Independent Packages** | A3. Compatibility/schema contract | B3. Separate repositories/packages | C4. Independent artifacts with compatibility checks | D3. Neutral interchange manifest | E4. Required-outcome/assurance tier | F3. Mental model/terms → demo → hands-on → review/retrieval | G3. Spaced retrieval plus periodic consolidation |
| **X3 — Hybrid Core and Overlays** | A2. Name-neutral semantic contract | B4. Hybrid modules/submodules/generated packages | C2. Canonical shared core plus overlays | D2. Explicit one-time converter/map | E2. Work-characteristic score | F4. Diagnostic/adaptive sequence | G3. Spaced retrieval plus periodic consolidation |
| **X4 — Hidden Additive Counter-config** | A1. Exact named sequence | B2. Same repository, hidden root siblings | C1. Clone-and-own | D1. Pure additive copy | E1. Person/team maturity labels | F1. Explain all four mechanics, then practice | G4. Artifact-only reinforcement |
| **X5 — Visible Generated, Archived Migration** | A3. Compatibility/schema contract | B1. Same repository, visible `editions/<edition>/` | C3. Generated editions from a schema/template model | D4. New workspace plus linked archive | E3. Observable escalation triggers | F2. Bounded attempt → name mechanism → guided repeat → compare trace | G2. Immediate retrieval plus trace review |

X5 is the combination not proposed in the Briefing: visible same-repository sources do not require clone/copy installation or in-place upgrades. They can be generated from a compatibility model while live-project migration creates a clean target workspace and preserves the prior workspace as an authoritative archive.

## 3. Minimal cross-edition compatibility contract

G-D1 makes the historical core name-neutral. G-D3 requires compatibility to be operational rather than inferred from additive files. The smallest extracted contract therefore has six obligations:

| Contract ID | Obligation | Observable condition | Non-compliant behavior |
|---|---|---|---|
| **K1 Purpose** | Preserve the human-readable purpose and current project context. | Target has either the original content or an explicit reference to the preserved source; no inferred rewrite is presented as original intent. | Purpose is replaced by starter text, silently summarized, or loses its source. |
| **K2 Bounded work** | Preserve stable work-item identity, status, observable completion condition, and links to parent context. | Every migrated work item has a source identity and an unambiguous target representation. | Rows are recreated without identity, status meanings change silently, or completion evidence becomes detached. |
| **K3 Trace/outcome** | Preserve source trace, decisions, outcome, evidence references, and provenance without rewriting history. | Original trace remains readable; derived target artifacts point back to it. | Migration overwrites a trace, drops rejected alternatives, or makes generated content indistinguishable from original evidence. |
| **K4 Continuation context** | Preserve durable facts, decisions, assumptions/open questions, their epistemic status, and source when known. | Target either represents the status directly or retains the source record as an extension/archive. | An open question becomes a fact, a decision loses rationale, or unsupported content is promoted as confirmed knowledge. |
| **K5 Authority/version** | Declare source edition/version, target edition/version, active runtime authority, and authority for each migrated semantic role. | A reader or agent can determine which framework instructions and project-state artifact govern without directory-order guessing. | Two editions can both appear active, generated output competes with its source, or old/new instructions have unspecified precedence. |
| **K6 Conflict/receipt** | Detect conflicts before write and emit a migration receipt with copied, mapped, deduplicated, archived, unresolved, and rejected items. | Equal IDs with unequal content stop or become explicit unresolved records; unsupported data is retained, not discarded. | Last-write-wins, silent defaults, silent field loss, or success without a receipt. |

This is a semantic contract, not a mandate for one filename set. K5–K6 are not historical product-spine concepts; they are the minimum compatibility envelope needed to make H6 testable.

### 3.1 Repository fixture check

The TFW-51 starter cannot be copied mechanically into the current repository root without policy decisions:

| TFW-51 source | Current semantic/path target | Direct comparison | Extracted conflict class |
|---|---|---|---|
| `tfw-light-ru/README.md` (71 lines) | root `README.md` (290 lines) | Same path role, non-identical content. | **Authority/path collision:** starter overview versus active Task Board/project README. |
| `tfw-light-ru/AGENTS.md` (122 lines) | root `AGENTS.md` (61 lines) | Same filename, non-identical instructions. | **Instruction conflict:** overwrite or coexistence can change agent behavior. |
| `tfw-light-ru/TASKS.md` (30 lines) | current Task Board inside root `README.md` | Different filename and representation for related task-state semantics. | **Semantic mapping conflict:** additive copy produces two task boards unless one authority is declared. |
| `tfw-light-ru/memory/PROJECT.md` (52 lines) | current `KNOWLEDGE.md` (189 lines) and Full knowledge workflow | Related purpose, different epistemic model and structure. | **Status/provenance conflict:** field copying can promote or lose meaning. |

All four compared pairs are non-identical. This does not reject additive installation; it shows that additive **migration** requires K5 authority and K6 conflict behavior. Filesystem non-destruction alone does not satisfy semantic preservation.

## 4. Configuration anatomy

### X1 — Visible Contract

**Coherence.** Visible edition directories keep hand-authored products inspectable in one repository. A small compatibility suite checks the name-neutral K1–K6 contract without requiring a shared generator or a large universal core.

**Authority model.**

- The selected edition package is authoritative for framework instructions and templates.
- The live project must have one explicit active-edition/version declaration; the source `editions/` tree is not itself an active runtime.
- Existing project-state content remains authoritative for intent and history; the converter is authoritative only for the documented mapping operation.

**Migration behavior.** A versioned source-to-target map reads the active edition and writes only absent or explicitly mapped targets. It emits a receipt and leaves source traces readable. Upgrade is verifiable and mostly mechanical only for cases covered by the map.

**Conflict behavior.**

- Absent target: add.
- Semantically equivalent item with stable identity: deduplicate and record both locations.
- Same identity with unequal content: stop that item and require an explicit resolution record.
- Existing `README.md`, `AGENTS.md`, task board, or project-memory target: never overwrite by generic copy; invoke the role-specific mapping.
- Multiple runtime declarations: migration fails before writes.

**Pedagogical sequence.** Compact terms/mental model → visible edition demo → guided task producing a trace → immediate review/retrieval. Project-knowledge promotion remains edition-native and separate from remembering the method, satisfying G-D5.

### X2 — Independent Packages

**Coherence.** Separate edition packages can release independently while a neutral interchange schema carries K1–K6. The contract, not repository co-location, supplies continuity.

**Authority model.**

- Each package release is authoritative for its own runtime and exporter/importer.
- A separately versioned interchange specification is authoritative for portable fields.
- The target importer is authoritative for target representation, but cannot reinterpret source epistemic status without recording the conversion.

**Migration behavior.** Export source state to the neutral manifest, validate it, import into a clean target version, and retain both the manifest and receipt. Package release compatibility explicitly declares supported interchange versions.

**Conflict behavior.** Duplicate stable IDs with differing values are rejected. Unsupported source fields remain in a namespaced extension/archive. Contract-version mismatch stops import. Defaults may fill target-only fields only when marked generated, never as source facts.

**Pedagogical sequence.** Compact model/terms → edition-specific demo → hands-on artifact → retrieval/review → later spaced retrieval and periodic knowledge consolidation. A package can optimize guidance locally, but must still teach the shared K1–K4 semantics.

### X3 — Hybrid Core and Overlays

**Coherence.** A canonical name-neutral core is composed with independently versioned edition overlays or delivery packages. This treats shared evolution and release independence as separate concerns.

**Authority model.**

- The common core is authoritative only for declared invariant semantics and shared assets.
- An edition overlay is authoritative only at registered variation points.
- A locked composition manifest identifies exact core and overlay versions; generated/runtime output is never the authoring source of truth.

**Migration behavior.** A converter maps old composition/core/overlay versions to the new composition. Common fields follow the core mapping; edition-specific fields follow the overlay mapping; the receipt records both authorities.

**Conflict behavior.** An overlay that changes an invariant outside a registered variation point fails composition. Two overlays claiming the same variation point fail unless an explicit precedence rule exists. Editing generated output creates drift and is rejected or regenerated from source.

**Pedagogical sequence.** A short diagnostic routes low-prior-knowledge users to model/demo/guided practice and experienced users to bounded attempt/comparison. Both paths converge on retrieval/review and periodic project-knowledge consolidation.

### X4 — Hidden Additive Counter-config

**Coherence.** This configuration maximizes apparent simplicity: each hidden edition is a copied, self-contained bundle; users choose by maturity label; upgrade adds a new bundle; training explains the complete ladder once. It remains in the space as the requested counter-configuration.

**Authority model.** The intended authority is conventionally "the newest or selected hidden directory," but neither clone-and-own nor pure additive copy supplies a durable, shared selection authority. Root instructions and tool-specific discovery order may disagree.

**Migration behavior.** Copy the next hidden directory and preserve prior directories. No semantic converter or neutral representation is required.

**Conflict behavior.** Conflicts are deferred rather than resolved. Divergent task boards, memory files, instructions, and adapters can coexist; whichever file a person/tool reads first may win. A manual pointer could reduce ambiguity, but adding a versioned pointer and compatibility checks would change this configuration toward X1 or X3.

**Pedagogical sequence.** Explain all four editions and the exact named spine, then practice in the chosen edition. The artifact is assumed to reinforce learning; there is no explicit retrieval or knowledge-consolidation loop.

### X5 — Visible Generated, Archived Migration

**Coherence.** Visible edition sources are generated from an explicit compatibility schema, but upgrades avoid mixed-runtime in-place changes. Escalation triggers initialize a clean higher-edition workspace and link the prior project as preserved evidence.

**Authority model.** The schema/template model is authoritative for generated edition sources; generated directories are inspectable delivery artifacts, not editable canon. The prior workspace remains authoritative for historical content, while the new workspace is authoritative for new work after a recorded cutover.

**Migration behavior.** Generate a clean target, import only K1–K4 items that pass mapping, link the prior workspace/archive, record unmapped items, then declare cutover. No source workspace is overwritten.

**Conflict behavior.** Schema/template disagreement fails generation. Imported identity conflicts stop the affected item. Unmapped content remains available through the archive link. Parallel post-cutover edits require an explicit reconciliation; the archive is otherwise read-only by policy.

**Pedagogical sequence.** A bounded task exposes a coordination/assurance limit → the mechanism is named → the user repeats in the generated higher edition → traces are compared and immediately retrieved. The escalation event itself supplies the instructional contrast; project-knowledge consolidation is still a separate policy.

## 5. Cross-configuration patterns

### 5.1 Topology does not determine migration safety

- X1 and X5 share visible `editions/` topology but use different source authority, migration, and conflict models.
- X2 and X3 can both deliver independent packages, while only X3 centralizes invariant source assets.
- X4 can be structurally additive yet semantically ambiguous.

Therefore H5 can compare clarity of source layout, but it cannot infer safe migration from directory placement alone. The actual safety-bearing elements are active-runtime identity, role-based authority, explicit mappings, non-silent conflicts, retained source material, and a receipt.

### 5.2 "Mechanical" has three different meanings

| Meaning | Can be automated? | Human boundary |
|---|---|---|
| **Structural copy** | Yes: create/copy files and directories. | Human is still needed when active authority or target role is ambiguous. |
| **Syntactic conversion** | Yes: rename fields, reshape tables, add version metadata. | Human validates defaults and unsupported fields. |
| **Semantic reconciliation** | Only for proven equivalence rules. | Unequal intent, epistemic status, competing decisions, and contradictory instructions require an explicit decision. |

H6 is credible only if "mechanical" means structural and known syntactic transformations with fail-closed semantic conflicts. "Without loss or manual reconstruction" requires preserved originals/extensions and receipts; it cannot mean automatic resolution of every conflict.

### 5.3 Selection and pedagogy are related but not identical

Work characteristics can select the amount of trace/assurance without labeling the user. Prior knowledge can separately select how that edition is taught. X3 makes this separation explicit: E2 routes the product, F4 routes instructional guidance. An experienced user may need Full for high-risk collaborative work; a novice may appropriately use Light for a short low-risk task.

### 5.4 Retrieval and project consolidation remain separate

- G2 checks whether a person can recall and apply the method after practice.
- G3 also revisits learning and promotes verified project knowledge over time.
- K4 preserves knowledge status during migration but does not itself teach the method.

No configuration should treat a migration receipt, a saved trace, or a knowledge store as proof that the user learned the mechanics.

## 6. External cross-check and counter-evidence

| Source | Extracted rule | Configuration effect | Counter-evidence / transfer limit |
|---|---|---|---|
| SEI, *Variability in Software Product Lines* — https://www.sei.cmu.edu/library/variability-in-software-product-lines/ | Variation must be modeled explicitly and consistently; unmanaged variability can duplicate mechanisms, create incompatible mechanisms, and miss required variants. | Supports registered variation points in X3 and explicit compatibility checks in X1/X2. It also justifies keeping the configuration set small. | TFW has far fewer assets than industrial software product lines; a full variability platform could cost more than hand-authored editions. This challenges overbuilding X3/X5. |
| Kubernetes, *Deprecation Policy* — https://kubernetes.io/docs/reference/using-api/deprecation-policy/ | Version removal requires a version change; supported versions must round-trip without information loss; old/new versions overlap before preferred/storage authority advances. | Supplies an external model for K5–K6, coexistence windows, round-trip tests, and rollback-aware cutover. | Kubernetes has a typed API server and conversion machinery. File-based TFW cannot claim the same guarantees without explicit schemas/tests; policy text alone does not make H6 true. |
| Kubernetes, *Deprecated API Migration Guide* — https://kubernetes.io/docs/reference/using-api/deprecation-guide/ | Migration documentation names target versions and notable semantic changes; automatic conversion can choose non-ideal defaults and therefore requires inspection. | Supports per-version maps, receipts, explicit defaults, and fail-closed semantic differences in X1–X3. | Direct counter-evidence to "converter means no manual review": even mature automated conversion can apply non-ideal defaults. |
| Kalyuga and Renkl, expertise-reversal synthesis — https://doi.org/10.1007/s11251-009-9102-0 | Guidance effective for novices can become redundant or harmful for knowledgeable learners; instruction should adapt as knowledge grows. | Supports X3's diagnostic/adaptive F4 and limiting orientation in X1/X2. | Prior knowledge is hard to diagnose reliably, and evidence from instructional domains does not establish TFW workplace transfer. This challenges making F4 mandatory before a small pilot. |
| Kalyuga et al., *The Expertise Reversal Effect* — https://doi.org/10.1207/S15326985EP3801_4 | The effectiveness of instructional techniques depends substantially on learner expertise. | Separates product selection (work characteristics) from pedagogy selection (prior knowledge). | It does not decide between TFW's F2 and F3 sequences; actual TFW retention and transfer still need measurement. |

## 7. Department-neutral scenario projection

These are analytic projections, not user-test results.

| Work scenario | Work-characteristic signal | Configuration behavior that remains coherent | Mis-selection counterexample |
|---|---|---|---|
| One analyst prepares a reversible internal note | One role, short knowledge life, low error cost. | Light-level output under X1/X2/X3; minimal trace and immediate retrieval are sufficient. | "Advanced analyst → Full" over-processes the work under E1. |
| HR policy change with legal review and later reuse | Multiple roles, high error cost, long-lived rationale. | Higher assurance/consolidation regardless of operator expertise; X2/X3 can retain review and knowledge history. | "Beginner team → Light" under-specifies review evidence. |
| Marketing experiment with rapid iterations | Repeated work, moderate hand-offs, reversible decisions, value in comparisons. | Escalation triggers in X5 or work score in X1/X3 add consistent traces without necessarily adding independent review. | Role count alone may push too high; knowledge lifetime and reversibility temper the choice. |
| Executive transformation program | Many roles, long horizon, high decision cost, need for independent evidence. | Full/Team-like assurance under E2/E4, with pedagogy routed separately by prior knowledge. | A mature executive audience can still need strong guidance on unfamiliar TFW mechanics; maturity label is not instructional diagnosis. |

The scenarios support H7 structurally, but clarity across departments remains an empirical question for Challenge or a later user test.

## 8. Hypothesis status after Extract

| Hypothesis | Extract status | Structural result | Challenge target |
|---|---|---|---|
| **H5** | **NARROWED, still open** | Visible editions support clear source comparison in X1/X5 and avoid X4's hidden-directory discovery ambiguity. Separate packages and hybrid composition remain coherent when authority is explicit. | Test wrong-root/install/runtime discovery and independent release changes. H5 may win over hidden siblings without winning over all separate/hybrid models. |
| **H6** | **REVISE** | The historical A2 spine can support verifiable migration only with K5–K6 and a versioned map/manifest. Exact named stages, pure additive copy, universal automation, and zero manual semantic decisions are not supported. | Test representative Light/current/legacy fixtures, round-trip or archive retention, defaults, duplicate IDs, instruction collisions, and knowledge-status changes. |
| **H7** | **PROVISIONALLY SUPPORTED** | Product selection by work characteristics or required assurance stays coherent across all non-counter configurations; pedagogy can route independently by prior knowledge. | Test short vignettes across departments for consistency, burden, and false escalation. |
| **H8** | **REVISE, effectiveness unproven** | F2, F3, and F4 are coherent only with guidance and retrieval; INNO evidence and expertise reversal reject one universal sequence. | Compare time-to-first-valid-trace, delayed retrieval, transfer to a new task, and novice/expert reactions. |

## 9. Extract decisions

- **E-D1 — Use five topology-anchored configurations, not the Cartesian product.** They cover the required visible, separate, hybrid, and hidden families plus a new visible/generated/archive combination.
- **E-D2 — Define compatibility by K1–K6.** The name-neutral historical spine is necessary but not sufficient; active authority, versions, fail-closed conflicts, preservation, and receipts make migration claims testable.
- **E-D3 — Treat source topology and active runtime as separate states.** A repository may contain several edition sources, but a live project must expose exactly one active framework authority.
- **E-D4 — Carry three automation levels into Challenge.** Structural copy and known syntactic conversion may be mechanical; semantic reconciliation must stop for explicit decisions.
- **E-D5 — Route edition by work and guidance by prior knowledge.** H7 and H8 use different decision signals; person maturity is not a substitute for either.

## 10. Findings

### Found

- Five configurations expose the main topology/governance/migration combinations without a 16,384-row Cartesian product.
- Visible edition directories become materially safer only when paired with a compatibility contract and a single active-runtime declaration.
- Separate packages and hybrid delivery remain coherent; repository co-location is not required for semantic continuity.
- The hidden-siblings counter-config is superficially simple but has no intrinsic authority or conflict-resolution behavior.
- The actual TFW-51/current filename and semantic collisions falsify "copying is enough" for migration.
- K1–K6 turn the historical invariant into a testable compatibility boundary without forcing identical filenames.
- A source layout can be visible while migrations deliberately create clean workspaces and preserve archives; in-place copying is not implied by H5.
- Product routing by work characteristics and pedagogical routing by prior knowledge are independent decisions.

### Remaining

- Challenge must attack each configuration with wrong-root activation, interrupted migration, conflicting IDs/instructions, rollback, independent releases, and mixed prior knowledge.
- No TFW fixture has yet demonstrated a lossless conversion or archive-preserving cutover.
- No cross-department user test has measured selection clarity.
- No TFW learning experiment has measured delayed retrieval or transfer; H8's comparative effectiveness remains unproven.

## 11. Checkpoint

### Sufficiency

- [x] External sources were used in Extract.
- [x] Briefing gaps were reduced into explicit configurations and a compatibility contract.
- [x] The Configuration Space uses all Gather dimension names and G-D1 through G-D5.
- [x] At least one HL hypothesis was tested; H5–H8 were all re-probed.
- [x] Counter-evidence was actively sought for topology, conversion, and pedagogy.
- [x] At least two stage decisions were made.
- [x] Metacognitive check completed: the new result is that visible source topology, active runtime authority, and migration strategy are three separable concerns; the Briefing implicitly bundled them.

**Stage complete:** YES

**Blocking questions:** None.

**Recommended next action:** Run `/tfw-research` Challenge for iteration 1. Pairwise-attack X1–X5 and K1–K6 using wrong-root, live-project migration, conflict/default, rollback, independent-update, cross-department selection, and novice/expert teaching scenarios; retain only configurations whose authority and failure behavior remain explicit.

**Coordinator record:** Extract checkpoint accepted on 2026-08-08; Challenge authorized.
