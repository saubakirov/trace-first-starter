"""Generated-output checks, sharing one fresh MkDocs build per module.

Source/Git/temp-tree contracts live in test_repository_contracts.py.
Install docs/requirements.txt and pytest for this output family.
"""

import re
import os
import subprocess
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
SITE_DIR = Path(os.environ.get("TFW_ASSURANCE_SITE_DIR", str(PROJECT_ROOT / "site")))


@pytest.fixture(scope="module", autouse=True)
def build_site():
    """Run mkdocs build once before all integration tests."""
    env = os.environ.copy()
    env["DISABLE_MKDOCS_2_WARNING"] = "true"
    from datetime import datetime, timezone
    started = datetime.now(timezone.utc).isoformat()
    result = subprocess.run(
        [
            sys.executable, "-m", "mkdocs", "build",
            "--config-file", "docs/mkdocs.yml",
            "--site-dir", str(SITE_DIR),
        ],
        capture_output=True, text=True, cwd=str(PROJECT_ROOT),
        env=env,
    )
    # Optional upstream evidence sink; not part of installed receiver behavior.
    if capture := env.get("TFW_ASSURANCE_BUILD_CAPTURE"):
        import hashlib, json
        destination = Path(capture); destination.mkdir(parents=True, exist_ok=False)
        for name, value in (("stdout.txt", result.stdout), ("stderr.txt", result.stderr)):
            (destination / name).write_text(value, encoding="utf-8")
        receipt = {"argv": result.args, "started": started,
                   "finished": datetime.now(timezone.utc).isoformat(), "exit_code": result.returncode,
                   "cwd": str(PROJECT_ROOT),
                   "streams": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in destination.glob("*.txt")}}
        (destination / "receipt.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    if result.returncode != 0:
        pytest.fail(f"MkDocs build failed:\n{result.stderr}\n{result.stdout}")
    yield


def test_static_pages_generated():
    """Key static pages exist in site/ output."""
    site = SITE_DIR
    assert (site / "index.html").exists(), "index.html missing"
    assert (site / "getting-started" / "index.html").exists(), "getting-started missing"
    assert (site / "concepts" / "philosophy" / "index.html").exists(), "philosophy missing"
    assert (site / "reference" / "conventions" / "index.html").exists(), "conventions missing"
    assert (site / "reference" / "glossary" / "index.html").exists(), "glossary missing"
    assert (site / "reference" / "changelog" / "index.html").exists(), "changelog missing"


def test_knowledge_index_generated():
    """KNOWLEDGE.md compiled to knowledge-index page."""
    site = SITE_DIR
    page = site / "knowledge-index" / "index.html"
    assert page.exists(), "knowledge-index page missing"
    content = page.read_text(encoding="utf-8")
    assert "Architecture" in content or "architecture" in content


def test_task_pages_generated():
    """Task artifacts are accessible."""
    site = SITE_DIR
    tasks_dir = site / "tasks"
    if not tasks_dir.exists():
        pytest.skip("No tasks/ in site output")
    task_pages = list(tasks_dir.rglob("index.html"))
    assert len(task_pages) > 10, f"Expected 10+ task pages, got {len(task_pages)}"


def test_knowledge_topic_pages_generated():
    """Knowledge topic files are compiled."""
    site = SITE_DIR
    knowledge_dir = site / "knowledge"
    assert knowledge_dir.exists(), "knowledge/ section missing"
    topic_pages = list(knowledge_dir.glob("*/index.html"))
    assert len(topic_pages) >= 3, f"Expected 3+ topics, got {len(topic_pages)}"


def test_workflow_pages_generated():
    """Workflow reference pages exist."""
    site = SITE_DIR
    wf_dir = site / "reference" / "workflows"
    assert wf_dir.exists(), "reference/workflows/ missing"
    wf_pages = list(wf_dir.rglob("index.html"))
    assert len(wf_pages) >= 5, f"Expected 5+ workflow pages, got {len(wf_pages)}"


def test_template_pages_generated():
    """Template reference pages exist."""
    site = SITE_DIR
    tpl_dir = site / "reference" / "templates"
    assert tpl_dir.exists(), "reference/templates/ missing"
    tpl_pages = list(tpl_dir.rglob("index.html"))
    assert len(tpl_pages) >= 5, f"Expected 5+ template pages, got {len(tpl_pages)}"


def test_frontmatter_in_generated_pages():
    """Generated pages have YAML frontmatter (title/source)."""
    site = SITE_DIR
    # Check knowledge-index page title in HTML
    page = site / "knowledge-index" / "index.html"
    if page.exists():
        content = page.read_text(encoding="utf-8")
        # MkDocs Material puts the title in <title> tag
        assert "<title>" in content


def test_decision_refs_resolved_in_knowledge_index():
    """D{N} references in knowledge-index resolve to #architecture-decisions anchors."""
    site = SITE_DIR
    page = site / "knowledge-index" / "index.html"
    if not page.exists():
        pytest.skip("knowledge-index page not built")
    content = page.read_text(encoding="utf-8")
    # D{N} refs should be resolved to anchor links (relative URL format)
    assert "#architecture-decisions" in content, \
           "D{N} references not resolved in knowledge-index"


def test_artifact_refs_resolved_in_knowledge_topics():
    """Knowledge topic files contain resolved links to task artifacts."""
    site = SITE_DIR
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
    site = SITE_DIR
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
    site = SITE_DIR
    leaked = re.compile(r"<hr />\s*<p>title: ")
    offenders = [p for p in site.rglob("index.html") if leaked.search(p.read_text(encoding="utf-8"))]
    assert not offenders, (
        f"{len(offenders)} of {len(list(site.rglob('index.html')))} pages render their frontmatter "
        "as body text, e.g. " + ", ".join(str(p.relative_to(site)) for p in offenders[:3])
    )


def test_index_override_used():
    """When docs/index.md exists, it should be used instead of README.md."""
    site = SITE_DIR
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
    site = SITE_DIR
    knowledge = site / "knowledge" / "index.html"
    assert knowledge.exists()
    assert "<a" in knowledge.read_text(encoding="utf-8")
    assert not (site / "tasks" / "index.html").exists()
    landing = site / "tasks" / "2026" / "TFW_20260902-222456_RTBO" / "index.html"
    assert landing.exists() and "Task trace" in landing.read_text(encoding="utf-8")


def test_every_recognized_task_has_an_unlisted_landing_and_nav_has_no_tasks_entry():
    sys.path.insert(0, str(PROJECT_ROOT / "tools"))
    import tfw_state
    site = SITE_DIR
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
    site = SITE_DIR
    knowledge_dir = site / "knowledge"
    if not knowledge_dir.exists():
        pytest.skip("knowledge/ not built")
    for page in knowledge_dir.rglob("index.html"):
        content = page.read_text(encoding="utf-8")
        # Check that links to /tasks/ don't end with .md
        import re
        md_links = re.findall(r'href="/tasks/[^"]*\.md"', content)
        assert not md_links, f"Found .md links in {page}: {md_links[:3]}"


def test_current_slc_parent_hl_routes_are_real_single_destinations():
    """Explicit links, control-source paths and the plain ONB citation reach the real HL."""
    from html.parser import HTMLParser
    from urllib.parse import unquote, urlsplit

    class Anchors(HTMLParser):
        def __init__(self):
            super().__init__(); self.links = []; self.current = None
        def handle_starttag(self, tag, attrs):
            if tag == 'a':
                self.current = [dict(attrs).get('href', ''), '']
        def handle_data(self, data):
            if self.current is not None:
                self.current[1] += data
        def handle_endtag(self, tag):
            if tag == 'a' and self.current is not None:
                self.links.append(self.current); self.current = None

    task_id = 'TFW_20260907-020729_SLC'
    folder = SITE_DIR / 'tasks/2026' / task_id
    target = folder / f'HL-{task_id}/index.html'
    assert target.is_file()
    expected = [(folder / f'{kind}__{task_id}/index.html', label) for kind, label in
                [('RF', 'Frozen SLC HL'), ('TS', 'Frozen SLC HL'),
                 ('REVIEW', 'HL '), ('ONB', f'HL {task_id}')]]
    expected.append((folder / 'status/index.html', f'HL-{task_id}'))
    expected.extend((page, f'HL-{task_id}') for page in (folder / 'journal').glob('*/index.html')
                    if f'>HL-{task_id}</a>' in page.read_text(encoding='utf-8'))
    assert len(expected) > 5, 'No current control-event HL route exercised'
    for page, label in expected:
        parsed = Anchors(); parsed.feed(page.read_text(encoding='utf-8'))
        links = [href for href, text in parsed.links if label in text and f'HL-{task_id}' in href]
        assert links, (page, label)
        for href in links:
            assert not any(char in href for char in '[]()'), (page, href)
            url = urlsplit(href)
            actual = (page.parent / unquote(url.path) / 'index.html').resolve()
            assert actual == target.resolve() and actual.is_file(), (page, href)
            if url.fragment:
                assert f'id="{unquote(url.fragment)}"' in actual.read_text(encoding='utf-8')



def test_tkl_five_mixed_navigation_families_reach_exact_generated_destinations():
    from html.parser import HTMLParser
    from urllib.parse import unquote, urlsplit
    class Links(HTMLParser):
        def __init__(self):
            super().__init__(); self.links = []; self.current = None
        def handle_starttag(self, tag, attrs):
            if tag == "a":
                assert self.current is None, "nested anchor"
                self.current = [dict(attrs).get("href", ""), ""]
        def handle_data(self, value):
            if self.current is not None: self.current[1] += value
        def handle_endtag(self, tag):
            if tag == "a" and self.current is not None:
                self.links.append(self.current); self.current = None
    site = SITE_DIR
    record = site / "knowledge/records/TKL-20260913-01/index.html"
    entry = site / "knowledge-index/index.html"
    topic = site / "knowledge/process/index.html"
    task = "tasks/2026/TFW_20260909-231654_TKL"
    cases = [
        (record, "KNOWLEDGE.md D37", entry, "d37"),
        (entry, "Process", topic, ""),
        (entry, "TKL-20260913-01", record, ""),
        (record, "D82", entry, "d82"),
        (record, "owner decision", site / task / "journal/20260913-141400__handoff__8c2a/index.html", ""),
        (record, "HL decision context", site / task / "HL-TFW_20260909-231654_TKL/index.html", ""),
        (topic, "RES TFW-22", site / "tasks/TFW-22__coordinator_research_enrichment/RES__TFW-22__coordinator_research_enrichment/index.html", ""),
    ]
    for page, label, target, fragment in cases:
        assert page.is_file() and target.is_file(), (page, target)
        parsed = Links(); parsed.feed(page.read_text(encoding="utf-8"))
        matches = [href for href, text in parsed.links if label in text]
        assert matches, (page, label)
        resolved = []
        for href in matches:
            url = urlsplit(href)
            if url.scheme or url.netloc: continue
            destination = (page.parent / unquote(url.path) / "index.html").resolve()
            resolved.append((destination, unquote(url.fragment)))
        assert (target.resolve(), fragment) in resolved, (page, label, resolved)
        if fragment: assert f'id="{fragment}"' in target.read_text(encoding="utf-8")


def test_tkl_five_reviewed_fragment_occurrences_reach_existing_exact_ids():
    from html.parser import HTMLParser
    from urllib.parse import unquote, urlsplit

    class Page(HTMLParser):
        def __init__(self, path):
            super().__init__()
            self.hrefs = []
            self.ids = []
            self.feed(path.read_text(encoding="utf-8"))

        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            if "id" in attrs:
                self.ids.append(attrs["id"])
            if tag == "a" and "href" in attrs:
                self.hrefs.append(attrs["href"])

    site = SITE_DIR
    tkl = site / "tasks/2026/TFW_20260909-231654_TKL"
    slc = site / "tasks/2026/TFW_20260907-020729_SLC"
    hl = tkl / "HL-TFW_20260909-231654_TKL/index.html"
    onb = tkl / "ONB__TFW_20260909-231654_TKL/index.html"
    rf = slc / "RF__TFW_20260907-020729_SLC/index.html"
    review = slc / "REVIEW__TFW_20260907-020729_SLC/index.html"
    cases = [
        (hl, site / "reference/workflows/knowledge/index.html", "canonical-knowledge-gate-algorithm"),
        (hl, rf, "11-correction-round-c2--exact-link-preservation"),
        (hl, review, "c2-bounded-acceptance--2026-09-10"),
        (onb, rf, "11-correction-round-c2--exact-link-preservation"),
        (onb, review, "independent-c2-return-and-closure-boundary--2026-09-10"),
    ]
    for source, target, fragment in cases:
        matching = [urlsplit(href) for href in Page(source).hrefs
                    if unquote(urlsplit(href).fragment) == fragment]
        assert matching, (source, fragment)
        assert any((source.parent / unquote(url.path) / "index.html").resolve() == target.resolve()
                   for url in matching if not url.scheme and not url.netloc), (source, fragment)
        assert Page(target).ids.count(fragment) == 1, (target, fragment)
    historical = (site / "reference/workflows/knowledge/index.html").read_text(encoding="utf-8")
    assert "Retired historical destination" in historical
    assert "ec91c56007c20cda79f740fec15c85e4af74d17c" in historical
