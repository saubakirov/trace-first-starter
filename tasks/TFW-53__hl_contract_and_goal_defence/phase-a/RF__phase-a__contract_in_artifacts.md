# RF — TFW-53 / Phase A: Contract in Artifacts

> **Date**: 2026-08-13
> **Author**: Executor (Claude Code)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-53](../HL-TFW-53__hl_contract_and_goal_defence.md) — 🔒 FROZEN
> **TS**: [TS Phase A](TS__phase-a__contract_in_artifacts.md)
> **ONB**: [ONB Phase A](ONB__phase-a__contract_in_artifacts.md) — 2 blocking questions, both answered

---

## 1. What Was Done

### New Files

| File | Description |
|------|------------|
| `tasks/TFW-53__hl_contract_and_goal_defence/phase-a/evidence/EV__phase-a__contract_in_artifacts.md` | Structured evidence: environment, per-AC table, verdict, three detailed exhibits (E2, E9, E11) |
| `tasks/TFW-53__hl_contract_and_goal_defence/phase-a/evidence/baseline_recovery.txt` | AC-6 — the documented recovery command run on live history under both shells, plus the rejected form and the pre-rule baseline |
| `tasks/TFW-53__hl_contract_and_goal_defence/phase-a/evidence/classification_exercise.md` | AC-8 — five discriminating RES iter1 rows classified from the shipped rule text alone, circularity limit stated first |

**Zero new framework files.** The phase adds nothing to `.tfw/` and nothing to a project's root — HL §3.1's *"0 new artifacts in a project's root"* claim holds.

### Modified Files

| File | Changes |
|------|---------|
| `.tfw/templates/HL.md` | Contract header block (5 fields + a field-usage note, left open for Phase C); three-state marker on every section heading (`🔒 FROZEN` / `🟢 FREE` / `🟢 APPEND-ONLY`) plus a subsection-inheritance rule; new `## 12. Amendment Log` with 10-column grammar, `Type` and `Verdict` vocabularies, append-only/no-edit-before-verdict/remark-is-not-a-verdict instruction and the `No amendments.` default; §3.1 gate clause block appended (4 properties + checkpoint statement). +92 / −6 |
| `.tfw/templates/RES.md` | `HL Update Recommendations` rewritten as two classed tables — `Refinements` (free sections, coordinator applies) and `Amendment Proposals` (frozen sections, owner verdict required, AC-2 column grammar minus the two fields a researcher cannot fill); classify-never-apply instruction; explicit-N/A for both classes; **line 32 `<!-- … Coordinator applies these. -->` deleted**. +34 / −4 |
| `.tfw/conventions.md` | §3 → new `#### HL Contract` subsection: state table + 21 numbered rules across four groups (contract, Contract Baseline, delegated authority, Phase HL); §5 → REJECT branch (a) redefined as filing an amendment, verdict vocabulary untouched; §14 → 7 anti-patterns appended. +55 / −0 |

**Total: 165 insertions, 16 deletions, 3 files modified, 0 framework files created.** Budget (30 files / 15 new / 3000 LOC / 30 modified): within all four by an order of magnitude.

## 2. Key Decisions

