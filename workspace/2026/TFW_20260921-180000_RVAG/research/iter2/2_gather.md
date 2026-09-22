# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260921-180000_RVAG](../../HL-TFW_20260921-180000_RVAG.md)
> Goal: Restore independent review as a gate on purpose, accepted value and material quality, while preventing administrative record defects from restarting unchanged product execution.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D _(if any)_ |
|-----------|-------|-------|-------|-----------------|
| D1: Decision topology | One terminal verdict with classified per-item findings | Separate value and record-health verdicts (C4+) | Ordered VALUE / ASSURANCE / TRACE sub-verdicts plus terminal verdict | Numeric or weighted score |
| D2: Mixed-round aggregation | Highest rung controls every item | Each item follows its own route; terminal verdict names one next executable act | Split the review into separate formal rounds by class | Return only the highest-severity item and defer the rest |
| D3: Blocking predicate | Any discrepancy or breached criterion | Affected claim/authority + observed fact/oracle + harm + material consequence + completion route | Fixed severity threshold | Risk-owner acceptance alone |
| D4: Evidence/result identity | Evidence carrier exists | Evidence names subject revision | Evidence binds subject, revision, environment, oracle and authority | Independent reproduction makes original identity irrelevant |
| D5: Verification selection | Changed-file ratio with discrepancy escalation | Material claims, risk, dependencies, environment, oracle and evidence gaps | Universal full audit | Reviewer discretion without explicit selection record |
| D6: Test/check admission | Presence and green result | Red-before-green only | Protected behavior/invariant + failure consequence + relevant counterfactual detection | Suite-wide score threshold |
| D7: Provider return ownership | Every adapter duplicates payload and transport | Canonical Review owns payload/ordering; adapter owns only evidenced transport | New provider-neutral message-schema artifact | Durable REVIEW alone, with no addressed terminal signal |
| D8: Propagation surface | Canonical workflow/templates only | Canonical semantics + shared conventions/config/glossary | Canonical semantics + every adapter rule/readme | New registry/stage plus release metadata |

## Findings

### G1: Iteration 1 is falsifiable on six explicit boundaries

Iteration 1's D1–D7 form one candidate, not a conclusion: ordered `VALUE → ASSURANCE → TRACE`, one
terminal verdict, five-field material findings, claim/risk/oracle verification, detection-power test
admission, class-selected routes and existing carriers. D8 leaves C4+ alive only if it can change a
safe authorized decision; D9 leaves provider overlap to this accepted-AGSK pass. The six predecessor
threads make the attack observable: a surviving counterexample must defeat single-verdict decision
power, mixed routing, safety/human authority, evidence identity, accepted transport separation, or
existing-carrier sufficiency.

### G2: The accepted AGSK landing supplies Antigravity transport, not Reviewer payload semantics

The accepted lineage is durable and present: both AGSK phases and the task are `DONE`; independent
REVIEWs approve Candidates `68dd9ce` and `bde7334`; the closure commit is `7cb2991`; tagged release
`v3.5.0` at `16cbb8f845511c68b55cfa3e57c12e32116253a2` is an ancestor of the inspected HEAD.
Only these accepted artifacts and landed files were inspected—no live transcript, unaccepted draft,
or private role reasoning.

AGSK adds the concrete Antigravity mechanism in `.agents/rules/tfw.md`, its byte-identical adapter
template, and `.tfw/adapters/antigravity/README.md`: strip the
`antigravity:thread:local:` prefix from `coordinator_route`, call native `send_message`, and report
Reviewer REV start plus the terminal verdict. That establishes provider-specific addressed transport
and the vertical recipient. It does **not** define RVAG's exact terminal payload, require
`artifact@ref`, require the durable REVIEW and authorized status/journal effect before sending, or
classify VALUE/ASSURANCE/TRACE findings. Those remain canonical Reviewer semantics rather than a
reason to rewrite AGSK transport.

### G3: The active Review still has the two iteration-1 false-return triggers

`.tfw/workflows/review.md` still requires at least `ceil(files × min_verify_ratio)` and escalates any
discrepancy to 100%; both project-config copies still carry `min_verify_ratio: 0.42`. The workflow
issues one verdict but does not require every blocking finding to name material harm and a
class-specific completion route. `conventions.md` states that a rung belongs to an item, yet the
highest required authority controls a mixed round and any rung-2 item creates one TS revision for
the whole executable round. This can preserve authority while still dragging unchanged VALUE and
record-only items into a product-execution-shaped return.

### G4: Mixed rounds require per-item disposition before aggregation

The adversarial matrix separates the item that controls the terminal verdict from the fate of every
other item:

| Round | Material item | Other item | Safe aggregate behavior | Failure if treated as one undifferentiated round |
|---|---|---|---|---|
| M1 | Wrong business behavior | Stale label/count | Return the failed VALUE claim; repair/observe the record item without making it product work | The record item enlarges TS/execution or appears to justify the return |
| M2 | Material claim unestablished | Independently verified correct result | Return the ASSURANCE gap while preserving Candidate identity unless VALUE changes | Product is reimplemented merely to repair evidence |
| M3 | Unauthorized effect or wrong ruler | Harmless wording defect | Hard-stop on authority; dispose the wording item separately | A clean product or tidy record legitimizes an unauthorized act |
| M4 | Unsafe/security-relevant behavior | Perfect trace | Block on VALUE/ASSURANCE safety boundary | Materiality is misused as permission to waive low-frequency severe harm |
| M5 | False sole evidence carrier | Same false carrier with independent sufficient proof | First is an ASSURANCE failure; second is record-only correction/observation | Classification follows the filename rather than whether the claim remains established |

