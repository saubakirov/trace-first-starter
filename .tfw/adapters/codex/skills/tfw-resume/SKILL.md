---
name: tfw-resume
description: Locate and resume a Trace-First Workflow task from its filesystem traces and Task Board state. Use when the user invokes /tfw-resume, tfw-resume, or $tfw-resume, or asks for a phase status matrix, interrupted-task continuation, or next TFW stage.
---

# TFW Resume

Use this skill as the Codex-native equivalent of `/tfw-resume`.

## Contract

- Treat `/tfw-resume`, `tfw-resume`, and `$tfw-resume` as aliases when the text reaches Codex.
- Confirm the repository contains `.tfw/`.
- Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, `KNOWLEDGE.md` if present, the `README.md` Task Board, and relevant task artifacts in that order.
- Read `.tfw/workflows/resume.md` completely before resuming; it is the canonical workflow.
- Enforce the Coordinator role lock for resume: permit read-only status analysis plus Phase HL/TS when the workflow reaches planning; forbid ONB, RF, RES, REVIEW, and code changes.
- Use artifact existence and Task Board state as evidence instead of chat memory.
- Follow the decision gate and stop exactly where the workflow requires.

Report the status matrix and name the exact next Codex skill after the user chooses a phase.
