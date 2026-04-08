# Gather — "What do we NOT know?"
> Parent: [HL-TFW-29](../HL-TFW-29__consistency_audit.md)
> Goal: Reference files (conventions.md, glossary.md) and 11 workflows are free from redundancy — agents load minimum tokens for maximum signal.

## Findings

### G1: Workflow Context Loading Patterns — Verbatim Extraction

Every workflow was read. Here is exactly how each one loads context:

| # | Workflow | Context Loading Pattern | Explicit §-refs to conventions.md |
|---|----------|------------------------|-----------------------------------|
| 1 | **plan.md** | Step 1: "Read conventions.md §10. Verify: AGENTS.md, KNOWLEDGE.md, task board, conventions.md and glossary.md loaded." | §10 (context loading), §6 (scope budgets), §14 (anti-patterns ×2), §15 (role lock), §5 (status transitions) |
| 2 | **research/base.md** | Step 1: "Read conventions.md §10. Verify loaded: AGENTS.md, conventions.md, glossary.md, KNOWLEDGE.md, Master HL" | §10 (context loading), §14 (anti-patterns) |
| 3 | **handoff.md** | Full numbered list: 1.AGENTS.md 2.conventions.md 3.glossary.md 4.KNOWLEDGE.md 5.Master HL 6.Phase HL 7.TS 8.Related files 9.Code files | None — zero §-refs to conventions.md content |
| 4 | **review.md** | Full numbered list: 1.AGENTS.md 2.conventions.md 3.glossary.md 4.KNOWLEDGE.md 5.Master HL 6.Phase HL 7.TS 8.RF 9.Related files 10.Code files | None — zero §-refs to conventions.md content |
| 5 | **resume.md** | No explicit Context Loading section. Reads Master HL §1,§4,§7,§11 and Master TS. | None |
| 6 | **docs.md** | No explicit Context Loading section. | None |
| 7 | **knowledge.md** | Prerequisites: 1.knowledge_state.yaml 2.KNOWLEDGE.md 3.topic files 4.PROJECT_CONFIG.yaml | §10.1 (fact categories ×3) |
| 8 | **release.md** | Prerequisites: 1.RELEASE.md 2.CHANGELOG.md 3.VERSION 4.Task Board | None |
| 9 | **update.md** | Prerequisites: 1.PROJECT_CONFIG.yaml 2.Fetch upstream 3..upstream VERSION 4..upstream CHANGELOG | None |
| 10 | **config.md** | No explicit Context Loading section. Reads PROJECT_CONFIG.yaml on demand. | §6 (scope budgets, in Config Sync Registry) |
| 11 | **init.md** | No Context Loading (initializes from scratch). Phase 1: Discover reads project files. | None |

**Key observation:** Only 4 of 11 workflows explicitly load glossary.md (plan, research, handoff, review). The other 7 never mention glossary. But conventions.md §10 says "on every new session, load glossary.md" — so indirectly, all workflows that reference §10 load it.

### G2: Adapter Entry Points — What They Trigger

| Adapter | Context Loading Order | Workflow List | Issues Found |
|---------|----------------------|---------------|--------------|
| **AGENTS.md** (root) | 1.AGENTS.md 2.conventions.md 3.glossary.md 4.KNOWLEDGE.md 5.Task board 6.Relevant HL/TS/RF | Lists 5: plan, handoff, review, resume, docs | **Missing 6:** research, knowledge, init, config, release, update |
| **.agent/rules/agents.md** | Same as AGENTS.md | Lists 4: plan, handoff, resume, docs | **Missing 7:** research, knowledge, init, config, release, update, review. Also: handoff says "ONB→develop→RF→**REVIEW**" ← ERROR (handoff does NOT produce REVIEW) |
| **.agent/rules/tfw.md** | 1.AGENTS.md 2.`.agent/rules/conventions.md` OR `.tfw/conventions.md` 3.`.agent/rules/glossary.md` OR `.tfw/glossary.md` 4.KNOWLEDGE.md 5.HL/TS/RF | No workflow list | **References non-existent files**: `.agent/rules/conventions.md` and `.agent/rules/glossary.md` do not exist |

### G3: Anti-patterns — Full Block Comparison

**conventions.md §14** (16 items, authoritative):
- 8 executor-specific
- 3 coordinator-specific
- 3 role-lock violations (explicit)
- 2 mixed (scope/process)

**handoff.md** (13 items): Subset of conventions §14 with 2 additions:
- "Executor continues past Phase 3 — must STOP after RF" ← UNIQUE to handoff
- "Executor writes REVIEW file" ← exists in both, but handoff adds "🔒 Role Lock violation" label

**review.md** (7 items): Subset with 2 unique:
- "Reviewer writes REVIEW without reading RF" ← UNIQUE to review
- "Reviewer and executor are the same session" ← UNIQUE to review

**.tfw/README.md** (9 items): Strict subset of conventions §14 (no unique items). Phrased differently but identical content.

**resume.md** (6 items): All unique to resume context:
- "Skip reading Master HL/TS and jump straight to writing phase TS"
- "Read all RF files in full" 
- "Start planning without showing the status matrix first"
- "Assume phase order is fixed"
- "Ignore TECH_DEBT.md items from previous phases"
- "Ignore accumulated tech debt when planning next phase scope"

