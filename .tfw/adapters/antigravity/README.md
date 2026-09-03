# Antigravity Adapter

Antigravity discovers workspace rules at `.agents/rules/` and workflows at
`.agents/workflows/` (plural). The singular `.agent/*` path is obsolete. The exact 11
commands, canonical sources, and roles are declared once in `../manifest.yaml`.

## Install or Repair

1. Copy `tfw-rules.md.template` to `.agents/rules/tfw.md`.
2. Copy every manifest workflow to `.agents/workflows/tfw-{command}.md`; this includes
   `/tfw-config`, `/tfw-knowledge`, and `/tfw-research` from
   `.tfw/workflows/research/base.md`.
3. Preserve unrelated rules and workflows. Repeating the install must be a no-op.
4. Verify the vendor root and the literal 11-command/role set against the manifest; do not
   accept “whatever files already exist” as parity.

The persistent rule is a compact router. It does not preload full conventions, glossary, or
KNOWLEDGE and never treats the tooling manifest as runtime authority.
