#!/usr/bin/env python3
"""Build a standalone offline A4 HTML document from a small Markdown profile."""

from __future__ import annotations

import argparse
import html
from html.parser import HTMLParser
import os
from pathlib import Path
import re
import sys
import tempfile
import xml.etree.ElementTree as ET


PROPERTIES = ("--font-body", "--font-heading", "--color-text", "--color-muted", "--color-accent", "--color-paper")
THEME_INTERFACE = "assisted-theme-v1"
SHAPES = {"svg", "g", "path", "rect", "circle", "ellipse", "line", "polyline", "polygon"}
ATTRIBUTES = {
    "xmlns", "viewBox", "width", "height", "fill", "stroke", "stroke-width", "stroke-linecap",
    "stroke-linejoin", "d", "x", "y", "x1", "x2", "y1", "y2", "cx", "cy", "r", "rx", "ry",
    "points", "opacity", "fill-rule", "clip-rule", "transform",
}


class TemplateError(Exception):
    """Invalid input or unsafe local customization."""


def regular(path: Path, label: str) -> Path:
    if path.is_symlink() or not path.is_file():
        raise TemplateError(f"{label} must be a regular file")
    return path


def local_resource(raw: str, template_root: Path, label: str) -> Path:
    candidate = Path(raw)
    candidate = candidate if candidate.is_absolute() else template_root / candidate
    try:
        resolved = candidate.resolve(strict=True)
        if os.path.commonpath([str(resolved), str(template_root)]) != str(template_root):
            raise TemplateError(f"{label} must stay inside the template directory")
    except (OSError, ValueError) as exc:
        raise TemplateError(f"{label} is unavailable") from exc
    return regular(resolved, label)


def validate_theme(data: str) -> dict[str, str]:
    if "\\" in data or "@" in data or re.search(r"url\s*\(|content\s*:", data, re.I):
        raise TemplateError("theme contains an active or escaped construct")
    match = re.fullmatch(r"\s*:root\s*\{(?P<body>[^{}]*)\}\s*", data, re.S)
    if not match:
        raise TemplateError("theme must contain exactly one :root block")
    values = {}
    declarations = [item.strip() for item in match.group("body").split(";") if item.strip()]
    for declaration in declarations:
        if declaration.count(":") != 1:
            raise TemplateError("theme declaration is invalid")
        name, value = (item.strip() for item in declaration.split(":", 1))
        if name not in PROPERTIES or name in values or not value:
            raise TemplateError("theme properties must be the exact six-property interface")
        if name.startswith("--color-"):
            if not re.fullmatch(r"#[0-9a-fA-F]{6}", value):
                raise TemplateError("theme colors must use six-digit hex values")
        elif not re.fullmatch(r"[A-Za-zА-Яа-яЁё0-9 ,'\-]+", value):
            raise TemplateError("theme font stack is invalid")
        values[name] = value
    if set(values) != set(PROPERTIES):
        raise TemplateError("theme must define every declared property exactly once")
    return values


def validate_svg(data: bytes) -> str:
    if any(marker in data.upper() for marker in (b"<!DOCTYPE", b"<!ENTITY", b"<SCRIPT", b"<STYLE", b"<TEXT", b"<METADATA", b"<!--")):
        raise TemplateError("mark contains forbidden markup")
    try:
        root = ET.fromstring(data)
    except ET.ParseError as exc:
        raise TemplateError("mark is not valid SVG") from exc
    for element in root.iter():
        tag = element.tag.rsplit("}", 1)[-1]
        if tag not in SHAPES or element.text and element.text.strip() or element.tail and element.tail.strip():
            raise TemplateError("mark must contain shapes only")
        for raw_name, value in element.attrib.items():
            name = raw_name.rsplit("}", 1)[-1]
            if name not in ATTRIBUTES or name.casefold().startswith("on") or "url(" in value.casefold() or "http" in value.casefold():
                raise TemplateError("mark contains a forbidden attribute or reference")
    if root.tag.rsplit("}", 1)[-1] != "svg" or "viewBox" not in root.attrib:
        raise TemplateError("mark root and viewBox are required")
    return data.decode("utf-8")


def inline(raw: str) -> str:
    escaped = html.escape(raw, quote=False)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(?<!\*)\*([^*]+)\*", r"<em>\1</em>", escaped)
    return escaped


def table(lines: list[str]) -> str:
    rows = [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in lines]
    if len(rows) < 2 or not all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in rows[1]):
        return "".join(f"<p>{inline(line)}</p>" for line in lines)
    width = len(rows[0])
    if width == 0 or any(len(row) != width for row in rows):
        raise TemplateError("Markdown table rows have inconsistent widths")
    head = "".join(f"<th>{inline(cell)}</th>" for cell in rows[0])
    body = "".join("<tr>" + "".join(f"<td>{inline(cell)}</td>" for cell in row) + "</tr>" for row in rows[2:])
    return f"<div class=\"table-wrap\"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>"


