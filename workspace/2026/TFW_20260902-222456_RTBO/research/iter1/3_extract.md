# Extract — "What do we NOT see?"
> **Mindset:** Analyst. You have the raw findings. Now build structure. Make combinations visible that nobody proposed.
> Parent: [HL-TFW_20260902-222456_RTBO](../../HL-TFW_20260902-222456_RTBO.md)
> Goal: TFW keeps task state inspectable without a committed portfolio cache, a hard prose-length gate, or a runtime prerequisite.

## Configuration Space

The full cross-product has 16,384 combinations. The rows below retain every coherent architectural
family and vary at least one dimension from C1; combinations that require a committed cache, put
code into Assisted, or make an optional helper a mandatory lifecycle step are omitted as directly
contradictory to the frozen contract.

| Config | D1: ownership | D2: runtime contract | D3: lifecycle relationship | D4: output | D5: diagnostic severity | D6: documentation exposure | D7: compatibility ownership |
|--------|---------------|----------------------|----------------------------|------------|-------------------------|----------------------------|-----------------------------|
| C1 | optional utility shipped in Full | Python + declared PyYAML | explicit opt-in command | terminal/JSON read-only report | material errors plus separate advice | slim current-status page + compiled navigation-hidden traces | live utility retains old behavior |
| C2 | maintainer-only repository tool | documentation-CI environment only | no lifecycle reference | terminal/JSON + virtual CI page | structured per-class severity | slim current-status page + compiled navigation-hidden traces | versioned migration owns legacy behavior |
| C3 | shipped shared core + maintainer front end | Python + declared PyYAML for explicit utility only | no lifecycle reference | terminal/JSON from optional front end | material errors plus separate advice | compiled navigation-hidden traces | shared core owns identity/config; migration owns board history |
| C4 | no canonical executable code in Full; canonical prose contract in Full | environment-chosen agent tooling | no lifecycle reference | no aggregate output in Full | prose guidance in Full; structured maintainer findings | compiled navigation-hidden traces | versioned migration owns legacy behavior |
| C5 | maintainer-only repository tool | documentation-CI environment only | automatic advisory report in upstream CI only | virtual CI page + CI log | material build failures plus separate advisory report | top-level slim current-status page + compiled hidden traces | versioned migration owns legacy behavior |
| C6 | optional status-only utility in Full; maintainer doctor separate | Python standard library only for status listing | explicit opt-in command | terminal/JSON report | status tool reports input defects; doctor owns project QA | compiled navigation-hidden traces | migration and doctor keep separate compatibility adapters |
| C7 | optional packaged Full utility | Python + named optional dependency extra | explicit opt-in command | terminal/JSON report | material errors plus separate advice | top-level task library | live utility retains old behavior |
| C8 | maintainer-only collector and doctor | environment-chosen agent tooling for ordinary Full | no lifecycle reference | CI artifact only | one binary CI verdict on structural corruption only | no task index; compiled citation targets only | versioned migration owns legacy behavior |

C4 exposes a combination not proposed in the Briefing: make the algorithm and file contracts
canonical while allowing the receiving agent to choose or synthesize the executable mechanism; keep
the reference implementation only in the upstream repository. C8 exposes another: the generated
portfolio may be retained as a CI artifact for maintainers without becoming a public documentation
page at all.

## Findings

### E1: shipping, depending, and invoking are independent decisions

H2 contains a valid conditional statement but not a value argument. A Full payload can contain an
optional Python file without requiring Python if and only if all four conditions hold:

1. no normal workflow invokes it unconditionally;
2. the file reports a missing interpreter/dependency only after explicit helper use;
3. a complete agent-readable procedure exists for the lifecycle outcome; and
4. tests exercise a receiving project where the helper cannot run.

The current repository satisfies none of conditions 1, 3, or 4 for plan/knowledge/init/update.
Declaring PyYAML would fix dependency honesty for an explicit invocation, but would not make the
mandatory calls optional. Conversely, moving the file out of `.tfw/` would remove the dependency
from receiving projects, but would break current consumers until the resolver/digest/migration jobs
are reassigned.

The useful distinction is:

```text
Full method contract (must always work)
    ├── agent-readable state/discovery procedure
    └── optional executable accelerator (may be absent)

upstream repository QA (may require a declared development environment)
    ├── doctor/reporting front end
    ├── documentation compiler
    └── conformance and migration tests
```

The Python packaging specification shows one robust way to communicate an optional dependency, but
TFW is copied as files rather than installed as a Python distribution. C7 would therefore add a
packaging product solely to make one convenience honest. That cost exists even before evaluating
whether the convenience is valuable.

### E2: a split is needed, but a shipped code core is not the only split

The module boundary should follow stable responsibility, not the current import graph. Three kinds
of contract are visible:

| Contract kind | Stable subject | Candidate owner |
|---|---|---|
| Method/data contract | task identifiers, task containers, `status.md`, journal shape, selected knowledge headings | Full prose/templates; never maintainer-only |
| Receiver convenience | portfolio/status aggregation | optional Full utility only if independently justified |
| Upstream product assurance | installation consistency, canonical-copy drift, current corpus health, docs build | maintainer tooling / bounded doctor |
| Historical compatibility | pre-2.0 board parsing and migration accounting | versioned migration route, not a permanent lifecycle dependency |
| Publication projection | copying trace pages, resolving citations, optional task/status page | documentation build tooling |

This separation permits C2/C4/C5/C8 without duplicating authority: the prose/schema remains the
canonical Full contract, while executable implementations are consumers. "One parser" need not mean
"one file shipped to every receiver"; it can mean one implementation per deterministic product
boundary, tested against the same canonical cases. Whether that test contract is sufficient to
prevent drift remains a Challenge question.

### E3: diagnostic severity follows consequence and compliance timing

The current branches fall into four classes:

| Class | Examples in current code | Consequence | Candidate behavior |
|---|---|---|---|
| Structural integrity | duplicate whole identifier; malformed recognized `status.md`; ID/directory disagreement; undeclared lifecycle without verbatim value; terminal state without outcome; live phase without state | authority cannot be selected or its claim is internally contradictory | material finding; non-zero in an explicitly requested health check |
| Trace integrity | malformed current event shape; missing accountable human; filename/body kind mismatch; half transition; invalid ref container | event cannot be attributed or interpreted safely | material when the violated rule existed at write epoch; otherwise compatibility note |
| Project consistency | version mismatch; missing creation container/team; machine-local provenance; configured command naming a missing file | installation cannot perform a declared operation portably | material in init/update/maintainer QA; not a task-state verdict |
| Advisory authoring | summary over 120; likely title/goal/value/outcome length bounds | no authority loss or observed consumer failure; the writer may already have completed an immutable act | advice only; must not alter exit status |
| Compatibility information | legacy event name; stateless phases under terminal/stateless legacy tasks | expected historical form | note; deduplicated and exit-neutral |

Python's own warning model makes the semantic distinction explicit: warnings alert a user to a
condition that normally does not warrant terminating the program, and repeated warnings may be
suppressed. That supports a separate advice channel rather than one binary count in which a
three-character prose overrun is indistinguishable from duplicate identity.

Source: [Python `warnings` documentation](https://docs.python.org/3/library/warnings.html).

Two limitations prevent a final diagnostic contract in this stage. First, current `check_tasks`
does not call the only function that checks legal transition pairs. Second, applying today's strict
pre-write rules to all old immutable events can manufacture new historical defects. A bounded doctor
therefore needs an explicit read-time compatibility policy; it cannot simply invoke
`validate_new_event` over the corpus.

### E4: publication can preserve reachability while subtracting prominence

Compilation, link resolution, status projection, and navigation should be separate switches:

```text
task artifact source
    ├── compile page ─────────────────────> citation target remains reachable
    ├── add to generated task index ─────> optional discovery surface
    └── add index to global navigation ──> prominence choice
```

The smallest reachability-preserving change is to keep compiling task pages and resolving links but
remove the top-level `Tasks` item. A second independent change can replace the current all-artifact
index with a compact current-status projection. A third can retain that projection only as a CI
artifact. GitHub documents build artifacts as files produced by a workflow for deployment,
debugging, or later viewing, distinct from dependency caches; this is an established place for a
generated report that should not be committed.

Source: [GitHub Actions workflow artifacts](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts).

No repository evidence establishes readership or decisions caused by the current top-level task
library. The evidence does establish that compiled pages are required by live references. Therefore
H3's reachability half is supported; the claim that a public current list helps orientation remains
plausible but unmeasured.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| H2 is technically feasible only under four testable conditions; it does not establish that a shipped collector earns its payload and maintenance cost. | Attempt to break the strongest non-shipped and split designs with Knowledge Gate, migration, and clean-receiver cases. |
| Canonical prose/data contract plus maintainer implementation is a real split-core alternative; shared executable code is not required for shared authority. | Determine the minimum conformance cases needed to prevent parser drift if implementations separate. |
| Structural, trace, project, advisory, and compatibility findings require different severity and context. | Define the safe treatment of immutable current-grammar events that predate stricter pre-write validation. |
| Trace compilation and citation resolution can survive removal of the top-level task library. | Decide whether the current-status page is public, CI-only, or omitted pending evidence. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Configuration Space built from Gather dimensions?

Stage complete: YES
→ User decision: Prior autonomous-run direction applied; proceed to adversarial checks without changing implementation or the HL.
