# TS — TFW-8: Reviewer Role and Workflow

> **Date**: 2026-03-12
> **Author**: Coordinator (AI)
> **Status**: 🟡 TS — Awaiting approval
> **Parent HL**: [HL-TFW-8](HL-TFW-8__reviewer_role_and_workflow.md)

---

## 1. Goal

Extract review from `handoff.md` into a standalone `/tfw-review` workflow with its own Role Lock, add a Reviewer role to the glossary and conventions, update all references across the project, and log the change in CHANGELOG. Two phases: A = core extraction, B = documentation sync.

## 2. Scope

### In Scope
- **Phase A**: Create review workflow + adapter, gut handoff Phase 4, fix Role Lock, update glossary/AGENTS/CHANGELOG
- **Phase B**: Sync all doc references (`.tfw/README.md`, `plan.md`, `resume.md`, `init.md`, adapter README)

### Out of Scope
- REVIEW template changes (template is already solid — REVIEW template `{coordinator}` → `{reviewer}` noted for future)
- Claude Code / Cursor adapter copies (not actively maintained here, see TD-7)
- Status flow changes (`🔍 REV` stays as-is)
- `plan.md` / `resume.md` / other workflow structural changes (only reference updates)

## 3. Affected Files

### Phase A: Core extraction (2 NEW + 6 MODIFY)

| File | Action | Description |
|------|--------|-------------|
| `.tfw/workflows/review.md` | CREATE | Canonical review workflow with Role Lock: Reviewer |
| `.agent/workflows/tfw-review.md` | CREATE | Adapter copy (byte-identical, YAML frontmatter) |
| `.tfw/workflows/handoff.md` | MODIFY | Remove Phase 4 (L99-140), add STOP block, update header/role lock/diagram/anti-patterns |
| `.agent/workflows/tfw-handoff.md` | MODIFY | Adapter sync — same edits as canonical handoff.md |
| `.tfw/conventions.md` | MODIFY | §8 add review.md row, fix handoff role; §14 add anti-pattern; §15 fix Role Lock table |
| `.tfw/glossary.md` | MODIFY | Add Reviewer role; update Coordinator role; update Workflow definition |
| `AGENTS.md` | MODIFY | Add review.md to workflow list, update handoff description |
| `.tfw/CHANGELOG.md` | MODIFY | Add entry in `[Unreleased]` section |

**Budget:** 2 NEW + 6 MODIFY = 8 files. Over by 1 — justified: 2 MODIFYs are adapter copies (byte-identical to canonical).

### Phase B: Documentation sync (0 NEW + 5 MODIFY)

| File | Action | Description |
|------|--------|-------------|
| `.tfw/README.md` | MODIFY | L77 directory tree, L168 workflows table, L281 evolution |
| `.tfw/workflows/plan.md` | MODIFY | L14, L76 — add `/tfw-review` mention after handoff |
| `.tfw/workflows/resume.md` | MODIFY | L83 — add review step reference |
| `.tfw/init.md` | MODIFY | L97, L184, L192 — add review to workflow lists |
| `.tfw/adapters/antigravity/README.md` | MODIFY | L21, L39, L51 — add review workflow to adapter setup |

**Budget:** 0 NEW + 5 MODIFY = 5 files. Within budget ✅

## 4. Detailed Steps — Phase A

### Step 1: Create `.tfw/workflows/review.md`

Canonical review workflow. Must contain:

- **YAML frontmatter**: `description: TFW Review — reviewer checks RF against TS, writes REVIEW, triages tech debt`
- **Role Lock block**: `🔒 ROLE LOCK: REVIEWER` — permitted: REVIEW file; forbidden: code, ONB, RF, HL, TS
- **Context Loading**: same as executor context loading + RF as mandatory read + TS for DoD check
- **Review process**: the 9-point checklist from current `handoff.md` Phase 4 (L103-115)
- **Tech Debt Collection**: exact same process from handoff.md L119-133 (read observations → triage → TECH_DEBT.md)
- **Verdict section**: APPROVE / REVISE / REJECT with trace updates
- **Anti-patterns**: reviewer-specific (e.g., reviewing without reading RF, skipping observations triage, executor writing REVIEW)
- **REVISE flow**: if 🔄 REVISE, reviewer specifies items → user starts new `/tfw-handoff` session for fixes

### Step 2: Create `.agent/workflows/tfw-review.md`

Byte-identical copy of `.tfw/workflows/review.md`. Same YAML frontmatter — Antigravity picks up the `description` field for `/tfw-review` slash command.

