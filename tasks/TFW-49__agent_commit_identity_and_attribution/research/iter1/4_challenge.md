# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would the supported disposition survive an independent attack using counter-evidence, edge cases, and the declared exclusions?"
> Parent: [HL-TFW-49](../../HL-TFW-49__agent_commit_identity_and_attribution.md)
> Goal: Every new agent-created commit should carry truthful, subject-leading, searchable agent-surface, task/work-scope, and TFW-role provenance without replacing Git authorship, Proof Records, RF attestation, or REVIEW.

## Authoritative Challenge Correction

The owner supplied a Human-Only signal during Challenge: Git operations in a
TFW-managed project are agent-managed; the repository policy may require canonical
identity on every new commit; project hooks may supersede rather than chain existing
local/user hooks; and any TFW hook runtime must be installed per repository by
`/tfw-init` and repaired or updated through its owning lifecycle. The global hook
directory remains untouched. The separately observed plaintext-credential owner action
also remains excluded.

This changes the target population and migration design, but not the truth claim:

- a post-activation commit without canonical identity is a repository-policy failure,
  not an implicitly human commit;
- a structurally conforming identity is contractual provenance, not authenticated
  proof of which human or agent process invoked Git;
- `--no-verify`, direct plumbing, and contexts not supplied through the agent entrypoint
  remain explicit bypass or truth gaps;
- the user authorization permits a repository-local override to make inherited/global
  hooks irrelevant for this project, but does not authorize reading, copying, deleting,
  or mutating the external/global hook directory.

## Consistency Check

Challenge each material relationship from Gather/Extract: "Can these alternatives
coexist, and what evidence would falsify the claimed relationship?"

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| Repository population | every new commit must carry canonical identity | Human classification | missing prefix means human | The new owner policy makes omission a violation; local Git state still cannot authenticate the actual invoker. |
| Operator truth | subject role is the current commit operator | Cross-context autosquash | preserve the target's nested identity | Git matches `fixup!`/`squash!` against the target subject; a different current operator/task/work identity at byte zero does not match, while retaining the target identity is stale provenance. |
| Replay truth | acting identity must be current | Automatic cross-context revert/cherry-pick | accept Git's generated/copied subject unchanged | Synthetic replay retained the target/source identity. `commit-msg` was not invoked, so structural final-message validation cannot repair it. |
| Hook claim | a hook blocks an operation | Hook observability | the hook is not invoked | Synthetic Git 2.42 invoked `prepare-commit-msg`, but not `commit-msg`, for automatic revert and cherry-pick. Only the observed prepare stage can add immediate context checking. |
| Project-local ownership | TFW disables inherited hooks by local override | Prior-hook proxy | chain every inherited hook | The owner has authorized disablement. Proxying adds secret ingestion, cycle, ordering, and worktree failure modes without adding required value. |
| Contractual provenance | structurally valid identity | Actor authentication | local hook proves the actor | A local actor can self-declare fields, bypass hooks, or use plumbing; syntax cannot establish authenticated actor identity. |
| `task:none` | lifecycle-only, explicitly declared non-task work | Task-scoped change | staged canonical task path or `phase-*` work | Treating `none` as compatible would make it an escape hatch from task attribution. |
| Mixed-origin truth | core role is the commit operator | One-role compression | content from other task/work/role is silently represented by the operator role | Operator and content origin are independent facts. Atomic splitting or a full optional origin record is required. |

**Surviving configurations** (from Extract's Configuration Space, after removing rows
containing incompatible pairs and applying the owner signal):

| Config | Subject grammar | Operation contract | Enforcement/installation | Verdict |
|--------|-----------------|--------------------|--------------------------|---------|
| C1-R — compact layered, repaired | `[surface/task/work/role] summary`, mandatory on every new commit; narrow same-context Git-marker exceptions | agent entrypoint supplies expected context; explicit replay router; cross-context autosquash prohibited; operator role plus optional full origin trailers | per-repository TFW-owned `prepare-commit-msg` context check + `commit-msg` structural validator + independent all-commit range audit; no prior-hook proxy | **Leading challenged configuration; survives with material repairs** |
| C2-R — labeled layered, repaired | `[agent:surface][task:id][work:scope][role:role] summary`, otherwise same semantics | same as C1-R | same as C1-R | **Viable labeled fallback; survives, but no observed failure justifies its extra subject width** |
| C3-R — entrypoint plus range audit | C1-R or C2-R | same explicit router | no local validator; independent all-commit audit | **Unexpected partial survivor, but rejected as the default:** truthful and smaller in mechanisms, yet loses immediate failure visibility and does not neutralize an inherited mutating hook by itself |

