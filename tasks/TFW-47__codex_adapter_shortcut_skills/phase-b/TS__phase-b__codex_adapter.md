# TS — TFW-47 / Phase B: Codex Adapter + Framework Integration

> **Date**: 2026-07-17
> **Author**: Coordinator (Antigravity)
> **Status**: ✅ APPROVED — stakeholder-amended 2026-07-21
> **Parent HL**: [HL-TFW-47](../HL-TFW-47__codex_adapter_shortcut_skills.md)
> **Phase HL**: [HL Phase B](HL__phase-b__codex_adapter.md)
> **Research**: [iter2/RES.md](../research/iter2/RES.md) (Codex adapter mechanics)

---

## 1. Objective

Create a first-class Codex adapter that gives people the same user-facing `/tfw-*` workflow commands they use in Claude Code and Antigravity. Codex must recognize TFW immediately from the repository, route every command to the canonical local workflow, and safely attach or repair the adapter when a TFW project was initialized by another agent. Repository-local skills are the supported Codex implementation mechanism, not a wrapper users must learn.

### Stakeholder amendment (2026-07-21)

The original research classified `$tfw-*` as primary and `/tfw-*` as a secondary soft alias. Live Codex Desktop behavior in this task contradicted that conclusion: `/tfw-handoff TFW-47 phase b` was accepted and routed to the TFW handoff workflow, and the active Codex skill catalog discovered repository-local skills whose descriptions name `/tfw-*` triggers. Current official Codex documentation also maps imported slash commands to skills and identifies skills as the supported repository-shared workflow format.

Therefore:

- `/tfw-*` is the primary human-facing contract across TFW adapters.
- `.agents/skills/tfw-*` remains the Codex-native implementation and discovery layer.
- `$tfw-*` and `/skills` are troubleshooting/explicit-selection fallbacks, not the normal TFW UX.
- Root `AGENTS.md` provides always-on project recognition and fallback routing.
- `tfw-init` must support both first initialization and idempotent Codex attach/repair for an existing TFW project.

## 2. Scope

### In Scope
- Codex adapter source files in `.tfw/adapters/codex/`
- 11 handwritten skills (plan, research, handoff, review, resume, docs, knowledge, release, update, config, init)
- Installed copies at `.agents/skills/tfw-*/SKILL.md`
- Root `AGENTS.md` plus the marker-bounded Codex routing template
- Framework docs: README, quickstart, adapters README, init.md, update.md, glossary.md
- Removal of obsolete imported `.agents/skills/source-command-tfw-*` copies that duplicate canonical workflows
- Evidence: Codex runs `/tfw-resume` or `/tfw-plan` in CL mode after adapter installed

### Out of Scope
- `tfw-task` meta-workflow skill (non-canonical and duplicates plan/handoff logic)
- Evidence template changes (done in Phase A)
- Release packaging (Phase C)
- Antigravity/Claude Code/Cursor adapter changes

## 3. Principles Check

| # | Principle (from HL §7) | Enforced by | Gate |
|---|----------------------|-------------|------|
| P3 | Thin adapters over duplicated workflows | AC-2 | Each skill reads `.tfw/workflows/*.md`, no workflow logic in skill |
| P4 | Visible affordance over hidden inference | AC-2, AC-7 | `/tfw-*` prompts route to separately discoverable repository workflows |
| P5 | Truthful invocation contract | AC-1, AC-7 | Docs lead with the slash syntax verified in the active Codex environment and describe skills as the implementation layer |
| P6 | Portable installation | AC-3 | `.agents/skills/` works cross-platform |
| P7 | Fallback-first | AC-1 | README documents generic AGENTS.md routing as fallback |
| P8 | Adapter parity | AC-4, AC-5 | Codex row in adapter table, init/update workflows |

