# ONB — TFW-49 / Phase A: Canonical Commit Identity Contract and Validator

> **Date**: 2026-07-30
> **Author**: Executor (Codex)
> **Status**: 🟠 ONB — Awaiting Coordinator approval
> **Parent HL**: [Phase A HL](HL__phase-a__canonical_contract_and_validator.md)
> **TS**: [Phase A TS](TS__phase-a__canonical_contract_and_validator.md)
> **Master HL**: [TFW-49](../HL-TFW-49__agent_commit_identity_and_attribution.md)
> **Research**: [Iteration 1 RES](../research/iter1/RES.md)

---

## 1. Understanding

Phase A must create the single versioned data and executable owner for the approved
C1-R commit identity, `[surface/task/work/role] summary`, without adding a Git
entrypoint, hook, workflow, adapter, installation path, or authentication claim. The
universal JSON schema owns production registries, patterns, field order, reserved
forms, trailers, and synthetic diagnostic inputs; separate project state owns the
`agent-managed` policy, matching contract version, and full activation anchor. A
standard-library Python CLI consumes both records to format, parse, validate, compare
expected context, validate state/schema relations, and audit the exact prospective
Git range.

The ten approved Requirement Claims bind:

1. single JSON ownership without a duplicate Python registry or pattern set;
2. separate project state with exact anchor
   `f1106186417e84cdb38e797f7af66a60885bad76`;
3. strict C1-R normalization, formatting, parsing, and independent search keys;
4. exact same-context-only reserved forms and stale-context rejection;
5. operator semantics, guarded `task:none`, complete repeatable content-origin
   records, and separate optional co-author/model/session/source metadata;
6. stable actionable diagnostics that do not disclose arbitrary message, path, hook,
   credential-like, or environment content;
7. an exact fail-closed `anchor..target` audit that excludes the anchor and all prior
   history while inspecting every descendant;
8. explicit contractual-provenance and non-authentication boundaries;
9. schema-backed examples and owner links that cannot drift into a second grammar;
10. exactly six framework consumers, reproducible tests/render/range proof, and zero
    hook, Git-config, history, workflow, adapter, or global-state mutation.

C2-R remains a documented fallback only and is not accepted by version 1. Technical
Guidance on CLI subcommand names, internal JSON nesting, argument packaging, and
specific standard-library modules is adaptable only while all claim boundaries and
proof obligations above remain intact. Phase A stops after Executor-owned EV/RF;
independent REVIEW, Phase B consumption, and Phase C hook installation are separate
authority boundaries.

## 2. Entry Points

### Exact Planned Write Scope

Phase 1 is limited to this ONB and the TFW-49 Task Board trace in
[`README.md`](../../../README.md). No approved implementation consumer is touched
before Coordinator approval.

After approval, Phase 2 may change all and only these six framework consumers:

| File | Planned action | Authority |
|------|----------------|-----------|
| `.tfw/commit_identity.schema.json` | CREATE | Universal C1-R registries, patterns, forms, trailers, version |
| `.tfw/commit_identity_state.json` | CREATE | Project policy, matching version, full activation anchor |
| `.tfw/scripts/commit_identity.py` | CREATE | Standard-library contract CLI and range auditor |
| `.tfw/scripts/test_commit_identity.py` | CREATE | Contract, mutation, diagnostic, and temporary-Git suite |
| `.tfw/conventions.md` | MODIFY | Canonical human contract and truth/range boundaries |
| `.tfw/glossary.md` | MODIFY | Concise Commit Identity definition and owner links |

Executor lifecycle traces after approval are limited to
`evidence/EV__phase-a__canonical_contract_and_validator.md`,
`RF__phase-a__canonical_contract_and_validator.md`, and the TFW-49 Task Board row.
HL, TS, RES, Challenge, REVIEW, workflows, adapters, root instructions, skills,
hooks, Git configuration, history, init/update, docs/knowledge, global state, and
credential remediation are protected.

### Specification-to-Reality Check

