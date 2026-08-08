# Challenge — "What do we NOT expect?"

> **Mindset:** Critic. Every survivor needs an explicit authority and failure model; every elimination needs a falsifiable reason.
> **Test:** Would the surviving configurations hold if a different researcher attacked wrong-root activation, live migration, independent releases, and mixed learner expertise?
> **Parent:** [HL-TFW-52](../../HL-TFW-52__tfw_light_v1.md)
> **Goal:** Eliminate internally inconsistent edition configurations, preserve real alternatives, and issue bounded verdicts on H5–H8.

## 1. Attack protocol

Three OODA challenge loops were applied:

1. **Authority and migration:** wrong root, multiple installed editions, path collisions, duplicate identities, interrupted writes, rollback, downgrade, and unsupported fields.
2. **Evolution and proportionality:** shared change propagation, independent releases, contract drift, overlay/generator complexity, and hand-authored transparency.
3. **Selection and pedagogy:** cross-department work signals, novice/expert divergence, immediate performance versus delayed retrieval, and project-knowledge consolidation.

Configurations were attacked against seven gates:

| Gate | Pass condition | Failure condition |
|---|---|---|
| **P1 Active authority** | A person and an agent identify exactly one active edition/version and role authority, or the operation fails before mutation. | Discovery order, current directory, or newest-looking folder silently selects authority. |
| **P2 Semantic preservation** | K1–K4 are preserved in target representation or a readable retained source/archive. | Intent, identity, evidence, rationale, or epistemic status is silently changed or lost. |
| **P3 Conflict safety** | K5–K6 detect unequal identities/content, incompatible versions, and instruction collisions before writes; a receipt records disposition. | Last-write-wins, permissive import, silent defaults, or success without a receipt. |
| **P4 Rollback/continuity** | Failed/interrupted migration leaves a recoverable source and a declared cutover state. | Partial target becomes active or the only readable source is mutated. |
| **P5 Independent evolution** | Common changes and edition-specific releases have an explicit propagation/compatibility path. | Fixes drift silently or every edition release must move atomically without product need. |
| **P6 Proportionality** | Mechanism cost is justified by observed variation, migration risk, or release independence. | Schema, generator, overlay, or repository coordination costs exceed the small edition portfolio's demonstrated need. |
| **P7 Pedagogical credibility** | Sequence includes bounded guidance, observable practice, retrieval/review, and separates method learning from project-knowledge consolidation. | It assumes lecture, artifact production, or migration alone proves understanding and retention. |

Outcome labels:

- **SURVIVE:** coherent with explicit conditions and no known fatal pair.
- **LIMITED SURVIVOR:** a mechanism survives, but the full Extract configuration is not proportionate as a default.
- **ELIMINATE AS SPECIFIED:** repairing the failure changes one or more defining alternatives, turning it into another configuration.

## 2. Pairwise attack: X1–X5

All ten configuration pairs were compared; no row is omitted.

