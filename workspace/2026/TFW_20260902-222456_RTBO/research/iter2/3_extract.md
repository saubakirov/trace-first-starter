# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> **Test:** "Does my configuration space reveal at least one combination that nobody proposed in the Briefing?"
> Parent: [HL-TFW_20260902-222456_RTBO](../../HL-TFW_20260902-222456_RTBO.md)
> Goal: TFW keeps task state inspectable at scale without a committed portfolio cache, a hard prose-length gate, or a runtime prerequisite.

## Configuration Space

The full cross-product has 16,384 combinations. Rows below preserve the coherent architectural
families. Configurations with a committed cache, mandatory ordinary-Full helper, regex pretending to
parse general YAML, current rules imposed indiscriminately on immutable legacy history, or no
compiled citation targets are direct contradictions and are omitted before Challenge.

| Config | D1: Full executable ownership | D2: carrier interpretation | D3: Knowledge Gate mechanism | D4: pre-2.0 migration delivery | D5: diagnostic applicability | D6: documentation exposure | D7: prose constraint behavior |
|---|---|---|---|---|---|---|---|
| C1 | none; outcome-only workflow | agent semantic YAML / available conforming parser | explicit no-helper algorithm | versioned transient bundle | shape/contract epochs | hidden traces + generated task landings | prompt guidance + projection wrapping |
| C2 | none; outcome-only workflow | same | same | immutable release asset/tag archive | shape/contract epochs | hidden traces + generated task landings | same |
| C3 | optional collector | declared PyYAML only on explicit use | no-helper primary; command accelerator | versioned transient bundle | shape/contract epochs | hidden traces + public slim status page | prompt guidance + projection wrapping |
| C4 | optional shared parser/core | declared PyYAML only on explicit use | command or no-helper parity | versioned bundle imports shared core | rule-introduction epochs | hidden traces + generated task landings | annotations separated from assertions |
| C5 | none | environment-selected parser | explicit no-helper algorithm | guide only; agent synthesizes implementation | shape/contract epochs | hidden traces + generated task landings | prompt guidance only |
| C6 | none | agent semantic YAML | explicit no-helper algorithm | versioned transient bundle | structural errors only; compatibility not classified | hidden traces + task landings + opt-in CI status artifact | prompt guidance + projection wrapping |
| C7 | optional collector | Python standard library over newly narrowed carrier | command or no-helper parity | standard-library versioned bundle | shape/contract epochs | hidden traces + generated task landings | prompt guidance + projection wrapping |
| C8 | none | agent semantic YAML / available parser | explicit no-helper algorithm | versioned transient bundle | shape/contract epochs | hidden traces + public top-level task library | prompt guidance + projection wrapping |
| C9 | none | agent semantic YAML / available parser | explicit no-helper algorithm | versioned transient bundle | shape/contract epochs | hidden traces + generated task landings; no status aggregate | no numeric prose limits anywhere |

Two combinations were not explicit in the Briefing:

- **C1/C6 dependency asymmetry:** ordinary Full can be completely executable-free while the one-time
  pre-2.0 compatibility route declares a runtime. A migration dependency is not an ordinary lifecycle
  dependency when it is loaded only on a crossed major and removed afterwards.
- **Hidden per-task landings without a task library:** generating an `index.html` target for a no-HL
  task does not require a global `Tasks` navigation item or a public portfolio. Landing existence and
  landing prominence are independent switches.

## Findings

### E1: exactness needs one authority, not one shipped executable

The Knowledge Gate proof separates three layers that the monolith previously collapsed:

```text
Full method authority
  canonical YAML meanings + task grammars + selected headings + tuple framing + stop rules
                 |
                 +---- acting agent / environment-chosen implementation
                 |       produces the gate result without a required helper
                 |
                 +---- upstream conformance corpus
                         tests the maintainer reference implementation and known vectors
```

Full must retain the exact result algorithm because `/tfw-plan` and `/tfw-knowledge` act on it. It
does not need to retain `gen_index.py`. The independent PowerShell calculation demonstrates that
SHA-256, fence-aware extraction, and map reconciliation are implementation-independent; the regex
failure demonstrates that the prose cannot suggest a partial YAML parser. “Semantically read the
addressed YAML mapping” is already the normal agent operation throughout TFW, while an available
conforming processor may accelerate it.

The smallest single authority is an addressed `Knowledge Gate` range in Full canon, read by both
workflows. Duplicating the ten-step algorithm into both workflows would recreate drift; hiding it in
upstream tests would make the tests, not Full, the method. Upstream fixtures should record at least
the exercised known vectors (empty tuple, fenced heading, changed body, removed identity, malformed
path, collision, absent map, equal timestamp, retry-before-state, soft/hard/off), but they consume the
Full contract and do not outrank it.

