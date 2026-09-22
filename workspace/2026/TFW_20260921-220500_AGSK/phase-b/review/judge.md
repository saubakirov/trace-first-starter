# Judge — "Is the quality sufficient?"
> **Mindset:** Judge. You have the evidence from Verify. Now rule on quality. Every ✅ needs proof. Every ❌ needs a specific finding.
> **Test:** "Would I stake my reputation on this passing production review?"
> Verify findings: [verify.md](verify.md)

## Universal Checklist

| # | Check | Status | Evidence |
|---|---|---|---|
| 1 | DoD met? | ✅ | All 7 AC in TS §5 independently verified against actual files (verify.md V1-V10). HL §5 DoD items 6-8 (migration guide, documentation sync, tests) all satisfied. |
| 2 | **(a) Purpose Check** — is this what we set out to do? **(b) Design soundness** | ✅ | **(a)** HL §1 (contract baseline): "Каталог в единственном числе .agent/ полностью выведен из эксплуатации [...] через воспроизводимый протокол обновления." North Star (`README.md` § How It Works): "Inspectable project context — Purpose, decisions, constraints [...] can be inspected alongside the output." The migration guide provides an exhaustive downstream upgrade path and the documentation sync eliminates stale references, directly serving both the contract's "reproducible update protocol" and the North Star's "inspectable context." Concrete harm at stake: without this work, downstream projects would have no migration path and the repository's own documentation would reference defunct `.agent/` paths, violating inspectability. **(b)** Design follows the established migration guide precedent (3.4.0.md, 3.4.1.md structure) and the manifest-as-single-source-of-truth principle from HL §7. Sound. |
| 3 | Debt disposed | ✅ | RF §6 records one observation (KNOWLEDGE.md Workflows row stale `resume` reference). This is not a debt item — it is an out-of-scope observation correctly excluded from the 10-file VALUE denominator. No §5 debt rows require disposition. |
| 4 | Style & standards | ✅ | File naming follows conventions: `TS__phase-b__*.md`, `RF__phase-b__*.md`, `ONB__phase-b__*.md`, `EV__phase-b__*.md`. Migration guide follows English-language TFW Core style. CHANGELOG follows Keep a Changelog format. Coordination Messaging section placed consistently in both rule and README. |
| 5 | Observations collected | ✅ | RF §6 contains one genuine observation (stale `resume` in KNOWLEDGE.md Workflows row). Not a filler item — it was independently identified in ONB §5 as well. Quality filter passes. |
| 6 | RF completeness (§7-9) | ✅ | §7 Fact Candidates: "No fact candidates" — appropriate since this is documentation/migration work producing no novel architectural decisions. §8 Strategic Insights: "No strategic insights" — appropriate. §9 Diagrams: "No diagrams" — appropriate for documentation-only changes. |
| 7 | Evidence completeness — does the evidence exist? | ✅ | EV file contains 8 evidence rows (E1-E7 + E-accounting), all with VERIFIED status. `doc-sweep.txt` attachment exists and covers all 10 VALUE paths. Total: 8/8 present. |
| 8 | Evidence sufficiency — does the evidence establish the claim? | ✅ | E1 (AC-1) establishes migration guide content by section count and structural analysis. E2 (AC-2) establishes stale-path removal via `git grep` exit 1. E3 (AC-3) establishes glossary update at specific line. E4 (AC-4) establishes README updates via `git grep` exit 1 and `doc-sweep.txt`. E5 (AC-5) establishes CHANGELOG entry at specific line range. E6 (AC-6) establishes test passage with exact count and exit code. E7 (AC-7) establishes byte-equality via `git diff --no-index` exit 0. E-accounting establishes full NUL-safe accounting replay with adds/deletes/LOC. Each evidence item tests the correct claim with an appropriate oracle. The Reviewer independently reran commands 1-5 in verify.md and obtained matching results. |
| 9 | Backward compatibility | ✅ | The migration guide (3.5.0.md) is a new file — no existing consumer affected. KNOWLEDGE.md Adapters row: consumed by future `/tfw-plan` and `/tfw-knowledge` workflows — update is semantically correct (10 routes matches reality post-Phase-A). Glossary Tool Adapter: consumed by readers of `.tfw/glossary.md` — update reflects actual file locations. README adapter tables: consumed by project visitors — update reflects actual entry points. CHANGELOG: append-only format, no existing entries modified. `.agents/rules/tfw.md`: consumed by Antigravity sessions — Coordination Messaging is an additive section that does not alter existing routing behavior. Adapter README: consumed by `/tfw-init` and `/tfw-update` — additive documentation. No breaking changes. |
| 10 | Safety | ✅ | No secrets, credentials, or destructive operations. The migration guide explicitly warns against blind deletion of `.agent/` and requires content inspection first (3.5.0.md §3: "Do not delete `.agent/` without inspecting its contents"). All changes are documentation-only modifications to markdown files. |

