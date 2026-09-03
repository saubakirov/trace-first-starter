# TFW Adapters

`.tfw/adapters/manifest.yaml` is the single tooling-only copy/check map. It declares the
four vendor roots, the exact 11 public commands, their canonical workflows and roles, and
the source/target strategy. Runtime roles never read the manifest; installed vendor files
route to canonical workflows, which remain authoritative.

| Tool | Persistent discovery root | Command discovery root |
|---|---|---|
| Codex | `AGENTS.md` | `.agents/skills/tfw-*/SKILL.md` |
| Claude Code | `CLAUDE.md` | `.claude/commands/tfw-*.md` |
| Cursor | `.cursor/rules/tfw.mdc` | `.cursor/commands/tfw-*.md` |
| Antigravity | `.agents/rules/tfw.md` | `.agents/workflows/tfw-*.md` |

`init.md` installs the manifest's exact target set, `update.md` repairs those same copies,
and `config.md` verifies affected generated copies. Missing sources, targets, roles, extra or
missing commands, duplicate managed blocks, and receiver-path mismatches are hard failures.

## Adapter Requirements

1. The persistent root recognizes `/tfw-*` but does not preload common files or duplicate a
   workflow algorithm.
2. Command files are deterministic copies at the vendor-documented discovery path.
3. Marker-bounded project roots update only the managed block; an unmarked existing file is
   reported and left untouched.
4. Installation is idempotent and preserves unrelated receiver content.
5. The clean-receiver test must resolve exactly the manifest's 11 commands and roles.

Templates carry no `{version}` substitution. They read `.tfw/VERSION` only when a selected
workflow actually requires version information.
