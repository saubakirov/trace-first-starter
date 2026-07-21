---
name: tfw-research
description: Run structured Trace-First Workflow research and create RES plus research stage traces. Use when the user invokes /tfw-research, tfw-research, or $tfw-research, or requests a TFW investigation, research iteration, or RES artifact.
---

# TFW Research

Use this skill as the Codex-native equivalent of `/tfw-research`.

## Contract

- Treat `/tfw-research`, `tfw-research`, and `$tfw-research` as aliases when the text reaches Codex.
- Confirm the repository contains `.tfw/`.
- Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, `KNOWLEDGE.md` if present, the `README.md` Task Board, the master HL, and research control files in that order.
- Read `.tfw/workflows/research/base.md` completely before research; it is the canonical workflow.
- Enforce the Researcher role lock: permit RES and `research/` stage files; forbid HL, TS, ONB, RF, REVIEW, and code changes.
- Use `.tfw/templates/RES.md` and `.tfw/templates/research/*` for new artifacts.
- Respect `research/iterations.yaml`, resume the first incomplete stage, and never overwrite prior iteration folders.
- Follow every WAIT/STOP gate and stop after RES exactly as the workflow requires.

When research ends, direct the user to `$tfw-plan` so a Coordinator can apply the findings.
