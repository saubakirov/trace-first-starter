# RF — TFW_20260921-220500_AGSK / Phase B: Migration Guide and Documentation Sync

> **Current filename**: `RF__phase-b__migration_guide_and_documentation_sync.md`

> **Date**: 2026-09-22
> **Author**: Executor
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW_20260921-220500_AGSK](../HL-TFW_20260921-220500_AGSK.md)
> **TS**: [TS Phase B](TS__phase-b__migration_guide_and_documentation_sync.md)
> **Producer unit**: antigravity:thread:local:ec458eac-9120-412b-ae03-78f365c5484d
> **Parent Coordinator**: antigravity:thread:local:8888199a-c102-44c8-b661-f9c6bef8d7a6
> **Activation / dispatch source**: owner-direct (`/tfw-handoff agsk phase-b`)
> **Coordination authority**: "../HL-TFW_20260921-220500_AGSK.md"
> **Originating proposer**: none

---

## 1. What Was Done

Created the normative migration guide `.tfw/migrations/3.5.0.md` for downstream projects, updated the `KNOWLEDGE.md` Adapters row, the `.tfw/glossary.md` Tool Adapter definition, all three README localizations' adapter tables, added the `[3.5.0]` CHANGELOG entry, added explicit coordination messaging instructions to the Antigravity rule/template (byte-identical), and documented the messaging mechanics in the adapter README.

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | `637df43` (ONB commit containing approved TS; TS approved by owner-direct `/tfw-handoff` invocation) |
| Baseline / Candidate | `a26322e2a9899936c0cdb1a1d523960b80f6aec9` / `bde7334ff626e8c2c43f315717f90271182b4ab3` |
| VALUE membership | `.tfw/migrations/3.5.0.md` (A, VALUE, migration guide); `KNOWLEDGE.md` (M, VALUE, Adapters row); `.tfw/glossary.md` (M, VALUE, Tool Adapter definition); `README.md` (M, VALUE, adapter table); `README.ru.md` (M, VALUE, adapter table); `README.kk.md` (M, VALUE, adapter table); `.tfw/CHANGELOG.md` (M, VALUE, 3.5.0 release entry); `.agents/rules/tfw.md` (M, VALUE, coordination messaging); `.tfw/adapters/antigravity/tfw-rules.md.template` (M, VALUE, template sync); `.tfw/adapters/antigravity/README.md` (M, VALUE, messaging documentation) |
| Arithmetic | 174 + 5 = 179 touched text LOC; 10 logical files; binary N/A: 0 |
| Membership deviations | None — exact match to TS §4 denominator of 10 files |
| Trigger disposition | N/A — 179 LOC is well below 5000 trigger; 10 files is well below 50 trigger |
| Authority and timing | Immutable denominator: 10 literal paths from TS §4, approved before work by owner-direct `/tfw-handoff`; multiplier 2 ceiling not reached |
| Reproduction | `git diff --numstat --find-renames=50% a26322e2a9899936c0cdb1a1d523960b80f6aec9 bde7334ff626e8c2c43f315717f90271182b4ab3 -- $valuePaths` |

### New Files

| File | Description |
|---|---|
| `.tfw/migrations/3.5.0.md` | Normative migration guide for downstream projects: route table (§1), workflow retirement procedure (§2), `.agent/` classification and retirement algorithm (§3), verification checklist (§4) |

### Modified Files

| File | Changes |
|---|---|
| `KNOWLEDGE.md` | Adapters row: 11→10 routes, `.agent/workflows/`→`.agents/skills/`, "compatibility only"→"fully retired" |
| `.tfw/glossary.md` | Tool Adapter: `.agents/workflows/tfw-{command}.md`→`.agents/skills/tfw-{command}/SKILL.md` |
| `README.md` | Antigravity entry point: `.agent/rules/tfw.md`→`.agents/rules/tfw.md` plus `.agents/skills/tfw-*/SKILL.md` |
| `README.ru.md` | Same Antigravity entry point update (Russian localization) |
| `README.kk.md` | Same Antigravity entry point update (Kazakh localization) |
| `.tfw/CHANGELOG.md` | Added `## [3.5.0] — 2026-09-22` with AGSK codename, Changed/Removed/Compatibility subsections |
| `.agents/rules/tfw.md` | Added `### Coordination Messaging` section with `send_message` instructions for all TFW roles |
| `.tfw/adapters/antigravity/tfw-rules.md.template` | Synchronized with `.agents/rules/tfw.md` (byte-identical) |
| `.tfw/adapters/antigravity/README.md` | Added `## Coordination Messaging` section documenting cross-session addressed messaging |

