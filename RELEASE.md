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
5. Git commit: `release: vX.Y.Z`
6. Git tag: `vX.Y.Z`
7. Push to GitHub

---

> Maintained by project owner. Referenced by `.tfw/workflows/release.md`.
