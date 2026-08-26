# Category execution ledger — TFW55-I2-CATEGORY-FILEREAD-v4

Status: **VALID CATEGORY FAMILY COMPLETE; STOP BEFORE ABLATION**

## Execution and validity

- Two complete passes ran in frozen order `Q7 → M2 → R5 → K8 → V1`.
- Every critic and scorer used a fresh `fork_turns=none` agent with `gpt-5.6-sol`, reasoning `low`.
- Every role produced a matching pre-read attestation. Audit totals: 20 attestations, 10 scorer inputs, 20 raw role outputs, zero schema/attestation failures.
- Every critic output passed exact JSON/schema/label/case checks. Every scorer output passed its exact category schema.
- Raw role outputs were hashed immediately and supplied unchanged to mechanical scorer assembly. No invalidated v2 output or zero-run v3 artifact was reused.
- The runtime does not expose child tool traces to root. The fixed control messages and all 20 final reports state one sanctioned reader invocation, one assigned output write, and zero other tool actions. This is procedural isolation, not filesystem sandboxing or proof of semantic consumption.

## Opaque results before mapping reveal

| Label | Pass 1 score D/E/R | Drift | Ambiguity | Pass 2 score D/E/R | Drift | Ambiguity |
|---|---:|---:|---:|---:|---:|---:|
| Q7 | 2/2/2 | 0 | 3 | 2/2/2 | 0 | 3 |
| M2 | 2/2/2 | 0 | 4 | 2/2/2 | 0 | 3 |
| R5 | 2/2/2 | 0 | 4 | 2/2/2 | 0 | 3 |
| K8 | 2/2/2 | 0 | 3 | 2/2/2 | 0 | 3 |
| V1 | 2/2/2 | 0 | 3 | 2/2/2 | 0 | 3 |

`D/E/R` means definition / exclusion / rule application. Pass 1 triggered mandatory full-family replication because ambiguity differed. Pass 2 did not confirm the ordered difference: every label scored ambiguity `3`. The pass-1 difference is therefore an **unstable observation, not comparative evidence**. No third pass is permitted.

Mapping was revealed only after all required role outputs and audits completed:

| Opaque | Configuration |
|---|---|
| Q7 | C1 discipline |
| M2 | C4 framework-only challenger |
| R5 | C10 explicit hierarchy |
| K8 | C9 quiet methodology |
| V1 | C3 methodology-first |

## Permitted and forbidden inference

Permitted: in this one controlled model/reasoning setting, each of the five wordings supported immediate, schema-valid application of the same provisional F1–F4 boundary to the seven neutral cases in both probes. No stable category-wording difference was observed in score, drift, or ambiguity.

Forbidden: equivalence of candidates; proof that discipline, methodology, hierarchy, or framework is the true category; human comprehension or terminology reception; component/composition novelty; real adoption; durable learning; cross-tool robustness; or evidence that an applicable boundary elevates a framework into a methodology/discipline. The official Scrum counter-control remains decisive against that last inference.

## Category-scoped dispositions

| Candidate | Evidence viability after category family | Frozen-HL compatibility | Category disposition |
|---|---|---|---|
| C1 discipline | Valid boundary packet; no stable advantage over C4 | Directly compatible with frozen discipline-first wording | Survives, but the family supplies no comparative evidence for the added discipline claim |
| C3 methodology-first | Valid boundary packet; no stable advantage over C4 | Conflicts if it replaces frozen discipline as primary; would require conditional A1 treatment | Survives as an evidence-viable amendment candidate, not as an evidential winner |
| C4 framework-only | Valid full-strength low-assumption control; equal bounded performance | Conflicts with frozen fundamental-discipline wording if made primary; architecture otherwise fits | Survives intact; remains the control higher-category claims must beat, but equal scores do not themselves select it |
| C9 quiet methodology | Valid boundary packet; no stable category advantage; terminology manipulation was not tested here | Category and public-language changes would require conditional A1/A2 treatment | Survives, but category evidence does not distinguish it from C3 and cannot mature A2 |
| C10 explicit hierarchy | Valid boundary packet; no stable advantage; hierarchy-necessity burden remains | Partly aligned with philosophy/method/framework layers, but conflicts with a single discipline-first primary formulation | Survives as a positioning/amendment candidate; the family did not justify the necessity of all three layers |

No configuration is eliminated by a confirmed comparative difference because none exists. The useful narrowing is asymmetric: shared-boundary applicability survives, while the extra category claims receive no comparative support over C4.

## Hypothesis status after category only

| Hypothesis | Evidence status | Frozen-HL compatibility |
|---|---|---|
| H1 authority/canon | Not tested by this family; remains conditionally supported from Iteration 1 | Unchanged |
| H2 above-framework identity | Narrowed: immediate application of the shared provisional composition is supported for this model setting, but discipline/methodology/hierarchy wording adds no stable benefit and the family cannot prove a higher category | Frozen H2 remains open; C4 continues as the low-assumption control and A1 remains conditional |
| H3 founder/teaching knowledge | Not tested by this family; remains narrowly supported | Unchanged |
| H4 exposition and human/agent compatibility | Not tested by this family; remains mixed/open | Unchanged |

No new HL amendment candidate matures here. A1 remains conditional; A2 and A3 receive no evidence from category runs.

## Required stop

Category is complete. Ablation, authority, D9, terminology, and exposition were not run and remain unauthorized. Before ablation, a separate hash-guarded mechanical file-read execution package for the later families must return to an execution-instrumentation Extract gate.
