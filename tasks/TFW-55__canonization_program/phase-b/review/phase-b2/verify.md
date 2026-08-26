# Verify — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact. Open files. Run commands. Compare claims against reality.
> **Test:** "If I removed the RF, would the evidence alone prove the work was done?"
> **Review target:** `f8b0731b1624f7ab28f80020519702cb85e6014b`
> **Contract freeze:** `5dee93d31fde4ee5ea279880137e83fb50fca296`
> Min verify ratio: `0.42`
> RF files claimed: `8`
> Files to verify: `ceil(8 × 0.42) = 4`
> Actual verification: `8/8 (100%)` because the first discrepancy triggered full verification.

## Verification Log

### V1: `README.md`
- **RF claim:** The exact 1,485-word historic project-guide function is restored, practical growth is classified, current mechanics are exact, and the live board is preserved except for TFW-55.
- **Actual:** The public prefix is a practical guide, not an essay mirror. It retains every historic H2 function, answers all seven cold-newcomer questions, separates mechanics/philosophy/history/help/repository/author/license routes, and grows descriptively to 2,149 words for concrete Edition, start-state, command, structure, authority, and navigation functions. The board-tail and reviewed-essay gates hold. However, line 209 says `⛔ BLOCKED`; the authoritative status is `❌ BLOCKED` in conventions, glossary, config, and the live Task Board.
- **Match:** ⚠️ partial — purpose and reconstruction hold; AC-4 current-status exactness does not.

### V2: `README.ru.md`
- **RF claim:** A complete, natural, semantically faithful Russian localization with exact mechanics and no authority drift.
- **Actual:** The full practical guide, routes, commands, paths, Edition names, and English-only board boundary are present and generally natural. Line 27 translates `responsibility to stop` as `обязанность остановить работу`, changing retained human responsibility/decision authority into an unconditional duty to stop the work. The Russian critic's own final semantic table repeats that wording and accepts it. Line 201 also uses the non-canonical `⛔ BLOCKED` glyph.
- **Match:** ❌ — material human-authority drift plus a factual lifecycle-token error.

### V3: `README.kk.md`
- **RF claim:** A complete, natural, semantically faithful Kazakh localization with exact mechanics and no authority drift.
- **Actual:** The full practical guide is present and generally natural. The draft HIGH finding was correctly repaired to `жұмысты тоқтату жөніндегі жауапкершілік`; the central and How-It-Works formulations preserve responsibility rather than an obligation to stop. Commands, paths, routes, identifiers, language-source notice, and board boundary match English. The accepted LOW `пен` preference is taste-only. Line 201 nevertheless uses `⛔ BLOCKED` instead of authoritative `❌ BLOCKED`.
- **Match:** ⚠️ partial — semantic localization holds; lifecycle-token exactness does not.

### V4: `phase-b/ONB__phase-b2__project_readme_localization.md`
- **RF claim:** The corrective execution was onboarded against the exact historical baseline, current start/freeze, protected essay blob, scope gate, and source gaps.
- **Actual:** The ONB records those gates, has no unresolved blocking question, preserves the unavailable Iteration 2 citation as a pre-existing observation, and explicitly defers stale D66 to post-APPROVE `/tfw-docs`.
- **Match:** ✅

### V5: `phase-b/evidence/EV__phase-b2__project_readme_localization.md`
- **RF claim:** The EV independently establishes all nine ACs as `VERIFIED`.
- **Actual:** The document contains a strong, reproducible repository-verification record: baseline reconstruction, ledger, newcomer matrix, source table, command/link/board checks, localization lineage, scope, and counts. Three substantive claims are false: current lifecycle exactness (E4), Russian semantic fidelity (E5), and sufficient critic closure (E7). More fundamentally, TS AC-1 through AC-9 each specify `Evidence: N/A`; EV lines 25–33 and 241 relabel deterministic Git/document checks as nine real-environment `VERIFIED` Evidence items. The TS template permits a MAY-deviate choice only with RF justification; the RF records neither the deviation nor a justification, and the cited material does not show target-environment observation beyond repository/document checks.
- **Match:** ❌

