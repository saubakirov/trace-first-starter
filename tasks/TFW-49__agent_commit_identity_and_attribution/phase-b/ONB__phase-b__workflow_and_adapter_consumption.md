# ONB — TFW-49 / Phase B: Workflow and Adapter Consumption

> **Date**: 2026-07-31
> **Author**: Executor (Codex)
> **Status**: 🟠 ONB — Awaiting explicit Coordinator approval
> **Parent HL**: [Phase B HL](HL__phase-b__workflow_and_adapter_consumption.md)
> **TS**: [Phase B TS](TS__phase-b__workflow_and_adapter_consumption.md)
> **Master HL**: [TFW-49](../HL-TFW-49__agent_commit_identity_and_attribution.md)
> **Approved planning commit**: `95f95c730e4365606cb5b1aafc796cdf1fd6ae21`
> **Publication boundary**: local work and local commits only; process F26 prohibits push or any remote publication

---

## 1. Understanding

Phase B must add one standard-library operation router and its isolated tests, then
make every canonical TFW workflow and registered adapter surface consume that router
without creating a second C1-R grammar, registry, trailer vocabulary, diagnostic truth
boundary, or identity authority. The active adapter supplies only its exact registered
surface. The active workflow supplies an explicit task, work slice, and Role Lock.
The router validates that complete current context through the unchanged Phase A
schema, state, formatter, parser, message validator, staged-path guard, and
secret-safe diagnostics.

The seven authorized Requirement Claims are:

1. one router with the exact 11-workflow context map;
2. truthful ordinary, merge, amend, fixup, squash, revert, and cherry-pick routing;
3. guarded `task:none`, missing/stale-context failure, and non-disclosing diagnostics;
4. point-of-action consumption only in handoff, docs, and release, with F26 separating
   a local commit or tag decision from push, deploy, publish, and notify;
5. exact surface declarations and canonical-copy parity for Antigravity, Claude Code,
   Codex, and the uninstalled Cursor source;
6. full local regression and protected-state proof without hooks, Git configuration,
   migration, history rewrite, publication, authentication, or Phase C claims; and
7. traceable local completion through `PR-B1`–`PR-B8`, EV, RF, a local C1-R commit,
   the Phase B Task Board row, and an explicit stop for independent review.

Acceptance-critical precision is the exact 11-workflow map, the operation outcomes,
four-field equality, guarded `task:none`, four registered surface declarations, the
28-path framework write set, all protected Phase A/Phase C/publication boundaries, and
the required proof relations. Adaptable Technical Guidance is limited to the router's
internal API/data structures, CLI flag names, machine-readable plan layout, test
helper structure, mechanical copy method, and compact cue wording when the same
authority, context, action, stop, and diagnostic consequences remain observable.

Execution will follow the dependency order `AC-1 → AC-2/AC-3 → AC-4 → AC-5 → AC-6
→ AC-7`. No implementation file will change before explicit Coordinator `APPROVE`.

## 2. Entry Points

### Exact Planned Framework Write Scope

The write scope is exactly 28 framework paths: 2 CREATE and 26 MODIFY.

