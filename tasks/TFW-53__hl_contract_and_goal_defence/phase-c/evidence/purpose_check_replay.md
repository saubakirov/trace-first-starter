# Purpose Check Replay — TFW-53 / Phase C (AC-11, frozen DoD-29)

> **Date**: 2026-08-13
> **Author**: Executor (Claude Code)
> **Check under test**: the Purpose Check exactly as shipped in `.tfw/templates/review/judge.md` row 2(a)
> and its block below the table — reference set, fused citation-and-harm field, excess-and-adjacency,
> deferral confession, materiality bar, override clause, three outcomes.
> **Corpus**: 6 rejected-corpus phase REVIEWs (TFW-48 A/B/C, TFW-49 A/B/C, recovered with
> `git show 721ca15:<path>`) + 3 sound reviews (TFW-50, TFW-42/A, TFW-47/B)
> **AC-11 pass condition**: ≥1 non-approve on the rejected corpus, **0** on the sound corpus

---

## 0. What this replay can and cannot establish

**Discrimination, not a rate.** Nine reviews cannot produce a firing rate, and this file does not present
one. What it establishes is that the check separates two populations selected in advance by an outcome the
check did not see: work the owner rejected wholesale, and work the owner kept and built on. The
`~4 blocks in 149 reviews` figure carried inside row 2(a) comes from a different, production-sized corpus
and measures a different population — ordinary work, most of which is sound. The two numbers are checked
for **consistency** in §4, never equated.

**Three divergences from AC-11's wording, all recorded rather than averaged away:**

| # | Divergence | Why it exists | Direction |
|---|-----------|---------------|-----------|
| D-a | The three **TFW-48** rows run against the master HL as it stood at `721ca15` — *post-drift*, not at an approved baseline | TFW-48's pre-amendment HL was never committed. That is the documented TFW-48 failure and the reason frozen DoD-5 exists. There is nothing else to read | **Harder.** The check must fire while reading the contract the drift already reached |
| D-b | The three **sound-corpus** rows have no frozen baseline either — the contract mechanism did not exist in 2026-04/08. The reference set is each master HL as committed when the review ran | Pre-contract tasks cannot have a freeze commit. Stated so a reader does not mistake this for the shipped recovery path failing | **Neutral** for a false-positive test |
| D-c | No project north star existed for any of the nine. Every row runs on the **fallback chain** — master HL §1 at the baseline | The designation is HL §11 S38 and is deliberately not yet written into either README (TS §2) | **Neutral, and it is the point:** the fallback is what makes the check work on day one |

**Correction of record — 2026-08-13, second pass.** The first version of this file ruled row **49/A** the
*third outcome* (reference set internally inconsistent), on the reading that TFW-49's approved §1 promised
*"readable without special tooling"* while approved DoD-3 required a versioned structural validator.
**That ruling was wrong, and the cause was a quotation ended early.** At `9e19a4f` the sentence continues:

> "The identity remains readable without special tooling, **while structural validation prevents quiet
> drift** between Coordinator, Researcher, Executor, Reviewer, adapters, and repositories."

§1 asks for both properties in one breath; DoD-3 discharges the second, and DoF-8 — which forbids
enforcement resting *only* on prose or *only* on unversioned `.git/` state — is satisfied by any versioned
check. No pair of clauses here is jointly unsatisfiable. Row 49/A is re-scored to **`✅ aligned`** in §1,
which is where research iteration 2 put it before amendment A6 existed. **So the shipped check and the
research replay agree on all nine rows** — the earlier claim that they diverged was an artifact of the same
truncation. Found by REVIEW Phase C (D1), verified against the source before acceptance, and recorded here
as a correction rather than a silent rewrite, because a phase whose thesis is *alignment must be cited, not
asserted* cannot quietly repair a citation.

The truncation originated in research iteration 2 and reached three sections of the HL as well; the
coordinator corrected those and appended a correction of record below §12 without rewriting A6's row.
**A6's verdict stands** and the third outcome ships on its structural argument; what is withdrawn is the
claim that an instance had been observed.

---

## 1. Rejected corpus — TFW-48 and TFW-49

> Owner's verdict on the whole result: *"TFW-49 solved a small prompt-design need with an unnecessary
> software subsystem. … Phases A–C remain immutable failure evidence; they are not the desired
> architecture."* 149 files, 27,103 deletions on revert. Every review below returned ✅ APPROVE.

