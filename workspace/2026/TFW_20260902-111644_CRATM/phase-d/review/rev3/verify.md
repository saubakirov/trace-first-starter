# Verify rev3 — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF files claimed: 23 Candidate files (21 VALUE + 2 ASSURANCE)
> Files to verify: ⌈23 × 0.42⌉ = 10; verified: 23/23 Candidate files, then 100% of the affected source, assurance, evidence, history, and citation surface after the first discrepancy.

## Verification Log

| # | Source / claim | Independent result | Match |
|---|---|---|---|
| V1 | Approval and Candidate lineage | Approval `b755de9128f2b0442615a4ca8b787761f937bbcd` is an ancestor of Candidate `2363c3d315a855fc0bd6c6dbf683e16bfbaf1726`; Candidate parent is `6a5ee8682c17e5b551cd5d69b64996b42fca5f60`. Candidate is the first Executor VALUE+ASSURANCE commit after approval and before EV/RF/state TRACE. | ✅ |
| V2 | Exact Candidate surface | Candidate modifies exactly the approved 21 VALUE paths and the two ASSURANCE paths, all as text modifications. Every current blob for those 23 paths equals the Candidate blob; no post-Candidate product change exists. | ✅ |
| V3 | Product Baseline replay | Literal approved selector from Baseline `8e68ab37d300122ff110500ad58f354f76b6210f` to Candidate returns 21 members, 459 additions, 462 deletions, 921 touched text LOC, no binary row, and no membership deviation. The actual is 11 LOC below the approved 21/932 forecast. | ✅ |
| V4 | Approval-epoch boundary | Approval→Candidate contains 21 VALUE, 2 ASSURANCE, and four legal Phase-D continuation TRACE paths only. Phase A–C directories, master A7, Phase-D HL, original/rev2/rev3 TS, original/rev2 REVIEW and stage history are byte-exact at the approval epoch; Phase E is absent. | ✅ |
| V5 | Pre-approval WIP preservation | The receipt records the same 20-path map digest before/after fast-forward: `ff36d393785fd6450ac0717603e47ad668e695026ed818454992dc4262be1719`; cached/untracked are 0/0 and incoming TRACE has five paths with zero overlap. The 20 recorded rows are unique. Fourteen recorded blobs remain directly recoverable at Candidate; six were deliberately changed by the approved follow-on work and are receipt-only historical hashes. | ✅ within the recorded pre-act evidence boundary |
| V6 | A5 measurements | Direct execution of the source measurer reproduces active corpus 33,676 against 33,749 and central range 160 against 260; neither crosses. All primary/session route historical caps cross and every charged workflow-local net remains negative. No cap literal or denominator ratchet was found. | ✅ |
| V7 | Rev2 AC-1 declaration/activation | Fourteen source-derived AT-mode cases reproduce their independent expected decisions: manual/ordinary AG stay available, missing approval/commit/LEAD/mandate waits, `—` and missing gate/direct/unit report and wait, and the valid row continues. | ✅ |
| V8 | Rev2 AC-2/AC-3 principal, unit, origin, replacement | Canon, HL/profile/event carriers and workflow consumers keep stable principal, actual unit/address/parent, proposal origin, root grant, owner routes and two-act replacement distinct. Seventy-five Phase-D mutants all change projection before independent rejection. | ✅ |
| V9 | Rev2 AC-4/AC-5 consumers and admission | Plan/Resume/Handoff/Research/Review canon equals all ten accepted copies; Codex managed block equals its template and outside-marker root bytes are preserved. Combined admission admits only the supplied limited profile and requires one native all-eight trial for every additional profile; partial receipts do not compose. | ✅ |
| V10 | Rev3 AC-6 assurance and closure | Targeted integration is 11/11; full configured suite is 667 passed/1 skipped; `git diff --check` exits 0. Candidate remains reachable, and Candidate→dispatch contains EV/RF/state/journal TRACE only. | ✅ |
| V11 | Strict documentation build | Exact command `python -m mkdocs build --strict -f docs/mkdocs.yml --quiet` exits 0. The JSON contains 24 warning tokens; independent `git grep -F -n` replay matches all 24 pre-Candidate/Candidate occurrence pairs with zero mismatches. This establishes token/count equality, not complete build-log equivalence. | ✅ at the exact claimed boundary |
| V12 | AC-7 root/child predicate | Sixteen navigation cases reproduce the intended root Plan/Resume title, ordinary cues for children and invalid/ambiguous sources, and altered-readback reporting. Fourteen root-navigation mutants change projection and are rejected. | ✅ for the modeled cases |
| V13 | AC-7 collision inheritance | Canon defines `BASE` and `LEAD_BASE` separately, then scopes collision to `duplicate(BASE)`. The selected-root rendered title is `LEAD_BASE`, so the required collision suffix is excluded or at minimum left ambiguous. A duplicated qualified root title with stable key therefore has no canonical route to the suffix. | ❌ |
| V14 | AC-7 assurance for collision/fail-soft | `LeadNavigationCase` has neither existing-title nor stable-key inputs; `resolve_lead_navigation()` has no collision branch; the 16 cases include altered readback but no duplicate LEAD title with stable key or without one; the 14 mutants contain no collision target. Older `SessionIdentityCase` collision tests exercise ordinary `BASE`, not the handle-bearing root `LEAD_BASE`. | ❌ |

