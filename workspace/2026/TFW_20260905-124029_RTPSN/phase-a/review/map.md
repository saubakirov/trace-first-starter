# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase A](../RF__phase-a__command_entry_reliability.md)
> TS: [TS Phase A](../TS__phase-a__command_entry_reliability.md)

## Understanding

The Executor added a non-default Codex command-entry evaluation harness and its offline assurance suite, then documented one universal six-step entry boundary and six non-substitutable evidence levels in the three unconditional VALUE surfaces. The approved 54-valid-run live matrix was stopped after observed usage made completion infeasible under the immutable 750,000-token ceiling; seven valid attempts were retained, AC-3 was reported `BLOCKED`, H4 remained inconclusive, and the current production skill baseline was retained without changing the conditional 22 skill paths. The immutable Candidate contains the seven implementation/assurance files plus execution trace setup; EV, raw evidence, RF, and the final RF transition follow it in later TRACE-only commits.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 — reproduce the exact 11-command × 4-adapter census, immutable revision comparison, incident classification, and six-level claim boundary | RF §3 marks AC-1 complete and points to the topology evidence, revision/context comparison, causal boundary, and live/absent-host limits | ✅ |
| AC-2 — provide a safe, explicit, non-default harness with fixed fixtures/arms, independent graders, budgets, redaction, cleanup, dry-run, and offline mutants | RF §3 marks AC-2 complete; RF §§1/4 report the harness, exact dry-run schedule, independent summary, fake-runner coverage, and 31 passing harness tests | ✅ |
| AC-3 — complete exactly 54 valid live runs unless the immutable 750,000-token or 180-minute ceiling blocks the matrix | RF §3 leaves AC-3 unchecked and reports `BLOCKED` after 7/54 valid runs; RF §1 preserves the denominator, 702,852 reported completed-run tokens, and an interrupted attempt with no invented telemetry | ✅ |
| AC-4 — apply one predeclared production decision without relaxing the comparison rule | RF §§2–3 record exactly `BASELINE RETAINED`, do not apply comparative selection to the partial sample, and report no production skill edit or superiority claim | ✅ |
| AC-5 — document/test one universal pre-action contract without a second algorithm, manifest runtime authority, generated input, workflow change, or Phase-B behavior | RF §3 marks AC-5 complete and RF §§1/4 claim the three documentation surfaces and semantic mutants preserve those boundaries | ✅ |
| AC-6 — prove exact topology, context accounting, parity, clean receivers, regression tests, immutable Candidate scope, and approved VALUE accounting | RF §§3–4 claim 282 targeted tests, 612 passed/1 skipped full suite, project consistency, receiver parity, immutable Candidate, and 3 logical VALUE files / 81 additions / 0 deletions | ✅ |
| AC-7 — provide a locally resolvable, claim-bounded evidence package with H3/H4 and protected-scope limits stated accurately | RF §§1, 3–5 claim 6/6 evidence artifacts resolve, H3 remains refuted, H4 remains inconclusive, 7/8 evidence rows are VERIFIED and AC-3 alone is BLOCKED | ✅ |

## Deviations from TS

- The fixed 54-valid-run matrix did not complete. The RF presents this as the TS-prescribed terminal `BLOCKED` outcome under AC-3 rather than as a smaller denominator, substituted experiment, or completed acceptance criterion.
- Seven valid attempts completed before the stop reached the running process, although the Coordinator's strategic STOP used telemetry from the first two. One already-started eighth invocation was interrupted without completed usage telemetry and is reported as uncounted rather than estimated.
- The partial live set covers only the Coordinator new-task fixture, so the RF makes no cross-role comparative, statistical-superiority, or causal claim and retains the baseline.
- The global task-state census exits 1 for a pre-existing RDP journal-summary length defect. RF §4 and §6 identify it as foreign, immutable, and out of Phase-A scope; RTPSN's project consistency check is reported separately as green.

## Checkpoint

**Self-check:**
- [x] Read RF §1–§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

Stage complete: YES
