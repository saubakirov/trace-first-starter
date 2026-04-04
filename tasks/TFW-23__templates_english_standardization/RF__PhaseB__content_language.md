# RF — TFW-23 / Phase B: Content Language Config

> **Date**: 2026-04-04
> **Author**: Executor
> **Status**: 🟢 RF — Complete
> **Parent HL**: [HL-TFW-23](HL-TFW-23__templates_english_standardization.md)
> **TS**: [TS Phase B](TS__PhaseB__content_language.md)

---

## 1. What Was Done

### Modified Files
| File | Changes |
|------|---------|
| `.tfw/PROJECT_CONFIG.yaml` | Added `content_language: en` (line 12) |
| `.tfw/conventions.md` | Added Content Language rule to §11 Quality Standard (line 240) |
| `.tfw/workflows/init.md` | Added language question to Phase 2 Interview Batch 1 (line 45) |
| `.tfw/workflows/config.md` | Added `content_language` section to Config Sync Registry (lines 88-92) |

## 2. Key Decisions

1. **Placed rule in §11 Quality Standard** — not a separate section. Content language is a quality concern: "how agents produce output"
2. **One question in Batch 1** — kept minimal: "What language should I use for artifact content? (default: English)"

## 3. Acceptance Criteria

- [x] `tfw.content_language: en` exists in PROJECT_CONFIG.yaml
- [x] Convention rule explains how agents use the key
- [x] tfw-init asks user for preferred language
- [x] Config Sync Registry has entry for content_language

## 4. Verification

- grep `content_language` in PROJECT_CONFIG.yaml: ✅ line 12
- grep `Content Language` in conventions.md: ✅ line 240
- grep `artifact content` in init.md: ✅ line 45
- grep `content_language` in config.md: ✅ lines 88, 92

## 5. Observations (out-of-scope, not modified)

| # | File | Line(s) | Type | Description |
|---|------|---------|------|-------------|
| 1 | `.tfw/workflows/config.md` | 19 | naming | Edit mode prompt still in Russian: "Что хотите изменить в конфигурации?" |
| 2 | `.tfw/workflows/config.md` | 29 | naming | Confirmation prompt in Russian: "Применить? ({N} файлов)" |

## 6. Fact Candidates

| # | Category | Candidate | Source | Confidence |
|---|----------|-----------|--------|------------|
| 1 | process | When user requests a feature during research and coordinator defers it unilaterally (without gate approval), the user loses trust in the process. Gate skipping = feature loss | Session observation: content_language was requested by user but deferred without approval | High |
| 2 | convention | `content_language` is a project-level config, not personal preference. `.user_preferences.md` already has personal `Language:` field (init.md line 104). These serve different purposes: project content language vs personal communication preference | init.md analysis | Medium |

---

*RF — TFW-23 / Phase B: Content Language Config | 2026-04-04*