## Mandatory AC-7 Collision Probe

The expected decisions below come from AC-7's requirement that existing collision/readback/fail-soft
behavior remain for the rendered selected-root title, not from the delivered parser.

| Case | Input | Expected by AC-7 | Current canonical result | Match |
|---|---|---|---|---|
| Duplicate qualified root with stable key | Existing `LEAD · cratm-main · CRATM · D`; selected key `ab7`, competing key `ac9` | `LEAD · cratm-main · CRATM · D · @ab`, then exact readback | Literal collision subject is `BASE`; `LEAD_BASE` is unchanged | ❌ |
| Duplicate qualified root without stable key | Same duplicate, no exposed stable key | report once with `no-key`; continue unclaimed | No collision trigger is defined for `LEAD_BASE`, so the fail-soft branch has no unambiguous entry | ❌ |
| Altered readback | Root LEAD rename reads back a pipe/mutable-name title | report once with `altered-readback`; continue unclaimed | The general Failure clause and current modeled case do this | ✅ |

The collision clause at `.tfw/conventions.md:398` is exact: `duplicate(BASE)+exposed(stable-key)`.
`LEAD_BASE` is defined at line 378 and selected at line 386. The distinction is material because the
new title adds the handle before TASK and cannot be treated as the already-defined `BASE` grammar
without silently erasing that definition.

## Commands Executed

| # | Command / method | Result |
|---|---|---|
| 1 | `git show` / `git diff --name-status` / `git diff --numstat` across approval, Baseline, Candidate, EV/RF and dispatch tips | Exact lineage, 23 Candidate files, 21/921 accounting, legal TRACE boundaries |
| 2 | Blob-by-blob Candidate/current and canonical/copy comparisons | 23/23 current product/assurance blobs exact; five canonical workflows equal ten copies; managed block exact |
| 3 | WIP receipt parse plus `c1809cd4…`→`89ed24bd…` incoming path replay | 20 recorded WIP paths, five incoming TRACE paths, zero overlap; exact recorded digest before/after |
| 4 | Direct `phase_d_attention_payload()` execution | Active corpus 33,676/33,749; central 160/260; route and workflow-local figures match the attachment |
| 5 | `--phase-d-scenarios`, `--phase-d-mutants`, `--session-identity-scenarios`, `--session-identity-mutants` | 14 mode cases, 75 Phase-D mutants, 16 navigation cases, 14 navigation mutants; all modeled expectations hold |
| 6 | Independent PowerShell `LEAD_BASE` collision/source probe | Stable-key and no-key cases have no canonical `LEAD_BASE` collision branch; altered-readback branch exists |
| 7 | `python -m pytest docs/scripts/test_integration.py -q -k phase_d --disable-warnings --maxfail=1` | 11 passed, 106 deselected in 136.19s |
| 8 | `python -m pytest .tfw/scripts/ docs/scripts/ -q` | 667 passed, 1 skipped in 434.28s |
| 9 | `python -m mkdocs build --strict -f docs/mkdocs.yml --quiet` | Exit 0 |
| 10 | Independent 24-token pre-Candidate/Candidate tracked-Markdown count replay | 24 tokens, 0 count mismatches |
| 11 | `git diff --check` | Exit 0, empty output |

## Claim & Source Checks

| # | Claim | Traced to | Holds? |
|---|---|---|---|
| C1 | Root/child navigation is source-derived | Canon, Plan/Resume, 16 case records, 14 mutants | ✅ for qualification, continuity, child/invalid-source fallbacks and altered readback |
| C2 | Existing collision behavior remains for root LEAD | RF Round 3 Acceptance; EV R3-E7; AC-7 checkbox 4 | ❌ — neither canon nor the LEAD oracle applies collision to `LEAD_BASE` |
| C3 | The 14 root-navigation mutants prove AC-7 | `phase-d-round3-mutants.json`; assurance source | ❌ for complete AC-7 — all 14 target root qualification/continuity/leakage, none collision or no-key behavior |
| C4 | Strict-build warnings are inherited | `phase-d-round3-mkdocs-baseline.json` | ✅ only as 24 token-presence/count pairs; no claim of full-log equality is accepted |
| C5 | Supplied/additional admission is corrected | Canon plus adapter and source-derived admission cases/mutants | ✅ |
| C6 | Historical A–C/revision epochs are protected | Approval/Candidate Git objects and 11 targeted integration tests | ✅ |

