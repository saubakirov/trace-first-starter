# Antigravity Adapter Setup

Antigravity uses `.agent/rules/` (always-on) and `.agent/workflows/` (on-demand).

## Setup

### 1. Copy the TFW rule

```bash
mkdir -p .agent/rules
cp .tfw/adapters/antigravity/tfw-rules.md.template .agent/rules/tfw.md
```

This rule loads TFW context in every Antigravity chat.

### 2. Copy TFW workflows

```bash
mkdir -p .agent/workflows
cp .tfw/workflows/plan.md .agent/workflows/tfw-plan.md
cp .tfw/workflows/handoff.md .agent/workflows/tfw-handoff.md
cp .tfw/workflows/resume.md .agent/workflows/tfw-resume.md
```

Antigravity reads `.agent/workflows/` directly, so files must be copied (not referenced).

### 3. Add project-specific rules and workflows

You can add more files alongside the TFW ones:

```
.agent/rules/
├── tfw.md                  # TFW v3 (from step 1)
├── agents.md               # Your AI role and mission
└── safety-rules.md         # Domain-specific safety rules

.agent/workflows/
├── tfw-plan.md             # TFW plan (from step 2)
├── tfw-handoff.md          # TFW handoff (from step 2)
├── tfw-resume.md           # TFW resume (from step 2)
├── deploy-api.md           # Your deploy workflow
└── build-project.md        # Your build workflow
```

## Keeping Workflows in Sync

When `.tfw/workflows/` is updated, re-copy:

```bash
cp .tfw/workflows/plan.md .agent/workflows/tfw-plan.md
cp .tfw/workflows/handoff.md .agent/workflows/tfw-handoff.md
cp .tfw/workflows/resume.md .agent/workflows/tfw-resume.md
```
