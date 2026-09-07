from __future__ import annotations

import argparse
import json
import socket
import sys


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--socket", required=True)
    parser.add_argument("--request", required=True)
    args = parser.parse_args()

    payload = json.loads(args.request)
    conn = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    conn.connect(args.socket)
    conn.sendall(json.dumps(payload, sort_keys=True).encode("utf-8") + b"\n")
    data = b""
    while not data.endswith(b"\n"):
        chunk = conn.recv(65536)
        if not chunk:
            break
        data += chunk
    conn.close()
    sys.stdout.write(data.decode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
