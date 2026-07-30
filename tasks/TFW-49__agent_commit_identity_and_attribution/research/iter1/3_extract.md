# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does the structure reveal a consequential relationship or explain why the material options exhaust the decision?"
> Parent: [HL-TFW-49](../../HL-TFW-49__agent_commit_identity_and_attribution.md)
> Goal: Every new agent-created commit should carry truthful, subject-leading, searchable agent-surface, task/work-scope, and TFW-role provenance without replacing Git authorship, Proof Records, RF attestation, or REVIEW.

## Configuration Space

The full cross-product is not decision-safe: grammar, actor classification, replay
behavior, and hook topology have dependencies. For example, automatic cherry-pick is
not a valid value under operator-role semantics unless another mechanism replaces its
stale identity. The table therefore includes every materially distinct complete
configuration that can change the decision and excludes combinations that already
contradict a mandatory HL principle or a Gather observation.

| Config | Subject core | Operator/classification | Local and replay enforcement | Review/server layer | Installation and migration | Claim boundary |
|--------|--------------|-------------------------|------------------------------|---------------------|----------------------------|----------------|
| C1 — compact layered | fixed-order `[surface/task/work/role]` | mandatory fields describe the classified commit operator; agent entrypoint supplies context | prior-hook dispatcher → non-mutating replay guard → final `commit-msg`; explicit no-commit/re-commit for revert/cherry-pick; Git-reserved fixup/squash markers | structural range scan; trusted actor policy optional, not added by default | repository-local generated dispatcher; narrowly supersede known legacy prepare; proxy unrelated hooks by reference | contractual provenance for classified agent commits; no inference about unclassified commits |
| C2 — labeled layered | `[agent:...][task:...][work:...][role:...]` | same as C1 | same as C1 | same as C1 | same as C1 | same truth boundary as C1, with more subject noise |
| C3 — entrypoint-only | C1 or C2 | agent wrapper supplies context | wrapper constructs ordinary/replay messages; no new validator/dispatcher | optional structural scan | preserves existing hook topology unchanged | only wrapper-mediated commits; current branch mutator can still corrupt the subject |
| C4 — commit-msg-only | C1 or C2 | environment/self-declared agent activation | final `commit-msg` only | optional structural scan | install into selected hooks path | misses automatic revert/cherry-pick; `--no-verify`; cannot classify humans |
| C5 — Conventional-first | `type(scope): [surface/role] summary` | task/work/role split between scope and suffix | wrapper and/or hooks | conventional tooling/CI | any hook topology | strict Conventional compatibility, but identity is not first and fields are less separable |
| C6 — trailers/prose | plain or Conventional subject; agent detail only in trailers | natural-language or author metadata | prose only or trailer checker | offline trailer scan | no migration or local owner | identity is absent from `--oneline`; ordinary drift is silent |
| C7 — global mutation | any generated prefix | hook invents or prepends context | mutating global `prepare-commit-msg` | none required by configuration | overwrite external/global hook path or bodies | broad local reach, but false/invented provenance and unrelated-hook damage remain possible |
| C8 — hosted authenticated | C1 or C2 | hosting/automation identity classifies agent commits | local layer optional | required authenticated server policy rejects every classified agent mismatch | hosting integration plus local lifecycle | authenticated population claim, with cost and scope not required by the current practical outcome |

Inclusion rules:

1. `agent surface`, `task`, `work scope`, and `TFW role` remain separate in every
   subject-leading candidate.
2. The mandatory role means the commit operator's active TFW authority. A
   content-origin role cannot replace it.
3. Model, session, and content origin can appear only as optional metadata.
4. Human commits remain plain unless a later owner policy changes their contract.
5. Automatic replay with an inherited identity is excluded because it contradicts
   operator provenance.
6. A hosted identity system is represented for comparison but is not included in the
   leading TFW-49 architecture unless Challenge shows the practical outcome otherwise
   cannot be met.

## Findings

### E1. The leading mandatory grammar is a compact fixed-order operator identity

The leading candidate is:

```text
[<surface>/<task>/<work>/<role>] <summary>
```

Canonical examples:

```text
[codex/TFW-49/master/coordinator] approve research direction
[codex/TFW-49/research-iter1/researcher] map hook and history evidence
[claude-code/TFW-49/phase-a/executor] implement commit identity validator
[codex/TFW-49/phase-a/reviewer] verify validator and migration evidence
[codex/TFW-49/docs/coordinator] update commit identity guidance
[codex/TFW-49/knowledge/coordinator] consolidate provenance decision
[codex/TFW-49/release/coordinator] prepare release metadata
[codex/none/maintenance/coordinator] repair installed adapter metadata
```

