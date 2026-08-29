from __future__ import annotations

import json
import tempfile
from pathlib import Path

from agency_kernel.g1 import ActionRequest, AuthenticationContext, AuthorityGrant, AuthorityRoot, EffectContract, EffectIntent, Principal
from agency_kernel.g2 import Capability
from agency_kernel.g4 import GitFile, GitObserver, GitTreeOperation, Kernel, PROTECTED_REF_DEFAULT


def seed(root: Path):
    k = Kernel(root / "control.db", root / "target.git", clock=lambda: 100)
    alice = Principal("alice")
    context = AuthenticationContext("session-alice")
    intent = EffectIntent("intent.git", "sanitized-git-transfer")
    contract = EffectContract("contract.git", intent.intent_id)
    k.add_authority_root(AuthorityRoot("root"))
    k.add_principal(alice)
    k.establish_authentication_context(context, alice)
    k.add_effect_intent(intent)
    k.add_effect_contract(contract)
    k.add_authority_grant(AuthorityGrant("grant", "root", "alice", intent.intent_id))
    k.add_capability(Capability("cap", PROTECTED_REF_DEFAULT))
    k.set_authorized_effect_envelope(contract.contract_id, frozenset({
        k.ref_effect(PROTECTED_REF_DEFAULT), k.path_effect("A.txt"), k.path_effect("goal.txt"), k.path_effect("hidden.txt")
    }))
    auth = k.authorize(ActionRequest("request", intent.intent_id, contract.contract_id), authentication_context=context)
    attempt = k.start_attempt(auth.authorization).attempt
    return k, attempt, GitObserver(k.git_repo)


def operation(k: Kernel, files: dict[str, str]) -> GitTreeOperation:
    expected = k.git_repo.rev_parse_ref()
    items = tuple(GitFile(p, v) for p, v in sorted(files.items()))
    shell = GitTreeOperation(PROTECTED_REF_DEFAULT, expected, items, frozenset())
    return GitTreeOperation(PROTECTED_REF_DEFAULT, expected, items, k.required_possible_effects(shell))


def main() -> int:
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--output", required=True)
    args = p.parse_args()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    evidence = {}

    with tempfile.TemporaryDirectory() as td:
        k, attempt, observer = seed(Path(td))
        exact = "  leading and trailing  \n"
        op = operation(k, {"A.txt": exact})
        adm = k.admit_git_operation(attempt, "cap", op)
        k.execute_git_admission(adm.admission.admission_id)
        obs = observer.observe()
        evidence["exact_observation"] = {"expected": exact, "observed": dict(obs.files)["A.txt"], "equal": dict(obs.files)["A.txt"] == exact}

    with tempfile.TemporaryDirectory() as td:
        k, attempt, observer = seed(Path(td))
        op = operation(k, {"A.txt": "authorized"})
        adm = k.admit_git_operation(attempt, "cap", op)
        k.execute_git_admission(adm.admission.admission_id)
        k.inject_unattributed_ref_for_test((GitFile("A.txt", "authorized"), GitFile("hidden.txt", "hidden")))
        obs = observer.observe()
        comp = k.assess_compliance(adm.admission, obs, supported_possible_effects=op.possible_effects)
        evidence["hidden_target_mutation"] = {"files": dict(obs.files), "did": k.did(adm.admission, obs), "compliance": comp.status, "reason": comp.reason}

    with tempfile.TemporaryDirectory() as td:
        k, attempt, observer = seed(Path(td))
        expected = k.git_repo.rev_parse_ref()
        files = (GitFile("secret.txt", "forbidden"),)
        shell = GitTreeOperation(PROTECTED_REF_DEFAULT, expected, files, frozenset())
        required = k.required_possible_effects(shell)
        result = k.admit_git_operation(attempt, "cap", GitTreeOperation(PROTECTED_REF_DEFAULT, expected, files, required))
        evidence["unauthorized_path_envelope"] = {"allowed": result.allowed, "reason": result.reason, "required_effects": sorted(required), "ref": observer.observe().commit_oid}

    with tempfile.TemporaryDirectory() as td:
        k, attempt, observer = seed(Path(td))
        legal = operation(k, {"A.txt": "legal"})
        adm = k.admit_git_operation(attempt, "cap", legal)
        k.execute_git_admission(adm.admission.admission_id)
        before_auth = len(k.snapshot()["action_authorizations"])
        k.inject_unattributed_ref_for_test((GitFile("goal.txt", "goal"),))
        obs = observer.observe()
        comp = k.assess_compliance(adm.admission, obs, supported_possible_effects=legal.possible_effects)
        acceptance = k.accept(True)
        evidence["outcome_history_not_repaired"] = {
            "satisfied": k.satisfied(obs, {"goal.txt": "goal"}), "acceptance": acceptance.passed,
            "compliance": comp.status, "reason": comp.reason, "within_scope": k.within_scope(comp),
            "authorization_count_unchanged": len(k.snapshot()["action_authorizations"]) == before_auth,
        }

    out.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
