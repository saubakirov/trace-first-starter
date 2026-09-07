# PROPOSAL — TFW_20260907-133942_PTTC: Proportionate Testing and Task Closure

> **Date**: 2026-09-07
> **Abbreviation**: PTTC
> **Registration approval**: owner saubakirov, 2026-09-07, direct reply “pttc принимается” to the proposed full title and abbreviation; approval registers the proposal, not its candidate architecture.

> **Author**: robert (Main Coordinator; source unit `01a07050-9d35-7080-a5f6-afd14334e68d`)
> **Owner**: saubakirov
> **Status**: TODO — future proposal only; no HL freeze, TS, research run, implementation, extra agent, automation, or release gate is authorized.
> **Entry point**: `/tfw-plan`
> **Origin**: the owner's direct request during the CRATM Phase E late-assurance correction.
> **Scheduling**: independent follow-up; do not make CRATM wait for this redesign.

## 1. Purpose and value

Make this repository's verification and task-closure process proportionate to the actual risk.
A small legitimate documentation change must not force hours of repeated orchestration and broad
test runs. Preserve meaningful defect detection, independent review, honest completion, and durable
evidence while reducing unnecessary elapsed time, agent tokens, and owner attention.

The owner reports that the latest apparently one-character CRATM repair cost several hours and
thousands of tokens and was still running when this proposal was requested. That is stakeholder
evidence of an unacceptable experience, not a measured billing total. Tests cannot be cost-free:
the required outcome is justified, measured cost, not an impossible zero-cost promise.

## 2. Bounded retrospective: what is known

This is an interim retrospective, not a claim that CRATM E has finished. The evidence snapshot is
formal review tip `784ace52034a782ccf6930b033f106c1bf245082`. The same independent Reviewer has
returned APPROVE for the bounded repair; final knowledge reconciliation, closure, release, and saved
landing are not yet established. Append their actual outcome when available without inventing it now.

| Observation | Evidence and consequence |
|---|---|
| Legitimate document evolution failed a current-text guard | At K2 `7b4d4190c06a6ca02d55e23f90ed24214df8d2b5`, the CRATM artifact row changed from `B–D` to `B–E`. `test_phase_e_knowledge_keeps_exact_rtbo_and_final_cratm_decisions` still required exactly one `B–D` row and found zero. Earlier D82/D83 preservation checks passed. This failure did not establish missing or false knowledge. |
| An isolated text test unconditionally builds the documentation site | `docs/scripts/test_integration.py` has a module-scoped `autouse=True` `build_site` fixture invoking MkDocs. The affected test reads Git objects and Markdown, not generated HTML. Selecting one test still invokes this fixture; each new pytest process can build again. Exact setup/body timing has not yet been separately measured. |
| The correction became materially larger than a suffix change | Main's accepted repair bound required coherent pre/post states, historical pins, and negative cases. Candidate `a7b9fd8b6a319d56850b9048e321f1242b288631` changes one test function by 67 additions and 12 deletions. This was a coordination decision, not an unavoidable consequence of Python or pytest. |
| Repeated verification amplified iteration cost | The late-round transcript records a failing baseline, a failing mutant, an initial green full suite invalidated by a later one-line correction, then single, targeted, and full reruns. Broad reruns were required by the accepted order, rather than chosen from an explicit risk/dependency model. |
| Closure changed an already-reviewed surface | Formal review preceded docs/knowledge effects. Shared review Step 7 permits DONE once docs/knowledge markers and debt dispositions are complete, without an explicit affected-output check after those effects. CRATM had its own additional postconditions, but DONE was recorded before they succeeded. Distinguish the shared rule gap from our failure to follow the task's stronger order. |
| Recovery introduced further administrative errors | Premature DONE events were retained and corrected under the owner's authorization. A phase-local correction then carried an escaping ref; a later dispatch carried an invented full commit SHA. Both were preserved and corrected before the final review dispatch. These are coordination failures, not product defects; inspect why repair bookkeeping created fresh opportunities for failure. |

An additional closure defect was observed while registering this proposal: commit
`f6309596eb496cfaea54e739347623f2c80669f5` set the CRATM root and E phase to DONE but omitted
the mandatory `outcome` field in both status files. The release preflight caught this before release
writes; Main approved a two-status, append-only TRACE correction without another implementation or
review round. Its application is not assumed here. This is evidence for a cheap, complete pre-write
status check, not an argument for deleting validation or running the whole product suite again.

