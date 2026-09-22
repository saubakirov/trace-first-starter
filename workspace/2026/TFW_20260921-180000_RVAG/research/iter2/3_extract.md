# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260921-180000_RVAG](../../HL-TFW_20260921-180000_RVAG.md)
> Goal: Restore independent review as a gate on purpose, accepted value and material quality, while preventing administrative record defects from restarting unchanged product execution.

## Configuration Space

The table keeps only non-obviously-contradictory representatives from the eight Gather dimensions;
each row changes at least one dimension from C1.

| Config | D1: Decision topology | D2: Mixed-round aggregation | D3: Blocking predicate | D4: Evidence/result identity | D5: Verification selection | D6: Test/check admission | D7: Provider return ownership | D8: Propagation surface |
|--------|-----------------------|-----------------------------|------------------------|------------------------------|----------------------------|--------------------------|-------------------------------|-------------------------|
| C1 | One terminal verdict + classified items | Per-item route + one next executable act | Five-field material consequence | Bound subject/revision/environment/oracle/authority | Claim/risk/dependency/gap | Behavior + harm + relevant counterfactual | Canonical payload; adapter transport | Canonical + shared rules/config/terms |
| C2 (C4+) | Separate value and record-health verdicts | Per-item route + one next executable act | Five-field material consequence | Bound tuple | Claim/risk/dependency/gap | Behavior + harm + relevant counterfactual | Canonical payload; adapter transport | Canonical + shared rules/config/terms |
| C3 | Ordered VALUE/ASSURANCE/TRACE sub-verdicts + terminal verdict | Per-item route + one next executable act | Five-field material consequence | Bound tuple | Claim/risk/dependency/gap | Behavior + harm + relevant counterfactual | Canonical payload; adapter transport | Canonical + shared rules/config/terms |
| C4 | One terminal verdict + classified items | Highest rung recasts every item | Five-field material consequence | Bound tuple | Claim/risk/dependency/gap | Behavior + harm + relevant counterfactual | Canonical payload; adapter transport | Canonical + shared rules/config/terms |
| C5 | One terminal verdict + classified items | Per-item route + one next executable act | Five-field material consequence | Carrier/revision identity | Changed-file ratio + discrepancy escalation | Green presence | Canonical payload; adapter transport | Canonical + shared rules/config/terms |
| C6 | One terminal verdict + classified items | Per-item route + one next executable act | Fixed severity threshold + risk-owner override | Bound tuple | Claim/risk/dependency/gap | Behavior + harm + relevant counterfactual | Canonical payload; adapter transport | Canonical + shared rules/config/terms |
| C7 | One terminal verdict + classified items | Per-item route + one next executable act | Five-field material consequence | Bound tuple | Claim/risk/dependency/gap | Behavior + harm + relevant counterfactual | Every adapter duplicates payload and transport | Canonical + all adapter rules/readmes |
| C8 | One terminal verdict + classified items | Per-item route + one next executable act | Five-field material consequence | Bound tuple | Claim/risk/dependency/gap | Behavior + harm + relevant counterfactual | New provider-neutral message schema | New schema/registry/stage + canonical propagation |
| C9 | One terminal verdict + classified items | Split formal round per finding class | Five-field material consequence | Bound tuple | Universal full audit | Red-before-green only | Canonical payload; adapter transport | Canonical + shared rules/config/terms |

## Findings

### E1: A finding is the unit of classification, consequence and payment

The smallest item model that survives every Gather case is:

| Field | Required meaning | Why it cannot be inferred |
|---|---|---|
| `subject` | `VALUE`, `ASSURANCE`, or `TRACE` | Artifact path does not reveal what failed. |
| `claim_or_authority` | Accepted claim, frozen clause, result identity or ruler affected | A generic discrepancy cannot ground a return. |
| `observed_fact_and_oracle` | What was observed and the basis for calling it false/insufficient | Separates proof from assertion. |
| `harm` | Concrete effect on purpose, behavior, safety, authority, trust or continuation | “Breached AC” alone does not establish consequence. |
| `material_consequence` | Acceptance conclusion or authorized action that changes | Distinguishes blocking work from an observation/record repair. |
| `owner` | Existing actor/ruler who can complete or accept the condition | Reviewer independence forbids self-repair or invented authority. |
| `completion_condition` | Observable state that closes this item | Prevents open-ended revision loops. |
| `route` | Product/spec return, assurance-only return, ruler stop, record-only repair, or observation | Mixed rounds cannot safely infer a shared route from verdict alone. |
| `candidate_effect` | `changes` or `preserved` | Makes unchanged VALUE explicit in assurance/record-only work. |

The four fields named by the Coordinator—subject, consequence, owner and route—are the irreducible
dispatch core. The remaining fields make those four testable rather than labels.

### E2: One aggregate verdict follows item classification without flattening the items

The candidate aggregation algorithm is deterministic:

1. Classify every real finding independently using E1. An immaterial item is still visible but has
   `record-only repair` or `observation`, not an executable product return.