**Unexpected survivors**:

- C3-R survives as a truthful minimum claim for commits made through the entrypoint,
  because the independent all-commit audit can detect structural omissions. It does not
  lead: per-repository hooks materially improve point-of-action diagnostics, catch
  ordinary omissions before a commit is created, and supply a local override that makes
  the inherited/global hook path irrelevant for this project.
- C2-R survives because explicit labels are semantically unambiguous. It remains a
  fallback rather than the leader: the closed positional grammar and strict parser
  remove the ambiguity that labels would otherwise solve.

## Findings

### C1. Sequencer coverage repairs the hook claim

Challenge used only synthetic hooks and temporary repositories under:

```text
E:\TEMP\tfw49-challenge-a4ea443dc0524e8eb1f5f8e1d06748bc
```

The fixtures recorded hook name, Git-provided source argument, synthetic expected
context, and operation state. They did not read, execute, fingerprint, quote, copy, or
hash any production hook or credential.

Observed with Git `2.42.0.windows.1`:

| Operation | `prepare-commit-msg` delta | `commit-msg` delta | Generated subject behavior |
|-----------|----------------------------|--------------------|----------------------------|
| automatic `git revert` | +1 | 0 | `Revert "[old identity] old subject"` |
| automatic `git cherry-pick` | +1 | 0 | copied the source commit's old identity |
| guarded automatic revert with a different expected identity | +1, exit 42 | 0 | commit not created; stable mismatch diagnostic |
| guarded automatic cherry-pick with a different expected identity | +1, exit 42 | 0 | commit not created; stable mismatch diagnostic |

The Gather statement that automatic replay bypassed `commit-msg` remains true, but the
stronger inference that hooks cannot observe replay is false. `prepare-commit-msg` did
run for both replay operations. Operation-state detection was not reliable enough to
own the rule: `CHERRY_PICK_HEAD` was visible during cherry-pick, while the revert
fixture did not expose a consistent equivalent at the observed point.

The repaired rule is therefore general rather than operation-name based:

1. the agent Git entrypoint/router establishes the canonical expected identity;
2. `prepare-commit-msg`, when that context exists, non-mutatingly compares the complete
   proposed subject's effective identity with the expected identity and rejects a
   mismatch;
3. `commit-msg` validates final structure for the ordinary operations it observes;
4. the operation router remains the semantic owner and uses explicit no-commit plus
   re-commit when Git would carry a stale identity.

This hook is a guard, not an operation router and not an authentication mechanism.
Direct Git without trusted expected context can still present a structurally valid
stale identity. The implementation must never advertise that a hook blocks an
operation it does not observe.

Operation corrections:

- **Cherry-pick across identity context:** use `git cherry-pick --no-commit`, inspect the
  staged result, then create a new current-operator commit. An optional
  `TFW-Source-Commit: <object-id>` trailer may preserve source provenance. The copied
  source identity must not remain the acting identity.
- **Revert across identity context:** use `git revert --no-commit`, then create a normal
  current-operator subject such as `[current identity] revert: <summary>`. An optional
  source-object trailer may record the reverted commit.
- **Same-context replay:** a Git-generated reserved subject may be accepted only when
  the nested identity exactly equals the current expected four-field identity.
- **Amend:** the entrypoint must revalidate the resulting subject against current
  context. Retaining an older operator identity is permitted only when the operation
  is an explicitly authorized correction of that same atomic unpublished commit and
  the identity remains factually accurate.

### C2. Cross-context autosquash cannot satisfy both target matching and current operator truth

The synthetic autosquash repository used:

```text
target: [claude-code/TFW-49/phase-a/executor] target change
current context: [codex/TFW-49/phase-b/executor]
```

`git commit --fixup=<target>` produced:

```text
fixup! [claude-code/TFW-49/phase-a/executor] target change
```

The nested identity was copied from the target, not the current operator. A manually
authored alternative beginning:

```text
fixup! [codex/TFW-49/phase-b/executor] ...
```

did not match the target during the captured `rebase --autosquash` plan and remained an
ordinary `pick`. The stale form matched and was moved as `fixup`.

Therefore Git's byte-zero marker exception is narrower than Extract proposed:

```text
ordinary  = ID SP summary
fixup     = ("fixup!" / "squash!") SP ID SP target-summary
revert    = "Revert " DQUOTE ID SP target-summary DQUOTE
```

`ID` is the same four-field record as the ordinary grammar. For any reserved form, the
nested `ID` must exactly equal the entrypoint's current expected identity. Structural
validation without expected context can verify only shape, not equality to the actor.

Disposition:

- same-surface/task/work/role autosquash remains allowed;
- cross-operator, cross-task, or cross-work autosquash is prohibited by default;
- the truthful default is a normal follow-up commit carrying the current identity;
- an explicitly authorized rewrite of unpublished history may reword the final commit
  to the actual operator, but stale identity must not be retained or published merely
  to make autosquash match.

This is an honest restriction, not an attempt to make every Git convenience fit H6.
H6 survives only as "small explicit grammar and operation restrictions," not as
transparent support for every automatic form.

### C3. Closed registries need normalization, ownership, and cross-field escape guards

Challenge inventoried the current adapter and phase spellings rather than testing only
ideal examples.

Current supported agent surfaces found under `.tfw/adapters/`:

```text
antigravity
claude-code
codex
cursor
```

The role registry remains:

```text
coordinator
researcher
executor
reviewer
```

The release workflow's descriptive `Coordinator/Maintainer` header does not establish
a fifth Role Lock. Until the canonical role contract is changed, an agent release or
maintenance commit uses its actual workflow role, normally `coordinator`;
`maintainer` is not silently accepted.

The work-scope tests covered current legacy and canonical forms:

| Input/condition | Disposition |
|-----------------|-------------|
| `PhaseA`, `PhaseA2`, `PhaseD`, `PhaseE` | normalize to lower canonical `phase-a`, `phase-a2`, `phase-d`, `phase-e` |
| `phase-a` through current project phases | accept canonical output |
| external/current observed `phase-a3.4` class | accept under the strict phase-token rule |
| `master`, `research-iter1`, `docs`, `knowledge`, `release`, `config`, `init`, `update`, `maintenance` | accept as owned scopes |
| unregistered `windsurf`, ambiguous `codex/latest`, or unregistered `maintainer` | reject with registry diagnostic |
| `task:none/phase-a` | reject |
| `task:none` without an explicit non-task entrypoint declaration | reject |
| `task:none` while staged paths include `tasks/<canonical-id>/...` | reject |

The fixture matrix returned 22 accepted and 6 rejected cases. A phase token is
permissive only within an anti-ambiguity rule: lowercase ASCII segments, single `-` or
`.` separators, no slash, brackets, whitespace, empty segment, or consecutive
separator. The entrypoint emits canonical lower-case output; the validator does not
preserve legacy capitalization.

Registry ownership:

- the canonical commit-identity contract owns the surface, work, and role registries;
- `/tfw-init` installs the consumer generated from that contract;
- `/tfw-update` updates existing consumers;
- adding an adapter requires an atomic registry, generated-consumer, and fixture update;
- a closed registry is preferable to an arbitrary surface token because it makes
  typos and ambiguous version/model suffixes actionable rather than silently durable.

`task:none` remains necessary for lifecycle work outside a task, but it is not a free
escape. It requires all three: an explicit non-task declaration from the entrypoint, a
lifecycle work scope, and no staged canonical task path. A mixed lifecycle/task change
must be split or attributed to the task.

### C4. Mixed-origin commits require either atomicity or a complete origin record

The core role is always the commit operator. The default batching rule is one atomic
same-origin commit. Cross-task mixed batching is rejected by default because one task
field cannot truthfully scope several independent task changes.

For a justified mixed-origin commit, the optional trailer is repeatable and contains
the full record:

```text
TFW-Content-Origin: claude-code/TFW-49/phase-a/executor
TFW-Content-Origin: codex/TFW-49/research-iter1/researcher
Co-authored-by: Fixture Partner <fixture@example.invalid>
```