### Recorded late-round test cost

Source: `phase-e/evidence/phase-e-completion-tests.txt`, RETURN ROUND 2 at the snapshot above.

| Recorded run | Seconds |
|---|---:|
| Before-edit single failure | 272.62 |
| First after-edit single failure | 163.22 |
| Full suite before final one-line correction; historical evidence only | 628.42 |
| Final-byte single test | 126.28 |
| Final-byte Phase E selection | 143.58 |
| Final-byte full suite | 628.61 |
| Sum of these six distinct recorded runs | 1962.73 |

The sum is **32 minutes 42.73 seconds of recorded run durations**, not end-to-end elapsed time,
CPU time, or the total incident cost. It excludes other diagnostic runs, independent review,
separately invoked strict builds, tool latency, reasoning, messages, and earlier E rounds.
Do not add fixture time again: it is already inside the corresponding pytest duration.
The final Executor full suite reports 529 passed and 1 skipped. Formal revision 3 independently
reports 529 passed and 1 skipped on the exact package-applied Candidate and an APPROVE verdict;
its additional run cost is not included in this six-run subtotal. No exact token or monetary ledger
has been established.

## 3. Questions the future task must answer

1. Which tests protect shipped behavior, authority, data preservation, parsing, adapter parity,
   rendering, and migration, and which merely freeze incidental task history or prose?
2. Which checks truly need a full-site build, real Git history, or the whole corpus? Which can use
   a small fixture without making the fixture a second, self-confirming specification?
3. What change invalidates which prior evidence: product bytes, test logic, fixture/environment,
   docs/knowledge output, release output, or only unrelated lifecycle metadata?
4. What independent work must a Reviewer perform, and when is a second full run justified instead
   of focused reproduction and inspection of provenance?
5. How can docs/knowledge, final verification, DONE, release, and landing form a finite sequence?
   What changes require another formal review, and what can be checked without manufacturing a
   fresh selected knowledge section and repeating the entire closure cycle?
6. How should an erroneous terminal record be corrected honestly and proportionately without
   silent historical rewriting or unnecessary owner involvement in routine technical repair?
7. Which remedies belong only to this repository, and which closure rules are shipped to TFW
   users? Preserve project-owned build commands and tool-independent ordinary Full usage.

## 4. Candidate direction — Main Coordinator's proposal, not approved architecture

| Candidate change | Implementation/maintenance cost to investigate | Risk if omitted or applied carelessly |
|---|---|---|
| Separate pure parser/text/contract checks from HTML-build integration tests; make expensive fixtures explicit | Small-to-medium test organization change; measure dependencies first | Omission keeps even tiny probes expensive; careless splitting can stop testing real integration |
| Separate immutable historical acceptance checks from current-state invariants | Audit literal assertions and state their protected consequence | Omission repeats false failures on legitimate updates; careless loosening can hide lost decisions |
| Define fast, affected-integration, and final/release verification routes from changed inputs and risk | A small documented selection/invalidation policy, not a new orchestration platform | Wrong selection can miss cross-surface defects; defaulting every change to full repeats current cost |
| Reuse valid evidence only for unchanged relevant inputs and environment; preserve independent challenge | Explicit provenance and invalidation rules in existing evidence carriers | Blind reuse can accept stale results; blind reruns consume time without adding evidence |
| Close in the order review → docs/knowledge → affected-output verification → DONE; bound release/landing checks separately | Review existing closure contracts and test representative interruption paths | DONE before verification lies; an unbounded review/knowledge recursion becomes a new trap |
| Review test value and incident cost alongside correctness | Lightweight timings and counts in existing traces; exact token cost only where actually available | Arbitrary test-count/time caps can become another bureaucracy; no measurement hides runaway cost |

Do not assume a one-character diff is harmless. Test selection must follow the protected behavior and
dependencies, not changed-line count alone. Conversely, a late administrative change must not
automatically invalidate evidence for unchanged product inputs.

## 5. Expected outputs and observable completion

The later approved HL/TS should require:

1. A source-backed CRATM timeline separating product defects, stale assurance, harness mistakes,
   legitimate review work, and coordination overhead. State measured costs and unknowns separately.
2. A test inventory grouped by protected consequence, required inputs, fixture/build dependency,
   historical/current target, execution cost, and known false-positive or defect evidence.
3. A concrete decision table for common changes: text-only correction, parser behavior, canonical
   workflow plus copies, docs/knowledge capture, release, and lifecycle-only metadata.
