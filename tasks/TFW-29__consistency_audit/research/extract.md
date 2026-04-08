# Extract — "What do we NOT see?"
> Parent: [HL-TFW-29](../HL-TFW-29__consistency_audit.md)
> Goal: Reference files (conventions.md, glossary.md) and 11 workflows are free from redundancy — agents load minimum tokens for maximum signal.

## Findings

### E1: Section Usage Matrix — conventions.md Sections × Workflows

Legend: **R** = reads/references at runtime, **D** = duplicates content from it, **—** = ignores

| § | Section | plan | research | handoff | review | resume | docs | knowledge | release | update | config | init |
|---|---------|------|----------|---------|--------|--------|------|-----------|---------|--------|--------|------|
| 1 | Purpose | — | — | — | — | — | — | — | — | — | — | — |
| 2 | Required Artifacts | — | — | — | — | — | — | — | — | — | — | — |
| 3 | Artifact Types | — | — | — | — | — | — | — | — | — | — | — |
| 4 | Task Numbering | R | — | — | — | — | — | — | — | — | — | — |
| 5 | Task Statuses | R | — | — | — | — | — | — | — | — | — | — |
| 6 | Scope Budgets | R | — | — | — | — | — | — | — | — | R | — |
| 7 | Execution Modes | — | — | — | — | — | — | — | — | — | — | — |
| 8 | Workflows | — | — | — | — | — | — | — | — | — | — | — |
| 9 | Tool Adapter | — | — | — | — | — | — | — | — | R | — | R |
| 10 | Context Loading | R | R | D | D | — | — | — | — | — | — | — |
| 10.1 | Fact Categories | — | — | — | — | — | — | R | — | — | — | — |
| 10.2 | Knowledge Infra | — | — | — | — | — | — | — | — | — | — | — |
| 11 | Quality Standard | — | — | — | — | — | — | — | — | — | R | — |
| 12 | Safety | — | — | — | — | — | — | — | — | — | — | — |
| 13 | Trace Discipline | — | — | — | — | — | — | — | — | — | — | — |
| 14 | Anti-patterns | R | R | D | D | — | — | — | — | — | — | — |
| 15 | Role Lock | R | — | — | — | — | — | — | — | — | — | — |
| 16 | Compilable Contract | — | — | — | — | — | — | — | — | — | — | — |
| 16.1 | Source Manifest | — | — | — | — | — | — | — | — | — | — | — |
| 16.2 | Reference Format | — | — | — | — | — | — | — | — | — | — | — |
| 16.3 | Frontmatter | — | — | — | — | — | — | — | — | — | — | — |
| 16.4 | Output Nav | — | — | — | — | — | — | — | — | — | — | — |

**Dead sections** (never R or D by any workflow at runtime):
- §1 Purpose
- §2 Required Artifacts (list of files — onboarding/init reference only)
- §3 Artifact Types (loaded as background knowledge, never explicitly referenced)
- §7 Execution Modes (only referenced via AGENTS.md, not via conventions.md)
- §8 Workflows (table, never used at runtime)
- §10.2 Knowledge Infrastructure (table, knowledge.md reads the files directly)
- §12 Safety
- §13 Trace Discipline
- §16 entire block (all 4 sub-sections)

**Active sections** (referenced at least once):
- §4, §5, §6, §9, §10, §10.1, §11, §14, §15

That's 9 active § out of 20 total § — **55% of conventions.md content is never read by a workflow at runtime.**

### E2: Glossary Dependency Map — Term Categories

Based on G4 data, glossary terms fall into 3 clear tiers:

**Tier 1: Unique terms (15) — MUST stay in glossary, no duplicate elsewhere**
- Stage (Research), Pass (Research), Read-only AG
- Phase, Scope Budget
- Fact Candidate, Strategic Insight, Topic File, Knowledge Gate, Consolidation
- Config Sync Registry
- Roles (User, Coordinator, Researcher, Executor, Reviewer) — 5 role definitions
- Tool Adapter

**Tier 2: Duplicated terms (10) — conventions.md has the SoT, glossary duplicates**
- HL, RES, TS, RF, ONB, REVIEW (full definitions — conventions §3 is authoritative)
- CL/AG modes (conventions §7 is authoritative)
- Task Naming (conventions §4 is authoritative)
- Status Flow (conventions §5 is authoritative)
- TECH_DEBT.md, KNOWLEDGE.md (conventions §2 is authoritative)

**Tier 3: Meta/unused terms (6) — never referenced by any workflow at runtime**
- Concept Taxonomy (nice-to-have for humans, agents never read it)
- Workflow (canonical) — self-referential, workflows don't need a definition of "workflow"
- .tfw/ Directory — same, meta
- Execution Engine, Progress Reporting — config-level, never used
- tfw-init, tfw-release, tfw-update workflow descriptions — workflows self-describe, these are redundant

**Compression plan:**
| Tier | Current lines | Proposed | Savings |
|------|--------------|----------|---------|
| Tier 1 (unique) | ~85 lines | Keep as-is | 0 |
| Tier 2 (duplicated) | ~60 lines | 1-liner + "→ conventions.md §N" per item | ~45 lines saved |
| Tier 3 (meta/unused) | ~25 lines | Remove entirely | ~25 lines saved |
| Compilable Contract terms | ~12 lines | 1-liner + "→ conventions.md §16" | ~8 lines saved |
| **Total** | **~182 lines** | **~104 lines** | **~78 lines saved** |

**Result: ~104 lines** — larger than the HL's 80-line estimate, but the user flagged 80 as potentially too small. 104 preserves all Tier 1 terms at full length.

### E3: Common Spine vs Divergence Report

