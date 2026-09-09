# Gather — Boundary evidence
> **Mindset:** Scout. Inspect the cases that could overturn iteration 1.
> **Test:** Find where an unchanged reader would lose history or invent work.
> Parent: [HL SLC](../../HL-TFW_20260907-020729_SLC.md)
> Goal: Complete the preferred design's evidence without expanding scope.

## Comparison Matrix
Fewer than three new independent dimensions remain; use a focused matrix rather than manufacturing another 27-row space.

| Recovery variant | Evidence retained before writes | First live semantic write | Remaining question |
|---|---|---|---|
| V1 | Immutable before-image in existing update attachment area | Exact historical digest reconciliation | Can every cut converge while preserving later unrelated edits? |
| V2 | Same before-image | Active/history config split | Can the pre-existing removed-ID trap be avoided? |
| V3 | External Git checkpoint only | Whole staged group via repository operation | What happens to non-Git receivers and later project work? |

## Findings
### G1: Existing historical intent need not be re-interviewed
This source has 53 recognized historical task directories and 53 corresponding remembered digest keys, 14 current task directories and 11 unaffected remembered keys. There are no cross-scope ID collisions, unmatched historical directories or remembered IDs outside both scopes at baseline `49ddad0`. Forty-two historical tasks have no `status.md`. The owner's explicit container disposition in frozen HL §3 is therefore essential: demanding a modern terminal status on each task would create needless questions, while declaring them all DONE would fabricate history. Helpdesk independently records an equally explicit historical-only owner decision.

### G2: Init and resume need small boundary changes
Init currently routes from `task_containers`; a configured project with only historical traces must take attach/repair, not full init. Named resume currently resolves only that same list and then proposes a next phase from state. Exact historical resolution must work, but a historical result must be presented for reading without automatically turning its old lifecycle into a current-work route. This is an operation guard, not a new lifecycle or reopening feature.

### G3: The registry does not require bulk configuration synchronization
The Config Sync Registry in `.tfw/workflows/config.md` has scope-budget, research, review and content-language inline targets; no container-value propagation entry exists. A project-specific historical path must not be copied into generic workflow prose. Necessary new semantics belong in shared contracts and actual readers; manifest-derived adapters are synchronized only where those canonical source files are copied.

### G4: Parallel PTTC work affects test placement, not the container API
The already received PTTC coordination identifies `docs/scripts/test_integration.py`, new `test_repository_contracts.py`, `test_runtime_context.py` R10/R14 addresses, and `tools/README.md`. The historical landing test stays an integration consumer. SLC needs its whole-corpus assertion updated for reference scope; it must not weaken that assertion to active tasks. Container read-budget extraction in runtime_context also needs the optional historical key for only the workflows that consume it. Re-read PTTC's accepted candidate before fixing TS paths; these research observations do not freeze its future file layout.

### G5: External preservation rationale still applies
[Debian configuration policy §10.7.3](https://www.debian.org/doc/debian-policy/ch-files.html#configuration-files) provides a comparison for preserving user changes and convergent retries. The TFW decision remains grounded in its owner-preservation rules; neither age nor a new default overrides an existing single/custom configuration.

## Checkpoint
| Found | Remaining |
|---|---|
| 42 missing legacy status files make owner disposition materially useful; init/resume and test boundaries identified | Select write/recovery rules and challenge every cut and conflicting input |

**Sufficiency:** external source used: YES; Briefing gap closed for Gather: YES; comparison matrix appropriate: YES.
Stage complete: YES
Decision: close Gather; proceed to explicit adoption/recovery outcomes. No user clarification is required.
