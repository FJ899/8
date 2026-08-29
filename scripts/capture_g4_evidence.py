from __future__ import annotations

import hashlib
import json
import tempfile
from pathlib import Path

from agency_kernel.g1 import ActionRequest, AuthenticationContext, AuthorityGrant, AuthorityRoot, EffectContract, EffectIntent, Principal
from agency_kernel.g2 import Capability
from agency_kernel.g4 import GitFile, GitObserver, GitTreeOperation, Kernel, PROTECTED_REF_DEFAULT


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def seed(root: Path):
    k = Kernel(root / "control.db", root / "target.git", clock=lambda: 100)
    principal = Principal("alice")
    context = AuthenticationContext("session-alice")
    intent = EffectIntent("intent.git", "sanitized-git-transfer")
    contract = EffectContract("contract.git", intent.intent_id)
    k.add_authority_root(AuthorityRoot("root"))
    k.add_principal(principal)
    k.establish_authentication_context(context, principal)
    k.add_effect_intent(intent)
    k.add_effect_contract(contract)
    k.add_authority_grant(AuthorityGrant("grant-alice", "root", "alice", intent.intent_id))
    k.add_capability(Capability("cap-git", PROTECTED_REF_DEFAULT))
    k.set_authorized_effect_envelope(contract.contract_id, frozenset({
        k.ref_effect(PROTECTED_REF_DEFAULT), k.path_effect("A.txt"), k.path_effect("goal.txt")
    }))
    auth = k.authorize(ActionRequest("request-1", intent.intent_id, contract.contract_id), authentication_context=context)
    start = k.start_attempt(auth.authorization)
    return k, start.attempt, GitObserver(k.git_repo), intent, contract


def op(k: Kernel, files: dict[str, str], *, expected: str | None = None, effects="auto") -> GitTreeOperation:
    expected = expected or k.git_repo.rev_parse_ref()
    items = tuple(GitFile(p, v) for p, v in sorted(files.items()))
    shell = GitTreeOperation(PROTECTED_REF_DEFAULT, expected, items, frozenset())
    required = k.required_possible_effects(shell)
    if effects == "auto":
        effects = required
    return GitTreeOperation(PROTECTED_REF_DEFAULT, expected, items, effects)


def main() -> int:
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--output-dir", required=True)
    args = p.parse_args()
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    scenarios = {}

    with tempfile.TemporaryDirectory() as td:
        k, attempt, observer, _intent, _contract = seed(Path(td))
        operation = op(k, {"A.txt": "positive"})
        adm = k.admit_git_operation(attempt, "cap-git", operation)
        exe = k.execute_git_admission(adm.admission.admission_id)
        obs = observer.observe()
        comp = k.assess_compliance(adm.admission, obs, supported_possible_effects=operation.possible_effects)
        scenarios["positive"] = {
            "admitted": adm.allowed, "occurred": exe.occurred, "did": k.did(adm.admission, obs),
            "compliance": comp.status, "satisfied": k.satisfied(obs, {"A.txt": "positive"}),
            "before_oid": exe.before_oid, "after_oid": exe.after_oid, "tree_oid": obs.tree_oid,
            "actual_effects": sorted(comp.actual_effects), "possible_effects": sorted(comp.possible_effects),
            "control_completion": k.has_control_completion(adm.admission.admission_id),
        }

    with tempfile.TemporaryDirectory() as td:
        k, attempt, observer, _intent, _contract = seed(Path(td))
        old = k.git_repo.rev_parse_ref()
        stale = GitTreeOperation(PROTECTED_REF_DEFAULT, "0" * 40, (GitFile("A.txt", "stale"),), frozenset({k.ref_effect(PROTECTED_REF_DEFAULT), k.path_effect("A.txt")}))
        result = k.admit_git_operation(attempt, "cap-git", stale)
        scenarios["stale_ref"] = {"allowed": result.allowed, "reason": result.reason, "ref_unchanged": observer.observe().commit_oid == old}

    with tempfile.TemporaryDirectory() as td:
        k, attempt, observer, _intent, _contract = seed(Path(td))
        operation = op(k, {"A.txt": "crash"})
        adm = k.admit_git_operation(attempt, "cap-git", operation)
        exe = k.execute_git_admission(adm.admission.admission_id, crash_point="after_ref_cas_before_control_completion")
        obs = observer.observe()
        scenarios["post_cas_crash"] = {
            "occurred": exe.occurred, "reason": exe.reason, "did": k.did(adm.admission, obs),
            "control_completion": k.has_control_completion(adm.admission.admission_id),
            "replay": k.execute_git_admission(adm.admission.admission_id).reason,
        }

    with tempfile.TemporaryDirectory() as td:
        k, attempt, observer, _intent, _contract = seed(Path(td))
        operation = op(k, {"A.txt": "authorized"})
        adm = k.admit_git_operation(attempt, "cap-git", operation)
        k.execute_git_admission(adm.admission.admission_id)
        k.inject_unattributed_ref_for_test((GitFile("A.txt", "unattributed"),))
        obs = observer.observe()
        comp = k.assess_compliance(adm.admission, obs, supported_possible_effects=operation.possible_effects)
        scenarios["unattributed_delta"] = {"did": k.did(adm.admission, obs), "compliance": comp.status, "reason": comp.reason, "files": dict(obs.files)}

    with tempfile.TemporaryDirectory() as td:
        k, attempt, observer, intent, contract = seed(Path(td))
        before_auth = len(k.snapshot()["action_authorizations"])
        k.inject_unattributed_ref_for_test((GitFile("goal.txt", "goal"),))
        obs = observer.observe()
        denied = k.authorize(ActionRequest("request-no-session", intent.intent_id, contract.contract_id))
        scenarios["retroactive_success"] = {
            "satisfied": k.satisfied(obs, {"goal.txt": "goal"}), "authorized_from_outcome": denied.allowed,
            "authorization_count_unchanged": len(k.snapshot()["action_authorizations"]) == before_auth,
            "observed_admission_id": obs.admission_id,
        }

    with tempfile.TemporaryDirectory() as td:
        k, attempt, observer, _intent, _contract = seed(Path(td))
        operation = op(k, {"A.txt": "x"})
        under = GitTreeOperation(operation.protected_ref, operation.expected_old_oid, operation.files, frozenset({k.ref_effect(PROTECTED_REF_DEFAULT)}))
        under_result = k.admit_git_operation(attempt, "cap-git", under)
        scenarios["underapproximation"] = {"allowed": under_result.allowed, "reason": under_result.reason, "ref": observer.observe().commit_oid}

    evidence = out / "g4_state_evidence.json"
    evidence.write_text(json.dumps(scenarios, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    manifest = {evidence.name: sha256(evidence)}
    (out / "SHA256SUMS.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
