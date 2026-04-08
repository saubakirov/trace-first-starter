"""TFW Documentation Generator — mkdocs-gen-files script.

Reads TFW project artifacts and generates virtual MkDocs pages.
Runs at build time via the mkdocs-gen-files plugin.

Contract: .tfw/compilable_contract.md (extracted from conventions.md §16)
"""

import re
from pathlib import Path, PurePosixPath

import yaml
import mkdocs_gen_files

# --- §16.1 Source Manifest ---

# Static sources: (source_path, output_path, required)
STATIC_SOURCES = [
    ("README.md", "index.md", True),
    (".tfw/README.md", "concepts/philosophy.md", True),
    (".tfw/init.md", "getting-started.md", True),
    (".tfw/conventions.md", "reference/conventions.md", True),
    (".tfw/glossary.md", "reference/glossary.md", True),
    (".tfw/CHANGELOG.md", "reference/changelog.md", True),
    ("KNOWLEDGE.md", "knowledge-index.md", False),
    ("TECH_DEBT.md", "reference/tech-debt.md", False),
    ("RELEASE.md", "reference/release.md", False),
    (".tfw/compilable_contract.md", "reference/compilable-contract.md", True),
]

# Glob sources: (glob_pattern, output_prefix, required)
GLOB_SOURCES = [
    ("knowledge/*.md", "knowledge/", False),
    ("tasks/**/*.md", "tasks/", False),
    (".tfw/workflows/**/*.md", "reference/workflows/", False),
    (".tfw/templates/**/*.md", "reference/templates/", False),
]

# Curated override
INDEX_OVERRIDE = "docs/index.md"


# --- Path Utilities ---

# Pipeline order (build time):
#   1. copy_with_frontmatter() reads source → adds frontmatter
#   2. rewrite_markdown_links() fixes relative markdown links using source→output map
#   3. add_table_anchors() injects HTML id anchors on entity table rows
#   4. resolve_references() resolves text patterns (artifact refs, D{N}, TD-{N}, bare task IDs)
#   5. _generate_nav() produces SUMMARY.md for literate-nav


def _normalize_posix_path(path: str) -> str:
    """Normalize path, resolving '..' and '.' components."""
    parts = path.replace("\\", "/").split("/")
    result: list[str] = []
    for part in parts:
        if part == "." or part == "":
            continue
        elif part == ".." and result and result[-1] != "..":
            result.pop()
        else:
            result.append(part)
    return "/".join(result) if result else "."


def _posix_relpath(target: str, base_dir: str) -> str:
    """Compute relative URL path from base_dir to target."""
    if not base_dir or base_dir == ".":
        return target
    target_parts = tuple(p for p in PurePosixPath(target).parts if p != ".")
    base_parts = tuple(p for p in PurePosixPath(base_dir).parts if p != ".")
    if not base_parts:
        return target
    common = 0
    for a, b in zip(base_parts, target_parts):
        if a != b:
            break
        common += 1
    ups = len(base_parts) - common
    downs = target_parts[common:]
    return "/".join([".."]*ups + list(downs)) or "."


def _build_path_map(root: Path) -> dict[str, str]:
    """Build source→output path mapping from Source Manifest."""
    path_map: dict[str, str] = {}
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
    source_dir = str(PurePosixPath(source_path).parent)

    def _rewrite_link(match: re.Match) -> str:
        text = match.group(1)
        target = match.group(2)
        # Skip external, anchors, absolute
        if target.startswith(("http://", "https://", "#", "/")):
            return match.group(0)
        # Neutralize template placeholder links (e.g. {PREFIX}-{N})
        if "{" in target:
            return f"`{text}`"
        # Separate anchor
        anchor = ""
        if "#" in target:
            target, anchor = target.split("#", 1)
            anchor = "#" + anchor
        # Skip non-md targets (images, yaml, etc.)
        if target and not target.endswith(".md") and not target.endswith("/"):
            return match.group(0)
        # Resolve relative to source
        if source_dir and source_dir != ".":
            resolved = _normalize_posix_path(source_dir + "/" + target)
        else:
            resolved = _normalize_posix_path(target)
        # Look up in path map
        if resolved in path_map:
            output_target = path_map[resolved]
            current_output = path_map.get(source_path, source_path)
            current_dir = str(PurePosixPath(current_output).parent)
            rel = _posix_relpath(output_target, current_dir)
            return f"[{text}]({rel}{anchor})"
        return match.group(0)

    md_link_pattern = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
    return md_link_pattern.sub(_rewrite_link, content)


