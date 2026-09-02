# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260902-112841_RDP](../../HL-TFW_20260902-112841_RDP.md)
> Goal: Every finding a review produces becomes a decision by rule — one criterion, one named decider, one termination.

## Sampling Method (declared, per the briefing's hard boundary)

331 REVIEW files exist across five corpora. Reading all of them badly was refused. The sample was drawn
in three deliberate passes, each with its population stated:

| Pass | Population | Selection | Files opened |
|---|---|---|---|
| 1 — census | all 331 | none opened; `find` + `awk` extraction of the §4 verdict from every file | 0 |
| 2 — the loop | every REVIEW past round 2 in any corpus (**7 files**) | **all of them** — this is the cap's entire evidence base, and it is now 7, not 4 | 7 |
| 3 — the criterion | every disposition row ruled under the new gate (**9 rows, 2 files**) | **all of them** — the complete population, not a sample | 2 |

Plus 4 orientation files (`helpdesk` REVIEW template, three helpdesk RFs) and `review.md` itself.
**14 files opened.** Within the soft limit of 15.

Every count below was produced by a command run in this session. Commands are given so a reader can
re-run them; the exclusions (`--exclude-dir=.tfw .claude .agents`) matter, because the shipped REVIEW
template contains the words `APPROVE / REVISE / REJECT` and inflates every naive grep.

---

## Dimensions

The problem decomposes into five independent decision factors. None of them is settled by the frozen
contract; each is a real degree of freedom the design must choose a value for.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| **D1 — What ends the loop** | fixed round cap (2) | unchanged-item detector: an item that survives a round forces escalation | escalation-completion: the loop cannot continue while a rung-2/3 item is unrouted | nothing (status quo) |
| **D2 — Decider for ordered work** | always executor | ladder stated in prose | ladder with a structural delivery site — the routed item lands where the coordinator must act | always coordinator |
| **D3 — Disposition vocabulary** | three outcomes (status quo) | three + *material but not actionable* | three, each carrying a criterion mark | two (owed / not owed) + a routing column |
| **D4 — Where the criterion lives** | `review.md` Step 4 only | Step 4 + `conventions.md` §5 | a column in `templates/REVIEW.md` §5 | all three |
| **D5 — Budget granularity** | per section edited | across the Steps 4–6 group | whole file (≤1 200) | none |

Do NOT mark any alternative as recommended — all remain open until Challenge.

---

## Findings

### G1: The census — five corpora, one template lineage, five different behaviours

```bash
find $p -name 'REVIEW*' -type f -not -path '*/.tfw/*' -not -path '*/.claude/*' -not -path '*/.agents/*' \
| while read f; do awk '/^##[[:space:]]*4\.?[[:space:]]*(Verdict|Вердикт)/{flag=1;next} flag&&/^\*\*/{print;exit}' "$f" \
| grep -oiE 'APPROVE|REVISE|REJECT' | head -1; done | sort | uniq -c
```

| Corpus | TFW | REVIEW files | APPROVE | REVISE | REJECT | **REVISE rate** | rounds past 1 | rounds past 2 |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `helpdesk` | 2.0.0-dirty.5 | 70 | 65 | 3 | 0 | **4.4 %** | **0** | 0 |
| `ai-first-devices` | 0.9.0 | 149 | 123 | 22 | 1 | 15.0 % | 11 | 4 |
| this repository | 2.1.0 | 85 | 66 | 12 | 1 | 15.0 % | 9 | 3 |
| `innoforce-ai-first` | 2.0.0-dirty.4 | 17 | 7 | 5 | 1 | **35.7 %** | 8 | 0 |
| `kaznpu-ai-lab` | 2.0.0-dirty.4 | 10 | 7 | 3 | 0 | 27.3 % | **0** | 0 |
| **total** | | **331** | 268 | 45 | 3 | | 28 | **7** |

`KZ-IT-telegram-list` was measured and excluded: no `.tfw/`, 0 REVIEW files.

