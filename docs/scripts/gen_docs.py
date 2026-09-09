"""TFW Documentation Generator — mkdocs-gen-files script.

Reads TFW project artifacts and generates virtual MkDocs pages.
Runs at build time via the mkdocs-gen-files plugin.

Contract: .tfw/compilable_contract.md (extracted from conventions.md §16)
"""

import re
import sys
from pathlib import Path, PurePosixPath

import yaml
import mkdocs_gen_files

def _find_root(start: Path) -> Path:
    """The project root, by walking upward for `.tfw/`.

    This is `tfw_state.find_project_root` restated, and it has to be: the import below
    needs the root to locate the upstream state module in the first place. Ten lines duplicated is the
    price of a bootstrap that cannot import its way out.

    Not depth arithmetic. mkdocs runs this file through the `gen-files` plugin with `docs/`
    as the config root, so the cwd is not the project root and cannot be assumed.
    """
    for candidate in (start, *start.parents):
        if ".upstream" in candidate.parts:
            continue
        if (candidate / ".tfw").is_dir():
            return candidate
    raise SystemExit(f"no project root above {start}: no directory contains .tfw/")


_ROOT = _find_root(Path(__file__).resolve().parent)

# Documentation is an upstream product concern, so it may use the upstream-only semantic
# reader under root tools/. Full receivers do not receive or require either directory.
sys.path.insert(0, str(_ROOT / "tools"))

import tfw_state  # noqa: E402  — upstream semantic task resolver

# --- §16.1 Source Manifest ---

# Static sources: (source_path, output_path, required)
STATIC_SOURCES = [
    ("README.md", "index.md", True),
    (".tfw/README.md", "concepts/philosophy.md", True),
    (".tfw/quickstart.md", "getting-started.md", True),
    (".tfw/conventions.md", "reference/conventions.md", True),
    (".tfw/glossary.md", "reference/glossary.md", True),
    (".tfw/CHANGELOG.md", "reference/changelog.md", True),
    ("KNOWLEDGE.md", "knowledge-index.md", False),
    ("RELEASE.md", "reference/release.md", False),
    (".tfw/compilable_contract.md", "reference/compilable-contract.md", True),
]

# Glob sources: (glob_pattern, output_prefix, required)
# Active and historical containers both compile; ordinary task discovery stays active-only.
BASE_GLOB_SOURCES = [
    ("knowledge/*.md", "knowledge/", False),
    (".tfw/workflows/**/*.md", "reference/workflows/", False),
    (".tfw/templates/**/*.md", "reference/templates/", False),
]


def _glob_sources(root: Path) -> list[tuple[str, str, bool]]:
    """Source globs for this project, with the task containers read from configuration."""
    sources = [(f"{container}/**/*.md", "tasks/", False)
               for container in tfw_state.reference_containers(root)]
    return sources + BASE_GLOB_SOURCES


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
    tfw_state.iter_task_dirs(root, tfw_state.reference_containers(root))  # refuse ID collisions before output
    path_map: dict[str, str] = {}
    for source, output, _ in STATIC_SOURCES:
        path_map[source] = output
    for pattern, prefix, _ in _glob_sources(root):
        base = _glob_base(pattern)
        base_path = Path(base)
        for path in sorted(root.glob(pattern)):
            relative = path.relative_to(root)
            try:
                subpath = relative.relative_to(base_path)
            except ValueError:
                subpath = relative
            output_path = _glob_output_path(relative, base_path, prefix)
            path_map[relative.as_posix()] = output_path
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
    """Read tfw.task_prefix from project_config.yaml."""
    config_path = root / ".tfw" / "project_config.yaml"
    if config_path.exists():
        with open(config_path, encoding="utf-8") as f:
            config = yaml.safe_load(f)
        return config.get("tfw", {}).get("task_prefix", "PROJ")
    return "PROJ"


def _get_project_root() -> Path:
    """The project root, found by marker rather than by counting directories up."""
    return _ROOT


# --- Transformation Functions ---

def extract_title(content: str, filename: str) -> str:
    """Derive title from first '# ' heading, fallback to filename stem."""
    for line in content.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return Path(filename).stem.replace("_", " ").title()


