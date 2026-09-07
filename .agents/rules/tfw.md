---
trigger: always_on
---

# TFW

This project follows Trace-First Workflow. Root instructions are already active; do not
reload them. For `/tfw-*`, open `.agents/workflows/tfw-<command>.md`, then follow the mapped
canonical workflow's Read Contract. The workflow selects all further inputs.

| Commands | Roles |
|---|---|
| `/tfw-plan`, `/tfw-resume`, `/tfw-docs`, `/tfw-knowledge`, `/tfw-release`, `/tfw-update`, `/tfw-config`, `/tfw-init` | Coordinator |
| `/tfw-research` | Researcher |
| `/tfw-handoff` | Executor |
| `/tfw-review` | Reviewer |

## Rules

- **No sycophancy.** Be direct, precise, concrete.
- **No placeholders.** All code and text must be production-ready.
- **Language.** Reply in the user's latest message language.
