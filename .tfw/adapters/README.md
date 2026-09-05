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

## Command-entry contract

All four adapters preserve the same boundary from `conventions.md` `Tool Adapter Pattern`:
discover the receiver, reach one canonical workflow, bind its Role Lock before task action,
execute its Read Contract in order, obey its gates/stops, and name the canonical next
`/tfw-*` route. Full-copy command receivers begin with byte-identical canonical workflow
content. Codex skills are thin routers that require a complete canonical read. Neither form
may add adapter-specific task logic or use the manifest as runtime authority.

Evidence is reported at the strongest observed level and never promoted: R0 source presence,
R1 receiver parity, R2 invocation, R3 complete canonical load, R4 later conformance, and R5
controlled comparative effect. A source file, exact installed copy, or successful clean
installation does not by itself prove live invocation or model behavior.

Keep these availability facts distinct for every route:

| Fact | What it says | What it does not say |
|---|---|---|
| declared | the manifest names a source, target, role, and workflow | that a target exists |
| tracked | a receiver file is present in this checkout | that a host discovers it |
| installed | the receiver exists at the active host's discovery root | that the command ran |
| clean-receiver reproduced | installation creates the exact declared target | that an external vendor host is live-tested |
| live-observed | one named host/model trace reached an evidence level | that another host or later action behaves the same |
