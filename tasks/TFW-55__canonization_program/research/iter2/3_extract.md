# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW-55](../../HL-TFW-55__canonization_program.md)
> Goal: Structure the category, authority, trace-floor, terminology, exposition, Editions, and consumption alternatives into frozen matched configurations without collecting critique evidence or selecting a winner.

## Configuration Space

The table keeps Gather's seven dimensions independent. It lists coherent configurations that expose material alternatives; it is not the Cartesian product and makes no viability judgement. **C1/C3/C4/C9 are carried unchanged and remain unranked.** D5 human authority is a normative/scope contract shared by every row, not a novelty claim. Public topology is held constant only inside matched D9/D4/D7 families; D2 may add or replace a selector, including a minimal manifest.

| Config | D1 — primary category | D2 — authority selector | D3 — trace floor | D4 — public terminology | D7 — exposition route | D8 — Editions routing | D9 — consumption contract |
|---|---|---|---|---|---|---|---|
| **C1 Layered discipline** | C — discipline | A — corpus + essay + specification | C — selected continuity floor | A — self-aware + six capabilities | A — problem → Light → Assisted → Full | A — bounded proportional example | B — separate parity surfaces |
| **C3 Methodology first** | B — methodology | A — corpus + essay + specification | C — selected continuity floor | A — self-aware + six capabilities | C — branch by role/prior knowledge/risk | A — bounded proportional example | B — separate parity surfaces |
| **C4 Framework-only challenger** | A — practical framework + philosophical framing | A — corpus + essay + specification | C — selected continuity floor | C — inspectable/resumable | C — branch by role/prior knowledge/risk | B — usage/teaching surfaces | B — separate parity surfaces |
| **C9 Quiet semantics** | B — methodology | A — corpus + essay + specification | C — selected continuity floor | D — no umbrella public label | C — branch by role/prior knowledge/risk | B — usage/teaching surfaces | B — separate parity surfaces |
| **C10 Explicit hierarchy** | D — no single primary category; philosophy → method → reference framework | A — corpus + essay + specification | C — selected continuity floor | B — self-describing | C — branch by role/prior knowledge/risk | A — bounded proportional example | B — separate parity surfaces |
| **C11 Manifested framework** | A — practical framework | D — separate minimal authority/version manifest | C — selected continuity floor | C — inspectable/resumable | C — branch by role/prior knowledge/risk | B — usage/teaching surfaces | B — separate parity surfaces |
| **C12 Common-core framework** | A — practical framework | B — one versioned common semantic core | C — selected continuity floor | C — inspectable/resumable | B — direct to method/specification | B — usage/teaching surfaces | A — one common core |
| **C13 Task-local framework** | A — practical framework | C — active task-local source/status declarations | C — selected continuity floor | D — state six capabilities only | C — branch by role/prior knowledge/risk | B — usage/teaching surfaces | C — task traces/mechanics first |
| **C14 Provenance-minimal control** | A — practical framework | A — corpus + essay + specification | A — provenance only | C — inspectable/resumable | B — direct | B — usage/teaching surfaces | B — separate parity surfaces |
| **C15 Decision-record control** | A — practical framework | A — corpus + essay + specification | B — ADR-like context/decision/consequences | C — inspectable/resumable | B — direct | B — usage/teaching surfaces | B — separate parity surfaces |
| **C16 Universal-assurance discipline** | C — discipline | A — corpus + essay + specification | D — universal evidence/review/knowledge chain | A — self-aware | D — concept first | D — canonical Editions spine | A — one common core |
| **C17 Direct quiet methodology** | B — methodology | A — corpus + essay + specification | C — selected continuity floor | B — self-describing | B — direct | B — usage/teaching surfaces | B — separate parity surfaces |
| **C18 Self-aware framework** | A — practical framework | A — corpus + essay + specification | C — selected continuity floor | A — self-aware + six capabilities | C — role/risk branch | A — bounded proportional example | B — separate parity surfaces |
| **C19 Quiet discipline** | C — discipline | A — corpus + essay + specification | C — selected continuity floor | D — state capabilities only | C — role/risk branch | B — usage/teaching surfaces | B — separate parity surfaces |

