# round3.md — raw output behind EV rows E19–E24

> **Date**: 2026-09-02 · **Author**: Claude Code (Executor), on behalf of `saubakirov`
> Every block below is pasted from a command run in this session, from the project root, in Git Bash.
> Nothing is retyped from memory.

---

## §1 — item 1: the detector learns the one admitted suffix, and the exception is asserted

The change, in full:

```
@@ -931,14 +931,19 @@ BACKTICKED = re.compile(r"`([^`" + chr(10) + r"]+)`")
 BARE_ID_AS_NAME = re.compile(
     r"(?:/" + STAMP + r"(?:/|$)"                       # a path segment
     r"|(?:^|/)(?:HL-|[A-Z]+__)" + STAMP + r"\.md"      # an artifact filename
     r"|(?:^|/)" + STAMP + r"/)"                        # a directory
 )
 
-#: `{ID}` already ends in the slug, so anything appended doubles it.
-DOUBLED_SLUG = re.compile(r"\{ID\}__")
+#: `{ID}` already ends in the slug, so anything appended doubles it — with exactly one
+#: exception, and `conventions.md` §4 mandates it: `__rev{N}`, the revision ordinal. A title
+#: suffix duplicates what `status.md` already holds, so it stays refused; an ordinal lives
+#: nowhere else, so the filename is its only home. Anything else after `{ID}__` still fires.
+#: The two assertions below pin that exception — without them, widening this regex is the one
+#: way the naming rule can be broken by a change that reports itself as passing.
+DOUBLED_SLUG = re.compile(r"\{ID\}__(?!rev\{N\})")
 
 #: An event example with only two segments has no actor, and two writers recording the same
 #: kind in the same second would collide on it.
 #: The kind may contain a single underscore (`ownership_changed`) but never a double one:
 #: `__` is the segment separator, so `[a-z_]+` would swallow the actor and call a correct
 #: three-segment name actorless. The detector's own self-check caught exactly that.
@@ -976,19 +981,21 @@ def test_the_naming_detectors_actually_fire(tmp_path):
     repeatedly been damaged by checks reported as passing that never ran.
     """
     assert BARE_ID_AS_NAME.search("workspace/2026/20260826-143000/")
     assert BARE_ID_AS_NAME.search("RES__20260826-143000.md")
     assert BARE_ID_AS_NAME.search("HL-20260826-143000.md")
     assert DOUBLED_SLUG.search("{container}/{YYYY}/{ID}__tfw_init/")
+    assert DOUBLED_SLUG.search("TS__{ID}__draft.md")
     assert ACTORLESS_EVENT.search("20260826-143000__created.md")
     assert ACTORLESS_EVENT.search("{YYYYMMDD-HHMMSS}__{kind}.md".replace("{kind}", "handoff"))
 
     # and the legitimate forms must NOT fire
     assert not BARE_ID_AS_NAME.search("created: 20260819-000000")
     assert not BARE_ID_AS_NAME.search("workspace/2026/20260826-143000__query_redesign/")
     assert not DOUBLED_SLUG.search("RES__{ID}.md")
+    assert not DOUBLED_SLUG.search("TS__{ID}__rev{N}.md")
     assert not ACTORLESS_EVENT.search("20260826-143000__created__saubakirov.md")
 
 
 def test_no_canonical_example_uses_a_bare_identifier_as_a_name():
     """AC-14 items 4 and 5. A bare stamp cannot name exactly one task."""
     offenders = _offenders(BARE_ID_AS_NAME)
```

**The suite, before and after — two full runs, both from the gate the order names.**

```
$ python -m pytest .tfw/scripts/ docs/scripts/ -q     # before
2 failed, 320 passed, 1 skipped in 181.53s (0:03:01)

$ python -m pytest .tfw/scripts/ docs/scripts/ -q     # after
1 failed, 321 passed, 1 skipped in 164.65s (0:02:44)
```

**The twelve former offenders, re-run through the shipped detector** — the list is now empty, and the
same call is what produced the twelve in round 2:

```
DOUBLED_SLUG offenders on the canonical surface: 0

the pattern now: \{ID\}__(?!rev\{N\})

exception admitted   TS__{ID}__rev{N}.md       -> False
exception admitted   REVIEW__{ID}__rev{N}.md   -> False
DELIBERATE NEGATIVE  TS__{ID}__draft.md        -> True
DELIBERATE NEGATIVE  TS__{ID}__revision2.md    -> True
DELIBERATE NEGATIVE  HL-{ID}__approved.md      -> True
surviving positive   {container}/{YYYY}/{ID}__tfw_init/ -> True

the other three detectors, exercised unchanged:
  BARE_ID_AS_NAME  offenders on the canonical surface: 0
  ACTORLESS_EVENT  offenders on the canonical surface: 0
  BACKTICKED       is the extractor every detector runs through; exercised by the three above

phase forms never contain the literal {ID}__, so they were never in this detector's scope:
  TS__phase-{x}__{title}__rev{N}.md        contains "{ID}__" -> False
  REVIEW__phase-{x}__{title}__rev{N}.md    contains "{ID}__" -> False
```

---

## §2 — item 2: step 7 is deleted, and the renumbering reaches its two readers

Phase 2 and Phase 3 as they now read:

```
## Phase 2: Execution
7. **Implement** — follow TS step by step:
8. **Run tests** — as specified in TS verification section
9. **Build gate** — run build/compile command from TS verification section.
10. **Collect evidence** — create the evidence folder and populate the EV file:
## Phase 3: Write RF
11. **Pre-RF Gate** — open `.tfw/templates/RF.md`. Read all section headings before writing anything. Then w
12. **Create RF file** — use `.tfw/templates/RF.md` as canonical format. MANDATORY sections:
13. **Set the task's own state** — `lifecycle: RF` in `{task}/status.md`, with a `transition` event in `{tas
```

No state is set that is not true when it is set: `ONB` at the end of Phase 1 covers the whole leg, and the
`RF` transition is the last step of Phase 3, after the RF file exists.

```
99:6. **Set the task's own state** — `lifecycle: ONB` and `updated` in `{task}/status.md`, and append a `handoff` event to `{tas
141:13. **Set the task's own state** — `lifecycle: RF` in `{task}/status.md`, with a `transition` event in `{task}/journal/`, th
```

The two `glossary.md` citations, de-numbered:

```
-The executor activity in handoff.md Step 11 (between bui [...] ave Evidence fields — step is skipped entirely. → `handoff.md` Step 11
+The executor activity in `handoff.md` **Collect evidence [...]  fields — step is skipped entirely. → `handoff.md`, *Collect evidence*
-Executor gate in `handoff.md` Phase 3: before writing th [...] e RF drift failure mode observed in HD-9. → `handoff.md` Phase 3 Step 11
+Executor gate in `handoff.md` Phase 3: before writing th [...] ift failure mode observed in HD-9. → `handoff.md` Phase 3, *Pre-RF Gate*
```

**The file must end shorter, and it does:**

```
file                                 before    after  ceiling
.tfw/workflows/handoff.md              1730     1727     1200
.tfw/workflows/review.md               1699     1699        -
.tfw/glossary.md                       5126     5174        -
.tfw/templates/REVIEW.md               1128     1140        -
```

`review.md` was **left closed** — not merely unchanged. No item names it and §7 makes a word added there a
failure:

```
(empty above means review.md carries no change in this round)
```

---

## §3 — item 3: the template stops inviting an order

```
diff --git a/.tfw/templates/REVIEW.md b/.tfw/templates/REVIEW.md
index 239f23d..3ef0561 100644
--- a/.tfw/templates/REVIEW.md
+++ b/.tfw/templates/REVIEW.md
@@ -45,8 +45,8 @@
 
 {Rationale referencing §2 Verify and §3 Judge evidence}
 
-### If REVISE — items to fix:
-1. {specific item to fix}
+### If REVISE — items proposed to the coordinator:
+1. {the item} — **basis:** {the TS acceptance criterion or frozen HL claim it breaches}
 
 ### If REJECT — fundamental issues:
 1. {issue requiring HL/TS rework}
```

Nothing was added — the section count is unchanged:

```
headings at a314751: 10
headings now:        10
```

Read against `conventions.md` §15's Reviewer entry — the two must say the same thing:

```
When a Reviewer reaches a verdict, the correct action is to **name the next act** — a decision with
no addressee is not a decision:
1. On ✅ APPROVE — inform the user the review is complete, then run the KNW steps (`/tfw-docs`, and
   `/tfw-knowledge` if Fact Candidates exist). `lifecycle: KNW`, not `DONE` yet
2. On 🔄 REVISE — state that the items are **proposals**, say how many, and **return the work to the
   Coordinator**: "Start `/tfw-plan` to order the round." Set `lifecycle: TS_DRAFT`. Do **not** write an
   ordered bound and do **not** dispatch an executor: a round is ordered in the coordinator's own
   artifact, and the reviewer does not own one
3. On ❌ REJECT — route by §5's three destinations and say **which**: (a) 📝 HL_DRAFT, (b) 🔬 RES,
 or
   (c) 🟡 TS_DRAFT
4. **Do NOT fix anything yourself** — a reviewer that repairs its own findings has reviewed nothing

and the template heading a reviewer now fills:
48:### If REVISE — items proposed to the coordinator:
```

---

## §4 — item 4: the EV file gets a class

```
+| **EV** | **appended** — a round's rows beside the earlier round's | Nothing about an EV governs either, and an earlier round's verification does not stop being true, so a later round has nothing to supersede. Named here because a round produces five artifacts and a grammar that classifies four leaves the fifth to an analogy — and an analogy two executors read differently is how one artifact

the table now classifies every artifact a round produces:
   **TS**       **sibling** 
   **REVIEW**   **sibling** 
   **RF**       **appended** — one new numbered subsection per round, in 
   **ONB**      **appended, never a sibling** 
   **EV**       **appended** — a round's rows beside the earlier round's 
```

---

## §5 — item 5: the locators are removed, and four bullets announce what ships

The gate: no `§14:9` locator survives, and both anti-patterns are still resolvable from the entry's own
quoted text.

```
$ grep -n "§14:9" .tfw/CHANGELOG.md
(no output — 0 hits)

the two clauses, before and after:
-  `conventions.md` §14. The second is a **verbatim** duplicate of `§14:902`. The first is not:
-  `§14:901` reads ``- Executor writes REVIEW file → **Role Lock violation**`` and carries no
+  `conventions.md` §14. The second is a **verbatim** duplicate of its §14 counterpart. The first is
+  not: §14 reads ``- Executor writes REVIEW file → **Role Lock violation**`` and carries no
```

The four bullets, one per shipping item, and nothing else:

```
+- **`.tfw/workflows/handoff.md` loses a step, and the executor's states renumber.** The step that set
+- **`.tfw/templates/REVIEW.md` §4 stops inviting an order.** `### If REVISE — items to fix:` becomes
+- **`conventions.md` §4's revision grammar classifies the EV file.** The table covered TS, REVIEW, RF
+- **`glossary.md`'s `Disposition` says what a `paid` ruling requires.** A `paid` ruling names the phase

no other locator in the entry was touched:
28	2	.tfw/CHANGELOG.md
```

---

## §6 — item 6: what a `paid` ruling requires

```
+The ruling a debt item carries before its task can close: **paid** as a phase of that task, **promoted** to a
 task created then and there, or **not material**, ruled on the record beside the item. Exactly three, and a d
isposition must name something that already exists — *"→ backlog"* and *"someone should open a task"* name
 nothing and are not dispositions. The reviewer proposes; the **coordinator** rules, once at the close of revi
ew. `pending — coordinator` and `pending — owner` are legal waiting states, not a fourth outcome, and each
 keeps the task open until it becomes one of the three. A **`paid`** ruling names the phase that pays it, and 
where the payment has not happened yet the **same act must order it** — in a round, citing the item's condit
ion; unordered, `paid` accepts an item without a decision, which is deferral under a new name. → `templates/
REVIEW.md` §5, conventions.md §15
```

The four `paid` rulings the sentence legitimises — REVIEW revision 2 §5, rows 1, 2, 3 and 4, all ruled
`paid — this task's phase` for work that had not yet happened and ordered in this round:

```
row  1    `DOUBLED_SLUG = re.compile(r"\{ID\}__")` contradicts `conventio
row  2    Step 7 orders `lifecycle: RF` — *execution complete, RF writt
row  3    `### If REVISE — items to fix:` — an order in the artifact 
row  4    Four artifacts classified; a round produces five. The EV file h

and this round is where each was ordered:
item  1    `docs/scripts/test_integration.py:938` — the check cont
item  2    `handoff.md:103` — step 7 orders a false state before t
item  3    `templates/REVIEW.md:48` — a heading ordering the act A
item  4    `conventions.md` §4 — the grammar classifies four arti
item  5    `.tfw/CHANGELOG.md` — two locators that are now false 
item  6    `glossary.md` `Disposition` — nothing says what a `paid
```

---

## §7 — the gates the order names, and the ones held over from earlier rounds

```
$ git grep -n "max_revision_cycles" -- . | grep -v "^workspace/\|^tasks/"
(no output — still 0 hits)

all 22 adapter copies against their 11 sources:
drift=0  (0 means all 22 are byte-identical)

$ python .tfw/scripts/gen_index.py --check tasks
note: tasks/TFW-55__canonization_program: 2 phase directories carry no status.md (phase-a, phase-b); informational, the task carries no status.md of its own; phase state is not written by migration
17 phase directories under 6 task(s) carry no state file; informational lines above, exit code unaffected

review.md word gates, unmoved by this round:
  Steps 4-6       477 of 483
  Anti-patterns   160 of 163
```

---

## §8 — the state sequence a round walks, from this task's own journal

```
20260902-115300__transition__640e.md         transition  HL_DRAFT -> RES
20260902-135257__transition__9218.md         transition  RES -> TS_DRAFT
20260902-142623__transition__768e.md         transition  TS_DRAFT -> ONB
20260902-143632__transition__845e.md         transition  ONB -> RF
20260902-155307__transition__d670.md         transition  RF -> ONB
20260902-155905__transition__3292.md         transition  ONB -> TS_DRAFT
20260902-165919__transition__ce94.md         transition  TS_DRAFT -> ONB
20260902-172139__transition__f189.md         transition  ONB -> RF
20260902-180008__transition__d469.md         transition  RF -> TS_DRAFT
20260902-183449__transition__8999.md         transition  TS_DRAFT -> ONB
```

---

*round3.md — TFW_20260902-112841_RDP: Review Decision Protocol | 2026-09-02*
