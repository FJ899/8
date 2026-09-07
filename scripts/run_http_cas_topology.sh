#!/usr/bin/env bash
set -euo pipefail

OUT=${1:-p7-http-cas-topology-evidence}
rm -rf "$OUT"
mkdir -p "$OUT"
exec 9>"$OUT/commands.trace"
export BASH_XTRACEFD=9
set -x

ROOT=$(pwd)
PRIVATE_ROOT=$(mktemp -d /tmp/agency-kernel-p7-private.XXXXXX)
SOCKET_ROOT=$(mktemp -d /tmp/agency-kernel-p7-ipc.XXXXXX)
PROVIDER_DIR="$PRIVATE_ROOT/provider"
LEDGER_DIR="$PRIVATE_ROOT/ledger"
PROVIDER_DB="$PROVIDER_DIR/provider.sqlite"
LEDGER="$LEDGER_DIR/control.sqlite"
TOKEN="$PRIVATE_ROOT/provider.token"
PROVIDER_READY="$SOCKET_ROOT/provider.ready"
BROKER_READY="$SOCKET_ROOT/broker.ready"
SOCKET="$SOCKET_ROOT/broker.sock"
CLIENT="$SOCKET_ROOT/http_cas_ipc_client.py"
PROVIDER_ID="p7-http-provider"

cleanup() {
  set +e
  if [[ -n "${BROKER_PID:-}" ]] && kill -0 "$BROKER_PID" 2>/dev/null; then
    sudo -u p7broker env PYTHONPATH="$ROOT" python "$CLIENT" --socket "$SOCKET" --request '{"action":"shutdown"}' >/dev/null 2>&1 || true
    sleep 0.1
    sudo kill "$BROKER_PID" 2>/dev/null || true
  fi
  if [[ -n "${PROVIDER_PID:-}" ]] && kill -0 "$PROVIDER_PID" 2>/dev/null; then
    sudo kill "$PROVIDER_PID" 2>/dev/null || true
  fi
  [[ -n "${BROKER_SUPERVISOR_PID:-}" ]] && wait "$BROKER_SUPERVISOR_PID" 2>/dev/null || true
  [[ -n "${PROVIDER_SUPERVISOR_PID:-}" ]] && wait "$PROVIDER_SUPERVISOR_PID" 2>/dev/null || true
  sudo userdel -f p7requester 2>/dev/null || true
  sudo userdel -f p7hostile 2>/dev/null || true
  sudo userdel -f p7broker 2>/dev/null || true
  sudo userdel -f p7provider 2>/dev/null || true
  sudo groupdel p7requester 2>/dev/null || true
  sudo groupdel p7hostile 2>/dev/null || true
  sudo groupdel p7trusted 2>/dev/null || true
  rm -rf "$PRIVATE_ROOT" "$SOCKET_ROOT"
}
trap cleanup EXIT

for user in p7requester p7hostile p7broker p7provider; do
  sudo userdel -f "$user" 2>/dev/null || true
done
sudo groupdel p7requester 2>/dev/null || true
sudo groupdel p7hostile 2>/dev/null || true
sudo groupdel p7trusted 2>/dev/null || true

sudo groupadd p7trusted
sudo useradd --no-create-home --shell /usr/sbin/nologin --gid p7trusted p7broker
sudo useradd --no-create-home --shell /usr/sbin/nologin --gid p7trusted p7provider
sudo useradd --no-create-home --shell /usr/sbin/nologin --user-group p7requester
sudo useradd --no-create-home --shell /usr/sbin/nologin --user-group p7hostile
BROKER_UID=$(id -u p7broker)
PROVIDER_UID=$(id -u p7provider)
REQUESTER_UID=$(id -u p7requester)
HOSTILE_UID=$(id -u p7hostile)

sudo chown root:p7trusted "$PRIVATE_ROOT"
sudo chmod 750 "$PRIVATE_ROOT"
sudo mkdir -p "$PROVIDER_DIR" "$LEDGER_DIR"
sudo chown p7provider:p7trusted "$PROVIDER_DIR"
sudo chown p7broker:p7trusted "$LEDGER_DIR"
sudo chmod 700 "$PROVIDER_DIR" "$LEDGER_DIR"
python - <<'PY' > "$TOKEN"
import secrets
print(secrets.token_urlsafe(48))
PY
sudo chown root:p7trusted "$TOKEN"
sudo chmod 640 "$TOKEN"