## 2. Key Decisions

1. Used `2026-09-22` as the CHANGELOG date for `[3.5.0]`, consistent with implementation date. The physical `.tfw/VERSION` bump occurs during `/tfw-release` and is out of scope per TS §2.
2. Migration guide follows the four-section structure of `3.4.0.md` and `3.4.1.md` precedents rather than inventing a new format.
3. The Coordination Messaging section in `.agents/rules/tfw.md` is placed after the Commands/Roles table and before the Rules heading, creating a natural reading flow from command identification → messaging mechanics → behavioral rules.

## 3. Acceptance Criteria

- [x] AC-1: `.tfw/migrations/3.5.0.md` created with all mandatory sections (route table, workflow retirement, `.agent/` classification, verification).
- [x] AC-2: `KNOWLEDGE.md` Adapters row updated to 10 routes with `.agents/skills/`; no `.agent/workflows/` substring remains.
- [x] AC-3: `.tfw/glossary.md` Tool Adapter definition updated to `.agents/skills/tfw-{command}/SKILL.md`.
- [x] AC-4: All three `README*.md` adapter tables updated; `git grep ".agent/rules/tfw.md" -- README*.md` returns zero matches.
- [x] AC-5: `.tfw/CHANGELOG.md` entry `[3.5.0]` added with AGSK codename and Changed/Removed/Compatibility subsections.
- [x] AC-6: `python -m pytest tools/tests/ docs/scripts/ -q` → 14 passed, exit code 0.
- [x] AC-7: Coordination Messaging added to both `.agents/rules/tfw.md` and template (byte-identical); adapter README documents the mechanics.

## 4. Verification

- Lint (`python -m pytest tools/tests/ docs/scripts/ -q --collect-only`): 14 tests collected
- Tests (`python -m pytest tools/tests/ docs/scripts/ -q`): 14 passed in 3.91s, exit code 0

## 5. Evidence

See [EV file](evidence/EV__phase-b__migration_guide_and_documentation_sync.md) for evidence details.

Evidence verdict: 8/8 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|---|---|---|---|
| 1 | `KNOWLEDGE.md` | L29 | stale-reference | Workflows row still lists `resume` among workflows (`init, plan, research/, handoff, review, resume, docs, release, update, knowledge, config`). Resume was retired in 3.4.1. Not in TS scope (not in VALUE denominator) |

## 7. Fact Candidates

No fact candidates.

## 8. Strategic Insights (Execution)

No strategic insights.

## 9. Diagrams

No diagrams.

### Material handover at this return

- **Producer unit:** Executor at `antigravity:thread:local:ec458eac-9120-412b-ae03-78f365c5484d`.
- **Source/epoch:** TS approval by owner-direct `/tfw-handoff` at 2026-09-22T10:57+05:00. Baseline `a26322e` (Phase A RF). Candidate `bde7334` (Phase B Implementation).
- **Inspected scope:** All 10 VALUE paths. Stale-path sweep across VALUE set. 14/14 pytest. Byte-equality verification between rule and template.
- **Material findings:** All 7 acceptance criteria met. One out-of-scope observation: `KNOWLEDGE.md` Workflows row contains stale `resume` reference from 3.4.1 era.
- **Uncertainty:** None within Phase B scope.
- **Continuation:** Return to Coordinator for `/tfw-review`.

---

*RF — TFW_20260921-220500_AGSK / Phase B: Migration Guide and Documentation Sync | 2026-09-22*
