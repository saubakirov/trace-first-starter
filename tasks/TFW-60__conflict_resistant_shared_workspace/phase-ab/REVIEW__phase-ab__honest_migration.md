# REVIEW — TFW-60 / Phase AB: Honest Migration

> **Date**: 2026-08-29
> **Author**: Claude Code (Reviewer), `on_behalf_of: saubakirov`, `via: claude-code`
> **Verdict**: 🔄 **REVISE** — two items, one line each, both in the phase's own subject; architecture sound, every other check passes
> **RF**: [RF Phase AB](RF__phase-ab__honest_migration.md) — commit `ecfceee`
> **TS**: [TS Phase AB, revision 2](TS__phase-ab__honest_migration.md)
> **Contract baseline**: master HL at `810b1b8` — recovered per `conventions.md` §3 rule 15
> **Stage files**: `review/map.md`, `review/verify.md`, `review/judge.md`
> This file is a synthesis of stage findings. Reference stage files for raw evidence.

---

## 1. Map

The executor removed the mechanism behind the third report's defect — an unanchored `re.search()` in `parse_board()` that extracted `HD-30` from `HD-30b` before the anchored grammar was consulted — and replaced it with one dispatcher in `gen_index.parse_identifier()` that classifies a whole candidate as `current`, `clock`, `legacy` or malformed. Duplicate rows and duplicate directories now raise before any output path is opened; the manifest computes three partition equalities, prints each with its arithmetic under `## Guarantees checked`, and lists what it did not check; `_plain()` strips `_` only at word boundaries so `normalize_text()` survives migration. The current grammar `{PREFIX}_{YYYYMMDD-HHMMSS}_{ABBR}` is issued by `plan.md` and `init.md` with the owner approving the abbreviation before a directory exists, carried by canon, glossary, both configs, three templates and the compiler; both historical forms stay readable. `update.md` fell from 1380 to 852 words while gaining source-pin, tag-check, provenance-drift and allowlist rules. `via` is free-form and validated non-empty. Release acts were correctly left to `/tfw-release` per §15 — a correction of Phase AA's ruling, acknowledged by the coordinator in the ONB. 23 implementation paths, 17 counted, 0 new, 1029 lines: inside every budget with no ruling needed.

## 2. Verify

| # | What was checked | Result | Evidence |
|---|-----------------|--------|----------|
| 1 | All 23 implementation paths diffed `57a5147..ecfceee`; all 8 work artifacts read — 100% after escalation | 21 ✅ · 2 ⚠️ | verify.md V1–V25 |
| 2 | Test suite re-run: `-k "not repository"` / `-k repository` | 281 passed, 3 deselected · 2 passed, 1 skipped — matches RF | verify.md commands 1–2 |
| 3 | `gen_index.py --check tasks` / `--check project` | 53 valid · consistent with `2.0.0-dirty.3` | commands 3–4 |
| 4 | HELPDESK_SHAPE parsed and `_plain()` run inline | `HD-30` legacy · `HD-30b` malformed · `TFW-01_single_underscore` malformed · dirty clock · current — reproduces the evidence file | command 8 |
| 5 | `update.md` word count · adapter triplets · 11 Codex skill pairs | 852 · byte-identical · byte-identical | commands 5–6 |
| 6 | Scope census | 17 counted files, +712 −317 = 1029 | command 7 |
| 7 | `HD-30b` mechanism claim | confirmed at `57a5147:migrate_board.py:130` | C1 |
| 8 | Seven third-report §7 items | each traced to a fix or a filed observation | C6 |
| 9 | 32 knowledge citations (HL §7.2 ×29, ONB N1–N3); PV 0–4 scanned in full | 32 resolve, 32 semantically verified, 0 irrelevant, 0 hallucinated; priorities 0 and 1 checked as distinct clauses | verify.md Knowledge Citations |
| 10 | Nine evidence items | 8 verified · 1 partial (E3: the collision clause is a transcription of the rule, not a run) | verify.md Evidence Verification |
| 11 | **D1** — `migrate_board.py`:750 `**Unaccounted: 0.**` is a string constant; `test_migrate_board.py`:237, :508 assert the literal | ❌ | verify.md D1 |
| 12 | **D2** — `update.md` Step 0 and Step 9: "Both temporary directories are gitignored"; `.gitignore` holds only `.tfw/.upstream/` | ❌ | verify.md D2, C7 |