def markdown(raw: str) -> str:
    lines = raw.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    output = []
    paragraph = []
    items = []
    table_lines = []
    code = []
    in_code = False

    def flush():
        nonlocal paragraph, items, table_lines
        if paragraph:
            output.append(f"<p>{inline(' '.join(item.strip() for item in paragraph))}</p>")
            paragraph = []
        if items:
            output.append("<ul>" + "".join(f"<li>{inline(item)}</li>" for item in items) + "</ul>")
            items = []
        if table_lines:
            output.append(table(table_lines))
            table_lines = []

    for line in lines:
        if line.startswith("```"):
            if in_code:
                output.append("<pre><code>" + html.escape("\n".join(code)) + "</code></pre>")
                code = []
            else:
                flush()
            in_code = not in_code
            continue
        if in_code:
            code.append(line)
            continue
        if line.strip() == "<!-- page -->":
            flush()
            output.append('<hr class="page-break">')
        elif not line.strip():
            flush()
        elif re.match(r"^#{1,4}\s+", line):
            flush()
            level = len(line) - len(line.lstrip("#"))
            output.append(f"<h{level}>{inline(line[level:].strip())}</h{level}>")
        elif re.match(r"^[-*]\s+", line):
            if paragraph or table_lines:
                flush()
            items.append(line[2:].strip())
        elif line.startswith("|") and line.endswith("|"):
            if paragraph or items:
                flush()
            table_lines.append(line)
        else:
            if items or table_lines:
                flush()
            paragraph.append(line)
    if in_code:
        raise TemplateError("unclosed Markdown code fence")
    flush()
    return "\n".join(output)


def document(title: str, body: str, theme: str, mark: str) -> str:
    safe_title = html.escape(title)
    return f"""<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{safe_title}</title><style>{theme}
@page{{size:A4;margin:16mm 17mm 18mm}}*{{box-sizing:border-box}}html{{background:#d8dce2}}body{{margin:0;color:var(--color-text);background:var(--color-paper);font:10.5pt/1.48 var(--font-body);print-color-adjust:exact;-webkit-print-color-adjust:exact}}main{{width:210mm;min-height:297mm;margin:10mm auto;padding:16mm 17mm 18mm;background:var(--color-paper);box-shadow:0 4px 24px #0002}}header{{display:flex;align-items:center;gap:10mm;border-bottom:2px solid var(--color-accent);padding-bottom:7mm;margin-bottom:10mm}}header svg{{width:18mm;height:18mm;flex:none}}h1,h2,h3,h4{{font-family:var(--font-heading);line-height:1.15;overflow-wrap:anywhere}}h1{{font-size:24pt;margin:0}}h2{{font-size:16pt;margin:10mm 0 4mm;color:var(--color-accent)}}h3{{font-size:12.5pt;margin:7mm 0 3mm}}p,li,td,th,code{{overflow-wrap:anywhere}}p{{margin:0 0 4mm}}li{{margin:0 0 1.5mm}}code,pre{{font-family:Consolas,'Courier New',monospace}}code{{background:#0000000b;padding:.05em .3em;border-radius:3px}}pre{{white-space:pre-wrap;overflow-wrap:anywhere;background:#00000008;border-left:3px solid var(--color-accent);padding:4mm}}.table-wrap{{overflow-x:auto;margin:5mm 0}}table{{border-collapse:collapse;width:100%;font-size:8.8pt}}th,td{{border:1px solid var(--color-muted);padding:2.2mm;text-align:left;vertical-align:top}}th:last-child,td:last-child{{min-width:21mm}}th{{color:var(--color-accent)}}.page-break{{border:0;break-after:page;page-break-after:always;margin:0;height:0}}footer{{margin-top:12mm;padding-top:4mm;border-top:1px solid var(--color-muted);color:var(--color-muted);font-size:8.5pt}}@media(max-width:220mm){{html{{background:var(--color-paper)}}main{{width:auto;margin:0;padding:8vw;box-shadow:none}}}}@media print{{html,body{{background:#fff}}main{{width:auto;min-height:auto;margin:0;padding:0;box-shadow:none}}header{{break-after:avoid}}.table-wrap{{overflow:visible}}}}
</style></head><body><main><header>{mark}<h1>{safe_title}</h1></header><article>{body}</article><footer>Локальный документ · TFW Assisted 1.5</footer></main></body></html>"""


def build(source: Path, output: Path, title: str, theme_path: Path, mark_path: Path) -> None:
    regular(source, "source")
    theme_text = theme_path.read_text(encoding="utf-8-sig")
    validate_theme(theme_text)
    mark_text = validate_svg(mark_path.read_bytes())
    result = document(title, markdown(source.read_text(encoding="utf-8-sig")), theme_text, mark_text)
    output.parent.mkdir(parents=True, exist_ok=True)
    descriptor, raw = tempfile.mkstemp(prefix=".a4-", suffix=".tmp", dir=output.parent)
    temporary = Path(raw)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(result)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, output)
        temporary = None
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(description=__doc__)
    value.add_argument("SOURCE", nargs="?")
    value.add_argument("OUTPUT", nargs="?")
    value.add_argument("TITLE", nargs="?")
    value.add_argument("--theme", default="theme.css")
    value.add_argument("--mark", default="assets/tfw-mark.svg")
    return value


def main() -> int:
    args = parser().parse_args()
    try:
        if not all((args.SOURCE, args.OUTPUT, args.TITLE)):
            raise TemplateError("SOURCE OUTPUT TITLE are required")
        root = Path(__file__).resolve().parent
        build(Path(args.SOURCE).expanduser().resolve(strict=True), Path(args.OUTPUT).expanduser().absolute(), args.TITLE, local_resource(args.theme, root, "theme"), local_resource(args.mark, root, "mark"))
        return 0
    except TemplateError as exc:
        print(f"blocked: {exc}", file=sys.stderr)
        return 4


if __name__ == "__main__":
    sys.exit(main())
