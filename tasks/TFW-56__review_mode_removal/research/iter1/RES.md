# RES — TFW-56: Remove the Review Mode Axis — Iteration 1

> **Date**: 2026-08-13
> **Author**: Researcher (Claude Code)
> **Status**: 🔬 RES — iteration 1 complete
> **Parent HL**: [HL-TFW-56](../../HL-TFW-56__review_mode_removal.md) — 🔒 FROZEN 2026-08-13
> **Mode**: Pipeline · focused (`loops_per_stage: 1`)
> **Stage files**: [1_briefing.md](1_briefing.md) · [2_gather.md](2_gather.md) · [3_extract.md](3_extract.md) · [4_challenge.md](4_challenge.md)

---

## Research Context

HL TFW-56 proposes deleting the `code / docs / spec` review axis on one empirical claim: across 18
REVIEW files in this repository, 38 mode-specific checklist rows produced 33 ✅, 4 N/A, 1 ⚠️ and 0 ❌
— *"the axis has never produced a finding"*. The HL then applies TFW-53's base-rate rule (a check
that cannot fail is ceremony) and promotes three survivor rows into the universal checklist.

The HL itself named the blind spot: **the claim was never tested outside this repository.** This
iteration measured it against two external TFW installs — `ai-first-devices` (AFD) and `helpdesk` —
totalling **203 mode-carrying reviews and 637 mode-specific rows**, audited every consumer of the
config key and header, built the coverage matrix, and attacked H6 (priming vs rows) head-on.

**The finding is that the HL's central empirical claim does not hold outside this repository, and
the frozen §3 coverage table that depends on it is wrong in two specific places.** The rest of the
HL — the gate, the three duplicate files, the wrong-by-default config key, the stale pointers,
`docs`/`spec` being synonyms — survives intact and is well-supported.

## Briefing

See [1_briefing.md](1_briefing.md). Owner directions at the gate: measurement gated on a
review-surface drift check (Q1b); `helpdesk` included as a second replication (Q3); H6 approach
delegated to the researcher (Q2) — resolved as *both* a pre-declared observational test and the
decision H6 forces. Autonomous execution authorised for stages 2-4.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| **D1** | The drift gate **passes**. AFD's entire review surface is byte-identical to this repo's 1.0.0 despite `VERSION 0.9.0`; helpdesk's drift is Evidence-Layer only and orthogonal to the mode axis. All 203 reviews are comparable; none excluded | Per-file `diff` across 9 review-surface files × 2 installs (2_gather G1) |
| **D2** | **H3 is refuted.** Mode rows fire at 10.2% raw / 7.7% hard across 637 rows, against a universal-row baseline of 8.4% raw / 8.3% hard in the same reviews. All eight rows fired somewhere. The "never fires" property belongs to this repository's 39-row sample, not to the mechanism | 2_gather G2/G3; stress-tested in 4_challenge C1 |
| **D3** | **The two HL claims separate: one is true, one is false.** "Mode rows never changed a verdict" is **true** (0 of 203 reviews had a mode row as the sole non-✅). "Mode rows produce no findings" is **false** (49 hard non-✅, incl. 20 ❌; 62 of 65 do not restate a failing universal row) | 2_gather G4; 3_extract E4 |
| **D4** | **H1 is refuted as stated.** The HL's disposition table misclassifies two rows: **Test coverage** (23.4% — the highest-firing row of all eight) and **Code quality** (6 hard ❌) are marked "already covered" and are not | 3_extract E1 |
| **D5** | **Four mode rows are one check in three genres.** Test coverage, Analytical quality, Source verification and Source attribution all produce findings of a single shape: *the artifact carries a green signal that does not establish the claim*. Combined firing 16.1% (28/174) — the most productive check in TFW review. The HL's promoted wording ("claims traceable to sources") captures roughly a third of it | 3_extract E2 |
| **D6** | **Corrected survivor set is four rows** — S1 *Evidence bears on the claim* · S2 *Backward compatibility* · S3 *Design soundness* · S4 *Safety* — collapsed by residue, not by name. **Content quality** is a genuine duplicate and is correctly dropped | 3_extract E2; stress-tested 4_challenge C5 |
| **D7** | **H2 has a hole.** Three `docs`/`spec` **verify actions** (spot-check claims · citations traceable to real artifacts · data claims against primary sources) have no unconditional home. They are Verify-stage actions, so promoting judge rows does not rescue them. The HL asserts H2 from `code`'s two actions only | 3_extract E1 |
| **D8** | **H5 is confirmed and closed.** `workflows/review/{code,docs,spec}.md` are byte-identical across three installs, two framework versions and two product domains. Never used as an extension point | 2_gather G5 |
| **D9** | **H4 splits.** No unknown consumer exists — `gen_docs.py` and `editions/` are clean; every hit is already in the HL's file list. But `update.md` categorises **files, never keys**, so a removed config key is invisible to its 🟢/🟡/🔴 triage. Failure mode is silent orphaning, not corruption | 2_gather G5; 3_extract E5 |
| **D10** | **H6 is unresolved and no longer decision-critical.** The observational test is **unavailable**, not null: the 77 unlabelled REVIEW files are structurally different documents (pre-TFW-38 or bespoke layouts, median 0 parseable Judge rows), not labelled reviews minus the label. Since the rows demonstrably carry signal, deletion loses coverage whether or not priming also existed | 4_challenge C4 |
| **D11** | **C1 (the HL as frozen) is eliminated; C3 is the strongest survivor** — delete the axis, promote the corrected four rows, and migrate the three orphaned verify actions into `verify.md`. C4 (project-optional) survives on the HL's own pre-registered filter and is the honest runner-up | 4_challenge C2/C3 |
| **D12** | **The promotion design needs structure, not just appended rows.** 10-11 flat equal-weight rows exceed the 5-9 checklist band and invite the composite dilution effect; always-present rows raise habituation exposure for low-firing checks. F21 explicit-N/A becomes load-bearing rather than decorative | 4_challenge C3; 2_gather G7 |
| **D13** | **Self-correction, recorded.** Gather's first headline said mode rows are *more* productive than universal rows. On the hard measure (discounting ⚠️ cells carrying "acceptable / not blocking / TS did not require"), the ranking reverses: 7.7% vs 8.3%. The defensible claim is **equal productivity, ~8% each** — which still refutes "never fires" | 4_challenge C1; Gather headline amended in place |

