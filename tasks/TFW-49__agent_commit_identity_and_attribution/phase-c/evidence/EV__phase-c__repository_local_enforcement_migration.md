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
| Implementation commit | `bc5566791d11c422244ec6274ff6f16c52ee923c` |
| Protected remote baseline | `origin/master=b4c0a06dc9fbc104c5b8997865b6df3211bd5c0c` |
| CI / Pipeline | Local standard-library CLI, pytest, MkDocs, Windows Git, and Ubuntu WSL |

## Proof Record Index

| Proof Record | Claim / AC | Boundary and proof class | Method or observation | Actual result | Artifact / provenance | Actor / time | Debt |
|--------------|------------|--------------------------|-----------------------|---------------|-----------------------|--------------|------|
| PR-C1 | AC-1 — exact `1.1.0` contract and project-safe state | Local; Seam: schema ↔ current state ↔ clean template ↔ validator/init | Exhaustive contract/state/template field-removal and semantic-mutation fixtures; source ownership scan | Exact `1.1.0`; current exclusive anchor preserved; clean template is null/root-inclusive; tracked state has no installed truth; schema remains the sole production registry/pattern owner | `.tfw/commit_identity.schema.json`; `.tfw/commit_identity_state.json`; `.tfw/templates/commit_identity_state.json`; 155 contract tests within the 345-test run | Executor, 2026-07-31 | None |
| PR-C2 | AC-2 — exact exclusive/root-inclusive population | Local; Seam: state semantics ↔ Git DAG ↔ audit output | Temporary one-root, multi-root merge, exclusive, unborn, missing, invalid, shallow, non-ancestor, and no-target DAG enumeration; current exact audit | All intended populations matched commit-for-commit; failure topologies failed closed; current target `bc556679…` audited 20 descendants after `f110618…`; `actor_authentication:false` | `.tfw/scripts/commit_identity.py`; `.tfw/scripts/test_commit_identity.py`; `python .tfw/scripts/commit_identity.py audit-range --repo .` | Executor, 2026-07-31 | None |
| PR-C3 | AC-3 — recognized portable two-hook runtime | Local; Seam; Live: declared Windows/Ubuntu Git/Python hook launch | Manifest/target mutation matrix, owned-target inventory, source scan, direct Windows and Ubuntu WSL hook commits | Exact runtime/contract `1.1.0`; only `prepare-commit-msg` and `commit-msg`; recognized changes fail closed; both declared platform boundaries launched the thin entries successfully | `.tfw/hooks/runtime.json`; `.tfw/hooks/prepare-commit-msg`; `.tfw/hooks/commit-msg`; `.tfw/scripts/test_commit_identity_hooks.py` | Executor, 2026-07-31 | None |
| PR-C4 | AC-4 — local lifecycle, private ledger, exact rollback | Local; Seam; Live: current repository local config/private common-dir state | Temp unset/opaque/idempotence/conflict/repair/linked-worktree matrix; current install → verify → rollback → verify exact unset → reinstall → verify | Temp cases restored exact opaque/unset state without disclosure; unknown material blocked; main/linked worktrees shared one ledger; current repository ended installed/valid with relative-owned local config and private ledger present | `.tfw/scripts/commit_identity_hooks.py`; hook tests; safe lifecycle JSON dispositions from current transaction | Executor, 2026-07-31 | None |
| PR-C5 | AC-5 — router-derived child-only carrier | Local; Seam: router plan ↔ carrier ↔ child environment ↔ hooks | Router/carrier mutation, environment-lifetime, allowlist, seven-operation, and prohibited-command tests | Complete four-field token and required-runtime status are schema/router-derived; forged plans and non-local/publication commands fail; child context is not persisted; outputs keep both non-claims false | `.tfw/scripts/commit_identity_router.py`; `.tfw/scripts/commit_identity_hooks.py`; 149 router tests and carrier tests | Executor, 2026-07-31 | None |
| PR-C6 | AC-6 — non-mutating prepare/final validation | Local; Seam; Live: actual accepted/rejected Git commits on both declared platforms | Byte-before/after checks; complete/partial/malformed/absent/stale context matrix; seven operations; trailer and redaction cases; actual hook invocations | Prepare preserved bytes; complete context passed; partial/malformed/stale failed safely; absent context was visibly structural-only; final validation preserved Phase B operation/trailer rules; no actor-identity claim | Hook runtime/tests; implementation commit `bc556679…` as a real accepted routed commit | Executor, 2026-07-31 | None |
| PR-C7 | AC-7 — destination-owned init/update state | Local; Seam: template/destination ↔ state ↔ init/update ↔ lifecycle | Unborn/existing/broken-HEAD init-state fixtures; canonical workflow assertions; update preservation and recognition scan | Unborn derives root-inclusive/null; existing derives current full OID/exclusive; broken HEAD with existing history blocks; update never sources/overwrites project state and repairs only recognized runtime | `.tfw/workflows/init.md`; `.tfw/workflows/update.md`; `test_init_state_*`; workflow semantic tests | Executor, 2026-07-31 | None |
| PR-C8 | AC-8 — handoff/review/release authority gates | Local; Seam: role workflows ↔ runtime/range ↔ RF/REVIEW/release ↔ F26 | Exact workflow command/scenario assertions and implementation commit through handoff carrier | Handoff uses carrier and post-commit exact audit; review owns independent verify/audit before verdict; release has pre-preparation and pre-publication gates; publication remains separately authorized and prohibited here | Five canonical workflows; `bc556679…`; workflow semantic tests | Executor, 2026-07-31 | VD-C1 for independent Reviewer live half inherited through AC-11 |
| PR-C9 | AC-9 — exact canonical/derived parity and scope | Local; Seam: five owners ↔ ten copies; protected consumers | Byte hashes, exact baseline diff, protected-path comparison, claim-language scan | Antigravity 5/5 and Claude 5/5 byte-exact; exact framework set 6 CREATE + 23 MODIFY; 0 extra framework paths; structural parity is not a live-client claim | Five `.tfw/workflows/*` owners and ten approved copies; exact allowlist script | Executor, 2026-07-31 | None |
| PR-C10 | AC-10 — platform/topology/security/operation matrix | Local; Seam; Live: declared Git/Python environments | 41 hook-runtime tests plus contract/router suites; Windows and Ubuntu WSL real hook launches; command spy, redaction canaries, topology matrices | Combined suite 345/345; declared versions reproduced; all required range/lifecycle/context/operation/surface-role/security families passed; no real sensitive corpus or external/global sampling used | Three test files; version commands in EV Environment; pytest output | Executor, 2026-07-31 | None |
| PR-C11 | AC-11 — current-repository install and independent Codex proof | Local; Seam; Live: current repository and Codex Executor; future independent Reviewer | Presence-only pre-state; approved live transaction; real routed Executor commit; runtime verify; full exact range; remote OID comparison | Executor half established: prior unset/ledger absent, exact rollback, final installed/valid, real routed commit `bc556679…`, 20-commit exact range, origin unchanged. Independent Reviewer verify/range/commit is not yet observed and is not claimed | Current local runtime dispositions; `bc556679…`; exact audit output; `origin/master` comparison | Executor, 2026-07-31 | VD-C1 |
| PR-C12 | AC-12 — regression, exact scope, traces, and Reviewer handoff | Local; Seam: 29 consumers ↔ regressions/docs ↔ EV/RF/Task Board ↔ independent review | 345 contract/runtime tests; 68 docs tests; pinned MkDocs comparison; rendered HTML link/anchor scan; parity/scope/protected-state/diff checks | Executor-owned implementation and handoff proof are reproducible; 29/29 framework paths, ONB/EV/RF plus one README row, no REVIEW, no publication; independent acceptance remains with Reviewer | This EV; Phase C RF; README TFW-49 row; verification matrix below | Executor, 2026-07-31 | No separate debt; AC-11 dependency is VD-C1 |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-1 | No separate intended-environment observation is triggered; ownership/state serialization is related by PR-C1 Local/Seam proof and live installation is scoped to AC-11 | Local source and fixtures | N/A | PR-C1 |
| E2 | AC-2 | No separate live observation is triggered here; temporary DAG proof is PR-C2 and the current-repository audit is scoped to AC-11 | Temporary Git DAGs and current repository | N/A | PR-C2, PR-C11 |
| E3 | AC-3 | The tracked hook runtime was invoked by actual Git in both declared Git/Python environments | Windows Git `2.42.0.windows.1` / Python `3.13.5`; Ubuntu WSL Git `2.43.0` / Python `3.12.3` | VERIFIED | PR-C3, PR-C10 |
| E4 | AC-4 | Install/verify/repair/rollback outcomes were observed in isolated repositories, and install/verify/rollback/reinstall was observed in the current repository without disclosing private values | Windows temporary repositories, linked worktree fixture, and current repository | VERIFIED | PR-C4, PR-C11 |
| E5 | AC-5 | No separate Evidence boundary is triggered; transport/environment lifetime is Local/Seam proof, while the real routed commit is recorded under AC-11 | Local process and current repository | N/A | PR-C5, PR-C11 |
| E6 | AC-6 | Actual accepted and rejected commits exercised prepare/final behavior on both declared platforms; the observation establishes structural/runtime validation only | Windows and Ubuntu WSL temporary repositories; current routed Executor commit | VERIFIED | PR-C6, PR-C10, PR-C11 |
| E7 | AC-7 | No separate Evidence boundary is triggered; destination/init/update behavior is isolated Local/Seam proof and current installation is AC-11 | Temporary repositories and workflow sources | N/A | PR-C7 |
| E8 | AC-8 | No separate row is claimed: real Executor/Reviewer use is owned by AC-11; release publication is forbidden by F26 and waives no local gate proof | Current handoff workflow; publication not authorized | N/A | PR-C8, PR-C11 |
| E9 | AC-9 | Source/copy parity is structural Seam proof only; no live Antigravity or Claude client is available or required | Local filesystem | N/A | PR-C9 |
| E10 | AC-10 | The same required runtime acceptance/rejection/lifecycle families were observed under the exact declared Windows and Ubuntu WSL versions | Windows and Ubuntu WSL temporary repositories | VERIFIED | PR-C10 |
| E11 | AC-11 | Current-repository install, exact rollback/reinstall, routed Executor commit, runtime verify, exact range, and unchanged origin were observed; the independent Reviewer operation is still pending | Current TFW repository, Codex Executor session | DEFERRED | PR-C11, VD-C1 |
| E12 | AC-12 | Aggregate Evidence is intentionally represented by E3/E4/E6/E10/E11; regression/build/scope/trace checks are Local/Seam proof rather than a second live observation | Local verification and handoff | N/A | PR-C12 |

