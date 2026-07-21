# TS — TFW-47 / Phase B: Codex Adapter + Framework Integration

> **Date**: 2026-07-17
> **Author**: Coordinator (Antigravity)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-47](../HL-TFW-47__codex_adapter_shortcut_skills.md)
> **Phase HL**: [HL Phase B](HL__phase-b__codex_adapter.md)
> **Research**: [iter2/RES.md](../research/iter2/RES.md) (Codex adapter mechanics)

---

## 1. Objective

Create a first-class Codex adapter in TFW with 11 dedicated shortcut skills, install them to `.agents/skills/`, update all framework docs and workflows to include Codex. The executor IS Codex itself — the adapter's first user creates it. Evidence = Codex runs a TFW workflow using the installed skills.

## 2. Scope

### In Scope
- Codex adapter source files in `.tfw/adapters/codex/`
- 11 handwritten skills (plan, research, handoff, review, resume, docs, knowledge, release, update, config, init)
- Installed copies at `.agents/skills/tfw-*/SKILL.md`
- Framework docs: README, adapters README, init.md, update.md, glossary.md
- Evidence: Codex runs `/tfw-resume` or `/tfw-plan` in CL mode after adapter installed

### Out of Scope
- `tfw-task` meta-workflow skill (deferred per iter2 Q2)
- Evidence template changes (done in Phase A)
- Release packaging (Phase C)
- Antigravity/Claude Code/Cursor adapter changes

## 3. Principles Check

| # | Principle (from HL §7) | Enforced by | Gate |
|---|----------------------|-------------|------|
| P3 | Thin adapters over duplicated workflows | AC-2 | Each skill reads `.tfw/workflows/*.md`, no workflow logic in skill |
| P4 | Visible affordance over hidden inference | AC-2, AC-7 | Skills appear in Codex `$` menu |
| P5 | Truthful invocation contract | AC-2 | SKILL.md describes `$tfw-*` as primary, `/tfw-*` as soft alias |
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
| `README.md` | MODIFY | Adapter table + Quick Start Codex section |
| `.tfw/adapters/README.md` | MODIFY | Add Codex adapter description |
| `.tfw/workflows/init.md` | MODIFY | Add Codex skill install option |
| `.tfw/workflows/update.md` | MODIFY | Add Codex adapter sync step |
| `.tfw/glossary.md` | MODIFY | Adapter Command includes Codex example |

**Budget:** 24 new files (13 source + 11 installed), 5 modifications = 29 total.
**Override justification:** 22 of 24 new files are skill SKILL.md files (~1.2 KB each, same structural convention). Single conceptual unit. Splitting into sub-phases would triple coordination cost for no quality gain.

## 5. Acceptance Criteria

### AC-1: Codex adapter source files exist

`.tfw/adapters/codex/` contains README and AGENTS.md template with install instructions.

- [ ] `.tfw/adapters/codex/README.md` exists with install steps, fallback instructions, troubleshooting
- [ ] `.tfw/adapters/codex/AGENTS.md.template` exists with TFW routing section for Codex users
- [ ] README documents `$tfw-*` as primary invocation, `/tfw-*` as soft alias
- [ ] README documents `.agents/skills/` as install target

Gate: Files exist, content covers install + fallback + invocation syntax
Evidence: N/A — documentation files

### AC-2: 11 handwritten skills in adapter source

Each TFW workflow has a corresponding Codex skill with YAML frontmatter and contract heading.

- [ ] 11 skill folders exist at `.tfw/adapters/codex/skills/tfw-{workflow}/SKILL.md`
- [ ] Workflows covered: plan, research, handoff, review, resume, docs, knowledge, release, update, config, init
- [ ] Each SKILL.md has YAML frontmatter with `name` and `description` fields
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

Gate: `diff` between source and installed copies shows no differences
Evidence: Codex discovers installed skills — see AC-7

### AC-4: README adapter table updated

Codex appears as a first-class adapter alongside Claude Code, Cursor, Antigravity.

- [ ] Tool Adapters table has Codex row: `.tfw/adapters/codex/` | `.agents/skills/tfw-*/SKILL.md`
- [ ] Quick Start section includes Codex-specific prompt or note

Gate: `grep "Codex" README.md` returns adapter table row
Evidence: N/A — documentation

### AC-5: Framework workflows updated

init.md and update.md include Codex adapter steps.

- [ ] `init.md` has Codex install option: copy skills from `.tfw/adapters/codex/skills/` to `.agents/skills/`
- [ ] `update.md` has Codex sync step: re-copy skills on framework upgrade
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

- [ ] Codex launched in CL mode in the project directory
- [ ] Codex discovers `tfw-*` skills (visible in skill list or invocable)
- [ ] Codex executes at least one TFW workflow (e.g., `/tfw-resume` to understand project state)
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

- **Skill structure convention** (iter2 D6): YAML frontmatter (`name`, `description`) + Contract heading with standard bullets. Each skill is individually authored — no copy-paste template. Reference AFD project `.agents/skills/` for working examples.
- **Workflow-specific contracts** (iter2 D2): 6/11 skills need unique contract clauses:
  - `tfw-research`: reference `iterations.yaml`, resume from last incomplete iteration
  - `tfw-handoff`: scope guard (budget check before execution)
  - `tfw-review`: verify claims against actual files, trust-but-verify
  - `tfw-config`: sync registry for config propagation
  - `tfw-update`: preserve project customizations during framework upgrade
  - `tfw-init`: handle missing `.tfw/` gracefully
- **On-demand loading** (iter2 D3): Skills instruct agent to `read conventions.md` and `read glossary.md` at runtime, not embed them.
- **Install = copy**: `tfw-init` copies `.tfw/adapters/codex/skills/tfw-*/ → .agents/skills/tfw-*/`. `tfw-update` re-copies.
- **AGENTS.md template**: Adds a `## TFW Workflows` section to project AGENTS.md. This is the fallback routing — works even without skills installed.

## 7. Definition of Failure

- ❌ Any skill duplicates workflow body instead of reading `.tfw/workflows/*.md`
- ❌ Skills use `.codex/skills/` (legacy) instead of `.agents/skills/` (2026 standard)
- ❌ Documentation claims `/tfw-plan` is a native Codex command (it's a soft alias)
- ❌ `tfw-update` overwrites or drops Codex adapter files during upgrade
- ❌ Evidence file missing or shows Codex cannot discover installed skills
- ❌ Fewer than 11 skills (all canonical workflows must be covered)

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Codex CL mode may not support skill discovery from `.agents/skills/` | Fallback: AGENTS.md routing + manual skill invocation. Document in adapter README. |
| 11 handwritten skills may drift from workflow list | Validate count: `ls .tfw/adapters/codex/skills/ | wc -l` = 11 |
| Quick Start Codex prompt may confuse users already using AGENTS.md | Separate section in Quick Start, clearly labeled "Codex users" |

## 9. Cross-Phase Modifications (multi-phase)

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `README.md` | Phase A (task board only) | Phase B modifies adapter table and Quick Start. No conflict with task board changes. |
| `.tfw/glossary.md` | Phase A (no glossary changes) | Phase B adds Codex to Adapter Command. No conflict. |
| `KNOWLEDGE.md` | Phase A (D53 added) | Phase B may add new decision. No conflict with D53. |

---

*TS — TFW-47 / Phase B: Codex Adapter + Framework Integration | 2026-07-17*