### Step 3: Modify `.tfw/workflows/handoff.md`

Four changes:

**3a. Update header and role lock block (lines 1-15):**
- Line 2: `description` → remove "coordinator review": `TFW Handoff — executor onboarding, implementation, RF`
- Line 7: Remove "→ Coordinator (reviews)" → `Roles: Coordinator (hands off) → Executor (receives, questions, implements)`
- Line 9: Output → `RF file with implementation results`
- Lines 11-15: Remove Phase 4 references. Only: `🔒 ROLE LOCK: EXECUTOR` with ONB/RF permitted, HL/TS/REVIEW forbidden

**3b. Replace Phase 4 (lines 99-140) with STOP block:**

```markdown
## 🛑 Executor STOP

> **Your work is done.** Do NOT proceed to review.
> Inform the user: "RF is complete. Start `/tfw-review` to review the results."
> Writing a REVIEW file as executor is a **🔒 Role Lock violation**.
```

**3c. Update Multi-Phase diagram (lines 142-161):**
- Remove "Coordinator: reviews → REVIEW" lines from each phase
- Add note: "After each Phase RF, run `/tfw-review` for review"
- Update diagram to show handoff ending at RF, review as separate step

**3d. Update Anti-patterns (lines 163-178):**
- Remove "Coordinator skips review" (that's now the reviewer's responsibility in review.md)
- Add: "Executor writes REVIEW file — **🔒 Role Lock violation**"
- Add: "Executor continues past Phase 3 — must STOP after RF"
- Update final line to include REVIEW in the lock: "Executor MUST NOT write HL, TS, REVIEW, or change scope"

### Step 4: Modify `.agent/workflows/tfw-handoff.md`

Apply identical edits as Step 3. This is the Antigravity adapter copy — must stay byte-identical to canonical `handoff.md`.

### Step 5: Modify `.tfw/conventions.md`

**5a. §8 Workflows table (lines 138-146):**
- Change handoff.md role: `Executor + Coordinator` → `Executor`
- Change handoff.md purpose: `Context load → ONB → execute → RF → REVIEW` → `Context load → ONB → execute → RF`
- Add new row: `| [review.md](workflows/review.md) | Reviewer | Read RF → checklist → verdict → tech debt → traces |`

**5b. §14 Anti-patterns (around line 195):**
- Add: `- Executor writes REVIEW file → **Role Lock violation**`

**5c. §15 Role Lock table (lines 202-209):**
- Remove `handoff.md (Phase 4) | Coordinator | REVIEW | —` row (line 206)
- Add new row: `| review.md | Reviewer | REVIEW | ONB, RF, HL, TS, code |`
- **Delete** line 209: `**REVIEW** files can be written by any role.`

**5d. §15 Hard Stop Rule (lines 211-217):**
- Add a second hard stop for Executor after the existing coordinator one:
  ```
  When an Executor finishes RF, the correct action is:
  1. Inform the user that execution is complete
  2. Instruct: "Start `/tfw-review` to review the results"
  3. **Do NOT write a REVIEW file**
  ```

### Step 6: Modify `.tfw/glossary.md`

**6a. Update Workflow definition (line 63):**
- Remove "Three canonical workflows" — replace with: "Canonical workflows in `.tfw/workflows/`: plan (HL→TS), handoff (ONB→execute→RF), review (RF→checklist→REVIEW), resume (status matrix→next phase)..."

**6b. Add Reviewer role (after Executor, around line 93):**

```markdown
### Reviewer (AI — coordinator in review mode)
- Reads RF and TS (for DoD verification)
- Writes REVIEW file with 9-point checklist
- Triages executor Observations → TECH_DEBT.md
- Updates Task Board status
- Cannot: write code, write ONB, write RF, modify HL/TS
```

**6c. Update Coordinator role (lines 79-84):**
- Remove "Reviews executor's RF output" and "Writes REVIEW files" — these move to Reviewer
- Keep: "Writes HL and TS", "Manages Task Board in README", "Triages executor observations to TECH_DEBT.md"

### Step 7: Modify `AGENTS.md`

