# TS — TFW-27 / Phase B: Link Resolution & Dynamic Navigation

> **Date**: 2026-04-08
> **Author**: Coordinator
> **Status**: 🟡 TS_DRAFT — Awaiting approval
> **Parent HL**: [HL__PhaseB__link_resolution.md](HL__PhaseB__link_resolution.md)

---

## 1. Objective

Add 4 features to gen_docs.py (~120 LOC): bare task ID resolver, markdown link rewriter, HTML table anchors, and literate-nav SUMMARY.md generation. Update mkdocs.yml and requirements.txt. Result: `mkdocs build --strict` passes clean, all cross-references resolve, navigation is auto-generated.

## 2. Scope

### In Scope
- gen_docs.py: 4 new features (§4 Steps 1-4)
- docs/requirements.txt: add `mkdocs-literate-nav`, `mkdocs-section-index`
- docs/mkdocs.yml: remove hardcoded `nav:`, add literate-nav plugin
- Existing unit/integration tests: update for new features

### Out of Scope
- P{N} auto-resolution (rejected in RES — double semantics)
- Plain text file path resolution without backticks (rejected in RES — false positive risk)
- Landing page redesign (Phase C)
- docs/index.md content (Phase C)
- site_url / repo_url (TFW-28)

## 3. Affected Files

| File | Action | Description |
|------|--------|-------------|
| `docs/scripts/gen_docs.py` | MODIFY | Add 4 features: bare task ID resolver, link rewriter, HTML anchors, literate-nav SUMMARY.md |
| `docs/mkdocs.yml` | MODIFY | Remove `nav:` block (lines 43-63), add `literate-nav` plugin |
| `docs/requirements.txt` | MODIFY | Add `mkdocs-literate-nav>=0.6` and `mkdocs-section-index>=0.3` |

**Budget:** 0 new files, 3 modifications. ~120 LOC added. Limits: max 14 files, max 1200 LOC.

## 4. Detailed Steps

### Step 1: Bare Task ID Resolver (~15 LOC)

Add to `resolve_references()` in gen_docs.py, **after** all existing resolvers (artifact, phase, HL-dash):

```python
# --- Bare task ID: {PREFIX}-{N} → task HL link ---
def _replace_bare_task(match: re.Match) -> str:
    task_id = match.group(1)
    # Find task folder
    candidates = sorted(root.glob(f"tasks/{task_id}__*/"))
    if not candidates:
        return match.group(0)
    folder = candidates[0]
    # Find HL file
    hl_candidates = sorted(folder.glob(f"HL-{task_id}*.md")) + sorted(folder.glob(f"HL__{task_id}*.md"))
    if hl_candidates:
        rel = str(hl_candidates[0].relative_to(root)).replace("\\", "/")
        url = _md_to_url("/" + rel)
        return f"[{match.group(0)}]({url})"
    # Fallback: link to task folder index
    rel = str(folder.relative_to(root)).replace("\\", "/")
    return f"[{match.group(0)}](/{rel}/)"

bare_task_pattern = re.compile(
    r'(?<!\[)(?<!\w)\b(' + re.escape(task_prefix) + r'-\d+)\b(?!\])(?!__)'
)
content = bare_task_pattern.sub(_replace_bare_task, content)
```

**Key constraints:**
- Runs LAST among resolvers (after artifact refs already consumed `HL TFW-18`, `TS TFW-18`)
- `(?<!\w)` prevents matching inside `TFW-18__knowledge` folder names
- `(?!__)` prevents matching `TFW-18__` prefixes in filenames

### Step 2: Markdown Link Rewriter (~50 LOC)

Add a new function `rewrite_markdown_links()` called from `copy_with_frontmatter()`:

```python
def _build_path_map(root: Path) -> dict[str, str]:
    """Build source→output path mapping from Source Manifest."""
    path_map = {}
    for source, output, _ in STATIC_SOURCES:
        path_map[source] = output
    for pattern, prefix, _ in GLOB_SOURCES:
        base = _glob_base(pattern)
        base_path = Path(base)
        for path in sorted(root.glob(pattern)):
            relative = path.relative_to(root)
            try:
                subpath = relative.relative_to(base_path)
            except ValueError:
                subpath = relative
            output_path = prefix + str(subpath).replace("\\", "/")
            path_map[str(relative).replace("\\", "/")] = output_path
    return path_map

def rewrite_markdown_links(
    content: str, source_path: str, path_map: dict[str, str]
) -> str:
    """Rewrite [text](relative.md) links using source→output path map."""
    source_dir = str(Path(source_path).parent).replace("\\", "/")

    def _rewrite_link(match: re.Match) -> str:
        text = match.group(1)
        target = match.group(2)
        # Skip external, anchors, absolute
        if target.startswith(("http://", "https://", "#", "/")):
            return match.group(0)
        # Separate anchor
        anchor = ""
        if "#" in target:
            target, anchor = target.split("#", 1)
            anchor = "#" + anchor
        # Resolve relative to source
        if source_dir and source_dir != ".":
            resolved = str(Path(source_dir) / target).replace("\\", "/")
        else:
            resolved = target
        # Normalize (remove ./ and resolve ..)
        resolved = str(Path(resolved)).replace("\\", "/")
        # Look up in path map
        if resolved in path_map:
            output_target = path_map[resolved]
            # Compute output dir for current file
            current_output = path_map.get(source_path, source_path)
            current_dir = str(Path(current_output).parent).replace("\\", "/")
            # Relative path from current output to target output
            try:
                rel = os.path.relpath(output_target, current_dir).replace("\\", "/")
            except ValueError:
                rel = output_target
            return f"[{text}]({rel}{anchor})"
        return match.group(0)

    md_link_pattern = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
    return md_link_pattern.sub(_rewrite_link, content)
```