**init.md** (6 items): All unique to init context.

**config.md** (4 items): All unique to config context.

**Observation:** handoff and review have genuinely role-specific anti-patterns that ADD to §14, they don't just duplicate it. .tfw/README.md is a pure subset — adds nothing. resume/init/config anti-patterns are contextual, not generic.

### G4: Glossary Terms — Which Workflows Actually Use Them

Traced every glossary term through the 11 workflows:

| Glossary Term | Used By | Needed at Runtime? |
|---------------|---------|--------------------|
| CL/AG modes | AGENTS.md, plan (implicit), handoff (CL/AG task), init | Yes — but definition in conventions §7 is SoT |
| HL/RES/TS/RF/ONB/REVIEW | All workflows (universal) | Yes — but full defs in conventions §3 are SoT |
| Task Naming | plan (§4 creates folders) | Yes — but conventions §4 is SoT |
| Status Flow | plan (§5 updates board), resume, review | Yes — but conventions §5 is SoT |
| Concept Taxonomy | — | Never referenced by any workflow |
| RESEARCH (stage) | plan, research/base, research/deep | Yes, unique definition |
| Stage (Research) | research/base, research/deep | Yes, **unique** to glossary |
| Pass (Research) | research/base, research/deep | Yes, **unique** to glossary |
| Phase | handoff, resume, plan | Yes, **unique** standalone definition |
| Scope Budget | plan (§6) | Yes — conventions §6 is SoT |
| Workflow (canonical) | — | Meta-definition, never used at runtime |
| .tfw/ Directory | — | Meta-definition, never used at runtime |
| Tool Adapter | init, update | Useful, **unique** standalone definition |
| Roles (5 roles) | All workflows (via Role Lock) | Yes, **unique** role definitions |
| Read-only AG | research/base | Yes, **unique** to glossary |
| Execution Engine | — | Config-level, never used at runtime |
| Progress Reporting | — | Config-level, never used at runtime |
| Task Board | plan, resume | Yes — conventions §5 is partial SoT |
| PROJECT_CONFIG.yaml | config, plan, knowledge, research | Useful, though not essential — agents read the file directly |
| VERSION/CHANGELOG.md | release, update | Useful, **unique** standalone definition |
| Fact Candidate | handoff (§6), review (§5), knowledge, research | Yes, **unique** to glossary (detail beyond §10.1 ref) |
| Strategic Insight | plan (§11), knowledge (§11/§7) | Yes, **unique** to glossary |
| Topic File | knowledge | Yes, **unique** to glossary |
| Knowledge Gate | plan (Step 2) | Yes, **unique** to glossary |
| Consolidation | knowledge | Yes, **unique** to glossary |
| Config Sync Registry | config | Yes, **unique** to glossary |
| RELEASE.md | release | Useful, **unique** standalone definition |
| tfw-init/tfw-release/tfw-update | init, release, update | Meta-descriptions, workflows are self-describing |
| Compilable Contract | — | Never referenced by any workflow at runtime |
| Reference Format | — | Never referenced by any workflow at runtime |
| Source Manifest | — | Never referenced by any workflow at runtime |
| TECH_DEBT.md | review, docs | Useful, conventions §2 has the same |
| KNOWLEDGE.md | docs, knowledge | Useful, conventions §2 has the same |

### G5: External Research — DRY Documentation for AI Agent Prompts

**Source:** Anthropic docs, industry surveys, AI agent framework best practices (2025-2026).

Key findings:
1. **Progressive Disclosure** is the consensus pattern — inject only what the agent needs for the current task, not everything upfront.
2. **"Lost in the middle" problem** — models process information at the start and end of context better than the middle. Long reference docs get "lost."
3. **Modular architecture** preferred — core identity (AGENTS.md) + task-specific modules (workflow) + shared guardrails (conventions). Glossary = shared guardrail.
4. **DRY is correct for source-of-truth**, but **critical enforcement instructions must be inline** — exactly what TFW's D24 (Pattern A) already establishes.
5. **Self-contained per-role is wasteful** — if handoff loads both conventions AND glossary AND its own anti-pattern block, tokens are wasted on duplicate content.

**Verdict on glossary duplication:** External best practice supports TFW's current direction (DRY). The glossary should NOT duplicate conventions — it should define terms that conventions doesn't, and link to conventions for shared definitions. Self-contained per-role context is an anti-pattern for cost and coherence.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Full workflow context loading map for all 11 workflows + 3 adapters | — |
| Complete §-reference inventory across all workflows | — |
| Anti-patterns: 4 block comparison (README is pure subset, handoff/review add unique items) | — |
| Glossary term usage: 15 unique terms, 10 duplicated, 6 meta/unused | — |
| External: progressive disclosure + modular docs confirmed as best practice | — |

**Sufficiency:**
- [x] External source used? (Anthropic docs, industry best practices survey)
- [x] Briefing gap closed? (All 3 briefing Gather bullets covered)

Stage complete: YES
→ User decision: proceed to Extract
