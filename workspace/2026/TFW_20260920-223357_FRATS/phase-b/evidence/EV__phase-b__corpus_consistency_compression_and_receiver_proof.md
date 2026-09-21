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

---

## Return Round 1 — Replacement Evidence

Earlier rows remain the rejected Candidate epoch and are not relabeled. The rows below supersede
their active claims where Candidate, word-bound, validator-path, provider-limit or accounting inputs
changed. Independent judgment of these rows is still owed.

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1-R1 | AC-1 | Identical successor method measured replacement Candidate 107,850 trajectory and 31,813 unique corpus from Baseline 114,221/37,818; historical series/bridge remain separate. | Immutable Git trees; Python 3.13.5 | VERIFIED | [`current-corpus-and-exposure.txt`](current-corpus-and-exposure.txt) Return Round 1 |
| E2-R1 | AC-2 | F12–F15 close the four previously missing workflow-bound contradictions; exact Candidate word counts are Plan 923, Handoff 937, Review 998, Update 988 and all ten canonical workflows are ≤1,200. | Candidate Git blobs; `\S+` oracle | VERIFIED | [`instruction-disposition-ledger.md`](instruction-disposition-ledger.md), [`adapter-and-suite.txt`](adapter-and-suite.txt) |
| E3-R1 | AC-3 | Six positive and six material-negative cases pass/reject from exact Candidate objects; real authority/recovery calls load existing `tools/tfw_state.py` and emit the recorded diagnostics. | Candidate Git objects; Python 3.13.5 | VERIFIED | [`rung1-semantic-replay.txt`](rung1-semantic-replay.txt), [`six-edge-replay.md`](six-edge-replay.md) |
| E4-R1 | AC-4 | Returned workflows meet the active bound through explicit consolidation dispositions while preserving all six carriers; no new runtime, registry, artifact class or exception was created. | Candidate source/ledger | VERIFIED | [`instruction-disposition-ledger.md`](instruction-disposition-ledger.md) F12–F15; [`rung1-semantic-replay.txt`](rung1-semantic-replay.txt) |
| E5-R1 | AC-5 | All ten canonical workflow blobs equal all 20 projections. Accepted Phase A bounds are Codex P2/partial P3, authenticated Claude P2, Antigravity P2/partial P3; no full P3/P4 or reliability rate is claimed. | Candidate Git blobs; accepted Phase A RF/REVIEW | VERIFIED | [`adapter-and-suite.txt`](adapter-and-suite.txt); [`../../phase-a/RF__phase-a__explicit_coordination_gateway_and_session_identity.md`](../../phase-a/RF__phase-a__explicit_coordination_gateway_and_session_identity.md); [`../../phase-a/REVIEW__phase-a__explicit_coordination_gateway_and_session_identity.md`](../../phase-a/REVIEW__phase-a__explicit_coordination_gateway_and_session_identity.md) |
| E6-R1 | AC-6 | R1–R3 do not read or write receiver trees; Coordinator R5 makes the original matched receiver epoch terminal not-owed. Its immutable evidence remains applicable to the unchanged receiver claim. | Recorded Round-0 epoch plus ruled REVIEW R5 | VERIFIED | [`receiver-replay.md`](receiver-replay.md); [`../REVIEW__phase-b__corpus_consistency_compression_and_receiver_proof.md`](../REVIEW__phase-b__corpus_consistency_compression_and_receiver_proof.md) §8 R5 |
| E7-R1 | AC-7 | Replacement Candidate: 14 collected, 14 passed; command-entry dry-run errors=[]/valid=true/18; 20/20 copy parity; exact final accounting reproduced. | Candidate; pytest 9.0.2; local dry-run | VERIFIED | [`adapter-and-suite.txt`](adapter-and-suite.txt) Return Round 1 |
| E8-R1 | AC-8 | Appended RF presents replacement Candidate, final counts/metrics, corrected provider bounds and unchanged exact D75 post-APPROVE route. | Executor Return Round 1 | VERIFIED | [`../RF__phase-b__corpus_consistency_compression_and_receiver_proof.md`](../RF__phase-b__corpus_consistency_compression_and_receiver_proof.md) Return Round 1 |
| E9-R1 | AC-9 | Same Executor produced tested replacement Candidate and appended evidence/RF under the ruled rung-1 bound. Same independent Reviewer verdict, post-APPROVE docs effect/follow-up and terminal Coordinator lineage remain downstream. | Executor unit and immutable refs | DEFERRED | Required next route: same independent `/tfw-review`; then ruled R4/closing sequence only after APPROVE. |
| E-accounting-R1 | AC-7 | TS approval `8c02d42375c3838ff62586bf5221b63f46d78446`; ruling `44f9a6135293a3a68af7a537a4875d722f25d5bf`; Baseline `1a9209530d7a939db1270e2f91dcef40a9f449e6`; Candidate `50ed7fb8c09cfc32e67623848b0551f9ada881da`; literal 47 VALUE paths; 39 modified + 8 zero-diff; 1,283 + 2,823 = 4,106 touched text LOC; net −1,540; no rename/binary/membership deviation; other changed paths are prior governing/TRACE history; below prompts/ceiling; immutable 47/4,800 approval predates work; exact NUL-safe method unchanged. | Repository; Git 2.42.0; exact refs | VERIFIED | [`adapter-and-suite.txt`](adapter-and-suite.txt) final 47-row table and reproduction method |

