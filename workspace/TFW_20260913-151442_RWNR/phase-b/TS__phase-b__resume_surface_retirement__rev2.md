# TS — TFW_20260913-151442_RWNR / Phase B: Retire the public Resume surface

> **Date**: 2026-09-13
> **Author**: robert, Coordinator unit `01a09a92-18fb-7da1-a639-6a86844bf147`
> **Status**: ✅ APPROVED REVISION 2 — `saubakirov`, 2026-09-14; exact three-ASSURANCE selector and unchanged `30 VALUE files / 650 touched text LOC` authorized
> **Revision**: `2` — supersedes [revision 1](TS__phase-b__resume_surface_retirement.md) after the C1 return
> **Ruling basis**: blocked RF producer `8640044df25027265f9fa451f84a3256d0497f34`; rejected Candidate `6d3f3890ece2f357ab6353d4fd15a28fe4f3767c`; C1 restore `d09d5d49496d13b64552fe99a03821826ae435b6`; exact failure at `docs/scripts/command_entry_eval.py:89-93`
> **Parent HL**: [Phase B derivation](HL__phase-b__resume_surface_retirement.md)
> **Master HL**: [Resume Workflow Necessity and Retirement](../HL-TFW_20260913-151442_RWNR.md)
> **Phase A prerequisite**: [DONE status](../phase-a/status.md) · [accepted REVIEW](../phase-a/REVIEW__phase-a__continuation_responsibilities.md) · integrated closure `d366bb1d6d70cf457acba84d4b5aafeb5c5f5b14`
> **Research**: [Iteration 2 RES](../research/iter2/RES.md) · [Extract E1–E5](../research/iter2/3_extract.md) · [Challenge](../research/iter2/4_challenge.md)

---

## 1. Objective

Retire `/tfw-resume` from the complete live repository and adapter surface now that Phase A's no-loss continuation result is independently accepted, landed, and integrated. The result has exactly ten public commands, preserves Plan and every lifecycle/Role Lock guarantee, migrates only owned receivers through a version-addressed all-preflight contract, leaves history true, and selects C1 automatically on any missing precondition or proof. No release metadata or effect occurs before G2.

## 2. Scope

### In Scope

- Delete the canonical Resume workflow, canonical and installed Codex Resume skills, and installed Antigravity/Claude Resume command copies.
- Remove the Resume row/path/description from exact current configs, manifest, adapter templates/roots, public READMEs, and compatibility documentation.
- Replace the nine live fixed eleven-command statements with manifest-coherent/current ten-command wording.
- Update exactly three existing assurance modules for live absence, ten-command parity, clean installation, version-addressed owned-only retirement, history preservation, complete accounting, failure mutants, Phase A regression, and the configured command-entry evaluator.
- Prove all connected receiver subjects before any destructive action and produce an immutable Candidate plus phase-local evidence/RF for independent review.

### Out of Scope

- Any edit to canonical Plan or its accepted `.agents/workflows/` and `.claude/commands/` Plan copies; any routing, identity, Phase A, lifecycle, Role Lock, close/recovery, or owner-authority redesign.
- A replacement command, alias, redirect, tombstone, compatibility shim, helper, runtime dependency, registry, or adapter-owned semantics.
- Any task trace, accepted artifact, existing migration guide, aggregate-history, knowledge, digest-state, TKL, or unrelated configuration mutation.
- Any change to `docs/scripts/test_command_entry_eval.py`; its 19 failures prove the evaluator defect but do not authorize a test-module edit.
- Importing or mutating concurrent TKL work, or treating a stale shared-history SHA as future landing authority; task-local evidence SHAs remain immutable, while LEAD re-resolves shared history at the actual landing.
- An actual `.tfw/migrations/<owner-selected-version>.md`, changelog/version/tag choice, release actor/composition, `/tfw-release`, push, publish, deploy, or notification; these remain G2-reserved.
- Implementation, review, landing, or G2 authority inferred from the owner approval; each remains with its named lifecycle owner and gate.

## 3. Principles Check

| # | Master HL §7 principle | Enforced by | Gate |
|---|---|---|---|
| P1 | Delete surface, preserve semantics | AC-1, AC-5, AC-8 | no live Resume plus all Phase A guarantees, or C1 |
| P2 | One user job, one obvious entry | AC-1, AC-5 | exactly ten commands and Plan remains the sole continuation entry |
| P3 | Role boundaries outrank convenience | AC-5 | accepted Plan/Role Lock projections remain unchanged |
| P4 | Evidence before retirement | AC-2–AC-8 | preflight, real temporary trees, mutants, immutable Candidate, independent review |
| P5 | Net simplification | AC-1, AC-6 | five deletions, no substitute, `C < 2,737`, Plan ≤1,200 |
| P6 | Canonical first, adapters thin | AC-2, AC-3 | one manifest/canonical topology; exact copies or managed blocks only |
| P7 | History remains true | AC-4 | 179 exact entries and three retained baseline subsequences |
| P8 | No substitute ceremony | AC-1, AC-6 | no new public/internal route, guide before G2, helper, registry, or tombstone |

