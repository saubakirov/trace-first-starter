# Challenge — "What do we NOT expect?"
> **Mindset:** Critic. You built the configurations. Now attack them. Every survivor needs evidence. Every elimination needs a reason.
> Parent: [HL-TFW_20260902-222456_RTBO](../../HL-TFW_20260902-222456_RTBO.md)
> Goal: TFW keeps task state inspectable without a committed portfolio cache, a hard prose-length gate, or a runtime prerequisite.

## Consistency Check

**Incompatible pairs:**

| Dimension A | Alternative | Dimension B | Alternative | Why incompatible |
|------------|-------------|------------|-------------|-----------------|
| D1: ownership | optional utility shipped in Full | D3: lifecycle relationship | mandatory workflow step | Optionality is false when an ordinary lifecycle hard-stops without the utility. |
| D1: ownership | maintainer-only repository tool | D3: lifecycle relationship | mandatory workflow step | A receiving Full project cannot invoke a tool it does not receive. |
| D2: runtime contract | documentation-CI environment only | D3: lifecycle relationship | any ordinary Full invocation | The declared runtime exists only in upstream CI. |
| D2: runtime contract | Python standard library only | D5: diagnostic severity | semantic validation of the present YAML carriers | YAML 1.2 includes scalar, collection, alias, and tag behavior not provided by the Python standard library; a regex subset is not the current data contract. |
| D4: output | committed Markdown cache | D3: lifecycle relationship | any routine use | The cache recreates the shared maintenance duty forbidden by the frozen contract. |
| D5: diagnostic severity | one binary verdict containing advice | D5: diagnostic severity | advisory prose length | Advice becomes indistinguishable from authority corruption and repeats the 123 failure. |
| D6: documentation exposure | no task pages | D6: documentation exposure | citation-reachable task traces | A resolved citation needs a generated target page, though it does not need global navigation. |
| D6: documentation exposure | top-level task library | D6: documentation exposure | only demonstrably useful traces remain prominent | No observed use or decision justifies making 1,307 task files a primary documentation product. |
| D7: compatibility ownership | live utility retains all old behavior | D4/D5 | no committed index and no hard 120 finding | Retaining writer/freshness/length behavior contradicts the task rather than preserving compatibility. |

**Surviving configurations:**

No Extract row survives unchanged. The following corrected forms survive the attacks:

| Config | D1: ownership | D2: runtime contract | D3: lifecycle relationship | Notes |
|--------|---------------|----------------------|----------------------------|-------|
| C4* | canonical prose/data contract in Full; no active executable dependency | environment-chosen agent tooling | no mandatory helper reference | Change C4's output from "none" to an ephemeral aggregate/digest map when the method requires one; prove it against conformance fixtures. |
| C8* | upstream-only collector/doctor/docs implementation | declared maintainer/CI environment | no Full lifecycle reference | Replace the binary bucket with per-class material/advisory/compatibility results and give Full a complete Knowledge Gate procedure. |
| C4* + C8* | Full owns the method; upstream owns the reference implementation | separate receiver and maintainer contracts | Full outcome is tool-independent | Board migration remains a versioned, explicitly invoked compatibility tool rather than an active lifecycle dependency. |

**Unexpected survivors:**

- **C4* + C8*:** A canonical executable is not necessary in every receiving project if the Full
  workflow owns a complete result-oriented procedure and the upstream implementation is tested as a
  consumer of the same conformance corpus.
- **CI-only portfolio artifact:** A current list can exist for upstream maintenance without becoming
  either a committed source or a public navigation destination. This preserves the option while its
  reader value is unproved.

## Findings

### C1: immediate relocation breaks three products

The strongest counterexample to a simple "move `gen_index.py` to maintainer tools" change is the
current dependency graph:

1. `/tfw-plan` and `/tfw-knowledge` hard-stop around `--knowledge-pending`.
2. `migrate_board.py` imports nine names from `gen_index.py`; a receiver crossing pre-2.0 loses its
   exact-accounting migration path.
3. `gen_docs.py` imports `gen_index.py` before building any page; upstream publication fails.

This does not justify keeping the monolith in Full. It proves that placement follows responsibility
extraction. The Knowledge Gate in particular is not a status list: it combines three identifier
grammars, configured containers, unmatched/collision refusal, selected-heading extraction outside
fences, LF normalization, tuple-framed SHA-256, prior-map validation, removed-task refusal, and
pending comparison. A prompt-only alternative must preserve that behavior or deliberately replace
it through a governed design.

An independent adversarial pass reached the same counterexample and found no C1–C8 row intact. Its
strongest surviving direction was the corrected C4*+C8* boundary above.

### C2: "standard-library parser" fails against the actual carrier

