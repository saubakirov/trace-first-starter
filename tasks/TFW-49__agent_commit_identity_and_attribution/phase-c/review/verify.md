# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact.
> Mode: code
> Min verify ratio: 0.42
> RF framework files claimed: 29
> Files required at minimum: 13
> Files verified after discrepancy escalation: 29/29 (100%)

## Verification Log

### V1 — Contract, state, template, and exact ranges

- **Files:** `.tfw/commit_identity.schema.json`,
  `.tfw/commit_identity_state.json`,
  `.tfw/templates/commit_identity_state.json`,
  `.tfw/scripts/commit_identity.py`
- **RF claim:** exact `1.1.0`; current exclusive anchor; clean null/root-inclusive
  template; no tracked installed truth; exact DAG enumeration.
- **Actual:** Owner fields and pairings are exact. The current audit excludes
  `f110618...`, includes all 21 descendants through `ad88c21...`, returns the complete
  object list, and keeps `actor_authentication:false`. Temporary one-root,
  multi-root-merge, missing-target, unborn, shallow, and non-ancestor cases pass/fail
  as specified.
- **Match:** ✅

### V2 — Runtime manifest, hook inventory, and lifecycle

- **Files:** `.tfw/hooks/runtime.json`, `.tfw/hooks/prepare-commit-msg`,
  `.tfw/hooks/commit-msg`, `.tfw/scripts/commit_identity_hooks.py`
- **RF claim:** the exact recognized runtime rejects every unexpected
  reserved-target/manifest mutation; lifecycle operations are idempotent and preserve
  exact opaque prior local state.
- **Actual:** Current tracked inventory and LF-normalized hashes are exact, both hook
  entries are `100755`, and ordinary known lifecycle cases pass. Two required
  fail-closed/idempotence edges do not:
  1. a valid manifest and both valid owned targets plus an extra unknown file is
     accepted by `install` and `verify`;
  2. non-empty mutation of a target `entrypoint`, and an unexpected top-level
     manifest field, are also accepted as recognized;
  3. when the exact prior local value is already `.tfw/hooks`, install and first
     rollback succeed, but the second rollback returns
     `E_RUNTIME_LEDGER_REQUIRED` instead of a stable idempotent disposition.
- **Match:** ❌ — D1/D2

### V3 — Router, carrier, and hook-stage context

- **Files:** `.tfw/scripts/commit_identity_router.py`,
  `.tfw/scripts/commit_identity_hooks.py`
- **RF claim:** Phase A remains the semantic owner; Phase B remains the operation
  owner; the carrier validates the plan, transports complete context only to the Git
  child, and permits no publication command.
- **Actual:** Exact 11-workflow mapping, four surfaces/four roles, guarded
  `task:none`, staged-task relation, forged-plan rejection, and seven operation
  dispositions pass. The carrier invokes only local `git commit`/`--amend`, validates
  the current staged set, and returns both authority non-claims as false.
- **Match:** ✅

### V4 — Prepare/final behavior and diagnostics

- **Files:** `.tfw/hooks/prepare-commit-msg`, `.tfw/hooks/commit-msg`,
  `.tfw/scripts/commit_identity_hooks.py`
- **RF claim:** prepare/final are non-mutating; exact context passes; partial,
  malformed, and stale context fails; absent context is visibly structural-only;
  diagnostics disclose no arbitrary input, path, environment, credential, or private
  config value.
- **Actual:** Byte-preservation, complete/partial/malformed/absent/stale matrices,
  real Windows/WSL hook launches, reserved/trailer rules, and redaction canaries pass.
  Source/command scans contain no production `--global`, `--show-origin`, remote
  executor, external-hook discovery, or arbitrary operation path.
- **Match:** ✅

### V5 — Init/update/handoff/review/release workflow owners

- **Files:** `.tfw/workflows/init.md`, `.tfw/workflows/update.md`,
  `.tfw/workflows/handoff.md`, `.tfw/workflows/review.md`,
  `.tfw/workflows/release.md`
- **RF claim:** init derives destination state; update preserves it and uses
  ownership-gated repair; action workflows use the carrier/full range and preserve
  F26.
- **Actual:** Required lifecycle commands, state-preservation language, pre/post
  exact-audit gates, Reviewer independence, and separate publication authority are
  present. Handoff/release explicitly retain process F26 and `APPROVE PUSH`.
- **Match:** ✅ for workflow text; lifecycle acceptance remains blocked by V2.

### V6 — Canonical/derived parity

- **Files:** the five `.agent/workflows/tfw-*.md` and five
  `.claude/commands/tfw-*.md` Phase C consumers.