**Two HL numbers are corrected here, and both were false positives from task names, not review names.**
An HL-era grep for `rev[0-9]|_v[0-9]|round` matched `HD-16__user_feedback_v12` and
`AFD-18__payment_tablet_android_v1` on the **directory**. Restricted to the REVIEW basename:

| HL §2.2 / §10 says | Measured 2026-09-02 |
|---|---|
| `helpdesk`: **1** repeat round | **0** — no `helpdesk` REVIEW file carries a round marker |
| this repository: **85** REVIEW files | **85** ✅ confirmed |
| this repository: 8 surfaces ran a repeat round | **5** by filename (phase-a, phase-aa, phase-ab, ASSISTED15, TLD) |
| this repository: 3 surfaces past two rounds | **3** ✅ confirmed |
| `ai-first-devices`: 150 REVIEW files | **149** outside `.tfw/` |

### G2: The mechanism behind `helpdesk`'s low REVISE rate — its reviewers mark ❌ five times less often

```bash
grep -rh --include='REVIEW*' -oE '\|[[:space:]]*(❌|✅|⚪)[^|]*\|' $p --exclude-dir=.tfw … \
| grep -oE '❌|✅|⚪' | sort | uniq -c
```

| Corpus | ✅ | ❌ | ⚪ | marks per review | **❌ per review** |
|---|---:|---:|---:|---:|---:|
| `helpdesk` | 1 265 | 14 | 0 | 18.3 | **0.20** |
| `ai-first-devices` | 2 450 | 119 | 0 | 17.2 | 0.80 |
| this repository | 1 219 | 90 | 4 | 15.4 | **1.06** |

**Marks per review are near-identical (15–18) — so the templates produce comparable row volume and the
corpora are comparable on this axis.** What differs is the failure rate: `helpdesk` reviewers record a ❌
at **one-fifth** this repository's rate. The low REVISE count is downstream of that, not of a practice
that resolves findings before the verdict.

Whether that is easier work or a more lenient reviewer is **not determined by this measurement** and is
carried to Extract. The design consequence is the same either way and is stated in G3.

### G3: What actually happens to a `helpdesk` REVISE — three cases, three different endings, no second verdict

All three REVISE verdicts in `helpdesk` were opened and their phase folders listed.

| Case | What the REVISE ordered | What the RF shows now | Second REVIEW? |
|---|---|---|---|
| `HD-10` PhaseC2 | *"The fix required is documentation-only… No code changes needed"* — 3 RF edits | header still reads **🟢 RF — Awaiting review**; carries a *"§9 Addendum: Refresh Token Race Condition Fix (post-RF)"* about work **unrelated to any REVISE item** | ❌ none |
| `HD-11` PhaseC | 2 changes to `mkdocs.yml`, then re-run `--strict` | header reads *Complete*; **no addendum**; `git log` shows one authoring commit and then only the task-closing commit | ❌ none |
| `HD-23` PhaseB | **one** item, *"Изменение ≤ 10 строк"* — `per_page=50` on mobile mount | header reads *🟢 RF — Complete (REVISE fixes applied)*; a **`## REVISE Addendum (2026-04-22)`** lists **15 numbered items** — 9 fixes plus a bundled *"Phase D Cleanup"* of 6 more | ❌ none |

**`helpdesk` does not avoid the loop. It leaves the round unclosed.** Three REVISE verdicts, zero
re-reviews. In the one case where the executor returned, the return round delivered **15 items against
1 ordered** — and nobody reviewed the other 14. `HD-10`'s RF has said *"Awaiting review"* since 2026-04-16
in a task that has no `status.md` at all.

**This falsifies H6's useful branch and supplies something better.** There is no importable practice. There
is an unbounded return round, which is direct evidence for HL Deliverable 7's clause *"what the round is
bounded by"* — the clause the HL wrote on intuition and now has a case for.

