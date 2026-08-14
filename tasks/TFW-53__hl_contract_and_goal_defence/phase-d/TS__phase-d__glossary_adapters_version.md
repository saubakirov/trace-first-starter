# TS — TFW-53 / Phase D: Glossary, Adapters and Version

> **Date**: 2026-08-13
> **Author**: Coordinator (Claude Code)
> **Status**: 🟡 TS_DRAFT — **approved by the owner 2026-08-13** · **amended 2026-08-14 after ONB**: six measurements corrected from the executor's re-measurement (glossary parent heading, article median, and four terminology counts), Q1 `uncommitted baseline` ruled out of mandate, Q2 the HL north-star field label enters AC-2, Q3 TD-158 re-routed out, R6 overruled as a recorded two-row scope extension in `CLAUDE.md`
> **Parent HL**: [HL-TFW-53](../HL-TFW-53__hl_contract_and_goal_defence.md) — 🔒 FROZEN
> **Covers**: frozen DoD 30–33
> **Predecessors read** (Pre-TS gate): [RF Phase C](../phase-c/RF__phase-c__goal_defence_in_review.md), [REVIEW Phase C](../phase-c/REVIEW__phase-c__goal_defence_in_review.md) — ✅ APPROVE, second pass · [RF Phase B](../phase-b/RF__phase-b__enforcement_in_workflows.md) · [RF TFW-56](../../TFW-56__review_mode_removal/RF__TFW-56__review_mode_removal.md)

---

## 1. Objective

Phases A, B and C built a contract, an enforcement path and a defender. All three exist in `.tfw/` and in exactly one of the three tool surfaces. This phase makes the work **portable and findable**: the vocabulary the task invented gets defined instead of merely used, the same concept stops carrying three names, and every adapter copy runs the same workflow the framework defines. Then the version bump ships it.

This is the gate where *we built it* becomes *everyone gets it*. It is not a refactor: nothing is redesigned, no section content is rewritten, and no mechanism is reopened.

## 2. Scope

### In Scope

- `glossary.md` — ten articles: the nine terms DoD-30 names, plus the missing `Result Visualization`
- Terminology consistency: one name per concept across `conventions.md`, `glossary.md`, templates and workflows
- **All 14 drifted adapter copies** re-synced, plus the entry points and the Codex skills
- `VERSION`, `CHANGELOG.md`, `project_config.yaml` `tfw.version`, and the TFW-54 pointer
- Five debts that fall inside this phase's mandate: **TD-157, TD-163, TD-164, TD-165, TD-167**

### Out of Scope

- **Rewriting any section's content.** HL §7.1: *"D changes no section content, only terminology consistency."* A synonym becomes the canonical term; a sentence does not become a better sentence
- **Six debts routed here by earlier reviews that do not belong** — see §6 for the reasoning and the re-routing: TD-120, TD-140, TD-142, TD-153, TD-154, TD-155
- Phase E (rejected-task traces) — independent, not blocked by this phase
- Any part of the AT execution mode (HL DoF-4)

## 3. Principles Check

| # | Principle (HL §7) | Enforced by | Gate |
|---|-------------------|-------------|------|
| P9 | Naming creates behavior | AC-1, AC-2 | Every term this task invented is defined; the measured three-name drift resolves to one |
| P8 | Tool-agnostic by behavior | AC-3, AC-4 | The drift check prints nothing; all three surfaces run the same workflow |
| P3 | Structural enforcement over guidelines | AC-3 | The acceptance test is a recorded command, not a claim that the sweep was done |
| P7 | Token density | AC-2, AC-7 | `plan.md` and `review.md` are within 25 words of the hard budget; substitutions must be word-neutral or negative |
| P12 | A frozen baseline must be diffable | AC-6 | TD-164 — the recovery form belongs in one place, and the template is currently the fourth copy |
| P1, P2, P4, P5, P6, P10–P17 | contract mechanics, purpose defence, traces | N/A | Discharged in Phases A–C, or Phase E. This phase changes no mechanism |

## 4. Affected Files

