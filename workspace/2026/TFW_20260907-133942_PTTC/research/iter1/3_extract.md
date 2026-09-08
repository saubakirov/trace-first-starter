# Extract — "What do we NOT see?"
> **Mindset:** Analyst. Make combinations and evidence boundaries visible without selecting a final design.
> **Parent:** [HL-TFW_20260907-133942_PTTC](../../HL-TFW_20260907-133942_PTTC.md)
> **Goal:** Reach the simplest complete and coherent verification and closure system while preserving meaningful protection, honest completion and continuation.

## Configuration Space

The full space is the factorized product `D1{A,B,C,D} × D2{A,B,C,D} × D3{A,B,C,D} × D4{A,B,C,D}`: 256 combinations. Since this exceeds 30, the table makes the baseline, one-dimension deviations and several mixed interactions explicit; every other tuple in the product remains open and is not rejected here. `A–D` refer to the alternatives in Gather and are not recommendations.

| Config | D1: execution dependency boundary | D2: oracle time and authority | D3: evidence applicability | D4: closure and return boundary |
|--------|----------------------------------|------------------------------|----------------------------|--------------------------------|
| C1 | A: module-wide automatic site build | A: exact historical snapshot hashes | A: reuse under unchanged inputs/oracle/environment | A: capture markers and dispositions |
| C2 | B: explicit fixture for output-dependent tests | A | A | A |
| C3 | C: no site build for pure text/Git checks | A | A | A |
| C4 | D: separate integration invocation | A | A | A |
| C5 | A | B: current semantic metadata and invariants | A | A |
| C6 | A | C: immutable pinned package-commit preimages | A | A |
| C7 | A | D: explicit mixed/corrupt-state rejection | A | A |
| C8 | A | A | B: targeted recheck of affected outputs | A |
| C9 | A | A | C: independent Reviewer applicability check | A |
| C10 | A | A | D: fresh broad rerun after any relevant change | A |
| C11 | A | A | A | B: capture plus changed-output checks |
| C12 | A | A | A | C: bounded material-change return to existing review |
| C13 | A | A | A | D: fresh review/knowledge cycle for every administrative correction |
| C14 | B | B | B | B |
| C15 | C | C | C | C |
| C16 | D | D | D | D |
| C17 | B | C | D | A |
| C18 | C | D | A | B |
| C19 | D | A | B | C |

## Findings

### E1: Protected predicate versus semantic meaning

