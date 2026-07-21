# ONB — TFW-47 / Phase B: Codex Adapter + Framework Integration

> **Date**: 2026-07-21
> **Author**: Executor (Codex)
> **Status**: ✅ ONB — amendment resolved, execution resumed
> **Parent HL**: [HL-TFW-47](../HL-TFW-47__codex_adapter_shortcut_skills.md)
> **TS**: [TS Phase B](TS__phase-b__codex_adapter.md)

---

## 1. Understanding

Phase B must add Codex as a first-class TFW adapter without duplicating canonical workflow logic. The framework-owned source will live under `.tfw/adapters/codex/`; 11 individually authored shortcut skills will be installed as exact copies under `.agents/skills/tfw-*/SKILL.md`; public docs, adapter docs, init/update workflows, and the glossary will describe the installation and invocation contract truthfully. Completion requires a new Codex session to discover the installed skills and record the result in the mandatory phase evidence file.

## 2. Entry Points

- `tasks/TFW-47__codex_adapter_shortcut_skills/HL-TFW-47__codex_adapter_shortcut_skills.md`
- `tasks/TFW-47__codex_adapter_shortcut_skills/phase-b/HL__phase-b__codex_adapter.md`
- `tasks/TFW-47__codex_adapter_shortcut_skills/phase-b/TS__phase-b__codex_adapter.md`
- `tasks/TFW-47__codex_adapter_shortcut_skills/research/iter2/RES.md` and its four stage files
- `tasks/TFW-47__codex_adapter_shortcut_skills/phase-a/RF__phase-a__evidence_enforcement.md`
- `.tfw/adapters/`, `.tfw/workflows/{init,update}.md`, `.tfw/glossary.md`, `README.md`
- `D:/projects/research/ai-first-devices/.agents/skills/tfw-*/SKILL.md` as the validated reference implementation
- `.agents/skills/source-command-tfw-*/SKILL.md` as existing project-local skill content that must be preserved

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Answer |
|---|----------|--------|
| 1 | The repository is on `master` at `7fbdf3b`, but all TFW-47 planning/Phase A artifacts, the Phase A framework changes, and the existing `.agents/skills/source-command-tfw-*` tree are still modified or untracked. The handoff workflow requires committing and pushing ONB before execution. Should the current working tree be treated as the approved baseline and included in a checkpoint commit, or should Phase A be committed separately before Phase B continues? | **Commit Phase A separately.** Make a checkpoint commit with all Phase A artifacts (task files, framework changes to conventions.md, templates, handoff.md, KNOWLEDGE.md D53) + existing `source-command-tfw-*` skills + planning artifacts (HL, research, iterations.yaml). This gives Phase B a clean baseline. Commit message suggestion: `TFW-47/A: evidence enforcement — mandatory evidence/ folder, EV template, D16 revoked`. Then proceed with Phase B execution on top of that commit. |

## 4. Recommendations (suggestions, not blocking)

1. Treat `.tfw/adapters/codex/skills/` as canonical adapter source and `.agents/skills/tfw-*/` as replaceable installed copies. Verify equality mechanically; do not introduce a generator or per-project divergence. — **✅ Confirmed. Matches TS AC-3 intent exactly.**
2. Use the AFD handwritten contracts as a reference, but align every role lock, permitted artifact, and hard stop with the current local workflow files. Do not copy AFD's extra `agents/openai.yaml` files because they are outside the approved TS. — **✅ Confirmed. YAML agent files are out of scope. Align contracts with local `.tfw/workflows/*.md`, not AFD verbatim.**
3. Document that skill discovery occurs at session start. AC-7 should be verified in a fresh Codex session after installation, not inferred from the current session. — **✅ Confirmed. Fresh session is the only valid evidence for AC-7.**
4. Preserve the existing `source-command-tfw-*` skills. Their removal or rename is outside Phase B; any duplicate menu affordance should be reported in RF observations. — **✅ Confirmed. Do not touch `source-command-tfw-*`. Report duplication in RF §6 Observations.**

## 5. Risks Found (edge cases, potential issues not in TS)

