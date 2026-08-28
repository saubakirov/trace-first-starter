# Judge — revision 2 — "Is the quality sufficient?"
> **Mindset:** Judge. Rule on quality against the evidence from Verify.
> Verify findings: [verify.md](verify.md) · first pass: [`../judge.md`](../judge.md)
> **Test:** "Would I stake my reputation on this passing production review?"

## Universal Checklist

Rows unchanged from the first pass are marked *(held)* with what re-verified them. Rows the
revise round moved carry new reasoning.

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | *(held, re-verified)* 14 of 15 AC halves; suite **255 passed, 1 skipped**; three `--check` subjects exit 0; `mkdocs build` exit 0 in 97 s. AC-13 half two still ❌ UNMET and still routed to the owner — unchanged, and unchanged is correct |
| 2 | **(a) Purpose Check** · **(b) Design soundness** | **(a) ✅** · **(b) ✅** | See the Purpose Check below. **(b)** strengthened by this round: the design gained a *structural* control where it previously had an intention. `test_no_normative_file_states_a_retired_rule` puts the "did the rewrite reach every copy" question into observable state — which is Methodology value **Structural Enforcement**, *"a rule that cannot reveal its own violation is only advice"*, applied to the phase's own failure mode |
| 3 | Tech debt documented | ✅ | RF §6 now carries eight observations. #8 is the new one and it is the right kind: it names what the new check cannot reach, why a line-proximity heuristic or an allowlist would rot, that the shipped harm is bounded because a receiving project never reads these test files, and the candidate fix if it recurs |
| 4 | Style & standards | ✅ **was ⚠️** | The finding that held this row is closed: `templates/status.md` states the two-act rule and **cites** §5 rather than adding a third copy of the table, and the count reads *"six"*. Naming, word ceiling and commit attribution re-checked and unchanged |
| 5 | Observations collected | ✅ | Quality filter re-applied to the new #8: it survives — it changes what a future maintainer will do |
| 6 | RF completeness (§7-9) | ✅ | §7 gains two candidates (#8, #9) and §8 gains S4, all three attributed to the review rather than claimed. §10 is a new section giving the revise round its own account. Nothing padded |
| 7 | Evidence completeness | ✅ | *(held)* 60 items, all artifacts resolve. `ac3_parser_untouched.txt` gained a second measurement and both methods |
| 8 | Evidence sufficiency | ✅ **was ⚠️** | All four named gaps closed, and I checked the closures against the artifacts rather than the RF's account of them. Two deserve specific credit: **(c)** the ASCII check's reach is now described as what the code does, not as what one would like it to do; and **(d)** in `312dca9` the executor caught itself about to ship *my* parser number as its own, re-derived it, got a different figure under a different boundary rule, and recorded both with their methods — *"a number from someone else's run is not one they can vouch for."* That is the correct relationship between a reviewer's measurement and an executor's evidence, and I would rather see the disagreement disclosed than my number adopted |
| 9 | Backward compatibility | ⚠️ | *(held for code)* — the one deliberate break is documented as before. **New, from the owner's audit:** the template moves changed three published documentation URLs with no redirect, and the move put `templates/knowledge/` beside `templates/KNOWLEDGE.md`, which on a case-insensitive filesystem merges two page directories in a local build. Neither reaches a receiving project — `docs/` is not in the payload — and deployment always builds on `ubuntu-latest`, so the live site is unaffected. Filed as debt, not as a round. **Verified clean, and worth stating:** `gen_docs.py`'s backtick resolver is existence-guarded, so the 17 deliberately-preserved historical artifacts naming a moved template render as inert code rather than as dead links — **0** dead hrefs in a full build |
| 10 | Safety | ✅ | *(held)* nothing in the revise round touches the destructive surface. Test-file root resolution moved from `parents[2]` to the marker search, which narrows rather than widens what a misplaced run could touch |

## Purpose Check — row 2 clause (a)

**Answered against the master HL at contract baseline `2123de1` plus the Project North Star.
Not the TS, not the Phase HL.**

**Outcome: Aligned ✅.**

Clause served, quoted: DoD **19** — *"An external project completes the update to a released
version **from the payload alone** — no file hand-carried from this repository, no edit inside
`.tfw/`, and every instruction the release gives names something the receiving project
actually has"* — read with **NS1**, *"another authorized person or agent can understand what
the work is for, inspect its material grounds and current result, see where authority remains,
and continue without rebuilding the original conversation."*

**Concrete harm at stake, and why this revision matters to it:** the phase's whole subject is
that a receiving project holds only the payload, so a payload that misleads it is the failure.
The first pass found the payload stating two opposite rules about the same act, with the
absolute one in the file a person hand-authors the carrier from. That is DoD 19's last clause
failing from the inside — *"every instruction the release gives names something the receiving
project actually has"* has a twin, *every rule it states must be the rule*. Revision 2 closes
it, and then closes three more of the same shape, one of them in code this phase had just
edited.

Three tests, each answered *no*:

1. **Excess and adjacency** — the revise round added one test file's worth of mechanism and
   four one-line corrections. Nothing outside the returned items and their own class.
2. **Deferral confession** — RF §6 #8 names what the new check does not reach and ships
   nothing there. Correct form.
3. **Materiality** — the harm was material and is now removed.

**Reference set consistency:** re-checked. Baseline Phase AA block, DoD 19, DoF 10 and NS1
remain coherent. **No contract defect.**

**The one thing the Purpose Check does not resolve, restated so approval is not read as more
than it is:** Phase AA's declared outcome is *a project other than this one completes the
update from the payload alone*, and the only run so far was the author's own clone. Purpose
asks whether this is what we set out to do — it is, exactly. Whether it is **proven** is
AC-13 half two, and the contract assigns that to the owner. Approving the phase's work is not
approving that claim.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---|---|---|
| 1 | **D37** — knowledge write territories | `KNOWLEDGE.md:22` still stale; executor did not write it; TD-191's registry half also left to `TECH_DEBT.md` | **No — the opposite, twice.** The executor took the half of TD-191 that was its own (drop the dead label) and left the half that belongs to a file it does not own. That is the ownership split working without being told |
| 2 | **D50** — numbered research stage files (`1_briefing.md`..`4_challenge.md`) | — | **No, but it exposes one:** `glossary.md` still names `research/gather.md`, `extract.md`, `challenge.md`, stale since TFW-42. D50 records the rename; the glossary never followed. Pre-existing, filed |
| 3 | **D65** — reverting a result never reverts its trace | The `[2.0.0-dirty]` CHANGELOG entry's absolute-rule paraphrase deliberately left standing, with the exemption written down | **No — a correct application.** A changelog records what a release shipped |
| 4 | **D31, D50, D55, D59** | *(held from the first pass)* | No |

## Findings

### F1 — the naming canon now illustrates itself with a deleted file · **Medium** · debt, not a round · verify.md E1

`conventions.md:690`, §10.4:

> Markdown templates in `.tfw/templates/` also follow `lower_snake_case`:
> - `topic_file.md` (not `TOPIC_FILE.md`)

`topic_file.md` was deleted by this phase. `census.md` **enumerated this exact line** — the
`topic_file.md` group lists conventions.md at `:603` and `:629`; `:603` was fixed and `:629`
(now `:690`) was not.

Why it is debt and not a third round: swapping the filename would leave a rule with **9
standing counterexamples** among its own 20 subjects — `HL.md`, `TS.md`, `RF.md`, `RES.md`,
`ONB.md`, `REVIEW.md`, `KNOWLEDGE.md`, `RELEASE.md`, `evidence/EV.md` — and, after this move,
**no live demonstrator of `lower_snake_case` at all** except a numbered research stage. Nine
of those predate the phase. The real fix is §10.4 stating what the convention actually is,
which is a scoped naming decision and not a line edit inside a delivery phase. Returning it
would buy a patch and leave the rule wrong.

### F2 — nothing checks template references outside `adapters/` · **Medium** · debt · verify.md E3

This is the mechanism behind F1 and behind the five stale `glossary.md` research references
that have sat there since TFW-42. The shipped path check (`test_every_path_an_adapter_source_names_resolves`)
scans `.tfw/adapters/**` and installed copies, and only the `.tfw/`-prefixed form. Workflows
and canon use **both** forms — `init.md` writes `.tfw/templates/X`, `plan.md` writes bare
`templates/X` — and neither is covered anywhere.

My own audit found six broken targets in 137 references. Three are the migration guide
deliberately naming retired paths; three are the pre-existing glossary drift. The gap is the
finding: a phase that moved three templates had no mechanism that could tell it whether the
move was complete, and it turned out to be complete except in one enumerated place.

**Worth saying about the fix's shape:** the executor's new retired-wording test is the right
precedent — a registry, a stated reach, and a proof that the failing branch fires. The same
form extended from *retired wordings* to *every path a payload file names*, in both reference
forms, would have caught F1, the glossary five, and TD-11's dead identifier in one pass.

### F3 — the template moves have two consequences in the docs site · **Low** · debt · verify.md E4, and verify.md Part 2

Both outside the payload, so no receiving project is affected.

- **Three published URLs changed with no redirect.** `reference/templates/team_profile/` →
  `reference/templates/team/profile/`, and likewise for the other two. No redirects plugin.
  Nothing in the repository links to the old URLs; an outside bookmark 404s.
- **`templates/knowledge/` now sits beside `templates/KNOWLEDGE.md`**, and mkdocs derives page
  paths from the subpath, so a build on a case-insensitive filesystem physically merges
  `reference/templates/KNOWLEDGE/` and `reference/templates/knowledge/topic/`. Verified: the
  local Windows build puts `topic/index.html` inside `KNOWLEDGE/` while the search index
  advertises `knowledge/topic/`. **`REVIEW.md` + `review/` already had this shape**, so the
  phase reproduced a latent defect rather than inventing one — and deployment always runs on
  `ubuntu-latest`, where the two are distinct, so the live site is correct. The bite is that a
  local Windows preview is not what deploys.

### What this round did better than it was asked to

Recorded because the reviewer's job includes saying when the answer exceeded the question.

The review returned one file, one line, and four wording corrections. The executor instead
took the **mechanic** the review's fact candidate named and ran it — finding a stale
`--validate` docstring in a test whose call site the same phase had updated, and `parents[2]`
still sitting in the test files of the module that had just stopped depending on depth. **The
first pass noticed that second one and did not file it.** The RF says so plainly. Then it
turned the mechanic into a test, stated the test's reach, proved its failing branch, and filed
what it cannot reach.

RF §8 S4 draws the right conclusion: *"A phase that legislates against a failure mode is the
most likely place to commit it."* That is a real finding about how this project works, not a
retrospective flourish.

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence?
- [x] Every `⚪ N/A` carries a reason — no bare-✅ skip? — no row was answered `⚪ N/A`
- [x] Row 2(a) answered against baseline `2123de1` and the north star, with a quoted clause **and** a named harm?
- [x] Rows 7 and 8 answered separately? — 7 asks whether the artifacts exist; 8 asks whether the four previously-loose claims now hold, checked at the artifacts
- [x] Referenced verify.md findings? — rows 1, 4, 8, 9 and F1–F3 all cite it
- [x] Checked RF §7-10 for presence AND quality?
- [x] KNOWLEDGE.md cross-referenced? — four items, no contradictions; D50 exposed a pre-existing drift, filed
- [x] Fact Candidates reviewed — any needing challenge? — nine reviewed, **none challenged.** #8 and #9 are attributed to the review, which is correct attribution rather than borrowed credit

Stage complete: YES