The knowledge test in [`docs/scripts/test_integration.py`](../../../../../docs/scripts/test_integration.py#L2650-L2720) is a layered structural and provenance predicate:

| Detector operation | Claim it directly supports | Claim it does not establish by itself |
|---|---|---|
| `row(ref, decision)` selects lines beginning with `| Dxx |` and requires exactly one row | A selected decision identifier has one exact row in the referenced Git object | That every wording change to the row changes the decision’s meaning |
| `expected_d82` and `expected_d83` come from pinned historical refs; `expected_d84` comes from K2 | The expected historical/current relationship is anchored to named immutable inputs | That the pinned text is the only semantically valid formulation of the decision |
| The predicate requires either the pre-K2 `B–D` row or the post-K2 `B–E` row, with Candidate-II and G-1 SHAs where applicable | The tested state transition and selected provenance links are present and not mixed | That an untested successor representation is invalid merely because its prose differs |
| Mutants remove/duplicate rows, alter the transition, corrupt SHAs, or replace `acting-principal attribution` with `working-unit attribution` | The detector is sensitive to selected structural, provenance and attribution perturbations | Whether an arbitrary changed line is a real authority change, a permitted successor, or an equivalent rewording |

The protected claim is therefore narrower than “current knowledge equals the historical rows”: the code checks exact row cardinality, selected text, state transition and provenance references. The phrase mutant may be a meaningful authority distinction in this project, but the test has no semantic equivalence predicate; a reviewer must inspect the authoritative decision and its relationship before classifying a changed line. A legitimate rephrasing that preserves the same authority could be rejected by exact-string comparison, while a different text that accidentally preserves the same bytes in the tested fields could escape this detector. This is an analysis of the predicate, not a verdict to weaken it.

The attributed CRUE repair provides a separate current-versus-historical pattern: `_current_release_metadata` checks current version/configuration/changelog semantics, while the six historical postimages are checked against the immutable `PHASE_E_II_RELEASE_COMMIT`. That pattern demonstrates two predicates with different authorities; it does not prove that the knowledge predicate should be changed in the same way. Source: commit `a767b17072733dc856d4c73fa6a72277e1538ba5`, inspected without rerun.

### E2: H2 inputs, oracle, environment and the smallest existing carrier

H2 becomes testable only when “same evidence” is decomposed into three independent inputs and one carrier:

| Evidence dimension | Concrete instance in this investigation | Reuse condition | Invalidation trigger |
|---|---|---|---|
| Relevant input | Exact selected files/bytes, Git refs, task artifacts and affected output paths; for the knowledge case, the pinned decision rows and `KNOWLEDGE.md` state | The selected input set and relevant bytes remain unchanged | A selected file, referenced commit, task artifact or affected output changes |
| Oracle | The exact predicate and expected relation: row cardinality/lineage for knowledge, current version/config/changelog semantics for release metadata, or doctor exit classification | The predicate, expected relation and its authority remain unchanged | The oracle code, expected relation, authoritative source or interpretation changes |
| Environment | Python/Git/OS and MkDocs only for checks that invoke them; the pure text/Git check has no semantic dependency on a generated site | Environment assumptions used by that evidence remain unchanged | A tool/runtime/version, configuration, filesystem or process assumption relevant to the check changes |
| Existing carrier | EV/RF evidence row and its referenced immutable Baseline/Candidate SHA, literal selector, command/result and environment; task `status.md` and `journal/` carry control state | The carrier records all three unchanged dimensions and its limitation | Any dimension is missing, stale, or not recorded at the required granularity |

The smallest already-existing evidence carrier is not a new registry or cache: it is the existing EV/RF result structure plus exact Git object identity. The task-local status and journal are the control carrier, not a substitute for evidence. This decomposition preserves a useful reuse path while making invalidation explicit. The [W3C PROV overview](https://www.w3.org/TR/prov-overview/) treats provenance as information about entities, activities and people involved in producing a thing and highlights reproducibility and versioning; that supports separating file/output entities, checking activities and responsible agents, but it does not define TFW authority. Git’s [official documentation](https://git-scm.com/docs/git#_identifier_terminology) defines commit/object names and explains that objects are identified by the contents hash; this supports immutable identity for the carrier, not permission to accept a result.

### E3: H3 protocol obligations, execution mistakes and material return

The observed CRATM failure separates protocol design from execution error:

| Obligation or event | Classification | Existing owner | Affected final output | Material return condition |
|---|---|---|---|---|
| Resolve identity, parent, dispatch and exact source before durable work; keep status/journal lineage | Protocol obligation | Root Coordinator validates the chain; each role stays inside its lock | Dispatch and task-local trace | Missing/ambiguous lineage or invented address stops the write and returns to Coordinator; the error remains visible |
| Preserve the approved claim while distinguishing historical evidence from current state | Oracle/protocol boundary | Test owner and independent Reviewer | Assurance result and current repository acceptance | A changed claim, authority or relevant oracle requires reclassification; a mere equivalent wording change needs semantic review, not automatic acceptance or rejection |
| Review evidence and then capture changed documentation/knowledge outputs | Existing route plus identified gap | Reviewer records verdict; Coordinator runs `tfw-docs` / `tfw-knowledge` | `KNOWLEDGE.md` §§1–3, any approved topic/state effects, REVIEW markers | If accepted outputs change after capture, run the affected-output check and route a material change back through review |
| Set `DONE` only after both KNW markers and no undisposed REVIEW §5 item | Existing protocol obligation | Coordinator writes task `status.md` and journal after authorized review route | Lifecycle and outcome in `status.md` | Missing marker, incomplete carrier or undisposed item blocks terminal close; it does not create an automatic second review loop |
| Keep publication separate from readiness | Owner reservation | Owner after Coordinator reports readiness | Release/push/publication effects | Any publication request remains a separate owner decision |

Observed execution mistakes include missing outcomes, an escaping reference and an invented commit address during recovery; these are not evidence that the protocol should be removed. The stale B–D assertion is a detector/oracle defect, not the same thing as a missing control record. The protocol gap is narrower: Review Step 7 names the capture markers and their ownership but does not name a changed-output check after docs/knowledge effects. H3 therefore has a concrete route to simplify: eliminate the cause of repeated bookkeeping-only cycles where accepted claims and outputs are unchanged, while retaining a bounded return when a captured output or material claim actually changes. This remains a structured hypothesis, not an applied closure change.

### E4: H4 interaction patterns for Challenge

The extracted combinations expose the trade-off without choosing one:

- **C1** couples a module-wide site build to an exact historical oracle, evidence reuse and capture-only closure. It preserves several checks on paper but carries both the known fixture edge and the post-capture gap.
- **C14** separates the build boundary, current semantic oracle, affected-output recheck and bounded return. It is the clearest interaction to challenge against the real protected relations, but its sufficiency and cost are not established here.
- **C15** removes the site dependency while retaining exact row text, targeted applicability and bounded return. It isolates whether the remaining exact-row detector protects authority or merely wording; the answer cannot be inferred from its mutant count.
- **C17** uses explicit output-dependent setup, immutable package preimages, a fresh broad rerun and capture-only closure. It is a valid cross-product member whose cost and closure limitation must be made visible rather than silently treated as the default.

These combinations show why a new selector, cache or control layer is not yet justified: the existing dimensions already express different boundaries. Challenge must test the protected consequence and the failure of a simpler option, not optimize the number of files or rows.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| The knowledge detector proves selected structural/provenance relations and sensitivity to selected mutants; it does not prove semantic equivalence or semantic change for arbitrary row wording. | Challenge must supply concrete authority-preserving and authority-changing counterexamples before any exact-row disposition is proposed. |
| H2 can use the existing EV/RF carrier plus immutable Git identity, with relevant input, oracle and environment recorded separately; W3C PROV and Git documentation support the distinction without requiring a registry or cache. | No empirical reuse trial or environment-change counterexample was run; the applicability rule remains to be tested against representative cases. |
| H3 separates protocol obligations, execution mistakes, affected outputs and existing owners; the missing changed-output check is distinct from the existing finite KNW/DONE route. | Challenge must determine the minimum affected-output set and the exact material return condition without recreating a bookkeeping-only cycle. |
| The full 256-combination space is represented factorized, with explicit one-axis and mixed configurations; module fixture setup is one shared setup per module/process. | No configuration is selected; no savings, defect-detection equivalence or closure completeness is established. |

**Focused OODA decision:**
- **External source used?** YES — W3C PROV overview and official Git documentation, both tied to H2’s provenance/applicability question.
- **Briefing gap closed?** YES — the predicate boundary, H2 carrier, H3 ownership/return structure and H4 interaction space are explicit.
- **Configuration Space built from Gather dimensions?** YES — full factorized product plus explicit deviations/interactions.

Stage complete: YES
→ User decision: Awaiting Coordinator checkpoint direction before Challenge.
