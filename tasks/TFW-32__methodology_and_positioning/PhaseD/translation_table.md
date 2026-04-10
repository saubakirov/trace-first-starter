# Translation Table — TFW Terms → Business Language

> **Pattern**: DORA model (technical metric → business value explanation)
> **Principle**: Translation, not simplification — TFW term stays primary, business equivalent is alias
> **Source**: D5 (RES1), G2 (gather.md — DORA/Shape Up/Scrum Guide patterns)

---

## How to Read This Table

The **TFW Term** column is the canonical name used in all TFW artifacts. The **Business Equivalent** is the translation for non-technical audiences — product leaders, analysts, and stakeholders. The **Context** column explains what the concept does in plain language.

TFW terms are precise by design (D28: "Naming Creates Behavior"). Business equivalents are approximations that sacrifice precision for accessibility. When writing for technical audiences, use TFW terms. When writing for business audiences, use business equivalents — but always link back to the canonical name.

---

## Artifact Types

| TFW Term | Business Equivalent | Context |
|----------|-------------------|---------|
| **HL** (High Level) | Strategic brief | The "map of meaning" for a task — defines why it matters, what constraints exist, which alternatives were considered and rejected. Not a task assignment; a context document that ensures everyone (human and AI) understands the problem the same way |
| **TS** (Task Spec) | Work order / Implementation brief | Self-contained instructions for executing a task: what to do, what "done" looks like, what's in and out of scope. Anyone with this document can start work without additional context gathering |
| **RF** (Result File) | Delivery report | What was done, which decisions were made during execution, what was observed but not changed, and any deviations from the work order. The primary source of truth for completed work |
| **RES** (Research Report) | Investigation report | Structured research output: hypotheses tested, evidence gathered, decisions reached, alternatives rejected. Preserves the reasoning that led to the task spec — not just the conclusion |
| **ONB** (Onboarding Report) | Pre-flight checklist | Executor's understanding check before starting: "Here's what I think the task is. Here are my questions. Here are the risks I see." Prevents miscommunication before work begins |
| **REVIEW** | Quality gate report | Formal assessment: did the delivery meet the spec? 9-point checklist, verdict (approve / revise / reject), and triage of issues found into the backlog |

## Process Concepts

| TFW Term | Business Equivalent | Context |
|----------|-------------------|---------|
| **Task Board** | Project dashboard | Single view of all tasks and their statuses — from planned to completed. Lives in README.md. The one place to answer "where does the project stand?" |
| **Knowledge Pipeline** | Institutional memory engine | The end-to-end process that captures raw observations during work, verifies them through review, and compounds them into structured project knowledge. Over time, the project accumulates a searchable, reliable knowledge base that makes every new decision better |
| **Pipeline status** | Workflow stage | Where a task is in its lifecycle. Nine stages from "planned" through "executing" to "knowledge captured and closed." Each stage has a specific artifact and a specific purpose |
| **Knowledge Gate** | Periodic checkpoint | A structured pause: "Have we captured what we learned from the last task?" Prevents knowledge loss by gating new work on knowledge capture from completed work |
| **Scope Budget** | Guardrails | Configurable limits per work unit — maximum files, maximum lines of change, maximum new components. Prevents the common failure mode where a "small change" spirals into an unreviable mess. Calibrated for AI agent capacity |
| **Trace** | Decision record | The complete record of reasoning behind a change: what prompted it, what was considered, what was rejected, what constraints existed, what the final decision was. Not just a log — a structured chain of reasoning that makes the decision reproducible |
| **Trace Discipline** | Documentation-by-working | The principle that every task produces traces as a byproduct of the work itself. Nobody writes documentation separately — the methodology captures it during planning, research, execution, and review |

## Roles

| TFW Term | Business Equivalent | Context |
|----------|-------------------|---------|
| **Coordinator** | Strategic planner | Plans tasks, writes specs, reviews results. Does NOT execute the work. Owns the "what" and "why" — the team owns the "how." (Parallel: Scrum Guide's Product Owner as "Value Maximizer" per G2) |
| **Executor** | Implementer | Reads the spec, does the work, delivers results. Cannot change scope — if the spec is wrong, flags it and stops. Separation prevents scope creep and ensures quality gates work |
| **Researcher** | Investigator | Conducts structured investigation between planning and execution. Tests hypotheses, gathers evidence, recommends changes to the plan. Does NOT plan or execute — only investigates and reports |
| **Reviewer** | Quality auditor | Checks delivery against spec. Cannot fix issues — only report them. Separation ensures the reviewer doesn't "clean up" execution problems that should be flagged and fixed properly |
| **Role Lock** | Separation of duties | Each role has strict permissions: what artifacts it can create, what it cannot touch. No role crossover. Prevents the common AI failure mode where the planner starts executing, or the executor rewrites the plan |

## Knowledge Capture

| TFW Term | Business Equivalent | Context |
|----------|-------------------|---------|
| **Fact Candidates** | Observed findings (unverified) | Raw observations recorded during work: patterns noticed, numbers discovered, stakeholder preferences observed. Not verified yet — they become verified facts after formal consolidation. Think of them as field notes |
| **Strategic Insights** | Domain intelligence | Human-sourced knowledge that can't be learned from project files: stakeholder priorities, market context, business constraints, domain patterns. The things that only the person (not the AI) knows |
| **KNOWLEDGE.md** | Architecture index | Central map of the project: structure, key decisions, legacy systems, and a pointer to verified knowledge topics. The "table of contents" for everything the project knows about itself |
| **TECH_DEBT.md** | Issue backlog (known shortcuts) | Registry of known shortcuts, deferred improvements, and observed problems — triaged by severity, not forgotten. Every item has a source (which review found it) and a severity (how urgently it needs fixing) |
| **Topic files** (`knowledge/`) | Verified knowledge base | Per-category files containing facts that have been verified through formal consolidation. Categories: philosophy, process, convention, constraint, domain, stakeholder, environment, risk, context |

---

## Usage Guide

### In README / external communications
Use **Business Equivalent** column. Example:
- "Every task produces a **delivery report** (RF) documenting what was done and why"
- "The **institutional memory engine** captures knowledge automatically"

### In TFW artifacts / internal work
Use **TFW Term** column. Example:
- "Write the RF documenting execution results"
- "Run /tfw-knowledge to consolidate fact candidates"

### In mixed audiences (presentations, demos)
Use both with parenthetical: "The **strategic brief** (what TFW calls an HL)..."

---

*Translation Table — TFW Terms → Business Language | 2026-04-10*
*Pattern: DORA (G2). Sources: D5, D28 (RES1), S1-S2 (HL §11)*
