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
