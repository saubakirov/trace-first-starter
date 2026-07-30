# EV — {PREFIX}-{N} / Phase {X}: {Title}

> **Date**: YYYY-MM-DD
> **Author**: {executor}
> **Task**: {PREFIX}-{N}
> **TS**: [TS Phase {X}](path-to-TS)

---

## Environment

> Capture the common verification environment. Fields marked "(if applicable)"
> may be omitted when irrelevant to the task type.

| Field | Value |
|-------|-------|
| OS | {e.g., Windows 11, Ubuntu 22.04, macOS 14} |
| Language / Runtime | {e.g., Python 3.12, Node 20} _(if applicable)_ |
| Database | {e.g., PostgreSQL 16, ClickHouse 24.3} _(if applicable)_ |
| Deploy target | {e.g., staging, localhost:3000, Vercel preview} _(if applicable)_ |
| CI / Pipeline | {e.g., GitHub Actions, local} _(if applicable)_ |

## Proof Record Index

> Create one-or-more stable `PR-*` records for every claimed deliverable. Local Proof is
> mandatory; add Seam/Live classes for every crossed/live boundary. Shared observations
> and grouped records are valid when each claim and boundary remains resolvable. A row,
> file, checkmark, or passing proxy proves only what the record directly relates.

| Proof Record | Claim / AC | Boundary and proof class | Method or observation | Actual result | Artifact / provenance | Actor / time _(when material)_ | Debt |
|--------------|------------|--------------------------|-----------------------|---------------|-----------------------|--------------------------------|------|
| PR-1 | {resolvable claimed deliverable / AC-N} | {Local; Seam: both sides + relation; Live: intended environment/event} | {reproducible Verification, source/interface comparison, or Evidence E#} | {what was and was not established} | {resolvable path, source/comparison, inline output, or E#} | {actor/time or N/A with reason} | None / VD-1 |

## Evidence

> One row per AC item. When a single verification covers multiple ACs,
> list them comma-separated in the AC column (e.g., "AC-3, AC-5").
> Use only the 4-status vocabulary: VERIFIED / DEFERRED / BLOCKED / N/A.
> Evidence means intended-environment observation, not synthetic Verification,
> source/interface comparison, or the Proof Record relation. Preserve these rows for
> RF §5 and downstream audit; status scopes only the row.

| # | AC | What was verified | Environment | Result | Artifact |
|---|----|--------------------|-------------|--------|----------|
| E1 | AC-{N} | {description of what was observed} | {specific environment detail if different from header} | {VERIFIED / DEFERRED / BLOCKED / N/A} | {file path in evidence/ or inline output} |

### Status Consequences

- `VERIFIED` — the intended real-world observation occurred and has resolvable
  artifact/provenance; it supports only the boundaries named by related `PR-*` records.
- `DEFERRED` — a named future event can produce the observation and a complete `VD-*`
  row records the explicit non-claim.
- `BLOCKED` — the observation cannot currently be obtained and no authorized safe
  due-event path supports closure; the affected claim cannot close.
- `N/A` — Evidence/live observation is not triggered, with a reason; Local Proof and
  any triggered Seam Proof remain required.

Missing artifact/provenance invalidates `VERIFIED`. Incomplete Value Debt invalidates
`DEFERRED`. An unjustified `N/A` or an Evidence status used as the entire claim,
attestation, or REVIEW status is invalid.

## Verdict

> Count only rows in §Evidence; Proof Record and Value Debt rows do not create a second
> status vocabulary.

Evidence verdict: {N}/{M} VERIFIED, {X} DEFERRED, {Y} BLOCKED, {Z} N/A

## Value Debt

> Required only when triggered Seam or Live Proof cannot yet exist. Every `DEFERRED`
> Evidence row must resolve to complete debt. If none: `No Value Debt.`

| Debt | Affected claim / Proof Record | Missing triggered proof | Owner | Due event | Evidence route | Impact and explicit non-claim | Closure condition |
|------|-------------------------------|-------------------------|-------|-----------|----------------|-------------------------------|-------------------|
| VD-1 | {AC-N / PR-*} | {Seam / Live boundary} | {named owner/authority} | {named future event} | {how observation will be obtained and preserved} | {what cannot be claimed now} | {what closes the debt} |

## Attachments

> Index of binary artifacts stored in this `evidence/` folder.
> If no binary artifacts exist: `No binary attachments.`

| File | Description |
|------|-------------|
| `{filename}` | {what it captures} |

---

> **File naming:**
> - Single-phase: `EV__{PREFIX}-{N}__{title}.md`
> - Multi-phase: `EV__phase-{x}__{title}.md`

*EV — {PREFIX}-{N} / Phase {X}: {Title} | YYYY-MM-DD*
