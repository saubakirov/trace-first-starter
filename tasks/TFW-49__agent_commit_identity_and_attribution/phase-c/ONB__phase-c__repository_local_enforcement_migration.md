# ONB — TFW-49 / Phase C: Repository-Local Enforcement, Migration, and Cross-Agent Proof

> **Date**: 2026-07-31
> **Author**: Executor (Codex)
> **Status**: 🟠 ONB — Awaiting explicit Coordinator approval
> **Parent HL**: [Phase C HL](HL__phase-c__repository_local_enforcement_migration.md)
> **TS**: [Phase C TS](TS__phase-c__repository_local_enforcement_migration.md)
> **Master HL**: [TFW-49](../HL-TFW-49__agent_commit_identity_and_attribution.md)
> **Approved HL commit**: `88414e1da99ab4ccc0e28875e1c464a90635c5bc`
> **Approved TS / entry commit**: `1123213193acdf07818d3d18acab38dd8dbf4330`
> **Publication boundary**: local work and local commits only; process F26 prohibits every remote publication action

---

## 1. Understanding

Phase C must turn the reviewed Phase A contract and Phase B router into a real,
reversible repository-local operating boundary. It upgrades the sole C1-R owner to
contract `1.1.0`, separates tracked project requirements from private clone-local
installation truth, adds exact `root-inclusive` history semantics beside the current
exclusive anchor, creates only the recognized prepare/final hook runtime, transports
complete expected context only to an allowlisted local Git child process, and makes
init, update, handoff, review, and release consume the same lifecycle and exact range.

The twelve authorized Requirement Claims are:

1. contract `1.1.0`, destination-safe state template, exact activation modes, and no
   tracked clone-local installed truth;
2. complete exclusive-anchor and root-inclusive range traversal with stable no-target
   and topology failures;
3. one recognized portable TFW runtime containing only `runtime.json`,
   `prepare-commit-msg`, and `commit-msg`;
4. idempotent local install, verify, repair, and exact rollback through one private
   Git-common-dir ledger;
5. router-derived complete expected context and a child-only, local-operation carrier;
6. non-mutating prepare validation and final subject/trailer validation for all seven
   Phase B operation classes;
7. destination-owned init state and update preservation/recognized repair;
8. distinct handoff attestation, independent review, release recheck, and F26 gates;
9. exact five canonical workflows and ten byte-identical derived copies;
10. Windows and Ubuntu WSL runtime/topology/security/operation matrices;
11. actual current-repository install and real independent Codex Executor/Reviewer
    local operations, with no non-Codex or authentication overclaim; and
12. `PR-C1`–`PR-C12`, claim-typed EV/RF, regressions, exact scope, protected-state
    proof, final range closure, and Executor STOP before REVIEW.

Binding precision is the exact `1.1.0` version; unchanged C1-R meaning; exact current
anchor; null/root-inclusive template; three runtime targets; one local relative
`.tfw/hooks` override; one private common-dir ledger; complete child-only context;
state-owned full-range gates; the 29-path framework allowlist; Windows and Ubuntu WSL
observations; real Codex-only live support; and absolute non-publication. Adaptable
Technical Guidance is limited to internal Python names, private-ledger child-key
spelling, atomic-write helpers, carrier subcommand/argument spelling, fixture helpers,
and concise workflow wording when all accepted semantics, ownership, diagnostics,
proof boundaries, and stops remain unchanged.

Execution will follow the approved dependency order
`AC-1 → AC-2 → AC-3 → AC-4 → AC-5 → AC-6 → AC-7 → AC-8 → AC-9 → AC-10 → AC-11 → AC-12`.
No Phase C implementation file, Git configuration, hook runtime, or private ledger
will change before explicit Coordinator `APPROVE`.

## 2. Entry Points

### 2.1 Exact Planned Framework Write Scope

The framework write scope is exactly 29 paths: 6 CREATE and 23 MODIFY.

