"""Disposable Phase B observation only; does not select or alter tests."""
import json
import os
from pathlib import Path
import subprocess
import time

OUT = Path(os.environ['PTTC_OBSERVATION'])


def emit(row):
    with OUT.with_suffix('.events.jsonl').open('a', encoding='utf-8') as stream:
        stream.write(json.dumps(row, ensure_ascii=True) + '\n')


OriginalPopen = subprocess.Popen


class ObservedPopen(OriginalPopen):
    def __init__(self, args, *pos, **kwargs):
        self.observed_args = [str(a) for a in args] if isinstance(args, (list, tuple)) else str(args)
        self.is_build = isinstance(self.observed_args, list) and self.observed_args[1:4] == ['-m', 'mkdocs', 'build']
        self.started = time.perf_counter()
        self.saved_build = False
        super().__init__(args, *pos, **kwargs)
        emit({'event': 'process_start', 'pid': self.pid, 'argv': self.observed_args,
              'cwd': str(kwargs.get('cwd', Path.cwd())), 'mkdocs': self.is_build})

    def communicate(self, *args, **kwargs):
        result = super().communicate(*args, **kwargs)
        if self.is_build and not self.saved_build:
            self.saved_build = True
            for suffix, value in zip(('stdout', 'stderr'), result):
                data = value if isinstance(value, bytes) else (value or '').encode('utf-8')
                OUT.with_suffix(f'.mkdocs-{self.pid}.{suffix}.txt').write_bytes(data)
            emit({'event': 'mkdocs_complete', 'pid': self.pid, 'exit': self.returncode,
                  'wall_seconds': time.perf_counter() - self.started})
        return result


subprocess.Popen = ObservedPopen


def pytest_runtest_logreport(report):
    emit({'event': 'test_report', 'nodeid': report.nodeid, 'when': report.when,
          'outcome': report.outcome, 'duration': report.duration})


def pytest_collection_finish(session):
    emit({'event': 'collection', 'count': len(session.items),
          'nodeids': [item.nodeid for item in session.items]})
