# Challenge — "What do we NOT expect?"
> Parent: [HL-TFW-29](../HL-TFW-29__consistency_audit.md)
> Goal: Reference files (conventions.md, glossary.md) and 11 workflows are free from redundancy — agents load minimum tokens for maximum signal.

## Findings

### C1: Hypothesis H2 — Is the Common Spine Real?

**Hypothesis:** All workflows follow the same 4-step context loading pattern but then diverge — the divergence points reveal which convention sections are actually needed per role.

**Verdict: PARTIALLY CONFIRMED.**

The spine (AGENTS → conventions → glossary → KNOWLEDGE → task artifacts) is real and shared by 4 core workflows (plan, research, handoff, review). But it's not universal:
- 5 workflows (knowledge, release, update, config, init) use their own prerequisites — they don't need the general spine because they work with specific files.
- 2 workflows (resume, docs) have NO loading section — a gap, not a design choice.

The divergence points DO reveal role-specific needs:
- **plan** needs §4, §5, §6, §10, §14, §15 — the most §-hungry workflow
- **research** needs §10, §14 — minimal
- **handoff/review** need the full spine but DON'T reference any specific § — they get value from conventions/glossary as background, not from specific rules

**Implication for compression:** The spine workflows will still load conventions + glossary. But the "dead" 55% of conventions.md means the spine workflows waste context on unreferenced sections. The fix isn't to split conventions — it's to ensure every section earns its place.

### C2: Hypothesis H4 — Can Non-Research Workflows Skip Glossary?

**Hypothesis:** Only Research workflows actually need glossary-unique terms (Stage, Pass, OODA); other workflows could skip glossary.

**Verdict: REFUTED.**

Glossary-unique terms needed by non-Research workflows:
1. **handoff.md** needs: Phase, Scope Budget, Fact Candidate, Roles (Executor)
2. **review.md** needs: Roles (Reviewer), Fact Candidate, Strategic Insight
3. **plan.md** needs: Phase, Knowledge Gate, Strategic Insight, RESEARCH (concept, not just workflow), Roles (Coordinator)
4. **knowledge.md** needs: Topic File, Consolidation, Fact Candidate, Knowledge Gate, Config Sync Registry
5. **resume.md** needs: Phase (core to its function)

**Conclusion:** Glossary has value beyond Research. The ~15 unique terms serve multiple workflows. Removing glossary from context loading would harm terminology consistency.

**But:** The 10 duplicated terms and 6 meta terms should still be compressed. An agent loading glossary should get unique definitions, not re-reads of conventions.

### C3: Counter-argument — Self-Contained Glossary is USEFUL

**The case FOR duplicating artifact defs in glossary:**
- Glossary is a lookup document. An agent looking up "HL" shouldn't need to cross-reference conventions.md — the definition should be right there.
- Progressive disclosure says "load only what you need." If a glossary has 1-liners + refs, the agent must now load 2 files to understand a term.

**The case AGAINST (stronger):**
1. The 1-liners still provide enough context for lookup: "HL (High Level) — context/frame artifact for a task. → conventions.md §3 for full definition." An agent knows what HL is from this single line.
2. The full definitions in glossary DON'T match conventions perfectly — they add/omit details, creating subtle inconsistencies. Example: glossary's HL entry mentions "Contains: Vision, As-Is, To-Be, Phases, DoD, DoF, Principles, Dependencies, Risks" — this list is NOT in conventions §3 and could drift as the HL template evolves.
3. When conventions §3 is updated, glossary must be manually synced. This has already drifted — evidence: glossary says HL "Contains: Vision, As-Is, To-Be..." which is the OLD template structure (pre-TFW-24, which added §10 RESEARCH Case and §11 Strategic Insights).
4. External research (G5) confirmed: duplication is an anti-pattern for AI agent context. DRY + precise refs is the correct architecture.

**Verdict:** 1-liners with refs are sufficient. The convenience of self-contained lookup does NOT justify the consistency risk and token cost.

### C4: Risk Check — What Could Break from HL §2.4 Compression?

Testing each proposed compression against the workflow corpus:

| HL Proposal | Risk | Assessment |
|-------------|------|------------|
| Glossary: replace artifact defs with 1-liners + refs | Could break if any workflow reads glossary for artifact semantics | **Safe** — no workflow reads glossary for artifact definitions. They read conventions §3 or the templates directly. |
| Glossary: replace status flow diagram with ref | Could break if any workflow reads glossary for status transitions | **Safe** — only plan.md reads §5, and it reads from conventions.md directly. |
| Glossary: remove Concept Taxonomy | Could break if any workflow uses it | **Safe** — grep shows 0 runtime references from any workflow. |
| Glossary: remove .tfw/ Directory definition | Could break if init/update rely on it from glossary | **Safe** — init/update read the actual directory, not a glossary definition of it. |
| Conventions: extract §16 to separate file | Could break if any workflow reads §16 at runtime | **Safe** — Section Usage Matrix shows 0 workflow references. Only gen_docs.py reads it via compilable contract. |
| Conventions: §10 numbering fix | Could break plan.md / research ref "§10" | **Safe** — refs use "§10" which will still work. Renumbering §10.1/10.2 before §10 to §10→§10.1→§10.2 just fixes ordering. |
| .tfw/README.md: remove anti-patterns block | Could break if any workflow refs README anti-patterns | **Safe** — no workflow references README.md for anti-patterns. They reference conventions.md §14 directly. |

**No breakage risk identified** for any proposed compression.

### C5: Gap Found — resume.md and docs.md Missing Context Loading

Both workflows run in Coordinator role but have no Context Loading section. This means:
- An agent starting `/tfw-resume` without prior context has no instructions to load conventions or glossary
- An agent starting `/tfw-docs` after a review has no instructions to load KNOWLEDGE.md (which it's about to update)

This is a bug, not a design choice. Both should have at minimum: "Read conventions.md §10" or their own prerequisite list.

**Recommendation:** Add minimal loading to both:
- resume.md: "Read conventions.md §10. Then read Master HL for the target task."
- docs.md: Already has trigger modes. Add prerequisite: "Read KNOWLEDGE.md and TECH_DEBT.md before starting checklist."

### C6: Gap Found — AGENTS.md Lists Only 5 of 11 Workflows

AGENTS.md §Workflows lists only plan, handoff, review, resume, docs. Missing: research, knowledge, init, config, release, update.

`.agent/rules/agents.md` is worse — only lists 4 (plan, handoff, resume, docs — missing review!) and has the "handoff → REVIEW" error.

**Impact:** An agent in a fresh session doesn't know research, knowledge, init, config, release, or update workflows exist. It can't recommend `/tfw-research` or `/tfw-knowledge` if it doesn't know they're available.

**Recommendation:** AGENTS.md must list all 11 workflows. The adapter `.agent/rules/agents.md` must be synced with AGENTS.md.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| H2: partially confirmed — spine is real for 4 workflows, not universal | — |
| H4: refuted — glossary unique terms needed by 5+ non-Research workflows | — |
| Self-contained glossary case lost — consistency risk > lookup convenience | — |
| All HL §2.4 compressions verified safe — zero breakage risk | — |
| Bug: resume.md and docs.md missing Context Loading | — |
| Bug: AGENTS.md lists only 5/11 workflows | — |

**Sufficiency:**
- [x] External source used? (G5 external research applied to challenge arguments)
- [x] Briefing gap closed? (All 3 Challenge bullets from briefing covered)

Stage complete: YES
→ User decision: proceed to Synthesis
