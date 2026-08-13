# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW-56](../../HL-TFW-56__review_mode_removal.md)
> Goal: Review stops asking which kind of review this is — the `code / docs / spec` axis is deleted and the two checks inside it that ever carried signal are promoted into the universal checklist.

> **Headline:** the HL's central empirical claim does not survive contact with the external corpora.
> **H3 is refuted.** Mode-specific rows fire at **10.2%** across 637 rows in 203 reviews — the same
> order as the universal rows' own **8.4%** baseline. The "row that cannot fail" is a property of
> *this repository's* 39 rows, not of the mechanism.
>
> ⚠️ **Read this headline together with Challenge §C1.** On a stricter measure that discounts ⚠️ cells
> carrying an explicit "acceptable / not blocking / TS did not require it" phrase, the rates become
> **7.7% mode vs 8.3% universal** — the small difference reverses sign. What is robust on *either*
> measure is that mode rows fire at roughly the universal rate and nowhere near zero.

---

## Dimensions

Six independent decision factors. No alternative is marked recommended — all stay open until Challenge.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| **D1 — Row substance**: does a mode row express a check the universal set does not? | Fully duplicate — drop it | Partially overlapping — merge wording into a universal row | Genuinely absent — must be promoted or lost | Absent *and* domain-specific — cannot be universalised without becoming vacuous |
| **D2 — Firing rate**: does the row ever produce a non-✅ in real reviews? | Never fires anywhere (ceremony) | Fires only in one corpus (context-dependent) | Fires everywhere at ≥ universal baseline | Fires rarely but with asymmetric cost when missed |
| **D3 — Priming**: does the *label* change reviewer behaviour beyond the rows it loads? | No effect — rows are the whole value | Real effect, and the label is the cheapest carrier of it | Real effect, but the TS/RF already carries it better | Effect exists but is *harmful* — the label narrows attention |
| **D4 — Consumer coupling**: what breaks on removal? | Nothing outside the known file set | Config-merge on `/tfw-update` breaks for existing projects | Downstream tooling (docs build, editions) reads it | History/traceability breaks |
| **D5 — Extension-point role**: is a mode file where a project puts its own checks? | Never used that way — three installs identical | Used, but replaceable by a `project_config.yaml` list | Used and irreplaceable — deletion removes a capability | Unused but the *only* documented slot for per-project checks |
| **D6 — Corpus generality**: does the answer hold outside markdown-only framework work? | Holds everywhere (measured in ≥2 domains) | Holds only for markdown/spec work | Holds only for software work | Untestable — no corpus in any other domain |

---

## Findings

### G1 — Drift gate (owner-approved precondition): the corpora are valid, and one surprise

Per the owner's answer to briefing Q1, the AFD measurement was gated on a review-surface diff before
any counting. Command run per file: `diff <external>/.tfw/<path> .tfw/<path>`.

| File | AFD (VERSION 0.9.0) | helpdesk (VERSION 0.8.7) |
|---|---|---|
| `workflows/review.md` | **byte-identical** | differs — Evidence-Layer rows only (D52/D53) |
| `workflows/review/code.md` | **byte-identical** | **byte-identical** |
| `workflows/review/docs.md` | **byte-identical** | **byte-identical** |
| `workflows/review/spec.md` | **byte-identical** | **byte-identical** |
| `templates/review/map.md` | **byte-identical** | **byte-identical** |
| `templates/review/verify.md` | **byte-identical** | differs — Evidence Verification section |
| `templates/review/judge.md` | **byte-identical** | differs — §-renumber + missing row 7 *Evidence completeness* |
| `templates/REVIEW.md` | **byte-identical** | differs — no Evidence rows |

**Surprise worth recording:** AFD's `VERSION` says 0.9.0, but its entire review surface is
byte-identical to this repo's 1.0.0. The version number is not a reliable indicator of framework
drift — files move independently of the version stamp. That is a small trace-integrity observation
in its own right, and it means **AFD is a full replication, not an approximation**.

Helpdesk's drift is real but **orthogonal to the mode axis**: every difference is an Evidence-Layer
addition (D52/D53) or a section renumber. The three mode files and the Mode-Specific Checklist
section are identical across all three installs. Helpdesk therefore measures the *same mechanism*
with one fewer universal row (6 vs 7) — which, if anything, biases *against* mode rows by giving
them a shorter universal set to be redundant with.

**Verdict on the gate: PASS.** No reviews excluded. All 203 mode-carrying reviews are comparable.

