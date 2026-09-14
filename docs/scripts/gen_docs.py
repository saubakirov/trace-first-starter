"""Generate the public site from README and the core .tfw documentation only."""

import re
from pathlib import Path, PurePosixPath

import mkdocs_gen_files
import yaml


def _find_root(start: Path) -> Path:
    for candidate in (start, *start.parents):
        if (candidate / ".tfw").is_dir():
            return candidate
    raise SystemExit(f"no project root above {start}: no directory contains .tfw/")


ROOT = _find_root(Path(__file__).resolve().parent)

# Explicit allowlists are the publication boundary. Project traces are not documentation inputs.
STATIC_SOURCES = [
    ("README.md", "index.md", True),
    (".tfw/README.md", "concepts/philosophy.md", True),
    (".tfw/quickstart.md", "getting-started.md", True),
    (".tfw/conventions.md", "reference/conventions.md", True),
    (".tfw/glossary.md", "reference/glossary.md", True),
    (".tfw/CHANGELOG.md", "reference/changelog.md", True),
    (".tfw/compilable_contract.md", "reference/compilable-contract.md", True),
]

GLOB_SOURCES = [
    (".tfw/workflows/**/*.md", "reference/workflows/"),
    (".tfw/templates/**/*.md", "reference/templates/"),
]


def _normalize_posix_path(path: str) -> str:
    parts = path.replace("\\", "/").split("/")
    result = []
    for part in parts:
        if part in ("", "."):
            continue
        if part == ".." and result and result[-1] != "..":
            result.pop()
        else:
            result.append(part)
    return "/".join(result) if result else "."


def _posix_relpath(target: str, base_dir: str) -> str:
    target_parts = tuple(p for p in PurePosixPath(target).parts if p != ".")
    base_parts = tuple(p for p in PurePosixPath(base_dir).parts if p != ".")
    common = 0
    for base, target_part in zip(base_parts, target_parts):
        if base != target_part:
            break
        common += 1
    return "/".join([".."] * (len(base_parts) - common) + list(target_parts[common:])) or "."


def _glob_base(pattern: str) -> Path:
    parts = []
    for part in Path(pattern).parts:
        if "*" in part or "?" in part:
            break
        parts.append(part)
    return Path(*parts) if parts else Path(".")


def _glob_output_path(path: Path, base: Path, prefix: str) -> str:
    return prefix + path.relative_to(base).as_posix()


def _source_map(root: Path) -> dict[str, str]:
    mapping = {source: output for source, output, _ in STATIC_SOURCES}
    for pattern, prefix in GLOB_SOURCES:
        base = _glob_base(pattern)
        for path in sorted(root.glob(pattern)):
            relative = path.relative_to(root)
            mapping[relative.as_posix()] = _glob_output_path(relative, base, prefix)
    return mapping


def rewrite_markdown_links(content: str, source_path: str, mapping: dict[str, str]) -> str:
    """Rewrite links only when both source and destination are in the public allowlist."""
    source_dir = str(PurePosixPath(source_path).parent)

    def replace(match: re.Match) -> str:
        label, target = match.groups()
        if target.startswith(("http://", "https://", "#", "/")):
            return match.group(0)
        if "{" in target:
            return f"`{label}`"
        path, separator, fragment = target.partition("#")
        if not path.endswith(".md"):
            return match.group(0)
        resolved = _normalize_posix_path(f"{source_dir}/{path}")
        if resolved not in mapping:
            return match.group(0)
        current_output = mapping.get(source_path, source_path)
        current_dir = str(PurePosixPath(current_output).parent)
        rewritten = _posix_relpath(mapping[resolved], current_dir)
        suffix = f"#{fragment}" if separator else ""
        return f"[{label}]({rewritten}{suffix})"

    return re.sub(r"\[([^\]]*)\]\(([^)]+)\)", replace, content)


def extract_title(content: str, filename: str) -> str:
    for line in content.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return Path(filename).stem.replace("_", " ").title()


def add_frontmatter(content: str, title: str, source: str) -> str:
    if content.startswith("---"):
        return content
    header = yaml.safe_dump(
        {"title": title, "source": source},
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )
    return f"---\n{header}---\n\n{content}"


def validate_sources(root: Path) -> None:
    missing = [source for source, _output, required in STATIC_SOURCES
               if required and not (root / source).is_file()]
    if missing:
        raise FileNotFoundError("required documentation source missing: " + ", ".join(missing))


def copy_page(source: str, output: str, root: Path, mapping: dict[str, str]) -> None:
    content = (root / source).read_text(encoding="utf-8")
    content = rewrite_markdown_links(content, source, mapping)
    if source == "README.md":
        content = re.sub(r'(src|href)="docs/', r'\1="', content)
        content = re.sub(
            r'<p\s+align="center">\s*<img\s+src="([^"]+)"\s+alt="([^"]*)"[^>]*>\s*</p>',
            r'![\2](\1)',
            content,
        )
    rendered = add_frontmatter(content, extract_title(content, source), source)
    with mkdocs_gen_files.open(output, "w") as destination:
        destination.write(rendered)


def _section_index(prefix: str, pages: list[str]) -> None:
    lines = [f"# {Path(prefix.rstrip('/')).name.replace('_', ' ').title()}\n\n"]
    for page in sorted(pages):
        relative = page[len(prefix):]
        label = Path(relative).stem.replace("_", " ").title()
        lines.append(f"- [{label}]({relative})\n")
    with mkdocs_gen_files.open(prefix + "index.md", "w") as destination:
        destination.writelines(lines)


def _generate_nav(root: Path) -> None:
    nav = mkdocs_gen_files.Nav()
    nav["Home"] = "index.md"
    nav["Getting Started"] = "getting-started.md"
    nav["Concepts", "Philosophy"] = "concepts/philosophy.md"
    nav["Reference", "Conventions"] = "reference/conventions.md"
    nav["Reference", "Glossary"] = "reference/glossary.md"
    nav["Reference", "Changelog"] = "reference/changelog.md"
    nav["Reference", "Compilable Contract"] = "reference/compilable-contract.md"

    for pattern, prefix, label in (
        (GLOB_SOURCES[0][0], GLOB_SOURCES[0][1], "Workflows"),
        (GLOB_SOURCES[1][0], GLOB_SOURCES[1][1], "Templates"),
    ):
        base = _glob_base(pattern)
        for path in sorted(root.glob(pattern)):
            relative = path.relative_to(root).relative_to(base)
            keys = tuple(part.replace("_", " ").title() for part in relative.with_suffix("").parts)
            nav[("Reference", label) + keys] = prefix + relative.as_posix()

    with mkdocs_gen_files.open("SUMMARY.md", "w") as destination:
        destination.writelines(nav.build_literate_nav())


def main() -> None:
    validate_sources(ROOT)
    mapping = _source_map(ROOT)

    for source, output, _required in STATIC_SOURCES:
        copy_page(source, output, ROOT, mapping)

    for pattern, prefix in GLOB_SOURCES:
        base = _glob_base(pattern)
        pages = []
        for path in sorted(ROOT.glob(pattern)):
            relative = path.relative_to(ROOT)
            output = _glob_output_path(relative, base, prefix)
            pages.append(output)
            copy_page(relative.as_posix(), output, ROOT, mapping)
        _section_index(prefix, pages)

    _generate_nav(ROOT)


if hasattr(mkdocs_gen_files, "open"):
    main()
