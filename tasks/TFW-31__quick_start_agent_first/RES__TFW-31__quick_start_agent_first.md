# RES — TFW-31: Quick Start Agent-First

**Date:** 2026-04-09
**Mode:** focused
**Researcher:** Antigravity

---

## §1 Core Finding

The current Quick Start and init.md have a **cold start problem**: they assume context that doesn't exist yet.

init.md says "Role: Coordinator" and "ROLE LOCK" — but a fresh agent doesn't know what TFW roles are. The workflow assumes AGENTS.md context loading was done first — but AGENTS.md doesn't exist yet at init time. This is a bootstrap paradox.

## §2 User Journey Analysis

### Real-world pattern (from user's actual workflow):

```
User to agent:
"Мы начинаем новый проект. [business context]. 
TFW описана здесь: /path/to/steps-framework. Сделай инициализацию проекта."
```

The agent gets:
- Access to the `.tfw/` folder
- Business context from the user
- An instruction to "initialize"

The agent reads init.md → but doesn't understand TFW concepts because there's no preamble.

### Three entry scenarios:

| Scenario | User has | Agent gets |
|----------|----------|-----------|
| **Local init** | TFW repo cloned locally, points agent at `.tfw/` | Direct file access to init.md |
| **Remote referral** | Someone said "use TFW from this repo" | Repo URL, needs to clone first |
| **Greenfield** | Nothing, just heard about TFW | Needs repo URL + explanation |

## §3 OMO Comparison (why it doesn't translate)

oh-my-openagent's approach:
- Product is **installable software** → `bunx oh-my-opencode install`
- installation.md is a **step-by-step CLI procedure** 
- Agent runs commands, configures JSON files, authenticates providers
- Self-contained because it's procedural

TFW's approach:
- Product is a **methodology** → nothing to `npm install`
- init.md is a **multi-phase agent workflow** with interviews, research, file creation
- Agent needs to understand TFW philosophy, roles, artifacts BEFORE executing
- NOT self-contained because it assumes prior context loading

## §4 Solution: Make init.md Self-Contained

**Don't create a separate QUICKSTART.md.** Enrich init.md itself with a preamble — a "Phase 0" that bootstraps context.

### What init.md needs at the top:

1. **What TFW is** (3 sentences) — so the agent understands the methodology
2. **Repository URL** — so the agent can clone if needed
3. **What to read first** — `.tfw/README.md` (philosophy), `conventions.md` (rules), `glossary.md` (terminology)
4. **For the human** — soft recommendation to read philosophy
5. **Key concepts** — roles (Coordinator/Executor), artifacts (HL/TS/RF), task lifecycle — just enough to make the rest of init.md intelligible

This is essentially the "Context Loading" that AGENTS.md would normally provide — but done inline because AGENTS.md doesn't exist yet at init time.

### What README Quick Start needs:

3 short blocks:

**Block 1: "I have TFW files locally"**
→ Tell your agent: `Read .tfw/workflows/init.md and follow it.`

**Block 2: "I want to start from scratch"**
→ `Clone https://github.com/saubakirov/trace-first-starter then read .tfw/workflows/init.md and initialize TFW in my project.`

**Block 3: "Already set up"**
→ `Read AGENTS.md, then follow .tfw/workflows/plan.md to create my first task.`

Plus FAQ.

## §5 HL Update Recommendations

| # | Section | Recommendation |
|---|---------|---------------|
| 1 | §2 Goal | Add: "Enrich init.md with self-contained preamble (Phase 0)" |
| 2 | §4 Scope | Change: 2 files Modified → init.md gets significant preamble addition (~30 lines) |
| 3 | §3 Visualization | Update Quick Start to-be to show simpler 3-block structure |

## §6 Fact Candidates

| # | Fact | Category | Source |
|---|------|----------|--------|
| 1 | init.md has a bootstrap paradox: it assumes AGENTS.md context loading, but AGENTS.md doesn't exist at init time | Architecture | Research analysis |
| 2 | TFW is a methodology, not installable software — onboarding patterns from tool frameworks (OMO, CLAUDE.md) don't translate directly | Positioning | OMO comparison |
| 3 | User's actual init pattern: point agent at `.tfw/` folder + describe business context in natural language | UX | User interview |

## §7 Conclusion

The Quick Start needs to be simpler (3 blocks, not 4 sections + FAQ sprawl), and init.md needs a self-contained preamble that bootstraps TFW context for a fresh agent. The OMO pattern of "curl this doc" doesn't work for a methodology — but "read this workflow, it's self-contained" does, IF the workflow actually explains TFW first.
