# HL — TFW-49 / Phase A: Canonical Commit Identity Contract and Validator

> **Date**: 2026-07-30
> **Author**: Coordinator (Codex)
> **Status**: ✅ HL — Approved under delegated owner authority
> **Master HL**: [TFW-49](../HL-TFW-49__agent_commit_identity_and_attribution.md)
> **Research**: [Iteration 1 RES](../research/iter1/RES.md) — SUFFICIENT
> **Depends on**: Research Iteration 1 ✅

---

## 1. Vision

Phase A turns C1-R from an approved research configuration into one executable,
versioned semantic contract. The contract can format, parse, validate, and audit commit
identity without hooks, workflow duplication, or external services. It owns field
registries, normalization, Git-reserved same-context forms, optional attribution
records, stable diagnostics, and the prospective activation range.

The phase does not install hooks or change how workflows invoke Git. Its output is the
single behavior owner that Phases B and C will consume.

**Impact:** Every later consumer can refer to one tested grammar rather than
reimplementing punctuation or field meaning. The task’s first compliant commit after
the recorded anchor can already be audited before permanent hook installation.

## 2. Approved Result

### 2.1 C1-R ordinary subject

```text
[<surface>/<task>/<work>/<role>] <summary>
```

The mandatory fields mean:

| Field | Meaning |
|-------|---------|
| `surface` | registered stable agent interaction surface operating the commit |
| `task` | canonical TFW task ID, or guarded `none` for declared non-task lifecycle work |
| `work` | canonical master, phase, research iteration, or lifecycle slice |
| `role` | commit operator’s active TFW Role Lock |
| `summary` | non-empty concise result |

C2-R labeled fields remain a documented fallback only. Phase A does not implement two
simultaneously valid subject grammars.

### 2.2 Data and executable ownership

```text
commit_identity.schema.json  → universal fields, registries, patterns, trailers
commit_identity_state.json   → project policy, contract version, activation anchor
commit_identity.py           → formatter, parser, validator, diagnostics, range audit
conventions/glossary         → human meaning and point-to-owner references
```

Universal schema and project state are separate so `/tfw-update` can later replace
method data without overwriting a project’s activation history.

### 2.3 Prospective range

The full activation anchor is:

```text
f1106186417e84cdb38e797f7af66a60885bad76
```

It is the last pre-policy commit. Commit
`642c647f91088e98c15f559c9553804433878fe6` is the first descendant intentionally
written in C1-R form. Phase A must audit `anchor..target` and must never judge commits
at or before the anchor.

## 3. Scope

### In Scope

1. One universal JSON schema for C1-R field registries, patterns, reserved forms,
   trailer names, and contract version.
2. One project state JSON record for `agent-managed` policy and activation anchor.
3. One standard-library executable supporting format, parse/validate, expected-context
   comparison, message-file validation, state/schema validation, and Git range audit.
4. Stable field-specific diagnostics with a complete corrected example and no
   arbitrary path, message body, hook body, credential, or environment disclosure.
5. Operator semantics, full repeatable optional content origin, separate optional
   model/session/source records, same-context-only autosquash/generated nesting, and
   guarded `task:none`.
6. Local documentation ownership and comprehensive temporary-repository tests.

### Out of Scope

- Git commit execution, merge/revert/cherry-pick routing, or a `/tfw-commit` command;
  Phase B owns action routing.
- `prepare-commit-msg`, `commit-msg`, `core.hooksPath`, init/update installation,
  repair, rollback, or global-hook changes; Phase C owns them.
- Workflow, adapter, root instruction, skill, or command consumption; Phase B owns it.
- Hosted identity, actor authentication, branch protection, or CI-provider policy.
- Rewriting, amending, rebasing, or relabeling historical commits.
- Reading, copying, fingerprinting, executing for tests, or diagnosing arbitrary
  existing hook bodies or the redacted sensitive material.

## 4. Deliverables

1. Canonical schema and state records with one contract version.
2. Cross-platform Python standard-library contract CLI.
3. Test suite covering grammar, registries, operations, optional records, audit range,
   bypass-shaped history, and secret-safe diagnostics.
4. Canonical conventions section and concise glossary term.
5. Phase EV/RF and independent REVIEW proving the contract before Phase B consumes it.

## 5. Definition of Done

- ✅ 1. C1-R is the only accepted ordinary grammar; each field and summary has an
  exact non-overlapping meaning.
- ✅ 2. Universal schema and project state are separate, valid JSON, version-related,
  and consumed rather than duplicated by the executable.
- ✅ 3. Current registered surfaces are `antigravity`, `claude-code`, `codex`, and
  `cursor`; roles are `coordinator`, `researcher`, `executor`, and `reviewer`.
- ✅ 4. Work normalization covers current master, phase, research, docs, knowledge,
  release, config, init, update, and maintenance scopes without ambiguous separators.
- ✅ 5. `task:none` requires an explicit non-task declaration, lifecycle work, and no
  staged canonical task path.
- ✅ 6. Core role/surface describe the operator; optional full
  `TFW-Content-Origin` records do not imply acceptance and coexist with
  `Co-authored-by`.
- ✅ 7. Same-context reserved forms validate; cross-context autosquash, replay,
  amend, or generated nested identity fails expected-context comparison.
- ✅ 8. Diagnostics are deterministic, actionable, field-specific, and secret-safe.
- ✅ 9. The audit validates every descendant in the exact recorded range, rejects a
  missing/non-ancestral anchor or structural violation, and preserves pre-anchor
  history outside the claim.
