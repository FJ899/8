from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import os
import platform
import sqlite3
import subprocess
import sys
import threading
import unittest
from pathlib import Path
from typing import Any, Dict

REPO_ROOT = Path(__file__).resolve().parents[1]
_IMPORT_ENV_KEYS = ("PYTHONHOME", "PYTHONPATH", "PYTHONUSERBASE", "PYTHONNOUSERSITE")


def _ensure_isolated() -> None:
    if sys.flags.isolated:
        return
    env = os.environ.copy()
    env["AK_G1_ORIGINAL_ARGV"] = json.dumps(sys.argv)
    env["AK_G1_ORIGINAL_PYTHONPATH"] = env.get("PYTHONPATH", "<unset>")
    for key in ("PYTHONHOME", "PYTHONPATH", "PYTHONUSERBASE"):
        env.pop(key, None)
    env["PYTHONNOUSERSITE"] = "1"
    os.execve(sys.executable, [sys.executable, "-I", str(Path(__file__).resolve()), *sys.argv[1:]], env)


_ensure_isolated()
os.chdir(REPO_ROOT)
sys.path.insert(0, str(REPO_ROOT))

import agency_kernel
import agency_kernel.g1 as agency_kernel_g1
import tests.test_g1 as test_g1
from agency_kernel import (
    ActionAuthorization, ActionRequest, AuthenticationContext, AuthorityGrant,
    AuthorityRoot, EffectContract, EffectIntent, Kernel, Principal,
)


class ProvenanceError(RuntimeError):
    pass


class ManualClock:
    def __init__(self, value: int = 100): self.value = value
    def __call__(self) -> int: return self.value


def _git(*args: str) -> str:
    completed = subprocess.run(["git", *args], cwd=REPO_ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if completed.returncode != 0:
        raise ProvenanceError(f"git {' '.join(args)} failed ({completed.returncode}): {completed.stderr.strip()}")
    return completed.stdout.strip()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""): digest.update(chunk)
    return digest.hexdigest()


