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
