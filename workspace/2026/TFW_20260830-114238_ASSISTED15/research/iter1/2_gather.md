# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> **Test:** "Can I name every dimension and its alternatives without checking my sources?"
> Parent: [HL-TFW_20260830-114238_ASSISTED15](../../HL-TFW_20260830-114238_ASSISTED15.md)
> Goal: Deliver a standalone, organizationally neutral Assisted 1.5 whose lifecycle, identity, update discipline, and practical templates are derived from the read-only Innoforce field lineage and maintained through an explicit public-core/private-overlay boundary.

## Dimensions

Each path or release operation must choose one alternative in every dimension. Alternatives remain open until Challenge.

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1: Path authority | public-core owned | stock but project-customizable | downstream-only overlay/state | retired or quarantine-only |
| D2: Direction model | public → downstream only | symmetric two-way mirror | asymmetric forward update + reviewed reverse promotion | generate both distributions from a third source tree |
| D3: Baseline proof | version label only | per-file SHA-256 manifest | retained three-way base snapshot | signed/tagged release manifest |
| D4: Mutation primitive | whole-directory replacement | hash-gated per-file replacement | three-way text merge | manual reconstruction/new-file-only |
| D5: Persistent participant state | package/shared project | conventional per-user state directory | explicitly proven non-shared path with fail-closed fallback | session-only state |
| D6: Template ownership | service-owned and overwritten | stock-hash protected customization | neutral semantic template + downstream brand overlay | downstream-only templates |
| D7: User-facing language authority | Russian source of truth | English source of truth | independently maintained bilingual copies | language-neutral mechanism + localized overlays |
| D8: Orchestration capability | manual lifecycle only | capability-detected autonomous mode + manual fallback | mandatory Codex task operations | external human/coordinator orchestration |
| D9: Release-history authority | copy field changelog literally | public Assisted history only | public history with separately labelled field provenance | history generated from repository tags |

## Findings

### G1 — OODA Loop 1: package and lineage topology

**Observe.** Read-only manifests were computed from relative path, byte size, and SHA-256. No field file was written or executed.

| Tree | Files | Canonical tree digest | Relevant delta |
|---|---:|---|---|
| Public `editions/02-assisted` | 9 | `e2c650323adf5a28950229407c0d7950d0d66597d7902ba3144941755968c37d` | Baseline product |
| Field 1.2 | 23 | captured during the stage | Adds versioning and initial skills |
| Field 1.3 | 29 | manifest inspected | 6 paths added; stable task lifecycle introduced |
| Field 1.4 | 26 | manifest inspected | 3 hook paths removed |
| Field 1.5 | 29 | `7e2248a7f7e77161644d8394b1557c731e0b5b31d7713843de30655b6e4fadc3` | 3 identity paths added; 15 of 26 shared paths changed from 1.4 |

Public → field 1.5 has 6 shared paths and all 6 differ; 23 paths are field-only and the 3 public-only paths are the lifecycle hook payload. The public hook files exactly match the three 1.2 stock hashes recorded by the field changelog, so their removal can be proven path-by-path rather than inferred from names.

The 1.5 tree is mechanically clean of project-instance state: `VERSION=1.5`, zero `work/`, zero human-profile files, zero UUID `project_id` values, and zero initialized-project markers. It is not organizationally neutral for a public release. A current case-insensitive union scan for already-known organization/environment markers hits **14 text files**, not the 12 stated in HL §2; four organizational records and one branded binary asset are also present. No private facts were copied into this trace.

**Orient.** The field changelog uses “clean/neutral” to mean an internally distributable, unpersonalized Innoforce starter. The public HL uses “neutral” to mean no Innoforce context at all. Both claims can be internally coherent only if the narrower field meaning is not reused as the public acceptance definition.

**Decide.** Treat field 1.5 as a mixed evidence distribution, never as a public release candidate. Retain its exact tree digest as the research baseline and classify behavior independently from wording, records, examples, and assets.

**Act.** Add path authority, baseline proof, release-history authority, and template ownership as independent dimensions.

### G2 — Field behavior ledger

