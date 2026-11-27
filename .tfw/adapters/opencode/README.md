# OpenCode Adapter

OpenCode discovers persistent project guidance in root `AGENTS.md` and project commands in
`.opencode/commands/<name>.md`; the file name is the command name. The exact manifest commands,
canonical workflows and roles are the entries in `../manifest.yaml`; `/tfw-research` is owned by
the Researcher.

## Install or Repair

1. Copy `AGENTS.md.template` only when `AGENTS.md` is absent. Otherwise synchronize only the
   `TFW:OPENCODE` managed block. A file without `TFW:OPENCODE` markers, including one that holds
   only a `TFW:CODEX` block, is reported and left untouched; the operator inserts the block once,
   and later syncs replace only that range. The `TFW:CODEX` block stays as it is.
2. Preserve the project identity, code standards and all text outside the managed block.
3. Copy every manifest workflow to `.opencode/commands/tfw-{command}.md`, including
   `.tfw/workflows/research/base.md` for `/tfw-research`. Preserve unrelated commands.
4. If the project keeps rules in `CLAUDE.md` next to `AGENTS.md`, report that OpenCode will not
   load them unless `opencode.json` lists `"instructions": ["CLAUDE.md"]`. The file is
   project-owned: change it only with the owner's approval.
5. Verify exactly the manifest command files, exact source bytes, canonical roles, path
   resolution, one managed block and idempotence. Missing or extra TFW commands are failures.

Command copies are vendor discovery artifacts, not independent algorithm owners. Each opens
with the canonical workflow content; the persistent block delegates further reads to that
workflow's Read Contract.

## Discovery facts

These facts come from the OpenCode source and documentation, not from a live TFW session:

- Command files: OpenCode reads YAML frontmatter (`description`, `agent`, `model`, `subagent`)
  and uses the body as the prompt template. The canonical workflows carry only `description`.
- Arguments: `$ARGUMENTS` and `$1`, `$2`, … are substituted, and `` !`cmd` `` runs a shell
  command. A template without placeholders receives non-empty arguments after a blank line, so
  `/tfw-plan TFW-12` delivers the workflow followed by `TFW-12`. A workflow edit that introduces
  `$<digit>`, `$ARGUMENTS` or `` !` `` changes OpenCode behavior and must be checked here.
- OpenCode does not read `.claude/commands/`. It reads skills from `.opencode/skills/`,
  `.claude/skills/` and `.agents/skills/`, so the Feedback skill installed for Codex,
  Antigravity or Claude Code is also discovered.
- Rules: in a directory with `AGENTS.md`, `CLAUDE.md` is skipped. `OPENCODE_DISABLE_CLAUDE_CODE`
  also skips `.claude` skills.

## Coordination

The adapter is common-only, like Cursor: no provider Coordinator profile is installed and no
tailored native offer is made. OpenCode subagent and addressed-messaging capabilities are not
verified for TFW role units; a profile needs that evidence first.

Economics is installed/updated by default from the manifest with selected adapters and resolves
`.tfw/workflows/economics.md`. Four formal roles remain; analysis retains an active Role Lock.
Optional Daily has no OpenCode entry; its installation contract names the supported receivers.
