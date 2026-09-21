# PROPOSAL — FRATS-D01: Operational Control Boundaries

> **Date**: 2026-09-21
> **Owner**: saubakirov
> **Author**: current FRATS Coordinator acting on behalf of saubakirov via Codex
> **Status**: PROPOSAL — deferred, non-normative planning input
> **Entry point**: `/tfw-plan` for a separately initiated task
> **Origin**: FRATS iteration-2 recommendations F1–F3 and the owner's direct request to preserve
> the deferred work without expanding the current refactoring task.

This proposal is not a task, mandate, lock, security policy, approval record, implementation order,
release authorization or dependency of FRATS. It changes no current workflow or repository rule.

## 1. Purpose

Design operational controls whose truth depends on infrastructure outside ordinary TFW artifacts:

1. serialization of landing and release effects on a shared target;
2. enforceable capability profiles for tools, environments and protected resources;
3. approval provenance stronger than an ordinary Git author field where a real reader requires it.

These subjects share one boundary: a prose instruction may declare intent, but it cannot prove
exclusive ownership, least-privilege enforcement or trusted approval.

## 2. Why this work is outside FRATS

FRATS owns instruction topology, role communication, session identity, artifact consistency and
semantic compression. It may preserve the honesty rules needed by later controls, but it has no
approved scope to install branch protection, deployment gates, provider permissions, OS isolation,
credential boundaries, signatures or an external authorization service.

Adding partial versions of those mechanisms to FRATS would create three false assurances:

- a repository file or task scan would be mistaken for an atomic landing lock;
- a prompt saying “beta only” would be mistaken for removal of production access;
- a Git author name would be mistaken for proof that architecture approval was valid.

## 3. Candidate work package F1 — landing and release ownership

### Question

How should one landing or release effect at a time be enforced for each actual shared target while
isolated candidate work may continue in parallel?

### Required decisions

| Decision | Required distinction |
|---|---|
| Target identity | Repository branch/ref, release metadata, tag and deployment environment are separate targets unless one platform operation binds them atomically. |
| Landing owner | A task or agent identity names responsibility but does not itself fence the target. |
| Admission | Scope comparison is advisory risk reduction, not a lock or proof of semantic independence. |
| Currentness | Landing evidence must be replayed against the actual current target baseline after any target movement. |
| Enforcement | Use branch/service/IAM controls where exclusivity matters; disclose a merely procedural boundary. |
| Recovery | Preserve stale and abandoned candidates; define supersession, human override and release of ownership without rewriting history. |

### Rejected shortcuts

- one universal mutating lane for the whole repository without evidence of a shared target;
- a maintained global scheduler merely to represent task state;
- a repository lease file that external or offline writers can bypass;
- treating worktree isolation as branch, tag or deployment isolation.

### Worktree topology that must be decided, not assumed

The current canon assigns one mutation owner to each delegated mutating-run worktree, and the
current Codex team profile uses separate worktrees for mutating units. A future task must compare
that model with the owner's simpler serial alternative:

| Alternative | Potential value | Required challenge |
|---|---|---|
| Separate worktree per mutating unit | Strong filesystem/index isolation and parallel candidates | Creates crossing, landing, status propagation and repeated integration cost between roles. |
| One worktree per task/phase with sequential ownership transfer | One visible task state and no intra-task candidate merge when roles run serially | Must prevent concurrent writes, preserve independent review, identify the current owner and recover safely from an unavailable holder. |

Do not infer “one worktree per agent” from an agent name, or “one worktree per task” from the path
name. The selected unit of isolation must follow the actual concurrency and mutation boundary. A
serial task may reuse one task/phase worktree only after the future contract defines exclusive
handoff, stale-session refusal, review behavior and cleanup.

## 4. Candidate work package F2 — enforceable capability profiles

### Question

How can a task-local mandate be matched to the capabilities actually exposed to its runtime—for
example beta but not production, one module but not another, read-only versus mutation, or a bounded
set of tools and network destinations?

### Required decisions

| Layer | Required evidence |
|---|---|
| Declared mandate | Exact task, role, scope, allowed effects, reservations and expiry/revocation conditions. |
| Runtime profile | Actual provider, account, host/container, filesystem, tool, network, secret and environment exposure. |
| Binding | Proof that the launched unit used the intended runtime profile; a name or session title is insufficient. |
| Default and exception | Fail-closed versus advisory operation, unavailable-control behavior and explicit human break-glass path. |
| Verification | Safe negative checks proving that forbidden production/resource effects are unavailable, not merely discouraged. |
| Recovery | Rotation/revocation, interrupted work, provider capability changes and honest downgrade reporting. |

### Fixed boundary

A stable principal, workflow role and task-local mandate remain separate from technical capability.
The effective action is their intersection with the actual exposed controls. A prompt-only limit is
procedural guidance and must never be reported as least-privilege enforcement.

## 5. Candidate work package F3 — approval provenance

### Question

When is owner approval plus an exact immutable artifact/blob sufficient, and when does a material
reader require stronger proof such as protected refs, signed commits/tags or service attestations?

### Required decisions

1. Name the concrete reader and consequence before adding stronger provenance.
2. Keep content identity, Git authorship, human approval, delegated mandate and technical
   authentication as separate facts.
3. Define the smallest trusted statement: who approved which exact bytes, for what scope, at what
   epoch and under which revocation/supersession rule.
4. Preserve operation when signing or identity infrastructure is unavailable without silently
   upgrading ordinary metadata into proof.
5. Avoid turning TFW into a general identity-management or certificate platform.

### Current sufficient baseline

For FRATS, direct owner approval plus the exact frozen artifact and commit/blob lineage remains
sufficient. Ordinary Git author metadata is attribution only and grants no architecture authority.

## 6. Recommended decomposition

Use three separately approvable tasks rather than one implementation task:

| Proposed task | Why separate | Possible dependency |
|---|---|---|
| Target landing and release control | Repository/service concurrency and recovery problem | May consume capability controls if a protected target already exposes them. |
| Runtime capability profiles | Provider, OS, tool, network and environment enforcement problem | May supply beta/prod enforcement to landing or deployment. |
| Trusted approval provenance | Reader-driven trust and attestation problem | Optional; starts only when ordinary owner approval plus immutable bytes is insufficient. |

They may share research vocabulary, but no task should wait for another unless its approved HL names
the exact dependency. The approval-provenance task may never be needed.

## 7. Invariants for every future task

- Agent names and session titles grant nothing.
- Role Locks cannot be widened by a runtime profile.
- A technical capability does not imply permission to use it.
- A mandate that exceeds actual capability remains unexecutable, not partially satisfied in secret.
- A task scan, status file or proposal is not a distributed lock.
- Security and exclusivity claims require native negative evidence at the enforcing boundary.
- Human override remains explicit and traceable; emergency action is not retroactively normalized.
- No implementation, agent launch, release, protected-resource mutation or credential request follows
  from this proposal alone.

## 8. Planning inputs and start boundary

The later Coordinator should begin from FRATS iteration-2 decisions D16–D18 and recommendations
F1–F3 at commit `29c17dc`, then inspect the actual target platforms before writing an HL. It must
not infer that every repository needs all three tasks or that one provider's controls transfer to
another.

The next act is deliberately unscheduled. When the owner selects one work package, start a new
`/tfw-plan`, approve its full title and abbreviation, and establish its own research and execution
boundary. FRATS does not wait for it.

---

*PROPOSAL — FRATS-D01: Operational Control Boundaries | 2026-09-21*