### V6: `phase-b/evidence/LANG_REVIEW__phase-b2__ru.md`
- **RF claim:** The same isolated Russian critic closed all draft findings and accepted the complete exact-final object with no open material issue.
- **Actual:** Draft/final commit and blob lineage is exact, all ten recorded draft findings have dispositions, and the critic reviewed the complete exact-final file. The final semantic table itself maps stop responsibility to `обязанность остановить работу` and incorrectly accepts the resulting authority drift. It also did not catch the official `BLOCKED` glyph mismatch.
- **Match:** ❌ — lineage exists, but its substantive acceptance is insufficient.

### V7: `phase-b/evidence/LANG_REVIEW__phase-b2__kk.md`
- **RF claim:** The same isolated Kazakh critic closed all draft findings, including one HIGH authority defect, and accepted the complete exact-final object with only one LOW preference.
- **Actual:** Draft/final commit and blob lineage is exact; all twelve draft findings are dispositioned; the HIGH authority defect is materially corrected in the final text; the retained LOW preference does not affect meaning or function. The exact-final acceptance did not catch the official `BLOCKED` glyph mismatch.
- **Match:** ⚠️ partial — language judgment holds; exact mechanic parity does not.

### V8: `phase-b/RF__phase-b2__project_readme_localization.md`
- **RF claim:** All ACs pass, the eight-path scope is exact, the critic chain is complete, and Evidence is `9/9 VERIFIED`.
- **Actual:** File/scope/count/provenance/board/blob/old-B1 claims reproduce. Sections 7–9 are present and meaningful. The RF nevertheless overstates AC-4, AC-5, AC-7, and the Evidence verdict because it inherits the three discrepancies above.
- **Match:** ❌

## Commands Executed

| # | Command or check | Result |
|---|---|---|
| 1 | `git status --short --branch`; target/parent/object inspection | Began clean at detached target `f8b0731`; target parent `5d7edc01…`; contract freeze object resolves exactly. Review-only files are the only subsequent additions. |
| 2 | Historic-prefix extraction from `git show b924926:README.md`, normalized-LF word/SHA calculation | 246 prefix lines; exactly 1,485 words; SHA-256 `d14f9b89b174a59f8cd3177dfd111147ec2efdfcb3254fd3790788896b11638d`. |
| 3 | H2-section word census at historic source and target | Editions `77→207`; Who `196→181`; Quick Start+FAQ `429→611`; How `142→171`; What's Inside `166→220`; Adapters `76→90`; Key Concepts `96→240`; Updating `64→66`; Links `71→100`. No historic practical H2 was removed. |
| 4 | Target prefix/file word, line, and blob census | EN prefix 2,149 words / 250 lines / README blob `969817f4…`; RU 2,032 / 240 / `54c24eff…`; KK 2,009 / 240 / `571884b2…`; essay blob `71a4d725…`. |
| 5 | Draft/final critic Git-object lineage | Draft `ff26598` and exact-final `5d7edc0` blobs reproduce for EN/RU/KK and both language reports. Target English prefix is byte-identical to the accepted `5d7edc0` prefix; only the board row changed later. |
| 6 | `git diff --name-status`, `--numstat`, and `--check` from execution start `2a534c70…` to target | Exactly 8 authorized paths, 1,349 insertions + 66 deletions = 1,415 changed lines; `git diff --check` clean. |
| 7 | Old-B1 object comparison from execution start to target | ONB, RF, REVIEW, EV, RU/KK reports, and old `review/map.md`, `review/verify.md`, and `review/judge.md` are byte-identical. |
| 8 | Board-tail comparison excluding only the TFW-55 row | Exact normalized-LF SHA-256 equality `02b8e94e0052907a40b129b3a463111017999d81070a933adfde5e4eb7330a37`; TFW-60 remains byte-identical at `🔬 RES (Iteration 2)`. |
| 9 | Markdown/HTML target, anchor, command-set, UTF-8, mojibake, language-switch, and board parser over EN/RU/KK | EN 69 target occurrences/35 unique/0 missing; RU 68/35/0; KK 68/35/0. Same 11 `/tfw-*` commands. Strict UTF-8 passes, zero mojibake patterns, switch visible in first 8 lines, exactly one EN board and zero localized boards. |
| 10 | Placeholder scan over five new Phase B.2 trace files | No template markers or unfinished-work markers. Configured build commands are unrelated unconfigured `echo` stubs, not artifact placeholders. |
| 11 | Configured `build.lint`, `build.test`, and `build.verify` commands | Each ran successfully and printed its configured `configure your … command` message; no substantive runner is configured for this document-only repository. |
| 12 | Full local-citation resolution over master HL and ONB | ONB local citations: 21/21 resolve. Master Markdown citations: 13/15 resolve; missing pre-existing targets are TFW-55 Iteration 2 RES and the TFW-54 HL link in Amendment A2. |