| # | Path | Action | Ownership purpose |
|---:|------|--------|-------------------|
| 1 | `.tfw/scripts/commit_identity_router.py` | CREATE | Single workflow-context and Git-operation router |
| 2 | `.tfw/scripts/test_commit_identity_router.py` | CREATE | Router, operation, context, security, and temporary-Git proof |
| 3 | `.tfw/workflows/docs.md` | MODIFY | Task-specific `docs/coordinator` local commit cue |
| 4 | `.tfw/workflows/handoff.md` | MODIFY | Routed local ONB commit and separate F26 publication gate |
| 5 | `.tfw/workflows/release.md` | MODIFY | Local release commit/tag decision separated from publication |
| 6 | `.tfw/adapters/antigravity/tfw-rules.md.template` | MODIFY | Exact `antigravity` surface declaration and router consumption |
| 7 | `.tfw/adapters/claude-code/CLAUDE.md.template` | MODIFY | Exact `claude-code` surface declaration and router consumption |
| 8 | `.tfw/adapters/codex/AGENTS.md.template` | MODIFY | Exact `codex` surface declaration and router consumption |
| 9 | `.tfw/adapters/cursor/tfw.mdc.template` | MODIFY | Exact `cursor` surface declaration; no live installation |
| 10 | `.agent/rules/tfw.md` | MODIFY | Installed Antigravity entry consumer |
| 11 | `CLAUDE.md` | MODIFY | Installed Claude Code entry consumer |
| 12 | `AGENTS.md` | MODIFY | TFW-managed Codex block only |
| 13 | `.agent/workflows/tfw-docs.md` | MODIFY | Exact canonical copy |
| 14 | `.agent/workflows/tfw-handoff.md` | MODIFY | Exact canonical copy |
| 15 | `.agent/workflows/tfw-init.md` | MODIFY | Restore exact canonical copy; no hook lifecycle |
| 16 | `.agent/workflows/tfw-knowledge.md` | MODIFY | Restore exact canonical copy |
| 17 | `.agent/workflows/tfw-plan.md` | MODIFY | Restore exact canonical copy |
| 18 | `.agent/workflows/tfw-release.md` | MODIFY | Exact canonical copy |
| 19 | `.agent/workflows/tfw-research.md` | MODIFY | Restore exact canonical copy |
| 20 | `.agent/workflows/tfw-update.md` | MODIFY | Restore exact canonical copy; no hook repair |
| 21 | `.claude/commands/tfw-docs.md` | MODIFY | Exact canonical copy |
| 22 | `.claude/commands/tfw-handoff.md` | MODIFY | Exact canonical copy |
| 23 | `.claude/commands/tfw-init.md` | MODIFY | Restore exact canonical copy; no hook lifecycle |
| 24 | `.claude/commands/tfw-knowledge.md` | MODIFY | Restore exact canonical copy |
| 25 | `.claude/commands/tfw-plan.md` | MODIFY | Restore exact canonical copy |
| 26 | `.claude/commands/tfw-release.md` | MODIFY | Exact canonical copy |
| 27 | `.claude/commands/tfw-research.md` | MODIFY | Restore exact canonical copy |
| 28 | `.claude/commands/tfw-update.md` | MODIFY | Restore exact canonical copy; no hook repair |

Executor lifecycle writes are limited to this ONB, the later Phase B EV path,
the Phase B RF, and the single TFW-49 Task Board row in `README.md`.

### Consumed and Protected Owners

- The unchanged Phase A owners are `.tfw/commit_identity.schema.json`,
  `.tfw/commit_identity_state.json`, `.tfw/scripts/commit_identity.py`, and
  `.tfw/scripts/test_commit_identity.py`.
- The unchanged canonical workflow owners are `plan.md`, `research/base.md`,
  `review.md`, `resume.md`, `knowledge.md`, `update.md`, `config.md`, and `init.md`.
- Exact config values `14/8/1200/12`, `.tfw/project_config.yaml`, its template, and
  all C1-R accepted values remain unchanged.
- All 11 canonical/installed Codex skill pairs are read-only and must remain
  byte-identical.
- Exact Antigravity/Claude copies for config, review, and resume are read-only.
- `.cursor/rules/tfw.mdc` remains absent. Legacy `.agent/workflows/tfw-task.md` and
  `.claude/commands/tfw-task.md` remain present and unchanged.
- HL, TS, RES, Phase A ONB/EV/RF/REVIEW and review stages, KNOWLEDGE, TECH_DEBT,
  hooks, `.tfw/hooks`, Git configuration, history migration, init/update hook
  lifecycle, release publication, and all Phase C outputs are protected.

### Specification-to-Reality Check

