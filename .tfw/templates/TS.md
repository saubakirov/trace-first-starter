# TS — {PREFIX}-{N} / Phase {X}: {Title}

> **Date**: YYYY-MM-DD
> **Author**: {author}
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-{PREFIX}-{N}](path-to-HL)

---

## 1. Objective
{One paragraph: what this phase delivers and why it matters.}

## 2. Scope

### In Scope
- {what will be done}

### Out of Scope
- {what will NOT be done in this phase}

## 3. Principles Check

> Map HL §7 principles to specific AC items. Each principle MUST have at least one AC enforcing it.
> If a principle has no applicable AC — mark as "N/A" with reason.

| # | Principle (from HL §7) | Enforced by | Gate |
|---|----------------------|-------------|------|
| P1 | {principle name} | AC-{N} | {how verified} |
| P2 | {principle name} | N/A | {reason not applicable} |

## 4. Affected Files

| File | Action | Description |
|------|--------|------------|
| `path/to/file` | CREATE / MODIFY / DELETE | {description} |

**Scope-attention measurement:** {counting method}; {N} total affected files,
{A} new files, {M} modified files, estimated {L} changed LOC. Current configured
signals: {max_files} files, {max_new} new files, {max_loc} LOC,
{max_modified} modified files.

**Response:** {Below signals — cohesion still checked / Simplified / Unrelated work
removed / Coherent value-boundary split / Bounded override with rationale / Returned
to Coordinator-user}. These measurements are transitional attention signals, not
quality, completion, or automatic-split criteria. A split must preserve the product
outcome, every crossed seam, and any triggered Value Debt.

## 5. Acceptance Criteria

> Describe WHAT the result should achieve, not HOW to implement it.
> Each AC must be independently verifiable. Mark dependencies with `[depends: AC-X]`.
> Executor verifies dependent ACs in order — a dependent AC cannot pass before its prerequisite.
>
> **Compact Requirement Claim:** Each material AC relates:
> - **Intent / authority** — product purpose, applicable Project Value, human
>   requirement/correction, cited authority, or explicit task-local source.
> - **Claim** — observable outcome the task is authorized to assert.
> - **Boundary** — local, plus every crossed source, interface, role, package, phase,
>   stakeholder, live environment, or irreversible event.
> - **Precision** — acceptance-critical identifiers/source relations/checks/outcomes
>   versus adaptable Technical Guidance. Use `N/A — {reason}` when no precision
>   decision is triggered.
> - **Proof intent** — Local Proof for every claimed deliverable; additive Seam/Live
>   Proof for every crossed/live boundary; unavailable triggered proof becomes Value
>   Debt.
>
> The fields may be compact or grouped when every claim and boundary remains
> resolvable. Do not duplicate HL narrative, prescribe implementation, require uniform
> row volume, leave blank boilerplate, or invent a value.
>
> **Gate** names the claim or failure protected by a synthetic, structural, source, or
> other local check. Code tests/builds are conditional examples, not universal gates.
>
> **Evidence** means intended-environment observation, not every kind of proof. Grammar:
> full spec, minimal spec, `N/A — {claim-based reason}`, `DEFERRED — {named future
> event; complete Value Debt required}`, or an explicit Executor decision boundary.
> Executor MAY change adaptable tools with RF rationale, but not acceptance-critical
> precision or triggered proof.

### AC-1: {title}
{What the result should achieve — 1-2 sentences.}
- **Intent / authority:** {why this outcome is required and who/what authorizes it}
- **Claim:** {observable outcome authorized for attestation}
- **Boundary:** {Local; add crossed source/interface/role/package/phase/stakeholder/live/irreversible boundaries}
- **Precision:** {acceptance-critical identifiers, source relations, checks, or outcomes / N/A with reason; adaptable choices belong in §6}
- **Proof intent:** {Local Proof; additive Seam/Live Proof; Value Debt route if a triggered proof cannot yet exist}
- [ ] {Verifiable criterion}
- [ ] {Verifiable criterion}

Gate: {What claim/failure is protected and how to check it — command, query, source comparison, render, inspection, or stakeholder confirmation}

Evidence: {What to observe in the intended environment — or N/A/DEFERRED with claim-based reason}

### AC-2: {title}  [depends: AC-1]
{What the result should achieve — 1-2 sentences.}
- **Intent / authority:** {source}
- **Claim:** {observable outcome}
- **Boundary:** {Local plus every crossed boundary}
- **Precision:** {acceptance-critical / adaptable / N/A with reason}
- **Proof intent:** {triggered Local/Seam/Live Proof or Value Debt}
- [ ] {Verifiable criterion}

Gate: {Protected claim/failure and verification method}

Evidence: {Intended-environment observation — or N/A/DEFERRED with reason}

### Evidence Artifacts

> List expected evidence files. Minimum: one EV file (always required).
> Additional binary artifacts (screenshots, API responses, logs) if applicable.

| File | Description |
|------|-------------|
| `evidence/EV__{PREFIX}-{N}__{title}.md` | Existing mandatory EV index: stable Proof Records, environment, per-AC Evidence rows, verdict, Value Debt, attachments _(required)_ |
| `evidence/{additional_file}` | {description} _(if applicable)_ |

## 6. Technical Guidance

> Reference material, not instructions. Executor MAY deviate with justification in RF.
- {Relevant context: where things are, what patterns exist, what constraints apply}

## 7. Definition of Failure

- ❌ {Condition that causes RF rejection — hard reject, not a warning}

## 8. Phase Risks

| Risk | Mitigation |
|------|------------|
| {risk} | {mitigation} |

## 9. Cross-Phase Modifications (multi-phase only)

> Include only for multi-phase tasks. Omit section entirely for single-phase tasks.

| File | Also modified in | Coordination note |
|------|-----------------|-------------------|
| `path/to/file` | Phase {X} | {what to watch for} |

> **Cross-references**: use Reference Format (e.g. `RF TFW-18`, `D24`, `TD-72`). See compilable_contract.md §2. Build script resolves to hyperlinks.

---

*TS — {PREFIX}-{N} / Phase {X}: {Title} | YYYY-MM-DD*
