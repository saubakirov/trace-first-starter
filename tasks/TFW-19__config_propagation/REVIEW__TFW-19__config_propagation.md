# REVIEW — TFW-19: Config Propagation

> **Дата**: 2026-04-03
> **Автор**: Reviewer (AI)
> **Статус**: 🔍 REV
> **Parent HL**: [HL-TFW-19](HL-TFW-19__config_propagation.md)
> **TS**: [TS-TFW-19](TS__TFW-19__config_propagation.md)
> **RF**: [RF-TFW-19](RF__TFW-19__config_propagation.md)

---

## 1. Review Checklist

| # | Check | Result | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | All 15 acceptance criteria verified against actual files |
| 2 | Code quality | ✅ | Standard 2-line header consistent across all 4 files; table format matches reference (research.md) |
| 3 | Test coverage | ✅ | Meta-project — grep verification in RF §4 correct; independent verification below |
| 4 | Philosophy aligned | ✅ | Pattern A (inline + config key) restores RESEARCH-12 recommendation. P1 (enforcement inline), P3 (no scripts) upheld |
| 5 | Tech debt | ✅ | TD-48 resolved. 3 new observations triaged below |
| 6 | Security | N/A | No secrets, no code |
| 7 | Observability | N/A | No code |
| 8 | Breaking changes | ⚠️ | See §2 |
| 9 | Style & standards | ✅ | Conventions followed, adapters byte-synced (diff = 0) |

## 2. Notable Items

### Config sync registry completeness

RF claims 16 entries: 8 scope_budgets + 4 research + 4 knowledge = 16. Verified — all present in config.md §Config Sync Registry.

Observation: RF #2 correctly flags that `PROJECT_CONFIG.yaml` `tfw.workflows` section doesn't include `config.md`. This is a legitimate consistency gap — the YAML lists 10 workflows but config.md is the 11th.

### Breaking change (⚠️ minor)

conventions.md §8 now lists 11 workflows (was 10). Downstream projects copying conventions from upstream will see the new entry. Not a breaking change per se, but notable for `tfw-update` — the diff will show the new row.

### TS.md template format

L27 now reads: `**Бюджет:** {N} новых файлов, {M} модификаций. Defaults: max {max_files} files, max {max_new} new, max {max_loc} LOC.`

The `{max_files}` etc. are **template placeholders for the coordinator** to fill from config when writing TS. This is correct — the coordinator reads config and substitutes. Not a runtime placeholder.

## 3. Independent Verification

| Check | Command / Inspection | Result |
|-------|---------------------|--------|
| plan.md budget table | `view_file L116-127` | ✅ 4 rows, values match config (14, 8, 1200, 12) |
| plan.md enforcement hook | `view_file L92-94` | ✅ Budget Check block present before small/large task split |
| plan.md Naming Rules | `grep -c "Naming Rules"` → 0 | ✅ TD-48 resolved |
| conventions.md §6 | `view_file L150-160` | ✅ 4 rows + Rationale column |
| conventions.md §8 | `grep config.md` → L189 | ✅ config.md listed |
| conventions.md §15 | `grep config.md` → L283 | ✅ Role Lock entry |
| knowledge.md §Limits | `view_file L107-118` | ✅ 4 rows, values match config |
| TS.md template L27 | `view_file L27` | ✅ Inline defaults format |
| research.md L142-143 | `view_file L142-143` | ✅ 2-line defaults header |
| config.md workflow | `view_file` full | ✅ Edit + Verify modes, Registry (3 categories, 16 entries) |
| glossary.md | `grep "Config Sync Registry"` → L152 | ✅ Term present |
| Adapter sync: config | `diff config.md tfw-config.md` → 0 | ✅ Byte-copy |
| Adapter sync: plan | `diff plan.md tfw-plan.md` → 0 | ✅ Byte-copy |
| Adapter sync: research | `diff research.md tfw-research.md` → 0 | ✅ Byte-copy |
| Adapter sync: knowledge | `diff knowledge.md tfw-knowledge.md` → 0 | ✅ Byte-copy |

## 4. Tech Debt Collected

| # | Source | Severity | File | Description | Action |
|---|--------|----------|------|-------------|--------|
| 1 | RF obs. #1 | Low | `.tfw/conventions.md` | §2 Required Artifacts doesn't list config.md — only original 10 listed, but §8 now has 11 | ⬜ Backlog |
| 2 | RF obs. #2 | Low | `.tfw/PROJECT_CONFIG.yaml` | `tfw.workflows` section missing `config: .tfw/workflows/config.md` | ⬜ Backlog |
| 3 | RF obs. #3 | Low | `.tfw/conventions.md` | §10.1/10.2 numbering — pre-existing TD-45, still present | N/A (existing TD-45) |

## 5. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | convention | Pattern A (inline defaults + config key) is the standard for enforcement-critical values. Standard header: `> Configured in... > Values below are defaults...`. Pattern B (pure reference) proven to kill agent compliance | HL-TFW-19, RES-TFW-19, RF-TFW-19 | High |
| 2 | process | Config Sync Registry pattern: config.md workflow maps YAML keys to file locations (section + row label). AI agent reads registry, finds sections, compares values. No scripts needed | config.md workflow | High |
| 3 | constraint | TS line numbers drift between writing and execution — always use content matching, not line-number targeting | RF obs., ONB §6 | Medium |

## 6. Verdict

### ✅ APPROVE

All 15 acceptance criteria met. Independent verification confirms:
- Budget tables restored with correct values matching PROJECT_CONFIG.yaml
- Enforcement hook in Phase 5
- Config workflow created with clean interactive UX
- All adapters byte-synced
- TD-48 resolved

Task addresses the root cause identified in the HL: Pattern B broke agent enforcement, Pattern A restores it with a systematic sync mechanism.

**tfw-docs: Applied — KNOWLEDGE.md updated: +P11 (enforcement inline), +D24 (Pattern A + Config Sync Registry, supersedes D17), +config.md to Architecture Map, +TFW-19 key artifact, +2 legacy entries (Pattern B superseded, Naming Rules removed). TECH_DEBT.md: +TD-50, +TD-51 (added during REVIEW)**

---

*REVIEW — TFW-19: Config Propagation | 2026-04-03*