| # | Path | Action | Ownership purpose |
|---:|------|--------|-------------------|
| 1 | `.tfw/templates/commit_identity_state.json` | CREATE | Clean null/root-inclusive project-state source |
| 2 | `.tfw/scripts/commit_identity_hooks.py` | CREATE | Standard-library lifecycle, carrier, prepare, and final owner |
| 3 | `.tfw/scripts/test_commit_identity_hooks.py` | CREATE | Git/platform/topology/context/ownership/security proof |
| 4 | `.tfw/hooks/runtime.json` | CREATE | Recognized runtime manifest |
| 5 | `.tfw/hooks/prepare-commit-msg` | CREATE | Thin portable non-mutating prepare entry |
| 6 | `.tfw/hooks/commit-msg` | CREATE | Thin portable final validator entry |
| 7 | `.tfw/commit_identity.schema.json` | MODIFY | Exact `1.1.0`, two activation modes, tracked/private semantics |
| 8 | `.tfw/commit_identity_state.json` | MODIFY | Preserve exact anchor; portable runtime requirement only |
| 9 | `.tfw/scripts/commit_identity.py` | MODIFY | State validation and exact exclusive/root-inclusive audit |
| 10 | `.tfw/scripts/test_commit_identity.py` | MODIFY | State/template/range/topology/mutation regressions |
| 11 | `.tfw/scripts/commit_identity_router.py` | MODIFY | Complete expected-context token and required-runtime status |
| 12 | `.tfw/scripts/test_commit_identity_router.py` | MODIFY | Context/status/operation/persistence/publication regressions |
| 13 | `.tfw/conventions.md` | MODIFY | Canonical state/runtime/context/client/audit/F26 boundaries |
| 14 | `.tfw/glossary.md` | MODIFY | Concise owner-linked Phase C terms |
| 15 | `.tfw/workflows/init.md` | MODIFY | Destination-derived state plus local install/verify |
| 16 | `.tfw/workflows/update.md` | MODIFY | State preservation plus recognized repair/rollback |
| 17 | `.tfw/workflows/handoff.md` | MODIFY | Routed carrier commit plus exact range attestation |
| 18 | `.tfw/workflows/review.md` | MODIFY | Independent runtime and exact-range gate |
| 19 | `.tfw/workflows/release.md` | MODIFY | Pre-preparation and pre-publication runtime/range gates |
| 20 | `.agent/workflows/tfw-init.md` | MODIFY | Exact canonical copy |
| 21 | `.agent/workflows/tfw-update.md` | MODIFY | Exact canonical copy |
| 22 | `.agent/workflows/tfw-handoff.md` | MODIFY | Exact canonical copy |
| 23 | `.agent/workflows/tfw-review.md` | MODIFY | Exact canonical copy |
| 24 | `.agent/workflows/tfw-release.md` | MODIFY | Exact canonical copy |
| 25 | `.claude/commands/tfw-init.md` | MODIFY | Exact canonical copy |
| 26 | `.claude/commands/tfw-update.md` | MODIFY | Exact canonical copy |
| 27 | `.claude/commands/tfw-handoff.md` | MODIFY | Exact canonical copy |
| 28 | `.claude/commands/tfw-review.md` | MODIFY | Exact canonical copy |
| 29 | `.claude/commands/tfw-release.md` | MODIFY | Exact canonical copy |

Executor lifecycle writes are limited to this ONB, the later Phase C EV and RF, and
the single TFW-49 Task Board row in `README.md`. The private common-dir ledger and the
authorized repository-local config setting are operational state, not framework paths
or tracked lifecycle traces.

### 2.2 Protected Boundaries

- Master HL, Phase C HL/TS, RES, all Phase A/B planning/execution/review traces,
  Reviewer-owned Phase C traces, KNOWLEDGE, TECH_DEBT, config, config template, exact
  scope values, version/release markers, prior history, and unrelated task traces are
  read-only.
- Adapter entry templates, root `AGENTS.md`/`CLAUDE.md`, Codex skill source/installed
  copies, Cursor, six unrelated canonical workflows, and all other derived copies are
  outside the allowlist.