| Check | Approved claim/source | Actual project/source | Proof or product-cohesion effect | Disposition |
|-------|-----------------------|-----------------------|----------------------------------|-------------|
| Required identifiers and paths | Six exact paths in TS §4 | Both documentation consumers exist; four CREATE paths and the parent `.tfw/scripts/` directory do not yet exist | This is the expected Phase A creation boundary, not an identifier mismatch | Match |
| Canonical grammar and owner | C1-R only; C2-R fallback; JSON owns accepted production values | Neither `.tfw/conventions.md` nor `.tfw/glossary.md` currently defines Commit Identity, and no competing runtime/schema exists | Phase A can establish one owner without migrating an existing consumer | Match |
| Activation range | Full anchor is last pre-policy commit; every descendant is audited | The anchor resolves as a commit and is an ancestor of `HEAD`; the current range contains `642c647...` and `d30d8de...`, both with C1-R subjects | Exact current-repository proof is feasible without judging pre-anchor history | Match |
| Cited systems or authorities | Phase HL §7.1, Master HL §7.2, RES D1–D9, Challenge C1–C9 | All 22 Phase/Master citation targets and named headings/decision records resolve; Challenge exposes C1–C9 | Source fidelity and later documentation Seam Proof are reproducible | Match |
| Required tests/checks | Contract pytest, 68-test docs pair, MkDocs render, JSON/link/scope/range/protected-state checks | Git 2.42.0.windows.1, Python 3.13.5, pytest 9.0.2, and MkDocs 1.6.1 are available; baseline docs pair is `68 passed in 47.27s`; contract test file is correctly absent until implementation | All named local proof routes are available; contract suite becomes runnable only after its approved CREATE action | Match |
| Diagnostics boundary | Stable code/field/remediation; no arbitrary message/path/hook/credential/environment disclosure | No existing diagnostic implementation or external-hook inspection is needed; fixture capture can use synthetic sentinels | Proof can be isolated in temporary data/repositories without accessing excluded hook bodies | Feasible |
| Outcome and live boundary | Searchable structural provenance, not authenticated actor identity | Local formatter/parser/audit and generated-page inspection can establish structural and documentation claims; no trusted identity provider is in scope | Live actor proof is not triggered; EV must keep the non-authentication limitation explicit | Feasible |
| Scope and product cohesion | Six framework files, four new/two modified, estimated 650–1,000 changed lines | Configured attention signals remain exactly 14 files, 8 new, 1,200 LOC, and 12 modified; schema, state, executable, tests, and two human consumers form one contract boundary | No split or override is indicated; lifecycle traces remain outside the six-file framework set | Coherent |
| Phase C runtime boundary | No hook/config installation in Phase A | `.tfw/hooks` does not exist, as expected before Phase C | Phase A commits must use the authorized command-local nonexistent path; no permanent runtime or config mutation is introduced | Match |

## 3. Questions (blocking — cannot proceed without answers)

No specification-to-reality mismatch requires a new design decision. There are no
blocking implementation questions.

The mandatory workflow gate still applies: Phase 2 may begin only after the
Coordinator explicitly returns **APPROVE** or **REVISE** for this ONB. The Executor
will direct that decision to Coordinator task
`019fa70f-8db9-70a3-8109-c69ff35c9592`, not to the user.

## 4. Recommendations (suggestions, not blocking)

1. Load field order, accepted surface/role/work values, task/work patterns, reserved
   markers, trailer names, and synthetic-example inputs from the schema for every
   operation. Python may own loader field names and error codes, but no accepted
   production registry or grammar pattern.
2. Allow test-only schema/state paths at the CLI/library boundary so mutation fixtures
   prove consumption rather than copying the production JSON into Python tests.
3. Keep expected-context comparison explicit in all four fields. A structurally valid
   reserved or nested form should return an unresolved mismatch when expected context
   is absent or stale, never infer context from branch, author, message prose, or
   session title.
4. Build all diagnostics from stable codes, field/rule labels, and schema-backed
   synthetic examples. Record only counts/object IDs where needed for audit; never
   include rejected arbitrary input values or configured paths in errors.
5. Enumerate the explicit `anchor..target` graph with Git object/ancestry primitives,
   fail closed on missing or shallow history, and report every violating object
   without selecting a fallback range.
6. Derive registry-wide positive/negative matrices from fixture JSON and use temporary
   Git repositories for staged-path, trailer, DAG, root/unborn, and non-ancestor
   cases. The production repository remains read-only except for authorized commits.

## 5. Risks Found (edge cases, potential issues not in TS)

1. A convenient Python constant for a work class, role, marker, or diagnostic example
   could quietly become a second production registry. AC-1/AC-9 need both source scan
   and fixture mutation proof.
2. Reserved-form parsing can accept a valid nested identity while losing the exact
   four-field expected-context relation. AC-4 must test every one-field mismatch, not
   structure alone.
3. `task:none` staged-path checks can leak a sensitive path through otherwise useful
   diagnostics. AC-5/AC-6 must prove the check observes names without echoing them.
4. Trailer handling can accidentally treat a message body as safe structured input.
   Tests must use Git parsing where applicable and scan all captured output for body,
   newline, control, credential-like, and environment sentinels.
5. Range enumeration can omit merged descendants, double-count a DAG, or confuse
   missing objects with an empty valid range. AC-7 requires explicit topology
   fixtures and fail-closed codes.
6. The audit corpus grows with every Phase A commit. Each new commit must use the
   exact C1-R context immediately and the final RF must enumerate the then-current
   full range rather than reuse this ONB snapshot.
