# REVIEW — TFW_20260902-111644_CRATM / Phase B: Named principals — Revision 2

> **Date**: 2026-09-06
> **Author**: Codex (Reviewer; on behalf of `saubakirov`)
> **Verdict**: ✅ APPROVE
> **Predecessor**: [REVIEW revision 1](REVIEW__phase-b__named_principals.md), including the Coordinator ruling at `3bc14ef3980a24ceae3b679db02deb15dc4f9225`
> **RF**: [RF Phase B](RF__phase-b__named_principals.md), returned at `c4ebd9077295b031460426dc2c71819409d494d6`
> **TS**: [TS Phase B](TS__phase-b__named_principals.md), approved at `1e2631bff51b3b62673808d5de57f812883d814b`
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`

---

## 1. Map

This revision reviews the evidence-only Phase B Round 2 return ordered by the Coordinator in revision
1. From ruling `3bc14ef3980a24ceae3b679db02deb15dc4f9225` to returned tip
`c4ebd9077295b031460426dc2c71819409d494d6`, the same Executor appended ONB, EV, RF, phase status,
and journal TRACE only. EV now preserves a complete executable validator assembled from the same 17
full documented fixture payloads and records its fresh outcome. Candidate
`0ee39046b760d6d3e8d837c2377e49c1c95668bd`, every VALUE owner, the governing TS, both HLs, and the
ruled first REVIEW remain unchanged.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|---|---|---|
| V-fixtures-R2 | Complete validator, full fixtures, and fresh execution | VERIFIED | The unique EV validator fence was extracted exactly and piped to Python. SHA-256 is `1c375695ac39e429f262f3e70cadd0aedbd98ac21b996554e918d745b30fbfb2`; AST/PyYAML inspection confirms 17 literal, non-empty mapping payloads in the expected order (11 profile, 4 event, 2 binding); all 17 expected outcomes pass and the process exits 0. |
| V-output-R2 | Recorded output and external-state boundary | VERIFIED | The program emits 18 lines. Together with independently observed exit status and two binding-path facts, actual and recorded evidence are 21/21 lines with delta 0. Both `C:\Users\c0rpa\AppData\Local\tfw\bindings.yaml` and `C:\Users\c0rpa\.tfw\bindings.yaml` remain absent. |
| V-history-R2 | Append-only return and execution honesty | VERIFIED | Ruling→tip additions are ONB `70/0`, RF `29/0`, EV `367/0`, lifecycle status, and three journal events. The return calls the program reconstructed current evidence, preserves the unknown historical validator bytes, and does not invent a pre-commit status, cached-name list, or `git commit --only` transcript. Returned commit memberships and subjects are exact. |
| V-boundary-R2 | Lineage, Candidate immutability, and protected artifacts | VERIFIED | Approval→Candidate→revision-1 REVIEW→ruling→tip ancestry passes. Candidate→tip diff/history over the four literal VALUE paths is empty and there is no later VALUE commit. Master HL, Phase HL, governing TS, and ruled revision-1 REVIEW blob IDs are identical at ruling and tip; the TS blob also equals its approval blob. |
| V-accounting-R2 | Immutable value-bearing accounting | VERIFIED | Baseline `a048b2db5f44f5d748f22f3a0133f4ecf0acd9c4`→Candidate still contains exactly four `M` VALUE paths with `143 + 72 = 215` touched text LOC, no binary row, and the approved keep-one-phase denominator/trigger. Candidate remains the first VALUE commit and delegated authority/timing remain valid. |
| V-rulings-R2 | All Coordinator dispositions | VERIFIED | Item 1 is paid by E-fixtures-R2 and independent replay; item 2 is terminally not material because retrospective proof is forbidden; items 3–4 are promoted to existing task `TFW_20260902-111644_CRATM`, whose proposal §6 item 9 and frozen Phase E deliverable 6/DoD 17 own the citation sweep. No ruling remains pending. |

Raw log: [review/verify.md](review/verify.md). The historical validator bytes and exact-path staging
transcript remain unavailable and are not claimed. This is not a current evidence gap: the complete
preserved Round 2 program and fixtures independently establish AC-1, AC-2, and AC-4. AC-3, AC-5, and
AC-6 remain established because no VALUE or assurance surface changed. The first-round full-suite
result (629 passed, 1 skipped) therefore remains applicable; Round 2 additionally passed the exact
validator replay, `git diff --check`, and the project structural check.

## 3. Judge

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | DoD / all TS AC | ✅ | The preserved program and 17 complete fixtures close the AC-1/AC-2/AC-4 evidence clauses; the unchanged evidence and no-later-VALUE proof preserve AC-3/AC-5/AC-6. |
| 2 | Purpose and design | ✅ | Frozen Vision and live NS1 require named, human-governed participants and inspectable continuation. Round 2 improves evidence for that result without changing its provider-neutral, directly accountable, grant-bounded design or adding adjacent scope. |
| 3 | Debt disposed by consequence | ✅ | All four revision-1 proposals have terminal Coordinator rulings: one paid in Phase B, one not material with retrospective fabrication forbidden, and two promoted to an existing Phase E sweep. |
| 4 | Style and standards | ✅ | Returned records are candid and append-only, project/diff checks pass, and this verdict uses the required `__rev2` sibling without rewriting revision 1. |
| 5 | Observations collected | ✅ | The historical evidence/staging limits remain visible, and both citation defects remain visibly promoted. No new material observation was found. |
| 6 | RF §7–§9 complete | ✅ | RF explicitly records no Fact Candidates, no Strategic Insights, and no diagrams; Round 2 creates none. |
| 7 | Evidence exists | ✅ | EV now contains seven cumulative rows, including E-fixtures-R2 with the complete program, full payloads, recorded output, and extraction command. |
| 8 | Evidence is sufficient | ✅ | Exact replay yields 17/17 and exit 0; every fixture is complete; actual/recorded combined evidence is 21/21 lines with delta 0; both real binding paths are absent. |
| 9 | Backward compatibility | ✅ | Candidate→tip VALUE diff/history is empty; protected governing and legacy sources are unchanged; the first-round compatibility proof remains valid. |
| 10 | Safety | ✅ | Replay was in-memory; no external binding, VALUE, implementation, code, config, test, runtime, provider, Phase C–E, or frozen planning state changed; no missing history was fabricated. |

Purpose outcome remains **aligned**. The contract-baseline Vision requires that a project declare its
people and named agents, while live NS1 requires another authorized participant to inspect the
material grounds and continue without reconstructing chat. The concrete avoided harm remains a
durable act whose identity, accountable human, or authority disappears with its session. The D59,
D68, D76, D77, and D79 knowledge boundaries remain satisfied, and no new contradiction appears.

## 4. Verdict

**✅ APPROVE**

The ruled Round 2 observable completion is fully met. E-fixtures-R2 preserves a complete validator
and all 17 full fixtures; independent replay produces 17/17 and exit 0; the combined 21-line evidence
block matches exactly; real bindings remain absent; Candidate is unchanged with no later VALUE; and
the governing HL/TS plus revision-1 REVIEW did not change after the ruling. The historical limitation
and non-fabrication boundary remain explicit. All six approved acceptance criteria are supported by
sufficient current evidence, and all four Coordinator dispositions are terminal.

## 5. Tech Debt Collected and Disposed

| # | Source | Disposition | Evidence / consequence |
|---|---|---|---|
| 1 | Revision 1 §5 item 1 | **paid — phase-b** | E-fixtures-R2 plus the independent exact replay establish the current evidence obligation: 17 full fixtures, 17/17, exit 0, and recorded-output parity. |
| 2 | Revision 1 §5 item 2 | **not material — owed but forbidden to pay retrospectively** | Git proves exact Candidate membership and non-contamination. Missing historical shell output cannot be recovered, and manufacturing it would violate execution honesty. |
| 3 | Revision 1 §5 item 3 | **promoted — `TFW_20260902-111644_CRATM`** | The existing master task's proposal §6 item 9 and frozen Phase E deliverable 6/DoD 17 own correction of the two stale North Star ordinals. |
| 4 | Revision 1 §5 item 4 | **promoted — `TFW_20260902-111644_CRATM`** | The same existing Phase E citation sweep owns correction of the broken Phase B B9 anchor. |

These rows transcribe the Coordinator ruling at `3bc14ef3980a24ceae3b679db02deb15dc4f9225`.
No disposition remains pending.

## 6. Traces Updated

- [x] Phase lifecycle transitioned `RF → KNW`; the transition is recorded in `status.md` and `journal/20260906-112340__transition__4b9c.md`.
- [x] HL status if phase completes; §5 has no pending row — N/A at this checkpoint because APPROVE enters knowledge capture and does not amend either frozen HL.
- [x] Stale project files checked — `python .tfw/scripts/gen_index.py --check project` and `git diff --check` are green; citation debt is terminally promoted.
- [x] tfw-docs: Applied — `KNOWLEDGE.md` §§1–3 updated with the Named Principals architecture row, D80, the Phase B artifact row, and the replaced human-only/no-writer rule.
- [x] tfw-knowledge: N/A — RF and both REVIEW revisions contain no Fact Candidates.

## 7. Fact Candidates

No fact candidates.

> fact-candidates: processed 2026-09-06

---

*REVIEW — TFW_20260902-111644_CRATM / Phase B: Named principals — Revision 2 | 2026-09-06*