### 48/A — Re-derive the Method Kernel · shipped verdict ✅ APPROVE

| Field | Filled as the shipped row requires |
|---|---|
| **Citation + harm** (one field) | Serves §1 Vision — *"The resulting framework is **smaller where precision and references can replace prose**"* — and fails it in the same act: the phase introduced a **Method Kernel** plus five independent obligation contracts (rule, proof, learning, extension, numeric-control) above the existing owners. Concrete harm: a new agent must now learn a kernel abstraction and five contract names **before** reading any workflow, and the surface the phase was chartered to shrink grew by five named layers |
| **Excess / adjacency** | **Fires.** Master **DoF-12**: *"The result adds another conceptual layer or document that duplicates an existing owner instead of simplifying the method."* The kernel duplicates `conventions.md` + `README` ownership |
| **Deferral confession** | No |
| **Materiality** | Yes — not phrasing. Every future reader pays the layer, and the owner's rejection names precisely this |
| **Outcome** | ❌ **`not fit for purpose`** → owner. **FIRES (strong)** |

> What the shipped review did instead, quoted from two places in the same file and checked verbatim to the
> end of each sentence: its Judge row 2 reads *"Phase HL P1–P10 all pass through their mapped ACs"*
> (`REVIEW__phase-a__method_kernel.md`:38) and its verdict concludes *"…satisfies all nine Phase A
> acceptance criteria and preserves all ten mapped principles"* (:51). The row was answered against a
> **Phase HL** that authored its own ten principles where the master carried thirteen — so master P7, P10
> and P12 were not in the table at all. This is the inverted check the phase replaces, caught in the act.
>
> _(REVIEW Phase C item 3 read the second quotation as a paraphrase of the first. Both sentences exist, at
> the lines given; the quotation was verbatim. Attributing each half to its own line is the improvement
> that was actually available, and it makes the stronger claim — the mapping was against the Phase HL — the
> one carrying a citation.)_

### 48/B — Planning, Research and the Learning Loop · shipped verdict ✅ APPROVE

| Field | Filled |
|---|---|
| **Citation + harm** | Serves **DoD-6** — *"Planning preserves user insights, product requirements, applicable Project Values, and uncertainty through to verifiable specification elements without embedding ready-made implementation"* — and delivers exactly that across twelve declared consumers. **No harm can be named.** The field is therefore filled with a citation and an explicit *no material harm*, which is the shape of an honest `✅` |
| **Excess / adjacency** | Tension only: the phase propagates Phase A's layer. But propagation into the twelve declared consumers is what the phase declared, config and topology were verified unchanged, and no non-goal, DoF item or phase boundary excludes it. **A downstream phase is not answerable for its predecessor's excess** |
| **Deferral confession** | No — H4 is declared unresolved and shipped as a non-claim, which is a deferral *without* shipping it here anyway |
| **Materiality** | N/A — nothing to block |
| **Outcome** | ✅ **aligned.** No block |

> **This row is the load-bearing one for AC-11.** A check that condemned all six would be a corpus
> detector, not a purpose check. The rejected task contains a phase that passes.

### 48/C — Specification, Execution and Evidence · shipped verdict ✅ APPROVE

| Field | Filled |
|---|---|
| **Citation + harm** | Serves **DoD-12** — *"Every claimed deliverable has local proof; crossed interfaces/sources and stakeholder/live claims add seam or live proof, and honest deferral creates explicit value debt"* — and exceeds it: the phase shipped **Proof Records**, **Value Debt**, **Executor Attestation** and a Local/Seam/Live taxonomy as a *second* evidence vocabulary over the existing Evidence Layer (D52/D53: `evidence/` folder, EV file, four-status vocabulary). Harm: two evidence languages in one framework, so a reviewer auditing an EV file has to know which one a given task speaks |
| **Excess / adjacency** | **Fires.** DoF-12 again — another conceptual layer duplicating an existing owner. Adjacency: the four scope values were re-cast as *"transitional attention signals"*, a change to the normativity of limits whose declared home is **Phase E (Lifecycle, Limits)** |
| **Deferral confession** | **Partial — and it is the adjacency finding's twin.** The phase states the limits question belongs elsewhere and still changes what the limits mean, here |
| **Materiality** | Yes — evidence vocabulary is what a reviewer must read to do the job |
| **Outcome** | ❌ **`not fit for purpose`** → owner. **FIRES (strong)** |

