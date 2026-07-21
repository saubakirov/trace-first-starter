# Gather — "What do we know?"
> **Mindset:** Explorer. Cast a wide net. Don't filter prematurely — collect everything that might matter.
> **Test:** "Have I looked at this from at least 3 independent angles?"

## Dimensions Identified

1. **Skill Discovery Mechanism** — where does Codex find skills, what directory structure
2. **Invocation Syntax** — how users trigger skills (`$`, `/`, natural language)
3. **Instruction Budget** — 32 KiB cap, what gets auto-loaded, truncation behavior
4. **Adapter Structure** — template vs handwritten, canonical location in `.tfw/adapters/codex/`
5. **Sync Strategy** — how `tfw-init` installs and `tfw-update` refreshes Codex skills

## Findings

### F1: Skill Discovery Directories

| Level | Directory | Use |
|-------|-----------|-----|
| Project-local | `.agents/skills/<skill-name>/SKILL.md` | Standard 2026 cross-platform convention |
| User-global | `~/.agents/skills/<skill-name>/SKILL.md` | Available across all projects |
| Legacy Codex | `~/.codex/skills/<skill-name>/SKILL.md` | Deprecated — may still work via `CODEX_HOME` |

**Key observation:** `.agents/skills/` (not `.codex/skills/`) is the 2026 cross-platform standard. Antigravity uses the same directory. The AFD project already uses `.agents/skills/tfw-*/SKILL.md` — 11 skill folders, one per TFW workflow.

### F2: SKILL.md Structure

Required YAML frontmatter:
- `name` (required) — human-readable identifier, used for `$name` invocation
- `description` (required) — triggers automatic matching; crucial for discoverability

Body: markdown instructions loaded on-demand (progressive disclosure — only frontmatter scanned at startup, body loaded when triggered).

**Measured sizes from AFD:**
| Skill | SKILL.md size |
|-------|--------------|
| tfw-plan | 1,181 bytes |
| tfw-research | 1,271 bytes |
| tfw-handoff | 1,235 bytes |
| tfw-config | 1,223 bytes |

All skills are ~1.2 KB. Well under any instruction budget.

### F3: Invocation Syntax

| Syntax | Behavior |
|--------|----------|
| `$tfw-plan` | Primary — opens skill menu or triggers directly |
| `/tfw-plan` in message text | Treated as alias — skill `description` matches on this text |
| `tfw-plan` in message text | Also matched — description includes it |
| Natural language ("plan a TFW task") | Automatic matching via `description` field |
| `/skills` | Lists all available skills |
| `$` (dollar sign alone) | Opens interactive skill menu |

**Confirmed:** `$tfw-plan` is the reliable invocation. `/tfw-plan` is not a native slash command but works because the skill description includes it as a trigger phrase. This is a soft alias, not a hard binding.

### F4: 32 KiB Instruction Cap

- `PROJECT_DOC_MAX_BYTES` = 32 KiB hard cap on auto-embedded docs (`AGENTS.md`)
- **Silent truncation** — no warning if exceeded
- Configurable via `config.toml` → `project_doc_max_bytes`
- Applies to: `AGENTS.md` cascade (auto-loaded at session start)
- Does NOT apply to: skill body (loaded on-demand), file reads during execution

**TFW impact:**
| File | Size | Under 32 KiB? |
|------|------|----------------|
| AGENTS.md | ~1.8 KB | ✅ |
| conventions.md | ~27 KB | ✅ but risky |
| glossary.md | varies | ✅ |
| AGENTS.md + conventions.md combined | ~29 KB | ⚠️ Approaches limit |

**Mitigation pattern from AFD skills:** Each skill's Contract section says "Load `AGENTS.md`, `.tfw/conventions.md`, `.tfw/glossary.md`..." — this is an on-demand read instruction, not an auto-embedded chain. The skill body tells the agent to open files at runtime, bypassing the 32 KiB auto-embed limit.

### F5: Existing AFD Adapter Architecture

```
.tfw/adapters/codex/
├── README.md                          # Setup + entry point table
└── tfw-command-skill.md.template      # Generic template (789 bytes)

.agents/skills/
├── tfw-plan/SKILL.md                  # Handwritten — role lock, context order, templates
├── tfw-research/SKILL.md              # Handwritten — research-specific: iterations.yaml, stage templates
├── tfw-handoff/SKILL.md               # Handwritten — executor role, scope guard, ONB/RF templates
├── tfw-config/SKILL.md                # Handwritten — config sync registry, verify/edit modes
├── tfw-docs/SKILL.md
├── tfw-init/SKILL.md
├── tfw-knowledge/SKILL.md
├── tfw-release/SKILL.md
├── tfw-resume/SKILL.md
├── tfw-review/SKILL.md
└── tfw-update/SKILL.md
```

**Observation:** Template exists (generic, 789 bytes) BUT all 11 skills are handwritten with workflow-specific details. The template is insufficient for skills like tfw-research (iterations.yaml handling) or tfw-config (sync registry mention).

### F6: Comparison with Other Adapters

| Aspect | Claude Code | Antigravity | Codex (AFD) |
|--------|-------------|-------------|-------------|
| Entry point | `CLAUDE.md` (auto-loaded) | `.agent/rules/tfw.md` | `AGENTS.md` (auto-loaded) |
| Commands | `.claude/commands/tfw-*.md` | `.agent/workflows/tfw-*.md` | `.agents/skills/tfw-*/SKILL.md` |
| Invocation | `/tfw-plan` (native slash) | `/tfw-plan` (native workflow) | `$tfw-plan` (skill trigger) |
| Template in adapters/ | `CLAUDE.md.template` | `tfw-rules.md.template` | `tfw-command-skill.md.template` |
| Per-workflow template? | No (thin 1-liners) | No (file copies) | No (generic + handwritten) |
| Sync strategy | Copy `.claude/commands/` | Copy `.agent/workflows/` | Copy `.agents/skills/tfw-*/` |

**Key difference:** Claude Code commands are 1-line routers. Antigravity copies entire workflow files. Codex skills are ~20-line handwritten contracts — a middle ground.

### F7: AGENTS.md Cascade Behavior

- Codex walks CWD → repo root → `~/.codex/` (or `~/.agents/`)
- Merged in order: global → root → deeper directories
- Later files override earlier
- Injected as user-role messages
- Cached at session start — changes require new session

### F8: Reload Behavior

- Skills scanned at session start (frontmatter only)
- Changes to SKILL.md require new chat session
- No hot-reload during active session
- `/skills` command shows current available skills

---

## Checkpoint

- [x] External source used (3 web searches: skill mechanics, instruction limits, AGENTS.md cascade)
- [x] Briefing gap closed (all 5 dimensions covered: discovery, invocation, budget, structure, sync)

Stage complete: YES
