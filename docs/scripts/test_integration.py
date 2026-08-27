"""Integration tests for the TFW documentation pipeline.

These tests run the actual MkDocs build on the real project and verify output.
They require: pip install -r docs/requirements.txt pytest
"""

import re
import subprocess
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


@pytest.fixture(scope="module", autouse=True)
def build_site():
    """Run mkdocs build once before all integration tests."""
    import os
    env = os.environ.copy()
    env["DISABLE_MKDOCS_2_WARNING"] = "true"
    result = subprocess.run(
        [
            sys.executable, "-m", "mkdocs", "build",
            "--config-file", "docs/mkdocs.yml",
        ],
        capture_output=True, text=True, cwd=str(PROJECT_ROOT),
        env=env,
    )
    if result.returncode != 0:
        pytest.fail(f"MkDocs build failed:\n{result.stderr}\n{result.stdout}")
    yield
    # No cleanup — site/ is in .gitignore


def test_static_pages_generated():
    """Key static pages exist in site/ output."""
    site = PROJECT_ROOT / "site"
    assert (site / "index.html").exists(), "index.html missing"
    assert (site / "getting-started" / "index.html").exists(), "getting-started missing"
    assert (site / "concepts" / "philosophy" / "index.html").exists(), "philosophy missing"
    assert (site / "reference" / "conventions" / "index.html").exists(), "conventions missing"
    assert (site / "reference" / "glossary" / "index.html").exists(), "glossary missing"
    assert (site / "reference" / "changelog" / "index.html").exists(), "changelog missing"


def test_knowledge_index_generated():
    """KNOWLEDGE.md compiled to knowledge-index page."""
    site = PROJECT_ROOT / "site"
    page = site / "knowledge-index" / "index.html"
    assert page.exists(), "knowledge-index page missing"
    content = page.read_text(encoding="utf-8")
    assert "Architecture" in content or "architecture" in content


def test_task_pages_generated():
    """Task artifacts are accessible."""
    site = PROJECT_ROOT / "site"
    tasks_dir = site / "tasks"
    if not tasks_dir.exists():
        pytest.skip("No tasks/ in site output")
    task_pages = list(tasks_dir.rglob("index.html"))
    assert len(task_pages) > 10, f"Expected 10+ task pages, got {len(task_pages)}"


def test_knowledge_topic_pages_generated():
    """Knowledge topic files are compiled."""
    site = PROJECT_ROOT / "site"
    knowledge_dir = site / "knowledge"
    assert knowledge_dir.exists(), "knowledge/ section missing"
    topic_pages = list(knowledge_dir.glob("*/index.html"))
    assert len(topic_pages) >= 3, f"Expected 3+ topics, got {len(topic_pages)}"


def test_workflow_pages_generated():
    """Workflow reference pages exist."""
    site = PROJECT_ROOT / "site"
    wf_dir = site / "reference" / "workflows"
    assert wf_dir.exists(), "reference/workflows/ missing"
    wf_pages = list(wf_dir.rglob("index.html"))
    assert len(wf_pages) >= 5, f"Expected 5+ workflow pages, got {len(wf_pages)}"


def test_template_pages_generated():
    """Template reference pages exist."""
    site = PROJECT_ROOT / "site"
    tpl_dir = site / "reference" / "templates"
    assert tpl_dir.exists(), "reference/templates/ missing"
    tpl_pages = list(tpl_dir.rglob("index.html"))
    assert len(tpl_pages) >= 5, f"Expected 5+ template pages, got {len(tpl_pages)}"


def test_frontmatter_in_generated_pages():
    """Generated pages have YAML frontmatter (title/source)."""
    site = PROJECT_ROOT / "site"
    # Check knowledge-index page title in HTML
    page = site / "knowledge-index" / "index.html"
    if page.exists():
        content = page.read_text(encoding="utf-8")
        # MkDocs Material puts the title in <title> tag
        assert "<title>" in content


