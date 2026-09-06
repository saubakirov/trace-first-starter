# Gather — "What do we NOT know?"
> **Mindset:** Explorer. You're mapping unknown territory. Widen before you narrow. Every assumption is a question.
> Parent: [HL-TFW_20260902-222456_RTBO](../../HL-TFW_20260902-222456_RTBO.md)
> Goal: TFW keeps task state inspectable without a committed portfolio cache, a hard prose-length gate, or a runtime prerequisite.

## Dimensions

| Dimension | Alt A | Alt B | Alt C | Alt D |
|-----------|-------|-------|-------|-------|
| D1: ownership | optional utility shipped in Full | maintainer-only repository tool | shipped shared core plus maintainer front end | no canonical code |
| D2: runtime contract | Python + declared PyYAML | Python standard library only | environment-chosen agent tooling | documentation-CI environment only |
| D3: lifecycle relationship | mandatory workflow step | explicit opt-in command | automatic advisory report | no lifecycle reference |
| D4: output | terminal/JSON read-only report | virtual CI page | committed Markdown cache | no aggregate output |
| D5: diagnostic severity | one binary verdict | material errors plus separate advice | structured findings with per-class severity | prose-only guidance |
| D6: documentation exposure | top-level task library | slim current-status page | compiled but navigation-hidden trace pages | no task pages |
| D7: compatibility ownership | live utility retains all old behavior | versioned migration owns legacy behavior | shared parser owns only identity/config | prompt procedure reimplements compatibility |

## Findings

### G1: `gen_index.py` is six products sharing one import boundary

The 1,748-line, 81,393-byte module has these separable responsibility groups:

| Responsibility | Principal functions / entry point | Actual consumer |
|---|---|---|
| Project root, configuration, exact identifier discovery | `find_project_root`, `read_config`, `task_containers`, `_walk_containers`, `parse_identifier`, `sort_key` | every command; `migrate_board.py`; `gen_docs.py` |
| Task and phase state parsing | `declared_lifecycles`, `read_status`, `validate_status`, `iter_phase_dirs`, `read_phase_status` | index, task check, project check, docs task page |
| Journal naming and validation | `event_filename`, `validate_event`, `validate_new_event`, `read_journal` | index unresolved section, task check, tests; no production event writer calls `validate_new_event` |
| Committed portfolio projection | `collect`, `render`, `build`, `output_path`, default CLI, `--check index` | `workspace/00-INDEX.md` and its freshness check |
| Knowledge Gate digest | `selected_knowledge_sections`, `knowledge_pending`, `knowledge_gate_result`, `--knowledge-pending` | mandatory `/tfw-plan` and `/tfw-knowledge` instructions |
| Project-installation diagnosis | `check_project` | mandatory end of `/tfw-init` and `/tfw-update` |

The migration utility imports nine resolver/configuration names from the module. The documentation
generator imports the module unconditionally and uses task containers, exact identifier parsing,
sorting, lifecycle vocabulary, directory discovery, and status reading. Deleting the index writer
therefore does not identify which of the other five products should disappear.

The shipped Full script directory contains two production programs and two test modules: 247,540
bytes total, of which 132,644 bytes are production code. Assisted contains no `gen_index`,
`00-INDEX`, `.tfw/scripts`, or PyYAML reference; its live instructions explicitly forbid making a
runtime or executable helper a hidden ordinary-user dependency.

### G2: the current "optional" helper is operationally mandatory and dependency-incomplete

`gen_index.py` imports `yaml` at module import time, before argument parsing. The only tracked
dependency declaration is `docs/requirements.txt`; it belongs to the documentation builder, not to
the copied Full `.tfw/` payload. An interpreter launched without site packages produced
`ModuleNotFoundError: No module named 'yaml'` before `--check project` could run.

The live workflow text gives no no-helper route:

- `/tfw-plan` and `/tfw-knowledge` require `--knowledge-pending`; a non-zero result is a hard stop.
- `/tfw-init` and `/tfw-update` require `--check project`.
- ordinary repository work does not automatically execute `--check tasks`, but the module and
  changelog still call it a build gate in several current passages.

External dependency mechanics confirm that copying source does not install its imports. PyYAML's
own documentation requires a separate `pip install pyyaml`. The Python Packaging User Guide defines
optional dependencies as dependencies considered only when a named extra is explicitly requested;
this repository is not packaged and declares no such extra. Therefore "the file is optional" is not
an operational dependency contract by itself.

