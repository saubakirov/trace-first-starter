# TS — TFW-56: Remove the Review Mode Axis

> **Date**: 2026-08-13
> **Author**: Coordinator (Claude Code)
> **Status**: 🟡 TS — approved by the owner 2026-08-13
> **Parent HL**: [HL-TFW-56](HL-TFW-56__review_mode_removal.md) — 🔒 FROZEN, re-frozen 2026-08-13 after A1–A5, A7
> **Contract baseline**: `git log -E --grep="^\[[^]]*/TFW-56/freeze/"` — two commits: initial freeze and re-freeze
> **Research**: [iteration 1](research/iter1/RES.md) — 637 rows / 203 reviews / 3 installs. H3 refuted; the promotion set below is the corrected one

---

## 1. Objective

Delete the `code / docs / spec` **selection** from review — the config key, the 🛑 WAIT gate, three
byte-identical mode files and four template fields — and promote the checks it was gating into the
universal Judge checklist, so every review asks them instead of one genre in three. The selection is
what a 637-row measurement found to be ceremony (0 verdict flips in 203 reviews); the checks are not
(~8% firing, matching the universal rows they join). This is a single phase: 22 files touched, almost
entirely deletion, with one recorded grep as its acceptance test.

## 2. Scope

### In Scope

- Deletion of `.tfw/workflows/review/` and its three mode files
- `review.md`: mode step, WAIT gate and mode-file load removed; steps renumbered contiguously
- Universal Judge checklist corrected to **10 rows** — U2 sharpened, S1/S2/S4 promoted, Content quality dropped
- The three orphaned `docs`/`spec` verify actions given an unconditional home in `verify.md`, or declined in writing
- `Mode:` / `Review Mode` fields removed from all four templates
- `tfw.review.default_mode` removed from both config files; `min_verify_ratio` untouched
- `config.md` propagation table corrected
- `conventions.md` review entry + one anti-pattern; `glossary.md` name disambiguation
- Six adapter and entry-point copies re-synced
- Version bump, CHANGELOG entry naming the removed **key**, TD-106 closed

### Out of Scope

- **The general `update.md` removed-key rule** — A5 was narrowed by the owner to the CHANGELOG clause only. The framework-wide rule is deferred (HL §8)
- **The rigour axis** — 8 of 13 field qualifiers encode verification depth, not genre. Touching it means touching `min_verify_ratio`, which DoF-4 protects. Sibling task
- **Review consolidator / subagents** — TFW-45 addendum, downstream of TFW-53 Phase C
- **Goal defence in review** — TFW-53 Phase C owns it. This task must not pre-empt its enforcement site
- **Rewriting history** — existing REVIEW files keep their mode headers; past CHANGELOG entries stay as written
- **`min_verify_ratio` behaviour or value** — it survives the removal of its sibling key unchanged

## 3. Principles Check

| # | Principle (from HL §7) | Enforced by | Gate |
|---|----------------------|-------------|------|
| P1 | Delete, don't relabel | AC-1, AC-6 | Folder absent; no `Mode:` field, no `default_mode`, no `none` placeholder value anywhere — AC-12 grep |
| P2 | No coverage loss without a recorded home | AC-3, AC-4 | RF carries a row for each of the 8 checklist rows **and** each of the 3 verify actions: promoted / already covered / declined with reason |
| P3 | A check that cannot fail is not a check | AC-2 | Each promoted row ships with its measured firing rate cited; a row without one violates DoF-2 as sharpened by A6 |
| P4 | What to check is declared once | AC-1, AC-7 | No second declaration survives: no mode step, no config key, no propagation row |
| P5 | Explicit N/A over silent skip | AC-2 | Skipping a promoted row must be **visibly marked**; a silent ✅ fails the AC |
| P6 | Single Source of Truth, behavioural adapter parity | AC-9 | Six copies carry no mode reference and behave as `.tfw/` does |
| P7 | History is evidence, not debt | AC-12 | Existing REVIEW headers and past CHANGELOG entries unchanged in the diff |
| P8 | Structural enforcement over promise | AC-12 | The acceptance test is a recorded command with its output in the EV file, not a claim |

## 4. Affected Files

