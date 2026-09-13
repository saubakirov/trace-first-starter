# RF — TFW_20260913-151442_RWNR / Phase A: Rehome continuation responsibilities

> **Date**: 2026-09-13
> **Author**: robert, Executor unit `01a09b39-f0c0-70c0-9b53-6981647e72fb`
> **Status**: 🟢 RF — Complete
> **Parent HL**: [Phase A HL](HL__phase-a__continuation_responsibilities.md)
> **TS**: [TS Phase A](TS__phase-a__continuation_responsibilities.md)
> **Candidate / producer**: `c319269d24abb89a58e2dc1a18ada1ea4ecb8120`

---

## 1. What Was Done

Plan now resolves an exact existing task or phase before the Knowledge Gate or any write, then returns one total routing result without performing another role's effect. It distinguishes active, historical, collision and invalid selections; keeps phase state local; covers every declared lifecycle/review branch; re-resolves and reapplies continuation identity; and routes close/recovery cases to the central Coordinator control contract. The canonical workflow was reduced to 1,199 strict Unicode words and synchronized byte-for-byte to both full-copy receivers. Resume and all live-retirement surfaces remain unchanged.

Assurance now supplies 28 no-mutation route fixtures, 10 identity/readback cases, seven semantic mutant families, isolated receiver migration preconditions, exact split-history oracles, immutable accounting and full regression gates. Phase A does not perform the modeled Phase B retirement.

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | `413945ca0a4f34065ff22b8b24f47bf694d72710`; TS blob `d15c5dc8b25c2751ed289a418f937226608333dc`; owner approval event `journal/20260913-194049__dispatch__f58c.md` |
| Baseline / Candidate | `f6e85aa898061779c6b37bba34dc97e28c76f01f` / `c319269d24abb89a58e2dc1a18ada1ea4ecb8120` |
| VALUE membership | MODIFY `.tfw/workflows/plan.md` — canonical returning-work router; MODIFY `.agents/workflows/tfw-plan.md` — exact Antigravity full-copy receiver; MODIFY `.claude/commands/tfw-plan.md` — exact Claude full-copy receiver. All three are VALUE. |
| Arithmetic | 255 additions + 492 deletions = 747 touched text LOC; 3 logical files; binary/non-text N/A |
| Membership deviations | None. Candidate also contains only the two approved ASSURANCE modifications; no new/unclassified instruction or Resume path. |
| Trigger disposition | Cause: one canonical rewrite plus two atomic copies. Cost: 3 files/747 LOC. Assurance: two approved contract modules and immutable receipts. Split: no useful split. Authority: within owner-approved `3/900`. Terminal verdict: below 50-file/5,000-LOC and 2× thresholds; no return trigger. |
| Authority and timing | Immutable denominator `3 VALUE files / 900 touched text LOC` approved before work at the ref above. Candidate is the first tested Executor implementation commit and was frozen before EV/RF; later TRACE does not move it. |
| Reproduction | `git diff --name-status --find-renames=50% -z <Baseline> <Candidate> -- <three literal VALUE paths>` and matching `--numstat`; exact command/output with visible NUL escaping is in `evidence/phase-a-tests.txt`. |

### New Files

| File | Description |
|---|---|
| `ONB__phase-a__continuation_responsibilities.md` | Executor onboarding, authority, risks and citation-resolution record |
| `evidence/phase-a-routing.json` | Candidate-bound route, identity and mutant receipt |
| `evidence/phase-a-receiver-migration.json` | Isolated receiver preflight, refusal, convergence and idempotence receipt |
| `evidence/phase-a-history.json` | Task-tree manifest and append-only aggregate receipt |
| `evidence/phase-a-accounting.json` | Immutable Baseline/Candidate VALUE and surface arithmetic |
| `evidence/phase-a-tests.txt` | Candidate-bound raw pytest, scope, parity and accounting output |
| `evidence/EV__phase-a__continuation_responsibilities.md` | One VERIFIED row per AC plus the required accounting row |

### Modified Files

| File | Changes |
|---|---|
| `.tfw/workflows/plan.md` | Added pure existing-reference continuation pre-route; preserved planning, identity, authority and amendment contracts while deduplicating to 1,199 words |
| `.agents/workflows/tfw-plan.md` | Synchronized exact canonical Plan bytes |
| `.claude/commands/tfw-plan.md` | Synchronized exact canonical Plan bytes |
| `docs/scripts/test_runtime_context.py` | Added total route/identity evaluators, 28 fixtures, 10 identity cases, no-mutation checks and seven semantic mutant families |
| `docs/scripts/test_repository_contracts.py` | Added Candidate accounting, receiver migration, history preservation, parity/scope and unchanged-Resume assurance |

## 2. Key Decisions

1. The returning-work decision is an early, pure Plan pre-route. Routes are outputs only; downstream workflow owners retain every lifecycle and implementation effect.
2. Selected phases read only phase-local carriers. Unselected `PHASES` waits for human selection; nested phase carriers are invalid.
3. LEAD navigation is recomputed from authoritative lineage on every continuation. Principal attribution, visible title and shared profile never substitute for the actual root unit or direct dispatch.
4. Receiver retirement remains Phase B work. Phase A proves the five preflight outcome classes and history conditions without deleting or changing any Resume surface.
5. Candidate identity is the first immutable implementation commit. The evidence and RF are TRACE-only and do not change the approved denominator or Candidate.

## 3. Acceptance Criteria

- [x] AC-1 — three-path canonical/copy boundary, 1,199-word Plan, `C=1,199 < B=2,737`, exact immutable accounting, no Resume or substitute surface.
- [x] AC-2 — all 28 source-derived lifecycle/selection fixtures return the exact route and preserve complete repository bytes.
- [x] AC-3 — all 10 continuation identity/reapply/readback cases preserve root/child/non-AT boundaries and fail soft only for transport.
- [x] AC-4 — Plan performs no delegated effect; close/recovery and carrier mismatch resolve to the exact Coordinator control address.
- [x] AC-5 — all five receiver classes, four-adapter convergence, empty second run, 179-entry task digest and three aggregate subsequence oracles pass; Resume stays unchanged.
- [x] AC-6 — Candidate-bound targeted, collection and configured suites pass; all mutant families change projection before independent rejection.

## 4. Verification

- Targeted (`python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_repository_contracts.py -q`): 355 passed in 268.38s.
- Lint/collection (`python -m pytest tools/tests/ docs/scripts/ -q --collect-only`): 625 tests collected in 0.22s.
- Tests (`python -m pytest tools/tests/ docs/scripts/ -q`): 624 passed, 1 platform skip, 0 failed in 514.42s.
- Scope/parity/accounting: Candidate has exactly five approved implementation paths; three VALUE copies share SHA-256 `47c79864b215c176e170da39e2b26067ecb04d60c894440c992e47b7e12b5749`; 3 files and 747 touched text LOC; Plan/C 1,199; no Resume path changed.

## 5. Evidence

See [EV file](evidence/EV__phase-a__continuation_responsibilities.md) for evidence details. Structured receipts are `phase-a-routing.json`, `phase-a-receiver-migration.json`, `phase-a-history.json`, and `phase-a-accounting.json`; exact command output is `phase-a-tests.txt`.

Evidence verdict: 7/7 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A

## 6. Observations (out-of-scope, not modified)

No observations.

## 7. Fact Candidates

No fact candidates.

## 8. Strategic Insights (Execution)

No strategic insights.

## 9. Diagrams

No diagrams.

---

*RF — TFW_20260913-151442_RWNR / Phase A: Rehome continuation responsibilities | 2026-09-13*