### 49/A — Canonical Contract and Validator · shipped verdict ✅ APPROVE

> **Re-scored on the second pass.** The first version ruled this row the third outcome on a truncated
> quotation of §1 — see the correction of record in §0. Below is the row as the shipped check actually
> returns it.

| Field | Filled |
|---|---|
| **Citation + harm** | **DoD-3** — *"A versioned structural validator rejects malformed or missing identity with an actionable expected example"* — resolves and is directly served by the delivered schema + Python formatter/parser/validator/range auditor. And §1 asks for it in the same sentence as readability: *"The identity remains readable without special tooling, **while structural validation prevents quiet drift**…"*. **No harm can be named against the cited clauses.** Citation alone approves this phase — H11's finding reproduced on the shipped wording |
| **Excess / adjacency** | Argued and rejected. 1,708 lines is a great deal of validator, but DoD-3 asks for one, **DoD-7** asks for *"repository fixtures … across all four TFW roles and at least two agent surfaces"* including *"search/filter behavior"* — which is what the range auditor serves — and the review verifies no Phase B/C, hook, config or adapter spill. Nothing was delivered that a cited clause does not ask for, and no non-goal, DoF item or phase boundary excludes it |
| **Deferral confession** | No |
| **Materiality** | N/A — nothing to block |
| **Outcome** | ✅ **aligned. No block** — the same verdict research iteration 2 recorded |

> **This row is where the check meets its own boundary, and the boundary is the argument for the anchor.**
> TFW-49 Phase A is aligned *with its approved contract*, and the owner rejected the product anyway:
> *"TFW-49 solved a small prompt-design need with an unnecessary software subsystem."* Part of the scope the
> owner rejected was a faithful reading of the DoD the owner approved. The check judges against the
> baseline, so a contract that is **internally coherent but wrong for the product** returns `aligned` and
> the check cannot help.
>
> That is not the third outcome — which needs clauses that *cannot both be satisfied* — and it is not a
> defect in the check. It is precisely the case HL §4 says the **north star** exists for: *"the only defence
> against a task whose own approved HL is wrong for the product."* This replay therefore supplies the
> missing empirical support for the deliverable weighting the HL declares: the reference-set rule catches
> 48/A, 48/C, 49/B and 49/C; only an anchor above the task HL could have caught 49/A. Priority 0 is not
> insurance — it is the one lever aimed at the failure this row demonstrates.

### 49/B — Workflow and Adapter Consumption · shipped verdict ✅ APPROVE

| Field | Filled |
|---|---|
| **Citation + harm** | Serves **DoD-4** — *"Every framework-owned commit-producing workflow and supported adapter has an observable point-of-action consumer of the canonical contract"* — and exceeds it: the delivered *consumer* is an executable **operation router** with its own test suite, 3,160 lines. Harm: a subject-line convention acquires a second runtime component that every future workflow change must keep in step, and Principle 11 promised the opposite — *"agents see the local imperative and one valid example at commit time; edge-case details remain in the canonical owner"* |
| **Excess / adjacency** | **Fires (moderate).** "Observable consumer" is loose enough to be argued into a router, which is why the confidence is moderate rather than strong. §1's *"readable without special tooling"* is the clause the router walks past |
| **Deferral confession** | No |
| **Materiality** | Yes — 3,160 lines of runtime is the substance of what the owner rejected, not its phrasing |
| **Outcome** | ❌ **`not fit for purpose`** → owner. **FIRES (moderate)** |

### 49/C — Repository-Local Enforcement and Migration · shipped verdict ✅ APPROVE

| Field | Filled |
|---|---|
| **Citation + harm** | Serves approved **Phase C deliverable 1** — *"**Replace or safely bypass** the current local branch-prefix hook without deleting history or unrelated user hooks"* — and delivers a **TFW-owned two-hook runtime, a private Git-common-dir ledger and a bounded carrier**. Harm, named concretely: enforcement now lives in unversioned `.git/` state that no clone carries, so the provenance guarantee is true only on the machine that ran the installer |
| **Excess / adjacency** | **Fires (strong), twice.** Excess: *"safely bypass"* → install a runtime. Adjacency: **DoF-8** — *"Enforcement depends only on agent compliance prose **or only on unversioned `.git/` state**"* — is an approved failure condition and the delivered ledger sits in exactly that state |
| **Deferral confession** | Present in the trace: the independent reviewer commit `1ebb680` recorded **7 of 10 Judge checks FAIL** and was overwritten three commits later |
| **Materiality** | Highest in the corpus. This is the phase the owner names when describing the failure |
| **Outcome** | ❌ **`not fit for purpose`** → owner. **FIRES (strong)** |

