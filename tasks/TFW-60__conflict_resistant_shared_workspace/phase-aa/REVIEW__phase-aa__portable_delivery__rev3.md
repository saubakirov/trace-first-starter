# REVIEW — TFW-60 / Phase AA: Portable Delivery (revision 3)

> **Date**: 2026-08-28
> **Author**: Claude Code (Reviewer), `on_behalf_of: saubakirov`, `via: claude`
> **Verdict**: ✅ **APPROVE — by owner decision, 2026-08-29**, over the reviewer's 🔄 REVISE.
> Two of the three blocking items were **closed** by the coordinator before the ruling landed
> (`ab7093e`, `edab067`); the third stands as **TD-199**. The phase's own closure commit
> `9570402` records this as a **waiver rather than an approval**, and that is the more precise
> word — it is kept here rather than smoothed over. The analysis that produced REVISE is left
> standing in §4 and in the stage files: the verdict changed, the finding did not.
> **Reviews the R4 corrective pass** — TS **revision 4**, AC-15, twelve items
> **TS**: [TS Phase AA, revision 4](TS__phase-aa__portable_delivery.md)
> **RF**: [RF Phase AA](RF__phase-aa__portable_delivery.md) — **at revision 2. It does not describe this pass**
> **Field report**: [second external update](../FIELD-REPORT__TFW-60__second_external_update.md) — filed, verbatim, not authored here
> **Contract baseline**: master HL at `2123de1` (after amendment A4)
> **Reviewed at**: `b75bef1`. Commits: `22de861` · `d62fd26` · `2d269e4` · `f7c9dfe` · `94f02a6` · `fd85b7c` · `5e9b0a1` · `b75bef1`
> **Stage files**: [`review/rev3/map.md`](review/rev3/map.md) · [`review/rev3/verify.md`](review/rev3/verify.md) · [`review/rev3/judge.md`](review/rev3/judge.md)
> Earlier passes stand: [first — REVISE](REVIEW__phase-aa__portable_delivery.md) · [revision 2 — APPROVE](REVIEW__phase-aa__portable_delivery__rev2.md)
> **Owner's stated emphasis:** quality, architecture, value, goal. Counts are not the question and are not reopened.

---

## 1. Map

The awaited evidence arrived and it brought a design error with it.

`innoforce-ai-first` — a real external project, a different session, no access to this phase's
reasoning — ran the full `1.3.0 → 2.0.0-dirty.2` update including the board migration and wrote
its own retro. On the phase's purpose the answer is unambiguous: the first consumer *"spent the
rest of the session reconstructing what to do and in what order"*; this one **spent nothing**.
Zero unrecognized directories, zero unaccounted rows, and the identity gate **refused** a bad
value rather than swallowing it.

Then it recorded what refusing cost. The operator wrote the obvious `actor: claude-code`, was
refused, **read the validator's source**, and invented `claude-20260828a`. Two projects out of
two were pushed into minting a profile per agent session; one later deleted them and left its
build gate **red permanently** — events are immutable, profiles are not, and no action inside
that project could ever clear it.

The owner's ruling names the cause rather than the symptom: `actor` was carrying two unrelated
jobs — *say who wrote this* and *make the filename unique* — and the two contradict each other.
A distinct writer needs a distinct value; a declared handle needs a profile. **Remove the field
until TFW-54.** The pass then closes eleven further items, every one traced to a measured
failure in a real project.

## 2. Verify

Every claim re-derived. Nothing accepted on the strength of a commit message.