## 4. Affected Files and Value-Bearing Accounting

| File / selector | Action | Class | Semantic reason / required result |
|---|---|---|---|
| `.tfw/workflows/resume.md` | DELETE | `VALUE` | remove the canonical public Resume behavior source |
| `.tfw/adapters/codex/skills/tfw-resume/SKILL.md` | DELETE | `VALUE` | remove the canonical Codex Resume skill |
| `.agents/skills/tfw-resume/SKILL.md` | DELETE | `VALUE` | remove the installed Codex Resume skill |
| `.agents/workflows/tfw-resume.md` | DELETE | `VALUE` | remove the installed Antigravity Resume command copy |
| `.claude/commands/tfw-resume.md` | DELETE | `VALUE` | remove the installed Claude Resume command copy |
| `.agent/rules/agents.md` | MODIFY | `VALUE` | remove Resume only from the valid managed compatibility block; never delete the file |
| `.agents/rules/tfw.md` | MODIFY | `VALUE` | converge the installed Antigravity persistent root on ten commands |
| `.tfw/adapters/antigravity/tfw-rules.md.template` | MODIFY | `VALUE` | canonical Antigravity managed-root source without Resume |
| `.tfw/adapters/claude-code/CLAUDE.md.template` | MODIFY | `VALUE` | canonical Claude persistent-root source without Resume |
| `.tfw/adapters/codex/AGENTS.md.template` | MODIFY | `VALUE` | canonical Codex managed-block source without Resume |
| `.tfw/adapters/codex/README.md` | MODIFY | `VALUE` | current Codex adapter documentation without the retired skill |
| `.tfw/adapters/cursor/tfw.mdc.template` | MODIFY | `VALUE` | canonical Cursor root without Resume registration |
| `.tfw/adapters/manifest.yaml` | MODIFY | `VALUE` | remove the Resume command record; exactly ten unique commands remain |
| `.tfw/conventions.md` | MODIFY | `VALUE` | remove the current Resume workflow/table surface without changing lifecycle ownership |
| `.tfw/project_config.yaml` | MODIFY | `VALUE` | remove only exact `tfw.workflows.resume: .tfw/workflows/resume.md` |
| `.tfw/templates/project_config.yaml` | MODIFY | `VALUE` | prevent clean initialization from restoring the exact Resume config row |
| `AGENTS.md` | MODIFY | `VALUE` | current root managed command table without Resume |
| `CLAUDE.md` | MODIFY | `VALUE` | current root command table without Resume |
| `README.kk.md` | MODIFY | `VALUE` | current Kazakh public documentation without Resume |
| `README.md` | MODIFY | `VALUE` | current English public documentation without Resume |
| `README.ru.md` | MODIFY | `VALUE` | current Russian public documentation without Resume |
| `.tfw/workflows/init.md` | MODIFY | `VALUE` | replace obsolete fixed eleven-command install claim with manifest-coherent ten-command behavior |
| `.agents/workflows/tfw-init.md` | MODIFY | `VALUE` | synchronize the installed Antigravity Init full copy |
| `.claude/commands/tfw-init.md` | MODIFY | `VALUE` | synchronize the installed Claude Init full copy |
| `.tfw/workflows/update.md` | MODIFY | `VALUE` | replace obsolete fixed count while retaining pinned version-addressed migration authority |
| `.agents/workflows/tfw-update.md` | MODIFY | `VALUE` | synchronize the installed Antigravity Update full copy |
| `.claude/commands/tfw-update.md` | MODIFY | `VALUE` | synchronize the installed Claude Update full copy |
| `.tfw/adapters/README.md` | MODIFY | `VALUE` | current adapter overview states the ten-command topology |
| `.tfw/adapters/claude-code/README.md` | MODIFY | `VALUE` | current Claude adapter instructions state the ten-command topology |
| `.tfw/adapters/antigravity/README.md` | MODIFY | `VALUE` | current Antigravity adapter instructions state the ten-command topology |
| `docs/scripts/command_entry_eval.py` | MODIFY | `ASSURANCE` | remove only `resume` from the hard-coded `REQUIRED_COMMANDS` set and change its exact eleven-command refusal text to the exact ten-command contract |
| `docs/scripts/test_repository_contracts.py` | MODIFY | `ASSURANCE` | exact surface, manifest, receiver, migration, history, accounting, idempotence, and C1 oracles |
| `docs/scripts/test_runtime_context.py` | MODIFY | `ASSURANCE` | retain Phase A routing/identity semantics and reject any Resume substitute or Role Lock drift |
| `workspace/TFW_20260913-151442_RWNR/phase-b/**` | CREATE/MODIFY | `TRACE` | exact phase-local planning, state, immutable journal, ONB, evidence, RF, review stages, and REVIEW; never runtime input |