| File | Action | Description |
|------|--------|------------|
| `.tfw/glossary.md` | MODIFY | Ten articles; the `Phase 0` stale pointer (TD-163) |
| `.tfw/conventions.md` | MODIFY | **Terminology only.** It currently uses all three baseline synonyms |
| `.tfw/templates/HL.md` | MODIFY | TD-164 — the recovery command replaced by a pointer to `conventions.md` §3 rule 15; terminology |
| `.tfw/templates/review/judge.md` | MODIFY | Terminology only (3 baseline occurrences) |
| `.tfw/workflows/review.md` | MODIFY | Terminology only — **word-neutral or negative**, the file is at 1,176 of 1,200 |
| `.tfw/workflows/plan.md` | MODIFY | Terminology only — **word-neutral or negative**, the file is at 1,195 of 1,200 |
| `.tfw/compilable_contract.md` | MODIFY | TD-165 (`NS{N}`/`PP{N}` resolution behaviour) and TD-167 (second stale `KNOWLEDGE.md` §0 reference) |
| `.claude/commands/tfw-*.md` × 7 | MODIFY | Re-copied from source: plan, review, research, init, handoff, update, knowledge |
| `.agent/workflows/tfw-*.md` × 7 | MODIFY | Same seven |
| `.tfw/adapters/codex/skills/tfw-{plan,review}/SKILL.md` | MODIFY | Behavioural parity check; edit only if a statement is now false |
| `.agents/skills/tfw-{plan,review}/SKILL.md` | MODIFY | Same |
| `CLAUDE.md`, `AGENTS.md` | MODIFY | The command table understates both workflows — see AC-4 |
| `.tfw/VERSION`, `.tfw/project_config.yaml` | MODIFY | `1.1.0` → `1.2.0`; `tfw.version` moves in lockstep (RF TFW-56 FC2) |
| `.tfw/CHANGELOG.md` | MODIFY | One entry covering Phases A–D, with the TFW-54 pointer |
| `TECH_DEBT.md`, `README.md` | MODIFY | Five closures; board row |
| `phase-d/evidence/EV__phase-d__glossary_adapters_version.md` | CREATE | Structured evidence |

**Budget:** 1 new, **28 modified** against a 30 limit — and **14 of the 28 are `cp`** with zero authored content. Not split into two phases: splitting core from adapters is the TFW-42/C and TFW-46/C precedent that opens a desync window and buys a second review cycle for a phase whose acceptance test is one command.

## 5. Acceptance Criteria

### AC-1: The vocabulary is defined, not merely used

Eight of the ten terms have **zero occurrences** in `glossary.md` today, measured. A term five files use and no file defines is jargon.

- [ ] Articles exist for: **HL Contract · Contract Baseline · Frozen Section · Amendment · Amendment Log · Project North Star · Purpose Check · `not fit for purpose` · `deferral confession`** (DoD-30)
- [ ] The nine ship as `###` entries under **one new `## Contract and Purpose Defence` grouping**, placed after `## Artifact Types`, in DoD-30's order _(ONB R1)_
- [ ] Plus **Result Visualization**, placed **between `### Value Flow` and `### Findings Map` under `## Knowledge Terms`** — where both siblings actually live _(corrected 2026-08-14, ONB §6.1: the TS named `## Artifact Types`, which is wrong; the operative requirement is "beside its siblings")_. Content per HL §4 Phase D deliverable 1: what the finished outcome looks like, written from the finished state, rendered visually, showing the value and not only the artifact — the owner's checkpoint before the spend, not an illustration of the plan
- [ ] Each article matches the house length. Measured across the 78 entries: median **35** words, p75 **50**, max 296 (the PV Index, a table) _(corrected from "40", ONB §6.4)_. **Ceiling is p75 = 50 words per article**; report per-article `wc -w`. An article that needs 150 is restating a rule that belongs in `conventions.md`
- [ ] Each article ends with a `→` pointer to the rule that governs it, following the existing entries' pattern
- [ ] `Amendment` and `Amendment Log` are distinguishable by their first sentence — one is a proposal against a frozen claim, the other is the log that carries it. Two adjacent entries with converging definitions collapse into one within a few reads (the S1-vs-U7 lesson from TFW-56)

