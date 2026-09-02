# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF__TFW_20260902-112841_RDP.md](../RF__TFW_20260902-112841_RDP.md)
> TS: [TS__TFW_20260902-112841_RDP.md](../TS__TFW_20260902-112841_RDP.md)
> Contract baseline: `29be329` · Reviewer session: Claude Code, on behalf of `saubakirov` (one profile in `team/`, used silently)

## Understanding

A review produced two kinds of output — work ordered now and work not done — and neither had a stated
basis, a named decider, or a rule that ends the loop. The executor wired six mechanisms into text that
already existed: an **axis** quoted from `NS1` (purpose · inspectability · authority · continuation) that
names which harms count and decides nothing; a **named consequence** as the test that decides an
individual finding, with a bare priority declared inadmissible and `not material` split into *not owed*
versus *owed and forbidden to pay*; **three rungs** routing each finding by what its fix must change
(nothing / the TS / a frozen HL claim), extending `conventions.md` §5's existing `❌ REJECT` route to
`🔄 REVISE`; **acceptance authority** named in §15 so the coordinator rules dispositions and the reviewer
only proposes; a **configured budget** (`tfw.review.max_revision_cycles`, default 2) counted in TS
revisions rather than review rounds; and a **return** on exhaustion to the `owner` handle in `status.md`
as a `transition` to `❌ BLOCKED`.

Sixteen files outside the task directory changed, zero were created, and one configuration key was spent.
Nine further enumerated paths were verified as genuine no-ops and left alone. `review.md` Steps 4–6 carry
all six mechanisms at 480 words against a 483 baseline, and the whole file is four words shorter than it
was.

**Three decisions worth carrying into Verify.** The debt-search snippet moved from `review.md` Step 5 to
`templates/REVIEW.md` §5 (instructed — a template is not an installed adapter copy and a workflow is). The
row count shipped as **253**, which is neither the CHANGELOG's 243 nor the TS authorisation's expected
252, because it was re-measured rather than transcribed. And eight files were silently converted to CRLF
mid-execution by `pathlib.write_text` and normalized back to LF before the adapter sync.

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC-1 — budget re-measured **first**; three figures per section; §5 measured; ceiling miss = STOP | 483→480, 163→160, §5 952→1 433, whole file 1 706→1 702; honest draft 753; eight named subtractions | ✅ |
| AC-2 — axis cited to `NS1`, not the test; §2.4 contradiction gone | Step 5 Axis row quotes the four words, links `NS1`, says it "decides nothing"; Filter row asks only *real or filler* | ✅ |
| AC-3 — consequence grammar, two questions, no fourth outcome, template + `judge.md` row 3, no row added | Grammar in `templates/REVIEW.md` §5; `judge.md` row 3 tightened; 10 rows before and after; nine TLD dispositions re-ruled, 3 of 9 change | ✅ |
| AC-4 — every rung a shipped destination; §5 extended; mixed-rung representable; `review.md` **uses** the route | §5 gains *The 🔄 REVISE route* with the rung table; AFD-48 rev2 replayed at four rung-1 and two rung-2 | ✅ |
| AC-5 — acceptance authority named where the role is defined | §15 row rewritten + a paragraph above the table; `disposition rulings` forbidden; Step 5 proposes, Step 6 rules | ⚠️ **partial** — see Deviations |
| AC-6 — key in both configs with a unit comment; Pattern A; unit = TS revision, not a round; exactly one key | Both configs, 4-line comment, `review.md` parameter row; four prose sites each pair the key with *default 2* | ✅ |
| AC-7 — exhaustion returns to `owner`; three owner cases; closed `kind`; no owner named | `transition` → `❌ BLOCKED`; human/agent/`unassigned` all handled; grep against `HEAD` shows one shifted pre-existing line | ✅ |
| AC-8 — `revision` defined; only a goal change restarts the count; glossary; `handoff.md` re-entry + prior REVIEW | `revision` 0 → 8 occurrences across three canon files; three glossary terms; *Returning after a 🔄 REVISE*; Context Loading item 8 of 10 | ✅ |
| AC-9 — nothing created outside the task dir; one key; before/after maintained-artifact counts | 0 added outside, scoped and unscoped both pasted; `.tfw/` 70→70 tracked; root `.md` 7→7 | ✅ |
| AC-10 — six copies `cmp`-verified; marker blocks and READMEs checked; 2.1.0 entry; verbatim retired wording; `--check project` | All six `cmp` OK; nine no-ops verified by reading; 2.1.0 entry extended; nine bullets carrying ten retired strings | ⚠️ **partial** — `glossary.md` did not carry the whole change; see Deviations |
| AC-11 — suite green; `--check tasks` green; this review runs under the protocol; DoD 14 answered | 322 passed / 1 skipped; 58 tasks validate; DoD 14 answered with a measured *yes* | ✅ |

## Deviations from TS

**1. RF work beyond the TS, declared.** `KNOWLEDGE.md` §3 Legacy & Deprecation gained one row. AC-10 asks
for §1 and §2 only. The executor states this in Decision 11 and asks the reviewer to rule on it rather
than letting it be discovered. Recording the retirement of *"REVISE → back to execution"* is what §3
exists for; taken as sound.

**2. TS items not fully addressed — `glossary.md`.** TS §2 In Scope names `glossary.md` and AC-10's third
bullet requires it to *carry the change*. Three new terms were added (`Revision`, `Revision budget`,
`Rung`) and the two **existing** entries the change contradicts were left untouched:

- `## Reviewer` still reads *"Triages executor Observations into REVIEW §5 and **disposes of every one**
  before the task closes."*
- `## Disposition` still names `pending — owner` as the only waiting state, names no ruler, and points
  the reader to `.tfw/workflows/review.md` Step 5 for a grammar that now lives in `templates/REVIEW.md` §5.

Carried into Verify as V7 and into Judge as the DoF-5 question.

**3. A shipped claim slightly wider than its evidence.** RF Decision 9, `evidence/word_budget.md`
subtraction 8 and the `.tfw/CHANGELOG.md` retired-wording entry all state that the two Anti-patterns
removed from `review.md` were *verbatim* `conventions.md` §14 lines. One of the two is; the other is not.
Carried into Verify as V8.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved? *(Four blocking questions, all answered in §3a; three were answered by amending the artifact — the TS header, AC-6, AC-9 — rather than by ruling in the table)*

Stage complete: YES