1. The active session loaded its `tfw-handoff` shortcut from the user-level Codex skill directory, not from the yet-to-be-created repository-local adapter. It cannot serve as evidence for AC-7. — **Coordinator: Acknowledged. Current session evidence is invalid for AC-7.**
2. Codex does not hot-reload project skills in an active session. If a fresh-session run cannot be captured from this environment, AC-7 must be marked DEFERRED with the exact blocker rather than claimed VERIFIED. — **Coordinator: Accepted. DEFERRED with honest blocker is correct per D53/§12. User will verify AC-7 manually in a fresh Codex session after Phase B delivery.**
3. `.agents/skills/` will contain both `tfw-*` and `source-command-tfw-*` families. Names do not collide, but users may see two affordances for the same workflow. — **Coordinator: Expected. Not a defect — `source-command-tfw-*` are Antigravity-facing, `tfw-*` are Codex-facing. Document in RF §6.**
4. Re-copy semantics in `tfw-update` must distinguish framework-owned installed skill copies from project-owned state: overwriting `.agents/skills/tfw-*` from adapter source is intended; overwriting unrelated `.agents/skills/*` is not. — **Coordinator: Important. The update.md step must explicitly scope re-copy to `.tfw/adapters/codex/skills/tfw-*/ → .agents/skills/tfw-*/` only. No glob on `.agents/skills/*`.**

## 6. Inconsistencies with Code (spec vs reality)

1. The TS header still says `🟡 TS_DRAFT — Awaiting approval`, while the user's explicit `/tfw-handoff TFW-47 phase b` invocation indicates execution approval. The executor will not modify the TS due to the role lock. — **Coordinator: Correct — TS is approved. Cosmetic header mismatch, not a blocker. Role lock respected.**
2. The TS assumes a clean Phase A prerequisite, but the approved Phase A artifacts and implementation remain uncommitted in the current worktree. — **Coordinator: Resolved by Q1 answer — commit Phase A first, then proceed.**
3. Research describes AFD as the empirical source for 11 handwritten skills, but AFD's framework adapter source still contains only a README and generic template; its handwritten skills live only in the installed `.agents/skills/` location. Phase B intentionally promotes individually authored skills into framework source. — **Coordinator: Correct observation. Phase B creates the source-of-truth in `.tfw/adapters/codex/skills/` that AFD never formalized. This is by design.**
4. Existing adapter documentation contains stale mappings such as `.tfw/workflows/research.md` and omits some canonical workflows. Updating Claude Code, Cursor, or Antigravity adapters is explicitly out of scope; these issues must not be fixed as bonus work. — **Coordinator: Confirmed. Do NOT fix other adapters. Report stale mappings in RF §6 Observations for future cleanup.**

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | KC1 — KNOWLEDGE.md D52 | ✅ | Applied | Preserves the coordinator → executor → reviewer evidence pipeline while Phase B uses the mandatory EV artifact delivered in Phase A. |
| 2 | KC2 — TFW-46 research D16 | ✅ | Applied | Read the revoked optional-folder decision; Phase B will follow D53 and always create its `evidence/` folder. |
| 3 | KC3 — knowledge/convention.md F5 | ✅ | Applied | Skills remain thin contracts that open canonical `.tfw/workflows/*.md` files. |
| 4 | KC4 — KNOWLEDGE.md D15 | ✅ | Applied | Reuses the established thin-adapter pattern without copying workflow bodies. |
| 5 | KC5 — KNOWLEDGE.md D50 | ✅ | Applied | Keeps adapter installation and synchronization explicit in init/update workflow integration. |
| 6 | KC6 — knowledge/process.md F3 | ✅ | Applied | Dedicated, accurately named `tfw-*` skills provide the intended visible affordance. |
| 7 | KC7 — knowledge/domain.md F4 | ✅ | Applied | Treats Codex as an IDE-level adapter surface, not as a new TFW role or capability model. |
| 8 | KC8 — conventions.md §12 | ✅ | Applied | AC-7 will only be VERIFIED with fresh-session observation and an artifact reference. |
| 9 | KC9 — conventions.md §14 | ✅ | Applied | Evidence claims without a resolvable artifact are prohibited. |
| 10 | New — knowledge/convention.md F3 | ✅ | Applied | Verified the actual AFD and local `.agents/skills/` layouts instead of trusting the TS description alone. |