def add_table_anchors(content: str) -> str:
    """Add HTML id anchors to table rows containing entity IDs (D, TD, P, F, S)."""
    patterns = [
        (re.compile(r'^\| (D\d+) \|', re.MULTILINE), lambda m: m.group(1).lower()),
        (re.compile(r'^\| (TD-\d+) \|', re.MULTILINE), lambda m: m.group(1).lower()),
        (re.compile(r'^\| (P\d+) \|', re.MULTILINE), lambda m: m.group(1).lower()),
        (re.compile(r'^\| (F\d+) \|', re.MULTILINE), lambda m: m.group(1).lower()),
        (re.compile(r'^\| (S\d+) \|', re.MULTILINE), lambda m: m.group(1).lower()),
    ]
    for pattern, id_fn in patterns:
        def _add_anchor(match: re.Match, _id_fn=id_fn) -> str:
            anchor_id = _id_fn(match)
            return f'| <span id="{anchor_id}">{match.group(1)}</span> |'
        content = pattern.sub(_add_anchor, content)
    return content


# --- Configuration ---

def _read_task_prefix(root: Path) -> str:
    """Read tfw.task_prefix from PROJECT_CONFIG.yaml."""
    config_path = root / ".tfw" / "PROJECT_CONFIG.yaml"
    if config_path.exists():
        with open(config_path, encoding="utf-8") as f:
            config = yaml.safe_load(f)
        return config.get("tfw", {}).get("task_prefix", "PROJ")
    return "PROJ"


def _get_project_root() -> Path:
    """Derive project root from script location: docs/scripts/gen_docs.py → root."""
    return Path(__file__).parent.parent.parent


# --- Transformation Functions ---

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
    return f'---\ntitle: "{title}"\nsource: "{source}"\n---\n\n{content}'


def validate_sources(root: Path) -> list[str]:
    """Check required sources exist, warn on missing optional."""
    warnings = []
    for source, _output, required in STATIC_SOURCES:
        path = root / source
        if not path.exists():
            if required:
                raise FileNotFoundError(f"Required source missing: {source}")
            warnings.append(f"Optional source missing: {source}")
    return warnings


def copy_with_frontmatter(
    source_path: str, output_path: str, root: Path, task_prefix: str,
    path_map: dict[str, str] | None = None,
) -> None:
    """Read source file, add frontmatter, rewrite links, resolve references, write virtual page."""
    path = root / source_path
    content = path.read_text(encoding="utf-8")
    title = extract_title(content, source_path)
    result = add_frontmatter(content, title, source_path)
    if path_map:
        result = rewrite_markdown_links(result, source_path, path_map)
    if output_path in ("knowledge-index.md", "reference/tech-debt.md"):
        result = add_table_anchors(result)
    result = resolve_references(result, project_root=root, task_prefix=task_prefix, output_path=output_path)
    # README-specific: rewrite HTML for MkDocs compatibility
    if source_path == "README.md":
        # Strip docs/ prefix (GitHub vs MkDocs path difference)
        result = re.sub(r'(src|href)="docs/', r'\1="', result)
        # Replace <p align="center"><img src="..." ...></p> with markdown image
        result = re.sub(
            r'<p\s+align="center">\s*<img\s+src="([^"]+)"\s+alt="([^"]*)"[^>]*>\s*</p>',
            r'![\2](\1)',
            result,
        )
    with mkdocs_gen_files.open(output_path, "w") as f:
        f.write(result)


