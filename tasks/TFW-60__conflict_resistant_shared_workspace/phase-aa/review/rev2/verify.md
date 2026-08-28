# Verify — revision 2 — "Are the claims true?"
> **Mindset:** Auditor. The RF is a declaration, not a fact.
> **Scope:** the delta since `8e83b6d`, plus the audit the owner asked for.
> First pass stands: [`../verify.md`](../verify.md) — 100% of files, 60 evidence items, 33 citations.
> **Counts are deliberately not re-litigated this pass** (owner's instruction). D3 is recorded, not reopened.

## Part 1 — the three returned items

### V1: `.tfw/templates/status.md` — items 1 and 2
- **RF claim:** the retired absolute sentence replaced with the two-act rule, citing §5; *"six keys"*
- **Actual:** diffed `b44bf7d`. Line 92's *"Normalizing such a value to a declared one is
  prohibited."* is **gone**, replaced by *"MIGRATION NEVER NORMALIZES IT. AN ACCOUNTABLE OWNER
  MAY RESOLVE IT — by setting the correct value and recording a `transition` event carrying
  `from: UNDECLARED`"*, closing with *"Full rule and the two-act table: conventions.md §5"* —
  a citation, not a third copy of the table, which is what the item asked for. It also now
  names the harm of the absolute reading. Line 31 reads *"The six keys that are never prose"*
- **Match:** ✅

### V2: the four narrowed claims — item 3
- **Actual, each checked against the artifact rather than the RF's account of it:**
  **(a)** EV E47 now carries the transcript's own `1` and the `__pycache__` explanation at the
  row. **(b)** RF §1 states **9** and **6** and adds *"they were 8 and 5, the values at
  `80c2ed5`, taken before the third commit and then reported against a later pin"* — I
  re-measured: 9 and 6 at `1079020`. **(c)** RF §4 and D7 now describe the ASCII check as a
  `print(`/`SystemExit(` span scan that reaches a literal and not a message assembled into a
  variable — which is what the code does. **(d)** `ac3_parser_untouched.txt` records both
  measurements with both methods
- **Match:** ✅

### V3: `312dca9` — the number the executor refused to borrow
- **Actual:** the revise round nearly shipped my `42 → 47` as its own. Its own extraction gives
  `40 → 45`; the gap is trailing blank lines under a different function-boundary rule. Both
  artifacts now state method, measured number, and *"a number from someone else's run is not
  one they can vouch for."* The conclusion is unchanged under either count, and I confirm it:
  no row-reading line is touched
- **Match:** ✅ — and this is the right instinct. A reviewer's number is not evidence for an executor

### V4: the four sites the generalization found — not returned by the review
| # | Site | Verified |
|---|---|---|
| 4 | `.tfw/scripts/test_gen_index.py:741` docstring naming `--validate` as the build-gate command | ✅ now *"`gen_index.main(--check tasks)`"*. This phase moved the call's arguments and left the prose |
| 5 | `test_gen_index.py:20`, `test_migrate_board.py:22` — `parents[2]` | ✅ both now `find_project_root(Path(__file__))`, with the reason in a comment. **The first pass saw this and did not file it** — my own miss, correctly attributed in the RF |
| 6 | `.tfw/CHANGELOG.md` citing the non-existent `TD-11` | ✅ label dropped with the reason stated; the registry decision correctly left to `TECH_DEBT.md`, so **TD-191 stays open** |
| 7 | `.tfw/CHANGELOG.md:168`'s paraphrase of the absolute rule | ✅ **deliberately not changed**, and classified: a changelog records what a release shipped. Same P9 logic as the eleven provenance comments. The exemption is written down so the next person running the grep does not re-derive it |

### V5: the class check itself — `test_no_normative_file_states_a_retired_rule`
- **RF claim:** a registry of retired wordings checked against every payload file that instructs
- **Actual:** re-ran its glob independently. **39 normative files scanned, including all 20
  templates and 13 workflows** — `templates/**/*.md` does reach `templates/status.md`, so the
  check genuinely covers the file it was written for. `CHANGELOG.md` excluded as a rule with
  the reason in a comment; `adapters/` excluded because it has its own path check.
  `test_the_retired_rule_check_actually_fires` proves the failing branch
- **Match:** ✅ — a real mechanism, not a gesture. Its stated reach matches what it does

## Part 2 — the template-move audit the owner asked for

> Three templates moved: `team_profile.md → team/profile.md`, `journal_event.md → journal/event.md`,
> `topic_file.md → knowledge/topic.md`. The question: does everything that referenced them point
> right, is it clear where each is taken from, and did any dirt survive.

### Every template reference in the live tree, resolved

I scanned **both** reference forms — `.tfw/templates/…` and the bare `templates/…` the
workflows also use — across `.tfw/workflows/`, `.tfw/templates/`, `.tfw/migrations/`,
`conventions.md`, `glossary.md`, `README.md`, `quickstart.md`, `compilable_contract.md`,
`AGENTS.md`, `CLAUDE.md`, `team/README.md`, `.claude/commands/`, `.agent/workflows/`,
`.agents/skills/`.

**137 references scanned. Six broken targets:**

| Broken target | Where | Verdict |
|---|---|---|
| `templates/team_profile.md` · `templates/journal_event.md` · `templates/topic_file.md` | `.tfw/migrations/2.0.0.md:65–66` only | ✅ **correct and required.** The guide names the retired paths so the operator deletes them. Naming them is the deliverable |
| `templates/research/gather.md` · `extract.md` · `challenge.md` | `.tfw/glossary.md:238, 241, 244, 247, 250` | ❌ **five stale references — but PRE-EXISTING.** Verified at `f14f744~1`: already stale before this phase. The files gained numeric prefixes at TFW-42 (`7111ee2`, v0.8.6) and the glossary was never swept. Not this phase's defect; found by asking this phase's question |

**The three moved templates have zero stale live references anywhere.** Every creation site
names the new path:

| Artifact | Where a reader is told to take it from | Sites | All correct? |
|---|---|---|---|
| `team/{handle}.md` | `init.md:123` · `update.md:124` · `migrations/2.0.0.md:158` · `team/README.md:18` · `conventions.md:28, 271` · the profile template's own header | **7** | ✅ all name `.tfw/templates/team/profile.md` |
| `knowledge/{topic}.md` | `workflows/knowledge.md:71` (+2 copies) · `conventions.md:664` · `glossary.md:262` | **5** | ✅ all name `.tfw/templates/knowledge/topic.md` |
| `{task}/journal/{…}.md` | `conventions.md:27, 270` · `project_config.yaml:27` | **3** | ✅ all name `.tfw/templates/journal/event.md` |

### The one leftover — **`conventions.md:690`** · DISCREPANCY

```
Markdown templates in `.tfw/templates/` also follow `lower_snake_case`:
- `topic_file.md` (not `TOPIC_FILE.md`)
```

§10.4's naming rule illustrates itself with a file **this phase deleted.** It is not a path
reference — no `templates/` prefix — so neither my path scan nor the shipped adapter path
check can see it, and it is not a *retired wording*, so the new registry check does not reach
it either. Three mechanisms, and the line falls between all of them.

**It was enumerated.** `census.md` lists conventions.md's `topic_file.md` group at
`:603` and **`:629`**. `:603` (the §10.2 table) was fixed; `:629` — now `:690` — was not.

The damage is wider than one dead example, and this is why it is debt rather than a one-word
edit:

| | State |
|---|---|
| The rule's only Markdown example | a deleted file |
| Markdown templates that obey `lower_snake_case` | after the move, **not one has an underscore** except `research/1_briefing.md`, a numbered stage. The rule has no live demonstrator |
| Markdown templates that contradict it | **9 of 20** — `HL.md`, `TS.md`, `RF.md`, `RES.md`, `ONB.md`, `REVIEW.md`, `KNOWLEDGE.md`, `RELEASE.md`, `evidence/EV.md`. The rule's own exemption covers project-root and `.tfw/` framework docs; templates are neither |
| Load-bearing? | Yes — ONB N1 cited §10.4 to rule on `team_README.md` |

Nine of those counterexamples predate the phase. So the correct fix is a §10.4 rewrite stating
what the convention actually is, not swapping one filename — which is a scoped naming task,
not a line in a delivery phase.

### Where the templates go in the docs site

`gen_docs.py` walks `.tfw/templates/**/*.md` and derives both the page URL and the nav key
from the subpath. Two consequences, both checked:

- **No broken links are generated.** The backtick resolver is guarded by
  `if full_path.exists():` (`gen_docs.py:566`), so a historical artifact naming
  `` `.tfw/templates/team_profile.md` `` renders as inert `<code>` rather than a dead href.
  Confirmed empirically against a full build: **0 files** contain a link to an old template
  URL. This matters, because the phase deliberately preserved 17 `tasks/` artifacts naming a
  moved template — they render honestly rather than pointing at nothing
- **Three published page URLs changed** with no redirect: `reference/templates/team_profile/` →
  `reference/templates/team/profile/`, and likewise for the other two. No redirects plugin is
  configured. Nothing in the repository links to the old URLs; an outside bookmark would 404
- **Nav nests correctly:** Reference → Templates → Team → Profile, mirroring the Research,
  Review and Evidence groups that already nest. Consistent with the shape the move adopted

### Strangeness worth naming, none of it a defect

| Observation | Read |
|---|---|
| `templates/KNOWLEDGE.md` · `templates/knowledge/` · `templates/knowledge_state.yaml` — three "knowledge" entries, three different outputs (root index · verified-fact topics · consolidation state) | The `REVIEW.md` + `review/` pair already had this shape and has confused nobody. `knowledge_state.yaml` is the one that reads as if it belonged *inside* `knowledge/` when it goes to `.tfw/`. Cosmetic |
| `evidence/EV.md` is the only **uppercase** file inside a template subdirectory — `journal/event.md`, `knowledge/topic.md`, `team/profile.md`, `review/map.md` are all lowercase | Pre-existing; the move makes it visible as the outlier. Belongs with the §10.4 rewrite, not on its own |
| Reference form is split: `init.md`, `update.md`, `knowledge.md`, `handoff.md` write `.tfw/templates/X`; `plan.md`, `review.md`, `research/base.md` write bare `templates/X` | Both resolve for a reader. But the shipped path check only validates the `.tfw/`-prefixed form **and only inside `adapters/`** — which is exactly why one enumerated census hit and five TFW-42 leftovers survived. This is the gap, not the split |
| No workflow names `templates/journal/event.md`; it is reachable only through `conventions.md` §4 | Pre-existing and unchanged by the move. `team/profile.md` is named in the workflow that creates it; the journal template is not. Asymmetry, not breakage |
| RF header says *"after REVIEW `440d6fd` returned 🔄 REVISE"* | `440d6fd` is the executor's own earlier commit; the review landed at `8e83b6d`. A citation slip in a header, corrected by pointing at it here |

## Commands Executed

| # | Command | Result |
|---|---------|--------|
| 1 | `pytest .tfw/scripts/ docs/scripts/ -q` | **255 passed, 1 skipped** in 155.8 s — matches the RF exactly; +2 over the first pass's 253 |
| 2 | `--check index` · `--check tasks` · `--check project` | **exit 0** each |
| 3 | `cmp` over 22 workflow copies + 11 Codex skills | **all in sync** after the revise round — no copy drifted |
| 4 | `python -m mkdocs build` | re-run at HEAD (the 95-test `docs/scripts/` suite inside (1) drives mkdocs builds and passed) |
| 5 | independent resolver over 137 template references, both forms, whole live tree | 6 broken targets — 3 deliberate, 3 pre-existing. Detailed above |
| 6 | independent glob replay of `NORMATIVE_GLOBS` | **39 files, 20 templates, 13 workflows** — the class check reaches `templates/status.md` |
| 7 | `git show f14f744~1:.tfw/glossary.md` | the five `research/` stale refs pre-date the phase |
| 8 | `git log --follow` at `1079020` | 9 and 6 — the RF's corrected figures are right |

## Claim & Source Checks

| # | Claim checked | Traces to | Holds? |
|---|---|---|---|
| C1 | *"255 passed 1 skipped"* (`b44bf7d` message) | re-run: 255 passed, 1 skipped | ✅ |
| C2 | *"the class is now a test proven against the pre-fix file rather than against a fixture alone"* | `test_the_retired_rule_check_actually_fires` proves the branch; the registry's first entry is the exact sentence that was in the pre-fix template | ✅ |
| C3 | *"my own extraction gives 40 → 45; the gap is trailing blank lines"* | my own run gave 42 → 47 under a different boundary rule. Both artifacts now state their method. The row-reading lines are byte-identical under either | ✅ — and the disagreement is disclosed rather than papered over |
| C4 | RF §6 obs. 8: the class check *"does not scan the payload scripts' own comments and docstrings"* | confirmed: `NORMATIVE_GLOBS` has no `scripts/` entry, and item 4 was found by hand | ✅ accurate self-report |
| C5 | RF §10 item 7: the CHANGELOG paraphrase is *"a paraphrase, so the exact-string grep does not reach it"* | `:168` reads *"normalizing it away is prohibited"* — not the registry string. Correct | ✅ |

## Discrepancies Found

| # | Discrepancy | Severity |
|---|---|---|
| **E1** | `conventions.md:690` — §10.4 illustrates the template naming rule with `topic_file.md`, deleted by this phase; an enumerated census hit (`:629`) left unclosed. Compounded by 9 standing counterexamples and no surviving demonstrator | **Medium** — debt, not a round |
| **E2** | `glossary.md:238–250` — five references to `templates/research/{gather,extract,challenge}.md`; the files are `2_gather.md`, `3_extract.md`, `4_challenge.md`. **Pre-existing since TFW-42** | Low — debt |
| **E3** | Nothing checks template references outside `adapters/`, and nothing checks the bare `templates/…` form at all. This is the mechanism gap that let E1 and E2 survive | Medium — debt, and the one worth fixing first |
| **E4** | Three published docs URLs changed with no redirect | Low — debt |
| **E5** | RF header cites `440d6fd` as the REVIEW commit; the review landed at `8e83b6d` | Trivial — noted, not filed |

**No escalation.** The first pass already ran at 100%; this pass re-verified the delta, the
whole template reference surface, and every claim in the revise round. Nothing found in the
delta is false.

## Evidence Verification — delta

| # | RF Evidence ref | Artifact exists? | Matches claim? |
|---|---|---|---|
| E13 | `ac3_parser_untouched.txt` | ✅ | ✅ both measurements with both methods, and why a borrowed number was not used |
| E47 | `fixture_run.txt` + `fixture_report.md` | ✅ | ✅ the `__pycache__` caveat is now **at the row** |
| E51 | AC-13 half two | — | ✅ **still DEFERRED, still the owner's.** Unchanged and correctly so |
| E60 | ASCII class check | ✅ | ✅ reach stated to match the code |
| new | `test_no_normative_file_states_a_retired_rule` + its fires-test | ✅ | ✅ replayed independently: 39 files, reach as stated |

## Knowledge Citations Verified — delta

No new citations. HL §7.2 and ONB §7 are unchanged; the first pass verified 33 of 33 with 0
hallucinated. Revision 2 adds two RF fact candidates (#8, #9) and one strategic insight (S4),
all sourced to this review — checked, and all three are attributed to the reviewer rather than
claimed as the executor's own.

## Checkpoint

**Self-check:**
- [x] Opened files and recorded findings? — the four changed payload files, both test files, the new test in full, plus an independent scan of 137 template references
- [x] Ran build/test commands? — 8, including the full suite, three check subjects, the `cmp` sweep, and two independent replays of the executor's own mechanisms
- [x] Claim & Source Checks filled? — C1–C5, each re-derived
- [x] Each returned item verified against the actual file, not the RF's account?
- [x] The owner's audit question answered end to end? — 137 references, both forms, whole live tree; docs URLs and nav; the four strangenesses named with a read on each
- [x] Counts deliberately not re-litigated, per the owner's instruction — D3 recorded as the RF now states it, and not reopened

Stage complete: YES
