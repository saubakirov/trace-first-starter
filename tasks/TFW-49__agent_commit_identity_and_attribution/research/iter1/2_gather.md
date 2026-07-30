# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name the material decision factors, realistic alternatives, evidence coverage, and exclusions without inventing filler?"
> Parent: [HL-TFW-49](../../HL-TFW-49__agent_commit_identity_and_attribution.md)
> Goal: Every new agent-created commit should carry truthful, subject-leading, searchable agent-surface, task/work-scope, and TFW-role provenance without replacing Git authorship, Proof Records, RF attestation, or REVIEW.

## Dimensions

| Dimension / decision factor | Material alternatives | Evidence / provenance | Exclusions or uncertainty |
|-----------------------------|-----------------------|-----------------------|---------------------------|
| Mandatory identity dimensions | agent surface; model; Git author/account; exact session; TFW role | HL §§2, 7, 10; Git 2.42 commit-information contract; local TFW roles and Session Naming | A field may be mandatory, optional, already represented by Git, or excluded; these dimensions are not interchangeable |
| Subject grammar | user hyphen/order; fixed labeled brackets; compact fixed-order slash/colon; Conventional-Commit-first; mandatory subject identity plus optional trailers | HL user example; history corpus; synthetic length, parse, and grep observations; Conventional Commits 1.0.0 | Gather establishes trade-offs, not a selected grammar |
| Task and work-scope vocabulary | task master; implementation phase; research iteration; docs; knowledge; release; config; init; update; non-task maintenance | TFW workflows, glossary, release procedure, and temporary valid-subject fixtures | Whether task and work scope are separate labeled fields or fixed-position components remains open |
| Provenance subject | commit operator/acting role; content-origin role; acting role plus optional contributor/origin metadata | Current Coordinator commits of planning/control traces; Executor's explicit handoff commit step; Git author/committer and co-author behavior | A mixed-agent staged diff cannot be truthfully reduced to one role without a batching rule or extra attribution |
| Agent-versus-human activation | all commits labeled; explicit agent context with plain human path; trusted external actor mapping; self-declared agent/human path | Human/agent synthetic commits; local and server-hook truthfulness fixtures | No local commit object or hook input independently proves whether the invoker was human or an agent sharing the same account |
| Local enforcement | prose only; mutating `prepare-commit-msg`; validating `commit-msg`; wrapper/entrypoint; source-aware layered hooks | Current/synthetic prepare behavior; official Git hook contract; temporary negative and bypass cases | Hook coverage differs by Git operation and `--no-verify`; hooks are not a security boundary |
| Review/server enforcement | none; offline review/CI range scan; server `pre-receive`; authenticated automation policy; layered local plus review/server | Synthetic bare-server push fixture; official receive-hook contract | A ref name or self-declared path is not trusted actor identity; the actual hosting/authentication policy is outside this iteration |
| Hook installation topology | repository-local hook; external/global `core.hooksPath`; versioned project hook directory; generated dispatcher that chains prior hooks; wrapper with no hook install | Four production-root topology inventories; official `core.hooksPath`; synthetic chained hook | Migration may discover names/paths and a known legacy hook, but must not ingest, quote, copy, or diagnose arbitrary hook bodies |
| Git operation policy | one universal prefix; Git-reserved marker exceptions; explicit no-commit plus re-commit flows; inherited identity for replayed commits | Amend, merge, revert, fixup/squash, cherry-pick, cleanup, and trailer fixtures | Automatic replays can preserve a structurally valid but wrong prior agent identity |
| Semantic owner and consumers | conventions-owned grammar; versioned validator-owned grammar; shared registry/schema; workflow-specific rules | One-source TFW principle; current workflow/adapter inventory | Point-of-action cues are currently absent from most commit-capable surfaces |
| Portability | POSIX `sh`; Git-for-Windows `sh`; native wrapper per platform; language runtime entrypoint | Git for Windows 2.42.0 fixture; Ubuntu Git 2.43.0 fixture under WSL; official Git hook rules | The fixtures do not establish behavior for every shell, GUI client, IDE, JGit implementation, or hosting provider |

## Findings