## 8. Scope Reopened — Codex-Native UX

> **Date**: 2026-07-21
> **Source**: Stakeholder correction during execution

The stakeholder clarified that the product goal is not “ship 11 skills.” The goal is: after TFW init—or when Codex opens an existing TFW project created by another agent—Codex must immediately understand the project, preserve its state, and route familiar `/tfw-plan`, `/tfw-handoff`, and related text without requiring users to learn an adapter-specific wrapper.

### Current official Codex findings

1. Codex currently exposes a fixed set of built-in top-level slash commands. Official documentation does not provide a supported mechanism for registering arbitrary repo-local commands such as `/tfw-plan` in that menu.
2. Deprecated custom prompts create slash entries only under the `/prompts:{name}` namespace, live in the user's Codex home directory, and are not repository-shared. They do not satisfy the target UX.
3. Repo-local `.agents/skills/` is current and supported for reusable workflows. Explicit invocation is `$tfw-plan` or selection through `/skills`; implicit selection can occur from a matching prompt, but `/tfw-plan` remains ordinary prompt text—not a guaranteed native command.
4. Root `AGENTS.md` is the supported always-loaded repository guidance surface. It is therefore the correct bootstrap/router for “Codex immediately understands this TFW project,” including projects initialized by another agent.
5. The current `init.md` only adds a Codex skill-copy option. It lacks an attach/repair path for an existing `.tfw/` project and does not define safe marker-bounded merging of TFW routing into an existing `AGENTS.md`.
6. The current skill-based implementation overstates two behaviors: it calls `/tfw-*` a deterministic soft alias, while official behavior only promises implicit skill selection from a matching description; and it requires a new task for every skill update, while current documentation says Codex detects changes automatically and restart is only a fallback.

### Blocking scope decision

| # | Question | Answer |
|---|----------|--------|
| 2 | Revise Phase B around the stakeholder goal? Recommended design: root `AGENTS.md` as the mandatory literal `/tfw-*` text router; `tfw-init` supports both new-project setup and existing-TFW attach/repair; `tfw-update` safely refreshes a marker-bounded Codex routing block; skills become optional discoverability aids or are removed entirely. The already-created skill-based commits (`0ae0d9c`, `21599ea`) remain local and unpushed until a revised TS decides their fate. | **Resolved by stakeholder.** Keep repository skills as the supported Codex implementation, make `/tfw-*` the primary user contract, add AGENTS routing and existing-project repair, remove obsolete duplicate adapters, then correct TS and write RF. |

### Executor stop

This stop applied until the stakeholder answered Question 2. The answer is now recorded above.

## 9. Scope Resolution and Research Correction

> **Date**: 2026-07-21
> **Authority**: stakeholder instruction in the active handoff

The stakeholder explicitly directed Codex to analyze the project and current adapter
mechanics, revise the TS, implement the corrected design, clean obsolete Codex
adapters, verify the result, and write RF. This authorizes the Phase B specification
amendment while keeping REVIEW outside the Executor role.

The earlier stop was based on an incorrect inference: it treated the absence of a
public API for arbitrary built-in CLI commands as proof that literal `/tfw-*` input did
not work in Codex Desktop. Live behavior disproved that inference. The task itself was
started with `/tfw-handoff TFW-47 phase b`, and the active Codex catalog discovered the
repository-local `/tfw-*`-described skills.

Corrected architecture:

1. `/tfw-*` remains the cross-tool user contract.
2. Repository skills are Codex's supported workflow implementation and discovery
   format, not a user-facing wrapper.
3. Root `AGENTS.md` supplies immediate project recognition and fallback routing.
4. `tfw-init` and `tfw-update` install or repair both layers without resetting an
   existing project's TFW state.
5. Imported `source-command-tfw-*` full-workflow copies are obsolete duplicates and
   may be removed after inspection.

---

*ONB — TFW-47 / Phase B: Codex Adapter + Framework Integration | 2026-07-21*
