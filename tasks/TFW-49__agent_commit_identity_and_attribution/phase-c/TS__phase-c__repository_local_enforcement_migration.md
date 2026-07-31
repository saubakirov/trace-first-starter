# TS — TFW-49 / Phase C: Repository-Local Enforcement, Migration, and Cross-Agent Proof

> **Date**: 2026-07-31
> **Author**: Coordinator (Codex)
> **Status**: ✅ TS — Approved for execution under delegated owner authority
> **Parent HL**: [Phase C HL](HL__phase-c__repository_local_enforcement_migration.md)
> **Master HL**: [TFW-49](../HL-TFW-49__agent_commit_identity_and_attribution.md)
> **Research**: [Iteration 1 RES](../research/iter1/RES.md) — SUFFICIENT
> **Phase A authority**: [RF](../phase-a/RF__phase-a__canonical_contract_and_validator.md) /
> [APPROVE REVIEW](../phase-a/REVIEW__phase-a__canonical_contract_and_validator.md)
> **Phase B authority**: [RF](../phase-b/RF__phase-b__workflow_and_adapter_consumption.md) /
> [APPROVE REVIEW](../phase-b/REVIEW__phase-b__workflow_and_adapter_consumption.md)
> **Execution approval**: 2026-07-31
> **Publication**: NOT AUTHORIZED — process F26 remains binding

---

## 1. Objective

Deliver the repository-local runtime and lifecycle that make the Phase A C1-R
contract and Phase B operation router observable at the Git action boundary. Phase C
must install, verify, repair, and exactly roll back only TFW-owned local hook state;
support clean new-project activation and exact existing-history ranges; transport
explicit expected context only to an allowlisted local Git child operation; and make
handoff, independent review, and release preparation prove the complete state-owned
range.

The implementation must install the runtime in this repository and prove it on the
declared Windows and Ubuntu WSL Git/Python boundary. Real client support is limited to
independent Codex Executor and Reviewer sessions using the TFW runtime and Git CLI.
Other registered surfaces receive synthetic contract coverage or structural copy
parity only. No task, phase, local commit, tag, review, docs, or knowledge result
authorizes push or any other remote publication.

## 2. Scope

### In Scope

- Upgrade the Commit Identity contract to exact semantic version `1.1.0` without
  changing C1-R field meaning or creating another accepted grammar.
- Add `root-inclusive` activation beside `exclusive-anchor`, with exact null/full-OID
  invariants and fail-closed range traversal.
- Create a clean project-state template; make full init derive destination state from
  it; preserve existing project activation through update.
- Refactor tracked `hook_runtime` to own only the required runtime version and
  canonical relative source, with no clone-local installed boolean.
- Create one standard-library hook lifecycle owner, one recognized manifest, and only
  the `prepare-commit-msg` and `commit-msg` versioned hook entries.
- Store observed installation and exact opaque prior local `core.hooksPath`
  presence/value only in
  `<git-common-dir>/tfw/commit_identity_runtime.json`.
- Install/verify/repair/rollback only recognized TFW-owned runtime through
  repository-local `core.hooksPath=.tfw/hooks`, including main and linked worktrees.
- Extend the Phase B router with an exact expected-context token and required-runtime
  status without inferring live installation from tracked state.
- Provide an allowlisted, command-scoped local Git carrier for
  `TFW_COMMIT_EXPECTED_CONTEXT`; keep its internal function/subcommand spelling
  adaptable and keep operation/grammar authority in existing owners.
- Validate prepare-stage structure/context non-mutatingly and final subject/trailers
  through the existing contract, including all seven Phase B operation classes.
- Integrate runtime lifecycle and exact range gates into init, update, handoff,
  review, and release, then synchronize only their exact Antigravity and Claude copies.
- Install the owned runtime in this repository and exercise real local Phase C commits
  through independent Codex Executor and Reviewer sessions.
- Prove Windows Git `2.42.0.windows.1` / Python `3.13.5`, Ubuntu WSL Git `2.43.0` /
  Python `3.12.3`, four registered surfaces × four roles synthetically, exact topology,
  replay/context, ownership, redaction, rollback, and no-publication boundaries.

### Out of Scope

- Any change to adapter entry templates, root `AGENTS.md` or `CLAUDE.md`, Codex skill
  sources/installed copies, unrelated workflows, Cursor installation, project config
  values/templates, knowledge, versions, changelog, release markers, or prior history.
- Reading, resolving, revealing, executing, copying, fingerprinting, chaining,
  overwriting, removing, or mutating any external/global hook path/body/value/config.
- Persistent shared expected-context files or variables, a second operation router,
  another grammar/registry/parser, hosted identity, actor authentication, or Git
  authorship changes.
- Live Antigravity, Claude Code, Cursor, GUI, IDE, JGit, hosted-provider, or CI support
  claims unless a genuinely independent matching client is actually exercised and the
  Coordinator explicitly revises this TS.
- Historical relabeling, force update, remote branch/tag mutation, push, deploy,
  publish, notify, host escalation, or external credential remediation.
- Treating hook/file presence, a synthetic matrix, an Executor attestation, or a
  recent/partial commit sample as independent acceptance.

### Acceptance-Critical Precision

- Contract version is exactly `1.1.0`.
- C1-R remains exactly `[surface/task/work/role] summary`; schema remains the sole
  registry/pattern/form/trailer/truth-boundary owner.
- `exclusive-anchor` requires a full lowercase 40-hex
  `last_pre_policy_commit`, excludes that object, and audits every reachable
  descendant through the target.
- `root-inclusive` requires `last_pre_policy_commit:null`; after a target exists it
  audits every commit reachable from the target including every root. An unborn/no
  target repository is install-ready but returns a stable no-target range failure.
- This project preserves
  `f1106186417e84cdb38e797f7af66a60885bad76` as its exact exclusive anchor.
- The project-state template contains no starter-repository anchor and no observed
  installed truth. Update never copies or overwrites tracked project state/activation.
- Tracked `hook_runtime` owns only required runtime version and canonical relative
  source. The private Git-common-dir ledger exclusively owns observed installation and
  exact opaque prior local presence/value.
- Versioned runtime targets are exactly `.tfw/hooks/runtime.json`,
  `.tfw/hooks/prepare-commit-msg`, and `.tfw/hooks/commit-msg`.
- Persistent Git mutation is only
  `git config --local core.hooksPath .tfw/hooks`; rollback restores the exact prior
  local value or unsets the key.
- Expected context is transported only as a complete
  `TFW_COMMIT_EXPECTED_CONTEXT=surface/task/work/role` value for an allowlisted local
  Git child operation. Partial/malformed context fails; absent context is an explicit
  structural-only, non-authenticated limitation.
