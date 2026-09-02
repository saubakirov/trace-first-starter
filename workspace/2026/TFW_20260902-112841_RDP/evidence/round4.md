# round4.md — raw output behind EV rows E25–E28

> **Date**: 2026-09-02 · **Author**: Claude Code (Executor), on behalf of `saubakirov`
> Every block below is pasted from a command run in this session, from the project root, in Git Bash.
> Nothing is retyped from memory. Diffs are `git diff 3c998ea 1a9059b` — round 3's delivery against
> round 4's — so what round 4 changed is separable from what round 3 changed.

---

## §0 — item 1's gate first: the third assertion fails against the old expression

The order's own words: *"the third assertion shown failing against the old regex — a test that cannot
fail against the bug it guards has not been tested."* Two proofs, in increasing strength.

**Proof 1 — the nine probes, old expression against new.** `want` is what the naming rule requires:
a doubled slug fires, the one mandated ordinal does not.

```text
probe                                  want  old   new
{container}/{YYYY}/{ID}__tfw_init/     True  True  True
TS__{ID}__draft.md                     True  True  True
TS__{ID}__rev{N}__extra.md             True  False True    <-- OLD WRONG
TS__{ID}__rev{N}_draft.md              True  False True    <-- OLD WRONG
TS__{ID}__rev{N}-final.md              True  False True    <-- OLD WRONG
RES__{ID}__iter2.md                    True  True  True
RES__{ID}.md                           False False False
TS__{ID}__rev{N}.md                    False False False
REVIEW__{ID}__rev{N}.md                False False False

mismatches: old=3  new=0
```

Three names escape the old expression, all of them a suffix hidden **after** the mandated ordinal. The
review probed the same nine and reported the same result; this is an independent re-run, not a quotation.

**Proof 2 — the assertion actually run under the old expression.** The regex was reverted in place, the
one test invoked, and the file restored from a copy taken beforehand. This is the proof that matters: a
regex comparison shows the expressions differ, but only running the assertion shows the *test* can fail.

```text
$ python -m pytest docs/scripts/test_integration.py::test_the_naming_detectors_actually_fire -q

947:DOUBLED_SLUG = re.compile(r"\{ID\}__(?!rev\{N\})")
        assert DOUBLED_SLUG.search("{container}/{YYYY}/{ID}__tfw_init/")
        assert DOUBLED_SLUG.search("TS__{ID}__draft.md")
>       assert DOUBLED_SLUG.search("TS__{ID}__rev{N}__extra.md")  # a suffix AFTER the ordinal
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       AssertionError: assert None
E        +  where None = <built-in method search of re.Pattern object at 0x...>('TS__{ID}__rev{N}__extra.md')
E        +    where <built-in method search ...> = re.compile('\\{ID\\}__(?!rev\\{N\\})').search

docs\scripts\test_integration.py:992: AssertionError
=========================== short test summary info ===========================
FAILED docs/scripts/test_integration.py::test_the_naming_detectors_actually_fire
1 failed in 133.15s (0:02:13)
```

**And the offender scan, both ways.** `test_no_canonical_example_doubles_the_slug` reports **0 offenders**
under the old expression and **0 under the new** — the tightening costs the canonical surface nothing,
which is why it is a repair rather than a widening in the other direction. Both figures are inside the
322-passed run in §4.

---

## §1 — item 1: the change, in full

```diff
diff --git a/docs/scripts/test_integration.py b/docs/scripts/test_integration.py
index cc561f6..8728fa0 100644
--- a/docs/scripts/test_integration.py
+++ b/docs/scripts/test_integration.py
@@ -938,9 +938,13 @@ BARE_ID_AS_NAME = re.compile(
 #: exception, and `conventions.md` §4 mandates it: `__rev{N}`, the revision ordinal. A title
 #: suffix duplicates what `status.md` already holds, so it stays refused; an ordinal lives
 #: nowhere else, so the filename is its only home. Anything else after `{ID}__` still fires.
-#: The two assertions below pin that exception — without them, widening this regex is the one
-#: way the naming rule can be broken by a change that reports itself as passing.
-DOUBLED_SLUG = re.compile(r"\{ID\}__(?!rev\{N\})")
+#: The lookahead spells `rev{N}.md`, not `rev{N}`, because the ordinal must **end** the name:
+#: `rev{N}` alone only asks what follows `{ID}__`, so `TS__{ID}__rev{N}__extra.md` slipped past
+#: it — a suffix hidden behind the one mandated exception. The three assertions below pin the
+#: exception from both directions, before the ordinal and after it; without the third, widening
+#: this regex is the one way the naming rule can be broken by a change that reports itself as
+#: passing.
+DOUBLED_SLUG = re.compile(r"\{ID\}__(?!rev\{N\}\.md)")
 
 #: An event example with only two segments has no actor, and two writers recording the same
 #: kind in the same second would collide on it.
@@ -985,6 +989,7 @@ def test_the_naming_detectors_actually_fire(tmp_path):
     assert BARE_ID_AS_NAME.search("HL-20260826-143000.md")
     assert DOUBLED_SLUG.search("{container}/{YYYY}/{ID}__tfw_init/")
     assert DOUBLED_SLUG.search("TS__{ID}__draft.md")
+    assert DOUBLED_SLUG.search("TS__{ID}__rev{N}__extra.md")  # a suffix AFTER the ordinal
     assert ACTORLESS_EVENT.search("20260826-143000__created.md")
     assert ACTORLESS_EVENT.search("{YYYYMMDD-HHMMSS}__{kind}.md".replace("{kind}", "handoff"))
 
```

