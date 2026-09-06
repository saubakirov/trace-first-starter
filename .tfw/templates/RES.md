# RES — {ID}: {Title}

> **Date**: YYYY-MM-DD
> **Author**: {author}
> **Status**: 🔬 RES — In progress
> **Parent HL**: [HL-{ID}](path) _(pipeline only)_
> **Mode**: Pipeline / Standalone

---

## Research Context
{One paragraph: what we are researching and why.}

## Briefing
{Copied from or reference to `1_briefing.md` in iteration folder.}

## Decisions
| # | Decision | Rationale |
|---|----------|-----------|

## Open Questions
| # | Question | Status | Answer |
|---|----------|--------|--------|

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | {text} | open | 🟡 testing | |

## HL Update Recommendations

> **The researcher classifies, never applies or rules.** Each recommendation names its HL section.
> Refinements target free sections (§2, §7.2, §8–§11); Amendment Proposals target frozen sections
> (§1, §3–§7). The Coordinator transcribes the latter into §12 as `PROPOSED`, preserving origin, then
> routes by `conventions.md` → `HL Contract` rule 8. Frozen claims wait for a valid terminal verdict.
> Use §3's declarative-claim granularity and §15 Role Lock. Empty class: **No refinements.** /
> **No amendment proposals.**

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §{n} | {what changes} | {stage finding} |

### Amendment Proposals — frozen sections, resolved-ruler verdict required

> Same columns as HL §12 except `Date`, originating `Proposer`, and `Verdict`, which the Coordinator
> adds; verdict starts `PROPOSED`. Reassign local `A1`, `A2` … into append-only §12. Evidence, cost,
> and a considered alternative are mandatory.

| # | § | Type | Proposed change | Evidence | Cost | Alternatives considered |
|---|---|------|-----------------|----------|------|------------------------|
| A1 | §{n} | `EXTEND` / `SUPERSEDE` / `RESTRICT` | {what changes} | {where the finding comes from} | {what it costs to accept} | {what else was weighed and why it lost} |

## Fact Candidates

> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.
>
> **Scope:** Agent-observed project patterns discovered during research.
> Record facts about THIS project — not findings about alternatives,
> not implementation details (those belong in tfw-docs).
>
> **Human-Only Test**: would this fact be unknown without the human saying it?
> If an agent can discover it by reading code or running commands — it's not a fact candidate.
> These are NOT verified facts. They become facts after `/tfw-knowledge` consolidation.
>
> **Before writing:** review the conversation history. The human's messages are the primary source.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|

> **Source format**: Use reference patterns (e.g., `HL-TFW-19`, `D24`). See compilable_contract.md §2.

## Strategic Insights (Research)

> **Cognitive mode:** Deep analytical synthesis. Capture human-sourced domain knowledge
> observed during research briefings, then ADD implications — what does this insight
> mean for the project's direction?
>
> **Human-Only Test:** Would this insight be unknown without the user saying it?
> If an agent can discover it by reading code — it's NOT a strategic insight, it's a Fact Candidate.
>
> **When to fill:** Only when the human provides domain knowledge, corrections, or strategic
> context in research briefings. If no human interaction occurred — write "No strategic insights."
>
> **Categories:** conventions.md §10.1.

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS1 | {category} | {insight} | User, {context} | ★★★/★★☆/★☆☆ |

## Findings Map

> **Cognitive mode:** Analytical research visualization.
> Visualize research findings: root cause analysis, hypothesis trees, priority matrices,
> relationship maps between discoveries.
>
> Formats: ASCII, mermaid, or structured tables.
> Focus: WHAT was discovered and WHY — pattern relationships, causal chains, decision trees.
>
> If no visualization is relevant — write "No findings map."

## Iteration Status

> **Mandatory block.** Every RES must include this, even for single-iteration research.

- **Iteration:** {N} of {min} (min) / {max} (max)
- **Hypotheses tested:** {H1 (status), H2 (status)...}
- **Hypotheses deferred:** {HN (reason) — or "None"}
- **Gaps discovered:** {list — or "None"}
- **Superseded decisions:** {DN supersedes DM (reason) — or "None"}

### Open Threads (for next iteration)

> If no open threads — write "No open threads."

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | {thread description} | {impact if not addressed} | {what next iteration should do} |

### Recommendation
- [ ] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations and write TS
- [ ] **MORE NEEDED** — {specify what and why}
- [ ] **BLOCKED** — {specify blocker}

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion
{One paragraph. What was researched. Key decisions made. What RESEARCH provided that would have been missed without it. Self-critique.}

---

*RES — {ID}: {Title} | YYYY-MM-DD*