- Handoff, review, and release use the state-owned exact range. Review is independent;
  release rechecks before local preparation and before any separately authorized
  publication.
- Live supported client is Codex + TFW runtime + Git CLI only. All other client or
  authentication claims are N/A/non-claims unless separately authorized and observed.
- `origin/master` remains
  `b4c0a06dc9fbc104c5b8997865b6df3211bd5c0c`; no remote mutation is allowed.

## 3. Principles Check

| # | Principle from Phase HL §7 | Enforced by | Gate |
|---|----------------------------|-------------|------|
| P1 | Product value before mechanism | AC-8, AC-11 | Action-local provenance and independent full-range outcome, not hook presence |
| P2 | One semantic owner | AC-1, AC-5, AC-6 | Schema/state/CLI/router source and mutation tests; no duplicate registry/router |
| P3 | Tracked requirement, private reality | AC-1, AC-4 | State-shape tests and Git-common-dir ledger inspection |
| P4 | No contaminated templates | AC-1, AC-7 | Unborn/existing init fixtures and update preservation comparison |
| P5 | Repository-local means repository-local | AC-3, AC-4, AC-10 | Local-only command spy, conflict matrix, and global/external non-access proof |
| P6 | Explicit context or honest limitation | AC-5, AC-6 | Complete/partial/malformed/absent context matrix |
| P7 | Hooks are visibility, not identity proof | AC-3, AC-6, AC-11 | Bypass disclosures, `actor_authentication:false`, and claim scan |
| P8 | Exact history over convenient samples | AC-2, AC-8, AC-11 | Exact DAG enumeration, failure topology, and independent rerun |
| P9 | Independent judgment | AC-8, AC-11, AC-12 | Reviewer-owned lifecycle/range execution and REVIEW boundary |
| P10 | Real proof stays real | AC-10, AC-11 | Separate synthetic, structural-parity, platform, and live-client dispositions |
| P11 | Reversibility includes secrecy | AC-4, AC-10 | Opaque prior-value rollback and redaction canaries |
| P12 | Publication is separate authority | AC-5, AC-8, AC-11 | Carrier allowlist, workflow hard stops, remote OID comparison |

## 4. Affected Files

### Create — six framework owners

| File | Action | Description |
|------|--------|-------------|
| `.tfw/templates/commit_identity_state.json` | CREATE | Clean project-state source with destination-derived activation and no clone-local installed truth |
| `.tfw/scripts/commit_identity_hooks.py` | CREATE | Standard-library install/verify/repair/rollback, command carrier, prepare, and final lifecycle owner |
| `.tfw/scripts/test_commit_identity_hooks.py` | CREATE | Isolated Git/platform/topology/context/ownership/security/lifecycle proof |
| `.tfw/hooks/runtime.json` | CREATE | Recognized TFW runtime manifest/version/owned-target source |
| `.tfw/hooks/prepare-commit-msg` | CREATE | Portable non-mutating prepare-stage entry |
| `.tfw/hooks/commit-msg` | CREATE | Portable final subject/trailer validation entry |

### Modify — eight contract/runtime consumers

| File | Action | Description |
|------|--------|-------------|
| `.tfw/commit_identity.schema.json` | MODIFY | Contract `1.1.0`; root-inclusive/exclusive and tracked/private runtime semantics |
| `.tfw/commit_identity_state.json` | MODIFY | Preserve exact current anchor; required runtime/version/source only |
| `.tfw/scripts/commit_identity.py` | MODIFY | Validate new state and audit exact root-inclusive/exclusive ranges |
| `.tfw/scripts/test_commit_identity.py` | MODIFY | State/template/range/topology/mutation regressions |
| `.tfw/scripts/commit_identity_router.py` | MODIFY | Emit complete expected-context token and required-runtime status without live-state inference |
| `.tfw/scripts/test_commit_identity_router.py` | MODIFY | Token/status/operation/persistence/publication regressions |
| `.tfw/conventions.md` | MODIFY | Canonical state split, runtime lifecycle, context, client, audit, and F26 boundaries |
| `.tfw/glossary.md` | MODIFY | Concise owner-linked terms without duplicated registries or lifecycle algorithms |

### Modify — five canonical lifecycle/audit workflows

| File | Action | Description |
|------|--------|-------------|
| `.tfw/workflows/init.md` | MODIFY | Derive tracked state from template; install and verify local runtime |
| `.tfw/workflows/update.md` | MODIFY | Preserve state; repair recognized versioned runtime after ownership checks; exact rollback |
| `.tfw/workflows/handoff.md` | MODIFY | Router + command carrier for local commit; exact range attestation; F26 stop |
| `.tfw/workflows/review.md` | MODIFY | Independent lifecycle verify and exact range before verdict |
| `.tfw/workflows/release.md` | MODIFY | Verify/range before local release preparation and before separately authorized publication |

### Modify — five exact Antigravity copies

| File | Action | Description |
|------|--------|-------------|
| `.agent/workflows/tfw-init.md` | MODIFY | Exact copy of canonical init |
| `.agent/workflows/tfw-update.md` | MODIFY | Exact copy of canonical update |
| `.agent/workflows/tfw-handoff.md` | MODIFY | Exact copy of canonical handoff |
| `.agent/workflows/tfw-review.md` | MODIFY | Exact copy of canonical review |
| `.agent/workflows/tfw-release.md` | MODIFY | Exact copy of canonical release |

### Modify — five exact Claude Code copies

| File | Action | Description |
|------|--------|-------------|
| `.claude/commands/tfw-init.md` | MODIFY | Exact copy of canonical init |
| `.claude/commands/tfw-update.md` | MODIFY | Exact copy of canonical update |
| `.claude/commands/tfw-handoff.md` | MODIFY | Exact copy of canonical handoff |
| `.claude/commands/tfw-review.md` | MODIFY | Exact copy of canonical review |
| `.claude/commands/tfw-release.md` | MODIFY | Exact copy of canonical release |

The Executor additionally creates Phase C ONB, EV, and RF traces and modifies only the
TFW-49 Task Board row as lifecycle state. Those four paths are outside the
29-framework-consumer measurement. Reviewer-owned files, docs/knowledge closure, and
this approved HL/TS are not Executor write scope.

**Scope-attention measurement:** exact path allowlist plus physical changed-line
measurement: 29 framework files, 6 new files, 23 modified files, estimated
2,600–3,600 changed framework LOC. Current configured signals are 14 files, 8 new
files, 1,200 LOC, and 12 modified files.

