# Extract — "What do we NOT see?"

> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW-53](../../HL-TFW-53__hl_contract_and_goal_defence.md)
> Goal: An approved HL is a contract, and the reviewer is its defender — review asks "is this what we set out to do?" against a north star above the task.

---

## Configuration Space

Dimension names as in [`2_gather.md`](2_gather.md). Not evaluated here — elimination happens in Challenge.
Eleven configurations; the full cross-product is 4⁷ = 16 384, so this is the reasoned set: the two real-world controls,
the design the HL currently implies, and the combinations that differ from it on at least one dimension in a way that
changes cost or failure mode.

| Config | D1 Locus | D2 Payload | D3 Obligation | D4 Forcing fn | D5 Verdict class | D6 Materiality | D7 Reference set |
|--------|----------|-----------|---------------|---------------|------------------|----------------|------------------|
| **C0** *(control: TFW today)* | — none | — | C optional, silent fallback | C free text | A reuse REJECT | — none | C + the TS |
| **C1** *(control: AFD today)* | B nominated HL | D full vision doc | C optional, silent fallback | C free text | A reuse REJECT | A prose clause | B + phase HL |
| **C2** *(HL as written)* | B nominated HL *or* section | C purpose + principles + non-goals | B mandatory field, N/A allowed | A quote + path | A reuse REJECT | A prose clause | A baseline + north star |
| **C3** *(owner instinct, minimal)* | A root README section | A purpose only | B mandatory field, N/A allowed | A quote + path | A reuse REJECT | A prose clause | A baseline + north star |
| **C4** | A root README section | C purpose + principles + non-goals | D fallback chain | A quote + path | D REJECT + named finding + owner routing | D two-part test | A baseline + north star |
| **C5** | A root README section | C purpose + principles + non-goals | D fallback chain | D quote + concrete harm | D REJECT + named finding + owner routing | D two-part test | A baseline + north star |
| **C6** | B nominated HL | C purpose + principles + non-goals | D fallback chain | A quote + path | D REJECT + named finding + owner routing | C proportionality | A baseline + north star |
| **C7** | D `KNOWLEDGE.md` §0 | B purpose + principles | B mandatory field, N/A allowed | B clause id only | C tiered inside existing tokens | B "what breaks" field | A baseline + north star |
| **C8** *(cheapest)* | A root README section | A purpose only | D fallback chain | B clause id only | A reuse REJECT | A prose clause | A baseline + north star |
| **C9** *(maximal)* | C new `NORTH_STAR.md` | C purpose + principles + non-goals | A mandatory, no fallback | A quote + path | B new verdict token | D two-part test | A baseline + north star |
| **C10** | A root README section | C purpose + principles + non-goals | D fallback chain | A quote + path | C tiered inside existing tokens | D two-part test | A baseline + north star |

---

## Findings

### E1: The load-bearing piece is the reference-set rule, not the anchor artifact

HL §4 Phase C names deliverable 1 (north-star anchor) *"the load-bearing piece; the other two are inert without it."*
G14 is direct counter-evidence.

At the moment TFW-49 Phase C shipped a hook runtime, the following were all true:

- An owner-approved Vision existed saying *"readable without special tooling"* and *"provenance, not decoration"*.
- An owner-approved Phase C deliverable said *"replace or safely **bypass**"*, not *install a runtime*.
- An owner-approved DoF-6 said *"normal human commits are blocked"* is a failure.
- All three were retrievable from git at `9e19a4f` throughout the task.
- Six reviewers read a Phase HL and a TS, both derived from the post-drift `642c647` text, and none opened `9e19a4f`.

The anchor was not missing. **The instruction to read the right one was.** The framework's context-loading list
(`review.md:23-33`) tells the reviewer to load "Master HL — understand vision", with no statement of *which revision*
and no rule excluding the Phase HL or the TS as the measuring stick.

This reorders the three Phase C deliverables by load:

| Deliverable | HL's stated weight | Weight the evidence supports |
|---|---|---|
| Reference-set rule (part of deliverable 2 / DoD-19) | implicit, one clause | **highest** — it alone would have exposed TFW-49 Phase C |
| Forcing function (deliverable 2 / DoD-20) | one of three clauses | **high** — converts the rule from readable to enforced (G11) |
| North-star anchor (deliverable 1) | "the load-bearing piece" | **medium** — necessary for the *cross-task* case (drift that stays inside one HL's own words), not for the corpus failure |

The anchor still earns its place: it is the only defence against a task whose *own approved HL* is wrong for the
product, which is the class HL §3 calls the self-referential chain. But it is the piece that can degrade gracefully
(D3 Alt D), and the reference-set rule is the piece that cannot.

**This does not require an amendment.** DoD-17/18 mandate that the PV Index gain priority 0 and that `templates/HL.md`
gain a header field. A fallback chain satisfies both — the field exists and resolves; what changes is what happens when
a project has not designated one. Deliverable ordering inside an approved phase is a refinement under iter1 D2/D4:
it needs no §5/§6 change.

### E2: If the anchor is an HL, the anchor is a contract — and AFD's has already drifted

The trap nobody in this task has stated. TFW-53 freezes §1/§3/§4/§5/§6/§7 of an approved HL. D1 Alt B designates an
existing HL as the north star. Therefore under D1=B the north star **is** a set of frozen sections — and G3(a) shows
AFD's designated anchor grew from 10 to 14 principles after approval, with six items carrying post-hoc `(Added…)`
markers and §4 carrying two "scope additions" blocks, none of which passed through anything resembling an amendment log.

Three consequences:

1. **D1=B is not neutral with respect to D3.** Nominating an HL as north star silently promotes a *task* contract to
   *project* authority, with no gate at the promotion point. The nominated HL was approved as a task scope, never as a
   standing statement of product purpose.
2. **A north star that can be edited by the task that owns it is not above the task.** HL §3's whole argument is that
   the principle chain is self-referential because §7 is coordinator-authored. Nominating a coordinator-authored HL as
   the anchor moves the self-reference up one level; it does not break it.
3. **D1=A and D1=D do break it,** for a structural reason: the root `README.md` and `KNOWLEDGE.md` §0 are *project-level*
   artifacts outside any task's write scope, edited under different workflows (`tfw-docs`, `tfw-knowledge`) with their
   own gates. Locus is not a matter of taste — it determines whether the anchor is inside or outside the drift path.

If D1=B is nonetheless chosen (it is AFD's live practice and cheap to adopt), the honest form is *nominated-and-frozen*:
the nominated HL's §1 and §7 become project-frozen, and changing them is an amendment against the **project**, not
against the task. That is a mechanism this task has not scoped and would need one.

### E3: The payload question is admission criteria, not size

H13 asks how big the anchor should be and answers ~one page. G3(b) shows the harder half: AFD's §7 mixes
*AI-first* (north-star grade) with *GPS: dirty + filtered, Kalman filter* (implementation detail). Under D4 Alt A the
reviewer must quote *a* clause the work serves — and a list containing implementation detail lets every piece of work
find a true, citable, entirely non-purposive clause. The forcing function then produces valid citations forever and
blocks nothing. **A size cap does not fix this; an admission test does.**

The workable admission test, derived from the corpus rather than invented:

> A north-star clause states something the product **is for** or **must never become**. If a clause could be satisfied or
> violated by a single task's implementation choice, it is a principle, not a north star — it belongs in HL §7.

Applied to AFD's 14: P1 (AI-first), P3 (единый стек), P7 (single screen), P8 (data-driven ads) pass; P11 (legacy
applicationId), P13 (bus-stop determinism), P14 (Kalman filter) fail — they are task-scoped decisions that reached the
anchor because the anchor is a task HL (E2). Roughly 4–6 of 14 survive, which is close to H13's one-page estimate by an
independent route.

This also supplies the missing payload element from G13: **non-goals**. The corpus failure mode is not "built something
opposed to the purpose" — it is "built an adjacent thing nobody excluded". TFW-49 Phase C did not contradict
*provenance, not decoration*; it **exceeded** it. A purpose statement alone cannot catch excess; a purpose statement
plus "what this is not" can. D2 Alt C is the only payload that carries the corpus's actual failure mode.

### E4: The forcing function's cost is one line per review; its yield is the whole check

H11 asks whether the citation requirement is what separates a live check from a rubber stamp. The measurable frame:

| | Without forcing function (D4 Alt C) | With forcing function (D4 Alt A/D) |
|---|---|---|
| Reviewer output per review | one ✅ and a free-text sentence | one quoted clause + resolvable path (+ harm, under Alt D) |
| Marginal cost | ~0 | one lookup, one line |
| What a dishonest/lazy pass looks like | *"Aligned with project goals."* — indistinguishable from a real pass | a quote that must exist in a specific file, and must be *about* the work |
| Detectable by a later reader? | No | Yes — the citation resolves or it does not (D43's exact mechanism) |
| External precedent | — | ISA 240: relate the matter to the **specific circumstances of the entity**; PCAOB: bare sign-off is a documented deficiency (G11) |
| Internal precedent | — | D43 Knowledge Citations, adopted because *"an agent says 'per D28' without a link — could be hallucinated"* |

The asymmetry is the argument. The cost is bounded and constant; the failure it prevents is the one that consumed
27,103 lines. And unlike a prose exhortation, a missing or unresolvable citation is **mechanically detectable by the next
role in the chain** — the same property that made D43 work and made D46's un-shipped "not rubber stamp" clause
undetectably absent for four months (G7).

Counter-consideration, recorded honestly: the forcing function cannot detect a citation that resolves but is
*irrelevant* — quoting P14 Kalman filter for a work item about advertising. That is a semantic failure a link check
cannot catch, and it is exactly why E3's admission criteria and D4 Alt D (quote **+ the concrete harm**) matter. The
citation makes laziness visible; the harm clause makes it costly.

### E5: Verdict class — the board already needs the distinction, and A5 already constrains the answer

Four positions, evaluated against three fixed constraints: (i) A5/iter1-D11 redefined `❌ REJECT` branch (a) as *file an
amendment*; (ii) Phase E introduces `❌ REJECTED` as a **terminal task status**, distinct from the review verdict; (iii)
D28 says the naming does the work.

| Alt | What it produces | Interaction with the constraints |
|---|---|---|
| **A** reuse `❌ REJECT`, grounds in prose | Nothing on the board distinguishes "built wrong" from "built the wrong thing" | Cheapest. But the grounds live in prose — the exact "reconstruct it from the prose" burden that A2 rejected for §12's `Type` column, five weeks ago, in this task |
| **B** new verdict token | A fourth verdict alongside APPROVE / REVISE / REJECT | Collides on two fronts: `review.md` §5, `REVIEW.md` §4, `conventions.md` §5 and the board legend all enumerate three; and Phase E is simultaneously adding `❌ REJECTED` as a *status*. Two new `❌` tokens in one release is the D17 confusion pattern |
| **C** tiered inside existing tokens | goal-`REVISE` (fixable in place) vs goal-`REJECT` (wrong thing built) | Honest about severity — not every purpose failure is fatal; AFD's corpus is 26 REVISE to 1 REJECT (G8). But two new compound tokens, and the tier boundary is a judgement call with no crisp test |
| **D** reuse `❌ REJECT` + a **named finding class** + mandatory owner routing | The verdict vocabulary is unchanged; the *finding* carries the name and the routing | Satisfies the board's need without touching the verdict enumeration; the name lands where A2 put the amendment `Type` — in a column, not in prose. DoD-22 already requires the owner routing, so this is the shape the DoD implies |

Alt D and Alt C are both live; Alt B is the one the corpus argues against. Note that DoD-22 is already written as *"a
goal failure is defined as sufficient grounds for `❌ REJECT`… and that verdict routes to the owner"* — i.e. the frozen
DoD **already chose reuse over a new token**. Alt B would need an amendment; Alt A, C and D would not.

Naming the finding class, against G9's corpus and G10's standard:

| Candidate | Provenance | Reads correctly outside software? | Collision |
|---|---|---|---|
| `Validation failure` | IEEE 1012 — *"was the right system built?"* | Yes, standards-backed | **Heavy** — `verify.md`, "validator", schema/form validation; TFW-49's linter was called "the validator" |
| `Not fit for purpose` | UK gate-review + contract law | Yes — the term is domain-general by origin | None in `.tfw/` |
| `Goal failure` | HL §10's own wording | Yes | None, but "goal" is generic enough to blur into DoD |
| `Purpose failure` | derived | Yes | None; pairs with "quality failure" as the orthogonal axis |
| `Declared outcome not achieved` | AFD-52/B2 verbatim, de-domained | Yes | None; long |
| `Hotfix, not investment` | AFD-38/B verbatim | **No** — software-specific; F13 violation | — |
| `Decoration, not delivery` | AFD idiom + **TFW-49's own approved §1** | Yes, and it is already TFW's own phrasing | None; evocative but not a category name |

The pair that survives both tests is **purpose / fit for purpose**: `not fit for purpose` names the finding, and the
IEEE pair supplies the underlying axis vocabulary (`verification` is already what `verify.md` does; the new half is
*validation* as a concept, without adopting the collision-heavy word as a label).

### E6: The namespace scheme has to solve a citation problem, not a tidiness problem

DoD-24 says project-level principles must not reuse HL §7's `P{n}`. G6 shows why in operational terms: the owner's own
directive cites `P8` in a way that is correct in one of three live namespaces. Under D4 Alt A, every review will now
produce a principle citation — so the collision rate goes from "occasionally confusing" to "once per review".

The minimum scheme that solves it, given that a citation must resolve without context:

| Layer | Prefix | Owner | Frozen? |
|---|---|---|---|
| Project north star clauses | `NS{n}` | project (README / KNOWLEDGE §0) | project-level, outside task write scope |
| Project principles (`KNOWLEDGE.md` §0) | `PP{n}` | `tfw-knowledge` | — |
| Task HL principles | `P{n}` (unchanged) | task coordinator | frozen on approval |

The important property is not the letters; it is that **a citation carries its layer**. `NS3` cannot be mistaken for
`P3`, and a reviewer quoting `NS3` has demonstrably reached above the task. `P{n}` stays as-is because renaming it would
touch every existing HL and TS §3 Principles Check in both projects — cost with no benefit, since ambiguity only exists
where two layers share a shape.

### E7: The corpus contains a mechanically detectable tell, and no check looks for it

G5's sharpest detail: the signal was in the TS. *"AFD-37 позже подхватит его в единый реестр"* — the spec itself recorded
that the proper home for the change was elsewhere and later. The reviewer read it, noted it, and rationalised it.

The same shape appears in the TFW corpus. TFW-49 Phase A's REVIEW Map: *"stops before Phase B routing and Phase C
hook/config installation"*; Phase B's: *"preserves … every Phase C hook/config/migration/cross-agent boundary"*. These
are boundary statements, which are legitimate. The tell is narrower and distinguishable:

> **Deferral confession** — the specification or the result states that the *correct* home, form or owner of a change is
> somewhere else, and ships the change here anyway. Distinguish from a *boundary statement*, which says this phase does
> not do X because another phase will do X **as its own declared outcome**.

A deferral confession is a purpose failure written down in advance by the party committing it. It is cheap to look for
(the reviewer already reads the TS and RF end to end) and it is the only trigger in the corpus that fired *before* the
damage rather than after. Whether it becomes a named check row or a clause inside the goal check is a drafting decision;
that it should be looked for is supported by the only two goal failures in either project that were caught at all.

### E8: The salami residual (open thread f3) costs one command, and the corpus says it would have fired

Iteration 1 conceded that twelve individually defensible deliverable refinements can sum to a new phase without reaching
§12. The proposed test: `git diff` against the freeze baseline at the pre-TS gate.

Cost, measured concretely: the baseline is recoverable by `git log --grep='/freeze/'` (iter1 D6), so the check is
`git diff $(git log --grep="/TFW-NN/freeze/" -1 --format=%H) -- <HL path>` — one command, one existing gate, no new
artifact, no new file, and the output is already in the reviewer's and coordinator's native format.

Would it have fired? On TFW-49 the drift commit `642c647` is `+167/−117` against `9e19a4f` — a diff no reader could
mistake for refinement. On TFW-48 it could not have fired, because the pre-amendment HL was never committed — which is
precisely the hole DoD-5 already closes. So the mechanism is complementary to what is already approved rather than
additive: DoD-5 makes the baseline exist, and this makes something read it.

This sits in Phase A/B territory, not Phase C, and it is a coordinator-side gate rather than a reviewer-side one.
Recording it as a costed recommendation for TS time, per iteration 1's own framing of the thread.

### E9: PV priority 1 is a defect this task discovered, not one it was scoped to fix

G2 establishes that priority 1 cites a section that is byte-identical in every TFW project. DoD-17 adds **priority 0**.
Two possible responses:

| Response | Effect on the index | Scope |
|---|---|---|
| Add priority 0 only (DoD-17 as written) | 8 sources; priority 0 = project purpose; priority 1 still says "README Values" and still resolves to `.tfw/README.md` | Inside DoD-17 |
| Add priority 0 **and** relabel priority 1 | Priority 1 becomes explicitly `.tfw/README.md § Values and Principles` — *methodology* values — removing the ambiguity that made the owner ask the question (S26) | One label change in `glossary.md`; DoD-17 already touches this table |

The second is a one-row edit to a table DoD-17 already requires editing, and leaving it undone ships a table where
priority 0 says "project purpose: root README" and priority 1 says "README Values" pointing elsewhere — an invitation to
exactly the confusion this iteration resolved. It is a refinement of an approved deliverable, not a new one, and needs
no amendment. But it is a *discovered* defect rather than a scoped one, and the coordinator should rule on whether it
travels with TFW-53 or gets its own entry — see RES Open Questions.

---

## Checkpoint

| Found | Remaining |
|-------|-----------|
| E1 — the reference-set rule outranks the anchor artifact by evidence; deliverable reordering is a refinement, not an amendment | Whether the coordinator accepts a re-weighting of a §4 prose claim without escalation |
| E2 — designating an HL as north star imports the drift problem one level up; AFD's anchor grew 10→14 principles unlogged | Whether *nominated-and-frozen* is worth scoping or whether D1=A/D sidesteps it |
| E3 — the payload problem is admission criteria + non-goals, not size; ~4–6 of AFD's 14 principles are north-star grade | — |
| E4 — forcing function: bounded constant cost, mechanically detectable failure; cannot catch an irrelevant-but-resolving citation | Test the "resolves but irrelevant" hole in Challenge |
| E5 — DoD-22 already chose verdict reuse; `not fit for purpose` survives de-domaining, `validation` collides | Final naming stress test in Challenge |
| E6 — `NS{n}` / `PP{n}` / `P{n}`; a citation must carry its layer | — |
| E7 — the *deferral confession* is a mechanically detectable tell present in both corpora | Whether it is a check row or a clause |
| E8 — salami check costs one command; would have fired on TFW-49, could not have on TFW-48 (DoD-5 closes that half) | Coordinator decision at Phase A/B TS time |
| E9 — PV priority 1 relabel is a one-row refinement of a table DoD-17 already edits | Coordinator ruling on scope travel |

**Sufficiency:**
- [x] External source used? — IEEE 1012 and the audit-standard anti-boilerplate requirement are load-bearing in E4/E5; CCB tiering underpins E5's severity discussion.
- [x] Briefing gap closed? — H11's mechanism is now costed (E4) rather than asserted; H13 is answered on both size and admission (E3); the verdict-vocabulary question has a shortlist with elimination reasons (E5).
- [x] Configuration Space built from Gather dimensions? — 11 configurations across all 7 dimensions, including two real-world controls.

**Mode-specific (deep):**
- [x] Hypothesis tested? — H11 (cost/yield model, with its stated blind spot), H13 (admission criteria, independent route to the same size).
- [x] Counter-evidence sought? — E1 is counter-evidence against the HL's own weighting of its Phase C deliverables; E2 against the cheapest locus; E4 names the hole the forcing function cannot cover; E5 records that the most standards-backed term is the one that collides worst.

**Metacognitive check.** Genuinely new: **E2** (the anchor-as-contract trap — no artifact in this task had noticed that
designating an HL promotes a task contract to project authority with no gate) and **E3** (admission criteria; the whole
task had been treating payload as a size question, and size is the easy half). **E7** re-frames an existing observation
into something checkable. **E1** is the uncomfortable one: it contradicts a weighting written in the frozen HL's §4
prose, and the honest reading is that the anchor is necessary but not the piece that would have saved TFW-49. What I did
*not* discover: any configuration that removes the need for a materiality bar — every path that blocks on purpose can
block on wording, and nothing in either corpus suggests otherwise.

Stage complete: YES
→ User decision: autonomous run — self-checkpoint passed, proceeding to Challenge.
