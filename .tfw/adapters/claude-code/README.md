# Claude Code Adapter

Claude Code discovers persistent guidance in root `CLAUDE.md` and legacy slash-command
copies in `.claude/commands/`. The exact 11 commands, canonical workflows, and roles are the
entries in `../manifest.yaml`; `/tfw-research` is owned by the Researcher.

## Install or Repair

1. Copy `CLAUDE.md.template` only when `CLAUDE.md` is absent. Otherwise synchronize only the
   `TFW:CLAUDE` managed block; an existing unmarked file is reported and left untouched.
2. Preserve the project identity, code standards, and all text outside the managed block.
3. Copy every manifest workflow to `.claude/commands/tfw-{command}.md`, including
   `.tfw/workflows/research/base.md` for `/tfw-research`.
4. Verify exactly 11 command files, exact source bytes, canonical roles, path resolution, and
   idempotence. Missing or extra TFW commands are failures.

Command copies are vendor discovery artifacts, not independent algorithm owners. Each opens
with the canonical workflow content; the persistent block delegates further reads to that
workflow's Read Contract.
