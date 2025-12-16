# Trace-First Workflow — A Canonical Starter

## Motivation

**The recurring pain:** with AI work, most knowledge appears in *dialogue* — goals, constraints, trade-offs — and then evaporates. We keep losing context across chats, models, and sessions. We re-explain the same project over and over. Some models (e.g., those that frequently ask to “start a new chat”) further fragment the story. Context windows end. Chats “age” or regress. Teams rotate. Six months later the code is different — and the *intent* is gone.

**Symptoms (you’ve seen these):**
- Ad-hoc threads branch and drift; no single source of truth.
- Repeated “what is this project again?” intros; duplicated Q&A.
- Model resets (or forced new chats) wipe working memory.
- Context windows truncate key decisions; long prompts get pruned.
- Deliverables ship without the “why” — hard to evolve responsibly.
- Token waste: agents reread bulky histories instead of structured traces.

**Why common fixes fail:**
- **One giant prompt**: brittle, expensive, and quickly stale.
- **Pinned notes** without ritual: decay into uncurated scrapbooks.
- **Chat exports**: linear blobs, hard to search, impossible to onboard a new agent fast.

**What a viable solution must do:**
- Provide a **single ritual** that works for *any* domain (reports, contracts, code, analytics, deployments).
- Make **traces first-class** artifacts (not an afterthought).
- Be **portable** (Markdown), **predictable** (same reading order), and **lightweight** (flat root).
- Enforce a **Summary discipline** — one short line per step — to keep progress auditable.
- Work **mid-chat** (flip ongoing conversations into project mode) and **new-chat** alike.
- Avoid flattery and vagueness: **Don’t be sycophantic**; **No placeholders**.

**The pain loop vs. the trace-first loop**

# AI Entry Point

This README is the single entrypoint for AI. It explains the *why*, the *what*, and the *how*, and contains the prompt you can paste into any chat to switch it into Trace-First Workflow project mode.

If you are AI Agent or AI chat or any instance of AI please read README and then strictly follow [AI_ENTRY_POINT.md](https://github.com/saubakirov/trace-first-starter/blob/master/AI_ENTRY_POINT.md) as a prompt and instructions.

---

## What we’re building here
- A **self-explanatory entry point**: humans and agents read `README.md` → understand values, rules, and how to proceed.
- A **CSA-first ritual**: every project/chat gets its own AGENTS.md as the first artifact.
- A **strict Summary discipline**: one line at the end of every reply, parsable and consistent.

## How to use (humans)
1) Share this repository link in any chat.
2) Ask the agent to **read README and AGENTS** (or paste them in order if browsing is off).
3) Expect one message containing **CSA, project README, TASK, and initial STEPS**.
4) Review and select next mode: Discuss/Scope | Plan | Produce | Edit/Refactor | Test/Review | Publish/Deploy.
5) Keep appending the agent’s Summary line to `STEPS.md`.

## How to use (agents)
- Read root `README.md`, then `AGENTS.md`, then `TASK.md`.
- **Self-instantiate CSA** for THIS chat (include context, deliverables, assumptions, risks).
- Produce project README, TASK, and 2–3 initial STEPS.
- End your reply with EXACTLY ONE Summary line (strict spec below).

## Values → Goals → Directions

| Layer      | We value                                                                 | This achieves                                       | Why it matters now                                  |
|-----------:|---------------------------------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|
| **Values** | Traces over code; clarity; candor;              | Reproducibility, fast onboarding, honest decisions  | AI work is dialogic; knowledge evaporates otherwise |
| **Goals**  | Convert *any* ad-hoc chat into a project in minutes                      | One ritual everywhere (Context → Analysis → Action) | Fewer resets, compounding progress                  |
| **Direction** | Canonical, flat root; teach by example; zero placeholders            | Predictable tokens; intuitive reading order         | People and agents self-orient quickly               |
| **Safety** | Local execution; no plain-text secrets                                   | Lower risk by default                               | Fits confidential/air-gapped workflows              |

---

**Artifact roles**

| File                | Role (for humans & agents)                                             |
|---------------------|-------------------------------------------------------------------------|
| `AGENTS.md`         | Role, protocol, language behavior, **no sycophancy**, **no placeholders** |
| `README.md`         | Story + rules + prompts + quick-start + examples                        |
| `TASK.md`           | Scope, boundaries, **DoD**, risks (agent drafts/updates as we go)       |
| `STEPS.md`          | One-line Summaries of progress/decisions/blockers                       |
| `digest.txt` (opt.) | Repo digest (e.g., from gitingest) once code exists                     |

---

## Quick-start (humans)

