# RF — TFW-6 / Phase B: Workflows

> **Date**: 2026-03-12
> **Author**: Executor (AI)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-6](HL-TFW-6__versioning_and_update.md)
> **TS**: [TS Phase B](TS__PhaseB__workflows.md)

---

## 1. What Was Done

### New Files
| File | Description |
|------|-------------|
| `.tfw/workflows/release.md` | Canonical release workflow — 7 steps, references RELEASE.md for project context |
| `.tfw/workflows/update.md` | Canonical update workflow — 8 steps with 🟢🟡🔴 change categorization |
| `.agent/workflows/tfw-release.md` | Antigravity adapter — identical copy of release.md |
| `.agent/workflows/tfw-update.md` | Antigravity adapter — identical copy of update.md |

### Modified Files
| File | Changes |
|------|---------|
| `.tfw/conventions.md` | §2: added RELEASE.md as optional artifact. §8: "three" → "five" workflows, added release + update table rows |
| `.tfw/glossary.md` | Added 5 terms: VERSION, CHANGELOG.md, RELEASE.md, tfw-release, tfw-update |

## 2. Key Decisions

1. **Adapter copies via file copy.** Used `Copy-Item` to ensure byte-identical copies. Verified with `Compare-Object`.
2. **Glossary term placement.** Added new terms before the `Project-Specific Terms` separator, keeping them in the framework section.
3. **Conventions §8 count update.** Changed "three canonical workflows" to "five canonical workflows" to reflect the addition.

## 3. Acceptance Criteria

- [x] `.tfw/workflows/release.md` exists with YAML frontmatter and complete release process (7 steps)
- [x] `.tfw/workflows/update.md` exists with YAML frontmatter and complete update process with 🟢🟡🔴 categorization (8 steps)
- [x] `.agent/workflows/tfw-release.md` is identical to `.tfw/workflows/release.md` (verified via Compare-Object)
- [x] `.agent/workflows/tfw-update.md` is identical to `.tfw/workflows/update.md` (verified via Compare-Object)
- [x] `.tfw/conventions.md` §8 includes release + update in Workflows table
- [x] `.tfw/conventions.md` §2 includes RELEASE.md as optional artifact
- [x] `.tfw/glossary.md` has entries for VERSION, CHANGELOG.md, RELEASE.md, tfw-release, tfw-update
- [x] All cross-references in modified files are valid

## 4. Verification

- Lint: N/A (Markdown only)
- Tests: N/A
- Verify: Adapter identity confirmed via `Compare-Object`. Cross-references checked manually.

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.agent/workflows/` | — | todo | No adapter copies exist for Claude Code or Cursor tool adapters for the new release/update workflows. TS explicitly notes this as out of scope (→ future task). |
| 2 | `.tfw/conventions.md` | 133 | style | The `docs.md` workflow (added in TFW-5) is not listed in the §8 Workflows table — only plan, handoff, resume are present (now + release, update). This predates Phase B. |

---

*RF — TFW-6 / Phase B: Workflows | 2026-03-12*