### Prospective accounting contract

| Fact | Approved value |
|---|---|
| Subject / exact VALUE selector | The 30 literal `VALUE` rows above, in the identical order reproduced by `$valuePaths` below. No path inference or content match may add a VALUE member after approval |
| Exact ASSURANCE selector | `docs/scripts/command_entry_eval.py`; `docs/scripts/test_repository_contracts.py`; `docs/scripts/test_runtime_context.py`. `docs/scripts/test_command_entry_eval.py` is excluded and must remain byte-identical |
| Exact TRACE selector | every path whose repository-relative name starts `workspace/TFW_20260913-151442_RWNR/phase-b/`; no TRACE path is runtime input or Candidate VALUE |
| Baseline / selector source | VALUE baseline remains `d366bb1d6d70cf457acba84d4b5aafeb5c5f5b14`. Revision 1 was approved from proposal `8920124c851fdeff6e3b77cfb729d9ca7ffbe73c` and blob `108863dd978b9e65b713f9d2feb99a8263c16857`. Revision 2 resolves blocked RF producer `8640044df25027265f9fa451f84a3256d0497f34`, rejected Candidate `6d3f3890ece2f357ab6353d4fd15a28fe4f3767c`, and C1 restore `d09d5d49496d13b64552fe99a03821826ae435b6`; its freeze commit and following transition event bind the exact revision-2 blob |
| Candidate rule | First tested immutable Executor commit with all required VALUE+ASSURANCE, before EV/RF/REVIEW/final transition; excluded-only later writes do not move it; later VALUE requires a new Candidate and recomputation |
| Logical VALUE files | `30`; rename = one and no rename is planned |
| Touched text LOC | at most `650` numeric additions + deletions across the 30 literal VALUE paths; record the actual split from `--numstat`; binary/non-text is per-file N/A and none is planned |
| Triggers / disposition | Forecast is below configured `50 files / 5,000 LOC`; the connected command/receiver surface cannot be split without allowing contradictory states, so one Phase B remains. Assurance and C1 address the destructive risk; no configured prompt fires |
| Multiplier / authority | Immutable plan `30/650`; at or above `60 VALUE files` or `1,300 LOC` returns to owner before work. Any additional VALUE path, replacement surface, migration/changelog/version path, or changed architecture/authority also returns to owner. Below `1,300 LOC`, only necessary growth inside the same 30 paths may receive a prospective Coordinator ruling with Goal, Value, outputs, AC, DoF, roles, target, interfaces, trust, and authority fixed |
| Approval epoch / failure | Owner and phase-status owner `saubakirov` directly approved (`разрешаю`) the exact revision-2 change on 2026-09-14: add only `docs/scripts/command_entry_eval.py` as the third ASSURANCE member and change its stale eleven-command/Resume expectation to the exact ten surviving commands. Proposal origin is `{robert, 01a09b39-f0c0-70c0-9b53-6981647e72fb}` from the blocked RF. The immutable VALUE denominator stays `30/650`; missing/mutable/mismatched/late = `BLOCKED`; metric-only N/A; unresolved phase = `INVALID`; `DEFERRED` is non-terminal |

```powershell
$valuePaths = @(
  '.tfw/workflows/resume.md',
  '.tfw/adapters/codex/skills/tfw-resume/SKILL.md',
  '.agents/skills/tfw-resume/SKILL.md',
  '.agents/workflows/tfw-resume.md',
  '.claude/commands/tfw-resume.md',
  '.agent/rules/agents.md',
  '.agents/rules/tfw.md',
  '.tfw/adapters/antigravity/tfw-rules.md.template',
  '.tfw/adapters/claude-code/CLAUDE.md.template',
  '.tfw/adapters/codex/AGENTS.md.template',
  '.tfw/adapters/codex/README.md',
  '.tfw/adapters/cursor/tfw.mdc.template',
  '.tfw/adapters/manifest.yaml',
  '.tfw/conventions.md',
  '.tfw/project_config.yaml',
  '.tfw/templates/project_config.yaml',
  'AGENTS.md',
  'CLAUDE.md',
  'README.kk.md',
  'README.md',
  'README.ru.md',
  '.tfw/workflows/init.md',
  '.agents/workflows/tfw-init.md',
  '.claude/commands/tfw-init.md',
  '.tfw/workflows/update.md',
  '.agents/workflows/tfw-update.md',
  '.claude/commands/tfw-update.md',
  '.tfw/adapters/README.md',
  '.tfw/adapters/claude-code/README.md',
  '.tfw/adapters/antigravity/README.md'
)
git diff --name-status --find-renames=50% -z d366bb1d6d70cf457acba84d4b5aafeb5c5f5b14 <CANDIDATE_SHA> -- $valuePaths
git diff --numstat --find-renames=50% -z d366bb1d6d70cf457acba84d4b5aafeb5c5f5b14 <CANDIDATE_SHA> -- $valuePaths
```

