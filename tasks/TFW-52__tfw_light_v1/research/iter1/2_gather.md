# Gather — "What do we NOT know?"

> **Mindset:** Explorer — map the space before selecting an answer.
> **Parent HL:** `tasks/TFW-52__tfw_light_v1/HL-TFW-52__tfw_light_v1.md`
> **Goal:** Map the product-spine, edition-topology, migration, selection, guidance, and consolidation decision space for H5–H8 without prematurely collapsing alternatives.

## 1. Source and method boundary

This stage used three deep-research loops:

1. **Historical-content loop:** inspect early repository trees and artifact bodies, not commit subjects, then compare them with TFW-51 and current Full.
2. **Guidance/consolidation loop:** audit TFW-51 and INNO-6/8/12/13 separately for scaffolding, practice, retrieval, and durable-memory mechanisms.
3. **Topology/challenge loop:** map independent topology, governance, migration, selection, and pedagogy dimensions; add external evidence and explicit counter-evidence.

Required local evidence was read from:

- early TFW artifacts at commits `45fd1b0`, `6afc8b5`, `d297fec`, and the first `.tfw` generation around `85e4217`;
- current `.tfw`, especially `.tfw/README.md`, `.tfw/conventions.md`, and `.tfw/workflows/knowledge.md`;
- `tasks/TFW-51__tfw_light_ru/` (`HL`, starter `README.md`, `AGENTS.md`, `TASKS.md`, and `memory/PROJECT.md`);
- `D:/projects/research/innoforce-ai-first/tasks/INNO-6*/HL*.md`;
- `D:/projects/research/innoforce-ai-first/tasks/INNO-8*/HL*.md`;
- `D:/projects/research/innoforce-ai-first/tasks/INNO-12*/HL*.md`;
- `D:/projects/research/innoforce-ai-first/tasks/INNO-13*/HL*.md`.

The local evidence set exceeds the stage's 15-file soft limit because the four specified INNO HLs, the full TFW-51 starter, and multiple historical transitions are mandatory and cannot be represented faithfully by commit metadata alone.

## 2. Historical invariant audit: artifact contents, not commit subjects

### 2.1 What early artifacts actually contained

| Historical state | Artifact-body evidence | What it establishes | What it does **not** establish |
|---|---|---|---|
| `45fd1b0` — `README.md`, `AGENTS.md`, `TASK.md`, `STEPS.md` | `README.md` frames chat knowledge evaporation and files as durable traces. `TASK.md` defines objective, DoD, risks, and the `Context → Analysis → Action` loop. `STEPS.md` is a compact iteration/progress log. `AGENTS.md` defines context intake, working modes, trace-first conduct, and continuation summaries. | Purpose/context, bounded and checkable work, persisted trace/progress, and continuation by a later session are present from the beginning. | No formal knowledge-candidate workflow, no edition topology, no named Working Backwards mechanism, and no invariant artifact names beyond that version. |
| `6afc8b5` — adds `AI_ENTRY_POINT.md` | The entry point reads canon and materializes chat-specific `AGENTS.md`, `README.md`, `TASK.md`, and `STEPS.md`; it limits onboarding questions and specifies a summary protocol. | Portability and guided bootstrapping were explicit early concerns. | Materializing duplicate control files is not evidence that duplication is a desirable current topology; it is historical counter-evidence about drift and ambiguity. |
| `d297fec` — v2 meta conventions and HL/TS/RF | `00_meta/HL_conventions.md` states reproducibility, traceability, continuation, a minimum artifact set, strict read order, quality/safety rules, and introduces HL/TS/RF. | The semantic spine survives while artifact richness increases. | The file is itself truncated mid-heading, showing that a prescribed structure can be incomplete and that file presence is not proof of operational guidance. Formal consolidation still is not an early invariant. |
| `85e4217` era — first `.tfw` tree | The tree moves conventions, glossary, templates, and workflows under `.tfw` while legacy root files still coexist. | A managed framework/runtime boundary emerges, with more formal roles and lifecycle stages. | Coexistence demonstrates migration ambiguity: multiple readable control surfaces can compete unless authority and precedence are explicit. |

### 2.2 Cross-generation semantic matrix

Legend: **strong** = explicit and operational; **partial** = present but lightly specified; **absent** = no meaningful mechanism found.

