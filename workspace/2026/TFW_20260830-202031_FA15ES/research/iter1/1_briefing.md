# Briefing — "What should we investigate?"
> **Mindset:** Strategist. You're planning an investigation, not doing it. Frame what matters. Resist solving.
> **Test:** "Can I explain WHY we're investigating this and what would change our approach?"
> Parent: [HL-TFW_20260830-202031_FA15ES](../../HL-TFW_20260830-202031_FA15ES.md)
> Goal: Restore field-proven Assisted 1.6 as an independent TFW realization while preserving isolated Full/Assisted identity semantics and a human-gated update path whose publisher chooses the release source.

## Research Plan

### Gather

- Read the current Full binding contract and field Assisted 1.6 identity/update contracts as independent systems; extract invariants rather than normalize their vocabulary.
- Verify platform and tool behavior relevant to device-local configuration roots, Google Drive folder/link semantics, and GitHub release/raw-content semantics against primary external sources.
- Decompose the choice into independent dimensions: device-store topology, identity-key namespace, source locator, release/version discovery, artifact acquisition, and trust/integrity proof.
- Record backward-compatibility constraints for existing Full `%LOCALAPPDATA%\tfw\bindings.yaml` and Assisted `tfw-assisted/bindings.yml` records, without proposing Full product edits.

### Extract

- Cross-reference the Gather dimensions into concrete configurations that keep Full and Assisted records isolated while presenting one convenient device-local parent facility.
- Compare source contracts based on publisher-authored locators, immutable release identities, exact artifact roots, transport-neutral retrieval, and explicit human gates.
- Separate contract fields that are universal from provider adapters/instructions that belong only to Google Drive or GitHub.
- Identify combinations that require executable update or identity machinery, silently change a project key, or introduce a second authority.

### Challenge

- Stress-test bindings coexistence for same path, same human, multiple projects, legacy locations, copied records, missing profiles, and one system being absent.
- Stress-test update discovery for mutable Drive folders, moved/renamed items, GitHub moving branches, private access, partial download, rollback, and source substitution.
- Attempt to delete every proposed manifest/schema/artifact and retain only elements with a unique necessary job under HL Principles 6 and 8.
- Mark what remains uncertain for iteration 2 rather than resolving ambiguity by changing frozen HL claims or Full files.

## Hypotheses (from HL §10)

| # | Hypothesis | HL Status |
|---|-----------|-----------|
| H2a | One backward-compatible machine-local bindings facility can serve Full and Assisted concurrently while keeping their files or namespaces, project keys, profile schemas, and write protocols independent and leaving Full product files unchanged. | needs-research |
| H4 | A provider-neutral source contract can let each Assisted producer select its own release location while the prompt-only `/tfw-update`, version, changelog, and migration maps keep updates explicit and human-gated; research must determine whether a separate manifest or schema has a unique necessary job. | needs-research |

## Scope Intent

- **In scope:** H2a and H4 only; current Full binding invariants; field Assisted 1.6 binding and prompt-only update invariants; Windows device-local placement; Google Drive, GitHub, and generic HTTPS/local-folder source behavior; backward compatibility, privacy, integrity, migration, and human authority.
- **Out of scope:** product edits; Full changes; profile conversion; merging identity models; executable identity/update/synchronization helpers; the 28-file disposition ledger; template neutralization; changelog sanitization; TS design; any change to frozen HL claims.

## Guiding Questions

1. Can a common machine-local parent directory, with two independently owned files/subdirectories and no cross-reader, satisfy “one facility” without changing either binding schema?
2. What minimum publisher-authored metadata is necessary for `/tfw-update` to locate one exact Assisted release across Google Drive, GitHub, or another source without embedding provider-specific semantics in the core contract?
3. Which trust, immutability, and rollback properties must be declared or verified so that a human gate is meaningful rather than merely confirming a mutable locator?

## User Direction

The Coordinator delegated the first pending iteration with an explicit role lock and scope: research only H2a and H4, produce complete stage traces and RES, do not edit product files, TS, frozen HL claims, or `research/iterations.yaml`, and stop after reporting so the Coordinator can decide the next iteration. The task owner has already ruled that Full and Assisted are independent implementations, the publisher chooses Google Drive, GitHub, or another release source, and no executable TFW identity/update runtime may be introduced.

---
Stage complete: YES
