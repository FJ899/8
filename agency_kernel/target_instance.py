from __future__ import annotations

import hashlib
import os
import sqlite3
from dataclasses import dataclass
from pathlib import Path


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


def filesystem_target_instance_id(path: str | Path, *, namespace: str) -> str:
    """Identify the current filesystem object, not its copyable contents.

    This reference-runtime identity is deliberately tied to the concrete local
    filesystem object using device+inode. A process restart over the same object
    preserves the identity; copying the store/repository to another object does
    not. It is not declared as a universal storage identity scheme.
    """

    resolved = Path(path).resolve()
    st = os.stat(resolved)
    payload = f"{namespace}\0{st.st_dev}\0{st.st_ino}".encode("ascii")
    return hashlib.sha256(payload).hexdigest()


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
    """Persist one historical target binding before trusted runtime execution proceeds.

    The binding write is intentionally separate from the older domain admission
    transaction. A crash before this write leaves an admission with no historical
    target proof; evidence recovery must then fail closed rather than inventing
    provenance. A successful EffectAdapter admission returns only after this
    record exists.
    """

    with kernel._connect() as connection:
        ensure_operation_target_binding_schema(connection)
        record_operation_target_binding(connection, admission_id, binding)
