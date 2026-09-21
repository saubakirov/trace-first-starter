# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [Phase A RF](../RF__phase-a__explicit_coordination_gateway_and_session_identity.md)
> TS: [Approved Phase A TS](../TS__phase-a__explicit_coordination_gateway_and_session_identity.md)

## Reviewed Set

| Item | Immutable reference |
|---|---|
| Governing TS | `ad6042dad73aa04b9bbe9f13880c5a944e7e4f05` |
| Accounting baseline | `c80c0dd5e79a6e996fdc68a89ad01b26887c638e` |
| First tested Executor Candidate | `1a9209530d7a939db1270e2f91dcef40a9f449e6` |
| Final Executor TRACE read | `51ee2c2274ed1c18b5135188f78540cd2321e14d` |
| Executor unit | `codex:thread:local:01a0c3a2-c742-7962-a981-369effb5ac83` |
| Coordinator route | `codex:thread:local:01a0bfdb-f0b7-7642-837c-8c47d0a284cf` |
| Reviewer unit | `codex:thread:local:01a0c3cf-8e17-7811-9e23-05575d87f952` |
| Activation source | owner-direct `/tfw-review`; originating proposer `none` |

## Understanding

The Executor replaced current mode/LEAD-centred coordination with one file-native contract: every
task-bound unit resolves a five-field routing spine, begins work only through exact skill activation,
and uses vertical gate/return traffic unless an exact iterative grant exists behind a separate
GATEWAY. The Candidate changes 47 declared VALUE paths plus one existing ASSURANCE evaluator, then
later TRACE commits migrate the live phase carrier and record tests, RF and bounded provider-native
evidence without changing VALUE.

The principal implementation choices are tolerant legacy reads with strict current writes,
authority-owned immutable `gate_answer` events, producer/parent/source provenance in role artifacts,
canonical-to-installed copy parity, and provider-specific evidence levels that preserve failures and
do not compose a reliability claim.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 — one current coordination vocabulary; historical modes remain readable but are not issued | `conventions.md` owns the model; glossary routes terms; census reports zero unexplained current issuers and no new runtime/registry/artifact | ✅ |
| AC-2 — closed five-field routing spine, legacy-read/current-write distinction, safe live migration | strict validator plus tolerant reader; partial/empty/invalid/unresolved cases refuse; Phase A status migrated post-Candidate in `9e9513a` | ✅ |
| AC-3 — vertical gates-only route; exact iterative grant; isolated GATEWAY; Reviewer independence | allowed/prohibited route matrix, GATEWAY separation and negative scenarios are reported in `coordination-scenarios.md`; live Codex return is bounded separately | ✅ |
| AC-4 — provision/activation/continuation separation and reconstructable unit lineage | owner-direct, delegated, continuation and invalid-activation cases are reported; role artifacts carry producer, parent, source and authority; title failure is fail-soft | ✅ |
| AC-5 — authority-owned `gate_answer`; ONB owns only question/reference/effect; authority changes escalate | event/template/validator fixtures reportedly cover accepted factual answer and self/cross-task/stale/missing/hidden-amendment refusals | ✅ |
| AC-6 — role-owned inputs, producer provenance, no unsolicited prework or distrust-only duplication | Briefing/RES, ONB/RF and REVIEW forms plus workflows were changed; discrepancy route remains through the detecting unit's Coordinator | ✅ |
| AC-7 — canonical/copy/migration parity, configured checks and exact accounting | RF reports 18 exact workflow copies, managed-block parity, green syntax/suite/diff checks, 47 VALUE members and no selector escape | ✅ |
| AC-8 — separately bounded native Codex, Claude and Antigravity evidence with P0–P4 limits | final ledger preserves Claude OAuth failure and first `agy` contradiction; authenticated/corrected runs are bound to native addresses and claim only Codex P2/partial P3, Claude P2, `agy` P2/partial P3; no P4/rate | ✅ |
| AC-9 — twelve semantic outcomes, configured suite, exact-path boundary, no receiver/history/FRATS-D01 mutation, then independent review | Executor reports its portion complete and explicitly leaves the independent REVIEW/final-output judgment deferred to this separate Reviewer unit | ✅ — sequencing remains open here |

## Changed-File Map

| Class | Executor result | Review target |
|---|---|---|
| VALUE | 47 literal TS members, all `MODIFY` | exact Baseline→Candidate membership, arithmetic, representative semantic checks, then 100% if any discrepancy |
| ASSURANCE | `docs/scripts/command_entry_eval.py` only | changed evaluator plus configured suite |
| TRACE before RF | Phase status migration, evidence set, RF and lifecycle journal | lineage, timing, refs and exact-path isolation |
| TRACE continuation | RF, EV and `provider-native.md` only at `51ee2c2…` | preserved contradiction, owner-authorized correction and absence of later VALUE writes |

## Deviations from TS

No RF-declared scope deviation exists. The actual 1,346 touched text LOC is below the immutable
3,200-LOC plan and below every configured trigger; all 47 planned VALUE members changed and no
additional VALUE path is claimed. Claude and `agy` do not demonstrate title readback, an addressed
cross-provider Coordinator return, full P3, P4 or a reliability rate; these are disclosed evidence
limits under AC-8 rather than substituted successes or omitted requirements.

The only intentionally unfinished item is the independent REVIEW/final-output portion of AC-9,
which belongs to this Reviewer and therefore could not be completed by the Executor.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

Stage complete: YES
