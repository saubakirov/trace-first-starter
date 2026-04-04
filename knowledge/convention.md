# Knowledge: Convention

> Topic file for `convention` facts. Updated by `/tfw-knowledge`.
> See KNOWLEDGE.md §4 for the index.

| # | Fact | Verified | Source(s) | Added |
|---|------|----------|-----------|-------|
| F1 | Adapter files in `.agent/workflows/` are exact byte-copies of `.tfw/workflows/` — `cp` is the correct sync method, not manual editing | ⚠️ 1 source | RF TFW-18 §6 | 2026-04-03 |
| F2 | Some `.tfw/` files use CRLF while others use LF — no line ending consistency rule exists | ⚠️ 1 source | RF TFW-18 §6 | 2026-04-03 |
| F3 | TS descriptions of existing file structure can drift from reality — executors should always verify actual file content, not trust TS descriptions | ⚠️ 1 source | REVIEW TFW-18 §5 | 2026-04-03 |
| F4 | Ref-pattern breaks NOT because of ref itself, but because there's no algorithmic step wrapping it. «Мы просто не сделали из этого алгоритм или шаг. Там было на уровне рекомендации». Solution: ref-inside-step (step is self-contained, ref adds precision) | ✅ verified | RES TFW-22 FC#4, REVIEW TFW-22 FC#4 | 2026-04-04 |
| F5 | `.tfw/workflows/*.md` is always source of truth for adapters. Adapter drift in `.claude/commands/` and `.agent/workflows/` is a known issue, resolved by copy-on-modify at end of each phase | ⚠️ 1 source | RF TFW-22 FC#2 | 2026-04-04 |
| F6 | HL §1 uses Amazon Working Backwards elements: Vision narrative ("write as if done"), Impact field, stakeholder-perspective Quote (press release pattern). §10 has "Why Not Just...?" section (internal FAQ pattern) — forces alternatives consideration before research | ⚠️ 1 source | REVIEW TFW-24 FC#4 | 2026-04-04 |
| F7 | Mature AI frameworks universally use 4-8 items for top-level values/principles. None exceed 10. Narrative format (heading + paragraph) preferred over tables for values sections | ⚠️ 1 source | RES TFW-25 FC2 (Microsoft RA, CrewAI, Cursor, NIST) | 2026-04-04 |
