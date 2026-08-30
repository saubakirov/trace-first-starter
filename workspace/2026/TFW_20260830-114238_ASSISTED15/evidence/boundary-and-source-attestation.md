# Boundary and source attestation — TFW_20260830-114238_ASSISTED15

> **Date:** 2026-08-30
> **Actor:** saubakirov via Codex Executor
> **Mode:** local verification; approved field source read-only

## Product boundary

- Baseline: `f3eb986`.
- The post-commit run independently enumerated all 20 Assisted commits through terminal evidence `640fad5`: zero changes to `.tfw`, root guides, `KNOWLEDGE.md`, `TECH_DEBT.md`, or `editions/01-light`. `640fad5` is in no remote-tracking ref or tag. This attestation-only follow-up is an exact staged set of five task-local RF/evidence files with zero forbidden paths by construction; it is rechecked after commit before handoff.
- The shared branch has concurrent forbidden-path changes under `.tfw/`; `boundary-summary.json` lists every current global path and classifies them as **external dirty/commits outside the Assisted task**. They are retained and explicitly not claimed as Assisted changes.
- The `editions/` product delta is exactly 35 paths: 25 added, 7 modified, 3 deleted.
- The product delta is 3,257 added plus 778 removed lines, 4,035 changed lines total; the TS ceiling is 4,800.
- The three deleted paths are exactly the retired stock hook paths. Their baseline bytes match the three accepted retirement hashes in `maintenance-policy.json`; no neighboring `.codex` path is classified for retirement.
- Product private-marker scan returned zero matches. `VERSION` is exactly `1.5\n`; the changelog records public `1.5 - Unreleased` and the public repository `1.0` baseline only.
- Task-scoped forbidden-path, current-global concurrency and product-diff checks are resolvable in `assisted15-verification.log` and `boundary-summary.json`.

## Read-only field source

The approved 29-file field tree was only enumerated and hashed. No field file was executed, written, renamed, deleted, touched by a renderer, or used as an update target.

Two aggregate digests are retained because the same 29 `(relative path, byte size, SHA-256)` rows sort Unicode paths differently:

| Reading | Algorithm | Before | After |
|---|---|---|---|
| Historical research pin | PowerShell culture-sort of `path<TAB>size<TAB>sha256<LF>` | `7e2248a7f7e77161644d8394b1557c731e0b5b31d7713843de30655b6e4fadc3` | same |
| Canonical execution evidence | UTF-8 POSIX path, Python code-point sort of the same records | `3a1885c65b13388a51ddaa5b1454122876d4f17d268bc49f0f94f6bb2dbee96b` | same |

The complete 29-row sets were equal across PowerShell and Python before execution, equal across both readers afterward, and byte-identical pre/post. Therefore the aggregate difference is ordering-only and not source drift.

The Executor stopped twice before fixture execution when the ordering distinction had not yet been classified. Those fail-closed aborts are retained in `source-immutability.json`; the Coordinator established row-set equality and authorized resumption without changing source authority or the approved contract.

The real mixed field tree was treated only as P6 comparison evidence. The retained public facts are limited to generic capability-presence booleans; no field payload, organization fact, person, identifier, path, history, logo, or exact private operation was projected into the product.

## Direction and publication audit

- P2 public-to-downstream ran only against isolated Git-baseline copies populated with synthetic work, knowledge, profile, project, customization, unrelated `.codex`, and separate Full-namespace state. The operation carried `maintenance/release-manifest.json` as its own journaled release record, reached `1.5`, passed `verify-release`, retired only the three stock hooks, preserved every protected byte, and ended `verified` with zero unexplained changes. A clean installed target then passed as the next source.
- The project lock is a stable private target-keyed path outside source, target and operation directories. A retained REAL two-process fixture gave two same-target operations the same lock key; the loser stopped before its operation directory and made zero target/product writes, while a different target independently reached `verified`.
- Actual Windows identity evidence reprobed the pinned full namespace chain and private owner/ACL state before the first registry read or lock probe. Instrumented namespace substitution at that boundary caused zero substituted reads and zero registry writes; all successful registry reads remained inside validated locality and the live OS lock.
- Reverse flow accepted two canonical create-once verified terminal reports with matching neighboring journals, exact outside-root approval and pinned provenance. Different operation IDs/counts emitted byte-identical candidate projections/public IDs. Fabricated provenance and a candidate under public core both rejected at zero writes.
- No tag contains product commits `957c70f`, `c6f1b0f`, `ca1ef26`, `b37f7a3`, or `afef18a`. No push, tag creation, or remote publication command was executed.

Detailed machine-readable evidence: `assisted15-fixture-results.json`, `source-immutability.json`, `identity-windows.json`, `maintenance/`, and `templates/render-summary.json`.