def _glob_base(pattern: str) -> str:
    """Extract the fixed base directory from a glob pattern.

    'tasks/**/*.md' → 'tasks'
    'knowledge/*.md' → 'knowledge'
    '.tfw/workflows/**/*.md' → '.tfw/workflows'
    """
    parts = Path(pattern).parts
    base_parts = []
    for p in parts:
        if "*" in p or "?" in p:
            break
        base_parts.append(p)
    return str(Path(*base_parts)) if base_parts else "."


def copy_glob(
    pattern: str, output_prefix: str, root: Path, task_prefix: str,
    path_map: dict[str, str] | None = None,
) -> None:
    """Glob source files relative to project root, copy each with frontmatter."""
    base = _glob_base(pattern)
    base_path = Path(base)
    for path in sorted(root.glob(pattern)):
        relative = path.relative_to(root)
        # Compute output: strip the glob base, prepend output prefix
        try:
            subpath = relative.relative_to(base_path)
        except ValueError:
            subpath = relative
        # Use forward slashes for MkDocs compatibility
        output_path = output_prefix + str(subpath).replace("\\", "/")
        copy_with_frontmatter(str(relative), output_path, root, task_prefix, path_map)


def _md_to_url(md_path: str) -> str:
    """Convert a .md path to MkDocs directory URL.

    MkDocs with use_directory_urls=true serves 'foo/bar.md' as 'foo/bar/'.
    Absolute links must use the directory form, not the .md form.
    """
    if md_path.endswith(".md"):
        base = md_path[:-3]
        # Preserve anchors
        return f"{base}/"
    return md_path


def _md_to_url_with_anchor(md_path: str) -> str:
    """Like _md_to_url but handles '#anchor' after .md."""
    if "#" in md_path:
        path_part, anchor = md_path.split("#", 1)
        return f"{_md_to_url(path_part)}#{anchor}"
    return _md_to_url(md_path)


def _generate_section_index(output_prefix: str, title: str, pages: list[str], root: Path = None) -> None:
    """Generate an index.md for a glob section listing all pages."""
    if output_prefix == "tasks/" and root:
        _generate_tasks_index(pages, root)
        return
    lines = [f"# {title}\n\n"]
    for page_path in sorted(pages):
        name = Path(page_path).stem.replace("_", " ").strip()
        if not name:
            continue
        rel = page_path[len(output_prefix):] if page_path.startswith(output_prefix) else page_path
        lines.append(f"- [{name}]({rel})\n")
    content = "".join(lines)
    with mkdocs_gen_files.open(output_prefix + "index.md", "w") as f:
        f.write(content)