| Candidate invariant | Early v1 | v2 | TFW-51 Light prototype | Current Full | Gather inference |
|---|---:|---:|---:|---:|---|
| Human-readable purpose and current context | strong | strong | strong | strong | Stable semantic invariant. |
| Bounded work with an observable completion condition | strong (`TASK`, DoD) | strong (`HL`/`TS`) | strong (task board, criteria, validation) | strong (HL/TS/RF/REVIEW) | Stable semantic invariant; exact artifact is variable. |
| Persisted trace of work, decisions, or progress | strong (`STEPS`) | strong | strong (task-local `TRACE.md`) | strong (artifact chain and evidence) | Stable semantic invariant; trace depth is variable. |
| Later-session continuation from files | strong | strong | strong | strong | Stable semantic invariant. |
| Reusable project context beyond one task | partial | partial | strong (`memory/PROJECT.md`) | strong (`KNOWLEDGE.md`, topic files/state) | Stable direction, but storage and verification differ. |
| Source/verification discipline | partial | stronger | strong by domain and checklist | strong and role-gated | Important common capability, not identical mechanism. |
| Formal knowledge consolidation | absent | absent | partial, task-close instruction only | strong, separate candidate/consolidation workflow | **Not** an early invariant; higher-discipline mechanism. |
| Formal roles, WAIT gates, review separation | absent | partial | absent/light | strong | Edition-specific assurance mechanism. |
| Working Backwards as the named task method | absent | absent | absent as a named invariant | available in current planning practice, not the whole historical spine | **Not** demonstrated as a historical invariant. |
| Exact filenames or one directory layout | changes between generations | changes | changes | changes | Not an invariant. |

### 2.3 Historical core that remains defensible

The content evidence supports a name-neutral core:

`purpose/context → bounded, checkable work → persisted trace/outcome → reusable continuation context`

This is narrower and better supported than H6's literal `goal → Working Backwards task → trace → knowledge` formulation. Working Backwards, formal knowledge promotion, role separation, and gates remain plausible edition mechanisms, but the early artifact bodies do not justify calling them universal historical invariants.

Counter-evidence retained:

- v1 had continuation summaries and traces but no formal consolidation layer;
- v2 added structure yet included a truncated convention file;
- the first `.tfw` generation coexisted with legacy root controls;
- therefore, additive files alone do not guarantee coherent authority, completeness, or operational compatibility.

## 3. Independent decision dimensions

No recommendation is made in Gather. Alternatives below remain live unless marked as contradicted by direct evidence; none is eliminated solely for being less convenient.

### Dimension A — Product-spine granularity

| Alternative | Definition | Supporting evidence | Risk / counter-evidence | What would distinguish it later |
|---|---|---|---|---|
| A1. Exact named sequence | `goal → Working Backwards task → trace → knowledge` is the shared contract. | Strongly legible product narrative; aligns with the TFW-52 draft thesis. | Working Backwards and formal knowledge are absent from early artifact bodies. It overstates history and may force Light to contain Full concepts. | Show that every edition can enact each named stage without semantic dilution. |
| A2. Name-neutral semantic contract | Shared contract is purpose/context, bounded/checkable work, persisted trace/outcome, and reusable continuation context. | Present in every inspected generation. Preserves the actual historical invariant while allowing different artifacts. | May be too abstract to constrain migration or compatibility. | Define observable obligations and prove that different edition artifacts satisfy them. |
| A3. Compatibility/schema contract | Common spine is a machine- or checklist-readable manifest mapping purpose, task, trace, outcome, and knowledge fields. | Could support mechanical migration and validation across layouts. | No such schema exists in early evidence; risks designing infrastructure before product comprehension. | Prototype a small mapping and measure ambiguity/failure cases. |
| A4. Independent edition contracts | Each edition is independently coherent; only documentation links them. | Maximizes local simplicity and permits different operating models. | Weakens H6, makes migration and shared evolution expensive, and increases semantic drift. | Estimate duplicated maintenance and cross-edition mapping cost. |

### Dimension B — Source topology

