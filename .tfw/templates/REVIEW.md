# REVIEW — {ID} / Phase {X}: {Title}

> **Date**: YYYY-MM-DD
> **Author**: {reviewer}
> **Verdict**: ✅ APPROVE / 🔄 REVISE / ❌ REJECT
> **RF**: [RF Phase {X}](path-to-RF)
> **TS**: [TS Phase {X}](path-to-TS)
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`
> This file is a synthesis of stage findings. Reference stage files for raw evidence.

---

## 1. Map

{2-3 sentence summary of understanding: what was done, key decisions, scope}

## 2. Verify

| # | What was checked | Result | Evidence |
|---|-----------------|--------|----------|

> Raw verification log: see `review/verify.md`. If verification was limited: state what could NOT be verified.

## 3. Judge

> Ten rows, matching `review/judge.md` one-for-one and in the same order.
> `⚪ N/A` is permitted on any row and requires a stated reason — a skipped row is never a bare ✅.

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ✅/❌/⚪ | {specific} |
| 2 | Purpose Check — is this what we set out to do? + design soundness | ✅/❌/⚪ | |
| 3 | Debt disposed — every §5 row names one of the three, ruled by the coordinator, naming something that exists, with a consequence rather than a priority _(kept on consequence: the undisposed item is what filled the retired registry — 77 of its 121 rows open)_ | ✅/❌/⚪ | |
| 4 | Style & standards | ✅/❌/⚪ | |
| 5 | Observations collected | ✅/❌/⚪ | |
| 6 | RF completeness (§7-9 present) | ✅/❌/⚪ | |
| 7 | Evidence completeness — does it exist? | ✅/❌/⚪ | |
| 8 | Evidence sufficiency — does it establish the claim? | ✅/❌/⚪ | |
| 9 | Backward compatibility | ✅/❌/⚪ | |
| 10 | Safety | ✅/❌/⚪ | |

## 4. Verdict

**{✅ APPROVE / 🔄 REVISE / ❌ REJECT}**

{Rationale referencing §2 Verify and §3 Judge evidence}

### If REVISE — items to fix:
1. {specific item to fix}

### If REJECT — fundamental issues:
1. {issue requiring HL/TS rework}

> **If the ground is purpose** — finding `not fit for purpose`: quote the baseline or north-star clause
> the work fails to serve, name the concrete harm, and say plainly that the quality checks passed if they
> did. Routes to the owner, not back to the executor. If the reference set itself is inconsistent, record
> a **contract defect** with both conflicting clauses quoted — also to the owner.

## 5. Tech Debt Collected and Disposed

> The only place debt is written. The heading keeps the words `Tech Debt Collected` deliberately — every
> REVIEW file already written carries them, and the search below matches on them. There is no project
> registry: retired at 2.1.0, its rows sealed in `tasks/DEBT-SNAPSHOT.md`. **Source format**: reference
> patterns (compilable_contract.md §2).
>
> **Every row carries a disposition, and a disposition names something that already exists:**
> `paid — phase-{x}` · `promoted — {TASK-ID}` · `not material — {one-sentence ruling}`. Three outcomes and
> no fourth. A row awaiting a ruling is `pending — coordinator`, or `pending — owner` where the ruling is
> the owner's, and it keeps the task open until it becomes one of the three. `→ backlog` is not a
> disposition. The task does not reach `DONE` with a row undisposed.
>
> **The ruling states a consequence, or the named absence of one.** A bare priority — *"low"*, *"minor"*,
> *"can wait"* — names nothing and is inadmissible: a refusal that cannot later be shown wrong is a
> preference, not a decision. `not material` says **which question it answers**: *not owed*, where no
> consequence can be named; or *owed and forbidden to pay*, where a consequence follows and the fix is
> barred by a frozen acceptance criterion, by a DoF item or by a named cost — and the ruling cites that
> clause. Filing the second as the first makes the record say the reviewer thought it did not matter while
> they argued that it did.
>
> The reviewer marks and proposes. Acceptance authority over dispositions is the coordinator's
> (`conventions.md` §15), exercised once at the close of review (`review.md` Step 6).

| # | Source | Severity | File | Description | Disposition |
|---|--------|----------|------|-------------|-------------|
| 1 | RF observations | Low/Med/High | `file.py` | {description} | not material — not owed: {the consequence that will not follow} |

If nothing survived the quality filter: `No debt captured.`

**Every captured item across the project, with its disposition** — one search, no maintained file:

```bash
grep -rl --include='REVIEW*.md' 'Tech Debt Collected' workspace tasks |
xargs awk 'FNR==1{s=0} /^## .*Tech Debt Collected/{s=1;next} /^## /{s=0}
           s && /^\| / && !/^\| *(#|-)/ {sub(/^/, FILENAME": "); print}'
```

From the project root; substitute your `tfw.task_containers` for `workspace tasks`. Append
`| grep -iv 'not material'` for the items still owed. On this corpus, 2026-09-02: **253 rows**.

## 6. Traces Updated

- [ ] the task's `status.md` — `lifecycle` set per verdict, with a `transition` event in its `journal/`, named `{YYYYMMDD-HHMMSS}__{kind}__{token}.md`, with the time read from the clock
- [ ] HL status — updated if phase completes
- [ ] the task's `status.md` — `updated` reflects this review. No counter is incremented: identifiers are clock-derived and nothing allocates them
- [ ] §5 — no row left undisposed
- [ ] Other project files — checked for stale info
- [ ] tfw-docs: {Applied — updated Sections X, Y / N/A (minor)}
- [ ] tfw-knowledge: {Applied / N/A / Deferred to batch}

## 7. Fact Candidates

> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.
>
> **Scope:** Reviewer-observed project patterns discovered during the review process.
> Good: "18% clients = 80% revenue (Pareto)", "stakeholder: find problem clients first"
> NOT fact candidates: "project uses git", implementation details (→ Observations → tfw-docs),
> or reviewer analysis/opinions (those belong in §4 Verdict rationale).
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

> **Categories** (open list): `environment`, `process`, `stakeholder`, `constraint`, `convention`, `domain`, `context`, `risk`, `philosophy`

---

*REVIEW — {ID} / Phase {X}: {Title} | YYYY-MM-DD*
