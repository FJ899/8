from __future__ import annotations

import argparse
import json
import os
from http.server import ThreadingHTTPServer
from pathlib import Path

from agency_kernel.http_cas_provider import (
    _make_handler,
    initialize_http_cas_provider,
    seed_http_cas_resource,
)


def read_credential(path: str | Path) -> str:
    token = Path(path).read_text(encoding="utf-8").strip()
    if not token:
        raise ValueError("empty_provider_credential")
    return token


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", required=True)
    parser.add_argument("--credential-file", required=True)
    parser.add_argument("--provider-id", required=True)
    parser.add_argument("--ready-file", required=True)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=0)
    parser.add_argument("--seed-resource", default="X")
    parser.add_argument("--seed-value", default="initial")
    parser.add_argument("--seed-version", type=int, default=0)
    args = parser.parse_args()

    if args.host != "127.0.0.1":
        raise ValueError("provider_host_must_be_loopback")
    os.umask(0o077)
    token = read_credential(args.credential_file)
    initialize_http_cas_provider(args.db, args.provider_id)
    seed_http_cas_resource(args.db, args.seed_resource, args.seed_value, args.seed_version)

    server = ThreadingHTTPServer(
        (args.host, args.port),
        _make_handler(args.db, token, False),
    )
    ready = Path(args.ready_file)
    ready.write_text(
        json.dumps(
            {
                "pid": os.getpid(),
                "port": int(server.server_address[1]),
                "provider_id": args.provider_id,
            },
            sort_keys=True,
        ),
        encoding="utf-8",
    )
    try:
        server.serve_forever(poll_interval=0.05)
    finally:
        server.server_close()
        try:
            ready.unlink()
        except FileNotFoundError:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