7. Documentation links to data/executable owners may resolve in source but fail after
   MkDocs generation. AC-9/AC-10 require rendered link and readability inspection.
8. Pytest and MkDocs are verification dependencies, but the production CLI must
   remain Python-standard-library-only. Imports need a runtime dependency scan.

## 6. Inconsistencies with Code (spec vs reality)

No blocking contradiction was found. The current differences are the intended Phase A
implementation gaps:

1. `.tfw/commit_identity.schema.json` and
   `.tfw/commit_identity_state.json` are absent, so no universal or project data owner
   exists yet.
2. `.tfw/scripts/commit_identity.py`,
   `.tfw/scripts/test_commit_identity.py`, and their parent directory are absent, so
   no executable contract, diagnostic surface, or contract suite exists yet.
3. `.tfw/conventions.md` and `.tfw/glossary.md` contain no Commit Identity contract or
   competing registry; Phase A must add owner references without restating accepted
   values as an independent data source.
4. `.tfw/hooks` is absent and no Phase A hook consumer is planned. This matches the
   protected Phase C installation boundary.
5. The current `anchor..HEAD` corpus has two descendants and both already use C1-R.
   This is a proof-feasibility snapshot, not the final range claim.

## 7. Knowledge Citations

### Phase HL §7.1

| # | Phase HL ref | Read? | Applied / N/A | Notes |
|---|--------------|-------|---------------|-------|
| 1 | Master HL — C1-R and activation contract | ✅ | Bound grammar, operator meaning, prospective range, and non-claims | Full Master HL read |
| 2 | Iteration 1 RES — D1–D9 | ✅ | Preserved the challenged grammar, same-context rule, guarded `none`, complete origin, range, and non-authentication boundary | Full RES read |
| 3 | D28 | ✅ | Treat field names and stable error vocabulary as behavior-shaping contract elements | Resolved in `KNOWLEDGE.md` |
| 4 | D54 | ✅ | Keep later adapters thin and out of Phase A; do not create a parallel consumer | Resolved in `KNOWLEDGE.md` |
| 5 | D55 | ✅ | Preserve role authority and observable enforcement while separating operator context from proof | Resolved in `KNOWLEDGE.md` |
| 6 | D57 | ✅ | Keep identity distinct from Proof Records, Executor Attestation, Evidence status, and REVIEW | Resolved in `KNOWLEDGE.md` |
| 7 | Honesty Over Convincingness | ✅ | Reject unknown/stale context and state limitations rather than fabricate provenance | Heading resolves in `.tfw/README.md` |
| 8 | Single Source of Truth | ✅ | JSON owns accepted production values; other consumers reference or consume it | Heading resolves in `.tfw/README.md` |
| 9 | Role Lock Protocol | ✅ | `role` means the workflow role actually operating the commit | Heading resolves in `.tfw/conventions.md` |
| 10 | Research Challenge C1–C8 | ✅ | Carried the replay, autosquash, registry, origin, population, migration, hook-visibility, and grammar repairs into the risk/proof plan | All C1–C8 headings resolve |

### Master HL §7.2

| # | Master HL ref | Read? | Applied / N/A | Notes |
|---|---------------|-------|---------------|-------|
| 1 | Traces Over Code | ✅ | Connect commit history to task/work/role traces | Heading resolves |
| 2 | Honesty Over Convincingness | ✅ | No inferred identity or authentication overclaim | Heading resolves |
| 3 | Structural Enforcement | ✅ | Formatter/validator/audit provide observable structural gates | Heading resolves |
| 4 | Naming Creates Behavior | ✅ | Fixed positional meanings and field-specific diagnostics | Heading resolves |
| 5 | Single Source of Truth | ✅ | One JSON-backed operational owner | Heading resolves |
| 6 | Portability | ✅ | Standard-library, relative-path, cross-platform contract boundary | Heading resolves |
| 7 | D28 | ✅ | Precise names reduce drift | Decision row resolves |
| 8 | D54 | ✅ | Adapter parity remains a later thin-consumer concern | Decision row resolves |
| 9 | D55 | ✅ | Role/provenance stays inside Method Kernel authority boundaries | Decision row resolves |
| 10 | D57 | ✅ | Identity cannot substitute for proof or acceptance | Decision row resolves |
| 11 | Role Lock Protocol | ✅ | Subject role is the active commit operator role | Heading resolves |
| 12 | Session Naming | ✅ | Session identity is related context, not a source from which commit identity may be invented | Heading resolves in `.tfw/glossary.md` |

**Citation audit:** 22/22 Phase/Master targets resolved to the named file,
heading, decision record, or Challenge section. No new applicable Project Value item
was found that changes the approved contract or scope.

---

*ONB — TFW-49 / Phase A: Canonical Commit Identity Contract and Validator | 2026-07-30*