def _generate_tasks_index(pages: list[str], root: Path) -> None:
    """Generate a structured tasks index grouped by task folder."""
    from collections import OrderedDict
    import re as _re

    # Group pages by task folder
    groups = OrderedDict()
    for page_path in sorted(pages):
        parts = page_path.split("/")
        if len(parts) >= 2:
            task_folder = parts[1]  # e.g. TFW-18__knowledge_consolidation
        else:
            task_folder = "_other"
        groups.setdefault(task_folder, []).append(page_path)

    # Parse task board from README.md for statuses
    statuses = {}
    readme_path = root / "README.md"
    if readme_path.exists():
        readme = readme_path.read_text(encoding="utf-8")
        for m in _re.finditer(
            r'\| \[?(?:TFW-\d+)\]?(?:\([^)]*\))?\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|',
            readme,
        ):
            # Columns: ID | Task | Status | ...
            # group(1) = Task name, group(2) = Status
            task_name = m.group(1).strip()
            status = m.group(2).strip()
            # Extract task ID from the match start
            id_m = _re.search(r'TFW-\d+', m.group(0))
            if id_m:
                task_id = id_m.group(0)
                statuses[task_id] = (task_name, status)

    lines = ["# Tasks\n\n"]
    lines.append("All TFW task artifacts, grouped by task.\n\n")
    # Sort groups by numeric task ID (TFW-1, TFW-2, ... not TFW-1, TFW-10, TFW-11)
    def _task_sort_key(folder_name: str) -> int:
        m = _re.search(r'(\d+)', folder_name)
        return int(m.group(1)) if m else 999
    sorted_groups = sorted(groups.items(), key=lambda x: _task_sort_key(x[0]))

    for folder, folder_pages in sorted_groups:
        # Extract task ID from folder name (e.g. TFW-18__knowledge → TFW-18)
        m = _re.match(r'(TFW-\d+)__(.*)', folder)
        if m:
            task_id = m.group(1)
            folder_title = m.group(2).replace("_", " ").title()
            name, status = statuses.get(task_id, (folder_title, ""))
            # Find HL file for link
            hl_candidates = [p for p in folder_pages if "/HL" in p]
            if hl_candidates:
                hl_link = hl_candidates[0][len("tasks/"):]
                lines.append(f"### [{task_id}: {name}]({hl_link})\n")
            else:
                lines.append(f"### {task_id}: {name}\n")
            if status:
                lines.append(f"\n> Status: {status}\n")
        else:
            lines.append(f"### {folder}\n")

        lines.append("\n")
        # List artifacts with readable names
        for page_path in folder_pages:
            filename = Path(page_path).stem
            # Clean up artifact name
            display = filename.replace("__", " — ", 1).replace("_", " ")
            rel = page_path[len("tasks/"):]
            lines.append(f"- [{display}]({rel})\n")
        lines.append("\n")

    content = "".join(lines)
    with mkdocs_gen_files.open("tasks/index.md", "w") as f:
        f.write(content)


# --- §16.2 Reference Resolver ---

