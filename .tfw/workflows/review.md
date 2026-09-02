---
description: TFW Review — reviewer checks RF against TS, writes REVIEW, proposes a disposition per finding
---

# TFW Review — Task Review by Reviewer

> **Role:** Reviewer (coordinator in review-locked mode)
> **Input:** Completed RF file + TS (for DoD verification)
> **Output:** REVIEW file with verdict + a disposition on every debt item it captured

> **🔒 ROLE LOCK: REVIEWER**
> Permitted artifacts: review stage files (map.md, verify.md, judge.md) + REVIEW file.
> Forbidden actions: writing code, writing ONB, writing RF, modifying HL/TS.
> The reviewer MUST NOT modify any implementation artifacts. If fundamental issues are found — write them in REVIEW and set verdict to ❌ REJECT.

## Step 0: Name This Session

**Name this session:** `Reviewer | {TASK-ID} | Phase {X}`
Set this as the session/conversation name before doing anything else.

## Context Loading (Reviewer)

When starting as reviewer, load in order:
1. `AGENTS.md` — agent instructions
2. `.tfw/conventions.md` — project conventions
3. `.tfw/glossary.md` — terminology
4. `KNOWLEDGE.md` — architecture, decisions, legacy (if exists)
5. **Master HL at its contract baseline** — vision, design philosophy, architecture decisions, and the Purpose Check's reference set. Not the current file; recover the baseline per `conventions.md` §3 rule 15
6. **Phase HL** (if multi-phase) — phase-specific scope and context
7. **TS file** for the task — exact scope, DoD, constraints
8. **RF file** to review — the executor's results (mandatory)
9. Related HL/TS/RF files referenced in the task
10. Relevant code files modified by the executor

> **Reviewer Identity:** Quality guardian, not rubber stamp. Your job is to protect the project
> from unverified claims, from incomplete work, and from work that is verified, complete and
> beside the point — goals, values and the north star are yours to defend, and they alone can
> ground a block. Trust evidence, not declarations.

## Who Is Acting

Resolve the acting handle **before the first durable write** — before any `status.md` change,
any journal event, any commit. Once per session, not per turn.

| Situation | What happens |
|---|---|
| One profile in `team/` | it is used, silently |
| Several profiles | read the binding on **this machine** — `~/.tfw/bindings.yaml`, or `%LOCALAPPDATA%\tfw\bindings.yaml` |
| No binding · a shared device · a copied binding · a handle whose profile is gone | **ask exactly one short question**, then proceed |

Identity is never inferred from an OS username, hostname, folder name or account display
string. Every event this session writes carries `on_behalf_of` (always a human) and `via`
(the tool). A writer is not named yet — that is TFW-54 — so do not create a profile per
session. → `conventions.md` §4

## Trust Protocol (Review)

| RF Claim Type | Trust Level | Reviewer Action |
|---------------|-------------|----------------|
| "Tests pass" | Verify | Re-run test command or check test file exists |
| "File modified" | Verify | Open file, confirm changes match description |
| "DoD met" (RF §3) | Verify | Cross-check each TS AC item against actual files |
| "Evidence: VERIFIED" (RF §5) | Verify | Check artifact exists and matches claim — see verify.md Evidence Verification |
| "Evidence: N/A" or no evidence (RF §5) | Challenge | Check if TS had Evidence fields; if yes, challenge the N/A |
| "No diagrams needed" | Challenge | Check if task had architecture/flow/state changes |
| "No fact candidates" | Challenge | Scan conversation — were there human insights? |
| Fact Candidates | Trust | Record, verify during /tfw-knowledge |
| Observations (RF §6) | Trust | Triage into REVIEW §5 without re-investigation, then dispose |

## Step 1: Map

> **Mindset:** Experienced newcomer. Understand before you judge.

Create `review/` subfolder in task phase directory.
Copy `templates/review/map.md` → fill all fields.
Complete self-check gate. If any unchecked → go back and do it.

## Step 2: Verify

> **Mindset:** Auditor. The RF is a declaration, not a fact.

Copy `templates/review/verify.md` → fill verification log.
Every action in it is unconditional — verification depth is set by the ratio below, never by the kind of work under review.
Check evidence: verify.md includes an Evidence Verification section — audit evidence artifacts against RF §5 claims.
Scan Project Values priorities 0–4 in full and 5–7 by relevance. For every HL §7.2 and ONB §7
citation, verify link resolution, item existence, semantic match, and relevance to the asserted
application. Check priority 0 against the purpose/principle/non-goal clause claimed and priority 1
against the methodology-value clause claimed, even when both share a README. A resolving but wrong
or irrelevant citation is a discrepancy and triggers the same 100% escalation as any other mismatch.

> From `project_config.yaml` (`tfw.review`). Defaults below.

| Parameter | Default | Type | Config key |
|-----------|---------|------|------------|
| Min verify ratio | 0.42 | Hard | `min_verify_ratio` |

Round up: if RF lists 5 files, verify at least ⌈5 × 0.42⌉ = 3. On any discrepancy → escalate to 100%.

Complete self-check gate. If any unchecked → go back and do it.

## Step 3: Judge

> **Mindset:** Judge. Evidence from Verify → rule on quality.

Copy `templates/review/judge.md` → fill checklists with evidence.
Must reference verify.md findings (not re-invent).

