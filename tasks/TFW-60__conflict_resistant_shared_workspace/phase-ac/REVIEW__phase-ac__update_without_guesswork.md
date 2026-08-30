# REVIEW — TFW-60 / Phase AC: Update Without Guesswork

> **Date**: 2026-08-30
> **Author**: Claude Code (Reviewer), `on_behalf_of: saubakirov`, `via: claude-code`
> **Verdict**: ✅ **APPROVE**
> **RF**: [RF Phase AC](RF__phase-ac__update_without_guesswork.md) — commits `d2e6bae`, `4fe3b1d`, `d047286`, `af1a695`
> **TS**: [TS Phase AC](TS__phase-ac__update_without_guesswork.md) — revision 2, amendment A7 approved 2026-08-30
> **Contract baseline**: master HL at `e8690c7` (the A7 re-freeze; `56c3d70..e8690c7` is A7 alone, `e8690c7..HEAD` is empty)
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`
> This file is a synthesis of stage findings. Reference stage files for raw evidence.

---

## 1. Map

Two field reports on `v2.0.0-dirty.4` found five places where the update path guessed or decided for the owner. The executor rewrote `update.md` at 1174 words so that the pin is derived from the tag the operator names, the update stops before its first durable write with exactly three questions, the payload copy excludes the two project-owned files and prints what it skipped, every Step 6 row is a `cmp` copy or a marker-bounded block under one rule stated in conventions §9, `installed_from` has one form, and the update ends with a four-block briefing rendered from a new template. `migrate_board.classify_status()` now refuses a status cell carrying a second declared token or a second Unicode-`So` symbol; `gen_index.check_tasks()` names phase directories without state (failure under a live task, one informational line per terminal or stateless task); `check_project()` reports a machine-local `installed_from`. Twenty text carriers were brought into agreement around the two scripts, and seven debt rows (TD-190, 191, 198, 200, 201, 203, 204) were closed in the CHANGELOG, `RELEASE.md`, three templates, four adapter files and the migration guide. 26 counted paths, 1 new, 943+/172−, inside the `50/50/5000/50` budget; two onboarding questions ruled before any fixture was written; A7 filed and approved the same day.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|-----------------|--------|----------|
| 1 | 24 of 26 counted files read or diffed; the 2 remaining (script test files) executed — ratio 1.0 against the 0.42 minimum | 24 ✅ · 0 ❌ · 1 ⚠️ (E29, below) | verify.md V1–V16 |
| 2 | Full suite `python -m pytest .tfw/scripts/ docs/scripts/ -q` | **315 passed, 1 skipped**, 153 s — equals the RF | command 1 |
| 3 | `--check tasks` · `--check project` on this repository | 6 informational lines over 17 directories, 54 validate, exit 0 · consistent | commands 2–3 |
| 4 | `update.md` word count · six workflow copies · Antigravity rule vs template · `TFW:CLAUDE` region of root `CLAUDE.md` vs template · `{version}` in three templates | 1174 · identical · identical · identical · 0/0/0 | commands 4–6 |
| 5 | `classify_status()` run on ten cells including the `AILAB-2` shape, `A+B`, `→`, `=`/`<`, a bare `U+FE0F`, a second declared token alone | every cell classified as the rule states; `Sm` punctuation survives in the outcome | command 7 |
| 6 | AC-5 and AC-8 fixture behaviours re-created on the reviewer's own scratch fixtures | machine-local `installed_from` → exit 1, symbolic and URL → exit 0, config unchanged; live task + stateless `phase-b` → failure naming the directory, exit 1; terminal task → informational, exit 0; nothing written | commands 8–9 |
| 7 | Census and LOC over the 26 counted paths (`b9baec2..d047286`) | 26 files, 943+/172− — equals the RF header | command 10 |
| 8 | Contract baseline: master HL frozen sections vs `56c3d70` and `e8690c7` | only A7 between the two freezes; nothing after | command 11 |
| 9 | Safety: tags in this repository; three consumer checkouts | no fabricated or dry-run tag here; consumers carry no `.tfw/` or adapter change | commands 12–13 |
| 10 | Six key claims traced to primary sources (C1–C6): the 114-row measurement, 22/28 before-after, the live-source pin runs, the owner's quote, the `gen_docs` resolution, the seven closed debt rows | 5 ✅ · 1 ⚠️ — the `gen_docs` claim is true but established by an existing test the EV does not cite | verify.md C1–C6 |
| 11 | 32 knowledge citations (HL §7.2 × 29 + ONB N1–N3): resolution, existence, meaning, relevance; priorities 0 and 1 checked separately | 32 resolved, 32 semantically verified, 0 irrelevant, 0 hallucinated | verify.md Knowledge Citations |
| 12 | 37 EV rows across 9 evidence artifacts | 34 VERIFIED (one ⚠️), 3 DEFERRED with named blockers assigned by the TS to `/tfw-release` and the field, 0 missing | verify.md Evidence Verification |

> Raw verification log: `review/verify.md`. **Not re-runnable at review:** the AG-mode dry run (E16) — an agent's transcript against a scratch fixture that no longer exists; it establishes that the rewritten text, followed as written, stops with no write, which is what a workflow can be tested for. Two discrepancies, both Low and neither a verdict ground: **D1** `update.md` Step 0 admits a commit target in prose but its block tests tag equality only (→ TD-206); **D2** EV E29 cites a hand-extracted regex where `test_gen_docs.py::test_current_identifier_artifact_phase_hl_and_bare_refs_resolve` already establishes the claim (→ TD-213 for the import that forced it).

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ✅ | Every executor-owned box of AC-1..AC-11 verified against files, commands or reproduced fixtures (judge.md row 1); the two open AC-11 boxes are `/tfw-release` and the field run, placed after review by the TS — Phase AB was approved on the same shape. Every DoF §7 line checked and none fires |
| 2 | Purpose Check — is this what we set out to do? + design soundness | ✅ | **(a)** Serves master HL §4 Phase AC at `e8690c7` — *"an update neither guesses nor decides for the owner … the owner is asked before the first durable write and briefed in their own language after the last; the migration refuses a status it cannot read whole and names every phase it left without state"* — and NS2 principle 4 *"Human authority, bounded delegation"*; the harm removed is the fifth report's: a handle inferred from a Git identity, containers and `build.*` chosen for an absent owner, a live task closed by its first status token under a gate that said *4 tasks validate*. No excess (all eleven deliverables in the baseline list; B, C, TFW-54, TFW-61 and the grammar untouched; `2.0.0` unclaimed), no deferral confession (O11 and the §6 minor items filed, not shipped), material. Reference set consistent. **(b)** Sound against P1, P3/P5, P4, P9, P10 and §7.1's new-artifact clause — `briefing.md` names the duplicate write it removes |
| 3 | Tech debt documented | ✅ | RF §6: 12 observations with file, line, type and disposition; every fifth-report §6 item and fourth-report defect 7 accounted for as fixed or filed |
| 4 | Style & standards | ✅ | Templates followed (RF §1–§9, EV, ONB §1–§8); commit grammar; phase journal of 8 clock-read events with `on_behalf_of`/`via` and the right `kind` for A7; `update.md` a procedure under the ceiling. One gap: E29's citation (D2) |
| 5 | Observations collected | ✅ | Nine promoted after the quality filter (§5 below); O9 (cosmetic outcome-string change in immutable consumer files), O10 (two READMEs, one pointer already present) and O12 (derived index rebuilt by its one writer at release) noted and not promoted |
| 6 | RF completeness (§7-9 present) | ✅ | Five human-sourced Fact Candidates (owner quote traced; rulings traced to ONB §8); three Strategic Insights with implications; three text diagrams matching the code read |
| 7 | Evidence completeness — does it exist? | ✅ | Eight TS §5 artifacts present; 37 rows; 3 DEFERRED each naming the blocker the TS assigns; no N/A |
| 8 | Evidence sufficiency — does it establish the claim? | ✅ | Suite, gates, corpora comparison and both fixtures reproduced by the reviewer. Two signals weaker than their status and named as such: E29 (hand-check; the establishing test exists uncited) and E16 (a transcript, not a tool run — the only test a workflow text admits). Neither leaves a claim unestablished |
| 9 | Backward compatibility | ✅ | Re-migration only for the classifier; `--check tasks` turns red on a consumer with a live task and a stateless phase directory (intended, `.5` item 6); `--check project` exits 1 on all three local consumers' `D:/` `installed_from` (intended, `.5` item 4); Codex append → report changes nothing for consumers already carrying the block; `.5` item 5 names `CLAUDE.md` only — TD-215 for the release entry |
| 10 | Safety | ✅ | No secrets; fabricated tags confined to a scratch clone (verified absent here); consumers read-only (verified); checks write nothing (verified on fixtures); the copy loop is bounded by an exclusion list and a payload-derived test; CHANGELOG appended, no event touched |

## 4. Verdict

**✅ APPROVE**

The phase does what the baseline says Phase AC is for, and every claim the RF makes about it was either reproduced by the reviewer or traced to an artifact that establishes it: the pin comes from the tag the operator names and no `HEAD` pin remains in the file; the three questions stand before the first write with the handle *asked, never inferred*; the copy loop skips the two project-owned files and says so; the marker rule is stated once and this repository obeys it; the status cell is refused on a second signal — measured first on four real boards so that `A+B` is not refused — and `--check tasks` names what the fifth report found silent, with exit codes that distinguish a live task from history. The full suite is green at 315 with 32 new tests, the four corpora reclassify exactly their eight multi-signal rows, and 26 counted paths sit inside a 50-path budget. Seven debt rows are closed in the files that carried them.

What stays open is what the TS places after review: `/tfw-release` cuts the `.5` entry — with the updating section RF §1 hands it, plus the one-clause addition TD-215 names — bumps `VERSION`, tags, and a consumer on the line updates from Step −1. Two Low findings are filed rather than returned: the commit-target path in Step 0 has no check behind its prose (TD-206), and one EV row rests on a hand-check where a test already exists (TD-213 for the import that forced it). Neither changes what a receiver on the tag path experiences.

## 5. Tech Debt Collected

> **Source format**: Use reference patterns (compilable_contract.md §2).

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| TD-206 | REVIEW TFW-60/AC §2 D1 | Low | `.tfw/workflows/update.md` Step 0 | The commit-target path admitted in prose has no executable check; the block tests tag equality only | → backlog: one sentence, 26 words of ceiling left |
| TD-207 | RF TFW-60/AC §6 O1 | Med | `tasks/TFW-55__canonization_program/` | A live task (uncommitted research) with no `status.md` at any level; the gate reads its stateless phases as history | → owner: author the state with a `transition` event, or close the research |
| TD-208 | RF TFW-60/AC §6 O2 | Low | consumer `README.md` route sections | No template for the permanent route; hand-rewritten in three places on a container change | → next payload-boundary phase |
| TD-209 | RF TFW-60/AC §6 O3 | Low | `gen_index.py` `build()` | A stale `00-INDEX.md` in a non-first container is never named | → Phase B (touches `gen_index.py`) |
| TD-210 | RF TFW-60/AC §6 O4, O5 | Low | `migrate_board.py` `build_status()`; `gen_index.py` `check_project()` | `created` seconds provenance unstated; `--check project` green while the board still stands in the README | → next scripts pass |
| TD-211 | RF TFW-60/AC §6 O11 | Med | payload boundary | The payload ships the framework's own `project_config.yaml` and `knowledge_state.yaml`; AC excludes them at copy, the payload still carries them | → owner ruling on the payload boundary (Phase AA surface) |
| TD-212 | RF TFW-60/AC §6 O7 | Low | `team/README.md` (this repository) | *humans and agents alike* — the wording TD-203 removed from the template stands in the file the template now points to | → backlog: one sentence |
| TD-213 | RF TFW-60/AC §6 O8; REVIEW §2 D2 | Low | `docs/scripts/gen_docs.py`:766 | `mkdocs_gen_files` at module load blocks importing the resolver outside a build; forced E29 onto a hand-check | → backlog, pairs with TD-79 |
| TD-214 | RF TFW-60/AC §6 O6 | Low | `gen_index.py` `check_project()` | Reads `team/` whole but not who references it; a deleted human profile is red only in `--check tasks` | → backlog: a cross-check line or a *not checked* sentence |
| TD-215 | REVIEW TFW-60/AC §3 row 9 | Low | `.tfw/CHANGELOG.md` `.5` entry (to be written) | The updating section names `CLAUDE.md` for the marker first-run rule and not `AGENTS.md`, whose rule changed the same way | → `/tfw-release`: one clause in item 5 |

Closed by this phase and marked so in `TECH_DEBT.md`: TD-190, TD-191, TD-198, TD-200 (completing TD-197), TD-201, TD-203, TD-204. Not promoted: O9, O10, O12 (see §3 row 5).

## 6. Traces Updated

- [x] the phase's `status.md` — `lifecycle: KNW`, `updated: 20260830-181735` from the clock; `transition` event `RF → KNW` at `journal/20260830-181735__transition__b950.md`. The event's first summary was 127 code points and `--check tasks` refused it; it was shortened to 110 in the same session, before any commit or reader — the same correction the coordinator made to the A7 event at `76dc7c0`. Gate green again: 54 validate, exit 0
- [ ] HL status — master HL header unchanged; Phase AC's release lands with `/tfw-release`, which also writes the `.5` entry
- [x] the task's `status.md` — the task-level file stays `PHASES`, by rule; the phase file carries this review's `updated`. No counter incremented
- [x] Other project files — `TECH_DEBT.md`: seven rows closed, TD-206..TD-215 appended. `workspace/00-INDEX.md` is stale (RF O12) and is left to its one writer at release; `--check tasks` is green after the transition (54 validate, exit 0)
- [x] tfw-docs: **Applied** — `KNOWLEDGE.md` §1 Adapters and Task State rows, D70 (refining D69's abbreviation sentence), §2 row TFW-60/AC, §3 Legacy row for the eight retired forms
- [x] tfw-knowledge: **Applied** 2026-08-30 — owner cleared the gates in chat: 142 candidates from TFW-55, TFW-60 (all phases, RES iter1–3) and TFW-56 HL triaged, **9 admitted by owner selection** (philosophy F43–F45, process F35–F36, stakeholder F10, convention F23, environment F5, new `knowledge/context.md` F1); ASSISTED15 and TFW-54 deferred by owner ruling; limits raised to 100 facts / 13 files; `knowledge_state.yaml` at seq 60; every processed source carries `fact-candidates: processed 2026-08-30`. Both markers set → `lifecycle: DONE`

## 7. Fact Candidates

> fact-candidates: processed 2026-08-30

> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | process | The owner treats a refusal that fires on a plainly single-signal row (`A+B`) as worse than a missed refusal: "a rule that refuses `A+B` teaches operators to distrust the refusal" — so whole-or-refuse rules are measured on real corpora for false refusals before their fixture is fixed | ONB §3 Q1 ruling (coordinator, 2026-08-30); RF §8 S3 | High |
| 2 | process | The owner's standard for an unattended update is being onboarded as a person would be — asked who they are and where they keep their work, then told what changed in positive terms — rather than having those facts inferred and the change reported in procedure vocabulary | fifth field report, owner quote `:58–60`; HL §12 A6 | High |
| 3 | stakeholder | `2.0.0` is not claimed after a phase whose field evidence is still pending; the owner reversed the 2026-08-29 ruling on 2026-08-30 after two more reports, and the line stays `2.0.0-dirty.N` until a consumer run on the new tag is on record | HL §12 A6 cost column; TS §2 settled decisions | High |

---

*REVIEW — TFW-60 / Phase AC: Update Without Guesswork | 2026-08-30*
