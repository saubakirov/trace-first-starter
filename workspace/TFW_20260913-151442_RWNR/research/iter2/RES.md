# RES — TFW_20260913-151442_RWNR: Focused retirement decision

> **Date**: 2026-09-13
> **Author**: robert, Researcher unit `01a09a9e-6935-7f53-bba3-50b5b08b17da`
> **Status**: 🔬 RES — Iteration 2 complete; G1 recommendation ready
> **Parent HL**: [HL-TFW_20260913-151442_RWNR](../../HL-TFW_20260913-151442_RWNR.md)
> **Mode**: Pipeline / focused

---

## Research Context

This second and minimum-required iteration closed the five proof gaps left by iteration 1: a total routing-only Plan state matrix, exact non-command close/recovery access and authority, owned-only versioned stale removal with ten-command convergence, a split immutable/additive history oracle, and one reproducible counter that includes moved instructions and resolves Plan's size breach. The work is governed by frozen baseline `d375bf6`, iteration-1 producer `e6bcec7`/landing `a27989f`, Coordinator gate producer `50f477d`, and continuing dispatch `1958235` / `journal/20260913-172647__dispatch__93c5.md`. The selected LEAD and direct return remain `robert`, unit `01a09a32-367e-7ea1-a405-9501d17ba270`; G1, the frozen amendment, and G2 remain reserved to owner `saubakirov`. This Researcher claims no amendment, TS, implementation, review, or release authority.

## Briefing

[Iteration 2 Briefing](1_briefing.md) fixed C2 as the candidate to prove, C1 as the fallback, the five gaps as the entire scope, and source/Git/model evidence as the proof method. No user question remained because the continuing dispatch supplied all research steering.

## Decisions

| # | Decision | Rationale |
|---|---|---|
| D1 | Recommend C2 for the owner’s G1 verdict; keep C1 as an automatic fallback. | C2 is the only retirement configuration compatible with Role Locks, one canonical owner, update safety, history, and the Plan design cap. Any failed condition leaves the current Resume command intact. |
| D2 | Put one pure existing-task pre-route gate in Plan before the Knowledge Gate and every Plan write. | The 28-case model covered the entire declared/unknown state space with exact routes and zero input mutation. Plan still performs only inspection, matrix rendering, questions, and routing at this gate. |
| D3 | Preserve `.tfw/conventions.md` → `Closing and record recovery` as the sole close/repair effect owner. | The unique heading already says the Coordinator uses it directly; Review already returns APPROVE/`KNW` to that Coordinator. Plan prints an exact natural-language address and stops. |
| D4 | Require four migration outcomes: `ABSENT`, `OWNED_EXACT`/`OWNED_BLOCK`, `TARGET_CURRENT`, and `FOREIGN_OR_DRIFTED`. | The first model exposed that three classes break repeat idempotence. The corrected seven-case model passed owned deletion, absent Cursor, foreign/unmarked/custom refusal, ten-command install, and second-run no diff. |
| D5 | Freeze the 179 task traces by exact baseline tree entries and protect three aggregates with an exact raw-line subsequence oracle. | The selector and task digest reproduce from `a2363fd`; additive aggregate records pass while edit/reorder mutants fail. One whole-file policy cannot serve both artifact kinds. |
| D6 | Use the repository's strict UTF-8 Unicode `\S+` counter on both baseline and Candidate, and require Plan itself to be ≤1,200. | It reproducibly yields 2,737, not 2,685; no Git revision supplies the frozen operands. Moved candidate lines are counted, and a combined reduction cannot waive the Plan cap. |
| D7 | Classify the counter/baseline/cap correction as a frozen amendment, not a free refinement. | The current 2,685 denominator and “explicit disposition” clause are frozen. Only the resolved owner can supersede them with `B=2,737`, the Candidate formula, and a hard Plan cap. |
| D8 | Recommend no iteration 3. | All research questions now have exact contracts, tested negative branches, and fallback conditions. Real receiver/candidate proof belongs to approved TS execution, not another conceptual iteration. |

## Open Questions

