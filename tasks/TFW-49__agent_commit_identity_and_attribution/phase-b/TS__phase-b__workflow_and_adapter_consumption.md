# TS — TFW-49 / Phase B: Workflow and Adapter Consumption

> **Date**: 2026-07-31
> **Author**: Coordinator (Codex)
> **Status**: ✅ TS — Approved for execution under delegated owner authority
> **Parent HL**: [Phase B HL](HL__phase-b__workflow_and_adapter_consumption.md)
> **Master HL**: [TFW-49](../HL-TFW-49__agent_commit_identity_and_attribution.md)
> **Research**: [Iteration 1 RES](../research/iter1/RES.md) — SUFFICIENT
> **Phase A authority**: RF and REVIEW approved; local closure commit `8e9e33089448854c1f52aeac8fb250afd1b5c2c6`
> **Execution approval**: 2026-07-31

---

## 1. Objective

Add one operation router that consumes the Phase A C1-R contract and makes truthful
local commit identity available to every canonical TFW workflow and registered adapter
surface. Phase B must correct the three workflows that currently contain explicit
history or publication actions, synchronize installed framework-owned consumers, and
prove ordinary and Git-reserved operation behavior without entering Phase C hook,
configuration, migration, or final cross-agent scope.

## 2. Scope

### In Scope

- Create one standard-library operation router and its isolated automated tests.
- Consume, without duplicating, `.tfw/commit_identity.schema.json`,
  `.tfw/commit_identity_state.json`, and the public formatter/parser/validator
  behavior in `.tfw/scripts/commit_identity.py`.
- Own one exact context map for all 11 canonical `/tfw-*` workflows.
- Route ordinary, merge, amend, fixup, squash, revert, and cherry-pick intent using
  explicit current surface, task, work, and Role Lock.
- Preserve guarded `task:none`, exact same-context reserved forms, current-operator
  replay identity, optional schema-owned source/origin trailers, and secret-safe
  diagnostics.
- Correct the explicit Git-action language in `/tfw-handoff`, `/tfw-docs`, and
  `/tfw-release`, including F26 publication separation.
- Declare each registered surface in its canonical adapter entry source and synchronize
  installed/current-project entry consumers.
- Restore all 11 Antigravity and Claude Code workflow copies to canonical parity where
  present. This changes eight copies per surface; the other three are already exact.
- Verify Codex’s 11 canonical/installed skill pairs remain byte-identical.
- Leave the absent Cursor live adapter absent while updating its canonical template.
- Produce local Proof Records, EV, ONB, RF, exact-path verification, and a local C1-R
  implementation commit. No push is authorized.

### Out of Scope

- Changing C1-R grammar, registries, normalization, trailers, activation anchor, range
  semantics, or the Phase A public truth boundary.
- Modifying `.tfw/scripts/commit_identity.py` or
  `.tfw/scripts/test_commit_identity.py`; their existing public behavior is sufficient.
  If execution finds otherwise, stop and return to the Coordinator.
- Creating `.tfw/hooks`, changing `core.hooksPath`, or claiming hook runtime is installed.
- Implementing `/tfw-init` installation, `/tfw-update` repair, ownership-conflict
  handling, rollback, or other hook lifecycle behavior.
- Rewriting, relabeling, rebasing, or migrating history.
- Final main/linked-worktree, shell/platform, client, hosted, or cross-agent proof.
- Adding commits to workflows that currently have no commit action.
- Installing `.cursor/rules/tfw.mdc`.
- Changing Codex skill copies that already match their canonical sources.
- Modifying legacy `.agent/workflows/tfw-task.md` or
  `.claude/commands/tfw-task.md`.
- Push, remote tag publication, deploy, publish, notify, or other network publication.

## 3. Principles Check