**Response:** bounded cohesion override. New-file count stays below its signal; total
files, modified files, and LOC cross attention signals. The 29 paths form one
indivisible value/proof seam: contract/state → router/context → recognized hook runtime
→ init/update lifecycle → handoff/review/release acceptance → exact derived copies.
Splitting would leave project state, live installation, commit execution, or
independent acceptance semantically inconsistent. No 30th framework path is allowed
without returning to the Coordinator; actual counts remain descriptive rather than
quality, completion, or automatic-split evidence.

## 5. Acceptance Criteria

### Acceptance-Critical Order

Execute and prove in dependency order:

```text
AC-1 state/contract
  → AC-2 exact range
  → AC-3 owned portable runtime
  → AC-4 private lifecycle
  → AC-5 router/carrier
  → AC-6 prepare/final operations
  → AC-7 init/update
  → AC-8 handoff/review/release gates
  → AC-9 derived parity
  → AC-10 platform/topology/security matrix
  → AC-11 current-repo live cross-session proof
  → AC-12 regression/traces
```

### AC-1: Contract 1.1.0 and Project-Safe State

The existing C1-R owner supports clean destination-derived activation and separates
portable project requirements from clone-local runtime observations.

- **Intent / authority:** Phase C HL DoD 1–3; D58/D59; philosophy F23; delegated owner
  state-split decision.
- **Claim:** Schema, tracked current-project state, and the new state template agree on
  contract `1.1.0`, exact activation modes, required runtime/version/source, and the
  non-authentication boundary without a clone-local installed boolean or starter-state
  contamination.
- **Boundary:** Local schema/state/validator/template; crossed framework-to-destination
  init boundary; Phase A compatibility.
- **Precision:** Exact `1.1.0`; C1-R unchanged; `exclusive-anchor` ↔ full lowercase
  40-hex; `root-inclusive` ↔ `null`; current project anchor exact; tracked
  `hook_runtime` contains required version + canonical relative source only.
- **Proof intent:** Local Proof from schema/state mutation and source-ownership tests;
  Seam Proof comparing template, current state, validator, init contract, D58/D59, and
  Phase A regressions.
- [ ] Schema is the only accepted registry/pattern/form/trailer/truth-boundary owner
      and rejects every invalid/missing downstream-consumed 1.1.0 field with stable
      field-specific diagnostics.
- [ ] Template has no TFW starter anchor, no observed installed value, no absolute
      path, and a valid root-inclusive/null clean activation.
- [ ] Current tracked state keeps the exact exclusive `f110618...` anchor and declares
      only portable runtime requirements.
- [ ] Removing/mutating each required schema/state/template owner changes or rejects
      behavior without adding a Python registry.

Gate: JSON parsing plus exhaustive field-removal/semantic-mutation and
schema-template-current-state comparison protects the single-owner and
non-contamination claim.

Evidence: N/A — state ownership and serialization are fully established by Local and
Seam Proof; no intended-environment observation beyond AC-7/AC-11 is triggered.

Proof Record: `PR-C1`.

### AC-2: Exact Exclusive and Root-Inclusive Range Semantics  [depends: AC-1]

The contract audits the entire prospective policy population for existing and fresh
repositories and fails closed when the range cannot be proven.

- **Intent / authority:** Phase C HL DoD 1/8; RES Open Thread 1; D58 exact-range
  requirement.
- **Claim:** Exclusive mode excludes its valid anchor and includes every reachable
  descendant; root-inclusive mode with null anchor includes every commit reachable
  from target including all roots; no-target, incomplete, missing, shallow, invalid,
  or non-ancestor states cannot become a valid result.
- **Boundary:** Local contract CLI ↔ real Git object graph; existing/unborn/root/merge/
  linked/shallow/missing/non-ancestor histories; Phase A exclusive-range compatibility.
- **Precision:** Exact mode/anchor invariants; stable no-target failure for unborn
  history; no recent-count/branch-tip/sample fallback; each reachable commit counted
  once.
- **Proof intent:** Local Proof from exact temporary DAG enumeration; Seam Proof
  between state semantics, Git graph output, and audit result.
- [ ] Root-inclusive fixtures cover one root, multiple roots reachable through merge,
      ordinary descendants, and target inclusion.
- [ ] Exclusive fixtures prove anchor exclusion, all descendant inclusion, merge
      deduplication, and current `f110618...` compatibility.
- [ ] Unborn/no target is install-ready but returns the stable no-target range failure.
- [ ] Shallow/incomplete/missing target/missing anchor/invalid OID/non-ancestor and
      inconsistent mode-anchor pairs fail closed without a fallback.
- [ ] Audit output keeps `actor_authentication:false` and reveals no arbitrary subject
      or unsafe repository path.

Gate: Fixture DAG enumeration compared commit-for-commit with CLI output protects the
population and topology claim.

Evidence: N/A — temporary Git graphs establish Local/Seam Proof; current-repository
live observation is triggered separately by AC-11.

Proof Record: `PR-C2`.

### AC-3: Recognized Portable TFW Hook Runtime  [depends: AC-1]

The versioned runtime contains one recognized manifest and only the two approved thin
Git hook entries, with validation logic delegated to the standard-library owner.

- **Intent / authority:** Phase C HL scope C2–C6; RES challenged no-proxy runtime;
  portability and one-owner Project Values.
- **Claim:** Runtime manifest, prepare entry, final entry, and lifecycle source are
  mutually consistent, relative, portable, executable by declared Git/Python
  environments, and distinguish recognized TFW material from unknown/conflicting
  targets.
- **Boundary:** Versioned manifest ↔ two hook entries ↔ lifecycle executable ↔ Git for
  Windows and Ubuntu WSL launch behavior.
- **Precision:** Exact targets `runtime.json`, `prepare-commit-msg`, `commit-msg`;
  runtime/contract `1.1.0`; no other reserved hook target; no absolute path or
  external-hook chaining/proxy metadata.
- **Proof intent:** Local Proof from manifest/source/entry inspection and launch tests;
  Seam Proof across versioned targets and both declared platforms.
- [ ] Missing/unknown manifest, wrong runtime/version/source, missing owned target,
      changed recognized target, or unexpected reserved-target material blocks verify,
      repair, and install as applicable.
- [ ] Hook entries are thin, non-secret, repository-relative, and contain no second
      parser/registry/operation policy.
- [ ] Versioned files contain no developer absolute path and launch under both
      declared Git/Python combinations in isolated repositories.
- [ ] Runtime recognition hashes/compares only TFW-owned manifest/material and never
      reads or fingerprints any external/global hook.

Gate: Manifest mutation, owned-target inventory, import/source scan, executable launch,
and cross-platform fixtures protect ownership and portability.

Evidence: Observe actual hook invocation in both declared Git/Python environments.
If either declared boundary cannot execute, record complete Value Debt and do not
claim that platform as supported.

