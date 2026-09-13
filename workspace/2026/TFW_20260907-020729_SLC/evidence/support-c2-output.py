"""One-shot C2 TRACE observation of the completed build and unchanged dependencies."""
import hashlib
import json
import subprocess
import tarfile
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
SITE = ROOT / 'site'
ID = 'TFW_20260907-020729_SLC'
OLD = '05c6fcdfe6a1c1b4e9615f0390d094ee1b1fb5e8'
CONTROL = 'd1ecc6994ea20fccddaaff57b7eb593ee490930f'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT).decode().strip()

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path; self.active = False; self.links = []; self.ids = set()
        self.text = ''; self.anchor = None; self.row = None; self.rows = []
        self.code = None
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'article':
            self.active = True
        if not self.active:
            return
        if tag == 'tr':
            self.row = {'text': '', 'links': [], 'code': []}
        if tag == 'code':
            self.code = ''
        if tag == 'a':
            self.anchor = {'href': attrs.get('href', ''), 'text': ''}

    def handle_data(self, data):
        if self.active:
            self.text += data
            if self.row is not None:
                self.row['text'] += data
            if self.code is not None:
                self.code += data
            if self.anchor is not None:
                self.anchor['text'] += data

    def handle_endtag(self, tag):
        if tag == 'a' and self.anchor is not None:
            self.links.append(self.anchor)
            if self.row is not None:
                self.row['links'].append(self.anchor)
            self.anchor = None
        if tag == 'code' and self.code is not None:
            if self.row is not None:
                self.row['code'].append(self.code)
            self.code = None
        if tag == 'tr' and self.row is not None:
            self.rows.append(self.row); self.row = None
        if tag == 'article':
            self.active = False

opened = {}
def read(path):
    path = path.resolve()
    if path not in opened:
        opened[path] = Page(path)
    return opened[path]

def follow(page, link):
    url = urlsplit(link['href'])
    assert not url.scheme and not url.netloc, link
    target = (page.path.parent / unquote(url.path)).resolve() if url.path else page.path
    if target.is_dir():
        target /= 'index.html'
    assert target.is_file(), (page.path, link, target)
    target_page = read(target)
    assert not url.fragment or unquote(url.fragment) in target_page.ids, (page.path, link)
    return {**link, 'target': target.relative_to(SITE).as_posix(),
            'target_sha256': sha(target), 'fragment_valid': True}

folder = SITE / 'tasks/2026' / ID
hl = folder / f'HL-{ID}/index.html'
cases = []
sources = [(folder / f'{kind}__{ID}/index.html', label) for kind, label in
           [('RF', 'Frozen SLC HL'), ('TS', 'Frozen SLC HL'),
            ('REVIEW', 'HL '), ('ONB', f'HL {ID}')]]
sources += [(folder / 'status/index.html', f'HL-{ID}')]
sources += [(p, f'HL-{ID}') for p in sorted((folder / 'journal').glob('*/index.html'))
            if f'>HL-{ID}</a>' in p.read_text(encoding='utf-8')]
for path, label in sources:
    page = read(path)
    selected = [a for a in page.links if label in a['text'] and f'HL-{ID}' in a['href']]
    assert selected, (path, label)
    resolved = []
    for link in selected:
        assert not any(c in link['href'] for c in '[]()'), link
        item = follow(page, link)
        assert item['target'] == hl.relative_to(SITE).as_posix(), item
        resolved.append(item)
    cases.append({'case': label, 'page': path.relative_to(SITE).as_posix(), 'links': resolved})

old_output = json.loads((HERE / 'opened-output.json').read_text(encoding='utf-8'))
for case in old_output['cases']:
    page = read(ROOT / case['opened_html'])
    landing = read(ROOT / case['landing'])
    links = [follow(landing, a) for a in landing.links
             if a['href'] and not a['href'].startswith('#') and not urlsplit(a['href']).scheme]
    assert links
    cases.append({'case': 'C2 fresh: ' + case['case'],
                  'page': page.path.relative_to(SITE).as_posix(),
                  'landing': landing.path.relative_to(SITE).as_posix(), 'links': links})

knowledge = read(SITE / 'knowledge-index/index.html')
rows = [r for r in knowledge.rows if r['text'].lstrip().startswith(('Task Storage', 'D87', ID,
        'tasks as the fresh Full default'))]
assert len(rows) == 4, [r['text'][:90] for r in rows]
for row in rows:
    row['resolved_links'] = [follow(knowledge, a) for a in row['links']
                             if a['href'] and not urlsplit(a['href']).scheme]