sudo chown root:p7trusted "$SOCKET_ROOT"
sudo chmod 775 "$SOCKET_ROOT"
cp "$ROOT/scripts/http_cas_ipc_client.py" "$CLIENT"
chmod 755 "$CLIENT"

sudo -u p7broker test -r "$TOKEN"
sudo -u p7provider test -r "$TOKEN"
! sudo -u p7requester test -r "$TOKEN"
! sudo -u p7hostile test -r "$TOKEN"

sudo -u p7provider env PYTHONPATH="$ROOT" python "$ROOT/scripts/http_cas_provider_process.py" \
  --db "$PROVIDER_DB" \
  --credential-file "$TOKEN" \
  --provider-id "$PROVIDER_ID" \
  --ready-file "$PROVIDER_READY" \
  --seed-resource X \
  --seed-value initial \
  --seed-version 0 \
  >"$OUT/provider.stdout" 2>"$OUT/provider.stderr" &
PROVIDER_SUPERVISOR_PID=$!

for _ in $(seq 1 100); do
  [[ -f "$PROVIDER_READY" ]] && break
  sleep 0.05
done
[[ -f "$PROVIDER_READY" ]]
PROVIDER_PID=$(python -c 'import json,sys; print(json.load(open(sys.argv[1]))["pid"])' "$PROVIDER_READY")
PROVIDER_PORT=$(python -c 'import json,sys; print(json.load(open(sys.argv[1]))["port"])' "$PROVIDER_READY")
PROVIDER_ENDPOINT="http://127.0.0.1:$PROVIDER_PORT"
kill -0 "$PROVIDER_PID"

sudo -u p7broker env PYTHONPATH="$ROOT" python "$ROOT/scripts/http_cas_broker.py" \
  --socket "$SOCKET" \
  --ledger "$LEDGER" \
  --provider-endpoint "$PROVIDER_ENDPOINT" \
  --credential-file "$TOKEN" \
  --provider-id "$PROVIDER_ID" \
  --authorized-uid "$REQUESTER_UID" \
  --ready-file "$BROKER_READY" \
  >"$OUT/broker.stdout" 2>"$OUT/broker.stderr" &
BROKER_SUPERVISOR_PID=$!

for _ in $(seq 1 100); do
  [[ -S "$SOCKET" && -f "$BROKER_READY" ]] && break
  sleep 0.05
done
[[ -S "$SOCKET" && -f "$BROKER_READY" ]]
BROKER_PID=$(cat "$BROKER_READY")
kill -0 "$BROKER_PID"

run_as() {
  local user=$1
  shift
  sudo -u "$user" "$@"
}

{
  echo "BROKER_UID=$BROKER_UID"
  echo "PROVIDER_UID=$PROVIDER_UID"
  echo "REQUESTER_UID=$REQUESTER_UID"
  echo "HOSTILE_UID=$HOSTILE_UID"
  echo "BROKER_PID=$BROKER_PID"
  echo "PROVIDER_PID=$PROVIDER_PID"
  echo "PROVIDER_ENDPOINT=$PROVIDER_ENDPOINT"
  echo "PRIVATE_ROOT=$PRIVATE_ROOT"
  echo "PROVIDER_DB=$PROVIDER_DB"
  echo "LEDGER=$LEDGER"
  echo "TOKEN_PATH=$TOKEN"
  echo "SOCKET=$SOCKET"
  printf 'BROKER_ID='; id p7broker
  printf 'PROVIDER_IDENTITY='; id p7provider
  printf 'REQUESTER_ID='; id p7requester
  printf 'HOSTILE_ID='; id p7hostile
  printf 'CLIENT_SHA256='; sha256sum "$CLIENT" | awk '{print $1}'
  printf 'CANDIDATE_CLIENT_BLOB='; git rev-parse HEAD:scripts/http_cas_ipc_client.py
  printf 'BROKER_BLOB='; git rev-parse HEAD:scripts/http_cas_broker.py
  printf 'PROVIDER_PROCESS_BLOB='; git rev-parse HEAD:scripts/http_cas_provider_process.py
  printf 'HTTP_KERNEL_BLOB='; git rev-parse HEAD:agency_kernel/http_cas.py
  printf 'HTTP_PROVIDER_BLOB='; git rev-parse HEAD:agency_kernel/http_cas_provider.py
  printf 'RUNTIME_BLOB='; git rev-parse HEAD:agency_kernel/runtime.py
  printf 'BINDINGS_BLOB='; git rev-parse HEAD:agency_kernel/bindings.py
  stat -c 'PRIVATE_ROOT_MODE=%a OWNER=%u GROUP=%g' "$PRIVATE_ROOT"
  stat -c 'PROVIDER_DIR_MODE=%a OWNER=%u GROUP=%g' "$PROVIDER_DIR"
  stat -c 'LEDGER_DIR_MODE=%a OWNER=%u GROUP=%g' "$LEDGER_DIR"
  stat -c 'TOKEN_MODE=%a OWNER=%u GROUP=%g' "$TOKEN"
  stat -c 'PROVIDER_DB_MODE=%a OWNER=%u GROUP=%g' "$PROVIDER_DB"
  stat -c 'LEDGER_MODE=%a OWNER=%u GROUP=%g' "$LEDGER"
  stat -c 'SOCKET_ROOT_MODE=%a OWNER=%u GROUP=%g' "$SOCKET_ROOT"
  stat -c 'SOCKET_MODE=%a OWNER=%u GROUP=%g' "$SOCKET"
  ps -o pid=,uid=,gid=,comm= -p "$BROKER_PID" -p "$PROVIDER_PID"
  findmnt -T "$PROVIDER_DB" -o TARGET,SOURCE,FSTYPE,OPTIONS
  findmnt -T "$LEDGER" -o TARGET,SOURCE,FSTYPE,OPTIONS
  ss -ltnup
} > "$OUT/topology.txt" 2>&1

