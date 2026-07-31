# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Mode: code
> Min verify ratio: 0.42
> RF files claimed: 32 changed paths (28 framework consumers + ONB/EV/RF/README traces)
> Files to verify: ⌈32 × 0.42⌉ = 14; dispatch-required coverage: 32/32 (100%)

## Verification Log

### V1: Production router and test owner

- **RF claim:** one standard-library router consumes the Phase A contract and plans
  the exact workflow/operation boundary; one isolated suite covers it.
- **Actual:** `.tfw/scripts/commit_identity_router.py` is 719 physical lines and
  imports the unchanged `commit_identity` module. It owns only workflow policy,
  operation dispositions, and safe CLI presentation. It imports no subprocess/Git
  executor, contains no copied ordinary/origin regex, and returns
  `publication_authority:false`, state-owned hook/authentication values, and the
  schema-owned truth-boundary claim.
- **Actual tests:** `.tfw/scripts/test_commit_identity_router.py` is 1,066 lines,
  collects 149 passing cases, and gives the production router 92% branch-aware
  coverage. It covers the 11×4 map, schema-owner mutations, guarded `task:none`,
  every four-field mismatch, all seven same-context operations, five
  context-sensitive cross-context branches, trailers, CLI redaction, action
  locality, adapter surfaces, copy parity, protected owners, and non-publication.
- **Match:** ✅

### V2: Exact 28-path framework consumer inventory

Every path was opened as bytes/text, hashed, and compared to the
`95f95c730e4365606cb5b1aafc796cdf1fd6ae21..350b56d62765938bd80749457c6dd6aaa17a8e2e`
diff. The actual framework set is exactly the allowlist below: 2 added, 26 modified,
0 missing, 0 extra.

| # | Status | Path | Actual |
|---:|:------:|------|--------|
| 1 | A | `.tfw/scripts/commit_identity_router.py` | 719-line router; full source opened |
| 2 | A | `.tfw/scripts/test_commit_identity_router.py` | 1,066-line suite; tests and coverage reproduced |
| 3 | M | `.tfw/workflows/docs.md` | `docs/coordinator`, task split, F26 publication stop at action point |
| 4 | M | `.tfw/workflows/handoff.md` | routed local ONB/completion commits; former commit/push coupling absent |
| 5 | M | `.tfw/workflows/release.md` | explicit task/guarded `none`, `release/coordinator`, separate local/remote actions |
| 6 | M | `.tfw/adapters/antigravity/tfw-rules.md.template` | exact `antigravity` surface only |
| 7 | M | `.tfw/adapters/claude-code/CLAUDE.md.template` | exact `claude-code` surface only |
| 8 | M | `.tfw/adapters/codex/AGENTS.md.template` | exact `codex` surface only |
| 9 | M | `.tfw/adapters/cursor/tfw.mdc.template` | exact `cursor` surface only; no live install |
| 10 | M | `.agent/rules/tfw.md` | thin Antigravity entry block; unrelated rules preserved |
| 11 | M | `CLAUDE.md` | thin Claude entry block; unrelated project instructions preserved |
| 12 | M | `AGENTS.md` | only the managed Codex block changed |
| 13 | M | `.agent/workflows/tfw-docs.md` | byte-exact canonical copy |
| 14 | M | `.agent/workflows/tfw-handoff.md` | byte-exact canonical copy |
| 15 | M | `.agent/workflows/tfw-init.md` | byte-exact canonical copy; no hook lifecycle |
| 16 | M | `.agent/workflows/tfw-knowledge.md` | byte-exact canonical copy |
| 17 | M | `.agent/workflows/tfw-plan.md` | byte-exact canonical copy |
| 18 | M | `.agent/workflows/tfw-release.md` | byte-exact canonical copy |
| 19 | M | `.agent/workflows/tfw-research.md` | byte-exact canonical copy |
| 20 | M | `.agent/workflows/tfw-update.md` | byte-exact canonical copy; no hook repair |
| 21 | M | `.claude/commands/tfw-docs.md` | byte-exact canonical copy |
| 22 | M | `.claude/commands/tfw-handoff.md` | byte-exact canonical copy |
| 23 | M | `.claude/commands/tfw-init.md` | byte-exact canonical copy; no hook lifecycle |
| 24 | M | `.claude/commands/tfw-knowledge.md` | byte-exact canonical copy |
| 25 | M | `.claude/commands/tfw-plan.md` | byte-exact canonical copy |
| 26 | M | `.claude/commands/tfw-release.md` | byte-exact canonical copy |
| 27 | M | `.claude/commands/tfw-research.md` | byte-exact canonical copy |
| 28 | M | `.claude/commands/tfw-update.md` | byte-exact canonical copy; no hook repair |

