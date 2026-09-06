# Map — "What was done?"
> **Mindset:** Experienced newcomer. Understand the returned round before judging it.
> **Test:** "Can I explain what was returned without relying on the RF verdict?"
> RF: [RF Phase C](../../RF__phase-c__authority_routing.md), cumulative Return Round 1
> TS: [approved TS Phase C](../../TS__phase-c__authority_routing.md), approval `1f1173d968e9b74a5e06e3e2070ae604c2844ca5`
> Predecessor: [historical REVIEW](../../REVIEW__phase-c__authority_routing.md), including Coordinator ruling `2d6e0f95696d12ed044305d4cf99b78d292338da`

## Understanding

The same Executor accepted the five Coordinator-ruled Rung 1 corrections under the unchanged TS,
Baseline, twelve-path VALUE selector, 12/320 denominator, and HC-C1/C2. Return Round 1 modifies six
already-approved Candidate members: canonical conventions and Plan, both accepted Plan copies, and
the two ASSURANCE modules; it then appends cumulative ONB/EV/RF and phase state/journal traces.

The return claims that live §14 owner-only readers were replaced, rule 8 now states old and new
guarantees, Plan 6d branches ordinary CL before delegated validation with actual-consumer tests, the
replacement Candidate has contemporaneous exact-path evidence, and validator stdout/fenced bytes
are separately and exactly hashed. Replacement Candidate is `989240a4714925ff9eaeb198d9f046c32f451d63`;
returned RF/state tip is `10e6b0a15e0c88e72d896343a2cc584f95578fe4`.

## TS ↔ RF Alignment

| TS / ruled requirement | RF Return Round 1 claim | Aligned? |
|---|---|---|
| AC-4 census: no competing current universal owner-signing reader; human exceptions remain | RF §10.2.1 and §10.4 claim both §14 readers corrected and allowed-class census clean | ✅ claimed |
| Frozen master deliverable 3 / DoD 10: rule 8 states prior owner-only and current resolved-ruler guarantees | RF §10.2.2 claims an explicit old→new statement without semantic change | ✅ claimed |
| AC-1/AC-4 ordinary CL: actual Plan consumer branches before delegated validation and tests routes/mutant | RF §10.2.3 and §10.5 claim actual-consumer coverage for three routes plus one rejected mutant | ✅ claimed |
| AC-6 exact-path replacement Candidate evidence and independent immutable accounting | RF §§10.1–10.3 claim contemporaneous complete capture, exact 12 VALUE members, 94 additions + 92 deletions = 186 touched LOC, and zero later VALUE | ✅ claimed |
| AC-5/AC-6 exact validator byte representations | RF §10.2.5 claims stdout 108,192 bytes/SHA `71f852...`, fenced 108,191 bytes/SHA `44e287...`, and fenced+LF equality | ✅ claimed |
| AC-2/AC-3 and compatibility boundary remain unchanged | RF §§10.3–10.5 claim preserved nearest-ruler semantics, named human exceptions, 12+2 scope, caps, copy parity, Phase A/B and D73–D80 regressions | ✅ claimed |
| Configured verification | RF §10.5 claims 638 collected; 637 passed + 1 skipped; project structure, MkDocs, diff hygiene, caps/corpus and copies pass | ✅ claimed |

## Deviations from TS

No deviation is declared. The original Candidate, RF assertions, REVIEW findings, and rejected
byte-equivalence statement remain visible as historical cumulative text; the returned sections name
the replacement Candidate and superseding live claims rather than rewriting that history. The
approved TS, both HLs, selector, denominator, caps, and Phase D/E boundaries are claimed unchanged.

## Checkpoint

**Self-check:**
- [x] Read cumulative RF §1–§5 and Return Round 1 completely?
- [x] Read the approved TS and matched every returned completion condition to its AC/frozen claim?
- [x] Read master HL §7 Principles and Phase C derivation — can I state the design philosophy?
- [x] Read cumulative ONB — were blocking questions resolved by the committed Coordinator ruling?

Stage complete: YES