| # | Principle (from HL §7) | Enforced by | Gate |
|---|-------------------------|-------------|------|
| P1 | One contract, one router | AC-1, AC-6 | Import/source relation and mutation tests prove schema/Phase A ownership |
| P2 | Context is supplied, never guessed | AC-1, AC-3, AC-5 | Complete map, negative context cases, exact adapter declarations |
| P3 | Point-of-action enforcement | AC-4 | Source inspection of the three actual action workflows |
| P4 | Current operator wins | AC-2 | Replay fixtures prove current-context subject and optional source trailer |
| P5 | Same-context convenience only | AC-2 | Exact four-field equality and cross-context rejection fixtures |
| P6 | Publication is separate authority | AC-4, AC-6 | F26 wording and protected no-publication proof |
| P7 | Adapters declare surface, not semantics | AC-5 | Entry-source inspection and canonical-copy parity |
| P8 | No action inflation | AC-1, AC-4 | Eight non-action workflows remain free of invented Git actions |
| P9 | Phase ownership stays visible | AC-6, AC-7 | Hook/config/history state and Phase C non-claim checks |
| P10 | Honest provenance boundary | AC-3, AC-6 | Diagnostic and non-authentication assertions |

## 4. Affected Files

### Canonical implementation and entry consumers

| File | Action | Description |
|------|--------|-------------|
| `.tfw/scripts/commit_identity_router.py` | CREATE | Single Phase B workflow-context and Git-operation router |
| `.tfw/scripts/test_commit_identity_router.py` | CREATE | Router, context, operation, security, and temporary-Git fixtures |
| `.tfw/workflows/docs.md` | MODIFY | Routed task-specific `docs/coordinator` local commit cue |
| `.tfw/workflows/handoff.md` | MODIFY | Routed local ONB commit; push separated behind F26 |
| `.tfw/workflows/release.md` | MODIFY | Separate local commit/tag decision from publication authority |
| `.tfw/adapters/antigravity/tfw-rules.md.template` | MODIFY | Declare registered `antigravity` surface and router consumption |
| `.tfw/adapters/claude-code/CLAUDE.md.template` | MODIFY | Declare registered `claude-code` surface and router consumption |
| `.tfw/adapters/codex/AGENTS.md.template` | MODIFY | Declare registered `codex` surface and router consumption |
| `.tfw/adapters/cursor/tfw.mdc.template` | MODIFY | Declare registered `cursor` surface; no live installation |
| `.agent/rules/tfw.md` | MODIFY | Synchronize installed Antigravity entry consumer |
| `CLAUDE.md` | MODIFY | Synchronize installed Claude Code entry consumer |
| `AGENTS.md` | MODIFY | Synchronize only the TFW-managed Codex block |

### Antigravity derived workflow copies

| File | Action | Description |
|------|--------|-------------|
| `.agent/workflows/tfw-docs.md` | MODIFY | Synchronize canonical docs workflow |
| `.agent/workflows/tfw-handoff.md` | MODIFY | Synchronize canonical handoff workflow and existing drift |
| `.agent/workflows/tfw-init.md` | MODIFY | Restore existing canonical parity; mapping only, no hook lifecycle |
| `.agent/workflows/tfw-knowledge.md` | MODIFY | Restore existing canonical parity |
| `.agent/workflows/tfw-plan.md` | MODIFY | Restore existing canonical parity |
| `.agent/workflows/tfw-release.md` | MODIFY | Synchronize canonical release workflow |
| `.agent/workflows/tfw-research.md` | MODIFY | Restore existing canonical parity |
| `.agent/workflows/tfw-update.md` | MODIFY | Restore existing canonical parity; no hook repair lifecycle |

### Claude Code derived command copies

| File | Action | Description |
|------|--------|-------------|
| `.claude/commands/tfw-docs.md` | MODIFY | Synchronize canonical docs workflow |
| `.claude/commands/tfw-handoff.md` | MODIFY | Synchronize canonical handoff workflow and existing drift |
| `.claude/commands/tfw-init.md` | MODIFY | Restore existing canonical parity; mapping only, no hook lifecycle |
| `.claude/commands/tfw-knowledge.md` | MODIFY | Restore existing canonical parity |
| `.claude/commands/tfw-plan.md` | MODIFY | Restore existing canonical parity |
| `.claude/commands/tfw-release.md` | MODIFY | Synchronize canonical release workflow |
| `.claude/commands/tfw-research.md` | MODIFY | Restore existing canonical parity |
| `.claude/commands/tfw-update.md` | MODIFY | Restore existing canonical parity; no hook repair lifecycle |

**Unchanged consumed owners:** `.tfw/commit_identity.schema.json`,
`.tfw/commit_identity_state.json`, `.tfw/scripts/commit_identity.py`,
`.tfw/scripts/test_commit_identity.py`; canonical workflows `plan.md`,
`research/base.md`, `review.md`, `resume.md`, `knowledge.md`, `update.md`,
`config.md`, and `init.md`; all 11 canonical and installed Codex skill pairs; already
exact Antigravity/Claude copies for config, review, and resume.