- **Match:** ✅

### V3: Workflow map and operation semantics

- `describe_workflows` independently returns the exact ordered 11-command set and
  schema-derived roles: coordinator for plan/resume/docs/knowledge/release/update/
  config/init, researcher for research, executor for handoff, reviewer for review.
- All four schema-registered surfaces resolve through the same map.
- Independent probes confirmed:
  - ordinary/merge generate current-context subjects;
  - amend re-identifies every changed field and classifies exact equality separately;
  - cross-context fixup/squash fail `E_ROUTER_AUTOSQUASH_CONTEXT`;
  - cross-context revert/cherry-pick return `--no-commit`, inspection, and a new
    current-reviewer subject;
  - optional source/origin data uses only schema-owned trailer names and validators;
  - unknown workflow/role/operation fails closed.
- A separate temporary repository with a staged canonical TFW-49 path rejected
  guarded `task:none` with `E_TASK_NONE_STAGED`; the diagnostic disclosed neither the
  repository path nor a traceback.
- **Match:** ✅

### V4: Action-cue locality, adapters, and parity

- Only `handoff`, `docs`, and `release` contain
  `commit_identity_router.py`; plan, research, review, resume, knowledge, update,
  config, and init contain no invented Git action. Update's clone remains an
  auxiliary fetch.
- Each of the four canonical templates and three installed entry consumers declares
  exactly one registered surface and no adapter-local task/work/role assignment.
- Antigravity workflow copies: 11/11 byte-exact.
- Claude workflow copies: 11/11 byte-exact.
- Codex skill pairs: 11/11 byte-exact and complete.
- Root Codex marker count is one start/one end and its managed block equals the
  template. Cursor live path is absent; both legacy `tfw-task.md` files are present
  and unchanged.
- **Match:** ✅

### V5: Protected Phase A, Phase C, publication, and history boundaries

- Zero baseline-to-target changes in the Phase A schema, state, CLI, and Phase A test
  owner; zero changes in project config/template and both legacy workflow copies.
- State remains full-anchor/exclusive-range, `hook_runtime.installed:false`, and
  `actor_authentication:false`.
- `.tfw/hooks`, `.cursor/rules/tfw.mdc`, and a Phase C output directory are absent.
- Router source contains no Git executor, hook installer, Git-config writer, history
  migration, network publication, or actor-authentication implementation.
- Local `core.hooksPath` is unset. `.git/config` was hashed without exposing any hook
  target. Per dispatch, no external/global hook path or body was read, printed,
  executed, or copied; the RF's earlier non-reversible global comparison is therefore
  not independently repeated.
- `origin/master` remains exactly
  `b4c0a06dc9fbc104c5b8997865b6df3211bd5c0c`; pre-review local state is ahead 7,
  behind 0. No network or remote operation was run.
- **Match:** ✅ for every independently observable boundary; ⚠️ global-hook
  before/after comparison intentionally not repeated under the explicit safety lock.

### V6: Regression, warnings, rendered structure, and links

- Combined Phase A + Phase B suites: `285 passed`.
- Existing docs suites: `68 passed`.
- Identical-input isolated MkDocs builds at planning baseline and implementation
  target both exit 0. Each emits 294 retained warning records and 139 normalized
  distinct records; set comparison is 0 added / 0 removed.
- Generated handoff/docs/release HTML contains the exact router cue and publication
  text. Required headings/anchors exist, the old `Commit and push ONB` phrase is
  absent, and all local links on the three pages resolve:
  handoff 85/85, docs 82/82, release 84/84.
- The in-app browser rejected the isolated `file:` URL under its URL policy, so the
  Executor's `scrollWidth=clientWidth=1265` observation could not be independently
  repeated. This is a verification limitation, not a contradictory product result;
  build, content, anchors, and links were independently reproduced from the rendered
  HTML.
