import importlib.util
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("daily_ab", REPO / "tools" / "daily_ab.py")
ab = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ab)


def journal_line(n):
    return json.dumps({
        "type": "assistant", "sessionId": "s", "timestamp": "2026-11-14T08:00:{:02d}.000Z".format(n),
        "message": {"id": "msg_{}".format(n), "model": "m", "usage": {
            "input_tokens": 10, "cache_read_input_tokens": 100, "cache_creation_input_tokens": 5,
            "output_tokens": 20}}})


def test_ab_overlay_replaces_package_with_commit_bytes(tmp_path):
    stale = tmp_path / ".tfw" / "extensions" / "daily-task" / "scripts" / "stale.py"
    stale.parent.mkdir(parents=True)
    stale.write_text("x", encoding="utf-8")
    ab.overlay(tmp_path, "8923f7d9")
    assert not stale.exists()
    assert (tmp_path / ".tfw" / "extensions" / "daily-task" / "references" / "economics.md").is_file()
    assert (tmp_path / ".claude" / "skills" / "tfw-daily-task" / "SKILL.md").is_file()


def test_ab_child_env_drops_parent_session(monkeypatch):
    monkeypatch.setenv("CLAUDE_CODE_SESSION_ID", "parent")
    monkeypatch.setenv("CLAUDECODE", "1")
    monkeypatch.setenv("CLAUDE_CODE_GIT_BASH_PATH", "bash")
    env = ab.child_env()
    assert "CLAUDE_CODE_SESSION_ID" not in env and "CLAUDECODE" not in env
    assert env["CLAUDE_CODE_GIT_BASH_PATH"] == "bash"


def test_ab_context_per_call_and_summary(tmp_path):
    path = tmp_path / "s.jsonl"
    path.write_text("\n".join([journal_line(1), journal_line(1), journal_line(2), "[]"]) + "\n", encoding="utf-8")
    assert ab.context_per_call(path, 0) == 115
    assert ab.context_per_call(path, 2) == 115 and ab.context_per_call(path, 3) is None
    runs = [{"variant": "a", "run": n, "work": {"seconds": s, "turns": 10, "context_per_call": 100, "denials": []},
             "close": {"seconds": 5, "turns": 2, "denials": ["Bash"]}, "record_bytes": 1000,
             "capture": {"received": 1, "failures": 0, "binding_gaps": 0, "unwritten": 0}}
            for n, s in ((1, 10), (2, 30), (3, 20))]
    table = ab.summary(runs)
    assert "| a | median | 20 | 10 | 100 | 5 | 2 | | | 1000 |" in table
    assert "1 received, 0 failed, 0 gaps, 0 not written | Bash |" in table
