# KNOWLEDGE.md — Project Knowledge Index

> Central index of project architecture, decisions, and evolution.
> **Principle**: Index, don't duplicate — link to RF/HL files, don't copy their contents.

---

## 0. Philosophy & Principles

> Core principles that guide all decisions. Each links to the HL/RF where it was formalized.

| # | Principle | Source |
|---|-----------|--------|
| P1 | _Describe your first principle_ | `tasks/{ID}/HL-...md` |
| P2 | _Second principle_ | `tasks/{ID}/RF-...md` |

---

## 1. Architecture Map

> High-level view of the system's components and their relationships.

### Components

| Component | Description | Key Files |
|-----------|-------------|-----------|
| _API Server_ | _Main backend_ | `src/api/` |
| _Frontend_ | _Web UI_ | `src/web/` |

### Architecture Decisions

| # | Decision | Rationale | Source RF |
|---|----------|-----------|-----------|
| D1 | _e.g., Chose PostgreSQL over MongoDB_ | _ACID compliance needed_ | `tasks/{ID}/RF-...md` |

---

## 2. Key Artifacts

> Most important task artifacts for understanding the project. Read these first.

| Task | Title | Key Artifact | Why Important |
|------|-------|-------------|---------------|
| _PROJ-1_ | _Initial setup_ | `tasks/PROJ-1.../RF-...md` | _Foundation decisions_ |

---

## 3. Legacy & Deprecation

> What was dropped, frozen, or replaced — and why.

| Item | Status | When | Replacement | Source |
|------|--------|------|-------------|--------|
| _e.g., Old auth module_ | Deprecated | _2026-01_ | _OAuth2 flow_ | `tasks/{ID}/RF-...md` |

---

## 4. Tech Stack & Infrastructure

> Current production stack. Update when infrastructure changes.

| Layer | Technology | Notes |
|-------|-----------|-------|
| _Backend_ | _Python / Node / etc._ | |
| _Database_ | _PostgreSQL / etc._ | |
| _Hosting_ | _GCP / AWS / etc._ | |
| _CI/CD_ | _GitHub Actions / etc._ | |

---

> **Maintenance**: This file is updated via the `tfw-docs` workflow after each REVIEW.
> See `.tfw/workflows/docs.md` for the update process.
