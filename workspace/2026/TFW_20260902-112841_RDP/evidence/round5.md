# round5.md — raw output behind EV rows E29–E30

> **Date**: 2026-09-02 · **Author**: Claude Code (Executor), on behalf of `saubakirov`
> Every block below is pasted from a command run in this session, from the project root, in Git Bash.
> Nothing is retyped from memory. The reference revision is `c38f87a`, the round's dispatch state.

---

## §1 — item 1: each figure measured false before it was removed

### 1a. The `116` denominator — true at no revision

Counted by **tree revision**, so the answer does not depend on an uncommitted working tree:

```text
$ for REV in 13f6d9b c38f87a; do
    N=$(git ls-tree -r "$REV" --name-only \
        | grep -E '^(workspace|tasks)/.*/journal/[^/]+\.md$' \
        | while read -r f; do git show "$REV:$f" | grep -q "^summary:" && echo x; done | wc -l)
    echo "$REV: events with a summary = $N"
  done

13f6d9b: events with a summary = 118      ← the commit that SHIPPED the "116" prose
c38f87a: events with a summary = 119      ← the round-5 dispatch state
```

And against the working tree, with the same predicate:

```text
$ python -c "import re,pathlib; \
  e=[p for p in list(pathlib.Path('workspace').rglob('journal/*.md'))+list(pathlib.Path('tasks').rglob('journal/*.md')) \
     if re.search(r'^summary:', p.read_text(encoding='utf-8', errors='replace'), re.M)]; \
  print(len(e))"
120
```

**118, 119, 120 — and the prose said 116.** The working-tree count exceeds the committed one by exactly
one file, and the file is not mine:

```text
$ (set difference, working tree vs c38f87a)
working-tree only: ['tasks/TFW-54__agent_team_mode/journal/20260902-225456__transition__7d1e.md']
commit only      : []
```

**Another session's event, still uncommitted, in a task that is not this one.** It arrived between two of
my own commands, a minute apart. That is the whole case for removal rather than correction, and it is why
the order's own series (117/118/114) and mine (118/119/120) differ without either being wrong: the value
depends on which paths are swept and on whether you read the commit or the tree.

**What replaced it** — the fact, with no denominator:

```diff
-  measured, and the only event over the ceiling among the 116 in this corpus that carry a summary — so
-  `gen_index.py --check tasks` run by hand still exits 1 and names it, alongside whatever else the corpus
-  holds at the time you run it.
+  measured, and the only event over the ceiling in this corpus — so `gen_index.py --check tasks` run by
+  hand still exits 1 and names it, alongside anything else the corpus holds when you run it. **No
+  denominator is quoted**, deliberately: the claim is about one event, not a proportion, and a count of
+  how many events exist is a number someone would have to maintain.
```

The surviving figure in that bullet — *123 code points against 120* — is a measurement of **one artifact**,
re-derivable, and the command that names it is in the same sentence.

### 1b. `56 tasks validate` — a passing check that does not pass

```text
$ python .tfw/scripts/gen_index.py --check tasks ; echo "exit=$?"
workspace/2026/TFW_20260902-112841_RDP/journal/20260902-181437__amendment_escalated__531a.md: summary is 123 code points, ceiling is 120; move the content into an artifact and reference it from the event
1 problem(s) across 61 tasks
exit=1
```

**61 tasks, 1 problem, exit 1.** The claim was wrong twice over — the count and the outcome. This is the
one figure that could not simply be dropped, because the false part was the *outcome*:

```diff
-  frontmatter fix). `--check tasks`: 56 tasks validate.
-  `--check project`: consistent. Documentation site builds; a `TD-N` citation opens
+  frontmatter fix), from `python -m pytest .tfw/scripts/ docs/scripts/ -q`.
+  `python .tfw/scripts/gen_index.py --check tasks` **exits 1**, on the over-length journal `summary`
+  recorded under *Known open at this tag* — it reports, and nothing gates on it.
+  `--check project`: consistent. Documentation site builds; a `TD-N` citation opens
```

**No count is asserted and no passing check is claimed.** Both surviving figures in the block now name the
command that produces them — the suite figure did not before, which was §7.1's second half failing
unnoticed beside its first.

