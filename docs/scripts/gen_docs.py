"""TFW Documentation Generator — mkdocs-gen-files script.

Reads TFW project artifacts and generates virtual MkDocs pages.
Runs at build time via the mkdocs-gen-files plugin.

Contract: .tfw/conventions.md §16 (Compilable Contract)
"""

import re
from pathlib import Path

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
    source_path: str, output_path: str, root: Path, task_prefix: str
) -> None:
    """Read source file, add frontmatter, resolve references, write virtual page."""
    path = root / source_path
    content = path.read_text(encoding="utf-8")
    title = extract_title(content, source_path)
    result = add_frontmatter(content, title, source_path)
    result = resolve_references(result, project_root=root, task_prefix=task_prefix)
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
    pattern: str, output_prefix: str, root: Path, task_prefix: str
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
        copy_with_frontmatter(str(relative), output_path, root, task_prefix)


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
        for m in _re.finditer(r'\| \[?(TFW-\d+)\]?.*?\| (.+?) \|.*?\| ([^|]+) \|', readme):
            task_id = m.group(1)
            task_name = m.group(2).strip()
            status = m.group(3).strip()
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
) -> str:
    """Scan content for reference patterns, resolve to hyperlinks.

    Uses closure-based sub-resolvers with access to project_root.
    """
    if project_root is None:
        project_root = _get_project_root()
    if task_prefix is None:
        task_prefix = _read_task_prefix(project_root)

    root = project_root

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
            url = _md_to_url("/" + rel)
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
            url = _md_to_url("/" + rel)
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
            url = _md_to_url("/" + rel)
            return f"[{match.group(0)}]({url})"
        print(f"WARNING [gen_docs]: Unresolved HL reference: {match.group(0)}")
        return match.group(0)

    hl_dash_pattern = re.compile(
        r'(?<!\[)\bHL-(' + re.escape(task_prefix) + r'-\d+)\b(?!\])'
    )
    content = hl_dash_pattern.sub(_replace_hl_dash, content)

    # --- TD-{N} → TECH_DEBT.md ---
    td_pattern = re.compile(r'(?<!\[)\bTD-(\d+)\b(?!\])')
    content = td_pattern.sub(r'[TD-\1](/reference/tech-debt/)', content)

    # --- D{N} → KNOWLEDGE.md §1 anchor ---
    # Resolve everywhere except inside backticks or existing links
    d_pattern = re.compile(r'(?<!\[)(?<!`)\bD(\d+)\b(?!`}?)(?!\])')
    content = d_pattern.sub(r'[D\1](/knowledge-index/#architecture-decisions)', content)

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
                url = _md_to_url("/" + rel)
                return f"[`{path_str}`]({url})"
        else:
            # Exact path — check if it maps to an output page
            full_path = root / path_str
            if full_path.exists():
                # Map source path to output path
                for src_prefix, out_prefix in [
                    (".tfw/conventions.md", "/reference/conventions/"),
                    (".tfw/glossary.md", "/reference/glossary/"),
                    (".tfw/README.md", "/concepts/philosophy/"),
                    (".tfw/init.md", "/getting-started/"),
                    (".tfw/CHANGELOG.md", "/reference/changelog/"),
                    (".tfw/PROJECT_CONFIG.yaml", ""),  # no output page
                ]:
                    if path_str == src_prefix and out_prefix:
                        return f"[`{path_str}`]({out_prefix})"
                # Generic: if path starts with known prefixes, link to output
                if path_str.startswith("tasks/") and path_str.endswith(".md"):
                    url = _md_to_url("/" + path_str)
                    return f"[`{path_str}`]({url})"
                if path_str.startswith("knowledge/") and path_str.endswith(".md"):
                    url = _md_to_url("/" + path_str)
                    return f"[`{path_str}`]({url})"
                if path_str.startswith(".tfw/workflows/") and path_str.endswith(".md"):
                    subpath = path_str[len(".tfw/workflows/"):]
                    url = _md_to_url("/reference/workflows/" + subpath)
                    return f"[`{path_str}`]({url})"
                if path_str.startswith(".tfw/templates/") and path_str.endswith(".md"):
                    subpath = path_str[len(".tfw/templates/"):]
                    url = _md_to_url("/reference/templates/" + subpath)
                    return f"[`{path_str}`]({url})"
        # Can't resolve — leave as-is
        return match.group(0)

    # Match `path/to/file.md` or `path/with.../abbreviation...md`
    backtick_path_pattern = re.compile(
        r'`((?:tasks|knowledge|\.tfw|KNOWLEDGE|TECH_DEBT|README|RELEASE)[^`]*\.(?:md|yaml))`'
    )
    content = backtick_path_pattern.sub(_replace_backtick_path, content)

    # --- P{N} → deferred to Phase C (no-op) ---
    # P{N} has high false-positive risk; skip for now

    return content


# --- Main ---

def main():
    """Entry point for mkdocs-gen-files plugin."""
    root = _get_project_root()
    task_prefix = _read_task_prefix(root)

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
                copy_with_frontmatter(INDEX_OVERRIDE, output, root, task_prefix)
                continue
        copy_with_frontmatter(source, output, root, task_prefix)

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
        copy_glob(pattern, prefix, root, task_prefix)
        # Generate index page for the section
        title = section_titles.get(prefix, prefix.rstrip("/").replace("/", " ").title())
        if pages:
            _generate_section_index(prefix, title, pages, root=root)


# mkdocs-gen-files executes at module level during build
# Guard: only run when mkdocs_gen_files is the real package (not a test mock)
if hasattr(mkdocs_gen_files, "open"):
    main()