The field order is fixed and answers four questions:

| Position | Meaning | Initial value contract |
|----------|---------|------------------------|
| `surface` | Which stable agent interaction surface invoked the commit? | registered lowercase token such as `codex` or `claude-code`; product/surface, not model, account, or session |
| `task` | Which TFW task owns the change? | canonical task ID such as `TFW-49`, or literal `none` only for genuinely non-task work |
| `work` | Which task/lifecycle slice is being committed? | `master`, `phase-<id>`, `research-iter<N>`, `docs`, `knowledge`, `release`, `config`, `init`, `update`, or `maintenance` |
| `role` | Which TFW authority operated the commit? | `coordinator`, `researcher`, `executor`, or `reviewer`; an AI release/update/maintenance action uses its actual TFW workflow role, normally `coordinator` |

The initial role registry stays aligned with the four TFW Role Locks. A human
maintainer uses normal Git author/committer metadata and the plain human path; a future
AI role requires an explicit registry change rather than silently overloading
`coordinator`.

The subject after `] ` is a concise free-form summary. It may begin with an action token
such as `docs:` or `fix:` when useful, but the resulting subject is not represented as
strictly Conventional-Commit conformant because Conventional Commits requires its type
at byte zero.

Why C1 leads C2:

- it preserves the same four independent fields;
- its representative prefix is 40 rather than 64 characters;
- slash positions are unambiguous under a closed registry and forbidden-slash value
  rule;
- each field has a stable fixed-string search:
  `^\[codex/`, `/TFW-49/`, `/research-iter1/`, and `/researcher\]`;
- the validator can diagnose each position by name even though labels are omitted from
  the subject;
- C2 remains a semantically viable fallback if Challenge shows that unlabeled order
  causes material human parsing or correction errors.

The flat user-hyphen form is eliminated as the leading grammar because `claude-code`,
`TFW-49`, `phase-a`, and `research-iter1` all contain meaningful hyphens; parsing them
requires escaping rules without producing a shorter prefix than C1. Conventional-first
and trailer-only forms are eliminated by the approved identity-first requirement.

### E2. Git-reserved markers are a narrow byte-zero exception, not another grammar

Git autosquash meaning requires these markers to remain first:

```text
fixup! [codex/TFW-49/phase-a/executor] implement validator
squash! [codex/TFW-49/phase-a/executor] implement validator
amend! [codex/TFW-49/phase-a/executor] implement validator
```

The canonical parser is therefore:

```text
subject :=
  [ git_reserved_marker SP ]
  "[" surface "/" task "/" work "/" role "]"
  SP summary

git_reserved_marker := "fixup!" | "squash!" | "amend!"
```

This is the only proposed marker allowed before the identity. It is operation syntax
owned by Git, not a second TFW identity order. Merge, revert, and cherry-pick do not
receive an equivalent leading exception:

```text
[codex/TFW-49/phase-a/coordinator] merge: integrate validator branch
[codex/TFW-49/phase-a/executor] revert: remove invalid validator behavior
[codex/TFW-49/phase-b/executor] cherry-pick: apply validator repair
```

### E3. Mandatory role means commit operator; mixed-origin content is split or disclosed

`role` cannot simultaneously mean:

- who invoked/authorized the Git commit;
- who originally authored every staged artifact; and
- who independently accepted the result.

The leading contract resolves it as the first meaning: the commit operator's active
TFW Role Lock or workflow authority. The corresponding `surface` is also the operator's
surface.

Default rule:

1. prefer atomic same-origin commits so the operator and content-producing agent align;
2. do not batch unrelated Researcher, Executor, and Reviewer outputs into one
   provenance claim merely for convenience;
3. when an inseparable commit includes content produced by a different agent/role,
   retain the operator in the subject and add one optional trailer per material origin:

```text
TFW-Content-Origin: codex/researcher
```

Optional volatile/specific metadata, when policy permits, uses trailers rather than
the mandatory core:

```text
TFW-Agent-Model: <model identifier>
TFW-Agent-Session: <opaque session identifier>
```

These trailers are not required, do not replace `Co-authored-by`, and must not contain
secrets. A session trailer may be omitted for privacy or repository-portability
reasons. Git author/committer fields continue to carry account-level attribution.

Neither the subject nor optional origin trailers are Proof Records, RF attestation, or
REVIEW acceptance.

### E4. The leading enforcement configuration is layered but keeps one semantic owner