## Purpose Check — row 2 clause (a)

**Reference set:** Master HL at contract baseline (frozen 2026-09-22) §1 Vision: "Каталог в единственном числе `.agent/` полностью выведен из эксплуатации и утилизирован как в исходном репозитории фреймворка, так и в сторонних проектах-потребителях через воспроизводимый протокол обновления." North Star (`README.md` § How It Works, L139): "Inspectable project context — Purpose, decisions, constraints [...] can be inspected alongside the output."

The Phase B deliverables directly serve both references: the migration guide (`3.5.0.md`) is the "reproducible update protocol" for downstream consumers, and the documentation sync eliminates stale `.agent/` references that would harm inspectability. Concrete harm without this work: downstream projects would face an undocumented breaking change (retired `.agent/` directory with no guidance), and the repository's own documentation would describe paths that no longer exist.

**Excess/adjacency test:** No. Every deliverable is within HL §4 Phase B scope (migration guide, documentation sync, CHANGELOG). The Coordination Messaging addition (AC-7) is explicitly scoped in the TS and serves HL §3 Target State point 4 ("актуализированы").

**Deferral confession test:** No. Neither the TS nor the RF names a different home for this work.

**Materiality test:** N/A — no purpose failure identified.

**Outcome:** Aligned ✅.

## Contradictions with KNOWLEDGE.md

| # | Knowledge item | RF claim | Contradiction? |
|---|---|---|---|
| 1 | Adapters row (L31): "10 routes [...] `.agents/skills/` surface; singular `.agent` is fully retired" | RF §1: KNOWLEDGE.md updated to reflect 10 routes and `.agents/skills/` | No — RF correctly updates the row to match current reality |
| 2 | D54 (L107): "11 handwritten skills in `.tfw/adapters/codex/skills/tfw-*/SKILL.md`" | RF makes no claim about D54 | No — D54 describes the Codex adapter's historical decision, which remains valid (the adapter source still has 11 skill templates; manifest routes 10 commands) |

## Checkpoint

**Self-check:**
- [x] Every checklist item has evidence (not just ✅/❌)?
- [x] Every `⚪ N/A` carries a stated reason — no row skipped as a bare ✅?
- [x] Row 2(a): answered against the contract baseline and the north star — never the TS or a Phase HL — with a quoted clause and a named harm in one field?
- [x] Rows 7 and 8 answered separately, with different reasoning?
- [x] Referenced verify.md findings in DoD assessment?
- [x] Row 3: every §5 row disposed by the coordinator, each disposition naming something that exists today, and each ruling naming a consequence or its absence rather than a priority?
- [x] Checked RF §7-9 for presence AND quality (not just existence)?
- [x] KNOWLEDGE.md cross-referenced — contradictions documented or "None"?
- [x] Fact Candidates from RF reviewed — any that need challenge?

Stage complete: YES
