# ONB — TFW_20260913-151442_RWNR / Phase B: Retire the public Resume surface

> **Date**: 2026-09-14
> **Author**: robert, Executor unit `01a09b39-f0c0-70c0-9b53-6981647e72fb`
> **Status**: 🟠 ONB — Accepted; no blocking questions
> **Parent HL**: [Phase B HL](HL__phase-b__resume_surface_retirement.md)
> **TS**: [TS Phase B](TS__phase-b__resume_surface_retirement.md)
> **Governing landing/base**: `4539234b55386c6c1ca652f172b2c90f4aa3407c`
> **Approved proposal / TS blob**: `8920124c851fdeff6e3b77cfb729d9ca7ffbe73c` / `108863dd978b9e65b713f9d2feb99a8263c16857`
> **Immutable denominator**: `30 VALUE files / 650 touched text LOC`

---

## 1. Understanding

Phase B removes the complete live `/tfw-resume` command family only after the accepted Phase A continuation result and all destructive preconditions remain provable. The implementation is one connected deletion-led change: delete five exact Resume artifacts, update 25 exact live VALUE paths to a ten-command topology, and modify only two ASSURANCE modules to prove absence, owned-only receiver retirement, history preservation, Phase A non-regression, immutable accounting, C1 fallback, and the G2 stop. Any selector, ownership, history, test, accounting, or authority miss selects C1 and leaves Resume coherent; no partial Candidate is admissible.

### Executor decision and AT identity

**Decision: ACCEPT the exact approved Phase B handoff.** There are no blocking questions and the explicit autonomous grant satisfies the authorization gate.

| Layer | Resolved fact | Authoritative source |
|---|---|---|
| Selected principal / mandate root | `robert`; LEAD/root unit `01a09a32-367e-7ea1-a405-9501d17ba270` (`LEAD · robert · RWNR`) | Frozen master HL §4.1; Phase B dispatch `journal/20260914-002214__dispatch__ba0e.md` |
| This unit | Executor `01a09b39-f0c0-70c0-9b53-6981647e72fb`, exact title/readback `EXEC · RWNR · B` | Direct Phase B dispatch; current Codex title application and direct task readback |
| Parent / direct channel / return | Parent and direct return are LEAD `01a09a32-367e-7ea1-a405-9501d17ba270`; direct Codex task channel | Phase B dispatch `ba0e` |
| Role and bound | `/tfw-handoff` through ONB, implementation, immutable Candidate, EV and RF only | Approved TS; Phase B dispatch `ba0e` |
| Accountable human / writer | owner `saubakirov`; acting principal/writer `robert` | Phase status, declared profiles, approval event and direct dispatch |
| Proposal origin | `{robert, 01a09a92-18fb-7da1-a639-6a86844bf147}` | Phase B dispatches `788c` and `ba0e` |
| Autonomous from | Exact approved Phase B execution after `TS_DRAFT`; not autonomous from review, landing, G2, knowledge, TKL or release | Frozen mandate, approved TS and dispatch |

Shared principal attribution does not merge the LEAD, Coordinator, Executor, or reserved independent Reviewer. This child has no amendment authority. The same Reviewer unit `01a09b82-d0ed-78b1-9b72-42291fd8359e` is reserved only after complete RF.

## 2. Entry Points

- The 30 literal VALUE paths in TS §4 are the complete value-bearing selector: 5 DELETE and 25 MODIFY.
- `docs/scripts/test_repository_contracts.py` owns the manifest, receiver, history, accounting, C1, and current Phase A guard assurance.
- `docs/scripts/test_runtime_context.py` owns retained Phase A route/identity semantics and the no-substitute/Role-Lock projection.
- `.tfw/adapters/manifest.yaml` is the tooling-only structural authority for the four adapters and ten surviving commands.
- `.tfw/workflows/init.md` and `.tfw/workflows/update.md`, plus their exact Antigravity and Claude copies, must converge without inventing a release guide.
- Baseline `d366bb1d6d70cf457acba84d4b5aafeb5c5f5b14`, historical baseline `a2363fd07253ca92410db149b4301432de79be3b`, accepted Phase A Candidate `ddb6fc4a1ab528525abd1020ee2fb562d4e10f65`, and governing base `4539234b55386c6c1ca652f172b2c90f4aa3407c` are the immutable comparison objects.

