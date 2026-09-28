---
description: TFW Release — prepare a release according to the receiving project's own contract
---

# TFW Release — Project-Defined Release Workflow

> **Role:** Coordinator for Full work; authorized Daily worker for a Daily result
> **Trigger:** explicit release preparation request or the project's recorded release trigger
> **Prerequisite:** an applicable project release contract, when the project has one

> **🔒 ROLE LOCK: COORDINATOR (Full) / AUTHORIZED DAILY WORKER (Daily)**
> Permitted: release preparation and separately authorized project release effects. Forbidden:
> implementation, task planning/execution/review artifacts, and implicit tag/push/publish/deploy.

## Read Contract

Read in order. A project without releases or `RELEASE.md` remains valid for ordinary work.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | selected task/phase `status.md` and `journal/` for Full; selected record for Daily | actual route, authority and lineage before readiness evidence | task-local authority |
| 2 | `RELEASE.md`, when present: `What Is a Release?`, `Audience`, `Version Scheme`, `Release Triggers`, `Pre-Release Checklist`, `Release Steps` | project-defined release contract | project |
| 3 | project version/output metadata named by that contract | identity and output | project |
| 4 | selected Full RF/EV/REVIEW or Daily result and checks | readiness evidence required by the project | governing work record |
| 5 | only selected changelog/migration/notes sources | release explanation and obligations | selected effect |
| 6 | final output and its checks | final verification | project contract |

Do not load every open task, infer a version scheme, or make the installed TFW version the project's
release version. Missing required contract headings, ambiguous selected evidence, or malformed selected
state stops the selected release effect, not unrelated routine work.

## Activation and routing checkpoint

Apply the active root activation/routing contract before material work. Full task-bound current work
requires a complete spine; total legacy absence is read-only and partial/mismatched routing refuses.
For Full work this unit must be the actual Coordinator, with authority through its recorded upward
route. For Daily, resolve the actual owner's release authorization and the selected record; no Full
role, routing spine or task artifacts are invented. A Daily worker may perform the release effects
that the owner and project contract authorize. A trigger or completed result alone grants none.
Every external effect remains separately authorized. A historical `owner_gateway` carrier retains
its own epoch; a phase result cannot grant release authority.

## Step 1 — Resolve the Project Release Route

The selected effect first resolves **Scope and Version** under the project's contract. If no trigger
fires, stop before preparation; a pre-release failure is also a stop.
Apply `RELEASE.md` Release Triggers before preparing any release metadata.

If no release procedure exists, explain that ordinary task completion remains valid and offer a bounded
planning route for the owner to define output, audience, identity/version rule, readiness evidence,
permitted effects, and next steps. Do not create `RELEASE.md`, Git requirements, SemVer, a tag, or a
publication destination automatically.

If a procedure exists, preserve its customizations and apply its own identity, trigger, audience, output,
and permission rules. A release of an application, report, document, or data product must not bump the
installed TFW version merely because TFW instructions were used.

## Step 2 — Select Effect and Evidence

Start from the selected shipping effect and its actual work route:

- **Full:** resolve governing task/phase TS, RF, EV and REVIEW at their approval epoch and topology.
  A phase-only result needs no invented root RF or global all-DONE scan.
- **Daily:** use the selected record's source, scope, result, checks, limits and owner acceptance,
  plus the project's release checks and any required independent review. Do not fabricate Full
  artifacts or convert the work to Full merely to release it. Daily never waives evidence or review
  required for an actual Full result; mixed releases retain each result's own lineage.

Unrelated open tasks and harmless traces do not block a selected effect; missing proof for it does.

## Step 3 — Prepare, Verify, and Report

Resolve readiness to prepare separately from verification of the prepared result. The concrete procedure
in `RELEASE.md` owns the project-specific metadata, output and check order. The generic route is:

1. select composition and readiness evidence;
2. prepare the project's output/version/changelog/migration notes;
3. verify the final composition and every selected check;
4. commit the exact checked result if the project procedure requires it;
5. perform tag, push, publish, deploy, or notification only after separate explicit authorization.

When a changelog is part of the project contract, move only selected bullets into its versioned
section; never manufacture a release note from unrelated task bodies.

All separate external effects remain separately authorized.
Use the project's own build/package/render checks. No common route requires Python, MkDocs, Git, SemVer,
`.tfw/VERSION`, `.tfw/CHANGELOG.md`, or a tag unless the project contract says so. Preserve the original
worktree and producer commits; if integration changes operational contents, verify the changed result.

## Step 4 — Trace and safety boundary

Classify incidental sibling traces by semantic effect. A selected stable trace-only path may accompany an
authorized exact-path commit after inspection; it does not make a sibling task DONE or authorize editing
it. Operational, authority-bearing, private, verification-input, mixed-effect, or unreviewed deliverable
paths retain their own gates. Never publish a project result or expose credentials as evidence.
