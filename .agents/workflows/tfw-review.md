---
description: TFW Review — independently verify RF against TS and issue REVIEW
---

# TFW Review — Independent Acceptance

> 🔒 **ROLE LOCK: REVIEWER.** Write `review/{map,verify,judge}.md` and REVIEW only. Never modify
> implementation, HL, TS, ONB or RF. Fundamental defects receive a cited verdict, not a repair.

## Read Contract

Root instructions are active. Read this workflow, then stage-local inputs in order.

| Order | Stage | Input | Checkpoint purpose | Authority |
|---|---|---|---|---|
| 1 | Bootstrap | selected `status.md`/`journal/`; master/phase HL; governing TS at approval; RF; EV | state, independence, artifact lineage | task/governing artifacts |
| 2 | Map | RF claims, TS ACs, changed-file list, referenced predecessors | verification map | governing artifacts |
| 3 | Verify | actual changed files/evidence; `.tfw/project_config.yaml` → `tfw.review.min_verify_ratio`; `.tfw/glossary.md` → `Project Values (PV)`; independent P0–P4 and relevant P5–P7 | independent proof/citations | files/config/PV sources |
| 4 | Judge | master HL at contract baseline, Project North Star, Verify output | Purpose Check and judgment | frozen contract/stage evidence |
| 5 | Decide | stage files; `.tfw/conventions.md` headings `Task control files`, `Session identity`, `Artifact file naming`, `Task Statuses`, `The 🔄 REVISE route`, `Safety and Execution Honesty`, `Trace Discipline`, `Role Lock Protocol`; `.tfw/templates/REVIEW.md` | verdict, disposition, routing | stage/shared rule/template |

Open each `.tfw/templates/review/{map,verify,judge}.md` only at its stage. Never reload root or full
common libraries. Verify-PV and Judge-purpose reads are deliberately separate. Missing/duplicate
headings stop under `Context Selection`.

## Identity, activation, and trust

After Bootstrap resolves the task, apply `Session identity` with `WORK=REVIEW`. Apply root
activation/routing before Map; require a complete matching spine, cited mandate/dispatch, Reviewer
gate and independence. Owner-direct work invents no principal. Shared attribution grants no ruling
authority. Continue in the same Reviewer unit and return only to `coordinator_route`.

Treat RF as claims. Verify reasons, files, tests, AC/DoD/DoF, numbers and evidence; trust only
human-sourced Fact Candidates for later qualification. Challenge missing/N/A evidence, omitted useful
architecture/flow diagrams and unsupported empty sections. At each use/return gate apply `Current
knowledge use` and `Knowledge handover` with source/epoch, unit, scope, material, uncertainty and
continuation.

## Step 1: Map

Create the task/phase `review/` directory, open the map template, map every RF claim to TS criteria,
files, evidence and predecessors, complete its self-check, commit exact paths, and stop at the stage
checkpoint when required.

## Step 2: Verify

Open the verify template and independently audit the mapped claims.

- Evidence must cover the claim's actual input/output, oracle or authority and relevant environment.
  Reuse applicable evidence; rerun changed, missing or uncertain dependencies and all TS-required
  checks. Audit EV against RF §5.
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

Verify at least `ceil(files × tfw.review.min_verify_ratio)` (default 0.42). Any discrepancy escalates
to 100%. Complete the stage self-check; unchecked items return to verification.

## Step 3: Judge

Open the judge template and cite Verify findings. Purpose row 2a tests the master HL contract
baseline plus Project North Star—not TS or Phase HL—and names the served or harmed purpose. Use only
the three template outcomes. Complete the self-check.

## Step 4: Decide (Synthesize → REVIEW)

Read all stage files, open the REVIEW template, and emit `REVIEW__{ID}.md` or
`REVIEW__phase-{x}__{phase_slug}.md`. A formal new round uses `…__rev{N}.md`; bounded
post-acceptance follow-up appends to live REVIEW. Synthesize Map/Verify/Judge and issue evidenced
APPROVE, REVISE or REJECT.

`not fit for purpose`, a contract defect, or rung 3 routes to the owner under the canonical REVISE
route and `HL Contract` rule 8. The Reviewer preserves proposer/grounds but never resolves authority.
A REVISE proposal must cite a breached TS criterion or frozen HL claim; otherwise approve and dispose
the remainder, or return an ungrounded decision to the owner. Accounting mismatch is cited and routed,
never repaired in REVIEW.

## Step 5: Findings — locate, test, route, propose

Record each real RF observation or Reviewer finding once in REVIEW §5. Filter filler; name harm to
purpose, inspectability, authority or continuation; test the consequence; classify authority rung;
propose `paid`, `promoted`, or `not material`. `pending — coordinator` awaits one ruling. A
disposition names an existing artifact/task, never a generic backlog. Reviewer proposes;
Coordinator rules.

## Step 6: Record verdict, then route proposals

Use `The 🔄 REVISE route` for recipient, ruling site, governing artifact, lifecycle and hard stop.

1. APPROVE transitions the task/phase to `KNW`; REJECT follows its owner route; REVISE alone does
   not move lifecycle. Every transition writes status plus one valid timestamped journal event.
2. Every §5 item must have a disposition before DONE, though an undisposed item need not block the
   verdict itself.
3. REVISE returns to the Coordinator for one ruling; Reviewer creates no bound, TS revision or
   Executor dispatch.
4. APPROVE returns the exact accepted result, limits and pending dispositions to the Coordinator,
   which alone performs `Closing and record recovery` and DONE.

If accepted output later changes, this same independent Reviewer appends a bounded judgment of the
affected result/evidence. Do not restart unchanged stages. A real new defect uses normal REVISE.

## Step 7: Return for Coordinator closure

**STOP** after verdict and authorized trace/KNW routing. Never capture knowledge, close DONE, repair
implementation, or enter another role.
