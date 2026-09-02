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
- **Skip release for** internal-only changes (task state transitions, this project's RF files)

## 5. Pre-Release Checklist

- [ ] All in-scope tasks are ✅ DONE or explicitly excluded
- [ ] every task closed in this release carries `lifecycle: DONE` and a filled `outcome` in its own `status.md`
- [ ] KNOWLEDGE.md updated via tfw-docs
- [ ] CHANGELOG.md entry written for this version
- [ ] **every quantitative claim in the entry is re-measured at the tag, and each carries the command that
      produces it.** A figure that was true when it was written drifts before it ships, and a released
      entry is never rewritten in substance — so a wrong number is wrong permanently. This row exists
      because 2.1.0 was found carrying **three**: a word count, an artifact count and a row count, each
      written by a task the release closes, each false by the time the tag was cut, and one of them
      standing in a bullet that argued against maintaining figures. Prefer **removing** a figure the claim
      does not need to correcting one it does
- [ ] the entry's **updating section reaches every earlier tag still in use**: it opens with *read the target's `.tfw/workflows/update.md`, not the installed one*, and names or points to every intervening entry's updating section (*"if you are on `.2`, also perform the `.3` section"* is sufficient). A receiver skips tags; the entries must not assume it did not
- [ ] where the release **reverses a normative statement**, the entry quotes the retired wording **verbatim** as a search string and says what a project that already acted on it does. Receivers copy framework principles into their own rule files, and the quoted string is the only thing `grep` finds
- [ ] an instruction a later release replaces keeps its text and gains a `> **Superseded by** {path} (date)` line above it. A CHANGELOG entry is never rewritten in substance: additions are appended to the entry they concern, dated
- [ ] VERSION file updated
- [ ] `init.md` still accurate for the new version
- [ ] Adapter templates consistent with current workflows

## 6. Release Steps

1. Review task state across the configured containers — identify all tasks closed since the last version
2. Decide version bump type (MAJOR / MINOR / PATCH)
3. Write CHANGELOG.md entry — with its updating section written for a receiver on **any** earlier tag of the line (see §5), the retired wordings quoted, and `> **Superseded by**` lines on anything it replaces
4. Update `.tfw/VERSION`
5. Git commit using Commit Attribution, for example: `[codex/project/release/coordinator] release vX.Y.Z`
6. Git tag: `vX.Y.Z`
7. After explicit user approval, push the commit and tag to GitHub

---

> Maintained by project owner. Referenced by `.tfw/workflows/release.md`.
