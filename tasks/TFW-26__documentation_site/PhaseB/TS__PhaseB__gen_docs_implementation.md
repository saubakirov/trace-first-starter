# TS — TFW-26 / Phase B: gen_docs.py Implementation

> **Date**: 2026-04-05
> **Author**: Coordinator
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL-TFW-26](../HL-TFW-26__documentation_site.md)

---

## 1. Objective

Implement all `# TODO: Phase B` functions in `docs/scripts/gen_docs.py`. After this phase, `mkdocs serve --config-file docs/mkdocs.yml` produces a fully navigable local site with all sources compiled, references resolved, and frontmatter injected.

## 2. Scope

### In Scope
- Implement gen_docs.py: all transformation functions, glob processing, reference resolver
- Read `tfw.task_prefix` from PROJECT_CONFIG.yaml (replace hardcoded `TFW`)
- Verify build locally with `mkdocs build --config-file docs/mkdocs.yml --strict`
- Verify reference resolution on real project artifacts (spot-check 5+ resolved links)
- Fix P{N} false positive issue (context-aware resolution)

### Out of Scope
- Curated landing page (Phase C)
- GitHub Pages deployment verification (Phase C)
- MCP server implementation (future task)
- Migration of existing KNOWLEDGE.md/knowledge/ to reference format (TD-66, TD-67 — tfw-docs scope)

## 3. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `docs/scripts/gen_docs.py` | MODIFY | Implement all TODO functions (~100 new LOC) |
| `docs/scripts/test_gen_docs.py` | CREATE | Unit tests: extract_title, add_frontmatter, resolve_references, validate_sources |
| `docs/scripts/test_integration.py` | CREATE | Integration test: build from real project, verify output pages and links |
| `docs/requirements.txt` | MODIFY | Add pytest, pyyaml |

**Budget:** 2 new files, 2 modifications = 4 total. Defaults: max 14 files, max 8 new, max 1200 LOC.

## 4. Detailed Steps

### Step 1: Implement core utilities

```python
def extract_title(content: str, filename: str) -> str:
    """Derive title from first '# ' heading, fallback to filename stem."""
    for line in content.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return Path(filename).stem.replace("_", " ").title()


def add_frontmatter(content: str, title: str, source: str) -> str:
    """Prepend YAML frontmatter (§16.3). Skip if content already has frontmatter."""
    if content.startswith("---"):
        return content
    return f"---\ntitle: \"{title}\"\nsource: \"{source}\"\n---\n\n{content}"
```

### Step 2: Implement source validation

```python
def validate_sources() -> list[str]:
    """Check required sources exist, warn on missing optional."""
    warnings = []
    root = Path(__file__).parent.parent.parent  # project root
    for source, output, required in STATIC_SOURCES:
        path = root / source
        if not path.exists():
            if required:
                raise FileNotFoundError(f"Required source missing: {source}")
            warnings.append(f"Optional source missing: {source}")
    return warnings
```

### Step 3: Implement static source processing

```python
def copy_with_frontmatter(source_path: str, output_path: str) -> None:
    """Read source file, add frontmatter, write as virtual MkDocs page."""
    root = Path(__file__).parent.parent.parent
    path = root / source_path
    content = path.read_text(encoding="utf-8")
    title = extract_title(content, source_path)
    result = add_frontmatter(content, title, source_path)
    result = resolve_references(result)
    with mkdocs_gen_files.open(output_path, "w") as f:
        f.write(result)
```

Handle INDEX_OVERRIDE: if `docs/index.md` exists, use it instead of README.md for `index.md` output.

### Step 4: Implement glob source processing

```python
def copy_glob(pattern: str, output_prefix: str) -> None:
    """Glob source files relative to project root, copy each with frontmatter."""
    root = Path(__file__).parent.parent.parent
    for path in sorted(root.glob(pattern)):
        relative = path.relative_to(root)
        # Compute output path: strip the source prefix, prepend output prefix
        output_path = output_prefix + str(relative.relative_to(
            Path(pattern).parent if not "**" in pattern
            else _glob_base(pattern)
        ))
        copy_with_frontmatter(str(relative), output_path)
```

