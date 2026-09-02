# Word budget — TFW_20260902-112841_RDP (AC-1)

> **Date**: 2026-09-02 · **Author**: Claude Code (Executor), on behalf of `saubakirov`
> **AC**: [AC-1](../TS__TFW_20260902-112841_RDP.md) — the budget is re-measured before anything is written
> Every figure below is command output pasted as it was returned. Nothing is inherited from research.

---

## The commands

```bash
# Steps 4–6, as one unit — the criterion (DoD 10, as amended by A1)
awk '/^## Step 4/{f=1} f&&/^## Step 7/{exit} f' .tfw/workflows/review.md | wc -w

# Anti-patterns — binds separately
awk '/^## Anti-patterns/{f=1} f' .tfw/workflows/review.md | wc -w

# conventions.md §5 — added to AC-1 after the ONB
awk '/^## 5\) Task Statuses/{f=1} f&&/^## 6\) Scope Budgets/{exit} f' .tfw/conventions.md | wc -w
```

## The three figures per section

| Section | Baseline | Honest draft | Compressed | Ceiling | Verdict |
|---|---:|---:|---:|---:|---|
| `review.md` Steps 4–6 | **483** | **753** (+56 %) | **480** | ≤483 | ✅ **3 words under** |
| `review.md` Anti-patterns | **163** | — | **160** | ≤163 | ✅ **3 words under** |

Per step, reported because DoD 10 asks for it and is explicit that it is **not** the criterion:

| | Step 4 | Step 5 | Step 6 | Group |
|---|---:|---:|---:|---:|
| baseline | 116 | 299 | 68 | **483** |
| honest draft | 214 | 374 | 165 | **753** |
| compressed | 148 | 212 | 120 | **480** |

Step 4 grows by 32 words and Step 5 falls by 87 — the group is what binds, and it is met.

**The whole file, reported and not the criterion either:** 1 706 → **1 702 words**. Six mechanisms
arrived and the file is **four words shorter** than it was.

### Baseline confirmation, before any edit

```
$ awk '/^## Step 4/{f=1} f&&/^## Step 7/{exit} f' .tfw/workflows/review.md | wc -w
483
$ awk '/^## Anti-patterns/{f=1} f' .tfw/workflows/review.md | wc -w
163
$ wc -w .tfw/workflows/review.md
1706 .tfw/workflows/review.md
```

Both figures reproduce A1's corrected baselines exactly. Iteration 1's per-step split (109 / 289 / 63)
does not reproduce — it sliced at different boundaries — but the **group figure, which is the criterion,
agrees to the word**.

### After

```
$ awk '/^## Step 4/{f=1} f&&/^## Step 7/{exit} f' .tfw/workflows/review.md | wc -w
480
$ awk '/^## Anti-patterns/{f=1} f' .tfw/workflows/review.md | wc -w
160
$ wc -w .tfw/workflows/review.md
1702 .tfw/workflows/review.md
```

## `conventions.md` §5 — measured because AC-1 now requires it

```
$ awk '/^## 5\) Task Statuses/{f=1} f&&/^## 6\) Scope Budgets/{exit} f' .tfw/conventions.md | wc -w
952        # before
1433       # after
```

**+481 words, and the reason it is not a relocation of the budget.** AC-1's added bullet draws the line:
*the reason may live in §5; the mechanism may not.* What §5 gained is the mechanism's **canonical home** —
the three-rung route table, the definition of `revision`, the budget's mechanics and the return — because
§5 is where every verdict route already lives and DoF 1 forbids creating a file for it. What `review.md`
kept is the mechanism **in use**: the axis quoted, the consequence test, the rung named per item, the
budget counted with its number, the coordinator's ruling act, the round's bound. AC-4's own last bullet
asks for exactly that division — *"`review.md` **uses** the route rather than restating it."*

The check a reader can run: delete `conventions.md` §5's new subsection and `review.md` still instructs
the reviewer to locate, test, route, propose and count — it just stops saying where a routed item lands.
Delete `review.md`'s Steps 5–6 additions and the mechanism has no site at all. The mechanism did not move.

## What was subtracted, and why each was terminology rather than substance

F40's method: where a paragraph is explaining, look for the missing word.

| Subtraction | Words | Justification |
|---|---:|---|
| Step 5's `grep`/`awk` discovery block moved to `templates/REVIEW.md` §5 | −73 | **Instructed** (TS §4 authorisation 1). A template is not an installed adapter copy; a workflow is, and a harness rewrites positional parameters in one before the agent reads it while `cmp` stays green. Verified intact and re-run below |
| Step 4's four §-summary bullets folded into one sentence | −25 | §11: *"Templates own format; workflows reference templates."* The four bullets restated `templates/REVIEW.md`'s own section numbering |
| Step 4's Routing paragraph compressed, `judge.md` row 2a cited | −26 | Both outcomes and both routes are already stated in full in `judge.md`'s Purpose Check table. Semantics unchanged: same two findings, same destination, same *"with every other check passing"* |
| Step 5's five-item numbered list became a two-column table | −55 | Not a subtraction of content — the same five acts, denser. It also reads as structure rather than prose |
| *"a refusal that cannot later be shown wrong is a preference"* moved out of Step 5 | −9 | The rationale's home is HL §7 Principle 5; the rule (*a bare priority is inadmissible*) stays, and `templates/REVIEW.md` §5 carries the reason where a reviewer writes the cell |
| Step 5's *"names something that already exists"* paragraph tightened | −8 | The full grammar now lives in the template's column note, which is where a cell is written |
| Step 6's *"two of three cannot be stamped"* clause dropped | −17 | It restated Step 5's *"a disposition names an artifact that already exists"* — one term, stated twice |
| Two Anti-patterns removed as verbatim duplicates of `conventions.md` §14 | −29 | *"Executor writes REVIEW file…"* and *"Reviewer approves without opening any files…"* are word-for-word §14 lines, and the block's own header reads *"Full generic list → conventions.md §14."* One list stopped saying it twice |

**Nothing on that list is a mechanism.** Every one of the six arrived whole; DoF 2's *"thinned to fit"*
did not happen, and the stop AC-1 reserves was not needed.

## The relocated search, re-run from the project root

`conventions.md` §11's rule is that a command written into a workflow must survive its adapter. The
command was already positional-parameter-free when `TLD` fixed it; it is verified here unchanged in its
new home, and run:

```
$ grep -n 'positional parameter placeholders' -c .tfw/templates/REVIEW.md   # no $N in the file
$ grep -rl --include='REVIEW*.md' 'Tech Debt Collected' workspace tasks |
  xargs awk 'FNR==1{s=0} /^## .*Tech Debt Collected/{s=1;next} /^## /{s=0}
             s && /^\| / && !/^\| *(#|-)/ {sub(/^/, FILENAME": "); print}' | wc -l
253
```

Run twice, both times **253**. This is the third value this measurement has carried: the CHANGELOG said
**243** (true before `TLD`'s own review added nine rows), the TS's authorisation 3 expected **252**, and
the corpus today returns **253**. The shipped figure is the one that was run, dated, and printed beside
its command — which is the only reason the earlier two could be caught.

---

*Word budget — TFW_20260902-112841_RDP (AC-1) | 2026-09-02*