---

## 2. Sound corpus — reviews the owner kept and built on

### TFW-50 — Minimal agent commit attribution · ✅ APPROVE, and it stands

| Field | Filled |
|---|---|
| **Citation + harm** | Serves §1 Vision — *"One precise Markdown rule achieves this **without enforcement software**"* — and the review verifies the boundary is exactly six existing paths, Markdown only, with no runtime, no cadence rule and no automatic-push authority. **No harm nameable** |
| **Excess / adjacency** | None. The corrective write is exactly two files; four adjacent files are byte-stable; the wider workflow/adapter corpus carries no competing rule |
| **Deferral confession** | No |
| **Outcome** | ✅ **aligned. No block** |

> **The sharpest discrimination result in the corpus.** TFW-49 and TFW-50 answer the *same* product
> question. The check fires on one and stays silent on the other, and the discriminator is not quality —
> both were verified, tested and internally consistent — but whether the delivery matched the clause it
> claimed to serve.

### TFW-42/A — Research cycle restructure · ✅ APPROVE, and it stands — **with a near-miss worth reading**

| Field | Filled |
|---|---|
| **Citation + harm** | Serves §1 Vision clause by clause — one `research/` container, numbered stage files sorting in execution order, kebab-case phase folders, `iterations.yaml` as the brief. Delivered item for item. **No harm nameable** |
| **Excess / adjacency** | **The check notices something, and the materiality bar stops it.** The phase also added a five-row *agent selection guidance table*, which the owner later removed as tautological overhead (`process.md` F22, D50). Tested honestly: it sits inside the cited clause's territory (*"agents … know exactly what to investigate"*), no non-goal, DoF item or phase boundary excluded it, and its harm is five rows of redundant instruction — not material impact on the value. Both TS deviations were disclosed and one was pre-approved at ONB |
| **Deferral confession** | No |
| **Materiality** | **Fails the bar, deliberately.** A block here would be the AFD-48 false positive reproduced |
| **Outcome** | ✅ **aligned. No block** |

> **This is the row that earns the materiality bar.** ONB §5 risk 1 predicted a false positive would
> appear here first — it is the one sound-corpus review the research iteration never ran — and something
> *did* surface. The bar is load-bearing, not decoration: without it, this replay would have produced a
> block on work the owner kept, and AC-11 would have failed on the check rather than on the corpus.

### TFW-47/B — Codex adapter · ✅ APPROVE, and it stands

| Field | Filled |
|---|---|
| **Citation + harm** | Serves §1 Vision — *"Codex becomes a first-class TFW adapter with dedicated shortcut skills … matching the adapter parity already achieved for Claude Code and Antigravity"* — with parity verified across six copies and live routing exercised on Codex Desktop. **No harm nameable** |
| **Excess / adjacency** | None. The one deviation — `$tfw-*` → `/tfw-*`, against the research conclusion — moves *toward* the cited clause (a truthful adapter) and was disclosed in RF §2 D7 and §6 obs. 3. Removing legacy duplicates is inside the clause |
| **Deferral confession** | No |
| **Outcome** | ✅ **aligned. No block** |

---

## 3. Result

```
REJECTED CORPUS — owner rejected the whole result (6 reviews, all shipped ✅ APPROVE)

              cite   excess/adjacency        confession   materiality   OUTCOME
48/A  kernel   ✓     ██ DoF-12 layer              ·          material    ❌ not fit for purpose
48/B  planning ✓      ·  tension only              ·             —        ✅ aligned
48/C  spec/ev  ✓     ██ DoF-12 + Phase E edge    ░ partial    material    ❌ not fit for purpose
49/A  validator✓      ·  argued, rejected          ·             —        ✅ aligned
                        └ §1 asks for readability AND structural validation in one sentence;
                          DoD-3 discharges it. Aligned with a contract the owner still rejected
                          → the case only a NORTH STAR can catch, not this row
49/B  router   ✓     ▓  cue → executable router    ·          material    ❌ not fit for purpose (mod)
49/C  migration✓     ██ "safely bypass" → runtime ░ 1ebb680   material    ❌ not fit for purpose
                     ██ DoF-8: unversioned .git/ state
                                                          ────────────────────────────────
                                                          4 non-approve · 2 aligned

SOUND CORPUS — work the owner kept and built on (3 reviews)

TFW-50   markdown-only rule      ✓  no excess              ·      —   ✅ no block
TFW-42/A research container      ✓  noticed → immaterial   ·   fails bar  ✅ no block
TFW-47/B codex adapter           ✓  deviation toward clause ·     —   ✅ no block
                                                          ────────────────────────────────
                                                          0 of 3 blocked
```