| Alternative | Definition | Supporting evidence | Risk / counter-evidence | What would distinguish it later |
|---|---|---|---|---|
| B1. Same repository, visible `editions/<edition>/` | Light, Assisted, and Full live as visible sibling trees. | One history and review surface; easy cross-edition comparison; consistent with a product-line asset view. | Users may confuse source packages with the active installed runtime; repository growth and release coupling remain. | Test install/upgrade clarity and active-runtime detection. |
| B2. Same repository, hidden root siblings | `.tfw-light/`, `.tfw-assisted/`, `.tfw/` coexist at root. | Directly mirrors runtime naming and may simplify copying. | Multiple hidden control trees create precedence ambiguity; historical legacy/current coexistence already shows this failure mode. | Define and test unambiguous authority and adapter behavior. |
| B3. Separate repositories/packages | Each edition has independent versioning and distribution. | Clean release/access boundaries and smaller installations; separate lifecycle when products diverge. | Cross-edition drift, duplicated fixes, harder atomic migrations, and fragmented history. | Compare release independence needs with synchronization cost. |
| B4. Hybrid modules/submodules/generated packages | Common source plus independently delivered edition packages. | Could combine shared change control with independent release surfaces. Git submodules explicitly preserve separate histories while composing repositories. | Adds tooling and contributor complexity; generated output may obscure authorship and source of truth. | Prototype contribution, release, and upgrade flows, not just repository layout. |

### Dimension C — Variant governance and evolution

| Alternative | Definition | Supporting evidence | Risk / counter-evidence | What would distinguish it later |
|---|---|---|---|---|
| C1. Clone-and-own | Copy a baseline, then edit each edition independently. | Fast start; each edition remains locally understandable. | External empirical work reports increasing maintenance and reuse-tracking difficulty as variants grow. Fix propagation becomes manual. | Model three representative cross-edition changes and count touches/conflicts. |
| C2. Canonical shared core plus overlays | One common semantic/asset core; editions add or override explicit variable parts. | Product-line research treats shared assets and controlled propagation as the central evolution problem. | Overlay rules can become implicit and hard to debug; a shared core can bloat to lowest-common-denominator abstractions. | Define variation points and demonstrate transparent composition. |
| C3. Generated editions from a schema/template model | Edition trees are produced from one declarative model. | Strong consistency and mechanical validation/migration potential. | Generation infrastructure may exceed Light's product value; generated files can become hostile to manual maintenance. | Build the smallest generator and evaluate edit/review ergonomics. |
| C4. Independent artifacts with compatibility checks | Keep hand-authored editions, enforce only a cross-edition contract/test suite. | Preserves clarity in each edition while detecting semantic divergence. | Tests can lag or validate only surface compatibility; shared fixes are still duplicated. | Specify behavioral compatibility tests and their maintenance owner. |

### Dimension D — Migration contract

| Alternative | Definition | Supporting evidence | Risk / counter-evidence | What would distinguish it later |
|---|---|---|---|---|
| D1. Pure additive copy | Add new edition files/directories; never rename or reinterpret old content. | Lowest destructive risk; matches H6's intuitive promise. | Historical coexistence shows that additive controls can create competing authorities. Additive structure is not necessarily additive semantics. | Run migrations on representative Light and legacy fixtures and inspect ambiguity. |
| D2. Explicit one-time converter/map | A versioned mapping identifies old sources, transforms fields, and records decisions/conflicts. | Makes semantic changes auditable; supports validation and rollback planning. | Converter ownership and long-term support add cost; automated mappings may encode wrong assumptions. | Define failure classes and require conflict surfacing instead of silent conversion. |
| D3. Neutral interchange manifest | Editions import/export a small common representation of purpose, tasks, traces, and durable context. | Decouples topology from semantic portability. | New abstraction is not evidenced historically and may omit edition-specific meaning. | Round-trip fixtures across all three editions without material loss. |
| D4. New workspace plus linked archive | Do not mutate in place; initialize target edition and link/import selected old traces. | Strong rollback and preservation; avoids ambiguous mixed runtimes. | More user effort, possible fragmented continuity, and weaker "mechanical" migration claim. | Measure transfer completeness and operator burden. |

### Dimension E — Edition selection signal

