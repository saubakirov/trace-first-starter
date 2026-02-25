# HL — TFW-3: Root README Public-Readiness

> **Date**: 2026-02-25
> **Author**: Antigravity (coordinator)
> **Status**: ✅ Approved → executed

---

## 1. Vision

Root README.md is the **canonical TFW project README** — compact landing page for the GitHub repo. Since this project *is* TFW, it includes brief motivation, but all deep content (thesis, lifecycle details, anti-patterns, scope budgets, evolution) lives in `.tfw/README.md` (the "paper"). No duplication — only one-line refs with anchor links.

## 2. Content Distribution (approved)

| Section | Root README | .tfw/README.md |
|---------|:-----------:|:--------------:|
| Brief motivation | ✅ 3-5 sentences | ✅ full "Knowledge Evaporates" |
| Thesis (Traces Over Code) | ❌ | ✅ |
| Who This Is For | ✅ | ✅ |
| Quick Start (new + mid-chat) | ✅ | ✅ |
| What's Inside (file tables) | ✅ | ✅ (tree) |
| Tool Adapters | ✅ table | ✅ pattern + diagram |
| Task Lifecycle | one-line + link | ✅ full diagram + 7 steps |
| Scope Budgets | one-line + link | ✅ table + rationale |
| Execution Modes (CL/AG) | one-line + link | ✅ full description |
| Conduct & Rules | one-line + link | ✅ full list |
| Values table | ❌ removed | ✅ "Values and Principles" |
| Anti-patterns | ❌ | ✅ list |
| Roles | ❌ | ✅ table |
| Evolution (v1→v3) | one-line + link | ✅ full history |
| Success Criteria | ❌ (in TASK.md) | ✅ |
| Author / Links | ✅ | ✅ |
| License | ✅ + LICENSE file | ❌ |
| Task Board | ✅ | ❌ |

## 3. Scope

- 1 rewrite (README.md, ~100 lines)
- 1 new file (LICENSE, MIT)
- 1 update (STEPS.md)

## 4. DoD

- [x] README compact landing, no section duplication with .tfw/README.md
- [x] Key Concepts as one-line refs with anchor links to .tfw/README.md
- [x] Public-repo metadata: Who This Is For, Author, License
- [x] Quick Start: new project + mid-conversation paths
- [x] Task Board preserved at bottom

---

*HL — TFW-3: Root README Public-Readiness | 2026-02-25*
