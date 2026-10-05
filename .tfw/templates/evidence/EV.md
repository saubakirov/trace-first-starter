# EV — {ID} / Phase {X}: {Title}

> **Current filename**: `evidence/EV__{ID}.md` or `evidence/EV__phase-{x}__{phase_slug}.md`; later rounds append to this file. Derive under `conventions.md` → `Artifact file naming`.

> **Date**: YYYY-MM-DD
> **Author**: {executor}
> **Task**: {ID}
> **TS**: [TS Phase {X}](path-to-TS)

---

## Environment

| Field | Value |
|---|---|
| OS | {OS/version} |
| Language / Runtime | {runtime/version or N/A} |
| Database | {version or N/A} |
| Deploy target | {target or N/A} |
| CI / Pipeline | {pipeline or local} |

## Evidence

Use only VERIFIED / DEFERRED / BLOCKED / N/A, and explain every result other than VERIFIED.
Combine ACs only when one check resolves them. A claim that cannot be repeated is attested: its row
says why, how its values were captured and what the Reviewer checks instead.

In the row, identify the claim's relevant input/output,
oracle or authority and environment assumptions only as needed to judge reuse. An enclosing commit
or record-only edit is not blanket invalidation or blanket PASS. Changed dependencies or uncertain
coverage require affected evidence. Preserve earlier rows; append later final-output observations
and their independent judgment references instead of relabeling the earlier epoch.

| # | AC | Verified | How | Observed | Result |
|---|---|---|---|---|---|
| E1 | AC-{N} | {claim checked} | {command or action; Candidate or target; environment} | {deciding values, not raw output} | {VERIFIED/DEFERRED/BLOCKED/N/A} |
| E-accounting | {accounting AC} | Exactly one row: approval ref; full Baseline/Candidate; selector and path/action/class/reason membership; phase-attribution detail including INVALID when unresolved; logical files; additions + deletions = touched LOC; binary/non-text N/A; trigger disposition; immutable-denominator authority/timing; exact NUL-safe method | {command; repo/Git/runtime} | {numbers} | {VERIFIED/DEFERRED/BLOCKED/N/A} |

`E-accounting` reproduces the approved TS selector. It cannot define one, move Candidate, ratchet the
denominator, or supply late authority.

## Verdict

Evidence verdict: {N}/{M} VERIFIED, {X} DEFERRED, {Y} BLOCKED, {Z} N/A

---

*EV — {ID} / Phase {X}: {Title} | YYYY-MM-DD*