## 3. Questions (blocking — cannot proceed without answers)

No blocking questions. The TS, owner approval, direct dispatch, selector, denominator, C1 fallback, knowledge exception, and G2 reservation are exact.

## 4. Recommendations (suggestions, not blocking)

1. Repair and independently mutant-check the Phase A live/TRACE classifier before the first deletion, exactly as the approved dispatch requires.
2. Capture one machine-readable preflight receipt in the later evidence showing all 32 implementation paths, source identities, Phase A lineage, connected receiver classes, history before-images, and the no-release boundary before applying the deletion group.
3. Keep the ten-command list structural in the manifest and use concise current wording elsewhere; do not create another normative command-count authority.

## 5. Risks Found (edge cases, potential issues not in TS)

1. Current Phase A assurance measures its broad changed-path set against a much earlier baseline, so phase-local TRACE filenames can look like live Resume mutation. The repair must distinguish TRACE without allowing a live Resume path to escape.
2. Removing the manifest row makes old Resume sources unavailable to target-current tests unless their exact Baseline blobs are read by immutable Git identity; tests must not reconstruct old bytes from the changed worktree.
3. Managed roots contain project-owned outer bytes. Tests must compare the outer prefix/suffix independently of the changed inner block and must refuse duplicate, malformed, or unmarked roots before any group write.
4. The eventual release migration guide is intentionally absent. Candidate-bound update assurance may use only an ephemeral synthetic pinned target and must label it as evidence-only.
5. A repository-wide term scan contains legitimate historical and Phase B TRACE matches. The allowlist must classify these rather than globally scrub them.

## 6. Inconsistencies with Code (spec vs reality)

