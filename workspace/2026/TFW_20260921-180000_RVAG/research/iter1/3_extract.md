# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260921-180000_RVAG](../../HL-TFW_20260921-180000_RVAG.md)
> Goal: Restore independent review as a gate on purpose, accepted value, and material quality, without letting immaterial process-record defects restart product execution.

## Configuration Space

The unconstrained cross-product is 16,384 rows. The table keeps coherent families and one-factor
variants so every Gather alternative appears and the interactions remain inspectable. It is
descriptive; Challenge will evaluate survivors.

| Config | D1: verdict architecture | D2: blocking predicate | D3: verification-depth selection | D4: TRACE disposition | D5: permanent-test admission | D6: correction owner and route | D7: terminal return |
|--------|--------------------------|------------------------|----------------------------------|-----------------------|------------------------------|--------------------------------|---------------------|
| C0 — current dominant path | Scalar checklist verdict | Any cited approved-criterion/frozen-claim breach | Fixed `0.42` file ratio; any discrepancy → 100% | A cited false/stale carrier can block | No explicit admission contract; red-before-green appears in task contracts | Full Executor return under rung route | Durable REVIEW only |
| C1 — predicate-only | Scalar checklist verdict | Claim + harm + material consequence + evidence | Fixed ratio/escalation retained | Material split | Green presence in configured suite | Classification-selected route | Durable REVIEW only |
| C2 — risk-only | Scalar checklist verdict | Any cited breach | Claim/risk/oracle/evidence gaps | Every false/stale carrier may block | Historical red-before-green only | Full Executor return | Durable REVIEW only |
| C3 — sequential | VALUE → ASSURANCE → TRACE feeding one verdict | Claim + harm + material consequence + evidence | Claim/risk/oracle/evidence gaps | Material split | Behavior + harm + demonstrated counterfactual | Classification-selected route | REVIEW + fixed compact envelope |
| C4 — dual judgment | Accepted-result verdict + record-health judgment | Claim + harm + material consequence + evidence | Claim/risk/oracle/evidence gaps | Separate record-health judgment | Behavior + harm + demonstrated counterfactual | Same-carrier repair or evidence-only follow-up by class | REVIEW + fixed compact envelope |
| C5 — enumerated | Scalar checklist verdict | Contract-enumerated blocking classes | Criticality tiers with prescribed minima | Owner escalation for unlisted TRACE | Historical red-before-green only | Full Executor return or owner decision | REVIEW + narrative message |
| C6 — scored | Scalar checklist verdict | Risk/criticality score threshold | Criticality tiers | Score threshold | Mutation/coverage threshold | Full Executor return | Provider-specific form |
| C7 — transport-only | Current checklist with local exceptions | Any cited breach | Fixed ratio/escalation | Every cited discrepancy may block | Green presence | Full Executor return | REVIEW + fixed compact envelope |
| C8 — materiality plus old depth | Scalar checklist verdict | Claim + harm + material consequence + evidence | Fixed ratio/escalation | Material split | Behavior + harm + demonstrated counterfactual | Classification-selected route | REVIEW + fixed compact envelope |
| C9 — materiality plus claim depth | Scalar checklist verdict | Claim + harm + material consequence + evidence | Claim/risk/oracle/evidence gaps | Material split | Behavior + harm + demonstrated counterfactual | Classification-selected route | Durable REVIEW only |
| C10 — sampling | VALUE → ASSURANCE → TRACE feeding one verdict | Claim + harm + material consequence + evidence | Changed-dependency reach plus bounded sampling | Material split | Behavior + harm + demonstrated counterfactual | Classification-selected route | REVIEW + fixed compact envelope |
| C11 — explicit safety boundary | VALUE → ASSURANCE → TRACE feeding one verdict | Material predicate plus enumerated safety/security, authority, identity, and continuation boundaries | Claim/risk/oracle with criticality floor | Material split; unsafe/insecure provenance cannot be record-only | Behavior + harm + demonstrated counterfactual | Classification-selected route | REVIEW + fixed compact envelope |

`Classification-selected route` is an Extract result not visible in the Briefing: D6's alternatives
are not mutually exclusive product choices. They are destinations selected after the defect subject
is known. The same is true of `same-carrier repair` and `evidence-only follow-up`; neither can replace
the other globally.

## Findings

### E1: Four axes are decision inputs; three are downstream routing or transport

D2 (materiality), D3 (verification selection), D4 (TRACE effect), and D5 (test admission) decide
whether the accepted result or assurance is trustworthy. D6 is a function of that classification,
not a single policy choice. D7 transports the already-recorded outcome and cannot repair verdict
semantics. D1 controls presentation: a scalar verdict, a sequence feeding one verdict, or a distinct
record-health judgment can all encode the same underlying predicate.

This separation exposes three partial changes that do not address the whole failure: changing only
the return message leaves MFX's false-return predicate intact; replacing only the file ratio changes
audit depth but not what can block; adding only a materiality sentence leaves every discrepancy on
the same correction route.

### E2: The case matrix yields a deterministic finding taxonomy

