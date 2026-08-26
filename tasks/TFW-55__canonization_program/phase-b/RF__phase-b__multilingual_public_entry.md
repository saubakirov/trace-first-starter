# RF — TFW-55 / Phase B: Multilingual public entry

> **Date**: 2026-08-26
> **Author**: Codex (Executor)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-55](../HL-TFW-55__canonization_program.md)
> **Phase HL**: [Phase B HL](HL__phase-b__multilingual_public_entry.md)
> **TS**: [TS Phase B](TS__phase-b__multilingual_public_entry.md)

---

## 1. What Was Done

The 1,485-word English public section was replaced with a 523-word doorway while preserving the English Task Board below its hard boundary. Independently written Russian and Kazakh doorways were added, reviewed in separate isolated Codex tasks, corrected, and rechecked at the exact final localization commit with zero unresolved HIGH findings.

### New Files

| File | Description |
|---|---|
| `README.ru.md` | Natural Russian public doorway; derived from the English semantic source; no Task Board |
| `README.kk.md` | Natural Kazakh public doorway; derived from the English semantic source; no Task Board |
| `tasks/TFW-55__canonization_program/phase-b/ONB__phase-b__multilingual_public_entry.md` | Executor onboarding, scope, baseline, and question resolution |
| `tasks/TFW-55__canonization_program/phase-b/evidence/EV__phase-b__multilingual_public_entry.md` | Per-AC gates, matrices, counts, navigation, board check, and subtraction ledger |
| `tasks/TFW-55__canonization_program/phase-b/evidence/LANG_REVIEW__phase-b__ru.md` | Complete Russian draft/final critique chain, dispositions, back-translation, and final severity |
| `tasks/TFW-55__canonization_program/phase-b/evidence/LANG_REVIEW__phase-b__kk.md` | Complete Kazakh draft/final critique chain, dispositions, two back-translations, and final severity |
| `tasks/TFW-55__canonization_program/phase-b/RF__phase-b__multilingual_public_entry.md` | Phase B result record |

### Modified Files

| File | Changes |
|---|---|
| `README.md` | Replaced only public onboarding above `## Task Board`; retained brand, added language/source routing, definition, proportional Editions, Quick Start, three routes, and authority boundary; changed only the normal TFW-55 workflow row inside the board |

### Execution commits

| Commit | Purpose |
|---|---|
| `328e6b4` | Executor ONB and normal TFW-55 board transition |
| `437f7a9` | Frozen multilingual draft reviewed by both independent critics |
| `caee273` | Closed RU H1–H4 and KK H1–H2 plus materially useful MEDIUM findings; exact final localization recheck target |

## 2. Key Decisions

1. **Keep one semantic source.** English `README.md` plus the reviewed English `.tfw/README.md` remains the Project North Star surface. RU/KK explicitly yield on conflict and do not create new authority.
2. **Count English only before `## Task Board`.** The heading and entire board tail are excluded from onboarding metrics. No required meaning was removed because the operational board is long.
3. **Localize independently.** Russian and Kazakh preserve semantic units, identifiers, paths, and commands while using target-language phrasing and list/paragraph structure rather than sentence-by-sentence translation.
4. **Use materiality for language fixes.** All 6 initial HIGH findings were closed and rechecked. Useful MEDIUM findings were applied; remaining taste-only alternatives are recorded as non-blocking and did not cause another loop.
5. **Do not pad to the preferred band.** EN/RU/KK are 523/528/526 words. All doorway units are present; adding 27/22/24 words solely to reach 550 would duplicate linked North Star, Edition, or Quick Start material.
6. **Preserve Phase A and shared state.** `.tfw/README.md` remains the reviewed blob; no research artifact, BoK, specification/glossary change, translation registry, public roadmap, or visual asset entered Phase B.

## 3. Acceptance Criteria

- [x] **AC-1:** English is a compact doorway with language/source notice, brand identity, continuity problem, functional definition, direct `NS1`–`NS3` links, and no forbidden claim.
- [x] **AC-2:** Russian is a natural, complete derived doorway with valid UTF-8, no Task Board/state, and zero unresolved HIGH findings.
- [x] **AC-3:** Kazakh is a natural, complete derived doorway with valid UTF-8, no Task Board/state, and zero unresolved HIGH findings.
- [x] **AC-4:** All six semantic/authority invariants map across EN/RU/KK with zero missing, extra, or contradictory claims.
- [x] **AC-5:** Language switches are first; all created/retained public local targets and required anchors resolve; shared paths/commands remain unchanged.
- [x] **AC-6:** Edition facts and new/existing/configured Quick Start actions match current guide/quickstart without unsupported Assisted capability claims.
- [x] **AC-7:** Understand/use/audit routes plus repository, author, and MIT license are visible in every doorway.
- [x] **AC-8:** Word/combined budgets pass; English has the sole Task Board; every non-TFW-55 board line matches the approved baseline.
- [x] **AC-9:** Separate RU/KK critiques and exact-final rechecks are preserved; 4 RU and 2 KK HIGH findings are closed; final unresolved HIGH is zero in both.
- [x] **AC-10:** EV/RF provenance and scope are complete; production changes are limited to three root READMEs; reviewed North Star blob is unchanged; no forbidden subsystem/artifact was created.

## 4. Verification

