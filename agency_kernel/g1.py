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
class AuthenticationContext:
    context_id: str


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
    """G1-only authority kernel with a durable SQLite control ledger."""

    _SNAPSHOT_TABLES = (
        "principals", "authentication_contexts", "authority_roots",
        "effect_intents", "effect_contracts", "authority_grants",
        "action_authorizations", "authorization_consumed", "action_attempts",
        "attempt_started",
    )

    def __init__(self, db_path: str | Path, clock: Callable[[], int] | None = None):
        self.db_path = str(db_path)
        self._clock = clock or (lambda: int(time.time()))
        self._trusted_contexts: Dict[int, AuthenticationContext] = {}
        self._initialize_schema()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.db_path, timeout=5.0, isolation_level=None, check_same_thread=False)
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("PRAGMA busy_timeout = 5000")
        return connection

    def _initialize_schema(self) -> None:
        Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
        connection = self._connect()
        try:
            connection.executescript("""
                PRAGMA journal_mode = WAL;
                PRAGMA synchronous = FULL;
                CREATE TABLE IF NOT EXISTS principals (principal_id TEXT PRIMARY KEY);
                CREATE TABLE IF NOT EXISTS authentication_contexts (
                    context_id TEXT PRIMARY KEY,
                    principal_id TEXT NOT NULL REFERENCES principals(principal_id),
                    valid INTEGER NULL CHECK (valid IN (0, 1) OR valid IS NULL));
                CREATE TABLE IF NOT EXISTS authority_roots (
                    root_id TEXT PRIMARY KEY,
                    active INTEGER NULL CHECK (active IN (0, 1) OR active IS NULL));
                CREATE TABLE IF NOT EXISTS effect_intents (
                    intent_id TEXT PRIMARY KEY, name TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS effect_contracts (
                    contract_id TEXT PRIMARY KEY,
                    intent_id TEXT NOT NULL REFERENCES effect_intents(intent_id));
                CREATE TABLE IF NOT EXISTS authority_grants (
                    grant_id TEXT PRIMARY KEY,
                    root_id TEXT NOT NULL REFERENCES authority_roots(root_id),
                    principal_id TEXT NOT NULL REFERENCES principals(principal_id),
                    intent_id TEXT NOT NULL REFERENCES effect_intents(intent_id),
                    validity INTEGER NULL CHECK (validity IN (0, 1) OR validity IS NULL),
                    revoked INTEGER NULL CHECK (revoked IN (0, 1) OR revoked IS NULL),
                    expires_at INTEGER NULL);
                CREATE TABLE IF NOT EXISTS action_authorizations (
                    authorization_id TEXT PRIMARY KEY, request_id TEXT NOT NULL,
                    principal_id TEXT NOT NULL REFERENCES principals(principal_id),
                    grant_id TEXT NOT NULL REFERENCES authority_grants(grant_id),
                    intent_id TEXT NOT NULL REFERENCES effect_intents(intent_id),
                    contract_id TEXT NOT NULL REFERENCES effect_contracts(contract_id),
                    issued_at INTEGER NOT NULL);
                CREATE TABLE IF NOT EXISTS authorization_consumed (
                    authorization_id TEXT PRIMARY KEY REFERENCES action_authorizations(authorization_id),
                    attempt_id TEXT NOT NULL UNIQUE, consumed_at INTEGER NOT NULL);
                CREATE TABLE IF NOT EXISTS action_attempts (
                    attempt_id TEXT PRIMARY KEY,
                    authorization_id TEXT NOT NULL UNIQUE REFERENCES action_authorizations(authorization_id),
                    principal_id TEXT NOT NULL REFERENCES principals(principal_id),
                    intent_id TEXT NOT NULL REFERENCES effect_intents(intent_id),
                    contract_id TEXT NOT NULL REFERENCES effect_contracts(contract_id));
                CREATE TABLE IF NOT EXISTS attempt_started (
                    attempt_id TEXT PRIMARY KEY REFERENCES action_attempts(attempt_id),
                    started_at INTEGER NOT NULL);
            """)
        finally:
            connection.close()

    @staticmethod
    def _db_bool(value: Optional[bool]) -> Optional[int]:
        return None if value is None else (1 if value else 0)

    def add_principal(self, principal: Principal) -> None:
        with self._connect() as c:
            c.execute("INSERT INTO principals(principal_id) VALUES (?)", (principal.principal_id,))

    def establish_authentication_context(self, context: AuthenticationContext, principal: Principal, *, valid: Optional[bool] = True) -> None:
        with self._connect() as c:
            c.execute("INSERT INTO authentication_contexts(context_id, principal_id, valid) VALUES (?, ?, ?)",
                      (context.context_id, principal.principal_id, self._db_bool(valid)))
        self._trusted_contexts[id(context)] = context

    def _trusted_context(self, value: AuthenticationContext | None) -> AuthenticationContext | None:
        if isinstance(value, AuthenticationContext):
            registered = self._trusted_contexts.get(id(value))
            return value if registered is value else None
        return None

    def set_authentication_context_valid(self, context_id: str, valid: Optional[bool]) -> None:
        self._update_one("UPDATE authentication_contexts SET valid = ? WHERE context_id = ?", (self._db_bool(valid), context_id))

    def add_authority_root(self, root: AuthorityRoot) -> None:
        with self._connect() as c:
            c.execute("INSERT INTO authority_roots(root_id, active) VALUES (?, ?)", (root.root_id, self._db_bool(root.active)))

    def add_effect_intent(self, intent: EffectIntent) -> None:
        with self._connect() as c:
            c.execute("INSERT INTO effect_intents(intent_id, name) VALUES (?, ?)", (intent.intent_id, intent.name))

    def add_effect_contract(self, contract: EffectContract) -> None:
        with self._connect() as c:
            c.execute("INSERT INTO effect_contracts(contract_id, intent_id) VALUES (?, ?)", (contract.contract_id, contract.intent_id))

    def add_authority_grant(self, grant: AuthorityGrant) -> None:
        with self._connect() as c:
            c.execute("INSERT INTO authority_grants(grant_id, root_id, principal_id, intent_id, validity, revoked, expires_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
                      (grant.grant_id, grant.root_id, grant.principal_id, grant.intent_id, self._db_bool(grant.validity), self._db_bool(grant.revoked), grant.expires_at))

    def set_grant_validity(self, grant_id: str, validity: Optional[bool]) -> None:
        self._update_one("UPDATE authority_grants SET validity = ? WHERE grant_id = ?", (self._db_bool(validity), grant_id))

    def set_grant_revoked(self, grant_id: str, revoked: Optional[bool]) -> None:
        self._update_one("UPDATE authority_grants SET revoked = ? WHERE grant_id = ?", (self._db_bool(revoked), grant_id))

    def set_grant_expiration(self, grant_id: str, expires_at: Optional[int]) -> None:
        self._update_one("UPDATE authority_grants SET expires_at = ? WHERE grant_id = ?", (expires_at, grant_id))

    def set_root_active(self, root_id: str, active: Optional[bool]) -> None:
        self._update_one("UPDATE authority_roots SET active = ? WHERE root_id = ?", (self._db_bool(active), root_id))

    def _update_one(self, sql: str, parameters: tuple[Any, ...]) -> None:
        with self._connect() as c:
            cursor = c.execute(sql, parameters)
            if cursor.rowcount != 1:
                raise KeyError("trusted state object not found")

    def _resolve_authenticated_principal(self, connection: sqlite3.Connection, authentication_context: AuthenticationContext | None) -> tuple[Optional[str], Optional[str]]:
        if authentication_context is None:
            return None, "missing_authentication_context"
        if not isinstance(authentication_context, AuthenticationContext):
            return None, "invalid_authentication_context"
        registered = self._trusted_contexts.get(id(authentication_context))
        if registered is not authentication_context:
            return None, "missing_authentication_context"
        row = connection.execute("SELECT c.principal_id, c.valid FROM authentication_contexts AS c JOIN principals AS p ON p.principal_id = c.principal_id WHERE c.context_id = ?", (authentication_context.context_id,)).fetchone()
        if row is None:
            return None, "unresolvable_authentication_context"
        if row["valid"] is None:
            return None, "unknown_authentication_context_fact"
        if row["valid"] != 1:
            return None, "invalid_authentication_context"
        return str(row["principal_id"]), None

    def may(self, authentication_context: AuthenticationContext | None, request: ActionRequest) -> MayResult:
        trusted = self._trusted_context(authentication_context)
        with self._connect() as c:
            principal_id, error = self._resolve_authenticated_principal(c, trusted)
            if principal_id is None:
                return MayResult(False, error or "invalid_authentication_context")
            return self._may_on_connection(c, principal_id, request, int(self._clock()))

    def _may_on_connection(self, c: sqlite3.Connection, principal_id: str, request: ActionRequest, now: int) -> MayResult:
        if c.execute("SELECT 1 FROM effect_intents WHERE intent_id = ?", (request.intent_id,)).fetchone() is None:
            return MayResult(False, "unknown_effect_intent")
        contract = c.execute("SELECT intent_id FROM effect_contracts WHERE contract_id = ?", (request.contract_id,)).fetchone()
        if contract is None or contract["intent_id"] != request.intent_id:
            return MayResult(False, "unknown_or_mismatched_effect_contract")
        rows = c.execute("SELECT g.grant_id, g.validity, g.revoked, g.expires_at, r.active AS root_active FROM authority_grants AS g JOIN authority_roots AS r ON r.root_id = g.root_id WHERE g.principal_id = ? AND g.intent_id = ? ORDER BY g.grant_id", (principal_id, request.intent_id)).fetchall()
        if not rows:
            return MayResult(False, "authority_absent")
        saw_unknown = saw_invalid = saw_expired = saw_revoked = False
        for row in rows:
            if row["root_active"] is None or row["validity"] is None or row["revoked"] is None:
                saw_unknown = True
            elif row["root_active"] != 1 or row["validity"] != 1:
                saw_invalid = True
            elif row["revoked"] != 0:
                saw_revoked = True
            elif row["expires_at"] is not None and now >= row["expires_at"]:
                saw_expired = True
            else:
                return MayResult(True, "may", row["grant_id"])
        if saw_unknown: return MayResult(False, "unknown_authority_fact")
        if saw_revoked: return MayResult(False, "authority_revoked")
        if saw_expired: return MayResult(False, "authority_expired")
        if saw_invalid: return MayResult(False, "authority_invalid")
        return MayResult(False, "authority_absent")

    def authorize(self, request: ActionRequest, *, authentication_context: AuthenticationContext | None = None) -> AuthorizationResult:
        trusted = self._trusted_context(authentication_context)
        c = self._connect()
        try:
            c.execute("BEGIN IMMEDIATE")
            principal_id, error = self._resolve_authenticated_principal(c, trusted)
            if principal_id is None:
                c.execute("ROLLBACK")
                return AuthorizationResult(False, error or "invalid_authentication_context")
            now = int(self._clock())
            decision = self._may_on_connection(c, principal_id, request, now)
            if not decision.allowed or decision.grant_id is None:
                c.execute("ROLLBACK")
                return AuthorizationResult(False, decision.reason)
            authorization = ActionAuthorization(str(uuid.uuid4()), request.request_id, principal_id, decision.grant_id, request.intent_id, request.contract_id, now)
            c.execute("INSERT INTO action_authorizations(authorization_id, request_id, principal_id, grant_id, intent_id, contract_id, issued_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
                      (authorization.authorization_id, authorization.request_id, authorization.principal_id, authorization.grant_id, authorization.intent_id, authorization.contract_id, authorization.issued_at))
            c.execute("COMMIT")
            return AuthorizationResult(True, "authorized", authorization)
        except BaseException:
            if c.in_transaction: c.execute("ROLLBACK")
            raise
        finally:
            c.close()

    def start_attempt(self, authorization: ActionAuthorization) -> StartResult:
        c = self._connect()
        try:
            c.execute("BEGIN IMMEDIATE")
            now = int(self._clock())
            if not isinstance(authorization, ActionAuthorization):
                c.execute("ROLLBACK"); return StartResult(False, "forged_authorization")
            row = c.execute("SELECT authorization_id, request_id, principal_id, grant_id, intent_id, contract_id, issued_at FROM action_authorizations WHERE authorization_id = ?", (authorization.authorization_id,)).fetchone()
            if row is None or not self._authorization_matches(row, authorization):
                c.execute("ROLLBACK"); return StartResult(False, "forged_authorization")
            if c.execute("SELECT 1 FROM authorization_consumed WHERE authorization_id = ?", (authorization.authorization_id,)).fetchone() is not None:
                c.execute("ROLLBACK"); return StartResult(False, "authorization_consumed")
            authority = self._specific_grant_status(c, authorization.grant_id, authorization.principal_id, authorization.intent_id, now)
            if not authority.allowed:
                c.execute("ROLLBACK"); return StartResult(False, authority.reason)
            contract = c.execute("SELECT intent_id FROM effect_contracts WHERE contract_id = ?", (authorization.contract_id,)).fetchone()
            if contract is None or contract["intent_id"] != authorization.intent_id:
                c.execute("ROLLBACK"); return StartResult(False, "unknown_start_precondition")
            attempt_id = str(uuid.uuid4())
            consumed = AuthorizationConsumed(authorization.authorization_id, attempt_id, now)
            attempt = ActionAttempt(attempt_id, authorization.authorization_id, authorization.principal_id, authorization.intent_id, authorization.contract_id)
            started = AttemptStarted(attempt_id, now)
            c.execute("INSERT INTO authorization_consumed(authorization_id, attempt_id, consumed_at) VALUES (?, ?, ?)", (consumed.authorization_id, consumed.attempt_id, consumed.consumed_at))
            c.execute("INSERT INTO action_attempts(attempt_id, authorization_id, principal_id, intent_id, contract_id) VALUES (?, ?, ?, ?, ?)", (attempt.attempt_id, attempt.authorization_id, attempt.principal_id, attempt.intent_id, attempt.contract_id))
            c.execute("INSERT INTO attempt_started(attempt_id, started_at) VALUES (?, ?)", (started.attempt_id, started.started_at))
            c.execute("COMMIT")
            return StartResult(True, "attempt_started", attempt, consumed, started)
        except sqlite3.IntegrityError:
            if c.in_transaction: c.execute("ROLLBACK")
            return StartResult(False, "authorization_consumed")
        except BaseException:
            if c.in_transaction: c.execute("ROLLBACK")
            raise
        finally:
            c.close()

    @staticmethod
    def _authorization_matches(row: sqlite3.Row, authorization: ActionAuthorization) -> bool:
        return all((row["authorization_id"] == authorization.authorization_id,
                    row["request_id"] == authorization.request_id,
                    row["principal_id"] == authorization.principal_id,
                    row["grant_id"] == authorization.grant_id,
                    row["intent_id"] == authorization.intent_id,
                    row["contract_id"] == authorization.contract_id,
                    row["issued_at"] == authorization.issued_at))

    def _specific_grant_status(self, c: sqlite3.Connection, grant_id: str, principal_id: str, intent_id: str, now: int) -> MayResult:
        row = c.execute("SELECT g.validity, g.revoked, g.expires_at, r.active AS root_active FROM authority_grants AS g JOIN authority_roots AS r ON r.root_id = g.root_id WHERE g.grant_id = ? AND g.principal_id = ? AND g.intent_id = ?", (grant_id, principal_id, intent_id)).fetchone()
        if row is None: return MayResult(False, "authority_absent")
        if row["root_active"] is None or row["validity"] is None or row["revoked"] is None: return MayResult(False, "unknown_authority_fact")
        if row["root_active"] != 1 or row["validity"] != 1: return MayResult(False, "authority_invalid")
        if row["revoked"] != 0: return MayResult(False, "authority_revoked")
        if row["expires_at"] is not None and now >= row["expires_at"]: return MayResult(False, "authority_expired")
        return MayResult(True, "may", grant_id)

    def snapshot(self) -> Dict[str, List[Dict[str, Any]]]:
        with self._connect() as c:
            return {table: [dict(row) for row in c.execute(f"SELECT * FROM {table} ORDER BY rowid").fetchall()] for table in self._SNAPSHOT_TABLES}