C1 decomposes into one contract and several narrow consumers:

```text
VERSIONED COMMIT IDENTITY CONTRACT
  ├─ field registries + parser + examples + diagnostics
  ├─ point-of-action agent entrypoint
  ├─ generated local hook dispatcher
  │    ├─ prior unrelated hook by reference
  │    ├─ TFW replay guard (prepare-commit-msg, no mutation)
  │    └─ TFW final validator (commit-msg)
  └─ optional review/CI range validator
```

Responsibilities:

| Component | Responsibility | Explicit non-responsibility |
|-----------|----------------|-----------------------------|
| Versioned contract | own field semantics, registries, reserved markers, regex/parser, complete examples, diagnostic codes, and contract version | does not contain developer-specific paths or copied hook bodies |
| Point-of-action agent entrypoint | require explicit surface/task/work/role, construct or verify the subject, and dispatch the intended Git operation | does not infer task/role from branch names or changed files |
| Generated local dispatcher | preserve unrelated installed hook names by reference, order message consumers, and call the versioned validator | does not ingest, copy, quote, or diagnose external hook contents |
| Replay guard | when classified agent context is present, stop automatic revert/cherry-pick that would retain missing/stale operator identity and show the explicit replay command | does not rewrite the message |
| Final `commit-msg` validator | after prior message hooks, validate the final ordinary/merge/fixup/squash/amend subject against supplied agent context; reject identity without the agent entrypoint | does not claim coverage when bypassed or classify plain commits as human |
| Review/CI validator | scan identity-bearing commits and any commits classified by a separately trusted actor policy | does not infer agent/human status from a missing prefix or a self-chosen ref |

The hook order is consequential:

1. invoke an unrelated prior hook by reference;
2. validate the final message afterward;
3. never let a prior mutator change an already accepted identity after TFW validation.

Workflow and adapter cues remain thin:

> Before committing agent work, use the TFW agent commit entrypoint with the active
> surface, task, work scope, and Role Lock. Do not call plain `git commit` for
> agent-classified work.

They link to the one contract and carry one current example; they do not duplicate
edge rules.

### E5. H4 becomes a precise contractual non-claim

The architecture can deterministically validate the internally consistent context of
a commit that enters through the explicit agent path. It cannot authenticate the
population.

Allowed claim:

> For a commit classified as agent-created by the TFW entrypoint or by a separately
> trusted actor policy, TFW validates the subject's surface, task, work scope, and
> operator role against the supplied context.

Required non-claims:

- an unclassified commit is not inferred to be human;
- Git author/committer names do not prove surface or role;
- a branch/ref name selected by the invoker is not trusted actor classification;
- a local hook is not an authentication or security boundary;
- `--no-verify`, alternate hook configuration, direct plumbing, and direct unclassified
  Git commands remain possible outside the contractual path;
- no hosted identity system is added by C1.

C8 would change the population claim only if an owner later supplies a trusted hosted
actor mapping. Gather did not show that this is required for the user's practical
search/resume/review outcome, so it remains outside the leading TFW-49 scope.

### E6. Explicit replay is the smallest truthful operation contract in the current evidence

For a classified agent, automatic cherry-pick and revert are rejected by the
non-mutating replay guard because their generated subjects may retain the original
operator identity and the tested Git 2.42 sequencer did not run `commit-msg`.

Leading replay flow:

```text
cherry-pick:
  git cherry-pick --no-commit <source>
  TFW agent commit with current operator identity
  Cherry-picked-from: <source-oid>

revert:
  git revert --no-commit <source>
  TFW agent commit with current operator identity
  Reverts: <source-oid>
```

The entrypoint should expose these as one user-facing operation even if it performs the
two Git steps internally. This keeps the explicit provenance transaction atomic from
the agent's perspective while preserving normal Git index/conflict handling.

Compared smaller alternatives:

| Alternative | Why it is not smaller and truthful at the same time |
|-------------|------------------------------------------------------|
| Accept the inherited source identity | structurally valid but false for the new commit operator/task/work scope |
| Add only an acting-agent trailer | leaves the mandatory subject-leading identity stale |
| Let review/CI repair later | a false commit has already landed; without trusted actor context the scan cannot know it is stale |
| Mutating `prepare-commit-msg` rewrites automatic replay | reduces visible commands but enlarges the trusted mutator, operation detection, source preservation, diagnostics, and portability surface; it repeats the current mutation class |
| Define identity as original content author | avoids cherry-pick change but makes ordinary commits, amend, merge, and role authority answer a different question than the approved operator contract |

