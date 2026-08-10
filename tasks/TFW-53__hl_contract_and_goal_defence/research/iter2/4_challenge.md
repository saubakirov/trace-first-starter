# Challenge — "What do we NOT expect?"

> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> **Test:** "Would my surviving configurations hold if a different researcher attacked them?"
> Parent: [HL-TFW-53](../../HL-TFW-53__hl_contract_and_goal_defence.md)
> Goal: An approved HL is a contract, and the reviewer is its defender — review asks "is this what we set out to do?" against a north star above the task.

---

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D7 Reference set | B — includes the Phase HL | — | (A1, approved) | A1 makes the Phase HL derivation-only: it may not carry §1/§5/§6/§7. It therefore holds nothing to measure against, and anything it *does* hold is unapproved. Including it can only import drift — TFW-48 is the proof (master P7/P10/P12 absent from the phase HL its reviewers used) |
| D7 Reference set | C — includes the TS | — | HL Principle 16 | *"Judge against the baseline, never the spec — the TS is downstream of any drift, so measuring against it can only confirm the drift."* Direct contradiction with a frozen principle; also DoF-12 |
| D7 Reference set | D — north star only | — | DoD-19 (frozen) | DoD-19 fixes the reference set as *"the committed contract baseline **plus** the north star"*. Dropping the baseline would require an amendment and would lose the only anchor that exists today for tasks with no project north star |
| D4 Forcing function | C — free text, no citation | D6 Materiality | any | Materiality attaches to a named claim. With no citation there is no claim to test impact against, so every materiality mechanism degrades to the reviewer's unexamined opinion. C0 and C1 — the two real-world controls — are exactly this combination, and both failed |
| D2 Payload | D — full vision document | D4 Forcing function | A — quote a clause | A 509-line anchor mixing purpose with implementation detail lets any work find a true, resolvable, non-purposive clause (E3: AFD's P14 Kalman filter). The citation requirement is satisfied and the check is neutralised — worse than no forcing function, because it now produces evidence of diligence |
| D1 Locus | B — nominated HL | D3 Obligation | C — optional, silent fallback | E2: the nominated HL is a *task* contract inside the drift path. With no rule promoting and freezing it at project level, the anchor drifts exactly as AFD's did (10 → 14 principles, six unlogged additions). An anchor that moves is not an anchor |
| D3 Obligation | A — mandatory, no fallback | — | F21, F13, H12 | Review becomes impossible in any project without a designated anchor, including every existing TFW project on the day of upgrade. Contradicts the explicit-N/A pattern (F21) and makes the framework un-adoptable for small projects — the risk HL §9 already flags |
| D5 Verdict class | B — new verdict token | — | DoD-22 (frozen) + Phase E | DoD-22 already fixes a goal failure as *"sufficient grounds for `❌ REJECT`"*. A fourth token needs an amendment, and Phase E is concurrently introducing `❌ REJECTED` as a terminal **status** — two new `❌` tokens in one release is the D17 confusion pattern |
| D6 Materiality | A — prose clause only | — | G7 (empirical) | Not logically incompatible; empirically refuted inside this repository. D46's prose clause *"not rubber stamp"* was recorded in KNOWLEDGE.md and never reached `.tfw/`. Prose-only materiality has a measured retention rate of 0/1 here and 0/2 counting TFW-48's P7 |

**Surviving configurations:**

| Config | D1 Locus | D2 Payload | D3 Obligation | D4 Forcing fn | D5 Verdict | D6 Materiality | D7 Ref set | Notes |
|--------|----------|-----------|---------------|---------------|------------|----------------|------------|-------|
| **C4** | A root README | C purpose + principles + non-goals | D fallback chain | A quote + path | D REJECT + named finding + owner routing | D two-part test | A baseline + north star | Cheapest survivor. Satisfies DoD-17..22 without amendment |
| **C5** | A root README | C purpose + principles + non-goals | D fallback chain | **D quote + concrete harm** | D | D two-part test | A | C4 with the forcing function carrying the harm clause — closes E4's "resolves but irrelevant" hole by fusing D4 and D6 |
| **C6′** | B nominated HL **and project-frozen** | C | D fallback chain | A quote + path | D | C proportionality | A | Survives only in the *nominated-and-frozen* form (E2). Needs a project-level freeze mechanism this task has not scoped |
| **C10** | A root README | C | D fallback chain | A quote + path | **C tiered inside existing tokens** | D two-part test | A | Unexpected survivor — see below |

**Unexpected survivors:**

- **C10 — tiered verdict inside the existing tokens.** Nobody proposed it: the HL discusses only "does a goal failure
  need a name distinct from REJECT". Tiering says something different — that *some* purpose failures are repairable in
  place (goal-`REVISE`) and only the "wrong thing entirely" case is goal-`REJECT`. It survives because DoD-22 says
  REJECT is *sufficient* grounds, not *the only* consequence, so tiering needs no amendment; and because the measured
  corpus is 26 REVISE to 1 REJECT (G8) — a check whose only output is REJECT will be under-used by reviewers who can see
  the work is fixable. Its weakness is that the tier boundary has no crisp test, which is why it ranks below C5.
- **C5's fusion of D4 and D6.** Treating the forcing function and the materiality bar as *one* field — "quote the clause
  and name the concrete harm" — was not in the design space as stated; the HL lists them as two of three independent
  clauses. Fusing them makes the same sentence carry both the anti-rubber-stamp and the anti-nitpick force: a reviewer
  who cannot name a concrete harm has failed the materiality bar, and a reviewer who cannot quote a clause has failed the
  citation requirement. One field, two failure modes closed.

---

## Findings

### C1: The drafted check (the thing being replayed)

Stated concretely so the replay tests something falsifiable rather than an intention. This is the C5 configuration
expressed as a `judge.md` row plus its reference-set rule.

> **Reference set.** The master HL at its **frozen baseline** (`git log --grep='/{TASK}/freeze/'`) plus the **project
> north star**. The Phase HL and the TS are **not** valid references for this check.
>
> **Row — Purpose served?** Answer all three; a bare ✅ is not an answer.
> **(a) Citation.** Quote the north-star or baseline clause this work serves, with a resolvable path. "Aligned" without a
> citation is not an answer.
> **(b) Excess and adjacency.** Does the result deliver something the cited clause does not ask for, or that a baseline
> non-goal, DoF item or phase boundary excludes?
> **(c) Investment or workaround.** Does the specification or the result state that the correct home, form or owner of
> this change is elsewhere, and ship it here anyway? *(deferral confession — E7)*
>
> **Materiality.** A block must name **both** the violated claim **and** the concrete consequence. Wording alone is never
> grounds.
> **Override.** *"The TS scoped it this way"* and *"the tests are green"* are **not** sufficient grounds to APPROVE.

### C2: Replay against the rejected corpus (HL DoD-26, part 1)

Six REVIEW files at `721ca15`; each replayed against its **approved** master baseline — TFW-49 at `9e19a4f`, TFW-48 at
`721ca15` (its master was amended by an unrecorded "research update approved 2026-07-29" that was never committed, so
`721ca15` is the only recoverable text; noted as a limit).

| # | Review | (a) Citation available? | (b) Excess / adjacency | (c) Deferral confession | Outcome |
|---|--------|------------------------|------------------------|-------------------------|---------|
| 1 | **TFW-48 / A** — Method Kernel | Yes — master P1 *Purpose Before Process*, P3 *Preserve Proven Outcomes* | **Yes, material.** The phase delivered *"the five-obligation Method Kernel and independent rule, proof, learning, extension, and numeric-control contracts"* — five new contract layers. Master **DoF-12** reads: *"The result adds another conceptual layer or document that duplicates an existing owner instead of simplifying the method."* Additionally the reference-set rule surfaces that the Phase A HL authored its own 10 DoD / 9 DoF / 10 principles and **dropped master P7, P10 and P12** — including P12 *No Arbitrary Compression Target*, on a compression task | No | **🔄 REVISE / ❌ REJECT — fires** |
| 2 | **TFW-48 / B** — planning, research, learning | Yes — master P6 *Reality Can Overrule the Plan*, P8 *Learning Must Become Portable* | **Tension, not a confident block.** *"One bounded Comparative Decision Procedure"* + *"qualitative focused/deep intensity"* sits adjacent to §7.1's prohibition (*"must not add a cognitive-strategy selector, catalog, or strategy extension contract while H4 remains unresolved"*), but the review explicitly records an *"H4 unresolved/T0-only non-claim"* — the reviewer engaged with the boundary and stayed inside it | No | **✅ passes — does not fire** |
| 3 | **TFW-48 / C** — specification, execution, evidence | Yes — master P5 *Structural Gates for Invariants* | **Yes, material.** Introduces *Proof Records*, *Value Debt*, *Executor Attestation* and an `EV` indexing artifact. TFW already had a canonical owner for this: D52's Evidence Layer, RF §5, `evidence/`. Master **DoF-12** again — a new document duplicating an existing owner | Partial — the phase declares four scope values *"become transitional attention signals"*, i.e. their real owner is a later, unbuilt phase | **🔄 REVISE — fires** |
| 4 | **TFW-49 / A** — canonical contract and validator | Yes — approved **DoD-3** *"a versioned structural validator rejects malformed or missing identity"* | **No confident block.** A JSON schema plus a standard-library formatter/parser/validator is a defensible reading of approved Phase A deliverable 4 (*"one versioned semantic owner and a cross-platform validation surface"*). The *"range auditor"* is marginal but arguable | No | **✅ passes — does not fire** |
| 5 | **TFW-49 / B** — workflow and adapter consumption | Yes — approved Phase B deliverable 2 (*"all TFW roles and adapters consume the same canonical contract"*) | **Yes, moderate.** Approved Phase B asks for *"a short mandatory identity **cue** immediately before every workflow action that can create a commit"* — a documentation change. Delivered: *"one standard-library operation **router** and its isolated tests"*, a second Python module, alongside the 26 workflow edits. Against §1's *"readable without special tooling"* this is adjacency: the phase's declared outcome was cues, and a runtime component arrived with them | No | **🔄 REVISE — fires (moderate)** |
| 6 | **TFW-49 / C** — repository-local enforcement migration | Yes — approved DoD-5 (*"install, verify, repair, and migrate enforcement without overwriting unrelated user Git-hook behavior"*) | **Yes, strong.** Approved Phase C deliverable 1 says *"Replace or safely **bypass** the current local branch-prefix hook"*. Delivered: *"recognized repository-local **two-hook runtime**, private **Git-common-dir ledger**, bounded **carrier**, exact exclusive/root-inclusive **DAG audit**"* — three artifact classes that appear nowhere in the approved contract. And the private ledger lives in the Git common dir, i.e. **unversioned `.git/` state**, which approved **DoF-8** names as a failure condition (*"Enforcement depends only on agent compliance prose or only on unversioned `.git/` state"*) | Yes — the same file's earlier revision at `1ebb680` was a 🔄 REVISE titled *"request runtime lifecycle corrections"*, i.e. the reviewer sensed the runtime was wrong-shaped and routed it as a quality fix | **❌ REJECT — fires strongly** |

**Result: 3 confident fires + 1 moderate, 2 passes.** DoD-26's requirement on this half (*at least one non-approve*) is
met four times over. The two passes are the important half of the outcome: the check discriminates. It does not condemn
TFW-49 Phase A, which was largely inside its contract, nor TFW-48 Phase B, whose reviewer explicitly policed the
boundary the check would have tested.

**Honest counter-finding, and it is significant.** The approved TFW-49 contract was **internally in tension**. §1 says
*"readable without special tooling"* and *"provenance, not decoration"*; DoD-3 demands *"a versioned structural
validator"*; DoD-7 demands *"repository fixtures"* across four roles and two surfaces; DoF-8 makes *"agent compliance
prose"* alone a **failure**. A large part of what the owner later rejected as *"an unnecessary software subsystem"* is a
faithful reading of the DoD the owner approved. The goal check fires on Phase C because of **excess against the phase's
declared outcome** and a **named DoF hit**, not because the runtime as such was forbidden. Two conclusions follow:

1. The check's discriminating power comes from **(b) excess against the declared outcome**, not from (a) citation.
   Citation is what makes (b) auditable; (b) is what does the work. A design that ships (a) without (b) — the pure
   "quote a clause" reading of DoD-20 — would have approved TFW-49 Phase C.
2. Some of TFW-49's failure was an **HL authoring defect**, not a review defect: a §1 and a §5 that pull in opposite
   directions cannot be defended by any downstream role. This is out of TFW-53's scope and belongs in the coordinator's
   HL-writing surface, but it bounds what Phase C can promise. Recorded as an Open Question.

### C3: Replay against sound reviews (HL DoD-26, part 2 — the false-positive control)

Three TFW reviews from the surviving corpus, chosen because each closed a task the owner kept and built on.

| # | Review | Cited clause | (b) Excess? | (c) Confession? | Outcome |
|---|--------|-------------|-------------|-----------------|---------|
| 1 | **TFW-46 / A** — Evidence templates | HL-TFW-46 §1: *"Every task produces an Evidence section where the executor demonstrates observable outcomes in a live environment… Self-deception is structurally hard because evidence requires real artifacts"* — the phase delivers precisely this | Two out-of-scope files (`compilable_contract.md`, `knowledge.md`) updated to prevent stale refs, **documented as deviations**. Not adjacency: it is maintenance of references to the thing being changed, disclosed in the RF | No | **✅ APPROVE — no block** |
| 2 | **TFW-47 / B** — Codex adapter | HL-TFW-47 §1: *"Codex becomes a first-class TFW adapter with dedicated shortcut skills… matching the adapter parity already achieved for Claude Code and Antigravity"* | No. The one deviation — `$tfw-*` → `/tfw-*` based on live Codex observation — moves the result *toward* the cited clause by making the adapter truthful. A purpose check should read this as a positive deviation, and does | No | **✅ APPROVE — no block** |
| 3 | **TFW-50** — commit attribution | HL-TFW-50 §1, verbatim: *"One precise Markdown rule achieves this **without enforcement software**"* — and the result is Markdown-only across six existing paths, with *"no runtime or cadence mechanism"* | No. The Map states the boundary the vision states, in the vision's own terms | No | **✅ APPROVE — no block** |

**Result: 0 of 3 blocked.** DoD-26's second requirement is met.

TFW-50 is worth naming as a positive control of unusual quality: it is the *same problem* as TFW-49, re-done after the
revert, and its Vision contains the exact clause (*"without enforcement software"*) that TFW-49 Phase C violated. The
check passes it for the same reason it blocks TFW-49/C — both readings come from comparing the result to the declared
outcome, not from a preference about runtimes.

### C4: The f2 negative control — TFW-48's master already demanded goal defence, and lost it

The hardest question this iteration was given: TFW-48's approved master carried **DoD-11** (*"Review can reject work that
satisfies TS/RF but violates the product north star, Project Values, cited sources, delivered reality, evidence honesty,
or an adjacent seam"*) and **P7** (*"Independent Review Protects the North Star — the reviewer is not a consistency
checker for documents; it is the last quality authority"*). Both were lost. Would the drafted check have fired *given
that the master already demanded it*?

The answer is uncomfortable and decisive:

1. **DoD-11 was a deliverable, not an active rule.** It described a capability TFW-48 was supposed to *build*. It could
   not govern TFW-48's own reviews, because the reviewers' checklist was the shipped `judge.md`, which had no such row.
2. **P7 *was* an active principle** — a frozen §7 item in the approved master — and it still did not fire. The mechanism
   of loss is exactly the reference-set defect: the reviewers checked `TS §3 Principles Check`, which was derived from
   the **Phase HL**, and the Phase A HL did not carry P7. The principle was live, approved, and invisible at the point
   of use.
3. **Therefore the reference-set rule (D7 Alt A) is load-bearing on its own.** Under the drafted check, a TFW-48 reviewer
   reads the *master* baseline, encounters P7, and must either cite it or explain its absence. The `judge.md` row is what
   makes reading the master baseline mandatory rather than aspirational.

**The generalised finding: a rule stated in an HL cannot defend that HL.** Goal defence written into a task's own DoD is
self-referential in the same way the principle chain is. It must live in the reviewer's template, in the framework, where
no task can drop it. This is the third instance of the retention pattern (with G7's D46 and iteration 1's TFW-48 finding)
and it converts HL Principle 3 (*structural enforcement over guidelines*) from a preference into a measured requirement:
**every rule this task ships that lives only in prose has a demonstrated survival rate of zero in this repository.**

### C5: Counter-evidence — the strongest case against shipping this

Deep mode requires actively seeking reasons the approach fails. Four survive scrutiny; three of them change the design.

**(i) The check is a judgement call wearing a checklist's clothes.** Every fire in C2 rests on a reviewer forming an
opinion about whether a deliverable "exceeds" a declared outcome. Two competent reviewers can disagree on TFW-49/B.
The citation makes the disagreement *visible* and *arguable*, which is the honest claim — it does not make the check
objective. Any framing that presents this as a mechanical gate will oversell it and, worse, invite agents to treat a
resolvable citation as a passing score. **Design consequence:** the row must be phrased as a judgement with a mandatory
evidence format, never as a pass/fail test.

**(ii) A reviewer motivated to approve can satisfy every clause.** Quote a true clause, assert no excess, assert no
confession, and the row is complete. The check raises the cost of a dishonest pass from zero to one paragraph — it does
not make it impossible. The only real defence is that the paragraph is *durable and re-readable*, so a later role or the
owner can falsify it. That is precisely how both AFD cases were actually caught (S22: neither fired unprompted; both were
caught by the owner reading output). **Honest positioning: the check makes rubber-stamping legible, not impossible.**

**(iii) The base rate argues the check will be right 145 times out of 149 by answering "aligned".** Being right by
default is how a gate decays (G12's "change theater"). The mitigation is not a higher firing rate — that is DoF-13 — but
the fact that the *cost* of the honest answer is one citation, which is paid whether or not it fires. A gate that costs
one line and fires 3% of the time is a good trade; a gate that costs a stage and fires 3% of the time is not, which is
the H8 argument that already carried.

**(iv) The strongest single objection: TFW-49's contract contradicted itself, and no reviewer can defend a contradictory
contract.** C2 established this. If the master's §1 and §5 disagree, the goal check produces a defensible fire and a
defensible pass from the same evidence, and the reviewer's verdict becomes a coin flip dressed in citations. Phase C
cannot fix this; it is an HL-authoring problem. **Design consequence:** the check must be permitted to return a third
outcome — *the reference set is internally inconsistent* — which routes to the owner as a contract defect rather than a
work defect. Without it, the first contradictory HL will produce a false REJECT and the check will lose credibility on
its debut, exactly as AFD-48/B's wording block nearly did.

### C6: Vocabulary stress test — de-domaining and collision

Each candidate pushed through three tests: does it survive outside software (F13); does it collide with a term already
live in `.tfw/`; and does an agent behave differently on reading it (D28).

| Term | Outside software | Collision in `.tfw/` | Behavioural read | Verdict |
|---|---|---|---|---|
| `Validation` / `Validation failure` | ✅ IEEE 1012, standards-backed | ❌ **severe** — `verify.md` already performs verification; "validator" is TFW-49's own linter; schema/form validation dominate the word in agent priors | Ambiguous — an agent may run a schema check | **Rejected as a label.** Keep the IEEE pair as the *rationale* for why the axis exists, not as the name |
| `Not fit for purpose` | ✅ contract law and UK gate-review practice; works for a report, a curriculum, a business process | ✅ none | Strong — carries "the thing works and is still wrong" without further explanation | **Adopt as the finding name** |
| `Purpose failure` (paired with `quality failure`) | ✅ | ✅ none | Strong — names the axis, pairs cleanly with the existing quality axis | **Adopt as the axis name** |
| `Goal failure` | ✅ | ⚠️ soft — "goal" blurs into DoD/AC language | Weak — reads as "an acceptance criterion missed" | Use only in prose |
| `Declared outcome not achieved` | ✅ — AFD's *«объявленная функция фазы не достигнута»*, de-domained | ✅ none | Strong but long | **Adopt as the (b) test's phrasing**, not as a label |
| `Deferral confession` | ✅ | ✅ none | Strong — names a thing reviewers can look for | **Adopt for the (c) test** |
| `Hotfix, not investment` | ❌ software-only — F13 violation | — | — | **Rejected**; the underlying idea survives as *"a local workaround rather than a contribution to the target state"* |
| `Decoration, not delivery` | ✅ | ✅ none | Evocative, but describes a symptom rather than naming a category | Use in the anti-pattern text; not as the label |
| `North Star` | ✅ owner's own term; established practice | ✅ none (1 incidental hit) | Strong | **Adopt**, with G13's caveat: the *document* sense, explicitly **not** the North Star Metric sense |

Resulting minimal vocabulary: **Project North Star** (the anchor), **Purpose Check** (the row), **not fit for purpose**
(the finding), **deferral confession** (the tell), **NS{n}** (the citation namespace). Five terms, all
domain-agnostic, none colliding — against DoD-27's seven-term list for Phase D, which this feeds.

### C7: Stress test — does the check survive a non-code project?

F13 is a frozen citation (§7.2 #12) and the corpus is 100% software. Applying C1's three tests to two non-code cases:

| Case | (a) Citation | (b) Excess / adjacency | (c) Deferral confession |
|---|---|---|---|
| A quarterly analytics report; north star = *"the board decides pricing from one page"* | *"one page"* is quotable | A 40-slide appendix with per-segment cuts: excess against the declared outcome, materially — the board will not read it | *"Full methodology to follow in a separate memo"* shipped inside the deliverable = confession |
| A curriculum module; north star = *"students can do the task unaided by week 6"* | quotable | A module that adds an assessed group project not asked for: adjacency | *"Assessment rubric to be defined by the department later"* = confession |

All three tests transfer without rewording. The one element that does **not** transfer is the reference-set mechanism's
dependency on `git log --grep` for the baseline — a project not under version control has no diffable baseline. That is
already a known consequence of iteration 1's D5/D6 and is not new here, but it should be stated once rather than
discovered: **the contract baseline requires version control; the purpose check does not.** A non-versioned project can
still run (a)/(b)/(c) against the north star and the current master HL, losing only the drift-detection half.

### C8: What this iteration would look like if it were wrong

The single assumption everything rests on: that a reviewer who is *told to read the approved master baseline and cite it*
will actually do so. Iteration 1's corpus says agents route around unenforced instructions (`process.md` F14), and G7
says a prose clause in this framework has a survival rate of zero. The check is a `judge.md` row, which is stronger than
prose — the stage file is a required artifact and an empty row is visible. But it is weaker than a structural gate: no
file fails to exist if the row is filled with a plausible sentence.

The honest strength ordering of the three Phase C deliverables, after this iteration:

```
strongest  ── reference-set rule           (changes WHAT is read; a wrong reference is checkable by a later reader)
           ── forcing function + harm      (changes WHAT IS WRITTEN DOWN; unresolvable citations are detectable)
           ── judge.md row itself          (changes WHAT IS ASKED; can be answered emptily but not omitted)
weakest    ── Reviewer Identity amendment  (changes WHAT IS FELT; D46 proves identity text can be silently dropped)
```

The Identity amendment (DoD-21) is still worth shipping — D46 records that identity anchoring beats instruction volume —
but this ordering says it must not be relied on, and that its own clause is the one most likely to be quietly lost in a
future edit. Recording it here so a later maintainer can check.

---

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C1 — the check drafted concretely as reference-set rule + three-part row + materiality + override | Phase C TS drafting (not this role) |
| C2 — replay on rejected corpus: **3 confident fires + 1 moderate, 2 passes**; DoD-26 part 1 met with discrimination | — |
| C2 counter-finding — TFW-49's approved contract was internally contradictory; part of the rejected scope was a faithful reading of the approved DoD | Whether HL-authoring coherence is in scope (→ Open Question) |
| C3 — replay on sound corpus: **0 of 3 blocked**; DoD-26 part 2 met | — |
| C4 — f2 answered: P7 was live and still invisible, because the reference set was the Phase HL. **A rule stated in an HL cannot defend that HL** | — |
| C5 — four counter-arguments; (iv) forces a third outcome: *reference set internally inconsistent* → route to owner as a contract defect | Coordinator ruling |
| C6 — vocabulary settled: North Star · Purpose Check · not fit for purpose · deferral confession · `NS{n}` | Phase D terminology pass |
| C7 — all three tests transfer to non-code work; the *baseline* half requires version control, the *purpose* half does not | — |
| C8 — strength ordering; Identity amendment is the weakest link and must not be load-bearing | — |

**Sufficiency:**
- [x] External source used? — IEEE 1012 governs C6's rejection of `validation` as a label; the audit-standard anti-boilerplate requirement and the CCB "change theater" finding are load-bearing in C5(ii)/(iii); UK gate-review usage supplies `not fit for purpose`.
- [x] Briefing gap closed? — H11 tested against the corpus (C2 shows citation alone would have approved TFW-49/C; the excess test does the work), H12 and H13 resolved in Gather, DoD-26 replay executed in full, verdict vocabulary settled, f1/f2/f3/f4 all answered.
- [x] Pairwise incompatibility checked? Surviving configurations listed? — 9 incompatible pairs; C4, C5, C6′, C10 survive; C5 recommended.

**Mode-specific (deep):**
- [x] Hypothesis tested? — H11 tested and **qualified rather than confirmed**: the forcing function is necessary but not sufficient; the excess test is what discriminates.
- [x] Counter-evidence sought? — C5 in full, plus the C2 counter-finding, which is the most consequential thing in this iteration and argues *against* part of the HL's diagnosis.

**Metacognitive check.** The genuinely new discovery is the **C2 counter-finding**: TFW-49's approved contract contained
the scope it was later condemned for, so the story "the coordinator drifted and the reviewers missed it" is incomplete —
the HL's own §1 and §5 disagreed before any drift occurred. I did not expect to find that, I looked for it because deep
mode requires counter-evidence, and it changes the design (C5(iv): a third outcome for an inconsistent reference set).
The second new item is **C4's generalisation** — a rule stated in an HL cannot defend that HL — which is the sharpest
form of the retention thesis and applies recursively to TFW-53's own DoD-19..22. What I merely confirmed: H13, the AFD
base rate, and the vocabulary shortlist. Sources not consulted and worth naming: the remaining 143 AFD reviews were
sampled rather than enumerated, so the "~4 goal blocks" figure remains prior-recon-sourced rather than independently
recounted; and the TFW-48 master could not be read at its true approval point, because that HL was never committed
pre-amendment — the same hole DoD-5 exists to close, encountered here as a research limit.

Stage complete: YES
→ User decision: autonomous run — self-checkpoint passed, proceeding to Synthesis.
