# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. Attack the causal account and every proposed survivor with a concrete consequence.
> **Parent:** [HL-TFW_20260907-133942_PTTC](../../HL-TFW_20260907-133942_PTTC.md)
> **Goal:** Reach the simplest complete and coherent verification and closure system while preserving meaningful protection, honest completion and continuation.

## Consistency Check

The alternatives are not a quota of mutually exclusive global policies. Reuse of unchanged dependencies and rechecking affected ones are branches of one evidence-applicability rule. Likewise, checking changed outputs after capture and returning only on a material change are branches of one finite closure route.

### Incompatible pairs

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D2: oracle time and authority | Exact historical snapshot used as the sole current-state oracle | D4: closure and return boundary | Capture markers/dispositions only after the accepted current output has changed | A legitimate successor can be rejected as mixed or corrupt, and no post-capture check can establish the new current output. This is the observed B–D/B–E and CRUE current-release failure pattern. |
| D3: evidence applicability | Reuse despite a changed relevant input, oracle or environment assumption | D4: closure and return boundary | Capture markers/dispositions only | The evidence no longer supports the affected claim, while capture-only closure has no place to detect the changed dependency. The valid Gather alternative was reuse **when unchanged**, not unconditional reuse. |

No unconditional cross-dimensional incompatibility was found between the following pairs: a no-build pure check can use a semantic current oracle; immutable historical preimages can coexist with current semantic checks for different claims; and reuse of unchanged evidence can coexist with a targeted recheck of affected outputs. Eliminating those pairs would create a false choice.

### Surviving configurations

| Config | Execution dependency | Oracle / authority | Applicability and closure | Notes |
|--------|---------------------|--------------------|---------------------------|-------|
| S1 | Pure text/Git checks have no MkDocs prerequisite; output-dependent checks invoke the build only in their own scope | Current claims use semantic predicates; immutable package/replay claims use pinned preimages | Reuse only when relevant inputs, oracle and environment are unchanged; check affected outputs after capture and return once on material change | **Selected simplest provisional design**; combines the compatible branches rather than treating them as alternatives |
| S2 | Explicit output-dependent fixture, with pure checks separated | Historical exact-row/provenance predicates remain in place for the claims they actually protect | Targeted applicability check plus bounded material return | Preserves stronger literal checks but leaves more exact-text sensitivity to challenge |
| S3 | Module-wide shared build remains | Current semantic metadata and pinned historical package checks are separated | Fresh broad rerun after any relevant change, then capture-only close | Technically coherent for a bounded integration module, but retains avoidable work and does not solve post-capture output ownership |
| S4 | Pure checks have no build prerequisite | Exact historical text remains the current oracle for evolving claims | Reuse unchanged evidence and capture-only close | Cheapest-looking subtraction, but fails the conditional incompatibility above when current accepted outputs advance |

S1 survives as the simplest provisional design because it removes the cause of the pure-check dependency, preserves historical evidence where historical identity is the claim, and uses existing evidence/closure carriers with one conditional return. It adds no selector, cache, counter or parallel closure system. This is an analytical selection, not an implementation authorization or empirical proof.

## Findings

### C1: H1 — challenge the cost cause, not the build itself

The module fixture is `scope="module", autouse=True`, so one `mkdocs build` setup is shared by the module/process; it is not a build per test. The challenge to H1 is therefore precise: the build may be necessary for tests that read generated HTML, but it is not shown to be necessary for the knowledge/Git predicate. The source inspection found that the knowledge test reads pinned Git objects and `KNOWLEDGE.md` and does not inspect `site/` output. The simplest surviving boundary is dependency-based: retain the build for output-dependent assertions and remove it from pure text/Git assertions.

H1 is **supported structurally but not measured economically**. Existing records combine collection, one module setup, test bodies, subprocess startup and other process work. No source-backed estimate in this iteration establishes a before/after saving, agent-time reduction or owner-attention reduction. A same-environment trial remains a material question for the next authorized iteration.

### C2: H2 — applicability is claim-granular, not commit-global

Changing an enclosing commit, an unrelated file or an evidence carrier does not automatically invalidate every claim. The relevant dependency tuple is:

`(selected input bytes/refs, oracle predicate + authority, environment assumptions)`.

Examples from the inspected sources:

- A change to `docs/scripts/test_integration.py` that alters `build_site` invalidates evidence about that fixture-dependent execution path, but does not by itself invalidate a separately recorded claim about a task-local status carrier whose bytes, predicate and environment are unchanged.
- The CRUE repair changes current-release metadata and doctor-gate behavior. It is relevant to those release/doctor claims; it is not a rerun or automatic invalidation of the CRATM knowledge predicate.
- A changed current release output invalidates historical-current applicability for a current-state assertion, while exact historical package preimages remain applicable to the immutable package claim.