Key considerations:
- `tasks/**/*.md` → output preserves relative path: `tasks/TFW-18__foo/RF__TFW-18.md` → same path
- `knowledge/*.md` → `knowledge/{name}.md`
- `.tfw/workflows/**/*.md` → `reference/workflows/{subpath}`
- `.tfw/templates/**/*.md` → `reference/templates/{subpath}`

### Step 5: Implement reference resolver

The resolver scans page content for reference patterns (§16.2) and replaces with markdown hyperlinks.

```python
def resolve_references(content: str) -> str:
    """Replace reference patterns with markdown hyperlinks."""
    content = _resolve_artifact_refs(content)   # RF TFW-18, HL-TFW-19
    content = _resolve_phase_refs(content)       # RF TFW-18/A
    content = _resolve_techdebt_refs(content)    # TD-59
    content = _resolve_decision_refs(content)    # D24
    # P{N} — skip for now due to false positive risk. Revisit in Phase C
    return content
```

**Artifact reference resolution (`RF TFW-18`):**

```python
def _resolve_artifact_refs(content: str) -> str:
    """Resolve '{TYPE} {PREFIX}-{N}' patterns to hyperlinks."""
    root = Path(__file__).parent.parent.parent
    pattern = re.compile(
        r'(?<!\[)\b(HL|TS|RF|ONB|RES|REVIEW)[- ](' + TASK_PREFIX + r'-\d+)\b(?!\])'
    )

    def replacer(match):
        artifact_type = match.group(1)
        task_id = match.group(2)
        # Glob for matching file
        candidates = sorted(root.glob(f"tasks/{task_id}*/{artifact_type}__*.md"))
        if not candidates:
            # Try HL naming convention: HL-{PREFIX}-{N}
            candidates = sorted(root.glob(f"tasks/{task_id}*/HL-{task_id}*.md"))
        if candidates:
            rel = candidates[0].relative_to(root)
            return f"[{match.group(0)}]({rel})"
        print(f"WARNING [gen_docs]: Unresolved reference: {match.group(0)}")
        return f"⚠️ {match.group(0)} *(unresolved)*"

    return pattern.sub(replacer, content)
```

**Key constraint:** the regex must NOT match references already inside markdown links — negative lookbehind `(?<!\[)` and negative lookahead `(?!\])` prevent `[RF TFW-18](...)` from being double-wrapped.

**Decision/TD reference resolution:**

```python
def _resolve_decision_refs(content: str) -> str:
    """Resolve 'D{N}' to KNOWLEDGE.md anchors. Only inside tables."""
    # Only resolve D{N} when it appears in a table row (starts with |)
    pattern = re.compile(r'(?<=\| )\bD(\d+)\b')
    return pattern.sub(r'[D\1](knowledge-index.md#architecture-decisions)', content)

def _resolve_techdebt_refs(content: str) -> str:
    """Resolve 'TD-{N}' to TECH_DEBT.md anchors."""
    pattern = re.compile(r'\bTD-(\d+)\b')
    return pattern.sub(r'[TD-\1](reference/tech-debt.md)', content)
```

**P{N} — deferred** to Phase C due to false positive risk. Needs heuristic tuning.

### Step 6: Implement main()

```python
def main():
    """Entry point for mkdocs-gen-files plugin."""
    warnings = validate_sources()
    for w in warnings:
        print(f"WARNING [gen_docs]: {w}")

    root = Path(__file__).parent.parent.parent

    # 1. Static sources
    for source, output, required in STATIC_SOURCES:
        path = root / source
        if not path.exists():
            continue  # already warned in validate_sources
        # Handle index override
        if output == "index.md":
            override = root / INDEX_OVERRIDE
            if override.exists():
                copy_with_frontmatter(INDEX_OVERRIDE, output)
                continue
        copy_with_frontmatter(source, output)

    # 2. Glob sources
    for pattern, prefix, required in GLOB_SOURCES:
        copy_glob(pattern, prefix)
```

### Step 7: Read task_prefix from config

```python
import yaml

def _read_task_prefix() -> str:
    """Read tfw.task_prefix from PROJECT_CONFIG.yaml."""
    root = Path(__file__).parent.parent.parent
    config_path = root / ".tfw" / "PROJECT_CONFIG.yaml"
    if config_path.exists():
        with open(config_path) as f:
            config = yaml.safe_load(f)
        return config.get("tfw", {}).get("task_prefix", "PROJ")
    return "PROJ"
```

