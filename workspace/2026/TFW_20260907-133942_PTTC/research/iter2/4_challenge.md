# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260907-133942_PTTC](../../HL-TFW_20260907-133942_PTTC.md)
> Goal: apply the Saint-Exupery principle to remove unnecessary verification and closure machinery while preserving a complete, coherent result.

## Consistency Check

The four Gather dimensions do not form one global policy. Some alternatives are compatible branches for different claim classes; others create a false-green, stale-oracle or authority gap.

### Incompatible pairs

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|-------------|-------------|-----------------|
| D1: subject and oracle boundary | Full current knowledge-row snapshot as the sole meaning oracle | D1: subject and oracle boundary | Current explanatory evolution must remain admissible without changing protected authority/lineage | Full-row equality turns harmless wording or citation evolution into a material failure; it overstates what the structural predicate proves. |
| D1: subject and oracle boundary | Exact historical preimage as the sole current oracle | D4: closure and receiving boundary | Capture markers only after an accepted current output changes | A legitimate successor can differ from the historical preimage, while capture-only closure has no current-output check to establish the successor. |
| D3: execution dependency and applicability | Explicit opt-in with an omitted real HTML consumer or helper | D3: execution dependency and applicability | Pure/no-site selection is treated as evidence that all output consumers are covered | The omitted consumer may read stale site/ content and pass; isolated absence/staleness must be distinguished before calling the boundary safe. |
| D3: execution dependency and applicability | Module-wide autouse setup retained for pure checks | D2: test disposition | KEEP pure source/Git checks as if the setup were a real dependency | The pure predicate does not consume generated output; retaining the setup preserves the avoidable coupling and can turn an unrelated fixture failure into an incomplete pure result. |
| D2: test disposition | REMOVE the current knowledge/provenance guard | D1: subject and oracle boundary | No replacement for identity, lineage, immutable references or current/superseded relation | Removing a structural consequence without an adequate replacement loses the protected claim; subtraction is justified only for the overbroad full-row/prose portion. |
| D4: closure and receiving boundary | Sender evidence treated as a universal receiver passport | D4: closure and receiving boundary | Receiver has its own environment, owner and check command | Receiver dependencies and authority differ; sender evidence can be applicable only to the named shared claim tuple. |

### Surviving configurations

| Config | D1 | D2 | D3 | D4 | Notes |
|--------|----|----|----|----|-------|
| S1 | D — hybrid protected fields plus current prose | B — REWORK | C — pure family without site prerequisite | B — affected-output check | Preserves semantic current meaning and structural lineage without a permanent latest-row snapshot. |
| S2 | B — historical preimage for historical identity | A — KEEP | B — shared output-scoped setup | B — affected-output check | Valid when the claim is byte identity or replay, not an evolving current contract. |
| S3 | A — current semantic predicate | A — KEEP | B — shared output-scoped setup | C — existing material-return route | Valid for output consumers whose result and oracle remain unchanged after capture. |
| S4 | D — hybrid protected fields plus current prose | C — MOVE | B — shared output-scoped setup | D — receiver-owned checks | The source-model receiver case remains isolated and does not export the sender's tools. |
| S5 | D — hybrid protected fields plus current prose | A — KEEP | C — pure family without site prerequisite | C — existing material-return route | One closure-record integrity duty with a record-only versus material/indeterminate branch. |
| S6 | B — historical preimage for historical identity | D — REMOVE obsolete wrapper/duplicate | C — pure family without site prerequisite | B — affected-output check | The unique revision-2 predicate and Git history remain; no unproven public test-name contract is carried. |

### Unexpected survivors

- **S4:** A receiver-owned check survives without requiring the receiving project to run pytest, MkDocs, the sender's corpus or PTTC tooling. This is less machinery and a stronger boundary than a sender-issued passport.
- **S6:** Removing a historical wrapper survives because the protected historical evidence is in Git and the later uniquely named predicate remains. A name-only compatibility promise is not enough to retain a duplicate obligation.
- **S5:** Combining administrative carrier repair and missing terminal outcome survives as one duty because both test truthful closure-record integrity; fake or unverifiable identity stays material/indeterminate.

## Findings

### C1: Explicit opt-in versus family split under absent and stale output

