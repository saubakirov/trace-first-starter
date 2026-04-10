# RF — {PREFIX}-{N} / Phase {X}: {Title}

> **Date**: YYYY-MM-DD
> **Author**: {author}
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-{PREFIX}-{N}](path-to-HL)
> **TS**: [TS Phase {X}](path-to-TS)

---

## 1. What Was Done

### New Files
| File | Description |
|------|------------|
| `path/to/file` | {description} |

### Modified Files
| File | Changes |
|------|---------|
| `path/to/file` | {description} |

## 2. Key Decisions

1. {Decision and rationale}
2. {Decision and rationale}

## 3. Acceptance Criteria

- [x] {Criterion from TS}
- [x] {Criterion from TS}

## 4. Verification

- Lint (`{config.build.lint}`): {result}
- Tests (`{config.build.test}`): {result}
- Verify (`{config.build.verify}`): {result}

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `path/to/file` | {lines} | {type} | {description} |

> **Types:** `dead-code`, `naming`, `todo`, `duplication`, `perf`, `security`, `style`, `missing-test`, `ux`
>
> **Quality bar**: report only issues that would bite the next developer. Don't generate observations just because the section exists.
> If nothing found: `No observations.`

## 6. Fact Candidates

> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.
>
> **Scope:** Agent-observed project patterns discovered during execution.
> Good: "18% clients = 80% revenue (Pareto)", "stakeholder: find problem clients first"
> NOT fact candidates: "project uses git", implementation details (→ §5 Observations → tfw-docs),
> or agent-generated analysis (→ §7 Strategic Insights).
>
> **Human-Only Test**: would this fact be unknown without the human saying it?
> If an agent can discover it by reading code or running commands — it's not a fact candidate.
> These are NOT verified facts. They become facts after `/tfw-knowledge` consolidation.
>
> **Before writing:** review the conversation history. The human's messages are the primary source.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | {category} | {what you learned} | {where from} | High/Medium/Low |

> **Source format**: Use reference patterns (e.g., `RF TFW-18`, `D24`). See compilable_contract.md §2.

> **Categories** (open list): see conventions.md §10.1 for full list with scope descriptions.

## 7. Strategic Insights (Execution)

> **Cognitive mode:** Deep analytical synthesis. Capture human-sourced domain knowledge
> observed during execution, then ADD implications — what does this insight mean for the project?
>
> **Human-Only Test:** Would this insight be unknown without the user saying it?
> If an agent can discover it by reading code — it's NOT a strategic insight, it's a Fact Candidate (§6).
>
> **When to fill:** Only when the human provides domain knowledge, corrections, or strategic
> context DURING execution. If no human interaction occurred — write "No strategic insights."
>
> **Categories:** conventions.md §10.1.

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | {insight} | {category — see §10.1} | User, {context} |

> **Source format**: Use reference patterns (e.g., `RF TFW-18`, `D24`). See compilable_contract.md §2.

## 8. Diagrams

> **Cognitive mode:** Technical engineering documentation.
> Visualize architecture, data flow, component interaction, or sequence diagrams
> for the work completed in this phase.
>
> Formats: ASCII, mermaid, or structured tables.
> Focus: HOW the system is built — components, layers, protocols, data flow.
>
> If no diagrams are relevant — write "No diagrams."

---

*RF — {PREFIX}-{N} / Phase {X}: {Title} | YYYY-MM-DD*