**The expression changed by four characters, not three.** REVIEW revision 3 and TS revision 4 both call
it *"three characters"*; the addition is `\.md` — backslash, dot, `m`, `d` — which is four. Counted
because a claim of exactness should itself be exact, and nothing about the repair depends on which
figure is right. Everything else in the block is the reason those four characters are there, written so
the next person who shortens the lookahead meets an argument instead of a bare pattern.

**The other three detectors and both surviving negatives are untouched.** Two hunks, at 938 and 989:
`BARE_ID_AS_NAME`, `ACTORLESS_EVENT`, `STAMP` and `BACKTICKED` appear in the diff only as context lines,
and `assert not DOUBLED_SLUG.search("RES__{ID}.md")` and
`assert not DOUBLED_SLUG.search("TS__{ID}__rev{N}.md")` are outside both hunks entirely — the surviving
positive the ONB checked in round 3 still fires, proven by the 322-passed run.

---

## §2 — items 2 and 3: the gates, before and after

**Item 2's gate**, verbatim from the order: `grep -n "Step [0-9]" .tfw/glossary.md` returns no
`handoff.md` step number.

Before (`3c998ea`), two hits naming a `handoff.md` step number:

```text
206: … at execution time, not at review. → `handoff.md` Phase 2 Step 8
215: Step 0 convention present in every TFW workflow … → `handoff.md` Step 0, `plan.md` Step 0, `review.md` Step 0
```

After (`1a9059b`), one hit remains:

```text
215: Step 0 convention present in every TFW workflow … → `handoff.md` Step 0, `plan.md` Step 0, `review.md` Step 0
```

**The gate is reported as it ran, not as it was hoped to run.** Line 215 survives and is a live
`handoff.md` step number. It was left deliberately, and the reasoning is ONB §10.5 item 2: it did not
drift (the renumbering moved steps 8–13; Step 0 is unmoved), it is a real heading — `## Step 0: Name This
Session` — so it is an anchor rather than a count, the glossary term itself *is* *"Step 0 convention"*, and
de-numbering it would rewrite the term and reach `plan.md` and `review.md`, which this round does not open.
REVIEW revision 3 read this file and proposed only `Execution Loop`. **Judgement, not a pass** — and the
reviewer may overrule it.

**Item 3's gate**: a project-wide search for `handoff` step numbers returns only history. Run over
`*.md`, excluding the task containers and the gitignored build:

```text
$ git grep -n "handoff[^|]\{0,40\}Step [0-9]\|Step [0-9][^|]\{0,40\}handoff" \
      -- '*.md' ':!workspace' ':!tasks' ':!site'

.tfw/CHANGELOG.md:1425   → entry [0.9.0]  2026-07-22   HISTORY
.tfw/CHANGELOG.md:1441   → entry [0.8.8]  2026-07-07   HISTORY
.tfw/CHANGELOG.md:1477   → entry [0.8.5]  2026-04-20   HISTORY
.tfw/CHANGELOG.md:1479   → entry [0.8.5]  2026-04-20   HISTORY
.tfw/CHANGELOG.md:1492   → entry [0.8.5]  2026-04-20   HISTORY
.tfw/CHANGELOG.md:1686   → entry [0.7.0]  2026-04-04   HISTORY
.tfw/glossary.md:215     → `Session Naming`, Step 0     LIVE — classified above, left deliberately
KNOWLEDGE.md:147         → §2's TFW-46 row              HISTORY — named by the order as not to be repaired
```

Each version header was read by walking back from the hit to the nearest `## [` line, not assumed from
the line number. **Eight hits, six of them in released entries, one named by the order as history, one
live and classified.**

