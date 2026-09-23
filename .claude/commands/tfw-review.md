---
description: TFW Review — independently verify RF against TS and issue REVIEW
---

# TFW Review — Independent Value Assurance

> 🔒 **ROLE LOCK: REVIEWER.** Write `review/{map,verify,judge}.md` and REVIEW only. Never modify
> implementation, HL, TS, ONB or RF. Fundamental defects receive a cited verdict, not a repair.

## Read Contract

Root instructions are active. Read this workflow, then stage-local inputs in order.

| Order | Stage | Input | Checkpoint purpose | Authority |
|---|---|---|---|---|
| 1 | Bootstrap | selected `status.md`/`journal/`; master/phase HL; governing TS at approval; RF; EV | state, independence, artifact lineage | task/governing artifacts |
| 2 | Map | RF claims, TS ACs, changed-file list, referenced predecessors | material claims, risks, boundaries and evidence identities | governing artifacts |
| 3 | Verify | actual changed files/evidence; `.tfw/glossary.md` → `Project Values (PV)`; independent P0–P4 and relevant P5–P7 | claim-selected proof and citations | files/PV sources |
| 4 | Judge | master HL at contract baseline, Project North Star, Verify output | ordered value-assurance judgment | frozen contract/stage evidence |
| 5 | Decide | stage files; `.tfw/conventions.md` headings `Task control files`, `Session identity`, `Artifact file naming`, `Task Statuses`, `The 🔄 REVISE route`, `Safety and Execution Honesty`, `Trace Discipline`, `Role Lock Protocol`; `.tfw/templates/REVIEW.md` | verdict, item routes, terminal signal | stage/shared rule/template |

Open each `.tfw/templates/review/{map,verify,judge}.md` only at its stage. Never reload root or full
common libraries. Verify-PV and Judge-purpose reads are deliberately separate. Missing/duplicate
headings stop under `Context Selection`.

## Identity, activation, and trust

After Bootstrap resolves the task, apply `Session identity` with `WORK=REVIEW`. Apply root
activation/routing before Map; require a complete matching spine, cited mandate/dispatch, Reviewer
gate and independence. Owner-direct work invents no principal. Shared attribution grants no ruling
authority. Continue in the same Reviewer unit and return only to `coordinator_route`.
Read effective `reporting` and `selection_ref`; a complete old five-field carrier means verified
baseline/native gates, while partial new fields refuse. Manual role creation leaves native returns
intact. Only an actual owner-transfer choice changes transport. A non-revoking selection retains
this independent Reviewer and prior valid activation. In a selected shared checkout, review only
the fixed reachable Candidate while Executor mutation is stopped.

Treat RF as claims. Verify reasons, files, tests, AC/DoD/DoF, numbers and evidence; trust only
human-sourced Fact Candidates for later qualification. Challenge missing/N/A evidence and unsupported
empty sections. At each gate apply `Current knowledge use` and `Knowledge handover`.

## Finding contract and judgment order

Judge the accepted result in this order:

1. **VALUE** — purpose, domain behavior, architecture, safety/security and human acceptance authority.
2. **ASSURANCE** — whether applicable evidence establishes each material claim for the accepted subject.
3. **TRACE** — authority, accepted-result identity, reproducibility and authorized continuation.

A finding—not an artifact, discrepancy or whole round—is the unit of classification and completion.
Every item that can block or return work records: subject/class; affected accepted claim or authority;
observed fact and oracle; concrete harm; material consequence; owner; observable completion condition;
route/rung; and Candidate effect. A breached criterion, citation, count or process record alone cannot
change the verdict. Safety/security, human authority and accepted-result identity are mandatory floors.

Classify and route items before one aggregate verdict. Highest authority orders only the next act;
it never reclassifies lower items, drags unchanged VALUE upward or moves a Candidate without a VALUE
change. Non-material TRACE is observed or repaired in its current carrier without product restart.

## Step 1 — Map

Create task/phase `review/`, open the Map template, and map accepted claims and boundaries to risk,
dependencies/behavior, environment, oracle/authority and evidence identity. Map RF claims to TS
criteria, complete the self-check, commit exact paths, and stop when required.

## Step 2 — Verify

Open the Verify template and independently audit the mapped claims.

- Select checks from material claim, risk/criticality, affected behavior/dependencies, relevant
  environment, oracle/authority, evidence gap and unresolved limit. Verify every mandatory
  safety/security, authority and accepted-result-identity boundary regardless of sampling.
- Evidence applies only to its `{accepted subject, revision/Candidate, relevant environment,
  oracle/authority, dependency state}`. Reuse adequate evidence; rerun changed, missing or uncertain
  dependencies and every TS-required check. Audit EV against RF §5.
- Admit a permanent guard only when it names protected behavior/invariant, failure consequence and
  demonstrated relevant counterfactual detection. Historical red-before-green is strong but not
  universal; a relevant mutant, fault, fixture or equivalent negative control can establish existing
  behavior. Label positive controls, temporary diagnostics, counts and governance assertions by their
  actual use; their presence or volume is not product assurance.