Proof Record: `PR-C3`.

### AC-4: Local Install, Verify, Repair, and Exact Rollback  [depends: AC-1, AC-3]

One idempotent lifecycle manages only the recognized runtime and repository-local Git
override while keeping live/rollback truth private to the Git common directory.

- **Intent / authority:** Phase C HL DoD 3–5/11; user per-repository direction;
  process F26 and safety boundary.
- **Claim:** Install, verify, repair, and rollback preserve TFW ownership, use only
  local `core.hooksPath=.tfw/hooks`, share one common-dir ledger across main/linked
  worktrees, and restore exact prior local presence/value without disclosure.
- **Boundary:** Versioned runtime ↔ repository-local Git config ↔ private
  `<git-common-dir>/tfw/commit_identity_runtime.json` ↔ main/linked worktrees;
  recognized upstream/framework repair source.
- **Precision:** Only `git config --local`; exact relative value `.tfw/hooks`; exact
  prior local value/presence stored opaquely; no global/external query; unknown material
  blocks; repeated actions are idempotent.
- **Proof intent:** Local Proof from lifecycle state machine and isolated config/runtime
  fixtures; Seam Proof across versioned owners, Git local config, private ledger,
  upstream recognized repair source, and linked worktrees; Live Proof in AC-11.
- [ ] Unset and synthetic opaque prior local values install, verify, and rollback to
      exact unset/value respectively without printing or resolving the value.
- [ ] Install/install, verify/verify, repair/repair, and rollback/rollback are
      idempotent with stable dispositions.
- [ ] Owned missing/broken runtime repairs from recognized framework/upstream owners
      only after ownership checks; unknown manifest/material blocks and is untouched.
- [ ] Main and linked worktrees resolve one common-dir ledger and agree on install,
      verify, repair, and rollback outcomes.
- [ ] Command spies/source scans prove no `--global`, external hook/config discovery,
      path/body/value/fingerprint access, remote command, or history rewrite.

Gate: Isolated lifecycle transition matrix plus exact before/after local-config and
private-ledger comparison protects reversibility, secrecy, and ownership.

Evidence: Observe install → verify → repair → rollback in actual declared Git
environments without exposing the private prior value. Current-repository live
installation remains AC-11.

Proof Record: `PR-C4`.

### AC-5: Router-Derived Command-Scoped Git Carrier  [depends: AC-1, AC-4]

The Phase B router provides complete expected context and required-runtime status to a
bounded carrier that launches only an allowlisted local Git child operation.

- **Intent / authority:** Phase C HL DoD 6; D59 router ownership; F26 publication
  separation.
- **Claim:** Router output includes exact expected-context token and required-runtime
  status without inferring live installation; the carrier sets context only for the
  child process, never persists it, and cannot execute publication or become another
  operation/grammar owner.
- **Boundary:** Phase B router ↔ lifecycle carrier ↔ child Git environment ↔ prepare/
  final hooks; local process and publication authority.
- **Precision:** Exact environment name `TFW_COMMIT_EXPECTED_CONTEXT`; complete
  `surface/task/work/role` token; allowlisted local operations cover the seven Phase B
  classes; push/fetch/remote/tag publication/deploy/publish/notify are forbidden.
  Internal function/subcommand/argument spelling is adaptable.
- **Proof intent:** Local Proof from router/carrier unit and process-environment tests;
  Seam Proof across schema, state, router, carrier, hook child, and workflow consumers.
- [ ] Router derives token from explicitly validated workflow context and never from
      branch, prior subject, path coincidence, model, session, tracked installed value,
      or mutable shared state.
- [ ] Carrier rejects missing/partial/malformed router plans, wrong runtime requirement,
      unknown operation, remote/publication command, and non-local target.
- [ ] Expected context exists only in the allowlisted child environment and is absent
      from parent/persistent tracked/private state after completion/failure.
- [ ] Operation disposition, subject, trailers, `task:none`, and source relations
      remain owned by Phase A/Phase B; carrier transports without re-deciding them.
- [ ] Output retains `publication_authority:false` and
      `actor_authentication:false`.

Gate: Environment-lifetime, allowlist, router mutation, subprocess-spy, and prohibited
command matrix protects explicit context and publication boundaries.

Evidence: N/A — process transport is Local/Seam Proof; actual routed commits are
observed in AC-11.

Proof Record: `PR-C5`.

### AC-6: Non-Mutating Prepare and Final Validation  [depends: AC-3, AC-5]

The two Git entries consume the existing contract truthfully across ordinary and
reserved operations without inventing or leaking context.

- **Intent / authority:** Phase C HL DoD 6–7; RES sequencer correction; Phase B
  operation contract.
- **Claim:** Prepare structurally validates the owned current message input without
  rewriting it; complete expected context is exact-compared, partial/malformed context
  fails, and absent context is a visible structural-only non-authenticated limitation.
  Final validation checks subject, trailers, and expected context when present.
- **Boundary:** Current Git message file ↔ prepare/final entries ↔ contract parser/
  validator ↔ command-scoped expected context; seven operation classes.
- **Precision:** Message bytes unchanged by prepare; complete four-field equality;
  stable absent/partial/stale diagnostics; schema-owned trailer names/values;
  ordinary, merge, amend, fixup, squash, revert, cherry-pick behavior matches Phase B.
- **Proof intent:** Local Proof from byte-before/after and positive/negative hook
  fixtures; Seam Proof across router plan, child context, Git hook invocation, final
  commit object, and Phase B operation decisions.
- [ ] Prepare leaves the message file byte-identical on success and failure.
- [ ] Complete current context passes; each stale field, partial token, malformed
      token, unknown field, or prohibited cross-context operation fails with stable
      safe diagnostics.
- [ ] Absent expected context can pass structural validation only and produces an
      explicit limitation that is never described as exact or authenticated context.
- [ ] Final validation covers ordinary subject and all permitted schema-owned
      trailers, rejects malformed/duplicate/unsafe provenance, and compares expected
      context when present.
- [ ] Same-context reserved forms and cross-context no-commit/current-operator replay
      remain exactly Phase B compatible across all seven operations.
- [ ] Parsing the owned current commit-message input is allowed, but tests import no
      real arbitrary/sensitive corpus and diagnostics never echo, retain, or disclose
      arbitrary message/body/environment/hook/secret canaries.

Gate: Temporary Git hook executions, message-byte comparison, seven-operation matrix,
context mutation, trailer matrix, and redaction canaries protect non-mutation,
truthfulness, and secrecy.

Evidence: Observe actual accepted and rejected commits in both declared Git/Python
environments. Evidence supports only structural/runtime behavior, not actor identity.