### Status Consequences

- `VERIFIED` rows establish only the runtime/platform/lifecycle observations named in
  their related Proof Records.
- `DEFERRED` E11 is an explicit non-claim for the independent Reviewer half and full
  Phase C acceptance; it does not invalidate the established Executor-local result.
- `N/A` rows retain their claim-based reason and do not waive Local or Seam Proof.
- No row claims actor authentication, live non-Codex client support, or publication.

## Verdict

Evidence verdict: 4/12 VERIFIED, 1 DEFERRED, 0 BLOCKED, 7 N/A

## Value Debt

| Debt | Affected claim / Proof Record | Missing triggered proof | Owner | Due event | Evidence route | Impact and explicit non-claim | Closure condition |
|------|-------------------------------|-------------------------|-------|-----------|----------------|-------------------------------|-------------------|
| VD-C1 | AC-8/AC-11; PR-C8/PR-C11 | Independent Reviewer current-repository runtime/range operation and valid routed Reviewer local commit | Independent TFW Reviewer | `/tfw-review` after Executor RF | Reviewer-owned verify/judge traces, REVIEW verdict, routed Reviewer commit, post-commit exact audit | Full AC-11 and Phase C independent acceptance are not claimed; Executor-local Codex/runtime support remains established only for the Executor half | Reviewer independently verifies runtime, reruns the full exact range, performs its own valid routed local commit, records the result, and judges the phase |

## Attachments

No binary attachments. Reproducible textual evidence is indexed above; temporary
repositories, generated sites, local Git configuration, and private runtime ledger
state are intentionally not committed.

---

*EV — TFW-49 / Phase C: Repository-Local Enforcement and Migration | 2026-07-31*