1. **`🚫 WITHDRAWN` added to the §12 verdict vocabulary** — the single substantive addition beyond the TS. AC-2's Evidence clause asked for a diff of the shipped grammar against the live rows *"and record any field the template cannot hold"*. Row A11 of HL-TFW-53 §12 is `🚫 WITHDRAWN by the coordinator, 2026-08-10`, and the drafted four-value vocabulary had no home for it. Recording the gap without closing it would have shipped a template that cannot carry the artifact AC-2 names as its test corpus. Constrained to retraction *by the proposer*, *before a ruling* — deleting the row would break append-only, and `❌ REJECTED` would credit the owner with a decision they never made. Full exhibit: EV §E2.
2. **The tripwire is time-scoped: "under §5 and §6 *as they stand at the moment of classification*."** Six words added during the AC-8 exercise, which surfaced the ambiguity: row A1 classifies as an amendment against the contract of 2026-08-08 and as a refinement against the contract of today, because A1's own approval added the DoD items that now accept it. Both readings were defensible from the draft text. Full exhibit: `classification_exercise.md` §Finding.
3. **Subsection state is inherited, not repeated.** §3.1/§3.2 are frozen with §3, §7.1 with §7; only §7.2 carries its own marker because it is the one subsection whose state differs from its parent. The alternative — marking every subsection — puts three markers on §3 alone and makes the template noisier without adding information. Stated as one rule in the template.
4. **The §3.1 gate is appended, never a rewrite.** The pre-existing Working Backwards paragraph, the four format options and the §3.2 contrast survive verbatim; the new block reframes the options as *choices of which rendering* rather than permission to skip one. DoF and AC-11's last bullet both required this.
5. **No budget, slot, size, count or cut-order language anywhere** — amendment A12 removed the property from the contract on 2026-08-10. Verified by grep, recorded in RF §4.
6. **`conventions.md` rules are numbered continuously across the four groups (1–21) rather than restarting per group.** A reviewer or a later phase can cite "rule 15" unambiguously; restarting the count would create three different rule 1s inside one subsection.
7. **RES `Amendment Proposals` carries 7 of §12's 10 columns.** `#`, `Date` and `Proposer` are added by the coordinator on transcription and `Verdict` opens as `PROPOSED` — a researcher cannot fill any of the four. The mapping is stated in the template so the transcription is mechanical rather than interpretive.
8. **Build gate substituted, with the substitution recorded.** `project_config.yaml` `build.lint/test/verify` are unconfigured starter placeholders that verify nothing. `pytest docs/scripts/` + `mkdocs build` is the pipeline that actually consumes `conventions.md` and `.tfw/templates/**` (Source Manifest rows 4 and 13). Approved in ONB Recommendation 6.

## 3. Acceptance Criteria

**AC-1 — The HL declares its own contract state** ✅
- [x] Header carries `**Contract**` with two states (`📝 DRAFT — not yet approved` / `🔒 FROZEN — approved by {owner} YYYY-MM-DD`), approval date in the frozen form
- [x] **Three** states marked, matching HL §3 exactly: 🔒 FROZEN §1/§3/§4/§5/§6/§7 · 🟢 FREE §2/§7.2/§8/§9/§10/§11 · 🟢 APPEND-ONLY §12
- [x] Header points at §12 as the amendment channel
- [x] Every section heading carries its marker inline (`## 1. Vision 🔒 FROZEN`); subsection inheritance stated as a rule
- [x] Gate: section lists cross-checked against HL-TFW-53 §3's table — agree exactly, 13 sections in 3 states