### G1. Current TFW history exposes branch and task patterns but not acting-agent provenance

The current TFW repository uses Git `2.42.0.windows.1`. The all-reachable-ref subject
inventory contains 143 commits:

| Observation | Count | Meaning |
|-------------|------:|---------|
| Subject begins with a bracketed branch prefix | 106 | Branch is often visually dominant even though it is not agent or role identity |
| Same branch prefix is duplicated at the beginning | 3 | The current mutating behavior is not idempotent |
| Subject contains a task-like TFW token | 85 | Task search is often possible but vocabulary/order is not universal |
| Conventional-Commit-shaped type is first | 6 | Strict Conventional Commit placement is uncommon |
| Conventional-Commit-shaped type follows a branch prefix | 15 | The branch mutator already displaces the type from the beginning |

The duplicate corpus includes `c4a7a92`, `30a0c0b`, and `e2fa6c5`. The transitional
planning commit `9e19a4f` has subject
`[master]: TFW-49: approve agent commit identity research`, changes the Task Board and
TFW-49 HL, and contains no agent-surface or TFW-role field. This is valid evidence of
the pre-activation system, not retroactive non-compliance.

Git author and committer fields identify the configured personal account but not the
acting AI surface, model, session, or TFW Role Lock. The official Git commit
documentation is explicit that author/committer names do not authenticate the actor.
The synthetic repository also produced a plain human subject and labeled Codex
subjects under the same author and committer metadata.

### G2. Representative project histories reproduce the search and duplication problem

Atamat, Helpdesk, and AFD were all available at their canonical roots. Only commit
subjects, Git hook topology/names, and relevant tracked configuration references were
read. No secrets, personal-memory files, or arbitrary hook bodies were included.

| Root | All reachable commits | Branch-prefixed | Same-prefix duplicates | Task tokens | Conventional type first | Conventional type after branch |
|------|----------------------:|----------------:|-----------------------:|------------:|------------------------:|-------------------------------:|
| TFW | 143 | 106 | 3 | 85 | 6 | 15 |
| Atamat | 170 | 120 | 9 | 73 | 1 | 14 |
| Helpdesk | 250 | 239 | 78 | 97 | 5 | 110 |
| AFD | 727 | 641 | 54 | 657 | 26 | 452 |

These are complete descriptive inventories of the reachable subjects at observation
time, not estimates of human/agent prevalence. They show:

- task and Conventional type tokens can coexist with the branch prefix, but their
  position varies;
- duplicated branch prefixes occur in every root;
- neither a task token nor a branch token answers agent-surface or TFW-role questions;
- a fixed new identity must not rely on the existing prefix being absent.

### G3. Effective hook ownership is external to the repository

All four roots resolve hooks through the same external/global `core.hooksPath`, not
their repository-local `.git/hooks` directory. The relevant effective
`prepare-commit-msg` is byte-identical to the repository-local copy, so the visible
repository copy is a dormant duplicate under the current configuration rather than
the active semantic owner.

A separate global `commit-msg` hook contains plaintext sensitive material. Its
contents, value, fingerprint, and diagnostics are excluded. Owner rotation/removal is
urgent but outside TFW-49's read-only research scope.

Architectural consequences supported by this topology:

1. `core.hooksPath` selects one hooks directory; a repository-local migration can
   silently disable global and repository-local consumers unless it explicitly
   discovers and chains them.
2. Migration discovery must operate on hook topology, names, ownership, and a
   narrowly recognized legacy hook. It must not ingest or copy arbitrary hook bodies.
3. A generated dispatcher can chain an unrelated prior hook by reference and validate
   the resulting message afterward; it must detect cycles and must not embed a
   developer's absolute path in versioned framework files.
4. The known branch-mutating prepare hook cannot be blindly chained for this
   repository because it would continue adding `[master]:`; superseding that known
   behavior and preserving unrelated hooks are separate migration actions.
5. Diagnostics must name only hook kind/path ownership and remediation, never hook
   contents.

### G4. Commit-producing authority is distributed while point-of-action consumption is sparse

The canonical method has no commit-identity semantic owner today. The exhaustive
workflow and lifecycle inventory is:

