# RF — TFW_20260902-111644_CRATM / Phase C: Authority routing

> **Date**: 2026-09-06
> **Author**: Codex (Executor, acting as `saubakirov`)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW_20260902-111644_CRATM](../HL-TFW_20260902-111644_CRATM.md)
> **TS**: [TS Phase C](TS__phase-c__authority_routing.md)

---

## 1. What Was Done

Implemented one canonical human-rooted authority resolver for frozen-HL amendments. The governing
task/phase human owner supplies the root and fallback address; a separate record authorizes the root
Coordinator; only a Coordinator on the resolved prefix may add a child. The originating proposer is
preserved across transcription and sessions. Ordinary `EXTEND`/`SUPERSEDE` traverses upward to the
nearest immutable-`true`, non-proposer principal, otherwise the owner. Missing, competing, malformed,
or non-human authority refuses before work.

Plan, Review, Handoff, HL, RES, and the six accepted singular workflow copies now consume that sole
resolver. Human-only exceptions remain separate: owner-reserved claims, self-grant/handle changes,
Purpose/contract defects, `❌ REJECT`, budget/unavailable returns, real direct-owner acts, and
filing-only `RESTRICT`. The two existing repository assurance modules derive 38 complete authority
payloads and ten output-changing contradiction mutants from live sources.

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | `1f1173d968e9b74a5e06e3e2070ae604c2844ca5`; approved planning content `95eb2ab510ed8d89205ed5fe498ccb061c112888` |
| Baseline / Candidate | `fb08c120a91aca4c9ceaea859d46dd49c032afd0` / `b2a963670e2587cffa6a61d8851f37065f03cda9` |
| VALUE membership | `.tfw/conventions.md`, `M`, VALUE, sole resolver/Rung-3/exceptions; `.tfw/workflows/plan.md`, `M`, VALUE, proposal origin and verdict gate; `.tfw/workflows/review.md`, `M`, VALUE, shared route plus human exceptions; `.tfw/workflows/handoff.md`, `M`, VALUE, terminal-verdict entry; `.tfw/templates/HL.md`, `M`, VALUE, §12 authority record; `.tfw/templates/RES.md`, `M`, VALUE, non-ruling research handoff; `.agent/workflows/tfw-plan.md`, `.agent/workflows/tfw-review.md`, `.agent/workflows/tfw-handoff.md`, `.claude/commands/tfw-plan.md`, `.claude/commands/tfw-review.md`, `.claude/commands/tfw-handoff.md`, each `M`, VALUE, byte-identical accepted receiver |
| Arithmetic | 89 additions + 90 deletions = 179 touched text LOC; 12 logical files; binary/non-text N/A |
| Membership deviations | None. The immutable twelve-path selector is exact. The 141-line underspend against the approved 320-LOC comparison denominator does not change that denominator. |
| Trigger disposition | Cause: 12 VALUE files / 179 touched LOC are below the configured 50/5,000 prompts. Cost: one cross-consumer authority contract. Assurance: 38/38 payload parity, 10/10 output-changing rejected mutants, six copy pairs, fixed attention limits, and 635 passing tests. Split rejected because convention-only, stale copies, or stale expected text ships contradictory authority. Terminal disposition: keep one Phase C. |
| Authority and timing | Immutable 12 files / 320 touched LOC (200 additions + 120 deletions) was approved before handoff. Both multiplier limits remain untriggered; HC-C1/C2 were not relaxed. Candidate was obtained from Git after the final verified surface and before EV/RF/REVIEW/final state. |
| Reproduction | The unchanged literal twelve-path PowerShell array and NUL-safe `git diff --name-status --find-renames=50% -z` / `git diff --numstat --find-renames=50% -z` method reproduce twelve `M` records and 89/90; see EV E-accounting. |

This reports the approved contract; it cannot create a selector, move Candidate, ratchet the denominator,
or supply late authority.

### New Files