def resolve_references(
    content: str,
    project_root: Path = None,
    task_prefix: str = None,
    output_path: str = None,
) -> str:
    """Scan content for reference patterns, resolve to hyperlinks.

    Uses closure-based sub-resolvers with access to project_root.
    When output_path is provided, generates relative links (strict-mode safe).
    """
    if project_root is None:
        project_root = _get_project_root()
    if task_prefix is None:
        task_prefix = _read_task_prefix(project_root)

    root = project_root
    output_dir = str(PurePosixPath(output_path).parent) if output_path else None

    def _make_url(source_rel_path: str) -> str:
        """Convert a source-relative .md path to a URL (relative if output_path set)."""
        url = _md_to_url("/" + source_rel_path)
        if output_dir is None:
            return url
        # Strip leading / and trailing / for relpath computation
        target = source_rel_path
        if target.endswith(".md"):
            target = target[:-3]
        target_with_ext = target + ".md"
        return _posix_relpath(target_with_ext, output_dir)

    # --- Artifact refs: {TYPE} {PREFIX}-{N} ---
    def _replace_artifact(match: re.Match) -> str:
        artifact_type = match.group(1)
        task_id = match.group(2)
        # Glob for matching file
        candidates = sorted(root.glob(f"tasks/{task_id}*/{artifact_type}__*.md"))
        if not candidates and artifact_type == "HL":
            # HL naming convention: HL-{PREFIX}-{N}__title.md
            candidates = sorted(root.glob(f"tasks/{task_id}*/HL-{task_id}*.md"))
        if candidates:
            rel = str(candidates[0].relative_to(root)).replace("\\", "/")
            url = _make_url(rel)
            return f"[{match.group(0)}]({url})"
        print(f"WARNING [gen_docs]: Unresolved reference: {match.group(0)}")
        return match.group(0)

    artifact_pattern = re.compile(
        r'(?<!\[)\b(HL|TS|RF|ONB|RES|REVIEW)[- ]('
        + re.escape(task_prefix)
        + r'-\d+)\b(?!\])'
    )
    content = artifact_pattern.sub(_replace_artifact, content)

    # --- Phase refs: {TYPE} {PREFIX}-{N}/{PHASE} ---
    def _replace_phase(match: re.Match) -> str:
        artifact_type = match.group(1)
        task_id = match.group(2)
        phase = match.group(3)
        # Search in PhaseX subfolder first
        candidates = sorted(
            root.glob(f"tasks/{task_id}*/Phase{phase}/{artifact_type}__Phase{phase}*.md")
        )
        if not candidates:
            # Fallback: task root
            candidates = sorted(root.glob(f"tasks/{task_id}*/{artifact_type}__*.md"))
        if candidates:
            rel = str(candidates[0].relative_to(root)).replace("\\", "/")
            url = _make_url(rel)
            return f"[{match.group(0)}]({url})"
        print(f"WARNING [gen_docs]: Unresolved phase reference: {match.group(0)}")
        return match.group(0)

    phase_pattern = re.compile(
        r'(?<!\[)\b(HL|TS|RF|ONB|RES|REVIEW)[- ]('
        + re.escape(task_prefix)
        + r'-\d+)/([A-Z])\b(?!\])'
    )
    content = phase_pattern.sub(_replace_phase, content)

    # --- HL-{PREFIX}-{N} (dash-prefixed HL refs) ---
    def _replace_hl_dash(match: re.Match) -> str:
        task_id = match.group(1)
        candidates = sorted(root.glob(f"tasks/{task_id}*/HL-{task_id}*.md"))
        if candidates:
            rel = str(candidates[0].relative_to(root)).replace("\\", "/")
            url = _make_url(rel)
            return f"[{match.group(0)}]({url})"
        print(f"WARNING [gen_docs]: Unresolved HL reference: {match.group(0)}")
        return match.group(0)

    hl_dash_pattern = re.compile(
        r'(?<!\[)\bHL-(' + re.escape(task_prefix) + r'-\d+)\b(?!\])'
    )
    content = hl_dash_pattern.sub(_replace_hl_dash, content)

    # --- TD-{N} → TECH_DEBT.md ---
    def _replace_td(match: re.Match) -> str:
        n = match.group(1)
        url = _posix_relpath("reference/tech-debt.md", output_dir) if output_dir else "/reference/tech-debt/"
        return f"[TD-{n}]({url})"

    td_pattern = re.compile(r'(?<!\[)\bTD-(\d+)\b(?!\])')
    content = td_pattern.sub(_replace_td, content)

    # --- D{N} → KNOWLEDGE.md §1 anchor ---
    def _replace_d(match: re.Match) -> str:
        n = match.group(1)
        if output_dir:
            base = _posix_relpath("knowledge-index.md", output_dir)
            return f"[D{n}]({base}#architecture-decisions)"
        return f"[D{n}](/knowledge-index/#architecture-decisions)"

    d_pattern = re.compile(r'(?<!\[)(?<!`)\bD(\d+)\b(?!`}?)(?!\])')
    content = d_pattern.sub(_replace_d, content)

    # --- Backtick-path resolver: `tasks/TFW-N.../...md` → clickable links ---
    def _replace_backtick_path(match: re.Match) -> str:
        path_str = match.group(1)
        # Try to find the file via glob (handles ... abbreviations)
        if "..." in path_str:
            # Convert abbreviated path to glob: tasks/TFW-2.../RF__TFW-2...md → tasks/TFW-2*/RF__TFW-2*.md
            glob_pattern = path_str.replace("...", "*")
            candidates = sorted(root.glob(glob_pattern))
            if candidates:
                rel = str(candidates[0].relative_to(root)).replace("\\", "/")
                url = _make_url(rel)
                return f"[`{path_str}`]({url})"
        else:
            # Exact path — check if it maps to an output page
            full_path = root / path_str
            if full_path.exists():
                # Map source path to output path via static lookup
                static_map = {
                    ".tfw/conventions.md": "reference/conventions.md",
                    ".tfw/glossary.md": "reference/glossary.md",
                    ".tfw/README.md": "concepts/philosophy.md",
                    ".tfw/init.md": "getting-started.md",
                    ".tfw/CHANGELOG.md": "reference/changelog.md",
                }
                if path_str in static_map:
                    url = _make_url(static_map[path_str])
                    return f"[`{path_str}`]({url})"
                if path_str == ".tfw/PROJECT_CONFIG.yaml":
                    return match.group(0)  # no output page
                # Generic: if path starts with known prefixes, link to output
                if path_str.startswith("tasks/") and path_str.endswith(".md"):
                    url = _make_url(path_str)
                    return f"[`{path_str}`]({url})"
                if path_str.startswith("knowledge/") and path_str.endswith(".md"):
                    url = _make_url(path_str)
                    return f"[`{path_str}`]({url})"
                if path_str.startswith(".tfw/workflows/") and path_str.endswith(".md"):
                    subpath = path_str[len(".tfw/workflows/"):]
                    url = _make_url("reference/workflows/" + subpath)
                    return f"[`{path_str}`]({url})"
                if path_str.startswith(".tfw/templates/") and path_str.endswith(".md"):
                    subpath = path_str[len(".tfw/templates/"):]
                    url = _make_url("reference/templates/" + subpath)
                    return f"[`{path_str}`]({url})"
        # Can't resolve — leave as-is
        return match.group(0)

    # Match `path/to/file.md` or `path/with.../abbreviation...md`
    backtick_path_pattern = re.compile(
        r'`((?:tasks|knowledge|\.tfw|KNOWLEDGE|TECH_DEBT|README|RELEASE)[^`]*\.(?:md|yaml))`'
    )
    content = backtick_path_pattern.sub(_replace_backtick_path, content)

    # --- Bare task ID: {PREFIX}-{N} → task HL link ---
    def _replace_bare_task(match: re.Match) -> str:
        task_id = match.group(1)
        candidates = sorted(root.glob(f"tasks/{task_id}__*/"))
        if not candidates:
            return match.group(0)
        folder = candidates[0]
        hl_candidates = sorted(folder.glob(f"HL-{task_id}*.md")) + sorted(
            folder.glob(f"HL__{task_id}*.md")
        )
        if hl_candidates:
            rel = str(hl_candidates[0].relative_to(root)).replace("\\", "/")
            url = _make_url(rel)
            return f"[{match.group(0)}]({url})"
        rel = str(folder.relative_to(root)).replace("\\", "/")
        fallback = _posix_relpath(rel, output_dir) if output_dir else f"/{rel}/"
        if not fallback.endswith("/"):
            fallback += "/"
        return f"[{match.group(0)}]({fallback})"

    bare_task_pattern = re.compile(
        r'(?<!\[)(?<!\w)\b(' + re.escape(task_prefix) + r'-\d+)\b(?!\])(?!__)(?!/)'
    )
    content = bare_task_pattern.sub(_replace_bare_task, content)

    return content