| # | Question | Status | Answer |
|---|---|---|---|
| Q1 | Can Plan cover the full return-state matrix without mutation? | Resolved | Yes as a pure pre-route contract: 28/28 model cases matched and inputs remained exact. Current Plan does not yet implement it. |
| Q2 | How does an interrupted close/repair remain discoverable without a new command? | Resolved | `/tfw-plan <exact task/phase>` inspects, prints the fixed `Coordinator control` address to the unique conventions heading, and stops; Review already uses the direct existing-Coordinator path. |
| Q3 | Can existing and clean receivers converge without deleting foreign files? | Resolved | Yes through the four-class, all-preflight versioned migration; seven corrected model cases passed, including absence, refusal, and repeat. |
| Q4 | Can historical truth accept a new retirement record without rewriting old evidence? | Resolved | Yes: exact bytes for 179 task files, exact ordered baseline raw lines for the three additive aggregates. |
| Q5 | What executable denominator governs H4? | Resolved subject to owner amendment | Strict UTF-8 `\S+`: baseline `2,021 + 716 = 2,737`; Candidate is complete Plan plus added lines in every other surviving instruction source. |
| Q6 | Will the real Candidate pass all gates? | Deferred to implementation, not research | The approved TS must require real temporary receivers, immutable Candidate identity, history oracles, Plan ≤1,200, and counted `C < 2,737`; a miss keeps Resume. |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status entering iteration 2 | RES Status | Evidence |
|---|---|---|---|---|
| H1 | The returning-user job served by `/tfw-resume` is already covered by `/tfw-plan` plus lifecycle-specific commands, so a second public entry has no independent user value. | partly refuted / narrowed | 🟠 literal current-state claim refuted; narrowed value claim confirmed | Current Plan lacks the guards. Under C2, the 28-case table assigns inspection to Plan and every product/control transition to an existing owner, leaving Resume no independent authority or transition. |
| H2 | Every unique resume protection can be assigned to an existing canonical route without widening the wrong Role Lock or creating a replacement public command. | architectural survivor, not empirical | 🟢 confirmed for G1 architecture | R1–R12 map to Plan inspection, lifecycle owners, or the direct Coordinator contract; 9/9 authority assertions passed and Plan stops before close/recovery. |
| H3 | Canonical sources, skills, adapters, manifests, docs, tests, clean installs, and update receivers can remove resume consistently while historical traces remain untouched. | blocked | 🟢 confirmed as an implementable acceptance contract | Four ownership classes, all-preflight refusal, four destinations, singular root, exact ten-command set, second-run convergence, 179-task digest, and three aggregate oracles are specified and mutant-tested. Implementation is not yet claimed. |
| H4 | The surviving design reduces the combined 2,685-word workflow surface and does not solve command count by making plan a larger monolith. | blocked | 🟡 confirmed only after the frozen numeric amendment | The repository counter proves `B=2,737`, moved-text accounting, `C < B`, and Plan ≤1,200. The 2,685 number is irreproducible and cannot remain the executable denominator. |

## G1 Decision Brief

### Recommended verdict

**Approve C2 conditionally at G1, together with amendment A1 below.** Retirement is authorized as an architecture only; Resume remains present until Phase A proves the exact replacement protections and Phase B removes the surface. If A1 is rejected or any acceptance condition fails, select C1 and keep Resume.

### What changes

- `/tfw-plan <task-or-phase>` becomes the sole general entry for both new planning and returning-work inspection.
- Resume's public route, canonical workflow, source skill, four generated command destinations, manifest/config registrations, live documentation, and tests are retired through the normal two-phase plan.
- Product work remains owned by Research, Handoff, Review, Docs, Knowledge, and the direct Coordinator close/recovery contract. No alias, tombstone, wrapper, or generic continuation helper survives.

### How it works: exact behavior preservation

| Resume responsibility | Surviving owner and exact behavior |
|---|---|
| R1 exact selection | Plan resolves the deduplicated active-plus-historical exact-reference union and refuses zero/multiple matches. |
| R2 historical safety | Plan reports historical-only access and stops read-only before matrix, repair, or continuation. |
| R3 state/lineage | Plan reads selected task/phase `status.md`, journal and governing artifacts before routing. |
| R4 phase-local truth | Unselected `PHASES` reads each phase's own carriers; selected phase evaluates its own lifecycle; no task rollup. |
| R5 REVIEW continuity | Plan reads the highest live REVIEW result needed to distinguish incomplete, REVISE, REJECT, APPROVE mismatch, and `KNW`. |
| R6 session identity | Plan resolves selected/acting principals and actual unit only after exact live scope resolves and before questions/routes. |
| R7 close/recovery | Plan emits the fixed `Coordinator control` address and stops; the unique conventions heading alone owns effects. |
| R8 state matrix | The Extract 22-row evidence table is the canonical routing contract, including malformed, blocked, terminal and unknown states. |
| R9 human phase gate | Plan renders the phase matrix, asks which phase, and stops without choosing or writing. |
| R10 lifecycle navigation | `RES`→Research; approved TS/`ONB`→Handoff; `RF`/incomplete `REV`→Review; REVISE→Plan Step 8; APPROVE/`KNW`→direct Coordinator control. |
| R11 write attribution | The pre-route is pure; any later owner resolves its own identity/authority before its permitted writes. |
| R12 Role Locks | Plan inspects/routes only; every lifecycle workflow and the close contract retain current permitted/forbidden artifacts. |

