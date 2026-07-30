# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Mode: code
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ❌ | Verify D1/D2 leave AC-1, AC-4, AC-6, and AC-10 unmet |
| 2 | Philosophy aligned | ❌ | P1/P5/P6 are not fully enforced because malformed owner semantics and absent reserved-form context can pass their intended gates |
| 3 | Tech debt documented | ✅ | RF §6 correctly avoids duplicating TD-125; the review findings are current closure defects, not deferred debt |
| 4 | Style & standards | ✅ | Standard-library implementation, type hints, stable names, canonical docs, exact role/scope boundaries, and protected-state discipline are otherwise sound |
| 5 | Observations collected | ✅ | RF §6 says no observations; independent review found correctable in-scope defects rather than new out-of-scope debt |
| 6 | RF completeness (§7–9) | ✅ | Fact Candidates, Strategic Insights, and diagram sections exist; no new Human-Only fact was omitted |
| 7 | Evidence completeness | ❌ | EV has all ten rows, but PR-1 and PR-4 are false in material part and RF V3 is not reproducible |

## Acceptance Criteria Judgment

| AC | Status | Independent judgment |
|----|--------|----------------------|
| AC-1 | ❌ | Production schema owns the expected data, but the declared schema-shape gate accepts missing/invalid consumed owner fields (Verify D1) |
| AC-2 | ✅ | Exact policy/version/full anchor and false hook/authentication state validate; ancestry is exact |
| AC-3 | ✅ | Ordinary formatting, parsing, normalization, registered values, and unsafe-input rejection reproduce |
| AC-4 | ❌ | Stale supplied context fails, but absent expected context validates a reserved form despite the binding supplied-context requirement (Verify D2) |
| AC-5 | ✅ | Operator, guarded `task:none`, full repeatable origins, optional metadata, and Git co-authorship remain distinct |
| AC-6 | ❌ | Normal sentinel diagnostics are secret-safe, but malformed schema-owned semantics are not rejected at their field boundary with the expected stable shape diagnostic (Verify D1) |
| AC-7 | ✅ | Exact exclusive `anchor..target` DAG behavior, merge uniqueness, root/unborn/shallow/missing/non-ancestor cases, and current audit reproduce |
| AC-8 | ✅ | All six consumers preserve operator/non-authentication/non-proof boundaries and Phase B/C ownership |
| AC-9 | ✅ | Schema-backed examples, source/generated owner links, exact anchors, rendered content, and layout reproduce |
| AC-10 | ❌ | Exact scope/tests/build/render/protected state pass, but the named independent claim checks fail and RF V3 is not reproducible |

## Phase Principles

| # | Principle | Status | Evidence |
|---|-----------|--------|----------|
| P1 | One executable contract | ❌ | The single owner exists, but its loader does not validate all consumed owner semantics |
| P2 | Operator, not mythology | ✅ | Operator/origin/authorship/acceptance remain distinct |
| P3 | Identity first | ❌ | Ordinary subjects are exact, but the reserved-form public gate lacks required supplied context |
| P4 | Prospective honesty | ✅ | Full anchor and exclusive descendant range preserve earlier history |
| P5 | Closed registries, owned extension | ❌ | Registry mutation is consumed, but semantically invalid owner extension data can pass schema validation |
| P6 | Failure before fabrication | ❌ | Missing reserved context and malformed owner semantics are accepted too early |
| P7 | Atomic provenance | ✅ | Full origins and co-author coexistence are preserved |
| P8 | Secret-safe diagnostics | ✅ | No arbitrary message/path/hook/credential/environment disclosure or traceback was observed |
| P9 | Cross-domain scope | ✅ | Master, phase, research, lifecycle, all surfaces, and all roles are covered |
| P10 | No authentication overclaim | ✅ | State, CLI, source, docs, audit, RF, and EV preserve the explicit non-claim |

## Mode-Specific Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 7 | Code quality | ❌ | Cohesive and readable overall, but `validate_schema` does not validate every downstream-consumed semantic field |
| 8 | Test coverage | ❌ | `46 passed`, but negative tests miss malformed truth/template ownership and absent public reserved context |
| 9 | Security | ✅ | No secret/path/body/environment disclosure; no external hook content inspected; no hook/config mutation |
| 10 | Breaking changes | ✅ | Prospective version-1 contract, C2-R rejected, no prior operational owner removed, later phases untouched |

## Scope and Quality Signals

- The 1,307 framework-line result exceeds the 1,200 attention signal by 107 lines.
  The diff remains one cohesive schema/state/executable/test/docs owner surface and
  does not spill into Phase B routing or Phase C installation. The variance is not a
  separate defect.
- All six approved framework consumers and all protected paths were checked at 100%.
- The identical pinned MkDocs comparison falsifies RF V3's measurements but yields the
  stronger product result of zero baseline/final warning delta. TD-125 is neither
  caused nor changed by Phase A.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF / implementation relation | Contradiction? |
|---|----------------|------------------------------|----------------|
| 1 | D28 — precise names shape behavior | Fixed field/diagnostic vocabulary is used | No |
| 2 | D54 — thin adapter parity | Adapter/workflow consumption remains Phase B | No |
| 3 | D55 — role authority and observable enforcement | Operator role and range gate are explicit | No |
| 4 | D57 — Proof → Attestation → independent REVIEW | Identity is never substituted for proof or acceptance | No |

## RF §7–§9 and Fact Candidate Challenge

RF §7–§9 are present. The conversation supplies no new Human-Only project fact during
review. The Coordinator's LOC handling direction is already recorded as RF S1 and is a
strategic execution disposition, not a new factual observation to invent or promote.
No Fact Candidate is added.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence?
- [x] Referenced Verify findings in DoD assessment?
- [x] Checked RF §7–§9 for presence and quality?
- [x] KNOWLEDGE.md cross-referenced?
- [x] Fact Candidates challenged against conversation history?

Stage complete: YES
