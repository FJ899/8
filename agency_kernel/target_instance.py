from __future__ import annotations

import hashlib
import os
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass(frozen=True)
class HistoricalTargetBinding:
    """Opaque historical binding between one admission and one concrete target instance.

    The common shape is intentionally small. `kind` selects domain semantics;
    `instance_id` is opaque and domain-specific; `logical_target` remains the
    resource/ref identity already enforced by capability admission.

    COMMON TYPE != COMMON SEMANTICS.
    """

    kind: str
    logical_target: str
    instance_id: str

    def __post_init__(self) -> None:
        for name, value in (
            ("kind", self.kind),
            ("logical_target", self.logical_target),
            ("instance_id", self.instance_id),
        ):
            if not isinstance(value, str) or not value:
                raise ValueError(f"invalid_{name}")


def _filesystem_stat_instance_id(st: os.stat_result, *, namespace: str) -> str:
    payload = f"{namespace}\0{st.st_dev}\0{st.st_ino}".encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def filesystem_target_instance_id(path: str | Path, *, namespace: str) -> str:
    """Identify the current filesystem object named by a path."""

    resolved = Path(path).resolve()
    return _filesystem_stat_instance_id(os.stat(resolved), namespace=namespace)


def filesystem_fd_target_instance_id(fd: int, *, namespace: str) -> str:
    """Identify the already-open filesystem object referenced by `fd`.

    Unlike pathname identity, this remains tied to the opened object even if the
    namespace path is later renamed or rebound. It is a Linux/local-filesystem
    reference-runtime primitive, not a universal storage identity scheme.
    """

    if not isinstance(fd, int) or fd < 0:
        raise ValueError("invalid_target_fd")
    return _filesystem_stat_instance_id(os.fstat(fd), namespace=namespace)


def ensure_operation_target_binding_schema(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS operation_target_bindings (
            admission_id TEXT PRIMARY KEY REFERENCES operation_admissions(admission_id),
            target_kind TEXT NOT NULL,
            logical_target TEXT NOT NULL,
            target_instance_id TEXT NOT NULL
        )
        """
    )


def record_operation_target_binding(
    connection: sqlite3.Connection,
    admission_id: str,
    binding: HistoricalTargetBinding,
) -> None:
    connection.execute(
        """
        INSERT INTO operation_target_bindings(
            admission_id, target_kind, logical_target, target_instance_id
        ) VALUES (?, ?, ?, ?)
        """,
        (
            admission_id,
            binding.kind,
            binding.logical_target,
            binding.instance_id,
        ),
    )


def persist_operation_target_binding(
    kernel,
    admission_id: str,
    binding: HistoricalTargetBinding,
) -> None:
    """Persist one historical target binding before trusted runtime execution proceeds."""

    with kernel._connect() as connection:
        ensure_operation_target_binding_schema(connection)
        record_operation_target_binding(connection, admission_id, binding)


def load_operation_target_binding(
    kernel,
    admission_id: str,
) -> Optional[HistoricalTargetBinding]:
    """Load the exact historical target binding for one admitted operation."""

    if not isinstance(admission_id, str) or not admission_id:
        raise ValueError("invalid_admission_id")
    with kernel._connect() as connection:
        table = connection.execute(
            """
            SELECT 1 FROM sqlite_master
            WHERE type = 'table' AND name = 'operation_target_bindings'
            """
        ).fetchone()
        if table is None:
            return None
        row = connection.execute(
            """
            SELECT target_kind, logical_target, target_instance_id
            FROM operation_target_bindings
            WHERE admission_id = ?
            """,
            (admission_id,),
        ).fetchone()
    if row is None:
        return None
    return HistoricalTargetBinding(
        str(row["target_kind"]),
        str(row["logical_target"]),
        str(row["target_instance_id"]),
    )