Gate: **case-insensitive** `grep -ci` each term in `glossary.md` → ≥1; `wc -w` per article. _(Case-sensitive would fail `deferral confession`, which ships capitalised at `judge.md`:50 — ONB §6.5.)_
Evidence: the ten articles, quoted

### AC-2: One name per concept [depends: AC-1]

Measured drift, case-sensitive, across `.tfw/**` excluding `CHANGELOG.md`:

> **Table corrected 2026-08-14 from the ONB's re-measurement, reproduced by the coordinator.** The
> original claimed three baseline names in six files; there are **two**, in five.

| Concept | Names in use today | Occurrences |
|---|---|---|
| The point the contract is frozen at | `frozen baseline` · `Contract Baseline` · one hybrid | **8** in five files · **2** in `conventions.md` (`:73` is already the canonical heading, `:94` reads *"frozen contract baseline"*) · `judge.md`:34 *"committed frozen baseline"* fuses both retired forms |
| The anchor above the task | `Project North Star` · bare `North Star` · lower-case `north star` | **5** · **2 genuine**, both the north-star field label and its explainer in `templates/HL.md`:18 and `:20` · **13**, permitted after first full mention |

> **`uncommitted baseline` is not a third name and is out of mandate** _(ONB Q1)_. Its two occurrences —
> `conventions.md`:75 and `plan.md`:60 — name the **absence** of a baseline. `grep -rnE "[^n]committed baseline"`
> returns 0 today. Substituting into them produces a sentence that means its opposite, and repairing that is a
> rewrite, which DoF-1 forbids. Leave both untouched; record the exclusion in the before/after table.

- [ ] **`Contract Baseline` is canonical** — chosen by frozen DoD-30, which names it as the term to define, not by preference. Phrases like *"at its frozen baseline"* become *"at its contract baseline"*: same word count
- [ ] **`Project North Star` is canonical.** One capitalised form only. Bare lower-case `north star` in running prose is permitted after the first full mention in a file — that is ordinary English, not drift. Capitalised `North Star` without `Project` **is** the drift, because it reads as a second defined term
- [ ] **`templates/HL.md`:18 and `:20` are renamed** — the north-star **field label** and its explainer, the two genuine bare-capital occurrences _(ONB Q2)_. A form field that says `North Star` while the glossary defines `Project North Star` teaches the wrong name at the moment the reader is learning it. The field sits **below** the contract block, so §9's restriction does not reach it. 2 lines, +2 words, in a template off the F2 budget
- [ ] `plan.md` and `review.md` do not grow. They sit at 1,195 and 1,176 against a 1,200 hard budget; a substitution that adds a word must find one to remove in the same sentence
- [ ] Any *third* synonym pair found while sweeping is **reported in RF §6, not fixed** — the mandate is the two concepts above, and a consistency pass that keeps finding new work is how a cleanup phase becomes a rewrite

Gate: `grep -rn` each retired form across `.tfw/` excluding `CHANGELOG.md` → 0; `wc -w` on both workflows before and after
Evidence: the before/after occurrence table and the two word counts

### AC-3: Every adapter copy runs what the framework defines

The drift check in `config.md` currently prints **14 lines**. Six are this task's doing (`tfw-plan` 82 diff lines × 2 folders, `tfw-review` 12 × 2, `tfw-research` 6 × 2); eight are pre-existing and belong to earlier tasks (`tfw-init` 41 × 2, `tfw-handoff` 14 × 2, `tfw-update` 12 × 2, `tfw-knowledge` 2 × 2).

