# HL — TFW-9: Update Source Mechanism

> **Date**: 2026-03-12
> **Author**: Coordinator (AI)
> **Status**: 🔵 HL — Awaiting review

---

## 1. Vision

Downstream projects can discover, fetch, and apply upstream TFW updates with a single config field and a gitignored staging directory — no OS-specific hacks, no hardcoded URLs.

## 2. As-Is (Problem)

`tfw-update` workflow says "Obtain upstream" **11 times** but never explains:
1. **Where** — no URL, no config field, no repo reference
2. **How** — no git command, no download instruction
3. **Where to put it** — no staging directory, `/tmp` is OS-specific

### Real-world scenario (Innoforce)

Company forks `trace-first-starter` to an internal repo. All company projects must pull updates from the internal fork, not from the public GitHub. Currently there's nowhere to configure this.

### Root cause

`PROJECT_CONFIG.yaml` has no `tfw.upstream` field. `update.md` has no fetch step.

## 3. To-Be

### Design decisions

**D1: One config field `tfw.upstream`** — URL to the upstream TFW starter repo.
- Default: `https://github.com/saubakirov/trace-first-starter`
- Companies override with their internal fork URL
- Canonical reference stays in `.tfw/README.md` §Canonical Reference (not in config)
- Why one field, not two (canonical + upstream): avoids "which one to use?" confusion

**D2: `.tfw/.upstream/` staging directory** — gitignored, inside the project.
- Workflow clones upstream here during update
- OS-independent: no `/tmp`, no `$TMPDIR`, no `$env:TEMP`
- Gitignored: no pollution in version control
- Can be cleaned after update or left (harmless)

**D3: Step 0 in `update.md`** — concrete fetch instructions.
- Reads `tfw.upstream` from config
- Clones to `.tfw/.upstream/`
- If `.tfw/.upstream/` already exists from previous update — clean and re-clone

### Flow after change

```
1. Agent reads PROJECT_CONFIG.yaml → tfw.upstream = "https://..."
2. Agent clones upstream into .tfw/.upstream/
3. Agent reads .tfw/.upstream/.tfw/VERSION → target version
4. Agent reads .tfw/.upstream/.tfw/CHANGELOG.md → changes list
5. Agent follows existing Steps 1-8 (compare, categorize, checklist, apply)
6. Clean .tfw/.upstream/ when done
```

## 4. Phases

### Single Phase 🔴

| # | File | Action | Description |
|---|------|--------|-------------|
| 1 | `.tfw/PROJECT_CONFIG.yaml` | MODIFY | Add `tfw.upstream` field with default URL |
| 2 | `.tfw/workflows/update.md` | MODIFY | Add Step 0: Fetch Upstream, update prerequisites to reference config |
| 3 | `.tfw/init.md` | MODIFY | Mention `tfw.upstream` in Step 2 (configure), mention `.upstream/` in .gitignore |
| 4 | `.tfw/glossary.md` | MODIFY | Update `tfw-update` entry to mention source resolution |
| 5 | `.gitignore` | MODIFY | Add `.tfw/.upstream/` |

Scope: 0 NEW + 5 MODIFY. Within budget.

## 5. Definition of Done (DoD)

- ✅ 1. `PROJECT_CONFIG.yaml` has `tfw.upstream` field with `https://github.com/saubakirov/trace-first-starter`
- ✅ 2. `update.md` Step 0 reads `tfw.upstream`, clones to `.tfw/.upstream/`, with cleanup
- ✅ 3. `.gitignore` has `.tfw/.upstream/` entry
- ✅ 4. `init.md` mentions `tfw.upstream` and `.upstream/` gitignore
- ✅ 5. Agent can follow `update.md` end-to-end: knows where, how, and where to put files

## 6. Definition of Failure (DoF)

- ❌ 1. Agent still doesn't know where to get upstream files
- ❌ 2. Hardcoded URL without config fallback
- ❌ 3. `.tfw/.upstream/` committed to git

## 7. Principles

- P1: Reproducibility — update process fully self-contained
- P5: Meta-project awareness — this repo IS the default upstream
- Portability — `.tfw/.upstream/` works on any OS

## 8. Risks

| Risk | Mitigation |
|------|------------|
| Private repos need auth for git clone | CL mode — user runs the command, handles auth |
| `.tfw/.upstream/` left after failed update | Gitignored, harmless. Step 0 cleans before clone |
| Company fork diverges from canonical | `tfw.upstream` points to company fork; canonical stays in `.tfw/README.md` for reference |

---

*HL — TFW-9: Update Source Mechanism | 2026-03-12*
