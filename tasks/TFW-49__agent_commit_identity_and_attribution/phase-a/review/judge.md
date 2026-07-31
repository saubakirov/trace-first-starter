# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. Every PASS needs independent evidence.
> **Test:** "Would I stake the Phase A approval on the reproduced result?"
> Mode: code
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | PASS | 10/10 AC pass; full contract/docs/build/range/scope matrix reproduced |
| 2 | Philosophy aligned | PASS | 10/10 Phase Principles pass; operator, honesty, ownership, and non-auth boundaries remain explicit |
| 3 | Tech debt documented | PASS | No new debt; TD-125/TD-126 are unchanged and not duplicated |
| 4 | Style & standards | PASS | Standard-library implementation, stable diagnostics, exact owners, type hints, and bounded docs |
| 5 | Observations collected | PASS | No new out-of-scope implementation defect; browser policy limitation is review-environment-specific |
| 6 | RF completeness (§§7–9) | PASS | Sections present; Fact Candidates challenged against human conversation history |
| 7 | Evidence completeness | PASS | 10/10 PR and 10/10 EV rows match reproduced behavior |

## Acceptance Criteria Judgment

| AC | Status | Independent judgment |
|----|--------|----------------------|
| AC-1 | PASS | Schema is the sole accepted registry/pattern owner; all consumed schema/state fields fail closed with exact codes/fields |
| AC-2 | PASS | State has exact policy/version/full anchor and false hook/authentication claims |
| AC-3 | PASS | C1-R format/parser/normalization and all registered work classes reproduce; unsafe forms reject |
| AC-4 | PASS | All reserved forms require complete public context; missing/stale errors and private range-only path reproduce |
| AC-5 | PASS | Operator, guarded `task:none`, full origins, optional metadata, and co-authorship stay distinct |
| AC-6 | PASS | Stable actionable diagnostics avoid arbitrary message/path/hook/credential/environment disclosure |
| AC-7 | PASS | Exact exclusive DAG semantics and every named topology/failure case pass |
| AC-8 | PASS | Six consumers preserve non-authentication/non-proof boundaries, bypasses, and Phase B/C ownership |
| AC-9 | PASS | Examples are schema-backed; final generated anchors and owner links resolve without a competing prose registry |
| AC-10 | PASS | Exact scope, 136 tests, 68 docs tests, identical MkDocs output, current range, and protected state pass |

## Phase Principles

| # | Principle | Status | Evidence |
|---|-----------|--------|----------|
| P1 | One executable contract | PASS | one schema/state interface, one Python consumer, no second registry/parser |
| P2 | Operator, not mythology | PASS | operator/origin/authorship/proof/acceptance are separate |
| P3 | Identity first | PASS | ordinary C1-R starts at byte zero; only exact same-context reserved nesting is exceptional |
| P4 | Prospective honesty | PASS | full anchor and exclusive descendant range protect earlier history |
| P5 | Closed registries, owned extension | PASS | schema fixture mutation changes behavior; malformed owners fail at load |
| P6 | Failure before fabrication | PASS | missing/stale/ambiguous context rejects; no branch/author/path guessing |
| P7 | Atomic provenance | PASS | same-origin default, full repeatable mixed origins, co-author coexistence |
| P8 | Secret-safe diagnostics | PASS | stable synthetic remediation, sentinel non-disclosure, no traceback |
| P9 | Cross-domain scope | PASS | master/phase/research/lifecycle, every surface and role are covered |
| P10 | No authentication overclaim | PASS | state/source/CLI/docs/RF/EV/audit all preserve the non-claim |

## Phase HL Definition-of-Failure Audit