- C1-R, schema-owned accepted registries/patterns/forms/trailers/truth boundary, Phase
  A public/private parsing split, Phase B seven-operation semantics, and F26 remain
  semantic owners; Phase C extends runtime transport/lifecycle only.
- Global/external Git config and hook path/body/value/fingerprint are outside the safe
  corpus. They will not be queried, resolved, read, printed, executed, copied,
  fingerprinted, chained, or mutated. No `git config --global`, `--show-origin`,
  inherited-hook enumeration, or external-hook inspection is permitted.
- Push, remote tag, deploy, publish, notify, host escalation, force update, and history
  rewrite remain prohibited. `origin/master` must stay
  `b4c0a06dc9fbc104c5b8997865b6df3211bd5c0c`.

### 2.3 Specification-to-Reality Check

| Check | Approved claim/source | Actual project/source | Proof or product-cohesion effect | Disposition |
|-------|-----------------------|-----------------------|----------------------------------|-------------|
| Entry commit and repository state | TS approval commit `1123213`; origin fixed at `b4c0a06`; clean, ahead 12 | `HEAD=1123213193acdf07818d3d18acab38dd8dbf4330`; `origin/master=b4c0a06dc9fbc104c5b8997865b6df3211bd5c0c`; ahead 12/behind 0; clean `master` | Establishes exact pre-write tree and no-publication baseline without contacting the remote | Match |
| Exact path inventory | TS §4: 6 CREATE + 23 MODIFY, no 30th framework path | All six CREATE paths are absent; all 23 MODIFY paths exist. Current index mode for every existing consumer is `100644` | Exact allowlist and new/existing classification are directly enforceable | Match |
| Contract and tracked state | AC-1: exact `1.1.0`, two modes, portable runtime requirement | Schema/state are still reviewed Phase A `1.0.0`; range registry contains only `exclusive-anchor`; state contains exact `f110618...`, `hook_runtime.installed:false`, and auth false | These are the authorized state/contract implementation gaps; Phase A accepted values and anchor remain a protected regression surface | Match — planned implementation gap |
| Clean state template | AC-1/AC-7 and philosophy F23 | `.tfw/templates/commit_identity_state.json` is absent | Init cannot yet derive clean null/root-inclusive state; new owner is required exactly as scoped | Match — planned implementation gap |
| Exact range behavior | AC-2: exclusive plus root-inclusive, no-target and topology failures | Current CLI implements exclusive `anchor..target` only. Baseline current-repository audit passes for 18 descendants through `1123213`, with `actor_authentication:false` | Existing exclusive behavior is a regression oracle; root-inclusive/unborn/multi-root semantics require in-scope extension | Match — planned implementation gap |
| Runtime ownership | AC-3: manifest plus two thin entries and one standard-library lifecycle owner | `.tfw/hooks` and both Phase C Python CREATE paths are absent | No current runtime conflict exists in the reserved tracked target; recognition, mode, launcher, and conflict proof remain implementation work | Match — planned implementation gap |
| Executable-bit/platform boundary | AC-3/AC-10: direct Windows and Ubuntu WSL execution | Windows Git `2.42.0.windows.1` / Python `3.13.5` and Ubuntu WSL Git `2.43.0` / Python `3.12.3` are available. No current hook entry exists; all existing scoped files are `100644` | Cross-platform proof is feasible. New hook entries must be committed as executable where Git requires it and invoked directly on both declared boundaries | Feasible — implementation risk recorded |
| Local config and private runtime state | AC-4/AC-11: only local relative override and one private common-dir ledger | Repository-local `core.hooksPath` is unset by presence-only check; Git common-dir resolves; the private runtime ledger is absent; one worktree is currently registered | Authorized install can preserve an exact unset rollback baseline. Linked-worktree sharing must be proved in isolated fixtures before live install | Match |
| Router/carrier | AC-5: exact token, required-runtime status, allowlisted child-only Git carrier | Phase B router plans seven operations but does not execute Git; it emits tracked `hook_runtime_installed:false`, no expected-context token, no runtime requirement, and no carrier | The router remains the operation owner; only transport/status extension belongs in Phase C | Match — planned implementation gap |
| Prepare/final behavior | AC-6: non-mutating prepare plus final message/trailer/context validation | Phase A can validate subjects/messages and exact expected context; no hook consumer or absent/partial command-scoped context boundary exists | Existing public parser is reusable; new hook owner must not duplicate parser/registry or expose message input | Match — planned implementation gap |
| Init/update lifecycle | AC-7: destination-derived state, install/verify, update preservation and recognized repair | Init creates knowledge state from a template but has no Commit Identity template/install step. Update's protected-state list omits Commit Identity state and has no ownership-gated runtime lifecycle | Both canonical workflows require the exact scoped integration; no broader adapter/init redesign is needed | Match — planned implementation gap |
| Handoff/review/release gates | AC-8: carrier + exact range attestation, independent verify/range, release double gate | Handoff routes only to a local plan; review has no Commit Identity runtime/range gate; release routes a local plan but does not verify runtime/range | The three scoped workflow owners are the exact missing acceptance surfaces | Match — planned implementation gap |
| Derived parity | AC-9: five canonical workflows × Antigravity/Claude exact copies | All ten approved derived files are currently byte-identical to their five canonical owners | Mechanical resynchronization after canonical edits is feasible; current equality is the protected baseline | Match |
| Regression/tooling baseline | AC-10/AC-12 | Phase A + B pair: `285 passed`; docs pair: `68 passed`; MkDocs `1.6.1` is available; JSON/Python/Git tools are available | Baseline and final comparisons, rendered QA, exact diff, and claim-typed proof are feasible | Match |
| Citations and authority | HL/TS source tables and local links | Phase C HL has 20 unique local link destinations and TS has 14; all resolve. Approved HL commit is an ancestor and approved TS commit is current `HEAD` | Source fidelity and Seam Proof can be reproduced without external lookup | Match |
| Live outcome | AC-11 requires current-repository install plus independent Executor/Reviewer Codex operations | No runtime is installed and no Phase C live commit exists. Independent Reviewer is available only after Executor RF; non-Codex clients remain unexercised | Executor can establish its own live observation after approval; independent Reviewer proof remains a later role-owned gate and cannot be claimed in RF as already complete | Feasible with explicit role boundary |
| Scope and cohesion | TS override: exact 29 paths, estimate 2,600–3,600 changed framework lines, signals `14/8/1200/12` | Actual owner seam is exactly the approved 29 paths; no extra path is needed. Six creates remain below the new-file signal; file/modified/LOC signals are expected to cross | Splitting would leave state, runtime, lifecycle, or acceptance inconsistent. Actual counts remain descriptive and require disclosure, not compression | Coherent approved override |

