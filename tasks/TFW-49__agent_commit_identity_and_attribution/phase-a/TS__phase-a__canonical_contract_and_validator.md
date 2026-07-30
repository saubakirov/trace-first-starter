# TS — TFW-49 / Phase A: Canonical Commit Identity Contract and Validator

> **Date**: 2026-07-30
> **Author**: Coordinator (Codex)
> **Status**: ✅ TS — Approved for execution under delegated owner authority
> **Parent HL**: [Phase A HL](HL__phase-a__canonical_contract_and_validator.md)
> **Master HL**: [TFW-49](../HL-TFW-49__agent_commit_identity_and_attribution.md)
> **Research**: [Iteration 1 RES](../research/iter1/RES.md) — SUFFICIENT
> **Execution approval**: 2026-07-30

---

## 1. Objective

Implement the single data and executable owner for C1-R commit identity before any
workflow or Git-hook consumer is added. Phase A must provide a deterministic formatter,
parser, validator, expected-context comparator, and prospective Git range audit whose
claims are bounded by the recorded activation anchor and the explicit
non-authentication contract.

## 2. Scope

### In Scope

- Add a universal JSON schema containing contract version, C1-R field registries,
  patterns, canonical work scopes, reserved same-context forms, and optional trailer
  names.
- Add a separate project state JSON record for the `agent-managed` policy, contract
  version, and full `f110618...` activation anchor.
- Add one Python standard-library executable that consumes both records and supports
  formatting, subject/message validation, expected-context comparison, state/schema
  validation, and anchored range audit.
- Add comprehensive automated contract and temporary-Git tests.
- Add one canonical conventions section and one concise glossary entry that point to
  the executable/data owner.
- Audit commit `642c647...` and every later Phase A planning/execution/review commit
  against the prospective range without changing history or Git configuration.

### Out of Scope

- A Git commit wrapper/router, actual `git commit` execution, or replay orchestration.
- Hooks, hook-path installation, init/update repair, rollback, or any global/local Git
  config mutation.
- Workflow, adapter, root instruction, command, or skill consumers.
- Hosted/actor authentication, branch policy, or CI-provider integration.
- Historical rewrite or validation of commits at or before the anchor.
- Arbitrary existing hook-body access or redacted credential remediation.

## 3. Principles Check

| # | Principle (Phase HL §7) | Enforced by | Gate |
|---|-------------------------|-------------|------|
| P1 | One executable contract | AC-1, AC-2, AC-9 | Registry/pattern duplication scan and mutation fixtures |
| P2 | Operator, not mythology | AC-3, AC-5, AC-8 | Operator/origin/authentication scenarios |
| P3 | Identity first | AC-3, AC-4 | Ordinary and reserved-form parser matrix |
| P4 | Prospective honesty | AC-7 | Exact anchor/range and history-preservation proof |
| P5 | Closed registries, owned extension | AC-1, AC-3, AC-9 | Registered/unregistered and schema-version matrix |
| P6 | Failure before fabrication | AC-5, AC-6 | Missing/ambiguous/stale expected-context diagnostics |
| P7 | Atomic provenance | AC-5 | Repeated full origin and co-author trailer scenarios |
| P8 | Secret-safe diagnostics | AC-6 | Sentinel/path/body/environment non-disclosure checks |
| P9 | Cross-domain scope | AC-3, AC-9 | Master/phase/research/lifecycle cases across all roles |
| P10 | No authentication overclaim | AC-2, AC-8, AC-10 | Source/doc scan and RF limitation attestation |

## 4. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `.tfw/commit_identity.schema.json` | CREATE | Universal C1-R data owner: version, registries, patterns, reserved forms, trailers |
| `.tfw/commit_identity_state.json` | CREATE | Project-owned policy/version/activation anchor |
| `.tfw/scripts/commit_identity.py` | CREATE | Standard-library formatter, validator, expected-context comparator, and range auditor |
| `.tfw/scripts/test_commit_identity.py` | CREATE | Unit, contract, and temporary-Git behavior suite |
| `.tfw/conventions.md` | MODIFY | Canonical human contract, truth boundary, consumer relation, and range invariant |
| `.tfw/glossary.md` | MODIFY | Concise Commit Identity definition with owner links |