A synthetic `git interpret-trailers --parse` test preserved the two origin records and
the `Co-authored-by` trailer as separate entries. A shorter surface/role origin was
rejected conceptually because it omits the task/work dimensions that make mixed content
ambiguous.

`TFW-Content-Origin` means only "content from this attributed workflow context is
included." It does not attest acceptance, review, authorization, proof, or current
operator. It does not replace `Co-authored-by`, which retains Git's established
co-author semantics.

Model and session remain optional, separate trailers:

```text
TFW-Agent-Model: <declared model token>
TFW-Agent-Session: <opaque session reference>
```

They are declared metadata, not authenticated identity and not mandatory search keys.

### C5. The Human-Only signal revises H4 without making it true as authentication

Gather refuted H4 as written because a local validator cannot distinguish an omitted
agent identity from an allowed human commit without trusting self-declaration. The new
owner policy removes the allowed plain-human branch for the default TFW-managed
repository:

```text
Every new post-activation commit must carry a canonical identity record.
```

That makes population selection operationally deterministic for structural validation:
the validator and range audit examine every new commit, and no commit is accepted as
"human because unclassified." It does not establish who actually invoked Git. A human
or different agent can still type a valid record, use `--no-verify`, use plumbing, or
invoke an automatic operation without entrypoint context.

Correct H4 disposition:

- **refuted** as an authenticated or actor-deterministic agent-only guarantee;
- **revised and supported** as a repository-wide structural policy when every
  post-activation commit is in scope;
- a future plain-human path requires an explicit owner policy/profile change and a
  truthful classification mechanism; it must not be inferred from missing identity.

No hosted identity service is required for the user's practical outcome. Adding one
would change the cost, trust, and project scope and remains deferred unless the owner
later requires authenticated actor provenance.

### C6. The viable migration is a per-repository override, not a prior-hook dispatcher

The new owner direction eliminates the need for Extract's complex default
chain-by-reference dispatcher. Challenge did not attempt to prove proxy ordering,
all-hook-name forwarding, or prior-hook cycle safety because the corrected
configuration contains no prior-hook proxy. Keeping that architecture would introduce
failure modes with no required benefit:

- it would expose the new runtime to arbitrary inherited hooks and potentially
  sensitive material;
- it would need cross-shell path, recursion, ordering, and failure-propagation policy;
- it would couple TFW's per-repository contract to an owner-external/global lifecycle;
- it is unnecessary after explicit authorization to disable inherited hooks for the
  project.

The viable leading lifecycle is:

1. `/tfw-init` inspects configuration topology and managed ownership markers without
   reading or copying arbitrary hook bodies.
2. It installs a TFW-owned, versioned runtime in a reserved repository path and sets a
   **local repository** `core.hooksPath` override to that path.
3. It never changes global Git configuration and never reads, deletes, writes, or
   mutates the external/global hook directory.
4. It records whether the prior local override was absent or records its exact prior
   value in non-versioned lifecycle state for rollback; diagnostics do not print the
   path or hook contents.
5. If the reserved target path already contains non-TFW-owned material, installation
   blocks. It does not overwrite, copy, or ingest those bodies.
6. For general attach, a pre-existing project-specific hook owner requires explicit
   supersession authority. The prior hook files remain in place. "Backup" means
   preserve them in place plus restore the prior config value, not copy their content.
7. `/tfw-update` replaces only files with a recognized TFW ownership/version marker and
   revalidates the local override. Repair follows the same ownership rule.
8. Rollback restores the exact former local setting; if it was previously unset,
   rollback unsets the local override so Git's inherited/default resolution returns.

This task's owner has already authorized project-local supersession. The external
plaintext-credential action remains a separate owner responsibility; neither the
installer nor its diagnostic output ingests the credential-bearing hook.

Synthetic configuration tests, with global configuration disabled for the fixtures,
confirmed:

| Prior local `core.hooksPath` state | Install | Rollback result |
|------------------------------------|---------|-----------------|
| unset | set `.tfw/hooks` | local value absent again; effective value absent in isolated fixture |
| `project-owned-hooks` | set `.tfw/hooks` | exact prior string restored |

