# Map — Phase B formal review round 3

> **Mindset:** Experienced newcomer; comprehend the evidence-only return before judging it.
> **RF:** [RF Phase B](../../RF__phase-b__corpus_consistency_compression_and_receiver_proof.md),
> Return Round 3
> **TS:** [approved TS revision 2](../../TS__phase-b__corpus_consistency_compression_and_receiver_proof__rev2.md)
> **Predecessor verdict:** [REVIEW revision 2](../../REVIEW__phase-b__corpus_consistency_compression_and_receiver_proof__rev2.md)
> **Reviewer unit:** `codex:thread:local:01a0c498-dc86-75f3-92d0-32e69b8bd5cc`
> **Coordinator route:** `codex:thread:local:01a0bfdb-f0b7-7642-837c-8c47d0a284cf`

## Understanding

Coordinator ruling `4cd4397795a5b831d6d90dacea1adb0a6d41efec` accepted REVIEW revision 2's
single rung-1 proposal and authorized the same Executor to repair only the reproducibility of the
rung-2 semantic replay. The Executor preserved Candidate
`93186cea9ac8209cade30a49e76f3b8a32ae6227`, added task-local TRACE harness
`evidence/rung2-semantic-replay.py`, replaced the label-only output record with an exact
command/predicate/mutation/output record, and appended affected EV/RF claims.

The executable evidence commit is `4d1c25e12564456ed7a7053532b8fa77cd73dc2f`; EV/RF binding is
`9f61f8e3bcc87274181b3ec84c449e4f014e61cd`; the RF transition is
`55ad930cf864e4afbba0572f4086ca0df0240553`. No VALUE, ASSURANCE or receiver path is claimed as
changed, and Baseline/Candidate accounting remains the independently verified 46 modified + one
zero-diff / 4,657 touched text LOC result.

## TS ↔ RF Alignment

| TS requirement | Return Round 3 claim | Mapped proof | Aligned? |
|---|---|---|---|
| AC-3 — positive/material-negative replay and Reviewer traceability | Thirteen source-derived scenarios each resolve at Candidate and fail after one exact critical-clause mutation; six edges are covered | `rung2-semantic-replay.py`; exact output `.txt`; EV E3-R3 | ✅ claimed |
| AC-10 — exact Plan behavior plus owner-direct/delegated/continuation/GATEWAY replay | Static exact-text/limit checks and five affected scenarios reproduce from TS/Candidate objects | harness `static_checks` and `SCENARIOS`; EV E10-R3 | ✅ claimed |
| AC-12 — provider-honest entry and observation boundaries | Seven mappings, allowed bounded signals/returns and prohibited transcript/session inspection are executable predicates | harness provider/observation scenarios; EV E12-R3 | ✅ claimed |
| AC-7 / scope accounting | Candidate, selector and arithmetic are unchanged; this round changes task-local TRACE only | Git path sets; EV E-accounting-R3 | ✅ claimed |
| AC-9 — independent acceptance and close | Same Reviewer verdict remains due; D75 Docs effect/follow-up and terminal close stay downstream | phase status/journal; RF/EV Return Round 3 | ⏳ downstream |
| Ruling completion condition | Exact command/harness, versions, predicates, source/mutation identity, output and exit are durable; no product runtime/permanent test is introduced | REVIEW rev2 §8; harness/text commits | ✅ claimed |

## Changed surface

- Product Candidate: unchanged at `93186cea…`.
- New task-local TRACE: `evidence/rung2-semantic-replay.py`.
- Replaced TRACE output: `evidence/rung2-semantic-replay.txt`.
- Appended cumulative records: ONB, EV, RF, REVIEW revision 2 ruling, phase status and two journal
  events.
- No canonical workflow, adapter, generated copy, assurance source, receiver repository,
  `KNOWLEDGE.md`, runtime, public command or permanent test is changed.

## Deviations from TS

No deviation is declared. A task-local executable evidence harness is explicitly authorized by the
rung-1 Coordinator ruling and serves AC-3 traceability without becoming product runtime or a
permanent test. The new evidence does not move Candidate or ratchet the immutable denominator.

## Checkpoint

**Self-check:**

- [x] Read RF Return Round 3 §§1–5 and its material handover.
- [x] Matched every affected claim to AC-3, AC-7, AC-9, AC-10 and AC-12.
- [x] Reused unchanged frozen purpose/principles and prior full Candidate verification; no changed
  input requires reopening unrelated ACs.
- [x] Read ONB Return Round 4; no blocking question remained and the ruling forbade VALUE changes.
- [x] Mapped ruling, ONB, harness, EV/RF and RF-transition chronology.

Stage complete: **YES**
