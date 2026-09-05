# Gather — «Что нам ещё неизвестно?»
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260905-124029_RTPSN](../../HL-TFW_20260905-124029_RTPSN.md)
> Goal: Make task-bound TFW sessions enter the intended canonical role workflow reliably before receiving a concise, evidence-selected identity.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1. Failure boundary | command not invoked | skill/proxy not loaded | canonical workflow not loaded | workflow loaded, but path uncovered or later instruction not followed |
| D2. Entry architecture | byte-identical full copy | current thin proxy + canonical workflow | strengthened minimal proxy + canonical workflow | direct single-authority entry |
| D3. Runtime evidence | file exists | source and receiver hashes match | trace records a completed read | later actions conform to the loaded workflow |
| D4. Distribution state | declared in manifest | receiver path present in checkout | installer/test can reproduce receiver | adapter is live in the observed host |
| D5. Adherence evidence | static instruction inspection | historical incident reconstruction | deterministic structural test | repeated controlled behavioural trial |
| D6. Cost surface | words/tokens read on entry | drift/parity surface | maintainer synchronization work | portability and discovery across vendors |

## Findings

### G1. The two known incidents fail at different boundaries

The source session trace is
`C:\Users\c0rpa\.codex\sessions\2026\09\02\rollout-2026-09-02T17-14-40-01a0620a-f397-7550-aa9e-a996f9ec41cf.jsonl`.
The following event pairs are adjacent completed tool results, not recollections from the
assistant's prose:

| Incident | Positive evidence | Observed deviation | Best-supported class | Classes contradicted by the trace |
|----------|-------------------|--------------------|----------------------|----------------------------------|
| CRATM title was not normalized as expected | Event 9433 reads `.agents/skills/tfw-plan/SKILL.md`; event 9434 completes. Event 9470 reads all of `.tfw/workflows/plan.md`; event 9471 completes. | The existing CRATM task was resumed, so the create-new-task branch containing the rename operation was skipped; event 9558 states that no rename call occurred. | Algorithm/path-coverage gap: the naming action existed only on the creation branch. | Non-invocation and non-load. There is no evidence that changed proxy cues caused the uncovered branch. |
| RTPSN design grammar was selected before research | Event 9570 reads the current skill and the complete plan workflow; event 9571 completes. Event 9771 nevertheless recommends `PLAN · CRATM · A`; event 9788 acknowledges that an unverified candidate was elevated before research. | A loaded uncertainty/research gate was not followed in later reasoning. | Post-load noncompliance. | Non-invocation and non-load. Loading the full workflow was not sufficient to prevent the deviation. |

Thus the known sample is `n=2`: one uncovered algorithmic path and one later compliance
failure. It contains zero observed non-invocations and zero observed canonical non-loads.
This is evidence against pure non-loading as the common explanation, but it is too small
and non-randomized to estimate a general failure rate.

### G2. The RCFR change shortened and reordered cues; it did not change topology

At commit `aa0466b74295d53abcfb9c4a0fb0e3c134fa37a2`, the `/tfw-plan` proxy changed from
154 words to 141 words. The former proxy preloaded several common and task files, then
said to read the canonical workflow before planning and follow every gate. The current
proxy puts the Coordinator Role Lock first, delegates input order to the workflow's Read
Contract, requires a complete workflow read, and retains the hard stop. The change removed
13 words and duplicate preload logic; it did not remove the complete-read requirement or
the Role Lock. Both known incidents demonstrably read the current proxy and canonical
workflow. Temporal association with RCFR therefore does not establish a measurable
entry-cue regression.

### G3. Exact 11-command census and runtime context estimate

Word counts use whitespace-delimited tokens from the checked-out UTF-8 files. Estimated
tokens use the declared, tokenizer-independent proxy `ceil(words × 4/3)`; they are planning
estimates, not API billing counts. “Effective” means the Codex route reads both its skill
proxy and the selected canonical workflow.

| Command | Proxy words | Workflow words | Effective words | Estimated tokens |
|---------|------------:|---------------:|----------------:|-----------------:|
| `/tfw-plan` | 141 | 2,150 | 2,291 | 3,055 |
| `/tfw-research` | 150 | 1,304 | 1,454 | 1,939 |
| `/tfw-handoff` | 160 | 2,013 | 2,173 | 2,898 |
| `/tfw-review` | 155 | 2,102 | 2,257 | 3,010 |
| `/tfw-resume` | 145 | 559 | 704 | 939 |
| `/tfw-docs` | 123 | 441 | 564 | 752 |
| `/tfw-knowledge` | 143 | 1,022 | 1,165 | 1,554 |
| `/tfw-release` | 140 | 464 | 604 | 806 |
| `/tfw-update` | 128 | 980 | 1,108 | 1,478 |
| `/tfw-config` | 125 | 687 | 812 | 1,083 |
| `/tfw-init` | 166 | 876 | 1,042 | 1,390 |
| **Corpus census, not one launch** | **1,576** | **12,598** | **14,174** | **18,904** |

For `/tfw-plan`, current proxy + workflow costs 2,291 words (~3,055 estimated tokens).
A valid full-copy replacement would cost 2,150 words (~2,867), saving 141 words (~188).
The pre-RCFR double-read path was 2,304 words (~3,072 if estimated on the combined word
count). `18,904` is the sum of the 11 per-command ceilings; estimating the 14,174-word
corpus once gives ~18,899. Either corpus total is only a maintenance/census measure because
a normal command does not read all 11 workflows.

### G4. Four adapters have three different states in this checkout

The manifest declares exactly four adapters and 11 commands. The inspection deliberately
separates declaration, tracked receiver presence, reproducibility, and current-host liveness.

