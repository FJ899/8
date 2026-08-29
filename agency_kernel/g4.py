from __future__ import annotations

import hashlib
import json
import os
import sqlite3
import subprocess
import tempfile
import uuid
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import FrozenSet, Iterable, Optional

from .g1 import ActionAttempt
from .g2 import AdmissionResult, Capability, Kernel as G2Kernel, OperationAdmission
from .g3 import AcceptanceResult, ComplianceResult


PROTECTED_REF_DEFAULT = "refs/heads/kernel-test"


def _safe_path(path: str) -> bool:
    if not path or path.startswith("/") or "\\" in path:
        return False
    p = PurePosixPath(path)
    if any(part in {"", ".", "..", ".git"} for part in p.parts):
        return False
    return str(p) == path


@dataclass(frozen=True)
class GitFile:
    path: str
    content: str


@dataclass(frozen=True)
class GitTreeOperation:
    protected_ref: str
    expected_old_oid: str
    files: tuple[GitFile, ...]
    possible_effects: Optional[FrozenSet[str]]

    def canonical_bytes(self) -> bytes:
        if not self.protected_ref.startswith("refs/heads/"):
            raise ValueError("invalid_protected_ref")
        if len(self.expected_old_oid) != 40 or any(ch not in "0123456789abcdef" for ch in self.expected_old_oid):
            raise ValueError("invalid_expected_old_oid")
        seen: set[str] = set()
        encoded_files = []
        for item in sorted(self.files, key=lambda x: x.path):
            if not _safe_path(item.path) or item.path in seen:
                raise ValueError("invalid_path")
            seen.add(item.path)
            encoded_files.append({"path": item.path, "content": item.content})
        effects = None if self.possible_effects is None else sorted(self.possible_effects)
        payload = {
            "operation_type": "sanitized_git_replace_tree",
            "protected_ref": self.protected_ref,
            "expected_old_oid": self.expected_old_oid,
            "files": encoded_files,
            "possible_effects": effects,
        }
        return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

    @property
    def operation_digest(self) -> str:
        return hashlib.sha256(self.canonical_bytes()).hexdigest()


@dataclass(frozen=True)
class GitExecutionResult:
    occurred: bool
    reason: str
    protected_ref: str
    before_oid: Optional[str] = None
    after_oid: Optional[str] = None
    tree_oid: Optional[str] = None
    operation_digest: Optional[str] = None


@dataclass(frozen=True)
class GitObservation:
    protected_ref: str
    commit_oid: Optional[str]
    tree_oid: Optional[str]
    parent_oid: Optional[str]
    files: tuple[tuple[str, str], ...]
    admission_id: Optional[str]
    operation_digest: Optional[str]
    metadata_tree_oid: Optional[str]
    expected_old_oid: Optional[str]
    covered: bool = True
    attribution_ambiguous: bool = False


