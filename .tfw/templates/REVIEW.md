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
- [ ] STEPS.md — closure entry added
- [ ] HL status — updated if phase completes
- [ ] PROJECT_CONFIG.yaml — initial_seq incremented if needed
- [ ] Other project files — checked for stale info

---

*REVIEW — {PREFIX}-{N} / Phase {X}: {Title} | YYYY-MM-DD*