**Scope-attention measurement:** six framework files, four new and two modified;
estimated 650–1,000 changed lines. Current configured signals are 14 files, 8 new,
1,200 LOC, and 12 modified. The phase is below each signal; cohesion is still checked
because schema, state, executable, tests, and human contract form one proof boundary.
Task traces and the README Task Board update are lifecycle files outside the six-file
framework set.

**Response:** Below signals — no automatic split. Unrelated workflow, adapter, hook,
and installation work is excluded to Phases B/C.

## 5. Acceptance Criteria

### AC-1: Universal schema is the single operational data owner

The universal JSON record defines every value or pattern needed to parse C1-R without
duplicating registries in Python or prose.

- **Intent / authority:** Master HL DoD 2, Phase HL P1/P5, RES D1/D4.
- **Claim:** One valid versioned JSON schema owns C1-R field order, registered
  surfaces/roles/lifecycle work, task/phase/research patterns, reserved forms,
  optional trailer names, and diagnostic-example inputs.
- **Boundary:** Local schema ↔ executable ↔ conventions/glossary consumers.
- **Precision:** File path and field meanings are acceptance-critical; internal JSON
  nesting is adaptable if all consumers remain generated/resolvable.
- **Proof intent:** Local JSON/schema checks plus Seam Proof that executable behavior
  changes when fixture schema data changes.
- [ ] Registered surfaces are exactly `antigravity`, `claude-code`, `codex`, `cursor`.
- [ ] Registered roles are exactly `coordinator`, `researcher`, `executor`, `reviewer`.
- [ ] Fixed field order is `surface/task/work/role`.
- [ ] Owned work scopes and strict task/phase/research patterns cover current TFW
  forms and reject ambiguous separators/characters.
- [ ] C2-R is documented as fallback but is not an accepted schema grammar.
- [ ] Python contains no duplicate production registry/pattern constants.

Gate: Parse the JSON with the standard library, mutate registry data only in a
temporary fixture, and prove formatter/validator results follow the fixture.

Evidence: N/A — source/data ownership is established through Local/Seam Proof.

### AC-2: Project state records policy and prospective activation

Project state binds this repository to the universal contract without mixing
project history into the universal schema.

- **Intent / authority:** Master HL activation decision, RES D2/D8.
- **Claim:** A separate valid JSON state records `agent-managed`, matching contract
  version, and full activation anchor
  `f1106186417e84cdb38e797f7af66a60885bad76`.
- **Boundary:** Project state ↔ schema version ↔ Git ancestry/range.
- **Precision:** Exact policy, version relation, and full anchor are binding.
- **Proof intent:** Local validation plus Git ancestry Seam Proof.
- [ ] State contains no copied universal registry.
- [ ] Version mismatch fails with a stable code.
- [ ] Missing/invalid/null anchor fails for an activated existing repository.
- [ ] The anchor resolves and is an ancestor of current `HEAD`.
- [ ] State does not claim hook installation or actor authentication.

Gate: Validate current state, then exercise missing, malformed, mismatched-version,
unknown-object, and non-ancestor fixture states.

Evidence: N/A — state/ancestry is synthetic and structural.

### AC-3: C1-R formatting, parsing, and normalization

The executable formats and parses the approved ordinary grammar and field semantics
for all registered surfaces, roles, and work classes.

- **Intent / authority:** User S1–S3, RES D1–D4.
- **Claim:** Valid context produces exactly
  `[surface/task/work/role] summary`; invalid or ambiguous context never produces a
  plausible identity.
- **Boundary:** Schema ↔ CLI inputs ↔ subject output.
- **Precision:** Delimiters, field order, lower-case canonical output, role/operator
  meaning, task syntax, and non-empty summary are binding.
- **Proof intent:** Local parser/formatter matrix and search-key checks.
- [ ] Master, `phase-a`, `phase-a2`, accepted dotted phase class,
  `research-iter1`, docs, knowledge, release, config, init, update, and maintenance
  normalize and round-trip.
- [ ] Legacy `PhaseA`, `PhaseA2`, and equivalent known forms normalize only at the
  formatter/entry boundary; validator requires canonical output.
- [ ] Slash, brackets, whitespace, empty/consecutive separators, model/version
  suffixes in surface, and unknown role/surface fail.
- [ ] `summary` is non-empty after normalization and cannot be only whitespace.
- [ ] Exact regex-safe filters independently locate surface, task, work, and role.

Gate: Run a table-driven format/parse/round-trip matrix covering every registry entry
and invalid-character class.

Evidence: N/A — grammar is verified synthetically.

