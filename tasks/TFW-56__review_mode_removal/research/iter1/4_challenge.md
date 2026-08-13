# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW-56](../../HL-TFW-56__review_mode_removal.md)
> Goal: Review stops asking which kind of review this is — the `code / docs / spec` axis is deleted and the two checks inside it that ever carried signal are promoted into the universal checklist.

> **Method note (owner delegated the H6 approach at the briefing gate).** Decision: run **both**
> halves. (a) a pre-declared behavioural signature tested observationally, and (b) the decision H6
> forces regardless of the result. Reason: a null from observation is weak evidence and must not be
> reported as a pass. As it turned out, (a) failed for a structural reason worth reporting in itself.

---

## C1 — First, attack my own headline

The Gather result is the most consequential finding in this research, so it gets attacked first.

**Attack 1 — "Your ⚠️ are not findings, they are polite N/A."**

Measured. Of the 45 ⚠️ on mode rows, **16 (36%)** contain an explicit softening phrase
(*"acceptable given context"*, *"TS did not require tests"*, *"not blocking"*, *"pre-existing"*,
*"→ TD item"*). The comparable figure for universal rows is **4 of 65 (6%)**.

Recomputing with hard non-✅ only (❌, plus ⚠️ with no softening phrase):

| Corpus | Mode rows | hard non-✅ | Universal rows | hard non-✅ |
|---|---:|---:|---:|---:|
| AFD | 408 | 34 (**8.3%**) | 743 | 74 (**10.0%**) |
| helpdesk | 190 | 15 (**7.9%**) | 327 | 22 (**6.7%**) |
| this repo | 39 | 0 (0.0%) | 126 | 3 (2.4%) |
| **All** | **637** | **49 (7.7%)** | **1196** | **99 (8.3%)** |

**The attack partly lands.** On the strict measure mode rows fire at **7.7%** against a universal
**8.3%** — the small edge I reported in Gather reverses. And the 36%-vs-6% gap in softening language
is a genuine partial vindication of the HL: mode rows are more often filled in a *ceremonial register*
even when they produce something.

**What survives the attack — and it is the load-bearing part.** On both measures the mode-row rate
is within ~1 point of the universal rate, and on both measures it is **7-10%, not ~0%**. The HL's
claim is not "mode rows fire slightly less than universal rows"; it is *"the axis has never produced
a finding"* and *"0 blocks in 18 reviews"*. That claim is refuted by 49 hard non-✅ including 20 ❌.
The correct restatement is: **mode rows and universal rows are equally productive, at roughly 8%
each.** Which is precisely the rate the HL treats as disqualifying for one set and acceptable for the
other.

**Attack 2 — "Your parse is a regex; the numbers are artifacts."**
Status glyphs behind the 65 non-✅: 31 bare `⚠️`, 20 bare `❌`, and 14 qualified (`⚠️ partial`,
`⚠️ noted`, `🟡`, `⚠️→✅`). One case — `⚠️→✅` — is a *resolved* finding counted as non-✅; that
inflates by 1. Row identity was matched on check **name** with EN+RU synonyms rather than row number,
which is the only robust key given that REVIEW.md numbers rows 1-6, judge.md 1-7, and the field uses
7-10. Residual risk: reviews using wholly non-standard Judge layouts parse to 0 rows and drop out —
**77 of 280 REVIEW files carry no parseable mode row**, and they are excluded, not counted as ✅.
This biases *toward* the mode axis by dropping reviews that ignored it. Stated, not hidden.

**Attack 3 — "The local 0% is the honest result and the external corpora are the anomaly."**
This is the strongest counter-attack available to the HL, and it fails on its own numbers. The local
corpus is **39 rows**, 6% of the sample. Of its 8 `code`-genre rows, **3 are N/A and 5 are ✅** — and
the repository contains no code. Three reviews in a markdown-only repository were labelled `code`
because `default_mode: code` is the configured default and, as the HL itself documents, that default
is wrong for this project. **The local 0% measures a mislabelled genre on a 39-row sample, not a
mechanism that cannot fire.** It is the weakest evidence in the HL, and it is the evidence the entire
frozen §3 coverage table rests on.

