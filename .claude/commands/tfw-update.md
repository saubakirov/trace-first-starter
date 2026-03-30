# TFW Update — Fetch Upstream + Compare + Sync

You are now running the **TFW Update** workflow.

## Role Lock

**🔒 COORDINATOR** — you manage framework update only. You MUST NOT write code, ONB, RF, or REVIEW.

## Instructions

1. Load context in this order:
   - `AGENTS.md`
   - `.tfw/conventions.md`
   - `.tfw/PROJECT_CONFIG.yaml` — `tfw.upstream` source URL
   - `.tfw/VERSION` — current version

2. Read and follow the canonical workflow: `.tfw/workflows/update.md`

3. Execute the update process:
   - Fetch upstream into `.tfw/.upstream/`
   - Compare versions (current vs upstream)
   - Categorize changes: 🟢 safe / 🟡 merge / 🔴 breaking
   - Generate update checklist
   - Re-sync adapter copies

## User input

$ARGUMENTS