A synthetic TFW-owned `commit-msg` validator at a relative `.tfw/hooks` path was
exercised from both a main worktree and a linked worktree. The same repository-local
config was visible in the linked worktree; valid C1 subjects invoked the validator,
while an unclassified linked-worktree commit was rejected. Hook observation was written
to the shared common Git directory. This supports relative, per-repository ownership
across normal linked worktrees. It does not prove every POSIX/Windows shell edge; the
eventual implementation still needs the cross-platform fixture matrix declared in the
HL.

Cycle detection is now a topology-install concern, not runtime proxy recursion:

- reject if the managed target resolves outside the repository or aliases the
  inherited/external path;
- reject an existing reserved target without recognized TFW ownership;
- do not create proxy references, so runtime hook cycles are absent from C1-R.

Secret-safe diagnostics contain only stable error code, hook stage, violated field, and
remediation. They contain no arbitrary hook body, configured hook path, credential,
full environment, or commit-message content.

### C7. Hooks survive only because they add immediate failure visibility

Under the all-commit repository policy, the mechanisms have distinct jobs:

| Mechanism | Material benefit | Honest gap |
|-----------|------------------|------------|
| agent Git entrypoint/operation router | establishes current surface/task/work/role, applies task/work cross-field rules, handles no-commit replay, and supplies expected context | direct Git can bypass the router |
| project-local `prepare-commit-msg` guard | rejects a complete proposed subject whose effective identity conflicts with supplied expected context; observes synthetic automatic revert/cherry-pick | no expected context means no actor comparison; not an operation detector |
| project-local `commit-msg` validator | immediate rejection of missing/malformed final identity for ordinary observed commits; stable diagnostics | `--no-verify` and the observed sequencer paths bypass it |
| independent post-activation range audit | checks every new commit because there is no human exception; catches structural `--no-verify` and plumbing bypass before push/review/release | cannot identify the actual actor or detect a structurally valid stale identity without trusted expected context |

The worktree fixture made a plain unclassified commit attempt:

```text
plain human maintenance
```

The local validator rejected it and left `HEAD` unchanged. Repeating with
`--no-verify` succeeded, as Git documents. A direct synthetic `commit-tree` operation
also created an unclassified commit without invoking the hook. An independent scan
over the temporary refs found exactly those two structural violations while accepting
the valid main and linked-worktree commits.

Therefore:

- C3-R entrypoint plus audit is the smallest truthful mechanism set, but not the
  smallest reliable point-of-action experience;
- C1-R/C2-R keep the two local hook stages because they materially shorten feedback and
  the local override disables the inherited mutator for this project;
- the range audit is required before push/review/release if the user wants structural
  completeness over all post-activation commits;
- none of these layers authenticates actor identity.

The independent audit may be run by a separate review/CI surface, but no hosted identity
system is part of the default recommendation. A local actor can bypass both local
hooks and a local audit; the contract must not claim otherwise.

### C8. Exact challenged grammar and configuration verdicts

#### C1-R — compact leader

Mandatory ordinary subject:

```text
[<surface>/<task>/<work>/<role>] <summary>
```

Candidate examples:

```text
[codex/TFW-49/master/coordinator] approve commit identity design
[codex/TFW-49/research-iter1/researcher] challenge sequencer behavior
[claude-code/TFW-49/phase-a/executor] implement the approved validator
[cursor/TFW-49/phase-a/reviewer] verify migration evidence
[codex/none/update/coordinator] repair installed TFW hook runtime
```

Required semantic rules:

- fixed field order and exactly one `/` separator between fields;
- closed registered surface and role;
- canonical task identifier, or guarded `none`;
- canonical lower-case work scope with explicit legacy normalization at the entrypoint;
- role means commit operator, not content author or reviewer of another agent's work;
- summary is non-empty and remains after the identity record;
- optional origin/model/session/source trailers do not replace the core;
- local proof/RF/REVIEW status is never encoded as if identity attested acceptance.

Reserved subject forms are allowed only with the same-context rule from C2. No generic
exception permits Git to carry a stale identity.

**Verdict:** C1 survives and leads after repairs to population policy, replay,
autosquash, registry, mixed-origin scope, and installation.

#### C2-R — labeled fallback

Mandatory ordinary subject:

```text
[agent:<surface>][task:<task>][work:<work>][role:<role>] <summary>
```