## C2 — Consistency Check (pairwise)

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|---|---|---|---|---|
| D1 Row substance | "fully duplicate — drop" | D2 Firing rate | "fires at ≥ universal baseline" | A row that is a true duplicate of a universal row cannot out-fire it — the universal row would have caught the same defect. Measured: 62/65 findings do not restate a failing universal row |
| D2 Firing rate | "never fires anywhere" | D6 Generality | "holds everywhere" | Refuted by measurement: all 8 rows fire, in 2 of 3 corpora, across 28 of 63 tasks and ≥9 reviewer identities |
| D3 Priming | "no effect — rows are the whole value" | D2 "fires at baseline" | — | Not incompatible, but **no longer jointly decision-relevant**: if the rows carry ~8% signal, deletion loses coverage whether or not priming also existed. See C4 |
| D5 Extension | "used and irreplaceable" | measurement | 3 byte-identical installs | Eliminated outright — H5 closed |
| D6 Generality | "holds only for markdown work" | D2 helpdesk 14.2% / AFD 9.3% | — | The rows fire *more* in software corpora; a markdown-only generalisation cannot be the universal one |
| C6 (extend enum) | any | F13 domain-agnostic | — | `prompt`/`design`/`architecture` enumerate software specialities inside a domain-agnostic framework. HL §10 already bars this and the measurement gives no reason to reopen it |

**Surviving configurations:**

| Config | D1 substance | D2 firing | D3 priming | D4 consumers | D5 ext | Verdict |
|---|---|---|---|---|---|---|
| **C1** delete + HL's 3 rows | ❌ assumes 3 absent; matrix shows 5 residues collapsing to 4 | ❌ assumes ~0 | assumed Alt A | Alt A ✅ | Alt A ✅ | **ELIMINATED** — its two premises are the two the measurement refutes |
| **C2** delete + corrected 4 rows (S1-S4) | ✅ | ✅ | open | ✅ | ✅ | **SURVIVES** |
| **C3** = C2 + migrate the 3 orphan docs/spec **verify actions** into `verify.md` | ✅ | ✅ | open | ✅ | ✅ | **SURVIVES — strongest** |
| **C4** project-optional axis (`default_mode: none`) | unchanged | unchanged | preserved | Alt B | Alt A | **SURVIVES — but see C3 below** |
| **C5** non-gated descriptor | needs C2/C3 anyway | n/a | Alt B | ✅ | ✅ | **SURVIVES only as a rider on C2/C3**, never alone |
| **C6** extend enum | +2 synonym rows each | untested | — | ✅ | Alt C | **ELIMINATED** — F13 |
| **C7** replace genre with rigour | orthogonal | n/a | Alt B | Alt B — touches `min_verify_ratio` | ✅ | **DEFERRED** — real signal (G6), wrong task |

**Unexpected survivors:**

- **C4 (project-optional)** survived, and it should not be dismissed as fast as HL §10's filter
  assumes. The filter says *"H3 false → the axis works in other projects; make it project-optional
  instead of removing it."* **H3 is false.** By the HL's own pre-registered rule, C4 is now the
  indicated fallback — the HL wrote the condition and the condition fired. Its weakness is that it
  keeps the gate, the three files and the key, which is most of the cost for a mechanism whose rows
  are indistinguishable from universal rows in firing rate. **The measurement that rescues C4 from
  the HL's filter is the same measurement that argues for promoting the rows instead of gating them.**
- **C3 over C2.** The orphaned `docs`/`spec` verify actions (E1) are not fixed by any promotion of
  judge rows, because they are Verify-stage actions. C2 without C3's migration step violates DoF-1
  on a technicality the HL never noticed.

## C3 — Why deletion-with-promotion beats keeping the axis, even now

C4 (keep it, make it optional) is now defensible on the data, so it needs a real argument, not a
dismissal. Three, in descending strength:

1. **The gate buys nothing, measurably.** 0 of 203 reviews had a mode row as the sole non-✅. A 🛑
   WAIT whose downstream never changes a verdict is a stop with no decision behind it. This is the
   one HL claim that came through the measurement intact and it is enough to kill the *gate*.
2. **The rows fire in genres they were not selected for.** `docs`+`spec` mode rows collapse into one
   residue (S1) that fires hardest in `code` reviews. Gating a check to a genre when the check is
   genre-independent means two thirds of reviews never see it. That is a coverage argument *for*
   promotion, and it is the HL's best instinct, now with evidence the HL did not have.
3. **Redundant/correlated criteria degrade LLM judges** — and the reviewers here are all LLM agents.
   Merging four genre-fragments into one well-specified row (S1) is exactly the "filter redundant,
   non-redundant rubric set" that the rubric literature recommends, while `docs`/`spec` as separate
   near-synonym rows is the correlated-criteria pattern it warns against.

