# TS — TFW-50: Prompt-First Session and Commit Identity

> **Date**: 2026-08-01
> **Author**: Coordinator (Codex)
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-50](HL-TFW-50__prompt_first_commit_identity.md)
> **Research decision**: No new research. The owner-approved correction resolves the
> product choice; implementation must remove the rejected mechanism, not compare new
> enforcement alternatives.
> **Publication boundary**: Local work only. No push, remote tag, deploy, publish,
> notify, or host escalation is authorized.

---

## 1. Objective

Replace TFW-49's rejected commit-identity software subsystem with a small prompt-led
convention. Agents receive a readable session and commit format, its purpose, and the
instruction to use explicit workflow context. The existing Python, schema, state,
router, hook, ledger, and range-audit machinery is removed completely without erasing
the TFW-49 failure trace.

## 2. Scope

### In Scope

- Keep exactly these human-readable forms:

  ```text
  Session: <Role> | <Task-ID> | <work>
  Commit:  [<surface>/<task>/<work>/<role>] <summary>
  ```

- Give the format and purpose one concise semantic owner in conventions, one glossary
  reference, and short point-of-use cues in the four adapter templates and three
  installed entry prompts.
- Delete the twelve TFW-49 runtime/schema/state/hook files without replacement.
- Remove obsolete runtime/router/hook/range-audit instructions from six canonical
  workflows and synchronize their twelve Claude/Antigravity copies.
- Unset this repository's local `core.hooksPath` and remove the private TFW runtime
  ledger. Verify the already-absent user-global override as a boolean only; do not read
  or disclose any external path or hook content.
- Preserve TFW-49 task artifacts and commits as rejected historical evidence.
- Demonstrate the prompt-only contract through actual Executor and independent
  Reviewer session/commit naming plus source, parity, and documentation checks.

### Out of Scope

- Any replacement executable, validator, schema, registry, state, manifest, hook,
  generated prompt system, audit service, or installation lifecycle.
- Actor authentication, Git authorship claims, hosted identity, CI enforcement, or
  support matrices for Git clients and platforms.
- Rewriting, squashing, deleting, or relabeling TFW-49 commits.
- Editing KNOWLEDGE, topic knowledge, or knowledge state before the post-review
  `/tfw-docs` and `/tfw-knowledge` decisions.
- Push, remote tags, release publication, deploy, notify, or other remote mutation.
- Inspecting or changing system Git configuration or reading external/global hook
  paths, files, bodies, fingerprints, values, or secrets.

## 3. Principles Check

| # | Principle (HL §7) | Enforced by | Gate |
|---|------------------|-------------|------|
| P1 | Methodology, not software | AC-1, AC-3 | Prompt contract exists; rejected programs and owners do not |
| P2 | Delete before adding | AC-3 | Twelve files removed, zero replacement framework files |
| P3 | Naming creates behavior | AC-1, AC-2, AC-6 | Format, purpose, and actual agent use are observable |
| P4 | One semantic owner | AC-1, AC-2, AC-5 | Conventions owns meaning; other locations remain short cues |
| P5 | Purpose before enforcement | AC-1, AC-3 | Searchability is stated; enforcement machinery is absent |
| P6 | Agents use explicit context | AC-1, AC-2, AC-6 | Prompt says never infer missing task/work/role/surface values |
| P7 | Failure remains a trace | AC-8 | TFW-49 history remains rejected and intact |
| P8 | Independent judgment remains | AC-6, AC-7 | Reviewer inspects real prompt-only behavior and documentation |

## 4. Affected Files

### Delete — rejected mechanism

| File | Action | Description |
|------|--------|-------------|
| `.tfw/commit_identity.schema.json` | DELETE | Remove accepted-value/schema registry |
| `.tfw/commit_identity_state.json` | DELETE | Remove project activation state |
| `.tfw/templates/commit_identity_state.json` | DELETE | Remove state template |
| `.tfw/scripts/commit_identity.py` | DELETE | Remove validator and range auditor |
| `.tfw/scripts/commit_identity_router.py` | DELETE | Remove operation router |
| `.tfw/scripts/commit_identity_hooks.py` | DELETE | Remove hook lifecycle runtime |
| `.tfw/scripts/test_commit_identity.py` | DELETE | Remove rejected validator tests |
| `.tfw/scripts/test_commit_identity_router.py` | DELETE | Remove rejected router tests |
| `.tfw/scripts/test_commit_identity_hooks.py` | DELETE | Remove rejected hook tests |
| `.tfw/hooks/runtime.json` | DELETE | Remove hook manifest |
| `.tfw/hooks/prepare-commit-msg` | DELETE | Remove repository hook |
| `.tfw/hooks/commit-msg` | DELETE | Remove repository hook |