- Enforce `Exact-path staging`: inspect full status/cached names; require explicit full pathspecs and
  `git commit --only`. Broad staging or inseparable foreign hunks fail. For crossings, verify producer
  task/phase, role, history, Candidate reachability and deferred cleanup.
- For accounting, resolve the approved TS and rerun its exact NUL-safe method with the RF's full
  Baseline/Candidate and literal VALUE selector. Verify logical membership/renames, numeric additions,
  deletions and touched LOC, binary N/A, phase attribution, protected boundaries and timing. Candidate
  is the first tested implementation commit before EV/RF/state; later VALUE moves it, later TRACE,
  ASSURANCE or non-value DERIVED does not.
- Recheck trigger disposition and prospective authority against the immutable owner-approved
  denominator. Never invent a selector, ratchet a plan or supply late authority. Missing/mutable/late
  facts are BLOCKED; unresolved attribution is INVALID; DEFERRED cannot close a required decision.
- Scan PV priorities 0–4 fully and 5–7 by relevance. For every HL §7.2/ONB §7 citation verify link,
  existence, semantic match, currentness and relevance, including distinct priority-0 purpose and
  priority-1 methodology clauses.

Record the selection argument, checks, finding candidates and explicit limits. A discrepancy expands
verification only when its affected claim, dependency, risk or evidence gap justifies that expansion.
Complete the stage self-check; unchecked material claims return to verification.

## Step 3 — Judge

Open the Judge template. Apply the ordered `VALUE → ASSURANCE → TRACE` judgment and cite Verify
evidence for every subject. Purpose tests the master HL contract baseline plus Project North Star—not
TS or Phase HL—and names the served or harmed purpose. Classify every finding with the full item
contract before deriving one aggregate verdict. Complete the self-check.

## Step 4 — Decide (Synthesize → REVIEW)

Read all stage files, open the REVIEW template, and emit `REVIEW__{ID}.md` or
`REVIEW__phase-{x}__{phase_slug}.md`. A formal new round uses `…__rev{N}.md`; bounded
post-acceptance follow-up appends to live REVIEW.

Use one terminal verdict:

- **APPROVE** when no open material VALUE, ASSURANCE or TRACE item changes acceptance or the next
  authorized act; visible observations and finite record-only correction remain item dispositions.
- **REVISE** for a material correctable item; every proposal cites its accepted claim/authority,
  concrete harm, material consequence, completion condition, owner, route and Candidate effect.
- **REJECT** for `not fit for purpose` or a contract defect; route to the exact ruler.

The Reviewer never repairs, rules authority or supplies a missing bound. One REVIEW may dispose
mixed items without a second verdict.

## Step 5 — Complete and route each item

Record each item once in REVIEW §5. VALUE uses product/specification rungs; ASSURANCE-only gaps
preserve an established Candidate and target missing proof; material authority/identity TRACE uses
its exact ruler; non-material TRACE stays in its current carrier. A disposition names an existing
artifact/task, never a generic backlog.

## Step 6 — Record verdict, then signal

Use `The 🔄 REVISE route` for recipient, ruling site, governing artifact, lifecycle and hard stop.

1. APPROVE transitions the task/phase to `KNW`; REJECT follows its owner route; REVISE alone does not
   move lifecycle. Every transition writes status plus one valid timestamped journal event.
2. Every §5 item retains its class, completion route and Candidate effect. Pending material or owed
   record work keeps close open; it does not automatically change the product verdict.
3. REVISE returns to the Coordinator for one ruling; Reviewer creates no bound or dispatch.
4. After durable REVIEW and the authorized status/journal effect exist, preflight the exact
   `coordinator_route` and immutable REVIEW ref, then send exactly one logical envelope:
   `REVIEW · <reviewer-unit> · <task-or-phase> · <verdict> · <review-artifact@ref>`.
5. The envelope contains no findings prose and never routes to owner, Executor, peer or GATEWAY under
   `tfw-gates-only`. Its exact tuple is its logical identity; duplicate receipt creates no second
   verdict, ruling or lifecycle act. Retry identical bytes only when the provider confirms
   non-application and its own mechanism permits one bounded retry. Ambiguous delivery is not claimed
   or blindly retried.
   Under explicit owner-transfer, present the same exact durable verdict/ref through the selected
   manual route; do not claim an inter-agent send.

Transport evidence stays provider-specific: accepted AGSK establishes Antigravity UUID extraction
and native `send_message`; Codex exposes exact `send_message_to_thread`. The payload fits both without
transport changes, but neither evidence nor analogy grants another provider automatic or exactly-once
behavior. Otherwise report owner-assisted/unavailable.

If accepted output later changes, this same independent Reviewer appends a bounded judgment of the
affected result/evidence. Do not restart unchanged stages. A real new defect uses normal REVISE.

## Step 7 — Stop

**STOP** after durable verdict, trace effect and compact signal. Never
capture knowledge, close DONE, repair implementation, or enter another role.
