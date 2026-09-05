# REVIEW — {ID} / Phase {X}: {Title}

> **Date**: YYYY-MM-DD
> **Author**: {reviewer}
> **Verdict**: ✅ APPROVE / 🔄 REVISE / ❌ REJECT
> **RF**: [RF Phase {X}](path-to-RF)
> **TS**: [TS Phase {X}](path-to-TS)
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`

---

## 1. Map

{Result, decisions, scope in 2–3 sentences.}

## 2. Verify

| # | What was checked | Result | Evidence |
|---|---|---|---|
| V-accounting | Independent value-bearing replay | {VERIFIED/BLOCKED/N/A/INVALID} | Approval ref; full Baseline/Candidate; literal VALUE membership/rename identity; adds/deletes/touched LOC; binary N/A; trigger; authority/timing; exact command |

Resolve the approved TS and rerun its method. Candidate is the first tested Executor implementation commit
before traces. Excluded-only later writes do not move it; later VALUE requires a new Candidate. Reuse the
immutable denominator and pre-work authority. Missing/mutable/mismatched/late is BLOCKED; metric-only N/A;
unresolved phase attribution INVALID; DEFERRED is non-terminal. Cite the accounting AC on discrepancy;
REVIEW never repairs the record or invents a total.

> Raw log: `review/verify.md`. State every verification limit.

## 3. Judge

Use the ten `review/judge.md` rows in this order; every N/A needs a reason.

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | DoD / all TS AC | ✅/❌/⚪ | {specific} |
| 2 | Purpose and design | ✅/❌/⚪ | {specific} |
| 3 | Debt disposed by consequence | ✅/❌/⚪ | {specific} |
| 4 | Style and standards | ✅/❌/⚪ | {specific} |
| 5 | Observations collected | ✅/❌/⚪ | {specific} |
| 6 | RF §7–§9 complete | ✅/❌/⚪ | {specific} |
| 7 | Evidence exists | ✅/❌/⚪ | {specific} |
| 8 | Evidence is sufficient | ✅/❌/⚪ | {specific} |
| 9 | Backward compatibility | ✅/❌/⚪ | {specific} |
| 10 | Safety | ✅/❌/⚪ | {specific} |

## 4. Verdict

**{✅ APPROVE / 🔄 REVISE / ❌ REJECT}**

{Rationale citing §2/§3 evidence.}

### If REVISE — proposals to coordinator

1. {item} — **basis:** {breached TS AC or frozen HL claim}

### If REJECT — fundamental issues

1. {issue requiring HL/TS rework}

Purpose failure quotes the baseline/North-Star clause, concrete harm, and passing quality checks; route it
to Owner. Conflicting references are a contract defect quoting both clauses.

## 5. Tech Debt Collected and Disposed

Write debt only here. Each row is `paid — phase-{x}`, `promoted — {TASK-ID}`, or
`not material — {consequence ruling}`. Pending Coordinator/Owner rulings keep the task open. A bare priority
or `→ backlog` is invalid.

| # | Source | Severity | File | Description | Disposition |
|---|---|---|---|---|---|
| 1 | {source} | Low/Med/High | `file` | {issue} | {terminal disposition} |

If empty: `No debt captured.` Project-wide discovery:

```bash
grep -rl --include='REVIEW*.md' 'Tech Debt Collected' workspace tasks |
xargs awk 'FNR==1{s=0} /^## .*Tech Debt Collected/{s=1;next} /^## /{s=0}
           s && /^\| / && !/^\| *(#|-)/ {sub(/^/, FILENAME": "); print}'
```

Use configured containers; append `| grep -iv 'not material'` for owed items.

## 6. Traces Updated

- [ ] task status lifecycle/outcome/updated and one timestamped transition event
- [ ] HL status if phase completes; §5 has no pending row
- [ ] stale project files checked
- [ ] tfw-docs: {Applied / N/A}
- [ ] tfw-knowledge: {Applied / N/A / Deferred}

## 7. Fact Candidates

| # | Category | Human-sourced candidate | Source | Confidence |
|---|---|---|---|---|
| 1 | {category} | {fact} | {conversation reference} | High/Medium/Low |

If empty: `No fact candidates.`

---

*REVIEW — {ID} / Phase {X}: {Title} | YYYY-MM-DD*