The source inventory finds all current generated-output consumers in the early integration segment: static pages, knowledge index, task pages, knowledge topics, workflows, templates, frontmatter, reference links, section indexes and resolved links. The later source/Git/temporary-state predicates include the board regex, README/state guards, adapter and Phase D/E checks, and the knowledge contract. Helpers do not hide an additional site consumer in the inspected module: every current site read is visible as a direct site/ path or a helper-local path in the enumerated lines. This is a source result, not a collection or runtime result.

Two designs were challenged:

| Attack case | Explicit opt-in in one module | Family split with shared output setup |
|---|---|---|
| Real output test omitted from explicit fixture use | It may read a stale site/ and pass if another test or previous run left plausible output. The test need not fail safely. | Output tests remain in a module whose shared setup runs before them; pure tests are outside that module. |
| Isolated selection with site/ absent | A missing fixture request is exposed as a failure only if the output is absent; this is a future proof case, not a permanent gate. | The output module's setup creates the required output before the consumer; pure module selection does not require it. |
| Isolated selection with stale sentinel output | A missed request may read the sentinel and produce a false green; a temporary stale-output case is required to reveal it. | The output module's setup is still the one shared producer; a stale sentinel must be replaced or the setup evidence is incomplete. |
| Cost and structure | No new file is needed, but every direct and helper consumer must be enumerated and kept correct by later edits. | One additional module boundary may move pure checks, but it encodes the actual dependency rather than a cosmetic grouping; no per-test build is introduced. |