Sources: [PyYAML installation](https://pyyaml.org/wiki/PyYAMLDocumentation.html),
[Python Packaging User Guide — optional dependencies](https://packaging.python.org/en/latest/specifications/pyproject-toml/#dependencies-optional-dependencies).

### G3: the existing checks do not form one coherent doctor

Current read-only runs over the repository produced:

| Entry point | Result | What it establishes |
|---|---|---|
| `--check tasks` | exit 1 | one 123-code-point summary exceeds the configured 120 ceiling; 17 stateless legacy phase directories are informational |
| `--check project` | exit 0 | version/config, team presence, container shape, retired keys, provenance form, configured Python paths, and malformed resolved task status are consistent |
| `--knowledge-pending` | exit 0 | two task digests pending, no unresolved digest input |

Coverage is fragmented in consequential ways:

- unmatched task directories are reported by index collection and the Knowledge Gate, but not by
  `--check tasks`;
- duplicate resolved identifiers raise before a formatted `--check tasks` verdict;
- status identity, required fields, lifecycle vocabulary, terminal outcome, timestamps, and phase
  state are checked on read;
- journal filename/body shape, attribution, kind, time shape, refs-list shape, half-transitions, and
  summary length are checked on read;
- real timestamp validity, safe relative refs, token shape, declared transition endpoints, and legal
  transition pairs exist only in `validate_new_event`, which no production writer calls;
- neither the current report nor the pre-write function establishes full journal lineage continuity.

Thus H4 cannot be proved by simply deleting the summary branch and renaming `--check tasks` to
doctor. Material findings can be separated from prose advice, but the desired examples are not all
currently observable through one report.

### G4: the documentation has four distinct task surfaces

The current build combines surfaces that can be changed independently:

1. It compiles every Markdown file under every task container into a page. The present corpus has
   1,307 such source files.
2. It resolves task/artifact citations to those compiled pages; at least 43 non-task project files
   contain task identifiers or artifact references.
3. It generates `tasks/index.md`, grouping every task and listing every compiled artifact while
   adding current lifecycle labels from `status.md`.
4. It adds one top-level `Tasks` navigation item pointing to that index page.

The committed `workspace/00-INDEX.md` is a fifth, separate source artifact. Current collection sees
21 state-bearing tasks (12 in flight, 9 closed), 41 historical tasks, 6 backlog rows, 2 absorbed rows,
and 3 unresolved inputs.

The documentation plugin already writes generated pages virtually during the build rather than to
the source tree. Its documented API supports exactly this build-only projection. MkDocs also states
that pages omitted from navigation are still rendered and can be reached by direct links; omission
only removes global navigation and previous/next placement. Therefore cited-trace reachability does
not require a top-level task library, and a CI-generated list does not require a committed index.

Sources: [mkdocs-gen-files virtual files](https://oprypin.github.io/mkdocs-gen-files/),
[MkDocs navigation behavior](https://www.mkdocs.org/user-guide/writing-your-docs/#configure-pages-and-navigation).

### G5: the 123-character event is a valid negative case, not an isolated data repair

The immutable event remains byte-untouched and is the only reason `--check tasks` exits non-zero.
Its `summary` is not rendered by the committed portfolio or documentation task page. Length is
therefore authoring guidance with no observed consumer failure. Removing only this length finding
would make the current task report quiet without weakening any independent status, identity,
transition-shape, attribution, or reference-shape branch.

However, `validate_status` also hard-fails prose bounds (`title` 80; `goal`, `value`, `outcome` 160;
`lifecycle_verbatim` 80). Unlike journal events, state files are mutable and some values are rendered
in the old index, but removal of that index erases the documented display rationale. Their
materiality is not established by the present evidence and should not be silently decided under the
narrow 123-character fix.

## Checkpoint

| Found | Remaining |
|-------|-----------|
| The monolith contains independently placed products; current lifecycle consumers make it mandatory despite optional wording. | Determine the smallest ownership split that preserves Knowledge Gate and migration correctness without retaining an ordinary-user runtime prerequisite. |
| Assisted is currently clean and can remain so. | Prove a clean Full no-helper path rather than relying on absence of Assisted references. |
| CI can compile hidden, citation-reachable trace pages independently of top-level navigation and a committed index. | There is no usage analytics proving that a current-status page itself earns public prominence. |
| The 123 finding is advisory noise and separable from other branches. | Define a severity/compatibility model for historical events and resolve whether other prose bounds belong in the same policy. |
| The present checks are fragmented and do not report every named material defect through one surface. | Decide whether that consolidation belongs to this task's bounded maintainer diagnostics or a later `tfw-doctor` contract. |

**Sufficiency:**
- [x] External source used?
- [x] Briefing gap closed?
- [x] Dimensions identified?

Stage complete: YES
→ User decision: Prior autonomous-run direction applied; proceed without changing the frozen HL or inventing answers for the remaining gaps.