## 4. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `.tfw/adapters/codex/README.md` | CREATE | Install instructions, fallback, troubleshooting |
| `.tfw/adapters/codex/AGENTS.md.template` | CREATE | Root routing section for Codex users |
| `.tfw/adapters/codex/skills/tfw-plan/SKILL.md` | CREATE | Thin router → `.tfw/workflows/plan.md` |
| `.tfw/adapters/codex/skills/tfw-research/SKILL.md` | CREATE | Thin router → `.tfw/workflows/research/base.md` |
| `.tfw/adapters/codex/skills/tfw-handoff/SKILL.md` | CREATE | Thin router → `.tfw/workflows/handoff.md` |
| `.tfw/adapters/codex/skills/tfw-review/SKILL.md` | CREATE | Thin router → `.tfw/workflows/review.md` |
| `.tfw/adapters/codex/skills/tfw-resume/SKILL.md` | CREATE | Thin router → `.tfw/workflows/resume.md` |
| `.tfw/adapters/codex/skills/tfw-docs/SKILL.md` | CREATE | Thin router → `.tfw/workflows/docs.md` |
| `.tfw/adapters/codex/skills/tfw-knowledge/SKILL.md` | CREATE | Thin router → `.tfw/workflows/knowledge.md` |
| `.tfw/adapters/codex/skills/tfw-release/SKILL.md` | CREATE | Thin router → `.tfw/workflows/release.md` |
| `.tfw/adapters/codex/skills/tfw-update/SKILL.md` | CREATE | Thin router → `.tfw/workflows/update.md` |
| `.tfw/adapters/codex/skills/tfw-config/SKILL.md` | CREATE | Thin router → `.tfw/workflows/config.md` |
| `.tfw/adapters/codex/skills/tfw-init/SKILL.md` | CREATE | Thin router → `.tfw/workflows/init.md` |
| `.agents/skills/tfw-plan/SKILL.md` ... (×11) | CREATE | Installed copies from adapters/codex/skills/ |
| `.agents/skills/source-command-tfw-*` (×11) | DELETE | Remove stale imported full-workflow duplicates |
| `AGENTS.md` | MODIFY | Add always-on `/tfw-*` routing and fallback contract |
| `README.md` | MODIFY | Adapter table + Quick Start Codex section |
| `.tfw/quickstart.md` | MODIFY | Tell agents to install/repair the Codex command surface during init |
| `.tfw/adapters/README.md` | MODIFY | Add Codex adapter description |
| `.tfw/conventions.md` | MODIFY | Define cross-tool `/tfw-*` contract and Codex two-layer adapter |
| `.tfw/workflows/init.md` | MODIFY | Add Codex skill install option |
| `.tfw/workflows/update.md` | MODIFY | Add Codex adapter sync step |
| `.tfw/glossary.md` | MODIFY | Adapter Command includes Codex example |

**Revised budget:** 48 touched files including RF/evidence: 22 source/installed
command files, 11 deleted legacy imports, 12 adapter/framework/trace files, and 3
result/evidence artifacts.
**Override justification:** the stakeholder explicitly authorized Codex adapter cleanup.
The high file count is mechanical: 11 exact source/installed command pairs plus 11
obsolete full-workflow copies. The conceptual change remains one adapter boundary;
splitting it would make source/install parity and cleanup harder to verify.

## 5. Acceptance Criteria

### AC-1: Codex adapter source files exist

`.tfw/adapters/codex/` contains README and AGENTS.md template with install instructions.

- [ ] `.tfw/adapters/codex/README.md` exists with install steps, fallback instructions, troubleshooting
- [ ] `.tfw/adapters/codex/AGENTS.md.template` exists with TFW routing section for Codex users
- [ ] README presents `/tfw-*` as the primary user commands and explains that repo skills implement them in Codex
- [ ] README documents `.agents/skills/` as install target
- [ ] README contains an idempotent new-project/existing-project install-or-repair procedure
- [ ] README defines marker-bounded `AGENTS.md` merging and preserves all instructions outside that block

Gate: Files exist, content covers install + fallback + invocation syntax
Evidence: N/A — documentation files

### AC-2: 11 handwritten skills in adapter source

Each TFW workflow has a corresponding Codex skill with YAML frontmatter and contract heading.