### AC-4: Git-reserved and generated forms are same-context only  [depends: AC-3]

Reserved markers never justify stale operator identity.

- **Intent / authority:** RES D5, Challenge C1–C2.
- **Claim:** `fixup!`, `squash!`, `amend!`, and supported generated revert nesting
  validate only when the nested C1-R identity exactly equals supplied expected
  context; cross-context use fails.
- **Boundary:** Git subject form ↔ nested identity ↔ expected operator context.
- **Precision:** Marker spelling and equality of all four fields are binding; the
  executable does not implement Git replay.
- **Proof intent:** Local matrix plus synthetic autosquash/revert subjects.
- [ ] Ordinary subjects accept no arbitrary leading token.
- [ ] Same-context reserved examples validate structurally and contextually.
- [ ] Any one-field context difference fails with a stable mismatch code.
- [ ] Cross-context autosquash is reported as prohibited, not auto-rewritten.
- [ ] Cherry-pick/revert source identity is never accepted as current merely because
  it is structurally valid.

Gate: Validate exact same-context and one-field-different variants for every supported
reserved form.

Evidence: N/A — actual routing belongs to Phase B.

### AC-5: Operator, task-none, and optional attribution remain truthful  [depends: AC-3]

The contract keeps operator identity, content origin, co-authorship, and optional
metadata distinct.

- **Intent / authority:** RES D3/D4/D9, D57.
- **Claim:** Core role/surface represent declared commit operator; `task:none` and
  optional records cannot compress or escape task/work provenance.
- **Boundary:** Subject ↔ staged task paths ↔ trailers ↔ Git authorship semantics.
- **Precision:** Full `TFW-Content-Origin: surface/task/work/role` is binding when
  used; model/session/source trailers remain optional declared metadata.
- **Proof intent:** Local message/staged-path/trailer parsing plus Seam Proof with
  `git interpret-trailers`.
- [ ] `task:none` requires explicit non-task mode, lifecycle work, and no staged
  `tasks/<canonical-id>/...` path.
- [ ] `none/master`, `none/phase-*`, and `none/research-*` fail.
- [ ] Task-scoped staged paths with `task:none` fail.
- [ ] Repeated full origin records and `Co-authored-by` parse as independent entries.
- [ ] Short origin records fail; origin never changes core operator.
- [ ] Model/session/source values are checked for newline/control/secret-shaped
  unsafe input without becoming mandatory identity.

Gate: Temporary repository cases cover task/no-task staged paths, repeated origins,
co-author trailers, and operator/origin disagreement.

Evidence: N/A — no live identity provider is claimed.

### AC-6: Diagnostics are actionable and secret-safe  [depends: AC-1, AC-3]

Every failure names the contract defect and a complete synthetic correction without
echoing arbitrary local content.

- **Intent / authority:** Master DoF 7/8, Phase HL P6/P8.
- **Claim:** Diagnostics expose stable code, failed field/rule, and remediation while
  excluding message body, configured paths, arbitrary hooks, credential sentinels,
  and environment dumps.
- **Boundary:** CLI failure ↔ stderr/stdout ↔ local sensitive inputs.
- **Precision:** Non-disclosure classes and non-zero exit behavior are binding;
  wording is adaptable if tests match stable codes.
- **Proof intent:** Local sentinel tests and captured outputs.
- [ ] Missing identity gives one complete valid synthetic example.
- [ ] Field/context/state/range errors have distinct stable codes.
- [ ] No test sentinel from message body, path, hook-like body, environment, or
  credential-shaped value appears in diagnostics.
- [ ] Success output is machine-readable or quiet as documented.
- [ ] Exceptions do not emit Python tracebacks for expected user errors.

Gate: Capture every expected failure with sentinel inputs and scan all output.

Evidence: N/A — diagnostic non-disclosure is Local Proof.

### AC-7: Anchored all-commit range audit is exact and fail-closed  [depends: AC-2, AC-3, AC-4, AC-5]

The audit proves structural coverage for every descendant after the recorded anchor
without authenticating actor identity or relabeling history.

- **Intent / authority:** User all-commit policy, RES D8/D9.
- **Claim:** Audit evaluates the exact `anchor..target` commit set, reports every
  structural violation, and fails closed when the range cannot be justified.
- **Boundary:** State anchor ↔ Git object/ancestry graph ↔ every in-range subject.
- **Precision:** Anchor exclusion, descendant inclusion, ancestry check, and
  non-authentication wording are binding.
