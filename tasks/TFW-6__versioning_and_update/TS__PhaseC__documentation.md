# TS — TFW-6 / Phase C: Documentation & Traces

> **Date**: 2026-03-12
> **Author**: Coordinator (AI)
> **Status**: 🟡 TS — Awaiting approval
> **Parent HL**: [HL-TFW-6](HL-TFW-6__versioning_and_update.md)

---

## 1. Goal

Update all documentation to reflect the new versioning infrastructure and workflows. Add architecture decisions to KNOWLEDGE.md, mention new workflows in `.tfw/README.md`, and update root README.md. After this phase, TFW-6 is fully traceable and all documentation is consistent.

## 2. Scope

### In Scope
- Update `KNOWLEDGE.md` — new D-records for version scheme, release/update workflows, RELEASE.md artifact
- Update `.tfw/README.md` — §Canonical Workflows to mention release + update
- Update root `README.md` — mention versioning in "What's Inside" section

### Out of Scope
- Code changes — all done in Phase A and B
- Adapter templates for Claude Code / Cursor — separate future concern

## 3. Files

| File | Action | Description |
|------|--------|-------------|
| `KNOWLEDGE.md` | MODIFY | Add D-records: D9 (version scheme), D10 (tfw-release), D11 (tfw-update), D12 (RELEASE.md). Add RELEASE.md to Architecture Map. |
| `.tfw/README.md` | MODIFY | §Canonical Workflows table: add release + update rows. §Project Structure: add VERSION, CHANGELOG. |
| `README.md` | MODIFY | "What's Inside" / .tfw/ table: add VERSION, CHANGELOG. §Tool Adapters or §Key Concepts: mention versioning. |

**Budget:** 0 new files, 3 modifications. ≤7 files ✅, ≤4 new ✅, ≤600 LOC ✅.

## 4. Detailed Steps

### Step 1: Update KNOWLEDGE.md

**A) Architecture Map → Framework Structure table — add rows:**

| Component | Description | Key Files |
|-----------|-------------|-----------|
| Versioning | Framework version tracking and changelog | `.tfw/VERSION`, `.tfw/CHANGELOG.md` |
| Release | Release strategy and process | `RELEASE.md` (optional), `.tfw/workflows/release.md` |

**B) Architecture Decisions — add:**

| # | Decision | Rationale | Source |
|---|----------|-----------|--------|
| D9 | Semver (MAJOR.MINOR.PATCH) for TFW versioning | Industry standard, easy to communicate breaking vs compatible changes | TFW-6 HL §3 |
| D10 | `tfw-release` as canonical workflow, `RELEASE.md` as project context | Separation: general process in workflow, specific context in per-project file | TFW-6 HL §3, discussion |
| D11 | `tfw-update` with 🟢🟡🔴 change categorization | Prevents overwriting project customizations during framework upgrades | TFW-6 HL §3 |
| D12 | `RELEASE.md` optional (like `KNOWLEDGE.md`) | Avoids file inflation for projects that don't release | TFW-6 discussion |

**C) Key Artifacts — add TFW-6 row:**

| Task | Title | Key Artifact | Why Important |
|------|-------|-------------|---------------|
| TFW-6 | Versioning + update | `tasks/TFW-6.../HL-TFW-6...md` | Version scheme, release/update workflow design, RELEASE.md pattern |

### Step 2: Update `.tfw/README.md`

**A) §Canonical Workflows table — add two rows:**

| Workflow | Role | What it does |
|----------|------|-------------|
| **release** | Coordinator | Read RELEASE.md → scope release → bump version → update CHANGELOG |
| **update** | Coordinator | Compare versions → categorize changes → checklist → re-sync adapters |

**B) §Project Structure tree — add under `.tfw/`:**

```
│   ├── VERSION       # Current framework version (semver)
│   ├── CHANGELOG.md  # Version history
```

And under root:
```
├── RELEASE.md         # Release strategy (optional)
```

### Step 3: Update root `README.md`

**A) "What's Inside" → .tfw/ table — add rows:**

| Path | Contents |
|------|----------|
| `.tfw/VERSION` | Current framework version (semver) |
| `.tfw/CHANGELOG.md` | Version history |

**B) Root Files table — add optional artifact:**

| File | Purpose |
|------|---------|
| `RELEASE.md` | Release strategy and context (optional) |

**C) §Key Concepts — add versioning bullet:**

```markdown
- **Versioning**: semver in `.tfw/VERSION`, changelog in `.tfw/CHANGELOG.md` — [details](.tfw/CHANGELOG.md)
```

## 5. Acceptance Criteria

- [ ] `KNOWLEDGE.md` has D9, D10, D11, D12 decisions and TFW-6 in Key Artifacts
- [ ] `.tfw/README.md` §Canonical Workflows lists 5 workflows (plan, handoff, resume, release, update)
- [ ] `.tfw/README.md` §Project Structure includes VERSION and CHANGELOG
- [ ] Root `README.md` mentions VERSION, CHANGELOG, and RELEASE.md in "What's Inside"
- [ ] Root `README.md` §Key Concepts mentions versioning
- [ ] All cross-references are valid (links to new files work)

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| Documentation references files not yet created | Execute Phase C only after Phase A and B are complete |
| `.tfw/README.md` changes conflict with TD-4 (workflow list incomplete) | This phase resolves TD-4 by adding the full workflow list |

---

*TS — TFW-6 / Phase C: Documentation & Traces | 2026-03-12*
