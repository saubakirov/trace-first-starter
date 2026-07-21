---
name: tfw-review
description: Review a completed Trace-First Workflow RF against its TS, implementation, and evidence. Use when the user invokes /tfw-review, tfw-review, or $tfw-review, or asks for a TFW verdict, RF verification, or REVIEW artifact.
---

# TFW Review

Use this skill as the Codex-native equivalent of `/tfw-review`.

## Contract

- Treat `/tfw-review`, `tfw-review`, and `$tfw-review` as aliases when the text reaches Codex.
- Confirm the repository contains `.tfw/`.
- Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`, `KNOWLEDGE.md` if present, the `README.md` Task Board, master/phase HL, TS, RF, evidence, and files needed to verify claims in that order.
- Read `.tfw/workflows/review.md` completely before review; it is the canonical workflow.
- Enforce the Reviewer role lock: permit review stage files and REVIEW; forbid ONB, RF, HL, TS, RES, code, and implementation changes.
- Use `.tfw/templates/review/*` and `.tfw/templates/REVIEW.md` for new artifacts.
- Verify RF claims against actual files, test output, and resolvable evidence; do not trust declarations alone.
- Follow the review-mode WAIT gate and every later gate exactly as the workflow requires.

After APPROVE, direct the user to `$tfw-docs` and `$tfw-knowledge` when the workflow requires knowledge capture.