# --- Navigation Generation ---


def _generate_nav(root: Path) -> None:
    """Generate SUMMARY.md for mkdocs-literate-nav."""
    nav = mkdocs_gen_files.Nav()
    # Static sections
    nav["Home"] = "index.md"
    nav["Getting Started"] = "getting-started.md"
    nav["Concepts", "Philosophy"] = "concepts/philosophy.md"
    # Knowledge (conditional on source existence)
    if (root / "KNOWLEDGE.md").exists():
        nav["Knowledge", "Architecture & Decisions"] = "knowledge-index.md"
    for path in sorted(root.glob("knowledge/*.md")):
        name = path.stem.replace("_", " ").title()
        nav["Knowledge", "Topics", name] = f"knowledge/{path.name}"
    # Reference
    nav["Reference", "Conventions"] = "reference/conventions.md"
    nav["Reference", "Glossary"] = "reference/glossary.md"
    if (root / "TECH_DEBT.md").exists():
        nav["Reference", "Tech Debt"] = "reference/tech-debt.md"
    nav["Reference", "Changelog"] = "reference/changelog.md"
    if (root / "RELEASE.md").exists():
        nav["Reference", "Release"] = "reference/release.md"
    # Dynamic: workflows
    for path in sorted(root.glob(".tfw/workflows/**/*.md")):
        subpath = path.relative_to(root / ".tfw" / "workflows")
        name = subpath.stem.replace("_", " ").title()
        sub_str = str(subpath).replace("\\", "/")
        parent_parts = list(subpath.parent.parts) if str(subpath.parent) != "." else []
        nav_key = ("Reference", "Workflows") + tuple(
            p.replace("_", " ").title() for p in parent_parts
        ) + (name,)
        nav[nav_key] = f"reference/workflows/{sub_str}"
    # Dynamic: templates
    for path in sorted(root.glob(".tfw/templates/**/*.md")):
        subpath = path.relative_to(root / ".tfw" / "templates")
        name = subpath.stem.replace("_", " ").title()
        sub_str = str(subpath).replace("\\", "/")
        parent_parts = list(subpath.parent.parts) if str(subpath.parent) != "." else []
        nav_key = ("Reference", "Templates") + tuple(
            p.replace("_", " ").title() for p in parent_parts
        ) + (name,)
        nav[nav_key] = f"reference/templates/{sub_str}"
    # Tasks
    nav["Tasks"] = "tasks/index.md"
    with mkdocs_gen_files.open("SUMMARY.md", "w") as f:
        f.writelines(nav.build_literate_nav())