**Scope-attention measurement:** 28 framework implementation/consumer paths: 2 new and
26 modified, with an estimated 2,100–2,700 changed LOC. The measured pre-existing
Antigravity/Claude canonical-copy delta contributes 1,076 changed LOC before Phase B’s
new routing changes. Task lifecycle traces and the Task Board transition are recorded
separately. Configured signals are 14 files, 8 new files, 1,200 changed LOC, and 12
modified files.

**Response:** bounded cohesion override. File, modified-file, and LOC signals are
crossed, while the new-file signal is not. One router, all registered surfaces, the
three real action workflows, and installed canonical-copy parity form one inseparable
consumer boundary. Splitting by workflow or adapter would knowingly leave supported
surfaces with different provenance behavior. No unrelated legacy cleanup, Phase A
contract change, Cursor installation, or Phase C lifecycle work is admitted.

## 5. Acceptance Criteria

### Acceptance-Critical Precision

The following are acceptance-critical:

- The Phase A schema/state/CLI remain the sole owners of grammar, registries,
  normalization, trailers, diagnostics policy, and range truth.
- The exact 11-workflow context map in AC-1.
- The exact ordinary, merge, amend, fixup, squash, revert, and cherry-pick outcomes in
  AC-2.
- Exact four-field same-context equality; guarded `task:none`; current-operator replay.
- The four registered surface values and exact physical consumer inventory in §4.
- Only handoff, docs, and release gain or change point-of-action Git cues.
- F26, `hook_runtime.installed:false`, no `.tfw/hooks`, no Git configuration change,
  no migration, no actor-authentication claim, and no publication.
- Proof of full canonical-copy parity for installed Antigravity and Claude commands,
  with Cursor still absent.

Adaptable Technical Guidance includes router subcommand/flag names, internal class or
function structure, machine-readable result layout, test-helper organization,
mechanical synchronization method, and exact cue prose where the same authority,
context, action, diagnostic, and stop conditions remain observable.

### AC-1: One Router and Complete Workflow Context Map

One Phase B router consumes the Phase A contract and resolves all 11 workflows from
explicit context without duplicating the grammar or inventing authority.

| Workflow owner | Role | Task rule | Work rule |
|----------------|------|-----------|-----------|
| `.tfw/workflows/plan.md` | `coordinator` | allocated task ID | `master` or selected `phase-*` |
| `.tfw/workflows/research/base.md` | `researcher` | current task ID | `research-iter<N>` |
| `.tfw/workflows/handoff.md` | `executor` | current task ID | `master` or current `phase-*` |
| `.tfw/workflows/review.md` | `reviewer` | reviewed task ID | reviewed `master` or `phase-*` |
| `.tfw/workflows/resume.md` | `coordinator` | resumed task ID | `master`, or selected `phase-*` when writing phase planning traces |
| `.tfw/workflows/docs.md` | `coordinator` | documented task ID | `docs` |
| `.tfw/workflows/knowledge.md` | `coordinator` | candidate-range task ID, or explicit guarded `none` | `knowledge` |
| `.tfw/workflows/release.md` | `coordinator` | explicit task ID, or explicit guarded `none` | `release` |
| `.tfw/workflows/update.md` | `coordinator` | explicit task ID, or explicit guarded `none` | `update` |
| `.tfw/workflows/config.md` | `coordinator` | explicit task ID, or explicit guarded `none` | `config` |
| `.tfw/workflows/init.md` | `coordinator` | initialized `{PREFIX}-1` task; never `none` while creating its canonical task path | `init` |

- **Intent / authority:** Phase B HL deliverables 1, 2, and 4; D58; Role Lock.
- **Claim:** every canonical workflow has one resolvable, truthful C1-R context rule.
- **Boundary:** local router ↔ Phase A contract ↔ 11 workflow authorities.
- **Precision:** table values and sole-owner relation are critical; internal router API
  shape is adaptable.
- **Proof intent:** Local Proof plus Seam Proof across router, schema/CLI, and workflow
  registry; record as `PR-B1` and `PR-B2`.