| Pair | Hardest attack / differentiator | Result |
|---|---|---|
| **X1 vs X2** | X1 has one review surface but couples source changes/releases and duplicates hand-authored fixes. X2 isolates release/runtime authority but introduces neutral-contract ownership and cross-repository conformance. | **Both survive conditionally.** X1 is smaller when releases move together; X2 is stronger when editions need independent release/access/ownership. Same-repo location is not a safety proof. |
| **X1 vs X3** | X1 avoids overlay machinery but relies on compatibility checks catching hand-authored drift. X3 propagates common assets but can hide variation in composition rules. | **Both survive conditionally.** X1 requires change-impact/conformance tests; X3 requires a variation registry, locked composition, and generated/source boundary. Neither dominates without change-frequency evidence. |
| **X1 vs X4** | Wrong-root or multiple-runtime discovery: X1 can fail before writes through K5; X4 lets hidden copied frameworks and reader/tool discovery order compete. | **X1 survives; X4 eliminated as specified.** A pointer plus compatibility/conflict checks would repair X4, but it would no longer be B2+C1+D1/G4 as extracted. |
| **X1 vs X5** | X1 performs in-place mapped migration with collision stops; X5 creates a clean target/archive but adds schema/generator/cutover mechanics. | **X1 survives as proportionate baseline; X5 mechanism survives for high-risk cutovers.** X5's generator is not justified as default without repeated-variation evidence. |
| **X2 vs X3** | X2 permits truly independent sources/releases but can drift at the neutral contract. X3 centralizes the invariant core but couples consumers to core/overlay composition. | **Both are real alternatives.** X2 needs a separately governed contract and support matrix; X3 needs explicit variation points and independent overlay compatibility. |
| **X2 vs X4** | X2 identifies an exact package version and importer; X4 has no durable active authority or semantic conflict model. | **X2 survives; X4 eliminated.** Hidden path simplicity does not compensate for ambiguous runtime state. |
| **X2 vs X5** | X2 pays ongoing contract/export/import cost; X5 pays generator and clean-workspace cutover cost. X2 better supports independent delivery, X5 stronger rollback isolation. | **X2 survives broadly; X5 only conditionally.** D4 archive cutover can be added to X2 without adopting C3 generation. |
| **X3 vs X4** | X3 controls where editions may vary; X4 permits clone drift and exact-spine divergence with no detection. | **X3 survives; X4 eliminated.** Making X4's clones conform to registered variation points changes it toward X3. |
| **X3 vs X5** | Both add product-line machinery. X3 pays composition complexity to propagate common changes; X5 pays generation/archive complexity to isolate migration. | **X3 survives conditionally; X5 limited.** Choose only after measuring common-change frequency versus migration/cutover risk. Combining both by default would compound P6 risk. |
| **X4 vs X5** | X4 preserves old folders but leaves authority ambiguous; X5 preserves an explicitly read-only archive and records cutover. | **X5 mechanism survives; X4 eliminated.** The difference is not copying versus archiving; it is explicit authority, cutover, and conflict disposition. |

## 3. X1 was not given a softer test

X1 is the configuration most aligned with the current HL direction, so it received six additional attacks.

| X1 attack | Failure found | Required survival condition | Residual gap |
|---|---|---|---|
| **Source/runtime confusion** | A visible `editions/` tree can be mistaken for an installed runtime or read from the wrong root. | One machine- and human-readable active-edition/version declaration; `editions/` explicitly marked as source packages; no declaration means fail before mutation. | No prototype has tested all supported agents/adapters from nested working directories. |
| **Hand-authored drift** | C4 checks may lag behind edition edits; a shared fix can be applied to only one edition. | Contract conformance and cross-edition change-impact checks run for every common semantic change. | Test scope and owner are undefined. |
| **Release coupling** | One repository encourages editions to move together even if Light needs a patch while Full is unstable. | Edition-scoped versioning/release notes and tests must permit independent package releases inside the repository. | Current release tooling has not demonstrated this. |
| **Converter-chain growth** | Every adjacent version/edition map can accumulate defaults and unsupported cases. | Declare supported source-target pairs, fail closed outside them, retain source/archive, and test direct plus chained migrations. | Maintenance cost across future versions is unknown. |
| **Downgrade/rollback** | Higher-edition-only fields cannot always round-trip into Light. | Downgrade retains unsupported data in an extension/archive and distinguishes rollback from destructive downgrade. | No round-trip fixture exists. |
| **Instruction collision** | TFW-51 and current root `README.md`/`AGENTS.md` are already non-identical path-role collisions. | Role-specific mapping, never generic overwrite; unequal instructions require explicit resolution or retained source. | The exact mapping is not specified in iteration 1. |

**X1 verdict:** conditional survivor, not a proven winner. It passes only with K5–K6, conformance ownership, edition-scoped releases, and fixture evidence. Without those, it degenerates into visible clone-and-own and fails P1/P3/P5 just as X4 does.

## 4. X2 and X3 as real alternatives

### X2 — Independent Packages

X2 survives because repository separation can strengthen, rather than weaken, active authority:

- the installed package/version is explicit;
- edition release and access boundaries are independent;
- a neutral manifest can make compatibility visible instead of relying on directory proximity;
- a clean importer naturally supports preflight validation and receipts.

Its failure mode is contract drift. X2 therefore requires a separately versioned K1–K6 specification, conformance fixtures consumed by every package, and a support matrix declaring which manifest versions each exporter/importer accepts. If those are absent, X2 becomes A4 independent contracts and H6 fails.

### X3 — Hybrid Core and Overlays

X3 survives because common-source and independent-delivery are not contradictory:

- invariant assets can receive one fix;
- overlays can version edition-specific mechanisms independently;
- a composition lock can make the delivered runtime reproducible;
- an overlay can teach or enforce a higher edition without copying every common asset.

Its failure mode is invisible variability. X3 therefore requires a short variation registry, an allowlist of overlay-owned roles, conformance tests for the composed product, and a prohibition on editing generated/runtime output as canon. If every file becomes a variation point, X3 fails P6 and is less understandable than X1.

The two alternatives serve different forces. X2 optimizes release/ownership independence; X3 optimizes propagation of shared changes. Both remain live until those forces are measured in the TFW portfolio.

## 5. X4 elimination test

X4 was tested for an unexpected survival case rather than rejected from its labels alone.

### Cases where hidden siblings can be useful

- an inert cache of downloaded edition packages;
- a read-only rollback snapshot;
- a test fixture directory that is never discovered as runtime authority;
- a source checkout used by one explicit installer.

These uses survive only when K5 declares them **inactive** and K6 prevents them from competing with the runtime. That repair removes X4's defining "newest/selected hidden directory by convention" authority and its pure copy/conflict-defer behavior.

### Elimination

As a product/runtime configuration, X4 fails:

- **P1:** multiple discoverable hidden roots have no intrinsic single authority;
- **P2:** its exact named spine is not the historical invariant and can force semantic reinterpretation;
- **P3:** clone-and-own plus pure additive copy defers conflicts;
- **P5:** fixes drift without compatibility checks;
- **P7:** lecture plus artifact-only reinforcement lacks retrieval and explicit consolidation.

**X4 verdict:** **ELIMINATE AS SPECIFIED.** Hidden directories may survive only as inactive storage/fixtures under another configuration's authority rules, not as competing edition runtimes.

## 6. X5 proportionality test

X5 contains two separable ideas:

1. **C3 generation from a schema/template model.**
2. **D4 clean target workspace plus preserved archive and explicit cutover.**

The D4 mechanism survives P1–P4: it makes rollback and provenance clearer than in-place mutation. The C3 mechanism does not yet pass P6 for a small document-oriented framework. No evidence shows that repeated cross-edition variation is large enough to repay schema design, generator maintenance, generated-output review, and contributor training.

**X5 verdict:** **LIMITED SURVIVOR.** Retain D4 as an optional high-risk migration profile usable by X1, X2, or X3. Do not carry C3 generation as the default topology recommendation unless a change simulation demonstrates lower total authoring/review cost and readable output.

## 7. Pairwise attack: K1–K6

All fifteen contract pairs were attacked. The contract is internally consistent only with the rules below.

| Pair | Collision or false inference | Required rule | Pair result |
|---|---|---|---|
| **K1 Purpose × K2 Bounded work** | Migration may infer current purpose from the newest task or attach work to the wrong goal. | Preserve purpose and task links separately; changed purpose is a versioned decision, not an automatic task-derived rewrite. | Compatible with explicit links. |
| **K1 × K3 Trace/outcome** | A trace may record work under an earlier purpose; rewriting it to current purpose falsifies history. | Preserve time-scoped source purpose and trace provenance; target may add a current-context reference without altering the trace. | Compatible with temporal provenance. |
| **K1 × K4 Continuation context** | Project memory may summarize purpose differently, creating two apparent truths. | Declare the purpose source and treat summaries as derived/contextual; disagreement becomes an open conflict. | Compatible with role authority. |
| **K1 × K5 Authority/version** | A new edition starter can overwrite project purpose while claiming framework authority. | Framework authority never implies authority over project intent; K5 must distinguish framework and project-state roles. | Compatible; fatal without role separation. |
| **K1 × K6 Conflict/receipt** | Purpose conflicts are tempting to merge as prose. | Unequal purpose records are never auto-merged; receipt records retained source, target, and explicit resolution. | Compatible, fail closed. |
| **K2 × K3** | A completed-looking trace can silently close a still-open task, or task status can erase contrary evidence. | Status conversion is explicit; trace is evidence, not status authority. Mismatch remains visible. | Compatible with independent roles. |
| **K2 × K4** | Task completion can be mistaken for fact confirmation or durable-knowledge promotion. | Completion and epistemic confirmation are separate state transitions. | Compatible; supports G-D5. |
| **K2 × K5** | TFW-51 `TASKS.md` and Full's README Task Board can both claim active task state. | K5 declares exactly one target task-state authority and maps source rows with stable IDs/status semantics. | Compatible only with role mapping. |
| **K2 × K6** | Equal task IDs with unequal status, criteria, or parent links. | Stop the item; never choose newest timestamp or target default silently. | Compatible, fail closed. |
| **K3 × K4** | A trace statement can be promoted directly to confirmed knowledge. | Trace remains evidence; promotion records source, verification, epistemic status, and decision. | Compatible with explicit promotion. |
| **K3 × K5** | Generated migration logs or target summaries can compete with original trace authority. | Original trace is immutable source evidence; derived artifacts declare origin and never replace it. | Compatible with provenance. |
| **K3 × K6** | Converter wants to normalize/rewrite trace history for target format. | Preserve original or content-addressed archive; receipt records derived representation and any rejected conversion. | Compatible; no destructive normalization. |
| **K4 × K5** | Target Full workflow may treat imported Light memory as confirmed knowledge. | Target representation preserves source epistemic status; framework workflow owns future promotion, not retroactive truth. | Compatible only with status mapping. |
| **K4 × K6** | Target lacks a field for an assumption, contradiction, or open question. | Retain unsupported data in extension/archive and report it; no silent drop or promotion. | Compatible with loss accounting. |
| **K5 × K6** | Conflict detection cannot decide precedence when authority is itself ambiguous. | Authority/version preflight runs first; multiple or missing active authorities stop migration before content writes. | Dependency: K6 is not sufficient without K5. |