4. A finite closure and recovery protocol with clear ownership, evidence invalidation, review
   re-entry conditions, and DONE last. An accepted ordinary administrative correction must not
   reopen the whole task merely to satisfy its own generated paperwork.
5. A bounded implementation proposal with KEEP, REWORK, MOVE, or REMOVE decisions and reasons;
   no removal solely to achieve a green run. Approve exact scope before changing tests or rules.
6. Before/after evidence on the same reference environment. At minimum, the representative pure
   text check must not invoke MkDocs; selected genuine defects must still fail; legitimate
   knowledge/result updates must pass; broader-risk changes must select their required checks.
7. A replay of the CRATM failure scenario through corrected verification and closure, including
   a late docs update and an interrupted/erroneous terminal write. Show convergence and fewer
   unnecessary runs; do not simply add another assertion spelling the repaired row.
8. A receiver-boundary check: repository-maintainer tests remain local, receiving projects keep
   their own commands, and a shared closure improvement does not impose this repository's
   corpus, Git history, Python, or MkDocs on ordinary TFW users.

Numerical runtime targets and allowable rerun counts must be chosen after a measured baseline,
with an explicit risk rationale. Do not invent another universal hard ceiling in this proposal.

## 6. Constraints and alternatives

- This proposal does not cancel, bypass, or rewrite CRATM's already approved final checks.
- It is not a new phase, dependency, or acceptance condition for CRATM.
- Do not start a new agent team, recurring timer, research run, or benchmark campaign now.
- Do not delete tests, mute failures, weaken meaningful safety checks, or edit user knowledge to
  match a test. Mechanical validation is not a truth assessment of project facts.
- Preserve immutable incident history; avoid duplicating whole transcripts in the proposal.
- Prefer changes to existing tests and workflow rules over a new test runner, state store, or
  permanent cost-control service.
- Compare keeping the current process, reducing assertions, and risk-based selection explicitly.
  Keeping the current process costs no implementation now but retains the observed failure mode.
  Removing tests broadly is cheap initially but loses protection; it is not the default solution.

## 7. Start boundary

The owner asked to record a future proposal. The next act is `/tfw-plan` on this task when scheduled:
use the finished CRATM evidence, approve the problem and scope, decide whether additional research
is necessary, then approve a proportionate TS. This proposal grants no autonomous execution mandate.

## 8. Reproducible source pointers

All paths below are repository-relative; use the immutable commit to distinguish incident evidence
from later legitimate changes. These are existing CRATM artifacts, not new PTTC research outputs.

| Source | Immutable commit | Path / section |
|---|---|---|
| Failed current-state guard and automatic site-build fixture | `7b4d4190c06a6ca02d55e23f90ed24214df8d2b5` | `docs/scripts/test_integration.py`: `build_site` and the named Phase E knowledge test |
| Actual repair boundary | `a7b9fd8b6a319d56850b9048e321f1242b288631` | Single-function commit diff in that test module |
| Main's repair order and original fixed scope | `85a97fb315c486c0889c6d5be467e92e62c213b8` | `workspace/2026/TFW_20260902-111644_CRATM/phase-e/REVIEW__phase-e__sweep_correction_and_release__rev2.md`, §8 |
| Late-round timings and failed attempts | `784ace52034a782ccf6930b033f106c1bf245082` | `workspace/2026/TFW_20260902-111644_CRATM/phase-e/evidence/phase-e-completion-tests.txt`, RETURN ROUND 2 |
| Independent review and correction dispositions | `784ace52034a782ccf6930b033f106c1bf245082` | `workspace/2026/TFW_20260902-111644_CRATM/phase-e/REVIEW__phase-e__sweep_correction_and_release__rev3.md`; `review/rev3/verify.md` |
| Existing shared closure rule | `b977b89be0c759297dd5653040564f0169ba3e56` | `.tfw/workflows/review.md`, Step 7; `.tfw/workflows/docs.md`, Apply and Route; `.tfw/workflows/knowledge.md`, Phase 4 |
| Project-owned build boundary | `b977b89be0c759297dd5653040564f0169ba3e56` | `.tfw/project_config.yaml`, `build`; `.tfw/workflows/update.md`, protected project-owned configuration |

Registration creates only this proposal, its TODO status, and one creation event. No test, workflow,
configuration, source knowledge, existing task, or release file is changed by registering PTTC.
