"""Retain exact text source snapshots without committing deep duplicated receiver paths."""
from pathlib import Path
import json
import hashlib

EV = Path(__file__).resolve().parent


def main():
    snapshots = {}
    for folder in sorted((EV / "package-snapshots").iterdir()):
        sources = {}
        for path in sorted(folder.rglob("*")):
            if path.is_file():
                data = path.read_bytes()
                sources[path.relative_to(folder).as_posix()] = {
                    "utf8_text": data.decode("utf-8"), "sha256": hashlib.sha256(data).hexdigest()}
        actual_id = hashlib.sha256(json.dumps({p: row["sha256"] for p, row in sources.items()}, sort_keys=True).encode()).hexdigest()
        assert actual_id == folder.name
        snapshots[folder.name] = sources
    (EV / "package-sources.json").write_text(json.dumps({"kind": "Exact UTF-8 snapshot bytes; source-labelled local proof, not release",
        "snapshots": snapshots}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"source_snapshots": len(snapshots), "bytes": (EV / "package-sources.json").stat().st_size}))


if __name__ == "__main__":
    main()