### Modify — concise owners and prompt consumers

| File | Action | Description |
|------|--------|-------------|
| `.tfw/conventions.md` | MODIFY | Replace the long subsystem contract with the concise prompt convention |
| `.tfw/glossary.md` | MODIFY | Keep one short Commit Identity definition; remove obsolete runtime terms |
| `.tfw/adapters/codex/AGENTS.md.template` | MODIFY | Add the Codex point-of-use naming cue; remove script routing |
| `.tfw/adapters/claude-code/CLAUDE.md.template` | MODIFY | Add the Claude cue; remove script routing |
| `.tfw/adapters/antigravity/tfw-rules.md.template` | MODIFY | Add the Antigravity cue; remove script routing |
| `.tfw/adapters/cursor/tfw.mdc.template` | MODIFY | Add the Cursor cue; remove script routing |
| `AGENTS.md` | MODIFY | Install the concise Codex prompt cue |
| `CLAUDE.md` | MODIFY | Install the concise Claude prompt cue |
| `.agent/rules/tfw.md` | MODIFY | Install the concise Antigravity prompt cue |
| `.tfw/workflows/docs.md` | MODIFY | Remove router/audit dependency; keep short local-commit cue |
| `.tfw/workflows/handoff.md` | MODIFY | Remove router/audit dependency; keep short local-commit cue |
| `.tfw/workflows/init.md` | MODIFY | Remove schema/state/hook installation lifecycle |
| `.tfw/workflows/release.md` | MODIFY | Remove runtime/audit dependency; preserve publication authority |
| `.tfw/workflows/review.md` | MODIFY | Remove runtime/audit dependency; retain independent judgment |
| `.tfw/workflows/update.md` | MODIFY | Remove schema/state/hook repair lifecycle |
| `.agent/workflows/tfw-docs.md` | MODIFY | Exact Antigravity copy of canonical docs workflow |
| `.agent/workflows/tfw-handoff.md` | MODIFY | Exact Antigravity copy of canonical handoff workflow |
| `.agent/workflows/tfw-init.md` | MODIFY | Exact Antigravity copy of canonical init workflow |
| `.agent/workflows/tfw-release.md` | MODIFY | Exact Antigravity copy of canonical release workflow |
| `.agent/workflows/tfw-review.md` | MODIFY | Exact Antigravity copy of canonical review workflow |
| `.agent/workflows/tfw-update.md` | MODIFY | Exact Antigravity copy of canonical update workflow |
| `.claude/commands/tfw-docs.md` | MODIFY | Exact Claude copy of canonical docs workflow |
| `.claude/commands/tfw-handoff.md` | MODIFY | Exact Claude copy of canonical handoff workflow |
| `.claude/commands/tfw-init.md` | MODIFY | Exact Claude copy of canonical init workflow |
| `.claude/commands/tfw-release.md` | MODIFY | Exact Claude copy of canonical release workflow |
| `.claude/commands/tfw-review.md` | MODIFY | Exact Claude copy of canonical review workflow |
| `.claude/commands/tfw-update.md` | MODIFY | Exact Claude copy of canonical update workflow |

Executor lifecycle artifacts (ONB, EV, RF) and the TFW-50 README row are additional
task traces, not framework consumers.

**Scope-attention measurement:** physical tracked paths and changed lines, with
deletions counted rather than reclassified: 39 framework files, 0 new framework files,
27 modified files, 12 deleted files, and an estimated 6,100–6,700 changed LOC including
exactly 5,910 existing runtime lines removed. Current configured signals: 14 files,
8 new files, 1,200 LOC, 12 modified files.

**Response:** bounded cohesive override. The signals are crossed because one rejected
owner system exists in twelve files and is referenced by twenty-seven prompt/workflow
consumers, including twelve required derived copies. Splitting deletion from reference
cleanup or prompt replacement would leave a broken or competing contract. No file is
added to the framework, and the result must be materially net-negative.