- [ ] **All fourteen** are re-copied. Owner decision 2026-08-13: a binary check that keeps printing eight failures after the phase whose deliverable is adapter parity stops being read — the same mechanism that produced 0 of 38 evidence folders while the folder was optional (D53)
- [ ] The RF states the split — which six were ours, which eight were not — so a reviewer sees the boundary rather than inferring scope creep
- [ ] Direction verified before copying: `.tfw/` is **ahead** of every copy, so this propagates already-reviewed content. If any copy turns out to be ahead of its source, **stop and report** — that is an undocumented edit in an adapter, not a sync
- [ ] The drift check is run **after** the sync and its silent output recorded with its exit status
- [ ] Codex and `.agents` skills are thin routers (180 and 153 words), not copies. Check them for statements that are now false and edit only those. Both were verified clean of mode vocabulary by TFW-56; the check here is for contract and purpose vocabulary

Gate: the `config.md` drift check → no output; `diff` per copy → empty
Evidence: the check's output before (14 lines) and after (silent), both recorded verbatim

**Note on DoD-32.** It reads *"adapter and entry-point copies of every changed workflow are re-synced (`tfw-plan`, `tfw-review` …)"*. Its parenthetical omits `tfw-research`, which Phase B changed — the general clause covers it, so no amendment. The eight unrelated copies are outside DoD-32 entirely and enter as a rule-6 refinement on owner instruction: DoD-32 stays satisfied and no DoF item is touched.

### AC-4: The entry points describe what the workflows now do

- [ ] `CLAUDE.md`'s command table says `/tfw-plan` does *"Research, write HL, RESEARCH gate, scope decision, write TS"* and `/tfw-review` does *"Review RF against checklist, write REVIEW"*. Both are now incomplete: plan freezes the contract and routes amendments, review defends goals against the contract baseline. Two cells, a few words each
- [ ] `AGENTS.md` carries the same table without a description column — check and change only if something is false
- [ ] **`CLAUDE.md`'s table gains the two rows it is missing** — `/tfw-knowledge` and `/tfw-config`, both of which `AGENTS.md` carries. **Coordinator scope extension, recorded 2026-08-14** _(ONB R6, overruling the executor's report-not-fix recommendation)_: DoD-32 does not cover these two, because this task did not change them. The ground is that `CLAUDE.md` is the entry point a Claude session reads, `/tfw-knowledge` is a mandatory KNW-stage workflow, and omitting it makes that workflow invisible to the surface it serves. **Limit: two rows, no other change to `CLAUDE.md`**
- [ ] No new section is added to either file. They are entry points, not documentation (F22)

Gate: read both tables against `plan.md` Step 4/6c/6d and `review.md` Step 3
Evidence: N/A — textual

### AC-5: The release is shippable and its purpose is not orphaned

- [ ] `VERSION` `1.1.0` → **`1.2.0`**, and `project_config.yaml` `tfw.version` with it — the two have moved in lockstep on every release since 0.8.5, and letting them disagree here would be the first time (RF TFW-56 FC2)
- [ ] `CHANGELOG.md` carries **one entry for Phases A–D**, not four. `### Added` names the HL contract, §12 Amendment Log, the Purpose Check and PV priority 0; `### Changed` names `plan.md` Step 6c's inversion and the retirement of the Judge mapping-integrity check; `### Removed` names what is gone by name, per the rule TFW-56 established for keys a file-level upgrade cannot surface
- [ ] The **TFW-54 pointer is recorded** (DoD-33). `TFW-54` currently appears **zero times** anywhere in `.tfw/`. The contract exists to make delegation safe; without the pointer the reason is legible only inside this task's folder
- [ ] Both `## [Unreleased]` bullets are folded into `1.2.0 ### Changed`, and the Adapter Sync bullet's closing sentence is **corrected, not carried verbatim** _(ONB R4)_. It currently reads *"First run of the check found 12 drifted copies (6 workflows × 2 folders) — recorded, not yet repaired."* Both halves are stale on this phase: the count is **14** (7 × 2) and the repair is AC-3. Folding it as written ships a release note that is false about the release it announces, on the day it ships, in the number that release corrects

Gate: `cat .tfw/VERSION`; `grep -c "tfw.version: 1.2.0" .tfw/project_config.yaml`; `grep -c "TFW-54" .tfw/CHANGELOG.md`
Evidence: the entry, quoted