- [ ] 11 skill folders exist at `.tfw/adapters/codex/skills/tfw-{workflow}/SKILL.md`
- [ ] Workflows covered: plan, research, handoff, review, resume, docs, knowledge, release, update, config, init
- [ ] Each SKILL.md has YAML frontmatter with `name` and `description` fields
- [ ] Each description begins from the corresponding `/tfw-*` command and includes natural-language trigger context
- [ ] Each SKILL.md has Contract section with: context loading, workflow file reference, role lock, hard stop
- [ ] No skill duplicates workflow body — all read from `.tfw/workflows/*.md`
- [ ] Skills with workflow-specific contracts (research: iterations.yaml; handoff: scope guard; review: verify-claims; config: sync registry; update: preserve-customizations; init: missing-.tfw handling) include those clauses

Gate: `ls .tfw/adapters/codex/skills/` returns 11 directories. Each SKILL.md contains `name:`, `description:`, contract bullets, workflow file path.
Evidence: Codex loads skills from installed location — see AC-7

### AC-3: Skills installed to `.agents/skills/`

Installed copies match source files.

- [ ] 11 skill folders exist at `.agents/skills/tfw-{workflow}/SKILL.md`
- [ ] Content matches `.tfw/adapters/codex/skills/` source files
- [ ] `.agents/skills/` not in `.gitignore` (skills committed to repo)
- [ ] Obsolete `source-command-tfw-*` full-workflow imports are absent

Gate: `diff` between source and installed copies shows no differences
Evidence: Codex discovers installed skills — see AC-7

### AC-4: README adapter table updated

Codex appears as a first-class adapter alongside Claude Code, Cursor, Antigravity.

- [ ] Tool Adapters table has Codex row: `.tfw/adapters/codex/` | `.agents/skills/tfw-*/SKILL.md`
- [ ] Quick Start tells Codex users to invoke the same `/tfw-*` commands as other adapters

Gate: `grep "Codex" README.md` returns adapter table row
Evidence: N/A — documentation

### AC-5: Framework workflows updated

init.md and update.md include Codex adapter steps.

- [ ] `init.md` has Codex install option: copy skills from `.tfw/adapters/codex/skills/` to `.agents/skills/`
- [ ] `init.md` detects an existing initialized TFW project and runs adapter attach/repair without resetting config, knowledge, tasks, or project docs
- [ ] `update.md` has Codex sync step: re-copy skills on framework upgrade
- [ ] `init.md` and `update.md` merge only the marker-bounded TFW block in root `AGENTS.md` and preserve project-specific instructions
- [ ] `.tfw/adapters/README.md` includes Codex adapter description

Gate: `grep -c "codex\|Codex" .tfw/workflows/init.md .tfw/workflows/update.md .tfw/adapters/README.md` > 0 for each
Evidence: N/A — workflow specs

### AC-6: Glossary updated

Adapter Command definition includes Codex skills.

- [ ] glossary.md Adapter Command entry mentions `.agents/skills/tfw-*/SKILL.md` as Codex example
- [ ] If "Codex" term added — includes discovery path and invocation syntax

Gate: `grep "Codex" .tfw/glossary.md` returns ≥1 hit
Evidence: N/A — glossary entry

### AC-7: Evidence — Codex runs TFW workflow

The adapter works: Codex discovers and executes a TFW workflow using the installed skills.

- [ ] Codex runs in the project directory
- [ ] Codex discovers repository-local `tfw-*` skills in the active skill catalog or selector
- [ ] A literal `/tfw-*` prompt executes the matching TFW workflow without requiring a `$` wrapper
- [ ] Output captured in `evidence/EV__phase-b__codex_adapter.md`

Gate: EV file exists with at least 1 VERIFIED evidence row showing Codex execution
Evidence: Codex runs `/tfw-resume` or equivalent. Capture: skill discovery confirmation + workflow execution output + any issues encountered.

### Evidence Artifacts

| File | Required | Description |
|------|----------|-------------|
| `evidence/EV__phase-b__codex_adapter.md` | ✅ | Structured EV: Environment (Codex version, OS, project path), per-AC table, Verdict |
| `evidence/codex_skill_list.txt` | Optional | `$` menu output showing tfw-* skills discovered |
| `evidence/codex_workflow_output.md` | Optional | Full output of Codex running a TFW workflow |