## Claim & Source Checks

| # | Claim / citation checked | Where it appears | Traces to | Holds? |
|---|---|---|---|---|
| C1 | Historic public prefix is 1,485 words with the named SHA-256 | RF §4; EV §1 | Primary Git object `b924926:README.md`, independently extracted | ✅ exact |
| C2 | The result restores the practical guide rather than paraphrasing the essay | RF §§1–4 | Master baseline §1/A6; target root README; reviewed `.tfw/README.md` blob `71a4d725…` | ✅ — the root guide retains Editions, audiences, three starts, FAQ, repository/workflow, updating, and separate destinations; it does not reproduce NS1–NS3 or the essay argument |
| C3 | Lifecycle and status identifiers match current sources | RF §4; EV E4/§5–6 | `.tfw/conventions.md` lines 325/341, `.tfw/glossary.md` line 130, `.tfw/project_config.yaml`, live board | ❌ — all three guides substitute `⛔ BLOCKED` for `❌ BLOCKED` |
| C4 | Russian preserves the human stop-responsibility boundary | RF AC-5; EV E5; RU critic | English README line 27; `.tfw/README.md` lines 35/58/94; master HL lines 263/351; RU line 27 | ❌ — responsibility/decision becomes an obligation to stop work |
| C5 | Nine Evidence items are `VERIFIED` | RF §5; EV final verdict | Approved TS lines 82/98/113/127/142/157/172/187/202; TS template line 48; conventions lines 177/500 | ❌ — every AC is specified `N/A`; the checks are deterministic repository verification, and RF neither declares nor justifies the permitted MAY-deviate choice |

All local citations in the three public guides were resolved, not only sampled. The established eight external URL strings were compared for exact cross-language preservation; live availability is explicitly not claimed and therefore was not treated as Evidence.

## Complete Keep / Update / Add / Remove and Purpose Audit

- The historical 1,485-word public prefix was reproduced exactly before comparison.
- Every historical H2 retains its practical function. No section was silently consolidated into the essay.
- Editions growth (`77→207`) supplies the current three-Edition choice table, availability, copy-contents rule, and migration route.
- Quick Start+FAQ growth (`429→611`) supplies Edition-first choice, new/existing/configured starts, preservation instructions, exact commands, current adapters, and bounded corrections to automation/reproduction claims.
- Key Concepts growth (`96→220→240`) supplies current lifecycle, roles, modes, budgets, Evidence, trace separation, versioning, and restores the baseline Conduct route. Its content is functional, although the `BLOCKED` glyph is factually wrong.
- Remaining growth is attributable to current repository/adapters/workflows, human-authority correction, retained audiences, and distinct mechanics/philosophy/history/help routes. No arbitrary ceiling or preferred band was used; size itself is not a finding.
- Minimal philosophy alignment holds in English: methodology grounded in Philosophy of Trace, bounded agents/human authority, selected durable Trace, and an essay link. The README does not retell the essay.
- Cold-newcomer traversal succeeds in EN/RU/KK for project identity, audience, Edition choice, new/existing/configured start, `/tfw-plan`, repository/workflow, mechanics, philosophy, history/evidence, help, repository, author, and license. The Russian authority sentence remains a material semantic exception, not a navigation failure.