The smallest sufficient existing carrier is one EV/RF result row for the materially related check group: exact Baseline/Candidate or source SHA, literal relevant selector, the relevant oracle/authority, environment only where it affects the check, command/result and limitation. Task `status.md` and `journal/` carry lifecycle/control state. This is not a universal passport for every check, and it does not require a new registry or cache. The W3C [PROV-DM Recommendation](https://www.w3.org/TR/prov-dm/) distinguishes entities, activities, derivations and agents bearing responsibility; Git’s [revision documentation](https://git-scm.com/docs/gitrevisions) defines full object names and revision selection. Together they support claim-granular provenance and immutable identity, but neither source supplies TFW authority or semantic equivalence.

H2 is **architecturally supported with explicit conditions; empirical reuse is unrun**. The next iteration must test at least one unchanged-dependency reuse case and one changed-input/oracle/environment invalidation case, without turning the carrier into a second control system.

### C3: H3 — bounded administrative repair versus material change

The current route can be decomposed into two outcomes with one stop point:

1. **Administrative repair only:** a missing outcome, escaping reference or invented address is corrected in the owned trace/carrier; the accepted product claim, relevant output, oracle and authority are unchanged. The responsible role validates the exact carrier and lineage, then stops. It does not create a new review/knowledge cycle merely because a record was repaired.
2. **Material accepted-output, oracle or authority change:** identify the affected output(s), run the bounded check for those outputs, and return once to the existing Reviewer/Coordinator route if the changed claim requires judgment. A frozen HL claim or owner-reserved decision follows its existing §12/owner route. The stop condition is the first complete affected-output result plus a resolved review disposition; no universal full-suite or recursive bookkeeping cycle follows automatically.

Existing ownership remains unchanged: the Reviewer records the verdict and evidence applicability; the Coordinator owns `tfw-docs` / `tfw-knowledge`, task status and journal transitions; the owner retains reserved amendment/publication decisions. The existing Step 7 markers cover documentation/knowledge routing but not an explicit changed-output check, so S1 adds a condition to the route rather than a parallel owner or artifact class.

Two counterexamples separate semantic meaning from detector sensitivity:

- **Authority-preserving rewording:** a decision sentence may be rephrased while retaining the same authority, scope and relationship. The current exact-line predicate would reject the changed bytes, but that rejection alone cannot show a material decision change. A semantic review of the authoritative decision and its references is required; no automatic weakening follows.
- **Real attribution distortion:** replacing `acting-principal attribution` with `working-unit attribution` can change the claim because the project conventions distinguish principal attribution from the actual addressable working unit. The mutant’s failure is therefore a useful warning for this specific relation, but the test still does not define semantic equivalence for every prose change. Source: [conventions’ delegation rules](../../../../../.tfw/conventions.md#hl-high-level) and the knowledge predicate in [`test_integration.py`](../../../../../docs/scripts/test_integration.py#L2650-L2720).

H3 is **supported as a bounded architectural route, not as demonstrated closure behavior**. The next iteration must replay a late output change and an administrative terminal-write error, observe the existing owners, and verify that the route stops without a bookkeeping-only cycle. No such replay was run here.

### C4: H4 — simplest complete design and protected consequences

S1 is the simplest survivor against the source-backed attacks:

- It removes an execution dependency where the protected claim does not consume its output, rather than accelerating a universal build.
- It keeps a literal/historical oracle only where exact historical identity or provenance is the protected claim, and uses a current semantic predicate for evolving current contracts.
- It reuses evidence by the concrete dependency tuple and checks only affected outputs when that tuple changes; it does not invalidate all claims because an enclosing commit changed.
- It treats post-capture output checking and material return as one finite route, preserving Reviewer judgment and Coordinator ownership without a new control layer.

The protected consequences are concrete: a legitimate current release must not be rejected for differing from a historical release; a missing or corrupt historical provenance link must still fail; a real attribution/authority change must not pass as harmless prose; a disclosed indeterminate historical corpus finding must not be converted into a global product-clean assertion; and a changed accepted output must not be silently closed.

H4 is **supported architecturally, not empirically**. No trial established that S1 preserves all defect detection, improves runtime, reduces review work or works in a receiving project. Those are not inferred from the smaller mechanism set.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| The simplest provisional design is dependency-scoped verification plus one bounded closure return: pure checks have no MkDocs prerequisite, current and historical oracles are separated by claim, evidence reuse is conditional, and affected outputs are checked after capture. | Same-environment defect-detection and cost trials were not run; no speedup, reliability or receiver claim is admitted. |
| Authority-preserving rewording and real attribution/authority distortion are distinct cases; exact-string mutant sensitivity is not semantic proof. | A later iteration must supply representative source-derived cases and an independent judgment of their protected consequences. |
| Administrative carrier repair is distinct from accepted-output/oracle/authority change; existing Reviewer/Coordinator/owner routes and a first-complete-result stop condition remain sufficient in the source model. | A late-output-change plus terminal-write-error replay is still needed to verify bounded convergence and the exact affected-output set. |
| H1 is structurally supported, H2 conditionally supported, H3 architecturally supported and H4 architecturally supported; all four remain empirically unverified. | Sequential iteration 2 requires a named unresolved material question and a bounded approved cost; it is not authorized by this dispatch. |

**Focused OODA decision:**
- **External source used?** YES — W3C PROV-DM and official Git revision documentation, applied to provenance granularity and immutable identity.
- **Briefing gap closed?** YES — real sufficient construction selected, protected consequences named, administrative/material returns separated, and empirical limits stated.
- **Pairwise incompatibility checked? Surviving configurations listed?** YES — conditional conflicts are explicit, compatible branches are retained, and S1–S4 are concrete survivors.

Stage complete: YES
→ User decision: Awaiting Coordinator checkpoint direction before synthesis.
