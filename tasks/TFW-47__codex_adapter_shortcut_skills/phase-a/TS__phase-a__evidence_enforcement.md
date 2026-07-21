# TS — TFW-47 / Phase A: Evidence Enforcement

> **Date**: 2026-07-17
> **Author**: Coordinator (Antigravity)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-47](../HL-TFW-47__codex_adapter_shortcut_skills.md)
> **Phase HL**: [HL Phase A](HL__phase-a__evidence_enforcement.md)
> **Research**: [iter1/RES.md](../research/iter1/RES.md) (evidence template design)

---

## 1. Objective

Make `evidence/` a mandatory subfolder in every task directory and provide a structured EV template that executors fill with real verification results. This closes the gap where 0/38 tasks created the folder despite D52 defining evidence as a first-class concept. RF §5 becomes a pointer to the EV file — one source of truth.

## 2. Scope

### In Scope
- Create EV template (`.tfw/templates/evidence/EV.md`)
- Update conventions.md §3 and §4 — mandatory evidence folder
- Update TS template — evidence artifacts section
- Update RF template §5 — pointer to EV file
- Update handoff.md Step 11 — evidence folder creation step
- Update KNOWLEDGE.md — revoke D16, extend D52

### Out of Scope
- Codex adapter (Phase B-E)
- Modifying existing completed tasks to add evidence/
- Review template changes (verify.md, judge.md) — these already reference RF §5 artifacts
- Glossary changes (deferred to Phase D)

## 3. Principles Check

| # | Principle (from HL §7) | Enforced by | Gate |
|---|----------------------|-------------|------|
| P1 | Evidence is mandatory, not optional | AC-1, AC-2, AC-3, AC-4 | conventions.md §4 lists evidence/ as mandatory |
| P2 | Template reflects values | AC-1 | EV template structure validated against iter1 D2/D5/D6 |
| P3 | Thin adapters over duplicated workflows | N/A | Phase A is evidence-only, no adapter changes |

## 4. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `.tfw/templates/evidence/EV.md` | CREATE | Evidence template: environment header + per-AC table + verdict + attachments index |
| `.tfw/conventions.md` | MODIFY | §3: mandatory folder language. §4: add `evidence/` to folder structure. §14: update anti-pattern (remove "optional" wording from D16) |
| `.tfw/templates/TS.md` | MODIFY | Add `## Evidence Artifacts` section after AC section |
| `.tfw/templates/RF.md` | MODIFY | §5: replace inline table with pointer to EV file |
| `.tfw/workflows/handoff.md` | MODIFY | Step 11: add evidence folder creation substep |
| `KNOWLEDGE.md` | MODIFY | Revoke D16 optional status, extend D52 |

**Budget:** 1 new file, 5 modifications = 6 total. Within limits (max 14 files, max 8 new).

## 5. Acceptance Criteria

### AC-1: EV template exists and follows research design

The evidence template captures real verification results in a structured format aligned with TFW values: trace-first, honest, reproducible.

- [ ] `.tfw/templates/evidence/EV.md` exists
- [ ] Contains Environment header with fields: Date, Author, OS, Language/Runtime (if applicable), Database (if applicable), Deploy target (if applicable), CI/Pipeline (if applicable)
- [ ] Contains per-AC evidence table with columns: `# | AC | What was verified | Environment | Result | Artifact`
- [ ] Result column uses 4-status vocabulary: VERIFIED / DEFERRED / BLOCKED / N/A
- [ ] Contains Verdict line: `{N}/{M} VERIFIED, {X} DEFERRED, {Y} BLOCKED, {Z} N/A`
- [ ] Contains optional Attachments section for binary artifacts in `evidence/`
- [ ] File naming pattern documented: `EV__{PREFIX}-{N}__{title}.md` (single-phase), `EV__phase-{x}__{title}.md` (multi-phase)

Gate: File exists at path, all structural elements present in template
Evidence: N/A — template is a definition document, not runtime output

### AC-2: conventions.md updated — evidence folder mandatory

conventions.md formally requires `evidence/` as a mandatory task subfolder.

- [ ] §3 (Evidence Sections): language updated — folder creation is required, not optional. Reference D16 revocation.
- [ ] §4 (Task Numbering): `evidence/` shown in folder structure examples (single-phase and multi-phase)
- [ ] §4: EV file naming added to artifact naming table
- [ ] §14 (Anti-patterns): any language from D16 about "only when binary artifacts exist" removed or replaced with "always required"

Gate: `grep -c "evidence/" conventions.md` returns ≥3 hits (§3, §4 single, §4 multi). No "optional" or "only when binary" language in evidence sections.
Evidence: N/A — conventions.md is a definition document