### Contract result

- K1–K4 are the portable semantic payload.
- K5 is the control plane that distinguishes framework source, active runtime, project state, original evidence, and generated derivatives.
- K6 is the transaction/evidence boundary.
- K5 and K6 are jointly necessary; neither compensates for missing K1–K4.
- The contract must be strict about known semantics but preserve unknown input in an extension/archive. Pure rejection would protect consistency but could strand old projects; permissive interpretation would hide divergence.

## 8. Incompatible dimension pairs

| Dimension A / alternative | Dimension B / alternative | Why incompatible as specified | Repair changes it into |
|---|---|---|---|
| **B2 hidden root siblings** | **D1 pure additive copy without K5/K6** | Multiple discoverable runtimes coexist with no deterministic active authority or conflict receipt. | X1-like explicit runtime contract or inactive archive storage. |
| **C1 clone-and-own** | **A1 exact universal spine without compatibility checks** | Independent edits can violate the claimed exact spine without detection. | C4 compatibility checks or C2 shared core. |
| **D1 pure additive copy** | **K5 exactly one active runtime**, if old runtimes remain discoverable | Copying another runtime adds ambiguity unless prior runtime is deactivated or marked inert. | Versioned cutover/pointer plus receipt; no longer pure D1. |
| **A4 independent edition contracts** | **D3 neutral interchange manifest** | A neutral manifest has no stable semantics if editions share no contract. | A2/A3 common semantic/compatibility contract. |
| **C3 generated editions** | **Generated output treated as hand-authored authority** | Two sources of truth cause drift and unreproducible regeneration. | Schema/model authority plus read-only/disposable output. |
| **C2 overlays** | **Unregistered overlay ownership** | An overlay can alter invariants or collide with another overlay invisibly. | Explicit variation registry/composition lock. |
| **E1 person maturity as primary selector** | **E2/E4 work or assurance as primary selector** | They can prescribe different editions for the same work and user; silent precedence defeats clarity. | Work selects edition; prior knowledge selects guidance. |
| **F1 explain all editions first** | **H8 as universal do-first superiority claim** | Both cannot be the universal primary sequence. Evidence indicates the choice varies with prior knowledge and task. | F3 safe default or F4 adaptive path. |
| **G4 artifact-only reinforcement** | **H8 consolidation as a claimed mechanism** | G4 contains no retrieval or consolidation behavior, so it cannot instantiate the claimed learning loop. | G2/G3 explicit retrieval/consolidation. |

Important non-incompatibilities:

- Same-repository source and independent edition releases can coexist if versioning/tests are edition-scoped.
- Separate repositories and one semantic contract can coexist through a separately governed contract/conformance suite.
- Hybrid composition and independent delivery can coexist through pinned component versions.
- Clean-workspace migration can be used with X1, X2, or X3; it is not exclusive to generated editions.

## 9. Surviving configurations

