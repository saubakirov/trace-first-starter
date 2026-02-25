# Trace-First Workflow v3

## Motivation

**The recurring pain:** with AI work, most knowledge appears in *dialogue* — goals, constraints, trade-offs — and then evaporates. We keep losing context across chats, models, and sessions. We re-explain the same project over and over. Some models (e.g., those that frequently ask to "start a new chat") further fragment the story. Context windows end. Chats "age" or regress. Teams rotate. Six months later the code is different — and the *intent* is gone.

**Symptoms (you've seen these):**
- Ad-hoc threads branch and drift; no single source of truth.
- Repeated "what is this project again?" intros; duplicated Q&A.
- Model resets (or forced new chats) wipe working memory.
- Context windows truncate key decisions; long prompts get pruned.
- Deliverables ship without the "why" — hard to evolve responsibly.
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
- Work with **any tool** (Claude Code, Cursor, Antigravity, any framework, plain chat) via adapters.
- Avoid flattery and vagueness: **Don't be sycophantic**; **No placeholders**.

---

## Values, Goals, Directions

| Layer | We value | This achieves | Why it matters now |
|------:|----------|---------------|-------------------|
| **Values** | Traces over code; clarity; candor | Reproducibility, fast onboarding, honest decisions | AI work is dialogic; knowledge evaporates otherwise |
| **Goals** | Convert *any* ad-hoc chat into a project in minutes | One ritual everywhere (Context → Analysis → Action) | Fewer resets, compounding progress |
| **Direction** | Canonical, flat root; teach by example; zero placeholders | Predictable tokens; intuitive reading order | People and agents self-orient quickly |
| **Safety** | Local execution; no plain-text secrets | Lower risk by default | Fits confidential/air-gapped workflows |

---

## Artifact Roles

| File | Role |
|------|------|
| `AGENTS.md` | Role, protocol, language behavior. **No sycophancy**, **no placeholders** |
| `README.md` | Story + rules + quick-start + task board |
| `TASK.md` | Scope, boundaries, **DoD**, risks |
| `STEPS.md` | One-line Summaries of progress/decisions/blockers |
| `TECH_DEBT.md` | Accumulated tech debt from reviews (observations → triage → registry) |

## Artifact Types (task-level)

| Type | Purpose | Template |
|------|---------|----------|
| **HL** (High Level) | Context, vision, phases, DoD/DoF, principles. Not a task — a "map of meaning" | `.tfw/templates/HL.md` |
| **TS** (Task Spec) | Concrete task definition: scope, steps, acceptance criteria. Self-contained | `.tfw/templates/TS.md` |
| **ONB** (Onboarding Report) | Executor's analysis before starting: questions, risks, inconsistencies | `.tfw/templates/ONB.md` |
| **RF** (Result File) | What was done, decisions, test results, mandatory observations | `.tfw/templates/RF.md` |
| **REVIEW** | Coordinator's review: checklist, verdict, tech debt collection | `.tfw/templates/REVIEW.md` |

---

## Task Lifecycle

```
⬜ TODO → 🔵 HL → 🟡 TS → 🟠 ONB → (develop) → 🟢 RF → 🔍 REV → ✅ DONE
                                                              │
                                                    ┌─────────┴─────────┐
                                                    🔄 REVISE          ❌ REJECT
                                                 (back to dev)    (new HL/TS)
                     ↓
                ❌ BLOCKED
```

**Review verdicts:**
- **✅ APPROVE** — all checks pass → close, update all traces
- **🔄 REVISE** — specific items to fix → executor iterates
- **❌ REJECT** — fundamental issues → back to HL/TS revision

---

## Workflows

TFW v3 defines three canonical workflows in `.tfw/workflows/`:

| Workflow | Role | What it does |
|----------|------|-------------|
| [plan.md](workflows/plan.md) | Coordinator | Research → write HL → review → scope decision → write TS |
| [handoff.md](workflows/handoff.md) | Executor + Coordinator | Context load → ONB → execute → RF → REVIEW |
| [resume.md](workflows/resume.md) | Coordinator | Locate task → phase status matrix → decide next phase |

These workflows describe **what** to do, not **how** (tool-agnostic). Each tool maps them to its own format:
- **Claude Code**: instructions in CLAUDE.md
- **Antigravity**: `.agent/workflows/`
- **Custom framework**: map to your framework's native format
- **Cursor**: `.cursor/rules`
- **Plain chat**: just follow the workflow file directly

---

## Execution Modes

### CL (Chat Loop) — default
- AI proposes steps, human approves/executes.
- AI does NOT execute external actions without approval.

### AG (Autonomous) — explicit request only
- AI works independently within approved TS scope.
- Makes incremental commits.
- Stops when encountering issues not covered by TS.

---

## Conduct & Rules

- **Language:** reply in the user's latest message language automatically.
- **Candor:** be direct, precise, concrete. **Don't be sycophantic.**
- **No placeholders:** when asked to implement, provide complete code/config.
- **Trace discipline:** end *every* significant reply with a Summary line.
- **Missing info:** propose concrete defaults; ask only for the *minimal* missing facts.
- **Security:** assume local execution; never request secrets in clear text; prefer environment variables.

---

## Tool Adapter Pattern

TFW v3 core lives in `.tfw/` — one copy per project. Each development tool reads its own entry point, which references `.tfw/`:

```
CLAUDE.md ──────────→ refs .tfw/
.cursor/rules/*.mdc ─→ refs .tfw/     ← single source of truth
.agent/rules/tfw.md ─→ refs .tfw/
```

Available adapter templates in `.tfw/adapters/`:

| Tool | Adapter | Entry point |
|------|---------|-------------|
| Claude Code | `adapters/claude-code/CLAUDE.md.template` | `CLAUDE.md` (project root) |
| Cursor | `adapters/cursor/tfw.mdc.template` | `.cursor/rules/tfw.mdc` |
| Antigravity | `adapters/antigravity/tfw-rules.md.template` | `.agent/rules/tfw.md` + workflows copied to `.agent/workflows/` |
| Plain chat | — | Read `.tfw/README.md` directly |

Adapters are chosen at project init. See [`.tfw/init.md`](init.md) for setup instructions.

---

## Summary Specification

Every significant reply ends with exactly one Summary line:

```
[YYYY-MM-DD] **Summary**: Stage={stage} | Iteration=N | Goal=... | Task=... | Status/Problem=...
```

Allowed stages: `Planning | Scoping | Writing | Implementation | Editing | Testing | Review | Debug | Publication | Deployment`

---

## Why This Helps

- **Continuity:** anyone can resume work from traces even if the code changed.
- **Speed:** stable ritual beats ad-hoc "prompt roulette".
- **Quality:** decisions are explicit; risks and DoD aren't afterthoughts.
- **Portability:** Markdown works everywhere; no special tools required.
- **Tool-agnostic:** same `.tfw/` works with any AI tool via adapters.

---

## Canonical Reference

TFW v3 canonical repository (read if browsing is available):
https://github.com/saubakirov/trace-first-starter
