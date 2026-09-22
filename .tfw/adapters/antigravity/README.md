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

## Coordination Messaging

Under `tfw-gates-only`, TFW role units report gate transitions to their Coordinator via
`send_message`. The target UUID is extracted from the phase or task `status.md` field
`coordinator_route` by stripping the `antigravity:thread:local:` prefix.

| Role | Reports |
|---|---|
| Researcher | Completion of each research iteration; RES artifact delivery |
| Executor | ONB start; blockers requiring `gate_answer`; RF completion |
| Reviewer | REV start; REVIEW verdict (APPROVE / REVISE / REJECT) |

Cross-session addressed messaging between active Antigravity threads is fully supported by the
platform. Role units must send formal notifications directly upon completing gate work instead of
delegating status delivery to the human owner.
