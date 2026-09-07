# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> Min verify ratio: 0.42
> RF Candidate-II product/assurance files claimed: 14
> Files verified: 14 of 14 (100% after discrepancies)

## Verification Log

### V1: `.tfw/workflows/{handoff,research/base,review}.md`
- **RF claim:** the three live TFW-54 promises are replaced by the one approved optional-principal sentence; each workflow is shorter.
- **Actual:** the exact sentence occurs once in each canonical workflow, the retired sentence occurs zero times, and independent `Measure-Object -Word` counts reproduce 2051→2024, 1167→1140, and 2122→2095.
- **Match:** ✅

### V2: six `.agent/workflows/` and `.claude/commands/` receivers
- **RF claim:** each accepted copy is byte-identical to its canonical workflow.
- **Actual:** the three independently computed SHA-256 triples are respectively `46d25df…`, `f1d62fbb…`, and `7cde168f…`; every triple is byte-identical and each copy contains the exact new sentence once.
- **Match:** ✅

### V3: `.tfw/glossary.md`
- **RF claim:** five terms are minimal routers to one normative owner.
- **Actual:** AT, Principal, Initiation Chain, Worktree Protocol, and Landing Commit each have one `Authority` link and no numbered procedure, `MUST`, `STOP`, or copied table.
- **Match:** ✅

### V4: `phase-b/HL__phase-b__named_principals.md`
- **RF claim:** B9 targets the real `#11-strategic-insights-planning-free` anchor.
- **Actual:** the old target is absent, the corrected target occurs once, and strict MkDocs exits 0.
- **Match:** ✅

### V5: `evidence/phase-e-3.0.0-release-package.md`
- **RF claim:** a complete, exact, replayable and recoverable six-file release package.
- **Actual:** the embedded patch parses once, applies in ledger order, yields exactly six staged paths / 177 additions + 3 deletions, and all six postimage SHA-256 values match. The operational wrapper is not complete: it creates `$releaseTree` at pre-Candidate `b0bfcd2…`, executes Python/MkDocs in the caller CWD, does not stop/propagate each native-command failure, deletes the patch before the documented rollback, and carries two misleading migration claims.
- **Match:** ❌ partial bytes, failed AC-4 operation/semantics

### V6: `docs/scripts/test_integration.py`
- **RF claim:** current behavior is separated from immutable snapshots and the package/successor is protected.
- **Actual:** immutable Phase-D/K1 separation is repaired and Candidate-II tests pass before release. Lines 2829–2836 nevertheless require the live current tree to retain all six pre-release states forever. After applying the exact package to Candidate II, the named test fails because `.tfw/migrations/3.0.0.md` legitimately exists.
- **Match:** ❌ AC-5 forbids a whole/current-state assertion that rejects an approved successor

### V7: `docs/scripts/test_runtime_context.py`
- **RF claim:** exact optional-writer positive/no-binding behavior, copy parity, historical/current separation, and mutants.
- **Actual:** the source-derived checks exercise the exact sentence, omit `writer` without a resolved principal, never infer `robert`, preserve baseline history, and reject three semantic mutants.
- **Match:** ✅