### AC-3: TS template includes Evidence Artifacts section

The TS template tells coordinators to specify what evidence files the executor should produce.

- [ ] New section `## Evidence Artifacts` added after §5 (Acceptance Criteria) — or as a subsection of §5
- [ ] Contains guidance: "List expected evidence files. Minimum: one EV file. Additional binary artifacts if applicable."
- [ ] Example showing: `evidence/EV__{PREFIX}-{N}__{title}.md` (required), optional binary files

Gate: Section exists in template, guidance text present
Evidence: N/A — template spec

### AC-4: RF template §5 updated — pointer to EV file

RF §5 becomes a single-line reference to the EV file. No more inline evidence table duplication.

- [ ] §5 Evidence section replaced with pointer format: `See [EV file](evidence/EV__...) for evidence details.`
- [ ] Verdict line preserved (summary still visible in RF): `Evidence verdict: {N}/{M} VERIFIED...`
- [ ] Cognitive mode comment preserved (observational verification)
- [ ] Old inline table removed

Gate: RF template §5 contains pointer, not inline table. Verdict line present.
Evidence: N/A — template spec

### AC-5: handoff.md Step 11 updated — evidence folder creation

Handoff workflow explicitly instructs executor to create `evidence/` folder and populate EV template.

- [ ] Step 11 includes substep: "Create `evidence/` folder in task directory (or phase directory for multi-phase)"
- [ ] Substep: "Copy `.tfw/templates/evidence/EV.md` to `evidence/EV__{PREFIX}-{N}__{title}.md`"
- [ ] Substep: "Fill EV template with real verification results for each AC item"
- [ ] Old language "Record results in RF §5 Evidence table" updated to "Record results in EV file, RF §5 points to EV"
- [ ] Condition "If NO TS AC items have Evidence fields — skip this step" **removed** — evidence folder always created

Gate: handoff.md Step 11 contains create + copy + fill substeps. No skip condition.
Evidence: N/A — workflow spec

### AC-6: KNOWLEDGE.md updated — D16 revoked, D52 extended

Architecture decisions updated to reflect the new mandatory evidence policy.

- [ ] D16 status changed to "REVOKED" or equivalent — with justification: "0/38 tasks created evidence folder under optional policy"
- [ ] D52 extended — add: "evidence/ folder mandatory, contains EV template file. RF §5 is a pointer to EV, not inline table."
- [ ] Version reference updated if applicable

Gate: D16 contains revocation language, D52 contains extension text
Evidence: N/A — knowledge document

## 6. Technical Guidance

- **EV template structure** (from iter1 D2/D5/D6/D7):
  - Header: task metadata + environment fields
  - Table: per-AC rows, identical columns to current RF §5
  - Verdict: summary line with counts per status
  - Attachments: optional index of binary files in evidence/
- **Proportionality** (iter1 D4): no template tiers. Minimum bar = environment header + ≥1 evidence row. Table length IS the proportionality.
- **"(if applicable)" fields** in environment header handle diversity across task types — methodology tasks won't have DB or CI fields.
- **RF §5 pointer format**: Keep the cognitive mode comment (observational verification) and verdict line in RF. Only the detailed table moves to EV.
- **Multi-phase**: evidence folder goes in phase directory, not task root. `phase-a/evidence/EV__phase-a__title.md`.
- **Anti-pattern update**: conventions.md §14 item about "VERIFIED without artifact reference" gets stronger — the artifact is now always in `evidence/`.

## 7. Definition of Failure

- ❌ EV template is a freeform dump without structured sections (no header, no per-AC table, no verdict)
- ❌ conventions.md still contains "optional" or "only when binary" language about evidence folder
- ❌ RF §5 retains the full inline evidence table (duplication with EV)
- ❌ handoff.md Step 11 still allows skipping evidence folder creation
- ❌ KNOWLEDGE.md D16 not explicitly revoked — agents can still cite it as justification for skipping

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| Existing review templates (verify.md, judge.md) reference "RF §5 artifacts" | They reference artifact paths — EV file path works the same way. No change needed in Phase A. |
| Executor uses old RF template without pointer | Gate check: RF §5 must be pointer format, not inline table |

## 9. Cross-Phase Modifications (multi-phase)

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `conventions.md` | Phase D (glossary/docs integration) | Phase A changes §3, §4, §14. Phase D changes §other sections for Codex. No overlap. |
| `KNOWLEDGE.md` | Phase D | Phase A modifies D16/D52. Phase D may add new decisions. No conflict. |

---

*TS — TFW-47 / Phase A: Evidence Enforcement | 2026-07-17*
