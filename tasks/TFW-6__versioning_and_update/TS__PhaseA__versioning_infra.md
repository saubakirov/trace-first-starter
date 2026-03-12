# TS — TFW-6 / Phase A: Core Versioning Infrastructure

> **Date**: 2026-03-12
> **Author**: Coordinator (AI)
> **Status**: 🟡 TS — Awaiting approval
> **Parent HL**: [HL-TFW-6](HL-TFW-6__versioning_and_update.md)

---

## 1. Goal

Establish the version tracking foundation: a `VERSION` file, a retroactive `CHANGELOG.md`, version field in `PROJECT_CONFIG.yaml`, a `RELEASE.md` template, this project's populated `RELEASE.md`, and `init.md` updates. After this phase, TFW has a clear version identity and every new project knows to track its TFW version.

## 2. Scope

### In Scope
- Create `.tfw/VERSION` with initial version `0.3.0`
- Create `.tfw/CHANGELOG.md` with retroactive history (v1, v2, v3) and current release entry
- Add `tfw_version` field to `.tfw/PROJECT_CONFIG.yaml`
- Create `.tfw/templates/RELEASE.md` — guiding scaffold for release strategy
- Create `RELEASE.md` (root) — fully populated instance for this project (trace-first-starter)
- Update `.tfw/init.md` — add version tracking section + mention RELEASE.md

### Out of Scope
- Workflows (tfw-release, tfw-update) → Phase B
- Documentation updates (KNOWLEDGE.md, README files) → Phase C
- Adapter workflow copies → Phase B

## 3. Files

| File | Action | Description |
|------|--------|-------------|
| `.tfw/VERSION` | CREATE | Single-line semver: `0.3.0` |
| `.tfw/CHANGELOG.md` | CREATE | Retroactive changelog: v1 (2024), v2 (2025), v3 (2026), + 0.3.1 release entry |
| `.tfw/PROJECT_CONFIG.yaml` | MODIFY | Add `tfw_version: "0.3.0"` under `tfw:` section |
| `.tfw/templates/RELEASE.md` | CREATE | Scaffold with guiding questions for project release strategy |
| `RELEASE.md` | CREATE | This project's release context: audience, triggers, scheme, checklist |
| `.tfw/init.md` | MODIFY | Add §Version Tracking + mention RELEASE.md in Step 4 and Verification |

**Budget:** 4 new files, 2 modifications. ≤7 files ✅, ≤4 new ✅, ≤600 LOC ✅.

## 4. Detailed Steps

### Step 1: Create `.tfw/VERSION`

Single line, no newline at end:
```
0.3.0
```

Rationale for `0.3.0`: matches the "v3" designation used in `.tfw/README.md`. Major=0 because TFW hasn't had a formal "1.0" release.

### Step 2: Create `.tfw/CHANGELOG.md`

Structure:
```markdown
# TFW Changelog

All notable changes to the Trace-First Workflow framework.
Format: [Keep a Changelog](https://keepachangelog.com/). Versioning: [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.3.1] — 2026-03-12
### Added
- `VERSION` file — machine-readable framework version
- `CHANGELOG.md` — version history (this file)
- `RELEASE.md` template — optional release context artifact
- `tfw-release` workflow — canonical release process
- `tfw-update` workflow — structured upgrade process for downstream projects
### Changed
- `PROJECT_CONFIG.yaml` — added `tfw_version` field
- `init.md` — added version tracking and RELEASE.md guidance

## [0.3.0] — 2026-03-02
### Added
- `KNOWLEDGE.md` template and tfw-docs workflow (TFW-5)
### Changed
- Framework cleanup: removed STEPS.md, TASK.md, Summary Discipline (TFW-4)
- Root README restructured for public readership (TFW-3)

## [0.2.0] — 2026-02-25
### Added
- `.tfw/` directory — tool-agnostic core (conventions, templates, workflows, adapters)
- ONB and REVIEW artifact types
- 7-status lifecycle with quality gates
- 3 canonical workflows (plan, handoff, resume)
- Scope budgets per phase
- TECH_DEBT.md pipeline
- Tool adapter pattern (Claude Code, Cursor, Antigravity)
- PROJECT_CONFIG.yaml
- Anti-patterns list
### Removed
- `AI_ENTRY_POINT.md`, `SUCCESS_CRITERIA.md`, `00_meta/` directory

## [0.1.0] — 2024
### Added
- Core concept: traces are more valuable than code
- 4-file structure (AGENTS, README, TASK, STEPS)
- Summary Discipline
- Chat→project conversion pattern
- CL/AG execution modes (informal)
```

Cross-reference: `.tfw/README.md` §Evolution for accuracy.

### Step 3: Add `tfw_version` to `PROJECT_CONFIG.yaml`

Add under the `tfw:` section:
```yaml
tfw:
  version: "0.3.0"         # Installed TFW version (update via tfw-update)
  task_prefix: PROJ
  ...
```

