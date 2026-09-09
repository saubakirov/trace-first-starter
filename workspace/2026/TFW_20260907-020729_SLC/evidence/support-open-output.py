"""Open the actual built HTML and follow representative historical/current landing links."""
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
import json

ROOT = Path(__file__).resolve().parents[4]
SITE = ROOT/'site'
EVIDENCE = Path(__file__).resolve().parent


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.links, self.words = [], []
        self.feed(path.read_text(encoding='utf-8'))
    def handle_starttag(self, tag, attrs):
        if tag == 'a' and dict(attrs).get('href'):
            self.links.append(dict(attrs)['href'])
    def handle_data(self, value):
        self.words.append(value)


cases = [
    ('legacy HL', 'tasks/TFW-18__knowledge_consolidation', 'HL-TFW-18__knowledge_consolidation', 'knowledge'),
    ('historical phase', 'tasks/TFW-60__conflict_resistant_shared_workspace', 'phase-a/RF__phase-a__task_state_and_coordination', 'coordination'),
    ('no-HL historical landing', 'tasks/TFW-36__content_marketing_blog_series', '', 'TFW-36'),
    ('current task', 'tasks/2026/TFW_20260907-020729_SLC', 'TS__TFW_20260907-020729_SLC', 'Workspace'),
]
results = []
for label, task, artifact, expected in cases:
    landing = SITE/task/'index.html'
    page_path = SITE/task/artifact/'index.html' if artifact else landing
    page = Page(page_path)
    assert expected.lower() in ' '.join(page.words).lower(), label
    navigation = Page(landing)
    resolved = []
    for href in navigation.links:
        parsed = urlsplit(href)
        if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith('/'):
            continue
        target = (landing.parent/unquote(parsed.path)).resolve()
        if target.is_dir(): target /= 'index.html'
        if target.is_relative_to(landing.parent) and target.suffix == '.html':
            assert target.exists(), (label,href)
            resolved.append({'href':href,'target':target.relative_to(SITE).as_posix()})
    if artifact:
        assert any(row['target'] == page_path.relative_to(SITE).as_posix() for row in resolved), label
    else:
        assert any('status/index.html' in row['target'] for row in resolved), label
    results.append({'case':label,'opened_html':page_path.relative_to(ROOT).as_posix(),
                    'sha256':hashlib.sha256(page_path.read_bytes()).hexdigest(),
                    'landing':landing.relative_to(ROOT).as_posix(),'resolved_relative_links':resolved})
record={'observed_at':datetime.now().astimezone().isoformat(),
        'subject':'actual local MkDocs output from 08-full; not a native agent workflow run',
        'method':'read completed HTML, inspect rendered text and follow real relative landing hyperlinks',
        'cases':results}
out=EVIDENCE/'opened-output.json'
assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2))