| Alternative | Definition | Supporting evidence | Risk / counter-evidence | What would distinguish it later |
|---|---|---|---|---|
| E1. Person/team maturity labels | Beginner → Light, growing → Assisted, mature → Full. | Easy to communicate and superficially intuitive. | Conflates capability with work needs; can stigmatize users and misroute experts doing low-risk work. | Cross-department vignette test with people of equal skill but different work. |
| E2. Work-characteristic score | Select by repeatability, participants/hand-offs, error cost, assurance need, and knowledge lifetime. | NASA tailoring explicitly varies required process/products by project type, complexity, and risk rather than operator identity. | Multi-factor scoring may impose decision burden before users understand the framework. | Test whether a short scorecard yields stable choices across departments. |
| E3. Observable escalation triggers | Start light; escalate after repeated failures, coordination load, audit need, or long-lived knowledge demand. | Avoids premature process; connects added discipline to experienced pain. | Reactive selection may escalate only after preventable loss; trigger thresholds can be subjective. | Define measurable triggers and test them on historical tasks. |
| E4. Required-outcome/assurance tier | Choose the smallest edition that produces the evidence, review independence, and continuity required by the work. | Directly ties artifacts to outcome obligations and is domain-neutral. | Users may not know assurance needs in advance; can reproduce compliance jargon. | Translate tiers into plain-language scenarios and observe choice accuracy. |

### Dimension F — Learning sequence

| Alternative | Definition | Supporting evidence | Risk / counter-evidence | What would distinguish it later |
|---|---|---|---|---|
| F1. Explain all four mechanics, then practice | Present the whole model first. | Provides a stable conceptual map; INNO-8 explicitly says "terminology first." | High abstraction and working-memory load; delayed value; conflicts with INNO-6/13 artifact rhythm. | Compare first successful trace time and delayed recall. |
| F2. Bounded attempt → name mechanism → guided repeat → compare trace | Experience a small problem before formal explanation, then consolidate immediately. | Productive-failure evidence supports problem solving before instruction under designed conditions. INNO-13 uses experience/analogy before precise terms inside a mapped topic. | Productive-failure results have learner/age/prior-knowledge boundaries; minimal guidance can fail. | Specify timebox, scaffold, consolidation, and fallback; test across prior-knowledge levels. |
| F3. Mental model/terms → demo → hands-on → review/retrieval | Give a compact map, show the behavior, let users practice, then retrieve and review. | Directly matches INNO-8 and INNO-13; INNO-12 supports explicit retrieval. | Can still become lecture-heavy if the map/demo expands; "experience first" is no longer literal. | Cap orientation time and require an observable artifact plus delayed retrieval. |
| F4. Diagnostic/adaptive sequence | Prior knowledge or task condition chooses F2 or F3, with shared guided practice and retrieval. | Reconciles productive-failure boundary conditions and mixed INNO designs. | Adds onboarding complexity and needs a reliable diagnostic. | Test a two- or three-question routing diagnostic against observed performance. |

### Dimension G — Reinforcement and consolidation

| Alternative | Definition | Supporting evidence | Risk / counter-evidence | What would distinguish it later |
|---|---|---|---|---|
| G1. Task-close transfer only | At closure, move durable facts/decisions into project memory. | TFW-51 explicitly instructs this and keeps the starter compact. | No candidate state, contradiction handling, deduplication, staleness, or proof that transfer occurs. | Close several tasks and audit omission/duplication rates. |
| G2. Immediate retrieval plus trace review | Quiz/restate mechanics and compare the saved artifact immediately. | INNO-12's strongest field-reported block was a live control quiz; INNO-13 adds recall/review/trace. | Immediate success does not prove delayed retention or correct future use. | Add a delayed follow-up check. |
| G3. Spaced retrieval plus periodic consolidation | Revisit mechanics later and periodically promote verified task knowledge. | Retrieval-practice research shows delayed retention advantages; current `.tfw/workflows/knowledge.md` supplies candidate, dedupe, contradiction, verification, and staleness machinery. | Too heavy for Light if copied intact; scheduled routines can become ceremony. | Design a minimal cadence and compare value with overhead. |
| G4. Artifact-only reinforcement | Producing the trace is sufficient; no formal recall or consolidation loop. | Lowest overhead and consistent with learning by doing. | INNO-12/13 and retrieval research provide direct counter-evidence: production and immediate familiarity do not establish retention. | Delayed unaided reproduction test. |

## 4. Guidance and consolidation audit

### 4.1 TFW-51 starter

