---
trigger: always_on
---

# TFW v3

This project follows **Trace-First Workflow v3**.

- Philosophy & lifecycle: `.tfw/README.md`
- Conventions: `.tfw/conventions.md`
- Glossary: `.tfw/glossary.md`
- Templates: `.tfw/templates/` (HL, TS, RF, ONB, REVIEW, KNOWLEDGE)
- Config: `.tfw/PROJECT_CONFIG.yaml`

## Context Loading (new session)

1. `AGENTS.md` — AI role and mission
2. `.agent/rules/conventions.md` or `.tfw/conventions.md`
3. `.agent/rules/glossary.md` or `.tfw/glossary.md`
4. `KNOWLEDGE.md` (if exists)
5. Relevant HL/TS/RF for current task

## Rules

- **No sycophancy.** Be direct, precise, concrete.
- **No placeholders.** All code and text must be production-ready.
- **Language.** Reply in the user's latest message language.