## Discrepancies Found

### D1 — material Russian human-authority drift

- **Location:** `README.ru.md:27`; accepted again in `LANG_REVIEW__phase-b2__ru.md:51`.
- **Contract/source:** `README.md:27`, `.tfw/README.md:35,58,94`, master HL lines 263/351, Phase B.2 TS AC-3/AC-5/AC-7.
- **Actual:** `обязанность остановить работу` means an obligation to stop the work. The contract retains human responsibility and decision authority to stop when warranted. The Kazakh critic identified the equivalent draft drift as HIGH and repaired it to responsibility language.
- **Impact:** This changes the central human/agent authority boundary in the semantic-source paragraph and invalidates the Russian critic's material acceptance.

### D2 — official `BLOCKED` token is wrong in all three guides

- **Locations:** `README.md:209`, `README.ru.md:201`, `README.kk.md:201`.
- **Authority:** `.tfw/conventions.md:325,341`, `.tfw/glossary.md:130`, `.tfw/project_config.yaml`, and the live board use `❌ BLOCKED`.
- **Actual:** All three guides use `⛔ BLOCKED` while RF/EV claim exact current lifecycle parity.
- **Impact:** A practical guide teaches a non-canonical operational status symbol and breaks AC-4 plus cross-language source parity.

### D3 — approved Evidence plan is systematically misclassified

- **Locations:** TS AC Evidence fields at lines 82/98/113/127/142/157/172/187/202; EV rows E1–E9 and line 241; RF line 108.
- **Authority:** conventions §Evidence requires real-environment observation for `VERIFIED`.
- **Actual:** The TS deliberately classifies all nine ACs `N/A` because these are Git/document facts and bounded language critique. Although the TS template permits an Executor to deviate with justification in RF, no deviation or justification is recorded, and the EV artifacts remain repository/document checks rather than external/live observations. EV and RF nevertheless relabel all nine as `VERIFIED`.
- **Impact:** The final trace falsely reports operating Evidence and contradicts the approved TS, even though many underlying repository checks are useful and reproducible.

### D4 — pre-existing missing TFW-55 Iteration 2 citation (non-blocking for B.2)

Master HL §7.2 item 14 and the Task Board point to `research/iter2/RES.md`, which does not exist. ONB and RF disclose the gap and rely on approved successors. Reconstruction is outside Executor scope and is not a Phase B.2 return item.

### D5 — pre-existing missing TFW-54 citation (non-blocking for B.2)

Master Amendment A2 links `../TFW-54__agent_team_mode/HL-TFW-54__agent_team_mode.md`, which does not exist in this checkout. It is outside Phase B.2, was not introduced by target `f8b0731`, and does not alter the owner-approved A6 contract used here.

## Evidence Verification

The EV artifact exists and contains all nine rows, but the TS-to-EV status mapping is invalid: the approved disposition remains `N/A` absent a documented MAY-deviate justification and qualifying target-environment observation. Neither is present. The table below separately assesses whether the repository material cited in each row supports the row's substantive claim.

| # | RF/EV reference | Artifact exists? | Matches substantive claim? |
|---|---|---|---|
| E1 | EV E1 / §1–2 | ✅ | ✅ exact historic baseline and ledger |
| E2 | EV E2 / §3–4 | ✅ | ✅ practical functions and cold traversal exist |
| E3 | EV E3 / §2, §5 | ✅ | ✅ English definition/anti-paraphrase/source blob hold |
| E4 | EV E4 / §5–7 | ✅ | ❌ official `BLOCKED` glyph does not match current sources |
| E5 | EV E5 / RU report | ✅ | ❌ central RU stop-responsibility meaning drifts |
| E6 | EV E6 / KK report | ✅ | ⚠️ language meaning holds; exact lifecycle-token parity does not |
| E7 | EV E7 / both reports | ✅ | ❌ Git lineage is exact, but RU material acceptance is unsound and both critics missed the status-token mismatch |
| E8 | EV E8 / §6, §8–9 | ✅ | ✅ switch, board, tail, encoding, links, and essay blob reproduce |
| E9 | EV E9 / §10 | ✅ | ✅ corrective provenance and eight-path scope reproduce |