| Surface | Canonical role | Commit-ready or commit-producing behavior | Current point-of-action identity consumer |
|---------|----------------|--------------------------------------------|-------------------------------------------|
| `/tfw-plan` | Coordinator | writes HL/TS, Task Board, and research control; the current TFW-49 planning/control commits are examples | none |
| `/tfw-research` | Researcher | writes stage traces and RES; another agent may later stage/commit them | none; the Researcher role lock itself forbids non-research artifacts but says nothing about commit identity |
| `/tfw-handoff` | Executor | explicitly says to commit and push ONB/Task Board; AG mode makes incremental commits | explicit commit action, no identity cue or grammar |
| `/tfw-review` | Reviewer | writes stage files/REVIEW and updates traces/knowledge candidates | none |
| `/tfw-resume` | Coordinator | may write the next Phase HL/TS after status selection | none |
| `/tfw-docs` | Coordinator/Reviewer | updates knowledge and debt; says to bundle knowledge with the task commit | bundle instruction, no identity cue |
| `/tfw-knowledge` | Coordinator | writes verified knowledge and state | none |
| `/tfw-release` plus `RELEASE.md` | Coordinator/Maintainer | writes changelog/version, then `release: vX.Y.Z`, tag, and push | exact release subject convention, no agent/task/role identity |
| `/tfw-config` | Coordinator | changes config and every registered inline consumer | none |
| `/tfw-init` | Coordinator | creates framework/project/adapters and RF | no commit cue; only a personal-file do-not-commit warning |
| `/tfw-update` | Coordinator | applies upstream changes, re-syncs adapters, and updates version | none |
| Tool adapters and installed Codex skills | thin tool-specific consumers | route to canonical workflows and are installed/repaired by init/update | no commit identity rule; Codex adapter says its skill copies are committed with the project |
| `.tfw/conventions.md` | tool-agnostic method owner | states AG makes incremental commits and defines roles/workflows | no canonical grammar or validator ownership |

The semantic owner should therefore remain singular, while every actual commit action
needs a short local imperative and one valid example. Adapter copies should consume
the owner, not independently define grammar.

The inventory also exposes a provenance question for Extract: when a Coordinator
commits an unchanged Researcher-owned trace, the commit operator and the content
origin are different. One mandatory role cannot truthfully mean both. Viable contracts
must either keep commits atomic to the acting/content-producing agent, define the
mandatory role as the commit operator and add optional content-origin attribution, or
prohibit mixed-origin batches.

### G5. Official Git contracts constrain mechanism and grammar

Primary sources were accessed on 2026-07-30. Version-specific pages were selected for
the installed Git 2.42 line; where the Git site resolves to an earlier manual version,
its version ledger reports no relevant change through 2.42.x.

