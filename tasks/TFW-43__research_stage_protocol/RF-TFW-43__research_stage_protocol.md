# RF — TFW-43: Research Stage Protocol

> **Date**: 2026-05-01
> **Author**: Executor (Antigravity)
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-43](HL-TFW-43__research_stage_protocol.md)
> **TS**: [TS-TFW-43](TS-TFW-43__research_stage_protocol.md)

---

## 1. What Was Done

### New Files
| File | Description |
|------|------------|
| `tasks/TFW-43__research_stage_protocol/ONB-TFW-43__research_stage_protocol.md` | Executor onboarding report |
| `tasks/TFW-43__research_stage_protocol/RF-TFW-43__research_stage_protocol.md` | This file |

### Modified Files
| File | Changes |
|------|---------| 
| `.tfw/templates/research/1_briefing.md` | Added h1 guiding question `"What should we investigate?"` + `> **Mindset:** Strategist...` + `> **Test:**` blockquote |
| `.tfw/templates/research/2_gather.md` | Added `> **Mindset:** Explorer...` + `> **Test:**` blockquote between h1 and `> Parent:` |
| `.tfw/templates/research/3_extract.md` | Added `> **Mindset:** Analyst...` + `> **Test:**` blockquote between h1 and `> Parent:` |
| `.tfw/templates/research/4_challenge.md` | Added `> **Mindset:** Critic...` + `> **Test:**` blockquote between h1 and `> Parent:` |
| `.tfw/workflows/research/base.md` | Step 3: removed batch template copy. Step 4: added copy-on-enter for briefing. Step 5: restructured as FOR EACH per-stage loop with copy→mindset→OODA→checkpoint→STOP |
| `.agent/workflows/tfw-research.md` | Byte-copy sync from base.md |
| `.claude/commands/tfw-research.md` | Byte-copy sync from base.md |
| `.tfw/VERSION` | `0.8.6` → `0.8.7` |
| `.tfw/project_config.yaml` | version: `0.8.6` → `0.8.7` |
| `.tfw/CHANGELOG.md` | Added `[0.8.7]` entry with Added/Changed/Removed sections |

## 2. Key Decisions

1. **Template rewrite vs edit**: Rewrote all 4 templates (overwrite) rather than in-place edit because the Mindset block insertion point is between h1 and `> Parent:` — the entire header region changes. Cleaner than multi-line insertions. All existing content below the header preserved exactly.

2. **Step 5 "FOR EACH" as numbered sub-steps**: Used numbered sub-steps (1. Copy, 2. Read Mindset, 3. Execute OODA, 4. Complete Checkpoint, 5. 🛑 STOP) inside a bold **FOR EACH stage** block. This matches KC5 (process F4: agents follow numbered steps + gates perfectly).

3. **Step 4 copy instruction phrasing**: Changed from "Write Briefing to... using `templates/research/1_briefing.md`" to explicit "Copy `templates/research/1_briefing.md` into `research/iterN/`. Read the **Mindset** block — adopt this cognitive mode." The word "copy" is deliberate and structural.

## 3. Acceptance Criteria

- [x] **AC-1**: Each research template has `> **Mindset:**` + `> **Test:**` blockquote — exact wording from TS §4 verified
- [x] **AC-2**: Step 3 creates only the folder — no template copying (batch copy line removed)
- [x] **AC-3**: Step 4 explicitly copies `1_briefing.md` before writing (copy-on-enter)
- [x] **AC-4**: Step 5 restructured as FOR EACH with per-stage copy + mindset + OODA + checkpoint
- [x] **AC-5**: 🛑 STOP present in the FOR EACH loop (sub-step 5) — each stage gets its own stop
- [x] **AC-6**: Step 0 Resume Protocol compatible — "which stage files exist? Resume from first missing stage" — no assumption that all files pre-exist
- [x] **AC-7**: Adapters byte-identical (SHA-256 verified: `D30A54C9...DBA0` all 3 files)
- [x] **AC-8**: VERSION=`0.8.7`, project_config.yaml version=`0.8.7`, CHANGELOG `[0.8.7]` entry with all items

## 4. Verification

- Lint (`echo "configure your lint command"`): N/A — methodology framework, no code lint
- Tests (`echo "configure your test command"`): N/A — no automated tests for markdown templates
- Verify: SHA-256 hash comparison confirms all 3 copies of base.md are byte-identical

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `conventions.md` | 152 | style | L152 says "Stage file format: see `.tfw/templates/research/` (`1_briefing.md`, `2_gather.md`, `3_extract.md`, `4_challenge.md`)." — doesn't mention Mindset blocks. Not critical since templates are self-documenting, but conventions text could note the Mindset block as a characteristic of research stage templates (like review templates have in L195) |

## 6. Fact Candidates

> **Cognitive mode:** Pure reporting — record factual observations without interpretation or synthesis.

No fact candidates. No human interaction occurred during execution — this was a clean AG implementation of a fully specified TS.

## 7. Strategic Insights (Execution)

No strategic insights. No human domain knowledge provided during execution.

## 8. Diagrams

```
BEFORE (batch copy):
  Step 3: mkdir + copy [1][2][3][4] ──→ all 4 files exist immediately
  Step 5: fill 1, fill 2, fill 3, fill 4 (no cognitive shift)
  Resume: sees 4 files → "all done" (broken)

AFTER (copy-on-enter):
  Step 3: mkdir only
  Step 4: copy [1] → Mindset → fill → STOP
  Step 5: FOR EACH [2,3,4]:
            copy → Mindset → OODA → Checkpoint → STOP
  Resume: sees [1][2] → "start at [3]" (correct)
```

---

*RF — TFW-43: Research Stage Protocol | 2026-05-01*