Add `pyyaml` to `docs/requirements.txt`.

### Step 8: Write tests

#### Unit tests (`docs/scripts/test_gen_docs.py`)

```python
import pytest
from gen_docs import extract_title, add_frontmatter, resolve_references


class TestExtractTitle:
    def test_heading_found(self):
        assert extract_title("# My Title\nContent", "file.md") == "My Title"

    def test_no_heading_fallback_to_filename(self):
        assert extract_title("No heading here", "my_file.md") == "My File"

    def test_heading_with_prefix(self):
        assert extract_title("# RF — TFW-26 / Phase A", "rf.md") == "RF — TFW-26 / Phase A"


class TestAddFrontmatter:
    def test_adds_frontmatter(self):
        result = add_frontmatter("# Title\nBody", "Title", "src.md")
        assert result.startswith("---")
        assert 'title: "Title"' in result
        assert 'source: "src.md"' in result

    def test_skips_existing_frontmatter(self):
        content = "---\ntitle: Existing\n---\nBody"
        assert add_frontmatter(content, "New", "src.md") == content


class TestResolveReferences:
    def test_artifact_ref_resolved(self, tmp_path):
        """RF TFW-18 → hyperlink when file exists."""
        # Create mock task structure
        task_dir = tmp_path / "tasks" / "TFW-18__knowledge"
        task_dir.mkdir(parents=True)
        (task_dir / "RF__TFW-18__knowledge.md").write_text("# RF")
        # Test resolution with project_root override
        content = "Source: RF TFW-18 §6"
        result = resolve_references(content, project_root=tmp_path)
        assert "[RF TFW-18]" in result
        assert "RF__TFW-18" in result

    def test_unresolved_ref_marked(self, tmp_path):
        """Unresolvable ref gets ⚠️ marker."""
        content = "Source: RF TFW-999"
        result = resolve_references(content, project_root=tmp_path)
        assert "⚠️" in result
        assert "unresolved" in result

    def test_existing_link_not_doubled(self, tmp_path):
        """[RF TFW-18](path) should NOT be re-wrapped."""
        content = "[RF TFW-18](tasks/TFW-18/RF.md)"
        result = resolve_references(content, project_root=tmp_path)
        assert content == result  # unchanged

    def test_td_ref_resolved(self):
        content = "| TD-59 | source |"
        result = resolve_references(content, project_root=None)  # no glob needed
        assert "[TD-59]" in result
        assert "tech-debt" in result

    def test_decision_ref_in_table(self):
        content = "| D24 | decision |"
        result = resolve_references(content, project_root=None)
        assert "[D24]" in result
        assert "knowledge-index" in result
```

#### Integration test (`docs/scripts/test_integration.py`)

```python
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent


def test_mkdocs_build_succeeds():
    """Full MkDocs build exits 0 on this project."""
    result = subprocess.run(
        [sys.executable, "-m", "mkdocs", "build",
         "--config-file", str(PROJECT_ROOT / "docs" / "mkdocs.yml"),
         "--strict"],
        capture_output=True, text=True, cwd=str(PROJECT_ROOT)
    )
    assert result.returncode == 0, f"Build failed:\n{result.stderr}"


def test_static_pages_generated():
    """Key static pages exist in site/ output."""
    site = PROJECT_ROOT / "site"
    assert (site / "index.html").exists(), "index.html missing"
    assert (site / "getting-started" / "index.html").exists()
    assert (site / "concepts" / "philosophy" / "index.html").exists()
    assert (site / "reference" / "conventions" / "index.html").exists()
    assert (site / "reference" / "glossary" / "index.html").exists()
    assert (site / "reference" / "changelog" / "index.html").exists()


def test_task_pages_generated():
    """Task artifacts are accessible."""
    site = PROJECT_ROOT / "site"
    # At least one task folder should have pages
    task_pages = list((site / "tasks").rglob("index.html")) if (site / "tasks").exists() else []
    assert len(task_pages) > 10, f"Expected 10+ task pages, got {len(task_pages)}"


def test_knowledge_pages_generated():
    """Knowledge topic files are compiled."""
    site = PROJECT_ROOT / "site"
    knowledge_dir = site / "knowledge"
    assert knowledge_dir.exists(), "knowledge/ section missing"
    topic_pages = list(knowledge_dir.glob("*/index.html"))
    assert len(topic_pages) >= 3, f"Expected 3+ topics, got {len(topic_pages)}"


def test_no_unresolved_markers_in_output():
    """No ⚠️ unresolved markers in key pages."""
    site = PROJECT_ROOT / "site"
    # Check a few key pages for unresolved markers
    key_pages = [
        site / "knowledge-index" / "index.html",
        site / "reference" / "tech-debt" / "index.html",
    ]
    for page in key_pages:
        if page.exists():
            content = page.read_text(encoding="utf-8")
            # Allow some unresolved in tech-debt (old format)
            # but knowledge-index should be clean
            if "knowledge-index" in str(page):
                assert "⚠️" not in content, f"Unresolved ref in {page}"
```