1. The approved validation baseline is intentionally not green: `test_rwnr_phase_a_resume_and_live_retirement_paths_are_unchanged` treats the two committed Phase B HL/TS TRACE filenames containing `resume` as live implementation because it filters all changed paths only by the substring `resume`. The exact isolated check reproduces one failure. This is the approved first ASSURANCE repair and is not a waived prerequisite.
2. Current install/update text, manifest, persistent roots, public READMEs, and tests still consistently describe eleven commands and the live Resume route. That is the expected Baseline state, not unapproved drift.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|---|---|---|---|
| 1 | `README.md` — How It Works / checkpoint continuation | ✅ | Applied | Candidate preserves task-local state, journal and explicit handoff continuity while deleting only the redundant public entry. |
| 2 | `.tfw/README.md` — NS1 first clause | ✅ | Applied | Preflight and evidence bind purpose, current result, authority and exact next owner. |
| 3 | `.tfw/README.md` — NS1 contrary condition | ✅ | Applied | No hidden router or Plan-owned effect is introduced. |
| 4 | `.tfw/README.md` — NS2.1 Purpose before activity | ✅ | Applied | The accepted Phase A pre-route remains byte-fixed; Phase B starts from its verified landing. |
| 5 | `.tfw/README.md` — NS2.2 subtraction | ✅ | Applied | Deletion occurs only after the complete preflight and all proofs; any miss selects C1. |
| 6 | `.tfw/README.md` — NS2.3 questions before answers | ✅ | Applied | Foreign/drifted ownership and ambiguous carriers refuse rather than guess. |
| 7 | `.tfw/README.md` — NS2.4 Selected Trace | ✅ | Applied | Preserve the 179 task entries exactly and retain the three aggregate before-images as ordered raw-line subsequences. |
| 8 | `.tfw/README.md` — NS2.5 bounded authority | ✅ | Applied | Immutable `30/650`, owned-only deletion, direct parent return and G2 stop remain hard boundaries. |
| 9 | `.tfw/README.md` — NS2.6 continuation | ✅ | Applied | Former Resume responsibilities retain the accepted Phase A owner/wait/terminal routes. |
| 10 | `.tfw/README.md` — NS2.7 proportional assurance | ✅ | Applied | Destructive retirement receives real temporary receivers, exact hashes, mutants, full regression and independent review. |
| 11 | `.tfw/README.md` — NS3 human authority | ✅ | Applied | Candidate performs no approval, acceptance, G2, release or external effect. |
| 12 | `.tfw/README.md` — NS3 no bureaucracy | ✅ | Applied | No tombstone, helper, registry, replacement command or extra value path is added. |
| 13 | `.tfw/README.md` — NS3 no untested claims | ✅ | Applied | Evidence distinguishes structural clean-install/update proof from unobserved native vendor runtime behavior. |
| 14 | `.tfw/README.md` — Where truth belongs | ✅ | Applied | Manifest/config/workflows own current topology; Git and traces retain history; no authority is duplicated. |
| 15 | `.tfw/README.md` — Candor Over Flattery | ✅ | Applied | The known red baseline and any later proof miss are reported as failure/C1, never waived. |
| 16 | `.tfw/README.md` — Structural Enforcement | ✅ | Applied | Absence, path membership, ownership, byte stability, accounting and mutants are executable assertions. |
| 17 | `.tfw/README.md` — Naming Creates Behavior | ✅ | Applied | `/tfw-plan` remains the sole public continuation entry and Coordinator control remains a named non-command route. |
| 18 | `.tfw/README.md` — Portability | ✅ | Applied | All four adapter destinations derive from canonical sources; no vendor-specific runtime becomes authority. |
| 19 | `.tfw/README.md` — Success 1 | ✅ | Applied | Retained Phase A tests prove continuation from durable task-local carriers. |
| 20 | `.tfw/README.md` — Success 2 | ✅ | Applied | Existing traces and historical statements remain exact and reviewable. |
| 21 | `.tfw/README.md` — Success 4 | ✅ | Applied | Candidate, receipts and RF must be complete, reproducible and independently reviewable. |
| 22 | `knowledge/philosophy.md` — F3 critical opponent | ✅ | Applied | Destructive assumptions are attacked with foreign, malformed, restored-surface, history and scope mutants. |
| 23 | `knowledge/philosophy.md` — F45 subtraction/artifact budget | ✅ | Applied | Five artifacts are deleted with no substitute or new runtime artifact. |
| 24 | `KNOWLEDGE.md` — D15 thin adapters | ✅ | Applied | Adapter copies/blocks remain projections; no adapter receives behavior. |
| 25 | `KNOWLEDGE.md` — D31 filesystem state/research continuation | ✅ | Applied | Research continuation remains owned by `/tfw-research`; no Resume logic is moved there. |
| 26 | `KNOWLEDGE.md` — D68 task-local live state | ✅ | Applied | No index, registry or global Resume replacement is introduced. |
| 27 | `.tfw/conventions.md` — HL Contract rules 3, 8, 12 | ✅ | Applied | Frozen claims, proposal origin and owner gates remain untouched; no amendment is inferred. |
| 28 | `.tfw/conventions.md` — Design Rules | ✅ | Applied | Accepted Plan stays byte-fixed at 1,199 words; added instruction text remains classified under the complete C calculation. |
| 29 | `.tfw/conventions.md` — prohibited Role Lock/history/routing patterns | ✅ | Applied | Executor writes no HL/TS/REVIEW and no historical event or task trace is rewritten. |
| 30 | `knowledge/process.md` — F37 measurement method/revision | ✅ | Applied | Every count names its baseline, exact command, selector and immutable Candidate. |
| 31 | `knowledge/process.md` — F39 delivery set is search-derived | ✅ | Applied | Independent path/content/count scans precede mutation and classify every candidate-side match. |
| 32 | `knowledge/stakeholder.md` — F13 Resume obsolete | ✅ | Applied | Supplies deletion value but does not waive no-loss evidence, C1 or independent acceptance. |
| 33 | `.tfw/conventions.md` — Session identity and AT continuation | ✅ | Applied | Exact Executor title/readback, actual unit, parent/channel, mandate, origin and direct return were re-resolved before work. |

