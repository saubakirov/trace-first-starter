# REVIEW — {PREFIX}-{N} / Phase {X}: {Title}

> **Дата**: YYYY-MM-DD
> **Автор**: {coordinator}
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

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| 1 | RF observations | Low/Med/High | `file.py` | {description} | → backlog / → next phase |

## 4. Traces Updated

- [ ] README Task Board — status updated
- [ ] HL status — updated if phase completes
- [ ] PROJECT_CONFIG.yaml — initial_seq incremented if needed
- [ ] Other project files — checked for stale info
- [ ] tfw-docs: {Applied — updated Sections X, Y / N/A (minor)}

## 5. Fact Candidates

> Record what you learned about this project that would change how the NEXT agent
> approaches a similar task. If it wouldn't change their decision — don't record it.
>
> Anti-patterns: "project uses git", "code is in Python", "tests exist"
> These are NOT verified facts. They become facts after `/tfw-knowledge` consolidation.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | {category} | {what you learned} | {where from} | High/Medium/Low |

> **Categories** (open list): `environment`, `process`, `stakeholder`, `constraint`, `convention`, `domain`, `context`, `risk`

---

*REVIEW — {PREFIX}-{N} / Phase {X}: {Title} | YYYY-MM-DD*
