# Phase HL — TFW_20260913-151442_RWNR / B: Retire the public Resume surface

> **Date**: 2026-09-13
> **Author**: robert, Coordinator unit `01a09a92-18fb-7da1-a639-6a86844bf147`
> **Status**: 📝 DERIVED DRAFT — Phase B TS awaits owner approval; `status.md` owns live state
> **Parent**: [Master HL](../HL-TFW_20260913-151442_RWNR.md), Phase B
> **Governing master contract**: frozen by `saubakirov`; A1 re-freeze `74e63242a1a713c8a2c4490edda24f84bfc68153`
> **Planning baseline**: `d366bb1d6d70cf457acba84d4b5aafeb5c5f5b14` on local `master`
> **Phase A prerequisite**: [status](../phase-a/status.md) `DONE`; accepted Candidate `ddb6fc4a1ab528525abd1020ee2fb562d4e10f65`; corrected TRACE `495de8ceda0532f4a9fdf2cf4002dcc84b652791`; independent REVIEW producer `eafeef6859f12f65f11f1a42a0174f8d38e7350d`; closure/landing producer `d366bb1d6d70cf457acba84d4b5aafeb5c5f5b14`
> **Research basis**: [Iteration 2 RES](../research/iter2/RES.md) · [Extract E1–E5](../research/iter2/3_extract.md) · [Challenge](../research/iter2/4_challenge.md)

## Parent Derivation

This phase implements only master HL §4 Phase B after Phase A's independently accepted result is landed and integrated. It inherits master DoD 4–20 where applicable, DoF 1–13, all eight principles, and §7.1 without changing them. Vision, acceptance, failure, principles, G1, A1, Phase A, TKL, and G2 authority remain solely in the frozen master HL.

The derivation is deletion-led: remove the public Resume surface and update only the live registrations, generated or managed receivers, current instructions, and assurance that would otherwise recreate or advertise it. It adds no replacement command, route, alias, helper, runtime, registry, or release artifact.

## Starting Point

- Local `master` and this planning branch both start at `d366bb1d6d70cf457acba84d4b5aafeb5c5f5b14`. Phase A is terminal `DONE`; its accepted Plan and full-copy receivers stay byte-fixed, Plan stays routing-only, and `C=1,199 < 2,737` at the Phase A Candidate.
- At research baseline `a2363fd07253ca92410db149b4301432de79be3b`, the deterministic live selector found 23 paths whose path or blob contains `/tfw-resume`, `tfw-resume`, or `resume.md` after excluding task traces and the three append-capable aggregates. Two are assurance modules; the other 21 are live VALUE surfaces.
- A separate case-insensitive scan for the obsolete fixed command count found nine additional live VALUE paths that state the eleven-command surface. Together these make the exact 30-path Phase B VALUE selector.
- Five live Resume artifacts are deletions: the canonical workflow, the canonical and installed Codex skills, and the two installed full-copy command files. The remaining 25 VALUE paths receive only the removal, registration, managed-block, count, or current-documentation edits required for ten-command convergence.
- Phase A proved the continuation, identity, receiver-preflight, and history mechanisms. Phase B must preserve those proofs and turn the migration model into Candidate-bound absence, clean-install, owned-receiver, foreign-refusal, and repeat-run evidence.
- The actual release version, migration filename/content, changelog entry, release actor, tag, and every external effect remain G2 decisions. Phase B may test the version-addressed algorithm with an ephemeral pinned target; it must not create or infer a release guide.

## Owner-Directed Knowledge-Gate Exception

The canonical hard Knowledge Gate exposed a known digest-state inconsistency: at least five active fact IDs are absent from `.tfw/knowledge_state.yaml`. Owner `saubakirov` ruled, through the direct LEAD continuation, “Про знания это баг, не обращай внимание на консолидацию пока что, идем дальше. Мы его этот баг исправим позже.” For this Phase B planning turn only, that ruling bypasses and defers the gate so planning can continue.

This is not consolidation and does not resolve, normalize, or generalize the defect. Phase B performs no `/tfw-knowledge` route and changes none of `KNOWLEDGE.md`, `knowledge/**`, `.tfw/knowledge_state.yaml`, `.tfw/project_config.yaml` for digest repair, or the gate algorithm. The existing configuration edit in Phase B is limited to removing the exact live `tfw.workflows.resume` registration after TS approval.

## Finished Phase View

```text
accepted Phase A Plan + exact lifecycle owners
                     |
                     v
all-preflight 30 live VALUE paths + receiver ownership + history before-images
       | any missing/extra/drift/proof failure
       +------------------------------------------> C1: keep Resume; no partial Candidate
       |
       v
delete 5 Resume artifacts + update 25 live surfaces + 2 assurance modules
       |
       +--> manifest/current docs: exactly 10 commands, no alias or tombstone
       +--> clean install: no Resume source, destination, route, or registration
       +--> version-addressed receiver model:
       |      ABSENT / OWNED_EXACT / OWNED_BLOCK / TARGET_CURRENT -> coherent result
       |      FOREIGN_OR_DRIFTED -> whole connected group unchanged + exact refusal
       +--> history: 179 exact task entries; 3 baseline aggregate subsequences retained
       +--> Plan and its two Phase A receivers remain byte-identical to accepted Phase A
       |
       v
immutable Candidate -> independent REVIEW -> accepted landing/integrated checks -> G2 hard stop
```

## Execution Boundary

### Included

