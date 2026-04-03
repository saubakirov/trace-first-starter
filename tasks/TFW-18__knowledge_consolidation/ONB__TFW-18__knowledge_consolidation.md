# ONB — TFW-18: Knowledge Consolidation

> **Дата**: 2026-04-03
> **Автор**: Executor (AI)
> **Статус**: 🟠 ONB — Ожидает ответов
> **Parent HL**: [HL-TFW-18](HL-TFW-18__knowledge_consolidation.md)
> **TS**: [TS TFW-18](TS__TFW-18__knowledge_consolidation.md)

---

## 1. Understanding (как понял задачу)

Implement the complete knowledge consolidation system across 3 phases: (A) add Fact Candidates sections to RF, REVIEW, RES templates + mindset reminders in 3 workflows + §5 in KNOWLEDGE.md template + .user_preferences.md in init.md, (B) create `/tfw-knowledge` workflow + topic file template + knowledge_state.yaml + PROJECT_CONFIG additions + docs.md item 6 + conventions/glossary updates, (C) add Phase 0 Knowledge Gate Check to plan.md. Then sync all 6 adapter files (5 modified + 1 new).

## 2. Entry Points (откуда начинать)

| File | Role |
|------|------|
| `.tfw/templates/RF.md` | Phase A: add §6 |
| `.tfw/templates/REVIEW.md` | Phase A: add §5 |
| `.tfw/templates/RES.md` | Phase A: add Closure FC |
| `.tfw/workflows/handoff.md` | Phase A: mindset reminder |
| `.tfw/workflows/research.md` | Phase A: mindset reminder |
| `.tfw/workflows/review.md` | Phase A: mindset reminder |
| `.tfw/templates/KNOWLEDGE.md` | Phase A: add §5 index |
| `.tfw/workflows/init.md` | Phase A: .user_preferences.md |
| `.tfw/workflows/knowledge.md` | Phase B: new file |
| `.tfw/templates/TOPIC_FILE.md` | Phase B: new file |
| `.tfw/knowledge_state.yaml` | Phase B: new file |
| `.tfw/PROJECT_CONFIG.yaml` | Phase B: tfw.knowledge section |
| `.tfw/workflows/docs.md` | Phase B: item 6 |
| `.tfw/conventions.md` | Phase B: FC + knowledge refs |
| `.tfw/glossary.md` | Phase B: 4 new terms |
| `.tfw/workflows/plan.md` | Phase C: Phase 0 |
| `.agent/workflows/tfw-*` | Adapters: sync all |

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| — | No blocking questions. HL, TS, and RES are all consistent. All steps are precisely specified with exact content. | — |

## 4. Recommendations (suggestions, not blocking)

1. **TS Step 6 (.user_preferences.md)**: TS says "Create template at project root suggestion in init.md" — I interpret this as: add guidance to init.md about creating `.user_preferences.md` + adding it to `.gitignore`, not creating the actual file in project root (since it's personal/gitignored). The template content goes into init.md's Phase 4 instructions.

2. **Adapter sync approach**: All 5 existing adapter files (`.agent/workflows/tfw-{handoff,research,review,docs,plan}.md`) are byte-identical copies of their canonical counterparts. I'll apply the same changes to both canonical and adapter, keeping them in sync.

3. **conventions.md structure**: TS Step 12 says "§3 artifact types: add Fact Candidates description" and "§8 workflows: add knowledge.md row" + new subsections. I'll add content at appropriate positions without restructuring existing sections.

## 5. Risks Found (edge cases, potential issues not in TS)

1. **RES template line endings**: `.tfw/templates/RES.md` uses LF line endings, while some other files (KNOWLEDGE.md template, docs.md) use CRLF. The Fact Candidates addition to RES will follow the file's existing LF convention.

2. **REVIEW.md renumbering**: Adding §5 "Fact Candidates" after existing §4 "Traces Updated" means the new section is at the end. TS says "After existing §4 Verdict" — but current template has §4 as "Traces Updated", not "Verdict". Verdict is §2. I'll add §5 FC after §4 (Traces Updated), before the footer. This matches the intent of "add to the end before closing."

## 6. Inconsistencies with Code (spec vs reality)

1. **REVIEW.md §4 naming**: TS Step 2 says "After existing §4 Verdict, add same section (renumbered to §5)." Current REVIEW.md has: §1 Checklist, §2 Verdict, §3 Tech Debt, §4 Traces Updated. The Verdict is §2. I'll add §5 FC after §4 Traces Updated — this is the logical end-of-review position, which matches HL intent.

---

*ONB — TFW-18: Knowledge Consolidation | 2026-04-03*