### Exact migration path

1. **G1:** owner rules C2 and A1. Without both approvals, stop with C1.
2. **Phase A TS/implementation:** add the early Plan table; preserve direct control route; implement real scenario/no-mutation tests, the four-class versioned migration behavior, history oracles, and counter. Produce the first tested immutable Candidate only when Plan ≤1,200 and `C < 2,737`.
3. **Independent Phase A review:** verify all table states, Role Locks, exact routes, migration refusal/idempotence, history and arithmetic. A failed claim keeps Resume and returns through the ordinary REVISE route.
4. **Phase B after accepted Phase A:** remove only live Resume surfaces, replace command-presence tests with behavior/absence tests, and retain the migration/changelog history. Do not edit the 179 task traces or any pre-existing aggregate line.
5. **Existing receiver update:** at the owner-selected G2 target version, the pinned version-addressed guide inventories old payload/config/four adapter destinations/managed roots/singular compatibility root; refuses before writes on foreign drift; deletes only old-exact owned subjects; recognizes target-current repeats; verifies ten commands and second-run no diff.
6. **G2:** the owner separately chooses release composition, version/tag/changelog and effects. G1 invents no version and authorizes no release.

### Why and value

Resume owns no unique product transition; it bundles inspection/navigation around existing owners. C2 removes one user choice and one distributed command family while preserving a single obvious return entry, task-local continuity, human phase selection, historical access, Role Locks, and explicit close/recovery. The value is not merely “one fewer command”: it eliminates duplicated public topology and future cross-adapter drift while making continuation behavior structurally testable.

### Cost and risk

- Plan must lose at least 821 existing words before funding the new router to meet 1,200; this is a substantive in-place rewrite with regression risk.
- At least 23 current live paths and four adapter layouts need classified treatment; existing update sync is not sufficient.
- A fresh interrupted close may require a two-step Plan-inspect then selected direct-control request; collapsing those steps would widen Plan or recreate Resume.
- Foreign/custom receiver material must block automatic retirement rather than be overwritten, so some updates will require an authoritative local resolution.
- The frozen 2,685 claim is wrong as an executable measure. Correcting it costs one owner-routed amendment and invalidates any evidence calculated against the unexplained number.
- Research models prove completeness and failure branches, not native adapter behavior or the future Candidate. Those remain mandatory Phase A evidence.

### Rejected alternatives

| Alternative | Why rejected |
|---|---|
| Delete Resume immediately | Current Plan lacks every unique pre-route guard. |
| Manifest/config removal only | Existing receivers retain stale absent-manifest files. |
| Copy Resume into Plan | Violates the 1,200 cap, duplicates lifecycle work, and expands the wrong Role Lock. |
| Permanent redirect/tombstone | Retains an eleventh continuation entry and the same user choice under another form. |
| Hidden generic dispatcher/helper | Recreates Resume without the public name and violates the no-replacement constraint. |
| Put guards in each lifecycle workflow | Repeats exact-selection/state policy across roles and creates drift. |
| Let Plan perform close/repair | Breaks independent acceptance and Plan's artifact boundary. |
| Delete all matching files/text | Rewrites historical truth and overwrites foreign/custom receivers. |
| Freeze all 182 history files whole | Prevents a legitimate additive changelog/knowledge record. |
| Keep 2,685 and count Candidate differently | Produces non-reproducible, non-comparable H4 evidence. |
| Permit an oversized but net-negative Plan | Treats combined subtraction as a waiver of an explicit workflow design rule. |

### Clause-level Project North Star application map