### 2.4 Safe Installation and Exact Rollback Plan

1. Finish and prove the recognized tracked runtime in temporary repositories before
   mutating current-repository operational state.
2. At the live gate, query only repository-local config through the lifecycle owner.
   Capture prior local key presence and any opaque value directly into the private
   common-dir ledger; never emit, resolve, hash for reporting, or copy that value.
   The ONB baseline establishes only that the current local key is unset.
3. Verify that all reserved targets are recognized TFW-owned material before any
   repair. Unknown manifest/target material blocks with no overwrite or cleanup.
4. Write the private ledger atomically inside the resolved common directory, then set
   only `git config --local core.hooksPath .tfw/hooks`. No global/external discovery
   or fallback is allowed.
5. Immediately run lifecycle verify and actual hook invocation. If the live
   transition fails, restore the exact prior local disposition (`unset` for the
   current baseline), remove only the recognized private ledger state, leave tracked
   owners intact, and return to the Coordinator with the failed claim.
6. Prove rollback in the current repository without exposing private state, then
   reinstall and verify the final required runtime. Destructive/topology/conflict
   cases remain confined to temporary repositories.
7. Compare local-config presence, private-ledger presence, tracked diff, worktree,
   exact range, and `origin/master` before/after using safe dispositions or object
   IDs only. Non-access to global/external state is proved through command spies and
   source scans, never by sampling prohibited state.