- **Proof intent:** Temporary Git DAGs plus Local verification against this
  repository’s `f110618..HEAD`.
- [ ] Commit at the anchor is excluded; every descendant reachable from target is
  inspected.
- [ ] Missing object, non-ancestor, invalid target, shallow/missing-history
  indication, and malformed in-range subject fail non-zero.
- [ ] Merge DAG descendants are neither omitted nor double-counted.
- [ ] Root/unborn behavior is explicit and fixture-tested; no arbitrary fallback
  anchor is selected.
- [ ] Audit accepts `642c647...` and all compliant later commits while leaving
  earlier `[master]:` history outside the verdict.
- [ ] Output does not claim the actual actor was authenticated.

Gate: Build temporary linear, branch/merge, root/unborn, missing/non-ancestor, and
violation DAGs; run current-repository audit from the exact anchor.

Evidence: N/A — audit is a structural Git claim, not intended-environment actor proof.

### AC-8: Contractual provenance and authority boundaries are explicit

Documentation and executable help consistently state what identity does and does not
prove.

- **Intent / authority:** RES D9, D55/D57, Honesty Over Convincingness.
- **Claim:** Identity is searchable declared commit context and is never represented
  as Git authorship, actor authentication, Proof Record, RF attestation, or REVIEW.
- **Boundary:** conventions ↔ glossary ↔ CLI help/errors ↔ later consumers.
- **Precision:** The six non-claims are acceptance-critical; prose layout is
  adaptable.
- **Proof intent:** Source/help semantic scan and contradiction scenarios.
- [ ] `--no-verify`, plumbing, direct Git, false/stale context, local audit bypass,
  and unsupported clients remain explicit limitations.
- [ ] No “verified actor,” “authenticated agent,” or equivalent claim exists.
- [ ] Git author/committer and `Co-authored-by` retain their separate meanings.
- [ ] Phase B/C responsibilities are named without being implemented.

Gate: Search every Phase A consumer and CLI help for required non-claims and banned
equivalents.

Evidence: N/A — this is an authority/semantic claim.

### AC-9: Generated examples and registries cannot drift  [depends: AC-1, AC-3]

Human-facing examples are executable contract fixtures, not manually maintained
parallel syntax.

- **Intent / authority:** Single Source of Truth, D28/D54.
- **Claim:** Every canonical example and registered field value in modified
  documentation resolves to schema-backed executable behavior.
- **Boundary:** JSON owner ↔ executable formatter ↔ conventions/glossary/tests.
- **Precision:** Example subjects and owner links are binding; narrative around them
  is adaptable.
- **Proof intent:** Example extraction/validation and registry-reference scan.
- [ ] All documented subjects validate through the executable.
- [ ] No prose table independently enumerates a conflicting registry.
- [ ] Adding a fixture-only surface changes accepted behavior only through fixture
  schema.
- [ ] Conventions/glossary owner links resolve in source and generated docs.

Gate: Extract bracketed C1-R examples from changed docs, validate them, and compare
registry mentions with schema data.

Evidence: Render generated conventions/glossary pages and verify links/examples.

### AC-10: Exact phase scope and reproducible quality  [depends: AC-1, AC-2, AC-3, AC-4, AC-5, AC-6, AC-7, AC-8, AC-9]

The six-file contract is complete, tested, rendered, and safe for Phase B consumption.

- **Intent / authority:** Phase HL scope/DoD and D57 claim-typed proof.
- **Claim:** All and only the six approved framework files change, the contract suite
  passes, and no Git hook/config/history/workflow/adapter behavior changes.
- **Boundary:** Framework diff ↔ tests ↔ generated docs ↔ protected Git state.
- **Precision:** Six framework paths, zero hook/config/history mutations, and exact
  test commands are binding.
- **Proof intent:** Local exact-write-set, tests, render, current-history audit, and
  protected-state comparison.
- [ ] `python -m pytest .tfw/scripts/test_commit_identity.py -q` passes.
- [ ] `python -m pytest docs/scripts/test_gen_docs.py docs/scripts/test_integration.py -q` passes.
- [ ] `python -m mkdocs build --config-file docs/mkdocs.yml` succeeds under the
  existing TD-125 warning baseline.
- [ ] `git diff --check`, JSON parse, owner-link/anchor, exact-write-set, and
  protected Git config/hook/history checks pass.