- **RF claim:** each is byte-exact to its canonical owner.
- **Actual:** SHA-256 comparison is 10/10 exact.
- **Match:** ✅

### V7 — Conventions and glossary

- **Files:** `.tfw/conventions.md`, `.tfw/glossary.md`
- **RF claim:** exact state/runtime/ledger/context/range/client/non-claim semantics are
  documented without claiming authentication or completion from presence.
- **Actual:** Root-inclusive/exclusive semantics, Git-common-dir ledger,
  `TFW_COMMIT_EXPECTED_CONTEXT`, structural-only limitation, live Codex boundary,
  known bypasses, and publication/authentication non-claims are present and rendered.
- **Match:** ✅

### V8 — Test sources and claimed matrices

- **Files:** `.tfw/scripts/test_commit_identity.py`,
  `.tfw/scripts/test_commit_identity_router.py`,
  `.tfw/scripts/test_commit_identity_hooks.py`
- **RF claim:** 155 + 149 + 41 = 345 tests cover the complete required matrix.
- **Actual:** Counts and passing result reproduce exactly. The suite covers the stated
  DAG, WSL, 4×4, seven-operation, linked-worktree, context, redaction, and normal
  lifecycle families, but omits the unexpected-entry/closed-manifest cases and the
  canonical-prior rollback/rollback case that independently fail.
- **Match:** ⚠️ partial — pass count true; completeness claim false.

### V9 — Exact scope and descriptive measurements

- **RF claim:** 29/29 framework paths; 6 create, 23 modify; `+2768/-134=2902`;
  physical LOC `7310→9944`; category totals exact; no protected spill.
- **Actual:** All counts reproduce byte-for-byte from `1123213..ad88c21`; production
  1227, tests 990, docs/workflows 618, data 67. No 30th framework path and no protected
  config, knowledge, adapter, Phase A/B, or later-scope path changed.
- **Match:** ✅

### V10 — Documentation generation and render

- **RF claim:** 68 docs tests; identical pinned MkDocs comparison
  `317/317`, `157/157`, `+0/-0`; 10/10 affected rendered pages.
- **Actual:** `68 passed`. Clean baseline/final archives built with the same
  environment and command both exit 0. Counting all lines beginning `WARNING` gives
  exactly `317/317`, `157/157`, `+0/-0`. Ten affected pages contain their key
  anchors/text, valid UTF-8, and zero broken local hrefs.
- **Match:** ✅

## Commands Executed

| # | Command / method | Result |
|---|------------------|--------|
| 1 | `python -m pytest -q` over three Commit Identity suites | `345 passed in 34.33s` |
| 2 | Per-file `pytest --collect-only` | 155 / 149 / 41 |
| 3 | `python -m pytest -q docs/scripts/test_gen_docs.py docs/scripts/test_integration.py` | `68 passed in 28.10s` |
| 4 | `python -m py_compile` for six production/test modules | pass |
| 5 | lifecycle `verify --repo .` | valid `1.1.0`, relative-owned, private ledger present, authority false |
| 6 | state-owned `audit-range --repo .` | valid, exclusive anchor, 21 exact descendants through `ad88c21...`, auth false |
| 7 | Windows/Ubuntu version commands | Git 2.42.0/Python 3.13.5; Git 2.43.0/Python 3.12.3 |
| 8 | isolated baseline/final MkDocs builds | exit 0/0; 317/317; 157/157; +0/−0 |
| 9 | rendered HTML page/anchor/link scan | 10/10; zero replacement characters/broken local hrefs |
| 10 | canonical/derived SHA-256 comparison | 10/10 exact |
| 11 | exact diff/LOC/numstat script | all RF measurements reproduced |
| 12 | unexpected reserved-target fixture | defect: install/verify accepted the unknown extra file |
| 13 | manifest mutation fixtures | defect: non-empty entrypoint and unexpected top-level key accepted |
| 14 | prior `.tfw/hooks` lifecycle fixture | defect: second rollback exited 2 with `E_RUNTIME_LEDGER_REQUIRED` |
| 15 | `git diff --check`, protected diff, hook modes, clean/status/origin checks | clean; exact scope; origin `b4c0a06...` |

## Discrepancies Found

### D1 — Runtime recognition is not closed over its approved manifest/inventory

AC-3 requires the recognized directory to contain exactly `runtime.json`,
`prepare-commit-msg`, and `commit-msg`, and requires unexpected reserved-target
material or manifest mutation to block install/verify/repair. The implementation
validates only the two named target bytes and selected manifest fields. It accepts:

- an extra unknown file beside the approved three files;
- a non-empty arbitrary `targets[*].entrypoint`;
- an unexpected top-level manifest field.

