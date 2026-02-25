# TASK — Trace-First Starter

## Purpose
Canonical public starter for Trace-First Workflow (TFW) v3. Provides templates, workflows, conventions, and tool adapters for any project.

## Scope
- Maintain `.tfw/` as the single source of truth for TFW v3
- Provide ready-to-fork structure for new projects
- Support multiple development tools via adapter pattern

## Definition of Done (project-level)
- AI handles tasks **end-to-end** without manual editing of results — only prompts (intent) are edited by humans
- Every decision is **traceable** to a specific instruction or context
- Tasks are **atomic** and verifiable by the user
- New project can be initialized from this starter in **< 5 minutes** via `.tfw/init.md`

## Risks
- TFW v3 changes not reflected in starter → keep canonical files in sync
- Too many files intimidate newcomers → `.tfw/init.md` guides step-by-step
- Tool adapter drift → adapters reference `.tfw/`, never duplicate

## Backlog
See Task Board in `README.md`.