**Not verified in this review:** the three external corpora (`97dd429`, `58329e7`, `aec5f2d`) live outside this repository and were accepted on the stated method — `git ls-tree` at the pin, pre-change regexes reimplemented inline, compared identifier by identifier — with this corpus's 53 confirmed independently.

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? (all TS acceptance criteria) | ❌ | 8 of 9 gates hold; AC-2 bullet 1 leaves a prose guarantee standing beside its computed form; AC-6's rewrite introduced a false sentence. AC-8 release correctly DEFERRED |
| 2 | Purpose Check — is this what we set out to do? + design soundness | ✅ | Serves DoD 20 and NS1 at `810b1b8`; harm removed: a shipped task silently written to `TODO` under a manifest asserting zero unaccounted. No excess, deferral honoured, material. Design sound on P1, P4, P5, P9, P10 |
| 3 | Tech debt documented | ✅ | RF §6, four typed rows with reasons |
| 4 | Style & standards | ✅ | Commit grammar, template, identity fields, clean staging. Minor: no journal event behind the RF `updated` stamp |
| 5 | Observations collected | ✅ | O1–O4 are real; all promoted |
| 6 | RF completeness (§7-9 present) | ✅ | Both empty sections justified; diagram matches code |
| 7 | Evidence completeness — does it exist? | ✅ | EV with nine rows and five attachments; one legitimate DEFERRED |
| 8 | Evidence sufficiency — does it establish the claim? | ✅ | Every green signal named with what it proves; two limits stated (external corpora on method; E3 collision clause is text) — neither weakens an AC gate |
| 9 | Backward compatibility | ✅ | Every previously parsed identifier parses identically; compiler gains dirty-clock resolution it lacked. Gap filed: artifact naming for the current grammar (TD-201) |
| 10 | Safety | ✅ | Refusals precede any write; consumers read at pins, never written; fixture discarded |

## 4. Verdict

**🔄 REVISE**

The phase does what amendment A5 asked and does it the right way: the cause is removed rather than the instance patched, the guarantee arithmetic runs before a file is opened, the grammar lands with the owner in the loop, and nothing historical moves. Every claim in the RF that could be re-run was re-run here and held (§2 rows 1–10). The verdict is REVISE, not APPROVE, because two sentences shipped in this commit fail the standard the commit itself sets — and this phase's Definition of Failure names both shapes explicitly: *"A guarantee printed that the tool did not compute"* and *"A check reported as passing that never ran"* has a text-side twin in a workflow that states a fact that is not true.

### If REVISE — items to fix:

1. **`migrate_board.py`:750 — delete the constant, or compute it.** `**Unaccounted: 0.** Every board row is classified exactly once; …` is a string literal that shows no arithmetic. It is entailed by `require_guarantees()` at the head of `render_manifest()`, but TS AC-2 bullet 1 allows exactly two states for an asserted invariant — computed under a heading naming it, or deleted, "not both left standing" — and the computed form already exists eleven lines lower. It is also the exact sentence the third report quoted over a table listing `HD-30` twice. Remove the line and the two assertions that enshrine it (`test_migrate_board.py`:237, :508), or print `len(rows) − Σ classified` from `computed_guarantees()[0]`. Expected diff: three lines.
2. **`update.md` Step 0 and Step 9 — remove or make true the claim "Both temporary directories are gitignored".** `.tfw/.upstream-source/` is not in `.gitignore`, and no receiving project ignores either directory unless its owner adds them; the payload ships no `.gitignore`. Either add `.tfw/.upstream-source/` to this repository's `.gitignore` **and** reword to an instruction ("add both to `.gitignore` if they are not already there"), or drop the sentence. Keep the file under 1200 words (it is at 852). Re-sync the two byte-identical copies.

On re-entry, the executor should also write the phase journal event that the RF stage lacks (row 4) — one `handoff` or `transition` event, clock-read, referencing this REVIEW — rather than back-dating anything.

**Recommendation to the coordinator, separate from the verdict:** TD-200 below (event template still defines `via` as a provider family) is one path, inside budget (24 / 18 against 30 / 15), and belongs to the same decision AC-7 closed. Admitting `.tfw/templates/journal/event.md` to §4 for the REVISE round costs one line of TS and closes TD-197 without a residue. If declined, TD-200 stands as filed.

## 5. Tech Debt Collected