### Prospective scope rulings

The 30 VALUE paths are one connected semantic group. Five exact artifacts delete and the other 25 modify; no VALUE creation or rename is approved. The three assurance modules may change only to prove this result and retain Phase A coverage. No split is useful: deleting canonical payload without registrations, receivers, current docs, evaluator parity, or migration proof would violate the master DoF. Phase-local TRACE never enlarges VALUE.

**Revision-2 ruling.** The Executor's blocked RF established one necessary ASSURANCE constituent outside revision 1: `docs/scripts/command_entry_eval.py:89-93` preserved `resume` and the exact eleven-command contract, causing all 19 configured failures at the rejected Candidate. Owner `saubakirov` directly approved (`разрешаю`) adding only that file and changing only that expectation to the ten surviving commands. Cost is one additional ASSURANCE path and the bounded expectation edit, with no VALUE spend and no denominator change. Keeping C1/live Resume was considered but rejected after the exact repair was identified; modifying `docs/scripts/test_command_entry_eval.py` was rejected because its unchanged tests already expose the defect. This is a rung-2 TS revision and a necessary assurance refinement inside the frozen Goal, Value, outputs, AC, DoF, roles, target, interfaces, trust, and authority; it changes no frozen HL claim.

The rejected Candidate remains evidence, never a starting acceptance. The C1 restore is the coherent pre-work implementation state; the same Executor must create a fresh Candidate containing all 30 VALUE and three ASSURANCE paths and rerun every Candidate-bound gate.

The actual version-addressed release guide is intentionally absent from the selector because G2 alone chooses its version, content, and changelog relation. Phase B proves the owned-only algorithm using a temporary pinned-target fixture and leaves a hard release-readiness stop requiring the eventual G2-selected guide to embody the proven contract.

TKL may independently advance or rewrite shared repository history. This phase neither mutates nor imports that work. Task-local Baseline, rejected Candidate, restore, RF, revision, and future Candidate identities remain immutable evidence; the LEAD must resolve the then-current shared landing target and prove the Phase B producer/content relation at the actual landing instead of requiring equality to a previously observed shared-history SHA.

### Task-local hard constraints

| M1 consequence | M2 object/risk | M3 measure/selector | M4 pre-act check | M5 softer-control gap | M6 change authority |
|---|---|---|---|---|---|
| Prevent a half-retired command surface that cannot be invoked consistently or upgraded safely | complete 30-path live VALUE group and three assurance paths | exact literal path membership; Baseline→Candidate NUL-safe name-status/numstat; live term/count scans | verify Phase A DONE/landing, all baseline objects, exact 30+3 membership, five deletion identities, exact ten-command evaluator expectation, and no newly discovered live surface before first deletion | review after deletion cannot make an incomplete current surface coherent | any miss selects C1; extra VALUE/migration/release path or ≥2× returns to owner; Executor cannot waive |
| Prevent owned deletion from overwriting project/foreign receiver content | canonical payloads, four adapter destinations, persistent roots, singular compatibility root, exact config key | `ABSENT`/`OWNED_EXACT`/`OWNED_BLOCK`/`TARGET_CURRENT`/`FOREIGN_OR_DRIFTED`; full connected-group before/after byte map | classify every selected subject from installed provenance and pinned old identities before any group write | per-file rollback or disclosure cannot prove that an earlier destructive write preserved foreign bytes | `FOREIGN_OR_DRIFTED` refuses the whole group; only owner/project authority may resolve foreign content outside this TS |
| Prevent historical erasure disguised as cleanup | 179 task entries, three aggregate before-images, existing migrations/accepted reports | exact path/mode/blob manifest and digest; raw-line subsequence oracle; Phase B exact-byte diff | materialize immutable `a2363fd` before-images and run history checks before Candidate creation | later prose or Git history cannot restore the accepted working-tree truth for users | no phase role may waive; failure selects C1 and preserves evidence |
| Prevent Phase B from choosing a release | version, guide, changelog, actor, composition, tag, external effects | absence of all release-metadata paths/effects from Candidate; G2 owner event required | inspect Candidate scope and journal before RF/review/landing and stop after integrated readiness | disclosure cannot substitute for the owner's composition/effect decision | only owner `saubakirov` at G2 may authorize; Coordinator/Executor/Reviewer cannot infer |