All fourteen Candidate-II paths were opened directly or compared byte-for-byte. Candidate II's own commit changes exactly the twelve approved VALUE and two approved ASSURANCE paths. The later EV/RF/dispatch line changes TRACE only.

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `git show`, `git rev-list --first-parent`, `git merge-base --is-ancestor` over baseline/K1/approval/dispatch/Candidate/EV/RF/review dispatch | Exact linear ancestry and object IDs reproduced; Candidate tree is `35e38510…`. |
| 2 | `python tools/tfw_doctor.py knowledge-pending` at detached K1 `e06a84d…` | Exit 0; `pending_task_ids: []`; CRATM digest `3ec4fae5…`. |
| 3 | K1 path/numstat/blob/marker/state checks | Exact ten VALUE paths / 97 LOC plus TRACE; nine marker additions across eight sources; 169/75/94/359/606/231; `KNOWLEDGE.md` blob stays `0325a157…`. |
| 4 | Candidate-II exact diff and accounting | Own commit has 14 paths; fixed VALUE selector is 12 paths / 417+37=454 LOC; ASSURANCE selector is exactly two paths; no binary N/A. |
| 5 | Canonical/copy SHA-256, stale census, and `Measure-Object -Word` | Three exact triples; current stale count 0, immutable baseline count 3; 2024/1140/2095 after counts. |
| 6 | Exact 46-path union reconstruction and `957f7be…→6c93e81…` numstat | 46 unique paths; 38 currently changed; 2247+661=2908 LOC; conservative `+200+180` forecast 3288≤4000. |
| 7 | Decode/apply package in detached disposable worktrees at `b0bfcd2…` and Candidate II | Both applications produce exact six-path staged diffs; all six postimage digests match; `git diff --cached --check` exits 0. |
| 8 | `python -m pytest ... --collect-only` from the package-created `b0bfcd2…` release tree | Exit 0 but only **522** tests collected: Candidate-II assurance is absent from that tree. The caller Candidate tree collects 529. |
| 9 | `python -m pytest docs/scripts/test_integration.py -q -k "phase_e_ii_release_destinations_are_protected_and_package_replays"` in Candidate-II-plus-package tree | Exit 1: 1 failed, 131 deselected. Failure at line 2833 because the legitimate new `3.0.0.md` exists. |
| 10 | Package-documented `git apply -R --check phase-e-3.0.0.patch` after its application sequence | Exit 128: package line 91 already removed the patch. |
| 11 | PowerShell native-command sequence with exit 7 followed by exit 0 and no explicit checks | Wrapper exits 0, reproducing the package's failure-masking behavior. |
| 12 | `python -m pytest docs/scripts/test_integration.py docs/scripts/test_runtime_context.py -q -k "phase_e"` at review dispatch | Exit 0: 15 passed, 310 deselected in 298.53s. |
| 13 | `python -m pytest tools/tests/ docs/scripts/ -q --collect-only` at review dispatch | Exit 0: 529 collected. |
| 14 | `python -m pytest tools/tests/ docs/scripts/ -q` at review dispatch | Exit 0: 528 passed, 1 skipped in 767.64s. |
| 15 | `python -m mkdocs build --strict -f docs/mkdocs.yml --quiet` at review dispatch | Exit 0; the disclosed pre-existing warning stream remains non-failing. |
| 16 | `git diff --check` for Candidate and TRACE successors; protected six-path baseline→Candidate diff | Exit 0; canonical release diff is empty at Candidate II. |
| 17 | Search assurance for `provider-homogeneous`, `Claude-only`, `no shared knowledge index`, rollback, and location-changing commands | Zero checks cover the four challenged package semantics. |

Disposable verification root: `E:\TEMP\tfw-phase-e-review-837284e3b4e34b83b1c50bf16b701378`. It contains only detached test worktrees and is not a product or evidence authority.

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|--------------------------|------------------|-----------|--------|
| C1 | “complete, exact, replayable release package” | RF §§1, 3–5; EV E4 | Approved TS AC-4 and executable package bytes | ❌ — exact bytes replay, but the prescribed verification/rollback flow is not executable as claimed. |
| C2 | 529 collected / 528 passed / 1 skipped; 15 Phase-E passes; strict docs 0 | RF §4; completion tests attachment | Independent local configured commands at dispatch | ✅ — all four pre-release figures reproduced. |
| C3 | “no shared knowledge index is maintained” | package migration §4 | `KNOWLEDGE.md` D37/D82, `/tfw-knowledge`, topic-file headers | ❌ — RTBO retired the portfolio cache and numeric line ceilings; semantic `KNOWLEDGE.md` §4 remains maintained. |
| C4 | provider-neutral AT availability without an admission caveat | package changelog/migration §§What this release gives you, 5 | Frozen master §3 claim 9/A6; corrected F11; `stakeholder.md` F15 | ❌ — 3.0.0 admits provider-homogeneous long-lived chains, Codex as the first implementation, no complete Claude-only chain, and cross-provider fresh helpers only. |