This is structurally analogous to the distinction between validation assertions and annotations:
JSON Schema defines assertions as pass/fail constraints and annotations as useful non-assertion
information. The distinction permits one carrier to convey guidance without letting it change
validity. Source: [JSON Schema validation vocabulary](https://json-schema.org/draft/2020-12/json-schema-validation).

For `/tfw-init` and `/tfw-update`, the no-helper outcome is smaller than the current project doctor:
verify the files just installed, VERSION/config agreement, at least one human profile, creation
container, retired-key absence, non-local provenance, named build paths, adapter parity, retired
vocabulary, customization, and configured builds. These workflows already perform most of those
checks directly. The current helper additionally requires its own `gen_index.py` and
`migrate_board.py` presence, a circular condition that cannot survive their removal. The correct
replacement is explicit workflow postconditions over the just-changed scope, while the broader
whole-project report moves upstream.

### E2: migration is a versioned compatibility product, not a Full utility

| Delivery shape | Works with no Python/PyYAML? | Exactness evidence | Receiver persistence | Cost / failure mode |
|---|---|---|---|---|
| current active `.tfw/scripts` | no | 64 pass, 1 skipped | permanent | undeclared import fails before help; permanent code for a one-time act |
| versioned transient upstream bundle | only when its declared environment exists | can carry the same implementation/tests/manifest guarantees | removed after crossed-major migration | honest hard stop when runtime absent; low architecture churn |
| immutable release asset | only when its declared environment exists | tag/SHA/asset attestation can identify exact bytes | downloaded only when needed | network/release-host dependency; asset matrix if binaries are attempted |
| guide plus agent-synthesized implementation | potentially yes | none until the generated implementation passes shared vectors and a dry-run manifest | ephemeral | widest availability, highest one-off verification cost; unsafe as an automatic fallback |
| multi-platform self-contained binaries | often | would need build provenance and platform tests | transient | packaging, signing, OS/architecture matrix, and release maintenance exceed the one-time value shown here |

The migration belongs to the **source major boundary** (`pre-2.0 -> 2.x`), while its corrected
implementation belongs to the exact destination release being installed. Semantic Versioning makes
that distinction useful: a major marks incompatible behavior, while every correction must appear in
a new version rather than silently changing an old release. Source:
[Semantic Versioning 2.0.0](https://semver.org/).

The resulting compatibility shape is:

1. Full keeps the crossed-major guide and exact invariants.
2. The pinned upstream source or immutable release supplies a versioned migration bundle outside the
   active Full runtime surface.
3. The bundle declares Python/PyYAML if it still needs them and fails before any receiver write when
   they are absent.
4. A no-Python receiver either runs that pinned bundle in a temporary compatible environment or uses
   another implementation only after the same conformance and dry-run accounting prove parity.
5. After success, the transient bundle leaves; history, snapshot, manifest, status files, and guide
   remain readable.

GitHub artifact attestations can bind a generated bundle to repository, workflow, commit SHA, and
trigger, but that is integrity evidence for delivery, not evidence the binary is worth maintaining.
Source: [GitHub artifact attestations](https://docs.github.com/en/actions/concepts/security/artifact-attestations).

### E3: diagnostic contract is a two-axis matrix, not one checker name

Diagnostics vary by both **audience/subject** and **applicability/consequence**:

| Subject / audience | Error (exit 1) | Indeterminate (exit 2) | Advice/note (exit-neutral) |
|---|---|---|---|
| selected task before a new write | missing required structure, invalid identity/ref/time/transition under current write contract | source cannot be read or authority cannot be resolved | concise-prose guidance |
| upstream corpus doctor, explicit local run | duplicate identity, malformed current status, missing authority, contradictory terminal state, corrupt current event shape | incomplete scan, invalid config carrier, unavailable required input | legacy shape, stateless historical phases, prose length |
| upstream CI | same material structural/project findings selected by the CI job | tool/setup failure; must not be reported as clean | advisory report may be uploaded but cannot redden the job |
| ordinary receiving Full | no automatic whole-corpus report | helper absence is irrelevant unless explicitly requested | workflows read selected state and continue |

Exit 0 means “the requested diagnostic completed and found no material error,” not “the project is
universally healthy.” Exit 1 means material finding. Exit 2 means the diagnostic could not establish
its subject; treating incomplete input as either clean or a material corpus defect would be false.
Advice and compatibility notes never alter these exit codes.

Applicability is durable and minimal:

- legacy filename/field shape selects the legacy reader;
- current filename/field shape selects current structural requirements that existed for that shape;
- stricter new-write checks run before installation and are not automatically retroactive;
- prose lengths are annotations across every epoch, including the real 123 event.

The task does not need to invent TFW-16's behavior analysis or a universal health score. “Doctor” is
only a bounded upstream interface over proven structural/project checks and explicit coverage notes.

### E4: the documentation and portfolio topology has five independent outputs

```text
task Markdown
  +--> hidden compiled artifact pages ----------> cited trace works
  +--> hidden task landing (generated in CI) ----> bare no-HL ID works
  +--> public global Tasks navigation -----------X no value evidence

task status.md
  +--> public current-status page ---------------? no reader evidence
  +--> opt-in CI artifact ------------------------> maintainer snapshot, disposable
```

The hidden build proved the first arrow and disproved the assumption that a task folder is already a
landing. Therefore a navigation-removal TS must pair subtraction with one of two resolver-safe
outcomes: generate a hidden landing per task, or make bare IDs resolve to a deterministic compiled
artifact. The landing is semantically cleaner because a bare task ID names the task, not whichever
artifact happened to sort first.

The docs generator, resolver, and any status projection belong upstream/CI, with their Python and
PyYAML dependencies declared in the docs environment. They may share an upstream implementation
module, but no docs import should force that module into a receiving Full project. The public site
keeps task pages only as reachable targets and removes the top-level library. A current-status page
is not promoted without reader evidence. An explicit CI artifact remains a reversible diagnostic
option; automatic upload is not necessary for ordinary documentation builds.

### E5: prose policy follows the protected object, not the field type

The extracted rule is:

```text
machine assertion = material consumer + observable harm + compliance before irreversible act
otherwise          = authoring guidance or projection-local presentation
```

Applied consequences:

- Delete numeric validity for `summary`, `title`, `goal`, `value`, `outcome`, and
  `lifecycle_verbatim`.
- Keep required presence, scalar/carrier shape, whole identity, declared lifecycle, authority,
  terminal/outcome relationship, and current transition/ref/time rules.
- Keep “brief one-line, normally <=120” for summary and concise one-line guidance for ordinary status
  prose, but no parser/checker/review failure follows from length.
- `lifecycle_verbatim` is not ordinary prose: it is evidence. Preserve it exactly with no truncation
  and no numeric guidance.
- Delete `max_summary_length`, `max_index_lines`, and `max_index_facts_lines`; an ignored limit is a
  false contract.
- Treat workflow word density as an upstream maintainer criterion, optionally measured in upstream
  CI before release, never as receiver health.
- Leave fact/topic capacity and source-derived experiment bounds outside the RTBO deletion set; they
  count corpus organization or a particular experiment, not prose validity. Their owners still owe
  an explicit action at the threshold.

### E6: placement ledger before adversarial elimination

| Surface | Delete | Retain | Move / generate |
|---|---|---|---|
| committed `workspace/00-INDEX.md` | source file, freshness check, route, maintenance duty | historical snapshots/references | none |
| status collector | Full payload and workflow invocations | exact upstream implementation/conformance behavior | upstream maintainer command; optional CI artifact output |
| Knowledge Gate | Python command dependency | exact outcome algorithm and digest state | one addressed Full canonical range; upstream tests/reference consumer |
| project check | self-presence and ordinary workflow command | concrete init/update postconditions | inline to owning workflows; broader doctor upstream |
| task/trace diagnostics | summary/status prose-length errors | material structural/trace/project checks | upstream bounded doctor + pre-write prompt contract |
| migration | active `.tfw/scripts` placement | 2.0.0 guide, exact manifest/accounting invariants, history | versioned transient bundle at pinned upstream/release boundary |
| docs | top-level Tasks prominence and Full import dependency | compiled citation targets | docs-local upstream resolver; hidden task landings generated in CI |
| status page | committed/public default | capability to render read-only snapshot | explicit upstream CI artifact only when requested |
| Assisted | every RTBO-originating code/reference | existing prompt-first edition | nothing |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| C1/C6/C9 separate Full method authority from upstream executable ownership without weakening the exercised Knowledge Gate. | Attack semantic-read drift, workflow size, and indeterminate-input behavior. |
| A declared runtime can be acceptable for a transient crossed-major migration even when ordinary Full has none. | Decide whether absence must hard-stop or whether agent synthesis can ever be a default. |
| Diagnostic exit meaning requires audience plus applicability epoch; advice is not a degraded error. | Attack with the real 123 event, legacy forms, structural corruption, and incomplete scans. |
| Hidden landings solve the no-HL case without restoring a global task library. | Verify the placement recommendation does not smuggle a public portfolio back through CI. |
| The preliminary ledger identifies exact deletion, retention, movement, and CI-generation effects. | Challenge each survivor on value, maintenance cost, and frozen DoD/DoF. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?

Stage complete: YES
→ User decision: Prior autonomous-run direction applied; close Extract and attack C1/C6/C9 plus the versioned migration boundary in Challenge.
