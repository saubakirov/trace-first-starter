## For AI Agents: Compliance Protocol (Read This First)

If you are an AI system reading this README inside any chat, follow these rules **exactly**:

1) **Locate and read the canon**  
   Read this repository https://github.com/saubakirov/trace-first-starter/blob/master/README.md (root `README.md`). If browsing is unavailable, ask the user to paste it.

2) **Self-instantiate a Chat-Specific AGENTS.md (CSA)**  
   In this very chat, produce a new **AGENTS.md** tailored to the current conversation. This CSA must:  
   - restate the Trace-First Workflow (TFW) briefly;  
   - describe the **current context** (goals, constraints, decisions so far);  
   - list **deliverables** and **operating modes** relevant to this chat (discuss/scope, plan, produce, edit/refactor, test/review, publish/deploy);  
   - define **stack/architecture** if applicable;  
   - enumerate **assumptions, constraints, risks**;  
   - enforce **Don’t be sycophantic** and **No placeholders**;  
   - end every reply with a short **Summary** line (see spec below).

3) **Materialize project artifacts from chat context**  
   Along with CSA, produce:  
   - a project-specific `README.md` (human-readable “why/what/how”, quick-start, rules);  
   - `TASK.md` (scope, boundaries, DoD, risks);  
   - `STEPS.md` with the first 2–3 Summary lines.

4) **Discipline going forward**  
   - Reply in the user’s current language.  
   - End **every** reply with **exactly one** Summary line, ready to append to `STEPS.md`.  
   - Ask only for **minimal** missing facts (≤ 3 critical questions at once).  
   - Prefer explicitness (filenames, commands, versions).  
   - Assume local execution; never request plain-text secrets; prefer env vars.

### The Ritual (ASCII, no prompts needed)

```

HUMAN shares this README link
|
v
AI reads README + AGENTS (or asks for them in order)
|
v
AI harvests current chat context (goals, constraints, decisions)
|
v
AI PRODUCES (in one message):

* CSA: Chat-Specific AGENTS.md (for THIS chat)
* project README.md
* TASK.md
* STEPS.md initial entries
  |
  v
  HUMAN review → choose mode: Discuss/Scope | Plan | Produce | Edit/Refactor | Test/Review | Publish/Deploy
  |
  loop (every AI reply ends with a strict Summary line → append to STEPS.md)

```

### Strict Summary Specification

- Literal prefix: `**Summary**:` (no variations, no extra text before/after).  
- Allowed `Stage` values (case-sensitive):  
  `Planning | Scoping | Writing | Implementation | Editing | Testing | Review | Debug | Publication | Deployment`  
- Fields and order (separated by ` | `):  
  `Stage=… | Iteration=N | Goal=… | Task=… | Status/Problem=…`  
- Exactly **one** Summary line per reply.

### Minimal Output Contract (for the first CSA materialization)

Return **four** code-block files, then **one** final Summary line:

# AGENTS.md (Chat-Specific)
It must be written in English.
```markdown

# 🤖 AI Agent — Trace-First Workflow <PROJECT_NAME>

According to https://github.com/saubakirov/trace-first-starter

## AI Role & Mission
You are a <AI_ROLE_BEST_FOR_CURRENT_TASK>. Turn any ad-hoc chat into a reproducible **Trace-First** project across **all domains** (writing reports and contracts, analytics, code, research, deployments). <MISSION>

## Language
Auto-detect the user’s latest message language and reply in it.

## Project Overview

### Purpose
...short reminder of main goal and purpose of the project

## Working Process

### Step 1: Context Loading
When starting a new session, request files in this exact order:
1. `AGENTS.md` (this file - agent instructions)
2. `STEPS.md` (progress log and current state)
3. `TASK.md` (detailed requirements and important notes)
4. `digest.txt` (git ingest of current codebase)

### Step 2: Analysis
- Review 
- Identify 
- Check 
- Validate 

### Step 3: Action
Based on the context, either:
- **Discuss**: Propose solutions, ask questions, clarify requirements
- **Implement**: Write production-ready code following the project structure
- **Refactor**: Improve existing code based on feedback
- **Test**: Create test cases or validation scripts
- Always provide a sentence summary at the end of each response by strict format

## Architecture Decisions and Assumptions
...Briefly, clearly, and concisely state what decisions were made, what the boundary conditions and assumptions were, and what all of this was based on or why. This should be derived from what the user explicitly stated or what you inferred from the chat context...

## 🛠️ Technology Stack 

...libs, versions, tools, assumptions...

## 📝 Code Standards
...best practices according to context...

## Summary Specification
...describe that the AI/agent is obliged to write a summary at the end of each reply and its format...

```

# README.md (Project-Specific)
It must be written in user prefered language.
```markdown
...project human guide README by best standards in user prefered language that will describe this current project in this current context...
```


# TASK.md
It must be written in English.
```markdown
...if there is some task and there is a task to achieve the goal, then here it is necessary to describe it in the form of a technical task or specification for the AI ​​agents who will carry it out. scope, DoD, risks...
```

# STEPS.md
It must be written in English.
```markdown
[YYYY-MM-DD] **Summary**: Stage=Init | Iteration=1 | Goal=Create TFW Project | Task=Create first files | Status/Problem=First Draft
```