One terminal verdict can safely aggregate these only if each item retains its subject, consequence,
owner and completion route. “Highest authority controls the round” is valid for who must rule, but
does not entail that every item changes the TS, Candidate or product execution.

### G5: Safety and identity sources support explicit non-waivable boundaries, not a new score

[NASA-STD-8739.8B](https://standards.nasa.gov/standard/nasa/nasa-std-87398) requires a systematic
software-assurance/safety approach coordinated with system safety, reliability and security, while
allowing the application approach to vary with the system. That supports risk-scaled depth with an
explicit safety/security floor; it does not support waiving severe harm because occurrence is rare
or because a general materiality score is low.

[SLSA 1.2 provenance](https://slsa.dev/spec/v1.2/provenance) defines provenance as verifiable
information linking an artifact to how it was produced, and the
[SLSA source requirements](https://slsa.dev/spec/v1.2/source-requirements) bind source verification
to the delivered revision identifier in `subject.digest`. RVAG does not import SLSA conformance, but
the identity principle is transferable: evidence for one Candidate/revision or environment cannot
silently establish another.

[NIST's structured-assurance work](https://www.nist.gov/programs-projects/measurement-metrics-and-assurance)
organizes assurance around claims, arguments and evidence. This corroborates item-level claim→proof
reasoning and exposes why evidence volume, file population or one global score cannot replace the
question “does this evidence establish this material claim?”

### G6: C4+ still lacks marginal decision power

The strongest candidate C4+ case is an accepted result with a deficient record. Existing REVIEW §5
and §6 already express the deficiency, its consequence, finite correction and preserved acceptance;
the terminal verdict can remain APPROVE. If the record defect instead changes authority, accepted
result identity, material proof, safety provenance or an authorized next action, it is no longer a
separate health-only fact—it is a material TRACE or ASSURANCE item that changes the existing verdict.
No gathered case yet produces a safe action available only through a second record-health verdict.

### G7: Existing carriers can express every gathered outcome

The current `review/{map,verify,judge}.md`, durable REVIEW §§2–6, task/phase `status.md` plus journal,
and exact addressed terminal message already cover understanding, proof, judgment, per-item
disposition, verdict/state and coordination. The observed deficiency is field semantics and routing,
not storage capacity. A new score, registry, stage, artifact or message-schema file would duplicate
an existing carrier and introduce a second source of truth.

### G8: The candidate post-AGSK denominator splits into semantic, propagation and release-owned clusters

Gather does not select a configuration, but the actual obligations map to three clusters:

| Cluster | Existing files implicated | Open question for Extract |
|---|---|---|
| Canonical Reviewer semantics | `.tfw/workflows/review.md`; `.tfw/templates/review/{verify,judge}.md`; `.tfw/templates/REVIEW.md`; `.tfw/conventions.md` | Which files need an actual rule change rather than explanatory duplication? |
| Active config/terminology | `.tfw/project_config.yaml`; `.tfw/templates/project_config.yaml`; `.tfw/glossary.md` | Delete/subordinate `min_verify_ratio`; align terms only where consumers would otherwise retain the old rule |
| Release/migration | existing release workflow plus the later `3.5.1` version/changelog/migration effect | Which paths belong to post-acceptance `/tfw-release`, not the RVAG implementation Candidate? |

The accepted AGSK transport files are a protected dependency, not presumptive RVAG edit targets.
The Codex and installed Review skills are thin routers into the canonical workflow, so copying
Reviewer semantics into them would add drift without changing behavior.

## OODA

- **Observe:** Re-read predecessor decisions/open threads; verified the accepted AGSK status,
  independent approvals, accepted commits/tag and current landed messaging surfaces; inspected the
  active Review workflow/templates/config/routing rule; consulted primary NASA, SLSA and NIST sources.
- **Orient:** AGSK closes the provider-transport uncertainty, while the verdict, verification and
  mixed-round defects remain canonical Review concerns. External evidence strengthens safety and
  result-identity boundaries rather than creating a metric.
- **Decide:** Carry eight independent dimensions and five mixed-round cases to Extract. Keep C4+ and
  new-carrier alternatives alive only for a demonstrated marginal safe decision.
- **Act:** Map configurations and derive the minimum semantic file denominator in `3_extract.md`.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Accepted AGSK proves Antigravity addressed transport and `3.5.0` ownership; RVAG still owns exact payload, ordering and value semantics. | Select the surviving configuration and exact existing-file denominator. |
| Mixed rounds need per-item classification/disposition even when one highest authority controls the aggregate round. | Define the aggregate rule without weakening authority, safety or human acceptance. |
| No C4+ or new-carrier case yet changes a safe authorized decision. | Challenge the strongest counterexamples after configuration mapping. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?

Stage complete: YES
→ User decision: Parent Coordinator approved Gather with no missing adversarial dimension and directed Extract to formalize per-item subject/consequence/owner/route plus one aggregate verdict without dragging unchanged VALUE onto the highest rung; accepted AGSK transport files remain protected absent a demonstrated compatibility gap.
