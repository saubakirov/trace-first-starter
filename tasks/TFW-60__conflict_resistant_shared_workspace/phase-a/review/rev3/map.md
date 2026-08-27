# Map — "What was done?" (revision 3)
> **Mindset:** Experienced newcomer. Understand the second corrective pass before judging it.
> **Test:** "Can I explain what changed since review revision 2?"
> RF: [RF Phase A, revision 2](../../RF__phase-a__task_state_and_coordination.md)
> TS: [TS Phase A, revision 4](../../TS__phase-a__task_state_and_coordination.md)
> Historical review: [revision 2 — REVISE](../../REVIEW__phase-a__task_state_and_coordination__rev2.md)

## Understanding

The second corrective pass addresses the bounded defects from review revision 2. It replaces
arithmetic journal timestamps with fresh clock readings, rejects provider-family actors,
declares the whole clock-plus-slug identifier in both configuration files, restores the
literal Windows binding path in canonical workflows and copies, adds a current handoff event,
and regenerates the contested RF/EV attachments.

The product remains the Phase A mode-agnostic core: task-local state and journals replace the
root board as live authority; a persisted index is derived and non-blocking; legacy tasks are
not moved; participant profiles carry declared attribution; and the release surface is TFW
2.0.0. The owner has formally approved the delivered 47-modified / 30-new / 77-file product
budget, so the unchanged count is not reopened in this review.

Review revision 2 had already covered all 119 then-current baseline-to-HEAD paths. This review
inspected every one of the 30 paths in the second corrective iteration; paths outside that
delta remain byte-identical to the surface audited in revision 2. The current
`80d6a16..HEAD` surface is 129 paths (77 modified, 52 added). The intervening TFW-58 proposal
commit is separately attributed and is not executor product for this phase.

## TS ↔ RF Alignment

| TS requirement | RF claim | Mapped result |
|---|---|---|
| AC-1 — configured containers, year nesting, stable paths | unchanged fixture and resolver behavior | Implemented; prior verification remains valid and full tests pass |
| AC-2 — the whole directory name is the identifier everywhere | both `id_format` values fixed | Config fixed; `init.md` and artifact-naming conventions still call the bare stamp `{ID}` or append `{title}` to an already whole ID |
| AC-3 — actual-clock, actor-bearing, accountable journal events | fresh-read helper, provider rejection, current handoff | Clock and provider fixes work; integrated actor/accountability validation still fails open when `team/` is empty and cannot enforce that `on_behalf_of` is human |
| AC-4 — participants declared in `team/` | declared-handle validation added | Direct-set tests pass; the production caller converts an empty handle set to `None`, disabling the rule, and profile types are discarded |
| AC-5 — derived index never authoritative | `--validate` remains the build gate | Implemented; `--check` is current before this review transition and is not a lifecycle gate |
| AC-6 — lossless migration | regenerated E35 and current accounting | The core 61-row migration remains sound; EV contains mutually contradictory old and new E35 output |
| AC-7 — references keep resolving | link relation re-run | Legacy compatibility remains intact; new-task artifact naming is internally inconsistent on the canonical release surface |
| AC-8 — root board retired | unfiltered sweep recorded | Implemented; 19 current hits are historical, migration, glossary, or guard-test uses |
| AC-9 — no runtime required | unchanged ordinary-file lifecycle | Implemented |
| AC-10 — release surface describes what shipped | configs, workflows, adapters, evidence updated | Not complete: canonical init/artifact/event examples still teach superseded identifier or event grammar |
| AC-11 — rejected-pass defects corrected | all original findings marked closed | The original clock/path/config defects are closed; evidence accuracy is still not closed |
| AC-12 — second precision and phase-local state | unchanged implementation | Implemented; phase state validates independently of task `PHASES` state |
| AC-13 — all review-revision-2 findings closed | eight corrections reported | Items 1–4 and 6 are materially fixed; item 5 remains false in the final evidence; item 7 was explicitly declined by approved TS R4 and disclosed in RF observation 12 |

## Review Revision 2 — Current Disposition

| Revision-2 item | Current disposition |
|---|---|
| 1. Fresh clock readings | ✅ Corrected; controllable-clock and midnight tests pass |
| 2. Provider actor rejection and declared handles | ⚠️ Provider rejection works; declared-handle/type enforcement is incomplete in the integrated caller |
| 3. Full identifier in configuration | ✅ Both config values corrected; broader canonical ID residue remains |
| 4. Literal Windows path and class gate | ✅ Literal path restored; 22 workflow copies remain byte-identical; current class scan finds zero control bytes |
| 5. Regenerate RF/EV evidence | ❌ Not closed; final artifacts retain incompatible counts, revisions, heads, and command output |
| 6. Current handoff event | ✅ `20260827-043340__handoff__saubakirov.md` validates and points at the current RF |
| 7. Citation addendum | Disposed by approved TS R4: the ONB remains immutable and RF observation 12 records the three bad applications. The applications remain semantically wrong but are not concealed |

## Deviations from TS

- No new implementation scope was added by the executor; the TFW-58 proposal is a separate
  coordinator commit and was isolated from the phase delta.
- The evidence attachments are work artifacts excluded from the product-file budget by S46;
  their addition does not change the approved 77-file product count.
- The approved R4 disposition preserves the old ONB rather than adding the addendum requested
  by review revision 2. This review treats the three irrelevant applications as disclosed
  historical trace, not as corrected semantics.

## Checkpoint

**Self-check:**
- [x] RF §§1–5 read completely.
- [x] TS revision 4 and every AC group mapped to RF claims.
- [x] Master HL at `c1782b3`, current Phase HL, and all master principles read.
- [x] ONB questions, revision-2 REVIEW, and all revision-2 stage files read.

Stage complete: YES
