from __future__ import annotations

import json
import os
import socket
import threading
from pathlib import Path


SOCKET = Path("/run/tfw/provider-connect.sock")
POLICY = {
    "claude": {"api.anthropic.com"},
    "codex": {"api.openai.com"},
}


def _decision(request: dict[str, object]) -> dict[str, object]:
    provider = request.get("provider")
    host = request.get("host")
    port = request.get("port")
    allowed = (
        request.get("action") == "CONNECT"
        and isinstance(provider, str)
        and isinstance(host, str)
        and port == 443
        and host in POLICY.get(provider, set())
    )
    return {
        "provider": provider,
        "host": host,
        "port": port,
        "decision": "ALLOW" if allowed else "DENY",
    }


def _serve(ready: threading.Event) -> None:
    SOCKET.unlink(missing_ok=True)
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as server:
        server.bind(str(SOCKET))
        os.chmod(SOCKET, 0o600)
        server.listen(1)
        ready.set()
        for _ in range(4):
            connection, _ = server.accept()
            with connection:
                payload = connection.makefile("rwb")
                line = payload.readline()
                request = json.loads(line)
                payload.write(json.dumps(_decision(request), sort_keys=True).encode() + b"\n")
                payload.flush()


def _ask(request: dict[str, object]) -> dict[str, object]:
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
        client.connect(str(SOCKET))
        client.sendall(json.dumps(request).encode() + b"\n")
        return json.loads(client.makefile("rb").readline())


def main() -> None:
    ready = threading.Event()
    server = threading.Thread(target=_serve, args=(ready,), daemon=True)
    server.start()
    if not ready.wait(2):
        raise RuntimeError("sidecar did not become ready")

    requests = [
        {"action": "CONNECT", "provider": "claude", "host": "api.anthropic.com", "port": 443},
        {"action": "CONNECT", "provider": "claude", "host": "api.openai.com", "port": 443},
        {"action": "CONNECT", "provider": "codex", "host": "api.openai.com", "port": 443},
        {"action": "CONNECT", "provider": "codex", "host": "api.openai.com", "port": 80},
    ]
    results = [_ask(request) for request in requests]
    blocked_root = False
    try:
        Path("/blocked-root-write").write_bytes(b"must fail")
    except OSError:
        blocked_root = True
    tmpfs_write = Path("/run/tfw/probe").write_text("ok", encoding="utf-8")
    del tmpfs_write
    cap_eff = next(
        line.split(":", 1)[1].strip()
        for line in Path("/proc/self/status").read_text(encoding="utf-8").splitlines()
        if line.startswith("CapEff:")
    )
    print(json.dumps({
        "uid": os.getuid(),
        "gid": os.getgid(),
        "cap_eff": cap_eff,
        "rootfs_write_blocked": blocked_root,
        "unix_socket": str(SOCKET),
        "results": results,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