The two repairs themselves:

```diff
-… at execution time, not at review. → `handoff.md` Phase 2 Step 8
+… at execution time, not at review. → `handoff.md` Phase 2, *Implement*
```

```diff
-executor collects evidence (RF §5 Evidence table, handoff Step 11)
+executor collects evidence (RF §5 Evidence table, handoff *Collect evidence*)
```

Both name the step the entry actually means. Step 8 is now *Run tests* and step 11 is now *Pre-RF Gate*,
so both citations resolved to a real but different step — which is the worst shape, because a reader is
misled rather than stopped.

**`KNOWLEDGE.md` — nothing else touched**, measured rather than asserted:

```text
$ git diff --stat 3c998ea 1a9059b -- KNOWLEDGE.md
 KNOWLEDGE.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

One line. §2's `TFW-46` row and the released 2.0.x entries are untouched.

---

## §3 — item 4: the gate, and what the record does and does not claim

**`git grep -n "build.verify"`, excluding the task containers and the build:**

```text
.tfw/CHANGELOG.md:340   the 2.1.0 `Removed` bullet — THIS ROUND
.tfw/CHANGELOG.md:352   the same bullet's receiver instruction — THIS ROUND
.tfw/CHANGELOG.md:354   the same bullet's "keep it if it names something of your own" — THIS ROUND
.tfw/CHANGELOG.md:457   the 2.1.0 `Known open` bullet's cross-reference — THIS ROUND
.tfw/CHANGELOG.md:511   entry [2.0.0], 2026-08-30                        HISTORY
.tfw/CHANGELOG.md:1078  entry [2.0.0-dirty], 2026-08-27                  HISTORY
.tfw/CHANGELOG.md:1150  entry [2.0.0-dirty], 2026-08-27                  HISTORY
.tfw/migrations/2.0.0.md:302  the 2.0.0 migration guide                  HISTORY
```

**Neither `project_config.yaml` holds the key** — the removal is real, and it was the coordinator's, in
`859dc74`. Verified independently of the order's account:

```text
$ git show --stat 859dc74 | grep -E "project_config|RF.md|test_gen_index"
 .tfw/project_config.yaml               |  4 +-
 .tfw/scripts/test_gen_index.py         | 12 +-
 .tfw/templates/RF.md                   |  1 -
 .tfw/templates/project_config.yaml     |  8 +-
```

**What the record claims, checked line by line against the order's three bullets:**

| The order requires | Where it is, and its words |
|---|---|
| `build.verify` **gone from the shipped template** | `Removed`: *"Gone from `.tfw/project_config.yaml` and from `.tfw/templates/project_config.yaml`, so no new project inherits it"* |
| the `Verify` line gone from `templates/RF.md` | the same bullet: *"the `Verify` reporting line from `.tfw/templates/RF.md`, whose only reader was that key"* |
| **a receiver should remove its own** `build.verify` | the same bullet: *"if your own `project_config.yaml` carries a `build.verify` that names this check, **remove it**"*, with the mechanism — *"`build.*` is a PROJECT section an update preserves, so nobody rewrites your key for you and this entry is the only thing that can tell you"* |
| **why**, in one sentence | *"a never-authoritative view must not stand in a blocking check, because one malformed line in one task then stops every unrelated run"* |
| it does **not** claim the event was repaired | `Known open at this tag`: *"One journal event in this repository's own corpus is over the summary ceiling, **and it was not repaired**"* — the event is named, the figure is given, and the owner's ruling that it is not edited and the ceiling is not moved is stated |

**The event, measured here rather than quoted from the review:**

```text
$ python  # over every journal event in workspace/ and tasks/
events with a summary: 116
over 120: 1
   123  workspace/2026/TFW_20260902-112841_RDP/journal/20260902-181437__amendment_escalated__531a.md

