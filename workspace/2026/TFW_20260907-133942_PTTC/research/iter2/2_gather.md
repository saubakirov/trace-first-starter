# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260907-133942_PTTC](../../HL-TFW_20260907-133942_PTTC.md)
> Goal: apply the Saint-Exupery principle to remove unnecessary verification and closure machinery while preserving a complete, coherent result.

## Dimensions

The independent factors are separated here without selecting an alternative. The source comparison is between main RES producer commit 8f1002be14af64aff608b3cdbeba6b048e223e2c and the independent audit producer commit 0ebf0b107cee9589e709746c836b989628230041, read as exact Git objects. Both are attributed to distinct Researcher units even though the principal is the same.

| Dimension | Alt A | Alt B | Alt C | Alt D _(if any)_ |
|-----------|-------|-------|-------|-----------------|
| D1: subject and oracle boundary | Current semantic predicate for an evolving claim | Exact historical preimage for an identity or replay claim | Full current knowledge-row snapshot | Hybrid: immutable protected fields and references plus current explanatory prose |
| D2: test disposition | KEEP the check in its current surface | REWORK the predicate or evidence boundary | MOVE the check to the dependency surface that consumes its output | REMOVE the check when its protected consequence is already covered and no distinct consequence remains |
| D3: execution dependency and applicability | Module-wide autouse site build | Output-scoped build fixture | Pure text/Git/temp-tree check with no site prerequisite | Existing EV/RF evidence reused only for an unchanged dependency tuple, with affected claims rechecked after change |
| D4: closure and receiving boundary | Capture markers and dispositions alone | Capture followed by an affected-output check | Existing Reviewer/Coordinator/owner material-return route | Receiver runs its own applicable checks and owns receiver-local acceptance |

## Findings

### G1: Agreement and disagreement between the two iteration-1 reports

The reports genuinely agree on the following source-backed boundaries:

| Agreement | Evidence and limit |
|---|---|
| Generated-output assertions need a build boundary; pure repository/Git/temp-tree predicates should not inherit an unrelated module-wide build. | The current integration module has build_site at lines 20–37 and output tests read site/ pages. The same module also contains pure source and Git checks. This is a dependency observation, not a measured saving. |
| Current evolving contracts must be separated from immutable historical identity or replay claims. | The main RES D3 and audit D2 both use the CRUE repair source as the counterexample to a historical snapshot acting as the sole current oracle. |
| Superseded early Phase D bodies must not be revived wholesale, and the same-name compatibility surface needs explicit treatment. | The module defines repeated Phase D names at lines 2117/2305 and 2159/2735. The audit correctly treats the wrapper/consumer question as unresolved rather than deleting or restoring by name alone. |
| Controlled protections must survive subtraction; neither report proves runtime savings, native behavior, receiver portability or complete defect detection. | Both exact RES sources state no test/build/runtime/benchmark execution and retain MORE NEEDED. |
| A new selector, cache, counter or parallel closure system is not justified by the source model. | Both reports prefer consequence-based separation and existing carriers, subject to a simpler-alternative challenge. |

The material disagreements are narrower than a global policy choice:

1. **Knowledge oracle.** Main RES keeps the boundary conditional and warns that exact-row mutant sensitivity is not semantic equivalence. The audit names a concrete minimum protected set: uniqueness, decision identity, task/phase lineage, required immutable sources and superseded/current relation, with full-row equality a REWORK candidate. The source comparison supports the audit's minimum as a candidate boundary, but the final field grammar remains a Challenge decision.
2. **Board-regex guard.** Main RES records a conditional architectural guard. The audit distinguishes its residual consequence from generated-output and source checks but leaves KEEP versus narrow REWORK open because no authorized consumer/dependency probe was run. The current source shows it scans generator source lines, skips comments and exempts the migration and test scripts; it does not inspect generated output.
3. **Historical wrapper.** Both reports reject restoring all old bodies. The audit identifies the exact compatibility wrapper as a separate question: repository source shows a same-name wrapper delegating to the later revision-2 predicate, but absence of an in-repository caller cannot establish absence of an external consumer.
4. **Closure and receiver.** The main RES supplies the closure ownership model; the independent audit deliberately did not cover H3. This is a scope complement, not a contradictory finding.

The comparison therefore has enough agreement to challenge one combined design, but not enough evidence to call any conditional KEEP/REWORK choice final.

### G2: Actual dependency and necessity surface

The source separates three classes of checks even though the current module setup couples them:

| Check class | Observed source behavior | Dependency implication | Current unknown |
|---|---|---|---|
| Generated HTML and link/rendering assertions | Tests such as test_static_pages_generated, test_knowledge_index_generated and link-resolution checks read site/ files. | A site build is an actual input; retain a build boundary for this class. | Whether the build should be function-scoped or grouped by one output consumer, and its before/after cost. |
| Pure source/Git/status predicates | The board-shaped regex reads generator source files; Phase D/E checks inspect Git objects, current markdown and path sets; the knowledge contract reads KNOWLEDGE.md and pinned Git objects. | These checks do not consume generated HTML, so module-wide build setup is an incidental prerequisite in the present module. | Whether moving them changes collection/setup/process cost or exposes a hidden shared dependency. |
| Controlled doctor and temporary-tree checks | tools/tests/test_tfw_doctor.py constructs a temporary project and preserves schema, deterministic read-only behavior, material versus indeterminate exit codes, collision handling, prose neutrality and bounded capability. | Their protected consequences are bounded input/state semantics, not documentation rendering. The CRUE repair source removes only the global live-repository cleanliness test while retaining controlled tests. | Whether an optional live diagnostic has a distinct operator value; it must not become a current product oracle or closure gate without a named consequence. |

The board guard is a source-pattern check, not a behavior proof. It compiles a Python regular expression and applies search to each non-comment line in each generator script, excluding migrate_board.py and test_integration.py. The official [Python regular-expression reference](https://docs.python.org/3/library/re.html#re.Pattern.search) defines search as scanning for a match anywhere in the searched string; that confirms the guard's mechanical surface only. It does not establish that a future generator would behave incorrectly, nor that the regex is the only adequate protection.

The repeated Phase D names are a different mechanism. The source defines the same names more than once, while the later definitions are the ones bound in the module namespace. Python's [function-definition reference](https://docs.python.org/3/reference/compound_stmts.html#function-definitions) states that executing a function definition binds its name in the current namespace and that the body runs only when called. The desk-check implication is that the earlier same-name bodies are not independently addressable under that name after the later binding; this is a source-language inference, not a pytest collection run. The later revision-2 predicates therefore remain the surviving current checks, and the historical wrapper can be retained only if its compatibility consequence is named.

The current knowledge index contains D82, D83 and D84 as one row each. The Phase E test at lines 2650–2727 takes exact rows from named Git objects, checks the current row cardinality, checks selected lineage and attribution strings, and rejects selected mutants. This establishes a structural/provenance predicate with a protected consequence. It does not establish semantic equivalence for arbitrary wording changes. A candidate hybrid boundary must therefore preserve decision identity, task/phase lineage, required immutable references and superseded/current relation while making harmless explanatory evolution reviewable rather than silently accepted.

Sources inspected:

- Main iter1 RES: workspace/2026/TFW_20260907-133942_PTTC/research/iter1/RES.md at 8f1002be14af64aff608b3cdbeba6b048e223e2c.
- Independent audit RES: exact Git object 0ebf0b107cee9589e709746c836b989628230041 at workspace/2026/TFW_20260907-133942_PTTC/research/iter1/RES.md.
- docs/scripts/test_integration.py lines 20–37, 195–220, 2117–2172, 2305–2500, 2650–2727.
- tools/tests/test_tfw_doctor.py lines 1–185.
- KNOWLEDGE.md lines 122–124 for D82–D84.
- .tfw/workflows/review.md Steps 5–7 for materiality, routing and closure ownership.

### G3: Eight source-model cases

These are desk-check cases derived from the six HL §3.1 preview rows, one genuine integration-failure case and one receiver case. They define what a future check must carry; they are not executed evidence.

| Case | Affected claim | Minimal retained or rechecked evidence | Existing owner | Valid stop or return | Remaining unknown |
|---|---|---|---|---|---|
| 1. Wording-only knowledge correction | Current knowledge meaning remains the same while explanatory prose or citation wording changes. | Current authoritative row, protected identity/lineage/reference fields, exact source revision, and a semantic review record if the structural predicate changes. No MkDocs build unless an HTML output claim is affected. | Reviewer checks evidence applicability; Coordinator routes knowledge capture; owner retains reserved authority. | Stop after the current predicate and semantic disposition agree that authority and lineage are unchanged. Return only if the protected claim or authority changed. | Exact field grammar and who records the semantic disposition without creating a universal validator. |
| 2. Protected decision lost, duplicated or materially contradicted | The current decision's identity, authority, lineage or required reference is no longer preserved. | Structural uniqueness/cardinality, decision/task/phase lineage, required immutable references, current-vs-superseded relation, and an independent challenge of the material contradiction. | Reviewer records the finding; Coordinator routes the result; owner rules reserved frozen or authority changes. | Stop on the first complete affected-claim result; material failure returns through the existing review/owner route. | Whether the selected counterexamples cover meaningful semantic defects beyond the named fields. |
| 3. Instruction changes an agent's permitted decision | The normative instruction surface and the agent's permitted authority differ. | Applicable instruction/parity checks, exact source and receiver copies, plus a bounded behavioral scenario in future implementation evidence. Text equality alone is not behavior proof. | Reviewer verifies evidence; Coordinator owns task routing; owner rules any frozen-authority change. | Stop after text/parity evidence and the bounded behavior result; return when the permitted decision or frozen claim changes. | Receiver-specific behavior and the smallest genuine scenario that exercises the changed permission. |
| 4. Test oracle or fixture changes | The check's oracle or execution prerequisite changes, possibly invalidating old evidence. | Exact oracle/authority revision, fixture/setup dependency, relevant input/environment tuple, and new evidence for affected claims only. | Reviewer classifies applicability; Coordinator preserves the task trace and dispatches any bounded follow-up. | Reuse unaffected claims; recheck affected claims; stop when each affected result is recorded or report indeterminate if the cap is reached. | Exact dependency fields sufficient to detect an oracle change without commit-global invalidation. |
| 5. Unrelated TODO is registered | An unrelated task-state change occurs while existing product evidence's actual dependencies remain unchanged. | Existing EV/RF-style result with exact source identity and applicable inputs/oracle/environment; task-local status/journal event for the TODO; no new global registry or replay. | Coordinator owns task state and journal; Reviewer owns evidence applicability if closure is being reviewed. | Preserve the existing result and stop; do not trigger a new implementation round merely from unrelated history. | Whether the TODO touches a shared generator/configuration dependency not captured by the initial tuple. |
| 6. Final capture changes an accepted output or terminal record lacks outcome | The accepted output, its oracle/authority, or closure record is materially incomplete after capture. | Capture revision, affected output identity, completed output check, outcome-bearing record and retained correction history. | Coordinator owns status/journal and docs/knowledge routing; Reviewer returns a material claim; owner rules reserved changes. | Administrative carrier repair with unchanged claim stops after exact carrier validation. Material output/oracle/authority change gets one affected-output check and one existing material return; no bookkeeping-only loop. | Late-output and erroneous-terminal-write behavior must be replayed during implementation evidence. |
| 7. Genuine integration failure | A generated output or cross-surface integration contract actually fails, such as a missing page/link or a generator/runtime boundary contradiction. | Build/output evidence for the affected consumer, exact input and oracle, failing output reference, and the smallest independent source or parity check that distinguishes generator failure from stale fixture state. | Executor produces RF/EV; Reviewer verifies the failure and disposition; Coordinator routes correction; owner rules any scope or frozen-claim change. | Stop at the first reproducible affected-output failure; return to the existing review/execution route. Do not rerun unrelated pure checks automatically. | Which integration failure is representative enough for a future bounded case and what output subset it exercises. |
| 8. Receiver with its own checks | A receiving project applies the evidence under its own paths, owner, environment and acceptance checks. | Sender's exact applicable source/claim tuple and limitations; receiver's own task-local status, oracle, environment and independent check result. | Receiver's own Executor/Reviewer/Coordinator/owner chain owns acceptance; PTTC sender remains responsible only for its stated evidence boundary. | Stop if receiver-owned checks pass for the named case. Return or mark inapplicable when receiver dependencies differ; never treat sender evidence as a universal passport. | A named receiving project and its own checks are required for implementation evidence; no receiver run is authorized here. |

The table shows why the same carrier cannot replace every check: case 1 needs semantic current meaning, case 7 needs generated output, and case 8 needs receiver-owned evidence. The common carrier fields are therefore conditional, not a global registry schema.

### G4: Existing costs and smallest prospective Phase A/B verification plan

Recorded observations provide planning inputs, not a performance baseline for the proposed design:

| Recorded source | Reported result | Proper use |
|---|---|---|
| CRATM collection | 529 collected in 0.39 s | Collection/setup reference only; not a cost of the pure check itself. |
| Targeted Phase E run | 15 passed, 310 deselected in 279.97 s | Shows a bounded existing output, knowledge and integration slice; not a before/after comparison. |
| Strict MkDocs build | exit 0 | Confirms one build invocation succeeded in the record; does not measure causal necessity for each test. |
| Final configured run | 528 passed, 1 skipped in 768.55 s | Overall recorded run duration with mixed test classes; cannot be assigned to the module fixture alone. |
| Initial configured run | 526 passed, 1 skipped, 2 failed in 721.91 s | Shows stale Phase-D/current-knowledge disagreement in the record; not evidence that the proposed boundary fixes it. |
| CRUE isolated repair source | 549 passed, 1 skipped in 715.86 s | Attributed source commit a767b17072733dc856d4c73fa6a72277e1538ba5; not rerun or saved-master/publication proof. |
| Late-round planning record | Six runs totaling 1962.73 s | A historical attention/cost signal only; no causal decomposition or new denominator. |

The smallest future verification plan can reuse existing carriers and recorded observations:

| Future unit | Existing carrier | Prospective measurement | Planning cap and stop rule | Protected consequence |
|---|---|---|---|---|
| Phase A-1: pure/output dependency split | One EV/RF result row plus exact source revision and affected test group | Record build invocations, pure-check result, selected negative cases, setup/body/process duration and environment. | One bounded comparison case and one adverse case; use a TS-approved time cap as a pre-act guard, not a target. Stop on cap or missing dependency evidence and report incomplete; no automatic retry. | Pure checks no longer require unrelated generated output; output checks still retain build protection. |
| Phase A-2: knowledge-oracle boundary | Existing source/Git predicate result and exact selected rows/objects | Compare harmless wording, legitimate successor and real lineage/authority distortion as named source-derived cases. | Fixed small case set named in TS; stop if field semantics cannot be ruled without owner input. No universal semantic validator. | Preserve decision identity, lineage, immutable references and current/superseded relation without freezing harmless prose. |
| Phase A-3: regex/wrapper necessity | Existing source test result, exact generator file set and Git history | Record distinct consequence, current in-repo callers and compatibility obligation from bounded source evidence. | One bounded consumer/source inspection; stop and report unknown for external consumers. No broad benchmark or deletion quota. | Avoid reintroducing the retired board API and avoid deleting a needed compatibility surface. |
| Phase B-1: closure branches | Existing Reviewer/Coordinator/status/journal carriers | Replay one administrative carrier repair, one changed accepted output, and one terminal record error using synthetic bounded inputs in the future implementation evidence. | Three named branches, one pass each; stop after first complete result or report the missing branch. No recursive administrative loop and no full-suite rerun. | DONE requires affected-output assurance and complete outcome record; administrative repair does not manufacture a new review cycle. |
| Phase B-2: receiver boundary | Receiver's own EV/RF/status/journal plus sender limitation record | Use one named receiver case with its own checks and compare the dependency tuple. | One receiver case; stop as inapplicable when receiver evidence or owner is unavailable. Never claim portability from sender-only evidence. | Receiver independence and honest applicability remain visible. |

Any cap above is a prospective TS planning bound, not measured runtime and not permission to report success after timeout. A future executor must preserve raw partial evidence, report the stop and await an explicit new bounded authorization if the missing result is material.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Main and independent reports agree on dependency-scoped output checks, current/historical separation, no blanket deletion, no revival of superseded bodies and no new machinery without necessity. | The final protected knowledge-field grammar, board-regex disposition and historical-wrapper disposition remain for Extract/Challenge. |
| The current module couples pure source/Git checks to module-wide MkDocs setup; generated-output checks have a real site dependency. | Cost magnitude, hidden shared dependencies and preserved defect detection require future implementation evidence. |
| The six HL cases, genuine integration failure and receiver boundary each require a different affected-claim/evidence/owner/stop tuple; no universal passport suffices. | No named receiver or executed integration/closure trial is authorized in research. |
| Existing recorded durations can bound a future plan, but cannot establish causality or savings. | TS must name prospective caps and pre-act stop/report rules; timeout is not success. |

**Focused OODA decision:**

- **External source used?** YES — official Python regular-expression and function-definition references, applied only to the source-level meaning of Pattern.search and repeated function-name binding. Prior pytest/MkDocs/PROV/Git references remain in the iter1 source reports and are not re-summarized here.
- **Briefing gap closed?** YES — report agreement/disagreement, disputed checks, eight source-model cases and a smallest future verification plan are mapped.
- **Dimensions identified?** YES — four independent dimensions with alternatives are listed; no alternative is marked recommended.

Stage complete: YES
→ User decision: Awaiting Coordinator checkpoint direction before Extract.