### 2.5 Source and Citation Audit

The cited Phase A/B RF and APPROVE REVIEW artifacts were read as current behavior,
not treated as substitutes for the actual sources. Iteration 1 RES was read through
its challenged configuration, limitations, and open threads. D58/D59, philosophy
F23, process F26, and the cited convention owners resolve and agree with the Phase C
scope. No citation is stale, missing, or contradicted by the current tree.

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking mismatch was found. Is Phase 2 execution approved under this exact 29-path allowlist, the private-ledger/local-config plan, and the recorded non-publication boundary? | _Coordinator must reply `APPROVE` or `REVISE`._ |

## 4. Recommendations (suggestions, not blocking)

1. Extend the existing schema/state loader first and generate all runtime examples,
   accepted values, trailer names, patterns, and truth-boundary output from it. The
   new hook lifecycle may own stable lifecycle diagnostic codes and algorithms, but
   never a second identity or operation registry.
2. Represent private prior local state as a structured presence/value record and keep
   every diagnostic presence-only. Use atomic same-directory replacement and reject
   symlinks, unknown manifest material, path escape, or inconsistent common-dir state.
3. Keep hook entries to portable relative launchers. Commit their intended executable
   mode explicitly, then test both direct entry invocation and real Git invocation on
   Windows and Ubuntu WSL.
4. Make the carrier accept a validated router plan plus an enum-like local operation,
   not an arbitrary command array or shell string. Construct the child environment
   from an allowlist and remove expected context after the child exits.
5. Use temporary repositories for unborn, multi-root, shallow, linked-worktree,
   conflict, repair, rollback, replay, bypass, and redaction cases. Limit the current
   repository to recognized install/verify/rollback/reinstall, real Executor commits,
   exact range, and read-only protected-state checks.
6. Capture a pinned `1123213` MkDocs baseline and final tree with identical commands,
   warning normalization, and link/render checks. Attribute every new warning to a
   changed consumer or block RF if the changed set introduces one.
7. Keep AC-11 honest in Executor RF: record the actual Executor live commit and the
   required later independent Reviewer operation as a pending acceptance dependency,
   not as already verified cross-session completion.

## 5. Risks Found (edge cases, potential issues not in TS)

1. Git for Windows may invoke a shebang hook even when the worktree executable bit is
   not represented like POSIX, while Ubuntu WSL also depends on the committed index
   mode. AC-3/AC-10 proof must distinguish index mode, direct launcher behavior, and
   actual Git hook invocation on each platform.
2. A lifecycle error that forwards raw Git stderr could disclose an opaque prior local
   value or repository path. The owner must translate failures to stable codes and
   discard arbitrary subprocess output.
3. Linked worktrees share a common directory but can have worktree-specific config
   behavior. The implementation must prove the intended local-key and ledger topology
   rather than assuming common-dir equivalence from path resolution alone.
4. The ONB commit precedes the Phase C runtime by design. It must use the exact routed
   C1-R subject with command-local transitional isolation; after live install, every
   Executor commit must pass through the new carrier and hooks.
5. Root-inclusive multi-root history can be undercounted if traversal follows only
   first-parent or one root. Expected commit IDs must be compared set-for-set against
   complete reachable history, not only by count.
6. An update implementation could accidentally treat tracked project state as a safe
   upstream file because the current classification table does not name it. AC-7 must
   add an explicit never-overwrite entry and fixture that uses conflicting upstream
   state.
7. Repair semantics can become destructive if “recognized manifest” is checked after
   file replacement. Ownership recognition must complete before any write and unknown
   targets must remain byte-identical.
8. Child-only context can leak through inherited environment, exception rendering, or
   a persisted plan. AC-5/AC-6 tests need parent-before/after, failure, concurrency,
   and synthetic-canary assertions.