$ python .tfw/scripts/gen_index.py --check tasks ; echo $?
… : summary is 123 code points, ceiling is 120; move the content into an artifact and reference it
… : goal exceeds 160 code points
2 problem(s) across 61 tasks
1
```

**Two figures against my own draft, both corrected before the commit.** The first draft of the `Known
open` bullet said *"the only such event in 56 tasks"*. Both halves were wrong to write: the corpus is
**61** tasks, not 56 (56 is the 2.1.0 `Verification` block's release-prep measurement, left untouched by
round 3's *no other locator* bar), and `--check tasks` reports **2** problems, not 1 — the second is
`workspace/2026/TFW_20260902-222456_RTBO/status.md`, *goal exceeds 160 code points*, a task another
session opened at 22:24, an hour after the order was written. **A shipped entry must not assert a number a
neighbouring task can falsify.** The bullet now quotes the one figure that cannot drift — 1 event over the
ceiling of the 116 carrying a summary — and says plainly that the check reports *"alongside whatever else
the corpus holds at the time you run it."*

---

## §4 — the suite, and the things not touched

```text
$ python -m pytest .tfw/scripts/ docs/scripts/ -q
........................................................................ [ 22%]
........................................................................ [ 44%]
...............................................s........................ [ 66%]
........................................................................ [ 89%]
...................................                                      [100%]
322 passed, 1 skipped in 158.32s (0:02:38)
```

**322 passed, 1 skipped** — the figure the order names, unchanged by this round. Round 3 closed at
*1 failed, 321 passed, 1 skipped*; the failure went with the gate in `859dc74`, before this round began,
and nothing here moved it.

**Every forbidden path diffed byte-for-byte, against the right reference.** The reference is `859dc74` —
the state of the tree when round 4 was dispatched — not the HL contract baseline `1c7b55e`, because
`review.md`, `handoff.md`, `templates/REVIEW.md` and `conventions.md` all differ from `1c7b55e` by rounds
1–3's own approved deliveries. **A byte-identity claim measured from the wrong revision would have read as
a violation, and the first draft of this file made exactly that mistake before the diff was run.**

```text
$ for f in …; do git diff --quiet 859dc74 HEAD -- "$f" && echo "BYTE-IDENTICAL  $f" || echo "CHANGED!!  $f"; done

BYTE-IDENTICAL  .tfw/scripts/gen_index.py
BYTE-IDENTICAL  workspace/…/journal/20260902-181437__amendment_escalated__531a.md
BYTE-IDENTICAL  .tfw/workflows/review.md
BYTE-IDENTICAL  .tfw/workflows/handoff.md
BYTE-IDENTICAL  .tfw/templates/REVIEW.md
BYTE-IDENTICAL  .tfw/conventions.md
BYTE-IDENTICAL  .tfw/project_config.yaml
BYTE-IDENTICAL  .tfw/templates/project_config.yaml
BYTE-IDENTICAL  .tfw/templates/RF.md
BYTE-IDENTICAL  .tfw/scripts/test_gen_index.py
```

`.tfw/conventions.md` byte-identical covers both §4's immutability clause and §5 without needing a
section-level argument. The last four rows are the coordinator's un-gating from `859dc74`: **this round
neither extended it nor undid it**, which is what item 4 being *a record and not a repair* means in the
diff. `.tfw/scripts/` as a whole: no file under it appears in either of this round's commits.

**The whole of what round 4 changed**, so nothing hides in a range:

```text
$ git diff --name-only 859dc74 HEAD

.tfw/CHANGELOG.md                                         ← item 3 + item 4
.tfw/glossary.md                                          ← item 2
KNOWLEDGE.md                                              ← item 3
docs/scripts/test_integration.py                          ← item 1
workspace/…/TFW_20260902-112841_RDP/ONB…md                ← §10, appended
workspace/…/TFW_20260902-112841_RDP/journal/20260902-223246__handoff__207d.md
workspace/…/TFW_20260902-112841_RDP/status.md
workspace/…/TFW_20260902-175227_RCFR/…  (4 files)         ← ANOTHER SESSION, not mine
workspace/…/TFW_20260902-222456_RTBO/…  (3 files)         ← ANOTHER SESSION, not mine
```

Four modification targets across four files, as the order's budget states, plus this task's own three
trace files. The seven remaining paths are two other sessions' commits inside the same range and appear
in no commit of mine — `git show --stat` on `b8d4b3c` and `1a9059b` lists seven files between them and no
eighth.

**No `cmp` step, and the reason rather than the omission.** None of the four files this round changes is
adapter-installed: `docs/scripts/` is repository tooling, and `CHANGELOG.md`, `glossary.md` and
`KNOWLEDGE.md` are read in place, not copied into `.claude/commands/` or `.agent/workflows/`. The adapter
drift check has nothing to compare, so it was not run.

**The shared working tree.** Three sessions committed during this round. Every commit here used
`git commit --only` with explicit paths, and `git status` was read whole beforehand. `.gitignore` is
dirty and belongs to another session; it is in no commit of mine. Two unrelated commits landed
mid-round — `8646892` (a new task, `TFW_20260902-222456_RTBO`) and `c9ef13c` (another task's research
iteration) — and neither touched any file this round opens, checked per file with `git log -1 -- <path>`.

---

*round4.md — TFW_20260902-112841_RDP: Review Decision Protocol | 2026-09-02*
