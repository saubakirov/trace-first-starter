# ONB — TFW-11 / Phase C: Full Adapter Sync + Claude Code Restore + Version 0.5.0

> **Date**: 2026-03-30
> **Author**: Executor (AI)
> **Status**: 🟠 ONB — Awaiting answers
> **Parent HL**: [HL-TFW-11](HL-TFW-11__research_stage.md)
> **TS**: [TS Phase C](TS__PhaseC__adapter_sync_version.md)

---

## 1. Understanding

Phase C completes the TFW-11 (RESEARCH stage) task by restoring the Claude Code adapter that was lost during a branch merge, creating 4 new slash commands for post-TFW-6 workflows (research, review, release, update), updating all 3 adapter templates and the Antigravity local adapter for v0.5 (RESEARCH + Reviewer role), syncing Antigravity workflow copies, fixing init.md and .tfw/README.md desyncs from Phase B observations, and bumping the framework version from 0.4.2 to 0.5.0 with a CHANGELOG entry.

## 2. Entry Points

| Area | Files |
|------|-------|
| Backup source | Branch `backup-research` — CLAUDE.md + 5 slash commands + adapter README |
| Claude Code adapter | `CLAUDE.md` (absent on master), `.claude/commands/` (absent on master) |
| Adapter templates | `.tfw/adapters/{claude-code,cursor,antigravity}/` |
| Antigravity local | `.agent/rules/tfw.md`, `.agent/workflows/tfw-{plan,handoff}.md` |
| Framework meta | `.tfw/VERSION`, `.tfw/CHANGELOG.md`, `.tfw/PROJECT_CONFIG.yaml` |
| Init + README | `.tfw/init.md`, `.tfw/README.md` |
| Tech debt | `TECH_DEBT.md` |
| Canonical workflows (copy sources) | `.tfw/workflows/{plan,research,handoff}.md` |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | TS Step 10 says "TD-5..TD-9 → ✅ Resolved". But actual TECH_DEBT.md TD-5..TD-9 are old items from TFW-6/7/8 era (already resolved or accepted). The Phase B observations (#1-#5) were **never appended** to TECH_DEBT.md as new TD items. The Phase B REVIEW §4 claims "TD-5 through TD-9 appended" but this didn't happen. **What should I do?** Options: (a) Append Phase B obs as TD-20..TD-24 and mark them ✅; (b) Skip TECH_DEBT update since the observations are resolved by this phase; (c) Other. | **(a) Append Phase B observations as TD-20..TD-24 and immediately mark ✅ Resolved (TFW-11/C). This preserves the trace that these desyncs existed and were fixed.** |

## 4. Recommendations (suggestions, not blocking)

1. **CLAUDE.md.template is severely outdated** (35 lines, missing conduct/execution modes/slash command table). TS Step 5 says "Expand to full version from backup, apply v0.5 updates." I recommend using the backup `CLAUDE.md` as the basis for the template, replacing project-specific values with `{placeholders}`, adding RES and 9-command table. This is within scope but the approach deserves explicit confirmation.
2. **`.agent/workflows/tfw-handoff.md` already synced** — diff is empty. TS Step 8 says "Re-copy (has pre-reviewer content)" but this is false: the canonical handoff.md and local copy are **identical**. The copy operation is harmless but unnecessary. I'll execute it anyway per TS.
3. **Antigravity workflows need YAML frontmatter** for slash-command registration. The canonical `.tfw/workflows/` files have `description:` frontmatter. When copying to `.agent/workflows/`, these are preserved. This is correct — no action needed.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **Summary Discipline reference** — backup CLAUDE.md (line 12) says "Summary discipline: End every significant reply with a TFW Summary line." This was deprecated in TFW-4 (replaced by Trace Discipline). The template also has it (line 29). Both should be updated to "Trace discipline" during v0.5 edits.
2. **Scope budget heavily exceeded** — TS acknowledges 24 files vs ≤7 budget. All operations are mechanical (restore/copy/edit-one-line), but I'll proceed strictly step-by-step to avoid errors.

## 6. Inconsistencies with Code (spec vs reality)

1. **TS §2 Group A says 7 files, Group B says 4 new, but actual `.claude/commands/` on backup has exactly 5 files** — plan (✓), handoff (✓), resume (✓), docs (✓), task (✓). No inconsistency with TS — the 7 in Group A includes CLAUDE.md (1) + 5 commands (5) + adapter README (1) = 7. Correct.
2. **TS §2 Group D says "Re-copy handoff.md (has pre-reviewer content)"** — but actual diff shows canonical handoff.md and Antigravity copy are identical. No pre-reviewer content remains. The copy is a no-op but not harmful.
3. **TS references `.agent/workflows/tfw-research.md` as NEW** — confirmed: this file does not exist in `.agent/workflows/`. Correct.

---

*ONB — TFW-11 / Phase C: Full Adapter Sync + Claude Code Restore + Version 0.5.0 | 2026-03-30*
