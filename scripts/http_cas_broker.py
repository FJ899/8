from __future__ import annotations

import argparse
import json
import os
import socket
import struct
import uuid
from pathlib import Path

from agency_kernel.bindings import CapabilityBinding, TrustedBindingRegistry
from agency_kernel.g1 import (
    ActionRequest,
    AuthenticationContext,
    AuthorityGrant,
    AuthorityRoot,
    EffectContract,
    EffectIntent,
    Principal,
)
from agency_kernel.g2 import Capability
from agency_kernel.http_cas import HttpCasEffectAdapter, Kernel
from agency_kernel.http_cas_provider import HttpCasObserver
from agency_kernel.http_cas_types import HttpCasOperation
from agency_kernel.runtime import KernelRuntime


_MAX_REQUEST = 1_000_000


def recv_json(conn: socket.socket) -> dict:
    data = b""
    while not data.endswith(b"\n"):
        chunk = conn.recv(65536)
        if not chunk:
            break
        data += chunk
        if len(data) > _MAX_REQUEST:
            raise ValueError("request_too_large")
    payload = json.loads(data.decode("utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("request_not_object")
    return payload


def send_json(conn: socket.socket, payload: dict) -> None:
    conn.sendall(json.dumps(payload, sort_keys=True).encode("utf-8") + b"\n")


def peer_uid(conn: socket.socket) -> int:
    raw = conn.getsockopt(socket.SOL_SOCKET, socket.SO_PEERCRED, struct.calcsize("3i"))
    _pid, uid, _gid = struct.unpack("3i", raw)
    return uid


def read_credential(path: str | Path) -> str:
    token = Path(path).read_text(encoding="utf-8").strip()
    if not token:
        raise ValueError("empty_provider_credential")
    return token


def _response(trace, peer: int) -> dict:
    payload: dict = {
        "peer_uid": peer,
        "request_id": trace.request_id,
        "authorization_allowed": bool(trace.authorization.allowed),
        "authorization_reason": trace.authorization.reason,
    }
    if not trace.authorization.allowed:
        payload["stage"] = "authorize"
        return payload

    authorization = trace.authorization.authorization
    if authorization is not None:
        payload["principal_id"] = authorization.principal_id
        payload["intent_id"] = authorization.intent_id
        payload["authorization_id"] = authorization.authorization_id

    if trace.binding is None:
        payload["stage"] = "binding"
        payload["binding_allowed"] = False
        payload["binding_reason"] = "binding_result_absent"
        return payload
    payload["binding_allowed"] = bool(trace.binding.allowed)
    payload["binding_reason"] = trace.binding.reason
    if trace.binding.binding is not None:
        payload["binding_id"] = trace.binding.binding.binding_id
        payload["bound_capability_id"] = trace.binding.binding.capability_id
        payload["bound_target_identity"] = trace.binding.binding.target_identity
    if not trace.binding.allowed:
        payload["stage"] = "binding"
        return payload

    if trace.start is None:
        payload["stage"] = "start"
        payload["start_allowed"] = False
        payload["start_reason"] = "start_result_absent"
        return payload
    payload["start_allowed"] = bool(trace.start.allowed)
    payload["start_reason"] = trace.start.reason
    if trace.start.attempt is not None:
        payload["attempt_id"] = trace.start.attempt.attempt_id
    if not trace.start.allowed:
        payload["stage"] = "start"
        return payload

    if trace.admission is None:
        payload["stage"] = "admission"
        payload["admission_allowed"] = False
        payload["admission_reason"] = "admission_result_absent"
        return payload
    payload["admission_allowed"] = bool(trace.admission.allowed)
    payload["admission_reason"] = trace.admission.reason
    if trace.admission.admission is not None:
        admission = trace.admission.admission
        payload["admission_id"] = admission.admission_id
        payload["operation_digest"] = admission.operation_digest
        payload["canonical_operation"] = admission.canonical_operation.decode("utf-8")
    if not trace.admission.allowed:
        payload["stage"] = "admission"
        return payload

    payload["stage"] = "execution"
    if trace.execution is None:
        payload["execution_occurred"] = False
        payload["execution_reason"] = "execution_result_absent"
        return payload
    payload["execution_occurred"] = bool(trace.execution.occurred)
    payload["execution_reason"] = trace.execution.reason
    payload["provider_status"] = trace.execution.provider_status
    payload["mutation_id"] = trace.execution.mutation_id
    payload["before_version"] = trace.execution.before_version
    payload["after_version"] = trace.execution.after_version
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--socket", required=True)
    parser.add_argument("--ledger", required=True)
    parser.add_argument("--provider-endpoint", required=True)
    parser.add_argument("--credential-file", required=True)
    parser.add_argument("--provider-id", required=True)
    parser.add_argument("--authorized-uid", required=True, type=int)
    parser.add_argument("--ready-file", required=True)
    args = parser.parse_args()

    os.umask(0o077)
    token = read_credential(args.credential_file)
    kernel = Kernel(
        args.ledger,
        args.provider_endpoint,
        token,
        args.provider_id,
        clock=lambda: 100,
        timeout=1.0,
    )

    root = AuthorityRoot("p7-http-root")
    principal = Principal("alice")
    context = AuthenticationContext(f"unix-peer-uid:{args.authorized_uid}")
    intent = EffectIntent("p7.http.cas.write", "P7 HTTP CAS protected write")
    contract = EffectContract("p7.http.cas.contract-X", intent.intent_id)
    capability_id = "p7-http-cap-X"

    kernel.add_authority_root(root)
    kernel.add_principal(principal)
    kernel.establish_authentication_context(context, principal)
    kernel.add_effect_intent(intent)
    kernel.add_effect_contract(contract)
    kernel.add_authority_grant(
        AuthorityGrant(
            "p7-http-grant-alice",
            root.root_id,
            principal.principal_id,
            intent.intent_id,
        )
    )
    kernel.add_capability(Capability(capability_id, "X"))
    kernel.set_authorized_effect_envelope(
        contract.contract_id,
        kernel.possible_effects_for("X"),
    )

    observer = HttpCasObserver(args.provider_endpoint, token, args.provider_id, timeout=1.0)
    adapter = HttpCasEffectAdapter(kernel, observer)
    registry = TrustedBindingRegistry(
        (
            CapabilityBinding(
                "p7-http-binding-X",
                intent.intent_id,
                capability_id,
                "X",
                adapter,
            ),
        )
    )
    runtime = KernelRuntime(kernel, registry)

    socket_path = Path(args.socket)
    socket_path.parent.mkdir(parents=True, exist_ok=True)
    if socket_path.exists():
        socket_path.unlink()
    listener = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    listener.bind(str(socket_path))
    os.chmod(socket_path, 0o666)
    listener.listen(16)
    Path(args.ready_file).write_text(str(os.getpid()), encoding="utf-8")

    try:
        while True:
            conn, _ = listener.accept()
            with conn:
                uid = peer_uid(conn)
                try:
                    request = recv_json(conn)
                except Exception as exc:
                    send_json(
                        conn,
                        {
                            "stage": "request",
                            "request_valid": False,
                            "reason": "malformed_request",
                            "detail": type(exc).__name__,
                            "peer_uid": uid,
                        },
                    )
                    continue

                if request.get("action") == "shutdown" and uid == os.getuid():
                    send_json(conn, {"stage": "shutdown", "shutdown": True, "peer_uid": uid})
                    break
                if request.get("action") != "mutate":
                    send_json(
                        conn,
                        {
                            "stage": "request",
                            "request_valid": False,
                            "reason": "unknown_action",
                            "peer_uid": uid,
                        },
                    )
                    continue

                effects_raw = request.get("possible_effects")
                if effects_raw is None:
                    effects = None
                elif isinstance(effects_raw, list) and all(isinstance(item, str) for item in effects_raw):
                    effects = frozenset(effects_raw)
                else:
                    send_json(
                        conn,
                        {
                            "stage": "request",
                            "request_valid": False,
                            "reason": "invalid_possible_effects",
                            "peer_uid": uid,
                        },
                    )
                    continue

                action_request = ActionRequest(
                    f"p7-http-request-{uuid.uuid4()}",
                    intent.intent_id,
                    contract.contract_id,
                    declared_principal=request.get("declared_principal"),
                    untrusted_authority=request.get("untrusted_authority"),
                )
                operation = HttpCasOperation(
                    request.get("resource", ""),
                    request.get("expected_version", -1),
                    request.get("new_value", ""),
                    effects,
                )
                trusted_context = context if uid == args.authorized_uid else None
                trace = runtime.run(
                    action_request,
                    operation,
                    authentication_context=trusted_context,
                )
                send_json(conn, _response(trace, uid))
    finally:
        listener.close()
        try:
            socket_path.unlink()
        except FileNotFoundError:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
