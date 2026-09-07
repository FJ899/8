from __future__ import annotations

import tempfile
import unittest
from dataclasses import FrozenInstanceError
from pathlib import Path

from agency_kernel.bindings import CapabilityBinding, TrustedBindingRegistry
from agency_kernel.effect_seams import G3EffectAdapter, G4EffectAdapter
from agency_kernel.g1 import (
    ActionRequest,
    AuthenticationContext,
    AuthorityGrant,
    AuthorityRoot,
    EffectContract,
    EffectIntent,
    Kernel as G1Kernel,
    Principal,
)
from agency_kernel.g2 import Capability
from agency_kernel.g3 import Kernel as G3Kernel, Observer, PutIfVersionOperation
from agency_kernel.g4 import (
    GitFile,
    GitObserver,
    GitTreeOperation,
    Kernel as G4Kernel,
    PROTECTED_REF_DEFAULT,
)
from agency_kernel.runtime import KernelRuntime


class MultiDomainFixture:
    def __init__(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        root = Path(self.tempdir.name)
        self.control_db = root / "control.db"
        self.target_db = root / "target.db"
        self.repo_path = root / "target.git"

        # One authority ledger is consumed by one runtime.  G3 and G4 use the
        # same durable control DB for attempts/admissions but keep separate
        # effect targets.
        self.authority = G1Kernel(self.control_db, clock=lambda: 100)
        self.g3 = G3Kernel(self.control_db, self.target_db, clock=lambda: 100)
        self.g4 = G4Kernel(self.control_db, self.repo_path, clock=lambda: 100)

        self.root = AuthorityRoot("root")
        self.principal = Principal("alice")
        self.context = AuthenticationContext("session-alice")
        self.put_intent = EffectIntent("intent.put", "versioned-put")
        self.git_intent = EffectIntent("intent.git", "sanitized-git")
        self.denied_intent = EffectIntent("intent.denied", "not-granted")
        self.put_contract = EffectContract("contract.put", self.put_intent.intent_id)
        self.git_contract = EffectContract("contract.git", self.git_intent.intent_id)
        self.denied_contract = EffectContract("contract.denied", self.denied_intent.intent_id)

        self.authority.add_authority_root(self.root)
        self.authority.add_principal(self.principal)
        self.authority.establish_authentication_context(self.context, self.principal)
        for intent in (self.put_intent, self.git_intent, self.denied_intent):
            self.authority.add_effect_intent(intent)
        for contract in (self.put_contract, self.git_contract, self.denied_contract):
            self.authority.add_effect_contract(contract)
        self.authority.add_authority_grant(
            AuthorityGrant(
                "grant-put",
                self.root.root_id,
                self.principal.principal_id,
                self.put_intent.intent_id,
            )
        )
        self.authority.add_authority_grant(
            AuthorityGrant(
                "grant-git",
                self.root.root_id,
                self.principal.principal_id,
                self.git_intent.intent_id,
            )
        )

        self.g3.add_capability(Capability("cap-X", "X"))
        self.g4.add_capability(Capability("cap-git", PROTECTED_REF_DEFAULT))
        self.g3.set_authorized_effect_envelope(
            self.put_contract.contract_id,
            self.g3.possible_effects_for("X"),
        )
        self.g4.set_authorized_effect_envelope(
            self.git_contract.contract_id,
            frozenset(
                {
                    self.g4.ref_effect(PROTECTED_REF_DEFAULT),
                    self.g4.path_effect("A.txt"),
                }
            ),
        )
        self.g3.seed_resource("X", "initial", 0)

        self.g3_adapter = G3EffectAdapter(self.g3, Observer(self.target_db))
        self.g4_adapter = G4EffectAdapter(self.g4, GitObserver(self.g4.git_repo))
        self.put_binding = CapabilityBinding(
            "binding-put",
            self.put_intent.intent_id,
            "cap-X",
            "X",
            self.g3_adapter,
        )
        self.git_binding = CapabilityBinding(
            "binding-git",
            self.git_intent.intent_id,
            "cap-git",
            PROTECTED_REF_DEFAULT,
            self.g4_adapter,
        )
        self.registry = TrustedBindingRegistry((self.put_binding, self.git_binding))
        self.runtime = KernelRuntime(self.authority, self.registry)

    def close(self) -> None:
        self.tempdir.cleanup()

    def put_operation(self, value: str = "after", resource: str = "X") -> PutIfVersionOperation:
        return PutIfVersionOperation(
            resource,
            0,
            value,
            self.g3.possible_effects_for(resource),
        )

    def git_operation(self, value: str = "after", protected_ref: str = PROTECTED_REF_DEFAULT) -> GitTreeOperation:
        expected = self.g4.git_repo.rev_parse_ref()
        shell = GitTreeOperation(
            protected_ref,
            expected,
            (GitFile("A.txt", value),),
            frozenset(),
        )
        effects = self.g4.required_possible_effects(shell) if protected_ref == PROTECTED_REF_DEFAULT else frozenset()
        return GitTreeOperation(
            protected_ref,
            expected,
            shell.files,
            effects,
        )

    def request(self, intent: EffectIntent, contract: EffectContract, request_id: str, **kwargs) -> ActionRequest:
        return ActionRequest(request_id, intent.intent_id, contract.contract_id, **kwargs)


class TrustedCapabilityBindingTests(unittest.TestCase):
    def fixture(self) -> MultiDomainFixture:
        fixture = MultiDomainFixture()
        self.addCleanup(fixture.close)
        return fixture

    def test_one_runtime_resolves_two_domains_from_persisted_authorization_intent(self) -> None:
        f = self.fixture()

        put = f.put_operation("put-through-registry")
        put_trace = f.runtime.run(
            f.request(f.put_intent, f.put_contract, "put-request"),
            put,
            authentication_context=f.context,
        )
        self.assertTrue(put_trace.authorization.allowed, put_trace.authorization.reason)
        self.assertTrue(put_trace.binding.allowed, put_trace.binding.reason)
        self.assertEqual(put_trace.binding.binding.binding_id, "binding-put")
        self.assertEqual(put_trace.binding.binding.capability_id, "cap-X")
        self.assertTrue(put_trace.execution.occurred, put_trace.execution.reason)
        put_observation = f.g3_adapter.observe(put)
        self.assertTrue(f.g3_adapter.did(put_trace.admission.admission, put_observation))

        git = f.git_operation("git-through-registry")
        git_trace = f.runtime.run(
            f.request(f.git_intent, f.git_contract, "git-request"),
            git,
            authentication_context=f.context,
        )
        self.assertTrue(git_trace.authorization.allowed, git_trace.authorization.reason)
        self.assertTrue(git_trace.binding.allowed, git_trace.binding.reason)
        self.assertEqual(git_trace.binding.binding.binding_id, "binding-git")
        self.assertEqual(git_trace.binding.binding.capability_id, "cap-git")
        self.assertTrue(git_trace.execution.occurred, git_trace.execution.reason)
        git_observation = f.g4_adapter.observe(git)
        self.assertTrue(f.g4_adapter.did(git_trace.admission.admission, git_observation))

    def test_hostile_routing_fields_cannot_override_authorized_intent_binding(self) -> None:
        f = self.fixture()
        operation = f.put_operation("trusted-binding")
        request = f.request(
            f.put_intent,
            f.put_contract,
            "hostile-routing",
            declared_principal="mallory",
            untrusted_authority={
                "intent_id": f.git_intent.intent_id,
                "adapter_id": "attacker-adapter",
                "capability_id": "cap-git",
                "provider": "attacker-provider",
                "resource": PROTECTED_REF_DEFAULT,
            },
        )
        trace = f.runtime.run(request, operation, authentication_context=f.context)
        self.assertTrue(trace.authorization.allowed, trace.authorization.reason)
        self.assertEqual(trace.authorization.authorization.intent_id, f.put_intent.intent_id)
        self.assertTrue(trace.binding.allowed, trace.binding.reason)
        self.assertEqual(trace.binding.binding.binding_id, "binding-put")
        self.assertEqual(trace.admission.admission.capability_id, "cap-X")
        self.assertTrue(trace.execution.occurred, trace.execution.reason)

    def test_missing_binding_stops_before_attempt_admission_and_effect(self) -> None:
        f = self.fixture()
        runtime = KernelRuntime(
            f.authority,
            TrustedBindingRegistry((f.git_binding,)),
        )
        before = f.authority.snapshot()
        trace = runtime.run(
            f.request(f.put_intent, f.put_contract, "missing-binding"),
            f.put_operation("must-not-run"),
            authentication_context=f.context,
        )
        after = f.authority.snapshot()
        self.assertTrue(trace.authorization.allowed)
        self.assertFalse(trace.binding.allowed)
        self.assertEqual(trace.binding.reason, "binding_absent")
        self.assertIsNone(trace.start)
        self.assertIsNone(trace.admission)
        self.assertIsNone(trace.execution)
        self.assertEqual(len(after["action_attempts"]), len(before["action_attempts"]))

    def test_exact_target_mismatch_stops_before_attempt(self) -> None:
        f = self.fixture()
        wrong = CapabilityBinding(
            "binding-put-wrong-target",
            f.put_intent.intent_id,
            "cap-X",
            "Y",
            f.g3_adapter,
        )
        runtime = KernelRuntime(f.authority, TrustedBindingRegistry((wrong, f.git_binding)))
        trace = runtime.run(
            f.request(f.put_intent, f.put_contract, "target-mismatch"),
            f.put_operation("must-not-run"),
            authentication_context=f.context,
        )
        self.assertTrue(trace.authorization.allowed)
        self.assertFalse(trace.binding.allowed)
        self.assertEqual(trace.binding.reason, "binding_target_mismatch")
        self.assertIsNone(trace.start)
        self.assertIsNone(trace.admission)
        self.assertIsNone(trace.execution)

    def test_cross_domain_operation_cannot_pivot_authorized_intent_to_other_adapter(self) -> None:
        f = self.fixture()
        trace = f.runtime.run(
            f.request(f.put_intent, f.put_contract, "cross-domain-pivot"),
            f.git_operation("must-not-run"),
            authentication_context=f.context,
        )
        self.assertTrue(trace.authorization.allowed)
        self.assertFalse(trace.binding.allowed)
        self.assertEqual(trace.binding.reason, "binding_operation_mismatch")
        self.assertEqual(trace.binding.binding.binding_id, "binding-put")
        self.assertIsNone(trace.start)
        self.assertIsNone(trace.admission)
        self.assertIsNone(trace.execution)

    def test_duplicate_or_conflicting_bindings_are_rejected_at_construction(self) -> None:
        f = self.fixture()
        same_intent = CapabilityBinding(
            "another-id",
            f.put_intent.intent_id,
            "cap-X",
            "X",
            f.g3_adapter,
        )
        with self.assertRaisesRegex(ValueError, "duplicate_binding_intent"):
            TrustedBindingRegistry((f.put_binding, same_intent))

        same_id = CapabilityBinding(
            f.put_binding.binding_id,
            "intent.other",
            "cap-X",
            "X",
            f.g3_adapter,
        )
        with self.assertRaisesRegex(ValueError, "duplicate_binding_id"):
            TrustedBindingRegistry((f.put_binding, same_id))

    def test_binding_for_ungranted_intent_does_not_create_may(self) -> None:
        f = self.fixture()
        denied_binding = CapabilityBinding(
            "binding-denied",
            f.denied_intent.intent_id,
            "cap-X",
            "X",
            f.g3_adapter,
        )
        runtime = KernelRuntime(
            f.authority,
            TrustedBindingRegistry((f.put_binding, f.git_binding, denied_binding)),
        )
        trace = runtime.run(
            f.request(f.denied_intent, f.denied_contract, "denied-intent"),
            f.put_operation("must-not-run"),
            authentication_context=f.context,
        )
        self.assertFalse(trace.authorization.allowed)
        self.assertEqual(trace.authorization.reason, "authority_absent")
        self.assertIsNone(trace.binding)
        self.assertIsNone(trace.start)
        self.assertIsNone(trace.admission)
        self.assertIsNone(trace.execution)

    def test_registry_and_binding_are_immutable_after_construction(self) -> None:
        f = self.fixture()
        with self.assertRaises(FrozenInstanceError):
            f.registry.bindings = ()
        with self.assertRaises(TypeError):
            f.registry._by_intent[f.put_intent.intent_id] = f.git_binding
        with self.assertRaises(FrozenInstanceError):
            f.put_binding.capability_id = "cap-git"
        public = {name for name in dir(f.registry) if not name.startswith("_")}
        for forbidden in ("add", "register", "remove", "replace", "update"):
            self.assertNotIn(forbidden, public)

    def test_registry_mode_rejects_parallel_fixed_capability_argument(self) -> None:
        f = self.fixture()
        with self.assertRaisesRegex(ValueError, "registry_mode_rejects_fixed_capability"):
            KernelRuntime(f.authority, f.registry, "cap-X")


if __name__ == "__main__":
    unittest.main()
