# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW_20260921-180000_RVAG](../../HL-TFW_20260921-180000_RVAG.md)
> Goal: Restore independent review as a gate on purpose, accepted value, and material quality, without letting immaterial process-record defects restart product execution.

## Consistency Check

Each row asks whether the two alternatives can govern the same finding without contradiction.

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D2: blocking predicate | Any cited breach blocks | D4: TRACE disposition | Record-only defect is non-blocking | The same grounded record error cannot both require a verdict return and leave the accepted conclusion/action unchanged. |
| D2: blocking predicate | Claim + harm + material consequence + evidence | D5: permanent-test admission | Green presence alone establishes a permanent guard | A passing test with no protected behavior, harm, or detection demonstration cannot satisfy the material-evidence predicate. |
| D3: verification-depth selection | Any discrepancy expands to 100% of changed files | D4: TRACE disposition | Only the affected material claim and dependencies reopen | An immaterial record discrepancy cannot simultaneously require unrelated full-file expansion and remain outside the affected claim. |
| D4: TRACE disposition | Material record split | D6: correction route | Every discrepancy returns to full Executor work | A branch defined as preserving unchanged VALUE cannot require a new product-execution round solely because its carrier is wrong. |
| D4: TRACE disposition | Every TRACE defect blocks | D6: correction route | Observation/no correction | A defect cannot be universally blocking and simultaneously owe no action. |
| D2: blocking predicate | Automatic score threshold decides | D6: correction route | Authority/safety acceptance routes to the human owner or exact delegated ruler | A score may inform a decision but cannot acquire human or mandate-bounded acceptance authority. |

**Surviving configurations** (including the explicit safety/security constraint added by the
Coordinator at the Extract gate):

| Config | D1 | D2 | D3 | D4–D7 summary | Notes |
|--------|----|----|----|----------------|-------|
| C3+ | VALUE → ASSURANCE → TRACE feeding one verdict | Five-field material predicate with explicit safety/security boundary | Claim/risk/oracle/evidence gaps | Material TRACE split; detection-power admission; class-selected route; fixed envelope | Passes all four boundary cases without a second verdict. |
| C4+ | Accepted-result verdict + record-health judgment | Same five-field predicate and safety/security boundary | Claim/risk/oracle/evidence gaps | Separate record health; class-selected route; fixed envelope | Passes all cases but creates two judgments that can drift or be mistaken for two acceptance authorities. |
| C10+ | VALUE → ASSURANCE → TRACE feeding one verdict | Same five-field predicate and safety/security boundary | Changed-dependency reach plus bounded residual sampling | Material TRACE split; class-selected route; fixed envelope | Passes when sampling is justified against residual material risk rather than a quota. |
| C11 | VALUE → ASSURANCE → TRACE feeding one verdict | Material predicate plus named safety/security, authority, identity, and continuation boundaries | Claim/risk/oracle with criticality floor | Material TRACE split; detection-power admission; class-selected route; fixed envelope | Makes the frozen high-consequence boundaries visible rather than relying on implication. |

**Unexpected survivor:** C4+ remains logically sound. A distinct record-health judgment can prevent
MFX-style false returns while still surfacing record quality. It was not initially favored because it
adds a second output, but none of the four boundary cases makes it incorrect. Its marginal value and
drift cost remain an explicit iteration-2 challenge rather than being silently dismissed here.

## Findings

### C1: Unsafe but functionally correct defeats a functionality-only value test

Suppose every requested output is correct, but the system leaks a secret, permits a hazardous
unintended action, or removes a safety interlock. `C0`, `C2`, and `C7` might still catch this through
their safety checklist row, but their architecture does not explain why that row must dominate a
green functional result. Any survivor needs the explicit rule: credible unsafe/insecure behavior,
or an evidence gap leaving a material safety/security claim unestablished, is a material VALUE or
ASSURANCE failure regardless of incident history, checklist frequency, or other green rows.

[NASA-STD-8739.8B](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398RevB.pdf)
defines software assurance to include intended and unintended behavior and separately requires safe
and secure systems. NASA's domain is not imported into TFW, but the counterexample is transferable:
correct intended output does not establish absence of dangerous unintended behavior. C3/C10 only
survive when strengthened to C3+/C10+; C11 states the boundary directly.

### C2: A correct result cannot legitimize an unauthorized external effect

A result may be functionally correct and well evidenced while the producing unit also pushed,
deployed, published, notified, spent funds, or modified an external system without authority. That
is not an immaterial process deviation. It changes the authorized world state, may be irreversible,
and may create legal, safety, privacy, or operational harm. The finding is material TRACE-authority
plus continuation/effect provenance. It routes to the human owner or exact delegated ruler named by
the task spine; product correctness neither retroactively grants authority nor tells the Executor how
to undo an effect.

