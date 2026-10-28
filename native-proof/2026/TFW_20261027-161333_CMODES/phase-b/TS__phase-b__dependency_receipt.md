# TS — TFW_20261027-161333_CMODES / Phase B: Dependency receipt

> **Date**: 2026-10-28
> **Author**: actual Coordinator `/root`
> **Status**: approved bounded verification order under product TS `18ee39772950a3be9cf42de3d49ae7c0c13c2c5b`; exact derived epoch is committed before dispatch.
> **Parent HL**: [phase HL](HL__phase-b__dependency_receipt.md)

## 1. Objective
Produce a checkable dependency receipt from the actual accepted A output, through real execution and fresh independent review under the same Coordinator.

## 2. Scope
Create this phase's `dependency-receipt.json` as ASSURANCE and required owned ONB/EV/RF/status/journal/numeric records. JSON has exactly four keys: `phase` = `phase-b`, `dependency_candidate` = the independently accepted A Candidate, `dependency_sha256` = SHA-256 of that Candidate's actual mode-receipt bytes, and `modes` = the ordered array decoded from those bytes. Read accepted A RF/Review and the immutable blob; this order does not substitute for reading the dependency. Do not edit A, framework/configuration, parent controls, HL/TS or another role's artifacts.

## 3. Principles Check
AC-1 proves accepted dependency use without repeating A work; AC-2 proves bounded new-phase activation, distinct state and independent Review. Existing authority, file context, Role Lock and own-source accounting remain applicable.

## 4. Affected Files and Value-Bearing Accounting
`native-proof/2026/TFW_20261027-161333_CMODES/phase-b/dependency-receipt.json`: CREATE ASSURANCE, disposable native verification excluded from shipped CMODES VALUE. Owned role/control/numeric records TRACE. Literal VALUE selector `[]`, fixed 0 logical files and 0 touched LOC (0 adds + 0 deletes), binary N/A. Baseline `2dc78f61903be0fb1a740dd1edc85ff56733cfd7`; Candidate is first tested ASSURANCE result commit before final TRACE. Empty selectors must return empty streams, never an unrestricted diff. Product denominator remains 38/2400; configured 50/5000 and 2× rules survive. No zero-plan VALUE growth or product fix is authorized here; a genuine product defect returns to CMODES Coordinator.

## 5. Acceptance Criteria
### AC-1: Accepted dependency
Exact UTF-8 JSON keys and values match the local phase and actual independently accepted A Candidate/blob. EV/RF identify immutable input/output, checks and observed results. B does not modify or pretend to repeat A.
### AC-2: Phase and role boundary
Actual unit/parent, B state/authority/cwd, requested/observed settings and own source are recorded. A returned invocation ends before this new bounded activation; source ranges preserve actual attribution. The separate fresh B Reviewer is selected by Coordinator and receives only its exact skill command at its gate. Reference-only returns, no copied conversation or peer raw session.
### Evidence Artifacts
Owned ONB/RF, `evidence/EV__phase-b__dependency_receipt.md` and numeric return. Required configured checks apply; reuse only when unchanged inputs/oracles/environment support the exact claim, with the basis stated. No permanent test or helper.

## 6. Technical Guidance
Use an isolated managed mutation checkout containing the committed B order and accepted A returns, explicit cwd, and a clean fixed Candidate. A reused native Executor may safely advance its own clean worktree to the exact new dispatch; validate receiving context before writing. Economics uses only its own source and proven disjoint B range; never duplicate or relabel A consumption.

## 7. Definition of Failure
Wrong or unaccepted dependency, role contamination, phase/source conflation, extra write, self-review or fabricated native coverage.

## 8. Phase Risks
This observation proves only the actual Codex native scenario. No other provider, disposal, full host restart or unlimited-capacity claim follows.

## 9. Cross-Phase Modifications
None. Accepted A is a read-only immutable dependency.
