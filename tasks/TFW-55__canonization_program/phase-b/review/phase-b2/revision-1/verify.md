# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> **Review cycle:** Formal return #1 / revision #1
> **Review target:** `abed57f993e58cb3e6147eda9de8246c5aa1f206`
> **Target parent:** `36075b486ae2adffeb7d19293f16606d3cc22a3f`
> **Contract freeze:** `5dee93d31fde4ee5ea279880137e83fb50fca296`
> Min verify ratio: `0.42`
> RF Executor files claimed: `8`
> Files to verify: `ceil(8 × 0.42) = 4`
> Actual verification: `8/8 (100%)`, plus protected sources, first-cycle review objects, and complete Git lineage.

## Verification Log

### V1: `README.md`
- **RF claim:** The historic practical guide is restored, current mechanics are exact, all newcomer routes remain, and only the TFW-55 board row changes.
- **Actual:** The public prefix is 2,149 words / 250 lines. It retains all nine historic H2 functions, gives Edition choice plus new/existing/configured starts, names `/tfw-plan` as the first workflow command, carries all 11 commands, explains repository/workflow/update mechanics, and provides separate mechanics/philosophy/history/help/repository/author/license routes. `❌ BLOCKED` now matches authoritative sources. The exact public prefix equals freeze `36075b4`; only the normal TFW-55 board transition changes the full target blob.
- **Match:** ✅

### V2: `README.ru.md`
- **RF claim:** A complete natural Russian localization with corrected stop-decision responsibility, canonical lifecycle facts, exact identifiers, and no board.
- **Actual:** All practical blocks and seven newcomer actions are present in idiomatic Russian. Lines 27 and 134 state `ответственность ... за решение об остановке работы`; no unconditional `обязанность остановить работу` remains in production. Commands, paths, URLs, Edition names, destination set, language authority, lifecycle tokens, and board boundary match English. Strict UTF-8 and local-link checks pass.
- **Match:** ✅

### V3: `README.kk.md`
- **RF claim:** A complete natural Kazakh localization with exact mechanics and same-critic acceptance.
- **Actual:** All practical blocks and seven newcomer actions are present; authority remains human, agents are bounded, and the Trace definition preserves selected durable context. Commands, paths, URLs, Editions, destinations, `❌ BLOCKED`, English semantic authority, and no-board boundary are exact. The previously accepted `пен` alternative remains understandable LOW/taste-only and has no functional, factual, authority, or navigation impact.
- **Match:** ✅

### V4: `phase-b/ONB__phase-b2__project_readme_localization.md`
- **RF claim:** Corrective onboarding records exact baselines, scope, protected sources, source gaps, and post-APPROVE D66 disposition.
- **Actual:** The ONB has no blocking question, carries the exact historic/start/freeze objects and scope gate, discloses the missing Iteration 2 target, and leaves stale D66 to post-APPROVE `/tfw-docs`. All 21 unique local Markdown targets resolve.
- **Match:** ✅

### V5: `phase-b/evidence/EV__phase-b2__project_readme_localization.md`
- **RF claim:** EV preserves all deterministic checks while classifying AC-1–AC-9 Evidence exactly as nine `N/A` items.
- **Actual:** E1–E9 are present and every status is `N/A`; there are zero `VERIFIED`, `DEFERRED`, or `BLOCKED` rows. The final tally is `0 VERIFIED / 0 DEFERRED / 0 BLOCKED / 9 N/A`, matching all nine TS Evidence fields. Repository/document checks and bounded critic work are explicitly described as verification, not target-environment or reception Evidence. Its baseline, counts, blobs, link, board, scope, and critic-lineage claims independently reproduce.
- **Match:** ✅

### V6: `phase-b/evidence/LANG_REVIEW__phase-b2__ru.md`
- **RF claim:** The same Russian critic acknowledged its earlier material error and re-read the complete exact return object with unresolved HIGH `0`.
- **Actual:** The report preserves the flawed first acceptance rather than erasing it, explicitly says why accepting `обязанность остановить работу` was wrong, identifies freeze `36075b4` / RU blob `e67f45a7…`, attests a complete exact-object re-read, supplies a fresh English back-translation and invariant table, closes both prior misses, and reports unresolved HIGH `0`. The blob and both corrected production locations reproduce exactly.
- **Match:** ✅