| File | Action | Description |
|------|--------|------------|
| `.tfw/workflows/review/code.md` | DELETE | 16 lines |
| `.tfw/workflows/review/docs.md` | DELETE | 13 lines |
| `.tfw/workflows/review/spec.md` | DELETE | 13 lines — folder becomes empty and goes with them |
| `.tfw/workflows/review.md` | MODIFY | Remove Step 1 (mode selection + 🛑 WAIT) and the mode-file load in Verify; renumber remaining steps contiguously; fix internal step references |
| `.tfw/templates/review/judge.md` | MODIFY | Remove `Mode:` and the Mode-Specific section; sharpen U2; add S1, S2, S4 with structural explicit-N/A grammar |
| `.tfw/templates/review/verify.md` | MODIFY | Remove `Mode:`; add the three `docs`/`spec` verify actions as unconditional, or none if declined |
| `.tfw/templates/review/map.md` | MODIFY | Remove `Mode:` |
| `.tfw/templates/REVIEW.md` | MODIFY | Remove `Review Mode` header field and the mode placeholder comment; realign §3 Judge table row-for-row with judge.md |
| `.tfw/project_config.yaml` | MODIFY | Remove `tfw.review.default_mode`; leave `min_verify_ratio` |
| `.tfw/templates/project_config.yaml` | MODIFY | Same |
| `.tfw/workflows/config.md` | MODIFY | Drop the `review.default_mode` row; correct the `review.min_verify_ratio` row's step pointer |
| `.tfw/conventions.md` | MODIFY | Review subfolder entry cleared of mode vocabulary; §14 anti-pattern added |
| `.tfw/glossary.md` | MODIFY | Disambiguate `Reviewer (AI — coordinator in review mode)` so "review mode" has one meaning |
| `.tfw/VERSION` | MODIFY | Bump |
| `.tfw/CHANGELOG.md` | MODIFY | New entry; `### Removed` names the config key, not only files |
| `.claude/commands/tfw-review.md` | MODIFY | Re-sync from `.tfw/workflows/review.md` |
| `.claude/commands/tfw-config.md` | MODIFY | Re-sync from `.tfw/workflows/config.md` |
| `.agent/workflows/tfw-review.md` | MODIFY | Re-sync |
| `.agent/workflows/tfw-config.md` | MODIFY | Re-sync |
| `.tfw/adapters/codex/skills/tfw-review/SKILL.md` | MODIFY | Remove the "review-mode WAIT gate" instruction |
| `.agents/skills/tfw-review/SKILL.md` | MODIFY | Same, installed copy |
| `TECH_DEBT.md` | MODIFY | Close TD-106 with the reason |
| `evidence/EV__TFW-56__review_mode_removal.md` | CREATE | Mandatory evidence artifact |

**Budget:** 0 new framework files (1 new evidence artifact), 19 modifications, 3 deletions — 22 framework
files touched. Project limits: 30 files, 15 new, 3000 LOC, 30 modified. Within budget on every axis;
net LOC is negative.

## 5. Acceptance Criteria

### AC-1: The selection is absent from the framework
No path remains by which a reviewer is asked to choose a review mode.
- [ ] `.tfw/workflows/review/` does not exist
- [ ] `review.md` contains no mode step, no mode WAIT gate, no mode-file load
- [ ] `review.md` steps are contiguous with Step 0 = Session Naming — the TFW-standard opening, which this file has never had
- [ ] Every internal reference in `review.md` to a renumbered step resolves to the intended step
Gate: `ls .tfw/workflows/review/` fails; read `review.md` end to end and confirm step numbering and internal references
Evidence: record the `ls` failure and the full renumbered step list in the EV file

### AC-2: The universal Judge checklist is the corrected ten rows
The checklist carries every check that survived the measurement, and no row without an evidenced rate.
- [ ] `judge.md` has no `Mode:` field and no Mode-Specific section
- [ ] U2 *Philosophy aligned* is sharpened to cover **design soundness** — whether the design itself serves the stated principles, not whether it is named well
- [ ] Three rows added: **S1 evidence sufficiency**, **S2 backward compatibility**, **S4 safety**
- [ ] S1 is worded so it cannot be read as U7: U7 asks whether evidence **exists**, S1 whether it **establishes the claim**
- [ ] *Content quality* is not present — it was the one true duplicate
- [ ] Each promoted row carries its measured firing rate as justification for being there
- [ ] Skipping a promoted row requires a **visible** mark; a silent ✅ is not a permitted way to skip
Gate: `judge.md` has exactly 10 universal rows; read S1 and U7 side by side and state in the RF why they cannot collapse
Evidence: fill the corrected checklist against one archived RF/REVIEW pair from this repository and record whether S1 and U7 produced **different** answers. If they produced the same answer, the naming failed and AC-2 is not met