| # | Checked | Result |
|---|---|---|
| 1 | Full suite | **260 passed, 1 skipped** |
| 2 | `mkdocs build` | exit **0** |
| 3 | `--check index` · `tasks` · `project` | exit **0** each |
| 4 | Retired vocabulary in the adapter layer | **0 files** |
| 5 | `actor` across every instruction surface | only prose narrating the retirement survives — **zero live instructions** to write it |
| 6 | §10.4 read back against all templates | **20 templates, 0 contradicting** |
| 7 | Every payload path, three reference forms | **unresolved: none** — TD-193 and TD-194 close |
| 8 | Consumer payload vs `v2.0.0-dirty.2` | 68 files, **0 missing, 0 stray**, 65 byte-identical; the 3 that differ are `CHANGELOG.md` (one commit behind the tag's own record) and the two project-owned files |
| 9 | `--check tasks` on the live consumer, current code | **15 tasks validate** — it was *"2 problems across 15 tasks"* under the shipped code |
| 10 | `git status --porcelain` in both consumers, before and after | **empty** — my verification wrote nothing to a project that is not ours |

### The architectural question, answered

**Is removing `actor` a loss of capability?** No — it is the removal of a false claim.

Measured, the field never carried an independent fact: upstream, **21 consecutive events**
repeat `on_behalf_of` in it; in the consumer it is `via` plus a session number. And the frozen
master HL §3.1 asks that a team be able to answer *"who/what acted"* — **two** questions. Two
fields answer them: `on_behalf_of` — who — and `via` — what. The three-field model was the
over-claim; the two-field model is closer to the frozen text, not further from it.

What is genuinely given up — telling two concurrent sessions of one tool apart inside the
journal — was never delivered; it is what forced the per-session profiles. Git commit
attribution (D55) still answers it where it was always answered. The canon says the gap is open
and gives it an owner: *"A writer is not named yet, and saying so is the point."*

**And the fix costs nobody anything.** An already-written `actor` is tolerated, never required,
never rewritten. 28 events here and 46 across two consumers keep their bytes. I re-measured it
myself: the same bytes that were red under the shipped code are green under this one, with
**zero bytes changed in that project.**

```
innoforce-ai-first, same files, read-only

  under 2.0.0-dirty.2   2 problem(s) across 15 tasks   ← permanently red: the profiles
                                                          those events name were deleted
  under this pass       15 tasks validate               ← nothing in that project changed
```

That is how a schema change earns trust, and it is measured rather than argued.

### AC-13 half two — ruled **MET**

The executor left E51 `DEFERRED` and routed the ruling here, correctly: *"whether the phase's
declared outcome is thereby met is a reviewer's and the owner's ruling, not the executor's to
grant itself."*

| The TS's own bullets | Measurement |
|---|---|
| a real external project, updated by its own operator | a different project, a different session, its own document filed verbatim |
| zero files hand-carried | **0 missing, 0 stray** of 68 payload files |
| zero edits inside `.tfw/` | 65 of 68 byte-identical; the three exceptions are one CHANGELOG commit and the two project-owned files |
| every delta the first consumer invented is unnecessary | board flags shipped, `team/README.md` withdrawn, tooling in the payload — all three confirmed |
| the run records what was confusing | five findings, four of which became AC-15 items |

**The findings it returned are what the criterion asked for, not evidence that it failed** — the
bullet requires the run to record what was confusing. And the regress needs naming: `b75bef1`'s
message says half two *"closes on a third external run."* It does not. Requiring a fresh
external run to certify each correction the previous run produced defers the phase forever. DoD
19 says *an* external project completes the update from the payload alone. One did, and I
measured it.

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ⚠️ | The engineering meets it and **AC-13 half two is now MET**. AC-15's twelve items have no RF row and no EV row, and the version marker names a release the CHANGELOG does not describe |
| 2 | Purpose · design soundness | **(a) ✅ · (b) ✅** | **(a)** serves DoD 19 and the north star's *"a session is not an independent person"* (PV 3 · D59) — which the framework's own gate was violating. **(b)** the strongest of the phase: an entity carrying two jobs found, removed, generalized into a DoF rule, and proved on live corpora |
| 3 | Tech debt documented | ❌ | No RF §6 entries for this pass. The word-ceiling breach is recorded only in an evidence file that defers to *"the RF"* |
| 4 | Style & standards | ⚠️ | Canon, templates and adapter layer clean. `update.md` **1380 words against a ceiling of 1200** |
| 5 | Observations collected | ❌ | Nothing to triage |
| 6 | RF completeness | ❌ | The RF predates the pass entirely |
| 7 | Evidence completeness | ⚠️ | Three good artifacts, **none indexed in the EV** |
| 8 | Evidence sufficiency | ✅ | Where evidence exists it is unusually strong; every gate re-derived and every one held |
| 9 | Backward compatibility | ⚠️ | The carrier change is handled **exactly right** — tolerance, not migration. But a consumer acted on a rule this pass retracts (F6) |
| 10 | Safety | ✅ | Both third-party projects read and never written |

**Purpose Check: Aligned ✅.** Reference set re-checked: §3.1's *"who/what acted"* is two
questions and now has two fields; the baseline states that *"the exact filenames and aggregation
mechanism remain research decisions"*, so the filename grammar was never frozen. **No contract
defect** — the contract permits this change. Only the TS forbids it, and that is F2.

## 4. Verdict

**✅ APPROVE — by owner decision, 2026-08-29, over the reviewer's 🔄 REVISE.**

> **What actually happened, and it is not what an earlier draft of this section said.** This
> review returned 🔄 REVISE with three items, all record-keeping and none in the engineering.
> The owner ruled them not worth a round: *«отметить как апрув, эти мелочи править не будем»*.
>
> **Two of the three were already closed by then**, by a coordinator session working
> concurrently in the same tree while this review was being written:
>
> | Item | Disposition |
> |---|---|
> | 2 — the TS mandated in AC-15 what §1, §7, §8 and §9 forbade | **Closed**, `ab7093e` — the four sentences now state the exception once with its reason, every other prohibition intact, and §9 tells Phases B and C directly that they extend a two-field event |
> | 3 — `VERSION` said `2.0.0-dirty.3` and no changelog entry described it | **Closed**, `edab067` — the entry leads with what an updating project must do about the `actor` removal: *nothing* |
> | 1 — the R4 pass has no RF | **Outstanding**, filed as **TD-199**. Genuinely waived |
>
> `F4` (`update.md` at 1380 words) and `TD-197` (`via` unvalidated) were **moved into Phase AB**
> rather than waived — both land in files that phase opens anyway.
>
> **The word the closure commit uses is "waiver, not approval", and it is the better word.**
> Blocking item 1 stands: the phase's largest architectural change has no executor declaration.
> What survives it is real — TS AC-15 carries the analysis and §2 of this review carries an
> independent measurement — but neither is an RF.
>
> **Nothing in the engineering was ever in question.** Every gate was re-derived here, and §4
> below already called this the strongest work of the phase.

The reasoning that produced the original verdict follows unchanged.

Let me be exact about what I was returning, because the work itself is the best in this phase.

**The architecture is right, and right for the right reason.** The report handed over a symptom
with two branches — bless per-session agent handles, or say the opposite. Taking the first
would have shipped a naming convention and left the contradiction in place. Instead the pass
asked what job the field actually does, found two, established that one of them cannot be done
honestly until there is a principal that delegates and answers to someone, and removed it. Then
it wrote the general rule into the DoF — *"an entity whose single job was never named aloud"* —
and listed four instances from this task against it, two of which the phase had itself
committed. That is a finding about how the project fails, not a patch.

**The value is delivered and measured.** A live external project's permanently-red gate goes
green with zero bytes changed inside it. Not argued — measured, by the executor and again by me.

**And it refused the small answer twice more.** §10.4 was rewritten as a rule rather than
patched at its example, with my revision-2 objection quoted rather than overridden — 20
templates, 0 contradicting. `PROVIDER_FAMILIES` was deleted rather than documented, because
with `actor` gone nothing reads it.

What I was returning is the record, not the work — **all three now carried as debt by owner
ruling** rather than closed in a round:

| # | Item | Routes to |
|---|---|---|
| **1** | **The pass has no RF.** Header says revision 2, cites TS revision 3, fourteen AC rows, no AC-15, no key decision for the two-jobs analysis, no verification block, no observation for the ceiling breach — which `r4_gates.txt` itself defers to *"the RF."* Three good evidence artifacts exist and **none is indexed in the EV**, which stops at E63. The Trust Protocol makes the RF the thing a review is conducted against; for the largest architectural change of the phase there is no declaration to test. In six months the reasoning that makes this defensible lives only in commit messages | **executor** |
| **2** | **The TS mandates in AC-15 what it forbids in §1, §7, §8 and §9.** §1 *"The model itself does not change… no carrier, schema… is touched"*; §7 *"❌ The model changed: any edit to a carrier schema, the event grammar…"*; §8 *"A finding about the model is filed, not fixed here"*; §9 *"changes no carrier they will extend."* The *"Why no amendment"* box is a sound argument about the **master HL** — no §5 or §6 clause is crossed and I agree — and it never touches the TS's own four sentences. An executor reading §7 before AC-15 is told the pass is a declared failure. **No amendment is needed**; the TS is not frozen and needs its own text brought into line with the ruling it now carries | **coordinator** |
| **3** | **`.tfw/VERSION` and `tfw.version` say `2.0.0-dirty.3`; the CHANGELOG has no such entry** — its newest is `[2.0.0-dirty.2]` and `[Unreleased]` says *"Nothing pending."* Meanwhile **eight payload files** teach a reader about `2.0.0-dirty.3`: the canon, the glossary, the migration guide, the event template, `bindings.yaml`, the adapter README, `update.md`, `project_config.yaml`. A project reading *"an event written before 2.0.0-dirty.3 carries `actor`"* and turning to the changelog finds no such release. This is AC-14's own criterion and HL principle 10, and it is the phase's subject inverted: not an instruction naming a missing file, but a version naming a missing record. **The entry must also carry F6** — that copies are now the declared adapter model and the *"commands never duplicate workflow content"* rule is withdrawn, because a consumer has already acted on it | **executor** (release surface, TS-authorized per ONB Q3) |

Two further items, not blocking, to be closed in the same pass or filed:

- **F4 — `update.md` 1165 → 1380 against the §11 ceiling of 1200.** This is the workflow a
  receiving project actually runs, and the one file this phase had deliberately brought *under*
  the ceiling by deleting duplication rather than content (D9). Run D9's move again, or get a
  coordinator ruling. `handoff`, `init`, `plan` and `review` are also over and were before this
  pass; `update.md` is the only one this pass pushed across.
- **F5 — `via` is now validated by nothing** while the canon still states it as an enumeration.
  Under **Structural Enforcement**, a rule that cannot reveal its own violation is advice.
  Either say `via` is free-form provider text, or check it. One deliberate sentence, not drift.

**This is not a REJECT and it is not close to one.** Purpose is aligned, the contract permits
the change, nothing is unsafe, no work is wasted, and no finding touches the design. Three
documents have to catch up with what was built.

### What this approval covers

**AC-13 half two is met and does not need re-running.** The phase closes on the evidence already
filed: a real external project, updated by an operator who is not the author, 0 files
hand-carried and 0 framework files edited inside `.tfw/`, independently re-measured by this
review. What a third external project produces afterwards is Phase AA's successor evidence, not
its gate.

**What it does not cover — one item, and it is the one that is genuinely waived.** **TD-199**:
the R4 pass ships with no RF, so the two-jobs analysis, the verification numbers and the
`update.md` ceiling breach live only in commit messages and three evidence files the EV does not
index. TS AC-15 carries the reasoning and §2 of this review carries an independent measurement —
both permanent, and neither is an executor's declaration of what was built.

Blocking items 2 and 3 are **not** in this category: `ab7093e` brought the TS's four sentences
into line with its own ruling, and `edab067` wrote the `2.0.0-dirty.3` entry. `F4` and `TD-197`
moved into **Phase AB**, which opens the same files anyway.

## 5. Tech Debt Collected

No RF §6 entries exist for this pass, so nothing was triaged from the executor. TD-192, TD-193
and TD-194 **close** with this pass — §10.4 rewritten as a rule, the path check extended to all
three reference forms, the glossary swept. Two new rows from this review:

| # | Source | Severity | File | Description | Action |
|---|---|---|---|---|---|
| TD-197 | REVIEW TFW-60/AA rev3 §4 F5 | Low | `.tfw/scripts/gen_index.py`, `.tfw/conventions.md`:317 | `PROVIDER_FAMILIES` was deleted at `2.0.0-dirty.3` with sound reasoning — its only reader was the `actor` gate. But the canon still states `via` as an enumeration (*"provider family — `claude`, `codex`, `gemini`"*) and **nothing validates it**. Under the project's own **Structural Enforcement** value a rule that cannot reveal its own violation is advice | ⬜ Open — one deliberate decision: declare `via` free-form provider text, or check it. Not urgent; the harm is drift, not breakage |
| TD-198 | REVIEW TFW-60/AA rev3 §4 F6 | Med | `.tfw/adapters/claude-code/README.md`, `.tfw/CHANGELOG.md` | **A consumer acted on a rule this release retracts.** `innoforce-ai-first` rewrote 12 command files from copies to thin adapters, citing the shipped sentence *"Commands never duplicate workflow content — they reference it."* AC-15 item 12 deletes that sentence and declares copies the model. The consumer followed a shipped rule and the rule was withdrawn behind it; its thin adapters now diverge from the declared shape and Step 6's re-sync will not recognize them | ⬜ Open — fold into blocking item 3: the `2.0.0-dirty.3` entry states the retraction and what a project that already went thin should do. A retraction reaching a project that acted on it is the class this phase measures |

## 6. Traces Updated

- [x] the phase's `status.md` — `lifecycle: DONE`, closed by the coordinator at `9570402` with the outcome recorded as a waiver: *"closed by owner 2026-08-29 with review rev3's blocking item 1 outstanding; the pass has no RF of its own"*
- [x] `TECH_DEBT.md` — **TD-197, TD-198** (this review) and **TD-199** (blocking item 1, filed by the coordinator) added; **TD-192, TD-193, TD-194 closed** by the R4 pass. There is no TD-200 or TD-201: blocking items 2 and 3 were fixed, not deferred
- [ ] tfw-docs: **Pending** — TD-186 (`KNOWLEDGE.md:22`) is its first item, and §1–§3 now need the two-field identity model
- [ ] tfw-knowledge: **Pending** — this review's two candidates plus the nine standing from earlier passes

## 7. Fact Candidates

> fact-candidates: processed 2026-08-30

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | philosophy | **A gate that refuses without naming what it accepts makes the reader fabricate data to get past it.** The identity gate correctly rejected `actor: claude-code`, named no valid form, and the operator read the validator's source and minted a per-session handle — then a second project did the same and, on tidying up, left its build gate red with no action available to it. The refusal was right and the design behind it was wrong: before adding a gate, say what passes it, and if that cannot be said the gate is guarding a field that should not exist | Second external update, F1; owner ruling 2026-08-28 | High |
| 2 | process | **A ruling that changes the spec must sweep the spec.** AC-15 was written into a TS whose §1, §7, §8 and §9 still forbid exactly what it mandates — the same class the phase itself prosecutes in the payload, committed in the document that governs the payload. The coordinator caught the shape one commit earlier (*"exactly the residue I had just finished telling the executor not to leave behind"*) and caught it in the header only | Reviewer, this revision | High |

---

*REVIEW — TFW-60 / Phase AA: Portable Delivery (revision 3) | 2026-08-28, reviewed at `b75bef1`*