[[ "$(ps -o uid= -p "$BROKER_PID" | tr -d ' ')" = "$BROKER_UID" ]]
[[ "$(ps -o uid= -p "$PROVIDER_PID" | tr -d ' ')" = "$PROVIDER_UID" ]]
! id -nG p7requester | tr ' ' '\n' | grep -qx p7trusted
! id -nG p7hostile | tr ' ' '\n' | grep -qx p7trusted

grep '^Cap' "/proc/$BROKER_PID/status" > "$OUT/broker_capabilities.txt"
grep '^Cap' "/proc/$PROVIDER_PID/status" > "$OUT/provider_capabilities.txt"
run_as p7requester sh -c 'id; grep "^Cap" /proc/self/status' > "$OUT/requester_capabilities.txt" 2>&1
run_as p7hostile sh -c 'id; grep "^Cap" /proc/self/status' > "$OUT/hostile_capabilities.txt" 2>&1
run_as p7requester sh -c 'ip addr; ip route' > "$OUT/requester_network.txt" 2>&1
run_as p7hostile sh -c 'ip addr; ip route' > "$OUT/hostile_network.txt" 2>&1

python - "$TOKEN" "$BROKER_PID" "$PROVIDER_PID" > "$OUT/process_secret_scan.txt" <<'PY'
from pathlib import Path
import hashlib
import sys

token = Path(sys.argv[1]).read_bytes().strip()
print("TOKEN_SHA256=" + hashlib.sha256(token).hexdigest())
for label, pid in (("BROKER", sys.argv[2]), ("PROVIDER", sys.argv[3])):
    cmdline = Path(f"/proc/{pid}/cmdline").read_bytes()
    environ = Path(f"/proc/{pid}/environ").read_bytes()
    print(f"{label}_CMDLINE_CONTAINS_TOKEN={str(token in cmdline).lower()}")
    print(f"{label}_ENVIRON_CONTAINS_TOKEN={str(token in environ).lower()}")
PY
grep -q 'BROKER_CMDLINE_CONTAINS_TOKEN=false' "$OUT/process_secret_scan.txt"
grep -q 'BROKER_ENVIRON_CONTAINS_TOKEN=false' "$OUT/process_secret_scan.txt"
grep -q 'PROVIDER_CMDLINE_CONTAINS_TOKEN=false' "$OUT/process_secret_scan.txt"
grep -q 'PROVIDER_ENVIRON_CONTAINS_TOKEN=false' "$OUT/process_secret_scan.txt"

# Positive control: authorized requester can cause the protected effect only through broker -> runtime -> provider.
run_as p7requester python "$CLIENT" --socket "$SOCKET" --request \
  '{"action":"mutate","resource":"X","expected_version":0,"new_value":"positive-control","possible_effects":["MODIFY(X)","PROVENANCE(X)"]}' \
  > "$OUT/positive_control.json" 2> "$OUT/positive_control.stderr"