## Open Questions

| # | Question | Status | Answer |
|---|----------|--------|--------|
| Q1 | Are the external corpora valid replications? | ✅ closed | Yes — D1. AFD is byte-identical on the whole review surface; helpdesk differs only in Evidence-Layer rows |
| Q2 | Do mode rows produce findings outside this repo? | ✅ closed | Yes — D2. 49 hard non-✅ incl. 20 ❌ |
| Q3 | Did a mode row ever flip a verdict? | ✅ closed | No — D3. 0 of 203 as sole driver |
| Q4 | Which rows are genuinely absent from the universal set? | ✅ closed | Four by residue — D6 |
| Q5 | Does anything unknown consume the key or header? | ✅ closed | No — D9 |
| Q6 | Does `/tfw-update` handle a removed framework key? | ✅ closed | No rule exists — D9. Silent orphaning |
| Q7 | Is a mode file ever used as a project extension point? | ✅ closed | Never — D8 |
| Q8 | Did the label prime the reviewer? | 🔴 **unresolved** | No test available in this corpus — D10. Two weak probes point away from strong priming; external evidence says role labels do affect LLM output |
| Q9 | Does S3 (design soundness) become a row, or a sharpening of U2 *Philosophy aligned*? | 🟡 open | TS/HL decision. 4 of 6 ❌ are arguably principle violations. **Silence loses 6 ❌** |
| Q10 | Does the axis hold in non-software, non-markdown domains? | 🔴 **untestable** | No corpus exists in reach. Named blind spot, carried forward |

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status | RES Status | Evidence |
|---|-----------|-----------|------------|----------|
| H1 | The eight mode rows contain exactly three checks absent from the universal set; the other five are synonyms or already mandated | open | ❌ **REFUTED as stated** | Five residues, collapsing to **four** distinct checks. Test coverage (23.4%) and Code quality (6 ❌) are misclassified as "already covered". 3_extract E1/E2 |
| H2 | No verify action is lost: `code`'s two distinctive actions are already unconditional | open | 🟡 **PARTIALLY CONFIRMED** | True for all four `code` actions. **False for three `docs`/`spec` actions**, which the HL never enumerated. 3_extract E1 |
| H3 | The finding replicates in AFD: mode rows produce ~0 findings across ~149 reviews | open | ❌ **REFUTED** | 408 rows, 20 ❌ + 18 ⚠️, 9.3% raw / 8.3% hard. Helpdesk independently: 190 rows, 14.2% raw. 2_gather G2 |
| H4 | No consumer breaks; `update.md`'s CONFIG merge handles a removed key | open | 🟡 **SPLIT** | Consumer audit ✅ clean (incl. `gen_docs.py`, `editions/`). Removed-key handling ❌ — no rule exists. 2_gather G5, 3_extract E5 |
| H5 | No project uses the mode files as an extension point | open | ✅ **CONFIRMED** | Byte-identical across 3 installs / 2 versions / 2 domains. 2_gather G5 |
| H6 | The axis's value was in its rows, not in priming | open | 🔴 **UNRESOLVED — test unavailable** | The unlabelled corpus is not a control group. Reported as unavailable, not as a null. Decision-relevance collapsed by D2/D3. 4_challenge C4 |