**Third independent invention of RF-append.** HL §2.3 records TLD inventing *"append to the RF"* on
2026-08-30 and calls it *"invented twice, written down nowhere."* `HD-23`'s addendum is dated **2026-04-22**
— four months earlier, in another project, on another TFW version. It is the **earliest** of the three.

### G4: Every round past two, in every corpus — the cap's real evidence base is 7 files, not 4

HL §10 names four. Restricting to REVIEW basenames carrying `rev3`/`rev4` across all corpora finds
**seven**, and the three additional ones are the strongest cases.

| # | Corpus | Surface | Round | What that round ordered |
|---|---|---|---|---|
| 1 | this repo | TFW-60 `phase-a` | rev3 🔄 | **work** — *"Make participant validation fail closed and type-aware… require `on_behalf_of` to name a declared **human** handle"*; plus a naming sweep and an evidence rebuild |
| 2 | this repo | TFW-60 `phase-a` | rev4 ✅ | nothing — the terminating verdict |
| 3 | this repo | TFW-60 `phase-aa` | rev3 🔄→✅ | **record only** — *"all record-keeping and none in the engineering"*; owner overrode: *«отметить как апрув, эти мелочи править не будем»* |
| 4 | this repo | `ASSISTED15` | rev3 🔄 | **work** — *"D11 makes the real Windows lock/ACL path non-terminating"*, a hang; plus evidence truthfulness |
| 5 | `AFD` | AFD-48 `phase-a` | rev3 🔄 | **work** — *"a standard Gradle included build can re-open the exact production raw-collection class and still pass the promised structural gate"*; plus **an unexecuted coordinator escalation** |
| 6 | `AFD` | AFD-48 `phase-a` | rev4 🔄 | **work** — *"AC-6 remains falsified by an executable green counterexample"*; **the same coordinator escalation, still open** |
| 7 | `AFD` | AFD-48 `phase-b-s3-block1`, `phase-c1-block1` | rev3 🔄 | not opened — outside the sample; counted, not classified |

### G5: The unexecuted escalation — why AFD-48 reached round 4

The item *"Obtain coordinator amendments. Reviewer cannot self-amend TS"* appears in **rev2, rev3 and
rev4** of the same surface — three consecutive rounds, verbatim in substance:

| Round | Item text | Rung |
|---|---|---|
| rev2 §4 item 3 | *"Obtain coordinator amendments. Explicitly ratify `RegistryApiTest` 49→50 and record the semantic AC-5 change… An executor statement that the change is unavoidable is not an amendment."* | 2 — coordinator |
| rev3 §4 item 2 | *"Obtain coordinator amendments. The coordinator must explicitly rule on (a)… and (b)… RF §3.6 is a good decision request, but it is not approval."* | 2 — coordinator |
| rev4 §4 item 3 | *"Obtain coordinator amendments A and B… Reviewer cannot self-amend TS."* | 2 — coordinator |

```bash
grep -rilE 'amendment log|§12' tasks/AFD-48__device_bus_stall_hardening/   # → phase-b only, never phase-a
```

**No amendment was ever logged for `phase-a`.** The reviewer identified rung 2 of the ladder correctly and
three times, wrote it into a list addressed to the **executor**, and the executor — who may not amend a TS —
could not discharge it. The item was structurally undischargeable and survived every round.

**The loop went deep because an escalation was ordered and never delivered, not because no cap forbade a
third round.**

### G6: The ladder is rare, and it is largely this repository's habit

```bash
grep -rlE --include='REVIEW*' '(no (HL/TS|HL or TS|TS) (amendment|rework|change)|bounded correction|under the approved TS|requires? (an? )?(HL|TS) (amendment|rework|change)|routes? to the owner|coordinator must (explicitly )?rule|Reviewer cannot self-amend)' $p --exclude-dir=.tfw …
```

| Corpus | reviews naming a decider or rung | of | rate |
|---|---:|---:|---:|
| this repository | **7** | 85 | 8.2 % |
| `ai-first-devices` | 3 | 149 | 2.0 % |
| `kaznpu-ai-lab` | 1 | 10 | 10.0 % |
| `helpdesk` | **0** | 70 | 0 % |
| `innoforce-ai-first` | **0** | 17 | 0 % |
| **all** | **11** | **331** | **3.3 %** |