| Clause | Status | Evidence |
|--------|--------|----------|
| PH-F1 second hard-coded registry | Not triggered | accepted values/patterns reside only in JSON |
| PH-F2 optional identity replaces mandatory C1-R field | Not triggered | models/sessions/account data remain optional, separate metadata |
| PH-F3 ambiguous field token accepted | Not triggered | complete invalid-character/separator matrix passes |
| PH-F4 `task:none` hides staged task work | Not triggered | staged canonical task paths reject |
| PH-F5 stale nested identity passes expected context | Not triggered | every stale field returns `E_CONTEXT_MISMATCH` |
| PH-F6 cross-context autosquash is presented as truthful | Not triggered | it is prohibited; routing remains Phase B |
| PH-F7 incomplete origin or implied acceptance | Not triggered | origin is full four-field repeatable context and a non-claim |
| PH-F8 audit selects fallback/recent range or condemns pre-anchor history | Not triggered | exact full anchor, no fallback, anchor excluded |
| PH-F9 diagnostics expose local/sensitive content | Not triggered | synthetic sentinel capture passes |
| PH-F10 contract claims authentication/unbypassable enforcement | Not triggered | auth false and six bypasses are explicit |
| PH-F11 Phase B/C/config/history behavior enters Phase A | Not triggered | exact scope/protected-state scan passes |

## TS Definition-of-Failure Audit

| Clause | Status | Evidence |
|--------|--------|----------|
| TS-F1 any Phase HL failure | Not triggered | PH-F1–PH-F11 all clear |
| TS-F2 registry/pattern duplication | Not triggered | source duplication scan and schema fixture consumption |
| TS-F3 malformed/stale lookalike accepted | Not triggered | negative parser/context matrices pass |
| TS-F4 valid non-code context rejected | Not triggered | lifecycle/research/docs work classes pass |
| TS-F5 `task:none` shortcut | Not triggered | declaration/lifecycle/staged-path guard passes |
| TS-F6 stale autosquash/replay identity published | Not triggered | stale context rejects; replay is not implemented |
| TS-F7 optional origin/model/session becomes mandatory/auth/acceptance | Not triggered | optional and semantically separate |
| TS-F8 range failure passes/falls back/rewrites | Not triggered | all fail-closed topology cases pass; no rewrite command |
| TS-F9 diagnostic disclosure | Not triggered | stable secret-safe output reproduced |
| TS-F10 hook/config/workflow/adapter/global-state change | Not triggered | protected diff is empty |
| TS-F11 named test/source/render/scope/review check fails | Not triggered | all named checks pass with the documented browser-policy limitation covered by rebuilt HTML and prior live observation |

## Mode-Specific Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 8 | Code quality | PASS | cohesive loader/parser/auditor separation and field-specific failures |
| 9 | Test coverage | PASS | 136 cases, including exhaustive consumed-owner and public-context negatives |
| 10 | Security | PASS | no disclosure, external hook read/copy, hook/config mutation, or authentication claim |
| 11 | Breaking changes | PASS | prospective version-1 C1-R only; C2-R rejected; later phases untouched |

## Scope and Quality Signals

- The final framework result is 1,708 lines, 508 above the configured attention
  signal. It is still one cohesive schema/state/parser/test/docs unit.
- The corrective 401 lines directly close D1/D2 through validation and negative proof;
  they add no router, selector, hook, workflow, adapter, or later-phase architecture.
- TD-125 attribution is reproducible as no baseline/final warning-set change.
- No new TECH_DEBT item qualifies.

## Contradictions with Project Knowledge

| Knowledge item | Relation | Contradiction? |
|----------------|----------|----------------|
| D28 — precise names shape behavior | fixed field/code vocabulary is enforced | No |
| D54 — thin adapter parity | adapters remain outside Phase A | No |
| D55 — role authority and observable enforcement | role/operator and exact range gate are explicit | No |
| D57 — Proof → Attestation → independent REVIEW | identity never substitutes for proof or acceptance | No |

## RF §§7–9 and Fact Candidate Challenge

RF §§7–9 are present and its "No Fact Candidates" statement was correct for the
Executor result. The later human override adds one new Human-Only process signal:
remote publication requires separate explicit human approval and is not implied by
implementation, review, or local commit completion. It is recorded in REVIEW §7 for
later `/tfw-knowledge` disposition, not treated here as already verified knowledge.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence
- [x] 10/10 AC and 10/10 Principles judged independently
- [x] All 22 Phase HL / TS Definition-of-Failure clauses explicitly audited
- [x] 10/10 PR/EV rows and Trust Protocol dispositions judged
- [x] Knowledge contradictions and conversation Fact Candidates challenged

Stage complete: YES