# --- Reference Resolution Spot-Checks ---
# These tests verify that gen_docs resolved text references into HTML links.


def test_decision_refs_resolved_in_knowledge_index():
    """D{N} references in knowledge-index resolve to #architecture-decisions anchors."""
    site = PROJECT_ROOT / "site"
    page = site / "knowledge-index" / "index.html"
    if not page.exists():
        pytest.skip("knowledge-index page not built")
    content = page.read_text(encoding="utf-8")
    # D{N} refs should be resolved to anchor links (relative URL format)
    assert "#architecture-decisions" in content, \
           "D{N} references not resolved in knowledge-index"


def test_artifact_refs_resolved_in_knowledge_topics():
    """Knowledge topic files contain resolved links to task artifacts."""
    site = PROJECT_ROOT / "site"
    knowledge_dir = site / "knowledge"
    if not knowledge_dir.exists():
        pytest.skip("knowledge/ not built")
    # At least one knowledge topic should have resolved task links
    found_task_link = False
    for page in knowledge_dir.rglob("index.html"):
        content = page.read_text(encoding="utf-8")
        if "/tasks/" in content:
            found_task_link = True
            break
    assert found_task_link, \
        "No resolved artifact references found in any knowledge/ topic page"


def test_td_refs_resolved_in_output():
    """TD-{N} references resolve to /reference/tech-debt.md links."""
    site = PROJECT_ROOT / "site"
    # Search across all pages for resolved TD links
    found_td_link = False
    for page in site.rglob("index.html"):
        content = page.read_text(encoding="utf-8")
        if "/reference/tech-debt/" in content:
            found_td_link = True
            break
    assert found_td_link, "No resolved TD-{N} references found in site output"


def test_index_override_used():
    """When docs/index.md exists, it should be used instead of README.md."""
    site = PROJECT_ROOT / "site"
    index = site / "index.html"
    assert index.exists(), "index.html missing"
    content = index.read_text(encoding="utf-8")
    override = PROJECT_ROOT / "docs" / "index.md"
    if override.exists():
        override_text = override.read_text(encoding="utf-8")
        if "Getting Started" in override_text:
            assert "Getting Started" in content, "Index override not applied"


