# RELEASE.md — Trace-First Starter

> Project-owned release contract for this self-hosting TFW repository. It is not a receiver default.

## 1. What Is a Release?

A release is a checked, versioned snapshot of the selected TFW payload and its required migrations,
adapters, instructions, and evidence. A selected phase-only result may enter through its actual RF/EV/
REVIEW lineage; it does not need an invented root task report.

## 2. Audience

- downstream TFW projects that copied `.tfw/`;
- framework contributors and maintainers;
- new users evaluating the methodology.

## 3. Version Scheme

This repository uses Semantic Versioning for the framework payload. The installed TFW version is not the
version of a receiving project's application, report, document, or data output. A release number is chosen
only by this project's separately authorized release decision.

## 4. Release Triggers

Prepare a release when the selected reviewed TFW effect is complete and its migration/compatibility
obligations are ready. Unrelated open tasks and harmless trace-only arrivals do not require global cleanup.

## 5. Pre-Release Checklist

- [ ] selected shipping effect and audience are explicit;
- [ ] governing task/phase TS, RF, EV, and REVIEW resolve at their approval epochs;
- [ ] selected VALUE/ASSURANCE composition is complete and isolated;
- [ ] `KNOWLEDGE.md` and applicable documentation/knowledge closure are updated when required;
- [ ] `.tfw/CHANGELOG.md` and every applicable version-addressed guide in `.tfw/migrations/` (including
      minor or patch guides when present) are included in the prepared composition and verified with
      the corresponding metadata;
- [ ] every quantitative claim is re-measured at the checked release source with its command;
- [ ] the update section reaches every earlier supported tag and normative reversals quote the retired
      wording with a successor;
- [ ] configured pytest/MkDocs/package checks pass for the selected release composition;
- [ ] no saved-master, original-project, production, credential, or publication effect is implied by
      preparation alone.

## 6. Release Steps

1. Select the exact reviewed effect and required dependencies in an isolated complete integration/release
   tree. Reuse a suitable completed tree; never tag a partial Executor branch blindly.
2. Resolve the applicable task/phase evidence and retain producer attribution and Candidate reachability.
3. Prepare the version/changelog/config/template/migration result and the still-applicable update route
   in the isolated tree; this includes `.tfw/VERSION`, `.tfw/project_config.yaml`,
   `.tfw/templates/project_config.yaml`, `.tfw/CHANGELOG.md`, `.tfw/templates/briefing.md`,
   `.tfw/adapters/manifest.yaml`, and every applicable version-addressed `.tfw/migrations/` guide
   (including minor or patch guides when selected).
4. Verify the final bytes and run final checks against that exact prepared composition, including
   post-integration content when integration changes operational files. The checks include the changed
   metadata and migration; do not rewrite them after verification.
5. Commit the verified release result with Commit Attribution. A tag, if later authorized, identifies
   this checked commit exactly.
6. Stop before merge to saved master, tag, push, publish, deploy, or notify until each effect is explicitly
   authorized.

The generic release workflow points here for this repository's concrete mechanics. This file never makes
the same mechanics mandatory for another project.

## 7. Self-Hosting Migration Intake

For this repository, apply the single authoritative sequence in §6. The self-hosting intake adds these
checks at the named §6 steps:

- At §6.1, pin the reviewed source and inspect `.tfw/VERSION`, `.tfw/CHANGELOG.md`, the selected
  `.tfw/workflows/`, `.tfw/templates/`, `.tfw/adapters/`, `.claude/commands/`, and `.agents/` files.
- At §6.2, read every applicable version-addressed guide in `.tfw/migrations/`, including minor and
  patch guides when present; a changelog entry alone is not a migration guide, and each guide must
  state receiver-facing ordering and compatibility obligations. The historical selector shape
  `.tfw/migrations/{major}.0.0.md` is illustrative, not an exhaustive restriction.
- At §6.3, prepare the selected canonical payload, exact adapter copies, and metadata while preserving
  project-owned, unselected, legacy, task-local, and historical traces. Do not alter `workspace/`, task
  `status.md`, task journals, saved-master state, original projects, production state, credentials,
  tags, or publication destinations.
- At §6.4, re-measure the selected source, run configured checks, and verify final migration and adapter
  topology against the exact release tree; do not rewrite VERSION/CHANGELOG after verification.
- At §6.5, retain full source/commit lineage. Tag, push, publication, deployment, and notification stay
  separate effects requiring explicit authorization after the checked commit exists.
