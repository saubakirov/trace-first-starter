# Judge — revision 3 — "Is the quality sufficient?"
> **Mindset:** Judge. Rule on quality against the evidence from Verify.
> Verify findings: [verify.md](verify.md) · earlier: [`../judge.md`](../judge.md) · [`../rev2/judge.md`](../rev2/judge.md)
> **Test:** "Would I stake my reputation on this passing production review?"

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ⚠️ | **The work is done and AC-13 half two is now MET** (verify Part 3, measured by me inside the live consumer). But AC-15's twelve items have **no RF row and no EV row**, and the release surface claims a version the CHANGELOG does not describe — D1, D3. The engineering meets the DoD; the record of it does not exist |
| 2 | **(a) Purpose Check** · **(b) Design soundness** | **(a) ✅** · **(b) ✅** | See below. (b) is the strongest it has been in this phase: the pass found an entity carrying two jobs, removed it, generalized the failure into a DoF rule, and proved the fix on two live corpora without writing to either |
| 3 | Tech debt documented | ❌ | RF §6 has eight observations, none from this pass. `update.md`'s ceiling breach is recorded only in `r4_gates.txt`, pointing at *"see the RF"* — a document that does not exist. `via`'s loss of validation is recorded nowhere |
| 4 | Style & standards | ⚠️ | Canon, templates and adapter layer are clean and internally consistent. **`update.md` is 1380 words against a §11 ceiling of 1200** (D4) — the one workflow this phase had deliberately brought under it |
| 5 | Observations collected | ❌ | Nothing to triage: no RF §6 entries for this pass |
| 6 | RF completeness (§7–10) | ❌ | The RF predates the pass entirely: header at revision 2, TS cited at revision 3, fourteen AC rows, no `actor` decision, no verification numbers |
| 7 | Evidence completeness — does it **exist**? | ⚠️ | The artifacts are good — `census_r4.md` measured before the first edit, `r4_gates.txt`, `ac15_actor_tolerated.txt`. **None is indexed in the EV**, which stops at E63 |
| 8 | Evidence sufficiency — does it **establish the claim**? | ✅ | Where evidence exists it is unusually strong. `ac15_actor_tolerated.txt` does not argue the ruling, it measures it: the same bytes, red before and green after. I re-derived every gate independently and every one held |
| 9 | Backward compatibility | ⚠️ | **The carrier change is handled exactly right**: an existing `actor` is tolerated, never required, never rewritten; 28 events in this repository and 46 across two consumers are untouched; a live project's permanently-red gate clears with nothing changed in it. That is how a schema change should be shipped. **But** D6 — the second consumer converted 12 command files to thin adapters on the strength of a sentence item 12 deletes, and nothing tells it the rule was retracted |
| 10 | Safety | ✅ | Both third-party projects were read and never written: `git status --porcelain` empty in each, before and after. The one destructive-shaped act in the pass — removing a field from a live schema — is implemented as tolerance rather than migration, so no historical record is touched |

## Purpose Check — row 2 clause (a)

**Answered against the master HL at contract baseline `2123de1` plus the Project North Star.
Not the TS — which in this round is the artifact under suspicion.**

**Outcome: Aligned ✅.**

Clause served, quoted: DoD **19** — *"An external project completes the update to a released
version from the payload alone… and every instruction the release gives names something the
receiving project actually has"* — read with the frozen §3.1 promise that six months later a
team can answer *"what state is it in, **who/what acted**, what debt remains, and what
knowledge is waiting."*

**Concrete harm at stake:** the identity model was making a receiving project fabricate data to
get past a gate. The operator wrote the obvious value, was refused, read the validator's
source, and invented a per-session handle — then a second project did the same and, on tidying
up, left its build gate red with no action available to it, because events are immutable and
profiles are not. That is DoD 19's clause failing in its sharpest form: the instruction named
something the reader did not have and could not create honestly. It is also the north star's
non-negotiable — *"a session is not an independent person"* (PV 3 · D59, HL §7.2 citation 14) —
being violated **by the framework's own gate.**

Three tests, each answered *no*:

1. **Excess and adjacency.** The twelve items each trace to a measured failure in a real
   project. Nothing was added because it was nearby. Item 2 went **further than specified in the
   subtractive direction** — the provider list was deleted rather than documented, because with
   `actor` gone nothing reads it.