python - "$OUT/positive_control.json" <<'PY'
import json, sys
p = json.load(open(sys.argv[1], encoding="utf-8"))
assert p["stage"] == "execution"
assert p["authorization_allowed"] is True
assert p["binding_allowed"] is True
assert p["start_allowed"] is True
assert p["admission_allowed"] is True
assert p["execution_occurred"] is True
assert p["execution_reason"] == "executed"
assert p["bound_capability_id"] == "p7-http-cap-X"
assert p["bound_target_identity"] == "X"
canonical = json.loads(p["canonical_operation"])
assert canonical == {
    "expected_version": 0,
    "new_value": "positive-control",
    "operation_type": "http_cas_put",
    "possible_effects": ["MODIFY(X)", "PROVENANCE(X)"],
    "resource": "X",
}
PY
python - "$PROVIDER_DB" <<'PY'
import sqlite3, sys
c = sqlite3.connect(sys.argv[1])
row = c.execute("SELECT value, version, last_admission_id, last_operation_digest FROM resources WHERE resource='X'").fetchone()
assert row is not None and row[0] == "positive-control" and row[1] == 1 and row[2] and row[3]
PY

# Neither untrusted identity can read or write the credential, provider DB, or control ledger.
for user in p7requester p7hostile; do
  set +e
  run_as "$user" cat "$TOKEN" >"$OUT/${user}_read_token.stdout" 2>"$OUT/${user}_read_token.stderr"
  READ_TOKEN_RC=$?
  run_as "$user" sh -c "printf x >> '$PROVIDER_DB'" >"$OUT/${user}_write_provider_db.stdout" 2>"$OUT/${user}_write_provider_db.stderr"
  WRITE_PROVIDER_RC=$?
  run_as "$user" sh -c "printf x >> '$LEDGER'" >"$OUT/${user}_write_ledger.stdout" 2>"$OUT/${user}_write_ledger.stderr"
  WRITE_LEDGER_RC=$?
  set -e
  printf '%s\n' "$READ_TOKEN_RC" > "$OUT/${user}_read_token.exit"
  printf '%s\n' "$WRITE_PROVIDER_RC" > "$OUT/${user}_write_provider_db.exit"
  printf '%s\n' "$WRITE_LEDGER_RC" > "$OUT/${user}_write_ledger.exit"
  [[ "$READ_TOKEN_RC" -ne 0 ]]
  [[ "$WRITE_PROVIDER_RC" -ne 0 ]]
  [[ "$WRITE_LEDGER_RC" -ne 0 ]]
done

# Trusted process separation: broker has credential but no direct provider DB path; provider has no ledger write path.
set +e
run_as p7broker sh -c "printf broker-direct >> '$PROVIDER_DB'" >"$OUT/broker_direct_provider_db.stdout" 2>"$OUT/broker_direct_provider_db.stderr"
BROKER_DIRECT_PROVIDER_RC=$?
run_as p7provider sh -c "printf provider-direct >> '$LEDGER'" >"$OUT/provider_direct_ledger.stdout" 2>"$OUT/provider_direct_ledger.stderr"
PROVIDER_DIRECT_LEDGER_RC=$?
set -e
printf '%s\n' "$BROKER_DIRECT_PROVIDER_RC" > "$OUT/broker_direct_provider_db.exit"
printf '%s\n' "$PROVIDER_DIRECT_LEDGER_RC" > "$OUT/provider_direct_ledger.exit"
[[ "$BROKER_DIRECT_PROVIDER_RC" -ne 0 ]]
[[ "$PROVIDER_DIRECT_LEDGER_RC" -ne 0 ]]

# /proc-root escape cannot recover the credential from another UID's broker process.
for user in p7requester p7hostile; do
  set +e
  run_as "$user" cat "/proc/$BROKER_PID/root$TOKEN" >"$OUT/${user}_proc_token.stdout" 2>"$OUT/${user}_proc_token.stderr"
  PROC_TOKEN_RC=$?
  set -e
  printf '%s\n' "$PROC_TOKEN_RC" > "$OUT/${user}_proc_token.exit"
  [[ "$PROC_TOKEN_RC" -ne 0 ]]
done

# Loopback endpoint is discoverable/reachable, but without the capability credential it is not effect-capable.
set +e
run_as p7requester curl -sS -w '\n%{http_code}\n' \
  -X POST "$PROVIDER_ENDPOINT/cas" -H 'Content-Type: application/json' --data '{}' \
  > "$OUT/requester_direct_provider_noauth.response" 2> "$OUT/requester_direct_provider_noauth.stderr"
