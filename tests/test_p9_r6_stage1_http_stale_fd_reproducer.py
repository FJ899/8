from __future__ import annotations

import os
import sqlite3
import tempfile
import unittest
from pathlib import Path

from agency_kernel.http_cas_provider import (
    _apply_provider_cas,
    initialize_http_cas_provider,
    read_http_cas_resource_for_test,
    seed_http_cas_resource,
)
from agency_kernel.http_cas_types import HttpCasOperation
from agency_kernel.target_instance import filesystem_target_instance_id


class P9R6Stage1HttpStaleFdCounterexample(unittest.TestCase):
    @staticmethod
    def _sqlite_clone(source: Path, destination: Path) -> None:
        with sqlite3.connect(str(source)) as src, sqlite3.connect(str(destination)) as dst:
            src.backup(dst)

    def test_stale_t1_fd_must_not_authenticate_connection_opened_on_replacement_t2(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "provider.sqlite"
            replacement = Path(td) / "replacement.sqlite"
            initialize_http_cas_provider(path, "provider-local")
            seed_http_cas_resource(path, "X", "initial", 0)
            self._sqlite_clone(path, replacement)

            expected_t1 = filesystem_target_instance_id(
                path,
                namespace="http-cas-provider-store:provider-local",
            )
            stale_t1_fd = os.open(path, os.O_RDONLY)
            try:
                # Remove the historical pathname while keeping the old T1 object
                # alive through stale_t1_fd, then install compatible T2 at the
                # exact same pathname. /proc/self/fd/<stale> names the deleted T1
                # using that pathname plus " (deleted)"; the frozen P9-R5 helper
                # strips that suffix and can mistake it for the new connection's
                # backing file.
                path.unlink()
                replacement.replace(path)
                current_t2 = filesystem_target_instance_id(
                    path,
                    namespace="http-cas-provider-store:provider-local",
                )
                self.assertNotEqual(current_t2, expected_t1)

                effects = frozenset({"MODIFY(X)", "PROVENANCE(X)"})
                operation = HttpCasOperation("X", 0, "mutated-on-t2", effects)
                receipt = _apply_provider_cas(
                    path,
                    "p9-r6-stale-fd-admission",
                    operation.operation_digest,
                    operation,
                    expected_target_instance_id=expected_t1,
                )

                # Security requirement. On frozen P9-R5 this is expected to FAIL:
                # the unrelated stale T1 FD authenticates the T2 connection and
                # the protected CAS commits on T2.
                self.assertNotEqual(
                    receipt["status"],
                    "committed",
                    "stale T1 FD authenticated sqlite3.Connection actually opened on replacement T2",
                )
                self.assertEqual(
                    read_http_cas_resource_for_test(path, "X"),
                    ("initial", 0),
                )
            finally:
                os.close(stale_t1_fd)


if __name__ == "__main__":
    unittest.main()