Proof Record: `PR-C6`.

### AC-7: Init and Update Preserve Project State  [depends: AC-1, AC-4]

Canonical lifecycle workflows create destination-owned state and install or repair the
recognized runtime without importing upstream project state.

- **Intent / authority:** Phase C HL DoD 2/4; philosophy F23; `/tfw-init` and
  `/tfw-update` ownership.
- **Claim:** Full init derives unborn/root-inclusive or existing-history/
  exclusive-anchor state from the destination and installs/verifies runtime; update
  never copies/overwrites tracked project state or activation and repairs only
  recognized versioned runtime after ownership checks.
- **Boundary:** State template ↔ destination Git history ↔ init workflow ↔ tracked
  project state ↔ update upstream/framework source ↔ local runtime lifecycle.
- **Precision:** Unborn = null/root-inclusive; existing history = full current
  last-pre-policy OID/exclusive unless an approved state already exists; update
  preserves every project-owned activation field byte/semantically; unknown material
  blocks.
- **Proof intent:** Local Proof from workflow/source checks and isolated init/update
  fixtures; Seam Proof across template, destination, tracked state, lifecycle, upstream
  source, and exact derived copies.
- [ ] Full init on unborn and existing-history repositories produces the correct
      destination-derived state and recognized local runtime.
- [ ] Existing TFW attach/repair preserves project state and uses lifecycle verify/
      repair rather than rerunning discovery or replacing activation.
- [ ] Update state classification explicitly includes Commit Identity tracked project
      state and never sources it from upstream; recognized runtime files may update
      only after ownership checks.
- [ ] Unknown/missing manifest or reserved-target conflict returns a blocking
      disposition without synthesizing or overwriting unknown material.
- [ ] Current repository retains exact `f110618...` through init/update proof.

Gate: Temporary full-init/attach/update source comparisons and before/after state hashes
protect destination ownership and migration safety.

Evidence: N/A — workflow/state behavior is proved in isolated repositories; actual
current-repository installation is observed under AC-11.

Proof Record: `PR-C7`.

### AC-8: Handoff, Independent Review, Release, and F26 Gates  [depends: AC-2, AC-4, AC-5, AC-6]

The three action/acceptance workflows use the same runtime and exact range while
retaining distinct Executor, Reviewer, release, and publication authorities.

- **Intent / authority:** Phase C HL DoD 8/13; D57 evidence/attestation boundary; D59
  workflow routing; process F26.
- **Claim:** Handoff routes each local commit through the carrier and records an exact
  range attestation; review independently verifies lifecycle and reruns the exact
  range before verdict; release verifies/reruns before local preparation and again
  before any separately authorized publication. No workflow treats local completion
  as publication authority.
- **Boundary:** Router/carrier/runtime ↔ Executor handoff/RF ↔ Reviewer REVIEW ↔ release
  preparation ↔ remote publication authority.
- **Precision:** State-owned exact range only; lifecycle verify + audit before REVIEW
  verdict; release pre-preparation and pre-publication gates; F26 exact later
  `APPROVE PUSH`; no recent/sample fallback or self-attested acceptance.
- **Proof intent:** Local Proof from workflow text/scenario tests; Seam Proof across
  workflow roles, runtime, range output, RF/REVIEW/release gates, and F26; Live Proof
  from real Executor/Reviewer commits in AC-11.
- [ ] Handoff's local commit action consumes router + carrier and its RF includes the
      post-commit exact range result and `actor_authentication:false`.
- [ ] Review independently runs lifecycle verify and exact audit after all Executor
      commits and before deciding APPROVE/REVISE/REJECT.
- [ ] Release runs lifecycle verify + exact range before modifying local release
      artifacts and again immediately before any separately authorized publication.
- [ ] Missing runtime, invalid range, unpublished current commit, local dirt, or
      incomplete/unsupported result blocks the applicable authority transition.
- [ ] Push, remote tag, deploy, publish, notify, and host escalation remain unavailable
      for TFW-49; local commit/tag language is distinct.

Gate: Workflow scenario assertions, exact command/source checks, role-owned range
reruns, and remote-OID/no-publication comparison protect authority separation.

Evidence: Observe independent Executor and Reviewer local workflow use in AC-11.
Release publication remains N/A because F26 forbids it; this N/A waives no local
verify/range proof.

Proof Record: `PR-C8`.

### AC-9: Exact Canonical and Derived Workflow Parity  [depends: AC-7, AC-8]

Only the five changed canonical lifecycle/audit workflows and their ten installed
Antigravity/Claude copies move together.

- **Intent / authority:** D54 behavioral parity; Phase C exact 29-path inventory;
  no-consumer-inflation decision.
- **Claim:** Init/update/handoff/review/release canonical owners contain the Phase C
  lifecycle/gates and each corresponding Antigravity/Claude copy is byte-exact; Codex
  skills/entry templates, Cursor, and unrelated workflows remain unchanged.
- **Boundary:** Five canonical sources ↔ ten installed derived copies ↔ protected
  adapter/skill/template consumers.
- **Precision:** Exact five names × two derived surfaces; byte equality; no Codex skill
  or entry-template path; no runtime-support inference from parity.
- **Proof intent:** Local Proof from exact path and byte comparisons; Seam Proof
  between canonical and derived copies; explicit N/A for live non-Codex clients.
- [ ] Canonical-to-Antigravity equality is 5/5 and canonical-to-Claude equality is 5/5.
- [ ] Exact framework diff is 6 CREATE + 23 MODIFY; no 30th path.
- [ ] Codex skill source/installed copies, adapter entry templates, root entries,
      Cursor paths, and six unrelated workflows are byte-unchanged/absent as declared.
- [ ] RF and REVIEW label parity as structural only, never live Antigravity/Claude
      runtime support.

Gate: Exact allowlist, byte comparison, protected-path hashes, and claim-language scan
protect synchronization without consumer inflation.

Evidence: N/A — source/copy parity is structural Seam Proof. No live Antigravity or
Claude client is available or required.

Proof Record: `PR-C9`.

### AC-10: Cross-Platform, Topology, Security, and Operation Matrix  [depends: AC-2, AC-3, AC-4, AC-5, AC-6]

The complete temporary-repository matrix demonstrates the declared runtime boundary
without using production-sensitive inputs.

- **Intent / authority:** Phase C HL DoD 9–10; RES platform/client limitation;
  safety/portability Project Values.
- **Claim:** Windows and Ubuntu WSL execute the same contract/runtime outcomes across
  state/range, lifecycle, worktree, hook/context, operations, identity registries,
  bypass disclosure, and redaction scenarios.
