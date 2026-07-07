# TS — TFW-46 / Phase C: Glossary + Adapters + Version

> **Date**: 2026-07-07
> **Author**: Coordinator (Antigravity, Claude Opus 4.6)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-46](../HL-TFW-46__evidence_layer.md)

---

## 1. Objective
Finalize the Evidence Layer by updating the glossary with new terms, syncing adapter workflow copies (`.agent/workflows/` and `.claude/commands/`), bumping the version to 0.8.8, and writing the CHANGELOG entry. After this phase, TFW 0.8.8 is the canonical version with Evidence as a complete, documented concept.

## 2. Scope

### In Scope
- glossary.md — new Evidence terms + fix TD-2 stale ref (RF §7 → §8)
- Adapter copies: `.agent/workflows/tfw-{handoff,review,plan}.md` (synced from `.tfw/workflows/`)
- Adapter copies: `.claude/commands/tfw-{handoff,review,plan}.md` (synced from `.tfw/workflows/`)
- VERSION — 0.8.7 → 0.8.8
- CHANGELOG.md — entry for 0.8.8

### Out of Scope
- Cursor adapter (`.cursor/rules/tfw.mdc`) — template only, no workflow copies to sync
- Adapter template files (`.tfw/adapters/*/`) — templates reference `.tfw/`, no content duplication
- KNOWLEDGE.md updates — no architecture decisions emerged from Phase A/B that require documentation

## 3. Principles Check

| # | Principle (from HL §7) | Enforced by | Gate |
|---|----------------------|-------------|------|
| P4 | Domain-agnostic by default | AC-1 (glossary terms use no domain-specific examples) | Review glossary text |
| P2 | Honest incompleteness | AC-1 (DEFERRED/BLOCKED defined as terms) | Glossary entries |

> P1, P3, P5-P7 are enforced by Phase A (templates) and Phase B (workflows). Phase C is documentation and sync — no new behavioral enforcement.

## 4. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `.tfw/glossary.md` | MODIFY | New Evidence terms + fix stale RF §7 → §8 ref |
| `.agent/workflows/tfw-handoff.md` | MODIFY | Sync from `.tfw/workflows/handoff.md` (Phase A+B changes) |
| `.agent/workflows/tfw-review.md` | MODIFY | Sync from `.tfw/workflows/review.md` (Phase A+B changes) |
| `.agent/workflows/tfw-plan.md` | MODIFY | Sync from `.tfw/workflows/plan.md` (Phase B changes) |
| `.claude/commands/tfw-handoff.md` | MODIFY | Sync from `.tfw/workflows/handoff.md` |
| `.claude/commands/tfw-review.md` | MODIFY | Sync from `.tfw/workflows/review.md` |
| `.claude/commands/tfw-plan.md` | MODIFY | Sync from `.tfw/workflows/plan.md` |
| `.tfw/VERSION` | MODIFY | 0.8.7 → 0.8.8 |
| `.tfw/CHANGELOG.md` | MODIFY | Add [0.8.8] entry |

**Budget:** 0 new files, 9 modifications. Defaults: max 26 files, max 18 new, max 500 LOC.

## 5. Acceptance Criteria

### AC-1: Glossary updated with Evidence terms
Glossary.md has new entries for Evidence-related terms under a new "Evidence" heading or within existing sections, following the established glossary entry pattern.
- [ ] New terms defined: **Evidence** (concept), **Evidence Plan** (TS field), **Evidence Collection** (RF §5 / handoff Step 11), **Evidence Audit** (reviewer action in verify.md/judge.md)
- [ ] **Evidence status vocabulary** defined: VERIFIED, DEFERRED, BLOCKED, N/A — each with a one-line description
- [ ] Terms use no domain-specific examples — definitions are abstract/universal
- [ ] Cross-references to conventions.md §3 (Evidence Sections) where appropriate
- [ ] Fix TD-2: Strategic Insight entry updated from `RF §7` to `RF §8`

Gate: Read glossary.md — Evidence terms present, TD-2 fixed, no domain-specific examples
Evidence: N/A — glossary is a definition document

### AC-2: Adapter workflow copies synced
All adapter workflow copies match their canonical `.tfw/workflows/` sources after Phase A and Phase B modifications.
- [ ] `.agent/workflows/tfw-handoff.md` content matches `.tfw/workflows/handoff.md`
- [ ] `.agent/workflows/tfw-review.md` content matches `.tfw/workflows/review.md`
- [ ] `.agent/workflows/tfw-plan.md` content matches `.tfw/workflows/plan.md`
- [ ] `.claude/commands/tfw-handoff.md` content matches `.tfw/workflows/handoff.md`
- [ ] `.claude/commands/tfw-review.md` content matches `.tfw/workflows/review.md`
- [ ] `.claude/commands/tfw-plan.md` content matches `.tfw/workflows/plan.md`

Gate: `diff` canonical vs adapter copies — all 6 pairs identical
Evidence: N/A — mechanical copy operation

### AC-3: Version bump
VERSION file updated from 0.8.7 to 0.8.8.
- [ ] `.tfw/VERSION` contains `0.8.8`

Gate: Read VERSION file
Evidence: N/A — single-line change

### AC-4: CHANGELOG entry  [depends: AC-3]
CHANGELOG.md has a new [0.8.8] entry under [Unreleased] documenting all Evidence Layer changes from Phases A, B, and C. Entry follows Keep a Changelog format.
- [ ] Entry has correct version and date: `## [0.8.8] — 2026-07-07`
- [ ] Entry has Added, Changed sections documenting Evidence Layer changes
- [ ] Entry references TFW-46 and its phases (A, B, C)
- [ ] [Unreleased] section remains (empty or with any remaining unreleased items)

Gate: Read CHANGELOG.md — entry present, format correct, references TFW-46
Evidence: N/A — documentation

## 6. Technical Guidance

> Reference material, not instructions. Executor MAY deviate with justification in RF.

- **Glossary entry pattern**: See existing entries (e.g., Fact Candidate, Strategic Insight, Per-template Naming). Each has: term name as h3, 2-3 line definition, cross-reference to conventions.md. Evidence terms should follow the same density.
- **Evidence heading placement**: Consider a new `## Evidence Terms` section after `## Knowledge Terms` (line 42) — follows the same grouping pattern.
- **Adapter sync**: Previous tasks (TFW-42, TFW-43) used file copy. The canonical workflow files are the source of truth. Adapter copies are byte-identical copies.
- **CHANGELOG format**: See [0.8.7] entry as reference. Group by Added/Changed/Removed. Reference task IDs. One entry per logical change.
- **TD-2 location**: glossary.md line 48, Strategic Insight entry — `RF §7 "Strategic Insights (Execution)"` should be `RF §8`.

## 7. Definition of Failure

- ❌ Glossary terms use code-specific examples (screenshots, browser, curl)
- ❌ Adapter copies diverge from canonical sources after sync
- ❌ CHANGELOG entry is incomplete (misses Phase A or B changes)
- ❌ Version bump without CHANGELOG entry

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Adapter copies have local modifications not in canonical files | Check for differences before overwriting — if any exist, document in RF Observations |
| CHANGELOG entry too verbose | Follow existing density — [0.8.7] has ~10 lines for 3 subsections. Aim for similar |
| Glossary grows too large with Evidence terms | Keep definitions to 2-3 lines each, no examples — conventions.md has the details |

---

*TS — TFW-46 / Phase C: Glossary + Adapters + Version | 2026-07-07*