def add_frontmatter(content: str, title: str, source: str) -> str:
    """Prepend YAML frontmatter (§16.3). Skip if content already has frontmatter.

    The block is serialized, never interpolated. Building it with an f-string put YAML's quoting
    rules in the caller's head: a title holding a double quote — 247 artifacts in this corpus do —
    closed the scalar early, and the whole block then rendered as body text instead of parsing.
    `yaml.safe_dump` knows the rules, so nothing here has to.
    """
    if content.startswith("---"):
        return content
    header = yaml.safe_dump(
        {"title": title, "source": source},
        allow_unicode=True, default_flow_style=False, sort_keys=False,
    )
    return f"---\n{header}---\n\n{content}"


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
    """Read source file, transform the body, then prepend frontmatter and write the virtual page.

    **Frontmatter goes on last, and that ordering is load-bearing.** Every transform below rewrites
    text by pattern, and each one used to run over the header too: `resolve_references` turned the
    bare task id inside `title: TFW-55 Iteration 2 …` into a markdown link, which rendered as HTML
    and left the block unparseable. Adding the header after the body is transformed makes that class
    of defect unrepresentable, for these four transforms and for any added later — which is why the
    fix is an ordering, not a guard on each of them.
    """
    path = root / source_path
    content = path.read_text(encoding="utf-8")
    title = extract_title(content, source_path)
    result = content
    if path_map:
        result = rewrite_markdown_links(result, source_path, path_map)
    if output_path in ("knowledge-index.md", "tasks/DEBT-SNAPSHOT.md"):
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
    result = add_frontmatter(result, title, source_path)
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


def _glob_output_path(relative: Path, base_path: Path, output_prefix: str) -> str:
    """Map a globbed source without letting container metadata become ``tasks/index``."""
    try:
        subpath = relative.relative_to(base_path)
    except ValueError:
        subpath = relative
    if output_prefix == "tasks/":
        parts = subpath.parts
        task_part = parts[1] if len(parts) > 1 and re.fullmatch(r"\d{4}", parts[0]) else parts[0]
        if tfw_state.parse_identifier(task_part) is None:
            subpath = Path("_container") / base_path.name / subpath
    return output_prefix + subpath.as_posix()


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
        output_path = _glob_output_path(relative, base_path, output_prefix)
        copy_with_frontmatter(relative.as_posix(), output_path, root, task_prefix, path_map)


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


def _generate_section_index(output_prefix: str, title: str, pages: list[str]) -> None:
    """Generate an index.md for a glob section listing all pages."""
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


def _task_output_dir(root: Path, task_dir: Path) -> str:
    """Map one configured task directory to its hidden documentation output directory."""
    for container in tfw_state.reference_containers(root):
        base = (root / container).resolve()
        try:
            relative = task_dir.resolve().relative_to(base).as_posix()
        except ValueError:
            continue
        return f"tasks/{relative}"
    raise ValueError(f"task is outside configured containers: {task_dir}")