| File | Description |
|---|---|
| `ONB__phase-c__authority_routing.md` | Executor onboarding, exact refs, scope, risks, and evidence plan |
| `evidence/EV__phase-c__authority_routing.md` | Complete executable validator, all expanded payloads/results, census, parity, route/corpus totals, tests, build, accounting, and lineage |

### Modified Files

| File | Changes |
|---|---|
| `.tfw/conventions.md` | Defines the sole human-root/child-only initiation and nearest eligible non-proposer ruler contract; updates Rung 3 and Phase C anti-patterns. |
| `.tfw/workflows/plan.md` | Preserves proposal origin, invokes rule 8, validates authority/signature, and stops before unresolved amendment application. |
| `.tfw/workflows/review.md` | Uses shared Rung-3 authority while retaining Purpose, contract-defect, and reject owner routes and Reviewer stop. |
| `.tfw/workflows/handoff.md` | Requires a valid terminal rule-8 verdict and keeps resolution outside Executor authority. |
| `.tfw/templates/HL.md` | Records proposer origin, ruler/signature, direct real-owner act, owner-reserved/self-grant returns, and filing-only `RESTRICT`. |
| `.tfw/templates/RES.md` | Keeps Researcher non-ruling; Coordinator transcribes with preserved origin and routes under rule 8. |
| `.agent/workflows/tfw-plan.md` | Byte-identical accepted Plan receiver. |
| `.agent/workflows/tfw-review.md` | Byte-identical accepted Review receiver. |
| `.agent/workflows/tfw-handoff.md` | Byte-identical accepted Handoff receiver. |
| `.claude/commands/tfw-plan.md` | Byte-identical accepted Plan receiver. |
| `.claude/commands/tfw-review.md` | Byte-identical accepted Review receiver. |
| `.claude/commands/tfw-handoff.md` | Byte-identical accepted Handoff receiver. |
| `docs/scripts/test_runtime_context.py` | Adds source-derived full authority payloads, resolver projections, expected outcomes, mutation rejection, and updates affected P2/Rung records without cap changes. |
| `docs/scripts/test_integration.py` | Verifies consumer/copy coherence and independently detects a surviving universal owner-only route. |

## 2. Key Decisions

1. `status.md.owner`, separate root authorization, and dispatch provenance remain three distinct facts.
   Neither profile accountability nor binding/title/provider/session data substitutes for any one.
2. Initiation is construction-time safety: only an already-rooted Coordinator adds a new child;
   repeated, competing, missing, backward, Executor, and non-human paths refuse before work.
3. Amendment resolution compares stable principal handles and preserves the original proposer. A new
   session or a Coordinator transcription cannot launder self-approval.
4. Consumers refer to `HL Contract` rule 8 instead of restating traversal. The six supported copies
   are exact bytes of their canonical workflows.
5. Human exceptions stayed literal and separate. `RESTRICT` applies on filing; ordinary delegated
   resolution cannot capture Purpose/defect/REJECT, reserved, self-grant, budget, or unavailable cases.
6. The approved ceilings were held by substitution and compaction. No cap, manifest, plural adapter,
   runtime, schema, role assignment, provider route, Phase D/E, or external state was changed.

## 3. Acceptance Criteria

- [x] AC-1 — human-rooted child-only initiation chain, ordinary CL compatibility, full refusal matrix, and no runtime/schema dependency.
- [x] AC-2 — nearest authorized non-proposer resolution, proposer/session stability, owner fallback, grant/signer validation, and immutable grants.
- [x] AC-3 — human exceptions, direct real-owner act, filing-only `RESTRICT`, Purpose/REJECT owner routes, and all Role Locks remain distinct.
- [x] AC-4 — every live owner-only occurrence is classified; consumers share rule 8; six copies match; source-derived tests and mutants reject contradictions.
- [x] AC-5 — exact boundary, prior Phase A/B/RCFR/VBSA invariants, word/corpus/route ceilings, structure, tests, and real MkDocs build pass without cap edits.
- [x] AC-6 — approval/Baseline/Candidate lineage, exact membership, NUL-safe 12/179 replay, first-tested Candidate timing, and zero later VALUE at EV capture are recorded.