REQUESTER_HTTP_RC=$?
run_as p7hostile curl -sS -w '\n%{http_code}\n' \
  -X POST "$PROVIDER_ENDPOINT/cas" -H 'Authorization: Bearer forged' -H 'Content-Type: application/json' --data '{}' \
  > "$OUT/hostile_direct_provider_forged.response" 2> "$OUT/hostile_direct_provider_forged.stderr"
HOSTILE_HTTP_RC=$?
run_as p7requester curl -sS -w '\n%{http_code}\n' \
  "$PROVIDER_ENDPOINT/state?resource=X" \
  > "$OUT/requester_direct_state_noauth.response" 2> "$OUT/requester_direct_state_noauth.stderr"
REQUESTER_GET_RC=$?
set -e
[[ "$REQUESTER_HTTP_RC" -eq 0 ]]
[[ "$HOSTILE_HTTP_RC" -eq 0 ]]
[[ "$REQUESTER_GET_RC" -eq 0 ]]
[[ "$(tail -n 1 "$OUT/requester_direct_provider_noauth.response")" = "401" ]]
[[ "$(tail -n 1 "$OUT/hostile_direct_provider_forged.response")" = "401" ]]
[[ "$(tail -n 1 "$OUT/requester_direct_state_noauth.response")" = "401" ]]

# Unauthorized peer cannot turn self-declared identity or credential-shaped payload into authority.
run_as p7hostile python "$CLIENT" --socket "$SOCKET" --request \
  '{"action":"mutate","declared_principal":"alice","provider_token":"forged","capability_id":"p7-http-cap-X","resource":"X","expected_version":1,"new_value":"hostile","possible_effects":["MODIFY(X)","PROVENANCE(X)"]}' \
  > "$OUT/hostile_broker_forgery.json" 2> "$OUT/hostile_broker_forgery.stderr"
python - "$OUT/hostile_broker_forgery.json" <<'PY'
import json, sys
p = json.load(open(sys.argv[1], encoding="utf-8"))
assert p["stage"] == "authorize"
assert p["authorization_allowed"] is False
assert p["authorization_reason"] == "missing_authentication_context"
PY

# Caller-supplied provider/credential/capability/admission routing fields cannot redirect the trusted path.
run_as p7requester python "$CLIENT" --socket "$SOCKET" --request \
  '{"action":"mutate","provider_url":"http://127.0.0.1:1","provider_token":"attacker","provider_id":"attacker","binding_id":"attacker-binding","capability_id":"attacker-cap","admission_id":"forged-admission","resource":"X","expected_version":1,"new_value":"trusted-route","possible_effects":["MODIFY(X)","PROVENANCE(X)"]}' \
  > "$OUT/hostile_routing_fields.json" 2> "$OUT/hostile_routing_fields.stderr"
python - "$OUT/hostile_routing_fields.json" <<'PY'
import json, sys
p = json.load(open(sys.argv[1], encoding="utf-8"))
assert p["stage"] == "execution" and p["execution_occurred"] is True
assert p["bound_capability_id"] == "p7-http-cap-X"
assert p["binding_id"] == "p7-http-binding-X"
assert p["admission_id"] != "forged-admission"
canonical = json.loads(p["canonical_operation"])
assert set(canonical) == {"expected_version", "new_value", "operation_type", "possible_effects", "resource"}
assert canonical["resource"] == "X" and canonical["new_value"] == "trusted-route"
PY
python - "$PROVIDER_DB" <<'PY'
import sqlite3, sys
c = sqlite3.connect(sys.argv[1])
row = c.execute("SELECT value, version FROM resources WHERE resource='X'").fetchone()
assert row == ("trusted-route", 2)
PY

# Cross-domain/target pivot is stopped at trusted binding before an attempt/effect path exists.
run_as p7requester python "$CLIENT" --socket "$SOCKET" --request \
  '{"action":"mutate","resource":"Y","expected_version":0,"new_value":"pivot","possible_effects":["MODIFY(Y)","PROVENANCE(Y)"]}' \
  > "$OUT/target_pivot.json" 2> "$OUT/target_pivot.stderr"
python - "$OUT/target_pivot.json" <<'PY'
import json, sys
p = json.load(open(sys.argv[1], encoding="utf-8"))
assert p["authorization_allowed"] is True
assert p["stage"] == "binding"
assert p["binding_allowed"] is False
assert p["binding_reason"] == "binding_target_mismatch"
assert "attempt_id" not in p and "admission_id" not in p
PY