> **The HL's own pre-registered filter, applied honestly.** HL §10 states: *"H3 false → the axis works
> in other projects; make it project-optional instead of removing it."* H3 is false. By the HL's
> written rule, the indicated response is C4, not C1. Research does not overrule that — it reports
> that the condition the HL wrote has fired, and that C3 is a stronger option than either, for the
> reasons in 4_challenge C3.

## HL Update Recommendations

### Refinements — free sections, coordinator applies

| # | § | What to update | Source |
|---|---|----------------|--------|
| R1 | §2 | Replace *"The axis has never produced a finding"* with the measured position: 637 rows across 203 reviews in 3 repositories, 10.2% raw / 7.7% hard non-✅ against an 8.4% / 8.3% universal baseline; **0 of 203 verdict flips**. Keep the local 38-row table as the local sub-sample it is | D2, D3 · 2_gather G2 |
| R2 | §2 | Correct *"A REVIEW header reads `docs + code` — multi-select invented in the field"*: **19 of 203 labels (9%)** deviate from the enum — 6 multi-value, 13 with free-text qualifiers, of which **8 encode verification depth**, not genre | 2_gather G6 |
| R3 | §2 | Add: `docs` and `spec` being synonyms is **confirmed** — their four rows collapse into a single residue that fires hardest in `code` reviews | D5 · 3_extract E2 |
| R4 | §7.2 | Add citations: Gawande Do-Confirm selection-by-consequence (supports the Safety row at 4.0%); the 5-9 checklist band; LLM-judge composite dilution and redundant-criteria degradation | 2_gather G7 |
| R5 | §8 | `/tfw-update` removed-key semantics: **⬜ unverified → 🔴 verified gap.** No rule exists; failure mode is silent orphaning of `default_mode: code` in existing projects, not corruption | D9 · 3_extract E5 |
| R6 | §9 | Update three risk rows: *"a mode row carried value the 38-fill sample cannot show"* — **materialised**, probability Medium → **Confirmed**; *"an external project depends on the mode files as an extension point"* — **closed, H5 confirmed**; *"the axis's real function was priming"* — **unresolved, test unavailable** | D2, D8, D10 |
| R7 | §9 | Add new risk: **promoted rows exceed the 5-9 checklist band and dilute the checklist** (10-11 flat equal-weight rows). Mitigation: structure + explicit-N/A grammar, not appended rows | D12 · 4_challenge C3 |
| R8 | §10 | Mark H1 ❌ refuted-as-stated · H2 🟡 partial · H3 ❌ refuted · H4 🟡 split · H5 ✅ confirmed · H6 🔴 unresolved. Record that the §10 filter condition for H3 has **fired** | All |
| R9 | §10 | Close the *"External base rate"* and *"Consumer audit"* blind spots; keep *"Priming vs rows"* open with the reason it could not be closed; keep *"Non-code projects"* open — no corpus in reach | D10, Q10 |
| R10 | §2 | Add the trace-integrity observation: AFD's `.tfw/VERSION` reads 0.9.0 while its review surface is byte-identical to 1.0.0 — **VERSION does not track file drift**. Affects any future cross-project replication | 2_gather G1 |

