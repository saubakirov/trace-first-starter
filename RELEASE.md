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
- [ ] `.tfw/CHANGELOG.md` and the applicable `.tfw/migrations/{major}.0.0.md` are prepared before the
      corresponding version write;
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
   `.tfw/adapters/manifest.yaml`, and the applicable `.tfw/migrations/{major}.0.0.md` when selected.
4. Run final checks against that exact prepared composition, including post-integration content when
   integration changes operational files. The final checks include the changed metadata and migration.
5. Commit the checked release result with Commit Attribution. A tag, if later authorized, identifies
   this checked commit exactly.
6. Stop before merge to saved master, tag, push, publish, deploy, or notify until each effect is explicitly
   authorized.

The generic release workflow points here for this repository's concrete mechanics. This file never makes
the same mechanics mandatory for another project.

## 7. Self-Hosting Migration Intake

For this repository, a release that changes the TFW payload follows this order:

1. Pin the reviewed source and inspect `.tfw/VERSION`, `.tfw/CHANGELOG.md`, the selected
   `.tfw/workflows/`, `.tfw/templates/`, `.tfw/adapters/`, `.claude/commands/`, and `.agents/` files.
2. Read the applicable `.tfw/migrations/{major}.0.0.md` before preparing a major release. The guide
   must state the receiver-facing ordering and the compatibility obligations; a changelog entry alone
   is not a migration guide.
3. Prepare the selected canonical payload and its exact adapter copies, preserving project-owned,
   unselected, legacy, task-local, and historical traces. Do not alter `workspace/`, task `status.md`,
   task journals, saved-master state, original projects, production state, credentials, tags, or
   publication destinations as part of preparation.
4. Re-measure the selected source, run the configured checks, and verify the final migration and adapter
   topology against the exact release tree.
5. Preserve the exact post-check metadata bytes in the commit and retain the full source/commit lineage;
   the migration and final checks run before `.tfw/VERSION` changes are accepted into the checked
   release tree, and do not rewrite VERSION/CHANGELOG after final verification.
6. Treat tag, push, publication, deployment, and notification as separate effects requiring explicit
   authorization after the checked commit exists.
