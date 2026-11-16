---
name: tfw-daily-task
description: Do one bounded everyday request in a TFW project (a fix, a document, an analysis, a small change) without the Full HL/TS/RF/REVIEW cycle - check that no formal task owns the object, keep a short record under daily/ with a checkpoint before the first product edit, run a focused check, and keep prepared, checked, accepted and released apart. Use when asked to "do it as a daily task", "/tfw-daily-task", "a quick task without a full cycle", "continue the daily record", or when the owner gives a clear bounded request outside an active formal task.
---

# TFW Daily Task

Do one bounded request end to end. The human keeps the purpose, accountability and acceptance; you, one worker, do the work.
Start from the result the person needs: state Goal and Value, test them against the project's North
Star and Values, challenge a weak premise with concrete reasons, and drop work that protects no
purpose, evidence or boundary. "Daily" names this route, not a cadence or a risk level.

## When to use, when not

Use it when a human gives a clear, bounded request and the project instructions or the request
source establish that human's authority over the object.

Do not use it when the object belongs to an active formal Full task or phase, or to another
mutation owner. Stop the dependent change, name the missing authority, and send it to that task's
Coordinator. Do not edit its controls, invent a verdict or relabel it Daily: the formal route owns
that object. Daily gives no Coordinator, Executor or Reviewer authority, and a title, model,
profile, prior task or urgency gives no permission.

## Fast path

1. **Read the sources.** Read project instructions, `.user_preferences.md` if present, local Daily
   rules and the actual request. Note the human and the worker; if an identity is unknown, say so
   instead of inventing a handle, because the record must stay attributable. A missing profile does
   not block; a missing request source or authority blocks the action that depends on it.
2. **Inspect the object, then history.** Read the current object and its governing sources first.
   Make one bounded search of recent Daily records and project knowledge by path, name or intended
   result; read only convincing matches. Record what you inspected (paths and commit, hash or
   state) or an honest no-match. Check old work's scope, currentness, source, producer and authority,
   and resolve a material successor or conflict by the project's knowledge rules: history never
   overrides the current product.
3. **Select the record.** Keep the project's own form, such as a task/brief/messages split.
   Otherwise create `daily/YYYY/YYYYMMDD-HHMMSS_slug/task.md` from `templates/task.md`: read the
   clock once, use the whole folder name as the immutable ID, and add a suffix if it is taken, never
   changing or moving the existing record. The template shapes new records only; never rewrite old
   ones to match it. Continue an existing record only for the same deliverable under the same
   authority, keeping the earlier request meaning, result and decisions through dated additions,
   justified versions or file history; a different outcome, owner or boundary gets its own record. Where the host can set and read back a title, use
   `DAILY · <folder ID>`; otherwise say once that it is unavailable and go on.
4. **Write the checkpoint before the first product edit:** source, inspected rules and object,
   prior-work result, Goal, Value, North Star fit, Boundaries and the completion check. A gate
   written after the fact proves nothing, so never backfill it. Keep it to observations and
   decisions, not private reasoning. In the same step, before the first product edit, add the
   economics binding block ([references/economics.md](references/economics.md) §1).
5. **Do the work** without a second plan approval. Resolve routine gaps from the sources. Ask only
   for a missing consequential fact, choice or authority, and hold only the action that depends on
   it. Put products at their ordinary project paths; give an output with no evident place an existing
   suitable one, and ask only when none fits ("working material" is a valid answer). Quote material human words exactly with author and source; copy no
   whole chat, secrets or private reasoning.
6. **Check, record, return.** Run the check that tests the completion condition itself: run the
   fixed function where it is used, open the finished document, view the design in its real
   format. Preserve a previous result when the request protects it. Keep observation, inference and
   uncertainty apart; a source read or a hash proves only that level, not the host's real behavior. If a check fails, fix it inside the boundary and recheck; if a required check is
   unavailable, the claim stays open. Update the record, then return the result and any decision
   left for the human.

## Stop and route

- **Goal or boundary change, or a reserved release, publication or communication:** keep the
  prepared work and route exactly that decision to its authority. Silence is not approval. Continue
  independent authorized preparation.
- **Owner-authorized Daily release:** follow `/tfw-release` and the project's release contract with
  this record and its checks. No Full conversion and no fabricated TS, RF or REVIEW.
- **Formal task owns the object:** stop and route as in "When to use, when not".

Consequence and uncertainty decide how deep the checks and independent review go.

## Record

- Write which claim holds: prepared, checked, human-accepted or released. Never invent acceptance,
  release or an unobserved effect, because only the human accepts. A checked result awaiting
  acceptance says so.
- Make source, Goal/Value, Boundaries, result, check and next authority readable without the chat.
  Keep the record to about one screen plus links; analysis lives in the products.
- At every turn return, not only at economics captures, the folder holds only the record and economics files, and the record
  lists every product with its path. Keep working material in the system temporary
  `tfw/<folder ID>/`; remove leftovers you see there, and remove it in the final turn.
- Add no `daily/README.md`, HL, RF, status, journal, lifecycle words or per-task knowledge file,
  and no folderless form by implication. Link related records only when they change a decision; no
  mandatory category, shared journal, backlink upkeep or archive-wide sweep.
- Keep a consequential reusable observation as a Fact Candidate with source, scope and uncertainty.
  Stable rules go to product documentation or the project's knowledge route; repetition neither
  proves a fact nor authorizes publication.
- Do not leave authorized work unfinished just because a record exists.

## Economics

Commands, binding block and failure forms: [references/economics.md](references/economics.md).

- Bind your own source at start or resume, before product edits (§1).
- Capture, validate and receive a cumulative snapshot (§2–3) before returning a prepared or checked
  deliverable or a materially revised result, before a planned pause or handover, and at close.
  Do not wait for human acceptance of a delivered result. A reply that only explains the unchanged
  result or reports status needs no separate capture; its usage enters the next cumulative bound.
- Only a verified covering successor of the same bound source replaces an earlier revision in
  totals. Disjoint sources or ranges add; failed or unproved successors never erase last-good facts.
- On resume, bind this worker's own source. Reuse earlier workers' received numeric files; do not
  read their private journals by default or claim their source as your own. A missing receipt or
  inaccessible own source is an explicit gap. List every measured source and unresolved return.
- A failed capture or an interruption without one leaves an explicit gap; keep the last good
  revision (§4). A later capture may recover own-source numbers but never proves that the earlier
  checkpoint existed.
- At close (actual acceptance, or the human ends the record), write one summary with the final
  snapshot: tokens, supported money and
  time, coverage and contributors. Disclose the uncounted tail after the cutoff once.
- Capture failure never blocks or erases useful work, and missing binding never becomes an invented
  measurement. Never reprice history or write a zero bill. Money, including the subscription
  line: §5.

Installation and update: [installation.md](installation.md); not needed for ordinary work.