# --- Main ---

def main():
    """Entry point for mkdocs-gen-files plugin."""
    root = _get_project_root()
    task_prefix = _read_task_prefix(root)
    path_map = _build_path_map(root)

    warnings = validate_sources(root)
    for w in warnings:
        print(f"WARNING [gen_docs]: {w}")

    # 1. Static sources
    for source, output, _required in STATIC_SOURCES:
        path = root / source
        if not path.exists():
            continue  # already warned in validate_sources
        # Handle index override
        if output == "index.md":
            override = root / INDEX_OVERRIDE
            if override.exists():
                copy_with_frontmatter(INDEX_OVERRIDE, output, root, task_prefix, path_map)
                continue
        copy_with_frontmatter(source, output, root, task_prefix, path_map)

    # 2. Glob sources + section index pages
    section_titles = {
        "knowledge/": "Knowledge Topics",
        "tasks/": "Tasks",
        "reference/workflows/": "Workflows",
        "reference/templates/": "Templates",
    }
    for pattern, prefix, _required in GLOB_SOURCES:
        # Collect pages generated by this glob
        base = _glob_base(pattern)
        base_path = Path(base)
        pages = []
        for path in sorted(root.glob(pattern)):
            relative = path.relative_to(root)
            try:
                subpath = relative.relative_to(base_path)
            except ValueError:
                subpath = relative
            output_path = prefix + str(subpath).replace("\\", "/")
            pages.append(output_path)
        copy_glob(pattern, prefix, root, task_prefix, path_map)
        # Generate index page for the section
        title = section_titles.get(prefix, prefix.rstrip("/").replace("/", " ").title())
        if pages:
            _generate_section_index(prefix, title, pages, root=root)

    # 3. Generate navigation (literate-nav SUMMARY.md)
    _generate_nav(root)


# mkdocs-gen-files executes at module level during build
# Guard: only run when mkdocs_gen_files is the real package (not a test mock)
if hasattr(mkdocs_gen_files, "open"):
    main()