### AC-6: Five debts close, and TD-164 closes first

- [ ] **TD-164 (High)** — `templates/HL.md`:10 carries a fourth copy of the baseline recovery command. Amendment A13 removed that form from this task's HL at all three occurrences and pointed at `conventions.md` §3 rule 15; the template was missed, so **every future HL is still born carrying it**. Replace with the same pointer. This is the single-source-of-truth rule broken at the most visible point in the framework
- [ ] **TD-163** — `glossary.md`:213 places the Knowledge Gate in *"Phase 0 of `plan.md`"*; `plan.md` has Steps 0–7 and no Phase 0
- [ ] **TD-165** — `compilable_contract.md`:81: `NS{N}` and `PP{N}` are declared in the §2 pattern table while the Resolution rules still read `D{N}, P{N}, F{N}, TD-{N} → anchor links`. A reference pattern that resolves nowhere is a rule with no enforcement site (F4), and the build script silently will not link either namespace. **The gap is wider than the debt says** _(ONB §5.4)_: `gen_docs.py` resolves only `TD-{N}` and `D{N}`, so `P{N}` and `F{N}` are already aspirational in that same line. Adding NS/PP keeps them at their neighbours' grain rather than inventing a claim. **File one new debt covering all four patterns**, naming the resolver as the site; extending `gen_docs.py` stays out of scope
- [ ] **TD-167** — `compilable_contract.md`:65: *"Where references appear"* opens with `KNOWLEDGE.md §0 Source column`, a section D37 removed in April. Six lines below the one Phase C corrected
- [ ] **TD-157** — closed by AC-3
- [ ] Each closure records **the reason**, not just the status

Gate: open each named line; `python -m pytest docs/scripts/` still passes
Evidence: before/after for each of the five

### AC-7: The phase changed no content it was not asked to change

The named risk of a consistency phase is that "consistency" becomes a licence to improve prose. HL §7.1 forbids it in as many words.

- [ ] Every diff hunk in `conventions.md`, `judge.md`, `review.md`, `plan.md` and `HL.md` is one of: a canonical-term substitution, a named debt fix, or a `cp`. No hunk is a rewritten sentence
- [ ] `git diff --stat` on the six framework files is reported with a one-line justification per file
- [ ] No section is added anywhere, and no template gains a field (F22)

Gate: `git diff` reviewed hunk by hunk against this list
Evidence: the diffstat with per-file justification

### Evidence Artifacts

| File | Description |
|------|-------------|
| `evidence/EV__phase-d__glossary_adapters_version.md` | Environment header, per-AC table, verdict _(required)_ |

## 6. Technical Guidance

> Reference material, not instructions. Deviate with justification in the RF.

**Six debts were routed here by earlier reviews and are being re-routed out. The reasoning, so the RF does not have to re-derive it:**