| Check | Approved claim/source | Actual project/source | Proof or product-cohesion effect | Disposition |
|-------|-----------------------|-----------------------|----------------------------------|-------------|
| Required identifiers and paths | TS §4: exactly 28 framework paths, 2 CREATE and 26 MODIFY | Both router paths are absent; all 26 MODIFY paths exist; Cursor live path is absent; legacy `tfw-task.md` paths exist | Exact scope and absent-path assertions are feasible; no 29th framework path is needed | Match |
| Phase A semantic owners | D58, Phase A RF/REVIEW, TS AC-1/AC-6 | Schema/state/CLI/tests load successfully; schema owns four surfaces, four roles, work rules, reserved forms, trailers, diagnostic example, and truth boundary; state owns the full anchor, hook false, and authentication false | Router can import the public owner and validate routing policy against it without changing it | Match |
| Workflow context inventory | TS AC-1 exact 11-row map | All 11 canonical workflows exist. Roles/task/work authority are resolvable from current workflow semantics; docs currently says Coordinator/Reviewer and release says Coordinator/Maintainer, while the approved Phase B output requires registered `coordinator` at commit time | In-scope wording must make the C1-R Role Lock explicit; no new role or action is required | Match — planned implementation gap |
| Current Git-action surfaces | TS AC-4: only handoff, docs, release change action cues; update clone is auxiliary fetch | Source scan finds `commit and push` only in handoff, task-commit wording in docs, release tag/deploy/publish/notify wording, and upstream clone only in update | The action boundary is exactly the approved three workflows; eight others need mapping only | Match |
| Adapter entry consumers | TS AC-5: four exact surface declarations, three installed entry consumers, no Cursor install | No adapter template currently declares a Commit Identity surface or router; root Codex managed block is one exact template copy; installed Antigravity/Claude entry files have project-specific surrounding text | Add only the thin surface/router cue; preserve unrelated root instructions and marker boundaries | Match — planned implementation gap |
| Derived workflow parity | TS §4/AC-5: 11/11 exact after sync; eight changed copies per installed copy surface | Antigravity and Claude are each 5/11 exact. Plan, research, handoff, knowledge, update, and init drift now; docs/release are exact now but will follow their changed canonical owners. Config/review/resume are already exact | Mechanical source-to-copy synchronization is feasible. Current one-surface delta is 538 changed lines; two-surface total is the TS-cited 1,076 | Match |
| Codex and Cursor boundaries | TS AC-5: Codex 11/11 unchanged; Cursor template only | All 11 Codex skill pairs are byte-identical; `.cursor/rules/tfw.mdc` is absent | Exact hash/parity and absence checks can prove the boundary without writes | Match |
| Required tests/checks | TS AC-1–AC-7 and PR-B1–PR-B8 | Baseline Phase A suite: `136 passed`; docs pair: `68 passed`; Python 3.13.5, Git 2.42.0, pytest and MkDocs 1.6.1 are available | Router/mutation/temporary-Git suites, docs tests, render/build comparison, link/parity/scope/state scans are feasible locally | Match |
| Exact activation audit | TS AC-6 and Phase A authority | `audit-range --repo .` passes at planning `HEAD=95f95c7` for exactly 11 descendants after full anchor `f110618...`; `actor_authentication:false` | Pre/post local commit audits can include every new ONB/implementation trace without shrinking the range | Match |
| Protected Git state | F26, TS AC-6/AC-7 | Branch `master`; `origin/master=b4c0a06`; local ahead 5 / behind 0; clean tree. Local `core.hooksPath` is unset, `.tfw/hooks` is absent. Global value was sampled only as a non-reversible hash; its path and hook bodies were not read | Local commits are feasible through command-local `.tfw/hooks` isolation; config and remote refs can be compared without publication | Match |
| Outcome and live boundary | All Phase B Evidence rows are claim-based `N/A` unless execution discovers a genuine intended-environment dependency | Phase B claims deterministic local source/interface/Git-fixture behavior. Rendered documentation is a QA seam, not cross-agent runtime evidence. Phase C owns live hook/client/platform proof | Local/Seam Proof is available; no Live Proof or Value Debt is presently triggered | Feasible |
| Scope and product cohesion | TS bounded cohesion override: 28 framework paths, estimated 2,100–2,700 changed LOC, configured signals `14/8/1200/12` | Actual scope is exactly 28 paths; 2 new and 26 modified. Pre-existing canonical-copy drift alone is reproducibly 1,076 changed lines across two surfaces | File, modified-file, and LOC attention signals are crossed; new-file signal is not. Splitting would leave registered consumers behaviorally inconsistent | Coherent approved override |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking question. The approved identifiers, source relations, exact scope, and proof routes match the current tree. Is Phase 2 execution approved under this ONB and its recorded protected boundaries? | _Coordinator must reply `APPROVE` or `REVISE`._ |

## 4. Recommendations (suggestions, not blocking)

1. Make the router data-oriented and import the Phase A module from the same scripts
   directory. Treat its workflow-role/work map as Phase B routing policy, validate
   every mapped value against the schema-owned registries/patterns at load time, and
   include mutation tests that prove removal/change of a schema value changes or
   rejects router behavior rather than activating a fallback.
2. Emit a small structured operation plan containing only normalized current context,
   operation disposition, validated subject or safe synthetic correction, required
   no-commit/inspection action, and optional schema-owned trailer names. Never return
   arbitrary rejected subject/body/path/environment input.