**AC-2 — `§12 Amendment Log` with an enforceable column grammar** ✅
- [x] Section exists with all 10 columns: `# · Date · § · Type · Proposer · Proposed change · Evidence · Cost · Alternatives considered · Verdict`
- [x] Type values enumerated: `EXTEND` / `SUPERSEDE` / `RESTRICT` (A10's token — the pre-A10 `APPLIED — restrictive` appears nowhere)
- [x] Restrictive rule shipped: applies on filing, verdict `✅ APPLIED — no owner verdict required`, restrictive-free prohibited. Stated in `conventions.md` §3 rule 10 and restated in the template
- [x] Empty-verdict value is `PROPOSED`, with the D28 reasoning line
- [x] Explicit-N/A default: `If nothing was ever proposed, write: **No amendments.**`
- [x] Instruction text: append-only, no edit before verdict, a research-thread remark is not a verdict
- [x] Evidence: grammar diffed against 12 live rows; one gap found (`🚫 WITHDRAWN`) and closed → EV §E2

**AC-3 — RES classifies instead of instructing** ✅
- [x] Two distinct tables: `Refinements` and `Amendment Proposals`
- [x] Both carry a `§` column naming the target HL section
- [x] `Amendment Proposals` carries Type, Evidence, Cost, Alternatives — consistent with AC-2
- [x] Instruction states the researcher classifies but never applies; proposals go to HL §12 as `PROPOSED`
- [x] Gate: `grep -n "Coordinator applies these" .tfw/templates/RES.md` → **0 matches**

**AC-4 — `conventions.md` defines the HL Contract** ✅
- [x] §3 `#### HL Contract`: six frozen sections, moment of freezing (owner approval, rule 1), §12 append-only (rule 4)
- [x] Free sections named; rule 2 states research updates them directly
- [x] Split matches `templates/HL.md` and HL-TFW-53 §3 — one decision, restated twice, re-decided nowhere

**AC-5 — An amendment verdict is a distinct recorded act** ✅
- [x] Rule 8: a verdict is a distinct recorded act
- [x] Rule 8: input inside a research thread, review or chat is evidence, never approval
- [x] Rule 9: an owner-initiated change is an amendment, owner as `Proposer`, verdict on the same row

**AC-6 — The baseline is diffable** ✅
- [x] Rule 13: approved HL committed before the first research iteration
- [x] Rule 14: reserved `freeze` scope word per the D55 grammar, applying to the **first** freeze and every re-freeze
- [x] Rule 15: recovery form is slash-free — `git log --grep="{TASK-ID}/freeze"` — with the MSYS reason stated
- [x] Rule 16: no header field can name its own commit
- [x] Gate: run under **both** shells → 5 freeze commits in each; the rejected `/freeze/` form returns 0 rows in Git Bash → `baseline_recovery.txt`

**AC-7 — Delegated authority is a ceiling** ✅
- [x] Rule 17: a delegated mandate is a ceiling, never a source of new permission
- [x] Rule 18: no agent may widen its own grant
- [x] Rule 19: delegation is never authority to accept a scope or budget overrun

**AC-8 — Granularity rule and carve-out** ✅
- [x] Rule 5: the frozen unit is the declarative claim, not the section text
- [x] Rule 5: claim-level list — phase set and each phase's declared outcome, §3 to-be claims, each §5/§6 item, each §7 principle, §1
- [x] Rule 6: deliverable-list changes inside an approved phase are refinements, with the §5/§6 tripwire
- [x] Rule 7: non-substantive edits are not amendments
- [x] Word-count delta measured and reported (§4)
- [x] Gate: five **discriminating** rows (2 tripwire, 1 inverse, 2 control) classified from the shipped text → 5/5 agreement, **circularity limit stated first** → `classification_exercise.md`

**AC-9 — The Phase HL may no longer author a contract** ✅
- [x] Rule 20: derivation-only — may restate master content and add execution context
- [x] Rule 21: may not carry its own §1, §5, §6 or §7
- [x] §14 carries the matching anti-pattern
- [x] Gate: `git show 721ca15:…TFW-48/phase-a/HL__phase-a__method_kernel.md` → violation on four independent counts → EV §E9

**AC-10 — `❌ REJECT` branch (a) no longer thaws the contract** ✅
- [x] §5 redefines branch (a) as filing an amendment against the frozen sections
- [x] States that re-entry to `📝 HL_DRAFT` reopens free sections only and does not thaw §1/§3/§4/§5/§6/§7
- [x] APPROVE / REVISE / REJECT unchanged; the §5 status table untouched (Phase E's territory)

**AC-11 — Working Backwards and visualization mandatory in §3.1** ✅
- [x] Working Backwards explicitly required — a description of the plan does not satisfy §3.1
- [x] Visual rendering mandatory, not a format option; prose alone insufficient
- [x] The value is shown, not only the artifact
- [x] Complete enough to hold at once — phase labels on every change, one line per phase
- [x] States §3.1 is the owner's checkpoint **before** the spend of tokens and time
- [x] Clause block, not a rewrite — the four format options and the §3.2 contrast survive verbatim
- [x] Gate: **no budget, slot, size, count or cut-order language anywhere** (grep, §4)
- [x] Evidence: shipped rule applied to HL-TFW-53's own §3.1 → **4/4 pass** → EV §E11

**AC-12 — The anti-pattern set is complete** ✅
- [x] All seven anti-patterns present: frozen edit without a logged verdict · unclassified recommendations · amendment applied before its verdict · research on an uncommitted HL · remark treated as a verdict · delegation cited to accept an overrun · Phase HL authoring its own AC or principles
- [x] Gate: reproducible §14-block count, 28 → 35 = exactly 7 additions, 0 removals (§4)

**12 of 12 acceptance criteria met.**

## 4. Verification

**Build gate** — `project_config.yaml` `build.*` are unconfigured starter placeholders (`echo "configure your … command"`) and verify nothing; substituted per ONB Recommendation 6:

- `python -m pytest docs/scripts/ -q` → **68 passed** in 60.30s
- `python -m mkdocs build --config-file docs/mkdocs.yml` → **built in 35.55s**, exit 0. Warnings are pre-existing cross-tree links in other tasks' artifacts (TFW-54, TFW-55); the three files this phase changed produced none. `strict` is not enabled in `docs/mkdocs.yml`

**Measurements**

| Metric | Before | After | Delta | Command |
|--------|--------|-------|-------|---------|
| `conventions.md` words | 3,952 | 5,068 | **+1,116** (+28.2%) | `$c = Get-Content .tfw/conventions.md -Raw; ($c -split '\s+' \| Where-Object {$_ -ne ''}).Count` |
| `conventions.md` lines | 513 | 568 | +55 | `(Get-Content .tfw/conventions.md).Count` |
| §14 block items | 28 | 35 | **+7, −0** | `awk '/^## 14\) Anti-patterns/,/^### 14\.1/' .tfw/conventions.md \| grep -c '^- '` |

> On the word delta: TS §6 warns `conventions.md` is near its attention budget, and +28% in one phase is a real number that Phases B, C and E inherit. It is not compressed below usability here (ONB Risk 5 ruling), but it is the measurement the next three phases should watch. F2's 700–900/1200-word budget governs *workflow* documents and does not apply to `conventions.md` — no workflow file was touched.

**Targeted gate commands**

| Gate | Command | Result |
|------|---------|--------|
| AC-3 | `grep -n "Coordinator applies these" .tfw/templates/RES.md` | 0 matches ✅ |
| AC-11 | `grep -niE "cut order\|budget\|slot" .tfw/templates/HL.md` | 0 matches ✅ |
| AC-2 | `grep -c "APPLIED — restrictive" .tfw/templates/HL.md` | 0 — the pre-A10 token ships nowhere ✅ |
| AC-6 | `git log --oneline --grep="TFW-53/freeze"` (both shells) | 5 commits each ✅ |

**DoF check** — no workflow file (`plan.md`, `review.md`, `research/base.md`) was opened for writing; no Phase C, D or E deliverable was delivered early; §14 was appended to, never restructured or renumbered; `git diff --stat` confirms exactly three modified files.

## 5. Evidence

See [EV file](evidence/EV__phase-a__contract_in_artifacts.md) for evidence details.

Evidence verdict: **5/12 VERIFIED, 0 DEFERRED, 0 BLOCKED, 7 N/A**

The seven N/A are the TS's own `Evidence:` field values, quoted verbatim in the EV table. The five VERIFIED are exactly the ACs TS §6 identified as observable against a live artifact or live history: AC-2, AC-6, AC-8, AC-9, AC-11.

## 6. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/templates/HL.md` | 150, 155 | style | §7.1 is an `##` heading while §7.2 is `###`, so §7.1 escapes the §7 nesting §7.2 observes. Pre-existing; ruled out of scope in ONB §6.6. Fixing it changes heading depth in every HL and is a Phase D terminology-pass candidate |
| 2 | `docs/scripts/gen_docs.py` | 442–465 | todo | `_replace_phase` globs `tasks/{id}*/Phase{X}/{TYPE}__Phase{X}*.md`, but D50 renamed phase folders to `phase-a/`. Every phase reference (`RF TFW-53/A`) silently falls back to the task root and mis-resolves. Live bug; coordinator flagged it for `TECH_DEBT.md` triage at review (ONB §3.1 inconsistency 7) |
| 3 | `.tfw/compilable_contract.md` | §2 Reference Format | todo | `P{N}` resolves to `KNOWLEDGE.md §0`, which D37 removed. HL §7 principle references have no resolution target. Phase C owns the namespace work (`NS{n}` / `PP{n}`) |
| 4 | `.tfw/project_config.yaml` | 1–4, 110–113 | todo | `project.name: my-project` and three `echo` placeholders for `build.lint/test/verify`. A consequence of this repository's dual identity (`constraint.md` F6 — simultaneously the upstream template and a live project), but it means no TFW task in this repo has ever had a working `build` gate from config |
| 5 | `.tfw/conventions.md` | §3 HL Contract | naming | The subsection is 21 numbered rules in one block. Readable now; if Phases B/C/E each append their own §3 subsections it will need sub-headings. Flagged so the next phase notices before it is a rewrite |
| 6 | `tasks/TFW-53__…/phase-a/TS__phase-a__…md` | 6, 83 | todo | TS header still carries the broken `git log --grep='/TFW-53/freeze/'` form that AC-6 exists to replace, and AC-2's Evidence says "nine live rows" where §12 now has twelve. Both are stale-at-write, not defects in the shipped work; noted so the reviewer does not read them as the contract |

## 7. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | environment | The owner's environment runs two shells against the same repository, and they disagree: Git Bash (MSYS2) rewrites a leading `/` in a command argument into a filesystem path before the program sees it, so `git log --grep='/freeze/'` returns zero rows there and five in PowerShell. Any shell command written into TFW framework text must be verified in both, or it ships broken for half the sessions on this machine | Executor, measured 2026-08-13; owner accepted as ONB Recommendation 1 | High |
| FC2 | process | The owner treats a defect found in their own artifact as a result, not a cost: both ONB blocking questions and four of five ONB risks were answered by *changing the TS or the contract*, including one owner amendment (A12) that **removed** a property the owner themselves had asked for two days earlier. The gate is used to find errors, not to confirm plans | Coordinator ONB rulings 2026-08-10 (*"it is a defect in what I wrote"*, *"your mitigation is better than my AC"*, A11 withdrawn) | High |
| FC3 | process | An executor is an accepted source of amendment proposals in this project: A10 is logged with `Proposer = Executor (Phase A ONB Q2)` and was approved. The amendment channel is not research-only, and the ONB is a live intake for it | HL-TFW-53 §12 row A10 | High |

## 8. Strategic Insights (Execution)

| # | Insight | Category | Source |
|---|---------|----------|--------|
| S1 | **The owner removed a requirement rather than satisfying it, and named why: it was never asked for.** A9's *budget and cut-order* property was folded in by the coordinator from reference material the owner had supplied as an *example*, then shipped into the DoD as if it had been requested. The owner's A12 verdict — remove it from §3.1, from `plan.md` and from the DoD — is the amendment protocol running against the coordinator's own inflation, two days after the coordinator wrote it. **Implication:** the drift this task exists to prevent does not only enter through research findings; it enters through the coordinator's reading of owner input. A9's own §12 row records the owner as `Proposer`, which is exactly what made the inflation invisible — an owner-proposed amendment carries the owner's authority even where its content is the coordinator's | philosophy | Owner ruling 2026-08-10; ONB §3.1 Risk 1; HL §12 A9/A11/A12 |
| S2 | **The gate paid for itself on its first use, and the payment was in contradictions, not in questions.** Both blocking questions turned out to be internal contradictions inside the *frozen* contract — DoD-2's column enumeration against DoD-6's proposer requirement, and a `Type` value that its own research defined as a `Verdict`. Neither was reachable by reading the TS; both required cross-reading HL, TS and RES iter1 against each other. The coordinator's own assessment: *"That is what this gate is for, and it worked on its first use."* **Implication for Phase C:** this is the same defect class as A6's *"reference set is internally inconsistent"* third outcome — and it was found by an executor at ONB time, not a reviewer at Judge time. The contract-defect route may need an intake earlier in the pipeline than review | philosophy | Coordinator ONB §3.1 Assessment, 2026-08-10 |
| S3 | **A rule's first live instance is where you learn whether it is enforceable.** Three of this phase's shipped clauses exist only because the rule was run against real history rather than reasoned about: the slash-free recovery form (the documented command returned nothing), the `freeze`-word-applies-to-the-first-freeze clause (TFW-53's own baseline commit is non-conforming), and `🚫 WITHDRAWN` (the corpus contained a disposition the vocabulary had no name for). **Implication:** the evidence requirement is not a reporting overhead on this kind of work — it is the design mechanism. Every one of the three would have shipped broken under a reading-only gate | philosophy | Executor, AC-6 / AC-2 evidence collection 2026-08-13 |

## 9. Diagrams

**Where each rule lives, and what it governs.** Phase A ships three files; the arrows are what a later phase must not break.

```
.tfw/templates/HL.md ─────────────────────────────── the artifact that carries the contract
  header   Contract: 📝 DRAFT | 🔒 FROZEN + date        ← AC-1   (Phase C appends north-star field here)
  §1 §3 §4 §5 §6 §7   🔒 FROZEN  (inline markers)      ← AC-1
  §2 §7.2 §8 §9 §10 §11  🟢 FREE                       ← AC-1
  §3.1     4-property gate clause block                ← AC-11  (A9, narrowed by A12)
  §12      🟢 APPEND-ONLY — 10-column grammar          ← AC-2
              │
              │ transcription: coordinator adds # · Date · Proposer, Verdict opens PROPOSED
              │
.tfw/templates/RES.md ────────────────────────────── where a finding is classified
  Refinements          → free sections   → coordinator applies, no ceremony
  Amendment Proposals  → frozen sections → HL §12, PROPOSED, owner rules   ← AC-3
  (line 32 "Coordinator applies these" — deleted)                          ← AC-3 / DoF-3

.tfw/conventions.md ──────────────────────────────── the governing definition
  §3  #### HL Contract
        rules 1–4    what freezes, when, append-only          ← AC-4
        rules 5–7    granularity: declarative claim, tripwire ← AC-8
        rules 8–12   verdict as an act, RESTRICT, Type        ← AC-5 / AC-2
        rules 13–16  Contract Baseline, git recovery          ← AC-6
        rules 17–19  delegated authority is a ceiling         ← AC-7
        rules 20–21  Phase HL is derivation-only              ← AC-9
  §5  REJECT branch (a) → file an amendment                   ← AC-10
  §14 +7 anti-patterns                                        ← AC-12
```

**The classification decision, as the shipped rules execute it.**

```
finding
  │
  ├─ typo · broken link · formatting? ──────────────────────────► apply, no log        [rule 7]
  │
  ├─ targets §2 §7.2 §8 §9 §10 §11? ───────────────────────────► refinement, apply     [rule 2]
  │
  ├─ narrows — adds a DoF, tightens scope, drops a deliverable?
  │      └──────────────► apply ON FILING + §12 row
  │                       Type RESTRICT · Verdict ✅ APPLIED — no owner verdict required   [rule 10]
  │
  ├─ changes only a deliverable list inside an approved phase?
  │      └─ acceptable under §5/§6 as they stand NOW? ── yes ───► refinement, apply     [rule 6]
  │                                                    └─ no ──► amendment          [rule 6 tripwire]
  │
  └─ changes a phase's set or declared outcome · a §3 claim · §5 · §6 · §7 · §1
         └───────────────────────────────────────────────────► §12 row, Verdict PROPOSED  [rule 5]
                                                                 Type EXTEND | SUPERSEDE  [rule 11]
                                                                        │
                                                                owner verdict — a distinct act  [rule 8]
                                                                ├─ ✅ APPROVED → apply → re-freeze commit
                                                                ├─ ❌ REJECTED → row stays; original holds
                                                                └─ 🚫 WITHDRAWN → proposer retracts, row stays
```

> Phase A defines this machine. Nothing executes it yet — `plan.md` and `research/base.md` still
> carry the old instructions, and Phase B is what makes them obey. A rule defined here and enforced
> nowhere is the expected intermediate state (TS §2).

---

*RF — TFW-53 / Phase A: Contract in Artifacts | 2026-08-13*