- [ ] The router rejects an unknown workflow and any role/work combination outside the map.
- [ ] Removing or changing a consumed Phase A registry value changes router behavior
      rather than revealing a duplicated fallback.
- [ ] The eight workflows without current Git actions receive mapping only, not new commits.

Gate: exhaustive 11-workflow mapping tests, consumed-owner mutation tests, and source
inspection for duplicate grammar/registries.

Evidence: N/A — this claim concerns local deterministic source and interface behavior,
not an intended live environment.

### AC-2: Truthful Git Operation Routing  [depends: AC-1]

The router preserves convenience only when the current and nested/source identities
remain truthful.

- **Intent / authority:** Phase B HL operation contract; D58; `.tfw/conventions.md`
  Commit Identity and Attribution.
- **Claim:** supported operation intent produces a validated current-context operation
  plan or fails closed.
- **Boundary:** local router ↔ Phase A parser/validator ↔ temporary Git repositories.
- **Precision:** operation outcomes below are critical; command spelling and internal
  plan structure are adaptable.
- **Proof intent:** Local and Seam Proof in `PR-B3`.
- [ ] Ordinary and merge commits produce a current-context C1-R subject.
- [ ] Amend may retain or reword only when all four existing identity fields equal the
      supplied current context; changed context requires a new current-context subject.
- [ ] `fixup!` and `squash!` are allowed only when the nested target identity exactly
      equals all four current fields.
- [ ] Cross-context autosquash is rejected and directs the operator to a normal
      current-context follow-up or separately authorized unpublished rewrite.
- [ ] Same-context generated replay is accepted only when its retained identity remains
      equal to current context.
- [ ] Cross-context revert and cherry-pick require `--no-commit`, inspection, and a new
      current-operator commit; optional provenance is limited to schema-owned
      `TFW-Source-Commit` and complete `TFW-Content-Origin`.
- [ ] A replayed source never replaces current surface/task/work/role identity.
- [ ] Router output never treats a local commit or tag decision as push authority.

Gate: positive and negative temporary-Git fixtures for every operation, including all
same-context/cross-context branches and trailer validation.

Evidence: N/A — fixtures establish the authorized local operation contract; Phase C
owns representative live client/platform execution.

### AC-3: Guarded Context and Safe Failure  [depends: AC-1]

Missing, stale, contradictory, mixed-task, or unsafe context fails with stable,
complete, non-sensitive correction guidance.

- **Intent / authority:** Phase B HL quality contract; Phase A diagnostics contract.
- **Claim:** the router never guesses task, work, role, surface, or current operator.
- **Boundary:** local explicit inputs, staged-path inspection, Phase A diagnostics.
- **Precision:** `task:none` guard and prohibited diagnostic content are critical;
  wording outside stable codes/fields/correction is adaptable.
- **Proof intent:** Local and Seam Proof in `PR-B4`.
- [ ] `task:none` requires explicit non-task intent, a registered lifecycle work value,
      and no staged canonical task path.
- [ ] Task-scoped or mixed-task docs/knowledge work splits by task or stops; it does not
      collapse into `none`.
- [ ] Unknown/stale surface, task, work, role, workflow, operation, target, or source
      context fails closed.
- [ ] Diagnostics include only stable code, failed field/rule, synthetic complete
      correction, and permitted object identifiers.
- [ ] Diagnostics do not echo arbitrary messages, bodies, configured paths, hook
      bodies, environment dumps, or credential-shaped input.

Gate: synthetic and temporary-repository negative matrix, including staged task paths,
mixed task paths, absent expected context, malformed reserved forms, and redaction
canaries.

Evidence: N/A — local validation and redaction behavior are the complete Phase B claim.

### AC-4: Point-of-Action Workflow Consumption  [depends: AC-1, AC-2]

Only workflows with an existing current-repository history/publication action gain or
change a short, complete router cue.

- **Intent / authority:** Rule Deployment, D58, F26, and Phase B HL deliverable 3.
- **Claim:** handoff, docs, and release invoke or require the truthful local route at the
  action point while keeping publication separately authorized.
- **Boundary:** router ↔ three canonical workflows ↔ their installed copies.
- **Precision:** action locations, contexts, and F26 stop are critical; compact prose is
  adaptable.
- **Proof intent:** Local and Seam Proof in `PR-B5`.
- [ ] Handoff creates a routed local ONB commit under the current task/work and
      `executor`; its former “commit and push” coupling is removed.