## 6. Technical Guidance

- **Skill structure convention** (iter2 D6): YAML frontmatter (`name`, `description`) + a concise router body. Each skill is individually authored and opens its canonical local workflow on demand.
- **Workflow-specific contracts** (iter2 D2): 6/11 skills need unique contract clauses:
  - `tfw-research`: reference `iterations.yaml`, resume from last incomplete iteration
  - `tfw-handoff`: scope guard (budget check before execution)
  - `tfw-review`: verify claims against actual files, trust-but-verify
  - `tfw-config`: sync registry for config propagation
  - `tfw-update`: preserve project customizations during framework upgrade
  - `tfw-init`: handle missing `.tfw/` gracefully
- **On-demand loading** (iter2 D3): Skills instruct agent to `read conventions.md` and `read glossary.md` at runtime, not embed them.
- **Install = copy**: `tfw-init` copies `.tfw/adapters/codex/skills/tfw-*/ → .agents/skills/tfw-*/`. `tfw-update` re-copies.
- **AGENTS.md template**: A marker-bounded fragment (`TFW:CODEX:START` / `TFW:CODEX:END`) that can be inserted or replaced idempotently without overwriting project instructions. This is the always-on recognition and fallback routing layer.
- **Existing project attach/repair**: If `.tfw/`, a configured Task Board, and project traces already exist, do not re-run full initialization. Install or refresh the Codex adapter only, verify it, report the changes, and stop.

## 7. Definition of Failure

- ❌ Any skill duplicates workflow body instead of reading `.tfw/workflows/*.md`
- ❌ Skills use `.codex/skills/` (legacy) instead of `.agents/skills/` (2026 standard)
- ❌ Documentation makes users learn `$tfw-*`, `/skills`, or another wrapper for normal TFW work
- ❌ Existing-project attach resets or overwrites project config, knowledge, tasks, Task Board, or non-TFW `AGENTS.md` content
- ❌ `tfw-update` overwrites or drops Codex adapter files during upgrade
- ❌ Evidence file missing or shows Codex cannot discover installed skills
- ❌ Fewer than 11 skills (all canonical workflows must be covered)

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| A Codex surface may render repo skills differently | Keep `/tfw-*` literal routing in `AGENTS.md`; document `$tfw-*` and `/skills` only as fallbacks, and prefer verified current-session behavior over broad UI claims. |
| 11 handwritten skills may drift from workflow list | Validate count: `ls .tfw/adapters/codex/skills/ | wc -l` = 11 |
| Quick Start Codex prompt may confuse users already using AGENTS.md | Separate section in Quick Start, clearly labeled "Codex users" |

## 9. Cross-Phase Modifications (multi-phase)

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `README.md` | Phase A (task board only) | Phase B modifies adapter table and Quick Start. No conflict with task board changes. |
| `.tfw/glossary.md` | Phase A (no glossary changes) | Phase B adds Codex to Adapter Command. No conflict. |
| `KNOWLEDGE.md` | Phase A (D53 added) | Phase B may add new decision. No conflict with D53. |

## 10. Research Correction Trace

The implementation keeps iter2 research files unchanged as historical traces. The following iter2 statements are superseded for Phase B:

| Prior statement | Corrected decision | Basis |
|-----------------|--------------------|-------|
| `$tfw-*` is primary; `/tfw-*` is only a soft alias | `/tfw-*` is the primary TFW user contract; skills are the internal Codex format | Live invocation in this task; active repo-skill discovery; official Codex import map: Slash commands → Skills |
| Skill changes require a new session | Codex detects skill changes automatically; restart is fallback if discovery does not refresh | Current official Build Skills documentation |
| AGENTS-only and skills are competing options | They are complementary: AGENTS = durable recognition/routing, skills = reusable/discoverable workflow implementation | Current official customization guidance and observed runtime behavior |

---

*TS — TFW-47 / Phase B: Codex Adapter + Framework Integration | 2026-07-17*
