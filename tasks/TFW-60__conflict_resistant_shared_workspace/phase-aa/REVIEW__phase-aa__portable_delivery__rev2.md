# REVIEW — TFW-60 / Phase AA: Portable Delivery (revision 2)

> **Date**: 2026-08-28
> **Author**: Claude Code (Reviewer), `actor: saubakirov`, `via: claude`
> **Verdict**: ✅ **APPROVE** — with five debt items, none of them in the payload's instruction surface
> **RF**: [RF Phase AA](RF__phase-aa__portable_delivery.md) at **revision 2**
> **TS**: [TS Phase AA, revision 3](TS__phase-aa__portable_delivery.md)
> **Historical REVIEW**: [first pass — 🔄 REVISE](REVIEW__phase-aa__portable_delivery.md)
> **Contract baseline**: master HL at `2123de1` (after amendment A4)
> **Reviewed at**: `312dca9`. Commits under review: `b44bf7d`, `312dca9`
> **Stage files**: [`review/rev2/map.md`](review/rev2/map.md) · [`review/rev2/verify.md`](review/rev2/verify.md) · [`review/rev2/judge.md`](review/rev2/judge.md)
> This is a new review revision. It does not replace or rewrite the first pass.
> **Owner's stated emphasis for this pass:** not file or line counts — *«важнее качество цели
> ценности»* — and a full audit of the template moves. Counts are recorded as the RF now states
> them and are **not** reopened.

---

## 1. Map

The three returned items are closed. Then the executor did more than was asked: it took the
**mechanic** the first review's fact candidate named — *grep the retired sentence, not the
concept* — ran it, and found four more sites of the same class. Two were in code this phase
had just edited. One of those, `parents[2]` still sitting in the test files of the module that
had stopped depending on depth, the first pass had **seen and not filed**; the RF says so.

`templates/status.md` now states the two-act `UNDECLARED` rule and **cites** `conventions.md`
§5 instead of adding a third copy of its table. The four loose claims are narrowed at the
artifact, not in prose about the artifact. And in `312dca9` the executor caught itself about to
ship the reviewer's parser measurement as its own, re-derived it, got a different figure under
a different boundary rule, and recorded both with their methods.

The class is now a test rather than an intention: a registry of retired wordings checked
against every payload file that instructs, with its reach stated and the part it cannot reach
filed as an observation.

## 2. Verify

| # | What was checked | Result |
|---|---|---|
| 1 | Full suite | ✅ **255 passed, 1 skipped** in 156 s — matches the RF; +2 over the first pass |
| 2 | `--check index` · `tasks` · `project` | ✅ exit **0** each |
| 3 | `mkdocs build` | ✅ exit **0** in 97 s |
| 4 | Adapter copies after the revise round | ✅ **22 workflow copies + 11 Codex skills, all in sync** — nothing drifted |
| 5 | Returned item 1 — the `UNDECLARED` sentence | ✅ replaced with the two-act rule **and a citation to §5**, plus the harm of the absolute reading. Exactly the form asked for |
| 6 | Returned item 2 — the miscount | ✅ *"The six keys that are never prose"* |
| 7 | Returned item 3 — four loose claims | ✅ all four, checked at the artifacts: `__pycache__` caveat now **at the row**; follow counts **9** and **6**, re-measured at the declared pin and I re-measured them too; ASCII check's reach described as what the code does; both parser measurements recorded with methods |
| 8 | The four sites the generalization found | ✅ stale `--validate` docstring; `parents[2]` in both test files → marker search; dead `TD-11` label dropped; and the CHANGELOG's historical paraphrase **deliberately kept**, with the exemption written down rather than silently taken |
| 9 | The new class check, replayed independently | ✅ **39 normative files, 20 templates, 13 workflows** — `templates/**/*.md` does reach `templates/status.md`, so it covers the file it exists for. Failing branch proven |
| 10 | **Template-move audit** — 137 references, both forms, whole live tree | See §2.1. **The three moved templates have zero stale live references.** One leftover in the canon, and three pre-existing drifts of the same class |

### 2.1 The template-move audit

I scanned **both** reference forms — `.tfw/templates/…` and the bare `templates/…` that half
the workflows use — across the payload, the adapters, the installed copies, the root documents
and `team/`. **137 references. Six broken targets.**

```
BROKEN, and CORRECT — the migration guide naming what a project must delete
  .tfw/migrations/2.0.0.md:65-66  → team_profile.md · journal_event.md · topic_file.md

BROKEN, and PRE-EXISTING since TFW-42 (7111ee2, v0.8.6) — verified at f14f744~1
  .tfw/glossary.md:238,241        → templates/research/gather.md      (is: 2_gather.md)
  .tfw/glossary.md:244            → templates/research/extract.md     (is: 3_extract.md)
  .tfw/glossary.md:247,250        → templates/research/challenge.md   (is: 4_challenge.md)
```