### AC-3: Every removed check has a recorded home  [depends: AC-2]
Nothing disappears silently — the accounting is in the RF, not in the reviewer's memory.
- [ ] All eight mode checklist rows appear in the RF, each marked promoted (naming its destination), already covered (naming the universal row that holds it), or declined (with a reason)
- [ ] The accounting matches what the files actually do
Gate: cross-read the RF table against `judge.md`; any row whose stated destination is not in the file fails the AC
Evidence: N/A — this is a documentation-completeness check, verifiable by reading

### AC-4: The three orphaned verify actions have a home
They are Verify-stage actions, so a promoted Judge row does not rescue them.
- [ ] *spot-check 2-3 key claims/sources*, *check citations traceable to real artifacts*, *verify data claims against primary sources* are each either present in `verify.md` as an unconditional action, or declined in the RF with a written reason
- [ ] All four `code`-mode verify actions remain mandated — the build/test command by `verify.md` Checkpoint, the test-file check by the `review.md` Trust Protocol, the ratio and the DoD cross-check by `verify.md`
- [ ] `map.md` and `verify.md` carry no `Mode:` field
Gate: `grep` each action's substance in `verify.md`; for any declined action, confirm the RF carries the reason
Evidence: N/A — file content, verifiable by reading

### AC-5: The REVIEW template matches the new checklist  [depends: AC-2]
The synthesis document cannot list checks the stage file does not have, or omit ones it does.
- [ ] No `Review Mode` header field, no mode placeholder comment
- [ ] §3 Judge table matches `judge.md`'s ten rows one-for-one, in the same order
Gate: diff the two row lists; any mismatch fails
Evidence: N/A — template content

### AC-6: The config key is gone and its sibling is untouched
- [ ] `tfw.review.default_mode` absent from `.tfw/project_config.yaml` and `.tfw/templates/project_config.yaml`
- [ ] `min_verify_ratio` present in both, value `0.42`, with its comment intact and its meaning unchanged
Gate: `grep -n "review:" -A4` on both files
Evidence: record both file excerpts in the EV file — this is the one place where collateral damage would be silent

### AC-7: The propagation table is correct  [depends: AC-1]
- [ ] `config.md` no longer routes `review.default_mode`
- [ ] Its `review.min_verify_ratio` row names the correct step number in the renumbered workflow — the pointer is stale today and must not stay stale
Gate: read the row, open `review.md` at the named step, confirm it is the Verify step
Evidence: N/A — cross-reference check

### AC-8: Conventions and glossary carry no mode vocabulary
- [ ] The Review subfolder entry in `conventions.md` describes stage files without reference to modes
- [ ] `conventions.md` §14 carries a new anti-pattern: adding a review checklist row whose firing rate is not evidenced — so the axis cannot regrow under a new name
- [ ] `glossary.md` defines no review-mode term, and the phrase "review mode" has exactly one meaning across `.tfw/`
Gate: `grep -rn "review mode" .tfw/` — every remaining hit means the same thing
Evidence: N/A — text content

### AC-9: Adapter parity  [depends: AC-1, AC-7]
- [ ] All six adapter and entry-point copies carry no mode reference
- [ ] Each behaves as its `.tfw/` source does — parity is behavioural, not byte-level
- [ ] The Codex skill no longer instructs the agent to follow a "review-mode WAIT gate" that does not exist
Gate: `grep` the six files for mode vocabulary; diff each against its source for behavioural drift
Evidence: record the grep across all six paths in the EV file

### AC-10: Version and changelog  [depends: AC-1]
- [ ] `VERSION` bumped
- [ ] CHANGELOG entry records the deletion, the corrected promotion set and the revocation of the mode-file decision
- [ ] Its `### Removed` block **names `tfw.review.default_mode` explicitly** — `/tfw-update` triages files, so a removed key is otherwise invisible to a project upgrading
Gate: read the entry; confirm the key appears by name
Evidence: N/A — changelog content

### AC-11: TD-106 closed
- [ ] `TECH_DEBT.md` marks TD-106 closed with the reason: the non-standard Step 0/Step 1 anomaly was deleted, not annotated
Gate: read the row
Evidence: N/A

### AC-12: The sweep is complete and history is intact  [depends: AC-1..AC-11]
The acceptance test is a command, not a claim.
- [ ] `grep -rn "code / docs / spec\|default_mode: code\|Review Mode\|review/{code" .tfw/ .claude/ .agent/ .agents/ --exclude=CHANGELOG.md` returns zero matches
- [ ] No existing task REVIEW file is modified — every `Review Mode` header in `tasks/` survives unchanged
- [ ] No past CHANGELOG entry is edited; only a new entry is added
- [ ] `git diff --stat` shows 3 deletions and no framework file created
Gate: the grep, plus `git status`/`git diff --stat` confirming nothing under `tasks/` was touched except this task's own artifacts
Evidence: record the grep command **with its output**, the diffstat, and the count of surviving `Review Mode` headers in `tasks/`

