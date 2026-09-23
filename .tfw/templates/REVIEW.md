# REVIEW — {ID} / Phase {X}: {Title}

> **Current filename**: `REVIEW__{ID}.md` or `REVIEW__phase-{x}__{phase_slug}.md`; a formal revision appends `__rev{N}`. Derive under `conventions.md` → `Artifact file naming`.
> **Date**: YYYY-MM-DD
> **Author**: {reviewer}
> **Verdict**: ✅ APPROVE / 🔄 REVISE / ❌ REJECT
> **RF**: [RF](path-to-RF)
> **TS**: [TS](path-to-TS)
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`
> **Producer unit**: {actual native Reviewer address}
> **Parent Coordinator**: {status.md coordinator_route}
> **Activation / dispatch source**: {owner-direct activation or immutable dispatch ref}
> **Coordination authority**: {exact status.md coordination_authority}
> **Originating proposer**: {principal and unit, or `none`}

---

## 1. Map

{Accepted result and purpose in 2–3 sentences. Name the material claim/risk selection, mandatory
safety/security and authority boundaries, accepted-result identity, evidence identities and limits.}

## 2. Verify

| # | What was checked | Result | Evidence / limit |
|---|---|---|---|
| V-selection | Claim/risk/dependency/environment/oracle selection and mandatory floors | HOLDS / FINDING / BLOCKED | `review/map.md`; `review/verify.md` selection and limits |
| V-value | Purpose, domain behavior, architecture, safety/security and human authority | HOLDS / FINDING / BLOCKED | {actual checks and finding IDs} |
| V-assurance | Evidence applicability/sufficiency and guard detection power | HOLDS / FINDING / BLOCKED | {subject tuples, guard classification and limits} |
| V-trace | Authority, accepted-result identity and authorized continuation | HOLDS / FINDING / BLOCKED | {actual trace checks and finding IDs} |
| V-accounting | Independent value-bearing replay | VERIFIED / BLOCKED / N/A / INVALID | Approval ref; full Baseline/Candidate; literal VALUE membership/actions/classes/reasons; adds/deletes/touched LOC; binary N/A; trigger; authority/timing; exact NUL-safe command |
| V-preservation | Affected baseline obligations and installed/receiver parity | HOLDS / FINDING / BLOCKED | Exact role, ordered-read, authority, research, review, accounting, knowledge and close comparisons; superseding HL amendment where applicable |

Candidate is the first tested Executor VALUE+ASSURANCE commit before traces. Excluded-only later
writes do not move it; later VALUE requires a new Candidate. Missing/mutable/mismatched/late authority
is BLOCKED; metric-only inapplicability is N/A; unresolved attribution is INVALID; DEFERRED is
non-terminal. A count, discrepancy, passing command or artifact presence is evidence only for the
claim it actually establishes.

> Raw log: `review/verify.md`. State every verification limit.

## 3. Judge — VALUE → ASSURANCE → TRACE

| Layer | Subject | Status | Evidence / finding IDs |
|---|---|---|---|
| VALUE | Purpose and approved value | ✅ / ❌ / ⚪ | {Contract Baseline + North Star clause, named harm} |
| VALUE | Domain behavior and AC | ✅ / ❌ / ⚪ | {actual behavior/oracle} |
| VALUE | Architecture and design principles | ✅ / ❌ / ⚪ | {soundness evidence} |
| VALUE | Safety/security and human acceptance authority | ✅ / ❌ / ⚪ | {mandatory boundary evidence} |
| ASSURANCE | Evidence exists, applies and sufficiently establishes material claims | ✅ / ❌ / ⚪ | {distinct existence/applicability/sufficiency reasoning} |
| ASSURANCE | Permanent guards demonstrate relevant counterfactual detection | ✅ / ❌ / ⚪ | {guard admissions; controls/diagnostics/governance labelled} |
| TRACE | Authority, accepted-result identity and reproducibility | ✅ / ❌ / ⚪ | {actual refs/accounting/citations} |
| TRACE | Authorized continuation, routes and dispositions | ✅ / ❌ / ⚪ | {owner/completion/route/Candidate effect} |

Every ❌ cites a §5 item with the complete finding contract and material consequence. Every ⚪ states
why the subject cannot apply. Non-material TRACE stays visible without becoming product failure.

## 4. Verdict

**{✅ APPROVE / 🔄 REVISE / ❌ REJECT}**

{One aggregate rationale citing §§2–3 and §5 item IDs. APPROVE requires no open material item that
changes acceptance or the next authorized act. REVISE requires a complete material correctable item.
REJECT is reserved for `not fit for purpose` or a contract defect routed to the owner.}

### If REVISE — proposals to Coordinator

1. {F# and proposal} — **basis:** {affected approved TS criterion or frozen HL claim}; **harm and material consequence:** {specific}; **owner/completion/route/Candidate effect:** {specific}

### If REJECT — fundamental issues

1. {F#; purpose or contract defect; exact owner route}

## 5. Findings, Completion Routes, and Observations

A finding—not an artifact or whole round—is the unit of classification and completion. Record each
item once. A breached criterion, discrepancy, citation or process record alone cannot change the
verdict. `pending — coordinator` awaits one ruling. Terminal dispositions are `paid — {existing
carrier/phase}`, `promoted — {existing task}`, or `not material — {named absence of acceptance or
action consequence}`. A generic backlog is invalid.

| ID | Class | Subject / affected claim or authority | Observed fact + oracle | Concrete harm and material consequence | Owner + observable completion | Route / rung | Candidate effect | Disposition |
|---|---|---|---|---|---|---|---|---|
| F1 | VALUE / ASSURANCE / TRACE | {subject and claim} | {fact + oracle} | {harm + consequence or named absence} | {owner + condition} | {exact route} | unchanged / moves | {pending / terminal disposition} |

If empty: `No findings or observations.`

VALUE/contract defects use product/specification rungs. ASSURANCE-only gaps preserve an independently
established Candidate and target the missing proof or guard. Material authority/identity TRACE routes
to its exact ruler. Non-material TRACE receives a visible observation or finite current-carrier repair
and never restarts unchanged product execution. Highest authority sequences only the next act; it does
not reclassify lower items or move unchanged VALUE.

## 6. Traces Updated and Terminal Signal

Reviewer records the durable verdict and authorized state/event first. Under `tfw-gates-only`, it
then preflights exact `coordinator_route` and immutable REVIEW ref and sends exactly one logical
envelope with no findings prose:

`REVIEW · <reviewer-unit> · <task-or-phase> · <verdict> · <review-artifact@ref>`

The exact tuple is the logical identity. Duplicate receipt creates no second verdict, ruling or
lifecycle act. Only a provider-confirmed non-applied failure may use one provider-specific bounded
identical retry; ambiguous delivery is neither claimed nor blindly retried. Never route the signal to
owner, Executor, peer or GATEWAY under `tfw-gates-only`.

- [ ] durable REVIEW and applicability limits recorded at immutable ref
- [ ] authorized lifecycle/status and journal effect recorded
- [ ] exact Coordinator route and immutable REVIEW ref preflighted
- [ ] one compact logical envelope sent to `coordinator_route`
- [ ] every §5 item retains class, completion route, disposition and Candidate effect

Coordinator appends separately attributed closing facts here under `conventions.md` → `Closing and
record recovery`; markers alone never establish DONE:

- [ ] Coordinator §5 rulings complete; no pending owed item
- [ ] tfw-docs: {Applied / N/A — actual effect or reason}
- [ ] tfw-knowledge: {Applied / N/A / Deferred — actual effect or reason}
- [ ] one truthful task changelog entry preserved; no release inferred
- [ ] task-owned sessions, worktrees/branches, helpers, containers/processes and temporary files each removed, specifically retained, or pending with actor/action
- [ ] final accepted output identity and affected independent judgment recorded
- [ ] selected landing/final effects complete and status/event validated before terminal write

Reuse applicable evidence for unchanged claims. Affected material changes receive a bounded
independent follow-up; a real cited defect uses ordinary REVISE. Record-only recovery identifies the
erroneous carrier/event, preserves acceptance, repairs only the current carrier, validates and stops.

## 7. Fact Candidates

| # | Category | Human-sourced candidate | Source | Confidence |
|---|---|---|---|---|
| 1 | {category} | {fact} | {conversation reference} | High / Medium / Low |

If empty: `No fact candidates.`

### Material handover at this return

Apply `conventions.md` → `Knowledge handover`. Record producer/unit, source/epoch, inspected scope,
material or justified-none, uncertainty, continuation, and unresolved owner/decision. Do not replace
the original source.

---

*REVIEW — {ID} / Phase {X}: {Title} | YYYY-MM-DD*