def _generate_task_landings(root: Path, path_map: dict[str, str]) -> None:
    """Generate one unlisted link landing for every recognized task, including no-HL tasks."""
    declared = tfw_state.declared_lifecycles(root)
    for task_dir in tfw_state.iter_task_dirs(root, tfw_state.reference_containers(root)):
        identifier = tfw_state.parse_identifier(task_dir.name)[1]
        output_dir = _task_output_dir(root, task_dir)
        status = tfw_state.read_status(task_dir, declared)
        title = identifier
        if status and not status.get("_error") and status.get("title"):
            title = str(status["title"])
        task_prefix = task_dir.relative_to(root).as_posix() + "/"
        compiled = sorted(
            output
            for source, output in path_map.items()
            if source.startswith(task_prefix) and source.endswith(".md")
        )
        lines = [f"# {title}", "", f"Task trace `{identifier}`.", ""]
        for page in compiled:
            label = Path(page).stem.replace("__", " — ", 1).replace("_", " ")
            lines.append(f"- [{label}]({_posix_relpath(page, output_dir)})")
        if not compiled:
            lines.append("No Markdown artifacts are present in this recognized task directory.")
        lines.append("")
        with mkdocs_gen_files.open(f"{output_dir}/index.md", "w") as f:
            f.write("\n".join(lines))


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
    reference_paths = tfw_state.reference_containers(root)
    task_universe = None  # one observed universe per page; no persistent cache or stale later call
    output_dir = str(PurePosixPath(output_path).parent) if output_path else None
    prefix = re.escape(task_prefix)
    task_id_source = (
        rf"(?:{prefix}_\d{{8}}-\d{{6}}_[A-Z0-9]+|"
        rf"\d{{8}}-\d{{6}}__[A-Za-z0-9][A-Za-z0-9_-]*|"
        rf"{prefix}-\d+)"
    )

    def _make_url(source_rel_path: str) -> str:
        """Convert a source-relative .md path to a URL (relative if output_path set)."""
        for container in reference_paths:
            if Path(source_rel_path).is_relative_to(Path(container)):
                source_rel_path = _glob_output_path(Path(source_rel_path), Path(container), "tasks/")
                break
        url = _md_to_url("/" + source_rel_path)
        if output_dir is None:
            return url
        # Strip leading / and trailing / for relpath computation
        target = source_rel_path
        if target.endswith(".md"):
            target = target[:-3]
        target_with_ext = target + ".md"
        return _posix_relpath(target_with_ext, output_dir)

    def _task_glob(task_id: str, tail: str) -> list[Path]:
        """Whole-ID lookup in the reference union; the existing walker refuses collisions."""
        nonlocal task_universe
        if task_universe is None:
            task_universe = tfw_state.iter_task_dirs(root, reference_paths)
        task_dirs = [path for path in task_universe
            if tfw_state.parse_identifier(path.name)[1] == task_id]

        found: list[Path] = []
        for task_dir in sorted(task_dirs, key=str):
            if tail:
                found.extend(sorted(task_dir.glob(tail)))
            else:
                found.append(task_dir)
        # Deterministic and duplicate-free: the same reference must resolve the same way
        # on every machine, whatever order the filesystem offered.
        seen, unique = set(), []
        for path in found:
            key = path.resolve()
            if key not in seen:
                seen.add(key)
                unique.append(path)
        return unique

    # --- Artifact refs: {TYPE} {ID}; ID is one of the three named grammars ---
    def _replace_artifact(match: re.Match) -> str:
        artifact_type = match.group(1)
        task_id = match.group(2)
        # Glob for matching file
        candidates = _task_glob(task_id, f"{artifact_type}__*.md")
        if not candidates and artifact_type == "HL":
            # HL naming convention: HL-{ID}__title.md
            candidates = _task_glob(task_id, f"HL-{task_id}*.md")
        if candidates:
            rel = candidates[0].relative_to(root).as_posix()
            url = _make_url(rel)
            return f"[{match.group(0)}]({url})"
        print(f"WARNING [gen_docs]: Unresolved reference: {match.group(0)}")
        return match.group(0)

    artifact_pattern = re.compile(
        r'(?<!\[)(?<![A-Za-z0-9_])(HL|TS|RF|ONB|RES|REVIEW)[- ]('
        + task_id_source
        + r')(?![A-Za-z0-9_/\]])'
    )
    content = artifact_pattern.sub(_replace_artifact, content)

    # --- Phase refs: {TYPE} {ID}/{PHASE} ---
    def _replace_phase(match: re.Match) -> str:
        artifact_type = match.group(1)
        task_id = match.group(2)
        phase = match.group(3)
        # Search in PhaseX subfolder first
        candidates = (_task_glob(task_id, f"phase-{phase.lower()}/{artifact_type}__phase-{phase.lower()}*.md")
                      or _task_glob(task_id, f"Phase{phase}/{artifact_type}__Phase{phase}*.md"))
        if not candidates:
            # Fallback: task root
            candidates = _task_glob(task_id, f"{artifact_type}__*.md")
        if candidates:
            rel = candidates[0].relative_to(root).as_posix()
            url = _make_url(rel)
            return f"[{match.group(0)}]({url})"
        print(f"WARNING [gen_docs]: Unresolved phase reference: {match.group(0)}")
        return match.group(0)

    phase_pattern = re.compile(
        r'(?<!\[)(?<![A-Za-z0-9_])(HL|TS|RF|ONB|RES|REVIEW)[- ]('
        + task_id_source
        + r')/([A-Z])(?![A-Za-z0-9_\]])'
    )
    content = phase_pattern.sub(_replace_phase, content)

    # --- HL-{ID} (dash-prefixed HL refs) ---
    def _replace_hl_dash(match: re.Match) -> str:
        task_id = match.group(1)
        candidates = _task_glob(task_id, f"HL-{task_id}*.md")
        if candidates:
            rel = candidates[0].relative_to(root).as_posix()
            url = _make_url(rel)
            return f"[{match.group(0)}]({url})"
        print(f"WARNING [gen_docs]: Unresolved HL reference: {match.group(0)}")
        return match.group(0)

    hl_dash_pattern = re.compile(
        r'(?<!\[)(?<![A-Za-z0-9_])HL-(' + task_id_source
        + r')(?![A-Za-z0-9_\]])'
    )
    content = hl_dash_pattern.sub(_replace_hl_dash, content)

    # --- TD-{N} → tasks/DEBT-SNAPSHOT.md ---
    # The registry was retired at 2.1.0 and sealed verbatim in the legacy container. It has no
    # manifest row: the task-container glob already compiles it, exactly as it does BOARD-SNAPSHOT.
    def _replace_td(match: re.Match) -> str:
        n = match.group(1)
        url = (_posix_relpath("tasks/DEBT-SNAPSHOT.md", output_dir) if output_dir
               else "/tasks/DEBT-SNAPSHOT/")
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
                rel = candidates[0].relative_to(root).as_posix()
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
                    ".tfw/quickstart.md": "getting-started.md",
                    ".tfw/CHANGELOG.md": "reference/changelog.md",
                }
                if path_str in static_map:
                    url = _make_url(static_map[path_str])
                    return f"[`{path_str}`]({url})"
                if path_str == ".tfw/project_config.yaml":
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
        r'`((?:tasks|knowledge|\.tfw|KNOWLEDGE|README|RELEASE)[^`]*\.(?:md|yaml))`'
    )
    content = backtick_path_pattern.sub(_replace_backtick_path, content)

    # --- Bare task ID: {PREFIX}-{N} → task HL link ---
    def _replace_bare_task(match: re.Match) -> str:
        task_id = match.group(1)
        candidates = _task_glob(task_id, "")
        if not candidates:
            return match.group(0)
        folder = candidates[0]
        hl_candidates = sorted(folder.glob(f"HL-{task_id}*.md")) + sorted(
            folder.glob(f"HL__{task_id}*.md")
        )
        if hl_candidates:
            rel = hl_candidates[0].relative_to(root).as_posix()
            url = _make_url(rel)
            return f"[{match.group(0)}]({url})"
        landing = f"{_task_output_dir(root, folder)}/index.md"
        fallback = _posix_relpath(landing, output_dir) if output_dir else _md_to_url("/" + landing)
        return f"[{match.group(0)}]({fallback})"

    bare_task_pattern = re.compile(
        r'(?<!\[)(?<![A-Za-z0-9_])(' + task_id_source
        + r')(?![A-Za-z0-9_/\]])'
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
    nav["Reference", "Changelog"] = "reference/changelog.md"
    if (root / "RELEASE.md").exists():
        nav["Reference", "Release"] = "reference/release.md"
    # Dynamic: workflows
    for path in sorted(root.glob(".tfw/workflows/**/*.md")):
        subpath = path.relative_to(root / ".tfw" / "workflows")
        name = subpath.stem.replace("_", " ").title()
        sub_str = subpath.as_posix()
        parent_parts = list(subpath.parent.parts) if str(subpath.parent) != "." else []
        nav_key = ("Reference", "Workflows") + tuple(
            p.replace("_", " ").title() for p in parent_parts
        ) + (name,)
        nav[nav_key] = f"reference/workflows/{sub_str}"
    # Dynamic: templates
    for path in sorted(root.glob(".tfw/templates/**/*.md")):
        subpath = path.relative_to(root / ".tfw" / "templates")
        name = subpath.stem.replace("_", " ").title()
        sub_str = subpath.as_posix()
        parent_parts = list(subpath.parent.parts) if str(subpath.parent) != "." else []
        nav_key = ("Reference", "Templates") + tuple(
            p.replace("_", " ").title() for p in parent_parts
        ) + (name,)
        nav[nav_key] = f"reference/templates/{sub_str}"
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
        "reference/workflows/": "Workflows",
        "reference/templates/": "Templates",
    }
    # Several globs may share one output prefix — every configured task container writes
    # into `tasks/`. Pages are collected per prefix and the section index is generated once
    # per prefix, or the last container would silently replace the others.
    pages_by_prefix: dict[str, list[str]] = {}
    for pattern, prefix, _required in _glob_sources(root):
        base_path = Path(_glob_base(pattern))
        for path in sorted(root.glob(pattern)):
            relative = path.relative_to(root)
            try:
                subpath = relative.relative_to(base_path)
            except ValueError:
                subpath = relative
            pages_by_prefix.setdefault(prefix, []).append(
                _glob_output_path(relative, base_path, prefix))
        copy_glob(pattern, prefix, root, task_prefix, path_map)

    for prefix, pages in pages_by_prefix.items():
        if prefix == "tasks/":
            continue
        title = section_titles.get(prefix, prefix.rstrip("/").replace("/", " ").title())
        if pages:
            _generate_section_index(prefix, title, sorted(set(pages)))

    # Hidden task landings are link infrastructure only: they are intentionally absent from nav.
    _generate_task_landings(root, path_map)

    # 3. Generate navigation (literate-nav SUMMARY.md)
    _generate_nav(root)


# mkdocs-gen-files executes at module level during build
# Guard: only run when mkdocs_gen_files is the real package (not a test mock)
if hasattr(mkdocs_gen_files, "open"):
    main()
