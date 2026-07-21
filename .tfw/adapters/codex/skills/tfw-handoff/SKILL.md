---
name: tfw-handoff
description: Execute an approved Trace-First Workflow TS and create ONB, implementation changes, evidence, and RF. Use when the user invokes /tfw-handoff, tfw-handoff, or $tfw-handoff, or asks Codex to implement an approved TFW task or phase.
---

# TFW Handoff

Use this skill as the Codex-native equivalent of `/tfw-handoff`.

## Contract

- Treat `/tfw-handoff`, `tfw-handoff`, and `$tfw-handoff` as aliases when the text reaches Codex.
- Confirm the repository contains `.tfw/`.
- Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, `KNOWLEDGE.md` if present, the `README.md` Task Board, master HL, phase HL, approved TS, referenced artifacts, and relevant implementation files in that order.
- Read `.tfw/workflows/handoff.md` completely before execution; it is the canonical workflow.
- Enforce the Executor role lock: permit ONB, RF, evidence, and implementation changes within the approved TS; forbid HL, TS, RES, REVIEW, and scope changes.
- Use `.tfw/templates/ONB.md`, `.tfw/templates/evidence/EV.md`, and `.tfw/templates/RF.md` at their workflow gates.
- Check the configured scope budget before implementation. Record out-of-scope findings without modifying them.
- Follow every approval and build gate, then stop after RF exactly as the workflow requires.

When RF is complete, direct the user to `$tfw-review`.
