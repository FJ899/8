from __future__ import annotations

import hmac
import json
import os
import socket
import sqlite3
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Optional

from .http_cas_types import (
    HttpCasObservation,
    HttpCasReceipt,
    decode_http_operation_payload,
    validate_loopback_endpoint,
)
from .target_instance import (
    HistoricalTargetBinding,
    filesystem_fd_target_instance_id,
    filesystem_target_instance_id,
)

_MAX_BODY = 65536


def _connect(path: str | Path) -> sqlite3.Connection:
    c = sqlite3.connect(str(path), timeout=30.0, isolation_level=None)
    c.row_factory = sqlite3.Row
    c.execute("PRAGMA journal_mode=WAL")
    c.execute("PRAGMA synchronous=FULL")
    c.execute("PRAGMA busy_timeout=30000")
    return c


def initialize_http_cas_provider(path: str | Path, provider_id: str) -> None:
    if not isinstance(provider_id, str) or not provider_id:
        raise ValueError("invalid_provider_id")
    with _connect(path) as c:
        c.executescript(
            """
            CREATE TABLE IF NOT EXISTS provider_metadata (
                provider_id TEXT PRIMARY KEY
            );
            CREATE TABLE IF NOT EXISTS resources (
                resource TEXT PRIMARY KEY,
                value TEXT NOT NULL,
                version INTEGER NOT NULL,
                last_admission_id TEXT NULL,
                last_operation_digest TEXT NULL,
                last_mutation_id TEXT NULL
            );
            CREATE TABLE IF NOT EXISTS receipts (
                admission_id TEXT PRIMARY KEY,
                operation_digest TEXT NOT NULL,
                resource TEXT NOT NULL,
                expected_version INTEGER NOT NULL,
                new_value TEXT NOT NULL,
                status TEXT NOT NULL CHECK(status IN ('committed', 'rejected_stale')),
                mutation_id TEXT NULL,
                before_version INTEGER NULL,
                after_version INTEGER NULL,
                created_at INTEGER NOT NULL
            );
            """
        )
        rows = c.execute("SELECT provider_id FROM provider_metadata").fetchall()
        if not rows:
            c.execute("INSERT INTO provider_metadata(provider_id) VALUES (?)", (provider_id,))
        elif len(rows) != 1 or str(rows[0]["provider_id"]) != provider_id:
            raise RuntimeError("provider_identity_mismatch")


def seed_http_cas_resource(path: str | Path, resource: str, value: str, version: int = 0) -> None:
    with _connect(path) as c:
        c.execute(
            """
            INSERT INTO resources(resource, value, version, last_admission_id, last_operation_digest, last_mutation_id)
            VALUES (?, ?, ?, NULL, NULL, NULL)
            ON CONFLICT(resource) DO UPDATE SET
                value = excluded.value,
                version = excluded.version,
                last_admission_id = NULL,
                last_operation_digest = NULL,
                last_mutation_id = NULL
            """,
            (resource, value, version),
        )


def inject_unattributed_http_cas_change_for_test(path: str | Path, resource: str, value: str, version: int) -> None:
    seed_http_cas_resource(path, resource, value, version)


def inject_committed_receipt_without_state_for_test(
    path: str | Path,
    *,
    admission_id: str,
    operation_digest: str,
    resource: str,
    expected_version: int,
    new_value: str,
) -> None:
    with _connect(path) as c:
        c.execute(
            """
            INSERT OR REPLACE INTO receipts(
                admission_id, operation_digest, resource, expected_version, new_value,
                status, mutation_id, before_version, after_version, created_at
            ) VALUES (?, ?, ?, ?, ?, 'committed', ?, ?, ?, ?)
            """,
            (
                admission_id,
                operation_digest,
                resource,
                expected_version,
                new_value,
                str(uuid.uuid4()),
                expected_version,
                expected_version + 1,
                int(time.time()),
            ),
        )


def read_http_cas_resource_for_test(path: str | Path, resource: str) -> tuple[Optional[str], Optional[int]]:
    with _connect(path) as c:
        row = c.execute("SELECT value, version FROM resources WHERE resource = ?", (resource,)).fetchone()
    if row is None:
        return None, None
    return str(row["value"]), int(row["version"])