> **Note:** `resolve_references()` needs a `project_root` parameter for testability (default: `Path(__file__).parent.parent.parent`). This is a minor signature change from the Phase A skeleton.

### Step 9: Run tests and verify locally

```bash
cd d:/projects/research/steps-framework
pip install -r docs/requirements.txt
pytest docs/scripts/test_gen_docs.py -v
mkdocs build --config-file docs/mkdocs.yml --strict
pytest docs/scripts/test_integration.py -v
mkdocs serve --config-file docs/mkdocs.yml
```

Spot-check in browser:
1. `/` — README.md with Task Board, links to tasks/ work
2. `/tasks/TFW-26__documentation_site/PhaseA/RF__PhaseA__compilable_contract/` — RF accessible
3. `/knowledge-index` — KNOWLEDGE.md, scroll to §1 Architecture Decisions
4. `/reference/conventions` — conventions.md including §16
5. `/reference/changelog` — 366 lines of CHANGELOG

Verify reference resolution:
- Open `/reference/tech-debt` — check that Source column `TFW-26/A RF obs.` references are resolved (or left as text if format doesn't match pattern)
- Open a knowledge/ topic file — check Source column references

## 5. Acceptance Criteria

- [ ] `mkdocs build --config-file docs/mkdocs.yml` exits 0 with no ERROR-level messages
- [ ] All 9 static sources produce pages with YAML frontmatter
- [ ] All 4 glob patterns produce pages (tasks/, knowledge/, workflows/, templates/)
- [ ] Task Board links in `index.md` navigate to task pages
- [ ] Reference resolver handles `RF TFW-18`, `HL-TFW-19`, `TD-{N}` patterns
- [ ] References already inside markdown links are NOT double-wrapped
- [ ] Missing optional sources produce WARNING (page not generated, nav entry skipped)
- [ ] Unresolvable references are marked with `⚠️` in output (never silent)
- [ ] `mkdocs build --strict` fails if any references are unresolvable
- [ ] `tfw.task_prefix` read from PROJECT_CONFIG.yaml (not hardcoded)
- [ ] `docs/requirements.txt` includes pytest, pyyaml
- [ ] Unit tests pass: `pytest docs/scripts/test_gen_docs.py` (8+ tests)
- [ ] Integration tests pass: `pytest docs/scripts/test_integration.py` (5+ tests)
- [ ] `resolve_references()` accepts `project_root` parameter for testability

## 6. Phase Risks

| Risk | Mitigation |
|------|------------|
| mkdocs-gen-files API differs from expected (open/write pattern) | Executor tests against installed version. Docs: https://github.com/oprypin/mkdocs-gen-files |
| Glob `tasks/**/*.md` picks up non-artifact files (e.g., research/ stage files) | These ARE valid artifacts per §16.1. Include them all |
| Reference resolver slows build on 130+ task files | Regex is O(n) per file. Expected total: <1s for all files |
| P{N} false positives | Deferred to Phase C. Only TD-{N}, D{N}, artifact refs resolved in Phase B |
| Index override conflicts with gen-files | If docs/index.md exists AND gen_docs writes index.md, gen-files last-write-wins. Logic: skip README.md for index when override exists |

---

*TS — TFW-26 / Phase B: gen_docs.py Implementation | 2026-04-05*