9. A structurally valid direct Git commit without expected context remains possible.
   Hooks must expose structural-only limitation honestly, while the exact range audit
   catches structure—not actor truth—and RF must retain the non-authentication claim.
10. Five canonical edits fan out to ten exact copies. A mechanical sync is required,
    but any sixth canonical workflow or adapter entry change is a blocking 30th-path
    deviation.
11. The branch is already twelve local commits ahead of the fixed remote. Any generic
    workflow wording or command that couples completion to push would violate F26 even
    if every local test passes.

## 6. Inconsistencies with Code (spec vs reality)

1. The approved contract is `1.1.0`, while schema and tracked state are `1.0.0` and
   know only `exclusive-anchor`.
2. The clean Commit Identity state template is absent; init cannot yet distinguish
   unborn null/root-inclusive state from existing-history exclusive activation.
3. Tracked state still carries `hook_runtime.installed:false`, which is clone-local
   observation rather than portable project requirement.
4. The validator requires a string anchor and implements only exclusive
   `anchor..target`; no null/root-inclusive or stable unborn/no-target route exists.
5. The hook manifest, prepare/final entries, lifecycle owner, lifecycle tests, and
   private common-dir ledger are absent; repository-local `core.hooksPath` is unset.
6. The router reports the tracked installed boolean and returns a plan only; it does
   not emit the complete context token/runtime requirement or launch an allowlisted
   child process.
7. Init does not instantiate Commit Identity state or install/verify its runtime.
   Update does not classify the tracked state as never-overwrite or repair recognized
   runtime ownership.
8. Handoff does not execute through a context carrier or attest the post-commit exact
   range. Review and release do not independently verify lifecycle and exact history.
9. Conventions/glossary correctly reserve Phase C ownership but do not yet define the
   tracked/private split, runtime lifecycle, supported-client boundary, or new range
   mode.
10. All ten derived workflow copies are currently exact; their future drift is an
    authorized consequence of changing only the five canonical owners and must close
    back to byte equality.