The official [pytest fixture guidance](https://docs.pytest.org/en/stable/explanation/fixtures.html#autouse-fixtures-fixtures-you-don-t-have-to-request) confirms that fixture setup is activated by explicit use or autouse and can have module scope. The source-level challenge is therefore not whether explicit opt-in can share a setup; it can. The problem is that no persistent consumer registry or metadata gate is authorized to prevent a later omission, and a stale output can make omission pass.

**Planning result:** choose the family split as the safer minimal adequate construction for this source. It keeps one shared module-scoped build for actual output consumers and makes the pure/no-site boundary structural. The additional module is justified by a real dependency boundary, not by organization. The smallest implementation proof is one static all-consumer/helper inventory plus one output-family selection with absent/stale-output protection and one pure-family selection without site output. If future source evidence proves explicit opt-in can be enforced with equal stale-output protection and less controlled change, that is a later implementation finding, not a reason to claim the present candidate complete.

### C2: Knowledge oracle — owner-approved successor, harmless wording and material distortion

Three concrete source-model variants challenge the extracted hybrid boundary:

| Variant | Full-row snapshot | Hybrid protected-field boundary | Consequence |
|---|---|---|---|
| Harmless wording/citation change with same decision key, task/phase, required references and current authority | Rejects changed bytes despite unchanged meaning | Structural fields remain stable; explanation can proceed through a semantic disposition | Full-row equality is overbroad. |
| Owner-approved successor changes current artifact relation from an earlier stage to a later accepted stage while retaining historical source identities | Rejects the successor as unlike the old row or freezes the old latest snapshot | Current/superseded relation and required immutable references make the successor explicit; current prose is not a historical preimage | Historical literals are not a new permanent latest snapshot. |
| Fake/unverifiable SHA, changed authority/lineage or duplicate selected row | May reject, but without distinguishing why | Fails the protected structural/provenance predicate and routes as material or indeterminate | It is not a benign typo or wording repair. |

**Planning result:** retain S1. The implementation proof must demonstrate the three named variants using existing predicate/evidence carriers and an owner/Reviewer semantic disposition where meaning changes. Exact selected mutants remain finite regression evidence; they do not become a universal semantic validator. The relevant authority is the owner-approved current contract and its lineage, while immutable Git objects anchor historical claims only.

### C3: Board-regex guard and obsolete same-name bodies

The board-shaped regex has a distinct consequence visible in source: it prevents a generator from reintroducing the retired root README board parser. The guard is not a generated-output test and not a behavior proof. Removing it without an equivalent consequence check would reopen a known architectural coupling; keeping it as a pure guard does not require a new registry or a full site build. **KEEP narrowly** remains justified.

The historical wrapper is different. The source contains earlier same-name Phase D bodies and later revision-2 definitions. Python binds a function definition's name in the current namespace; the later definition therefore replaces the earlier object under that name. The later compatibility definitions at the historical names delegate to the revision-2 predicate. The official [pytest selection documentation](https://docs.pytest.org/en/stable/example/markers.html#using-k-expr-to-select-tests-based-on-their-name) confirms that test names and node IDs can be used to select tests, but it does not make every historical name a public compatibility contract.

The challenge found no declared consumer, receiver obligation or separate protected consequence for the old wrapper. Git history retains the superseded bodies and exact historical source; the unique revision-2 predicates retain current protection. A full run would also execute the delegated predicate under its unique current name and could execute the wrapper under its historical name, duplicating the same obligation.

**Planning result:** REMOVE the obsolete same-name baseline bodies and the thin wrapper aliases in the implementation change, while retaining the unique revision-2 predicates and all historical Git objects. Do not restore superseded bodies. This removes dead definitions and duplicate execution obligations, not the protected historical evidence. The absence of an external consumer remains a bounded risk; it is not an automatic debt or a reason to invent a public API.

### C4: Closure record, integration failure and synthetic receiver

The six preview cases plus the two boundary cases survive one finite decision tree:

| Case family | Failure attacked | Retained/rechecked claim | Existing owner | Valid stop/return |
|---|---|---|---|---|
| Wording-only knowledge correction | Full-row oracle rejects harmless explanation | Hybrid protected fields and semantic current disposition | Reviewer applicability; Coordinator knowledge route; owner for reserved authority | Stop after exact field/reference and semantic disposition; no review cycle for unchanged claim. |
| Decision lost/duplicated/contradicted | Removing a structural guard hides identity or lineage loss | One selected row, decision key, task/phase, immutable refs, current/superseded relation and material attribution | Reviewer records; Coordinator routes; owner rules reserved change | Return on first complete material result; no full replay. |
| Instruction changes permitted decision | Text/parity guard is mistaken for behavior proof | Applicable instruction/parity result plus one bounded behavior case in future evidence | Reviewer/Coordinator; owner for frozen authority | Stop after text and bounded behavior evidence; return on authority change. |
| Oracle/fixture changes | Reused evidence remains green under changed dependency | Relevant input/oracle/environment tuple and affected claim recheck | Reviewer applicability; Coordinator trace | Reuse unaffected claims; recheck affected ones; report incomplete at cap. |
| Unrelated TODO | Unrelated history triggers ceremonial replay | Existing carrier and unchanged tuple | Coordinator task state; Reviewer if applicability is challenged | Preserve evidence and stop. |
| Closure-record integrity | Missing outcome, malformed record, fake SHA or changed accepted output | One duty with record-only versus material/indeterminate branch | Coordinator for carrier; Reviewer for material claim; owner for reserved authority | Exact unchanged carrier repair stops; material/indeterminate branch gets one affected-output check and one existing return. |
| Genuine integration failure | Generated page/link or cross-surface output is actually wrong | Output-specific build/result, exact source/oracle and failing artifact | Executor RF/EV; Reviewer; Coordinator; owner as required | Stop on first complete affected-output failure and return; no unrelated pure replay. |
| Synthetic receiver | Sender evidence is exported beyond its dependencies | Receiver's own status/evidence, owner and project-owned receiver-check command | Receiver's own roles and owner | Stop on one named receiver result; mark inapplicable when receiver evidence is unavailable. |

The closure-record variants are one obligation, not two trials: record-only repair is benign only after unchanged accepted claim, oracle and authority are established; an unverifiable identity is material or indeterminate. The receiver case is a single isolated synthetic project whose own check command is not required to be pytest, MkDocs, Git-corpus or any sender tool.

### C5: Minimum implementation proof program and affordable caps

The selected source-backed planning result is:

1. **Phase A dependency boundary:** split the pure source/Git/temporary-state family from the output-consumer family; preserve one shared module-scoped setup for the output family. Do not add a consumer registry, selector cache, counter or metadata gate.
2. **Phase A knowledge boundary:** implement the hybrid protected-field predicate and retain finite named counterexamples; route changed meaning through existing review/owner authority.
3. **Phase A guard cleanup:** keep the narrow board-regex source guard; remove obsolete same-name baseline bodies and wrapper aliases while retaining unique revision-2 predicates and Git history.
4. **Phase B closure:** verify the one closure-record integrity duty through record-only and material/indeterminate branches, with one affected-output check before any valid DONE route.
5. **Phase B receiver:** use one isolated synthetic receiving project with its own status, owner path and receiver-owned check command; carry sender evidence only where the dependency tuple matches.

The smallest future evidence set uses existing EV/RF/status/journal carriers:

| Unit | Maximum planned attempts | Required observation | Stop/report condition |
|---|---:|---|---|
| Consumer inventory | 1 bounded static inventory | Every direct site/ read and helper path classified as output or pure; no permanent registry created | Stop if a helper dependency cannot be classified; report incomplete. |
| A dependency split | 2 targeted selections: one output family, one pure family | Shared output setup occurs once for output consumers; pure selection is valid without site output; absent and stale sentinel cases do not yield false green | Stop on the first missing/stale-output ambiguity or approved time cap; preserve partial evidence and report. |
| Knowledge boundary | 1 bounded command or evidence unit containing 3 named variants | Harmless wording, approved successor and material/indeterminate distortion receive the distinct expected disposition | Stop if authority/lineage cannot be resolved; do not auto-retry or weaken the predicate. |
| Regex and wrapper | 1 bounded source/history inspection | Board guard's distinct consequence and wrapper's lack of separate supported contract are recorded; obsolete bodies are not revived | Stop/report unknown external consumer; no broad benchmark or deletion quota. |
| Closure-record integrity | 1 bounded scenario with 2 branches, not 2 separate duties | Record-only repair stops; fake/unverifiable identity or changed output routes once through existing material path | Stop after the first complete branch result or missing carrier; no bookkeeping loop or third branch. |
| Synthetic receiver | 1 isolated receiver project and 1 receiver-owned check command | Receiver result and sender applicability limitation are both recorded | Stop as inapplicable if receiver check/owner evidence is absent; do not export sender tooling. |

Historical durations constrain planning context only: collection 0.39 s, a targeted 279.97 s slice, a final 768.55 s mixed run and a six-run total of 1962.73 s were recorded earlier; none is a causal cap for the new design. Any wall-clock bound must be selected prospectively in TS before execution. The enforceable caps here are one inventory, two dependency selections, three named knowledge variants, one source/history inspection, one two-branch closure scenario and one receiver. A timeout is never success; an executor stops, preserves partial evidence and reports the unresolved result.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Explicit opt-in can retain shared module scope but is vulnerable to omitted consumers and stale site/ false greens; a family split is the safer minimal actual-dependency boundary while preserving one shared output setup. | Future implementation must prove all direct/helper consumers, absent/stale-output behavior and before/after protection/cost; no runtime trial was run here. |
| The hybrid knowledge oracle is the only coherent boundary: protected identity/cardinality, lineage, immutable references, current/superseded relation and material attribution; flexible prose requires semantic disposition. | Field-level implementation evidence and owner/Reviewer judgment remain outstanding. |
| Board-regex remains KEEP narrowly for its distinct retired-parser consequence; obsolete same-name Phase D bodies and thin wrapper aliases are REMOVE, with unique revision-2 predicates and Git history retained. | External consumer absence is bounded uncertainty, not a public API claim; a later named consumer could change the disposition. |
| Administrative carrier repair and missing terminal outcome are one closure-record integrity duty; receiver portability is one synthetic project with its own check command. | Closure behavior, integration failure and receiver results require future implementation evidence. |
| One source-backed planning result and a finite proof program are sufficient to route to implementation planning; remaining gaps are named, not generic. | No empirical savings, native behavior, receiver-wide reliability or complete defect-detection claim is made. |

**Focused OODA decision:**

- **External source used?** YES — official pytest fixture and test-selection references, applied to explicit fixture scope, stale-output risk and historical test-name selection. These sources establish tool mechanics only, not TFW authority or semantic equivalence.
- **Briefing gap closed?** YES — the two false-green/compatibility counterexamples were challenged, one concrete planning result was selected, and the minimum implementation proof program was bounded.
- **Pairwise incompatibility checked? Surviving configurations listed?** YES — incompatible oracle/dependency/closure pairs and six surviving configurations are explicit.

Stage complete: YES
→ User decision: Awaiting Coordinator checkpoint direction before RES.
