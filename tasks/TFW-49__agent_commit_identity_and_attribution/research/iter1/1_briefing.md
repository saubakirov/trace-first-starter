# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I name the decision-changing uncertainty, explain why comparison fits, and state what result would change our approach?"
> Parent: [HL-TFW-49](../../HL-TFW-49__agent_commit_identity_and_attribution.md)
> Goal: Every commit created by an AI agent identifies its origin at the beginning of
> the subject in one compact, canonical form, connecting Git history truthfully to
> agent surface, TFW role, task, and phase or research scope without replacing Git
> authorship, proof, attestation, or review.
> Mode: Pipeline — Deep
> Iteration: 1

## Comparative Procedure Fit

| Decision to support | Material alternatives / relationships / configuration question | What result would change the approach | Fit |
|---------------------|----------------------------------------------------------------|---------------------------------------|-----|
| Recommend the smallest truthful, searchable cross-agent commit-identity grammar and the enforcement/installation/migration architecture that TFW should plan | Compare semantic fields and their authority; subject-leading grammar/order/delimiters; optional trailers; context establishment; prose, mutating, validating, wrapper, CI/server, and layered enforcement; hook distribution and non-destructive migration | Evidence that a smaller grammar loses required filtering/truth, that a field cannot be established honestly, that Git-native behavior is corrupted, or that an enforcement layer cannot distinguish scoped agent commits without blocking humans will eliminate or narrow the configuration | **FIT** |

The Comparative Decision Procedure fits because the uncertainty is a bounded choice
among material grammars, semantic identity models, enforcement layers, and
installation/migration configurations. The alternatives share observable criteria and
can be challenged in isolated Git fixtures. This is not a direct lookup: official Git
semantics constrain the space, while repository history and fixture behavior determine
which configuration is truthful and usable for TFW.

## Research Plan

### Gather

- Establish the current-state corpus without mutation: inspect TFW history including
  the duplicated `[master]` subject and transitional `9e19a4f`, the active
  `.git/hooks/prepare-commit-msg`, relevant repository-local Git config origins, and
  every canonical workflow/convention/adapter surface that can directly or indirectly
  produce a commit. Distinguish the one prospective semantic owner from point-of-action
  consumers.
- Read-only inspect representative commit subjects and hook/config conventions in the
  available Atamat, Helpdesk, and AFD canonical roots. Report missing roots or
  inaccessible evidence instead of inferring it. Do not inspect secrets or personal
  memory.
- Use primary technical authority only: the installed Git version plus official Git
  documentation for hook invocation and bypass, `core.hooksPath`, cleanup, trailers,
  amend, merge, revert, fixup/squash, and cherry-pick; and the official Conventional
  Commits specification if it remains a material grammar option. Record access date
  and version applicability.
- Build temporary Git repositories outside production roots and exercise candidate
  subject grammars and hook configurations across all required roles/scopes,
  human/agent states, valid/false/missing context, Git-generated message flows,
  existing hooks, diagnostic quality, search/filter ergonomics, and available
  Windows/POSIX execution surfaces.

### Extract

- Separate identity dimensions: agent surface, model, account/author, session, TFW
  role, task scope, sub-scope, action/type, and optional attribution metadata. Determine
  which are mandatory, optional, derived, supplied, or unverifiable.
- Compare at minimum the user example/order, fixed bracketed fields, compact
  slash/colon scope, Conventional-Commit-compatible placement, and mandatory
  subject-leading identity plus optional trailers. Structure only configurations that
  preserve required semantics and normal Git meaning.
- Cross-reference grammar with enforcement, context-establishment, installation,
  coexistence, repair, migration, and bypass-boundary choices. Keep semantic ownership
  separate from local consumers and physical hook placement.

### Challenge

- Attack the strongest surviving configuration with false agent self-declaration,
  ordinary human commits, `--no-verify`, amend/revert/merge/fixup/squash/cherry-pick,
  co-author trailers, cleanup modes, missing context, stale context, existing user
  hooks, worktrees, Windows/POSIX portability, and actionable correction behavior.
- Test whether any client-side mechanism can distinguish a human from an agent without
  a trusted external signal. If not, narrow the promise to an explicit workflow
  contract and state exactly what validation can and cannot establish.
- Seek configurations that preserve current user hooks and prospective history without
  rewriting, double-prefixing, or claiming that provenance is Proof Record, RF
  attestation, or REVIEW acceptance.

### Synthesis

- Recommend the smallest supported grammar and field semantics; the canonical owner
  and point-of-action consumer map; the minimum enforcement layers and honest bypass
  boundary; and an install/verify/repair/migration architecture with explicit
  limitations and phased HL update recommendations.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H1 | A fixed subject-leading identity with separate agent, task/scope, and role fields is materially easier to recognize and filter than Git author metadata, branch prefixes, free-form prose, or trailers alone | open |