- [ ] Generated conventions/glossary pages are readable and free of changed-content
  overflow.
- [ ] RF reports the exact activation range and every in-range subject; no
  pre-anchor compliance claim appears.

Gate: Execute all named checks after EV/RF are complete and reproduce them from the
clean final tree.

Evidence: Record proof relations and rendered/current-repository observations in the
mandatory Phase A EV index.

### Evidence Artifacts

| File | Description |
|------|-------------|
| `evidence/EV__phase-a__canonical_contract_and_validator.md` | Stable Proof Records, structural observations, range result, limitations, and Value Debt |

No binary evidence is required unless rendered layout or a platform-specific failure
cannot be represented reproducibly in text.

## 6. Technical Guidance

- Prefer Python standard library only (`argparse`, `json`, `pathlib`, `re`,
  `subprocess`) so the contract can run before optional project dependencies exist.
- Keep registries and patterns in schema; Python may define code-level field names
  needed to bootstrap loading but must not duplicate accepted values.
- Use explicit CLI subcommands such as `format`, `validate-message`, `validate-state`,
  and `audit-range`; exact names may change if AC behavior remains stable.
- Expected context may be supplied as four explicit arguments or a single exact
  record; do not read branch names, Git author, changed paths, or session titles to
  invent missing identity.
- `task:none` may inspect staged path names but must not read file contents.
- Parse trailers through Git’s own `interpret-trailers` behavior where a temporary
  repository is available; do not reimplement every Git trailer rule.
- Range enumeration should use Git object/ancestry commands and explicit object IDs.
  Fail closed on missing history; never use “last N commits.”
- Treat C2-R as documentation-only fallback. Do not accept it in the version-1 parser.
- The current planning/research commits after `f110618` are part of the audit corpus.
  They were committed with command-local hook bypass solely to prevent the legacy
  `[master]:` mutator; Phase A must not change local Git config.

## 7. Definition of Failure

- ❌ Any Phase HL Definition of Failure occurs.
- ❌ JSON registries/patterns are duplicated as production constants in Python or
  another consumer.
- ❌ A malformed or stale identity is accepted because it resembles a valid prefix.
- ❌ A valid context is rejected only because work is non-code.
- ❌ `task:none` becomes a shortcut around task-scoped staged work.
- ❌ Autosquash/replay convenience is preserved by publishing stale operator identity.
- ❌ Optional origins/models/sessions become mandatory, authenticated, or acceptance
  metadata.
- ❌ Anchor/range failure silently passes, chooses a fallback, or rewrites history.
- ❌ Diagnostics expose arbitrary local content or sensitive material.
- ❌ Hook/config/workflow/adapter/global state changes in Phase A.
- ❌ Any named test, source/render check, exact-scope check, or independent review
  fails.

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Schema becomes too generic to validate precisely | Keep version 1 closed and explicit; extension requires versioned decision and tests. |
| Python dependency is unavailable during commit | Standard library only; Phase C proves executable lookup on supported clients. |
| Range audit is slow on large history | Enumerate exact range once, stream subjects, and measure descriptively; do not weaken completeness. |
| Revert subject parsing varies by Git locale/version | Limit accepted generated forms to proven English/default boundary or require explicit router; document unsupported variants. |
| Staged-path inspection leaks data | Inspect names only and keep them out of diagnostics. |
| Docs restate operational registries | Link to schema and validate examples rather than maintaining another list. |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `.tfw/conventions.md` | Phase B | Phase A owns semantics; Phase B adds point-of-action consumption without redefining fields. |
| `.tfw/commit_identity.schema.json` | Phase C/update events | Phase A owns version 1; later adapter registration is an atomic schema+consumer+fixture change. |
| `.tfw/commit_identity_state.json` | Phase C | Phase A records anchor/policy; Phase C records installation/runtime state without changing anchor history. |
| `.tfw/scripts/commit_identity.py` | Phase B/C | Phase B adds operation routing; Phase C thin hooks call the same parser/audit owner. |
| `.tfw/scripts/test_commit_identity.py` | Phase B/C | Later phases extend operation, hook, install, worktree, and rollback proof. |

> **Cross-references:** Master HL §§3–7 and §10; Iteration 1 RES D1–D9,
> Challenge C1–C9; D28, D54, D55, D57; Phase A HL §§2–7.

---

*TS — TFW-49 / Phase A: Canonical Commit Identity Contract and Validator | 2026-07-30*