### Amendment Proposals — frozen sections, owner verdict required

> The frozen unit is the declarative claim (conventions.md §3.5). Each row below targets a specific
> claim, not section prose.

| # | § | Type | Proposed change | Evidence | Cost | Alternatives considered |
|---|---|------|-----------------|----------|------|------------------------|
| **A1** | §3 (coverage table) | `SUPERSEDE` | Replace the 8-row disposition table. **Promote four rows by residue**: S1 *Evidence bears on the claim* (absorbs Test coverage · Analytical quality · Source verification · Source attribution), S2 *Backward compatibility*, S3 *Design soundness*, S4 *Safety*. Drop **Content quality** as a true duplicate of U4. The current table's *"Test coverage → already covered"* and *"Code quality → already covered"* are contradicted by measurement | Test coverage 23.4% non-✅ (highest of eight); Code quality 6 hard ❌ with contract-violation findings, not style; the four-genre convergence at 16.1% (3_extract E1/E2) | Rewrites the §3 table and the §3.1 before/after diagram; universal checklist becomes 11 rows, not 10; DoD-3 and DoD-4 must be reworded to match | (a) keep the HL's three rows — loses ~65% of the S1 signal, violates the HL's own DoF-1; (b) keep the axis (C4) — the HL's own §10 filter indicates this, but it retains a gate with 0 verdict flips |
| **A2** | §3 / §4 deliverables | `EXTEND` | Add a deliverable: migrate the three orphaned `docs`/`spec` **verify actions** into `verify.md` as unconditional actions, or decline each with a stated reason | H2 is asserted from `code`'s two actions only; the three docs/spec actions have no unconditional home (3_extract E1) | One added deliverable and ~3 lines in `verify.md`. Without it, DoF-1 is violated by construction | (a) treat as covered by promoted judge rows — false: these are Verify-stage actions; (b) decline explicitly — permitted by DoD-4's own grammar, but must be *written*, not implied |
| **A3** | §5 DoD-3 | `SUPERSEDE` | Name the four corrected promoted rows instead of the three current ones, and require the explicit-N/A grammar to be **structural** (a skipped row visibly marked, not silently ✅) | D6, D12; F21; composite-dilution and 5-9-band evidence (2_gather G7) | Reworded acceptance criterion; a template-grammar requirement the executor must satisfy | Leave DoD-3 as is — it would then accept a promotion set the measurement contradicts |
| **A4** | §5 DoD-4 | `EXTEND` | Extend the "every removed row accounted for" requirement to the **verify actions** as well as the checklist rows | A2's evidence | One clause | Rely on DoF-1 alone — DoF-1 is a failure condition, not an acceptance test; DoD-4 is where the accounting is actually enforced |
| **A5** | §5 | `EXTEND` | Add a DoD item for the removed-key gap: CHANGELOG `### Removed` must name the **key** (not only files), and `update.md` Step 3 must extend 🔴 Breaking to removed config keys | `update.md` categorises files only; a removed key falls through its triage (3_extract E5) | ~4 lines in `update.md`, one CHANGELOG convention. Generalises past this task | Task-local migration note only — cheaper, leaves the framework gap for the next key removal |
| **A6** | §6 DoF-2 | `RESTRICT` | Sharpen DoF-2 from *"a row that cannot produce a finding"* to *"a promoted row whose firing rate is not evidenced, or a promoted set that pushes the universal checklist past the point where rows are read rather than used"* | The corpus now provides per-row firing rates, so "cannot produce a finding" is testable rather than rhetorical; the 5-9 band and dilution evidence make set size a real failure mode | None — narrowing. Per conventions.md §3.10 a `RESTRICT` applies on filing | Leave DoF-2 as prose — it would then be satisfiable by assertion, which is what let §3's table through |

> **A1 is the load-bearing proposal.** A2-A6 are consequential on it. If the owner declines A1 and
> keeps §3 as frozen, the task remains executable — but it ships a promotion set that this
> measurement contradicts, and DoF-1 (*"a check disappears without a recorded home"*) is triggered on
> the day it lands rather than discovered later.

## Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| FC1 | environment | Three TFW installs are reachable from this machine and usable as measurement corpora: `ai-first-devices` (149 REVIEWs, TFW 0.9.0), `helpdesk` (70 REVIEWs, TFW 0.8.7), this repo (61, 1.0.0). The owner authorised read-only use of both externals for cross-project base-rate measurement | User, briefing gate 2026-08-13 | ★★★ |
| FC2 | process | A `.tfw/VERSION` value does not track actual framework-file drift: AFD reads 0.9.0 while its entire review surface is byte-identical to 1.0.0. Cross-project replication must diff files, not compare version stamps | 2_gather G1 | ★★★ |
| FC3 | convention | Reviewers repurpose the single free-text slot in the REVIEW header to record **verification depth** (`full mode — §6 guardrail`, `abbreviated`, `Round 3`, `89,6% LOC-budget`) — 8 of 13 qualifier instances. The template gives them nowhere else to declare how hard they looked | 2_gather G6 | ★★☆ |
| FC4 | process | `.tfw/workflows/update.md` triages at file granularity only; a removed **config key** is invisible to it. Applies to every future framework key removal, not just this one | 3_extract E5 | ★★★ |
| FC5 | risk | `tfw.review.min_verify_ratio` sits inside the `tfw.review` block that `update.md` marks *framework → update*, so a project that tuned 0.42 loses the tuning on any upgrade. Pre-existing; **not** caused by this task | 2_gather G5 | ★★☆ |
| FC6 | process | Review verdicts in the corpora are never driven by a single checklist row: in 203 mode-carrying reviews, no REVISE had a mode row as its sole non-✅, and every such REVISE carried a median of 4 failing universal rows | 2_gather G4 | ★★★ |

## Strategic Insights (Research)

| # | Category | Insight | Source | Confidence |
|---|----------|---------|--------|------------|
| SS1 | process | Owner overrode `min_iterations: 2` down to 1 on the argument that four of six hypotheses were settled by *measurement rather than judgement*. The argument held — but the measurement **inverted** the HL's premise instead of confirming it, which is the outcome an iteration override is least equipped to absorb. The lesson is not "don't override"; it is that an override is safe when measurement is cheap, and the cost of being wrong lands on the *contract*, not on the research | User, `iterations.yaml` 2026-08-13 | ★★★ |
| SS2 | philosophy | Owner delegated the H6 method to the researcher (*"dont know you decide"*) — and the right answer turned out to be **reporting that the test could not be run**. A delegated methodological choice whose honest output is "unavailable" is only possible where a null and an absence are distinguished. TFW's F21 (explicit N/A over silent skip) is the same principle applied one level up, to research method rather than to checklist rows | User, briefing gate 2026-08-13 | ★★★ |
| SS3 | process | Owner volunteered the second corpus (*"also you could use helpdesk project"*) after seeing only the reconnaissance counts. That instinct is what produced the independent replication: helpdesk's 14.2% is measured on a **6-row** universal checklist (no Evidence-completeness row), so it tests the mode rows against a *weaker* universal set and still finds them productive. A single external corpus would have left AFD's numbers attributable to one project's reviewing culture | User, 2026-08-13 | ★★★ |
| SS4 | philosophy | The owner's framing in HL S1 — *«что проверять задается рамкой задачи»* — is a **design** argument and survives the measurement untouched. What the measurement refutes is the **empirical** argument stacked on top of it (*"and besides, the rows never fire"*). The strategic lesson: when a design argument is already sufficient, adding a weak empirical prop makes the whole case falsifiable at the weakest joint. The HL would be in a stronger position today with S1 alone | User, HL §11 S1 · 2026-08-13 | ★★☆ |

## Findings Map

**Root-cause chain — why the HL's premise failed**

```
HL §2 claim: "the axis has never produced a finding"
  │
  ├── measured on 38 rows / 18 reviews ── ALL from this repository
  │     │
  │     ├── this repo is markdown-only ......... no code to break, no tests to miss
  │     ├── default_mode: code is WRONG here ... HL says so itself, §2
  │     └── so 8 code-genre rows were scored ... 3 N/A + 5 ✅  ← the "0 findings"
  │
  └── generalised to "the mechanism cannot fire"
        │
        └── TESTED on 598 more rows in 2 software repos
              │
              ├── AFD      408 rows → 20 ❌ + 18 ⚠️  (9.3% raw / 8.3% hard)
              ├── helpdesk 190 rows →  0 ❌ + 27 ⚠️  (14.2% raw / 7.9% hard)
              └── universal-row baseline, same reviews: 8.4% raw / 8.3% hard
                    │
                    └── VERDICT: mode rows ≈ universal rows ≈ 8%
                         "never fires" was a property of the SAMPLE
```