2. Protect non-delegable boundaries before ordinary aggregation: wrong purpose/contract, reserved
   human acceptance, unauthorized effect, safety/security risk acceptance and unresolved result
   identity route to their exact ruler and stop incompatible execution.
3. If any material item is executable under the current contract, the terminal verdict is `REVISE`;
   if a fundamental purpose/contract result is unfit, use `REJECT`/owner route; otherwise `APPROVE`.
4. Highest required authority controls the **sequence and next authorized act**, not the semantic
   class of every lower item. A rung-3 item can stop the round without turning a record typo into an
   HL amendment. A rung-2 item can require one TS revision without converting an assurance-only or
   record-only item into VALUE work.
5. The Coordinator rules one round, but each item keeps its completion condition and
   `candidate_effect`. Only a route that changes accepted VALUE moves the Candidate; proof-only and
   record-only work preserve it unless actual VALUE changes during correction.

This is the combination not explicit in the Briefing: one terminal verdict and one authority-ordered
next act, while multiple item routes remain semantically distinct inside that act.

### E3: C4+ is decision-equivalent to C1 and adds an inconsistent state space

For every record-health state:

- If it changes no acceptance conclusion or authorized action, C1 records it as a visible
  observation or finite record-only repair while retaining the terminal verdict.
- If it changes authority, result identity, material proof, safety/security provenance or the next
  authorized action, C1 classifies it as material TRACE/ASSURANCE and the terminal verdict changes.

Therefore a second record-health verdict has no distinct safe action. It creates extra combinations
(`VALUE=accept`, `RECORD=fail`, for example) whose operational meaning must be translated back into
the same per-item routes. C3's ordered questions remain useful as reasoning order, but three stored
sub-verdicts are likewise unnecessary; the item subject preserves the distinction without another
acceptance surface.

### E4: Evidence identity is a tuple, and redundancy changes classification

Use the bounded identity tuple
`{accepted subject, revision/Candidate, relevant environment, oracle/authority, dependency state}`.
Evidence establishes a claim only if the tuple matches or an explicit equivalence is proved.

- A false/stale carrier that is the sole support leaves the material claim unestablished: an
  `ASSURANCE` failure.
- The same carrier, when independent evidence already establishes the same claim for the same tuple,
  is a `TRACE` record-only correction or observation.
- Evidence for another Candidate, environment or ruler is not made applicable by a green result or
  enclosing commit SHA.

SLSA's requirement to bind source verification to the delivered revision identifier is an external
identity example, not an imported TFW control. It supports the tuple while leaving domain-specific
oracles and equivalence to the approved contract.

### E5: Verification is a selection argument, not a population ratio

Replace `ceil(files × min_verify_ratio)` and “any discrepancy → 100%” with a recorded selection:

1. enumerate material claims, protected authority/safety boundaries and actual changed dependencies;
2. select the affected behavior, inputs/outputs, relevant environment and oracle needed to establish
   each claim;
3. inspect broader dependencies only when the risk, observed uncertainty or failure mechanism makes
   them capable of changing the conclusion;
4. state unverified limits and route any acceptance-critical gap;
5. never count unrelated files as assurance merely because they were opened.

[NIST SP 800-53A Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) describes assessment
procedures as tailorable to organizational risk processes and risk tolerance. It is security-specific,
so RVAG imports no control catalog; the transferable point is that depth and coverage are selected
attributes supporting a risk decision rather than one universal file fraction.

### E6: Test admission needs an item-level detection argument

Classify a check as one of:

- **permanent guard:** names protected behavior/invariant, failure consequence, and demonstrated
  relevant counterfactual detection;
- **temporary diagnostic:** helps investigate or measure but is not retained as a guard;
- **positive control:** proves the harness can observe success but is not independent failure
  detection;
- **governance/trace assertion:** protects an actual authority or continuation mechanism, not product
  quality by default.

Historical red-before-green is preferred for newly corrected behavior. Existing contracts may use a
targeted mutant, fault injection, external fixture or another demonstrated negative control. Suite
counts and global mutation scores remain diagnostic, not admission authorities.

### E7: The compact terminal payload is fixed; transport remains provider-owned

The provider-neutral payload is exactly:

```text
REVIEW · <reviewer-unit> · <task-or-phase> · <verdict> · <review-artifact@ref>
```

Semantic rules:

1. write the durable REVIEW and authorized status/journal effect first;
2. send exactly one terminal envelope to the exact recorded `coordinator_route`;
3. use the actual Reviewer unit, task/phase identity, terminal verdict and resolvable artifact path plus
   immutable ref; do not repeat findings prose;
4. the envelope is a continuation signal, never acceptance authority, evidence replacement or an
   external effect;
5. use only the provider's independently evidenced addressed-send mechanism; otherwise report
   owner-assisted/unavailable honestly.

Accepted AGSK already proves Antigravity's UUID extraction and native `send_message`; Codex exposes
exact `send_message_to_thread`. The plain compact payload fits both without compatibility adaptation.
No observed gap requires changing AGSK's `.agents/rules/tfw.md`, byte-identical template, adapter
README, manifest, skill topology, migration `3.5.0`, or release history.

