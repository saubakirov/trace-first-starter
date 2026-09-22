# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260921-180000_RVAG](../../HL-TFW_20260921-180000_RVAG.md)
> Goal: Restore independent review as a gate on purpose, accepted value, and material quality, without letting immaterial process-record defects restart product execution.

## Dimensions

The cases expose seven independent decision factors. Alternatives are intentionally unordered and unselected at Gather.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1: verdict architecture | One scalar verdict aggregated from checklist rows | VALUE → ASSURANCE → TRACE sequence feeding one terminal verdict | Separate accepted-result verdict and record-health judgment | Current ten-row checklist with local exceptions |
| D2: blocking predicate | Any breached approved criterion or frozen claim | Affected claim + concrete harm + material consequence + evidence | Risk/criticality threshold matrix | Explicit owner/contract enumeration of blocking classes |
| D3: verification-depth selection | Fixed changed-file ratio with discrepancy escalation | Material claims, analysed risk, oracle strength, and evidence gaps | Changed-dependency reach plus bounded sampling | Criticality tiers with minimum prescribed techniques |
| D4: TRACE disposition | Every false or stale accepted-record statement blocks | Deterministic split by authority, result identity, material proof, safety, or next action | Separate record-only correction route | Observation unless an authorized decision-maker escalates |
| D5: permanent-test admission | Historical red-before-green only | Protected behavior + failure consequence + demonstrated counterfactual detection | Mutation-score or coverage threshold | Green presence in the configured suite |
| D6: correction owner and route | Full Executor round for every blocking discrepancy | Same-carrier record-only correction without product execution | Evidence-only correction with bounded same-Reviewer follow-up | Observation/no correction when no accepted conclusion or action changes |
| D7: terminal return | Durable REVIEW only | Durable REVIEW plus one fixed compact addressed envelope | Durable REVIEW plus narrative message | Provider-specific return forms with a shared semantic minimum |

## Findings

### G1: Current TFW mixes value, assurance, and record correctness into one scalar return

The active Review workflow verifies at least `ceil(changed files × 0.42)` and escalates every
discrepancy to 100% file verification. `verify.md` repeats the escalation for any discrepancy and
for any unresolved or semantically wrong knowledge citation. `judge.md` then aggregates ten
universal rows into one `APPROVE`, `REVISE`, or `REJECT`; rows distinguish evidence existence from
evidence sufficiency, but the terminal route does not distinguish a product correction from a
record-only correction. A `REVISE` proposal needs a breached TS criterion or frozen HL claim, yet no
second predicate requires that the breach change a material value, assurance, authority, or
continuation conclusion.

The checklist also carries historical non-green rates as retention evidence. Those rates explain why
a question exists, but they do not establish the materiality of a finding in the current result. The
same architecture therefore contains both a strong Purpose Check with a materiality test and weaker
rows where a formally breached claim can still drive the scalar verdict without a shared harm test.

Current canonical locations: [review workflow](../../../../../.tfw/workflows/review.md),
[Verify template](../../../../../.tfw/templates/review/verify.md),
[Judge template](../../../../../.tfw/templates/review/judge.md),
[REVIEW template](../../../../../.tfw/templates/REVIEW.md), and
[project configuration](../../../../../.tfw/project_config.yaml).

### G2: MFX is a repeated false-return class, not a single careless review

The committed Helpdesk range `1e1dcc6..95085d0` contains 35 commits, two belonging to concurrent
UPM, hence 33 MFX task commits after the first working product Candidate. Thirty-one touch the MFX
task trace. Summed per-commit task-trace churn is +3,986/−250 lines. There are no later commits or
endpoint changes under `code/mcp-plugin/src/` or `k8s/`. These figures reproduce HL §2.1; the method
used `git rev-list`, path-restricted history, and per-commit `git log --numstat` in the Helpdesk
repository at `95085d0`.

The first REVIEW independently verified product behavior, production identity, the configured suite,
security properties, and purpose alignment. It still returned the task because the RF contained an
unreproducible rename statement, one supposed red-before-green guard was actually red because a file
was absent, the TS had stale amendment wording, and citations or counts in the record were wrong.
That REVIEW explicitly said its evidence-sufficiency failures did not concern product operability.

Revision 2 returned seven record claims: a summary/count mismatch, one evidence row outside its
declared buckets, stale run epochs, an incorrect byte-identity statement, stale amendment status in
three carriers, an unresolved ONB citation, and wording already disproved in the prior round.
Revision 3 returned two remaining record defects plus a round-label correction. Revision 4 approved
the unchanged product, then found three more count/selector/attribution defects and classified all
three `not material`. The decisive variable was not whether the statement was false—false statements
appeared in every round—but whether it changed the accepted result, material proof, authority, or an
authorized next action.

Durable sources: Helpdesk `HD_20260920-133958_MFX` REVIEW revisions 1–4 and Git objects through
`95085d0`; no live role transcript was read.

### G3: Contrasting returns show why TRACE and assurance cannot become non-blocking by default

Three durable counterexamples separate necessary returns from MFX-style false loops:

- **TLD — product/transport defect.** The primary Claude Code adapter substituted `$0` in the newly
  shipped discovery command, making the release's headline operation invalid for every slash-command
  invocation. The canonical source was byte-identical and the rest of the result was strong, but the
  accepted mechanism failed at its actual point of use. `REVISE` correctly cited the breached AC and
  routed a one-line product correction.
- **CRATM Phase C — authority-path defect.** The shipped Plan consumer omitted the ordinary
  owner-direct branch and could STOP a valid non-delegated workflow; adjacent canonical sentences
  preserved contradictory signing authority. Missing contemporaneous staging evidence and an
  inexact digest boundary were additional assurance failures. The first three findings changed who
  could act and whether a valid path continued, so they were material even though much of the corpus
  and test suite passed.