## Discrepancies Found

1. **Material — AC-5 successor incompatibility (Rung 1).** `test_phase_e_ii_release_destinations_are_protected_and_package_replays` treats the live current tree as the immutable pre-release snapshot. Exact Candidate-II-plus-package reproduction fails at the first legitimate release creation. This breaches TS AC-5 lines 375–380 and makes G-3/full post-release verification impossible without an unauthorized late assurance write.
2. **Material — AC-4 package execution and rollback are incomplete (Rung 1).** The prescribed disposable tree is the pre-Candidate content baseline, so it lacks the Candidate-II assurance; the three Python/MkDocs commands run in the caller tree, do not individually stop/propagate failure, and therefore test the wrong state. The patch is deleted before the rollback section uses it. Exact reproduction collected 522 tests in the actual release tree, masked earlier native-command failure with a later zero, and produced rollback exit 128.
3. **Material — AC-4 RTBO migration semantics are false (Rung 1).** “No shared knowledge index is maintained” conflates the retired task portfolio cache/unused line ceiling with the retained semantic `KNOWLEDGE.md` §4 index. This is a current migration instruction, not protected history.
4. **Material — AC-4 provider scope is overstated/under-constrained (Rung 1).** The package advertises provider-neutral AT operation and permits an existing stable agent principal without carrying the frozen A6/F11 admission boundary. It omits provider-homogeneous long-lived chains, Codex-first implementation, the unadmitted complete Claude-only chain, and bounded fresh cross-provider helpers.
5. **Evidence limitation, folded into the Rung-1 rerun.** The Candidate commit's exact fourteen-path result is independently proved, but none of RF/EV/attachments captures the claimed `git status`/cached selector/`git commit --only -- <paths>` invocation. The correction round must preserve contemporaneous exact-path staging evidence; this limitation is not needed to establish the four material defects above.

Any discrepancy triggered 100% verification; all Candidate-II product/assurance files and all RF evidence artifacts were checked.

## Evidence Verification

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|----------------|-----------------|----------------|
| E1 | `phase-e-completion-accounting.txt` / K1 | ✅ | ✅ — K1 selector, markers, state, digest, zero-diff `KNOWLEDGE.md`, ancestry, and failed-intermediate disclosure reproduce. |
| E2 | `phase-e-completion-tests.txt` / writer semantics | ✅ | ✅ — sentence, census, word counts, no-binding behavior, and three parity hashes reproduce. |
| E3 | completion tests + EV debt table | ✅ | ✅ — glossary/anchor/protected surfaces and three terminal debt dispositions are present. |
| E4 | package + `phase-e-release-replay.txt` | ✅ | ❌ partial — patch bytes/digests reproduce, but the attachment explicitly leaves and does not verify CWD/exit/rollback/wording scope. |
| E5 | `phase-e-completion-tests.txt` / assurance | ✅ | ❌ partial — pre-release configured gates reproduce, but exact post-release current-state assurance fails. |
| E-accounting | `phase-e-completion-accounting.txt` | ✅ | ✅ — 12/454, exact two ASSURANCE paths, no post-Candidate VALUE, and 46/3288 forecast reproduce. |

## Knowledge Citations Verified