- [ ] Docs uses the documented task with `work:docs` and `role:coordinator`.
- [ ] Release uses an explicit task or guarded `none`, `work:release`, and
      `role:coordinator`; local commit/tag preparation is distinct from remote tag,
      push, deploy, publish, and notify authority.
- [ ] Every publication action stops unless separately authorized; for TFW-49 it remains
      unavailable until all phases close and the user later says `APPROVE PUSH`.
- [ ] The update workflow’s upstream clone remains classified as auxiliary fetch, not a
      current-repository commit action.
- [ ] No Git action is invented in plan, research, review, resume, knowledge, update,
      config, or init.

Gate: canonical source inspection, exact action-surface query, router-context checks,
and F26/prohibited-action assertions.

Evidence: N/A — this phase claims local workflow source behavior and performs no remote
publication.

### AC-5: Registered Adapter Parity  [depends: AC-1, AC-4]

Each canonical adapter entry source declares only its registered surface, while
workflow and operation semantics remain owned by canonical workflows and the router.

- **Intent / authority:** D54, D58, and Phase B HL deliverable 5.
- **Claim:** supported surfaces consume one behavior without adapter-local grammar or
  authority inference.
- **Boundary:** four canonical adapter entry sources ↔ three installed entry consumers
  ↔ Antigravity/Claude derived copies ↔ Codex skill pairs.
- **Precision:** registered surface values, exact path inventory, 11/11 parity, and
  absent Cursor live path are critical; synchronization mechanism is adaptable.
- **Proof intent:** Local and multi-source Seam Proof in `PR-B6`.
- [ ] Templates declare exactly `antigravity`, `claude-code`, `codex`, and `cursor`.
- [ ] An adapter supplies only its surface; task, work, role, and operation authority
      come from active workflow/router context.
- [ ] `.agent/rules/tfw.md`, `CLAUDE.md`, and only the root `AGENTS.md` managed block
      match their canonical entry-source behavior.
- [ ] All 11 `.agent/workflows/tfw-*.md` canonical command copies match their exact
      canonical workflow source after synchronization.
- [ ] All 11 `.claude/commands/tfw-*.md` canonical command copies match their exact
      canonical workflow source after synchronization.
- [ ] All 11 `.agents/skills/tfw-*/SKILL.md` files remain byte-identical to their
      `.tfw/adapters/codex/skills/tfw-*/SKILL.md` owners.
- [ ] `.cursor/rules/tfw.mdc` remains absent.
- [ ] Legacy `tfw-task.md` copies are neither removed nor changed.

Gate: exact source-to-copy comparisons, managed-block comparison, registered-surface
query, duplicate-contract search, and absent-path assertions.

Evidence: N/A — source/interface comparisons provide Seam Proof; final representative
cross-agent execution is explicitly Phase C and is not claimed here.

### AC-6: Regression, Protected Boundaries, and Honest Non-Claims  [depends: AC-1, AC-2, AC-3, AC-4, AC-5]

The complete Phase B result passes local regression and preserves every Phase C and
publication boundary.

- **Intent / authority:** D58, F26, Phase A REVIEW, Phase B HL deliverables 8–10.
- **Claim:** routing and consumers are locally complete without changing contract truth,
  Git lifecycle state, history, or remote state.
- **Boundary:** all Phase B files ↔ Phase A contract/tests ↔ docs generation ↔ local Git
  state.
- **Precision:** exact protected files/state and zero publication are critical; local
  tool arrangement is adaptable.
- **Proof intent:** Local and Seam Proof in `PR-B7`.
- [ ] Existing Phase A contract suite remains passing.
- [ ] The new router suite covers every workflow, surface, role, operation, context
      failure class, staged-path guard, secret-safe diagnostic, and trailer branch.
- [ ] Existing docs tests pass.
- [ ] A bounded identical-input MkDocs comparison adds no new warning type; any removed
      warning is reported honestly.
- [ ] `.tfw/commit_identity.schema.json`, `.tfw/commit_identity_state.json`,
      `.tfw/scripts/commit_identity.py`, and
      `.tfw/scripts/test_commit_identity.py` remain unchanged.
- [ ] `hook_runtime.installed` remains `false`; `.tfw/hooks` remains absent; local and
      global Git configuration remain unchanged.