- **Boundary:** Windows Git/Python ↔ Ubuntu WSL Git/Python; temporary Git repositories;
  main/linked worktrees; schema/router/runtime/lifecycle; synthetic surface/role values.
- **Precision:** Windows Git `2.42.0.windows.1` / Python `3.13.5`; Ubuntu WSL Git
  `2.43.0` / Python `3.12.3`; four surfaces × four roles; seven operations; exact
  required scenario families below.
- **Proof intent:** Local Proof from version-pinned automated runs; Seam Proof across
  platforms and owners; Live Proof only for runtime behavior in the declared
  environments, never client identity.
- [ ] Range families: exclusive, root-inclusive, root, multi-root merge, unborn/no
      target, missing, invalid, non-ancestor, incomplete/shallow, no fallback.
- [ ] Lifecycle families: unset and opaque prior local values, recognized/unowned
      conflict, missing/broken owned runtime, idempotent install/verify/repair/rollback,
      exact restore/unset, main/linked common-dir.
- [ ] Hook/router families: complete/partial/malformed/absent/stale context, prepare/
      final, ordinary/merge/amend/fixup/squash/revert/cherry-pick, `task:none`,
      trailers, mixed origins, carrier allowlist, no persistence/publication.
- [ ] Registry/client families: all four surfaces × four roles synthetically; no fake
      client operation or authentication claim.
- [ ] Security families: synthetic redaction canaries, arbitrary message/body/
      environment/hook/secret non-disclosure, no global/external query, no absolute
      path, no remote/history mutation.
- [ ] Platform outputs and versions are captured reproducibly in `PR-C10`; any
      unsupported result creates complete Value Debt and narrows the support claim.

Gate: Version-pinned automated matrix, command spy, temp-root containment, canary
absence, and cross-platform result comparison protect declared support and safety.

Evidence: Observe the same acceptance/rejection/lifecycle outcomes on both declared
Git/Python environments. A missing platform result is not `N/A`; it requires Value
Debt or removal of that support claim.

Proof Record: `PR-C10`.

### AC-11: Current-Repository Installation and Independent Codex Proof  [depends: AC-1, AC-2, AC-3, AC-4, AC-5, AC-6, AC-7, AC-8, AC-9, AC-10]

The actual TFW repository adopts its owned runtime locally and produces independently
operated, completely audited Phase C history without publication.

- **Intent / authority:** User authorized actual Phase C install and independent
  Codex sessions; Phase C HL DoD 11/13; process F26.
- **Claim:** Current repository preserves exact activation state, installs/verifies
  relative local runtime, and includes real C1-R Executor and Reviewer local commits
  whose full exact range is independently valid. Remote/global/history boundaries
  remain unchanged.
- **Boundary:** Current tracked owners ↔ current local Git config/private ledger ↔
  independent Codex Executor and Reviewer sessions ↔ complete `f110618...HEAD` range ↔
  protected origin/global/history state.
- **Precision:** Existing anchor exact; local `core.hooksPath=.tfw/hooks`; at least one
  real Executor commit and one independent Reviewer commit; live support claim Codex +
  TFW runtime + Git CLI only; origin exact `b4c0a06...`; no push.
- **Proof intent:** Local Proof from installed owners/config/ledger and exact audit;
  Seam Proof across sessions, roles, commit subjects, runtime, RF/REVIEW, and remote
  boundary; Live Proof from actual current-repository hook executions and independent
  session observations.
- [ ] Install uses the authorized lifecycle, leaves tracked project state correct,
      writes only private clone-local ledger outside versioned scope, and verifies the
      recognized runtime.
- [ ] Executor creates actual Phase C local commits via router + carrier; RF records
      post-commit exact audit and limitations.
- [ ] A separate Codex Reviewer session independently verifies runtime/range and
      creates its own valid Reviewer local commit before final closure.
- [ ] Exact range includes every post-anchor local commit through current target and
      reports `actor_authentication:false`.
- [ ] Synthetic four-surface/four-role results and structural Antigravity/Claude parity
      remain separate from the live Codex claim; Cursor/GUI/IDE/JGit/hosted are N/A.
- [ ] Safe before/after proof establishes local state change and no global command/
      external-hook access, no history rewrite, no remote mutation, and
      `origin/master=b4c0a06...` without reading global path/body/value.

Gate: Actual local install/verify, two independent session operations, exact full-range
enumeration, protected-path/config/remote OID comparison, and claim-boundary audit
protect the live result.

Evidence: VERIFIED only if actual current-repository install and independent Codex
Executor/Reviewer local operations are observed with resolvable artifacts. Any missing
declared live boundary becomes complete Value Debt and blocks full Phase C approval.

Proof Record: `PR-C11`.

### AC-12: Regression, Exact Scope, Evidence, and Coordinator Handoff  [depends: AC-1, AC-2, AC-3, AC-4, AC-5, AC-6, AC-7, AC-8, AC-9, AC-10, AC-11]

The full result remains within the approved owners, preserves prior contracts, and
hands independent review a reproducible claim-to-proof record without hidden debt.

- **Intent / authority:** D57 claim-typed proof; Phase A/B APPROVE results; Coordinator
  role boundary and exact 29-path approval.
- **Claim:** All 12 ACs resolve to `PR-C1`–`PR-C12`; regressions, docs/render, exact
  files/LOC, parity, protected state, current range, no-publication, limitations, and
  Value Debt are complete; Executor stops before REVIEW.
- **Boundary:** 29 framework consumers ↔ Phase A/B owners/tests ↔ docs/generated
  navigation ↔ EV/RF/Task Board ↔ independent Reviewer handoff.
- **Precision:** Exact 6 CREATE + 23 MODIFY; 2,600–3,600 estimate is descriptive;
  12 stable PR IDs; exact tests/commands/results and environment versions; no hidden
  Value Debt; no ONB/RF/REVIEW role violation or publication.
- **Proof intent:** Local Proof from regression/build/diff/source checks; Seam Proof
  across ACs, PRs, EV rows, RF attestation, Task Board, and Reviewer entry; Live Proof
  dispositions inherited from AC-3/4/6/10/11.
- [ ] Phase A contract tests, Phase B router tests, new Phase C tests, docs tests,
      MkDocs build/render/link/anchor checks, JSON/schema/compile/import checks, and
      platform matrices pass or have claim-narrowing Value Debt.
- [ ] Exact final framework path set is 29/29 with 0 extras; lifecycle trace set is
      ONB/EV/RF + one README row; protected paths/state remain unchanged as declared.
- [ ] EV contains `PR-C1`–`PR-C12`, per-AC Evidence rows, environments, methods,
      actual results, provenance, actors/time, limitations, and complete Value Debt.
