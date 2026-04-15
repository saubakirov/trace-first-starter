# Map — "What was done?"
> **Mindset:** Experienced newcomer. You arrived after someone else's work. Understand before you judge. No opinions yet — only comprehension.
> **Test:** "Can I explain what was done to someone who hasn't read the RF?"
> RF: [RF Phase B](../RF__PhaseB__naming_normalization.md)
> TS: [TS Phase B](../TS__PhaseB__naming_normalization.md)
> Mode: spec

## Understanding

The executor normalized file naming across `.tfw/` — renamed `PROJECT_CONFIG.yaml` → `project_config.yaml` (via `git mv`) and `TOPIC_FILE.md` → `topic_file.md`, then performed a global find-replace across 28 source files + 8 adapter copies (36 total). Added §10.4 (YAML File Naming Convention) to `conventions.md` codifying `lower_snake_case` for config/state YAML and non-artifact templates. Version bumped to 0.8.4 with a combined CHANGELOG entry covering both Phase A and Phase B changes, plus migration notes for downstream projects. Scope was expanded beyond the original TS (`.tfw/` only) to include `README.md`, `KNOWLEDGE.md`, and `docs/scripts/gen_docs.py` + tests — per coordinator's ONB answer ("Битые ссылки = баг, а не tech debt").

## TS ↔ RF Alignment

| TS requirement | RF claim | Aligned? |
|----------------|----------|----------|
| AC1: `grep -r "PROJECT_CONFIG" .tfw/` returns 0 | RF §3 ✓, only §10.4 negative example remains ("not `PROJECT_CONFIG.yaml`") | ✅ |
| AC2: `grep -r "TOPIC_FILE" .tfw/` returns 0 | RF §3 ✓ | ✅ |
| AC3: `.tfw/project_config.yaml` exists, old doesn't | RF §3 ✓, `git mv` executed | ✅ |
| AC4: `.tfw/templates/topic_file.md` exists, old doesn't | RF §3 ✓, `git mv` executed | ✅ |
| AC5: §10.4 naming convention in conventions.md | RF §3 ✓, lines 329-339 | ✅ |
| AC6: Version = 0.8.4 in VERSION, project_config, template | RF §3 ✓ | ✅ |
| AC7: CHANGELOG has v0.8.4 with migration notes | RF §3 ✓ | ✅ |
| AC8: 55/55 gen_docs tests pass | RF §3 ✓ | ✅ |
| AC9: Adapter workflows synced | RF §3 ✓, grep .agent/ = 0 | ✅ |
| AC10: README.md and KNOWLEDGE.md refs updated | RF §3 ✓ | ✅ |
| AC11: Historical task artifacts NOT modified | RF §3 ✓ | ✅ |

## Deviations from TS

- TS scope was `.tfw/` (19+ files). Executor expanded to include `README.md`, `KNOWLEDGE.md`, `gen_docs.py`, `test_gen_docs.py`, and `.agent/` adapter copies. This is a legitimate scope expansion via Q&A (ONB Q1 answer) — not a deviation.
- TS Step 1 suggested `Rename-Item`, executor used `git mv` instead (RF Decision D1). Better approach — preserves git history.
- No out-of-scope work detected.

## Checkpoint

**Self-check:**
- [x] Read RF §1-§5 completely?
- [x] Read TS DoD and matched each item to RF §3?
- [x] Read HL §7 Principles — can I state the design philosophy?
- [x] Read ONB — were blocking questions resolved?

Stage complete: YES
