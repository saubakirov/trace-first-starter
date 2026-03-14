# HL — TFW-10: Version String Sweep

> **Date**: 2026-03-14
> **Author**: Coordinator
> **Status**: 🔵 HL — Awaiting review

---

## 1. Vision

The project adopted semver (`0.4.x`) when `VERSION` was introduced in TFW-6 (2026-03-12). Before that, documentation used the informal label "TFW v3" to describe the current generation. When `VERSION` was introduced, the "TFW v3" strings were not cleaned up, leaving two conflicting version signals in the same codebase.

> *One project, one version scheme — all documentation must reference the semver version, not a stale generational label.*

## 2. Current State (As-Is)

**Versioning sources:**

| Source | Value | Authoritative? |
|--------|-------|----------------|
| `.tfw/VERSION` | `0.4.2` | ✅ Yes — machine-readable semver |
| `.tfw/PROJECT_CONFIG.yaml` → `tfw.version` | `0.4.2` | ✅ Yes |
| `.tfw/CHANGELOG.md` | semver entries | ✅ Yes |
| GitHub tags | `v0.4.0`, `v0.4.1`, `v0.4.2` | ✅ Yes |
| "TFW v3" strings (docs, adapters, headings) | `v3` | ❌ Stale — predates semver |

**"TFW v3" occurrences (14 total across 8 files):**

| File | Lines | Context |
|------|-------|---------|
| `.tfw/init.md` | 1, 194 | Document heading, adapter template example |
| `.tfw/conventions.md` | 1, 136 | Document heading, workflow description |
| `.tfw/glossary.md` | 1 | Document heading |
| `.tfw/README.md` | 148, 163, 205 | Prose sections |
| `.tfw/adapters/antigravity/tfw-rules.md.template` | 5 | Template heading |
| `.tfw/adapters/antigravity/README.md` | 34 | Comment in directory tree |
| `.tfw/adapters/claude-code/CLAUDE.md.template` | 16 | Section heading |
| `.tfw/adapters/cursor/tfw.mdc.template` | 2, 6 | Frontmatter + heading |

**Additionally:**
- `README.md` (root, line 1): `# Trace-First Workflow (TFW) v3 — Canonical Starter`
- `README.md` (root, line 75): `TFW v3 works with any development tool.`
- `README.md` (root, line 95): `**Current version**: v3 (2026)`
- `AGENTS.md` (line 4): `Follow TFW v3 to maintain traces…`

## 3. Target State (To-Be)

All "TFW v3" strings replaced with `TFW 0.4` (major.minor — stable within a generation's minor series, accurate, and self-updating via CHANGELOG). Generational history narrative in `.tfw/README.md` remains unchanged — "v3" appears only in the historical evolution section where it is accurate.

**Replacement rule:**
- `TFW v3` → `TFW 0.4` in headings, prose, adapter templates, and root files
- Exception: `.tfw/README.md` **Evolution** section (§ "v3 — Tool-Agnostic Core") — keep as historical narrative, it's factually correct there

**Why `TFW 0.4` and not `TFW 0.4.2`?**
Patch is irrelevant to document headings and adapter titles; it changes every release. Major.minor (`0.4`) identifies the stable generation within which patch updates are backwards-compatible.

**After sweep:**

| File | Before | After |
|------|--------|-------|
| `.tfw/init.md` h1 | `# TFW v3 — Quick Start` | `# TFW 0.4 — Quick Start` |
| `.tfw/conventions.md` h1 | `# TFW v3 — Conventions` | `# TFW 0.4 — Conventions` |
| `.tfw/glossary.md` h1 | `# TFW v3 Glossary` | `# TFW 0.4 Glossary` |
| adapter templates (3 files) | `# TFW v3` / description | `# TFW 0.4` / updated |
| `README.md` root h1 | `TFW (TFW) v3 — Canonical Starter` | `TFW — Canonical Starter (0.4)` |
| `AGENTS.md` | `Follow TFW v3…` | `Follow TFW 0.4…` |

## 4. Phases

### Phase A: Version String Sweep 🔴

Single phase — file edits only, no logic changes.

- Replace all stale `TFW v3` strings per the table in §3
- Preserve Evolution section in `.tfw/README.md`
- Deliver as a git branch + PR

## 5. Definition of Done (DoD)

- ✅ 1. `grep -r "TFW v3" .` returns zero results outside `.tfw/README.md` Evolution section
- ✅ 2. All 8 `.tfw/` files and root files updated per §3 table
- ✅ 3. Changes are on a dedicated git branch (`fix/version-string-sweep`)
- ✅ 4. PR opened against `master` with descriptive title and body summarising the change
- ✅ 5. No functional changes — only version label text replaced

## 6. Definition of Failure (DoF)

- ❌ 1. Any occurrence of `TFW v3` outside the allowed Evolution section after the sweep
- ❌ 2. Accidental edit to Evolution section that removes historical context
- ❌ 3. Functional content (workflow steps, rules) inadvertently altered

**On failure:** revert branch, rerun grep audit, fix only the failing items.

## 7. Principles

1. **Minimal diff** — change only the version label strings; touch nothing else in each file
2. **Semver as single source** — `VERSION` file is authoritative; all docs follow it
3. **Preserve history** — the Evolution narrative in `.tfw/README.md` is intentional and factually correct; do not alter it

## 8. Dependencies

| Dependency | Status |
|------------|--------|
| `VERSION` file exists and is authoritative | ✅ Done (TFW-6) |
| No in-flight PRs touching the same files | ✅ Confirmed |

## 9. Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Grep misses an occurrence | Low | Low | Run `grep -rn "TFW v3" .` after sweep to verify |
| Evolution section mistakenly edited | Low | Medium | Explicitly list it as out-of-scope in TS |

---

*HL — TFW-10: Version String Sweep | 2026-03-14*
