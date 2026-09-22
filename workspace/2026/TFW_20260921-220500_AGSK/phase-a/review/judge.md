# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|-------|--------|----------|
| 1 | DoD met? | ✅ | All 6 ACs verified in verify.md. AC-1: `.agent/` absent. AC-2: `.agents/workflows/` absent. AC-3: manifest retargeted. AC-4: template=rule byte-equal. AC-5: README updated. AC-6: 14 tests pass. |
| 2 | **(a) Purpose Check** — is this what we set out to do? **(b) Design soundness** | ✅ | **(a)** Serves `README.md` §How It Works principle "Inspectable project context": removing legacy directories and duplicate delivery paths makes the project structure honest and self-describing. Harm at stake: retaining `.agent/` and `.agents/workflows/` would perpetuate directory confusion, broken workflow references, and duplicate file delivery — directly harming inspectability and clean project organization. **(b)** Design is sound against HL §7 principles: single source of truth preserved (manifest is sole authority for adapter paths), zero tech debt achieved (no masked/renamed vestiges), consumer safety maintained (Phase B explicitly scoped for downstream guidance). |
| 3 | Debt disposed | ⚪ N/A | RF §6 "No observations." No §5 rows to dispose. |
| 4 | Style & standards | ✅ | Naming follows `Artifact file naming` conventions. RF, TS, ONB, EV all use correct `__phase-a__adapter_migration_and_cleanup` slug. Status frontmatter keys are valid. Commit messages follow `TFW_ID (Phase X): Description` convention. |
| 5 | Observations collected | ✅ | RF §6 declares "No observations." — this is accurate for a straightforward deletion+modification phase. No edge cases or surprising behavior encountered during independent verification. |
| 6 | RF completeness (§7-9) | ✅ | §7 Fact Candidates: "No fact candidates." — acceptable for a mechanical migration with no novel discoveries. §8 Strategic Insights: "No strategic insights." — the migration confirmed the known path without revealing new directions. §9 Diagrams: "No diagrams." — a deletion-heavy phase does not benefit from diagrams. All three sections are present and explicitly addressed. |
| 7 | Evidence exists | ✅ | EV file exists at `evidence/EV__phase-a__adapter_migration_and_cleanup.md`, 44 lines, 7 evidence rows covering AC-1 through AC-6 plus accounting. All rows marked VERIFIED. File is well-formed with Environment table, Evidence table, Verdict summary, and footer. |
| 8 | Evidence sufficiency | ✅ | E1–E5 rely on filesystem assertions (`Test-Path` returning false, file content inspection). These are adequate for deletion and modification claims — the filesystem is the primary source of truth for "file exists/not exists." E6 relies on `pytest` output (14 passed, exit 0) — this establishes the test suite is green. E-accounting cites exact SHAs and provides adds/deletes/LOC — independently confirmed via `git show --stat`. The evidence establishes what it claims: deletions occurred, modifications match spec, tests pass, accounting is accurate. Limitation: E1-E5 do not include raw command output — they are summary assertions. However, the Reviewer independently reran all checks and obtained matching results. |
| 9 | Backward compatibility | ✅ | Consumers of this change: (1) Antigravity itself — now routes `/tfw-*` through `.agents/skills/` which already exist and function (verified in current session). (2) Other adapters (Codex, Claude Code, Cursor) — unchanged per TS §2 Out of Scope; `git show 68dd9ce` confirms zero modifications to their files. (3) Downstream projects — Phase B explicitly handles migration guidance; Phase A's changes are internal to the framework repository. (4) Test suite — 14/14 pass, no regressions. |
| 10 | Safety | ✅ | No secrets, credentials, or destructive irreversible operations. Deletions remove framework-owned obsolete files (confirmed by commit history). No user data at risk within this repository. Downstream projects' `.agent/` directories are untouched by this change — the migration guide (Phase B) will address them. |

## Purpose Check — row 2 clause (a)

Reference set: `README.md` § How It Works (Project North Star) + master HL §1 at contract baseline (FROZEN).

- **North Star clause served:** "Inspectable project context — Purpose, decisions, constraints, rejected alternatives, evidence, current state, and debt can be inspected alongside the output" (README.md L139).
- **HL §1 clause served:** «Адаптер среды Google Antigravity в репозитории Steps Framework переведён на современную архитектуру навыков (`skills`), ликвидируя устаревший механизм рабочих процессов (`workflows`)» (HL L21).
- **Concrete harm at stake:** Retaining `.agent/` and `.agents/workflows/` alongside `.agents/skills/` would mean: (a) agents discovering conflicting routing instructions in different directories, (b) ~68 KB of dead workflow files creating false discovery targets, (c) the manifest claiming one path while files exist at another — violating single-source-of-truth and directly harming inspectability.

**Excess/adjacency test:** No. The result delivers exactly what the HL §1 vision describes and what Phase A's HL §4 deliverables list. Nothing outside scope.
**Deferral test:** No. Phase B work (migration guide, doc sync) is correctly deferred per HL §4 phase dependencies.
**Materiality:** The harm is material — broken routing and directory confusion directly impair agent and human workflow.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---------------|----------|----------------|
| 1 | D54 "Codex first-class adapter… installed at `.agents/skills/tfw-*/SKILL.md`" (KNOWLEDGE.md L107) | RF migrates Antigravity to the same target path | No — alignment; Antigravity now shares the Codex skill target |
| 2 | Adapters row: "singular `.agent` is compatibility only" (KNOWLEDGE.md L31) | RF deletes `.agent/` entirely | No contradiction — Phase A completes the retirement that KNOWLEDGE.md already characterized as "compatibility only." KNOWLEDGE.md L31 still references `.agent/workflows/` in its file list — this is deferred to Phase B doc sync (TS §2 Out of Scope). |

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Every `⚪ N/A` carries a stated reason — no row skipped as a bare ✅? (Row 3 N/A: "No observations. No §5 rows to dispose.")
- [x] Row 2(a): answered against the contract baseline and the north star — never the TS or a Phase HL — with a quoted clause **and** a named harm in one field?
- [x] Rows 7 and 8 answered separately, with different reasoning? (Row 7: evidence exists and is well-formed. Row 8: evidence establishes its claims, with stated limitation on raw output.)
- [x] Referenced verify.md findings in DoD assessment?
- [x] Row 3: N/A — no §5 rows exist.
- [x] Checked RF §7-9 for presence AND quality (not just existence)?
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or "None"? (Two items checked, no contradictions, one deferred update noted.)
- [x] Fact Candidates from RF reviewed — any that need challenge? (RF §7: "No fact candidates." — nothing to challenge.)

Stage complete: YES