| Debt | Why not Phase D | Where it goes |
|---|---|---|
| TD-140 (`HL.md` +76% in one phase), TD-142 (Phase A's artifacts are the largest in the repo) | Artifact growth, not naming. This is TFW-57's entire subject and TD-142 already says so | [TFW-57](../../TFW-57__artifact_growth_control/PROPOSAL__TFW-57__artifact_growth_control.md) |
| TD-153 (`RES.md`'s two classes cannot hold TS-aimed output), TD-154 (`plan.md` 6d has no `🚫 WITHDRAWN` path) | Gaps in a mechanism, not inconsistencies in a name. TD-154 also has nowhere to land: 14 words against 5 of headroom | Follow-up task |
| TD-155 (the re-freeze trigger reads *"after an approved amendment"* but fired after a refinement) | It is a rewording of `conventions.md` §3 rules 13–15 — **Phase A's section**. HL §7.1 forbids this phase from rewriting another phase's entries, and that outranks a debt row's routing note written before the ownership rule existed | Follow-up task, or a Phase A amendment if it proves substantive |
| TD-158 (`HL.md` §3.1 bullet 2 lists *"a narrative timeline"* in the bullet ending *"Prose alone is not a rendering"*) | **Added 2026-08-14, ONB Q3.** Its row pointed at Phase D and it appeared in neither TS list — my omission: the re-route list was built from the Phase C review's rows and `TECH_DEBT.md` was never re-scanned for older ones. It fails the same two tests as TD-155: a sentence rewrite (DoF-1) inside Phase A's section (§7.1). **The executor re-scans for any other row pointing here and reports what it finds** | Follow-up task |
| TD-120 (EV template absent from the Source Manifest) | Neither naming nor adapters | Backlog |

**The two workflows are effectively full.** `plan.md` 1,195 and `review.md` 1,176 against F2's 1,200 hard limit. Phase D adds nothing to either, so this does not block the phase — but it means any substitution must be word-neutral, and it is the strongest available argument for TFW-57.

**`judge.md` went 639 → 1,165 words in Phase C.** It is a template, so F2 does not bind it, and Phase C's design put the mechanism in a block below the table precisely to keep `review.md` off the budget. Recorded as an observation for TFW-57, not as a defect of this phase. Do not compress it here.

**Glossary placement.** `Value Flow` (line 50) and `Findings Map` (line 53) are `###` entries under `## Artifact Types`. `Result Visualization` joins them there. The contract terms are a different kind and may need their own `##` grouping — the existing file has 78 entries under 33 groupings, so adding one is in keeping.

**Direction of the adapter copy.** Confirm with `diff` per pair before copying, not after. The whole sync is safe only because `.tfw/` is canonical and ahead everywhere; a copy that is ahead of its source means someone edited an adapter directly, which is a finding, not a merge.

## 7. Definition of Failure

- ❌ A sentence is rewritten under the consistency banner — HL §7.1's explicit prohibition, and the way a cleanup phase becomes a redesign
- ❌ `plan.md` or `review.md` crosses 1,200 words
- ❌ The drift check still prints after the sync, or the sync is reported without the check having been run (`config.md`'s own anti-pattern)
- ❌ An adapter copy is found ahead of its source and merged instead of reported
- ❌ A glossary article restates a rule instead of defining a term — the article is 150 words and `conventions.md` already says it
- ❌ TD-164 is closed by editing the template's copy of the command rather than replacing it with the pointer — the defect is the fourth copy existing, not its wording
- ❌ A re-routed debt (TD-140, TD-142, TD-153, TD-154, TD-155, TD-120) is fixed here anyway
- ❌ `VERSION` and `tfw.version` disagree
- ❌ The version ships without the TFW-54 pointer, orphaning the contract's stated purpose

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| The consistency sweep keeps finding new synonym pairs and the phase never ends | AC-2's last bullet: report a third pair, do not fix it. The mandate is two concepts, both measured |
| Copying eight unrelated adapters ships something unreviewed | Direction check first: `.tfw/` is ahead everywhere, so the copy propagates reviewed content. A copy ahead of source stops the phase |
| 28 modified files against a 30 budget | 14 are `cp`. Splitting would open a desync window — the TFW-42/C precedent — for a phase whose acceptance test is one command |
| A glossary article contradicts the rule it names | Each article ends in a `→` pointer to its governing rule, so the two are read together |
| `CHANGELOG` for four phases becomes an essay | One entry, three blocks, named artifacts. The release note is a diff summary, not a retelling of the task |

## 9. Cross-Phase Modifications

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `.tfw/conventions.md` | A (§3, §14), B (§14), C (§3 north star, §14), E (§5, §13, §14) | D changes **terminology only** — never section content. Phase E has not run and may add to §5/§13/§14 after this |
| `.tfw/glossary.md` | C (PV Index priority 0) | D adds the term articles C deliberately did not pre-empt |
| `.tfw/templates/HL.md` | A (contract header, §12), B (§3.1) | D touches the header's recovery-command line (TD-164) and nothing else in the contract block |
| `README.md` | concurrent TFW-55 session | Stage by explicit path. If the board row is held, leave it uncommitted and say so — the coordinator lands it |

---

*TS — TFW-53 / Phase D: Glossary, Adapters and Version | 2026-08-13*