3. Keep action cues compact and local: one complete router invocation/requirement
   immediately before the actual handoff/docs/release history action. The other eight
   workflows remain registry-mapped without acquiring Git steps.
4. Synchronize the eight approved Antigravity and Claude copy pairs mechanically from
   canonical sources after canonical edits. Verify all 11 pairs, but do not rewrite
   the already exact config/review/resume copies.
5. Compare MkDocs baseline `95f95c730e4365606cb5b1aafc796cdf1fd6ae21`
   and the final tree in isolated local copies using identical Python/MkDocs inputs,
   warning filters, path normalization, and set comparison. Attribute every added
   warning; do not call unchanged TD-125 warnings new.
6. Capture protected-file hashes, local/global `core.hooksPath` presence plus
   non-reversible value hashes, remote-ref OIDs, and the exact `f110618...HEAD` audit
   before implementation. Re-run the same checks at Pre-RF and after the final local
   commit without printing configured paths or reading any hook body.

## 5. Risks Found (edge cases, potential issues not in TS)

1. A workflow map containing approved role/work literals could be mistaken for a
   second accepted-value registry. AC-1/PR-B1 must distinguish routing-policy
   assignments from the schema-owned acceptance registry and prove fail-closed
   consumption under owner mutation.
2. Phase A public reserved-form parsing intentionally requires complete expected
   context. The router must never fall back to the private structural-only range path
   for amend/fixup/squash/revert operation decisions.
3. Docs currently spans a Reviewer-triggered transition but Phase B requires
   `docs/coordinator` for the commit. The point-of-action cue must make that Role Lock
   transition explicit so the operator role is not inherited from review prose.
4. Release currently names “Maintainer,” which is not a registered C1-R role. Routing
   must require `coordinator` without expanding the Phase A role registry.
5. Same-context generated revert and cross-context replay share related Git words but
   require different outcomes. Tests must separate retained exact identity from
   `--no-commit` plus current-operator commit and optional source provenance.
6. `task:none` can look valid from task/work syntax alone. Router fixtures must include
   explicit non-task intent, missing staged-path inspection, one staged task, and
   mixed-task paths so no task-scoped batch collapses into `none`.
7. Full derived-copy replacement creates a large mechanical diff. Exact pair hashes
   and a 28-path allowlist are needed so unrelated legacy copies, root instructions,
   or already exact consumers cannot enter unnoticed.
8. Root `CLAUDE.md` contains pre-existing uppercase `PROJECT_CONFIG.yaml` references
   outside the Phase B identity behavior. Absorbing that cleanup would violate the
   no-unrelated-work boundary; synchronization must be targeted rather than a wholesale
   root-template replacement.
9. The global hook configuration exists. Phase B must compare it without printing its
   value, reading its target, or executing/copying/mutating any hook. Every real local
   Phase B commit must use only the authorized command-local isolation argument.
10. Local fixture success can be overclaimed as final cross-agent, GUI, hook,
    worktree, shell/platform, hosted, or actor-authentication proof. EV/RF must leave
    those Phase C claims explicitly open.
11. The repository is already five local commits ahead of `origin/master`. Any push,
    remote mutation, or history rewrite would violate F26 and the TS even if the local
    implementation is complete.

## 6. Inconsistencies with Code (spec vs reality)

1. TS requires one operation router and router tests, while both approved CREATE paths
   are absent. This is the primary authorized implementation gap, not a scope mismatch.
2. TS requires exact adapter surface declarations and shared router consumption, while
   the four canonical entry templates and three installed entry consumers contain no
   Commit Identity surface/router cue. This is an authorized AC-5 gap.
3. Canonical handoff still couples “commit and push ONB,” contrary to F26 and AC-4.
   The approved handoff consumer owns the corrective local-commit/separate-publication
   wording.
4. Canonical docs says to commit knowledge with the task commit but does not establish
   the documented task's `docs/coordinator` route. The approved docs consumer owns the
   point-of-action correction.
5. Canonical release delegates tag/deploy/publish/notify to project release steps
   without first separating local commit/tag preparation from remote authority. The
   approved release consumer owns that correction.
6. Antigravity and Claude copies are each only 5/11 byte-identical to canonical
   workflows. Six copy pairs are already stale; docs/release become two additional
   changed pairs when their owners change. The TS explicitly authorizes exactly those
   eight pairs per surface.
