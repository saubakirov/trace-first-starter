# TS — TFW-23 / Phase B: Content Language Config

> **Date**: 2026-04-04
> **Author**: Coordinator
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-23](HL-TFW-23__templates_english_standardization.md)

---

## 1. Objective
Add `tfw.content_language` config key so agents know what language to use when filling artifact content. Templates stay English (Phase A). Content follows user's preferred language from config. During `tfw-init`, user is asked for their preference.

## 2. Scope

### In Scope
- Add `tfw.content_language: en` to `PROJECT_CONFIG.yaml`
- Add convention rule to `conventions.md` §4 (Naming)
- Add init question to `tfw-init` workflow (Phase 2: Interview)
- Register key in Config Sync Registry (`config.md`)

### Out of Scope
- Changing template files (done in Phase A)
- Adding locale directories or translation files
- Changing AGENTS.md or .tfw/README.md

## 3. Affected Files

| File | Action | Description |
|------|--------|------------|
| `.tfw/PROJECT_CONFIG.yaml` | MODIFY | Add `content_language: en` under `tfw:` block |
| `.tfw/conventions.md` | MODIFY | Add content language rule: agents fill content in configured language |
| `.tfw/workflows/init.md` | MODIFY | Add question about preferred content language to Phase 2 Interview |
| `.tfw/workflows/config.md` | MODIFY | Add `content_language` entry to Config Sync Registry |

**Budget:** 0 new files, 4 modifications. Within limits.

## 4. Detailed Steps

### Step 1: Add config key to PROJECT_CONFIG.yaml
Add after line 11 (`initial_seq: 12`):
```yaml
  content_language: en      # Language for filled artifact content (en, ru, etc.)
```

### Step 2: Add convention rule to conventions.md
Find section `4) Naming`. Add rule:
```
**Content Language:** Template structure (headings, labels, field names) is always English.
Artifact content is filled in the language specified by `tfw.content_language` in PROJECT_CONFIG.yaml.
Default: `en`. Agent MUST check this value before writing artifacts.
```

### Step 3: Update tfw-init workflow
In Phase 2 Interview, add to Batch 1 (line 43-44 area):
```
- "What language should I use for artifact content? (default: English)"
```
In Phase 2 Mini-Setup (line 52), ensure the answer is written to `tfw.content_language` in PROJECT_CONFIG.yaml.

### Step 4: Register in Config Sync Registry
Add new section to `config.md` after `### knowledge`:
```markdown
### content_language

| Config Key | Target File | Section Header | Row Label |
|------------|------------|----------------|-----------|
| `content_language` | `.tfw/conventions.md` | 4) Naming | Content Language |
```

### Step 5: Verify
- Check `PROJECT_CONFIG.yaml` has `content_language: en`
- Check `conventions.md` has the content language rule
- Check `init.md` has the language question
- Check `config.md` has the registry entry

## 5. Acceptance Criteria

- [ ] `tfw.content_language: en` exists in PROJECT_CONFIG.yaml
- [ ] Convention rule explains how agents use the key
- [ ] tfw-init asks user for preferred language
- [ ] Config Sync Registry has entry for content_language

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| Agents ignore the config key | Convention rule uses MUST language |
| init.md becomes cluttered | One question added to existing batch — minimal |

---

*TS — TFW-23 / Phase B: Content Language Config | 2026-04-04*