| # | Artifact | Priority + exact citation | Link resolves? | Item exists? | Meaning matches? | Relevant to asserted application? |
|---|----------|---------------------------|----------------|--------------|------------------|-----------------------------------|
| 1 | HL §7.2 | PV0 `.tfw/README.md` NS1–NS3 | ✅ | ✅ | ✅ | ❌ — deleted rollback input defeats recoverable continuation. |
| 2 | HL §7.2 | PV1 methodology values + Success Criteria | ✅ | ✅ | ✅ | ❌ — byte replay did not verify the executable release state. |
| 3 | HL §7.2 | PV2 `philosophy.md` F37/F38 | ✅ | ✅ | ✅ | ✅ — no authority or attention ceiling was widened. |
| 4 | HL §7.2 | PV3 `KNOWLEDGE.md` D54, D73–D83 | ✅ | ✅ | ✅ | ❌ — the package misstates retained semantic knowledge and omits the A6/D83 operational boundary. |
| 5 | HL §7.2 | PV4 HL Contract, VALUE accounting, anti-patterns, Role Locks | ✅ | ✅ | ✅ | ❌ — exact verification/rollback commands do not survive their prescribed flow. |
| 6 | HL §7.2 | PV5 `convention.md` F4/F5/F19 | ✅ | ✅ | ✅ | ✅ — canonical rules/copies/naming are synchronized. |
| 7 | HL §7.2 | PV6 `process.md` F30/F39–F41 | ✅ | ✅ | ✅ | ❌ — package semantics lack an enforcement site and the current-state test contradicts the release. |
| 8 | HL §7.2 | PV7 `constraint.md` F2/F11/F12 | ✅ | ✅ | ✅ | ❌ — F11's provider boundary is absent from the migration package. |
| 9 | HL §7.2 | PV7 `stakeholder.md` F8; `risk.md` F1 | ✅ | ✅ | ✅ | ❌ — a legitimate release makes the current check noisy; exact-path command evidence is absent. |
| 10 | ONB §7 | PV0 `.tfw/README.md` NS1–NS3 | ✅ via HL | ✅ | ✅ | ❌ — same rollback/recoverability defect. |
| 11 | ONB §7 | PV1 methodology values + Success Criteria | ✅ via HL | ✅ | ✅ | ❌ — claimed exact replay omits actual release-tree verification. |
| 12 | ONB §7 | PV2 `philosophy.md` F37/F38 | ✅ via HL | ✅ | ✅ | ✅ — authority ceiling preserved. |
| 13 | ONB §7 | PV3 `KNOWLEDGE.md` D54, D73–D83 | ✅ via HL | ✅ | ✅ | ❌ — retained knowledge/provider boundaries are not preserved in the package. |
| 14 | ONB §7 | PV4 HL Contract, VALUE accounting, anti-patterns, Role Locks | ✅ via HL | ✅ | ✅ | ❌ — Candidate immutability is correct, executable command contract is not. |
| 15 | ONB §7 | PV5 `convention.md` F4/F5/F19 | ✅ via HL | ✅ | ✅ | ✅ — exact copy/name behavior holds. |
| 16 | ONB §7 | PV6 `process.md` F30/F39–F41 | ✅ via HL | ✅ | ✅ | ❌ — tests and package flow disagree. |
| 17 | ONB §7 | PV7 `constraint.md` F2/F11/F12 | ✅ via HL | ✅ | ✅ | ❌ — provider scope exceeds the cited fact. |
| 18 | ONB §7 | PV7 `stakeholder.md` F8; `risk.md` F1 | ✅ via HL | ✅ | ✅ | ❌ — successor noise and staging-evidence limitation remain. |

All 18 citations resolve, all 18 named items exist, and all 18 meanings/relevance choices are genuine. Four asserted applications hold fully; fourteen expose or share the implementation discrepancies above. No citation is irrelevant or hallucinated.

## Checkpoint

**Self-check:**
- [x] Opened ≥ ⌈14 × 0.42⌉ files and recorded findings? 14/14 opened or byte-compared; 100% after discrepancies.
- [x] Ran at least 1 build/test command? Configured collection, full suite, targeted Phase E, strict MkDocs, package replay, post-release failure, and rollback were run.
- [x] Claim & Source Checks filled — key claims checked against immutable Git objects and primary project authorities.
- [x] Each RF §3 (AC) checkmark verified against actual file? AC-1–AC-3 hold; AC-4 and AC-5 do not.
- [x] KNOWLEDGE.md checked — retained semantic §4 index contradicts package line 251.
- [x] Knowledge Citations verified? Total 18; resolved 18; items/meanings verified 18; irrelevant 0; hallucinated 0; application failures/partials 14.
- [x] Evidence artifacts verified? Total evidence rows 6; verified 4; partial/failed 2; missing 0.

Stage complete: YES
