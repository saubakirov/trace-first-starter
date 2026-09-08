# Antigravity Adapter

Antigravity's current canonical workspace rule root is `.agents/rules/`, and its default workflow
surface is `.agents/workflows/`. The vendor documents backward support for singular `.agent/rules/`.
Canonical new self-install and legacy compatibility are separate claims: singular rules are not a
license to delete foreign files, and rule support does not prove workflow discovery.

The exact 11 commands, canonical sources, and roles are declared once in `../manifest.yaml`.

## Install or Repair

1. Copy `tfw-rules.md.template` to `.agents/rules/tfw.md`.
2. Copy every manifest workflow to `.agents/workflows/tfw-{command}.md`, including `/tfw-config`,
   `/tfw-knowledge`, and `/tfw-research` from `.tfw/workflows/research/base.md`.
3. Preserve `.agent/rules`, `.agent/workflows`, foreign neighbors, and customized/unowned content.
   Retire a proven framework-owned superseded copy only after the plural replacement verifies.
4. Repeating install must be a no-op. Verify the vendor root and literal 11-command/role set against
   the manifest; do not accept whatever files already exist as parity.

The persistent rule is a compact router. It does not preload full conventions, glossary, or KNOWLEDGE
and never treats the tooling manifest as runtime authority.