| Area | Evidence found | Strength | Gap / counter-evidence |
|---|---|---:|---|
| First-run guidance | `AGENTS.md` supplies read order, no-more-than-three onboarding questions, a full task cycle, and a complete trace template. | strong | It relies on the agent following prose; no structural verification of onboarding behavior. |
| In-task scaffolding | Source rules vary by task domain; validation and completion checklists are explicit. | strong | Guidance is broad rather than exercised through a worked end-to-end example. |
| Observable output | `TASKS.md` status flow plus task-local `TRACE.md`; README states that work is incomplete until the result is saved in files. | strong | Board and trace consistency remain manual. |
| Durable context | `memory/PROJECT.md` separates project card, agreements, confirmed knowledge, decisions, and open questions, with source/date columns. | medium/strong | No candidate/confirmed state transition beyond prose, and no systematic contradiction or staleness process. |
| Consolidation | Agent is told to transfer durable knowledge when a task closes. | partial | This is aspirational/manual: no cadence, ownership gate, deduplication, contradiction handling, provenance sufficiency test, or evidence that transfer happened. |

### 4.2 INNO HL evidence

| Source | Guidance/scaffolding found | Consolidation/retrieval found | Implication and counter-evidence |
|---|---|---|---|
| INNO-6 | Live demos, executive language, a decision matrix, playbook, A4 materials, modular/self-contained blocks, and concrete artifacts. Starter files support autonomous continuation. | Continuation pack and saved artifacts; no explicit longitudinal retrieval loop. | Strong evidence for show-and-do guidance and artifact continuity. Weak evidence for durable learning consolidation. |
| INNO-8 | Three-week progression: mechanics/language → management/delegation → build/prove. Every exercise must state goal, input, expected output, criteria, and fallback. Friday theory, Saturday workshop, Sunday homework/support. | Supported homework, recordings, and final assistant/pet project. | Direct counter-evidence to a universal "experience first" claim: this HL explicitly requires terminology first. It still supports repeated guided production. |
| INNO-12 | Reuses a proven seminar and formalizes its strongest observed live block. Supplies terms policy, canonical answers, procedure, and fallback. | NotebookLM control quiz requires participants to retrieve and speak an answer; retained terms are a success condition. | Strongest field-based support for immediate retrieval, but only a single immediate check; delayed retention is unproven. |
| INNO-13 | Daily sequence is `RECALL → MENTAL MODEL → DEMO → HANDS-ON → REVIEW → DECISION/TRACE`. Participants act every 20–35 minutes. Terms are mapped before depth; within a topic, experience/analogy ends with precise naming and retrieval. | Daily recall/review/trace, saved artifact every day, and a later feedback/evidence phase. | Strong support for a hybrid sequence, not pure discovery. It is still an HL/pilot design, so efficacy is a hypothesis until execution evidence exists. |

### 4.3 Guidance/consolidation synthesis

The required local sources converge on four distinct functions that should not be collapsed:

1. **Orientation:** a compact terminology or mental-model map prevents blind exploration.
2. **Guided production:** demo, bounded hands-on work, explicit criteria, and fallback create a usable artifact.
3. **Retrieval/review:** the learner must restate, check, or reproduce the mechanism after using it.
4. **Knowledge consolidation:** durable project facts/decisions must be selected, verified, deduplicated, and kept current.

TFW-51 is strong on orientation, procedural guidance, and saved output, but only partial on function 4. INNO-12/13 strengthen function 3. Current Full has the strongest function-4 mechanism, but copying that workflow wholesale into Light would contradict the Light constraint; the open question is the minimum sufficient mechanism, not whether consolidation exists conceptually.

## 5. External research and counter-evidence

Research limitation: one follow-up web-search request did not return in a useful time window and was not repeated. The stage therefore relies on the already retrieved primary/official sources and DOI-indexed research below; this limits breadth, not the ability to map alternatives at Gather, and creates no blocking question.

### 5.1 Product topology and evolution