Its semantics, registries, reserved-marker restrictions, operation router, hooks,
audit, trailers, installation, and non-claims are identical to C1-R.

**Verdict:** C2 survives as the explicit-label fallback. Challenge found no case in
which the strict C1 parser could not identify a field position or produce a
field-specific diagnostic. The extra labels therefore do not yet justify their cost
in every subject.

#### Eliminated or deferred configurations

| Config | Disposition after Challenge | Reason |
|--------|-----------------------------|--------|
| Extract C1/C2 chain-by-reference dispatcher | eliminated/replaced | owner-authorized per-repository disablement removes the need; proxy adds secret, cycle, order, portability, and ownership risks |
| C3 entrypoint-only without audit | eliminated | direct omissions and bypasses are invisible; inherited mutator remains effective unless separately overridden |
| C3-R entrypoint plus audit | viable partial survivor, not default | truthful and structurally complete at the audit gate, but loses immediate rejection and project-local override benefit |
| C4 `commit-msg` only | eliminated | observed automatic revert/cherry-pick skip it; `--no-verify` bypasses it; no semantic operation routing |
| C5 Conventional-first | eliminated | identity is not subject-leading and work dimensions are compressed; strict Conventional compatibility is not an owner requirement |
| C6 trailers/prose | eliminated | identity is absent from normal one-line history and omission drift remains easy |
| C7 global mutation | eliminated | violates per-repository ownership and would touch excluded external/global state |
| C8 hosted authenticated | deferred/out of scope | not required for the practical structural policy; separate trust/cost decision |

Architecture selection remains Coordinator-owned. C1-R is the leading challenged
configuration, not an implemented or already selected framework architecture.

### C9. Definition-of-Failure repairs required in the HL

The current HL DoF cannot be carried unchanged because items 1, 5, and 6 embed the old
population and migration assumptions. The Coordinator should revise the HL/TS contract
to cover these failures:

1. **All-commit scope:** any post-activation commit in an agent-managed TFW repository
   that lacks canonical identity is a failure unless the owner has explicitly selected
   another repository policy profile. Missing identity must never be inferred as human.
2. **Authentication overclaim:** any wording that treats a valid prefix or local hook
   result as authenticated proof of the actual actor is a failure.
3. **False insertion:** a hook must not invent or silently replace context that the
   current agent entrypoint did not establish.
4. **Replay/autosquash:** an automatic revert/cherry-pick or cross-context
   fixup/squash/amend that retains a stale operator/task/work identity is a failure.
5. **Registry escape:** unregistered surface/role, ambiguous phase spelling, or
   `task:none` combined with task-scoped work/path is a failure.
6. **Origin compression:** using the operator role to imply all content origin, or a
   short origin trailer that omits task/work where those dimensions differ, is a
   failure.
7. **Installation boundary:** global config/hook mutation, arbitrary hook-body
   ingestion/copy, overwrite of non-TFW material at the reserved target, path/body
   leakage in diagnostics, or rollback that does not restore exact prior local config
   including "unset" is a failure.
8. **False completeness:** claiming hook or actor completeness despite
   `--no-verify`, plumbing, direct-entrypoint, sequencer-context, or local-audit bypass
   is a failure.

The old DoF 5 should no longer require preservation/chaining when the owner explicitly
authorizes per-repository supersession. "Detection and explicit authority" remain;
"preservation" means the prior files are left in place and the old config can be
restored, not that old hooks execute. The old DoF 6 ("normal human commits are blocked")
must be removed or scoped only to an explicitly selected mixed human/agent profile.

## Checkpoint

