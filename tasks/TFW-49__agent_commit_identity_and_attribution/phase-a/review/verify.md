# Verify — "Are the claims true?"
> **Mindset:** Auditor. RF is an attestation, not proof.
> **Test:** "Would the sources and reproduced outputs prove the result without RF prose?"
> Mode: code
> Min verify ratio: 0.42
> Escalated coverage: 100% of the six framework consumers, all Phase A traces, all
> 10 AC, all 10 Principles, all Definition-of-Failure clauses, and all 10 PR/EV rows

## Verification Log

### V1: schema and project-state ownership

- The production schema contains C1-R field order, identity/origin patterns, four
  reserved forms, rejected C2-R fallback, all registries, normalization, trailers,
  diagnostic example, and the complete truth boundary.
- The Python source contains loader keys and algorithms but no copied accepted
  surface/role/work registry or competing pattern registry.
- Independent mutations proved missing `truth_boundary`, incompatible
  `identity_template`, missing `ordinary_pattern` groups, and invalid truth-boundary
  shape fail during load with field-specific `E_SCHEMA_SHAPE`.
- Every downstream-consumed state owner field was removed independently. All failed
  closed with the exact field and `E_STATE_SHAPE`, except the contract-version owner
  which correctly uses `E_VERSION_MISMATCH`.
- State retains policy `agent-managed`, contract `1.0.0`, full anchor
  `f1106186417e84cdb38e797f7af66a60885bad76`, exclusive range semantics, no copied
  registry, `hook_runtime.installed:false`, and `actor_authentication:false`.

**Match:** PASS. Prior D1 is closed.

### V2: public contextual parsing and private structural audit

- All four reserved forms (`fixup!`, `squash!`, `amend!`, generated revert) were
  probed through the public library interface.
- Missing expected context fails with `E_EXPECTED_CONTEXT`; stale role context fails
  with `E_CONTEXT_MISMATCH`. The contract suite additionally covers every stale field.
- The public `parse_subject` signature has only `schema`, `subject`, `expected`,
  `non_task`, and `staged_paths`; it exposes no structural bypass.
- `_parse_subject_structural` is private. Source call-site inspection found its
  production use only inside `audit_range`; tests call it only to prove the boundary.
- Direct CLI probes returned exit 2 with the same stable actionable codes and the
  synthetic schema-owned correction, without echoing arbitrary input.

**Match:** PASS. Prior D2 is closed.

### V3: executable behavior, diagnostics, and tests

- `python -m compileall -q .tfw/scripts/commit_identity.py` passed.
- `validate-state` returned `{"status":"valid","contract_version":"1.0.0"}`.
- `describe` returned C1-R, the schema-backed example, and the exact claim,
  six non-claims, and six known bypasses.
- The full original-plus-corrective suite passed `136 passed`.
- Coverage includes registry/pattern fixture consumption, every surface/role/work
  class, canonical work normalization, guarded `task:none`, complete origins,
  optional metadata, `Co-authored-by`, safe diagnostics, and Git topology.
- AST import inspection found standard-library imports only.

**Match:** PASS.

### V4: exact anchored Git graph

- At target `b4c0a06dc9fbc104c5b8997865b6df3211bd5c0c`, `audit-range` returned valid,
  exclusive anchor semantics, `commit_count:6`, and `actor_authentication:false`.
- The six descendants are, in order:
  `642c647f91088e98c15f559c9553804433878fe6`,
  `d30d8deb84bd0946e3a8149b51a11c5e94515ee2`,
  `7740d83e6035b458a1e1f9bbbb4fd447cb4370d4`,
  `b83d8ee320f0dc54a3da901589f2026189ad33a9`,
  `929c489126f5fd78c8b606da98114867ceda1e67`, and
  `b4c0a06dc9fbc104c5b8997865b6df3211bd5c0c`.
- The passing suite independently covers anchor exclusion, every invalid descendant,
  merge uniqueness/completeness, missing object/target, root/unborn, non-ancestor,
  and shallow-history failure.
- No pre-anchor compliance or actor-authentication conclusion is drawn.

**Match:** PASS.

### V5: documentation, rendering, and warning attribution

- The docs suite passed `68 passed`.
- Identical isolated source trees at baseline `7740d83e...` and final `b4c0a06...`
  were built with Python 3.13.5 / MkDocs 1.6.1 and the exact same command.
- Both builds exited 0. The RF filter produced `283/283` warning lines,
  `131/131` normalized distinct warnings, and `0 added / 0 removed`.
- Current generated HTML contains exactly one conventions anchor and one glossary
  anchor, three owner links in each section, the glossary-to-conventions anchor link,
  and zero unresolved commit-identity `.md` links.
- A fresh interactive localhost/browser pass was attempted but the app browser's URL
  policy blocked local navigation. This is a review-environment limitation, not a
  product failure. The prior independent review already reproduced the live
  `1265/1265` no-overflow observation; the corrective documentation delta is four
  additions/two removals in the same bounded prose section, while the current final
  generated HTML and full docs suite were independently rebuilt and inspected.