The five skills, identity implementation, root contracts, migration/changelog, participant schema, and template inventory were inspected. This exceeded the 15-file soft reading ceiling because the frozen claim is “fully 1.5” and the leak/update risks cannot be tested from a sample. The write set remained one stage file.

| Surface | Field-proven candidate | Coupling or contradiction | Gather classification |
|---|---|---|---|
| Lifecycle | plan → separate handoff → independent review → human acceptance; stable task folder; explicit manual/autonomous choice | Exact task creation/naming/report operations are runtime-specific; field retry creates new handoff/review tasks, while the owner requested one reusable session per role per phase | Universal lifecycle candidate; orchestration adapter remains capability-bound |
| Identity | current participant, corporate role, project role, task owner, and AI role remain distinct; no silent first-profile selection; surname collision fails closed | Corporate-role vocabulary and provider markers are embedded; local-store safety is not fully proven on every OS | Preserve separation and collision semantics; generalize role/environment labels and strengthen locality proof |
| Update | whole source is checked statically; service/protected manifests; one gate; pre/post hashes; version-specific migrations; no source code before approval | `шаблоны/` is in the wholesale service replacement set even though the frozen public contract requires customized-template preservation | Updater contract is evidence, not directly reusable policy |
| Hooks | Manual order is authoritative; hooks were removed after timeout/hang evidence | Public 1.0 still ships the exact known stock payload | Retired path class; exact-hash removal evidence exists |
| Templates | Note, work plan, A4 document, presentation, deterministic A4 builder, and an asset form a real result-producing set | Several contain organization/city/brand markers; the asset is branded; no public-neutral fixture has yet been rendered | Semantics are public candidates; examples/style/assets require neutral reconstruction |
| Knowledge | Trace remains primary; candidates and verified records are distinct; no automatic consolidation claims | The distribution contains actual organization records and a populated index | Navigation/schema candidate only; records are downstream-only |
| Release history | Exact 1.2→1.5 migration maps and stock hashes provide valuable provenance | 1.1 is an Innoforce-only release and later releases were not public Assisted releases | Public history and field provenance must remain visibly separate |

### G3 — OODA Loop 2: external primary-source constraints

**Observe.** Nine focused web queries were used, exceeding the five-query soft ceiling because the stage had independent source-control, synchronization, OS-state, filesystem-atomicity, and Codex-capability claims. Only primary/official documentation informed the technical findings.

