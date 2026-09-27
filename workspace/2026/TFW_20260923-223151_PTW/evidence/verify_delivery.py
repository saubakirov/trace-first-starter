"""Finite source/copy/check evidence for PTW; not a receiver dependency or permanent test."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import yaml

ROOT = Path(__file__).resolve().parents[4]
EV = Path(__file__).resolve().parent


def main():
    report = {"copies": {}, "word_counts": {}, "metadata": {}, "commands": {}, "build": {}}
    manifest = yaml.safe_load((ROOT / ".tfw/adapters/manifest.yaml").read_text(encoding="utf-8"))
    assert len(manifest["commands"]) == 10
    report["commands"]["Full_manifest"] = list(manifest["commands"])
    assert set(manifest["commands"]) == {"plan", "research", "handoff", "review", "docs", "knowledge", "release", "update", "config", "init"}
    expected = {f"tfw-{name}.md" for name in manifest["commands"]}
    assert {p.name for p in (ROOT / ".claude/commands").glob("tfw-*.md")} == expected
    for name, row in manifest["commands"].items():
        canonical = (ROOT / row["workflow"]).read_bytes()
        copy = (ROOT / f".claude/commands/tfw-{name}.md").read_bytes()
        assert canonical == copy
        report["copies"][f".claude/commands/tfw-{name}.md"] = hashlib.sha256(canonical).hexdigest()
        router = f".agents/skills/tfw-{name}/SKILL.md"
        source = f".tfw/adapters/codex/skills/tfw-{name}/SKILL.md"
        assert (ROOT / router).read_bytes() == (ROOT / source).read_bytes()
        report["copies"][router] = hashlib.sha256((ROOT / source).read_bytes()).hexdigest()
    prefix = ".tfw/extensions/daily-task/"
    for key, target in [("codex", ".agents/skills/tfw-daily-task/SKILL.md"),
                        ("claude-code", ".claude/skills/tfw-daily-task/SKILL.md")]:
        source = prefix + f"entries/{key}/SKILL.md"
        assert (ROOT / target).read_bytes() == (ROOT / source).read_bytes()
        report["copies"][target] = hashlib.sha256((ROOT / source).read_bytes()).hexdigest()
    for path in [prefix + "SKILL.md", prefix + "entries/codex/SKILL.md", prefix + "entries/claude-code/SKILL.md"]:
        text = (ROOT / path).read_text(encoding="utf-8")
        data = yaml.safe_load(text.split("---", 2)[1])
        assert data["name"] == "tfw-daily-task" and isinstance(data["description"], str)
        report["metadata"][path] = data
    for path in [prefix + "SKILL.md", prefix + "installation.md", ".tfw/workflows/init.md",
                 ".tfw/workflows/update.md", ".tfw/workflows/config.md"]:
        count = len((ROOT / path).read_text(encoding="utf-8").split())
        assert count <= 1400, (path, count)
        report["word_counts"][path] = count
    before_manifest = subprocess.check_output(["git", "show", "0c32c50e8d7c0dd2b7c509e5cc0605e64c76d669:.tfw/adapters/manifest.yaml"], cwd=ROOT)
    assert before_manifest == (ROOT / ".tfw/adapters/manifest.yaml").read_bytes()
    for protected in [".tfw/templates/HL.md", ".tfw/templates/RF.md"]:
        assert subprocess.check_output(["git", "show", f"0c32c50e8d7c0dd2b7c509e5cc0605e64c76d669:{protected}"], cwd=ROOT) == (ROOT / protected).read_bytes()
    report["protected_manifest_and_templates"] = "byte-identical to immutable Baseline"
    for kind, args in [("lint", ["--collect-only"]), ("test", [])]:
        command = [sys.executable, "-m", "pytest", "tools/tests/", "docs/scripts/", "-q"] + args
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        report["build"][kind] = {"command": "python -m pytest tools/tests/ docs/scripts/ -q" + (" --collect-only" if args else ""),
                                  "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr}
        assert result.returncode == 0, result.stdout + result.stderr
    result = subprocess.run(["git", "diff", "--check"], cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout
    report["diff_check"] = "passed"
    report["limits"] = "Source/installed/parity plus actual local fixture observations; no live Claude invocation, universal cost or independent Reviewer judgment"
    output = sys.argv[1] if len(sys.argv) > 1 else "delivery-verification.json"
    assert Path(output).name == output and output.endswith(".json")
    (EV / output).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"Full_routes": 10, "optional_entries": 2, "word_counts": report["word_counts"],
                      "build": {k: v["returncode"] for k, v in report["build"].items()}}))


if __name__ == "__main__":
    main()