## 5. Acceptance Criteria

### AC-1: One concise prompt-owned naming contract

Conventions owns the exact session and commit forms, their searchable/resumable
purpose, the explicit-context rule, and the non-authentication/non-publication boundary.

- **Intent / authority:** User correction; HL principles P1, P3–P6; D28 and D55.
- **Claim:** A reader can find one concise semantic owner and understand what to write,
  why it matters, and what it does not prove or authorize.
- **Boundary:** Local conventions owner and glossary reference.
- **Precision:** The two approved forms are acceptance-critical. Explanatory wording
  may vary only if it preserves purpose, explicit context, and boundaries.
- **Proof intent:** Local source proof plus link resolution from glossary to owner.
- [ ] The owner contains exactly the approved session and commit forms and one valid
  Codex/TFW-50 example.
- [ ] Missing surface/task/work/role values must be resolved from current workflow
  context, never inferred from branch, history, model, path, or prior subject.
- [ ] The glossary links to the owner and does not recreate schema/state/runtime terms.

Gate: Inspect the owner/reference relation and scan for competing normative definitions.

Evidence: N/A — this is a local documentation/source relation, not a live-environment
observation.

### AC-2: Every supported adapter can discover the cue [depends: AC-1]

The four adapter templates and three installed prompt entries carry the same concise
point-of-use instruction without script calls or a copied long contract.

- **Intent / authority:** User asked for the format in agent prompts; HL DoD 2.
- **Claim:** Codex, Claude Code, Antigravity, and Cursor templates expose the naming
  instruction, and installed Codex/Claude/Antigravity entries match their surface.
- **Boundary:** Four template sources crossed to three installed copies; Cursor has no
  installed entry in this repository.
- **Precision:** Each cue must include both forms or an immediately resolvable owner
  link, purpose, explicit-context rule, and no-push boundary in compact form.
- **Proof intent:** Local proof per template; Seam Proof between each installed entry
  and its template/source meaning.
- [ ] Seven prompt consumers are correct for their registered surface and contain no
  commit-identity Python/router/hook instruction.
- [ ] No adapter acquires a new runtime, wrapper, generated prompt, or skill owner.

Gate: Seven-file semantic matrix and script/runtime reference scan.

Evidence: N/A — structural prompt availability is proven from repository sources.

### AC-3: Rejected machinery is completely removed [depends: AC-1]

All twelve TFW-49 runtime files disappear and no functional equivalent replaces them.

- **Intent / authority:** Explicit user rejection of TFW-49 as a complete product-fit
  failure; HL P1–P2 and DoF 1–2.
- **Claim:** The framework contains no commit-identity Python, tests, schema, state,
  hook manifest, or hook launcher.
- **Boundary:** Twelve tracked files plus the complete framework tree.
- **Precision:** Exact file absence and functional-equivalent absence are
  acceptance-critical; deletion method is adaptable.
- **Proof intent:** Local file inventory, reference scan, and net-negative diff proof.
- [ ] All twelve listed paths are absent.
- [ ] No replacement executable, schema, registry, state, hook, validator, audit, or
  generated enforcement layer exists elsewhere.
- [ ] The framework diff is net-negative and reports actual insertions/deletions.

Gate: Exact deleted-path check plus repository-wide semantic scan for rejected owners.

Evidence: N/A — tracked source absence and diff are local proof.

### AC-4: Git hook state is removed safely [depends: AC-3]

This repository stops using TFW hooks and the private runtime ledger is removed,
without inspecting or modifying external/system hook material.

- **Intent / authority:** User explicitly asked to disable the hooks; HL DoD 4.
- **Claim:** Local `core.hooksPath` is unset, the private TFW ledger is absent, and the
  already-completed user-global unset remains absent.
- **Boundary:** Current repository Git-local config, `.git/tfw/` ledger, and a redacted
  boolean check of user-global override absence.
- **Precision:** Exact local unset and ledger absence are critical. External/system
  path/value/body inspection is prohibited.
- **Proof intent:** Local Proof plus Live Proof from the current repository's observed
  Git configuration; unavailable redacted global confirmation becomes Value Debt.
