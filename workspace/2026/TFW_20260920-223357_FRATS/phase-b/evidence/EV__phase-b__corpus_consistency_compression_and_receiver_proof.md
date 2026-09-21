# EV — TFW_20260920-223357_FRATS / Phase B: Corpus Consistency, Compression and Receiver Proof

> **Current filename**: `evidence/EV__phase-b__corpus_consistency_compression_and_receiver_proof.md`; later rounds append to this file.
> **Date**: 2026-09-21
> **Author**: `saubakirov`, via Codex Executor
> **Task**: `TFW_20260920-223357_FRATS`
> **TS**: [Phase B TS](../TS__phase-b__corpus_consistency_compression_and_receiver_proof.md)

---

## Environment

| Field | Value |
|---|---|
| OS | Windows, PowerShell |
| Language / Runtime | Python 3.13.5; Git 2.42.0.windows.1; ripgrep 14.1.0; pytest 9.0.2 |
| Database | N/A |
| Deploy target | N/A — framework source and read-only local receiver replay |
| CI / Pipeline | Local immutable-ref and Candidate verification |

## Evidence

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1 | AC-1 | Historical RCFR audit reproduced 310,485→112,206 and 66,436→32,088 at its immutable Candidate; the separate ten-command successor measured Phase B Baseline 114,221/37,818 and Candidate 113,405/37,061 with selector, bridge and limits recorded. | Python 3.13.5; Git trees; historical detached worktree removed after verification | VERIFIED | [`current-corpus-and-exposure.txt`](current-corpus-and-exposure.txt) |
| E2 | AC-2 | All 47 VALUE paths have normative owner, reader/delivery and one disposition; F1–F11 close every detected contradiction, stale reference, duplicate or readerless bound; current and historical filename fixtures pass. | Baseline/Candidate source census | VERIFIED | [`instruction-disposition-ledger.md`](instruction-disposition-ledger.md) |
| E3 | AC-3 | C1–C5 map every consolidation across six edges; each edge has one positive and one output-changing negative replay; resolved old oracle projections stayed equal and disclosed skipped anchors are not claimed. | Exact Git trees; source-derived clauses; real lifecycle/event validator where applicable | VERIFIED | [`six-edge-replay.md`](six-edge-replay.md) |
| E4 | AC-4 | Shared rules have one owner, workflows are role-local, templates are structural, generated copies are delivery only; no new runtime, registry, backlog, mandatory artifact or restored oracle exists. Gross/net size is reported but did not select edits. | Candidate source and ledger | VERIFIED | [`instruction-disposition-ledger.md`](instruction-disposition-ledger.md), [`adapter-and-suite.txt`](adapter-and-suite.txt) |
| E5 | AC-5 | Ten canonical workflows equal all 20 Claude/Antigravity copies; Codex/Claude managed blocks and Antigravity target equal sources; Cursor absence is bounded; Update/Init/Config share the manifest and preserve provider limits. | Candidate Git blobs and SHA-256 managed-block comparison | VERIFIED | [`adapter-and-suite.txt`](adapter-and-suite.txt) |
| E6 | AC-6 | Four receiver start/end snapshots match on HEAD, branch, status count and status hash; proposed behavior was replayed without writes and local customizations/older versions bound every conclusion. | 2026-09-21T14:06:17.5456556Z–14:06:19.3562146Z; four local repos | VERIFIED | [`receiver-replay.md`](receiver-replay.md) |
| E7 | AC-7 | Required suite passed 14/14; command-entry dry-run was valid for 18 schedules; diff check passed; no ASSURANCE or receiver path changed; accounting reproduced the literal selector. | Candidate; pytest 9.0.2; local dry-run | VERIFIED | [`adapter-and-suite.txt`](adapter-and-suite.txt) |
| E8 | AC-8 | RF presents the two non-equal metric series, behavior benefit/cost/limits, receiver result, exact D75 replacement text/citations and the post-review `/tfw-docs` route without editing `KNOWLEDGE.md`. | Executor RF at Candidate/evidence epoch | VERIFIED | [`../RF__phase-b__corpus_consistency_compression_and_receiver_proof.md`](../RF__phase-b__corpus_consistency_compression_and_receiver_proof.md) |
| E9 | AC-9 | Executor produced one tested final Candidate, EV and RF with exact lineage. Independent Reviewer verdict, accepted docs effect/follow-up and terminal Coordinator closure necessarily occur after this RF. | Executor unit `codex:thread:local:01a0c415-c362-78b3-98e9-00d728c5ac18` | DEFERRED | Required next route: independent `/tfw-review`; exact missing outputs are REVIEW, any accepted `/tfw-docs` effect and terminal journal. |
| E-accounting | AC-7 | TS approval `8c02d42375c3838ff62586bf5221b63f46d78446`; Baseline `1a9209530d7a939db1270e2f91dcef40a9f449e6`; Candidate `fd0655ce17f2c650d238622c1d6a57ec5dd9a204`; literal 47-path selector; 39 modified + 8 zero-diff; 365 + 507 = 872 touched text LOC; all text, binary/N/A none; no membership deviation; no threshold crossing; immutable 47/4,800 denominator approved before work; NUL-safe commands unchanged. | Repository, Git 2.42.0; exact refs | VERIFIED | [`adapter-and-suite.txt`](adapter-and-suite.txt) exact per-path table and reproduction commands |

`E-accounting` reproduces the approved TS selector. It does not define one, move Candidate, ratchet
the denominator or supply late authority.

## Verdict

Evidence verdict: 9/10 VERIFIED, 1 DEFERRED, 0 BLOCKED, 0 N/A.

The single deferred row is the intentionally downstream independent-acceptance/terminal-lineage
portion of AC-9. It is not an Executor implementation failure and must not be relabeled VERIFIED
until the independent Reviewer and Coordinator produce the named records.

---

*EV — TFW_20260920-223357_FRATS / Phase B: Corpus Consistency, Compression and Receiver Proof | 2026-09-21*
