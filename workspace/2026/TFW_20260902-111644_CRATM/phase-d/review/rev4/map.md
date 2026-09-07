# Map rev4 — "What was done?"
> **Mindset:** Experienced newcomer. Understand before judging.
> **Test:** "Can I explain what was done to someone who has not read the RF?"
> RF: [RF Phase D](../../RF__phase-d__team_mode_and_role_assignment.md)
> TS: [approved TS revision 3](../../TS__phase-d__team_mode_and_role_assignment__rev3.md)
> Accepted return: [REVIEW revision 3 §8](../../REVIEW__phase-d__team_mode_and_role_assignment__rev3.md#8-coordinator-ruling--round-4-collision-and-continuation-repair)

## Understanding

Round 4 is a bounded Rung-1 return under the unchanged approved TS revision 3. The Executor changed
one VALUE path, `.tfw/conventions.md`, so collision/readback/fail-soft behavior applies to the already
rendered ordinary `BASE` or qualified `LEAD_BASE`; it changed the two approved ASSURANCE paths to
exercise that behavior and to replace open-ended Phase-D continuation matching with a finite rev3/
rev4 trace surface.

The replacement Candidate is `fac67ef443c5cb50a766cc6c6c639ea60a259437`. It follows ruling
`61c7364fac7e377a7e3b76c09d376dcd26475c98` and Round-4 ONB acceptance, and precedes cumulative
EV/RF, the RF transition and dispatch. RF reports the complete Baseline-to-Candidate VALUE result as
21 paths and 463 additions + 464 deletions = 927 touched text LOC, with Candidate-own changes limited
to the ruled one VALUE plus two ASSURANCE paths.

## TS ↔ RF Alignment

| TS requirement | RF Round-4 claim | Aligned? |
|---|---|---|
| Rev2 AC-1 — explicit AT entry, mandate, duties, returns and degradation | Retained product and assurance remain protected; no Round-4 change to AT entry or duties | ✅ claimed |
| Rev2 AC-2 — principal, working unit and proposal origin remain distinct | Collision keys remain outside authority; origin and unit history are protected | ✅ claimed |
| Rev2 AC-3 — mandate and unit instantiation remain separate | No Role Assignment, mandate, profile or lifecycle semantics were changed | ✅ claimed |
| Rev2 AC-4 — workflow consumers, copies and Codex operations keep the same model | Root/child and Plan/Resume behavior is retained; canonical/copy and managed-block checks pass | ✅ claimed |
| Rev2 AC-5 — supplied/additional profile admission composes correctly | Admission behavior is unchanged and covered by retained Phase-D tests | ✅ claimed |
| Rev3 AC-6 — replacement Candidate, protected history, cumulative traces, accounting and A5 are reproducible | Replacement Candidate is first tested implementation commit; 21/927 replay, 33,682/33,749 active corpus, 166/260 central range, cumulative Round-4 traces and finite attachments are reported | ✅ claimed |
| Rev3 AC-7 — only the selected root renders stable handle-bearing LEAD with inherited collision/readback/fail-soft behavior | `RENDERED:=BASE\|LEAD_BASE`; ab7/ac9 duplicate yields `· @ab`; exact readback claims; no-key and altered-readback report once and remain unclaimed; 19 cases and 23 mutants reported | ✅ claimed |
| REVIEW rev3 §8 — finite continuation admits only the named rev3/rev4 review, stages, cumulative artifacts, attachments, status and valid journals | Exact path constants plus closed journal grammar are reported; positive committed/anticipated surfaces and negative foreign paths are covered | ✅ claimed, post-review-tip gate still due |
| Retained verification boundary | Full suite, Phase-D tests, strict MkDocs, exact 24-token/count warning boundary, history and diff check pass | ✅ claimed |

## Changed Surface to Verify

### Candidate-own VALUE/ASSURANCE

1. `.tfw/conventions.md` — rendered-title collision contract.
2. `docs/scripts/test_runtime_context.py` — source-derived collision cases and mutants.
3. `docs/scripts/test_integration.py` — finite continuation allowlist and matrices.

### Post-Candidate TRACE

- Cumulative `ONB__…`, `EV__…`, and `RF__…` Round-4 sections.
- Seven exact `evidence/phase-d-round4-*` attachments.
- Phase status and valid transition/dispatch journals.

## Deviations from TS

No deviation is declared. The corrected files are exactly the three paths permitted by REVIEW rev3
§8, and the replacement Candidate remains inside the original 21 VALUE plus two ASSURANCE selector.
Independent verification must still establish the collision branches, finite continuation positives
and negatives, Baseline accounting, protected history, A5, tests/build, and the required continuation
guard on the final committed REVIEW rev4 tip.

## Checkpoint

**Self-check:**
- [x] Read RF §1–§5 completely, including cumulative Round 3 and Round 4 sections?
- [x] Read TS rev2 AC-1–AC-6 and governing TS rev3 AC-6/AC-7, and match them to RF §3?
- [x] Read master HL §7 Principles and identify human authority, mandate ceiling, unit/principal separation, non-authoritative navigation, structural enforcement and trace continuity?
- [x] Read cumulative ONB through Round 4; no blocking question remains and the exact return bound is accepted?
- [x] Resolve acting principal, Reviewer unit, parent Coordinator, direct route, lifecycle, dispatch and proposal origin?

Stage complete: YES