| Clause | C2 application | Failure signal |
|---|---|---|
| NS1 Purpose — inspect material grounds/current result, see remaining authority, continue without chat | exact task/phase state, lineage, REVIEW and route are read before action | route derived from glob/index/chat, missing authority, or user must reconstruct context |
| NS1 contrary condition — output must not obscure purpose, authority, inspectability or continuation | Plan is pure and every effect stays with its named owner | Plan writes close/execution artifacts or a hidden router obscures ownership |
| NS2.1 Purpose before activity | existing-task pre-route runs before Knowledge Gate/planning activity | Plan begins HL/TS work before resolving state |
| NS2.2 Saint-Exupéry — subtraction only after correctness, architecture, modularity, inspectability and continuation survive | retirement waits for state, Role Lock, history, migration and counter gates | deletion/command-count success without behavior proof |
| NS2.3 Questions before premature answers | ambiguous, phase, REJECT, BLOCKED and UNDECLARED cases visibly wait | guessed phase, normalized state, inferred dependency clearance |
| NS2.4 Selected Trace, not transcript | 179 task traces and original aggregate lines remain exact; only material new records add | historical rename/edit or global text scrub |
| NS2.5 Human authority, bounded delegation | owner rules A1/G1/G2; foreign/custom inputs refuse; Plan grants no scope | automatic amendment, overwrite, phase choice, or release |
| NS2.6 Continuation over isolated output | every state has an authoritative route, explicit wait, or terminal close | route gap or generic “resume last” behavior |
| Structural Enforcement | table-driven no-mutation, ownership, history, counter and mutant tests expose violations | prose-only promise or green test that never exercises failure |
| Naming Creates Behavior | one `/tfw-plan` entry and exact `Coordinator control` address cue distinct routing/effect roles | ambiguous “resume” alias or adapter-specific branching |
| Portability | four adapters converge from canonical sources; no runtime/helper/provider dependency is added | one adapter keeps behavior or a vendor becomes memory authority |
| NS3 — not a replacement for human judgment/authority | Plan reports/asks/stops; owner/Reviewer/Coordinator decisions remain distinct | automated approval, acceptance, UNDECLARED repair, or G2 effect |
| NS3 — not maximum-documentation bureaucracy | one command/helper disappears; no new closing artifact/registry/debt list | tombstone, helper, registry, or parallel history manifest as runtime |
| NS3 — no untested capability claims | models are labeled architectural; real Candidate/native receiver evidence stays required | RES described as completed implementation proof |
| Success 1 — authorized participant resumes from durable checkpoint | task-local carriers plus exact matrix replace chat-dependent command choice | missing/malformed carrier silently bypassed |
| Success 2 — material decisions traceable | split oracle preserves old decisions and permits a truthful new retirement record | history rewritten to make retirement look timeless |
| Success 4 — complete, usable, inspectable, placeholder-free result | exact routes, hashes, blobs, formulas, owner gates and fallback are stated | unspecified version, selector, counter, owner, or failure route |
| Where truth belongs | Plan owns current routing mechanics; conventions owns close/recovery; Git/task traces/changelog own history | behavior copied into adapters or current rules rewritten into history |

Supporting project knowledge applies consistently: F3 required the literal H1 and first migration model to be challenged rather than accepted; F45 makes subtraction preferred but conditional on proof; D15 forbids behavior-bearing adapters; D31 leaves research's filesystem continuation with Research; D68 keeps live state task-local instead of replacing Resume with a global registry.

## HL Update Recommendations

> **The researcher classifies, never applies or rules.** The Coordinator may apply free refinements. Amendment A1 must be transcribed to append-only HL §12 as `PROPOSED`, preserving this Researcher origin, then routed to owner `saubakirov` under `HL Contract` rule 8.

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|---|---|
| R1 | §2 Current State | Add the exact `a2363fd` evidence: current Plan lacks the pre-route guards; direct close/recovery already exists; current sync is additive; history splits 179+3; repository counter yields 2,737. | Gather G1–G5 |
| R2 | §7.2 Knowledge Citations | Add the clause-level NS1/NS2/NS3/Success/Where-truth applications and note F3/F45, D15/D31/D68 as tested constraints, not file-only citations. | G1 map; Challenge C1–C6 |
| R3 | §8 Dependencies/Research State | Mark iteration 2 complete and research sufficient; list owner A1/G1 verdict as the next gate rather than another research iteration. | Challenge recommendation |
| R4 | §9 Risks | Add target-current misclassification/idempotence, Plan compression regression, foreign/custom update refusal, and non-comparable 2,685 evidence; attach the exact mitigations. | Challenge C3/C5 |
| R5 | §10 RESEARCH Case | Record H1 literal refutation/narrowed confirmation, H2 confirmation, H3 implementable-contract confirmation, H4 amendment-conditional confirmation, and C2/C1 verdicts. | Challenge C6 |
| R6 | §11 Strategic Insights | Record that decision-ready retirement requires a pure router plus retained effect owners, and that the first three-class migration failed repeat until `TARGET_CURRENT` was explicit. | Extract E1–E3; Challenge C1–C3 |

### Amendment Proposals — frozen sections, resolved-ruler verdict required

