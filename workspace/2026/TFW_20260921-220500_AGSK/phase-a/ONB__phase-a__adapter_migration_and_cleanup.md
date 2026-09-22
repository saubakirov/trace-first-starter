# ONB — TFW_20260921-220500_AGSK / Phase A: Adapter Migration and Workspace Cleanup

> **Current filename**: `ONB__phase-a__adapter_migration_and_cleanup.md`
> **Date**: 2026-09-22
> **Author**: executor
> **Status**: 🟠 ONB — Ready for implementation
> **Parent HL**: [HL-TFW_20260921-220500_AGSK](../HL-TFW_20260921-220500_AGSK.md)
> **TS**: [TS Phase A](TS__phase-a__adapter_migration_and_cleanup.md)
> **Producer unit**: antigravity:thread:local:5a66cfd3-f075-45ad-9816-9d1aabf35468
> **Parent Coordinator**: antigravity:thread:local:8888199a-c102-44c8-b661-f9c6bef8d7a6
> **Activation / dispatch source**: owner-only
> **Coordination authority**: "../HL-TFW_20260921-220500_AGSK.md"
> **Originating proposer**: owner:saubakirov

---

## 1. Understanding
Migrate the Google Antigravity adapter to the `skills` standard by updating the `.tfw/adapters/manifest.yaml` target, deleting the legacy `.agent/` and `.agents/workflows/` directories, and removing outdated references in the `.agents/rules/tfw.md` rule and `.tfw/adapters/antigravity/README.md`. Ensure that the 15 value-bearing files match the approved budget and that all automated tests pass.

## 2. Entry Points
- `.agent/rules/agents.md` (to delete)
- `.agents/workflows/` (to delete)
- `.tfw/adapters/manifest.yaml` (to modify)
- `.agents/rules/tfw.md` and `.tfw/adapters/antigravity/tfw-rules.md.template` (to modify)
- `.tfw/adapters/antigravity/README.md` (to modify)

## 3. Questions (blocking — cannot proceed without answers)

| # | Question | Blocking reason | Answer authority / event ref | Operational effect |
|---|---|---|---|---|
| 1 | None | N/A | N/A | N/A |

## 4. Recommendations (suggestions, not blocking)
1. None

## 5. Risks Found (edge cases, potential issues not in TS)
1. Deleting `.agents/workflows/` could potentially break external tools if not documented properly, but Phase B mitigates this.

## 6. Inconsistencies with Code (spec vs reality)
1. None observed. Spec aligns perfectly with current repository state.

## 7. Knowledge Citations

| # | HL §7.2 ref | Read? | Applied / N/A | Notes |
|---|-------------|-------|---------------|-------|
| 1 | `README.md` § How It Works (P0) | ✅ | Applied | Confirmed removal of `.agent/` supports directory organization. |
| 2 | `.tfw/conventions.md` Role Lock Protocol (P1) | ✅ | Applied | Strictly following Executor role lock and TS directives. |
| 3 | `.tfw/compilable_contract.md` §2 Reference Format (P2) | ✅ | Applied | Using exact path references in ONB and RF artifacts. |
| 4 | `KNOWLEDGE.md` Row "Adapters" (P3) | ✅ | Applied | Confirms `.agents` is the authoritative root. |
| 5 | `.tfw/adapters/manifest.yaml` Секции adapters (P5) | ✅ | Applied | Ready to update manifest.yaml to point to skills. |

### Material handover at this return

- **Producer unit:** `antigravity:thread:local:5a66cfd3-f075-45ad-9816-9d1aabf35468`
- **Inspected scope:** `.tfw/adapters/manifest.yaml`, `.agents/rules/tfw.md`, `.tfw/adapters/antigravity/tfw-rules.md.template`, `.tfw/adapters/antigravity/README.md`, `.agent/`, `.agents/workflows/`
- **Material findings:** Ready for implementation of 15 VALUE items. No blockers found.
- **Continuation:** Proceeding to Step 2 — Implement and prove.
- **Uncertainty/unresolved:** None.

---

*ONB — TFW_20260921-220500_AGSK / Phase A: Adapter Migration and Workspace Cleanup | 2026-09-22*
