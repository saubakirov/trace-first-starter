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

## Command-entry reliability

The production baseline is one schema-valid thin skill per manifest command plus one complete
read of its canonical workflow. The skill is a discovery and routing boundary, not a second
algorithm: the workflow binds the Role Lock before task action, owns Read Contract order and
all gates/stops, and names any next `/tfw-*` route. Every source skill and installed copy must
remain byte-identical.

Static checks can prove source presence, source/copy parity, one manifest role, one canonical
route, and clean-receiver reproduction. They cannot prove that Codex invoked the skill, loaded
the workflow, conformed later, or that one entry wording outperforms another. Those claims need
R2–R5 tool/event and artifact-diff evidence on a named host, model, effort, and revision.

`docs/scripts/command_entry_eval.py` is the explicit, non-default evaluation harness for those
higher levels. It creates one disposable Git fixture per run, uses `codex exec --ephemeral`
with ignored user configuration and fixture-limited `workspace-write`, retains raw redacted
JSONL plus the final Git diff, and recomputes rates and the production decision separately.
It is assurance tooling only: no root, skill, or canonical workflow reads its generated
evidence. Missing live observations for Claude Code, Cursor, or Antigravity stay untested; a
Codex clean-receiver result must not be relabelled as their runtime behavior.