**The convergence nobody proposed — four rows, one check**

```
        genre-specific name              what it actually found
  ┌───────────────────────────┬──────────────────────────────────────────┐
  │ code:  Test coverage      │ "suites green, but the acceptance         │
  │        23.4% ── 141 rows  │  contract passes with a forbidden         │
  │                           │  production collector"                    │
  ├───────────────────────────┼──────────────────────────────────────────┤
  │ spec:  Analytical quality │ "собственные completeness gates           │
  │        25.0% ──   8 rows  │  отмечены зелёными при невыполнении"      │
  ├───────────────────────────┼──────────────────────────────────────────┤
  │ spec:  Source attribution │ "один primary-source claim неверен,       │
  │        22.2% ──   9 rows  │  восемь source bindings отсутствуют"      │
  ├───────────────────────────┼──────────────────────────────────────────┤
  │ docs:  Source verification│ "migration and changeset source           │
  │        12.5% ──  16 rows  │  checks fail"                             │
  └───────────────────────────┴──────────────────────────────────────────┘
                    │
                    ▼
     ONE CHECK:  "the artifact carries a green signal,
                  and the green signal does not establish the claim"
                    │
     combined:   28 non-✅ / 174 rows = 16.1%
                 ── the highest-firing check in TFW review ──
                    │
     HL promotes: "Claims traceable to sources"  ← docs/spec fragments only
                   captures ~35% of the signal, drops the code instance (141 of 174 rows)
```

**Configuration survival**

```
                        D1      D2      D3      D4      D5
                     substance firing priming consumers ext
  C1 HL as frozen ......  ✗       ✗      ?       ✓       ✓   ELIMINATED
  C2 delete + 4 rows ...  ✓       ✓      ?       ✓       ✓   survives
  C3 C2 + verify actions  ✓       ✓      ?       ✓       ✓   SURVIVES — strongest
  C4 project-optional ...  =       =      ✓       ~       ✓   survives (HL's own §10 filter)
  C5 non-gated descriptor  —       —      ✓       ✓       ✓   rider on C2/C3 only
  C6 extend enum .......  ✗       ?      ✓       ✓       ✗   ELIMINATED (F13)
  C7 genre → rigour ....   —       —      ✓       ~       ✓   DEFERRED (right signal, wrong task)
```

**Priority matrix for the coordinator**

| | **Low cost to fix** | **High cost to fix** |
|---|---|---|
| **High impact if ignored** | A2 orphaned verify actions · A5 removed-key rule | **A1 corrected promotion set** (rewrites frozen §3) |
| **Low impact if ignored** | A6 DoF-2 sharpening · R10 VERSION observation | Q9 S3-vs-U2 placement · C7 rigour axis (sibling task) |

## Iteration Status

- **Iteration:** 1 of 1 (min, coordinator override) / 3 (max)
- **Hypotheses tested:** H1 ❌ refuted-as-stated · H2 🟡 partial · H3 ❌ refuted · H4 🟡 split · H5 ✅ confirmed · H6 🔴 unresolved
- **Hypotheses deferred:** H6 — the observational test is unavailable in this corpus (no control group exists); closing it requires an experiment, not a measurement. Its decision-relevance for the C1-vs-C3 choice has collapsed, so deferring it does **not** block the task
- **Gaps discovered:**
  1. Three `docs`/`spec` **verify actions** have no unconditional home — invisible to the HL's judge-row-only analysis
  2. `update.md` has **no removed-key rule** at any granularity
  3. Q9 — S3 *Design soundness* is unresolved between "new row" and "sharpen U2 *Philosophy aligned*"; 6 hard ❌ depend on the answer
  4. The promotion target (10-11 flat rows) exceeds the 5-9 checklist band and invites composite dilution — a design problem the HL does not address
  5. **Q10 non-software domains remain untestable** — no analytics/curriculum/business-process corpus is in reach. This was a named HL blind spot at the start and it is still open