### E8: Minimal post-AGSK implementation denominator is twelve existing files

| # | File | Exact remaining obligation |
|---|---|---|
| 1 | `.tfw/workflows/review.md` | Ordered judgment, E1/E2 material route, E5 selection, E6 admission, E7 terminal envelope and stop. |
| 2 | `.tfw/templates/review/map.md` | Map material claims, risks, authority/safety boundaries and evidence identities before sampling. |
| 3 | `.tfw/templates/review/verify.md` | Remove ratio/escalation; record claim/risk/dependency/oracle selection, limits, evidence identity and detection power. |
| 4 | `.tfw/templates/review/judge.md` | Apply material consequence to every blocking row, retain explicit safety/human authority, and remove historical firing-rate anchors as decision inputs. |
| 5 | `.tfw/templates/REVIEW.md` | Carry classified per-item fields, aggregate verdict, Candidate-preservation and class-specific completion routes in the existing artifact. |
| 6 | `.tfw/conventions.md` | Make highest authority control sequencing only; define per-item mixed-round routes and finite assurance/record-only handling. |
| 7 | `.tfw/project_config.yaml` | Remove active `tfw.review.min_verify_ratio`. |
| 8 | `.tfw/templates/project_config.yaml` | Remove the receiver-default copy of that key. |
| 9 | `.tfw/workflows/config.md` | Retire the sync-registry row and name the old key as inert/removed migration state. |
| 10 | `.tfw/glossary.md` | Align REVIEW, Citation bar, Revision/Rung and Disposition meanings with material per-item routing. |
| 11 | `.claude/commands/tfw-review.md` | Regenerate the installed full-copy Review workflow from #1. |
| 12 | `.claude/commands/tfw-config.md` | Regenerate the installed full-copy Config workflow from #9. |

No change is justified in the Codex or Antigravity Review skills: both are thin routers that already
load the canonical Review workflow and templates. No change is justified in Antigravity's accepted
transport files. `handoff.md` already forbids redoing accepted work/unaffected evidence and moves
Candidate only on later VALUE, so the clarified REVIEW/conventions bound is sufficient without a
second Executor rule.

### E9: Release preparation is a later, separate effect—not part of the twelve-file Candidate

After independent acceptance and integration, the already-authorized `/tfw-release` route prepares
`3.5.1`. The release-owned changed paths are expected to be `.tfw/VERSION`, the version fields in the
two project-config files, `.tfw/CHANGELOG.md`, and a new `.tfw/migrations/3.5.1.md`; the release
contract also verifies the briefing template, adapter manifest and applicable adapter copies but
does not require changing unchanged files. Because the config pair is both semantic and release
metadata, the release version write is a post-review change that needs the existing bounded affected
follow-up before closure. Tag, push, publication, deployment and notification remain excluded.

### E10: External result models corroborate item detail plus one aggregate signal

[GitHub Checks](https://docs.github.com/en/rest/guides/using-the-rest-api-to-interact-with-checks)
separates a check run's aggregate conclusion from detailed annotations, each with its own location,
level and message. [SARIF 2.1.0](https://www.oasis-open.org/standard/sarif-v2-1-0/) likewise models
individual results rather than forcing every issue into one undifferentiated blob. Neither source
defines TFW authority or verdicts; they are independent existence proofs that one aggregate signal
and item-level semantics can coexist without a second acceptance verdict.

## OODA

- **Observe:** Crossed all eight Gather dimensions, inspected the active Config Sync and Executor
  return contracts, resolved the self-hosting release boundary, and consulted NIST/GitHub/OASIS
  primary sources.
- **Orient:** The unresolved work is semantic: item classification, aggregate routing, verification
  selection, check admission and terminal payload. AGSK transport and thin router skills already fit.
- **Decide:** Carry C1 as the candidate into Challenge; retain C2/C3/C4/C7/C8/C9 as explicit attacks.
  Fix the implementation denominator at twelve existing files and keep release preparation separate.
- **Act:** Challenge false approval, false return, authority/safety weakening, evidence ambiguity,
  C4+ marginal power, carrier necessity and the twelve-file boundary.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| One terminal verdict can preserve per-item subject/consequence/owner/route while highest authority controls only the next authorized act. | Attempt to break this with mixed, authority and safety cases. |
| Exact compact payload and twelve-file post-AGSK semantic denominator are identified; AGSK transport remains untouched. | Test compatibility and prove each included/excluded file boundary. |
| C4+ and new carriers add state but no demonstrated safe action. | Give both their strongest final counterexample in Challenge. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?

Stage complete: YES
→ User decision: Parent Coordinator approved Extract, the payload and twelve-file denominator, and directed Challenge to add a bounded protocol attack covering wrong `coordinator_route`, stale `REVIEW@ref`, duplicate delivery and retry after failed send without a second verdict, new effect or narrative expansion.