**You are mid-conversation and realize “it’s time”**
1. Copy-paste link to this repo https://github.com/saubakirov/trace-first-starter/blob/master/README.md to any AI Chat  
2. The agent will:  
   - harvest the chat history,  
   - create `AGENTS.md` for current project
   - draft/adjust `README.md` and `TASK.md` for this project,  
   - emit the first Summaries for `STEPS.md`,  
   - ask you to pick a mode: **(a) discuss, (b) implement, (c) refactor, (d) test, (e) deploy**.  
3. Approve or edit the drafts, pick a mode, continue.  
4. When a repository/codebase exists, add `digest.txt` to accelerate grounded analysis.
5. Iterate and don't forget to copy summaries to `STEPS.md`
6. This gives you ability to change AI agents and chat without loosing context.

---

## Conduct & rules (for agents and humans)

- **Language:** reply in the user’s latest message language automatically.  
- **Candor:** be direct, precise, concrete. **Don’t be sycophantic.**  
- **No placeholders:** when asked to implement, provide complete code/config and tests for critical paths.  
- **Trace discipline:** end *every* reply with a 1–3 line **Summary** (see format).  
- **Missing info:** propose concrete defaults and mark them “current version”; ask only for the *minimal* missing facts.  
- **Backwards compatibility:** keep behavior stable unless explicitly told otherwise; explain impacts.  
- **Security:** assume local execution; never request secrets in clear text; prefer environment variables and document them exactly.

**Operating modes (shared contract)**
- **Discuss** — options, invariants, risks; minimal questions.  
- **Implement** — production-ready artifacts end-to-end.  
- **Refactor** — structural improvements with rationale; avoid breakage.  
- **Test** — concrete cases/fixtures + how to run/verify.  
- **Deploy** — exact commands/config + post-checks.

---

## Why this helps (short rationale)

- **Continuity:** anyone can resume work from traces even if the code changed.  
- **Speed:** stable ritual beats ad-hoc “prompt roulette”.  
- **Quality:** decisions are explicit; risks and DoD aren’t afterthoughts.  
- **Portability:** Markdown works everywhere; no special tools required.

---

## TFW v2 Enhancements
This project implements TFW v2, adding:

- Formal CL/AG execution modes,
- Safe external execution protocol,
- Universal TS behavior rules,
- Deterministic file prefix logic (HL/TS/RF),
- Strict handling of TS in new chats,
- Human-vs-AI explicit role model,
- Enforcement of SQL-by-human rule.

These enhancements make TFW suitable for complex 
data/engineering workflows where safety, determinism, 
and reproducibility are critical.

## Execution Modes: CL (Chat Loop) and AG (Autonomous Mode)

TFW supports two execution modes:

### 1) Chat Loop Mode (CL) — Default for ANY new chat
- Trigger: user pastes a TS__*.md or asks to continue work.
- All external actions (SQL, commands, API calls, system interactions) 
  are performed by the human.
- The AI iteratively:
  - requests minimal missing context (HL/TS/RF),
  - generates exact next steps,
  - generates SQL queries or instructions,
  - waits for the user to execute and return results.

### 2) Autonomous Mode (AG)
- Trigger: user explicitly requests autonomous execution, 
  OR antigravity/agent tooling is invoked.
- All required knowledge must already exist in HL/TS/RF files.
- The AI works producing RF-files.

### Rules:
- Default = CL, unless user explicitly switches to AG.
- TS-files MUST be interpreted as CL tasks when opened in a fresh chat.
- AG mode MUST fail safely if required context is missing.

## Protocol for TS Files (Universal TS Behavior)

When an AI agent receives a TS__*.md:

1. Enter CL mode (unless AG is explicitly requested).
2. Read AGENTS.md → STEPS.md → TASK.md → HL/TS/RF relevant files.
3. Ask the user for exactly 1–3 minimal missing inputs.
4. Propose the first concrete step:
   - a SQL query,
   - a data check,
   - a command for the user,
   - or a request to provide a specific RF-file.
5. Never simulate or fabricate external data.
6. Every action must be deterministic, minimal, and safe.

## Hard Safety Constraints (Global for all TFW Agents)

- AI MUST NOT execute SQL, shell commands, or connect to external systems in CL mode.
- AI MUST base decisions ONLY on HL/TS/RF files or user-provided outputs.
- If context is insufficient → agent MUST ask a minimal clarification.

---

If you are AI Agent or AI chat or any instance of AI please strictly follow [AI_ENTRY_POINT.md](https://github.com/saubakirov/trace-first-starter/blob/master/AI_ENTRY_POINT.md) as a prompt and instructions.