2. **Deferral confession.** The opposite: what cannot be done now is named and given an owner.
   *"A writer is not named yet, and saying so is the point"* defers to TFW-54 in the canon, in
   the template and in the refusal, instead of shipping a half-answer.
3. **Materiality.** The harm was material, reached two projects out of two, and is now measured
   as removed.

**Reference set consistency:** re-checked. The frozen §3.1 asks *"who/what acted"* — two
questions. The **three**-field model was the over-claim; two fields answer two questions. The
baseline also states that *"the exact filenames and aggregation mechanism remain research
decisions"*, so the filename grammar was never frozen. **No contract defect.**

> **The contract permits this change; the TS forbids it.** That asymmetry is D2, and it is a
> defect in the coordinator's artifact rather than in the contract — which is why this review
> does not raise the third Purpose Check outcome. §1, §7, §8 and §9 are the coordinator's own
> text and the coordinator can repair them; a frozen section would need the owner.

## Contradictions with KNOWLEDGE.md

| # | Item | R4 claim | Contradiction? |
|---|---|---|---|
| 1 | **D59** — capability claims keep boundaries apart; *a session is not an independent person* | `actor` removed; a session may no longer be minted as a participant | **No — this is D59 finally enforced.** The old gate demanded exactly the conflation D59 forbids |
| 2 | **D55** — commit attribution `[agent/task/scope/role]` | unchanged by the pass | **No**, and it matters: the question *"which agent session did this"* is still answered where it was always answered. The journal never was that mechanism |
| 3 | **D65** — reverting a result never reverts its trace | 74 + 6 consumer events and 28 local ones carry `actor` and none is rewritten | **No — a correct application**, and the reason the fix costs nobody anything |
| 4 | **D37** — knowledge write territories | `KNOWLEDGE.md` still untouched by the executor | **No** — still `/tfw-docs`'s, still TD-186 |

## Findings

### F1 — the pass has no RF · **blocking** · verify D1

A carrier-schema change, a filename-grammar change, a canon rewrite, eight workflows and their
sixteen copies — and the RF describes none of it. Its header still says *revision 2*, cites the
**TS at revision 3**, and its acceptance table has fourteen rows.

This is not bookkeeping. The Trust Protocol makes the RF the thing a review is conducted
against; without it there is no declaration to test, only code to read. Concretely lost: no
key-decision row for the two-jobs analysis, no verification block, no observation for the
`update.md` ceiling breach — which `r4_gates.txt` itself defers to *"the RF"* — and no note that
item 2 was closed by deletion rather than documentation. The three evidence artifacts are good
and are not indexed in the EV, which stops at E63.

The work is sound. The record of the work does not exist, and in six months the reasoning that
makes this change defensible will live only in commit messages.

### F2 — the TS forbids in §7 what it mandates in AC-15 · **blocking · coordinator's** · verify D2

Four statements, all still standing:

| Where | Text |
|---|---|
| §1 Objective | *"The model itself does not change. No carrier, schema, vocabulary, lifecycle value or identifier rule is touched."* |
| §7 DoF, last line | *"❌ The model changed: any edit to a carrier schema, the event grammar, the lifecycle vocabulary or the identifier rules"* |
| §8 Risks, last row | *"A finding about the model is filed, not fixed here"* |
| §9 Cross-Phase | *"changes no carrier they will extend"* |

AC-15 item 1 removes a field from the event carrier and rewrites the filename grammar.

The *"Why no amendment"* box is a sound argument about the **master HL** — no §5 or §6 clause is
crossed, and I agree. It simply never addresses the TS's own four sentences. An executor who
opens §7 before AC-15 is told the pass is a declared failure; one who opens AC-15 first is told
it is the deliverable. `fd85b7c` corrected the revision header for precisely this class and
called it *"exactly the residue I had just finished telling the executor not to leave behind"* —
the same residue is four sections deep in the same file.

**Routes to the coordinator.** The TS is not frozen and needs no amendment; it needs its own
text brought into line with the ruling it now carries.

### F3 — the version marker names a release the CHANGELOG does not describe · **blocking** · verify D3

`.tfw/VERSION` and `tfw.version` read `2.0.0-dirty.3`. The CHANGELOG's newest entry is
`[2.0.0-dirty.2]`; `[Unreleased]` says *"Nothing pending."*

