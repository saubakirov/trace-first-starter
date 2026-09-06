# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260902-222456_RTBO](../../HL-TFW_20260902-222456_RTBO.md)
> Goal: TFW keeps task state inspectable at scale without a committed portfolio cache, a hard prose-length gate, or a runtime prerequisite.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1: Full executable ownership | no executable; outcome-only workflow | optional collector | shipped shared parser/core | mandatory helper |
| D2: carrier interpretation | agent semantically reads YAML | environment-selected conforming YAML processor | PyYAML reference implementation | narrow line/regex parser |
| D3: Knowledge Gate mechanism | explicit no-helper algorithm | ephemeral environment-chosen accelerator | shipped command | gate removed |
| D4: pre-2.0 migration delivery | active Full script | versioned in-payload compatibility bundle | immutable release asset/tag archive | agent-synthesized implementation from specification |
| D5: diagnostic applicability | latest grammar over all history | rule-by-introduction epoch | durable syntax/shape epochs | no historical diagnostics |
| D6: documentation exposure | public top-level task library | compiled hidden trace pages plus valid task landings | CI-only status artifact | no task projection |
| D7: prose constraint behavior | validity/error | prompt guidance | projection-local truncation/wrapping | no constraint |

## Findings

### G1: a complete no-helper Knowledge Gate is executable, but not as a shell-regex recipe

The current command on the real repository returned one pending identity and no unresolved input:

```text
pending_task_ids = [TFW_20260902-222456_RTBO]
problems = []
removed_task_ids = []
migration_required = false
exit = 0
```

An independent PowerShell/.NET calculation used no Python, PyYAML, or shipped helper. It implemented
the canonical identifier grammars, one-level year expansion, selected artifact/heading rules, fence
exclusion, LF normalization, UTF-8 plus NUL tuple framing, SHA-256, full-map reconciliation, and the
no-arithmetic-on-problem rule. Results matched the Python implementation byte-for-byte:

| Case | Independent result | Reference result |
|---|---|---|
| real RTBO task digest | `d29d4cab84f8b43a3de0fa838f6525b4b2c5c07272587eecc1dca06f9f072ef5` | same |
| fenced-heading fixture | selected only `Fact Candidates` and outside-fence `Strategic Insights (Research)` | same |
| fenced-heading digest | `f39b63471b8921f445b93b4857d940142adaaa1b1fcebad8a8edefa09d1b18f7` | same |
| changed selected body | `1fadcc14d7d169afd7239a2395e0ce51fd11bfd75c5b9f770c1f7037588d7cf4` | same; differs from baseline |
| no selected section | `96a296d224f285c67bee93c30f8a309157f0daa35dc5b87e410b78630a09cfc7` | same explicit empty-tuple digest |
| identical prior map | zero pending | zero pending |
| removed prior identity | named `TFW-2`; threshold forbidden | same policy |
| malformed/collision input | named problem; pending cleared; threshold forbidden | same policy |

The existing reference conformance cases also passed: **13 passed** for K0–K9, LF/unselected
artifact handling, malformed paths, and whole-identifier collisions. This covers absent state-map
migration, equal-timestamp identities, retry before state write, changed and late sections, removed
tasks, empty tasks, soft/hard/off thresholds, and write-free failure.

The complete no-helper procedure is therefore a result algorithm, not a command name:

1. Semantically read `tfw.task_containers`, `tfw.knowledge.gate_mode`, `interval`, and
   `knowledge.processed_task_digests`; validate their types and every 64-lowercase-hex value.
2. Resolve only the three whole identifier grammars across direct container children and one
   creation-year level; refuse duplicate identities and report every unmatched directory.
3. For each resolved task, sort eligible `HL`, `RF`, `REVIEW`, and `RES` Markdown paths by repository
   POSIX path.
4. Select each `Fact Candidates`, `Strategic Insights`, `Strategic Session Insights`, and
   `Execution Session Insights` section outside backtick or tilde fences; remove only an optional
   section number and the `🟢 FREE` suffix; keep the actual selected heading text.
5. Normalize CRLF/CR to LF and retain every other body byte and trailing newline. Hash sorted
   `(path UTF-8, NUL, heading UTF-8, NUL, body UTF-8)` tuples with SHA-256; hash `NUL,NUL` for an
   empty task.
6. Build the complete current map before comparison. A read failure, malformed path, collision,
   invalid prior key/digest, or removed prior identity is a hard stop; no pending count is valid.
7. With no problem, `migration_required` means an absent digest map and makes every current task
   pending. Otherwise pending is the sorted set whose digest differs from its prior digest.
8. Apply `off`/`soft`/`hard` and the distinct-pending count exactly; zero is a no-op and hard routes
   only at `delta >= interval`.
9. During consolidation, retain the approved batch universe, re-run steps 2–6 after source-marker
   changes, and refuse a changed universe or unresolved input.
10. Write the validated merged digest map **last**; before that write the previous state remains
    byte-identical, so retry converges.

