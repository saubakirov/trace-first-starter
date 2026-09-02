# -*- coding: utf-8 -*-
"""Сборка печатного A4-документа из Markdown по нейтральному стилю TFW Assisted.

Каждый раздел верхнего уровня (## …) начинается с новой страницы.
Запуск: python build_a4.py practice_day1.md practice_day1.html "Практика Дня 1"
"""
import io, re, sys, html

CSS = """
@page { size: A4 portrait; margin: 18mm 20mm; }
:root{
  --primary:#243B53; --blue:#334E68; --accent:#D9E2EC; --purple:#486581;
  --text:#1F2933; --muted:#52606D; --line:#BCCCDC; --light:#F0F4F8;
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'IBM Plex Sans','Segoe UI',Arial,sans-serif;font-size:11pt;line-height:1.45;color:var(--text);background:#fff}
.page{page-break-after:always;padding-bottom:6mm}
.page:last-child{page-break-after:auto}
.doc-head{border-bottom:2px solid var(--primary);padding-bottom:8px;margin-bottom:16px;position:relative}
.doc-head img{position:absolute;right:0;top:0;height:11mm}
h1{font-size:26pt;font-weight:700;line-height:1.15;color:var(--text);margin-bottom:6px;max-width:150mm}
.doc-meta{font-size:9pt;color:var(--muted)}
h2{font-size:17pt;font-weight:700;color:var(--primary);margin:0 0 10px;line-height:1.2}
h3{font-size:14pt;font-weight:600;color:var(--blue);margin:14px 0 6px}
p{margin:0 0 8px}
ul,ol{margin:0 0 8px 18px}
li{margin-bottom:4px}
strong{font-weight:600}
code{font-family:'IBM Plex Mono',Consolas,monospace;font-size:10pt;background:var(--light);padding:1px 4px;border-radius:3px}
blockquote{margin:10px 0;padding:8px 14px;border-left:4px solid var(--accent);background:rgba(217,226,236,.55);font-style:normal}
blockquote p{margin:0}
table{width:100%;border-collapse:collapse;margin:8px 0 10px;page-break-inside:avoid}
th{background:var(--accent);color:#111;font-weight:600;font-size:10pt;text-align:left;padding:6px 8px;border:1px solid var(--line)}
td{font-size:10pt;padding:6px 8px;border:1px solid var(--line);vertical-align:top}
tbody tr:nth-child(even){background:var(--light)}
hr{border:0;border-top:1px solid var(--line);margin:12px 0}
.note{font-size:9pt;color:var(--muted)}
.pagenum{position:running(pn)}
@media print{ body{background:#fff} }
"""

INLINE = [
    (re.compile(r'`([^`]+)`'), lambda m: '<code>%s</code>' % html.escape(m.group(1))),
    (re.compile(r'\*\*([^*]+)\*\*'), r'<strong>\1</strong>'),
    (re.compile(r'(?<!\*)\*([^*\n]+)\*(?!\*)'), r'<em>\1</em>'),
    (re.compile(r'\[([^\]]+)\]\(([^)]+)\)'), r'\1'),
]


def inline(t):
    t = html.escape(t, quote=False)
    for pat, rep in INLINE:
        t = pat.sub(rep, t)
    return t