| # | § | Type | Proposed change | Evidence | Cost | Alternatives considered |
|---|---|---|---|---|---|---|
| A1 | §3 baseline table/To-Be; Phase A accounting clause; §5 DoD 16 | `SUPERSEDE` | Replace Plan `1,995`, Resume `690`, and combined `2,685` with the named strict-UTF-8 Unicode `\S+` counter and immutable values `2,021 + 716 = 2,737`; define Candidate as complete candidate Plan plus candidate-side added-line tokens in every other changed surviving instruction source, counting generated copies once at source after parity; require `C < 2,737` **and** `W(candidate Plan) ≤ 1,200`; any unclassified moved instruction or miss keeps Resume. No purpose, phase, Role Lock, history, or G2 authority changes. | Baseline blobs `81f7d78…` and `31f3159…`; repeat counts; zero matching Git revisions for 1,995/690; counter/boundary/moved-line mutants in Challenge C5; Design Rules | Owner ruling plus TS/evidence changes; Plan must compress by at least 821 existing words before router additions; previous 2,685-derived evidence cannot be used | Keep 2,685: rejected because no reproducible counter; use 2,737 without amendment: rejected as a silent frozen edit; allow oversized net-negative Plan: rejected because it waives the explicit cap; keep Resume/C1: remains fallback if the ruler rejects A1 or Candidate misses it |

## Fact Candidates

No fact candidates. The dispatch supplied scope/authority, while all substantive findings were discoverable from repository sources, Git objects, or executed models.

## Strategic Insights (Research)

No strategic insights. There was no new human domain correction or briefing exchange in this iteration; the owner-origin facts already cited by the HL remain unchanged.

## Findings Map

```text
                           /tfw-plan <reference>
                                    |
                    pure exact-selection/state gate
                (before Knowledge Gate; repository unchanged)
                                    |
       +----------------------------+-----------------------------+
       |                            |                             |
 invalid/history/terminal       phase choice                  live route
 report owner/stop           matrix -> ask -> stop      Plan | Research | Handoff
                                                            | Review
                                                            v
                                               KNW or recoverable mismatch
                                                            |
                                              print Coordinator control
                                                    and STOP
                                                            |
                                  conventions -> Closing and record recovery
                                  (only Coordinator effects; Reviewer remains
                                   independent; truthful carrier writes only)

 retirement update: pinned version guide -> classify every stale subject
     ABSENT | OWNED_EXACT/BLOCK | TARGET_CURRENT | FOREIGN_OR_DRIFTED
                       |                         |
                 apply + verify             refuse before writes
                       |
       10 commands x 4 adapters -> repeat no diff

 proof envelope: 179 exact task blobs + 3 monotone aggregates
                 + Plan <= 1,200 + complete C < 2,737
                       |
              any failure -----------------> C1 keep Resume
```

## Iteration Status

- **Iteration:** 2 of 2 (min) / 5 (max)
- **Hypotheses tested:** H1 (literal refuted, narrowed confirmed), H2 (confirmed for architecture), H3 (complete implementable contract), H4 (confirmed conditional on A1)
- **Hypotheses deferred:** None. Candidate implementation verification is an execution acceptance obligation, not another hypothesis iteration.
- **Gaps discovered:** the frozen 2,685 denominator has no reproducible repository counter; the first migration model omitted `TARGET_CURRENT` and failed idempotence. Both are closed as A1 and corrected C2 respectively.
- **Superseded decisions:** Iteration-1 D7's “preserve 2,685 as historical denominator while blocking H4” is superseded for recommendation by A1: preserve the old claim in history but require an owner-approved executable denominator of 2,737. Extract's three-outcome migration preflight is superseded by the four-outcome version including `TARGET_CURRENT`. C7's mere Plan disposition is rejected in favor of an actual ≤1,200 gate.

### Open Threads (for next iteration)

No open research threads. Owner A1/G1 rulings and real Candidate evidence are the next lifecycle gates, not iteration-3 topics.

### Recommendation
- [x] **SUFFICIENT** — proceed to `/tfw-plan` to classify these recommendations, route A1/G1 to the owner, and write TS only after valid approval
- [ ] **MORE NEEDED**
- [ ] **BLOCKED**

> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

Iteration 2 converts C2 from a plausible consolidation into a decision-ready, falsifiable architecture. It supplies a complete read-only state matrix, a direct non-command control route with existing authority, an ownership-safe/idempotent migration, exact split-history baselines, and comparable surface accounting with a hard Plan cap. It also found two facts that an optimistic review would have missed: the frozen denominator cannot be reproduced, and a migration that recognizes only old/foreign states fails on its own second run. The self-critique is important: the passing models demonstrate completeness and failure semantics, not a finished product. G1 can now approve the architecture and amendment; only an immutable Phase A Candidate and independent review can prove implementation. Until then—and on any miss—Resume stays.

---

*RES — TFW_20260913-151442_RWNR: Focused retirement decision | 2026-09-13*