def _provider_id(path: str | Path) -> str:
    with _connect(path) as c:
        row = c.execute("SELECT provider_id FROM provider_metadata").fetchone()
    if row is None:
        raise RuntimeError("provider_identity_absent")
    return str(row["provider_id"])


def _provider_target_instance_id(path: str | Path, provider_id: str) -> str:
    return filesystem_target_instance_id(
        path,
        namespace=f"http-cas-provider-store:{provider_id}",
    )


def _receipt_payload(row: sqlite3.Row, provider_id: str) -> dict[str, Any]:
    return {
        "provider_id": provider_id,
        "admission_id": str(row["admission_id"]),
        "operation_digest": str(row["operation_digest"]),
        "resource": str(row["resource"]),
        "expected_version": int(row["expected_version"]),
        "new_value": str(row["new_value"]),
        "status": str(row["status"]),
        "mutation_id": None if row["mutation_id"] is None else str(row["mutation_id"]),
        "before_version": None if row["before_version"] is None else int(row["before_version"]),
        "after_version": None if row["after_version"] is None else int(row["after_version"]),
    }


def _apply_provider_cas(
    path: str | Path,
    admission_id: str,
    operation_digest: str,
    op,
    *,
    expected_target_instance_id: Optional[str] = None,
) -> dict[str, Any]:
    """Apply CAS to the same concrete provider-store object that is validated.

    Bound P9-R5 requests open the DB object first, validate its fstat identity,
    and then run SQLite through `/proc/self/fd/N` while the descriptor remains
    open. Raw legacy requests keep the historical pathname behavior.
    """

    pinned_fd: Optional[int] = None
    effect_path = str(path)
    try:
        if expected_target_instance_id is not None:
            pinned_fd = os.open(effect_path, os.O_RDWR)
            effect_path = f"/proc/self/fd/{pinned_fd}"
            provider_id = _provider_id(effect_path)
            current_target_instance_id = filesystem_fd_target_instance_id(
                pinned_fd,
                namespace=f"http-cas-provider-store:{provider_id}",
            )
            if current_target_instance_id != expected_target_instance_id:
                raise RuntimeError("target_instance_mismatch")
        else:
            provider_id = _provider_id(effect_path)

        c = _connect(effect_path)
        try:
            c.execute("BEGIN IMMEDIATE")
            existing = c.execute(
                "SELECT * FROM receipts WHERE admission_id = ?",
                (admission_id,),
            ).fetchone()
            if existing is not None:
                if (
                    str(existing["operation_digest"]) != operation_digest
                    or str(existing["resource"]) != op.resource
                    or int(existing["expected_version"]) != op.expected_version
                    or str(existing["new_value"]) != op.new_value
                ):
                    c.execute("ROLLBACK")
                    raise ValueError("idempotency_conflict")
                c.execute("COMMIT")
                return _receipt_payload(existing, provider_id)

            current = c.execute(
                "SELECT value, version FROM resources WHERE resource = ?",
                (op.resource,),
            ).fetchone()
            before = 0 if current is None else int(current["version"])
            if before != op.expected_version:
                c.execute(
                    """
                    INSERT INTO receipts(
                        admission_id, operation_digest, resource, expected_version, new_value,
                        status, mutation_id, before_version, after_version, created_at
                    ) VALUES (?, ?, ?, ?, ?, 'rejected_stale', NULL, ?, ?, ?)
                    """,
                    (
                        admission_id,
                        operation_digest,
                        op.resource,
                        op.expected_version,
                        op.new_value,
                        before,
                        before,
                        int(time.time()),
                    ),
                )
                c.execute("COMMIT")
                row = c.execute(
                    "SELECT * FROM receipts WHERE admission_id = ?",
                    (admission_id,),
                ).fetchone()
                assert row is not None
                return _receipt_payload(row, provider_id)

            after = before + 1
            mutation_id = str(uuid.uuid4())
            if current is None:
                c.execute(
                    """
                    INSERT INTO resources(
                        resource, value, version, last_admission_id, last_operation_digest, last_mutation_id
                    ) VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (op.resource, op.new_value, after, admission_id, operation_digest, mutation_id),
                )
            else:
                cur = c.execute(
                    """
                    UPDATE resources
                    SET value = ?, version = ?, last_admission_id = ?,
                        last_operation_digest = ?, last_mutation_id = ?
                    WHERE resource = ? AND version = ?
                    """,
                    (
                        op.new_value,
                        after,
                        admission_id,
                        operation_digest,
                        mutation_id,
                        op.resource,
                        before,
                    ),
                )
                if cur.rowcount != 1:
                    c.execute("ROLLBACK")
                    raise RuntimeError("provider_cas_race")
            c.execute(
                """
                INSERT INTO receipts(
                    admission_id, operation_digest, resource, expected_version, new_value,
                    status, mutation_id, before_version, after_version, created_at
                ) VALUES (?, ?, ?, ?, ?, 'committed', ?, ?, ?, ?)
                """,
                (
                    admission_id,
                    operation_digest,
                    op.resource,
                    op.expected_version,
                    op.new_value,
                    mutation_id,
                    before,
                    after,
                    int(time.time()),
                ),
            )
            c.execute("COMMIT")
            row = c.execute(
                "SELECT * FROM receipts WHERE admission_id = ?",
                (admission_id,),
            ).fetchone()
            assert row is not None
            return _receipt_payload(row, provider_id)
        except BaseException:
            if c.in_transaction:
                c.execute("ROLLBACK")
            raise
        finally:
            c.close()
    finally:
        if pinned_fd is not None:
            os.close(pinned_fd)


def _make_handler(path: str | Path, token: str, allow_test_faults: bool):
    db_path = str(path)
    expected_token = token.encode("utf-8")

    class Handler(BaseHTTPRequestHandler):
        server_version = "AgencyKernelHttpCas/1"

        def log_message(self, fmt: str, *args: Any) -> None:
            return

        def _authorized(self) -> bool:
            value = self.headers.get("Authorization", "")
            return hmac.compare_digest(value.encode("utf-8"), b"Bearer " + expected_token)

        def _json(self, status: int, payload: dict[str, Any]) -> None:
            body = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            try:
                self.wfile.write(body)
            except (BrokenPipeError, ConnectionResetError):
                pass

        def do_POST(self) -> None:
            if self.path != "/cas":
                self._json(404, {"error": "not_found"})
                return
            if not self._authorized():
                self._json(401, {"error": "unauthorized"})
                return
            try:
                length = int(self.headers.get("Content-Length", "0"))
            except ValueError:
                self._json(400, {"error": "invalid_length"})
                return
            if length <= 0 or length > _MAX_BODY:
                self._json(400, {"error": "invalid_length"})
                return
            try:
                payload = json.loads(self.rfile.read(length).decode("utf-8"))
                base_keys = {"admission_id", "operation_digest", "operation"}
                if set(payload) not in (base_keys, base_keys | {"expected_target_instance_id"}):
                    raise ValueError("invalid_request")
                admission_id = str(payload["admission_id"])
                operation_digest = str(payload["operation_digest"])
                op = decode_http_operation_payload(payload["operation"])
                expected_target_instance_id = payload.get("expected_target_instance_id")
                if expected_target_instance_id is not None and (
                    not isinstance(expected_target_instance_id, str)
                    or not expected_target_instance_id
                ):
                    raise ValueError("invalid_target_instance")
                if not admission_id or op.operation_digest != operation_digest:
                    raise ValueError("digest_mismatch")
            except (KeyError, TypeError, ValueError, UnicodeDecodeError, json.JSONDecodeError):
                self._json(400, {"error": "invalid_request"})
                return

            # P9-R4 early check remains useful for prompt rejection. P9-R5's
            # definitive check is inside _apply_provider_cas after opening the
            # object that the SQLite transaction will itself use.
            provider_id = _provider_id(db_path)
            if expected_target_instance_id is not None:
                current_target_instance_id = _provider_target_instance_id(db_path, provider_id)
                if current_target_instance_id != expected_target_instance_id:
                    self._json(
                        409,
                        {
                            "error": "target_instance_mismatch",
                            "provider_id": provider_id,
                        },
                    )
                    return

            fault = self.headers.get("X-Agency-Kernel-Test-Fault", "") if allow_test_faults else ""
            if fault == "delay_before_commit":
                time.sleep(0.35)
            if fault == "drop_before_decision":
                try:
                    self.connection.shutdown(socket.SHUT_RDWR)
                except OSError:
                    pass
                self.connection.close()
                return
            if fault == "forge_success_without_commit":
                self._json(
                    200,
                    {
                        "provider_id": provider_id,
                        "admission_id": admission_id,
                        "operation_digest": operation_digest,
                        "resource": op.resource,
                        "expected_version": op.expected_version,
                        "new_value": op.new_value,
                        "status": "committed",
                        "mutation_id": "forged-response-only",
                        "before_version": op.expected_version,
                        "after_version": op.expected_version + 1,
                    },
                )
                return
            try:
                receipt = _apply_provider_cas(
                    db_path,
                    admission_id,
                    operation_digest,
                    op,
                    expected_target_instance_id=expected_target_instance_id,
                )
            except ValueError:
                self._json(409, {"error": "idempotency_conflict"})
                return
            except RuntimeError as exc:
                if str(exc) == "target_instance_mismatch":
                    self._json(
                        409,
                        {
                            "error": "target_instance_mismatch",
                            "provider_id": provider_id,
                        },
                    )
                else:
                    self._json(409, {"error": "provider_conflict"})
                return
            if fault == "response_lost_after_commit":
                try:
                    self.connection.shutdown(socket.SHUT_RDWR)
                except OSError:
                    pass
                self.connection.close()
                return
            if fault == "delay_after_commit":
                time.sleep(0.35)
            self._json(200 if receipt["status"] == "committed" else 412, receipt)

        def do_GET(self) -> None:
            if not self._authorized():
                self._json(401, {"error": "unauthorized"})
                return
            try:
                parsed = urllib.parse.urlparse(self.path)
                query = urllib.parse.parse_qs(parsed.query, strict_parsing=True)
            except ValueError:
                self._json(400, {"error": "invalid_query"})
                return
            provider_id = _provider_id(db_path)
            if parsed.path == "/identity":
                self._json(
                    200,
                    {
                        "provider_id": provider_id,
                        "target_kind": "http-cas-provider-store",
                        "target_instance_id": _provider_target_instance_id(db_path, provider_id),
                    },
                )
                return
            if parsed.path == "/state":
                values = query.get("resource", [])
                if len(values) != 1:
                    self._json(400, {"error": "invalid_query"})
                    return
                resource = values[0]
                with _connect(db_path) as c:
                    row = c.execute(
                        """
                        SELECT value, version, last_admission_id, last_operation_digest, last_mutation_id
                        FROM resources WHERE resource = ?
                        """,
                        (resource,),
                    ).fetchone()
                if row is None:
                    self._json(
                        200,
                        {
                            "provider_id": provider_id,
                            "resource": resource,
                            "value": None,
                            "version": None,
                            "admission_id": None,
                            "operation_digest": None,
                            "mutation_id": None,
                        },
                    )
                    return
                self._json(
                    200,
                    {
                        "provider_id": provider_id,
                        "resource": resource,
                        "value": str(row["value"]),
                        "version": int(row["version"]),
                        "admission_id": None
                        if row["last_admission_id"] is None
                        else str(row["last_admission_id"]),
                        "operation_digest": None
                        if row["last_operation_digest"] is None
                        else str(row["last_operation_digest"]),
                        "mutation_id": None
                        if row["last_mutation_id"] is None
                        else str(row["last_mutation_id"]),
                    },
                )
                return
            if parsed.path == "/receipt":
                ids = query.get("admission_id", [])
                if len(ids) != 1:
                    self._json(400, {"error": "invalid_query"})
                    return
                with _connect(db_path) as c:
                    row = c.execute(
                        "SELECT * FROM receipts WHERE admission_id = ?",
                        (ids[0],),
                    ).fetchone()
                if row is None:
                    self._json(404, {"error": "receipt_absent"})
                    return
                self._json(200, _receipt_payload(row, provider_id))
                return
            self._json(404, {"error": "not_found"})

    return Handler


def serve_http_cas_provider(
    path: str | Path,
    token: str,
    provider_id: str,
    ready_connection=None,
    *,
    host: str = "127.0.0.1",
    port: int = 0,
    allow_test_faults: bool = False,
) -> None:
    if not isinstance(token, str) or not token:
        raise ValueError("invalid_provider_token")
    if host not in {"127.0.0.1", "localhost"}:
        raise ValueError("provider_host_must_be_loopback")
    initialize_http_cas_provider(path, provider_id)
    server = ThreadingHTTPServer((host, port), _make_handler(path, token, allow_test_faults))
    if ready_connection is not None:
        ready_connection.send(int(server.server_address[1]))
        ready_connection.close()
    try:
        server.serve_forever(poll_interval=0.05)
    finally:
        server.server_close()


class HttpCasObserver:
    __slots__ = ("_endpoint", "_token", "_provider_id", "_timeout")

    def __init__(self, endpoint: str, token: str, provider_id: str, *, timeout: float = 0.2) -> None:
        self._endpoint = validate_loopback_endpoint(endpoint)
        self._token = token
        self._provider_id = provider_id
        self._timeout = timeout

    def _get(self, path: str) -> dict[str, Any]:
        req = urllib.request.Request(
            self._endpoint + path,
            headers={"Authorization": "Bearer " + self._token},
            method="GET",
        )
        with urllib.request.urlopen(req, timeout=self._timeout) as response:
            payload = json.loads(response.read(_MAX_BODY).decode("utf-8"))
        if payload.get("provider_id") != self._provider_id:
            raise RuntimeError("provider_identity_mismatch")
        return payload

    def historical_target_binding(self, resource: str) -> HistoricalTargetBinding:
        payload = self._get("/identity")
        if payload.get("target_kind") != "http-cas-provider-store":
            raise RuntimeError("provider_target_kind_mismatch")
        instance_id = payload.get("target_instance_id")
        if not isinstance(instance_id, str) or not instance_id:
            raise RuntimeError("provider_target_instance_absent")
        return HistoricalTargetBinding(
            "http-cas-provider-store",
            resource,
            instance_id,
        )

    def receipt(self, admission_id: str) -> Optional[HttpCasReceipt]:
        try:
            payload = self._get(
                "/receipt?" + urllib.parse.urlencode({"admission_id": admission_id})
            )
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            raise
        return HttpCasReceipt(
            provider_id=str(payload["provider_id"]),
            admission_id=str(payload["admission_id"]),
            operation_digest=str(payload["operation_digest"]),
            resource=str(payload["resource"]),
            expected_version=int(payload["expected_version"]),
            new_value=str(payload["new_value"]),
            status=str(payload["status"]),
            mutation_id=None
            if payload["mutation_id"] is None
            else str(payload["mutation_id"]),
            before_version=None
            if payload["before_version"] is None
            else int(payload["before_version"]),
            after_version=None
            if payload["after_version"] is None
            else int(payload["after_version"]),
        )

    def observe(
        self,
        resource: str,
        *,
        covered: bool = True,
        attribution_ambiguous: bool = False,
    ) -> HttpCasObservation:
        payload = self._get(
            "/state?" + urllib.parse.urlencode({"resource": resource})
        )
        admission_id = (
            None if payload["admission_id"] is None else str(payload["admission_id"])
        )
        receipt = None if admission_id is None else self.receipt(admission_id)
        return HttpCasObservation(
            provider_id=str(payload["provider_id"]),
            resource=str(payload["resource"]),
            value=None if payload["value"] is None else str(payload["value"]),
            version=None if payload["version"] is None else int(payload["version"]),
            admission_id=admission_id,
            operation_digest=None
            if payload["operation_digest"] is None
            else str(payload["operation_digest"]),
            mutation_id=None
            if payload["mutation_id"] is None
            else str(payload["mutation_id"]),
            receipt_status=None if receipt is None else receipt.status,
            receipt_mutation_id=None if receipt is None else receipt.mutation_id,
            receipt_after_version=None if receipt is None else receipt.after_version,
            receipt_value=None if receipt is None else receipt.new_value,
            covered=covered,
            attribution_ambiguous=attribution_ambiguous,
        )
