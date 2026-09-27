"""Preserve exact finite receiver bytes in one verified archive, before disposable-tree cleanup."""
from pathlib import Path
import hashlib
import json
import zipfile

EV = Path(__file__).resolve().parent


def main():
    source = (EV / "receivers").resolve()
    assert source.parent == EV.resolve() and source.name == "receivers"
    files = sorted(p for p in source.rglob("*") if p.is_file())
    assert all(not p.is_symlink() and p.resolve().is_relative_to(source) for p in files)
    target = EV / "package-receivers.zip"
    assert not target.exists()
    observed = {}
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            name = path.relative_to(EV).as_posix()
            data = path.read_bytes()
            archive.writestr(name, data)
            observed[name] = hashlib.sha256(data).hexdigest()
    with zipfile.ZipFile(target) as archive:
        assert archive.testzip() is None and set(archive.namelist()) == set(observed)
        assert all(hashlib.sha256(archive.read(name)).hexdigest() == value for name, value in observed.items())
    report = {"archive": target.name, "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
              "bytes": target.stat().st_size, "file_count": len(files), "entry_hashes": observed,
              "verification": "Every archive entry byte-hash matched actual receiver; CRC check passed",
              "raw_resource": "evidence/receivers", "disposition": "verified preservation; raw disposable receiver tree may be removed",
              "reconstruction": "Extract archive to a new task-owned assurance directory; do not restore over a live project"}
    (EV / "receiver-archive.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "entry_hashes"}))


if __name__ == "__main__":
    main()
