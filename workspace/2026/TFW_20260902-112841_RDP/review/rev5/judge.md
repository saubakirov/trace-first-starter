# Judge — "Is the quality sufficient?" · round 5

> **Mindset:** Judge. Evidence from Verify → rule on quality. Every ✅ needs proof. Every ❌ needs a
> specific finding.
> Verify findings: [verify.md](verify.md) · Map: [map.md](map.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | Both items' criteria in RF §3.5 verified against source, not read back. Item 1: the `116` gone, `56 tasks validate` replaced by the true exit-1 outcome **with its command**, `evidence/round4.md`'s placeholder replaced by three runnable commands whose pasted output matches my re-run character for character, F18's worked example corrected, sweep reported as 17. Item 2: `plan.md` citation gone, universal true, **0** `Step 0` hits in `plan.md` at HEAD *and* at frozen `1c7b55e`, both survivors resolving to line 16, nothing de-numbered. Gates: suite **322 passed, 1 skipped** re-run by me (verify.md §1); every surviving figure in the block names its command |
| 2a | **Purpose Check** | ✅ | See the field below |
| 2b | **Design soundness** vs HL §7 | ✅ | The payment is **subtraction**: three figures removed, one corrected only because the false part was the *outcome*. That is HL §7.1's *"Touch nothing you do not have to"* and F43's *"answering a correct catch with the smallest possible fix is itself a defect pattern"* applied in the same act — the smallest fix was to edit two digits, and editing digits is what produced the defect four rounds running. **No new entity**: no file, key, criterion or status. The discriminator the executor states in RF §2.5 — *does the sentence still make its point without the number?* — is a reusable rule, not an ad-hoc call, and it is now F21 |
| 3 | **Debt disposed** | ✅ | **All seven rev4 rows are ruled**, one act, `REVIEW__…__rev4.md` §6: three `paid`, three `not material — not owed`, one `promoted — TFW_20260902-222456_RTBO` (which I confirmed exists at `lifecycle: TODO` with a PROPOSAL carrying the item). None `pending`. I re-opened none. My own four §5 rows carry `pending — coordinator` with a proposal each, in the shipped grammar — a named consequence or its named absence, never a priority — which is legal and keeps the task open |
| 4 | Style & standards | ✅ | Commit subjects follow the attribution form; three commits, all `--only` with explicit paths in a live shared tree, and **nothing of another session's work was staged** — verified: `tasks/TFW-54…` and `workspace/00-INDEX.md` are still dirty and unstaged. `conventions.md` states no line-width rule, so the one 137-char line the round left is not a standard (verify.md §5, dropped as pedantry) |
| 5 | Observations collected | ✅ | Four rows in RF §6.5, all real, none filler. Row 1 is the executor arguing against its own decision; row 3 names the other session's dirty tree as *the thing that moved the denominator mid-measurement*, which is the round's own thesis; row 4 is a `TFW-N` example correctly classified as illustrative rather than a citation obliged to resolve. **Row 2 is real but under-measured** — see D1 |
| 6 | RF completeness (§7–§9) | ✅ | §7.5 three fact candidates (F21–F23), §8.5 present, §9.5 present. F21 and F22 are the round's own lessons stated as rules; F22's corollary — *"the command is recoverable has to mean the command, not a description of one"* — is why the `$ python  #` placeholder was itself a §7.1 breach, which is a sharper reading of the clause than the order gave |
| 7 | Evidence **exists** | ✅ | E29–E30 in the EV file; artifacts `evidence/round5.md` (275 lines, subsections matching each sub-claim) and the corrected `evidence/round4.md` §3. TS rev5 named an Evidence field per item; both are covered. No `N/A` claimed |
| 8 | Evidence **establishes the claim** | ✅ | The distinguishing test: every figure was measured **false before it was removed**, so the evidence proves the defect and not merely the edit. And the round's weakest point is evidenced *against itself* — the `1 706` block prints the whole drift series `1706 → 1702 → 1699` with the commits, which is what let me confirm in one command that the executor's account of its own omission is exact. Evidence offered against the author's own decision is the strongest form this check can see |
| 9 | Backward compatibility | ✅ | Consumers checked, not assumed. The glossary entry loses one citation to a step that **never existed**, so nothing that resolved stops resolving. `tasks/TFW-60/.../3_extract.md:243` repeats the same false universal and is **deliberately left** — frozen history, and the order named it. Removing figures reverses no normative statement, so `RELEASE.md` §5's *quote the retired wording verbatim as a search string* row does not fire — I checked it rather than skipping it, because it is the row that would fire if a rule rather than a number had been withdrawn |
| 10 | Safety | ✅ | No secrets, no credentials, no destructive operation. Four text files. The live-shared-tree hazard is the real risk here and it was handled: explicit-path commits, `git status` read whole, nothing of `tasks/TFW-54…` touched |

## Purpose Check — row 2 clause (a)

**Reference set:** master HL at its contract baseline `1c7b55e` (verified byte-identical to HEAD), plus
the project north star NS1–NS3.

**The clause served,** HL §1 Vision 🔒 FROZEN: *"a round is available exactly when the reviewer can name
the condition the work breaches, and when nothing can be named the finding is disposed or the task goes
back to whoever initiated it."* **The concrete harm at stake:** the executor found a false figure it could
not pin to any condition this order carries, and instead of quietly fixing it — which would have been
easy, one digit — or quietly ignoring it, it **reported it, argued against its own decision, and named the
revertible hunk for the one call it did make on a wider reading**. That is this task's own rule executed
one round before it ships. Had it acted instead, the mechanism would have reached `/tfw-knowledge`
refuted by the conduct of the round that wrote it — the exact defect F18 was corrected for, and the harm
is that the shipped rule would arrive with its own counter-example attached and nobody downstream would
trust it.

Three tests, each answered *no*:

1. **Excess and adjacency** — nothing was delivered that §7.1 does not ask for. The one act beyond the two
   named figures (the `253`) is judged below and is *inside* the sweep bullet the order itself wrote.
2. **Deferral confession** — the RF names a different home (the release step) for exactly one item and
   **does not ship it here**. That is the opposite of the confession this test looks for: it is the
   deferral declared, evidenced and handed up for a ruling.
3. **Materiality** — the harm named above is material to the task's value, not to wording.

**Outcome: Aligned ✅.** No purpose failure. **No contract defect** — I read HL §1 and §7.1 against each
other to the end of both sentences, and §7.1's *"Touch nothing you do not have to"* discharges rather than
contradicts §1's citation rule: both point at the same restraint, which is why the round could pay two
items and leave a third without either clause being violated.

## The three contested calls, ruled

### C1 — was lifting the bound for the `253` defensible? **Yes, and on better ground than the executor claimed.**

The executor's read (ONB §11.5 item 1) is that `locator` and `figure` are different things, so the sweep
bullet governs figures. I tested that against round 3's actual text rather than accepting it:

- `TS__…__rev3.md:98` — *"Two **line-number locators** removed, not corrected"*
- `TS__…__rev3.md:118` — *"two locators that are now false … a **locator that does not resolve** is not one"*
- `TS__…__rev3.md:274–276` — *"❌ A locator in `.tfw/CHANGELOG.md` is corrected rather than removed, or
  another one is swept up with it. *(This guards a **locator sweep** — opening the file for two numbers and
  tidying six others. **It does not bar** the four `⚠️ Changed` bullets, which are a different act required
  by DoD 13…)*"*

Round 3's bound was written about line-number locators, it says so three times, **and its own DoF
parenthetical already establishes that it does not bar a different act the order requires.** So the bound
never reached figures at all, and the `253` needed no lift — only TS rev5 item 1 bullet 3, *"if it is
false, fix or remove it"*, which is an acceptance criterion of the approved order. The removal breached
nothing. The executor's caution in naming a revertible hunk was correct conduct and is not needed.

### C2 — was leaving `review.md is 1 706 words` correct? **Yes, and it was required rather than merely permitted.**

Two independent grounds, both verified:

1. **It is not this task's claim.** `git blame` → `168e119`, `TFW_20260830-194027_TLD`. HL §7.1 governs
   *"a count in **this task's** artifacts"*, and that clause is the only condition either item cites. It
   does not reach TLD's claim. And it was **true when written** — 1706 at `168e119`, measured.
2. **It is not a corpus count.** The sweep bullet's own scope is *"any other **corpus count**"*. A single
   file's word count is not a count of the corpus — and the executor applied that same line consistently
   across the sweep, leaving claims 6 (`477`, `160`, this task's own single-file counts) and 15 (`123 code
   points`) on the identical reasoning. A discriminator applied consistently to this task's own figures as
   well as to other tasks' is a rule, not an excuse.

So **no condition reaches it**, and TS rev5 §4 bars a third item outright. Ordering it would have made the
round breach its own order — and it would have been the manufactured revision cycle HL §7.2 row 11 cites
F42 to prevent: *"Every gate needs a materiality bar or it manufactures revision cycles on wording."*
→ **§5 row 1, disposed. Not orderable.**

### C3 — item 2's judgement call: two citations, not four. **Right, and adding the other two would have been a defect.**

Four workflows carry a `## Step 0`, confirmed:

```text
.tfw/workflows/handoff.md:16        ## Step 0: Name This Session
.tfw/workflows/review.md:16         ## Step 0: Name This Session
.tfw/workflows/update.md:17         ## Step 0: pin the source from the tag the operator names
.tfw/workflows/research/base.md:12  ## Step 0: Resume & Iteration Detection
```

I read both bodies. `update.md`'s Step 0 resolves `tfw.upstream` to a checkout; `research/base.md`'s
detects a resumed iteration. Neither names a session. The glossary entry defines **Session Naming**, so
citing them would have added two citations that resolve to a heading and not to the convention — a
resolving-but-irrelevant citation, which this project's own verify stage counts as a discrepancy. The
executor's RF §2.5 decision 5 states exactly this and reached it by reading the files rather than trusting
its grep. **Correct.**

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---|---|---|
| 1 | **D71** — *"(247 artifacts in this corpus carry a double quote in their title)"* | RF §6.5 claim 9 leaves `247 artifacts` untouched and declines to assert it false | **No contradiction with the RF** — the RF asserts nothing about it. But D71's own figure is **false at HEAD**: 289–296 by `extract_title()`'s documented rule (verify.md D1). Consolidated knowledge carrying a stale count. **Out of scope in TS rev5 §2 and `KNOWLEDGE.md` verified byte-identical** → §5 row 3 |

Nothing else applies.

## Checkpoint / self-check gate

- [x] Every row answered with evidence from `verify.md`, none re-invented, no bare `✅`
- [x] Purpose Check answered from the master HL at baseline + north star — **not** from the TS
- [x] Both clauses of row 2 answered separately
- [x] Rows 7 and 8 asked as different questions
- [x] The three contested calls ruled on evidence, each against the source text rather than the RF's account
- [x] No standing owner ruling relitigated; AC-11 bullet 2 not cited; the journal event not cited
- [x] **No finding without a named consequence** — and the one non-finding is recorded as dropped