### G2 — The corpus, and what it actually shows (H3 — **REFUTED**)

Extraction method: every `REVIEW*.md` outside `.tfw/templates/` and `.tfw/adapters/` in the three
repositories; `Review Mode` and `Verdict` parsed from the header block; the `## 3. Judge` table
parsed row by row; each row classified by **check name** (EN + RU synonyms), not by row number,
because REVIEW.md numbers rows 1-6 while judge.md numbers 1-7 and the field numbers them anywhere
from 7 to 10. Script: `scratchpad/extract2.py`, raw data `data2.json`.

**Corpus shape**

| Corpus | REVIEW files | Carrying `Review Mode` | Mode-specific rows filled |
|---|---:|---:|---:|
| AFD (`ai-first-devices`) | 149 | **129** | 408 |
| helpdesk | 70 | **54** | 190 |
| this repo | 61 | **20** | 39 |
| **Total** | **280** | **203** | **637** |

> The HL §2 table says 61 REVIEW files, 18 with the field, 38 rows. Re-measured here: 61 files,
> **20** with the field, **39** rows. The two extra are a `docs + code` header and one review the
> HL's `judge.md`-based count missed. The HL's local numbers are essentially correct — its
> *generalisation* from them is what fails.

**Mode-specific row outcomes**

| Corpus | n | ✅ | ⚠️ | ❌ | N/A | **non-✅ rate** |
|---|---:|---:|---:|---:|---:|---:|
| AFD | 408 | 365 | 18 | **20** | 5 | **9.3%** |
| helpdesk | 190 | 157 | 27 | 0 | 6 | **14.2%** |
| this repo | 39 | 36 | 0 | 0 | 3 | **0.0%** |
| **All** | **637** | 558 | 45 | **20** | 14 | **10.2%** |

**Universal-row baseline, same reviews** — the control the HL never computed:

| Corpus | n | non-✅ rate |
|---|---:|---:|
| AFD | 737 | 9.9% |
| helpdesk | 327 | 7.3% |
| this repo | 126 | 2.4% |
| **All** | **1190** | **8.4%** |

**This is the finding.** Mode rows fire at **10.2%**; universal rows fire at **8.4%** in the same
reviews. In helpdesk mode rows fire at *nearly twice* the universal rate (14.2% vs 7.3%). The mode
axis is not a rubber stamp — it is, corpus-wide, at least as productive per row as the checklist the
HL wants to promote rows into. (Challenge §C1 stress-tests this comparison and narrows it: the two
rates are equal within measurement noise, and the ranking depends on how soft ⚠️ cells are counted.
The *refutation of "never fires"* is unaffected.)

The HL's premise — *"the axis has never produced a finding"* — is true of this repository and false
of the mechanism. This repository has 39 of the 637 rows (6%) and is the only markdown-only corpus.

**Robustness check.** 17 of the 65 non-✅ mode rows come from one task (AFD-48). Excluding AFD-48
entirely, AFD still fires at **5.7%** (7 ❌ + 14 ⚠️ in 371 rows) and helpdesk is untouched at 14.2%.
Non-✅ mode rows appear in **28 of 63 tasks** and across **at least 9 distinct reviewer identities**
(Claude Opus 4.7/4.8/5, Codex, Antigravity, unnamed). The effect is not one strict reviewer.

**Time trend** (mode-row non-✅ by month, all corpora): 04→11.7%, 05→10.6%, 06→2.5%, 07→9.2%,
08→19.6%. No decay toward zero. The rows were not becoming ceremony over time.

### G3 — Per-row firing rates break the HL's coverage table (H1 — **REFUTED as stated**)

| Mode row | n | ✅ | ⚠️ | ❌ | N/A | non-✅ | HL §3 disposition | Verdict on the HL |
|---|---:|---:|---:|---:|---:|---:|---|---|
| **Test coverage** | 141 | 99 | **26** | **7** | 9 | **23.4%** | "already covered" by universal 7 | ❌ **Wrong.** Highest-firing row of all eight |
| **Analytical quality** | 8 | 6 | 1 | 1 | 0 | 25.0% | "already covered" by universal 1/4 | ❌ **Wrong**, though n=8 |
| **Source attribution** | 9 | 7 | 1 | 1 | 0 | 22.2% | → promoted | ✅ supported |
| **Source verification** | 16 | 14 | 1 | 1 | 0 | 12.5% | → promoted | ✅ supported |
| **Breaking changes** | 141 | 126 | **11** | 1 | 3 | 8.5% | → promoted | ✅ supported — but the HL thought it fired **once**; it fired **12 times** |
| **Content quality** | 17 | 16 | 0 | 1 | 0 | 5.9% | "already covered" | ⚠️ fires, n small |
| **Code quality** | 155 | 147 | 1 | **6** | 1 | 4.5% | "already covered" by universal 4 | ❌ **Wrong.** 6 hard ❌ |
| **Security** | 150 | 143 | 4 | 2 | 1 | 4.0% | → promoted with explicit N/A | ✅ supported |

