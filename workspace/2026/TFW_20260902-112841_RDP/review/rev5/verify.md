# Verify — "Is it true?" · round 5

> **Mindset:** Auditor. The RF is a declaration, not a fact.
> **Ratio:** `min_verify_ratio` = 0.42. RF §1.5 lists **4 files** → floor is ⌈4 × 0.42⌉ = **2**.
> **Verified: 4 of 4 = 100%.** Escalated to 100% on my own initiative before finding anything, because the
> round ships into a tag that cannot be rewritten; then held at 100% because I did find a discrepancy
> (D1 below), which triggers the escalation rule independently.
> Every figure below was run in this session, in `d:\projects\research\steps-framework`, Git Bash.

## 1. The gate the standing ruling told me to verify myself

**AC-11 bullet 1 — the suite.** Ran it, did not take the RF's word:

```text
$ python -m pytest .tfw/scripts/ docs/scripts/ -q
322 passed, 1 skipped in 160.89s (0:02:40)
[exited with code 0]
```

**322 passed, 1 skipped, exit 0.** Matches RF §4.5 exactly. Gate **GREEN**.

*(AC-11 bullet 2 is withdrawn by the owner's ruling and is not cited anywhere in this review. The malformed
journal event and `--check tasks` exiting 1 are the owner's standing ruling; I reproduce the exit code
below only to test the truth of the CHANGELOG's new sentence about it, never as a defect.)*

## 2. Every figure the round asserts, re-measured

| # | RF claim | My measurement | Verdict |
|---|---|---|---|
| 1 | suite `322 passed, 1 skipped` | `322 passed, 1 skipped`, exit 0 | ✅ exact |
| 2 | `--check tasks` **exits 1** | exit **1** | ✅ exact |
| 3 | corpus is **61** tasks, **1 problem** | `1 problem(s) across 61 tasks` | ✅ exact |
| 4 | the offending event is **123 code points** against 120 | `summary is 123 code points, ceiling is 120` | ✅ exact |
| 5 | `--check project`: consistent *(surviving prose in the same block)* | `project is consistent with the release it declares`, exit 0 | ✅ true |
| 6 | the documented search returns **285** | **285** rows | ✅ exact |
| 7 | `review.md` is **1699** words at HEAD | `wc -w` → **1699** | ✅ exact |
| 8 | `review.md` was **1706** at `168e119` | `git show 168e119:… \| wc -w` → **1706** | ✅ exact |
| 9 | Steps 4–6 hold at **477** words | `awk '/^## Step 4/,/^## Step 7/' \| sed '$d' \| wc -w` → **477** | ✅ exact |
| 10 | `Anti-patterns` is **160** with its heading, **158** without | **160** / **158** | ✅ exact |
| 11 | `plan.md` has **no** `Step 0` at HEAD and at `1c7b55e` | 0 hits at both revisions | ✅ exact |
| 12 | `plan.md:84` states the omission is deliberate | *"This is step 3 and not step 0 deliberately"* — read in place | ✅ exact |
| 13 | `handoff.md` / `review.md` Step 0 at **line 16** of each | `## Step 0: Name This Session` at `handoff.md:16`, `review.md:16` | ✅ exact |
| 14 | the `116` denominator was true at **no** revision | my own count: **124** in the working tree. Order measured 117/118/114, executor 118/119/120, I get 124 — **four parties, four answers, none of them 116** | ✅ the claim was false, and F22's thesis is confirmed by my own disagreement with both of them |

**Authorship, independently blamed** — this is what the two coordinator questions turn on:

| Figure | `git blame` | Task |
|---|---|---|
| `253 rows` (CHANGELOG **and** `templates/REVIEW.md:98`) | `1f5f578` | **this task, round 1** |
| `review.md is 1 706 words` | `168e119` | **`TFW_20260830-194027_TLD`** — not this task |
| `247 artifacts` | `168e119` | **`TFW_20260830-194027_TLD`** — not this task |

Both `1 706` (line 447) and `247` (line 323) sit **inside** the 2.1.0 entry: the entry spans lines
127–464 (`## [2.1.0] — 2026-09-02` to `## [2.0.0]`). **There is no `v2.1.0` tag** — `git tag` ends at
`v2.0.0-dirty.5` — so the entry is genuinely unreleased and still repairable.

## 3. The bounds, tested rather than assumed

| Bound (TS rev5 §4) | Test | Result |
|---|---|---|
| `review.md` byte-identical | `git diff c38f87a HEAD -- .tfw/workflows/review.md` | **empty** ✅ |
| no out-of-scope file touched | `git diff --name-only c38f87a HEAD -- .tfw/workflows/ .tfw/conventions.md .tfw/templates/ .tfw/scripts/ KNOWLEDGE.md tasks/` | **empty** ✅ |
| frozen legacy corpus not edited | included above — **nothing under `tasks/`** | ✅ |
| nothing de-numbered in `glossary.md` | diff read: `Step 0` retained in the definition; `handoff.md Step 0` and `review.md Step 0` citations byte-identical | ✅ |
| no locator other than the two named touched | the three touched hunks carry `templates/REVIEW.md` §5, `conventions.md` §4 and *see `build.verify` under **Removed*** — **all three unchanged** in the diff | ✅ |
| suite green | §1 above | ✅ |
| HL frozen, no amendment | `git diff 1c7b55e HEAD` on the HL is empty; RF proposes no amendment | ✅ |
| a third item is not worked | the `253` is the contested one → judged in `judge.md`, not here | → judge |

## 4. Evidence verification (RF §5.5 claims 2/2 VERIFIED)

| Row | Claim | Audit |
|---|---|---|
| E29 | three figures gone, one outcome corrected, every survivor names its command; sweep = 17 claims | Artifact `evidence/round5.md` §1 exists, 275 lines, four subsections `1a`–`1d` matching the four sub-claims. Every figure in the row re-measured above; **all exact.** ✅ VERIFIED |
| E30 | the universal is true and every surviving citation resolves | Artifact `evidence/round5.md` §2 exists with the *"Two citations that were NOT added"* subsection. Verified independently: `plan.md` 0 hits at both revisions, both survivors resolve to line 16. ✅ VERIFIED |

**`evidence/round4.md` §3 — the ordered repair, audited in place.** The `$ python  #` placeholder is gone.
In its place: `gen_index.py --check tasks | grep "code points"` with its real output pasted, `--check
tasks > /dev/null; echo $?` → `1`, and a third runnable one-liner for the denominator should anyone ever
want it. I re-ran the first two; the pasted output matches mine character for character. ✅

**No `cmp` step is owed.** None of the four files is an adapter-installed copy. Confirmed against
`.tfw/adapters/`.

## 5. The sweep, audited — 8 of 17 claims re-measured independently

Claims 5, 6, 9, 11, 12, 13, 15, 16 re-measured from source. **Seven verdicts correct.** One discrepancy:

**D1 — claim 9 (`247 artifacts`) is derivable, and it is false.** The executor's verdict reads *"Deriving
it needs `gen_docs.py`'s own title logic, so I did **not** assert it false."* The logic is six lines,
`extract_title()` at `docs/scripts/gen_docs.py:218`: *"Derive title from first `# ` heading, fallback to
filename stem."* Applying exactly that rule:

```text
$ python -c "…first '# ' heading per file, count those containing a double quote…"
  ['workspace','tasks']          files-with-h1: 904   containing a double quote: 289
  ['workspace','tasks','docs']   files-with-h1: 905   containing a double quote: 289
  ['.']                          files-with-h1: 1030  containing a double quote: 296
```

**289–296 against the entry's 247** — false at HEAD by 42 to 49, under the script's own documented rule.
The executor's caution was honest but over-cautious: it declined to assert what it could have measured.

**And the figure is not only in the CHANGELOG.** The same count is stated at seven more sites, one of them
already consolidated project knowledge:

```text
.tfw/CHANGELOG.md:323                    docs/scripts/gen_docs.py:230
KNOWLEDGE.md:165  (D71)                  site/scripts/gen_docs.py:230
docs/scripts/test_gen_docs.py:73         site/scripts/test_gen_docs.py:73
docs/scripts/test_integration.py:161     site/scripts/test_integration.py:161
```

Every one of them is **out of scope** in TS rev5 §2, and `KNOWLEDGE.md` I verified byte-identical in §3.
Routing is `judge.md`'s and §5's problem, not this stage's.

**D2 — a second site of the `253` survives, in a file this round was forbidden to touch.**
`templates/REVIEW.md:98` reads *"On this corpus, 2026-09-02: **253 rows**."* — same commit `1f5f578`, same
figure, and it is the file the CHANGELOG sentence points at. The executor's sweep was bounded to the
2.1.0 entry, so not reporting it is within the letter of the order; it is nonetheless a fact the
coordinator does not have. Materiality and routing → `judge.md`.

*(Non-finding, recorded so it is visibly considered and dropped: the round left a 137-character line at
`.tfw/CHANGELOG.md:458`. `conventions.md` states no line-width rule, and the same file already carries 100+
long lines in hunks this round never opened. No condition, no consequence — **pedantry, not a finding.**)*

## 6. Self-check gate

- [x] Ratio met and exceeded — 4/4 files, 100%
- [x] Every RF figure re-measured from source, not read back from the RF
- [x] The suite re-run in this session, not trusted
- [x] Evidence artifacts opened and matched against their rows
- [x] Every bound in TS rev5 §4 tested with a command, not asserted
- [x] Discrepancies recorded as D1, D2 — carried to `judge.md`, not ruled here
- [x] Standing owner rulings checked before searching, and nothing barred is cited
