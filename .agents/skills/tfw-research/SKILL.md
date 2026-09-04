---
name: tfw-research
description: Command /tfw-research runs structured Trace-First Workflow research and creates RES plus stage traces. Use for /tfw-research, a TFW investigation, a research iteration, or a RES artifact.
---

# /tfw-research

This repository skill implements the `/tfw-research` command.

## Contract

- Treat literal `/tfw-research` input as a command. Also accept `tfw-research` and matching natural-language requests.
- Confirm the repository contains `.tfw/`.
- Enforce the Researcher role lock: permit RES and `research/` stage files; forbid HL, TS, ONB,
  RF, REVIEW, and code.
- Read `.tfw/workflows/research/base.md` completely and follow its Read Contract. Root instructions
  are already active; do not independently preload `AGENTS.md` or any full common library.
- Let the canonical workflow select the mode and first incomplete stage template; use
  `.tfw/templates/RES.md` only at synthesis, never overwrite an earlier iteration, and obey every
  WAIT/STOP gate.

When research ends, direct the user to `/tfw-plan` so a Coordinator can apply the findings.
