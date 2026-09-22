# RF — TFW_20260922-123250_CMTR / Phase C: Minimal Core Integration and Live Pilot

> **Current filename**: `RF__phase-c__minimal_core_integration_and_live_pilot.md`
>
> **Date**: 2026-09-22
> **Author**: separate Codex Executor unit
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW_20260922-123250_CMTR](../HL-TFW_20260922-123250_CMTR.md)
> **TS**: [TS Phase C](TS__phase-c__minimal_core_integration_and_live_pilot.md)
> **Producer unit**: `codex:thread:local:01a0c913-7c9c-7c01-9664-dadf91e800f8`
> **Parent Coordinator**: `codex:thread:local:01a0c400-3e48-7422-bb86-3b34fe177aa5`
> **Activation / dispatch source**: `journal/20260922-173311__dispatch__41c6.md`, continued by `journal/20260922-173526__gate_answer__0e7c.md` at `bce77012f71e92350d3da5b70b1b922f6f9502aa`
> **Coordination authority**: `../HL-TFW_20260922-123250_CMTR.md @ addb2e707dd9f271b7bf1287617a8b93b8d72cb0`
> **Originating proposer**: none

---

## 1. What Was Done

Replaced the rejected tier/profile/self-calibration approach with the accepted per-launch selection rule, enforced it in Plan dispatches, and removed the two decorative template fields. The change remains provider-neutral and limits claims to requested settings and observable delivery/outcome evidence.

### Actual Value-Bearing Accounting

| Fact | Actual result |
|---|---|
| TS approval ref | `d5a953fc985c343f93e92ab07e21123afff93f67` |
| Baseline / Candidate | `e819908` / `e29ae633814c47cc41c82afab6d5359cd66f78ca` |
| VALUE membership | MODIFY/VALUE `.tfw/conventions.md` — core rule; MODIFY/VALUE `.tfw/workflows/plan.md` — dispatch enforcement; MODIFY/VALUE `.tfw/templates/HL.md` — remove profile column; MODIFY/VALUE `.tfw/templates/TS.md` — remove profile field. |
| Arithmetic | 39 additions + 50 deletions = 89 touched text LOC; 4 logical files; binary/non-text N/A. |
| Membership deviations | None. |
| Trigger disposition | Project prompts are 50 files / 5,000 LOC; actual 4 files / 89 LOC is below both. No split or escalation applies. |
| Authority and timing | Immutable owner-approved denominator: four literal paths / 300 LOC, approved in the Phase C TS at `d5a953fc985c343f93e92ab07e21123afff93f67`; no scope deviation. The later Candidate reflects an in-boundary Coordinator-requested brevity pass. |
| Reproduction | `git diff --name-status --find-renames=50% -z e819908 e29ae633814c47cc41c82afab6d5359cd66f78ca -- $valuePaths`; `git diff --numstat --find-renames=50% -z e819908 e29ae633814c47cc41c82afab6d5359cd66f78ca -- $valuePaths` |

### New Files

| File | Description |
|---|---|
| `ONB__phase-c__minimal_core_integration_and_live_pilot.md` | Executor onboarding and scope/routing validation. |
| `evidence/EV__phase-c__minimal_core_integration_and_live_pilot.md` | Acceptance, test, and accounting evidence. |
| `RF__phase-c__minimal_core_integration_and_live_pilot.md` | This implementation return record. |

### Modified Files

| File | Changes |
|---|---|
| `.tfw/conventions.md` | Replaced the tier/profile policy with `Launch selection`. |
| `.tfw/workflows/plan.md` | Requires launch selection at every role dispatch; 1,390 words. |
| `.tfw/templates/HL.md` | Removed execution-profile column and sample cell. |
| `.tfw/templates/TS.md` | Removed recommended-execution-profile field. |
| `status.md` | Transitioned Phase C from ONB to RF. |

## 2. Key Decisions

1. Preserved the binding launch-selection wording in substance and made the Plan pass concise at 1,390 words.
2. Treated requested task parameters, effective settings, delivery, outcome, and material rework as distinct evidence levels.
3. Kept the Candidate at the final tested in-boundary VALUE commit after the Coordinator-requested brevity pass.

## 3. Acceptance Criteria

- [x] AC-1: concise provider-neutral launch rule is in active core text.
- [ ] AC-2: Reviewer launch/outcome remains pending; Executor dispatch and Plan enforcement are recorded.
- [x] AC-3: decorative profile fields are removed.
- [x] AC-4: exact four-path / 300-LOC boundary and Plan word limit pass.
- [ ] AC-5: existing tests pass; independent REVIEW remains pending.

## 4. Verification

- Lint (`python -m pytest tools/tests/ docs/scripts/ -q --collect-only`): not run separately; the full test command below collected and executed the same configured suites.
- Tests (`python -m pytest tools/tests/ docs/scripts/ -q`): `14 passed in 3.45s`.
- Focused checks: `git diff --check` clean; legacy profile/tier/self-calibration search absent from the four VALUE files; Plan word count 1,390.

## 5. Evidence

See [EV file](evidence/EV__phase-c__minimal_core_integration_and_live_pilot.md) for evidence details.

Evidence verdict: 4/6 VERIFIED, 2 DEFERRED, 0 BLOCKED, 0 N/A

## 6. Observations (out-of-scope, not modified)

No observations.

## 7. Fact Candidates

No fact candidates.

## 8. Strategic Insights (Execution)

No strategic insights.

## 9. Diagrams

No diagrams.

### Material handover at this return

- **Producer/unit:** separate Codex Executor `codex:thread:local:01a0c913-7c9c-7c01-9664-dadf91e800f8`.
- **Source/epoch:** approved Phase C TS `d5a953fc985c343f93e92ab07e21123afff93f67`; source-delivery repair `bce77012f71e92350d3da5b70b1b922f6f9502aa`.
- **Inspected scope:** the four VALUE files, Phase C traces, configured checks, exact baseline-to-Candidate accounting, and launch evidence.
- **Materiality:** the correction is implemented and the configured existing test suite passed.
- **Uncertainty:** effective backend settings, comparative minimum sufficiency, and the independent Reviewer launch/outcome remain unobserved.
- **Continuation:** Coordinator should dispatch the independent `/tfw-review` and retain Candidate reachability; no Executor work remains.

---

*RF — TFW_20260922-123250_CMTR / Phase C: Minimal Core Integration and Live Pilot | 2026-09-22*
