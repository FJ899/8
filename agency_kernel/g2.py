from __future__ import annotations

import hashlib
import json
import sqlite3
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import FrozenSet, Optional

from .g1 import ActionAttempt, Kernel as G1Kernel


@dataclass(frozen=True)
class Capability:
    capability_id: str
    resource: str
    valid: Optional[bool] = True


@dataclass(frozen=True)
class TechnicalOperation:
    operation_type: str
    resource: str
    value: str
    possible_effects: Optional[FrozenSet[str]]

    def canonical_bytes(self) -> bytes:
        if self.operation_type != "boundary_mutation":
            raise ValueError("unsupported_operation")
        if not self.resource or "/" in self.resource or "\\" in self.resource or self.resource in {".", ".."}:
            raise ValueError("invalid_resource")
        effects = None if self.possible_effects is None else sorted(self.possible_effects)
        payload = {
            "operation_type": self.operation_type,
            "possible_effects": effects,
            "resource": self.resource,
            "value": self.value,
        }
        return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

    @property
    def operation_digest(self) -> str:
        return hashlib.sha256(self.canonical_bytes()).hexdigest()


@dataclass(frozen=True)
class OperationAdmission:
    admission_id: str
    attempt_id: str
    capability_id: str
    operation_digest: str
    canonical_operation: bytes


@dataclass(frozen=True)
class AdmissionResult:
    allowed: bool
    reason: str
    admission: Optional[OperationAdmission] = None


@dataclass(frozen=True)
class ExecutionResult:
    allowed: bool
    reason: str
    resource: Optional[str] = None
    operation_digest: Optional[str] = None


