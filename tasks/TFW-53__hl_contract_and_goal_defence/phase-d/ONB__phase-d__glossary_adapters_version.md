# ONB — TFW-53 / Phase D: Glossary, Adapters and Version

> **Date**: 2026-08-14
> **Author**: Executor (Claude Code)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-53](../HL-TFW-53__hl_contract_and_goal_defence.md) — 🔒 FROZEN, approved 2026-08-08
> **TS**: [TS Phase D](TS__phase-d__glossary_adapters_version.md)
> **Covers**: frozen DoD 30–33

---

## 1. Understanding

Phases A, B and C built the contract, the enforcement path and the goal defender. Each shipped into
`.tfw/` and into exactly one of the three tool surfaces. Phase D makes that work **portable and
findable** and then ships it: the nine terms the task invented (plus the missing `Result
Visualization`) get glossary articles; two concepts that currently carry three names each collapse to
one canonical name; all fourteen drifted adapter copies are re-synced so every tool runs what `.tfw/`
defines; five tech-debt rows close; and `VERSION` goes 1.1.0 → 1.2.0 with one CHANGELOG entry
covering A–D and the TFW-54 pointer.

It is explicitly **not** a refactor. HL §7.1 binds this phase to *terminology consistency only* — a
synonym becomes the canonical term, a sentence does not become a better sentence. Three of my
blocking questions exist because a literal reading of an AC-2 gate collides with that prohibition.

## 2. Entry Points

Everything below was opened and measured in this session — no number is quoted from the TS unchecked.

