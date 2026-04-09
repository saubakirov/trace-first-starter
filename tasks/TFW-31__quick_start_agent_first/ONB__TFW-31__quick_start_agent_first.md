# ONB — TFW-31: Quick Start — Agent-First Rewrite (v3)

**Date:** 2026-04-09
**Executor:** Antigravity (Opus)

## 1. Understanding

TS v3 separates learning from execution: new `.tfw/quickstart.md` (reading list for agents) replaces the Phase 0 Bootstrap injected into init.md in v2. README Quick Start prompts redirect agents to `quickstart.md`. Tutorial Mode in init.md gets mini-examples. gen_docs.py source mapping updated.

## 2. Entry Points

| File | Change |
|------|--------|
| `.tfw/quickstart.md` | [NEW] 4-step reading list for agents |
| `README.md` lines 42–81 | Rewrite Quick Start (prompts reference quickstart.md) |
| `.tfw/workflows/init.md` lines 16–54 | Remove Phase 0 (lines 16–42), add Tutorial Mode mini-examples |
| `docs/scripts/gen_docs.py` line 21, 524 | Change init.md → quickstart.md in source mapping |

## 3. Questions (blocking)

None.

## 4. Recommendations

1. gen_docs.py line 524 has a backtick resolver static_map entry for `.tfw/init.md` → `getting-started.md`. Should also update to `.tfw/quickstart.md`. TS doesn't mention this but it's the same source mapping logic.

## 5. Risks Found

1. `.tfw/init.md` (the old pointer file at `.tfw/init.md`, not `.tfw/workflows/init.md`) is referenced in README line 119 and 137. TS scope says "no other sections of README.md modified" — I'll leave those references as-is per scope.

## 6. Inconsistencies with Code

1. TS Change 3a says "lines 16–42" for Phase 0 removal. Current init.md has Phase 0 at exactly lines 16–42. Matches.
2. TS Change 3b says replace "current Tutorial Mode" — that's at lines 44–54 after Phase 0 removal. Matches.