No additional Project Value item was found beyond the 33 cited applications. The owner-directed Knowledge Gate exception produces no knowledge change or Fact Candidate.

---

*ONB — TFW_20260913-151442_RWNR / Phase B: Retire the public Resume surface | 2026-09-14*

## 8. Return Round 2 — Approved evaluator assurance correction

### 8.1 Return decision and identity

**Decision: ACCEPT revision 2 with no blocking questions.** Phase state is `TS_DRAFT`; governing TS
`TS__phase-b__resume_surface_retirement__rev2.md` is frozen at
`e5efd3e608975184995d254bc5eb84176b8b4451`, blob
`8c06e15e3ad8211195f2d48314d055ad1f111979`, and the direct redispatch is
`journal/20260914-081515__dispatch__8a9a.md` at isolated base
`5d3ed163b45fc64c54effb539e23099a9683dfca`.

The same actual Executor is `01a09b39-f0c0-70c0-9b53-6981647e72fb`; its title was reapplied and read
back exactly as `EXEC · RWNR · B`. Acting principal/writer remains `robert`, owner/on_behalf_of remains
`saubakirov`, and parent/direct return remains LEAD `01a09a32-367e-7ea1-a405-9501d17ba270` through
the direct Codex task channel. The revision-2 proposal origin is
`{robert, 01a09b39-f0c0-70c0-9b53-6981647e72fb}` from the blocked RF; this origin grants no amendment
authority. Autonomous scope is ONB, the approved 30-VALUE plus three-ASSURANCE implementation, a fresh
immutable Candidate, revised evidence, and cumulative RF only. Review, landing, TKL, G2, knowledge,
release, and external effects remain excluded.

### 8.2 Resolved correction and entry points

Revision 2 leaves all frozen Goal, Value, interfaces, roles, 30 VALUE members, five DELETE plus 25
MODIFY actions, and the immutable `30 files / 650 touched text LOC` denominator unchanged. It adds only
`docs/scripts/command_entry_eval.py` as a third `ASSURANCE` path. The authorized production edit is
exact: remove only `resume` from `REQUIRED_COMMANDS` and change only the associated refusal text from
the eleven-command to the ten-command contract. Existing assurance paths remain
`docs/scripts/test_repository_contracts.py` and `docs/scripts/test_runtime_context.py`.
`docs/scripts/test_command_entry_eval.py` is explicitly excluded and must remain byte-identical.

The rejected Candidate `6d3f3890ece2f357ab6353d4fd15a28fe4f3767c` supplies diagnostic design only; it cannot satisfy this
round. The coherent C1 restore `d09d5d49496d13b64552fe99a03821826ae435b6` is an ancestor of the
redispatch base. Current evaluator blob `b846b6c0f41bdbe47c0fe3f5105e235665c5ac5b` and excluded-test blob
`7f195b31c622ac8cdbd7dad0a0f2e9ae7fa7a539` match that restore, and current evaluator lines 89–93
contain the exact approved stale `resume` / eleven-command expectation.

### 8.3 Questions, recommendations, risks, and citations

No blocking questions remain. Reuse the independently tested revision-1 implementation shape only as
diagnostic input, generate a fresh patch and Candidate from the restored state, bind every proof to the
new Candidate, and add a byte-identity oracle for the excluded test module. The principal new risk is
accidentally treating the earlier Candidate receipts as current evidence; every mutable Candidate-bound
receipt and test result must be regenerated. Concurrent TKL/shared-master history must not enter this
lineage and will be re-resolved by LEAD only at landing.

The 33 knowledge applications in §7 remain unchanged and applicable; revision 2 changes assurance
coverage, not project-value interpretation. In particular, Structural Enforcement now includes the
command-entry evaluator, F3 still requires hostile mutants, F37 still requires fresh Candidate-bound
measurement, and NS2.5 still enforces the immutable 30/650 VALUE authority. No new Project Value item,
fact candidate, or strategic insight is introduced by the returned correction.

---

*ONB return round 2 — TFW_20260913-151442_RWNR / Phase B | 2026-09-14*

## 9. Return Round 3 — Real AC-8 recovery models