class SanitizedGitRepo:
    def __init__(self, repo: str | Path, protected_ref: str = PROTECTED_REF_DEFAULT):
        self.repo = Path(repo)
        self.protected_ref = protected_ref
        self.hooks_dir = self.repo.parent / "controlled-empty-hooks"
        self.hooks_dir.mkdir(parents=True, exist_ok=True)
        os.chmod(self.hooks_dir, 0o700)
        if not self.repo.exists():
            self.repo.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(["git", "init", "--bare", str(self.repo)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self._configure()
        self._ensure_initial_ref()

    def _env(self, extra: Optional[dict[str, str]] = None) -> dict[str, str]:
        env = dict(os.environ)
        env.update({
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_CONFIG_GLOBAL": os.devnull,
            "HOME": str(self.repo.parent),
            "GIT_AUTHOR_NAME": "Agency Kernel Broker",
            "GIT_AUTHOR_EMAIL": "broker@example.invalid",
            "GIT_COMMITTER_NAME": "Agency Kernel Broker",
            "GIT_COMMITTER_EMAIL": "broker@example.invalid",
            "GIT_AUTHOR_DATE": "2000-01-01T00:00:00+00:00",
            "GIT_COMMITTER_DATE": "2000-01-01T00:00:00+00:00",
        })
        env.pop("GIT_ALTERNATE_OBJECT_DIRECTORIES", None)
        env.pop("GIT_OBJECT_DIRECTORY", None)
        env.pop("GIT_COMMON_DIR", None)
        if extra:
            env.update(extra)
        return env

    def git(self, *args: str, input_text: Optional[str] = None, check: bool = True, extra_env: Optional[dict[str, str]] = None) -> str:
        cp = subprocess.run(
            ["git", "--git-dir", str(self.repo), *args],
            input=input_text,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=self._env(extra_env),
        )
        if check and cp.returncode != 0:
            raise RuntimeError(f"git_failed:{args!r}:{cp.stderr.strip()}")
        return cp.stdout.strip()

    def _configure(self) -> None:
        self.git("config", "core.hooksPath", str(self.hooks_dir))
        self.git("config", "protocol.file.allow", "never")
        self.git("config", "receive.denyNonFastforwards", "false")
        self.git("config", "gc.auto", "0")
        alternates = self.repo / "objects" / "info" / "alternates"
        if alternates.exists():
            alternates.unlink()

    def _ensure_initial_ref(self) -> None:
        current = self.rev_parse_ref(allow_missing=True)
        if current is not None:
            return
        tree = self.git("mktree", input_text="")
        commit = self.git("commit-tree", tree, input_text="agency-kernel-initial\n")
        self.git("update-ref", self.protected_ref, commit, "0" * 40)

    def rev_parse_ref(self, *, allow_missing: bool = False) -> Optional[str]:
        cp = subprocess.run(
            ["git", "--git-dir", str(self.repo), "rev-parse", "--verify", self.protected_ref],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=self._env(),
        )
        if cp.returncode != 0:
            if allow_missing:
                return None
            raise RuntimeError("protected_ref_absent")
        return cp.stdout.strip()

    def tree_oid(self, commit_oid: str) -> str:
        return self.git("rev-parse", f"{commit_oid}^{{tree}}")

    def list_files(self, commit_oid: str) -> tuple[tuple[str, str], ...]:
        paths = [p for p in self.git("ls-tree", "-r", "--name-only", commit_oid).splitlines() if p]
        result = []
        for path in paths:
            content = self.git("show", f"{commit_oid}:{path}")
            result.append((path, content))
        return tuple(sorted(result))

    def build_tree(self, files: Iterable[GitFile]) -> str:
        index_fd, index_path = tempfile.mkstemp(prefix="g4-index-", dir=str(self.repo.parent))
        os.close(index_fd)
        try:
            os.unlink(index_path)
            env = {"GIT_INDEX_FILE": index_path}
            self.git("read-tree", "--empty", extra_env=env)
            for item in sorted(files, key=lambda x: x.path):
                blob = self.git("hash-object", "-w", "--stdin", input_text=item.content)
                self.git("update-index", "--add", "--cacheinfo", f"100644,{blob},{item.path}", extra_env=env)
            return self.git("write-tree", extra_env=env)
        finally:
            try:
                os.unlink(index_path)
            except FileNotFoundError:
                pass

    def changed_paths(self, old_tree: str, new_tree: str) -> FrozenSet[str]:
        out = self.git("diff-tree", "--no-commit-id", "--name-only", "-r", old_tree, new_tree)
        return frozenset(line for line in out.splitlines() if line)

    def create_commit(self, tree_oid: str, old_oid: str, admission_id: str, operation_digest: str) -> str:
        message = (
            f"agency-kernel-admission:{admission_id}\n"
            f"operation-digest:{operation_digest}\n"
            f"tree:{tree_oid}\n"
            f"expected-old:{old_oid}\n"
        )
        return self.git("commit-tree", tree_oid, "-p", old_oid, input_text=message)

    def cas_update(self, new_oid: str, expected_old_oid: str) -> bool:
        cp = subprocess.run(
            ["git", "--git-dir", str(self.repo), "update-ref", self.protected_ref, new_oid, expected_old_oid],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=self._env(),
        )
        return cp.returncode == 0

    def commit_metadata(self, oid: str) -> tuple[Optional[str], Optional[str], Optional[str], Optional[str], Optional[str]]:
        raw = self.git("show", "-s", "--format=%P%n%B", oid)
        lines = raw.splitlines()
        parent = lines[0].split()[0] if lines and lines[0].strip() else None
        values: dict[str, str] = {}
        for line in lines[1:]:
            for key in ("agency-kernel-admission", "operation-digest", "tree", "expected-old"):
                prefix = key + ":"
                if line.startswith(prefix):
                    values[key] = line[len(prefix):]
        return parent, values.get("agency-kernel-admission"), values.get("operation-digest"), values.get("tree"), values.get("expected-old")


class GitObserver:
    def __init__(self, repo: SanitizedGitRepo):
        self.repo = repo

    def observe(self, *, covered: bool = True, attribution_ambiguous: bool = False) -> GitObservation:
        oid = self.repo.rev_parse_ref()
        tree = self.repo.tree_oid(oid)
        parent, admission_id, digest, metadata_tree, expected_old = self.repo.commit_metadata(oid)
        return GitObservation(
            self.repo.protected_ref,
            oid,
            tree,
            parent,
            self.repo.list_files(oid),
            admission_id,
            digest,
            metadata_tree,
            expected_old,
            covered,
            attribution_ambiguous,
        )


class Kernel(G2Kernel):
    """G4 transfer adapter for one sanitized protected Git ref; frozen kernel semantics are unchanged."""

    def __init__(self, control_db: str | Path, repo_path: str | Path, protected_ref: str = PROTECTED_REF_DEFAULT, clock=None):
        self.git_repo = SanitizedGitRepo(repo_path, protected_ref)
        self.protected_ref = protected_ref
        super().__init__(control_db, Path(str(repo_path) + ".unused-g2-boundary"), clock=clock)
        self._initialize_g4_schema()

    def _initialize_g4_schema(self) -> None:
        with self._connect() as c:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS g4_execution_completions (
                    admission_id TEXT PRIMARY KEY REFERENCES operation_admissions(admission_id),
                    commit_oid TEXT NOT NULL,
                    completed_at INTEGER NOT NULL
                )
                """
            )

    def has_control_completion(self, admission_id: str) -> bool:
        with self._connect() as c:
            return c.execute("SELECT 1 FROM g4_execution_completions WHERE admission_id = ?", (admission_id,)).fetchone() is not None

    @staticmethod
    def ref_effect(ref: str) -> str:
        return f"REF({ref})"

    @staticmethod
    def path_effect(path: str) -> str:
        return f"PATH({path})"

    def required_possible_effects(self, operation: GitTreeOperation) -> FrozenSet[str]:
        old_tree = self.git_repo.tree_oid(operation.expected_old_oid)
        new_tree = self.git_repo.build_tree(operation.files)
        changed = self.git_repo.changed_paths(old_tree, new_tree)
        return frozenset({self.ref_effect(operation.protected_ref), *(self.path_effect(p) for p in changed)})

    def admit_git_operation(self, attempt: ActionAttempt, capability_id: str, operation: GitTreeOperation) -> AdmissionResult:
        try:
            canonical = operation.canonical_bytes()
        except (TypeError, ValueError):
            return AdmissionResult(False, "invalid_operation")
        if operation.protected_ref != self.protected_ref:
            return AdmissionResult(False, "protected_ref_mismatch")
        if operation.possible_effects is None:
            return AdmissionResult(False, "unknown_possible_effects")
        current = self.git_repo.rev_parse_ref()
        if current != operation.expected_old_oid:
            return AdmissionResult(False, "stale_ref")
        try:
            required = self.required_possible_effects(operation)
        except RuntimeError:
            return AdmissionResult(False, "invalid_expected_ref_state")
        if not required.issubset(operation.possible_effects):
            return AdmissionResult(False, "effect_model_underapproximation")

        c = self._connect()
        try:
            c.execute("BEGIN IMMEDIATE")
            row = self._attempt_row(c, attempt.attempt_id)
            if row is None:
                c.execute("ROLLBACK")
                return AdmissionResult(False, "invalid_attempt")
            if (row["authorization_id"], row["principal_id"], row["intent_id"], row["contract_id"]) != (
                attempt.authorization_id, attempt.principal_id, attempt.intent_id, attempt.contract_id
            ):
                c.execute("ROLLBACK")
                return AdmissionResult(False, "forged_attempt")
            authority = self._specific_grant_status(c, row["grant_id"], row["principal_id"], row["intent_id"], int(self._clock()))
            if not authority.allowed:
                c.execute("ROLLBACK")
                return AdmissionResult(False, authority.reason)
            cap = c.execute("SELECT resource, valid FROM capabilities WHERE capability_id = ?", (capability_id,)).fetchone()
            if cap is None:
                c.execute("ROLLBACK")
                return AdmissionResult(False, "capability_absent")
            if cap["valid"] is None:
                c.execute("ROLLBACK")
                return AdmissionResult(False, "unknown_capability_fact")
            if cap["valid"] != 1:
                c.execute("ROLLBACK")
                return AdmissionResult(False, "capability_invalid")
            if cap["resource"] != self.protected_ref:
                c.execute("ROLLBACK")
                return AdmissionResult(False, "capability_resource_mismatch")
            envelope = frozenset(r["effect"] for r in c.execute("SELECT effect FROM effect_envelopes WHERE contract_id = ?", (row["contract_id"],)).fetchall())
            if not operation.possible_effects.issubset(envelope):
                c.execute("ROLLBACK")
                return AdmissionResult(False, "effect_envelope_exceeded")
            admission = OperationAdmission(str(uuid.uuid4()), attempt.attempt_id, capability_id, hashlib.sha256(canonical).hexdigest(), canonical)
            c.execute(
                "INSERT INTO operation_admissions(admission_id, attempt_id, capability_id, operation_digest, canonical_operation) VALUES (?, ?, ?, ?, ?)",
                (admission.admission_id, admission.attempt_id, admission.capability_id, admission.operation_digest, admission.canonical_operation),
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
    def _decode_operation(canonical: bytes, expected_digest: str) -> tuple[Optional[GitTreeOperation], Optional[str], str]:
        digest = hashlib.sha256(canonical).hexdigest()
        if digest != expected_digest:
            return None, "admission_digest_mismatch", digest
        try:
            payload = json.loads(canonical.decode("utf-8"))
            if payload.get("operation_type") != "sanitized_git_replace_tree":
                return None, "invalid_admitted_operation", digest
            files = tuple(GitFile(str(item["path"]), str(item["content"])) for item in payload["files"])
            effects_raw = payload.get("possible_effects")
            effects = None if effects_raw is None else frozenset(str(x) for x in effects_raw)
            op = GitTreeOperation(str(payload["protected_ref"]), str(payload["expected_old_oid"]), files, effects)
            if op.canonical_bytes() != canonical:
                return None, "noncanonical_admitted_operation", digest
            return op, None, digest
        except (KeyError, TypeError, ValueError, json.JSONDecodeError, UnicodeDecodeError):
            return None, "invalid_admitted_operation", digest

    def execute_git_admission(self, admission_id: str, *, crash_point: Optional[str] = None) -> GitExecutionResult:
        c = self._connect()
        try:
            c.execute("BEGIN IMMEDIATE")
            row = c.execute("SELECT operation_digest, canonical_operation FROM operation_admissions WHERE admission_id = ?", (admission_id,)).fetchone()
            if row is None:
                c.execute("ROLLBACK")
                return GitExecutionResult(False, "admission_absent", self.protected_ref)
            if c.execute("SELECT 1 FROM operation_admission_executions WHERE admission_id = ?", (admission_id,)).fetchone() is not None:
                c.execute("ROLLBACK")
                return GitExecutionResult(False, "admission_consumed", self.protected_ref)
            op, error, digest = self._decode_operation(bytes(row["canonical_operation"]), str(row["operation_digest"]))
            if error is not None or op is None:
                c.execute("ROLLBACK")
                return GitExecutionResult(False, error or "invalid_admitted_operation", self.protected_ref, operation_digest=digest)
            c.execute("INSERT INTO operation_admission_executions(admission_id, executed_at) VALUES (?, ?)", (admission_id, int(self._clock())))
            c.execute("COMMIT")
        finally:
            c.close()

        current = self.git_repo.rev_parse_ref()
        if current != op.expected_old_oid:
            return GitExecutionResult(False, "stale_ref", self.protected_ref, current, current, operation_digest=digest)
        new_tree = self.git_repo.build_tree(op.files)
        if crash_point == "before_ref_cas":
            return GitExecutionResult(False, "crash_before_ref_cas", self.protected_ref, current, current, new_tree, digest)
        new_commit = self.git_repo.create_commit(new_tree, op.expected_old_oid, admission_id, digest)
        if not self.git_repo.cas_update(new_commit, op.expected_old_oid):
            now = self.git_repo.rev_parse_ref()
            return GitExecutionResult(False, "stale_ref", self.protected_ref, op.expected_old_oid, now, new_tree, digest)
        if crash_point == "after_ref_cas_before_control_completion":
            return GitExecutionResult(True, "crash_after_ref_cas_before_control_completion", self.protected_ref, op.expected_old_oid, new_commit, new_tree, digest)
        with self._connect() as c:
            c.execute("INSERT INTO g4_execution_completions(admission_id, commit_oid, completed_at) VALUES (?, ?, ?)", (admission_id, new_commit, int(self._clock())))
        return GitExecutionResult(True, "executed", self.protected_ref, op.expected_old_oid, new_commit, new_tree, digest)

    def did(self, admission: OperationAdmission, observation: GitObservation) -> bool:
        if observation.commit_oid is None or observation.tree_oid is None:
            return False
        if observation.admission_id != admission.admission_id or observation.operation_digest != admission.operation_digest:
            return False
        if observation.metadata_tree_oid != observation.tree_oid:
            return False
        if observation.expected_old_oid != observation.parent_oid:
            return False
        with self._connect() as c:
            row = c.execute("SELECT operation_digest FROM operation_admissions WHERE admission_id = ?", (admission.admission_id,)).fetchone()
            return row is not None and row["operation_digest"] == admission.operation_digest

    def assess_compliance(self, admission: OperationAdmission, observation: GitObservation, *, supported_possible_effects: FrozenSet[str]) -> ComplianceResult:
        if not observation.covered:
            return ComplianceResult("INDETERMINATE", "missing_coverage", frozenset(), supported_possible_effects)
        if observation.attribution_ambiguous:
            return ComplianceResult("INDETERMINATE", "ambiguous_attribution", frozenset(), supported_possible_effects)
        if not self.did(admission, observation):
            return ComplianceResult("INDETERMINATE", "unresolved_attribution", frozenset(), supported_possible_effects)
        assert observation.parent_oid is not None and observation.tree_oid is not None
        old_tree = self.git_repo.tree_oid(observation.parent_oid)
        changed = self.git_repo.changed_paths(old_tree, observation.tree_oid)
        actual = frozenset({self.ref_effect(observation.protected_ref), *(self.path_effect(p) for p in changed)})
        if not actual.issubset(supported_possible_effects):
            return ComplianceResult("FAIL", "effect_model_unsound", actual, supported_possible_effects)
        return ComplianceResult("PASS", "within_scope", actual, supported_possible_effects)

    @staticmethod
    def within_scope(compliance: ComplianceResult) -> bool:
        return compliance.status == "PASS"

    @staticmethod
    def satisfied(observation: GitObservation, expected_files: dict[str, str]) -> bool:
        return dict(observation.files) == dict(expected_files)

    @staticmethod
    def accept(passed: bool, reason: str = "human_or_external_acceptance") -> AcceptanceResult:
        return AcceptanceResult(passed, reason)

    def inject_unattributed_ref_for_test(self, files: tuple[GitFile, ...]) -> str:
        """Adversarial test hook: mutate the protected ref without Agency Kernel provenance metadata."""
        old = self.git_repo.rev_parse_ref()
        tree = self.git_repo.build_tree(files)
        commit = self.git_repo.git("commit-tree", tree, "-p", old, input_text="unattributed external mutation\n")
        if not self.git_repo.cas_update(commit, old):
            raise RuntimeError("test_injection_cas_failed")
        return commit