- **Match:** ✅, with the stated overflow-observation limitation.

### V7: Exact scope and trace claims

- Framework measurements reproduce exactly:
  router 719 + tests 1,066 + workflow owners/copies 1,296 + adapter owners/consumers
  79 = 3,160 changed lines.
- Implementation commit is
  `350b56d62765938bd80749457c6dd6aaa17a8e2e`, parent
  `0006a6b6699ab301bf9876f7212f8b70b3570b60`, subject
  `[codex/TFW-49/phase-b/executor] implement workflow and adapter consumption`,
  and contains the expected 32-path implementation/trace set.
- ONB, EV, RF, and the single README row are present; README is at `🟢 RF (B)`.
- EV contains mandatory headings, PR-B1–PR-B8, seven AC Evidence rows, and the exact
  `0/7 VERIFIED, 0 DEFERRED, 0 BLOCKED, 7 N/A` verdict. RF contains all mandatory
  §§1–9 and 7/7 checked AC rows.
- **Match:** ✅

### V8: Activation anchor and exact local history

- `audit-range --repo .` at target `350b56d...` returns valid exclusive-anchor
  semantics, the full anchor
  `f1106186417e84cdb38e797f7af66a60885bad76`, 13 exact descendants, and
  `actor_authentication:false`.
- `git merge-base --is-ancestor` succeeds and independent `rev-list` count is 13.
- All 13 subject-leading identities parse under C1-R; no pre-anchor commit is included.
- **Match:** ✅

## Acceptance, Principle, and Failure Matrices

### TS AC

| AC | Independent result |
|----|--------------------|
| AC-1 | ✅ One Phase A-consuming router; exact 11-workflow map; no second accepted-value/pattern registry |
| AC-2 | ✅ Seven operations and every same-/cross-context disposition reproduced |
| AC-3 | ✅ Guarded none, mixed-task, missing/stale/unsafe inputs, stable codes, synthetic correction, and redaction reproduced |
| AC-4 | ✅ Exactly three action-local cues; F26 stop and no action inflation |
| AC-5 | ✅ Four template surfaces; three installed entries; 11/11 + 11/11 + 11/11 parity; Cursor absent |
| AC-6 | ✅ Tests/build/warnings/scope/protected state/range/no-publication/non-claims pass |
| AC-7 | ✅ PR-B1–PR-B8, EV/RF, local C1-R implementation commit, board trace, and review stop are traceable |

### HL DoD and Principles

| Set | Result | Evidence |
|-----|--------|----------|
| HL DoD 1–3 | ✅ 3/3 | sole Phase A owner relation; exact map; three action cues separate publication |
| HL DoD 4–5 | ✅ 2/2 | full operation matrix; cross-context replay uses no-commit/current operator |
| HL DoD 6–8 | ✅ 3/3 | four surfaces/thin adapters; guarded context/trailers; stable secret-safe failures |
| HL DoD 9–10 | ✅ 2/2 | tests/Proof Records; hooks/config/history/Phase C/publication boundaries |
| P1–P2 | ✅ 2/2 | one router; all context is explicit and schema/workflow validated |
| P3–P5 | ✅ 3/3 | action locality; current operator; convenience only on exact equality |
| P6–P8 | ✅ 3/3 | separate publication; thin surface-only adapters; no action inflation |
| P9–P10 | ✅ 2/2 | Phase C stays open; declared provenance/non-authentication is explicit |

### Definition of Failure

| DoF | Absent? | Independent evidence |
|----:|:-------:|----------------------|
| 1 | ✅ | 11×4 resolution and unknown-workflow failure |
| 2 | ✅ | schema/module consumption and duplicate-contract scan |
| 3 | ✅ | seven entry blocks declare only surface |
| 4 | ✅ | explicit CLI context; no branch/prior/path/model inference |
| 5 | ✅ | every four-field changed-context branch re-identifies/rejects |
| 6 | ✅ | cross autosquash rejected; replay returns `--no-commit` |
| 7 | ✅ | staged task and mixed-task fixtures fail closed |
| 8 | ✅ | handoff/docs/release F26 gates and unchanged remote ref |
| 9 | ✅ | no hooks/config/migration/history/Phase C implementation |
| 10 | ✅ | false authentication state and explicit provenance-only non-claims |
| 11 | ✅ | unrelated instructions/legacy copies preserved; Cursor not installed |