- [ ] `git config --local --get-all core.hooksPath` returns no value.
- [ ] `.git/tfw/commit_identity_runtime.json` is absent.
- [ ] Verification records only whether user-global `core.hooksPath` is absent; it
  never prints a value or reads any external hook path/content.

Gate: Secret-safe boolean checks of current-repository state; any external inspection
or disclosed value fails the phase.

Evidence: Minimal — record tool/version, current repository, local unset result,
ledger absence, and redacted global absence result.

### AC-5: Workflows no longer depend on the subsystem [depends: AC-3]

The six canonical workflows contain only behavior they still own, and their twelve
Claude/Antigravity copies stay exact.

- **Intent / authority:** One-owner/local-cue principle and deletion seam integrity.
- **Claim:** docs/handoff/release use a concise prompt-led local-commit cue;
  init/update contain no identity installation or repair lifecycle; review retains
  independent claim/risk judgment without mechanical identity audit.
- **Boundary:** Six canonical owners crossed to twelve exact derived copies.
- **Precision:** Canonical/derived equality and absence of runtime/router/range-audit
  dependencies are critical. Editorial compression is adaptable.
- **Proof intent:** Local proof for each canonical workflow and Seam Proof for 12 copies.
- [ ] Six canonical workflows contain no dead references or replacement mechanism.
- [ ] Each of the twelve derived copies is byte-exact with its canonical workflow.
- [ ] Role, destructive, irreversible, and publication gates remain locally complete.

Gate: Reference scan, canonical/copy hashes, and boundary-preservation inspection.

Evidence: N/A — repository source equality and semantics are local/seam proof.

### AC-6: Prompt-only behavior is demonstrated [depends: AC-2, AC-4, AC-5]

The task's Executor and independent Reviewer operate without hooks or the deleted
programs while producing understandable session and local commit names.

- **Intent / authority:** User selected agent understanding over mechanical
  enforcement; HL P8 requires independent judgment.
- **Claim:** The actual Executor and Reviewer sessions use
  `<Role> | TFW-50 | <work>`, and their local commit subjects begin with the approved
  four-field prefix from explicit context.
- **Boundary:** Executor and independent Reviewer roles, current repository history,
  and the prompt consumers they received.
- **Precision:** Actual session names, local subjects, absence of hook/script use, and
  no-push state are acceptance-critical. Summary text is adaptable.
- **Proof intent:** Live Proof from the two independent sessions and local commit
  objects; actor authentication is explicitly not claimed.
- [ ] Executor records its session name and local implementation commit subject.
- [ ] Reviewer independently records its session name and local review commit subject.
- [ ] Neither role invokes commit-identity Python/hooks; neither pushes.

Gate: RF/REVIEW attestation plus local Git inspection after hooks are removed.

Evidence: Minimal — record the two session names, local commit hashes/subjects, absence
of hook/script invocation, and unchanged remote reference.

### AC-7: Documentation remains coherent [depends: AC-1, AC-2, AC-5]

The net-negative change leaves generated documentation and references usable.

- **Intent / authority:** Deletion must not trade simplicity for broken navigation.
- **Claim:** Documentation tests and the bounded MkDocs build pass; changed pages have
  no broken owned links or materially unreadable rendering.
- **Boundary:** Changed Markdown sources crossed to generated documentation.
- **Precision:** Existing test commands, link resolution for changed owners, and build
  success are critical; browser tooling is adaptable if rendering can be inspected.
- **Proof intent:** Local tests plus Seam Proof between source and generated pages.
- [ ] `python -m pytest docs/scripts/test_gen_docs.py docs/scripts/test_integration.py`
  passes.
- [ ] `python -m mkdocs build --config-file docs/mkdocs.yml` succeeds; existing TD-125
  warnings are separated from any TFW-50-added warning.
- [ ] Changed owner/prompt links and headings resolve in source and rendered output.

Gate: Reproducible tests/build and changed-link/render inspection.

Evidence: Minimal — record environment, commands, results, warning attribution, and
rendered changed-owner inspection.

### AC-8: Failure history and closure boundaries remain honest [depends: AC-3]

TFW-49 stays rejected and inspectable while TFW-50 owns only the corrective result.

- **Intent / authority:** User chose acknowledgement over destructive history rewrite;
  F26 keeps publication separately authorized.