| H2 | A stable agent-surface identifier plus TFW role is more durable and truthful than a model-version or exact-session identifier as the mandatory core; more specific identity can remain optional metadata | open |
| H3 | One canonical grammar plus a short point-of-commit imperative and a versioned `commit-msg` validator provides the smallest reliable enforcement contract; documentation-only or a mutating `prepare-commit-msg` hook is insufficient | open |
| H4 | Agent-only enforcement can be made deterministic without blocking human commits if agent workflows establish explicit context that the validator verifies rather than invents | open |
| H5 | `core.hooksPath` with conflict-aware init/update migration can supersede the current `[master]:` hook while preserving unrelated user hooks and normal Git operations | open |
| H6 | The contract can handle merge/revert/amend/fixup/release exceptions with a small explicit grammar rather than workflow-specific formats | open |

## Scope Intent

- **In scope:** Commit subject identity semantics; required versus optional dimensions;
  Git-author and trailer relationships; agent/human scope truth; actual TFW
  commit-producing surfaces; versioned semantic ownership and point-of-action
  consumption; validating/mutating/wrapper/CI enforcement options; diagnostics;
  installation, coexistence, verification, repair, rollback, and prospective
  migration; temporary-repository behavioral tests.
- **Out of scope:** Implementing or modifying framework/runtime files; changing real
  hooks or Git config; creating production commits, branches, tags, or pushes;
  rewriting history; changing Git author metadata; treating identity as proof,
  attestation, or review acceptance; executing comparison agents/models; accessing
  secrets or excluded personal-memory files.
- **Declared corpus / evidence families:** Approved TFW-49 HL and Project Values; TFW
  Git history and active local hook/config state; complete current workflow,
  convention, adapter, init/update/release/config/docs/knowledge surfaces;
  representative Atamat/Helpdesk/AFD histories and hook/config conventions when
  available; official Git documentation and installed Git behavior; official
  Conventional Commits specification if relevant; isolated temporary Git fixtures.
- **Known exclusions:** Client-side hooks cannot create a security boundary against a
  user with repository control; server-side policy availability may not be observable
  locally; exact behavior on unavailable operating systems/shells must be reported
  rather than simulated; production histories are observational and cannot prove
  causal superiority; untracked personal-memory and secret-bearing files are excluded.

## Guiding Questions

- Which mandatory subject-leading fields and order are the smallest set that preserves
  truthful task/sub-scope, TFW role, and agent-surface filtering without conflating
  model, account, session, author, or action?
- What explicit signal can honestly place a commit inside the agent-authored policy,
  and what can a validator prove when a human or agent can falsify that signal?
- Which layered enforcement and lifecycle configuration validates ordinary agent
  commits, preserves Git-generated flows and unrelated hooks, and states the
  `--no-verify`/client-control boundary without overstating enforcement?

## User Direction

- The user delegated research and workflow decisions to the Coordinator task
  `019fa70f-8db9-70a3-8109-c69ff35c9592`; all WAIT decisions go there, not directly to
  the user.
- The Coordinator approved Pipeline — Deep intensity and declared the Comparative
  Decision Procedure FIT.
- The Coordinator created `research/iterations.yaml` in commit `cf2abe9`; its Iteration
  1 focus, H1–H6, source families, and pending state are binding inputs.
- Research writes only `research/iter1/` artifacts through RES and stops. All
  repository, hook, config, history, and production-project inspection is read-only.
  Candidate mechanisms run only in temporary Git repositories.

## Checkpoint

| Decision effect | Remaining gap / authority outcome |
|-----------------|-----------------------------------|
| The plan can compare field semantics, grammar, enforcement, context truth, and lifecycle architecture against one declared corpus and adversarial fixture suite | Coordinator must approve or revise the declared corpus, temporary-fixture boundary, identity dimensions, and three decision questions before Gather |

## Learning Receipt

**No selected signal.** The Coordinator's mode, fit, control-file, and boundary
directions instantiate already approved task authority; they do not add a new durable
or contradictory project signal at this checkpoint.

---
Stage complete: YES
→ Coordinator decision: APPROVED decisions 1-3. Briefing accepted as written;
  Iteration 1 marked `in_progress` in the Coordinator-owned control file and pushed in
  `f110618`. Proceed to Gather under the declared corpus, temporary-fixture-only
  behavior tests, primary-source rule, explicit human/agent truthfulness challenge,
  and all read-only/no-implementation boundaries. Preserve `No selected signal` unless
  Gather produces a genuinely durable or contradictory signal.