def git_blob_id(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def expected_blob(path: str) -> str:
    line = _git("ls-tree", "HEAD", "--", path)
    if not line: raise ProvenanceError(f"candidate tree has no blob for {path}")
    metadata, actual_path = line.split("\t", 1)
    _, object_type, blob = metadata.split()
    if object_type != "blob" or actual_path != path: raise ProvenanceError(f"unexpected tree entry for {path}: {line}")
    return blob


def module_provenance(name: str, module: Any, repo_path: str) -> Dict[str, Any]:
    origin = getattr(module, "__file__", None)
    if not origin: raise ProvenanceError(f"{name} has no __file__")
    origin_path = Path(origin).resolve(); expected_path = (REPO_ROOT / repo_path).resolve(); expected = expected_blob(repo_path)
    materialized = git_blob_id(expected_path); loaded = git_blob_id(origin_path)
    if origin_path != expected_path or materialized != expected or loaded != expected:
        raise ProvenanceError(f"module provenance mismatch for {name}")
    return {"module": name, "repo_path": repo_path, "origin": str(origin_path), "expected_origin": str(expected_path),
            "expected_candidate_blob": expected, "materialized_git_blob": materialized, "loaded_git_blob": loaded,
            "materialized_sha256": sha256(expected_path), "loaded_sha256": sha256(origin_path)}


def capture_runtime_provenance() -> Dict[str, Any]:
    modules = {
        "agency_kernel": module_provenance("agency_kernel", agency_kernel, "agency_kernel/__init__.py"),
        "agency_kernel.g1": module_provenance("agency_kernel.g1", agency_kernel_g1, "agency_kernel/g1.py"),
        "tests.test_g1": module_provenance("tests.test_g1", test_g1, "tests/test_g1.py"),
    }
    script_expected = expected_blob("scripts/capture_g1_evidence.py")
    script_materialized = git_blob_id(Path(__file__).resolve())
    if script_materialized != script_expected: raise ProvenanceError("evidence script does not match candidate blob")
    return {"repository_root": str(REPO_ROOT), "cwd": os.getcwd(), "candidate_head": _git("rev-parse", "HEAD"),
            "candidate_tree": _git("rev-parse", "HEAD^{tree}"), "original_command_argv": json.loads(os.environ.get("AK_G1_ORIGINAL_ARGV", "[]")),
            "effective_command_argv": [sys.executable, "-I", str(Path(__file__).resolve()), *sys.argv[1:]],
            "original_pythonpath": os.environ.get("AK_G1_ORIGINAL_PYTHONPATH", "<unknown>"),
            "import_environment": {key: os.environ.get(key, "<unset>") for key in _IMPORT_ENV_KEYS}, "sys_path": list(sys.path),
            "isolated": bool(sys.flags.isolated), "no_user_site": bool(sys.flags.no_user_site), "python_version": sys.version,
            "sqlite_version": sqlite3.sqlite_version, "platform": platform.platform(), "os_name": os.name, "modules": modules,
            "evidence_script": {"origin": str(Path(__file__).resolve()), "expected_candidate_blob": script_expected,
                                "materialized_git_blob": script_materialized, "sha256": sha256(Path(__file__).resolve())}}


def run_g1_tests() -> Dict[str, Any]:
    suite = unittest.defaultTestLoader.loadTestsFromModule(test_g1); runner_stream = io.StringIO(); stdout = io.StringIO(); stderr = io.StringIO()
    with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
        result = unittest.TextTestRunner(stream=runner_stream, verbosity=2).run(suite)
    return {"successful": result.wasSuccessful(), "tests_run": result.testsRun, "failures": len(result.failures), "errors": len(result.errors),
            "skipped": len(result.skipped), "runner_output": runner_stream.getvalue(), "stdout": stdout.getvalue(), "stderr": stderr.getvalue(),
            "exit_code": 0 if result.wasSuccessful() else 1}


def seed(db_path: Path, *, grant: AuthorityGrant | None = None):
    clock = ManualClock(100); kernel = Kernel(db_path, clock=clock); root = AuthorityRoot("root"); alice = Principal("alice"); mallory = Principal("mallory")
    alice_context = AuthenticationContext("fixture-session-alice"); mallory_context = AuthenticationContext("fixture-session-mallory")
    intent = EffectIntent("intent.read", "bounded-reference-intent"); contract = EffectContract("contract.read", intent.intent_id)
    kernel.add_authority_root(root); kernel.add_principal(alice); kernel.add_principal(mallory)
    kernel.establish_authentication_context(alice_context, alice); kernel.establish_authentication_context(mallory_context, mallory)
    kernel.add_effect_intent(intent); kernel.add_effect_contract(contract)
    if grant is not None: kernel.add_authority_grant(grant)
    return kernel, clock, root, alice, mallory, alice_context, mallory_context, intent, contract


def request(intent: EffectIntent, contract: EffectContract, **overrides: Any) -> ActionRequest:
    values: Dict[str, Any] = {"request_id": "request-1", "intent_id": intent.intent_id, "contract_id": contract.contract_id,
                              "declared_principal": None, "untrusted_authority": None}; values.update(overrides); return ActionRequest(**values)


def active_grant(root: AuthorityRoot, principal: Principal, intent: EffectIntent, grant_id="grant") -> AuthorityGrant:
    return AuthorityGrant(grant_id, root.root_id, principal.principal_id, intent.intent_id)


def result_dict(result: Any) -> Dict[str, Any]: return {"allowed": result.allowed, "reason": result.reason}


def assert_checkpoint(condition: bool, scenario: str, detail: str) -> None:
    if not condition: raise AssertionError(f"{scenario}: {detail}")


def assert_no_early_auth_failure(scenario: str, result: Any) -> None:
    assert_checkpoint(result.reason not in {"missing_authentication_context", "forged_authorization"}, scenario, f"unexpected early {result.reason}")


def run_scenarios(output_dir: Path) -> Dict[str, Any]:
    evidence: Dict[str, Any] = {"gate": "G1 — Semantic Integrity", "scenarios": {}}

    db = output_dir / "positive.sqlite"; kernel, clock, root, alice, mallory, ac, mc, intent, contract = seed(db)
    kernel.add_authority_grant(active_grant(root, alice, intent)); legal = request(intent, contract)
    may = kernel.may(ac, legal); auth = kernel.authorize(legal, authentication_context=ac)
    assert_checkpoint(may.allowed and may.reason == "may", "positive_legal_trace", "MAY checkpoint not reached")
    assert_checkpoint(auth.allowed and auth.authorization is not None, "positive_legal_trace", "ActionAuthorization not created")
    start = kernel.start_attempt(auth.authorization); assert_checkpoint(start.allowed and start.consumed is not None and start.started is not None, "positive_legal_trace", "consume/start checkpoint not reached")
    snap = Kernel(db, clock=clock).snapshot(); assert_checkpoint(len(snap["action_authorizations"]) == len(snap["authorization_consumed"]) == len(snap["action_attempts"]) == len(snap["attempt_started"]) == 1, "positive_legal_trace", "durable trace incomplete")
    evidence["scenarios"]["positive_legal_trace"] = {"may": result_dict(may), "authorize": result_dict(auth), "start": result_dict(start), "reopened_snapshot": snap}

    db = output_dir / "self_authorization.sqlite"; kernel, clock, root, alice, mallory, ac, mc, intent, contract = seed(db)
    trusted = active_grant(root, alice, intent); kernel.add_authority_grant(trusted); hostile = request(intent, contract, declared_principal=alice.principal_id, untrusted_authority=trusted)
    outcome = kernel.authorize(hostile, authentication_context=mc); assert_no_early_auth_failure("request_self_authorization", outcome)
    assert_checkpoint(not outcome.allowed and outcome.reason == "authority_absent" and not kernel.snapshot()["action_authorizations"], "request_self_authorization", "hostile request created authority")
    evidence["scenarios"]["request_self_authorization"] = {"outcome": result_dict(outcome), "snapshot": kernel.snapshot()}

    expected = {"invalid_grant": "authority_invalid", "expired_grant": "authority_expired", "revoked_grant": "authority_revoked", "unknown_authority": "unknown_authority_fact"}
    grants = {"invalid_grant": AuthorityGrant("grant", "root", "alice", "intent.read", validity=False), "expired_grant": AuthorityGrant("grant", "root", "alice", "intent.read", expires_at=100),
              "revoked_grant": AuthorityGrant("grant", "root", "alice", "intent.read", revoked=True), "unknown_authority": AuthorityGrant("grant", "root", "alice", "intent.read", validity=None)}
    for name, grant in grants.items():
        db = output_dir / f"{name}.sqlite"; kernel, clock, root, alice, mallory, ac, mc, intent, contract = seed(db, grant=grant)
        outcome = kernel.authorize(request(intent, contract), authentication_context=ac); assert_no_early_auth_failure(name, outcome)
        assert_checkpoint(not outcome.allowed and outcome.reason == expected[name] and not kernel.snapshot()["action_authorizations"], name, f"expected {expected[name]}, got {outcome.reason}")
        evidence["scenarios"][name] = {"outcome": result_dict(outcome), "snapshot": kernel.snapshot()}

    db = output_dir / "untrusted_input.sqlite"; kernel, clock, root, alice, mallory, ac, mc, intent, contract = seed(db)
    hostile_grant = AuthorityGrant("hostile-grant", "hostile-root", mallory.principal_id, intent.intent_id); before = kernel.snapshot()
    outcome = kernel.authorize(request(intent, contract, untrusted_authority=hostile_grant), authentication_context=mc); assert_no_early_auth_failure("untrusted_proof_bearing_input", outcome); after = kernel.snapshot()
    assert_checkpoint(not outcome.allowed and outcome.reason == "authority_absent" and after["authority_roots"] == before["authority_roots"] and after["authority_grants"] == before["authority_grants"] and not after["action_authorizations"], "untrusted_proof_bearing_input", "untrusted input changed proof-bearing state")
    evidence["scenarios"]["untrusted_proof_bearing_input"] = {"outcome": result_dict(outcome), "snapshot": after}

    db = output_dir / "forged_authorization.sqlite"; kernel, clock, root, alice, mallory, ac, mc, intent, contract = seed(db); grant = active_grant(root, alice, intent); kernel.add_authority_grant(grant)
    forged = ActionAuthorization("forged-id", "request-1", alice.principal_id, grant.grant_id, intent.intent_id, contract.contract_id, 100); outcome = kernel.start_attempt(forged)
    assert_checkpoint(not outcome.allowed and outcome.reason == "forged_authorization" and not kernel.snapshot()["action_attempts"], "forged_authorization", "forged authorization was not denied")
    evidence["scenarios"]["forged_authorization"] = {"outcome": result_dict(outcome), "snapshot": kernel.snapshot()}

    db = output_dir / "replay.sqlite"; kernel, clock, root, alice, mallory, ac, mc, intent, contract = seed(db); kernel.add_authority_grant(active_grant(root, alice, intent)); auth = kernel.authorize(request(intent, contract), authentication_context=ac); assert_no_early_auth_failure("replay", auth)
    first = kernel.start_attempt(auth.authorization); replay = kernel.start_attempt(auth.authorization); snap = kernel.snapshot()
    assert_checkpoint(first.allowed and not replay.allowed and replay.reason == "authorization_consumed" and len(snap["action_attempts"]) == 1, "replay", "replay created second attempt")
    evidence["scenarios"]["replay"] = {"first": result_dict(first), "replay": result_dict(replay), "snapshot": snap}

    db = output_dir / "double_consume.sqlite"; kernel, clock, root, alice, mallory, ac, mc, intent, contract = seed(db); kernel.add_authority_grant(active_grant(root, alice, intent)); auth = kernel.authorize(request(intent, contract), authentication_context=ac); assert_no_early_auth_failure("double_consume", auth)
    barrier = threading.Barrier(3); results = []; lock = threading.Lock()
    def consume() -> None:
        barrier.wait(); value = kernel.start_attempt(auth.authorization)
        with lock: results.append(value)
    threads = [threading.Thread(target=consume) for _ in range(2)]
    for thread in threads: thread.start()
    barrier.wait()
    for thread in threads: thread.join()
    snap = Kernel(db, clock=clock).snapshot(); assert_checkpoint(sum(1 for value in results if value.allowed) <= 1 and len(snap["action_attempts"]) <= 1, "double_consume", "more than one successful attempt")
    evidence["scenarios"]["double_consume"] = {"outcomes": [result_dict(value) for value in results], "snapshot": snap}

    db = output_dir / "invalidation_before_start.sqlite"; kernel, clock, root, alice, mallory, ac, mc, intent, contract = seed(db); grant = active_grant(root, alice, intent); kernel.add_authority_grant(grant); auth = kernel.authorize(request(intent, contract), authentication_context=ac); assert_no_early_auth_failure("authority_invalidation_before_start", auth)
    kernel.set_grant_revoked(grant.grant_id, True); outcome = kernel.start_attempt(auth.authorization); snap = kernel.snapshot()
    assert_checkpoint(not outcome.allowed and outcome.reason == "authority_revoked" and not snap["authorization_consumed"] and not snap["action_attempts"] and not snap["attempt_started"], "authority_invalidation_before_start", "invalidation-before-start created attempt")
    evidence["scenarios"]["authority_invalidation_before_start"] = {"outcome": result_dict(outcome), "snapshot": snap}
    evidence["scenarios"]["can_to_may"] = {"applicable": False, "reason": "optional inert Capability/CAN not implemented"}
    return evidence


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--output-dir", required=True); args = parser.parse_args(); output_dir = Path(args.output_dir).resolve(); output_dir.mkdir(parents=True, exist_ok=True)
    state = run_scenarios(output_dir); state["runtime_provenance"] = capture_runtime_provenance(); state["test_execution"] = run_g1_tests()
    json_path = output_dir / "g1_state_evidence.json"; json_path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    hashes = {path.name: sha256(path) for path in sorted(output_dir.iterdir()) if path.is_file() and path.name != "SHA256SUMS.json"}
    hash_path = output_dir / "SHA256SUMS.json"; hash_path.write_text(json.dumps(hashes, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"evidence": str(json_path), "hashes": str(hash_path), "tests_exit_code": state["test_execution"]["exit_code"]}, sort_keys=True))
    if not state["test_execution"]["successful"]: raise SystemExit(state["test_execution"]["exit_code"])


if __name__ == "__main__": main()