These ten items are the approved Phase C implementation gaps. None requires a 30th
framework path, a new grammar/operation owner, global/external hook access, or a
broader client/publication claim.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | [`.tfw/README.md` — Traces Over Code](../../../concepts/philosophy.md#traces-over-code) | ✅ | Applied | Exact local subjects and full-range audits connect Git history to durable task/phase/role traces. |
| 2 | [`.tfw/README.md` — Honesty Over Convincingness](../../../concepts/philosophy.md#honesty-over-convincingness) | ✅ | Applied | Missing context, unavailable clients, and failed platform/live proof remain limitations or debt, never inferred success. |
| 3 | [`.tfw/README.md` — Structural Enforcement](../../../concepts/philosophy.md#structural-enforcement) | ✅ | Applied | Hooks add action-boundary visibility; completion still requires claim proof and independent authority. |
| 4 | [`.tfw/README.md` — Naming Creates Behavior](../../../concepts/philosophy.md#naming-creates-behavior) | ✅ | Applied | Stable state, runtime, context, and diagnostic names must preserve one behavior. |
| 5 | [`.tfw/README.md` — Single Source of Truth](../../../concepts/philosophy.md#single-source-of-truth) | ✅ | Applied | Schema/state/CLI/router remain owners; hooks and workflows are narrow consumers. |
| 6 | [`.tfw/README.md` — Portability](../../../concepts/philosophy.md#portability) | ✅ | Applied | Relative standard-library runtime and direct Windows/Ubuntu WSL proof are mandatory. |
| 7 | [philosophy F4](../../../knowledge/philosophy.md) | ✅ | Applied | Runtime/file presence proves structure only, not claim closure. |
| 8 | [philosophy F13](../../../knowledge/philosophy.md) | ✅ | Applied | Workflow/runtime wording stays domain-agnostic and agent-portable. |
| 9 | [philosophy F23](../../../knowledge/philosophy.md) | ✅ | Applied | Clean template and destination-derived activation prevent starter-state contamination. |
| 10 | [process F3](../../../knowledge/process.md) | ✅ | Applied | Precise runtime/context vocabulary is treated as an operational control. |
| 11 | [process F4](../../../knowledge/process.md) | ✅ | Applied | Install, verify, repair, rollback, range, and authority transitions require explicit ordered gates. |
| 12 | [process F26](../../../knowledge/process.md) | ✅ | Applied | No local result authorizes push or any remote publication. |
| 13 | [D28](../../../knowledge-index.md) | ✅ | Applied | Contract/lifecycle names must prompt the intended action without duplicated prose owners. |
| 14 | [D54](../../../knowledge-index.md) | ✅ | Applied | Five canonical workflows fan out to exact Antigravity/Claude copies; parity is structural only. |
| 15 | [D55](../../../knowledge-index.md) | ✅ | Applied | Role authority, proof boundaries, independent judgment, and visible stops remain Method Kernel obligations. |
| 16 | [D57](../../../knowledge-index.md) | ✅ | Applied | Hook/range output relates through Proof Records but cannot replace EV, RF attestation, or REVIEW. |
| 17 | [D58](../../../knowledge-index.md) | ✅ | Applied | Preserve sole C1-R/schema/state/CLI owners, exact anchor, public/private parser split, and non-authentication. |
| 18 | [D59](../../../knowledge-index.md) | ✅ | Applied | Extend the Phase B router with transport/status only; preserve seven operation outcomes and F26. |
| 19 | [Commit Identity conventions](../../../reference/conventions.md#commit-identity-and-attribution) | ✅ | Applied | Existing field, trailer, reserved-form, replay, guarded-none, and truth-boundary rules remain binding. |
| 20 | [Proof Record conventions](../../../reference/conventions.md#proof-records-and-claim-boundaries) | ✅ | Applied | `PR-C1`–`PR-C12` will resolve Local/Seam/Live claims and complete debt/limitations. |
| 21 | [File Classification](../../../reference/conventions.md#file-classification-in-tfw) | ✅ | Applied | Template, tracked project state, private clone state, and upstream update source remain distinct owners. |
| 22 | [Safety and Execution Honesty](../../../reference/conventions.md#safety-and-execution-honesty) | ✅ | Applied | Current-repository mutation is delayed to the approved live gate with exact rollback and no prohibited inspection. |
| 23 | [Role Lock Protocol](../../../reference/conventions.md#15-role-lock-protocol) | ✅ | Applied | Executor writes only ONB, approved consumers, EV/RF, and Task Board; Reviewer owns independent acceptance. |
| 24 | [Phase A RF](../phase-a/RF__phase-a__canonical_contract_and_validator.md) | ✅ | Applied | Current owner behavior and corrected diagnostics/public-context boundaries are protected regressions. |
| 25 | [Phase A REVIEW](../phase-a/REVIEW__phase-a__canonical_contract_and_validator.md) | ✅ | Applied | APPROVE establishes Phase A facts but not Phase C runtime completion. |
| 26 | [Phase B RF](../phase-b/RF__phase-b__workflow_and_adapter_consumption.md) | ✅ | Applied | Router map, seven operations, parity, and local/publication split are current inputs. |
| 27 | [Phase B REVIEW](../phase-b/REVIEW__phase-b__workflow_and_adapter_consumption.md) | ✅ | Applied | APPROVE protects router ownership, exact parity, and non-publication behavior. |
| 28 | [Iteration 1 RES](../research/iter1/RES.md) | ✅ | Applied | Use the challenged no-proxy local runtime, explicit replay, exact audit, and non-authentication boundary; open platform/range threads become Phase C proof. |

No new knowledge item was found. The private-ledger and publication requirements are
applications of D58/D59, philosophy F23, and process F26 rather than new Fact
Candidates.

---

*ONB — TFW-49 / Phase C: Repository-Local Enforcement, Migration, and Cross-Agent Proof | 2026-07-31*
