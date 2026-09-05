# RF — TFW_20260905-124029_RTPSN / Phase B: Session Identity Ergonomics

> **Date**: 2026-09-06
> **Author**: codex/TFW_20260905-124029_RTPSN/phase-b/executor
> **Status**: 🟢 RF — Complete
> **Parent HL**: [Master HL](../HL-TFW_20260905-124029_RTPSN.md) · [Phase HL](HL__phase-b__session_identity_ergonomics.md)
> **TS**: [TS Phase B](TS__phase-b__session_identity_ergonomics.md)
> **Candidate**: `e16e6100b4957478a2ba351a225a1d400cee6367`

---

## 1. What Was Done

Implemented one provider-neutral, state-backed, fail-soft session identity authority and activated it
at the first valid checkpoint of the seven approved task-bound or conditional workflows. Removed the
legacy pre-state Handoff/Review title steps, retained project-wide route skips, synchronized the
fourteen approved tracked full copies, and added source-derived semantic, context, receiver, and
protection assurance in the two existing test files.

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | `f904af889be95798ebd9b93c46508a6c295e596f` |
| Baseline / Candidate | `83b31ff8d6cdb879fdf4f20578fa688b48863f8a` / `e16e6100b4957478a2ba351a225a1d400cee6367` |
| VALUE membership | Exactly the 23 path/action/class/reason rows in [session-identity-accounting.txt](evidence/session-identity-accounting.txt) |
| Arithmetic | 360 additions + 240 deletions = 600 touched text LOC; 23 logical files; binary/non-text N/A |
| Membership deviations | None; ASSURANCE and TRACE excluded exactly as approved |
| Trigger disposition | 23 < 50 files and 600 < 5000 LOC; no split; exact prospective owner approval governs |
| Authority and timing | Immutable denominator and baseline fixed by approved TS at `f904af8` before ONB/implementation; Candidate fixed before EV/RF |
| Reproduction | Unchanged NUL-safe `git diff --name-status/--numstat --find-renames=50% -z` with 23 explicit selectors |

This reports the approved contract; it does not create a selector, move Candidate, ratchet the
denominator, or supply late authority.

### New Files

| File | Description |
|---|---|
| None | No implementation VALUE file was created; post-Candidate evidence files are TRACE. |

### Modified Files

| File | Changes |
|---|---|
| `.tfw/conventions.md` | Added the sole `Session identity` authority; retained non-authoritative navigation and A1/fail-soft rules. |
| `.tfw/glossary.md` | Replaced the obsolete role/pipe wording with a meaning/authority router. |
| `.tfw/workflows/plan.md` | Added existing/new Plan checkpoints and semantic-preserving in-file compression. |
| `.tfw/workflows/research/base.md` | Added the Research checkpoint, excluded iteration from PHASE, and preserved all stage gates. |
| `.tfw/workflows/handoff.md` | Removed legacy Step 0; added post-state EXEC checkpoint; preserved ONB/build/evidence/RF gates. |
| `.tfw/workflows/review.md` | Removed legacy Step 0; added post-Bootstrap REVIEW checkpoint; preserved Map/Verify/Judge/verdict gates. |
| `.tfw/workflows/resume.md` | Added single-task/single-phase RESUME or governing LEAD checkpoint. |
| `.tfw/workflows/docs.md` | Added auto/manual DOCS checkpoint and batch skip. |
| `.tfw/workflows/init.md` | Added post-ID/pre-state full-init checkpoint and attach/repair skip. |
| `.claude/commands/tfw-{plan,research,handoff,review,resume,docs,init}.md` | Synchronized seven exact canonical copies. |
| `.agent/workflows/tfw-{plan,research,handoff,review,resume,docs,init}.md` | Synchronized seven exact canonical compatibility copies. |
| `docs/scripts/test_runtime_context.py` | Added source parser, 15 scenarios, 16 mode cases, seven mutant families, graph/corpus and protected-span checks, and CLI evidence commands. |
| `docs/scripts/test_integration.py` | Added manifest census, ordering/deletion mutants, clean receivers, all-copy parity, protected selectors, and runtime-input bounds. |

## 2. Key Decisions

1. The conventions range is the only naming/fallback authority; workflow prose binds only state-backed timing and WORK.
2. A1 is implemented exactly as approved: a shortest unique stable-key prefix is used only after an exact BASE collision and exact readback. The rejected pipe/ASCII fallback is forbidden.
3. Complete charged-route and corpus ceilings outrank local elegance. Compression stayed inside the same seven canonical workflow paths and retained every tested gate and stop.
4. The non-resolving dispatch baseline suffix `…f8d` was not guessed. Approved artifacts/Git and an explicit Coordinator ruling establish `…f8a` without scope change.
5. Static parity and synthetic projections remain R0/R1-style assurance; only the two local Codex title readbacks support a current-host metadata claim.

## 3. Acceptance Criteria

- [x] AC-1 — one exact identity authority, deterministic task/phase/lead/collision/failure behavior, and glossary router.
- [x] AC-2 — all seven checkpoints and all eleven manifest routes/modes classified and mutation-tested.
- [x] AC-3 — every charged profile and corpus non-growth ceiling passes; copies and protected sources are exact.
- [x] AC-4 — 15 normal scenarios, 16 workflow-mode cases, complete records, and seven changing/rejected mutant families.
- [x] AC-5 — exact new/resumed local Codex readback; unavailable search/visible metrics and other hosts explicitly bounded.
- [x] AC-6 — targeted/full tests, project check, protected diffs, and immutable 23-file/600-LOC accounting verified.

## 4. Verification

- Syntax/whitespace: `py_compile` and `git diff --check` PASS.
- Targeted identity tests: 7 passed.
- Required two-file gate: 268 passed.
- Full `.tfw/scripts/ + docs/scripts/` suite: 629 passed, 1 suite-defined skip.
- Project check: PASS.
- Task check: no RTPSN defect; one pre-existing RDP 123-code-point event remains.
- Context: Plan 24665; Research 6052/6117; Handoff 6298/6298; Review 24884; Resume 3196; Docs 15242; Init 4508; active corpus 33211.
- Local caps: central 33 words; all seven workflow net deltas ≤45.
- Accounting: 23 VALUE paths, 360 additions, 240 deletions, 600 touched LOC.

## 5. Evidence

See [EV file](evidence/EV__phase-b__session_identity_ergonomics.md) for evidence details.

Evidence verdict: 7/7 VERIFIED, 0 DEFERRED, 0 BLOCKED, 0 N/A.

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|---|---|---|---|
| 1 | `workspace/2026/TFW_20260902-112841_RDP/journal/20260902-181437__amendment_escalated__531a.md` | 9 | naming | Pre-existing event summary is 123 code points against the 120 ceiling; it is the sole task-check error and was not changed. |

## 7. Fact Candidates

> fact-candidates: processed 2026-09-06

| # | Category | Candidate | Source | Confidence |
|---|---|---|---|---|
| 1 | Process | Dispatch suffix `…f8d` was a transmission typo; the approved immutable baseline is the existing Git object `…f8a`, with no scope change. | Coordinator ruling, task `01a07281-f5c5-7dc2-b0ea-37f8a6755b4e`, 2026-09-05 | High |

## 8. Strategic Insights (Execution)

No strategic insights.

## 9. Diagrams

```text
authoritative state/lineage
          │
          ▼
conventions: Session identity ──► workflow checkpoint ──► rename + exact readback
                                                        └─failure─► report once; continue unclaimed
```

---

*RF — TFW_20260905-124029_RTPSN / Phase B: Session Identity Ergonomics | 2026-09-06*
