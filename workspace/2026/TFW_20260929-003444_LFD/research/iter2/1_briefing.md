# Briefing — Update time and what the procedure can drop

> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW_20260929-003444_LFD](../../HL-TFW_20260929-003444_LFD.md)
> Goal: Installing or updating TFW moves only the framework, about one megabyte, by one written method, and a newer release shows in one line when new work starts; the owner decides whether and when to update.
> Producer unit: `claude-code:agent:local_e821cd09-6696-482b-bd88-ca93dba929a2/lfd-researcher`, continued by name; this in-session agent cannot read its own name back
> Parent Coordinator: `claude-code:session:local_e821cd09-6696-482b-bd88-ca93dba929a2`
> Activation / dispatch source: delegated; continuation [dispatch ded6](../../journal/20260929-030426__dispatch__ded6.md) in `526da86d2a1bc65bd2ca6b405ea00245da690493`; prior activation [dispatch c29b](../../journal/20260929-005309__dispatch__c29b.md); message `/tfw-research TFW_20260929-003444_LFD`
> Coordination authority: `HL-TFW_20260929-003444_LFD.md @ c4044d2efc78e2e422849b27bccc4e0d9da2688e`
> Originating proposer: none
> Mode: focused, answered in advance by the Coordinator. Iteration 2 of `research/iterations.yaml`: H2 and the subtraction challenge.
> Selection: `baseline` · `native-gates` · `tfw-gates-only`. Returns go only to the Coordinator above. Navigation title `RESEARCH · LFD` is unavailable: an in-session agent has no title of its own.

## Why this investigation, and what would change the approach

The HL's critical challenge (§10) is that the download may be a minority of update time. The one timed
receipt (R1, 2026-09-28) spent about 10 minutes applying and 2 on project checks. Iteration 1 measured the
old download at 41 s and the light fetch at 5–8 s on this connection. If that shape holds, removing
113 MiB saves well under a minute here, and the update still feels slow unless some of the procedure's
own steps go. §3 claim 5 admits such removals only with evidence, and only where preservation, pinning
and owner decisions survive (DoF 5).

The approach changes if:
- the receipts show that the procedure's time goes to steps that do protect state, so DoD 7 records that
  no change is warranted;
- a step that looks removable caught a real problem in some receipt, such as a mismatch, drift or a
  partial application;
- staging has entered a receiver's history before, which makes open thread 2 an observed risk rather than
  a theoretical one;
- S2, or S3 with a tag, behaves on GitHub unlike on the local server, in size or with a large time
  difference.

## What iteration 1 hands over

[RES iteration 1](../iter1/RES.md), verified and closed by the Coordinator:
- **Binding decisions:**
  - a raw-byte check (D1);
  - a sparse clone with no archive step (D2), under fixed clone settings (D3);
  - staging stays at `.tfw/.upstream/`, in the order clone, copy, check, delete (D4);
  - a size check after the clone (D5), and one disclosed fallback (D6);
  - S3 for an untagged commit (D7).
- **Open threads taken up here:**
  1. H2.
  2. Staging exposure.
  3. S3 with a tag on GitHub.
- **Not taken up here:**
  - The owner's rulings on A1 and A2 (in §12; not awaited).
  - Unobserved environments; the TS names them.
- **New direction:** S2's GitHub observation completes the A1 comparison, which lacked it.

## Planning inventory (not evidence; Gather observes again)

- **Receivers.** 28 receivers sit under the projects root on this machine. HL §2 counts 24; Gather
  reconciles the difference.
- **Receipts.** The receivers hold 45 sealed receipt copies, but only 17 distinct receipts, in 8
  repositories by Git common directory; 7 of them appear five times each. Sizes run from 4.5 to
  29.0 KB, against the 3,660 B receipt template.
- **Timing.** Only 1 distinct receipt contains any duration word, presumably the R1 receipt HL §2 cites.
  H2's timing evidence is therefore essentially one update. The other receipts give sizes, step counts
  and checks, not durations.
- **Text.** `update.md` has 1,227 words, the receipt template 554 and the final-message briefing
  template 240.
- **Knowledge on why the steps exist:** D70 (pin; no guessing), D11 (change categories protect
  customizations) and D47 (state kept apart from framework). No knowledge record names `update.md`.

## Research Plan

### Gather — every step, its cost and what it protects

- **The steps.** Walk `update.md` Steps 0–4 and list every mandated action. For each, record its trigger
  (always or conditional), its source (`update.md`, a pinned guide or a template), and what it protects:
  receiver state, the pin, an owner decision, or nothing stated.
- **The receipts.** Read the 17 distinct receipts read-only, under anonymized R numbers (HL's R1 and R2
  kept where they match). Per receipt, record:
  - the version pair and any recorded duration;
  - the download size;
  - how many times the payload was hashed;
  - which project checks ran, and whether their inputs include `.tfw/`;
  - the receipt's size against the template;
  - how staging was cleaned up.

  No names, paths or project-specific text are copied.
