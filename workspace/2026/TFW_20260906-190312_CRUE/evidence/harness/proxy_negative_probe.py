from __future__ import annotations

import socket


with socket.create_connection(("127.0.0.1", 3129), timeout=5) as connection:
    connection.sendall(
        b"CONNECT api.openai.com:443 HTTP/1.1\r\n"
        b"Host: api.openai.com\r\n\r\n"
    )
    print(connection.recv(128).decode("ascii", "replace"), end="")