**Zero rows never fired.** All eight produced at least one non-✅ somewhere. The HL's five
"already covered" dispositions rest on rows that collectively produced **9 ❌ and 28 ⚠️**.

The two hardest failures for the HL:
- **Test coverage (23.4%)** is the single most productive row in the entire mechanism, and the HL
  classifies it as redundant with universal row 7 *Evidence completeness*. Helpdesk alone has 23 ⚠️
  on it. Note that helpdesk's judge.md **has no row 7** — so for 190 of the 637 rows, the universal
  row the HL says covers it did not exist. That is not evidence of redundancy; it is evidence the
  mode row was doing work nothing else did.
- **Code quality** produced 6 ❌ with substantive findings (*"Grace window выдан за recovery action"*,
  *"Foreign code can retain/collect/emit through the bus-owned mutable flow"*). Universal row 4 is
  *Style & standards — conventions, naming*. These are not style findings.

### G4 — Did a mode row ever *drive* a verdict? (the HL's strongest surviving argument)

| Verdict | mode row non-✅ | files |
|---|---|---:|
| APPROVE | no | 150 |
| APPROVE | **yes** | **34** |
| REVISE | no | 4 |
| REVISE | **yes** | **14** |
| REJECT | — | 0 |

**In 0 of 203 reviews was a failing mode row the *only* failing row.** Every REVISE with a mode-row
failure also had ≥1 universal-row failure (median 4). So on the narrow question *"would the verdict
have changed?"* — the answer is no, not once. The HL's instinct is right on **verdict causation**
and wrong on **finding production**.

But those are different questions, and DoF-1 is written about the second one: *"a check available
today disappears without a recorded home — coverage loss disguised as simplification."* A finding
that does not flip a verdict is still a finding: it lands in §5 Tech Debt Collected and in the RF
follow-up. 34 APPROVE reviews carry a non-✅ mode row — those are findings recorded in reviews that
passed, which is exactly where a low-severity check earns its keep.

**Duplication test.** For each of the 65 non-✅ mode rows, I measured lexical overlap between its
Evidence cell and the union of all failing universal-row Evidence cells in the same review
(≥34% token overlap = plausible restatement). Result: **3 of 65 overlap; 62 do not.** Sample of
non-overlapping findings that would have no other home:

- `❌ Security` — *"SQL injection vector in `scheduleByDate`"* (AFD-10/A1) — universal rows in that
  review flagged DoD-partial and nothing else named injection.
- `⚠️ Breaking changes` — *"образ, стартовавший раньше V24, не удаляет…"* — a deployment-ordering
  hazard named nowhere else.
- `⚠️ Breaking changes` — *"`create()/transition()` return type changed. All prod callers updated.
  **But**: `test_ticket_service.py` mocks not updated"* (helpdesk).
- `⚠️ Source verification` — *"3 несущих claim'а спот-чекнуты… byte-stable диффом · D114 моим
  форс-прогоном · прод моими curl/nslookup"* — a provenance trace with no universal home.

This is a **lexical** test, not a semantic one, and it overstates uniqueness where two rows describe
the same defect in different words. It is offered as an upper bound on lost coverage, not a
measurement of it. Even discounted heavily, it is not zero.

### G5 — Consumer audit (H4 — **partially refuted**; H5 — **confirmed**)

Grep run over `.tfw/ .claude/ .agent/ .agents/ editions/ docs/ site/ *.md` for `default_mode`,
`Review Mode`, `review/{mode}`, `review/{code`, `code / docs / spec`.

**Every consumer found is already in the HL's file list.** Nothing new:

| Consumer | Files | In HL scope? |
|---|---|---|
| Workflow + adapters | `.tfw/workflows/review.md` (×4 refs), `.claude/commands/tfw-review.md`, `.agent/workflows/tfw-review.md` | ✅ yes |
| Config routing | `.tfw/workflows/config.md:92` + 2 adapter copies (all three carry the stale *"Step 0"* pointer) | ✅ yes |
| Config values | `.tfw/project_config.yaml:60`, `.tfw/templates/project_config.yaml:64` | ✅ yes |
| Templates | `templates/review/{map,verify,judge}.md`, `templates/REVIEW.md` | ✅ yes |
| Mode files | `.tfw/workflows/review/{code,docs,spec}.md` | ✅ yes |
| Knowledge/debt | `KNOWLEDGE.md:74` (D42), `TECH_DEBT.md:22` (TD-106), `.tfw/CHANGELOG.md:95,130` | ✅ yes |

**Named blind spots cleared:**
- `docs/scripts/gen_docs.py` and `site/scripts/gen_docs.py` — **zero** mode coupling (the only
  `mode` hit is the word *"strict-mode safe"* in a docstring).
- `editions/01-light/`, `editions/02-assisted/` — **zero** hits for `default_mode`, `Review Mode`,
  or `review/`. The light editions never adopted the axis.

**H4 second half — `/tfw-update` on a removed key: the HL's `⬜ unverified` is justified, and the
answer is that no rule exists.** `.tfw/workflows/update.md` Step 3 categorises **files**, not keys:

- `tfw.review` is listed as a **framework section → update** in the `project_config.yaml` merge
  rules (update.md §"Files requiring merge"). So the block is meant to be replaced from upstream.
- The 🔴 Breaking category triggers on *"any file listed under `### Removed` or `### Changed` in
  CHANGELOG"* — **file-granularity only**. A removed *config key* is not a removed file and falls
  through the categorisation entirely.
- The merge is a human/agent judgement step (*"diff and merge carefully"*), not a script. There is
  no mechanism that would corrupt a config — but equally no mechanism that guarantees the stale key
  is removed. The realistic failure is **silent orphaning**: projects keep `default_mode: code` in
  their config forever, pointing at a workflow step that no longer exists.
- Adjacent hazard, pre-existing and not created by this task: `min_verify_ratio` lives in the same
  `tfw.review` block that update.md marks *"framework → update"*. A project that tuned 0.42 would
  have it overwritten on any update. Worth recording; **out of this task's scope**.

**H5 — confirmed, strongly.** `workflows/review/{code,docs,spec}.md` are **byte-identical across all
three installs**, spanning two other framework versions and two other product domains. In 280
reviews nobody ever edited a mode file to add a project check. The extension-point risk in HL §9 is
empirically dead: **D5 = Alt A**.

### G6 — The label as used in the field (input to H6)

**19 of 203 labelled reviews (9%) do not use the sanctioned three-value enum.**

- **6 are multi-value** — `code + docs + spec` (×3, AFD), `code + docs` (AFD), `docs + spec`
  (AFD, owner-directed), `docs + code` (this repo). The HL found one; there are six.
- **13 are a single value plus a free-text qualifier**, and the qualifiers are the interesting part —
  none of them describe a *genre*:
  - `code (full mode — conventions §6 guardrail: phase exceeds 80% of scope budgets)`
  - `code (full mode — conventions §6 guardrail: phase exceeds maxnewfiles, 22 > 18)`
  - `code (full-режим: RF заявляет ~30 файлов ≈ 86% бюджета 35 → guardrail conventions §6)`
  - `code (full verification; 89,6% LOC-budget)` · `code (full-mode guardrail)`
  - `code (abbreviated — full codebase verified by AFD-6)`
  - `code (revision-2 full verification)` · `code · Round: 3 (финальный)` · `code · Pass: #3`
  - `code (primary) + spec + docs lenses (owner-requested hybrid)` · `spec + docs (owner-directed)`
  - `code (владелец подтвердил mode code)` · `code (spike)` · `code + UX (post-Codex pass)`

Eight of the thirteen qualifiers encode **verification depth or pass number**, not genre —
"full vs abbreviated", "round 3", "89.6% LOC-budget", "guardrail triggered". Reviewers reached for
the one free-text slot in the header and used it to record *how hard they looked*, because the
template gives them nowhere else to say it. Two more record **who decided the mode** (owner
override / owner confirmation).

This is a live design signal, and it points somewhere the HL does not look: **the field is being
repurposed as a depth/rigour declaration.** That is the same variable `min_verify_ratio` controls —
the key the HL keeps.