| Source | Relevant evidence | Effect on the option space |
|---|---|---|
| SEI, *The Evolution of Product Line Assets* — https://insights.sei.cmu.edu/library/the-evolution-of-product-line-assets/ | Shared product-line assets evolve; changes can propagate to dependent products, so evolution and impact must be anticipated and controlled. | Supports a common-source/variation-point model, but also warns that a shared repository by itself is not governance. Keeps B1/B4 and C2/C4 live. |
| Git documentation, *Submodules* — https://git-scm.com/book/en/v2/Git-Tools-Submodules | A repository can compose another repository while preserving independent history/version choice. | Demonstrates that separate lifecycle plus one composition surface is technically viable. Keeps B3/B4 alive; does not prove it is understandable for TFW users. |
| Patzke et al., clone-and-own vs. platform/product-line empirical study — https://doi.org/10.1016/j.infsof.2020.106444 | The product-line approach was more effective/efficient/satisfying in the study, while also requiring more checking and exposing more possibilities than engineers needed. | Counter-evidence against both extremes: clone-and-own drift is real, but a richer platform can impose option and checking burden. Keeps C1–C4 open pending TFW-scale tests. |
| KAIST et al., clone-and-own migration study — https://doi.org/10.1093/comjnl/bxaf134 | Clone-and-own starts quickly, but maintenance and reuse tracking become harder as variants grow; migration requires identifying and integrating cloned artifacts. | Challenges a purely additive-copy interpretation of H6 and strengthens the need for explicit mapping/compatibility evidence. |

### 5.2 Edition selection

| Source | Relevant evidence | Effect on the option space |
|---|---|---|
| NASA, *Systems Engineering Handbook*, tailoring guidance — https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf | Process and required technical products are tailored to project type, complexity, risk, and lifecycle needs. | Supports work-context dimensions over personal maturity labels. Does not yet prove that one scorecard is understandable across TFW departments. |

### 5.3 Learning and retention

| Source | Relevant evidence | Effect on the option space |
|---|---|---|
| Kapur, *Productive Failure in Learning Math* — https://doi.org/10.1080/00461520.2014.917555 | Problem solving before instruction can improve conceptual understanding when the failure is intentionally bounded and followed by consolidation. | Supports F2 under explicit conditions, not unguided discovery. |
| Kirschner, Sweller, and Clark, minimal-guidance review — https://doi.org/10.1207/s15326985ep4102_1 | Minimally guided instruction can overload novices and underperform guided instruction. | Direct counter-evidence against a universal experience-first or artifact-only path; supports orientation/scaffolding/fallback. |
| Mazziotti et al., productive-failure boundary study — https://doi.org/10.1038/s41539-019-0041-5 | Productive-failure effects were mixed for younger learners; age, prior knowledge, and collaboration are boundary conditions. | Keeps F3/F4 live and requires a diagnostic or safe default rather than one universal sequence. |
| Roediger and Karpicke, *Test-Enhanced Learning* — https://doi.org/10.1111/j.1467-9280.2006.01693.x | Restudy can win immediately, while retrieval testing produces stronger retention after days. | Supports delayed retrieval as a separate mechanism from immediate practice and challenges G1/G4 as sufficient learning reinforcement. |

## 6. Hypothesis probes at Gather

| Hypothesis | Gather status | Supporting evidence | Counter-evidence / unresolved test |
|---|---|---|---|
| **H5:** same-repo `editions/` is safer and clearer than root hidden siblings or separate repos | **OPEN; plausible but not established** | Same history/review surface and product-line change visibility favor B1. Historical coexistence makes B2 risky. | Separate repos/hybrid modules preserve independent lifecycle; same-repo package vs active runtime may confuse users. Safety/clarity requires fixture and user-flow tests. |
| **H6:** all editions share `goal → Working Backwards task → trace → knowledge`, enabling additive mechanical migration | **PARTIAL / wording challenged** | Every generation supports purpose/context, bounded work, persisted trace/outcome, and continuation context. | Working Backwards and formal consolidation are not early invariants. Additive coexistence can produce authority conflicts. Mechanical migration needs an explicit semantic mapping and failure behavior. |
| **H7:** edition choice by work characteristics is clearer than by person maturity | **PROVISIONALLY SUPPORTED** | Historical editions vary assurance and continuity mechanisms; NASA tailoring supports project/risk/complexity signals. INNO programs show the same audience can need different structures by outcome. | Cross-department comprehension and scoring burden are untested. Trigger-based and outcome-tier alternatives remain live. |
| **H8:** `do it → name it → repeat it → consolidate it` is more effective than explaining all mechanics first | **PARTIAL; pure reading is contradicted** | INNO-6/12/13, productive-failure evidence, and retrieval research support bounded action, naming, repeat/review, and consolidation. | INNO-8 says terminology first; INNO-13 starts with recall/mental model; minimal-guidance and boundary evidence reject universal unguided experience-first. A hybrid/adaptive sequence is the live interpretation. |