**Actions (not budget dimensions):** VALUE = 5 DELETE + 25 MODIFY; ASSURANCE = 3 MODIFY; TRACE = deterministic Phase B prefix.
**Immutable owner-approved denominator:** `30 VALUE files / 650 touched text LOC`; never ratchets.

## 5. Acceptance Criteria

### AC-1: Complete live retirement with no replacement

- [ ] Exactly the five approved VALUE paths are absent at Candidate; all 25 MODIFY paths remain and expose no live Resume command, source, target, route, skill, config registration, alias, redirect, or tombstone.
- [ ] `.tfw/adapters/manifest.yaml` contains exactly the ten surviving unique command records: `plan`, `research`, `handoff`, `review`, `docs`, `knowledge`, `release`, `update`, `config`, `init`.
- [ ] Every live fixed eleven-command statement in the nine exact count paths is removed or replaced by manifest-coherent/current ten-command wording; no new duplicate count source is introduced.
- [ ] A case-insensitive repository search reclassifies every `/tfw-resume`, `tfw-resume`, and `resume.md` match as one of the fixed historical/TRACE exemptions; any unclassified live match fails.
- [ ] No public/internal compatibility command, alias, wrapper, helper, registry, or behavior-bearing adapter replaces Resume.

Gate: immutable Candidate tree/path scan, manifest schema/count/uniqueness checks, exact 30-path diff, and mutants that restore each of the five deleted artifacts or one live registration/count.

Evidence: Full — `evidence/phase-b-surface.json` records Baseline/Candidate, actions, manifest records, search matches/classification, and mutant verdicts.

### AC-2: Canonical adapters and clean installation [depends: AC-1]

- [ ] All four manifest adapters resolve every one of the ten commands and no Resume row; exact-copy receivers match sources and managed roots contain exactly one valid marker block with foreign outer bytes unchanged.
- [ ] `.agent/rules/agents.md` is never deleted wholesale; only its single valid `TFW:CODEX` inner block may converge. Missing, duplicate, malformed, or unmarked compatibility roots refuse mutation.
- [ ] A clean installation for each supported adapter creates one valid persistent root and exactly ten unique command destinations, with no Resume path or registration.
- [ ] Cursor command-directory absence before installation is a normal empty-receiver case; selected install creates only the ten current destinations, and an unselected/absent receiver is not treated as drift.
- [ ] Re-entering the clean-install operation from the same source produces an empty diff.

Gate: real temporary receiver trees for all four adapters, source/receiver hashes, foreign-neighbor and marker mutants, destination inventory, and second-run diff.

Evidence: Full — `evidence/phase-b-receivers.json` records each adapter, source/target identities, preflight class, before/after hashes, refusal, and repeat result.

### AC-3: Version-addressed owned-only update [depends: AC-1, AC-2]

- [ ] A temporary pinned target includes one synthetic version-addressed retirement guide that records Resume as retired and enumerates the expected old source identities; the test version is evidence-only and is never written to repository release metadata.
- [ ] Preflight covers both old canonical payload paths, four possible adapter command destinations, selected persistent roots, `.agent/rules/agents.md` when present, and the exact receiver `tfw.workflows.resume` config entry.
- [ ] `ABSENT` and `TARGET_CURRENT` succeed without destructive work; `OWNED_EXACT` deletes only exact retired payload/receiver paths or the exact default config key; `OWNED_BLOCK` replaces only the exact old inner block and preserves outer bytes.
- [ ] Any unknown provenance, changed bytes, duplicate/malformed markers, unmarked live root, non-default/duplicate config value, or other `FOREIGN_OR_DRIFTED` subject preserves every byte and refuses the whole connected retirement group before writes with exact observed/expected identities and next action.
- [ ] After a successful owned update, roots/config match the intended ten-command target, no stale path is recreated, and a second update from the same pinned target has an empty diff.
- [ ] Candidate creates no actual migration guide or changelog/version entry. G2 must select and approve the real version-addressed guide/content before a release update can claim the retirement.

Gate: temporary Git source and receiver projects, all five classes, mixed cross-adapter/config refusal cases, before/after complete-group hashes, pinned-target coherence, and repeat-run diff.

Evidence: Full — the update cases and guide identity live in `evidence/phase-b-receivers.json`; no synthetic version is represented as a release identity.

### AC-4: Historical truth and aggregate preservation

