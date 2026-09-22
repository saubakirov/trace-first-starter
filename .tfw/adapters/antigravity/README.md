# Antigravity Adapter

Antigravity's current canonical workspace rule root is `.agents/rules/`, and its default skills
surface is `.agents/skills/`.

The exact ten commands, canonical sources, and roles are declared once in `../manifest.yaml`.

## Install or Repair

1. Copy `tfw-rules.md.template` to `.agents/rules/tfw.md`.
2. Copy every manifest command skill to `.agents/skills/tfw-{command}/SKILL.md`.
3. Preserve foreign neighbors and customized/unowned content.
4. Repeating install must be a no-op. Verify the vendor root and literal ten-command/role set against
   the manifest; do not accept whatever files already exist as parity.

The persistent rule is a compact router. It does not preload full conventions, glossary, or KNOWLEDGE
and never treats the tooling manifest as runtime authority.
