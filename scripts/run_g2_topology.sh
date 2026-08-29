#!/usr/bin/env bash
set -euo pipefail

OUT=${1:-g2-topology-evidence}
rm -rf "$OUT"
mkdir -p "$OUT"

ROOT=$(pwd)
PRIVATE_ROOT=$(mktemp -d /tmp/agency-kernel-g2-private.XXXXXX)
SOCKET_ROOT=$(mktemp -d /tmp/agency-kernel-g2-ipc.XXXXXX)
TARGET="$PRIVATE_ROOT/target"
LEDGER="$PRIVATE_ROOT/ledger.sqlite"
SOCKET="$SOCKET_ROOT/broker.sock"
READY="$SOCKET_ROOT/ready"

cleanup() {
  if [[ -n "${BROKER_PID:-}" ]] && kill -0 "$BROKER_PID" 2>/dev/null; then
    python scripts/g2_ipc_client.py --socket "$SOCKET" --request '{"action":"shutdown"}' >/dev/null 2>&1 || true
    wait "$BROKER_PID" 2>/dev/null || true
  fi
  sudo userdel -f g2requester 2>/dev/null || true
  sudo userdel -f g2hostile 2>/dev/null || true
  rm -rf "$PRIVATE_ROOT" "$SOCKET_ROOT"
}
trap cleanup EXIT

sudo userdel -f g2requester 2>/dev/null || true
sudo userdel -f g2hostile 2>/dev/null || true
sudo useradd --no-create-home --shell /usr/sbin/nologin g2requester
sudo useradd --no-create-home --shell /usr/sbin/nologin g2hostile
REQUESTER_UID=$(id -u g2requester)
HOSTILE_UID=$(id -u g2hostile)

chmod 700 "$PRIVATE_ROOT"
chmod 777 "$SOCKET_ROOT"
mkdir -p "$TARGET"
chmod 700 "$TARGET"

python scripts/g2_broker.py \
  --socket "$SOCKET" \
  --ledger "$LEDGER" \
  --target "$TARGET" \
  --authorized-uid "$REQUESTER_UID" \
  --ready-file "$READY" \
  >"$OUT/broker.stdout" 2>"$OUT/broker.stderr" &
BROKER_PID=$!

for _ in $(seq 1 100); do
  [[ -S "$SOCKET" && -f "$READY" ]] && break
  sleep 0.05
done
[[ -S "$SOCKET" && -f "$READY" ]]

{
  echo "REQUESTER_UID=$REQUESTER_UID"
  echo "HOSTILE_UID=$HOSTILE_UID"
  echo "BROKER_PID=$BROKER_PID"
  echo "PRIVATE_ROOT=$PRIVATE_ROOT"
  echo "TARGET=$TARGET"
  echo "LEDGER=$LEDGER"
  echo "SOCKET=$SOCKET"
  stat -c 'PRIVATE_ROOT_MODE=%a OWNER=%u GROUP=%g' "$PRIVATE_ROOT"
  stat -c 'TARGET_MODE=%a OWNER=%u GROUP=%g' "$TARGET"
  stat -c 'SOCKET_MODE=%a OWNER=%u GROUP=%g' "$SOCKET"
  findmnt -T "$TARGET" -o TARGET,SOURCE,FSTYPE,OPTIONS
  findmnt -T "$LEDGER" -o TARGET,SOURCE,FSTYPE,OPTIONS || true
  ss -ltnup || true
} > "$OUT/topology.txt" 2>&1

run_as() {
  local user=$1
  shift
  sudo -u "$user" env PYTHONPATH="$ROOT" "$@"
}

# Positive control: authenticated OS peer uid, exact admission, Broker-owned target effect.
run_as g2requester python scripts/g2_ipc_client.py --socket "$SOCKET" --request \
  '{"action":"mutate","resource":"X","value":"positive-control","possible_effects":["MODIFY(X)"]}' \
  > "$OUT/positive_control.json" 2> "$OUT/positive_control.stderr"
grep -q '"allowed": true' "$OUT/positive_control.json"
grep -q '^positive-control$' "$TARGET/X"

# Hostile executor cannot directly mutate target.
set +e
run_as g2hostile sh -c "printf hostile-direct > '$TARGET/X'" >"$OUT/direct_target.stdout" 2>"$OUT/direct_target.stderr"
DIRECT_TARGET_RC=$?
set -e
printf '%s\n' "$DIRECT_TARGET_RC" > "$OUT/direct_target.exit"
[[ "$DIRECT_TARGET_RC" -ne 0 ]]
grep -q '^positive-control$' "$TARGET/X"

