# REVIEW — {PREFIX}-{N} / Phase {X}: {Title}

> **Date**: YYYY-MM-DD
> **Author**: {reviewer}
> **Verdict**: ✅ APPROVE / 🔄 REVISE / ❌ REJECT
> **RF**: [RF Phase {X}](path-to-RF)
> **TS**: [TS Phase {X}](path-to-TS)

---

## 1. Review Checklist

| # | Check | Status | Notes |
|---|-------|--------|-------|
| 1 | DoD met? (all TS acceptance criteria) | ✅/❌ | {details} |
| 2 | Code quality (conventions, naming, type hints) | ✅/❌ | |
| 3 | Test coverage (tests written and passing) | ✅/❌ | |
| 4 | Philosophy aligned (matches HL design philosophy) | ✅/❌ | |
| 5 | Tech debt (shortcuts documented?) | ✅/❌ | |
| 6 | Security (no secrets exposed, guards in place) | ✅/❌/N/A | |
| 7 | Breaking changes (backward compat, migrations) | ✅/❌/N/A | |
| 8 | Style & standards (code style, conventions) | ✅/❌ | |
| 9 | Observations collected (executor reported findings) | ✅/❌ | |

## 2. Verdict

**{✅ APPROVE / 🔄 REVISE / ❌ REJECT}**

{Rationale for the verdict}

### If REVISE — items to fix:
1. {specific item to fix}

### If REJECT — fundamental issues:
1. {issue requiring HL/TS rework}

## 3. Tech Debt Collected

> **Source format**: Use reference patterns (compilable_contract.md §2).

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| 1 | RF observations | Low/Med/High | `file.py` | {description} | → backlog / → next phase |

## 4. Traces Updated

- [ ] README Task Board — status updated
- [ ] HL status — updated if phase completes
- [ ] PROJECT_CONFIG.yaml — initial_seq incremented if needed
- [ ] Other project files — checked for stale info
- [ ] tfw-docs: {Applied — updated Sections X, Y / N/A (minor)}
- [ ] tfw-knowledge: {Applied / N/A / Deferred to batch}

## 5. Fact Candidates

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

*REVIEW — {PREFIX}-{N} / Phase {X}: {Title} | YYYY-MM-DD*
