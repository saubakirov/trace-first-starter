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

> **Before writing Fact Candidates, review the conversation history.** The human's
> messages are the primary source of strategic knowledge — domain insights, stakeholder
> priorities, business context, and constraints that shape decisions.
>
> Good: "18% clients = 80% revenue (Pareto)", "stakeholder: find problem clients first"
> NOT fact candidates: "project uses git", "code is in Python", implementation details (→ §5 Observations → tfw-docs)
>
> **Human-Only Test**: would this fact be unknown without the human saying it?
> If an agent can discover it by reading code or running commands — it's not a fact candidate.
> These are NOT verified facts. They become facts after `/tfw-knowledge` consolidation.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | {category} | {what you learned} | {where from} | High/Medium/Low |

> **Source format**: Use reference patterns (e.g., `RF TFW-18`, `D24`). See compilable_contract.md §2.

> **Categories** (open list): `environment`, `process`, `stakeholder`, `constraint`, `convention`, `domain`, `context`, `risk`, `philosophy`

---

*RF — {PREFIX}-{N} / Phase {X}: {Title} | YYYY-MM-DD*