This triggers AC-3, AC-10, and DoF 5. PR-C3/PR-C10 and E3/E10 therefore overstate the
matrix.

### D2 — Rollback/rollback is not idempotent for an allowed exact prior value

With a synthetic repository whose pre-install local `core.hooksPath` is already the
exact opaque value `.tfw/hooks`, install records that prior value and the first
rollback restores it exactly. The second rollback cannot distinguish the restored
prior value from an orphaned owned override and fails with
`E_RUNTIME_LEDGER_REQUIRED`. This contradicts AC-4's unqualified stable
rollback/rollback disposition requirement. PR-C4/E4 overstate lifecycle completeness.

Any discrepancy requires 100% verification; all 29 framework paths were consequently
checked.

## Acceptance Criteria Verification

| AC | Result | Independent basis |
|----|--------|-------------------|
| AC-1 | ✅ PASS | exact owners/template/state tests and source inspection |
| AC-2 | ✅ PASS | exact current audit and temporary topology suite |
| AC-3 | ❌ FAIL | D1 fail-open manifest/inventory recognition |
| AC-4 | ❌ FAIL | D2 rollback idempotence; D1 also affects lifecycle recognition |
| AC-5 | ✅ PASS | router/carrier/child-only/allowlist reproduction |
| AC-6 | ✅ PASS | seven operations, context matrix, non-mutation, diagnostics |
| AC-7 | ✅ PASS | init/update semantics and state preservation |
| AC-8 | ✅ PASS | workflow authority/range/F26 gates |
| AC-9 | ✅ PASS | 29-path scope and 10/10 parity |
| AC-10 | ❌ FAIL | claimed complete security/lifecycle matrix misses D1/D2 |
| AC-11 | ❌ FAIL pending correction | Reviewer live operation can close VD-C1, but AC-11 depends on failed AC-3/4/10 |
| AC-12 | ❌ FAIL | regression/evidence package overclaims D1/D2 coverage and depends on AC-11 |

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|-----------------|-----------------|----------------|
| E1 | AC-1 N/A | ✅ | ✅ claim-based N/A is justified; Local/Seam proof reproduced |
| E2 | AC-2 N/A | ✅ | ✅ claim-based N/A is justified; DAG/current audit reproduced |
| E3 | AC-3 VERIFIED | ✅ | ❌ D1 falsifies complete recognized-runtime observation |
| E4 | AC-4 VERIFIED | ✅ | ❌ D1/D2 falsify complete lifecycle/idempotence claim |
| E5 | AC-5 N/A | ✅ | ✅ transport is Local/Seam; real commit belongs to E11 |
| E6 | AC-6 VERIFIED | ✅ | ✅ actual Windows/WSL hook behavior reproduced |
| E7 | AC-7 N/A | ✅ | ✅ init/update are Local/Seam; no separate live row required |
| E8 | AC-8 N/A | ✅ | ✅ release publication is forbidden; Reviewer use belongs to E11 |
| E9 | AC-9 N/A | ✅ | ✅ parity is structural, not a live non-Codex claim |
| E10 | AC-10 VERIFIED | ✅ | ❌ platform versions are true, but the claimed complete matrix misses D1/D2 |
| E11 | AC-11 DEFERRED | ✅ | ✅ honest pre-review status; Reviewer commit/audit is owned after trace creation |
| E12 | AC-12 N/A | ✅ | ⚠️ N/A aggregation reason is valid, but PR-C12 cannot pass with D1/D2 |

Evidence artifact exists and all PR-C1–PR-C12 relations resolve. Status wording does
not claim authentication, non-Codex live clients, or publication, but PR-C3/4/10/12
must be corrected after implementation fixes.

## Knowledge Citations Verified

All 28 Phase HL §7.2 citations and their ONB §7 applications resolve:

- 6/6 `.tfw/README.md` philosophy anchors;
- 6/6 knowledge facts (philosophy F4/F13/F23, process F3/F4/F26);
- 6/6 decisions D28/D54/D55/D57/D58/D59;
- 5/5 convention anchors;
- 5/5 Phase A/B RF/REVIEW and Iteration 1 RES sources.

Total citations: 28; verified: 28; hallucinations: 0.

## Checkpoint

**Self-check:**
- [x] Opened and verified 29/29 changed framework files after escalation
- [x] Ran code, docs, platform, render, parity, scope, lifecycle, and range checks
- [x] Verified every RF §3 checkmark against actual sources and outputs
- [x] Checked KNOWLEDGE.md and topic facts for contradictions
- [x] Verified 28/28 HL/ONB knowledge citations
- [x] Verified/challenged all 12 EV rows and PR-C1–PR-C12

Stage complete: YES