| Topic | Primary evidence | Consequence |
|---|---|---|
| Non-mutating comparison | Official Git documentation states that `git diff --no-index` compares two filesystem paths, including directories, and implies an exit status: [git-diff](https://git-scm.com/docs/git-diff) | A read-only directory comparison is feasible without making either tree a Git repository, but it does not assign path authority or make an update safe by itself |
| Three-way merge | Official Git documentation requires current, base, and other inputs; overlapping edits produce conflicts, and `--stdout` avoids overwriting the current file: [git-merge-file](https://git-scm.com/docs/git-merge-file) | Three-way merge is an optional text-file primitive only when a trusted base exists; it is not a binary/template policy and conflicts still need a decision |
| Synchronized-folder behavior | Google documents that differing local/cloud content can be kept as both files and that incompatible cloud/local changes can leave an edited copy or Lost & Found item: [stream/mirror](https://support.google.com/drive/answer/13401938?hl=en), [sync errors](https://support.google.com/drive/answer/2565956?co=GENIE.Platform%3DDesktop&hl=en-en) | A local post-read/hash detects only the visible local state. It cannot prove completed remote synchronization, exclusive writing, or a distributed transaction |
| Linux state locality | The XDG specification defines `XDG_STATE_HOME` as persistent user-specific state, but reserves an explicit “local and not shared” guarantee for `XDG_RUNTIME_DIR`: [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir/0.8/) | The field script's default `~/.local/state/tfw-assisted` is appropriately categorized as state, but the standard does not prove it is machine-local or unsynchronized |
| Windows state locality | Microsoft documents `FOLDERID_LocalAppData` as a per-user folder at `%USERPROFILE%\AppData\Local`: [KNOWNFOLDERID](https://learn.microsoft.com/en-us/windows/win32/shell/knownfolderid) | “Per-user” supports separation from the project but is not, by itself, proof that an operator has not redirected or synchronized the path |
| Local atomic replacement | Python documents that successful `os.replace` is atomic and can fail across filesystems: [Python `os.replace`](https://docs.python.org/3/library/os.html#os.replace) | The identity script has a defensible local-file replacement primitive because its temp file is in the same directory; this says nothing about cloud replication |
| Codex autonomy | Official OpenAI guidance describes multi-agent as a Responses API beta and stresses explicit autonomy/approval boundaries: [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model) | Inference: this is not a universal guarantee that every Codex desktop build exposes create/name/wait/read/continue operations. Runtime capability detection and manual fallback remain mandatory |

**Orient.** Local atomicity, per-user placement, synchronization completion, and multi-agent availability are four different claims. The field contracts usually state those boundaries honestly, but the Linux default-path implementation makes a stronger machine-local assumption than the XDG specification supports.

**Decide.** H1 is **conditionally supportable**, not confirmed: the behavioral identity contract can be extracted only if the public implementation refuses persistent binding when non-shared locality is not demonstrated and falls back to session-only state. H2 is **narrowed**: classified manifests plus non-mutating comparison are sufficient for planning and gating, not for applying a safe update without a trusted baseline and per-class mutation rule.

**Act.** Add persistent-state locality, mutation primitive, and orchestration capability as separate dimensions; carry Linux/macOS locality proof and runtime task-operation detection into Extract/Challenge.

### G4 — OODA Loop 3: counter-evidence and contradictions

**Observe.** The following counterexamples were actively sought rather than inferred from the desired architecture.

| # | Claimed or tempting interpretation | Counter-evidence | Effect |
|---|---|---|---|
| C1 | “Clean 1.5” can be copied as public-neutral | 14 marker-bearing text files, populated organization records, and a branded asset coexist with mechanically clean project state | Neutralization must be semantic and path-classified, not a marker-only copy filter |
| C2 | Field `/tfw-update` already protects templates | Its service set replaces the whole template directory, while public DoD 8 requires preservation of customized templates | A public updater needs stock-hash/customizable rules or a split stock/overlay layout |
| C3 | `XDG_STATE_HOME` proves machine-local binding | XDG defines persistent user state there but does not require it to be local/non-shared | Unknown locality must reject persistence or use a user-proved safe location/session-only fallback |
| C4 | A local post-hash proves a safe Drive write | Google documents asynchronous propagation, incompatible changes, duplicate copies, and Lost & Found recovery | Shared-write checks can detect some races but cannot promise remote completion or transactional safety |
| C5 | The field updater supplies both maintenance directions | It supplies downstream installation/migration only; no reverse promotion authority or sanitization contract exists | Reverse promotion is a new public maintenance process, not a renamed update operation |
| C6 | Autonomous orchestration is universally available | Field plan itself requires capability detection; official public material found in this stage does not establish the exact desktop task-control surface | Manual mode is the portable baseline; autonomous mode is conditional |
| C7 | Every 1.5 field behavior is a universal invariant | Exact organization role labels, Google Drive wording, house templates, and “new task per retry” session policy are downstream choices | Extract invariants at claim level; do not preserve accidental implementation shape |
| C8 | `VERSION=1.5` alone makes every visible version claim coherent | Field `PROJECT.md` keeps a separate compatibility marker at edition version 1.0 while the service package is 1.5 | Public documents need one explained version authority and must not appear to be simultaneously 1.0 and 1.5 |

**Orient.** The highest-risk failures come from collapsing two layers: service versus project customization, local filesystem versus distributed synchronization, and universal behavior versus field-specific operating policy.

**Decide.** The core/overlay boundary must be declared per path and per direction. A path cannot be “bidirectional” without a named authority, baseline, and operation. The current field package and updater cannot be copied verbatim under the frozen DoD/DoF.

**Act.** Preserve all nine dimensions for Extract and require pairwise configuration checks in Challenge.

### G5 — Initial path-class candidates

This is an input classification for Extract, not a final recommendation.

| Candidate class | Paths/surfaces | Why |
|---|---|---|
| Public core | neutral root contracts; lifecycle skill contracts/metadata; identity contract/implementation; version/changelog schema; participant and knowledge navigation schemas | Universal behavior or public release authority |
| Stock but customizable | project card and AI-role configuration blocks; practical templates and presentation/document styling | Installed projects legitimately personalize these surfaces |
| Downstream-only | organization records, human profiles, project UUID, tasks/traces/results, local bindings, company defaults, company brand assets | State or context owned by a specific installation/organization |
| Retired/quarantine-only | legacy TFW lifecycle hook registration/adapters and customized copies preserved only for recovery evidence | Field lineage removed the mechanism; public source hashes are known |

### G6 — Hypothesis status after Gather

| Hypothesis | Gather result | Evidence state |
|---|---|---|
| H1 | Conditional support | Five-field separation and local atomic primitives survive; default non-shared locality is not proven on all platforms |
| H2 | Narrowed | Manifest + read-only diff supports comparison/gating; safe mutation additionally requires trusted baseline and per-class rule |
| H3 | Partial support | Six useful template categories are structurally separable from records/branding; full semantic neutralization and render evidence remain open |
| H4 | Open | Russian is the coherent field baseline, but maintenance cost versus a language-neutral/localized split has not yet been compared |

### G7 — Gather-stage decisions

1. Use the field 1.5 tree as read-only evidence with digest `7e2248…fadc3`, not as a copy source whose “neutral” label is trusted.
2. Treat forward update and reverse promotion as separate operations with separate authorities; do not model them as a symmetric sync toggle.
3. Treat local atomicity, non-shared persistence, cloud synchronization, and task-control availability as independent evidence obligations.
4. Treat the public hook payload as exact known stock eligible for evidenced removal, while preserving unrelated or modified `.codex` material in installed-project migrations.

### G8 — Open threads for Extract

- Produce the configuration space and determine the minimum manifest schema: path class, source authority, baseline hash, operation, direction, sensitivity, and postcondition.
- Determine whether customizable templates remain in place under stock-hash protection or split into immutable stock plus project/brand overlay.
- Test the identity implementation's macOS/default-store locality and provider-neutral shared-root handling; specify the safe fallback without weakening DoD 5.
- Define one public version authority and a truthful Assisted changelog shape without presenting field-only 1.1–1.5 milestones as public releases.
- Compare Russian-only authority against localized overlays under actual synchronization cost; H4 remains unresolved.
- Determine the reusable-session orchestration refinement consistent with the owner's “one coordinator/executor/reviewer per phase” direction and runtime capability detection.

### G9 — Recommendation classification

- **Refinements:** correct HL §2's marker-bearing text count from 12 to 14 for the current field digest; update §9 with the unproven Linux/macOS local-store locality risk; narrow H1/H2/H3 statuses in §10; add the absence of a reverse-promotion contract and the exact public-hook stock match to §8/§10.
- **Amendment proposals:** none. Every contradiction can be resolved inside the existing frozen DoD/DoF by strengthening implementation requirements; no phase, target-state claim, acceptance criterion, failure condition, or principle needs to change.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| Nine independent dimensions with 3–4 alternatives; exact public/field manifests and lineage deltas; all five skills plus identity code; six template categories; seven official primary-source topics; eight explicit contradictions | Build and eliminate configurations; finish template semantic/render analysis; verify safe local-store fallback and language/version authority |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?
- [x] Hypothesis tested?
- [x] Counter-evidence sought?

**Deep-mode exit:** 4 Gather decisions recorded; H1–H3 tested; counter-evidence recorded; three OODA loops completed.

**Metacognitive check:** New findings, not mere confirmation: the marker surface is 14 rather than 12 files; the Linux persistent-state default is not proven machine-local by XDG; the field updater would overwrite customized templates; reverse promotion does not exist in the field contract; and the public hooks exactly match the known 1.2 stock hashes.

Stage complete: YES
→ Phase Coordinator decision: recommend close Gather and proceed to Extract
