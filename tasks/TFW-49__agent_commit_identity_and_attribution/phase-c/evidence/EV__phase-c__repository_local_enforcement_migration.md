# EV — TFW-49 / Phase C: Repository-Local Enforcement and Migration

> **Date**: 2026-07-31
> **Author**: codex / Executor
> **Task**: TFW-49
> **TS**: [TS Phase C](../TS__phase-c__repository_local_enforcement_migration.md)

---

## Environment

| Field | Value |
|-------|-------|
| Primary OS | Microsoft Windows `10.0.26200` |
| Primary Git / Python | Git `2.42.0.windows.1`; Python `3.13.5` |
| Declared secondary boundary | Ubuntu WSL; Git `2.43.0`; Python `3.12.3` |
| Repository | Local `D:\projects\research\steps-framework`; branch `master` |
| Approved baseline | TS commit `1123213193acdf07818d3d18acab38dd8dbf4330` |
| Implementation commits | `bc5566791d11c422244ec6274ff6f16c52ee923c`; corrective `4754392e3608e4d2b1bfa094cfb8c1309daaddfa` |
| Independent Reviewer operation | Routed Reviewer trace commit `1ebb680457e6ece360dc53adbb0e61da8b62584e`; verdict remains `REVISE` pending corrective re-review |
| Protected remote baseline | `origin/master=b4c0a06dc9fbc104c5b8997865b6df3211bd5c0c` |
| CI / Pipeline | Local standard-library CLI, pytest, MkDocs, Windows Git, and Ubuntu WSL |

## Proof Record Index

