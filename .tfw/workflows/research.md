---
description: TFW Research — structured investigation between HL and TS, or standalone
---

# TFW Research — Structured Investigation

> **Role:** Coordinator (research mode)
> **Output:** RES file with decisions, findings, and checkpoint verdicts
> **When to use:** After HL approval (pipeline) or anytime for standalone research

> **🔒 ROLE LOCK: COORDINATOR**
> Permitted artifacts: RES only.
> Forbidden actions: writing code, writing TS/ONB/RF, executing implementation.
> Agent operates in read-only AG: reads project files and web sources, writes only to the RES file.

## Entry Modes

### Pipeline (after HL, before TS)
- Task and HL already exist
- Coordinator recommends RESEARCH with rationale, user confirms
- RES file goes into the task folder: `RES__{PREFIX}-{N}__{title}.md`

### Standalone (any time, any topic)
- No existing task required
- Create a task folder: `tasks/{PREFIX}-{N}__{title}/`
- Add to Task Board with status `🔬 RES`
- Lifecycle: `🔬 RES → ✅ DONE` or `🔬 RES → new task with full HL`

## Prerequisites

Load context in order:
1. `AGENTS.md` — agent instructions
2. `.tfw/conventions.md` — rules and naming
3. `.tfw/glossary.md` — terminology
4. `KNOWLEDGE.md` — architecture, decisions (if exists)
5. **Master HL** for the task (pipeline mode)
6. Relevant code and artifacts referenced in HL

## Process

### 1. Create RES file immediately

Use `.tfw/templates/RES.md`. Fill in the Research Context section. The RES file is a living document — update it as you go.

### 2. Run three stages (checklist, not strict sequence)

The agent must cover all three stages. Order is flexible — adapt to the situation. Each stage ends with a checkpoint where the user decides whether to continue or close.

#### Stage: Gather — "What do we NOT know?"
- Analyze HL and identify information gaps
- Autonomous search: documentation, changelogs, issues, blog posts
- Questions to user: "Do you have X? Have you tried Y? What version of Z?"
- Result: closed gaps, discovered facts

#### Stage: Extract — "What do we NOT see?"
- Study the project: code, artifacts, configs, patterns
- Questions to user: "I see X in code — intentional?", "Any context not in the project?"
- Hidden knowledge: what the user knows but hasn't shared
- Result: extracted context, implicit requirements

#### Stage: Challenge — "What do we NOT expect?"
- Alternative approaches: "What if we do X instead of Y?"
- Blind spots: edge cases, atypical scenarios
- Critique decisions from HL: what could go wrong
- Unexpected intersections: "This resembles problem Z, usually solved via..."
- Result: tested/rejected alternatives, new risks

### 3. Checkpoint after each stage

After completing a stage, present in the RES file:

```markdown
### Checkpoint: {Stage}
| Found | Remaining |
|-------|-----------|
| Fact 1 | Gap 1 |
| Fact 2 | — |

**Agent assessment:** {one sentence — is this stage sufficient}
**Recommendation:** close stage / dig deeper into {specific topic}
→ User decision: ___
```

The agent always gives a recommendation. The user decides.

### 4. Final checkpoint

After all stages, present the summary table and complexity check:

```markdown
## Final Checkpoint
| Stage | Status | Key Findings |
|-------|--------|-------------|
| Gather | ✅/🔬 | ... |
| Extract | ✅/🔬 | ... |
| Challenge | ✅/🔬 | ... |

### Complexity Check
**Question:** Is the solution proportionate to the problem? What can be removed without losing value?
**Agent assessment:** {concrete answer — what is excessive, what to keep}
→ User decision: ___

**Verdict:** Sufficient for TS / Need another pass
```

### 5. Conclude

Write the Conclusion section. One paragraph: what was researched, key decisions, value added, self-critique.

If verdict is "Need another pass" — repeat unclosed stages (pass 2+).

## Agent Behavior

- **Tone:** constructive critique + collaborative investigation, not interrogation
- **Questions:** max 3 per stage (hard limit). Focused, not scattershot.
- **Autonomy:** read project files and web sources freely. Write only to RES file.
- **Convergence:** every stage ends with a checkpoint. No infinite research.
- **Decisions table:** update continuously as findings emerge. Decisions at the top, log below.

## Limits

Configured in `.tfw/PROJECT_CONFIG.yaml` under `research:`:

| Parameter | Default | Type |
|-----------|---------|------|
| Web queries per stage | 5 | Soft |
| Project files read per stage | 15 | Soft |
| Questions to user per stage | 3 | Hard |
| Max passes | 3 | Soft |

Soft limit exceeded: inform user, continue if confirmed.
Hard limit: cannot exceed.

## Status Transitions

```
Pipeline:  🔵 HL → 🔬 RES → 🟡 TS → ...
Standalone: ⬜ TODO → 🔬 RES → ✅ DONE (or → new task)
Skip:      🔵 HL ··· 🟡 TS (user confirms skip)
```

## Anti-patterns

- Agent asks 10+ questions in a single batch (max 3 per stage)
- RESEARCH without convergence — no checkpoint, no verdict
- RES duplicates HL content instead of adding new findings
- Agent skips stages without user agreement
- Agent modifies any file other than the RES artifact
- RESEARCH becomes mandatory bureaucracy for trivial tasks (skip path must exist)
- Agent acts as interrogator instead of collaborative researcher
