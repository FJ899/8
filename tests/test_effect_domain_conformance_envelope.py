from __future__ import annotations

import unittest

from agency_kernel.g4 import PROTECTED_REF_DEFAULT
from tests.test_effect_domain_conformance import DOMAIN_FACTORIES


class EffectEnvelopeConformanceTests(unittest.TestCase):
    def test_authorized_effect_envelope_must_cover_exact_domain_effect_model(self) -> None:
        for factory in DOMAIN_FACTORIES:
            with self.subTest(domain=factory.name):
                domain = factory()
                self.addCleanup(domain.close)

                if domain.name == "g3-versioned-store":
                    restricted = frozenset({"MODIFY(X)"})
                elif domain.name == "g4-sanitized-git":
                    restricted = frozenset({domain.kernel.ref_effect(PROTECTED_REF_DEFAULT)})
                else:
                    self.fail(f"unmapped_domain:{domain.name}")

                domain.kernel.set_authorized_effect_envelope(
                    domain.contract.contract_id,
                    restricted,
                )
                result = domain.admit(domain.operation("after"))
                self.assertFalse(result.allowed)
                self.assertEqual(result.reason, "effect_envelope_exceeded")


if __name__ == "__main__":
    unittest.main()
