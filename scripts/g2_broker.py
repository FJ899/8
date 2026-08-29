from __future__ import annotations

import argparse
import json
import os
import socket
import struct
import uuid
from pathlib import Path

from agency_kernel.g1 import ActionRequest, AuthenticationContext, AuthorityGrant, AuthorityRoot, EffectContract, EffectIntent, Principal
from agency_kernel.g2 import Capability, Kernel, TechnicalOperation


def recv_json(conn: socket.socket) -> dict:
    data = b""
    while not data.endswith(b"\n"):
        chunk = conn.recv(65536)
        if not chunk:
            break
        data += chunk
        if len(data) > 1_000_000:
            raise ValueError("request_too_large")
    return json.loads(data.decode("utf-8"))


def send_json(conn: socket.socket, payload: dict) -> None:
    conn.sendall(json.dumps(payload, sort_keys=True).encode("utf-8") + b"\n")


def peer_uid(conn: socket.socket) -> int:
    raw = conn.getsockopt(socket.SOL_SOCKET, socket.SO_PEERCRED, struct.calcsize("3i"))
    _pid, uid, _gid = struct.unpack("3i", raw)
    return uid


def safe_operation_digest(operation: TechnicalOperation) -> str | None:
    try:
        return operation.operation_digest
    except (TypeError, ValueError):
        return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--socket", required=True)
    parser.add_argument("--ledger", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--authorized-uid", required=True, type=int)
    parser.add_argument("--ready-file", required=True)
    args = parser.parse_args()

    socket_path = Path(args.socket)
    socket_path.parent.mkdir(parents=True, exist_ok=True)
    if socket_path.exists():
        socket_path.unlink()

    kernel = Kernel(args.ledger, args.target, clock=lambda: 100)
    root = AuthorityRoot("g2-root")
    alice = Principal("alice")
    context = AuthenticationContext(f"unix-peer-uid:{args.authorized_uid}")
    intent = EffectIntent("g2.boundary.write", "G2 boundary mutation")
    contract = EffectContract("g2.contract.write-X", intent.intent_id)
    kernel.add_authority_root(root)
    kernel.add_principal(alice)
    kernel.establish_authentication_context(context, alice)
    kernel.add_effect_intent(intent)
    kernel.add_effect_contract(contract)
    kernel.add_authority_grant(AuthorityGrant("g2-grant-alice", root.root_id, alice.principal_id, intent.intent_id))
    kernel.add_capability(Capability("g2-cap-X", "X"))
    kernel.set_authorized_effect_envelope(contract.contract_id, frozenset({"MODIFY(X)"}))

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
                    send_json(conn, {"allowed": False, "reason": "malformed_request", "detail": type(exc).__name__, "peer_uid": uid})
                    continue

                if request.get("action") == "shutdown" and uid == os.getuid():
                    send_json(conn, {"allowed": True, "reason": "shutdown"})
                    break

                if request.get("action") != "mutate":
                    send_json(conn, {"allowed": False, "reason": "unknown_action", "peer_uid": uid})
                    continue

                trusted_context = context if uid == args.authorized_uid else None
                action_request = ActionRequest(
                    f"g2-request-{uuid.uuid4()}",
                    intent.intent_id,
                    contract.contract_id,
                    declared_principal=request.get("declared_principal"),
                    untrusted_authority=request.get("untrusted_authority"),
                )
                authorization = kernel.authorize(action_request, authentication_context=trusted_context)
                if not authorization.allowed:
                    send_json(conn, {"allowed": False, "stage": "authorize", "reason": authorization.reason, "peer_uid": uid})
                    continue

                start = kernel.start_attempt(authorization.authorization)
                if not start.allowed:
                    send_json(conn, {"allowed": False, "stage": "start", "reason": start.reason, "peer_uid": uid})
                    continue

                effects_raw = request.get("possible_effects")
                effects = None if effects_raw is None else frozenset(str(item) for item in effects_raw)
                operation = TechnicalOperation(
                    "boundary_mutation",
                    str(request.get("resource", "")),
                    str(request.get("value", "")),
                    effects,
                )
                admission = kernel.admit_operation(start.attempt, "g2-cap-X", operation)
                if not admission.allowed:
                    send_json(conn, {
                        "allowed": False,
                        "stage": "admission",
                        "reason": admission.reason,
                        "peer_uid": uid,
                        "principal_id": authorization.authorization.principal_id,
                        "operation_digest": safe_operation_digest(operation),
                    })
                    continue

                execution = kernel.execute_admission(admission.admission.admission_id)
                send_json(conn, {
                    "allowed": execution.allowed,
                    "stage": "execution",
                    "reason": execution.reason,
                    "peer_uid": uid,
                    "principal_id": authorization.authorization.principal_id,
                    "attempt_id": start.attempt.attempt_id,
                    "admission_id": admission.admission.admission_id,
                    "operation_digest": admission.admission.operation_digest,
                    "canonical_operation": admission.admission.canonical_operation.decode("utf-8"),
                    "possible_effects": sorted(operation.possible_effects or []),
                    "authorized_effect_envelope": ["MODIFY(X)"],
                })
    finally:
        listener.close()
        if socket_path.exists():
            socket_path.unlink()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
