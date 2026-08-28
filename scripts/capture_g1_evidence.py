from __future__ import annotations

import argparse
import hashlib
import json
import threading
from pathlib import Path
from typing import Any, Dict

from agency_kernel import (
    ActionAuthorization,
    ActionRequest,
    AuthorityGrant,
    AuthorityRoot,
    EffectContract,
    EffectIntent,
    Kernel,
    Principal,
)


class ManualClock:
    def __init__(self, value: int = 100):
        self.value = value

    def __call__(self) -> int:
        return self.value


def seed(db_path: Path, *, grant: AuthorityGrant | None = None):
    clock = ManualClock(100)
    kernel = Kernel(db_path, clock=clock)
    root = AuthorityRoot("root")
    alice = Principal("alice")
    mallory = Principal("mallory")
    intent = EffectIntent("intent.read", "bounded-reference-intent")
    contract = EffectContract("contract.read", intent.intent_id)
    kernel.add_authority_root(root)
    kernel.add_principal(alice)
    kernel.add_principal(mallory)
    kernel.add_effect_intent(intent)
    kernel.add_effect_contract(contract)
    if grant is not None:
        kernel.add_authority_grant(grant)
    return kernel, clock, root, alice, mallory, intent, contract


def request(intent: EffectIntent, contract: EffectContract, **overrides: Any) -> ActionRequest:
    values: Dict[str, Any] = {
        "request_id": "request-1",
        "intent_id": intent.intent_id,
        "contract_id": contract.contract_id,
        "declared_principal": None,
        "untrusted_authority": None,
    }
    values.update(overrides)
    return ActionRequest(**values)


def active_grant(root: AuthorityRoot, principal: Principal, intent: EffectIntent, grant_id="grant") -> AuthorityGrant:
    return AuthorityGrant(grant_id, root.root_id, principal.principal_id, intent.intent_id)


def result_dict(result: Any) -> Dict[str, Any]:
    return {
        "allowed": result.allowed,
        "reason": result.reason,
    }