- [ ] RF maps all ACs/Principles/DoF to Proof Records, reports actual physical
      file/new/modified/LOC measurements and signal variance, and makes no unsupported
      client/authentication/publication claim.
- [ ] Final Executor local commit passes the owned runtime and exact range; worktree is
      ready for independent `/tfw-review`; no REVIEW is created by Executor.
- [ ] `origin/master` remains exactly `b4c0a06...`; no push/publication occurs.

Gate: Full regression suite, exact allowlist/protected diff, generated documentation
QA, PR/EV/RF structure scan, post-commit exact audit, clean-tree and remote OID checks
protect traceable completion.

Evidence: Aggregate only the claim-triggered Evidence from AC-3, AC-4, AC-6, AC-10,
and AC-11. N/A rows must retain their claim-based reasons; unavailable declared support
must be complete Value Debt, never a silent N/A.

Proof Record: `PR-C12`.

### Evidence Artifacts

| File | Description |
|------|-------------|
| `evidence/EV__phase-c__repository_local_enforcement_migration.md` | Mandatory indexed `PR-C1`–`PR-C12` claim/proof relations, environment observations, per-AC Evidence rows, verdict, limitations, and Value Debt |

No additional committed evidence artifact is pre-required. Reproducible textual
outputs may be embedded or linked from EV/RF; temporary repositories and private
runtime state must not be committed.

## 6. Technical Guidance

### Canonical owners and adaptable internals

- `.tfw/commit_identity.schema.json` remains the only accepted grammar/registry owner.
  `.tfw/scripts/commit_identity.py` remains the contract/range algorithm owner.
  `.tfw/scripts/commit_identity_router.py` remains the workflow/operation policy owner.
- `.tfw/scripts/commit_identity_hooks.py` may choose internal classes, functions,
  subcommands, and argument spelling for install/verify/repair/rollback/carrier/
  prepare/final behavior. These names are adaptable if all acceptance-critical
  semantics and stable diagnostics remain true.
- A practical tracked-state shape may use `hook_runtime.required_version` and
  `hook_runtime.source`; the child-key spelling is adaptable only if the schema,
  template, current state, init, update, manifest, and tests consume one unambiguous
  canonical shape. No `installed` field is allowed in tracked state.
- The private ledger format may include a state kind, observed runtime version,
  installed disposition, and a structured prior-local presence/value record. It must
  stay under the resolved Git common directory, be atomic, private, untracked, and
  non-diagnostic.

### Runtime and Git safety

- Resolve repository/common-dir behavior through Git's local repository interfaces.
  Do not use `--show-origin`, `--global`, inherited hook enumeration, external-path
  resolution, or environment dumps.
- A test spy/fake Git executable may prove that no global/external/remote action was
  requested. Proving non-access is preferable to reading a global value before/after.
- `/tfw-update` may repair versioned runtime only from recognized upstream/framework
  owners after manifest/ownership checks. Lifecycle `verify` reports mismatch and must
  not synthesize or overwrite unknown material.
- Hook entries should be the thinnest portable launchers that can locate the
  repository-owned standard-library runtime without embedding absolute paths.
  Executable-bit and Windows shebang/launcher behavior require direct tests.
- Install/repair must not use destructive recursive cleanup against unresolved paths.
  Replacement of recognized TFW-owned files should be atomic/recoverable.
- Diagnostics may name stable action/field codes and safe schema-generated examples.
  They must not echo arbitrary current messages, bodies, paths, prior local values,
  environment content, hook content, or secret canaries.

### Context and operation routing

- The router should return the exact expected-context token and the portable required
  runtime status separately from any observed live-state result. The lifecycle may
  verify live state at action time.
- The carrier should receive a validated router plan and invoke a narrowly allowlisted
  local Git operation with a child-only environment. It should not accept arbitrary
  command arrays or shell strings.
- `prepare-commit-msg` receives the owned current message file and Git parameters. It
  may read the file for structural/context validation but must never rewrite it.
- `commit-msg` validates the final message/trailers and expected context when present.
  Range audit remains the catch-all structural check for bypasses and operation paths
  that do not execute every hook.
- Preserve Phase B outcomes: ordinary/merge current-context commits; amend reidentify
  current operator when needed; same-context fixup/squash only; cross-context
  revert/cherry-pick through `--no-commit`, inspection, and current-operator re-commit
  with optional schema-owned source/origin trailers.

### Proof and support claims

- Run destructive/topology/replay/security cases only in temporary repositories.
  Production/current repository work is limited to authorized runtime install,
  validation, real Phase C commits, exact audit, and non-mutating inspection.
- Windows and WSL results should record exact Git/Python versions and equivalent
  scenario IDs. A platform unavailable at execution time is a material claim change,
  not a routine N/A.
- Synthetic `antigravity`, `claude-code`, `codex`, and `cursor` values prove registry
  behavior only. Exact Antigravity/Claude copies prove structural parity only.
- Real client proof requires the client to operate its own session/commit. Codex must
  not create an artificial `claude-code`, `antigravity`, or `cursor` operator commit.
- Snapshot current repository facts safely: tracked hashes/diffs, local-config
  presence/value handled privately, command-spy proof of no global access, exact Git
  objects/range, and local remote-tracking OID. Do not contact or mutate the remote.
- Strictly preserve F26: do not push at Executor or Reviewer stop. Even full TFW-49
  closure needs later explicit user `APPROVE PUSH`.

### Source authority