**7a. Workflow list (lines 29-32):**
- Update handoff line: `handoff.md` — execution (ONB → develop → RF)` (remove "→ REVIEW")
- Add: `- `review.md` — task review (RF → checklist → REVIEW → traces)`

### Step 8: Modify `.tfw/CHANGELOG.md`

**8a. Under `[Unreleased]` section (line 6):**

```markdown
## [Unreleased]
### Added
- `review.md` workflow — standalone review process with `🔒 ROLE LOCK: REVIEWER`
- Reviewer role — coordinator in review-locked mode (glossary, conventions)
### Changed
- `handoff.md` — removed Phase 4 (review), added executor STOP block
- `conventions.md` — Role Lock table updated, "any role" for REVIEW removed
### Removed
- Review phase from `handoff.md` (moved to `review.md`)
```

## 5. Detailed Steps — Phase B

### Step 9: Modify `.tfw/README.md`

**9a. Directory tree (around L77):**
- Add `review` to the workflows list: `workflows/     # Canonical workflows (plan, handoff, review, resume, docs, release, update)`

**9b. Workflows table (around L168):**
- Change handoff role: `Executor + Coordinator` → `Executor`
- Change handoff purpose: remove `→ REVIEW`
- Add row: `| **review** | Reviewer | Read RF → checklist → verdict → tech debt → traces |`

**9c. Evolution section (around L281):**
- Update "3 canonical workflows" — change count and add review to list

### Step 10: Modify `.tfw/workflows/plan.md`

**10a. Role Lock block (L14):**
- After "instruct the user to start a `/tfw-handoff` session" — no change needed here (this is about planning, not review)

**10b. Small task path (L76):**
- After "Start execution with `/tfw-handoff`" add: "After RF, run `/tfw-review` to review results."

**10c. Multi-phase pattern (L106-116):**
- Update the pattern to show review as separate step after each phase RF

### Step 11: Modify `.tfw/workflows/resume.md`

**11a. Handoff reference (L83):**
- After the handoff reference, add: "After RF, run `/tfw-review` to review results."

### Step 12: Modify `.tfw/init.md`

**12a. Adapter copy instructions (L97):**
- Add: `cp .tfw/workflows/review.md .agent/workflows/tfw-review.md`

**12b. Workflow references (L184, L192):**
- Add `review` to workflow lists: "(plan, handoff, review, resume)"

### Step 13: Modify `.tfw/adapters/antigravity/README.md`

**13a. Copy instructions (L21):**
- Add: `cp .tfw/workflows/review.md .agent/workflows/tfw-review.md`

**13b. Directory listing (L39):**
- Add: `├── tfw-review.md           # TFW review (from step 2)`

**13c. Sync section (L51):**
- Add: `cp .tfw/workflows/review.md .agent/workflows/tfw-review.md`

## 6. Acceptance Criteria

- [ ] `.tfw/workflows/review.md` exists with `🔒 ROLE LOCK: REVIEWER`, 9-point checklist, tech debt collection, verdict+traces
- [ ] `.agent/workflows/tfw-review.md` is byte-identical to `.tfw/workflows/review.md`
- [ ] `handoff.md` has no Phase 4; ends with `🛑 Executor STOP` block; role lock says Executor only
- [ ] `.agent/workflows/tfw-handoff.md` matches canonical `handoff.md`
- [ ] `conventions.md` §8 has review.md row; §15 Role Lock table has Reviewer row; "any role" line deleted
- [ ] `glossary.md` has Reviewer role definition; Coordinator no longer lists review duties
- [ ] `AGENTS.md` lists review.md workflow
- [ ] `CHANGELOG.md` has review workflow entry in `[Unreleased]`
- [ ] `.tfw/README.md` directory tree, workflows table, and evolution updated
- [ ] `plan.md` mentions `/tfw-review` after handoff
- [ ] `resume.md` mentions review step
- [ ] `init.md` has review workflow in copy instructions and workflow lists
- [ ] Antigravity adapter README has review in setup instructions
- [ ] `grep -r "Phase 4" .tfw/workflows/handoff.md` returns 0 results
- [ ] `grep "any role" .tfw/conventions.md` returns 0 results

## 7. Risks

| Risk | Mitigation |
|------|------------|
| Executor still sees review instructions via cached context | The canonical `handoff.md` is the source — once Phase 4 is removed, new sessions won't have it |
| Existing REVIEW files in TFW-6/TFW-7 reference "Coordinator (AI)" as author | Historical — no retroactive change needed. New reviews will say "Reviewer" |
| TD-10/TD-11 ("Three canonical workflows") need updating | Step 6a addresses this — the Workflow glossary definition gets updated |
| Phase B scope may uncover more references | Grep scan covered all `.tfw/` files — unlikely to find more |

---

*TS — TFW-8: Reviewer Role and Workflow | 2026-03-12*