- **Two light GitHub runs,** in Windows PowerShell 5.1, the shell with the tighter S1 baseline
  (4.8–5.0 s): S2, and S3 with tag `v3.7.1`.
  - Each is rehearsed first against the local server with the same flags.
  - A size check follows every network step; above 2 MiB the run stops and is reported.
  - Files are checked byte for byte per D1.
- **Why each step exists:** D70 and D11 in full, and the CHANGELOG entries behind the Step 2–4 checks.
  External sources: Git documentation for `.git/info/exclude`, and for `git add` with an embedded
  repository.
- **Candidate dimensions:**
  - time share: download against procedure;
  - step class: mandated, or agent habit;
  - protection: state, pin, owner decision or none;
  - change form: remove, narrow, merge or keep;
  - staging control: order only, a local exclude, an ignore line added at init, or a check before
    commit.

### Extract — the step map and H2

- A step matrix: cost (measured, estimated or unknown) × what the step protects × change form. Each row
  names its evidence.
- H2: the download's share of the recorded procedure time, from iteration 1's measured rate. The same
  bytes are also computed at slower link speeds, labelled as inferred, because the HL's false case is
  about "ordinary networks".
- Staging exposure: how long each window stays open under each staging control, and what each control
  costs in words and in receiver writes. There are two windows: the clone's (seconds) and the payload
  copy's (until Step 4 cleanup).

### Challenge — attack each removal

- For each candidate removal, look for the case where the step would have caught something, and test it
  against DoF 5.
- Whether the receipt template forces the length, or agents add it.
- Whether a removal would contradict a pinned guide's obligation: the guides are immutable, and the new
  `update.md` cannot waive them.
- Metacognitive check: what is new, and what was only confirmed.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H2 | Download is a minority of update duration and the procedure's repeated steps (triple re-hash, project checks that `.tfw/` cannot affect, oversized receipts) dominate. False case: the download dominates on ordinary networks → no procedure change; true case → a bounded removal list. | open — iteration 2; input: the old download took 41 s, the light fetch 5–8 s |

## Scope Intent

- **In scope:**
  - H2, from existing receipts and iteration 1's timings.
  - The subtraction challenge over `update.md` and the templates it names.
  - Open thread 2: staging exposure.
  - One light GitHub run each of S2 and of S3 with a tag.
  - External documentation at every stage.
- **Out of scope:**
  - Any trial update execution.
  - Any receiver change, including writing a local exclude in a real receiver.
  - Any other GitHub transfer.
  - Editing shipped files or the immutable pinned guides.
  - The owner's rulings on A1 and A2.
  - Re-testing H1, H3 or H4; the version line; the Codex sandbox.
- **Hygiene:**
  - Receipts are read only, and receivers appear only as R numbers.
  - No names, machine paths or identifying receipt text enter these files.
  - Trials run in scratch directories only.
  - Limits: 15 project files and 5 web queries per stage. Receipts count separately, as evidence items,
    not as project files.

## Guiding Questions

1. **Thin timing evidence.** Only 1 of the 17 distinct receipts records any duration. I propose a bounded
   answer to H2:
   - that one timed update, plus iteration 1's download times;
   - step counts, hash passes and receipt sizes as proxies for the rest;
   - the unmeasured share named as unmeasured.

   The alternative is a timed trial update of a scratch receiver copy, which the iteration 2 focus
   excludes. I recommend the bounded answer: HL §4 deliverable 7 already puts a trial update in the
   Executor's evidence, and DoD 7 makes the RF measure each removal's cost.
2. **Staging exposure.** The receipts may not show whether staging ever entered a receiver's history. May
   I run a read-only `git log --all --oneline -- .tfw/.upstream` in each receiver and report only
   anonymized counts? Without it, thread 2 is settled by reasoning about how long each window stays open,
   not by observed incidents.

## User Direction

- **Mode (Coordinator, answered in advance, 2026-09-29):** focused.
- **Researcher's check for deep mode:** no decision-changing reason found.
  - The limit on H2 is the evidence the focus allows, and more loops cannot enlarge it.
  - The subtraction challenge already requires each removal to show why preservation holds.
  - Independent review of each removal (HL §9) and DoD 7 guard the rest.
- **Session title:** unavailable for an in-session agent.
- **Guiding questions:** pending the Coordinator's answer.

**Knowledge handover.**
- **Producer and recipient:** as in the header.
- **Inspected:**
  - `status.md` and the journal, including dispatch ded6 and escalation e4b3.
  - The HL at `526da86d`, with the applied refinements and §12 A1 and A2 as `PROPOSED`.
  - `iterations.yaml`, with iteration 2 pending.
  - RES iteration 1.
  - `research/base.md`, `focused.md`, the Briefing template and `conventions.md` `Session identity`.
  - `KNOWLEDGE.md` row titles on update topics.
  - Anonymized counts of receivers and receipts.
- **Material:** the plan, the inventory and the two questions.
- **Uncertainty:** H2 is open, and so is the cause of the 28-against-24 receiver count.
- **Continuation:** the Coordinator's answers, then Gather.

---
Stage complete: YES
Gate: WAIT — Briefing returned to the Coordinator; Gather needs its continuation.
