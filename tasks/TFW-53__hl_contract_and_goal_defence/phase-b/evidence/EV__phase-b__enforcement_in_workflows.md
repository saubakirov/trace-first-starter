# EV — TFW-53 / Phase B: Enforcement in Workflows

> **Date**: 2026-08-13
> **Author**: Executor (Claude Code)
> **Task**: TFW-53
> **TS**: [TS Phase B](../TS__phase-b__enforcement_in_workflows.md)
> **Artifact under test**: commit `fbdf443`

---

## Environment

| Field | Value |
|-------|-------|
| OS | Windows 11 Pro 10.0.26200 |
| Language / Runtime | Python 3.13.5 |
| Tooling | git 2.42.0, pytest (68 tests in `docs/scripts/`), mkdocs |
| CI / Pipeline | local. `project_config.yaml` `build.lint/test/verify` are unconfigured placeholders (TD-134) — substituted per ONB Recommendation 4 |
| Word-count command | `wc -w <file>` — one command for every count in this file, per AC-6's gate and ONB Recommendation 5 |

## Evidence

| # | AC | What was verified | Result | Artifact |
|---|----|-------------------|--------|----------|
| E1 | AC-1 | Step 4's `On approval — freeze the contract` block carries the three required items and no copied rule text | N/A | TS Evidence field: `N/A — workflow text.` Gate result in RF §4 |
| E2 | AC-2 | `grep -n "[Uu]pdate HL" .tfw/workflows/plan.md` → 0 matches. Repository-wide scan of `.tfw/**/*.md` (excl. `CHANGELOG.md`) → 0 matches | VERIFIED | RF §4, inline output |
| E3 | AC-2 | 22 recommendation rows from `research/iter2/RES.md` routed using only the shipped Step 6c text. 19 route; 1 routes **against** its label and catches a live unlogged frozen-section edit; 3 cannot route because they target the TS, not the HL | VERIFIED | [`routing_replay.md`](routing_replay.md) |
| E4 | AC-3 | The approved path replayed against this task's own history: 5 re-freeze rounds, 12 approved amendments, all reproduced by the shipped 6d block — including A13, which was filed from this phase's own ONB and ruled while this file was being written. Three divergences recorded | VERIFIED | Exhibit A below |
| E5 | AC-3 | The **rejected** path could not be replayed | DEFERRED | Blocker: zero rejected amendments exist. 13 §12 rows = 12 `✅ APPROVED` + 1 `🚫 WITHDRAWN`. The branch is unexercised by any history available to this phase (S33 flagged it at 0/5; it is now 0/13) |
| E6 | AC-4 | `research/base.md` Step 6 class names and target-section requirement checked character-by-character against `templates/RES.md` | N/A | TS Evidence field: `N/A — workflow text; correctness is agreement with a shipped template, verifiable by reading.` Gate result in RF §4 |
| E7 | AC-5 | `grep -niE "windows\|macos\|linux\|bash\|msys\|powershell\|zsh"` over both workflows → 0 matches, before and after | N/A | TS Evidence field: `N/A — a grep is the whole check.` Output in RF §4 |
| E8 | AC-6 | `plan.md` 1,206 → **1,195** words (`wc -w`). Every removal paired with the source it restates | VERIFIED | Exhibit B below |

## Verdict

Evidence verdict: **4/8 VERIFIED, 1 DEFERRED, 3 N/A, 0 BLOCKED.**

The three N/A rows carry the TS's own `Evidence: N/A` justification verbatim; their gates are reading or
grep checks and are recorded in RF §4 Verification, where synthetic tool output belongs (`conventions.md`
§3 Evidence Sections). The one DEFERRED row names a corpus gap, not a missing environment: the rejected
verdict path is specified and readable, but nothing in this task's history exercises it.

---

## Exhibit A — AC-3 against this task's own history

Seven commits carry a `freeze`-class subject or served as a baseline. Recovered with
`git log --format="%h %s"` filtered on `^\S+ \[[^]]*/TFW-53/freeze/` (6 hits) plus the initial approval
commit, which that filter does **not** return:

| Commit | Date | Subject | Amendments settled | Shipped 6d describes it? |
|--------|------|---------|--------------------|--------------------------|
| `8136306` | 2026-08-08 | `[…/TFW-53/task/coordinator] freeze approved hl and prepare research` | — (initial approval baseline) | Step 4, yes. **Not returned by the recovery form** — divergence 1 |
| `d9a4c57` | 2026-08-08 | `re-freeze after amendments A1-A5` | A1-A5 approved | ✅ |
| `99d4e20` | 2026-08-10 | `re-freeze after amendments A6-A8` | A6-A8 approved | ✅ |
| `dcb9bf1` | 2026-08-13 | `re-freeze after amendment A9` | A9 approved | ✅ |
| `70f3553` | 2026-08-13 | `re-freeze after A10 and A12; withdraw A11` | A10, A12 approved; A11 withdrawn | Partly — divergence 2 |
| `ffe6c6a` | 2026-08-13 | `clear the header, show value per phase` | none — a refinement | No — divergence 3 |
| `e8ee76e` | 2026-08-13 | `re-freeze after amendment A13` | A13 approved | ✅ |

**Five re-freeze rounds** (the TS originally said three and was corrected to four after ONB Risk 2; A13
made it five *during this phase*), plus one non-amendment freeze. **Thirteen §12 rows**: twelve approved,
A11 withdrawn, none rejected.

> **The corpus grew while the evidence was being written, through the channel this phase ships.** A13 is
> `**Executor (Phase B ONB, inconsistency 3)**` — the ONB finding that the frozen HL still described the
> baseline as *"recoverable via `git log --grep`"* after AC-15 replaced that form. It was not fixed by the
> executor, who has no channel to a frozen section: it was filed as a proposal with evidence, cost and two
> considered alternatives, ruled `✅ APPROVED — owner, 2026-08-13`, applied to all three occurrences, and
> re-frozen at a new baseline. The only `git log` left in the HL is inside A13's own row, quoting the form
> it retired — append-only preserved.
>
> This is the full approved path executing end-to-end on a live finding, and it is the **second** instance
> of the ONB entry point (A10 came from the Phase A ONB). Both sit outside the research loop, which is the
> measurement 6d was placed on its own for.

### Divergence 1 — the first baseline is not recoverable by the shipped form

`8136306` uses scope word `task`, not `freeze`. `conventions.md` §3 rule 14 says the reserved word applies
to *"the **first** freeze and to every re-freeze after an approved amendment"*. The commit predates the rule
that governs it, so this is history rather than a defect — but the consequence is live: **TFW-53's own
original approved baseline is invisible to the documented recovery form.** Anyone auditing what the owner
first approved must know the commit hash out of band, which is precisely the property rule 13 exists to
prevent. Not fixable by this phase — the subject of a merged commit cannot be rewritten, and Phase B's file
set does not include `conventions.md`.

### Divergence 2 — `🚫 WITHDRAWN` has no path in the shipped block

6d covers approved, rejected and `RESTRICT`. A11 was withdrawn by its proposer before any ruling, a
disposition Phase A added to the template's verdict vocabulary (RF Phase A Decision 1) precisely because
the four-value set could not name it. The shipped block therefore cannot describe one of the thirteen rows,
and its clause *"only an owner verdict moves one"* is in tension with a withdrawal, which moves a proposal
with no owner verdict at all.

Not added, deliberately. AC-3 enumerates four bullets and withdrawal is not among them; AC-6's remaining
headroom is **5 words** against F2's 1,200 and the bullet costs ~14. Adding it would have broken the
number, and manufacturing 14 more words of "duplication" to pay for it would have been the trim AC-6
bullet 3 forbids. Recorded for the coordinator: it is a one-line addition once an artifact budget exists
(TFW-57), or a Phase D item.

### Divergence 3 — a refinement to a frozen section also produced a freeze commit

