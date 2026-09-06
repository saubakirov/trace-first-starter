"""Integration tests for the TFW documentation pipeline.

These tests run the actual MkDocs build on the real project and verify output.
They require: pip install -r docs/requirements.txt pytest
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

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
    """TD-{N} references resolve to the retired registry's snapshot page.

    The registry was retired at 2.1.0 and its manifest row deleted: the snapshot is compiled by
    the task-container glob, like BOARD-SNAPSHOT.md, so there is exactly one output page for it.
    This test is what stops a citation going dead in a rename that looks harmless.
    """
    site = PROJECT_ROOT / "site"
    # Search across all pages for resolved TD links
    found_td_link = False
    for page in site.rglob("index.html"):
        content = page.read_text(encoding="utf-8")
        if "/tasks/DEBT-SNAPSHOT/" in content:
            found_td_link = True
            break
    assert found_td_link, "No resolved TD-{N} references found in site output"


def test_no_page_renders_its_own_frontmatter_as_body_text():
    """The header a page carries must parse, whatever the page is called or contains.

    Three separate causes shipped this same symptom, on 860 of 990 pages:
      * the source path reached `source:` OS-native, and a Windows backslash is an invalid escape;
      * the block was built by interpolation, so a title holding a double quote — 247 artifacts here
        do — closed the scalar early;
      * `resolve_references` ran over the header as well as the body and turned a bare task id in a
        title into a markdown link, which rendered as HTML.

    Each was fixed by removing the thing that made it possible rather than by escaping harder:
    `Path.as_posix()`, `yaml.safe_dump`, and adding the header last. This test is the end-to-end
    backstop for a fourth cause nobody has thought of.
    """
    site = PROJECT_ROOT / "site"
    leaked = re.compile(r"<hr />\s*<p>title: ")
    offenders = [p for p in site.rglob("index.html") if leaked.search(p.read_text(encoding="utf-8"))]
    assert not offenders, (
        f"{len(offenders)} of {len(list(site.rglob('index.html')))} pages render their frontmatter "
        "as body text, e.g. " + ", ".join(str(p.relative_to(site)) for p in offenders[:3])
    )


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
    body = gen_docs[gen_docs.index("def _generate_task_landings"):]
    body = body[:body.index(chr(10) + "def ", 1)]
    assert "tfw_state.read_status" in body, "task landings no longer read task state"
    quotes = chr(34) * 3
    opening = body.index(quotes) + len(quotes)
    code = body[body.index(quotes, opening) + len(quotes):]
    offenders = [line for line in code.splitlines()
                 if "README" in line and not line.lstrip().startswith("#")]
    assert not offenders, "task landings read the root README: " + str(offenders)


def test_the_board_is_gone_from_the_root_readme():
    """The README carries direct trace routes, not a live table or portfolio cache."""
    readme = (PROJECT_ROOT / "README.md").read_text(encoding="utf-8")
    assert "## Task Board" not in readme
    assert "workspace/00-INDEX.md" not in readme
    assert "workspace/2026/" in readme, "no direct selected-trace route"
    live_rows = [line for line in readme.splitlines()
                 if re.match(r"^\| \[?TFW-\d+", line)]
    assert not live_rows, "live task rows still in the README: " + str(live_rows[:3])


def test_section_index_pages_generated():
    """Knowledge is indexed; task traces have hidden per-task landings only."""
    site = PROJECT_ROOT / "site"
    knowledge = site / "knowledge" / "index.html"
    assert knowledge.exists()
    assert "<a" in knowledge.read_text(encoding="utf-8")
    assert not (site / "tasks" / "index.html").exists()
    landing = site / "tasks" / "2026" / "TFW_20260902-222456_RTBO" / "index.html"
    assert landing.exists() and "Task trace" in landing.read_text(encoding="utf-8")


def test_every_recognized_task_has_an_unlisted_landing_and_nav_has_no_tasks_entry():
    sys.path.insert(0, str(PROJECT_ROOT / "tools"))
    import tfw_state
    site = PROJECT_ROOT / "site"
    containers = tfw_state.task_containers(PROJECT_ROOT)
    for task_dir in tfw_state.iter_task_dirs(PROJECT_ROOT):
        relative = next(
            task_dir.relative_to(PROJECT_ROOT / container)
            for container in containers
            if task_dir.is_relative_to(PROJECT_ROOT / container)
        )
        landing = site / "tasks" / relative / "index.html"
        assert landing.exists(), task_dir.relative_to(PROJECT_ROOT).as_posix()
    home = (site / "index.html").read_text(encoding="utf-8")
    assert not re.search(r'<a[^>]*class="md-nav__link"[^>]*>\s*Tasks\s*</a>', home)


def test_status_snapshot_is_explicit_finite_non_gating_and_outside_site():
    workflow = (PROJECT_ROOT / ".github/workflows/docs.yml").read_text(encoding="utf-8")
    assert "status_snapshot:" in workflow and "type: boolean" in workflow and "default: false" in workflow
    condition = "github.event_name == 'workflow_dispatch' && inputs.status_snapshot"
    assert workflow.count(condition) == 2
    assert "python tools/tfw_doctor.py --root . status --format json" in workflow
    assert "diagnostic_exit=$?" in workflow and "exit-code.txt" in workflow
    assert "retention-days: 7" in workflow
    snapshot_block = workflow.partition("- name: Collect optional status snapshot")[2].partition("- name: Build docs")[0]
    assert "site/" not in snapshot_block
    assert "exit $diagnostic_exit" not in snapshot_block


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
    ".tfw/.upstream/.tfw/workflows/update.md":
        "the TARGET's update workflow inside the same staging directory: Step -1 tells the "
        "operator to follow it instead of the installed copy, which is what the update "
        "replaces",
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


MANAGED_BLOCK = re.compile(
    r"<!-- TFW:(?P<name>[A-Z]+):START -->" + chr(10) + r"(?P<body>.*?)<!-- TFW:(?P=name):END -->",
    re.S)


def _managed_block(text: str, name: str):
    """The marker-bounded region of one managed block, or None when the file has no markers.

    None is a result, not an error: conventions §9 says a file without markers is REPORTED and
    left untouched, so a sync that receives None writes nothing.
    """
    blocks = [m for m in MANAGED_BLOCK.finditer(text) if m.group("name") == name]
    assert len(blocks) <= 1, f"exactly one {name} block per file"
    return blocks[0] if blocks else None


def _sync_block(installed: str, template: str, name: str):
    """What update.md Step 6 does for a block row: replace between the markers, or None."""
    have, want = _managed_block(installed, name), _managed_block(template, name)
    assert want, "the template must carry the block"
    if have is None:
        return None
    return installed[:have.start("body")] + want.group("body") + installed[have.end("body"):]


def test_installed_adapter_copies_match_their_sources():
    """A copy that has drifted from its source ships instructions nobody reviewed.

    The framework is its own first consumer: its root `CLAUDE.md` carries the Claude rules
    block between markers, byte-identical to the template's, and is checked here like every
    other installed copy -- on the region between the markers, since the text outside them is
    this project's own.
    """
    drifted = []
    template = (PROJECT_ROOT / ".tfw" / "adapters" / "claude-code" / "CLAUDE.md.template"
                ).read_text(encoding="utf-8")
    installed = (PROJECT_ROOT / "CLAUDE.md").read_text(encoding="utf-8")
    want, have = _managed_block(template, "CLAUDE"), _managed_block(installed, "CLAUDE")
    assert want, "CLAUDE.md.template must carry the TFW:CLAUDE block"
    assert have, "this repository's CLAUDE.md must carry the TFW:CLAUDE block"
    if want.group("body") != have.group("body"):
        drifted.append("CLAUDE.md (TFW:CLAUDE block)")
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


def test_a_marker_bounded_sync_leaves_project_text_untouched(tmp_path):
    """AC-4's gate: a fixture CLAUDE.md carrying project text above and below the block.

    After the sync the region between the markers equals the template's; every byte outside
    it is unchanged. `cmp` on the region is the whole verification.
    """
    template = (PROJECT_ROOT / ".tfw" / "adapters" / "claude-code" / "CLAUDE.md.template"
                ).read_text(encoding="utf-8")
    above = "# Consumer rules" + chr(10) + chr(10) + "Hand-written, three times edited." + chr(10) + chr(10)
    below = chr(10) + "## Code standards" + chr(10) + chr(10) + "Ours, not the framework's." + chr(10)
    stale = ("<!-- TFW:CLAUDE:START -->" + chr(10) + "## TFW 1.3.0" + chr(10)
             + "old block text" + chr(10) + "<!-- TFW:CLAUDE:END -->" + chr(10))
    fixture = tmp_path / "CLAUDE.md"
    fixture.write_text(above + stale + below, encoding="utf-8")

    synced = _sync_block(fixture.read_text(encoding="utf-8"), template, "CLAUDE")
    assert synced is not None
    fixture.write_text(synced, encoding="utf-8")
    after = fixture.read_text(encoding="utf-8")
    assert after.startswith(above) and after.endswith(below), "project text outside the block changed"
    assert _managed_block(after, "CLAUDE").group("body") == _managed_block(template, "CLAUDE").group("body")
    assert "old block text" not in after


def test_a_file_without_markers_is_reported_and_left_untouched(tmp_path):
    """The first-run rule, conventions §9: no markers -> report, never append.

    The fourth report's consumer had a hand-written TFW section without markers; appending
    would have produced two sections that disagree.
    """
    template = (PROJECT_ROOT / ".tfw" / "adapters" / "claude-code" / "CLAUDE.md.template"
                ).read_text(encoding="utf-8")
    unmarked = "# Consumer rules" + chr(10) + chr(10) + "## TFW 2.0.0-dirty.2" + chr(10) + "hand-written" + chr(10)
    fixture = tmp_path / "CLAUDE.md"
    fixture.write_text(unmarked, encoding="utf-8")
    assert _sync_block(fixture.read_text(encoding="utf-8"), template, "CLAUDE") is None
    assert fixture.read_text(encoding="utf-8") == unmarked


def test_no_adapter_template_requires_a_version_substitution():
    """TD-204: a rendered rule reads `.tfw/VERSION`; a template asking for `{version}` on
    every update is a substitution somebody forgets -- one consumer announced 0.8.5 for two
    releases. The Antigravity and Cursor templates are whole copies now."""
    for rel in (".tfw/adapters/antigravity/tfw-rules.md.template",
                ".tfw/adapters/cursor/tfw.mdc.template",
                ".tfw/adapters/claude-code/CLAUDE.md.template"):
        text = (PROJECT_ROOT / rel).read_text(encoding="utf-8")
        assert "{version}" not in text, f"{rel} still asks for a version substitution"
    rendered = (PROJECT_ROOT / ".agent" / "rules" / "tfw.md").read_bytes()
    source = (PROJECT_ROOT / ".tfw" / "adapters" / "antigravity" / "tfw-rules.md.template").read_bytes()
    assert rendered == source, "the Antigravity rule and its template must agree byte for byte"


EXPECTED_TFW_COMMANDS = {
    "plan": "Coordinator", "research": "Researcher", "handoff": "Executor",
    "review": "Reviewer", "resume": "Coordinator", "docs": "Coordinator",
    "knowledge": "Coordinator", "release": "Coordinator", "update": "Coordinator",
    "config": "Coordinator", "init": "Coordinator",
}

PRIMARY_ROUTES = {
    "plan": ("Coordinator", ".tfw/workflows/plan.md"),
    "research": ("Researcher", ".tfw/workflows/research/base.md"),
    "handoff": ("Executor", ".tfw/workflows/handoff.md"),
    "review": ("Reviewer", ".tfw/workflows/review.md"),
}

SECONDARY_ROUTES = {
    "resume": ("Coordinator", ".tfw/workflows/resume.md"),
    "docs": ("Coordinator", ".tfw/workflows/docs.md"),
    "knowledge": ("Coordinator", ".tfw/workflows/knowledge.md"),
    "release": ("Coordinator", ".tfw/workflows/release.md"),
    "update": ("Coordinator", ".tfw/workflows/update.md"),
    "config": ("Coordinator", ".tfw/workflows/config.md"),
    "init": ("Coordinator", ".tfw/workflows/init.md"),
}

ALL_ROUTES = {**PRIMARY_ROUTES, **SECONDARY_ROUTES}

EXPECTED_PERSISTENT_TARGETS = {
    "codex": "AGENTS.md",
    "claude-code": "CLAUDE.md",
    "cursor": ".cursor/rules/tfw.mdc",
    "antigravity": ".agents/rules/tfw.md",
}


def _adapter_manifest():
    path = PROJECT_ROOT / ".tfw" / "adapters" / "manifest.yaml"
    assert path.exists(), "Phase A adapter manifest is missing"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _expand(pattern: str, command: str, workflow: str | None = None) -> str:
    return pattern.replace("{command}", command).replace("{workflow}", workflow or "")


def _manifest_errors(manifest) -> list[str]:
    errors = []
    commands = manifest.get("commands", {})
    if set(commands) != set(EXPECTED_TFW_COMMANDS):
        errors.append("command set is not exact")
    for name, role in EXPECTED_TFW_COMMANDS.items():
        row = commands.get(name, {})
        if row.get("route") != f"/tfw-{name}" or row.get("role") != role:
            errors.append(f"{name}: route/role mismatch")
        source = row.get("workflow")
        if not source or not (PROJECT_ROOT / source).is_file():
            errors.append(f"{name}: canonical workflow is unresolved")
    adapters = manifest.get("adapters", {})
    if set(adapters) != set(EXPECTED_PERSISTENT_TARGETS):
        errors.append("adapter set is not exact")
    for name, target in EXPECTED_PERSISTENT_TARGETS.items():
        row = adapters.get(name, {})
        persistent = row.get("persistent", {})
        commands_row = row.get("commands", {})
        if persistent.get("target") != target:
            errors.append(f"{name}: persistent target mismatch")
        if not (PROJECT_ROOT / str(persistent.get("source", "missing"))).is_file():
            errors.append(f"{name}: persistent source is unresolved")
        if persistent.get("strategy") not in {"copy", "managed_block"}:
            errors.append(f"{name}: persistent strategy is invalid")
        if commands_row.get("strategy") != "copy":
            errors.append(f"{name}: command strategy is invalid")
        for command in EXPECTED_TFW_COMMANDS:
            source = _expand(str(commands_row.get("source", "")), command,
                             commands.get(command, {}).get("workflow", ""))
            destination = _expand(str(commands_row.get("target", "")), command)
            if not source or not (PROJECT_ROOT / source).is_file():
                errors.append(f"{name}/{command}: command source is unresolved")
            if not destination or "{command}" in destination:
                errors.append(f"{name}/{command}: command target is unresolved")
    return errors


def _install_from_manifest(receiver: Path, adapter: str) -> list[Path]:
    manifest = _adapter_manifest()
    row = manifest["adapters"][adapter]
    written = []
    persistent = row["persistent"]
    destination = receiver / persistent["target"]
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(PROJECT_ROOT / persistent["source"], destination)
    written.append(destination)
    for command in manifest["commands"]:
        source = PROJECT_ROOT / _expand(row["commands"]["source"], command,
                                        manifest["commands"][command]["workflow"])
        destination = receiver / _expand(row["commands"]["target"], command)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        written.append(destination)
    return written


def _sync_from_manifest(receiver: Path, adapter: str) -> tuple[list[Path], list[Path]]:
    """Apply manifest copy/managed-block semantics to an existing or empty receiver."""
    manifest = _adapter_manifest()
    row = manifest["adapters"][adapter]
    written, reported = [], []
    persistent = row["persistent"]
    source = PROJECT_ROOT / persistent["source"]
    destination = receiver / persistent["target"]
    destination.parent.mkdir(parents=True, exist_ok=True)
    if not destination.exists() or persistent["strategy"] == "copy":
        shutil.copyfile(source, destination)
        written.append(destination)
    else:
        installed = destination.read_bytes().decode("utf-8")
        template = source.read_bytes().decode("utf-8")
        block = _sync_block(installed, template, "CLAUDE" if adapter == "claude-code" else "CODEX")
        if block is None:
            reported.append(destination)
        else:
            destination.write_bytes(block.encode("utf-8"))
            written.append(destination)
    for command, command_row in manifest["commands"].items():
        source = PROJECT_ROOT / _expand(row["commands"]["source"], command,
                                        command_row["workflow"])
        destination = receiver / _expand(row["commands"]["target"], command)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        written.append(destination)
    return written, reported


def test_adapter_manifest_is_one_exact_four_by_eleven_contract():
    manifest = _adapter_manifest()
    assert manifest.get("version") == 1
    assert _manifest_errors(manifest) == []


@pytest.mark.parametrize("adapter", sorted(EXPECTED_PERSISTENT_TARGETS))
def test_empty_receiver_gets_exact_vendor_root_and_eleven_commands(tmp_path, adapter):
    receiver = tmp_path / adapter
    written = _install_from_manifest(receiver, adapter)
    manifest = _adapter_manifest()
    assert receiver / EXPECTED_PERSISTENT_TARGETS[adapter] in written
    destinations = {
        _expand(manifest["adapters"][adapter]["commands"]["target"], command)
        for command in manifest["commands"]
    }
    assert len(destinations) == 11
    assert all((receiver / target).is_file() for target in destinations)
    assert manifest["commands"]["research"]["role"] == "Researcher"
    for command, (role, _) in ALL_ROUTES.items():
        path = receiver / _expand(manifest["adapters"][adapter]["commands"]["target"], command)
        command_text = path.read_text(encoding="utf-8")
        assert "role lock" in command_text.lower()
        assert role.lower() in command_text.lower()


def test_primary_manifest_routes_and_installed_copies_are_exact():
    manifest = _adapter_manifest()
    for command, (role, workflow) in PRIMARY_ROUTES.items():
        row = manifest["commands"][command]
        assert row == {"route": f"/tfw-{command}", "workflow": workflow, "role": role}
        canonical = (PROJECT_ROOT / workflow).read_bytes()
        assert (PROJECT_ROOT / ".claude/commands" / f"tfw-{command}.md").read_bytes() == canonical
        assert (PROJECT_ROOT / ".agent/workflows" / f"tfw-{command}.md").read_bytes() == canonical
        source = PROJECT_ROOT / ".tfw/adapters/codex/skills" / f"tfw-{command}" / "SKILL.md"
        installed = PROJECT_ROOT / ".agents/skills" / f"tfw-{command}" / "SKILL.md"
        assert installed.read_bytes() == source.read_bytes()


def test_secondary_manifest_routes_and_installed_copies_are_exact():
    manifest = _adapter_manifest()
    for command, (role, workflow) in SECONDARY_ROUTES.items():
        assert manifest["commands"][command] == {
            "route": f"/tfw-{command}", "workflow": workflow, "role": role,
        }
        canonical = (PROJECT_ROOT / workflow).read_bytes()
        assert (PROJECT_ROOT / ".claude/commands" / f"tfw-{command}.md").read_bytes() == canonical
        assert (PROJECT_ROOT / ".agent/workflows" / f"tfw-{command}.md").read_bytes() == canonical
        source = PROJECT_ROOT / ".tfw/adapters/codex/skills" / f"tfw-{command}" / "SKILL.md"
        installed = PROJECT_ROOT / ".agents/skills" / f"tfw-{command}" / "SKILL.md"
        assert installed.read_bytes() == source.read_bytes()


@pytest.mark.parametrize("adapter", sorted(EXPECTED_PERSISTENT_TARGETS))
def test_manifest_sync_is_idempotent_repairs_commands_and_preserves_unrelated_files(tmp_path, adapter):
    receiver = tmp_path / adapter
    first_written, first_reported = _sync_from_manifest(receiver, adapter)
    assert first_written and first_reported == []
    snapshot = {path.relative_to(receiver).as_posix(): path.read_bytes()
                for path in receiver.rglob("*") if path.is_file()}
    second_written, second_reported = _sync_from_manifest(receiver, adapter)
    assert second_written and second_reported == []
    assert snapshot == {path.relative_to(receiver).as_posix(): path.read_bytes()
                        for path in receiver.rglob("*") if path.is_file()}

    unrelated = receiver / "project-owned.txt"
    unrelated.write_text("keep exactly\n", encoding="utf-8")
    manifest = _adapter_manifest()
    plan = receiver / _expand(manifest["adapters"][adapter]["commands"]["target"], "plan")
    plan.write_text("drift\n", encoding="utf-8")
    _sync_from_manifest(receiver, adapter)
    expected = PROJECT_ROOT / _expand(manifest["adapters"][adapter]["commands"]["source"],
                                      "plan", manifest["commands"]["plan"]["workflow"])
    assert plan.read_bytes() == expected.read_bytes()
    assert unrelated.read_text(encoding="utf-8") == "keep exactly\n"


@pytest.mark.parametrize("adapter", ("codex", "claude-code"))
def test_managed_root_sync_preserves_project_text_and_never_duplicates_an_unmarked_root(tmp_path, adapter):
    receiver = tmp_path / adapter
    _sync_from_manifest(receiver, adapter)
    manifest = _adapter_manifest()
    root = receiver / manifest["adapters"][adapter]["persistent"]["target"]
    original = root.read_text(encoding="utf-8")
    root.write_text("project preface\n\n" + original + "\nproject suffix\n", encoding="utf-8")
    _sync_from_manifest(receiver, adapter)
    assert root.read_text(encoding="utf-8").startswith("project preface\n\n")
    assert root.read_text(encoding="utf-8").endswith("\nproject suffix\n")

    unmarked = tmp_path / f"{adapter}-unmarked"
    target = unmarked / manifest["adapters"][adapter]["persistent"]["target"]
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("hand-written root without markers\n", encoding="utf-8")
    _, reported = _sync_from_manifest(unmarked, adapter)
    assert target in reported
    assert target.read_text(encoding="utf-8") == "hand-written root without markers\n"


def test_persistent_runtime_roots_delegate_without_a_common_library_preload():
    manifest = _adapter_manifest()
    for adapter, row in manifest["adapters"].items():
        for path in (PROJECT_ROOT / row["persistent"]["source"],
                     PROJECT_ROOT / row["persistent"]["target"]):
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            assert re.search(r"read\s+contract", text, re.IGNORECASE)
            preload_lines = [line for line in text.splitlines()
                             if line.lower().startswith(("load ", "- load "))]
            assert not any(all(name in line for name in
                               ("conventions.md", "glossary.md", "KNOWLEDGE.md"))
                           for line in preload_lines)


def test_primary_runtime_routes_do_not_read_the_tooling_manifest():
    for command, (_, workflow) in PRIMARY_ROUTES.items():
        assert ".tfw/adapters/manifest.yaml" not in (PROJECT_ROOT / workflow).read_text(encoding="utf-8")
        skill = PROJECT_ROOT / ".agents/skills" / f"tfw-{command}" / "SKILL.md"
        assert ".tfw/adapters/manifest.yaml" not in skill.read_text(encoding="utf-8")


def _codex_entry_errors(command, row, source, installed):
    errors = []
    normalized = source.casefold()
    if row["workflow"] not in source:
        errors.append("canonical route")
    if "completely" not in normalized:
        errors.append("complete load")
    if f"{row['role'].casefold()} role lock" not in normalized:
        errors.append("role lock")
    if "read contract" not in normalized:
        errors.append("read contract")
    if "stop" not in normalized:
        errors.append("stop")
    if source != installed:
        errors.append("source/copy parity")
    if "phase-a/evidence" in normalized or "command-entry-summary" in normalized:
        errors.append("generated evidence input")
    return [f"{command}: {error}" for error in errors]


def test_rtpsn_exact_eleven_codex_entries_reach_one_role_workflow_and_installed_copy():
    manifest = _adapter_manifest()
    errors = []
    assert len(manifest["commands"]) == 11 and len(manifest["adapters"]) == 4
    for command, row in manifest["commands"].items():
        source_path = PROJECT_ROOT / _expand(
            manifest["adapters"]["codex"]["commands"]["source"], command, row["workflow"])
        installed_path = PROJECT_ROOT / _expand(
            manifest["adapters"]["codex"]["commands"]["target"], command)
        errors.extend(_codex_entry_errors(
            command, row, source_path.read_text(encoding="utf-8"),
            installed_path.read_text(encoding="utf-8")))
    assert errors == []


@pytest.mark.parametrize("adapter", sorted(EXPECTED_PERSISTENT_TARGETS))
def test_rtpsn_clean_receivers_preserve_full_copy_or_thin_router_contract(tmp_path, adapter):
    receiver = tmp_path / adapter
    _install_from_manifest(receiver, adapter)
    manifest = _adapter_manifest()
    for command, row in manifest["commands"].items():
        target = receiver / _expand(manifest["adapters"][adapter]["commands"]["target"], command)
        if adapter == "codex":
            source = (PROJECT_ROOT / _expand(
                manifest["adapters"][adapter]["commands"]["source"], command,
                row["workflow"])).read_text(encoding="utf-8")
            assert _codex_entry_errors(command, row, source, target.read_text(encoding="utf-8")) == []
        else:
            assert target.read_bytes() == (PROJECT_ROOT / row["workflow"]).read_bytes()


@pytest.mark.parametrize(
    ("old", "new", "expected"),
    (
        (".tfw/workflows/plan.md", ".tfw/workflows/missing.md", "canonical route"),
        ("completely", "partially", "complete load"),
        ("Coordinator role lock", "Coordinator role hint", "role lock"),
        ("Stop when the workflow routes", "Continue when the workflow routes", "stop"),
    ),
)
def test_rtpsn_codex_entry_mutants_fail_at_their_own_boundary(old, new, expected):
    manifest = _adapter_manifest()
    row = manifest["commands"]["plan"]
    path = PROJECT_ROOT / ".tfw/adapters/codex/skills/tfw-plan/SKILL.md"
    source = path.read_text(encoding="utf-8")
    assert old in source
    mutant = source.replace(old, new, 1)
    errors = _codex_entry_errors("plan", row, mutant, mutant)
    assert f"plan: {expected}" in errors


def test_rtpsn_source_copy_and_generated_input_mutants_fail_independently():
    manifest = _adapter_manifest()
    row = manifest["commands"]["plan"]
    source = (PROJECT_ROOT / ".tfw/adapters/codex/skills/tfw-plan/SKILL.md").read_text(
        encoding="utf-8")
    assert "plan: source/copy parity" in _codex_entry_errors(
        "plan", row, source, source + "\ndrift\n")
    assert "plan: generated evidence input" in _codex_entry_errors(
        "plan", row, source + "\nRead phase-a/evidence/command-entry-summary.json.\n", source)


REVISE_CONSUMERS = ("plan", "handoff", "review")
UNIVERSAL_REVISE_CONTRADICTIONS = (
    "who orders the round in a TS revision",
    "Set `lifecycle: TS_DRAFT`",
    "The round is **your** artifact, in two writes",
    "every REVISE requires a TS revision",
    "STOP until owner verdict",
    "only the owner rules them",
    "wait for an owner ruling",
    "owner verdict required",
)

CRATM_UNIVERSAL_OWNER_READERS = (
    "logged owner verdict",
    "owner rules on something already done",
    "only the owner rules them",
    "wait for an owner ruling",
    "owner verdict required",
    "stop until owner verdict",
    "owner verdict leaves an executable bound",
    "then wait for the owner",
)


def _revise_consumer_errors(name: str, text: str) -> list[str]:
    errors = []
    if "The 🔄 REVISE route" not in text:
        errors.append(f"{name}: shared route authority is absent")
    for contradiction in UNIVERSAL_REVISE_CONTRADICTIONS:
        if contradiction.casefold() in text.casefold():
            errors.append(f"{name}: universal route survives: {contradiction}")
    return errors


def test_revision_2_revise_consumers_and_tracked_copies_share_one_route():
    conventions = (PROJECT_ROOT / ".tfw/conventions.md").read_text(encoding="utf-8")
    route = resolve_markdown_heading(conventions, "The 🔄 REVISE route")
    assert all(f"| {case} |" in route for case in
               ("Rung 1 only", "Any rung 2", "Rung 3", "Mixed rung 1 + 2"))
    assert "single routing authority" in route
    assert "no TS sibling" in route and "highest approved TS revision" in route
    assert "STOP until terminal verdict" in route

    for command in REVISE_CONSUMERS:
        canonical = PROJECT_ROOT / ".tfw/workflows" / f"{command}.md"
        text = canonical.read_text(encoding="utf-8")
        assert _revise_consumer_errors(command, text) == []
        for copy in (PROJECT_ROOT / ".claude/commands" / f"tfw-{command}.md",
                     PROJECT_ROOT / ".agent/workflows" / f"tfw-{command}.md"):
            assert copy.read_bytes() == canonical.read_bytes()


def test_revision_2_revise_consumer_contradiction_detector_fires():
    plan = (PROJECT_ROOT / ".tfw/workflows/plan.md").read_text(encoding="utf-8")
    assert _revise_consumer_errors("plan", plan) == []
    injected = plan + "\nEvery REVISE requires a TS revision.\n"
    assert _revise_consumer_errors("plan", injected) == [
        "plan: universal route survives: every REVISE requires a TS revision"
    ]


def _cratm_authority_consumer_errors() -> list[str]:
    required = {
        ".tfw/conventions.md": ("`status.md.owner` must be a declared human",
                                "Old: “only the owner rules.”",
                                "New ordinary delegation: nearest eligible non-proposer, else governing owner.",
                                "separate governing record authorizes the root Coordinator",
                                "nearest remaining immutable `true` principal"),
        ".tfw/workflows/plan.md": ("HL Contract` rule 8", "valid terminal verdict",
                                   "**No delegation claimed:**", "**Delegation claimed:**"),
        ".tfw/workflows/review.md": ("HL Contract` rule 8", "route to the **owner**, never the executor"),
        ".tfw/workflows/handoff.md": ("HL Contract` rule 8", "never an Executor decision"),
        ".tfw/templates/HL.md": ("Preserve the originating proposer", "Owner-reserved"),
        ".tfw/templates/RES.md": ("preserving origin", "resolved-ruler verdict required"),
    }
    errors = []
    for path, clauses in required.items():
        text = (PROJECT_ROOT / path).read_text(encoding="utf-8")
        errors.extend(f"{path}: {clause}" for clause in clauses if clause not in text)
    return errors


def _cratm_live_owner_reader_errors(overrides: dict[str, str] | None = None) -> list[str]:
    overrides = overrides or {}
    paths = (
        ".tfw/conventions.md", ".tfw/workflows/plan.md", ".tfw/workflows/review.md",
        ".tfw/workflows/handoff.md", ".tfw/templates/HL.md", ".tfw/templates/RES.md",
    )
    errors = []
    for path in paths:
        text = overrides.get(path, (PROJECT_ROOT / path).read_text(encoding="utf-8"))
        for line_no, line in enumerate(text.splitlines(), 1):
            folded = line.casefold()
            restrict_exception = (
                "no owner verdict required" in folded
                and ("restrict" in folded or "`restrict`" in folded))
            for reader in CRATM_UNIVERSAL_OWNER_READERS:
                if reader in folded and not restrict_exception:
                    errors.append(f"{path}:{line_no}: universal owner reader: {reader}")
    return errors


def test_cratm_phase_c_authority_consumers_and_six_copies_are_coherent():
    assert _cratm_authority_consumer_errors() == []
    assert _cratm_live_owner_reader_errors() == []
    for command in REVISE_CONSUMERS:
        canonical = PROJECT_ROOT / ".tfw/workflows" / f"{command}.md"
        for copy in (PROJECT_ROOT / ".claude/commands" / f"tfw-{command}.md",
                     PROJECT_ROOT / ".agent/workflows" / f"tfw-{command}.md"):
            assert copy.read_bytes() == canonical.read_bytes()


def test_cratm_phase_c_owner_only_consumer_mutant_is_rejected():
    handoff = (PROJECT_ROOT / ".tfw/workflows/handoff.md").read_text(encoding="utf-8")
    injected = handoff + "\nSTOP until owner verdict.\n"
    assert _revise_consumer_errors("handoff", injected) == [
        "handoff: universal route survives: STOP until owner verdict"
    ]
    conventions = (PROJECT_ROOT / ".tfw/conventions.md").read_text(encoding="utf-8")
    old = "a §12 row carrying the valid rule-8 verdict"
    mutant = conventions.replace(old, "a §12 row carrying a logged owner verdict", 1)
    assert mutant != conventions
    census = _cratm_live_owner_reader_errors({".tfw/conventions.md": mutant})
    assert len(census) == 1 and census[0].endswith(
        "universal owner reader: logged owner verdict")


def test_adapter_manifest_check_rejects_a_missing_command_and_wrong_role():
    manifest = _adapter_manifest()
    missing = yaml.safe_load(yaml.safe_dump(manifest))
    del missing["commands"]["research"]
    assert "command set is not exact" in _manifest_errors(missing)
    wrong = yaml.safe_load(yaml.safe_dump(manifest))
    wrong["commands"]["research"]["role"] = "Coordinator"
    assert "research: route/role mismatch" in _manifest_errors(wrong)
    unresolved = yaml.safe_load(yaml.safe_dump(manifest))
    unresolved["commands"]["init"]["workflow"] = ".tfw/workflows/missing.md"
    assert "init: canonical workflow is unresolved" in _manifest_errors(unresolved)
    extra = yaml.safe_load(yaml.safe_dump(manifest))
    extra["commands"]["invented"] = extra["commands"]["resume"]
    assert "command set is not exact" in _manifest_errors(extra)


def test_managed_block_check_rejects_duplicate_authority():
    template = (PROJECT_ROOT / ".tfw/adapters/claude-code/CLAUDE.md.template").read_text(
        encoding="utf-8")
    block = _managed_block(template, "CLAUDE").group(0)
    with pytest.raises(AssertionError, match="exactly one CLAUDE block"):
        _managed_block(template + "\n" + block, "CLAUDE")


def resolve_markdown_heading(text, heading):
    """Resolve one Markdown heading range and refuse missing or duplicate addresses."""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").splitlines(keepends=True)
    matches = []
    for index, line in enumerate(lines):
        found = re.match(r"^(#{1,6})\s+(.+?)\s*$", line.rstrip("\n"))
        if found:
            title = re.sub(r"^(?:§\s*)?\d+(?:\.\d+)*(?:[.)])?\s+", "", found.group(2)).strip()
            if title == heading:
                matches.append((index, len(found.group(1))))
    if len(matches) != 1:
        raise ValueError(f"heading {heading!r} resolved {len(matches)} times")
    start, level = matches[0]
    end = len(lines)
    for index in range(start + 1, len(lines)):
        found = re.match(r"^(#{1,6})\s+", lines[index])
        if found and len(found.group(1)) <= level:
            end = index
            break
    return "".join(lines[start:end])


def _antigravity_surface_errors(conventions, glossary, manifest, receiver):
    errors = []
    expected_rule = ".agents/rules/tfw.md"
    expected_commands = ".agents/workflows/tfw-{command}.md"
    singular = re.compile(r"(?<!s)\.agent/(?:rules|workflows)")
    for name, text in (("conventions", conventions), ("glossary", glossary)):
        if expected_rule not in text or expected_commands not in text:
            errors.append(f"{name}: plural authority missing")
        if singular.search(text):
            errors.append(f"{name}: singular authority advertised")
    row = manifest["adapters"]["antigravity"]
    if row["persistent"]["target"] != expected_rule:
        errors.append("manifest: persistent target mismatch")
    if row["commands"]["target"] != expected_commands:
        errors.append("manifest: command target mismatch")
    expected = {expected_rule} | {
        _expand(expected_commands, command) for command in manifest["commands"]
    }
    actual = {path.relative_to(receiver).as_posix() for path in receiver.rglob("*") if path.is_file()}
    if actual != expected:
        errors.append("receiver: plural target set mismatch")
    return errors


def test_antigravity_authority_is_plural_across_every_runtime_surface(tmp_path):
    conventions = resolve_markdown_heading(
        (PROJECT_ROOT / ".tfw/conventions.md").read_text(encoding="utf-8"), "Tool Adapter Pattern"
    )
    glossary = resolve_markdown_heading(
        (PROJECT_ROOT / ".tfw/glossary.md").read_text(encoding="utf-8"), "Tool Adapter"
    )
    manifest = _adapter_manifest()
    receiver = tmp_path / "antigravity"
    _install_from_manifest(receiver, "antigravity")
    assert _antigravity_surface_errors(conventions, glossary, manifest, receiver) == []

    mutations = []
    mutations.append((conventions.replace(".agents/", ".agent/", 1), glossary, manifest, receiver))
    mutations.append((conventions, glossary.replace(".agents/", ".agent/", 1), manifest, receiver))
    wrong_manifest = yaml.safe_load(yaml.safe_dump(manifest))
    wrong_manifest["adapters"]["antigravity"]["persistent"]["target"] = ".agent/rules/tfw.md"
    mutations.append((conventions, glossary, wrong_manifest, receiver))
    wrong_receiver = tmp_path / "singular-receiver"
    shutil.copytree(receiver, wrong_receiver)
    plural_rule = wrong_receiver / ".agents/rules/tfw.md"
    singular_rule = wrong_receiver / ".agent/rules/tfw.md"
    singular_rule.parent.mkdir(parents=True)
    shutil.move(plural_rule, singular_rule)
    mutations.append((conventions, glossary, manifest, wrong_receiver))
    assert all(_antigravity_surface_errors(*mutation) for mutation in mutations)


#: Payload files that are the PROJECT's, never the framework's to overwrite (conventions
#: §10.3): a `.yaml` at the payload root that has a template counterpart is created from the
#: template at init and owned by the project from then on. `update.md` Step 5 must exclude
#: every one of them by name, and print what it skipped.
PROJECT_OWNED_PAYLOAD_FILES = {"project_config.yaml", "knowledge_state.yaml"}


def test_every_project_owned_payload_file_is_excluded_from_the_copy():
    """AC-7: a project-owned file added to the payload without an exclusion fails here.

    `cp -r` of the payload overwrote a consumer's `project_config.yaml` with the framework's
    own (`name: my-project`) and its `knowledge_state.yaml` with the framework's consolidation
    state. The list is derived from the payload, not typed: every root `.yaml` with a
    template counterpart is project-owned.
    """
    payload = PROJECT_ROOT / ".tfw"
    owned = {p.name for p in payload.glob("*.yaml")
             if (payload / "templates" / p.name).exists()}
    assert owned == PROJECT_OWNED_PAYLOAD_FILES, (
        "the payload's project-owned files changed; update the exclusion list in update.md "
        "Step 5 and this registry together: " + ", ".join(sorted(owned)))
    update = (payload / "workflows" / "update.md").read_text(encoding="utf-8")
    apply_step = resolve_markdown_heading(update, "Apply Without State Loss")
    for name in owned:
        assert f".tfw/{name}" in update, f"{name} is project-owned and not named by update"
    assert "skipping and reporting project config/state" in apply_step
    assert "does not report both skips" in apply_step


#: Wordings a release retired, and where the rule that replaced each one now lives.
#:
#: A rule corrected in the canon is not corrected until every shipped copy of its OLD wording
#: is found. TFW-60/AA rewrote the absolute `UNDECLARED` prohibition in `conventions.md` and
#: `glossary.md` and left the identical sentence standing in the carrier template — the one
#: file a receiving project hand-authors from. The two edited files are the ones a reviewer
#: reads; the missed one is the one a project reads.
#:
#: The check is on the retired STRING, not on the concept, because a string is what a stale
#: copy actually carries. Add a row here whenever a release replaces a normative wording.
RETIRED_WORDINGS = [
    ("Normalizing such a value to a declared one is prohibited",
     "conventions.md §5: migration never normalizes, an accountable owner may resolve "
     "through a recorded transition event"),
    ("--validate",
     "gen_index.py --check tasks: one flag, three subjects"),
    ("--doctor",
     "gen_index.py --check project: never a third synonym"),
    ("__{kind}__{actor}",
     "the event filename's third component is an opaque token: __{kind}__{token}"),
    ("carries `actor`",
     "two identity fields, on_behalf_of and via. A writer is not named until TFW-54"),
    ("Commands never duplicate workflow content",
     "copies are the model (2.0.0-dirty.3, owner ruling 2026-08-28): every /tfw-* command "
     "is a byte copy of its workflow, re-synced by update.md Step 6. A consumer that "
     "rewrote its commands into thin adapters on the strength of the retired sentence "
     "re-copies them (TD-198)"),
]

#: Terms that are legitimate in prose which NARRATES a retirement and never legitimate in a
#: live instruction. `RETIRED_WORDINGS` above is the other job: a wording that is wrong
#: wherever it appears. Keeping them apart is what stops either check growing an exemption
#: list — `glossary.md` says the status legend *"moved here at 2.0.0 when the root Task Board
#: was removed"*, which is history, and an adapter file saying the same words is an order.
#:
#: Assembled from two literals on purpose: a registry that spells the term whole becomes a hit
#: on itself the moment anything greps for it. That is precisely how `update.md`'s own
#: instruction refuted its own check before this was noticed.
RETIRED_IN_INSTRUCTIONS = [
    ("Task" + " Board",
     "retired at 2.0.0: task state lives in {task}/status.md, and the portfolio view is the "
     "derived {container}/00-INDEX.md"),
]

#: Files that INSTRUCT. A stale wording here misleads a reader who is acting on it.
NORMATIVE_GLOBS = ("templates/**/*.md", "workflows/**/*.md", "migrations/*.md",
                   "conventions.md", "glossary.md", "README.md", "quickstart.md",
                   "compilable_contract.md")

#: `CHANGELOG.md` is excluded, and the reason is a rule rather than a convenience: a
#: changelog RECORDS what a release did. Its `2.0.0-dirty` entry states the absolute
#: prohibition because that is what `2.0.0-dirty` shipped, and rewriting it would make the
#: record describe something that did not happen. `adapters/` is excluded for the same
#: reason its own path check exists separately: it is tool-specific text, not canon.


#: Paths a payload file names deliberately without shipping them. Each is annotated, because
#: an exemption nobody can explain becomes a place to hide a broken reference.
PAYLOAD_PATH_EXEMPT = {
    "CHANGELOG.md":
        "a changelog RECORDS what a release shipped. Its historical entries name paths that "
        "were correct at those releases, and rewriting them would make the record describe "
        "something that did not happen",
    "migrations/2.0.0.md":
        "the migration guide names the retired files an operator is told to DELETE. Naming "
        "them is the instruction",
}

#: Three reference forms. The third is the one that was missed: a bare filename with no
#: directory at all, which both earlier scans were blind to. `conventions.md` §10.4 named a
#: deleted template that way and survived four releases behind two checks that could not see
#: it — which is the mechanism gap, not the reference.
PAYLOAD_PATH_FORMS = (
    ("prefixed", re.compile(
        r"`(\.tfw/(?:templates|workflows|scripts|migrations|adapters)/[A-Za-z0-9_./-]+"
        r"\.(?:md|py|yaml|yml|template))`")),
    ("bare-dir", re.compile(
        r"`((?:templates|workflows|scripts|migrations|adapters)/[A-Za-z0-9_./-]+"
        r"\.(?:md|py|yaml|yml|template))`")),
    ("bare-file", re.compile(
        r"`([a-z][a-z0-9_]*\.(?:md|yaml|yml|py))`")),
)

#: A bare filename is only a payload reference if the payload has a file of that name
#: somewhere. `README.md` and `desktop.ini` are not claims about `.tfw/`.
def _bare_file_targets(payload):
    index = {}
    for f in payload.rglob("*"):
        if f.is_file() and ".upstream" not in f.parts:
            index.setdefault(f.name, []).append(f)
    return index


def payload_path_findings():
    """Every path a payload file names that the payload does not ship, in all three forms."""
    payload = PROJECT_ROOT / ".tfw"
    by_name = _bare_file_targets(payload)
    findings = []
    for f in sorted(payload.rglob("*")):
        if not f.is_file() or f.suffix not in {".md", ".yaml", ".yml", ".template"}:
            continue
        if ".upstream" in f.parts:
            continue
        rel = f.relative_to(payload).as_posix()
        if rel in PAYLOAD_PATH_EXEMPT:
            continue
        text = f.read_text(encoding="utf-8", errors="replace")
        for form, pattern in PAYLOAD_PATH_FORMS:
            for match in pattern.finditer(text):
                named = match.group(1)
                if form == "prefixed":
                    exists = (PROJECT_ROOT / named).exists()
                elif form == "bare-dir":
                    exists = (payload / named).exists()
                else:
                    # A bare filename claims a payload file of that name exists somewhere.
                    # Only checked when the payload once had one: otherwise every ordinary
                    # word in backticks becomes a path claim.
                    if named not in by_name and named not in RETIRED_PAYLOAD_FILENAMES:
                        continue
                    exists = named in by_name
                if not exists:
                    findings.append(f"{rel} -> {named}  [{form}]")
    return sorted(set(findings))


#: Bare filenames the payload once shipped and no longer does. Without this the bare-file form
#: cannot fire at all: a deleted file is absent from the name index, so the check would skip
#: exactly the reference it exists to catch. This is the list §10.4's dead example needed.
RETIRED_PAYLOAD_FILENAMES = {
    "topic_file.md", "team_profile.md", "journal_event.md",
}


def test_every_path_a_payload_file_names_resolves():
    """TD-193. Two independent sources named this gap before it was closed.

    The reviewer called it *"the mechanism gap that let TD-192 and TD-194 survive"*; an
    external operator's report found the same thing from the other side. Both were right, and
    both understated it — the earlier checks covered `.tfw/adapters/**` in one reference form,
    so a dead path in `conventions.md` written as a bare filename was invisible to everything.
    """
    findings = payload_path_findings()
    assert not findings, ("payload files name paths the payload does not ship:" + chr(10)
                          + chr(10).join(findings))


def test_the_payload_path_check_fires_in_all_three_forms(tmp_path):
    """Proven to fail before it is trusted to pass — once per form, since a form that cannot
    fire is the defect this replaced."""
    for form, sample in (
        ("prefixed", "routes to `.tfw/workflows/definitely-not-here.md`"),
        ("bare-dir", "copy `templates/definitely_not_here.md` into place"),
        ("bare-file", "named `topic_file.md` (not `TOPIC_FILE.md`)"),
    ):
        probe = PROJECT_ROOT / ".tfw" / "templates" / "_probe.md"
        probe.write_text(sample + chr(10), encoding="utf-8")
        try:
            findings = payload_path_findings()
            assert any("_probe.md" in f and form in f for f in findings), (form, findings)
        finally:
            probe.unlink()
    # and with nothing planted, the payload is clean
    assert payload_path_findings() == []


def test_no_normative_file_states_a_retired_rule():
    """The mechanical form of "did the rewrite reach every copy".

    Not a wording check. Two shipped normative files giving a reader opposite instructions
    about the same act is the defect, and the reader most likely to hit it is the one who
    has only the payload.

    **Reach, stated so the silence is not over-read.** This covers prose a reader *acts on*:
    templates, workflows, migrations and the named root documents. It does **not** scan the
    payload scripts' own comments and docstrings — a comment explaining that a flag was
    retired legitimately names it, and no mechanical rule separates that from a docstring
    that still instructs. One such stale docstring was found by hand in this phase
    (`test_gen_index.py` naming `--validate` as the build gate command), and that residual gap
    is recorded in the RF rather than papered over with an allowlist that would rot.
    """
    payload = PROJECT_ROOT / ".tfw"
    files = sorted({p for pattern in NORMATIVE_GLOBS for p in payload.glob(pattern)
                    if p.is_file()})
    assert files, "no normative payload files found"
    offenders = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        for retired, replacement in RETIRED_WORDINGS:
            if retired in text:
                line = next(n for n, l in enumerate(text.splitlines(), 1) if retired in l)
                offenders.append(
                    f"{path.relative_to(PROJECT_ROOT).as_posix()}:{line}: "
                    f"{retired!r} was retired. Now: {replacement}")
    assert not offenders, ("a normative payload file states a retired rule:" + chr(10)
                           + chr(10).join(offenders))


#: The adapter layer: byte copies of payload workflows, plus each tool's own entry point.
#: A stale copy here is a second set of instructions contradicting the payload, and until
#: `2.0.0-dirty.3` nothing read it — one external project carried six such files.
ADAPTER_SURFACE = (".claude/commands", ".agent/workflows", ".agents/skills", ".agent/rules",
                   ".cursor/rules", "AGENTS.md", "CLAUDE.md")


def test_no_adapter_file_states_a_retired_rule():
    """Item 6, as a test rather than as a command somebody remembers to run.

    The manual grep is still in `update.md` because a receiving project cannot run this file.
    Here it is a gate: the same registry, the other surface.
    """
    paths = []
    for entry in ADAPTER_SURFACE:
        target = PROJECT_ROOT / entry
        if target.is_file():
            paths.append(target)
        elif target.is_dir():
            paths.extend(p for p in target.rglob("*") if p.is_file() and p.suffix == ".md")
    assert paths, "no adapter surface found"
    offenders = []
    for path in sorted(paths):
        text = path.read_text(encoding="utf-8", errors="replace")
        # Both registries: an adapter file is instructions end to end, so it may carry
        # neither a retired wording nor a retired term.
        for retired, replacement in [*RETIRED_WORDINGS, *RETIRED_IN_INSTRUCTIONS]:
            if retired in text:
                line = next(n for n, l in enumerate(text.splitlines(), 1) if retired in l)
                offenders.append(
                    f"{path.relative_to(PROJECT_ROOT).as_posix()}:{line}: "
                    f"{retired!r} was retired. Now: {replacement}")
    assert not offenders, ("an adapter file states a retired rule:" + chr(10)
                           + chr(10).join(offenders))


def test_the_retired_rule_check_actually_fires(tmp_path):
    """Proven to fail before it is trusted to pass."""
    retired, _ = RETIRED_WORDINGS[0]
    assert retired, "the registry must not be empty"
    stale = tmp_path / "stale.md"
    stale.write_text("A rule: " + retired + ".\n", encoding="utf-8")
    assert any(r in stale.read_text(encoding="utf-8") for r, _ in RETIRED_WORDINGS), \
        "the registry must match the wording it retires"
    fresh = tmp_path / "fresh.md"
    fresh.write_text("Migration never normalizes; an owner may resolve.\n", encoding="utf-8")
    assert not any(r in fresh.read_text(encoding="utf-8") for r, _ in RETIRED_WORDINGS)


def test_the_adapter_retired_term_check_actually_fires(tmp_path):
    """A registry that cannot produce a finding is ceremony."""
    term, _ = RETIRED_IN_INSTRUCTIONS[0]
    probe = PROJECT_ROOT / ".claude" / "commands" / "_probe.md"
    probe.parent.mkdir(parents=True, exist_ok=True)
    probe.write_text(f"Update the {term} row.{chr(10)}", encoding="utf-8")
    try:
        with pytest.raises(AssertionError, match="retired"):
            test_no_adapter_file_states_a_retired_rule()
    finally:
        probe.unlink()
    # and clean once more with nothing planted
    test_no_adapter_file_states_a_retired_rule()


def test_the_status_template_examples_parse_and_validate():
    """A carrier template whose own example is invalid teaches the mistake it warns about.

    The shipped example modelled the unquoted form — `title: short task name` — and the
    first project to hand-author this carrier produced five unparseable files in a row.
    Both the skeleton and the worked example are now checked against the real validator,
    not eyeballed.
    """
    import yaml
    sys.path.insert(0, str(PROJECT_ROOT / "tools"))
    import tfw_state

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
    problems = tfw_state.validate_status(example)
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

#: `{ID}` already ends in the slug, so anything appended doubles it — with exactly one
#: exception, and `conventions.md` §4 mandates it: `__rev{N}`, the revision ordinal. A title
#: suffix duplicates what `status.md` already holds, so it stays refused; an ordinal lives
#: nowhere else, so the filename is its only home. Anything else after `{ID}__` still fires.
#: The lookahead spells `rev{N}.md`, not `rev{N}`, because the ordinal must **end** the name:
#: `rev{N}` alone only asks what follows `{ID}__`, so `TS__{ID}__rev{N}__extra.md` slipped past
#: it — a suffix hidden behind the one mandated exception. The three assertions below pin the
#: exception from both directions, before the ordinal and after it; without the third, widening
#: this regex is the one way the naming rule can be broken by a change that reports itself as
#: passing.
DOUBLED_SLUG = re.compile(r"\{ID\}__(?!rev\{N\}\.md)")

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
    assert DOUBLED_SLUG.search("TS__{ID}__draft.md")
    assert DOUBLED_SLUG.search("TS__{ID}__rev{N}__extra.md")  # a suffix AFTER the ordinal
    assert ACTORLESS_EVENT.search("20260826-143000__created.md")
    assert ACTORLESS_EVENT.search("{YYYYMMDD-HHMMSS}__{kind}.md".replace("{kind}", "handoff"))

    # and the legitimate forms must NOT fire
    assert not BARE_ID_AS_NAME.search("created: 20260819-000000")
    assert not BARE_ID_AS_NAME.search("workspace/2026/20260826-143000__query_redesign/")
    assert not DOUBLED_SLUG.search("RES__{ID}.md")
    assert not DOUBLED_SLUG.search("TS__{ID}__rev{N}.md")
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


VBSA_BASELINE = "f5a96af07dcdc4230ecf31100bd155a3dca09604"
VBSA_SCOPE_KEYS = {
    "decomposition_trigger_files": 50,
    "decomposition_trigger_loc": 5000,
    "owner_escalation_multiplier": 2,
}
VBSA_ADAPTERS = ("plan", "handoff", "review", "config", "update", "init")


def _git_bytes(ref: str, path: str) -> bytes:
    result = subprocess.run(["git", "show", f"{ref}:{path}"], cwd=PROJECT_ROOT,
                            capture_output=True, check=True)
    return result.stdout


def _vbsa_update_mapping(text: str) -> dict[str, str | None]:
    match = re.search(
        r"### Project-owned scope-budget migration\n(?P<body>.*?)(?=\n## )", text, re.DOTALL)
    assert match, "version-agnostic migration section is missing"
    mapping = {}
    for old, new in re.findall(r"^\| `([^`]+)` \| (`[^`]+`|—) \|", match["body"], re.MULTILINE):
        mapping[old] = None if new == "—" else new.strip("`")
    return mapping


def _apply_vbsa_mapping(old: dict[str, int], mapping: dict[str, str | None]) -> dict[str, int]:
    result = {new: old[key] for key, new in mapping.items() if new is not None}
    result["owner_escalation_multiplier"] = 2
    return result


def test_vbsa_config_has_exact_three_key_contract_in_live_and_starter_files():
    for relative in (".tfw/project_config.yaml", ".tfw/templates/project_config.yaml"):
        scope = yaml.safe_load((PROJECT_ROOT / relative).read_text(encoding="utf-8"))["tfw"]["scope_budgets"]
        assert scope == VBSA_SCOPE_KEYS


def test_vbsa_migration_preserves_values_and_removes_only_retired_keys():
    update = (PROJECT_ROOT / ".tfw/workflows/update.md").read_text(encoding="utf-8")
    mapping = _vbsa_update_mapping(update)
    assert mapping == {
        "max_files_per_phase": "decomposition_trigger_files",
        "max_loc": "decomposition_trigger_loc",
        "max_new_files": None,
        "max_modified_files": None,
    }
    old = {"max_files_per_phase": 17, "max_new_files": 19,
           "max_loc": 2300, "max_modified_files": 13}
    assert _apply_vbsa_mapping(old, mapping) == {
        "decomposition_trigger_files": 17,
        "decomposition_trigger_loc": 2300,
        "owner_escalation_multiplier": 2,
    }


def test_vbsa_migration_mutant_changes_result_before_rejection():
    update = (PROJECT_ROOT / ".tfw/workflows/update.md").read_text(encoding="utf-8")
    mutant = update.replace("| `max_loc` | `decomposition_trigger_loc` |",
                            "| `max_loc` | `decomposition_trigger_files` |", 1)
    produced = _apply_vbsa_mapping({"max_files_per_phase": 17, "max_loc": 2300,
                                    "max_new_files": 19, "max_modified_files": 13},
                                   _vbsa_update_mapping(mutant))
    assert produced != {"decomposition_trigger_files": 17,
                        "decomposition_trigger_loc": 2300,
                        "owner_escalation_multiplier": 2}
    with pytest.raises(AssertionError):
        assert produced == VBSA_SCOPE_KEYS


def _vbsa_north_star_policy(text: str) -> dict[str, str]:
    match = re.search(
        r"### Receiver North-Star operation\n(?P<body>.*?)(?=\n### |\n## )", text, re.DOTALL)
    assert match, "receiver North-Star operation does not resolve"
    return {
        state.replace("`", ""): operation
        for state, operation in re.findall(
            r"^\| (.+?) \| `([A-Z_]+)` \|$", match["body"], re.MULTILINE)
    }


def _vbsa_north_star_policies(texts: dict[str, str]) -> dict[str, dict[str, str]]:
    return {name: _vbsa_north_star_policy(text) for name, text in texts.items()}


def _validate_vbsa_north_star_policies(policies: dict[str, dict[str, str]]) -> None:
    common = {
        "Existing root README.md": "PRESERVE_BYTES",
        "Existing .tfw/README.md": "PRESERVE_BYTES",
        "Starter quotation": "DO_NOT_INJECT",
    }
    expected = {
        "init": {**common, "Absent project North Star": "CREATE_FROM_DISCOVERY"},
        "update": {**common, "Absent project North Star": "LEAVE_ABSENT"},
    }
    if policies != expected:
        raise ValueError("receiver North-Star preservation policy changed")


def _execute_vbsa_north_star_policy(
        receiver: Path, starter: Path, policy: dict[str, str]) -> None:
    targets = {
        "Existing root README.md": (receiver / "README.md", starter / "README.md"),
        "Existing .tfw/README.md": (receiver / ".tfw/README.md", starter / ".tfw/README.md"),
    }
    for state, (destination, source) in targets.items():
        operation = policy[state]
        if operation == "PRESERVE_BYTES":
            continue
        if operation == "OVERWRITE_FROM_STARTER":
            destination.write_bytes(source.read_bytes())
            continue
        raise ValueError(f"unsupported receiver operation: {operation}")


def _vbsa_receiver_fixture(tmp_path: Path, name: str):
    receiver, starter = tmp_path / f"{name}-receiver", tmp_path / f"{name}-starter"
    (receiver / ".tfw").mkdir(parents=True)
    (starter / ".tfw").mkdir(parents=True)
    receiver_bytes = {
        "README.md": b"# Receiver root North Star\n",
        ".tfw/README.md": b"# Receiver TFW North Star\n",
        "approved-ts.md": b"# Approved historical TS\n",
    }
    starter_bytes = {
        "README.md": b"# Starter root\n",
        ".tfw/README.md": b"# Starter quotation must not cross\n",
    }
    for path, payload in receiver_bytes.items():
        target = receiver / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
    for path, payload in starter_bytes.items():
        target = starter / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
    return receiver, starter, receiver_bytes


def test_vbsa_update_and_init_execute_receiver_north_star_preservation(tmp_path):
    texts = {name: (PROJECT_ROOT / f".tfw/workflows/{name}.md").read_text(encoding="utf-8")
             for name in ("init", "update")}
    policies = _vbsa_north_star_policies(texts)
    _validate_vbsa_north_star_policies(policies)
    for name, policy in policies.items():
        receiver, starter, expected = _vbsa_receiver_fixture(tmp_path, name)
        _execute_vbsa_north_star_policy(receiver, starter, policy)
        assert {path: (receiver / path).read_bytes() for path in expected} == expected


def test_vbsa_receiver_overwrite_mutant_changes_bytes_before_rejection(tmp_path):
    texts = {name: (PROJECT_ROOT / f".tfw/workflows/{name}.md").read_text(encoding="utf-8")
             for name in ("init", "update")}
    texts["init"] = texts["init"].replace("PRESERVE_BYTES", "OVERWRITE_FROM_STARTER")
    produced = _vbsa_north_star_policies(texts)
    receiver, starter, expected = _vbsa_receiver_fixture(tmp_path, "mutant")
    _execute_vbsa_north_star_policy(receiver, starter, produced["init"])
    assert any((receiver / path).read_bytes() != payload
               for path, payload in expected.items() if path != "approved-ts.md")
    with pytest.raises(ValueError, match="preservation policy changed"):
        _validate_vbsa_north_star_policies(produced)


def test_vbsa_saint_principle_is_local_and_not_injected_into_foreign_north_stars():
    quote = "Perfection is achieved not when there is nothing left to add"
    local = (PROJECT_ROOT / ".tfw/README.md").read_text(encoding="utf-8")
    assert local.count(quote) == 1
    ns2 = local.partition("## NS2 — Principles")[2].partition("## NS3")[0]
    assert "2. **The Saint-Exupéry Principle.**" in ns2 and quote in ns2
    for path in ("README.md", "README.ru.md", "README.kk.md"):
        assert quote not in (PROJECT_ROOT / path).read_text(encoding="utf-8")
        assert quote.encode() not in (PROJECT_ROOT / path).read_bytes()
    assert quote not in (PROJECT_ROOT / ".tfw/workflows/update.md").read_text(encoding="utf-8")
    assert quote not in (PROJECT_ROOT / ".tfw/workflows/init.md").read_text(encoding="utf-8")


def _vbsa_release_entry(changelog: str, installed_version: str) -> tuple[str, str]:
    """The introducing entry survives the Unreleased -> versioned release transition."""
    headings = list(re.finditer(r"^## \[([^\]]+)\][^\n]*\n", changelog, re.MULTILINE))
    entries = [
        (heading[1], changelog[heading.end():headings[index + 1].start()
                              if index + 1 < len(headings) else len(changelog)])
        for index, heading in enumerate(headings)
    ]
    introducing = [(version, body) for version, body in entries
                   if "Scope accounting now governs only the declared value-bearing surface." in body]
    assert len(introducing) == 1, "exactly one introducing scope-accounting entry must resolve"
    version, body = introducing[0]
    assert all(term in body for term in (
        "max_files_per_phase", "max_loc", "max_new_files", "max_modified_files",
        "decomposition_trigger_files", "decomposition_trigger_loc",
        "owner_escalation_multiplier", "approval epoch", "/tfw-release")), "migration is incomplete"
    if version != "Unreleased":
        assert re.fullmatch(r"\d+\.\d+\.\d+", version), "introducing version must be explicit"
        assert tuple(map(int, version.split("."))) <= tuple(map(int, installed_version.split("."))), \
            "introducing release cannot be newer than the installed version"
    return version, body


def test_vbsa_release_preserves_migration_before_and_after_publication():
    changelog = (PROJECT_ROOT / ".tfw/CHANGELOG.md").read_text(encoding="utf-8")
    release = (PROJECT_ROOT / "RELEASE.md").read_text(encoding="utf-8")
    installed = (PROJECT_ROOT / ".tfw/VERSION").read_text(encoding="utf-8").strip()
    version, body = _vbsa_release_entry(changelog, installed)
    assert ".tfw/migrations/{major}.0.0.md" in release
    assert "before `.tfw/VERSION` changes" in release
    baseline_major = int(_git_bytes(VBSA_BASELINE, ".tfw/VERSION").decode().split(".")[0])
    if version != "Unreleased" and int(version.split(".")[0]) > baseline_major:
        guide = PROJECT_ROOT / ".tfw/migrations" / f"{version.split('.')[0]}.0.0.md"
        assert guide.is_file(), "a major introducing release requires its version-named guide"
        guide_text = guide.read_text(encoding="utf-8")
        assert all(term in guide_text for term in (
            "decomposition_trigger_files", "decomposition_trigger_loc",
            "owner_escalation_multiplier", "approval epoch"))


@pytest.mark.parametrize("placement", ("Unreleased", "2.2.0", "3.0.0"))
def test_vbsa_release_entry_accepts_both_lifecycle_locations(placement):
    changelog = (PROJECT_ROOT / ".tfw/CHANGELOG.md").read_text(encoding="utf-8")
    _, body = _vbsa_release_entry(changelog, "3.0.0")
    fixture = f"## [{placement}]\n{body}\n## [1.0.0]\nUnrelated history.\n"
    assert _vbsa_release_entry(fixture, "3.0.0") == (placement, body + "\n")


@pytest.mark.parametrize("defect", ("missing", "mapping", "epoch", "duplicate", "future"))
def test_vbsa_release_entry_rejects_lost_or_ambiguous_migration(defect):
    changelog = (PROJECT_ROOT / ".tfw/CHANGELOG.md").read_text(encoding="utf-8")
    _, body = _vbsa_release_entry(changelog, "3.0.0")
    fixture = f"## [2.2.0]\n{body}"
    if defect == "missing":
        fixture = "## [2.2.0]\nMigration is described somewhere else.\n"
    elif defect == "mapping":
        fixture = fixture.replace("decomposition_trigger_loc", "lost_mapping")
    elif defect == "epoch":
        fixture = fixture.replace("approval epoch", "lost_epoch")
    elif defect == "duplicate":
        fixture += f"\n## [Unreleased]\n{body}"
    else:
        fixture = fixture.replace("## [2.2.0]", "## [3.0.0]", 1)
    with pytest.raises(AssertionError):
        _vbsa_release_entry(fixture, "2.2.0")


def test_release_versions_migration_and_onboarding_support_receiver_update():
    changelog = (PROJECT_ROOT / ".tfw/CHANGELOG.md").read_text(encoding="utf-8")
    installed = (PROJECT_ROOT / ".tfw/VERSION").read_text(encoding="utf-8").strip()
    for path in (".tfw/project_config.yaml", ".tfw/templates/project_config.yaml"):
        config = yaml.safe_load((PROJECT_ROOT / path).read_text(encoding="utf-8"))
        assert config["tfw"]["version"] == installed, f"release version drift in {path}"
    version, body = _vbsa_release_entry(changelog, installed)
    if version == "Unreleased":
        return
    assert f"(migrations/{version}.md)" in body
    guide = (PROJECT_ROOT / f".tfw/migrations/{version}.md").read_text(encoding="utf-8")
    assert all(term in guide for term in (
        "first read `migrations/2.0.0.md`", "decomposition_trigger_files",
        "decomposition_trigger_loc", "owner_escalation_multiplier", "approval epoch",
        ".tfw/templates/briefing.md", "tfw.content_language", "Added/Changed/Fixed/Removed",
        "record delivery in the update checklist"))


@pytest.mark.parametrize("name", VBSA_ADAPTERS)
def test_vbsa_adapter_copy_is_exact(name):
    canonical = (PROJECT_ROOT / f".tfw/workflows/{name}.md").read_bytes()
    assert (PROJECT_ROOT / f".agent/workflows/tfw-{name}.md").read_bytes() == canonical
    assert (PROJECT_ROOT / f".claude/commands/tfw-{name}.md").read_bytes() == canonical


def test_vbsa_adapter_manifest_topology_is_unchanged_from_baseline():
    path = ".tfw/adapters/manifest.yaml"
    assert (PROJECT_ROOT / path).read_bytes() == _git_bytes(VBSA_BASELINE, path)


# RTPSN Phase B integration: manifest-derived route coverage, exact receivers, and protected paths.
RTPSN_PHASE_B_BASELINE = "83b31ff8d6cdb879fdf4f20578fa688b48863f8a"
RTPSN_TASK_ROUTES = frozenset({"plan", "research", "handoff", "review", "resume", "docs", "init"})
RTPSN_PROJECT_ROUTES = frozenset({"knowledge", "release", "update", "config"})
RTPSN_MODE_MARKERS = {
    "plan": ("For an existing task", "With the approved ID"),
    "research": ("After task and iteration resolution", "Iteration never supplies `PHASE`"),
    "handoff": ("After Read Contract item 1", "WORK=EXEC"),
    "review": ("After Bootstrap item 1", "WORK=REVIEW"),
    "resume": ("After one task resolves", "only when exactly one resolves"),
    "docs": ("Auto/manual:", "Batch: skip."),
    "init": ("Full-init: after-item4/before-item5.", "Attach/repair:"),
}
RTPSN_ORDER_ANCHORS = {
    "plan-existing": ("## Step 1: Load context", "### Session identity checkpoint", "## Step 2: Knowledge Gate"),
    "plan-new": ("**The whole directory name is the identifier.**", "3. **Apply session identity.**", "4. **Write the task's own state"),
    "research": ("Resume from first missing stage.", "## Session identity checkpoint", "## Who Is Acting"),
    "handoff": ("## Read Contract", "## Session identity checkpoint", "## Who Is Acting"),
    "review": ("## Read Contract", "## Session identity checkpoint", "> **Reviewer Identity:**"),
    "resume": ("1. Resolve the selected task", "5. After one task resolves", "## 2. Build the Matrix"),
    "docs": ("Modes:", "### Session identity checkpoint", "For each selection decide"),
    "init": ("4. Read the clock once", "### Session identity checkpoint", "5. From the status/event templates"),
}


def _rtpsn_identity_route_errors(text: str, before: str, marker: str, after: str) -> list[str]:
    errors = []
    counts = {value: text.count(value) for value in (before, marker, after)}
    if counts != {before: 1, marker: 1, after: 1}:
        errors.append(f"anchors:{counts}")
    elif not text.index(before) < text.index(marker) < text.index(after):
        errors.append("order")
    return errors


def _rtpsn_git_paths(prefix: str) -> tuple[str, ...]:
    output = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", RTPSN_PHASE_B_BASELINE, "--", prefix],
        cwd=PROJECT_ROOT, text=True, encoding="utf-8", capture_output=True, check=True,
    ).stdout
    return tuple(path for path in output.splitlines() if path)


def test_rtpsn_phase_b_manifest_census_classifies_all_eleven_routes_once():
    manifest = _adapter_manifest()
    commands = set(manifest["commands"])
    assert commands == RTPSN_TASK_ROUTES | RTPSN_PROJECT_ROUTES
    assert RTPSN_TASK_ROUTES.isdisjoint(RTPSN_PROJECT_ROUTES)
    for command, row in manifest["commands"].items():
        text = (PROJECT_ROOT / row["workflow"]).read_text(encoding="utf-8")
        if command in RTPSN_TASK_ROUTES:
            assert "Session identity" in text
            assert all(marker in text for marker in RTPSN_MODE_MARKERS[command])
        else:
            assert "Session identity" not in text


def test_rtpsn_phase_b_identity_checkpoints_follow_resolution_and_precede_work():
    for case, (before, marker, after) in RTPSN_ORDER_ANCHORS.items():
        command = case.split("-", 1)[0]
        path = _adapter_manifest()["commands"][command]["workflow"]
        text = (PROJECT_ROOT / path).read_text(encoding="utf-8")
        assert _rtpsn_identity_route_errors(text, before, marker, after) == [], case


def test_rtpsn_phase_b_deleted_and_reordered_checkpoint_mutants_fail_locally():
    for case, (before, marker, after) in RTPSN_ORDER_ANCHORS.items():
        command = case.split("-", 1)[0]
        text = (PROJECT_ROOT / _adapter_manifest()["commands"][command]["workflow"]).read_text(
            encoding="utf-8")
        deleted = text.replace(marker, "", 1)
        reordered = text.replace(marker, "RTPSN_TEMP", 1).replace(
            after, marker, 1).replace("RTPSN_TEMP", after, 1)
        assert _rtpsn_identity_route_errors(deleted, before, marker, after)
        assert _rtpsn_identity_route_errors(reordered, before, marker, after) == ["order"]


@pytest.mark.parametrize("adapter", sorted(EXPECTED_PERSISTENT_TARGETS))
def test_rtpsn_phase_b_clean_receivers_have_exact_identity_classification(tmp_path, adapter):
    receiver = tmp_path / f"phase-b-{adapter}"
    _install_from_manifest(receiver, adapter)
    manifest = _adapter_manifest()
    assert len(manifest["commands"]) == 11
    for command, row in manifest["commands"].items():
        target = receiver / _expand(manifest["adapters"][adapter]["commands"]["target"], command)
        installed = target.read_text(encoding="utf-8")
        canonical = (PROJECT_ROOT / row["workflow"]).read_text(encoding="utf-8")
        if adapter == "codex":
            assert row["workflow"] in installed
            assert installed.casefold().count("role lock") == 1
        else:
            assert installed == canonical
            assert len(re.findall(r"^> .*ROLE LOCK", installed, re.MULTILINE)) == 1
        assert ("Session identity" in canonical) == (command in RTPSN_TASK_ROUTES)
        if adapter != "codex":
            assert ("Session identity" in installed) == (command in RTPSN_TASK_ROUTES)


def test_rtpsn_phase_b_all_eleven_tracked_full_copy_routes_are_byte_exact():
    manifest = _adapter_manifest()
    for command, row in manifest["commands"].items():
        canonical = (PROJECT_ROOT / row["workflow"]).read_bytes()
        assert (PROJECT_ROOT / f".claude/commands/tfw-{command}.md").read_bytes() == canonical
        assert (PROJECT_ROOT / f".agent/workflows/tfw-{command}.md").read_bytes() == canonical


def test_rtpsn_phase_b_codex_manifest_roots_phase_a_cratm_and_project_routes_are_protected():
    manifest = _adapter_manifest()
    protected = {".tfw/adapters/manifest.yaml", "AGENTS.md", "CLAUDE.md"}
    for command, row in manifest["commands"].items():
        protected.add(_expand(manifest["adapters"]["codex"]["commands"]["source"],
                              command, row["workflow"]))
        protected.add(_expand(manifest["adapters"]["codex"]["commands"]["target"], command))
    protected.update(manifest["commands"][command]["workflow"] for command in RTPSN_PROJECT_ROUTES)
    protected.update(_rtpsn_git_paths("workspace/2026/TFW_20260905-124029_RTPSN/phase-a"))
    protected.update(_rtpsn_git_paths("workspace/2026/TFW_20260902-111644_CRATM"))
    assert len({path for path in protected if "/skills/tfw-" in path}) == 22
    rtbo_declared = {
        f".tfw/workflows/{name}.md" for name in ("plan", "knowledge", "init", "update")
    } | {
        f"{base}/tfw-{name}.md"
        for base in (".claude/commands", ".agent/workflows")
        for name in ("plan", "knowledge", "init", "update")
    }
    for path in sorted(protected):
        if path in rtbo_declared:
            continue
        if path == "AGENTS.md":
            before = _git_bytes(RTPSN_PHASE_B_BASELINE, path).decode("utf-8")
            after = (PROJECT_ROOT / path).read_text(encoding="utf-8")
            old_block, new_block = _managed_block(before, "CODEX"), _managed_block(after, "CODEX")
            assert old_block and new_block
            assert before[:old_block.start()] == after[:new_block.start()]
            assert before[old_block.end():] == after[new_block.end():]
        else:
            assert (PROJECT_ROOT / path).read_bytes() == _git_bytes(RTPSN_PHASE_B_BASELINE, path), path


def test_rtpsn_phase_b_runtime_sources_never_consume_task_spec_or_generated_evidence():
    manifest = _adapter_manifest()
    for command in RTPSN_TASK_ROUTES:
        workflow = (PROJECT_ROOT / manifest["commands"][command]["workflow"]).read_text(encoding="utf-8")
        if command != "init":
            assert ".tfw/adapters/manifest.yaml" not in workflow
        else:
            assert workflow.count(".tfw/adapters/manifest.yaml") == 1  # pre-existing attach/repair input
        assert "TFW_20260905-124029_RTPSN/phase-b/evidence" not in workflow
        assert "TS__phase-b__session_identity_ergonomics" not in workflow
        skill = (PROJECT_ROOT / _expand(manifest["adapters"]["codex"]["commands"]["source"],
                                        command, manifest["commands"][command]["workflow"])).read_text(
                                            encoding="utf-8")
        assert "Session identity" not in skill


# CRATM Phase D integration: literal selector, accepted consumers, and historical boundaries.
PHASE_D_BASELINE = "8e68ab37d300122ff110500ad58f354f76b6210f"
PHASE_D_PREFIX = "workspace/2026/TFW_20260902-111644_CRATM/phase-d/"
PHASE_D_VALUE_PATHS = (
    ".tfw/conventions.md", ".tfw/templates/HL.md", ".tfw/workflows/plan.md",
    ".tfw/workflows/handoff.md", ".tfw/workflows/review.md",
    ".tfw/workflows/research/base.md", ".tfw/adapters/codex/AGENTS.md.template", "AGENTS.md",
    ".agent/workflows/tfw-plan.md", ".agent/workflows/tfw-handoff.md",
    ".agent/workflows/tfw-review.md", ".agent/workflows/tfw-research.md",
    ".claude/commands/tfw-plan.md", ".claude/commands/tfw-handoff.md",
    ".claude/commands/tfw-review.md", ".claude/commands/tfw-research.md",
)
PHASE_D_ASSURANCE_PATHS = ("docs/scripts/test_runtime_context.py", "docs/scripts/test_integration.py")
PHASE_D_WORKFLOW_COPIES = {
    ".tfw/workflows/plan.md": (".agent/workflows/tfw-plan.md", ".claude/commands/tfw-plan.md"),
    ".tfw/workflows/resume.md": (".agent/workflows/tfw-resume.md", ".claude/commands/tfw-resume.md"),
    ".tfw/workflows/handoff.md": (".agent/workflows/tfw-handoff.md", ".claude/commands/tfw-handoff.md"),
    ".tfw/workflows/review.md": (".agent/workflows/tfw-review.md", ".claude/commands/tfw-review.md"),
    ".tfw/workflows/research/base.md": (
        ".agent/workflows/tfw-research.md", ".claude/commands/tfw-research.md"),
}


def _phase_d_git_paths(prefix):
    return tuple(subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", PHASE_D_BASELINE, "--", prefix],
        cwd=PROJECT_ROOT, text=True, encoding="utf-8", capture_output=True, check=True,
    ).stdout.splitlines())


def test_phase_d_literal_value_assurance_and_trace_boundary_is_complete():
    changed = set(subprocess.run(
        ["git", "diff", "--name-only", PHASE_D_BASELINE, "--"], cwd=PROJECT_ROOT,
        text=True, encoding="utf-8", capture_output=True, check=True,
    ).stdout.splitlines())
    assert set(PHASE_D_VALUE_PATHS) <= changed
    assert set(PHASE_D_ASSURANCE_PATHS) <= changed
    allowed = set(PHASE_D_VALUE_PATHS) | set(PHASE_D_ASSURANCE_PATHS)
    assert not {path for path in changed if path not in allowed and not path.startswith(PHASE_D_PREFIX)}


def test_phase_d_workflow_copies_and_codex_managed_receiver_are_exact():
    for canonical, copies in PHASE_D_WORKFLOW_COPIES.items():
        expected = (PROJECT_ROOT / canonical).read_bytes()
        assert all((PROJECT_ROOT / path).read_bytes() == expected for path in copies)
    template = (PROJECT_ROOT / ".tfw/adapters/codex/AGENTS.md.template").read_text(encoding="utf-8")
    receiver = (PROJECT_ROOT / "AGENTS.md").read_text(encoding="utf-8")
    want, have = _managed_block(template, "CODEX"), _managed_block(receiver, "CODEX")
    assert want and have and want.group("body") == have.group("body")
    baseline = _git_bytes(PHASE_D_BASELINE, "AGENTS.md").decode("utf-8")
    old = _managed_block(baseline, "CODEX")
    assert old
    assert baseline[:old.start()] == receiver[:have.start()]
    assert baseline[old.end():] == receiver[have.end():]


def test_phase_d_claude_release_config_history_and_prior_phases_are_byte_exact():
    protected = {
        ".tfw/CHANGELOG.md", ".tfw/VERSION", ".tfw/project_config.yaml",
        ".tfw/templates/project_config.yaml", ".tfw/adapters/manifest.yaml",
        ".tfw/adapters/claude-code/CLAUDE.md.template", ".tfw/glossary.md",
        ".tfw/README.md", ".tfw/templates/RELEASE.md", "RELEASE.md", "CLAUDE.md",
    }
    protected.update(_phase_d_git_paths(".tfw/migrations"))
    protected.update(_phase_d_git_paths("knowledge"))
    protected.update(path for path in _phase_d_git_paths(
        "workspace/2026/TFW_20260902-111644_CRATM") if not path.startswith(PHASE_D_PREFIX))
    for path in sorted(protected):
        assert (PROJECT_ROOT / path).read_bytes() == _git_bytes(PHASE_D_BASELINE, path), path
    assert not (PROJECT_ROOT / "workspace/2026/TFW_20260902-111644_CRATM/phase-e").exists()


def test_phase_d_added_product_lines_do_not_leak_provider_names_or_apis():
    canonical = tuple(path for path in PHASE_D_VALUE_PATHS if path not in {
        ".tfw/adapters/codex/AGENTS.md.template", "AGENTS.md"})
    diff = subprocess.run(
        ["git", "diff", "--unified=0", PHASE_D_BASELINE, "--", *canonical],
        cwd=PROJECT_ROOT, text=True, encoding="utf-8", capture_output=True, check=True,
    ).stdout
    added = "\n".join(line[1:] for line in diff.splitlines()
                      if line.startswith("+") and not line.startswith("+++"))
    assert not re.findall(
        r"\b(?:Codex|Claude|create_thread|send_message_to_thread|wait_threads|fork_thread|spawn_agent)\b",
        added)


# CRATM Phase D revision 2: replace the historical selector/protection projection above without
# erasing it. Product movement is measured from the original baseline; history protection starts at
# the exact revised-TS approval epoch.
PHASE_D_APPROVAL_EPOCH = "b755de9128f2b0442615a4ca8b787761f937bbcd"
PHASE_D_A7_FREEZE = "2386bfb0994f6e0a1aed7b734e345cdb2a540ae1"
PHASE_D_CANDIDATE = "fac67ef443c5cb50a766cc6c6c639ea60a259437"
PHASE_D_FINAL = "18d54060da8796ddca7d648365cbfeb18f60690b"
PHASE_D_VALUE_PATHS = (
    ".tfw/conventions.md", ".tfw/templates/HL.md", ".tfw/templates/team/profile.md",
    ".tfw/templates/journal/event.md", ".tfw/workflows/plan.md",
    ".tfw/workflows/resume.md", ".tfw/workflows/handoff.md", ".tfw/workflows/review.md",
    ".tfw/workflows/research/base.md", ".tfw/adapters/codex/AGENTS.md.template", "AGENTS.md",
    ".agent/workflows/tfw-plan.md", ".agent/workflows/tfw-resume.md",
    ".agent/workflows/tfw-handoff.md",
    ".agent/workflows/tfw-review.md", ".agent/workflows/tfw-research.md",
    ".claude/commands/tfw-plan.md", ".claude/commands/tfw-resume.md",
    ".claude/commands/tfw-handoff.md",
    ".claude/commands/tfw-review.md", ".claude/commands/tfw-research.md",
)
PHASE_D_CUMULATIVE_PATHS = (
    PHASE_D_PREFIX + "ONB__phase-d__team_mode_and_role_assignment.md",
    PHASE_D_PREFIX + "RF__phase-d__team_mode_and_role_assignment.md",
    PHASE_D_PREFIX + "evidence/EV__phase-d__team_mode_and_role_assignment.md",
)
PHASE_D_REVIEW_CONTINUATION_RELS = frozenset({
    "REVIEW__phase-d__team_mode_and_role_assignment__rev3.md",
    "review/rev3/map.md", "review/rev3/verify.md", "review/rev3/judge.md",
    "REVIEW__phase-d__team_mode_and_role_assignment__rev4.md",
    "review/rev4/map.md", "review/rev4/verify.md", "review/rev4/judge.md",
})
PHASE_D_ROUND_ATTACHMENT_NAMES = frozenset({
    "phase-d-round3-a5.json", "phase-d-round3-accounting.txt",
    "phase-d-round3-mkdocs-baseline.json", "phase-d-round3-mutants.json",
    "phase-d-round3-scenarios.json", "phase-d-round3-test-output.txt",
    "phase-d-round3-wip-preservation.txt",
    "phase-d-round4-a5.json", "phase-d-round4-accounting.txt",
    "phase-d-round4-mkdocs-baseline.json", "phase-d-round4-mutants.json",
    "phase-d-round4-scenarios.json", "phase-d-round4-test-output.txt",
    "phase-d-round4-wip-preservation.txt",
})
PHASE_D_EXACT_CONTINUATION_RELS = frozenset({
    "status.md",
    "ONB__phase-d__team_mode_and_role_assignment.md",
    "RF__phase-d__team_mode_and_role_assignment.md",
    "evidence/EV__phase-d__team_mode_and_role_assignment.md",
    *PHASE_D_REVIEW_CONTINUATION_RELS,
    *(f"evidence/{name}" for name in PHASE_D_ROUND_ATTACHMENT_NAMES),
})
PHASE_D_FROZEN_INPUTS = (
    "workspace/2026/TFW_20260902-111644_CRATM/HL-TFW_20260902-111644_CRATM.md",
    PHASE_D_PREFIX + "HL__phase-d__team_mode_and_role_assignment.md",
    PHASE_D_PREFIX + "TS__phase-d__team_mode_and_role_assignment__rev2.md",
    PHASE_D_PREFIX + "TS__phase-d__team_mode_and_role_assignment__rev3.md",
    PHASE_D_PREFIX + "REVIEW__phase-d__team_mode_and_role_assignment__rev2.md",
    ".tfw/templates/bindings.yaml", "KNOWLEDGE.md",
)


def _phase_d_tree_paths(ref, prefix=""):
    return tuple(subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", ref, "--", prefix], cwd=PROJECT_ROOT,
        text=True, encoding="utf-8", capture_output=True, check=True).stdout.splitlines())


def _phase_d_changed(ref, target=None):
    command = ["git", "diff", "--name-only", ref]
    if target is not None:
        command.append(target)
    command.append("--")
    return set(subprocess.run(
        command, cwd=PROJECT_ROOT,
        text=True, encoding="utf-8", capture_output=True, check=True).stdout.splitlines())


def _phase_d_allowed_continuation(path):
    if not path.startswith(PHASE_D_PREFIX): return False
    rel = path[len(PHASE_D_PREFIX):]
    if rel in PHASE_D_EXACT_CONTINUATION_RELS: return True
    return bool(re.fullmatch(
        r"journal/\d{8}-\d{6}__(?:created|dispatch|handoff|transition|ownership_changed|"
        r"amendment_escalated)__[0-9a-f]{4}\.md", rel))


def test_phase_d_continuation_guard_is_finite_and_covers_rev3_plus_round4_sequence():
    review_ruling_tip = "61c7364fac7e377a7e3b76c09d376dcd26475c98"
    changed_at_review = set(subprocess.run(
        ["git", "diff", "--name-only", PHASE_D_APPROVAL_EPOCH, review_ruling_tip, "--"],
        cwd=PROJECT_ROOT, text=True, encoding="utf-8", capture_output=True, check=True,
    ).stdout.splitlines())
    selected = set(PHASE_D_VALUE_PATHS) | set(PHASE_D_ASSURANCE_PATHS)
    committed_trace = changed_at_review - selected
    assert committed_trace
    assert all(_phase_d_allowed_continuation(path) for path in committed_trace)

    anticipated_round4_rels = {
        "ONB__phase-d__team_mode_and_role_assignment.md",
        "RF__phase-d__team_mode_and_role_assignment.md",
        "evidence/EV__phase-d__team_mode_and_role_assignment.md",
        "status.md",
        "journal/20260906-233320__dispatch__98b7.md",
        "journal/20260906-233606__transition__cd98.md",
        "journal/20260907-000001__transition__a1b2.md",
        "REVIEW__phase-d__team_mode_and_role_assignment__rev4.md",
        "review/rev4/map.md", "review/rev4/verify.md", "review/rev4/judge.md",
        *(f"evidence/{name}" for name in PHASE_D_ROUND_ATTACHMENT_NAMES
          if name.startswith("phase-d-round4-")),
    }
    assert all(_phase_d_allowed_continuation(PHASE_D_PREFIX + rel)
               for rel in anticipated_round4_rels)
    assert PHASE_D_REVIEW_CONTINUATION_RELS == {
        "REVIEW__phase-d__team_mode_and_role_assignment__rev3.md",
        "review/rev3/map.md", "review/rev3/verify.md", "review/rev3/judge.md",
        "REVIEW__phase-d__team_mode_and_role_assignment__rev4.md",
        "review/rev4/map.md", "review/rev4/verify.md", "review/rev4/judge.md",
    }
    assert len(PHASE_D_ROUND_ATTACHMENT_NAMES) == 14

    foreign_rels = (
        "REVIEW__phase-d__team_mode_and_role_assignment__rev5.md",
        "REVIEW__phase-d__team_mode_and_role_assignment__rev30.md",
        "review/rev3/notes.md", "review/rev4/extra.md", "review/rev5/map.md",
        "evidence/phase-d-accounting.json", "evidence/phase-d-round4-extra.json",
        "evidence/phase-d-round30-a5.json", "evidence/phase-d-round4-a5.json.bak",
        "journal/random.md", "journal/20260907-000001__unknown__a1b2.md",
        "journal/20260907-000001__transition__ZZZZ.md",
        "journal/nested/20260907-000001__transition__a1b2.md", "notes.md",
    )
    assert not any(_phase_d_allowed_continuation(PHASE_D_PREFIX + rel) for rel in foreign_rels)
    assert not _phase_d_allowed_continuation(".tfw/conventions.md")
    assert not _phase_d_allowed_continuation("docs/scripts/test_integration.py")


def test_phase_d_literal_value_assurance_and_trace_boundary_is_complete():
    baseline_value = set(subprocess.run(
        ["git", "diff", "--name-only", PHASE_D_BASELINE, PHASE_D_CANDIDATE,
         "--", *PHASE_D_VALUE_PATHS],
        cwd=PROJECT_ROOT, text=True, encoding="utf-8", capture_output=True, check=True,
    ).stdout.splitlines())
    assert baseline_value == set(PHASE_D_VALUE_PATHS)
    changed = _phase_d_changed(PHASE_D_APPROVAL_EPOCH, PHASE_D_CANDIDATE)
    allowed = set(PHASE_D_VALUE_PATHS) | set(PHASE_D_ASSURANCE_PATHS)
    assert set(PHASE_D_VALUE_PATHS) <= changed
    assert set(PHASE_D_ASSURANCE_PATHS) <= changed
    assert not {path for path in changed
                if path not in allowed and not _phase_d_allowed_continuation(path)}
    assert subprocess.run(
        ["git", "merge-base", "--is-ancestor", PHASE_D_APPROVAL_EPOCH,
         PHASE_D_CANDIDATE],
        cwd=PROJECT_ROOT, capture_output=True).returncode == 0


def test_phase_d_baseline_numstat_is_numeric_for_exact_twenty_one_value_paths():
    output = subprocess.run(
        ["git", "diff", "--numstat", PHASE_D_BASELINE, PHASE_D_CANDIDATE,
         "--", *PHASE_D_VALUE_PATHS],
        cwd=PROJECT_ROOT, text=True, encoding="utf-8", capture_output=True, check=True,
    ).stdout.splitlines()
    records = [line.split("\t") for line in output if line]
    assert len(records) == 21
    assert {row[2] for row in records} == set(PHASE_D_VALUE_PATHS)
    assert all(len(row) == 3 and row[0].isdigit() and row[1].isdigit() for row in records)


def test_phase_d_workflow_copies_and_codex_managed_receiver_are_exact():
    for canonical, copies in PHASE_D_WORKFLOW_COPIES.items():
        snapshot = _git_bytes(PHASE_D_CANDIDATE, canonical)
        assert all(_git_bytes(PHASE_D_CANDIDATE, path) == snapshot for path in copies)
        expected = (PROJECT_ROOT / canonical).read_bytes()
        assert all((PROJECT_ROOT / path).read_bytes() == expected for path in copies)
    template = (PROJECT_ROOT / ".tfw/adapters/codex/AGENTS.md.template").read_text(encoding="utf-8")
    receiver = (PROJECT_ROOT / "AGENTS.md").read_text(encoding="utf-8")
    want, have = _managed_block(template, "CODEX"), _managed_block(receiver, "CODEX")
    assert want and have and want.group("body") == have.group("body")
    approved = _git_bytes(PHASE_D_APPROVAL_EPOCH, "AGENTS.md").decode("utf-8")
    candidate = _git_bytes(PHASE_D_CANDIDATE, "AGENTS.md").decode("utf-8")
    old = _managed_block(approved, "CODEX")
    candidate_block = _managed_block(candidate, "CODEX")
    assert old and candidate_block
    assert approved[:old.start()] == candidate[:candidate_block.start()]
    assert approved[old.end():] == candidate[candidate_block.end():]
    assert candidate[:candidate_block.start()] == receiver[:have.start()]
    assert candidate[candidate_block.end():] == receiver[have.end():]


def test_phase_d_approval_epoch_protects_history_inputs_and_cumulative_prefixes():
    for path in PHASE_D_FROZEN_INPUTS:
        assert _git_bytes(PHASE_D_CANDIDATE, path) == _git_bytes(
            PHASE_D_APPROVAL_EPOCH, path), path
    for path in PHASE_D_CUMULATIVE_PATHS:
        assert _git_bytes(PHASE_D_CANDIDATE, path).startswith(
            _git_bytes(PHASE_D_APPROVAL_EPOCH, path)), path
    preapproval_journal = _phase_d_tree_paths(PHASE_D_APPROVAL_EPOCH, PHASE_D_PREFIX + "journal")
    assert preapproval_journal
    for path in preapproval_journal:
        assert _git_bytes(PHASE_D_CANDIDATE, path) == _git_bytes(
            PHASE_D_APPROVAL_EPOCH, path), path
    for phase in ("phase-a", "phase-b", "phase-c"):
        for path in _phase_d_tree_paths(
                PHASE_D_APPROVAL_EPOCH,
                f"workspace/2026/TFW_20260902-111644_CRATM/{phase}"):
            assert _git_bytes(PHASE_D_CANDIDATE, path) == _git_bytes(
                PHASE_D_APPROVAL_EPOCH, path), path
    assert not _phase_d_tree_paths(
        PHASE_D_CANDIDATE, "workspace/2026/TFW_20260902-111644_CRATM/phase-e")


def test_phase_d_final_trace_is_byte_exact_in_the_integrated_tree():
    final_paths = _phase_d_tree_paths(PHASE_D_FINAL, PHASE_D_PREFIX)
    assert final_paths
    for path in final_paths:
        assert (PROJECT_ROOT / path).read_bytes() == _git_bytes(PHASE_D_FINAL, path), path


def test_phase_d_closure_visible_knowledge_uses_approval_epoch_not_product_baseline():
    def decision_row(ref, decision):
        text = _git_bytes(ref, "KNOWLEDGE.md").decode("utf-8")
        rows = [line for line in text.splitlines() if line.startswith(f"| {decision} |")]
        assert len(rows) == 1
        return rows[0]

    current = (PROJECT_ROOT / "KNOWLEDGE.md").read_text(encoding="utf-8")
    d82 = decision_row("957f7be8f5f208b87be12a8cd4d67b24af00cd1e", "D82")
    d83 = decision_row(PHASE_D_FINAL, "D83")
    assert d82 in current and d83 in current
    assert current.count("| D82 |") == 1 and current.count("| D83 |") == 1
    assert "D82 | **Agent Team declaration" not in current
    assert decision_row(PHASE_D_FINAL, "D83") != decision_row(
        PHASE_D_APPROVAL_EPOCH, "D82")


def test_phase_d_release_config_migrations_and_original_d_history_are_protected():
    prefixes = (".tfw/migrations", "knowledge")
    paths = {
        ".tfw/CHANGELOG.md", ".tfw/VERSION", ".tfw/project_config.yaml",
        ".tfw/templates/project_config.yaml", ".tfw/adapters/manifest.yaml",
        ".tfw/adapters/claude-code/CLAUDE.md.template", ".tfw/glossary.md", ".tfw/README.md",
        ".tfw/templates/RELEASE.md", "RELEASE.md", "CLAUDE.md",
    }
    for prefix in prefixes:
        paths.update(_phase_d_tree_paths(PHASE_D_APPROVAL_EPOCH, prefix))
    for path in sorted(paths):
        assert _git_bytes(PHASE_D_FINAL, path) == _git_bytes(PHASE_D_APPROVAL_EPOCH, path), path
    old_d = [path for path in _phase_d_tree_paths(PHASE_D_APPROVAL_EPOCH, PHASE_D_PREFIX)
             if not _phase_d_allowed_continuation(path)]
    for path in old_d:
        if path in PHASE_D_VALUE_PATHS or path in PHASE_D_ASSURANCE_PATHS: continue
        assert _git_bytes(PHASE_D_FINAL, path) == _git_bytes(PHASE_D_APPROVAL_EPOCH, path), path


def test_phase_d_added_product_provider_terms_are_confined_to_adapter_and_named_exception():
    neutral = tuple(path for path in PHASE_D_VALUE_PATHS if path not in {
        ".tfw/adapters/codex/AGENTS.md.template", "AGENTS.md", ".tfw/conventions.md"})
    diff = subprocess.run(
        ["git", "diff", "--unified=0", PHASE_D_BASELINE, PHASE_D_CANDIDATE,
         "--", *neutral],
        cwd=PROJECT_ROOT, text=True, encoding="utf-8", capture_output=True, check=True,
    ).stdout
    added = "\n".join(line[1:] for line in diff.splitlines()
                      if line.startswith("+") and not line.startswith("+++"))
    assert not re.findall(
        r"\b(?:Codex|Claude|create_thread|send_message_to_thread|wait_threads|fork_thread|spawn_agent)\b",
        added)
    canon = (PROJECT_ROOT / ".tfw/conventions.md").read_text(encoding="utf-8")
    assert canon.count("supplied initial Codex profile") == 1
    assert "create_thread" not in canon and "send_message_to_thread" not in canon


def test_phase_d_a7_freeze_and_historical_denominator_are_immutable_anchors():
    assert subprocess.run(
        ["git", "cat-file", "-e", f"{PHASE_D_A7_FREEZE}^{{commit}}"], cwd=PROJECT_ROOT,
        capture_output=True).returncode == 0
    ts = _git_bytes(
        PHASE_D_FINAL,
        PHASE_D_PREFIX + "TS__phase-d__team_mode_and_role_assignment__rev3.md",
    ).decode("utf-8")
    assert "Historical `16/640` remains the immutable denominator" in ts
    assert "| Logical VALUE files | `21`;" in ts
    assert "`461` additions + `471` deletions = `932`" in ts


def test_phase_d_resume_copy_parity_and_unaffected_session_consumers_are_protected():
    for canonical in (".tfw/workflows/plan.md", ".tfw/workflows/resume.md"):
        name = Path(canonical).stem
        snapshot = _git_bytes(PHASE_D_CANDIDATE, canonical)
        assert _git_bytes(PHASE_D_CANDIDATE, f".agent/workflows/tfw-{name}.md") == snapshot
        assert _git_bytes(PHASE_D_CANDIDATE, f".claude/commands/tfw-{name}.md") == snapshot
        expected = (PROJECT_ROOT / canonical).read_bytes()
        assert (PROJECT_ROOT / f".agent/workflows/tfw-{name}.md").read_bytes() == expected
        assert (PROJECT_ROOT / f".claude/commands/tfw-{name}.md").read_bytes() == expected
    protected = [".tfw/glossary.md"]
    for name in ("docs", "init"):
        protected.extend((f".tfw/workflows/{name}.md", f".agent/workflows/tfw-{name}.md",
                          f".claude/commands/tfw-{name}.md"))
    for path in protected:
        assert _git_bytes(PHASE_D_CANDIDATE, path) == _git_bytes(
            PHASE_D_APPROVAL_EPOCH, path), path
    for name, cue in (("research/base", "RESEARCH"), ("handoff", "EXEC"), ("review", "REVIEW"),
                      ("docs", "DOCS"), ("init", "INIT")):
        text = (PROJECT_ROOT / f".tfw/workflows/{name}.md").read_text(encoding="utf-8")
        assert "LEAD · {handle}" not in text and cue in text, name


# Keep the historical pytest names as stable entrypoints while applying the rev2 epoch semantics.
def test_phase_d_claude_release_config_history_and_prior_phases_are_byte_exact():
    test_phase_d_approval_epoch_protects_history_inputs_and_cumulative_prefixes()


# CRATM Phase E: integration-gate checks remain valid while the exact merge is open, at
# Candidate I, and on later trace-only descendants.  Historical Phase D assertions above stay
# pinned to their own immutable candidate/final objects instead of treating the integrated tree
# as if it were still the Phase D approval checkout.
PHASE_E_BASELINE = "957f7be8f5f208b87be12a8cd4d67b24af00cd1e"
PHASE_E_APPROVAL = "78509fdfdab05f1f7b621e7d83ae8ed48a1b52bd"
PHASE_E_FIRST_PARENT = "cafd4947791d95907d1cd81fa10e1d9bbbe56578"
PHASE_E_MAIN = "2adf89918c64643f9edfde07182508decef1fde4"
PHASE_E_RTBO = "ae494e2a9f9ee82e5d0bd2a9d79e4e23d58a1822"
PHASE_E_D_PARTICIPANTS = "3153c5d12528bc5bf859333f5d17097fc04b4d46"
PHASE_E_VALUE_PATHS = (
    ".agent/workflows/tfw-handoff.md", ".agent/workflows/tfw-plan.md",
    ".agent/workflows/tfw-research.md", ".agent/workflows/tfw-resume.md",
    ".agent/workflows/tfw-review.md", ".claude/commands/tfw-handoff.md",
    ".claude/commands/tfw-plan.md", ".claude/commands/tfw-research.md",
    ".claude/commands/tfw-resume.md", ".claude/commands/tfw-review.md",
    ".tfw/adapters/codex/AGENTS.md.template", ".tfw/conventions.md",
    ".tfw/templates/HL.md", ".tfw/templates/journal/event.md",
    ".tfw/templates/team/profile.md", ".tfw/workflows/handoff.md",
    ".tfw/workflows/plan.md", ".tfw/workflows/research/base.md",
    ".tfw/workflows/resume.md", ".tfw/workflows/review.md", "AGENTS.md",
    "KNOWLEDGE.md", "team/README.md", "team/robert.md", "team/saubakirov.md",
)
PHASE_E_ASSURANCE_PATHS = (
    "docs/scripts/test_integration.py", "docs/scripts/test_runtime_context.py",
)
PHASE_E_WORKFLOW_COPIES = {
    ".tfw/workflows/plan.md": (
        ".agent/workflows/tfw-plan.md", ".claude/commands/tfw-plan.md"),
    ".tfw/workflows/research/base.md": (
        ".agent/workflows/tfw-research.md", ".claude/commands/tfw-research.md"),
    ".tfw/workflows/handoff.md": (
        ".agent/workflows/tfw-handoff.md", ".claude/commands/tfw-handoff.md"),
    ".tfw/workflows/review.md": (
        ".agent/workflows/tfw-review.md", ".claude/commands/tfw-review.md"),
    ".tfw/workflows/resume.md": (
        ".agent/workflows/tfw-resume.md", ".claude/commands/tfw-resume.md"),
    ".tfw/workflows/init.md": (
        ".agent/workflows/tfw-init.md", ".claude/commands/tfw-init.md"),
    ".tfw/workflows/knowledge.md": (
        ".agent/workflows/tfw-knowledge.md", ".claude/commands/tfw-knowledge.md"),
    ".tfw/workflows/update.md": (
        ".agent/workflows/tfw-update.md", ".claude/commands/tfw-update.md"),
}


def _phase_e_merge_head():
    result = subprocess.run(
        ["git", "rev-parse", "-q", "--verify", "MERGE_HEAD"], cwd=PROJECT_ROOT,
        text=True, encoding="utf-8", capture_output=True,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def _phase_e_candidate():
    """Return the exact two-parent integration commit once it exists."""
    if _phase_e_merge_head():
        return None
    output = subprocess.run(
        ["git", "rev-list", "--merges", "--parents", "HEAD"], cwd=PROJECT_ROOT,
        text=True, encoding="utf-8", capture_output=True, check=True,
    ).stdout.splitlines()
    matches = []
    for line in output:
        fields = line.split()
        if len(fields) == 3 and fields[1:] == [PHASE_E_FIRST_PARENT, PHASE_E_MAIN]:
            matches.append(fields[0])
    assert len(matches) == 1
    return matches[0]


def _phase_e_diff_command(mode, paths):
    command = ["git", "diff", mode, PHASE_E_BASELINE]
    candidate = _phase_e_candidate()
    if candidate:
        command.append(candidate)
    command.extend(("--", *paths))
    return command


def test_phase_e_candidate_has_exact_lineage_or_open_merge_heads():
    merge_head = _phase_e_merge_head()
    head = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=PROJECT_ROOT, text=True, encoding="utf-8",
        capture_output=True, check=True,
    ).stdout.strip()
    if merge_head:
        assert (head, merge_head) == (PHASE_E_FIRST_PARENT, PHASE_E_MAIN)
    else:
        candidate = _phase_e_candidate()
        parents = subprocess.run(
            ["git", "show", "-s", "--format=%P", candidate], cwd=PROJECT_ROOT,
            text=True, encoding="utf-8", capture_output=True, check=True,
        ).stdout.strip().split()
        assert parents == [PHASE_E_FIRST_PARENT, PHASE_E_MAIN]

    for ancestor, descendant in (
        (PHASE_E_APPROVAL, PHASE_E_FIRST_PARENT),
        (PHASE_E_BASELINE, PHASE_E_FIRST_PARENT),
        (PHASE_E_RTBO, PHASE_E_FIRST_PARENT),
        (PHASE_D_CANDIDATE, PHASE_E_MAIN),
        (PHASE_D_FINAL, PHASE_E_MAIN),
        (PHASE_E_D_PARTICIPANTS, PHASE_E_MAIN),
    ):
        assert subprocess.run(
            ["git", "merge-base", "--is-ancestor", ancestor, descendant],
            cwd=PROJECT_ROOT, capture_output=True,
        ).returncode == 0, (ancestor, descendant)


def test_phase_e_value_accounting_is_exact_and_within_budget():
    names = subprocess.run(
        _phase_e_diff_command("--name-only", PHASE_E_VALUE_PATHS), cwd=PROJECT_ROOT,
        text=True, encoding="utf-8", capture_output=True, check=True,
    ).stdout.splitlines()
    assert len(names) == 25
    assert set(names) == set(PHASE_E_VALUE_PATHS)

    output = subprocess.run(
        _phase_e_diff_command("--numstat", PHASE_E_VALUE_PATHS), cwd=PROJECT_ROOT,
        text=True, encoding="utf-8", capture_output=True, check=True,
    ).stdout.splitlines()
    records = [line.split("\t") for line in output if line]
    assert len(records) == 25
    assert {row[2] for row in records} == set(PHASE_E_VALUE_PATHS)
    assert all(len(row) == 3 and row[0].isdigit() and row[1].isdigit() for row in records)
    assert sum(int(row[0]) + int(row[1]) for row in records) == 971
    assert 971 <= 1200


def test_phase_e_integrated_workflows_have_exact_copy_parity():
    for canonical, copies in PHASE_E_WORKFLOW_COPIES.items():
        expected = (PROJECT_ROOT / canonical).read_bytes()
        assert all((PROJECT_ROOT / copy).read_bytes() == expected for copy in copies), canonical


def test_phase_e_preserves_rtbo_phase_d_and_protected_boundaries():
    phase_d_paths = _phase_d_tree_paths(PHASE_D_FINAL, PHASE_D_PREFIX)
    assert phase_d_paths
    assert all((PROJECT_ROOT / path).read_bytes() == _git_bytes(PHASE_D_FINAL, path)
               for path in phase_d_paths)
    assert not (PROJECT_ROOT / ".tfw/scripts").exists()
    assert not (PROJECT_ROOT / "workspace/00-INDEX.md").exists()
    assert (PROJECT_ROOT / "tools/tfw_state.py").is_file()
    assert (PROJECT_ROOT / "tools/tfw_doctor.py").is_file()
    assert (PROJECT_ROOT / ".tfw/templates/project_config.yaml").read_bytes() == _git_bytes(
        PHASE_E_FIRST_PARENT, ".tfw/templates/project_config.yaml")


def test_phase_e_knowledge_keeps_exact_rtbo_and_final_cratm_decisions():
    def row(ref, decision):
        text = _git_bytes(ref, "KNOWLEDGE.md").decode("utf-8")
        rows = [line for line in text.splitlines() if line.startswith(f"| {decision} |")]
        assert len(rows) == 1
        return rows[0]

    current = (PROJECT_ROOT / "KNOWLEDGE.md").read_text(encoding="utf-8")
    assert row(PHASE_E_BASELINE, "D82") in current
    assert row(PHASE_D_FINAL, "D83") in current
    assert current.count("| D82 |") == 1 and current.count("| D83 |") == 1
    assert "D82 | **Agent Team declaration" not in current
    artifact_rows = [line for line in current.splitlines()
                     if line.startswith("| TFW_20260902-111644_CRATM/B–D |")]
    assert len(artifact_rows) == 1
    artifact_row = artifact_rows[0]
    assert "D82 preserves the initial Phase D capture" not in artifact_row
    assert "the pinned Phase D revision chain preserves the superseded initial owner AT capture" \
        in artifact_row
    assert "D83 records the final post-freeze owner AT choice" in artifact_row


def test_phase_e_selected_product_and_assurance_files_have_no_conflict_markers():
    markers = ("<<<<<<< ", "=======", ">>>>>>> ")
    for path in (*PHASE_E_VALUE_PATHS, *PHASE_E_ASSURANCE_PATHS):
        text = (PROJECT_ROOT / path).read_text(encoding="utf-8")
        assert not any(line.startswith(markers) for line in text.splitlines()), path
    test_phase_d_release_config_migrations_and_original_d_history_are_protected()


def test_phase_d_added_product_lines_do_not_leak_provider_names_or_apis():
    test_phase_d_added_product_provider_terms_are_confined_to_adapter_and_named_exception()


def test_cratm_phase_c_authority_consumers_and_six_copies_are_coherent():
    conventions = (PROJECT_ROOT / ".tfw/conventions.md").read_text(encoding="utf-8")
    assert all(clause in conventions for clause in (
        "governing task/phase `status.md.owner` must be a declared human",
        "selected LEAD's root Coordinator may rule only a genuinely",
        "A child\nnever inherits that grant", "`writer` is attribution, not an edge",
        "LEAD/root-unit-origin", "routes to the human owner"))
    required = {
        ".tfw/workflows/plan.md": ("HL Contract` rule 8", "valid terminal verdict",
                                   "selected principal/mandate separately"),
        ".tfw/workflows/review.md": ("HL Contract` rule 8", "proposal origin `{principal, unit}`"),
        ".tfw/workflows/handoff.md": ("HL Contract` rule 8", "never an Executor decision"),
        ".tfw/templates/HL.md": ("Selected LEAD mandate", "Working-unit assignment"),
        ".tfw/templates/RES.md": ("preserving origin", "resolved-ruler verdict required"),
    }
    for path, clauses in required.items():
        text = (PROJECT_ROOT / path).read_text(encoding="utf-8")
        assert all(clause in text for clause in clauses), path
    assert _cratm_live_owner_reader_errors() == []
    for command in REVISE_CONSUMERS:
        canonical = PROJECT_ROOT / ".tfw/workflows" / f"{command}.md"
        for copy in (PROJECT_ROOT / ".claude/commands" / f"tfw-{command}.md",
                     PROJECT_ROOT / ".agent/workflows" / f"tfw-{command}.md"):
            assert copy.read_bytes() == canonical.read_bytes()


def test_cratm_phase_c_owner_only_consumer_mutant_is_rejected():
    conventions = (PROJECT_ROOT / ".tfw/conventions.md").read_text(encoding="utf-8")
    assert "`writer` is attribution, not an edge" in conventions
    mutant = conventions.replace("`writer` is attribution, not an edge",
                                  "`writer` is the authority edge", 1)
    assert mutant != conventions
    assert "`writer` is attribution, not an edge" not in mutant
    handoff = (PROJECT_ROOT / ".tfw/workflows/handoff.md").read_text(encoding="utf-8")
    injected = handoff + "\nSTOP until owner verdict.\n"
    assert _revise_consumer_errors("handoff", injected) == [
        "handoff: universal route survives: STOP until owner verdict"]


def test_rtpsn_phase_b_codex_manifest_roots_phase_a_cratm_and_project_routes_are_protected():
    manifest = _adapter_manifest()
    protected = {".tfw/adapters/manifest.yaml", "AGENTS.md", "CLAUDE.md"}
    for command, row in manifest["commands"].items():
        protected.add(_expand(manifest["adapters"]["codex"]["commands"]["source"],
                              command, row["workflow"]))
        protected.add(_expand(manifest["adapters"]["codex"]["commands"]["target"], command))
    protected.update(manifest["commands"][command]["workflow"] for command in RTPSN_PROJECT_ROUTES)
    protected.update(_rtpsn_git_paths("workspace/2026/TFW_20260905-124029_RTPSN/phase-a"))
    assert len({path for path in protected if "/skills/tfw-" in path}) == 22
    rtbo_declared = {
        f".tfw/workflows/{name}.md" for name in ("plan", "knowledge", "init", "update")
    } | {
        f"{base}/tfw-{name}.md"
        for base in (".claude/commands", ".agent/workflows")
        for name in ("plan", "knowledge", "init", "update")
    }
    for path in sorted(protected):
        if path in rtbo_declared:
            continue
        if path == "AGENTS.md":
            before = _git_bytes(RTPSN_PHASE_B_BASELINE, path).decode("utf-8")
            after = (PROJECT_ROOT / path).read_text(encoding="utf-8")
            old_block, new_block = _managed_block(before, "CODEX"), _managed_block(after, "CODEX")
            assert old_block and new_block
            assert before[:old_block.start()] == after[:new_block.start()]
            assert before[old_block.end():] == after[new_block.end():]
        else:
            assert (PROJECT_ROOT / path).read_bytes() == _git_bytes(RTPSN_PHASE_B_BASELINE, path), path
    test_phase_d_approval_epoch_protects_history_inputs_and_cumulative_prefixes()
