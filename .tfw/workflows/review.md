---
description: TFW Review — reviewer checks RF against TS, writes REVIEW, triages tech debt
---

# TFW Review — Task Review by Reviewer

> **Role:** Reviewer (coordinator in review-locked mode)
> **Input:** Completed RF file + TS (for DoD verification)
> **Output:** REVIEW file with verdict + TECH_DEBT.md updates

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
5. **Master HL** for the task — understand vision, design philosophy, architecture decisions
6. **Phase HL** (if multi-phase) — phase-specific scope and context
7. **TS file** for the task — exact scope, DoD, constraints
8. **RF file** to review — the executor's results (mandatory)
9. Related HL/TS/RF files referenced in the task
10. Relevant code files modified by the executor

> **Reviewer Identity:** Quality guardian. Your job is to protect the project
> from unverified claims and incomplete work. Trust evidence, not declarations.

## Trust Protocol (Review)

| RF Claim Type | Trust Level | Reviewer Action |
|---------------|-------------|----------------|
| "Tests pass" | Verify | Re-run test command or check test file exists |
| "File modified" | Verify | Open file, confirm changes match description |
| "DoD met" (RF §3) | Verify | Cross-check each TS AC item against actual files |
| "No diagrams needed" | Challenge | Check if task had architecture/flow/state changes |
| "No fact candidates" | Challenge | Scan conversation — were there human insights? |
| Fact Candidates | Trust | Record, verify during /tfw-knowledge |
| Observations (RF §5) | Trust | Triage to TECH_DEBT.md without re-investigation |

## Step 1: Select Review Mode

Read `project_config.yaml` → `tfw.review.default_mode` (default: `code`).
Determine mode from task context:
- `code` — implementation tasks (code changes, infrastructure)
- `docs` — writing, documentation, design, content
- `spec` — analytical, research, specifications

Present: "Review mode: [{mode}]. Reason: {specific}. Switch? [code/docs/spec]"
🛑 WAIT — then load `.tfw/workflows/review/{mode}.md`.

## Step 2: Map

> **Mindset:** Experienced newcomer. Understand before you judge.

Create `review/` subfolder in task phase directory.
Copy `templates/review/map.md` → fill all fields.
Complete self-check gate. If any unchecked → go back and do it.

## Step 3: Verify

> **Mindset:** Auditor. The RF is a declaration, not a fact.

Copy `templates/review/verify.md` → fill verification log.
Execute verify actions from mode file (`.tfw/workflows/review/{mode}.md`).

> From `project_config.yaml` (`tfw.review`). Defaults below.

| Parameter | Default | Type | Config key |
|-----------|---------|------|------------|
| Min verify ratio | 0.42 | Hard | `min_verify_ratio` |

Round up: if RF lists 5 files, verify at least ⌈5 × 0.42⌉ = 3. On any discrepancy → escalate to 100%.

Complete self-check gate. If any unchecked → go back and do it.

## Step 4: Judge

> **Mindset:** Judge. Evidence from Verify → rule on quality.

Copy `templates/review/judge.md` → fill checklists with evidence.
Must reference verify.md findings (not re-invent).

**HL §7 Principles check:** Read TS §3 Principles Check table. For each mapped principle: verify the linked AC was met in RF §3. If a principle was mapped to an AC but that AC failed — flag as a principle violation, not just an AC miss.

Complete self-check gate. If any unchecked → go back and do it.

## Step 5: Decide (Synthesize → REVIEW)

> **Mindset:** Decision-maker. Synthesize stages into a binding verdict with cited proof.

Read all 3 stage files (map.md, verify.md, judge.md).
Write `REVIEW__*.md` using `templates/REVIEW.md` — synthesize, don't copy-paste.
- §1 Map: summarize from map.md
- §2 Verify: reference verify.md findings table
- §3 Judge: summarize from judge.md checklist
- §4 Verdict: APPROVE / REVISE / REJECT with rationale citing stage evidence

## Step 6: Tech Debt Collection

After reviewing, the reviewer MUST:
1. Read executor's `## Observations` section from RF
2. **Quality filter** — reject filler observations. Only promote items that would cause real problems if left unfixed
3. Triage each surviving item (severity: Low/Medium/High)
4. Add to REVIEW file as `## Tech Debt Collected` section
5. Append to project-level `TECH_DEBT.md`

## Step 7: Update Traces

After verdict:
1. **Update Task Board** in `README.md` — set status per verdict
2. **Update TECH_DEBT.md** — append any new items from Tech Debt Collected
3. If ✅ APPROVE: mark task as 📚 KNW in Task Board (not ✅ DONE yet)

## Step 8: Knowledge Capture (KNW)

After ✅ APPROVE verdict:
1. Run `/tfw-docs` — update KNOWLEDGE.md §1-§3 + TECH_DEBT.md
2. If Fact Candidates exist in RF/REVIEW/RES → run `/tfw-knowledge`
3. Mark both in REVIEW §6: `tfw-docs: Applied/N/A` | `tfw-knowledge: Applied/N/A`
4. When both markers are set → update Task Board status to ✅ DONE

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
- Reviewer skips observations triage — every observation must be triaged to TECH_DEBT.md
- Reviewer modifies RF or code — **🔒 Role Lock violation**
- Executor writes REVIEW file — **🔒 Role Lock violation** (start `/tfw-review` instead)
- Reviewer approves without checking DoD — each TS acceptance criterion must be verified
- Reviewer and executor are the same session — review must be a separate session/agent
- Reviewer approves without opening any files — Step 2 (Verify) requires spot-checking RF claims against actual artifacts
- **🔒 Reviewer MUST NOT write code, ONB, RF, HL, or TS** — Role Lock violation