| Survivor | Status | Required conditions | Why it remains live |
|---|---|---|---|
| **X1 Visible Contract** | **SURVIVE, conditional** | Single active-runtime declaration; K1–K6 conformance owner; edition-scoped releases; role-specific converters; preserved sources and receipts. | Smallest transparent same-repo option and directly addresses hidden-root ambiguity, but is not safe by layout alone. |
| **X2 Independent Packages** | **SURVIVE, conditional** | Separately versioned neutral contract; shared conformance fixtures; exporter/importer support matrix; explicit package ownership. | Clean runtime/release authority and legitimate independent lifecycle. It falsifies any claim that same-repo is the only coherent topology. |
| **X3 Hybrid Core and Overlays** | **SURVIVE, conditional** | Minimal invariant core; registered variation points; composition lock; conformance tests; generated/source boundary. | Best structural answer when shared changes are frequent and delivery must remain independent, but must prove proportionality. |
| **X5-D4 Archive Cutover** | **LIMITED SURVIVOR** | Clean target, immutable/read-only source archive, explicit cutover, K1–K6 import/receipt, reconciliation rule for post-cutover edits. | Strong rollback/provenance mechanism for risky live migrations. The broader generator configuration does not yet survive as default. |

**Eliminated:** X4 Hidden Additive Counter-config as a product/runtime design. Hidden storage survives only when explicitly inactive under another survivor's authority.

### Unexpected survivor

**X2 Independent Packages** is the unexpected survivor. The initial HL favored visible same-repository editions, yet source separation does not imply semantic fragmentation when K1–K6, conformance fixtures, and package-version authority are explicit. Git's official submodule model further demonstrates that independent histories can be pinned and composed; the trade-off is operational initialization/synchronization, not logical impossibility.

Unexpected surviving mechanism: X5's D4 archive cutover remains useful even if generation is rejected. It can strengthen X1, X2, or X3 without adopting X5 wholesale.

## 10. External challenge and counter-evidence

| Source | Attack result | Effect on survivors | Limitation / counter-pressure |
|---|---|---|---|
| IAB RFC 9413, *Maintaining Robust Protocols* — https://www.rfc-editor.org/info/rfc9413/ | Broadly tolerating unexpected input can entrench divergent semantics and increase future interoperability cost. Active maintenance should surface and resolve ambiguity. | Supports fail-closed K5–K6 and rejects permissive "best effort" migration. | Strict exclusion can fracture an ecosystem; RFC 9413 also supports understanding affected deployments and providing a migration plan. Therefore unknown TFW fields should be retained/reported, not merely rejected or silently accepted. |
| Git, *gitsubmodules* — https://git-scm.com/docs/gitsubmodules | Independent repositories can retain separate histories, be pinned to exact commits, and be composed in a superproject. | Confirms X2/X3 are technically real alternatives and can have deterministic version authority. | Submodules require explicit initialization/update and introduce synchronization state. This is operational counter-evidence against treating hybrid composition as free simplicity. |
| Google, *Why Google Stores Billions of Lines of Code in a Single Repository* — https://research.google/pubs/why-google-stores-billions-of-lines-of-code-in-a-single-repository/ | A monorepo can provide a common source of truth, but the published case explicitly reports trade-offs and specialized supporting systems/workflows. | Supports X1's review surface but does not eliminate X2/X3. | Direct counter-evidence to generic "one repository is clearer" reasoning; TFW must prove benefits with its scale and tooling. |
| SEI, *Variability in Software Product Lines* — https://insights.sei.cmu.edu/library/variability-in-software-product-lines/ | Unnecessary, duplicate, incompatible, or awkward variation mechanisms make product-line management difficult. | Supports explicit X3 variation points and X1/X2 conformance. | Challenges X5 generation and any X3 overlay model whose setup/variation count exceeds demonstrated need. |
| Rey and Buchwald, randomized expertise-reversal trial — https://pubmed.ncbi.nlm.nih.gov/21443379/ | In the study, added explanatory text improved novice retention/transfer but reversed for participants made more knowledgeable. | Supports separating work-based edition routing from prior-knowledge-based guidance and keeps F4 credible. | The study used mathematical animation with 104 students, not TFW workplace tasks; it cannot prove H8's effectiveness claim. |

## 11. H5–H8 verdicts