- [ ] Regenerate the sorted 179-entry task-tree manifest from `a2363fd07253ca92410db149b4301432de79be3b` and require digest `ed52c4c26845e90c14a569f867ec2200b18da44374f7df2fd897bf7fb58bef96`; Candidate has identical paths, modes, and blobs.
- [ ] Preserve baseline blobs `403776ef38da18df21a40d665c1ef75001993ff5`, `4f3a90aea1280981edadbd09d24f2e9c72bbe5ba`, and `692822f36de7dc9a2ca699ce99ee2959dd3bba89` only if they resolve to the respectively named aggregates; then require their raw line chunks as exact ordered subsequences at Candidate.
- [ ] Phase B Candidate leaves `.tfw/CHANGELOG.md`, `KNOWLEDGE.md`, `knowledge/stakeholder.md`, all existing `.tfw/migrations/**`, accepted artifacts, and historical tasks byte-identical to Baseline `d366bb1d6d70cf457acba84d4b5aafeb5c5f5b14`.
- [ ] Delete/edit/reorder/re-encode/line-ending mutants fail; historical Resume mentions remain allowed and are never used as proof of a live command.

Gate: Git-object task manifest, path/mode/blob comparison, aggregate path/blob validation, raw line-terminator-preserving subsequence algorithm, exact Phase B diff, and deliberate mutants.

Evidence: Full — `evidence/phase-b-history.json` records all before-images, manifests, digests, comparisons, and mutant outcomes.

### AC-5: Phase A continuation and authority remain intact [depends: AC-1, AC-2]

- [ ] Canonical Plan and its two accepted full-copy receivers have no Baseline→Candidate diff and remain byte-identical to each other.
- [ ] All accepted Phase A routing, lifecycle, identity re-resolution, title/readback, no-mutation, close/recovery address, receiver, and negative scenarios remain green from Candidate.
- [ ] Plan remains an inspector/router and gains no lifecycle, selection, close/recovery, approval, implementation, knowledge, release, or adapter-owned effect.
- [ ] Every former Resume responsibility still has the exact Phase A surviving owner, wait, or terminal state; removal changes discoverability only, not authority.

Gate: accepted Phase A source-derived suites and semantic mutants; exact diff/hash of three Plan paths; Role Lock projection.

Evidence: Full — retained Phase A outputs plus Candidate-bound raw execution in `evidence/phase-b-tests.txt`; EV identifies reused versus newly observed evidence.

### AC-6: Immutable VALUE and retained-instruction accounting [depends: AC-1, AC-5]

- [ ] Baseline→Candidate VALUE diff contains all and only the 30 literal VALUE paths with exactly 5 DELETE and 25 MODIFY actions; the three assurance paths are the only non-TRACE implementation changes.
- [ ] Numeric `--numstat` additions plus deletions across the 30 VALUE paths are at most 650 touched text LOC; actual split and logical file count are recorded. No binary/non-text value path is expected.
- [ ] Reproduce master baseline `B = 2,021 + 716 = 2,737` from the named `a2363fd` blobs. Compute final Candidate `C` as complete Candidate Plan plus candidate-side added-line tokens in every other changed surviving instruction source from `a2363fd` to Candidate, counting a generated copy once at source only after parity.
- [ ] Require `W(candidate Plan) ≤ 1,200` and `C < 2,737`; machine config removals add zero, while every added instructional config/doc/adapter line is classified. Any new or unclassified instruction path fails structurally.
- [ ] The approved `30/650` denominator never moves; a prospective same-path ruling below 2× is recorded before work, while any extra VALUE path, changed target/authority, or ≥2× returns to the owner.

Gate: the NUL-safe commands in §4; strict UTF-8 Unicode `\S+`; zero-context/no-renames added-line scan from `a2363fd`; path/action/classification and parity mutants.

Evidence: Full — `evidence/phase-b-accounting.json` records all SHAs/blobs, selector source, actions, numstat, Plan/C calculation, instruction classification, denominator, rulings, and terminal verdict.

### AC-7: Reproducible Candidate evidence and regression package [depends: AC-1–AC-6]

- [ ] Targeted surface, adapter, install/update, history, accounting, Phase A regression, and mutant tests pass against the immutable Candidate.
- [ ] At Candidate, `docs/scripts/command_entry_eval.py` accepts exactly the ten surviving manifest commands, contains no `resume` expectation, and reports the exact ten-command contract; `docs/scripts/test_command_entry_eval.py` remains byte-identical to the C1 restore and its focused suite passes.
- [ ] Configured collect-only and full maintainer commands over `tools/tests/` and `docs/scripts/` pass; any pre-existing unrelated failure is separated and cannot support acceptance.
- [ ] EV has one row per AC using only `VERIFIED`, `DEFERRED`, `BLOCKED`, or justified `N/A`; every claim resolves to raw evidence and immutable Baseline/Candidate SHAs.
- [ ] Candidate commit contains exactly the 30 VALUE and three ASSURANCE paths. TRACE-only ONB/evidence/RF/REVIEW/journal writes occur after it and never move Candidate. The rejected `6d3f3890ece2f357ab6353d4fd15a28fe4f3767c` Candidate cannot satisfy this revision.