def run_scenarios(output_dir: Path) -> Dict[str, Any]:
    evidence: Dict[str, Any] = {"gate": "G1 — Semantic Integrity", "scenarios": {}}

    db = output_dir / "positive.sqlite"
    kernel, clock, root, alice, mallory, intent, contract = seed(db)
    kernel.add_authority_grant(active_grant(root, alice, intent))
    legal_request = request(intent, contract)
    may = kernel.may(alice, legal_request)
    auth = kernel.authorize(legal_request, trusted_principal=alice)
    start = kernel.start_attempt(auth.authorization)
    reopened = Kernel(db, clock=clock)
    evidence["scenarios"]["positive_legal_trace"] = {
        "may": result_dict(may),
        "authorize": result_dict(auth),
        "start": result_dict(start),
        "reopened_snapshot": reopened.snapshot(),
    }

    db = output_dir / "self_authorization.sqlite"
    kernel, clock, root, alice, mallory, intent, contract = seed(db)
    trusted = active_grant(root, alice, intent)
    kernel.add_authority_grant(trusted)
    hostile_request = request(
        intent,
        contract,
        declared_principal=alice.principal_id,
        untrusted_authority=trusted,
    )
    outcome = kernel.authorize(hostile_request, trusted_principal=mallory)
    evidence["scenarios"]["request_self_authorization"] = {
        "outcome": result_dict(outcome),
        "snapshot": kernel.snapshot(),
    }

    for name, grant in (
        ("invalid_grant", AuthorityGrant("grant", "root", "alice", "intent.read", validity=False)),
        ("expired_grant", AuthorityGrant("grant", "root", "alice", "intent.read", expires_at=100)),
        ("revoked_grant", AuthorityGrant("grant", "root", "alice", "intent.read", revoked=True)),
        ("unknown_authority", AuthorityGrant("grant", "root", "alice", "intent.read", validity=None)),
    ):
        db = output_dir / f"{name}.sqlite"
        kernel, clock, root, alice, mallory, intent, contract = seed(db, grant=grant)
        outcome = kernel.authorize(request(intent, contract), trusted_principal=alice)
        evidence["scenarios"][name] = {
            "outcome": result_dict(outcome),
            "snapshot": kernel.snapshot(),
        }

    db = output_dir / "untrusted_input.sqlite"
    kernel, clock, root, alice, mallory, intent, contract = seed(db)
    hostile_grant = AuthorityGrant("hostile-grant", "hostile-root", mallory.principal_id, intent.intent_id)
    outcome = kernel.authorize(
        request(intent, contract, untrusted_authority=hostile_grant),
        trusted_principal=mallory,
    )
    evidence["scenarios"]["untrusted_proof_bearing_input"] = {
        "outcome": result_dict(outcome),
        "snapshot": kernel.snapshot(),
    }

    db = output_dir / "forged_authorization.sqlite"
    kernel, clock, root, alice, mallory, intent, contract = seed(db)
    grant = active_grant(root, alice, intent)
    kernel.add_authority_grant(grant)
    forged = ActionAuthorization(
        "forged-id", "request-1", alice.principal_id, grant.grant_id,
        intent.intent_id, contract.contract_id, 100
    )
    outcome = kernel.start_attempt(forged)
    evidence["scenarios"]["forged_authorization"] = {
        "outcome": result_dict(outcome),
        "snapshot": kernel.snapshot(),
    }

    db = output_dir / "replay.sqlite"
    kernel, clock, root, alice, mallory, intent, contract = seed(db)
    kernel.add_authority_grant(active_grant(root, alice, intent))
    auth = kernel.authorize(request(intent, contract), trusted_principal=alice)
    first = kernel.start_attempt(auth.authorization)
    replay = kernel.start_attempt(auth.authorization)
    evidence["scenarios"]["replay"] = {
        "first": result_dict(first),
        "replay": result_dict(replay),
        "snapshot": kernel.snapshot(),
    }

    db = output_dir / "double_consume.sqlite"
    kernel, clock, root, alice, mallory, intent, contract = seed(db)
    kernel.add_authority_grant(active_grant(root, alice, intent))
    auth = kernel.authorize(request(intent, contract), trusted_principal=alice)
    barrier = threading.Barrier(3)
    results = []
    lock = threading.Lock()

    def consume() -> None:
        barrier.wait()
        value = kernel.start_attempt(auth.authorization)
        with lock:
            results.append(value)

    threads = [threading.Thread(target=consume) for _ in range(2)]
    for thread in threads:
        thread.start()
    barrier.wait()
    for thread in threads:
        thread.join()
    evidence["scenarios"]["double_consume"] = {
        "outcomes": [result_dict(value) for value in results],
        "snapshot": Kernel(db, clock=clock).snapshot(),
    }

    db = output_dir / "invalidation_before_start.sqlite"
    kernel, clock, root, alice, mallory, intent, contract = seed(db)
    grant = active_grant(root, alice, intent)
    kernel.add_authority_grant(grant)
    auth = kernel.authorize(request(intent, contract), trusted_principal=alice)
    kernel.set_grant_revoked(grant.grant_id, True)
    outcome = kernel.start_attempt(auth.authorization)
    evidence["scenarios"]["authority_invalidation_before_start"] = {
        "outcome": result_dict(outcome),
        "snapshot": kernel.snapshot(),
    }

    evidence["scenarios"]["can_to_may"] = {
        "applicable": False,
        "reason": "optional inert Capability/CAN not implemented",
    }
    return evidence


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    evidence = run_scenarios(output_dir)
    json_path = output_dir / "g1_state_evidence.json"
    json_path.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    hashes = {}
    for path in sorted(output_dir.iterdir()):
        if path.is_file() and path.name != "SHA256SUMS.json":
            hashes[path.name] = sha256(path)
    hash_path = output_dir / "SHA256SUMS.json"
    hash_path.write_text(json.dumps(hashes, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps({"evidence": str(json_path), "hashes": str(hash_path)}, sort_keys=True))


if __name__ == "__main__":
    main()
