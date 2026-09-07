# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF](../RF__TFW_20260902-222456_RTBO.md)
> TS: [approved TS](../TS__TFW_20260902-222456_RTBO.md)

## Understanding

The Executor performed one repository-wide runtime-boundary cutover: removed the committed portfolio
cache and all Full payload scripts, moved retained semantic and migration behavior into upstream-only
`tools/`, added a bounded read-only doctor, and replaced numeric prose validity with authoring guidance
while retaining structural validation. The same Candidate also changed Full canon and active adapters,
kept Assisted unchanged, generated hidden per-task documentation landings without primary Tasks/status
publication, and supplied assurance for clean receivers, migration, documentation, history, and exact
VALUE accounting.

The implementation lineage is linear: owner approval `cf89d380cab94462dc2ed5d3cd41816003e14647`,
pre-execution Baseline correction `d2488c718024f9514adce3cb553b2f0b0ff3483b`, Executor onboarding
`a25b9de0cc6b30290cf6850a6995102b4c93753a` / `aa8f2acd6981e1444f89802ca6ea5e562184a1c6`,
implementation Candidate `fd1d29949f948d141b745dcc99d771b953fd75c9`, and TRACE/evidence/final
Executor ref `15685f4687a4f14da8693b7f36e0ac202f2b73d2`. The Candidate-to-final diff is
limited to the RF, EV, nine evidence attachments, one transition event, and task `status.md`.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 — delete `workspace/00-INDEX.md`, current index/freshness/write behavior, and all ordinary duties; keep only read-only discovery | RF §§1, 2, 3 and E1 claim the cache, payload scripts, current routes, and shared-write behavior are absent | ✅ |
| AC-2 — one exact semantic no-helper Knowledge Gate with complete cases, a single Plan route, independent parity, and mutant rejection | RF §§1–3 and E2 claim one canonical algorithm, a routed Plan workflow, independent vectors, and regex-mutant failures | ✅ |
| AC-3 — exactly four optional upstream doctor operations, deterministic output, exits 0/1/2, no repair or ordinary gate | RF §§1–3 and E3 claim the bounded CLI, stable output/exits, epoch behavior, and no-write/no-gate placement | ✅ |
| AC-4 — prose brevity is guidance only; no numeric rejection/truncation; structural defects and the unedited 123 event are handled correctly | RF §§1–3 and E4 claim all prose bounds are retired, the event is unchanged/quiet, and structural counterexamples still fail | ✅ |
| AC-5 — self-contained versioned migration with explicit runtime/dependency stop, exact behavior, no overwrite, and untruncated prose | RF §§1–3 and E5 claim an isolated `tools/migrations/2.0.0/` bundle, help without site packages, zero-write prerequisite stops, and parity | ✅ |
| AC-6 — compile all traces and hidden task landings, remove primary Tasks/status publication, retain direct/cited reachability, make CI status opt-in/non-gating | RF §§1–3 and E6 claim 64/64 landings, resolved direct/cited routes, no Tasks navigation, and an explicit finite artifact outside the site | ✅ |
| AC-7 — current canon, configs, workflows, build commands, and active adapters express one no-cache/no-runtime boundary | RF §§1–3 and E7 claim authority agreement, 8/8 byte-exact adapter copies, clean receivers, current build paths, and compatible Unreleased guidance | ✅ |
| AC-8 — Assisted and all protected pre-Baseline history remain unchanged; only allowed additive compatibility notes change | RF §§1–3 and E8 claim Assisted tree equality, 243 protected tuples unchanged, the known event blob unchanged, and no broad TFW-16 claim | ✅ |
| AC-9 — full suite/collect-only/docs/doctor/receivers pass and immutable VALUE accounting replays exactly | RF §§1, 3–5 and E9/E-accounting claim 491 collected, 490 passed + 1 skipped, clean docs/doctor/receivers, 35 logical VALUE files, and 2,226 touched text LOC | ✅ |

## Deviations from TS

- RF declares no membership or scope deviation.
- One planned ASSURANCE move, `.tfw/scripts/test_gen_index.py` →
  `tools/tests/test_tfw_state.py`, appears in the Candidate diff as delete plus add at Git's 50%
  rename threshold. Both paths were approved in the ASSURANCE selector; the action form does not add a
  VALUE member or change an acceptance criterion.
- The approved TS commit initially named the earlier research-close commit as the Baseline inside the
  replay command. Commit `d2488c718024f9514adce3cb553b2f0b0ff3483b` corrected only that literal to
  the owner-approval ref `cf89d380cab94462dc2ed5d3cd41816003e14647` before ONB and implementation;
  the approved 35-file / 3,600-LOC denominator and all scope, architecture, and AC text stayed fixed.
- Baseline→Candidate includes only the approved VALUE, ASSURANCE, DERIVED, and task-local TRACE surfaces.
  Candidate→final contains 13 task-local trace/evidence paths and no implementation path.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

Stage complete: YES
