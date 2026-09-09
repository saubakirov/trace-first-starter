"""One-shot Executor TRACE: preserve native observations; never run receiver workflows."""
from pathlib import Path
from datetime import datetime
import hashlib
import io
import json
import re
import tarfile

SOURCE = Path('E:/TEMP/tfw-slc-native-05c6fcdfe6a1')
OUTPUT = Path(__file__).resolve().parent
ARCHIVE = OUTPUT / 'native-evidence.tar.xz'
INDEX = OUTPUT / 'native-package-index.json'
VERIFY = OUTPUT / 'native-package-verification.json'
assert not any(p.exists() for p in (ARCHIVE, INDEX, VERIFY)), 'Preserve previous packaging epochs'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def descendants(path):
    entries = sorted(path.rglob('*'))
    assert all(not p.is_symlink() for p in entries), 'Unexpected symbolic link'
    assert all(p.is_file() or p.is_dir() for p in entries), 'Unexpected filesystem object'
    return entries


expected = {
    'FINAL-NATIVE-RETURN.md': 'dddeed4d720324c7601aa1afe2b5fa7ce6948ad2d8c334308c33b99b05217728',
    'EVIDENCE-INDEX.json': 'a8fb01c6930c01b09446f4adc408d12057b997c7c24903d59e3d858ce9de0cb9',
}
for name, sha in expected.items():
    assert digest((SOURCE / 'observations' / name).read_bytes()) == sha, name
native = read_json(SOURCE / 'observations/EVIDENCE-INDEX.json')
assert native['candidate'] == '05c6fcdfe6a1c1b4e9615f0390d094ee1b1fb5e8'

entries = descendants(SOURCE)
mapping = {}
for path in entries:
    record = {'entry': 'native/' + path.relative_to(SOURCE).as_posix(),
              'kind': 'file' if path.is_file() else 'directory'}
    if path.is_file():
        data = path.read_bytes()
        record.update(bytes=len(data), sha256=digest(data))
    mapping[path.as_posix()] = record

locators = []


def inspect_locators(value):
    if isinstance(value, dict):
        if 'path' in value and 'sha256' in value:
            p = Path(value['path'])
            actual = mapping[p.as_posix()]
            assert actual['sha256'] == value['sha256'], p
            if 'bytes' in value:
                assert actual['bytes'] == value['bytes'], p
            locators.append(p.as_posix())
        for child in value.values():
            inspect_locators(child)
    elif isinstance(value, list):
        for child in value:
            inspect_locators(child)


inspect_locators(native)
tree_checks = []


def verify_tree(path, manifest_path):
    manifest = read_json(manifest_path)
    actual_paths = descendants(path)
    files = {p.relative_to(path).as_posix(): mapping[p.as_posix()] for p in actual_paths if p.is_file()}
    directories = sorted(p.relative_to(path).as_posix() for p in actual_paths if p.is_dir())
    assert set(files) == set(manifest['files']), path
    assert directories == sorted(manifest['directories']), path
    for name, expected_file in manifest['files'].items():
        assert files[name]['sha256'] == expected_file['sha256'], (path, name)
        assert files[name]['bytes'] == expected_file['bytes'], (path, name)
    tree_checks.append({'root': path.as_posix(), 'manifest': manifest_path.as_posix(), 'files': len(files), 'mismatches': 0})


for case in native['cases']:
    for snapshot in case['snapshots']:
        manifest_path = Path(snapshot['path'])
        verify_tree(manifest_path.parent / 'tree', manifest_path)
    verify_tree(Path(case['receiver']), Path(case['final_manifest']['path']))

report = (SOURCE / 'observations/FINAL-NATIVE-RETURN.md').read_text(encoding='utf-8-sig')
links = re.findall(r'\]\((E:/[^)]+)\)', report)
assert all(Path(link).as_posix() in mapping for link in links)
diffs = []
for path in sorted((SOURCE / 'observations').glob('NF-*/*diff.json')):
    if path.name in ('repeat-diff.json', 'resume-diff.json'):
        value = read_json(path)
        assert value == {'added': [], 'removed': [], 'modified': []}, path
        diffs.append(path.as_posix())
assert len(diffs) == 8

old = native['original_deviating_nf3_receipt']
old_path = (SOURCE / 'receivers/nf3-tasks/.tfw/update_receipts/UPDATE__20260909-233251__4fcd.md').as_posix()
assert old_path not in mapping
aliases = {old_path: {
    'entry': mapping[old['retained']['path']]['entry'],
    'sha256': old['original_sha256'],
    'reason': 'Coordinator re-preparation relocated the original attempt before Executor intake; original receipt locators are unchanged.',
    'also_retained_entry': mapping[old['snapshot']['path']]['entry'],
}}
manifest = {'format': 'SLC native evidence transport map v1', 'original_root': SOURCE.as_posix(),
            'candidate': native['candidate'], 'paths': mapping, 'historical_locator_aliases': aliases,
            'scope': 'Every file and directory under the supplied native root; exact file bytes. No receipt path, content or attribution rewritten.'}
