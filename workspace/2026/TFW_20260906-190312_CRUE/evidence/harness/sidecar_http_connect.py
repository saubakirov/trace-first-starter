from __future__ import annotations

import json
import os
import selectors
import signal
import socket
import threading
from pathlib import Path


SOCKETS = {
    "claude": Path("/run/tfw/proxy/claude.sock"),
    "codex": Path("/run/tfw/proxy/codex.sock"),
}
POLICY = {
    "claude": {"api.anthropic.com"},
    "codex": {"chatgpt.com"},
}
stop = threading.Event()
stats_lock = threading.Lock()
stats: list[dict[str, object]] = []


def _record(**entry: object) -> None:
    with stats_lock:
        stats.append(entry)


def _read_headers(connection: socket.socket) -> bytes:
    data = bytearray()
    while b"\r\n\r\n" not in data and len(data) <= 16384:
        chunk = connection.recv(4096)
        if not chunk:
            break
        data.extend(chunk)
    return bytes(data)


def _connect_target(provider: str, request: bytes, connection: socket.socket) -> None:
    first_line = request.split(b"\r\n", 1)[0].decode("ascii", "replace")
    parts = first_line.split()
    target = parts[1] if len(parts) >= 2 and parts[0].upper() == "CONNECT" else ""
    host, separator, port_text = target.rpartition(":")
    try:
        port = int(port_text) if separator else -1
    except ValueError:
        port = -1
    allowed = host in POLICY[provider] and port == 443
    _record(provider=provider, host=host, port=port, decision="ALLOW" if allowed else "DENY")
    if not allowed:
        connection.sendall(b"HTTP/1.1 403 Forbidden\r\nContent-Length: 0\r\n\r\n")
        return
    try:
        upstream = socket.create_connection((host, port), timeout=15)
    except OSError as exc:
        _record(provider=provider, host=host, port=port, decision="UPSTREAM_ERROR", error=type(exc).__name__)
        connection.sendall(b"HTTP/1.1 502 Bad Gateway\r\nContent-Length: 0\r\n\r\n")
        return
    with upstream:
        connection.sendall(b"HTTP/1.1 200 Connection Established\r\n\r\n")
        _tunnel(connection, upstream)
        _record(provider=provider, host=host, port=port, decision="TUNNEL_CLOSED")


def _tunnel(left: socket.socket, right: socket.socket) -> None:
    selector = selectors.DefaultSelector()
    selector.register(left, selectors.EVENT_READ, right)
    selector.register(right, selectors.EVENT_READ, left)
    try:
        while not stop.is_set():
            events = selector.select(timeout=1)
            if not events:
                continue
            for key, _ in events:
                payload = key.fileobj.recv(65536)
                if not payload:
                    return
                key.data.sendall(payload)
    finally:
        selector.close()


def _serve(provider: str, ready: threading.Event) -> None:
    path = SOCKETS[provider]
    path.unlink(missing_ok=True)
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as server:
        server.bind(str(path))
        os.chmod(path, 0o600)
        server.listen(16)
        ready.set()
        while not stop.is_set():
            server.settimeout(1)
            try:
                connection, _ = server.accept()
            except socket.timeout:
                continue
            threading.Thread(target=_handle, args=(provider, connection), daemon=True).start()


def _handle(provider: str, connection: socket.socket) -> None:
    with connection:
        try:
            request = _read_headers(connection)
            if not request.endswith(b"\r\n\r\n"):
                _record(provider=provider, decision="MALFORMED")
                return
            _connect_target(provider, request, connection)
        except (OSError, UnicodeError):
            _record(provider=provider, decision="CONNECTION_ERROR")


def main() -> None:
    Path("/run/tfw/proxy").mkdir(parents=True, exist_ok=True)
    ready_events = []
    for provider in SOCKETS:
        event = threading.Event()
        ready_events.append(event)
        threading.Thread(target=_serve, args=(provider, event), daemon=True).start()
    if not all(event.wait(5) for event in ready_events):
        raise RuntimeError("proxy sockets did not become ready")

    def _stop(*_args: object) -> None:
        stop.set()

    signal.signal(signal.SIGTERM, _stop)
    signal.signal(signal.SIGINT, _stop)
    while not stop.wait(1):
        pass
    print(json.dumps({"decisions": stats}, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
