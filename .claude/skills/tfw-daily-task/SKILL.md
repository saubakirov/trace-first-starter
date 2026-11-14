---
name: tfw-daily-task
description: Do one bounded everyday request in a TFW project (a fix, a document, an analysis, a small change) without the Full HL/TS/RF/REVIEW cycle - check that no formal task owns the object, keep a short record under daily/ with a checkpoint before the first product edit, run a focused check, and keep prepared, checked, accepted and released apart. Use when asked to "do it as a daily task", "/tfw-daily-task", "a quick task without a full cycle", "continue the daily record", or when the owner gives a clear bounded request outside an active formal task.
allowed-tools:
  - Bash(python .tfw/extensions/daily-task/scripts/*)
  - Bash(python3 .tfw/extensions/daily-task/scripts/*)
  - Bash(py .tfw/extensions/daily-task/scripts/*)
  - PowerShell(python .tfw/extensions/daily-task/scripts/*)
  - PowerShell(python3 .tfw/extensions/daily-task/scripts/*)
  - PowerShell(py .tfw/extensions/daily-task/scripts/*)
---

# TFW Daily Task entry

Resolve the receiving project root and read `.tfw/extensions/daily-task/SKILL.md` completely before
task action. Follow that canonical skill's ordered context and authority gates and selected local
record form. A missing or ambiguous canonical source stops this route. This entry adds no algorithm
and is not a formal Full role command.