| Source | Required relation |
|--------|-------------------|
| [Phase C HL](HL__phase-c__repository_local_enforcement_migration.md) | Exact scope, state split, client claim, proof plan, principles, and DoF |
| [Iteration 1 RES](../research/iter1/RES.md) | Challenged C1-R/per-repository no-proxy configuration and limitations |
| [Phase A RF](../phase-a/RF__phase-a__canonical_contract_and_validator.md) / [REVIEW](../phase-a/REVIEW__phase-a__canonical_contract_and_validator.md) | Actual schema/state/CLI and corrected public/private validation contract |
| [Phase B RF](../phase-b/RF__phase-b__workflow_and_adapter_consumption.md) / [REVIEW](../phase-b/REVIEW__phase-b__workflow_and_adapter_consumption.md) | Actual router, seven operations, parity, and F26 action separation |
| [KNOWLEDGE D58/D59](../../../KNOWLEDGE.md) | Durable owner and phase boundaries |
| [process F26](../../../knowledge/process.md) | Human-only remote publication authority |
| [philosophy F23](../../../knowledge/philosophy.md) | Template/project-state contamination prevention |
| [Commit Identity conventions](../../../.tfw/conventions.md#commit-identity-and-attribution) | Existing C1-R truth boundary |
| [Proof Record conventions](../../../.tfw/conventions.md#proof-records-and-claim-boundaries) | Claim-typed PR/EV/RF/REVIEW relation |
| [File classification](../../../.tfw/conventions.md#file-classification-in-tfw) | Template, tracked project state, private runtime, and update ownership |
| [Role Lock](../../../.tfw/conventions.md#role-lock-protocol) | Coordinator/Executor/Reviewer artifact and operation boundaries |

## 7. Definition of Failure

- ❌ 1. Contract/state/runtime uses a truncated/non-semver alias or any value other
  than exact `1.1.0`.
- ❌ 2. C1-R meaning/accepted registry is duplicated or changed, or Python/workflows/
  hooks become a second grammar, registry, parser, or operation owner.
- ❌ 3. Template/current/update state copies the starter anchor, stores clone-local
  installed truth, accepts invalid mode/anchor pairing, or overwrites project
  activation.
- ❌ 4. Exclusive audit includes its anchor or omits a descendant; root-inclusive
  audit omits target/root/reachable commits; no-target/shallow/incomplete/missing/
  non-ancestor state passes or uses a recent/sample fallback.
- ❌ 5. Manifest or lifecycle recognizes, repairs, overwrites, deletes, executes,
  copies, or trusts unknown/unowned reserved-target material.
- ❌ 6. Any implementation or proof queries, resolves, reveals, reads, executes,
  fingerprints, chains, or mutates an external/global hook path/body/value/config.
- ❌ 7. Installation uses non-local Git config, an absolute versioned path, a
  non-relative hooksPath, or fails to restore exact opaque prior local value/unset.
- ❌ 8. Private ledger is tracked, copied, printed, split across main/linked
  worktrees, non-atomic, or inconsistent with observed local state.
- ❌ 9. Router infers installed state from tracked state, or carrier persists context,
  accepts arbitrary commands, launches a remote/publication action, or becomes a
  second operation owner.
- ❌ 10. Prepare mutates the commit message, accepts partial/malformed/stale expected
  context, or represents absent context as exact/authenticated.
- ❌ 11. Final validation accepts malformed subject/trailers/context, prohibited
  cross-context autosquash/replay, invalid `task:none`, or an unregistered surface/role.
- ❌ 12. Tests import real arbitrary/sensitive message/body/environment/hook/secret
  material instead of synthetic redacted fixtures, or diagnostics echo, retain, or
  disclose arbitrary owned message input or canaries.
- ❌ 13. Init/update synthesize or overwrite unknown runtime/state, or any canonical/
  derived lifecycle workflow disagrees with its owner.
- ❌ 14. Handoff, REVIEW, or release accepts hook/file presence, an Executor-only
  claim, incomplete current history, invalid runtime, or a partial/recent range.
- ❌ 15. Synthetic four-surface/four-role coverage or Antigravity/Claude byte parity is
  represented as live non-Codex client execution, GUI/IDE/JGit/hosted support, or actor
  authentication.
- ❌ 16. Windows or Ubuntu WSL is declared supported without actual versioned runtime
  observation and reproducible result; missing proof is hidden as N/A instead of
  complete Value Debt/claim narrowing.
- ❌ 17. A 30th framework file, adapter entry, Codex skill, config, knowledge, Cursor,
  unrelated workflow, version, prior-history, or external-remediation change enters
  without a new Coordinator decision.
- ❌ 18. EV lacks any `PR-C1`–`PR-C12` relation, RF hides a limitation/Value Debt/
  material deviation, or Executor writes REVIEW or otherwise violates Role Lock.
- ❌ 19. `origin/master` changes from `b4c0a06...`, or any push, remote tag, deploy,
  publish, notify, host escalation, force update, or history rewrite occurs.

**On failure:** stop the affected operation, preserve exact current Git and private
rollback state, leave unknown/global/external material untouched, record the failed
claim and complete Value Debt in EV/RF, and return to the Coordinator. Do not bypass
hooks/audit, shrink the range, fake a client identity, overwrite a conflict, or publish
to manufacture completion.

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| State template contaminates downstream projects | Null/root-inclusive template plus destination-init and update-preservation matrices |
| Root-inclusive graph semantics miss roots or merges | Exact Git DAG enumeration, multi-root merge fixtures, and stable no-target failure |
| Tracked/private runtime truth drifts | Schema-enforced split, common-dir ledger, live verify, and mutation tests |
| Global/external hook is accidentally inspected | Local-only command wrapper, subprocess spy, source scan, and no global snapshot values |
| Unknown target is overwritten during repair | Manifest ownership gate and conflict-preservation fixtures |
| Opaque prior local value leaks | Private ledger, presence-only diagnostics, canaries, and exact rollback comparison |
| Main/linked worktrees disagree | Common-dir resolution and two-way lifecycle scenario matrix |
| Hook launcher differs on Windows/WSL | Thin relative entries and direct version-pinned execution |
| Command context persists or races | Child-only carrier and parent/private/tracked absence checks |
| Sequencer skips final hook | Prepare guard + Phase B router + independent exact range |
| Broad scope hides incomplete seams | Dependency-ordered ACs, exact 29-path allowlist, PR-C1–C12, 100% review on discrepancy |
| Synthetic coverage is overclaimed | Separate Evidence rows for registry, copy parity, platform runtime, and live Codex sessions |
| Missing live/platform proof is waived | Mandatory complete Value Debt and blocked full-support claim |
| Local closure triggers publication | F26 wording, remote OID proof, and no-push hard failure |

## 9. Cross-Phase Modifications

| File / group | Also modified in | Coordination note |
|--------------|-----------------|-------------------|
| Schema, tracked state, contract CLI/tests, conventions, glossary | Phase A | Preserve approved C1-R, owner-field failures, public reserved-context, exclusive-range, and non-authentication behavior while extending to 1.1.0 |
| Router/tests | Phase B | Preserve one workflow/operation owner and all seven operation outcomes; add transport/status only |
| Handoff workflow and derived copies | Phase B | Preserve routed local action and F26 separation; add carrier/runtime/range execution |
| Init/update workflow copies | Phase B parity restoration | Canonical Phase C lifecycle becomes the new copy owner; no adapter entry change |
| Review/release workflow copies | Existing canonical parity | Add independent lifecycle/range gates without changing Role Lock or publication authority |

There is no later implementation phase. After Executor RF and independent REVIEW,
Phase C proceeds through `/tfw-docs` and `/tfw-knowledge` as applicable. Full local
TFW-49 closure still does not authorize publication.

---

*TS — TFW-49 / Phase C: Repository-Local Enforcement, Migration, and Cross-Agent Proof | 2026-07-31*