Evidence item count: `9` present; substantive claims fully supported: `5`; partial: `1`; failed: `3`. Evidence-status mapping: `0/9` valid because the approved classification is `N/A`, and RF does not invoke or justify the allowed deviation.

## Knowledge Citations Verified

| # | Artifact | Citation set | Link resolves? | Items exist? |
|---|---|---|---|---|
| 1 | Master HL §7.2 #1 | `b924926:README.md` | ✅ Git object | ✅ exact prefix reproduced |
| 2 | Master HL §7.2 #2–13 | essay, KNOWLEDGE decisions, six knowledge topics, TFW-32, TFW-52, RES Iteration 1 | ✅ | ✅ cited decisions/facts/sections were read and exist |
| 3 | Master HL §7.2 #14 | `research/iter2/RES.md` | ❌ | ❌ pre-existing missing artifact, disclosed by ONB/RF |
| 4 | Master HL §7.2 #15–17 | owner-local essay/architecture/BoK corpus | ⚪ non-repository, non-link sources | ⚪ explicitly N/A to direct B.2 loading; approved successors govern; BoK remains non-authoritative and out of scope |
| 5 | ONB §7 #1–13 | historic Git object, repository authority, knowledge, prior reviewed traces | ✅ | ✅ |
| 6 | ONB §7 #14 | TFW-55 Iteration 2 | ⚠️ explicitly recorded unavailable | ❌ same single missing artifact as master #14 |
| 7 | ONB §7 #15–17 | owner-local sources and BoK | ⚪ explicitly indirect/N/A | ⚪ correctly not treated as B.2 authority |

Logical master §7.2 citations: `17`; verified repository/Git citations: `13`; missing: `1`; explicit non-repository/N/A: `3`. ONB correctly mirrors that state. The broader master-link scan also found the separate pre-existing TFW-54 missing target in Amendment A2.

## KNOWLEDGE Cross-Check

- D2 and D35 support a practical root landing/project guide separate from the essay; the target follows them.
- D52 requires the fixed Evidence vocabulary and real-world boundary; EV/RF contradict it by converting nine TS `N/A` items to `VERIFIED` without the MAY-deviate justification required by the TS template or qualifying real-environment observations.
- D58/D59 support the bounded Assisted/manual-fallback and capability language; target claims remain within those limits.
- D66 still describes the owner-rejected compact doorway. The corrective contract explicitly requires it to remain stale until post-APPROVE `/tfw-docs`; it is not acceptance evidence and must not be edited during this REVISE cycle.
- `knowledge/philosophy.md` F35/F36/F42 require contract fidelity, purpose checking, and a materiality bar. The practical-guide purpose passes; D1–D3 are meaning/fact/trace defects rather than taste-only wording preferences.
- All required knowledge topic files (`constraint`, `convention`, `domain`, `environment`, `philosophy`, `process`, `risk`, `stakeholder`) were read in full. No additional material contradiction was found.

## Checkpoint

**Self-check:**
- [x] Opened ≥ `ceil(8 × 0.42)` files and recorded findings? (`8/8`, 100%)
- [x] Ran at least 1 build/test command (or documented why not)?
- [x] Claim & Source Checks filled — key claims checked against primary Git/repository sources; all public-guide local citations resolved; master/ONB citation gaps recorded?
- [x] Each RF §3 (AC) checkmark verified against actual files?
- [x] KNOWLEDGE.md and all topic files checked — contradictions with changes documented?
- [x] Knowledge Citations from HL §7.2 and ONB §7 verified?
  - Logical HL citations: `17`; repository/Git verified: `13`; missing: `1`; explicit non-repository/N/A: `3`
- [x] Evidence artifact from RF §5 verified and statuses checked?
  - Total EV rows: `9`; present: `9`; Evidence statuses valid against TS/conventions: `0`

Stage complete: **YES**