Challenge should attempt to falsify the replay guard and explicit wrapper flow, but no
smaller alternative in Gather preserves all four mandatory operator fields.

Amend policy follows the same operator rule:

- same surface/task/work/role may retain the existing identity with `--amend --no-edit`;
- changed operator context must reword the subject and revalidate;
- amending another agent's published commit is a history/authority action outside the
  ordinary entrypoint and requires explicit authorization.

### E7. Migration is a topology transaction, not a file copy

Leading C1 migration lifecycle:

1. **Discover without ingestion**
   - resolve effective hook topology and configuration scope;
   - enumerate hook names and ownership only;
   - do not read/copy arbitrary bodies or emit paths/contents in diagnostics.
2. **Recognize the legacy prepare hook narrowly**
   - supersede only the known branch mutator when a no-output equality check confirms
     it is the canonical legacy behavior already identified for this project;
   - do not generalize by filename, size, or substring;
   - any non-matching prepare hook is unrelated and is chained or blocks for owner
     conflict resolution.
3. **Generate local dispatch**
   - create an unversioned repository runtime dispatcher in Git-local state;
   - store the prior effective hook reference and install version in local Git config,
     not versioned framework files;
   - set repository-local `core.hooksPath` to the generated dispatcher, never mutate the
     user's global setting.
4. **Preserve by reference**
   - generate a proxy for every unrelated effective hook name so changing the single
     hooks directory does not silently disable checkout, merge, commit, or push hooks;
   - for `prepare-commit-msg`, skip only the recognized legacy mutator, otherwise call
     the prior hook and then the TFW replay guard;
   - for `commit-msg`, call the prior hook first and the TFW final validator second;
   - never copy prior hook bodies into the project or diagnostics.
5. **Detect conflicts and cycles**
   - resolve new and previous hook roots before writing;
   - block if the previous reference resolves to the new dispatcher, a proxy points to
     itself, ownership is ambiguous, or chaining would recurse;
   - report hook kind and remediation class without sensitive content or absolute-path
     disclosure.
6. **Verify and roll back**
   - test normal, invalid, human, merge, replay, fixup/squash, and chained synthetic
     behavior before production activation;
   - verify the repository-local config points to the generated dispatcher and all
     unrelated hook names have proxies;
   - rollback restores the exact prior local-config presence/value and removes only
     generated TFW-owned runtime files.

Lifecycle ownership:

| Owner | Responsibility |
|-------|----------------|
| Versioned method/contract | grammar, registries, parser behavior, diagnostic contract, migration invariants |
| `/tfw-init` attach/install | fresh install and existing-project topology transaction |
| `/tfw-update` | version comparison, dispatcher repair, legacy migration, consumer sync |
| `/tfw-config` | audit contract version and registered values without becoming another semantic owner |
| Workflows/adapters | point-of-action cue and exact current example |
| Owner outside TFW-49 | remove/rotate sensitive material; authorize any destructive conflict resolution or hosted identity expansion |

The repository-local `.git/hooks` directory is not a viable install target under the
observed external/global `core.hooksPath`. Replacing the global path or copying its
hooks is eliminated because it changes every repository and can ingest unrelated
sensitive material.

### E8. Configuration disposition before Challenge

| Config | Extract disposition | Reason |
|--------|---------------------|--------|
| C1 compact layered | leading challenged candidate | smallest four-field core; satisfies operator semantics, current hook topology, replay truth, and no-hosted-identity scope |
| C2 labeled layered | viable fallback | same semantics and enforcement; 24 additional prefix characters buy visible labels that Challenge may or may not justify |
| C3 entrypoint-only | conditional/non-default | preserves hook topology but cannot supersede the active branch mutator or observe direct malformed commits |
| C4 commit-msg-only | eliminate as complete architecture | useful consumer but incomplete for sequencer operations and bypassable |
| C5 Conventional-first | eliminate | contradicts approved identity-first visibility and splits fields ambiguously |
| C6 trailers/prose | eliminate | core identity is hidden and structural enforcement is absent/late |
| C7 global mutation | eliminate | invents/mutates provenance and risks unrelated repositories/hooks |
| C8 hosted authenticated | defer/out of scope | stronger authentication claim but not required by gathered practical outcome and needs separate owner/system scope |

This is not final architecture selection. C1 is the concrete leading candidate for
Challenge; the Coordinator retains selection authority after RES.

### E9. Hypothesis disposition entering Challenge

