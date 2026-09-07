# Phase E 3.0.0 Release Package

> **Classification:** VALUE — accepted release input, not execution evidence
> **Prepared:** 2026-09-07
> **Content baseline:** `b0bfcd22125d8a34366d7eb885a2fb54234bdc7d`
> **Release state:** prepared and replay-verified only; not applied, tagged, pushed, published, or deployed

This package fixes the exact six-file 3.0.0 release result before `/tfw-release`. It is applied only
after Phase E review, K2, DONE, and Main's G-3 preflight name the exact post-DONE baseline and this
package digest. The later baseline may contain approved changes elsewhere, but these six preimages
must still match the content baseline below. Any mismatch stops before a write.

## Destination and digest ledger

All files are UTF-8 without a BOM and use LF line endings. SHA-256 is over exact file bytes.

| Order | Operation | Destination | Baseline SHA-256 | Expected 3.0.0 SHA-256 |
|---:|---|---|---|---|
| 1 | CREATE | `.tfw/migrations/3.0.0.md` | `ABSENT` | `409644e95a32422d1384436c69c5733de04ed85d8285eedc16bc3a260c735b3d` |
| 2 | MODIFY | `.tfw/migrations/2.2.0.md` | `16eda3e281ec7062b021dd1169ecd3dbbd824d959d722ffb1803759d365eb9da` | `40eda9e6a36bce7f1f58f7ac9a5017fc005ff08bf70c035a7e8c717a5993a3f1` |
| 3 | MODIFY | `.tfw/CHANGELOG.md` | `3736f3a2a5d2ca0b0500f08dd2ef12a71c60978f9a28bcca34fd18f492151bc9` | `531c7544691ab9d5fe7972924277853c297265e626ba7769c69e488d10cecbd0` |
| 4 | MODIFY | `.tfw/VERSION` | `c4a2383a03bdb6739d16a0e24058e4b9c7da4e63d203e0be2f448868cc03c530` | `2985be8b28d3ade858e8d8fb4bc22f565b1bf6020dff982dce141f7721b9999c` |
| 5 | MODIFY | `.tfw/project_config.yaml` | `8c9c13f7c80e36740c3f2bc762f2fd0ad3e56ead1997a8c83e605fe666bf9f28` | `9e1b9609552c14deb493ec1632efe586e6693dd7276a9151033b406b15f1af21` |
| 6 | MODIFY | `.tfw/templates/project_config.yaml` | `eb91f17b8d352c0e3b7d8b114e19810ad94144d03c051d718cf2cfde22b72714` | `ac9c22a31db388dfea615168d3ea8768e02ebb974010839aef3aa3d04fc60acc` |

The embedded patch contains the complete final 3.0.0 migration, the exact additive 2.2.0
supersession note, all changelog/updating insertions while retaining historical entries, and the
three exact version substitutions. Its full-index preimages bind every retained byte in modified
files; the SHA-256 ledger binds every final byte.

## Pre-write checks

Run in a generated disposable Git worktree first. The later canonical application uses the same
patch only after Main's G-3 preflight identifies its exact post-DONE checkout.

