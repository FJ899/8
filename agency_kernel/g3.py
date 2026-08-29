from __future__ import annotations

import hashlib
import json
import sqlite3
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import FrozenSet, Optional

from .g1 import ActionAttempt
from .g2 import AdmissionResult, OperationAdmission, Kernel as G2Kernel


@dataclass(frozen=True)
class PutIfVersionOperation:
    resource: str
    expected_version: int
    value: str
    possible_effects: Optional[FrozenSet[str]]

    def canonical_bytes(self) -> bytes:
        if not self.resource or "/" in self.resource or "\\" in self.resource or self.resource in {".", ".."}:
            raise ValueError("invalid_resource")
        if not isinstance(self.expected_version, int) or self.expected_version < 0:
            raise ValueError("invalid_expected_version")
        payload = {
            "operation_type": "put_if_version",
            "possible_effects": None if self.possible_effects is None else sorted(self.possible_effects),
            "resource": self.resource,
            "expected_version": self.expected_version,
            "value": self.value,
        }
        return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()

    @property
    def operation_digest(self) -> str:
        return hashlib.sha256(self.canonical_bytes()).hexdigest()


@dataclass(frozen=True)
class PutResult:
    occurred: bool
    reason: str
    resource: str
    before_version: Optional[int] = None
    after_version: Optional[int] = None
    mutation_id: Optional[str] = None
    operation_digest: Optional[str] = None


@dataclass(frozen=True)
class Observation:
    resource: str
    value: Optional[str]
    version: Optional[int]
    mutation_id: Optional[str]
    admission_id: Optional[str]
    operation_digest: Optional[str]
    covered: bool = True
    attribution_ambiguous: bool = False


@dataclass(frozen=True)
class ComplianceResult:
    status: str
    reason: str
    actual_effects: FrozenSet[str]
    possible_effects: FrozenSet[str]


@dataclass(frozen=True)
class AcceptanceResult:
    passed: bool
    reason: str


class Observer:
    def __init__(self, target_db: str | Path):
        self.target_db = str(target_db)

    def observe(self, resource: str, *, covered: bool = True, attribution_ambiguous: bool = False) -> Observation:
        uri = f"file:{Path(self.target_db).resolve()}?mode=ro"
        c = sqlite3.connect(uri, uri=True)
        c.row_factory = sqlite3.Row
        try:
            row = c.execute("SELECT value, version FROM resources WHERE resource=?", (resource,)).fetchone()
            prov = c.execute(
                "SELECT mutation_id,admission_id,operation_digest,after_version,value FROM mutation_provenance WHERE resource=? ORDER BY rowid DESC LIMIT 1",
                (resource,),
            ).fetchone()
            matches = bool(row and prov and int(row["version"]) == int(prov["after_version"]) and row["value"] == prov["value"])
            return Observation(
                resource,
                None if row is None else row["value"],
                None if row is None else int(row["version"]),
                prov["mutation_id"] if matches else None,
                prov["admission_id"] if matches else None,
                prov["operation_digest"] if matches else None,
                covered,
                attribution_ambiguous,
            )
        finally:
            c.close()