**Common Spine (shared by plan, research, handoff, review):**
```
1. AGENTS.md
2. .tfw/conventions.md
3. .tfw/glossary.md
4. KNOWLEDGE.md (if exists)
5. Relevant task artifacts (HL/TS/RF)
```

**Divergence points:**

| Workflow | Divergence from spine | Intentional? |
|----------|----------------------|--------------|
| **plan.md** | Says "Read §10" (1-line ref) — trusts spine is in conventions | ✅ Intentional (Pattern A ref-inside-step) |
| **research/base.md** | Says "Read §10. Verify loaded:" — lists what to check | ✅ Intentional (same pattern) |
| **handoff.md** | Full expanded list (9 items, includes Phase HL, Code files) — duplicates §10 + adds executor-specific items | ⚠️ Mostly intentional (executor needs more context) but duplicates the first 4 items verbatim |
| **review.md** | Full expanded list (10 items, includes RF mandatory) — duplicates §10 + adds reviewer-specific items | ⚠️ Same pattern as handoff — duplicates core 4, adds role-specific items |
| **resume.md** | No Context Loading section at all | ❓ Unclear — coordinator workflow without a loading step |
| **docs.md** | No Context Loading section at all | ⚠️ Problematic — runs after review, should load something |
| **knowledge.md** | Own Prerequisites section (reads YAML, doesn't load conventions/glossary) | ✅ Intentional — knowledge workflow needs specific files, not general context |
| **release.md** | Own Prerequisites (RELEASE.md, CHANGELOG, VERSION) | ✅ Intentional — release-specific context |
| **update.md** | Own Prerequisites (CONFIG, upstream fetch) | ✅ Intentional — update-specific context |
| **config.md** | No Context Loading section | ⚠️ Reads CONFIG on demand in step — works but inconsistent |
| **init.md** | No Context Loading (creates everything from scratch) | ✅ Intentional — nothing exists yet |

**Pattern:** Workflows divide into 2 architecture styles:
1. **"Spine + extend" (plan, research, handoff, review)** — reference or expand the 4-step spine
2. **"Own prerequisites" (knowledge, release, update, config, init)** — task-specific context, no general spine

The **resume** and **docs** workflows are in neither camp — they have no explicit context loading at all.

### E4: Anti-patterns Architecture Decision

From G3, the blocks divide cleanly:

| Source | Role | Items | Unique to source? |
|--------|------|-------|--------------------|
| conventions.md §14 | All | 16 | 13 generic + 3 explicit role-lock |
| handoff.md | Executor | 13 | 2 unique (STOP after RF, continues past Phase 3) |
| review.md | Reviewer | 7 | 2 unique (reviews without reading RF, same-session reviewer) |
| .tfw/README.md | All | 9 | 0 unique — pure subset of §14 |
| resume.md | Coordinator | 6 | 6 unique (all resume-specific) |
| init.md | Coordinator | 6 | 6 unique (all init-specific) |
| config.md | Coordinator | 4 | 4 unique (all config-specific) |

**Decision analysis:**
- **Option A: Unified list in §14** — merge handoff/review unique items into §14, tag by role. Simple governance, single source. But §14 grows to ~20 items.
- **Option B: §14 = generic, workflows own role-specific** — §14 keeps 16 generic items. Each workflow keeps only its unique items. `.tfw/README.md` block → "→ conventions.md §14".
- **Option C: Separate §14 by role** (user's lean) — §14.1 Executor, §14.2 Coordinator, §14.3 Reviewer. Workflows say "→ §14.{role}".

**Recommendation: Option B.** Reasons:
1. Handoff/review unique items are truly role-specific: "Executor STOP after RF" only makes sense inline in handoff. Putting it in conventions adds cognitive load for non-executors.
2. Resume/init/config anti-patterns are contextual — they'd be noise in a generic list.
3. §14 stays compact (16 items). README block becomes a ref.
4. This matches the "DNA/Library" pattern (D25): enforcement-critical stays inline (the role-specific anti-patterns at point of use), reference data goes via ref (generic anti-patterns via §14).

### E5: Token Cost Estimation

Current duplication cost per session (agent loads conventions + glossary + workflow):

| Duplication category | Approx words duplicated | Tokens (~0.75 words/token) |
|---------------------|------------------------|---------------------------|
| Artifact defs (conventions §3 + glossary) | ~300 words | ~400 tokens |
| Status flow (conventions §5 + glossary) | ~100 words | ~133 tokens |
| Anti-patterns (.tfw/README = copy of §14) | ~150 words | ~200 tokens |
| Context Loading (§10 + handoff/review expansions) | ~100 words | ~133 tokens |
| CL/AG modes (conventions §7 + glossary + AGENTS.md) | ~80 words | ~107 tokens |
| Compilable Contract terms (glossary repeats §16 defs) | ~80 words | ~107 tokens |
| TECH_DEBT/KNOWLEDGE defs (§2 + glossary) | ~40 words | ~53 tokens |
| **Total per session** | **~850 words** | **~1,133 tokens** |

Not catastrophic per session, but accumulated over many sessions, it multiplies. More importantly, it's **confusion cost** — agents see the same concept defined slightly differently in 2-3 places, increasing misinterpretation risk.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Section Usage Matrix: 55% of conventions.md is dead at runtime | — |
| Glossary: 15 unique, 10 duplicated, 6 unused → can compress to ~104 lines | — |
| Common Spine: real pattern for 4 workflows, 2 styles, 2 workflows missing loading | — |
| Anti-patterns: Option B recommended (§14 stays generic, workflows own role-specific) | — |
| ~1,133 tokens/session wasted on duplication | — |

**Sufficiency:**
- [x] External source used? (Section Usage Matrix built from full workflow corpus)
- [x] Briefing gap closed? (All 4 Extract bullets from briefing covered)

Stage complete: YES
→ User decision: proceed to Challenge
