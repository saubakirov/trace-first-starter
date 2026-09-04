---
name: tfw-review
description: Command /tfw-review reviews a completed Trace-First Workflow RF against its TS, implementation, and evidence. Use for /tfw-review, a TFW verdict, RF verification, or a REVIEW artifact.
---

# /tfw-review

This repository skill implements the `/tfw-review` command.

## Contract

- Treat literal `/tfw-review` input as a command. Also accept `tfw-review` and matching natural-language requests.
- Confirm the repository contains `.tfw/`.
- Enforce the Reviewer role lock: permit review stage files and REVIEW; forbid ONB, RF, HL, TS, RES, code, and implementation changes.
- Read `.tfw/workflows/review.md` completely and follow its stage-specific Read Contract. Root
  instructions are already active; do not independently preload `AGENTS.md` or any full common
  library. Preserve separate Verify PV and Judge Purpose reads.
- Open `.tfw/templates/review/*` and `.tfw/templates/REVIEW.md` only at their stage gates; verify
  declarations against actual files/evidence and stop after the workflow's verdict/closure route.

After APPROVE, direct the user to `/tfw-docs` and `/tfw-knowledge` when the workflow requires knowledge capture.
