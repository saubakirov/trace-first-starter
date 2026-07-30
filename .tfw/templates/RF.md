# RF — {PREFIX}-{N} / Phase {X}: {Title}

> **Date**: YYYY-MM-DD
> **Author**: {author}
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-{PREFIX}-{N}](path-to-HL)
> **TS**: [TS Phase {X}](path-to-TS)
> **Executor Attestation**: This RF states only what the Executor can support from the
> cited Proof Records and disclosed limitations. Independent REVIEW retains
> acceptance/rejection authority.

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

## 2. Key Decisions and Material Deviations

1. {Decision and rationale}
2. {Decision and rationale}

### Material Deviations

> Record every departure that can affect a Requirement Claim or its proof. An
> acceptance-critical or scope mismatch requires Coordinator/user authority and cannot
> be normalized here. If none: `No material deviations.`

| # | Source requirement or guidance | Actual choice | Rationale | Affected claim / Proof Record | Authority |
|---|--------------------------------|---------------|-----------|-------------------------------|-----------|
| D1 | {TS/HL/source reference; acceptance-critical or adaptable} | {deviation} | {why} | {AC / PR-* and impact} | {approval or MAY-deviate boundary} |

### Transition and Removal Classification

> For contract/framework changes, classify removed or replaced behavior. Omit when no
> semantic removal occurred.

| # | Former behavior/content | Classification | Current owner or stronger relation |
|---|-------------------------|----------------|------------------------------------|
| R1 | {removed wording/branch} | Obsolete / Moved to owner-reference / Replaced by precise term / Covered by stronger structural relation | {owner/reference} |

## 3. Acceptance Criteria and Executor Attestation

> A checked AC means only that the Executor supports the stated deliverable within its
> named boundary from the cited Proof Records. It cannot coexist with unresolved
> blocking proof. Supported local work may coexist with explicit Seam/Live Value Debt,
> but that deferred boundary remains a non-claim.

| AC | Claimed deliverable and Executor statement | Proof Record(s) | Limitations, Value Debt, or blocked condition | Result |
|----|--------------------------------------------|-----------------|----------------------------------------------|--------|
| AC-{N} | {what is supported within what boundary} | {PR-*} | {None / limitation / VD-* / blocking condition} | [x] / [ ] |

## 4. Verification

> Report only applicable checks. Each row names the claim/failure protected, a
> reproducible command or method, the actual result, and related Proof Records.
> `N/A` requires a claim-based reason; a passing proxy does not widen the boundary.

| # | Claim / failure protected | Command or method | Actual result | Proof Record(s) |
|---|---------------------------|-------------------|---------------|-----------------|
| V1 | {claim or failure} | `{command}` / {method} | {result, count, or N/A with reason} | {PR-*} |

### Descriptive Measurements

> Use one reproducible counting method for all before/after values. Measurements are
> scope observations, not completion or quality evidence.

| Measurement | Before | After | Delta | Method / provenance |
|-------------|-------:|------:|------:|---------------------|
| Lines | {N} | {N} | {±N} | {one method} |
| Words/tokens | {N} | {N} | {±N} | {one method} |
| Branches/decision points | {N} | {N} | {±N} | {one method} |
| Consumers | {N} | {N} | {±N} | {exact write-set method} |

## 5. Evidence

> **Cognitive mode:** Observational verification — Evidence rows and the Proof Record
> index live in EV, not inline. RF §5 is a summary pointer, not proof by presence.

See [EV file](evidence/EV__{PREFIX}-{N}__{title}.md) for evidence details.

Evidence verdict: {N}/{M} VERIFIED, {X} DEFERRED, {Y} BLOCKED, {Z} N/A

{One-sentence Evidence limitation or `No Evidence limitations beyond those stated in
the linked EV and §3.`}

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `path/to/file` | {lines} | {type} | {description} |

> **Types:** `dead-code`, `naming`, `todo`, `duplication`, `perf`, `security`, `style`, `missing-test`, `ux`
>
> **Quality bar**: report only issues that would bite the next developer. Don't generate observations just because the section exists.
> If nothing found: `No observations.`

## 7. Fact Candidates

> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.
>
> **Scope:** Agent-observed project patterns discovered during execution.
> Good: "18% clients = 80% revenue (Pareto)", "stakeholder: find problem clients first"
> NOT fact candidates: "project uses git", implementation details (→ §6 Observations → tfw-docs),
> or agent-generated analysis (→ §8 Strategic Insights).
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

## 8. Strategic Insights (Execution)

> **Cognitive mode:** Deep analytical synthesis. Capture human-sourced domain knowledge
> observed during execution, then ADD implications — what does this insight mean for the project?
>
> **Human-Only Test:** Would this insight be unknown without the user saying it?
> If an agent can discover it by reading code — it's NOT a strategic insight, it's a Fact Candidate (§7).
>
> **When to fill:** Only when the human provides domain knowledge, corrections, or strategic
> context DURING execution. If no human interaction occurred — write "No strategic insights."
>
> **Categories:** conventions.md §10.1.

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | {insight} | {category — see §10.1} | User, {context} |

> **Source format**: Use reference patterns (e.g., `RF TFW-18`, `D24`). See compilable_contract.md §2.

## 9. Diagrams

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
