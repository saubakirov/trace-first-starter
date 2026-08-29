# Map — revision 3 — "What was done?"
> **Mindset:** Experienced newcomer. Understand before you judge.
> **Scope:** the R4 corrective pass — TS revision 4, AC-15, twelve items. Earlier passes stand:
> [`../map.md`](../map.md) · [`../rev2/map.md`](../rev2/map.md)
> TS: [TS Phase AA](../../TS__phase-aa__portable_delivery.md) at **revision 4**
> RF: [RF Phase AA](../../RF__phase-aa__portable_delivery.md) — **still at revision 2. It does not describe this pass.**
> Commits: `22de861` · `d62fd26` · `2d269e4` · `f7c9dfe` · `94f02a6` · `fd85b7c` · `5e9b0a1` · `b75bef1`
> **Owner's stated emphasis:** quality, architecture, value, goal. Counts are not the question.

## Understanding

Two things happened, and only one of them is a correction.

**The awaited evidence arrived.** A second real external project, `innoforce-ai-first`, ran the
full `1.3.0 → 2.0.0-dirty.2` update including the board migration, and wrote its own retro.
The coordinator filed it verbatim at task root. It says the phase achieved what it was for:
the first consumer *"spent the rest of the session reconstructing what to do and in what
order"*; this one **spent nothing** — Step 3 routed it to the guide and the guide had the
order with the consequence of skipping each step. Zero unrecognized directories, zero
unaccounted rows, and the identity gate **refused** a bad value instead of swallowing it.

**And it named a design error.** Writing an obvious `actor: claude-code` was refused; the
operator read the validator's source to invent `claude-20260828a`; two external projects ended
up minting a profile per agent session, and one later deleted them — leaving its build gate
red **permanently**, because events are immutable and profiles are not. The owner ruled:
`actor` carried two unrelated jobs — *say who wrote this* and *make the filename unique* — and
those two contradict each other. Remove it until TFW-54.

So the pass removes a field from the event carrier, replaces the filename's third component
with a four-hex opaque token whose only job is uniqueness, defines `bindings.yaml` (instructed
by seven workflows, defined by none), admits per-phase journals to the model, adds the missing
Claude Code row to Step 6, records `installed_from`, and rewrites §10.4 as a rule rather than
patching its example.

## TS ↔ RF Alignment

**This is the finding of the Map stage, and it is not a small one.** The RF header reads
*"revision 2, after REVIEW `440d6fd`"*, cites the **TS at revision 3**, and its §3 acceptance
table has **fourteen rows and no AC-15**. Neither `5e9b0a1` nor `b75bef1` touched it.

| TS revision 4 | RF says | Aligned? |
|---|---|---|
| AC-15, twelve items, one of them architectural | *nothing* — the AC does not appear in the RF | ❌ |
| The `actor` removal, its rationale, its tolerance rule | *nothing* — no §2 decision row | ❌ |
| `260 passed 1 skipped`, three gates, mkdocs | in `evidence/r4_gates.txt`, **not indexed in the EV** | ⚠️ |
| `update.md` at 1380 words against a ceiling of 1200 | `r4_gates.txt` says *"OVER, see the RF"* — **and there is no RF to see** | ❌ |
| AC-13 half two | RF still reports **UNMET**; EV E63 records the arriving artifact and routes the ruling to the reviewer | ⚠️ correct routing, stale RF |

The evidence artifacts themselves are good — `census_r4.md` measured before the first edit,
`r4_gates.txt`, `ac15_actor_tolerated.txt`. They are simply not gathered into the two documents
a review reads.

## Deviations from TS

- **The TS contradicts itself**, and the executor is not the cause. §1 still says *"The model
  itself does not change. No carrier, schema, vocabulary, lifecycle value or identifier rule is
  touched"*; §7 DoF still ends *"❌ The model changed: any edit to a carrier schema, the event
  grammar…"*; §8's last risk row says *"A finding about the model is filed, not fixed here"*;
  §9 says the phase *"changes no carrier they will extend."* AC-15 mandates exactly what those
  four forbid. Coordinator's, not executor's.
- **`PROVIDER_FAMILIES` was deleted rather than documented.** AC-15 item 2 asked for it to be
  named in payload prose. With `actor` gone its only reader — the gate refusing a provider name
  in `actor` — has no subject, so the set went instead of the prose. Better than specified, and
  it needs a line in an RF that does not exist.
- **`census_r4.md` raises the budget under the two methods** (22 by ruling S32, 38 by distinct
  paths) and proceeds under the declared one, before acting. That is the return-to-coordinator
  rule working as designed.

## Checkpoint

**Self-check:**
- [x] Read RF §1–§5 completely? — yes, and established that it predates this pass
- [x] Read TS DoD and matched each item to RF §3? — AC-15's twelve items match nothing in the RF
- [x] Read HL §7 Principles — can I state the design philosophy? — principle 3 (one normal writer) and the frozen §3.1 question *"who/what acted"* are what the identity model answers, and the R4 change is measured against them in verify
- [x] Read ONB — were blocking questions resolved? — the eight stand; R4 raised none

Stage complete: YES
