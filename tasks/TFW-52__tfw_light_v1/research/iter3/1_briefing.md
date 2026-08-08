# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW-52](../../HL-TFW-52__tfw_light_v1.md)
> Goal: Determine whether Team has a stable, independently useful working mechanism between Assisted and Full, while preserving the simpler Assisted-plus-subagents answer if H9 fails.

## Research Plan

### Gather

- Build an evidence-lane matrix that separates current official Codex support, behavior observed in this local desktop task, unavailable or untested behavior, and proposed TFW behavior for subagents, collaboration agents, user-owned tasks/threads, independent sessions, worktrees/shared checkouts, messaging, waiting, handoff, context, permissions, approvals, visibility, and persistence.
- Decompose the Team decision into independent dimensions: coordination authority, session ownership, execution isolation, context transfer, communication channel, approval boundary, artifact ownership, review independence, persistence/resume, and upward compatibility.
- Compare at minimum four mechanisms: one-session subagents, coordinator-controlled collaboration agents, separate user-owned app tasks/threads, and truly independent human/agent sessions; record what each can and cannot do beyond Assisted.
- Model owner, coordinator, executor, and reviewer responsibilities across task intake, Working Backwards planning, assignment, handoff, blocking questions, status, shared artifacts, review, interruption/resume, stale context, concurrent edits, and completion.
- Seek direct counter-evidence from the outset: cases where Assisted plus ordinary subagents is sufficient, separate tasks cannot coordinate, role separation is only nominal, shared checkout creates races, and Team artifacts add ceremony without measurable assurance.

### Extract

- Build a Configuration Space across coordination mechanism, session independence, checkout isolation, communication/persistence, role separation, and artifact spine; keep a no-Team configuration live as the falsification control.
- Define explicit tests for a distinct Team mechanism: cross-session ownership, durable routable blocking questions/status, independently inspectable handoff, genuinely independent review, collision-safe artifact ownership, and resumability without hidden chat context.
- Test role-collapse configurations for 2–3 people: owner/coordinator, coordinator/executor, executor/reviewer, and coordinator/reviewer; identify which separations create independently verifiable value and which merely rename one actor.
- Derive the smallest Team artifact spine and an exact mapping into Full HL/TS/ONB/RF/REVIEW, preserving semantic continuity without claiming Full gates, evidence, or bureaucracy prematurely.
- Produce lifecycle scenarios for normal completion, blocked work, interrupted/resumed sessions, stale instructions, parallel edits in a shared checkout, isolated worktrees, rejected handoff, and reviewer loss of independence.

### Challenge

- Pairwise-attack every surviving configuration against capability limits, approval/visibility boundaries, shared-checkout races, stale context, lost messages, orphaned tasks, hidden coordinator dependence, and inability to verify reviewer independence.
- Attempt to falsify H9 by showing that Assisted plus subagents or coordinator-controlled agents supplies the same measurable outcomes with fewer roles and artifacts.
- Attempt the converse only after falsification: identify any capability that requires durable, separately owned sessions/tasks or independent human/agent authority and cannot be reproduced by one-session delegation.
- Eliminate roles and artifacts that add no measurable control, trace, isolation, or recovery value; reject configurations that silently expand into the Full lifecycle.
- State a bounded verdict—supported, refuted, or conditional—plus whether Team deserves a stable edition, the minimum viable role/artifact set if it does, and exact UNAPPROVED HL diffs without applying them.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H9 | Team can be a separate stable edition between Assisted and Full only if Codex tasks/threads provide verifiable separation of coordinator, executor, and reviewer beyond ordinary subagents. | needs-research |

## Scope Intent

- **In scope:** H9 only; current official Codex distinctions; safe read-only local/app observations; comparison of delegation/session mechanisms; minimum Team roles; lifecycle and communication; independent-review value; checkout/edit isolation; minimal Team-to-Full artifact mapping; active counter-evidence; exact transparent and unapplied HL change proposals.
- **Out of scope:** modifying the approved master HL or plan; reopening edition topology, Light, or Assisted design; implementing Team; changing `README.md`, `research/iterations.yaml`, TS/product/adapter/code files, or predecessor research; commits/staging; external writes; creating user-owned tasks/threads or subagents without an explicit bounded-experiment authorization from the coordinator.

## Guiding Questions

1. What observable capability, if any, distinguishes Team from Assisted plus ordinary subagents strongly enough to justify a stable edition?
2. What is the smallest role, lifecycle, communication, and artifact model that makes coordination and review independently verifiable for 2–3 people without becoming Full?
3. Under which current Codex execution model—shared-session agents, coordinator-controlled agents, separate app tasks/threads, isolated worktrees, or independent human/agent sessions—do those guarantees actually hold, and where do they fail?

## User Direction

- Run iteration 3 in DEEP mode as a separate Researcher session; H9 is the only hypothesis.
- Treat the approved master HL and plan as immutable. Research may confirm, challenge, or recommend exact transparent diffs, but every proposed change remains **UNAPPROVED** and unapplied.
- Carry iteration 1 and iteration 2 only as boundary conditions. Do not reopen edition topology or Assisted design.
- Do not assume Team is necessary. Try to falsify H9 and preserve Assisted plus subagents if it is sufficient.
- Use safe local read-only and permitted task/app evidence. Do not create user-owned tasks/threads or subagents unless the coordinator explicitly authorizes a bounded experiment at a checkpoint. Make no external writes.
- Write only this iteration's `1_briefing.md`, `2_gather.md`, `3_extract.md`, `4_challenge.md`, and `RES.md`; use every DEEP checkpoint and stop for coordinator authorization before advancing.

---
Stage complete: YES
Coordinator record: Briefing accepted on 2026-08-08; Gather authorized.
