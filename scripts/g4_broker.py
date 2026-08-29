from __future__ import annotations

import argparse
import json
import os
import socket
import struct
import uuid
from pathlib import Path

from agency_kernel.g1 import ActionRequest, AuthenticationContext, AuthorityGrant, AuthorityRoot, EffectContract, EffectIntent, Principal
from agency_kernel.g2 import Capability
from agency_kernel.g4 import GitFile, GitTreeOperation, Kernel, PROTECTED_REF_DEFAULT


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


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--socket", required=True)
    p.add_argument("--ledger", required=True)
    p.add_argument("--repo", required=True)
    p.add_argument("--authorized-uid", required=True, type=int)
    p.add_argument("--ready-file", required=True)
    args = p.parse_args()

    socket_path = Path(args.socket)
    socket_path.parent.mkdir(parents=True, exist_ok=True)
    if socket_path.exists():
        socket_path.unlink()

    kernel = Kernel(args.ledger, args.repo, clock=lambda: 100)
    root = AuthorityRoot("g4-root")
    alice = Principal("alice")
    context = AuthenticationContext(f"unix-peer-uid:{args.authorized_uid}")
    intent = EffectIntent("g4.git.write", "sanitized protected-ref tree transition")
    contract = EffectContract("g4.contract.kernel-test", intent.intent_id)
    kernel.add_authority_root(root)
    kernel.add_principal(alice)
    kernel.establish_authentication_context(context, alice)
    kernel.add_effect_intent(intent)
    kernel.add_effect_contract(contract)
    kernel.add_authority_grant(AuthorityGrant("g4-grant-alice", root.root_id, alice.principal_id, intent.intent_id))
    kernel.add_capability(Capability("g4-cap-ref", PROTECTED_REF_DEFAULT))
    kernel.set_authorized_effect_envelope(
        contract.contract_id,
        frozenset({
            kernel.ref_effect(PROTECTED_REF_DEFAULT),
            kernel.path_effect("A.txt"),
            kernel.path_effect("B.txt"),
            kernel.path_effect("goal.txt"),
        }),
    )

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

                trusted_context = context if uid == args.authorized_uid else None

                if request.get("action") == "execute_admission":
                    if trusted_context is None:
                        send_json(conn, {"allowed": False, "reason": "missing_authentication_context", "peer_uid": uid})
                        continue
                    result = kernel.execute_git_admission(str(request.get("admission_id", "")))
                    send_json(conn, {
                        "allowed": result.occurred,
                        "stage": "execution",
                        "reason": result.reason,
                        "before_oid": result.before_oid,
                        "after_oid": result.after_oid,
                        "tree_oid": result.tree_oid,
                    })
                    continue

                if request.get("action") != "mutate":
                    send_json(conn, {"allowed": False, "reason": "unknown_action", "peer_uid": uid})
                    continue

                action_request = ActionRequest(
                    f"g4-request-{uuid.uuid4()}",
                    intent.intent_id,
                    contract.contract_id,
                    declared_principal=request.get("declared_principal"),
                    untrusted_authority=request.get("untrusted_authority"),
                )
                auth = kernel.authorize(action_request, authentication_context=trusted_context)
                if not auth.allowed:
                    send_json(conn, {"allowed": False, "stage": "authorize", "reason": auth.reason, "peer_uid": uid})
                    continue
                start = kernel.start_attempt(auth.authorization)
                if not start.allowed:
                    send_json(conn, {"allowed": False, "stage": "start", "reason": start.reason, "peer_uid": uid})
                    continue

                files_raw = request.get("files", {})
                if not isinstance(files_raw, dict):
                    send_json(conn, {"allowed": False, "stage": "proposal", "reason": "invalid_files", "peer_uid": uid})
                    continue
                files = tuple(GitFile(str(k), str(v)) for k, v in sorted(files_raw.items()))
                effects_raw = request.get("possible_effects")
                effects = None if effects_raw is None else frozenset(str(item) for item in effects_raw)
                expected = str(request.get("expected_old_oid") or kernel.git_repo.rev_parse_ref())
                op = GitTreeOperation(PROTECTED_REF_DEFAULT, expected, files, effects)
                admission = kernel.admit_git_operation(start.attempt, "g4-cap-ref", op)
                if not admission.allowed:
                    send_json(conn, {"allowed": False, "stage": "admission", "reason": admission.reason, "peer_uid": uid})
                    continue
                execution = kernel.execute_git_admission(admission.admission.admission_id)
                obs = None
                if execution.occurred:
                    from agency_kernel.g4 import GitObserver
                    obs = GitObserver(kernel.git_repo).observe()
                send_json(conn, {
                    "allowed": execution.occurred,
                    "stage": "execution",
                    "reason": execution.reason,
                    "peer_uid": uid,
                    "principal_id": auth.authorization.principal_id,
                    "attempt_id": start.attempt.attempt_id,
                    "admission_id": admission.admission.admission_id,
                    "operation_digest": admission.admission.operation_digest,
                    "canonical_operation": admission.admission.canonical_operation.decode("utf-8"),
                    "before_oid": execution.before_oid,
                    "after_oid": execution.after_oid,
                    "tree_oid": execution.tree_oid,
                    "observed_files": {} if obs is None else dict(obs.files),
                })
    finally:
        listener.close()
        if socket_path.exists():
            socket_path.unlink()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