### Evidence Artifacts

| File | Description |
|------|-------------|
| `evidence/EV__TFW-56__review_mode_removal.md` | Environment header; per-AC table; the recorded grep gate with output; the deleted-folder check; both config excerpts; the six-adapter grep; the diffstat; and the S1-vs-U7 dry-run result _(required)_ |

## 6. Technical Guidance

> Reference material, not instructions. Deviate with justification in the RF.

- **The renumbering trap is documented and this is its second occurrence.** TD-106 exists because `review.md` was renumbered once before: it is the only TFW workflow whose Step 0 was not Session Naming. Removing the mode step finally makes it standard. Check `config.md` and its two adapter copies — they still point at "Step 0: Select Review Mode", which has been Step 1 since an earlier task. They are already wrong, and they are in scope.
- **The three mode files are byte-identical across three separate TFW installs.** Read them before deleting so the coverage accounting in AC-3 is line-based rather than remembered.
- **The measured firing rates**, for AC-2's justification: Analytical quality 25.0% · Test coverage 23.4% · Source attribution 22.2% · Source verification 12.5% — these four are S1, combined 16.1% across 174 rows. Breaking changes 8.5% → S2. Content quality 5.9% → dropped. Code quality 4.5%, six hard failures, all contract violations rather than style → S3, folded into U2. Security 4.0% → S4, retained on consequence rather than rate.
- **Adapters under `.claude/` and `.agent/` are full copies, not thin references** — re-sync means overwrite from the `.tfw/` source, then re-read to confirm nothing project-specific was clobbered.
- **`min_verify_ratio` is the collateral-damage risk.** It lives in the same `tfw.review` block as the key being removed. AC-6 exists specifically to prove it survived.
- **Shared files with TFW-53 Phase C:** `review.md`, `judge.md`, `REVIEW.md`, `glossary.md`, `conventions.md` §14. Phase C will replace U2's mapping-integrity check with a substantive purpose check — so **sharpen U2, do not restructure it**, and leave the Judge template's overall shape intact. If a change here would make Phase C's frozen deliverables unlandable, stop and report rather than solving it.
- **Line endings:** this repository has CRLF working-copy files. Do not reformat whole files; keep diffs to the lines that change.

## 7. Definition of Failure

- ❌ A check or verify action available today disappears without a recorded home in the RF
- ❌ A promoted row ships without its measured firing rate, or the promoted set exceeds ten rows
- ❌ S1 and U7 are worded so that a reviewer answers them the same way — the naming is the deliverable, not decoration
- ❌ A stale step reference survives anywhere in `.tfw/` or the six adapter copies
- ❌ `min_verify_ratio` changes value, comment or behaviour
- ❌ Any existing task REVIEW file or past CHANGELOG entry is edited
- ❌ Adapters left desynced, or the Codex skill still naming a WAIT gate that no longer exists
- ❌ The axis is renamed rather than removed — a "for information" mode field, a `default_mode: none`, or an empty `review/` folder
- ❌ The grep gate is reported as passing without its output recorded in the EV file
- ❌ A change here forces an amendment against TFW-53's frozen sections

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Renumbering leaves a stale pointer — the exact trap TD-106 records | AC-1 reads the file end to end; AC-7 resolves the one known external pointer; AC-12's grep is the backstop |
| S1 collapses into U7 within a few reviews | AC-2's Evidence is a real dry-run against an archived review, and a same-answer outcome fails the AC rather than being noted as a caveat |
| Ten rows is at the edge of the readable band | U2 absorbs S3 instead of an eleventh row being added — the owner-approved modification. No further row may be added in this task |
| `min_verify_ratio` damaged as collateral | AC-6, with both file excerpts recorded as evidence |
| Collision with TFW-53 Phase C in five shared files | §6 constrains the U2 change to a sharpening; DoF forbids resolving any conflict by touching TFW-53's frozen sections. This task lands first by owner decision |
| Adapter copies drift because they are full copies | AC-9 checks behaviour, not bytes, and names the Codex skill line explicitly |
| The deletion looks like simplification while quietly losing the strongest check | AC-3 and AC-4 exist for precisely this; the whole reason the frozen contract was amended is that the first version of this task would have lost about two thirds of S1 |

---

*TS — TFW-56: Remove the Review Mode Axis | 2026-08-13*