| Area | Files | State measured today |
|------|-------|---------------------|
| Glossary | `.tfw/glossary.md` | 78 entries (35 `##` + 43 `###`), 3,128 words. 8 of the 10 target terms: **0 occurrences**. `Project North Star` 1, `Result Visualization` 1 |
| Terminology | `conventions.md`, `glossary.md`, `templates/HL.md`, `templates/review/judge.md`, `workflows/review.md`, `workflows/plan.md`, `compilable_contract.md` | see §6 for the corrected drift table |
| Adapters | `.claude/commands/tfw-*.md` ×7, `.agent/workflows/tfw-*.md` ×7 | drift check prints **14 lines**, exit 0 — reproduced verbatim |
| Codex routers | `.tfw/adapters/codex/skills/tfw-{plan,review}/SKILL.md`, `.agents/skills/tfw-{plan,review}/SKILL.md` | source and installed copies **byte-identical**; plan 153 words, review 180 |
| Entry points | `CLAUDE.md`, `AGENTS.md` | CLAUDE.md 10 rows with a Purpose column; AGENTS.md 11 rows, no Purpose column |
| Release | `.tfw/VERSION` = `1.1.0`, `project_config.yaml` `version: "1.1.0"`, `.tfw/CHANGELOG.md` | `TFW-54` appears **0 times** anywhere in `.tfw/` |
| Debts | `TECH_DEBT.md` TD-157, TD-163, TD-164, TD-165, TD-167 | all four line references confirmed at the stated locations |
| Budgets | `plan.md` **1,195** · `review.md` **1,176** · `judge.md` 1,165 | against F2's 1,200 hard limit |
| Test baseline | `python -m pytest docs/scripts/` | **68 passed** in 56s, before any change |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | **AC-2's `committed baseline` gate cannot be satisfied without a forbidden rewrite.** Measured: the phrase never occurs as a standalone term. Both hits are the substring inside **`uncommitted baseline`** — `conventions.md`:75 (*"An uncommitted baseline makes 'frozen' permanently unverifiable"*) and `plan.md`:60 (*"an uncommitted baseline cannot be diffed"*). These name the **absence** of the thing, not a synonym for it, so substitution yields nonsense and any fix is a sentence rewrite — which DoF-1 and AC-7 forbid. Which? **(a) Out of mandate (recommended)** — `uncommitted baseline` is not a third name; AC-2's gate is read with the negation excluded (`grep -rn "[^n]committed baseline"` → already 0 today), 0 edits, no sentence touched. **(b) Substitute** → *"an uncommitted contract baseline"*: +1 word in `conventions.md` (Phase A's §3) and +1 in `plan.md`, which sits at 1,195/1,200 and which AC-2's third bullet forbids growing — and the literal grep still returns 2, because the substring survives. **(c)** Leave both and report in RF §6, gate recorded as 2 rather than 0 | _{coordinator fills in}_ |
| 2 | **The only genuine bare-capital `North Star` is the HL template's header field label.** Full audit of `.tfw/`: 8 literal occurrences, of which 5 are inside `Project North Star` and 1 (`glossary.md`:236) is a line-wrap of `Project North\nStar` — not drift. The two real ones are both Phase C's: `templates/HL.md`:18 `> **North Star**: {…}` (the field itself) and `:20` `> **North Star field** —` (its explainer). Nothing outside `templates/HL.md` cites the label, so a rename is local. AC-2 says capitalised `North Star` without `Project` **is** the drift; TS §9 says D touches *"the header's recovery-command line (TD-164) and nothing else in the contract block"* — the field sits below that block, so it is arguably outside the restriction, but it is Phase C's shipped surface. Which? **(a) Rename to `Project North Star` (recommended)** — 2 lines, +2 words in `templates/HL.md`, no other file affected; the field label is exactly where a reader learns the term, which is D28's whole argument. **(b) Leave** — declare a form field label a form identifier rather than running prose, record the exemption in AC-2's before/after table; 0 edits, but DoD-31 reads as unmet on a literal grep | _{coordinator fills in}_ |
| 3 | **TD-158 is routed to Phase D by `TECH_DEBT.md` but appears in neither of the TS's two lists.** Its row reads *"Backlog — → Phase D terminology pass, alongside TD-140's §12 half"*. The TS names five debts in scope (157, 163, 164, 165, 167) and six re-routed out (120, 140, 142, 153, 154, 155); TD-158 is in neither, and DoF makes fixing a re-routed debt a failure while saying nothing about this one. Its content — `templates/HL.md` §3.1 bullet 2 lists *"a narrative timeline"* in the same bullet that ends *"Prose alone is not a rendering."* — can only be fixed by rewriting a sentence in Phase A's section, which HL §7.1 forbids this phase and which TD-140 already records as needing a §12 amendment first. Which? **(a) Re-route out (recommended)** — joins TD-140/141/142/153/154/155 in the follow-up task, TECH_DEBT row re-pointed, RF §6 states the reasoning; 0 risk. **(b) Fix here** — triggers DoF-1 and crosses the §7.1 section-ownership line | _{coordinator fills in}_ |

## 4. Recommendations (suggestions, not blocking)

1. **Glossary placement — one new `##` grouping for the nine contract terms.** TS §6 leaves this open
   (*"may need their own `##` grouping … adding one is in keeping"*). I propose one grouping,
   `## Contract and Purpose Defence`, placed immediately after `## Artifact Types`, holding all nine as
   `###` entries in DoD-30's order. One grouping rather than two keeps the file's 35 → 36 `##` growth
   minimal, and the five HL-contract terms and the four review-side terms are one mechanism read from
   two ends. Override with a different name or a split if you prefer.
2. **`Result Visualization` goes under `## Knowledge Terms`, not `## Artifact Types`** — see §6.1.
   Placement stays *beside its two siblings*, which is what AC-1 actually asks for; only the parent
   heading named in the TS is wrong.
3. **`README.md` board row: edit, do not stage.** The working tree already carries an uncommitted
   README change from the concurrent TFW-55 session (the TFW-55 row moving `🔬 RES` → `🟡 TS_DRAFT (A)`,
   plus the TFW-53 row's own `📚 KNW (A, B, C)`). `git add README.md` would sweep TFW-55's row into a
   TFW-53 commit. TS §9 already provides the fallback — I will make the row edit, leave `README.md`
   entirely unstaged, and say so in the RF for the coordinator to land.
4. **The `[Unreleased]` block must be edited, not folded verbatim.** Its Adapter Sync bullet ends
   *"First run of the check found 12 drifted copies (6 workflows × 2 folders) — recorded, not yet
   repaired."* Both halves go stale on this phase: the count is now **14** (7 × 2), and the repair is
   this phase's AC-3. I will fold both `[Unreleased]` bullets into `1.2.0 ### Changed` and correct that
   sentence to the repaired state — otherwise the release ships a statement that is false on the day
   it ships.
5. **TD-163's second half stays open, deliberately.** The debt has two parts: the `glossary.md`:213
   *"Phase 0 of `plan.md`"* pointer (AC-6 names this one) **and** `plan.md` Step 2 restating the three
   Knowledge Gate modes that `glossary.md` also states (~50 words). Removing the duplication is content
   deletion in Phase B's file, not a naming fix — but it is the single cheapest ~50 words available to
   a file sitting at 1,195/1,200. I will close only the glossary half and report the other in RF §6 as
   input to TFW-57.
6. **`CLAUDE.md`'s command table is missing two rows** — `/tfw-knowledge` and `/tfw-config`, both of
   which `AGENTS.md` carries. That is incompleteness, not falsity, and AC-4 scopes the work to two
   Purpose cells. Reporting rather than fixing, unless you rule otherwise here.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **The eight unrelated adapter copies carry no surprises — verified before copying, as AC-3 requires.**
   I read every diff. In all fourteen pairs `.tfw/` is strictly ahead: the adapter side holds older text
   of the same passages (`tfw-init` lacks the whole Codex Phase 0 block, `tfw-update` lacks the Codex
   re-sync rows, `tfw-knowledge` says `RF §7` where the source says `RF §8`, `tfw-handoff` carries the
   pre-EV-file Step 11). **No copy holds content its source lacks**, so no undocumented adapter edit
   exists and AC-3's stop condition does not fire. Diff sizes measured today: plan 108 lines, init 49,
   handoff 20, review 19, update 15, research 9, knowledge 4 — per folder.
2. **This session was itself invoked from a stale copy.** `/tfw-handoff` loaded
   `.claude/commands/tfw-handoff.md`, which still instructs an inline RF §5 evidence table and permits
   skipping Step 11 when no AC carries an `Evidence:` field. The canonical
   `.tfw/workflows/handoff.md` requires a structured `evidence/EV__*.md` file and no skip. I am
   following the canonical file. This is TD-157's exact failure mode observed live on a **second**
   workflow — worth recording as evidence for AC-3's argument rather than as a defect of this phase.
3. **The word budgets are safe, measured rather than assumed.** `plan.md` contains **no**
   `frozen baseline` occurrence, so AC-2 gives it zero substitutions. `review.md` has 2, both in the
   phrase *"at its frozen baseline"* → *"at its contract baseline"*: 3 words to 3 words, exactly
   neutral. `judge.md`:34's *"committed frozen baseline"* → *"contract baseline"* is −1 word, and
   `judge.md` is a template and off F2's budget anyway. Neither workflow can grow under AC-2 as
   written.
4. **Closing TD-165 will state a resolution behaviour the build script does not implement.** Adding
   `NS{N}` and `PP{N}` to `compilable_contract.md`'s Resolution rules line puts them beside `P{N}` and
   `F{N}` — and I checked `docs/scripts/gen_docs.py`: it resolves only `TD-{N}` and `D{N}` to links.
   `P`/`F`/`S` get table anchors injected but no link resolution; `NS`/`PP` get neither. So the line is
   *already* aspirational for two of its four existing entries, and the fix keeps NS/PP at the same
   grain as their neighbours rather than inventing a new claim. Extending `gen_docs.py` is out of TS
   scope — AC-6's gate is *"pytest still passes"*, which presumes no code change. Recording this in
   RF §6 so the resolver gap is visible as one item covering P, F, NS and PP rather than four.
5. **`git diff --stat` on the six framework files (AC-7) will be dominated by one file.**
   `glossary.md` gains ten articles; the other five see only substitutions and four debt lines. The
   per-file justification AC-7 asks for will therefore read as five one-liners and one paragraph — I
   plan to report added-lines per file so the asymmetry is visible rather than averaged away.

## 6. Inconsistencies with Code (spec vs reality)

### 6.1 AC-1 and §6 name the wrong parent heading for `Result Visualization`

TS AC-1: *"placed beside the existing `Value Flow` and `Findings Map` entries under `## Artifact
Types`, **where both siblings already live**"*. TS §6 repeats it: *"`Value Flow` (line 50) and
`Findings Map` (line 53) are `###` entries under `## Artifact Types`."*

The line numbers are right; the parent heading is not. Measured heading map:

```
line  11  ## Artifact Types
line  15    ### HL (High Level)          ┐
line  18    ### RES (Research Report)    │  nine artifact-type entries,
      …                                  │  HL … RELEASE.md
line  39    ### RELEASE.md               ┘
line  42  ## Knowledge Terms          ← the siblings actually live here
line  44    ### Fact Candidate
line  47    ### Strategic Insight
line  50    ### Value Flow            ← named by the TS
line  53    ### Findings Map          ← named by the TS
line  56    ### Per-template Naming
line  59  ## Evidence Terms
```

Resolution taken (unless overruled): follow the **intent** — beside the two named siblings — and place
`### Result Visualization` between `### Value Flow` and `### Findings Map` under `## Knowledge Terms`.
That satisfies every operative word of AC-1 and contradicts only the parenthetical.

### 6.2 The measured drift table differs from AC-2's in three places

AC-2's table, against what `grep -o` returns today across `.tfw/**` excluding `CHANGELOG.md`:

| Form | TS says | Measured | Note |
|---|---|---|---|
| `frozen baseline` | 8 | **8** ✅ | 5 files: `conventions.md`, `glossary.md`, `templates/HL.md`, `judge.md` ×3, `review.md` ×2 |
| `committed baseline` | 2 | **0 as a term** | both hits are the substring inside `uncommitted baseline` — see blocking Q1 |
| `contract baseline` | 1 | **2** | `conventions.md`:73 (the `**Contract Baseline**` heading) and :94 (*"frozen contract baseline"*) |
| "in six files" | 6 | **5** | five distinct files carry `frozen baseline` |
| `Project North Star` | 5 | **5** ✅ | one occurrence in each of 5 files |
| `North Star` bare | 8 | **2 genuine** | 5 of the 8 are inside `Project North Star`; 1 is a line-wrap — see blocking Q2 |
| `north star` lower | 12 | **13** | permitted by AC-2's own second bullet after first full mention |

None of these changes what the phase must do. They change what the AC-2 **before/after evidence table**
must contain, and I will report the measured figures rather than the TS's.

### 6.3 A fourth baseline form exists that AC-2's table does not list

`templates/review/judge.md`:34 — *"the **master HL at its committed frozen baseline**"*. It combines
both retired forms in one phrase. Under AC-2's canonical rule it becomes *"at its contract baseline"*
(−1 word). Flagging it because the AC-2 gate as written (`grep` each retired form) catches it only via
`frozen baseline`, and a reviewer reading the before/after table would otherwise not see that the
`committed` half was also removed.

### 6.4 The glossary house length is 35 words, not 40

AC-1: *"The glossary's measured median is **40 words** across 78 entries."* The entry count is exact —
78. The median I measure is **35**. Full distribution across the 78 entries:

```
min  0   ──  p25  17   ──  median  35   ──  p75  50   ──  max  296
                                                          (### PV Index — a table)
```

Practical effect: none, in the same direction. I will hold each of the ten articles at or under the
**p75 = 50 words**, which is stricter than the TS's stated 40-word median as a ceiling would be lenient,
and report the per-article `wc -w` for AC-1's gate.

### 6.5 `Deferral confession` exists — a case-sensitivity trap worth recording

A case-sensitive search for `deferral confession` across `.tfw/` returns **zero**, which would suggest
DoD-30 requires a glossary article for a term Phase C never shipped. It is there:
`templates/review/judge.md`:50, capitalised as `**Deferral confession**` — the second of the Purpose
Check's three tests. The `→` pointer for its article resolves. Recording it because the same
case-sensitive check appears in AC-1's gate (`grep -c` each term) and would produce a false failure on
this one term.

## 7. Knowledge Citations

> Executor read of HL §7.2. Where an item governed an earlier phase's mechanism rather than this
> phase's naming and sync work, it is marked N/A with the reason.

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | `.tfw/README.md` § Structural Enforcement | ✅ | Applied | AC-3's acceptance test is a recorded command with its exit status, not a claim the sweep was done |
| 2 | `.tfw/README.md` § Naming Creates Behavior | ✅ | Applied | The whole of AC-1 and AC-2. Drives blocking Q2's recommendation: a field label is where the reader learns the term |
| 3 | `.tfw/README.md` § Candor Over Flattery | ✅ | Applied | §6 reports six places where measurement contradicts the TS rather than quoting the TS back |
| 4 | `KNOWLEDGE.md` D19 | ✅ | N/A | Research channel narrowing — Phase A/B mechanism, untouched here |
| 5 | `KNOWLEDGE.md` D20 | ✅ | N/A | Implicit approval — Phase A |
| 6 | `KNOWLEDGE.md` D23 | ✅ | Applied | Workflow compression is why AC-2 forbids growth; measured both files before proposing any substitution (§5.3) |
| 7 | `KNOWLEDGE.md` D24 | ✅ | Applied | Pattern A. TD-164 is D24 broken at its most visible point — the template every HL is born from |
| 8 | `KNOWLEDGE.md` D31 | ✅ | N/A | Filesystem state — no state mechanism in this phase |
| 9 | `KNOWLEDGE.md` D49 | ✅ | Applied | Gates over guidelines — every AC here has a runnable gate; I ran each one to establish the before-state |
| 10 | `KNOWLEDGE.md` D54 | ✅ | Applied | AC-3's entire justification. Confirmed the parity promise is behavioural: Codex routers stay routers, only the two full-copy folders take `cp` |
| 11 | `knowledge/philosophy.md` F4 | ✅ | Applied | Named in §5.4 — closing TD-165 states behaviour the resolver does not implement, which is F4's own shape one layer up |
| 12 | `knowledge/philosophy.md` F13 | ✅ | Applied | The ten articles carry no domain-specific language; `not fit for purpose` is checked as gate-review and contract-law usage, not software usage |
| 13 | `knowledge/philosophy.md` F21 | ✅ | Applied | Explicit N/A — every article gets a `→` pointer; none is left implicit |
| 14 | `knowledge/philosophy.md` F22 | ✅ | Applied | AC-4's *"no new section"* and AC-7's *"no template gains a field"*. Recommendation 6 defers to it: CLAUDE.md's two missing rows get reported, not added |
| 15 | `knowledge/philosophy.md` F25 | ✅ | Applied | All three blocking questions carry options with cost, not decisions taken on your behalf |
| 16 | `knowledge/process.md` F4 | ✅ | Applied | No prose block added to any workflow in this phase |
| 17 | `knowledge/process.md` F6 | ✅ | Applied | Scope explosion. Recommendations 5 and 6 and blocking Q3 all resolve toward *report, do not fix* |
| 18 | `knowledge/process.md` F14 | ✅ | Applied | Fast-run. Ran the drift check, the pytest suite and every grep gate before writing this file rather than after |
| 19 | `knowledge/process.md` F20 | ✅ | Applied | HL is authoritative on WHAT — where AC-1's parenthetical contradicts the file (§6.1), the deliverable's intent wins and the contradiction is reported |
| 20 | `knowledge/constraint.md` F2 | ✅ | Applied | 1,195 / 1,176 verified today; §5.3 shows the substitutions are word-neutral or negative |
| 21 | `.tfw/conventions.md` §7 | ✅ | N/A | CL/AG modes — no mode work in this phase (DoF-4 bars AT entirely) |
| 22 | `.tfw/conventions.md` §15 | ✅ | Applied | Role Lock. This file and the RF are the only artifacts I write; all three blocking questions are scope questions I may not answer myself |
| 23 | `KNOWLEDGE.md` D55 | ✅ | Applied | Commit attribution for the ONB and subsequent commits: `[claude-code/TFW-53/phase-d/executor]` |
| 24 | `knowledge/process.md` F11 | ✅ | N/A | Organic emergence → formalisation — Phase A's pattern |
| 25 | `KNOWLEDGE.md` D43 | ✅ | Applied | Citation-as-anti-hallucination — this table, and the `→` pointer AC-1 requires on every article |
| 26 | `KNOWLEDGE.md` D46 | ✅ | N/A | Reviewer Identity — Phase C shipped it; D changes no review content |

**New items found relevant, not in HL §7.2:**

| # | Source | Item | Why it matters here |
|---|--------|------|--------------------|
| N1 | `KNOWLEDGE.md` §1 **D53** | Optional never happens — 0 of 38 tasks created `evidence/` while the folder was optional | The owner's 2026-08-13 decision to sync all fourteen copies rests on exactly this: a binary check that keeps printing eight failures stops being read. TS AC-3 cites D53 without naming it |
| N2 | `KNOWLEDGE.md` §1 **D62** | Framework defaults follow observed practice, in **both** carriers | The lockstep argument behind AC-5's `VERSION` / `tfw.version` requirement, and the reason the `[Unreleased]` scope-budget bullet must survive the fold into 1.2.0 rather than be dropped |
| N3 | `KNOWLEDGE.md` §1 **D61** / §3 Legacy | Review mode axis deleted 2026-08-13; existing REVIEW files keep their `Review Mode` headers — history is not rewritten | Precedent for the consistency sweep's boundary: shipped artifacts are not retro-corrected. The sweep touches `.tfw/` framework files only, never `tasks/**` |
| N4 | `conventions.md` §14 | *"A reviewer approves work that satisfies the TS but not the approved contract"* | Reached through this phase's own mechanism. It is why §6 reports the TS's measurement errors instead of reproducing them into the RF — the RF is what the reviewer measures against the contract |

> **Cross-references**: Reference Format per `compilable_contract.md` §2.

---

*ONB — TFW-53 / Phase D: Glossary, Adapters and Version | 2026-08-14*