SHA-256 itself is a portable byte-level standard, not a Python behavior; NIST specifies it as a
message-digest algorithm, and the independent .NET implementation used UTF-8 bytes and SHA-256 in
the documented way. Sources: [NIST FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final),
[Microsoft .NET hash guidance](https://learn.microsoft.com/en-us/dotnet/standard/security/ensuring-data-integrity-with-hash-codes).

One attempted shortcut produced useful counter-evidence. A PowerShell regex read of the real YAML
falsely reported a version mismatch (`"2.1.0"` versus `2.1.0`), falsely found retired
`review.default_mode` inside a later block, and treated a comment token as a missing build path.
YAML 1.2 is a complete serialization language with mappings, sequences, multiple scalar styles,
aliases, and tags; presentation text is not the representation. A canonical no-helper workflow must
therefore require semantic YAML reading by the acting agent or any conforming parser available in
its environment. It must not ship a regex parser disguised as portability. Source:
[YAML 1.2.2 specification](https://yaml.org/spec/1.2.2/).

### G2: exact migration is proven with its current environment, not without it

The current migration suite passed **64 tests, 1 skipped**. It covers every-row visibility,
whole-identifier parsing, collisions before writes, source-board revision pinning, byte preservation,
exact accounting guarantees, refusal of ambiguous lifecycle cells, stateless phases, dry run,
non-overwrite, snapshot fidelity, and repository accounting.

Delivery and execution separate sharply:

| Receiver condition | Observed behavior | Meaning |
|---|---|---|
| normal repository environment | 64 passed, 1 skipped | current implementation has strong exactness evidence |
| Python with site packages disabled | `python -S ...migrate_board.py --help` exits 1 at import with `ModuleNotFoundError: yaml` | even help and dry run require undeclared PyYAML transitively through `gen_index.py` |
| no Python | the Python entry point is unavailable by construction | source delivery does not equal executable availability |
| tagged source | both `v2.0.0` and `v2.1.0` contain the guide, `migrate_board.py`, and `gen_index.py` | a tag can recover a versioned implementation, but it also recovers that release's defects and dependency boundary |

The dependency declaration is only `docs/requirements.txt`, so a receiver copying Full is not told
how to satisfy it. The present active-payload location is also permanent even though the act occurs
once. Conversely, an agent-synthesized migration is available in more environments but cannot claim
exact accounting merely because it prints balanced totals; it needs the same conformance corpus and
manifest invariants before write.

A safe versioned path can be distributed independently of active lifecycle tooling. GitHub releases
are tag-based deliverable iterations, and immutable releases lock the tag and assets and add an
attestation including tag, commit SHA, and assets. That makes a version-specific migration bundle
obtainable and verifiable without making it ordinary Full runtime. It does **not** make Python appear
on a no-Python receiver. Sources: [GitHub releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases),
[GitHub immutable releases](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases).

### G3: diagnostic epochs can quiet the real 123 event and keep structural failures non-zero

The real repository's current task check exits 1 for exactly one problem: the immutable
`20260902-181437__amendment_escalated__531a.md` summary is 123 code points against 120. Seventeen
stateless historical phase directories are already exit-neutral notes. With only the numeric length
assertion removed, the real event has **zero** remaining findings.

Controlled counterexamples produced:

| Event/status case | Proposed class | Observed independent findings with length ignored |
|---|---|---|
| real current-shape 123 event | advisory prose | none; exit 0 |
| legacy two-part event with `actor`, no `on_behalf_of` | compatibility | none; legacy form remains readable |
| current event lacking `on_behalf_of`, empty `refs`, and half transition | trace integrity | missing accountability, missing/empty refs, incomplete transition; non-zero |
| new current event with `+15:00`, escaping ref, and `TODO -> DONE` | pre-write trace integrity | invalid offset, task escape, illegal transition; refused before installation |
| status with long title/goal/value/outcome only | advisory prose | only four current length findings; none when bounds are removed |
| same status with empty authority, wrong ID, nonterminal outcome | structural integrity | all three remain when every prose-length branch is removed |

The durable applicability model is shape/contract based:

- **Legacy epoch:** an event identifiable by its durable legacy filename/fields is parsed under the
  schema that could have produced it; legacy differences are notes, not repair demands.
- **Current structural epoch:** current filename/body shape requires attributable human, interpretable
  kind/time/ref/transition structure; objective corruption is material. New-write-only rules run
  before installation and are not silently imposed on old immutable bytes.
- **Post-RTBO policy:** prose-length preferences are declassified across every epoch because they
  protect no authority or consumer. This is not an exception for one event; the assertion disappears.

Warnings are conventionally appropriate for useful conditions that do not normally warrant
termination; that supports a separate advice channel rather than an error count. Source:
[Python warning control](https://docs.python.org/3/library/warnings.html).

### G4: hidden trace navigation works; the current no-HL bare fallback does not

A clean `HEAD` archive was patched only to omit `nav["Tasks"]`, then built as a temporary MkDocs
projection. The build produced **1,284 task `index.html` pages**, the top navigation contained zero
`Tasks` entries, a representative cited phase RF existed, and the knowledge page containing the
reference existed. This practically confirms that trace compilation and direct citation reachability
do not depend on global task prominence. MkDocs documents the same behavior: pages omitted from
navigation are still rendered and become hidden unless directly linked.

The adversarial no-HL case failed. `knowledge/process.md` contains bare `TFW-57`; the resolver emitted
`../tasks/TFW-57__artifact_growth_control/`, but that folder has no generated `index.html` even though
its proposal page exists. Hiding navigation neither causes nor repairs this bug. A stable hidden
task landing (or a deterministic link to a real compiled artifact) is required before broad
navigation is removed.

Sources: [MkDocs pages and navigation](https://www.mkdocs.org/user-guide/writing-your-docs/#configure-pages-and-navigation).

A current portfolio was also rendered to `E:\TEMP\tfw-rtbo-ci-portfolio.md`: 18,249 bytes, 135 lines,
21 state files, 61 snapshot rows, and 3 unresolved inputs; Git status was unchanged. This proves a
build artifact is feasible, not that anyone values a public list. GitHub defines workflow artifacts
as run-produced files retained for later viewing or downstream jobs, distinct from dependency caches.
The CI-only form therefore preserves optional maintainer visibility without source churn or public
prominence. Source: [GitHub Actions workflow artifacts](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts).

### G5: the remaining numeric prose bounds have no common justification

| Bound | Material consumer | Pre-write compliance point | Finding |
|---|---|---|---|
| journal `summary <=120` | none; not rendered | nominal template instruction, but no production writer calls the validator and history is immutable | remove config and validity branch; retain “brief, normally <=120” only as prompt guidance |
| status `title <=80` | old portfolio and docs heading | current planning can shorten before write | display concern, not state validity; use projection wrapping/truncation if ever needed |
| status `goal <=160` | old portfolio only | current planning can shorten before write | consumer leaves with the committed index; keep concise one-line guidance, no parser failure |
| status `value <=160` | no aggregate consumer found | current planning | pure authoring preference; no parser failure |
| status `outcome <=160` | old portfolio; release reads DONE state/artifacts, not a fixed-width field | close step can shorten | completeness matters more than arbitrary width; no parser failure |
| `lifecycle_verbatim <=80` | migration diagnosis/index/docs | migration currently truncates | actively conflicts with carrying the unknown source value verbatim; remove the bound and never truncate |
| `max_index_lines`, `max_index_facts_lines` | no executable reader | none | dead configuration; delete rather than soften |
| workflow `<=1200 words` | maintainer context-density objective | before canonical workflow commit | keep as upstream design guidance; if measured, measure only in maintainer CI, never receiver health |
| `max_facts_per_topic`, `max_topic_files` | knowledge organization/context capacity | consolidation plan before write | counts, not prose validity; retain only with an explicit split/approval action when reached |
| experiment `strengthened_max_added_words <=15` | source-derived evaluation comparison | experiment fixture creation | task-specific measured AC, not a universal prose rule; leave outside RTBO |

Deleting only `BOUNDS` length checks from the controlled status case left authority, identity, and
terminal-state contradictions observable. Length and integrity are therefore separable in status as
they are in journal events.

### G6: Assisted already has the required boundary

`editions/02-assisted` contains no active `gen_index`, `migrate_board`, `00-INDEX`,
`--knowledge-pending`, `tfw-doctor`, or `.tfw/scripts` lifecycle reference outside historical or
migration explanation. Its prompt-first contract explicitly rejects hidden Python/runtime/helper
dependencies. It does contain an unrelated user-facing A4 document-building template; RTBO has no
authority or reason to touch it. The required result is zero RTBO-originating lifecycle, diagnostic,
migration, collector, or docs code/reference copied into Assisted.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Independent non-Python hashing and reference tests match every exercised Knowledge Gate outcome, including the real task, fences, changes, empty sections, malformed input, collisions, removal, migration, and thresholds. | Challenge whether semantic YAML reading plus a conformance corpus is sufficient authority without shipped code; forbid regex pseudo-parsers. |
| Current migration exactness is strongly tested, but Python without PyYAML fails before help and no-Python cannot execute it. | Choose a versioned compatibility delivery whose explicit dependency does not leak into ordinary Full; state the no-runtime fallback honestly. |
| The 123 event becomes quiet while current structural counterexamples remain non-zero under shape/contract epochs. | Fix exit semantics and distinguish upstream doctor, pre-write refusal, compatibility note, and prose advice. |
| Hidden navigation preserves compiled citations; a real no-HL bare link is broken. | Require a hidden landing or deterministic real-page fallback before deleting global navigation. |
| Every remaining numeric prose bound is classified by consumer and compliance timing. | Decide which keys/checks are deleted, which become prompt guidance, and which belong only to upstream CI. |
| Assisted has no active RTBO lifecycle surface. | Preserve that zero-diff boundary through planning. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?

Stage complete: YES
→ User decision: Prior autonomous-run direction applied; close Gather and test the resulting configurations in Extract.
