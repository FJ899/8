from __future__ import annotations

import hashlib
import json
import urllib.parse
from dataclasses import dataclass
from typing import FrozenSet, Optional


@dataclass(frozen=True)
class HttpCasOperation:
    resource: str
    expected_version: int
    new_value: str
    possible_effects: Optional[FrozenSet[str]]

    def canonical_bytes(self) -> bytes:
        if not isinstance(self.resource, str) or not self.resource:
            raise ValueError("invalid_resource")
        if any(ch in self.resource for ch in ("/", "\\", "?", "#")) or self.resource in {".", ".."}:
            raise ValueError("invalid_resource")
        if isinstance(self.expected_version, bool) or not isinstance(self.expected_version, int) or self.expected_version < 0:
            raise ValueError("invalid_expected_version")
        if not isinstance(self.new_value, str):
            raise ValueError("invalid_value")
        effects = None if self.possible_effects is None else sorted(self.possible_effects)
        payload = {
            "expected_version": self.expected_version,
            "new_value": self.new_value,
            "operation_type": "http_cas_put",
            "possible_effects": effects,
            "resource": self.resource,
        }
        return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

    @property
    def operation_digest(self) -> str:
        return hashlib.sha256(self.canonical_bytes()).hexdigest()


@dataclass(frozen=True)
class HttpCasExecutionResult:
    occurred: bool
    reason: str
    resource: str
    operation_digest: Optional[str] = None
    provider_status: Optional[str] = None
    mutation_id: Optional[str] = None
    before_version: Optional[int] = None
    after_version: Optional[int] = None


@dataclass(frozen=True)
class HttpCasReceipt:
    provider_id: str
    admission_id: str
    operation_digest: str
    resource: str
    expected_version: int
    new_value: str
    status: str
    mutation_id: Optional[str]
    before_version: Optional[int]
    after_version: Optional[int]


@dataclass(frozen=True)
class HttpCasObservation:
    provider_id: str
    resource: str
    value: Optional[str]
    version: Optional[int]
    admission_id: Optional[str]
    operation_digest: Optional[str]
    mutation_id: Optional[str]
    receipt_status: Optional[str] = None
    receipt_mutation_id: Optional[str] = None
    receipt_after_version: Optional[int] = None
    receipt_value: Optional[str] = None
    covered: bool = True
    attribution_ambiguous: bool = False


def decode_http_operation_payload(payload) -> HttpCasOperation:
    if not isinstance(payload, dict):
        raise ValueError("invalid_operation")
    expected_keys = {"expected_version", "new_value", "operation_type", "possible_effects", "resource"}
    if set(payload) != expected_keys or payload.get("operation_type") != "http_cas_put":
        raise ValueError("invalid_operation")
    resource = payload.get("resource")
    expected_version = payload.get("expected_version")
    new_value = payload.get("new_value")
    effects_raw = payload.get("possible_effects")
    if not isinstance(resource, str) or isinstance(expected_version, bool) or not isinstance(expected_version, int):
        raise ValueError("invalid_operation")
    if not isinstance(new_value, str):
        raise ValueError("invalid_operation")
    if effects_raw is not None and (not isinstance(effects_raw, list) or not all(isinstance(x, str) for x in effects_raw)):
        raise ValueError("invalid_operation")
    effects = None if effects_raw is None else frozenset(effects_raw)
    op = HttpCasOperation(resource, expected_version, new_value, effects)
    if json.loads(op.canonical_bytes().decode("utf-8")) != payload:
        raise ValueError("noncanonical_operation")
    return op


def validate_loopback_endpoint(endpoint: str) -> str:
    if not isinstance(endpoint, str):
        raise ValueError("invalid_provider_endpoint")
    parsed = urllib.parse.urlparse(endpoint)
    if parsed.scheme != "http" or parsed.hostname not in {"127.0.0.1", "localhost"}:
        raise ValueError("provider_endpoint_must_be_loopback_http")
    if parsed.username is not None or parsed.password is not None or parsed.query or parsed.fragment or parsed.path not in {"", "/"}:
        raise ValueError("invalid_provider_endpoint")
    if parsed.port is None or parsed.port <= 0:
        raise ValueError("invalid_provider_endpoint")
    return endpoint.rstrip("/")
