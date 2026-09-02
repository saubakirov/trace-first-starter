# Map — "What was done?" — round 4

> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF__TFW_20260902-112841_RDP](../../RF__TFW_20260902-112841_RDP.md) — round 4 is the `.4`
> subsection of every section it touches (§1.4–§9.4). Rounds 1–3 are not re-read as work under review.
> TS: [TS__TFW_20260902-112841_RDP__rev4](../../TS__TFW_20260902-112841_RDP__rev4.md) — **the highest
> ordinal governs**
> HL: [HL-TFW_20260902-112841_RDP](../../HL-TFW_20260902-112841_RDP.md) — 🔒 FROZEN at `1c7b55e`,
> **verified byte-identical against that baseline** (`git diff 1c7b55e HEAD` on the HL: empty)
> ONB: §10, the executor's round-4 appendix
> Prior verdict: [REVIEW revision 3](../../REVIEW__TFW_20260902-112841_RDP__rev3.md) — 🔄 REVISE, four
> proposals, seven §5 rows all ruled

## Understanding

Round 4 is **three one-line repairs and one record**, all four of them the coordinator's own errors
returning. Item 1 gives `DOUBLED_SLUG`'s negative lookahead its tail so the mandated revision ordinal must
**end** the filename — four characters, `\.md` — plus a third assertion that places a suffix *after* the
ordinal, the direction round 3's two new assertions could not test. Items 2 and 3 are the same edit in two
files: `glossary.md`'s `Execution Loop` and `KNOWLEDGE.md`'s **D52** were the third and fourth consumers of
round 3's step renumbering, both of which the order's own enumeration missed, and both now name the step by
its title instead of its number. Item 4 is not work at all: the un-gating of the board — `build.verify`
removed from both `project_config.yaml` files, the `Verify` line from `templates/RF.md`, and one
live-corpus exit-code assertion from `test_gen_index.py` — was applied by the **coordinator** in `859dc74`
on the owner's direct instruction *before* this round began, and nothing recorded it. This round wrote the
record: a `### Removed` bullet in the unreleased 2.1.0 entry with the receiver instruction, and a
`### Known open at this tag` bullet stating that the malformed journal event was **not** repaired.

Two things shape how this round should be read. First, **the suite is green because a gate was removed, not
because a number moved** — the journal event, the ceiling and `gen_index.py` are all byte-identical against
`859dc74`, which I verified path by path. Second, **the executor handed one gate over unmet rather than
filtering it**: item 2's grep still returns one `handoff.md` step number, at `glossary.md:215`, and the RF
declares it a judgement the reviewer may overturn instead of reporting the gate clean.

## TS ↔ RF Alignment

| TS revision 4 requirement | RF claim | Aligned? |
|---|---|---|
| Item 1 — lookahead becomes `\{ID\}__(?!rev\{N\}\.md)` | §3.4 ✅, §1.4 row 1 | ✅ |
| Item 1 — a third assertion placing a suffix **after** the ordinal | §3.4 ✅, the assertion quoted | ✅ |
| Item 1 — gate: the third assertion shown **failing** against the old regex | §3.4 ✅ — `AssertionError: assert None`, run not reasoned | ✅ |
| Item 1 — the other three regexes and both surviving negatives untouched | §3.4 ✅ — "two hunks, they appear in neither" | ✅ |
| Item 2 — `glossary.md` `Execution Loop` named by title | §3.4 ✅ | ✅ |
| Item 2 — gate: `grep -n "Step [0-9]" .tfw/glossary.md` returns **no** `handoff.md` step number | §3.4 **☐ NOT MET, declared** — returns one, line 215 `Session Naming` | ⚠️ **handed over** |
| Item 3 — `KNOWLEDGE.md` D52 named by title | §3.4 ✅ | ✅ |
| Item 3 — the CHANGELOG round-3 bullet says **four** live citations | §3.4 ✅, and names all four | ✅ |
| Item 3 — **nothing else** in `KNOWLEDGE.md` touched | §3.4 ✅ — 1 insertion, 1 deletion | ✅ |
| Item 3 — gate: project-wide search returns only history | §3.4 ✅ — 8 hits, 6 released, 1 named history, 1 live and classified | ✅ (with the same survivor) |
| Item 4 — CHANGELOG records the un-gating, with the receiver instruction and its mechanism | §3.4 ✅ | ✅ |
| Item 4 — it says **why**, in one sentence | §3.4 ✅ | ✅ |
| Item 4 — it does **not** claim the event was repaired | §3.4 ✅ | ✅ |
| Item 4 — gate: `git grep build.verify` returns only the entry and history | §3.4 ✅ — neither config holds it | ✅ |
| AC-11 bullet 1 — the build passes | §3.4, §4.4 — **322 passed, 1 skipped** | ✅ |
| AC-11 bullet 2 — `--check tasks` stays green | **withdrawn by the owner's ruling**, TS rev4 §1 | n/a — not claimed, correctly |
| §7 DoF — event, ceiling, `conventions.md` §4, `gen_index.py`, `.tfw/scripts/`, `review.md` all untouched | §4.4 — ten paths listed byte-identical vs `859dc74` | ✅ |
| §7 DoF — no fifth item worked | §1.4 — four targets, four files | ✅ |

## Deviations from TS

1. **Item 2's gate is reported unmet, deliberately and unfiltered.** `glossary.md:215` `Session Naming`
   still cites `handoff.md` Step 0 (and `plan.md` Step 0, `review.md` Step 0). The RF, the ONB §10.5 item
   2 and the EV row E26 all carry the same three grounds and all three name it as overturnable. This is a
   *disclosed* deviation, not a missed criterion — the distinction matters for the verdict and is taken up
   in `judge.md`.
2. **Item 4's record went into two CHANGELOG sections, not one.** TS revision 4 §2 and §4 place it in
   `### Known open at this tag`; §5 item 4's checkboxes order a receiver-facing record of the un-gating.
   The executor satisfied both readings — the receiver instruction into `### Removed`, the un-repaired-event
   fact into `Known open` — and named the removable half in ONB §10.5 item 1 if the coordinator wants one
   site. The seam is the coordinator's own (§2/§4 were written under route (d), §1 under the un-gating),
   and the reading taken is the later statement. **Not a deviation against the executor.**
3. **Three figures corrected against the order and against the executor's own draft**: the repair is four
   characters not three (the order and REVIEW rev3 both say three); the corpus is 61 tasks not 56; and
   byte-identity is measured from the round's dispatch state `859dc74`, not the HL baseline `1c7b55e`.
   All three corrections are in the executor's favour to omit and were made anyway.
4. **No `cmp` step, stated rather than skipped** — none of the four files is adapter-installed, so the
   drift check has nothing to compare. TS §6 asked for exactly this to be said out loud.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely? — §1.4 through §5.4 in full, plus §6.4, §7.4, §8.4, §9.4
- [x] Read TS DoD and matched each item to RF §3? — TS revision 4 §5's four items and §7's nine failure
      conditions, each matched to §3.4 above; AC-11's two bullets handled separately, bullet 2 as withdrawn
- [x] Read HL §7 Principles — can I state the design philosophy? — yes: no new entities; touch nothing you
      do not have to; every claim about the corpus carries its measurement; a rule with no enforcement site
      is decoration. §7.1's Quality Contract is the clause this round is measured against most closely
- [x] Read ONB — were blocking questions resolved? — §10.2 declares **none**, and the one ambiguity
      (item 4's placement) is resolved in §10.5 item 1 with its alternative named rather than raised as a
      blocker. Correct call: guessing wrong there is visible in the diff and cheap to reverse

Stage complete: **YES**