- ✅ 10. Tests reproduce the first compliant task commit, malformed/bypass-shaped
  commits, multiple surfaces/roles/scopes, state/schema errors, fresh/root and
  ancestry cases, search keys, and Windows/POSIX path behavior available locally.
- ✅ 11. Conventions and glossary point to the executable/data owner without creating
  a second registry or representing identity as authentication, proof, attestation,
  or review.
- ✅ 12. Independent REVIEW approves all claims before Phase B begins.

## 6. Definition of Failure

- ❌ The executable contains a second hard-coded registry that can drift from schema.
- ❌ The schema allows model, session, Git account, branch, or review verdict to
  replace a mandatory C1-R field.
- ❌ A field can contain slash, bracket, whitespace, empty/consecutive separators, or
  another ambiguous token outside its exact rule.
- ❌ `task:none` can hide staged task-scoped work.
- ❌ A structurally valid stale nested identity passes expected-context validation.
- ❌ Cross-context autosquash is represented as transparent or truthful.
- ❌ An origin record omits task/work when the origin differs, or implies acceptance.
- ❌ Audit silently chooses a recent range, passes a missing/non-ancestral anchor, or
  treats pre-anchor history as non-compliant.
- ❌ A diagnostic prints commit-message body, arbitrary configured path, hook body,
  secret, credential, or full environment.
- ❌ The contract claims actor authentication or that hooks/audit cannot be bypassed.
- ❌ Phase B/C workflow, hook installation, global config, or history mutation enters
  Phase A.

**On failure:** stop Phase A, leave hook/config/history state unchanged, record the
failed contract claim and repair the canonical owner before any consumer is added.

## 7. Principles

1. **One executable contract** — grammar data and behavior are resolved through one
   schema/state interface.
2. **Operator, not mythology** — subject fields describe declared commit-operation
   context, never inferred authorship or acceptance.
3. **Identity first** — ordinary subjects begin at byte zero with C1-R; only exact
   Git-reserved same-context nesting is exceptional.
4. **Prospective honesty** — the activation anchor bounds the claim and protects
   historical evidence.
5. **Closed registries, owned extension** — additions are explicit method changes
   with synchronized fixtures.
6. **Failure before fabrication** — missing or ambiguous context is rejected, never
   guessed from branch, path, author, or prose.
7. **Atomic provenance** — same-origin commits are default; mixed origin is explicit
   and complete.
8. **Secret-safe diagnostics** — validation reports the contract failure, not
   arbitrary local content.
9. **Cross-domain scope** — task/work/role apply to all TFW deliverables, not code
   alone.
10. **No authentication overclaim** — syntax is contractual provenance and remains
    distinct from Git authorship, Proof Records, RF, and REVIEW.

### 7.1 Knowledge Citations

| # | Source | Item | How it applies |
|---|--------|------|----------------|
| 1 | [Master HL](../HL-TFW-49__agent_commit_identity_and_attribution.md) | C1-R and activation contract | Phase A implements the approved grammar, range, and truth boundary only. |
| 2 | [Iteration 1 RES](../research/iter1/RES.md) | D1–D9 | Research defines the challenged fields, operations, enforcement split, and non-claims. |
| 3 | [KNOWLEDGE.md](../../../KNOWLEDGE.md) | D28 | Precise names and fixed meanings reduce prompt volume and drift. |
| 4 | [KNOWLEDGE.md](../../../KNOWLEDGE.md) | D54 | Adapter additions require behavioral parity and thin consumption. |
| 5 | [KNOWLEDGE.md](../../../KNOWLEDGE.md) | D55 | Role authority and observable enforcement are Method Kernel obligations. |
| 6 | [KNOWLEDGE.md](../../../KNOWLEDGE.md) | D57 | Identity provenance cannot replace claim-typed proof or independent review. |
| 7 | [.tfw/README.md](../../../.tfw/README.md#honesty-over-convincingness) | Honesty Over Convincingness | Missing/stale identity fails rather than being plausibly inferred. |
| 8 | [.tfw/README.md](../../../.tfw/README.md#single-source-of-truth) | Single Source of Truth | Schema/state/executable ownership must prevent registry duplication. |
| 9 | [.tfw/conventions.md](../../../.tfw/conventions.md#15-role-lock-protocol) | Role Lock | The role field names the authority actually operating the commit. |
| 10 | [Research Challenge](../research/iter1/4_challenge.md) | C1–C8 | Edge behavior and selected repairs are acceptance-critical. |

## 8. Risks

| Risk | Mitigation |
|------|------------|
| JSON and Python both become semantic owners | Load every registry/pattern from JSON and test that examples/diagnostics use loaded data. |
| Parser grows into Phase B operation router | Keep Phase A commands pure: format, validate, expected-context compare, and audit only. |
| Range audit mishandles Git topology | Test root/unborn, missing object, non-ancestor, merge descendants, shallow indication, and explicit fail-closed paths. |
| Optional trailers become hidden mandatory identity | Test that C1-R stands alone and trailers never replace core fields. |
| Secret-safe errors become too vague | Emit stable code, field name, rule, and synthetic corrected example without local content. |
| C2-R fallback causes two accepted grammars | Document fallback only; executable accepts C1-R until an approved future decision changes version. |

## 9. Phase Boundary

Phase A hands Phase B:

- the exact CLI and data contract;
- accepted/rejected operation forms;
- current surface/role/work registries;
- context inputs that a commit entrypoint must supply;
- stable error codes and audit interface;
- activation anchor and current conforming-range result.

Phase B may add an operation router and consumers but may not redefine the grammar.
Phase C may install thin hooks and configure Git but may not add a second validator.

---

*HL — TFW-49 / Phase A: Canonical Commit Identity Contract and Validator | 2026-07-30*