| Hypothesis | Challenge verdict | Evidence that survives | What is rejected or still unproven |
|---|---|---|---|
| **H5** — visible `editions/` is clearer/safer than hidden root siblings | **SUPPORTED against hidden siblings; NOT a global topology winner** | X1/X5 separate source packages from active runtime and can expose one review surface. X4 fails authority/conflict gates. | X2 and X3 remain coherent alternatives. Same-repo visibility alone does not create migration safety; K5–K6 do. |
| **H6** — one exact semantic core permits mechanical no-loss upgrades | **REFUTED AS WRITTEN; revised form survives** | The name-neutral K1–K4 payload plus K5–K6, versioned mappings, retained originals/extensions, and receipts supports verifiable structural/syntactic migration. | Working Backwards/formal knowledge are not historical universals. Universal automation, zero manual semantic decisions, and no-loss claims without archive/round-trip tests fail. |
| **H7** — work characteristics are clearer than maturity labels | **PROVISIONALLY SUPPORTED; clarity unmeasured** | E2/E4 route the same experienced person differently by error cost, roles, assurance, and knowledge life; E1 produces systematic scenario mis-selection. | No department-user study has measured agreement, burden, or false escalation. Work factors may still need a simpler trigger/tier presentation. |
| **H8** — do/notice/mechanism/repeat teaches better than lecture-first | **PARTIAL / REVISE; comparative effectiveness unproven** | Bounded action, explicit naming, guided repeat, retrieval, and separate knowledge consolidation survive. INNO-6/12/13 support action/retrieval; external evidence supports adapting guidance. | A universal do-first order fails novice-guidance and expertise-reversal attacks; INNO-8/13 include orientation/terms first. No TFW trial shows better delayed retention or transfer than a compact-model-first sequence. |

## 12. Measurable gaps and proposed evidence gates

| Gap | Minimum test | Measures | Evidence gate before a product claim |
|---|---|---|---|
| **M1 Active-runtime clarity** | Clean Light, Full, mixed legacy, duplicate-marker, nested-working-directory, and inactive-archive fixtures across supported adapters/agents. | Selected edition/version; time to identify; pre-write failures; silent precedence count. | 100%: exactly one correct authority or explicit pre-write failure; zero discovery-order selection. |
| **M2 Migration preservation** | TFW-51 Light, early v1/v2, current Full, conflicting-ID, interrupted-write, unsupported-field, and downgrade fixtures. | K1–K4 preserved/mapped/archived; unresolved items; silent loss; receipt coverage; rollback success. | Zero silent loss/promotion/overwrite; every source item has a receipt disposition; failed migration leaves source usable. |
| **M3 X1/X2/X3 evolution cost** | Apply at least 10 representative changes: common wording fix, new invariant field, Light-only guidance, Full-only gate, security fix, rename, deprecation, adapter update, release-only patch, contract-version change. | Authoring touches, duplicated edits, repositories/releases coordinated, conformance failures caught, elapsed review effort. | Do not choose a topology globally until median and worst-case costs are compared; publish the measured trade-off rather than infer it from layout. |
| **M4 X2 contract viability** | Version-skew matrix with current and one prior manifest version across all edition exporters/importers. | Successful supported imports, rejected unsupported pairs, retained extensions, drift caught by shared fixtures. | Every declared pair passes shared fixtures; undeclared version pairs fail before write. |
| **M5 X3/X5 proportionality** | Prototype one minimal overlay path and one generator path against the same 10-change set, without changing product files in this iteration. | Setup/maintenance effort, variation points, generated diff readability, manual overrides, duplicate mechanisms, amortization estimate. | X3/X5 machinery advances only if it demonstrably reduces repeated authoring/review cost without making generated outputs or authority harder to inspect. No threshold is claimed before the baseline is measured. |
| **M6 Edition-selection clarity** | At least 12 department-neutral vignettes spanning HR, legal/compliance, marketing/operations, research, and executive work; mixed-role reviewers choose edition and explain why. | Inter-rater agreement, completion time, factor usage, over/under-escalation, maturity-label leakage. | H7's "clearer" claim advances only if work-based routing has higher agreement and no higher harmful under-selection than maturity labels. |
| **M7 Pedagogy/retention** | Compare compact-model-first and bounded-attempt-first routes for low/high prior knowledge on the same TFW task; repeat on a novel task after 48–72 hours. | Time to first valid trace, immediate errors, unaided mechanic recall, new-task transfer, perceived confidence versus actual performance. | H8's "more effective" claim advances only with better delayed retrieval/transfer for a defined learner segment, not immediate satisfaction alone. |
| **M8 Consolidation behavior** | Close several Light tasks containing facts, decisions, assumptions, contradictions, and open questions, then audit project memory. | Omission, duplicate, status-promotion, contradiction, provenance, and stale-record rates. | Define the minimum Light consolidation loop only after observing which failures task-close transfer actually produces. |