## 4. Verification

- Collection (`python -m pytest .tfw/scripts/ docs/scripts/ --collect-only -qq`): PASS — 636 tests collected.
- Tests (`python -m pytest .tfw/scripts/ docs/scripts/ -q`): PASS — 635 passed, 1 skipped in 360.27 s.
- Authority projection: PASS — 38/38 full expected/actual payloads; 10/10 output-changing mutants independently rejected.
- Preserved-program replay: PASS — 503-line EV program reproduced the recorded 3,788-line output byte-for-byte; SHA-256 `1a0445cb508a3634b462e083731e98eb661819c16980aa28ba2375268dda21f6`.
- Documentation: PASS — the integration autouse fixture ran `python -m mkdocs build --config-file docs/mkdocs.yml` before its 97 passing tests.
- Project structure (`python .tfw/scripts/gen_index.py --check project`): PASS — project consistent with framework 2.1.0.
- Copy parity: PASS — all six canonical/copy SHA-256 pairs match.
- Attention contract: PASS — Plan 24,678/24,725; Research focused 6,091/6,102; Research deep 6,156/6,167; Handoff 6,339/6,366; Review 24,920/24,954; Resume 3,194/3,264; Docs 15,264/15,278; Init 4,513/4,529; active corpus 33,288/33,749.
- Diff hygiene (`git diff --check <Baseline> <Candidate> -- <12 VALUE + 2 ASSURANCE paths>`): PASS.
- Candidate immutability: PASS — Candidate is an ancestor of evidence tip; `git diff <Candidate> HEAD -- <12 VALUE paths>` and later VALUE history are empty.

## 5. Evidence

See [EV file](evidence/EV__phase-c__authority_routing.md) for evidence details.

Evidence verdict: 7/7 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|---|---|---|---|
| 1 | `.tfw/conventions.md` | 1057 | naming | The live §14 anti-pattern still says “logged owner verdict.” Canonical rule 8 narrows this to a verdict in the owner-rooted §12 channel and the HL terminal forms name `{ruler}`, so it adds no second traversal; read alone, however, the legacy noun can imply that only the owner may sign. Candidate was frozen before evidence intake, so this ambiguity is disclosed for independent Reviewer judgment rather than silently edited. |

## 7. Fact Candidates

No fact candidates.

## 8. Strategic Insights (Execution)

No strategic insights.

## 9. Diagrams

No diagrams.

## 10. Return Round 1 Results

This section appends the same-Executor Rung 1 return required by the Coordinator's
`REVISE` ruling. It supersedes the original RF's Candidate, accounting, evidence verdict,
and unresolved observation for the live review route; the original text remains intact as
rejected history.

### 10.1 Ruling and replacement lineage

- Coordinator ruling tip: `2d6e0f95696d12ed044305d4cf99b78d292338da`.
- Approval: `1f1173d968e9b74a5e06e3e2070ae604c2844ca5`.
- Baseline: `fb08c120a91aca4c9ceaea859d46dd49c032afd0`.
- Planning content: `95eb2ab510ed8d89205ed5fe498ccb061c112888`.
- Replacement Candidate: `989240a4714925ff9eaeb198d9f046c32f451d63`.
- Replacement Candidate parent: `f904e3af4ccb87ebc466ec2d896c25fa66b694be`.
- Cumulative evidence commit: `67e8052211e42429532fd0dd11db8b0eb7077a01`.
- The prior Candidate `b2a963670e2587cffa6a61d8851f37065f03cda9` remains historical and is not the review target.

### 10.2 Ruling disposition

1. Both live conventions §14 owner-signing formulations now require the valid rule-8
   verdict/application sequence. The allowed-class census reports zero competing universal
   owner readers.
