# Verify — "Do the material claims hold?"
> **Mindset:** Auditor. RF is a declaration, not a fact. Open files, run necessary checks, compare
> accepted claims with reality, and state the limits.
> **Test:** "Would the evidence establish this claim for this subject, revision and environment without RF?"
> Map: [map.md](map.md)

## Selection Argument

| Claim IDs | Risk / criticality | Affected behavior / dependencies | Environment | Oracle / authority | Evidence gap / limit | Selected verification and why |
|---|---|---|---|---|---|---|
| {C1…} | {risk} | {scope} | {environment} | {oracle} | {gap or none} | {check / applicable evidence} |

Safety/security, human acceptance authority and accepted-result identity are mandatory floors.
Expand verification when an observed fact changes a mapped claim, dependency, risk or evidence gap;
the existence or count of discrepancies never selects depth by itself.

## Verification Log

### {V1: claim IDs and subject}
- **Accepted claim / authority:** {what must hold}
- **Subject tuple:** {accepted subject, revision/Candidate, environment, oracle/authority, dependency state}
- **Action or evidence:** {what was inspected or run}
- **Observed:** {actual result}
- **Limit:** {none or explicit unresolved limit}
- **Result:** HOLDS / FINDING / BLOCKED

## Commands Executed

| # | Command | Claim IDs | Result |
|---|---|---|---|
| 1 | {build/test/lint/inspection command} | {C1…} | {exit and concise observed result} |

Run TS-required checks and checks needed by the selection argument. When reusing evidence, explain
why its subject tuple and assumptions still apply. If a required check cannot run, name the exact
unresolved material claim and missing environment; this is not PASS.

## Claim and Source Checks

1. Spot-check key claims or sources by material reliance, not convenience.
2. Confirm every citation resolves to a real, relevant artifact.
3. Verify data claims against a primary source where reachable.

| # | Claim / citation | Where | Primary artifact / source | Holds? |
|---|---|---|---|---|
| C1 | {claim} | {file + section} | {source or unresolved} | ✅ / ❌ / ⚠️ |

If the deliverable has no claims, citations or data, state what it does contain and why this is N/A.

## Guard and Check Admission

| # | Kind | Protected behavior / invariant | Failure consequence | Counterfactual detection | Admission |
|---|---|---|---|---|---|
| G1 | permanent guard / positive control / temporary diagnostic / governance assertion | {subject} | {harm or actual limited use} | {historical red, relevant mutant/fault/fixture, or N/A with reason} | admitted / labelled control / temporary / governance only / rejected |

A permanent guard requires the first four fields and relevant demonstrated detection. Historical
red-before-green is strong, not universal. A relevant mutant, fault, fixture or equivalent negative
control may establish existing behavior. Positive controls, diagnostics, counts, commit/artifact
existence and scope arithmetic keep their actual labels and are never product-quality guards by volume.

## Candidate Findings

A breached criterion, discrepancy, citation or process record becomes verdict-relevant only after
the full item contract establishes a material accepted claim or authority consequence.

| ID | Class | Subject | Affected claim / authority | Observed fact + oracle | Concrete harm | Material consequence or named absence | Owner | Observable completion | Route / rung | Candidate effect | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F1 | VALUE / ASSURANCE / TRACE | {subject} | {claim} | {fact + oracle} | {harm} | {material consequence / none} | {owner} | {condition} | {route} | unchanged / moves | open / complete / observation |

If empty: `No findings.` Non-material TRACE remains visible as an observation or finite
current-carrier repair; it cannot restart product execution.

## Evidence Verification

Evidence applies to `{accepted subject, revision/Candidate, relevant environment, oracle/authority,
dependency state}`. Changed dependencies or insufficient proof require an affected check; an enclosing
SHA or unrelated record change does not invalidate adequate evidence.

| # | RF evidence ref | Subject tuple | Artifact exists? | Establishes the claim? | Limit |
|---|---|---|---|---|---|
| E1 | {evidence/file or inline ref} | {tuple} | ✅ / ❌ | ✅ / ❌ / ⚠️ | {none or limit} |

If RF §5 has no evidence items: state `N/A — no evidence artifacts to verify` and why that can satisfy
the mapped claims.

## Knowledge Citations Verified

Scan PV priorities 0–4 in full and 5–7 by relevance. Verify every HL §7.2 and ONB §7 citation for
resolution, item existence, semantic match, currentness and relevance. Check priority 0 purpose and
priority 1 methodology separately even when one file contains both.

| # | Artifact | Priority + exact citation | Resolves? | Item exists? | Meaning matches? | Relevant? |
|---|---|---|---|---|---|---|
| 1 | HL §7.2 #{N} | {priority and item} | ✅ / ❌ | ✅ / ❌ | ✅ / ❌ — {comparison} | ✅ / ❌ — {application} |

If HL §7.2 says no applicable items: `N/A — no citations to verify.`

## Accounting Replay

| Approval / authority | Baseline | Candidate | Literal VALUE membership / actions / classes / reasons | Adds | Deletes | Touched LOC | Binary | Trigger disposition | Exact NUL-safe command | Verdict |
|---|---|---|---|---:|---:|---:|---|---|---|---|
| {ref and timing} | {full SHA} | {full SHA} | {exact result} | {N} | {N} | {N} | N/A / details | {result} | {command} | VERIFIED / BLOCKED / N/A / INVALID |

Candidate is the first tested implementation commit before EV/RF/state. Later VALUE moves it; later
TRACE, ASSURANCE or non-value DERIVED does not. Missing/mutable/mismatched/late authority is BLOCKED;
metric-only inapplicability is N/A; unresolved attribution is INVALID; DEFERRED is non-terminal.

## Selected Knowledge Evidence

Inspect contributing-role returns, material sources and completed dispositions against dispatch
lineage. Record source/epoch, producer/unit, scope, authority and applicability. Presence, newer time,
clean merge or an Applied marker is not independent acceptance.

## Checkpoint

**Self-check:**
- [ ] Replayed the Map selection and verified all mandatory safety/security, authority and identity floors?
- [ ] Established evidence applicability and ran every TS-required or dependency-affected check?
- [ ] Recorded explicit limits instead of substituting file, discrepancy, test, commit or artifact counts?
- [ ] Classified guards and controls by protected behavior, consequence and counterfactual detection?
- [ ] Recorded every candidate finding with the complete item contract and material consequence test?
- [ ] Verified RF AC claims, evidence references, citations and immutable accounting against actual artifacts?

Stage complete: YES / NO