Gate: `python -m pytest docs/scripts/test_runtime_context.py docs/scripts/test_repository_contracts.py docs/scripts/test_command_entry_eval.py -q`; configured `python -m pytest tools/tests/ docs/scripts/ -q --collect-only`; configured `python -m pytest tools/tests/ docs/scripts/ -q`; exact Git scope/accounting replay.

Evidence: Full — `evidence/phase-b-tests.txt` plus the four structured receipts and required EV below.

### AC-8: Automatic C1 fallback and no partial landing [depends: AC-1–AC-7]

- [ ] Before the first destructive edit, verify Phase A terminal/producer lineage, exact Baseline objects, the C1 restore, exact 30+3 selector membership, the stale evaluator lines 89-93 as the authorized repair target, no new live match, all connected receiver ownership, history before-images, and test prerequisites. Any miss records the invariant and stops with the implementation path set identical to the C1-restored state.
- [ ] Any implementation/check failure before Candidate creation restores or abandons all planned VALUE/ASSURANCE edits as one group; TRACE may retain the failure, but no partial retirement commit is created.
- [ ] Any independent REVIEW rejection leaves the Candidate unlanded and preserves the then-current accepted shared branch; the rejected Candidate may remain reachable only as traceable evidence.
- [ ] Any landing/integrated-check mismatch stops before G2, preserves the then-current accepted shared branch, and returns the exact failed invariant to the Coordinator/owner. Concurrent TKL history is re-resolved at landing and is never imported into this phase merely to satisfy a stale SHA equality.

Gate: preflight-failure, mid-application-failure, Reviewer-rejection, and landing-mismatch models assert whole-group path/byte identity and no release route.

Evidence: Full — C1 cases and hashes are recorded in `evidence/phase-b-receivers.json` and summarized independently in EV/RF/REVIEW.

### AC-9: G2 remains the release hard stop [depends: AC-7, AC-8]

- [ ] Phase B Candidate and TRACE contain no release metadata mutation or external effect and make no claim that a real installed receiver can update without the eventual owner-selected guide.
- [ ] Only after Phase B independent acceptance, producer landing/reachability against the shared history resolved at that time, and integrated checks may LEAD prepare the read-only G2 comparison of `RWNR` alone, `RWNR + TKL`, and deferral. TKL remains an independent input, not a Phase B mutation or imported branch.
- [ ] No `/tfw-release` dispatch, migration/changelog/version/tag write, push, publish, deploy, or notification occurs without owner `saubakirov` selecting composition, actor, exact version, migration/changelog contents, tag, and effects.

Gate: exact Candidate/TRACE scope, journal lineage, local `master` ancestry/checks, and absence of a G2 approval event before release routing.

Evidence: N/A for external release effects — they are forbidden in Phase B; readiness and stop evidence belong in EV/RF/REVIEW and later G2 control trace.

### Evidence Artifacts

| File | Description |
|---|---|
| `evidence/EV__phase-b__resume_surface_retirement.md` | required per-AC evidence and terminal verdict |
| `evidence/phase-b-surface.json` | exact 30-path actions, ten-command manifest, live-match classifications, and mutants |
| `evidence/phase-b-receivers.json` | clean install, five ownership classes, connected-group refusal, pinned-guide fixture, and idempotence |
| `evidence/phase-b-history.json` | 179 task entries, aggregate before-images/subsequences, Phase B exact preservation, and mutants |
| `evidence/phase-b-accounting.json` | immutable Baseline/Candidate, selector/approval source, VALUE numstat, Plan/C count, and instruction classification |
| `evidence/phase-b-tests.txt` | exact targeted/configured commands and raw output |

## 6. Technical Guidance

- Treat RES Extract E3–E5 as the exact receiver/history/accounting design and Phase A's corrected tests as prerequisites. The ACs above govern delivery.
- Build the complete preflight observation before changing any connected path. Apply only after every subject classifies; record before/after identities for the whole group, not isolated successes.
- Remove only the exact default config key/value. Preserve other keys and project-owned configuration; never use the owner-directed knowledge-gate exception as mutation authority.
- Keep manifest as structural command authority. Where prose need not make its point with a number, remove the fixed number; tests still require the exact ten-record target.
- Extend existing test helpers and temporary repositories. Add no runtime code, migration engine, alias, or parallel surface registry.
- In `docs/scripts/command_entry_eval.py`, remove only `resume` from the exact `REQUIRED_COMMANDS` set and change only the corresponding eleven-command refusal text to ten; do not edit `docs/scripts/test_command_entry_eval.py`.
- Treat the rejected Candidate and C1 receipts as diagnostic evidence only. Produce and fully test a fresh 30+3 Candidate from the restored implementation state.
- Test a synthetic version-addressed guide only inside an ephemeral pinned target. The real guide filename/content and changelog relation must remain absent until G2.
- Use Git objects, strict UTF-8 reads, NUL-safe diff output, line terminators retained, exact byte maps, and temporary receiver directories. Keep default tests offline.
- Under this approval, commit implementation with exact-path staging over only the 33 VALUE+ASSURANCE paths, after full status inspection. Create no Candidate until all required Candidate-bound checks pass.
- Do not merge, cherry-pick, rewrite, or otherwise import concurrent TKL work into the Executor branch. At future landing, LEAD resolves the current shared history and verifies the exact task-local producer and tree relationship without freezing an incidental shared-master SHA in this TS.

