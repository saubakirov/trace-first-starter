# TFW Codex Adapter

Codex discovers repository-local skills in `.agents/skills/`. TFW keeps the framework-owned source in `.tfw/adapters/codex/skills/` and installs exact copies into the discovery directory.

## Entry Points

| TFW workflow | Codex skill | Canonical workflow |
|--------------|-------------|--------------------|
| `/tfw-plan` | `$tfw-plan` | `.tfw/workflows/plan.md` |
| `/tfw-research` | `$tfw-research` | `.tfw/workflows/research/base.md` |
| `/tfw-handoff` | `$tfw-handoff` | `.tfw/workflows/handoff.md` |
| `/tfw-review` | `$tfw-review` | `.tfw/workflows/review.md` |
| `/tfw-resume` | `$tfw-resume` | `.tfw/workflows/resume.md` |
| `/tfw-docs` | `$tfw-docs` | `.tfw/workflows/docs.md` |
| `/tfw-knowledge` | `$tfw-knowledge` | `.tfw/workflows/knowledge.md` |
| `/tfw-release` | `$tfw-release` | `.tfw/workflows/release.md` |
| `/tfw-update` | `$tfw-update` | `.tfw/workflows/update.md` |
| `/tfw-config` | `$tfw-config` | `.tfw/workflows/config.md` |
| `/tfw-init` | `$tfw-init` | `.tfw/workflows/init.md` |

## Install

Run from the project root.

**Linux / macOS:**

```bash
mkdir -p .agents/skills
cp -R .tfw/adapters/codex/skills/tfw-* .agents/skills/
```

**Windows PowerShell:**

```powershell
$tfwSkillSource = ".tfw/adapters/codex/skills"
$tfwSkillTarget = ".agents/skills"
New-Item -ItemType Directory -Force -Path $tfwSkillTarget | Out-Null
Get-ChildItem -LiteralPath $tfwSkillSource -Directory -Filter "tfw-*" |
  Copy-Item -Destination $tfwSkillTarget -Recurse -Force
```

Commit `.agents/skills/tfw-*/SKILL.md` with the repository. If the project has no root `AGENTS.md`, copy `AGENTS.md.template` there; otherwise merge its TFW routing sections without replacing project-specific rules.

Start a new Codex task after installing or changing skills because discovery occurs at session start.

## Invocation Contract

- `$tfw-*` is the primary Codex skill invocation and visible affordance.
- `/tfw-*` is a soft text alias matched by each skill description; it is not a native Codex slash command.
- Natural-language requests can also trigger a skill when they match its description.
- Every skill opens the matching `.tfw/workflows/` file on demand. Workflow bodies are never duplicated in skills, so the AGENTS.md instruction-size limit does not constrain TFW context loading.

## Fallback and Troubleshooting

- If skills are unavailable, invoke the workflow in plain language: “Read `.tfw/workflows/plan.md` and run TFW planning.” The root `AGENTS.md` routing remains sufficient for behavior but provides no skill-menu entry.
- If `$tfw-plan` is absent, verify `.agents/skills/tfw-plan/SKILL.md` exists and start a new Codex task.
- Keep `.agents/skills/tfw-*` identical to `.tfw/adapters/codex/skills/tfw-*`; `tfw-init` installs them and `tfw-update` re-copies only this namespace.