Seven of the eleven are in this repository. The three in `AFD` are the AFD-48 `phase-a` chain of G5 — the
one place the ladder was reached independently, and the one place it produced nothing.

### G7: `review.md` — the baseline DoD 10 names is wrong by 22 words

```bash
awk '/^## Step 4/{f=1} f&&/^## Step 7/{exit} f' .tfw/workflows/review.md | wc -w   # → 483
awk '/^## Anti-patterns/{f=1} f'               .tfw/workflows/review.md | wc -w   # → 163
```

| Section | HL DoD 10 says | Measured 2026-09-02 |
|---|---:|---:|
| Steps 4–6 | **461** | **483** (+22) |
| Anti-patterns | **161** | **163** (+2) |
| whole file | 1 706 | **1 706** ✅ |

Per step, which DoD 10's own wording (*"every section this task edits"*) makes the binding unit:

| Step | Words | What this task must add to it |
|---|---:|---|
| Step 4 Decide | **109** | criterion · routing ladder · revision definition · termination rule — **four of six mechanisms** |
| Step 5 Debt | **289** | authority move · prediction rule |
| Step 6 Traces | **63** | wording only |

### G8: `helpdesk`'s shipped REVIEW template still offers `→ backlog`

The 2.0.0 template in `helpdesk/.tfw/templates/REVIEW.md` §5 carries `| Action | … → backlog / → next phase |`.
`grep -c '→ *backlog'` over its REVIEW corpus: **131 occurrences**. This repository retired that channel at
2.1.0 and `conventions.md` §14 now names it an anti-pattern. Not this task's subject — recorded because it
bounds what `helpdesk` can be cited *for*: it is a pre-gate corpus, and its dispositions are not comparable
to TLD's nine.

---

## Checkpoint

| Found | Remaining |
|-------|-----------|
| `helpdesk` has **0** repeat rounds, not 1 — and 3 REVISE verdicts that never reached a second verdict. H6's useful branch is dead | Whether `helpdesk`'s 5× lower ❌ rate is easier work or a more lenient reviewer — undetermined |
| The ❌ rate, not a practice, explains the low REVISE rate: 0.20 vs 1.06 per review on comparable mark volume | — |
| The cap's evidence base is **7** files, not 4 — and 4 of the 5 substantive rounds corrected **work** | AFD `phase-b-s3-block1` and `phase-c1-block1` rev3 counted but not classified |
| AFD-48 reached round 4 because a rung-2 escalation was ordered three times and never delivered | — |
| The ladder appears in **3.3 %** of 331 reviews, 7 of 11 instances in this repository — H5's convergence claim is weak | — |
| DoD 10's baseline is 461/161; the file measures **483/163** | — |
| Step 4 is **109 words** and must absorb four of the six mechanisms | Whether the budget binds per section or per group — the two readings give opposite verdicts |

**Sufficiency:**
- [x] External source used? — four sibling repositories, 331 REVIEW files, all read-only
- [x] Briefing gap closed? — every Gather bullet answered; the two open items are named above
- [x] Dimensions identified? — five, all independent
- [x] Hypothesis tested? — H6 falsified, H5 weakened, H2 undermined, all by measurement
- [x] Counter-evidence sought? — the HL's own counts were re-run before being built on, and two were wrong

**Metacognitive check.** Did I discover something new, or confirm what I knew? **New, and it reversed the
brief.** The HL sent me to `helpdesk` expecting a practice worth more than the cap. What is there is an
unclosed loop. And the causal finding — G5, the escalation ordered three times and never delivered — was
not in any hypothesis. It reframes the task: the loop's depth is an escalation-delivery failure, and the
cap addresses the symptom.

Stage complete: YES
→ User decision: proceed — gates written through on the owner's *"no questions to me"*