# Unknown and overbroad effect models cannot reach the provider.
run_as p7requester python "$CLIENT" --socket "$SOCKET" --request \
  '{"action":"mutate","resource":"X","expected_version":2,"new_value":"unknown-effects"}' \
  > "$OUT/unknown_effects.json" 2> "$OUT/unknown_effects.stderr"
run_as p7requester python "$CLIENT" --socket "$SOCKET" --request \
  '{"action":"mutate","resource":"X","expected_version":2,"new_value":"overbroad","possible_effects":["MODIFY(X)","PROVENANCE(X)","MODIFY(Y)"]}' \
  > "$OUT/overbroad_effects.json" 2> "$OUT/overbroad_effects.stderr"
python - "$OUT/unknown_effects.json" "$OUT/overbroad_effects.json" <<'PY'
import json, sys
u = json.load(open(sys.argv[1], encoding="utf-8"))
o = json.load(open(sys.argv[2], encoding="utf-8"))
assert u["stage"] == "admission" and u["admission_allowed"] is False and u["admission_reason"] == "unknown_possible_effects"
assert o["stage"] == "admission" and o["admission_allowed"] is False and o["admission_reason"] == "effect_model_mismatch"
PY

# Replacement and continuation-shaped fields cannot change the exact operation or execute an admission directly.
run_as p7requester python "$CLIENT" --socket "$SOCKET" --request \
  '{"action":"mutate","resource":"X","expected_version":2,"new_value":"O1","replacement_resource":"Y","replacement_value":"O2","replacement_possible_effects":["MODIFY(Y)","PROVENANCE(Y)"],"possible_effects":["MODIFY(X)","PROVENANCE(X)"]}' \
  > "$OUT/o1_replacement_o2.json" 2> "$OUT/o1_replacement_o2.stderr"
python - "$OUT/o1_replacement_o2.json" <<'PY'
import json, sys
p = json.load(open(sys.argv[1], encoding="utf-8"))
assert p["stage"] == "execution" and p["execution_occurred"] is True
canonical = json.loads(p["canonical_operation"])
assert canonical["resource"] == "X" and canonical["new_value"] == "O1"
assert "O2" not in p["canonical_operation"]
PY
O1_ADMISSION_ID=$(python -c 'import json,sys; print(json.load(open(sys.argv[1]))["admission_id"])' "$OUT/o1_replacement_o2.json")
run_as p7requester python "$CLIENT" --socket "$SOCKET" --request \
  "{\"action\":\"execute_admission\",\"admission_id\":\"$O1_ADMISSION_ID\",\"resource\":\"Y\",\"new_value\":\"O2\"}" \
  > "$OUT/bypass_admission.json" 2> "$OUT/bypass_admission.stderr"
python - "$OUT/bypass_admission.json" <<'PY'
import json, sys
p = json.load(open(sys.argv[1], encoding="utf-8"))
assert p["stage"] == "request" and p["request_valid"] is False and p["reason"] == "unknown_action"
PY

python - "$PROVIDER_DB" > "$OUT/final_provider_state.txt" <<'PY'
import sqlite3, sys
c = sqlite3.connect(sys.argv[1])
rows = c.execute("SELECT resource, value, version, last_admission_id, last_operation_digest, last_mutation_id FROM resources ORDER BY resource").fetchall()
assert len(rows) == 1
assert rows[0][0] == "X" and rows[0][1] == "O1" and rows[0][2] == 3
for row in rows:
    print("|".join("" if value is None else str(value) for value in row))
PY

# Scan evidence without ever putting the secret on a command line; no evidence/log may contain the bearer value.
python - "$TOKEN" "$OUT" > "$OUT/evidence_secret_scan.txt" <<'PY'
from pathlib import Path
import sys

token = Path(sys.argv[1]).read_bytes().strip()
root = Path(sys.argv[2])
hits = []
for path in root.rglob("*"):
    if not path.is_file() or path.name == "evidence_secret_scan.txt":
        continue
    try:
        data = path.read_bytes()
    except OSError:
        continue
    if token and token in data:
        hits.append(str(path))
print("TOKEN_LEAK_FILE_COUNT=" + str(len(hits)))
for path in hits:
    print("TOKEN_LEAK_FILE=" + path)
PY
grep -q '^TOKEN_LEAK_FILE_COUNT=0$' "$OUT/evidence_secret_scan.txt"

set +x
find "$OUT" -type f ! -name SHA256SUMS -print0 | sort -z | xargs -0 sha256sum > "$OUT/SHA256SUMS"