### 9.1 Return decision and identity

**Decision: ACCEPT the closed rung-1 return with no blocking questions.** Phase lifecycle is `RF`,
the governing artifact remains `TS__phase-b__resume_surface_retirement__rev2.md` with exact blob
`8c06e15e3ad8211195f2d48314d055ad1f111979`, and the sole Coordinator ruling is live REVIEW §4.1.
Durable dispatch is `journal/20260914-103334__dispatch__8fa9.md` at clean detached base
`8209049faaa2fca443ca503999cac5c2764a521b`, tree
`012e2cf56f3c16554cdf2d2a5953748deb0743e3`, whose direct parent is independent Reviewer producer
`efa7cdd2ad66856d2be5e5799a82ba67e4c1b7cc`.

The same actual Executor remains `01a09b39-f0c0-70c0-9b53-6981647e72fb`; title was reapplied and read
back exactly as `EXEC · RWNR · B`. Acting principal/writer is `robert`, owner/on_behalf_of is
`saubakirov`, selected LEAD/parent/direct return is `01a09a32-367e-7ea1-a405-9501d17ba270`, and the
accepted correction origin is `{robert, 01a09b82-d0ed-78b1-9b72-42291fd8359e}` in the independent
Reviewer unit. The current Coordinator-task delivery repeats the already durable bound and supplies no
additional authority. Autonomous scope is this rung-1 ONB, the ruled assurance correction, a fresh
exact 30+3 Candidate, affected evidence, and cumulative RF only.

### 9.2 Closed implementation bound

Replace only the declarative `rwnr_phase_b_c1_decision()` proof inside approved ASSURANCE path
`docs/scripts/test_repository_contracts.py` with real temporary-tree execution for four cases:
preflight refusal; injected mid-application failure after at least one connected-group write; Reviewer
rejection; and landing/integrated mismatch. Each model derives the full approved 30+3 path/byte map,
compares the observed final map with the required coherent before-image, and observes an empty release
route/effect set. Three hostile mutants—altered path, one retained deletion, and emitted release
route—must independently fail the oracle.

Rejected Candidate `6d6d094ac5325377772f26ddf314b965c1dfd135` remains unaccepted/unlanded evidence. The current
retired implementation will first be restored as one exact 30+3 group to coherent C1 bytes on this
lineage; only then will the complete 30 VALUE plus three ASSURANCE result be reapplied with the real
AC-8 proof and frozen as a fresh Candidate. Before that Candidate commit, preserve literal full
`git status --short --untracked-files=all`, empty-index output, the exact staging command/path list, and
the 33/33 cached-set audit; after commit, preserve exact immutable scope.

### 9.3 Questions, recommendations, risks, and citations

No question or scope conflict remains. The primary risk is another false-green abstraction: scenario
success must be computed from filesystem bytes and emitted routes, never assigned as a Boolean claim.
The injected failure must occur only after at least one actual group write, then restore the complete
map. Reviewer/landing rejection models must begin from retired Candidate bytes and restore the same
coherent baseline map. Mutation checks must change observable path/byte/effect output before the oracle
rejects them.

Prior ONB questions and all 33 §7 knowledge applications remain resolved and applicable; this round
changes only AC-8 assurance strength. Structural Enforcement, F3 critical-opponent testing, NS2.5
bounded authority, and F37 measurement remain the deciding applications. No new Project Value item,
fact candidate, strategic insight, selector, denominator, HL/TS claim, knowledge/digest action, TKL,
shared-master operation, G2 decision, or release effect is introduced.

---

*ONB return round 3 — TFW_20260913-151442_RWNR / Phase B | 2026-09-14*

## 10. Return Round 4 — Exact-path Candidate evidence

### 10.1 Return decision and identity

