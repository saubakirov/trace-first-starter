# EV — TFW_20260921-220500_AGSK / Phase B: Migration Guide and Documentation Sync

> **Current filename**: `evidence/EV__phase-b__migration_guide_and_documentation_sync.md`

> **Date**: 2026-09-22
> **Author**: Executor
> **Task**: TFW_20260921-220500_AGSK
> **TS**: [TS Phase B](../TS__phase-b__migration_guide_and_documentation_sync.md)

---

## Environment

| Field | Value |
|---|---|
| OS | Windows 10/11 |
| Language / Runtime | Python 3.x (pytest) |
| Database | N/A |
| Deploy target | N/A |
| CI / Pipeline | local |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1 | AC-1 | `.tfw/migrations/3.5.0.md` created with route table (§1), workflow retirement procedure (§2), `.agent/` classification algorithm (§3), and verification checklist (§4); follows `3.4.0.md`/`3.4.1.md` structural precedents | local filesystem | VERIFIED | `.tfw/migrations/3.5.0.md` (100 lines, 4 sections) |
| E2 | AC-2 | `KNOWLEDGE.md` Adapters row updated: "10 routes", ".agents/skills/" surface, ".agent is fully retired"; ripgrep for `.agent/workflows/` returns zero matches | local filesystem + git grep | VERIFIED | `git grep -n ".agent/workflows/" -- KNOWLEDGE.md` → exit 1 (no matches) |
| E3 | AC-3 | `.tfw/glossary.md` Tool Adapter definition updated: `.agents/workflows/tfw-{command}.md` → `.agents/skills/tfw-{command}/SKILL.md`; ripgrep confirms no `.agents/workflows` remains | local filesystem + grep | VERIFIED | `.tfw/glossary.md` L379 |
| E4 | AC-4 | README.md L192, README.ru.md L190, README.kk.md L191 updated: `.agent/rules/tfw.md` → `.agents/rules/tfw.md` plus `.agents/skills/tfw-*/SKILL.md`; `git grep -n ".agent/rules/tfw.md" -- README*.md` → exit 1 (no matches) | local filesystem + git grep | VERIFIED | `evidence/doc-sweep.txt` |
| E5 | AC-5 | `.tfw/CHANGELOG.md` entry `## [3.5.0] — 2026-09-22` added with codename `AGSK — Antigravity Skill Migration & Legacy .agent Retirement`, containing `Changed`, `Removed` and `Compatibility and updating` subsections with link to `migrations/3.5.0.md` | local filesystem | VERIFIED | `.tfw/CHANGELOG.md` L8–40 |
| E6 | AC-6 | `python -m pytest tools/tests/ docs/scripts/ -q` → 14 passed in 3.91s, exit code 0 | local Python runtime | VERIFIED | inline: `14 passed in 3.91s` |
| E7 | AC-7 | `.agents/rules/tfw.md` and `.tfw/adapters/antigravity/tfw-rules.md.template` both contain `### Coordination Messaging` section with `send_message` instructions for Researcher, Executor and Reviewer; `git diff --no-index` returns zero diff (byte-identical); `.tfw/adapters/antigravity/README.md` contains `## Coordination Messaging` section documenting the same mechanics in table form | local filesystem + git diff | VERIFIED | `git diff --no-index .tfw/adapters/antigravity/tfw-rules.md.template .agents/rules/tfw.md` → exit 0, zero output |
| E-accounting | TS §4 accounting | TS approval: ONB commit `637df43` (TS approved by owner-direct `/tfw-handoff` invocation). Baseline: `a26322e2a9899936c0cdb1a1d523960b80f6aec9` (Phase A RF). Candidate: `bde7334ff626e8c2c43f315717f90271182b4ab3` (Implementation Candidate). VALUE membership: 10 files (1 CREATE `.tfw/migrations/3.5.0.md` + 9 MODIFY) — exact match to TS §4 denominator. Adds: 174, deletions: 5, touched text LOC: 179. Binary N/A: 0. Trigger: N/A (179 LOC « 5000, 10 files « 50). Authority/timing: TS approved by owner before execution via `/tfw-handoff` invocation. Candidate is the first tested implementation commit before EV/RF/trace writes. Exact command: `git diff --numstat --find-renames=50% a26322e bde7334 -- $valuePaths` | repo/Git | VERIFIED | see E-accounting output above |

## Verdict

Evidence verdict: 8/8 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

## Attachments

| File | Description |
|---|---|
| `doc-sweep.txt` | Stale-path sweep across all 10 VALUE files confirming zero `.agent/workflows/` or `.agent/rules/tfw.md` matches |

---

*EV — TFW_20260921-220500_AGSK / Phase B: Migration Guide and Documentation Sync | 2026-09-22*
