import importlib.util
import json
import tempfile
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
SID = "11111111-2222-3333-4444-555555555555"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


close_mod = load("daily_close", REPO / ".tfw" / "extensions" / "daily-task" / "scripts" / "daily_close.py")


def journal_line(n, session=SID):
    return json.dumps({
        "type": "assistant", "sessionId": session, "version": "2.1.323",
        "timestamp": "2026-11-14T08:00:{:02d}.000Z".format(n),
        "message": {"id": "msg_{}".format(n), "model": "claude-opus-5-5", "usage": {
            "input_tokens": 10, "cache_read_input_tokens": 100, "cache_creation_input_tokens": 5,
            "cache_creation": {"ephemeral_5m_input_tokens": 0, "ephemeral_1h_input_tokens": 5},
            "output_tokens": 20}}})


@pytest.fixture
def env(tmp_path, monkeypatch):
    monkeypatch.setattr(tempfile, "tempdir", str(tmp_path / "tmp"))
    (tmp_path / "tmp").mkdir()
    journal = tmp_path / "claude" / "projects" / "c--proj" / (SID + ".jsonl")
    journal.parent.mkdir(parents=True)
    journal.write_text(journal_line(1) + "\n", encoding="utf-8")
    return {"root": tmp_path / "proj", "config": str(tmp_path / "claude"), "journal": journal}


def make(env, owner="owner1", newline="\n"):
    folder = env["root"] / "daily" / "2026" / "20261114-130000_demo"
    folder.mkdir(parents=True)
    fields = {"schema_version": 1, "id": folder.name, "project": "proj", "goal": "G", "value": "V",
              "created": "2026-11-14T13:00:00+05:00", "owner": owner, "result_state": "prepared"}
    text = "# Daily Task\n\n### Economics\n\n" + close_mod.binding_line(fields) + "\n\n## 5. Next or close\n"
    record = folder / "task.md"
    record.write_bytes(text.replace("\n", newline).encode("utf-8"))
    return record


def close(env, record, *extra, session=SID):
    return close_mod.main(["--record", str(record), "--session-id", session,
                           "--config-root", env["config"]] + list(extra))


def test_collects_receives_and_chains_revisions(env, capsys):
    record = make(env)
    assert close(env, record, "--write") == 0
    line1 = capsys.readouterr().out.strip()
    assert line1.startswith("Revision 1: lines `[0, 1)`, `--complete`, cutoff ")
    assert "model `claude-opus-5-5`, 1 responses: 135 tokens — cache read 100, cache write 1 h 5, " \
           "fresh 10, output 20." in line1
    with env["journal"].open("a", encoding="utf-8") as handle:
        handle.write(journal_line(2) + "\n")
    assert close(env, record, "--write", "--state", "accepted") == 0
    line2 = capsys.readouterr().out.strip()
    assert line2.startswith("Revision 2 (covers revision 1, do not add): lines `[0, 2)`")
    received = close_mod.received_files(close_mod.load_helper(), record.parent)
    first, second = sorted(received, key=lambda i: i["manifest"]["revision"])
    assert second["manifest"]["predecessor_sha256"] == first["sha256"]
    assert second["manifest"]["source_version"] == "2.1.323"
    text = record.read_text(encoding="utf-8")
    assert line1 in text and line2 in text and text.index(line2) < text.index("<!-- tfw-economics")
    assert close_mod.read_binding(record)["result_state"] == "accepted"
    assert not (Path(tempfile.gettempdir()) / "tfw").exists()


def test_failed_collect_becomes_a_received_failure_receipt(env, capsys):
    record = make(env)
    env["journal"].write_text(journal_line(1) + "\n" + journal_line(2, session="other") + "\n", encoding="utf-8")
    assert close(env, record, "--write") == 3
    line = capsys.readouterr().out.strip()
    assert line.startswith("Revision 1 failed, unmeasured: attempted lines `[0, 2)`, code `collect_failed`")
    assert "no earlier good revision" in line
    received = close_mod.received_files(close_mod.load_helper(), record.parent)
    assert len(received) == 1 and close_mod.is_failure(received[0])


def test_unfound_source_is_a_binding_gap_written_once(env, capsys):
    record = make(env)
    for _ in range(2):
        assert close(env, record, "--write", session="absent") == 3
    assert "Binding gap `source_not_found`" in capsys.readouterr().out
    assert [g["code"] for g in close_mod.read_binding(record)["binding_outcomes"]] == ["source_not_found"]
    assert record.read_text(encoding="utf-8").count("Binding gap `source_not_found`") == 1
    assert not (record.parent / "economics").exists()


def test_unknown_owner_collects_nothing(env, capsys):
    record = make(env, owner=None)
    assert close(env, record) == 3
    assert "Binding gap `owner_unknown`" in capsys.readouterr().out
    assert not (record.parent / "economics").exists()


def test_unknown_range_is_a_gap_not_an_invented_end(env, capsys):
    record = make(env)
    assert close(env, record, "--start", "5") == 3
    assert "Binding gap `range_unknown`" in capsys.readouterr().out
    gap = close_mod.read_binding(record)["binding_outcomes"][0]
    assert gap["known"]["range_start"] == 5 and "range_end" in gap["unavailable"]


def test_glob_session_id_is_refused(env):
    record = make(env)
    assert close(env, record, session="*") == 3
    assert [g["code"] for g in close_mod.read_binding(record)["binding_outcomes"]] == ["session_invalid"]


def test_exit_2_writes_nothing(env):
    record = make(env)
    before = record.read_bytes()
    assert close_mod.main(["--record", str(record), "--state", "checked", "--source", "x"]) == 2
    assert record.read_bytes() == before


def test_record_writes_keep_crlf(env):
    record = make(env, newline="\r\n")
    assert close(env, record, "--write", "--state", "checked") == 0
    raw = record.read_bytes()
    assert raw.count(b"\n") == raw.count(b"\r\n") and b".\r\n\r\n<!-- tfw-economics" in raw