### V7: `phase-b/evidence/LANG_REVIEW__phase-b2__kk.md`
- **RF claim:** The same Kazakh critic re-read the complete new EN/KK objects, closed the lifecycle-token return, and retained only one non-blocking LOW.
- **Actual:** The report identifies freeze `36075b4`, EN blob `78644c95…`, KK blob `42db59ee…`, full exact-object isolation, correct `❌ BLOCKED` parity, both required back-translations, every prior disposition, unresolved HIGH `0`, and the persistent LOW `KK-F-L1` as explicitly non-blocking.
- **Match:** ✅

### V8: `phase-b/RF__phase-b2__project_readme_localization.md`
- **RF claim:** All nine ACs pass after formal return #1; the revision is bounded; Evidence is nine `N/A`; first-cycle review history remains intact.
- **Actual:** RF §§1–10 are complete and consistent with the actual target. It transparently records formal return #1, exact final blobs, all correction dispositions, deterministic checks, scope accounting, observations, no Fact Candidates, Strategic Insights, no-diagram rationale, and coordinator-owned post-APPROVE closure. The claimed `0/0/0/9 N/A` tally and every reproduced count/object/path hold.
- **Match:** ✅

## Commands Executed

| # | Command or check | Result |
|---|---|---|
| 1 | HEAD/status/parent/ancestry inspection; `git merge --ff-only abed57f…` | Clean detached `f02c240…` fast-forwarded without merge commit to exact target `abed57f…`; parent is exactly `36075b4…`; first REVIEW commit is an ancestor. |
| 2 | Historic-prefix extraction from `git show b924926:README.md`; normalized-LF count/SHA | 246 lines, 1,485 whitespace words, SHA-256 `d14f9b89b174a59f8cd3177dfd111147ec2efdfcb3254fd3790788896b11638d`. |
| 3 | Complete historic/final H2 census | Same nine practical H2s. Historic→final: Editions `77→207`, Who `196→181`, Quick Start+FAQ `429→611`, How `142→171`, Inside `166→220`, Adapters `76→90`, Key Concepts `96→240`, Updating `64→66`, Links `71→100`. |
| 4 | Frozen/final word census | EN `2,129→2,149`; Key Concepts `220→240` only for restored Conduct. Final RU `2,039`, KK `2,009`; both 240 lines. No size gate applied. |
| 5 | Cold newcomer and purpose/anti-paraphrase walkthrough over all three guides | Every language answers all seven questions and routes separately. Root H2 topology is practical; essay topology is philosophical; root contains zero `NS1`/`NS2`/`NS3` or essay-section mirrors. |
| 6 | Command/workflow/skill/source scan | Same 11 command identifiers in EN/RU/KK; all 11 have canonical workflow, local skill, and `AGENTS.md` route. Edition, migration, core, adapter, version, update, and license sources resolve. |
| 7 | Markdown/HTML link/anchor/path scan on public surfaces | EN/RU/KK each have 35 unique targets, 27 local, 8 external, zero missing/broken; normalized sets are equal except intended board route. Occurrences are `69/68/68`. |
| 8 | Strict UTF-8, BOM, mojibake, language-switch, board parser | Strict decode passes, no BOM/replacement/common-mojibake hit; switch appears in first six lines; one EN board, zero RU/KK board markers/rows. |
| 9 | Lifecycle parity scan against conventions/glossary/config | EN has two public/board `❌ BLOCKED` occurrences; RU/KK each one; zero `⛔ BLOCKED`. Config pairs `BLOCKED` with emoji `❌`; `REJECTED` distinction remains exact. |
| 10 | Board-tail extraction from start `2a534c70…` and target excluding only the complete `| [TFW-55]…` row | Both normalized-LF SHA-256 values are `02b8e94e0052907a40b129b3a463111017999d81070a933adfde5e4eb7330a37`; TFW-60 row is byte-identical and remains `🔬 RES (Iteration 2)`. |
| 11 | Protected-tree/blob comparisons | `.tfw/README.md` remains `71a4d725…`; master, B.2 HL/TS, Phase A tree, research tree, KNOWLEDGE, and all 11 old-B1 artifacts are unchanged from start. |
| 12 | First-cycle review-object comparison at `f02c240…` vs target | Canonical REVISE blob `314ab803…` and raw map/verify/judge blobs `72f40830…` / `6a023fcd…` / `b0a6c646…` are byte-identical before this new review update. |
| 13 | Critic object lineage | Draft `ff26598`: EN/RU/KK `cc43a3cb…` / `d9f3c7af…` / `d1d5e80b…`; first final `5d7edc0`: `21e7078a…` / `54c24eff…` / `571884b2…`; return freeze `36075b4`: `78644c95…` / `e67f45a7…` / `42db59ee…`. Target preserves the freeze public prefix and both localized blobs. |
| 14 | TS↔EV↔RF Evidence status scan | TS: nine `Evidence: N/A`; EV: 0 VERIFIED / 0 DEFERRED / 0 BLOCKED / 9 N/A; RF and EV final tallies exact and matching. |
| 15 | Full lineage and return-scope diff | Start→target: 12 paths, 9 new/3 modified, 1,826 additions + 66 deletions = 1,892; exactly 8 Executor paths plus 4 first-review paths. Executor-owned subset is 8 paths / 1,520 changed lines, under TS estimate 1,800. `f02c240…abed57f…` touches only 7 permitted Executor paths. |
| 16 | Placeholder and forbidden-scope scan | No template/unresolved delivery placeholder in the five Executor traces. Prompt fill-in markers in the practical Quick Starts are intentional user inputs. No BoK, mechanics, Editions, research, knowledge, docs, visual, Phase A, old B1, or unrelated production change. |
| 17 | Configured lint/test/verify commands | All three configured echo stubs ran successfully; no substantive project runner is configured for this documentation-only target. |
| 18 | Master/ONB citation resolver | ONB: 21/21 unique local links resolve. Master: 13/15 resolve; only pre-existing missing TFW-55 Iteration 2 RES and TFW-54 HL targets remain, both disclosed and outside B.2 return scope. |
| 19 | `git diff --check 2a534c70…abed57f…` | Clean. |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Primary source | Holds? |
|---|---|---|---|---|
| C1 | Historic public prefix is exactly 1,485 words with named SHA | RF AC-1/§4; EV §1 | `b924926:README.md` bytes before `## Task Board` | ✅ exact |
| C2 | Result is the requested practical guide, not a paraphrase or structural mirror of the essay | RF §§1–4 | Master freeze §1/A6 and Root README contract; target root prefix; reviewed `.tfw/README.md` | ✅ all practical functions restored; distinct topology/job; no essay retelling |
| C3 | Editions, commands, lifecycle, paths, and update facts are current | RF AC-4; EV §§5–7 | `editions/README.md`, `.tfw/quickstart.md`, `AGENTS.md`, workflows/skills, conventions, glossary, config, repository tree | ✅ exact, including `❌ BLOCKED` |
| C4 | Russian preserves retained human stop-decision responsibility | RF AC-5; EV E5; RU report | Master DoD 6/Root contract; English definition/How-It-Works; exact RU blob lines 27/134 | ✅ responsibility is for the human decision; bounded agents remain explicit |
| C5 | Evidence classification is nine `N/A`, while checks remain verification | RF §5; EV E1–E9/final; TS AC-1–AC-9 | Approved TS Evidence fields; conventions Evidence/Verification boundary; glossary vocabulary | ✅ exact `0/0/0/9`; no operating/reception Evidence claim |

