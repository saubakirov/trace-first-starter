# TS — {ID} / Phase {X}: {Title}

> **Date**: YYYY-MM-DD
> **Author**: {author}
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-{ID}](path-to-HL)

---

## 1. Objective

{Delivered result and value.}

## 2. Scope

### In Scope

- {included work}

### Out of Scope

- {excluded work}

## 3. Principles Check

| # | HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P1 | {principle} | AC-{N} / N/A | {verification or reason} |

## 4. Affected Files and Value-Bearing Accounting

Classify whole paths by semantic purpose and accepted-output/necessary-constituent precedence. Classes:
`VALUE`, `ASSURANCE`, `TRACE`, `DERIVED`. A narrower exclusion requires a pre-work deterministic selector.

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `path` | CREATE / MODIFY / DELETE | `{class}` | {reason} |

### Prospective accounting contract

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | {paths or deterministic selector} |
| Baseline / selector source | {full immutable SHA}; this TS at {approval commit} |
| Candidate rule | First tested Executor commit with required VALUE+ASSURANCE, before EV/RF/REVIEW/final transition; excluded-only later writes do not move it; later VALUE requires a new Candidate and recomputation |
| Logical VALUE files | {planned count}; rename = one |
| Touched text LOC | {adds} + {deletes} = {total}; numeric numstat fields; binary/non-text = per-file N/A |
| Triggers / disposition | {configured file/LOC prompts; cause, cost, assurance, split, authority, terminal verdict, pre-work ref} |
| Multiplier / authority | {immutable planned denominator, boundaries, planned-zero rule, pre-work decision} |
| Approval epoch / failure | {prospective epoch}; missing/mutable/mismatched/late = BLOCKED; metric-only N/A; unresolved phase = INVALID; DEFERRED is non-terminal |

```powershell
git diff --name-status --find-renames=50% -z <BASELINE_SHA> <CANDIDATE_SHA> -- $valuePaths
git diff --numstat --find-renames=50% -z <BASELINE_SHA> <CANDIDATE_SHA> -- $valuePaths
```

### Prospective scope rulings

{None, or pre-work cause/cost/assurance/split/Saint-Exupéry/authority/verdict/time reference.}

### Task-local hard constraints (when material)

| M1 consequence | M2 object/risk | M3 measure/selector | M4 pre-act check | M5 softer-control gap | M6 change authority |
|---|---|---|---|---|---|
| {harm} | {boundary} | {direct measure} | {check} | {reason} | {role} |

**Actions (not budget dimensions):** {counts by class/action}.
**Immutable owner-approved denominator:** {VALUE files and touched LOC}; never ratchets.

## 5. Acceptance Criteria

Each AC is independently verifiable; dependencies use `[depends: AC-X]`. Gate is synthetic verification;
Evidence is real-environment verification: full/minimal spec, `N/A — reason`, `DEFERRED — reason`, or blank.

### AC-1: {title}

{Outcome.}
- [ ] {criterion}

Gate: {command/check}
Evidence: {real-environment check/status}

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__{ID}.md` | Per-AC evidence and verdict (required) |
| `evidence/{file}` | {additional artifact, if applicable} |

## 6. Technical Guidance

- {non-binding reference; Executor may deviate with RF justification}

## 7. Definition of Failure

- ❌ {hard reject condition}

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| {risk} | {mitigation} |

## 9. Cross-Phase Modifications (multi-phase only)

| File | Also modified in | Coordination note |
|---|---|---|
| `path` | Phase {X} | {note} |

> References use compilable-contract patterns (`RF TFW-18`, `D24`, `TD-72`).

---

*TS — {ID} / Phase {X}: {Title} | YYYY-MM-DD*
