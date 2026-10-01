# Claude Code Adapter

Claude Code discovers persistent guidance in root `CLAUDE.md` and legacy slash-command
copies in `.claude/commands/`. The exact manifest commands, canonical workflows, and roles are the
entries in `../manifest.yaml`; `/tfw-research` is owned by the Researcher.

## Install or Repair

Standard `/tfw-economics` uses `.claude/commands/tfw-economics.md`, a canonical workflow
copy. Daily alone uses explicitly selected `.claude/skills/` thin discovery. Read core migration
before replacing/retiring old optional Economics aliases; preserve custom/history.

1. Copy `CLAUDE.md.template` only when `CLAUDE.md` is absent. Otherwise synchronize only the
   `TFW:CLAUDE` managed block; an existing unmarked file is reported and left untouched.
2. Preserve the project identity, code standards, and all text outside the managed block.
3. Copy every manifest workflow to `.claude/commands/tfw-{command}.md`, including
   `.tfw/workflows/research/base.md` for `/tfw-research`.
4. Verify exactly the manifest command files, exact source bytes, canonical roles, path resolution, and
   idempotence. Missing or extra TFW commands are failures.

Command copies are vendor discovery artifacts, not independent algorithm owners. Each opens
with the canonical workflow content; the persistent block delegates further reads to that
workflow's Read Contract.

Economics is installed/updated by default from the manifest with selected adapters and resolves
`.tfw/workflows/economics.md`. Four formal roles remain; analysis retains an active Role Lock.
Daily opt-in is separate. Public tariff cache/used task copies follow the common economics README;
old optional/custom receivers follow `migrations/economics-core.md` before connected writes.