class Kernel(G2Kernel):
    def __init__(self, control_db: str | Path, target_db: str | Path, clock=None):
        self.target_db = str(target_db)
        super().__init__(control_db, Path(str(target_db) + ".g2-boundary"), clock=clock)
        with self._connect() as c:
            c.execute("CREATE TABLE IF NOT EXISTS g3_execution_completions(admission_id TEXT PRIMARY KEY REFERENCES operation_admissions(admission_id), mutation_id TEXT NOT NULL, completed_at INTEGER NOT NULL)")
        self._initialize_target_store()

    def _target_connect(self) -> sqlite3.Connection:
        c = sqlite3.connect(self.target_db, timeout=5.0, isolation_level=None, check_same_thread=False)
        c.row_factory = sqlite3.Row
        c.execute("PRAGMA busy_timeout=5000")
        return c

    def _initialize_target_store(self) -> None:
        Path(self.target_db).parent.mkdir(parents=True, exist_ok=True)
        with self._target_connect() as c:
            c.executescript("""
            PRAGMA journal_mode=WAL; PRAGMA synchronous=FULL;
            CREATE TABLE IF NOT EXISTS resources(resource TEXT PRIMARY KEY,value TEXT NOT NULL,version INTEGER NOT NULL);
            CREATE TABLE IF NOT EXISTS mutation_provenance(
              mutation_id TEXT PRIMARY KEY, admission_id TEXT NOT NULL, operation_digest TEXT NOT NULL,
              resource TEXT NOT NULL, before_version INTEGER NOT NULL, after_version INTEGER NOT NULL,
              value TEXT NOT NULL, committed_at INTEGER NOT NULL);
            """)

    @staticmethod
    def possible_effects_for(resource: str) -> FrozenSet[str]:
        return frozenset({f"MODIFY({resource})", f"PROVENANCE({resource})"})

    def has_control_completion(self, admission_id: str) -> bool:
        with self._connect() as c:
            return c.execute("SELECT 1 FROM g3_execution_completions WHERE admission_id=?", (admission_id,)).fetchone() is not None

    def seed_resource(self, resource: str, value: str = "", version: int = 0) -> None:
        with self._target_connect() as c:
            c.execute("INSERT OR REPLACE INTO resources(resource,value,version) VALUES(?,?,?)", (resource, value, version))

    def simulate_unattributed_delta(self, resource: str, value: str, version: int, *, preserve_old_provenance: bool = False) -> None:
        with self._target_connect() as c:
            c.execute("INSERT OR REPLACE INTO resources(resource,value,version) VALUES(?,?,?)", (resource, value, version))
            if not preserve_old_provenance:
                c.execute("DELETE FROM mutation_provenance WHERE resource=?", (resource,))

    def inject_unattributed_delta_for_test(self, resource: str, value: str, version: int) -> None:
        self.simulate_unattributed_delta(resource, value, version)

    def inject_unattributed_delta_preserving_provenance_for_test(self, resource: str, value: str, version: int) -> None:
        self.simulate_unattributed_delta(resource, value, version, preserve_old_provenance=True)

    def admit_put_if_version(self, attempt: ActionAttempt, capability_id: str, operation: PutIfVersionOperation) -> AdmissionResult:
        try:
            canonical = operation.canonical_bytes()
        except (TypeError, ValueError):
            return AdmissionResult(False, "invalid_operation")
        if operation.possible_effects is None:
            return AdmissionResult(False, "unknown_possible_effects")
        if operation.possible_effects != self.possible_effects_for(operation.resource):
            return AdmissionResult(False, "effect_model_mismatch")
        c = self._connect()
        try:
            c.execute("BEGIN IMMEDIATE")
            row = self._attempt_row(c, attempt.attempt_id)
            if row is None:
                c.execute("ROLLBACK"); return AdmissionResult(False, "invalid_attempt")
            actual = (row["authorization_id"], row["principal_id"], row["intent_id"], row["contract_id"])
            claimed = (attempt.authorization_id, attempt.principal_id, attempt.intent_id, attempt.contract_id)
            if actual != claimed:
                c.execute("ROLLBACK"); return AdmissionResult(False, "forged_attempt")
            authority = self._specific_grant_status(c, row["grant_id"], row["principal_id"], row["intent_id"], int(self._clock()))
            if not authority.allowed:
                c.execute("ROLLBACK"); return AdmissionResult(False, authority.reason)
            cap = c.execute("SELECT resource,valid FROM capabilities WHERE capability_id=?", (capability_id,)).fetchone()
            if cap is None:
                c.execute("ROLLBACK"); return AdmissionResult(False, "capability_absent")
            if cap["valid"] is None:
                c.execute("ROLLBACK"); return AdmissionResult(False, "unknown_capability_fact")
            if cap["valid"] != 1:
                c.execute("ROLLBACK"); return AdmissionResult(False, "capability_invalid")
            if cap["resource"] != operation.resource:
                c.execute("ROLLBACK"); return AdmissionResult(False, "capability_resource_mismatch")
            envelope = frozenset(r["effect"] for r in c.execute("SELECT effect FROM effect_envelopes WHERE contract_id=?", (row["contract_id"],)))
            if not operation.possible_effects.issubset(envelope):
                c.execute("ROLLBACK"); return AdmissionResult(False, "effect_envelope_exceeded")
            admission = OperationAdmission(str(uuid.uuid4()), attempt.attempt_id, capability_id, hashlib.sha256(canonical).hexdigest(), canonical)
            c.execute("INSERT INTO operation_admissions(admission_id,attempt_id,capability_id,operation_digest,canonical_operation) VALUES(?,?,?,?,?)",
                      (admission.admission_id, admission.attempt_id, admission.capability_id, admission.operation_digest, canonical))
            c.execute("COMMIT")
            return AdmissionResult(True, "admitted", admission)
        except BaseException:
            if c.in_transaction: c.execute("ROLLBACK")
            raise
        finally:
            c.close()

    @staticmethod
    def _decode_put(canonical: bytes, expected_digest: str):
        digest = hashlib.sha256(canonical).hexdigest()
        if digest != expected_digest:
            return None, "admission_digest_mismatch", digest
        try:
            p = json.loads(canonical.decode())
            if p.get("operation_type") != "put_if_version": raise ValueError
            op = PutIfVersionOperation(str(p["resource"]), int(p["expected_version"]), str(p["value"]), frozenset(p["possible_effects"]))
            if op.canonical_bytes() != canonical: return None, "noncanonical_admitted_operation", digest
            return op, None, digest
        except (KeyError, TypeError, ValueError, UnicodeDecodeError, json.JSONDecodeError):
            return None, "invalid_admitted_operation", digest

    def execute_put_if_version_admission(self, admission_id: str, *, crash_point: Optional[str] = None) -> PutResult:
        c = self._connect()
        try:
            c.execute("BEGIN IMMEDIATE")
            row = c.execute("SELECT operation_digest,canonical_operation FROM operation_admissions WHERE admission_id=?", (admission_id,)).fetchone()
            if row is None:
                c.execute("ROLLBACK"); return PutResult(False, "admission_absent", "")
            if c.execute("SELECT 1 FROM operation_admission_executions WHERE admission_id=?", (admission_id,)).fetchone():
                c.execute("ROLLBACK"); return PutResult(False, "admission_consumed", "")
            op, error, digest = self._decode_put(bytes(row["canonical_operation"]), str(row["operation_digest"]))
            if error:
                c.execute("ROLLBACK"); return PutResult(False, error, "", operation_digest=digest)
            c.execute("INSERT INTO operation_admission_executions(admission_id,executed_at) VALUES(?,?)", (admission_id, int(self._clock())))
            c.execute("COMMIT")
        finally:
            c.close()
        if crash_point == "after_admission_before_mutation":
            return PutResult(False, "crash_after_admission_before_mutation", op.resource, operation_digest=digest)
        t = self._target_connect()
        try:
            t.execute("BEGIN IMMEDIATE")
            current = t.execute("SELECT value,version FROM resources WHERE resource=?", (op.resource,)).fetchone()
            version = 0 if current is None else int(current["version"])
            if version != op.expected_version:
                t.execute("ROLLBACK"); return PutResult(False, "stale_version", op.resource, version, version, operation_digest=digest)
            if crash_point == "before_mutation":
                t.execute("ROLLBACK"); return PutResult(False, "crash_before_mutation", op.resource, version, version, operation_digest=digest)
            after = version + 1
            mutation_id = str(uuid.uuid4())
            if current is None:
                t.execute("INSERT INTO resources(resource,value,version) VALUES(?,?,?)", (op.resource, op.value, after))
            else:
                cur = t.execute("UPDATE resources SET value=?,version=? WHERE resource=? AND version=?", (op.value, after, op.resource, version))
                if cur.rowcount != 1:
                    t.execute("ROLLBACK"); return PutResult(False, "stale_version", op.resource, version, version, operation_digest=digest)
            t.execute("INSERT INTO mutation_provenance(mutation_id,admission_id,operation_digest,resource,before_version,after_version,value,committed_at) VALUES(?,?,?,?,?,?,?,?)",
                      (mutation_id, admission_id, digest, op.resource, version, after, op.value, int(self._clock())))
            t.execute("COMMIT")
        except BaseException:
            if t.in_transaction: t.execute("ROLLBACK")
            raise
        finally:
            t.close()
        if crash_point == "after_mutation_before_control_completion":
            return PutResult(True, "crash_after_mutation_before_control_completion", op.resource, version, after, mutation_id, digest)
        with self._connect() as c:
            c.execute("INSERT INTO g3_execution_completions(admission_id,mutation_id,completed_at) VALUES(?,?,?)", (admission_id, mutation_id, int(self._clock())))
        return PutResult(True, "executed", op.resource, version, after, mutation_id, digest)

    def assess_compliance(self, admission: OperationAdmission, observation: Observation, *, supported_possible_effects: FrozenSet[str]) -> ComplianceResult:
        if not observation.covered:
            return ComplianceResult("INDETERMINATE", "missing_coverage", frozenset(), supported_possible_effects)
        if observation.attribution_ambiguous:
            return ComplianceResult("INDETERMINATE", "ambiguous_attribution", frozenset(), supported_possible_effects)
        if observation.admission_id != admission.admission_id or observation.operation_digest != admission.operation_digest:
            return ComplianceResult("INDETERMINATE", "unresolved_attribution", frozenset(), supported_possible_effects)
        actual = frozenset({f"MODIFY({observation.resource})", f"PROVENANCE({observation.resource})"})
        if not actual.issubset(supported_possible_effects):
            return ComplianceResult("FAIL", "effect_model_unsound", actual, supported_possible_effects)
        return ComplianceResult("PASS", "within_scope", actual, supported_possible_effects)

    @staticmethod
    def did(admission: OperationAdmission, observation: Observation) -> bool:
        return observation.admission_id == admission.admission_id and observation.operation_digest == admission.operation_digest

    @staticmethod
    def within_scope(compliance: ComplianceResult) -> bool:
        return compliance.status == "PASS"

    @staticmethod
    def satisfied(observation: Observation, expected_value: str) -> bool:
        return observation.value == expected_value

    @staticmethod
    def accept(passed: bool, reason: str = "human_or_external_acceptance") -> AcceptanceResult:
        return AcceptanceResult(passed, reason)


class DishonestPrimitive:
    @staticmethod
    def declared_possible_effects() -> FrozenSet[str]:
        return frozenset({"A"})

    @staticmethod
    def execute(target_db: str | Path) -> FrozenSet[str]:
        c = sqlite3.connect(str(target_db))
        try:
            c.execute("INSERT OR REPLACE INTO resources(resource,value,version) VALUES('A','mutant-A',1)")
            c.execute("INSERT OR REPLACE INTO resources(resource,value,version) VALUES('B','mutant-B',1)")
            c.commit()
        finally:
            c.close()
        return frozenset({"A", "B"})

    @classmethod
    def diagnostic(cls, actual: Optional[FrozenSet[str]] = None) -> ComplianceResult:
        actual_effects = actual if actual is not None else frozenset({"A", "B"})
        return ComplianceResult("FAIL", "effect_model_unsound", actual_effects, cls.declared_possible_effects())