- Delete the five exact live Resume artifacts and remove Resume only from the 25 other literal VALUE paths in the Phase B TS.
- Converge the manifest and all four supported adapter surfaces on the ten surviving commands: `plan`, `research`, `handoff`, `review`, `docs`, `knowledge`, `release`, `update`, `config`, `init`.
- Replace fixed “11 commands” instructions with the coherent manifest-defined/current ten-command surface where those statements are live; do not invent another counter-bearing source of truth.
- Replace Resume-presence checks with Candidate-bound command-absence, canonical/receiver parity, clean-install, version-addressed update, history, accounting, Role Lock, and Phase A regression checks.
- Apply the Extract E3 all-preflight ownership classes: `ABSENT`, `OWNED_EXACT`, `OWNED_BLOCK`, `TARGET_CURRENT`, and `FOREIGN_OR_DRIFTED`; preserve foreign/outer bytes and require an empty second run.
- Produce one immutable implementation Candidate and phase-local evidence/RF; route it to the existing independent Reviewer role before any landing.

### Excluded

- Editing `.tfw/workflows/plan.md` or either accepted Plan full-copy receiver; reopening Phase A routing, identity, lifecycle ownership, acceptance, or closure.
- Adding a public/internal Resume substitute, redirect, tombstone, alias, compatibility command, runtime helper, registry, or adapter-owned behavior.
- Creating `.tfw/migrations/<version>.md`, editing `.tfw/CHANGELOG.md` or `.tfw/VERSION`, choosing a version/tag/actor/composition, or starting `/tfw-release`; all remain G2-reserved.
- Rewriting historical task artifacts, existing migration guides, accepted reports, or aggregate history; Phase B Candidate changes none of them.
- Knowledge consolidation, digest-state repair, project-wide configuration repair, TKL work, docs capture, or unrelated cleanup.
- Owner TS approval, Executor/Reviewer dispatch, implementation, review, landing, or release effects from this planning act.

## Live Surface and History Boundary

| Surface | Phase B rule |
|---|---|
| 30 literal VALUE paths | complete implementation mutation set; 5 DELETE and 25 MODIFY |
| 2 literal ASSURANCE paths | only implementation-side test mutation set |
| `workspace/TFW_20260913-151442_RWNR/phase-b/**` | TRACE only; lifecycle, evidence, RF, REVIEW, and journal |
| 179 task-trace entries at `a2363fd` | exact path, mode, and blob identity; digest `ed52c4c26845e90c14a569f867ec2200b18da44374f7df2fd897bf7fb58bef96` |
| `.tfw/CHANGELOG.md`, `KNOWLEDGE.md`, `knowledge/stakeholder.md` | baseline raw-line subsequences remain the long-lived oracle; Phase B itself leaves all three byte-identical |
| existing `.tfw/migrations/**` | historical truth; unchanged in Phase B |

The immutable owner-facing proposal is `30 VALUE files / 650 touched text LOC`. The five deletions account for 287 current logical lines; the remaining budget covers bounded row, managed-block, registration, count, and current-documentation edits without approaching the configured `50 files / 5,000 LOC` prompts. No phase split is useful because the canonical removal, adapter convergence, and absence proof are one connected semantic group.

## Dependencies and Fallback

| Dependency | Phase-B state |
|---|---|
| Frozen master, A1, and G1 C2 | satisfied by existing governing records |
| Independent Phase A acceptance and integrated landing | satisfied at `d366bb1d6d70cf457acba84d4b5aafeb5c5f5b14` |
| Owner-directed knowledge-gate deferral | satisfied for this planning turn only; defect remains open and out of scope |
| Exact Phase B TS and immutable VALUE denominator | pending explicit owner approval |
| Direct Executor and independent Reviewer dispatches | pending after approval; reuse the established role units |
| Actual release version and version-addressed guide/changelog | reserved for G2 after both phases are accepted, landed, reachable, and integrated |
| C1 | automatic on any missing precondition, scope mismatch, foreign/drifted connected subject, failed proof, Reviewer rejection, or landing mismatch; local `master` keeps the accepted Phase A tree and live Resume |

## Phase-Local Risks

| Risk | Control |
|---|---|
| One stale registration survives the remembered list | two independent pre-work searches, exact 30-path selector, Candidate live-wording scan, and mutant coverage |
| Deletion begins before a foreign/drifted receiver is found | all-subject preflight and before/after connected-group hashes before the first write |
| The future migration guide is invented before G2 | use only an ephemeral pinned-target fixture; no migration/changelog/version path enters Candidate |
| Removing Resume weakens Phase A routing or identity | accepted Plan/receivers are outside VALUE and byte-fixed; Phase A source-derived tests remain green |
| Historical text is scrubbed to make search results clean | exact 179-entry oracle and raw-line aggregate subsequences; historical matches are explicitly allowed |
| A fixed ten-command count becomes the next stale claim | manifest is the structural source; current prose names the set only where the exact set is the contract |
| A partial Candidate is landed after failure | C1 forbids a partial Candidate/landing; Reviewer rejection leaves local `master` at the live-Resume baseline |

## Knowledge Application

All master HL §7.2 citations remain controlling. Phase B directly instantiates rows 5, 7, 10, 12, 14, 16, 18, 23, 24, and 28–32: subtraction follows proof; history remains true; adapter behavior stays canonical and portable; evidence is structural; measurement names its revision; the delivery set comes from searches; and stakeholder F13 supplies direction without waiving no-loss proof. The owner-directed gate exception above authorizes no knowledge mutation and produces no Fact Candidate.

---

*Phase HL — TFW_20260913-151442_RWNR / B: Retire the public Resume surface | 2026-09-13*
