# TS — TFW-3: Root README Public-Readiness

> **Date**: 2026-02-25
> **Status**: 🟡 TS → executing

## Goal
Rewrite root README.md as a compact project landing page: brief motivation, who it's for, two quick-start paths, what's inside, tool adapters, author, license. Remove sections that duplicate `.tfw/README.md`.

## Steps

1. Rewrite `README.md` (~100-120 lines):
   - Brief motivation (3-5 sentences) + link to `.tfw/README.md`
   - Who This Is For (5 bullets)
   - Quick Start: new project + mid-conversation
   - What's Inside (keep tables)
   - Tool Adapters (keep table)
   - One-line refs for lifecycle, conduct, evolution → `.tfw/`
   - Author + Links
   - Task Board (keep at bottom)
   - **Remove**: Values table, full Conduct, Lifecycle diagram, "Why This Helps"
2. Create `LICENSE` (MIT)
3. Update `STEPS.md`
4. Commit

## DoD
- [ ] README compact, no duplication with .tfw/README.md
- [ ] Public-repo metadata present (author, license, who-for)
- [ ] Task Board preserved