`E-accounting-R1` is the sole accounting row for the replacement Candidate epoch. It does not move
Candidate, redefine selector, ratchet denominator or provide late authority.

### Return Round 1 Verdict

Replacement evidence verdict: 9/10 VERIFIED, 1 DEFERRED, 0 BLOCKED, 0 N/A.

The only deferred row is the deliberately downstream independent acceptance/docs follow-up/terminal
lineage portion of AC-9. The independent Reviewer must confirm or revise this Executor verdict.

---

## Return Round 2 — Revision 2 and Transcript-Isolation Evidence

Earlier rows remain their historical Candidate epochs. The rows below are the sole active evidence
set for Candidate `93186cea9ac8209cade30a49e76f3b8a32ae6227`; they incorporate the owner-approved
revision 2 and the prospective REVIEW §10 necessary constituent.

| # | AC | What was verified | Environment | Result | Artifact |
|---|---|---|---|---|---|
| E1-R2 | AC-1 | Identical successor selector measured 114,221→110,512 trajectory (−3,709; −3.2472%) and 37,818→33,220 unique corpus (−4,598; −12.1582%); the historical 112,206/32,088 series and bridge remain separate. | Exact Baseline/Candidate Git trees; Python 3.13.5 | VERIFIED | [`current-corpus-and-exposure.txt`](current-corpus-and-exposure.txt) Return Round 2 |
| E2-R2 | AC-2 | F16–F19 close the revision-2 and transcript-observation findings with one canonical owner and actual readers; the cumulative F1–F19 census has no undispositioned active-source finding. | Approved TS, prospective ruling and Candidate blobs | VERIFIED | [`instruction-disposition-ledger.md`](instruction-disposition-ledger.md) Return Round 2/3 |
| E3-R2 | AC-3 | Exact-source entry/continuation/GATEWAY/provider and transcript-isolation scenarios pass. Bounded wait/status/one request/returned artifacts are allowed; transcript, reasoning, tool-output, terminal, unreturned-tree and session-inspection variants refuse. | Named Git objects only; no role transcript input | VERIFIED | [`rung2-semantic-replay.txt`](rung2-semantic-replay.txt), [`six-edge-replay.md`](six-edge-replay.md) |
| E4-R2 | AC-4 | All ten canonical workflows are ≤1,400 words; semantic additions are ruled owner text or necessary safety, not filler. No runtime, registry, workflow, command, artifact class, permanent test or exception was added. | Candidate source and ledger | VERIFIED | [`adapter-and-suite.txt`](adapter-and-suite.txt), [`instruction-disposition-ledger.md`](instruction-disposition-ledger.md) |
| E5-R2 | AC-5 | Ten canonical workflows equal all 20 projections; Codex/Claude managed blocks and Antigravity full target equal sources; provider limits remain Codex P2/partial P3, authenticated Claude P2, Antigravity P2/partial P3, with no full P3/P4 or reliability rate. | Candidate Git blobs; accepted Phase A RF/REVIEW | VERIFIED | [`adapter-and-suite.txt`](adapter-and-suite.txt) Return Round 2 |
| E6-R2 | AC-6 | Four receiver start/end snapshots match on resolved path, HEAD, branch, status count and status hash at a new declared epoch; no receiver write, install or normalization occurred. | 2026-09-21T20:44:44.4264548Z–20:44:45.9853790Z; four local repos | VERIFIED | [`receiver-replay.md`](receiver-replay.md) Revision-2/final-Candidate epoch |
| E7-R2 | AC-7 | Candidate passes 14/14 tests, 54-schedule dry-run, diff check, 20/20 copy parity, 84/84 relative-link checks, active-heading search and exact immutable accounting. | Python 3.13.5; pytest 9.0.2; Git 2.42.0 | VERIFIED | [`adapter-and-suite.txt`](adapter-and-suite.txt) Return Round 2 |
| E8-R2 | AC-8 | RF reports final metrics, gross/net accounting, owner-visible behavior, limitations and the unchanged exact D75 post-APPROVE `/tfw-docs` route without editing `KNOWLEDGE.md`. | Executor RF at final Candidate epoch | VERIFIED | [`../RF__phase-b__corpus_consistency_compression_and_receiver_proof.md`](../RF__phase-b__corpus_consistency_compression_and_receiver_proof.md) Return Round 2 |
| E9-R2 | AC-9 | Same Executor produced one tested descendant Candidate and appended EV/RF under revision 2 plus the prospective necessary constituent. Independent verdict, accepted D75 docs effect/follow-up and terminal Coordinator lineage remain downstream by design. | Executor unit `codex:thread:local:01a0c415-c362-78b3-98e9-00d728c5ac18` | DEFERRED | Required next route: same independent `/tfw-review`; after APPROVE only, ruled docs/follow-up/closure sequence. |
| E10-R2 | AC-10 | Canonical Plan contains the exact Strategic Architect mindset and nine planning steps, retains the answered post-approval dispatch paragraph, reads Coordination and is 1,370 words; both projections are exact. | TS approval object and Candidate Git blobs | VERIFIED | [`rung2-semantic-replay.txt`](rung2-semantic-replay.txt), [`adapter-and-suite.txt`](adapter-and-suite.txt) |
| E11-R2 | AC-11 | Exact Phase/Step/Stage/Gate glossary and Design Rules text resolve; operational headings and references are normalized; all workflows remain ≤1,400; changed VALUE Markdown has 84 checked links and zero missing. | Candidate Git blobs and static link/heading audit | VERIFIED | [`rung2-semantic-replay.txt`](rung2-semantic-replay.txt), [`adapter-and-suite.txt`](adapter-and-suite.txt) |
| E12-R2 | AC-12 | Seven provider source/target paths disclose the four capabilities honestly and carry the bounded transcript-isolation mapping. Codex refuses `read_thread`/`includeOutputs` monitoring; other providers refuse opening/resuming another role session; silence routes through wait/status or one addressed request. | Candidate Git blobs; exact-source replay | VERIFIED | [`rung2-semantic-replay.txt`](rung2-semantic-replay.txt), [`adapter-and-suite.txt`](adapter-and-suite.txt) |
| E-accounting-R2 | AC-7 | Revision-2 approval `116a324bb38d5ca21094bf6c5d528620d4ec4121`; prospective necessary-constituent ruling `68d85cc20b285e2dce083d23519d3394056033f4`; Baseline `1a9209530d7a939db1270e2f91dcef40a9f449e6`; Candidate `93186cea9ac8209cade30a49e76f3b8a32ae6227`; literal 47 VALUE paths with approved classes/reasons; 46 modified + 1 zero-diff; 1,675 + 2,982 = 4,657 touched text LOC; net −1,307; no binary/rename/membership deviation; other changed paths are governing/TRACE history; below 50/5,000 prompt and 94/9,600 ceiling; immutable 47/4,800 approval predates all work and does not ratchet; unchanged NUL-safe method. | Repository; Git 2.42.0; exact refs | VERIFIED | [`adapter-and-suite.txt`](adapter-and-suite.txt) final 47-row table and reproduction method |

`E-accounting-R2` is the sole accounting row for the final Candidate epoch. It neither moves
Candidate nor supplies late authority: REVIEW §10 prospectively admitted the eight-path constituent
inside the existing selector before implementation.

### Return Round 2 Verdict

Final-Candidate evidence verdict: 12/13 VERIFIED, 1 DEFERRED, 0 BLOCKED, 0 N/A.

The only deferred row is AC-9's intentionally downstream independent acceptance, D75 docs effect,
bounded follow-up and terminal lineage. No transcript/session inspection is evidence for any row.