All Round-3 RF/EV references resolve. The strict-build attachment's exact evidentiary boundary is
retained: it proves 24 token/count pairs, while the real build's exit 0 proves the build requirement.

## Evidence Verification

| Evidence | Exists? | What it establishes |
|---|---|---|
| Cumulative `evidence/EV__phase-d__team_mode_and_role_assignment.md` | ✅ | All seven Round-3 rows and attachment routes exist; R3-E7 overstates AC-7 completeness because its oracle omits collision |
| `phase-d-round3-accounting.txt` | ✅ | Exact 21-member, 459+462=921 Baseline replay and ancestry |
| `phase-d-round3-wip-preservation.txt` | ✅ | Contemporaneous 20-path before/after digest receipt; later superseded WIP bytes are not all reconstructible from Git after the fact |
| `phase-d-round3-a5.json` | ✅ | Exact active-corpus, route, central-range and workflow-local measurements; independently reproduced |
| `phase-d-round3-scenarios.json` | ✅ | 14 AT cases and 16 root/child cases; no LEAD collision fixture |
| `phase-d-round3-mutants.json` | ✅ | 75 Phase-D and 14 root-navigation mutants; no LEAD collision mutant |
| `phase-d-round3-test-output.txt` | ✅ | Targeted/full/build/diff results; independent full, targeted integration, strict-build and diff replays agree |
| `phase-d-round3-mkdocs-baseline.json` | ✅ | 24 warning tokens and unchanged occurrence counts only; independent count replay agrees |

## Knowledge Citations Verified

All 38 master-HL §7.2 rows, 11 Phase-HL §7.2 rows, and 31 ONB §7 rows were checked: 80/80
rows resolve to existing sources/items and are semantically relevant to the stated application. The 28
explicit local Markdown links in the two HL tables resolve with zero missing paths; `same` and ONB
references were traced to their preceding/source rows rather than treated as standalone links.

PV0 purpose/non-goals and PV1 methodology/success criteria were checked as separate semantic inputs
even where they share `.tfw/README.md`. P2 F37/F38, P3 D63/D72–D82, the relevant P4 canon sections,
P5 F4/F5/F19, P6 F6/F7/F30/F39–F41, and the cited P7 constraint/stakeholder/environment/risk/edition
items all exist and support their applications. No contradiction with current `KNOWLEDGE.md` was found.

## Discrepancies Found

1. **Material AC-7 source gap:** the new handle-bearing selected-root title is `LEAD_BASE`, while the
   inherited collision rule names only `BASE`. A duplicated qualified-root title therefore cannot
   deterministically reach the required shortest-unique stable-key suffix or the no-key fail-soft
   path. This breaches AC-7 checkbox 4 and its evidence/gate requirement.
2. **Assurance gap:** the new source-derived LEAD oracle and its 14 mutants do not model collision at
   all. Green tests therefore establish root qualification and readback failure around, not through,
   the missing behavior.

The discrepancy triggered complete verification of all 23 Candidate files and every required
evidence/history/citation surface. No implementation correction was made.

## Verification Limits

- The WIP receipt is contemporaneous evidence of an ephemeral pre-approval dirty state. Fourteen of
  its 20 hashes remain recoverable at Candidate; the six later-edited WIP blobs were not written as Git
  objects, so their bytes cannot be independently reconstructed after the fact. This limit does not
  create the AC-7 finding and is not restated as stronger evidence.
- The strict-build baseline attachment is not a pre-/post-build log comparison. Only its 24 tracked-
  Markdown token occurrence pairs were independently replayed.
- RTBO/saved-master landing, release/tag/push, Phase E, and knowledge promotion are outside this review.

## Checkpoint

**Self-check:**
- [x] Opened at least 10 files and recorded findings? — 23/23 Candidate files plus all related trace/evidence/history sources.
- [x] Ran at least one build/test command? — full suite, targeted integration and exact strict build.
- [x] Claim & Source Checks filled with primary-source results?
- [x] Every RF AC checkmark verified against actual files/evidence?
- [x] `KNOWLEDGE.md` and all cited PV items checked independently?
- [x] Evidence artifacts opened and evidentiary limits stated?
- [x] Any discrepancy escalated to 100% verification?

Stage complete: YES