```powershell
$contentBaseline = 'b0bfcd22125d8a34366d7eb885a2fb54234bdc7d'
$package = 'workspace/2026/TFW_20260902-111644_CRATM/phase-e/evidence/phase-e-3.0.0-release-package.md'
$tempRoot = [IO.Path]::GetFullPath([IO.Path]::GetTempPath())
$releaseTree = [IO.Path]::GetFullPath((Join-Path $tempRoot ('tfw-3.0.0-release-' + [guid]::NewGuid().ToString('N'))))
if (-not $releaseTree.StartsWith($tempRoot, [StringComparison]::OrdinalIgnoreCase)) { throw 'temporary tree escaped its root' }
git worktree add --detach $releaseTree $contentBaseline
$destinations = @(
  '.tfw/migrations/3.0.0.md',
  '.tfw/migrations/2.2.0.md',
  '.tfw/CHANGELOG.md',
  '.tfw/VERSION',
  '.tfw/project_config.yaml',
  '.tfw/templates/project_config.yaml'
)

git -C $releaseTree rev-parse --verify "$contentBaseline^{commit}"
git -C $releaseTree merge-base --is-ancestor $contentBaseline HEAD
if ($LASTEXITCODE -ne 0) { throw 'content baseline is not an ancestor' }
if (Test-Path -LiteralPath (Join-Path $releaseTree '.tfw/migrations/3.0.0.md')) {
  throw '3.0.0 migration already exists'
}
$expectedPre = @{
  '.tfw/migrations/2.2.0.md' = '16eda3e281ec7062b021dd1169ecd3dbbd824d959d722ffb1803759d365eb9da'
  '.tfw/CHANGELOG.md' = '3736f3a2a5d2ca0b0500f08dd2ef12a71c60978f9a28bcca34fd18f492151bc9'
  '.tfw/VERSION' = 'c4a2383a03bdb6739d16a0e24058e4b9c7da4e63d203e0be2f448868cc03c530'
  '.tfw/project_config.yaml' = '8c9c13f7c80e36740c3f2bc762f2fd0ad3e56ead1997a8c83e605fe666bf9f28'
  '.tfw/templates/project_config.yaml' = 'eb91f17b8d352c0e3b7d8b114e19810ad94144d03c051d718cf2cfde22b72714'
}
foreach ($path in $expectedPre.Keys) {
  $actual = (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $releaseTree $path)).Hash.ToLowerInvariant()
  if ($actual -ne $expectedPre[$path]) { throw "preimage mismatch: $path" }
}
```

## Exact ordered application

Decode the block between the patch markers to a UTF-8-without-BOM LF file named
`phase-e-3.0.0.patch`: a line containing only `␠` represents the single-space unified-diff context
line. Check the complete decoded patch, then apply its destinations in ledger order:

```powershell
$packageText = Get-Content -Raw -Encoding UTF8 -LiteralPath $package
$match = [regex]::Match($packageText, '(?s)<!-- RELEASE_PATCH_START -->\r?\n```diff\r?\n(.*?)\r?\n```\r?\n<!-- RELEASE_PATCH_END -->')
if (-not $match.Success) { throw 'release patch block missing or ambiguous' }
$patchPath = Join-Path $releaseTree 'phase-e-3.0.0.patch'
$encodedLines = $match.Groups[1].Value.Replace("`r`n", "`n") -split "`n"
$patchText = (($encodedLines | ForEach-Object { if ($_ -eq '␠') { ' ' } else { $_ } }) -join "`n") + "`n"
[IO.File]::WriteAllText($patchPath, $patchText, [Text.UTF8Encoding]::new($false))
git -C $releaseTree apply --check -- $patchPath
if ($LASTEXITCODE -ne 0) { throw 'complete release patch does not apply' }
foreach ($path in $destinations) {
  git -C $releaseTree apply --index "--include=$path" -- $patchPath
  if ($LASTEXITCODE -ne 0) { throw "ordered release write failed: $path" }
}
Remove-Item -LiteralPath $patchPath
```

