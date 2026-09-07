---
description: TFW Release — prepare a release according to the receiving project's own contract
---

# TFW Release — Project-Defined Release Workflow

> **Role:** Coordinator
> **Trigger:** explicit release preparation request or the project's recorded release trigger
> **Prerequisite:** an applicable project release contract, when the project has one

> **🔒 ROLE LOCK: COORDINATOR**
> Permitted: release preparation and separately authorized project release effects. Forbidden:
> implementation, task planning/execution/review artifacts, and implicit tag/push/publish/deploy.

## Read Contract

Read in order. A project without releases or `RELEASE.md` remains valid for ordinary work.

| Order | Input | Checkpoint purpose | Authority |
|---|---|---|---|
| 1 | `RELEASE.md`, when present: `What Is a Release?`, `Audience`, `Version Scheme`, `Release Triggers`, `Pre-Release Checklist`, `Release Steps` | project-defined release contract | project |
| 2 | project version/output metadata named by that contract | identity and output | project |
| 3 | selected task/phase `status.md` and referenced RF/EV/REVIEW | readiness evidence | task-local authority |
| 4 | only selected changelog/migration/notes sources | release explanation and obligations | selected effect |
| 5 | final output and its checks | final verification | project contract |

Do not load every open task, infer a version scheme, or make the installed TFW version the project's
release version. Missing required contract headings, ambiguous selected evidence, or malformed selected
state stops the selected release effect, not unrelated routine work.

## 1. Resolve the Project Release Route

The selected effect first resolves **Scope and Version** under the project's contract. If no trigger
fires, stop before preparation; a pre-release failure is also a stop. If no trigger fires, stop.
Apply `RELEASE.md` Release Triggers before preparing any release metadata.

If no release procedure exists, explain that ordinary task completion remains valid and offer a bounded
planning route for the owner to define output, audience, identity/version rule, readiness evidence,
permitted effects, and next steps. Do not create `RELEASE.md`, Git requirements, SemVer, a tag, or a
publication destination automatically.

If a procedure exists, preserve its customizations and apply its own identity, trigger, audience, output,
and permission rules. A release of an application, report, document, or data product must not bump the
installed TFW version merely because TFW instructions were used.

## 2. Select Effect and Evidence

Start from the selected shipping effect, then resolve its governing task/phase TS, RF, EV, and REVIEW at
the applicable approval epoch and topology. A phase-only result does not need an invented root RF or a
global all-DONE scan. Unrelated open tasks and harmless trace arrivals do not block a selected effect;
missing proof for that effect does.

## 3. Prepare, Verify, and Report

Apply the project's checklist before writing its version/changelog/output metadata. Distinguish readiness
to prepare release artifacts from final verification of those artifacts. The order is:

1. select composition and readiness evidence;
2. prepare the project's output/version/changelog/migration notes;
3. verify the final composition and every selected check;
4. commit the exact checked result if the project procedure requires it;
5. perform tag, push, publish, deploy, or notification only after separate explicit authorization.

When a changelog is part of the project contract, move only selected bullets into its versioned
section; never manufacture a release note from unrelated task bodies.

For a self-hosting payload, **Update `.tfw/VERSION` and `tfw.version` together** only when that
project-owned procedure selects the effect. Every user explicitly authorizes that effect separately;
otherwise the route stops with a prepared-result report.

For this self-hosting repository, that selected effect may **Update `.tfw/VERSION`**,
`.tfw/project_config.yaml`, `.tfw/templates/project_config.yaml`, `.tfw/CHANGELOG.md`,
`.tfw/templates/briefing.md`, `.tfw/adapters/manifest.yaml`, and the applicable
`.tfw/migrations/{major}.0.0.md`; these are examples of this project's contract, not receiver defaults.
All separate external effects remain separately authorized.
Use the project's own build/package/render checks. No common route requires Python, MkDocs, Git, SemVer,
`.tfw/VERSION`, `.tfw/CHANGELOG.md`, or a tag unless the project contract says so. Preserve the original
worktree and producer commits; if integration changes operational contents, verify the changed result.

## 4. Trace and safety boundary

Classify incidental sibling traces by semantic effect. A selected stable trace-only path may accompany an
authorized exact-path commit after inspection; it does not make a sibling task DONE or authorize editing
it. Operational, authority-bearing, private, verification-input, mixed-effect, or unreviewed deliverable
paths retain their own gates. Never publish a project result or expose credentials as evidence.