2. Rule 8 now states the transition explicitly: old "only the owner rules"; new ordinary
   delegation uses the nearest eligible non-proposer, falling back to the governing owner.
3. Plan 6d now places the ordinary CL/no-delegation branch before the delegated-prefix
   branch. Assurance parses and executes the actual Plan consumer, and its output-changing
   mutant is independently rejected.
4. The replacement Candidate was made with one successful exact-path commit invocation
   whose contemporaneous full status, cached names, unstaged names, pathspec, commit output,
   and Git-derived hash are preserved in EV §8. An earlier wrapper parse failure executed no
   statement and is disclosed but is not presented as the capture.
5. Validator stdout and fenced-content digests are separately labeled. The exact stdout is
   108,192 bytes including one terminal LF with SHA-256
   `71f852a74b19efb803033e9d7bb265b3029221f93158be92297db4bd339e2381f`; the fenced content
   is 108,191 bytes with SHA-256
   `44e2878f7e5aa95a3423cec2f07e31a83871ca25825a01cd0d23bc00c06fc74f`.
   The unsupported original live equivalence claim is withdrawn; its rejected historical
   record is preserved.

### 10.3 Actual value-bearing accounting

| Measure | Approved denominator | Replacement actual | Result |
|---|---:|---:|---|
| VALUE files | 12 | 12 | Exact approved set |
| Added lines | 200 | 94 | Within denominator |
| Deleted lines | 120 | 92 | Within denominator |
| Touched LOC | 320 | 186 | 41.9% below denominator |

The return changed six approved files: `.tfw/conventions.md`, the canonical Plan workflow,
its two approved copies, and the two approved assurance files. Baseline-to-replacement
membership remains exactly the immutable 12-file VALUE set. No cap, scope, product/runtime,
configuration, schema, manifest, plural target, Phase D/E, external state, or unauthorized
file changed. There were no deviations from the Rung 1 ruling.

### 10.4 Acceptance criteria

- [x] AC-1 — initiation, ordinary CL, and refusal behavior remain intact.
- [x] AC-2 — nearest eligible non-proposer resolution and governing-owner fallback are explicit and executable.
- [x] AC-3 — human exceptions and owner-reserved routes remain distinct from ordinary delegation.
- [x] AC-4 — both live §14 formulations are corrected; six copies match; census and mutants reject contradictions.
- [x] AC-5 — all local/corpus ceilings, structure checks, regression tests, and the real MkDocs build pass without cap edits.
- [x] AC-6 — replacement capture, lineage, exact membership, 12/186 accounting, stdout framing, and zero later VALUE changes are recorded reproducibly.

### 10.5 Verification and evidence

- Targeted runtime assurance: `8 passed, 171 deselected in 69.41s`.
- Direct final integration census/copy/mutant checks: 2 passed.
- Collection: 638 tests.
- Configured suite: `637 passed, 1 skipped in 334.64s (0:05:34)`, including the real MkDocs build.
- Project structure: `python .tfw/scripts/gen_index.py --check project` exited 0.
- Authority program: 38 fixtures, 38 parity checks, 10 base mutants, 3 Plan cases, and 1 Plan mutant rejected.
- Copy parity: all canonical/copy SHA-256 pairs match.
- Diff hygiene, NUL-safe accounting, lineage, cap-span immutability, route/corpus ceilings,
  Candidate ancestry, and zero post-Candidate VALUE delta all pass.

See cumulative [EV §8](evidence/EV__phase-c__authority_routing.md) for the complete program,
output, capture transcript, accounting, and replay material.

Return evidence verdict: 7/7 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A.

### 10.6 Return observations and candidates

The original §6 observation is resolved by the approved return edit. No new observations,
fact candidates, strategic insights, or diagrams were introduced.

---

*RF — TFW_20260902-111644_CRATM / Phase C: Authority routing | 2026-09-06*