<!-- RELEASE_PATCH_START -->
```diff
diff --git a/.tfw/CHANGELOG.md b/.tfw/CHANGELOG.md
index 99b2a5c0a9211a89fb9c68a653659516a1be5da6..3a2b141a0cf3f092f94373c5c9217216b1712b0f 100644
--- a/.tfw/CHANGELOG.md
+++ b/.tfw/CHANGELOG.md
@@ -5,8 +5,23 @@ Format: [Keep a Changelog](https://keepachangelog.com/). Versioning: [Semantic V
␠
 ## [Unreleased]
␠
+## [3.0.0] — 2026-09-07
+
 ### Changed
␠
+- Agent Team is now a provider-neutral, explicitly owner-selected execution mode: one stable LEAD
+  principal is attribution, while Coordinator, Researcher, Executor, and Reviewer remain distinct
+  directly addressable working units. Human-rooted initiation, immutable mandate/grant ceilings,
+  preserved proposal origin, bounded dispatch, exact return channels, and independent review remain
+  separate from profile, binding, title, provider, role, and `writer` metadata.
+- Concurrent mutation uses isolated worktrees, exact-path staging, producer-attributed landing
+  commits, and retained Candidate reachability. Session identity is navigation-only; only the exact
+  LEAD root Coordinator renders the LEAD title, and same-principal children retain ordinary role
+  titles.
+- Handoff, Research, and Review set optional event `writer` only when **Who Is Acting** resolves a
+  declared principal; otherwise they omit it. They never create one profile per session, and a shared
+  principal grants a child no unit identity or authority.
+
 - Task-local `status.md`, journals, and artifacts are now the only ordinary Full discovery
   inputs. The shared portfolio cache, generator, freshness check, default public Tasks navigation,
   and root-guide catalogue routes are removed. Generated documentation still copies every task
@@ -23,6 +38,12 @@ Format: [Keep a Changelog](https://keepachangelog.com/). Versioning: [Semantic V
␠
 ### Added
␠
+- Canonical glossary routers now name Principal, Initiation Chain, Worktree Protocol, Landing Commit,
+  and AT while leaving each normative procedure at its single owner.
+- The reviewed Phase E release package fixes the six destination contents and SHA-256 digests before
+  release application. The release commit is separate from implementation/closure and precedes any
+  independently authorized tag, push, publication, or deployment.
+
 - Upstream-only `tools/tfw_state.py` provides side-effect-free semantic readers and
   `tools/tfw_doctor.py` provides exactly four optional read-only operations: `status`, `check tasks`,
   `check project`, and `knowledge-pending`, with deterministic human/JSON output and exits 0/1/2 for
@@ -43,6 +64,18 @@ Format: [Keep a Changelog](https://keepachangelog.com/). Versioning: [Semantic V
␠
 ### Compatibility and updating
␠
+Read the target's `.tfw/workflows/update.md`, not the installed one. Pin `v3.0.0`, verify its version,
+and follow `.tfw/migrations/3.0.0.md`. Receivers on 2.2.0 use that guide directly. Receivers on 2.1.0,
+2.0.0, a `2.0.0-dirty*` tag, or 1.x first follow the ordered prior routes named there; 0.x and
+unknown/custom receivers require a project-specific migration plan. Intermediate tags need not be
+installed, but their still-applicable migration actions may not be skipped.
+
+The retired current-workflow instruction is: “A writer is not named yet — that is TFW-54 — so do not
+create a profile per session.” Replace current payload copies through the canonical update route;
+preserve historical true-at-the-time artifacts. If a receiver created per-session profiles, preserve
+the trace and use a separately reviewed owner-authorized migration to stable principals and external
+machine bindings.
+
 Pin the target release first, acquire `tools/migrations/2.0.0/` from that same immutable ref when
 pre-2.0 conversion is still needed, and follow the target `update.md`. Remove obsolete payload files
 only after exact-path comparison. Preserve receiver config, knowledge state, North Star, team, task
diff --git a/.tfw/VERSION b/.tfw/VERSION
index ccbccc3dc62631f22ff358ac418e52401ec770b4..4a36342fcab700951adb18ae7adc930997f6c3f4 100644
--- a/.tfw/VERSION
+++ b/.tfw/VERSION
@@ -1 +1 @@
-2.2.0
+3.0.0
diff --git a/.tfw/migrations/2.2.0.md b/.tfw/migrations/2.2.0.md
index 9eacef5f2960ac450f5b0289a8212bd9ac1b9fe7..1c30a458dfe711c06bf6dfcd586455fde6b4cb1b 100644
--- a/.tfw/migrations/2.2.0.md
+++ b/.tfw/migrations/2.2.0.md
@@ -1,5 +1,8 @@
 # Updating to TFW 2.2.0
␠
+> **Superseded by** `.tfw/migrations/3.0.0.md` (2026-09-07) for targets at 3.0.0 or later. This
+> guide remains the historical 2.2.0 route and must not replace the final target's migration.
+
 Read the target's `.tfw/workflows/update.md`, not the installed one. Pin `v2.2.0`, verify
 its `.tfw/VERSION`, and follow that pinned workflow; this guide supplies the release-specific
 decisions, not a second update algorithm. Never copy a moving working tree.
diff --git a/.tfw/migrations/3.0.0.md b/.tfw/migrations/3.0.0.md
new file mode 100644
index 0000000000000000000000000000000000000000..62586c4fc6e8e895a4ca8eae127e631add81c98e
--- /dev/null
+++ b/.tfw/migrations/3.0.0.md
@@ -0,0 +1,138 @@
+# Updating to TFW 3.0.0
+
+Read the target's `.tfw/workflows/update.md`, not the installed one. Pin `v3.0.0`, verify its
+`.tfw/VERSION`, and follow that pinned workflow. This guide records the 3.0.0 migration decisions;
+it is not a second update algorithm. Never copy a moving working tree.
+
+## What this release gives you
+
+- Provider-neutral Agent Team (AT) operation with one owner-selected stable LEAD principal and
+  distinct, directly addressable Coordinator, Researcher, Executor, and Reviewer working units.
+- Human-rooted delegation, immutable amendment grants, preserved proposal origin, exact dispatch
+  edges, and owner-return conditions that identity metadata cannot bypass.
+- Worktree isolation, exact-path staging, producer-attributed landing commits, and Candidate
+  reachability across cleanup.
+- Optional event `writer` attribution resolved through **Who Is Acting** without creating profiles
+  per session or treating a principal as a working unit.
+- Task-local discovery and Knowledge Gate semantics without a shipped Python runtime, shared task
+  index, or ordinary generated status catalogue.
+
+## 1. Select the starting-version route
+
+Intermediate tags do not need to be installed separately. Apply every still-relevant migration in
+order under the final target's `update.md`; inspect actual receiver state before each action.
+
+| Installed version | Route to 3.0.0 |
+|---|---|
+| 2.2.0 | This guide, including the RTBO removals and CRATM adoption below |
+| 2.1.0 | Apply the 2.2.0 guide, then this guide |
+| 2.0.0 | Apply the 2.1.0 changelog updating section and the 2.2.0 guide, then this guide |
+| Any `2.0.0-dirty*` | Follow the ordered dirty-to-2.0.0 route in the 2.1.0 changelog, then 2.2.0 and this guide |
+| 1.x | Apply `migrations/2.0.0.md`, the 2.1.0 route, the 2.2.0 guide, then this guide |
+| 0.x or unknown/custom | No automatic route is claimed. Stop before writes and obtain a project-specific migration plan |
+
+Do not repeat a migration already evidenced in the receiver. A copied version string is not proof
+that its structural migration ran.
+
+## 2. Preserve project-owned state before payload writes
+
+Pause task writers at a safe workflow boundary. Record the installed version and provenance, the
+target ref and digest, current `git status`, task-container configuration, build commands, adapter
+roots, and any project-owned changes under paths the target updates. Make a recoverable commit or
+backup. Preserve project configuration, knowledge state and topic files, North Star, `team/`, task
+history, status files, journals, artifacts, snapshots, and unrelated build commands.
+
+Resolve the acting human and optional principal through the target workflow. Do not copy a local
+machine binding into the repository and do not infer a principal from provider, model, account,
+hostname, folder, session, role, or `writer`.
+
+## 3. Apply the target payload and adapter topology
+
+Use the pinned target manifest and update workflow to copy declared payload files, managed adapter
+blocks, and all eleven `/tfw-*` routes. Antigravity's persistent and command roots are plural
+`.agents/`; `.agent/` is the separate accepted workflow-copy surface. Preserve receiver-owned text
+outside managed blocks and preserve configured project values.
+
+The target workflow is authoritative over selective reads, lifecycle gates, role locks, templates,
+and copy parity. Do not transplant only the AT paragraphs or hand-edit receiver copies independently
+of their canonical workflows.
+
+## 4. Apply the RTBO removals and configuration mapping
+
+After exact-path comparison and preservation of project-owned state, remove obsolete copied payload
+files `.tfw/scripts/gen_index.py`, `.tfw/scripts/migrate_board.py`, their payload-only tests, and the
+tracked shared cache `workspace/00-INDEX.md`. Remove these retired keys from active config and local
+templates without mapping them to another validity rule:
+
+| Retired key | 3.0.0 result |
+|---|---|
+| `tfw.journal.max_summary_length` | removed; complete one-line prose is structurally validated, while brevity remains advice |
+| `tfw.knowledge.max_index_lines` | removed; no shared knowledge index is maintained |
+| `tfw.knowledge.max_index_facts_lines` | removed; no line ceiling substitutes for semantic reconciliation |
+
+Keep configured `task_containers`. Task-local `status.md`, journals, and referenced artifacts are the
+ordinary discovery surface. Upstream-only `tools/tfw_state.py`, `tools/tfw_doctor.py`, and the pinned
+`tools/migrations/2.0.0/` bundle are optional maintainer tooling, not copied Full runtime or default
+receiver gates. Remove stale receiver build commands that invoke the retired `.tfw/scripts/` paths;
+replace them only with real project checks.
+
+## 5. Adopt principals and Agent Team without inventing authority
+
+Existing projects remain in CL unless the human owner explicitly selects AT after approving and
+committing the governing HL. Do not infer AT from profiles, bindings, task titles, provider support,
+or existing parallel sessions. An AT declaration selects one existing stable agent principal as
+LEAD and fixes its protected mandate; working-unit assignments and bounded dispatches are separate,
+append-only operational trace.
+
+Validate existing `team/{handle}.md` files against the target schema. Four-key human profiles remain
+valid. Agent profiles require an existing human `accountable_to` and immutable Boolean
+`may_rule_amendments`; a grant change requires a new handle. Do not create profiles for roles,
+workers, sessions, or runs. Preserve historical events unchanged. New events always name the human
+in `on_behalf_of`, the tool in `via`, and set optional `writer` only when **Who Is Acting** resolves a
+declared valid principal.
+
+Only the selected LEAD's exact root Coordinator unit can use a true amendment grant, and only inside
+the owner-fixed mandate. Children sharing its principal inherit no grant, role, parent, scope,
+proposal origin, or authority. Refuse ambiguous or non-human-rooted chains and route owner-reserved,
+out-of-mandate, malformed, same-ruler, or unavailable-holder cases exactly as the target contract
+requires.
+
+## 6. Remove the retired live-workflow promise
+
+Search current workflow/rule copies for this exact retired instruction:
+
+> A writer is not named yet — that is TFW-54 — so do not create a profile per session.
+
+The target workflows supersede it with optional resolved-principal attribution. Replace current
+payload copies through the canonical update route; do not rewrite historical task artifacts or
+changelog entries where the sentence was true at the recorded epoch. A receiver that created a
+profile per session must stop, preserve the history, choose or create only valid stable principals
+under owner authority, update local bindings outside the repository, and remove invalid profiles
+only through a separately reviewed project migration.
+
+## 7. Approval epochs and preservation rules
+
+Apply prospective semantics from the 3.0.0 payload/update approval epoch. Do not reinterpret earlier
+approved work, rewrite immutable events, collapse principals into working units, or promote generated
+views to authority. Preserve exact reviewed snapshot refs while testing current behavior against the
+updated tree. A task's fixed Baseline, Candidate selector, VALUE accounting, and review separation
+remain authoritative for that task.
+
+## 8. Verify and roll back safely
+
+Before declaring the update complete, verify:
+
+1. `.tfw/VERSION`, active `tfw.version`, and the installed framework version agree at `3.0.0`.
+2. Every manifest-declared adapter route exists and exact-copy receivers match canonical workflows.
+3. `.agents/` and `.agent/` retain their distinct manifest-defined meanings.
+4. The three retired current-workflow sentences, removed runtime paths, shared cache, and retired
+   config keys are absent from current payload/config while historical artifacts remain unchanged.
+5. No session-created profiles or repository-local machine bindings were introduced.
+6. Configured task discovery, status/event structure, Knowledge Gate, project build commands, target
+   tests, and strict documentation build pass without a shipped runtime dependency.
+7. The update diff contains only intended payload/config changes and preserved receiver-owned hunks.
+
+On failure, stop before lifecycle claims, tags, pushes, publication, or deployment. Restore the
+pre-update payload and config from the recorded commit or backup, restore only exact removed paths,
+and leave project history and immutable events untouched. Re-run the receiver's original checks to
+confirm the rollback before resuming work.
diff --git a/.tfw/project_config.yaml b/.tfw/project_config.yaml
index 59218bc9556ce691423e5a52205b1d05672cfea7..1cb9139793bd5b95fe3837380dea9ea5329ab620 100644
--- a/.tfw/project_config.yaml
+++ b/.tfw/project_config.yaml
@@ -4,7 +4,7 @@ project:
   branch: main
␠
 tfw:
-  version: "2.2.0"   # Installed TFW version (update via tfw-update)
+  version: "3.0.0"   # Installed TFW version (update via tfw-update)
   installed_from: "self"   # this repository IS the upstream; a receiving project names source@tag
   upstream: "https://github.com/saubakirov/trace-first-starter"  # Source for tfw-update
   content_language: en      # Language for filled artifact content (en, ru, etc.)
diff --git a/.tfw/templates/project_config.yaml b/.tfw/templates/project_config.yaml
index 5b12c5853c27c5fa9c05da8690514968674f88f0..5957bb04988ea05700be910d0f2be2649d2ca281 100644
--- a/.tfw/templates/project_config.yaml
+++ b/.tfw/templates/project_config.yaml
@@ -8,7 +8,7 @@ project:                              # ← PROJECT: set during init
   branch: main
␠
 tfw:
-  version: "2.2.0"                    # ← FRAMEWORK: updated by tfw-update
+  version: "3.0.0"                    # ← FRAMEWORK: updated by tfw-update
   upstream: "https://github.com/saubakirov/trace-first-starter"  # ← FRAMEWORK
   # Where this payload ACTUALLY came from, in ONE form: {upstream}@{verified-tag}, where
   # {upstream} is the value of `upstream` above as configured — a URL or a symbolic name —
```
<!-- RELEASE_PATCH_END -->