**C10 normalization is strict.** D1-D is the mutually exclusive claim “no single primary category; an explicit philosophy → method → reference-framework hierarchy.” C10 must justify the necessity and boundaries of all three layers. It may not simultaneously be counted as C1 or C3 while escaping their discipline/methodology burden.

**Unanticipated configurations:** C18 shows that the public self-awareness term does not logically require a discipline/methodology category; C19 shows that a discipline claim does not require that term or the Editions bridge. C10 exposes a hierarchy option that is neither C1 nor C3. C11 keeps the framework-only identity while reopening a new authority surface only as a D2 control. These combinations were not proposed as complete candidates in the Briefing.

## Findings

### E1 — External labels describe different objects; they do not supply a universal category taxonomy

The sources' own labels are usable evidence about their objects, not a general decision rule for classifying TFW:

| Source | Self-description | Operational boundary | Extract implication |
|---|---|---|---|
| [Scrum Guide](https://scrumguides.org/scrum-guide.html) | “lightweight framework,” founded on theory and philosophy | Its core elements are essential; partial Scrum is not Scrum; other methods/practices can sit inside it | Mandatory composition and consequential exclusions are compatible with **framework**. This is the required counter-control against upgrading TFW's category merely because its boundary works |
| [W3C PROV-O](https://www.w3.org/TR/prov-o/) | W3C Recommendation and provenance ontology | Defines interoperable provenance classes/relations at several levels | Strong component overlap does not make an ontology a work method or decide TFW's category |
| [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) | Risk Management Framework with Govern/Map/Measure/Manage functions | AI-risk scope, roles, oversight, documentation, monitoring, and risk response | Framework can contain normative responsibilities and functions; human-authority overlap is not category evidence |
| [Diátaxis](https://diataxis.fr/) | systematic approach to documentation | Four content purposes/needs; implementation remains open | “Approach” can be systematic without establishing a framework/methodology taxonomy |
| Nygard ADR / docs-as-code / Nonaka / Hutchins | practice proposal, approach/philosophy, theory, and descriptive distributed-cognition analysis respectively | Each governs a different object | Their nouns track source purpose and disciplinary convention; they cannot be combined into an external ladder that discovers TFW's “true” category |

No official source in the bounded comparison provides a shared decision rule distinguishing `framework`, `methodology`, `discipline`, `approach`, `theory`, and `ontology` across domains. D1 is therefore a **calibrated positioning claim constrained by evidence**, not an externally discovered taxonomic fact. Sources can falsify overclaim (for example, “frameworks cannot have mandatory composition”) and expose burden, but cannot select C1/C3/C4/C9/C10 by vocabulary alone.

### E2 — Component overlap and consequential composition are now separate comparisons

The adjacent controls establish broad overlap:

- durable decision records and retained superseded history overlap ADRs;
- repository-native text, Git, review, and automation overlap docs-as-code;
- provenance/attribution overlap PROV-O;
- human responsibility, role differentiation, stop/deactivation, and risk scaling overlap NIST AI RMF;
- distributed project memory and explicit knowledge overlap Hutchins/Nonaka;
- role-specific explanatory surfaces overlap Diátaxis.

None of those overlaps answers whether the four-element **positive semantic floor** has a consequential composition:

| Floor element | Positive rule | Removal consequence under the provisional fixture |
|---|---|---|
| **F1 Purpose/authority** | Human purpose, context, intended result, acceptance owner, and stop responsibility are explicit | Work may be durable, but legitimate purpose, acceptance, and stop authority cannot be resolved |
| **F2 Bounded delegation** | AI task, role, constraints, and authority limit are visible | The boundary of delegated cognition cannot be reconstructed or audited |
| **F3 Selected durable trace** | Material sources/findings/decisions/rejections plus result/current state are selected; only material items are required | Result and material reasoning state disappear or raw transcript/provenance substitutes for useful continuity |
| **F4 Authoritative result/continuation** | Result location plus next action or explicit closed/no-next-action state is visible | A successor cannot tell what output governs or whether to resume, stop, or close |

The separate **R1 risk-scaling rule** says evidence, independent review, and verified knowledge are distinct assurance layers selected proportionally to risk. R1 is not a fifth mandatory artifact. Removing proportionality can make a design over-engineered while F1–F4 still pass.

The frozen ablations include two important controls:

- `NO_ALTERNATIVES` passes: a simple low-risk Light case with no material alternative is not rejected for failing to invent one. Sources, findings, decisions, and rejections are recorded only when material.
- `NO_RISK_SCALING` passes F1–F4 but fails R1: this prevents universal Full assurance from masquerading as the semantic floor.

These ablations show what the **provisional rule says breaks**. They do not prove that F1–F4 is the true or distinctive boundary. The synthetic policy/research cases test logical coherence and generalizability, not real-world non-code adoption.

### E3 — Category variants share a boundary, so primary-category burden remains visible

The frozen category family applies the same F1–F4 boundary and the same seven neutral cases to C1, C3, C4, C9, and C10. No TFW artifact names or founder intent appear in the cases.

| Candidate | Additional primary claim beyond the shared boundary | Burden that remains after correct case classification |
|---|---|---|
| **C1** | Transferable normative **discipline** | Explain what discipline adds as the best primary positioning rather than restating the framework boundary |
| **C3** | Organized transferable **methodology** | Explain what methodology adds that C4 does not already provide at lower assumption cost |
| **C4** | Practical prompt-and-files **framework** with philosophical framing | Explain the value without collapsing into “just documentation,” but does not need a higher-category proof |
| **C9** | Methodology with quiet public semantics | Carries C3's category burden even if terminology ambiguity is lower |
| **C10** | No single primary category; explicit philosophy→method→reference-framework hierarchy | Demonstrate why all three layers are necessary and non-redundant; cannot borrow C1/C3 status selectively |

If blinded bounded critiques apply the shared boundary equally across C1/C3/C4/C9, that result cannot establish a higher category and triggers the coordinator's C4 loss rule for primary positioning. If a higher-category packet improves boundary application, it is still only bounded model evidence and remains subject to Scrum's counter-control: an applicable boundary does not itself convert a framework into a methodology/discipline.

### E4 — D2 selector architectures are independent of matched public topology

D2 legitimately changes selector architecture; it is not frozen by the D9/D4/D7 topology control.

| D2 | What preserves history/evidence? | What selects stable meaning? | What selects mechanics? | Formal failure mode to test |
|---|---|---|---|---|
| **A Layered** | Corpus | Canonical essay | Living specification | Claim type or precedence is missing/ambiguous |
| **B Common core** | Corpus | One versioned core | Same core | Stable explanation and fast-changing mechanics overload/drift in one authority |
| **C Task-local declarations** | Corpus | Active trace's declared `meaning_source` | Active trace's declared `mechanics_source` | Missing/conflicting metadata or two active tasks select different current sources |
| **D Minimal manifest** | Corpus | Manifest mapping | Manifest mapping | A new selector drifts, duplicates links, or is not maintained |

All four can be logically deterministic if their declarations are complete. The four frozen scenarios—direct contradiction, semantic update, Russian derivative, and external-author citation—separate determinacy from cost. Sources/logic can identify whether an architecture has an explicit resolution rule; bounded model critique can test immediate application; only external-author use can show whether the maintenance and citation contract works in practice.

### E5 — Matched families freeze one manipulation at a time

The original v1 fixture is **rejected before run and produced no evidence**; its unchanged file/hash remain only for audit in [V1_REJECTED.md](fixtures/V1_REJECTED.md). The revised normative fixture is [frozen_design.v2.json](fixtures/frozen_design.v2.json), summarized in [README_V2.md](fixtures/README_V2.md), with integrity manifest [SHA256SUMS.v2](fixtures/SHA256SUMS.v2). v2 SHA-256 is `d7fdb413af669abdf92cb3c055f7a966db3d4daec58d2ac15c36e679805f0f7a`. JSON parsing, all hashes, mappings, schemas, source counts, and packet-load checks were verified after writing. **No critic or scorer run has occurred.**

| Family | Held constant | Manipulation | Frozen blind order | Evidence available only after Challenge |
|---|---|---|---|---|
| **Category** | Neutral cases, F1–F4, R1, exclusions, prompt, rubric | Primary category explanation: C1/C4/C10/C9/C3 | `Q7 → M2 → R5 → K8 → V1` | Model boundary application/ambiguity only; no ontological or human-category proof |
| **Ablation** | Provisional rule, questions, rubric | Remove one floor element; violate R1; or omit non-material alternatives | `Aster → Birch → Cedar → Dahlia → Elm → Fir → Gorse` | Immediate rule/minimality application; answer key is not truth evidence |
| **Authority** | Same four scenarios and evaluator | D2-B/A/D/C selector architecture | `Iris → Juniper → Kelp → Lotus` | Immediate precedence/rule accuracy and unresolved cases |
| **D9 agent route** | C4, P1–P6 exactly once, task, authority semantics, actual packet load, rubric | Mandatory agent entry route and surface partition: common core vs specification-first vs task-first/specification; unissued/optional surfaces are not sent | `Lark → Moss → Sage` | Immediate agent route definition/precedence/rule accuracy and actual issued load for this model; human-side D9 remains untested |
| **Terminology** | Six capabilities, non-sentience limit, sentence template, task, rubric | `self-describing project` vs `self-aware project` | `Tide → Vale` | Model-induced immediate ambiguity only; not human reception |
| **Exposition ordering proxy** | Six exact semantic blocks once each, equal payload budget, questions, rubric | Linear block order: direct-like vs role/risk-like vs problem/Editions-like framing | `Fjord → Grove → Haven` | Immediate ordering sensitivity only; cannot select D7/D8 or trigger A3 |

The predeclared seed `TFW55-I2-EXTRACT-2026-08-13-v1` is retained because v1 had zero runs; changing it during repair would create an opportunistic rerandomization. Label mappings and the SHA-256 ordering algorithm are frozen in v2. Every D9 agent packet actually delivered to the critic is mechanically equal at **2493 UTF-8 bytes, 246 whitespace words, two source surfaces, and P1–P6 exactly once**; optional/unissued ESSAY is not delivered. Every exposition-proxy packet is equal at **2211 bytes, 227 words, and B1–B6 once**. Terminology word budgets are equal; the expected five-byte term-spelling difference is recorded.

Each family now has an exact critic JSON schema. Each critic output is scored in a **separate isolated opaque scoring pass** that receives the opaque packet/output, programmatic checks, relevant neutral answer-key value, rubric, and scorer schema—but no C/D mapping, other variant, frozen-HL preference, founder intent, or coordinator recommendation. Mapping is revealed only after all required critic and scorer passes for the family finish. Mechanical JSON/schema/label/count/load/coverage checks run programmatically where possible.

The first complete family pass is an **adversarial probe**. Any material atom-score difference, ambiguity-count difference, or malformed/schema-invalid output forces exactly one second complete pass of the entire family with identical critic and scorer model/reasoning settings. Selective reruns and a third pass are forbidden. A difference becomes comparative evidence only if the same ordered difference or malformed class is confirmed in pass 2; otherwise it is an unstable observation. One all-equal valid pass supports only “difference not observed in this adversarial probe,” never equivalence.

Any later change to packet, prompt, answer key, schema, label, order, rubric, scorer, or replication rule invalidates the whole family and requires returning to Extract. C3 D9 sensitivity is not an adaptive v2 rerun: it requires a coordinator ruling that completed frozen C4 agent-route results plausibly depend on category wording, followed by a new frozen fixture and gate.

### E6 — Evidence-resolution map prevents model results from answering human questions

| Difference / claim | Primary/official sources + logic can resolve | Independent model-based bounded critique can resolve | Necessarily future human or field evidence |
|---|---|---|---|
| Individual component novelty | **Yes:** ADR/docs-as-code/PROV-O/NIST/etc. establish overlap | Not needed | No, unless studying adoption perception rather than novelty |
| F1–F4 internal coherence/minimality | **Partly:** ablation consequences and cross-Edition fit can expose redundancy/contradiction | **Partly:** consistent immediate application and ambiguity | Real non-code adoption and failure cases; synthetic cases cannot supply them |
| Framework vs methodology vs discipline vs hierarchy | **Only burden calibration:** official self-labels supply no universal taxonomy; Scrum refutes category elevation by boundary alone | Can test whether wording changes immediate boundary application, not the category's truth | Human-facing positioning/reception if the public category claim depends on reader interpretation |
| D2 authority selector | Can test formal determinacy, surface count, and maintenance implications | Can test immediate precedence/rule accuracy on frozen conflicts | External-author citation/update use over time |
| D9 consumption | Can verify proposition parity, actual issued packet load, and declared route | Can compare immediate mandatory **agent-route** rule accuracy, used issued units, and drift for the tested model | Human-side D9, human reading load/comprehension, and cross-tool/field agent robustness |
| `self-aware` terminology / A2 | Sources can identify anthropomorphic risk but not reception | Can reveal model-induced ambiguity only | **Required** for human reception, memorability, preference, and an A2 amendment trigger based on people |
| Exposition / Editions / A3 | Logic can expose duplication and keep observation/mechanism/outcome separate | v2 can test **linear ordering sensitivity only** | Staged progression, real role/risk branching, human comprehension/path preference; A3 cannot be triggered by this proxy; durable learning/retention/transfer remain outside this design |
| H2 independent boundary application | Sources define controls; logic defines cases and exclusions | Model runs can provide bounded non-human application evidence | Human readers are required if the final public claim is about independent human applicability |

This map implies that Challenge can narrow H1/H2/H4 and detect packet defects, but it must not convert a favorable model score into human reception, durable learning, or real adoption. A2 remains pending future human evidence if its amendment rationale is human reaction. The exposition ordering proxy is not a sufficient A3 trigger; A3 remains pending staged/branched and human evidence even if the proxy shows a replicated model difference.

### E7 — Pairwise incompatibilities and dependency structure

- **D1 A/B/C/D are mutually exclusive primary-positioning claims.** A document may discuss philosophy and method under any category, but only D1-D denies one primary category and asserts the three-layer hierarchy.
- **D2 and D9 are independent.** A manifest can coexist with any consumption contract; a common consumption core need not be the official selector. Keeping them separate prevents “everyone reads it” from becoming authority.
- **D3-C and R1 are complementary, not one payload.** The floor says what continuity must survive; R1 chooses additional assurance by risk.
- **D4 and D1 are independent.** C18 and C19 demonstrate that self-awareness language neither proves nor requires a higher category.
- **D7 ordering and D8 Editions destination are related but not identical.** Editions can be a usage example even when the essay starts direct-to-method; a problem-led route need not make Editions the canonical spine.
- **D9 tests freeze topology only inside the family.** D2-D may add a manifest outside that test without contradiction.

The strongest hidden dependency is between **category burden and C4**: because every category packet currently uses the same consequential boundary, higher-category candidates need evidence beyond equal case classification. The strongest hidden independence is between **public terminology and primary category**, exposed by C18/C19.

### E8 — Focused OODA result

**Observe.** Official sources use category words according to their own governed objects, not a shared taxonomy. Scrum explicitly combines philosophy/theory, mandatory composition, exclusions, and extensibility while remaining a framework. The Gather boundary becomes clearer when F1–F4 are separated from R1 and ablated.

**Orient.** The extractable decisions are not “which noun sounds strongest.” They are: whether the composition is coherent/minimal; whether any higher-category wording improves consequential application beyond C4; which selector architecture resolves claims; whether mandatory agent routes and terminology change immediate model accuracy without content confounds; and whether linear ordering produces only a proxy signal rather than an exposition-architecture verdict.

**Decide.** Revised Extract is sufficient for focused mode. The corrected configuration count is fourteen; D1-D is mutually exclusive; floor and risk rule are deconfounded; v1 is rejected with zero evidence; v2 freezes actual agent-route packets, family-specific critic/scorer schemas, opaque scoring, full-family replication, eight external source versions, and hash-verified mechanics; and the evidence-resolution map states what Challenge cannot claim.

**Act.** Recommend `close stage`. After the coordinator gate—and only then—Challenge may run the frozen isolated model critiques, apply one falsification scheme to C1/C3/C4/C9/C10 and the controls, separate evidence viability from frozen-HL compatibility, and preserve every raw run/score.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Fourteen coherent configurations cover all D1/D2/D3/D4/D7/D8/D9 alternatives; C1/C3/C4/C9 remain unchanged and unranked. | Challenge must eliminate/narrow configurations with explicit falsifiers; Extract selects none. |
| C10 makes the hierarchy claim explicit and mutually exclusive; C18/C19 expose category/terminology independence. | D1 remains calibrated positioning because the external sources supply no universal category taxonomy. |
| F1–F4 form the positive floor; R1 is a separate proportional-assurance rule; seven ablations include pass controls for no alternatives and low-risk Light. | Challenge must distinguish rule coherence from evidence that the boundary is true or adopted. |
| Exact category/ablation/authority/D9-agent-route/terminology/exposition-ordering-proxy v2 fixtures, family schemas, scorer protocol, and replication rule are frozen and hash-verified. | No critic/scorer evidence exists yet; Challenge runs require coordinator authorization and cannot alter v2. |
| Sources/logic, bounded model critique, and future human/field evidence now have explicit claim boundaries. | Human terminology reception, human boundary applicability, field adoption, and durable learning cannot be closed by model runs. |

**Sufficiency:**
- [x] External source used? — the 2020 Scrum Guide and W3C PROV-O were rechecked as mandatory category and provenance controls; NIST and Diátaxis remain normalized official controls.
- [x] Briefing gap closed? — category/composition, selector architectures, ablations, D9 agent-route, terminology, exposition ordering proxy, Editions, cross-domain limitations, evidence lanes, opaque scoring, and replication are structured without collecting results.
- [x] Configuration Space built from Gather dimensions? — all seven dimensions appear in fourteen coherent configurations; unanticipated C10/C18/C19 are explicit.

### Questions for `Coordinator | TFW-55`

1. Accept the corrected fourteen-configuration space, including mutually exclusive C10 plus C18/C19 controls, with C1/C3/C4/C9 still unranked?
2. Authorize frozen fixture `TFW55-I2-EXTRACT-v2`, SHA-256 `d7fdb413…805f0f7a`, for Challenge under its full-family replication and isolated opaque-scoring rules?
3. Accept that D9 v2 tests mandatory agent routes only and exposition v2 is only a linear-ordering proxy, leaving human-side D9 and A3 triggers to future human/field evidence?

Stage complete: YES
→ User decision: **Pending revised coordinator gate; researcher recommends `close stage` and v2 freeze authorization.**

### Extract refinement record

- Coordinator verdict on v1: `refine`; Gather does not repeat and v1 is not authorized.
- Corrected the configuration count from fifteen to fourteen without inventing another architecture.
- Replaced the D9 all-units/order packet with a surface-partitioned mandatory agent-route fixture and explicitly excluded human-side D9 claims.
- Renamed the exposition family to a linear-ordering proxy and prohibited it from selecting D7/D8 or triggering A3.
- Added exact family-specific critic and scorer schemas, separate opaque scoring, programmatic checks, and a predeclared full-family replication rule.
- Expanded the source registry to all eight external controls used in Gather/Extract.
- Preserved v1 unchanged as `rejected-before-run / no evidence`; emitted hash-verified v2 and returned to this Extract checkpoint with zero runs.

## Category execution refinement v3 — return from Challenge

### Trigger and evidence disposition

Challenge began under the authorized v2 design. The category family stopped during pass 1 because the fourth scorer (`K8`) received a manually abbreviated scorer input instead of the exact frozen assembly. This is an execution-protocol defect, not a category result and not a replication trigger.

The freeze rule therefore invalidates the **entire category family**:

- all five critic outputs and the four scorer outputs remain immutable instrumentation/audit traces only;
- `V1` was never scored;
- no mapping was revealed;
- no category score, ambiguity, drift, ranking, or hypothesis inference is admissible;
- the invalidated traces do not count as pass 1 and may not be reused in a replacement run;
- ablation and all later families were not started.

The preserved disposition is recorded in `challenge_runs/category/INVALIDATION.md`. Frozen v2 itself, `README_V2.md`, `SHA256SUMS.v2`, and `V1_REJECTED.md` were not changed.

### Replacement execution package

`fixtures/category_v3/` defines `TFW55-I2-CATEGORY-EXEC-v3`, limited to mechanical execution of the unchanged v2 category family. It does **not** change category semantics, packets, opaque labels/order, neutral answer key, rubric, critic/scorer schemas, replication rule, or allowed inference.

The replacement removes discretionary scorer-prompt assembly:

1. A v2-hash-guarded builder preassembles the five exact critic inputs and records their byte-level SHA-256 values.
2. After a critic raw JSON is preserved verbatim, the same builder validates its structure, performs the declared mechanical checks, and assembles the complete scorer input from the exact packet, raw output, v2 answer key, full rubric, and exact scorer schema.
3. The generated scorer-input hash is recorded before dispatch. The isolated scorer must preserve the exact prompt it received; its hash must match before another scorer can start.
4. Any input-hash mismatch invalidates the entire replacement family immediately. Abbreviation, normalization, selective rerun, and a third pass remain forbidden.

The v3 design SHA-256 is `8e53b00a305dde62f1697015daf3ece76fdca3351714ce48fda0f642a09d3500`. Its nine-entry `SHA256SUMS` verifies completely; the manifest SHA-256 is `72abfa80de41a0427ddd4577235bd3e08df8072cde93d187002842fab49f4ee6`. Frozen v2 still verifies as `d7fdb413af669abdf92cb3c055f7a966db3d4daec58d2ac15c36e679805f0f7a`. **Zero v3 critic or scorer runs exist.**

### Replacement checkpoint

The category family must restart with a complete new pass 1 in the original frozen order `Q7 → M2 → R5 → K8 → V1`. The original model/reasoning/isolation settings and literal v2 replication rule remain in force. Challenge may proceed to later frozen families only after the replacement category family completes validly. No adaptive C3 sensitivity fixture is included or authorized.

Questions for `Coordinator | TFW-55`:

1. Accept the v2 category-family invalidation as `instrumentation only / no evidence / no reuse`, with no mapping reveal and no effect on C1/C3/C4/C9/C10 or H1–H4?
2. Authorize `TFW55-I2-CATEGORY-EXEC-v3` at design SHA-256 `8e53b00a…a09d3500` for a full category pass-1 restart under its exact-input hash guards?
3. After a valid v3 category completion, authorize Challenge to continue in the unchanged v2 family order and constraints?

Category execution refinement complete: YES
→ User decision: **Pending new Extract gate; no v3 run is authorized.**

## Category file-read refinement v4 — dispatch-verifiability preflight

### Coordinator disposition of v3

The coordinator accepted the v2 category invalidation as `no evidence / no pass / no reuse`, verified the v3 and upstream hashes, and authorized a complete v3 category restart only. Authorization was conditional: post-dispatch verification had to hash the **actual inline string sent by orchestration**, not the intended input file, a model echo, or a reconstructed copy.

### Pre-run runtime finding

The collaboration spawn interface accepts inline message text but exposes no post-dispatch API for retrieving the exact dispatched message bytes or their hash. Therefore the v3 inline-delivery contract cannot satisfy the authorization condition. This was detected before the first critic spawn:

- v3 critic runs: `0`;
- v3 scorer runs: `0`;
- no new experimental output or mapping information exists;
- no intended-file hash is represented as actual-dispatch verification.

Per the coordinator's explicit fallback, execution returns to a file-read instrumentation design.

### TFW55-I2-CATEGORY-FILEREAD-v4

`fixtures/category_v4/` changes only the delivery channel. The isolated critic/scorer reads one exact hash-attested input file through `file_read_prompt.ps1`; the script rechecks frozen v2, all nine v3 checksum entries, the chosen input path/hash, strict UTF-8 decoding, and writes a pre-model-read attestation before emitting the exact text without an added newline.

The inline orchestration message becomes control-only; it does not contain the experimental packet. The agent is forbidden to inspect invalidated outputs, other variants, mapping, founder/coordinator context, or other project files. It writes its role output once to an assigned raw-output file; root hashes that file and never edits or normalizes it before mechanical scorer assembly.

Integrity state:

- v4 design SHA-256: `05cb8b5c1dbf4ea3171753a12759e6242838e933fddfc690c28695cdf4e51c63`;
- v4 `SHA256SUMS`: 3/3 entries match;
- v4 `SHA256SUMS` SHA-256: `474d181be45e2615b0e6e7d55e3f4b78501360a397ee0980cbba0c0a1a2ec1bd`;
- PowerShell parser errors: `0`;
- v2 and v3 upstream hashes still match;
- v4 run artifacts: `0`.

Question for `Coordinator | TFW-55`:

1. Authorize `TFW55-I2-CATEGORY-FILEREAD-v4` at design SHA-256 `05cb8b5c…f4e51c63` for the complete category restart, with file attestations as the proof of actual experimental prompt bytes read by each isolated role?

Category file-read refinement complete: YES
→ User decision: **`close stage` — v4 authorized for the complete category restart only. Attestation proves the sanctioned reader verified/emitted the named bytes; it does not prove filesystem sandboxing or semantic consumption.**