### G7 — External evidence: what checklist and rubric research says

**Checklist design (aviation/surgical, Gawande's Read-Do vs Do-Confirm):**
- Do-Confirm lists *"should focus only on critical items that are commonly missed or have severe
  consequences if overlooked"* — low frequency is not disqualifying if consequence is high. This
  supports promoting **Security** despite a 4.0% rate, and is the strongest external support in the
  HL for a position the HL argues from cost-asymmetry alone.
- Length guidance: **5-9 items** (working-memory limit); *"the art of checklist design is as much
  about what you leave out as what you include… each additional item needs to earn its place by
  addressing a specific, consequential risk."* The HL's proposed **10 universal rows exceeds this
  band**, and unlike the current design every reviewer reads all 10 every time.
- Complacency: *"if a pilot reads an item like 'pressurization checked' one hundred times without any
  anomaly, it becomes easy to simply read the line without looking."* This cuts **both ways** and the
  HL only cites the half that helps it: the always-present promoted row is read more often than the
  mode-gated one, so promotion *increases* habituation exposure for a low-firing check.

**LLM-as-judge rubric research** (the reviewers here are all LLM agents, so this is directly on point):
- *"Rubrics… contain redundant or highly correlated criteria — degrading judge accuracy."* Supports
  deleting genuinely duplicate rows (Content quality vs Style & standards), and warns against
  promoting rows that overlap.
- **Composite dilution effect:** *"equal-weighted composites with many dimensions underperform their
  best individual dimensions."* A flat 10-row equal-weight checklist is the shape this warns about.
- LLM judges are *"sensitive to the ordering of rubric dimensions"* — relevant to the HL's plan to
  append three promoted rows at positions 8-10, the tail of the list.
- Role/persona priming has a **measured, non-zero effect**: *"role prompting systematically increases
  expertise depth while reducing clarity."* This is the first evidence in the file that D28's
  prediction has external support — the label plausibly does something. It is a *tradeoff*, not a
  pure gain, which matters for Challenge.

---

## Checkpoint

| Found | Remaining |
|-------|-----------|
| **H3 refuted.** Mode rows fire at 10.2% (637 rows) vs 9.4% universal baseline; helpdesk 14.2% vs 7.3%. The "never produced a finding" claim holds only for this repo's 39 rows | Whether the *findings* mode rows produce are semantically unique or restatements — the 62/65 non-overlap figure is lexical and is an upper bound |
| **H1 refuted as stated.** All 8 rows fire. Test coverage (23.4%) and Code quality (6 ❌) are classified "already covered" by the HL and are not | Which universal row, if any, genuinely absorbs Test coverage — Extract's job |
| **H2 supported so far.** Both distinctive `code` verify actions confirmed present in `verify.md` Checkpoint and `review.md` Trust Protocol | Line-by-line confirmation of the docs/spec verify actions, which the HL never enumerated |
| **H4 split.** No unknown consumer exists (gen_docs, editions clean). But `update.md` has **no removed-key rule at all** — key removal is invisible to its file-granularity categorisation | Whether that gap needs fixing in this task or is a separate debt item |
| **H5 confirmed.** Mode files byte-identical across 3 installs / 2 versions / 2 domains. Never used as an extension point | — closed |
| **Drift gate passed.** AFD review surface byte-identical to 1.0.0 despite VERSION 0.9.0; helpdesk drift is Evidence-Layer only, orthogonal to the axis | Trace-integrity observation: VERSION does not track file drift (out of scope, → Fact Candidate) |
| **G6:** 19/203 labels deviate from the enum; 8 of 13 qualifiers encode *verification depth*, not genre | Whether the axis's real latent variable is depth (a `min_verify_ratio` sibling), not genre — Extract/Challenge |
| **G7:** external research supports low-frequency/high-consequence retention, warns that 10 flat rows exceed the 5-9 band and invites composite dilution, and gives D28's priming prediction independent support | H6 itself — Challenge |

**Sufficiency:**
- [x] External source used? — two external repositories (203 reviews) + 3 web searches (checklist design, persona priming, LLM-judge rubric design)
- [x] Briefing gap closed? — all four HL blind spots addressed except *non-code projects*, which has no reachable corpus and is carried forward as a named open thread
- [x] Dimensions identified? — 6 independent dimensions, ≥3 alternatives each

Stage complete: YES
→ User decision: autonomous run authorised at briefing; proceeding to Extract without a gate