| AC-11 condition | Result |
|---|---|
| ≥1 non-approve on the rejected corpus | ✅ **4 of 6** — all four `not fit for purpose` (3 strong, 1 moderate). Was 5 of 6 on the first pass; 49/A re-scored to aligned (§0) |
| 0 blocks on the sound corpus | ✅ **0 of 3** — untouched by the correction |
| Every outcome carries a filled citation-and-harm field | ✅ nine rows, each with the clause quoted and the harm named or explicitly absent |
| Third outcome recorded as such, not collapsed into "fired" | ⚪ **no instance in the corpus.** The one candidate was withdrawn on the second pass; the outcome ships on its structural argument, and `judge.md` now says plainly that no instance has been observed |
| Post-drift rows recorded per review | ✅ D-a — the three TFW-48 rows |
| Check did **not** fire on sound work | ✅ — and the one place it came close (TFW-42/A) is written up rather than smoothed over |

## 4. Reconciliation with the `~4 in 149` figure the row carries

They measure different populations and are consistent, not equal:

| Corpus | Composition | Purpose-check result |
|---|---|---|
| Production (~149 reviews, the figure inside row 2(a)) | ordinary work, overwhelmingly sound | ~4 goal-based blocks — a **low** rate |
| This replay, sound half (3) | selected for being kept and built on | **0** blocks — consistent with a low production rate |
| This replay, rejected half (6) | selected for total product-fit failure | **4** non-approve — consistent with a check that fires when purpose actually fails. The two that pass are the informative half: 48/B is a sound phase inside a rejected task, and 49/A is a phase aligned with a contract that was itself wrong for the product |

A check with a low production rate and a high rate on a corpus selected for failure is behaving as
designed. The inconsistent result would have been fires on the sound half (a phrasing police) or none on
the rejected half (a rubber stamp). Neither appeared, and after the second pass the shipped check agrees
with research iteration 2 on **all nine rows** — two independent runs, one of them adversarial to the
other's design, reaching the same nine outcomes. **Nine samples remain nine samples:** the honest
next measurement is the one research iteration 2 already named — after 5–10 live reviews, count how many
Purpose Check rows cite a clause *and* name a harm. A row that never names a harm is decaying.

## 5. The check's own failure mode, tested (AC-2's second half)

The same row, filled two ways against **RF TFW-53/B** — reference set: HL-TFW-53 at frozen baseline
`e8ee76e`, fallback in use because this project's north-star designation is not yet written into either
README (HL §11 S38, TS §2):

**Passing form.** *Serves §1 Vision — "Research can no longer edit them; it can only propose an amendment,
with evidence, into a visible Amendment Log, and wait for an explicit owner verdict." Harm avoided is
concrete and measured: `plan.md` Step 6c previously instructed the coordinator to rewrite the HL, and this
phase's own replay found a live frozen-section edit (DoD-18's priority-1 relabel) carrying an owner ruling
but no §12 row — without the shipped step that class of edit stays invisible.* → excess: none, the file
left the phase shorter · deferral: none, the two deferred items were routed and named · **✅ aligned.**

**Failing form, rejected by the row's own wording.** *"✅ — aligned with §1 Vision."* → the citation
resolves and the field carries **no harm**, so the row fails on its stated condition: *"A harm asserted
with no citation fails it. `✅` with an empty field fails it."* And the two escapes are pre-closed — *"the
TS scoped it this way"* would not have covered AC-6's word-count shortfall, and *"tests are green"*
(68 passed) is listed as insufficient grounds.

---

*Purpose Check Replay — TFW-53 / Phase C | 2026-08-13*