**Decision: ACCEPT the closed rung-1 exact-path return with no blocking questions.** Phase lifecycle
is `RF`; governing TS remains revision 2 with exact blob
`8c06e15e3ad8211195f2d48314d055ad1f111979`; the sole executable Coordinator ruling is live REVIEW
§8.7. Durable dispatch is `journal/20260914-121917__dispatch__ca23.md` at clean detached base
`4b0521c5c7606f3fe6586a1c54ae62bcc33df3a6`, tree
`da9903c0f306da8f3b84cc5925e672d9adcb75d7`. The binding independent REVIEW producer is
`9eaf775cc0ff3a28e3c989e4018d34b3b707eb57`; the preceding LEAD-authorized control transition
`c99a0218bd28e5c076d879ddb453fd2f57b23dff` restored the canonical `RF` prior state without
changing the verdict or product.

The same actual Executor is `01a09b39-f0c0-70c0-9b53-6981647e72fb`; title was reapplied and read
back exactly as `EXEC · RWNR · B`. Acting principal/writer remains `robert`, owner/on_behalf_of
remains `saubakirov`, selected LEAD/parent/direct return remains
`01a09a32-367e-7ea1-a405-9501d17ba270`, and the accepted proposal origin remains
`{robert, 01a09b82-d0ed-78b1-9b72-42291fd8359e}` in the independent Reviewer unit. Autonomous scope
is this appended ONB, exact 33-path byte replay, outside-repository raw boundary receipt, fresh
Candidate, affected evidence, cumulative EV/RF, and phase-local state/journal TRACE only.

### 10.2 Closed implementation and evidence bound

All 33 current implementation paths are byte-identical to independently verified but unaccepted
Candidate `a81e0c12ec982ee4f73639ebf15394ef53877294`; all 33 coherent C1 before-image objects remain
available. The round will first create a TRACE-free coherent C1 implementation-baseline commit on
the current lineage, then reapply the exact 30 VALUE plus three ASSURANCE bytes with no semantic
change. The fresh Candidate must contain exactly those 33 paths and use the actual command form
`git commit --only -- <all 33 literal pathspecs>`; no broad commit, inferred selector, TRACE, evidence,
or unrelated path may enter it.

Before Candidate creation, one raw receipt will be captured outside the repository and retain
verbatim the complete `git status --short --untracked-files=all`, empty
`git diff --cached --name-only`, literal ordered 33-path selector, exact staging command, complete
staged names/actions, and explicit `missing=0` / `extra=0` audit. Immediately after Candidate freeze,
the same outside-repository receipt will append the exact Candidate command/result, complete
post-commit status, and exact Candidate scope. Only then may its bytes be copied into phase-local
evidence and committed later as TRACE. The raw receipt path itself is not a Candidate path.

Every Candidate-bound targeted, configured collection/full, focused evaluator, state, accounting,
and diff gate will be rerun. Cumulative EV/RF will identify the fresh Candidate and preserve every
prior epoch, failure, REVISE, and unaccepted Candidate without overstatement. AC-8 implementation
and every Candidate implementation byte remain functionally and byte-identical to the independently
verified return; this round changes only Candidate creation and evidence integrity.

### 10.3 Questions, recommendations, risks, and citations

No blocking question remains. The principal risk is self-invalidating evidence: writing the receipt
inside the repository before Candidate would add an unauthorized path, while copying it only after
commit without a contemporaneous outside-repository source would reconstruct evidence. The control is
one temporary raw carrier written before commit, extended immediately after the command, byte-copied
only afterward, and checked for equality before TRACE commit. The Candidate command will spell all 33
pathspecs literally and will not rely on a shell variable at commit time.

Prior ONB questions and all 33 HL §7.2 knowledge applications remain resolved because no product,
authority, interface, or oracle semantics change. The deciding applications are P1 Structural
Enforcement (the command and raw boundary must be observable), P1 Candor Over Flattery (no reconstructed
pre-commit claim), P4 Exact-path/Role Lock prohibitions, P6 F37 named reproducible measurement, and
NS2.5 bounded subtraction under unchanged 30/650 authority. No new Project Value item, Fact Candidate,
strategic insight, selector, denominator, HL/TS claim, knowledge/digest action, shared-master/TKL work,
G2 decision, release metadata, or external effect is introduced.

---

*ONB return round 4 — TFW_20260913-151442_RWNR / Phase B | 2026-09-14*
