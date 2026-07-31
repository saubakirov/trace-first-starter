# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. Every ruling is grounded in Verify evidence.
> Mode: code
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | Verify AC matrix: AC-3/4/10/11/12 fail |
| 2 | Philosophy aligned | ❌ | Failed mapped ACs violate P1/P3/P5/P7–P12 despite otherwise narrow non-claim language |
| 3 | Tech debt documented | ✅ | RF reports no observations; D1/D2 are current acceptance defects, not deferred debt |
| 4 | Style & standards | ❌ | Code is typed and readable, but runtime recognition is fail-open against the exact owned-shape convention |
| 5 | Observations collected | ✅ | RF §6 explicitly reports none; no unrelated backlog issue was found |
| 6 | RF completeness (§§7–9) | ✅ | Required sections exist; no new human-only fact or diagram claim is hidden |
| 7 | Evidence completeness | ❌ | PR-C3/4/10/12 and E3/E4/E10 overclaim the required negative matrix |

## Mode-Specific Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 8 | Code quality | ❌ | `verify.md` D1: manifest/directory recognition does not close the owned shape |
| 9 | Test coverage | ❌ | 345 tests pass, but required unexpected-inventory/manifest and canonical-prior idempotence cases are absent and fail independently |
| 10 | Security | ❌ | Diagnostics and external/global secrecy pass, but unknown reserved-target material is trusted as a recognized runtime |
| 11 | Breaking changes / migration | ❌ | Normal install/repair/rollback paths work, but the exact-prior lifecycle cannot satisfy the specified stable rollback/rollback transition |

## Principles Check

The TS maps each Phase HL principle to acceptance criteria. Per the review workflow,
any failed mapped AC is also a principle violation.

| Principle | Result | Basis |
|-----------|--------|-------|
| P1 Product value before mechanism | ❌ | AC-11 cannot close while prerequisite runtime gates fail |
| P2 One semantic owner | ✅ | schema/state/CLI/router ownership remains separated |
| P3 Tracked requirement, private reality | ❌ | AC-4 lifecycle state machine is incomplete for the exact prior owned value |
| P4 No contaminated templates | ✅ | clean null/root-inclusive template and destination derivation pass |
| P5 Repository-local means repository-local | ❌ | AC-3/4/10 fail by accepting unknown reserved-target material |
| P6 Explicit context or honest limitation | ✅ | complete/stale/absent context behavior passes |
| P7 Hooks are visibility, not identity proof | ❌ | non-claim wording passes, but mapped AC-3/11 do not |
| P8 Exact history over convenient samples | ❌ | audit itself passes; mapped AC-11 remains dependency-blocked |
| P9 Independent judgment | ❌ | review is independent, but AC-11/12 cannot accept the result |
| P10 Real proof stays real | ❌ | WSL/synthetic distinctions pass; PR-C10 still overstates matrix completeness |
| P11 Reversibility includes secrecy | ❌ | secrecy passes; D2 fails exact stable lifecycle behavior |
| P12 Publication is separate authority | ❌ | F26 is preserved, but mapped AC-11 cannot close |

## Definition of Failure Audit

| DoF | Status | Evidence |
|-----|--------|----------|
| 1 exact `1.1.0` | not triggered | schema/state/runtime exact |
| 2 duplicate semantic owner | not triggered | runtime consumes contract/router |
| 3 contaminated/invalid state | not triggered | template/current pairings pass |
| 4 incomplete range | not triggered | complete exclusive/root populations pass |
| 5 unknown reserved material trusted | **TRIGGERED** | D1 |
| 6 global/external hook/config access | not triggered | source/command spy and Reviewer conduct |
| 7 non-local config/non-relative path/bad restore | not triggered | exact restore occurs; D2 is idempotence after restore |
| 8 tracked/split/non-atomic ledger | not triggered | private common-dir behavior passes normal matrix |
| 9 tracked install inference/arbitrary carrier | not triggered | verified allowlist and child-only context |
| 10 prepare mutation/bad context | not triggered | context/non-mutation matrix passes |
| 11 final malformed/replay/task:none | not triggered | router/contract suites pass |
| 12 unsafe fixture/diagnostic disclosure | not triggered | redaction and source scans pass |
| 13 init/update overwrite/disagreement | not triggered | workflow/state/parity checks pass |
| 14 presence/Executor-only/incomplete acceptance | not triggered by Reviewer | verdict is REVISE and VD-C1 is not treated as acceptance |
| 15 synthetic represented as live/auth | not triggered | claim language remains narrow |
| 16 unsupported platform hidden | not triggered | exact Windows/WSL executions reproduced |
| 17 30th framework path/scope spill | not triggered | exact 29-path scope |
| 18 EV/RF hides limitation or misses relation | **TRIGGERED** | PR-C3/4/10/12 and E3/E4/E10 omit D1/D2 Value Debt |
| 19 publication/origin/history violation | not triggered | origin fixed; no remote/history action |

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|----------------|----------|----------------|
| 1 | D58/D59 one-owner and Phase C boundary | runtime/lifecycle consumes prior owners | No structural scope contradiction |
| 2 | process F26 | local work grants no push authority | No; origin remains fixed and no publication occurred |
| 3 | philosophy F4 / D57 | presence is not completion | No; this REVISE verdict prevents presence-based closure |

## Corrective Ruling

1. **D1 — close runtime recognition.** Install/verify/repair must reject every
   unexpected reserved-directory entry and every non-canonical manifest/target shape
   or semantic field, without reading or altering external/global material. Add
   negative fixtures for extra files, extra fields, and non-canonical non-empty
   entrypoints.
2. **D2 — close the exact-prior idempotence state.** Define and implement an
   unambiguous safe lifecycle for a pre-install local value already equal to
   `.tfw/hooks` so install/install, verify/verify, repair/repair, and rollback/rollback
   have stable dispositions while exact prior state and secrecy remain preserved.
3. **D3 — correct proof claims.** Re-run the full 345+ tests with the new negatives,
   both declared platform boundaries, docs/render/warning/parity/scope/current-range
   gates, and update PR-C3/4/10/12 plus E3/E4/E10/EV verdict/RF wording to the actual
   result. Do not treat the Reviewer commit as acceptance until the corrective full
   rerun passes.

## Checkpoint

**Self-check:**
- [x] Every checklist item cites Verify evidence
- [x] DoD ruling references the full AC matrix
- [x] RF §§7–9 checked for presence and quality
- [x] KNOWLEDGE.md and process F26 cross-referenced
- [x] RF Fact Candidates challenged; none qualify beyond already-recorded F26

Stage complete: YES
