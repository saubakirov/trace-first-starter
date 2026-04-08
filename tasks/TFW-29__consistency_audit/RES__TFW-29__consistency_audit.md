# RES — TFW-29: Consistency Audit

> **Date**: 2026-04-08
> **Author**: Researcher (AI)
> **Status**: ✅ RES — Complete
> **Parent HL**: [HL-TFW-29](HL-TFW-29__consistency_audit.md)
> **Mode**: Pipeline

---

## Research Context
TFW-29 audits the three core reference files (conventions.md, glossary.md, .tfw/README.md) and 11 workflows for redundancy, contradiction, and dead weight. The HL identified structural issues through static analysis. This research empirically validated those findings by tracing every workflow's actual reading path — what each workflow loads, which §-sections it references, which glossary terms it needs — and stress-tested every proposed compression for breakage risk.

## Briefing
→ [research/briefing.md](research/briefing.md)

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Glossary compression to ~104 lines (not 80 as HL estimated) | 15 unique terms at full length + 10 duplicated terms as 1-liners + 6 meta terms removed. User flagged 80 as potentially too small — 104 preserves all Tier 1 terms. H4 refuted: glossary terms needed by 5+ non-Research workflows. |
| D2 | Anti-patterns architecture: Option B (§14 = generic, workflows own role-specific) | handoff/review have genuinely unique role-specific anti-patterns (Executor STOP after RF, Reviewer same-session). resume/init/config anti-patterns are contextual. Putting all in §14 adds noise. .tfw/README.md block → ref to §14 (pure subset, 0 unique items). Matches D25 DNA/Library pattern. |
| D3 | §16 Compilable Contract: extract to `.tfw/compilable_contract.md` | Section Usage Matrix confirms 0 of 11 workflows reference §16 at runtime. Only gen_docs.py consumes it. ~100 lines freed from conventions.md. |
| D4 | Conventions §10 numbering: reorder §10.1/§10.2 before §10 → §10/§10.1/§10.2 in logical order | Current numbering has §10.1, §10.2, then §10 — confusing. Fix: rename §10 (Context Loading) to §10.3 or move it before §10.1. Simplest: swap order so §10 comes first. |
| D5 | 55% of conventions.md sections are dead at runtime — but should NOT be removed | Dead sections (§1-§3, §7-§8, §12-§13) serve as onboarding reference for new human readers and as background context agents absorb during initial loading. They're not "read" at runtime but they're not waste either — they inform. Compression target should focus on duplicated content, not on "reference" content. |
| D6 | resume.md and docs.md need Context Loading sections | Bug found: both coordinator workflows lack loading instructions. Agent starting fresh has no guidance. Fix in TS. |
| D7 | AGENTS.md must list all 11 workflows | Bug found: lists 5/11. `.agent/rules/agents.md` lists 4/11 and has a factual error (handoff→REVIEW). Fix in TS. |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| 1 | Should §14 anti-patterns be separated by role (§14.1 Executor, §14.2 Coordinator, §14.3 Reviewer) or stay as one mixed list? | Resolved | Option B chosen: §14 stays as one list (generic). Role-specific items stay inline in workflows. No §14.1/14.2/14.3 needed. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | Compilable Contract (§16) is never read by any workflow at runtime | confirmed | ✅ Confirmed | Section Usage Matrix: 0/11 workflows reference §16. grep confirms no workflow mentions §16, Source Manifest, Reference Format, or Frontmatter Convention. |
| H2 | All workflows follow the same 4-step context loading pattern but then diverge | open | 🟡 Partially Confirmed | Spine is real for 4 core workflows (plan, research, handoff, review). 5 workflows use own prerequisites (knowledge, release, update, config, init). 2 workflows have NO loading (resume, docs) — a bug. |
| H3 | Anti-patterns in .tfw/README.md, handoff.md add unique items not in conventions.md §14 | confirmed | ✅ Confirmed + nuanced | README adds 0 unique items (pure subset). handoff adds 2 unique. review adds 2 unique. resume/init/config add contextual unique items. |
| H4 | Only Research workflows need glossary-unique terms | open | ❌ Refuted | 5 non-Research workflows need glossary-unique terms: handoff (Phase, Fact Candidate), review (Roles, Strategic Insight), plan (Knowledge Gate, Phase), knowledge (Topic File, Consolidation), resume (Phase). |

## HL Update Recommendations

| # | What to update | Source |
|---|---------------|--------|
| 1 | §2.4 glossary target: change from ~80 lines to ~104 lines | D1 — H4 refuted, more unique terms than expected |
| 2 | §2.4 / §4 PhaseA: add "Fix resume.md and docs.md missing Context Loading" | D6 — bug found |
| 3 | §2.4 / §4 PhaseA: add "Fix AGENTS.md workflow list (5→11) and sync adapter" | D7 — bug found |
| 4 | §4 PhaseA: add "Anti-patterns architecture: §14 stays generic, .tfw/README.md block → ref" | D2 — resolved question |
| 5 | DoD §8: change glossary target from ≤130 to ≤110 lines (realistic with 104-line estimate + headers) | D1 |
| 6 | §3.1 Target State: update AFTER word count from ~5,200 to reflect actual estimate | D5 — dead sections kept |

## Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | convention | Agent context loading divides into 2 architecture styles: "Spine + extend" (core workflows that reference conventions §10 and then add role-specific files) and "Own prerequisites" (specialized workflows with task-specific file lists). Both are valid. | RES TFW-29, Extract E3 | High |
| FC2 | process | Glossary serves as a shared terminology layer across all roles, not just Research. 15 of its terms are unique and used by 5+ workflows. Removing glossary from non-Research context would cause terminology gaps. | RES TFW-29, Challenge C2 | High |
| FC3 | constraint | User indicates 80-line glossary may be too small ("может 80 мало"). Research confirmed: 104 lines is the practical floor for preserving all unique term definitions. | User (briefing), RES TFW-29 D1 | High |

## Conclusion

This research validated all 4 hypotheses from HL §10 and discovered 2 bugs not anticipated in static analysis (missing Context Loading in resume/docs, incomplete workflow list in AGENTS.md). The Section Usage Matrix proved that 55% of conventions.md is unreferenced at runtime, but this content serves as onboarding reference — the compression opportunity is in deduplication (glossary→refs, README anti-patterns→refs), not in removing reference sections. The glossary compression target should be ~104 lines (not 80), since H4 was refuted and 15 terms are genuinely unique across 5+ workflows. Anti-patterns should follow Option B: generic list in §14, role-specific items inline in workflows, README block replaced with ref. External research confirmed that DRY + progressive disclosure is the correct architecture for AI agent documentation. Without this research, the 80-line glossary target and the assumption that non-Research workflows don't need glossary would have led to overcutting.

---

*RES — TFW-29: Consistency Audit | 2026-04-08*