- Configured lint (`echo "configure your lint command"`): command ran; configuration placeholder, not a substantive gate.
- Configured tests (`echo "configure your test command"`): command ran; configuration placeholder, not a substantive gate.
- Configured verify (`echo "configure your verify command"`): command ran; configuration placeholder, not a substantive gate.
- Markdown whitespace check (`git diff --check`): PASS.
- Strict UTF-8/mojibake: PASS for EN/RU/KK and `.tfw/README.md`; zero replacement/mojibake sequences.
- Raw Markdown words: EN `523`, RU `528`, KK `526`, `.tfw/README.md` `1,548`; combined English `2,071` versus `2,600` ceiling.
- Public local links: EN `28` total / `24` unique; RU `25` / `21`; KK `25` / `21`; zero broken targets.
- Anchors/routes: `NS1`–`NS3`, Task Board, Editions, Quick Start, conventions, tasks, knowledge, repository, and license PASS in every applicable doorway.
- Commands: `/tfw-plan`, `/tfw-handoff`, `/tfw-review` occur exactly once and unchanged in every language.
- Task Board: headings EN/RU/KK = `1/0/0`; localized task rows RU/KK = `0/0`.
- Board tail excluding only TFW-55 row: PASS; baseline/final normalized SHA-256 `a8c544a50cc3d098f3890bc6b8d6e26bb9d5a05c333a9eb64672d7aa44b4ecb6`.
- Reviewed North Star: blob `71a4d725cff7d0d7508403589195e9f87a0fc49a` — PASS.
- Independent language rechecks: Russian `unresolved HIGH=0`; Kazakh `unresolved HIGH=0`.

### Semantic source and terminology

| Item | Decision |
|---|---|
| Semantic source | English `README.md` + reviewed English `.tfw/README.md` |
| Philosophy | `Philosophy of Trace` / `Философия Следа` / `Із философиясы` |
| Trace | `Trace`; `След (Trace)`; `Із (Trace)` on first localized use |
| Stable identifiers | `Trace-First Workflow`, TFW, Light/Assisted/Full, `NS1`–`NS3`, `/tfw-*`, and paths remain unchanged |
| Human boundary | Purpose, legitimate authority, judgment, acceptance, accountability, and stop right/responsibility remain human/institutional |
| Agent boundary | Agents perform bounded work; participation alone grants no authority |

### Old-content disposition summary

| Disposition | Content classes |
|---|---|
| Removed | Persona cards, FAQ/comparisons, lifecycle/status explanation, file inventories, adapter tables, root glossary, update walkthrough |
| Linked | Detailed meaning → Project North Star; Editions → guide; use → Quick Start/conventions; history → Task Board/tasks/knowledge |
| Retained compactly | Brand, continuity problem, functional definition, proportional Editions, three project-start cases, repository/author/license |
| Localized | Every required semantic, Edition, Quick Start, navigation, source, repository, and license unit |
| Added | First-block language switch, explicit semantic-source notices, root authority designation, RU and KK doorways |

English subtraction is `-962` words. The final three root onboarding surfaces total `1,577` words versus the old English-only `1,485` (+92) while expanding access from one to three languages. Added English source/navigation copy is contained within the 523-word compressed doorway; RU/KK remain separately bounded. Task Board content was excluded from this accounting.

## 5. Evidence

> **Cognitive mode:** Observational verification — evidence lives in the EV file, not inline.

See [EV file](evidence/EV__phase-b__multilingual_public_entry.md) for per-AC results, semantic/terminology matrices, language-critique dispositions, word/link/anchor/board checks, three-route walkthroughs, and the subtraction ledger.

Language reports:

- [Russian](evidence/LANG_REVIEW__phase-b__ru.md) — draft `437f7a9` → final `caee273`; unresolved HIGH `0`.
- [Kazakh](evidence/LANG_REVIEW__phase-b__kk.md) — draft `437f7a9` → final `caee273`; unresolved HIGH `0`.

Evidence verdict: **0/10 VERIFIED, 0 DEFERRED, 0 BLOCKED, 10 N/A**

The N/A statuses follow the approved TS: these are directly inspectable repository-document gates, not live-environment or population-level claims.

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|---|---|---|---|
| 1 | `README.md` | Task Board / TFW-55 row | baseline/shared-checkout | The existing Iteration 2 link targets missing `research/iter2/RES.md` in this clean worktree. Coordinator confirmed it is a pre-existing uncommitted research trace outside Phase B. The board link and research artifacts were not changed or added. |

## 7. Fact Candidates

No Fact Candidates. Execution produced document and verification results, not new human-only domain facts for knowledge consolidation.

## 8. Strategic Insights (Execution)

No strategic insights. Owner guidance on the preferred word band, Task Board boundary, and material language-review threshold was applied as task-specific acceptance context and is already recorded in the approved HL/TS and evidence.

## 9. Diagrams

No diagrams. The change is a three-file documentation doorway with direct source/navigation relationships already captured in the EV matrices.

## 10. Residual non-blocking risks

- Live HTTP availability of external repository/documentation/author URLs was not tested; their strings and local Markdown destinations are intact. The TS requires repository-local navigation, not live-site evidence.
- RU critic noted three optional editorial alternatives; KK critic noted two. They do not affect meaning, factual accuracy, authority, navigation, ordinary comprehension, or TS compliance and therefore did not trigger another revision cycle.
- The known missing Iteration 2 target remains a baseline/shared-checkout issue outside the public onboarding boundary and Phase B scope.

---

*RF — TFW-55 / Phase B: Multilingual public entry | 2026-08-26*
