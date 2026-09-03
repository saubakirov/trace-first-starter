# TFW Codex Adapter

Codex discovers persistent project guidance in root `AGENTS.md` and repository skills in
`.agents/skills/`. The public interface is the exact 11 `/tfw-*` commands declared by
`../manifest.yaml`; the command's repository skill opens its canonical workflow and that
workflow selects all further reads.

## Install or Repair

1. Require `.tfw/`; otherwise obtain the framework source before `/tfw-init`.
2. For each manifest command, copy
   `.tfw/adapters/codex/skills/tfw-{command}/SKILL.md` to
   `.agents/skills/tfw-{command}/SKILL.md`. Preserve unrelated skills.
3. Synchronize only the `TFW:CODEX` managed block from `AGENTS.md.template` into root
   `AGENTS.md`. If the destination exists without markers, report it and leave it untouched.
4. Remove a legacy `source-command-tfw-*` directory only when its own content proves it is
   an obsolete imported TFW copy.
5. Verify the literal command set, roles, source equality, one managed block, and a safe
   `/tfw-resume` routing smoke test. File existence alone is not success.

The install is idempotent. The root block is already active and must not order a reload of
itself or a universal common-file preload. Skill and workflow changes are synchronized by
the manifest-driven update path in the same commit.