- **Claim:** No TFW-49 task artifact or commit is rewritten/deleted, no knowledge
  architecture is silently edited before review, and no remote state changes.
- **Boundary:** TFW-49 trace/history, TFW-50 lifecycle, knowledge owners, and remote.
- **Precision:** Preserved commit ancestry, rejected Task Board status, protected
  knowledge files, and unchanged `origin/master` are critical.
- **Proof intent:** Local ancestry/diff proof and Live Proof of unchanged remote-tracking
  reference; later D58–D60 supersession is due at `/tfw-docs` after APPROVE review.
- [ ] TFW-49 remains `❌ REJECTED` and its task files/history remain present.
- [ ] KNOWLEDGE/topic/state files are unchanged during implementation/review.
- [ ] No push, remote tag, deploy, publish, notify, or host escalation occurs.

Gate: Protected-path diff, ancestry check, and before/after local remote-reference hash.

Evidence: Minimal — record protected diff, local ancestry, and unchanged
`origin/master` value without network publication.

### Evidence Artifacts

| File | Description |
|------|-------------|
| `evidence/EV__TFW-50__prompt_first_commit_identity.md` | Required EV index with stable Proof Records, per-AC Evidence rows, verdict, and any Value Debt |

## 6. Technical Guidance

- Prefer deletion and direct Markdown edits. Do not preserve rejected code for
  compatibility or create a replacement helper.
- A compact adapter cue may say: “Name the session `Role | Task-ID | work`; start each
  local commit `[surface/task/work/role] summary`, using explicit current workflow
  context so traces are recognizable; this never authorizes push.” Conventions remains
  the semantic owner; wording may be compressed without losing these meanings.
- Remove the repository-local override with Git's local-config operation and verify
  absence. Delete only the known private ledger path. Do not enumerate, resolve, print,
  read, copy, fingerprint, run, or mutate external/global hook material.
- Make the first implementation commit after local hook removal directly from the
  prompt contract. Do not call the deleted router or bypass a still-active hook with a
  hidden fallback.
- Keep the six canonical workflows authoritative, then mechanically synchronize only
  their named Claude/Antigravity copies.
- Existing TFW-49 task artifacts and commits are evidence, not cleanup targets.
- If an unexpected consumer genuinely depends on the rejected runtime, stop and return
  to the Coordinator; do not silently expand scope or retain a compatibility layer.

## 7. Definition of Failure

- ❌ Any listed runtime/schema/state/hook file, private ledger, local hook override, or
  functional equivalent remains.
- ❌ A new executable, validator, registry, audit layer, generated prompt mechanism,
  hook lifecycle, or compatibility shim is introduced.
- ❌ The naming purpose or explicit-context rule is lost, or a supported adapter cannot
  discover the cue.
- ❌ A workflow/template/glossary becomes a second long semantic owner.
- ❌ Any task/work/role/surface value is inferred from branch, history, model, session,
  path, or prior commit rather than explicit workflow context.
- ❌ Prompt naming is described as authentication, Proof, acceptance, or publication
  authority.
- ❌ Canonical/derived workflow copies drift, or role/safety/irreversible/publication
  gates are weakened during compression.
- ❌ TFW-49 history is rewritten/deleted, protected knowledge is changed before its
  workflow, or any push/remote mutation occurs.
- ❌ The final framework diff is not materially net-negative or exceeds this exact
  scope without a Coordinator-approved revision.

## 8. Risks

| Risk | Mitigation |
|------|------------|
| A dead script/hook reference remains | Exact repository-wide reference scan and no compatibility layer |
| The prompt grows into another contract | One owner, one example, compact cues, independent review |
| Adapter or derived-copy drift | Explicit seven-consumer matrix and twelve byte-equality checks |
| Local hook removal exposes external behavior | User-global override already absent; never inspect external/system material |
| Deletion weakens role or publication safety | Preserve full local imperatives at those irreversible boundaries |
| Agents occasionally mistype the convention | Correct the prompt/behavior through review; do not rebuild enforcement software |
| Concurrent unrelated local work contaminates the diff | Exact path/protected-state checks; preserve unrelated worktree changes |

---

*TS — TFW-50: Prompt-First Session and Commit Identity | 2026-08-01*