All 35 unique public targets in every language were resolved, not sampled. External URLs were checked for exact string parity; the README explicitly avoids claiming permanent third-party availability, so live HTTP reachability is not an acceptance/Evidence claim.

## Complete Keep / Update / Add / Remove and Purpose Audit

- The exact 1,485-word historic prefix and SHA were reproduced independently before comparison.
- Every historic practical H2 remains with the same function. The current guide preserves hero/problem, Editions, three audiences/use cases, new/existing/configured starts, FAQ, How It Works, root/core structure, adapters, concepts/lifecycle, update, and links.
- Editions growth (`77→207`) supplies current three-Edition selection, availability, copy-contents safety, and migration. Quick Start+FAQ growth (`429→611`) supplies Edition-first choice, state-safe three-project-state actions, exact commands, current adapters, and bounded corrections to automation/reproduction claims. Key Concepts (`96→220→240`) supplies current lifecycle, roles, modes, budgets, Evidence, trace types, versioning, and the restored historic Conduct function.
- Other additions supply language/semantic authority, current repository/workflow/adapters, bounded human/agent authority, and distinct current destinations. The Who section is shorter than history (`196→181`), showing the ledger was not padded uniformly.
- No material addition lacks a concrete newcomer function, current factual correction, authority correction, or restored historic function. No arbitrary ceiling, compression ratio, preferred band, or target length governed acceptance.
- English uses only a compact methodology/human-authority/selected-Trace definition plus essay route. It does not reproduce NS1–NS3, the essay narrative, trace-first principles, or non-goal exposition.
- Cold newcomer traversal passes independently in EN/RU/KK for project identity, audience, Edition, new/existing/configured installation/init, first `/tfw-plan`, repository/workflow, and separate mechanics/philosophy/history/help/repository/author/license routes.