## Post-write verification

```powershell
$expectedPost = @{
  '.tfw/migrations/3.0.0.md' = '409644e95a32422d1384436c69c5733de04ed85d8285eedc16bc3a260c735b3d'
  '.tfw/migrations/2.2.0.md' = '40eda9e6a36bce7f1f58f7ac9a5017fc005ff08bf70c035a7e8c717a5993a3f1'
  '.tfw/CHANGELOG.md' = '531c7544691ab9d5fe7972924277853c297265e626ba7769c69e488d10cecbd0'
  '.tfw/VERSION' = '2985be8b28d3ade858e8d8fb4bc22f565b1bf6020dff982dce141f7721b9999c'
  '.tfw/project_config.yaml' = '9e1b9609552c14deb493ec1632efe586e6693dd7276a9151033b406b15f1af21'
  '.tfw/templates/project_config.yaml' = 'ac9c22a31db388dfea615168d3ea8768e02ebb974010839aef3aa3d04fc60acc'
}
foreach ($path in $expectedPost.Keys) {
  $actual = (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $releaseTree $path)).Hash.ToLowerInvariant()
  if ($actual -ne $expectedPost[$path]) { throw "release digest mismatch: $path" }
}
$changed = @(git -C $releaseTree diff --cached --name-only -- $destinations)
if (Compare-Object $destinations $changed) { throw 'release diff is not the exact six-path set' }
git -C $releaseTree diff --cached --check -- $destinations
if ($LASTEXITCODE -ne 0) { throw 'release diff check failed' }
if ((Get-Content -Raw (Join-Path $releaseTree '.tfw/VERSION')).Trim() -ne '3.0.0') { throw 'VERSION mismatch' }
$activeVersions = @(Select-String -Path (Join-Path $releaseTree '.tfw/project_config.yaml') -Pattern '^  version: "3\.0\.0"')
$templateVersions = @(Select-String -Path (Join-Path $releaseTree '.tfw/templates/project_config.yaml') -Pattern '^  version: "3\.0\.0"')
if ($activeVersions.Count -ne 1 -or $templateVersions.Count -ne 1) { throw 'config version mismatch' }
python -m pytest tools/tests/ docs/scripts/ -q --collect-only
python -m pytest tools/tests/ docs/scripts/ -q
python -m mkdocs build --strict -f docs/mkdocs.yml --quiet
```

The changelog keeps an empty `[Unreleased]`, makes 3.0.0 the first released entry, retains every
historical entry, routes all supported earlier tags, and quotes only the retired live-workflow
instruction needed to locate its supersession. No quantitative product claim is introduced.

## Rollback boundary

Until the separately verified six-path release commit exists, rollback is the exact reverse patch in
the disposable/application tree: `git apply -R --check phase-e-3.0.0.patch`, then
`git apply -R --index phase-e-3.0.0.patch`. Do not reverse after other writes overlap these paths. After the
release commit, rollback requires a new reviewed forward commit; never reset, rewrite task history,
or delete immutable events. Tag, push, publication, deployment, saved-checkout landing, and foreign
dirty-hunk preservation remain separate G-3/Main actions and are not authorized by this package.
