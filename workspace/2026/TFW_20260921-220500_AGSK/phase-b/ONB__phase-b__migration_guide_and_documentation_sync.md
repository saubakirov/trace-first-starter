# ONB — TFW_20260921-220500_AGSK / Phase B: Migration Guide and Documentation Sync

> **Current filename**: `ONB__phase-b__migration_guide_and_documentation_sync.md`

> **Date**: 2026-09-22
> **Author**: Executor
> **Status**: 🟠 ONB — No blockers
> **Parent HL**: [HL-TFW_20260921-220500_AGSK](../HL-TFW_20260921-220500_AGSK.md)
> **TS**: [TS Phase B](TS__phase-b__migration_guide_and_documentation_sync.md)
> **Producer unit**: antigravity:thread:local:ec458eac-9120-412b-ae03-78f365c5484d
> **Parent Coordinator**: antigravity:thread:local:8888199a-c102-44c8-b661-f9c6bef8d7a6
> **Activation / dispatch source**: owner-direct (`/tfw-handoff agsk phase-b`)
> **Coordination authority**: "../HL-TFW_20260921-220500_AGSK.md"
> **Originating proposer**: none

---

## 1. Understanding

Phase B delivers the external-facing documentation layer of the AGSK migration: a normative migration guide for downstream projects upgrading from versions with `.agent/` and `.agents/workflows/`, synchronization of all project documentation (KNOWLEDGE.md, glossary, three README localizations) with the new adapter architecture, a CHANGELOG entry for 3.5.0, and explicit coordination messaging instructions in the Antigravity rule and adapter documentation. The work builds directly on Phase A's completed adapter migration (Candidate `68dd9ce`, approved and reviewed).

## 2. Entry Points

| File | Role |
|---|---|
| `.tfw/migrations/3.4.0.md`, `.tfw/migrations/3.4.1.md` | Structural precedents for the new `3.5.0.md` |
| `KNOWLEDGE.md` L31 | Adapters row — stale references to `.agent/workflows/` and 11 routes |
| `.tfw/glossary.md` L379 | Tool Adapter definition — stale `.agents/workflows/` reference |
| `README.md` L192 | Antigravity entry point — stale `.agent/rules/tfw.md` |
| `README.ru.md` L190 | Russian Antigravity entry point — stale `.agent/rules/tfw.md` |
| `README.kk.md` L191 | Kazakh Antigravity entry point — stale `.agent/rules/tfw.md` |
| `.tfw/CHANGELOG.md` L6-7 | `[Unreleased]` section — needs `[3.5.0]` entry |
| `.agents/rules/tfw.md` L26-27 | Missing `Coordination Messaging` section |
| `.tfw/adapters/antigravity/tfw-rules.md.template` L26-27 | Same — must stay byte-identical to tfw.md |
| `.tfw/adapters/antigravity/README.md` L18 | Missing messaging documentation |
| `.tfw/adapters/manifest.yaml` | Already migrated in Phase A — no changes needed |

## 3. Questions (blocking — cannot proceed without answers)

No blocking questions. The TS prescribes exact content for all 10 VALUE files, precedents are clear, and Phase A's Candidate provides the verified baseline. Owner directly invoked `/tfw-handoff`, approving the TS.

## 4. Recommendations (suggestions, not blocking)

1. The CHANGELOG date for `[3.5.0]` should use today's actual date (`2026-09-22`) as the implementation date, recognizing that the physical bump of `.tfw/VERSION` occurs during `/tfw-release` and is out of scope per TS §2.

## 5. Risks Found (edge cases, potential issues not in TS)

1. The `Workflows` row in KNOWLEDGE.md (L29) still references `resume` among the workflow list. This is out of scope (not in the 10-file VALUE denominator), but it is a residual inconsistency from 3.4.1 that the Reviewer may note.

## 6. Inconsistencies with Code (spec vs reality)

1. KNOWLEDGE.md L31 currently says "11 routes" and includes `.agent/workflows/` in the file list — the TS correctly targets this for update to "10 routes" with `.agents/skills/` replacing it.
2. The three README files all reference `.agent/rules/tfw.md` (singular `.agent`) as the Antigravity entry point — the TS correctly targets the update to `.agents/rules/tfw.md`.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | `README.md` § How It Works (P0) | ✅ | Applied: README adapter table update ensures directory layout consistency | |
| 2 | `.tfw/conventions.md` Role Lock Protocol (P1) | ✅ | Applied: Executor role lock — no HL/TS/RES/REVIEW/scope modifications | |
| 3 | `.tfw/compilable_contract.md` §2 Reference Format (P2) | ✅ | Applied: cross-references in migration guide will follow compilable format | |
| 4 | `KNOWLEDGE.md` Row "Adapters" (P3) | ✅ | Applied: directly targeted for AC-2 update | |
| 5 | `.tfw/adapters/manifest.yaml` (P5) | ✅ | Applied: manifest paths verified as source of truth for all documentation updates; manifest itself is out of scope (Phase A) | |

No additional PV sources identified beyond the TS-declared set.

### Material handover at this return

- **Producer unit:** Executor at `antigravity:thread:local:ec458eac-9120-412b-ae03-78f365c5484d`.
- **Source/epoch:** Phase-b TS at `TS_DRAFT`, owner approval by `/tfw-handoff` invocation at 2026-09-22T10:57+05:00; baseline `a26322e` (Phase A RF commit).
- **Inspected scope:** All 10 VALUE paths in current working tree, manifest.yaml (no changes needed), migration precedents `3.4.0.md` and `3.4.1.md`.
- **Material findings:** No blockers. All target files exist at expected locations with identified stale content ready for update. Structural precedents for migration guide are clear.
- **Uncertainty:** None.
- **Continuation:** Proceed to implementation (Step 2).

---

*ONB — TFW_20260921-220500_AGSK / Phase B: Migration Guide and Documentation Sync | 2026-09-22*