**Match:** PASS, with the stated browser-policy limitation. Prior D3 is closed and RF
V3/EV wording matches the reproduced values.

### V6: exact scope, protected state, and attention signal

- Baseline-to-final framework scope is exactly six consumers: four added JSON/Python
  paths and two modified docs paths.
- The corrective diff changes only conventions, validator, validator tests,
  README, RF, and EV. It does not change HL, TS, ONB, REVIEW/stage inputs, RES,
  KNOWLEDGE, TECH_DEBT, project config, hooks, workflows, adapters, or later phases.
- `.tfw/hooks` has no tracked path; repository-local `core.hooksPath` is unset.
- `git diff --check` passes.
- Physical framework accounting reproduces original `1,307`, final `1,708`,
  corrective delta `401`, and signal variance `+508`. The increase is cohesive and
  confined to the existing owner/parser/test/docs boundary.

**Match:** PASS.

### V7: Evidence, Trust Protocol, and citations

- All ten Proof Records and all ten Evidence rows exist and map one-to-one to AC-1
  through AC-10.
- E1–E8 N/A dispositions are justified: their Requirement Claims are deterministic
  Local/Seam relations and do not trigger intended-environment observation.
- E9/E10 VERIFIED remains scoped to rendered/current-repository observation and does
  not authenticate an actor or approve the phase.
- PR-1 and PR-4 now match independent negative probes. PR-9/PR-10 match the rebuilt
  final pages, warning comparison, scope, and tests.
- Phase HL 10 citations and Master HL 12 citations still resolve to their named files,
  headings, decisions, and Challenge items; ONB mirrors all 22. None of those sources
  changed in the corrective commit.

**Match:** PASS: 10/10 Proof Records, 10/10 Evidence rows, 22/22 citations.

## Commands and Methods Executed

| # | Command / method | Result |
|---|------------------|--------|
| 1 | Full contract pytest command | `136 passed in 7.56s` |
| 2 | Full docs pytest command | `68 passed in 47.43s` |
| 3 | Compile, JSON/state validation, `describe`, AST import scan | PASS; standard library only |
| 4 | Independent 24-case owner/context mutation probe | `24/24` passed with exact field/code checks |
| 5 | Direct public CLI missing/stale context probes | exit 2; `E_EXPECTED_CONTEXT` / `E_CONTEXT_MISMATCH` |
| 6 | `audit-range` at `b4c0a06...` plus reverse log | exact 6 descendants; valid; auth false |
| 7 | Identical isolated baseline/final MkDocs build and normalized set comparison | `283/283`, `131/131`, `0/0`, both exit 0 |
| 8 | Current generated HTML anchor/link checks | anchors 1/1; owner links 3/3; unresolved commit `.md` links 0 |
| 9 | Full/corrective `git diff`, protected-path, hook/config, and `diff --check` scans | exact scope; protected state unchanged |
| 10 | Physical-line accounting from pinned original/final trees | `1307 → 1708`, corrective `+401`, signal variance `+508` |

The temporary Python 3.13 permission normalizer was used outside the repository only
to avoid Windows sandbox `0700` temp-directory denial. It changed neither product
inputs nor outputs. The repository `.tfw/review-tmp-new/` directory was removed before
final diff/commit.

## Discrepancies

No remaining material discrepancy. Any earlier discrepancy triggered 100% coverage;
the complete Phase A result, not only the corrective patch, was rechecked.

## Evidence Verification

| Evidence | Result | Independent basis |
|----------|--------|-------------------|
| E1 / PR-1 | PASS | owner-field removal, semantic mutations, source-duplication scan, 136 tests |
| E2 / PR-2 | PASS | exact state/version/anchor, malformed-state matrix, current ancestry |
| E3 / PR-3 | PASS | complete formatter/parser/normalization registry matrix |
| E4 / PR-4 | PASS | four-form public/library/CLI context matrix and private range path |
| E5 / PR-5 | PASS | `task:none`, origins, metadata, trailer/co-author coexistence |
| E6 / PR-6 | PASS | sentinel non-disclosure and stable field/actionable diagnostics |
| E7 / PR-7 | PASS | complete topology suite and exact current six-commit range |
| E8 / PR-8 | PASS | six-consumer non-claim/bypass/phase-boundary scan |
| E9 / PR-9 | PASS | current generated HTML/docs build plus prior live layout observation |
| E10 / PR-10 | PASS | exact scope/tests/build/range/protected-state reproduction |

## Checkpoint

**Self-check:**
- [x] Verification escalated to 100% after prior discrepancies
- [x] All ten RF AC checkmarks verified against actual sources and outputs
- [x] All ten Phase Principles and every Phase/TS Definition-of-Failure clause checked
- [x] All ten PR rows and ten EV rows checked under the Trust Protocol
- [x] All 22 knowledge citations verified and unchanged
- [x] Temporary review artifacts removed from the repository

Stage complete: YES
