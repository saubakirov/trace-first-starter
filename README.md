# Trace-First Workflow — A Canonical Starter (For Humans and AI)

**Short story:** In classic software, code was the main carrier of knowledge. With AI, most value appears in *dialogue*-assumptions, trade-offs, constraints — then evaporates. Six months later, code changes; intentions are lost.  
This repository makes **traces** the first-class artifact. Traces outlive code and let both humans and AI agents **reproduce** the reasoning and continue the work anywhere.

This README is the single entrypoint. It explains the *why*, the *what*, and the *how*, and contains the two “kickoff” prompts you can paste into any chat to switch it into project mode.

---

## 1) Values → Goals → Directions

| Layer      | We value                                                                 | This achieves                                       | Why it matters now                                  |
|-----------:|---------------------------------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|
| **Values** | Traces over code; clarity; candor;              | Reproducibility, fast onboarding, honest decisions  | AI work is dialogic; knowledge evaporates otherwise |
| **Goals**  | Convert *any* ad-hoc chat into a project in minutes                      | One ritual everywhere (Context → Analysis → Action) | Fewer resets, compounding progress                  |
| **Direction** | Canonical, flat root; teach by example; zero placeholders            | Predictable tokens; intuitive reading order         | People and agents self-orient quickly               |
| **Safety** | Local execution; no plain-text secrets                                   | Lower risk by default                               | Fits confidential/air-gapped workflows              |

---

## 2) What’s in the root (flat & canonical)

```

.
├─ README.md            # You are here: narrative + rules + prompts + quick-start
├─ AGENTS.md            # Governing instruction for the agent (role, protocol, Summary format)
├─ TASK.md              # Current scope, boundaries, Definition of Done, risks
├─ STEPS.md             # One-line iteration log (Summaries)
├─ KICKOFF\_midchat.txt  # Prompt to flip an ongoing chat into project mode
└─ KICKOFF\_newchat.txt  # Prompt to start a brand-new project chat

```

**Artifact roles (at a glance)**

| File                | Role (for humans & agents)                                             |
|---------------------|-------------------------------------------------------------------------|
| `AGENTS.md`         | Role, protocol, language behavior, **no sycophancy**, **no placeholders** |
| `README.md`         | Story + rules + prompts + quick-start + examples                        |
| `TASK.md`           | Scope, boundaries, **DoD**, risks (agent drafts/updates as we go)       |
| `STEPS.md`          | One-line Summaries of progress/decisions/blockers                       |
| `digest.txt` (opt.) | Repo digest (e.g., from gitingest) once code exists                     |

---

## 3) The ritual (ASCII flow)

```

\[Chat History]
|
v
\[Paste a Kickoff] --> \[Attach AGENTS.md]
\|                         |
\|                         v
\|                 Agent reads rules
v                         |
\[Agent harvests chat context]---+
|
v
\[Agent drafts README.md (this project), TASK.md]
|
v
\[Agent emits Summary --> you append to STEPS.md]
|
v
Choose Mode: (a) discuss | (b) implement | (c) refactor | (d) test | (e) deploy
|
loop (each reply always ends with a new Summary)

```

**Summary format (must end every agent reply):**  
```

**Summary**: Stage=\[Planning/Implementation/Testing/Debug/Deployment] | Iteration=N | Goal=<current objective> | Task=<specific action> | Status/Problem=<done or blocker>

```

---

## 4) Quick-start (humans)

**Scenario A — you are mid-conversation and realize “it’s time”**
1. Copy-paste **KICKOFF_midchat.txt** (see below).  
2. Immediately attach **AGENTS.md** (from this repo).  
3. The agent will:  
   - harvest the chat history,  
   - draft/adjust `README.md` and `TASK.md` for this project,  
   - emit the first Summaries for `STEPS.md`,  
   - ask you to pick a mode: **(a) discuss, (b) implement, (c) refactor, (d) test, (e) deploy**.  
4. Approve or edit the drafts, pick a mode, continue.  
5. When a repository/codebase exists, add `digest.txt` to accelerate grounded analysis.

**Scenario B — brand-new chat**
1. Copy-paste **KICKOFF_newchat.txt**.  
2. Attach **AGENTS.md**.  
3. Proceed as above.

**Token care:** the root is intentionally compact; examples live inside README and the three MD files. Agents aren’t forced to crawl extra folders.

---

## 5) Conduct & rules (for agents and humans)

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

## 6) Why this helps (short rationale)

- **Continuity:** anyone can resume work from traces even if the code changed.  
- **Speed:** stable ritual beats ad-hoc “prompt roulette”.  
- **Quality:** decisions are explicit; risks and DoD aren’t afterthoughts.  
- **Portability:** Markdown works everywhere; no special tools required.

---

## 7) Minimal examples

**Example `STEPS.md` entries**
```

\[2025-09-08] **Summary**: Stage=Planning | Iteration=1 | Goal=Initialize canonical starter | Task=Provide root files (README/AGENTS/TASK/STEPS + KICKOFFs) | Status/Problem=Ready to bootstrap any chat
\[2025-09-08] **Summary**: Stage=Discuss | Iteration=2 | Goal=Confirm DoD | Task=Draft TASK.md with scope/boundaries/risks | Status/Problem=Draft proposed; waiting for approval

```

**Example `TASK.md` DoD snippet**
- New artifact → rationale + how to verify.  
- Refactor/fix → reason + expected impact.  
- Deploy step → exact commands/config + post-checks.

---

## 8) Kickoff prompts (copy from here into any chat)

### 8.1 `KICKOFF_midchat.txt`
```

Switch this ongoing chat to Trace-First mode.

Read AGENTS.md. Harvest our chat history.
Draft now: (1) project-specific README.md, (2) TASK.md (scope, DoD, risks), (3) initial STEPS.md entries from your Summaries.
Ask me to choose: (a) discuss, (b) implement, (c) refactor, (d) test, (e) deploy.
Auto-detect my language. Be direct; **Don’t be sycophantic**. No placeholders. If data is missing, propose a “current version”.
End EVERY reply with a 1–3 line Summary for `STEPS.md`.

```

### 8.2 `KICKOFF_newchat.txt`
```

Initialize a new project in Trace-First mode.

Read AGENTS.md. From this initial goal, draft README.md and TASK.md. Produce the first STEPS.md entry from your Summary.
Ask for next mode: (a) discuss, (b) implement, (c) refactor, (d) test, (e) deploy.
Auto-detect my language. **Don’t be sycophantic**. No placeholders. Propose “current version” when uncertain.
End EVERY reply with a 1–3 line Summary for `STEPS.md`.

```

---

## 9) Maintenance & evolution

- Keep the root minimal and canonical.  
- Adjust `TASK.md` when scope changes; the agent will align future actions.  
- Enforce Summary discipline; it’s the heartbeat of continuity.  
- If the repo grows, prefer links/examples inline in README over extra folders.

---

**Start here:** pick the scenario (mid-chat or new-chat), paste the appropriate Kickoff, attach `AGENTS.md`, approve drafts, choose a mode, and keep appending Summaries to `STEPS.md`.