## 7. Gather decisions

- **G-D1 — Carry a name-neutral invariant forward.** Extract will treat `purpose/context → bounded/checkable work → persisted trace/outcome → reusable continuation context` as the historically supported spine. It will keep Working Backwards and formal knowledge promotion as candidate mechanisms rather than assume they are universal.
- **G-D2 — Keep topology families independent and live.** Same-repo visible editions, root hidden siblings, separate packages, and hybrid composition remain candidates. Governance (clone-and-own, overlays, generation, compatibility checks) will be evaluated separately from repository location.
- **G-D3 — Separate migration structure from semantic compatibility.** "Additive" will not be used as a synonym for "safe." Extract must define authority, mapping, conflicts, and rollback/continuity obligations before testing H6.
- **G-D4 — Carry a hybrid/adaptive pedagogy model forward.** Extract will compare a compact orientation plus bounded experience, naming, guided repeat, retrieval/review, and consolidation. It will not assume a universal experience-first sequence.
- **G-D5 — Keep retrieval and project-knowledge consolidation distinct.** Remembering the method and promoting durable project facts are different loops with different evidence and cost.

## 8. Findings

### Found

- The strongest historical invariant comes from artifact contents, not filenames: purpose/context, bounded/checkable work, persisted trace/outcome, and file-based continuation.
- The literal Working Backwards-to-knowledge sequence is not historically universal; H6 currently overclaims the invariant.
- Formal consolidation appears late: TFW-51 requests task-close transfer but lacks the candidate, verification, contradiction, deduplication, and staleness machinery found in current Full.
- Repository topology and variant governance are separate decisions. At least four topology families and four governance models remain plausible.
- Pure additive copying is structurally non-destructive but can be semantically unsafe when multiple authorities coexist.
- Work characteristics—repeatability, hand-offs, error cost, assurance, and knowledge lifetime—have stronger evidence as selection inputs than personal maturity labels, but the best presentation remains untested.
- Required INNO evidence favors guided, artifact-producing, retrieval-aware learning. It contradicts both "explain everything first" and a universal unguided "experience first" rule.
- Immediate retrieval and durable project consolidation solve different problems; an edition model may need both at different intensities.

### Remaining unknowns

- Which topology/governance pairing has the lowest total ambiguity and maintenance cost for actual TFW install, upgrade, and contribution flows?
- What is the smallest observable cross-edition contract that is strong enough for migration without importing Full terminology into Light?
- Can Light-to-Assisted-to-Full migration be round-tripped or at least verified on representative legacy/current fixtures without silent semantic loss?
- Which selection interface—scorecard, triggers, or outcome/assurance tier—is most consistently understood across departments?
- What minimum retrieval and consolidation cadence produces retained behavior without turning Light into process ceremony?
- How should prior knowledge route learners between bounded attempt-first and compact-model-first sequences?

## 9. Checkpoint

### Stage sufficiency

- [x] At least 3 alternatives are documented for every decision dimension.
- [x] Alternatives are independent across product spine, topology, governance, migration, selection, learning sequence, and consolidation.
- [x] Historical invariants were extracted from artifact bodies rather than commit subjects.
- [x] TFW-51 guidance and consolidation were audited separately.
- [x] INNO-6/8/12/13 guidance and consolidation/retrieval were audited separately.
- [x] External research and counter-evidence were added in this stage.
- [x] At least two stage decisions were made and H5–H8 each received a Gather probe.
- [x] Metacognitive check completed: the main risk is conflating a memorable product narrative with the historically evidenced semantic core; all major topology alternatives remain live.

**Stage complete:** YES

**Blocking questions:** None.

**Recommended next action:** Run `/tfw-research` Extract for iteration 1: reduce the independent dimensions into a small set of coherent topology/governance/migration/pedagogy configurations, define explicit invariant and compatibility criteria, and test H5–H8 against local fixtures and counter-evidence without changing the parent HL.

**Coordinator record:** Gather checkpoint accepted on 2026-08-08; Extract authorized.