def test_no_board_shaped_regex_survives_in_the_generators():
    """TD-81 and TD-177 stay dead.

    The docs build used to regex-read columns out of the root README's Task Board. That
    made a hand-maintained table an implicit API (TD-81) and broke on the table's own
    schema drift (TD-177). Deleting the parser retires both; this test is what stops a
    future convenience from quietly reintroducing the coupling.

    The migration script is exempt: reading the board once, to retire it, is its job.
    """
    scripts = sorted((PROJECT_ROOT / "docs" / "scripts").glob("*.py"))
    assert scripts, "no generator scripts found"
    table_regex = re.compile(r"""r?['"][^'"]*\\\|\s*\\?\[?\(\?""")
    offenders = []
    for script in scripts:
        if script.name in {"migrate_board.py", "test_integration.py"}:
            continue
        for number, line in enumerate(script.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("#"):
                continue
            if table_regex.search(line):
                offenders.append(script.name + ":" + str(number) + ": " + line.strip())
    assert not offenders, "board-shaped table regex reintroduced: " + "; ".join(offenders)


def test_generators_do_not_read_the_root_readme_for_task_state():
    """Task lifecycle comes from each task's own status.md, never from a root table."""
    gen_docs = (PROJECT_ROOT / "docs" / "scripts" / "gen_docs.py").read_text(encoding="utf-8")
    body = gen_docs[gen_docs.index("def _generate_tasks_index"):]
    body = body[:body.index(chr(10) + "def ", 1)]
    assert "gen_index.read_status" in body, "tasks index no longer reads task state"
    # Drop the docstring: it names the retired board deliberately, as the historical note.
    quotes = chr(34) * 3
    opening = body.index(quotes) + len(quotes)
    code = body[body.index(quotes, opening) + len(quotes):]
    offenders = [line for line in code.splitlines()
                 if "README" in line and not line.lstrip().startswith("#")]
    assert not offenders, "the tasks index reads the root README again: " + str(offenders)


def test_the_board_is_gone_from_the_root_readme():
    """The README carries a route to the index, not a live task table."""
    readme = (PROJECT_ROOT / "README.md").read_text(encoding="utf-8")
    assert "## Task Board" not in readme
    assert "workspace/00-INDEX.md" in readme, "no route to the portfolio index"
    live_rows = [line for line in readme.splitlines()
                 if re.match(r"^\| \[?TFW-\d+", line)]
    assert not live_rows, "live task rows still in the README: " + str(live_rows[:3])


def test_section_index_pages_generated():
    """Glob sections have auto-generated index pages (tasks/, knowledge/, etc.)."""
    site = PROJECT_ROOT / "site"
    for section in ["tasks", "knowledge"]:
        index = site / section / "index.html"
        assert index.exists(), f"{section}/index.html missing"
        content = index.read_text(encoding="utf-8")
        # Index should list pages as links
        assert "<a" in content, f"{section} index has no links"


def test_resolved_links_use_directory_urls():
    """Resolved artifact links use directory URLs (no .md extension)."""
    site = PROJECT_ROOT / "site"
    knowledge_dir = site / "knowledge"
    if not knowledge_dir.exists():
        pytest.skip("knowledge/ not built")
    for page in knowledge_dir.rglob("index.html"):
        content = page.read_text(encoding="utf-8")
        # Check that links to /tasks/ don't end with .md
        import re
        md_links = re.findall(r'href="/tasks/[^"]*\.md"', content)
        assert not md_links, f"Found .md links in {page}: {md_links[:3]}"


# ===========================================================================
# Control characters in shipped text (review rev2, items 4 / 7 / 8)
# ===========================================================================

CONTROL_CHARS = re.compile("[" + "".join(
    chr(c) for c in list(range(0, 9)) + [11, 12] + list(range(14, 32))) + "]")

#: Text the project ships and an agent reads as instructions. Binary assets are excluded by
#: extension rather than by guessing: a PNG legitimately contains control bytes.
SHIPPED_TEXT = ("*.md", "*.yaml", "*.yml", "*.py", "*.template", "*.txt")

BINARY_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf", ".woff", ".woff2"}


def _scan_for_control_chars(paths):
    """Return (path, line number, character name) for every control character found.

    Deliberately implemented in Python rather than as a shell pipeline. `grep -P` aborts on
    this machine with *-P supports only unibyte and UTF-8 locales* and **exits without
    output** — which is indistinguishable from a clean scan. A check whose failure mode is
    silence is not a check.
    """
    names = {0x08: "BACKSPACE", 0x09: "TAB", 0x0b: "VERTICAL TAB", 0x0c: "FORM FEED",
             0x1b: "ESCAPE", 0x00: "NUL"}
    found = []
    for path in paths:
        if path.suffix.lower() in BINARY_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for number, line in enumerate(text.splitlines(), 1):
            for char in CONTROL_CHARS.findall(line):
                found.append((path, number, names.get(ord(char), hex(ord(char)))))
    return found


def test_the_control_character_scanner_actually_detects_one(tmp_path):
    """Prove the check can fail, before believing that it passed.

    This is the guard on the guard. Three times this phase was damaged by a check reported as
    passing that never ran — a review that recorded 61 rows against a file containing zero, an
    event stamped from a composed time, and a `grep -P` scan that aborted on the locale and
    returned nothing. Each time a claim was accepted where a measurement was available.
    """
    good = tmp_path / "clean.md"
    good.write_text("A normal line\n\twith a tab and a — dash\n", encoding="utf-8")
    assert _scan_for_control_chars([good]) == [], "tab, newline and CR must be allowed"

    bad = tmp_path / "corrupt.md"
    bad.write_text("path: %LOCALAPPDATA%" + chr(9) + "fw" + chr(8) + "indings.yaml\n",
                   encoding="utf-8")
    hits = _scan_for_control_chars([bad])
    assert hits, "the scanner failed to detect a known-bad input"
    assert {h[2] for h in hits} == {"BACKSPACE"}, hits

    binary = tmp_path / "asset.png"
    binary.write_bytes(bytes([0x89, 0x50, 0x4e, 0x47, 0x00, 0x08, 0x1b]))
    assert _scan_for_control_chars([binary]) == [], "binary assets are excluded by extension"


def test_no_shipped_text_carries_a_control_character():
    """The class, not the string.

    A regression test on one path leaves the next Windows path free to break the same way.
    `\\t` and `\\b` inside a Windows path are the trap — they were interpreted as escapes and
    written as a TAB and a BACKSPACE, sending every agent to a location that cannot exist.
    """
    roots = [PROJECT_ROOT / d for d in
             (".tfw", "docs/scripts", ".claude", ".agent", ".agents", "tasks", "team",
              "workspace", "knowledge")]
    roots += [PROJECT_ROOT]
    paths = []
    for root in roots:
        if not root.exists():
            continue
        for pattern in SHIPPED_TEXT:
            paths.extend(root.glob(pattern) if root == PROJECT_ROOT
                         else root.rglob(pattern))

    hits = _scan_for_control_chars(sorted(set(paths)))
    rendered = [f"{p.relative_to(PROJECT_ROOT).as_posix()}:{n}: {name}" for p, n, name in hits]
    assert not rendered, "control characters in shipped text:\n" + "\n".join(rendered)


#: Paths that intentionally do not exist in the tree, with the reason each one is exempt.
#: Every entry is a real path a shipped instruction names on purpose; the list is short and
#: annotated so it cannot quietly become a place to hide a broken reference.
NON_REPO_PATHS = {
    ".tfw/bindings.yaml":
        "not a project path at all. The per-machine binding lives at ~/.tfw/bindings.yaml, "
        "outside the tree, because a project-local file is gitignorable but not "
        "sync-ignorable",
    ".tfw/.upstream/.tfw/CHANGELOG.md":
        "created at runtime by update.md Step 0, which clones upstream into a staging "
        "directory, and removed again at Step 9",
}

TFW_PATH = re.compile(r"\.tfw/[A-Za-z0-9_./-]+\.(?:md|yaml|yml|py|template)")


def _unresolved_tfw_paths(files):
    """Every `.tfw/...` path named by these files that does not resolve, with its source."""
    findings = []
    for path in files:
        named = sorted(set(TFW_PATH.findall(path.read_text(encoding="utf-8"))))
        for target in named:
            if target in NON_REPO_PATHS or (PROJECT_ROOT / target).exists():
                continue
            try:
                where = path.relative_to(PROJECT_ROOT).as_posix()
            except ValueError:
                where = path.as_posix()   # a fixture outside the tree, in the self-test
            findings.append(f"{where} -> {target}")
    return findings


def test_every_path_an_adapter_source_names_resolves():
    """A shipped instruction must name a file the receiving project actually has.

    `.tfw/adapters/claude-code/CLAUDE.md.template` routed `/tfw-research` at
    `.tfw/workflows/research.md` for two releases. That file has never existed under that
    name — the workflow became a directory — so a project that installed or re-synced the
    Claude Code adapter from source inherited a route to nothing, and nothing said so.

    The check is over every adapter source, not over the one file that was found broken.
    """
    sources = sorted(p for p in (PROJECT_ROOT / ".tfw" / "adapters").rglob("*")
                     if p.is_file() and p.suffix in {".md", ".template"})
    assert sources, "no adapter sources found"
    unresolved = _unresolved_tfw_paths(sources)
    assert not unresolved, ("adapter sources name paths that do not exist:" + chr(10)
                            + chr(10).join(unresolved))


def test_every_path_an_installed_adapter_copy_names_resolves():
    """The same check over what is installed, so a stale copy is not invisible."""
    roots = [PROJECT_ROOT / d for d in (".claude/commands", ".agent/workflows",
                                        ".agents/skills")]
    files = sorted(p for root in roots if root.exists()
                   for p in root.rglob("*.md"))
    assert files, "no installed adapter copies found"
    unresolved = _unresolved_tfw_paths(files)
    assert not unresolved, ("installed adapter copies name paths that do not exist:"
                            + chr(10) + chr(10).join(unresolved))


def test_the_adapter_path_check_actually_fires(tmp_path):
    """The check is proven to fail before it is trusted to pass.

    A check whose failing branch was never taken is one of the four forms of "a check
    reported as passing that never ran".
    """
    broken = tmp_path / "broken.template"
    broken.write_text("routes to `.tfw/workflows/definitely-not-here.md`\n",
                      encoding="utf-8")
    assert _unresolved_tfw_paths([broken]), "the check must catch a path that is not there"
    fine = tmp_path / "fine.template"
    fine.write_text("routes to `.tfw/workflows/research/base.md`\n", encoding="utf-8")
    assert _unresolved_tfw_paths([fine]) == []
    exempt = tmp_path / "exempt.template"
    exempt.write_text("the binding lives at `.tfw/bindings.yaml` on this machine\n",
                      encoding="utf-8")
    assert _unresolved_tfw_paths([exempt]) == [], "an annotated exemption must be honoured"


def test_installed_adapter_copies_match_their_sources():
    """A copy that has drifted from its source ships instructions nobody reviewed."""
    drifted = []
    for workflow in sorted((PROJECT_ROOT / ".tfw" / "workflows").glob("*.md")):
        for target in (PROJECT_ROOT / ".claude" / "commands" / f"tfw-{workflow.stem}.md",
                       PROJECT_ROOT / ".agent" / "workflows" / f"tfw-{workflow.stem}.md"):
            if target.exists() and target.read_bytes() != workflow.read_bytes():
                drifted.append(target.relative_to(PROJECT_ROOT).as_posix())
    for skill in sorted((PROJECT_ROOT / ".tfw" / "adapters" / "codex" / "skills").glob(
            "tfw-*/SKILL.md")):
        target = PROJECT_ROOT / ".agents" / "skills" / skill.parent.name / "SKILL.md"
        if target.exists() and target.read_bytes() != skill.read_bytes():
            drifted.append(target.relative_to(PROJECT_ROOT).as_posix())
    assert not drifted, "adapter copies out of sync with their sources: " + ", ".join(drifted)


def test_the_status_template_examples_parse_and_validate():
    """A carrier template whose own example is invalid teaches the mistake it warns about.

    The shipped example modelled the unquoted form — `title: short task name` — and the
    first project to hand-author this carrier produced five unparseable files in a row.
    Both the skeleton and the worked example are now checked against the real validator,
    not eyeballed.
    """
    import yaml
    sys.path.insert(0, str(PROJECT_ROOT / ".tfw" / "scripts"))
    import gen_index

    text = (PROJECT_ROOT / ".tfw" / "templates" / "status.md").read_text(encoding="utf-8")

    skeleton = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    assert skeleton, "the template must open with front matter"
    assert isinstance(yaml.safe_load(skeleton.group(1)), dict), \
        "the template's own skeleton does not parse as YAML"

    marker = "A COMPLETE, VALID EXAMPLE"
    assert marker in text, "a person hand-authoring this needs a complete example"
    body = re.search(r"    ---\n(.*?)\n    ---\n", text.split(marker)[1], re.S)
    assert body, "the worked example must be a full front-matter block"
    example = yaml.safe_load(chr(10).join(line[4:] for line in body.group(1).splitlines()))
    assert isinstance(example, dict), "the worked example does not parse"
    problems = gen_index.validate_status(example)
    assert not problems, "the worked example fails the real validator: " + "; ".join(problems)


def test_every_runtime_message_is_ascii():
    """A message printed to a terminal must survive the terminal's encoding.

    The tools print to stderr on machines whose console codepage nobody chose. An em dash
    or a `·` in a refusal renders as a replacement character there — and worse, it made a
    test that read a subprocess's stderr fail on a `UnicodeDecodeError` rather than on the
    thing it was checking. Prose in docstrings and comments is unaffected; this is about
    the strings that reach a person mid-run.

    A class check, not a list of the four occurrences that were found once.
    """
    offenders = []
    for script in sorted((PROJECT_ROOT / ".tfw" / "scripts").glob("*.py")):
        if script.name.startswith("test_"):
            continue
        emitting = False
        for number, line in enumerate(script.read_text(encoding="utf-8").splitlines(), 1):
            if re.search(r"\b(print|SystemExit)\s*\(", line):
                emitting = True
            if emitting:
                bad = sorted({c for c in line if ord(c) > 127})
                if bad:
                    names = " ".join(f"U+{ord(c):04X}" for c in bad)
                    offenders.append(f"{script.name}:{number}: {names}")
            if emitting and line.rstrip().endswith(")"):
                emitting = False
    assert not offenders, ("non-ASCII in runtime output:" + chr(10)
                           + chr(10).join(offenders))


def test_the_windows_binding_path_is_the_literal_one():
    """The specific case, kept alongside the class check rather than instead of it."""
    expected = "%LOCALAPPDATA%" + chr(92) + "tfw" + chr(92) + "bindings.yaml"
    canonical = sorted((PROJECT_ROOT / ".tfw" / "workflows").rglob("*.md"))
    carrying = [p for p in canonical if "LOCALAPPDATA" in p.read_text(encoding="utf-8")]
    assert carrying, "no canonical workflow names the Windows binding location"
    for path in carrying:
        text = path.read_text(encoding="utf-8")
        assert expected in text, f"{path.name} does not carry the literal path"

    # and every adapter copy agrees with its source
    for source in carrying:
        for copy_root, prefix in ((PROJECT_ROOT / ".claude" / "commands", "tfw-"),
                                  (PROJECT_ROOT / ".agent" / "workflows", "tfw-")):
            name = source.stem if source.stem != "base" else "research"
            copy = copy_root / f"{prefix}{name}.md"
            if copy.exists():
                assert expected in copy.read_text(encoding="utf-8"), \
                    f"{copy.relative_to(PROJECT_ROOT).as_posix()} is stale or corrupted"


# ===========================================================================
# Canonical naming on the shipped surface (review rev3, items 4 / 5)
# ===========================================================================

STAMP = r"\d{8}-\d{6}"

#: Only backticked spans are checked: those are the examples a reader copies. Prose about
#: the grammar is allowed to name a bare stamp — the rule is about names, not about words.
BACKTICKED = re.compile(r"`([^`" + chr(10) + r"]+)`")

#: A bare stamp used where a NAME belongs: a directory segment or an artifact filename.
#: A bare stamp used as a timestamp VALUE (`created: 20260819-000000`) is correct and is
#: deliberately not matched.
BARE_ID_AS_NAME = re.compile(
    r"(?:/" + STAMP + r"(?:/|$)"                       # a path segment
    r"|(?:^|/)(?:HL-|[A-Z]+__)" + STAMP + r"\.md"      # an artifact filename
    r"|(?:^|/)" + STAMP + r"/)"                        # a directory
)

#: `{ID}` already ends in the slug, so anything appended doubles it.
DOUBLED_SLUG = re.compile(r"\{ID\}__")

#: An event example with only two segments has no actor, and two writers recording the same
#: kind in the same second would collide on it.
#: The kind may contain a single underscore (`ownership_changed`) but never a double one:
#: `__` is the segment separator, so `[a-z_]+` would swallow the actor and call a correct
#: three-segment name actorless. The detector's own self-check caught exactly that.
ACTORLESS_EVENT = re.compile(
    r"(?<![\w-])(?:" + STAMP + r"|\{YYYYMMDD-HHMMSS\})__[a-z]+(?:_[a-z]+)*\.md")


def _canonical_surface():
    """The files a user actually runs, plus the propagated copies they run instead."""
    roots = [PROJECT_ROOT / d for d in
             (".tfw/workflows", ".tfw/templates", ".claude/commands", ".agent/workflows",
              ".agents/skills")]
    files = [p for root in roots if root.exists() for p in root.rglob("*.md")]
    for name in ("conventions.md", "glossary.md", "quickstart.md", "compilable_contract.md"):
        candidate = PROJECT_ROOT / ".tfw" / name
        if candidate.exists():
            files.append(candidate)
    return sorted(set(files))


def _offenders(pattern):
    found = []
    for path in _canonical_surface():
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for span in BACKTICKED.findall(line):
                if pattern.search(span):
                    found.append(f"{path.relative_to(PROJECT_ROOT).as_posix()}:{number}: `{span}`")
    return found


def test_the_naming_detectors_actually_fire(tmp_path):
    """Prove each detector can fail before believing that it passed.

    Same discipline as the control-character gate, and for the same reason: this phase has
    repeatedly been damaged by checks reported as passing that never ran.
    """
    assert BARE_ID_AS_NAME.search("workspace/2026/20260826-143000/")
    assert BARE_ID_AS_NAME.search("RES__20260826-143000.md")
    assert BARE_ID_AS_NAME.search("HL-20260826-143000.md")
    assert DOUBLED_SLUG.search("{container}/{YYYY}/{ID}__tfw_init/")
    assert ACTORLESS_EVENT.search("20260826-143000__created.md")
    assert ACTORLESS_EVENT.search("{YYYYMMDD-HHMMSS}__{kind}.md".replace("{kind}", "handoff"))

    # and the legitimate forms must NOT fire
    assert not BARE_ID_AS_NAME.search("created: 20260819-000000")
    assert not BARE_ID_AS_NAME.search("workspace/2026/20260826-143000__query_redesign/")
    assert not DOUBLED_SLUG.search("RES__{ID}.md")
    assert not ACTORLESS_EVENT.search("20260826-143000__created__saubakirov.md")


def test_no_canonical_example_uses_a_bare_identifier_as_a_name():
    """AC-14 items 4 and 5. A bare stamp cannot name exactly one task."""
    offenders = _offenders(BARE_ID_AS_NAME)
    assert not offenders, "bare identifier used as a name:" + chr(10) + chr(10).join(offenders)


def test_no_canonical_example_doubles_the_slug():
    """`{ID}__tfw_init` expanded to a doubled slug — a new project's first task was given a
    name its own contract rejects."""
    offenders = _offenders(DOUBLED_SLUG)
    assert not offenders, "{ID} already carries the slug:" + chr(10) + chr(10).join(offenders)


def test_no_canonical_event_example_is_actorless():
    """The actor is what separates two writers recording the same kind in the same second."""
    offenders = _offenders(ACTORLESS_EVENT)
    assert not offenders, "event example without an actor:" + chr(10) + chr(10).join(offenders)


def test_the_canonical_surface_is_actually_being_scanned():
    """A scan over an empty file list passes trivially. Assert it is not empty."""
    files = _canonical_surface()
    assert len(files) > 30, f"only {len(files)} canonical files found"
    names = {p.name for p in files}
    assert "conventions.md" in names and "init.md" in names and "status.md" in names