| Primary source | Material contract |
|----------------|-------------------|
| [Git hooks](https://git-scm.com/docs/githooks/2.41.0) | Hooks normally live under `$GIT_DIR/hooks` unless `core.hooksPath` redirects them. `prepare-commit-msg` runs before the editor, can edit or abort, and is not suppressed by `--no-verify`. `commit-msg` may validate/edit but is bypassed by `--no-verify`; it is documented for `git commit` and `git merge`. |
| [Git config 2.42.0](https://git-scm.com/docs/git-config/2.42.0) | `core.hooksPath` replaces the hook lookup directory and may be absolute or relative. It is a centralization mechanism, not a multi-directory merge. |
| [Git commit](https://git-scm.com/docs/git-commit/2.38.0) | `--no-verify` skips `pre-commit` and `commit-msg`; `--fixup`/`--squash` reserve leading `fixup!`, `amend!`, or `squash!`; cleanup modes can remove comments/whitespace; authorship can be overridden and is not authentication. |
| [Git interpret-trailers 2.42.0](https://git-scm.com/docs/git-interpret-trailers/2.42.0) | Structured trailers are parsed at the end of a message and coexist with standard entries such as `Signed-off-by` and `Co-authored-by`. |
| [Git merge 2.42.0](https://git-scm.com/docs/git-merge/2.42.0) | Merge creates a commit except for fast-forward/squash cases; `commit-msg` applies and `git merge --no-verify` bypasses it. |
| [Git revert](https://git-scm.com/docs/git-revert/2.39.0) | Revert normally creates a new commit with an editable/generated message; `--no-commit` applies the inverse without committing. |
| [Git cherry-pick](https://git-scm.com/docs/git-cherry-pick/2.39.3) | Cherry-pick normally creates a new commit for the selected change; `--no-commit` stages it; `-x` can append source provenance. |
| [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) | A conforming subject must begin with `type[optional scope]: description`; footers may follow Git-trailer-like syntax. |

Strict identity-first placement and strict Conventional Commit conformance cannot both
own byte zero: an external identity prefix makes the type non-leading, while a
type-first form makes identity non-leading. TFW can retain action tokens such as
`docs:` after its identity, or choose Conventional-Commit-first placement, but it must
not claim both strict contracts simultaneously.

### G6. Candidate grammar observations

Representative Researcher prefixes measured in the synthetic corpus:

| Candidate | Example prefix | Prefix characters | Observation |
|-----------|----------------|------------------:|-------------|
| G1 user hyphen/order | `codex-tfw-49-researcher-research-iter1:` | 39 | compact, but `claude-code`, task hyphens, role, and work scope require escaping or a schema-aware parser |
| G2 fixed labeled brackets | `[agent:codex][task:TFW-49][work:research-iter1][role:researcher]` | 64 | self-describing, exact-field grep and diagnostics are simple, but visually heavy |
| G3 compact slash/fixed order | `[codex/TFW-49/research-iter1/researcher]` | 40 | shortest unambiguous fixed-position form in this set, but field meaning depends on memorized order |
| G4 Conventional-Commit-first | `docs(tfw-49-research-iter1): [codex/researcher]` | 47 | strict type-first compatibility, but fails the approved identity-first principle and task/role field clarity |
| G5 mandatory subject identity plus optional trailers | G2 or G3 subject; optional `Agent-Model`/`Agent-Session` trailers | subject-dependent | keeps volatile detail out of `--oneline`; trailers alone are insufficient because the core identity would be hidden |

G2 was used as the behavior-fixture grammar because its field boundaries make
diagnostics and test interpretation explicit. That choice is a fixture control, not a
Gather recommendation. Exact `git log --grep` filters over the fixture independently
matched agent, task, work scope, role, and reserved `fixup!`/`squash!` forms.

The evidence supports these semantic separations:

- `agent` should describe the stable interaction surface (`codex`, `claude-code`),
  not the model;
- `role` should describe the active TFW Role Lock;
- model and exact session are volatile/specific optional metadata if retained;
- Git author/committer remain the account-level metadata and should not be duplicated
  as the mandatory agent field;
- task and work scope must distinguish master, phase, research iteration, and
  lifecycle/non-task work;
- co-author trailers remain contributor metadata and do not replace acting-agent
  provenance.

### G7. Synthetic local-hook behavior

All behavior used synthetic hooks and temporary repositories. No production hook was
executed or modified.

The G2 validator accepted:

- Coordinator/master, Researcher/research iteration, Executor/phase, and
  Reviewer/phase cases;
- two agent surfaces (`codex`, `claude-code`);
- docs, knowledge, release, and `task:none` maintenance scopes;
- a human commit with no agent activation;
- standard `Co-authored-by` trailers;
- same-context `--amend --no-edit`;
- leading Git-reserved `fixup!` and `squash!` markers before a valid identity;
- explicit identity-first merge, revert, and cherry-pick commits after `--no-commit`
  flows;
- default and `--cleanup=strip` subjects while Git applied the documented body cleanup.

It rejected with a complete corrected example:

- agent activation with missing identity;
- malformed context;
- subject/context mismatch;
- a different-role amend that retained the prior subject;
- an identity-bearing subject presented without the agent entrypoint.

Mechanism boundaries observed:

| Case | Observation | Disposition effect |
|------|-------------|--------------------|
| Synthetic mutating prepare hook | prepended `[main]:`; a pre-prefixed message became `[main]: [main]: ...`; `--no-verify` did not suppress mutation | A mutator is not an idempotent validator and can corrupt otherwise meaningful order |
| Existing-hook chain | a synthetic prior `commit-msg` ran before the TFW validator on every applicable attempt on Windows and Ubuntu | Preservation by generated dispatch is feasible without copying an existing hook body |
| Agent omits activation | plain commit succeeded and is indistinguishable from the allowed human path | H4's deterministic agent-only claim is false without a trusted external actor signal |
| Agent self-declares human | plain commit succeeded | Self-declaration cannot establish truth |
| `git commit --no-verify` | malformed agent commit succeeded | Local `commit-msg` is an ergonomics/structural gate, not absolute enforcement |
| Merge default message | `commit-msg` ran and rejected missing/mismatched identity; an explicit identity-first merge commit then succeeded | Merge is locally coverable but needs a documented message flow |
| Automatic revert | created `Revert "..."` under a different actor context without running the synthetic `commit-msg` validator | `commit-msg` alone does not cover Git 2.42 sequencer behavior |
| Automatic cherry-pick | created a structurally valid copy of the source subject under a different actor context; `commit-msg` did not run | A replay can look compliant while attributing the new commit to the prior agent/task/work scope |
| Revert/cherry-pick `--no-commit` plus explicit commit | the explicit new commit ran both local hooks and retained source linkage in a trailer | A truthful explicit replay flow is feasible, with higher workflow cost |
| Offline structural scan | 20 subjects were structurally leading; two default reverts had nested prior identities; five subjects lacked identity | The commit objects cannot distinguish the three simulated agent bypasses from the two human commits |

The automatic revert/cherry-pick observation narrows H3 as well as H4: a versioned
`commit-msg` validator is a useful core consumer, but it is not by itself complete for
all commit-producing Git commands.

### G8. Synthetic server/review behavior preserves the same truth limit

A temporary bare repository used a synthetic `pre-receive` rule:

- a correctly labeled commit on an `agent/*` ref was accepted;
- an unlabeled commit on an `agent/*` ref was rejected;
- the identical unlabeled commit was accepted when the invoker pushed it to a
  `human/*` ref.

Thus server/CI range validation can enforce grammar for a population selected by a
trusted hosting identity, protected workflow, or authenticated automation account. A
branch/ref name chosen by the same invoker merely relocates self-declaration and does
not solve the human-versus-agent classification problem.

A truthful contract can claim:

> When an agent commit enters through the TFW agent entrypoint or a trusted external
> actor policy classifies it as agent-created, the subject grammar is validated
> locally and/or at review/server boundaries. The mechanism does not prove that an
> unclassified commit was human-created.

### G9. Portability coverage

The same POSIX-`sh` synthetic dispatcher/validator ran in:

- Git for Windows `2.42.0.windows.1` on Windows NT 10.0.26200.0; and
- native Ubuntu Git `2.43.0` under WSL.

Both accepted a valid Codex/Researcher/research-iteration subject, allowed the plain
human baseline, rejected missing agent context with the same actionable diagnostic,
and invoked the synthetic prior hook. Git-for-Windows `sh -n` also accepted every
synthetic hook file.

This supports portable shell syntax and the two observed runtimes. It does not prove
GUI/IDE propagation of environment context, executable-bit installation on every
filesystem, JGit behavior, or hosted-server behavior. Those remain implementation
Proof obligations rather than Gather assumptions.

### G10. Enforcement configurations remain materially distinct

| Configuration | What it can establish | Honest boundary |
|---------------|-----------------------|-----------------|
| Prose only | shared intent when agents comply | no structural observation; ordinary drift is silent |
| Mutating `prepare-commit-msg` | can insert/alter text and cannot be skipped with `--no-verify` | can invent provenance, double-prefix, act before editing, and interfere with Git-reserved messages |
| Validating `commit-msg` | final-message grammar and actionable local rejection for ordinary `git commit`/merge | `--no-verify`; automatic revert/cherry-pick gap; no independent actor classification |
| Agent wrapper/entrypoint | establishes explicit surface/task/work/role context for comparison | direct Git invocation bypasses it; same actor can lie or omit activation |
| CI/server scan | validates landed/pushed ranges outside the local hook | requires a trusted rule that selects which commits are agent-created; branch self-declaration is insufficient |
| Layered local plus review/CI | combines fast feedback with independent range validation and migration checks | still provenance-by-contract unless external authentication identifies the agent population |

No single mechanism in the corpus supplies both ergonomic context and authenticated
human/agent truth. Extract must therefore configure a contract, consumer set, replay
policy, migration lifecycle, and explicit non-claim together.

## Checkpoint

| Coverage and exclusions | Decision effect | Remaining gap / authority outcome | Saturation |
|-------------------------|-----------------|-----------------------------------|------------|
| Covered current TFW log, duplicate cases, `9e19a4f`, redacted effective/local hook topology, all canonical workflows and adapter/init/update/config/docs/knowledge/release surfaces, Atamat/Helpdesk/AFD histories, official Git/Conventional Commit sources, grammar/filter/diagnostic comparisons, and synthetic Windows/Ubuntu local plus bare-server fixtures. Excluded production mutation/execution, arbitrary or sensitive hook contents, secrets/personal memory, history rewrite, GUI/JGit/hosting-provider-specific behavior, and authenticated external actor systems not present in the corpus. | H1/H2 remain plausible; H3 is narrowed because `commit-msg` misses automatic revert/cherry-pick and is bypassable; H4 is refuted as an agent-only deterministic guarantee; H5 must separate known-legacy supersession from unrelated-hook chaining under external/global topology; H6 requires Git-reserved and replay-specific behavior rather than one unconditional prefix. | Extract must define coherent grammar/enforcement/migration configurations and explicit provenance non-claims. Coordinator/owner must later decide whether to add trusted hosted identity policy; absent that, the claim must remain contractual rather than authenticated. Sensitive-material rotation/removal remains an owner action outside TFW-49. | Additional reachable local subjects stopped changing the factor inventory. The two runtimes and official semantics converged on the same local boundary. The remaining gaps are configuration/design and external-authority questions owned by Extract/Challenge or the Coordinator, not missing Gather corpus. |

**Sufficiency:**
- [x] Material evidence/corpus coverage and exclusions are explicit?
- [x] Material decision factors, alternatives, or comparison structure are established?
- [x] The decision effect or explicit unresolved result is stated?
- [x] Further available evidence is not changing a material disposition, or the limitation is explicit?

## Learning Receipt

| Signal and trigger | Disposition | Required relation | Responsible actor |
|--------------------|-------------|-------------------|-------------------|
| Effective hooks are selected by external/global `core.hooksPath`; the repository-local prepare hook is a dormant identical copy, and an unrelated sensitive global hook must remain excluded. This contradicts the HL's simple "active local hook" model and changes migration ownership. | derive | Carry into Iteration 1 RES and Coordinator HL/Phase C planning as a topology-first, no-content-ingestion, chain-or-supersede migration requirement; backlink to G3. | Researcher derives; Coordinator owns HL/TS disposition; owner separately handles rotation/removal |
| An agent can omit activation or self-declare the human path, and local/server rules cannot infer the truth from the resulting commit object. This refutes H4's deterministic agent-only claim absent trusted external actor classification. | derive | Carry as H4 refutation and explicit non-claim into RES; Coordinator must narrow the target contract and any later TS/DoD language; backlink to G7-G8. | Researcher derives; Coordinator owns claim correction |
| Automatic revert and cherry-pick created commits without the synthetic `commit-msg` validator; cherry-pick copied a valid but prior agent identity under a different acting context. This contradicts H3's sufficiency claim and changes replay architecture. | derive | Carry into RES and Phase A/B planning as a required source-operation policy and coverage proof; backlink to G5/G7. | Researcher derives; Coordinator owns architecture selection |

Stage complete: YES
→ User decision: APPROVED — Coordinator accepted decisions 1–3 after full inspection and authorized Extract; H4 is refuted as an authenticated/deterministic claim, mandatory-core synthesis must separate operator role from optional origin metadata, replay operations require explicit truth-preserving handling, and migration must remain topology-only and secret-safe.