| Proof Record | Claim / AC | Boundary and proof class | Method or observation | Actual result | Artifact / provenance | Actor / time | Debt |
|--------------|------------|--------------------------|-----------------------|---------------|-----------------------|--------------|------|
| PR-C1 | AC-1 — exact `1.1.0` contract and project-safe state | Local; Seam: schema ↔ current state ↔ clean template ↔ validator/init/runtime | Exhaustive contract/state/template field-removal and semantic-mutation fixtures; exact runtime-owner shape fixtures; source ownership scan | Exact `1.1.0`; current exclusive anchor preserved; clean template is null/root-inclusive; tracked state has no installed truth; schema solely owns production registries/patterns plus canonical runtime kind and target-to-entrypoint relation | `.tfw/commit_identity.schema.json`; `.tfw/commit_identity_state.json`; `.tfw/templates/commit_identity_state.json`; 157 contract tests within the 376-test run | Executor, 2026-07-31 | None |
| PR-C2 | AC-2 — exact exclusive/root-inclusive population | Local; Seam: state semantics ↔ Git DAG ↔ audit output | Temporary one-root, multi-root merge, exclusive, unborn, missing, invalid, shallow, non-ancestor, and no-target DAG enumeration; current exact audit | All intended populations matched commit-for-commit; failure topologies failed closed; corrective pre-RF target `4754392…` audited 23 descendants after `f110618…`; `actor_authentication:false` | `.tfw/scripts/commit_identity.py`; `.tfw/scripts/test_commit_identity.py`; `python .tfw/scripts/commit_identity.py audit-range --repo .` | Executor, 2026-07-31 | None |
| PR-C3 | AC-3 — recognized portable two-hook runtime | Local; Seam; Live: declared Windows/Ubuntu Git/Python hook launch | Exact schema/manifest/target/claims shape mutations; extra file/directory and non-regular target cases; install/verify/repair fail-closed matrix; direct Windows and Ubuntu WSL hook commits | Exact runtime/contract `1.1.0`; only `runtime.json`, `prepare-commit-msg`, and `commit-msg` are recognized; arbitrary non-empty entrypoints, unexpected fields, extra entries, and equivalent shape mutations fail closed without modification; both platform boundaries launched the owned entries | `.tfw/commit_identity.schema.json`; `.tfw/hooks/runtime.json`; hook entries; `.tfw/scripts/commit_identity_hooks.py`; `.tfw/scripts/test_commit_identity_hooks.py` | Executor, 2026-07-31 | None |
| PR-C4 | AC-4 — local lifecycle, private ledger, exact rollback | Local; Seam; Live: current repository local config/private common-dir state | Temp unset/opaque/exact-owned-prior/idempotence/conflict/repair/linked-worktree matrix; current runtime verify | Unset and opaque states restore exactly; prior `.tfw/hooks` retains an explicit secret-safe `prior-relative-owned` disposition across install/install, verify/verify, repair/repair, rollback/rollback; unknown material blocks; main/linked worktrees share one ledger; current repository is installed/valid | `.tfw/scripts/commit_identity_hooks.py`; 70 hook-runtime tests; safe current verify output | Executor, 2026-07-31 | None |
| PR-C5 | AC-5 — router-derived child-only carrier | Local; Seam: router plan ↔ carrier ↔ child environment ↔ hooks | Router/carrier mutation, environment-lifetime, allowlist, seven-operation, and prohibited-command tests | Complete four-field token and required-runtime status are schema/router-derived; forged plans and non-local/publication commands fail; child context is not persisted; outputs keep both non-claims false | `.tfw/scripts/commit_identity_router.py`; `.tfw/scripts/commit_identity_hooks.py`; 149 router tests and carrier tests | Executor, 2026-07-31 | None |
| PR-C6 | AC-6 — non-mutating prepare/final validation | Local; Seam; Live: actual accepted/rejected Git commits on both declared platforms | Byte-before/after checks; complete/partial/malformed/absent/stale context matrix; seven operations; trailer and redaction cases; actual hook invocations | Prepare preserved bytes; complete context passed; partial/malformed/stale failed safely; absent context was visibly structural-only; final validation preserved Phase B operation/trailer rules; no actor-identity claim | Hook runtime/tests; implementation commit `bc556679…` as a real accepted routed commit | Executor, 2026-07-31 | None |
| PR-C7 | AC-7 — destination-owned init/update state | Local; Seam: template/destination ↔ state ↔ init/update ↔ lifecycle | Unborn/existing/broken-HEAD init-state fixtures; canonical workflow assertions; update preservation and recognition scan | Unborn derives root-inclusive/null; existing derives current full OID/exclusive; broken HEAD with existing history blocks; update never sources/overwrites project state and repairs only recognized runtime | `.tfw/workflows/init.md`; `.tfw/workflows/update.md`; `test_init_state_*`; workflow semantic tests | Executor, 2026-07-31 | None |
| PR-C8 | AC-8 — handoff/review/release authority gates | Local; Seam: role workflows ↔ runtime/range ↔ RF/REVIEW/release ↔ F26 | Exact workflow command/scenario assertions; routed Executor commits; independent Reviewer operation and `REVISE` judgment | Handoff uses carrier and post-commit exact audit; Reviewer independently exercised the carrier and retained verdict authority by returning D1–D3; release keeps two range/runtime gates; publication remains separately authorized and prohibited | Five canonical workflows; `bc556679…`; `4754392…`; Reviewer commit `1ebb680…`; REVIEW and stage traces | Executor + Reviewer, 2026-07-31 | Corrective result awaits re-review; this is an acceptance-authority boundary, not missing Evidence |
| PR-C9 | AC-9 — exact canonical/derived parity and scope | Local; Seam: five owners ↔ ten copies; protected consumers | Byte hashes, exact baseline diff, protected-path comparison, claim-language scan | Antigravity 5/5 and Claude 5/5 byte-exact; exact framework set 6 CREATE + 23 MODIFY; 0 extra framework paths; structural parity is not a live-client claim | Five `.tfw/workflows/*` owners and ten approved copies; exact allowlist script | Executor, 2026-07-31 | None |
| PR-C10 | AC-10 — platform/topology/security/operation matrix | Local; Seam; Live: declared Git/Python environments | 70 hook-runtime tests plus 157 contract and 149 router tests; Windows/Ubuntu WSL real hook launches; closed recognition, exact-prior lifecycle, command-spy, redaction, topology, and operation matrices | Combined suite 376/376; declared versions reproduced; D1/D2 negatives and all required range/lifecycle/context/operation/surface-role/security families passed; no real sensitive corpus or external/global sampling used | Three test files; version commands in EV Environment; pytest output | Executor, 2026-07-31 | None |
| PR-C11 | AC-11 — current-repository install and independent Codex proof | Local; Seam; Live: current repository and independent Codex Executor/Reviewer sessions | Approved live transaction; routed Executor implementation/corrective commits; Reviewer runtime/range verification and routed commit; current runtime verify; full exact range; remote OID comparison | Current runtime is installed/valid; Executor commits `bc556679…` and `4754392…` and independent Reviewer commit `1ebb680…` are C1-R/routed and in the exact range; origin remains `b4c0a06…`. The Reviewer operation observation is established, while its `REVISE` verdict is not represented as approval | Current safe runtime/audit outputs; commits `bc556679…`, `4754392…`, `1ebb680…`; REVIEW/stage traces; `origin/master` comparison | Executor + Reviewer, 2026-07-31 | None |
| PR-C12 | AC-12 — regression, exact scope, traces, and corrective re-review handoff | Local; Seam: 29 consumers ↔ regressions/docs ↔ EV/RF/Task Board ↔ independent review | 376 contract/runtime tests; 68 docs tests; pinned MkDocs comparison; rendered HTML link/anchor scan; parity/scope/protected-state/diff checks | Corrected Executor implementation/proof is reproducible; exact 29/29 framework paths, Executor EV/RF plus one README row, Reviewer artifacts read-only, no publication; acceptance remains solely with corrective re-review | This EV; Phase C RF; README TFW-49 row; REVIEW `1ebb680…`; verification matrix below | Executor, 2026-07-31 | None |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | No separate intended-environment observation is triggered; ownership/state serialization is related by PR-C1 Local/Seam proof and live installation is scoped to AC-11 | Local source and fixtures | N/A | PR-C1 |
| E2 | AC-2 | No separate live observation is triggered here; temporary DAG proof is PR-C2 and the current-repository audit is scoped to AC-11 | Temporary Git DAGs and current repository | N/A | PR-C2, PR-C11 |
| E3 | AC-3 | Actual Git invoked the exact closed runtime on both platforms; isolated lifecycle observations rejected extra reserved entries, non-canonical entrypoints, unexpected manifest/target fields, and equivalent owner-shape mutations across install/verify/repair | Windows Git `2.42.0.windows.1` / Python `3.13.5`; Ubuntu WSL Git `2.43.0` / Python `3.12.3`; Windows temporary repositories | VERIFIED | PR-C3, PR-C10 |
| E4 | AC-4 | Install/verify/repair/rollback observations include unset, opaque, linked-worktree, and exact prior `.tfw/hooks`; repeated rollback preserves `prior-relative-owned` with ledger absent and no private value disclosure; current verify is valid | Windows temporary repositories, linked worktree fixture, and current repository | VERIFIED | PR-C4, PR-C11 |
| E5 | AC-5 | No separate Evidence boundary is triggered; transport/environment lifetime is Local/Seam proof, while the real routed commit is recorded under AC-11 | Local process and current repository | N/A | PR-C5, PR-C11 |
| E6 | AC-6 | Actual accepted and rejected commits exercised prepare/final behavior on both declared platforms; the observation establishes structural/runtime validation only | Windows and Ubuntu WSL temporary repositories; current routed Executor commit | VERIFIED | PR-C6, PR-C10, PR-C11 |
| E7 | AC-7 | No separate Evidence boundary is triggered; destination/init/update behavior is isolated Local/Seam proof and current installation is AC-11 | Temporary repositories and workflow sources | N/A | PR-C7 |
| E8 | AC-8 | No separate row is claimed: real Executor/Reviewer use is owned by AC-11; release publication is forbidden by F26 and waives no local gate proof | Current handoff workflow; publication not authorized | N/A | PR-C8, PR-C11 |
| E9 | AC-9 | Source/copy parity is structural Seam proof only; no live Antigravity or Claude client is available or required | Local filesystem | N/A | PR-C9 |
| E10 | AC-10 | The complete corrected recognition, lifecycle, hook, context, operation, topology, and diagnostics matrix was observed, including real hook launches under the exact declared Windows and Ubuntu WSL versions | Windows and Ubuntu WSL temporary repositories | VERIFIED | PR-C10 |
| E11 | AC-11 | Current install/verify, routed Executor commits, exact full range, unchanged origin, and the independent Reviewer routed operation at `1ebb680…` were observed; its verdict was `REVISE`, so acceptance still requires independent corrective re-review | Current TFW repository; independent Codex Executor and Reviewer sessions | VERIFIED | PR-C11; REVIEW and reviewer stage traces |
| E12 | AC-12 | Aggregate Evidence is intentionally represented by E3/E4/E6/E10/E11; regression/build/scope/trace checks are Local/Seam proof rather than a second live observation | Local verification and handoff | N/A | PR-C12 |

### Status Consequences

- `VERIFIED` rows establish only the runtime/platform/lifecycle observations named in
  their related Proof Records.
- `VERIFIED` E11 establishes the independent routed operation observation only; the
  existing `REVISE` verdict is not converted into approval by corrective Executor work.
- `N/A` rows retain their claim-based reason and do not waive Local or Seam Proof.
- No row claims actor authentication, live non-Codex client support, or publication.

## Verdict

Evidence verdict: 5/12 VERIFIED, 0 DEFERRED, 0 BLOCKED, 7 N/A

## Value Debt

No Value Debt. The previously deferred independent Reviewer operation occurred in
commit `1ebb680…` and remains valid Evidence; its `REVISE` judgment correctly returned
D1–D3 for correction. Only a fresh independent re-review can issue acceptance.

## Attachments

No binary attachments. Reproducible textual evidence is indexed above; temporary
repositories, generated sites, local Git configuration, and private runtime ledger
state are intentionally not committed.

---

*EV — TFW-49 / Phase C: Repository-Local Enforcement and Migration | 2026-07-31*