- [ ] No history rewrite or pre-anchor relabeling occurs.
- [ ] Exact exclusive-anchor audit remains valid with
      `actor_authentication:false`.
- [ ] No push, remote tag, deploy, publish, notify, network publication, or host
      escalation occurs.
- [ ] The result claims contractual provenance only, not actor authentication,
      authorship, Proof, RF attestation, REVIEW acceptance, or Phase C completeness.

Gate: full test/build comparison; exact protected-file hashes; Git config/state/path
inspection; exact diff inventory; `git diff --check`; exclusive-anchor audit; local
ahead/behind and remote-ref comparison.

Evidence: N/A — all Phase B deliverables are local. Live/cross-agent and hook-runtime
outcomes are Phase C claims, so their absence creates no Phase B Value Debt.

### AC-7: Traceable Local Completion  [depends: AC-6]

Execution records reproducible Proof Records and stops locally for independent review.

- **Intent / authority:** TFW Proof Record chain, Phase B HL, F26.
- **Claim:** ONB, EV, RF, and the local implementation commit accurately describe the
  implemented scope, observations, limitations, and remaining Phase C work.
- **Boundary:** Phase B implementation ↔ EV/RF attestation ↔ independent REVIEW handoff.
- **Precision:** stable Proof Record identifiers, exact commit scope, protected
  no-push state, and explicit Phase C non-claim are critical.
- **Proof intent:** Local and Seam Proof in `PR-B8`.
- [ ] EV indexes `PR-B1` through `PR-B8`, with claim, boundary/proof class, method,
      result, provenance, actor/time when material, and unresolved debt.
- [ ] Each Evidence row is `N/A` with its claim-based local reason unless execution
      discovers a genuine intended-environment dependency.
- [ ] RF maps every AC to its Proof Records and explicitly leaves independent REVIEW
      open.
- [ ] The implementation commit uses valid current C1-R identity and remains local.
- [ ] Task Board lifecycle changes are limited to the applicable Phase B stage.
- [ ] Phase C, full TFW-49 closure, and publication remain unstarted.

Gate: EV/RF structural checks, AC-to-Proof mapping, exact commit subject/scope
validation, clean-tree check, and no-push state.

Evidence: N/A — local trace integrity is established by Local/Seam Proof; REVIEW is a
separate authority, not Evidence.

### Evidence Artifacts

| File | Description |
|------|-------------|
| `evidence/EV__phase-b__workflow_and_adapter_consumption.md` | Mandatory EV index containing Proof Records, environment, per-AC Evidence rows, verdict, Value Debt, and attachments |
| `PR-B1` | Router consumes Phase A owners without duplicating contract semantics |
| `PR-B2` | Exact 11-workflow context map and no-action-inflation result |
| `PR-B3` | Ordinary/reserved/replay operation matrix in temporary Git repositories |
| `PR-B4` | Context guards, staged-path failures, stable diagnostics, and redaction |
| `PR-B5` | Handoff/docs/release action cues and F26 publication separation |
| `PR-B6` | Four-surface declarations and canonical/installed parity |
| `PR-B7` | Regression, build, exact scope, protected state, audit, and no-publication proof |
| `PR-B8` | EV/RF/commit/Task Board handoff and explicit remaining Phase C boundary |

## 6. Technical Guidance

- A separate `.tfw/scripts/commit_identity_router.py` is the preferred cohesive owner.
  The Phase A CLI is already the contract/validation/audit owner; adding workflow and
  operation policy to it would blur phase ownership.
- The router can import the existing Phase A module from the scripts directory and
  reuse its schema loading, formatting, parsing, message validation, expected-context
  comparison, staged-path inspection, and safe diagnostic behavior.
- The workflow map should be data-oriented and exhaustively checked against the exact
  11-command registry. It must not reproduce schema field patterns or registries.
- Router output may be a stable text or machine-readable operation plan. Exact
  subcommand and flag spelling is adaptable if callers can observe the resolved
  context, action, subject, stop reason, and safe correction.
- Tests should use temporary repositories and synthetic messages/paths. They must not
  mutate current history or depend on developer-specific absolute paths.
- Derived Antigravity and Claude files should be synchronized mechanically from their
  canonical workflows. Current drift exists in handoff, init, knowledge, plan,
  research, and update; docs and release become changed copies because their canonical
  owners change in Phase B.