`ffe6c6a` re-froze after §3.1 was re-rendered and the header cleaned — changes the HL §12 notes classify as
refinements, not amendments. 6d ties the re-freeze commit to an *approved amendment*, so the shipped text
does not authorise this commit, yet the practice looks correct: the baseline moved, and an unmoved baseline
reference would then point at a superseded file. **Undocumented practice worth naming** — the trigger for a
re-freeze is arguably "the frozen text changed", not "an amendment was approved". Flagged, not resolved:
changing the trigger is a `conventions.md` rule, which this phase may not touch.

### Practice note — freeze commits are not atomic

`d9a4c57` and `99d4e20` bundle the re-freeze with four research stage files each; `70f3553` bundles it with
a TS and an ONB. Diffability survives (`git show <sha>:<path>` reaches the HL at that baseline), so no rule
is broken. Recording it because a reader expecting a single-file baseline commit will not find one.

---

## Exhibit B — AC-6 word count and removal ledger

**Measured with one command throughout: `wc -w`.**

| File | Before | After | Δ |
|------|-------:|------:|--:|
| `.tfw/workflows/plan.md` | 1,206 | **1,195** | −11 |
| `.tfw/workflows/research/base.md` | 869 | 943 | +74 |

`plan.md` is **under F2's 1,200 hard-degradation threshold** for the first time since it crossed it.
It is **not** inside F2's 700-900 working range — see the honest-failure note below.

`wc -w` reports 1,206 where the Phase A REVIEW and TD-140/141 report 1,205; the delta is the YAML
frontmatter delimiters. Both endpoints above use the same command, so the comparison holds regardless of
which convention a later reader prefers (ONB Recommendation 5).

### Mechanisms added — 245 words

| AC | Block | Words |
|----|-------|------:|
| AC-1 | Step 4 `On approval — freeze the contract` | 59 |
| AC-2 | Step 6c items 3-4 (classify, escalate) | 84 |
| AC-2 | replacement for the deleted line 117 | 29 |
| AC-3 | new 6d Amendment verdicts block | 73 |

### The two target instructions deleted — 29 words

| Text | Words |
|------|------:|
| `3. Update HL with research findings (present diff to user)` | 10 |
| `After all iterations complete: update HL → present diff to user → user confirms → proceed to Step 7.` | 19 |

### Duplication removed — 225 words, each paired with the source it restated