| Counter-evidence and exclusions | Decision disposition | Remaining gap / authority outcome | Saturation |
|---------------------------------|----------------------|-----------------------------------|------------|
| Automatic revert/cherry-pick were exercised with synthetic prepare and final validators. Contrary to the initial inference, `prepare-commit-msg` ran for both; `commit-msg` did not. State-file operation detection was inconsistent. | **Revised/supported:** entrypoint expected context plus a general prepare comparison can reject stale generated proposals; operation router remains primary. | Eventual implementation must reproduce the matrix on supported Git/platform versions. Research does not implement hooks. | The key observability question is resolved for the inspected Git version; another synthetic hook body would not change the semantic ownership boundary. |
| Cross-operator/task/work fixups were created and an autosquash plan was captured. Target-matching stale identity worked; current-operator nested identity did not match. | **Restricted:** reserved fixup/squash only for exact same four-field context; otherwise normal follow-up or explicitly authorized unpublished rewrite. | Coordinator must carry the restriction into HL/TS. | The conflict is intrinsic to Git's target-subject matching, so more examples would repeat the same relationship. |
| All current TFW adapter surfaces, legacy/canonical phase spellings, lifecycle scopes, all four roles, and `task:none` escape cases were exercised in a 28-case registry matrix. | **Supported with guards:** closed registry, entrypoint normalization, cross-field `none` checks, owned extension path. | Contract owner must define the generated registry/update mechanism. | Current surface/work/role classes are covered; future adapters are an update event, not missing research. |
| Full repeated `TFW-Content-Origin` records and `Co-authored-by` were parsed synthetically. | **Supported:** atomic same-origin default; full optional origin records for justified mixed content. | Coordinator decides whether the optional trailer enters Phase A or is deferred. | The semantic ambiguity of shorter records is resolved; acceptance/proof remains explicitly excluded. |
| New Human-Only owner signal removed the plain-human default; plain commit, `--no-verify`, and direct plumbing were exercised in a temporary repository. | **H4 revised:** repository-wide structural coverage is feasible; authenticated/deterministic actor claim remains refuted. | Coordinator must update H4/DoF and preserve the non-authentication claim. | The tested bypasses bound local structural enforcement; authentication would require a separately scoped trust system. |
| Relative per-repository hooks were exercised from main and linked worktrees; unset and prior-value config rollback were isolated and restored. Prior-hook proxying was attacked against the new owner authorization. | **Supported/repaired:** per-repo TFW-owned override; no chain/proxy default; old bodies remain unread and in place. | Coordinator owns architecture selection; init/update implementation and Windows/POSIX validation belong to later TS/execution. | The default topology decision is saturated. Compatibility chaining would be a separate option with no current owner requirement. |

**Sufficiency:**

- [x] Material relationships/options received an independent countercheck?
- [x] Edge/failure cases and exclusions are explicit?
- [x] Every supported/eliminated claim has evidence or an explicit limitation?
- [x] Decision disposition or unresolved result is stated?

## Learning Receipt

| Signal and trigger | Disposition | Required relation | Responsible actor |
|--------------------|-------------|-------------------|-------------------|
| Effective hooks resolve through external/global topology; arbitrary and sensitive bodies remain excluded. The owner now permits repository-local disablement rather than chaining. | derive | **Revised relation:** C6 replaces Extract E7's chain-by-reference candidate with a TFW-owned per-repository override. Carry to RES and Coordinator HL/TS with backlinks to Gather G3, Extract E7, and this Challenge correction. | Researcher derives; Coordinator owns architecture/HL/TS; owner handles excluded credential action |
| Agent omission/self-declared human could not be distinguished under the old allowed-human branch. | derive | C5 preserves the authentication refutation while the new all-commit repository policy removes the structural classification exception. Carry to RES and Coordinator H4/claim correction with backlink to Gather G7-G8. | Researcher derives; Coordinator owns claim language |
| Automatic revert/cherry-pick bypassed `commit-msg` and retained stale identity; Challenge found that `prepare-commit-msg` does run. | derive | C1 repairs Extract E2/E6: expected-context prepare comparison is a narrow guard, while explicit no-commit/re-commit remains the operation contract. Carry to RES and Phase A/B planning. | Researcher derives; Coordinator owns operation architecture |
| **Human-Only signal:** the user performs project Git work through agents, requires agents to manage Git, authorizes disabling project-local/inherited hooks for this repository, and requires per-repository init/update ownership. This materially changes population selection and migration. | derive | State: **selected authoritative user signal, 2026-07-30**. Reason: it removes the default unclassified-human branch and the need for a prior-hook proxy, but does not authenticate actors. Destination: Iteration 1 RES and Coordinator HL/TS, with backlink to this Challenge section. | User supplies signal; Researcher records/disposes; Coordinator owns HL/TS and architecture |

Stage complete: YES
→ User decision: PENDING COORDINATOR — approve/revise C1-R/C2-R verdicts, the per-repository no-proxy lifecycle, and the HL Definition-of-Failure repairs.