7. Docs uses a `Coordinator / Reviewer` header and release uses
   `Coordinator / Maintainer`, while the approved commit contexts use the registered
   `coordinator` role. Phase B must make the commit-time authority explicit without
   adding a role.
8. Phase A `validate_state` retains the diagnostic phrase “must remain false in Phase
   A” for installed hooks. The actual state is false and Phase B also requires false;
   changing this protected Phase A owner is unnecessary and forbidden. It remains a
   read-only wording observation with no acceptance effect.
9. Root `CLAUDE.md` has pre-existing uppercase config references outside the approved
   identity behavior. This does not affect the Phase B claims and will not be changed.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | [`.tfw/README.md` — Traces Over Code](../../../.tfw/README.md#traces-over-code) | ✅ | Applied | The local subject and router plan connect Git history to the same task/work/role filesystem traces. |
| 2 | [`.tfw/README.md` — Honesty Over Convincingness](../../../.tfw/README.md#honesty-over-convincingness) | ✅ | Applied | Missing or conflicting context fails; no guessed provenance, publication, authentication, or Phase C claim. |
| 3 | [`.tfw/README.md` — Structural Enforcement](../../../.tfw/README.md#structural-enforcement) | ✅ | Applied | Actual action workflows receive observable router gates; exact copy/path/state checks prove deployment. |
| 4 | [`.tfw/README.md` — Single Source of Truth](../../../.tfw/README.md#single-source-of-truth) | ✅ | Applied | Phase A JSON/CLI remain the semantic owners; Phase B adds one router and thin local consumers only. |
| 5 | [D54](../../../KNOWLEDGE.md) | ✅ | Applied | Four adapter surfaces use thin, progressively loaded entry consumers and canonical workflow copies. |
| 6 | [D55](../../../KNOWLEDGE.md) | ✅ | Applied | Role/authority and rule-locality consequences remain complete at the commit action boundary. |
| 7 | [D57](../../../KNOWLEDGE.md) | ✅ | Applied | Commit identity is provenance, never Proof, Evidence status, RF attestation, or REVIEW acceptance. |
| 8 | [D58](../../../KNOWLEDGE.md) | ✅ | Applied | Phase B owns routing/consumption; hooks, Git configuration, migration, and cross-agent proof remain Phase C. |
| 9 | [`.tfw/conventions.md` — Rule Record and Rule Deployment](../../../.tfw/conventions.md#rule-record-and-rule-deployment) | ✅ | Applied | Short complete cues go only at the three real action surfaces; mappings elsewhere do not inflate actions. |
| 10 | [`.tfw/conventions.md` — Commit Identity and Attribution](../../../.tfw/conventions.md#commit-identity-and-attribution) | ✅ | Applied | Exact context, reserved forms, replay, `task:none`, trailer, safe-diagnostic, and non-claim rules govern the router. |
| 11 | [`.tfw/conventions.md` — Role Lock Protocol](../../../.tfw/conventions.md#15-role-lock-protocol) | ✅ | Applied | Each routed role must equal the active workflow authority; Executor writes stay inside ONB/implementation/EV/RF/Task Board scope. |
| 12 | [knowledge/convention.md — F4](../../../knowledge/convention.md) | ✅ | Applied | Each remote contract reference is wrapped in an algorithmic router step where the consequence is observable. |
| 13 | [knowledge/process.md — F26](../../../knowledge/process.md) | ✅ | Applied | Local commits do not authorize push; no Phase B remote operation will occur. |
| 14 | [`.tfw/README.md` — Completeness Over Speed](../../../.tfw/README.md#completeness-over-speed) | ✅ | Applied — new relevant value | Preserve all 11 workflows/four surfaces and complete operation cases; do not split or compress merely to satisfy attention numbers. |
| 15 | [`.tfw/README.md` — Naming Creates Behavior](../../../.tfw/README.md#naming-creates-behavior) | ✅ | Applied — new relevant value | Stable workflow/operation names and field-specific diagnostics are behavioral controls, not cosmetic labels. |
| 16 | [`.tfw/README.md` — Portability](../../../.tfw/README.md#portability) | ✅ | Applied — new relevant value | Production router remains standard-library and consumers avoid developer-specific paths or external-hook dependencies. |

---

*ONB — TFW-49 / Phase B: Workflow and Adapter Consumption | 2026-07-31*
