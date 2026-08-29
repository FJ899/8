from __future__ import annotations

import hashlib
import json
import tempfile
from pathlib import Path

from agency_kernel.g1 import ActionRequest, AuthenticationContext, AuthorityGrant, AuthorityRoot, EffectContract, EffectIntent, Principal
from agency_kernel.g2 import Capability
from agency_kernel.g3 import DishonestPrimitive, Kernel, Observer, PutIfVersionOperation


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def seed(root: Path):
    k = Kernel(root / "control-ledger.db", root / "target.db", clock=lambda: 100)
    principal = Principal("alice"); context = AuthenticationContext("session-alice")
    intent = EffectIntent("intent.put", "versioned-put"); contract = EffectContract("contract.put", intent.intent_id)
    k.add_authority_root(AuthorityRoot("root")); k.add_principal(principal); k.establish_authentication_context(context, principal)
    k.add_effect_intent(intent); k.add_effect_contract(contract); k.add_authority_grant(AuthorityGrant("grant-alice", "root", "alice", intent.intent_id))
    k.add_capability(Capability("cap-X", "X")); k.set_authorized_effect_envelope(contract.contract_id, k.possible_effects_for("X"))
    auth = k.authorize(ActionRequest("request-1", intent.intent_id, contract.contract_id), authentication_context=context)
    start = k.start_attempt(auth.authorization); k.seed_resource("X", "initial", 0)
    return k, start.attempt, Observer(root / "target.db")


def main() -> int:
    import argparse
    p = argparse.ArgumentParser(); p.add_argument("--output-dir", required=True); args = p.parse_args()
    out = Path(args.output_dir); out.mkdir(parents=True, exist_ok=True); s = {}

    with tempfile.TemporaryDirectory() as td:
        root = Path(td); k, attempt, observer = seed(root); op = PutIfVersionOperation("X", 0, "after", k.possible_effects_for("X"))
        adm = k.admit_put_if_version(attempt, "cap-X", op); exe = k.execute_put_if_version_admission(adm.admission.admission_id); obs = observer.observe("X")
        comp = k.assess_compliance(adm.admission, obs, supported_possible_effects=op.possible_effects)
        s["positive"] = {"admitted": adm.allowed, "occurred": exe.occurred, "did": k.did(adm.admission, obs), "compliance": comp.status, "satisfied": k.satisfied(obs, "after"), "control_completion": k.has_control_completion(adm.admission.admission_id), "actual_effects": sorted(comp.actual_effects), "possible_effects": sorted(comp.possible_effects)}

    with tempfile.TemporaryDirectory() as td:
        root = Path(td); k, attempt, observer = seed(root); op = PutIfVersionOperation("X", 9, "stale", k.possible_effects_for("X"))
        adm = k.admit_put_if_version(attempt, "cap-X", op); exe = k.execute_put_if_version_admission(adm.admission.admission_id)
        s["stale_version"] = {"occurred": exe.occurred, "reason": exe.reason, "observed": observer.observe("X").value, "control_completion": k.has_control_completion(adm.admission.admission_id)}

    with tempfile.TemporaryDirectory() as td:
        root = Path(td); k, attempt, observer = seed(root); op = PutIfVersionOperation("X", 0, "crash", k.possible_effects_for("X"))
        adm = k.admit_put_if_version(attempt, "cap-X", op); exe = k.execute_put_if_version_admission(adm.admission.admission_id, crash_point="after_mutation_before_control_completion"); obs = observer.observe("X")
        s["post_mutation_crash"] = {"occurred": exe.occurred, "reason": exe.reason, "did": k.did(adm.admission, obs), "mutation_id": obs.mutation_id, "control_completion": k.has_control_completion(adm.admission.admission_id), "replay": k.execute_put_if_version_admission(adm.admission.admission_id).reason}

    with tempfile.TemporaryDirectory() as td:
        root = Path(td); k, attempt, observer = seed(root); op = PutIfVersionOperation("X", 0, "expected", k.possible_effects_for("X"))
        adm = k.admit_put_if_version(attempt, "cap-X", op); k.inject_unattributed_delta_for_test("X", "unattributed", 1); obs = observer.observe("X")
        comp = k.assess_compliance(adm.admission, obs, supported_possible_effects=op.possible_effects)
        s["observed_delta_without_provenance"] = {"observed_value": obs.value, "mutation_id": obs.mutation_id, "did": k.did(adm.admission, obs), "compliance": comp.status, "reason": comp.reason}

    with tempfile.TemporaryDirectory() as td:
        root = Path(td); k, attempt, observer = seed(root); op = PutIfVersionOperation("X", 0, "authorized", k.possible_effects_for("X"))
        adm = k.admit_put_if_version(attempt, "cap-X", op); k.execute_put_if_version_admission(adm.admission.admission_id)
        k.inject_unattributed_delta_preserving_provenance_for_test("X", "later-unattributed", 2); obs = observer.observe("X")
        comp = k.assess_compliance(adm.admission, obs, supported_possible_effects=op.possible_effects)
        s["stale_provenance_after_later_delta"] = {"observed_value": obs.value, "observed_version": obs.version, "mutation_id": obs.mutation_id, "did": k.did(adm.admission, obs), "compliance": comp.status, "reason": comp.reason}

    with tempfile.TemporaryDirectory() as td:
        root = Path(td); k, attempt, observer = seed(root); op = PutIfVersionOperation("X", 0, "goal", k.possible_effects_for("X"))
        adm = k.admit_put_if_version(attempt, "cap-X", op); before = len(k.snapshot()["action_authorizations"]); k.set_grant_revoked("grant-alice", True)
        k.inject_unattributed_delta_for_test("X", "goal", 1); obs = observer.observe("X"); comp = k.assess_compliance(adm.admission, obs, supported_possible_effects=op.possible_effects)
        later = k.admit_put_if_version(attempt, "cap-X", PutIfVersionOperation("X", 1, "later", k.possible_effects_for("X")))
        s["successful_unattributed_outcome"] = {"satisfied": k.satisfied(obs, "goal"), "did": k.did(adm.admission, obs), "compliance": comp.status, "reason": comp.reason, "authorization_count_unchanged": len(k.snapshot()["action_authorizations"]) == before, "later_authorization_path_allowed": later.allowed}

    with tempfile.TemporaryDirectory() as td:
        root = Path(td); _k, _attempt, observer = seed(root); DishonestPrimitive.execute(root / "target.db")
        observed_actual = frozenset(x for x in ("A", "B") if observer.observe(x).value is not None); d = DishonestPrimitive.diagnostic(observed_actual)
        s["dishonest_negative_control"] = {"effect_occurred": observed_actual == frozenset({"A", "B"}), "compliance": d.status, "reason": d.reason, "actual_effects": sorted(d.actual_effects), "possible_effects": sorted(d.possible_effects), "effect_model": "UNSOUND", "tcb_assumption": "FALSIFIED_DETECTED"}

    evidence = out / "g3_state_evidence.json"; evidence.write_text(json.dumps(s, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (out / "SHA256SUMS.json").write_text(json.dumps({evidence.name: sha256(evidence)}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__": raise SystemExit(main())