| Case / finding | Subject | Material consequence | Evidence state | Required effect | Candidate identity |
|---|---|---|---|---|---|
| F31 wrong-purpose but polished result | VALUE / purpose | Accepted output serves the wrong goal | Quality evidence may be strong but irrelevant to purpose | `REJECT` or frozen-contract/owner route | May be technically stable but unacceptable |
| TLD `$0` substitution | VALUE / actual behavior and compatibility | Shipped headline command cannot execute for its consumer | Direct reproduction establishes failure | Product correction under existing approved scope | Must move |
| CRATM missing owner-direct branch | TRACE-authority + continuation, with product behavior | Valid owner-direct work can STOP; signing authority is contradictory | Actual consumer contradicts intended route | Authority/product correction; owner route if frozen authority changes | Must move if consumer text changes |
| FRATS unreproducible semantic replay | ASSURANCE | Material preservation claim is unestablished | Output exists but lacks executable predicates and command | Evidence-only correction plus bounded independent follow-up | Remains unchanged |
| MFX false byte-identity statement after independent image verification | TRACE/record | No accepted product, material proof, authority, safety, or next action changes | Claim is false; stronger independent evidence establishes the underlying result | Correct current carrier or record observation | Remains unchanged |
| MFX count, label, unit, stale free-section citation | TRACE/DERIVED record | Reader cost or local confusion only; no material conclusion/action changes | Error is reconstructable from named source | Finite same-carrier correction or documented observation | Remains unchanged |
| Unsafe/insecure behavior or an unestablished safety/security claim | VALUE or ASSURANCE, safety/security boundary | Credible harm, secret exposure, destructive/irreversible action, or unsafe acceptance | Failure shown or material claim remains unestablished | Block/return through the governing authority; never downgrade for absent incident history | Moves for product defect; may remain for assurance-only gap |

The deterministic split is semantic, not path-based. A false statement inside `EV` is material when
it is the only support for an acceptance-critical claim; the same false statement is record-only
when the claim is independently established against the correct result, oracle, environment, and
authority. Likewise, a TRACE file can contain a material authority or Candidate-identity defect, and
a product file can carry a harmless wording issue.

### E3: Minimal blocking grammar

A finding can change the verdict only when it records all of the following:

1. **Subject and authority:** `VALUE`, `ASSURANCE`, or `TRACE`, plus the accepted claim/frozen clause
   and its authorized decision owner.
2. **Observed fact and oracle:** what was independently observed, against which actual result,
   environment, source epoch, or authority.
3. **Concrete harm:** what fails, becomes unsafe/insecure, becomes untrustworthy, loses authority or
   produces a wrong next action.
4. **Material consequence:** which acceptance conclusion or authorized action changes now.
5. **Completion condition and route:** product correction, evidence-only correction, frozen-contract
   ruling, record-only repair, or no owed change.

Absence of one element means the finding can remain visible but cannot by itself ground `REVISE` or
`REJECT`. Safety and security are not optional examples: credible unsafe/insecure behavior, or
insufficient evidence for a material safety/security claim, always satisfies the material-boundary
test until resolved. A record-only route is unavailable when a record defect can alter a safe action,
expose a secret, hide an irreversible operation, misidentify the actual environment/result, or
invalidate security authority.

### E4: Verification depth follows claims and risk, not artifact population

The smallest selection model uses the material claim inventory, risk/criticality, affected behavior
and dependencies, actual environment, available oracle/authority, and evidence gaps. A discrepancy
reopens the affected claim and its dependencies; it does not automatically make every changed file
relevant. Residual sampling remains available when the Reviewer names why the sample can expose a
remaining material risk.

[NIST SP 800-171A Rev. 3](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/800-171Ar3/NIST.SP.800-171Ar3.html)
states that a broad list of potential methods and objects is not itself a required artifact set,
sets no expected number of methods or objects, and lets organizations choose what is sufficient to
support the compliance claim based on policy, dependencies, operational context, threats, and risk.
That is a security-specific standard, so RVAG does not import its controls; the transferable point is
the claim/risk selection relationship. It also reinforces the Coordinator's safety constraint:
security rigor is selected by the protected requirement and risk, never by absence of a prior incident.

### E5: Assurance is a traceable relation, not a volume score

