# Map — "What was done?" · round 5

> **Mindset:** Experienced newcomer. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF__TFW_20260902-112841_RDP.md](../../RF__TFW_20260902-112841_RDP.md) §1.5–§9.5
> Order: [TS__TFW_20260902-112841_RDP__rev5.md](../../TS__TFW_20260902-112841_RDP__rev5.md) — highest ordinal governs
> Contract: [HL-TFW_20260902-112841_RDP.md](../../HL-TFW_20260902-112841_RDP.md) · 🔒 FROZEN at `1c7b55e`
> Prior verdict: [REVIEW__…__rev4.md](../../REVIEW__TFW_20260902-112841_RDP__rev4.md) — 🔄 REVISE, seven §5 rows, **all seven ruled** by the coordinator (three `paid`, three `not material — not owed`, one `promoted — RTBO`; rows 2 and 3 overruled from `promoted` to `paid`)
> Reviewer session: Claude Code, on behalf of `saubakirov` — one profile in `team/`, used silently
> Round dispatch state: `c38f87a` · round 5 commits: `34044b6`, `00a12b1`, `6998348`

## 1. The order, in one line

Two items, both false statements in files about to be tagged into 2.1.0, both citing the same frozen
clause — **HL §7.1**, *"Every claim about the corpus carries its measurement. A count in this task's
artifacts is one that was run, with the command recoverable."* Bound: **two items, nothing else.**

## 2. What the executor changed

Four files, and I confirmed the change set is exactly four by diffing the round's commits against
dispatch state `c38f87a`:

| File | Change |
|---|---|
| `.tfw/CHANGELOG.md` — *Known open at this tag* | the `116` denominator **removed**; a clause states no denominator is quoted and why |
| `.tfw/CHANGELOG.md` — *Verification* | *"`--check tasks`: 56 tasks validate"* replaced by *`gen_index.py --check tasks` **exits 1***, with its command; the suite figure gains its command |
| `.tfw/CHANGELOG.md` — *⚠️ Changed* | the **`253 rows`** count **removed** — found by the sweep, not named in the order |
| `.tfw/glossary.md` — *Session Naming* | *"present in every TFW workflow"* → *"in the executor and reviewer workflows"*; the `plan.md` Step 0 citation removed; one clause names why `plan.md` has none |
| `evidence/round4.md` | the placeholder `$ python  #` becomes three runnable commands with pasted output |
| `RF` §7.4 fact candidate F18 | worked example corrected — the repair is *no denominator*, not a better one |

The last two are in-place edits to round 4 artifacts. Both were **ordered by name** in TS rev5 item 1, and
the executor recorded the departure from the append-only grammar in RF §1.5 rather than making it quietly.

## 3. The three things the executor volunteered

These are what the round actually turns on, and they are why it is reviewable rather than mechanical:

1. **A 17-claim sweep** of the whole 2.1.0 entry (RF §6.5), each claim with its `git blame` author and a
   verdict. 3 acted on, 1 given its command, 3 verified true and left, 1 false-at-HEAD reported and left,
   9 other tasks' or non-corpus.
2. **A third figure acted on beyond the two named** — `253 rows` — with the authority read written down in
   ONB §11.5 item 1 and **the single revertible hunk named** in RF §1.5 if the coordinator reads the bound
   narrower.
3. **One figure left standing with the full case against leaving it** — `review.md is 1 706 words`, false
   at HEAD (1699), and *this task* staled it. Recommended for the release step in ONB §11.5 item 2, not
   taken on the executor's own authority.

## 4. What was deliberately not done

`review.md` byte-identical. The malformed journal event untouched and `--check tasks` still exiting 1, **by
the owner's standing ruling**, reported as recorded state and not as a defect. `tasks/TFW-60`'s copy of the
same false universal left standing — frozen history. `templates/`, `conventions.md`, `KNOWLEDGE.md`,
`gen_index.py`, both `project_config.yaml` files: out of scope.

## 5. Self-check gate

- [x] I can state the order's two items without re-reading it
- [x] I can state every file changed, and confirmed the set independently of the RF's own list
- [x] I have read the prior verdict **and its rulings**, and know which rows are closed
- [x] I know which standing owner rulings bar a finding before I look for one
- [x] No opinion formed yet — Verify is next