## Discrepancies Found

No new material discrepancy. Formal return findings 1–3 are closed on the exact target.

Non-blocking conditions remain explicit:

1. `KK-F-L1` (`пен` after the written identifier) is a taste-level allomorph preference accepted by the Kazakh critic; meaning and function are clear.
2. Master/board citations to missing TFW-55 Iteration 2 and master Amendment A2's missing TFW-54 HL pre-date B.2, are not changed by the target, and do not affect the controlling A6/product sources.
3. KNOWLEDGE D66 still describes the owner-rejected compact doorway. The contract and delegation deliberately defer correction until an APPROVE followed by coordinator-owned `/tfw-docs`.

## Evidence Verification

N/A — all nine TS Evidence items are correctly `N/A`, so there are no target-environment Evidence artifacts to verify. The EV file itself exists and its nine-row classification ledger matches TS/RF exactly. Its deterministic repository checks were independently rerun as verification above and establish the bounded document/Git claims without claiming human reception or operating effectiveness.

## Knowledge Citations Verified

| # | Artifact | Citation set | Link resolves? | Item exists? |
|---|---|---|---|---|
| 1 | Master HL §7.2 #1 | `b924926:README.md` | ✅ Git object | ✅ exact prefix reproduced |
| 2 | Master HL §7.2 #2–13 | essay, KNOWLEDGE decisions, topic files, TFW-32, TFW-52, Iteration 1 | ✅ | ✅ all read and applied critically |
| 3 | Master HL §7.2 #14 | TFW-55 `research/iter2/RES.md` | ❌ pre-existing | ❌ disclosed; approved successor contracts govern B.2 |
| 4 | Master HL §7.2 #15–17 | owner-local corpus/architecture/BoK | ⚪ non-repository/N/A | ⚪ approved Phase A successors govern; BoK explicitly excluded |
| 5 | ONB §7 #1–13 | historic object, repository authority, knowledge, prior reviewed traces | ✅ | ✅ |
| 6 | ONB §7 #14 | TFW-55 Iteration 2 | ⚠️ explicitly unavailable | ❌ same disclosed pre-existing gap |
| 7 | ONB §7 #15–17 | owner-local sources and BoK | ⚪ explicitly indirect/N/A | ⚪ not treated as B.2 authority |

Full Markdown-target scan: ONB `21/21`; master `13/15`, with the second pre-existing missing target being the TFW-54 HL link in Amendment A2. All eight required PV topic files were read in full; no additional material contradiction emerged.

## KNOWLEDGE Cross-Check

- D2/D35 support the restored practical root guide as a separate job from the essay.
- D52's Evidence boundary now agrees with TS/EV/RF: document/Git checks are verification and all nine Evidence items are `N/A`.
- D58/D59 capability limits hold: manual fallback, bounded agents, and no automatic truth/availability/self-maintenance promise.
- D66 is visibly stale, unchanged, and explicitly deferred to post-APPROVE `/tfw-docs`; it is superseded history, not acceptance evidence.
- `knowledge/philosophy.md` F35/F36/F42 support frozen-contract fidelity, independent purpose defense, and a materiality threshold. The result serves the owner-approved practical-guide function, and the remaining LOW/pre-existing conditions do not meet the material blocking bar.

## Checkpoint

**Self-check:**
- [x] Opened ≥ `ceil(8 × 0.42)` files and recorded findings? (`8/8`, 100%)
- [x] Ran at least one configured command and substantive deterministic checks?
- [x] Claim & Source Checks filled from primary Git/repository sources; all public citations resolved?
- [x] Each RF §3 AC verified against actual files and exact objects?
- [x] KNOWLEDGE.md and all eight PV topic files checked for contradictions?
- [x] HL §7.2 and ONB §7 citation states independently reproduced?
- [x] Evidence classification verified? (9 TS fields; 9 EV rows; exact `0/0/0/9 N/A`)
- [x] First-cycle raw stages preserved and new cycle written only under `revision-1/`?

Stage complete: **YES**