def md_to_pages(md):
    lines = md.split('\n')
    pages, cur = [], []
    i, n = 0, len(lines)
    title, meta = None, []
    in_meta = True
    while i < n:
        ln = lines[i]
        if ln.startswith('# ') and title is None:
            title = ln[2:].strip(); i += 1; continue
        if in_meta and ln.startswith('>'):
            meta.append(ln.lstrip('> ').rstrip()); i += 1; continue
        if ln.strip() == '---' and in_meta:
            in_meta = False; i += 1; continue
        if ln.startswith('## '):
            in_meta = False
            if cur: pages.append(cur)
            cur = [('h2', ln[3:].strip())]; i += 1; continue
        in_meta = False
        if ln.startswith('### '):
            cur.append(('h3', ln[4:].strip())); i += 1; continue
        if ln.startswith('|'):
            tbl = []
            while i < n and lines[i].startswith('|'):
                tbl.append(lines[i]); i += 1
            cur.append(('table', tbl)); continue
        if ln.startswith('> '):
            q = []
            while i < n and lines[i].startswith('>'):
                q.append(lines[i].lstrip('> ').rstrip()); i += 1
            cur.append(('quote', ' '.join(q))); continue
        if re.match(r'^\s*[-*] ', ln):
            it = []
            while i < n and re.match(r'^\s*[-*] ', lines[i]):
                it.append(re.sub(r'^\s*[-*] ', '', lines[i])); i += 1
            cur.append(('ul', it)); continue
        if re.match(r'^\s*\d+\. ', ln):
            it = []
            while i < n and re.match(r'^\s*\d+\. ', lines[i]):
                it.append(re.sub(r'^\s*\d+\. ', '', lines[i])); i += 1
            cur.append(('ol', it)); continue
        if ln.strip() == '---':
            i += 1; continue
        if ln.strip() == '':
            i += 1; continue
        para = [ln]
        i += 1
        while i < n and lines[i].strip() and not re.match(r'^(#{2,3} |\||> |\s*[-*] |\s*\d+\. |---$)', lines[i]):
            para.append(lines[i]); i += 1
        cur.append(('p', ' '.join(x.strip() for x in para)))
    if cur: pages.append(cur)
    return title, meta, pages


def render_table(rows):
    cells = [[c.strip() for c in r.strip().strip('|').split('|')] for r in rows]
    if len(cells) >= 2 and re.match(r'^:?-{2,}:?$', cells[1][0].replace(' ', '')):
        head, body = cells[0], cells[2:]
    else:
        head, body = None, cells
    out = ['<table>']
    if head:
        out.append('<thead><tr>' + ''.join('<th>%s</th>' % inline(c) for c in head) + '</tr></thead>')
    out.append('<tbody>')
    for r in body:
        out.append('<tr>' + ''.join('<td>%s</td>' % inline(c) for c in r) + '</tr>')
    out.append('</tbody></table>')
    return '\n'.join(out)


def render(title, meta, pages, doc_title):
    parts = ['<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8">',
             '<title>%s</title>' % html.escape(doc_title),
             '<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet">',
             '<style>%s</style></head><body>' % CSS]
    for pi, page in enumerate(pages):
        parts.append('<div class="page">')
        if pi == 0:
            parts.append('<div class="doc-head"><img src="assets/tfw-mark.svg" alt="TFW">')
            parts.append('<h1>%s</h1>' % inline(title or doc_title))
            if meta:
                parts.append('<p class="doc-meta">%s</p>' % inline(' · '.join(m for m in meta if m.strip())))
            parts.append('</div>')
        for kind, val in page:
            if kind == 'h2':
                parts.append('<h2>%s</h2>' % inline(val))
            elif kind == 'h3':
                parts.append('<h3>%s</h3>' % inline(val))
            elif kind == 'p':
                parts.append('<p>%s</p>' % inline(val))
            elif kind == 'ul':
                parts.append('<ul>' + ''.join('<li>%s</li>' % inline(x) for x in val) + '</ul>')
            elif kind == 'ol':
                parts.append('<ol>' + ''.join('<li>%s</li>' % inline(x) for x in val) + '</ol>')
            elif kind == 'quote':
                parts.append('<blockquote><p>%s</p></blockquote>' % inline(val))
            elif kind == 'table':
                parts.append(render_table(val))
        parts.append('</div>')
    parts.append('</body></html>')
    return '\n'.join(parts)


if __name__ == '__main__':
    src, dst, doc_title = sys.argv[1], sys.argv[2], sys.argv[3]
    md = io.open(src, encoding='utf-8').read()
    t, meta, pages = md_to_pages(md)
    io.open(dst, 'w', encoding='utf-8', newline='').write(render(t, meta, pages, doc_title))
    print('pages:', len(pages))
