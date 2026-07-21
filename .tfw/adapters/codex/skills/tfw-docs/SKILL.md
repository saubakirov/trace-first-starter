---
name: tfw-docs
description: Update Trace-First Workflow project documentation and technical debt after review. Use when the user invokes /tfw-docs, tfw-docs, or $tfw-docs, or asks to update KNOWLEDGE.md sections 1-3 or TECH_DEBT.md from RF/REVIEW results.
---

# TFW Docs

Use this skill as the Codex-native equivalent of `/tfw-docs`.

## Contract

- Treat `/tfw-docs`, `tfw-docs`, and `$tfw-docs` as aliases when the text reaches Codex.
- Confirm the repository contains `.tfw/`.
- Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, `KNOWLEDGE.md`, `TECH_DEBT.md`, the `README.md` Task Board, and the relevant REVIEW/RF in that order.
- Read `.tfw/workflows/docs.md` completely before documentation work; it is the canonical workflow.
- Enforce the Coordinator role lock: permit the documentation, convention, and debt surfaces named by the workflow; forbid code and implementation changes.
- Preserve traceability to RF, REVIEW, and task artifacts. Do not consolidate Fact Candidates into `knowledge/`; that belongs to `$tfw-knowledge`.
- Follow the triage gate and stop exactly where the workflow requires.

If Fact Candidates remain, direct the user to `$tfw-knowledge`.