- **FRATS Phase B — material proof defect with unchanged product.** Earlier semantic-replay output
  could not establish preservation because it lacked executable predicates and a reproducible
  command. The correction added executable positive and paired negative checks while preserving the
  Candidate. Revision 3 approved the same product identity after the affected proof became
  reproducible. This is a legitimate evidence-only return, distinct from a product-execution round.

The non-code/purpose contrast is already preserved in `knowledge/process.md` F31: seven technically
rigorous reviews across TFW-48/49, six approving, still produced work the owner rejected wholesale
because review measured downstream specifications rather than the governing purpose. A value gate
must therefore be able to reject a polished document or analysis that is beside the point.

Local sources: `TFW_20260830-194027_TLD` REVIEW,
`TFW_20260902-111644_CRATM/phase-c` REVIEW, and
`TFW_20260920-223357_FRATS/phase-b` REVIEW revision 3.

### G4: External sources support claim/risk/oracle selection, but not a new universal score

[ISO/IEC/IEEE 29119-1:2022](https://www.iso.org/obp/ui#iso:std:iso-iec-ieee:29119:-1:ed-2:v1:en)
describes exhaustive testing as impractical, makes the test basis and oracle important, and uses
risk-based testing to prioritize and focus testing. Its definition makes selection and use of
testing activities consciously depend on analysed types and levels of risk. This supports replacing
a file-count denominator with an explicit selection rationale; it does not prescribe RVAG's exact
decision grammar.

The [NIST assurance glossary](https://csrc.nist.gov/glossary/term/assurance) defines assurance as
grounds for justified confidence relative to specific claims, obtained through credible evidence.
NASA's [Software Assurance guidance](https://swehb.nasa.gov/spaces/SWEHBVB/pages/32604457/SWE-022%2B-%2BSoftware%2BAssurance)
ties assurance to product quality, safe and reliable operation, customer needs, independent
reporting, and effort tailored by classification, criticality, and risk. Together they distinguish
the claim being protected from the existence of a process record.

Mutation evidence is useful but must remain claim-specific. Papadakis et al.'s
[large-scale ICSE study](https://ieeexplore.ieee.org/document/8453121/) found mutation score's
correlation with real-fault detection becomes weak when test-suite size is controlled, although
higher mutation scores can guide improvement relative to same-size suites. A targeted mutant or
counterfactual can therefore demonstrate that a named guard detects a relevant failure; a universal
mutation-score threshold would be another proxy.

### G5: The post-AGSK return surface is not yet eligible for final mapping

At the inspected RVAG epoch `8528730c46f74df5f8e881c658ff5e419bfb92d9`, the current Review workflow
requires return only to `coordinator_route` but does not define the frozen compact envelope.
`TFW_20260921-220500_AGSK/phase-b/status.md` is at lifecycle `RF`, not an independently accepted
REVIEW/landing. Its live RF was not consumed. Gather can separate semantics now—RVAG owns Reviewer
payload, timing, and value meaning; AGSK owns Antigravity transport—but cannot name the final overlap
or file denominator until the accepted AGSK result lands and is rebased.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Seven independent design dimensions and their alternatives. | Extract must map case configurations to verdict effects and eliminate coupled dimensions. |
| The active scalar route allows any grounded discrepancy to become a full REVISE even when no material conclusion changes. | Determine the smallest universal predicate and whether one verdict or separate judgments express it best. |
| MFX reproduces the false-return class; TLD, CRATM, FRATS, and F31 supply material product, authority, proof, and purpose counterexamples. | Derive a deterministic TRACE split and correction owner/route from those contrasts. |
| External sources support claim/risk/oracle/evidence selection and warn against metric substitution. | Translate that support into provider- and domain-neutral TFW grammar without importing a new score. |
| AGSK Phase B is not yet independently accepted. | Final post-AGSK overlap and exact file surface remain a declared dependency, not a guessed answer. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified? _(seven independent factors mapped)_

### Material handover at this checkpoint

**Producer and unit:** Researcher, `codex:thread:local:01a0c7ba-6045-7ab0-b261-11cec3ca1af5`.

**Bounded source/epoch:** RVAG Contract Baseline
`db61ecac1a7f0743036f84a5d5075ca727b5364c`; current framework HEAD
`8528730c46f74df5f8e881c658ff5e419bfb92d9`; canonical Review workflow/templates/config named
above; Helpdesk MFX Git range `1e1dcc6..95085d0` and REVIEW revisions 1–4; TLD, CRATM Phase C, and
FRATS Phase B durable REVIEW artifacts; current knowledge decisions/facts cited by the HL; ISO,
NIST, NASA, and ICSE sources linked above. No peer transcript or unaccepted AGSK RF was read.

**Material result:** MFX's cost is produced by a missing universal materiality predicate and a route
that equates product work with record correction, not by lack of independent verification. Necessary
returns still exist where purpose, behavior, authority, accepted-result identity, safety, or material
proof changes. Fixed file ratios, discrepancy escalation, test counts, and mutation scores are
candidate diagnostics, not acceptance outcomes.

**Uncertainty and continuation:** Extract must decide whether a single terminal verdict with a
universal predicate is sufficient, map deterministic TRACE and evidence-only routes, and isolate
subtractions from additions. The exact AGSK overlap remains unavailable until independent acceptance
and landing. No new human-only Fact Candidate arose in this stage.

---
Stage complete: YES
→ User decision: Recommend close Gather and proceed to Extract; no deeper Gather pass unless the Coordinator identifies a missing case class.
