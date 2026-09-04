# EV — {ID} / Phase {X}: {Title}

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

Use only VERIFIED / DEFERRED / BLOCKED / N/A. Give VERIFIED a resolving artifact and explain every other
result. Combine ACs only when one check resolves them.

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1 | AC-{N} | {observed result} | {specific environment} | {VERIFIED/DEFERRED/BLOCKED/N/A} | {path or inline output} |
| E-accounting | {accounting AC} | Exactly one row: approval ref; full Baseline/Candidate; selector and path/action/class/reason membership; phase-attribution detail including INVALID when unresolved; logical files; additions + deletions = touched LOC; binary/non-text N/A; trigger disposition; immutable-denominator authority/timing; exact NUL-safe method | {repo/Git/runtime} | {VERIFIED/DEFERRED/BLOCKED/N/A} | {command and result} |

`E-accounting` reproduces the approved TS selector. It cannot define one, move Candidate, ratchet the
denominator, or supply late authority.

## Verdict

Evidence verdict: {N}/{M} VERIFIED, {X} DEFERRED, {Y} BLOCKED, {Z} N/A

## Attachments

| File | Description |
|---|---|
| `{filename}` | {binary artifact; omit section when none} |

> Names: single-phase `EV__{ID}.md`; multi-phase `EV__phase-{x}__{title}.md`.

---

*EV — {ID} / Phase {X}: {Title} | YYYY-MM-DD*