- Config, review, and resume copies are already canonical and should remain untouched
  while participating in the 11/11 parity proof.
- The Codex skill pairs are already 11/11 byte-identical; verify rather than rewrite.
- `/tfw-init` and `/tfw-update` may be represented in the context map. Their hook
  install/repair/rollback behavior remains Phase C.
- Use command-local hook bypass only as already required for valid post-anchor local
  commits while `.tfw/hooks` is absent. Do not set persistent Git configuration.
- All implementation, tests, builds, commits, and audits remain local.

## 7. Definition of Failure

- ❌ The router duplicates C1-R grammar, registries, normalization, trailers, or
  diagnostic policy instead of consuming Phase A.
- ❌ Any of the 11 canonical workflows lacks the exact context mapping or uses an
  unregistered role/work value.
- ❌ An adapter guesses task, work, or role, or embeds a competing operation contract.
- ❌ Missing or stale context is inferred from branch, author, prior subject, path
  coincidence, or model/session identity.
- ❌ Same-context reserved behavior passes without exact four-field equality.
- ❌ Cross-context autosquash passes, or cross-context revert/cherry-pick retains source
  identity instead of using no-commit plus a current-operator commit.
- ❌ Handoff, docs, release, task completion, local commit, or local tag is represented
  as push, deploy, publish, or notify authorization.
- ❌ A workflow without an existing Git action gains an artificial commit.
- ❌ Any installed Antigravity/Claude canonical command copy remains behaviorally stale,
  or a Codex skill pair is changed without an approved reason.
- ❌ The absent Cursor adapter is installed or legacy `tfw-task.md` copies are absorbed.
- ❌ Phase A owners, hook state, `.tfw/hooks`, Git configuration, prior history, or
  activation/range semantics change.
- ❌ Diagnostics echo arbitrary messages, paths, bodies, environment data, hooks, or
  credential-shaped inputs.
- ❌ Local fixture success is represented as actor authentication, final cross-agent
  proof, REVIEW acceptance, or Phase C completion.
- ❌ Any push, remote tag, deploy, publish, notify, network publication, host escalation,
  or history rewrite occurs.

**On failure:** stop the affected operation or phase, preserve repository and Git
state, record the failed claim and boundary in EV/RF, and return to the Coordinator.
Do not bypass the router or publish to obtain a passing result.

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Workflow map drifts from the 11 canonical commands | Exhaustive registry comparison and unknown-workflow rejection |
| Router duplicates Phase A semantics | Import/source-relation and consumed-owner mutation tests |
| `task:none` hides task-scoped or mixed-task work | Explicit declaration, lifecycle-work registry, and staged-task-path guard |
| Release authority is mapped to an unregistered “maintainer” role | Require registered `coordinator` |
| Replay retains stale source provenance | Exact context comparison and cross-context no-commit route |
| Handoff preserves its current commit/push coupling | Explicit F26 source and negative publication assertions |
| Large derived-copy diff obscures logical ownership | Separate owner/copy inventory and exact parity Proof Record |
| Sync absorbs unrelated legacy copies | Restrict synchronization to canonical 11-command copies; exclude `tfw-task.md` |
| Router grows into hook/config management | Protected-state hashes and explicit Phase C stop |
| Local tests are overclaimed as final runtime proof | Keep Phase B claims local and reserve live/cross-agent proof for Phase C |
| Documentation changes add resolver warnings | Identical-input bounded MkDocs warning comparison |
| Local completion is mistaken for publication approval | F26 checks, unchanged remote ref, and explicit no-push stop |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|------|------------------|-------------------|
| `.agent/workflows/tfw-init.md` | Phase C | Resynchronize after canonical init gains hook installation lifecycle |
| `.claude/commands/tfw-init.md` | Phase C | Resynchronize after canonical init gains hook installation lifecycle |
| `.agent/workflows/tfw-update.md` | Phase C | Resynchronize after canonical update gains recognized-runtime repair/rollback |
| `.claude/commands/tfw-update.md` | Phase C | Resynchronize after canonical update gains recognized-runtime repair/rollback |

Phase C will also consume the Phase B router and Phase A owners, but it must not change
their Phase B contract silently. Any required semantic expansion returns to planning.

---

*TS — TFW-49 / Phase B: Workflow and Adapter Consumption | 2026-07-31*