guide = '.tfw/migrations/3.3.0.md'
assert sum(guide in r['code'] for r in rows) == 3
assert not any(guide in a['href'] for r in rows for a in r['links'])
assert git('hash-object', 'KNOWLEDGE.md') == git('rev-parse', f'{CONTROL}:KNOWLEDGE.md')
assert git('hash-object', f'workspace/2026/{ID}/TS__{ID}.md') == '6535418fb65ad1b6f7f7a7b40a01506c1df27943'

build = json.loads((HERE / 'c2-03-integration.receipt.json').read_text(encoding='utf-8'))
old_check = json.loads((HERE / '08-full.receipt.json').read_text(encoding='utf-8'))
build_changed = [p for p, h in build['source_sha256'].items() if sha(ROOT / p) != h]
assert not build_changed, build_changed
old_changes = [p for p, h in old_check['source_sha256'].items() if sha(ROOT / p) != h]
allowed = {'docs/scripts/gen_docs.py', 'docs/scripts/test_gen_docs.py', 'docs/scripts/test_integration.py'}
assert {p.replace('\\', '/') for p in old_changes} == allowed, old_changes

release = ['.tfw/VERSION', '.tfw/project_config.yaml', '.tfw/templates/project_config.yaml',
           '.tfw/CHANGELOG.md', '.tfw/templates/briefing.md', '.tfw/adapters/manifest.yaml']
release += [p.relative_to(ROOT).as_posix() for p in sorted((ROOT / '.tfw/migrations').glob('*.md'))]
release += [f'{base}/tfw-{name}.md' for base in ['.agents/workflows', '.claude/commands']
            for name in ['init', 'resume', 'knowledge', 'update']]
release += [f'.tfw/workflows/{name}.md' for name in ['init', 'resume', 'knowledge', 'update']]
release_rows = []
for path in release:
    blob = git('hash-object', path)
    assert blob == git('rev-parse', f'{OLD}:{path}'), path
    release_rows.append({'path': path, 'git_blob': blob, 'sha256': sha(ROOT / path), 'equal_original_candidate': True})
for name in ['init', 'resume', 'knowledge', 'update']:
    canonical = git('hash-object', f'.tfw/workflows/{name}.md')
    assert all(git('hash-object', f'{base}/tfw-{name}.md') == canonical
               for base in ['.agents/workflows', '.claude/commands'])
assert (ROOT / '.tfw/VERSION').read_text().strip() == '3.3.0'
assert '(migrations/3.3.0.md)' in (ROOT / '.tfw/CHANGELOG.md').read_text(encoding='utf-8')
native_sha = sha(HERE / 'native-evidence.tar.xz')
assert native_sha == '2b96acbdd5fd814477bd330c8642a1908af1d07a5beb01854bb30b441aa513a5'

archive = HERE / 'c2-opened-html.tar.xz'
with tarfile.open(archive, 'x:xz') as tar:
    for path in sorted(opened):
        tar.add(path, arcname=path.relative_to(SITE).as_posix(), recursive=False)
with tarfile.open(archive, 'r:xz') as tar:
    for member in tar.getmembers():
        assert hashlib.sha256(tar.extractfile(member).read()).hexdigest() == sha(SITE / member.name)
record = {'observed_at': datetime.now().astimezone().isoformat(), 'input_head': git('rev-parse', 'HEAD'),
          'source_epoch': 'C2 checked product/test working bytes; RF/EV correction append is later TRACE',
          'method': 'Read completed HTML bytes, parsed article text/anchors, followed actual local URLs and fragments; no browser or human-delivery claim',
          'cases': cases, 'knowledge_rows': rows, 'knowledge_source_sha256': sha(ROOT / 'KNOWLEDGE.md'),
          'opened_pages': [{'path': p.relative_to(SITE).as_posix(), 'sha256': sha(p)} for p in sorted(opened)],
          'archive': {'path': archive.name, 'sha256': sha(archive), 'members': len(opened)},
          'release_constituents': release_rows,
          'reuse': {'original_check': '08-full.receipt.json', 'original_changed_dependencies': old_changes,
                   'fresh_build_source_hashes': len(build['source_sha256']), 'changes_after_build': build_changed,
                   'native_archive_sha256': native_sha,
                   'claim': 'Reuse unchanged source/native claims only; resolver and generated-output claims use C2. No new full suite or native run.'},
          'limits': 'Selected routes only; historical link/anchor diagnostics remain. Raw non-Markdown site publication is excluded O8. O7 independent payment and closing remain pending.'}
with (HERE / 'c2-opened-output.json').open('x', encoding='utf-8', newline='\n') as f:
    json.dump(record, f, ensure_ascii=False, indent=2); f.write('\n')
print(json.dumps({'cases': len(cases), 'pages': len(opened), 'knowledge_rows': len(rows),
                  'release_constituents': len(release_rows), 'archive': record['archive'],
                  'reuse': record['reuse']}, indent=2))
