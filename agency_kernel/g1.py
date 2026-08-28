from __future__ import annotations

import sqlite3
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional


@dataclass(frozen=True)
class Principal:
    principal_id: str


@dataclass(frozen=True)
class AuthorityRoot:
    root_id: str
    active: Optional[bool] = True


@dataclass(frozen=True)
class AuthorityGrant:
    grant_id: str
    root_id: str
    principal_id: str
    intent_id: str
    validity: Optional[bool] = True
    revoked: Optional[bool] = False
    expires_at: Optional[int] = None


@dataclass(frozen=True)
class EffectIntent:
    intent_id: str
    name: str


@dataclass(frozen=True)
class EffectContract:
    contract_id: str
    intent_id: str


@dataclass(frozen=True)
class ActionRequest:
    request_id: str
    intent_id: str
    contract_id: str
    declared_principal: Optional[str] = None
    untrusted_authority: Any = None


@dataclass(frozen=True)
class ActionAuthorization:
    authorization_id: str
    request_id: str
    principal_id: str
    grant_id: str
    intent_id: str
    contract_id: str
    issued_at: int


@dataclass(frozen=True)
class AuthorizationConsumed:
    authorization_id: str
    attempt_id: str
    consumed_at: int


@dataclass(frozen=True)
class ActionAttempt:
    attempt_id: str
    authorization_id: str
    principal_id: str
    intent_id: str
    contract_id: str


@dataclass(frozen=True)
class AttemptStarted:
    attempt_id: str
    started_at: int


@dataclass(frozen=True)
class MayResult:
    allowed: bool
    reason: str
    grant_id: Optional[str] = None


@dataclass(frozen=True)
class AuthorizationResult:
    allowed: bool
    reason: str
    authorization: Optional[ActionAuthorization] = None


@dataclass(frozen=True)
class StartResult:
    allowed: bool
    reason: str
    attempt: Optional[ActionAttempt] = None
    consumed: Optional[AuthorizationConsumed] = None
    started: Optional[AttemptStarted] = None