**Counter-argument I could not dismiss.** Checklist research puts the working-memory band at **5-9
items** and warns that *"each additional item needs to earn its place"*; rubric research reports a
**composite dilution effect** — equal-weighted many-dimension composites underperform their best
single dimension. The HL's target is **10 flat rows**; the corrected survivor set would make it
**11**. Both exceed the band, and unlike today's design every reviewer reads every row every time,
which raises habituation exposure for the low-firing ones (the pilot-and-the-pressurization-gauge
failure). **The promotion design needs a structure — grouping, weighting, or an explicit-N/A grammar
that makes a skipped row visible — not just three or four appended rows at positions 8-11.** The HL's
F21 explicit-N/A instinct is the right seed; the corrected set makes it load-bearing rather than
decorative. This belongs in the HL's §3, and it is not there.

## C4 — H6, attacked head-on

**The counter-argument in its strongest form.** D28 says naming creates behaviour; `.tfw/README.md`
lists *"Naming Creates Behaviour"* as a value; this task removes a name. External evidence now
supports the mechanism rather than merely asserting it: role/persona prompting has a **measured,
non-zero effect on LLM output** — it *"systematically increases expertise depth while reducing
clarity"*. Every reviewer in all three corpora is an LLM agent. So the prior for "the label did
something" is not zero, and TFW's own doctrine points at this HL.

**Test (a) — the pre-declared signature, and why it could not be run.**
Signature declared before looking: *if the label primes, then reviews written with no label should
show lower verify-row counts, shorter review bodies, and fewer non-✅ than labelled reviews of
comparable artifacts.* The control group exists on paper — 77 REVIEW files carry no `Review Mode`
header.

It is not a control group. Inspection of the unlabelled files shows they are **structurally
different documents**, not labelled documents with the label removed: helpdesk's 16 unlabelled
reviews are pre-TFW-38 (`## 1. Review Checklist` / `## 2. Verdict`, no Map-Verify-Judge at all);
AFD's use bespoke layouts (`## 1. Scope and provenance`, `## Blocking Findings`, `§1 Map`). Their
median parseable Judge-row count is **0** — they have no comparable checklist to compare. Comparing
them to labelled reviews would measure *"did this review follow the 4-stage template"*, not *"did the
label prime the reviewer"*.

**Reporting this as a null result would have been wrong**, and it is the specific failure the owner's
delegated choice was meant to avoid. The honest statement is: **the observational test is unavailable
in this corpus.** No A/B exists; the only clean test would be re-running reviews of the same RF with
and without the label, which is an experiment, not a measurement.

**Two weak probes, reported as weak:**
- Of the 11 unlabelled reviews that *do* have a structured Judge table, **4 (36%)** spontaneously
  carry a mode-topic row anyway (Security ×4, Code quality, Test coverage, Breaking changes) — and
  all 7 such rows are ✅. Suggests reviewers partially self-generate the topics without the label,
  but do not fire on them. n=11. Directionally against strong priming; nowhere near conclusive.
- **19 of 203 labels (9%) deviate from the sanctioned enum** — 6 multi-value, 13 with free-text
  qualifiers, 2 recording an owner override. Reviewers routinely *rewrite* the label to fit the work.
  A label being overridden by the person it is supposed to prime is evidence the causal arrow points
  the other way: the reviewer classifies the work, then edits the field to match.

**Test (b) — the decision H6 forces, which is the part that actually resolves.**
H6 was framed as *"was the value in the rows or in the priming?"* — a disjunction. The measurement
collapses the disjunction: **the rows demonstrably carry ~8% firing and 62/65 findings with no other
home.** Whether priming *also* contributed is now second-order, because deletion-as-specified loses
the row coverage regardless of the answer.

So H6's status changes from *"most likely to be refuted, decides the task"* to **"unresolved, and no
longer decision-critical for the C1-vs-C2/C3 choice."** It stays live for exactly one question:
whether C5 — a non-gated one-line descriptor — should ride along as cheap insurance.

**On C5 as insurance, the evidence is genuinely mixed and I will not fake a verdict:**
- *For:* costs one header line, no gate, no key, no file; preserves whatever priming exists; and G6
  shows reviewers **already write into this slot voluntarily**, 19 times, including qualifiers no
  template asked for. Removing the slot deletes a channel the field demonstrably uses.
- *Against:* HL §10 rightly notes a field with no behaviour still needs a template slot, an
  instruction and six adapter copies, and *"is exactly the kind of decoration that regrows into a
  gate"*. D28 cuts both ways — a name with no behaviour is itself a D28 violation.