| Adapter | Declared target | Checkout evidence | Exactness evidence | Live evidence in this session |
|---------|-----------------|-------------------|--------------------|-------------------------------|
| Codex | `.agents/skills/tfw-*/SKILL.md` plus root `AGENTS.md` block | all 11 targets present | 0/11 hash mismatches against `.tfw/adapters/codex/skills`; integration tests specify source-to-target copy | **Live**: the current host exposed all 11 repository skills and this run entered `tfw-research` through that route |
| Claude Code | `.claude/commands/tfw-*.md` plus root `CLAUDE.md` block | all 11 targets present | 0/11 hash mismatches against canonical workflows | not observable from the Codex host |
| Cursor | `.cursor/commands/tfw-*.md` plus `.cursor/rules/tfw.mdc` | no command or rule receiver present | clean-receiver tests specify the route, but the checkout has no installed target | not observable |
| Antigravity (declared) | plural `.agents/workflows/tfw-*.md` plus `.agents/rules/tfw.md` | declared plural paths absent | clean-receiver and authority tests require plural paths | not observable |
| Antigravity compatibility surface (undeclared) | singular `.agent/workflows/tfw-*.md` plus `.agent/rules/tfw.md` | all 11 workflow files and rule present | 0/11 hash mismatches against canonical workflows | not a manifest receiver and not live here |

The singular/plural difference is substantive: `.agent/workflows` is tracked and exact,
whereas the manifest-authoritative `.agents/workflows` is absent. Calling the singular
surface “installed Antigravity” without the qualifier “compatibility surface” would merge
two different claims.

### G5. Existing tests measure structure, not behavioural adherence

`docs/scripts/test_integration.py` verifies the exact four-by-eleven manifest contract,
installs into clean temporary receivers, checks declared role text, compares Codex sources
to installed skill copies, compares full-copy receivers to canonical workflows, and tests
plural Antigravity authority by injecting a singular-path mutation. These are strong
parity, routing, and reproducibility checks. They do not execute a language model, observe
whether a command was selected, or measure whether later actions obeyed a loaded workflow.

Targeted validation result: `9 passed, 66 deselected in 155.33s`. The selection covered
the manifest contract, clean receiver installation, primary and secondary routes, installed
copy parity, and plural Antigravity authority.

### G6. Official Codex mechanics separate discovery from full instruction loading

OpenAI documents skills as packages that Codex first discovers by name and description,
then fully loads when selected (“progressive disclosure”). Explicit skill invocation uses
the skill UI/`$skill-name`; repository skills are discovered under `.agents/skills`, and
symlinked skill folders are supported. Consequently:

- a thin `SKILL.md` and a linked canonical workflow are two runtime reads;
- literal `/tfw-*` is a TFW/root-instruction convention rather than the documented explicit
  `$skill-name` syntax;
- a byte-identical copy of the current canonical `plan.md` cannot simply replace the Codex
  `SKILL.md`, because the canonical file has `description` but no required skill `name`;
- a symlink-based single-authority design is technically possible for Codex only after
  restructuring a canonical file into a valid skill package; it does not automatically
  satisfy Claude, Cursor, or Antigravity receiver conventions.

Source: [OpenAI — Build skills](https://developers.openai.com/codex/skills).

### G7. A strengthened proxy can be minimal and measurable

A concrete strengthened `/tfw-plan` proxy was drafted only as a research specimen. It adds
an explicit pre-action boundary (“before task reasoning, questions, decisions, tool calls,
or durable writes”), immediately binds the Role Lock, prohibits input reordering, and says
that the proxy supplies no alternative algorithm. Including frontmatter, it is 151 words
(~202 estimated tokens): +10 words / ~14 estimated tokens over the current proxy. It would
improve the clarity and observability of the entry contract, but no evidence yet shows that
those ten words improve later cross-role adherence.

Exact counted specimen (not an implementation change):

```markdown
---
name: tfw-plan
description: Command /tfw-plan plans a Trace-First Workflow task and creates or revises HL/TS artifacts. Use for /tfw-plan, TFW task inception, scope planning, or phase specifications.
---

# /tfw-plan

This skill is an entry contract, not a second planning algorithm.

Before task reasoning, questions, decisions, tool calls, or durable writes:

1. Confirm that `.tfw/` exists.
2. Read `.tfw/workflows/plan.md` completely.
3. Bind its Coordinator Role Lock immediately.

After the read:

4. Execute the workflow Read Contract in its listed order; do not preload, replace, or reorder inputs.
5. Follow every numbered step, WAIT/STOP gate, template instruction, and hard stop. This file supplies no alternative algorithm.
6. If the workflow is missing, unreadable, or its role cannot be honored, stop and report the blocker before task action.
7. Stop when the workflow routes onward; recommend the next workflow only by its `/tfw-*` name.

The canonical workflow and `.tfw/` traces remain authoritative.
```

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Both incidents include completed proxy and canonical-workflow reads. | No controlled behavioural trial estimates architecture-specific adherence. |
| Failure classes differ: uncovered branch vs post-load noncompliance. | Other commands/adapters have no comparable live incident traces. |
| Counts cover all 11 commands and include proxy + canonical workflow. | Token figures are transparent estimates, not tokenizer measurements. |
| Four manifest adapters were separated from tracked and live state. | Cursor and manifest-declared plural Antigravity are not installed/live here. |
| Full copy, current proxy, strengthened proxy, and direct entry are technically distinguishable. | Cross-vendor direct/symlink portability remains an implementation question, not a demonstrated property. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?

Stage complete: YES
→ User decision: advance under the explicit mandate to complete Iteration 1 without a second session.