| Hypothesis | Extract disposition | Configuration consequence |
|------------|---------------------|---------------------------|
| H1 fixed subject-leading fields improve recognition/filtering | provisionally supported | challenge C1 compact positions against C2 labels and edge parsing |
| H2 surface + role are more durable than model/session | provisionally supported | mandatory C1 core; optional trailers only for model/session/origin |
| H3 one owner + cue + `commit-msg` is smallest reliable contract | partially supported, materially revised | retain one owner/cues/validator; add classified entrypoint, replay guard, and explicit operation policy |
| H4 deterministic agent-only enforcement without blocking humans | refuted as authentication/population claim | use contractual classified-agent claim and explicit unclassified non-claim |
| H5 `core.hooksPath` can preserve unrelated behavior | provisionally supported only through generated topology-aware dispatch | challenge proxy completeness, legacy recognition, order, cycles, repair, and rollback |
| H6 small exception grammar covers Git operations | provisionally supported with a split | reserved marker exception is small; replay requires explicit workflow rather than inherited identity |

## Checkpoint

| Structure and exclusions | Decision effect | Remaining gap / authority outcome | Saturation |
|--------------------------|-----------------|-----------------------------------|------------|
| Represented eight complete configurations across grammar, operator/classification, local/replay enforcement, review/server, topology lifecycle, and claim boundary. Excluded impossible cross-products: inherited replay identity under operator semantics, trailer-only identity under identity-first, arbitrary-hook copying, global overwrite, mixed-origin single-role fiction, and hosted authentication as an unapproved default. | C1 is the leading challenged candidate: `[surface/task/work/role]`, operator role, optional origin/model/session trailers, classified agent entrypoint, generated chain-by-reference dispatcher, non-mutating replay guard, final `commit-msg`, explicit replay, optional structural scan, and topology-safe init/update lifecycle. C2 is the semantic fallback if labels prove necessary. | Challenge must attack compact-order readability, registry completeness, fixup/squash/amend parsing, replay guard/wrapper failure recovery, merge behavior, hook ordering/proxy/cycle/rollback safety, GUI/context loss, mixed-origin use, and diagnostics. Coordinator retains architecture selection; hosted identity and credential handling remain owner/out-of-scope. | Additional cross-products either duplicate C1/C2 semantics or violate a Gather fact/HL invariant. The remaining uncertainty is adversarial behavior of the leading/fallback configurations, which belongs to Challenge rather than more Extract restructuring. |

**Sufficiency:**
- [x] Structure is derived from Gather's material factors/evidence?
- [x] Inclusion/exclusion rules are explicit and decision-safe?
- [x] Consequential relationships or tradeoffs are visible?
- [x] Decision effect or explicit unresolved result is stated?

## Learning Receipt

The three Gather signals remain selected and are carried without changing their
dispositions:

| Signal and trigger | Disposition | Required relation | Responsible actor |
|--------------------|-------------|-------------------|-------------------|
| Effective hooks are external/global; the repository-local prepare hook is a dormant identical copy, and arbitrary/sensitive hook contents remain excluded. | derive | C1/E7 translates the Gather G3 signal into a topology-first, chain-by-reference, known-legacy-only migration candidate; carry to RES and Coordinator HL/TS planning with backlink to Gather G3. | Researcher derives; Coordinator owns architecture/HL/TS; owner handles excluded credential action |
| Agent omission/self-declared human paths cannot be distinguished from allowed human commits without trusted external classification. | derive | C1/E5 preserves the H4 refutation as a contractual classified-agent claim plus explicit unclassified non-claim; carry to RES and Coordinator claim correction with backlink to Gather G7-G8. | Researcher derives; Coordinator owns claim language |
| Automatic revert/cherry-pick bypassed `commit-msg`, and cherry-pick retained a stale but structurally valid prior operator identity. | derive | C1/E2/E6 translates the Gather G5/G7 signal into reserved-marker syntax, a non-mutating replay guard, and explicit no-commit/re-commit/source-trailer flow; carry to RES and Phase A/B planning. | Researcher derives; Coordinator owns operation architecture |

No additional signal passed the selection test independently of these three derived
relationships.

Stage complete: YES
→ User decision: APPROVED AS CHALLENGE CANDIDATES — Coordinator accepted decisions 1–3 after full inspection; C1 leads, C2 remains the labeled fallback, and final architecture selection remains Coordinator-owned. Challenge must verify sequencer observability, cross-context autosquash truth, registry/escape coverage, full mixed-origin scope, dispatcher/worktree/rollback safety, and the contractual non-authentication boundary.