# Hostile executor cannot write the control ledger.
set +e
run_as g2hostile sh -c "printf hostile-ledger >> '$LEDGER'" >"$OUT/direct_ledger.stdout" 2>"$OUT/direct_ledger.stderr"
DIRECT_LEDGER_RC=$?
set -e
printf '%s\n' "$DIRECT_LEDGER_RC" > "$OUT/direct_ledger.exit"
[[ "$DIRECT_LEDGER_RC" -ne 0 ]]

# Request-payload identity does not substitute for authenticated peer identity.
run_as g2hostile python scripts/g2_ipc_client.py --socket "$SOCKET" --request \
  '{"action":"mutate","declared_principal":"alice","resource":"X","value":"forged-identity","possible_effects":["MODIFY(X)"]}' \
  > "$OUT/forged_identity.json" 2> "$OUT/forged_identity.stderr"
grep -q '"allowed": false' "$OUT/forged_identity.json"
grep -q 'missing_authentication_context' "$OUT/forged_identity.json"
grep -q '^positive-control$' "$TARGET/X"

# Fake Broker credential fields do not create authenticated identity.
run_as g2hostile python scripts/g2_ipc_client.py --socket "$SOCKET" --request \
  '{"action":"mutate","broker_token":"forged","declared_principal":"alice","resource":"X","value":"forged-token","possible_effects":["MODIFY(X)"]}' \
  > "$OUT/forged_broker_credential.json" 2> "$OUT/forged_broker_credential.stderr"
grep -q '"allowed": false' "$OUT/forged_broker_credential.json"
grep -q '^positive-control$' "$TARGET/X"

# Unknown possible effects reach admission under an authenticated requester and deny pre-effect.
run_as g2requester python scripts/g2_ipc_client.py --socket "$SOCKET" --request \
  '{"action":"mutate","resource":"X","value":"unknown-effects"}' \
  > "$OUT/unknown_effects.json" 2> "$OUT/unknown_effects.stderr"
grep -q '"stage": "admission"' "$OUT/unknown_effects.json"
grep -q 'unknown_possible_effects' "$OUT/unknown_effects.json"
grep -q '^positive-control$' "$TARGET/X"

# Malformed/over-broad declaration cannot pass the boundary model.
run_as g2requester python scripts/g2_ipc_client.py --socket "$SOCKET" --request \
  '{"action":"mutate","resource":"X","value":"overbroad","possible_effects":["MODIFY(X)","MODIFY(Y)"]}' \
  > "$OUT/overbroad_effects.json" 2> "$OUT/overbroad_effects.stderr"
grep -q '"allowed": false' "$OUT/overbroad_effects.json"
grep -q '^positive-control$' "$TARGET/X"

# Alternate host/proc path to target is not writable by hostile executor.
PROC_TARGET="/proc/$BROKER_PID/root$TARGET/X"
set +e
run_as g2hostile sh -c "printf proc-escape > '$PROC_TARGET'" >"$OUT/proc_target.stdout" 2>"$OUT/proc_target.stderr"
PROC_TARGET_RC=$?
set -e
printf '%s\n' "$PROC_TARGET_RC" > "$OUT/proc_target.exit"
[[ "$PROC_TARGET_RC" -ne 0 ]]
grep -q '^positive-control$' "$TARGET/X"

# No TCP Broker target API is exposed by the harness.
set +e
run_as g2hostile python -c 'import socket; s=socket.socket(); s.settimeout(1); s.connect(("127.0.0.1", 43177))' \
  >"$OUT/network_target.stdout" 2>"$OUT/network_target.stderr"
NETWORK_RC=$?
set -e
printf '%s\n' "$NETWORK_RC" > "$OUT/network_target.exit"
[[ "$NETWORK_RC" -ne 0 ]]

{
  printf 'TARGET_FINAL='; cat "$TARGET/X"
  printf 'TARGET_SHA256='; sha256sum "$TARGET/X" | awk '{print $1}'
  printf 'LEDGER_SHA256='; sha256sum "$LEDGER" | awk '{print $1}'
} > "$OUT/final_state.txt"

find "$OUT" -type f ! -name SHA256SUMS -print0 | sort -z | xargs -0 sha256sum > "$OUT/SHA256SUMS"