### 1c. `253 rows` — found by the sweep, and this task's own

Run with the entry's **own documented search**, verbatim from `templates/REVIEW.md` §5:

```text
$ grep -rl --include='REVIEW*.md' 'Tech Debt Collected' workspace tasks \
  | xargs awk 'FNR==1{s=0} /^## .*Tech Debt Collected/{s=1;next} /^## /{s=0}
               s && /^\| / && !/^\| *(#|-)/ {print}' | wc -l
285
```

**285 now; the entry says 253; REVIEW revision 3 measured 271.** Three values, one search, one evening.

Authorship, because the bound turns on it:

```text
$ git blame -L 178,178 --porcelain .tfw/CHANGELOG.md | grep summary
summary [claude-code/TFW_20260902-112841_RDP/rf/executor] ship the review decision protocol
```

**This task's round 1** — which is the order's own stated reason for lifting round 3's bar: *"both of
these are claims this task wrote."* The removal, and note what the sentence was arguing:

```diff
-  every captured item across REVIEW files. Measured on this corpus, 2026-09-02: **253 rows** — re-run, not
-  inherited. It shipped in `review.md` Step 5 and moved on the day of release:
+  every captured item across REVIEW files. Its answer is **re-run, never inherited**, which is why no row
+  count is quoted here: the search is the figure, and a number beside it would be one more thing to keep
+  true. It shipped in `review.md` Step 5 and moved on the day of release:
```

A bullet titled *Discovery replaces maintenance* had shipped a maintained figure. **This is the one hunk
to revert** if the coordinator reads the bound narrower than ONB §11.5 item 1 does.

### 1d. The sweep's own number, run rather than estimated

**17 distinct quantitative claims** in the 2.1.0 entry. The extraction, then the classification by hand
with `git blame` on each line:

```text
$ sed -n '127,460p' .tfw/CHANGELOG.md \
  | grep -oE "\*\*[^*]*[0-9][^*]*\*\*|[0-9][0-9 ]*(rows|words|lines|tasks|pages|projects|artifacts|passed|skipped|of [0-9]+)" \
  | sort | uniq -c | sort -rn
```

The full table — every claim, its author, its verdict — is **RF §6.5**. Summary: 3 acted on, 1 given its
command, 3 verified true and left, 1 false-at-HEAD reported and not touched, 9 other tasks' claims or
non-corpus/derived figures.

**Two verified true rather than assumed**, both worth stating because they are mine:

```text
$ awk '/^## Step 4/{f=1} /^## Step 7|^## Anti-patterns/{f=0} f{n+=NF} END{print n}' .tfw/workflows/review.md
477                    ← the entry claims 477. Holds.

$ awk '/^## Anti-patterns/{f=1;next} /^## /{f=0} f{n+=NF} END{print n}' .tfw/workflows/review.md
158                    ← the entry claims 160; 158 + the 2-word heading = 160. Method consistent.
```

And one verified exactly, another task's, left with the command already printed beside it:

```text
$ git show c153895:TECH_DEBT.md | wc -l ; git show c153895:TECH_DEBT.md | wc -w
132
12352                  ← the entry claims "132 lines and 12 352 words". Exact.
```

---

## §2 — item 2: the false universal, checked against all three files it cites

`plan.md`, at **both** revisions the claim could be measured against:

```text
$ grep -c "Step 0" .tfw/workflows/plan.md
0
$ git show 1c7b55e:.tfw/workflows/plan.md | grep -c "Step 0"
0
$ grep -n "^## " .tfw/workflows/plan.md | head -3
13:## Step 1: Load context
17:## Step 2: Knowledge Gate
29:## Step 3: Research & Understand
```

**No Step 0 at HEAD, none at the frozen baseline, and the numbering starts at 1.** The file says so
itself:

```text
$ sed -n '84,86p' .tfw/workflows/plan.md
   This is step 3 and not step 0 deliberately. Understanding the task and asking before
   creating a folder is the right order, and it is kept — which means the identifier does not
   exist until now, so an instruction to use it earlier is unsatisfiable …
```

The two surviving citations, each resolving to a real heading:

```text
$ grep -n "^## Step 0: Name This Session" .tfw/workflows/handoff.md .tfw/workflows/review.md
.tfw/workflows/handoff.md:16:## Step 0: Name This Session
.tfw/workflows/review.md:16:## Step 0: Name This Session
```

The change:

```diff
-Step 0 convention present in every TFW workflow: name the current session as `Role | Task-ID | Phase` … → `handoff.md` Step 0, `plan.md` Step 0, `review.md` Step 0
+Step 0 convention in the executor and reviewer workflows: name the current session as `Role | Task-ID | Phase` … `plan.md` has no Step 0 **by design** — the task identifier does not exist until the directory is created, so the coordinator names the session at step 3. → `handoff.md` Step 0, `review.md` Step 0
```

**Nothing de-numbered**, and the two surviving citations are byte-identical in the entry.

### Two citations that were NOT added, and why the grep was not trusted

A `grep` for `^## Step 0` across the workflows returns **four** files, not two:

```text
$ for f in .tfw/workflows/*.md .tfw/workflows/research/*.md; do grep -q "^## Step 0" "$f" && echo "$f"; done
.tfw/workflows/handoff.md
.tfw/workflows/review.md
.tfw/workflows/update.md
.tfw/workflows/research/base.md
```

So the entry looked **incomplete** as well as false, and the obvious repair was to cite four. Reading the
two extra steps settled it:

```text
$ grep "^## Step 0" .tfw/workflows/update.md .tfw/workflows/research/base.md
.tfw/workflows/update.md:## Step 0: pin the source from the tag the operator names
.tfw/workflows/research/base.md:## Step 0: Resume & Iteration Detection
```

**Different steps that merely share a number.** The Session Naming convention exists in exactly two
workflows. Had the grep been trusted, the repair for a false universal would have been a **wider** false
universal — and the alternative wording, *four of eleven workflows*, would have introduced precisely the
maintained count item 1 exists to remove.

**`tasks/TFW-60`'s copy of the same false universal is untouched**, as ordered:

```text
$ git diff --name-only c38f87a -- tasks/
(nothing of mine; the one path listed is another session's status.md)
```

---

## §3 — the suite, and everything not touched

```text
$ python -m pytest .tfw/scripts/ docs/scripts/ -q
322 passed, 1 skipped in 154.59s (0:02:34)
```

```text
$ for f in …; do git diff --quiet c38f87a -- "$f" && echo "BYTE-IDENTICAL  $f"; done

BYTE-IDENTICAL  .tfw/scripts/gen_index.py
BYTE-IDENTICAL  .tfw/workflows/review.md
BYTE-IDENTICAL  .tfw/workflows/handoff.md
BYTE-IDENTICAL  .tfw/conventions.md
BYTE-IDENTICAL  KNOWLEDGE.md
BYTE-IDENTICAL  .tfw/templates/REVIEW.md
BYTE-IDENTICAL  .tfw/templates/RF.md
BYTE-IDENTICAL  .tfw/project_config.yaml
BYTE-IDENTICAL  .tfw/templates/project_config.yaml
BYTE-IDENTICAL  .tfw/migrations/2.0.0.md
BYTE-IDENTICAL  workspace/2026/TFW_20260902-112841_RDP/journal/20260902-181437__amendment_escalated__531a.md
```

**The journal event is untouched and `--check tasks` still exits 1 on it, by the owner's ruling.** Stated
as the recorded state of the release, not as a defect — §1b above prints that exit code as evidence, and
the CHANGELOG now names it as the reason the check exits 1.

**The shared tree.** Another session wrote `tasks/TFW-54__agent_team_mode/status.md`, a new `journal/`
beneath it, and `workspace/00-INDEX.md` while this round ran. `git status` was read whole before each
commit, every commit used `git commit --only` with explicit paths, and none of those three appears in any
commit of mine. `.gitignore` remains another session's and unstaged, as in rounds 3 and 4.

**No `cmp` step, and the reason rather than the omission:** none of the four files this round touches is
adapter-installed. `CHANGELOG.md` and `glossary.md` are read in place; the RF and its evidence attachment
are task artifacts.

---

*round5.md — TFW_20260902-112841_RDP: Review Decision Protocol | 2026-09-02*