**Called in `copy_with_frontmatter()`** after `add_frontmatter()` and before `resolve_references()`:
```python
result = rewrite_markdown_links(result, source_path, path_map)
result = resolve_references(result, ...)
```

Note: `import os` needed at top of file.

### Step 3: HTML Anchors on Table Rows (~30 LOC)

Add a new function `add_table_anchors()`:

```python
def add_table_anchors(content: str) -> str:
    """Add HTML id anchors to table rows containing entity IDs."""
    patterns = [
        (re.compile(r'^\| (D\d+) \|', re.MULTILINE), lambda m: m.group(1).lower()),
        (re.compile(r'^\| (TD-\d+) \|', re.MULTILINE), lambda m: m.group(1).lower()),
        (re.compile(r'^\| (P\d+) \|', re.MULTILINE), lambda m: m.group(1).lower()),
        (re.compile(r'^\| (F\d+) \|', re.MULTILINE), lambda m: m.group(1).lower()),
        (re.compile(r'^\| (S\d+) \|', re.MULTILINE), lambda m: m.group(1).lower()),
    ]
    for pattern, id_fn in patterns:
        def _add_anchor(match, _id_fn=id_fn):
            anchor_id = _id_fn(match)
            return f'| <span id="{anchor_id}">{match.group(1)}</span> |'
        content = pattern.sub(_add_anchor, content)
    return content
```

**Applied to:** KNOWLEDGE.md and TECH_DEBT.md only (pages with entity tables).

**Called in `copy_with_frontmatter()`** for specific output paths:
```python
if output_path in ("knowledge-index.md", "reference/tech-debt.md"):
    result = add_table_anchors(result)
```

### Step 4: literate-nav SUMMARY.md (~25 LOC)

Add SUMMARY.md generation to `main()`:

```python
def _generate_nav(root: Path) -> None:
    """Generate SUMMARY.md for mkdocs-literate-nav."""
    nav = mkdocs_gen_files.Nav()
    # Static sections
    nav["Home"] = "index.md"
    nav["Getting Started"] = "getting-started.md"
    nav["Concepts", "Philosophy"] = "concepts/philosophy.md"
    # Knowledge
    nav["Knowledge", "Architecture & Decisions"] = "knowledge-index.md"
    for path in sorted(root.glob("knowledge/*.md")):
        name = path.stem.replace("_", " ").title()
        nav["Knowledge", "Topics", name] = f"knowledge/{path.name}"
    # Reference
    nav["Reference", "Conventions"] = "reference/conventions.md"
    nav["Reference", "Glossary"] = "reference/glossary.md"
    nav["Reference", "Tech Debt"] = "reference/tech-debt.md"
    nav["Reference", "Changelog"] = "reference/changelog.md"
    nav["Reference", "Release"] = "reference/release.md"
    # Dynamic: workflows
    for path in sorted(root.glob(".tfw/workflows/**/*.md")):
        subpath = path.relative_to(root / ".tfw/workflows")
        name = subpath.stem.replace("_", " ").title()
        nav["Reference", "Workflows", name] = f"reference/workflows/{subpath}"
    # Dynamic: templates
    for path in sorted(root.glob(".tfw/templates/**/*.md")):
        subpath = path.relative_to(root / ".tfw/templates")
        name = subpath.stem.replace("_", " ").title()
        nav["Reference", "Templates", name] = f"reference/templates/{subpath}"
    # Tasks
    nav["Tasks"] = "tasks/index.md"
    with mkdocs_gen_files.open("SUMMARY.md", "w") as f:
        f.writelines(nav.build_literate_nav())
```

### Step 5: Update mkdocs.yml

Remove the entire `nav:` block (lines 43-63). Add plugins:

```yaml
plugins:
  - search
  - gen-files:
      scripts:
        - scripts/gen_docs.py
  - literate-nav:
      nav_file: SUMMARY.md
  - section-index
```

### Step 6: Update requirements.txt

Add:
```
mkdocs-literate-nav>=0.6
mkdocs-section-index>=0.3
```

### Step 7: Verify

1. `pip install -r docs/requirements.txt`
2. `python -m mkdocs build -f docs/mkdocs.yml --strict`
3. Verify: 0 warnings, 0 errors
4. Spot-check: navigation matches current structure, links resolve, anchors work

## 5. Acceptance Criteria

- [ ] `mkdocs build --strict` passes clean (0 warnings)
- [ ] Bare `TFW-18` in text → clickable link
- [ ] `.tfw/README.md` link `[conventions.md](conventions.md)` → resolves to `/reference/conventions/`
- [ ] README.md link `[.tfw/README.md](.tfw/README.md)` → resolves to `/concepts/philosophy/`
- [ ] `/knowledge-index/#d1` deep link works
- [ ] `/reference/tech-debt/#td-72` deep link works
- [ ] Navigation auto-generated, no `nav:` in mkdocs.yml
- [ ] Adding hypothetical `knowledge/new_topic.md` would appear in nav without config changes
- [ ] Existing 6 resolvers still work (no regression)

## 6. Risks

| Risk | Mitigation |
|------|------------|
| Link rewriter breaks existing resolved links | Run rewriter BEFORE reference solver. Reference solver overwrites any conflicts |
| literate-nav section order unexpected | Static sections defined first in code, matching current mkdocs.yml order |
| `<span id="...">` breaks table rendering | Test with pymdownx extensions. Fallback: use `{: #id}` attr_list syntax |
| `os.path.relpath` platform differences (Windows vs Unix) | Use `PurePosixPath` for URL computation, not `os.path` |

---

*TS — TFW-27 / Phase B: Link Resolution & Dynamic Navigation | 2026-04-08*
