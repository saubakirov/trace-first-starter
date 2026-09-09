"""Generated-output checks, sharing one fresh MkDocs build per module.

Source/Git/temp-tree contracts live in test_repository_contracts.py.
Install docs/requirements.txt and pytest for this output family.
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
    containers = tfw_state.reference_containers(PROJECT_ROOT)
    for task_dir in tfw_state.iter_task_dirs(PROJECT_ROOT, containers):
        relative = next(
            task_dir.relative_to(PROJECT_ROOT / container)
            for container in containers
            if task_dir.is_relative_to(PROJECT_ROOT / container)
        )
        landing = site / "tasks" / relative / "index.html"
        assert landing.exists(), task_dir.relative_to(PROJECT_ROOT).as_posix()
    home = (site / "index.html").read_text(encoding="utf-8")
    assert not re.search(r'<a[^>]*class="md-nav__link"[^>]*>\s*Tasks\s*</a>', home)


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
