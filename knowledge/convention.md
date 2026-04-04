# Knowledge: Convention

> Topic file for `convention` facts. Updated by `/tfw-knowledge`.
> See KNOWLEDGE.md §5 for the index.

| # | Fact | Verified | Source(s) | Added |
|---|------|----------|-----------|-------|
| F1 | Adapter files in `.agent/workflows/` are exact byte-copies of `.tfw/workflows/` — `cp` is the correct sync method, not manual editing | ⚠️ 1 source | RF TFW-18 §6 | 2026-04-03 |
| F2 | Some `.tfw/` files use CRLF while others use LF — no line ending consistency rule exists | ⚠️ 1 source | RF TFW-18 §6 | 2026-04-03 |
| F3 | TS descriptions of existing file structure can drift from reality — executors should always verify actual file content, not trust TS descriptions | ⚠️ 1 source | REVIEW TFW-18 §5 | 2026-04-03 |
| F4 | Checkpoint behavioral fields (Agent assessment, Depth check, Recommendation) must live in templates, not inline in workflows — template-owns-format pattern, single source of truth | ⚠️ 1 source | TFW-21 RES R1 | 2026-04-03 |
| F5 | Ref-pattern breaks NOT because of ref itself, but because there's no algorithmic step wrapping it. «Мы просто не сделали из этого алгоритм или шаг. Там было на уровне рекомендации». Solution: ref-inside-step (step is self-contained, ref adds precision) | ✅ verified | RES TFW-22 FC#4, REVIEW TFW-22 FC#4 | 2026-04-04 |
| F6 | Config Sync Registry purpose = "what YAML keys are consumed where" — any key read in a workflow step should be registered, even without inline display. Expanded beyond original "inline display locations" scope | ✅ verified | RF TFW-22 FC#1, REVIEW TFW-22 FC#5 | 2026-04-04 |
| F7 | `.tfw/workflows/*.md` is always source of truth for adapters. Adapter drift in `.claude/commands/` and `.agent/workflows/` is a known issue, resolved by copy-on-modify at end of each phase | ⚠️ 1 source | RF TFW-22 FC#2 | 2026-04-04 |
| F8 | §3.1 Result Visualization must be domain-agnostic — TFW is not code-only. HL-level thinking = values, processes, outcomes. User: «на уровне HL мыслить надо иначе, через ценности, процессы». Applies to education, business, research, presentations — not just software | ✅ verified | RF-A TFW-23 FC#4, REVIEW TFW-23 FC#3 | 2026-04-04 |
| F9 | Research uses filesystem-level state machine: `research/` subfolder with stage files. File existence = stage completion. No parsing, no format compliance needed. Deterministic, crash-resilient, zero-parsing | ✅ verified | RF-A TFW-24 FC#2, REVIEW TFW-24 FC#2 | 2026-04-04 |
| F10 | RES = synthesis document with intentionally different structure from stage files. Stage sections removed from RES template — those live in `research/` subfolder. Term: "Synthesis" for consolidation step (base.md Step 6). Different structure forces integrated thinking, prevents copy-paste | ✅ verified | RF-A TFW-24 FC#3, REVIEW TFW-24 FC#3 | 2026-04-04 |
| F11 | HL §1 uses Amazon Working Backwards elements: Vision narrative ("write as if done"), Impact field, stakeholder-perspective Quote (press release pattern). §10 has "Why Not Just...?" section (internal FAQ pattern) — forces alternatives consideration before research | ⚠️ 1 source | REVIEW TFW-24 FC#4 | 2026-04-04 |
| F12 | Stage templates live in `templates/research/` (briefing, gather, extract, challenge). Each has: Parent HL link, Goal from §1 Vision, D28 guiding question as subtitle, Findings section, Checkpoint with `Stage complete: YES/NO`, Sufficiency checklist. Starting points, not contracts | ✅ verified | RF-B TFW-24 FC#1, REVIEW-B TFW-24 FC#1 | 2026-04-04 |