class Kernel(G1Kernel):
    """G2 extension implementing exact-operation admission and one-shot boundary execution."""

    def __init__(self, db_path: str | Path, target_root: str | Path, clock=None):
        self.target_root = Path(target_root)
        self.target_root.mkdir(parents=True, exist_ok=True)
        super().__init__(db_path, clock=clock)
        self._initialize_g2_schema()

    def _initialize_g2_schema(self) -> None:
        with self._connect() as c:
            c.executescript(
                """
                CREATE TABLE IF NOT EXISTS capabilities (
                    capability_id TEXT PRIMARY KEY,
                    resource TEXT NOT NULL,
                    valid INTEGER NULL CHECK (valid IN (0, 1) OR valid IS NULL)
                );
                CREATE TABLE IF NOT EXISTS effect_envelopes (
                    contract_id TEXT NOT NULL,
                    effect TEXT NOT NULL,
                    PRIMARY KEY(contract_id, effect),
                    FOREIGN KEY(contract_id) REFERENCES effect_contracts(contract_id)
                );
                CREATE TABLE IF NOT EXISTS operation_admissions (
                    admission_id TEXT PRIMARY KEY,
                    attempt_id TEXT NOT NULL REFERENCES action_attempts(attempt_id),
                    capability_id TEXT NOT NULL REFERENCES capabilities(capability_id),
                    operation_digest TEXT NOT NULL,
                    canonical_operation BLOB NOT NULL
                );
                CREATE TABLE IF NOT EXISTS operation_admission_executions (
                    admission_id TEXT PRIMARY KEY REFERENCES operation_admissions(admission_id),
                    executed_at INTEGER NOT NULL
                );
                """
            )

    def add_capability(self, capability: Capability) -> None:
        with self._connect() as c:
            c.execute(
                "INSERT INTO capabilities(capability_id, resource, valid) VALUES (?, ?, ?)",
                (capability.capability_id, capability.resource, self._db_bool(capability.valid)),
            )

    def set_capability_valid(self, capability_id: str, valid: Optional[bool]) -> None:
        self._update_one(
            "UPDATE capabilities SET valid = ? WHERE capability_id = ?",
            (self._db_bool(valid), capability_id),
        )

    def set_authorized_effect_envelope(self, contract_id: str, effects: FrozenSet[str]) -> None:
        with self._connect() as c:
            c.execute("DELETE FROM effect_envelopes WHERE contract_id = ?", (contract_id,))
            for effect in sorted(effects):
                c.execute(
                    "INSERT INTO effect_envelopes(contract_id, effect) VALUES (?, ?)",
                    (contract_id, effect),
                )

    def _attempt_row(self, c: sqlite3.Connection, attempt_id: str):
        return c.execute(
            """
            SELECT a.attempt_id, a.authorization_id, a.principal_id, a.intent_id, a.contract_id,
                   aa.grant_id
            FROM action_attempts AS a
            JOIN attempt_started AS s ON s.attempt_id = a.attempt_id
            JOIN action_authorizations AS aa ON aa.authorization_id = a.authorization_id
            WHERE a.attempt_id = ?
            """,
            (attempt_id,),
        ).fetchone()

    def admit_operation(self, attempt: ActionAttempt, capability_id: str, operation: TechnicalOperation) -> AdmissionResult:
        try:
            canonical = operation.canonical_bytes()
        except (TypeError, ValueError):
            return AdmissionResult(False, "invalid_operation")

        if operation.possible_effects is None:
            return AdmissionResult(False, "unknown_possible_effects")

        expected_effect = f"MODIFY({operation.resource})"
        if operation.possible_effects != frozenset({expected_effect}):
            return AdmissionResult(False, "nonconservative_boundary_effect_declaration")

        c = self._connect()
        try:
            c.execute("BEGIN IMMEDIATE")
            row = self._attempt_row(c, attempt.attempt_id)
            if row is None:
                c.execute("ROLLBACK")
                return AdmissionResult(False, "invalid_attempt")
            if (
                row["authorization_id"] != attempt.authorization_id
                or row["principal_id"] != attempt.principal_id
                or row["intent_id"] != attempt.intent_id
                or row["contract_id"] != attempt.contract_id
            ):
                c.execute("ROLLBACK")
                return AdmissionResult(False, "forged_attempt")

            authority = self._specific_grant_status(
                c,
                row["grant_id"],
                row["principal_id"],
                row["intent_id"],
                int(self._clock()),
            )
            if not authority.allowed:
                c.execute("ROLLBACK")
                return AdmissionResult(False, authority.reason)

            cap = c.execute(
                "SELECT resource, valid FROM capabilities WHERE capability_id = ?",
                (capability_id,),
            ).fetchone()
            if cap is None:
                c.execute("ROLLBACK")
                return AdmissionResult(False, "capability_absent")
            if cap["valid"] is None:
                c.execute("ROLLBACK")
                return AdmissionResult(False, "unknown_capability_fact")
            if cap["valid"] != 1:
                c.execute("ROLLBACK")
                return AdmissionResult(False, "capability_invalid")
            if cap["resource"] != operation.resource:
                c.execute("ROLLBACK")
                return AdmissionResult(False, "capability_resource_mismatch")

            envelope = frozenset(
                r["effect"]
                for r in c.execute(
                    "SELECT effect FROM effect_envelopes WHERE contract_id = ?",
                    (row["contract_id"],),
                ).fetchall()
            )
            if not operation.possible_effects.issubset(envelope):
                c.execute("ROLLBACK")
                return AdmissionResult(False, "effect_envelope_exceeded")

            admission = OperationAdmission(
                str(uuid.uuid4()),
                attempt.attempt_id,
                capability_id,
                hashlib.sha256(canonical).hexdigest(),
                canonical,
            )
            c.execute(
                """
                INSERT INTO operation_admissions(
                    admission_id, attempt_id, capability_id, operation_digest, canonical_operation
                ) VALUES (?, ?, ?, ?, ?)
                """,
                (
                    admission.admission_id,
                    admission.attempt_id,
                    admission.capability_id,
                    admission.operation_digest,
                    admission.canonical_operation,
                ),
            )
            c.execute("COMMIT")
            return AdmissionResult(True, "admitted", admission)
        except BaseException:
            if c.in_transaction:
                c.execute("ROLLBACK")
            raise
        finally:
            c.close()

    @staticmethod
    def _decode_admitted_operation(canonical: bytes, expected_digest: str):
        digest = hashlib.sha256(canonical).hexdigest()
        if digest != expected_digest:
            return None, None, None, "admission_digest_mismatch", digest
        try:
            payload = json.loads(canonical.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            return None, None, None, "invalid_admitted_operation", digest
        if payload.get("operation_type") != "boundary_mutation":
            return None, None, None, "invalid_admitted_operation", digest
        resource = payload.get("resource")
        value = payload.get("value")
        effects = payload.get("possible_effects")
        if not isinstance(resource, str) or not isinstance(value, str):
            return None, None, None, "invalid_admitted_operation", digest
        if effects != [f"MODIFY({resource})"]:
            return None, None, None, "invalid_admitted_operation", digest
        if not resource or "/" in resource or "\\" in resource or resource in {".", ".."}:
            return None, None, None, "invalid_admitted_operation", digest
        return resource, value, effects, None, digest

    def execute_admission(self, admission_id: str) -> ExecutionResult:
        c = self._connect()
        try:
            c.execute("BEGIN IMMEDIATE")
            row = c.execute(
                "SELECT operation_digest, canonical_operation FROM operation_admissions WHERE admission_id = ?",
                (admission_id,),
            ).fetchone()
            if row is None:
                c.execute("ROLLBACK")
                return ExecutionResult(False, "admission_absent")
            if c.execute(
                "SELECT 1 FROM operation_admission_executions WHERE admission_id = ?",
                (admission_id,),
            ).fetchone() is not None:
                c.execute("ROLLBACK")
                return ExecutionResult(False, "admission_consumed")

            canonical = bytes(row["canonical_operation"])
            resource, value, _effects, error, digest = self._decode_admitted_operation(
                canonical, str(row["operation_digest"])
            )
            if error is not None:
                c.execute("ROLLBACK")
                return ExecutionResult(False, error, operation_digest=digest)

            c.execute(
                "INSERT INTO operation_admission_executions(admission_id, executed_at) VALUES (?, ?)",
                (admission_id, int(self._clock())),
            )
            c.execute("COMMIT")
        except BaseException:
            if c.in_transaction:
                c.execute("ROLLBACK")
            raise
        finally:
            c.close()

        target = self.target_root / resource
        try:
            target.write_text(value, encoding="utf-8")
        except (OSError, ValueError):
            return ExecutionResult(False, "effect_failed", resource, digest)
        return ExecutionResult(True, "executed", resource, digest)