> **Source format**: Use reference patterns (compilable_contract.md §2).

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| TD-200 | RF TFW-60/AB §6 O4 | Med | `.tfw/templates/journal/event.md`:49, :70 | The event template — the file every event author copies — still defines `via` as "provider family: claude, codex, gemini" while `conventions.md` §4 and `validate_event()` now declare and check free-form non-empty text. Same drift class as TD-197, one carrier over; outside the approved 25-path surface, so filed rather than fixed | → Phase AB REVISE round if the coordinator admits the path; otherwise next phase touching the payload |
| TD-201 | REVIEW TFW-60/AB §2 (reviewer finding) | Med | `.tfw/conventions.md` §4 *Artifact file naming* | The table's examples and its no-title rule address clock and legacy tasks only; the current grammar `PREFIX_stamp_ABBR` has no example and no stated rule. The phase's own AC-3 fixture produced `HL-TFW_20260829-172110_ABT__approved_fixture.md` — a title appended — while `templates/status.md` in the same commit teaches `authority: HL-PREFIX_YYYYMMDD-HHMMSS_ABBR.md`. A framework undefined about its own artifact names is the class Phase AB exists to end | → Phase AB REVISE round (one table row and one sentence) or the `2.0.0` release pass |
| TD-202 | RF TFW-60/AB §6 O1 | Med | `KNOWLEDGE.md`:102 (D68), :162 (§3 Legacy) | Both still declare `YYYYMMDD-HHMMSS__slug` the current identifier and say a current event name includes its actor. D37 reserves these sections for `/tfw-docs`; correctly not touched by the executor | → `/tfw-docs` after APPROVE, together with TD-186 |
| TD-203 | RF TFW-60/AB §6 O2 · third field report §7 item 2 | Med | `.tfw/templates/team/profile.md`:12–14, 27–33 | Says profiles cover "humans and agents alike", then that `team/` holds people and agent profiles are unusable until TFW-54. Shipped to consumers; the third report's operator read both. Outside the approved surface | → scoped follow-up (payload template pass) |
| TD-204 | RF TFW-60/AB §6 O3 · third field report §7 item 5 | Med | `.tfw/adapters/antigravity/tfw-rules.md.template`:5–7, `.agent/rules/tfw.md`:5–8 | Adapter source requires a `{version}` substitution on every update while the rendered rule reads `.tfw/VERSION`; the substitution was missed twice in a consumer, which then announced "TFW 0.8.5" for two releases. Align source with rendering | → scoped adapter update |
| TD-205 | REVIEW TFW-60/AB §3 row 4 | Low | `tasks/TFW-60__conflict_resistant_shared_workspace/phase-ab/journal/` | The phase journal holds one event (ONB → execution, 16:55:40); the RF completion that set `updated: 20260829-173155` has no event. The state file says where the phase is; the journal does not say how it got to RF | → REVISE round: one clock-read event on re-entry, stating the gap; nothing back-dated |

## 6. Traces Updated

- [x] the phase's `status.md` — `lifecycle: RF` unchanged (REVISE returns to execution, same task, as in `20260829-062100__transition__b2dc.md`); `updated` set from the clock; `transition` event written to `phase-ab/journal/` as `{stamp}__transition__{token}.md` with `from: RF`, `to: RF`
- [ ] HL status — unchanged; the phase is not complete
- [x] the phase's `status.md` — `updated` reflects this review. No counter is incremented
- [x] Other project files — `TECH_DEBT.md` appended TD-200–TD-205; TD-197 left ⬜ Open with a note that the canon and validator half closed at `ecfceee` and the template half is TD-200
- [ ] tfw-docs: **Pending APPROVE** — first items TD-202 (D68, §3 Legacy) and TD-186
- [ ] tfw-knowledge: **N/A for this review** — no fact candidates below; pending candidates from Phase AA still stand

## 7. Fact Candidates

> fact-candidates: processed 2026-08-30

No fact candidates from this review. The human rulings that shaped Phase AB — the grammar lands in this phase rather than after `2.0.0`, no fourth external run gates the release, `HD-30b` is a closed sub-item and stays untouched, `ABT` is approved for a disposable fixture — are already recorded in HL §12 A5, TS §2 and ONB answers 1–3, and nothing human-only was added during this review session. The reviewer's own observations (a test that asserts a literal guarantee string enshrines the constant it should be checking; a rewrite that shortens a workflow can widen a local fact into a false one) are analysis, and belong in §4 where they are.

---

*REVIEW — TFW-60 / Phase AB: Honest Migration | 2026-08-29*