- **Unexpected third option, from G6:** if a descriptor is kept, the evidence says it should record
  **verification depth**, not genre — that is what 8 of 13 free-text qualifiers actually encode. This
  is C7's seed at one-line cost, without touching `min_verify_ratio`.

## C5 — Stress-testing the corrected survivor set

| Row | Stress test | Result |
|---|---|---|
| **S1** Evidence bears on the claim | *Is it too abstract to be actionable — will it become the rubber stamp DoF-2 forbids?* | Base rate 16.1% (28/174) is the highest in the mechanism, so it fires. Risk is real but inverted from DoF-2: an abstract row that fires often is F24's "heuristic over instruction". **Needs concrete per-genre examples in the template**, or it degrades |
| **S2** Backward compatibility | *Does it generalise past code?* | Yes — measured instances include a doc-anchor break, a template renumbering (TFW-46/A), a deployment-ordering hazard and a wire-shape change. The HL is right, and undercounted it 12-fold (thought 1 fire, actually 12) |
| **S3** Design soundness | *Is it just U2 Philosophy aligned?* | **Contestable and unresolved.** 4 of 6 ❌ are arguably HL-principle violations. Folding into a sharpened U2 is defensible. Must be decided explicitly — silence loses 6 ❌ |
| **S4** Safety | *4.0% is below the base rate the HL used to kill things* | Survives on the checklist-design rule that Do-Confirm items are selected for **consequence**, not frequency: *"critical items… that have severe consequences if overlooked"*. This is external support for a position the HL argued from intuition |
| Content quality | *Dropped — justified?* | Yes. Its residue is U4 Style & standards plus S1. Sole ❌ in 17 rows is an accuracy finding S1 covers |

## C6 — What would have to be true for the HL to be right as frozen

Stated so the owner can judge the size of the gap, not just the direction:

1. The 49 hard non-✅ mode rows would have to be restatements of universal-row findings. **Measured
   the other way:** 62 of 65 do not lexically overlap any failing universal row. Lexical, hence an
   upper bound — but it would have to be ~100% wrong for the HL's §3 to stand.
2. `docs`/`spec`'s three unique verify actions would have to be already mandated. **They are not**
   (E1) — the HL asserts H2 from `code`'s two actions only.
3. Test coverage would have to be redundant with U7 Evidence completeness. **For 190 of 637 rows
   (helpdesk) U7 did not exist**, and its findings are evidence-*validity*, not evidence-*presence*.
4. The 39-row local sample would have to represent the mechanism. It is 6% of the corpus, genre-
   mismatched, and its `code` rows are N/A or ✅ in a repository with no code.

None of the four holds. §3's coverage table and §5 DoD-3/DoD-4 rest on them.

---

## Checkpoint

| Found | Remaining |
|-------|-----------|
| **My own headline survives attack but narrows:** mode rows 7.7% hard / 10.2% raw vs universal 8.3% / 8.4%. The two sets are equally productive. "Never fires" is refuted on either measure; "fires more than universal" is not supportable | — |
| **36% of mode ⚠️ carry an explicit "acceptable" phrase vs 6% of universal ⚠️** — partial vindication of the HL's ceremony intuition, on tone rather than on output | Whether S1-S4's wording can avoid inheriting that register |
| **C1 (the frozen HL) is eliminated**; C3 (delete + corrected 4 rows + migrate 3 verify actions) is the strongest survivor; C4 survives on the HL's *own* pre-registered filter | Coordinator/owner decision — outside the researcher's role |
| **H6 unresolved and no longer decision-critical.** The observational test is unavailable — the unlabelled corpus is structurally different, not a control. Reported as unavailable, not as a null | Only C5-as-insurance still depends on it |
| **Checklist/rubric research bites the target design:** 10-11 flat equal-weight rows exceed the 5-9 band and invite composite dilution; promotion raises habituation exposure | The promotion needs structure, not just appended rows — HL §3 work |
| **S3 (design soundness) unresolved** between "new row" and "sharpen U2" | Explicit TS/HL decision required; silence loses 6 ❌ |

**Sufficiency:**
- [x] External source used? — checklist design (Read-Do/Do-Confirm, 5-9 band, complacency), persona/role priming, LLM-judge rubric design (composite dilution, redundant criteria)
- [x] Briefing gap closed? — H6 attacked head-on, with the negative result about test availability reported rather than disguised
- [x] Pairwise incompatibility checked? Surviving configurations listed? — 6 incompatible pairs, C1/C6 eliminated, C2/C3/C4/C5 survive, C7 deferred

Stage complete: YES
→ User decision: autonomous run authorised at briefing; proceeding to Synthesis
