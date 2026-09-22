# Judge — "Is the accepted result fit and sufficiently established?"
> **Mindset:** Judge. Apply the evidence from Verify in `VALUE → ASSURANCE → TRACE` order.
> **Test:** "Would I defend this acceptance decision for the named purpose, harm and authority?"
> Verify findings: [verify.md](verify.md)

## Status and Materiality

**Status vocabulary:** `✅` holds · `❌` finding · `⚪ N/A` does not apply with a stated reason.
Every `❌` cites a Verify finding with the complete item contract. A row, criterion, discrepancy,
citation, count or process record never changes the verdict by itself. Blocking requires an affected
accepted claim or authority, concrete harm and material consequence. Safety/security, human
acceptance authority and accepted-result identity are non-waivable subjects.

## 1. VALUE

| Subject | Status | Evidence / finding IDs |
|---|---|---|
| Purpose and approved value | ✅ / ❌ / ⚪ | {Purpose Check below} |
| Domain behavior and acceptance criteria | ✅ / ❌ / ⚪ | {actual behavior and oracle} |
| Architecture and HL principles | ✅ / ❌ / ⚪ | {soundness evidence} |
| Safety and security | ✅ / ❌ / ⚪ | {intended/unintended behavior and harm} |
| Human acceptance authority and reserved effects | ✅ / ❌ / ⚪ | {actual ruler and boundary} |

### Purpose Check

Use the **master HL at its Contract Baseline** plus the **Project North Star**, never TS or a Phase HL.
In one field quote the clause served and name the concrete harm at stake. A resolving but irrelevant
citation fails. Green tests or TS inclusion are not sufficient.

Test three conditions:

1. **Excess and adjacency** — does the result deliver something the cited clause does not ask for or excludes?
2. **Deferral confession** — does the result ship work that its own contract assigns elsewhere?
3. **Materiality** — would the issue materially harm the approved value? Wording alone is not harm.

| Outcome | Status | Required finding and route |
|---|---|---|
| Aligned | ✅ | quoted clause + named harm protected |
| Purpose failure | ❌ | `not fit for purpose`; full item contract; owner route |
| Reference set necessarily inconsistent | ❌ | `contract defect`; quote both clauses; owner route |

Surface tension is not inconsistency. Read each clause completely. A coherent but wrong result is a
purpose failure, not a contract defect.

## 2. ASSURANCE

| Subject | Status | Evidence / finding IDs |
|---|---|---|
| Evidence exists | ✅ / ❌ / ⚪ | {RF/EV refs} |
| Evidence applies to accepted subject, Candidate/revision, environment, oracle/authority and dependencies | ✅ / ❌ / ⚪ | {subject tuples} |
| Evidence is sufficient for each material claim and risk | ✅ / ❌ / ⚪ | {selection and limits} |
| Permanent guards demonstrate relevant counterfactual detection | ✅ / ❌ / ⚪ | {guard admission; distinguish controls/diagnostics/governance} |

Evidence existence and sufficiency are different judgments. A material ASSURANCE gap changes the
verdict only when it leaves a material VALUE, safety, authority or accepted-result claim unestablished.
If independent applicable proof already establishes the same claim, preserve the Candidate and treat
the false/redundant record by its TRACE consequence.

## 3. TRACE

| Subject | Status | Evidence / finding IDs |
|---|---|---|
| Governing authority and independent role lineage | ✅ / ❌ / ⚪ | {status/journal/dispatch} |
| Accepted-result identity and immutable accounting | ✅ / ❌ / ⚪ | {Baseline/Candidate and exact replay} |
| Reproducibility and citation integrity needed for material claims | ✅ / ❌ / ⚪ | {actual refs and methods} |
| Authorized continuation, item completion routes and dispositions | ✅ / ❌ / ⚪ | {route, owner, completion, Candidate effect} |
| Record-only observations | ✅ / ❌ / ⚪ | {finite repair or observation; no product restart} |

TRACE blocks only when it materially changes authority, accepted-result identity, safety provenance,
material proof or an authorized next action. Non-material wording, count, label and citation defects
remain visible but receive observation or finite current-carrier repair with Candidate unchanged.

## 4. Finding Rulings

Copy every real Verify finding once. Preserve its class and route before deriving the verdict.

| ID | Class | Subject / affected claim or authority | Fact + oracle | Harm and material consequence | Owner / completion | Route / rung | Candidate effect | Disposition |
|---|---|---|---|---|---|---|---|---|
| F1 | VALUE / ASSURANCE / TRACE | {subject and claim} | {fact + oracle} | {harm + consequence or named absence} | {owner + observable condition} | {route} | unchanged / moves | pending / paid / promoted / not material |

The highest required authority sequences only the next authorized act. It never reclassifies lower
items, moves unchanged VALUE or forces every item through the highest rung. One mixed REVIEW retains
one aggregate verdict.

## 5. Aggregate Verdict

- **APPROVE** — no open material item changes acceptance or the next authorized act. Visible
  non-material TRACE and finite record-only correction retain their own dispositions.
- **REVISE** — one or more material correctable items have a cited claim/authority, harm, consequence,
  completion condition, owner, route and Candidate effect.
- **REJECT** — `not fit for purpose` or a contract defect requires the owner route.

**Verdict:** {✅ APPROVE / 🔄 REVISE / ❌ REJECT}

**Reason:** {cite item IDs and ordered VALUE/ASSURANCE/TRACE evidence}

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | Accepted claim | Contradiction / effect |
|---|---|---|---|

If none: `No applicable contradictions.`

## Checkpoint

**Self-check:**
- [ ] Judged VALUE, then ASSURANCE, then TRACE, including every mandatory floor?
- [ ] Supported every status with Verify evidence and every N/A with a reason?
- [ ] Answered Purpose against Contract Baseline + North Star with a relevant clause and concrete harm?
- [ ] Kept evidence existence, applicability and sufficiency distinct?
- [ ] Gave every verdict-relevant item the complete finding contract, class, route and Candidate effect?
- [ ] Let highest authority sequence the next act without reclassifying mixed items?
- [ ] Derived exactly one verdict without using checklist, discrepancy, file, test or artifact volume as a quality objective?

Stage complete: YES / NO