**Purpose Check (row 2a):** answer it against the master HL at its contract baseline plus the project north star — never the TS, which is downstream of any drift, and never a Phase HL, which holds nothing approved. Quote the clause served and name the concrete harm in one field. Full mechanism, including the third outcome: `judge.md`.

Complete self-check gate. If any unchecked → go back and do it.

## Step 4: Decide (Synthesize → REVIEW)

> **Mindset:** Decision-maker. Synthesize stages into a binding verdict with cited proof.

Read all 3 stage files (map.md, verify.md, judge.md).
Write `REVIEW__*.md` using `templates/REVIEW.md` — synthesize §1–§3 from them, don't copy-paste. §4 is the verdict: APPROVE / REVISE / REJECT, with rationale citing stage evidence.

**Routing.** `not fit for purpose` and a **contract defect** both ground ❌ REJECT with every other check
passing, and both route to the **owner**, never the executor (`judge.md` row 2a).

**The citation bar.** A 🔄 REVISE may propose only items naming the condition each breaches — a TS
acceptance criterion, or a frozen HL claim; the rest is disposed of in §5. Cite nothing and the verdict is
✅ APPROVE, the remainder disposed. Neither cite nor approve and the work returns to the task's `owner`
(`conventions.md` §5).

## Step 5: Findings — locate, test, route, propose

Debt is written **once**, in this REVIEW's §5 — no project registry (`tasks/DEBT-SNAPSHOT.md` holds the
retired one). Project-wide search: `templates/REVIEW.md` §5.

Per item in the executor's RF `## Observations`:

| Act | The rule |
|---|---|
| **Filter** | real, or filler? Not what it deserves |
| **Axis** | does leaving it undone damage **purpose, inspectability, authority or continuation**? From [`NS1`](../README.md#ns1): it names which harms *count* and decides nothing |
| **Test** | name the consequence, or its named absence. A bare priority — *"low"*, *"can wait"* — is inadmissible |
| **Route** | by what the fix must change: rung 1 nothing, rung 2 the TS, rung 3 a frozen claim — the 🔄 REVISE route, `conventions.md` §5 |
| **Propose** | `paid` · `promoted` · `not material` beside the item — three outcomes, no fourth. `not material` states which question it answers: *not owed*, or *owed and forbidden to pay* with the barring clause cited. `pending — coordinator` awaits a ruling |

**A disposition names an artifact that already exists** — a phase directory, or a task directory and
`status.md` created now. *"→ backlog"* names nothing. Grammar: `templates/REVIEW.md` §5.

**The reviewer marks and proposes; the coordinator rules** — `conventions.md` §15.

## Step 6: Rule, then update traces

**The coordinator rules every proposed disposition — one act at the close, not one per item.** A discharged rung-2 item changes the TS, and that change alone sets `lifecycle: TS_DRAFT`, once per round.

After verdict:
1. **Set the task's own state** — `lifecycle` in `{task}/status.md` per verdict, with a `transition` event in `{task}/journal/` as `{YYYYMMDD-HHMMSS}__{kind}__{token}.md`, with the time read from the clock
2. **Check §5** — every item carries one of the three dispositions. An undisposed item blocks `DONE`, not the verdict
3. If ✅ APPROVE: `lifecycle: KNW`, not `DONE` yet
4. If 🔄 REVISE: the items stay **proposals** and the work returns to the **coordinator**, who orders the round in a TS revision (§15). No bound, no dispatch

## Step 7: Knowledge Capture (KNW)

After ✅ APPROVE verdict:
1. Run `/tfw-docs` — update KNOWLEDGE.md §1-§3
2. If Fact Candidates exist in RF/REVIEW/RES → run `/tfw-knowledge`
3. Mark both in REVIEW §6: `tfw-docs: Applied/N/A` | `tfw-knowledge: Applied/N/A`
4. When both markers are set **and REVIEW §5 carries no undisposed item** → set `lifecycle: DONE` and fill `outcome` in the task's `status.md`

For trivial tasks: reviewer pre-marks both as N/A during review.

> 💡 If you discovered something about the project during review that isn't
> in KNOWLEDGE.md, record it in REVIEW §7 Fact Candidates.
>
> **Before writing Fact Candidates, review the conversation history.** The human's
> messages are the primary source of strategic knowledge — domain insights, stakeholder
> priorities, business context, and constraints that shape decisions.

## Anti-patterns

> Full generic list → conventions.md §14. Role-specific items below:

- Reviewer writes REVIEW without reading RF — must read the actual results
- Reviewer skips observations triage — every surviving observation is recorded in REVIEW §5 and disposed of there
- Reviewer closes a task with an item undisposed, or writes a disposition naming something not yet in existence — the deferred queue under a new word
- Reviewer rules a disposition instead of proposing it — acceptance authority is the coordinator's, `conventions.md` §15
- A ruling names no consequence, or names only a priority — a preference, not a decision
- Reviewer modifies RF or code — **🔒 Role Lock violation**
- Reviewer approves without checking DoD — each TS acceptance criterion must be verified
- Reviewer and executor are the same session — review must be a separate session/agent
- **🔒 Reviewer MUST NOT write code, ONB, RF, HL, or TS** — Role Lock violation