[NIST SP 800-37 Rev. 2](https://csrc.nist.gov/pubs/sp/800/37/r2/final) separates assessment from
authorization: assessment supplies information, while a responsible senior official makes the
risk-based authorization decision. This is corroborative structure, not TFW authority. TFW's own
frozen contract remains controlling: the Reviewer verifies and proposes, the bounded Coordinator
rules only inside its grant, and human acceptance authority and reserved external effects remain
human. C6 fails because an automatic score cannot accept risk or cure missing authority. C5 fails
when an unlisted effect is auto-downgraded instead of reaching the real ruler.

### C3: Strong evidence bound to the wrong accepted-result identity is weak evidence for this review

Assume an exhaustive test suite, production observation, and signed evidence all prove Candidate A,
but the RF/REVIEW asks to accept Candidate B, another environment, or an output changed after the
measurement. Evidence strength does not transfer across an unproved identity relation. This is a
material ASSURANCE/TRACE-identity gap even when B happens to be correct. The route is to establish
the relation or collect affected evidence; it is record-only only after the actual accepted output,
dependencies, environment and oracle are reconstructably unchanged.

The [SLSA provenance model](https://slsa.dev/spec/v1.2/build-provenance) illustrates the identity
principle by binding a particular build platform execution to produced artifacts, inputs, resolved
dependencies and digests. RVAG remains domain-agnostic and does not require SLSA, but the challenge
shows why an enclosing green run or impressive test volume cannot substitute for binding evidence to
the accepted subject. C1/C8 still risk excessive audit work, but they correctly block if identity is
unresolved; C3+/C4+/C10+/C11 block only the affected claim and relation.

### C4: An immaterial citation defect must remain visible without becoming a product loop

Assume a citation points to the wrong heading, while the primary source exists, the Reviewer opens it,
and independent evidence establishes the material claim against the correct result and environment.
The citation is false and should be corrected or recorded, but no accepted conclusion or authorized
action changes. Returning product execution would recreate MFX. If the bad citation is the only
support for a material claim, however, the same surface defect becomes an ASSURANCE gap and blocks.

This stress test defeats filename-based classification and blanket rules in both directions. “All
citations block” produces false returns; “citations never block” produces false approvals. The
five-field predicate distinguishes the cases by evidence applicability and consequence.

### C5: Human acceptance authority survives every configuration

No surviving configuration lets Reviewer or Coordinator turn evidence into owner acceptance outside
the recorded mandate. Reviewer determines whether claims are established and records `APPROVE`,
`REVISE`, or `REJECT`; it does not accept an unauthorized effect, waive safety/security risk, amend a
frozen contract, or decide `not fit for purpose` for the owner. The Coordinator may rule only within
the immutable grant in `status.md`/HL; owner-reserved purpose, contract, external-effect, and risk
acceptance decisions return to the owner.

This also constrains the compact envelope: it reports the durable verdict and artifact identity; it
does not say “accepted by owner,” perform an effect, or create authority through transport.

### C6: Test-deletion and metric-substitution attacks

The proposed admission contract keeps four useful guard classes without making historical red the
only gate:

| Guard class | Detection demonstration | Challenge result |
|---|---|---|
| Newly corrected behavior | Historical red-before-green on the corrected failure | Admitted when the failure is relevant to the named harm. |
| Existing behavior/contract | Targeted mutant, broken fixture, fault injection, or other relevant negative control | Admitted without fabricating a historical bug. |
| External receiver/environment | Failure exposed only in a representative external fixture or actual environment | Admitted when the internal producer cannot observe the integration failure. |
| Positive control/health check | Shows the instrument runs or environment responds | Retained as a control, not counted as an independent regression guard. |

Coverage, mutation score, test count, commit count and green status can inform the Reviewer but do
not satisfy admission alone. This prevents both false deletion of characterization tests and growth
of a new score-driven test bureaucracy.

### C7: Bureaucratic-growth attack leaves no need for a new carrier

The five blocking elements need not become five new fields in every artifact; they can be one
structured finding sentence/table row in the existing REVIEW. `Subject/authority` and
`observed fact/oracle` are already implicit in current findings, while harm, consequence and route
are partly present in Purpose Check and the rung table. The change is to make the predicate universal
and to use existing correction branches consistently.

C4+ survives logic but pays for a second judgment that C11 can encode as finding classification plus
one terminal verdict. No boundary case yet requires the second judgment, new score, registry, stage,
or artifact. Under the subtraction principle, C11 and C3+ have the smaller semantic surface; C4+
remains a deliberate counter-hypothesis for iteration 2.

### C8: Configuration eliminations and hypothesis state after iteration 1

| Config(s) | Challenge outcome | Reason |
|---|---|---|
| C0, C2, C7 | Eliminated | Any grounded discrepancy can still force a false return; transport or risk-depth changes alone do not repair the predicate. |
| C1, C8 | Eliminated as stated | Fixed ratio and blanket escalation remain governing proxies, contrary to frozen DoD 7; they could survive only if subordinated, which turns them into C3+/C10+/C11 behavior. |
| C5 | Eliminated | Closed enumerations miss novel material harms and invite unlisted authority/safety defects to become discretion. |
| C6 | Eliminated | Scores recreate metric substitution and cannot supply acceptance authority. |
| C9 | Eliminated against the frozen contract | Semantics hold, but durable REVIEW alone omits the required compact addressed return. |
| C3, C10 | Survive only as C3+/C10+ | Safety/security must be explicit, not inferred. |
| C3+, C4+, C10+, C11 | Survive iteration 1 | All four boundary cases and the MFX/TLD/CRATM/FRATS contrasts remain correctly classified. |

| Hypothesis | Iteration-1 state | Grounds |
|---|---|---|
| H1 | Supported, not final | One verdict plus universal classification and route passes every case; C4+ remains a live but costlier counter-hypothesis for iteration 2. |
| H2 | Supported with safety floor | Claim/risk/oracle/evidence selection handles material gaps; fixed ratios add no demonstrated protection. |
| H3 | Supported | Authority, accepted-result identity, material proof, safety/security provenance and authorized next action form the deterministic TRACE boundary. |
| H4 | Supported | Protected behavior, harm and a relevant counterfactual retain useful existing tests while excluding green/count-only proxies. |
| H5 | Supported | MFX repeats known F31/F32 process-proxy failures and contrasts with material TLD/CRATM/FRATS returns. |
| H6 | Supported | Existing stage/REVIEW/rung/recovery carriers suffice; deletion/subordination dominates new machinery. |
| H7 | Partially supported; transport pending | Durable REVIEW + compact semantic envelope is sufficient in Codex reasoning, but exact overlap waits for accepted AGSK Phase B landing and independent provider evidence. |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Four configurations survive after explicit safety/security strengthening; one-verdict C11/C3+ and dual-judgment C4+ are the main iteration-2 contest. | Iteration 2 must attempt a case where separate record health changes a safe decision that one classified verdict cannot express. |
| All four Coordinator boundary cases are classified without weakening product, safety, security, authority, identity, or human acceptance. | Exact provider return mechanics and final overlap remain pending accepted AGSK landing. |
| Five-field material predicate blocks false approval and false return while permitting evidence-only and record-only correction. | Implementation grammar, field compression and exact carriers belong to later planning after iteration 2. |
| No new artifact, score, registry, stage, or permanent suite is required by the challenged cases. | Iteration 2 must actively search for a counterexample requiring one. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Pairwise incompatibility checked? Surviving configurations listed?

### Material handover at this checkpoint

**Producer and unit:** Researcher, `codex:thread:local:01a0c7ba-6045-7ab0-b261-11cec3ca1af5`.

**Bounded source/epoch:** Briefing, Gather and Extract in this iteration; RVAG frozen HL and current
framework HEAD `8528730c46f74df5f8e881c658ff5e419bfb92d9`; durable MFX/TLD/CRATM/FRATS cases;
NASA-STD-8739.8B, NIST SP 800-37 Rev. 2 and SLSA Build Provenance linked above. External sources
corroborate safety, authority separation and evidence identity but do not grant TFW authority.

**Material result:** C11/C3+ show that one terminal verdict can preserve VALUE, ASSURANCE, material
TRACE, safety/security and human authority when every blocking finding names its material consequence
and correction route. C4+ remains logically valid but has no demonstrated marginal decision power.
Unauthorized effects and wrong result identity block even with correct outputs or strong evidence;
an immaterial citation error does not block once the material claim is independently established.

**Uncertainty and continuation:** H1–H6 are supported only for iteration 1 and must be adversarially
retested in iteration 2. H7 remains partial until accepted AGSK Phase B landing supplies the actual
provider transport denominator. No new human-only Fact Candidate arose.

Stage complete: YES
→ User decision: Recommend close Challenge and synthesize iteration 1; preserve C4+ and the AGSK dependency as explicit iteration-2 targets.