class Kernel:
    """G1-only authority kernel with a durable SQLite control ledger.

    `trusted_principal` is the abstract trusted authenticated-context input
    permitted by G1. Request-declared identity and authority-shaped request data
    are never consulted as authoritative state.
    """

    _SNAPSHOT_TABLES = (
        "principals",
        "authority_roots",
        "effect_intents",
        "effect_contracts",
        "authority_grants",
        "action_authorizations",
        "authorization_consumed",
        "action_attempts",
        "attempt_started",
    )

    def __init__(self, db_path: str | Path, clock: Callable[[], int] | None = None):
        self.db_path = str(db_path)
        self._clock = clock or (lambda: int(time.time()))
        self._initialize_schema()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(
            self.db_path,
            timeout=5.0,
            isolation_level=None,
            check_same_thread=False,
        )
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("PRAGMA busy_timeout = 5000")
        return connection

    def _initialize_schema(self) -> None:
        Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
        connection = self._connect()
        try:
            connection.executescript(
                """
                PRAGMA journal_mode = WAL;
                PRAGMA synchronous = FULL;

                CREATE TABLE IF NOT EXISTS principals (
                    principal_id TEXT PRIMARY KEY
                );

                CREATE TABLE IF NOT EXISTS authority_roots (
                    root_id TEXT PRIMARY KEY,
                    active INTEGER NULL CHECK (active IN (0, 1) OR active IS NULL)
                );

                CREATE TABLE IF NOT EXISTS effect_intents (
                    intent_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS effect_contracts (
                    contract_id TEXT PRIMARY KEY,
                    intent_id TEXT NOT NULL REFERENCES effect_intents(intent_id)
                );

                CREATE TABLE IF NOT EXISTS authority_grants (
                    grant_id TEXT PRIMARY KEY,
                    root_id TEXT NOT NULL REFERENCES authority_roots(root_id),
                    principal_id TEXT NOT NULL REFERENCES principals(principal_id),
                    intent_id TEXT NOT NULL REFERENCES effect_intents(intent_id),
                    validity INTEGER NULL CHECK (validity IN (0, 1) OR validity IS NULL),
                    revoked INTEGER NULL CHECK (revoked IN (0, 1) OR revoked IS NULL),
                    expires_at INTEGER NULL
                );

                CREATE TABLE IF NOT EXISTS action_authorizations (
                    authorization_id TEXT PRIMARY KEY,
                    request_id TEXT NOT NULL,
                    principal_id TEXT NOT NULL REFERENCES principals(principal_id),
                    grant_id TEXT NOT NULL REFERENCES authority_grants(grant_id),
                    intent_id TEXT NOT NULL REFERENCES effect_intents(intent_id),
                    contract_id TEXT NOT NULL REFERENCES effect_contracts(contract_id),
                    issued_at INTEGER NOT NULL
                );

                CREATE TABLE IF NOT EXISTS authorization_consumed (
                    authorization_id TEXT PRIMARY KEY REFERENCES action_authorizations(authorization_id),
                    attempt_id TEXT NOT NULL UNIQUE,
                    consumed_at INTEGER NOT NULL
                );

                CREATE TABLE IF NOT EXISTS action_attempts (
                    attempt_id TEXT PRIMARY KEY,
                    authorization_id TEXT NOT NULL UNIQUE REFERENCES action_authorizations(authorization_id),
                    principal_id TEXT NOT NULL REFERENCES principals(principal_id),
                    intent_id TEXT NOT NULL REFERENCES effect_intents(intent_id),
                    contract_id TEXT NOT NULL REFERENCES effect_contracts(contract_id)
                );

                CREATE TABLE IF NOT EXISTS attempt_started (
                    attempt_id TEXT PRIMARY KEY REFERENCES action_attempts(attempt_id),
                    started_at INTEGER NOT NULL
                );
                """
            )
        finally:
            connection.close()

    @staticmethod
    def _db_bool(value: Optional[bool]) -> Optional[int]:
        if value is None:
            return None
        return 1 if value else 0

    def add_principal(self, principal: Principal) -> None:
        connection = self._connect()
        try:
            connection.execute(
                "INSERT INTO principals(principal_id) VALUES (?)",
                (principal.principal_id,),
            )
        finally:
            connection.close()

    def add_authority_root(self, root: AuthorityRoot) -> None:
        connection = self._connect()
        try:
            connection.execute(
                "INSERT INTO authority_roots(root_id, active) VALUES (?, ?)",
                (root.root_id, self._db_bool(root.active)),
            )
        finally:
            connection.close()

    def add_effect_intent(self, intent: EffectIntent) -> None:
        connection = self._connect()
        try:
            connection.execute(
                "INSERT INTO effect_intents(intent_id, name) VALUES (?, ?)",
                (intent.intent_id, intent.name),
            )
        finally:
            connection.close()

    def add_effect_contract(self, contract: EffectContract) -> None:
        connection = self._connect()
        try:
            connection.execute(
                "INSERT INTO effect_contracts(contract_id, intent_id) VALUES (?, ?)",
                (contract.contract_id, contract.intent_id),
            )
        finally:
            connection.close()

    def add_authority_grant(self, grant: AuthorityGrant) -> None:
        connection = self._connect()
        try:
            connection.execute(
                """
                INSERT INTO authority_grants(
                    grant_id, root_id, principal_id, intent_id,
                    validity, revoked, expires_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    grant.grant_id,
                    grant.root_id,
                    grant.principal_id,
                    grant.intent_id,
                    self._db_bool(grant.validity),
                    self._db_bool(grant.revoked),
                    grant.expires_at,
                ),
            )
        finally:
            connection.close()

    def set_grant_validity(self, grant_id: str, validity: Optional[bool]) -> None:
        self._update_one(
            "UPDATE authority_grants SET validity = ? WHERE grant_id = ?",
            (self._db_bool(validity), grant_id),
        )

    def set_grant_revoked(self, grant_id: str, revoked: Optional[bool]) -> None:
        self._update_one(
            "UPDATE authority_grants SET revoked = ? WHERE grant_id = ?",
            (self._db_bool(revoked), grant_id),
        )

    def set_grant_expiration(self, grant_id: str, expires_at: Optional[int]) -> None:
        self._update_one(
            "UPDATE authority_grants SET expires_at = ? WHERE grant_id = ?",
            (expires_at, grant_id),
        )

    def set_root_active(self, root_id: str, active: Optional[bool]) -> None:
        self._update_one(
            "UPDATE authority_roots SET active = ? WHERE root_id = ?",
            (self._db_bool(active), root_id),
        )

    def _update_one(self, sql: str, parameters: tuple[Any, ...]) -> None:
        connection = self._connect()
        try:
            cursor = connection.execute(sql, parameters)
            if cursor.rowcount != 1:
                raise KeyError("trusted state object not found")
        finally:
            connection.close()

    def may(self, trusted_principal: Principal, request: ActionRequest) -> MayResult:
        connection = self._connect()
        try:
            return self._may_on_connection(
                connection,
                trusted_principal,
                request,
                int(self._clock()),
            )
        finally:
            connection.close()

    def _may_on_connection(
        self,
        connection: sqlite3.Connection,
        trusted_principal: Principal,
        request: ActionRequest,
        now: int,
    ) -> MayResult:
        principal = connection.execute(
            "SELECT principal_id FROM principals WHERE principal_id = ?",
            (trusted_principal.principal_id,),
        ).fetchone()
        if principal is None:
            return MayResult(False, "unknown_trusted_principal")

        intent = connection.execute(
            "SELECT intent_id FROM effect_intents WHERE intent_id = ?",
            (request.intent_id,),
        ).fetchone()
        if intent is None:
            return MayResult(False, "unknown_effect_intent")

        contract = connection.execute(
            "SELECT intent_id FROM effect_contracts WHERE contract_id = ?",
            (request.contract_id,),
        ).fetchone()
        if contract is None or contract["intent_id"] != request.intent_id:
            return MayResult(False, "unknown_or_mismatched_effect_contract")

        rows = connection.execute(
            """
            SELECT
                g.grant_id,
                g.validity,
                g.revoked,
                g.expires_at,
                r.active AS root_active
            FROM authority_grants AS g
            JOIN authority_roots AS r ON r.root_id = g.root_id
            WHERE g.principal_id = ? AND g.intent_id = ?
            ORDER BY g.grant_id
            """,
            (trusted_principal.principal_id, request.intent_id),
        ).fetchall()

        if not rows:
            return MayResult(False, "authority_absent")

        saw_unknown = False
        saw_invalid = False
        saw_expired = False
        saw_revoked = False
        for row in rows:
            if (
                row["root_active"] is None
                or row["validity"] is None
                or row["revoked"] is None
            ):
                saw_unknown = True
                continue
            if row["root_active"] != 1 or row["validity"] != 1:
                saw_invalid = True
                continue
            if row["revoked"] != 0:
                saw_revoked = True
                continue
            if row["expires_at"] is not None and now >= row["expires_at"]:
                saw_expired = True
                continue
            return MayResult(True, "may", row["grant_id"])

        if saw_unknown:
            return MayResult(False, "unknown_authority_fact")
        if saw_revoked:
            return MayResult(False, "authority_revoked")
        if saw_expired:
            return MayResult(False, "authority_expired")
        if saw_invalid:
            return MayResult(False, "authority_invalid")
        return MayResult(False, "authority_absent")

    def authorize(
        self,
        request: ActionRequest,
        *,
        trusted_principal: Principal,
    ) -> AuthorizationResult:
        connection = self._connect()
        try:
            connection.execute("BEGIN IMMEDIATE")
            now = int(self._clock())
            decision = self._may_on_connection(
                connection,
                trusted_principal,
                request,
                now,
            )
            if not decision.allowed or decision.grant_id is None:
                connection.execute("ROLLBACK")
                return AuthorizationResult(False, decision.reason)

            authorization = ActionAuthorization(
                authorization_id=str(uuid.uuid4()),
                request_id=request.request_id,
                principal_id=trusted_principal.principal_id,
                grant_id=decision.grant_id,
                intent_id=request.intent_id,
                contract_id=request.contract_id,
                issued_at=now,
            )
            connection.execute(
                """
                INSERT INTO action_authorizations(
                    authorization_id, request_id, principal_id, grant_id,
                    intent_id, contract_id, issued_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    authorization.authorization_id,
                    authorization.request_id,
                    authorization.principal_id,
                    authorization.grant_id,
                    authorization.intent_id,
                    authorization.contract_id,
                    authorization.issued_at,
                ),
            )
            connection.execute("COMMIT")
            return AuthorizationResult(True, "authorized", authorization)
        except BaseException:
            if connection.in_transaction:
                connection.execute("ROLLBACK")
            raise
        finally:
            connection.close()

    def start_attempt(self, authorization: ActionAuthorization) -> StartResult:
        connection = self._connect()
        try:
            connection.execute("BEGIN IMMEDIATE")
            now = int(self._clock())

            if not isinstance(authorization, ActionAuthorization):
                connection.execute("ROLLBACK")
                return StartResult(False, "forged_authorization")

            row = connection.execute(
                """
                SELECT authorization_id, request_id, principal_id, grant_id,
                       intent_id, contract_id, issued_at
                FROM action_authorizations
                WHERE authorization_id = ?
                """,
                (authorization.authorization_id,),
            ).fetchone()
            if row is None or not self._authorization_matches(row, authorization):
                connection.execute("ROLLBACK")
                return StartResult(False, "forged_authorization")

            consumed = connection.execute(
                "SELECT 1 FROM authorization_consumed WHERE authorization_id = ?",
                (authorization.authorization_id,),
            ).fetchone()
            if consumed is not None:
                connection.execute("ROLLBACK")
                return StartResult(False, "authorization_consumed")

            authority = self._specific_grant_status(
                connection,
                authorization.grant_id,
                authorization.principal_id,
                authorization.intent_id,
                now,
            )
            if not authority.allowed:
                connection.execute("ROLLBACK")
                return StartResult(False, authority.reason)

            contract = connection.execute(
                "SELECT intent_id FROM effect_contracts WHERE contract_id = ?",
                (authorization.contract_id,),
            ).fetchone()
            if contract is None or contract["intent_id"] != authorization.intent_id:
                connection.execute("ROLLBACK")
                return StartResult(False, "unknown_start_precondition")

            attempt_id = str(uuid.uuid4())
            consumed_record = AuthorizationConsumed(
                authorization_id=authorization.authorization_id,
                attempt_id=attempt_id,
                consumed_at=now,
            )
            attempt = ActionAttempt(
                attempt_id=attempt_id,
                authorization_id=authorization.authorization_id,
                principal_id=authorization.principal_id,
                intent_id=authorization.intent_id,
                contract_id=authorization.contract_id,
            )
            started = AttemptStarted(attempt_id=attempt_id, started_at=now)

            connection.execute(
                """
                INSERT INTO authorization_consumed(authorization_id, attempt_id, consumed_at)
                VALUES (?, ?, ?)
                """,
                (
                    consumed_record.authorization_id,
                    consumed_record.attempt_id,
                    consumed_record.consumed_at,
                ),
            )
            connection.execute(
                """
                INSERT INTO action_attempts(
                    attempt_id, authorization_id, principal_id, intent_id, contract_id
                ) VALUES (?, ?, ?, ?, ?)
                """,
                (
                    attempt.attempt_id,
                    attempt.authorization_id,
                    attempt.principal_id,
                    attempt.intent_id,
                    attempt.contract_id,
                ),
            )
            connection.execute(
                "INSERT INTO attempt_started(attempt_id, started_at) VALUES (?, ?)",
                (started.attempt_id, started.started_at),
            )
            connection.execute("COMMIT")
            return StartResult(True, "attempt_started", attempt, consumed_record, started)
        except sqlite3.IntegrityError:
            if connection.in_transaction:
                connection.execute("ROLLBACK")
            return StartResult(False, "authorization_consumed")
        except BaseException:
            if connection.in_transaction:
                connection.execute("ROLLBACK")
            raise
        finally:
            connection.close()

    @staticmethod
    def _authorization_matches(
        row: sqlite3.Row,
        authorization: ActionAuthorization,
    ) -> bool:
        return (
            row["authorization_id"] == authorization.authorization_id
            and row["request_id"] == authorization.request_id
            and row["principal_id"] == authorization.principal_id
            and row["grant_id"] == authorization.grant_id
            and row["intent_id"] == authorization.intent_id
            and row["contract_id"] == authorization.contract_id
            and row["issued_at"] == authorization.issued_at
        )

    def _specific_grant_status(
        self,
        connection: sqlite3.Connection,
        grant_id: str,
        principal_id: str,
        intent_id: str,
        now: int,
    ) -> MayResult:
        row = connection.execute(
            """
            SELECT g.validity, g.revoked, g.expires_at, r.active AS root_active
            FROM authority_grants AS g
            JOIN authority_roots AS r ON r.root_id = g.root_id
            WHERE g.grant_id = ? AND g.principal_id = ? AND g.intent_id = ?
            """,
            (grant_id, principal_id, intent_id),
        ).fetchone()
        if row is None:
            return MayResult(False, "authority_absent")
        if (
            row["root_active"] is None
            or row["validity"] is None
            or row["revoked"] is None
        ):
            return MayResult(False, "unknown_authority_fact")
        if row["root_active"] != 1 or row["validity"] != 1:
            return MayResult(False, "authority_invalid")
        if row["revoked"] != 0:
            return MayResult(False, "authority_revoked")
        if row["expires_at"] is not None and now >= row["expires_at"]:
            return MayResult(False, "authority_expired")
        return MayResult(True, "may", grant_id)

    def snapshot(self) -> Dict[str, List[Dict[str, Any]]]:
        connection = self._connect()
        try:
            snapshot: Dict[str, List[Dict[str, Any]]] = {}
            for table in self._SNAPSHOT_TABLES:
                rows = connection.execute(f"SELECT * FROM {table} ORDER BY rowid").fetchall()
                snapshot[table] = [dict(row) for row in rows]
            return snapshot
        finally:
            connection.close()