## 13. Challenge decisions

- **CH-D1 — Eliminate X4 as specified.** Hidden sibling folders may be inactive caches/archives/fixtures, but cannot be competing runtime editions without becoming another contract-governed configuration.
- **CH-D2 — Preserve X1, X2, and X3 as conditional survivors.** X1 is not privileged; X2 and X3 answer legitimate independent-release and shared-change forces that H5's directory comparison does not settle.
- **CH-D3 — Split X5.** Preserve D4 clean-workspace/archive cutover as an optional high-risk migration profile; do not recommend C3 generation by default until M5 demonstrates proportionality.
- **CH-D4 — Require K1–K6 as a dependency system.** K1–K4 carry meaning, K5 establishes authority, and K6 supplies fail-closed conflict accounting. Unknown data is retained/reported rather than silently interpreted or discarded.
- **CH-D5 — Narrow the hypotheses.** H5 wins only against hidden runtime siblings; H6 is refuted as written; H7 remains provisionally supported; H8 requires a guided/adaptive formulation and direct TFW measurement.

## 14. Findings

### Found

- X1 survives only under the same strict authority, conflict, rollback, and conformance demands applied to X2/X3.
- X2 is the unexpected survivor: separate packages can provide clearer runtime/release authority while sharing a neutral contract.
- X3 remains a real alternative for frequent common changes, but overlay/variation complexity must be measured.
- X4 has no unexpected product-runtime survival; useful hidden storage requires explicit inactive status and therefore belongs under another configuration.
- X5's archive cutover is valuable, while generation is disproportionate until demonstrated otherwise.
- All K1–K6 pairs can coexist, but K5–K6 are control dependencies; missing authority makes conflict handling meaningless.
- Strict compatibility must not become destructive rejection: unknown legacy content needs explicit retention and a migration path.
- H5–H8 all require narrower wording or evidence boundaries; none supports the full original claim without qualification.

### Remaining

- M1–M8 are measurable but unexecuted; this iteration contains analysis, not implementation or user trials.
- The final topology choice cannot be made from repository aesthetics alone; common-change frequency, release independence, and migration fixtures remain decisive.
- The minimum Light consolidation behavior remains open until real task-close omissions/status errors are measured.
- H7 and H8 retain empirical clarity/effectiveness gaps that local HL designs and external transfer evidence cannot close.

## 15. Checkpoint

### Sufficiency

- [x] External sources were used in Challenge.
- [x] Briefing gaps were converted into surviving/eliminated configurations and bounded verdicts.
- [x] All 10 X1–X5 pairs were attacked.
- [x] All 15 K1–K6 pairs were attacked.
- [x] X1 received no softer standard than X2/X3.
- [x] X2/X3 were retained as real alternatives, X4 was tested for survival, and X5 proportionality was split into mechanism versus default configuration.
- [x] Incompatible pairs, surviving configurations, and an unexpected survivor are explicit.
- [x] H5–H8 received final Challenge verdicts and M1–M8 define measurable gaps.
- [x] Counter-evidence was sought for permissive compatibility, monorepo preference, product-line machinery, and universal pedagogy.
- [x] At least two stage decisions were made.
- [x] Metacognitive check completed: the new result is not simply that visible editions win; separate packages unexpectedly survive, and archive cutover survives independently of generation.

**Stage complete:** YES

**Blocking questions:** None.

**Recommended next action:** Synthesize iteration 1 into `research/iter1/RES.md`: carry CH-D1–CH-D5, the conditional survivor set, H5–H8 verdicts, and M1–M8 gaps into decisions/hypotheses/recommendations without modifying the parent HL; then STOP at `[ITERATION_COMPLETE]`.

**Coordinator record:** Challenge checkpoint accepted on 2026-08-08; Synthesis authorized.
