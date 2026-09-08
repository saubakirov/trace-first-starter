from __future__ import annotations

import os
import selectors
import socket
import threading
from pathlib import Path


ROUTES = {
    3128: Path("/run/tfw/proxy/claude.sock"),
    3129: Path("/run/tfw/proxy/codex.sock"),
}


def _tunnel(left: socket.socket, right: socket.socket) -> None:
    selector = selectors.DefaultSelector()
    selector.register(left, selectors.EVENT_READ, right)
    selector.register(right, selectors.EVENT_READ, left)
    try:
        while True:
            events = selector.select(timeout=1)
            for key, _ in events:
                payload = key.fileobj.recv(65536)
                if not payload:
                    return
                key.data.sendall(payload)
    finally:
        selector.close()


def _handle(client: socket.socket, upstream_path: Path) -> None:
    with client:
        try:
            upstream = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            upstream.connect(str(upstream_path))
        except OSError:
            return
        with upstream:
            _tunnel(client, upstream)


def _serve(port: int, path: Path) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("127.0.0.1", port))
        server.listen(16)
        while True:
            client, _ = server.accept()
            threading.Thread(target=_handle, args=(client, path), daemon=True).start()


def main() -> None:
    for port, path in ROUTES.items():
        threading.Thread(target=_serve, args=(port, path), daemon=True).start()
    threading.Event().wait()


if __name__ == "__main__":
    main()
