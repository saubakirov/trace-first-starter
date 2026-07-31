---
trigger: always_on
---

# TFW

This project follows **Trace-First Workflow**.
Version: see `.tfw/VERSION`.

- Philosophy & lifecycle: `.tfw/README.md`
- Conventions: `.tfw/conventions.md`
- Glossary: `.tfw/glossary.md`
- Templates: `.tfw/templates/` (see `tfw.templates` in `.tfw/project_config.yaml`)
- Config: `.tfw/project_config.yaml`

## Context Loading (new session)

1. `AGENTS.md` — AI role and mission
2. `.tfw/conventions.md` — formal rules
3. `.tfw/glossary.md` — terminology
4. `KNOWLEDGE.md` (if exists)
5. Relevant HL/TS/RF for current task

## Commit Identity Consumer

- **Registered surface:** `antigravity`. This adapter supplies only that surface.
- The active workflow supplies the explicit task, work slice, Role Lock, and operation;
  do not infer them from a branch, prior subject, path coincidence, model, or session.
- Immediately before any workflow-owned current-repository commit action, consume
  `.tfw/scripts/commit_identity_router.py` exactly as the canonical workflow directs
  and use its validated local subject.
- A routed local subject is declared provenance only. It does not authenticate an
  actor or authorize push, remote tags, deploy, publish, or notify.

## Rules

- **No sycophancy.** Be direct, precise, concrete.
- **No placeholders.** All code and text must be production-ready.
- **Language.** Reply in the user's latest message language.
