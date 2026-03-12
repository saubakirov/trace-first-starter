# HL — TFW-6: Versioning, Changelog, and tfw-update Workflow

> **Date**: 2026-03-12
> **Author**: Coordinator (AI)
> **Status**: 🔵 HL — Awaiting review (v2 — post-discussion)

---

## 1. Vision

TFW is a living framework. The starter repo (`trace-first-starter`) evolves — new templates, new workflows, convention changes, bug fixes. But downstream projects that forked or copied `.tfw/` have **no mechanism** to know what changed, what version they're on, or how to safely update.

This task introduces:
- **Semantic versioning** for the TFW framework itself.
- **A CHANGELOG** that documents every release.
- **A `tfw-update` workflow** — a structured process for downstream projects to compare their `.tfw/` against upstream and apply updates safely.
- **A `tfw-release` workflow** — a canonical process for cutting framework versions (general rules applicable to any project that versions its outputs).
- **A `RELEASE.md` artifact** — optional, project-specific release context (like `KNOWLEDGE.md`). Template provides guided questions; each project fills it with its own release strategy.

> *"If you can't tell what version you're running, you can't tell what's missing."*

## 2. Current State (As-Is)

| Aspect | Status |
|--------|--------|
| Version tracking | ❌ None — `.tfw/README.md` mentions "v3" in prose, no machine-readable version |
| Changelog | ❌ None — evolution history is narrative in `.tfw/README.md` §Evolution |
| Update mechanism | ❌ None — manual diff of entire `.tfw/` directory |
| Release process | ❌ None — no workflow for cutting versions |
| Release context | ❌ None — no project-level release strategy document |
| Downstream awareness | ❌ — forked projects have no way to know upstream changed |
| Adapter sync | ❌ — `.agent/workflows/` are copies of `.tfw/workflows/`, no version check |

### Files Involved (current)
| File | Role | Relevant? |
|------|------|-----------|
| `.tfw/README.md` | Philosophy + evolution narrative (v1→v2→v3) | Version info buried in prose |
| `.tfw/PROJECT_CONFIG.yaml` | Per-project config | No version field |
| `.tfw/conventions.md` | Rules, required artifacts | No RELEASE.md entry |
| `.tfw/init.md` | Setup guide | Describes copying `.tfw/`, no update/release guidance |
| `.agent/workflows/` | Antigravity adapter copies | Copies of `.tfw/workflows/` — can drift |

## 3. Target State (To-Be)

| Aspect | Target |
|--------|--------|
| Version tracking | `VERSION` file in `.tfw/` with semver (`MAJOR.MINOR.PATCH`) |
| Changelog | `CHANGELOG.md` in `.tfw/` — structured, per-version, with categories |
| Project version tracking | `tfw_version` field in `.tfw/PROJECT_CONFIG.yaml` records installed version |
| Update workflow | `.tfw/workflows/update.md` — step-by-step upgrade process for downstream projects |
| Release workflow | `.tfw/workflows/release.md` — canonical release process (general, any project) |
| Release context | `RELEASE.md` (root, optional) — project-specific release strategy. Template in `.tfw/templates/RELEASE.md` |
| Adapter workflows | `.agent/workflows/tfw-update.md` + `.agent/workflows/tfw-release.md` |
| Docs integration | `init.md` mentions versioning + RELEASE.md; KNOWLEDGE.md updated |

### Version Scheme

```
MAJOR.MINOR.PATCH
```

- **MAJOR** — breaking changes to conventions, templates, or workflow structure (requires manual migration)
- **MINOR** — new workflows, new templates, new optional features (backward-compatible)
- **PATCH** — fixes, clarifications, typos in existing files

### CHANGELOG Format

```markdown
# TFW Changelog

## [0.3.1] — 2026-03-12
### Added
- `CHANGELOG.md` — version history
- `VERSION` file — machine-readable version
- `tfw-release` workflow — canonical release process
- `tfw-update` workflow — structured upgrade process
- `RELEASE.md` template — optional release context artifact
### Changed
- `PROJECT_CONFIG.yaml` — added `tfw_version` field
- `init.md` — added version tracking and release guidance
```

Categories: `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`.

### RELEASE.md Design

**Template** (`.tfw/templates/RELEASE.md`) — a scaffold with guiding questions:
- What does a "release" mean for this project?
- Who consumes the releases?
- What triggers a release?
- What version scheme does the project use?
- Pre-release checklist items

**This project's instance** — fully populated with TFW framework release context:
- Audience: downstream TFW projects
- Trigger: accumulated `.tfw/` changes ready to ship
- Scheme: semver
- Checklist: Task Board scan → version bump → CHANGELOG → git tag

### tfw-release Workflow (canonical, general)

Lives in `.tfw/workflows/release.md`. General steps applicable to any project:

1. Read `RELEASE.md` for project-specific context
2. Review what changed since last release (Task Board, git log, RF files)
3. Decide version bump type (consulting `RELEASE.md` strategy)
4. Update changelog
5. Update version marker
6. Tag/commit

### tfw-update Workflow (canonical, for downstream consumers)

Lives in `.tfw/workflows/update.md`. For projects consuming TFW:

1. Read current version from `PROJECT_CONFIG.yaml` → `tfw_version`
2. Read target version from upstream `.tfw/VERSION`
3. Show CHANGELOG diff — all entries between current and target
4. Categorize changes:
   - 🟢 **Auto-apply** — new files, new workflows (no project customization risk)
   - 🟡 **Manual merge** — changed templates, conventions (project may have customized)
   - 🔴 **Breaking** — removed/renamed files, structural changes
5. Generate update checklist — concrete file-by-file actions
6. Update `tfw_version` in `PROJECT_CONFIG.yaml` after completion
7. Re-sync adapter copies (`.agent/workflows/` etc.) from `.tfw/workflows/`

## 4. Phases

### Phase A: Core Versioning Infrastructure 🔴

- Create `.tfw/VERSION` file with initial version `0.3.0`
- Create `.tfw/CHANGELOG.md` with retroactive entries for v1, v2, v3
- Add `tfw_version` field to `.tfw/PROJECT_CONFIG.yaml`
- Create `.tfw/templates/RELEASE.md` — scaffold template with guiding questions
- Create `RELEASE.md` (root) — fully populated for this project
- Update `.tfw/init.md` — sections on version tracking + RELEASE.md mention

### Phase B: Workflows 🔴

- Create `.tfw/workflows/release.md` — canonical release workflow
- Create `.tfw/workflows/update.md` — canonical update workflow
- Create `.agent/workflows/tfw-release.md` — Antigravity adapter
- Create `.agent/workflows/tfw-update.md` — Antigravity adapter
- Update `.tfw/conventions.md` §8 Workflows table — add release + update entries
- Update `.tfw/conventions.md` §2 Required Artifacts — mention RELEASE.md as optional
- Update `.tfw/glossary.md` — version-related terms + RELEASE.md entry

### Phase C: Documentation & Traces 🟡

- Update `KNOWLEDGE.md` — new D-records (version scheme, release/update workflows, RELEASE.md design)
- Update `.tfw/README.md` §Canonical Workflows — mention release + update
- Update root `README.md` — mention versioning in "What's Inside"

## 5. Definition of Done (DoD)

- ✅ 1. `.tfw/VERSION` exists with valid semver
- ✅ 2. `.tfw/CHANGELOG.md` exists with retroactive history and current release
- ✅ 3. `PROJECT_CONFIG.yaml` has `tfw_version` field
- ✅ 4. `.tfw/templates/RELEASE.md` exists with guiding scaffold
- ✅ 5. `RELEASE.md` (root) populated for this project
- ✅ 6. `.tfw/workflows/release.md` exists with general release process
- ✅ 7. `.tfw/workflows/update.md` exists with complete update process
- ✅ 8. `.agent/workflows/tfw-release.md` + `.agent/workflows/tfw-update.md` exist
- ✅ 9. `init.md` documents version tracking and RELEASE.md during setup
- ✅ 10. `KNOWLEDGE.md` updated with version-related decisions
- ✅ 11. All existing files pass consistency check (no broken cross-references)

## 6. Definition of Failure (DoF)

- ❌ 1. Version scheme is too complex — more than 3 numbers or requires tooling to parse
- ❌ 2. CHANGELOG becomes bureaucratic overhead — entries take more than 2 minutes to write
- ❌ 3. Workflows require scripting/tooling — must be pure Markdown instructions
- ❌ 4. RELEASE.md template confuses users about whether they need it — must clearly state "optional"

**On failure:** Simplify. Version can be a single number. CHANGELOG can be a flat list. RELEASE.md scaffold can be 5 lines.

## 7. Principles

1. **Plain text, no tooling** — VERSION is a text file, CHANGELOG is Markdown. No scripts needed to read or compare.
2. **Retroactive completeness** — CHANGELOG covers v1, v2, v3 history so the record is complete from day one.
3. **Downstream safety** — tfw-update MUST distinguish between files safe to overwrite and files the project has customized. Never silently destroy project-specific changes.
4. **Optional over mandatory** — RELEASE.md is optional (like KNOWLEDGE.md). Projects that don't do releases skip it. No overhead.
5. **General over specific** — tfw-release workflow contains general release steps. Project-specific context lives in RELEASE.md, not in the workflow.
6. **Adapter parity** — every canonical workflow in `.tfw/workflows/` gets a corresponding adapter copy.

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| TFW-4 (framework cleanup) | 🟡 TS — in progress but not blocking |
| TFW-5 (KNOWLEDGE + tfw-docs) | ✅ DONE |

## 9. Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Retroactive CHANGELOG inaccurate | Medium | Low | Cross-check with `.tfw/README.md` §Evolution and task RFs |
| Projects forget to update `tfw_version` | Medium | Medium | tfw-update workflow includes version bump as final step |
| RELEASE.md template too vague | Medium | Low | Populate this project's RELEASE.md as a real example; link from template |
| Breaking changes hard to communicate | Low | High | CHANGELOG uses clear `### Breaking` section; tfw-update flags 🔴 items |

---

*HL — TFW-6: Versioning, Changelog, and tfw-update Workflow | 2026-03-12 (v2)*
