# TFW Adapters

`.tfw/adapters/manifest.yaml` is the single tooling-only copy/check map. It declares the
four vendor roots, the exact standard public commands, their canonical workflows and roles, and
the source/target strategy. Runtime roles never read the manifest; installed vendor files
route to canonical workflows, which remain authoritative.

Exactly three provider-specific Coordinator profiles live at
`codex/coordinator.md`, `claude-code/coordinator.md` and `antigravity/coordinator.md`. The selected
persistent adapter names its one exact path. New-task Plan entry reads only that profile after task-control and shared-rule reads, before
substantive framing, for the mandatory owner-facing startup card and initial mode choice. Plan
Step 5 validates/records that choice, and re-reads the profile only for a material surface or
capability change. The task Coordinator uses the card for new work; a phase Coordinator receives
its bounded dispatch and current phase status. Other
role commands do not preload it. Cursor keeps common-only compatibility without a fourth product
profile. Profiles own
mechanics and dated limitations, never authorization, Role Locks or a copied workflow algorithm.
They are `.tfw/` payload files, so init/update distribute them with the framework; no runtime
manifest lookup, registry or generated loader is added.

| Tool | Persistent discovery root | Command discovery root |
|---|---|---|
| Codex | `AGENTS.md` | `.agents/skills/tfw-*/SKILL.md` |
| Claude Code | `CLAUDE.md` | `.claude/commands/tfw-*.md` |
| Cursor | `.cursor/rules/tfw.mdc` | `.cursor/commands/tfw-*.md` |
| Antigravity | `.agents/rules/tfw.md` | `.agents/skills/tfw-*/SKILL.md` |

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
5. The clean-receiver test must resolve exactly the manifest's commands and roles.

Templates carry no `{version}` substitution. They read `.tfw/VERSION` only when a selected
workflow actually requires version information.

### Optional Daily entries

The optional Daily package has one canonical source under `.tfw/extensions/daily-task/` and a
separate explicit [source/receiver map](../extensions/daily-task/installation.md). Selected discovery
targets are `.agents/skills/tfw-daily-task/SKILL.md` and
`.claude/skills/tfw-daily-task/SKILL.md`; both are thin byte-copied entry sources. They are not
manifest commands or Full roles. Full install/update without opt-in creates neither discovery
target. Verify the manifest's exact records and then selected optional entries separately;
an unknown extra route remains an error. Preserve custom local skills/forms rather than inferring
package ownership or opt-in. Source, installed, reproduced and live-observed remain distinct levels.

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

Economics is installed/updated by default from the manifest with selected adapters and resolves
`.tfw/workflows/economics.md`. Four formal roles remain; analysis retains an active Role Lock.
Daily opt-in is separate. Public tariff cache/used task copies follow the common economics README;
old optional/custom receivers follow `migrations/economics-core.md` before connected writes.
