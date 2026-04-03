# RES — TFW-19: Config Propagation

> **Date**: 2026-04-03
> **Author**: Coordinator (AI)
> **Status**: 🔬 RES — Complete
> **Parent HL**: [HL-TFW-19](HL-TFW-19__config_propagation.md)
> **Mode**: Pipeline

---

## Research Context

TFW-12 centralized config values to PROJECT_CONFIG.yaml using Pattern B (pure reference). This broke agent enforcement of scope budgets. TFW-19 proposes restoring inline values (Pattern A) + creating tfw-config workflow for sync. RESEARCH validates the approach.

## Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| R1 | Pattern A = inline defaults + config key column is the standard | research.md Limits table already implements this and works |
| R2 | Rationale column only in conventions.md (canonical description). All other files = compact: Parameter, Default, Config key | Token density: fewer tokens = better agent performance (P10) |
| R3 | tfw-config = interactive dialog (user says what to change, agent updates all files) + verify mode (audit) | User requirement: «спрашивало что хотите изменить и вело дальше» |
| R4 | Config Sync Registry lives inside config.md workflow file | Self-contained, no extra files, agent reads workflow → sees registry |
| R5 | No scripts — AI agent reads YAML, finds sections, updates values | TFW constraint: pure AI prompt framework, universal |
| R6 | Section-based lookup (header + row label) = not fragile for AI | AI agents understand document structure natively, no regex needed |
| R7 | 3 categories inline: scope_budgets, research, knowledge. Others (statuses, templates, workflows) = lookup, not enforcement — skip | Agreed by user |

## Open Questions

All closed.

---

## Stage: Gather ✅

Full config audit: 7 config sections, 3 need inline enforcement.

| Category | Config Keys | Inline State | Action |
|----------|-------------|-------------|--------|
| scope_budgets (4) | max_files, max_new, max_loc, max_modified | ❌ Removed by TFW-12 | Restore |
| research (4) | queries, files, questions, passes | ✅ Pattern A already | Keep |
| knowledge (6) | interval, gate_mode, max_index, etc. | ❌ Names only, no numbers | Add |
| statuses, templates, workflows, project, tfw meta | Various | Identity/lookup | Skip |

External: Industry confirms inline = only enforcement for AI prompts without code validation.

### Checkpoint: Gather
| Found | Remaining |
|-------|-----------|
| research.md = working Pattern A reference | — |
| 3 categories need inline, 4 skip | — |
| External: inline = advisory but only option for prompt frameworks | — |

**Agent assessment:** Gaps identified and closed.
→ User decision: closed

---

## Stage: Extract ✅

Target file mapping:

| File | Section | Format | Action |
|------|---------|--------|--------|
| plan.md L133-137 | §Scope Budget per Phase | Compact (no Rationale) | Restore table |
| conventions.md L132-135 | §6 Scope Budgets | Full (with Rationale) | Restore table |
| TS.md L27 | Budget line | Inline text | Replace with defaults |
| research.md L140-152 | §Limits | ✅ Compact + config key | Keep, restore «defaults» wording |
| knowledge.md (new) | §Limits (add after Anti-patterns) | Compact (no Rationale) | Add table |

### Checkpoint: Extract
| Found | Remaining |
|-------|-----------|
| 5 target files mapped with exact locations | — |
| research.md lost «defaults» wording in TFW-21 | — |
| knowledge.md has 6 config refs without numbers | — |

**Agent assessment:** Full map ready.
→ User decision: closed

---

## Stage: Challenge ✅

| Challenge | Result |
|-----------|--------|
| C1: Section-based lookup fragility | Not a problem for AI — native document understanding |
| C2: Word count tension with TFW-21 | Negligible (+3-7%, ~40-60 words per table) |
| C3: tfw-config UX | Two modes: edit (interactive, primary) + verify (audit) |
| C4: Registry placement | In workflow file — self-contained |
| C5: Downstream project init | Defaults match → in sync from start |

### Checkpoint: Challenge
| Found | Remaining |
|-------|-----------|
| No show-stoppers | — |

**Agent assessment:** Design validated.
→ User decision: closed

---

## Final Checkpoint

| Stage | Status | Key Findings |
|-------|--------|-------------|
| Gather | ✅ | 3/7 categories need inline. research.md = working reference |
| Extract | ✅ | 5 files mapped, exact sections identified |
| Challenge | ✅ | No fragility, negligible word count impact, interactive UX |

**Verdict:** Sufficient for HL finalization.

## Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|-------|------------|
| F1 | process | TFW = чисто AI prompt framework, no scripts. Workflows ARE the automation — AI agent is the execution engine | User message | High |
| F2 | constraint | Pattern B (pure reference «see config») kills agent enforcement for numeric limits. Proven by TFW-12→TFW-19 regression | Root cause analysis | High |
| F3 | convention | Reference Pattern A format: inline defaults + config key column. research.md Limits table = canonical reference | Extract finding | High |

## Conclusion

RESEARCH confirmed the HL design. Key value: discovered research.md already implements the target pattern (Pattern A), proving the approach works in production. External research validated that inline values are the only enforcement mechanism for AI prompt frameworks. The interactive tfw-config model addresses the original TFW-12 design gap. Self-critique: Challenge was confirmatory — the design was well-grounded from TFW-12 lessons learned.

---

*RES — TFW-19: Config Propagation | 2026-04-03*