| Site | Words | Removed text (abbreviated) | What it restated |
|------|------:|----------------------------|------------------|
| Mindset ¶2 | −29 | *"When recommending RESEARCH: your default is to recommend it… Present concretely: 'RESEARCH could reveal X, Y, Z.'"* | Step 6a, same file: *"Default recommendation: **run RESEARCH**"* + *"Frame as risk reduction"* + *"Skipping requires concrete justification"* |
| Step 1 | −9 | *"Verify: AGENTS.md loaded, KNOWLEDGE.md read, task board checked, conventions.md and glossary.md loaded"* | `conventions.md` §10, the numbered list the same sentence points at |
| Step 3 item 2 | −8 | *"what needs to change. Do NOT rush to solutions."* | Mindset, same file: *"Understand the problem deeply **before proposing solutions**"* |
| Step 3 item 4 | −17 | *"Full scan: README Values, knowledge/philosophy.md, KNOWLEDGE.md §1, conventions.md §3/§11/§14. Skim: knowledge/convention.md, knowledge/process.md, other topic files."* | `glossary.md` PV Index, the table the same line points at. The full/skim boundary is **preserved** as *"priorities 1-4 in full, 5-7 skimmed"* — the mechanism stays, the source list goes. This copy had also drifted: Phase C relabels priority 1 and adds priority 0, and a lossy duplicate would have gone stale silently (S32) |
| Step 4 items 3-4 | −11 | *"create ASCII visualization of To-Be (mandatory). Add mermaid if flow is complex"* · *"apply filter «If false, would approach change?» Remove if no. Add blind spots, risks of not researching, proposed RESEARCH focus"* | `templates/HL.md` §3.1 (six format options; ASCII-only was already **stale** against what Phase A shipped) and §10, which carries the filter verbatim and names all four subsections |
| Step 4 items 5-6 | −13 | *"ID must be a link: `[PROJ-N](tasks/PROJ-N__title/)`"* · *"Each insight: Category (§10.1), Source. Human-Only Test: would this be unknown without the user saying it?"* | `conventions.md` §5 Task Board format, verbatim · `templates/HL.md` §11, which carries the Human-Only Test verbatim and *"Categories: conventions.md §10.1"* |
| Step 6b | −38 | the six-bullet field list: `task_id`, `title`, `iterations` array shape, optional `agent`/`sources` | `conventions.md` §4 Research subfolder, which prints the whole YAML block including both optional fields. The enforcement-critical defaults (`min_iterations: 2`, `max_iterations: 5`) stay **inline** per D24 |
| Step 7 item 2 | −8 | *"read `project_config.yaml` → `tfw.scope_budgets`. Read `conventions.md` §6 for rules."* | `conventions.md` §6, which holds the parameter table; the instruction (count, then split or document) is kept |
| Step 7 item 3 | −26 | *"for each AC item, consider whether real-environment evidence is needed… (full spec, minimal, N/A, DEFERRED, or leave empty). **See TS template for grammar.** Proportionality: trivial tasks may have all Evidence fields N/A or empty."* | `templates/TS.md` §5 — named in the removed text itself, one clause after the grammar it enumerates |
| Step 7 4b | −3 | the seven-line phase folder tree | `conventions.md` §4 Multi-phase folder structure, a fuller version of the same tree |
| Step 7 5b/6b | −4 | *"After RF, run `/tfw-review`. Repeat for next phase."* | the line two above it: *"Each phase: HL → TS → `/tfw-handoff` → ONB → RF → `/tfw-review` → REVIEW"*. Also removes a numbering collision — Step 6 and Step 7 both had a `6b` |
| Role Lock ¶ | −20 | *"⚠️ The coordinator MUST NOT proceed to ONB/execution/RF. Even for small tasks, the role boundary is absolute."* | the file's own header: *"You do NOT write ONB, RF, RES, REVIEW, or code. Violation = immediate stop + report."* — and `conventions.md` §15, which the removed text also linked |
| Footer | −39 | the six-question anti-pattern list | `conventions.md` §14 — the removed text enumerated a subset and then linked to the full list on the next line |

**Reconciliation:** −225 (duplication) −29 (target instructions) +245 (mechanisms) = **−9**, against a
measured −11. The 2-word gap is fragment-boundary accounting: `wc -w` counts markdown glyphs (`>`, `-`,
`**`) as words differently when a fragment is measured alone than in situ. The measured endpoints
(1,206 → 1,195) are authoritative; the ledger is the audit trail for where the words went.

### AC-6's working range — reported, not reached

F2's working range is 700-900. Reaching it from 1,195 needs another ~300 words, and no further measured
duplication exists: the remaining large blocks — Step 2's Knowledge Gate (66), Step 5's hypothesis loop
(71), Step 6a (61), Step 7's Pre-TS Gate (57) — are each the sole statement of their mechanism, and
`plan.md` is the enforcement site the glossary and `knowledge.md` point *at*, not a copy of them. Cutting
them would be the mechanism-trimming AC-6 bullet 3 and DoF-2 forbid.

Per AC-6 bullet 1 the hard threshold is met and the working target is not. Reported here rather than
resolved: the working range for a workflow that owns five gates may itself be the wrong number, which is
TD-141's territory and now TFW-57's.

## Attachments

| File | Description |
|------|-------------|
| [`routing_replay.md`](routing_replay.md) | AC-2's replay of all 22 `research/iter2/RES.md` recommendation rows through the shipped Step 6c |

---

*EV — TFW-53 / Phase B: Enforcement in Workflows | 2026-08-13*
