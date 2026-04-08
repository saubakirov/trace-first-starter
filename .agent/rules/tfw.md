---
trigger: always_on
---

# TFW

This project follows **Trace-First Workflow**.
Version: see `.tfw/VERSION`.

- Philosophy & lifecycle: `.tfw/README.md`
- Conventions: `.tfw/conventions.md`
- Glossary: `.tfw/glossary.md`
- Templates: `.tfw/templates/` (see `tfw.templates` in `.tfw/PROJECT_CONFIG.yaml`)
- Config: `.tfw/PROJECT_CONFIG.yaml`

## Context Loading (new session)

1. `AGENTS.md` — AI role and mission
2. `.tfw/conventions.md` — formal rules
3. `.tfw/glossary.md` — terminology
4. `KNOWLEDGE.md` (if exists)
5. Relevant HL/TS/RF for current task

## Rules

- **No sycophancy.** Be direct, precise, concrete.
- **No placeholders.** All code and text must be production-ready.
- **Language.** Reply in the user's latest message language.