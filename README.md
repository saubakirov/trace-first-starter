# Trace-First Workflow (TFW) v3 — Canonical Starter

## What is TFW?

**Trace-First Workflow** is a methodology for structured AI-human collaboration that works across **any domain** — code, analytics, reports, contracts, research, deployments. It turns ad-hoc conversations into reproducible projects by making **traces first-class artifacts**.

The core problem: with AI work, most knowledge appears in *dialogue* — goals, constraints, trade-offs — and then evaporates. TFW solves this with a single ritual: capture context, structure decisions, deliver results — all tracked through one-line Summary entries.

For the full philosophy, motivation, and design rationale, see [`.tfw/README.md`](.tfw/README.md).

## Quick Start

1. Fork/clone this repository
2. Follow [`.tfw/init.md`](.tfw/init.md) to set up your project
3. Choose your tool adapter (Claude Code, Cursor, Antigravity, or plain chat)
4. Start with [`.tfw/workflows/plan.md`](.tfw/workflows/plan.md)

## What's Inside

### Root Files (your project)

| File | Purpose |
|------|---------|
| `README.md` | Project guide + Task Board |
| `AGENTS.md` | AI agent role and behavior |
| `TASK.md` | Scope, DoD, risks |
| `STEPS.md` | Progress journal (Summary lines) |
| `TECH_DEBT.md` | Tech debt registry |

### .tfw/ (TFW core — tool-agnostic)

| Path | Contents |
|------|----------|
| `.tfw/README.md` | Philosophy, values, lifecycle |
| `.tfw/conventions.md` | Formal rules (statuses, naming, scope budgets, anti-patterns) |
| `.tfw/glossary.md` | Terminology |
| `.tfw/templates/` | Canonical templates (HL, TS, RF, ONB, REVIEW) |
| `.tfw/workflows/` | Process workflows (plan, handoff, resume) |
| `.tfw/adapters/` | Tool adapter templates |
| `.tfw/init.md` | Setup instructions |
| `.tfw/PROJECT_CONFIG.yaml` | Project parameters |

## Values → Goals → Directions

| Layer | We value | This achieves | Why it matters now |
|------:|----------|---------------|-------------------|
| **Values** | Traces over code; clarity; candor | Reproducibility, fast onboarding, honest decisions | AI work is dialogic; knowledge evaporates otherwise |
| **Goals** | Convert *any* ad-hoc chat into a project in minutes | One ritual everywhere (Context → Analysis → Action) | Fewer resets, compounding progress |
| **Direction** | Canonical, flat root; teach by example; zero placeholders | Predictable tokens; intuitive reading order | People and agents self-orient quickly |
| **Safety** | Local execution; no plain-text secrets | Lower risk by default | Fits confidential/air-gapped workflows |

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

## Conduct & Rules

- **Language:** reply in the user's latest message language automatically.
- **Candor:** be direct, precise, concrete. **Don't be sycophantic.**
- **No placeholders:** when asked to implement, provide complete code/config.
- **Trace discipline:** end *every* significant reply with a Summary line.
- **Missing info:** propose concrete defaults; ask only for the *minimal* missing facts.
- **Security:** assume local execution; never request secrets in clear text; prefer environment variables.

Full rules in [`.tfw/conventions.md`](.tfw/conventions.md).

## Tool Adapters

TFW v3 works with any development tool via adapters. Templates are in `.tfw/adapters/`:

| Tool | Adapter location | Project entry point |
|------|-----------------|---------------------|
| Claude Code | `.tfw/adapters/claude-code/` | `CLAUDE.md` (project root) |
| Cursor | `.tfw/adapters/cursor/` | `.cursor/rules/tfw.mdc` |
| Antigravity | `.tfw/adapters/antigravity/` | `.agent/rules/tfw.md` |
| Plain chat | — | Read `.tfw/README.md` directly |

See [`.tfw/init.md`](.tfw/init.md) for setup.

## Why This Helps

- **Continuity:** anyone can resume work from traces even if the code changed.
- **Speed:** stable ritual beats ad-hoc "prompt roulette".
- **Quality:** decisions are explicit; risks and DoD aren't afterthoughts.
- **Portability:** Markdown works everywhere; no special tools required.
- **Tool-agnostic:** same `.tfw/` works with any AI tool via adapters.

## Canonical Reference

TFW v3 canonical repository:
https://github.com/saubakirov/trace-first-starter

---

## Task Board

| ID | Task | Status | HL | TS | ONB | RF | REV |
|----|------|--------|----|----| --- |----| --- |

> Statuses: ⬜ TODO → 🔵 HL → 🟡 TS → 🟠 ONB → 🟢 RF → 🔍 REV → ✅ DONE | ❌ BLOCKED
