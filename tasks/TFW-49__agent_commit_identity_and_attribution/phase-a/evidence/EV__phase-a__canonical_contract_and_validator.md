# EV — TFW-49 / Phase A: Canonical Commit Identity Contract and Validator

> **Date**: 2026-07-30
> **Author**: Executor (Codex)
> **Task**: TFW-49
> **TS**: [TS Phase A](../TS__phase-a__canonical_contract_and_validator.md)

---

## Environment

| Field | Value |
|-------|-------|
| OS | Windows |
| Language / Runtime | Python 3.13.5; standard-library production runtime |
| Git | 2.42.0.windows.1 |
| Verification tools | pytest 9.0.2; MkDocs 1.6.1; Material-generated local site |
| CI / Pipeline | Local Executor verification on repository `master` |

## Proof Record Index

| Proof Record | Claim / AC | Boundary and proof class | Method or observation | Actual result | Artifact / provenance | Actor / time _(when material)_ | Debt |
|--------------|------------|--------------------------|-----------------------|---------------|-----------------------|--------------------------------|------|
| PR-1 | AC-1 — JSON is the single operational owner | Local; Seam: schema ↔ Python ↔ documentation | Parse the production schema; run field-removal, semantic-mutation, source-duplication, and fixture-behavior tests across every schema/state field consumed downstream | Versioned schema owns field order, exact registries, patterns, forms, trailers, examples, and the complete truth boundary. Missing or unusable owner fields fail during contract loading with stable field-specific shape diagnostics; `grammar.identity_template` must contain each required placeholder exactly once and round-trip the schema-owned diagnostic example through `ordinary_pattern`. Fixture-only registry/pattern mutation changes behavior; Python retains loader keys and diagnostic codes but no duplicate accepted registry/pattern constants | `.tfw/commit_identity.schema.json`; `.tfw/scripts/test_commit_identity.py`; contract test run `136 passed` (original 46 plus 90 corrective cases) | N/A — deterministic local relation | None |
| PR-2 | AC-2 — project state and prospective activation | Local; Seam: state ↔ schema version ↔ Git ancestry | `validate-state`; malformed/missing/mismatched/unknown/non-ancestor fixture matrix | State is valid with policy `agent-managed`, contract `1.0.0`, full exclusive anchor `f1106186417e84cdb38e797f7af66a60885bad76`, hook runtime false, and actor-authentication claim false; fail-closed fixture cases pass | `.tfw/commit_identity_state.json`; `python .tfw/scripts/commit_identity.py validate-state` → `{"status":"valid","contract_version":"1.0.0"}` | N/A — deterministic local relation | None |
| PR-3 | AC-3 — C1-R format, parse, normalize, and search keys | Local | Table-driven surface/role/work/task, legacy-entry normalization, round-trip, and invalid-character tests | Canonical output is exactly `[surface/task/work/role] summary`; all approved work classes round-trip; canonical validation rejects legacy output, ambiguity, unknown values, unsafe delimiters, and empty summary | `.tfw/scripts/commit_identity.py`; `.tfw/scripts/test_commit_identity.py` | N/A — deterministic local behavior | None |
| PR-4 | AC-4 — same-context reserved forms | Local | Public library/CLI matrix for `fixup!`, `squash!`, `amend!`, and generated revert nesting with absent context and every one-field stale context; independent range-audit structural-path fixtures | Every public/contextual reserved-form validation requires all four expected fields and returns secret-safe `E_EXPECTED_CONTEXT` when they are absent; exact context passes and any stale field returns `E_CONTEXT_MISMATCH`. Only the private range-audit parser admits structural-only reserved validation; no Git replay is implemented | `.tfw/scripts/test_commit_identity.py`; `_parse_subject_structural` and stable context diagnostics in `.tfw/scripts/commit_identity.py` | N/A — synthetic subject behavior | None |
| PR-5 | AC-5 — operator, guarded `task:none`, and attribution separation | Local; Seam: message/staged path ↔ Git trailer parser | Temporary repositories, staged task/non-task paths, repeated full origins, optional metadata, `Co-authored-by`, and operator/origin disagreement | `task:none` is limited to explicit non-task lifecycle work with no staged canonical task path; origins remain full independent records; optional metadata cannot replace core identity; Git authorship/co-authorship remains separate | `.tfw/scripts/test_commit_identity.py`; Git `interpret-trailers` exercised in temporary repositories | N/A — isolated Git seam | None |
| PR-6 | AC-6 — actionable secret-safe diagnostics | Local | Capture expected CLI/library failures containing body, path, hook-like, environment, and credential-shaped sentinels; scan all output | Failures return stable code/field/remediation without echoing arbitrary rejected content or configured paths; missing identity uses the schema-owned synthetic example; expected failures emit no traceback | `.tfw/scripts/test_commit_identity.py`; `.tfw/commit_identity.schema.json` diagnostic inputs | N/A — synthetic non-disclosure proof | None |
| PR-7 | AC-7 — exact fail-closed range audit | Local; Seam: state anchor ↔ Git object/ancestry graph | Temporary linear/merge/invalid/root/unborn/shallow graphs plus the current repository audit | Fixture DAG coverage, non-ancestor/missing/shallow/malformed failures, anchor exclusion, and no-double-count behavior pass through the explicit internal structural parser. Pre-corrective-commit target `929c489126f5fd78c8b606da98114867ceda1e67` has exactly five valid descendants: `642c647f91088e98c15f559c9553804433878fe6`, `d30d8deb84bd0946e3a8149b51a11c5e94515ee2`, `7740d83e6035b458a1e1f9bbbb4fd447cb4370d4`, `b83d8ee320f0dc54a3da901589f2026189ad33a9`, and `929c489126f5fd78c8b606da98114867ceda1e67`; output states `actor_authentication:false` | `python .tfw/scripts/commit_identity.py audit-range --repo .`; `.tfw/scripts/test_commit_identity.py` | Executor, 2026-07-30 | None |
| PR-8 | AC-8 — provenance and authority boundaries | Local; Seam: CLI ↔ conventions ↔ glossary | Semantic scan of six consumers and CLI help/description; contradiction/non-claim tests | Identity is consistently declared searchable operation context, not actual-actor authentication, Git authorship, Proof Record, Executor Attestation, Evidence status, or REVIEW acceptance. Bypasses and Phase B/C ownership are explicit | `.tfw/conventions.md#commit-identity-and-attribution`; `.tfw/glossary.md#commit-identity`; `.tfw/commit_identity.schema.json`; `.tfw/scripts/commit_identity.py` | N/A — source/consumer consistency | None |
| PR-9 | AC-9 — schema-backed examples and resolvable owners | Local; Seam: JSON owner ↔ formatter ↔ generated pages; Live: rendered documentation view | Extract and validate documented C1-R examples; registry/reference scan; docs tests; open generated conventions and glossary anchors in the in-app browser | Canonical example validates, no prose registry competes with JSON, three owner links per section resolve in generated HTML, headings/content are visible, the conventions table is readable, and neither page has changed-content horizontal overflow (`1265/1265` document width) | Generated `site/reference/conventions/#commit-identity-and-attribution` and `site/reference/glossary/#commit-identity`; `.tfw/scripts/test_commit_identity.py`; docs pair `68 passed` | Executor browser observation, 2026-07-30 | None |
| PR-10 | AC-10 — exact scope and reproducible quality | Local; Seam: framework diff ↔ tests/build ↔ protected Git state; Live: rendered documentation view | Exact status/diff set, JSON parse, compile, contract/docs tests, identical-input MkDocs baseline/final comparison, links/anchors, range audit, hooks/history checks, rendered browser QA | The phase still changes exactly six approved framework consumers, plus Executor EV/RF/README traces; the corrective patch changes only three of those consumers plus the same traces. No protected tracked file changes exist and `.tfw/hooks` remains absent. Contract tests pass `136` (46 original + 90 corrective); docs tests pass `68`; both isolated MkDocs builds exit zero. Using the same command, environment, warning filter, path normalization, and pinned source inputs yields `283/283` warning lines, `131/131` normalized distinct warnings, and `0 added / 0 removed`; TD-125 remains pre-existing. Final commit necessarily postdates this artifact's pre-commit range snapshot and is audited immediately after creation before push/STOP | Commands and results in RF §4; generated pages; `git status --short`; `git diff --check`; final post-commit audit reported to the Coordinator | Executor, 2026-07-30 | None |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | Intended-environment observation is not triggered for local data ownership; exhaustive field-removal/semantic-mutation loading checks and schema-consumption Seam Proof are PR-1 | Local contract fixtures | N/A | PR-1 |
| E2 | AC-2 | Intended-environment observation is not triggered for structural state/version/ancestry validation | Local repository and temporary Git fixtures | N/A | PR-2 |
| E3 | AC-3 | Intended-environment observation is not triggered for deterministic grammar behavior | Local parser/formatter matrix | N/A | PR-3 |
| E4 | AC-4 | Actual Git routing is explicitly Phase B; Phase A proves public context-required behavior, stale-context rejection, and the separate internal structural audit path only | Synthetic autosquash/revert inputs | N/A | PR-4 |
| E5 | AC-5 | No live identity provider or actor assertion is claimed; local staged-path and Git-trailer relations are sufficient for the Phase A claim | Temporary Git repositories | N/A | PR-5 |
| E6 | AC-6 | Diagnostic non-disclosure is a local output property; no live secret or external hook body was accessed | Synthetic sentinel capture | N/A | PR-6 |
| E7 | AC-7 | Structural Git graph/range proof does not authenticate an actor and therefore triggers no live actor evidence | Temporary graphs and current local repository | N/A | PR-7 |
| E8 | AC-8 | Authority/non-claim consistency is established through source/help comparison, not a live identity event | Six approved consumers | N/A | PR-8 |
| E9 | AC-9 | Completed generated conventions and glossary pages were opened at their exact anchors; headings, example/definition, owner links, table layout, and overflow were inspected | Material-generated site served locally and opened in the in-app browser | VERIFIED | PR-9; generated `site/reference/conventions/` and `site/reference/glossary/` |
| E10 | AC-10 | The rendered sub-boundary and current-repository state were observed after the approved implementation changes: both pages are readable, the exact pre-commit activation range is valid, and the permanent hook directory remains absent | Generated local docs and current repository | VERIFIED | PR-7, PR-10; inline browser and CLI output recorded above |

### Status Consequences

- `VERIFIED` scopes only the rendered/current-repository observations named in E9/E10.
- The structural contract claims remain supported by their Local/Seam Proof Records;
  Evidence status does not authenticate an actor or approve the phase.
- The final C1-R trace commit cannot be part of an artifact written before that commit.
  The Executor must run the same exact range audit after commit creation, report every
  resulting descendant to the Coordinator, then push and stop.

## Verdict

Evidence verdict: 2/10 VERIFIED, 0 DEFERRED, 0 BLOCKED, 8 N/A

## Value Debt

No Value Debt.

## Attachments

No binary attachments. Rendered-page observations are reproducible from the generated
site and recorded inline in PR-9/E9.

---

*EV — TFW-49 / Phase A: Canonical Commit Identity Contract and Validator | 2026-07-30*