Meanwhile **eight payload files** teach a reader about `2.0.0-dirty.3` — `conventions.md`,
`glossary.md`, `migrations/2.0.0.md`, `templates/journal/event.md`, `templates/bindings.yaml`,
`adapters/claude-code/README.md`, `workflows/update.md`, `project_config.yaml`. A receiving
project reads *"an event written before 2.0.0-dirty.3 carries `actor`"*, turns to the changelog
to find out what `.3` is, and finds that it does not exist.

AC-14 is *"The release describes what shipped."* HL principle 10 is *"Every phase pays for its
release surface."* This is the phase's own subject inverted: not an instruction naming a missing
file, but a version naming a missing record. It is also the one item here that a **third**
external consumer would hit immediately.

### F4 — `update.md` is back over the ceiling · **Medium** · verify D4

1165 → **1380** against §11's 1200. D9 in the first round brought this file *under* by deleting
duplication rather than required content, and the RF made a point of it. The pass added Step 6's
measurement, the retired-term grep, `installed_from` and the binding guidance, and did not run
D9's move a second time. `r4_gates.txt` names the breach and points at the missing RF.

`handoff`, `init`, `plan` and `review` are also over — all four were over before this pass and
moved +18 to +38. `update.md` is the only one this pass pushed across, and it is the workflow a
receiving project actually runs.

### F5 — `via` now has no gate · **Low** · verify D5

`PROVIDER_FAMILIES` was deleted with sound reasoning: its only reader was the `actor` gate.
But the canon still states `via` as an enumeration — *"provider family — `claude`, `codex`,
`gemini`"* — and nothing checks it. Under **Structural Enforcement**, a rule that cannot reveal
its own violation is advice. Either say `via` is free-form provider text, or check it. Not
urgent; worth one deliberate sentence rather than drift.

### F6 — a consumer acted on a rule this pass retracts · **Medium** · verify D6

`innoforce-ai-first` rewrote 12 command files from copies to thin adapters, citing
`adapters/claude-code/README.md`: *"Commands never duplicate workflow content — they reference
it."* Item 12 deletes that sentence and declares copies the model. The consumer followed a
shipped rule, and the rule was withdrawn behind it. Its thin adapters now diverge from the
declared shape and Step 6's re-sync will not recognize them.

Not a defect in the ruling — copies-as-the-model is defensible and now has two mechanisms
backing it. The defect is that a retraction reaching a project that already acted on it is
exactly the class this phase measures, and the release note is where it belongs.

### What this pass did outstandingly well

Recorded because a reviewer should say when the work is better than its brief.

**It found a design error rather than a bug, and said so.** The report handed over a symptom —
*"there is no naming convention for an agent handle"* — with two branches: bless per-session
handles, or say the opposite. Taking the first would have shipped a naming rule and left the
contradiction. The pass asked what job the field actually does, found two, and removed the one
that could not be done honestly yet.

**It generalized the failure into a rule.** DoF R4 — *"an entity whose single job was never
named aloud"* — with four instances in this task named against it, including two the phase had
already committed. That is the finding, not the fix.

**It refused the small answer twice.** §10.4 was rewritten as a rule rather than patched at its
example, with my revision-2 objection quoted rather than overridden. `PROVIDER_FAMILIES` was
deleted rather than documented.

**It proved the fix on live third-party corpora without writing to them.** Red before, green
after, zero bytes changed, `git status` empty. That is how a schema change earns trust.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence?
- [x] Every `⚪ N/A` carries a reason — no bare-✅ skip? — no row answered `⚪ N/A`
- [x] Row 2(a) answered against baseline `2123de1` and the north star, with a quoted clause **and** a named harm?
- [x] Rows 7 and 8 answered separately, with different reasoning? — 7: the artifacts exist but are unindexed and the RF is absent. 8: what does exist establishes its claims unusually well. `⚠️` on 7 with `✅` on 8 is the shape here
- [x] Referenced verify.md findings? — rows 1, 3, 4, 6, 7, 9 and F1–F6 all cite it
- [x] Checked RF §7–10 for presence AND quality? — present from earlier passes, **absent for this one**
- [x] KNOWLEDGE.md cross-referenced — four items, no contradictions; D59 is enforced rather than crossed
- [x] Fact Candidates reviewed — none new from the executor this pass, because there is no RF to carry them. Two are filed in the REVIEW instead

Stage complete: YES