- **Superseded decisions:** D13 supersedes Gather's first headline (mode rows *more* productive than universal rows → **equally** productive, ~8%). No prior-iteration decisions exist to supersede

### Open Threads (for next iteration)

| # | Thread | Why it matters | Suggested focus |
|---|--------|---------------|-----------------|
| 1 | **H6 priming** — unresolved, no observational test available | Only decides whether C5 (a non-gated descriptor) rides along as insurance. Cheap to adopt, cheap to skip | Not a research question any more — it is an experiment (re-review one RF with and without the label) or an owner judgement call. **Do not spend an iteration on measurement that cannot exist** |
| 2 | **Q9 — S3 placement** (own row vs sharpened U2) | 6 hard ❌ lose their home if neither is chosen. Silence is the failure mode DoF-1 names | Resolvable at TS time by reading the 6 findings against U2's current wording. ~30 minutes, no new corpus needed |
| 3 | **Q10 — non-software domains** | F13 claims domain-agnosticism; all evidence is from software + one markdown framework repo | No corpus exists. Recommend the coordinator **record it as a standing limitation** rather than schedule an iteration that cannot gather data |
| 4 | **C7 — genre→rigour axis** | 8 of 13 field qualifiers encode verification depth; the field is being repurposed. Real signal about what reviewers need | Sibling task or HL amendment **after** TFW-56 lands. Explicitly out of scope here — it touches `min_verify_ratio` (DoF-4) |

### Recommendation

- [x] **SUFFICIENT** — proceed to `/tfw-plan`, **but the coordinator cannot proceed straight to TS.**
      A1-A6 target frozen sections. Per conventions.md §3.3/§3.8 they must be transcribed into HL §12
      as `PROPOSED` and ruled by an explicit owner verdict before any TS is written against §3/§5/§6.
- [ ] MORE NEEDED
- [ ] BLOCKED

> A second iteration would add little: of the four open threads, one is an experiment rather than a
> measurement (H6), one is a 30-minute reading task at TS time (Q9), one has no reachable data (Q10),
> and one is out of scope by design (C7). The binding constraint now is an **owner ruling on A1**,
> not more evidence.
>
> ⚠️ Coordinator decides whether to continue or proceed. Researcher recommends but does NOT decide.

## Conclusion

This iteration set out to replicate a base-rate finding outside its home repository and instead
inverted it. Across 203 mode-carrying reviews and 637 mode-specific rows in three TFW installs — a
corpus 16× the one the HL reasons from — the `code/docs/spec` checklist rows fire at roughly **8%**,
statistically indistinguishable from the universal rows they were to be folded into, and every one of
the eight fired somewhere. The HL's *"never produced a finding"* turns out to be a property of a
39-row markdown-only sample scored under a `default_mode: code` the HL itself calls wrong for this
project. What survived the measurement is substantial and I want to be precise that the task is not
dead: the 🛑 gate is genuinely unjustified (0 verdict flips in 203 reviews), the three mode files are
byte-identical across three installs and duplicate `verify.md` in their first action, `docs` and
`spec` really are synonyms, the key is wrong-by-default and routed by three stale pointers, and H5 is
closed outright. The deletion is defensible on **cost and design**; it is the **empirical prop** —
and the frozen §3 coverage table resting on it — that does not hold. Research's specific contribution
beyond the numbers is E2: read by what they *found* rather than by what they are *called*, four of
the eight rows are one check in three genre costumes — *does the evidence offered actually establish
the claim* — firing at 16.1%, the most productive check TFW review has, and the HL's promoted wording
would have carried about a third of it while the rest disappeared into a deletion diff that looked
like simplification. **Self-critique:** the duplication figure (62 of 65 findings with no other home)
is lexical, not semantic, and overstates uniqueness — it is an upper bound and I have marked it as
one; the `⚠️` classification proved softer than `❌` in a way I did not anticipate and had to correct
mid-research (D13), which is recorded rather than smoothed over; H6 was the hypothesis the HL called
most likely to be refuted and I could not test it at all, because the control group I expected turned
out to be a different kind of document rather than the same document minus a label. Reporting that as
*unavailable* rather than as a *null* is the single most important thing in this file that is not a
number.

---

*RES — TFW-56: Remove the Review Mode Axis — Iteration 1 | 2026-08-13*
