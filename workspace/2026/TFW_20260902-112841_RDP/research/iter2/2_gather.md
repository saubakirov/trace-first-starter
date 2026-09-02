# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260902-112841_RDP](../../HL-TFW_20260902-112841_RDP.md)
> Goal: Every finding a review produces becomes a decision by rule — one criterion, one named decider, one termination.

## Sampling Method (declared, per the briefing's hard boundary)

Three threads, three populations, each stated. Iteration 1's D2 holds: open a complete small population
rather than sample a large one badly.

| Pass | Population | Selection | Files opened |
|---|---|---|---|
| 1 — the replay | AFD-48 `phase-a`'s rung-2 chain and the surface where the same reviewer's rung-2 items **were** discharged | rev2 (the finding's origin), the artifact that carried it, the TS it landed in, and both rounds after | 5 |
| 2 — thread 4 | the deep rounds counted and not classified | **all of them** — and re-counting first found more than iteration 1 knew about (G1) | 5 |
| 3 — H3's candidate sites | the canon text this task edits | `review.md` Steps 4–6, `conventions.md` §5 · §15 · task control files, `templates/journal/event.md` | 4 |

**14 files opened**, within the soft limit of 15. Sibling trees were read with `find`, `grep -n`, `sed -n`
and `wc` only; nothing outside this task directory was created, modified, moved or deleted.

External sources: four sibling repositories (as iteration 1), plus two web searches on the rubber-stamp
question, which is the one question in this iteration where **this project has no corpus of its own** —
3.3 % of 331 reviews name a decider at all, and the coordinator's disposition act does not exist yet.

---

## Dimensions

Iteration 1 decomposed the *problem*. This iteration decomposes the *mechanism*, and every alternative
below is one a real corpus actually chose.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| **D1 — Where a rung-2 item is delivered** | the reviewer's `items to fix` list — a list only the executor reads (status quo) | `lifecycle: TS_DRAFT` — the applied A3 route | **an artifact addressed to the coordinator** — AFD's `PROPOSAL` | **a new surface with its own TS** — INNO-9's `phase-a-rev8` |
| **D2 — What records the coordinator's act** | a verdict or signature line | **a disposition cell citing the clause** — A5's site | **a round-labelled section appended to the TS** — AFD's `## 11. [rev5]` | a journal event — but the `kind` vocabulary is closed (G7) |
| **D3 — What bounds the return round** | nothing — `helpdesk` HD-23 returned 15 items against 1 ordered | the reviewer's item list | **a coordinator's closing checklist naming what is excluded** — AFD's §11.6 | the TS diff |
| **D4 — Who classifies the rung** | the reviewer, at verdict — what deliverable 3 assumes | **the executor, on receipt** — what AFD actually did | the coordinator, at close | nobody — the status quo in 96.7 % of the corpus |
| **D5 — What makes a ruling checkable** | that it exists | it names a **consequence specific to the item** | it **cites the clause** that forbids paying | it names **what the next round may not reopen** |

Do NOT mark any alternative as recommended — all remain open until Challenge.

---

## Findings

### G1: The deep-round population is **11**, not 7 — and the miscount has a cause the design must care about

Iteration 1's D3 says re-run every number before building on it. Applied to iteration 1's own number:

```bash
for p in steps-framework ai-first-devices helpdesk innoforce-ai-first kaznpu-ai-lab; do
  find /d/projects/research/$p -type f -name 'REVIEW*' \
    -not -path '*/.tfw/*' -not -path '*/.claude/*' -not -path '*/.agents/*'
done | grep -cE 'rev[3-9]'          # → 11
```

| Corpus | iteration 1 reported | measured now | The three that were invisible |
|---|---:|---:|---|
| this repository | 3 | **4** | `ASSISTED15__rev3` was listed in G4's table but counted in the *phase* column, not the corpus total |
| `ai-first-devices` | 4 | **4** | ✅ unchanged |
| `innoforce-ai-first` | **0** | **3** | `REVIEW__phase-b-rev5__…` · `REVIEW__phase-b-rev5-rev1__…` · `REVIEW__phase-a-rev8__…` |
| `helpdesk` · `kaznpu-ai-lab` | 0 | 0 | ✅ unchanged |
| **total** | 7 | **11** | |

**The cause is not arithmetic.** Iteration 1 matched a **trailing** `__rev3` on the basename. In
`innoforce-ai-first` the round marker sits **inside** the surface name — `phase-a-rev8`,
`phase-b-rev5-rev1` — so a grep looking for the round at the end cannot see it. That is the same class of
error iteration 1 corrected in the HL (a grep matching directory names), inverted: **a grep that assumes
where the round marker lives.**

⚠️ And the assumption is not the researcher's. **HL §10's own answer to *"Why not count rounds in a
control file?"* is: *"The round is already visible in the artifact names — `rev2`, `rev3` — and that is
the structural home."*** G2 is what happens to that structural home in practice.

### G2: A revision wearing a phase name — INNO-9 ran **nine** revisions and was reviewed **three** times

`tasks/INNO-9__ceo_transformation_plan_2026h2/phase-a/`, listed in full:

```text
  ONB__phase-a__plan_content.md              TS__phase-a__plan_content.md        RF__phase-a__…      REVIEW__phase-a__plan_content.md
  ONB__phase-a-rev1-rev2__…                  TS__phase-a-rev1__academic_russian.md
                                             TS__phase-a-rev2__visuals_and_governance.md
  ONB__phase-a-rev3__…                        (no TS)                            RF__phase-a-rev3__…
  ONB__phase-a-rev4__…                       TS__phase-a-rev4__…                 RF__phase-a-rev4__…
  ONB__phase-a-rev5__…                       TS__phase-a-rev5__…                 RF__phase-a-rev5__…
  ONB__phase-a-rev6__…                       TS__phase-a-rev6__…                 RF__phase-a-rev6__…
  ONB__phase-a-rev7__…                       TS__phase-a-rev7__…                 RF__phase-a-rev7__…   REVIEW__phase-a-rev1-7__consistency_and_language.md   🔄 REVISE
  ONB__phase-a-rev8__…                       TS__phase-a-rev8__…                 RF__phase-a-rev8__…   REVIEW__phase-a-rev8__terminology_and_language.md      ✅ APPROVE
  ONB__phase-a-rev9__…                       TS__phase-a-rev9__…                 RF__phase-a-rev9__…    (no REVIEW)
```

| Count | Value |
|---|---:|
| Revisions of the same deliverable pair (`plan_content.md`, `org_structure.md`) | **9** |
| `ONB` files | 9 · **`TS` files** 8 · **`RF` files** 9 |
| `REVIEW` files | **3** |
| Revisions that reached a verdict of their own | **2** (rev1-7 consolidated, rev8) |

`REVIEW__phase-a-rev1-7` reviews **seven revisions in one file**, judging *"the **final state** of the two
CEO-facing deliverables"*, and its verdict is 🔄 REVISE with a six-item list. `rev8` closes that list and
approves. `rev9` has an ONB, a TS and an RF and **no review at all**.

**Why this is a finding about the contract and not about that project.** Every one of those revisions is a
repair of what was already specified — a `revision` under deliverable 5's own definition. And each was
given **its own TS**, which under deliverable 5's second sentence reclassifies it as *new work*. So:

```text
  Deliverable 5:  "Work that cannot be accepted under the existing TS is new work and takes a new TS."
  Deliverable 6:  a round that returns an item the previous round already ordered is the terminating round.
                                        │
                                        ▼
        a new TS  ⇒  no "previous round" on this specification  ⇒  the trigger has nothing to compare
                                        │
                                        ▼
        INNO-9 phase-a:  9 revisions · 0 terminating rounds fired · the practice is not even irregular —
        it is what deliverable 5, read literally, instructs
```

Neither the round count (HL's *"structural home"*) nor A2's unchanged-item trigger can fire across a TS
boundary. **The cheapest escape from the termination rule is to call the fix new work**, and it is an
escape the canon currently *recommends*. HL §10 H5 suspected exactly this for `ai-first-devices` —
*"18 numbered sub-phases of which an unknown share are revision rounds wearing a phase name"* — and it was
never tested. `innoforce-ai-first` is the clean case because the name says `rev8` out loud.

### G3: The natural experiment — one task, one reviewer, one week, two rung-2 items, two different endings

AFD-48 is a controlled comparison and nobody set it up as one. Same task, same reviewer (Codex), same
TFW 0.9.0, 2026-07-30 to 2026-08-03.

| | `phase-a` | `phase-b` · S3 Block 1 |
|---|---|---|
| Reviewer's rung-2 items | rev2 §4 item 3 — *"Obtain coordinator amendments… An executor statement that the change is unavoidable is not an amendment"*; and item 5 — *"no executor-authored contract decisions"* | rev1's four items, of which two the executor judged to need a decision |
| Where they were written | `### Items to fix` — **a list only the executor reads** | the same list |
| What happened next | the executor could not discharge them; **the same item returned in rev3 and rev4, verbatim in substance** | the executor wrote **`PROPOSAL__phase-b-s3-block1__revise_closure.md`**, 2 137 words, *«Адресовано: Coordinator — решение о способе закрытия»* |
| Coordinator's act | **none logged.** `grep -rilE 'amendment log|§12'` over the task → `phase-b` only, never `phase-a` | **`TS__phase-b-s3` §10 and §11**, authored by the coordinator, dated, round-labelled |
| Rounds | rev1 · rev2 · rev3 · **rev4**, still 🔄 REVISE at the end of the trail | rev1 · rev2 · **rev3 ✅ APPROVE** |

```text
  SAME REVIEWER, SAME TASK, SAME WEEK

  phase-a          rung-2 item ──► "items to fix" ──► executor ──► cannot amend a TS
                                          ▲                              │
                                          └──────────────────────────────┘
                                              rev2 · rev3 · rev4  (still open)

  phase-b/S3       rung-2 item ──► "items to fix" ──► executor ──► PROPOSAL to coordinator
                                                                        │
                                                                        ▼
                                                        coordinator writes TS §10, §11
                                                                        │
                                                                        ▼
                                                              rev3  ✅ APPROVE
```

**The variable is not the finding's difficulty and not the reviewer.** It is whether anything carried the
item to someone who could discharge it. That is §2.9 confirmed by a within-task control, which iteration 1
established from a single arm.

### G4: What the landing site looked like when it was used — a round-labelled section appended to the TS

`TS__phase-b-s3__honest_off_trip_contract.md` section headers, tail:

```text
  ## 8.  Knowledge Citations
  ## 9.  [rev3] Контракт ревизии Блока 1 (coordinator, 2026-08-03)
  ## 10. [rev4] Решение владельца: «почему который раз одно и то же» — матрица полос записи
  ## 11. [rev5] Ответ на REVIEW rev2 — гейт, который я добавил, повторил ошибку Phase A
  ### 11.4 🔧 Решение по скоупу: гейт делится, и это исправление МОЕЙ ошибки процесса
  ### 11.5 Контракт принуждения полноты (для S4a, пишу заранее)
  ### 11.7 [rev6] BusStopStatusChanged вне рейса — проверенный ОТРИЦАТЕЛЬНЫЙ ответ, работы нет
  ### 11.6 Закрывающий чек-лист — ровно это и ничего больше
```

Four properties of that site, each of which the design needs and none of which required a new artifact:

| Property | Evidence, verbatim |
|---|---|
| **Round-labelled and append-only** — the TS grows a section per round and no earlier section is rewritten | `[rev3]` `[rev4]` `[rev5]` `[rev6]` in the headers themselves |
| **Per-item ruling with the authority named** | *«**R1 → A** · **R2 → A** · **R3** механика · **R4 → A** (чинить пробу; 8 строк в чужом тесте **разрешаю явно — это моё решение как автора AC-9**, §9.5) · **R5 → B с падением в A**»* |
| **The scope decision announced rather than taken quietly** | *«Дополнительный AC из §10.4 в Блоке 1 **сужается** до честной матрицы. **Это решение координатора, объявленное вслух, а не тихое снятие требования**»* |
| **The return round bounded, in both directions** | §11.6 *«Закрывающий чек-лист — **ровно это и ничего больше**»*, five numbered items, then a `⛔ Не делать` list, then *«**Ревьюеру — три факта, чтобы не было третьего круга**»* |

And the next round's REVIEW confirms the bound held: rev3 §1 — *«TS §11 принят как владеющий контракт…
**Rev3 проверена по пяти конкретным пунктам координатора**»*, verdict ✅ APPROVE.

⚠️ **The one thing the site did not do.** `AFD-48` has **no `status.md` and no `journal/`** anywhere in the
task — `find … -name 'status.md' -o -name journal` returns nothing. TFW 0.9.0 had neither. So this corpus
demonstrates the **landing site** and says nothing about the **lifecycle move** A3 specifies; the two are
separable, and iteration 1's proposal fused them.

### G5: The coordinator's act was not a stamp — and what made it not one is measurable

The `PROPOSAL` arrived as a menu, not an assertion. Its structure, counted:

| Element | Present |
|---|---|
| A per-item table with a **`Решение нужно?`** column | ✅ 6 items, 3 marked *да* |
| Named alternatives per decision, each with **cost** and **risk** | ✅ R1 four variants (A/B/C/D), R2 two, R4 three, R5 two |
| A recommendation, with the reasoning attached | ✅ each |
| An explicit list of questions to the decider | ✅ §9, five numbered |
| A list of what the author is **not** proposing, and why | ✅ §8, five rows |
| A retraction of the author's own earlier proposal | ✅ *«Бисекция… Я предлагал это в первой версии плана — снимаю»* |

And the coordinator's replies **reversed the coordinator's own prior instructions, twice, in writing**:

> §10.3 — *«⛔ **Бисекция батча отменяется** (мой §9.2 предлагал её как альтернативу)… **Исполнитель прав**.»*
>
> §11.4 — *«Я сам сказал владельцу: ⛔ не расширять стадию, находящуюся под ревизией… **И в rev4 сделал
> именно это**… **Второй REVISE вызван моим добавлением, а не работой исполнителя. Исправляю.**»*

A signature cannot do that. **A decision that arrives as a choice among named alternatives forces the
decider to name one**, and naming one is visible; naming one that contradicts your own earlier text is
visible as reasoning. This is `philosophy` F25 — *«Фреймворк предлагает — человек выбирает»* — observed
producing the anti-rubber-stamp property, in a corpus that never stated the rule.

### G6: The reviewer already has somewhere to say *"this one is not mine"* — and it is not a route

`AFD-48 phase-a` rev2 §6 Traces Updated:

```text
  - [x] REVIEW rev2 and map/verify/judge rev2 created
  - [x] README Task Board marked 🔄 REVISE rev2
  - [ ] HL/TS history — coordinator-owned fix required        ← an unchecked box, correctly attributed
  - [ ] tfw-docs — deferred until APPROVE
  - [ ] tfw-knowledge — deferred until APPROVE; FC6 requires correction
```

The reviewer identified the owner of the fix and wrote it into a **checklist about their own trace
updates**. It is the closest thing to a rung-2 declaration the templates offer, and it went nowhere across
three rounds. **An unchecked box addressed to nobody is the same failure as an item in a list only the
executor reads** — §2.9's shape, in a second location, which deliverable 3 does not currently name.

### G7: The journal `kind` vocabulary is **closed**, which shuts one of H3's four doors

`templates/journal/event.md` and `conventions.md` (task control files) state it twice:

| kind | Records |
|---|---|
| `created` | the task came into existence |
| `dispatch` | work was handed to a named participant |
| `handoff` | a role boundary was crossed |
| `transition` | lifecycle changed, blockage and resumption included |
| `ownership_changed` | the `owner` field in `status.md` changed |
| `amendment_escalated` | a frozen-section change was filed for an owner verdict |
| `consolidation` | **RESERVED — not valid yet** |

> *"SOME ARTIFACTS LEGITIMATELY HAVE NO EVENT, and that is how the vocabulary stays closed. An artifact no
> `kind` covers is filed without one, and no kind is invented for it."*
> *"A closed vocabulary that opens at the first inconvenience was never closed."*

**Consequence for H3:** a `disposition_ruled` kind is a new entity by the canon's own construction, so
DoF 1 forbids it and the honest reading is that the journal is **not** H3's site.

**Consequence for A3, in the opposite direction:** both kinds the ladder needs already exist and are in
live use — this very task wrote `20260902-123244__amendment_escalated__9cc4.md` four minutes before this
iteration began. Rung 3 has its event. Rung 2 has `transition`, whose own definition covers a lifecycle
change to `TS_DRAFT` without amendment.

### G8: `review.md` has no step in which the coordinator acts, and the reviewer currently does two things §15 does not grant

Measured 2026-09-02, re-running iteration 1's command:

```bash
awk '/^## Step 4/{f=1} f&&/^## Step 7/{exit} f' .tfw/workflows/review.md | wc -w   # → 483
```

| Step | Words | Who acts, per the text as it stands |
|---|---:|---|
| Step 4 Decide | 109 | reviewer — writes the verdict; `Routing` names the **owner** for two cases and the executor for none |
| Step 5 Debt | 289 | **reviewer** — *"Dispose of every item before the verdict"*. This is the authority §2.7 says was never granted |
| Step 6 Traces | 63 | **reviewer** — *"Set the task's own state — `lifecycle` in `{task}/status.md` … with a `transition` event"* |

`conventions.md` §15 grants `review.md` exactly: *"review stage files (map.md, verify.md, judge.md),
REVIEW"*, and forbids *"ONB, RF, HL, TS, code"*.

| The reviewer does | §15 grants it | Note |
|---|---|---|
| write REVIEW, stage files | ✅ | |
| **rule dispositions** (Step 5.4) | ❌ | §2.7 — the defect this task fixes |
| **write `status.md`** (Step 6.1) | ❌ silent — neither granted nor forbidden | not in either column of the role table |
| **write a journal event** (Step 6.1) | ❌ silent | same |

**Two observations, and only the first is this task's business.** The disposition grant is deliverable 4.
The `status.md` and journal grant is a *second* unnamed grant in the same three steps — and DoF 8 forbids
rewriting what this task does not touch, while Step 6 **is** a section this task touches. Flagged, not
resolved, in Extract.

### G9: External — why an approval body rubber-stamps, and the one test used elsewhere to tell a real refusal from a formality

Two searches; this is the only question in the iteration with no local corpus.

**Why boards approve everything.** The diagnosis in the change-management literature is not a character
failure, it is an input failure: the board approves everything because **declining requires a rationale
nobody wrote down**, and requests **arrive without impact assessments, so the board has no basis for
refusal** ([Onplana](https://onplana.com/blog/change-control-board-that-works),
[monday.com](https://monday.com/blog/teamwork/change-advisory-board/)). The prescribed corrections are
(a) every decision recorded **with its rationale and its conditions**, as an audit trail that later
requests are judged against, and (b) **separation of duties — the requester and the approver are different
people** ([ISO 27001 walkthrough](https://www.konfirmity.com/blog/iso-27001-change-management),
[PDCA](https://pdcaconsulting.com/cab-best-practices-implementation/)). Financial regulators name the
missing property directly and call it **effective challenge** — a board that cannot show it challenged is
treated as not having decided
([FCA, via RWA](https://insight.rwabusiness.com/blog/posts/2024/december/boards-should-not-act-as-rubber-stamp-of-approval-effective-challenge-vital-to-consumer-duty-board-reports-according-to-fca/)).

**This converges exactly on G3 and G5, from outside the project.** `phase-a`'s rung-2 item arrived as an
assertion addressed to nobody who could act → no decision. `phase-b`'s arrived as an impact assessment
with named alternatives and costs, addressed to the decider → a decision, twice reversing the decider's
own prior text. And separation of duties is already this project's `KNOWLEDGE.md` D13.

**Counter-evidence, sought because `deep` requires it, and it is strong.** A mandatory written
justification degrades into boilerplate. The best-documented case is discovery objections: courts hold
that boilerplate objections *"lack sufficient information to allow the court to evaluate the merits"*, that
rote terms become *"a ritualized legal incantation… emptied of recoverable meaning"*, and that they are
**not valid objections and are sanctionable** ([ABA](https://www.americanbar.org/groups/litigation/resources/newsletters/pretrial-practice-discovery/beware-boilerplate-reasonable-inquiry-required-discovery-responses-objections/),
[Baker Sterchi](https://www.bakersterchi.com/federal-judges-blow-their-stacks-over-boilerplate-objections)).

⚠️ **The test that survives that objection is not "a reason was written" but "the reason carries enough
information to be evaluated" — and it is enforced by a consequence.** Mapped onto this contract: a
disposition that names a consequence *specific to this item* is evaluable; *"low priority"* and *"purpose
is damaged"* are incantations. DoF 3 is this project's sanction, and A4 is the amendment that already
separated the evaluable half from the incantation.

---

## Checkpoint

| Found | Remaining |
|-------|-----------|
| The deep-round population is **11**, not 7 — three files in `innoforce-ai-first` carry the round marker mid-basename | Nothing: the population is now closed by measurement, and the two files thread 4 named are classified in Extract |
| **INNO-9 ran 9 revisions and 3 reviews**, each revision with its own TS. Neither a round cap nor A2's trigger can fire across a TS boundary — and deliverable 5, read literally, instructs the split | Whether this is a defect in deliverable 5, in deliverable 6, or in their interaction — Extract |
| **A within-task control**: AFD-48 `phase-a` (rung-2 item to the executor's list → rev2·rev3·rev4, open) vs `phase-b/S3` (rung-2 item to the coordinator by artifact → rev3 APPROVE) | — |
| The site that worked is a **round-labelled append-only section in the TS**, carrying a per-item ruling with named authority, an announced scope decision, and a closing checklist addressed to executor **and reviewer** | AFD has no `status.md` and no `journal/` at all, so it evidences the **landing site** and not A3's **lifecycle move**. The two are separable |
| The coordinator's act resisted the stamp because the input was a **menu with costs**, not an assertion — and the rulings reversed the coordinator's own two prior instructions | Whether that property can be required structurally without becoming boilerplate — Challenge |
| The journal `kind` vocabulary is **closed** ⇒ a disposition event is a new entity ⇒ **not H3's site**. But `transition` and `amendment_escalated` already exist for rungs 2 and 3 | Which of the three surviving H3 candidates is checkable — Extract |
| `review.md` has **no step where the coordinator acts**, and Step 6 has the reviewer writing `status.md` and a journal event, which §15 neither grants nor forbids | Whether naming that second grant is in scope or is DoF 8 |
| External diagnosis converges: boards stamp because refusal needs a rationale nobody wrote and requests carry no impact assessment. Counter-evidence: mandated rationale becomes boilerplate unless the test is *evaluable*, with a sanction | — |

**Sufficiency:**
- [x] External source used? — four sibling repositories, read-only, plus two web searches on the one question with no local corpus
- [x] Briefing gap closed? — every Gather bullet answered; the corrected AFD-27 attribution is in G1
- [x] Dimensions identified? — five, and every alternative is one some corpus actually chose
- [x] Hypothesis tested? — H3's four candidate sites enumerated and one eliminated by the canon's own closed vocabulary (G7); H2's population closed (G1)
- [x] Counter-evidence sought? — G9's second search was run **against** the finding the first one supported, and it landed: mandated rationale becomes ritual unless the test is evaluability plus a consequence. Iteration 1's own count was also re-run and was wrong by four

**Metacognitive check.** New, and it moved a frozen deliverable's foundation. What I expected to find was
whether A3's route works. What I found is that **the route was already run, by hand, in another project,
and it worked** — and separately that **the termination rule this task is shipping has a free, canon-endorsed
escape hatch** (G2) that no hypothesis named and that HL §10 suspected in the wrong corpus. The second
finding is worth more than the first and was not on the coordinator's list.

Stage complete: YES
→ Gate written, not taken — owner instruction *«без вопросов ко мне»*, 2026-09-02