[NISTIR 7608](https://www.nist.gov/publications/software-assurance-using-structured-assurance-case-models)
models assurance as claims supported by explicit arguments from objective evidence. It treats a
claim as a demonstrable statement about a property or behavior and identifies evidence sufficiency,
evidence quality, and sub-claim granularity as unresolved judgment problems. RVAG can therefore use
the lightweight relation `material claim → oracle/argument → evidence` without adding an assurance
case artifact, registry, completeness score, or mandatory claim tree.

For permanent tests this relation becomes:

`protected behavior/invariant → failure consequence → relevant counterfactual → observed detection`.

Historical red-before-green is one strong counterfactual for corrected behavior. Existing correct
behavior can use a targeted mutant, fault injection, broken fixture, external receiver, metamorphic
violation, or other relevant negative control. A positive control proves the instrument can run; it
does not independently prove detection power. Coverage, mutation score, test count, and green status
remain diagnostics unless the accepted product itself is that exact mechanism.

### E6: Correction routing is a function of the failed subject

| Failed subject | Default owner/route | Lifecycle/Candidate effect | Reviewer continuation |
|---|---|---|---|
| Material product/domain behavior inside approved TS | Existing Coordinator ruling → same Executor under rung 1 | `RF → ONB`; new Candidate after accepted correction | Same Reviewer verifies affected result/evidence |
| TS defect or missing executable bound | Existing Coordinator → rung 2 TS revision → same Executor | `TS_DRAFT → ONB`; new Candidate if product changes | Same Reviewer verifies return |
| Frozen purpose/authority/contract defect | Coordinator → valid rule-8 ruler; STOP until terminal verdict | No Executor dispatch before executable bound | Same Reviewer only after valid route returns |
| Material assurance gap with unchanged accepted result | Evidence producer/correct carrier under Coordinator bound | Candidate remains; no product round solely for evidence | Same Reviewer performs bounded affected follow-up |
| Material authority, result-identity, environment, safety/security provenance, or continuation defect | Existing authority route selected by the affected claim | Block until identity/authority/proof is reconstructable; Candidate moves only if VALUE changes | Same Reviewer checks affected claim |
| Reconstructable record-only defect | Existing Coordinator/current carrier; preserve history | No TS revision, Candidate, full review round, or execution | Validate repair and stop; no stage restart |
| Immaterial observation with no owed correction | Record once with named consequence/absence | No lifecycle or Candidate change | None |

This matrix extends the existing rung table rather than replacing it: rungs still select authority for
real product/spec/contract defects, while record-only and evidence-only branches prevent a false
product loop.

### E7: Candidate minimal change surface uses existing carriers

No new artifact, registry, score, checklist stage, or permanent test suite is needed. The semantic
carriers already exist:

- `workflows/review.md` for subject order, materiality, verification selection, verdict and return;
- `templates/review/verify.md` for claim/risk/oracle selection and affected-discrepancy expansion;
- `templates/review/judge.md` for the universal blocking grammar and explicit safety/security boundary;
- `templates/REVIEW.md` for verdict, finding fields, correction class and terminal envelope reference;
- `conventions.md` for REVISE, evidence-only and record-only routing;
- `project_config.yaml`, its template, and Config propagation for deleting or retiring
  `review.min_verify_ratio` consistently;
- glossary, shipped adapter copies, migration guidance and release documentation where the accepted
  behavior is named or propagated.

The exact terminal-return and Antigravity overlap is deliberately unresolved. AGSK Phase B remains
at `RF` on the second Extract check, so its unaccepted RF is still excluded. After accepted landing,
the final surface must consume AGSK transport and add only Reviewer-specific payload/timing/value
semantics, not duplicate provider transport.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Twelve coherent configurations expose which changes are semantic, routing, or transport-only. | Challenge must attempt false approval, false return, safety/security weakening, and bureaucratic growth against the strongest families. |
| One deterministic semantic taxonomy covers VALUE, ASSURANCE, material TRACE, record-only TRACE, and DERIVED observations. | Iteration 2 must stress ambiguous mixed findings and non-code or high-risk cases. |
| A five-field blocking grammar and claim/risk/oracle verification model replace proxy counts without lowering assurance. | Challenge must test whether every field is necessary and whether any can be merged without ambiguity. |
| Correction route follows the failed subject; evidence-only and record-only paths preserve Candidate identity when VALUE did not change. | Exact lifecycle wording and AGSK overlap wait for accepted landing and later planning. |
| Existing carriers are sufficient; no new artifact or score is structurally required. | Challenge must try to find a case that truly requires a new carrier. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?

### Material handover at this checkpoint

**Producer and unit:** Researcher, `codex:thread:local:01a0c7ba-6045-7ab0-b261-11cec3ca1af5`.

**Bounded source/epoch:** Gather sources and current framework HEAD
`8528730c46f74df5f8e881c658ff5e419bfb92d9`; `conventions.md` Task Statuses, Closing and record
recovery, and canonical REVISE route; NISTIR 7608 and NIST SP 800-171A Rev. 3 linked above; AGSK
Phase B status reread at lifecycle `RF`. No live peer transcript or unaccepted AGSK result was read.

**Material result:** The minimal architecture does not depend on a second score or new artifact. A
finding needs a claim, observed fact/oracle, harm, material consequence and route; verification depth
follows claim/risk/oracle/evidence gaps; correction route follows the failed subject. Safety/security
remain explicit frozen material boundaries. Existing rungs remain authoritative for product/spec/
contract defects while evidence-only and record-only branches prevent false product loops.

**Uncertainty and continuation:** Challenge must attack the strongest scalar, sequential and dual-
judgment families, especially mixed findings, independently established claims with false records,
useful pre-existing tests, safety/security, and provider transport separation. Exact post-AGSK files
remain unavailable pending independent acceptance and landing. No new human-only Fact Candidate arose.

Stage complete: YES
→ User decision: Recommend close Extract and proceed to Challenge; no additional configuration family is needed unless the Coordinator identifies a missing authority or safety class.