## 7. Definition of Failure

- ❌ Any of the five deleted artifacts remains live, any Resume registration/path/alias survives, or any replacement surface appears.
- ❌ A VALUE path outside the 30-path selector changes, one of the 30 is omitted, action counts differ from 5 DELETE + 25 MODIFY, an ASSURANCE path differs from the exact three-path selector, `docs/scripts/test_command_entry_eval.py` changes, or another unapproved implementation path enters Candidate.
- ❌ Plan or either accepted Plan receiver changes, a Phase A scenario regresses, or a lifecycle/Role Lock authority moves.
- ❌ A connected receiver is written before complete preflight, foreign/drifted or outer bytes change, exact config ownership is guessed, or the second run is nonempty.
- ❌ Clean install/update recreates Resume, Cursor absence is treated as an error, or adapters/manifests/current docs disagree about the ten commands.
- ❌ A historical task/blob/mode changes, a baseline aggregate line is deleted/edited/reordered/re-encoded, or an existing migration/accepted report is rewritten.
- ❌ VALUE exceeds `30/650` without a required prospective ruling, reaches `60/1,300` without owner approval, Plan exceeds 1,200, `C ≥ 2,737`, or any instruction addition is unclassified.
- ❌ A real migration guide/version/changelog/tag/actor/effect is inferred before G2, or synthetic test provenance is presented as a release identity.
- ❌ A precondition, test, evidence, review, or integrated-landing proof misses without selecting C1; a partial retirement commit or landing is retained as accepted output.
- ❌ Knowledge/digest repair, TKL, unrelated cleanup, or release work enters this phase without its own authority.

**On failure:** stop the connected mutation, preserve truthful TRACE evidence, and select C1. Before Candidate, leave the implementation paths identical to Baseline; after Candidate rejection, do not land it; after landing mismatch, restore the last accepted local `master` state through the owning Coordinator/LEAD process. Never claim partial retirement.

## 8. Phase Risks

| Risk | Mitigation |
|---|---|
| Literal selector misses a differently worded live surface | baseline path/blob scan plus independent fixed-count scan; Candidate re-scan and unclassified-match failure |
| Test model repeats Phase A's former false-green weakness | temporary repositories are actual inputs; mutants must change observable paths/bytes/routes before rejection |
| Version-addressed proof is confused with release authorization | synthetic pinned version stays ephemeral; Candidate forbids guide/changelog/version paths; G2 owner event is mandatory |
| Delete budget encourages scope compression | exact 30 paths and 650 LOC are independent constraints; no moving instructions to escape accounting |
| Foreign receiver prevents automatic update | all-preflight refuses coherently and reports exact identities/next action; no partial cleanup |
| Current-source cleanup erases historical truth | separate live and 179+3 selectors; Phase B exact-byte preservation is stronger than the long-lived subsequence rule |
| Shared TKL work changes the apparent landing base while Phase B runs | keep TKL outside this phase; preserve task-local immutable evidence and have LEAD re-resolve the then-current shared branch and producer relation at landing |
| G2 starts from unintegrated evidence | require independent approval, reachable producers, current shared-branch landing, and integrated checks before the comparison |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|---|---|---|
| `.tfw/workflows/plan.md`, `.agents/workflows/tfw-plan.md`, `.claude/commands/tfw-plan.md` | Phase A VALUE; Phase B read-only dependency | byte-fix the independently accepted Plan result; no Phase B edit permitted |
| `docs/scripts/test_runtime_context.py` | Phase A ASSURANCE | retain corrected source-derived routing/identity behavior while removing only Resume-surface expectations |
| `docs/scripts/test_repository_contracts.py` | Phase A ASSURANCE | reuse corrected receiver/history/accounting oracles and bind them to the Phase B Candidate |
| `.tfw/CHANGELOG.md`, `KNOWLEDGE.md`, `knowledge/stakeholder.md` | later G2/knowledge may append under separate authority | Phase B leaves them byte-identical; long-lived oracle preserves baseline raw-line subsequences |

---

*TS — TFW_20260913-151442_RWNR / Phase B: Retire the public Resume surface | 2026-09-13*