## Commands Executed

| # | Command / method | Result |
|---|------------------|--------|
| 1 | `python -m pytest .tfw/scripts/test_commit_identity.py .tfw/scripts/test_commit_identity_router.py -q` | 285 passed |
| 2 | `python -m pytest docs/scripts/test_gen_docs.py docs/scripts/test_integration.py -q` | 68 passed |
| 3 | coverage run for router suite | 149 passed; router 92% branch-aware coverage |
| 4 | isolated baseline/final `python -m mkdocs build --config-file docs/mkdocs.yml` | exit 0/0; warnings 294/294, distinct 139/139, +0/−0 |
| 5 | exact 28-path inventory/hash/parity/protected-owner script | 28/28; 2 A, 26 M; no extra; all parity/protected checks pass |
| 6 | independent router compile/describe/operation/failure probes | compile 2/2; exact map; required dispositions/codes/non-claims |
| 7 | real staged-path guarded-none fixture | exit 2, `E_TASK_NONE_STAGED`, no path/traceback leak |
| 8 | rendered HTML anchor/internal-link audit | handoff 85/85, docs 82/82, release 84/84 |
| 9 | `git diff --check` and category `numstat` | clean patch; exact 3,160 measurement |
| 10 | `commit_identity.py audit-range --repo .` + independent DAG checks | valid 13-commit exclusive range; actor authentication false |
| 11 | local Git/config/path/ref checks | local hook unset; no hooks/Cursor; origin fixed; ahead 7/behind 0 |

## Discrepancies Found

No acceptance discrepancy.

Verification limitation: the isolated rendered pages could not be opened through the
in-app browser because its URL policy rejects `file:` pages. The rendered HTML,
required text/headings, anchors, and all internal links were independently checked;
only the RF's exact browser-layout width observation remains an Executor observation.

## Evidence Verification

The EV file exists and every Proof Record was challenged against source or reproduced
output. All seven `N/A` dispositions are justified because the corresponding
Requirement Claim stops at local deterministic behavior or a source/interface seam;
none claims the Phase C live hook/client/platform boundary or a remote irreversible
outcome.

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|-----------------|------------------|----------------|
| E1 | PR-B1/PR-B2 | ✅ | ✅ N/A justified: schema ownership and workflow resolution are local/source-seam claims |
| E2 | PR-B3 | ✅ | ✅ N/A justified: Phase B claims a planner/temp-Git contract, not live client execution |
| E3 | PR-B4 | ✅ | ✅ N/A justified: rejection/redaction is the local output property claimed |
| E4 | PR-B5 | ✅ | ✅ N/A justified: source/render seam is claimed; no publication event is intended |
| E5 | PR-B6 | ✅ | ✅ N/A justified: parity is deterministic; representative cross-agent use remains Phase C |
| E6 | PR-B7 | ✅ | ✅ N/A justified: regression/protected/range checks are local; no hook/hosted/auth outcome is claimed |
| E7 | PR-B8 | ✅ | ✅ N/A justified: local trace integrity neither performs live observation nor independent acceptance |

Evidence items: 7; justified dispositions: 7; missing: 0. Proof Records: 8; resolved:
8.

## Knowledge Citations Verified

- HL §7.2: 13/13 source links resolve and D54/D55/D57/D58, F4, F26, philosophy,
  conventions, and Role Lock items exist.
- ONB §7: 16/16 generated-site links and anchors resolve in the independently built
  final site; every cited D/F/value/convention item exists in its canonical source.
  The ONB intentionally uses generated-site targets after RF D2, so these links are
  evaluated in their rendered context rather than as raw repository-relative paths.

Total citations: 29; verified: 29; hallucinations: 0.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈32 × 0.42⌉ files and recorded findings?
- [x] Ran at least 1 build/test command (or documented why not)?
- [x] Each RF §3 (AC) checkmark verified against actual file?
- [x] KNOWLEDGE.md checked — contradictions with changes documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified (links resolve, items exist)?
  - Total citations: 29, verified: 29, hallucinations: 0
- [x] Evidence artifacts from RF §5 verified (files exist, claims match)?
  - Total evidence items: 7, justified: 7, missing: 0

Stage complete: YES
