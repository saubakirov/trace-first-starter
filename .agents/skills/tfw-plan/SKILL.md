---
name: tfw-plan
description: Plan a Trace-First Workflow task and create or revise approved HL/TS artifacts. Use when the user invokes /tfw-plan, tfw-plan, or $tfw-plan, or asks for TFW task inception, scope planning, or phase specifications.
---

# TFW Plan

Use this skill as the Codex-native equivalent of `/tfw-plan`.

## Contract

- Treat `/tfw-plan`, `tfw-plan`, and `$tfw-plan` as aliases when the text reaches Codex.
- Confirm the repository contains `.tfw/`.
- Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, `KNOWLEDGE.md` if present, the `README.md` Task Board, and relevant task artifacts in that order.
- Read `.tfw/workflows/plan.md` completely before planning; it is the canonical workflow.
- Enforce the Coordinator role lock: permit HL and TS; forbid ONB, RF, RES, REVIEW, and code changes.
- Use `.tfw/templates/HL.md` and `.tfw/templates/TS.md` for new artifacts.
- Follow every gate and stop exactly where the workflow requires. Do not continue into research, handoff, execution, or review.

When the workflow routes onward, name the exact next skill, such as `$tfw-research` or `$tfw-handoff`.