manifest_bytes = (json.dumps(manifest, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
with tarfile.open(ARCHIVE, 'w:xz', preset=6) as archive:
    for absolute, record in mapping.items():
        path = Path(absolute)
        info = tarfile.TarInfo(record['entry'])
        info.mtime = int(path.stat().st_mtime)
        info.mode = 0o644 if record['kind'] == 'file' else 0o755
        if record['kind'] == 'file':
            data = path.read_bytes()
            assert digest(data) == record['sha256'], ('changed during packaging', path)
            info.size = len(data)
            archive.addfile(info, io.BytesIO(data))
        else:
            info.type = tarfile.DIRTYPE
            archive.addfile(info)
    info = tarfile.TarInfo('TRANSPORT-MANIFEST.json')
    info.size = len(manifest_bytes)
    archive.addfile(info, io.BytesIO(manifest_bytes))

# Read every compressed member, verify its bytes and membership; do not extract over originals.
by_entry = {v['entry']: v for v in mapping.values()}
with tarfile.open(ARCHIVE, 'r:xz') as archive:
    members = archive.getmembers()
    names = [m.name for m in members]
    assert len(names) == len(set(names))
    assert set(names) == set(by_entry) | {'TRANSPORT-MANIFEST.json'}
    for member in members:
        assert not member.name.startswith('/') and '..' not in Path(member.name).parts
        if member.name == 'TRANSPORT-MANIFEST.json':
            assert archive.extractfile(member).read() == manifest_bytes
            continue
        record = by_entry[member.name]
        assert member.isdir() == (record['kind'] == 'directory')
        if member.isfile():
            data = archive.extractfile(member).read()
            assert len(data) == record['bytes'] and digest(data) == record['sha256']
        else:
            assert member.isdir()

assert [p.as_posix() for p in descendants(SOURCE)] == [p.as_posix() for p in entries]
for absolute, record in mapping.items():
    if record['kind'] == 'file':
        assert digest(Path(absolute).read_bytes()) == record['sha256'], ('source changed', absolute)

archive_sha = digest(ARCHIVE.read_bytes())
index = {'candidate': native['candidate'], 'archive': ARCHIVE.name, 'archive_bytes': ARCHIVE.stat().st_size,
         'archive_sha256': archive_sha, 'manifest_entry': 'TRANSPORT-MANIFEST.json',
         'manifest_sha256': digest(manifest_bytes), 'original_root': SOURCE.as_posix(),
         'entry_rule': 'native/ plus the path relative to original_root; full exact absolute-path map and directory entries are inside TRANSPORT-MANIFEST.json.',
         'original_return': {'entry': 'native/observations/FINAL-NATIVE-RETURN.md', 'sha256': expected['FINAL-NATIVE-RETURN.md']},
         'original_index': {'entry': 'native/observations/EVIDENCE-INDEX.json', 'sha256': expected['EVIDENCE-INDEX.json']},
         'historical_locator_aliases': aliases, 'cases': native['cases'],
         'read_instruction': 'Use Python tarfile or an xz-capable archive reader. Extract only to a separate fresh directory if desired. Do not replace absolute paths inside immutable receipts. Apply the transport map and the explicit old NF-3 alias when opening a preserved locator.'}
verification = {'observed_at': datetime.now().astimezone().isoformat(), 'operator_task': '01a08585-01f5-7101-b4a7-5155aaead0da',
                'kind': 'Executor packaging integrity verification, not independent product acceptance',
                'candidate': native['candidate'], 'archive_sha256': archive_sha,
                'source_files': sum(v['kind'] == 'file' for v in mapping.values()),
                'source_directories': sum(v['kind'] == 'directory' for v in mapping.values()),
                'source_file_bytes': sum(v.get('bytes', 0) for v in mapping.values()),
                'indexed_hashed_locators': len(locators), 'report_links': len(links),
                'snapshot_trees': sum(len(c['snapshots']) for c in native['cases']), 'current_receivers': len(native['cases']),
                'snapshot_and_receiver_file_hash_comparisons': sum(t['files'] for t in tree_checks),
                'tree_checks': tree_checks, 'zero_write_repeat_resume_diffs': diffs,
                'all_archive_members_read': True, 'archive_members': len(mapping) + 1,
                'source_rechecked_after_packaging': True, 'source_writes': 0, 'mismatches': 0}
for path, data in ((INDEX, index), (VERIFY, verification)):
    with path.open('x', encoding='utf-8', newline='\n') as output:
        json.dump(data, output, ensure_ascii=False, indent=2)
        output.write('\n')
print(json.dumps({k: v for k, v in verification.items() if k not in ('tree_checks', 'zero_write_repeat_resume_diffs')}, indent=2))
print('Archive bytes:', ARCHIVE.stat().st_size)