Field name: `version` (not `tfw_version` — it's already under the `tfw:` namespace).

### Step 4: Create `.tfw/templates/RELEASE.md`

Scaffold with guiding questions:
```markdown
# RELEASE.md — {Project Name}

> Release strategy and context for this project.
> Optional artifact — create only if your project has releases, publications, or versioned outputs.

---

## 1. What Is a Release?

> What does "release" mean for this project? Examples:
> - A version bump of a framework or library
> - A deployed application build
> - A published report or document
> - A data pipeline promotion to production

{Describe what constitutes a release for your project}

## 2. Audience

> Who consumes your releases?
> - Downstream projects / developers
> - End users / clients
> - Internal teams
> - The public (open source)

{Describe your audience}

## 3. Version Scheme

> How do you track versions?
> - Semantic versioning (MAJOR.MINOR.PATCH)
> - Calendar versioning (YYYY.MM)
> - Sequential (v1, v2, v3)
> - None (single living document)

{Describe your versioning approach, or "N/A" if not applicable}

## 4. Release Triggers

> When should a release happen?
> - After N tasks complete
> - On a fixed schedule
> - When a milestone is reached
> - Ad-hoc, when the maintainer decides

{Describe what triggers a release}

## 5. Pre-Release Checklist

> What must be true before cutting a release?
> Customize this list for your project.

- [ ] All in-scope tasks are ✅ DONE
- [ ] Task Board is current
- [ ] TECH_DEBT.md reviewed — no critical items blocking release
- [ ] KNOWLEDGE.md updated (if applicable)
- [ ] {Add project-specific checks}

## 6. Release Steps

> Project-specific release actions (beyond what `tfw-release` workflow covers).
> Examples: deploy, publish, notify, tag, build artifacts.

{Describe your release steps, or leave for later}

---

> Maintained by the project owner. Referenced by `.tfw/workflows/release.md`.
```

### Step 5: Create `RELEASE.md` (root) for this project

Fully populated:
```markdown
# RELEASE.md — Trace-First Starter

> Release strategy for the TFW framework canonical starter repository.

---

## 1. What Is a Release?

A release is a versioned snapshot of the `.tfw/` directory (conventions, templates, workflows, adapters, config) that downstream projects can reference and update to.

Each release bundles accumulated changes from one or more TFW tasks into a coherent version that consumers can safely adopt.

## 2. Audience

- **Downstream TFW projects** — any project that copied `.tfw/` from this starter
- **Framework contributors** — people proposing changes to TFW itself
- **New users** — people discovering TFW and judging its maturity

## 3. Version Scheme

Semantic versioning: `MAJOR.MINOR.PATCH`

| Bump | When | Examples |
|------|------|----------|
| MAJOR | Breaking changes to conventions, templates, or workflow structure | Template field renamed, status flow changed, required file removed |
| MINOR | New workflows, templates, optional features (backward-compatible) | New workflow added, new template, new optional artifact |
| PATCH | Fixes, clarifications, typos | Typo in template, wording fix in conventions |

Version is tracked in `.tfw/VERSION` (machine-readable) and `.tfw/CHANGELOG.md` (human-readable).

## 4. Release Triggers

Ad-hoc, when the maintainer decides accumulated changes justify a new version. Guidelines:

- **Always release after** completing a task that adds/changes workflows, templates, or conventions
- **Consider release after** documentation-only tasks if they affect downstream behavior
- **Skip release for** internal-only changes (task board updates, this project's RF files)

## 5. Pre-Release Checklist

- [ ] All in-scope tasks are ✅ DONE or explicitly excluded
- [ ] Task Board is current
- [ ] TECH_DEBT.md reviewed — no critical items blocking release
- [ ] KNOWLEDGE.md updated via tfw-docs
- [ ] CHANGELOG.md entry written for this version
- [ ] VERSION file updated
- [ ] `init.md` still accurate for the new version
- [ ] Adapter templates consistent with current workflows

## 6. Release Steps

1. Review Task Board — identify all tasks completed since last version
2. Decide version bump type (MAJOR / MINOR / PATCH)
3. Write CHANGELOG.md entry
4. Update `.tfw/VERSION`
5. Update `tfw.version` in `.tfw/PROJECT_CONFIG.yaml`
6. Git commit: `release: vX.Y.Z`
7. Git tag: `vX.Y.Z`
8. Push to GitHub

---

> Maintained by project owner. Referenced by `.tfw/workflows/release.md`.
```

### Step 6: Update `.tfw/init.md`

Add version tracking mention in two places:

**A) New section after Step 2 (Configure):**

```markdown
## Step 2.5: Record TFW Version

Your `.tfw/PROJECT_CONFIG.yaml` includes a `tfw.version` field. It was set when you copied `.tfw/`.
This field is used by the `tfw-update` workflow to detect which version of TFW your project is running.

> ⚠️ Do not manually change `tfw.version` — it is updated by the `tfw-update` workflow.
```

**B) In Step 4 (Create Root Files), add RELEASE.md mention:**

```markdown
# RELEASE.md (optional) — if your project has versioned releases
cp .tfw/templates/RELEASE.md RELEASE.md
# Edit RELEASE.md: answer the guiding questions for your project's release strategy
```

**C) In Verification checklist, add:**

```markdown
- [ ] `tfw.version` in `PROJECT_CONFIG.yaml` matches `.tfw/VERSION`
- [ ] `RELEASE.md` exists (if project has releases) or consciously skipped
```

## 5. Acceptance Criteria

- [ ] `.tfw/VERSION` contains `0.3.0` (single line, valid semver)
- [ ] `.tfw/CHANGELOG.md` has entries for 0.1.0, 0.2.0, 0.3.0, 0.3.1 with accurate content
- [ ] `.tfw/PROJECT_CONFIG.yaml` has `version: "0.3.0"` under `tfw:` section
- [ ] `.tfw/templates/RELEASE.md` has guiding scaffold with 6 sections
- [ ] `RELEASE.md` (root) is fully populated for trace-first-starter
- [ ] `.tfw/init.md` mentions version tracking and RELEASE.md
- [ ] No broken cross-references in modified files

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| Retroactive CHANGELOG entries inaccurate | Cross-check against `.tfw/README.md` §Evolution and task RF files |
| `tfw.version` field name conflicts with YAML conventions | Use simple string field, no complex types |

---

*TS — TFW-6 / Phase A: Core Versioning Infrastructure | 2026-03-12*