**Where each moved thing is now taken from — every site, all correct:**

| Artifact | Told to copy from | Sites |
|---|---|---|
| `team/{handle}.md` | `.tfw/templates/team/profile.md` | **7** — `init.md:123`, `update.md:124`, `migrations:158`, `team/README.md:18`, `conventions.md:28` and `:271`, and the template's own header |
| `knowledge/{topic}.md` | `.tfw/templates/knowledge/topic.md` | **5** — `workflows/knowledge.md:71` + 2 copies, `conventions.md:664`, `glossary.md:262` |
| `{task}/journal/{…}.md` | `.tfw/templates/journal/event.md` | **3** — `conventions.md:27` and `:270`, `project_config.yaml:27` |

**The docs site, checked because it is where a move usually leaves dead links:**
`gen_docs.py`'s backtick resolver is guarded by `if full_path.exists():`, so the **17
deliberately-preserved historical artifacts** naming a moved template render as inert code
rather than as links to nothing. Confirmed against a full build: **0 dead hrefs.** Nav nests
Reference → Templates → Team → Profile, mirroring Research, Review and Evidence, which already
nest. That part is clean.

**The one leftover:**

```
conventions.md:690  (§10.4, the naming rule)

    Markdown templates in `.tfw/templates/` also follow `lower_snake_case`:
    - `topic_file.md` (not `TOPIC_FILE.md`)
                ↑
      deleted by this phase — and census.md enumerated this exact line
      (the topic_file.md group lists :603 and :629; :603 was fixed, :629 was not)
```

Three mechanisms exist and the line falls between all of them: it has no `templates/` prefix,
so a path scan cannot see it; it is not a retired *wording*, so the new registry check does not
reach it; and the shipped path check only looks inside `adapters/`.

**Strangeness worth naming, none of it a defect:** three "knowledge" entries in one templates
directory meaning three different outputs (`KNOWLEDGE.md`, `knowledge/`, `knowledge_state.yaml`);
`evidence/EV.md` now the only uppercase file inside a template subdirectory; the split
reference form (`.tfw/templates/X` vs bare `templates/X`); and no workflow naming the journal
template, which is reachable only through `conventions.md` §4. All four are pre-existing shapes
the move made visible rather than created. The RF header's citation of `440d6fd` as the review
commit — it was `8e83b6d` — is a header slip, noted and not filed.

## 3. Judge

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | 14 of 15 AC halves, re-verified. AC-13 half two still ❌ UNMET, still the owner's — unchanged, and unchanged is correct |
| 2 | Purpose Check + design soundness | **(a) ✅ · (b) ✅** | **(a)** Serves DoD **19** — *"every instruction the release gives names something the receiving project actually has"* — with **NS1**. The harm the first pass found was that clause failing from inside: the payload stating two opposite rules about the same act, the absolute one in the file a person hand-authors from. Closed, along with three more of its shape. **(b)** strengthened: the phase gained a *structural* control where it had an intention, which is the **Structural Enforcement** value applied to its own failure mode |
| 3 | Tech debt documented | ✅ | Eight observations. #8 names what the new check cannot reach, why an allowlist would rot, that the harm is bounded because a receiving project never reads test files, and the candidate fix |
| 4 | Style & standards | ✅ *(was ⚠️)* | The finding that held this row is closed |
| 5 | Observations collected | ✅ | Filter re-applied; #8 survives it |
| 6 | RF completeness (§7-10) | ✅ | Two new fact candidates and S4, all three **attributed to the review** rather than claimed. §10 gives the round its own honest account |
| 7 | Evidence completeness | ✅ | 60 items, all resolve |
| 8 | Evidence sufficiency | ✅ *(was ⚠️)* | All four gaps closed and checked at the artifacts. `312dca9` deserves specific credit: refusing to adopt a reviewer's number, re-deriving it, disclosing the disagreement |
| 9 | Backward compatibility | ⚠️ | Code unchanged and clean. From the audit: three published docs URLs changed with no redirect, and `templates/knowledge/` beside `templates/KNOWLEDGE.md` merges two page directories in a build on a case-insensitive filesystem. Neither reaches a receiving project — `docs/` is not in the payload — and deployment always builds on `ubuntu-latest`, so the live site is correct. Filed, not returned |
| 10 | Safety | ✅ | Nothing in the round touches the destructive surface; test root resolution narrowed |

**Purpose Check outcome: Aligned ✅.** Reference set re-checked for internal consistency:
baseline Phase AA, DoD 19, DoF 10 and NS1 remain coherent. **No contract defect.**

## 4. Verdict

**✅ APPROVE**

On the goal and the value, which is what this pass was asked to weigh:

**The goal is served, and served in the way that mattered.** DoD 19 says every instruction the
release gives must name something the receiving project actually has. The first pass found the
twin of that clause failing — the payload stating one rule in the canon and its retired
opposite in the template a person hand-authors from. The value of Phase AA is that a project
holding nothing but `.tfw/` can act on it without being misled, and a payload that contradicts
itself spends exactly that value. It is now consistent, and consistency is enforced by
something that can reveal its own violation rather than by having been checked once.

**The round exceeded its brief in the right direction.** I returned one file, one line and four
wording corrections. What came back was the class: the executor ran the mechanic my own fact
candidate had named, found a stale `--validate` docstring in a test whose call site this phase
had just edited, found `parents[2]` still in the test files of the module that had stopped
depending on depth — which I had seen and failed to file — dropped a dead identifier from its
own release note, and *declined* to rewrite a historical changelog paraphrase, writing the
exemption down instead of taking it silently. Then it made the mechanic a test, stated its
reach, proved its failing branch, and filed what it cannot reach.

RF §8 S4 states the finding behind all of it: *"A phase that legislates against a failure mode
is the most likely place to commit it."* This phase's DoF names *"a check reported as passing
that never ran"* in four forms, and the review found four such claims — the author's own. That
is worth more to the project than the four line edits.

**On the template moves, which the owner asked about directly: they are clean.** 137 references
across both forms, the whole live tree — payload, adapters, installed copies, root documents.
The three moved templates have **zero** stale live references. Every place that tells a reader
where to take a thing from names the new path: seven sites for the participant profile, five
for the topic file, three for the journal event, all correct. The migration guide names the old
paths because naming them is its job. The docs generator is existence-guarded, so seventeen
deliberately-preserved historical artifacts render honestly instead of pointing at nothing.

**One leftover, and it is debt rather than a third round.** `conventions.md:690` illustrates the
template naming rule with `topic_file.md`, which this phase deleted — and `census.md` had
enumerated that exact line. Swapping the filename would leave a rule with **nine standing
counterexamples** among its own twenty subjects and, after this move, no live demonstrator of
`lower_snake_case` at all. Nine of those counterexamples predate the phase. The fix is §10.4
saying what the convention actually is, which is a naming decision and not a line edit inside a
delivery phase. Returning it would buy a patch and leave the rule wrong — and *«фиксы ради
фиксов»* is the thing this phase was corrected away from at R3.

**Nothing here is grounds for REJECT or a further REVISE.** Purpose is aligned, the contract is
coherent, the design is sound, the payload is self-consistent, and the five debt items are all
outside the instruction surface a receiving project reads.

### What approval does not cover

**AC-13 half two remains unmet and remains the owner's.** Phase AA's declared outcome is *a
project other than this one completes the update from the payload alone*, and the only run so
far was the author's own clone. Approving the work is not approving that claim. The phase
closes when a real external project is updated by its own operator and the result is filed at
task root as `FIELD-REPORT__TFW-60__second_external_update.md`.

**Next acts, in order:** `/tfw-docs` (TD-186 is its first item), `/tfw-knowledge` (nine RF
candidates plus one from this review), then `/tfw-release` for the `v2.0.0-dirty.2` tag the
executor correctly did not cut. The tag is now clear to cut: the payload it names no longer
contradicts its own release note.

## 5. Tech Debt Collected

The first pass filed TD-186 … TD-191 and they stand. TD-191's executor half is done — the dead
`TD-11` label is dropped from the release note — and its registry half is still open, correctly,
because `TECH_DEBT.md` is not the executor's file. Five new rows from this pass:

| # | Source | Severity | File | Description | Action |
|---|---|---|---|---|---|
| TD-192 | REVIEW TFW-60/AA rev2 §2.1 | Med | `.tfw/conventions.md`:690 | §10.4 illustrates the Markdown template naming rule with `topic_file.md`, deleted by TFW-60/AA. Enumerated in `census.md` (`:629`) and left unclosed while `:603` was fixed. Wider than the example: **9 of 20** Markdown templates contradict the rule (`HL.md`, `TS.md`, `RF.md`, `RES.md`, `ONB.md`, `REVIEW.md`, `KNOWLEDGE.md`, `RELEASE.md`, `evidence/EV.md`) and the rule's own exemption covers only project-root and `.tfw/` framework docs, which templates are not; after the move **no Markdown template demonstrates `lower_snake_case`** except the numbered `research/1_briefing.md`. Load-bearing: ONB N1 cited §10.4 to rule on `team_README.md` | ⬜ Open — → a scoped naming task. **Do not swap the filename alone**: that leaves the rule wrong about nine of its own subjects. §10.4 must state the convention that actually holds |
| TD-193 | REVIEW TFW-60/AA rev2 §2.1 | Med | `docs/scripts/test_integration.py` | **Nothing checks template references outside `adapters/`, and nothing checks the bare `templates/…` form at all.** `test_every_path_an_adapter_source_names_resolves` scans `.tfw/adapters/**` plus installed copies, prefixed form only. Workflows and canon use both forms — `init.md` writes `.tfw/templates/X`, `plan.md` writes bare `templates/X`. This is the mechanism gap that let TD-192 and TD-194 survive. A reviewer's independent scan of 137 references found 6 broken targets, 3 of them stale for four releases | ⬜ Open — highest value of this set. Fix shape: extend the executor's own retired-wording precedent — a registry, a stated reach, a proven failing branch — from *retired wordings* to *every path a payload file names*, in both reference forms |
| TD-194 | REVIEW TFW-60/AA rev2 §2.1 | Low | `.tfw/glossary.md`:238, 241, 244, 247, 250 | Five references to `templates/research/gather.md`, `extract.md`, `challenge.md`; the files gained numeric prefixes at TFW-42 (`7111ee2`, v0.8.6) and are `2_gather.md`, `3_extract.md`, `4_challenge.md`. **Pre-existing** — verified stale at `f14f744~1`, so not TFW-60/AA's doing. KNOWLEDGE D50 records the rename; the glossary never followed | ⬜ Backlog — closes as a side effect of TD-193's check, which is the reason to do that one first |
| TD-195 | REVIEW TFW-60/AA rev2 §2.1 | Low | `docs/scripts/gen_docs.py`, `docs/mkdocs.yml` | The template moves changed three published documentation URLs with no redirect: `reference/templates/team_profile/` → `reference/templates/team/profile/`, and likewise `journal_event` → `journal/event`, `topic_file` → `knowledge/topic`. No redirects plugin is configured. Nothing in the repository links to the old URLs, so the only loss is an outside bookmark. Recorded because page URLs are derived from source paths, so every future template move has this consequence | ⬜ Backlog — decide once whether published reference URLs are a stable surface. If yes, add `mkdocs-redirects`; if no, say so in `RELEASE.md` so it stops being a question |
| TD-196 | REVIEW TFW-60/AA rev2 §2.1 | Low | `docs/scripts/gen_docs.py` nav/URL derivation | **A docs build on a case-insensitive filesystem merges two template page directories.** Page paths come from the source subpath, so `templates/KNOWLEDGE.md` → `reference/templates/KNOWLEDGE/` and `templates/knowledge/topic.md` → `reference/templates/knowledge/topic/`. On Windows/macOS the second lands physically inside the first: verified locally, `topic/index.html` sits in `KNOWLEDGE/` while the search index advertises `knowledge/topic/`. `REVIEW.md` + `review/` already had this shape, so TFW-60/AA reproduced a latent defect rather than creating one. **The live site is unaffected** — `.github/workflows/docs.yml` always builds on `ubuntu-latest`. The bite is that a local preview is not what deploys | ⬜ Backlog — monitor. Candidate fix: case-fold or namespace the derived page path, or rename the flat `KNOWLEDGE.md`/`REVIEW.md` templates, which pairs naturally with TD-192 |

## 6. Traces Updated

- [x] the phase's `status.md` — `lifecycle: KNW` per ✅ APPROVE (`conventions.md` §5), with a `transition` event in the task's `journal/`
- [x] HL status — Phase AA's work is approved; the **phase does not close** until AC-13 half two lands, so no HL phase marker is flipped to complete
- [x] the phase's `status.md` — `updated` reflects this review; no counter incremented
- [x] Other project files — `TECH_DEBT.md` gains TD-192 … TD-196; `KNOWLEDGE.md:22` remains stale by design and is TD-186, `/tfw-docs`'s first item
- [ ] tfw-docs: **Pending** — run now. TD-186 first
- [ ] tfw-knowledge: **Pending** — nine RF candidates plus this review's one

## 7. Fact Candidates

> fact-candidates: processed 2026-08-30

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | process | **A move is verified by resolving every reference in every form the project actually writes, not in the form the checker happens to know.** Half this repository's workflows name a template as `.tfw/templates/X` and half as bare `templates/X`; the shipped path check validates only the first, and only inside `adapters/`. Scanning both forms across the whole live tree — 137 references — found six broken targets, three of them stale for four releases and one an enumerated census hit. The audit is cheap and it is the only thing that tells a move it is finished | Reviewer, this revision, prompted by the owner's question | High |

One only. The RF's nine are strong, its #8 and #9 already carry the class insight from the
first pass, and paraphrasing them here would make `/tfw-knowledge`'s job worse rather than
better.

---

*REVIEW — TFW-60 / Phase AA: Portable Delivery (revision 2) | 2026-08-28, reviewed at `312dca9`*
