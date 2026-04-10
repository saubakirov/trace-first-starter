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
| F8 | Fact categories (conventions.md §10.1) are the single source of truth. Hardcoding category lists in templates causes drift — coordinator's own TS had different list from §10.1 and didn't notice. Always reference §10.1, never duplicate | ⚠️ 1 source | User, TFW-26 session (caught divergence) | 2026-04-05 |
| F9 | Secondary motto = "The trace is the product." Used as inline brand anchor near philosophy link in README. Tagline (F10 in philosophy.md) is the primary brand statement | ⚠️ 1 source | HL TFW-27/A S8 (user, approved from option B) | 2026-04-08 |
| F10 | Self-contained prompts: when user copies a starter prompt from README into an agent, the prompt must include everything (repo URL, what TFW is, what to read) because the agent doesn't see the surrounding README context. Prompt ≠ documentation — it's an isolated instruction | ⚠️ 1 source | REVIEW TFW-31 FC4 (user UX insight) | 2026-04-09 |
| F11 | TFW has two orthogonal types of research "passes": Pass (OODA loops within one iteration, controlled by `loops_per_stage`/`max_passes`) and Iteration (full research rounds, controlled by `min_iterations`). Pass = depth within one investigation, Iteration = breadth across investigations | ⚠️ 1 source | REVIEW TFW-32/C FC#2 | 2026-04-10 |