C6 is not a safe shortcut. The Full contract uses YAML, not a project-defined `key: scalar` subset.
The YAML 1.2.2 specification includes block and flow collections, multiple scalar styles,
anchors/aliases, and tags. Replacing PyYAML with hand-written line extraction would either be a new,
narrower carrier contract or a partial parser that can silently disagree with valid files.

Source: [YAML 1.2.2 specification](https://yaml.org/spec/1.2.2/).

The remaining choices are honest: declare PyYAML for an explicitly requested optional or maintainer
tool, or let the agent use whatever conforming parser exists in its environment. "No PyYAML" cannot
mean "parse less YAML without saying so."

### C3: the 123 rule can be removed without suppressing material branches

A direct read of the immutable event produced this controlled result:

| Case | Length treatment | Result |
|---|---|---|
| Actual 123-code-point event | ceiling raised only for the function call | no remaining event problem |
| Synthetic event without `on_behalf_of`, with empty refs and only `from` | same relaxed ceiling | four independent integrity findings remain |
| Synthetic `TODO -> DONE` transition | same relaxed ceiling, pre-write validation | illegal transition still reported |
| Synthetic status with missing authority, undeclared lifecycle, and wrong ID | no journal length involved | all three independent state findings reported |

This confirms H4's central separation: deleting the length assertion does not require silencing
other checks or editing the historical event. The useful schema analogy is the formal distinction
between assertions, which affect validity, and annotations, which carry useful information without
changing validation outcome. "Normally no more than 120" belongs to the latter class.

Source: [JSON Schema validation — assertions and annotations](https://json-schema.org/draft/2020-12/json-schema-validation).

The attack does expose a coverage gap: legal transition pairs, real timestamp validity, safe
relative refs, and summary type/one-line shape live only in `validate_new_event`; no production
writer invokes it and `--check tasks` uses the historical reader. A future doctor must not claim
those properties until it defines an epoch-compatible read check or a real pre-write integration.

### C4: citation reachability survives navigation subtraction, but one fallback is unsafe

Removing `nav["Tasks"]` and even the all-artifact `tasks/index.md` does not remove the task-page glob
or the reference resolver. MkDocs explicitly renders pages omitted from navigation and leaves them
available through direct links. Existing repository tests separately exercise page generation and
reference resolution, so the separation is testable.

Source: [MkDocs — configure pages and navigation](https://www.mkdocs.org/user-guide/writing-your-docs/#configure-pages-and-navigation).

One edge case needs new evidence: a bare task identifier without an HL falls back to a task-folder
URL. Some such folders have no generated index page. Citation reachability must therefore be proved
for hidden pages and no-HL bare identifiers; the current "10+ task pages" test is insufficient.

No evidence shows that a public current-status page changes reader decisions. The safe first
boundary is compiled citation targets with no global Tasks prominence. A current list may be emitted
as an upstream CI artifact; public promotion should wait for evidence or an explicit owner product
choice.

### C5: hypothesis disposition after attack

| Hypothesis | Iteration-1 disposition | Grounds |
|---|---|---|
| H2 | **conditionally supported, not selected** | Full can ship an optional utility only after all lifecycle paths work without it and dependency absence is isolated to explicit invocation. Current Full does not. H1 supplies no value case for shipping the status collector, so feasibility alone is insufficient. |
| H3 | **partly supported** | CI generation and citation-reachable hidden traces are proven separable from source commits and global navigation. The value of a public current-status list is unmeasured. |
| H4 | **supported for the 120 separation; incomplete for doctor scope** | The 123 event becomes quiet while independent synthetic structural defects remain visible. Existing entry points still miss or fragment several claimed material checks. |

## Checkpoint

| Found | Remaining |
|-------|-----------|
| The corrected C4*+C8* boundary best matches owner intent and removes ordinary Full runtime dependence. | Prove a complete environment-neutral Knowledge Gate procedure and its conformance corpus. |
| The 120 limit can safely become prompt guidance without a historical exception. | Decide whether other prose bounds are assertions or advice; define event-era compatibility for doctor checks. |
| Compiled trace pages can remain citation targets without global task navigation. | Test hidden-page links, bare IDs without HL, and decide whether any status list earns public rather than CI-only exposure. |
| The one-time migration must be separated before the live monolith moves. | Decide how a pre-2.0 receiver obtains and runs the versioned migration tool when Python/PyYAML is unavailable. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Pairwise incompatibility checked? Surviving configurations listed?

Stage complete: YES
→ User decision: Prior autonomous-run direction applied. Iteration 1 is ready for synthesis; the mandatory second iteration should attack the four remaining proof obligations rather than repeat the inventory.
